---
otero_id: 3036
otero_key: "44S289D9"
title: "Genetic-based approaches in ranking function discovery and optimization in information retrieval — A framework"
authors: "Weiguo Fan; Praveen Pathak; Mi Zhou"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.04.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Genetic-based approaches in ranking function discovery and optimization in information retrieval — A framework

Weiguo Fan <sup>a</sup>, Praveen Pathak <sup>b,</sup>⁎, Mi Zhou <sup>c</sup>

<sup>a</sup> 3007 Pamplin Hall, Virginia Tech Blacksburg, VA 24061, USA

<sup>b</sup> 339 STZ, Warrington College of Business Administration, University of Florida, Gainesville, FL 32611, USA

<sup>c</sup> School of Management, Xi'an Jiaotong University, Xi'an, Shaanxi, 710049, PR China

## a r t i c l e i n f o

Article history: Received 21 August 2007 Received in revised form 9 March 2009 Accepted 2 April 2009 Available online 15 April 2009

Keywords: Information retrieval Arti<sup>fi</sup>cial intelligence Evolutionary computations Data fusion Genetic algorithms

## a b s t r a c t

An Information Retrieval (IR) system consists of document collection, queries issued by users, and the matching/ranking functions used to rank documents in the predicted order of relevance for a given query. A variety of ranking functions have been used in the literature. But studies show that these functions do not perform consistently well across different contexts. In this paper we propose a two-stage integrated framework for discovering and optimizing ranking functions used in IR. The <sup>fi</sup>rst stage, discovery process, is accomplished by intelligently leveraging the structural and statistical information available in HTML documents by using Genetic Programming techniques to yield novel ranking functions. In the second stage, the optimization process, document retrieval scores of various well-known ranking functions are combined using Genetic Algorithms. The overall discovery and optimization framework is tested on the well-known TREC collection of web documents for both the ad-hoc retrieval task and the routing task. Utilizing our framework we observe a signi<sup>fi</sup>cant increase in retrieval performance compared to some of the well-known stand alone ranking functions.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

As the cost of storage devices continues to decrease, there is a huge growth in databases of all sorts (relational, graphical, and textual). The tremendous growth of the World Wide Web has also contributed to the explosive growth of documents available. This has led to huge, fragmented, and unstructured document collections within organizations. Although it has become easier to collect and store information in document collections, it has become increasingly dif<sup>fi</sup>cult to retrieve relevant information from these large document collections. This is true both in the context of World Wide Web (WWW) as well as in ecommerce. In WWW when users search the Web using popular search engines such as Google and Yahoo, they often are faced with either having to look at many webpages before <sup>fi</sup>nding a relevant one or they cannot <sup>fi</sup>nd all the relevant information they are looking for. In the context of e-commerce users may <sup>fi</sup>nd it dif<sup>fi</sup>cult to locate products they are trying to shop for. Retrieval performance is paramount for the users of the Web and e-commerce. Various techniques have been used by researchers to address the issue of improving retrieval performance [8,19,23,40].

An Information Retrieval (IR) system typically consists of three subsystems: Documents, Users with Queries, and Matching/Ranking

Functions<sup>1</sup>. There are users with varying information requirements, both in terms of breadth and depth of topics they are interested in. A document collection consists of documents about many different topics. Documents are represented in a form (typically using vector space model [39]) that can be easily used by the matching function, taking care that this representation correctly represents author's intention. User's information requirements are translated into queries that the system can process. Query formatting depends on the underlying model of retrieval used (Boolean models [6], vector space models [39], probabilistic models [37], fuzzy retrieval models [7], models based on arti<sup>fi</sup>cial intelligence techniques [10]).

A system matching function matches the information in queries with that in the document representations and typically calculates a score called ‘retrieval status value’ (RSV). The documents are presented to the user in decreasing order of RSV. The user rates these documents as either relevant or non-relevant to his/her information need. Various system performance criteria like precision and recall have been used to gauge the effectiveness of the system in meeting users' information requirements. Recall is the ratio of the number of relevant retrieved documents to the total number of relevant documents available in the document collection. Precision is de<sup>fi</sup>ned as the ratio of the number of relevant retrieved documents to the total number of retrieved documents. Relevance feedback is typically used by the system to improve document descriptions, or queries with the expectation that the overall performance of the system will improve after such a feedback.

An IR system's performance can be affected by factors affecting any of the three subsystems: documents, queries, or ranking functions. Researchers have extensively looked at how to improve retrieval performance by manipulating the documents and the queries [3,19,22,27,32,40]. In this paper we focus our attention on discovering and optimizing the ranking functions. Ranking functions, in the web scenario, typically exploit three characteristics of the documents: the content of the document, the links to the documents, and the structure of the document. The content based ranking functions [38,42] make extensive usage of many lexical/syntactical statistics (e.g. token frequency (tf), document frequency (df), document length, etc.) of words in a document collection for ranking purposes. Linkbased ranking functions [8,30] utilize web interconnection information to help boost the ranking performance by identifying pages that are highly endorsed by others. Structure based ranking functions exploit the structural properties in documents by assigning weights to words appearing in different structural position, such as Title, Header, Anchor, and use those weighting heuristics to improve ranking performance. Although for proprietary reasons, the exact algorithm used by commercial search engines is not known, it is conjectured that these search engines typically use structural information in their ranking functions [1].

There are some other ranking functions that seek to combine the evidence at the content, link, and structure levels as evidenced in recent TREC<sup>2</sup> web track competition [24,25]. In the TREC competition it was clear that using link information alone does not provide much help in performance improvement (in terms of performance measures such as precision and recall) as compared to using content information alone. Also, the ranking functions based on content alone are still very successful. For example, Okapi [42], a ranking function based on content alone was found very successful. We conducted a preliminary test using Okapi function by adding keywords from document title, in addition to the body text of the document. It was found that adding structural information (like the information from the document title) improved retrieval performance even by the same ranking function Okapi.

Ranking function tuning is very important for IR system performance improvement (in terms of precision and recall). There is some prior research in using Genetic Programming (GP) for ranking function discovery [14] and using Genetic Algorithms (GA) for ranking fusion [5,34–36]. But, to the best of our knowledge, there is no research combining these two into a systematic, integrated framework. GP is known to be very powerful for novel nonlinear function discovery, and GA is known to be suitable for parameterized nonlinear optimization. However, it remains to be explored whether the novel ranking functions discovered by GP can be effectively fused later with other well-known ranking functions by GA to further improve the ranking function performance. We believe that these two streams of ranking function improvement research can be integrated yielding improved retrieval performance. In this paper, we propose such an integrated two-stage framework for improving retrieval performance. In the <sup>fi</sup>rst stage, called discovery or exploration stage, we would exploit the structural information in documents along with the content information in them to discover new ranking functions. We would use GP for such a discovery. In the second stage, called optimization or exploitation stage, we would combine the information provided by well-known ranking functions (including the ones discovered by GP) using an optimization technique like GA to further improve retrieval performance.

