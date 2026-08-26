---
otero_id: 5866
otero_key: "2RQGTK8C"
title: "The BIG CHASE: A decision support system for client acquisition applied to financial networks"
authors: "Lara Quijano-Sanchez; Federico Liberatore"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.04.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The BIG CHASE: A decision support system for client acquisition applied to financial networks

Lara Quijano-Sanchez\*, Federico Liberatore\*

UC3M-BS Institute of Financial Big Data Universidad Carlos III de Madrid, Getafe, Madrid, Spain

A R T I C L E I N F O

Article history: Received 26 October 2016 Received in revised form 18 April 2017 Accepted 20 April 2017 Available online xxxx

Keywords: Client acquisition Financial networks Social modelling Projected gradient descent Maximum reliability path

## A B S T R A C T

Bank agencies daily store a huge volume of data regarding clients and their operations. This information, in turn, can be used for marketing purposes to acquire new clients or sell products to existing clients. A Decision Support System (DSS) can help a manager to decide the sequence of clients to contact to reach a designed target. In this paper we present the BIG CHASE, a DSS that translates bank data into a reliability graph. This graph models relationships based on a probability of traversal function that includes social measures. The proposed DSS, developed in close collaboration with Banco Santander, S.A., fits the parameters of the probability function to explicit solution evaluations given by experts by means of a specifically designed Projected Gradient Descent algorithm. The fitted probability function determines the reliabilities associated to the edges of the graph. An optimization procedure tailored to be eficient on very large sparse graphs with millions of nodes and edges identifies the most reliable sequence of clients that a manager should contact to reach a specific target. The BIG CHASE has been tested with a case study on real data that includes Banco Santander, S.A. 2015 Spain bank records. Experimental results show that the proposed DSS is capable of modeling the experts’ evaluations into probability function with a small error.

© 2017 Elsevier B.V. All rights reserved

## 1. Introduction

In this paper, we present a case study of a DSS created in collaboration with the bank Banco Santander, S.A.<sup>1</sup> (BS) to address a specific necessity. In fact, BS is interested in developing a system that uses the information stored in their client and operations databases for marketing purposes. In particular, the DSS should provide the best sequence of clients that a manager should contact to reach a target, starting from any client in the manager’s portfolio, with the aim of acquiring new clients or selling additional products to existing ones. The banks’ goal is to identify all the different existing sequences of clients to reach a target and to rank them according to their reliability. With this information, bank managers will be able to either ask the intermediates to introduced them to the target or to refer to their relationships with intermediates when dealing with the target. An additional challenge is given by the size of the bank databases, that are comprised of millions of entries. We will refer to this decision-making problem as the BIG CHASE, as we are “chasing” a target through a “big” database of bank operations. A tool capable of solving this problem finds immediate application in marketing for the sale of products and services to clients, in the expansion of managers’ portfolios and in the acquisition of new clients. Also, the tool can be easily extended to other banks or application contexts such as the identification of influencers for products and offers placement, as well as the clustering of the network into trust-based communities.

Our proposal relies on the translation of the data provided by the bank into a large reliability graph, comprised of millions of nodes and edges. Fig. 1 provides a simplified representation of the methodology proposed. In the graph, nodes represent actors (i.e., clients, non-clients, and managers) while edges are weighted by a traversal probability, that is, the probability of the edge’s origin node positively influencing the opinion of the edge’s destination node about a specific bank product. Given the lack of historical data on client acquisitions, these probabilities are approximated by a probability function, that makes use of information drawn from the bank databases and from the graph itself. The probability function is adjusted to fit explicit evaluations given by experts of sample solutions through a Projected Gradient Descent procedure. Then, the probabilities associated to the edges (weights) are computed. Finally, the path on the graph (i.e., a sequence of actors) that maximizes the reliability between the manager and the target is obtained by a Maximum Reliability Path algorithm. Given the size of the network, a

L. Quijano-Sanchez, F. Liberatore / Decision Support Systems xxx (2017) xxx–xxx

![](/api/attachments/2RQGTK8C/fulltext/images/5ef59530218c2c584629d956e71b8b084b2ccd4660c8a52410fd076e3ffd4cc6.jpg)  
Fig. 1. The BIG CHASE’s graphical representation. The financial databases are translated into a graph where nodes represent actors (i.e., clients, non-clients, and managers) and edges are weighted by a probability of traversal. The best sequence of clients that the manager should contact to reach the target is represented by thick arrows.

number of optimizations are implemented to increase the eficiency of the DSS.

The proposed system, developed in strict collaboration with BS, is capable of modeling the evaluations provided by experts and identifying the most reliable path as illustrated in a real case study on BS’s financial data. Thus, the contribution of this research consists of a method, the BIG CHASE, to model BS’s specific problem through the following steps:

C1. A novel methodology for building a reliability graph using monetary relationships among customers obtained from financial databases.

C2. A function for weighting the graph with the probability of positively influencing one’s opinion.

C3. A procedure for adjusting the weight function based on experts’ evaluations by means of a Projected Gradient Descent approach.

C4. An algorithm for the identification of the maximum reliability path between nodes in a large graph.

C5. A case study where the BIG CHASE is tested with input data from BS’s 2015 records.

The reminder of the paper is organized as follows. In the next section we present the state of the art on client acquisition support systems and provide the necessary background and justification for the probability function. In Section 3, the BIG CHASE is formally discussed along with the structure of the reliability graph. Next, in Section 4, the probability function and its components are introduced in detail. A Projected Gradient Descent algorithm for adjusting the probability function to evaluations given by experts is the topic of Section 5. The algorithm for the identification of the most reliable manager-target paths on the weighted graph is given in Section 6. In Section 7, the BIG CHASE is applied to BS’s 2015 Spanish client data. The article concludes with a summary of the main findings and some possible future lines of research.

## 2. Literature review

In this section, the relevant literature on client acquisition is presented along with a more in-depth analysis of the state of the art in social factors and tie strength modeling that provides a background to the components of the probability function presented in Section 4.

Client acquisition is one of the dimensions that comprise Customer Relationship Management (CRM) [4]. CRM has attracted the interest of researchers from a wide range of fields, including quantitative methods. A comprehensive literature review on data mining techniques applied to CRM is the subject of Ngai et al. [21]. However, the number of optimization models that address the problem of client acquisition is quite limited. Recently, King et al. [16] propose a model that balances customer acquisition and retention under resource constraints. Their approach could be used as a preliminary step to select the targets for the BIG CHASE.

DSSs for client acquisition are a relative recent field that is still at its early stages. Thus, the number of contributions in the literature is still very limited: Calvão et al. [3] use client–lawyer networks to simulate client acquisition behavior. A different approach is proposed by Du et al. [9] that introduce OpinionRings, a visualization tool in the form of concentric circles that reflect the inclination of an actor to adopt a positive or negative opinion about a product. Despite the lack of contributions, Fang and Zhang [10] recognize that the importance of client acquisition, retention problems and risk evaluations will grow in financial big data in the next years.

To the best of the authors’ knowledge, no model similar to the BIG CHASE in rationale or methodology has been presented in the literature. In detail, the BIG CHASE is the first proposed DSS to support decisions on bank client acquisition and development by using the social structure deriving from clients operations and relations.

## 2.1. Social factors modeling

