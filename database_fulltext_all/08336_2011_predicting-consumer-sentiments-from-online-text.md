---
otero_id: 8336
otero_key: "R26EFUEA"
title: "Predicting consumer sentiments from online text"
authors: "Xue Bai"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.024"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting consumer sentiments from online text

Xue Bai

Department of Operations and Information Management, School of Business, University of Connecticut, Storrs, CT 06269, USA

## a r t i c l e i n f o

Available online 19 August 2010

Keywords: Sentiment analysis Online reviews Online news Markov blanket Heuristic search

## a b s t r a c t

Sentiment analysis from unstructured text has witnessed a boom in interest in recent years, due to the sheer volume of online reviews and news corpora available in digital form. An accurate method for predicting sentiments could enable us, for instance, to extract opinions from the Internet and gauge online customers preferences, which could prove valuable for economic or marketing research, for leveraging a strategic advantage for an enterprise, or for detecting cyber risk and security threats. In this paper, we propose a heuristic search-enhanced Markov blanket model that is able to capture the dependencies among words and provide a vocabulary that is adequate for the purpose of extracting sentiments. Computational results on two collections of online movie reviews and three collections of online news show that our method is able to identify a parsimonious set of predictive features, yet simultaneously yield comparable or better prediction results about sentiment orientations, than several state-of-the-art feature selection algorithms as well as sentiment prediction methods. Our results suggest that sentiments are captured by conditional dependencies among words as well as by keywords or high-frequency words.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Prior to the Internet, researchers used surveys to collect limited amounts of data in a structured form to analyze consumers' opinions on a product or service. In recent years, the advent of the Internet, and the widespread use of advanced information technologies in general (e.g. Web 2.0), have resulted in a surge of information that is freely available online in a text format. For example, many online forums and review sites exist for people to post their opinions about a product. While such consumer-generated online content offers tremendous business opportunities, potential risk and security concerns arise due to the possible malicious use of online social media [8]. Automatic and accurate understanding of sentiments expressed within the online text could lead to effective information retrieval, enable automated cyber risk management strategies, and improve business pro<sup>fi</sup>ts.

Researchers in the data mining <sup>fi</sup>eld have studied the problem of text classi<sup>fi</sup>cation for more than three decades. Effective solutions have been found in the area of topic categorization and of authorship attribution. Topics are captured by sets of keywords, while authors are identi<sup>fi</sup>ed by their choices in the use of non-contextual, highfrequency words [2,3]. Pang et al. [34] showed that such solutions, or extensions of them, underperform when applied to sentiment extraction, yielding cross-validated accuracies and areas under the curve (AUC) in only between the high 70%s to low 80%s. Even more worrisome is the fact that these performances are obtained using large vocabularies, for which the discriminatory power of words is likely due to chance for many of the words. We conjecture that one reason for the failure of such approaches may be attributed to the fact that the words selected in the classi<sup>fi</sup>cation are considered to be independent of one another. We argue that their very interactions lead to the emergence of sentiments in the text. The goal of this paper is to present a machine learning method for learning predominant sentiments of online texts available in unstructured format, that is capable of selecting words that are related to one another and to the sentiment embedded in the texts signi<sup>fi</sup>cantly, i.e., beyond pure chance, and <sup>fi</sup>nding a minimal vocabulary that leads to good performance in categorization and prediction tasks.

In this paper, we present a two-stage prediction algorithm, the Markov Blanket Classi<sup>fi</sup>er, that is able to capture the dependencies among words, <sup>fi</sup>nd a vocabulary that can ef<sup>fi</sup>ciently extract sentiments, and ultimately, provide better predictions about sentiment expressed in a text document, compared to several state-of-the-art machine learning methods. Our two-stage Markov Blanket Classi<sup>fi</sup>er learns conditional dependencies among the words and encodes them into a Markov Blanket Directed Acyclic Graph (MB-DAG) for the sentiment variable (<sup>fi</sup>rst stage), and then uses a Tabu search (TS) meta-heuristic strategy to <sup>fi</sup>ne-tune the MB-DAG (second stage) in order to yield a higher cross-validated accuracy. Learning dependencies allows us to capture semantic relations and dependent patterns among the words, which help us to approximate the meaning of sentences with respect to the sentiment they encode. Furthermore, performing the classi<sup>fi</sup>cation task using a Markov Blanket (MB) for the sentiment variable has two important properties: it speci<sup>fi</sup>es a statistically ef<sup>fi</sup>cient prediction of the probability distribution of the sentiment variable from the smallest subset of predictors, and it provides accuracy while avoiding over-<sup>fi</sup>tting due to redundant predictors. We test our algorithm on two versions of the publicly available online movie reviews data [32,34] and on three collections of proprietary online news with different degrees of topicality [30]. The computational results show that our method is able to achieve a crossvalidated accuracy and AUC comparable to the best performance of competing state-of-the-art sentiment classi<sup>fi</sup>cation methods with a parsimonious vocabulary.

The remainder of this paper is organized as follows. Section 2 surveys relevant literature. Section 3 provides brief background knowledge about Bayesian networks, Markov Blankets, and Tabu search heuristic. Section 4 introduces the methodology. Section 5 presents the data sets used in the study. Section 6.2.2 presents the experimental results with comparisons to several state-of-the-art methods. Section 7 discusses the <sup>fi</sup>ndings and concludes with a summary of this work and future directions.

## 2. Literature review

## 2.1. Bayesian network and Markov blanket classification

Research in the Bayesian network <sup>fi</sup>eld has sought to identify a part of the Bayesian Network that can be exploited as classi<sup>fi</sup>ers for the target class variable.

Friedman et al. introduced the General Bayesian Network (GBN) algorithm [14]. The basic idea of GBN is to learn a Bayesian Network structure that contains the target class node using Information Gain scores, and to perform the classi<sup>fi</sup>cation based on the Bayesian Network learned. The score driving the search of the structure for GBN measures the overall <sup>fi</sup>t. The score is calculated on a weighted average schema over all the nodes in the network, not optimized for the target class node. In addition, the GBN algorithm learns the whole Bayesian Network <sup>fi</sup>rst in order to use a portion of it for classi<sup>fi</sup>cation; hence it is feasible only for small data sets.

Madden proposed a methodology for induction of a Bayesian network structure for classi<sup>fi</sup>cation [24]. This structure is called Partial Bayesian Network (PBN). PBN is implemented using the K2 framework introduced in [10]. Learning the Partial Bayesian Network essentially reduces to a Bayesian Network learning problem using the K2 algorithm. The complexity of K2 algorithm is exponential to the number of variables; hence, PBN is also feasible only for small data sets.

Later, Madden presented an extended description of the algorithm in [24], introducing the concept of “Markov Blanket” [25]. The algorithm is called MBBC. However, the result of MBBC is a set of “Markov Blanket” variables, not a MB-DAG; each node represents a variable in the Markov blanket. This is because the results of K2 can only correctly identify the union of the set of variables adjacent to the target and the set of variables adjacent to those variables. It does not correctly identify the edge orientations of the variables in the union. By contrast, a MB-DAG contains both the variables in the Markov blanket and the relevant edges among the variables. MBBC, like PBN, is feasible only for small data sets. This is because 1) the scoring criterion used to construct the MB is a K2 metric [25]; and 2) after the MB is constructed, the conditional independence tests used to do the classi<sup>fi</sup>cation is the joint probabilities estimation proposed in the K2 algorithm, which is essentially also an exponent-based K2 metric estimation.

To the best of our knowledge, little of the previous work has dealt with real world data with a large number of variables and limited number of samples. Furthermore, for those studies that have used the notion of Markov Blanket as a minimal set of dependent variables, none of them have actually generated and retained the graphical structure of the Markov Blanket corresponding to a speci<sup>fi</sup>c data set, nor have they used the structure for Bayesian inference in order to perform the classi<sup>fi</sup>cation. Our algorithm addresses all of these limitations.

## 2.2. Sentiment analysis

Sentiment analysis is also known as opinion extraction or semantic classi<sup>fi</sup>cation in the text mining literature [1,33]. A related problem is that of studying the semantic orientation or polarity of words [31]. Huettner and Subasic [19] developed a cognitive linguistic model for affection sentiments based on fuzzy logic. Liu et al. [23] proposed a method to categorize emotions using a large dictionary of common sense knowledge and on linguistic models. Das and Chen [11] constructed lexicon and grammar rules using domain knowledge to capture the “pulse” of <sup>fi</sup>nancial markets, as expressed by online news about traded stocks, and thus achieved a classi<sup>fi</sup>cation accuracy of 62% (against the baseline accuracy of 33%). Hatzivassiloglou and McKeown [17] developed a log-linear model to predict the semantic orientation of conjoined adjectives. Turney and Littman [41] proposed a semisupervised method for learning the polarity of adjectives starting from a small set of adjectives with known polarity. Turney [40] later applied this method to predicting the consumers' opinions about various objects (e.g., movies, cars, banks), and achieved accuracies between 66% and 84%. Pang et al. [34] applied the off-the-shelf classi<sup>fi</sup>cation methods to frequent, non-contextual words in combination with various heuristics and annotators, and achieved a maximum crossvalidated accuracy of 82.9% on the IMDb data set. Dave et al. [12] classi<sup>fi</sup>ed movie reviews into positive versus negative using support vector machines on different types of semantic features based on substitutions and proximity, and achieved an accuracy of 88.9% on data sets from Amazon and CNN.Net.

