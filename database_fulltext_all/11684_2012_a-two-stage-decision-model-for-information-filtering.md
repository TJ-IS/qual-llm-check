---
otero_id: 11684
otero_key: "PBPDB8UV"
title: "A two-stage decision model for information filtering"
authors: "Yuefeng Li; Xujuan Zhou; Peter Bruza; Yue Xu; Raymond Y.K. Lau"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A two-stage decision model for information <sup>fi</sup>ltering

Yuefeng Li <sup>a,</sup>⁎, Xujuan Zhou <sup>a</sup>, Peter Bruza <sup>b</sup>, Yue Xu <sup>a</sup>, Raymond Y.K. Lau <sup>c</sup>

<sup>a</sup> School of Electrical Engineering and Computer Science, Queensland University of Technology, Brisbane, QLD 4001, Australia

<sup>b</sup> School of Information Systems, Queensland University of Technology, Brisbane, QLD 4001, Australia

<sup>c</sup> Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon Hong Kong SAR, China

## a r t i c l e i n f o

Article history: Received 8 November 2010 Received in revised form 25 October 2011 Accepted 4 November 2011 Available online 12 November 2011

Keywords: Information <sup>fi</sup>ltering Text classi<sup>fi</sup>cation User pro<sup>fi</sup>les Pattern mining Decision models

## a b s t r a c t

Information mismatch and overload are two fundamental issues in<sup>fl</sup>uencing the effectiveness of information <sup>fi</sup>ltering systems. Even though both term-based and pattern-based approaches have been proposed to address the issues, neither of these approaches alone can provide a satisfactory decision for determining the relevant information. This paper presents a novel two-stage decision model for solving the issues. The <sup>fi</sup>rst stage is a novel rough analysis model to address the overload problem. The second stage is a pattern taxonomy mining model to address the mismatch problem. The experimental results on RCV1 and TREC <sup>fi</sup>ltering topics show that the proposed model signi<sup>fi</sup>cantly outperforms the state-of-the-art <sup>fi</sup>ltering systems. © 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Knowledge workers always need precise and high-quality information to effectively carry out their tasks within organizational contexts [8]. Nevertheless, the massive amount of user-generated content in the era of Web 2.0 has made it increasingly more dif<sup>fi</sup>cult for knowledge workers to effectively utilize information to achieve various organizational goals. For instance, the huge volume of online <sup>fi</sup>nancial news contributed by <sup>fi</sup>nancial experts or general investors on a daily basis may far exceed the information processing capacity of a <sup>fi</sup>nancial analyst (i.e. a knowledge worker) who needs to scan through the news to make vital <sup>fi</sup>nancial investment decisions.

An Information Filtering (IF) [5] system monitors an incoming information (document) stream to make binary decisions for relevant information (documents) in order to meet user information needs. IF systems were originally considered to have the same function as Information Retrieval (IR) systems. Unlike IR systems, IF systems were commonly personalized to support long-term information needs of users [5]. The main distinction between IR and IF was that IR systems used “queries” but IF systems used “user pro<sup>fi</sup>les”.

There are two fundamental issues with regards to the effectiveness of information <sup>fi</sup>ltering: mismatch and overload. Mismatch means some useful or interesting information has been omitted (loss of recall), whereas, overload means some <sup>fi</sup>ltered information is not relevant (loss of precision). The problem of “mismatch” occurs when the terms in a query do not match those found in a document, even though the document is relevant to the query.

The representation of the user information needs is variously referred to as user pro<sup>fi</sup>les, or topic pro<sup>fi</sup>les. As the quality of the pro-<sup>fi</sup>les directly in<sup>fl</sup>uences the quality of information <sup>fi</sup>ltering, the issue of how to build accurate, reliable pro<sup>fi</sup>les is a crucial concern [31]. The tasks of the <sup>fi</sup>ltering track in TREC included batch and routing <sup>fi</sup>ltering, and adaptive <sup>fi</sup>ltering [33]. A batch <sup>fi</sup>ltering system uses a retrieval algorithm to score each incoming document. If the score is greater than a speci<sup>fi</sup>ed threshold, then the document is delivered to the user. The routing <sup>fi</sup>ltering systems are more similar to the retrieval systems, the pro<sup>fi</sup>le remains constant and the task is to match an incoming stream of documents to a set of pro<sup>fi</sup>les. Routing systems need to return a ranked list of documents. Adaptive <sup>fi</sup>ltering involves feedback to dynamically adapt IF systems [17,49]. The pro<sup>fi</sup>le is adapted dynamically based on feedback received. This paper is concerned with routing.

Most pro<sup>fi</sup>les are term-based, such as Rocchio and probabilistic models [3], rough set models [23], and BM25 and SVM based <sup>fi</sup>ltering models [35]. The advantages of term-based pro<sup>fi</sup>les are ef<sup>fi</sup>cient computational performance as well as mature theories for term weighting, which have emerged over the last couple of decades from the IR and machine learning communities. However, term-based pro<sup>fi</sup>les suffer from the problems of polysemy and synonymy. In addition, the threshold for accepting or rejecting documents is usually determined empirically. As IF systems are sensitive to data sets, it is a challenge to set the optimal threshold.

Over the years, the IR community has often held the hypothesis that phrases could perform better than using keywords only, as phrases are more discriminative and arguably carry more “semantics”. Many researchers illustrated that phrases are useful and crucial for query expansion in building good ranking functions [6,45]. Naturally, phrases have inferior statistical properties to words, and there are a large number of redundant and noisy phrases among them [38,39]. Therefore, it is a challenge to <sup>fi</sup>nd only the useful phrases for text classi<sup>fi</sup>cation and information <sup>fi</sup>ltering [27].

Sequential closed patterns used in data mining have turned out to be a promising alternative to phrases [13,47] because patterns exhibit good statistical properties like words. To overcome the disadvantages of phrase-based approaches, pattern-based approaches (or pattern taxonomy models (PTMs) [25,46,47]) have been proposed for IF. These pattern-based approaches have shown encouraging improvements on effectiveness, but at the expense of computational ef<sup>fi</sup>ciency. In regard to the aforementioned problem of redundancy and noise, a PTM adopts the concept of closed patterns. However, it is still a challenging issue for a PTM to deal with low frequency patterns because the measures used in data mining to learn pro<sup>fi</sup>les turn out to be not suitable in the <sup>fi</sup>ltering stage. By way of illustration, given a speci<sup>fi</sup>ed topic, a highly frequent pattern is usually a general pattern, and a speci<sup>fi</sup>c pattern usually has a low frequency. This parallels the situation in term indexing where words of high frequency (stop words) or very low frequency (uncommon words conveying signi<sup>fi</sup>- cant information) are not considered useful.

To learn the accurate and reliable user pro<sup>fi</sup>les, a relevance feedback approach is utilized for acquiring user pro<sup>fi</sup>les, that uses a training set, including both the positive and the negative documents. Usually, only a small portion of the documents are positive for the user information needs, but the number of negative samples can be huge. Therefore, the computation of user pro<sup>fi</sup>les using only documents with positive relevance feedback has often been emphasized [12,26,54]. On the other hand, recent research attempting to exploit the negative relevance feedback information has not been promising [16,43]. Therefore, this emphasizes the important issue of how to effectively interpret user pro<sup>fi</sup>les with only positive feedback.

In this research, a two-stage decision model is proposed to address the limitations of term-based approaches and pattern-based approaches. The <sup>fi</sup>rst stage is called the “topic <sup>fi</sup>ltering”, and the second stage is called the “pattern mining”. This study will only use the positive feedback at the training stage for both the topic <sup>fi</sup>ltering and the pattern mining. In the topic <sup>fi</sup>ltering stage, the system tries to quickly make decisions to <sup>fi</sup>lter out the most likely irrelevant information based on term-based pro<sup>fi</sup>les to solve the mismatch problem. The intention after the <sup>fi</sup>rst stage is that only a relatively small amount of potentially highly relevant documents remain as input to the second stage. The objective of the second stage is to solve the overload problem by using a pattern taxonomy mining approach to make more precise decisions. It aims to assign large weights to the most likely relevant documents by exploiting patterns based on the pattern taxonomy. This stage is precision oriented. Since only a relatively small number of documents are involved, the previously mentioned computational cost can be markedly reduced. In addition, the setting of the threshold is theoretically, rather than empirically, determined.

The remainder of the paper is organized as follows. Section 2 highlights previous research in related areas, information <sup>fi</sup>ltering and text mining, and compares this research to that presented here. Section 3 introduces the existing approaches for setting thresholds theoretically. Section 4 discusses the new method for setting thresholds for the <sup>fi</sup>rst stage, topic <sup>fi</sup>ltering. Section 5 discusses the pattern taxonomy mining for the second stage of information <sup>fi</sup>ltering. The empirical results are reported in Section 6. Section 7 describes the <sup>fi</sup>ndings of the experiments and discusses the results. Concluding remarks are outlined in Section 8.

## 2. Related work

The objective of information <sup>fi</sup>ltering is to reduce users' information load concerning personal user pro<sup>fi</sup>les. User pro<sup>fi</sup>le construction is one of most challenging tasks within the IF <sup>fi</sup>eld. The user pro<sup>fi</sup>les can be constructed using a variety of learning techniques.

Traditional IF uses single-vector or multi-vector models that produce one term-weight [39], more than one term-weight vectors [31] or multiple representations of documents [24] to represent the relevant information of the topic of likely interest for a user. There is a term “independence” assumption in those models. In contrast, data mining-based models try to discover the association between terms and categories (for example, a term or a set of terms). These association relationships can be described as association rules in data mining.

As mentioned in the introduction, most methods for describing user pro<sup>fi</sup>les are term-based, and the advantages of term-based pro-<sup>fi</sup>les are ef<sup>fi</sup>cient computational performance as well as mature theories for term weighting. Term-based IF models have been developed recently which take into consideration more constraints in relation to the labeled data in training sets. For instance, Rocchio-style classi-<sup>fi</sup>ers [20]; ranking SVM [32]; and BM25 for structured documents [36]. However, the research on term-based IF models has arguably hit somewhat of a wall in terms of performance improvement, possibly due to the ambiguity problem mentioned earlier.

A phrase based user pro<sup>fi</sup>le model that uses multiple words (phrases) as features is therefore proposed to solve the semantic ambiguity problem. It is believed that the simple term-based representation of the pro<sup>fi</sup>le is usually inadequate, because single words are rarely suf<sup>fi</sup>ciently speci<sup>fi</sup>c for accurate discrimination [42]. In general, phrases carry more speci<sup>fi</sup>c content than single words. Fuhr [10] investigated the probabilistic models in IR and pointed out that a dependent model for phrases is not suf<sup>fi</sup>cient, because only the occurrence of the phrase components in a document is considered, but not the syntactical structure of the phrases. Moreover, the certainty of identi<sup>fi</sup>cation should also be regarded, such as, whether the words occur adjacent to each other or only within the same paragraph. In [1], they apply data mining techniques to text analysis by extracting co-occurring terms as descriptive phrases from document collections. However, the effectiveness of the text mining systems using phrases as text representation showed no noteworthy improvement. The likely reason is that a phrase-based method has a “lower consistency of assignment and a lower document frequency for terms” as mentioned in [18].

