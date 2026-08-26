---
otero_id: 6936
otero_key: "FVMQAF8H"
title: "An adaptive learning to rank algorithm: Learning automata approach"
authors: "Javad Akbari Torkestani"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An adaptive learning to rank algorithm: Learning automata approach

Javad Akbari Torkestani

Department of Computer Engineering, Arak Branch, Islamic Azad University, Arak, Iran

a r t i c l e i n f o

Article history: Received 1 October 2011 Received in revised form 15 May 2012 Accepted 11 August 2012 Available online 21 August 2012

Keyword: Learning to rank Ranking function Learning automata Search engine

## a b s t r a c t

The recent years have witnessed the birth and explosive growth of the web. It is obvious that the exponential growth of the web has made it into a huge interconnected source of information wherein <sup>fi</sup>nding a document without a searching tool is unimaginable. Today's search engines try to provide the most relevant suggestions to the user queries. To do this, different strategies are used to enhance the precision of the information retrieval process. In this paper, a learning method is proposed to rank the web documents in a search engine. The proposed method takes advantage of the user feedback to enhance the precision of the search results. To do so, it uses a learning automata-based approach to train the search engine. In this method, the user feedback is de<sup>fi</sup>ned as its interest to review an item. Within the search results, the document that is visited by the user is more likely relevant to the user query. Therefore, its choice probability must be increased by the learning automaton. By this, the rank of the most relevant documents increases as that of the others decreases. To investigate the ef<sup>fi</sup>ciency of the proposed method, extensive simulation experiment is conducted on well-known data collections. The obtained results show the superiority of the proposed approach over the existing methods in terms of mean average precision, precision at position n, and normalized discount cumulative gain.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Due to the huge amount of information available on the evergrowing World Wide Web, the retrieval process of the relevant information is remarkably hard. This becomes more dif<sup>fi</sup>cult when the same query is utilized by different users for different purposes. Under such circumstances, designing an ef<sup>fi</sup>cient retrieval function and ranking algorithm by which the most relevant results are provided is of the greatest importance. The information retrieval (IR) process in a typical search engine is generally composed of two stages: <sup>fi</sup>nding the potentially relevant documents, and ranking them in descending order of relevance. A relevant document that includes all or some of the search terms is found by intersection of the query and document index. The ranking of a document is computed based on its similarity to the query. Due to the vast amount of information on the web (several billions of documents), the number of results for user's queries may reach hundreds of thousands or even millions, while only the <sup>fi</sup>rst few have the chance to be reviewed by the user. Therefore, designing the ef<sup>fi</sup>cient search algorithms by which the most relevant results are ranked <sup>fi</sup>rst is the challenging issue on which the search engines compete. That is why the details of the internal design of the search engines remain as closely guarded secrets. In addition to the relevance to the query, the popularity of the retrieved results is another issue that is taken into consideration by the search engines [38–40].

The problem of learning to rank arises in many applications such as the design of search engines, information retrieval, recommendation systems and so on. In these applications, the ordering of the documents or recommendations returned to the user is of greater importance than searching them. Designing the ef<sup>fi</sup>cient information retrieval and ranking functions has recently become a research area of growing signi<sup>fi</sup>cance because of the rapid development of the web. Joachims [1] proposed a pair-wise ranking algorithm (hereafter is referred to as SVMRank) to optimize the performance of search engines using the clickthrough data. The idea behind the SVMRank is to formalize the learning to rank as a problem of binary classi<sup>fi</sup>cation on document pairs, and then to solve the classi<sup>fi</sup>cation problem using the support vector machine. The probability of clicking on a link from the presented ranking is directly proportional to the relevance of the link to the query. The probability that the user clicks on a link at rank 1000 is virtually zero even if it is the most relevant document to the query. In this method, the retrieval function is updated in such a way that the links that have the chance to be reviewed by the user to be ranked higher next times. In [2], Salton studied the connection between the content information of a document and its citation information. He showed that the integration of the citation information of the document with the textual information signi<sup>fi</sup>cantly improves the performance of the retrieval function in comparison with those using the content information only.

Pan et al. [3] proposed a learning to rank approach based on combination of document ranks and relevance scores. In [3], learning to rank techniques is generally subdivided into two main groups: pair-wise and list-wise approaches. The authors propose a list-wise performance function called PERF by encoding the relevance scores. They claim that the presented list-wise function is capable of relieving the problems with pair-wise methods. To achieve better results, the proposed performance function is combined with evaluation functions MAP or NDCG yielding PERF-MAP and PERF-NDCG. Experimental results given in [3] show that the ranking algorithm (derived from AdaRank [7]) that uses the hybrid performance functions (PERF-MAP and PERF-NDCG) is superior to AdaRank baselines. Comparing the results of PERF-MAP and PERF-NDCG, it is concluded that PERF-MAP slightly outperforms PERF-NDCG. Therefore, PERF-MAP (hereafter is referred to as LRDRS) is used here as one of our baselines in simulation experiments. A learning to rank technique based on genetic programming approach was proposed by Trotman [4]. In this work, a term-oriented inverted <sup>fi</sup>le information retrieval system is used to identify the relevant documents (which documents contain which terms) and to learn two new general purpose ranking functions. Ailon and Mohri [5] presented an ef<sup>fi</sup>cient preference-based learning to rank algorithm. The proposed model is composed of two stages. In the <sup>fi</sup>rst stage, algorithm learns a preference function de<sup>fi</sup>ned over pairs. It then makes use of the preference function to accurately rank the documents in the second stage. The main idea behind the proposed method is based on a reduction of the learning to rank problem to a binary classi<sup>fi</sup>cation. In [6], Agarwal considered the problem of learning to rank in a graph-based data representation and proposed several algorithms. Ranking algorithms are based on the generalization of the graph regularization concepts for learning the ranking functions on graphs. These algorithms learn a ranking function in a reproducing kernel Hilbert space (RKHS) derived from the graph. Evolutionary algorithms have been shown to be useful in web page classi<sup>fi</sup>cation and ranking [8–11]. Besides the list-wise and pair-wise approaches, the point-wise [40–42] is another learning to rank approach in which a single document is the input of the learning process. In the point-wise approaches, the loss function is de<sup>fi</sup>ned based on the individual documents. Linear Regression (hereafter is referred to as LREG) is a statistical-based point-wise method [41,42]. Linear Regression aims at learning a linear ranking function that maps a feature vector (with multiple items) to a real value [40].

In this paper, a Learning automata-based Ranking algorithm based on User Feedback called LRUF is proposed to rank the web documents. In this method, a learning automaton is responsible for ranking the search results. Each item of the search results is associated with an action of the learning automaton. At each stage, learning automaton randomly chooses one of its actions according to its action probability vector. The web document associated with the selected action at stage k is ranked at the $k ^ { t h }$ position of the <sup>fi</sup>nal ranking. This process continues until no item remains to be ranked. Then, the ranking list is shown to the user. Normally, user chooses the documents that are more relevant to the searched topic. The relevant documents that are selected by the user to review must be shown in a higher rank in the future. To do so, the learning automaton updates its action probability vector by rewarding the actions corresponding to the visited documents. Rewarding increases the choice probability of a document for the next user queries. In the beginning, all actions have the same choice probability. However, as the number of submitted queries increases (or the search engine receives the feedbacks of different users), the proposed ranking method learns how to rank the recommended results so that the most relevant ones are appeared at the top positions of the ranking list as much as possible. The performance of the proposed method is measured through the simulation experiment on several well-known benchmark data collections. The proposed ranking method is compared with those of SVMRank, LREG, and LRDRS, and the obtained results show that it outperforms the others in terms of precision at position n, mean average precision, and normalized discount cumulative gain.

Taking advantage of the variable action-set learning automata, LRUF rewards each reviewed document in the (scaled) list proportional to its list size (that is directly proportional to the relevance degree of the reviewed item) on the basis of the relevancy function given in Eq. (4). That is, a document may be rewarded in comparison with the other non-relevant documents, while it is penalized against a more relevant document too. This mitigates the problem of the previous similar (i.e., user feedback-based) methods with updating the score of the non-relevant documents reviewed by user and the non-visited relevant documents. Therefore, LRUF signi<sup>fi</sup>cantly improves the ranking precision by rewarding and penalizing each document proportional to its relevance degree (choice probability). Furthermore, the proposed ranking rule takes into consideration the position of each document in the ranking list to update its ranking score, while in the previous methods the score of all ranked documents changes (increases or decreases) with the same rate. Therefore, the proposed learning algorithm can be considered as a random direction search with adaptive step size. The proposed method combines the average relevancy function and probability distribution function to collect the most relevant documents on the top positions of the list. Unlike the previous methods, LRUF is order-sensitive. That is, the order in which user visits the ranked documents (i.e., the reviewing behavior of users) in<sup>fl</sup>uences the rate with which the documents' score is updated. This property of the proposed updating rule ranks a document higher than the others, even if its relevance degree is slightly larger. This signi<sup>fi</sup>cantly increases the average precision of LRUF. The rest of the paper is organized as follows. The next section of this paper brie<sup>fl</sup>y reviews the learning automata theory. In Section 3, the learning automata-based ranking method is presented. Section 4 shows the performance of the proposed algorithm through simulation experiments and comparison with the previous methods. Finally, Section 5 concludes the paper.