Recent research tackles the problem by pairing data mining algorithms with feature selection methods [1,15,26,27,32,36,42]. Gamon [14] developed a linear support vector machine algorithm that combines two feature reduction pre-processing procedures. The features are <sup>fi</sup>rst <sup>fi</sup>ltered by linguistic analysis, then by the ranking of “predictiveness.” The algorithm was evaluated on two sets of satisfaction survey data and achieved high classi<sup>fi</sup>cation accuracy. Ng et al. [27] used unigram and n-gram features combined with a loglikelihood based feature selection method and showed that the simple “bag-of-words” method was able to attain satisfactory accuracy on the movie review data set, using SVM classi<sup>fi</sup>ers. Reliff et al. [36] implemented a subsumption hierarchy mechanism in Information Gain criterion and showed good improvement in opinion classi<sup>fi</sup>cation using three opinion-related data sets. Abbasi et al. [1] developed a hybrid genetic algorithm that incorporated the Information Gain heuristic with the entropy metric for feature selection. Their method, namely Entropy Weighted Genetic Algorithm (EWGA), when paired with SVM classi<sup>fi</sup>ers, has achieved high classi<sup>fi</sup>cation performance on both the movie reviews data and the web forum postings in multiple languages. Other studies have also achieved good classi<sup>fi</sup>cation results by pairing “bag-of-words” n-gram features with various advanced feature selection schema, such as attitude and orientation features [42], topic proximity and syntactic-relations features [26], and sentence-level sentiment extraction [32].

For an excellent survey of recent work on sentiment analysis, please see [33] and [1].

## 3. Problem de<sup>fi</sup>nition and background knowledge

In this section, we introduce the problem de<sup>fi</sup>nition and brie<sup>fl</sup>y discuss its scope, and provide brief overviews of relevant concepts to our model.

## 3.1. Problem definition

The problem can be formally de<sup>fi</sup>ned as a sentiment prediction problem as described in [4]. The data consists of a collection of N documents $\{ x _ { d 1 } , . . . , x _ { d V } \} _ { d = 1 } ^ { N }$ , that is, of N examples of the random variables corresponding to the words, $\{ X _ { 1 } , . . . , X _ { V } \}$ . The overall sentiment of a document d is captured by the class variable $Y = y _ { d } ,$ which can take one of a <sup>fi</sup>nite number of sentiment values $( y _ { d } = q , q = 0 , . . . , Q )$ . An index w identi<sup>fi</sup>es a unique word in the vocabulary, and V denotes the size of the vocabulary observed in the collection of N documents. Each of the variables $\{ X _ { w } \} _ { w = 1 } ^ { V }$ encodes the presence or absence of word w in document d, i.e., $\{ x _ { d w } \} { \in } \{ 0 , 1 \} \mathrm { f o r } d { = } 1 , { \ldots } , N .$ The problem is de<sup>fi</sup>ned as below.

Sentiment Prediction: given a collection of N documents $\{ x _ { d 1 } , . . . ,$ ${ \boldsymbol { x } } _ { d V } \} _ { d = 1 } ^ { N } \in \{ 0 , 1 \} ^ { V } ,$ , and an indication of the corresponding sentiments they encode, $\{ y _ { d } \} _ { d = 1 } ^ { N } \in [ 0 , Q ]$ , we want to predict the overall sentiment of new document, f: $\{ 0 , 1 \} ^ { V } \to [ 0 , Q ] .$

Although the mathematical formulation of the problem is a typical supervised classi<sup>fi</sup>cation problem, the most interesting characteristic of the problem is that sentiments are complex semantic elements that cannot be expressed by independent presence or absence patterns of words. We develop a model to capture the dependency patterns of the presence or absence of words.

## 3.2. Background knowledge

## 3.2.1. Bayesian network and Markov blanket

A Bayesian network is a graphical representation of the joint probability distribution of a set of random variables [35]. A Bayesian Network for a set of variables $X { = } \{ X _ { 1 } { , } . . . , X _ { V } \}$ consists of: (i) a directed acyclic graph (DAG) S that encodes a set of conditional independence assertions among variables in X ; and (ii) a set $P { = } \{ p _ { 1 } { , } . . . , p _ { V } \}$ of local conditional probability distributions associated with each node and its parents. A Bayesian Network also has a causal interpretation: a directed edge from one variable to another, $X  Y ,$ represents the claim that X is a direct cause of Y with respect to other variables in the DAG [35,37].

De<sup>fi</sup>nition 1. P satis<sup>fi</sup>es the Markov Condition for S if every node Xi in S is independent of its non-descendants and non-parents in S, conditional on its parents [35].

The Markov Condition implies that the joint probability distribution p can be factorized as a product of conditional probabilities by specifying that the distribution of each node is conditional on its parents [35]. In particular, for a given S, the joint probability distribution for X can be written as

$$
P (X) = \prod_ {i = 1} ^ {V} P (X _ {i} | p a _ {i})\tag{1}
$$

where $p a _ { i }$ denotes the set of parents of $X _ { i \cdot }$ This is called a Markov factorization of P according to S.

De<sup>fi</sup>nition 2. Given the set of variables X and target variable $Y ,$ a Markov Blanket (MB) for Y is the smallest subset Z of variables in X such that Y is independent of $X \backslash Z ,$ conditional on the variables in Z [35].

Assuming that there are no conditional independence relations in P other than those entailed by the Markov condition for S, then for a given Bayesian Network $( S , P )$ , there is a unique Markov Blanket for Y consisting of $p a _ { Y } ,$ the set of parents of Y; ch , the set of children of Y; and pa $c h _ { Y } ,$ the set of parents of children of Y [35].

For example, consider the two DAGs in Fig. 1. The factorization of p for the Bayesian Network (S, P) is the following,

$$
\begin{array}{c} P (Y, X _ {1}, \ldots , X _ {7}) = P (Y | X _ {1}) P (X _ {1}) P (X _ {2} | X _ {1}) P (X _ {3} | X _ {1}) P (X _ {4} | X _ {2}, X _ {7}, Y) \\ \times P (X _ {5} | X _ {4}, Y) P (X _ {6} | X _ {4}) P (X _ {7}). \end{array}\tag{2}
$$

The factorization of the conditional probability entailed by the Markov Blanket for $Y , \ P \ ( Y \ | X _ { 1 } , . . . , X _ { 7 } )$ , corresponds to the product of those (local) factors in $\operatorname { E q . } \left( 2 \right)$ that contain $Y ,$

