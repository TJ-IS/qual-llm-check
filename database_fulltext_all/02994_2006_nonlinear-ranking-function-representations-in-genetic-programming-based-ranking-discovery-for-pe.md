---
otero_id: 2994
otero_key: "922S6NZT"
title: "Nonlinear ranking function representations in genetic programming-based ranking discovery for personalized search"
authors: "Weiguo Fan; Praveen Pathak; Linda Wallace"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.11.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Nonlinear ranking function representations in genetic programming-based ranking discovery for personalized search

Weiguo Fan <sup>a,\*</sup>, Praveen Pathak <sup>b</sup>, Linda Wallace <sup>c</sup>

<sup>a</sup> Virginia Polytechnic Institute and State University, 3007 Pamplin Hall, Blacksburg, VA 24061, United States <sup>b</sup> University of Florida, United States

<sup>c</sup> Virginia Polytechnic Institute and State University, United States

Received 14 October 2004; received in revised form 24 October 2005; accepted 3 November 2005 Available online 7 December 2005

## Abstract

Ranking function is instrumental in affecting the performance of a search engine. Designing and optimizing a search engine’s ranking function remains a daunting task for computer and information scientists. Recently, genetic programming (GP), a machine learning technique based on evolutionary theory, has shown promise in tackling this very difficult problem. Ranking functions discovered by GP have been found to be significantly better than many of the other existing ranking functions. However, current GP implementations for ranking function discovery are all designed utilizing the Vector Space model in which the same term weighting strategy is applied to all terms in a document. This may not be an ideal representation scheme at the individual query level considering the fact that many query terms should play different roles in the final ranking. In this paper, we propose a novel nonlinear ranking function representation scheme and compare this new design to the well-known Vector Space model. We theoretically show that the new representation scheme subsumes the traditional Vector Space model representation scheme as a special case and hence allows for additional flexibility in term weighting. We test the new representation scheme with the GP-based discovery framework in a personalized search (information routing) context using a TREC web corpus. The experimental results show that the new ranking function representation design outperforms the traditional Vector Space model for GP-based rankin function discovery.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Information routing; Information retrieval; Genetic programming; Ranking function

## 1. Introduction

Nowadays, more and more people are using web search engines to find information online to help them make better informed decisions. Major search engines such as Google, Yahoo!, etc., receive millions of search requests per day according to searchenginewatch.com. Although many of the search engines have fast search response times and reasonably good search quality, most of them lack the personalized search capabilities which would allow different people to receive different search results for the same query, depending on their own personal preferences and profiles. This kind of personalized search is highly desirable in the business intelligence arena where people/organizations constantly look for individual-tailored information [12,32].

Prior research on personalized search has focused on the user profiling perspective in which historic feedback information (relevance feedback information or user clickthrough data) is used to infer a user’s real information need [12,32]. The inferred profile is then used for later information routing or personalized search when new unseen documents become available. In this paper, we approach the personalized search task from the user preference modeling perspective. In particular, we look at how to use common information heuristics or cues to model a user’s ranking preference towards information. We will use an advanced machine learning technique called genetic programming (GP) to combine all of the available information heuristics in order to obtain best permissible personalized search results. The remainder of this section provides a brief introduction to the GP technique, explains its application to information retrieval, and outlines the primary goals of this paper.

Genetic algorithms (GAs) [23] and genetic programming [26] are search algorithms based on evolutionary theory. They represent the solution to a problem as an individual (also called a chromosome) in a population pool. They evolve the population of individuals (chromosomes), generation by generation, following the genetic transformation operations – such as reproduction, crossover, and mutation – with the aim of discovering chromosomes with better fitness values. A fitness function is used to assign the fitness value for each individual.

The difference between GAs and GP is the internal representation – or data structure – of the individual chromosome. In GAs, each individual is commonly (though not always) represented by a fixed-length bit string, like (1101110. . .) or a fixed-length sequence of real numbers (1.2, 2.4, 4, . . .). In GP, more complex data structures (e.g., tree, linked list, or stack) are used [27]. Moreover, the length or size of the data structure is not fixed, although it may be constrained within a certain size limit by implementation. GAs are often used to solve difficult optimization problems, while GP is typically used to approximate complex, nonlinear functional relationships [26]. Because of the intrinsic parallel search mechanism and powerful global exploration capability in a high-dimensional space, both GAs and GP have been used to solve a wide range of difficult optimization problems that often have no best known solutions.

Because of these merits, there has been increasing interest in applying GAs and GP to intelligent information retrieval (IR) in recent years [3–12,17,18,24,28, 29,31,41]. The application areas cover a wide range of IR topics such as document indexing; query induction, representation, and optimization; document clustering; and. document matching and ranking.

GP has previously been applied to discover ranking functions for both individual queries (personalized search or information routing tasks) [7,8,10,15,16] and multiple queries (consensus search or ad hoc retrieval tasks) [9,11–13,15]. Given a query (or a set of queries), a ranking function is used by a search engine to rank documents according to their match with the query. Since there is no known best ranking function for a query (or a set of queries), we model this problem as a GP search problem. Candidate ranking functions are represented as individuals in a GP population using a tree structure, and then evolved by GP to discover ranking functions with better fitness values.

So far, previous ranking function discovery efforts have centered on the Vector Space model (VSM), in which all documents and queries are represented as vectors and the same term weighting strategy used in a ranking function is applied to all terms in a document. For example, given a term weighting strategy tf, a ranking function will count all the term frequencies (tf) of all the terms matching a user query and use the sum of scores (also called retrieval status value—RSV) for final ranking. Ranking functions based on the Vector Space model have performed very well in various IR experimental evaluations and TREC (Text Retrieval and Evaluation Conference) competitions [19–22,35,37].

