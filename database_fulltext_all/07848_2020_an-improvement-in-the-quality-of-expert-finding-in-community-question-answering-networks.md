---
otero_id: 7848
otero_key: "UNRYX7WW"
title: "An improvement in the quality of expert finding in community question answering networks"
authors: "Mahdi Dehghan; Ahmad Ali Abin; Mahmood Neshati"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113425"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

An improvement in the quality of expert finding in community question answering networks

Mahdi Dehghan, Ahmad Ali Abin, Mahmood Neshati

Decision Support Systems

![](/api/attachments/UNRYX7WW/fulltext/images/203dc38b2ea8e6923c11250e5985e10088cbcb95a6500415323deb1c27e90e74.jpg)

PII: S0167-9236(20)30180-9

DOI: https://doi.org/10.1016/j.dss.2020.113425

Reference: DECSUP 113425

To appear in: Decision Support Systems

Received date: 5 May 2020

Revised date: 1 September 2020

Accepted date: 13 October 2020

Please cite this article as: M. Dehghan, A.A. Abin and M. Neshati, An improvement in the quality of expert finding in community question answering networks, Decision Support Systems (2020), https://doi.org/10.1016/j.dss.2020.113425

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# An Improvement in the Quality of Expert Finding in Community Question Answering Networks

Mahdi Dehghan<sup>a</sup>, Ahmad Ali Abin<sup>a,\*</sup>, Mahmood Neshati<sup>a</sup>

<sup>a</sup>Faculty of Computer Science and Engineering, Shahid Beheshti University, Tehran, Iran

## Abstract

Expert finding in Community Question Answering (CQA) networks such as Stack Overflow is a practical issue facing a challenging problem called vocabulary gap. A widely used approach to overcome this problem is translation model. Different from prior works that only consider the relevancy of translations to a query, we intend to diversify query translations for better coverage of query topics. In this work, we have utilized the idea of clustering to group relevant translations to a given query into different clusters and then select representatives from each cluster as a set of diverse translations. We have proposed two new approaches to cluster translations. In the first one, the Mutual Information was primarily utilized as a similarity measure during clustering. In the second approach, the relevant translations are embedded in a topic space and then clustered in that space. After clustering, we propose two batch and sequential methods to select a diverse set of translations from the resultant cluster . The batch method selects the top most relevant translations from each cluster proportional to the relevancy of that cluster to the user query. The sequential one selected ones. Finally, to rank users, a regression model was utilized to learn how expert and non-expert users differ in using a set of diverse translations in their documents. Experiments on a large dataset generated from Stack Overflow demonstrate that the proposed methods improve the ranking performance over baselines in the expert finding.

Keywords: Expert finding, Question answering, Stack Overflow, Translations diversification 2010 MSC: 00-01 99-00

## 1. Introduction

Expert finding is an well-studied problem in Information Retrieval (IR) research which has attracted the attention of many researchers [1, 2]. Given a user query, the focus of expert finding is to address the task of providing an ordered list of experts in the field of the given query. Finding talented people has found many applications in Community Question Answering (CQA) networks [3, 4, 5]. Stack Overflow is one the most popular CQA websites. In Stack Overflow, users can post questions and answers, leave comments and determine the importance and quality of posts by voting and choosing the accepted answer. Any questioner should assign one or more tags to his question to identify the skills needed for answering the question.

The tags associated with each question are considered as queries and a set of answers given by users are used as textual expertise evidences. Finding talented people in Stack Overflow is a challenging task due to the term mismatch between the query and textual expertise evidence (i.e. answers in Stack Overflow) of candidates [4]. In fact, an expert in a specific tag like “OSX” domain, rarely uses the word “OSX” in his answers, instead, he uses a set of words (such as “mac”, “os”, “apple”, etc.) that make the concept of “OSX” more specialized.

So far, multiple research studies has been conducted to overcome the vocabulary gap issue by using translation models [6, 4, 7]. Although translation models have been successful in solving this: 1) they did not cover query topics as much as possible. Our experiments indicate that the more a set of translations cover important query topics, the less the effect of the VG will be, 2) they did not efficiently utilize a set of translations to estimate the expertise of candidates.

In this work, we investigate the effectiveness of translations diversification on the quality of expert finding. To this end, we extract relevant translations to each query in the first step. Next, we cluster the translations to extract a set of representative as a diverse set of translations. Finally, for a better ranking of candidates, we construct a regression model to learn how expert and non-expert users differ in using a set of diverse translations in their documents. Experiments on a large dataset gathered from Stack Overflow show the effectiveness of the proposed methods against the baselines.

## 1.1. Related work

Expert finding as a well-studied field in information retrieval, addresses the task of identification and ranking knowledgeable people in the subject of user query. Several models in literature have been proposed to solve this task [8], [9]. Expert finding was studied in multiple domains including organizations [6, 10], bibliographic networks [11, 12, 13], CQA networks [3, 1, 14], social networks [15, 16] and etc.

Neshati et al. [17] have addressed the task of future expert finding with respect to the expertise evidence in the current time in Stack Overflow. They proposed a supervised learning framework in order to predict the best ranking of experts in the future. They have defined four user behavior, and topic transition and examined the impact of them in the future expert finding problem.

Sotudeh et al. [14] have mined the shape of expertise and defined three knowledge levels including Advanced, Intermediate, and Beginner which are obtained by the ranking of users in a specific context. Further, they have defined 3 types of users: Non-expert, T-shaped, and C-shaped. With regard to the knowledge levels and the list of expertise that a user possesses, then they have determined the type of each user in the dataset. Finally, by proposing three approaches (DBA, EBA, and XEBA), they have evaluated the effectiveness of each approach on IR metrics.

Dehghan et al. [18] have proposed a new method for T-shaped expert finding on Stack Overflow. They have taken the temporal dynamics of expertise into account to mine the shape of expertise of each candidate expert by using an LSTM neural network. They have applied a filtering technique on top of the LSTM neural network to create a profile for each candidate exert. Finally, They have determined the shape of expertise for each candidate by using his profile.

One of the challenging problems in the CQA websites is the problem of VP which was previously investigated by Dargahi Nobari et al. in [4] and Dehghan et al. in [3]. Topic modeling [19], translation models [3, 4, 20] and word embedding [21] are considered as efficient solutions to overcome the VG problem.

Topic modeling is one of the well-known techniques that has been utilized in a large number of text mining tasks [22, 23]. Tang et al. [24] have proposed a novel topic modeling algorithm, named as Labeled Phrase Latent Dirichlet Allocation (LPLDA) considers simultaneously semantical label information and the ordering of words. Momtazi et al. [19] have proposed an approach based on topic modeling to find experts in TREC Enterprise track for 2005 and 2006 . They have extracted the main topics of documents in the collection using the Latent Dirichlet

Allocation method [25]. Then, they have used these topics in a probabilistic framework as an intermediary to rank candidates.

Karimzadehgan et al. [20] have proposed a statistical translation model to overcome the problem of VG between queries and documents. They have considered the normalized mutual information between two words as translation probability. They have also proposed a regularization of self-translation probabilities in order to overcome the problem of under-estimating self-translation (i.e. translate a word into itself) probabilities.

Dargahi et al. [4] have also proposed two translation models to overcome VG problem. They have translated query words into a set of relevant words during the translation stage and then used these translations to predict the best ranking of experts at the stage of score aggregation. Their first translation model was based on normalized Mutual Information and their second one was based on word embedding. In the score aggregation phase, they have used query translation to retrieve relevant documents and then ranked the candidates according to the total number of retrieved relevant documents. In these translation models, VG problem was somewhat resolved. However, the issue of diversification in translations has been ignored. Moreover, in the score aggregation phase, they have used a naive model to rank candidates. Authors in [2] utilized other features to improve the results. Accordingly, they have introduced the concept of vote share to determine the quality of the posts. Eventually, the posts with higher vote share would have more impact on the translation model.

Dehghan et al. [3] have proposed a translation model to overcome the VG problem. In the space is clustered a co-occurrence space. Representatives of each cluster in the co-occurrence space are returned to their parent cluster in the query space. Finally, candidate experts are retrieved and ranked using query translations which are selected using a probabilistic model.

To sum up, the previous works on expert finding problems can be categorized into two main groups. The first one [6, 26, 27]-which is older in comparison with the second group- mainly focused on the modeling of the expert finding and completely ignored VG (i.e. query term mismatch) problem. The second group proposed naive methods to overcome the vocabulary mismatch problem. Specifically, Momtazi and Naumann [19], proposed a topic modeling approach and Dargahi et.al [4] and Dehghan et.al [3] proposed a translation approach to solve VG problem.

Basically, in these methods, the user query is expanded with some few terms to reduce the gap between query and document terms. Although, these methods have been successful to improve the quality of expert finding but they ignore the diversification of selected terms to cover all aspects of the user query. Our paper is a natural extension of the second group to improve the quality of expert finding by selecting relevant as well as diverse translations for the user query.

## 1.2. Contributions of this work

The main contributions of this work are as follows:

1. We investigate the effectiveness of translation diversification approach on the quality of expert finding. In other words, we attempt to diversify query translations besides considering the relevancy of translations to a user query in order to overcome VG problem.

2. We use two clustering approaches and a regression model to learn how to effectively diversify the query translation.

3. We experiment on a large dataset gathered from Stack Overflow and show that the proposed methods can significantly outperform the state of the art [6, 19] as well as the best performing translation models [4, 3, 2] in terms of Mean Average Precision (MAP).

## 1.3. Organization of this paper

In Section 2, we will present the proposed method for expert finding. Details for the dataset, baseline models, evaluation measures, parameter setting, and implementation are given in Section 3. Discussion was presented in Section 4. The paper concludes with conclusions and future directions in Section 5.