Arti<sup>fi</sup>cial intelligence based techniques such as machine-learning based techniques subsequently arrived on the scene. Machine learning is the study of computer algorithms that improve automatically through experience. Applications range from data mining programs that discover general rules in large data sets, to information <sup>fi</sup>ltering systems that automatically learn users' interests. Based on user feedback, machine-learning based systems tended to learn a map $f { : } D \to R$ such that $f ( d )$ corresponded to the relevance of a document d, where D denoted the set of incoming documents, R was the set of real numbers. To decrease the burden of on-line learning, a decomposition model for IF was presented in [31]. In this model, the map f was replaced by $f _ { 1 } \circ f _ { 2 } ,$ where $f _ { 1 } ( { f _ { 1 } } { : } D {  } \{ C _ { 1 } , { \ldots } , C _ { m } \} )$ , and $f _ { 2 } ( f _ { 2 } ; \{ C _ { 1 } , . . . ,$ $C _ { m } \} \to R )$ were maps, respectively; and $C _ { 1 } , . . . , C _ { m }$ were clusters. This model tried to represent user pro<sup>fi</sup>les using a set of clusters based on a kind of classi<sup>fi</sup>cation method, such as the neural network [30].

Linear classi<sup>fi</sup>cation methods have linear decision boundaries between positive and negative classes. The most popular text classi<sup>fi</sup>- cation algorithms, such as the Support Vector Machine (SVM), K Nearest Neighbours (K-NN), and logistic regression have been used for <sup>fi</sup>ltering tasks [7,15,51].

Usually, users do not know how to use or do not like to use classi-<sup>fi</sup>cation structures for their information needs. They simply want IF systems to return relevant or interesting information. Rough set based decision models were developed for this purpose. Such models represent pro<sup>fi</sup>les using three clusters: positive region, boundary region and negative region [23,53]. Even though rough set based models have emerged from the <sup>fi</sup>eld of data mining, their principle objective is very closely aligned to the aim of the <sup>fi</sup>ltering track in TREC [35]. This track measures the ability of IF systems to build pro-<sup>fi</sup>les using sets of training documents to separate relevant and nonrelevant documents.

In the <sup>fi</sup>eld of text mining, pattern mining techniques can be used to <sup>fi</sup>nd various text patterns, such as co-occurring terms and multiple grams, maximal frequent patterns, and closed patterns, for building up a representation with these new types of features. Mining maximal frequent patterns [4] was also proposed to reduce the time complexity of mining all frequent patterns, where an itemset (or a pattern) was described as maximal frequent if it had no superset that was frequent. The similar idea of maximal association rules, was also used for text mining [2,9], where users provided categories for <sup>fi</sup>nding the maximal rules they wanted. The notion of closed patterns has its origins in the mathematical theory of Formal Concept Analysis introduced in [11]. Closed patterns were used to prune some smaller redundant patterns [44] and have been used for improving the effectiveness of text mining [46].

Many other text mining methods have been developed in order to achieve the goal of information <sup>fi</sup>ltering or Web personalization [27]. Term-based ontology mining methods also provided some ideas for text representations. For example, hierarchical clustering [28] was used to determine synonymy and hyponymy relations between keywords. Also, the pattern evolution technique was introduced in [22] in order to improve the performance of term-based ontology mining.

Pattern-based approaches have shown encouraging performance for IF, but at the expense of computational ef<sup>fi</sup>ciency. It is still a challenging issue for pattern-based methods to deal with low frequency patterns because the measures used from data mining (e.g., “support” and “con<sup>fi</sup>dences”) to learn pro<sup>fi</sup>les turned out to be not suitable in the <sup>fi</sup>ltering stage. By way of illustration, a short pattern (normally a highly frequent pattern with large support) is usually a general pattern, or a large pattern (a low frequent pattern with small support) could be a speci<sup>fi</sup>c one.

The following comparisons drawn from the literature place pattern-based methods and term-based IF systems in perspective: (i) Pattern-based methods are more computationally intensive to train; (ii) sequential patterns are more effective than normal patterns; (iii) closed sequential patterns are better than sequential patterns; and (iv) too much noise in the input data (incoming document stream) adversely affects pattern-based systems.

Despite many attempts to develop Information Filtering (IF) systems so that the goal of information seeking can be realized [17,41], a satisfactory solution has not yet emerged to cope with the extraordinary speed of information generation in the era of Web 2.0. According to the previous empirical <sup>fi</sup>ndings, the excessive volume of information and the irrelevance or unimportance of much of that information were the two main causes of information overload perceived by knowledge workers [8].

The main objective of the research work presented in this paper is to develop a novel IF model which integrates topic <sup>fi</sup>ltering and pattern mining strategies to provide more precise document <sup>fi</sup>ltering. The idea of integrating term-based approaches (topic <sup>fi</sup>ltering) and pattern-based approaches (pattern taxonomy mining) for IF systems has evolved from these two well established, but largely disparate <sup>fi</sup>elds. This proposed method intends to exploit the advantages of term-based approaches (IR) and pattern-based approaches (data mining) within one system.

## 3. Thresholds for information <sup>fi</sup>ltering systems

As mentioned previously, the <sup>fi</sup>rst stage aims to quickly <sup>fi</sup>lter out likely non-relevant documents. As a result only a relatively small number of potentially relevant documents remain as input into the second stage. The objective of the second stage is to employ a pattern taxonomy mining approach to boost precision. As the mining is performed on a relatively small set of documents, the computational cost is markedly reduced.

The basic hypothesis for the <sup>fi</sup>rst stage is that incoming documents are likely non-relevant if they are not close to the feature descriptions of the positive documents in the training set. As mentioned in the introduction, thresholds for IF systems are usually determined empirically, because IF systems are sensitive to data sets. In this section, we analyze two existing approaches for determining thresholds theoretically by describing the features of positive documents in the training set.

Let D be a training set of documents, which consists of a set of positive documents, $D ^ { + }$ <sup>+</sup>; and a set of negative documents, D<sup>−</sup>. Let $T = \{ t _ { 1 } ,$ $t _ { 2 } , . . . , t _ { m } \}$ be a set of terms which are extracted from the set of positive documents, $D ^ { + }$

Given a training set, usually an IF model (e.g., Rocchio, BM25 or SVM) attempts to <sup>fi</sup>nd feature descriptions for both positive documents and negative documents in the training set. It then uses a technique to weaken the common feature descriptions of the positive documents and negative documents. For example, the Rocchio algorithm, which has been widely adopted in information retrieval [29], can be used to build a text representation of a training set. Each document d is represented as a vector d . First, the normalized document vectors of the positive documents and those of the negative documents are summed up, respectively. The topic pro<sup>fi</sup>les are then represented by combining these two parts. In the Rocchio algorithm, two parameters,α and β, are used to adjust the relevant impact of positive and negative training examples, respectively.

This kind of feature description denotes that incoming documents are likely relevant if they include all terms that are selected in the positive documents.

The obvious advantage of using the above approach is that the IF system can have a high precision if positive terms are selected correctly; however, the recall is very low. The interesting and hard question is how to <sup>fi</sup>nd suitable subsets of terms (or conditions) for deciding thresholds for IF systems.

For this question, a decision theory [50] has been used for IF systems in [23], and the theory has been further developed to a decision-rule based model for IF systems in [21,22]. The model tried to describe the possible boundary between the relevant documents and the non-relevant documents rather than to determine the suitable subsets of terms.

The decision-rule based model <sup>fi</sup>rstly represented documents as sets of terms, and classi<sup>fi</sup>ed incoming documents into three groups based on term distributions of the positive documents: the positive region, boundary region and negative region. It also provided associ ated decision rules for the partitioning of the incoming document stream into the three regions. This approach differs from many of the state-of-the-art methods that tend to set thresholds empirically.

Let d be an incoming document. The basic assumption for the decision-rule based model is that d is possibly relevant $\mathbf { f } \exists d _ { i } \in { \cal D } ^ { + }$ such that $d \supseteq d _ { i } .$ The set of all documents d such that $d _ { i } \subseteq d$ is called the covering set of d .

The union of all covering sets of all $d _ { i } \in { \cal D } ^ { + }$ is called the positive region (POS) of incoming documents. The set of all documents d such that $\exists d _ { i } \in D ^ { + } \Rightarrow d _ { i } \cap d \neq \emptyset$ is called the boundary region (BND). Also, the set of all documents d such that $\forall d _ { i } \in D ^ { + } \Rightarrow d _ { i } \cap d = \emptyset$ is called the negative region (NEG).

Given a document d, the decision rules can be determined ideally as follows:

$$
\frac {\exists d _ {i} \in D ^ {+} \Rightarrow d _ {i} \subseteq d}{d \in P O S}, \text {   and   } \frac {\exists d _ {i} \in D ^ {+} \Rightarrow d _ {i} \cap d \neq \emptyset}{d \in B N D}, \text {   and   } \frac {\forall d _ {i} \in D ^ {+} \Rightarrow d _ {i} \cap d = \emptyset}{d \in N E G}.
$$

The model also recommended a method to theoretically determine thresholds for <sup>fi</sup>nding the relevant documents if there is a probability function pr for terms in T. For example, in [21], this function was de<sup>fi</sup>ned as

$$
p r (t) = \frac {1}{m} \sum_ {d _ {i} \in D ^ {+}, t \in d _ {i}} \frac {1}{| d _ {i} \cap T |}
$$

for all terms $t \in T ,$ where $m = | \boldsymbol { T } |$ , the number of elements of T.

Theorem 3.1. Let pr be a probability function on T. We have the following property:

$$
\sum_ {t \in d \cap T} p r (t) \geq \min _ {d _ {i} \in D ^ {+}} \left\{\sum_ {t \in d _ {i} \cap T} p r (t) \right\}
$$

for all incoming documents d∈POS.

Proof. Let d be an incoming document and d∈POS. Based on the decision rules, we have

$$
\exists d _ {0} \in D ^ {+} \Rightarrow d _ {0} \subseteq d.
$$

Also, it is obvious that $p r ( t ) \geq 0$ for all $t \in T .$ Therefore, we have

$$
\sum_ {t \in d \cap T} p r (t) \geq \sum_ {t \in d _ {0} \cap T} p r (t) \geq \min _ {d _ {i} \in D ^ {+}} \left\{\sum_ {t \in d _ {i} \cap T} p r (t) \right\}.
$$

This theorem suggested using

$$
\min _ {d _ {i} \in D ^ {+}} \left\{\sum_ {t \in d _ {i} \cap T} p r (t) \right\}\tag{1}
$$