The advantage of the VSM is that it is simple, effective and easy to implement. This, however, does not necessarily mean that it is optimal for all application contexts. The VSM is very good for generic information retrieval (IR) engines such as web search engines or library catalog search systems, as these systems can effectively leverage the simplicity and powerfulness of the VSM to strive for speed and accuracy. However, the VSM may not be ideal for a personalized search (information routing) context where a user is consistently searching for the same information over a long period of time. In the new world of constant information, such a personalized search has become a critical component in the arsenal of the knowledge worker. For example, consider a stock analyst who has to constantly monitor the information about a company (for example Intel) or an industry and come up with recommendations with this new information. The information requirements of this analyst are fairly static – the analyst is interested in any news item that may affect the stock she is covering. In generic information retrieval (also known as ad hoc), a query given to the retrieval system to find documents about <sup>b</sup>intel<sup>Q</sup> might come up with documents about CIA, FBI, Intelligence about Iraq, etc. But the stock analyst is not interested in this type of <sup>b</sup>intel<sup>Q</sup>. The stock analyst is interested in the documents that talk about Intel as a company. Thus, a generic retrieval system is not enough to satisfy the requirements of this analyst. What is needed is a targeted personalized search (or information routing) mechanism which will deliver appropriate documents to this analyst.

From the above example, it is clear that simple linear ranking functions on the basis of VSM may not be enough for personalized search. Therefore, the goal of this paper is to propose and validate an alternative nonlinear ranking function representation scheme for ranking function discovery in a personalized search context. We will also show that the linear VSM ranking representation is a special case of our nonlinear ranking representation.

The remainder of the paper is organized as follows. In Section 2, we briefly review the background information on term weighting and its relationship to ranking function. We also review previous work on the application of genetic programming (GP) to ranking function discovery. In Section 3, we formally describe our nonlinear ranking function representation methodology. Section 4 presents the experimental setup that was used to evaluate the performance of the nonlinear ranking functions and compare them to other ranking functions. We summarize the experimental results in Section 5 and discuss our conclusions in Section 6.

## 2. Background

## 2.1. Term weighting and ranking function

As mentioned earlier, in the VSM, both documents and user queries are represented in vectors. More formally, suppose there are a total of t index terms in a given query, then a given document D and query Q can be represented as follows:

$$
\begin{array}{l} D = \left(w _ {d 1}, w _ {d 2}, w _ {d 3},.., w _ {d t}\right) \\ Q = \left(w _ {q 1}, w _ {q 2}, w _ {q 3},.., w _ {q t}\right) \end{array}
$$

where $w _ { d i } , w _ { q i } ( i = 1 \mathrm { { t o } } t )$ are term weights assigned to different terms for the document D and query $\mathcal { Q } ,$ , respectively. The similarity between a query and a document can be calculated by the inner product of the two vectors [37]:

$$
\text { Similarity } (Q, D) = \sum_ {i = 1} ^ {t} w _ {q i} \times w _ {d i}.\tag{1}
$$

Documents then are ordered by decreasing values of this measure or its normalized version (normalized with respect to the document length). The similarity value of a document to a query is also called retrieval status value (RSV).

The art of designing ranking functions depends on the design of term weighting strategies to assign weights for terms in a document, $w _ { d i } \left( w _ { q i } \right.$ is commonly represented by 1 if the term is present in the query and 0 otherwise, and hence it can be safely ignored in future analysis). Different term weighting strategies influence the similarity measure that is computed according to Eq. (1). For example, one of the commonly used term weighting strategies is the so-called <sup>b</sup>TFIDF<sup>Q</sup> strategy $( t f \times i d f )$ . For a term i, it is represented as $\begin{array} { r } { t f _ { i } \times \log \left( \frac { N } { d f _ { i } } \right) } \end{array}$ The resulting ranking function for a query $\mathcal { Q }$ and document $D$ can be represented as

$$
\text { Similarity } (Q, D) = \sum_ {i = 1} ^ {t} t f _ {i} \times \log \left(\frac {N}{d f _ {i}}\right)\tag{2}
$$

Here N is the total number of documents in a collection, $t f _ { i }$ is frequency of term i in the document, and $d f _ { i }$ is the number of unique documents in which term i appears in the entire collection. It is not difficult to see from $\operatorname { E q } .$ (2) that the final retrieval status value (RSV) for a given document D is a linear sum of calculated values using the same term weighting strategy for each term. We call this type of ranking function as a linear ranking function (LRF).

A quick example will illustrate the calculations of RSVs for different documents. Suppose we have a query asking for <sup>b</sup>corporate fraud<sup>Q</sup>. Thus $Q =$ <sup>b</sup>corporate fraud<sup>Q</sup>. Suppose there are a total of 1000 documents in the collection. Thus $N { = } 1 0 0 0$ . Say we want to find the RSV for the first two documents $D _ { 1 } ,$ and $D _ { 2 }$ in the collection. Suppose the term <sup>b</sup>corporate<sup>Q</sup> appears 5 times in the first document and it does not appear at all in the second document. Suppose the term <sup>b</sup>fraud<sup>Q</sup> appears 3 times in the first document and 2 times in the second document. Also suppose the term <sup>b</sup>corporate<sup>Q</sup> appears in 200 different documents while the term <sup>b</sup>fraud<sup>Q</sup> appears in 20 different documents. Then the above descriptions about the documents can be stated as:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$D_{1}=(information: 5, retrieval: 3)$ $D_{2}=(information: 0; retrieval: 2)$ 
And df(information)=200, df(retrieval=20), N=1000
</div>

Then according to Eq. (2), we can state that:

$$
\begin{array}{r l} \operatorname{RSV} (D _ {1}) & = \text { Similarity } (Q, D _ {1}) \\ & = 5 ^ {*} \log (1 0 0 0 / 2 0 0) + 3 ^ {*} \log (1 0 0 0 / 2 0) \\ & = 8. 5 9 \end{array}
$$

$$
\begin{array}{r l} \operatorname{RSV} (D _ {2}) & = \text { Similarity } (Q, D _ {2}) \\ & = 0 ^ {*} \log (1 0 0 0 / 2 0 0) + 2 ^ {*} \log (1 0 0 0 / 2 0) \\ & = 3. 4 \end{array}
$$

Thus, the first document has higher RSV and, hence, would be ranked higher than the second document.

Many well-known ranking functions, such as Okapi BM25, Pivoted TFIDF, INQUERY, are represented in LRF format [11,38]. LRFs are also the ranking function representation scheme used in all previous GP-based ranking function discovery studies [8–12,15,16].

## 2.2. Linear ranking function discovery by GP