## 2. The proposed method

Existing works in translation models only considered the relevancy of translations to the user’s query during expert finding. Such approaches could not provide acceptable results when the coverage of query topics by the relevant translations is low. In order to involve diversification in translation models, we retrieve relevant translations at first step, then we utilize the idea of data clustering to group the retrieved translations into different clusters and select representatives from the clusters as a set of diverse translations. The general idea behind the proposed method was summarized in Algorithm 1. As the algorithm shows, the proposed method ranks candidates in four steps. In the first step, it extracts a set of relevant translations $T _ { q } ^ { \mathrm { r e l } }$ for a given query $q$ from $D$ where D is a set of documents (see section 2.1). In the second step, $T _ { q } ^ { \mathrm { r e l } }$ is grouped into $k _ { q }$ different clusters $C _ { q } = \{ c _ { q } ^ { 1 } , . . . , c _ { q } ^ { k _ { q } } \}$ . Here we have two different approaches to do this, clustering based on MI (see section 2.2.1) and clustering in topic space (see section 2.2.2). In the next step, a diverse set of translations $T _ { q } ^ { \mathrm { d i v } }$ is selected from $C _ { q }$ . Here, we have two different approaches to do this, batch (see section 2.3.1) and sequential (see section 2.3.2). Finally, the proposed method ranks candidates using $T _ { q } ^ { \mathrm { d i v } }$ (see section 2.4). Due to the earlier explanations, we have four different translation models that consider both relevancy and Further details of the proposed methods will be $\prime _ { \lambda } ,$ lained in following sections. Also, Table 1

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 The proposed expert finding method. Input: Query q . Output: Sorted list of experts $E_{q}$ .   
1: procedure RANKEXPERTS(a)   
2: $D\gets$ Set of documents (answers) in CQA.   
3: Step1: $T_{q}^{\mathrm{rel}}\gets$ Extract relevant translations of $q$ from $D$ .   
4: Step2: $C_q\gets$ Cluster $T_{q}^{\mathrm{rel}}$ .   
5: Step3: $T_{q}^{\mathrm{div}}\gets$ Extract diverse translations from $C_q$ .   
6: Step4: $E_{q}\gets$ Rank candidates using $T_{q}^{\mathrm{div}}$ .   
7: return Sorted list of experts $E_{q}$ .
</div>

Table 1: Summary of notations.

<table><tr><td>Notation</td><td>Notation description</td></tr><tr><td>q</td><td>query</td></tr><tr><td>w.</td><td>word</td></tr><tr><td>x</td><td>word w. or query q</td></tr><tr><td> $T_q^{rel}$ </td><td>Set of relevant translations of query q</td></tr><tr><td> $T_q^{div}$ </td><td>Set of diverse translations of query q</td></tr><tr><td>D</td><td>Set of documents (Answers) in CQA</td></tr><tr><td> $C_q$ </td><td>Set of resultant clusters due to clustering set of relevant translations  $T_q^{rel}$ </td></tr><tr><td> $c_q^i$ </td><td> $i^{th}$  cluster in  $C_q$ </td></tr></table>

## 2.1. Step 1: Extraction of relevant translations

In the first step, we extract top- n most relevant translations for a query $q ( \mathrm { i } . \mathrm { e } . \ T _ { q } ^ { \mathrm { r e l } } )$ . We calculate mutual information (MI), which is a well-known measure for determining how much information the presence or absence of a term contributes to the relevancy of two words [4, 3, 20], between query q and each word $w _ { \bullet }$ in the set of documents D . We then normalize MI score to obtain $p _ { _ { M } } ( w _ { \bullet } \vert q )$ which is the translation $q$ $w _ { \bullet }$ the following equation.

$$
p _ {M} (N _ {\bullet} \mid q) = \frac {M I (q , w _ {\bullet})}{\sum_ {w _ {\bullet} ^ {\prime}} M I (q , w _ {\bullet} ^ {\prime})}\tag{1}
$$

where ${ M I } ( q , w _ { \bullet } )$ is calculated as the following.

$$
M ^ {I I} (q, w _ {\bullet}) = \sum_ {A _ {q} = 0, 1} \sum_ {A _ {w _ {\bullet}} = 0, 1} p \left(A _ {q}, A _ {w _ {\bullet}}\right) \log \frac {p \left(A _ {q} , A _ {w _ {\bullet}}\right)}{p \left(A _ {q}\right) p \left(A _ {w _ {\bullet}}\right)}\tag{2}
$$

where $A _ { _ q }$ and $A _ { \nu _ { \bullet } }$ are two binary variables indicating the event of occurrence of $q$ and $w$ in a document (i.e. answer) d $\in { \cal D }$ . At the end of this step, we have extracted a set of translations $T _ { q } ^ { \mathrm { r e l } }$ that is highly relevant to query $q$ .

## 2.2. Step 2: Clustering relevant translations

In the second step, we cluster $T _ { q } ^ { \mathrm { r e l } }$ into $k _ { q }$ different clusters $C _ { q } = \{ c _ { q } ^ { 1 } , . . . , c _ { q } ^ { k _ { q } } \}$ . Here, the idea is to group similar translations into same cluster for a better translations diversification. To this end, we propose two methods to cluster $T _ { q } ^ { \mathrm { r e l } }$ . In the following, each method is discussed in more details.

## 2.2.1. Method 1: Clustering based on MI

In this solution, for each query q we group $T _ { q } ^ { \mathrm { r e l } }$ into different clusters of translations by utilizing MI as similarity measure. We refer to this method as CMI in the rest of the paper. It is obvious that different clusters are representatives for different query topics, and semantically similar translations will be grouped in the same cluster. By choosing translations from different clusters, we expect to cover more query topics. $\mathrm { \bf S o } .$ , the first step in this solution is to determine how much the words in $T _ { q } ^ { \mathrm { r e l } }$ are semantically similar. To this end, we utilize $p _ { _ { \mathrm { M } } } ( w _ { j } \mid w _ { i } )$ which is the $w _ { i }$ $w _ { j }$ $p _ { _ { M } } ( w _ { j } \mid w _ { i } )$ is estimated by using the following equation.

$$
p _ {M I} \left(w _ {j} \mid w _ {i}\right) = \frac {M I \left(w _ {i} , w _ {j}\right)}{\sum_ {w ^ {\prime} \in T _ {q} ^ {\mathrm{rel}}} M I \left(w _ {i} , w ^ {\prime}\right)}\tag{3}
$$

where $M I ( w _ { i } , w _ { i } )$ is calculated in the following way.

$$
M I \left(w _ {i}, w _ {j}\right) = \sum_ {A _ {w _ {i}} = 0, 1} \sum_ {A _ {w _ {j}} = 0, 1} p \left(A _ {w _ {i}}, A _ {w _ {j}}\right) \log \frac {p \left(A _ {w _ {i}} , A _ {w _ {j}}\right)}{p \left(A _ {w _ {i}}\right) p \left(A _ {w _ {j}}\right)}\tag{4}
$$

where binary variables ${ \bf \iota } _ { { { \boldsymbol \kappa } _ { i } } }$ and $A _ { w _ { j } }$ indicate the event of occurrence of words $w _ { i }$ and $w _ { j }$ in document (i.e. answer) $d \equiv D$ . Having the pairwise similarity of translations $p _ { _ { M } } ( w _ { j } \mid w _ { i } )$ for all $w _ { i } , w _ { j } \in T _ { q } ^ { \mathrm { r e l } }$ calculated using Eq. (3), we cluster $T _ { q } ^ { \mathrm { r e l } }$ into $k _ { q }$ groups of translations using Algorithm 2. As the algorithm shows, the proposed clustering method selects a random word $w _ { \bullet }$ from among $T _ { q } ^ { \mathrm { r e l } }$ at the first step, then it calculates the similarity of $w _ { \bullet }$ to each cluster $c _ { q } ^ { i } \in C ^ { q } , i = 1 , . . . , k _ { q }$ and selects the cluster with maximum similarity as the winner cluster in the second step. Finally if the maximum similarity is higher than a predefined threshold then the word $w _ { \bullet }$ will be assigned to the winner cluster, otherwise it will remain as a member of its cluster. This process will be completed when no change exists in the clusters assignment or the total number of epochs exceeds a maximum epoch. After clustering, we expect that each cluster ${ c _ { q } ^ { i } , i = 1 , . . . , k _ { q } }$ contains translations that are semantically similar and cover same query topics.

Algorithm 2 The method proposed for translations clustering based on MI. Input: Set of n top most relevant translations $T _ { q } ^ { \mathrm { r e l } }$ to query $q$ , The similarity matrix $P \equiv [ p _ { i j } ] _ { n \times n }$ where $p _ { i j }$ is the probability of translating word $w _ { i } \in T _ { q } ^ { \mathrm { r e l } }$ into $w _ { j } \in T _ { q } ^ { \mathrm { r e l } } \ \mathrm { ~ ( i . e . ~ } \ p _ { _ { \mathrm { M I } } } ( w _ { j } \mid w _ { i } ) \ )$ and the input parameter $\beta$ that controls when a new cluster should be created. Output: Set of clusters $C _ { q } = \{ c _ { q } ^ { i } \} , i = 1 , . . . , k _ { q }$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
procedure CLUSTERING( $P, T_{q}^{rel}, \beta$ )

2:  $T_{q}' \leftarrow T_{q}^{rel}$ $w_{\bullet} \leftarrow$  Select a random word from  $T_{q}'$ .

4:  $c_{q}^{1} \leftarrow c_{q}^{1} \cup \{w_{\bullet}\}$ $T_{q}' \leftarrow T_{q}' / \{w_{\bullet}\}$ $\triangleright$  Remove word  $w_{\bullet}$  from  $T_{q}'$ 