$$
P (Y | X _ {1}, \dots , X _ {7}) = C ^ {'} P (Y | X _ {1}) P (X _ {4} | X _ {2}, X _ {7}, Y) P (X _ {5} | X _ {4}, Y),\tag{3}
$$

where C′ is a normalizing constant independent of Y.

De<sup>fi</sup>nition 3. MB-DAGs that entail the same set of conditional independence relations are said to be Markov equivalent; and the set of all MB-DAGs that are Markov equivalent form a Markov equivalence class [35].

## 3.2.2. Tabu search

Tabu search is a meta-heuristic search method that is able to guide traditional local search methods to escape local optima with the assistance of adaptive memory [16]. We were motivated to use Tabu search because of its adaptive memory capability. The adaptive memory feature of Tabu search allows the search procedures to explore a much larger set of candidate solutions in the solution space in an economical and effective manner.

The adaptive memory feature of Tabu search heuristic appears particularly suitable for Bayesian Networks and Markov Blanket approaches, for which there exist a lot of local optimal graphic structures. In its simplest form, Tabu search starts with a feasible solution and chooses the best move according to an evaluation function, while taking steps to ensure that the method does not revisit a solution previously generated. This is accomplished by introducing tabu restrictions on possible moves to discourage the reversal and in some cases repetition of selected moves. The tabu list that contains these forbidden moves is known as the short-term memory function. It operates by modifying the search trajectory to exclude moves leading to new solutions that contain attributes (or attribute mixes) belonging to solutions previously visited within a time horizon governed by the short-term memory. Intermediate and long-term memory functions may also be incorporated to intensify and diversify the search. Tabu search and its use of adaptive memory have been proven successful, both when it is applied directly to a problem and when it is embedded within other hybrid methods [18,39].

![](/api/attachments/R26EFUEA/fulltext/images/81c07fcca91d491968f104a0ef6ec5ce40f44f5fb9fb7390b827866d9b1a9e44.jpg)  
Fig. 1. (left) A Bayesian Network (S, P), and (right) the Markov Blanket for the variable encoding the overall sentiment of a document, Y.

## 4. The Markov blanket model for word dependencies

In this section we describe our learning algorithm and the intuitions behind it. The various subprocedures used in the algorithm are summarized here and listed in Appendix A. A complete version of the algorithm can be found in [6].

## 4.1. The Markov blanket for a sentiment variable

The algorithm for learning the Markov Blanket for a sentiment variable is called a Markov Blanket Classifier. The algorithm contains two stages [4]: stage 1 <sup>fi</sup>nds a parsimonious vocabulary that is expressive enough to capture the overall sentiment of a document, and stage 2 <sup>fi</sup>nds a dependency structure between the set of words in the vocabulary and the sentiment variable that leads to good predictions of the overall sentiment of a new document. Fig. 2 presents an overview of the algorithm for learning the Markov Blanket Classi<sup>fi</sup>er.

At the <sup>fi</sup>rst stage (steps 1 to 4), a collection of training documents, D, is used to generate an initial Markov blanket for the sentiment variable Y. The <sup>fi</sup>rst stage aims at <sup>fi</sup>nding a parsimonious yet expressive vocabulary. The search for the expressive vocabulary takes into account dependency patterns among words. The <sup>fi</sup>rst stage stops at step 4 with an output of a subset of words found to be expressive enough to describe the word patterns to predict the overall sentiment in the text (the $M B _ { D A G }$ for Y). At this point, the selected set of words (L) may contain those that are not part of the Markov Blanket for Y. The algorithm however cannot de<sup>fi</sup>nitively exclude (in step 3) due to their potential for being useful in expressing sentiments.

The initial $M B _ { D A G }$ learned at stage 1 may be highly suboptimal, due to the application of repeated conditional independence tests [37] in steps 1 and 2, and propagation of errors in edge orientation [5]. Hence, Tabu search is applied in the second stage (step 5) to improve the predictive accuracy of the initial Markov blanket as a classi<sup>fi</sup>er. The second-stage procedure stops after a <sup>fi</sup>xed number of iterations or a <sup>fi</sup>xed number of non-improving iterations.

The parameters used in the algorithm are: a data set with V words and N documents; Y, the sentiment variable; δ, the maximum size of the separating sets (sets of words) considered for the conditional independence tests; and $\alpha ,$ the signi<sup>fi</sup>cance level for the $G ^ { 2 }$ statistical independence tests. The $G ^ { 2 }$ test is a variation of the $\chi ^ { 2 }$ test for independence of random variables. For a formal de<sup>fi</sup>nition please see [37]. Both the $G ^ { 2 }$ test of independence and the use of binary variables to encode presence/absence of words are choices dictated by our endeavor for a parsimonious and topic-independent vocabulary. Intuitively, we can divide the words into three groups: words that are highly frequent in most documents of a collection, words that are topic-related and highly frequent in a few documents, and rare words. Using presence/absence of words, rather than their frequency of

$$
\text { LrnMBC } \left(\left\{\mathrm{x} _ {\mathrm{d} 1},..., \mathrm{x} _ {\mathrm{dV}} \right\}, \left\{\mathrm{y} _ {\mathrm{d}} \right\}, \delta , \alpha\right)
$$

$$
1. \mathrm{L} _ {\mathrm{Y}} = \operatorname{Adj} \left(\left\{\mathrm{y} _ {\mathrm{d}} \right\}, \left\{\mathrm{x} _ {\mathrm{d} 1},..., \mathrm{x} _ {\mathrm{dV}} \right\}, \delta , \alpha\right)
$$

2. for $\mathbf { X } _ { \mathrm { i } } \in \mathrm { L } _ { \mathrm { Y } }$

$$
\mathrm{L} _ {\mathrm{X} _ {\mathrm{i}}} = \operatorname{Adj} \left(\left\{\mathrm{x} _ {\mathrm{di}} \right\}, \left\{\mathrm{x} _ {\mathrm{d} 1}, \dots , \mathrm{x} _ {\mathrm{dV}} \right\} \backslash \mathrm{x} _ {\mathrm{di}}, \delta , \alpha\right)
$$

$$
3. \mathrm{G} = \operatorname{Ornt} \left(\mathrm{Y} \cup \mathrm{L} _ {\mathrm{Y}} \cup_ {\mathrm{i}} \mathrm{L} _ {\mathrm{X} _ {\mathrm{i}}}\right)
$$

$$
\left\{\mathrm{MB} _ {\mathrm{DAG}} (\mathrm{Y}), \mathrm{L} \right\} = \operatorname{Trsfm} (\mathrm{G})
$$

$$
5. \text {   TabuSrch   } (\mathrm{MB} _ {\mathrm{DAG}} (\mathrm{Y}), \mathrm{L}, \text { Max } _ {\text { Iter }})
$$

occurrence, dampens the discriminative power of topical words, while selecting words with a signi<sup>fi</sup>cant $G ^ { 2 }$ statistic favors words that are highly frequent overall. The combined effect is that words that are strongly associated with sentiments are retained. In fact, one can think of sentiments as behaving like broad topics in terms of word frequency patterns [4].

## 4.2. The algorithm

The <sup>fi</sup>ve steps of the LrnMBC algorithm are summarized as follows.

Steps 1 and 2: Search of the adjacency structure. In the <sup>fi</sup>rst two steps, independence and conditional independence $G ^ { 2 }$ tests are carried out according to a breadth-<sup>fi</sup>rst heuristic. In step 1, the function Adj is used to identify a list of words that are related to the sentiment variable, $L _ { Y } ,$ and then in step 2, Adj is again used to identify lists of words related to each word $X _ { \mathrm { i } }$ in the list $L _ { Y } .$ Throughout steps 1 and 2, the adjacencies are represented by undirected edges. At the end of step 2, an undirected graph is formed over the words $Y \cup L _ { Y } \cup _ { i } L _ { X _ { i } } ,$ , which contains the $M B _ { D A G }$ for Y in terms of $p a _ { Y } ,$ ch , and pa ch .

Step 3: Edge orientation. At step 3, the procedure Ornt is applied for the orientation of the edges. The edges are oriented by repeatedly applying a set of four edge orientation rules [37,38], which are described in detail in Appendix A. These rules are meant to recover the true but unobservable DAG over the selected words. This procedure is provably guaranteed to <sup>fi</sup>nd the correct DAG at the large number limit, that is, with an in<sup>fi</sup>nite number of documents [5]. The underlying assumption for the asymptotic correctness argument is that every conditional independence statement that we can derive from the data also holds in the true graph, which is a typical assumption underlying methods for statistical learning of causal relations [35].

Step 4: Formation of an initial Markov Blanket DAG. At step 4, the procedure Trsfm transforms the output of step 3 into a proper $M B _ { D A G }$ by removing the undirected and bi-directed edges, along with the corresponding nodes, that is, words. These words are not thrown away, but are stored in the list L. L consists of the words that were not removed from the battery of conditional independence tests, but for which it is uncertain as to what role they may have in the $M B _ { D A G }$

Step 5: Tabu search. At the <sup>fi</sup>nal step, TabuSrch procedure is applied to the initial $M B _ { D A G }$ and to L in order to boost the predictive structure of the DAG amongst the words in the selected vocabulary. Our algorithm searches for solutions in the space of logical Markov Blankets, e.g., moves that result in cyclic graphs are not valid. In particular, four kinds of moves are allowed in TabuSrch: edge addition, edge deletion, edge reversal, and edge reversal with node pruning, as illustrated in [6]. The procedure stops after a <sup>fi</sup>xed number of iterations or until there is no improvement in the scoring criterion for a pre-speci<sup>fi</sup>ed number of iterations. At each step and for each allowed move, the corresponding $M B _ { D A G }$ is computed, its conditional probability factored, and its predictions scored; the best move is then selected and applied. The best solution and best score at each step are tracked. The tabu list keeps a record of m previous moves; so that moves in the tabu list will not be repeated until their corresponding tabu tenure expires. The parameter m is called tabu tenure. The value of tabu tenure varies according to the complexity of the candidate $M B _ { D A G } s$ in different problems. Simple versions of TabuSrch based on tabu tenures between 7 and 12 have been found to work well in settings where tabu restrictions rule out a non-trivial portion of otherwise available moves [16]. A <sup>fi</sup>xed tabu tenure value of 7 is used in our experiments.

## 4.3. Prediction

Predicting sentiments for the document samples in the testing set is the next task after the LrnMBC algorithm learns the classi<sup>fi</sup>er on the training documents. We approach the prediction as a multipleclass classi<sup>fi</sup>cation problem, i.e., we do not divide the problem into a series of binary classi<sup>fi</sup>cation problems. The overall sentiment of a new document is assigned according to its posterior probability given the words that are present in it. Formally, for each new document, $\{ x _ { 1 } , . . . , x _ { V } \} ,$ , we compute: $l _ { i } = \log \left[ \frac { P ( Y = y _ { i } | \{ x _ { 1 } , . . . , x _ { V } \} ) } { P ( Y = y _ { 0 } | \{ x _ { 1 } , . . . , x _ { V } \} ) } \right]$ , for ∀ i= 1, … I, where the y s represent the possible values of the sentiment variable. We choose the sentiment that maximizes the log-odds, $i ^ { * } { = } \mathtt { a r g }$ max $l _ { \mathrm { i } } .$ The classi<sup>fi</sup>cation is carried out using logistic regression, which has a performance comparable to more sophisticated methods, while also having the advantage of being entirely automated, i.e., no parameter tuning is necessary [21].

The proposed Markov Blanket Classi<sup>fi</sup>er has two fundamental properties that add theoretical guarantees to its good empirical performance. First, it learns the correct Markov blanket at the limit; second, the complexity of training such a Markov Blanket Classi<sup>fi</sup>er is $O ( N )$ , i.e., linear with respect to the number of documents N. For an indepth analysis of these properties, we refer to [5].

## 5. Data

Five sets of data are used for the computational experiments: two collections of online movie reviews data provided by Pang et al. [34] and Pang and Lee [32], respectively, and three proprietary collections of online news provided by Infonic Ltd. [30]. In this section we describe the data and the pre-processing steps performed to prepare the data used in the experiments.

## 5.1. A binary classification case: movie reviews data

Most studies on sentiment analysis have evaluated the performances of their methodologies on the IMDb movie reviews data. Both versions of the data are available online [29]. While most of the earlier work tested their methods on version 1.0 as in [34], recent studies have mainly used version 2.0 for algorithm evaluations, as in [32]. In order to be able to compare our method with the majority of the previously proposed methods that have yielded good results, we conduct two sets of experiments, one each on the two versions of the IMDb database, respectively, as shown in Tables 4 and 5. The movie reviews data contains approximately 29,000 posts to the rec.arts. movies.reviews newsgroup archived at the Internet Movie Database (IMDb). The original posts are available in the form of HTML pages. Some pre-processing was performed to produce the version of the data we used. Speci<sup>fi</sup>cally, only reviews where authors' ratings were expressed explicitly (either by stars or by numerical values) were selected. Then explicit ratings were removed and converted into one of three categories: positive, negative, or neutral. Finally, version 1.0 [34] contains 700 positive reviews and 700 negative reviews, which the authors of the corpus judged to be more extreme, which were selected for our study. Version 2.0 [32] contains 1000 positive and 1000 negative reviews all written before 2002, with a cap of 20 reviews per author (312 authors total) per category.

## 5.1.1. Data preparation

In this study, words are de<sup>fi</sup>ned as strings of letters enclosed by non-letters to the left and to the right excluding punctuation, even though exclamation signs and question marks may be helpful for the task of classifying sentiments [4]. As indicated earlier, sentiment classi<sup>fi</sup>cation is essentially a hybrid task between authorship attribution and topic categorization. In the data preparation step, we consider frequent words that help express lexical patterns but not are necessarily related to the context, as well as low frequency words that may be speci<sup>fi</sup>c to few review styles, but very indicative of an opinion. We choose all the words that appeared in more than 8 documents as the input features; words with lower counts were discarded, as they are too rare to be informative in the classi<sup>fi</sup>cation. As a result, for version 1.0, we have a total number of 7716 words as the initial vocabulary; for version 2.0, we have a total number of 8259 words as the initial vocabulary. Each document is <sup>fi</sup>nally represented as a vector, $X : = [ X _ { 1 } , . . . , X _ { V } ]$ , where V is the size of the initial vocabulary, and each X is a binary random variable that takes the value of 1 if the ith word in the vocabulary is present in the document and the value of 0 otherwise. Table 1 summarizes the descriptive characteristics of the Movie reviews data.

Table 1  
Description of movie reviews data.

<table><tr><td>Data set</td><td>Classification</td><td>Size of vocabulary (V)</td><td>Num of samples</td><td>Predictive vars.</td></tr><tr><td>IMDb v1.0</td><td>Positive/negative</td><td>7716</td><td>1400</td><td>Binary</td></tr><tr><td>IMDb v2.0</td><td>Positive/negative</td><td>8259</td><td>2000</td><td>Binary</td></tr></table>

## 5.2. A multi-class classification case: online news data

The online news data consists of three sets of 600 news articles each on the following topics: mergers and acquisitions (M&A), <sup>fi</sup>nance, and mixed news. These three corpora have been designed to exhibit distinct levels of speci<sup>fi</sup>city, where M&A is the most speci<sup>fi</sup>c corpus. Articles in the M&A corpus concern only real or speculated mergers, acquisitions, take-overs or joint-ventures. Mixed News is the least speci<sup>fi</sup>c corpus. Mixed News corpus contains news and editorial content concerning a broad range of topics. The news in the Finance corpus falls somewhere in between. The Finance corpus includes articles concerning all other corporate <sup>fi</sup>nancial matters, except those that would merit inclusion in the M&A. The sentiments considered are three: positive, neutral, and negative. Each corpus contains 200 articles of each sentiment category. Articles were manually labeled with a document-level sentiment by three independent annotators from a pool of seven trained annotators; all documents in the corpus have at least a two-way consensus for their sentiment rating. The agreement rate between annotators was found to be consistently above 78%.

Speci<sup>fi</sup>cally, the articles in the online news data were selected using online news aggregators (e.g., Google News)<sup>1</sup> and specialist news sites (e.g., Reuters).<sup>2</sup> Articles were selected to ensure that they were not sarcastic and that they expressed sentiment concerning only one clearly identi<sup>fi</sup>able entity. A number of manual inspections of the corpora were conducted to ensure that all the above criteria were met, and to remove any duplicate items. A total of six sentiment categories were initially available for annotation as described in [4]: categories 1 or 2 for very positive or very negative: unreservedly or overwhelmingly positive or negative; categories 3 or 4 for positive or negative: unreservedly, but only mildly positive or negative, or containing mixed sentiment which on balance was positive or negative; category 5 for neutral: entirely objective, expressing no sentiment; and category 6 for balanced: containing both positive and negative sentiment with no clear bias towards either. All articles that did not have at least a two-way consensus, or those that had a consensus of balanced, were removed. The resulting corpora each contained 200 news articles for each of the remaining <sup>fi</sup>ve sentiment categories. Finally, the two positive and negative categories were collapsed into a single positive or negative category by randomly selecting 100 articles in each corpus from each of the four non-neutral sentiment categories.

Table 2  
Description of online news data.

<table><tr><td>Data set</td><td>Classification</td><td>Size of vocabulary (V)</td><td>Number of samples</td><td>Predictive vars.</td></tr><tr><td>M&amp;A News</td><td>Positive/neutral/negative</td><td>10,531</td><td>600</td><td>Binary</td></tr><tr><td>Financial News</td><td>Positive/neutral/negative</td><td>11,220</td><td>600</td><td>Binary</td></tr><tr><td>Mixed News</td><td>Positive/neutral/negative</td><td>15,685</td><td>600</td><td>Binary</td></tr></table>

## 5.2.1. Data preparation

Similar to the processing procedure in Section 6, words are strings of letters enclosed by non-letters to the left and to the right excluding punctuations. For the within-topic classi<sup>fi</sup>cation experiments, we considered all the words in a corpus as the starting pool, from which to extract the <sup>fi</sup>nal vocabulary. This yields starting vocabularies of sizes 10,531, 11,220, and 15,685, for the M&A, Financial, and Mixed News corpora, respectively. Table 2 summarizes the descriptive characteristics of the online news data.

## 6. Computational results

In this section we describe the experimental setup, present the computational results, and discuss the main <sup>fi</sup>ndings from our experiments.

## 6.1. Experimental design

As discussed in Section 4, the parameters relevant to our experiments were: δ, the maximum size of the separating sets to consider for conditional independence tests in $A d j ;$ and α, the signi<sup>fi</sup>cance level of the $G ^ { 2 }$ tests used to decide whether to accept or reject each of these tests. In Table 3 we show the speci<sup>fi</sup>c values for δ and α that we have considered in our experimental design.

To estimate the predictive accuracy on new documents, we use a <sup>fi</sup>ve-fold or ten-fold cross-validation scheme for the experiments.<sup>3</sup> In particular, we used a nested cross-validation scheme. For example, in the case of ten-fold cross-validation scheme, we randomly divided each of the ten training sets of documents (one for each crossvalidation fold, consisting of 9/10 of the documents respectively) into a sub-training and a sub-testing set of documents at random, using 80% and 20% of the training documents respectively. Stage 1 of the LrnMBC procedure then uses the sub-training set of documents, and stage 2 of the LrnMBC procedure re<sup>fi</sup>nes the $M B _ { D A G }$ on the sub-testing set of documents with the objective of avoiding over-<sup>fi</sup>tting. This process is repeated for each pair $( \delta , \alpha )$ of the con<sup>fi</sup>guration parameters in Table 3. The dominant con<sup>fi</sup>guration of parameters in terms of accuracy on the sub-testing set of documents is chosen as the best configuration. Finally, the best con<sup>fi</sup>guration $M B _ { D A G }$ for the sentiment variable for a given cross-validation fold, is used to measure the performance on the testing data for that fold.

For binary classi<sup>fi</sup>cation problems such as the problem of the online movie reviews data set, we report the cross-validated AUC and accuracy for each experiment. As AUC is not a feasible measure for multi-class classi<sup>fi</sup>cation problems, we report the cross-validated Kappa statistic and accuracy for each experiment for the online news data sets. Kappa statistic was introduced by Carletta [7] to assess the quality of a classi<sup>fi</sup>er in terms of accuracy above a random baseline. It is de<sup>fi</sup>ned as $\begin{array} { r } { \kappa = \frac { A - R } { 1 - R } , } \end{array}$ where A is the empirical probability of agreement on a category, and R is the probability of agreement for two annotators that label documents at random (with the empirically observed frequency of each label). Hence kappa ranges from −1 to +1; positive values indicate a performance better than the random baseline, whereas negative values indicate a worse performance.

Table 3  
Con<sup>fi</sup>gurations of experimental parameters.

<table><tr><td>Performance measures</td><td>Depth of search δ</td><td>Significance level α</td><td>Cross validation</td></tr><tr><td>AUC, kappa, accuracy</td><td>1, 2, 3</td><td>0.001, 0.005, 0.01, 0.05</td><td>5-fold, 10-fold</td></tr></table>

## 6.2. Results and analysis

We conducted three batches of experiments to examine the effectiveness of our method in terms of classi<sup>fi</sup>cation, feature selection, and robustness of classi<sup>fi</sup>cations for the binary and multiclass classi<sup>fi</sup>cation problems, respectively. In addition, in order to investigate the effect of the <sup>fi</sup>rst-stage search for an initial Markov Blanket Classi<sup>fi</sup>er and that of the second-stage Tabu heuristic search, we compare the two-stage search procedure (hereby called “TS-MBC”) with the <sup>fi</sup>rst-stage procedure, prior to Tabu search process (hereby called “MBC”). The computational results are presented in Tables 4–8.

## 6.2.1. Comparing classification algorithms

In the <sup>fi</sup>rst batch of experiments, we tested the performance of TS-MBC as a classi<sup>fi</sup>er using the IMDb data version 1.0. Speci<sup>fi</sup>cally, TS-MBC was compared with four widely used classi<sup>fi</sup>ers in machine learning research: a Naïve Bayes classi<sup>fi</sup>er based on the multivariate Bernoulli distribution with Laplace prior for unseen words, discussed in Nigam et al. [28]; a support vector machine (SVM) classi<sup>fi</sup>er, discussed by Joachims [20]; an implementation of the voted perceptron, discussed in Freund and Schapire [13]; and a maximum entropy conditional random <sup>fi</sup>eld learner, introduced by Lafferty et al. [22]. The results are presented in Table 4.

Columns 2 and 3 of Table 4 compare the performance of TS-MBC with that of the other classi<sup>fi</sup>ers using the whole feature set as input. We observe that classification using the whole set of words vielded neither the highest accuracy nor the highest AUC, suggesting that more words may not necessarily lead to better performance. A possible explanation is that the classi<sup>fi</sup>ers were not able to distinguish discriminating words from noise. By contrast, TS-MBC selects 35 relevant words out of 7716 words in the vocabulary. The feature reduction ratio is 99.58%; the cross-validated AUC based on the 35 words and their dependencies is 87.52%, which is about 5% higher than the best of the other four methods; the corresponding crossvalidated accuracy is 78.08%, which is comparable to maximum entropy (79.43%) but less accurate than SVM (84.07%). As SVMs are known for better performance on larger sets of features, in such comparisons, it is reasonable to expect a good performance of the SVM with respect to the other classi<sup>fi</sup>ers.<sup>4</sup> However, because the sensitivity of SVM to the capacity parameter sharply restrict the breadth of their applicability, TS-MBC could be considered to offer a higher crossvalidation accuracy for data overall.

It is not clear, however, what the source is of the differences in the observed accuracies and AUC. A plausible argument could be that the

## Table 4

Average performances of various classi<sup>fi</sup>ers using a 5-fold cross-validation scheme, using all words, word subsets of various sizes selected by Information Gain, and the same set of words selected by the two-stage Markov Blanket Classi<sup>fi</sup>er. These results were obtained using the IMDb version 1.0 movie reviews data set used in Pang et al. [34]. Starred results (\*) are obtained on a subset of 26 words selected by MBC. The values in bold indicate the best performance in each column.

<table><tr><td rowspan="2">Words required</td><td colspan="2">Full set</td><td colspan="6">Words selected by Information Gain</td><td colspan="2">TS-MBC</td></tr><tr><td colspan="2">7716 words</td><td colspan="2">1000 words</td><td colspan="2">100 words</td><td colspan="2">35 words</td><td colspan="2">35 words</td></tr><tr><td>Method</td><td>AUC (%)</td><td>Accu. (%)</td><td>AUC (%)</td><td>Accu. (%)</td><td>AUC (%)</td><td>Accu. (%)</td><td>AUC (%)</td><td>Accu. (%)</td><td>AUC (%)</td><td>Accu. (%)</td></tr><tr><td>MBC</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>79.25*</td><td>69.33*</td></tr><tr><td>TS-MBC</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>87.52</td><td>78.08</td></tr><tr><td>Naïve Bayes</td><td>82.61</td><td>66.22</td><td>81.90</td><td>69.10</td><td>82.51</td><td>73.10</td><td>81.46</td><td>72.43</td><td>81.81</td><td>73.36</td></tr><tr><td>SVM</td><td>81.32</td><td>84.07</td><td>72.56</td><td>77.31</td><td>67.91</td><td>72.84</td><td>67.88</td><td>72.21</td><td>69.47</td><td>73.00</td></tr><tr><td>Voted perc.</td><td>77.09</td><td>70.00</td><td>79.62</td><td>71.82</td><td>79.95</td><td>72.30</td><td>78.68</td><td>71.71</td><td>80.61</td><td>73.93</td></tr><tr><td>Max. entropy</td><td>75.79</td><td>79.43</td><td>71.83</td><td>75.17</td><td>69.50</td><td>73.07</td><td>69.11</td><td>72.86</td><td>69.81</td><td>73.44</td></tr></table>

## Table 5

Performances of best TS-MBC classi<sup>fi</sup>er using a combination of unigrams and semantic features from DocuScope [8] compared to previously published results on the same data set— IMDb version 2.0 movie reviews used in Pang and Lee [32], containing 2000 movie reviews. Starred results (\*\*) were obtained with an earlier version of the data set—Pang et al. [34] version 1.0, containing 1400 movie reviews. The values in bold indicate the best performance in each column.

<table><tr><td>Method</td><td>Accuracy</td><td>St. dev.</td><td>Validation</td><td>Features (total number of features selected)</td></tr><tr><td>TS-MBC</td><td>92.70</td><td>±2.412</td><td>90/10 boot</td><td>Unigrams, bigrams, semantic features (76)</td></tr><tr><td>Abbasi et al. [1]</td><td>95.55</td><td>±2.969</td><td>10-fold cv</td><td>n-grams, syntactic, stylistic (1752)</td></tr><tr><td>Ng et al. [27]</td><td>90.50</td><td>-</td><td>10-fold cv</td><td>n-grams, adjectives polarity</td></tr><tr><td>Riloff et al. [36]</td><td>82.70**</td><td>-</td><td>3-fold cv</td><td>Unigrams, bigrams, extraction patterns</td></tr><tr><td>Whitelaw et al. [42]</td><td>90.20</td><td>-</td><td>10-fold cv</td><td>n-grams, attitude and orientation (49,911)</td></tr><tr><td>Pang and Lee [32]</td><td>87.20</td><td>-</td><td>10-fold cv</td><td>Subjective, objective sentences in IMDb versions 1.0 and 2.0)</td></tr><tr><td>Mullen and Collier [26]</td><td>86.00**</td><td>-</td><td>10-fold cv</td><td>Unigrams, topic proximity, syntactic-relations</td></tr><tr><td>Pang et al. [34]</td><td>82.90**</td><td>-</td><td>3-fold cv</td><td>Unigrams (16,165)</td></tr></table>