The paper is organized as follows. In Section 2 we will discuss related work in the area of ranking function discovery and adaptation. In Section 3 we will present our framework for ranking function discovery and optimization. The framework will be tested on a wellknown web document collection by conducting experiments detailed in Section 4. In Section 5 we will discuss the results of the experiments, and Section 6 will conclude the paper.

## 2. Related work

In this section we will brie<sup>fl</sup>y review research related to our work in this paper. Speci<sup>fi</sup>cally we will <sup>fi</sup>rst review the vector space model (VSM), which is the theoretical model upon which our integrated framework of ranking function discovery and optimization is based. Then we will review the work in data fusion technique as applied to information retrieval (IR), and <sup>fi</sup>nally we will review work in IR that uses GP and GA.

## 2.1. Vector space model (VSM)

This is a theoretically well grounded model in IR. It is based on vector space and hence is easily interpreted from a geometric perspective [39]. Each document and query is placed in an n dimensional space where its properties can be studied using geometrical similarity. This model has been one of the most successful models in various performance evaluation studies [39,40] and most existing search engines and information retrieval systems are designed based on it.

In VSM, both documents and queries are represented as vectors of terms. Suppose there are t terms in the collection, then a document D and a query Q are represented as:

$$
\begin{array}{l} D = (w _ {d 1}, w _ {d 2}, \ldots , w _ {d t}) \\ Q = (w _ {q 1}, w _ {q 2}, \ldots , w _ {q t}) \end{array}
$$

where $w _ { d i } , w _ { q i }$ (for i = 1 to t) are weights assigned to different terms in the document and query respectively. The similarity between the two vectors is calculated as the cosine of the angle between the two vectors. It is expressed as [39]:

$$
\text { Similarity } (Q, D) = \frac {\sum_ {i = 1} ^ {t} w _ {q i} w _ {d i}}{\sqrt {\sum_ {i = 1} ^ {t} \left(w _ {q i}\right) ^ {2} * \sum_ {i = 1} ^ {t} \left(w _ {d i}\right) ^ {2}}}.\tag{1}
$$

This score, also called retrieval status value (RSV), is calculated for each document in the collection and the documents are ordered and presented to the user in the decreasing order of RSV. Various content based features are available in VSM to compute the term weights. The most common ones are the term frequency (tf) and the inverse document frequency (idf). Term frequency measures the number of times a term appears in the document or the query. The higher this number, the more important the term is assumed to be in describing the document. Inverse document frequency is calculated as log(N/DF), where N is the total number of documents in the collection, and DF is the number of documents in which the term appears. A high value of idf means the term appears in relatively few number of documents and hence the term is assumed to be important in describing the document. A lot of similar content based features are available in literature [39,40]. The features can be combined (e.g. $t f ^ { * } i d f )$ to generate a variety of new composite features that can be used in term weighting.

Eq. (1)) suggests that in order to discover a good ranking function, we need to discover the optimal way of assigning weights to document and query keywords. Traditional VSM focuses on the functional space of the combination of a set of weighting features, such as tf, df, idf etc. It does not typically take into account the structural information within documents. If we qualify these weighting features to include the structural/positional information such as Anchor, Title, Abstract, and Body, we can get an expanded set of features such as tf<sub>anchor</sub>, tf<sub>title</sub>, tf<sub>abstract</sub>, tf<sub>body</sub> etc. In the <sup>fi</sup>rst stage of our framework, we seek to discover new ways of leveraging structural information in assigning weights to document and query terms. The theoretical foundation serving Eq. (1) can still be applied to the structural context.

## 2.2. Combining ranking functions

The second stage in our model involves combining results obtained from various well-known expert ranking functions. This is the so called data-fusion technique. It has been typically applied in IR in the context of combining similarities obtained from different query representations and also on combining query representations themselves [4]. It was found that progressive combination of different Boolean query formulations lead to improved retrieval performance. Bartell et al. [2] used combinations of three different experts on two test collections and found that an optimized combination performed better than any individual system. Savoy et al. [41] combined Okapi probabilistic model with various vector space schemes and used a heuristic to determine the best retrieval expert for a given query. But they did not <sup>fi</sup>nd any performance gains over individual experts. Fox et al. [18] used minimum, maximum, or the sum of the individual similarities to combine retrieval results from different experts and found CombMNZ [18] as the best performing formula. Lee [33] used ranks instead of similarity to extend the work of Fox et al. Bartell et al. [3] used numerical methods to optimize only the parameters involved in a standard inner product measure. Thus their adapted matching function is limited to variations of standard inner product measures. Vogt et al. [43] used linear combinations of three experts (a binary scheme for vector space model, a tf–idf weighted scheme, and one based on latent semantic indexing) to determine a set of parameters. Their method worked well on training set of documents, but did not generalize well to unseen test documents. In another paper, Vogt et al. [43] did a theoretical and empirical study on combining two IR systems and demonstrated conditions under which the linear combination model might work. However, this paper failed to provide any insights into how to combine more than 2 IR expert matching systems, and how to optimize the weights of combination directly on the standard performance measure like average precision.

## 2.3. Genetic-based approaches in IR

GA [26] and GP [31] are arti<sup>fi</sup>cial intelligence search algorithms based on evolutionary theory. They represent the solution to a problem as a chromosome (or an individual) in a population pool. They evolve the population of chromosomes in successive generations by following the genetic transformation operations such as reproduction, crossover, and mutation to discover chromosomes with better <sup>fi</sup>tness values. A <sup>fi</sup>tness function assigns the <sup>fi</sup>tness value for each chromosome and represents how good the chromosome is at solving the problem at hand.

Because of the intrinsic parallel search mechanism and powerful global exploration capability in a high-dimensional space, both GA and GP have been used to solve a wide range of hard optimization problems. GAs are typically used to solve dif<sup>fi</sup>cult parameterized nonlinear optimization problems, while GP is typically used to approximate or discover complex, nonlinear functional relationships [31]. There has been some interest in using these algorithms in the <sup>fi</sup>eld of information retrieval and speci<sup>fi</sup>cally in document indexing; query induction, representation, and optimization; and document clustering [10–12,14,21,22,27,32,34,35,44]. We now proceed to present our framework for ranking function discovery and optimization.

## 3. Ranking discovery and optimization framework

Evaluation studies [42,45] on use of ranking functions have shown that no single ranking function performs best for all contexts of document collections and queries. The best method to pick a good ranking function for a given query is still an open question. Moreover, there may still be some good ranking functions which are yet to be discovered. In this section we present a framework to address these issues. The <sup>fi</sup>rst part of the framework explores a variety of clues available in content and structural information about the documents and the queries to discover new ranking functions, while the second part intelligently combines the evidence obtained from these newly discovered ranking functions as well as from various well-known existing ranking functions to yield better retrieval performance. We apply GP for the <sup>fi</sup>rst discovery part while applying GA for the optimization part. The <sup>fi</sup>rst part, the discovery of new ranking function, aims at combining various document related features (both content and structural features). Although GA could be applied in this stage, given the <sup>fl</sup>exibility and ease of representation (in terms of tree structure as shown later) afforded by GP, we have used GP in the <sup>fi</sup>rst stage. Here we have followed Koza's argument [31] about use of GP instead of GA while discovering new functions. In the second stage we have used data-fusion techniques to combine the evidence obtained from various well-known ranking functions (including the ones discovered in the <sup>fi</sup>rst part). This combination is done by weighing the score obtained by each ranking function. GA's have been shown to be very useful for such fusion [17,31,36]. Hence we use GA in the second part. The framework is presented in Fig. 1.