The use of social factors to model clients’ relationships and decisions has been recently endorsed by some authors: Chen and Shen [6] point out that consumers’ decisions are strongly correlated with users’ trust towards a community and its members. Along this line, Dai et al. [7] afirm that a positive emotion towards a product is positively related to consumers’ satisfaction. Social network data offers significant opportunities for research in marketing [15,31]. In this line, researchers have studied the role of social interactions and contagion and have concluded that humans are social individuals and, therefore, social behavior has a great impact on their decisionmaking processes [29]. Also, it has become clear that users’ social environment and their networks have a great influence on individuals when coming to a decision. This is commonly referred to as “emotional contagion,” i.e., the effect of individuals’ affective state on others in an environment [1,19]. This contagion is usually proportional to the tie strength (or trust) between individuals as closer friends have a higher influence [12,28]. Besides, the principle of homophily states that people tend to trust and be friends with people who they share interests with [2,20]. However, the influence that affects an individual inside a network also depends on the individual’s degree of conformity [19], that can be modeled as the personality [24]. Besides, it has been proven that individuals’ decisions change upon receiving more sophisticated arguments and remain the same otherwise. This individual reaction upon persuasion is an essential part of understanding social interactions and contagion and can explain the advantage of studying users’ behavior as a whole entity inside a social network over users’ individual behavior in decision-making processes [22]. In this line, influencers are defined as leaders or connectors, or as just plain interesting personalities who have the ability to influence potential users. This term has been extensively researched in the social sciences over the past few decades [2,20] and is related to persuasiveness. Finally, when exploring the impact of word of mouth and contagion on the behavior of others, a measure of how the product on which to decide meets or surpasses the customer’s expectations is needed. This measure is commonly estimated with the customer’s satisfaction [14,32] and studies like Storbacka et al. [27] afirm that satisfaction is a requirement to retain existing customers.

## 2.2. Tie strength modeling

In mathematical sociology, interpersonal ties are defined as information-carrying connections between people. Granovetter [13] defines the tie strength between two individuals as a (probably linear) combination of four components: (1) the time they have know each other; (2) the intimacy of the relationship, that measures how close or intimate a relationship is; (3) the intensity of the relationship that measures the frequency of contact; (4) the existence of reciprocal services, that measures the reciprocity of the relationship. Later research has elaborated this list: Lin et al. [17] suggest that the social distance is key in measuring tie strength; Shi et al. [26] believe that it can be estimated through having at least one mutual friend. While Gilbert and Karahalios [11] conclude that, in theory, tie strength has more than seven dimensions and many manifestations but that, in practice, relatively simple proxies can approximate it. However, the literature has not resolved the issue of how to actually measure tie strength, let alone defined a specific model.

## 2.3. Trust propagation

A subject that is related to the BIG CHASE is that of Trust Propagation. In fact, tie strength (a measure of trust) is one of the factors of the probability function used to weight the edges in the reliability graph (see Section 4). Trust Propagation algorithms estimate the trust of two users that are not directly connected by making use of their trust with friends in common [33]. Wierzbicki [34] compares some of the most well known Trust Propagation algorithms such as Advogato, Applesed, GKRT, TidalTrust and Closelook. Differently from them, the goal of the BIG CHASE is the identification of sequences of clients that have a high probability of being successful at connecting a client-manager with a potential target. In this regard, it could be seen as a specialized trust propagation algorithm. The comparison of the BIG CHASE against other trust propagation procedures is left as future work.

## 3. The BIG CHASE

In this section, a formal description of sets, data and attributes required by the BIG CHASE is given. Also, a definition of the reliability graph and of a solution to the problem are presented, along with a summary of the methodology proposed.

## 3.1. Formulation of the problem

The goal of the BIG CHASE is identifying the most reliable sequence of clients that a manager should contact to reach a defined target (a client or a non-client). The first client in the sequence must necessarily belong to the portfolio of the manager. More formally, the BIG CHASE is formulated as follows.

## 3.1.1. Sets, data and parameters

The BIG CHASE requires the definition of the main entities in the problems: actors and operations.

1. N, set of actors involved in the problem. This set is partitioned into $\{ N ^ { c l i } , N ^ { n o n } , N ^ { m a n } \} ,$ , where $N ^ { c l i }$ is the set of clients, $N ^ { n o n }$ is the set of non-clients and $N ^ { m a n }$ is the set of managers.

2. $M _ { m } \subseteq N ^ { c l i } , \forall m \in N ^ { m a n }$ , set of manager’s m portfolio.

3. R, set of the different types of existing relationships between actors.

Also, actors and their relationships are characterized by the following data.

• lin $\in \ [ 0 , 1 ] ,$ strength of the relationship (or link) of actor $i \in N ^ { c l i } \cup N ^ { n o n }$ with the bank. This is intended as the degree of involvement of each actor with the bank. All the nonclients have this parameter equal to zero, and viceversa. More formally: $l i n _ { i } = 0 \Longleftrightarrow i \in N ^ { n o n }$

$p _ { m , j } \in [ 0 , 1 ] .$ , the strength of the relationship between manager $m \in N ^ { m a n }$ and client $j \in M _ { m } .$ . This is intended as the strength of the tie between a manager m and each client j in her portfolio.

$n _ { i , j , r } \in [ 0 , 1 ]$ , the intensity of each relationship type r ∈ R originated from actor i and directed to j, with $i , j \in \hat { N ^ { c l i } } \cup N ^ { n o n }$ . This is intended as a measure of the frequency and volume of a relationship between actors. An intensity of zero indicates that the actors have never shared a relationship of type r. Note that, for a given $r \in R , n _ { i , j , r }$ is not necessarily symmetrical, e.g., i makes monthly transfers to j to pay the rent but the opposite is not true.

Finally, for each instance of the problem, the manager and the target must be provided:

1. $s ,$ the source (initial) actor. It must be necessarily a manager, $\mathrm { i } . \mathrm { e } . , s \in N ^ { m a n }$

2. t, the target actor. It must be necessarily a client or a non-client, $\mathrm { i . e . , } t \in \hat { N } ^ { c l i } \cup N ^ { n o n }$

## 3.1.2. Reliability graph generation

Bank agencies daily store a huge volume of data regarding clients and their operations. In the following, a methodology to translate bank data containing millions of entries into a reliability graph that models relationships among various actors based on social measures is shown. The novelty of the approach consists of using among other values the monetary relationships between customers as a basis for estimating a reliability graph (which could also be seen as a trust network). This design could be useful in other applications, e.g., a bank could establish a matchmaking service for prospective customers based on trust propagation in the graph.

The reliability graph is represented as an undirected graph $G =$ (N, E), where N (the set of actors presented in Section 3.1.1) is the set of nodes and E the set of edges. An edge is included in the graph if and only if the actors share at least one type of relationship. More formally:

$$
(i, j) \in E \longleftrightarrow \exists \quad r \in R: (n _ {i, j, r} > 0) \vee (n _ {j, i, r} > 0).\tag{1}
$$

Each edge $( i , j )$ is characterized by a weight $p _ { i , j }$ representing the reliability of the arc. In case one of the nodes corresponds to a manager, this is given as data (see the explanation of $p _ { m , j }$ in Section 3.1.1). For all the other cases, the weight is approximated by a traversal probability, as explained in Section 4.

## 3.1.3. Solution representation