## Table 6

Average performances of various classi<sup>fi</sup>ers using all words, word subsets of various sizes selected by Information Gain, and the same set of words selected by the two-stage Markov Blanket Classi<sup>fi</sup>er. These are the results for the <sup>fi</sup>nancial online news data. Starred results (\*) are obtained on a subset of 27 words selected by MBC rather than using all of the input words. The values in bold indicate the best performance in each column.

<table><tr><td rowspan="2">Words required</td><td colspan="2">Full set</td><td colspan="6">Words selected by Information Gain</td><td colspan="2">TS-MBC</td></tr><tr><td colspan="2">11,220 words</td><td colspan="2">1000 words</td><td colspan="2">100 words</td><td colspan="2">36 words</td><td colspan="2">36 words</td></tr><tr><td>Method</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td></tr><tr><td>MBC</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>52.55*</td><td>65.09*</td></tr><tr><td>TS-MBC</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>59.83</td><td>73.21</td></tr><tr><td>Naïve Bayes</td><td>41.99</td><td>61.33</td><td>33.86</td><td>54.71</td><td>20.14</td><td>46.17</td><td>10.00</td><td>40.00</td><td>23.75</td><td>49.16</td></tr><tr><td>SVM(1-vs-all)</td><td>59.79</td><td>73.33</td><td>54.86</td><td>70.11</td><td>40.07</td><td>65.34</td><td>37.76</td><td>58.66</td><td>59.00</td><td>72.66</td></tr><tr><td>Poisson</td><td>55.25</td><td>70.16</td><td>55.42</td><td>69.57</td><td>41.26</td><td>65.18</td><td>38.10</td><td>59.12</td><td>44.99</td><td>63.33</td></tr><tr><td>Voted perc.</td><td>10.75</td><td>33.83</td><td>19.67</td><td>49.13</td><td>21.52</td><td>46.81</td><td>19.75</td><td>46.50</td><td>22.25</td><td>48.16</td></tr></table>

