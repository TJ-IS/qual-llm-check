---
otero_id: 21449
otero_key: "C3SFRDTY"
title: "Discovering and using knowledge from unsupervised data"
authors: "Tu Bao Ho"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00011-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Discovering and using knowledge from unsupervised data

Tu Bao Ho \*

Japan Advanced Institute of Science and Technology, Tatsunokuchi, Ishikawa, 923-12 Japan

## Abstract

Though most knowledge discovery methods have been developed for supervised data, the task of finding knowledge from unsupervised data often arises in real-world situations. Without feedback about the appropriateness of discovered knowledge as in supervised systems, techniques for unsupervised knowledge discovery are essentially different and still much less developed than those for supervised discovery. In this paper we present a method for discovering and using classificatory knowledge from unsupervised data. We first extended the classical view on concepts commonly used in the framework of the Galois lattice by combining it with the prototype and exemplar views, and develop an algorithm for inducing concept hierarchies. We then introduce a procedure that combines matching approaches in inductive learning with case-based reasoning in order to classify unknown cases, using discovered knowledge. We present the implementation of the method as an interactive system. An experimental comparative study of some knowledge discovery systems, in terms of knowledge description and prediction, shows advantages and application potential of the method in decision-making. © 1997 Elsevier Science B.V.

Keywords: Knowledge discovery; Unsupervised data; Views on concepts; Concept hierarchy; Matching approaches; Case-based reasoning

## 1. Introduction

As knowledge is of central importance in intelligent systems, to acquire useful knowledge is a crucial problem in the development of knowledge-based decision support systems $[7,30]$ . Recently, knowledge discovery in databases (KDD) has emerged as a rapidly growing interdisciplinary field that merges together techniques of databases, statistics and machine learning in order to find useful knowledge from databases, and KDD has shown its application potential in various domains $[8,10]$ .

Knowledge discovery techniques depend entirely on the degree of supervision in data. Most early works in knowledge discovery focused on supervised tasks that aimed at finding descriptive knowledge of concepts given their labelled instances. Supervised discovery methods are always driven by feedback about the appropriateness of discovered knowledge obtained from classified data. Moreover, knowledge discovered from supervised data is often represented in flat structures such as conjunctions of conditions $[26]$ , production rules [6], or in a decision tree structure [3,28], that lead to relatively simple ways of using knowledge (final rules or leaf nodes in decision trees) in predicting classes of unknown cases. However, in real-world situations the unsupervised discovery task can also arise quite often, like when the task aims at finding ‘natural’ classes in databases with their descriptions where feedback about the appropriateness of discovered knowledge cannot be obtained from the data. Essentially, unsupervised knowledge discovery concerns two mutual problems: (1) hierarchical clustering (i.e., finding a hierarchy of useful subsets of unlabelled instances), and (2) characterization (i.e., finding an intensional definition for each of these instance subsets). Consequently, knowledge from unsupervised data seems suitable to be discovered in hierarchical structures such as concept hierarchies, which influence the ways of predicting unknown cases (where many concepts can be detected and used at intermediate levels [17]).

Techniques of unsupervised discovery are essentially characterized by the search for regularities in data and are still much less developed than those of supervised discovery $[22]$ . Basically, unsupervised discovery methods depend strongly on how concepts are understood and represented. Among views on concepts in cognitive science and machine learning, the classical, prototype and exemplar ones are widely known and used $[19,31]$ . Moreover, unsupervised discovery systems compose solutions to the problem by employing one or more of the three main categorization constraints based on similarity, feature correlation $[12]$ , and syntactical structure of the concept hierarchy $[24]$ . The properties of concepts, main strengths and limitations of views on concepts and categorization constraints are given in Table 1, which are summarized in Refs. $[19,31,33]$ .

COBWEB [9] and AUTOCLASS [5] are often referred to as typical unsupervised learning methods which employ the probabilistic (prototype) representation for concepts. COBWEB organizes data so as to maximize inference ability, and AUTOCLASS uses a Bayesian method for determining the optimal classes. CLUSTER/2 [26] is an early influential conceptual clustering method that employs the classical view on concepts to form categories with 'good' conjunctions of features common to all category members. Recently, several concept learning systems have been developed using the classical view on concepts in the Galois lattice structure. In the GALOIS system [4] and in Ref. [11], all possible concepts in the Galois lattice are incrementally generated. Although the Galois lattice provides a powerful structure for discovering concepts, this framework has considerable limitations in KDD, where the user often has to deal with large databases. The search for all possible formal concepts is perhaps not always tractable as in worse cases where the number of concepts can be exponential in the number of instances and attributes. For example, with the commonly used data set of Congressional voting of 435 instances described by 16 attributes, the Galois lattice consists of about 150,000 nodes that reaches the space limit of a Sparcstation LX equipped with 32 Mb of RAM and the execution time increases dramatically [4]. Moreover, the classical representation of concepts in the Galois lattice does not capture the typicality effects and vagueness. In Ref. [16], an alternative approach to hierarchical conceptual clustering, which extracts a part of the Galois lattice in the form of a concept hierarchy, is proposed.

As analysed in Ref. [31], each system which relies on a single view on concepts has several limitations in capturing the rich variety of conceptual knowledge. Therefore, hybrid systems are an attempt to improve the concept learning process by combining fairly different theoretical views on concepts and constraints of categorization.

The two primary goals of discovery systems in practice are description and prediction [8]. Description focuses on finding human-interpretable patterns describing the data, and relates to the understandability of knowledge. Prediction involves using some variables or fields in the database to predict unknown or future values of other variables of interest. The first lesson learned from real databases in Ref. [5] is that “‘discovery of patterns in data is only the beginning of a cycle of interpretation followed by more testing’”. Though the procedure of using the results of knowledge discovery in prediction is an important issue in practice [22], there has been so far little work in KDD associated with procedures for exploiting discovered knowledge, e.g., Refs. [1,34].

Current discovery systems do not always equate human ability in identifying useful concepts, and as the search problem in such a complex process requires much background knowledge and heuristics, the human factor in discovery process is always necessary. Without feedback obtained from the data about discovered knowledge, unsupervised discovery systems cannot produce maximally useful results when operating alone. The ability to interact with the user allows considerable improvements in the performance of discovery systems $[20,23,35]$ .

Table 1  
Properties, views on concepts and categorization constraints