![](/api/attachments/44S289D9/fulltext/images/20ea057f0de963b44d0a793f986d37097b4fc2bdf2eb3873a3302dbe91c46a50.jpg)  
Fig. 1. Framework for ranking function discovery and optimization.

Features used in the discovery process.

<table><tr><td>Features used</td><td>Statistical meaning</td></tr><tr><td>tf_XX</td><td>Number of times the term appeared in part XX of the document</td></tr><tr><td>tf_max_XX</td><td>Maximum tf in the part XX of the document</td></tr><tr><td>tf_avg_XX</td><td>Average tf in the part XX of the document</td></tr><tr><td>tf_max_XX_Col</td><td>Maximum tf_XX in the entire document collection</td></tr><tr><td>df_XX</td><td>Number of documents in the collection the term appeared in the part XX</td></tr><tr><td>df_max_XX</td><td>Maximum df_XX</td></tr><tr><td>N</td><td>Number of documents in the entire text collection</td></tr><tr><td>Length_XX</td><td>Length of a document part XX</td></tr><tr><td>Length_avg_XX_Col</td><td>Average length of part XX in the entire collection</td></tr><tr><td>n</td><td>Number of unique terms in the document</td></tr></table>

Note: XX here stands for different parts (either entire document, anchor, title, body, or abstract) of a HTML document.

We now describe each of the parts in the framework.

## 3.1. GP based discovery of ranking functions

The <sup>fi</sup>rst stage in the framework is the GP based discovery of ranking function. Training and validation set of documents as well as either ad-hoc queries or routing queries serve as input to this discovery process. Ad-hoc queries are used when we want to discover a ranking function which is applicable to any of the queries issued to the system, while routing queries are used when we are interested in discovering a query speci<sup>fi</sup>c ranking function for each individual query. We base this discovery framework on the work done by Fan et al. [14,16]. In that work only the content information from documents and queries is utilized. We enhance that work by including not just the content based information but also the structure based information in documents and queries. As mentioned earlier, in our preliminary work with Okapi ranking function, we found that by adding structure information to the retrieval process the retrieval performance can be enhanced signi<sup>fi</sup>cantly. Moreover the Fan et al. framework was targeted at only routing queries. We enhance that by discovering ranking functions not just for the routing queries but also for the ad-hoc queries as mentioned earlier. The content and structure based information that we include in our model is given in Table 1.

As per the table, there are a total of 42 different features that can be used in the model. We need to explore the multi-dimensional space which combines these features in such a way as to improve the retrieval performance. We will use the tree data structure as shown in Fig. 2 to combine these features. A tree based representation allows for ease of parsing and implementation. The discovery of an optimal tree representing the ranking function is essentially the exploratory and discovery stage of our model. We use GP for discovering such a tree. GP is chosen for several reasons. First, GP can be used to optimize any type of <sup>fi</sup>tness function. It does not require the <sup>fi</sup>tness function to be continuous or differentiable. Many <sup>fi</sup>tness/objective functions in IR are discrete in nature (we will talk of our <sup>fi</sup>tness function later, but it also falls under this category), and hence GP is suited for such a task. Second, GP has been shown to be very useful for nonlinear function discovery [31]. And <sup>fi</sup>nally, it has been empirically shown that solutions discovered by GP are typically better than those discovered by other heuristic algorithms and are nearly close to the global optimum [31].

![](/api/attachments/44S289D9/fulltext/images/a09434e30eccd9f0733d92db985c027c0e6a95a6e1f0fbacaa1a03b0a02c45e2.jpg)  
Fig. 2. A sample tree representation for a ranking function

In order to apply GP in our context we need to de<sup>fi</sup>ne several components for it. These are given in Table 2.

For the purpose of our discovery framework we will de<sup>fi</sup>ne these parameters as follows:

An individual in the population is expressed in terms of a tree which represents one possible ranking function. A population in a generation consists of P such trees.

Terminals: we use the features mentioned in Table 1 and realvalued numbers as the terminals.

Functions: we use $+ , - , * , / ,$ and log as the functions allowed.

Fitness function: we use the P\_Avg as the <sup>fi</sup>tness function which is de<sup>fi</sup>ned in Eq. (2)

$$
P _ {-} \text { Avg } = \frac {\sum_ {i = 1} ^ {| D |} \left(r (d _ {i}) ^ {*} \left(\frac {\sum_ {j = 1} ^ {i} r (d _ {j})}{i}\right)\right)}{\text { TRel }}\tag{2}
$$

where $r ( d _ { i } ) \in \{ 0 , 1 \}$ is the relevance score assigned to a document, it being 1 if the document is relevant and 0 otherwise. |D| is the total number of retrieved documents. TRel is the total number of relevant documents for the query.

P\_Avg is the standard performance measure used in retrieval studies because it takes into account not just how many relevant documents are retrieved but also the positions at which they are retrieved (the more relevant documents at the top the better the P\_Avg score). Thus, it combines both precision and recall in one single measure.

Reproduction: reproduction copies the top (in terms of <sup>fi</sup>tness) trees in the population into the next population. If P is the population size and reproduction rate is rate\_r then top rate $r ^ { \ast } P$ trees are copied into next generation.

Table 2 Essential GP components.

<table><tr><td>GP parameters</td><td>Meaning</td></tr><tr><td>Terminals</td><td>Leaf nodes in the tree data structure</td></tr><tr><td>Functions</td><td>Non-leaf nodes used to combine the leaf nodes. Typically numerical operations</td></tr><tr><td>Fitness function</td><td>The objective function that needs to be optimized</td></tr><tr><td>Reproduction and crossover</td><td>Genetic operators used to copy fit solutions from one generation to another and to introduce diversity in the population</td></tr></table>

![](/api/attachments/44S289D9/fulltext/images/0b733053d0155dd4e954c209a1d4d3fdd79a847c5a0685840c221dc90b4e3b7d.jpg)  
Fig. 3. GA optimization problem.

Selection: we use the tournament selection to select trees from the population.

Crossover: the top two among the six trees (in terms of <sup>fi</sup>tness) are selected for crossover and they exchange sub-trees to form trees for the next generation. Crossover point is randomly chosen. If the new trees formed after crossover are invalid mathematically then a new crossover point is chosen. The process is repeated till two valid trees for the next generation are formed.

The details of the ranking function discovery process will be outlined in the next section on experiments conducted.

## 3.2. GA based optimization

In the GP based discovery phase of the framework we combined various content and structure based features of HTML documents by using GP for discovery purpose. The output of the discovery stage is basically a set of newly discovered ranking functions. As we will see in the Results and discussion section, some of the discovered ranking functions yield much better retrieval results than the well-known existing ranking functions for both the ad-hoc and the routing tasks. It is apparent that different ranking functions give varying importance to different features in the documents and the queries and hence yield different retrieval performance. But the question arises, is it possible to combine the evidence from existing ranking functions as well as that from the new ones discovered by the GP process to further improve the retrieval performance. The second stage of our framework tries to answer that question.