whole set of words were not the best set of words for the competing methods, so feature selection techniques could potentially improve performance of the methods. To investigate this point, we conducted two additional sets of experiments for the competing classi<sup>fi</sup>ers. In both sets of experiments, a feature selection criterion is <sup>fi</sup>rst used to select a subset of words from the vocabulary, and then feed the selected words into the competing classi<sup>fi</sup>ers as input features.

Speci<sup>fi</sup>cally, the <sup>fi</sup>rst set of classi<sup>fi</sup>cation results (from column 4 to column 9) is obtained using words selected by the Information Gain criterion. We use three subsets of words with the highest Information

## Table 7

Average performances of various classi<sup>fi</sup>ers using all words, word subsets of various sizes selected by Information Gain, and the same set of words selected by the two-stage Markov Blanket Classi<sup>fi</sup>er. These are the results for the mergers and acquisitions online news data. Starred results (\*) are obtained on a subset of 29 words selected by MBC rather than using all of the input words. The values in bold indicate the best performance in each column

<table><tr><td rowspan="2">Words required</td><td colspan="2">Full set</td><td colspan="6">Words selected by Information Gain</td><td colspan="2">TS-MBC</td></tr><tr><td colspan="2">10,531 words</td><td colspan="2">1000 words</td><td colspan="2">100 words</td><td colspan="2">43 words</td><td colspan="2">43 words</td></tr><tr><td>Method</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td></tr><tr><td>MBC</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>58.19*</td><td>66.01*</td></tr><tr><td>TS-MBC</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>62.99</td><td>75.32</td></tr><tr><td>Naïve Bayes</td><td>44.00</td><td>62.66</td><td>34.46</td><td>56.01</td><td>24.27</td><td>45.61</td><td>19.50</td><td>39.70</td><td>27.50</td><td>51.66</td></tr><tr><td>SVM(1-vs-all)</td><td>63.21</td><td>77.52</td><td>52.53</td><td>74.69</td><td>48.98</td><td>72.34</td><td>47.10</td><td>63.18</td><td>58.25</td><td>72.16</td></tr><tr><td>Poisson</td><td>59.75</td><td>73.16</td><td>56.81</td><td>73.12</td><td>48.57</td><td>64.96</td><td>46.75</td><td>64.50</td><td>48.75</td><td>65.84</td></tr><tr><td>Voted perc.</td><td>17.00</td><td>38.00</td><td>25.08</td><td>48.33</td><td>19.01</td><td>42.27</td><td>17.75</td><td>38.50</td><td>16.75</td><td>44.50</td></tr></table>