<table><tr><td colspan="2">Features listing</td></tr><tr><td>Nonnecessary features</td><td>Features are true only for some/most of concept members.</td></tr><tr><td>Disjunctive concepts</td><td>Perhaps no feature shared by all concept members.</td></tr><tr><td>Relational information</td><td>Features are about object&#x27;s function/relation to others.</td></tr><tr><td>Features as concepts</td><td>Features are not only atomic units of description.</td></tr><tr><td colspan="2">Internal structure</td></tr><tr><td>Typicality</td><td>Concept members have different typical/representative roles.</td></tr><tr><td>Basic levels</td><td>Many concepts are viewed at an intermediate level.</td></tr><tr><td>Superordinate distance</td><td>Concept is not always rated most similar to its parents.</td></tr><tr><td colspan="2">Categorization</td></tr><tr><td>Unclear cases</td><td>Concept membership varies in different objects.</td></tr><tr><td>Context effects</td><td>Categorization depends on context (available information).</td></tr><tr><td>Multiple categorization</td><td>Many categories could apply to an object.</td></tr><tr><td>Classical view</td><td>Concepts are viewed by necessary and sufficient features</td></tr><tr><td>Strengths</td><td>Clear semantics, used by standard logic.</td></tr><tr><td>Limitations</td><td>Difficult to specify defining features in many cases, does not capture typicality effects and vagueness.</td></tr><tr><td>Prototype view</td><td>Concepts are viewed by most common or typical features</td></tr><tr><td>Strengths</td><td>Generality, flexibility.</td></tr><tr><td>Limitations</td><td>Does not preserve enough information, does not address context effects and explain concept coherence.</td></tr><tr><td>Exemplar view</td><td>Concepts are viewed by individual examples</td></tr><tr><td>Strengths</td><td>Conserve information and context sensitivity.</td></tr><tr><td>Limitations</td><td>Ignore generalization, does not explain the concept coherence.</td></tr><tr><td>Similarity constraint</td><td>Categories consist of similar objects</td></tr><tr><td>Correlation constraint</td><td>Maximize intra-correlations and minimize inter-correlations</td></tr><tr><td>Structure constraint</td><td>Syntactical structure of the entire conceptual system</td></tr></table>

The motivation of this work is to extend and develop the unsupervised discovery method OSHAM introduced in Ref. [16], according to the aspects mentioned above. Three themes about discovering knowledge, using knowledge, system implementation and evaluation will be addressed in this paper. In Section 2, we enrich the classical view on concepts in the Galois lattice by several features of the prototype and exemplar views, and develop an algorithm for inducing a concept hierarchy from the Galois lattice. In Section 3, we propose a procedure for using discovered knowledge to classify unknown cases based on an integration of matching approaches in inductive learning with case-based reasoning. In Section 4, we present the implementation of method in the X Window with the direct manipulation style of interaction, and an experimental comparative study of some knowledge discovery methods in terms of knowledge description and prediction accuracy. In Section 5, we address the application potential of the method in decision-making and conclusions.

## 2. Discovering knowledge from unsupervised data

## 2.1. Representing concepts

A database is a collection of data organized logically into files or tables of fixed-length records (objects), described by a set of attributes. Each attribute is defined with a set of potential values known as its domain. Information about attributes and their domains is often maintained in a separate data dictionary. Each record is an ordered list of values, one value for each field. A tuple is a conjunction of attribute-value pairs.

For simplicity of representation, we limit ourselves in considering a single relational database. Denote by $\mathcal{O}$ the set of all objects (records), $\mathcal{A}$ the set of all attributes, and $\mathcal{T}$ the set of all possible tuples in the database. For any object subset $X \subseteq \mathcal{O}$ , the largest tuple common to all objects in $X$ is denoted by $\lambda(X)$ . For any tuple $S \in \mathcal{T}$ , the set of all objects satisfying $S$ is denoted by $\rho(S)$ . A tuple $S$ is closed if $\lambda(\rho(S)) = S$ .

The basis of the maximum understanding of a concept is the function of collecting individuals into a group with certain common properties. One distinguishes these common properties as the intent of the concept that determines its extent, which are the objects accepted as members of the concept. Formally, a concept C, in the classical view, is a pair $(X, S)$ , $X \subseteq O$ and $S \subseteq T$ , satisfying $\rho(S) = X$ and $\lambda(X) = S$ . X and S are then called extent and intent of C, respectively. Concept $(X_{2}, S_{2})$ is a subconcept of concept $(X_{1}, S_{1})$ if $X_{2} \subseteq X_{1}$ which is equivalent to $S_{2} \supseteq S_{1}$ , and $(X_{1}, S_{1})$ is then a superconcept of $(X_{2}, S_{2})$ . For simplicity of representation, we sometimes call the direct superconcepts (father concepts) and the direct subconcepts (son concepts) of a concept by superconcepts and subconcepts, respectively.

It was mathematically shown that the set of all possible concepts associated with the superconcept-subconcept relationship has the structure of a complete lattice (also called the Galois lattice). $\lambda$ and $\rho$ define a Galois connection between the power sets $\mathcal{L}^{\mathcal{O}}$ and $\mathcal{L}^{\mathcal{A}}$ , i.e., they are two order-reversing one-to-one operators [32]. To overcome the limitations of the classical representation of concepts in the Galois lattice, we enrich this representation by adding several components based on the prototype and exemplar views on concepts that allow dealing better with typical or unclear cases in the region boundaries, and propose a clustering method to extract a concept hierarchy in the Galois lattice of possible concepts.

A concept hierarchy $\mathcal{H}$ is a part of the concept lattice satisfying the following properties (1) the root concept $(\mathcal{O}, \lambda(\mathcal{O})) \in \mathcal{H}$ ; (2) if $C_1 = (X_1, S_1)$ , $C_2 = (X_2, S_2) \in \mathcal{H}$ and $X_1 \cap X_2 \neq \emptyset$ then either $C_1$ is a subconcept of $C_2$ or $C_2$ is a subconcept of $C_1$ . Note that the property $(\{o\}, \lambda(o)) \in \mathcal{H}$ for every $o \in \mathcal{O}$ in the usual definition of the hierarchy structure is not necessarily required here as for the generalization purpose, many concepts at high levels need to be pruned.

A concept hierarchy is formed by OSHAM in the top-down direction with different levels of generality, from the most general (root concept) to the most specific concept (leaf concept) in each branch. Associated with each concept $C_k$ are the level $l(C_k)$ , two lists of its direct superconcepts $f(C_k)$ and direct subconcepts $s(C_k)$ . The intent $i(C_k)$ is inherited by all subconcepts $C_{k_i}$ of $C_k$ , and thus the intent of each subconcept $C_{k_i}$ is the conjunction of $i(C_k)$ with selected attribute-value pairs. The extent $e(C_k)$ is classified into extent of its subconcepts $C_{k1}, C_{k2}, \ldots, C_{k_n}$ at higher levels in the process of analyzing $C_k$ into subconcepts. In fact, this is a process of searching for regularities among instances of $C_k$ in determining good non-necessary features that correspond to useful subconcepts of $C_k$ . In this process, it may happen that some instances of $C_k$ do not satisfy the features of any subconcept $C_{k_i}$ , and so will not be classified as instances of any subconcept $C_{k_i}$ . We call these local instances of $C_k$ and denote this set by $C_k^r = e(C_k) \setminus \bigcup_{i=1}^{n} e(C_{K_i})$ . In fact, OSHAM splits each concept $C_k$ into subconcepts until the set $C_k^r$ satisfies some unsplittable conditions. The probability of occurrence $p(C_k)$ of $C_k$ and the conditional probability $p(C_k^r | C_k)$ of local instances in $C_k$ are of interest as they will be used later in the prediction of unknown instances.