6: Initialize the set of clusters  $C_{q}$  with  $c_{q}^{1}$ .

loop = 1

8: while loop ≠ maxLoop and cluster assignments change do

while  $T_{q}'$  isn't empty

10:  $w_{\bullet} \leftarrow$  Select a random word from  $T_{q}'$ .

 $T_{q}' \leftarrow T_{q}' / \{w_{\bullet}\}$ $\triangleright$  Remove word  $w_{\bullet}$  from  $T_{q}'$ 

12:  $c_{q}^{winner} \leftarrow argmax_{c \in C_{q}} \frac{\sum\limits_{u \in c} P(u, w_{\bullet})}{|c|}$ $\triangleright |c|$  means number of words in cluster

c

 $s \leftarrow \max\limits_{c \in C_{q}} \frac{\sum\limits_{u \in c} P(u, w_{\bullet})}{|c|}$ 

14: if  $s &gt;= \beta$  then
</div>

Remove $w _ { \bullet }$ from its previous cluster $c _ { q } ^ { p r e \nu }$

$$
c _ {q} ^ {\text { winner }} \leftarrow c _ {q} ^ {\text { winner }} \cup \{w _ {\bullet} \}
$$

else

Create new cluster $c _ { n e w }$

$$
c _ {q} ^ {\text { new }} \leftarrow c _ {q} ^ {\text { new }} \cup \{w _ {\bullet} \}
$$

$$
C _ {q} \leftarrow C _ {q} \cup \left\{c _ {q} ^ {\text {new}} \right\}
$$

loop ← loop + 1

22:

$$
T _ {q} ^ {\prime} \leftarrow T _ {q} ^ {\mathrm{rel}}
$$

return Set of clusters $C _ { q }$

## 2.2.2. Method 2: Clustering in topics space

The second method for clustering is an embedding approach that clusters relevant translations in a new space consisting of $\mathbf { m _ { \lambda } } \mathbf { . m }$ topics of query (This method referred to as CTS in the rest of this paper). In this method, in order to group relevant translations into different clusters, we create a new space of main topics of the given query, then embed words in that space. Two words with close vectors in this space are more relevant than the ones with far vectors. We embed relevant translations of the given query by estimating their relevancy to the main topics of the given query. Therefore, the first $\mathbf { S } \cdot \mathbf { \partial } ^ { \mathbf { 2 } } \mathbf { 0 }$ is to extract main topics of query $q$ and translations $w _ { i } \in T _ { q } ^ { \mathrm { r e l } } : i = 1 , 2 , . . . , n$ in order to embed words in query main topic space. Given any word $x \ ( x$ may be a query q or a translation $w _ { i } \mathrm { ~ , ~ }$ ), we extract the main topics of x in the following way: In the first step, we use LDA algorithm in order to group documents $d _ { i } \in D : i = 1 , 2 , . . , N$ into M topics to estimate the probability of topic $z _ { i } \in Z : i = 1 , . . . , M$ given x (i.e. ${ \hat { p } } ( z _ { i } \mid x ) )$ . Having $\hat { p } ( z _ { i } \mid x )$ , we extract the main topics covered by x using Eq. (5). This equation labels topic $z _ { i }$ as main topic for x (i.e. x is highly related to $z _ { i } )$ if the probability of $z _ { i }$ given x is higher than the prior probability of $z _ { i }$ [28].