Table 8  
Average performances of various classi<sup>fi</sup>ers using all words, word subsets of various sizes selected by Information Gain, and the same set of words selected by the two-stage Markov Blanket Classi<sup>fi</sup>er. These are the results for the mixed online news data. Starred results (\*) are obtained on a subset of 31 words selected by MBC rather than using all of the input words. The values in bold indicate the best performance in each column.

<table><tr><td rowspan="2">Words required</td><td colspan="2">Full set</td><td colspan="6">Words selected by Information Gain</td><td colspan="2">TS-MBC</td></tr><tr><td colspan="2">15,685 words</td><td colspan="2">1000 words</td><td colspan="2">100 words</td><td colspan="2">43 words</td><td colspan="2">43 words</td></tr><tr><td>Method</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td><td>Kappa (%)</td><td>Accu. (%)</td></tr><tr><td>MBC</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>61.27*</td><td>69.86*</td></tr><tr><td>TS-MBC</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>65.03</td><td>76.68</td></tr><tr><td>Naïve Bayes</td><td>47.75</td><td>65.16</td><td>35.68</td><td>51.85</td><td>18.46</td><td>47.63</td><td>12.25</td><td>41.50</td><td>28.50</td><td>52.33</td></tr><tr><td>SVM(1-vs-all)</td><td>64.25</td><td>76.84</td><td>58.73</td><td>75.13</td><td>58.32</td><td>74.65</td><td>53.49</td><td>59.21</td><td>62.50</td><td>75.05</td></tr><tr><td>Poisson</td><td>57.75</td><td>71.84</td><td>58.14</td><td>74.61</td><td>42.83</td><td>61.84</td><td>39.00</td><td>59.33</td><td>44.99</td><td>63.33</td></tr><tr><td>Voted perc.</td><td>11.50</td><td>34.33</td><td>11.67</td><td>41.17</td><td>10.14</td><td>40.61</td><td>9.25</td><td>39.50</td><td>10.50</td><td>40.33</td></tr></table>

Gains, of sizes 1000, 100 and 35, respectively, in which 35 is the size of words selected by TS-MBC. The second set of classi<sup>fi</sup>cation results is obtained using the exact 35 words selected by TS-MBC (columns 10 and 11).

Comparing the results across columns of Table 4, we have the following observations: the accuracy of the various classi<sup>fi</sup>cation methods is typically increased when we use the 35 words selected by TS-MBC, as opposed to the top-35 words selected by IG. In addition, the accuracy obtained using the 35 words selected by TS-MBC is higher than the accuracy obtained using the top-100 IG words. Such results indicate that the words selected by the TS-MBC are more predictive of sentiments than those selected by IG. This pattern is consistent across Tables 6–8, as we show later in this section, adding support to our claim.

We also observe a non-negligible improvement in the performance by comparing the classi<sup>fi</sup>cation results of TS-MBC with those of MBC. The difference in the results between TS-MBC and MBC indicates that the <sup>fi</sup>rst-stage procedure alone is able to automatically identify a very well-discriminated subset of features (or words) that are relevant to the target variable (Y, the label of the review). Speci<sup>fi</sup>cally, the selected features are those that form the Markov Blanket for Y. However, in some cases it can be suboptimal in the space of Markov Blankets. With the Tabu search heuristic, it is able to search in larger solution spaces and therefore retrieve features that are predictive but were not selected by the <sup>fi</sup>rst-stage procedure.

Of particular interest to us are the comparisons of the results in columns 8 and 9 of Table 4 with those in columns 10 and 11. Columns 8 and 9 present classi<sup>fi</sup>cation results of the competing classi<sup>fi</sup>ers using the same number of words selected by Information Gain. In fact, Information Gain allows us to rank the features from most to least discriminating but gives no indication of how many words are correlated with the sentiment variable, signi<sup>fi</sup>cantly beyond chance. In this comparison, the results by TS-MBC (the highlighted numbers in columns 10 and 11) dominate the competing methods both in terms of AUC and accuracy, though it is not yet clear whether the superior performance comes from the different feature selection strategies, or from the dependencies encoded by the MB. To investigate this point, columns 10 and 11 in Table 4 compare the performance of TS-MBC with other classi<sup>fi</sup>ers using the same exact features selected by TS-MBC. We <sup>fi</sup>nd that the set of words selected as part of the Markov blanket contains more discriminative words for the sentiment variable; in fact, all four of the competing classi<sup>fi</sup>ers performed better on the set of features in the Markov blanket. Thus, these words are also signi<sup>fi</sup>cantly discriminative beyond pure chance.

So far we have examined the effect of TS-MBC as a classi<sup>fi</sup>er through comparisons against competing classi<sup>fi</sup>ers on different sizes of vocabularies that had been selected by Information Gain and by TS-MBC criteria. In the next batch of experiments, we compare the best performance of TS-MBC against those of the competing classi<sup>fi</sup>ers with their best sets of features, to examine the differential effect of TS-MBC as a feature selection procedure.

## 6.2.2. Comparing feature selection algorithms

We examine the performance of the TS-MBC as a feature selection method, and we then compare our method with several of the most recently developed feature selection algorithms: those by Gamon [15], Pang and Lee [32], Mullen and Collier [26], Whitelaw et al. [42], Ng et al. [27], Riloff et al. [36], and Abbasi et al. [1]. We use IMDb data version 2.0 for this batch of experiments. The version 2.0 IMDb data set we prepared for our experiments contains 2000 reviews with a vocabulary size of 8259 distinct words.

In Table 5 we report, for each method, the averages and, if available, the standard deviations of the cross-validated accuracy, the validation schema, the types of features, and the total number of features selected. We report the best performance of TS-MBC. The result is achieved by incorporating into the original unigram-feature set, an additional set of n-grams and semantic features that we obtained using DocuScope, a text tagging and visualization software developed by Collins and Kaufer at Carnegie Mellon University [9]. As a result, a total of 76 features are selected by TS-MBC. We reported the result for a hybrid bootstrap, cross-validation scheme; we retained the 90/10 split used by alternative methods, but repeated that split 1000 times, rather than repeating it 10 times as in the standard 10- fold cross-validation scheme. By doing so, we obtain a better estimate of variability of our results, while our average performance remains comparable to the published performances. The average crossvalidated accuracy is 92.70%, with a standard deviation of 2.4%. This result is better than most published results on the same data set, with the exception of Abbasi et al. [1], who have achieved an average accuracy of 95.55% with a standard deviation of 2.9% using 1752 features. We argue that our results may be considered comparable to those of Abbasi et al. [1]: despite the lower average accuracy, our results are less variable and were obtained with a substantially smaller feature set.

## 6.2.3. Performance on multi-class classification problems

We repeated the same battery of experiments on the online news corpora and present the results in Tables 6–8. From the results we obtained similar patterns. TS-MBC constantly yields comparable, and in some cases, better classi<sup>fi</sup>cation results when paired with any set of selected words, including the various sets of words selected by Information Gains as well as the exact set of words selected by TS-MBC. The SVM often outperforms competing methods in terms of accuracy, when used on the full set of words as features in the absence of any selection strategy applied, or with a large enough number of relevant features. TS-MBC often outperforms competing methods in terms of Kappa statistics, even when compared to Kappa statistics achieved by competing methods on the full set of words. The only exception is the voted perceptron in Table 8, 40.61% using the top-100 words selected by Information Gains, versus 39.50% when using the top-43 words selected by Information Gains, and 40.33% when using the 43 words selected by TS-MBC. Notice that AUC is for binary-class problems only; thus, we choose instead to report the Kappa statistics, which intuitively measure the incremental performance of a classi<sup>fi</sup>er with respect to the baseline accuracy. The baseline accuracy is the accuracy of randomly guessing the sentiment class, and in the threeclass problem, the expected accuracy is 33.33%.

Table 9  
Words selected from the movie reviews and online news data.

<table><tr><td>Data set</td><td># words selected</td><td>The selected words</td></tr><tr><td>Movie reviews</td><td>35</td><td>Also, again, as, awful, bad, bland, boring, both, but, dull, effective, even, had, if, its, just, lame, laughable, lifeless, maybe, memorable, mess, not, nothing, outstanding, perfect, solid, stupid, true, unfunny, wasted, world, without, worst, would</td></tr><tr><td>M&amp;A News</td><td>43</td><td>Add, after, against, all, also, as, be, been, billion, board, but, by, close, down, drop, expected, few, first, he, industry, latest, market, more, network, not, offer, officials, other, see, shareholders, strong, success, support, takeover, than, that, they, this, together, we, will, with, without</td></tr><tr><td>Finance News</td><td>36</td><td>Against, after, allowed, as, been, but, could, demand, expectations, for, from, funds, growth, have, he, may, no, not, officials, out, rose, pleased, positive, solid, some, strong, than, that, they, this, was, we, were, would, year, yet</td></tr><tr><td>Mixed News</td><td>43</td><td>Accuse, allegedly, around, as, but, court, do, down, even, form, good, great, had, arrest, if, important, it, its, just, more, my, new, not, our, police, project, result, sales, should, some, success, well, than, that, there, this, up, very, was, we, with, would, world</td></tr></table>

## 6.3. Discussion

The main <sup>fi</sup>ndings that emerge from our experimental results are as follows.

