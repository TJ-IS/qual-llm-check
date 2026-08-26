---
otero_id: 19531
otero_key: "992SDHGD"
title: "Building a term suggestion and ranking system based on a probabilistic analysis model and a semantic analysis graph"
authors: "Lin-Chih Chen"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.02.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building a term suggestion and ranking system based on a probabilistic analysis model and a semantic analysis graph

Lin-Chih Chen ⁎

Department of Information Management, National Dong Hwa University, No. 1, Sec. 2, Da Hsueh Road, Shou-Feng, Hualien 97401, Taiwan

## a r t i c l e i n f o

Article history: Received 28 October 2010 Received in revised form 11 November 2011 Accepted 2 February 2012 Available online 15 February 2012

Keywords: Probabilistic analysis model Semantic analysis graph Probability parameters Expectation maximization algorithm Euclidean distance

## a b s t r a c t

Term suggestion is a kind of information retrieval technique that attempts to suggest relevant terms to help users formulate more effective queries and reduce unnecessary search steps. In this paper, we apply two semantic analysis methods, the probabilistic analysis model and semantic analysis graph, to design a term suggestion system that can effectively deal with the problems of synonymy and polysemy. The main contributions of this paper are the following. First, we apply two semantic analysis methods to design a high-performance term suggestion system. Second, we design an intelligent mechanism that can effectively balance cost and performance to minimize the number of iterations required for our system.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Search Engine Optimization (SEO) is the process of improving a Website's position so the Web page comes up higher in the search results of major search engines. All search engines have a unique way of ranking the importance of a Website. Some search engines focus on the content while others review the Meta tags to identify who and what a Website's business is. Most search engines use a combination of content, Meta tags, link popularity, and click popularity to determine Website ranking. However, SEO is a dif<sup>fi</sup>cult task for the Website administrator to improve their Website's ranking since modern search engines apply different ranking policies to generate search engine listings, and the ranking policies change frequently [12].

Alternatively, the business can bid on certain terms or phrases related to its market orientation to obtain a higher ranking in search engine listings. However, this bidding process may result in a substantially high cost for the most popular search terms. A good way to start the bidding process is to bid on a large number of low-cost terms that are relevant to their product or service. If the business bids on a large number of these low-cost terms, the combined traf<sup>fi</sup>c from them adds up to the level produced by a popular search term, at a fraction of the cost. [21]. This method is typically called term suggestion or query suggestion [6].

The research objective of this paper is to develop a highperformance term suggestion system, called Learning-Inference (LI). Our system involves two main procedures: “Generating Parameter” and “Generating Candidate Term”. In the “Generating Parameter” procedure, we mainly use a probabilistic analysis model, called Probabilistic Latent Semantic Analysis (PLSA), to estimate the probability parameters of our system. In the “Generating Candidate Term” procedure, we apply a semantic analysis graph, called the Term Suggestion Graph (TSG), to generate all candidate terms. In the TSG graph, we <sup>fi</sup>rst build a graph based on a Breadth First Search (BFS) algorithm and the concept of the inverse link. Then, we transform the probability parameters into the edge weights of the graph to measure the similarity degree between the input search term and the suggested terms. In fact, since PLSA and TSG are all based on semantic analysis between two terms, this is why we use these two semantic analysis methods to suggest relevant terms.

We make the following two contributions in this paper. First, we implement a high-performance prototype system for the research of term suggestions. According to the results of computer simulation, we conclude our system outperforms other similar systems. Second, since the “Generating Parameter” procedure requires a lot of time and resources, we thus design an intelligent mechanism to save the number of iterations required for this procedure. In addition, according to the results of computer simulation, we conclude the suggested term generated from our mechanism is a performanceeffective solution.

The rest of this paper is structured as follows. We review some of the related work in the next section. Section 3 describes our

LI system in detail. Section 4 discusses the results of the computer simulation. Finally, Section 5 concludes this paper and outlines our future work.

## 2. Related work

In this section, we brie<sup>fl</sup>y review the related works in two aspects: online term suggestion systems and the termination criteria for the EM algorithm.

## 2.1. Online term suggestion systems

Several researchers have designed and implemented various term suggestion systems. The list of online systems is shown in Table 1. Wu and Chen [39] proposed a Highlight system that adopts lexical analysis and a probabilistic framework to generate relevant terms. Carpineto and Romano [3] designed the Credo system that applies a formal concept analysis to construct all suggested terms in a hierarchical tree structure allowing users to judge which one is appropriate. Osinski and Weiss [32] developed the Carrot2 system that uses sentences with variable length words as the candidate suggested terms; then, it utilizes suf<sup>fi</sup>x tree clustering to identify which one should be suggested. Radovanović and Ivanović [34] constructed the CatS system that uses a separate category tree, which is based on the concept of the dmoz taxonomy. Segev et al. [37] proposed the Vivisimo system that uses the concise all pairs pro<sup>fi</sup>ling (CAPP) clustering method to generate relevant terms. It compares all classes pairwise and then minimizes the overall number of features needed to guarantee each pair of classes is contrasted by at least one feature. Google [35] proposed a Google Proximity Search (GPS) system that submits the user's query to a search engine to get high ranking Web pages and expands new suggested terms in the proximity range of the query for all collected Web pages. Google and Yahoo have recently released two new term suggestion systems: Google AdWords (GA) [15] and Yahoo Search Marketing (YSM) [41]. These two systems analyze the search logs to determine what terms are most searched for, and suggest associated popular terms to users. Ferragina and Guli [11] developed the SnakeT system that uses a frequent item set-like approach to extract all candidate terms; then, it uses a bottom-up hierarchy construction process to suggest relevant terms in a hierarchy form.

## 2.2. Termination criteria for the EM algorithm

The PLSA model is a statistical latent class model (or aspect model) that has recently shown excellent results in several information retrieval related tasks [27]. It has the positive feature of assigning probability distributions over classes to documents and terms. Aspect models are also successfully used in other areas of natural language processing, like language modeling [26] or parsing [40].

The PLSA model uses the Expectation Maximization (EM) algorithm to estimate the parameters that probabilistically characterize the hidden variables underlying the co-occurrence observation data, and measure the relationship among hidden and observed variables. The EM algorithm is an iterative procedure for <sup>fi</sup>nding maximum likelihood estimates when the observations can be viewed as incomplete data. Each iteration of the EM algorithm consists of two steps: expectation and maximization. In the expectation step, the missing data are estimated given the observed data and current estimate of the model parameters. In the maximization step, the log-likelihood function is maximized under the assumption the missing data are known.

The list of online systems available on the Internet.

<table><tr><td>System</td><td>URL</td></tr><tr><td>Highlight</td><td>http://highlight.njit.edu/</td></tr><tr><td>Credo</td><td>http://credo.fub.it/</td></tr><tr><td>Carrot2</td><td>http://search.carrot2.org/</td></tr><tr><td>CatS</td><td>http://tinyurl.com/3jn32ja</td></tr><tr><td>Vivisimo</td><td>http://clusty.com/</td></tr><tr><td>GPS</td><td>http://www.rapidkeyword.com/</td></tr><tr><td>GA</td><td>https://adwords.google.com/</td></tr><tr><td>YSM</td><td>http://tinyurl.com/3fjmnja</td></tr><tr><td>SnakeT</td><td>http://snaket.di.unipi.it/</td></tr><tr><td>LI</td><td>http://cayley.sytes.net/li_new</td></tr></table>