as a threshold for determining the relevant documents because all documents d∈POS can obtain a larger weight than the minimum weight of positive documents in the training set, that is, the method is complete in determining the positive documents.

In summary, the decision-rule based model can largely increase the recall of IF systems; however, the precision can be very low because the threshold would be very small if the training set includes many positive documents.

## 4. Rough threshold model for topic <sup>fi</sup>ltering

To improve the robustness of IF systems, in the topic <sup>fi</sup>ltering stage, we do not use the feature descriptions for the negative documents because the coverage of negative documents can be very large; therefore, it is impossible to describe their common features. In this paper, the feature descriptions are employed for only positive documents in the training set in order to precisely identify relevant information for the second stage.

In this section, we present a rough threshold model (RTM) for topic <sup>fi</sup>ltering and the corresponding algorithm. In contrast to most information <sup>fi</sup>ltering systems, topic <sup>fi</sup>ltering tries to <sup>fi</sup>lter out the likely negative (non-relevant) documents. Its primary goal is to achieve high performance for determining non-relevant information. Therefore, the objective of designing topic <sup>fi</sup>ltering models is different from the previous works for information <sup>fi</sup>ltering.

RTM discusses how to represent the positive documents in term weight distributions. It also proposes a new method for deciding thresholds for <sup>fi</sup>ltering out likely non-relevant documents for the second stage. In contrast to our previous method, the new one tries to describe the common feature of the training set.

## 4.1. Discovery of r-patterns

A set of terms is referred to as a termset. Given a positive document d and a term $t , t f ( d _ { i } , t )$ is de<sup>fi</sup>ned as the number of occurrences of t in $d _ { i \cdot } A$ set of term frequency pairs

$$
\hat {d} _ {i} = \{(t, f) | t \in T, f = t f (t, d _ {i}) \}
$$

is referred to as an initial r-pattern (rough pattern) in this paper.

Let termse $\because ( p ) = \{ t | ( t , f ) \in p \}$ be the termset of r-pattern p. In this paper, r-pattern $p _ { 1 }$ equals r-pattern $p _ { 2 }$ if and only if termse $t ( p _ { 1 } ) =$ termset(p ). A r-pattern is uniquely determined by its termset. Two initial r-patterns can be composed if they have the same termset. In this paper, we use the composition operation, ⊕, that is de<sup>fi</sup>ned in [22] to compose r-patterns. For example,

$$
\{(t _ {1}, 2), (t _ {2}, 5) \} \oplus \{(t _ {1}, 1), (t _ {2}, 3) \} = \{(t _ {1}, 3), (t _ {2}, 8) \}
$$

(notice: ⊕ is also suitable for patterns with different termsets, for instance, $\{ ( t _ { 1 } , 2 ) , ( t _ { 2 } , 5 ) \} \oplus \{ ( t _ { 1 } , 1 ) \} = \{ ( t _ { 1 } , 3 ) , ( t _ { 2 } , 5 ) \} )$ .

Based on the above de<sup>fi</sup>nitions, for a given set of positive documents $D ^ { + } { = } \{ d _ { 1 } , d _ { 2 } , . . . , d _ { n } \}$ , there are n corresponding initial r-patterns $\hat { d } _ { 1 } , \hat { d } _ { 2 } , . . . , \hat { d } _ { n } .$ . We can also group the initial r-patterns that have the same termset into clusters and use their composition, a r-pattern, to represent the cluster. Therefore, the training set of the positive documents, $D ^ { + }$ , is described as a set of r-patterns, $R P { = } \{ p _ { 1 } , p _ { 2 } , . . . , p _ { r } \}$ where $r \leq n ,$ , and $n = | D ^ { + } |$ is the number of the positive documents in D. We write this process as $R P = \{ p _ { 1 } , p _ { 2 } , . . . , p _ { r } \} \stackrel { \cdot } { = } \oplus \left( \left\{ \hat { d } _ { 1 } , \hat { d } _ { 2 } , . . . , \hat { d } _ { n } \right\} \right)$

Let clus $t e r ( p _ { i } )$ <sup>¼ f g ¼</sup>be the set of documents (initial patterns) that are composed to generate $p _ { i \cdot }$ We can de<sup>fi</sup>ne the support of a r-pattern $p _ { i }$ as follows:

$$
\operatorname{support} \left(p _ {i}\right) = \frac {\left| \operatorname{cluster} \left(p _ {i}\right) \right|}{\left| D ^ {+} \right|}.\tag{2}
$$

Theorem ${ \bf 4 . 1 }$ . Let $R P { = } \{ p _ { 1 } , p _ { 2 } , . . . , p _ { r } \}$ be the set of r-patterns discovered in $D ^ { + }$ . We have

$$
\sum_ {p _ {i} \in R P} \text { support } (p _ {i}) = 1.
$$

Proof. For any two r-patterns $p _ { i }$ and $p _ { j } ,$ , we have cluster(p )∩cluster $\quad ( p _ { j } ) =$ ∅ as the documents in the different r-patterns have different termsets. Therefore, we have

$$
\left. \left| \operatorname{cluster} \left(p _ {i}\right) \right| + \left| \operatorname{cluster} \left(p _ {j}\right) \right| = \left| \operatorname{cluster} \left(p _ {i}\right) \cup \operatorname{cluster} \left(p _ {j}\right) \right|. \right.
$$

Based on this equation and $\operatorname { E q . } \left( 2 \right)$ , we also have

$$
\begin{array}{l} \sum_ {p _ {i} \in R P} s u p p o r t (p _ {i}) = \sum_ {p _ {i} \in R P} \frac {| c l u s t e r (p _ {i}) |}{| D ^ {+} |} = \\ \frac {1}{| D ^ {+} |} \times \left| \bigcup_ {p _ {i} \in R P} c l u s t e r (p _ {i}) \right| = \frac {1}{| D ^ {+} |} \times \left| D ^ {+} \right| = 1. \end{array}
$$

Table 1 shows a set of initial r-patterns in a training set $D ^ { + } = \{ d _ { 1 }$ $d _ { 2 } , . . . , d _ { 6 } \}$ , where $T = \{ t _ { 1 } , t _ { 2 } , . . . , t _ { 7 } \}$ , and the numbers are term frequencies in the corresponding documents.

Table 2 illustrates the discovered r-patterns, their clusters and their supports by using the composition operation over the initial r-patterns in Table 1, where $p _ { 1 } = \hat { d } _ { 1 } , p _ { 2 } = \hat { d } _ { 2 } , p _ { 3 } = \hat { d } _ { 3 } \oplus \hat { d } _ { 4 }$ , and $p _ { 4 } =$ $\hat { d } _ { 5 } \oplus \hat { d } _ { 6 }$ <sup>¼</sup>for all discovered r-patterns.

## 4.2. Thresholds

Up to now, the positive documents in the training set have been represented as r-patterns. In the topic <sup>fi</sup>ltering stage, the discovered r-patterns are employed to <sup>fi</sup>lter out most irrelevant documents rather than to identify relevant documents.

Formally the relationship between r-patterns and terms can be described as the following association mapping if we consider term frequencies:

$$
\beta : R P \to 2 ^ {T \times [ 0, 1 ]},\tag{3}
$$

such that

$$
\beta (p _ {i}) = \{(t _ {1}, w _ {1}), (t _ {2}, w _ {2}), \dots , (t _ {k}, w _ {k}) \},
$$

where $p _ { i } { \in } R P$ is a r-pattern; and $\begin{array} { r } { w _ { i } = \frac { f _ { i } } { \sum _ { j = 1 } ^ { k } f _ { j } } } \end{array}$ if we assume

$$
p _ {i} = \{(t _ {1}, f _ {1}), (t _ {2}, f _ {2}), \dots , (t _ {k}, f _ {k}) \}.
$$

We call $\beta ( p _ { i } )$ the normal form of r-pattern $p _ { i }$ in this paper. The association mapping β can derive a function for the weight distribution of terms on T in order to show the importance of terms in the positive documents, which satis<sup>fi</sup>es:

$$
p r _ {\beta} (t) = \sum_ {p _ {i} \in R P, (t, w) \in \beta (p _ {i})} \text { support } (p _ {i}) \times w\tag{4}
$$

for all $t \in T .$

Theorem 4.2. Let RP be the set of discovered r-patterns, then $p r _ { \beta }$ is a probability function on $T \ i f \ \beta ( p _ { i } )$ is the normal form of all r-pattern $p _ { i } { \in } R P .$

Proof. Based on Eq. (4) and Theorem 4.1, we have

$$
\begin{array}{l} \sum_ {t \in T} p r _ {\beta} (t) = \sum_ {t \in T} \sum_ {p _ {i} \in R P, (t, w) \in \beta (p _ {i})} s u p p o r t (p _ {i}) \times w = \\ \sum_ {p _ {i} \in R P} \sum_ {(t, w) \in \beta (p _ {i})} s u p p o r t (p _ {i}) \times w = \\ \sum_ {p _ {i} \in R P} \left(s u p p o r t (p _ {i}) \times \sum_ {(t, w) \in \beta (p _ {i})} w\right) = \\ \sum_ {p _ {i} \in R P} s u p p o r t (p _ {i}) \times 1 = 1. \end{array}
$$

Based on the above discussion, a positive document $d _ { i }$ can be described as an event that represents what users want with the probability value

$$
\operatorname{prob} \left(d _ {i}\right) = \sum_ {t \in d _ {i} \cap T} \operatorname{pr} _ {\beta} (t).
$$

For the <sup>fi</sup>rst stage, the focus is on “removing” the “noise” (irrelevant documents). The basic assumption is that document d is irrelevant if it is not close to the common feature of the positive documents in the training set. Therefore, the threshold can be determined as follows:

$$
\text { threshold } = \bar {m} + \gamma (\sigma + \beta \times \text { skew })\tag{5}
$$

where m- is the mean of the probabilities of the positive documents in $\begin{array} { r } { D ^ { + } ; \bar { m } = \frac { 1 } { n } \sum _ { d _ { i } \in D ^ { + } } p r o b ( d _ { i } ) ; } \end{array}$ σ is the standard deviation of the proba-<sup>¼ ð Þ</sup>bilities of positive documents

$$
\sigma = \sqrt {\frac {1}{n} \sum_ {d _ {i} \in D ^ {+}} (p r o b (d _ {i}) - \bar {m}) ^ {2}};
$$

skew is the skewness of the probabilities

$$
s k e w = \frac {\sqrt {n} \sum_ {d _ {i} \in D ^ {+}} (p r o b (d _ {i}) - \bar {m}) ^ {3}}{\left(\sum_ {d _ {i} \in D ^ {+}} (p r o b (d _ {i}) - \bar {m}) ^ {2}\right) ^ {\frac {3}{2}}}; a n d
$$

γ and $\beta$ are experimental coef<sup>fi</sup>cients.

## 4.3. Topic filtering algorithms