As mentioned in the previous section, ranking functions are used by a search engine to rank documents according to how well they match a particular query. Since there is no single best ranking function for a query (or set of queries) [37,42], the problem of ranking function discovery can be modeled as a GP search problem. Candidate ranking functions can be represented as individuals in a GP population using tree structures, and then evolved by GP to discover better performing ranking functions than the existing ones. Previously, GP has been used to discover best permissible VSM-based LRFs [8– 12,15,16].

To apply GP to ranking function discovery, each ranking function is represented as an individual (chromosome) in a GP population. An example of such a representation is the well-known TFIDF LRF shown in Fig. 1.

Several required key components of a GP system are defined in Table 1. Fig. 2 illustrates graphically the process of crossover operation. It can be seen in Fig. 2 that the two children generated after the crossover operation are different from their parents. The crossover operation can not only allow children to inherit good <sup>b</sup>genes<sup>Q</sup> from their parents, but can also improve the diversity of the population. Thus, it is used extensively in genetic programming [26].

The configuration of the GP system used for linear ranking function discovery in previous work [8– 12,15,16] is shown in Table 2.

The overall ranking function discovery framework is shown in Fig. 3. Note that in Step 2.1, to assign a score for each document, we have to apply the same ranking (weighting) tree to each matching term and add the results up to obtain the total summation score as the RSV for a document. This step will be different for nonlinear ranking function design discussed in the following section.

![](/api/attachments/922S6NZT/fulltext/images/da92f9c6ba32b7d745d17603e8abcb62f6840903211f30ec295e42decbf0320f.jpg)  
Fig. 1. A sample tree representation for the TFIDF linear ranking function.

Table 1  
Essential GP component

<table><tr><td>Components</td><td>Meaning</td></tr><tr><td>Terminals</td><td>Leaf nodes in the tree structure.</td></tr><tr><td>Functions</td><td>Non-leaf nodes used to combine the leaf nodes. Commonly, numerical operations: +, -, ×, /.</td></tr><tr><td>Fitness function</td><td>The objective function GP aims to optimize.</td></tr><tr><td>Reproduction</td><td>A genetic operator that copies the individuals with the best fitness values directly into the population of the next generation without going through the crossover operation.</td></tr><tr><td>Crossover</td><td>A genetic operator that exchanges sub-trees from two parents to form two new children. Its aim is to improve diversity as well as the genetic fitness of the population. This process is shown in Fig. 2.</td></tr><tr><td>Mutation</td><td>A genetic operator that randomly selects a sub-tree and replaces it with another randomly created one. Its aim is to improve diversity as well as prevent being trapped in a local optimal solution.</td></tr></table>

## 3. Nonlinear ranking function representation

As mentioned in the previous two sections, linear ranking functions assume all terms in a document are assigned term weights according to the same weighting strategy. This assumption makes the VSM a very attractive model for ad hoc retrieval tasks in which a large number of queries from a variety of users have to be served. Thus the VSM is very suitable for generic information retrieval (IR) engines such as web search engines or library catalog search systems.

The restriction of this assumption is that it limits the ranking function to only a linear functional form, even though its components may be of nonlinear functional forms. Mathematically, all LRFs have the following form:

$$
\text { Similarity } (Q, D) = \sum_ {i = 1} ^ {t} w _ {d i}\tag{3}
$$

where t is the number of terms in the query Q. The linear functions may not have enough approximation power to model very complex relationships between documents and their relevance information to a given query due to the very complex human relevance judgment process [1,2,40].

![](/api/attachments/922S6NZT/fulltext/images/8e1791edd3cb348b381ef966488e5ed24c84098b1a66a3b0a890f0f5144f3f2a.jpg)  
Fig. 2. A graphical illustration of the crossover operation.

We believe for a given user query in a routing/ personalized search context, a ranking function should be flexible enough to reflect different roles played by different terms. Consider, for example, that we are interested in finding out or detecting whether a document is talking about potential fraud in a company. The term restatement may appear in very few documents (a high inverse document frequency idf for the term restatement) in the document collection we are looking at. At the same time the term say earnings miss appears quite frequently in these documents (a high tf for this term). It can be seen that the documents which have high tf for earnings miss and at the same time have high idf for restatement are better at discovering potential fraud in a company. From this example, we can see that instead of using the same term weighting strategy for all terms, different weighting strategies should be applied to different terms. These diverse weighting strategies can then be synthesized to generate a new nonlinear ranking function. For example, instead of applying the same tf strategy to all terms $\begin{array} { r } { ( { \mathrm { i . e . , } } f = \sum _ { i = 1 } ^ { 2 } t f _ { i } ) } \end{array}$ (if there are two terms in the query), we could use tf for term 1, $t f ^ { * } i d f$ for term 2, etc. The final ranking function would be a nonlinear function in a form like (but not limited to) $t f _ { 1 } + t f _ { 2 } { ^ { * } i d f _ { 2 } }$ . We believe that this type of nonlinear ranking function should handle the routing/personalized search task better than the traditional VSM-based linear ranking function because of its flexibility and high predictive power associated with nonlinear functional forms.

Modeling setup for linear ranking function discovery by GP

<table><tr><td>Components</td><td>Values</td></tr><tr><td>Terminals</td><td>As shown in Table 3</td></tr><tr><td>Functions</td><td>+, ×, /, log</td></tr><tr><td>Fitness function</td><td>Average precision (defined in Eq. (7))</td></tr><tr><td>Genetic operator</td><td>Reproduction, crossover, mutation</td></tr></table>

Refer to Table 1 for explanations of the various components.

We next give the formal definition of the nonlinear ranking functions.

Definition. For a document D, given all weighting evidence $e _ { i }$ where $i \in \{ 1 , . . . , m \}$ a nonlinear ranking function (NLRF) is of the following form:

$$
\mathrm{NLRF} = f (e _ {1},.., e _ {m})\tag{4}
$$

where m is the number of unique terms in the query, f( ): $\mathbf { R } ^ { m } \mapsto \mathbf { R } ^ { 1 }$ is a nonlinear function<sup>1</sup> of $e _ { 1 }$ to $e _ { m } .$

The set of weighting strategies that can be used in nonlinear ranking function representation is shown in Table 4.

