---
otero_id: 8138
otero_key: "7V4VYU75"
title: "An associate constraint network approach to extract multi-lingual information for crime analysis"
authors: "Christopher C. Yang; Kar Wing Li"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.04.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An associate constraint network approach to extract multi-lingual information for crime analysis

Christopher C. Yang <sup>a,⁎</sup>, Kar Wing Li <sup>b</sup>

<sup>a</sup> Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Hong Kong <sup>b</sup> Department of Information Systems, City University of Hong Kong, Hong Kong

Available online 7 July 2006

## Abstract

International crime and terrorism have drawn increasing attention in recent years. Retrieving relevant information from criminal records and suspect communications is important in combating international crime and terrorism. However, most of this information is written in languages other than English and is stored in various locations. Information sharing between countries therefore presents the challenge of cross-lingual semantic interoperability. In this work, we propose a new approach – the associate constraint network – to generate a cross-lingual concept space from a parallel corpus, and benchmark it with a previously developed technique, the Hopfield network. The associate constraint network is a constraint programming based algorithm, and the problem of generating the cross-lingual concept space is formulated as a constraint satisfaction problem. Nodes and arcs in an associate constraint network represent extracted terms from parallel corpora and their associations. Constraints are defined for the nodes in the associate constraint network, and node consistency and network satisfaction are also defined. Backmarking is developed to search for a feasible solution. Our experimental results show that the associate constraint network outperforms the Hopfield network in precision, recall and efficiency. The cross-lingua concept space that is generated with this method can assist crime analysts to determine the relevance of criminals, crimes, locations and activities in multiple languages, which is information that is not available in traditional thesauri and dictionaries. © 2006 Elsevier B V All rights reserved

Keywords: Cross-lingual concept space; Cross-lingual information retrieval; Associate constraint network; Constraint satisfaction problem; Crime analysis

## 1. Introduction

In this age of globalisation and information revolution, the threat of international crime and terrorism has increased significantly. Rapid changes in technology have opened new opportunities for trafficking contraband, conducting illicit trade, laundering money and engaging in large-scale economic crimes. New forms of terrorism are also emerging. These threats have a great effect on the citizens, businesses and national security of many countries. Some evidence of cross-border international crime and terrorism is shown below:

• Algerian national Ahmed Ressam, who was associated with an extremist group that has ties to Al Qaeda, attempted to smuggle bomb making material into the United States from Canada. He was arrested in Port Angeles, Washington.

• The number of annual fatalities in terrorist-related violence in south Asia far exceeds the death toll in the Middle East, which is traditionally held to be the cradle of terrorism [2].

• Illegal migration that is facilitated by organized alien smuggling networks is on the rise. The “human cargo” is often kept in cramped, unhealthy and dangerous conditions, and many women and children are smuggled across borders for sexual exploitation and forced labour.

• The tremendous cost of legally disposing of pollutants and dangerous chemicals has created new illicit business opportunities, and many criminal organizations illegally export toxic wastes to countries in Eastern and Central Europe, Asia and Africa.

• Intellectual property rights (IPR) crimes cause tremendous revenue losses for the entertainment industries, and the explosion of digitisation and the Internet has enabled the IPR violators to effortlessly copy and distribute electronic products.

• International criminals produce, distribute and use counterfeit money for profit, to make illicit transactions, to finance illegal operations, and to promote illicit activities.

• Finally, high-tech crimes, in particular against computer networks, are becoming an increasing law enforcement and national security problem because of the growing reliance of government entities, public utilities, industries, business and financial institutions on electronic data and information storage, retrieval and transmission.

All of this evidence demonstrates that a strong alliance of the law enforcement, defence and security agencies in different countries is needed, and channels through which agencies can exchange information and intelligence on international criminal and terrorist activities are needed.

The successful combating of international crimes and terrorism relies on information sharing between different countries to evaluate the threats and vulnerabilities and to issue the necessary warnings. A knowledge management system can enable the retrieval of relevant information from criminal records and suspect communications in multiple languages for a threat before it causes widespread harm. This creates the challenge of cross-lingual semantic interoperability.

The language barrier is a major problem in knowledge management for international crime analysis. Terrorists and criminals may communicate through emails and bulletin boards in languages other than English. Many of the words that are used in such communications are unknown words that do not exist in dictionaries, such as the names of criminals or terrorists. Typical dictionary-based approach is unable to provide a translation for such terms. Furthermore, translations may not be consistent across different regions. The translation of “Bin Laden”, for example, may be different in China, Hong Kong and Taiwan. It is impossible to update these translations manually. The use of an automated cross-lingual concept space has proved to be promising in solving the problem of cross-lingual semantic interoperability. A concept space is a semantic network that consists of concepts (noun phrases in the textual domain) and related concepts, in which the association of concepts is computed based on co-occurrence relationships. A concept is a noun phrase that represents something that is conceived in the mind. For a given language, a concept may be represented by a word or words, or by a morpheme, an idiomatic expression, a tone or word order. Several concepts may be represented by a single word in one language, but may be translated as one word, two words, a phrase or even a sentence in another language [15]. A concept space for two languages is called a bilingual concept space. A bilingual concept space that represents the association of concepts across the languages is also known as the cross-lingual concept space. In this work, we focus on an English/Chinese cross-lingual concept space.

The research problem in this work is to build a crosslingual concept space to resolve the problem of crosslingual semantic interoperability. Such a cross-lingual concept space must be capable of supporting users to search across language boundaries for relevant information to combat international crime and terrorism. For example, users may submit the query ‘peer to peer’ to search for information about the illegal downloading of copyrighted electronic files. An automatic cross-lingual concept space would then provide related concepts in the same language and other languages, such as ‘P2P’, ‘ ’ (peer to peer), ‘ ’ (peer to peer), ‘ ’ (client), ‘client’, ‘ ’ (server), and ‘server’. The related concepts can then be used to expand the original query to search for relevant information in multiple languages.