Without class attribute to drive the search, unsupervised discovery techniques often exploit the relation between intra-similarity and inter-similarity among concepts. The distance $\delta(o_{p}, o_{q})$ between two instances $o_{p}$ and $o_{q}$ is defined as an extension of the Jaccard distance [2], suitably in the Galois lattice

$$
\delta \left(o _ {p}, o _ {q}\right) = 1 - \frac {\sum_ {a \in \lambda \left(\left\{o _ {p} , o _ {q} \right\}\right)} \gamma (a)}{\sum_ {a \in \lambda \left(\left\{o _ {p} \right\}\right) \cup \lambda \left(\left\{o _ {q} \right\}\right)} \gamma (a)}\tag{1}
$$

where $\gamma(a)\in\mathbb{Z}^{+}$ are positive integer weights of attributes a (with a value of 1 by default). The attribute weights $\gamma(a)$ embody background knowledge about the environment and concepts (importance of attributes, attribute rank by potential relevancy, etc.). The dispersion $d(C_{k})$ between instances in $e(C_{k})$ , considered as the inverse of the homogeneity of $e(C_{k})$ , is defined as the average distance between all pairs of instances in $e(C_{k})$ .

$$
d \left(C _ {k}\right) = \frac {2 \times \sum_ {o _ {p} , o _ {q} \in e \left(C _ {k}\right)} \delta \left(o _ {p} , o _ {q}\right)}{\left| e \left(C _ {k}\right) \right| \times \left| e \left(C _ {k}\right) - 1 \right|}\tag{2}
$$

If $C_k$ is a non-leaf concept, its local instances in $C_k^r$ may be considered to be more typical and representative than its instances classified into subconcepts $C_{k_i}$ . As an instance, $o$ is a member of different concepts along a branch in the concept hierarchy, the concept $C_k$ that $o \in C_k^r$ is of particular interest. If $C_k$ is a leaf concept, we have $e(C_k) = C_k^r$ and its instances are all considered to have the same representative role.

The extent of all direct subconcepts $C_{k_1}, C_{k_2}, \ldots, C_{k_n}$ of $C_k$ and the set of local instances $C_k^r$ form a partition $P$ of $e(C_k)$ . Denote by $W(C_k)$ the average of all $d(C_{k_i})$ and $d(C_k^r)$ . The dissimilarity between subconcepts of $C_k$ , denoted by $B(C_k)$ , is defined as the average of distances $\Delta\big(c(C_{k_i}), c(C_{k_j})\big)$ between all pairs $(C_{k_i}, C_{k_j}) \in P$ , where the distance $\Delta\big(c(C_{k_i}), c(C_{k_j})\big)$ is determined as the smallest distance among the distances of all pairs of instances $o_p \in C_{k_i}$ and $o_q \in C_{k_j}$ .

$$
\Delta \left(c \left(C _ {k _ {i}}\right), c \left(C _ {k _ {j}}\right)\right) = \operatorname{Min} _ {o _ {p} \in C _ {k _ {i}}, o _ {q} \in C _ {k _ {j}}} \delta \left(o _ {p}, o _ {q}\right)\tag{3}
$$

The quality of splitting a concept $C_k$ into subconcepts in the next level, denoted by $q(C_k)$ , is measured by $q(C_k) = W(C_k) / B(C_k)$ (4)

Summarily, OSHAM represents each concept $C_{k}$ in the concept hierarchy by a 10-tuple of the following components

$$
\langle l \left(C _ {k}\right), f \left(C _ {k}\right), s \left(C _ {k}\right), e \left(C _ {k}\right), i \left(C _ {k}\right), p \left(C _ {k}\right), d \left(C _ {k}\right), p \left(C _ {k} ^ {r} \mid C _ {k}\right), d \left(C _ {k} ^ {r}\right), q \left(C _ {k}\right) \rangle\tag{5}
$$

## 2.2. Discovering concept hierarchies

This discovery process is characterized by splitting recursively each existing concept into subconcepts at higher levels without knowing a priori the number of subconcepts. OSHAM tends to find a concept hierarchy with sufficiently general and discriminant concepts represented by Eq. (5). This tendency lies in the fact that the generality and discrimination of concepts are two dual characteristics, i.e., the more general the less discriminant the concepts. There is no way to estimate directly the discrimination of concepts from unsupervised data, however the discrimination ability concerns the partition quality and can be indirectly estimated, such as by the similarity between-class and within-class of a partition. This similarity is estimated based on different measures, as category utility in COBWEB [9], the intercorrelation among variables in WITT [12], or Eqs. (1)-(4) in OSHAM. For each concept $C_k$ , in general there are many possible tuples derived from $e(C_k)$ that can be used to form subconcepts $C_{k_i}$ , and the quality of the corresponding partition according to Eq. (4), differs greatly. OSHAM aims at extracting sequentially general subconcepts $C_{k_i}$ (with large extent), but among the hypothesized tuples which may generate hypothesized $C_{k_i}$ , it selects one that minimizes Eq. (4) in order to increase the discrimination.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 2
The OSHAM algorithm

Input: concept hierarchy H and an existing splittable concept  $C_{k}$ .

Result: H formed gradually.

Top-level: call OSHAM (root concept,  $\varnothing$ ).

Variables:  $\alpha$ ,  $\beta$ ,  $\eta$  are given thresholds.

Algorithm OSHAM ( $C_{k}$ , H)

1. Suppose that  $C_{k_{1}},\ldots,C_{k_{n}}$  are subconcepts of  $C_{k}$  found so far. While  $C_{k}$  is still splittable, find a new subconcept  $C_{k_{n+1}}$  of  $C_{k}$  that corresponds to the hypothesis with minimal  $q(C_{k})$  among  $\eta$  hypotheses  $C_{k_{n+1}^{1}},\ldots,C_{k_{n+1}^{n}}$ . Each hypothesis  $C_{k_{n+1}^{t}}$  is generated by doing the following steps (a)–(d)

(a) Find an attribute-value pair ( $a^{*},v^{*}$ ) so that  $\bigcup_{i=1}^{n}e(C_{k_{i}})\bigcup\rho(\{(a^{*},v^{*})\})$  is the largest cover of  $e(C_{k})$ .

(b) Find a maximal closed tuple S containing ( $a^{*},v^{*}$ ).

(c) Form subconcept  $C_{k_{n+1}^{t}}\setminus i(C_{k_{n+1}^{t}})=S$  and  $e(C_{k_{n+1}^{t}})=\rho(S)$ .

(d) Evaluate  $q(C_{k})$  with the new  $C_{k_{n+1}^{t}}$ .

Form intersecting subconcepts corresponding to intersections of extent of  $C_{k_{n+1}}$  with extent of existing concepts on H, excluding its superconcepts.

2. Update  $C_{k}^{r}=e(C_{k})\setminus\bigcup_{i=1}^{n+1}e(C_{k_{i}})$ . If one of the following conditions holds then  $C_{k}$  is considered unsplittable

(a) There exist not any closed tuple in  $C_{k}^{r}$ .