Although the EM algorithm can converge to a local optimal solution, it may take a lot of computing time to reach this solution. Alternatively, many researchers have adopted different mechanisms to determine whether the algorithm should be terminated. According to relevant literatures, these mechanisms are comprised of two termination criteria: (1) setting a <sup>fi</sup>xed number of iterations as the maximum allowable iterations of the algorithm [14,29,30]; and (2) setting a prede<sup>fi</sup>ned threshold to determine whether the algorithm should be terminated.

Let us now brie<sup>fl</sup>y review the second criterion. Ristad and Yianilos [36] de<sup>fi</sup>ned the termination criterion of the algorithm as the increased total probability of the training corpus between two consecutive iterations falling below a certain threshold rate. Zhang and Goldman [42] combined the algorithm with the concept of diverse density to solve multiple instance learning problems. They selected a set of instances in the expectation step; then, in the maximization step, they calculated the probability of diverse density from all selected data. They concluded the algorithm should be terminated if the increased probability between two consecutive iterations is less than or equal to a prede<sup>fi</sup>ned probability. Many researchers [14,33,38] used the log-likelihood function as the performance function of the algorithm. The algorithm should be terminated if the relative change in the performance function between two consecutive iterations is less than a relatively low probability.

Although these two termination criteria can obtain a fast response time compared with the local optimal solution, they may cause two major problems. First, a small number of iterations may result in a large difference compared with the <sup>fi</sup>nal solution and the local optimal solution. Second, a large number of iterations may result in small improvements compared with the <sup>fi</sup>nal solution and the local optimal solution.

To prevent these two potential problems, we use the concepts of improvement history progress and variation history progress to dynamically determine whether the algorithm should be terminated. It implies the number of iterations required to run the algorithm varies because the improvement history and the variation history are not always equal for each iteration of the algorithm. In Section 4.2, we will prove the <sup>fi</sup>nal solution derived from our combined concepts is a performance-effective solution.

## 3. Term suggestion and ranking system

This section describes our prototype system in detail. Our system involves two main procedures: “Generating Parameter” and “Generating Candidate Term”, as shown in Fig. 1(a) and (b), respectively. In the “Generating Parameter” procedure, we mainly use the PLSA model to estimate the probability parameters of our system. In the “Generating Candidate Term” procedure, we apply the TSG graph to generate all candidate terms. To generate the TSG graph, we <sup>fi</sup>rst build a graph based on the BFS algorithm and the concept of the inverse link. Then, we apply the average Euclidean distance to transform the probability parameters into the edge weights of the graph to measure the similarity degree between two terms.

In this paper we adopt two semantic analysis methods, TSG and PLSA, to implement a new term suggestion system. In the second procedure, we use a TSG graph to generate all candidate terms. TSG is a powerful graph search method to <sup>fi</sup>nd terms with semantic relations [43]. However, it lacks not only the ability to distinguish the type of semantic relations, including synonymy and polysemy, but also the ability to calculate the degree of similarity between terms. In the <sup>fi</sup>rst procedure, we use a PLSA model to solve these two problems. PLSA can deal with the problems of synonymy and polysemy and can explicitly distinguish between different meanings and different types of term usage [5,17]. That is, in our system, we <sup>fi</sup>rst use TSG to <sup>fi</sup>nd good candidate terms. Then, we use PLSA to identify the type of semantic relations between and to calculate the similarity degree

![](/api/attachments/992SDHGD/fulltext/images/cd9caeb5d316f4928e6f68f71fa9791216ddefb19bcc78b27db711185b2b4a0a.jpg)  
(a) The procedure of “Generating Parameter”

![](/api/attachments/992SDHGD/fulltext/images/58df59bab8839b46e0e9cc1dfb513811a36649df8fec021cc5f08d700f454ed8.jpg)  
(b) The procedure of “Generating Candidate Term”  
Fig. 1. The <sup>fl</sup>owchart for our system.

$$
P r o b P a r a m e t e r s = \left[ \begin{array}{c c c c c} P (1, 1) & \dots & P (1, d _ {j}) & \dots & P (1, N) \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ P (t _ {i}, 1) & \dots & P (t _ {i}, d _ {j}) & \dots & P (t _ {i}, N) \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ P (M, 1) & \dots & P (M, d _ {j}) & \dots & P (M, N) \end{array} \right]
$$

Fig. 2. The probability parameters of our system.

between terms. The details of these two procedures are described in Sections 3.1 and 3.2, respectively.

## 3.1. The procedure of “generating parameter”

The PLSA model has been successfully applied to various Information Retrieval (IR) <sup>fi</sup>elds such as collaborative <sup>fi</sup>ltering [17], Web mining [13], text learning and mining [16], and co-citation analysis [8]. It can effectively deal with the problems of synonymy (two terms are syntactically different but semantically interchangeable expressions) and polysemy (a term has different meanings), even though two terms never occur together [16,17]. In this paper, we use the PLSA model to estimate the probability parameters of our system for a corpus with M terms and N documents, as shown in Fig. 2, where $P ( t _ { i } , d _ { j } )$ is the latent probability of a term $t _ { i } , i { \in } \{ 1 , 2 , . . . , M \}$ , in a particular document $d _ { j } , j { \in } \{ 1 , 2 , . . . , N \}$

The PLSA model is based on a probabilistic model called the aspect model, which can be utilized to identify the hidden semantic relations between terms. The aspect model is a latent variable model for co-occurrence data, which associates unobserved class variables $z _ { k } , \ k { \in } \{ 1 , 2 , . . . , L \}$ with each observation, where L is the total number of latent topics. In our settings, the observation is an occurrence of a term t in a particular document $d _ { j } .$ The probabilities related to this model are de<sup>fi</sup>ned as follows: $\overline { { ( 1 ) \ P ( t _ { i } ) } }$ is the probability $t _ { i }$ has been selected; $( 2 ) P ( d _ { j } | t _ { i } )$ is the posterior probability of $d _ { j }$ occurring in $t _ { i } \colon ( 3 ) \ P ( d _ { j } | z _ { k } )$ is the posterior probability of $d _ { j }$ occurring in a latent topic $z _ { k } ;$ and $( 4 ) \ P ( \boldsymbol { z } _ { k } | t _ { i } )$ is the posterior probability of z<sub>k</sub> occurring in t<sub>i</sub>.

Based on these de<sup>fi</sup>nitions, we calculate the latent probability of an observed pair (t ,d ) by adopting a series of unobserved class variables $z _ { k } ,$ as shown in the following:

$$
P (t _ {i}, d _ {j}) = P (t _ {i}) P (d _ {j} | t _ {i}), w h e r e P (d _ {j} | t _ {i}) = \sum_ {k = 1} ^ {L} P (d _ {j} | z _ {k}) P (z _ {k} | t _ {i})\tag{1}
$$

Summing over all possible choices of $z _ { k }$ from which the observation could have been generated, using Bayes' rule, it is straightforward to transform the latent probability $P ( t _ { i } , d _ { j } )$ into the following form:

$$
P (t _ {i}, d _ {j}) = \sum_ {k = 1} ^ {L} P (z _ {k}) P (t _ {i} | z _ {k}) P (d _ {j} | z _ {k})\tag{2}
$$