In our previous work [14], we investigated the Hopfield network for generating a cross-lingual concept space to support cross-lingual information retrieval using the Hong Kong SAR Police Department's Web corpus as the test bed for crime analysis. The results found the investigated technique to be promising, and high precision and recall were obtained. However, the Hopfield network has two shortcomings. Firstly, its efficiency in a large network of association of English and Chinese terms is unsatisfactory, and the convergence process is time consuming, especially for general terms. The general terms usually have small semantic distance with other terms. As a result, many terms can be activated and it may not converge. Secondly, the results from the cross-lingual concept space are not consistent, because the Hopfield network is basically a random process, and thus the results that are generated through different convergence processes with the same input are not necessarily the same.

In this work, we propose an associate constraint network approach to tackle the problem of cross-lingual semantic interoperability. The cross-lingual concept space is modelled as an associate constraint network, and the problem of generating cross-lingual concepts is formulated as a constraint satisfaction problem. The nodes in the associate constraint network represent the extracted bilingual terms of a parallel corpus, and the arcs of the associate constraint network represent the association between the extracted terms. The constraints on the nodes are presented. Node consistency and network satisfaction are then defined. A constraint propagation technique that is known as backmarking is proposed to solve the constraint satisfaction problem. Using backmarking, various items of information in different languages are linked together according to the conceptual relationships that are embedded in a parallel corpus and are presented to the analyst as the result for a single query. In our experiment, the English/Chinese daily press releases that are issued by the Hong Kong Police Department are used. Such a crosslingual knowledge base can aid the pursuit and apprehension of suspects, the searching for evidence and the allocation of resources. An adequate knowledge base could form the basis for collective action in response to the elusive tactics of global terrorists.

## 2. Automatic generation of cross-lingual concept space

Due to the limitation of a dictionary-based approach to cross-lingual information retrieval and the infeasibility of manually constructing a sophisticated bilingual dictionary or multilingual thesaurus, most recent works have focused on a corpus-based approach to the problem of cross-lingual semantic interoperability. The corpusbased approach uses term co-occurrence statistics in parallel or comparable corpora to construct a statistical translation model. A parallel corpus is a collection of pairs of documents in two languages, in which the pairs of documents are translations of each other. A comparable corpus is a collection of documents that is composed independently in the respective languages and combined on the basis of similarity of content, domain and communicative function [16].

To automatically generate a cross-lingual concept space, several major components are needed. (1) Aligning documents to construct parallel corpus, (2) phrase extraction in each language, (3) co-occurrence analysis and (4) concept space generation. Fig. 1 depicts the mechanism for the automatic generation of an English/Chinese concept space.

## 2.1. Construction of a parallel corpus

In our previous work, we developed an alignment technique to construct a parallel corpus from the Web [20], in which the longest common subsequence was utilized to optimize the alignment of English and Chinese titles and redundancy was considered in the translations. Our results showed that 100% precision was achieved and over 90% recall was obtained, where precision was the fraction of extracted pairs of parallel documents that were correctly aligned and recall was the fraction of correctly aligned pairs of parallel documents that were extracted. A parallel corpus of Hong Kong SAR police press releases on the Web with over 2500 pairs of documents was collected for the experiment in this work.

## 2.2. Phrase extraction

The phrase extraction of the English and Chinese documents identifies important conceptual phrases in the corpus. In the English phrase extraction, a stop-word list and term-phrase formation are utilized [17]. A stop-word list is a list of non-semantic bearing words such as ‘the’, ${ \bf \ddot { a } } _ { \bf \dot { \theta } }$ , ‘on’ and $ { \mathrm { \ddot { \cdot } } } _ { \mathrm { i n } } ,$ . The stop words are first removed from the English documents, and the term-phrase formation is then utilized to formulate phrases by combining adjacent words [4]. For example, ‘international crime’ is a term phrase that is formed by the two adjacent words, ‘international’ and ‘crime’. In the Chinese phrase extraction, we employ our heuristic approach, which is based on mutual information, and the significant estimation [5] of adjacent Chinese characters [21,22]. Over 90% accuracy is achieved using this heuristic approach.

![](/api/attachments/7V4VYU75/fulltext/images/0b53d2faf18811e4957cd41088a24ec872488f1ca35e8c6932c0bce09b625c09.jpg)  
Fig. 1. Automatic Chinese–English concept space generation.

## 2.3. Co-occurrence analysis

In the Chinese/English parallel corpus, N pairs of Chinese documents and English documents, $C _ { i }$ and $E _ { i }$ $( i { = } 1 , 2 , . . . , N )$ , are aligned. For each document pair, the M most significant Chinese terms and the M most significant English terms are extracted based on the term weights $( d _ { i j }$ and $d _ { i j * } )$ that are computed by the term frequencies and the inverse document frequencies. The term frequency factor provides a measurement of how well a term describes the document contents, which is called the intradocument characterization. The inverse document frequency factor is a measurement of inter-cluster similarity, which is important because terms that appear in many documents are not useful in distinguishing a relevant document from a non-relevant document. A log function is typically applied to the inverse document frequencies to penalize terms that appear in many documents. This function has been proved to be effective, and has been applied in most information retrieval techniques.

$$
d _ {i j} = t f _ {i j} \times \log \left(\frac {N}{d f _ {j}} \times w _ {j}\right)\tag{1}
$$

$$
d _ {i j *} = t f _ {i j} * \times \log \left(\frac {N}{d f _ {j} *} \times w _ {j} *\right)\tag{2}
$$

where

$t f _ { i j }$ is the term frequency of Chinese term j in document i

$N$ is the total number of documents in the collection,

$d f _ { j }$ is the document frequency of Chinese term j, $w _ { j }$ is the length of Chinese term $j ,$

$\mathcal { H } _ { i j * }$ is the term frequency of English term $j ^ { * }$ in document $i ,$

$d f _ { j * }$ is the document frequency of English term $j ^ { * } { } _ { ; }$ , and

$w _ { j } { } ^ { * }$ is the length of English term $j *$

The length of an English term is determined by the number of words, and the length of a Chinese term is determined by the number of characters.