(b)  $|C_{k}^{\prime}|\leq\alpha$ .

(c)  $d(C_{k}^{\prime})\leq\beta$ .

3. Apply OSHAM ( $C_{k_{i}}$ , H) to each  $C_{k_{i}}$  formed in the step 1.
</div>

The algorithm OSHAM described in Table 2 forms gradually and recursively a concept hierarchy H, initially with the root concept whose extent is the set of all instances of O and its intent is $\lambda(\mathcal{O})$ which is often empty. In each recursive application to an existing splittable concept $C_{k}$ , OSHAM will split $C_{k}$ sequentially into

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 3
Auxiliary OSHAM procedures

MaxCoverage ( $a^{*}$ ,  $v^{*}$ ,  $C_{k}$ , H)
Find ( $a^{*}$ ,  $v^{*}$ ) ∈ T_{C_k} satisfying  $\left|\bigcup_{i=1}^{n}e\left(C_{k_i}\right)\cup\rho\left(\left\{(a^{*},v^{*})\right\}\right)\right|=\max_{(a,v)\in\mathcal{T}_{C_k}}\left|\bigcup_{i=1}^{n}e\left(C_{k_i}\right)\cup\rho\left(\left\{(a,v)\right\}\right)\right|$ 
If this maximum holds at several ( $a^{*}$ ,  $v^{*}$ ), then choose an arbitrary ( $a^{*}$ ,  $v^{*}$ ) that minimizes  $\left|\bigcup_{i=1}^{n}e\left(C_{k_i}\right)\cap\rho\left(\left\{(a^{*},v^{*})\right\}\right)\right|$ 
(referred to as the minimum intersection condition).