As mentioned earlier in the Related work section, there have been some efforts at combining evidence from ranking functions. But they have some limitations. For example, Bartell et al. [3] had to restrict their optimized functions to variations of inner product measures. They have used numerical methods for optimization because they assumed that the relevant criteria for optimization are differentiable in nature. With important IR measures like P\_Avg that is not the case. Vogt et al. [43] could <sup>fi</sup>nd the performance of combined functions to be as good as only the second best individual function. They also did not combine more than 2 experts at a time. Our proposed optimization process does not face these limitations.

The optimization stage in our framework is based on the work done by Pathak et al. [36]. That work was very limited in scope. It did not use any structural information in documents. The optimization of ranking functions was done at the individual query level for the routing task. Moreover the queries used were user-provided. In this work we enhance upon their work by incorporating structural information in documents. We show how our framework can be used for both the ad-hoc retrieval and routing task. We also use not only the user-provided queries but also queries which have been adapted using feedback information.

In this stage of our framework (Fig. 1), some of the newly discovered ranking functions from the GP discovery stage, as well as other existing well-known ranking functions, will be used as input ranking functions for the optimization process. The optimization problem for the GA is as shown in Fig. 3. As shown in the <sup>fi</sup>gure let there be ‘n’ different ranking functions (including the ones discovered by the <sup>fi</sup>rst phase by GP). For a given query, each ranking function assigns a retrieval score to each document in the document collection. We weigh these retrieval scores with a weight ‘w’ (from w to w respectively) and linearly combine these weighted scores. The documents in the collection are ordered in the decreasing order of this weighted score and the top ‘DCV’<sup>3</sup> number of documents is retrieved for the user. The user judges these documents as either relevant or non-relevant for his/her information needs. Based on these judgments we calculate the retrieval performance of the system in terms of P\_Avg (given in Eq. (2)).

The optimization problem is to maximize the P\_Avg performance measure subject to proper assignment of the weights w to w . We utilize GA to do the assignment of these weights. GA's are chosen because of the large search space involved and the characteristics of the objective function. The weights are real-valued numbers assigned in the range of −1.0 to 1.0. The search space is basically in<sup>fi</sup>nite and the problem is a needle-in-a-haystack problem. Moreover the objective function that we use in Eq. (2) is discrete in nature. GA does not need the objective function to be continuous as long as it can differentiate good solutions from bad ones. For comparison purposes we will also use simulated annealing (SA) technique [29] to assign the weights involved and compare the results obtained with the ones obtained by GA.

At the end of the optimization stage, we have a set of ranking functions (including the ones that were discovered by the prior GP discovery stage) and associated weights. Any new retrieval will use these as the effective ranking function to retrieve documents. In the next section we outline the experiments we conducted to test the effectiveness of our framework on the retrieval performance.

## 4. Experiments

We test the effectiveness of our framework for retrieval by conducting various experiments. We now describe the data that was used, the exact process for GP discovery and GA optimization that was followed, the various ranking functions (apart from the newly discovered ones) that were used, and the <sup>fi</sup>tness functions that were used in the discovery and optimization process.

## 4.1. Data used for experiments

For both the discovery and the optimization process we use the web track document collection from the TREC 9 and TREC 10 conferences [24,25]. It has been used extensively in IR evaluation studies. Residual collection method [39] is used to segment the data into three datasets: for training (50%), for validation (20%), and for testing (30%). There are a total of 100 queries used in these datasets. We use only 88 queries out of these, since the remaining 12 do not have any relevant document in the validation and the test datasets. The performance results reported in the next section are based on the retrieval results obtained on the test dataset.

## 4.2. Queries used (user-provided queries and relevance feedback queries)

As stated earlier we use the 88 queries out of 100 queries available in TREC 9 and TREC 10. There has been a lot of research in IR in improving query descriptions through relevance feedback. We wanted to test the effect of such feedback on the performance of our framework. Hence we use two types of queries in the experiments. The <sup>fi</sup>rst type is the raw queries (called user-provided queries) available from TREC. For the second type, we replace the userprovided queries with feedback queries which are generated using the Robertson Selection Value formula [15,37]. This method uses relevant documents to identify the best terms for a user's search, even if the user doesn't include them in the query. We select the top 10 words for each query as we <sup>fi</sup>nd this size works the best in the training collection for three well-known ranking systems: Okapi, Pivoted TFIDF and INQUERY [19,42].

![](/api/attachments/44S289D9/fulltext/images/546f3f33cc21e41d67563842a461e73c8f72a70dc4cac0fac9faba15ff6be6d6.jpg)  
Fig. 4. GP discovery process.

![](/api/attachments/44S289D9/fulltext/images/fa6dff4fc7ece2ce4fe2e1cedbf18c03fac315cff918fe5eda9a5caa94e05eb3.jpg)  
Fig. 5. GA optimization process

## 4.3. Performance measures

We use two performance measures to report our results. The <sup>fi</sup>rst one is the P\_Avg measure which is given in Eq. (2). As mentioned earlier, it is the most widely used measure in IR. It not only takes into account how many relevant documents are found, but also how early in the retrieval order they are found. The second measure we will use is P\_10 measure. It de<sup>fi</sup>nes the precision obtained in the top 10 documents retrieved. This measure might be important for typical web search tasks where the user is willing to see only the top few documents and would like to get as many relevant documents as possible in the top 10 retrieved documents.

## 4.4. GP discovery process

The GP based discovery stage follows steps shown in Fig. 4. The training phase is conducted for 30 generations $( N _ { \mathrm { { g e n } } } { } ^ { 4 }$ parameter). The population size is 500. Tournament selection is used to select, with replacement, 6 random trees from the population. Reproduction rate rate\_r is set to 0.1. After each generation we record the top 10 $( N _ { \mathrm { t o p } }$ parameter) ranking trees along with their <sup>fi</sup>tness. Reproduction and crossover are as explained earlier. Mutations are helpful in GA process but not that helpful in GP process [31]. Hence we did not include mutation operator in the GP process.

In the validation phase the 300 candidate ranking trees are applied on the validation documents. We select the top two best performing trees (on validation dataset) for comparison with other well-known ranking functions. These also serve as input to the subsequent optimization phase.

## 4.5. Ranking functions used for optimization

We use 6 different ranking functions in the optimization process. The <sup>fi</sup>rst two (named GP1 and GP2) are the output of our discovery process. The other four are very well-known functions in IR literature and they have performed well on TREC evaluation studies. These will be used as baseline functions for comparisons. The functions are Okapi

Performance comparison for user-provided queries for discovery process.

<table><tr><td rowspan="3"></td><td colspan="7">Ranking functions</td></tr><tr><td colspan="2">Discovered by GP</td><td colspan="5">Well-known functions</td></tr><tr><td>GP1</td><td>GP2</td><td>Okapi BM25</td><td>Okapi BM2500</td><td>PTFIDF</td><td>INQUERY</td><td></td></tr><tr><td rowspan="2">Performance measures</td><td>P_Avg</td><td>0.2821</td><td>0.2675</td><td>0.2247</td><td>0.2397</td><td>0.1736</td><td>0.1749</td></tr><tr><td>P_10</td><td>0.2886</td><td>0.2841</td><td>0.2420</td><td>0.2602</td><td>0.2080</td><td>0.2227</td></tr></table>