After extracting the most significant terms from N document pairs, the relevance weights between the extracted terms are computed based on the co-occurrence analysis. The co-importance weight $d _ { i j k }$ between term j and term k is computed as follows, where term j and term k can be Chinese terms or English terms (term $j ^ { * }$ and term k<sup>⁎</sup>).

$$
d _ {i j k} = t f _ {i j k} \times \log \left(\frac {N}{d f _ {j k}} \times w _ {j}\right)\tag{3}
$$

where

$t f _ { i j k }$ is the minimum of $t f _ { i j }$ and $t f _ { i k }$ in document pair $i ,$

$d f _ { j k }$ is the document frequency of both term j and term k.

$d _ { i j k }$ corresponds to the co-importance weight between Chinese term j and English term $k ^ { * }$ in document pair i, $d _ { i j k }$ corresponds to the co-importance weight between Chinese term $j$ and Chinese term k and $d _ { i j } { ^ { * } k ^ { * } }$ corresponds to the co-importance weight between English term $j ^ { * }$ and English term $k ^ { * }$

The relevance weights between term j and term k, $W _ { j k }$ and $W _ { k j } ,$ , are then computed based on the following asymmetric functions.

$$
W _ {j k} = \frac {\sum_ {i = 1} ^ {N} d _ {i j k}}{\sum_ {i = 1} ^ {N} d _ {i j}} \times \text { WeightingFactor } (k)\tag{4}
$$

$$
\operatorname{WeightingFactor} (k) = \frac {\log \frac {N}{d f _ {k}}}{\log N}\tag{5}
$$

The relevance weights between term j and term $k$ are asymmetric. If term j is more significant than term $k ( \sum$ $d _ { i j } { > } \sum d _ { i k } )$ , then $W _ { j k }$ is less than $W _ { k j } ,$ , which means that the more significant term will have less impact on the less significant term. For example, the term ‘peer to peer’ has less impact on the term ‘Internet’, and thus ‘Internet’ will not be included in the concept space of ‘peer to peer’.

## 2.4. Hopfield network

We previously investigated the generation of a crosslingual concept space using the Hopfield network [13,23]. The Hopfield network resembles an associative network, exhibits a parallel relaxation property and can transform a partial noisy distributed pattern into a stable state representation. Knowledge and information can be stored in single-layered, interconnected neurons (nodes), and weighted synapses (links). The cross-lingual concept space can be retrieved based on the parallel relaxation and convergence methods of the network.

Each term in the network-like thesaurus is treated as a neuron, and the asymmetric weight between any two terms is taken as the unidirectional, weighted connection between neurons. The value of the weight indicates the strength of the connection and degree of relevance between two neuron nodes. Using user-supplied terms as input patterns, the Hopfield algorithm activates the neighbours of the terms (strongly associated terms), combines the weights of all of the associated neighbours by summing the collective association strengths, and repeats this process until convergence. During the process, the algorithm causes a damping effect, in which terms that are further away from the initial terms receive gradually decreasing activation weights and eventually ‘die out’. This phenomenon is consistent with the spreading activation process of the human memory [4]. The activation process is shown as follows.

$$
u _ {j} (t + 1) = f _ {s} \left[ \sum_ {i = 0,} ^ {n - 1} W _ {i j} u _ {i} (t) \right], 0 \leq j \leq n - 1\tag{6}
$$

where

$u _ { j } ( t ^ { + } 1 )$ denotes the value of node j in iteration $t + 1$ n is the total number of nodes in the network, $W _ { i j }$ denotes the relevance weight from node i to node $j ,$ and

$f _ { s }$ is the continuous SIGMOID transformation function, which normalizes any given value to a value between 0 and 1. This formula shows the parallel relaxation property of the Hopfield network. The details of the algorithm are discussed in [13].

## 2.4.1. Shortcomings of the Hopfield network

The Hopfield network has many desirable properties, but also has a few drawbacks. In terms of the construction of the concept space, the Hopfield network approach does not converge efficiently towards a feasible equilibrium state, and there is often a trade-off between computational time and minimising the network error. With a network of 9222 English and Chinese terms, it takes 49 s on average to generate the concept space of a single term. Building the concept space of all of the English and Chinese terms takes over 450,000 ${ \bf S } ,$ and in some cases the Hopfield network may not converge at all. Moreover, the Hopfield network consists of a sequence of random variables that evolve over time. The value of a particular variable at time t + 1 depends on the state of the variables at time t. As the number of iterations increases in the convergence process, it is impossible to trace back how the nodes are activated, and the concept space that is generated is not necessarily consistent because of the randomness. This means that the relevant concepts that are extracted by the Hopfield network in different converging processes may be different. In addition, the Hopfield network is totally recurrent [8,9] and thus the order in which the units are updated can have a significant effect on processing.

## 3. Associate constraint network approach

To overcome the shortcomings of the Hopfield network in the automatic construction of a cross-lingual concept space, we propose a constraint programming based algorithm. The cross-lingual concept space is modelled as an associate constraint network, and the problem of generating the cross-lingual concept space is formulated as a constraint satisfaction problem.

## 3.1. Constraint satisfaction problem

The constraint satisfaction problem (CSP) has been a prominent research topic in artificial intelligence for many years. A constraint satisfaction problem is a triple (V, D, C), where

• $V$ is a set of variables, $V = \{ \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { n } \}$

• D is a function that maps every variable in V to a set of possible values, (D: $V { \xrightarrow { } } a$ set of possible values) and the set $D _ { i }$ is the domain of variable $\nu _ { i } ,$ and

$C$ is a set of constraints on an arbitrary subset of variables in V that restricts the values that the variables can simultaneously take.

The solution of a CSP involves the assignment of a value from its domain to every variable so that every constraint is satisfied. A CSP is satisfiable if a solution tuple exists. A solution tuple of a CSP is a compound label for all of the variables that satisfy all of the constraints [18]. Depending on the requirements of an application, CSPs can be classified into the following categories.

1. CSPs in which one has to find any solution tuple.

2. CSPs in which one has to find all of the solution tuples.