$$
\mathcal {J} (x, z _ {i}) = \left\{ \begin{array}{l l} 1 & \text { if } \hat {p} (z _ {i} \mid x) > p (z _ {i}) \\ 0 & \text { otherwise } \end{array} \right.\tag{5}
$$

Let $A \in \mathbb { R } ^ { M }$ be a column vector where being 1 at each position j means that topic $z _ { j }$ is a main topic for query $q$ and $A ^ { \prime } \in \mathbb { R } ^ { M }$ be another column vector where being 1 at each position l means that the topic $z _ { l }$ is a main topic of translation $w _ { i }$ . Let $m = \textstyle \sum _ { j = 1 } ^ { M } A [ j ]$ be the total number of main topics extracted for query $q$ . For example, consider we have grouped all documents into 5 topics $z _ { 1 } , z _ { 2 } , . . . , z _ { 5 }$ . Assuming $z _ { 2 }$ and $z _ { 4 }$ are the main topics of a particular query $q$ and $z _ { 2 }$ , $z _ { 3 }$ and $z _ { 5 }$ are the main topics of a particular translation $w _ { i }$ , the corresponding topics indication vector $\boldsymbol { A } = [ 0 , 1 , 0 , 1 , 0 ] ^ { T }$ and $A ^ { \prime } = [ 0 , 1 , 1 , 0 , 1 ] ^ { T }$ <sub>1</sub> <sub>3</sub> <sub>52</sub> <sub>4</sub><sup>z</sup> <sup>z</sup> <sup>z</sup> <sup>z</sup> <sup>z</sup> <sub>1</sub> <sub>42</sub> <sub>3</sub> <sub>5</sub><sup>z</sup> <sup>z</sup> <sup>z</sup> <sup>z</sup> <sup>z</sup>

After extracting main topics for query q and translations $\because \in T _ { q } ^ { \mathrm { r e l } } : i = 1 , 2 , . . . , n$ , we embed each translation $w _ { i }$ into a new ( 1) m  -dimensional vector $V = [ \nu _ { 1 } , . . . , \nu _ { m } , \nu _ { m + 1 } ] ^ { T }$ , where $\nu _ { _ { o } } : o = 1 , . . , m$ identifies the coverage of $w _ { i }$ on the topic corresponding to $o ^ { \mathfrak { t h } }$ non-zero element of A . The last dimension $\nu _ { m + 1 } = 1 - \textstyle \sum _ { o = 1 } ^ { m } \nu _ { o }$ indicates the amount of non-coverage of query topics by $w _ { i }$ . Calculation of $[ \nu _ { 1 } , . . . , \nu _ { m } , \nu _ { m + 1 } ] ^ { T }$ is done as indicated in following equations:

$$
v _ {o} = \left\{ \begin{array}{l l} p (z _ {i d x} \mid w _ {i}) & o \neq m + 1, A [ i d x ] = 1, A ^ {\prime} [ i d x ] = 1 \\ 0 & o \neq m + 1, A [ i d x ] = 1, A ^ {\prime} [ i d x ] = 0 \\ \sum_ {l = 1} ^ {M} P (z _ {l} \mid w _ {i}) & o = m + 1 \\ \left\{ \begin{array}{l} A ^ {\prime} [ ] = 0 \\ A ^ {\prime} [ ] = 1 \end{array} \right. \end{array} \right.\tag{6}
$$

where idx is the position of $o ^ { \mathfrak { t h } }$ non-zero topic in A and $p ( z _ { i d x } \mid \boldsymbol { w } _ { i } )$ is the probability of topic $z _ { i d x }$ given $w _ { i }$ which is normalized on main topics of $w _ { i }$ and calculated by using Eq. (7):

$$
p(z_{idx}\mid w_{i}) = \frac{\hat{p} (z_{idx}\mid w_{i})}{\sum_{\substack{j = 1\\ A^{\prime}[j] = 1}}^{M}\hat{p} (z_{j}\mid w_{i})}\tag{7}
$$

After embedding each translation $w _ { i }$ into the new space, we group them in $k _ { q }$ clusters ${ c _ { q } ^ { i } , i = 1 , . . . , k _ { q } }$ which are used for translation diversification in the next step.

## 2.3. Step 3: Translations diversification

In the third step, we try to select most diverse set of translations $T _ { q } ^ { \mathrm { d i v } }$ from $C _ { q } = \{ c _ { q } ^ { 1 } , . . . , c _ { q } ^ { k _ { q } } \}$ (i.e. the result of clustering obtained from previous step). Here, the idea is to increase the coverage of query topics by choosing a diverse set of translations from $C _ { q }$ . By this, we hope the final accuracy of expert finding to be enhanced by choosing experts with a wider coverage of query topics. To this end, we propose two batch and sequential methods to select a diverse set of translations from $C _ { q }$

## 2.3.1. Method 1: Batch translations diversification

In the batch strategy, to select a diverse set of translations $T _ { q } ^ { \mathrm { d i v } }$ from the resultant clusters $C _ { q } = \{ c _ { q } ^ { 1 } , . . . , c _ { q } ^ { k _ { q } } \}$ , we choose some representative translations from each cluster. The number of representatives selected from each cluster $c _ { q } ^ { i }$ is determined by using the following equation.

$$
\text {share} ^ {c _ {q} ^ {l}} = \left[ \frac {\sum_ {w _ {\bullet} \in c _ {q} ^ {i}} p _ {M I} (w _ {\bullet} \mid q)}{\sum_ {j = 1} ^ {k _ {q}} \sum_ {w _ {\bullet} \in c _ {q} ^ {j}} p _ {M I} (w _ {\bullet} \mid q)} \times n ^ {\prime} \right]\tag{8}
$$

where [.] operator rounds the input argument to its nearest integer and $n ^ { \prime }$ is the total number of translations that we tend to diverse for each query. In fact, sharing translations gives more chance to the more relevant clusters to be presented in the final set of translations. After determining the share of each cluster $\boldsymbol { c } _ { q } ^ { i } , i = 1 , . . . , k _ { q }$ , the words of that cluster are sorted in descending order based on their translation probabilities into the query (i.e. $p _ { _ { M } } ( w w _ { \bullet } \vert q ) )$ and the $s h a r e ^ { c _ { q } ^ { i } }$ top words are returned as the representatives (i.e. diverse translations selected from $c _ { q } ^ { i } )$ of that cluster.

## 2.3.2. Method 2: Sequential translations diversification

The sequential method for translations diversification is based on concepts in topic modeling. In this method, we iteratively choose an optimal translation to cover important query topics which are less covered by the previously selected translations. Let $w _ { 1 } , w _ { 2 } , . . . , w _ { t - 1 } \in T _ { q } ^ { \mathrm { d i v } }$ be the previously selected translations for query $q$ and $w _ { t }$ be the $t ^ { \mathrm { t h } }$ candidate translation. At each step t , we utilize the main topics extracted for query $q$ and translations $w _ { i } : i = 1 , . . , t$ to select the optimal translation. The main topics for query q and translations $w _ { i } : i = 1 , . . , t$ are extracted by utilizing the method described in Section 2.2.2.

Let $A _ { x } \in \mathbb { R } ^ { M }$ be a column vector in which being 1 at each position l indicates that the topic $z _ { l }$ is a main topic of word x (where x may be query q or a translation $w _ { i } : i = 1 , . . . , t )$ and let $\hat { p } ( z _ { j } \mid x )$ be the probability of any topic $z _ { j } : j = 1 , . . . , M \mathrm { g i v } _ { \tt c l t } \chi$ which is calculated during extraction of main topics. We calculate the normalized probability of each main topic $z _ { l }$ given word x (i.e. $p ( z _ { l } \mid x ) ) ,$ ) using the following equation:

$$
p(z_{l}\mid x) = \frac{\hat{p}(z\mid x)}{\sum_{\substack{j = 1\\ A_{x}^{\prime}i] = 1}}^{T}j(z_{j}\mid x)} -\tag{9}
$$

The proposed method for sequential translations diversification is illustrated in Algorithm 3. As this algorithm shows, we select the most relevant translation from each cluster and score it by using Eq. (10). Then we select translation with the maximum score (referred to as the winner translation) as the first best and remove it from the winner cluster. Next, the best translations are selected sequentially in the following way. At each iteration, we select the most relevant translation from each cluster and choose from among them the translation with the maximum relevancy to one of the query topics (i.e. $_ { F } ( \mathfrak { z } | q ) p \big ( w _ { \bullet } | q , z \big ) \rangle$ and the minimum relevancy to the topics covered by the previously selected translations (i.e. $\prod _ { \left\{ w _ { \bullet } ^ { \prime } \in T _ { q } ^ { \operatorname { d i v } } \right\} } \left( 1 - p ( w _ { \bullet } ^ { \prime } \mid q , z ) \right) )$

$$
S(q,w_{t},T_{q}^{\text{div}}) = \lambda \underbrace{\sum_{\substack{j = 1\\ A_{q}[j] = 1}}^{M}\left(p\left(z_{j} \mid q\right)p\left(w_{t} \mid q,z_{j}\right)\prod_{\left\{w_{\bullet}^{\prime}\in T_{q}^{\text{div}}\right\}}\left(1 - p\left(ww_{\bullet}^{\prime} \mid q,z_{j}\right)\right)\right)}_{\text{Diversification Score}} + (1 - \lambda)\underbrace{p_{MI}(w_{t} \mid q)}_{\text{Relevancy Score}}\tag{10}
$$

where controls the amount of diversification, $\boldsymbol { p } _ { \ u { M } } \left( \boldsymbol { w } _ { t } \mid \boldsymbol { q } \right)$ indicates the translation probability of word $w _ { t }$ to query $q$ calculated by Eq. (3), $p ( z | q )$ shows the relevancy of query $q$ to topic z calculated by using Eq. (9), and $p ( w _ { \bullet } \mid q , z )$ shows how much the word $w _ { \bullet }$ covers topic z from query $q$ which is obtained using the following equation:

$$
p (w _ {\bullet} \mid q, z) \propto p (w _ {\bullet} \mid q) \times p (z \mid w _ {\bullet})\tag{11}
$$

where $p ( z \mid w _ { \bullet } )$ is calculated using Eq. (9), and $p ( w _ { \bullet } \mid q ) = { \frac { 2 \times { \Big ( } n - R _ { w _ { \bullet } } + 1 { \Big ) } } { n \times { \Big ( } n + 1 { \Big ) } } }$ , where $R _ { { _ w _ { \bullet } } }$ is the ranking of word $w _ { \bullet }$ in $T _ { q } ^ { \mathrm { r e l } }$ and n is the total number of initial translations obtained in Section 2.1.

Algorithm 3 The proposed method for sequential translations diversification. Input: Query q , set of clusters $C _ { q } = \{ c _ { q } ^ { 1 } , . . . , c _ { q } ^ { k _ { q } } \}$ and $n ^ { \prime }$ , totoal number of translations that we want to diverse for each query. Output: Set of diverse translations $T _ { q } ^ { \mathrm { d i v } }$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: procedure SEQUENTIALDIVERSIFICATION ( $q, C_{q}, n'$ )

2:  $T_{q}^{div} = \emptyset$ 

3: for  $i = 1...n'$  do

4: maxScore  $\leftarrow 0$ 

5: for  $j = 1...k_{q}$  do

6:  $w_{\bullet} \leftarrow$  The most relevant translation selected from cluster  $c_{q}^{j}$ 

7: score  $\leftarrow$  Score( $q, w_{\bullet}, T_{q}^{div}$ ) By using Eq. (10)

8: if score &gt;maxScore then

9: maxScore  $\leftarrow$  score

10: winnerTranslation  $\leftarrow w_{\bullet}$ 

11: idx  $\leftarrow j$ $\triangleright$  Keep the index of winner cluster

12:  $T_{q}^{div} \leftarrow T_{q}^{div} \cup \{winnerTranslation\}$ 

13:  $c_{q}^{idx} \leftarrow c_{q}^{idx} / \{winnerTranslation\}$ 

14: return Set of diverse translations  $T_{q}^{div}$ .
</div>

## 2.4. Step 4 : Ranking of candidates

The ranking is an important step playing a significant role in the accuracy of expert finding. During the ranking, we utilize the query translations to estimate the expertise of candidates. The ranking method proposed in [4], referred to as Naive method, is a successful model in the expert ranking. For each query $q$ , a Naive ranking method retrieves all documents containing at least one word from its translations $( T _ { q } ^ { \mathrm { r e l } } )$ in the first step. Next, it scores candidates based on the number of retrieved documents that he/she authored. Finally, it sorts candidates based on their scores [4] and returns them as the final ranked results.

The ranking method presented in [4], does not consider the fact that experts and non-expert users may differ in the way they are using expertise keywords in their documents. In this section, a new ranking approach is proposed which tries to discover how expert and non-expert users differ in using a set of discriminative keywords in their $\mathbf { a } \mathbf { c }$ cuments. Therefore, for each query $q$ , we consider its diverse translations $T _ { q } ^ { \mathrm { d i v } }$ as $\therefore \sin ,$ constructed based on the behavior of expert and non-expert users in answering (writing documents) in the following way. For each user having at least one answer, we will create a training vector based on term frequency (TF) of discriminative keywords (diverse translations $T _ { q } ^ { \mathrm { d i v } } \ .$ ) in his answers. If he is expert in quer ining vector will be labeled as 1 indicating the pattern of keywords generated by an expert. Otherwise, that vector will be labeled as 0 showing the user does not use such a pattern for keywords usage in his answers. After generating the training data, we train a multi-layer neural network $\aleph _ { q }$ for each query $q$ , which consists of an input layer with the number of neurons equals to the total number of diverse translations $n ^ { \prime }$ , a hidden layer containing ten neurons and an output layer with a single neuron.

We use the trained network $\aleph _ { q }$ during expert ranking in the following way: For each candidate in query $q$ , we create a test vector based on the term frequency of discriminative keywords (diverse translations $T _ { q } ^ { \mathrm { d i v } } )$ in his answers. The output of the trained network $\aleph _ { q }$ shows the expertise degree of that candidate in the range of 0 to 1. By sorting outputs in descending order, the quality of experts ranking can be evaluated in terms of MAP, P@K, and so on.

To sum up, as we described in the Section 2, there are four different combinations of the proposed method that consider both relevancy and diversity in translating a given query. We explain when to use which combination of the proposed method will produce more desired results. Both CMI and CTS are utilized to create boundaries between the relevant translations. In CMI we utilize a clustering approach to create these boundaries but in CTS we first embed each word in a topic space and then cluster each translation in the new main topic space of query. Actually, CTS is more intelligent because we consider relevancy to query during making these boundaries. In other words, in CTS we consider how much two translation are similar to each other and to the query word but in the CMI we only consider the relevancy of two translations to each other. Considering relevancy to query can be beneficial for creating relevant translations. After clustering relevant translations, we proposed two different approaches to select some representatives from clusters. In the first one, which is a batch method, we choose the most relevant translations from each cluster. Share of each cluster in selecting representatives are specified based on its relevancy to the query. In the second one, which is a sequential approach, we first select the most relevant translation from each cluster. After that we calculate a score for each one based on its relevancy to the query and how it covers main query topics. Eventually, the translation with maximum score is selected. We keep doing this process until selecting enough amount of translations. As it is obvious the second approach is more intelligent but it is a little time consuming than the batch method. Therefore, we expect to get better result in the presence of CTS method and sequential approach.

## 3. Experimental setup

In this section, the effectiveness of the proposed method is investigated in comparison with state-of-the-art approaches in the expert finding. Details for the dataset, baseline models, evaluation measures, parameter setting, and implementation are given in the following sections.

## 3.1. Dataset

We have used a subset of questions and their corresponding answers posted to Stack Overflow<sup>1</sup> between August 2008 and March 2015 in the domain of “JAVA” and “PHP” as the dataset for expert finding. Both “JAVA” and “PHP” are two popular domains that including a large number of documents. This dataset includes 810,071 questions and 1,510,812 answers related to “JAVA” domain and 714, 476 questions and 1, 298,107 answers related to “PHP” domain. The generated dataset consists of 200 tags which have highly occurred with “JAVA” or “PHP” tags. To be more specific, we have considered 100 top tags which have highly occurred with “java” and 100 top tags having most co-occurrence with “PHP” as candidate queries for expert finding. To label experts in a particular tag, two conditions must occur simultaneously [3]: having at least 10 accepted answers and, acceptance ratio higher than average acceptance ratio in dataset ( 40% in both “JAVA” and “PHP” domains [3]). The test collection will be uploaded on Github<sup>2</sup>.

## 3.2. Baseline Models

We have compared the proposed method against eight well-known methods in expert finding literature. The first baseline method is a profile-based language model (referred to as LM1 in the rest of this paper) and the second one is a document-based language model (referred to as LM2 in the rest of paper) [6]. Both LM1 and LM2 are set up with the JM smoothing parameter equals to 0.5. The third and fourth baseline methods [4] are two models which are selected owing to the fact these approaches are considering VG issue in expert finding which makes them a sufficient baseline to compare the proposed approaches with. These methods are based on word embedding and mutual information and referred to as WE and MI, respectively. The fifth and sixth baselines method [2] are extensions of two proposed translations methods in [4] which are referred to as WE(VS) and MI(VS). The seventh baseline method [3]is a clustering translation model referred to as CTM in the rest of this paper. CTM tries to overcome the VG problem by diversifying query translations to improve the quality of final ranking. The last baseline method [19] is based on topic modeling referred to as TM in the rest of this paper. TM also tries to cope with VG problem in expert finding. However, it uses a different approach.

## 3.3. Evaluation Measures

In this section, the evaluation metrics for evaluating the quality of results are introduced. We have used Coverage, Confidence and $\mathrm { F _ { s c o r e } }$ metrics [29] to compare the quality of translations.

The more topics a set of translations covers, the better the result of expert ranking will be (i.e. Coverage). When two sets of translations cover the same query topics, the set with a larger number of translations per query topic is preferred (i.e. Confidence).

Let $T _ { q } ^ { \bullet }$ be a set of translations for a given query $q$ . The coverage measure of $T _ { q } ^ { \bullet }$ is defined as percentage of query topics (here, the query q ) covered by $T _ { q } ^ { \bullet }$ . To calculate the topic coverage of $T _ { q } ^ { \bullet }$ we need to determine how much a translation $w \in T _ { q } ^ { \bullet }$ covers the main topics of $q$ . Accordingly, in the first step we group documents $d _ { i } : i = 1 , 2 , . . , N$ into M topics $z _ { j } \in Z : j = 1 , . . , M$ using LDA algorithm and extract main topics $\smash { \ r _ { 0 , 1 } ^ { \sim } } \to \mathcal { W }$ as illustrated in Eq. (5). After extracting the main topics, we calculate the coverage of $\vec { \mathbf { \nabla } } _ { \pmb { q } } ^ { - 0 }$ using the following equation.

$$
\text { Coverage } (T _ {q} ^ {\bullet}, q) = \frac {\sum_ {z _ {j} \in Z} \left(\mathcal {J} (q , z _ {j}) \mathbf {1} _ {\{\sum_ {w _ {j} \in T _ {q} ^ {\bullet}} \mathcal {J} (w _ {j} , z _ {j}) \}}\right)}{\sum_ {z _ {j} \in Z} \mathcal {J} (q , z _ {j})}\tag{12}
$$

where $\mathbf { 1 } _ { \{ c o n d i t i o n \} } = 1$ if condition > 0. Also, we take the confidence of $T _ { q } ^ { \bullet }$ into account to measure the redundancy of translations in $\mathbf { c c } \ \mathrm { v e } \ \mathbf { . 1 . 3 }$ query topics. Confidence measure is defined in the following way:

$$
\text {Confidence} (T _ {q} ^ {\bullet}, q) = \frac {\sum_ {z _ {i} \in Z} \frac {\mathcal {J} (q , z _ {i}) \sum_ {w _ {j} \in T _ {q} ^ {\bullet}} \mathcal {J} (w _ {j} , z _ {i})}{n}}{\sum_ {z _ {i} \in Z} \left(\mathcal {J} (q , z _ {i}) \mathbf {1} _ {\{\sum_ {w _ {j} \in T _ {q} ^ {\bullet}} \mathcal {J} (w _ {j} , z _ {i}) \}}\right)}\tag{13}
$$

where $\mathbf { 1 } _ { \{ c o n d i t i o n \} } = 1$ if condition > 0 . The last measure is $\mathrm { F _ { s c o r e } }$ that is defined as the harmonic mean of coverage and confidence as follows:

$$
F _ {\text { score }} = \frac {2 \times \text { Coverage } (T _ {q} ^ {\bullet} , q) \times \text { Confidence } (T _ {q} ^ {\bullet} , q)}{\text { Coverage } (T _ {q} ^ {\bullet} , q) + \text { Confidence } (T _ {q} ^ {\bullet} , q)}\tag{14}
$$

In order to assess the quality of experts ranking, the precision at $k \ ( \boldsymbol { p } @ \boldsymbol { k } )$ and Mean Average Precision ( MAP ) that are two commonly used evaluation measures for ranking in IR, are employed in this work. The evaluation measure $p @ k$ for a given query q is the percentage of experts in the top k retrieved results.

$$
p @ k = \frac {\text { number   of   experts   in   the   top } k \text { retrieved   results }}{k}\tag{15}
$$

The MAP evaluation measure is defined as the mean value of Average Precision ( AP ) for all queries in test collection. For each query q , we define AP by using the following relation:

$$
A P = \frac {\sum_ {k = 1} ^ {| E _ {q} |} p @ k \times r e l (k)}{R}\tag{16}
$$

where $E _ { q }$ is ordered list of candidates for query $q , \mid E _ { q } \mid$ indicates the total number of candidates, R is the total number of real experts in the golden set, and rel k( ) is a binary function indicating the expertise of given candidate.

## 3.4. Parameters Setting and Implementation Details

To prepare Stack Overflow data for the next processing step, we did some preprocessing on data to remove HTML tags and scripts, remove stop-words, stem words occurred in documents, extract topics and so on. The Apache $\mathrm { \Delta } \mathrm { \omega } _ { \mathrm { - } } \mathrm { \Delta } \mathrm { \omega } _ { \mathrm { - } } 3$ Standard Analyzer was used to stop-words removal and words stemming. The well-known MALLET topic modeling package was used for topic done by using the Apache Lucene tool.

The first step in the proposed method is to extract n top most relevant translations $T _ { q } ^ { \mathrm { r e l } }$ to query q (Section 2.1). $\boldsymbol { \varGamma } _ { q } ^ { \mathrm { r e l } }$ will be diversified in the next steps to select a set of diverse translations $T _ { q } ^ { \mathrm { d i v } }$ . In this paper, we extract top- 200 relevant translations as $T _ { q } ^ { \mathrm { r e l } }$ which are candidates for diversification (i.e. n = 200 ). Because the proposed method takes both relevancy and diversity of translations into account, any word that is not highly relevant to the query has a lower chance to be presented at the final set of translations. It is a nice feature because the proposed method prevents the presence of translations unrelated to the query on the final set of translations. When we increase n , the irrelevant translations will have more chances to come up with the final results and this contradicts the basic principle of translation models.

In the first proposed method for clustering (i.e. CMI method described in Section 2.2.1), we have the parameter $\beta$ which is the minimum value of similarity for assigning data to clusters. When $\beta$ is greater than a maximum threshold, the number of clusters will be equal to the number of translations, and when its value is lower than a minimum threshold, all translations will be grouped into a single cluster. In such cases, if we use the batch method for translations diversification (Section 2.3.1) the diversity of translations is ignored. As a result, the best value of parameter $\beta$ should be initialized between a minimum and maximum threshold. To estimate the maximum threshold, we average the maximums of pairwise similarities between translations for all queries. Similarly, to estimate the minimum threshold, we $\mathbf { \Sigma } _ { \infty } ^ { \bullet \mathbf { \Gamma } } \mathbf { ^ { \bullet \mathbf { \Gamma } } }$ the minimums of pairwise similarities between translations for all queries. Table 2 shows maximum and minimum thresholds for $\beta$ in “JAVA” and “PHP” domains. Then, we fine-tune $\beta$ in range of minimum to the maximum threshold for all 100 tags in “JAVA” and select the best value of $\beta$ based on average coverage, average confidence and average $\mathrm { F } _ { \mathrm { s } \mathrm { c } \mathrm { \circ } \mathrm { r e } }$ in order of priority from first to last. Similarly, the optimal value for $\beta$ in $\mathrm { \displaystyle { \tilde { \rho } H P ^ { \prime } } }$ is calculat $\ J \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf \Sigma \mathbf { } \Sigma \Sigma \mathbf { } \Sigma \mathbf { \Sigma } \mathbf \Sigma \Sigma \Sigma \mathbf { } \Sigma \Sigma \mathbf { } \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \mathbf { } \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma $ The optimal value of $\beta$ for tags in “JAVA” and “PHP” domains are 0.01 and 0.04 , $\mathrm { r e s } _ { \mathrm { \mathbf { r } } }$ pectively.

Table 2: Maximum and minimum thresholds for $\beta$ in “JAVA” and “PHP” domains.

<table><tr><td>Domain</td><td>Minimum threshold</td><td>Maximum threshold</td></tr><tr><td>PHP</td><td>0.0006</td><td>0.06</td></tr><tr><td>JAVA</td><td>0.0003</td><td>0.05</td></tr></table>

In the second proposed method for translation clustering (i.e. CTS method described in Section 2.2.2), the well-known k -Means clustering algorithm is utilized to cluster relevant translations $T _ { q } ^ { \mathrm { r e l } }$ in the embedding space. As is known in the literature, finding the optimal number of clusters for the k -Means algorithm has remained as an open issue in machine learning research [30]. A common test to determine the appropriate number of clusters is to plot the ratio of the between-group variance to the total variance against the various number of clusters and determine the place of “elbow” where the slope of the curve is leveling off to the right of the plot. To the right of this point, there is not an impressive reduction in variance when the number of clusters increases.

In this work, we use the elbow test to determine the optimal number of clusters for relevant translations $T _ { q } ^ { \mathrm { r e l } }$ in the embedding space and set the optimal number of clusters to the value of k that is corresponding to 90% percentage of variance.

Each neural network used for ranking candidates (Section 2.4) is configured with 10 neurons in the hidden layer with the RELU activation function. The activation function of the output layer is selected to be a sigmoid function in which the output is in a range of 0 to 1. The weights of each network are learned using the stochastic batch gradient descent method with a batch size of 50 and the learning rate of 0.01. We use Tensorflow<sup>4</sup> to create and train these networks.

## 3.5. Experimental results

To evaluate the effectiveness of proposed method, three experiments are conducted. The effect of diversification on the quality of translations is studied in the first experiment. In the second one, the effectiveness of the proposed method in expert finding is compared with baseline methods introduced in Section 3.2. Because we have proposed two clustering methods for translations (i.e CMI and CTS) and two methods for translation diversification (i.e. batch and sequential), the notation  is used to show a combination of clustering method and diversification method . In the last experiment, we investigate the effectiveness of the proposed blending method details.

## 3.5.1. Experiment 1: The effect of diversification on the quality of translations

In this experiment, we study the effect of diversification on the quality of translations. First, we show several examples of translations diversified by the proposed method in Figure 1. In this figure, the word cloud visualization technique is used to expeditiously identify the relevancy and diversification of translations to the query word. We asked an expert to realize that each translation is placed in which query topics. In Figure 1 the words on the same topic, are displayed with the same color. As a result, the existence of more colors in each word cloud demonstrates covering more query topics. Moreover, the selection order of translations is visualized by font size such that the earlier translations have a larger font size. To better illustrate the selection order of translations, the rating of each translation is also included. As demonstrated in this figure, the diversification of colors in each word cloud shows that the suggested method has been able to include a high degree of diversification.

Figure 1: Sample query translations using CMI+Sequential method in “JAVA” domain.

To compare the proposed and baseline methods in terms of translation quality, for each baseline and proposed method we report the average Coverage, average Confidence and average $\mathrm { F _ { s c o r e } }$ for 100 tags in “JAVA” and 100 tags in “PHP”. The results are summarized in Table 3. As shown in this table, the proposed method outperforms the $\mathrm { t } \ a s _ { \setminus } \cdot 1 \mathrm { i } r _ { \cdot } \ a$ methods on translation quality. A noteworthy point in Table 3 is that the quality of translations increases when the sequential method is used for translation diversification.

Table 3: Comparison of the proposed method over the baseline methods in terms of ability to cover query topics.

<table><tr><td>Tag</td><td>Method</td><td>Average Coverage</td><td>Average Confidence</td><td>Average  $F_{score}$ </td></tr><tr><td rowspan="5">PHP</td><td>MI [4]</td><td>73.2</td><td>49.8</td><td>48.1</td></tr><tr><td>WE [4]</td><td>74.4</td><td>53.6</td><td>52.8</td></tr><tr><td>CMI+Batch</td><td>76.2</td><td>54.2</td><td>52.6</td></tr><tr><td>CTS+Batch</td><td>76.7</td><td>60.2</td><td>56.2</td></tr><tr><td>CMI+Sequential ( $\lambda = 0.8$ )</td><td>77.0</td><td> $\underline{60.5}$ </td><td>56.6</td></tr><tr><td></td><td>CTS+Sequential ( $\lambda = 0.8$ )</td><td> $\underline{78.0}$ </td><td>59.3</td><td> $\underline{57.7}$ </td></tr><tr><td rowspan="4">JAVA</td><td>MI [4]</td><td>82.8</td><td>50.7</td><td>56.5</td></tr><tr><td>WE [4]</td><td>83.0</td><td>51.9</td><td>56.9</td></tr><tr><td>CMI+Batch</td><td>85.3</td><td>51.9</td><td>57.0</td></tr><tr><td>CTS+Batch</td><td>86.2</td><td>56.4</td><td>61.2</td></tr><tr><td rowspan="2"></td><td>CMI+Sequential ( $\lambda = 0.7$ )</td><td>87.2</td><td>57.6</td><td>63.1</td></tr><tr><td>CTS+Sequential ( $\lambda = 0.7$ )</td><td>87.7</td><td>57.8</td><td>63.6</td></tr><tr><td colspan="5"> $CMI \equiv Translations \underline{Clustering based on Mutual Information}$ </td></tr><tr><td colspan="5"> $CTS \equiv Translations \underline{Clustering in Topic Space}$ </td></tr><tr><td colspan="5"> $Batch \equiv Batch translations diversification$ </td></tr><tr><td colspan="5"> $Sequential \equiv Sequential translations diversification$ </td></tr></table>

An important parameter which can affect the quality of translations in sequential method for diversification (Section 2.3.2) is . Increasing will increase coverage and confidence until it exceeds a threshold by which both coverage and confidence are significantly diminished. That is because in such a situation the proposed sequential method will be more interested in choosing diverse translations without considering their relevancy. The effect of different values of on coverage and confidence are plotted in Figure 2 for tags in “PHP” domain.

Figure 2: The effect of different values of on coverage and confidence in “PHP” domain.

We also investigate the effect of the number of translations on the quality of experts ranking sensitivity of the best-proposed method (i.e. CTS+sequential) and all baselines on the different number of translations for both ”Java” and ”PHP” domains, respectively. Evidently, almost in all methods, by increasing the number of query translations, the quality of expert ranking will improve. It can be explained by considering that increasing the number of query translations makes more query topics coverage and improve the quality of expert ranking. In the proposed method, we try to select a diverse set of query translations to cover more query topics. So we expect that increasing the number of query translations makes more improvement in the proposed method than the baseline methods.

Figure 3: Analysis the effect of varying number of translations on MAP measure for all baselines and the best proposed method (i.e CTS+Sequential).

## 3.5.2. Experiment 2: The effectiveness of diversification in the expert finding

In this experiment, the effectiveness of the proposed method in expert finding is compared with the baseline methods. The results are summarized in Table 4. As this table shows our proposed methods have significantly improved ranking metrics over the baseline models. A remarkable point in this table is that in both “JAVA” and “PHP” domains, the proposed method outperforms the baseline methods. Another point is that the sequential method for expert finding is performing better than the batch and all other baseline methods in terms of MAP , P@1 , P@5 , and P@10 measures.

Table 4: Comparison of the proposed method with the baselines methods.

<table><tr><td>Tag</td><td>Method</td><td>MAP</td><td>AVG. P@1</td><td>AVG. P@5</td><td>AVG. P@10</td></tr><tr><td>PHP</td><td>LM 1 [6]</td><td>37.7</td><td>56.0</td><td>50.0</td><td>44.0</td></tr><tr><td></td><td>LM 2 [6]</td><td>36.2</td><td>54.0</td><td>48.2</td><td>42.5</td></tr><tr><td></td><td>TM [19]</td><td>40.1</td><td>53.0</td><td>55.0</td><td>49.1</td></tr><tr><td></td><td>MI [4]</td><td>45.8</td><td>59.0</td><td>61.2</td><td>56.1</td></tr><tr><td></td><td>WE [4]</td><td>50.2</td><td>60.0</td><td>62.6</td><td>58.1</td></tr><tr><td></td><td>CTM [3]</td><td>53.2</td><td>61.2</td><td>62.5</td><td>58.7</td></tr><tr><td></td><td>MI(VS) [2]</td><td>58.7</td><td>75.0</td><td>72.6</td><td>64.2</td></tr><tr><td></td><td>WE(VS) [2]</td><td>56.2</td><td>75.0</td><td>69.6</td><td>62.1</td></tr><tr><td></td><td>CMI+Batch</td><td>67.6</td><td>72.0</td><td>69.4</td><td>58.1</td></tr><tr><td></td><td>CTS+Batch</td><td>67.7</td><td>72.0</td><td>69.8</td><td>59.6</td></tr><tr><td></td><td>CMI+Sequential (λ=0.8)</td><td>68.1</td><td>72.0</td><td>69.8</td><td>61.3</td></tr><tr><td></td><td>CTS+Sequential(λ=0.8)</td><td>70.0</td><td>76.0</td><td>71.6</td><td>62.6</td></tr><tr><td>JAVA</td><td>LM 1 [6]</td><td>37.7</td><td>56.0</td><td>50.0</td><td>44.0</td></tr><tr><td></td><td>LM 2 [6]</td><td>36.2</td><td>54.0</td><td>48.2</td><td>42.5</td></tr><tr><td></td><td>TM [19]</td><td>43.4</td><td>55.0</td><td>53.0</td><td>48.8</td></tr><tr><td></td><td>MI [4]</td><td>47.8</td><td>66.0</td><td>60.4</td><td>52.9</td></tr><tr><td></td><td>WE [4]</td><td>49.6</td><td>65.0</td><td>62.6</td><td>54.0</td></tr><tr><td></td><td>CTM [3]</td><td>52.2</td><td>69.2</td><td>61.5</td><td>55.8</td></tr><tr><td></td><td>MI(VS) [2]</td><td>64.7</td><td>85.0</td><td>73.6</td><td>65.2</td></tr><tr><td></td><td>WE(VS) [2]</td><td>66.0</td><td>86.0</td><td>72.8</td><td>66.1</td></tr><tr><td></td><td>CMI+Batch</td><td>75.8</td><td>82</td><td>75.3</td><td>64.8</td></tr><tr><td></td><td>CTS+Batch</td><td>75.9</td><td>83</td><td>77.9</td><td>67.0</td></tr><tr><td></td><td>CMI+Sequential $\left( {\lambda = {0.7}}\right)$ </td><td>77.2</td><td>83.0</td><td>77.7</td><td>67.0</td></tr><tr><td></td><td>CTS+Sequential $\left( {\lambda = {0.7}}\right)$ </td><td>78.1</td><td>86.0</td><td>78.3</td><td>67.5</td></tr><tr><td colspan="6"> $\mathbf{{CMI}} \equiv \underline{\text{Clustering based on Mutual Information}}$ </td></tr><tr><td colspan="6"> $\mathbf{{CTS}} \equiv \underline{\text{Clustering in Topic Space}}$ </td></tr><tr><td colspan="6"> $\mathbf{{Batch}} \equiv \underline{\mathbf{{Batch}}}$  translations diversification</td></tr><tr><td colspan="6"> $\underline{\text{Sequential}} \equiv \underline{\text{Sequential}}$  translations diversification</td></tr></table>

Table 5 reports improvement of the best-proposed method (i.e. CTS+Sequential) over the baselines. As illustrated in this tabl proposed CTS+Sequential method has a significant improvement over the baseline metho

Table 5: Improvement of the best proposed method (i.e. CTS+Sequential) over the baselines.

<table><tr><td>Tag</td><td>Methods</td><td>MAP</td><td>P@1</td><td>P@5</td><td>P@10</td></tr><tr><td>PHP</td><td>CTS+Sequential vs TM</td><td>74.5%</td><td>43.3%</td><td>30.1%</td><td>27.4%</td></tr><tr><td></td><td>CTS+Sequential vs MI</td><td>52.8%</td><td>28.8%</td><td>16.9%</td><td>11.5%</td></tr><tr><td></td><td>CTS+Sequential vs WE</td><td>37.5%</td><td>26.6%</td><td>14.3%</td><td>7.7%</td></tr><tr><td>JAVA</td><td>CTS+Sequential vs TM</td><td>79.9%</td><td>56.3%</td><td>47.7%</td><td>38.3%</td></tr><tr><td></td><td>CTS+Sequentialvs MI</td><td>63.3%</td><td>30.3%</td><td>29.6%</td><td>27.5%</td></tr><tr><td></td><td>CTS+Sequential vs WE</td><td>57.4%</td><td>32.3%</td><td>14.3%</td><td>15.9%</td></tr></table>

## 3.5.3. Experiment 3: Investigating the effectiveness of the ranking method

In this experiment, we investigate the effectiveness of the proposed method for experts ranking (Section 2.4) over a various set of translations. Due to using a different method for expert ranking, we evaluate the effectiveness of baseline methods by replacing the proposed ranking method with their built-in ranking method to have a fair comparison of results (see Table 6).

Table 6: Performance of baselines utilizing our proposed ranking method.

<table><tr><td>Tag</td><td>Translation method</td><td>Ranking method</td><td>MAF</td><td>P@1</td><td>P@5</td><td>P@10</td></tr><tr><td>PHP</td><td>MI [4]</td><td>Proposed</td><td>59.1</td><td>69.0</td><td>63.9</td><td>53.3</td></tr><tr><td></td><td></td><td>Built-in[4]</td><td>45.8</td><td>59.0</td><td>61.2</td><td>56.1</td></tr><tr><td></td><td>WE [4]</td><td>Proposed</td><td>63.0</td><td>75.0</td><td>67.3</td><td>58.1</td></tr><tr><td></td><td></td><td>Built-in[4]</td><td>50.9</td><td>60.0</td><td>62.6</td><td>58.1</td></tr><tr><td>JAVA</td><td>MI [4]</td><td>Proposed</td><td>70.3</td><td>76.0</td><td>70.6</td><td>61.4</td></tr><tr><td></td><td></td><td>Built-in[4]</td><td>47.8</td><td>66.0</td><td>60.4</td><td>52.9</td></tr><tr><td></td><td>WE [4]</td><td>Proposed</td><td>72.0</td><td>79.0</td><td>73.0</td><td>64.6</td></tr><tr><td></td><td></td><td>Built-in[4]</td><td>49.6</td><td>65.0</td><td>62.6</td><td>54.0</td></tr></table>

In order to show the relationship between Coverage and MAP , we have plotted these measures in Figures 4-(a) and 4-(b) for all tags in “PHP” and “JAVA” domain, respectively. The MAP of all baseline methods in these figures are calculated using the proposed ranking method instead of the built-in method in order to make a fair comparison. As these figures show, the more topics are covered by a set of translations, the more precise the expert finding method will be. This fact justifies the idea behind the proposed method in the diversification of translations in order to improve the results.

Figure 4: The relationship between topics covered by a set of translations and the MAP measure in:

a) “PHP”, and b) “JAVA” domain.

The paper also makes mention of common transformations such as damping the effects of raw counts using sub-linear functions, therefore it is possible to determine the degree to which suboptimal feature shaping might be contributing to the need for feature selection. By this, it is easy to learn much that is generalizable from the results that are presented. To this end, we demonstrate the effectiveness of the best-proposed method (i.e. CTS+Sequential) when the square root, cube root, and logarithm of feature vectors are used for damping effect analysis in the proposed ranking method. The results are given in Table 7.

Table 7: Performance analysis of the best proposed method (i.e. CTS+Sequential) encountering damping effects of raw counts using sub-linear functions.

<table><tr><td>Tag</td><td>Sub-linear function</td><td>MAP</td><td>P@1</td><td>P@5</td><td>P@10</td></tr><tr><td>PHP</td><td> $\log_2(\bullet)$ </td><td>67.9</td><td>73.0</td><td>70.1</td><td>61.3</td></tr><tr><td></td><td> $^2\sqrt{\bullet}$ </td><td>68.2</td><td>73.0</td><td>70.9</td><td>62.2</td></tr><tr><td></td><td> $^3\sqrt{\bullet}$ </td><td>67.4</td><td>73.0</td><td>69.8</td><td>61.8</td></tr><tr><td>JAVA</td><td> $\log_2(\bullet)$ </td><td>76.7</td><td>83.0</td><td>78.9</td><td>69.1</td></tr><tr><td></td><td> $^2\sqrt{\bullet}$ </td><td>77.8</td><td>83.0</td><td>79.7</td><td>68.0</td></tr><tr><td></td><td> $^3\sqrt{\bullet}$ </td><td>76.3</td><td>84.0</td><td>79.1</td><td>68.2</td></tr></table>

## 4. Discussion

As we described in Section 2, there are four different combinations of the proposed method that consider both relevancy and diversity in translating a given query. Both CMI and CTS find boundaries between the relevant translations. A clustering approach was used by CMI to find the boundaries but the clustering of translations embedded in the new topic space was used by CTS for the boundaries detection. Experiments show tah CTS is more smart than CMI because it considers the relevancy to query during boundaries detection. In other words, CTS considers how much translation are similar to each other and to the query word, but CMI only considers the relevancy of translations to each other. After clustering the relevant translations, we use two batch and sequential method to select representative for each cluster. In the batch method, we choose the most relevant translations from each cluster and the share of each cluster in selecting representatives are specified based on its relevancy to the query. In the sequential method, we first select the most relevant translation from each cluster and calculate a score for each one based on its relevancy to the query and how it covers the main query topics. Experiments show that the second one is more intelligent but it is a little time consuming than the batch one. Therefore, we expect to get better result in the presence of CTS and sequential approach.

In the following, we do an analysis on the computational complexity of the proposed method. Let $T ( n , m )$ , be the computational complexity of the proposed method, where n and m stands for the total number of vocabularies and documents in the collection, respectively. As mentioned in the section 2, we extract top- k relevant translations, where $k \leq n$ , by using MI criteria in the first step of the proposed method. The time complexity of this step is bounded to the total number of vocabulary (i.e. $O ( n m + n \log ( n ) )$ ). In the next step of the proposed method, we cluster top- k extracted translations. We have introduced two CMI and CTS clustering approaches for this step. The time complexity of CMI is bounded to number of selected relevant translations and number of documents (i.e. $O ( k m + k ^ { 2 } ) ,$ ). In CTS approach we have utilized K-means clustering algorithm, therefore the time complexity $O ( k ^ { 2 } )$ . Eventually, in the last step of our proposed translation model we intend to select a set of diverse translations that cover query topics as much as possible. $\mathrm { T o } \ \mathrm { c } \cdot \mathrm { s o }$ we have introduced two Batch and Sequential approaches. The time complexity of Batch and Sequential approaches are $O ( k \log ( k ) )$ and $O ( k \log ( k ) + k )$ respectively. Therefore, if we consider $k = n$ , the time complexity of the best proposed approach $( { \mathrm { i . e . ~ C T S + S e q u e n t i a l } } ) \cdots { \mathrm { . 1 } }$ be $O ( n m + n \log ( n ) + n ^ { 2 } + n \log ( n ) + n ) \sim O ( n m + n ^ { 2 } )$ . As it is obvious from Table 4, the best baseline methods in PHP and JAVA domains are MI(VS) and WE(MS), respectively. The time complexity of MI(VS) is $O ( n m + n \log ( n ) )$ which is relatively close to the best combination of the proposed method. The best baseline method in JAVA domain is a MLP neural network based approach which as the results shows is not reliable in all domains and has a big problem that is if a user poses a new query which is not in the predefined set of translations, it can not translate that. Therefore, although the proposed method is slightly more time-consuming, it performs much better in terms of the quality of results and has relieved the shortcomings of baseline methods to some extent.

## 5. Conclusion

Expert finding in CQA websites has attracted the attention of many researchers. VG is a basic problem in CQA websites making expert finding a challenging task. In this work, translation models are used in a way that takes both relevancy and diversity into account during translating queries. The mutual information measure has been used to ensure that translations are relevant to the user’s query and the idea of clustering has been used to consider diversification of query translations. For a better ranking of candidates, a regression model was used to learn how expert experiments indicate that diversifying query translations can be beneficial in the quality of translations and consequently ranking of candidates.

## References

[1] M. Dehghan, H. A. Rahmani, A. A. Abin, V.-V. Vu, Mining shape of expertise: A novel approach based on convolutional neural network, Information Processing & Management 57 (4) (2020) 102239.

[2] A. D. Nobari, M. Neshati, S. S. Gharebagh, Quality-aware skill translation models for expert finding on stackoverflow, Information Systems 87 (2020) 101413.

[3] M. Dehghan, A. A. Abin, Translations diversification for expert finding: A novel clustering-based approach, ACM Trans. Knowl. Discov. Data 13 (3) (2019) 32:1–32:20.

[4] A. Dargahi Nobari, S. Sotudeh Gharebagh, M. Neshati, Skill translation models in expert finding, in: Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2017, pp. 1057–1060.

[5] P. Rostami, M. Neshati, T-shaped grouping: Expert finding models to agile software teams retrieval, Expert Systems with Applications 118 (2019) 231–245.

[6] K. Balog, L. Azzopardi, M. de Rijke, A language modeling framework for expert finding, Information Processing & Management 45 (1) (2009) 1–19.

[7] H. Li, J. Xu, et al., Semantic matching in search, Foundations and Trends® in Information Retrieval 7 (5) (2014) 343–469.

[8] K. Balog, Y. Fang, M. de Rijke, P. Serdyukov, L. Si, et al., Expertise retrieval, Foundations

and Trends® in Information Retrieval 6 (2–3) (2012) 127–256.

[9] S. Lin, W. Hong, D. Wang, T. Li, A survey on expert finding techniques, Journal of Intelligent Information Systems 49 (2) (2017) 255–279.

[10] Q. Wang, J. Ma, X. Liao, W. Du, A context-aware researcher recommendation system for university-industry collaboration on r&d projects, Decision Support Systems 103 (2017) 46–57.

[11] S. H. Hashemi, M. Neshati, H. Beigy, Expertise retrieval in bibliographic network: a topic dominance learning approach, in: Proceedings of the 22nd ACM international conference on Conference on information & knowledge management, ACM, 2013, pp. 1117–1126.

[12] C. Moreira, P. Calado, B. Martins, Learning to rank academic experts in the dblp dataset, Expert Systems 32 (4) (2015) 477–493.

[13] C. Moreira, A. Wichert, Finding academic on a multisensor approach using shannons entropy, Expert Systems with Applications 40 (14) (2013) 5740–5754.

[14] S. S. Gharebagh, P. Rostami, M. Neshati, T-shaped mining: A novel approach to talent finding for agile software teams, in: Springer, 2018, pp. 411–423.

[15] M. Neshati, D. Hiemstra, E. Asgari, H. Beigy, Integration of scientific and social networks, World wide web 17 (5) (2014) 1051–1079.

[16] Y. Xu, D. Zhou, J. Ma, Scholar-friend recommendation in online academic communities: An approach based on heterogeneous network, Decision Support Systems 119 (2019) 1–13.

[17] M. Neshati, Z. Fallahnejad, H. Beigy, On dynamicity of expert finding in community question answering, Information Processing & Management 53 (5) (2017) 1026–1042.

[18] M. Dehghan, M. Biabani, A. A. Abin, Temporal expert profiling: With an application to t-shaped expert finding, Information Processing & Management 56 (3) (2019) 1067–1079.

[19] S. Momtazi, F. Naumann, Topic modeling for expert finding using latent dirichlet allocation, Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery 3 (5) (2013) 346–353.

[20] M. Karimzadehgan, C. Zhai, Estimation of statistical translation models based on mutual information for ad hoc information retrieval, in: Proceedings of the 33rd international ACM SIGIR conference on Research and development in information retrieval, ACM,

2010, pp. 323–330.

[21] C. Van Gysel, M. de Rijke, M. Worring, Unsupervised, efficient and semantic expertise retrieval, in: Proceedings of the 25th International Conference on World Wide Web, International World Wide Web Conferences Steering Committee, 2016, pp. 1069–1079.

[22] X. Li, C. Li, J. Chi, J. Ouyang, Short text topic modeling by exploring original documents, Knowledge and Information Systems 56 (2) (2018) 443–462.

[23] C. Li, W. K. Cheung, Y. Ye, X. Zhang, D. Chu, X. Li, The author-topic-community model for author interest profiling and community discovery, Knowledge and Information Systems 44 (2) (2015) 359–383.

[24] Y.-K. Tang, X.-L. Mao, H. Huang, Labeled phrase latent dirichlet allocation and its online learning algorithm, Data Mining and Knowledge Discovery 32 (4) (2018) 885–912.

[25] D. M. Blei, A. Y. Ng, M. I. Jordan, Latent dirichlet allocation, Journal of machine Learning research 3 (Jan) (2003) 993–1022.

[26] M. Neshati, E. Asgari, D. Hiemstra, H. Beigy, A joint classification method to integrate scientific and social networks, Springer, 2013, pp. 122–133.

[27] M. Neshati, H. Beigy, D. Hiemstra, Expert group formation using facility location analysis,

[28] F. M. Belém, C. S. Batista, R. L. Santos, J. M. Almeida, M. A. Gonçalves, Beyond relevance novelty and diversity in tag recommendation, ACM stems and Technology (TIST) 7 (3) (2016) 26.

[29] M. Karimzadehgan, C. Zhai, G. Belford, Multi-aspect expertise matching for review assignment, in: Proceedings of the 17th ACM conference on Information and knowledge management, ACM, 2008, pp. 1113–1122.

[30] A. A. Abin, A random walk approach to query informative constraints for clustering, IEEE Transactions on Cybernetics (2018) 1–12.

## Credit Author Statement:

Mahdi Dehghan: Data Curation, Software, Writing - Original Draft

Ahmad Ali Abin: Conceptualization, Methodology, Supervision, Writing - Review & Editing

Mahmood Neshati: Conceptualization, Validation, Review

 Translations diversification was investigated on the quality of expert finding

 Both diversity and relevancy of translations were considered for expert finding

 A regression model was used for expert ranking

## Biographical Note

Mahdi Dehghan received the B.Sc. in computer engineering from the University of Golestan, Golestan, Iran, in 2016. He received the M.Sc. degrees in computer engineering from the Shahid Beheshti University, Tehran, Iran, in 2019. His primary research interest is in the area of information retrieval and machine learning.

Ahmad Ali Abin received the B.Sc. in computer engineering from the Iran University of Science and Technology, Tehran, Iran, in 2005. He received the M.Sc. and Ph.D. degrees in computer engineering from the Sharif University of Technology, Tehran, Iran, in 2008 and 2014, respectively. Since 2014, he joined with the Department of Computer Science and Engineering, Shahid Beheshti University, Tehran, Iran. His research interests include pattern recognition, machine learning and neural computing.

Mahmood Neshati received the B.S. (2005), M.S. (2007) and PhD (2014) degrees in computer engineering from the Sharif University of Technology, Tehran, Iran. He is currently an assistant professor at Shahid Beheshti University, Tehran, Iran. Prior to that, he was a research assistant at Qatar Computing Research Institute (QCRI-2015). He has published several research papers in Information Retrieval journals and conferences (SIGIR, CIKM and ECIR). His main research interests also include big data analytic, large scale distributed system design and information management.

<table><tr><td>(a) Jdbc</td><td>(b) Hibenate</td><td>(c) Database</td><td>(d) JPA</td></tr></table>

![](/api/attachments/UNRYX7WW/fulltext/images/8a106fec0f76e35a1e61c4ca08d134050a4cafe1592ddb3b65d9556aafd4c73d.jpg)  
(a) Coverage

![](/api/attachments/UNRYX7WW/fulltext/images/9c15177dab12d70305858a756d165b249755ef83bf3c3d8c61c61fb2493a2bd6.jpg)  
(b) Confidence  
Figure 2

![](/api/attachments/UNRYX7WW/fulltext/images/655a4ce3ae17ceaeb3050ad67c28768123c6df3dd922c23377b6eb451a6ff934.jpg)  
(a) Java

![](/api/attachments/UNRYX7WW/fulltext/images/9d3824fa541727e43b0b850bff7b1d8f912eaac384577d7da4df5aa459358270.jpg)  
(b) PHP  
Figure 3

![](/api/attachments/UNRYX7WW/fulltext/images/4ff5c81e5b947e0d8b3a7f37be59921c863ea29f7db8f1c5728c1ba6710ea5f9.jpg)  
(a) “PHP"

![](/api/attachments/UNRYX7WW/fulltext/images/b7f8f6d9928e7e52b1ce4f9aeb95ead9e98ddf73d01e39d65c6186410c61efba.jpg)  
(b) ${ } ^ { 6 6 } \mathrm { J } \mathrm { A V } \mathrm { A } ^ { \prime \prime }$  
Figure 4