BM 25, Okapi BM2500, Pivoted TFIDF, and INQUERY. Details of these functions can be found elsewhere [19,42].

## 4.6. GA optimization process

The GA based optimization process follows steps shown in Fig. 5. The training phase is conducted for 30 generations $( N _ { \mathrm { g e n } }$ parameter). The population size is 100. After each generation we record the top 10 $( N _ { \mathrm { t o p } }$ parameter) set of weights along with their <sup>fi</sup>tness. We copy the top 15% of the individuals in a generation into next generation. The remaining 85% individuals are selected using tournament selection. The crossover rate is chosen as 70%. We use Blx\_alpha crossover operator as it has proved very effective in other evaluation studies with real-valued genes (components of chromosomes or individuals) [20]. Mutations are performed by introducing Gaussian noise in randomly selected (according to mutation rate of 15%) genes. In the validation phase the 300 candidate set of weights are applied on the validation documents. The best performing individual on the validation dataset is chosen as a representative to be applied on test dataset. All the results reported in the next section are based on results from test dataset

## 4.7. Fitness functions used

In the GA optimization phase we wanted to test for the effect of <sup>fi</sup>tness functions used during optimization. We used three different <sup>fi</sup>tness functions: P\_Avg (Eq. (2)), CHK, and DCG [13,28]. These are order based <sup>fi</sup>tness functions and have been used in other evaluation studies [34].

We now proceed to discuss the results obtained by using our framework.

## 5. Results and discussion

In this section we discuss the results of experiments done in the last section. We <sup>fi</sup>rst report results for user-provided queries and then for relevance feedback queries. Within each of these we will report results for ad-hoc retrieval and then for routing retrieval. After that we will discuss the effects of using various <sup>fi</sup>tness functions on the robustness of our results. Results have been provided as averages of performance measures obtained across all queries. This is standard practice for reporting results in the IR literature [9,17,24,25].

Performance comparisons for routing task with P\_Avg <sup>fi</sup>tness function for userprovided queries.

<table><tr><td rowspan="2">Method</td><td colspan="4">Performance measures</td></tr><tr><td>P_Avg</td><td>Improvement by GA based optimization</td><td>P_10</td><td>Improvement by GA based optimization</td></tr><tr><td>GA based optimization</td><td>0.2973</td><td>-</td><td>0.3170</td><td>-</td></tr><tr><td>Pivoted TFIDF</td><td>0.1736</td><td>71%</td><td>0.2080</td><td>52%</td></tr><tr><td>INQUERY</td><td>0.1749</td><td>70%</td><td>0.2227</td><td>42%</td></tr><tr><td>Okapi BM25</td><td>0.2247</td><td>32%</td><td>0.2420</td><td>31%</td></tr><tr><td>Okapi BM2500</td><td>0.2397</td><td>24%</td><td>0.2602</td><td>22%</td></tr><tr><td>GP2</td><td>0.2675</td><td>11%</td><td>0.2841</td><td>12%</td></tr><tr><td>GP1</td><td>0.2821</td><td>5%</td><td>0.2886</td><td>10%</td></tr><tr><td>SA based optimization</td><td>0.2797</td><td>6%</td><td>0.2857</td><td>11%</td></tr></table>

Table 5 Performance comparisons for ad-hoc task with P\_Avg <sup>fi</sup>tness function for user-provided queries.

<table><tr><td rowspan="2">Method</td><td colspan="4">Performance measures</td></tr><tr><td>P_Avg</td><td>Improvement by GA based Optimization</td><td>P_10</td><td>Improvement by GA based Optimization</td></tr><tr><td>GA based optimization</td><td>0.2866</td><td>-</td><td>0.2977</td><td>-</td></tr><tr><td>Pivoted TFIDF</td><td>0.1736</td><td>65%</td><td>0.2080</td><td>43%</td></tr><tr><td>INQUERY</td><td>0.1749</td><td>64%</td><td>0.2227</td><td>34%</td></tr><tr><td>Okapi BM25</td><td>0.2247</td><td>28%</td><td>0.2420</td><td>23%</td></tr><tr><td>Okapi BM2500</td><td>0.2397</td><td>20%</td><td>0.2602</td><td>14%</td></tr><tr><td>GP2</td><td>0.2675</td><td>7%</td><td>0.2841</td><td>5%</td></tr><tr><td>GP1</td><td>0.2821</td><td>2%</td><td>0.2886</td><td>3%</td></tr><tr><td>SA based optimization</td><td>0.2669</td><td>7%</td><td>0.2837</td><td>3%</td></tr></table>

## 5.1. Results on user-provided querie

User-provided queries are raw queries without any modi<sup>fi</sup>cations due to relevance feedback. The results obtained by applying the discovery framework alone on these queries are as shown in Table 3. The numbers are the average of all queries. We see that the two discovered functions by our GP process namely GP1 and GP2 signi<sup>fi</sup>cantly outperform any of the well-known ranking functions used. Among the well-known ranking functions Okapi Bm2500 performed the best. But GP1 and GP2 outperformed<sup>5</sup> this by 17.7% and 11.6% respectively on P\_Avg and by 10.91% and 9.19% respectively on P\_10.

The best ranking function discovered by GP (GP1) for ad-hoc queries is shown in Eq. (3)

$$
\log \left(\frac {t f \_ D o c}{t f \_ m a x \_ D o c} \times \frac {d f \_ m a x \_ D o c}{d f \_ D o c} \times \frac {\text { length\_avg\_Abstract\_Col }}{t f \_ a v g \_ A b s t r a c t}\right)\tag{3}
$$

We can see that the <sup>fi</sup>rst part of the equation $\frac { t f _ { - } D o c } { t f _ { - } m a x _ { - } D o c }$ is the wellknown normalized tf in IR [39]. The second part $\frac { d f _ { - } m a x _ { - } D o c } { d f _ { - } D o c }$ is a new normalized IDF. The third part $\frac { l e n g t h \_ a v g \_ A b s t r a c t \_ C o l } { t f \_ a v g \_ A b s t r a c t }$ is the structural part <sup>- -</sup>of the ranking function. It can be treated as a scaling factor for the ranking. We can see that the GP process is indeed able to discover well-known existing relationships as well as discover truly new ones.

It is to be noted that the functional form of the second best ranking function (GP2) discovered by GP was quite different from that of GP1 in terms of the features selected and the way these features were combined. This indicates that our method is able to discover functions from different types of formula and is not restricted to just a variation of a type of formulae.

We use the two discovered ranking functions GP1 and GP2 as two of the six ranking functions in the GA based optimization process<sup>6</sup>. The results of optimization are shown for both the ad-hoc task and the routing task in Tables 4 and 5 respectively.