where $P ( z _ { k } )$ is the probability $z _ { k }$ has been observed; $P ( t _ { i } | z _ { k } )$ is the posterior probability of $t _ { i }$ occurring in $z _ { k } .$

Now, to calculate $P ( t _ { i } , d _ { j } )$ , we need to estimate the parameters, $P ( z _ { k } ) , ~ P ( t _ { i } | z _ { k } )$ , and $P ( d _ { j } | z _ { k } )$ , while maximizing the following loglikelihood function at iteration n:

$$
L L _ {n} \left(t _ {i}, d _ {j}\right) = \sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {N} t d \left(t _ {i}, d _ {j}\right) \log P \left(t _ {i}, d _ {j}\right)\tag{3}
$$

where $t d ( t _ { i } , d _ { j } )$ is the weight of the term-document matrix for term $t _ { i }$ in Web page $d _ { j }$

The EM algorithm [9] is a well-known method to perform maximum log-likelihood parameter estimation in probabilistic latent variable models. Generally, two steps are required to perform this algorithm alternately: (1) expectation step where the posterior probability of $z _ { k }$ is calculated based on the current estimates of the parameters t and d ; and (2) maximization step where the PLSA parameters, including $P ( z _ { k } ) , P ( t _ { i } | z _ { k } )$ , and $P ( d _ { j } | z _ { k } )$ , are updated and used to maximize the log-likelihood function based on the posterior probability of z calculated in the previous expectation step.

The EM algorithm begins with some initial values of $P ( z _ { k } ) , P ( t _ { i } | z _ { k } )$ and $P ( d _ { j } | z _ { k } )$ . The initial parameters of PLSA can be determined by using either randomly initialized knowledge or some prior knowledge [5]. In the expectation step, PLSA again applies Bayes' rule to generate the posterior probability of z<sub>k</sub> based on the current estimates of the parameters $t _ { i }$ and $d _ { j }$ as follows:

$$
P (z _ {k} | t _ {i}, d _ {j}) = P (z _ {k}) P (t _ {i} | z _ {k}) P (d _ {j} | z _ {k}) / \sum_ {k = 1} ^ {L} P (z _ {k}) P (t _ {i} | z _ {k}) P (d _ {j} | z _ {k})\tag{4}
$$

In the maximization step, PLSA applies the Lagrange multipliers method (see [16] for details) to solve the constraint maximization problem to obtain the following equations for the re-estimated parameters:

$$
P (z _ {k}) = \sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {N} t d (t _ {i}, d _ {j}) P (z _ {k} | t _ {i}, d _ {j}) / \sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {N} t d (t _ {i}, d _ {j})\tag{5}
$$

$$
P (t _ {i} | z _ {k}) = \sum_ {j = 1} ^ {N} t d (t _ {i}, d _ {j}) P (z _ {k} | t _ {i}, d _ {j}) / \sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {N} t d (t _ {i}, d _ {j}) P (z _ {k} | t _ {i}, d _ {j})\tag{6}
$$

$$
P (d _ {j} | z _ {k}) = \sum_ {i = 1} ^ {M} t d (t _ {i}, d _ {j}) P (z _ {k} | t _ {i}, d _ {j}) / \sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {N} t d (t _ {i}, d _ {j}) P (z _ {k} | t _ {i}, d _ {j})\tag{7}
$$

Iterating the computation of the expectation and maximization steps monotonically increases the log-likelihood function of the observed data until the termination criteria are reached.

The time complexity of PLSA is closely related to the convergence speed of the EM algorithm. Hoffmann [17] has proved the time complexity of PLSA is ${ \cal O } ( M \times N \times L )$ , where O(M×N) is the time complexity of the EM algorithm for each iteration.

However, in the current Internet environment, the total number of terms (M) and the total number of documents (N) are both huge [22]. Meanwhile, the total number of latent topics (L) is increased along with increased M and N [19]. This easily results in the problem of performance degradation in such a large size M, N, and L when PLSA is applied to solve large-scale IR problems.

According to the above discussion of Section 2.2, the termination criteria of the EM algorithm involve the following two cases: (1) it converges to the local optimal solution; and (2) the maximum allowable number of iterations is reached. Let us discuss these two cases in detail.

Case 1. It converges to the local optimal solution.

In this case, we de<sup>fi</sup>ne the local optimal solution is reached if the improvement value between two consecutive iterations is less than a prede<sup>fi</sup>ned threshold. We use the following equation to de<sup>fi</sup>ne the improvement value between two consecutive iterations.

$$
I M P _ {n} = L L _ {n} \left(t _ {i}, d _ {j}\right) - L L _ {n - 1} \left(t _ {i}, d _ {j}\right)\tag{8}
$$

According to the above de<sup>fi</sup>nition, we can easily de<sup>fi</sup>ne the local optimal solution is reached if the condition, $I M P _ { n } { \leq } \varepsilon ,$ is reached, where ε is a prede<sup>fi</sup>ned threshold.

## Case 2. The maximum allowable number of iterations is reached.

In this case, the maximum allowable number of iterations is usually set to a <sup>fi</sup>xed number of iterations through several experiments. However, it is a dif<sup>fi</sup>cult task to determine what is enough for the maximum allowable number of iterations. According to the discussion in Section 2.2, the EM algorithm uses a <sup>fi</sup>xed number of iterations because the maximum allowable number of iterations may result in the following two potential problems. On the one hand, a small number of iterations may result in a large difference compared with the <sup>fi</sup>nal solution and the local optimal solution. On the other hand, a large number of iterations may result in a small improvement compared with the <sup>fi</sup>nal solution and the local optimal solution. The key point of these two problems is cost and performance always run in opposite directions. In Case 2, we design an intelligent mechanism that can effectively balance cost and performance to minimize the number of iterations required for our system.

Our mechanism is based on [4] suggestion that there is a point after which the cost of extending a given run exceeds the performance obtained from the increase in the cumulative probability of success. According to their suggestion, we must de<sup>fi</sup>ne two important curves, one for the increasing cost curve, and one for the decreasing performance curve. In Case 2, the termination criterion is ful<sup>fi</sup>lled if there is an iteration number n such that the cost curve is larger than the performance curve.

We de<sup>fi</sup>ne the cost curve as follows: this curve will gradually ascend if the improvement value is less than the average value of the improvement history progress. If this situation is met, we assume the <sup>fi</sup>nal solution would be better when we continue to run PLSA. That is, we give more iteration to perform PLSA that may result in better performance if this situation is met. According to this de<sup>fi</sup>nition, we use the following equation to de<sup>fi</sup>ne the cost curve, where $\overline { { I M P _ { n - 1 } } }$ is the average value of the improvement history progress.