3. CSPs in which one has to find optimal solutions, where optimality is defined according to the domain knowledge [18].

There are two broad classes of algorithms for searching systematically through the possible assignments of values to variables to find the solution to a constraint satisfaction problem. The first class of algorithms traverses the space of partial solutions (or partial value assignments), and the second class explores the space of complete value assignments to all of the variables stochastically [10]. A partial value assignment is the search for a solution tuple by incrementally instantiating variables until all of the constraints are satisfied. A complete value assignment is the search for all of the solution tuples by generating all of the possible combinations of variable assignments and finding the tuples that satisfy all of the constraints. An exhaustive search is the conducting of a complete value assignment. The efficiency of a complete value assignment will be much lower than a partial value assignment, but for some applications complete value assignments are needed so that all of the solution tuples or the optimized solution tuple can be identified. However, for the generation of a cross-lingual concept space, optimization is not required, and one solution tuple is sufficient.

A CSP is usually depicted as a constraint network [19]. A constraint network is a declarative structure that consists of nodes and arcs, in which each node represents a variable and each arc represents a constraint between the variables that is represented by the end points of the arc. Consistency can be defined in terms of nodes (node consistency), arcs (arc consistency) or paths (path consistency). The satisfaction of a constraint network requires the consistency of nodes, arcs, or paths [1].

In this research, an associate constraint network approach is proposed to construct an automatic thesaurus that simulates associate memory in the human brain. An associate network is a graph where the edges represent the relationships among the nodes in the graph. The associate constraint network is the associate network of the terms that are extracted from a parallel corpus with constraints imposed on the nodes of the network. The cross-lingual concept space of an input term in either English or Chinese is generated if the associate constraint network is satisfied. In the following sections, the definitions of node consistency and network satisfaction are provided for the proposed associate constraint network.

## 3.2. Associate constraint network for the generation of a cross-lingual concept space