## 2. Learning automata theory

A learning automaton [27,28] is an adaptive decision-making unit that improves its performance by learning how to choose the optimal action from a <sup>fi</sup>nite set of allowed actions through repeated interactions with a random environment. The action is chosen at random based on a probability distribution kept over the action-set and at each instant the given action is served as the input to the random environment. The environment responds to the taken action in turn with a reinforcement signal. The action probability vector is updated based on the reinforcement feedback from the environment. The objective of a learning automaton is to <sup>fi</sup>nd the optimal action from the action-set so that the average penalty received from the environment is minimized. Learning automata have been found to be useful in systems where incomplete information about the environment exists [29]. Learning automata are also proved to perform well in complex, dynamic and random environments with a large amount of uncertainties. A group of learning automata can cooperate to cope with many hard-to-solve problems. To name just a few, learning automata have a wide variety of applications in combinatorial optimization problems [30,43,50,54], computer networks [31,44–46,48,49,52,55], Grid computing [47,56], Web engineering [51,53], queuing theory [32], signal processing [33], information retrieval [34], adaptive control [35], and pattern recognition [36].

The environment can be described by a triple{α,β,c}, where $\alpha { \equiv } \{ \alpha _ { 1 } , \alpha _ { 2 } , . . . . \alpha _ { \mathrm { r } } \}$ represents the <sup>fi</sup>nite set of the inputs, $\beta \equiv \{ \beta _ { 1 } , \beta _ { 2 } , . . . , \beta _ { m } \}$ denotes the set of the values that can be taken by the reinforcement signal, and $c { \equiv } \{ c _ { 1 } , c _ { 2 } , . . . . , c _ { r } \}$ denotes the set of the penalty probabilities, where the element c is associated with the given action α If the penalty probabilities are constant, the random environment is said to be a stationary random environment, and if they vary with time, the environment is called a non stationary environment. The environments depending on the nature of the reinforcement signal β can be classi<sup>fi</sup>ed into P-model, Q-model and S-model. The environments in which the reinforcement signal can only take two binary values 0 and 1 are referred to as P-model environments. Another class of the environment allows a <sup>fi</sup>nite number of the values in the interval [0, 1] to be taken by the reinforcement signal. Such an environment is referred to as Q-model environment. In S-model environments, the reinforcement signal lies in the interval [a,b].

Learning automata can be classi<sup>fi</sup>ed into two main families [27]: <sup>fi</sup>xed structure learning automata and variable structure learning automata. Variable structure learning automata are represented by a triple ${ < } \beta , \alpha , L >$ , where $\beta$ is the set of inputs, α is the set of actions, and L is learning algorithm. The learning algorithm is a recurrence relation which is used to modify the action probability vector. Let $\alpha _ { i }$ $( k ) \in \alpha$ and $p \left( k \right)$ denote the action selected by learning automaton and the probability vector de<sup>fi</sup>ned over the action set at instant k, respectively. Let a and b denote the reward and penalty parameters and determine the amount of increases and decreases of the action probabilities, respectively. Let r be the number of actions that can be taken by learning automaton. At each instant k, the action probability vector $p \left( k \right)$ is updated by the linear learning algorithm given in Eq. (1), if the selected action α (k) is rewarded by the random environment, and it is updated as given in Eq. (2) if the taken action is penalized.