$$
N I I _ {n} = \left\{ \begin{array}{l l} N I I _ {n - 1} + 1 & i f (I M P _ {n} <   \overline {{I M P _ {n - 1}}}) \\ N I I _ {n - 1} & o t h e r w i s e \end{array} \right.\tag{9}
$$

We then discuss the performance curve as follows. According to the above discussion, the time complexity of PLSA is $O ( M \times N \times L )$ Clearly, the required number of iterations for PLSA is closely related to the size of $L ;$ thus, we set the size of L as the main parameter of the performance curve.

Next, we apply the concepts of the improvement history progress and the variation history progress to de<sup>fi</sup>ne the performance curve. If the improvement history progress is much less, we suppose the <sup>fi</sup>nal solution is close to the local optimal solution. Similarly, if the variation history progress is much less, we suppose the <sup>fi</sup>nal solution is close to a stable stage. The performance curve will gradually descend if the above two situations are met. According to this de<sup>fi</sup>nition, we use the following equation to de<sup>fi</sup>ne the performance curve.

$$
M A I _ {n} = \left\{ \begin{array}{c l} \left[ I M P _ {n} / \overline {{I M P _ {n - 1}}} \times L \times s (I M P _ {n}) / \overline {{s (I M P _ {n - 1})}} \right] & i f (I M P _ {n} > \varepsilon) \\ 0 & o t h e r w i s e \end{array} \right.\tag{10}
$$

where $s ( I M P _ { n } )$ is the standard deviation of al $I M P _ { \varphi } , \ 1 { \leq } \varphi { \leq } n ;$ and $\overline { { s ( I M P _ { n - 1 } ) } }$ is the average value of all $s ( I M P _ { \gamma } ) , 1 \leq \gamma \leq n - 1$

<sup>Þ</sup>According to the de<sup>fi</sup>nition in Eq. (10), the performance curve is dynamically determined based on the ratio of improvement history progress $( I M P _ { n } / \overline { { I M P _ { n - 1 } } } )$ and the ratio of variation history progress $( s ( I M P _ { n } ) / { \overline { { s ( I M P _ { n - 1 } ) } } } )$ . If either $I M P _ { n } / \overline { { I M P _ { n - 1 } } }$ or $s ( I M P _ { n } ) / \overline { { s ( I M P _ { n - 1 } ) } }$ is <sup>ð Þ ð Þ ð Þ ð Þ</sup>less, we assume there is no signi<sup>fi</sup>cant improvement or variation progress in the log-likelihood function.

Finally, according to the de<sup>fi</sup>nition of cost and performance curves, we de<sup>fi</sup>ne the termination criterion of Case 2 as follows.

$$
N I I _ {n} > M A I _ {n}\tag{11}
$$

## 3.2. The procedure of “generating candidate term”

In this procedure, we apply the TSG graph to generate all candidate terms. In our de<sup>fi</sup>nition, the vertices denote the candidate terms, the edges denote any two candidate terms with a semantic relation, and the edge weights are used to measure the similarity degree between two candidate terms.

On the one hand, to construct the vertices and edges of the graph, we apply the BFS algorithm and the concept of the inverse link to build the graph without the edge weights. On the other hand, to calculate the edge weights of the graph, we transform the probability parameters of our system into the edge weights by using the average Euclidean distance metric. Let us de<sup>fi</sup>ne the graph in detail.

In the TSG(V,E,W) graph based on a given term $t _ { i } ,$ V is a set of vertices, each of which corresponds to a candidate term $S T _ { t i \cdot }$ E is a set of directed edges, an edge $\left( t _ { i } , S T _ { t i } \right)$ indicates these two terms $t _ { i }$ and $S T _ { t i }$ exist in a semantic relation and $S T _ { t i }$ is suggested from $t _ { i \cdot }$ W is a set of weight vectors, each of which uses to measure the similarity degree between t and $S T _ { t i } .$ Based on the de<sup>fi</sup>nition of NISO (National Information Standards Organization) [31], we give a formal de<sup>fi</sup>nition for the semantic relation as follows.

![](/api/attachments/992SDHGD/fulltext/images/105ba3486750fffdca2a354bba4d899fc64f29429e95e95714d1b603bc6003ff.jpg)  
Fig. 3. A partial TSG graph for t is “peer to peer”.

## De<sup>fi</sup>nition. Semantic relation

In the TSG graph, we de<sup>fi</sup>ne the directed edge $( t _ { i } , S T _ { t i } )$ as existing in a semantic relation if and only $\mathrm { i f } t _ { i }$ and $S T _ { t i }$ must satisfy at least one of the following relations: equivalence, hierarchy, and association [31]. If $t _ { i }$ and $S T _ { t i }$ are expressing the same concept, these two terms exist in an equivalence relation. If there is a parent–child relation between $t _ { i }$ and $S T _ { t i }$ via an intermediate term, these two terms exist in a hierarchy relation. If there is an association relation between t and $S T _ { t i }$ via a series of intermediate terms, these two terms exist in an association relation.

For example, in Fig. 3, “peer to peer” and “p2p” exist in an equivalence relation, whose directed edge is (“peer to peer”, “p2p”). For an example of hierarchy relation, “peer to peer” and “bittorrent” exist in a parent–child relation, whose directed edge is (“peer to peer”, “bittorrent”), via an intermediate term $\ " { \mathsf { p } } 2 \mathsf { p } ^ { \prime \prime }$ . “peer to peer” and “isohunt.com” exist in an association relation, whose directed edge is (“peer to peer”, “isohunt.com”), via a series of intermediate terms “p2p”, “bittorrent”.

For each equivalence relation, we apply a well-known IR concept, called the inverse link, to construct the directed edge $( t _ { i } , S T _ { t i } ) .$ . That is, if $t _ { i }$ and $S T _ { t i }$ link to an important Web page that is presented in the term-document matrix, we can apply the concept of inverse link to specify these two terms. For example, if two queries, “peer to peer” and $\ " { \mathsf { p } } \ / { 2 } { \mathsf { p } } ^ { \prime \prime }$ , link to an important Web page “en.wikipedia.org/wiki/ peer to peer”, then we can simply apply the inverse link of this Web page to construct the directed edge (“peer to peer”, “p2p”).

For each hierarchy or association relation, we apply the BFS algorithm to construct the directed edge $\left( t _ { i } , S T _ { t i } \right)$ . The pseudo code of the algorithm is listed in the following (Fig. 4).

In the following discussion, we will use an example (Example 1) to illustrate how to build semantic relations from the above algorithm.

For each edge weight DS(t ,ST ), in line 14 of Algorithm BFS, we apply an Average Euclidean Distance (AED) metric, a classical approach is used to measure the similarity degree between two given vectors, to transform the probability parameters of our system into edge weights. The edge weights are not only used to determine the similarity degree between the input search term and the candidate terms, but also used to discard the candidate terms with a relatively small edge weight. The transformation formula is de<sup>fi</sup>ned as follows.

```c
Algorithm BFS (t_i, Depth, MaxDepth, td(t_i,d_j))
{
    Input: t_i is a seed term, Depth is the current depth of TSG, MaxDepth is the maximum allowable depth of TSG, and td(t_i,d_j) is the term-document matrix.
    Output: TSG is a semantic analysis graph, where each vertex is ST_i, each directed edge is (t_i,ST_i), and each edge weight is DS(t_i,ST_i).
    If (Depth≥MaxDepth)
    Return (TSG):
    Else {
    <WPs> = Identify all important Web pages of t_i based on the content of the matrix td(t_i,d_j):
    For each <WPs> as WP {
    <ST_i s> = Use the inverse links of WP, which are defined in td(t_i,d_j), to specify all relevant candidate terms;
    For each <ST_i s> as ST_i {
    TSG(V) += ST_i;
    TSG(E) += (t_i,ST_i);
    TSG(W) += DS(t_i,ST_i) (see equation (12));
    BFS (ST_i, Depth+1, MaxDepth, td(t_i,d_j));
    } End of For each
    } End of For each
    } End of Else
} End of Algorithm
```

$$
D S (t _ {i}, S T _ {t i}) = 1 - \sqrt {\sum_ {j = 1} ^ {N} \left(P \left(t _ {i} , d _ {j}\right) - P \left(S T _ {t i} , d _ {j}\right)\right) ^ {2}} / N\tag{12}
$$

where $P ( \theta , d _ { j } ) , \theta \in \{ t _ { i } , S T _ { t i } \}$ , is the latent probability of term θ in document $d _ { j }$ derived from the procedure of “Generating Parameter”. To use the AED metric as a similarity measure, rather than a distance measure, we de<sup>fi</sup>ne a similarity degree metric, called Degree of Similarity (DS), by subtracting AED from 1.<sup>1</sup> Finally, we use an example to illustrate how to suggest relevant terms to help readers easily understand the whole process of our term suggestion method.

Example 1. The process of term suggestion.

$$
T D = \begin{array}{c} t _ {1} \\ t _ {2} \\ t _ {3} \\ t _ {4} \\ t _ {5} \\ t _ {6} \end{array} \left[ \begin{array}{l l l} 0. 6 7 & 0. 0 7 & 0. 0 8 \\ 0. 6 1 & 0. 4 5 & 0. 0 8 \\ 0. 5 6 & 0. 0 7 & 0. 0 1 \\ 0. 2 5 & 0. 0 8 & 0. 0 7 \\ 0. 0 4 & 0. 6 1 & 0. 5 0 \\ 0. 0 1 & 0. 0 7 & 1. 0 0 \end{array} \right] \tag {a}
$$

In this example, we assume $t _ { 1 } = " \mathrm { p e e r }$ to peer”, $t _ { 2 } = { } ^ { \circ } \mathsf { p } 2 \mathsf { p } ^ { \prime \prime } , t _ { 3 } =$ “peer to peer sites”, $t _ { 4 } =$ “best peer to $\mathbf { p e r } ^ { \prime \prime } , t _ { 5 } = \cdot$ “bittorrent”, $t _ { 6 } =$ “isohunt.com”, $d _ { 1 } \ =$ “en.wikipedia.org/wiki/peer to peer”, $d _ { 2 } \ =$ “www.bittorrent.com”, $d _ { 3 } = \mathrm { " i s o h u n t . c o m " }$ . To generate the termdocument matrix, we use a metasearch technology [20] to calculate the weight of the term-document matrix for term $t _ { i }$ in Web page $d _ { j } .$ Our metasearch technology is based on a well-known IR formula, called Mean Reciprocal Rank (MRR) [2], as shown in the following equation.

$$
t d \left(t _ {i}, d _ {j}\right) = 1 / | S E | \sum_ {e = 1} ^ {| S E |} 1 / r a n k \left(t _ {i}, d _ {j}\right) _ {e}\tag{13}
$$

where |SE| is the number of search engines used in our metasearch technology; rank $( t _ { i } , d _ { j } ) _ { e }$ is the relative order of Web page $d _ { j }$ returned from search engine e when the search term is $t _ { i \cdot }$ We assume the relative orders of document $d _ { 1 }$ within three different search engines are 1, 2, and $^ { 2 , }$ respectively when the search term is $t _ { 1 } .$ Based on Eq. (13), we calculate the weight of $t d ( t _ { 1 } , d _ { 1 } )$ equals 0.67 $( ( 1 / 1 + 1 / 2 + 1 / 2 ) / 3 )$

$$
\text { ProbParameters } = \begin{array}{c} t _ {1} \\ t _ {2} \\ t _ {3} \\ t _ {4} \\ t _ {5} \\ t _ {6} \end{array} \left[ \begin{array}{c c c} d _ {1} & d _ {2} & d _ {3} \\ 0. 9 2 & 0. 5 0 & 0. 5 7 \\ 0. 9 0 & 0. 5 5 & 0. 5 4 \\ 0. 3 0 & 0. 1 4 & 0. 1 1 \\ 0. 3 5 & 0. 1 7 & 0. 1 4 \\ 0. 6 7 & 0. 7 7 & 0. 6 3 \\ 0. 7 1 & 0. 6 5 & 0. 9 0 \end{array} \right]
$$

Fig. 5. A term-document matrix and the <sup>fi</sup>nal results of the probability parameters.

Similarly, we calculate the weights of term-document matrix based on the MRR formula, as shown in Fig. 5(a).

To construct the vertices and edges of the TSG graph, we apply the BFS algorithm and the concept of the inverse link to build the graph without the edge weights. In the <sup>fi</sup>rst BFS call, in line $^ { 8 , }$ for the seed term $t _ { 1 } ,$ , we can <sup>fi</sup>nd an important Web page $d _ { 1 }$ based on the content of the matrix TD. Then, in line 10, we can <sup>fi</sup>nd the candidate terms $t _ { 2 } ,$ $t _ { 3 } ,$ and $t _ { 4 }$ by the inverse links of $d _ { 1 }$ . Finally, for the equivalence relation, the directed edges based on $t _ { 1 }$ are $( t _ { 1 } , t _ { 2 } ) , ( t _ { 1 } , t _ { 3 } ) , ( t _ { 1 } , t _ { 4 } )$

In the second BFS call, in line 8, for the candidate term $t _ { 2 } ,$ we can <sup>fi</sup>nd an additional Web page $d _ { 2 }$ based on the content of the matrix TD. Then, in line 10, we can <sup>fi</sup>nd an additional candidate term t<sub>5</sub> by the inverse link o $\cdot _ { d _ { 2 } }$ , and the hierarchy relation is t $\mathrm { i } \left( { \vec { d } } _ { 1 } \right) t _ { 2 } \left( { \vec { d } } _ { 2 } \right) t _ { 5 } , \mathrm { w h e r e } \left( { \vec { d } } _ { j } \right)$ denotes an equivalence relation between two terms by the inverse link of $d _ { j } .$ Finally, for the hierarchy relation, the directed edge based on $t _ { 1 }$ is $( t _ { 1 } , t _ { 5 } )$

In the third BFS call, in line $^ { 8 , }$ for the candidate term $t _ { 5 } ,$ , we can <sup>fi</sup>nd an additional Web page $d _ { 3 } ;$ then, in line 10, we can <sup>fi</sup>nd an additional candidate term $t _ { 6 } ,$ and the association relation is $t _ { 1 } \left( { \vec { d } } _ { 1 } \right) t _ { 2 } \left( { \vec { d } } _ { 2 } \right) t _ { 5 }$ ${ \bigg ( } { \vec { d } } _ { 3 } { \bigg ) } t _ { 6 } .$ Finally, for the association relation, the directed edge based on $t _ { 1 } \mathrm { i } s \left( t _ { 1 } , t _ { 6 } \right) .$

We then apply the AED metric to transform the probability parameters into the edge weights of the TSG graph. Fig. 5(b) is an example of the <sup>fi</sup>nal results of the probability parameters derived from the procedure of “Generating Parameter”.

We apply the AED metric to transform the probability parameters into the edge weights of the TSG graph. For example, the edge weight of the directed edge $( t _ { 1 } , t _ { 2 } )$ is 0.9962. In this graph, we discard the candidate terms, $t _ { 3 }$ and $t _ { 4 } ,$ since the edge weights of $\left( t _ { 1 } , t _ { 3 } \right)$ and $( t _ { 1 } , t _ { 4 } )$ are calculated with a relatively small edge weight (0.2744 and 0.3813). Finally, the suggested terms are $t _ { 2 } ( \mathsf { p } 2 \mathsf { p } ) , t _ { 5 }$ (bittorrent), and $t _ { 6 }$ (isohunt.- com) when the search term is $t _ { 1 }$ (peer to peer).

## 4. Preliminary experiment results

In this section, we <sup>fi</sup>rst conduct an experiment to verify the performance of our system and other systems. To verify whether our intelligent mechanism is a performance-effective solution, we then perform a simulation experiment to compare the performance and computational cost of different simulation scenarios.

## 4.1. Experiment with different online systems

In this experiment, we pay attention to how to rate the performance of different systems compared with Highlight, Credo, Carrot2, CatS, Vivisimo, GPS, GA, YSM, SnakeT, and LI. All the systems except LI are described in Section 2.1.

In this experiment, we randomly selected 1000 query terms from Dogpile [18], which people were using on the Internet. The 1000 random query terms are listed in [10].

To compare the performance of different systems for our simulation program, we use a Measure of Semantic Relatedness (MSR) statistical technique, called Normalized Similarity Score (NSS), to automatically extract term similarity information from the large corpus of data [25]. NSS is a popular MSR that can handle all the corpus types we were considering in our research. Other MSRs, for example LSA [23], ICAN [24], and GLSA [28], simply cannot handle large Webbased corpora [25].

NSS calculates the probability of the co-occurrence of two terms to ascertain their semantic similarity value. This probability varies greatly from one corpus to another; thus, the output of NSS trained on different corpora also varies greatly. There are many corpora commonly used to train NSS and each produces different semantic similarity values. Let us brie<sup>fl</sup>y discuss the concept of NSS and the training corpora used in our research

## 4.1.1. The concept of NSS

Recently, an automatic MSR technique has been proposed using the search results counts from the Google search engine, i.e. the Normalized Google Distance (NGD) technique [7]. The NGD can detect the semantic relationship among terms using the Google search engine. Based on Google's blog post, the Google search engine indexed 1 trillion pages [1]. Thus, the WWW is the largest corpus that can be used to analyze the semantic relationships among terms. The main idea of the NGD is to understand the relationships between any two terms according to the number of search results, i.e., the number of return pages. The researchers [7] provided a statistical index based on Google page counts, showing the logical distance of a pair of terms called NGD, as shown in the following equation.

$$
N G D _ {C} \left(t _ {i}, S T _ {t i}\right) = \frac {\max \left\{\log f \left(t _ {i}\right) , \log f \left(S T _ {t i}\right) \right\} - \log f \left(t _ {i} , S T _ {t i}\right)}{\log C S - \min \left\{\log f \left(t _ {i}\right) , \log f \left(S T _ {t i}\right) \right\}}\tag{14}
$$

where CS is the total number of pages in the corpus $C ; f ( t _ { i } )$ and f(ST<sub>ti</sub>) are the number of pages for terms $t _ { i }$ and $S T _ { t i } ,$ , respectively; and $f ( t _ { i } , S T _ { t i } )$ is the number of pages on which both t and $S T _ { t i }$ occur. When the value gets lower, it implies there is a closer relation between two terms. NGD provides a relative measure of how far two terms are semantically, which is very suitable for the comparison of different systems.

To use NGD as a semantic similarity measure, rather than a measure of distance, we convert NGD scores into similarity scores by subtracting NGD from 1 (1 being the maximum NGD score). From this point forth, we will refer to the similarity score based on the NGD formula as the Normalized Similarity Score (NSS), as shown in the following equation.

$$
\begin{array}{l} N S S _ {C} (t _ {i}, S T _ {t i}) = 1 - D i s t a n c e _ {C} (t _ {i}, S T _ {t i}) \\ \text { where } D i s t a n c e _ {C} (t _ {i}, S T _ {t i}) = \left\{ \begin{array}{c c} 1, & \text { if } (f (t _ {i}) = 0 | | f (S T _ {t i}) = 0 | | f (t _ {i}, S T _ {t i}) = 0) \\ N G D _ {C} (t _ {i}, S T _ {t i}), & \text { Otherwise } \end{array} \right. \end{array}\tag{15}
$$

## 4.1.2. The training corpora

In this experiment, we use several well-known Web-based corpora, including WWW, new articles, encyclopedia, and books, to evaluate the performance of the above-mentioned ten systems.

## • WWW corpus (Google)

This corpus is an extremely large collection of text (the World Wide Web), and is a popular choice for a training corpus. One major advantage of this corpus is NSS runs extremely fast on it. Counting the number of hits returned by a given query takes an inconsequential length of time.

## • News articles corpus (New York Times)

The New York Times is a news source that we chose to study as a corpus because of their large collection of online articles. To use this corpus, we count the hits returned by the Google search for the terms after restricting our results to “site: nytimes.com”.

## • Encyclopedia corpus (Wikipedia)

Wikipedia is the largest free-content encyclopedia on the Internet written by hundreds and thousands of contributors. We choose to study this corpus because it represents a great wealth of human knowledge. We access this corpus in the same way we access New York Times, by restricting Google searches to “site: wikipedia.org”.

![](/api/attachments/992SDHGD/fulltext/images/f19aa7e9345eda2815304cbb178decf4ebeb007e7c7bc8f215f113f063f5ddff.jpg)  
Fig. 6. The result of Mean(NSS ) when the corpus G is used to measure.

## • Books corpus (Gutenberg)

Gutenberg is an online collection of over 30,000 free books produced by tens of thousands of volunteers. This corpus represents one of the largest online collections of books available. We use this corpus in the same way we use New York Times and Wikipedia, by restricting our searches on Google to “site: gutenberg.org”.

![](/api/attachments/992SDHGD/fulltext/images/098200fa561b88e897bb36429615ff3263cbdcbb5c4e54dd0862d04b6f01c87c.jpg)  
Fig. 7. The average Mean(NSS ) scores, C∈{G, Gnytimes, Gwikipedia, Ggutenberg}.

![](/api/attachments/992SDHGD/fulltext/images/4c87cd72d1e63e912b3ff07ee28f931f45667abac2eb4e7bd94c0695ec7d2d33.jpg)  
Number of Runs

![](/api/attachments/992SDHGD/fulltext/images/00d0df7cdd3151daa631bdd20ec5345c746482c14cbc009e394cd23ca240f000.jpg)  
Number of Runs  
Fig. 8. Performance and cost metrics for 1000 simulation runs.

All corpora that end with G use the Google search engine to search the entire Web, Gnytimes searches only nytimes.com on Google, Gwikipedia searches only wikipedia.org on Google, Ggutenberg searches only gutenberg.org on Google.

We then use the following equation to measure the average similarity degree between t and its all suggested terms, where RT(t ) is all suggested terms returned from $t _ { i \cdot }$ Interested readers can calculate the score of Mean(NSS ) in our simulation system (http://cayley.sytes. net/experiment\_nss/).

$$
\text { Mean } (N S S _ {C}) = 1 / | R T (t _ {i}) | \sum_ {S T _ {t i} = 1} ^ {| R T (t _ {i}) |} N S S _ {C} (t _ {i}, S T _ {t i})\tag{16}
$$

Fig. 6 means the average similarity degree between t and all suggested terms when the number of $t _ { i }$ equals 1000 and the corpus G (Google) is used to measure. In this <sup>fi</sup>gure, the x-axis denotes the number of $t _ { i \cdot }$ The dot in this <sup>fi</sup>gure is the average value over 50 queries. According to this <sup>fi</sup>gure, we observe the average similarity degree obtained from LI is the highest.

For comparison purposes, we then average all $M e a n ( N S S _ { G } )$ scores for each evaluated system, as shown in Fig. 7. The average Mean(NSS ) score for LI is 0.79214. Moreover in Fig. 7 we extend this analysis to other analyses $M e a n ( N S S _ { G n y t i m e s } )$ , Mean $. N S S _ { G w i k i p e d i a } )$ , and $M e a n ( N S S _ { G g u t e n b e r g } ) .$ No matter which corpora are used to measure, the average Mean(NSS ) score for LI is the highest, implying the performance of our system is the best.

In this experiment, we found the performance of NSS on the Gutenberg corpus is the worst because it has the smallest corpus size. When we compare it with other corpora, it has a higher chance of not returning any hits from Google. That is, the parameters of $N S S _ { C }$ including $f ( t _ { i } ) , f ( S T _ { t i } )$ , and $f ( t _ { i } , S T _ { t i } )$ , have a high chance of being 0. This implies NSS has a high chance of being 0. On the contrary, NSS performed best on the Google corpus because it has the largest corpus size. Our results show different corpora greatly affect the performance of NSS.

## 4.2. Experiment on a performance-effective solution

In this experiment, we veri<sup>fi</sup>ed the <sup>fi</sup>nal solution derived from our system could yield a performance-effective solution. According to the description of Section 3.1, the termination criteria have the following two cases: (1) it converges to the local optimal solution or (2) the maximum allowable number of iterations is reached. Readers can simulate this experiment at http://cayley.sytes.net/li\_new/term\_li.php.

To verify whether the second case is a performance-effective solution, we simulated 1000 times the Performance–Cost Ratio (PCR) of the simulation results calculated by the second case (“LI”) with some prede<sup>fi</sup>ned numbers of iterations. The prede<sup>fi</sup>ned number of iterations is based on the local optimal solution that can classify the number of iterations required to run into the following situations: $" L O "$ (local optimal solution), $" L O - 2 0 "$ (LO minus 20), and ${ } ^ { \mathfrak { a } } L O$ $- 4 0 "$ (LO minus 40).

In our PCR metric we <sup>fi</sup>rst needed to de<sup>fi</sup>ne a performance metric, Successful Percentage (SP), between the real $L L _ { n }$ achieved by the #ITEth iteration $( L L _ { \# I I E } ( t _ { i } , d _ { j } ) )$ and the local optimal $L L _ { n } \left( L L _ { L O } ( t _ { i } , d _ { j } ) \right)$ ) as follows:

$$
S P _ {I T E} = L L _ {I T E} \left(t _ {i}, d _ {j}\right) / L L _ {L O} \left(t _ {i}, d _ {j}\right)\tag{17}
$$

where # $\mathsf { \Pi } ^ { \mathsf { t } } \Pi I I E { = } \{ { ^ { \mathsf { w } } L I ^ { \mathsf { w } } , ^ { \mathsf { w } } L O ^ { \mathsf { w } } , ^ { \mathsf { w } } L O - 2 0 ^ { \mathsf { w } } , ^ { \mathsf { w } } L O - 4 0 ^ { \mathsf { n } } } \}$

Fig. 8(a) is the SP distribution over 1000 simulation runs. The average SP (MSP) values for different #ITEs are 1 (“LO”), 0.998333 (“LO $- 2 0 " )$ , 0.998146 (“LI”), and 0.639456 $( { } ^ { \mathfrak { u } } L O - 4 0 ^ { \mathfrak { v } } )$ respectively.

Fig. 8(b) shows the cost metric, Number of Iterations (NI), required to run for different #ITEs. The average number of iterations (MNI) for different #ITEs are 58.435196 (“LO”), 38.435196 (“LO 20”), 31.369284 (“LI”), and 18.435196 $( { } ^ { \mathfrak { u } } L O - 4 0 ^ { \mathfrak { v } } )$ respectively.

For any two cases, we de<sup>fi</sup>ne PCR between #ITE1 and #ITE2 by dividing the increased successful percentage by the increased percentage of the number of iterations as follows:

$$
P C R _ {I T E 1, I T E 2} = \frac {M S P _ {I T E 1} - M S P _ {I T E 2}}{\left(M N I _ {I T E 1} - M N I _ {I T E 2}\right) / M N I _ {I T E 2}}\tag{18}
$$

Using $\# I T E 2 = \ " L O - 4 0 "$ as a benchmark, the PCR scores for different #ITEs, $" L O ' ,$ $" L O - 2 0 "$ , and $" L ^ { \prime \prime }$ are 0.166167, 0.330798, and 0.511248, respectively. We found the case $0 \mathbf { f } \ { } ^ { \ast } \# I T E 1 = L I ^ { \ast }$ signi<sup>fi</sup>cantly outperforms other #ITEs by at least 18.045% (0.511248–0.330798). The PCR scores drop rapidly beyond the case $\ ^ { \mathfrak { u } } \# I T E { 1 } = L I ^ { \mathfrak { n } }$ . In summary, we conclude our system can yield a performance-effective solution in a comparatively short time.

## 5. Conclusions and future work

This paper introduced a novel approach for the research of term suggestions. Our approach is based on two semantic analysis methods, the probabilistic analysis model and semantic analysis graph, to design a term suggestion system that can effectively deal with the problems of synonymy and polysemy. According to the results of the computer simulation, we concluded using multiple semantic analysis methods to suggest terms can give signi<sup>fi</sup>cant performance gains. The interested readers can verify our preliminary system at http://cayley.sytes.net/ li\_new.

In the current system, the initialization values of the probability parameters are based on random assignments. For a given initialization, the result increases with each iteration of PLSA until the local optimal solution is reached, so the quality of the solution greatly depends on the initialization values. In the future, we plan to use other semantic analysis methods as the initialization values. Rather than trying to predict the best initialization values of PLSA from a set of data, we will focus on how to <sup>fi</sup>nd a good way to initialize PLSA.

## Acknowledgements

We would like to thank anonymous reviewers of the paper for their constructive comments which help us to improve the paper in several ways. This work was supported in part by National Science Council, Taiwan under Grant NSC 100-2410-H-259-010- MY2.

## References

[1] J. Alpert, N. Hajaj, Off<sup>fi</sup>cial Google Blog: We Knew the Web was Big, 2008 http:// tinyurl.com/5blvgm (accessed date November 11 2011).

[2] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, Addison Wesley Press, 1999.

[3] C. Carpineto, G. Romano, Exploiting the potential of concept lattices for information retrieval with CREDO, Journal of Universal Computer Science 10 (8) (2004) 985–1013.

[4] L.C. Chen, C.J. Luh, C. Jou, Generating page clippings from web search results using a dynamically terminated genetic algorithm, Information Systems 30 (4) (2005) 299–316.

[5] Y. Chen, F.S. Tsai, K.L. Chan, Machine learning techniques for business blog search and mining, Expert Systems with Applications 35 (3) (2008) 581–590.

[6] Y. Chen, G.-R. Xue, Y. Yu, Advertising keyword suggestion based on concept hierarchy, Proceedings of the International Conference on Web Search and Web Data Mining, 2008, pp. 251–260.

[7] R.L. Cilibrasi, P.M.B. Vit´anyi, The Google similarity distance, IEEE Transaction on Knowledge and Data Engineering 19 (3) (2007) 370–383.

[8] D. Cohn, T. Hofmann, The missing link — a probabilistic model of document content and hypertext connectivity, Advances in Neural Information Processing Systems 13 (2001) 430–436.

[9] A.P. Dempster, N.M. Laird, D.B. Rubin, Maximum likelihood from incomplete data using the EM algorithm, Journal of the Royal Statistical Society B 39 (1977) 1–38.

[10] Dogpile, The Project of Term Suggestion: Listing of Testing Queries, 2008 http:// cayley.sytes.net/li/listing\_all\_testing\_keywords.php (accessed date November 11 2011).

[11] P. Ferragina, A. Guli, A personalized search engine based on web-snippet hierarchical clustering, Software: Practice and Experience 38 (1) (2008) 189–225.

[12] R. Fishkin, J. Pollard, Search Engine Ranking Factors V2, 2007 http://www. seomoz,org/article/search-ranking-factors (accessed date November 11 2011).

[13] E.D. Giacomo, W. Didimo, L. Grilli, G. Liotta, Graph visualization techniques for web clustering engines, IEEE Transactions on Visualization and Computer Graphics 13 (2) (2007) 294–304.

[14] S. Gibson, A. Wills, B. Ninness, Maximum-likelihood parameter estimation of bilinear systems, IEEE Transactions on Automatic Control 50 (10) (2005) 1581-1596.

[15] Google, Google AdWords: Keyword Tool, 2008 http://tinyurl.com/qkfuh (accessed date November 11 2011).

[16] T. Hofmann, Unsupervised learning by probabilistic latent semantic analysis, Machine Learning 42 (1) (2001) 177–196.

[17] T. Hofmann, Latent semantic models for collaborative <sup>fi</sup>ltering, ACM Transactions on Information Systems 22 (1) (2004) 89–115.

[18] InfoSpace, Dogpile SearchSpy, 2008 http://tinyurl.com/5sglhg (accessed date November 11 2011).

[19] M. Inoue, The remarkable search topic-<sup>fi</sup>nding task to share success stories of cross-language information retrieval, Proceedings of the Fifth Workshop on Important Unresolved Matters, 2005, pp. 61–64.

[20] B.J. Jansen, A. Spink, S. Koshman, Web searcher interaction with the dogpile.com metasearch engine, Journal of the American Society for Information Science and Technology 58 (8) (2007) 744–755.

[21] A. Joshi, R. Motwani, Keyword generation for search engine advertising, Proceedings of the Sixth IEEE International Conference on Data Mining, 2006, pp. 490–496.

[22] M.d. Kunder, The Size of the World Wide Web, 2008 http://worldwidewebsize. com/ (accessed date November 11 2011).

[23] T.K. Landauer, S.T. Dumais, A solution to plato's problem: the latent semantic analysis theory of acquisition, induction, and representation of knowledge, Psychological Review 104 (2) (1997) 211–240.

[24] B. Lemaire, G. Denhiere, Incremental construction of an associative network from a corpus, Proceedings of the 26th Annual Meeting of the Cognitive Science Socie ty, 2004, pp. 825–830

[25] R. Lindsey, V.D. Veksler, A. Grintsvayg, W.D. Gray, Be wary of what your computer reads: the effects of corpus selection on measuring semantic relatedness, Proceedings of the 8th International Conference on Cognitive Modeling, 2007.

[26] D.-C. Lyu, R.-Y. Lyu, Y.-C. Chiang, C.-N. Hsu, Cross-lingual audio-to-text alignment for multimedia content management, Decision Support Systems 45 (3) (2008) 554–566.

[27] J. Malinowski, T. Weitzel, T. Keim, Decision support for team staf<sup>fi</sup>ng: an automated relational recommendation approach, Decision Support Systems 45 (3) (2008) 429–447.

[28] I. Matveeva, G.-A. Levow, A. Farahat, C. Royer, Term representation with generalized latent semantic analysis, Proceedings of the International Conference on Recent Advances in Natural Language Processing (RANLP-05), 2005.

[29] K. Metaxoglou, A. Smith, Maximum likelihood estimation of VARMA models using a stage-space EM algorithm, Journal of Time Series Analysis 28 (5) (2007) 666–685.

[30] V. Nguyen, S. Gächter, A. Martinelli, N. Tomatis, R. Siegwart, A comparison of line extraction algorithms using 2D range data for indoor mobile robotics, Autonomous Robots 23 (2) (2007) 97–111.

[31] NISO, ANSI/NISO Z39.19-2005 Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies, NISO Press, 2005.

[32] S. Osinski, D. Weiss, A concept-driven algorithm for clustering search results, IEEE Intelligent Systems 20 (3) (2005) 48–54.

[33] F. Pernkopf, D. Bouchaffra, Genetic-based EM algorithm for learning Gaussian mixture models, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (8) (2005) 1344–1348

[34] M. Radovanović, M. Ivanović, CatS: a classi<sup>fi</sup>cation-powered meta-search engine, Advances in Web Intelligence and Data Mining 23 (1) (2006) 191–200.

[35] N.L. Ranks, Keyword Proximity Analyzer, 2008 http://www.ranks.nl/tools/ proximity,html (accessed date November 11 2011).

[36] E.S. Ristad, P.N. Yianilos, Learning string-edit distance, IEEE Transactions on Pattern Analysis and Machine Intelligence 20 (5) (1998) 522–532.

[37] A. Segev, M. Leshno, M. Zviran, Context recognition using internet as a knowledge base, Journal of Intelligent Information Systems 29 (3) (2007) 305–327.

[38] X.-B. Wen, H. Zhang, Z.-T. Jiang, Multiscale unsupervised segmentation of SAR imagery using the genetic algorithm, Sensors 8 (3) (2008) 1704–1711.

[39] Y.-F. Wu, X. Chen, Extracting features from web search returned hits for hierarchical classi<sup>fi</sup>cation, Proceedings of the International Conference on Information and Knowledge Engineering, 2003, pp. 103–108.

[40] K. Xu, S.S. Liao, J. Li, Y. Song, Mining comparative opinions from customer reviews for competitive intelligence, Decision Support Systems 50 (4) (2011) 743–754.

[41] Yahoo, Start Advertising with Yahoo! Search Marketing, 2008 http://tinyurl.com/ 3fjmnja (accessed date November 11 2011).

[42] Q. Zhang, S.A. Goldman, EM-DD: an improved multiple-instance learning technique, Neural Information Processing Systems 14 (2001) 1073–1080.

[43] B. Zhou, J. Pei, Answering aggregate keyword queries on relational databases using minimal group-bys, Proceedings of the 12th International Conference on Extending Database Technology: Advances in Database Technology, 2009, pp. 108–119.

Lin-Chih Chen is an associate professor in the Department of Information Management at National Dong Hwa University, Taiwan. His research interests include Web Intelligent and Web Technology. He is also the leader of Cayley group. He develops many Web Intelligent systems include Cayley search engine, On-The-Fly Document Clustering, Cayley digital content system, iClubs community, language agent, LI keyword sug gestion system, WSC clustering system, Cayley Scholar.