It is clear from Tables 4 and 5 that our GA based optimization method outperforms the well-known ranking functions (baselines)<sup>7</sup> for both the routing task and the ad-hoc task of retrieval, with differences ranging from 20% to 70% for P\_Avg performance measure and from 14% to 52% for the P\_10 performance measure. The method also outperforms the two ranking functions discovered by GP in the earlier stage. It was observed that optimization done using simulated annealing barely matched the best matching function (GP1). The GA based optimization was at least 6% better on P\_Avg and at least 3% better on P\_10 performance measure, than the one achieved by simulated annealing.

Table 6  
Performance comparisons for routing task with P\_Avg <sup>fi</sup>tness function for relevance feedback queries.

<table><tr><td rowspan="2">Method</td><td colspan="4">Performance measures</td></tr><tr><td>P_Avg</td><td>Improvement by GA based optimization</td><td>P_10</td><td>Improvement by GA based optimization</td></tr><tr><td>GA based optimization</td><td>0.4704</td><td>-</td><td>0.4835</td><td>-</td></tr><tr><td>Pivoted TFIDF</td><td>0.3382</td><td>39%</td><td>0.3614</td><td>34%</td></tr><tr><td>INQUERY</td><td>0.2792</td><td>68%</td><td>0.3261</td><td>48%</td></tr><tr><td>Okapi BM25</td><td>0.4003</td><td>18%</td><td>0.4250</td><td>14%</td></tr><tr><td>Okapi BM2500</td><td>0.4170</td><td>13%</td><td>0.4307</td><td>12%</td></tr><tr><td>GP2</td><td>0.4424</td><td>6%</td><td>0.4464</td><td>8%</td></tr><tr><td>GP1</td><td>0.4556</td><td>3%</td><td>0.4680</td><td>3%</td></tr><tr><td>SA based optimization</td><td>0.4478</td><td>5%</td><td>0.4507</td><td>7%</td></tr></table>

Another interesting observation can be made from these tables. The optimization performance decreases by 3.6% on P\_Avg and by 6.1% on P\_10 as we go from routing queries to ad-hoc queries. This is expected because by the very nature of ad-hoc queries the optimization is trying to <sup>fi</sup>nd a set of weights that are suitable for all the queries together, while in the case of routing queries the optimization has to <sup>fi</sup>nd the weights just for a particular query. It is to be noted that in adhoc queries all the queries together serve as input to the GA optimization process. The optimization process <sup>fi</sup>nds an optimal set of weights for this set of queries. On the other hand in routing queries the GA optimization process <sup>fi</sup>nds an optimal set of weights for each of the queries separately. The results reported for routing queries are thus average performance measures for each of the query. Hence we see performance improvements in routing queries as compared to the ad-hoc queries. But even with this decrease in performance for ad-hoc queries as compared to routing queries, it is observed that the GA based optimization still outperforms the six individual ranking functions.

## 5.2. Results on relevance feedback queries

As stated earlier the relevance feedback queries are generated based on relevance information. The results of the optimization process on these types of queries are summarized in Tables 6 and 7. Comparing these results with those for the user-provided queries, one noticeable difference is the huge improvement of the performance measures of the individual well-known ranking functions (the baselines). Relevance feedback improves the baseline performance by 80%–100%. Even with these highly improved baseline results we can make similar (to the user-provided queries) observations about the performance obtained by the discovery process and the GA optimization process. The GP discovery process can still discover ranking functions which outperform<sup>8</sup> the individual wellknown ranking functions (baselines) while the GA based optimization outperforms all the well-known individual ranking functions as well as the two best discovered ranking functions by GP. The performance improvement over well-known ranking functions (baselines) ranges from 9% to 39% on P\_Avg and from 10% to 34% on P\_10 measure.

Table 7  
Performance comparisons for ad-hoc task with P\_Avg <sup>fi</sup>tness function for relevance feedback queries.

<table><tr><td rowspan="2">Method</td><td colspan="4">Performance measures</td></tr><tr><td>P_Avg</td><td>Improvement by GA based optimization</td><td>P_10</td><td>Improvement by GA based optimization</td></tr><tr><td>GA based optimization</td><td>0.4530</td><td></td><td>0.4725</td><td></td></tr><tr><td>Pivoted TFIDF</td><td>0.3382</td><td>34%</td><td>0.3614</td><td>31%</td></tr><tr><td>INQUERY</td><td>0.2792</td><td>62%</td><td>0.3261</td><td>45%</td></tr><tr><td>Okapi BM25</td><td>0.4003</td><td>13%</td><td>0.4250</td><td>11%</td></tr><tr><td>Okapi BM2500</td><td>0.4170</td><td>9%</td><td>0.4307</td><td>10%</td></tr><tr><td>GP2</td><td>0.4319</td><td>5%</td><td>0.4453</td><td>6%</td></tr><tr><td>GP1</td><td>0.4366</td><td>4%</td><td>0.4573</td><td>3%</td></tr><tr><td>SA based optimization</td><td>0.4308</td><td>5%</td><td>0.4441</td><td>6%</td></tr></table>

## 5.3 Effect of fitness functions

The genetic process requires the use of a <sup>fi</sup>tness function. Inappropriate choice of such a <sup>fi</sup>tness function may mean suboptimal results. Hence we wanted to test the effect of <sup>fi</sup>tness functions on our results. As mentioned earlier we chose three wellknown <sup>fi</sup>tness functions P\_Avg, CHK, and DCG for our evaluations. Tables 8 and 9 highlight the performance difference (in terms of P\_Avg and P\_10 performance measure) obtained for both the routing and ad-hoc tasks by using the three <sup>fi</sup>tness functions. The <sup>fi</sup>rst table gives the data for user-provided queries while the second gives the data for relevance feedback queries. It was observed that our results are not affected by the <sup>fi</sup>tness function used as long as it is a wellknown <sup>fi</sup>tness function. The variation in performance obtained by different <sup>fi</sup>tness functions was less than 5% for either of the performance measures.

## 6. Conclusion

In this paper we presented an integrated framework for using genetic-based approaches (speci<sup>fi</sup>cally the Genetic Programming and Genetic Algorithms) to discover new ranking functions as well as to optimize the well-known existing ones. The <sup>fi</sup>rst part of the framework uses GP to discover novel ranking functions. We used both the content as well as the structural information in HTML documents to discover such functions. It was observed that these newly discovered functions outperformed the baseline namely the existing well-known ranking functions. To improve the retrieval performance further we incorporate the second stage of optimization in our model. It uses the scores assigned by individual ranking functions to the documents and assigns weights to these scores. The set of weights are optimized using Genetic Algorithms. It was observed that such optimized ranking function outperformed all the baselines as well as the newly discovered ranking functions by GP.

Our framework can be easily applied in practice. The process would start with the search engine processing information about previous search results to discover new ranking function and optimized weights for a set of well-known ranking functions, for a set of queries (ad-hoc queries given to the search engine). Then when a new query arrives, this newly discovered ranking function, along with the optimized weights, can be used to retrieve information for the user. User feedback about the relevance of documents retrieved can be used to <sup>fi</sup>ne-tune the starting ranking function and starting weights. This process can be repeated for any new search query. It is to be noted that the search performance in terms of time to retrieve the documents would not suffer in this scheme as the GP discovery and GA optimization happen of<sup>fl</sup>ine and before the user issues a new search query.