The difference between the terminals defined in Tables 4 and 3 is that many of single terminals defined in Table 3 now become multiple terminals in Table 4. For example, tf in Table 3 becomes tf ; $i \in \{ 1 , . . . , n _ { Q } \}$ where $n _ { Q }$ is the number of unique terms in a query Q. This corresponds to the conversion of traditional <sup>b</sup>vector<sup>Q</sup> variables into <sup>b</sup>scalar<sup>Q</sup> variables in a numerical sense. This can be illustrated in Fig. 4 to contrast the two different ranking function representation schemes.

In fact, we can prove that LRFs used in the Vector Space model are special cases of NLRFs. In other words, all LRFs can be represented using the notation of NLRFs.

Theorem 1. Let LRF and NLRF be two sets of linear and non-linear ranking functions respectively. Then LRF is a subset of NLRF, i.e., LRFoNLRF.

Proof. We first prove that $\mathrm { L R F \subseteq N L R F } ,$ , then we prove that LRFp NLRF.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. Generate an initial population of random “ranking trees”.
2. Perform the following sub-steps on training documents for  $N_{gen}$  generations:
2.1 Use each ranking tree to score and rank the collection separately for a given query
2.2 Calculate the fitness of each ranking tree,
2.3 Record the top  $N_{top}$  ranking trees,
2.4 Create new population by:
a) Reproduction
b) Crossover
c) Mutation
3. Apply the recorded ( $N_{gen} \times N_{top}$ ) candidate “ranking trees” to a set of validation documents and select the best performing tree as the unique discovery output.
</div>

Fig. 3. Overall ranking function discovery framework. $N _ { \mathrm { g e n } }$ and $N _ { { \mathrm { t o p } } }$ are user-specified parameters. We set $N _ { \mathrm { g e n } } { = } 3 0$ and $N _ { \mathrm { t o p } } { = } 1 0$ for all our experiments.

First, take any element x from LRF, and treat $w _ { d i }$ in Eq. (3) as $e _ { i } ,$ then $x = e _ { 1 } + \cdots + e _ { n }$ . Because x satisfies the definition of NLRF, therefore x <sup>a</sup> NLRF, which proves $\mathrm { L R F \subseteq N L R F }$

Second, we use proof-by-contradiction to prove that NLRF is not equal to LRF, i.e., LRFp NLRF. Assume LRF=NLRF, which means for any $y \in \mathrm { N L R F } ,$ $y \in \mathrm { L R F }$ also holds. However, for example, if ${ \boldsymbol { y } } = t f _ { 1 } ^ { * } d f _ { 2 }$ , there is no equivalent representation in LRF form using $t f$ and $d f$ as the notation. Thus y gLRF, and hence our initial assumption LRF=NLRF is rejected.

Combining the above, LRF oNLRF is proven. 5

Theorem 1 shows that LRFs are special cases of NLRFs. Combining all the discussions above, it is not difficult to see that the NLRFs offer several advantages over LRFs:

a) More flexible weighting of terms: different terms can have their own way of weighting;

Table 3  
The terminals used in the linear GP discovery system

<table><tr><td>Terminals</td><td>Meaning</td></tr><tr><td> $tf$ </td><td>Number of occurrences of a term in a document</td></tr><tr><td> $tf_{\text{max}}$ </td><td>Maximum  $tf$  for a document</td></tr><tr><td> $tf_{\text{avg}}$ </td><td>Average  $tf$  for a document</td></tr><tr><td> $tf_{\text{doc,max}}$ </td><td>Maximum  $tf$  in the document collection</td></tr><tr><td> $df$ </td><td>Number of unique documents with a term</td></tr><tr><td> $df_{\text{max}}$ </td><td>Maximum df for a given query</td></tr><tr><td> $N$ </td><td>Total number of documents in the text collection</td></tr><tr><td>length</td><td>Length of a document</td></tr><tr><td> $length_{\text{avg}}$ </td><td>Average length of a document in the collection</td></tr><tr><td> $R$ </td><td>Real constant number randomly generated by the GP system</td></tr><tr><td> $n$ </td><td>Number of unique terms in a document</td></tr></table>

b) Higher predictive power due to the nonlinear functional form;

c) Larger functional space: LRFs are a proper subset of NLRFs.

Thus we hypothesize that NLRFs will perform better than LRFs for the personalized search task.

Note, however, that NLRF is only applicable at the individual query level. Thus, it is only suitable for information routing or personalized search with individual queries. This is because several terminals, such as $t f _ { i }$ and $d f _ { i } ,$ are applicable only to specific query words. Thus the NLRF scheme is not suitable for ad hoc information retrieval such as generic web search context. The VSM-based LRF form, on the other hand, does not have this constraint. As will be shown later in the results section, there is a trade-off between representation schemes and performance.

Table 4  
The terminals used in the nonlinear GP discovery system

<table><tr><td>Terminals</td><td>Meaning</td></tr><tr><td> $tf_{i}; i \in \{1, \dots, n_{Q}\}$ </td><td>Number of occurrences of a term in a document</td></tr><tr><td> $tf_{\text{max}}$ </td><td>Maximum  $tf$  for a document</td></tr><tr><td> $tf_{\text{avg}}$ </td><td>Average  $tf$  for a document</td></tr><tr><td> $tf_{\text{doc,max}}$ </td><td>Maximum  $tf$  in the document collection</td></tr><tr><td> $df_{i}; i \in \{1, \dots, n_{Q}\}$ </td><td>Number of unique documents with a term</td></tr><tr><td> $df_{\text{max}}$ </td><td>Maximum  $df$  for a given query</td></tr><tr><td> $N$ </td><td>Total number of documents in the text collection</td></tr><tr><td>length</td><td>Length of a document</td></tr><tr><td> $length_{\text{avg}}$ </td><td>Average length of a document in the collection</td></tr><tr><td> $R$ </td><td>Real constant number randomly generated by the GP system</td></tr><tr><td> $n$ </td><td>Number of unique terms in a document</td></tr></table>

![](/api/attachments/922S6NZT/fulltext/images/7eac289166f71b3ac0fd286cf055e4ad8369b4240f65d7fe41ac92a2ef6d77a5.jpg)  
Fig. 4. Conversion of a LRF representation to a NLRF representation different ranking function representation schemes.

More generic representation forms such as LRF, although suitable for both the information routing and ad hoc tasks in retrieval, may not have the best performance in all tasks. Similarly, more specialized representation form such as the NLRF may not be applicable in all contexts. We believe that the representation scheme should be context-specific based on the IR task we are performing.