Dependencies amongst words play a crucial role in <sup>fi</sup>nding a parsimonious yet predictive vocabulary. The TS-MBC leads to better predictions by <sup>fi</sup>rst selecting statistically discriminating words with respect to the sentiment variable, and then learning those conditional dependencies among the words that lead to the emergence of sentiments in the texts. In settings where a parsimonious vocabulary of words is desired, the set of words that are selected by TS-MBC yields better prediction performance than those for the same number of words selected by Information Gain. As shown in the last four columns of Tables 4, 6, 7, and 8, comparing to the same number of words selected by Information Gain, the set of words selected by TS-MBC as predictors improves cross-validated accuracy, AUC, and Kappa statistics for all classi<sup>fi</sup>ers. The results are consistent for both the movie reviews data (two sentiments) and online news data (three sentiments).

TS-MBC tends to select words that are relevant and exportable. Table 9 lists the sets of words that are selected by TS-MBC from the movie reviews data<sup>5</sup> and the online news data. The results show that the TS-MBC procedure selects not only words that are intuitively important for predicting sentiments, e.g. important, success, positive, solid, expected, strong were selected, but also pairs of non-contextual words, e.g., no-but, or-not, POS-but, NEG-but etc. This pattern is particularly true in the three sets of features for the online news data. A counter-intuitive observation is that those non-contextual words, which were not deemed as important for predicting sentiments according to their Information Gain scores, were deemed to be distinctive features by TS-MBC procedure. We conjecture that this is due to the fact that sentiment classi<sup>fi</sup>cation is the task of predicting the overall sentiment, e.g., positive or negative, expressed in a document. While in theory topic and domain are expected to be orthogonal to sentiment, in practice it is found that within any given data set certain topic/domain words are invariably associated more strongly with one sentiment category than another. It is extremely dif<sup>fi</sup>cult to construct a data set where there is equal representation of every topic and sub-topic between the different sentiment categories.

Even if this were achieved, certain non-sentiment-bearing words will likely still be more strongly associated with one sentiment category.

Consider, for instance, a collection of news collected during 2003– 2004; in such a collection, the word Iraq is more likely to be associated with negative sentiment, despite the fact that such an association is purely topic- and time-dependent. Most research in sentiment classi<sup>fi</sup>cation has, whether intentionally or not, involved texts about the same topic or from the same domain. The feature selection methods that are commonly used to complement the proposed classi<sup>fi</sup>ers (e.g., Information Gain, $\chi ^ { 2 }$ statistics) process the words independently, which may be one of the reasons behind the poorer performance exhibited by the words selected according to the Information Gain criterion. Our algorithm is able to learn predominant sentiments conveyed in the text of online documents (such as news or posts), which is based on the dependencies among words, and therefore, the sentiment patterns are less “topic-dependent.” As both the $G ^ { 2 }$ test of independence and the use of binary variables to encode presence/absence of words are well suited to selecting a topicindependent vocabulary, words that capture linguistic issues such as negation and comparisons appear in the selected vocabularies. However, we observed only a modest overlap between the selected vocabularies across the data sets. One possible reason is that, given the small number of documents in each of the data sets, a small subset of words may yield very good performance on one speci<sup>fi</sup>c data set but different ones for different collections. More experiments on a larger number of corpora with more documents are needed in order to substantiate stronger claims.

Tabu search improves the prediction performance. The results from both the movie reviews data and the online news corpora show nonnegligible improvements of the prediction performance, when Tabu search is paired with the <sup>fi</sup>rst-stage procedure (MBC). As shown in the <sup>fi</sup>rst two rows of Tables 4, 6, 7 and 8, although the MBC procedure by itself can identify a discriminating subset of words, the Tabu searchenhanced procedure (TS-MBC) identi<sup>fi</sup>es the sets of words that improve both the accuracy and the AUC or Kappa statistics in all the experiments. This is due to the fact that the Tabu search heuristic has several favorable properties because of its adaptive memory capability, and it appears particularly suited to the Bayesian Networks and Markov Blanket approaches. Tabu search does not stop at the <sup>fi</sup>rst local optimum, whereas local heuristic searches such as Best First Search (BFS) do. In this sense, the Tabu search heuristic searches a bigger space in general. Further, Tabu search incorporates effective strategies for driving the search away from previously visited regions. A simple means of doing this, for example, is to dynamically control the size of the tabu list: the longer the list is, the further away the solutions are. Therefore, by just keeping m previous moves instead of m previous solutions (MBs), TS prevents revisiting the m most recent solutions. The smart use of dynamic memory is one of the key factors contributing to the ef<sup>fi</sup>ciency and effectiveness of our procedure.

The prediction performance of our method is consistent for binary and multi-classi<sup>fi</sup>cation problems. The results of comparisons with benchmark classi<sup>fi</sup>ers and feature selection methods show that our method performs consistently well on both the two versions of the online movie reviews data and the three sets of online news. We note that our method is robust in multi-class classi<sup>fi</sup>cation problems. Our investigations generalize previous attempts at multi-class classi<sup>fi</sup>cation in existing literature, particularly because our method is effective for both binary-class and three-class problems, and our results are shown to be consistently robust in both problem settings while previous works have only focused on binary classi<sup>fi</sup>cation problems.

## 7. Conclusions

This paper proposed a computationally ef<sup>fi</sup>cient and effective prediction model for multi-class sentiment classi<sup>fi</sup>cation in a setting with few samples and high dimensional attributes. The proposed model is able to select a parsimonious vocabulary, well suited for the classi<sup>fi</sup>cation tasks in terms of size and relevant features; it is able to capture the conditional dependencies among words while selecting the vocabulary, and learns the correct Markov blanket for the sentiment variable in the large sample limit. The complexity of this model is linear in the number of samples, which in our case is the number of training documents. The computational results suggest that words that occur often, along with their conditional dependencies and a few strong adjectives, constitute most of the vocabulary needed to express sentiments and perform reasonable predictions. As a feature selection method, our model identi<sup>fi</sup>es vocabularies that enhance the predictive performance of several popular classi<sup>fi</sup>ers when compared to vocabularies selected with Information Gain. When paired with logistic regression to perform classi<sup>fi</sup>cation, for instance, our method yields predictive performance comparable and in many cases superior to those of other state-of-the-art classi<sup>fi</sup>cation methods. Most importantly, the small size of the vocabulary allows for interpretability and understandability. In summary, in order to capture sentiments, a method needs to move beyond the search for richer feature sets while maintaining the independence assumption. It is rather crucial to capture those dependencies among words that lead to the emergence of context and meaning.

Possible future directions of this work include: validating our approach on larger data sets, with more sentiment categories and shorter texts, for instance, sentence-level sentiment analysis; exploring cross-genre applicability, which could generate powerful tools for predicting emerging trends, potential cyber crime, as well as cyber risk management, in which data samples are extremely dif<sup>fi</sup>cult to obtain; examining the effect of pre-processing techniques for generating an initial set of features on the performance of feature selection and classi<sup>fi</sup>cation, including the use of stemming, lemmatization or thesauri, as well as the use of generalized features for nonwords, such as numbers, dates and punctuation; and developing algorithms that would allow the search to reach global optima starting from documents with one speci<sup>fi</sup>c level of topicality or one speci<sup>fi</sup>c language, and yield consistently optimal feature sets for predicting sentiments across topicality or language of the documents.

## Acknowledgments

The author wishes to thank William Cohen, Ramayya Krishnan, Clark Glymour, Rema Padman, Joseph Ramsey, and Peter Spirtes of Carnegie Mellon University, and Edoardo M. Airoldi of Harvard University, for the helpful discussions and insights; Lillian Lee and Bo Pang at Cornell University for the helpful discussions and suggestions; Roy Lipski for the helpful suggestions and for the sharing the online news data, prepared by Infonic Ltd.; and the anonymous Decision Support Systems reviewers for the helpful comments.

## Appendix A. Subprocedures of the LrnTSMBC algorithm

Below we present the four subprocedures used in the LrnTSMBC algorithm in Section 4.2.

Adj (Node Y, Node List L, Depth δ, Signi<sup>fi</sup>ance α)

1. $\mathsf { A } _ { \mathsf { Y } } : = \{ X _ { i } \in L \colon X _ { i }$ is dependent of Y at level α}

2. for $X _ { i } { \in } A _ { Y }$ and for all distinct subsets $S \subset \{ A _ { Y } | X _ { i } \} ^ { d }$ 2.1. $i f X _ { i }$ is independent of Y given S at level α 2.2. then remove $X _ { i }$ from $A _ { Y }$

3. for $\boldsymbol { X _ { i } } { \in } \boldsymbol { A _ { Y } }$

3.1. $A _ { X _ { i } } { : = } \{ X _ { j } { \in } L \colon X _ { j }$ is dependent of $X _ { i }$ at level $\alpha , j \neq i \}$

3.2. for all distinct subsets $S \subset \{ A _ { X _ { i } } \} ^ { d }$

3.2.1. $i f X _ { i }$ is independent of Y given S at level α

3.2.2. then remove $X _ { i }$ from $A _ { Y }$

4. return A<sub>Y</sub>

Ornt (Graph G)

Apply the following 4 rules iteratively wherever it applies:

1. Rule 1 (Collider Orientation Rule): for each triple of vertices $( X , V , Z )$ in G, if pair (X, V) and (V, Z) are adjacent, pair (X, Z) are not adjacent (i.e. a pattern: X–V–Z), and if V∉SepSet(X,Z), then orient X–V–Z as $X { \right. } V { \left. } Z ^ { 6 }$

2. Rule 2: for each triple of vertices (X, V, Z) in G, if X→V and V, Z are adjacent, X, Z are not adjacent (i.e. a pattern $X  V - Z )$ , and there is no arrow into V, then orient V–Z as V→Z.

3. Rule $3 \colon i f \left( X \to Z \to V \right)$ , and ∃ (undirected edge between X and V, i.e. pattern X–V), then orient X–V as X→V