An ef<sup>fi</sup>cient training procedure for calculating the derived probability function $p r _ { \beta }$ in topic <sup>fi</sup>ltering is described in Algorithm TF1T. In order to improve ef<sup>fi</sup>ciency, composition operations are not actually used in Algorithm TF1T. All initial r-patterns $R P$ are calculated in steps (1) and (2). Step (3) uses the composition operation ⊕ to group RP into clusters such that each cluster is described as a r-pattern. The probability distribution over T is then initialized to zero in step (4). Finally, each initial r-pattern is normalized and the probability values are accumulated in step (5). The time complexity of Algorithm TF1T in the training phase is $O ( n m q + n ^ { 2 } m ^ { 2 } )$ , since it only needs a single traversal through the positive documents and the composition time takes $O ( n ^ { 2 } m ^ { 2 } )$ , where q is the average size of the documents; $n = | D ^ { + } |$ and $m = | T | .$ . Algorithm TF1F describes the <sup>fi</sup>ltering process of the <sup>fi</sup>rst stage of the <sup>fi</sup>ltering process using the threshold de<sup>fi</sup>ned in Eq. (6). The time complexity of Algorithm TF1F in the testing phase is $O ( n m ) + O ( m q u ) = O ( m ( n +$ $q u ) ) = O ( m q u )$ since it only needs a traversal through each incoming document, where q is the average size of the testing documents; u is the size of the testing set, and usually $n { < } u .$