Table 8  
Effect of <sup>fi</sup>tness functions on performance for user-provided queries.

<table><tr><td rowspan="2" colspan="4"></td><td colspan="3">Fitness functions</td></tr><tr><td>P_Avg</td><td>CHK</td><td>DCG</td></tr><tr><td rowspan="4">Task</td><td rowspan="2">Routing</td><td rowspan="2">Performance measure</td><td>P_Avg</td><td>0.2973</td><td>0.3116</td><td>0.3079</td></tr><tr><td>P_10</td><td>0.3170</td><td>0.3328</td><td>0.3284</td></tr><tr><td rowspan="2">Ad-hoc</td><td rowspan="2">Performance measure</td><td>P_Avg</td><td>0.2866</td><td>0.2839</td><td>0.2880</td></tr><tr><td>P_10</td><td>0.2977</td><td>0.2909</td><td>0.3045</td></tr></table>

Table 9  
Effect of <sup>fi</sup>tness functions on performance for relevance feedback queries.

<table><tr><td rowspan="2" colspan="4"></td><td colspan="3">Fitness functions</td></tr><tr><td>P_Avg</td><td>CHK</td><td>DCG</td></tr><tr><td rowspan="4">Task</td><td rowspan="2">Routing</td><td rowspan="2">Performance measure</td><td>P_Avg</td><td>0.4704</td><td>0.4821</td><td>0.4747</td></tr><tr><td>P_10</td><td>0.4835</td><td>0.4914</td><td>0.4888</td></tr><tr><td rowspan="2">Ad-hoc</td><td rowspan="2">Performance measure</td><td>P_Avg</td><td>0.4530</td><td>0.4512</td><td>0.4543</td></tr><tr><td>P_10</td><td>0.4725</td><td>0.4698</td><td>0.4805</td></tr></table>

We see a number of signi<sup>fi</sup>cant contributions of this research:

• Our framework can discover as yet unknown ranking functions which can contribute signi<sup>fi</sup>cantly to the retrieval performance.

• The framework can combine the evidence from existing well-known ranking functions to further improve performance.

• The framework works well with both the routing and ad-hoc queries for retrieval.

• Our method is scalable. In the discovery phase we can incorporate any number of features and functions. There is no restriction on the type of feature or the type of functions to be used. Similarly, in the optimization phase we can incorporate any number of ranking functions.

• The framework works well with both the user-based queries as well as with the relevance feedback queries.

• The framework can be used with any <sup>fi</sup>tness function.

In the future, we plan to apply this framework to more diverse document collections such as XML collections, and multimedia data collections to see its viability in these settings. The framework proposed in this paper can also be applied to other data mining and operations research tasks where proper ranking or ordering of subjects is highly desired.

## References

[1] qwww.searchenginewatch.com.q

[2] B. Bartell, G. Cottrell, R.K. Belew, Automatic combination of multiple ranked retrieval systems, Proceedings of the 17th Annual International ACM-SIGIR Conference on Research and Development in Information Retrieval (SIGIR), 1994, pp. 173–181, (Dublin).

[3] B. Bartell, G. Cottrell, R.K. Belew, Optimizing similarity using multi-query relevance feedback, Journal of the American Society for Information Science 49 (1998) 742–761.

[4] N.J. Belkin, P. Kantor, E.A. Fox, J.A. Shaw, Combining the evidence of multiple query representations for information retrieval, Information Processing & Management 31 (1995) 431–448.

[5] H. Billhardt, D. Borrajo, V. Maojo, Learning retrieval expert combinations with genetic algorithms, International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems 11 (2003) 87-113

[6] A. Bookstein, Probability and fuzzy set applications to information retrieval, Annual Review of Information Science and Technology 20 (1985) 117–151.

[7] G. Bordogna, G. Pasi, A fuzzy linguistic approach generalizing Boolean information retrieval: a model and its evaluation, Journal of the American Society for Information Science 44 (1993) 70–82.

[8] S. Brin, L. Page, The anatomy of a large-scale hypertextual Web search engine, Computer Networks and ISDN Systems 30 (1998) 107–117.