4. Rule 4: for any undirected edge connected to $X ( \mathrm { i . e . } X \mathrm { - } V ) , i f \exists ( Z , W )$ s.t. Z is adjacent to X, W is adjacent to X, Z is not adjacent to W, and there is a pattern $W { \right. } V { \left. } Z ,$ then orient X–V as $X  V$

Trsfm (Graph G, Target Y)

1. for any X in $G \ S . \mathrm { t } . \ X \longleftrightarrow Y$ or X–Y, reorient this edge as $X \to V$

2. for any $X , ~ Z$ in G s.t. $Z - X \to V ,$ where $Z \not \in \{ Y \} \cup$ ParentChild(Y), remove the edge Z–X

3. for any $X , X { \not \in } \{ Y \}$ ∪ParentChild(Y)∪ParentChild(ParentChild(Y)) 3.1. remove X and all the associated edges

4. return G

TabuSrch $( M B _ { D A G } , L , M a x _ { I t e r } )$

1. init: $b e s t _ { M B } = c u r r _ { M B } = M B _ { D A G } , b e s t _ { S c o r e } = 0$

2. repeat until $( b e s t _ { S c o r e }$ does not improve for k consecutive iterations) 2.1. form $c a n d i d a t e _ { M o v e s } \mathrm { f o r } c u r r _ { M B }$

2.2. find $b e s t _ { M o v e }$ among candidat $e _ { M o v e s }$ according to function score 2.3. $i f \left( b e s t _ { S c o r e } { < } s c o r e \ ( b e s t _ { M o v e } ) \right)$ 2.3.1. update $b e s t _ { M B } ,$ by applying $b e s t _ { M o v e } ,$ and $b e s t _ { S c o r e }$ 2.3.2. add $b e s t _ { M o v e }$ to TabuList

2.4. update current<sub>M B</sub> by applying $b e s t _ { M o v e }$

3. return best<sub>MB</sub>

## References

[1] A. Abbasi, H. Chen, A. Salem, Sentiment analysis in multiple languages: feature selection for opinion classi<sup>fi</sup>cation in web forums, ACM Transactions on Information and Systems 26 (2008).

[2] E.M. Airoldi, A.G. Anderson, S.E. Fienberg, K.K. Skinner, Who wrote Ronald Reagan radio addresses? Bayesian Analysis 1 (2006) 289–320.

[3] E.M. Airoldi, S.E. Fienberg, K.K. Skinner, Whose ideas? Whose words? Authorship of the Ronald Reagan radio addresses, Political Science & Politics 40 (2007) 501–506.

[4] E.M. Airoldi, X. Bai, R. Padman, Markov-blanket and meta-heuristic search: sentiment extraction from unstructured text, Lecture Notes in Computer Science, vol. 3932, Springer-Verlag, 2006, pp. 167–187.

[5] X. Bai, Tabu search enhanced graphical models for classi<sup>fi</sup>cation of high dimensional data, Technical Report CMU-CALD-05-101, School of Computer Science, Carnegie Mellon University, 2005.

[6] X. Bai, R. Padman, J.D. Ramsey, P. Spirtes, Tabu search enhanced graphical models for classi<sup>fi</sup>cation in high dimensions, INFORMS Journal on Computing 20 (3) (2008) 423–437.

[7] J. Carletta, Assessing agreement on classi<sup>fi</sup>cation tasks: the kappa statistic, Computational Linguistics 22 (1996) 249–254.

[8] H. Chen, Intelligence and Security Informatics for International Security: Information Sharing and Data Mining, Springer Press, London, 2006.

[9] J. Collins, D.F. Kaufer, Docu-Scope: a Java application for statistical literary style modeling, Technical Report, Carnegie Mellon University, 2001.

[10] G. Cooper, C. Aliferis, J. Aronis, B. Buchanan, R. Caruana, M. Fine, C. Glymour, G. Gordon, B. Hanusa, J. Janosky, C. Meek, T. Mitchell, T. Richardson, P. Spirtes, An evaluation of machine-learning methods for predicting pneumonia mortality, Arti<sup>fi</sup>cial Intelligence in Medicine 9 (1992) 107–139.

[11] S. Das, M. Chen, Yahoo! for Amazon: sentiment parsing from small talk on the web, Proceedings of the Eighth Asia Paci<sup>fi</sup>c Finance Association Annual Conference, APFA, 2001.

[12] K. Dave, S. Lawrence, D. Pennock, Mining the peanut gallery: opinion extraction and semantic classi<sup>fi</sup>cation of product reviews, Proceedings of the Twelfth International Conference on World Wide Web, 2003, pp. 519–528.

[13] Y. Freund, R. Schapire, Large margin classi<sup>fi</sup>cation using the perceptron algorithm, Machine Learning 37 (1999) 277–296.

[14] N. Friedman, D. Geiger, M. Goldszmidt, Bayesian network classi<sup>fi</sup>ers, Machine Learning 29 (1997) 131–163.

[15] M. Gamon, Sentiment classi<sup>fi</sup>cation on customer feedback data: noisy data, large feature vectors, and the role of linguistic analysis, COLING '04: Proceedings of the 20th International Conference on Computational Linguistics, Morristown, NJ, USA, Association for Computational Linguistics, 2004, p. 841.

[16] F. Glover, Tabu Search, Kluwer Academic Publishers, 1997.

[17] V. Hatzivassiloglou, K. McKeown, Predicting the semantic orientation of adjectives, Proceedings of the Eighth Conference on European Chapter of the Association for Computational Linguistics, ACL, 1997, pp. 174–181.

[18] A.R. Hedar, J. Wang, M. Fukushima, Tabu search for attribute reduction in rough set theory, Soft Computing — A Fusion of Foundations, Methodologies and Applications 12 (2008) 909–918.

[19] A. Huettner, P. Subasic, Fuzzy typing for document management, Association for Computational Linguistics 2000 Companion Volume: Tutorial Abstracts and Demonstration Notes, 2000, pp. 26–27.

[20] T. Joachims, A statistical learning model of text classi<sup>fi</sup>cation with support vector machines, Proceedings of the Conference on Research and Development in Information Retrieval, ACM, 2001, pp. 128–136.

[21] Komarek, P., Moore, A.: Making logistic regression a core data mining tool (2005) manuscript.

[22] J. Lafferty, A. McCallum, F. Pereira, Conditional random <sup>fi</sup>elds: probabilistic models for segmenting and labeling sequence data, Proceedings of the Eighteenth International Conference on Machine Learning, 2001, pp. 282–289.

[23] H. Liu, H. Lieberman, T. Selker, A model of textual affect sensing using real-world knowledge, Proceedings of the Eighth International Conference on Intelligent User Interfaces, 2003, pp. 125–132.

[26] T. Mullen, N. Collier, Sentiment analysis using support vector machines with diverse information sources, Proceedings of Empirical MEthods in Natural Language Processing, 2004, pp. 412–418.

[27] V. Ng, S. Dasgupta, S.M.N. Ari<sup>fi</sup>n, Examining the role of linguistic knowledge sources in the automatic identi<sup>fi</sup>cation and classi<sup>fi</sup>cation of reviews, Proceedings of the COLING/ACL on Main Conference Poster Sessions, Morristown, NJ, USA, Association for Computational Linguistics, 2006, pp. 611–618.

[28] K. Nigam, A. McCallum, S. Thrun, T. Mitchell, Text classi<sup>fi</sup>cation from labeled and unlabeled documents using EM, Machine Learning 39 (2000) 103–134.

[29] Online movie reviews data. http://www.cs.cornell.edu/people/pabo/moviereviewdata/.

[30] Online news data. http://www.infonic.com/.

[31] C. Osgood, G. Suci, P. Tannenbaum, The Measurement of Meaning, University of Illinois Press, Chicago, Illinois, 1957.

[32] B. Pang, L. Lee, A sentimental education: sentimental analysis using subjectivity summarization based on minimum cuts, Proceedings 42nd Annual Meeting of the Association for Computational Linguistics, 2004, pp. 271–278.

[33] B. Pang, L. Lee, Sentimental Extraction and Opinion Analysis, Springer Press, London, 2009.

[34] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up? Sentiment classi<sup>fi</sup>cation using machine learning techniques, Proceedings of the 2002 Conference on Empirical Methods in Natural Language Processing, 2002, pp. 79–86

[35] J. Pearl, Causality: Models, Reasoning, and Inference, Cambridge University Press, 2000.

[36] E. Riloff, S. Patwardhan, J. Wiebe, Feature subsumption for opinion analysis, EMNLP '06: Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing, Morristown, NJ, USA, Association for Computational Linguistics, 2006, pp. 440–448

[37] P. Spirtes, C. Glymour, R. Scheines, Causation, Prediction, and Search, MIT Press, 2000.

[38] P. Spirtes, C. Meek, Learning bayesian networks with discrete variables from data, Proceedings of the First International Conference on Knowledge Discovery and Data Mining, AAAI Press, 1995, pp. 294–299.

[39] P. Toth, D. Vigo, The granular Tabu search and its application to the vehicle routing problem, INFORMS Journal on Computing 15 (4) (2003) 334–346.

[40] P. Turney, Thumbs up or thumbs down? Semantic orientation applied to unsupervised classi<sup>fi</sup>cation of reviews, Proceedings Fortieth Annual Meeting of the Association for Computational Linguistics, 2002, pp. 417–424.

[41] P. Turney, M. Littman, Unsupervised learning of semantic orientation from a hundred-billion-word corpus, Technical Report EGB-1094, National Research Council, Canada, 2002.

[42] C. Whitelaw, N. Garg, S. Argamon, Using appraisal groups for sentiment analysis, Proceedings of the 14th ACM Conference on Information Knowledge Management, 2005, pp. 625–631.