We would like to note that the computational complexity in NLRF is relatively more than the LRF-based GP discovery since the number of the terminals are larger in NLRF than in the LRF approach. This makes the search space larger than LRF approach. However, our experiments showed that the computation time is still very fast and within acceptable practical limits.

The overall nonlinear ranking function discovery process with GP is similar to the process described in Fig. 3 except that in Step 2.1, the nonlinear ranking function represented by a GP tree can be applied to a document directly without the need to go through the iterating vector calculation process for each term to obtain the retrieval status value (RSV).

## 4. Experiment

The goal of the experiment discussed in this section was to test the performance of the proposed NLRF representation scheme in comparison to the traditional VSM-based LRF scheme.

## 4.1. Baselines

To be consistent with previous experiments [9–11], we used three baselines in our experiment.

The first baseline is the Okapi BM25 ranking Equation [34]. Okapi BM25 is designed utilizing a 2-stage Poisson model and has consistently performed very well in TREC competitions [21,22,34]. More formally, given a query $\mathcal { Q }$ and document $D ,$ , the Okapi BM25 ranking formula is defined as follows:

$$
\begin{array}{l} \operatorname{Sim} _ {O} (Q, D) = \sum_ {T \in Q} \frac {(k _ {1} + 1) t f}{k _ {1} \times \left((1 - b) + b \frac {\text { length }}{\text { length } _ {\text { avg }}}\right) + t f} \\ \times \log \frac {N - d f + 0 . 5}{d f + 0 . 5} \times q t f \end{array} \tag {5}
$$

where

$t f$ is the term frequency of a term (word) in the document text.

$q t f$ is the term frequency of a term (word) in the query text.

$N$ is the total number of documents in the collection. $d f$ is the number of documents in the collection in which the term under consideration is present. length is the length of the document (in words). $\mathrm { \ l e n g t h _ { a v g } }$ is the average document length in the collection (in words).

$k _ { 1 } , b$ are the parameters used to fine-tune the search performance.

We used the same value as in Robertson et al. [34] for $k _ { 1 }$ and $b \colon k _ { 1 } = 2$ and b =0.75. So Eq. (5) becomes:

$$
\begin{array}{l} \text {Sim} _ {O} \sum_ {T \in Q} \frac {3 \times t f}{0 . 5 + 1 . 5 \times \frac {\text {length}}{\text {length} _ {\text {avg}} + t f}} \\ \times \log \frac {N - d f + 0 . 5}{d f + 0 . 5} \times q t f. \end{array}\tag{6}
$$

Our second baseline is the SVM (Support Vector Machine), commonly used in information routing/filtering experiments. Our SVM implementation is similar to the one used in [12,39]. We trained the SVM for each query on the training data and used the model it produced to get the performance result on the test data.

Our third baseline is the GP-based discovery using the LRF representation scheme. We call this baseline LGP, standing for <sup>b</sup>linear GP<sup>Q</sup>. Our proposed GP approach using NLRF will be referred to as NLGP, standing for <sup>b</sup>nonlinear GP<sup>Q</sup>. Thus NLGP will be competing with three baseline models in this experiment.

## 4.2. Test collection

We used the widely used testbed for web search – TREC 10GB collection [21] – as our test collection. It contains 1.69 million documents. On average, each document has 311 words. We used 100 queries from topics 451–550 used in TREC 9 and TREC 10 web tracks as the test queries. The relevance judgment about each document in the collection is known in advance. It is obtained in TREC using a pool-based method. In this method, the top 1000 documents from each competing team taking part in TREC competitions are pooled together and duplicates are removed. A human expert on this topic is used to give relevance judgment for each document in this pool of documents. The other documents are assumed non-relevant. In our experiments, since 12 queries yielded no relevant documents in either validation or test data, we used the remaining 88 queries as the training queries. The length of the queries varied from 2 to 13 words. We indexed all documents and 88 queries into our own indexing format (designed for a GP experiment) after applying stopword removal and stemming [36].

## 4.3. Experimental design

As mentioned earlier, our experiment focused on the task of information routing or personalized search. For this task, a set of feedback training documents with known relevance information are available for user profiling or query expansion, as well as ranking function tuning. Thus, this experiment can be qualified as a supervised learning task. We followed a three data-sets design [9–11,30] in this experiment. We randomly split the data into training (49%), validation (21%), and test (30%) parts. The purpose of the validation data set was to help alleviate the problem of overfitting of GP on the training data and to select the best generalizable ranking function. All performance results were reported using only the test data set. The detailed experimental procedure for GP-based experiments – LGP and NLGP – followed the framework articulated in Fig. 3. Following GP, parameters were used in our experiments: We used tournament selection method to select parents for crossover and mutation. Crossover utilized a standard random subtree swapping algorithm. Population size was 500, crossover rate was 0.9, and mutation rate was 0.1.

We tested all four systems on two types of user profiles. One type of profile was a set of keywords extracted from the user-provided topic description. The other type of profile was the system-constructed profile utilizing relevance feedback or query expansion. We used the Robertson’s Selection Value scheme [33] to do the profile construction as this method has been found to work the best for user profiling and information routing tasks [14]. Thus, we have, in total, two independent experiments. For each experiment, both LGP and NLGP were run 10 times using different random seeds. The best result among 10 runs on validation data set was reported and used for comparison along with the Okapi and SVM baseline systems.

## 4.4. Performance evaluation

We report performance results using the standard non-interpolated average precision (PAVG) and precision at the top 10 hits (P10) [20,22]. These are the most popular measures for reporting performance of different IR systems.

PAVG, standing for average precision, is a commonly used performance measure in TREC evaluations [20]. It can be formally defined as follows:

$$
\text { Fitness } _ {\text { PAVG }} = \frac {\sum_ {i = 1} ^ {| D |} \left(r (d _ {i}) \times \left(\frac {\sum_ {j = 1} ^ {i} r (d _ {j})}{i}\right)\right)}{T _ {\text { Rel }}}\tag{7}
$$

where $r ( d ) \in \{ 0 , 1 \}$ is the relevance score assigned to a document, it being 1 if the document is relevant and 0 otherwise. |D| is the total number of retrieved documents. $T _ { \mathrm { R e l } }$ is the total number of relevant documents in a collection