$$
p _ {j} (k + 1) = \left\{ \begin{array}{l} p _ {j} (k) + a \Big [ 1 - p _ {j} (k) \Big ] j = i \\ (1 - a) p _ {j} (k) \forall j \neq i \end{array} \right.\tag{1}
$$

$$
p _ {j} (k + 1) = \left\{ \begin{array}{l} (1 - b) p _ {j} (k) j = 1 \\ \left(\frac {b}{r - 1}\right) + (1 - b) p _ {j} (k) \forall j \neq i \end{array} \right.\tag{2}
$$

If $a = b ,$ , the recurrence Eqs. (1) and (2) are called linear reward– penalty $\left( L _ { R - P } \right)$ algorithm, if a≫b the given equations are called linear reward– penalty $\left( L _ { R - \in P } \right)$ , and <sup>fi</sup>nally $\operatorname { i f } b = 0$ they are called linear reward–inaction $\left( L _ { R - I } \right)$ . In the latter case, the action probability vectors remain unchanged when the taken action is penalized by the environment.

## 2.1. Variable action-set learning automata

A variable action-set learning automaton is an automaton in which the number of actions available at each instant changes with time. It has been shown in [37] that a learning automaton with a changing number of actions is absolutely expedient and also ∈-optimal, when the reinforcement scheme is $L _ { R - I } .$ Such an automaton has a <sup>fi</sup>nite set of r actions, $\alpha = \{ \alpha _ { 1 } , \alpha _ { 2 } , . . . , \alpha _ { \mathrm { { r } } } \} . \ A = \{ A _ { 1 } , A _ { 2 } , . . . , A _ { m } \}$ denotes the set of action subsets and A (k) α is the subset of all the actions can be chosen by the learning automaton, at each instant $k .$ The selection of the particular action subsets is randomly made by an external agency according to the probability distribution $\Psi \left( k \right) =$ $\smash { \{ \psi _ { 1 } ( k ) , \psi _ { 2 } ( k ) , . . . , \psi _ { m } ( k ) \} }$ de<sup>fi</sup>ned over the possible subsets of the actions, where $\psi _ { i } \left( k \right) = p r o b [ A ( k ) = A _ { i } | A _ { i } \in A , 1 \le i \le 2 ^ { r } - 1 ]$

$\hat { p } _ { i } ( k ) = p r o b [ \alpha ( k ) = \alpha _ { i } | A ( k ) , \alpha _ { i } \in A ( k ) ]$ denotes the probability of <sup>ð Þ ¼</sup>choosing action $\alpha _ { i } ,$ <sup>Þ ¼ j -ð Þ ð Þ</sup>conditioned on the event that the action subset $A ( k )$ has already been selected and $\alpha _ { i } { \in } A \left( k \right)$ too. The scaled probability ${ \hat { p } } _ { i } ( k )$ is de<sup>fi</sup>ned as

$$
\hat {p} _ {i} (k) = \frac {p _ {i} (k)}{K (k)}\tag{3}
$$

where $K ( k ) = \Sigma _ { o i A ( k ) p i } ( k )$ is the sum of the probabilities of the actions in subset $A ( k )$ , and $p _ { i } ( k ) = p r o b [ \alpha ( k ) = \alpha _ { i } ]$ ].

The procedure of choosing an action and updating the action probabilities in a variable action-set learning automaton can be described as follows. Let $A ( k )$ be the action subset selected at instant k. Before choosing an action, the probabilities of all the actions in the selected subset are scaled as de<sup>fi</sup>ned in Eq. (3). The automaton then randomly selects one of its possible actions according to the scaled action probability vector ${ \hat { p } } ( k )$ . Depending on the response received from the environment, the learning automaton updates its scaled action probability vector. Note that the probability of the available actions is only updated. Finally, the probability vector of the actions of the chosen subset is rescaled as $p _ { i } ( k + 1 ) = \hat { p } _ { i } ( k + 1 ) { \cdot } K ( k )$ , for all $\alpha _ { i } { \in } A ( k )$ . The absolute expediency and ε-optimality of the method described above have been proved in [37].

## 3. LRUF: the proposed ranking algorithm

In this section, an adaptive learning automata-based method is proposed to train the search engine for ranking the web documents dependent upon the user feedback. To provide the suf<sup>fi</sup>cient background for understanding the proposed learning to rank technique, some preliminaries must be presented <sup>fi</sup>rst. Therefore, this section is organized as follows. The learning to rank problem is initially introduced. Then, the adaptive con<sup>fi</sup>guration of the learning automaton is discussed. Finally, the learning technique is presented.

## 3.1. Problem statement

The proposed learning to rank method is de<sup>fi</sup>ned as an optimization problem that can be shown by a quintuple $< q _ { i } , A _ { i } , \ \underline { { { d } } } _ { i } , \ \underline { { { R } } } _ { i } , \ \underline { { { f } } } _ { i } > ,$ where $q _ { i }$ denotes the query submitted by the user to the search engine $S , A _ { i }$ is the learning automaton associated with query q , $\underline { { d _ { i } } } = \left\{ d _ { i } ^ { j } | 1 \leq j \leq n _ { i } \right\}$ is the set of n documents listed for query $q _ { i }$ from the search results, $\underline { { R } } _ { i } =$ $\left\{ r _ { i } ^ { j } \middle | \mathrm { f o r } d _ { i } ^ { j } \in \underline { { d _ { i } } } \right\}$ denotes the ranking function that assigns a rank r<sup>j</sup> to each document d<sup>j</sup>, and $\underline { { f } } _ { i }$ is the set of user feedbacks (list of reviewed items) for ranking $R _ { i }$ . Feedback set $\underline { { f } } _ { i } ,$ including the visited web documents, is constructed by observing the clicking behavior of the user. As mentioned earlier, at each stage k (where $1 \leq k \leq n _ { i } )$ , learning automaton $A _ { i }$ chooses one of its actions according to action probability vector $p _ { i } { = } \{ p _ { i } ^ { 1 } , p _ { i } ^ { 2 } , { \ldots } , p _ { i } ^ { n _ { i } } \}$ to form the ranking R . Therefore, ranking R strongly depends on the con<sup>fi</sup>guration of action probability vector $p _ { i \cdot }$ . On the other hand, user feedback $\underline { { f _ { i } } }$ is de<sup>fi</sup>ned based on the relevance of ranking $\underline { { R } } _ { i } .$ Hence, user feedback $\underline { { f _ { i } } }$ and con<sup>fi</sup>guration $p _ { i }$ are mutually independent. In fact, user feedback is served as the input of the learning automaton $A _ { i \cdot }$ The proposed algorithm LRUF aims at converging action probability vector $p _ { i }$ to the optimal con<sup>fi</sup>guration based on user feedback $\underline { { f _ { i } } } .$ . To do so, feedback set $f _ { i }$ must be translated into an understandable value. Let function $g _ { i } : \underline { { f _ { i } } } \to \overline { { \mathbb { R } } } ^ { + }$ be a mapping from the feedback set $\underline { { f } } _ { i }$ into a posi-<sup>―</sup>tive real number $\mathbb { R } ^ { + }$ <sup>―</sup>. This function is de<sup>fi</sup>ned to compute the average relevance score of ranking $\underline { { R _ { i } } }$ based on user feedback $f _ { i }$ as follows:

$$
g _ {i} = \frac {1}{N _ {i}} \sum_ {d _ {i} ^ {j} \in \underline {{f}} _ {i}} a \left(r _ {i} ^ {j}\right) ^ {- 1}\tag{4}
$$

where a is the learning rate, $N _ { i }$ denotes the number of items visited by the user, and $r _ { \ i } ^ { j }$ denotes the rank of document d<sup>j</sup> in $R _ { i }$ which is a positive integer number of $\{ 1 , 2 , . . . , n _ { i } \}$ . In Eq. (4), the score of the top-ranked and the bottom-ranked documents is de<sup>fi</sup>ned as 1 and $n _ { i } ,$ respectively.

Function g represents the average relevance of ranking $R _ { i }$ on the basis of user feedback $\underline { { f _ { i } } } .$ . From the connection between con<sup>fi</sup>guration $p _ { i }$ and user feedback $\underline { { f } } _ { i } ,$ , it follows that con<sup>fi</sup>guration $p _ { i }$ can be optimized based on relevance function $g _ { i } .$ . The learning to rank technique proposed in this paper intends to adjust con<sup>fi</sup>guration $p _ { i }$ in such a way that the relevance level $g _ { i }$ is maximized (the most relevant documents are listed at top <sup>fi</sup>rst positions).

## 3.2. Action-set formation

Before discussing the proposed algorithm, we describe how to form the action-set of learning automaton. Let $A _ { i }$ be the learning automaton corresponding to query q , and $n _ { i }$ denotes the number of items ranked for this query (the size of ranking list). The action-set of learning automaton $\bar { A } _ { i } ( \mathrm { i . e . , } \alpha _ { i } { = } \{ \alpha _ { i } ^ { 1 } , \alpha _ { i } ^ { 2 } , { \ldots } , \alpha _ { i } ^ { \bar { n _ { i } } } \} $ ) includes n distinct actions, each associated with an item of the document set $d _ { i }$ . Obviously, the relevance degree of the search results is unknown a priori for the learning automaton. Therefore, the initial choice probability of every action α<sup>j</sup> $( \mathrm { f o r } j { \in } \{ 1 , 2 , . . . , n _ { i } \} )$ is set to the same value $\scriptstyle { \frac { 1 } { n _ { i } } } .$ That is,

$$
p _ {i} ^ {j} (0) = \frac {1}{n _ {i}}; \text {   for   } j \in \{1, 2,..., n _ {i} \}.\tag{5}
$$

This means that each searched document might be ranked at $n _ { i }$ possible positions of the ranking list with the same probability at <sup>fi</sup>rst. The size of action-set $\alpha _ { i }$ may change for different queries based on the user request. Therefore, to support this dynamic, we take advantage of variable action set learning automat as described in Section 2.1. Let $q _ { i } ^ { t }$ and $q _ { i } ^ { t + 1 }$ be the query q<sub>i</sub> submitted to the search engine S at instant t and $t + 1$ , respectively. Let n<sup>t</sup> and $n _ { i } ^ { t + 1 }$ be the size of action-set $\alpha _ { i }$ at instant t and t+1, respectively, where n<sup>t</sup> $^ { + 1 } > n _ { i } ^ { t } .$ In this case, procedure IAS (short for Increase Action-set Size) given below is called to update the action-set and action probability vector of learning automaton $A _ { i } .$

As shown in Fig. 1, procedure IAS initially adds $( n _ { i } ^ { t + 1 } - n _ { i } ^ { t } )$ actions to the action set $\alpha _ { i } .$ The choice probability of the newly added actions is all set to $\frac { 1 } { n _ { i } ^ { t + 1 } }$ . This is because the new documents extracted from the search results are judged for the <sup>fi</sup>rst time now. The choice probability of the old actions must be also reduced. The second ‘For’ loop shown in lines 05–06 of Fig. 1 decreases the choice probability of the old actions proportional to their values at instant t.

To reduce the number of results $( \mathrm { i . e . , ~ } n _ { i } ^ { t + 1 } < n _ { i } ^ { t } )$ for the next queries, the action-set and the action probability vector of the learning automaton $A _ { i }$ need to be updated by procedure RAS (short for Reduce Action-set Size) shown in Fig. 2. In this procedure, to shorten the ranking list, the set of actions $\{ \alpha _ { i } ^ { j } | n _ { i } ^ { t + 1 } + 1 \le \bar { \mathrm { j } } \le n _ { i } ^ { t } \}$ is <sup>fi</sup>rst removed from the action-set $\alpha _ { i } .$ Then, the total choice probability of the newly removed actions is computed and stored in $\chi .$ Finally, total choice probability $\chi$ must be evenly distributed between the remaining actions proportional to their previous choice probabilities (see lines 07–08 of Fig. 2).

## 3.3. Learning to rank

The proposed learning to rank algorithm is generally subdivided into two main parts. In the <sup>fi</sup>rst part so called ranking process, the search results are classi<sup>fi</sup>ed in descending order of relevance, and in the second one called training process, the ranking algorithm is trained to re<sup>fi</sup>ne the ranking result based on the user feedback.

## 3.3.1. Ranking process

Let us assume that the structures (action-set and action probability vector) of learning automaton $A _ { i }$ are con<sup>fi</sup>gured as discussed in Section 3.2. Once a query $q _ { i }$ is submitted to the search engine S, the learning automaton is activated and sequentially chooses a subset of its possible actions at random. Each action has been already associated with a web document. Therefore, the set of selected actions forms the ranked document set $d _ { i }$ The ranking process is composed of k different stages, where $1 \leq k \leq n _ { i } .$ The following describes the performance of the ranking process at stage k.

At $k ^ { t h }$ stage of the ranking process, learning automaton $A _ { i }$ chooses one of its available actions according to the action probability vector $p _ { i } ( . )$ updated at previous stage $k - 1 .$ . Let $\alpha _ { i } ^ { j } { \in } \alpha _ { i }$ be the action that is selected at this stage. Document d<sup>j</sup> corresponding to the selected action $\alpha _ { i } ^ { j }$ is ranked at the $k ^ { t h }$ position of ranking $R _ { i }$ . Now, for ranking a document at the $k + 1 ^ { t h }$ position, the internal structure of the learning automaton $A _ { i }$ must be updated. To do ${ \bf { S 0 , } }$ the action that learning automaton chooses at stage $k \ ( \mathrm { i } . \mathrm { e } . , \alpha _ { l } ^ { j } )$ must be temporarily removed from the action set $\alpha _ { i }$ as described in Subsection 2.1 on the variable action set learning automata. This is because the documents ranked in the previous stages should not be involved in the ranking process any more. After pruning the action-set of learning automaton, it initiates another stage to choose a document for ranking at $k + 1 ^ { t h }$ position. This process repeats until $n _ { i }$ documents of the search results are ranked in $R _ { i } \ ( \mathrm { i . e . , } \ k = n _ { i } )$ . As k approaches $n _ { i } ,$ the size of action-set $\alpha _ { i }$ becomes smaller. For instance, at last stage $n _ { i } ,$ the cardinality of action-set $\alpha _ { i }$ is one, and the only available option is selected with probability one.

## 3.3.2. Training process

This part aims to improve the performance of the ranking algorithm by updating the state of the learning automaton based on the user feedback. As the input of training part, the result of the ranking process (i.e., ranking $\underline { { R _ { i } } } )$ is given back to the user. User explores the ranking list to <sup>fi</sup>nd the most relevant documents. To construct the user feedback set $\underline { { f _ { i } } } ,$ , the clicking behavior of the user is monitored by the training process until the user query session is expired. Query session is expired, if the user submits another query to the search engine or exits the search engine. User selects to review the more relevant results with a higher probability. Feedback set $\underline { { f _ { i } } }$ includes the list of reviewed document. Users hope to <sup>fi</sup>nd the best results within the <sup>fi</sup>rst few ranks. So, there is no chance to review the bottom-ranked documents, even if they are relevant to the user query. Therefore, a ranking technique becomes popular, if it can assign the proper higher ranks to the more relevant search results. Function $g _ { i }$ introduced in Section 3.1 represents the average relevancy of the ranking $\underline { { R } } _ { i }$ . It is computed based on the user feedback. From Eq. (4), we <sup>fi</sup>nd that g becomes larger as the number of visited top-ranked documents increases. Training process intends to maximize $g _ { i }$ by updating the internal con<sup>fi</sup>guration of learning automaton. After query session is over, the value of g is measured and compared with a dynamic relevance threshold T . T is initially set to zero. If the average relevance score of ranking R is greater than or equal to the dynamic relevance threshold $( \mathrm { i . e . , } g _ { i } \overline { { \geq } } T _ { i } )$ , the actions corresponding to the visited documents are rewarded by Eq. (1), and dynamic threshold T is set to $\cdot g _ { i } .$ Otherwise, the action probability vector remains unchanged. By this, ranking $R _ { i }$ is rewarded by the user, only if it provides more relevant documents than before. This assures that the internal state of learning automaton converges to the optimal con<sup>fi</sup>guration. It should be noted that before updating the probability vector all disabled actions must be enabled again. As the number of times that query $q _ { i }$ is submitted to the search engine increases, the internal state of the learning automaton $A _ { i }$ converges to its optimal con<sup>fi</sup>guration and therefore expected value of g is maximized. Fig. 3 shows the pseudo code of the proposed learning to rank technique.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure IAS
01:Begin Procedure
02:For  $j \leftarrow n_{i}^{t} + 1$  to  $n_{i}^{t+1}$ 
03:  $\underline{\alpha_{i}} \leftarrow \underline{\alpha_{i}} + \{\alpha_{i}^{j}\}$ 
04:  $p_{i}^{j}(t + 1) \leftarrow \frac{1}{n_{i}^{t+1}}$ 
05: For  $j \leftarrow 1$  to  $n_{i}^{t}$ 
06:  $p_{i}^{j}(t + 1) \leftarrow \frac{n_{i}^{t}}{n_{i}^{t+1}} \cdot p_{j}^{i}(t)$
</div>

Fig. 1. Pseudo code of IAS.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure RAS
01:Begin Procedure
02:For  $j \leftarrow n_{i}^{t+1} + 1$  to  $n_{i}^{t}$ 
03:  $\underline{\alpha_{i}} \leftarrow \underline{\alpha_{i}} - \{\alpha_{i}^{j}\}$ 
04:  $\chi \leftarrow 0$ 
05: For  $j \leftarrow n_{i}^{t+1} + 1$  to  $n_{i}^{t}$ 
06:  $\chi \leftarrow \chi + p_{i}^{j}(t)$ 
07: For j = 1 to  $n_{i}^{t+1}$ 
08:  $p_{i}^{j}(t + 1) \leftarrow p_{i}^{j}(t) \cdot (1 + \frac{\chi}{1 - \chi})$
</div>

Fig. 2. Pseudo code of RAS.

Obviously, the non-relevant documents receive no attention from the users. This causes the choice probability of these documents to gradually converge to zero (i.e., is less than very small threshold $T _ { \varepsilon } )$ LRUF ranks these documents at the end of the list, while there are a number of relevant documents within the searched results for query $q _ { i \cdot }$ To improve the performance of information retrieval process, the proposed ranking algorithm replaces the non-relevant documents with new ones. To do this, after updating the state of learning automaton $A _ { i } ,$ the action-set $\alpha _ { i }$ is checked to see if there is an action whose choice probability is less than threshold $T _ { \varepsilon \cdot }$ If $s 0 ,$ , the document associated with this action is removed from the document set $\underline { { d _ { i } } }$ and replaced with another document of the search list that has not been already included in $d _ { i } .$ To replace a document with a new one, procedure RAS given in Fig. 2 is <sup>fi</sup>rst called to remove the non-relevant document (with a probability less than threshold $T _ { \varepsilon } )$ from the list and to

## 4. Numerical results

update the action probability vector accordingly. Then, procedure IAS given in Fig. 1 is called to add the document (not have been already in the ranking) with the highest choice probability from the search results (see lines 28–30 of Fig. 3) to the ranked list.

To investigate the performance and correctness of the proposed learning to rank algorithm, we have conducted several simulation experiments on the renowned benchmark data collections. To show the superiority of the proposed method, the obtained results are compared with those of the following three baselines: SVMRank, LREG, and LRDRS. Experiments are conducted in three different groups to measure three metrics of interest. The <sup>fi</sup>rst group aims to measure the precision at position n of each algorithm, and the second one is concerned with investigating the accuracy in terms of mean average precision. The last group of experiments measures the normalized discount cumulative gain. The datasets on which the performance of the proposed algorithm and the baselines are tested are TREC 2003 (Topic Distillation, TD2003), TREC 2004 (Topic Distillation, TD2004), OHSUMED, and MQ2007. In what follows, we <sup>fi</sup>rst introduce our metrics of interest and descriptions of data collections. Then, the simulation scenarios and the obtained results are discussed.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm LRUF
01:Input Query $q_i$, Number of results $n_i$
02:Output Ranking $\underline{R_i}$
03:Assumption
04: Let $A_i$ be the learning automaton corresponding to query $q_i$ with action-set $\alpha_i$
05: Action $\alpha_i^j \in \alpha_i$ is associated with document $d_i^j \in \underline{d_i}$
06: Let $k$ denotes the stage number
07: Let $G$ be the total relevance score
08:Begin Algorithm
09: $\bar{k} \leftarrow 1, T_i \leftarrow 0$
10: While $k \leq n_i$
11: $\bar{A}_i$ randomly chooses one of its actions (e.g., $\alpha_i^j$) at random
12: Document $d_i^j$ corresponding to selected action $\alpha_i^j$ is ranked at $k^{th}$ position of $\underline{R_i}$
13: Configuration of $A_i$ is updated by disabling action $\alpha_i^j$
14: $k \leftarrow k + 1$
15: Ranking $R_i$ is shown to the user
16: $N_i \leftarrow 0, \underline{f_i} \leftarrow \emptyset, G \leftarrow 0$
17: Repeat
18: For every document $d_i^j$ visited by user
19: $\underline{f_i} \leftarrow \underline{f_i} + \{d_i^j\}$
20: $G \leftarrow G + a \cdot (r_i^j)^{-1}$
21: $N_i \leftarrow N_i + 1$
22: Until query session is expired
23: $g_i \leftarrow \frac{G}{N_i}$
24: Configuration of $A_i$ is updated by re-enabling all disabled actions
25: If $g_i \geq T_i$ Then
26: Reward the actions corresponding to all visited documents by Equation (1)
27: $T_i \leftarrow g_i$
28: For all $\alpha_i^j \in \underline{\alpha_i}$
29: If $p_i^j &lt; T_\varepsilon$ Then
30: $d_i^j$ is replaced with another document of the searched results
</div>

Fig. 3. Pseudo code of LRUF.

## 4.1. Evaluation metrics

Our metrics of interest are precision at position n (P@n), mean average precision (MAP), and normalized discount cumulative gain (NDCG) which are widely used in information retrieval. These metrics are supported by the set of evaluation tools provided by LETOR team [21]. By using this set of evaluation tools, the experimental results of different IR methods can be easily and impartially compared. That is why we choose these metrics to evaluate the performance of the proposed algorithm.

## 4.1.1. Precision at position n (P@n) [26]

This metric is de<sup>fi</sup>ned as the number of relevant documents listed in the <sup>fi</sup>rst n positions of the <sup>fi</sup>nal ranking. That is, this metric measures the relevance of the top n documents in the <sup>fi</sup>nal ranking for a given query. For a given query q, precision at position n (P@n) is formulated as

$$
P @ n = \frac {N o R _ {n}}{n}\tag{6}
$$

where NoR denotes the number of relevant documents listed within the top n positions of the <sup>fi</sup>nal ranking. Let us assume that the top 10 documents returned by the ranking method for a given query are {r,i,i,r,r,r,i,i,r,r}, where r and i denote the relevant and irrelevant documents, respectively. The values of P@1 through P@10 will be $\{ \frac { 1 } { 1 } , \ \frac { 1 } { 2 } , \frac { 1 } { 3 } , \frac { 2 } { 4 } , \frac { 3 } { 5 } , \frac { 4 } { 6 } , \frac { \hat { 4 } } { 7 } , \frac { 4 } { 8 } , \frac { 5 } { 9 } , \frac { 6 } { 1 0 } \}$ respectively.

## 4.1.2. Mean average precision (MAP) [26]

For a single query, the average precision (AP) is de<sup>fi</sup>ned as the average of the P@n values for all relevant documents as follows

$$
A P = \frac {\sum_ {n = 1} ^ {N} (P @ n \cdot R _ {e} (n))}{T _ {R}}\tag{7}
$$

where N denotes the number of retrieved documents, $T _ { R }$ denotes the total number of relevant documents, and $R _ { e } ( n )$ is a binary function specifying the relevance of $n ^ { t h }$ document. $R _ { e } ( n )$ is de<sup>fi</sup>ned as

$$
R _ {e} (n) = \left\{ \begin{array}{l l} 1 & ; \quad \text {   if   the   } n ^ {t h} \text {   document   is   relevant   }. \\ 0 & ; \quad \text {   otherwise   } \end{array} \right.\tag{8}
$$

Mean average precision (MAP) [26] is de<sup>fi</sup>ned as the average of the $A P$ values of all submitted queries. It can be seen that P@n and MAP can be used to measure the precision, only when the relevance judgments are of binary representation, relevant (1) or irrelevant (0). NDCG is another metric that can deal with the cases where the relevance judgment has multiple values.

## 4.1.3. Normalized discount cumulative gain (NDCG) [24,25]

The NDCG value of a ranking list at position n is de<sup>fi</sup>ned as follows

$$
\mathrm{NDCG} \equiv Z _ {n} \sum_ {m = 1} ^ {N} \frac {2 ^ {r (m)} - 1}{\log (m + 1)}\tag{9}
$$

where r(m) denotes the relevance rate of $m ^ { t h }$ document in the ranking list, and $Z _ { n }$ is the normalization constant. $Z _ { n }$ must be chosen in such a way that the perfect list gets a NDCG score of 1. To calculate the NDCG scores, the relevance rate of each document must be speci<sup>fi</sup>ed. For TREC 2003 and TREC 2004, the relevance rate is de<sup>fi</sup>ned as a binary function that returns 0 and 1 for “irrelevant” and “relevant” documents, respectively. For OHSUMED, it is de<sup>fi</sup>ned in three levels 0, 1, and 2 corresponding to “not relevant”, “partially relevant”, and “de<sup>fi</sup>nitely relevant”, respectively [12]. In Eq. $( 9 ) , 2 ^ { r ( m ) } - 1$ denotes the gain of $m ^ { t h }$ document, $2 ^ { r ( m ) } - 1 / \log ( m + 1 )$ is the discounted gain, $\sum _ { m = 1 } ^ { N } \Big [ 2 ^ { r ( m ) } - 1 / \log ( m + 1 ) \Big ]$ is the discounted cumulative gain at position <sup>¼</sup>n of the list, and <sup>fi</sup>nally $\bar { Z } _ { n } \sum _ { m = 1 } ^ { N } \left[ 2 ^ { r ( m ) } - 1 / \log ( m + 1 ) \right]$ denotes the normalized discounted cumulative gain at position n of the list.

## 4.2. Data collections

We conducted our simulation experiments on well-known data collections LETOR [21]. LETOR is a package of benchmark data sets for LEarning TO Rank released by Microsoft Research Asia including standard features, relevance judgments, data partitioning, evaluation tools, and several baselines [21]. LETOR team extracted totally 44 features for the query–document pair that cover most of the standard features required for information retrieval. In [12], Liu et al. classi<sup>fi</sup>ed these features as low-level content features (e.g., term frequency, normalized term of frequency, inverse document frequency, document length, and their combinations), high-level content features such as outputs of BM25 [13] (e.g., BM25 of title, BM25 of anchor) and LMIR [14] (e.g., LMIR.DIR of anchor, LMIR.JM of anchor, LMIR.ABS of extracted title), hyperlink features (e.g., PageRank [15], HITS authority [16], HITS hub [16], HostRank [17], topical PageRank [18], topical HITS authority [18], and topic HITS hub [18]), and hybrid features as combination of content-based and hyperlink-based features (e.g., sitemap based feature propagation [19], hyperlink-based score propagation [20], and so on). LETOR 2.0 includes three text retrieval datasets named TREC 2003, TREC 2004, and OHSUMED. TREC (Text Retrieva Conference) was started in 1992 as part of the TIPSTER Text program. The goal of TREC is to develop the research in the <sup>fi</sup>eld of information retrieval by providing the infrastructure required for large-scale evaluation of text retrieval methodologies. TREC datasets [22] include the documents evolved from a crawl of the .gov web sites in January 2002 [12]. TREC collection includes 1,053,110 html documents in this col lection, together with 11,164,829 hyperlinks. There exist 50 queries and 75 queries in TREC 2003 and TREC 2004, respectively. TREC data sets, the relevance judgment for each query–document pair is showed in a binary representation form (1 for relevant and 0 for irrelevant) The OHSUMED collection [23] is a subset of MEDLINE, a well-known database on medical publications. This collection consists of 106 queries with 25 features. Each query is about a medical search associated with the patient and topic information OHSUMED collection includes 348,566 records extracted from 270 medical journals during the period of 1987–1991. Each record is composed of title, abstract, author, source publication type, and MeSH indexing terms [12]. The relevance degree of each query-document pair is judged as definitely relevant, partially relevant, or not relevant. LETOR 4.0 contains 8 datasets for four differen ranking settings (supervised ranking, semi-supervised ranking, rank aggregation, and list-wise ranking) derived from the two Million Query (MQ) track sets of TREC 2007 and TREC 2008 called MQ2007 and MQ2008 [21]. MQ2007 and MQ2008 include about 1700 and 800 queries with labeled documents, respectively. LETOR 4.0 uses the Gov2 web page collection. To conduct a <sup>fi</sup>ve-fold cross validation, these data collections are partitioned into <sup>fi</sup>ve subsets $S _ { 1 } , S _ { 2 } , S _ { 3 } , S _ { 4 }$ and $S _ { 5 } .$ Each fold uses three subsets for training, one for validation, and the remaining one for testing. In this paper, we use the training set to learn the proposed model. Validation set is used to tune the parameters of the learning automaton, and experimental results are averaged over testing set of all <sup>fi</sup>ve folds to conduct a <sup>fi</sup>ve-fold cross validation.

## 4.3. Simulation scenarios

For these experiments, the proposed algorithm is calibrated as follows: Needless to say, the performance of the proposed algorithm strongly depends on the learning rate a. By the proper choice of the learning rate, a good trade-off between the computational cost of the algorithm and its precision (i.e., gap to the optimal ranking) can be made. The computational cost of the algorithm is inversely proportional and its gap to the optimal ranking is directly proportional to the learning rate. In this section, several experiments are performed to adjust the learning rate so as to achieve a compromise between the cost and precision of the algorithm. In these experiments, the learning rate changes from 0.04 to 0.4. The obtained results show that for the learning rates larger than 0.10 the precision of the algorithm signi<sup>fi</sup>cantly degrades. On the other side, for the learning rates smaller than 0.060 the computational cost of the algorithm becomes signi<sup>fi</sup>cant. The numerical results con<sup>fi</sup>rm that a good trade-off between the cost and precision of the algorithm is made when the learning rate is set to 0.085. Threshold $T _ { \varepsilon }$ is another parameter that must be tuned. Obviously, the replacement probability of a relevant document increases, and so the average ranking precision may reduce, as threshold $T _ { \varepsilon }$ increases. On the other hand, a non-relevant document is kept within the ranking list for a long time (and this may also reduce the average ranking precision) if $T _ { \varepsilon }$ is set to a very close-to-zero number. To tune parameter $T _ { \varepsilon } ,$ the average precision of the <sup>fi</sup>nal ranking is measured where $T _ { \varepsilon }$ changes from 0.001 to 0.01. The obtained results show that no signi<sup>fi</sup>cant changes can be seen for values of $T _ { \varepsilon }$ between 0.004 and 0.007. The results also show that the average precision starts being reduced for the values larger than 0.007 and smaller than 0.003. Therefore, threshold $T _ { \varepsilon }$ is set to 0.005 in these experiments. Since all the metrics of interest, i.e., P@n, AP, and NDCG@n, are measured for n(=10) top-ranked documents, the ranking set size $n _ { i }$ is set to 10 for all the user queries.

Table 1 P@n for TD2003.

<table><tr><td>n</td><td>SVMRank</td><td>LRDRS</td><td>LREG</td><td>LRUF</td></tr><tr><td>1</td><td>0.320</td><td>0.331</td><td>0.320</td><td>0.494</td></tr><tr><td>2</td><td>0.310</td><td>0.317</td><td>0.300</td><td>0.482</td></tr><tr><td>3</td><td>0.293</td><td>0.309</td><td>0.260</td><td>0.465</td></tr><tr><td>4</td><td>0.285</td><td>0.301</td><td>0.245</td><td>0.402</td></tr><tr><td>5</td><td>0.276</td><td>0.289</td><td>0.216</td><td>0.395</td></tr><tr><td>6</td><td>0.250</td><td>0.283</td><td>0.213</td><td>0.371</td></tr><tr><td>7</td><td>0.222</td><td>0.245</td><td>0.205</td><td>0.360</td></tr><tr><td>8</td><td>0.207</td><td>0.237</td><td>0.195</td><td>0.349</td></tr><tr><td>9</td><td>0.200</td><td>0.220</td><td>0.184</td><td>0.345</td></tr><tr><td>10</td><td>0.188</td><td>0.216</td><td>0.178</td><td>0.341</td></tr></table>

The proposed algorithm uses the relevance judgment for each query–document pair of the training set as the user feedback. To make the evaluation and comparison fair, the relevance degree of the ranking results is judged by the evaluation tools of the package provided by Microsoft research web site (LETOR) [21]. These tools have been written in perl, and evaluate the P@n, MAP and NDCG of the ranking results of a given ranking algorithm. In these experiments, we use “Eval-Rank.pl” tool to evaluate the ranking results. This tool gets two inputs: the <sup>fi</sup>rst input parameter is the relevance information of the testset on which the experiment is conducted, and the second one is the rank positions given by the ranking algorithm. For LRUF, the second input is the output of the <sup>fi</sup>rst part (i.e., ranking process). The output <sup>fi</sup>le of the evaluation tool includes the evaluation results of P@n, MAP and NDCG.

Table 2 P@n for TD2004.

<table><tr><td>n</td><td>SVMRank</td><td>LRDRS</td><td>LREG</td><td>LRUF</td></tr><tr><td>1</td><td>0.413</td><td>0.451</td><td>0.360</td><td>0.532</td></tr><tr><td>2</td><td>0.346</td><td>0.407</td><td>0.340</td><td>0.521</td></tr><tr><td>3</td><td>0.346</td><td>0.382</td><td>0.333</td><td>0.510</td></tr><tr><td>4</td><td>0.333</td><td>0.351</td><td>0.320</td><td>0.498</td></tr><tr><td>5</td><td>0.301</td><td>0.312</td><td>0.312</td><td>0.480</td></tr><tr><td>6</td><td>0.286</td><td>0.302</td><td>0.286</td><td>0.454</td></tr><tr><td>7</td><td>0.280</td><td>0.293</td><td>0.270</td><td>0.442</td></tr><tr><td>8</td><td>0.266</td><td>0.282</td><td>0.268</td><td>0.437</td></tr><tr><td>9</td><td>0.254</td><td>0.270</td><td>0.259</td><td>0.430</td></tr><tr><td>10</td><td>0.252</td><td>0.265</td><td>0.249</td><td>0.421</td></tr></table>

Table 3 P@n for OHSUMED.

<table><tr><td>n</td><td>SVMRank</td><td>LRDRS</td><td>LREG</td><td>LRUF</td></tr><tr><td>1</td><td>0.597</td><td>0.621</td><td>0.596</td><td>0.656</td></tr><tr><td>2</td><td>0.549</td><td>0.610</td><td>0.600</td><td>0.642</td></tr><tr><td>3</td><td>0.542</td><td>0.590</td><td>0.576</td><td>0.637</td></tr><tr><td>4</td><td>0.544</td><td>0.582</td><td>0.560</td><td>0.629</td></tr><tr><td>5</td><td>0.531</td><td>0.570</td><td>0.533</td><td>0.611</td></tr><tr><td>6</td><td>0.525</td><td>0.551</td><td>0.504</td><td>0.599</td></tr><tr><td>7</td><td>0.509</td><td>0.536</td><td>0.500</td><td>0.589</td></tr><tr><td>8</td><td>0.493</td><td>0.520</td><td>0.483</td><td>0.574</td></tr><tr><td>9</td><td>0.492</td><td>0.501</td><td>0.475</td><td>0.563</td></tr><tr><td>10</td><td>0.486</td><td>0.491</td><td>0.466</td><td>0.540</td></tr></table>

## 4.3.1. Experiment I

This set of simulation experiments is conducted to measure the accuracy of the ranking algorithms in terms of precision at position n, where n ranges from 1 to 10. This metric judges the number of relevant documents that are listed in the top n positions of the ranking. The obtained results of the proposed algorithm are summarized in Tables 1, 2, 3, and 4 in comparison with those of SVMRank, LRDRS, and LREG. Table 1 shows the obtained results for different ranking algorithms on dataset TD2003. Comparing the results given in this table, it is found that the proposed ranking algorithm, LRUF, signi<sup>fi</sup>- cantly outperforms the other methods. This is due to the fact that LRUF combines both user feedback and learning technique to <sup>fi</sup>nd the best ranking function. The obtained results also con<sup>fi</sup>rm that LRDRS is slightly superior to the pair-wise SVMRank. This can be due to the higher precision of the list-wise performance function used in LRDRS in comparison with the clickthrough data technique of the pair-wise SVMRank. The results summarized in Table 1 show that the point-wise ranking algorithm, LREG, lags far behind the list-wise and pair-wise algorithms in almost all cases. For all algorithms, it can be seen that the accuracy decreases as the number of positions n increases. This property of the ranking algorithm is arisen from the interest of the users to <sup>fi</sup>nd the most relevant documents within the top (<sup>fi</sup>rst few) ranking positions. That is, a ranking algorithm performs better, if it can rank the most relevant documents at the highest positions. Tables 2, 3, and 4 show the accuracy (at position) of the ranking algorithms on datasets TD2004, OHSUMED, and MQ2007, respectively. The results summarized in these three tables conform to the results given in Table 1 and show the superiority of the proposed ranking technique over the others. For the OHSUMED data collection, it can be seen that the precision of LREG is higher than that of SVMRank at the <sup>fi</sup>rst <sup>fi</sup>ve ranking positions (n≤5). Comparing the accuracy rate on OHSUMED data collection with that on the other two datasets, it can be seen that all ranking algorithms perform better on OHSUMED. This seems to be due to the nature of the datasets and the pertinence of the provided features to the user queries. The results summarized in Table 4 on MQ2007 dataset reveal that the precision of LRDRS at the top-ranked positions is considerably higher than that of SVMRank and LREG. The gap between LRDRS, SVMRank, and LREG reduces as the number of rank positions (n) increases.

Table 4  
P@n for MQ2007.

<table><tr><td>n</td><td>SVMRank</td><td>LRDRS</td><td>LREG</td><td>LRUF</td></tr><tr><td>1</td><td>0.474</td><td>0.522</td><td>0.441</td><td>0.575</td></tr><tr><td>2</td><td>0.449</td><td>0.508</td><td>0.423</td><td>0.570</td></tr><tr><td>3</td><td>0.431</td><td>0.489</td><td>0.410</td><td>0.552</td></tr><tr><td>4</td><td>0.419</td><td>0.490</td><td>0.402</td><td>0.558</td></tr><tr><td>5</td><td>0.413</td><td>0.463</td><td>0.393</td><td>0.547</td></tr><tr><td>6</td><td>0.404</td><td>0.446</td><td>0.389</td><td>0.532</td></tr><tr><td>7</td><td>0.399</td><td>0.419</td><td>0.378</td><td>0.526</td></tr><tr><td>8</td><td>0.393</td><td>0.411</td><td>0.381</td><td>0.519</td></tr><tr><td>9</td><td>0.386</td><td>0.407</td><td>0.375</td><td>0.508</td></tr><tr><td>10</td><td>0.383</td><td>0.412</td><td>0.368</td><td>0.501</td></tr></table>

Table 5  
Mean average precision (MAP).

<table><tr><td>Dataset</td><td>SVMRank</td><td>LRDRS</td><td>LREG</td><td>LRUF</td></tr><tr><td>TD2003</td><td>0.262</td><td>0.335</td><td>0.240</td><td>0.390</td></tr><tr><td>TD2004</td><td>0.223</td><td>0.307</td><td>0.207</td><td>0.347</td></tr><tr><td>OHSUMED</td><td>0.433</td><td>0.481</td><td>0.422</td><td>0.565</td></tr><tr><td>MQ2007</td><td>0.464</td><td>0.456</td><td>0.396</td><td>0.538</td></tr></table>

## 4.3.2. Experiment II

The aim of this set of simulation experiments is to investigate the accuracy of the ranking algorithms in terms of the mean average precision (MAP). In this experiment, the number of retrieved documents N is <sup>fi</sup>xed at 10. Algorithms are tested on four datasets TD2003, TD2004, OHSUMED, and MQ2007. The results are averaged over the testing set of all <sup>fi</sup>ve folds of the datasets. Table 5 shows the comparison of the results of the proposed ranking function with those of SVMRank, LRDRS, and LREG. From the results given in Table 5, it is observed that the proposed algorithm signi<sup>fi</sup>cantly outperforms the other ranking methods for all four datasets. LRDRS is ranked below LRUF. LREG has the worst results and SVMRank slightly performs better than LREG. The outperformance of LRUF is revealed more when the number of queries that are submitted to the search engine increases, speci<sup>fi</sup>cally for small learning rates. This is because the small learning rate and the large number of queries lead the internal state of the learning automaton to the optimal con<sup>fi</sup>guration by which the best ranking function is generated. Numerical results also show that mean average precision of LRDRS is meaningfully higher than that of SVMRank. Comparing the results of the conducted experiments on TD2003, TD2004, and OHSUMED, it is found that the mean average precision is signi<sup>fi</sup>- cantly higher (lower) for dataset OHSUMED (TD2004). One of the advantages of the proposed ranking algorithm is highly adaptation to the user and environment dynamics. When the popularity of a document (or a set of documents) varies over time, its penalty probability changes and so the learning automaton is led to the new optimal con<sup>fi</sup>guration that generates the ranking with the highest relevancy to the most recent requirements of the user.

## 4.3.3. Experiment III

This set of simulation experiments is conducted to evaluate the performance of the proposed ranking algorithm in terms of the normalized discount cumulative gain (NDCG) as compared to SVMRank, LREG, and LRDRS. In this experiment, all ranking algorithms are tested on datasets TD2003, TD2004, OHSUMED, and MQ2007. The obtained results are summarized in Tables 6, 7, 8 and 9, respectively. For TREC datasets (TD2003, TD2004), the relevance of a document is judged at two levels 0 and 1 corresponding to “irrelevant” and “relevant” documents, respectively. It is de<sup>fi</sup>ned in three levels 0, 1, and 2 corresponding to “not relevant”, “partially relevant”, and “de<sup>fi</sup>nitely relevant” for OHSUMED and MQ2007. For almost all algorithms and all datasets, numerical results show that NDCG is inversely proportional to the number of positions and decreases as n increases from 1 to 10. As mentioned earlier, this is because all ranking functions aim to list the most relevant documents at the highest positions of the ranking list. Unlike TD2003, for TD2004 and OHSUMED, the NDCG of SVMRank decreases as n increases. For the proposed ranking algorithm, the obtained results show that the NDCG is inversely proportional to the number ranking positions. Comparing the results given in all four Tables 6, 7, 8, and 9, it is obvious that the proposed algorithm, LRUF, meaningfully outperforms the other methods in terms of NDCG. For each submitted query, LRUF updates the internal state of the learning automaton based on the user feedback in such a way that the reward given to (or the average relevance score of) the ranking increases for the next queries. Therefore, the accuracy of the results of LRUF increases as the number of submitted queries increases. Numerical results reveal that LRDRS lags far behind the proposed algorithm. From Tables 6, 7, 8, and 9, it can be seen that NDCG of the pair-wise SVMRank is very close to (and in most cases larger than) that of the point-wise LREG algorithm. Comparing the results, it is observed that the gap between different algorithms for the top-ranked positions is more signi<sup>fi</sup>cant. The gap between the precision of the algorithms is reversely proportional to the number of ranking positions. Therefore, the superiority of an algorithm is judged based on the precision of the top-ranked documents. For TD2003, TD2004, and MQ2007, SVMRank outperforms LREG, while for the OHSUMED dataset LREG performs better.

Table 6 NDCG@n for TD2003.

<table><tr><td>n</td><td>SVMRank</td><td>LRDRS</td><td>LREG</td><td>LRUF</td></tr><tr><td>1</td><td>0.320</td><td>0.380</td><td>0.320</td><td>0.551</td></tr><tr><td>2</td><td>0.330</td><td>0.307</td><td>0.320</td><td>0.542</td></tr><tr><td>3</td><td>0.344</td><td>0.283</td><td>0.307</td><td>0.512</td></tr><tr><td>4</td><td>0.353</td><td>0.276</td><td>0.308</td><td>0.501</td></tr><tr><td>5</td><td>0.362</td><td>0.260</td><td>0.298</td><td>0.481</td></tr><tr><td>6</td><td>0.355</td><td>0.265</td><td>0.311</td><td>0.479</td></tr><tr><td>7</td><td>0.346</td><td>0.257</td><td>0.315</td><td>0.467</td></tr><tr><td>8</td><td>0.344</td><td>0.258</td><td>0.323</td><td>0.455</td></tr><tr><td>9</td><td>0.345</td><td>0.251</td><td>0.325</td><td>0.449</td></tr><tr><td>10</td><td>0.346</td><td>0.249</td><td>0.326</td><td>0.441</td></tr></table>

Table 7 NDCG@n for TD2004.

<table><tr><td>n</td><td>SVMRank</td><td>LRDRS</td><td>LREG</td><td>LRUF</td></tr><tr><td>1</td><td>0.413</td><td>0.496</td><td>0.360</td><td>0.582</td></tr><tr><td>2</td><td>0.346</td><td>0.427</td><td>0.340</td><td>0.560</td></tr><tr><td>3</td><td>0.346</td><td>0.405</td><td>0.335</td><td>0.552</td></tr><tr><td>4</td><td>0.341</td><td>0.412</td><td>0.328</td><td>0.547</td></tr><tr><td>5</td><td>0.324</td><td>0.405</td><td>0.325</td><td>0.543</td></tr><tr><td>6</td><td>0.318</td><td>0.409</td><td>0.313</td><td>0.529</td></tr><tr><td>7</td><td>0.315</td><td>0.402</td><td>0.307</td><td>0.525</td></tr><tr><td>8</td><td>0.310</td><td>0.405</td><td>0.308</td><td>0.511</td></tr><tr><td>9</td><td>0.306</td><td>0.398</td><td>0.306</td><td>0.509</td></tr><tr><td>10</td><td>0.307</td><td>0.390</td><td>0.303</td><td>0.503</td></tr></table>

## 5. Conclusion

In this paper, we proposed a learning automata-based ranking algorithm in which the user feedback is used as the environment response to train the learning automaton. In the proposed method, a learning automaton is responsible for ranking the search results. The action-set of learning automaton includes the set of searched results. For each query, the number of actions is determined based on the user request. After generating a ranking list, the user feedback is collected. User feedback is de<sup>fi</sup>ned as the attempt of the user to review a document. User feedback information is achieved from the user clicking behavior. Based on the user feedback, the relevance level of the ranking is judged. Learning automaton rewards a ranking, if its average relevance score is greater than or equal to that of the best ranking generated so far. As the number of queries submitted to the search engine increases, the proposed algorithm learns how to rank the searched results in such a way that the most relevant documents are appeared at the top positions of the ranking. The proposed method was tested on the renowned benchmarks TREC 2003, TREC 2004, OHSUMED, and MQ2007. The obtained results showed that the proposed algorithm considerably outperforms SVMRank, LREG, and LRDRS in terms of P@n, MAP, and NDCG.

Table 8  
NDCG@n for OHSUMED.

<table><tr><td>n</td><td>SVMRank</td><td>LRDRS</td><td>LREG</td><td>LRUF</td></tr><tr><td>1</td><td>0.495</td><td>0.513</td><td>0.445</td><td>0.620</td></tr><tr><td>2</td><td>0.433</td><td>0.493</td><td>0.453</td><td>0.607</td></tr><tr><td>3</td><td>0.420</td><td>0.472</td><td>0.442</td><td>0.610</td></tr><tr><td>4</td><td>0.424</td><td>0.449</td><td>0.436</td><td>0.603</td></tr><tr><td>5</td><td>0.416</td><td>0.442</td><td>0.427</td><td>0.600</td></tr><tr><td>6</td><td>0.415</td><td>0.439</td><td>0.421</td><td>0.598</td></tr><tr><td>7</td><td>0.413</td><td>0.432</td><td>0.421</td><td>0.592</td></tr><tr><td>8</td><td>0.407</td><td>0.438</td><td>0.418</td><td>0.586</td></tr><tr><td>9</td><td>0.412</td><td>0.430</td><td>0.413</td><td>0.571</td></tr><tr><td>10</td><td>0.414</td><td>0.427</td><td>0.411</td><td>0.569</td></tr></table>

Table 9 NDCG@n for MQ2007.

<table><tr><td>n</td><td>SVMRank</td><td>LRDRS</td><td>LREG</td><td>LRUF</td></tr><tr><td>1</td><td>0.409</td><td>0.421</td><td>0.395</td><td>0.530</td></tr><tr><td>2</td><td>0.407</td><td>0.418</td><td>0.392</td><td>0.521</td></tr><tr><td>3</td><td>0.406</td><td>0.416</td><td>0.385</td><td>0.514</td></tr><tr><td>4</td><td>0.408</td><td>0.417</td><td>0.389</td><td>0.501</td></tr><tr><td>5</td><td>0.414</td><td>0.415</td><td>0.365</td><td>0.489</td></tr><tr><td>6</td><td>0.419</td><td>0.410</td><td>0.362</td><td>0.488</td></tr><tr><td>7</td><td>0.425</td><td>0.414</td><td>0.361</td><td>0.476</td></tr><tr><td>8</td><td>0.430</td><td>0.429</td><td>0.350</td><td>0.471</td></tr><tr><td>9</td><td>0.436</td><td>0.430</td><td>0.352</td><td>0.475</td></tr><tr><td>10</td><td>0.443</td><td>0.418</td><td>0.343</td><td>0.483</td></tr></table>

## References

[1] T. Joachims, Optimizing search engines using clickthrough data, in: Proceedings of the SIGKDD Conference, ACM Press, New York, USA, 2002, pp. 133–142.

[2] G. Salton, Associative document retrieval techniques using bibliographic information, Journal of the ACM 10 (4) (1963) 440–457.

[3] Y. Pan, H.-X. Luo, Y. Tang, C.-Q. Huang, Learning to rank with document ranks and scores, Knowledge-Based Systems 24 (4) (2011) 478–483.

[4] A. Trotman, Learning to rank, Information Retrieval 8 (2005) 359–381.

[5] N. Ailon, M. Mohri, Preference-based learning to rank, Machine Learning 80 (2–3) (2010) 189–211.

[6] S. Agarwal, Learning to rank on graphs, Machine Learning 81 (3) (2010) 333–357.

[7] J. Xu, H. Li, AdaRank: a boosting algorithm for information retrieval, in: Proceedings of the ACM SIGIR Conference on Research and Development in Information Retrieval, 2007, pp. 391–398

[8] T.P.C. Silva, E.S. de Moura, J.M.B. Cavalcanti, A.S. da Silva, M.G. de Carvalho, M.A. Goncalves, An evolutionary approach for combining different sources of evidence in search engines, Information Systems 34 (2009) 276–289.

[9] K. Berlt, E.S. Moura, A. Carvalho, M. Cristo, N. Ziviani, T. Couto, Modeling the web as a hypergraph to compute page reputation, Information Systems 35 (2010) 530-543

[10] W. Fan, P. Pathak, M. Zhou, Genetic-based approaches in ranking function discovery and optimization in information retrieval—a framework, Decision Support Systems 47 (2009) 398–407.

[11] W. Fan, P. Pathak, L. Wallace, Nonlinear ranking function representations in genetic programming-based ranking discovery for personalized search, Decision Support Systems 42 (2006) 1338–1349.

[12] T.-Y. Liu, J. Xu, T. Qin, W. Xiong, H. Li, LETOR: benchmark dataset for research on learning to rank for information retrieval, in: SIGIR 2007 Workshop on Learning to Rank for Information Retrieval (LR4IR 2007), 2007, pp. 3–10.

[13] S.E. Robertson, Overview of the Okapi projects, Journal of Documentation 53 (1) (1997) 3–7.

[14] C. Zhai, J. Lafferty, A study of smoothing methods for language models applied to ad hoc information retrieval, in: Proceedings of SIGIR 2001, 2001, pp. 334–342.

[15] S. Brin, Page, “The anatomy of a large-scale hypertextual Web search engine”, Computer Networks and ISDN Systems 30, No. 1–7, (1998) 107–117.

[16] J. Kleinberg, Authoritative sources in a hyperlinked environment, Journal of the ACM 46 (5) (1999) 604–622.

[17] G.R. Xue, Q. Yang, H.J. Zeng, Y. Yu, Z. Chen, Exploiting the hierarchical structure for link analysis, in: Proceedings of the Annual International ACM SIGIR Conference, 2005, p. 28.

[18] L. Nie, B.D. Davison, X. Qi, Topical link analysis for web search, in: Proceedings of the Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, vol. 29, 2006, pp. 91–98.

[19] T. Qin, T.Y. Liu, X.D. Zhang, Z. Chen, W.Y. Ma, A study of relevance propagation for web search, in: Proceedings of the Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, vol. 28, 2005, pp. 408–415.

[20] A. Shakery, C.X. Zhai, Relevance propagation for topic distillation UIUC TREC 2003-web track experiments, in: Proceedings of Text REtrieval Conference (TREC), 2003.

[21] http://research.microsoft.com/users/LETOR

[22] N. Craswell, D. Hawking, R. Wilkinson, M. Wu, Overview of the TREC 2003 web track, in: Proceedings of the 12th Text Retrieval Conference, 2003, pp. 78–92.

[23] W.R. Hersh, C. Buckley, T.J. Leone, D.H. Hickam, OHSUMED: an interactive retrieval evaluation and new large test collection for research, in: Proceedings of the 17th Annual ACM SIGIR Conference, 1994, pp. 192–201.

[24] K. Jarvelin, J. Kekalainen, IR evaluation methods for retrieving highly relevant documents, in: Proceedings of the Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, vol. 23, 2000, pp. 41–48.

[25] K. Jarvelin, J. Kekalainen, Cumulated gain-based evaluation of IR techniques, ACM Transactions on Information Systems 20 (4) (2002) 422–446

[26] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, Addison Wesley, 1999.

[27] K.S. Narendra, M.A.L. Thathachar, Learning Automata: An Introduction, New York, Printice-Hall, 1989.

[28] S. Lakshmivarahan, M.A.L. Thathachar, Bounds on the convergence probabilities of learning automata, IEEE Transactions on Systems, Man, and Cybernetics SMC-6 (1976) 756–763.

[29] E.A. Billard, S. Lakshmivarahan, Learning in multi-level games with incomplete information—part I, IEEE Transactions on Systems, Man, and Cybernetics — Part B: Cybernetics 19 (1999) 329–339.

[30] J. Akbari Torkestani, M.R. Meybodi, A new vertex coloring algorithm based on variable action-set learning automata, Journal of Computing and Informatics 29 (3) (2010) 1001–1020.

[31] J. Akbari Torkestani, M.R. Meybodi, An ef<sup>fi</sup>cient cluster-based CDMA/TDMA scheme for wireless mobile ad-hoc networks: a learning automata approach, Journal of Network and Computer Applications 33 (2010) 477–490

[32] M.R. Meybodi, “Learning Automata and Its Application to Priority Assignment in a Queuing System with Unknown Characteristics”, Ph.D. thesis, Department of Electrical Engineering and Computer Science, University of Oklahoma, Norman, Oklahoma, USA, 1983.

[33] A.A. Hashim, S. Amir, P. Mars, Application of learning automata to data compression, in: K.S. Narendra (Ed.), Adaptive and Learning Systems, Plenum Press, New York 1986 pp. 229-234

[34] B.J. Oommen, E.R. Hansen, List organizing strategies using stochastic move-tofront and stochastic move-to-rear operations, SIAM Journal of Computations 16 (Aug. 1987) 705–716

[35] C. Unsal, P. Kachroo, J.S. Bay, Multiple stochastic learning automata for vehicle path control in an automated highway system, IEEE Transactions on Systems, Man, and Cybernetics Part A 29 (1999) 120–128.

[36] A.G. Barto, P. Anandan, Pattern-recognizing stochastic learning automata, IEEE Transactions on Systems, Man, and Cybernetics SMC-15 (1985) 360–375.

[37] M.A.L. Thathachar, B.R. Harita, Learning automata with changing number of actions, IEEE Transactions on Systems, Man, and Cybernetics SMG17 (1987) 1095–1100.

[38] T. Westerveld, W. Kraai, D. Hiemstra, Retrieving web pages using content, links, urls and anchors in: Notebook of 10th Text Retrieval Conference (TREC) 2001.

[39] P. Calado, M. Cristo, E. Moura, N. Ziviani, B. Ribeiro-Neto, M.A. Gonc-alves, Combining link-based and content-based methods for web document classification. in: Proceedings of the 12th International Conference on Information and Knowledge Management, ACM Press, New York, USA, 2003, pp. 394–401.

[40] T. Qin, T.-Y. Liu, J. Xu, H. Li, LETOR: a benchmark collection for research on learning to rank for information retrieval, Information Retrieval 13 (2010) 346–374.

[41] L. Li, H.-T. Lin, Ordinal regression by extended binary classi<sup>fi</sup>cation, in: B. Schölkopf, J. Platt, T. Hoffman (Eds.), Advances in Neural Information Processing Systems, vol. 19, MIT Press, 2007, pp. 865–872.

[42] P. Li, C. Burges, Q. Wu, Mcrank: learning to rank using multiple classi<sup>fi</sup>cation and gradient boosting, in: J.C. Platt, D. Koller, Y. Singer, S. Roweis (Eds.), Advances in Neural Information Processing Systems, vol. 20, MIT Press, 2008, pp. 897–904.

[43] J. Akbari Torkestani, Degree constrained minimum spanning tree problem in stochastic graph, Journal of Cybernetics and Systems 43 (1) (2012) 1–21.

[44] J. Akbari Torkestani, M.R. Meybodi, LLACA: an adaptive localized clustering algorithm for wireless ad hoc networks based on learning automata, Journal of Computers & Electrical Engineering 37 (2011) 461–474

[45] J. Akbari Torkestani, M.R. Meybodi, A link stability-based multicast routing protocol for wireless mobile ad hoc networks, Journal of Network and Computer Applications 34 (4) (2011) 1429–1440.

[46] J. Akbari Torkestani, An adaptive backbone formation algorithm for wireless sensor networks, Computer Communications 35 (2012) 1333–1344

[47] J. Akbari Torkestani, A New Approach to the Job Scheduling Problem in Computational Grids, Cluster Computing 15 (2012) 201–210.

[48] J. Akbari Torkestani, “LAAP: A Learning Automata-based Adaptive Polling Scheme for Clustered Wireless Ad-Hoc Networks". Wireless Personal Communication, in press, 2012.

[49] J. Akbari Torkestani, Mobility prediction in mobile wireless networks, Journal of Network and Computer Applications 35 (2012) 1633–1645.

[50] J. Akbari Torkestani, M.R. Meybodi, Finding minimum weight connected dominating set in stochastic graph based on learning automata, Information Sciences 200 (2012) 57–77.

[51] J. Akbari Torkestani, An Adaptive Learning Automata-based Ranking Function Discovery Algorithm, Journal of Intelligent Information Systems 39 (2012) 441–459.

[52] J. Akbari Torkestani, “A Stable Virtual Backbone for Wireless MANETS”, Telecom munication Systems Journal, in press, 2012.

[53] J. Akbari Torkestani, “An adaptive focused Web crawling algorithm based on learning automata,” Applied Intelligence, in press.

[54] J. Akbari Torkestani, An adaptive heuristic to the bounded-diameter minimum spanning tree problem, Soft Computing 16 (2012) 1977–1988.

[55] J. Akbari Torkestani, Backbone formation in wireless sensor networks, Sensors and Actuators A: Physical 185 (2012) 117–126.

[56] J. Akbari Torkestani, A distributed resource discovery algorithm for P2P grids, Journal of Network and Computer Applications 35 (2012) 2008–2036

Javad Akbari Torkestani received the B.S. and M.S. degrees in Computer Engineering in Iran, in 2001 and 2004, respectively. He also received the Ph.D. degree in Computer Engineering from Science and Research University, Iran, in 2009. Currently, he is an assistant professor in Computer Engineering Department at Arak Azad University, Arak, Iran. Prior to the current position, he joined the faculty of the Computer Engineering Department at Arak Azad University as a lecturer. His research interests include wireless networks, mobile ad hoc networks, fault tolerant systems, learning systems, parallel algorithms, grid computing, web engineering, and soft computing.