A solution to an instance of the BIG CHASE is an $s - t$ path P represented as a sequence of ordered edges $\{ P _ { 1 } , P _ { 2 } , \ldots , P _ { | P | } \}$ , where |P| is the length of the path. Note that $P _ { 1 }$ must comply $P _ { 1 } \stackrel { \cdot } { = } \stackrel { \cdot } { ( } s , j ) , j \in M _ { s } ,$ and that $P _ { \left| P \right| }$ must end in t. Also, $P _ { 2 } , \ldots , P _ { | P | - 1 } \in N ^ { c l i }$ , that is, all the intermediate nodes must be clients. Each path is characterized by a reliability, $\hat { y } _ { P } ~ \in ~ [ 0 , 1 ]$ . Given that each edge $( i , j )$ is weighted by a traversal probability, $p _ { i , j } ,$ the reliability of a path is given by the product of its edges’ weights. More formally:

$$
\hat {y} _ {P} = \prod_ {(i, j) \in P} p _ {i, j}.\tag{2}
$$

## 3.2. The BIG CHASE methodology

The methodology proposed for the solution of the BIG CHASE is detailed in the following. It is a process comprised of four steps:

1. Construction of a graph of reliability between actors, as described in Section 3.1.3.

2. Computation of the components (based on the social data and the graph structure) used as input in the edge weight function representing the reliability between two nodes, Section 4.

3. Adjusting the coeficients in the probability function based on explicit evaluations of paths given by experts. To this end, a Projected Gradient Descent algorithm has been specifically designed to solve this problem. The procedure is illustrated in Section 5.

4. Finally, once the weights of the graph are determined, the most reliable s−t path is identified by the Maximum Reliability Path algorithm described in Section 6.

In the next section, the function used to assign traversal probabil ities to the edges is presented.

## 4. Probability function

The weight of an edge between two nodes (i, j) estimates the probability that node j accepts a bank offer after interacting with client i. More in general, we could speak of the probability $p _ { i , j }$ of success of node i positively influencing the opinion of node j about a specific bank product. Considering the information and the data given by the bank, which does not include historical data on client acquisitions by managers, we have based our methodology on recent advances in relationship modeling in Social Networks [15,31]. As explained in the literature review (Section 2) people are social individuals and hence social behavior has a great impact on their decision-making processes. Thus, studying social factors such as tie strength,<sup>2</sup> personality,<sup>3</sup> homophily, persuasion and satisfaction are key aspects when modeling decision-making processes in the application context of this research. As shown in Section 2.1, to the best of the authors’ knowledge no standard formulation for our probability $p _ { i , j } ,$ let alone an approach that matches our domain characteristics, has been presented in the literature so far. Hence, out of all the studied social factors we have identified a subset that can be derived from the data provided by BS and results in a good estimation of $p _ { i j }$ (as illustrated empirically in Section 7.2).

The probability of i successfully influencing j, $p _ { i , j } ,$ , is estimated by the convex combination of the following four social components: (1) $t i e _ { i , j } ,$ tie strength between i and j (i.e., how close they are); (2) sat , satisfaction of actor i with the bank; (3) inf , influence (or persuasive) capabilities of $i ; ( 4 ) p e r _ { j } ,$ personality of j, or degree of conformity. This is summarized in Eq. (3):

$$
p _ {i, j} = \alpha_ {t i e} \cdot t i e _ {i, j} + \alpha_ {s a t} \cdot s a t _ {i} + \alpha_ {i n f} \cdot i n f _ {i} + \alpha_ {p e r} \cdot p e r _ {j} + \alpha_ {o n e} \cdot o n e.\tag{3}
$$

All the components are assumed to take values in the range [0, 1]. Let us define the set of components C<sup>¯</sup> = {tie, sat, inf , per, one}, where one is a component that always takes the value 1. Coeficients $\alpha _ { c } , \quad c \in \bar { C } ,$ , represent the importance of component c and satisfy $\alpha _ { c } \geq 0$ and $\begin{array} { r } { \sum _ { c \in \bar { C } } \alpha _ { C } = 1 } \end{array}$

In the following, the components are defined in detail and a specific instantiation of each component (particular to our case study domain) is presented.

## 4.1. Tie strength $( t i e _ { i , j } )$

As shown in the literature review (Section 2.2), tie strength is strongly correlated to trust, thus, in the estimation of the reliability between i and j, $p _ { i , j } ,$ , the strength of the tie between the two actors involved is a key factor. In this research, following the definition given in the seminal paper by Granovetter [13], the tie strength is estimated as a linear combination of three of the four components he suggests. Unfortunately, the time component had to be disregarded since no information was given by BS regarding the length of the relationship between clients. However, this could be easily included in the system if provided. In summary, the tie strength is computed as follows:

$$
t i e _ {i, j} = \alpha_ {i n t} \cdot i n t _ {i, j} + \alpha_ {f r e} \cdot f r e _ {i, j} + \alpha_ {r e c} \cdot r e c _ {i, j}\tag{4}
$$

where $i n t _ { i , j } , f r e _ { i , j } , r e c _ { i , j }$ are components representing degree of intimacy, intensity and reciprocity between i and j, respectively, and take values in the range [0, 1]. Let us define the set of components $\bar { C } ^ { T I E } = \{ i n t , f r e , r e c \}$ . The real numbers $\alpha _ { c } , \quad c \in \bar { C } ^ { T I E }$ represent the importance of component c and are subject to $\alpha _ { c } \ \ge \ 0$ and $\begin{array} { r } { \sum _ { c \in \bar { C } ^ { T I E } } \alpha _ { c } = 1 } \end{array}$ . The components of the tie strength are presented in the following.

## 4.1.1. Intimacy $( i n t _ { i , j } )$

Intimacy is defined as the state of being in a very personal or private relationship (Webster’s dictionary). In the BIG CHASE, the degree of intimacy between i and j depends on the type of relationship two actors share and the level of intimacy they reflect. Let us define the function

$$
I N T (r) \mapsto [ 0, 1 ]\tag{5}
$$

where $r \in R$ is a type of relationship. Function INT assigns a real value between zero (no intimacy) and one (high personal closeness) to each type of relationship. The intimacy between i and j is given by the most intimate relationship type that the actors share:

$$
i n t _ {i, j} = \max _ {r \in R: n _ {i, j, r} > 0 \lor n _ {j, i, r} > 0} \left\{I N T (r) \right\}.\tag{6}
$$

## 4.1.2. Intensity $( f r e _ { i , j } )$

Intensity is defined as the degree or amount of strength or force that something has (Webster’s dictionary). When applied to our domain, it can be understood as the intensity, or frequency, with which two actors interact. In the BIG CHASE, the intensity between i and j is defined as:

$$
f r e _ {i, j} = \max _ {r \in R} \left\{n _ {i, j, r}, n _ {j, i, r} \right\}\tag{7}
$$

where $n _ { i , j , r }$ is the intensity of relationship type r between i and $j ,$ as defined in Section 3.1.1.

## 4.1.3. Reciprocal services(rec )

Reciprocal (of a pronoun) indicates that action is given and received by each subject (Collins dictionary). In the context of the BIG CHASE, reciprocal services indicate that relationships exist going from i to j as well as from j to i:

$$
r e c _ {i, j} = \left\{ \begin{array}{l l} 1 & \text { if } \quad (\exists r \in R: n _ {i, j, r} > 0) \land (\exists r \in R: n _ {j, i, r} > 0) \\ 0. 5 & \text { if } \quad (\exists r \in R: n _ {i, j, r} > 0) \oplus (\exists r \in R: n _ {j, i, r} > 0) \\ 0 & \text { otherwise } \end{array} \right.\tag{8}
$$

where ⊕ is the exclusive disjunction operator.

## 4.2. Satisfaction (sat<sub>i</sub>)

As motivated in the literature review (Section 2.1), in order to measure the probability that a client i endorses a bank product it is fundamental to consider the satisfaction of that client with the bank. The level of commitment of actor i with the bank, lin (introduced in Section 3.1.1), provides a reasonable proxy for the satisfaction based on the assumption that an actor that is very satisfied with the bank would be more connected or vinculated to it. Therefore:

$$
s a t _ {i} = l i n _ {i}.\tag{9}
$$

## 4.3. Influence (inf )

The proposed probability function integrates a factor that plays an important role in the definition of the probability of influencing, that is, the ability of influencing itself. This concept, as seen in the literature review (Section 2.1), is related to persuasiveness, one of the social factors involved in word of mouth and contagion. One of the ways of estimating the influence of an actor is through the computation of how well connected she is with respect to her environment. That is, through the relative log-degree of the corresponding node in graph G:

$$
i n f _ {i} = \frac {\ln d e g r e e _ {i} - \ln \min _ {j \in N} d e g r e e _ {j}}{\ln \max _ {j \in N} d e g r e e _ {j} - \ln \min _ {j \in N} d e g r e e _ {j}}\tag{10}
$$

where degree is the number of edges node i has and minj ∈ Ndegree and maxjdegree are the minimum and maximum degrees found in the graph, respectively.

## 4.4. Personality (per<sub>j</sub>)

An additional factor that needs to be estimated in order to model $p _ { i , j }$ is the probability of node j being influenced or, in other words, acting in favor of the bank’s interests. Masthoff and Gatt [19] afirm that the capacity of influence of the environment depends on the individual’s degree of conformity. Hence, the level of commitment of actor j with the bank, lin (introduced in Section 3.1.1), can be used as a proxy for the personality of node j, based on the assumption that the more vinculated an actor is with the bank, the easier it is to convince her to act in favor of the bank. On the other hand, if actor j is not connected to the bank, it would be more dificult to convince her to acquire a new product or to act in favor of the bank, since she has never showed that type of behavior before. Therefore:

$$
p e r _ {j} = l i n _ {j}.\tag{11}
$$

The last elements involved in determining the edge weights in the reliability graph (Eqs. (3) and (4)), are the coeficients $\alpha _ { c }$ that establish the contribution of each component in the formulas. In the next section we present a methodology to estimate these values from expert evaluations of given paths. Note that although in this paper specific factors for the generic components that form the probability function are presented, other factors could be used to model them. Also, other social components such as those mentioned in Section 2.1 could be introduced (e.g., homophily and length of relationship). The coeficients of the resulting function could still be optimized using the approach proposed in the following.

## 5. Projected gradient descent

In a real setting, and due to the size of the graph considered in the application context, obtaining a significant number of edge-weights evaluations could be unrealistic and extremely cumbersome for an expert. On the other hand, it is reasonable to obtain a significant sample of full paths evaluations, which provide an indirect evaluation of a much larger number of edges. Therefore, in order to estimate the best coeficients for the probability function $p _ { i , j } \left( \mathrm { E q s . } \left( 3 \right) \right.$ and (4)) we have designed a methodology based on the optimization of the Root Mean Square Logarithm Error (RMSLE) given explicit expert evaluations of the goodness of a set Q of manager-target (or s − t) paths. To do so, Eqs. (3) and (4) are firstly combined into:

$$
\begin{array}{l} p _ {i, j} = \beta_ {i n t} \cdot i n t _ {i, j} + \beta_ {f r e} \cdot f r e _ {i, j} + \beta_ {r e c} \cdot r e c _ {i, j} + \\ + \beta_ {s a t} \cdot s a t _ {i} + \beta_ {i n f} \cdot i n f _ {i} + \beta_ {p e r} \cdot p e r _ {j} + \beta_ {o n e} \cdot 1 \end{array}\tag{12}
$$

$$
\begin{array}{l} \text { where } \beta_ {i n t} = \alpha_ {t i e} \alpha_ {i n t}, \beta_ {f r e} = \alpha_ {t i e} \alpha_ {f r e}, \beta_ {r e c} = \alpha_ {t i e} \alpha_ {r e c}, \beta_ {s a t} = \alpha_ {s a t}, \\ \beta_ {i n f} = \alpha_ {i n f}, \beta_ {p e r} = \alpha_ {p e r}, \text { and } \beta_ {o n e} = \alpha_ {o n e}. \\ \text { More   generally, } p _ {i j} \text { can   be   expressed   as: } \end{array}
$$

$$
p _ {i, j} = \sum_ {c \in C} \beta c \cdot x _ {c} ^ {i, j}\tag{13}
$$

where C is the set of components $C = \{ i n t , f r e ,$ , rec, sat, inf, per, one} and $x _ { c } ^ { i , j }$ is the value of component c for edge $( i , j ) .$ Note that it still stands that $\beta _ { c } \ \ge \ 0$ and $\textstyle \sum _ { c \in C } \beta _ { c } = 1$ . Also note that, as explained in Section 3.1.1, the probability $p _ { m , j }$ of edge $( m , j )$ connecting the manager m to the client j belonging to her portfolio (i.e., the first client node in the path) is given as data and, thus, is not computed according to Eq. (13).

According to Eq. (2), the computed reliability of an s − t path P is $\begin{array} { r } { \hat { y } _ { P } = \Pi _ { ( i , j ) \in P } p _ { i , j } } \end{array}$ . Knowing the true reliability of $P , y _ { P } ,$ , the best values for the factor coeficients in Eq. (12) can be estimated by $\hat { y } _ { P } \simeq y _ { P }$ However, given the multiplicative structure of Eq. (2), the natural logarithm of both terms is considered, that is, ln yˆ  ln y . Supposing that the true reliability of a set of s − t paths Q is known, the estimation error can be computed by means of RMSLE:

$$
R M S L E = \sqrt {\frac {1}{| Q |} \sum_ {P \in Q} \left(\ln \hat {y} _ {P} - \ln y _ {P}\right) ^ {2}}\tag{14}
$$

where |Q| is the number of paths in Q. Finally, the values for the coeficients $\beta _ { c }$ can be estimated by solving the following model:

$$
\begin{array}{l l} \min & R M S L E \simeq \\ \min _ {\hat {y} _ {P}} & \sum_ {P \in Q} \left(\ln \hat {y} _ {P} - \ln y _ {P}\right) ^ {2} = \\ \min _ {\beta} & f (\beta) = \\ & \sum_ {P \in Q} \left[ \ln p _ {m, j} + \sum_ {(i, j) \in \hat {P}} \left(\ln \sum_ {c \in C} \beta c \cdot x _ {c} ^ {i, j}\right) - \ln y _ {P} \right] ^ {2} \end{array}\tag{15}
$$

$$
s. t. \quad \beta \geq 0 \quad \forall c \in C\tag{16}
$$

$$
\sum_ {c \in C} \beta = 1\tag{17}
$$

where $\hat { P } = P { - } ( m , j ) , \mathrm { i . e }$ ., the set of edges in P excluding the first edge, that is, the edge leaving from the manager m. Note that minimizing the RMSLE is equivalent to minimizing $f ( \beta )$ as the square root and the average do not affect the optimization direction.

For the solution of this optimization problem a Projected Gradient Descent algorithm (PGD) is proposed. This decision is motivated by the gradient descent approaches used in recent works such as: Liu et al. [18] where authors use a gradient approach to learn user preferences in Web content or Chen et al. [5] where authors use a gradient approach in informative friend recommendation models. Hence, given a solution $\beta ^ { n - 1 }$ it generates iteratively the nth solution $\beta ^ { n }$ via:

$$
\beta^ {n} = \pi_ {S} \left(\beta^ {n - 1} - \gamma \cdot \nabla f \left(\beta^ {n - 1}\right)\right)\tag{18}
$$

where $\nabla f ( \boldsymbol { \beta } ^ { n - 1 } )$ is the gradient of the objective function (Function (15)) evaluated at $\beta ^ { n - 1 } , \gamma > 0$ is the step size, and $\pi _ { S }$ is the projection operator.

Note that for a generic solution $\beta ,$ the gradient ∇f(b) is the vector of the partial derivative of f(b), defined for a specific $\beta _ { c ^ { \prime } }$ as:

$$
\frac {\delta f (\beta)}{\delta \beta_ {c ^ {\prime}}} = 2 \sum_ {P \in Q} \left[ (\ln \hat {y} _ {P} - \ln y _ {P}) \cdot \sum_ {(i, j) \in \hat {P}} \frac {x _ {c ^ {\prime}} ^ {(i , j)}}{\sum_ {c \in C} \beta_ {c} \cdot x _ {c} ^ {(i , j)}} \right].\tag{19}
$$

The projection operator p projects any point into the closest point (by Euclidean distance) belonging to the convex set S defined by the problem’s constraints:

$$
S = \left\{\beta \in \mathbb {R} ^ {| C |}: \beta \geq 0, \sum_ {c \in C} \beta = 1 \right\}.\tag{20}
$$

Specifically, the considered convex set S is a probability simplex and the corresponding projection operator p is defined as follows:

$$
\pi (\beta) = (\beta - \lambda \mathbb {1}) _ {+}\tag{21}
$$

where k is obtained by solving:

$$
\mathbb {1} ^ {\top} (\beta - \lambda \mathbb {1}) = \sum_ {c \in C} \max \left\{0, \beta_ {c} - \lambda \right\} = 1.\tag{22}
$$

In this paper, the projection operator is implemented using the algorithm proposed by Wang and Carreira-Perpiñán [30], which is very eficient.

Algorithm 1. Projected Gradient Descent algorithm.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:  $\gamma$ ,  $\mu$ .

Output:  $\beta^{n}$ .

1: n := 1;    ▷ Iteration counter initialization.

2:  $\beta_{n}^{n} := unif(0,1) \forall c \in C$ ;    ▷ Random generation of initial point.

3:  $\beta^{n} := \pi_{S}(\beta^{n})$ ;    ▷ Projection of initial point.

4: m := 0;    ▷ Non-improving iteration counter initialization.

5: while  $m \leq \mu$  do

6:  $\beta^{n+1} := \pi_{S}(\beta^{n} - \gamma \cdot \nabla f(\beta^{n}))$ ;    ▷ Generating next point.

7: if RMSLE( $\beta^{n+1}$ ) &lt; RMSLE( $\beta^{n}$ ) then    ▷ Checking for improvement in the RMSLE.

8: m := 0;    ▷ Resetting the non-improving iteration counter.

9: else

10: m := m + 1;    ▷ Incrementing the non-improving iteration counter.

11: end if

12: n := n + 1    ▷ Incrementing the iteration counter.

13: end while

14: return  $\beta^{n}$
</div>

The complete procedure for the proposed PGD is described in Algorithm 1. The algorithm requires as input the step size c and the maximum number of non-improving iterations, l, that is used as termination criterion. Next, the algorithm generates the initial point $\beta ^ { 1 }$ by assigning random uniform values in [0, 1] to its component. To ensure feasibility, the initial point is projected onto the convex space S. Also, the iteration counter n is set to one and the nonimproving iteration counter m is set to zero. In the main loop, the algorithm generates the next point according to Eq. (18). Finally, the algorithm iterates until l subsequent non-improving iterations have been completed.

Once the components coeficients $( \beta _ { c } )$ have been estimated, it is possible to compute the traversal probability of the edges in the graph $( p _ { i , j } )$ and, therefore, the paths’ reliabilities (yˆ ). In the following section, we present the optimization model used to compute the maximum reliability paths between a manager and a target actor.

## 6. Maximum reliability path algorithm

In this section, we introduce the algorithm designed to identify the sequence of clients that a manager should contact to reach a desired target. In the context of graph optimization, the BIG CHASE can be described as follows:

Given a weighted graph $G = ( N , E )$ where the weight associated to an edge $( i , j ) \in E , p _ { i , j }$ , represents the probability of traversal, a source node s, a destination node t, and a maximum length L, find the most reliable path connecting the source node, s, to the destination node, t, comprised of at most L edges.

More formally, the problem can be defined as:

$$
\max _ {P} \quad \hat {y} _ {P} = \prod_ {(i, j) \in P} p _ {i, j}\tag{23}
$$

$$
s. t. \sum_ {j: (i, j) \in P} 1 - \sum_ {j: (j, i) \in P} 1 = \left\{ \begin{array}{l l} 1, \text { if   } i = s; \\ - 1, \text { if   } i = t; & \forall i \in N \\ 0, \text { otherwise }. \end{array} \right.\tag{24}
$$

$$
(i, j) \in E, \quad \forall (i, j) \in P\tag{25}
$$

$$
\left| P \right| \leq L.\tag{26}
$$

The goal is to identify the maximum reliability path P, defined as a set of edges. The first constraints (Eq. (24)) impose classical flow conditions on the nodes. The second set of constraints (Eq. (25)) imposes

Please cite this article as: L. Quijano-Sanchez, F. Liberatore, The BIG CHASE: A decision support system for client acquisition applied to financial networks, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.04.007

that all the edges in P must belong to the set of edges E. Finally, the last constraint (Eq. (26)) establishes that the total number of edges in P must be L at most.

This problem is equivalent to a length-constrained Most Reliable Path problem [23,25]. Thus, the BIG CHASE can be solved by the labeling procedure described by Dijkstra [8] on an alternative graph where the weights of the edges are $w _ { i j } = - \mathrm { l n } p _ { i j } .$ . However, the fastest implementation of the Dijkstra runs in $O ( | E | \stackrel { \cdot } { + } | V | \log | V | )$ That means that, despite being a very eficient algorithm, Dijkstra’s cannot be used effectively on a large set of (manager, target) pairs, due to the size of graph G that, as a result of the application context, is comprised of millions of nodes and edges. This problem has been addressed in this research by implementing a number of optimizations in the solution algorithm.

Algorithm 2. Batch Maximum Reliability Path algorithm on large graph.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: $\gamma, \mu$.

Output: $\beta^n$.

1: $n := 1$; $\triangleright$ Iteration counter initialization.

2: $\beta_c := \text{unif}(0,1) \forall c \in C$; $\triangleright$ Random generation of initial point.

3: $\beta^n := \pi_S (\beta^n)$; $\triangleright$ Projection of initial point.

4: $m := 0$; $\triangleright$ Non-improving iteration counter initialization.

5: while $m \leq \mu$ do

6: $\beta^{n+1} := \pi_S (\beta^n - \gamma \cdot \nabla f (\beta^n))$; $\triangleright$ Generating next point.

7: if RMSLE $(\beta^{n+1}) &lt; RMSLE (\beta^n)$ then $\triangleright$ Checking for improvement in the RMSLE.

8: $m := 0$; $\triangleright$ Resetting the non-improving iteration counter.

9: else

10: $m := m + 1$; $\triangleright$ Incrementing the non-improving iteration counter.

11: end if

12: $n := n + 1$; $\triangleright$ Incrementing the iteration counter.

13: end while

14: return $\beta^n$
</div>

Algorithm 2 illustrates the pseudocode of the procedure implemented to solve the length-constrained Maximum Reliability Path on a large graph for a single source node and multiple target nodes. The algorithm requires as inputs the graph $G = ( N , E ) ,$ , the source node s (i.e., the manager), the set of targets T (i.e., a list of target users), and the maximum length L, and it returns a set of maximum reliable paths Q. First, the set Q is initialized to the empty set. Then, all the manager nodes apart from t are removed from G. This step is necessary to ensure that the solution paths do not go through other managers. Next, the algorithm extracts the ego graph of node s having order L: an ego graph is the subgraph comprised of the nodes not farther than a given limit (the order) from the origin node (the ego). The ego graph is obtained by breadth-first exploration of the original graph. Note that, given that L is relatively small compared to the diameter of the graph, this operation is practically inexpensive. A consequence of this operation is that all the target nodes that cannot be reached from s in L steps are excluded from the ego graph. Next, the algorithm loops on every target node t that can still be reached and, for each of them, it takes the following operations: first, it removes from the source ego graph all the non-client nodes, while preserving t. This step is necessary as the path should not go through non-client nodes. At this point, the connectivity between the source node s and the current target node t could have been compromised $( \mathbf { e . g . }$ , the only s − t path went through a non-client node). Therefore, the algorithm extracts the order L ego graph of t from the source ego graph and checks if the source node s belongs to it. If that is the case, then at least a feasible s − t path exists and we can find the most reliable one by running Dijkstra on the target ego graph. Note that this graph is just a small fraction of the original graph in size, therefore, Dijkstra can be run eficiently on it. The most reliable path found is stored in Q. Finally, once all the target nodes have been processed, the algorithm returns the set of the most reliable paths Q.

As illustrated in next section, the algorithm proved to be very eficient on a real case study. Another advantage of its structure is that it can be easily parallelized in a cluster by running steps 2 and 3 (see Algorithm 2) on the driver node and the remaining steps on the worker nodes. Then, each worker node could process all the queries for a single manager, resulting in an eficient and scalable algorithm.

## 7. Case study

In this section, an application of the BIG CHASE to a real context is presented. Specifically, the BIG CHASE has been applied to the financial data relative to 2015 BS’s Spanish clients. Experimental results show that the proposed probability function and PGD method are capable of modeling the evaluations given by experts with a reasonable error. The validation has been performed with the following data:

## 7.1. Sets and data

A description of the sets and data introduced as input in this case study is given in the following.

$- N ^ { c l i }$ , initial cardinality of the set is 6,440,864. All clients that do not appear in any relationship in the last year have been removed. After this operation, the size of the set is 5,742,380.

$- N ^ { n o n } ,$ , initial cardinality of the set is 1,795,633.

$. ~ N ^ { m a n }$ , cardinality of the set is $3 5 9 0 . \textrm { - } M _ { m } \subseteq N ^ { c l i } , \forall m \textrm { \in } N ^ { m a n }$ portfolios are given as (manager, client) pairs. The total number of pairs is 3,819,091.

– R, 12 different types of relationships are considered and presented in Table 1 with a brief description. In case of relationships representing payments or money exchanges (e.g., rent, payer), the end user is the receiver.

$l i n _ { i } ,$ value of the strength of the relationship of an actor with the bank has been defined a priori by the bank following a procedure that is used for internal evaluation of the clients. The details of how this value is computed are sensible information and cannot be divulged.

$\cdot p _ { m , j } ,$ value of the strength of the relationship between a manager and a client has been also defined by the bank. This value is computed according to the following formula:

$$
p _ {m, j} = \left\{ \begin{array}{l l} 0. 9 5, & \quad \text {if} \quad c o n _ {m, j} <   p e r c _ {2 0} \\ 0. 9 6, & \quad \text {if} \quad c o n _ {m, j} <   p e r c _ {4 0} \\ 0. 9 7 5, & \quad \text {if} \quad c o n _ {m, j} <   p e r c _ {6 0} \\ 0. 9 9, & \quad \text {if} \quad c o n _ {m, j} <   p e r c _ {8 0} \\ 1, & \quad \text {if} \quad c o n _ {m, j} \geq p e r c _ {8 0} \end{array} \right.
$$

where $c o n _ { m , j }$ is the number of contacts between the manager m and client j in the time frame considered and $p e r c _ { x }$ is the x-th percentile.

$\textstyle - n _ { i , j , r } ,$ this value depends on the number of times that the actors have shared the relationship type considered. For instance, all the relationship types that two agents have not shared in the last year

Relationship types. For each type, the table shows a brief description, the corresponding value in the intimacy function (as defined by the experts from BS), and the reciprocity.

<table><tr><td>Relationship type</td><td>Definition</td><td>INT</td><td>Reciprocal</td></tr><tr><td>Rent</td><td>i pays the rent to j.</td><td>0.3</td><td>No</td></tr><tr><td>Friendly</td><td>i and j are friends.</td><td>0.8</td><td>Yes</td></tr><tr><td>Proxy</td><td>i is a proxy representative of j.</td><td>0.9</td><td>No</td></tr><tr><td>Reverse factoring</td><td>i pays j through reverse factoring.</td><td>0.7</td><td>No</td></tr><tr><td>Proposal</td><td>i proposes j as the ordering party of a reverse factoring which is not approved by the bank yet.</td><td>0.7</td><td>No</td></tr><tr><td>Co-owner</td><td>i and j co-own an account.</td><td>1</td><td>Yes</td></tr><tr><td>Discount</td><td>i pays j through a discount service.</td><td>0.6</td><td>No</td></tr><tr><td>Related</td><td>i and j are related.</td><td>1</td><td>Yes</td></tr><tr><td>Subsidiary</td><td>i is a company controlled by j.</td><td>0.6</td><td>Yes</td></tr><tr><td>Payer</td><td>i pays the pension or the salary to j.</td><td>0.3</td><td>No</td></tr><tr><td>Card</td><td>i has a corporative card of j.</td><td>0.8</td><td>Yes</td></tr><tr><td>Transfer</td><td>i performs a transfer to j.</td><td>0.7</td><td>No</td></tr></table>

Error measures plot

take value zero. In case a relationship type is shared, the value of $n _ { i , j , r }$ is computed according to the following rules:

$$
n _ {i, j, r} = (f r e q \_ s c o r e _ {i, j, r} + a m o u n t \_ s c o r e _ {i, j, r}) / 2\tag{27}
$$

where:

$$
\begin{array}{l} f r e q \_ s c o r e _ {i, j, r} = \left\{ \begin{array}{l l} 0. 2 5, & \text { if } \quad f r e q _ {i, j, r} <   p e r c _ {2 0} \\ 0. 5, & \text { if } \quad f r e q _ {i, j, r} <   p e r c _ {5 0} \\ 0. 7 5, & \text { if } \quad f r e q _ {i, j, r} <   p e r c _ {7 0} \\ 1, & \text { otherwise } \end{array} \right| a m o u n t \_ s c o r e \\ = \left\{ \begin{array}{l l} 0. 2 5, & \text { if } \quad a m o u n t _ {i, j, r} <   p e r c _ {2 0} \\ 0. 5, & \text { if } \quad a m o u n t _ {i, j, r} <   p e r c _ {5 0} \\ 0. 7 5, & \text { if } \quad a m o u n t _ {i, j, r} <   p e r c _ {7 0} \\ 1, & \text { otherwise }. \end{array} \right. \end{array}\tag{28}
$$

The percentiles $p e r c _ { x }$ are relative to the type of relationship considered.

Relationships that are marked as reciprocal in Table 1 (e.g., coowner) represent an exception to the rule. In fact, when two actors share a reciprocal relationship, it stands that $n _ { i , j , r } = n _ { j , i , r } = 1$ . The initial number of non-zero values is 18,579,692. All the values relative to removed nodes have been set to zero. After this operation, the number of non-zero values is 17,976,814.

Finally, BS has provided 133,097 (manager,target) pairs of interest, corresponding to 8675 unique targets. That is equivalent to running 133,097 instances of the Maximum Reliability Path problem on the graph. The graph built from the data provided is formed by 5,754,645 nodes and 17,976,814 edges. Concerning the probability function, the experts from BS provided the values for function INT (Table 1) that associates each type of relationship with a level of intimacy.

## 7.2. Computational experience

To estimate the component coeficients for the probability function (Eq. (12)), BS has provided explicit evaluations of s−t paths given by experts. Two former managers having similar levels of experience and seniority have evaluated 143 paths. The evaluations given by the experts (that show a Spearman correlation of 0.8206, indicating very similar rankings) are averaged to obtain a single measure of reliability for each path. Overall, the sample includes 28 managers, 61 targets and 165 edges.

Given the random nature of the PGD procedure proposed, we run the algorithm 10 times and record the computational time (in seconds), number of iterations, RMSLE, Root Mean Square Error (RMSE), and Mean Absolute Error (MAE). The parameters used are: $\gamma = 0 . 0 0 1$ (step size) and $\mu = 1 0$ (allowed non-improving iterations). The average values and the standard deviations obtained in training (rounded to the fourth digit) are: time 178.49 ± 38.7248; iterations 324.3 ± 70.7626; RMSLE 0.2354 ± 0; RMSE $0 . 1 0 2 9 \pm \quad 0 ;$ MAE 0.0771 ± 0.0001. A run of the algorithm takes approximately three minutes, which is totally acceptable considering the application context. The high variation in the computational time and iterations is due to the random initialization. However, it can be observed that the algorithm shows a very stable behavior in terms of convergence, as the standard deviation of the error measures are approximately equal to zero. The MAE obtained in training is extremely low, especially considering that the PGD is trying to adjust the parameter of the trust function to subjective evaluations that might not be internally coherent. Finally, Fig. 2 is a plot of the evolution of the error measures for one of the runs. Interestingly the three error measures show identical behavior suggesting that, for the dataset and parameters considered,

![](/api/attachments/2RQGTK8C/fulltext/images/92569530ceaca87e5f8bbc6de716e7496e144ef34c6f2c070a4bb513fc40afed.jpg)  
Fig. 2. Error measures plot

Please cite this article as: L. Quijano-Sanchez, F. Liberatore, The BIG CHASE: A decision support system for client acquisition applied to financial networks, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.04.007

optimizing the RMSLE is equivalent to optimizing the RMSE and the MAE.

Leave-One-Out Cross-Validation has been used for testing. The algorithm has been run only once per sample element as it showed in training good convergence properties on the data considered. The errors obtained are: RMSLE 0.2401; RMSE 0.1049; and MAE 0.0788. The errors in the test are slightly larger than the training, but they are still very close and comparable. Apart from confirming the ability of the BIG CHASE to correctly model and represent the knowledge of experts, it also indicates that there is no overfitting.

The best set of coeficients found has been used to assign weights to the graph. The Maximum Reliability Path algorithm (Algorithm 2) has been run on the graph with a maximum length L = 3. The most reliable path exists for 7941 of the initial 133,097 (manager, target) pairs and all the remaining pairs are actually disconnected in the graph. Given the low number of solutions found, the optimization algorithm has been modified to provide all the existing s − t paths in the graph (8256 paths), ranked according to their total reliability.

## 7.3. Evaluation of the BIG CHASE

As pointed out in Section 1, the BIG CHASE has been developed in strict collaboration with BS. The system has been defined after several meetings and interviews with experts from the BS, to provide a DSS tailored to their requirements and characteristics of the problem, over the course of six months approx. The positive results obtained in the computational experience motivated the full implementation of the BIG CHASE and its subsequent installation in BS’s servers. The system is now being run monthly for all the client–manager portfolios.

To assess the usefulness of the BIG CHASE, 10 managers have taken a short survey addressing their opinion on the subject. The questionnaire is comprised of three questions that can be answered on a 10-Likert scale: i) How much does it facilitate the acquisition of new clients?; ii) Please, rate your level of satisfaction with the tool (0, extremely bad; 10, extremely good); iii) How much do you consider that the tool helps your productivity in terms of goals achieved?

The minimum, mean and standard deviations of the answers are: Question (i) min $= 6 / \bar { x } = 7 . 8 / s = 1 . 1 4 ;$ Question (ii) min = $6 / \bar { x } = 7 / s = 0 . 8 2 ;$ Question (iii) min $= 7 / \bar { x } = 7 . 7 / s = 0 . 4 8$ This preliminary evaluation of the usefulness of the BIG CHASE is indeed promising. In fact, the averages are all greater than or equal to seven and the minimum scores are greater than or equal to six. Due to its success, BS is planning on pursuing in the next year more studies on DSSs that further exploit the information provided by the relationship network.

## 8. Conclusions

This study presents a comprehensive system for client acquisition in a financial context developed in collaboration with Banco Santander, S.A. Our methodology, called the BIG CHASE, can be easily adapted or extended to other application contexts. Specifically, our proposal relies on translating financial data on bank clients and operations into a reliability graph were edge weights represent the probability of a client positively influencing an existing or a potential client. The goal is to identify the most reliable path connecting an initial node representing a manger to a target node. Given the lack of historical data on client acquisition, the edge weights are approximated using a probability function that models the actors’ social reality. This function’s parameters can be adjusted through explicit path evaluations provided by experts. To this end we propose a Projected Gradient Descent Algorithm specifically designed for the problem at hand. Once the graph is weighted, we can identify the best solution by solving a Maximum Reliability Path problem, adapted to be run on a large network. Finally, the BIG CHASE has been tested on Spain’s 2015 BS financial data. Our tests show that the BIG CHASE is capable of modeling the evaluations provided by bank experts with a low margin of error (MAE 0.08, approx.) and of identifying the most reliable s − t paths in a large graph (5,754,645 nodes and 17,976,814 edges). Qualitative assessment of the BIG CHASE’s usefulness reported that the system is in general useful, that provides solid support to the operations of client acquisition and is a substantial help for the achievement of client–managers ’ goals.

Despite the positive results, a number of potential improvements, variants and new research lines are possible. The probability function can be improved by enhancing the definitions of its components, i.e., satisfaction, personality, influence and tie strength. This would require new sources of data. Also, the function could be extended by including new factors, such as those presented in the literature (see Section 2). This variability facilitates reusability of our method.

## Acknowledgments

We would like to thank María del Mar Ruiz-Andújar, Álvaro Fernández-Velando, Fernando Baladrón-Herrera, Miguel Angel González-Álvarez, Mónica Tevar-Zamora and Paola Rosario Sordo-Fernández from Banco Santander, S.A. for their time, help and support. Also, we thank the Editor and two anonymous reviewers for their constructive and insightful comments.

## References

[1] S.G. Barsade, The ripple effect: emotional contagion and its influence on group behavior, Adm. Sci. Q. 47 (4) (2002) 644–675.

[2] R.S. Burt, Toward a structural theory of action: network models of social structure, perception and action, Am. J. Sociol. 90 (6) (1982) 1336–1338.

[3] A.M. Calvão, C.A. Paixão, F.C. Coelho, R.R. Souza, The consumer litigation industry: chasing dragon kings in lawyer–client networks, Soc. Networks 40 (2015) 17–24.

[4] J.O. Chan, Toward a unified view of customer relationship management, J. Am. Acad. Bus. 6 (2005) 32–38.

[5] C.C. Chen, S.Y. Shih, M. Lee, Who should you follow? Combining learning to rank with social influence for informative friend recommendation, Decis Support. Syst. 90 (2016) 33–45.

[6] J. Chen, X. Shen, Consumers’ decisions in social commerce context: an empirical investigation, Decis. Support. Syst. 79 (2015) 55–64.

[7] H. Dai, X.R. Luo, Q. Liao, M. Cao, Explaining consumer satisfaction of services: the role of innovativeness and emotion in an electronic mediated environment, Decis. Support. Syst. 70 (2015) 97–106.

[8] E.W. Dijkstra, A note on two problems in connexion with graphs, Numer. Math 1 (1959) 269–271.

[9] X. Du, Y. Ye, R.Y.K. Lau, Y. Li, OpinionRings: inferring and visualizing the opinion tendency of socially connected users, Decis. Support. Syst. 75 (2015) 11–24.

[10] B. Fang, P. Zhang, Big Data in Finance, Springer International Publishing. 2016.

[11] E. Gilbert, K. Karahalios, Predicting tie strength with social media, International Conference on Human Factors in Computing Systems, CHI ’09, 2009. pp. 211-220

[12] J. Golbeck, Combining Provenance with Trust in Social Networks for Semantic Web Content Filtering, International Provenance and Annotation Workshop, IPAW’06, vol. 4145, 2006. pp. 101–108.

[13] M.S. Granovetter, The strength of weak ties, Am. J. Sociol. 78 (1973) 1360–1380.

[14] A. Gustafsson, M.D. Johnson, I. Roos, The effects of customer satisfaction, relationship commitment dimensions, and triggers on customer retention, 69 (2005)210-218

[15] R. Ivengar, C. Van den Bulte, T.W. Valente, Opinion leadership and social contagion in new product diffusion, Mark. Sci. 30 (2011) 195–212.

[16] G.J. King, X. Chao, I. Duenyas, Dynamic customer acquisition and retention management, Production and Operations Management (2016)

[17] N. Lin, W.M. Ensel, J.C. Vaughn, Social resources and strength of ties: structura factors in occupational status attainment, Am. Sociol Rey 46 (1981) 393-405

[18] X. Liu, R. Nielek, P. Adamska, A. Wierzbicki, K. Aberer, Towards a highly effective and robust Web credibility evaluation system, Decis. Support. Syst. 79 (2015) 99–108.

[19] J. Masthoff, A. Gatt, In pursuit of satisfaction and the prevention of embarrassment: affective state in group recommender systems, User Model. User-Adap. Inter. 16 (2006) 281–319.

[20] M. Mcpherson, L.S. Lovin, J.M. Cook, Birds of a feather: homophily in social networks, 2001.

[21] E.W. Ngai, L. Xiu, D.C. Chau, Application of data mining techniques in customer relationship management: a literature review and classification, Expert Syst. Appl.36 (2009) 2592-2602

Please cite this article as: L. Quijano-Sanchez, F. Liberatore, The BIG CHASE: A decision support system for client acquisition applied to financial networks, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.04.007

[22] S.P. Penczynski, Persuasion: An Experimental Study of Team Decision Making, University of Mannheim, Department of Economics. 2014.

[23] R. Petrovic, S. Joanovic, Two algorithms for determining the most reliable path of a network, IEEE Trans. Reliab. 28 (2) (1979) 115–119.

[24] L. Quijano-Sánchez, B. Díaz-Agudo, J.A. Recio-García, Development of a group recommender application in a social network, Knowl.-Based Syst. 71 (2014) 72–85.

[25] N.G.F. Sancho, Maximum reliability through a network with resource constraints, J. Oper. Res. Soc. 36 (1985) 537–540.

[26] X. Shi, L. Adamic, M. Strauss, Networks of strong ties, Physica A 378 (2007) 33–47.

[27] K. Storbacka, T. Strandvik, C. Grnroos, Managing customer relationships for profit: the dynamics of relationship quality, Int. J. Serv. Ind. Manag. 5 (1994) 21–38.

[28] P. Victor, C. Cornelis, M.D. Cock, A. Teredesai, Key figure impact in trust-enhanced recommender systems, AI Commun. 21 (2008) 127–143.

[29] L. Wang, L. Doucet, G. Northcraft, Culture, Affect, and Social Influence in Decision-Making Groups, 2006, 147–172.

[30] W. Wang, M.Á. Carreira-Perpiñán, Projection onto the probability simplex: an eficient algorithm with a simple proof, and an application, CoRR abs/1309.1541 (2013)

[31] R. Xiang, J. Neville, M. Rogati, Modeling relationship strength in online social networks, International Conference on World Wide Web, WWW’10, 2010. pp. 981–990.

[32] X. Yang, X. Zhang, F. Zuo, Word of Mouth: The Effects of Marketing Efforts and Customer Satisfaction, International Joint Conference on Artificial Intelligence, IJCAI’09, 2009. pp. 687–690.

[33] Y. Katz, J. Golbeck, Social network-based trust in prioritized default logic. In: International Conference on Innovative Applications of Artificial Intelligence, IAAI’06, 2006. pp. 1345–1350,

[34] A. Wierzbicki, Trust and Fairness in Open, Distributed Systems, Studies in Computational Intelligence 298. Springer 2010.

Lara Quijano-Sanchez is a Postdoc Researcher at the UC3M-BS Institute of Big Data for Finance. Her areas of research are recommender systems, group recommender systems, social networks, expert systems, user modeling, knowledge-based systems, cased-based reasoning, information retrieval and explanations. She is presently working in the analysis of social networks applied to financial Big Data and, in sensors and big data research applied to mobile tourism recommender applications.

Federico Liberatore is a Postdoc Researcher at the UC3M-BS Institute of Big Data for Finance and a Fulbright Alumni. His area of expertise are Location Analysis, Humanitarian Logistics, Combinatorial Optimization and Operational Research in general. He also has relevant research experience in Artificial Intelligence and Time Series Analysis. His present research work involves the analysis of large-scale networks applied to financial Big Data, as well as evacuation models in Humanitarian Logistics, and police patrolling and resource location models.