PAVG measures both the precision and recall capabilities of an IR system, while P10 focuses more on the precision at the top of the retrieved list. We use both measures to get a balanced view of the benefits offered by each of the ranking functions. The next section shows the average results of all four ranking functions using these two measures over 88 queries.

## 5. Results

The performance results for the two experiments using different profiles are summarized in this section.

Table 5 lists the results for user-provided profiles extracted from user provided topic descriptions, and Table 6 lists results for system-constructed profiles with relevance feedback. In each table, two sets of performance results are reported. One set of results is under the heading of <sup>b</sup>predictive<sup>Q</sup>. For SVM, LGP and NLGP, these are the predictive performance results on the test data using the best ranking function/model discovered from the training process. Since there is no training for Okapi, the results under this heading report the performance results on the test data only. The other set of results is under the heading of <sup>b</sup>upperbound<sup>Q</sup>. These results only pertain to the GPbased discovery approaches. We applied all 300 candidate ranking functions (30 generations \* 10 best trees for each generation) discovered from the training session to the test data directly and chose the best result as the upperbound. The differences between these two sets of results will give us information about the generalizability of GP-discovered ranking functions.

Several interesting observations can be made with regards to Tables 5 and 6:

<sup>!</sup> NLGP performs better than LGP for both types of profiles. This can be observed from the comparison of the last two rows of each table. For predictive results of user-provided profiles, NLGP improves over LGP by 7.6% in PAVG and 6.3% in P10. Pairwise t-test shows that the improvement results on both measures are statistically significant with p <sup>b</sup>0.05. NLGP outperformed LGP in 75% of the queries. For upperbound results of user-provided profiles, NLGP improves over LGP by 7.8% in PAVG and 6.9% in P10. The improvement is even more for system-constructed profiles. In predictive experiments, NLGP improves over LGP by 9.2% in PAVG and 8.3% in P10 and these improvements are also statistically significant. For upperbound results, NLGP improves over LGP by 11% in PAVG and 10.5% in P10. The larger improvements of NLGP on system-constructed profiles over user-provided profiles show that this approach works better when user needs are more clearly identified, as in the systemconstructed profile case. The strong gain in upperbound performance results indicate that the chances of finding good ranking functions are higher in NLGP than in LGP as there is a strong correlation between predictive performance results and upperbound performance results. This clearly exemplifies our initial hypothesis that using NLRF as the representation scheme for GP-based ranking function discovery is beneficial.

Table 5  
Performance comparison on user-provided profiles

<table><tr><td rowspan="2"></td><td colspan="2">Predictive</td><td colspan="2">Upperbound</td></tr><tr><td>PAVG</td><td>P10</td><td>PAVG</td><td>P10</td></tr><tr><td>Okapi</td><td>0.2215</td><td>0.2452</td><td>-</td><td>-</td></tr><tr><td>SVM</td><td>0.1585</td><td>0.1698</td><td>-</td><td>-</td></tr><tr><td>LGP</td><td>0.2982</td><td>0.3281</td><td>0.4376</td><td>0.4258</td></tr><tr><td>NLGP</td><td>0.3209</td><td>0.3486</td><td>0.4718</td><td>0.4551</td></tr></table>

Table 6  
Performance comparison on system-constructed (relevance feedback) profiles

<table><tr><td rowspan="2"></td><td colspan="2">Predictive</td><td colspan="2">Upperbound</td></tr><tr><td>PAVG</td><td>P10</td><td>PAVG</td><td>P10</td></tr><tr><td>Okapi</td><td>0.3933</td><td>0.4114</td><td>-</td><td>-</td></tr><tr><td>SVM</td><td>0.4021</td><td>0.4102</td><td>-</td><td>-</td></tr><tr><td>LGP</td><td>0.4232</td><td>0.4282</td><td>0.5439</td><td>0.5157</td></tr><tr><td>NLGP</td><td>0.4622</td><td>0.4639</td><td>0.6042</td><td>0.5697</td></tr></table>

<sup>!</sup> Both NLGP and LGP show strong performance gains over the two baseline systems – Okapi and SVM – on user-provided profiles. The performance gains are generally in the range of 30% to 40% in terms of both PAVG and P10. The performance gains are even more dramatic compared to SVM. SVM did not perform well for user-constructed profiles. One possible reason is that the small numbers of features available did not help SVM to learn effectively, which is not unexpected as SVM is known to work well for larger dimensions [25]. For system-constructed profiles, the performance gains by LGP and NLGP over the two baseline systems are not as dramatic as those in the userprovided profiles. This is expected as both baselines have gained tremendously in performance after query expansion through relevance feedback. Still, NLGP outperforms Okapi by 15% in PAVG and 10% in P10.

<sup>!</sup> There are still gaps between predictive performances and their corresponding upperbounds. For user-provided profiles, the predictive performance results of both LGP and NLGP are within 68% in PAVG and 77% in P10 of their corresponding upperbound performance results. The gap shrinks for system-constructed profiles, with both LGP and NLGP within 75% in PAVG and 81% in P10 of their corresponding upperbound results. The discrepancies between the predictive and upper-bound performance results indicate that the ranking functions discovered by GP may still suffer from an overfitting problem, in which the best solution discovered from training may not work consistently well in the test data. This overfitting is inevitable due to the sampling error as well as the inherent noise in textual data.

<sup>!</sup> Both experiments confirm that system-constructed profiles are favorable over user-provided profiles. All four systems compared thus far have gained dramatically when profiles are changed from userprovided to system-constructed. These results are consistent with previous research findings [14]. It also points out the concern with many existing topic tracking systems in which user-provided profiles are not only prevalent, but often the only method available. The future generation information routing or content syndication system should enable multiple profile representation or generation methods so that the user experience with such a service can be enhanced. For example, instead of asking users directly to provide their topic keywords, the system could ask users to provide sample documents within their interests and outside of their interests. Alternatively, the system could keep track of the users’ click-through data to implicitly update or augment a user’s profile with proper user consent.

## 6. Conclusion