Based on the above analysis, we believe that both algorithms for the topic <sup>fi</sup>ltering stage are ef<sup>fi</sup>cient.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm TF1T ( $D^{+}$ , T)
Input: a set of positive documents  $D^{+}$  and a set of terms T.
Output: a probability function  $pr_{\beta}$  on T and a set of r-patterns RP.
Method:
(1)  $RP = \varnothing;$ 
(2) for (document  $d \in D^{+}$ ){
    for ( $t_{i} \in T$ ) let  $f_{i}$  be its term frequency in d;
    $\hat{d} = \left\{(t_{1}, f_{1}), \ldots, (t_{|T|}, f_{|T|})\right\};$ 
    support( $\hat{d}$ ) =  $\frac{1}{|D^{+}|};$ $RP = RP \cup \left\{\hat{d}\right\};$ 
(3)  $RP = \oplus(RP);$ 
(4) for (term  $t \in T$ )  $pr_{\beta}(t) = 0;$ 
(5) for (r-pattern  $p \in RP$ )
    for ((t, w) ∈ β(p))
    $pr_{\beta}(t) = pr_{\beta}(t) + w × support(p);$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm TF1F ( $D^{+}$ , T,  $pr_{\beta}$ , prob, RP,  $\gamma$ )
Input: Positive documents  $D^{+}$ , terms T,  $pr_{\beta}$ , prob,
r-patterns RP, and a coefficient  $\gamma$ .
Output: a set of retained (possible relevant) documents rel.
Method:
(1)  $n = \frac{1}{|D^{+}|}$ ,
 $\bar{m} = \frac{1}{n} \sum_{d_i \in D^+} prob(d_i)$ ,
 $\sigma = \sqrt{\frac{1}{n} \sum_{d_i \in D^+} (prob(d_i) - \bar{m})^2}$ ,
skew =  $\frac{\sqrt{n} \sum_{d_i \in D^+} (prob(d_i) - \bar{m})^3}{\left(\sum_{d_i \in D^+} (prob(d_i) - \bar{m})^2\right)^{\frac{3}{2}}}$ ;
(2) threshold =  $\bar{m} + \gamma (\sigma + \beta \times skew)$ ;
(3) rel = ∅;
for every document in the testing set {
    relevance(d) =  $\sum_{t \in T} pr_{\beta}(t) \tau(t, d)$ ;
    if (relevance(d) ≥ threshold)
    rel = rel ∪ {d};
}
</div>

Table 1  
A set of initial r-patterns of $D ^ { + } .$

<table><tr><td>Initial r-pattern</td><td> $t_1$ </td><td> $t_2$ </td><td> $t_3$ </td><td> $t_4$ </td><td> $t_5$ </td><td> $t_6$ </td><td> $t_7$ </td></tr><tr><td> $d_1$ </td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $d_2$ </td><td>0</td><td>0</td><td>2</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $d_3$ </td><td>0</td><td>0</td><td>3</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td> $d_4$ </td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td> $d_5$ </td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td> $d_6$ </td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr></table>

## 5. Pattern taxonomy mining

After the topic <sup>fi</sup>ltering task has been carried out, the most irrelevant documents have been removed from the testing sets. The second stage is to process the remaining documents using a pattern-based model. In the second stage, all the remaining documents after the <sup>fi</sup>rst stage are split into paragraphs. So a given document $d _ { i }$ yields a set of paragraphs DP.

## 5.1. Closed patterns in documents

Table 3 lists a set of the paragraphs for a given document, where duplicate terms are removed and $D P = \{ d p _ { 1 } , d p _ { 2 } , . . . , d p _ { 6 } \}$ . Let min $_ { - } s u p = 5 0 \%$ giving rise to ten frequent patterns of Table 3. Table 4 illustrates these frequent patterns and their covering paragraphs. Not all frequent patterns in Table 4 are useful. For example, pattern $\{ t _ { 3 } , t _ { 4 } \}$ always appears in paragraphs with term t in the paragraphs. Therefore, we believe that the shorter one $\{ t _ { 3 } , t _ { 4 } \}$ is a noisy pattern and it is expected to keep its super pattern, the larger one, $\left\{ t _ { 3 } , t _ { 4 } , t _ { 6 } \right\}$ only.

Based on the above de<sup>fi</sup>nitions, there are only three patterns that are closed in Table 4 (they are $\{ t _ { 3 } , t _ { 4 } , t _ { 6 } \} , \{ t _ { 1 } , t _ { 2 } \}$ and $\left\{ t _ { 6 } \right\} )$ , where a pattern is not a closed pattern if its covering paragraph is equal to the covering paragraph of any of its super patterns.

## 5.2. Pattern taxonomy

Patterns can be structured into a taxonomy by using the $i s \_ a$ (or “subset”) relation, where the nodes represent closed patterns and the edges are the direct “subset” relation. For example, pattern $\{ t _ { 6 } \}$ would become a direct sub-pattern of $\left\{ t _ { 3 } , t _ { 4 } , t _ { 6 } \right\}$ after pruning nonclosed patterns $\{ t _ { 3 } , t _ { 6 } \}$ and $\{ t _ { 4 } , t _ { 6 } \}$

The evaluation of term weights (called supports here) is different to most term-based approaches. In the term-based approaches, a component of a given term's weighting is estimated based on its appearance in the documents. In a PTM, terms are weighted according to their appearances in the discovered closed patterns. Furthermore, to effectively use the discovered closed patterns and the taxonomy information in a PTM, term supports are worked out by deploying (or summarizing) sets of closed patterns into r-patterns.

Formally, for each positive document $d _ { i } \in { \cal D } ^ { + }$ , we <sup>fi</sup>rst deploy its closed patterns on a common set of terms T in order to obtain the following r-patterns:

$$
\vec {d} _ {i} = <   \left(t _ {i _ {1}}, n _ {i _ {1}}\right), \left(t _ {i _ {2}}, n _ {i _ {2}}\right), \dots , \left(t _ {i _ {m}}, n _ {i _ {m}}\right) >\tag{6}
$$

A set of clusters of initial r-patterns.

<table><tr><td>R-pattern</td><td> $t_1$ </td><td> $t_2$ </td><td> $t_3$ </td><td> $t_4$ </td><td> $t_5$ </td><td> $t_6$ </td><td> $t_7$ </td><td>Cluster</td><td>Support</td></tr><tr><td> $p_1$ </td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $\{d_1\}$ </td><td>1/6</td></tr><tr><td> $p_2$ </td><td>0</td><td>0</td><td>2</td><td>1</td><td>0</td><td>1</td><td>0</td><td> $\{d_2\}$ </td><td>1/6</td></tr><tr><td> $p_3$ </td><td>0</td><td>0</td><td>4</td><td>2</td><td>2</td><td>2</td><td>0</td><td> $\{d_3,d_4\}$ </td><td>1/3</td></tr><tr><td> $p_4$ </td><td>3</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td> $\{d_5,d_6\}$ </td><td>1/3</td></tr></table>

Table 3  
A set of paragraphs.

<table><tr><td>Paragraph</td><td>Terms</td></tr><tr><td> $dp_{1}$ </td><td> $t_{1}$  $t_{2}$ </td></tr><tr><td> $dp_{2}$ </td><td> $t_{3}$  $t_{4}$  $t_{6}$ </td></tr><tr><td> $dp_{3}$ </td><td> $t_{3}$  $t_{4}$  $t_{5}$  $t_{6}$ </td></tr><tr><td> $dp_{4}$ </td><td> $t_{3}$  $t_{4}$  $t_{5}$  $t_{6}$ </td></tr><tr><td> $dp_{5}$ </td><td> $t_{1}$  $t_{2}$  $t_{6}$  $t_{7}$ </td></tr><tr><td> $dp_{6}$ </td><td> $t_{1}$  $t_{2}$  $t_{6}$  $t_{7}$ </td></tr></table>

where $t _ { i _ { j } }$ in pair $( t _ { i _ { j } } , n _ { i _ { j } } )$ denotes a single term and $n _ { i _ { j } }$ is its support in $d _ { i }$ which is the number of the closed patterns that contain $t _ { i _ { j } } ,$ that is,

$n _ { i _ { j } } = \left| \{ p | p \right.$ is a closed pattern of $d _ { i }$ and $t _ { i _ { j } } { \in } p \big \} \vert$

The concept of frequent and closed patterns is also suitable for the sequential patterns. A sequential pattern $s = < t _ { 1 } , . . . , t _ { r } > \ ( t _ { i } \subseteq T )$ is an ordered list of terms. A sequence $s _ { 1 } = < x _ { 1 } , . . . , x _ { i } >$ is a sub-sequence of another sequence $s _ { 2 } { = } { < } y _ { 1 } , { \ldots } , y _ { j } { > }$ , denoted by $s _ { 1 } \subseteq s _ { 2 } ,$ iff $\exists j _ { 1 } , . . . , j _ { y }$ such that $1 \leq j _ { 1 } < j _ { 2 } \ldots < j _ { y } \leq j$ and $x _ { 1 } = y _ { j _ { 1 } } , x _ { 2 } = y _ { j _ { 2 } } , . . . , x _ { i } = y _ { j _ { y } }$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm PTM2 ( $D^{+}$ , min_sup)
Input:  $D^{+}$ ; minimum support, min_sup.
Output: a set of r-patterns RP, and supports of terms.
Method:
(1)  $RP = \varnothing$ ;
(2) for (document  $d \in D^{+}$ ){
    let DP be the set of paragraphs in d;
    //sequential pattern mining in a set of paragraphs
    SP = SPMining(DP, min_sup);
    d =  $\varnothing$ ;
    for (pattern  $p_{i} \in SP$ ) {
    $p = \{(t, 1) | t \in p_{i}\}$ ;
    $d = d \oplus p\}$ $RP = RP \cup \left\{\begin{matrix} \rightarrow \\ d \end{matrix}\right\}$ 
(3)  $T = \{t | (t, w) \in p, p \in RP\}$ ;
    for (term  $t \in T$ ) support(t) = 0;
(4) for (r-pattern  $p \in RP$ )
    for  $((t, w) \in \beta(p))$ 
    support(t) = support(t) + w;
</div>

To improve the ef<sup>fi</sup>ciency of the mining of the pattern taxonomy, an algorithm, SPMining, was proposed in [47] to <sup>fi</sup>nd all closed sequential patterns, which used the well known Apriori property in order to reduce the searching space. In [27,52], many experiments showed that the closed sequential patterns are more effective than the normal closed patterns, and mining closed sequential patterns was more ef<sup>fi</sup>cient than mining normal closed patterns.

## 5.3. Pattern mining algorithm

Algorithm PTM2 describes the training process of estimating term supports using SPMining and the pattern deploying approach. For every positive document, the SPMining algorithm is <sup>fi</sup>rst called in step (2) giving rise to a set of closed sequential patterns SP. Additionally, all discovered patterns in a positive document are composed into an r-pattern giving rise to a set of r-patterns $R P$ in step (2). Thereafter in step (3) and (4), the support is calculated for all terms that appear in the r-patterns, where the normal forms $\beta ( p )$ (see $\operatorname { E q . } \ ( 4 ) )$ for all r-patterns $p { \in } R P$ are used.

Table 4  
Frequent patterns and covering paragraphs.

<table><tr><td>Frequent pattern</td><td>Covering paragraphs</td></tr><tr><td> $\{t_3, t_4, t_6\}$ </td><td> $[2,3,4] = \{dp_2, dp_3, dp_4\}$ </td></tr><tr><td> $\{t_3, t_4\}$ </td><td> $[2,3,4] = \{dp_2, dp_3, dp_4\}$ </td></tr><tr><td> $\{t_3, t_6\}$ </td><td> $[2,3,4] = \{dp_2, dp_3, dp_4\}$ </td></tr><tr><td> $\{t_4, t_6\}$ </td><td> $[2,3,4] = \{dp_2, dp_3, dp_4\}$ </td></tr><tr><td> $\{t_3\}$ </td><td> $[2,3,4] = \{dp_2, dp_3, dp_4\}$ </td></tr><tr><td> $\{t_4\}$ </td><td> $[2,3,4] = \{dp_2, dp_3, dp_4\}$ </td></tr><tr><td> $\{t_1, t_2\}$ </td><td> $[1,5,6] = \{dp_1, dp_5, dp_6\}$ </td></tr><tr><td> $\{t_1\}$ </td><td> $[1,5,6] = \{dp_1, dp_5, dp_6\}$ </td></tr><tr><td> $\{t_2\}$ </td><td> $[1,5,6] = \{dp_1, dp_5, dp_6\}$ </td></tr><tr><td> $\{t_6\}$ </td><td> $[2,3,4,5,6] = \{dp_2, dp_3, dp_4, dp_5, dp_6\}$ </td></tr></table>

The time complexity of post-processing discovered patterns in Algorithm PTM2 is $O ( | p | ^ { 2 } | S P | + m n )$ , since it needs $( | S P | - 1 )$ ⊕ composition operations and each ⊕ takes $O ( | p | ^ { 2 } )$ , and takes O(mn) for steps (3) and (4), where |SP| is the average number of the discovered patterns in each document; |p| is the average size of patterns, and $n = | D ^ { + } |$ and $m = \left| T \right|$ de<sup>fi</sup>ned as before.

After the supports of terms have been computed from the training set, the speci<sup>fi</sup>c value of a pattern p for the given topic is de<sup>fi</sup>ned as follows:

$$
\operatorname{spe} (p) = \sum_ {t \in p} \operatorname{support} (t).
$$

It is also easy to verify ${ s p e } ( p _ { 1 } ) { \le } s p e ( p _ { 2 } )$ if $p _ { 1 } \subseteq p _ { 2 } ,$ , that is, $p _ { 1 }$ is a sub-pattern of pattern $p _ { 2 } .$ . This property shows that a document should be assigned a large weight if it contains many large patterns. Based on this observation, we will assign the following weight to a document d for ranking documents in the second stage:

$$
w e i g h t (d) = \sum_ {t \in T} s u p p o r t (t) \tau (t, d).
$$

## 6. Experiments

The Reuters Corpus Volume 1 (RCV1) [19] has been selected to test the effectiveness of the new two-stage information <sup>fi</sup>ltering model. The RCV1 contains about 806,791 Reuters news articles that were produced by Reuters journalists for the period 20 August 1996 to 19 August 1997.

The RCV1 was used for TREC-11 Filtering Tracks [34,35]. The TREC-11 has developed and provided 100 topics with relevance judgments for the <sup>fi</sup>ltering track to simulate the user pro<sup>fi</sup>les to build a robust <sup>fi</sup>ltering system [37]. The topics are divided into two sets [40]: Assessor topics (a <sup>fi</sup>rst set of 50 topics) developed by the assessors of the National Institute of Standards and Technology (NIST) and Intersection topics (a second set of 50 topics) constructed arti<sup>fi</sup>cially from the intersections of pairs of Reuters categories.

The detailed comparisons of these two sets of topics can be found in [35,40]. In general, the <sup>fi</sup>rst set (the 50 human created topics) simulates the real user scenario in a more realistic way. The assessor topics are more reliable and have a good quality, but are more expensive. The second 50 topics are created by a computer-learning system. The quality of the intersection topics is not quite as good, compared with the assessor topics but a machine-learning system works faster than a human expert.

Table 5  
Different integrations of <sup>fi</sup>ltering models.

<table><tr><td>Integration (1st + 2nd)</td><td>Model</td><td>Description</td></tr><tr><td>Term + Pattern</td><td>T-SM</td><td>RTM integrated with PTM</td></tr><tr><td>Term + Pattern</td><td>BM25 + PTM</td><td>BM25 integrated with PTM</td></tr><tr><td>Term + Pattern</td><td>SVM + PTM</td><td>SVM integrated with PTM</td></tr><tr><td>Term + Term</td><td>RTM + BM25</td><td>RTM integrated with BM25</td></tr><tr><td>Term + Term</td><td>RTM + SVM</td><td>RTM integrated with SVM</td></tr></table>

Table 6  
T-SM vs DRM+PTM: results on assessor topics

<table><tr><td></td><td>DRM + PTM</td><td>T-SM (RTM + PTM)</td><td>PTM</td><td>%chg</td></tr><tr><td>B/P</td><td>0.4303</td><td>0.5275</td><td>0.4288</td><td>23.01%</td></tr><tr><td>MAP</td><td>0.4393</td><td>0.5393</td><td>0.4372</td><td>23.35%</td></tr><tr><td> $F_{\beta=1}$ </td><td>0.4366</td><td>0.5029</td><td>0.4357</td><td>15.19%</td></tr></table>

In this paper, all 100 topics are used. The experimental results will be reported on the assessor topics, intersection topics and all 100 topics, respectively. The purpose of reporting on different sets is to verify that the proposed method will be effective for a variety assessment methods.

## 6.1. Evaluation metrics

The following measures are some widely accepted and wellestablished evaluation metrics. Each metric focuses on a different aspect of the system performance, as described below.

The F-beta $\left( F _ { \beta } \right)$ measure is a function of Recall (R) and Precision (P), together with a free parameter beta $\beta .$ It is calculated by the following function: $F _ { \beta } = \frac { { \left( { \beta } ^ { 2 } + 1 \right) } P R } { { \beta } ^ { 2 } P + R } ;$ β can be viewed as the relative <sup>þ</sup>degree of importance attributed to the P precision and R recall [39]. The parameter $\beta = 1$ is used in our study, which means that recall and precision are weighed equally. Therefore $F _ { \beta }$ is denoted by: $\begin{array} { r } { F _ { 1 } = \frac { 2 P R } { ( P + R ) } } \end{array}$

<sup>¼ ð</sup> <sup>Þ</sup> <sup>þ</sup> Mean Average Precision (MAP) is calculated by measuring the precision of each relevant document <sup>fi</sup>rst, and then averaging the precision over all the topics. It combines precision, relevance ranking and overall recall together to measure the quality of the retrieval engines.

Breakeven Point (B/P) is the value of the precision (or recall) for which the P/R curve intersects the precision=recall line. The measure was <sup>fi</sup>rst proposed by [18] and used by [14,48]. The larger the measure scores, the better the system performs. Because the breakeven point metric is independent of the different threshold choices, it can therefore be regarded as a pure measure of the quality of the computed classi<sup>fi</sup>er itself.

11-Points is introduced and has been adopted before in several research works [48]. It is used to compare the performance of different systems by averaging the precisions at 11 standard recall levels $( \mathrm { r e c a l l } 1 { = } 0 . 0 , 0 . 1 , . . . , 1 . 0 ,$ where 0.0 means the smallest positive value).

The paired two-tailed t-test is used in this paper to give statistical evidence to support our hypotheses, H1 and H2. Due to the length of paper limitation, the t-test is applied over 100 topics on $F _ { 1 }$ scores only.

## 6.2. Baseline models

The state-of-the-art term-based models, BM25 and SVM, and the newly developed pattern-based PTM, are used as baseline models.

BM25 [35] is one of the state-of-the-art retrieval functions used in document retrieval. BM25 and its variants have been extensively described and evaluated in the IR literature, and hence serve as a strong, reproducible baseline. The BM25 variant we used for our experiments computes the term weights using the following equation:

Table 7  
T-SM vs DRM+PTM: results on intersection topics.

<table><tr><td></td><td>DRM + PTM</td><td>T-SM (RTM + PTM)</td><td>PTM</td><td>%chg</td></tr><tr><td>B/P</td><td>0.4799</td><td>0.5771</td><td>0.4791</td><td>20.25%</td></tr><tr><td>MAP</td><td>0.5125</td><td>0.6081</td><td>0.5118</td><td>18.65%</td></tr><tr><td> $F_{\beta=1}$ </td><td>0.4703</td><td>0.5258</td><td>0.4700</td><td>11.80%</td></tr></table>

Table 8  
RTM vs BM25 and SVM: results on all 100 topics.

<table><tr><td></td><td>BM25</td><td>SVM</td><td>RTM</td><td>%chg</td></tr><tr><td>B/P</td><td>0.4345</td><td>0.4501</td><td>0.4556</td><td>-1.2%</td></tr><tr><td>MAP</td><td>0.4629</td><td>0.4674</td><td>0.4531</td><td>3.15%</td></tr><tr><td> $F_{\beta=1}$ </td><td>0.4453</td><td>0.4517</td><td>0.4388</td><td>2.94%</td></tr></table>

$$
W (t) = \frac {t f \cdot (k _ {1} + 1)}{k _ {1} \cdot ((1 - b) + b \frac {D L}{A V D L}) + t f} \cdot \log \frac {\frac {(r + 0 . 5)}{(n - r + 0 . 5)}}{\frac {(R - r + 0 . 5)}{(N - n - R + r + 0 . 5)}}
$$

where N is the total number of documents in the training set; R is the number of positive documents in the training set; n is the number of documents which contain term t; r is the number of positive documents which contain term t; tf is the term frequency; DL and AVDL are the document length and average document length, respectively; and k and b are the experimental parameters (the values of $k _ { 1 }$ and b are 1.2 and 0.75, respectively [35,47]. We also use that setting in this paper).

Information <sup>fi</sup>ltering can also be regarded as a special instance of text classi<sup>fi</sup>cation [39]. SVM is a statistical method that can be used to <sup>fi</sup>nd a hyperplane that best separates two classes. SVM achieved the best performance on the Reuters-21578 data collection for document classi<sup>fi</sup>cation [48]. The decision function in SVM is de<sup>fi</sup>ned as:

$$
h (x) = \operatorname{sign} (W \cdot x + b) = \left\{ \begin{array}{l l} + 1 & \text { if } (w \cdot x + b) > 0 \\ - 1 & \text { otherwise } \end{array} \right.
$$

where x is the input object; b ε R is a threshold and $\begin{array} { r } { W = \sum _ { i = 1 } ^ { l } y _ { i } \alpha _ { i } x _ { i } } \end{array}$ for the given training data: $\left( x _ { i } , y _ { i } \right) , . . . , \left( x _ { l } , y _ { l } \right)$ , where $x _ { i } \ \varepsilon \ \Re ^ { n }$ and y equals $+ 1 \ ( - 1 )$ , if document x is labeled positive (negative). α ε R is the weight of the training example $x _ { i }$ and satis<sup>fi</sup>es the following constraints:

$$
\forall_ {i}: \alpha_ {i} \geq 0 \quad \text { and } \quad \sum_ {i = 1} ^ {l} \alpha_ {i} y _ {i} = 0\tag{7}
$$

To compare with other baseline models, we tried to use SVM to rank documents rather than to make binary decisions. For this purpose, threshold b can be ignored. We also believe that the positive documents in the training set would have the same importance to user information needs because the training set was only simply divided into relevant documents and non-relevant documents by the assessors. So we assign the same α value $( \mathsf { e } . \mathsf { g } _ { \cdot } , 1 )$ to each positive document <sup>fi</sup>rst, and then determine the same α $( \mathrm { e } . \mathrm { g } . , \alpha ^ { - 1 } )$ value for each negative document based on Eq. (7). Therefore, we use the following weighting function to estimate the terms weights:

$$
W = \left(\sum_ {d _ {i} \in D ^ {+}} d _ {i}\right) + \left(\sum_ {d _ {j} \in D ^ {-}} d _ {j} \alpha^ {- 1}\right).
$$

The PTM model is also selected as one of the baseline models, because we want to verify that the “noise” is removed at the topic <sup>fi</sup>ltering stage and then this leads to the PTM model achieving a signi<sup>fi</sup>cant improvement of performance in the relatively “clean” incoming document steam. The two-stage model (T-SM) uses 150 terms in the <sup>fi</sup>rst stage. To keep a suf<sup>fi</sup>cient number of documents in the testing set for each topic, the experimental coef<sup>fi</sup>cients $\gamma { = } 0 . 2 5$ and β=1 (see Eq. (5)) are used in the <sup>fi</sup>rst stage. In the second stage, min ${ \_ } s u p { = } 0 . 2$ , and the average size of the term set is 4000.

Table 9  
T-SM vs other two-stage IF: results on assessor topics.

<table><tr><td></td><td>BM25 + PTM</td><td>T-SM</td><td>SVM + PTM</td><td>RTM + BM25</td><td>RTM + SVM</td><td>%chg</td></tr><tr><td>B/P</td><td>0.4670</td><td>0.5275</td><td>0.4501</td><td>0.4251</td><td>0.4338</td><td>13.00%</td></tr><tr><td>MAP</td><td>0.4778</td><td>0.5393</td><td>0.4820</td><td>0.4403</td><td>0.4296</td><td>11.89%</td></tr><tr><td> $F_{\beta=1}$ </td><td>0.4557</td><td>0.5029</td><td>0.4593</td><td>0.4343</td><td>0.4324</td><td>9.50%</td></tr></table>

Table 10  
T-SM vs other two-stage IF: Results on intersection topics.

<table><tr><td></td><td>BM25 + PTM</td><td>T-SM</td><td>SVM + PTM</td><td>RTM + BM25</td><td>RTM + SVM</td><td>%chg</td></tr><tr><td>B/P</td><td>0.5203</td><td>0.5771</td><td>0.5231</td><td>0.4934</td><td>0.5162</td><td>10.32%</td></tr><tr><td>MAP</td><td>0.5602</td><td>0.6081</td><td>0.5652</td><td>0.5328</td><td>0.5494</td><td>7.59%</td></tr><tr><td> $F_{\beta=1}$ </td><td>0.4940</td><td>0.5258</td><td>0.4972</td><td>0.4784</td><td>0.4899</td><td>5.75%</td></tr></table>

After the weights of terms have been computed from the training set for a given topic, the following weight will be assigned to every incoming document d for deciding its relevance:

$$
\operatorname{weight} (d) = \sum_ {t \in T} W (t) \tau (t, d),\tag{8}
$$

where $\tau ( t , d ) = 1 { \mathrm { ~ i f ~ } } t \in d ; { \mathrm { ~ o t h e r w i s e ~ } } \tau ( t , d ) = 0 .$

## 6.3. Hypotheses

The proposed two-stage <sup>fi</sup>ltering model (T-SM) integrates two types of <sup>fi</sup>ltering models: a term-based <sup>fi</sup>ltering model and a pattern miningbased model. In the <sup>fi</sup>rst stage, a threshold setting method is developed based on the rough analysis. It is called the Rough Threshold Model (RTM). In the second stage, a document ranking model is developed based on the pattern taxonomy model (PTM). The major objectives of the experiments are to show how the rough threshold model of the <sup>fi</sup>rst stage can affect the performance of the two-stage <sup>fi</sup>ltering system and how the pattern mining method can help improve the performance in the second stage. Hence, to give a comprehensive investigation for the proposed model, our experiments involve comparing the <sup>fi</sup>ltering performance of the different threshold setting methods and the different combinations of term-based and pattern-based <sup>fi</sup>ltering models.

## 6.3.1. Topic filtering

The threshold setting method developed by Li [21] in 2004 has been discussed in Section 3. This threshold setting method is called the Decision Rule-based Model (DRM). In this section, T-SM is evaluated in terms of the following hypothesis:

![](/api/attachments/PBPDB8UV/fulltext/images/8ca325f65e0928d3537e419f359a3ad9dd1706b70ccd89f7fd2070aa945c0dba.jpg)  
Fig. 1. T-SM vs PTM and “Term+Pattern”: results of 11-points on all 100 topics.

![](/api/attachments/PBPDB8UV/fulltext/images/828e66e712b6d877d2731cef71d5477b0b0cd55cfab9958208b11fe8b3fb8dcc.jpg)  
Fig. 2. T-SM vs BM25, SVM and “Term +Term”: results of 11-points on all 100 topics.

Hypothesis H1. In the <sup>fi</sup>rst-stage, the rough threshold model developed in Eq. (5) is designed to achieve high performance for determining non-relevant information. The rough threshold model is better than the DRM (see Theorem 3.1 and Eq. (1)); but its performance for determining relevant information is not required to be better than the state-of-the-art term-based models.

## 6.3.2. Different combinations of filtering models

Some pattern-based and term-based models have been discussed as a single <sup>fi</sup>ltering model. These models can be combined to create different types of two-stage models. Table 5 illustrates the possible combinations of a term-based model with the pattern-based model or a term-based model with another term-based model, where for the ef<sup>fi</sup>ciency issue, the model used for the <sup>fi</sup>rst stage should be a term-based model.

In this section, T-SM will be evaluated in terms of the following hypothesis:

Hypothesis H2. The rough threshold model, the <sup>fi</sup>rst stage of T-SM, has better performance to <sup>fi</sup>lter out the non-relevant information in the <sup>fi</sup>rst stage. The new two-stage model (T-SM) will perform better than other types of “two-stage models”.

## 6.4. Results

## 6.4.1. Experiments for testing Hypothesis H1

The performance of DRM+PTM, T-SM and PTM is compared. The results are shown in Tables 6 and 7, where %chg means the percentage change of T-SM over DRM+PTM and the bold entries mean the best performance.

As can be seen from the results presented in the above tables, DRM+PTM is slightly better than PTM, and T-SM is extremely better than DRM+PTM, which achieves the best performance with very high percentage changes (see %chg) for all measures. With regards to the threshold setting methods, the newly developed threshold setting model RTM is much better than the DRM in terms of <sup>fi</sup>ltering out the non-relevant documents. These results strongly support Hypothesis H1.

Table 11  
Paired t test results: T-SM vs all other IF models over all 100 topics on $F _ { 1 } .$

<table><tr><td></td><td> $F_{\beta=1}$ </td><td>p-Value</td></tr><tr><td>T-SM</td><td>0.5144</td><td></td></tr><tr><td>BM25 + PTM</td><td>0.4749</td><td>2.15271E-07</td></tr><tr><td>SVM + PTM</td><td>0.4783</td><td>2.02454E-06</td></tr><tr><td>RTM + BM25</td><td>0.4564</td><td>4.90958E-08</td></tr><tr><td>RTM + SVM</td><td>0.4612</td><td>4.23648E-07</td></tr><tr><td>BM25</td><td>0.4453</td><td>4.19638E-09</td></tr><tr><td>SVM</td><td>0.4517</td><td>2.70726E-08</td></tr></table>

Table 12  
Statistical results for 100 topics after the topic <sup>fi</sup>ltering

<table><tr><td></td><td>%chg_p</td><td>%chg_n</td><td>%f_out</td><td>%n_filtered</td></tr><tr><td>After filtering</td><td>+71.4</td><td>-19.0</td><td>79</td><td>82</td></tr></table>

Also, the design objective of the RTM is not required to be better than the state-of-the-art term-based models for deciding the relevant information. We also conducted some experiments to compare the term weighting technique used in the RTM with the state-of-the-art methods (SVM and BM25). Table 8 shows the results over all 100 topics on all three measures, where the bold entries mean the best performance. It was found that BM25 and SVM were better than the RTM on the MAP and $F _ { 1 }$ measure, but the RTM is a little bit better on the B/P measure. In the following sub-sections, however, we will <sup>fi</sup>nd that the rough threshold model will achieve the best performance in terms of two-stage <sup>fi</sup>ltering.

## 6.4.2. T-SM vs other two-stage IF models

The results of the comparisons of T-SM with other possible twostage IF models, which include the BM25+PTM, SVM+PTM, RTM+ BM25, and RTM+SVM models are displayed in Tables 9 and 10, where %chg means the percentage change over the best result produced by other models and the bold entries mean the best performance. Figs. 1 and 2 illustrate the comparisons of T-SM with all single-stage and two-stage IF models over the 11-points measure. Eq. (5) is used as the method for determining a threshold, and the best results were obtained when the threshold parameters were set at γ=−0.25 and β=1.

The threshold parameter γ is obtained from the speci<sup>fi</sup>c data set (RCV1 in this study). It is an empirical value. When the user pro<sup>fi</sup>les are speci<sup>fi</sup>c, a lower value of γ can be used allowing more documents to be added into the second stage <sup>fi</sup>ltering. Likewise, a higher value of γ will potentially limit the irrelevant documents moving into next stage. For adaptive <sup>fi</sup>ltering, γ can be a dynamic parameter (reducing) as the user pro<sup>fi</sup>les become more certain.

The results show that T-SM signi<sup>fi</sup>cantly outperforms other twostage models in all measures. The purpose of the topic <sup>fi</sup>ltering stage is to remove the “noise” and prepare more “clean” data for the pattern-mining stage. As can be seen from the above results, the rough threshold model RTM can achieve this goal because the design objectives of the RTM are different to the traditional <sup>fi</sup>ltering models. The RTM has excellent performance for determining the non-relevant information compared with the traditional models that focus on the performance for determining the relevant information.

Table 11 shows the t-test results, where the bold entry means the best performance. As shown in Table 11, the p values in all the paired (i.e., T-SM between another IF model) are less than 0.0001. The improvements are considered to be extremely statistically signi<sup>fi</sup>cant. The results also strongly support Hypotheses H1 and H2.

## 7. Discussion

Comprehensive experimental results have been reported in the previous section. The comprehensive performance study shows that the two-stage IF model is superior to all baseline models. Furthermore, it con<sup>fi</sup>rms that the threshold-setting method used in the topic <sup>fi</sup>ltering of the two-stage model is the optimal method. In this section, we discuss the underlying reasons and the implications of the theoretical model design.

Table 13  
Statistical results of 100 topics for the interesting <sup>fi</sup>nding.

<table><tr><td></td><td>min_w</td><td> $N_{w \geq min\_w}$ </td><td> $N_{POS}$ </td><td>Possible errors</td></tr><tr><td>Avg.</td><td>3.003312527</td><td>134.3</td><td>50.77</td><td> $\geq 83.53$ </td></tr></table>

## 7.1. Post hoc analysis

To resolve the question of how well the theoretically-motivated threshold performed in practice, a post hoc analysis has been conducted in this section. The results of the statistical analysis are depicted in Tables 12 and 13. The notations used in Table 12 are explained below:

• %chg \_p denotes the average percentage change in number of positive documents after the topic <sup>fi</sup>ltering.

• %chg \_n denotes the average percentage change in number of negative documents after the topic <sup>fi</sup>ltering.

• %f \_out means the average percentage of the <sup>fi</sup>ltered out documents.

• %n \_filtered means the average percentage of negative documents in the <sup>fi</sup>ltered out documents.

The observation from Table 12 is that the <sup>fi</sup>rst stage (the topic <sup>fi</sup>lter) removed, on average, 79% of the documents and 82% of these were indeed irrelevant. In the remaining documents intended for the second stage, the average percentage in number of positive documents is +71.4% (increase); and the average percentage in number of the negative documents is −19.0% (decrease). On the whole, the threshold can deliver enough relevant documents for an effective pattern taxonomy to be mined.

Compared with term-based approaches, patterns appear to capture more “semantic” information, which, we speculate, is the reason for the boost in performance. In the experiments, 150 terms were used for the term-based models, because larger numbers of terms degraded the performance. In contrast, 4000 terms were used for the pattern mining in the second stage.

In the pattern mining <sup>fi</sup>ltering stage, a small min \_sup is used to <sup>fi</sup>nd interesting patterns because of patterns having a low frequency of occurrence. The consequence is that some noisy terms and their combinations (patterns) are also retained which results in some negative documents obtaining large weights in the pattern mining model. This interesting <sup>fi</sup>nding is also veri<sup>fi</sup>ed by the experiments that are illustrated in Table 13. The notations used in Table 13 are explained below:

• min \_w is the minimum of the document weights in rel of the retained testing documents.

$N _ { w \geq m i n \_ w }$ is the number of <sup>fi</sup>ltered out documents that have the weights ≥min \_w

$N _ { P O S }$ is the number of positive documents that are <sup>fi</sup>ltered out.

The T-SM divides the testing documents into two sets. One is the set of remaining documents that consists of a set of relevant documents (rel) and a set of irrelevant documents. The other is the set of <sup>fi</sup>ltered-out documents. The latter includes 50.77 positive documents on average; however, the pattern mining model can move 134.3 documents to rel if topic <sup>fi</sup>ltering is not used <sup>fi</sup>rst, that is, there are more than 83.53 (134.3−50.77) errors the pattern mining model would make.

In conclusion, these <sup>fi</sup>ndings discussed above provide the evidence to support the hypothesis that the proposed two-stage model can signi<sup>fi</sup>cantly improve the effectiveness of IF systems. This signi<sup>fi</sup>cant improvement is due mainly to the success in the removal of the noisy information by the topic <sup>fi</sup>ltering stage.

## 8. Conclusions

We presented the initial idea of a two-stage decision model for IF in [26], which illustrated a new methodology which integrates two different IF models in order to alleviate information overload and mismatch problems. The <sup>fi</sup>rst decision stage of the proposed model is to dramatically reduce the excessive volume of information exposed to knowledge workers via a rough sets-based information analysis, and the second decision stage is to select the most relevant and interesting information that best meets knowledge workers' needs via a semantic information matching mechanism empowered by pattern taxonomy mining.

In this paper, we continue to develop the two-stage decision model and experimentally prove that the integration of the rough analysis and pattern taxonomy mining is the best way for designing a twostage decision model for IF systems. We also justify the rationale of the proposed model and design a set of experiments in order to illustrate the signi<sup>fi</sup>cance of the proposed model. The proposed model has been evaluated using the standard TREC routing framework. Compared with the BM25, SVM, and PTM methods and other possible types of “two-stage” models, the results of experiments on the RCV1 collection demonstrate that the performance of information <sup>fi</sup>ltering can be signi<sup>fi</sup>cantly improved by the proposed new model. The substantial improvement is mainly due to the rough threshold model applied to the topic <sup>fi</sup>ltering in the <sup>fi</sup>rst stage and the “semantic” nature of patterns in the second stage. This research provides a promising methodology for developing effective <sup>fi</sup>ltering systems based on the positive feedback information.

## Acknowledgments

This paper was partially supported by grant DP0556455 from the Australian Research Council (ARC Discovery Project). The authors also wish to thank Dr. Sheng-Tang Wu for providing help with the experiments, and Prof. Ning Zhong for his constructive suggestions.

## References

[1] H. Ahonen, O. Heinonen, M. Klemettinen, A.I. Verkamo, Applying data mining techniques for descriptive phrase extraction in digital document collections, Proc. of the IEEE Forum on Research and Technology Advances in Digital Libraries, Santa Barbara, CA, USA, 1998, pp. 2–11

[2] A. Amir, Y. Aumann, R. Feldman, M. Fresko, Maximal association rules: a tool for mining associations in text, Journal of Intelligent Informaiton Systems 25 (3) (2005) 333–345.

[3] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, Addison Wesley, 1999.

[4] J. Bayardo, Ef<sup>fi</sup>ciently mining long patterns from databases, Proc. of SIGMOD'98 1998, pp. 85–93.

[5] N.J. Belkin, W.B. Croft, Information <sup>fi</sup>ltering and information retrieval: two sides of the same coin? Communications of the ACM 35 (12) (1992) 29–38.

[6] G. Cao, J. Nie, J. Gao, S. Robertson, Selecting good expansion terms for pseudorelevance feeback, Proc. of SIGIR'08, 2008, pp. 243–250.

[7] J.P. Caulkins, W. Ding, G. Duncan, R. Krishnan, E. Nyberg, A method for managing access to web pages: Filtering by Statistical Classi<sup>fi</sup>cation (FSC) applied to text, Decision Support Systems 42 (1) (2006) 144–161.

[8] A. Farhoomand, D. Drury, Managerial information overload, Communications of the ACM 45 (10) (2002) 127–131.

[9] R. Feldman, Y. Aumann, A. Amir, A. Zilberstein, W. Kloesgen, Maximal association rules: a new tool for mining for keyword cooccurrences in document collections, Proc. of KDD'97, 1997, pp. 167–170.

[10] N. Fuhr, Probabilistic models in information retrieval, The Computer Journal 35 (3) (1992) 243–255.

[11] B. Ganter, R. Wille, Formal Concept Analysis: Mathematical Foundation, Springer-Verlag, 1999.

[12] M. Iwayama, Relevance feedback with a small number of relevance judgements: incremental relevance feedback vs. document clustering, Proc. of SIGIR'00, 2000, pp. 10–16.

[13] N. Jindal, B. Liu, Identifying comparative sentences in text documents, Proc. of SIGIR'06, ACM, New York, NY, USA, 2006, pp. 244–251.

[14] T. Joachims, Transductive inference for text classi<sup>fi</sup>cation using support vector machines, 16th International Conference on Machine Learning, Bled Slovenia, 1999 pp. 200–209

[15] T. Joachims, A statistical learning model of text classi<sup>fi</sup>cation with support vector machines, Proc, of ACM SIGIR'01. 2001 pp. 128-136.

[16] R. Kaptein, J. Kamps, D. Hiemstra, The Impact of Positive, Negative and Topical Relevance Feedback, TREC, 2008.

[17] R.Y.K. Lau, P.D. Bruza, D. Song, Towards a belief-revision-based adaptive and context-sensitive information retrieval system, ACM Transactions on Information Systems 26 (2) (2008) 1–38.

[18] D.D. Lewis, An evaluation of phrasal and clustered representations on a text categorization task, Proc. of SIGIR'92, 1992, pp. 37–50.

[19] D.D. Lewis, Y. Yang, T.G. Rose, F. Li, RCV1: a new benchmark collection for text categorization research, Journal of Machine Learning Research 5 (2004) 361–397.

[20] X. Li, B. Liu, Learning to classify texts using positive and unlabeled data, Proc. of IJCAI'03, 2003, pp. 587–594.

[21] Y. Li, N. Zhong, Web mining model and its applications for information gathering, Knowledge-Based Systems 17 (2004) 207–217.

[22] Y. Li, N. Zhong, Mining ontology for automatically acquiring web user information needs, IEEE Transactions on Knowledge and Data Engineering 18 (4) (2006) 554–568

[23] Y. Li, C. Zhang, J.R. Swan, An information <sup>fi</sup>ltering model on the Web and its application in JobAgent, Knowl.-Based Syst. 13 (5) (2000) 285–296.

[24] Y. Li, C. Zhang, S. Zhang Cooperative, Strategy for web data mining and cleaning, Applied Arti<sup>fi</sup>cial Intelligence 17 (2003) 443–460.

[25] Y. Li, S.-T. Wu, Y. Xu, Deploying association rules on hypothesis spaces, Proceedings of CIMCA'04, Gold Coast, Australia, 2004, pp. 769–778.

[26] Y. Li, X. Zhou, P. Bruza, Y. Xu, R.Y. Lau, A two-stage text mining model for information <sup>fi</sup>ltering, Proc. of CIKM'08, Napa Valley, California, USA, 2008, pp. 1023–1032.

[27] Y. Li, A. Algarni, N. Zhong, Mining positive and negative patterns for relevance feature discovery, Proceedings of 16th ACM SIGKDD international conference on Knowledge discovery and data mining (KDD'10), Washington, USA, 2010, pp. 753–762.

[28] A. Maedche, Ontology Learning for the Semantic Web, Kluwer Academic, 2003.

[29] C.D. Manning, P. Raghavan, H.S. An, Introduction to Information Retrieval, Cambridge University Press, 2008.

[30] J. Mostafa, W. Lam, Automatic classi<sup>fi</sup>cation using supervised learning in a medi cal document <sup>fi</sup>ltering application, Inf. Process. Manage. 36 (3) (2000) 415–444.

[31] J. Mostafa, S. Mukhopadhyay, W. Lam, M.J. Palakal, A multilevel approach to intelligent information <sup>fi</sup>ltering: model, system, and evaluation, ACM Transactions on Information Systems 15 (4) (1997) 368–399.

[32] T. Qin, X.-D. Zhang, D.-S. Wang, T.-Y. Liu, W. Lai, H. Li, Ranking with multiple hyperplanes, Proc. of SIGIR'07, 2007, pp. 279–286.

[33] S. Robertson, D.A. Hull, The TREC9 <sup>fi</sup>ltering track <sup>fi</sup>nal report, TREC-9, 2000.

[34] S. Robertson, I. Soboroff, The TREC-10 <sup>fi</sup>ltering track <sup>fi</sup>nal report, TREC 2001, 2001.

[35] S.E. Robertson, I. Soboroff, The TREC 2002 Filtering Track Report, TREC, 2002.

[36] S.E. Robertson, H. Zaragoza, M.J. Taylor, Simple BM25 extension to multiple weighted <sup>fi</sup>elds, Proc. of CIKM'04, 2004, pp. 42–49.

[37] T. Rose, M. Stevenson, M. Whitehead, The reuters corpus volume1 — from yesterday's news to today's language resources, 3rd Inter. Conf. on Language Resources and Evaluation, Las Palmas, Spain, 2002, pp. 29–31.

[38] S. Scott, S. Matwin, Feature engineering for text classi<sup>fi</sup>cation, 16th International Conference on Machine Learning, 1999, pp. 379–388.

[39] F. Sebastiani, Machine learning in automated text categorization, ACM Computing Surveys 34 (1) (2002) 1–47.

[40] I. Soboroff, S.E. Robertson, Building a <sup>fi</sup>ltering test collection for TREC 2002, Proc. of SIGIR'03, 2003, pp. 243–250.

[41] D. Song, R. Lau, P. Bruza, K. Wong, D. Chen, An adaptive information agent for document title classi<sup>fi</sup>cation and <sup>fi</sup>ltering in document-intensive domains, Decision Support Systems 44 (1) (2007) 251–265.

[42] T. Strzalkowski, Robust text processing in automated information retrieval, Proceedings of the 4th Applied Natural Language Processing Conference (ANLP), 1994, pp. 168–173.

[43] D. Tao, X. Li, S.J. Maybank, Negative samples analysis in relevance feedback, IEEE Trans. Knowl. Data Eng. 19 (4) (2007) 568–580.

[44] P. Tzvetkov, X. Yan, J. Han, TSP: mining top-K closed sequential patterns, 3rd IEEE International Conference on Data Mining, Melbourne, Florida, USA, 2003, pp. 347–354.

[45] H.F.X. Wang, C. Zhai, A study of methods for negative relevance feedback, Proc. of SIGIR'08, 2008, pp. 219–226.

[46] S.-T. Wu, Y. Li, Y. Xu, B. Pham, P. Chen, Automatic pattern-taxonomy extraction for web mining, the IEEE/WIC/ACM International Conference on Web Intelligence, China, 2004, pp. 242–248.

[47] S.-T. Wu, Y. Li, Y. Xu, Deploying approaches for pattern re<sup>fi</sup>nement in text mining, 6th IEEE International Conference on Data Mining, Hong Kong, 2006, pp. 1157–1161.

[48] Y. Yang, X. Liu, A re-examination of text categorization methods, Proc. of SIGIR'99, 1999, pp. 42–49.

[49] Y. Yang, A. Lad, N. Lao, A. Harpale, B. Kisiel, M. Rogati, Utility-based information distillation over temporally sequenced documents, Proc. of SIGIR'07, ACM, New York, NY, USA, 2007, pp. 31–38.

[50] Y. Yao, S.K.M. Wong, A decision theoretic framework for approximating concepts, International Journal of Man-Machine Studies 37 (6) (1992) 793–809.

[51] Z. Zheng, K. Chen, G. Sun, H. Zha, A regression framework for learning ranking functions using relative relevance judgments, Proc. of SIGIR'07, 2007, pp. 287–294.

[52] N. Zhong, Y. Li, S.-T. Wu, Effective pattern discovery for text mining. IEEE Transactions on Knowledge and Data Engineering 24 (1) (2012) 30–44 doi:10.1109/ TKDE 2010.211

[53] X. Zhou, S.-T. Wu, Y. Li, Y. Xu, R.Y.K. Lau, P.D. Bruza, Utilizing search intent in topic ontology-based user pro<sup>fi</sup>le for web mining, 2006 IEEE/WIC/ACM International Conference on Web Intelligence, Hong Kong, 2006, pp. 558–564.

[54] X. Zhou, Y. Li, P. Bruza, S.-T. Wu, Y. Xu, R.Y.K. Lau, Using information <sup>fi</sup>ltering in web data mining process, 2007 IEEE/WIC/ACM International Conference on Web Intelligence, 2007, pp. 163–169.

![](/api/attachments/PBPDB8UV/fulltext/images/e75bf664aaceb00e52449f40c7f9969a0b5d01e75ff97c49aa2a336058193c57.jpg)

Professor Yuefeng Li is the Leader of the eDiscovery Lab, Queensland University of Technology (QUT), Australia. He has been recognized in the areas of Web Intelligence, Text Mining and Data mining, and has been an active contributor to the development of these exciting research areas. He has published over 140 refereed papers (including 43 journal papers). He has demonstrable experience in leading large-scale research projects and has achieved many established research outcomes that have been published and highly cited in many signi<sup>fi</sup>cant Journals and Conferences (e.g., IEEE TKDE, Decision Support Systems, Journal of MIS, KDD, ICDM, CIKM and WI conferences). He has been a program chair of several International

Conferences and workshops (AMT05, ATM06, RSKT09, WI-IAT 2010 workshops). He is currently an Associate Editor of the International Journal of Pattern Recognition and Arti<sup>fi</sup>cial Intelligence, and an Associate Editor of the IEEE Intelligent Informatics Bulletin.

![](/api/attachments/PBPDB8UV/fulltext/images/f20432d4f434f6241aa9b60b4109002944e87d0ac9a0b17d84ccf3ed73ad7915.jpg)

Dr. Xujuan Zhou is a Senior Research Assistant in the School of Electrical Engineering and Computer Science at the Queensland University of Technology, Australia. She holds a Ph.D. from Queensland University of Technology, Australia in 2009. Her current research interests are focused on information <sup>fi</sup>ltering, data mining and web intelligence. Dr. Zhou is the author of more than 10 refereed international journals and conference papers.

Professor Peter Bruza holds a PhD in mathematics and computer science from the University of Nijmegen, The Netherlands (1993). Since graduating, he is primarily known for his development of formal models of information retrieval. In recognition of his research contribution in this <sup>fi</sup>eld, he was appointed program co-chair of the premier international conference in information retrieval – ACM SIGIR – in 2004. He serves on the international editorial boards of the “Journal of Applied Logic”, (Elsevier) “Information Retrieval”, (Springer) “The Logic Journal of IGPL” (Oxford University Press) and the book series “Information Science and Knowledge Management” (Springer). His current research turns around the question of how to develop information-processing technology, which is aligned with human cognition. This is a cross disciplinary enterprise spanning the <sup>fi</sup>elds of information retrieval, computation al linguistics, applied cognition, logic and quantum theory.

![](/api/attachments/PBPDB8UV/fulltext/images/229d07126caa2207d92781278055df479985180c9f7dc22ce5817edcb146cfa8.jpg)

Dr. Yue Xu is an Associate Professor in the School of Electrical Engineering and Computer Science at the Queensland University of Technology (QUT), Australia. She is also a co-leader of the eDiscovery Lab at QUT. Her current research interests are focused on data mining and web intelligence, She has made important contributions to the areas of association rule mining and web-based recommender systems. Dr. Xu has published over 100 refereed papers covering research areas of association rule mining, recommender systems, text mining, and cross-language information retrieval, some of which were published in major conferences such as ICDM, CIKM, HT, PAKDD, and WI conferences. She has been a program committee mem-

ber for many conferences and the workshop chair of the International Workshop on Web Personalization, Reputation and Recommender Systems from 2007 to 2011.

![](/api/attachments/PBPDB8UV/fulltext/images/db774460782c59eb6f244f737a64a95238785dd8d86fcfc0bef93931881de943.jpg)

Dr. Raymond Y.K. Lau is an Assistant Professor in the Department of Information Systems at City University of Hong Kong. He holds a Ph.D. in Information Technology from Oueensland University of Technology, Australia, He has worked at the academia and the ICT industry for over 20 vears. He is the author of over, 100 refereed interna: tional journals and conference papers. His research work has been published in renowned journals such as ACM Transactions on Information Systems, IEEE Transactions on Knowledge and Data Engineering, IEEE Internet Computing, Journal of MIS, Decision Support Systems, etc. His research interests include Information Retrieval, Text Mining, and Agent-Mediated e-Commerce. He is the asso-

ciate editor of the International Journal of Systems and Service-Oriented Engineering. He is a senior member of the IEEE and the ACM respectively.