[9] L. Chen, K. Sycara, WebMate: a personal agent for browsing and searching, in: K.P.S.a.M. Wooldridge (Ed.), Proceedings of the 2nd International Conference on Autonomous Agents (Agents'98), ACM Press, New York, 1998, pp. 132–139.

[10] H. Chen, Y. Chung, M. Ramsey, C. Yang, A smart itsy bitsy spider for the Web, Journal of the American Society for Information Science 49 (1998) 604–618.

[11] H. Chen, G. Shankaranarayanan, L. She, A. Iyer, A machine learning approach to inductive query by examples: an experiment using relevance feedback, ID3, genetic algorithms, and simulated annealing, Journal of the American Society for Information Science 49 (1998) 693–705.

[12] O. Cordon, F. Moya, M.C. Zarco, A new evolutionary algorithm combining simulated annealing and genetic programming for relevance feedback in fuzzy information retrieval systems, Soft Computing 6 (2002) 308–319.

[13] W. Fan, E.A. Fox, P. Pathak, H. Wu, The effects of <sup>fi</sup>tness functions on genetic programming-based ranking discovery for web search, Journal of the American Society for Information Science and Technology 55 (2004) 628–636.

[14] W. Fan, M. Gordon, P. Pathak, Discovery of context-speci<sup>fi</sup>c ranking functions for effective information retrieval using genetic programming, IEEE Transactions on Knowledge and Data Engineering 16 (2004) 523–527.

[15] W. Fan, M.D. Gordon, P. Pathak, Effective pro<sup>fi</sup>ling of consumer information retrieval needs: a uni<sup>fi</sup>ed framework and empirical comparison, Decision Support Systems 40 (2005) 213–233.

[16] W. Fan, M. Gordon, P. Pathak, An integrated two-stage model for intelligent information routing, Decision Support Systems 42 (2006) 362–374.

[17] W. Fan, M. Gordon, P. Pathak, On linear mixture of experts approach to information retrieval, Decision Support Systems 42 (2006) 975–987.

[18] E.A. Fox, J.A. Shaw, Combination of multiple searches, Proceedings of the 2nd Text Retrieval Conference (TREC-2), vol. 500-215, NIST, 1994, pp. 243–252.

[19] J. Gao, G. Cao, H. He, M. Zhang, J. Nie, S. Walker, S.E. Robertson, TREC-10 web track experiments at MSRA, in: E. Voorhees, H.D. (Eds.), Tenth Text Retrieval Conference NIST Special Publication, 2002, pp. 384–392.

[20] D.E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning, Addison-Wesley, 1989.

[21] M. Gordon, Probabilistic and genetic algorithms for document retrieval, Communications of ACM 31 (1988) 152–169.

[22] M. Gordon, User-based document clustering by redescribing subject descriptions with a genetic algorithm, Journal of the American Society for Information Science 42 (1991) 311–322.

[23] U. Güntzer, R. Müller, S. Müller, R.-D. Schimkat, Retrieval for decision support resources by structured models, Decision Support Systems 43 (2007) 1117–1132.

[24] D. Hawking, Overview of the TREC-9 web track, in: E. Voorhees, H.D. (Eds.), Ninth Text Retrieval Conference, NIST Special Publication, vol. 500-249, 2000, pp. 86–102

[25] D. Hawking, N. Craswell, Overview of the TREC-2001 web track, in: E. Voorhees, D.K. Harman (Eds.), Proceedings of the Tenth Text Retrieval Conference, vol. 500-250, NIST, 2001, pp. 61–67.

[26] J.H. Holland, Adaptation in Natural and Arti<sup>fi</sup>cial Systems, 2nd ed.MIT Press, 1992.

[27] J. Horng, C. Yeh, Applying genetic algorithms to query optimization in document retrieval, Information Processing & Management 36 (2000) 737–759.

[28] K. Jarvelin, J. Kekalainen, IR evaluation methods for retrieving highly relevant documents Proceedings of the 23rd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, New York, 2001, pp. 41–48.

[29] S. Kirkpatrick, C.D. Gelatt, M.P. Vecchi, Optimization by simulated annealing, Science 220 (1983) 671–680.

[30] J.M. Kleinberg, Authoritative sources in a hyperlinked environment, Journal of the Association for Computing Machinery 46 (1999) 604

[31] J.R. Koza, Genetic Programming: On the Programming of Computers by Means of Natural Selection, MIT Press Cambridge MA USA 1992

[32] D. Kraft, E. Petry, B. Buckles. T. Sadasivan, Genetic algorithms for query optimization in information retrieval: relevance feedback, Genetic Algorithms and Fuzzy Logic Systems: Soft Computing Perspectives, 1997, pp. 155–173.

[33] J. Lee, Analysis of multiple evidence combination, Proceedings of Twentieth Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 1997, pp. 267–276.

[34] C. Lopez-Pujalte, V.P. Guerrero Bote, F.d.M. Anegon, A test of genetic algorithms in relevance feedback, Information Processing & Management 38 (2002) 793–805.

[35] M.J. Martin-Bautista, M. Vila, H.L. Larsen, A fuzzy genetic algorithm approach to an adaptive information retrieval agent, Journal of the American Society for Information Science 50 (1999) 760–771.

[36] P. Pathak, M. Gordon, W. Fan, Effective information retrieval using genetic algorithms based matching function adaptation, Proceedings of the 33rd Hawaii International Conference on System Science (HICSS), 2000, (Hawaii USA).

[37] S.E. Robertson, K.S. Jones, Relevance weighting of search terms, Journal of the American Society for Information Science 27 (1976) 129–146.

[38] S.E. Robertson, S. Walker, S. Jones, M.M. Hancock-Beaulieu, M. Gatford, Okapi at TREC-4, in: D.K. Harman (Ed.), Proceedings of the Fourth Text Retrieval Conference, NIST Special Publication, vol. 500-236, 1996, pp. 73–97.

[39] G. Salton, Automatic Text Processing, Addison-Wesley Publishing Co., Reading, MA, 1989.

[40] G. Salton, C. Buckley, Term weighting approaches in automatic text retrieval, Information Processing and Management 24 (1988) 513–523.

[41] J. Savoy, M. Ndarugendamwo, D. Vrajitoru, Report on the TREC-4 experiment: combining probabilistic and vector space schemes, in: D.K. Harman (Ed.), Proceedings of the Fourth Text REtrieval Conference (TREC-4), NIST, 1996, pp. 537-548

[42] A. Singhal, G. Salton, M. Mitra, C. Buckley, Document length normalization, Information Processing and Management 32 (1996) 619–633.

[43] C. Vogt, G. Cottrell, Fusion via a linear combination of scores, Information Retrieval 1 (1999) 151–173.

[44] V. Vrajitoru, Crossover improvement for the genetic algorithm in information retrieval, Information Processing & Management 34 (1998) 405–415.

[45] J. Zobel, A. Moffat, Exploring the similarity space, SIGIR Forum 32 (1998) 18–34

![](/api/attachments/44S289D9/fulltext/images/30dfee7cc8ddea397b118feedcf51abb69f761fa4c319587adc38d233d06c879.jpg)

Dr. Weiguo (Patrick) Fan is an Associate Professor of Accounting and Information Systems at the Virginia Polytechnic Institute and State University (Virginia Tech). He received his Ph.D. in Information Systems from the Ross School of Business, University of Michigan, Ann Arbor, in July 2002, a M. Sce in Computer Science from the National University of Singapore in 1997, and a B. E. in Information and Control Engineering from the Xi'an Jiaotong University, P.R. China, in 1995. His research interests focus on the design and development of novel information technologies — information retrieval, data mining, text/web mining, social computing, personalization and knowledge management techniques — to support better business information man-

![](/api/attachments/44S289D9/fulltext/images/eade8e58c55cfbd5aa632ec1859e19df1f5fa9cb710fc34d8573d5a4d9ce4631.jpg)

Dr. Mi Zhou is an Assistant Professor of School of Management at Xi'an Jiaotong University, P.R. China. She received her Ph.D. in Management Science and Engineering from the School of Management at Xi'an Jiaotong University, P.R. China, in July 2007, a M.Sce. in Management Science and Engineering at Xi'an Jiaotong University, P.R. China, in 1998, and a B.E. in Mechanical Engineering from Nanjing Polytechnic University, P.R. China, in 1992. Her research interests focus on the information management, social relationship and knowledge management (knowledge transfer, knowledge sharing, knowledge creation), models of online knowledge communities.

agement and decision making. He has published more than 90 refereed journal and conference papers. His research has appeared in many prestigious information technology journals such as ACM Transactions on Internet Technology, Communications of the ACM, Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, IEEE Intelligent Systems, Information Systems, Information Processing and Management, Journal of the American Society on Information Science and Technology, Journal of Management Information Systems, Pattern Recognition, etc., and in leading information technology conferences such as SIGIR, WWW, CIKM, HLT, ICIS, HICSS, AMCIS,DS, ICOTA, etc. His research studies are/have been funded by NSF, PWC.

![](/api/attachments/44S289D9/fulltext/images/b177b523a676d64fba2fe4e33caadd00b757a5af6b4b47089d60f5ecb9846e1e.jpg)

Dr. Praveen Pathak is an Associate Professor of Information Systems and Operations Management at the Warrington College of Business at the University of Florida. He received his PhD in Information Systems from the Ross School of Business, University of Michigan, Ann Arbor, in 2000. He also holds an MBA (PGDM) from the Indian Institute of Management, Calcutta, and an Engineering degree, B. Tech. (Hons.), from the Indian Institute of Technology, Kharagpur. His research interests include information retrieval, web mining, offshore outsourcing and business intelligence. His research has appeared in many journals such as Journal of Management Information Systems (JMIS), Decision Support Systems (DSS), IEEE Transactions on Knowledge and

Data Engineering (TKDE), Information Processing and Management (IP&M), Journal of the American Society for Information Science and Technology (JASIST), and in leading information technology conferences such as ICIS, HICSS, WITS, and INFORMS.