In this paper, we considered the model representation issues in GP-based ranking discovery for information routing/personalized search context. We proposed a novel nonlinear ranking function representation scheme (NLRF) and theoretically showed its relationship with the traditional linear ranking function (LRF) representation scheme based on the Vector Space Model. This new NLRF scheme was then incorporated into the GP ranking function discovery engine to detect the best possible ranking function for an information routing/personalized search task. The experimental results of this NLGP engine in comparison with various well-known baseline systems (Okapi, SVM, and LGP) show that NLGP works better than LGP and the other baseline systems. The results also demonstrate that generic ranking function representation schemes such as LRF may not work well for all contexts. The ranking function representation should be customized or tailored to the task at hand. We also discussed the profile representation issues with the current information routing or context syndication systems and gave our recommendations.

In the future, we plan to expand the terminals used in the NLGP system to include more structural weighting evidence. For example, instead of using $t f _ { i } ,$ , we may use $t \mathrm { f _ { a n c h o r _ { \it i } } , \ } t f _ { \mathrm { t i t l e _ { \it i } } } , \mathrm { e t c . }$ ., to include more structural information to see whether the additional structural information is beneficial. Here anchor refers to the terms appearing in the anchors (link references to other documents) of documents, while the title refers to the terms appearing in the title of the document. Another possible direction is to introduce Boolean operation into the terminal set design and use GP to discover Boolean decision rules for information filtering/text classification applications. We are also in the process of building a prototype personalized information routing engine. We plan to incorporate the ideas discussed in this paper and conduct more extensive real user evaluations to compare different approaches.

## References

[1] C.L. Barry, L. Schamber, Users’ criteria for relevance evaluation: a cross-situational comparison, Information Processing & Management 34 (2–3) (1998) 219– 236.

[2] P. Borlund, The concept of relevance in IR, Journal of the American Society for Information Science and Technology 54 (10) (2003) 913– 925.

[3] H. Chen, Machine learning for information retrieval: neural networks, symbolic learning, and genetic algorithms, Journal of the American Society for Information Science 46 (3) (1995) 194– 216.

[4] H. Chen, Y. Chung, M. Ramsey, C. Yang, A smart itsy bitsy spider for the web, Journal of the American Society for Information Science 49 (7) (1998) 604– 618.

[5] H. Chen, G. Shankaranarayanan, L. She, A. Lyer, A machine learning approach to inductive query by examples: an experiment using relevance feedback, ID3, genetic algorithms, and simulated annealing, Journal of the American Society for Information Science 49 (8) (1998) 693– 705.

[6] O. Cordon, F. Moya, M.C. Zarco, A GA-P algorithm to automatically formulate extended Boolean queries for a fuzzy information retrieval system by means of gap techniques, Mathware and Soft Computing 7 (2–3) (2000) 309– 322.

[7] W. Fan, D. Gordon, P. Pathak, Automatic generation of matching functions by genetic programming for effective information retrieval, Proceedings of 1998 Americas Conference on Information Systems, Milwaukee, USA, 1998.

[8] W. Fan, D. Gordon, P. Pathak, Personalization of search engine services for effective retrieval and knowledge management, Proceedings of 2000 International Conference on Information Systems (ICIS), Brisbane, Australia, 2000, pp. 20 – 34.

[9] W. Fan, E.A. Fox, P. Pathak, H. Wu, The effects of fitness functions on genetic programming-based ranking discovery for web search, Journal of the American Society for Information Science and Technology 55 (7) (2004) 628– 636.

[10] W. Fan, M.D. Gordon, P. Pathak, Discovery of context-specific ranking functions for effective information retrieval using genetic programming, IEEE Transactions on Knowledge and Data Engineering 16 (4) (2004) 523– 527.

[11] W. Fan, M.D. Gordon, P. Pathak, A generic ranking function discovery framework by genetic programming for information retrieval, Information Processing & Management 40 (4) (2004) 587– 602.

[12] W. Fan, M.D. Gordon, P. Pathak, W. Xi, E.A. Fox, Ranking function optimization for effective web search by genetic

programming: an empirical study, Proceedings of 37th Hawaii International Conference on System Sciences, IEEE, Hawaii, 2004.

[13] W. Fan, M. Luo, L. Wang, W. Xi, E.A. Fox, Tuning before feedback: combining ranking function discovery and blind feedback for robust retrieval, Proceedings of the 27th Annual International ACM SIGIR Conference, ACM, UK, 2004.

[14] W. Fan, M.D. Gordon, P. Pathak, Effective profiling of consumer information retrieval needs: a unified framework and empirical comparison, Decision Support Systems 40 (2) (2005) 213– 233.

[15] W. Fan, M.D. Gordon, P. Pathak, Genetic programming based discovery of ranking functions for effective web search, Journal of Management Information Systems 21 (4) (2005) 37– 56.

[16] W. Fan, M.D. Gordon, P. Pathak, An integrated two-stage model for intelligent information routing, Decision Support Systems (in press).

[17] M. Gordon, Probabilistic and genetic algorithms for document retrieval, Communications of ACM 31 (2) (1988) 152– 169.

[18] M. Gordon, User-based document clustering by redescribing subject descriptions with a genetic algorithm, Journal of the American Society for Information Science 42 (5) (1991) 311 – 322.

[19] D.K. Harman, Overview of the first text retrieval conference (TREC-1), in: D.K. Harman (Ed.), Proceedings of the First Text Retrieval Conference, NIST Special Publication, vols. 500-207, 1993, pp. 1 – 20.

[20] D.K. Harman, Overview of the fourth text retrieval conference (TREC-4), in: D.K. Harman (Ed.), Proceedings of the Fourth Text Retrieval Conference, NIST Special Publication, vols. 500-236, 1996, pp. 1 – 24.

[21] D. Hawking, Overview of the TREC-9 web track, in: E.M. Voorhees, D.K. Harman (Eds.), Proceedings of the Ninth Text Retrieval Conference, NIST Special Publication, vol. 500-249, 2000, pp. 86– 102.

[22] D. Hawking, N. Craswell, Overview of the TREC-2001 web track, in: E.M. Voorhees, D.K. Harman (Eds.), Proceedings of the Tenth Text Retrieval Conference, NIST Special Publication, vols. 500-250, 2001, pp. 61–67.

[23] J.H. Holland, Adaptation in Natural and Artificial Systems, 2nd edition, MIT Press, 1992.