MaxClosedTuple ( $a^{*}$ ,  $v^{*}$ ,  $C_{k}$ , H)
(Find the closed tuple containing a given attribute–value pair ( $a^{*}$ ,  $v^{*}$ ); Let  $S=\{(a^{*},v^{*})\}$ . For every (a, v) ∈ T_{C_k}$(a^{*},v^{*})$  do if  $\rho(\{(a,v)\})=\rho(\{(a^{*},v^{*})\})$  then  $S=S\wedge(a,v)$ .

ClosedTuple ( $C_{k}$ , H)
(Verify whether there exists a closed tuple in  $C_{k}'$ )
1. Determine ( $a^{*}$ ,  $v^{*}$ ) that satisfies  $\varphi(\{(a^{*},v^{*})\})=\max_{(a,v)\in\mathcal{T}_{C_k}}\varphi(\{(a,v)\}).$ 
2. Determine the tuple  $S=\left\{\wedge(a,v)\in\mathcal{T}_{C_k}\mid\rho(\{(a,v)\})=\rho(\{(a^{*},v^{*})\})\right\}.$ 
3. If  $\varphi(S)&lt;1$  then return success with S else return failure.

IntersectionConcept (H, S)
(Form intersecting concepts from a given concept ( $\rho(S)$ , S))
1. For every existing concept ( $\rho(S')$ ,  $S'$ ) on H, excluding superconcepts of ( $\rho(S)$ , S), if  $\rho(S)\cap\rho(S')\neq\emptyset$ , then create the intersecting concept  $C_{h}=(\rho(S''),S'').$  The extent  $\rho(S'')$  is the intersection of the extent of two constituent concepts,  $\rho(S'')=\rho(S)\cap\rho(S')$ . The intent  $S''$  is the closed attribute set found by procedure MaxClosedTuple ( $a^{*}$ ,  $v^{*}$ ,  $C_{h}$ , H) where ( $a^{*}$ ,  $v^{*}$ ) is one attribute-value pair chosen arbitrarily from  $\lambda\rho(S'').$ 
2. Apply intersection concept (H,  $S''$ ) recursively.
</div>

![](/api/attachments/C3SFRDTY/fulltext/images/7fb32fcf7e3ddc081b90a0f7e05d359090c9a68d239b5b220069f4a21cf1c165.jpg)  
Fig. 1. Discovering overlapping concepts by the interactive OSHAM.

subconcepts $C_{k_{i}}$ , until an unsplittable condition holds. Conditions 2(a)–(c) determine whether the concept $C_{k}$ is possible or worthwhile to split further. In particular, 2(a) ensures that there exists at least one admissible subconcept of $C_{k}$ , 2(b) guarantees to consider only concepts that cover at least a minimum number $\alpha$ of instances, and 2(c) prevents splitting $C_{k}$ when its local instances are rather homogeneous.

OSHAM is refined by several auxiliary procedures described in Table 3: 1(a) by MaxCoverage $(a^{*}, v^{*}, C_{k}, \mathcal{H})$ , 1(b) by MaxClosedTuple $(a^{*}, v^{*}, C_{k}, \mathcal{H})$ , and 2(a) by ClosedTuple $(C_{k}, \mathcal{H})$ . In these procedures, $\mathcal{T}_{C_k}$ stands for the set of attribute-value pairs which are different from those used in the branch from the root concept to the concept $C_{k}$ being considered, and $\varphi(S) = |\rho(S)| / |\mathcal{O}|$ for $S \in \mathcal{T}$ . The intersection condition described in MaxCoverage and the procedure IntersectionConcept allow OSHAM to discover overlapping concepts (Fig. 1). By using the constraint $e(C_{k_i}) \cap \rho(\{(a^*, v^*)\}) = \emptyset$ in MaxCoverage, OSHAM is able as well to discover disjoint concepts. The difference and benefits of disjoint and overlapping concepts are addressed in more detail, e.g., in Refs. [9,25]. In fact, the interactive-graphic system OSHAM, described in Section 4, is capable of discovering both disjoint and overlapping concepts according to the user's interest and applications.

Algorithm OSHAM is originally described for discrete attributes with unordered nominal values. In the current version, continuous attributes are discretized before the learning process by k-means clustering [13]. In fact, for each continuous attribute the k-means algorithm is applied to cluster its values into k groups $(k=1,2,\ldots,K)$ . A criterion similar to Eq. (4) with the Euclidean distance is used to choose a value of k that corresponds to the best partition according to this criterion.

## 3. Using discovered knowledge

Decision-making is the process of choosing among alternative courses of actions for the purpose of attaining a goal or goals $[30]$ . In a decision tree obtained from supervised data, all training instances are covered by leaf concepts and only leaf concepts are considered as possible goals. In a concept hierarchy obtained from unsupervised data, training instances are covered by either non-leaf concepts or leaf concepts, and non-leaf concepts may also be considered as possible goals.

There are three broad classes of interpreters for discovered knowledge $[22]$ which can be applied to decision-making. The logical approach carries out an ‘all or none’ matching process depending on whether the unknown instance satisfies the concept intent. The threshold approach carries out a partial matching process and employs some threshold to determine an acceptable degree of match. The competitive approach also carries out a partial matching process and selects the best competitor based on estimated degrees of match. It is known that different interpreters can yield different meanings for the same representation of concepts.

As the generality is decreased along branches of $\mathcal{H}$ , we say that a concept $C_k$ matches an unknown instance $e$ if $C_k$ is the most specific concept in a branch that matches $e$ intensionally (though all superconcepts of $C_k$ match $e$ ). Naturally, there are three types of outcomes when matching logically $\mathcal{H}$ with $e$ : only one concept on $\mathcal{H}$ that matches $e$ (single-match), many concepts on $\mathcal{H}$ that match $e$ (multiple-match), and no concept on $\mathcal{H}$ that matches $e$ (no-match). Most KDD works dealing with the cases of no match and multiple-match employ a probabilistic estimation. In particular, the measure of fit for no match cases and estimate of probability for multiple-match cases in Ref. [27] have been widely adopted. Because of the nature of knowledge obtained from unsupervised data, the logical match of the concept intent does not always provide a decision with enough satisfaction. Based on different case studies, we develop a decision procedure that combines matching approaches in inductive learning with the minimum-distance classifier principle in case-based reasoning [21]. In fact, this procedure uses the logical interpretation associated with hierarchical structure information, the probabilistic estimation and the nearest neighbors of unknown instances. The nearest neighbor of $e$ in the object set $\mathcal{O}$ and the concept in $\mathcal{H}$ to which it belongs, denoted by $NN(e)$ and $c[NN(e)]$ , provide useful information to be used to reduce the risk of decision in all cases of single-match, multiple-match and no-match.

This decision procedure consists of two stages: (1) find all concepts on $\mathcal{H}$ that match $e$ logically (intensionally), and (2) decide among these concepts which one matches $e$ best. This procedure shares the same stages with the system POSEIDON [1,27] but functions differently.

In the second stage, we need to determine and compare the degree of the match of competitors, then choose the concept that matches e best. The satisfying degree of decision depends on how good the decision is obtained. From various case-studies, we found that a concept $C_{k}$ matches e well (with a low error rate) if it satisfies the majority of the following conditions: $l(C_{k})$ is high, $C_{k}$ is a leaf concept, $p(C_{k}) \times p(C_{k}^{r})$ is high, $d(C_{k})$ is low, $d(C_{k}^{r})$ is low, and generally none of these conditions has a clearly higher priority than the others. Formally, the functions $\tau_{N}, \tau_{L}, \tau_{P}, \tau_{D}$ and $\tau_{R}$ , according to the above conditions, can be used to compare two concepts, $C_{k}$ and $C_{h}$ , which match e intensionally:

$$
\tau_ {N} (C _ {k}, C _ {h}) = \left\{ \begin{array}{c c c} 1, & \text {if} & l (C _ {k}) > l (C _ {h}) \\ 0, & \text {if} & l (C _ {k}) = l (C _ {h}) \\ - 1, & \text {if} & l (C _ {k}) <   l (C _ {h}) \end{array} \right.\tag{6}
$$

$$
\tau_ {N} \left(C _ {k}, C _ {h}\right) = \left\{ \begin{array}{c c l} 1, & \text {if} & C _ {k} = \text {leaf} \wedge C _ {h} \neq \text {leaf} \\ 0, & \text {if} & C _ {k} = \text {leaf} \wedge C _ {h} = \text {leaf} \vee C _ {k} \neq \text {leaf} \wedge C _ {h} \neq \text {leaf} \\ - 1, & \text {if} & C _ {k} \neq \text {leaf} \wedge C _ {h} = \text {leaf} \end{array} \right.\tag{7}
$$

$$
\tau_ {P} \left(C _ {k}, C _ {h}\right) = \left\{ \begin{array}{c c l} 1, & \text {if} & p \left(C _ {k}\right) \times p \left(C _ {k} ^ {r} \mid C _ {k}\right) > p \left(C _ {h}\right) \times p \left(C _ {h} ^ {r} \mid C _ {h}\right) \\ 0, & \text {if} & p \left(C _ {k}\right) \times p \left(C _ {k} ^ {r} \mid C _ {k}\right) = p \left(C _ {h}\right) \times p \left(C _ {h} ^ {r} \mid C _ {h}\right) \\ - 1, & \text {if} & p \left(C _ {k}\right) \times p \left(C _ {k} ^ {r} \mid C _ {k}\right) <   p \left(C _ {h}\right) \times p \left(C _ {h} ^ {r} \mid C _ {h}\right) \end{array} \right.\tag{8}
$$

$$
\tau_ {D} \left(C _ {k}, C _ {h}\right) = \left\{ \begin{array}{c c c} 1, & \text {if} & d \left(C _ {k}\right) <   d \left(C _ {h}\right) \\ 0, & \text {if} & d \left(C _ {k}\right) = d \left(C _ {h}\right) \\ - 1, & \text {if} & d \left(C _ {k}\right) > d \left(C _ {h}\right) \end{array} \right.\tag{9}
$$

$$
\tau_ {R} \left(C _ {k}, C _ {h}\right) = \left\{ \begin{array}{c c c} 1, & \text {if} & d \left(C _ {k} ^ {r}\right) <   d \left(C _ {h} ^ {r}\right) \\ 0, & \text {if} & d \left(C _ {k} ^ {r}\right) = d \left(C _ {h} ^ {r}\right) \\ - 1, & \text {if} & d \left(C _ {k} ^ {r}\right) > d \left(C _ {h} ^ {r}\right) \end{array} \right.\tag{10}
$$

The following heuristic function $\tau$ compares the degree of match between $C_k$ and $C_h$ . We consider that $C_k$ matches $e$ better than $C_h$ if

$$
\tau \left(C _ {k}, C _ {h}\right) = \theta_ {N} \times \tau_ {N} \left(C _ {k}, C _ {h}\right) + \theta_ {L} \times \tau_ {L} \left(C _ {k}, C _ {h}\right) + \theta_ {P} \times \tau_ {P} \left(C _ {k}, C _ {h}\right) + \theta_ {D} \times \tau_ {D} \left(C _ {k}, C _ {h}\right) + \theta_ {R} \times \tau_ {R} \left(C _ {k}, C _ {h}\right) > 0\tag{11}
$$

where $\theta_N, \theta_L, \theta_P, \theta_D$ and $\theta_R$ are positive weights for the importance of the level, leaf concept, local instance conditional probability, concept dispersion, and local instance dispersion (they are all set to be 1 by default).

Denote by $\phi$ the satisficing degree of decision, and by $c[e]$ the concept that matches e best. The procedure described in Table 4 relies essentially on the comparison, using the function $\tau$ , between concepts that match e intensionally and the concept containing the nearest neighbor of e. In this decision procedure, different symbolic values are assigned to the satisfying degree $\phi$ of decision. They reflect the decreasing rank of decision satisfaction. For example, $S_{1}$ may be considered as ‘best decision’, $M_{1}$ as ‘strong decision’ while $N_{1}$ as ‘weakly accepted decision’ and $N_{2}$ as ‘no decision’. The interpretation for different values of $\phi$ depends on the judgment of the user or domain experts. In order to support the user to make the final decision, all concepts that match e intensionally with their associated information as well as the best matched concept estimated by OSHAM are displayed in both text and graphical forms as described in Section 4.1.

```txt
Table 4
Decision procedure for an unknown instance

Input: concept hierarchy H and unknown instance e.
Result: best matched concept c[e] and associated satisfying degree φ.
Variables: σ is a given threshold.
Procedure Matching (H, e, c[e], φ)
If there is only one concept C_k ∈ H that matches e intensionally then
if c[NN(e)] = C_k then c[e] ← C_k, φ ← S_1; else if τ(C_k, c[NN(e)])
≥ 0 then c[e] ← C_k, φ ← S_2; else c[e] ← c[NN(e)], φ ← S_3.
If there are m concepts C_{i_1}, ..., C_{i_m} ∈ H that match e intensionally then Choose among them C_{i_K} satisfying τ(C_{i_K}, C_{i_K}) ≥ 0,
∀ i_k ∈ {i_1, ..., i_m}, if C_{i_K} = c[NN(e)] ≥ 0 then c[e] ← C_{i_K}, φ ← M_1; else if τ(C_{i_K}, c[NN(e)]) ≥ 0 then c[e] ← C_{i_K}, φ ← M_2
else c[e] ← c[NN(e)], φ ← M_3.
If there is not any concept that matches e intensionally then, if δ(NN(e), e) ≤ σ then c[e] ← c[NN(e)], φ ← N_1; else c[e] = ∅, φ ← N_2.
```

## 4. Implementation and evaluation

In order to support the production of maximally useful results, OSHAM has been implemented as an interactive–graphic system that we first describe in this section. We then present a comparative evaluation of OSHAM with other methods in terms of description and prediction. Generally, it is difficult to evaluate unsupervised discovery systems since the class information is not available and so there is less agreement on the evaluation methodology. In Ref. [9], a task of flexible prediction, which requires the system to predict the values of one or more arbitrary attributes that have been excised from the test instances, was introduced. Another way is to employ supervised data but hide the class information in the whole discovering and matching phases and use the class information only to evaluate discovered knowledge [24]. We employ the latter to evaluate OSHAM with the predicted name of each discovered concept $C_{k}$ as the most frequently occurring name of instances in $e(C_{k})$ . In this way, it is possible to compare the prediction of supervised and unsupervised discovery systems.

## 4.1. An interactive knowledge discovery system

Recently, several interactive–graphic supervised discovery systems have been developed, e.g., in Refs. [20,23,35]. We have implemented OSHAM in the X Window on a Sparcstation with the direct manipulation style of interaction [14], that allows the user to interact with OSHAM during the discovery process. As mentioned above, OSHAM gradually forms concepts at different levels of generality in the top–down direction, and the size and form of concept hierarchies depend on the parameters $\alpha$ , $\beta$ and $\eta$ . In contrast to discovery systems with implicit parameters such as the fixed pruning threshold in C4.5 [29], we share the view in Ref. [1] about the role of parameters in a discovery system that allows the user to explicitly modify them in the discovery process.

With a non-interactive unsupervised discovery system, the user has to run it independently at different times with various parameters, store all generated results, then compare them and choose the most suitable one. Interactive OSHAM allows the user to participate actively in the discovery process. The user can initialize parameters to cluster data, visualize the concept hierarchy gradually, observe the results and the quality evaluation, manually modify the parameters when necessary before the system continues to go further to cluster subsequent data or backtrack to regrow the concept hierarchy with respect to the categorization scheme $[18]$ .

Though a full comprehensive investigation on the sensitivity of the trade-off between prediction quality and simplicity of the concept hierarchies regarding the various parameters goes beyond the scope of this paper, the main effects of parameters can be viewed. In principle, the smaller $\alpha$ and/or $\beta$ , the larger size of H, and the larger $\eta$ the higher quality of generated concepts on H.

Fig. 1 shows a main screen of the interactive OSHAM in discovering overlapping concepts from the Wisconsin breast cancer data. The database, obtained from the University of Wisconsin Hospitals, consists of observations of benign and malignant cases (shown in the window 'Wisconsin Breast Cancer Data') on nine symbolic symptoms: clump thickness, uniformity of cell size, ..., mitoses, and each has 10 possible values (shown in the window 'Wisconsin Breast Cancer Attributes'). The window 'parameters' shows the initialized parameters in this run. The main browser window shows a part of the generated concept hierarchy. Each discovered concept corresponds to a small rectangle with some information and links to its superconcepts and subconcepts. For example, the information '108 13, 2 (Cell Size,1)' found within one small rectangle indicates that its concept identifier in the generated order is 108, the number of instances it covers is 13, the number of local instances is 2 (omitted for leaf concepts), and the local tuple is (Cell Size,1). All tuples in the concept intent can be obtained by aggregating local tuples along the branch from the considered concept to the root, for example $i(C_{108}) = (\text{Cell Size},1) \wedge (\text{Epithelial},3) \wedge (\text{Nucleoli},1) \wedge (\text{Mitoses},1)$ . The description of each concept can be seen in the window 'Class Description' by clicking on its sensitive rectangle, e.g., the description of the concept number 108. OSHAM yields discovered knowledge in a concept hierarchy or transform them into a rule base. Below is an example of a concept in the output file

```txt
CONCEPT 22
Level = 3
Super_Concepts = {7 20} Subconcepts = {78 97}
Concept_dispersion = 0.414614
Local_instance_dispersion = 0.582011
Subconcept_partition_quality = 4.063252
Concept probability = 0.092210
Features = {(Thickness,5) (Adhesion,1) (Mitoses,1)}
Local_instances(7) = {63 163 234 269 477 480 612}
Local_instance_conditional_probability = 0.120690
```

There is a considerable distinction between concepts found by OSHAM in contrast to those from others, such as supervised system C4.5 [29], unsupervised systems COBWEB [9] and AUTOCLASS [5]. C4.5 induces decision trees in which concepts are represented only by their intent associated with a predicted error rate, and it also does not need to maintain intermediate concepts. Without the class information, OSHAM needs to induce concepts with additional information as described in Section 2.1. Concepts obtained by OSHAM also differ from those of COBWEB and AUTOCLASS. COBWEB represents each concept $C_k$ as a set of attributes $a_i$ , associated with a set of their possible values $v_{ij}$ , the occurrence probability of concept $P(C_k)$ , and the conditional probability $P(a_i = v_{ij}|C_k)$ associated with each value $v_{ij}$ . In AUTOCLASS, a concept (referred to as a class) is defined as a particular set of parameter values and their associated model. A classification is defined as a set of classes, the probability of each class, and two additional probabilities for each hypothesized model: the model probability $P(H)$ and the conditional parameter probability distribution $P(p|H)$ .

## 4.2. Evaluation of the predictive accuracy

As mentioned above, we use the benchmark introduced in Ref. [24] for evaluating the predictive accuracy of unsupervised discovery systems. It is worth mentioning that multiple train-and-test experiments are much computationally expensive but give more reliable evaluation than single train-and-test experiments. A k-fold cross-validation is the process of doing k times a single train-and-test experiment then average the results as the final evaluation. The data is divided into mutually exclusive subsets of approximately equal size. In each experiment, one subset is taken as testing data and the others as training data.

We carried out experiments on several databases from the UCI repository of machine learning databases, including the Wisconsin breast cancer, Congressional voting, mushroom, tic-tac-toe with 10-fold cross validation and monks with single train-and-test experiments. Table 5 gives information about the size of these databases in terms of the number of discrete and continuous attributes, number of instances, and number of natural classes in the original data.

All experiments are carried out for four systems C4.5, CART, AUTOCLASS and OSHAM in the same conditions, i.e., the same randomly divided data sets. The predictive accuracies of C4.5 and CART are estimated directly by these programs with fixed thresholds for the post-pruning. For AUTOCLASS, we use the public version AUTOCLASS-C implemented recently in C language and run three steps of search, report and predict with the default parameters. The predicted name and predictive accuracy of AUTOCLASS are obtained in the same way as those in OSHAM, i.e., the predictive accuracy is the ratio of the number of testing instances correctly predicted regarding the predicted name of concepts over the total number of testing instances. In order to have an unbiased evaluation of OSHAM, although in each concrete database the user can adjust OSHAM's parameters to obtain the most suitable concept hierarchy, we fixed values $\alpha = 1\%$ of the size of the training set, $\beta = 15\%$ , and $\sigma = 10\%$ of the number of attributes, and $\eta = 3$ in all experiments of OSHAM. Table 6 reports the results of predictive accuracy (%) of C4.5, CART, OSHAM and AUTOCLASS (AUTOC), the average number of concepts in hierarchies and CPU time of OSHAM. Some remarks can be drawn from the experimental results.

Table 5  
Description of databases

<table><tr><td>Data sets</td><td>Discrete</td><td>Continuous</td><td>Instances</td><td>Classes</td></tr><tr><td>Breast cancer</td><td>9</td><td>-</td><td>699</td><td>2</td></tr><tr><td>Vote</td><td>16</td><td>-</td><td>435</td><td>2</td></tr><tr><td>Mushroom</td><td>23</td><td>-</td><td>8125</td><td>2</td></tr><tr><td>Tic-tac-toe</td><td>9</td><td>-</td><td>862</td><td>9</td></tr><tr><td>Glass</td><td>-</td><td>9</td><td>214</td><td>6</td></tr><tr><td>Ionosphere</td><td>-</td><td>35</td><td>351</td><td>2</td></tr><tr><td>Waveform</td><td>-</td><td>21</td><td>300</td><td>3</td></tr><tr><td>Pima diabetes</td><td>-</td><td>8</td><td>768</td><td>2</td></tr><tr><td>Thyroid (new)</td><td>-</td><td>6</td><td>215</td><td>3</td></tr><tr><td>Heart disease</td><td>8</td><td>5</td><td>303</td><td>2</td></tr></table>

The predicted name obtained by the majority of occurring name of instances in the concepts of OSHAM and AUTOCLASS is different from the concept name obtained in supervised discovery (e.g., C4.5) using the pruning threshold based on the class information. An unsupervised concept in the worse case may contain nearly equal positive and negative instances, and an unsupervised classification may fail in distinguishing very similar instances. It explains that, while the predictive accuracies between supervised and unsupervised methods do not look so different, they are slightly different in essence.

The complexity of OSHAM is $\mathcal{O}(|\mathcal{O}||\mathcal{A}|)$ , and the concept hierarchy is constructed by OSHAM in linear time in the number of instances and the total number of attribute-value pairs. The average number of concepts in concept hierarchies and CPU times (in second) of induction obtained by 10-fold cross validation on the Sparcstation are also reported in two last columns of Table 6. In comparison with the huge number of nodes and execution time of the Galois lattice (e.g., Congressional voting), OSHAM provides a much simpler solution with the reasonable prediction accuracy.

Using two different representations of concepts, the predictive accuracy of OSHAM and AUTOCLASS in these experiments are only slightly different. AUTOCLASS is better than OSHAM in the Breast cancer data, but vice-versa in Tic-tac-toe data, etc. The main advantage of OSHAM in representing concepts over the probabilistic representation is that it maintains the concept coherence and so its concept hierarchies can be easily understood.

Table 6  
Predictive accuracies, number of concepts and CPU time of OSHAM

<table><tr><td></td><td>C4.5</td><td>CART</td><td>OSHAM</td><td>AUTOC</td><td>Concepts</td><td>CPU times</td></tr><tr><td>Breast cancer</td><td>93.3</td><td>94.1</td><td>92.6</td><td>96.6</td><td>98</td><td>484</td></tr><tr><td>US voting</td><td>94.5</td><td>93.8</td><td>93.7</td><td>91.2</td><td>69</td><td>151</td></tr><tr><td>Mushroom</td><td>100.0</td><td>100.0</td><td>88.2</td><td>86.5</td><td>63</td><td>1288</td></tr><tr><td>Tic-tac-toe</td><td>88.0</td><td>86.2</td><td>92.6</td><td>82.3</td><td>204</td><td>475</td></tr><tr><td>Glass</td><td>66.6</td><td>66.0</td><td>65.3</td><td>55.7</td><td>37</td><td>6.5</td></tr><tr><td>Ionosphere</td><td>91.5</td><td>88.3</td><td>81.2</td><td>91.5</td><td>110</td><td>64</td></tr><tr><td>Waveform</td><td>72.4</td><td>72.5</td><td>73.0</td><td>59.2</td><td>215</td><td>278</td></tr><tr><td>Pima diabetes</td><td>71.2</td><td>72.2</td><td>72.7</td><td>68.2</td><td>39</td><td>72</td></tr><tr><td>Thyroid (new)</td><td>91.1</td><td>90.3</td><td>84.6</td><td>89.3</td><td>19</td><td>5</td></tr><tr><td>Heart disease</td><td>59.5</td><td>52.4</td><td>58.4</td><td>49.2</td><td>65</td><td>13</td></tr></table>

## 5. Conclusion

We have described the unsupervised discovery system OSHAM that combines different views on concepts and categorization constraints in discovering knowledge. We have also developed a decision procedure by integrating interpreters in inductive learning with case-based reasoning that allows the use of discovered knowledge to decide the class of unknown instances with the satisfying degree. The main contribution of this work lies in the enrichment of the classical views on concepts, its way of finding and using knowledge which is different from other approaches in the KDD literature. Moreover, it has been implemented as an interactive and highly graphic system that permits the interaction of the user with the system during the discovery process and the interpretation of unknown cases. Careful experiments on different databases show that OSHAM can find classificatory knowledge from data with high predictive accuracy and understandability.

OSHAM has an application potential in business decision-making, particularly in the construction of knowledge-based decision support systems. Generated in the hierarchical form and supported by the graphical browser, concepts discovered by OSHAM can be easily understood and used in making decision for unknown cases. They can be rewritten in hierarchical object knowledge bases by tools for knowledge-based systems such as KEE, KAPPA, NEXPERT OBJECT, or used directly by the generator TESOR $[15]$ . Concepts discovered in the hierarchical structure by OSHAM can also be transformed into the usual form of decision rules with some modification. Summarily, OSHAM is amenable to business applications in which the user need to construct knowledge bases from low-cost and high-quality databases.

## References

[1] F. Bergadano, S. Matwin, R.S. Michalski, J. Zhang, Learning two-tiered descriptions of flexible concepts: the POSEIDON system, Machine Learning 8 (1992) 5–43.

[2] B.R. Boyce, C.T. Meadow, D.H. Kraft, Measurement in Information Science, Academic Press, 1994.

[3] L. Breiman, J. Friedman, R. Olshen, C. Stone, Classification and Regression Trees, Wadsworth, Belmont, CA, 1984.

[4] C. Carpenito, G. Romano, A lattice conceptual clustering system and its application to browsing retrieval, Machine Learning 10 (1996) 95–122.

[5] P. Cheeseman, J. Stutz, Bayesian classification (AutoClass): Theory and results, in: U.M. Fayyad, et al. (Eds.), Advances in Knowledge Discovery and Data Mining, AAAI Press/MIT Press, 1996, pp. 153–180.

[6] P. Clark, T. Niblett, The CN2 induction algorithm, Machine Learning 3 (1989) 261–284.

[7] M.K. El-Najdawi, A.C. Stylianou, Expert support systems: integrating AI technology, communications of the ACM, 36 12 (1993) 55–65.

[8] U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy, From data mining to knowledge discovery: an overview, in: U.M. Fayyad, et al. (Eds.), Advances in Knowledge Discovery and Data Mining, AAAI Press/MIT Press, 1996, pp. 1–36.

[9] D. Fisher, Knowledge acquisition via incremental conceptual clustering, Machine Learning 2 (1987) 139–172.

[10] W.J. Frawley, G. Piatetsky-Shapiro, C.J. Matheus, Knowledge discovery in databases: an overview, in: G. Piatetsky-Shapiro, W.J. Frawley (Eds.), Knowledge Discovery in Databases, AAAI Press, 1993, pp. 1–27.

[11] R. Godin, R. Missaoui, An incremental concept formation approach for learning from databases, Theor. Comput. Sci. 133 (1994) 387–419.

[12] S.J. Hanson, M. Bauer, Conceptual clustering, categorization and polymorphy, Machine Learning 3 (1989) 343–372.

[13] J.A. Hartigan, Clustering Algorithms, Wiley, New York, 1975.

[14] M. Helander (Ed.), Handbook of Human-Computer Interaction, Elsevier, 1991.

[15] T.B. Ho, N.K. Pham, H.K. Bach, T.M. Hoang, C.S. Ngo, T.D. Nguyen, T.H. Tong, Q.T. Hoang, Development and applications of the expert system generator TESOR, Proceedings of NCSR of Vietnam, Vol. 2 (1992), No. 2, pp. 3–14.

[16] T.B. Ho, An approach to concept formation based on formal concept analysis, IEICE Trans. Inf. Systems E78-D (5) (1995) 553–559.

[17] T.B. Ho, A hybrid model for concept formation, in: Y. Tanaka, et al. (Eds.), Information Modelling and Knowledge Bases VII, IOS Publisher, 1996, pp. 22–35.

[18] T.B. Ho, T.D. Nguyen, Integrating human factors with a concept formation process, Proceedings 6th International Conference on Human-Computer Interaction, 1995, 74.

[19] H. Kangassalo, On the concept of concept for conceptual modelling and concept detection, in: S. Ohsuga, et al. (Eds.), Information Modelling and Knowledge Bases III, IOS Press, 1992, pp. 17–58.

[20] T. Kervahut, J.Y. Potvin, An interactive–graphic environment for automatic generation of decision trees, Decision Support Systems 18 (1996) 117–1343.

[21] J. Kolodner, Case-Based Reasoning, Morgan Kaufmann, 1993.

[22] P. Langley, Elements of Machine Learning, Morgan Kaufmann, 1996.

[23] H.Y. Lee, H.L. Ong, L.H. Quek, Exploiting visualization in knowledge discovery, Proceedings of First International Conference on Knowledge Discovery and Data Mining, 1995, pp. 198–203.

[24] K.B. McKusick, P. Langley, Constraint on tree structure in concept formation, Proceedings of International Joint Conference on Artificial Intelligence, 1991, pp. 810–816.

[25] J.D. Martin, D.O. Billman, Acquiring and combining overlapping concepts, Machine Learning 10 (1994) 121–155.

[26] R.S. Michalski, R.E. Stepp, Learning from observation: conceptual learning, in: R.S. Michalski, J.G. Carbonelle, T.M. Michell (Eds.), Machine Learning: An Artificial Intelligence Approach, Vol. 1, Morgan Kaufmann, 1983, pp. 331–363.

[27] R.S. Michalski, Learning flexible concepts: Fundamental ideas and a method based on two-tiered representation, in: R.S. Michalski, Y. Kodratoff (Eds.), Machine Learning: An Artificial Intelligence Approach, Vol. III, Morgan Kaufmann, 1990.

[28] J.R. Quinlan, Decision trees and decisionmaking, IEEE Trans. Systems, Man, Cybernetics 20 (2) (1990) 339–346.

[29] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, 1993.

[30] E. Turban, Decision Support and Expert Systems: Management Support Systems, Prentice-Hall, 1995.

[31] I. Van Mechelen, J. Hampton, R.S. Michalski, P. Theuns (Eds.), Categories and Concepts. Theoretical Views and Inductive Data Analysis, Academic Press, 1993.

[32] R. Wille, Restructuring lattice theory: an approach based on hierarchies of concepts, in: I. Rival (Ed.), Ordered Sets, Reidel, 1982, pp. 445–470.

[33] S. Wrobel, Concept Formation and Knowledge Revision, Kluwer Academic Publishers, 1994.

[34] X. Wu, Hybrid interpretation of induction results, in: N. Terashima, E. Altman (Eds.), Advanced IT Tools, Chapman & Hall, 1996, pp. 497–506.

[35] J. Zytkow, J. Baker, Interactive mining of regularities in databases, in: G. Piatetsky-Shapiro, W.J. Frawley (Eds.), Knowledge Discovery in Databases, AAAI Press, 1993, pp. 31–53.

![](/api/attachments/C3SFRDTY/fulltext/images/dbf25a98494bcb3eec1e4b2dbed5f38e3ee2ff0d659de914fb9b62b6bd1ecc7d.jpg)  
Tu Bao Ho is currently a visiting associate professor at the Graduate School of Information Science, Japan Advanced Institute of Science and Technology (JAIST). He received a B.Tech degree in Applied Mathematics from the Hanoi University of Technology, in 1978, and M.S. and Ph.D. degrees in Computer Science from Pierre and Marie Curie University, Paris, in 1984 and 1987. In 1979, he joined the Institute of Information Technology, National Centre for Natural Science and Technology of Vietnam where he is an associate professor. His research interests include knowledge-based systems, machine learning, decision support systems, knowledge discovery and data mining.