As illustrated in Fig. 2, the nodes of the associate constraint network $( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ represent the terms extracted from a parallel corpus. n is the number of English and Chinese terms. The values of the nodes are binary: $x _ { i } = \{ 0 , 1 \} . x _ { i } = 1$ if x is a term in the cross-lingual concept space, and $x _ { i } = 0$ if $x _ { i }$ is not a term in the crosslingual concept space.

![](/api/attachments/7V4VYU75/fulltext/images/f4a9b34ac29210dd52c9e53f39d8c7cc217b63fa289ed09fc234f15aa0f2d739.jpg)  
Fig. 2. Associate network of terms extracted from a parallel corpus.

The arcs of the associate network represent the association between the extracted terms.

The constraint on $x _ { j } , c _ { j } ,$ is

$$
x _ {j} = \left\{ \begin{array}{l l} 1, & \text { if } \sum_ {i = 0} ^ {n - 1} W _ {i j} x _ {i} \geq \text { threshold } \\ 0, & \text { if } \sum_ {i = 0} ^ {n - 1} W _ {i j} x _ {i} <   \text { threshold } \end{array} \right.
$$

where the threshold is determined experimentally, $W _ { i j }$ denotes the relevance weight from node i to node j as presented in Eq. (4) and n is the number of nodes in the network.

The generation of the cross-lingual concept space is then formulated as a constraint satisfaction problem. We define the node consistency and network satisfaction as follows.

## Definition 1. (node consistency)

$x _ { j }$ is consistent if and only if $c _ { j }$ is satisfied in the associate constraint network.

## Definition 2. (network satisfaction)

The associate constraint network is satisfied if and only if all of the nodes in the associate constraint network are consistent and $\textstyle \sum _ { j } x _ { j } < C _ { ! }$ , where C is a constant.

The inequality in Definition 2 is used to control the size of the concept space, and C is the upper limit of the size of the concept space.

The associate network structure is built in such a way that the assignment of values to each node (variable) affects the assignment to every other node (variable). The associate constraint network approach consists of binary nodes that are connected by an asymmetric network structure. The connections (arcs) between the nodes (variables) are weighted, and the weights determine the contribution of each node to a node's weighted sum and eventually its assignment. The weight may be considered as fixing a constraint between two nodes i and j. If node j is given the chance to instantiate, then the contribution to its assignment from node i is positive, and this may well serve to bring the weighted sum of j above the threshold and cause its assigned value to be 1. After assigning a value of 1 to a variable, a consistency evaluation technique is applied to the associate constraint network to test the node consistency between the instantiated variables. The assignment of variable x depends on four elements: the assigned value of the other variables $\{ x _ { 1 } , x _ { 2 } , . . . x _ { n } \}$ , the ratio of their weights to the variable $x _ { j } ,$ summation, and the threshold. The objective of the associate constraint network is to determine the highly associated bilingual terms in the cross-lingual concept space that satisfy the constraints that are defined for the network.

## 3.3. Constraint propagation

Most algorithms for solving CSPs search systematically through the possible assignment of values to variables [1] and focus on two categories: lookahead and backtracking. The lookahead approach requires more computation to check whether an infeasible solution will be obtained before assignment is made, and the efficiency of this approach is a major concern. The backtracking approach, however, traces back and identifies other possible solutions when an infeasible solution is obtained during the assignment. In this work, we utilize the backtracking approach.

## 3.3.1. Backtracking, backchecking and backmarking

A constraint satisfaction problem can be solved using the backtracking paradigm (BT), which is the most common algorithm for performing a systematic search. Backtracking incrementally extends a partial solution that specifies consistent values for some of the variables to a complete solution by repeatedly choosing a value for another variable that is consistent with the values in the current partial solution [18].

In the BT method, variables are instantiated sequentially, and as soon as all of the variables that are relevant to a constraint have been instantiated, the validity of the constraint is checked. If a partial solution violates any of the constraints, then backtracking is performed on the most recently instantiated variable for which alternatives are still available. Clearly, whenever a partial instantiation violates a constraint, backtracking can eliminate a subspace from the Cartesian product of all of the variable domains.

However, a simple backtracking algorithm normally suffers from expensive compatibility checks [18]. To shorten the computation time, some improvements over backtracking have been developed to reduce the number of compatibility checks as much as possible. Both backchecking (BC) and its descendent backmarking (BM) are developed for this purpose.

![](/api/attachments/7V4VYU75/fulltext/images/bc91a0a41571f1d1128539ad1a5b366a514db8d4b842b8764882fc5cd5d34ed2.jpg)  
Fig. 3. Display of bilingual concepts after pressing the button ‘Navigate the concept space’.

3.3.1.1. Backchecking. In backchecking, a label is a variable-value pair that represents the assignment of a value to a variable. For example, by,bN denotes the label for assigning the value b to the variable y. $\mathrm { < y } , b \mathrm { > }$ is only meaningful if b is in the domain of y [18]. In considering the label ${ < y , b > }$ , BC checks whether or not the label is compatible with all of the labels that have been committed to so far. $\mathrm { I f } < y , b >$ is found to be incompatible with the label ${ < x , a > }$ , then the BC process will put it in the memory. As long as ${ < x , a > }$ is still committed to, by, $b >$ will not be considered again.

3.3.1.2. Backmarking. Backmarking (BM) is an improvement on backchecking (BC). Similar to BC, it reduces the number of compatibility checks by memorizing every label that is incompatible with the labels that have already been committed to. Furthermore, it avoids repeating compatibility checks that have already been performed and that have succeeded.

For each variable, BM records the highest level to which it last backtracked. The levels are based on the chronological ordering of the variables, which helps BM to avoid repeating compatibility checks that are known to have succeeded or failed. The key is to perform compatibility checks according to the chronological order of the variables — the earlier a label is committed to, the earlier it is checked against the currently considered label [18].

In the cross-lingual concept space problem, we propose a backmarking algorithm to solve the constraint satisfaction problem.

3.3.2. Backmarking (BM) for the associate constraint network in the cross-lingual concept space problem

1. Initialisation. The values of all nodes are initialized to be 0.

$$
x _ {i} (0) = u _ {i}, \quad 0 \leq \mathrm{i} \leq n - 1
$$

$x _ { i } ( t )$ is the value of node i at time $t ,$

$x _ { i } ( t )$ is the output of node i at time $t ,$

$u _ { i }$ indicates a value of node i where $u _ { i }$ can be either 0 or 1,

$u _ { i } = 1$ if $u _ { i }$ represents the input term, otherwise $u _ { i } { = } 0 ,$ , and n is the number of terms in the constraint network,

$S { = } \emptyset$ S is a set of indexes of the potential terms of the concept space and is initialized to $\emptyset$ ,

![](/api/attachments/7V4VYU75/fulltext/images/89455ff64eee528028d0440c56f7f996bb5608ae3aeabe87ef169103174f8838.jpg)  
Fig. 4. Display of the retrieval result after pressing the button ‘Search with concept space’.

![](/api/attachments/7V4VYU75/fulltext/images/b7f9e1aa76527b4de97d72d03ee805a9ce24181c447ee8a03c6172ee8426fde1.jpg)  
Fig. 5. Graphical User Interface for criminal analysis with the aid of the bilingual concept space.

S = S ∪ {i} if the node i is an input term, and $S ^ { \prime } { = } \mathcal { O } \quad S ^ { \prime }$ is a set of indexes for the nodes that cause the infeasible solution.

An infeasible solution is found if $\textstyle \sum _ { i = 0 } ^ { n - 1 } x _ { i } \geq C$ where C is constant.

2. Search for a potential solution.

$$
v _ {j} (t) = \sum_ {i = 0, i \neq j} ^ {n - 1} W _ {i j} x _ {i} (t)
$$

$$
x _ {j ^ {*}} (t) = 1 \text {   where   } j ^ {*} = \arg \max _ {j, j \notin S ^ {\prime}, S} (v _ {j} (t))
$$

$W _ { i j }$ is the relevance weight from node i to node j and n is the number of nodes in the network.

3. Determine whether or not a solution has been found. Check the node consistency for all of the nodes. IF all of the nodes are consistent

$$
\text { IF } \sum_ {j = 0,} ^ {n - 1} x _ {j} <   C
$$

THEN the solution(s) is found

ELSE

$$
x _ {j *} (t) = 0 / / x _ {j} ^ {*} (t)
$$

$$
S ^ {\prime} = S ^ {\prime} \cup \{j ^ {*} \}
$$

go to Process 2 // backtracking is needed ELSE // next iteration

$$
S = S \cup \{j ^ {*} \}
$$

## 4. User interface of the multilingual information extraction system for international crime analysis

We developed a multilingual information extraction system for international crime analysis using the associate constraint network approach. The graphical user interface of the system is presented in Figs. 3–5.

The user enters the keyword of interest in the ‘Query’ text field and then clicks the ‘Navigate the concept space’ button (Fig. 3). The system then conducts the backmarking propagation based on the user query and generates a bilingual concept space. The English and Chinese terms in the bilingual concept space are presented in the text fields beneath. The user may select any of these English and Chinese terms and then click the ‘Search with concept space’ button to search the police press release database with the expanded query, which includes the original query and the selected terms from the bilingual concept space. The ‘Result’ field displays a list of press release articles in both English and Chinese in order of relevance (Fig. 4). The release date of the article is also shown. If the user wishes to read an article, then they may double-click on the title in the ‘Result’ field, and the complete article will be presented in the text field on the right-hand side (Fig. 5).

For example, as illustrated in Fig. 3, the query ‘smuggling’ is submitted. By clicking ‘Navigate the concept space’, the network creates a bilingual concept space with English terms such as ‘vice establishment’, ‘illegal immigration’, ‘drug trafficking’ and ‘anti-piracy parallel operation,’ and Chinese terms such as ‘ (Hong Kong customs), ‘ (anti-piracy parallel operation) and ‘ ’ (piracy activities). By selecting all of the English and Chinese terms in the bilingual concept space and clicking the ‘Search with concept space’ button, a list of articles will be extracted from the database and presented in the text field below the bilingual concept space (Fig. 4). The most relevant articles are “HK and Guangdong Customs combat cross-boundary piracy/ 香港及廣束海關進行雙误行動打擊跨境偷運侵犯版 ”, and “Joint operation to combat organized crime/ ”. Clicking on the fifth article “\$232 million worth of ice seized in HK– Australia joint operation” reveals the complete article in the text field on the right-hand side (Fig. 5).

Alternately, the user can conduct a search without the aid of the bilingual concept space. The user simply enters a keyword in the ‘Query’ field and clicks the button ‘Search without the aid of concept space’. The result will be presented in the lower left text field, but no bilingual concept space will be generated. The system only performs the lexical matching between the keyword in the ‘Query’ field and the words in the documents, and the articles in the result will only include those that contain the same language as the query.

Distribution of size of the cross-lingual concept space as generated by the associate constraint network and the Hopfield network

<table><tr><td rowspan="2">Size of concept space</td><td colspan="2">Hopfield network</td><td colspan="2">Associate constraint network</td></tr><tr><td>Distribution (%)</td><td>Cumulative distribution (%)</td><td>Distribution (%)</td><td>Cumulative distribution (%)</td></tr><tr><td>2</td><td>14.46</td><td>14.46</td><td>13.62</td><td>13.62</td></tr><tr><td>3–5</td><td>26.55</td><td>41.01</td><td>24.32</td><td>37.94</td></tr><tr><td>6–9</td><td>31.25</td><td>72.26</td><td>34.66</td><td>72.6</td></tr><tr><td>10–13</td><td>18.38</td><td>90.64</td><td>19.24</td><td>91.84</td></tr><tr><td>&gt;13</td><td>9.36</td><td>100</td><td>8.16</td><td>100</td></tr></table>

Two-sample t-test of the precision of the Hopfield network and the associate constraint network

<table><tr><td></td><td>Hopfield network</td><td>Associate constraint network</td></tr><tr><td>Average precision</td><td>0.835</td><td>0.891</td></tr><tr><td>Standard deviation</td><td>0.120</td><td>0.086</td></tr><tr><td>Two-tailed P value (n=50)</td><td>0.0001</td><td></td></tr></table>

## 5. Experiments

We conducted an experiment to measure the performance of the associate constraint network approach in generating a cross-lingual concept space and benchmarked it with the previous approach, the Hopfield network.

## 5.1. Experiment testbed

English and Chinese have been used as the official languages in Hong Kong for the purpose of communication between the government and the public since 1974 [23]. The English/Chinese press releases of the Hong Kong police are available through the Web, but are organized in a monolingual sub-tree structure [20]. The alignment technique as described in Section 2.1 is utilized to build a parallel corpus of these documents for this experiment. In this experiment, 2548 pairs of parallel documents were collected. Using the co-occurrence analysis as described Section 2.3, 9222 terms (3635 English terms and 5597 Chinese terms) were extracted. The extracted terms included many social, political and legislative terms and abbreviations, names of government departments and agencies.

## 5.2. Experiment design

Ten subjects were recruited from the Department of Systems Engineering and Engineering Management at the

Two-sample t-test of the recall of the Hopfield network and the associate constraint network

<table><tr><td></td><td>Hopfield network</td><td>Associate constraint network</td></tr><tr><td>Average recall</td><td>0.795</td><td>0.824</td></tr><tr><td>Standard deviation</td><td>0.133</td><td>0.119</td></tr><tr><td>Two-tailed P value (n=50)</td><td>0.0328</td><td></td></tr></table>

Table 4  
Two-sample t-test of the processing times of the Hopfield network and the associate constraint network

<table><tr><td></td><td>Hopfield network</td><td>Associate constraint network</td></tr><tr><td>Average processing time (seconds)</td><td>49</td><td>20</td></tr><tr><td>Standard deviation</td><td>7.09</td><td>1.97</td></tr><tr><td>Two-tailed P value (n=9222)</td><td>&lt;0.0001</td><td></td></tr></table>

Chinese University of Hong Kong to participate in the experiment. Of these 10 subjects, 5 were local students and 5 were students from mainland China. All of them had lived in Hong Kong for more than 1 year. The subjects had sufficient knowledge and experience of both the police system and the living environment of the Hong Kong SAR to evaluate the cross-lingual concept space.

The experiment was divided into two evaluation sessions. In the first session, 50 terms were randomly selected as the inputs for the associate constraint network and the Hopfield network. Each term, together with the terms that were retrieved by the two networks, was presented to the subjects. A small portion of noise terms (10% of the total number of retrieved terms) was added to the concept space to reduce the bias of the subject to the computer-generated result. In addition, the terms that were retrieved by the associate constraint network and the Hopfield network were presented in random order so that the subjects were not able to determine how the terms were generated. The subjects were asked to use their professional knowledge to determine whether the retrieved terms were relevant to the input term. If the direct translation of an input term was found amongst the retrieved terms, then the subjects were asked to make a mark against the term. The concept precision was then computed using the following formulation.

$$
\text { Concept   Precision } = \frac {\text { Number   of   Retrieved   Relevant   Concepts }}{\text { Number   of   Total   Retrieved   Concepts }}
$$

In the second session, 50 terms were randomly selected and presented to the subjects. The subjects were asked to suggest relevant terms according to their experience and knowledge. The concept spaces that were generated by the associate constraint network and the Hopfield network were compared with the suggested terms, and the concept recall was then computed using the following formulation.

$$
\text { Concept   Recall } = \frac {\text { Number   of   Retrieved   Relevant   Concepts }}{\text { Number   of   Total   Relevant   Concepts }}
$$

## 5.3. Granularity of the concept space

Table 1 presents the distribution of size of the crosslingual concept space as generated by the associate constraint network and the Hopfield network using 9222 English and Chinese terms.

Based on the results that are presented in Table 1, the difference between the distribution of size of the crosslingual concept space as generated by the associate constraint network and the Hopfield network is not obvious. The majority of them have 3 to 9 terms retrieved in the cross-lingual concept space.

Input terms that generated over 13 terms in the concept space were usually terms without a specific context. For example, ‘Yau Ma Tei’ is an area in Hong Kong with a high crime rate. The terms in its concept space include ‘cellular phone theft’, ‘drug trafficking’, ‘obscene articles’, ‘traffic accident’, ‘criminal damage’, ‘ ’ (drug trafficking) ‘ ’ (obscene articles), ‘ ’ (criminal damage) and ‘ (cellular phone theft). All of these terms relate to crimes that occurred in Yau Ma Tei.

## 5.4. Experimental results

Tables 2 and 3 show the precision and recall of the cross-lingual concept space as generated by the Hopfield network and the associate constraint network, and the results of two-sample t-tests on the difference in precision and recall between the Hopfield network and the associate constraint network. The associate constraint network has a significantly higher precision at $p { \le } 0 . 0 0 0 1$ and a significantly higher recall at $p { \leq } 0 . 0 4$ than the Hopfield network.

In addition to the measurement of precision and recall, we examined all of the associated concepts that were generated by the associate constraint network and the Hopfield network to measure their translation capability. Of the 9222 test descriptors, direct translations of 92.6% (8540 concepts) were found from the associated concepts using the backmarking algorithm in the associate constraint network. This shows that the concept space that is generated by the associate constraint network approach can effectively recognize the translations of a concept in a parallel corpus. However, only direct translations of 87.7% (8087 concepts) of the test descriptors were found from the associated concepts in the Hopfield network.

The efficiency of the two networks was also examined. As shown in Table 4, the associate constraint network is substantially more efficient than the Hopfield network. The average processing time for the Hopfield network was 49 s and the average processing time for the associate constraint network was 20 s. The associate constraint network is therefore significantly more efficient than the Hopfield network at $p \leq$ 0.0001.

The associate constraint network significantly reduces the processing time for the generation of a crosslingual concept space from a parallel corpus, and also displays better performance in terms of precision and recall than the Hopfield network.

## 5.5. Discussion

A lexical item (word) in a sentence may be represented by a concept in one language [11], where a concept is taken to be a recognizable unit of meaning in any given language [7]. Similarly, a concept that is represented by a single word in one language may be translated into a word, two words, a phrase or even a sentence in another language [7]. A concept in one language can be a broad concept that encompasses certain narrower concepts, and the translation of such a concept may result in an altered concept in another language. In contrast, a narrow concept in one language may be translated as a broader concept in another language. This relationship is known as the generic-specific relationship [11]. For example, the general word ‘ ’ (firearm) is related to be a specific word ‘ ’ (Remington), which is a kind of gun. The word ‘drugs’ can be translated into $\yen 4$ (medicine), but may also refer to $\yen 5$ (dangerous drugs), such as ‘ketamine’ ( ), and therefore conceptual alternation may occur in translation. He [7] explained that conceptual alternation occurs because no two languages are completely isomorphic, different languages may have different domain vocabularies, and some languages are more rhetorical than others. Our automatic cross-lingual concept space construction technique is able to cluster concepts with generic-specific relationships and to identify the correct translation of a concept.

Courtial and Pomian [6] argued that searches which are performed in the realms of science and technology frequently involve the association of concepts that lie outside of the traditional associations that are represented in thesauri. Associative constraint networks extract the concept space of associated terms that would be impossible for humans to find on their own. In earlier research, Lesk [12] found little overlap between term relationships that are generated through term associations and those that are presented in thesauri. Term relationships are especially important for criminal analysis, and the associated concepts in a concept space can therefore provide links about criminals, terrorists, types of crimes, locations of crimes, related weapons, and associated organizations. For example, ‘ ’ (pirated VCDs) is associated with more than 14 concepts, such as obscene materials, money laundering, triad offences and narcotic-related crimes. The identification of the recent trend of selling pirated VCDs may assist in the investigation of complex organized crime and serious triad offences.

## 6. Conclusion

In light of the increasing threat of international crime and terrorism that has occurred as a result of globalisation and rapid changes in technology, information sharing and effective methods for information retrieval of multi-lingual information to evaluate threats and vulnerabilities is vital. To identify and share information on a threat before it causes widespread harm, an intelligent system is required to retrieve relevant information from criminal records and suspect communications. Most of this information is only available in languages other than English, and thus information sharing between different countries gives rise to the challenge of cross-lingual semantic interoperability. The major obstacles to the retrieval of such information are therefore the lack of explicit semantic clustering of relevant information and the limits of conventional keyword-driven search techniques (either full or index-based) [3].

This article presents a cross-lingual concept space approach that uses an associate constraint network. The cross-lingual concept space allows the user to interactively refine a search by selecting concepts that are automatically generated and presented to the user. The approach addresses the relevancy of information, offers the user associative navigation through the information that is embedded in the repository, and enables information retrieval in multiple languages.

We present evidence that the constraint programming approach works well in the construction of the crosslingual concept space, and is more traceable and efficient than the cross-lingual concept space approach that is based on the Hopfield network. The research output consists of a thesaurus-like semantic network that is based on the statistical correlation analysis of semantics embedded in English/Chinese daily press releases that are issued by the Hong Kong Police Department. Such a knowledge base provides a basis for collective action in response to the elusive tactics of global terrorists.

## References

[1] R. Bartak, Theory and practice of constraint propagation, Proceedings of the 3rd Workshop on Constraint Programming for Decision and Control (CPDC2001), Wydavnictvo Pracovni Komputerowej, Gliwice, Poland, June 2001, pp. 7–14.

[2] B. Chellaney, Fighting terrorism in Southern Asia: the lessons of history, International Security 26 (3) (Winter 2001/2002) 94–116.

[3] H. Chen, K.J. Lynch, Automatic construction of networks of concepts characterizing document database, IEEE Transactions on Systems, Man and Cybernetics 22 (5) (1992) 885–902.

[4] H. Chen, T. Ng, J. Martinez, B. Schatz, A concept space approach to addressing the vocabulary problem in scientific information retrieval: an experiment on the Worm Community System, Journal of the American Society for Information Science 48 (1) (1997) 17–31.

[5] L.F. Chien, PAT-Tree-BASED keyword extraction for Chinese information retrieval, Proceedings of ACM SIGIR, Philadelphia, PA, 1997, pp. 50–58.

[6] J.P. Courtial, J. Pomian, A system based on associational logic for the interrogation of databases, Journal of Information Science 13 (1987) 91–97.

[7] S. He, Translingual alteration of conceptual information in medical translation: a cross-language analysis between English and Chinese, Journal of the American Society for Information Science 51 (11) (2000) 1047–1060.

[8] J.J. Hopfield, Neural network and physical systems with collective computational abilities, Proceedings of the National Academy of Sciences of the United States of America 79 (4) (1982) 2554–2558.

[9] J.J. Hopfield, Neurons with graded response have collective computational properties like those of two-state neurons, Proceedings of the National Academy of Sciences of the United States of America 81 (30) (1984) 88–92.

[10] V. Kumar, Algorithms for constraint satisfaction problems: a survey, AI Magazine 13 (1) (1992) 32–44.

[11] M.L. Larson, Meaning-Based Translation: A Guide to Cross-Language Equivalence, University Press of America, Lanham, MD, 1998.

[12] M.E. Lesk, Word–word associations in document retrieval systems, American Documentation 20 (1) (1969) 27–38.

[13] K.W. Li, C.C. Yang, Automatic construction of cross-lingual networks of concepts from the Hong Kong SAR Police Depart ment, Proceedings of the First NSF/NIJ Symposium on Intelligence and Security Informatics (ISI 2003)Tucson, U.S.A., June 2–3, 2003.

[14] K.W. Li, C.C. Yang, Automatic cross-lingual thesaurus generated from the Hong Kong SAR Police Department Web corpus for crime analysis, Journal of the American Society for Information Science and Technology 56 (3) (2005) 272–282.

[15] K.W. Li, C.C. Yang, Conceptual analysis of parallel corpus collected from the Web, Journal of the American Society for Information Science and Technology 57 (5) (2006) 684–696.

[16] D.W. Oard, Alternative approaches for cross-language text retrieval, Proceedings of 1997 AAAI Symposium in Cross-Language Text and Speech Retrieval, AAAI, 1997.

[17] G. Salton, Automatic Text Processing, Reading, Addison-Wesley, MA, 1989.

[18] E. Tsang, Foundations of Constraint Satisfaction, Academic Press, London, 1995.

[19] P. Van Beek, R. Dechter, On the minimality and global consistency of Row–Convex Constraint Networks, Journal of the Association for Computing Machinery 42 (3) (May 1995) 543–561.

[20] C.C. Yang, K.W. Li, Automatic construction of English/Chinese parallel corpora, Journal of the American Society for Information Science and Technology 54 (8) (June 2003) 730–742.

[21] C.C. Yang, K.W. Li, Segmenting Chinese unknown words by heuristic method, Proceedings of the International Conference on Asia Digital Libraries, Malaysia, December 8–11, 2003.

[22] C.C. Yang, K.W. Li, A heuristic method based on statistical approach for Chinese text segmentation, Journal of the American Society for Information Science and Technology 56 (13) (2005) 1428–1447.

[23] C.C. Yang, J. Luk, Automatic generation of English/Chinese thesaurus based on a parallel corpus in law, Journal of the American Society for Information Science and Technology, Special Topic Issue on Web Retrieval and Mining: A Machine Learning Perspective 54 (7) (May 2003) 671–682.

![](/api/attachments/7V4VYU75/fulltext/images/4631c24d20a5c5165b2993da7251e8d34dfe2f6b75ee8fc594bfdf1747aa82e2.jpg)

Christopher C. Yang is an associate professor in the Department of Systems Engineering and Engineering Management at the Chinese University of Hong Kong. He received his B.S., M.S., and Ph.D. in Electrical and Computer Engineering from the University of Arizona. He has also been a faculty member in the Department of Computer Science and Information Systems at the University of Hong Kong and a research scientist in the Department of Management

Information Systems at the University of Arizona. His recent research interests include cross-lingual information retrieval and knowledge management, Web search and mining, security informatics, text summarization, multimedia retrieval, information visualization, digital library, and electronic commerce. He has published over 120 referred journal and conference papers in the Journal of the American Society for Information Science and Technology (JASIST), Decision Support Systems (DSS), IEEE Transactions on Image Processing, IEEE Transactions on Robotics and Automation, IEEE Computer, Information Processing and Management, Journal of Information Science Graphical Models and Image Processing, Optical Engineering Pattern Recognition, International Journal of Electronic Commerce, Applied Artificial Intelligence, IWWWC, SIGIR, ICIS, CIKM, and more. He has edited several special issues on multilingual information systems, knowledge management, and Web mining in JASIST and DSS. He has also frequently served as an invited panelist in the NSF Review Panels in the US. He was the chairman of the Association for Computing Machinery Hong Kong Chapter.

![](/api/attachments/7V4VYU75/fulltext/images/0bac54acfd5b3ae0e4c5179844595f8ce28263e8187127868473dd8cd4f5f4d4.jpg)

Kar Wing Li is currently at the Department of Information Systems, The City University of Hong Kong. Before his career at the Department of Information Systems, he worked as Assistant Professor at the Department of Computing, The Polytechnic University of Hong Kong. He completed his PhD at the Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong. He received his B. Eng. in Information System Engineering

from Imperial College, University of London, U.K. and M.Phil. from the Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong. Before he studied in the Chinese University of Hong Kong, he had worked in different departments of the University of Hong Kong and Hong Kong Polytechnic University as a researcher. His research specialization is in the areas of cross-lingual information retrieval, multimedia information retrieval, digital library, internet information retrieval, knowledge management, machine translation, neural networks and constraint networks. His research has been published in several leading journals such as the Journal of the American Society for Information Science and Technology, Information Processing and Management, and proceedings of international conferences such as ACM/IEEE Joint Conference, WWW, International Conference on Asia Digital Libraries, and others.