[24] J.-T. Horng, C.-C. Yeh, Applying genetic algorithms to query optimization in document retrieval, Information Processing & Management 36 (2000) 737– 759.

[25] T. Joachims, Making large-scale support vector machine learn ing practical, in: A.S.B. Scholkopf, C. Burges (Eds.), Advances in Kernel Methods: Support Vector Machines, MIT Press, Cambridge MA, 1998.

[26] J.R. Koza, Genetic Programming: On the Programming of Computers by Means of Natural Selection, MIT Press, Cambridge, MA, USA, 1992.

[27] W.B. Langdon, Data Structures and Genetic Programming: Genetic Programming + Data Structures = Automatic Programming, Kluwer Publishing, 1998.

[28] C. Lopez-Pujalte, V.P.G. Bote, F. de Moya Anegon, A test of genetic algorithms in relevance feedback, Information Processing & Management 38 (2002) 793– 805.

[29] M.J. Martin-Bautista, M. Vila, H.L. Larsen, A fuzzy genetic algorithm approach to an adaptive information retrieval agent, Journal of the American Society for Information Science 50 (9) (1999) 760– 771.

[30] T.M. Mitchell, Machine Learning, McGraw Hill, 1997.

[31] P. Pathak, M. Gordon, W. Fan, Effective information retrieval using genetic algorithms based matching function adaptation,

Proceedings of the 33rd Hawaii International Conference on System Science (HICSS), Hawaii, USA, 2000.

[32] J. Pitkow, H. Schutze, T. Cass, R. Cooley, D. Turnbull, A. Edmonds, E. Adar, T. Breuel, Personalized search, Communica tions of the ACM 45 (9) (2002 (September)) 50–55.

[33] S. Robertson, On relevance weight estimation and query expansion, Journal of Documentation 42 (1986) 182– 188.

[34] S.E. Robertson, S. Walker, S. Jones, M.M. Hancock-Beaulieu, M. Gatford, Okapi at TREC-4, in: D.K. Harman (Ed.), Proceedings of the Fourth Text Retrieval Conference, NIST Special Publication, vols. 500-236, 1996, pp. 73– 97.

[35] G. Salton, The SMART Retrieval System: Experiments in Automatic Document Processing, Prentice Hall, New Jersey, 1971.

[36] G. Salton, Automatic Text Processing, Addison-Wesley Publishing Co., Reading, MA, 1989.

[37] G. Salton, C. Buckley, Term weighting approaches in automatic text retrieval, Information Processing & Management 24 (5) (1988) 513– 523.

[38] A. Singhal, G. Salton, M. Mitra, C. Buckley, Document length normalization, Information Processing & Management 32 (5) (1996) 619– 633.

[39] A. Sun, E.-P. Lim, W.-K. Ng, Web classification using support vector machine, Proceedings of the Fourth International Workshop on Web Information and Data Management, ACM Press, 2002, pp. 96 – 99.

[40] R. Tang, P. Solomon, Toward an understanding of the dynamics of relevance judgement: an analysis of one person’s search behavior, Information Processing & Management 34 (2–3) (1998) 237– 256.

[41] J.J. Yang, R.R. Korfhage, Effects of query term weights modification in document retrieval: a study based on a genetic algorithm, Proceedings of the Second Annual Symposium on Document Analysis and Information Retrieval, Las Vegas, NV, 1993, pp. 271– 285.

[42] J. Zobel, A. Moffat, Exploring the similarity space, SIGIR Forum 32 (1) (1998) 18–34.

![](/api/attachments/922S6NZT/fulltext/images/c7743faa2edb15310f917d3a97e532fd7a27222aac7dd177afbc4b599d3f0130.jpg)

Weiguo (Patrick) Fan is an assistant professor of information systems and computer science at the Virginia Polytechnic Institute and State University. He received his Ph.D. in Information Systems from the Ross School of Business at the University of Michigan, Ann Arbor, in July 2002, a M.Sc. in Computer Science from the National University of Singapore, in 1997, and a B.E. in Information and Control Engineering from the Xi’an Jiaotong University, P.R. China, in 1995.

His research interests focus on the design and development of novel information technologies information retrieval, data mining, text/web mining, personalization and knowledge management techniques to support better business information management and decision making. His research has appeared in many leading information technology journals such as Communications of ACM, IEEE Transactions on Knowledge and Data Engineering, Journal of the American Society on Information Science and Technology, Information Processing and Management, Information Systems, Journal of Management Information Systems, Decision Support Systems, ACM Transactions on Internet Technology, IEEE Intelligent Systems, International Journal of Electronic Business, and in leading information technology conferences such as SIGIR, WWW, CIKM, HLT, ICIS, HICSS, etc.

![](/api/attachments/922S6NZT/fulltext/images/03eac797763e7312627505550ad0d6f9eb4791237d186bd32ec838ea1b6496ce.jpg)

Praveen Pathak is an Assistant Professor of Decision and Information Sciences at the Warrington College of Business at the University of Florida. He received his Ph.D. in Computer and Information Systems from the Ross School of Business, University of Michigan, Ann Arbor, in 2000, MBA from the Indian Institute of Management, Calcutta, in 1990, and B.Tech. (Hons.) from the Indian Institute of Technology, Kharagpur, in 1987. His research interests include information

retrieval, text mining, business intelligence, and knowledge management. His research has been published in Journal of Management Information Systems, Information Processing and Management, IEEE Transactions on Knowledge and Data Engineering, Decision Support Systems, Journal of the American Society on Information Science and Technology, and in conference proceedings such as ICIS, HICSS, AMCIS and WITS.

![](/api/attachments/922S6NZT/fulltext/images/9ad2a24a4ebde86d4e4368f70efb938a6cb9f99ee54cc60081ce14ad83cf15e1.jpg)

Linda Wallace is an assistant professor in the Department of Accounting and Information Systems at the Virginia Polytechnic Institute and State University. She obtained her Ph.D. in Computer Information Systems from Georgia State University in 1999. She also received a B.B.A. in Accounting and a B.S. in Math/Computer Science from Oglethorpe University in 1992.

Her research interests include software project risk, agile software development, in-

formation security, and online communities. Her research has been accepted for publication in journals such as Decision Sciences, Communications of the ACM, Information & Management, and Journal of Systems and Software, and the Proceedings of the Academy of Management.
