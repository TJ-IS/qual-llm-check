---
otero_id: 1890
otero_key: "HAFFY2HV"
title: "A new role mining framework to elicit business roles and to mitigate enterprise risk"
authors: "Alessandro Colantonio; Roberto Di Pietro; Alberto Ocello; Nino Vincenzo Verde"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.022"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A new role mining framework to elicit business roles and to mitigate enterprise risk

Alessandro Colantonio <sup>a,b,</sup>⁎, Roberto Di Pietro <sup>b</sup>, Alberto Ocello <sup>a</sup>, Nino Vincenzo Verde <sup>b</sup>

<sup>a</sup> Engiweb Security, Roma, Italy

<sup>b</sup> Università di Roma Tre, Dipartimento di Matematica, Roma, Italy

## a r t i c l e i n f o

## Available online 19 August 2010

Keywords: RBAC Role engineering Role mining Risk management Clustering coef<sup>fi</sup>cient

## a b s t r a c t

Role-based access control (RBAC) allows to effectively manage the risk derived from granting access to resources, provided that designed roles are business-driven. Role mining represents an essential tool for role engineers, but existing techniques are not able to elicit roles with an associated clear business meaning. Hence, it is dif<sup>fi</sup>cult to mitigate risk, to simplify business governance, and to ensure compliance throughout the enterprise. To elicit meaningful roles, we propose a methodology where data to analyze are decomposed into smaller subsets according to the provided business information. We introduce two indices, minability and similarity, that drive the decomposition process by providing the expected complexity to <sup>fi</sup>nd roles with business meaning. The proposed methodology is rooted on a sound theoretical framework. Moreover, experiments on real enterprise data support its effectiveness

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Access control is a cornerstone of enterprise risk and security management. It represents the process of mediating requests to data and services maintained by a system, and determining whether the requests should be granted or denied [11]. It is the responsibility of an access control system to ensure that only users with legitimate credentials are granted permissions to access requested resources. Hence, in an access control model the risk factor of illegitimate credentials is eliminated by construction [2]. Signi<sup>fi</sup>cant research has focused on providing formal representations of access control models. Among all models proposed in the literature, Role-Based Access Control (RBAC) [1] is certainly the most adopted by medium- to large-size organizations, greatly due to its simplicity: a role can be seen as a set of permissions; users, in turn, are assigned to appropriate roles based on their responsibilities and quali<sup>fi</sup>cations. As a result, RBAC offers great bene<sup>fi</sup>ts to business users. A role represents a job function or a title established for a set of users within an organization. Thus, the adoption of RBAC makes it easier to de<sup>fi</sup>ne security policies by business users [16]. RBAC also implements the appropriate security engineering principles to enforce risk reduction, such as separation of duties (SoD) and least privilege [2]. Further, the use of roles minimizes system administration effort due to the reduced number of relationships required to relate users to permissions [5].

Despite the bene<sup>fi</sup>ts related to deploying role-based access control systems, many organizations are reluctant to adopt them, since there are still some important issues that need to be addressed. In particular, the model must be customized to capture the needs and functions of the organization. In an ideal RBAC environment, we expect roles to be well de<sup>fi</sup>ned so that role de<sup>fi</sup>nitions are formed with strict role boundary rules in order to enforce all the required enterprise security policies. Unfortunately, where RBAC is deployed, this rarely happens, thus leading to role misuse [2]. For this purpose, the role engineering discipline [9] has been introduced. However, choosing the best way to design a proper set of roles is still an open problem. Various approaches to role engineering have been proposed, which are usually classi<sup>fi</sup>ed as: top-down and bottom-up. The former requires a deep analysis of business processes to identify which access permissions are necessary to carry out speci<sup>fi</sup>c tasks. The latter seeks to identify de facto roles embedded in existing access control information. Since bottom-up approaches usually resort to data mining techniques, the term role mining is often used as a synonym for bottom-up. To maximize bene<sup>fi</sup>ts, bottom-up should be used in conjunction with top-down, leading to an hybrid approach. As a matter of fact, top-down may ignore existing permissions and exceptions, whereas bottom-up may not consider the business functions of an organization [19].

The bottom-up approach has attracted researchers, since it can be easily automated [22]. Indeed, companies which plan to go for RBAC usually <sup>fi</sup>nd themselves in the situation of having a collection of several legacy and standard security systems on different platforms that provide “conventional” access control [20]. Thus, role mining is the application of data mining techniques to generate roles from the access control information of this collection of systems. Several works prove that the role mining problem is reducible to many other well-known NP-hard problems, such as clique partition, binary matrix factorization, bi-clustering, graph vertex coloring [6,8,32] to cite a few. However, on one hand the slavish application of standard data mining approaches to role engineering might yield roles that are merely a set of permissions, namely with no connection to the business practices. On the other hand organizations are unwilling to deploy roles they cannot bind to a business meaning [5]. Indeed, such roles could have some dif<sup>fi</sup>culties in being inserted within the risk management framework in use within the organization. In such a case, risks are incurred to the system by users that are authorized to use their access right in an incorrect manner [2]. Moreover, when hundreds of thousands of existing user–permission assignments need to be analyzed, the number of candidate roles might be so high that trying to assign a business meaning to each of them is often impracticable. The number of candidate roles may also grow because of the “noise” within the data—namely, permissions exceptionally or accidentally granted or denied. In such a case, classical role mining algorithms discover multiple small fragments of the true role, but missing the role itself [7]. This increases the risk of designing roles that do not capture the actual business needs of the organization.

Only a few recent works value business requirements in role mining [3,5] by proposing a measure for the business meaning of roles. However, it is dif<sup>fi</sup>cult to introduce this metric in existing role mining approaches currently found in the literature. An alternative way of leveraging business-related information to offer meaningful candidate role-sets may be by restricting the analysis to sets of data that are homogeneous from an enterprise perspective. For instance, let us suppose that a partial or coarse-grained top-down analysis identi<sup>fi</sup>es a certain set of users that perform the same tasks, but the analysis lacks the knowledge of which permissions are required for the execution of these tasks. In this scenario, by restricting role mining techniques to these users only—instead of analyzing the organization as a whole—, the elicited roles will be related to such tasks. Thus, it will likely be easier to assign a business meaning to the results obtained from the bottom-up approach. Moreover, by grouping users that perform similar tasks together <sup>fi</sup>rst, and then analyzing them separately, eliciting roles with no business meaning can be avoided. Indeed, investigating analogies among groups of users that perform completely different tasks is far from being a good role mining strategy [5]. Further, it will be easier to manage resulting candidates roles, achieving two results: a simpli<sup>fi</sup>cation of the security policy enforcement process; and, a reduction of the risk related to unintentional/incorrect use of granted permissions through roles. Partitioning data also introduces bene<sup>fi</sup>ts in terms of execution time of role mining algorithms. Indeed, most role mining algorithms have a complexity that is not linear with respect to the number of users or permissions to analyze [3,13,21,30]. Based on previous observations, several enterprise information may be used to decompose the role mining problem. Business processes, work<sup>fl</sup>ow tasks, and organization unit trees are just a few examples of business elements that can be leveraged. Usually, such information is already available in most companies before starting the role engineering task. However, when dealing with information from several sources, a few decisions have to be made about: what information can actually improve the role mining process; what level of detail is required; and, lastly, how to verify that each sub-problem is easily solvable using a data mining algorithm.

To address all the abovementioned issues, this paper proposes a methodology that helps role engineers leverage business information during the role mining process. In particular, we propose to divide the access data to analyze into smaller subsets that are homogeneous according to some business data, instead of performing a single bottom-up analysis on the entire organization. This eases the attribution of business meaning to automatically elicited roles and reduces the problem complexity, thus allowing for better enforcement of security policies and reducing the risk related to illegal accesses. In order to select the best business information that improves the subsequent role mining process, as well as to establish how deeply the data must be partitioned, two indices, referred to as minability and similarity, are identi<sup>fi</sup>ed. Minability and similarity are both rooted on sound mathematical theory. These indices are used to measure the expected complexity of analyzing the outcome of the bottom-up approaches. Leveraging these indices allows for the identi<sup>fi</sup>cation of business information that best <sup>fi</sup>ts with the access control data, namely the information that induces a decomposition which increases the business meaning of the roles elicited in the role mining phase and, at the same time, simpli<sup>fi</sup>es the analysis. This leads to a decrease in the likelihood of making errors in role management, and consequently reduces the risk of role misuse. The paper also introduces two fast probabilistic algorithms to ef<sup>fi</sup>ciently compute such indices, making them suitable also for big organization with hundreds of thousands of users and permissions. The quality of the indices is also formally assured. Several examples illustrate the practical implications of the proposed methodology and related tools, which have also been applied on real enterprise data. Results support the quality and viability of the proposal.

The paper is organized as follows: Section 2 introduces the background required to formally describe the proposed tools and reports on related works. The adopted risk model is then described in Section 3, that also maps typical risk-related concepts to RBAC entities. Minability and similarity indices are introduced and further discussed with simple examples in Section 4. The proposed methodology, which is mainly based on these two indices, is proposed in Section 5. In Section 6 two ef<sup>fi</sup>cient probabilistic algorithms are proposed: one to calculate similarity, the other one to calculate the minability index. Then, the viability of the proposed applications is demonstrated in Section 7, showing the results of a test on real data. Finally, Section 8 provides concluding remarks.

## 2. Background and related work

## 2.1. Role engineering

Before introducing the required formalism used to describe role engineering, we <sup>fi</sup>rst review some concepts of the ANSI/INCITS RBAC standard [1] needed for the present analysis. For the sake of simplicity, we do not consider sessions, role hierarchies or separation of duties constraints in this paper. In particular, we are only interested in the following entities:

• PERMS, USERS, and ROLES are the sets of all access permissions, users, and roles, respectively;

$U A \subseteq U S E R S \times R O L E S ,$ is the set of all role–user relationships;

$P A \subseteq P E R M S \times R O L E S ,$ , is the set of all role–permission relationships.

The following functions are also provided:

• ass $\_ u s e r s : R O L E S  2 ^ { U S E R S }$ to identify users assigned to a role. We consider it as derived from UA, that is ass \_users(r)={u∈USERS|〈u, r〉 ∈ UA};

• ass $_ { - p e r m s : R O L E S }  2 ^ { P E R M S }$ to identify permissions assigned to a role. We consider it as derived from PA, that is $a s s \_ p e r m s ( r ) =$ $\{ p \in P E R M S | \langle p , r \rangle \in P A \}$

In addition to RBAC concepts, this paper introduces other entities required to formally describe the proposed approach. In particular, we de<sup>fi</sup>ne:

$U P \subseteq U S E R S \times P E R M S ,$ , the set of the existing user–permission assignments to be analyzed;

$p e r m s : U S E R S  2 ^ { P E R M S } ,$ , the function that identi<sup>fi</sup>es permissions assigned to a user. Given u∈USERS, it is de<sup>fi</sup>ned as $p e r m s ( u ) =$ $\{ p \in P E R M S | \langle u , p \rangle \in U P \}$ ;

• users : $P E R M S  2 ^ { U S E R S }$ , the function that identi<sup>fi</sup>es users that have been granted a given permission. Given $\mathsf { \Pi } _ { p \in P E R M S }$ , it is de<sup>fi</sup>ned as $u s e r s ( p ) = \{ u \in U S E R S | \langle u , p \rangle \in U P \}$

Having introduced these entities, it is now possible to formally de<sup>fi</sup>ne the main objective of role engineering: given UP, PERMS, and USERS, we are interested in determining the best setting for ROLES, PA, and UA that covers all possible combinations of permissions possessed by users. In this context “best” means that the proposed roles should maximize the advantages offered by adopting RBAC, that is, to simplify business governance, to mitigate risk, and to ensure compliance throughout the enterprise. This can be seen as a multiobjective optimization problem [5]. As for the coverage, there is a need that for each $\langle u , p \rangle \in U P$ at least one role $r \in R O L E S$ should exist such that u∈ass \_users(r) and $p { \in } a s s \_ p e r m s ( r )$

Role engineering was <sup>fi</sup>rst illustrated by Coyne [9] through a topdown perspective. Many other authors sought to leverage business information to design roles by adopting a top-down approach such as [19,23,26]. These works represent pure top-down approaches—they do not consider existing access permissions—; hence, they do not take into account how the organization actually works. As for the bottomup approach, Kuhlmann et al. [20] <sup>fi</sup>rst introduced the term “role mining”, trying to apply existing data mining techniques to elicit roles from existing access data. After that, several algorithms explicitly designed for role engineering were proposed [13,14,21,28,30,33]. The main limitation of these works is that they do not always lead to the optimal set of roles from a business perspective. To the best of our knowledge, the work from Colantonio et al. [3] represents the <sup>fi</sup>rst approach that allows for the discovery of roles with business meanings through a role mining algorithm. A cost function is introduced as a metric for evaluating a “good” collections of roles. By minimizing the cost function it is possible to elicit those roles that contextually minimize the overall administration effort and <sup>fi</sup>t the needs of an organization from a business perspective. Further improvements of this approach are represented by [4,5,6,8].

## 2.2. Role mining and graphs

The approach proposed in this paper is based on a formal correspondence between the role mining problem and selected problems from graph theory. Thus, we <sup>fi</sup>rst need to review some graph-related concepts. A graph G is an ordered pair $G = \langle V _ { G } , E _ { G } \rangle$ where $V _ { G }$ is the set of vertices, and $E _ { G }$ is a set of unordered pairs of vertices [12]. We say that v,w∈V are endpoints of the edge $\langle \nu , w \rangle \in E _ { G }$ Given the subset of vertices S $V _ { G } ,$ then the subgraph induced by S is the graph that has S as vertex set, and members of $E _ { G }$ are such that their endpoints are both in S as edge set. A bipartite graph $B = \langle V _ { B } , E _ { B } \rangle$ is a graph where the set of vertex $V _ { B }$ can be partitioned into two subsets $V _ { 1 }$ and $V _ { 2 }$ such that $\forall \langle \nu _ { 1 } , \nu _ { 2 } \rangle \in E _ { B } : \nu _ { 1 } \in V _ { 1 } , \nu _ { 2 } \in V _ { 2 } .$

A clique (of an unipartite graph G) is a subset of vertices S $V _ { G } ,$ , such that the subgraph induced by S is a complete graph, namely for every two vertices in S an edge connecting the two exists. A biclique in a bipartite graph B, also called bipartite clique, is a set of vertices $W _ { 1 } ~ V _ { 1 }$ and $W _ { 2 } \ V _ { 2 }$ such that $\forall w _ { 1 } \in W _ { 1 } , \forall w _ { 2 } \in W _ { 2 } : \langle w _ { 1 } , w _ { 2 } \rangle \in E _ { B } .$ In both the unipartite and bipartite cases, we will say that a set of edges induces a (bi)clique if the subgraph induced by the endpoints of the edges is a (bi)clique. A clique cover of a unipartite graph G is a collection of cliques $S _ { 1 } , . . . , S _ { k } ,$ , such that for each edge $\langle u , v \rangle \in E _ { G }$ there is some $S _ { i }$ that contains both u and v. A clique partition of a graph is a collection of cliques such that each vertex is a member of exactly one of the cliques: it is a partition of the vertices into cliques. Similarly, a biclique cover of a bipartite graph B is a collection of biclique $W _ { 1 } , . . . , W _ { k }$ such that for each edge $\langle \nu _ { 1 } , \nu _ { 2 } \rangle \in E _ { B }$ there is some W that contains both $\nu _ { 1 }$ and $\nu _ { 2 } .$ Thus, each edge of B is covered by at least one biclique.

An access control system con<sup>fi</sup>guration can be represented by a bipartite graph $B { = } \langle U S E R S \cup P E R M S , U P \rangle$ , where two vertices u∈USERS and $\pmb { p } { \in } P E R M S$ are connected by an edge if the user u is granted permission p, namely $\langle u , p \rangle \in U P . \mathrm { ~ A ~ }$ biclique cover of this graph B univocally identi<sup>fi</sup>es a candidate role-set [5], namely a set of roles, and for each role a set of users and permissions, such that all the user– permission assignments belonging to UP can be covered by at least one role. Indeed, every biclique identi<sup>fi</sup>es a role, and the vertices of the biclique identify the users and the permissions assigned to this role [6,13]. Starting from the bipartite graph B set up via the user– permission relations in UP, it is possible to construct an undirected unipartite graph G in the following way: each edge in B (i.e., a user– permission relationship of UP) becomes a vertex in $G ,$ and two vertices in G are connected by an edge if and only if the endpoints of the corresponding edges of B induce a biclique. To ease exposition, we de<sup>fi</sup>ne the function biclique: $U P  2 ^ { U P }$ that indicates all edges in UP which induces a biclique together with the given edge, namely:

$$
b i c l i q u e (\langle u, p \rangle) = \{\langle u ^ {\prime}, p ^ {\prime} \rangle \in U P | \langle u, p ^ {\prime} \rangle , \langle u ^ {\prime}, p \rangle \in U P \wedge \langle u, p \rangle \neq \langle u ^ {\prime}, p ^ {\prime} \rangle \}.\tag{1}
$$

Note that a pair of edges $\pmb { \omega } _ { 1 } = \langle u _ { 1 } , p _ { 1 } \rangle$ and $\pmb { \omega } _ { 2 } = \langle u _ { 2 } , p _ { 2 } \rangle$ of UP that share the same user (that is, $u _ { 1 } = u _ { 2 } )$ or the same permission (that is, $p _ { 1 } = p _ { 2 } )$ induce a biclique. Also, $\langle u _ { 1 } , p _ { 1 } \rangle$ and $\langle u _ { 2 } , p _ { 2 } \rangle$ induce a biclique if another pair $\langle u _ { 1 } , p _ { 2 } \rangle , \langle u _ { 2 } , p _ { 1 } \rangle { \in } U P$ exists. Moreover, given $\omega _ { 1 } , \omega _ { 2 } \in U P ,$ , it can be easily veri<sup>fi</sup>ed that $\omega _ { 1 } \in b i c l i q u e ( \omega _ { 2 } ) \Longleftrightarrow \omega _ { 2 } \in b i c l i q u e ( \omega _ { 1 } )$ and $\omega _ { 1 } \in b i c l i q u e ( \omega _ { 2 } ) \Rightarrow \omega _ { 1 } \neq \omega _ { 2 } .$ Therefore, the undirected unipartite graph G induced from UP can be formally de<sup>fi</sup>ned as:

$$
G = \langle U P, \{\langle \omega_ {1}, \omega_ {2} \rangle \in U P \times U P | \omega_ {1} \in b i c l i q u e (\omega_ {2}) \} \rangle .\tag{2}
$$

Any clique partition of G corresponds to a biclique cover of B as well as to a possible solution for the role mining problem represented by the sets USERS, UA, and PA [6].

## 2.3. Jaccard and clustering coefficients

In this paper we extensively use two mathematical tools. The <sup>fi</sup>rst one is represented by the Jaccard coefficient [18] that is a measure of the similarity between two sets. Given two sets $S _ { 1 } , S _ { 2 } ,$ , the coef<sup>fi</sup>cient is de<sup>fi</sup>ned as the size of the intersection divided by the size of their union:

$$
J _ {S _ {1} S _ {2}} = | S _ {1} \cap S _ {2} | / | S _ {1} \cup S _ {2} |.\tag{3}
$$

The Jaccard coef<sup>fi</sup>cient is widely used in statistic. However, to our knowledge, the only application to RBAC is given by Vaidya et al. [29], that offers a method to consider previously de<sup>fi</sup>ned roles during the role mining process in order to minimize the “perturbation” introduced by new candidate roles. In Section 4.1 we will use the Jaccard index to measure the similarities among users of an access control con<sup>fi</sup>guration.

The other mathematical tool is the clustering coefficient. It was <sup>fi</sup>rst introduced by Watts and Strogatz [31], in order to measure the cliquishness of a typical neighborhood. This coef<sup>fi</sup>cient became one of the central characteristics in complex network theory. In [24,25] the authors show that, in many real networks, the probability of having a relationship between two actors is much greater if the two actors have another mutual acquaintance, or several. An ef<sup>fi</sup>cient clustering coef<sup>fi</sup>cient computation for large scale networks is described in [27].

The coef<sup>fi</sup>cient can be formally de<sup>fi</sup>ned as follows. Let $G = \langle V , E \rangle$ be an undirected graph with a set of nodes V and a set of edges E. We indicate with δ(v) the number of triangles of $\nu ,$ formally:

$$
\delta (v) = | \{\langle u, w \rangle \in E | \langle v, u \rangle \in E \wedge \langle v, w \rangle \in E \} |.\tag{4}
$$

A path of length two for which v is the center node is called a triple of the vertex v. We indicate with $\tau ( \nu )$ the number of triples of v, namely:

$$
\tau (v) = | \{\langle u, w \rangle \in V \times V | \langle v, u \rangle \in E \wedge \langle v, w \rangle \in E \} |.\tag{5}
$$

We now de<sup>fi</sup>ne the clustering coefficient of a graph G as:

$$
C (G) = \frac {1}{| V |} \sum_ {v \in V} c (v),\tag{6}
$$

where

$$
c (v) = \left\{ \begin{array}{l l} \frac {\delta (v)}{\tau (v)}, & \tau (v) \neq 0; \\ 1, & \text { otherwise } \end{array} \right.\tag{7}
$$

quanti<sup>fi</sup>es how close the vertex v and its neighbors are to being a clique. The quantity $c ( \nu )$ is also referred to as the local clustering coef<sup>fi</sup>cient of v, while $C ( G )$ is the average of all local clustering coef<sup>fi</sup>cients, and it is also referred to as the global clustering coef<sup>fi</sup>cient of G. Thus, C(G) can be used to quantify “how well” a whole graph G is partitionable in cliques—in Section 4.2 we will further explain what “well” means in an access control scenario. Note that the provided de<sup>fi</sup>nition differs from the classical de<sup>fi</sup>nition of clustering coef<sup>fi</sup>cient. Indeed, its value is usually set to 0 when there are no triples. Our new de<sup>fi</sup>nition is introduced because it is more suitable for role engineering applications, as will be clari<sup>fi</sup>ed in Section 4.2, by contextualizing the cluster coef<sup>fi</sup>cient usage in the role mining process.

The clustering coef<sup>fi</sup>cient can also be written as:

$$
C (G) = \frac {1}{| V |} \sum_ {v \in V} \sum_ {\pi \in \Pi_ {v}} \frac {X (\pi)}{\tau (v)} + \frac {| \{v \in V | \tau (v) = 0 \} |}{| V |},
$$

where $X { : \Pi _ { v } \to \{ 0 , 1 \} }$ is such that X(π) is equal to 1 if there is an edge between the outer nodes of the triple π, and 0 otherwise. The <sup>fi</sup>rst addendum is the minability of the subset of vertices that have $\tau ( \nu ) \neq 0 ,$ , while the second one corresponds to the minability of the set of vertices such that $\tau ( \nu ) = 0 .$ . Leveraging this de<sup>fi</sup>nition of the clustering coef<sup>fi</sup>cient, $C ( G )$ can be computed by considering each triple of the graph G, and then checking if it is a triangle or not.

## 3. Risk model

To better clarify the bene<sup>fi</sup>ts introduced by the proposed approach, we <sup>fi</sup>rst recall some risk management concepts. In particular, a typical risk management approach is made up of two key components: risk analysis (or assessment) and risk control. During risk analysis we identify potential risks and assess probabilities of negative events together with their consequences. With risk control we establish the tolerable level of risk for the organization, hence providing controls for failure prevention as well as actions to reduce the likelihood of a negative event—such an activity is usually referred to as risk mitigation.

Plugging the previous concepts in a RBAC environment, three essential components should be considered: users, roles, and permissions. Among them, particular attention must be taken on risk incurred by users. Indeed, the main threat in an access control scenario is to allow a user to execute an illegitimate operation over an object or a resource. A system which is only supposed to be used by authorized users must attempt to detect and exclude unauthorized ones. Accesses are therefore usually controlled by insisting on an authentication procedure to determine with some established degree of con<sup>fi</sup>dence the identity of the user, hence granting permissions authorized to that identity. RBAC mitigate the risk of unauthorized accesses by restricting user's permission to prede<sup>fi</sup>ned role de<sup>fi</sup>nitions. In a usual RBAC setting, users are assigned to roles which are then granted permissions to perform prede<sup>fi</sup>ned tasks [15].

In this scenario, and assuming that it is not possible to by-pass the access control mechanism, the risk of illegitimate credentials is prevented by adopting a RBAC system. But, there is an important aspect that has not been considered so far: the role lifecycle. Roles are not static, but they follow the evolution of the organization: new users may join, existing users may leave or may change their job position, applications may be replaced with new ones, etc.. Hence, an important aspect to consider when evaluating the risks related to RBAC systems is the risk introduced by roles that are dif<sup>fi</sup>cult to manage, mainly due to an unclear understanding of their meaning. Indeed, the more a role is intelligible and well designed, the less error prone it will be. A comprehensive risk management approach should consider these aspects starting from the creation of roles, that is the role mining phase. More speci<sup>fi</sup>cally, we focus on the following risk-related aspects of a generic RBAC system:

• Vulnerabilities. They corresponds to roles that are not meaningful enough from the administrator's perspective, namely roles that are dif<sup>fi</sup>cult to manage and to maintain.

• Threats. They are represented by errors and wrong administration actions, unintentionally committed while managing roles during their lifecycle.

• Risks. They correspond to allowing users to execute operations that are not permitted, or hampering their jobs by not granting required permissions. In both cases, the consequences could raise <sup>fi</sup>nancial loss.

To evaluate such risks, in this paper we propose a general risk formula that involves multiple factors with different probabilities, namely:

$$
R i s k = \sum_ {i = 1} ^ {n} P _ {i} \times C _ {i},\tag{8}
$$

where $P _ { i }$ denotes the probability of each risk factor i, and $C _ { i }$ quanti<sup>fi</sup>es the consequences of these risk factors. In our model, risk factors are represented by homogeneous groups of users. Indeed, every user does not have the same degree of importance. For example, there could be users in charge of activities that are critical for the main business of the organization, while other users could be assigned to roles that have a marginal importance for the business. In general, we need to assign various degree of importance to each risk factor by taking the consequence of its execution into consideration. This process requires a thorough analysis of the organization. We assume that the impact evaluation is provided by experts. As for the probability of occurrence, we are able to propose two metrics that are suitable to evaluate the likelihood that an administration error is made when managing roles. In such a way, we evaluate the risk of an error in role management, and subsequently we are able to drive the de<sup>fi</sup>nition of roles that mitigate this risk.

## 4. New metrics for role mining

In this section we describe two indices that can help role engineers to condition role mining in order to craft roles with business meaning and to downsize the problem complexity, hence reducing risk issues as well as required role mining effort. The <sup>fi</sup>rst index is referred to as similarity, and its value is proportional to the number of permissions a given set of users share. The second one is minability, and it measures the complexity of selecting candidate roles given a set of user–permission assignments. Both indices provide a measure of how easy it is to analyze a given set of user–permission assignments through a bottom-up approach, but using different perspectives.

Indeed, roles may be classi<sup>fi</sup>ed in two categories, as described in [10, Ch. 5] and [23]:

• Organizational or structural roles, which depend on employee's position within a homogeneous group of users—for instance, an organization unit or all users that have the same job title. Common permissions are usually assigned to these kinds of roles, and each user typically has only one organizational role.

• Functional roles, which depend on the task that need to be performed in a particular position. Detailed permissions are usually assigned to this kind of roles. Functional roles are supposed to provide further access rights in addition to those being granted by organizational roles. Any number of functional roles can be assigned to a user.

Since the similarity index helps identify situations where all users share the majority of their permissions, its usage is most suitable when evaluating how easy identifying organizational roles is. Instead, the minability index indicates the level of complexity involved in identifying subsets of users that share the same permissions; thus, it is suitable to evaluate whether <sup>fi</sup>nding roles, both functional and organizational, is a simple task or not.

By leveraging the previous observations, it possible to use information resulting from a top-down approach in order to drive a bottom-up analysis. The key idea is to partition the data-set to analyze into smaller subsets according to some business information. For instance, a top-down analysis might identify groups of users that are homogeneous from an enterprise perspective. Then, user–permission assignments can be partitioned such that each subset contains only assignments related to users of the same group. For each subset, we calculate the minability and similarity indices, thus getting a prediction about how complex a subsequent role mining task on the subset will be. This decomposition process can be performed for each available business information, thus generating different data partitions; by selecting the one with the highest index values, we choose the partition that most simpli<sup>fi</sup>es the subsequent role mining analysis. Furthermore, each subset might be iteratively partitioned in even smaller subsets until we reach a given threshold for minability and similarity. The application of role mining algorithms on each subset will produce roles with more business meaning when compared to the outcome of the same algorithms applied on the whole data-set: since subsets are identi<sup>fi</sup>ed according to some business criteria, elicited roles will likely have a business meaning and the probability that administrators select a wrong role to assign to users will decrease, hence reducing the related risk.

In the following, we formally describe the minability and similarity indices, then in Section 5 we will introduce a methodology to apply them in practice within the proposed risk model.

## 4.1. Similarity

In order to introduce the similarity index, we leverage the Jaccard coef<sup>fi</sup>cient de<sup>fi</sup>ned in Section 2.3 In particular, referring to Eq. (3), we provide the following de<sup>fi</sup>nition:

## De<sup>fi</sup>nition 1. (Similarity Between Two Users)

Given two users $u _ { 1 } , u _ { 2 } \in U S E R S ,$ , the similarity index between them is formally de<sup>fi</sup>ned as:

$$
s (u _ {1}, u _ {2}) = \frac {| p e r m s (u _ {1}) \cap p e r m s (u _ {2}) |}{| p e r m s (u _ {1}) \cup p e r m s (u _ {2}) |}.\tag{9}
$$

The following observations are useful for the remainder of the paper:

• u “contains” u if $p e r m s ( u _ { 1 } ) \supset p e r m s ( u _ { 2 } )$ , namely permissions of u are also possessed by $u _ { 2 } ,$ , but are not equal $( p e r m s ( u _ { 1 } ) \ne p e r m s ( u _ { 2 } ) )$ In such a case, $s ( u _ { 1 } , u _ { 2 } ) \in ( 0 , 1 )$

• u is “equivalent” to u if $p e r m s ( u _ { 1 } ) = p e r m s ( u _ { 2 } )$ , namely $u _ { 1 } , u _ { 2 }$ share the same permission set. This condition matches with $s ( u _ { 1 }$ $u _ { 2 } ) = 1$

• u “overlaps” u when perms ${ ( u _ { 1 } ) \cap p e r m s ( u _ { 2 } ) \neq \emptyset }$ but $p e r m s ( u _ { 1 } ) \mathbb { \underline { { \phi } } }$ perms u and perms u Mperms u , namely $u _ { 1 } , u _ { 2 }$ share some <sup>ð Þ ð Þ</sup>permission but neither does $u _ { 1 }$ <sup>ð Þ</sup>contain u nor does u contain $u _ { 1 } .$ This means that $s ( u _ { 1 } , u _ { 2 } ) { \in } ( 0 , 1 )$

• u is “not related” to u i $\mathrm { { } } ^ { \mathrm { { f } } } p e r m s ( u _ { 1 } ) \cap p e r m s ( u _ { 2 } ) = \emptyset ,$ , namely u ,u do not share any common permissions. This corresponds to $s ( u _ { 1 } , u _ { 2 } ) = 0$

## De<sup>fi</sup>nition 2. (Similarity Among a Set of Users)

Given a set of users USERS, the similarity index is the average similarity between all possible (unordered) user pairs. Formally,

$$
S (U S E R S) = \left\{ \begin{array}{l l} \frac {1}{\binom {| U S E R S |} {2}} \sum_ {u _ {1}, u _ {2} \in U S E R S: u _ {1} \neq u _ {2}} s (u _ {1}, u _ {2}), & | U S E R S | > 1; \\ 1, & \text { otherwise }. \end{array} \right.\tag{10}
$$

Notice that Eqs. (9) and (10) can be extended to also consider other enterprise information. For instance, similarities can be evaluated over shared activities, involved organization units, etc.. We can de<sup>fi</sup>ne a similarity index for each kind of business data. In general, the most suitable similarity de<sup>fi</sup>nition depends on speci<sup>fi</sup>c organization needs and role engineering requirements. To ease exposition, in this paper the term “similarity” indicates only the percentage of permissions shared among users, according to the previous de<sup>fi</sup>nitions.

## 4.2. Minability

The minability index measures how complex it is to identify and select the roles required to manage existing user–permission assignments. To do this, we will rede<sup>fi</sup>ne the clustering coef<sup>fi</sup>cient (see Section 2.3) to be used with bipartite graphs that represent the user– permission assignments of an organization. In particular, given a user–permission assignment $\omega \in U P ,$ , we de<sup>fi</sup>ne the function triples: $U P \xrightarrow { } \hat { 2 } ^ { U P \times U P }$ as

$$
\operatorname{triples} (\omega) = \{\langle \omega_ {1}, \omega_ {2} \rangle \in U P \times U P | \omega_ {1}, \omega_ {2} \in b i c l i q u e (\omega) \wedge \omega_ {1} \neq \omega_ {2} \},\tag{11}
$$

namely the set of all possible pairs of elements in UP that both induce a biclique with ω. We also de<sup>fi</sup>ne the function triangles: $U P \to 2 ^ { U P \times U P }$ as

$$
\text { triangles } (\omega) = \{\langle \omega_ {1}, \omega_ {2} \rangle \in \text { triples } (\omega)   |   \omega_ {1} \in \text { biclique } (\omega_ {2}) \},\tag{12}
$$

namely the set of all possible pairs of elements in UP that both induce a biclique with ω, and that also induce a biclique with each other

## De<sup>fi</sup>nition 3. (Minability)

The minability index of an access control system con<sup>fi</sup>guration represented by the set UP is de<sup>fi</sup>ned as

$$
M (U P) = \frac {1}{| U P |} \sum_ {\omega \in U P} m (\omega),\tag{13}
$$

where

$$
m (\omega) = \left\{ \begin{array}{l l} \frac {| t r i a n g l e s (\omega) |}{| t r i p l e s (\omega) |}, & t r i p l e s (\omega) \neq \varnothing ; \\ 1, & \text { otherwise }. \end{array} \right.\tag{14}
$$

The value of m(ω) is also referred to as the local minability index of ω, and it quanti<sup>fi</sup>es how close ω, together with all the edges which induce a biclique with it, are to being a biclique. Hence $M ( U P )$ , also referred to as the global minability index of UP, quanti<sup>fi</sup>es how well the bipartite graph, induced by the user–permission relations UP, is coverable with distinct bicliques. In other words, how easily a candidate role-set for the analyzed data can be identi<sup>fi</sup>ed—see below for a de<sup>fi</sup>nition of “easy”. Notice that, according to Eq. (14), when a user–permission assignment does not induce biclique with any other assignment, or it induces biclique with just one other assignment, its local minability is conventionally set to 1. This case is identi<sup>fi</sup>ed by $| t r i p l e s ( \mathbf { \omega } \mathbf { { \omega } } ) | = 0$ . Note that when $t r i p l e s ( \omega ) = 0 ,$ , the assignment ω induces a biclique with at most another user– permission assignment. Thus, the identi<sup>fi</sup>cation and selection of the unique role to manage ω is trivial.

Eq. (13) can be alternatively written as

$$
M (U P) = \frac {1}{| U P |} \sum_ {\omega \in U P} \sum_ {\langle \omega_ {1}, \omega_ {2} \rangle \in t r i p l e s (\omega)} \frac {Y (\omega , \omega_ {1} , \omega_ {2})}{| t r i p l e s (\omega) |} + \frac {| \{\omega \in U P | t r i p l e s (\omega) = \emptyset \} |}{| U P |},\tag{15}
$$

where $Y { : } U P { \times } U P { \times } U P {  } \{ 0 { , } 1 \}$ returns 1 if their parameters induce a biclique, and 0 otherwise. Formally:

$$
Y (\omega , \omega_ {1}, \omega_ {2}) = \left\{ \begin{array}{l l} 1, & \langle \omega_ {1}, \omega_ {2} \rangle \in t r i a n g l e s (\omega); \\ 0, & \text { otherwise }. \end{array} \right.
$$

With the above formulation, the minability index M(UP) can be computed by considering each tuple $\langle \omega , \omega _ { 1 } , \omega _ { 2 } \rangle \in U P \times U P \times U P$ such that $\omega _ { 1 } , \omega _ { 2 } \in b i c l i q u e ( \omega )$ , and checking whether the condition $\omega _ { 1 } \in$ biclique (ω<sub>2</sub>) holds true.

The following lemma de<sup>fi</sup>nes a mapping between the clustering coef<sup>fi</sup>cient, as de<sup>fi</sup>ned in Eq. (6), and the minability index:

Lemma 1. If G is the unipartite graph constructed from UP according to Eq. (2), then $M ( U P ) = C ( G )$ , that is the minability of UP is equal to the clustering coef<sup>fi</sup>cient of G.

Proof. It follows by construction of the graph G in Eq. (2), and de<sup>fi</sup>nitions of M(UP) in Eq. (13) and C(G) in Eq. (6). □

Lemma 1 will be used in Sections 4.3 and 5.3 to offer a graph representation for the given examples. A relevant observation relates similarity with minability, and it is represented by the following lemma:

Lemma 2. Given a set of users USERS that have been granted permissions in PERMS through the corresponding assignments UP, then $S ( U S E R S ) = 1 \Rightarrow M ( U P ) = 1$

Proof. When S(USERS)=1 and USERS = 1, there is only one user <sup>j j</sup>that possesses all the permissions in PERMS. If $S ( U S E R S ) = 1$ and $| U S E R S | > 1$ , then all users share the same permission set, $\mathrm { n a m e l y } \forall u _ { 1 } ,$ $u _ { 2 } { \in } U S E R S ; p e r m s ( u _ { 1 } ) { = } p e r m s ( u _ { 2 } )$ . In both cases, $U P = U S E R S \times P E R M s$ S. According to Eqs. (11) and (1 $2 ) , \forall \omega \in U P : t r i p l e s ( \omega ) = t r i a n g l e s ( \omega )$ The proof immediately follows from the minability de<sup>fi</sup>nition (Eq. (13)). □

The previous lemma states that the similarity index is tighter than the minability index. Indeed, a similarity index equal to 1 requires that all users share the same set of permissions, whereas minability can be equal to 1 even if the users do not share all the same permissions. Further, notice that the inverse of Lemma 2 does not hold. The example depicted in Fig. 1(a) is one possible case of $M ( U P ) = 1$ and S (USERS)b1. In the following section we will offer more details on this example.

In the remainder of this section we introduce de<sup>fi</sup>nitions and prove theorems that help to better understand the relationship between the minability index and the complexity of the role mining problem. In particular, the following de<sup>fi</sup>nition is required to formalize all the subsequent considerations:

De<sup>fi</sup>nition 4. (Maximal Equivalent Roles (MERs))

Given a role $\overline { { r } } \in R O L E S ,$ it is a maximal equivalent role (MER) if:

$$
\nexists U \subseteq \text { USERS }, \nexists P \subseteq \text { PERMS }: U \times P \subseteq U P \wedge \text { ass\_users } (\bar {r}) \times \text { ass\_perms } (\bar {r}) \subset U \times P.\tag{16}
$$

Informally, a MER is a role that is “representative” of all possible subsets of permissions shared by a given set of users [4]. The key observation which is made regarding a MER is that two permissions which always occur together among users should simultaneously belong to the same candidate roles. Without further business semantics of access control data, a bottom-up approach to role engineering cannot differentiate between a role made up of two permissions and two roles that contain individual permissions. Moreover, de<sup>fi</sup>ning roles made up of as many permissions as possible likely minimizes the administration effort of the RBAC system by reducing the number of required role–user assignments. MERs properties are further detailed in [4], which also proposes a variant of the Apriori algorithm to ef<sup>fi</sup>ciently identify all possible MERs within UP.

![](/api/attachments/HAFFY2HV/fulltext/images/f142432f1b099c329b3032d0a69f80d858e8928b8b131e3d1f2c30c6fa5f6a09.jpg)  
Fig. 1. Access control con<sup>fi</sup>gurations as bipartite graphs and corresponding unipartite graphs.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- $m(\omega) = 1 \Longleftrightarrow |MERS_{\omega}| = 1$;
- $m(\omega) = 0 \Longleftrightarrow |MERS_{\omega}| = |biclique(\omega)|$;
- $m(\omega) \in (0, 1) \Longleftrightarrow 1 &lt; |MERS_{\omega}| &lt; |biclique(\omega)|$.
</div>

The following theorem relates the minability index to the complexity of the role mining problem in terms of number of MERs:

Theorem 1. Let ROLES be the set of all possible MERs that can be derived from UP. Given a user–permission assignment $\omega \in U P ,$ let $M E R S _ { \omega }$ be the set of all possible MERs that “cover” the given user– permission assignment, namely $M E R S _ { \omega } = \{ r \in R O L E S$ risaMER∧ω∈ $a s s _ { u } s e r s ( \overline { { r } } ) \times a s s _ { p } e r m s ( \overline { { r } } ) \}$ <sup>f j</sup>. Then, the followings holds:

Proof. First, we analyze the case m $( \omega ) = 1 .$ . Let r be a role made up of the users and permissions involved by the assignments ω and biclique (ω), formally assXusers $\overline { { r } } ) = \{ u { \in } U S E R S | \exists p { \in } P E R M S , \langle u , p \rangle \in$ biclique $( \mathbf { \omega } _ { \mathbf { \omega } } ) \cup \{ \mathbf { \omega } _ { \mathbf { \omega } } \} \}$ <sup>ð</sup>and assXperms $\bar { r } ) = \{ p { \in } P E R M S | \exists u { \in } U S E R S , \langle u , p \rangle { \in }$ biclique <sup>ð Þ f gg ð Þ f j</sup>ω ∪ ω . We now demonstrate that r is a MER. Indeed, according to <sup>ð Þ f</sup>Eq. (1), $\forall \langle u _ { 1 } , p _ { 1 } \rangle , \langle u _ { 2 } , p _ { 2 } \rangle \in b i c l i q u e ( \omega ) \cup \{ \omega \} \Rightarrow \exists \langle u _ { 1 } , p _ { 2 } \rangle , \langle u _ { 2 } , p _ { 1 } \rangle \in U P ,$ namely both users $\iota _ { 1 } , u _ { 2 }$ have permission ${ p } _ { 1 } , { p } _ { 2 }$ been granted. According to Eq. (14), $m ( \omega ) = 1 \Rightarrow t r i p l e s ( \omega ) = t r i a n g l e s ( \omega )$ , thus the previous consideration holds for every possible pair of user–permission relationships in $b i c l i q u e ( \omega ) \cup \{ \omega \}$ . This means that biclique $( { \bf { \omega } } ) \cup \{ { \bf { \omega } } { \bf { \omega } } ^ { } =$ <sup>ð Þ f g</sup>assXusers r × assXperms r . Seeking a contradiction, if r were not a <sup>ð Þ</sup>MER, two sets $U \subseteq U S E R S$ <sup>Þ</sup>and $P \subseteq P E R M S$ would exist such that assXusers r × assXperms ${ \overline { { r } } } ) { \subset } U \times P { \subseteq } U P$ (see Eq. (16)). Let $\omega = \langle \boldsymbol { u } ,$ <sup>ð Þ</sup>p〉. Yet, for each 〈u $, p ^ { \prime } \rangle { \in } ( U \times P ) $ 5 assXusers r × assXperms r it can <sup>ð Þ ð</sup>be easily shown that both the assignments $\langle u , p ^ { \prime } \rangle , \langle u ^ { \prime } , p \rangle$ <sup>ð ÞÞ</sup>always exists in $U { \times } P .$ Hence, according to Eq. (1), $\langle u ^ { \prime } , p ^ { \prime } \rangle \in b i c l i q u e ( \omega )$ ), meaning that U × P 5 assXusers $\overline { { r } } ) \times a s s \_ p e r m s ( \overline { { r } } ) ) = \emptyset$ . Therefore, r is a MER. <sup>ð Þ ð ð Þ ð ÞÞ</sup>We now demonstrate that another MER that contains ω cannot exist. Indeed, if ${ \overline { { r } } } ^ { \prime }$ is a MER that contains ω (i.e., $\bullet \bullet \bullet s \underline { { { u s e r s ( \bar { r } ^ { \prime } ) } } } \times$ assX $\boldsymbol { p e r m s } ( \overline { { \boldsymbol { r } } } ^ { \prime } ) )$ , for all ω<sup>′</sup>∈assXusers $( \overline { r } ^ { \prime } ) \times$ × assXperms $( \overline { r } ^ { \prime } )$ <sup>ð Þ</sup>ω it can be shown that ω<sup>′</sup>∈biclique(ω). Hence, ${ \overline { { r } } } = { \overline { { r } } } ^ { \prime }$ . Finally, having only one MER that contains ω implies that $m ( \omega ) = 1$ . Let r be such a MER. Since it is the only MER, for each pair ${ \mathfrak { o } } _ { 1 } , { \mathfrak { o } } _ { 2 } \in$ assXusers r × assXperms r such that $\omega _ { 1 } \neq \omega _ { 2 }$ we have $\omega _ { 1 } \omega _ { 1 } = b i c l i q u e ( \omega _ { 2 } )$ <sup>ð Þ ð Þ</sup>. Thus, triples(ω) = triangles (ω), which corresponds to state that $m ( \omega ) = 1$ □

When m(ω)=0, we now demonstrate that it is possible to identify biclique ω distinct MERs made up of ω combined with each element <sup>j jð Þ</sup>of biclique(ω). Let $\omega = \langle u , p \rangle$ . First, observe that such roles are distinct since $m ( \omega ) = 0 \Rightarrow$ triangles(ω)= . We want to show that for each $\langle u _ { i } , p _ { i } \rangle { } \in { } b i c l i q u e ( \langle u , p \rangle { } )$ , the role $\overline { { r } } _ { i }$ such that $a s s _ { u } s e r s ( \overline { { r } } _ { i } ) = \{ u , u _ { i } \}$ and ass<sub>p</sub>erms $\overline { { r } } _ { i } ) = \{ p , p _ { i } \}$ <sup>ð Þ f</sup>is a MER. Seeking a contradiction, if $r _ { i }$ <sup>ð Þ f g</sup>were not a MER, two sets U USERS and P PERMS would exist such that $\{ u , u _ { i } \} \times \{ p , p _ { i } \} \subset U \times P \subset U P$ (see Eq. (16)). Let $\langle u ^ { \prime } , p ^ { \prime } \rangle \in ( U \times P ) \backslash ( \{ u ,$ $u _ { i } \} \times \{ p , p _ { i } \} )$ . It can be easily shown that $\langle u ^ { \prime } , p ^ { \prime } \rangle { \in } b i c l i q u e ( \langle u _ { i } , p _ { i } \rangle )$ thus $t r i a n g l e s ( \omega ) \neq \emptyset$ . But, according to Eq. (14), this means that m $( \omega ) { > } 0$ , which is a contradiction. Moreover, more than biclique ω <sup>j jð Þ</sup>distinct MERs that contain ω cannot exist. Indeed, let n ℕ : n N biclique ω be the number of the distinct MERs that contain $\omega .$ <sup>j</sup>Let $r _ { i }$ <sup>jð Þ</sup>indicate the ith MER, and let $\mathbf { \omega } _ { \omega _ { i } \in }$ assXusers $\overline { { \boldsymbol { r } } } _ { i } ) \times$ assXperms $\left( \overline { { r } } _ { i } \right) ) \left\{ \mathbf { \omega } \in \right\}$ . Thus, $\forall i \in 1 \ldots n : \omega _ { i } \in b i c l i q u e ( \omega )$ <sup>ð Þ</sup>, contradicting the in-<sup>ð ÞÞ f g</sup>equality biclique(ω)bn. We now prove that having biclique ω MERs implies that $m ( \omega ) = 0$ . Let $r _ { i }$ indicate the ith MER, and let $\mathbf { \omega } _ { \mathbf { 0 } i } { \in } ( a s s \mathbf { \omega } _ { \mathbf { - } { u s e r s } ( \overline { { r } } } \mathbf { \omega } _ { i } ) \times a s s$ Xperms $\overline { { r } } _ { i } ) ) \left\{ \mathbf { 6 } \mathbf { ) } \right\}$ . Since the roles are distinct, $\forall i , j { \in } 1 . . . | b i c l i q u e { ( \mathbf { \boldsymbol { \omega } } ) } |$ <sup>ð ÞÞ f g</sup>: i≠j we have that ω ∉biclique ω . Thus, trian-$g l e s ( \omega ) = \emptyset$ <sup>jð Þ</sup>and, according to Eq. $( 1 4 ) , m ( \omega ) = 0 .$

Finally, by excluding the previous two cases we merely have that $m ( \omega ) { \in } ( 0 , 1 ) { \iff } 1 { < } | M E R S _ { \omega } | { < } | b i c l i q u e ( \omega ) |$

The previous theorem allows us to make some consideration on the complexity of the role mining problem. Given a user–permission assignment ω, the higher its local minability is, the less the number of possible MERs to analyze is. The following subsection and Section 7 offer practical examples about this property.

## 4.3. Examples

We now show some examples which demonstrate how minability and similarity indices can actually provide role mining engineers with the expected complexity to <sup>fi</sup>nd functional and/or organizational roles. In Fig. 1, three different and simple access control con<sup>fi</sup>gurations are depicted. In each one, we have 4 users and 6 permissions, but with different user–permission assignments.

To better illustrate these indices, we also report the corresponding unipartite graphs constructed according to Eq. (2).

In Fig. 1(a) the minability index is 1. In this case, it is straightforward to verify that a clique cover of the unipartite graph is represented by $C _ { 1 } = \{ \langle A , 1 \rangle , \langle A , 2 \rangle \langle A , 3 \rangle , \langle B , 1 \rangle , \langle B , 2 \rangle , \langle B , 3 \rangle \}$ } and $C _ { 2 } = \{ \langle C , 4 \rangle , \langle C , 5 \rangle , \langle C , 6 \rangle$ $\langle D , 4 \rangle , \langle D , 5 \rangle , \langle D , 6 \rangle \}$ . In RBAC terms, $C _ { 1 }$ and $C _ { 2 }$ correspond to two maximal equivalent roles: the <sup>fi</sup>rst one made up of permissions {1,2,3} and it is assigned with users {A,B}, the second one made up of permissions $\{ 4 , 5 , 6 \}$ and assigned with users {C,D}. As for the similarity index, S({A,B, ${ \mathrm { C } } , { \mathrm { D } } \} ) = 1 / 3$

Fig. 1(b) shows another access control con<sup>fi</sup>guration, where the minability index is equal to 0. According to Th. 1, it represents the most ambiguous case. Indeed, in this example we have two possible MERs to manage each user–permission assignment (one is composed by one user and two permissions, the other one is made up of one permission and two users). Yet, without further business semantics of access control data, it is not clear which is the best choice. Another observation is that in Fig. 1(b) the similarity index is smaller than in Fig. 1(a). Indeed, since each permission is used by 2 users, it is impossible to de<sup>fi</sup>ne a role that has to be assigned to the majority of users.

Fig. 1(c) shows a slightly more complicated con<sup>fi</sup>guration, where the minability index is between 0 and 1, while the similarity is higher than in all previous cases. It is quite clear that the unipartite graph can be covered with two cliques (i.e., two MERs), and this suggests that the minability must be very close to 1. Indeed, we have an ambiguity only for the user–permission assignment D; 1: it can belong to both the cliques $C _ { 1 } = \{ \langle A , 1 \rangle , \ \langle B , 1 \rangle , \ \langle C , 1 \rangle , \ \langle D , 1 \rangle \}$ and $C _ { 2 } = \{ \langle D , 1 \rangle , \ \langle D , 2 \rangle$ $\langle D , 3 \rangle , \langle D , 4 \rangle , \langle D , 5 \rangle , \langle D , 6 \rangle \} . M ( U P ) = 0 . 9 4$ is in line with the previous observation.

## 5. Applications of minability and similarity

As shown in the previous section, minability and similarity are estimates of the expected complexity to select roles within the role mining results. As a consequence, they are also metrics for the likelihood of making administration errors when managing roles throughout their lifecycle. For instance, given a group of users, when the minability index equals 1 for user–permission assignments involved in the group, according to Th. 1 there will be just one possible maximal equivalent role for managing those assignments. This means, for example, that new permissions introduced within the system will likely be assigned to all users of the group (via the single role) or to none of them, and new users that join such a group will likely be granted the same permissions of other users (namely, all the permissions contained within the single role). Moreover, the business meaning of the role is strictly related to business aspects that users within the group have in common. Therefore, the probability of making wrong access control decisions is low.

One possible application of the minability and similarity indices is to help data analysts guide a divide-and-conquer approach to role mining. Decomposing the role mining problem into smaller subproblems is a best practice, especially when dealing with large datasets. Typical steps of a generic role mining process are [20]:

1. Choice of information sources. From the available data, a subset has to be selected which is most promising to yield suitable information for role creation.

2. Data preparation. The data is collected from the various locations, cleaned up from obvious or known as incorrect information, and transformed into a format in which it can then be processed by the data mining software.

3. Exploration. This phase is crucial for the whole role mining process. It will provide a “feeling” for the data contents and the expected role scheme. The results of this phase are suitable attribute sets for the unique representation of organizational and functional roles and suitable parameters for the role mining algorithms.

4. Mining. The role mining algorithm is performed.

5. Role creation. The outcome of the data mining run are used to derive candidate organizational and functional roles.

6. Check, approval and implementation of resulting roles. The resulting roles have to be checked for plausibility and correctness.

7. User assignment. The elicited roles are <sup>fi</sup>nally assigned to users.

In this scenario, leveraging minability and similarity allows for the identi<sup>fi</sup>cation of the business information that “best <sup>fi</sup>ts” with the access control data, namely the information that induces a decomposition which most simpli<sup>fi</sup>es the identi<sup>fi</sup>cation of a business meaning for roles elicited in the role mining phase. Both indices can be calculated in the exploration step and used to guide the subsequent role mining steps.

The reason why minability and similarity change after decomposing the problem can be analyzed in terms of the graph model described in Section 2.2. As a matter of fact, partitioning the set UP is equivalent to partitioning the unipartite graph G constructed according to Eq. (2) in subgraphs, since each element in UP corresponds to a node in G. Hence, partitioning UP means discarding all the relationships between user–permission assignments that are in two different subsets of the partition—they will no longer induce a biclique—, namely removing edges in G that connect distinct subgraphs. In other words, the partition “breaks” roles that spread across multiple subsets into more parts; that is, roles without a clear meaning according to the business information that induced the partition. However, an important problem arises: how to be sure that the roles selected to be broken down are less relevant from a business perspective. The following section explains how minability and similarity indices can practically be used in conjunction with a divide-and-conquer approach to role mining to elicit business roles and to mitigate enterprise risk.

## 5.1. Choosing the best decomposition

When we have several business information at our disposal (e.g., organization units, job titles, applications, etc.), we have to select the one that induces a partition for UP, which minimizes the risk for each subset and that simpli<sup>fi</sup>es the subsequent mining steps. The best partition can change depending on the organization needs. To guide the decomposition process, it is useful to have a metric that allows data analysts:

• To decide what business information most reduces the risk of a poor role de<sup>fi</sup>nition and simpli<sup>fi</sup>es the subsequent mining steps.

• To predict whether splitting the problem into more sub-problems actually reduces the risk of having ill-de<sup>fi</sup>ned roles. In particular, we can decide to iteratively decompose the data before executing the mining step, by applying a different decomposition at each iteration until given minability and similarity thresholds are reached for each subset.

• To verify that partitioning does not actually reduce the role mining complexity. If this is the case, access control information should thus be reviewed in order to improve their manageability.

In all previous cases, similarity and minability are a means to estimate the risk related to the data being analyzed. In fact, since both indices express the likelihood of making bad administration decisions due to the unclear meaning of roles, they can be used in conjunction with the risk formula (Eq. (8)) proposed in Section 3. Depending on the kind of roles that role engineers are looking for (organizational or functional), the similarity or the minability value can be combined with the importance of each subset to evaluate the risk of incurring a poor role design. In particular, the following indicators can support the partition selection problem:

## De<sup>fi</sup>nition 5. (Similarity-Based Risk)

Let USERS be a set of users to analyze, and PERMS,UP be the corresponding permissions and assignments. The similarity-based risk of USERS is de<sup>fi</sup>ned as:

$$
\operatorname{Risk} _ {S} (\text { USERS }) = (1 - S (\text { USERS })) \times C,\tag{17}
$$

where C is the importance of the user group USERS, while S(USERS) is the similarity value computed over the users belonging to USERS.

## De<sup>fi</sup>nition 6. (Minability-Based Risk)

Let UP be a set of user–permission assignments between users in USERS and permissions in PERMS. The minability-based risk of UP is de<sup>fi</sup>ned as:

$$
R i s k _ {M} (U P) = (1 - M (U P)) \times C,\tag{18}
$$

where C is the importance of the data represented by the assignment set UP, while M(UP) is the similarity value computed over the user– permission assignments belonging to UP.

The previous de<sup>fi</sup>nitions offer an estimate for the risk related to each subset. However, if the objective is to identify the best partition, we will compare the values obtained for similarity-based and/or minability-based risks on all subsets and choose the partition with the lowest “average” risk. Similarly, when we want to check if further decomposing the problem actually reduces the role mining complexity, we have to compare the “average” risk that we have with and without the decomposition. The following section shows a possible approach to summarize the risk related to a partition.

## 5.2. Conditioned indices

Instead of analyzing the risk values calculated on each subset of a given partition, in most case it is more advantageous to have a risk value that “summarizes” the simpli<sup>fi</sup>cation introduced by the partition. To this aim, we need to review all the abovementioned indices to condition them by the given partition. The conditioning concept will apply on both similarity and minability indices (we therefore speak of conditioned similarity and minability) and risk evaluation metrics (we therefore speak of conditioned similarity- or minability-based risk).

## 5.2.1. Conditioned similarity and similarity-based risk

Let $\boldsymbol { \Omega } = \{ \Omega _ { 1 } , . . . , \Omega _ { k } \}$ be a k-partition of UP such that $\Omega _ { i } \subseteq U P$ and $U P = \textstyle \bigcup _ { i = 1 } ^ { k } \widehat { \Omega _ { i } }$ . Each subset $\Omega _ { i }$ induces a set of users $\Upsilon _ { i ^ { \prime } }$ such that $\Upsilon _ { i } =$ $\{ u \in { U S E R S } | \exists p \in { P E R M S } , \langle u , p \rangle \in \Omega _ { i } \}$ . According to Eq. (10), we can de<sup>fi</sup>ne the similarity of $\Upsilon _ { i }$ in the following way:

$$
S (\Upsilon_ {i}) = \left\{ \begin{array}{l l} \frac {1}{\binom {| \Upsilon_ {i} |} {2}} \sum_ {u _ {1}, u _ {2} \in \Upsilon_ {i}: u _ {1} \neq u _ {2}} s _ {\Omega_ {i}} (u _ {1}, u _ {2}), | U | > 1; \\ 1, & \text { otherwise }. \end{array} \right.\tag{19}
$$

where $S _ { \Omega } ( u _ { 1 } , u _ { 2 } )$ is the similarity of the users $u _ { 1 }$ and $u _ { 2 }$ obtained by only considering the permissions that are involved in $\Omega _ { i } .$ Eq. (19) can also be rewritten in the following way:

$$
S(\Upsilon_{i}) = \frac{1}{\sigma_{i} + \binom{|\Upsilon_{i}|}{2}}\left(\sigma i + \sum_{\substack{u_{1},  u_{2}\in \Upsilon_{i}:\\ u_{1}\neq u_{2}}}s_{\Omega i}(u_{1},u_{2})\right),
$$

where

$$
\sigma_ {i} = \left\{ \begin{array}{l l} 1, & | \Upsilon_ {i} | = 1; \\ 0, & \text { otherwise }. \end{array} \right.
$$

We can then offer the following de<sup>fi</sup>nition:

De<sup>fi</sup>ntion 7. (Conditioned Similarity).

Given a partition $\Omega = \{ \Omega _ { 1 } , . . . , \Omega _ { k } \}$ for UP such that $\textstyle U P = \bigcup _ { i = 1 } ^ { k } \Omega$ <sub>i</sub> and the induced sets of users $\Upsilon _ { i } = \{ u \in U S E R S | \exists p \in P E R M S , \langle u , p \rangle \in \Omega _ { i } \}$ , we de<sup>fi</sup>ne the similarity index conditioned by Ω as

$$
S _ {\Omega} (U S E R S) = \frac {\sum_ {i = 1} ^ {k} S (\Upsilon_ {i}) \left(\sigma_ {i} + \binom {| \Upsilon_ {i} |} {2}\right)}{\sum_ {i = 1} ^ {k} \left(\sigma_ {i} + \binom {| \Upsilon_ {i} |} {2}\right)} = \frac {\sum_ {i = 1} ^ {k} \sigma_ {i} + \sum_ {i = 1} ^ {k} S (\Upsilon_ {i}) \binom {| \Upsilon_ {i} |} {2}}{\sum_ {i = 1} ^ {k} \sigma_ {i} + \sum_ {i = 1} ^ {k} \binom {| \Upsilon_ {i} |} {2}}\tag{20}
$$

Notice that Eq. (20) holds since $S ( \mathcal { T } _ { i } ) = 1$ when $\sigma _ { i } = 1$ . Another important observation is that the conditioned index $\left( \operatorname { E q . } \left( 2 0 \right) \right)$ is a sort of “modi<sup>fi</sup>ed” version of Eq. (10), where the pairs of users that belong to different subsets are discarded.

As for risk analysis, Def. 7 can be extended in order to take into account the importance of each subset. In particular, we provide the following de<sup>fi</sup>nition:

De<sup>fi</sup>nition 8. (Conditioned Similarity-Based Risk)

Given a k-partition $\Omega = \{ \Omega _ { 1 } , . . . , \Omega _ { k } \}$ of UP and the induced sets of users $\Upsilon _ { i } = \{ u \in U S E R S | \exists p \in P E R M S , \langle u , p \rangle \in \Omega _ { i } \}$ , we de<sup>fi</sup>ne the similarity-based risk conditioned by Ω as

$$
R i s k _ {S _ {\Omega}} (U S E R S, \Omega) = \frac {\sum_ {i = 1} ^ {k} (1 - S (\Upsilon_ {i})) C _ {i} \bigg (\sigma_ {i} + \binom {| \Upsilon_ {i} |} {2} \bigg)}{\sum_ {i = 1} ^ {k} \bigg (\sigma_ {i} + \binom {| \Upsilon_ {i} |} {2} \bigg)},\tag{21}
$$

where $C _ { i }$ is the importance of the user group $\Upsilon _ { i } .$

In particular, $R i s k _ { S _ { \Omega } } ( U S E R S , \Omega )$ is a weighted average of the risks related to each subset, where the weights are proportional to the subset cardinalities.

## 5.2.2. Conditioned minability and minability-based risk

Given a k-partition $\Omega = \{ \Omega _ { 1 } , . . . , \Omega _ { k } \}$ of UP, according to Eq. (13) the minability index of each subset $\Omega _ { i }$ is

$$
M (\Omega_ {i}) = \frac {1}{| \Omega_ {i} |} \sum_ {\omega \in \Omega_ {i} m _ {\Omega_ {i}} (\omega),}
$$

where $m _ { \Omega _ { i } } ( \omega )$ indicates the local minability of ω obtained considering only the user–permission assignments belonging to $\Omega _ { i \cdot }$ This leads to the following de<sup>fi</sup>nition:

De<sup>fi</sup>nition 9. (Conditioned Minability)

Given a k-partition $\Omega = \{ \Omega _ { 1 } , . . . , \Omega _ { k } \}$ of UP the minability index conditioned by Ω is

$$
M _ {\Omega} (U P) = \frac {\sum_ {i = 1} ^ {k} M (\Omega_ {i}) | \Omega_ {i} |}{\sum_ {i = 1} ^ {k} | \Omega_ {i} |} = \frac {1}{| U P |} \sum_ {i = 1} ^ {k} \sum_ {\omega \in \Omega_ {i}} m _ {\Omega_ {i}} (\omega) = \frac {1}{| U P |} \sum_ {\omega \in U P} m _ {\Omega_ {i}} (\omega).\tag{22}
$$

It is possible to note that the conditioned index $\left( \operatorname { E q . } \left( 2 2 \right) \right)$ is similar to the basic minability index (Eq. (13)), except that relationships between user–permission assignments that belong to different subsets are no longer considered.

As for risk analysis, Def. 9 can be extended in order to take into account the importance of each subset. In particular, we provide the following de<sup>fi</sup>nition:

## De<sup>fi</sup>nition 10. (Conditioned Minability-Based Risk)

Given a k-partition $\Omega = \{ \Omega _ { 1 } , . . . , \Omega _ { k } \}$ of the set $U P$ we de<sup>fi</sup>ne the minability-based risk conditioned by Ω as

$$
R i s k _ {M _ {\Omega}} (U P, \Omega) = \frac {\sum_ {i = 1} ^ {k} (1 - M (\Omega_ {i})) C _ {i} | \Omega_ {i} |}{\sum_ {i = 1} ^ {k} | \Omega_ {i} |},\tag{23}
$$

where $C _ { i }$ is the importance of the subset $\Omega _ { i } .$

In particular, $R i s k _ { M _ { \Omega } } ( U P , \Omega )$ is a weighted average of the risks related to each subset, where the weights are represented by the subset cardinalities

## 5.3. Examples

In this subsection we show a simple application of our indices. Let us assume that the access control con<sup>fi</sup>guration to analyze is the one depicted in Fig. $2 ( \mathsf { a } ) .$ . The unipartite graph corresponding to the analyzed access control con<sup>fi</sup>guration is shown in Fig. 2(b). The values of the indices are reported in the caption. We now try to split the problem into several sub-problems by leveraging some available business information in order to check whether the minability and similarity values increase, and consequently the risk indices decrease. For this purpose, suppose that we have two different business information at our disposal: the organization unit the user belongs to, and the applications involved by the given permission set. This information is depicted in Fig. 2(a). In particular, the organization unit $\mathrm { U } _ { 1 }$ is composed of the users A, B, and $\complement ,$ while the organization units $\mathrm { U } _ { 2 }$ and $\mathrm { { U } } _ { 3 }$ are composed of the users D and E, respectively. As for the applications, $\mathsf { A } _ { \mathrm { x } }$ is composed of the permissions 1,2,3, and $4 ; \mathrm { A _ { y } }$ is composed of the permissions 5 and $6 ;$ while $\mathsf { A } _ { \mathrm { z } }$ is made up of permissions 7,8, and 9.

Given these pieces of information, we have to choose which one induces the partition that most simpli<sup>fi</sup>es the successive role mining steps. To ease exposition, we assume that all the subsets have the same importance. Fig. $2 ( \mathsfit { c } )$ shows the subsets generated by partitioning according to the organization units. Notice that both minability and similarity indices are equal to 1 for each subset, whereas the risk values are 0. Hence, the conditioned basic and risk indices equal 1 and $^ { 0 , }$ respectively. Fig. 2(d) shows the subsets generated by partitioning according to applications and the corresponding minability and similarity values for each subset. When comparing the conditioned indices of the two partitions, it can be easily seen that the

(a) Access configuration

![](/api/attachments/HAFFY2HV/fulltext/images/f3c95250bbc0eb5ac5ea72766940ba1dcf1b5920d82cdef976c854c42f8ed1b7.jpg)

(c) Partitioning by user attributes

![](/api/attachments/HAFFY2HV/fulltext/images/1d89d112560e0e76627dcf24d474eca9d7ef15253c3e340e0d1408e20a8698dc.jpg)  
(d)Partitioning by permission attributes

![](/api/attachments/HAFFY2HV/fulltext/images/a75a9150d5bea5bb0bfdf670bf8f01015ae2d13a64bc5aacd8ae7ac99c36c597.jpg)  
Fig. 2. A partitioning example.

organization-unit based partition is preferable to the applicationsbased partition. Indeed, the minability conditioned by applications is 0.88, which is even worse than the not-conditioned minability. Partitioning by organization units is also preferable when evaluating other conditioned indices.

## 6. Fast index approximation

In this section, we illustrate two algorithms to ef<sup>fi</sup>ciently compute the similarity and minability indices introduced in Sections 4.1 and 4.2.

## 6.1. Approximating the similarity

Let us analyze the computation time required to determine the exact value of S(USERS). In particular, according to its de<sup>fi</sup>nition $( \operatorname { E q . }$ (10)), this value can be calculated in $\mathcal { O } \Big ( \vert \breve { P E R M S } \vert \vert U S E R S \vert ^ { 2 } \Big )$ time. Indeed, $\mathcal { O } \left( \left| U S E R S \right| ^ { 2 } \right)$ <sup>O j jj j</sup>time is required to identify all possible user pairs. <sup>O j</sup>For each pair $u _ { 1 } , u _ { 2 } ^ { \prime } { \in } U S E R S$ , the cardinality of both the intersection and the union of their granted permissions can be computed in PERMS . In particular, by scanning UP only once, we can build a <sup>Oð Þj j</sup>hashtable of permissions that each user has been granted. Notice that $| U P | { \leq } | U S E R S | | P E R M S |$ . Hence, checking if a permission is in $p e r m s ( u _ { 1 } )$ <sup>j j j jj j</sup>requires 1 . This check should be done for every permission in <sup>Oð Þ</sup>perms(u ), thus requiring PERMS . Altogether, the similarity index <sup>Oð Þj j</sup>can be calculated in PERMS USERS <sup>2</sup> <sup> </sup>.

Algorithm 1. Approximation of the similarity index.

$$
\begin{array}{l} 1 \text {:} \text { Procedure } \tilde {S} (U S E R S, k) \\ 2 \text {:} \quad \ell \leftarrow 0 \end{array}
$$

```txt
3: if |USERS| = 1 then
4:    return 1
5: else
6:    for i = 1 ... kdo
7:    Select u₁, u₂ ∈ USERS: u₁ ≠ u₂ uniformly at random
8:    ℓ ← ℓ + s(u₁, u₂)
9:    end for
10:    return ℓ / k
11:    end if
12: end procedure
```

To reduce the computation time, we propose the ε-approximated algorithm listed in Algorithm 1. The algorithm performs uniform sampling over all possible user pairs and then computes the average similarity among them. In particular, in each of the k sampling (Line 6), a user pair $u _ { 1 } , u _ { 2 }$ is randomly chosen (Line 7). Then, the variable ℓ is incremented by the similarity value of this pair (Line 8). In accordance with our de<sup>fi</sup>nition, the returned result is $\ell / k .$ We now show that the algorithm is totally correct: it terminates in a <sup>fi</sup>nite time and provides a correct result. First, Algorithm 1 always terminates because its core is a <sup>fi</sup>nite loop. Then, the following theorem proves that the computed result is probabilistically correct:

Theorem 2. The value $\tilde { S } ($ USERS; k computed by a run of Algorithm 1 satis<sup>fi</sup>es:

$$
\operatorname * {P r} \left(\left| \tilde {S} (U S E R S, k) - S (U S E R S) \right| \geq \varepsilon\right) \leq 2 \exp \left(- 2 k \varepsilon^ {2}\right).
$$

Proof. If $| U S E R S | = 1$ the proof is immediate. Let us consider the case when $| U S E R S | > 1$ . We will use the Hoeffding inequality [17] to prove this theorem. The cited inequality states that if $X _ { 1 } \ldots X _ { k }$ are independent random variables such that $0 { \le } X _ { i } { \le } 1$ , then

$$
\operatorname * {P r} \left(\left| \sum_ {i = 1} ^ {k} X _ {i} - \mathbb {E} \left[ \sum_ {i = 1} ^ {k} X _ {i} \right] \right| \geq t\right) \leq 2 \exp \left(- \frac {2 t ^ {2}}{k}\right),\tag{24}
$$

where $\mathbb { E } [ \cdot ]$ indicates the expected value of a random variable. In our case, $X _ { i }$ indicates the similarity of a randomly chosen user pair. Eq. (24) can be rewritten as

$$
\operatorname * {P r} \left(\left| \frac {1}{k} \sum_ {i = 1} ^ {k} X _ {i} - \mathbb {E} \left[ \frac {1}{k} \sum_ {i = 1} ^ {k} X _ {i} \right] \right| \geq \varepsilon\right) \leq 2 \exp \left(- 2 k \varepsilon^ {2}\right),\tag{25}
$$

where $\varepsilon { = } t / k .$ Notice that the value $\frac { 1 } { k } \sum _ { i = 1 } ^ { k } X _ { i }$ is exactly the output of Algorithm 1. Hence, in order to prove that the algorithm gives an approximation of S(USERS), we have to prove that $\hat { \mathfrak { z } } \left[ \frac { 1 } { k } \sum _ { i = 1 } ^ { k } X _ { i } \right]$ is equal to S(USERS). Because of the linearity of the expectation, the following equation holds:

$$
\mathbb {E} \left[ \frac {1}{k} \sum_ {i = 1} ^ {k} X _ {i} \right] = \frac {1}{k} \sum_ {i = 1} ^ {k} \mathbb {E} [ X _ {i} ].\tag{26}
$$

Since the user pair used to calculate $X _ { i }$ is picked uniformly at random, the corresponding similarity value is produced with a probability of $1 / \binom { | U S E R S | } { 2 }$ —that is, one out of all the possible (unordered) pairs. Thus, the expected value of $X _ { i }$ is

$$
\forall i\in 1\dots k,\mathbb{E}[X_{i}] = \sum_{\substack{u_{1},u_{2}\in USER:\\ u_{1}\neq u_{2}}}\frac{s(u_{1},u_{2})}{\binom{|USERS|}{2}}.
$$

The previous equation is the de<sup>fi</sup>nition of S(USERS) as in Eq. (10) when USERS N 1, completing the proof. □

<sup>j j</sup>For practical applications of Algorithm 1, it is possible to calculate the number of loops needed to obtain an expected error that is less than ε with a probability greater than $p .$ The following is an application of Th. 2:

$$
k > - \frac {1}{2 \varepsilon^ {2}} \ln \left(\frac {1 - p}{2}\right).\tag{27}
$$

For instance, if we want an error εb0.05 with probability greater than 98.6%, it is enough to choose k≥993.

Finally, we shall demonstrate that the computational complexity of Algorithm 1 is UP PERMS . Indeed, according to the <sup>Oð Þj jj j</sup>observation made at the beginning of this section, we can build a hashtable of permissions possessed by users in UP . The loop in <sup>Oð Þ</sup>Line 6 is repeated k times, and we reasonably assume that k∈ UP . Computing the similarity of two users in each loop <sup>Oð Þj j</sup>requires PERMS thanks to the hashtable. Therefore, the total <sup>Oð Þj j</sup>complexity is UP PERMS , that is advantageous when compared to the exact similarity calculation if the number of users is greater than the number of permissions and, most of all, when the user set is large.

## 6.2. Approximating the minability

Here we will show that the computational complexity of calculating M(UP) is $\mathcal { O } \Big ( | U P | ^ { 3 } \Big )$ . In the case of a large-size organization, <sup>O j j</sup>computation may be unfeasible since UP can count hundreds of thousands of user–permission assignments. For this reason, we propose an approximation algorithm for $M ( U P )$ that has a computational complexity of  k UP  .

<sup>Oð Þj j</sup>First, let us consider the complexity of computing the exact value of M(UP). In Eq. (15), the <sup>fi</sup>rst sum is over all the user–permission assignments ω∈UP, while the second one is over all the triples $\langle \omega _ { 1 } , \omega _ { 2 } \rangle \in t r i p l e s ( \omega ) { - } \mathrm { t h } a \mathrm { t } ,$ for a given ω, are $( | U P | { - } 1 ) ( | U P | { - } 2 )$ in the <sup>ð Þj j ð Þj j</sup>worst case. Each addendum of the sum corresponds to checking whether the selected triple is also a triangle. It is a triangle if the two outer nodes $\pmb { \omega } _ { 1 } = \langle u , p \rangle$ and $\omega _ { 2 } = \langle u ^ { \prime } , p ^ { \prime } \rangle$ 〉 of the selected triple induce a biclique. This occurs $\operatorname { f } u = u ^ { \prime } , \operatorname { o r } p = p ^ { \prime } .$ , or other two edges $\omega _ { 3 } = \langle u , p ^ { \prime } \rangle$ and $\omega _ { 4 } = \langle u ^ { \prime } , p \rangle$ exist in UP. It is possible to check if $u = u ^ { \prime } \ : 0 \mathrm { r } p = p ^ { \prime }$ in a constant time. Instead, the search for the pair $\omega _ { 3 } , \omega _ { 4 }$ can be executed in 1 after having built a hashtable of all possible user–permission assignments in $\mathcal { O } ( | U P | )$ . The total computational cost is thus $\mathcal { O } \Big ( | U P | ^ { 3 } \Big )$

## Algorithm 2. Approximation of the minability index.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Procedure  $\tilde{M}(UP,k)$ 
2:    $\ell\leftarrow0$ 
3:    for  $i=1\ldots k$  do
4:    Select  $\omega\in UP$  uniformly at random
5:    if triples( $\omega$ )  $\neq\varnothing$  then
6:    Select  $\langle\omega_{1},\omega_{2}\rangle\in\text{triples}(\omega)$  uniformly at random
7:    if  $\omega_{1}\in\text{biclique}(\omega_{2})\text{then}$ 
8:    $\ell\leftarrow\ell+1$ 
9:    end if
10:    else
11:    $\ell\leftarrow\ell+1$ 
12:    end if
13:    end for
14:    return  $\ell/k$ 
15: end procedure
</div>

To reduce the computation time, we propose the ε-approximated algorithm listed in Algorithm 2, that is inspired by [27] but adapted to the bipartite graph case. In each of the k steps, a user–permission assignment ω is randomly chosen (Line 4). Then, two random user– permission assignments among those that induce a biclique together with ω (if any) are selected (Line 6). If these two user–permission assignments induce a biclique, the counter ℓ is incremented by 1 since we have found a triple that is also a triangle (Line 7). The ratio of the number of found triangles ℓ to the number of sampled triples k (Line 14) represents the approximated minability value.

In the following, we show that the algorithm terminates and returns a correct result. First, notice that the core of Algorithm 2 is a <sup>fi</sup>nite loop, thus it always outputs a result in a <sup>fi</sup>nite amount of time. The following theorem proves that this answer is probabilistically correct:

Theorem 3. The value $\tilde { M } ( U P , k )$ computed by a run of Algorithm 2 satis<sup>fi</sup>es:

$$
\operatorname * {P r} \left(\left| \tilde {M} (U P, k) - M (U P) \right| \geq \varepsilon\right) \leq 2 \exp \left(- 2 k \varepsilon^ {2}\right).
$$

Proof. We follow the same proof schema of Th. 2. Let $X _ { 1 } . . . X _ { k }$ be independent random variables, where $X _ { i } = 1 { \mathrm { ~ i f } } ,$ for a randomly selected tuple $\langle \omega , \omega _ { 1 } , \omega _ { 2 } \rangle \ U P \times U P \times U P$ such that $\langle \omega _ { 1 } , \omega _ { 2 } \rangle$ ∈ triples(ω), either $\omega _ { 1 } \in b i c l i q u e ( \omega _ { 2 } )$ or triples $( \omega ) = \emptyset$ . Otherwise, $X _ { i } = 0$ . In this case, Eq. (25) still holds and, in particular, $\frac { 1 } { k } \sum _ { i = 1 } ^ { k } X _ { i }$ is exactly the output of <sup>-</sup>Algorithm 2. Hence, in order to prove that the algorithm gives an approximation of M(UP), we have to prove that E $\textstyle \left[ { \frac { 1 } { k } } \sum _ { i = 1 } ^ { k } X _ { i } \right]$ is equal to $M ( U P )$ . Because of the linearity of the expectation, Eq. (26) still holds. To calculate X we <sup>fi</sup>rst pick a user–permission relationship uniformly at random, then we pick two user–permission relationships that make up a triple. Thus, the corresponding minability value is produced with a probability of $1 / \left( | U P | | t r i p l e s ( \mathbf { \omega } \omega ) | \right)$ . Consequently, the expected value $\mathrm { o f } X _ { i }$ is

$$
\forall i \in 1... k, \mathbb {E} [ X _ {i} ] = \sum_ {\omega \in U P} \sum_ {\langle \omega_ {1}, \omega_ {2} \rangle \in t r i p l e s (\omega)} \frac {Y (\omega , \omega_ {1} , \omega_ {2})}{| U P | | t r i p l e s (\omega) |} + \sum_ {\omega \in U P: t r i p l e s (\omega) = \emptyset} \frac {1}{| U P |}.
$$

The previous equation is equivalent to the de<sup>fi</sup>nition of $M ( U P )$ as in Eq. (15), completing the proof. □

In the same way as the similarity index, it is possible to calculate the number of times it takes the loop in Algorithm 2 to obtain an expected error which is less than ε with a probability greater than $p .$ By analyzing Th. 3 it can be seen that the same result $\left( \operatorname { E q . } \left( 2 7 \right) \right)$ holds for this case.

As for computational complexity, we will now show that Algorithm 2 requires a time $\mathcal { O } ( k | U P | )$ to run. The loop in Line 3 is repeated k times. In each loop, a random user–permission relationship $\omega { \in } U P$ can be selected in constant time (Line 4). Let us consider $\omega =$ $\langle u , p \rangle$ . In order to randomly select a pair $\langle \omega _ { 1 } , \omega _ { 2 } \rangle$ that belongs to triples (ω), we have to calculate the set biclique(ω), then every possible pair of this set is in triples(ω) (Line $5 ) . \operatorname { E q . } ( 1 )$ states that $b i c l i q u e ( \boldsymbol { \omega } ) = \{ \langle u ^ { \prime }$ $p ^ { \prime } \rangle { \in } U P | \langle u , p ^ { \prime } \rangle , \langle u ^ { \prime } , p \rangle { \in } U P \land \langle u , p \rangle { \neq } \langle u ^ { \prime } , p ^ { \prime } \rangle { } ]$ . The number of elements of $b i c l i q u e ( \omega )$ is at most $| U P | - 1$ , and each element can be found in <sup>j j</sup>1 after having built a hashtable of all possible user–permission assignments in $\mathcal { O } ( | U P | )$ . Then, the computational cost incurred to <sup>Oð Þj j</sup>identify a biclique is at most $\mathcal { O } ( | U P | )$ . Line 7 can be executed in $\mathcal { O } ( 1 )$ since it represents a search in the hashtable to verify the conditions in Eq. (1). Hence, the computational complexity of Algorithm 2 is $\mathcal { O } ( k | U P | )$ , which greatly improves over the time required to calculate <sup>Oð Þj j</sup>the exact value $M ( U P )$ . This computational improvement is traded-off with a slight (tunable) decrease in the precision of the computed value $M ( U P , k )$

## 6.3. Approximation of conditioned indices

We now demonstrate that the amount of approximation introduced by the proposed randomized algorithms, when applied to the calculation of conditioned indices, is comparable to the approximation of the non-conditioned indices.

Theorem 4. Let $S _ { \Omega } ( U S E R S ) , R i s k _ { S _ { \mathrm { o } } } ( U S E R S , \Omega ) , M _ { \Omega } ( U P )$ , and $R i s k _ { M _ { \Omega } } ( U P , \Omega )$ be the exact indices conditioned by a given partition Ω according to de<sup>fi</sup>nitions 7, 8, 9, and 10, respectively. Let $\tilde { S } _ { \Omega } ( U S E R S , k ) , \tilde { R } i s k _ { S _ { 0 } } ( U S E R S$ $\Omega , k ) , M _ { \Omega } ( U P , k ) ,$ , and $\tilde { R } i s k _ { M _ { 0 } } ( U P , \Omega , k )$ <sup>ð Þ</sup> <sup>ð</sup>be the corresponding approxi-<sup>Þ ð Þ ð Þ</sup>mated values computed by adopting Algorithm 1 and Algorithm 2 for each subset $\Omega _ { i } \in \Omega .$ . Then:

$$
\operatorname * {P r} \left(\left| \tilde {S} _ {\Omega} (U S E R S, k) - S _ {\Omega} (U S E R S) \right| \geq \varepsilon\right) \leq 2 \exp \left(- 2 k \varepsilon^ {2}\right)
$$

$$
\operatorname * {P r} \left(\left| \tilde {\text { Risk }} _ {S _ {\Omega}} (\text { USERS }, \Omega , k) - \text { Risk } _ {S _ {\Omega}} (\text { USERS }, \Omega) | \geq \varepsilon\right) \leq 2 \exp \left(- 2 k \varepsilon^ {2}\right) \right.
$$

$$
\operatorname * {P r} \left(\left| \tilde {M} _ {\Omega} (U P, k) - M _ {\Omega} (U P) \right| \geq \varepsilon\right) \leq 2 \exp \left(- 2 k \varepsilon^ {2}\right)
$$

$$
\operatorname * {P r} \left(\left| \tilde {\text { Risk }} _ {M _ {\Omega}} (U P, \Omega , k) - \text { Risk } _ {M _ {\Omega}} (U P, \Omega) | \geq \varepsilon\right) \leq 2 \exp \left(- 2 k \varepsilon^ {2}\right). \right.
$$

Proof. We <sup>fi</sup>rst demonstrate that the theorem holds true for the approximation introduced by the given algorithms for the conditioned minability. Let $\varepsilon _ { i }$ be the approximation for each subset $\Omega _ { i } ,$ namely:

$$
\tilde {M} (\Omega_ {i}, k) = M (\Omega_ {i}) + \varepsilon_ {i}
$$

The approximated conditioned value will thus be:

$$
\tilde {M} _ {\Omega} (U P, k) = \frac {\sum \tilde {M} (\Omega_ {i} , k) | \Omega_ {i} |}{\sum | \Omega_ {i} |} = M _ {\Omega} (U P) + \frac {\sum \varepsilon_ {i} | \Omega_ {i} |}{\sum | \Omega_ {i} |}\tag{28}
$$

According to Th. 3, ε ≥ε with probability less than $2 \exp \left( - 2 k \mathfrak { c } ^ { 2 } \right)$ hence $\left| \frac { \sum \varepsilon _ { i } | \Omega _ { i } | } { \sum | \Omega _ { i } | } \right|$ ≥ε with probability less than 2 exp $\left( - 2 k \varepsilon ^ { 2 } \right)$ . Put another way, P $\mathrm { r } \left( \left| \tilde { M } _ { \Omega } ( U P , k ) - M _ { \Omega } ( U P ) \right| \geq \varepsilon \right) \leq 2 \exp \left( - 2 k \varepsilon ^ { 2 } \right)$ . Thus completing the proof for the approximated conditioned minability. The proof for other conditioned indices can simply be obtained by replacing Eq. (28) with the corresponding index de<sup>fi</sup>nitions. □

## 7. Results and discussion

To demonstrate the usefulness of the proposed indices, we show how they have been applied to a real case. Our case study has been carried out on a large private organization. We examined a representative organization branch that contained 1363 users with 5319 granted permissions, resulting in a total of 84201 user–permission assignments. To apply our approach we used two information sources: the organization unit (OU) chart, and a categorization of the users based on their job titles. In order to protect organization privacy, all names reported in this paper for organization units and job titles are slightly different from the original ones. We calculated all the indices described in the previous sections by adopting Algorithm 1 and Algorithm 2 with $k = 5 0 0 0 ,$ , hence obtaining an error of less than 0.02 with a probability higher than 96%.

The remainder of this section is organized as follows. In Section 7.1 we will show two examples that have different values for minability and similarity, thus making it possible to better understand the meaning of having high or low values associated to these indices. In turn, in Section $7 . 2$ we will apply our methodology in order to select the best available top-down information to decompose the problem. To further demonstrate the reliability of the methodology, we borrow from biology the methodology of introducing a control test. That is, we try to categorize users according to the <sup>fi</sup>rst character of their surname. Since this categorization does not re<sup>fl</sup>ect any access control logic, we will analytically show that—as expected—it never helps the mining phase. Finally, in Section 7.3 we will use the proposed methodology in conjunction with the organizational unit chart to “drill-down” into smaller role mining problems.

## 7.1. High and low values of minability and similarity

Fig. 3 shows the user–permission assignments for two distinct sets of users that belong to two chosen branches of the analyzed organization. The two OUs are comparable in terms of number of users, permissions, and user–permission assignments: Fig. 3(a) is related to 54 users who possess 285 permissions through 2379 user–permission assignments; Fig. 3(b) represents 48 users who possess 299 permissions through 2081 user–permission assignments.

Assignments are depicted in a matrix form, where each row represents a user, each column represents a permission, and a black cell indicates a user with a given permission granted. By using the role mining algorithm described in [4], we computed all possible maximal equivalent roles. Then, rows and columns have been sorted so that roles with the largest number of users and permissions appear as “big” areas of contiguous painted cells.

Fig. 3(a) is an example of high values for minability (0.84) and similarity (0.43). It visually demonstrates how, in this case, it is easy to identify candidate roles—few groups of contiguous cells that cover most of the assignments can be easily identi<sup>fi</sup>ed via a visual inspection. The role identi<sup>fi</sup>cation task clearly requires more effort

(a) Example of high similarity (0.43) and high minability (0.84)  
![](/api/attachments/HAFFY2HV/fulltext/images/d8e9f875d57df3d0e7a00ac1a20ddc3e32882c7344abed292afbe9309d5dd491.jpg)

(b)Example of low similarity (0.21) and low minability (0.66)  
![](/api/attachments/HAFFY2HV/fulltext/images/6c2fff364795c28f359a734828955f7b979316154d3c99c336d0b5df28f7c4d4.jpg)

(c) Local minability per assignment for Fig. (a)  
![](/api/attachments/HAFFY2HV/fulltext/images/d9ce1d85871ffaa0597795f631286b7f2427e8cb7b1b3484e14dc29c16f4a9c0.jpg)

(d) Local minability per assignment for Fig. (b)  
![](/api/attachments/HAFFY2HV/fulltext/images/abf245079fb8811fca983180efea34791ad103f898d10c8b1dc84625088db089.jpg)

(e) MERs per assignment for Fig. (a)  
![](/api/attachments/HAFFY2HV/fulltext/images/b6d40e1bd167b778c1e41e9037b031232c7e00915d36a9e3bf2bde630a7f9ac9.jpg)

(f) MERs per assignment for Fig. (b)  
![](/api/attachments/HAFFY2HV/fulltext/images/f2bb4c9bcfdc7e6b3f2bf1941495f03207935c9394e4868f5ac9fc01ba46b29b.jpg)  
Fig. 3. Examples of different values for similarity and minability. Figures (a) and (b) depict user–permission assignments in a matrix form, where each black cell indicates a user (row) that has a certain permission (column) been granted. Figures (e) and (f) show the number of MERs which cover each user–permission assignment, sorted by the descending local minability values reported in (c) and (d).

in Fig. 3(b), in line with lower values for minability (0.66) and similarity (0.21). Indeed, it is impossible to de<sup>fi</sup>ne an organizational role composed of as many users and permissions as in the previous case, and it is harder to identify roles in general. This intuition is also supported by Fig. 3(e) and (f). In these pictures we show the number of possible MERs that can be used to manage each user–permission assignment of Fig. 3(a) and (b), respectively. Assignments are sorted by descending local minabilities, and the corresponding minability values are reported in Fig. 3(c) and (d). In the <sup>fi</sup>rst case, the number of assignments with a local minability close to 1 is higher than in the second case. This is re<sup>fl</sup>ected by the number of MERs that cover each user–permission assignment, that is lower in the <sup>fi</sup>rst case. Put another way, the ambiguity of selecting the role to manage each user– permission assignment is lower in the <sup>fi</sup>rst example. This is in line with Th. 1, which states that when the local minability of an assignment is equal to 1, there is only one MER to choose. The more the minability is far from 1, the more the number of MERs that can be used to manage that assignment increases, indicating that the identi<sup>fi</sup>cation of the “best” role-set requires more effort and, consequently, it is more error prone.

## 7.2. Selection of the best business information

In this section we summarize how we have implemented our divide-and-conquer approach. As anticipated before, we had at our disposal two top-down pieces of information—OU and job titles—, and we wanted to choose the one that mostly simpli<sup>fi</sup>es the subsequent mining steps. As a control, we also introduced a third “arti<sup>fi</sup>cial”

Table 1  
Further decomposition of the sample organization branch.

<table><tr><td>Organization Unit</td><td>Index Type</td><td>Similarity</td><td>Minability</td><td>Similarity-Based Risk</td><td>Minability-Based Risk</td><td>Roles</td><td>msec</td></tr><tr><td colspan="2">Operations</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Manufacturing</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Not Conditioned</td><td>0.08</td><td>0.68</td><td>4.59</td><td>1.58</td><td>10,001</td><td>242</td></tr><tr><td></td><td>Conditioned by Alphabetical Groups</td><td>0.08</td><td>0.74</td><td>7.30</td><td>1.70</td><td>4,422</td><td>134</td></tr><tr><td></td><td>Conditioned by Organization Units</td><td>0.10</td><td>0.78</td><td>4.40</td><td>0.97</td><td>4,424</td><td>125</td></tr><tr><td></td><td>Conditioned by Job Titles</td><td>0.29</td><td>0.89</td><td>3.23</td><td>0.53</td><td>918</td><td>59</td></tr><tr><td colspan="2">Product Development</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Not Conditioned</td><td>0.20</td><td>0.82</td><td>4.01</td><td>0.92</td><td>4,007</td><td>150</td></tr><tr><td></td><td>Conditioned by Alphabetical Groups</td><td>0.20</td><td>0.84</td><td>6.24</td><td>1.11</td><td>2,511</td><td>73</td></tr><tr><td></td><td>Conditioned by Organization Units</td><td>0.37</td><td>0.86</td><td>4.83</td><td>1.05</td><td>2,080</td><td>76</td></tr><tr><td></td><td>Conditioned by Job Titles</td><td>0.38</td><td>0.90</td><td>5.63</td><td>0.64</td><td>818</td><td>36</td></tr><tr><td colspan="2">Material Management</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Not Conditioned</td><td>0.28</td><td>0.76</td><td>0.72</td><td>0.24</td><td>36,620</td><td>276</td></tr><tr><td></td><td>Conditioned by Alphabetical Groups</td><td>0.28</td><td>0.80</td><td>5.58</td><td>1.28</td><td>3,504</td><td>48</td></tr><tr><td></td><td>Conditioned by Organization Units</td><td>0.33</td><td>0.85</td><td>0.69</td><td>0.17</td><td>1,224</td><td>25</td></tr><tr><td></td><td>Conditioned by Job Titles</td><td>0.28</td><td>0.82</td><td>0.72</td><td>0.21</td><td>21,614</td><td>105</td></tr><tr><td colspan="2">Sales</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Not Conditioned</td><td>0.07</td><td>0.63</td><td>4.64</td><td>1.85</td><td>61,933</td><td>471</td></tr><tr><td></td><td>Conditioned by Alphabetical Groups</td><td>0.08</td><td>0.72</td><td>8.15</td><td>2.23</td><td>11,659</td><td>81</td></tr><tr><td></td><td>Conditioned by Organization Units</td><td>0.11</td><td>0.67</td><td>1.63</td><td>1.39</td><td>50,314</td><td>301</td></tr><tr><td></td><td>Conditioned by Job Titles</td><td>0.11</td><td>0.80</td><td>4.21</td><td>0.73</td><td>1,757</td><td>30</td></tr><tr><td colspan="2">Quality</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Not Conditioned</td><td>0.08</td><td>0.89</td><td>4.61</td><td>0.57</td><td>40</td><td>2</td></tr><tr><td></td><td>Conditioned by Alphabetical Groups</td><td>0.08</td><td>0.94</td><td>8.35</td><td>0.58</td><td>36</td><td>1</td></tr><tr><td></td><td>Conditioned by Organization Units</td><td>0.12</td><td>0.94</td><td>5.92</td><td>0.45</td><td>24</td><td>2</td></tr><tr><td></td><td>Conditioned by Job Titles</td><td>0.21</td><td>0.96</td><td>3.61</td><td>0.22</td><td>25</td><td>1</td></tr><tr><td colspan="2">Logistics</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Not Conditioned</td><td>0.24</td><td>0.71</td><td>3.78</td><td>1.43</td><td>1,677</td><td>19</td></tr><tr><td></td><td>Conditioned by Alphabetical Groups</td><td>0.24</td><td>0.80</td><td>6.47</td><td>1.60</td><td>642</td><td>13</td></tr><tr><td></td><td>Conditioned by Organization Units</td><td>0.33</td><td>0.80</td><td>3.35</td><td>0.87</td><td>854</td><td>16</td></tr><tr><td></td><td>Conditioned by Job Titles</td><td>0.64</td><td>0.83</td><td>0.59</td><td>0.45</td><td>357</td><td>12</td></tr></table>

information without any relation to the business—the <sup>fi</sup>rst letter of user's surname. We generated three groups of users: A–G, H–P, and Q–Z. Obviously, we did not expect that this information would help the identi<sup>fi</sup>cation of roles. Indeed, experimental results con<sup>fi</sup>rmed our expectations, as shown later on.

The job title information was only available inside OU branches at the second level of the OU tree. Therefore, we <sup>fi</sup>rst decomposed the problem by using the <sup>fi</sup>rst OU level. Table 1 sums up the results for one of the <sup>fi</sup>rst level OUs, namely the branch Operations. As required by Def. 8 and Def. 10, for both OUs and job titles we estimated the impact of harmful administration actions for each potential group of users— due to the large number of involved job titles, in Table 2 we only report the impact classi<sup>fi</sup>cation for OUs. Each group of users had been classi<sup>fi</sup>ed as “Low”, “Medium”, or “High” impact. Adopting a threepoint scale made it easier to reach consensus among administrators. The values assigned to those impact classes were conventionally set by administrators to 1, 5, and 10, respectively.

For each index, the best values among all available partitions is highlighted in gray in Table 1. First, notice that alphabetical groups are never preferred, since they do not capture any pattern or commonality among users within access control data. For the other pieces of information, different cases can be identi<sup>fi</sup>ed:

• In ‘Manufacturing’, partitioning by job titles is the best choice according to all indices. This means that job title is a good user's attribute to use when de<sup>fi</sup>ning administration rules for the assignment of roles with users belonging to ‘Manufacturing’.

• Even though the job title concept is closer to the “role” concept, partitioning by job titles is not always the best choice. Material Management shows a case where the best partition is based on OUs. In this case, this is justi<sup>fi</sup>ed by the fact that the majority of the users have the same job title. Hence, partitioning does not actually improve the mining complexity.

• The unit Sales shows a con<sup>fi</sup>guration where the minability and similarity indices suggest to partition by job title, but the risk indices promote the OU information. This happens because the unit Logistics contains many users that have a medium impact, and such users are not as similar among them as those having job titles with medium impact.

• Partitioning is not always advantageous. For instance, all users within the unit ‘Product Development’ have some commonalities in their permissions that will be lost when decomposing—as a matter of fact, users within Marketing have a medium impact and are not similar among them. Thus, if the role engineering objective is to <sup>fi</sup>nd organizational roles for ‘Product Development’, it is better to analyze the unit as a whole.

• As for the mining complexity, the number of maximal roles elicited by the role mining algorithm [4] is in line with the minability and similarity indices. Few roles also means less elaboration time, thus resulting in faster algorithm runs.

<table><tr><td>Organization Unit</td><td>Users</td><td>Permissions</td><td>User-Perms Assignments</td><td>Impact</td><td>Similarity</td><td>Minability</td><td>Similarity Based Risk</td><td>Minability-Based Risk</td><td>Roles</td><td>msec</td></tr><tr><td>Operations</td><td>946</td><td>3,647</td><td>56,905</td><td>Medium</td><td>0.07</td><td>0.65</td><td>4.63</td><td>1.73</td><td>219,086</td><td>3 637</td></tr><tr><td>Manufacturing</td><td>379</td><td>1,810</td><td>20,400</td><td>Medium</td><td>0.08</td><td>0.68</td><td>4.59</td><td>1.58</td><td>10,001</td><td>242</td></tr><tr><td>Parent</td><td>1</td><td>64</td><td>64</td><td>Low</td><td>1.00</td><td>1.00</td><td>0.00</td><td>0.00</td><td>1</td><td>0</td></tr><tr><td>Technology</td><td>49</td><td>323</td><td>2,342</td><td>Low</td><td>0.35</td><td>0.92</td><td>0.65</td><td>0.08</td><td>127</td><td>6</td></tr><tr><td>Control</td><td>26</td><td>577</td><td>2,396</td><td>Low</td><td>0.30</td><td>0.81</td><td>0.70</td><td>0.19</td><td>254</td><td>7</td></tr><tr><td>Test &amp; Quality</td><td>8</td><td>226</td><td>301</td><td>Low</td><td>0.09</td><td>0.92</td><td>0.91</td><td>0.08</td><td>17</td><td>1</td></tr><tr><td>Production</td><td>288</td><td>1,452</td><td>15,226</td><td>Medium</td><td>0.09</td><td>0.75</td><td>0.54</td><td>1.26</td><td>4 013</td><td>111</td></tr><tr><td>Plants</td><td>7</td><td>39</td><td>71</td><td>Low</td><td>0.12</td><td>0.83</td><td>0.88</td><td>0.17</td><td>12</td><td>0</td></tr><tr><td>Product Development</td><td>319</td><td>1,341</td><td>14,222</td><td>Medium</td><td>0.20</td><td>0.82</td><td>4.01</td><td>0.92</td><td>4 007</td><td>150</td></tr><tr><td>Parent</td><td>2</td><td>32</td><td>33</td><td>Low</td><td>0.03</td><td>0.98</td><td>0.97</td><td>0.02</td><td>3</td><td>0</td></tr><tr><td>Engineering</td><td>77</td><td>559</td><td>2,898</td><td>Medium</td><td>0.36</td><td>0.82</td><td>3.22</td><td>0.90</td><td>564</td><td>16</td></tr><tr><td>Design #1</td><td>88</td><td>361</td><td>3,275</td><td>Medium</td><td>0.41</td><td>0.84</td><td>2.94</td><td>0.80</td><td>10</td><td>1</td></tr><tr><td>Design #2</td><td>121</td><td>739</td><td>6,965</td><td>High</td><td>0.87</td><td>0.87</td><td>6.48</td><td>1.34</td><td>232</td><td>10</td></tr><tr><td>Design #3</td><td>6</td><td>115</td><td>214</td><td>Medium</td><td>0.14</td><td>0.93</td><td>4.28</td><td>0.36</td><td>1 205</td><td>47</td></tr><tr><td>Marketing</td><td>17</td><td>404</td><td>663</td><td>Medium</td><td>0.08</td><td>0.91</td><td>4.58</td><td>0.45</td><td>57</td><td>2</td></tr><tr><td>Innovation</td><td>8</td><td>92</td><td>174</td><td>Medium</td><td>0.23</td><td>0.97</td><td>3.85</td><td>0.16</td><td>9</td><td>0</td></tr><tr><td>Material Management</td><td>58</td><td>1,038</td><td>8,670</td><td>Low</td><td>0.28</td><td>0.76</td><td>0.72</td><td>0.24</td><td>36,620</td><td>276</td></tr><tr><td>Parent</td><td>3</td><td>286</td><td>368</td><td>Low</td><td>0.17</td><td>0.95</td><td>0.83</td><td>0.05</td><td>6</td><td>1</td></tr><tr><td>Purchase Dept #1</td><td>23</td><td>549</td><td>3,043</td><td>Low</td><td>0.27</td><td>0.80</td><td>0.73</td><td>0.20</td><td>745</td><td>10</td></tr><tr><td>Purchase Dept #2</td><td>13</td><td>407</td><td>2,136</td><td>Low</td><td>0.49</td><td>0.89</td><td>0.51</td><td>0.11</td><td>382</td><td>6</td></tr><tr><td>Purchase Dept #3</td><td>7</td><td>406</td><td>1,054</td><td>Low</td><td>0.29</td><td>0.77</td><td>0.71</td><td>0.23</td><td>56</td><td>3</td></tr><tr><td>Purchase Dept #4</td><td>5</td><td>311</td><td>972</td><td>Low</td><td>0.69</td><td>0.91</td><td>0.31</td><td>0.09</td><td>15</td><td>2</td></tr><tr><td>Saving Control</td><td>3</td><td>203</td><td>303</td><td>Medium</td><td>0.32</td><td>0.86</td><td>0.40</td><td>0.70</td><td>7</td><td>1</td></tr><tr><td>Analysis &amp; Reproting</td><td>4</td><td>376</td><td>794</td><td>Low</td><td>0.35</td><td>0.87</td><td>0.65</td><td>0.13</td><td>13</td><td>2</td></tr><tr><td>Sales</td><td>100</td><td>1,531</td><td>9,483</td><td>Medium</td><td>0.07</td><td>0.63</td><td>4.64</td><td>1.85</td><td>61,933</td><td>471</td></tr><tr><td>Parent</td><td>1</td><td>68</td><td>68</td><td>Low</td><td>1.00</td><td>1.00</td><td>0.00</td><td>0.00</td><td>1</td><td>0</td></tr><tr><td>Logistics</td><td>36</td><td>1,142</td><td>6,836</td><td>Medium</td><td>0.24</td><td>0.63</td><td>3.78</td><td>1.84</td><td>49,256</td><td>279</td></tr><tr><td>Support</td><td>63</td><td>795</td><td>2,579</td><td>Low</td><td>0.07</td><td>0.76</td><td>0.93</td><td>0.24</td><td>1 057</td><td>22</td></tr><tr><td>Quality</td><td>16</td><td>272</td><td>697</td><td>Medium</td><td>0.08</td><td>0.89</td><td>4.61</td><td>0.57</td><td>40</td><td>2</td></tr><tr><td>Parent</td><td>1</td><td>20</td><td>20</td><td>Low</td><td>1.00</td><td>1.00</td><td>0.00</td><td>0.00</td><td>1</td><td>0</td></tr><tr><td>Certification</td><td>2</td><td>40</td><td>46</td><td>Low</td><td>0.15</td><td>0.92</td><td>0.85</td><td>0.08</td><td>3</td><td>0</td></tr><tr><td>Audit</td><td>6</td><td>188</td><td>352</td><td>High</td><td>0.20</td><td>0.94</td><td>8.00</td><td>0.60</td><td>7</td><td>1</td></tr><tr><td>Quality Center</td><td>7</td><td>151</td><td>279</td><td>Medium</td><td>0.07</td><td>0.93</td><td>4.67</td><td>0.36</td><td>13</td><td>1</td></tr><tr><td>Logistics</td><td>73</td><td>1,078</td><td>3,432</td><td>Medium</td><td>0.24</td><td>0.71</td><td>3.78</td><td>1.43</td><td>1 677</td><td>19</td></tr><tr><td>Parent</td><td>0</td><td>0</td><td>0</td><td>Low</td><td>-</td><td>-</td><td>1.00</td><td>1.00</td><td>0</td><td>0</td></tr><tr><td>Methodologies</td><td>2</td><td>350</td><td>549</td><td>Low</td><td>0.57</td><td>0.92</td><td>0.43</td><td>0.08</td><td>3</td><td>1</td></tr><tr><td>Planning</td><td>7</td><td>311</td><td>682</td><td>Low</td><td>0.41</td><td>0.88</td><td>0.59</td><td>0.12</td><td>38</td><td>2</td></tr><tr><td>Distribution #1</td><td>62</td><td>464</td><td>1,780</td><td>Medium</td><td>0.32</td><td>0.70</td><td>3.38</td><td>1.52</td><td>810</td><td>12</td></tr><tr><td>Distribution #2</td><td>2</td><td>351</td><td>241</td><td>Medium</td><td>0.20</td><td>0.93</td><td>4.00</td><td>0.37</td><td>3</td><td>1</td></tr></table>

Table 2  
Further decomposition of the sample organization branch.

The previous examples also demonstrate that, in general, the choice of the best index to use (similarity, minability, similarity-based risk index, or minability-based risk index) depends on the main objective of the role engineering task.

## 7.3. Drill down

We now show an application of the proposed methodology when hierarchical information is available. Suppose that the only available top-down information is the organizational unit chart. Table 2 shows index values obtained by iteratively applying a decomposition based on OUs for the unit Operations. First, notice that partitioning users according to the second level of the OU tree raised the values of both indices for most OUs. For instance, ‘Product Development’, which holds approximately one third of the branch Operations, has a minability of 0.82 and a similarity of 0.20. Conversely, ‘Manufacturing still has low values for those indices. This means that it would be easier to <sup>fi</sup>nd optimal organizational and functional roles for ‘Product Development’ rather than for ‘Manufacturing’. Moreover, the average increase of minability is re<sup>fl</sup>ected by a lower number of possible MERs, dropped down from 219,086 to 114,278.

Another observation is that partitioning always reduces the number of users, permissions, and user–permission assignments to analyze, but the minability and the similarity values do not rise proportionally. For example, Logistics has a minability of 0.71, but his child ‘Distribution #1’ has a minability of 0.70, indicating that the “mess” of Logistics is likely concentrated in ‘Distribution #1’, as con<sup>fi</sup>rmed by the number of MERs. Further, ‘Product Development’ has much more users than Logistics, but it also has a higher minability. Moreover, high values for similarity imply high minability as well, but the inverse does not hold. If similarity is close to 1, then all users possess the same permissions; thus, minability is also close to 1. The opposite is false. For example, ‘Distribution #2’ shows a high minability (0.93) and a low similarity (0.20).

There are other examples of different trends for minability and similarity when compared to the number of users or permissions. For instance, let us consider ‘Marketing’ and ‘Purchase Dept #2’ which have similar number of users and permissions. In the <sup>fi</sup>rst case, we have 0.91 for minability and 0.08 for similarity, while in the second case we have 0.89 for minability (less than the previous case) and 0.49 for similarity (more than the previous case). Thus, this con<sup>fi</sup>rms that there is no direct relation between these two indices, but both are helpful to address role elicitation by highlighting two different aspects of the user–permission set. Indeed, if the objective of role engineers is to elicit organizational roles, the similarity helps to identify the OUs where an organizational role that covers a relevant number of user–permission assignment exists. This happens, for instance, for ‘Purchase Dept #4’ because of the similarity of 0.69. On the other hand, if the objective of role engineers is to <sup>fi</sup>nd functional roles, they have to consider the minability index. For example, the sub-branch Innovation is likely to be an easily solvable sub-problem due to a minability of 0.97, as con<sup>fi</sup>rmed by the low number of possible MERs.

As for risk indices, Table 2 highlights the behavior with respect to minability and similarity. For example, although the unit Audit has higher values for minability and similarity than the parent unit ‘Quality’, the high impact of the tasks performed by involved users compels a careful role design. According to this example, decomposing is a possible way to highlight data that requires particular attention from a risk management perspective. Another aspect to take into account is the required granularity for the partition. The most sensible approach is probably to stop decomposing when the risk indices do not increase or even increase slightly. For example, as shown in Table 1, by partitioning ‘Product Development’ according to its sub-units, the similarity-based risk index increases from 4.01 to 4.83, while the minability-based risk index grows from 0.92 to 1.05, reducing the gain in performing sub-unit driven analysis.

## 8. Concluding remarks

This paper describes a methodology that helps role engineers leverage business information during the role mining process. In particular, we demonstrate that by dividing data to analyze into smaller, more homogeneous subsets, it practically leads to more meaningful roles from a business perspective, hence decreasing the risk to make errors in managing them. To drive this process, two indices, referred to as minability and similarity, have been introduced. These indices are used to measure the expected complexity of analyzing the outcome of bottom-up approaches. In particular, we have shown how to apply such indices: to predict the effort needed to execute a role mining task over a set of user– permission assignments, thus being able to choose when to split a problem in several sub-problems; and, to select the top-down information that most simpli<sup>fi</sup>es the subsequent mining steps when more top-down information is available to role engineers. Leveraging these indices allows to identify the decomposition that increases business meaning in elicited roles in subsequent role mining steps, thus simplifying the analysis. We also introduced two fast probabilistic algorithms to ef<sup>fi</sup>ciently compute such indices, making them also suitable for big organization with hundreds of thousands of users and permissions. The quality of the indices is also formally assured.

Several examples, developed on real data, illustrate how to apply the tools that implement the proposed methodology, as well as its practical implications. Achieved results support the quality and the viability of the proposal.

## Acknowledgement

We would like to thank the anonymous reviewers that helped improve the quality of the paper.

## References

[1] American National Standards Institute (ANSI) and InterNational Committee for Information Technology Standards (INCITS). ANSI/INCITS 359-2004, Information Technology—Role Based Access Control. 2004.

[2] Ebru Celikel, Murat Kantarcioglu, Bhavani Thuraisingham, Elisa Bertino, A risk management approach to RBAC, Risk and Decision Analysis 1 (2) (2009) 21–33 IOS Press.

[3] Alessandro Colantonio, Roberto Di Pietro, Alberto Ocello., A cost-driven approach to role engineering, Proceedings of the 23 rd ACM Symposium on Applied Computing, SAC '08, 2008, pp. 2129–2136.

[4] Alessandro Colantonio, Roberto Di Pietro, Alberto Ocello, Leveraging lattices to improve role mining, Proceedings of the IFIP TC 11 23 rd International Information Security Conference SFC '08 in JFIP International Federation for Information Processing, Springer-Verlag, 2008, pp. 333–347.

[5] Alessandro Colantonio, Roberto Di Pietro, Alberto Ocello, Nino Vincenzo Verde, A formal framework to elicit roles with business meaning in RBAC systems,

Proceedings of the 14th ACM Symposium on Access Control Models and Technologies, SACMAT '09, 2009, pp. 85–94.

[6] Alessandro Colantonio, Roberto Di Pietro, Alberto Ocello, Nino Vincenzo Verde, A probabilistic bound on the basic role mining problem and its applications, Proceedings of the IFIP TC 11 24th International Information Security Conference, SEC '09 in IFIP International Federation for Information Processing, Springer-Verlag 2009, pp. 376–386.

[7] Alessandro Colantonio, Roberto Di Pietro, Alberto Ocello, Nino Vincenzo Verde., ABBA: adaptive bicluster-based approach to impute missing values in binary matrices, Proceedings of the 25th ACM Symposium on Applied Computing, SAC '10, 2010.

[8] Alessandro Colantonio, Roberto Di Pietro, Alberto Ocello, Nino Vincenzo Verde, Mining stable roles in RBAC. Proceedings of the IFIP TC 11 24th International Information Security Conference, SEC '09, IFIP International Federation for Information Processing, Springer-Verlag, 2009, pp. 259–269

[9] Edward J. Coyne, Role-engineering, Proceedings of the 1st ACM Workshop on Role-Based Access Control, RBAC '95, 1995, pp. 15–16.

[10] Edward J. Coyne, John M. Davis., Role engineering for enterprise security management, Artech House (2007).

[11] Sabrina De Capitani Di Vimercati, Sara Foresti, Pierangela Samarati, Sushil Jajodia Access control policies and languages, International Journal of Computationa Science and Engineering 3 (2) (2007) 94–102 Inderscience Publishers.

[12] Reinhard Diestel, Graph Theory (Graduate Texts in Mathematics), 3 rd ed. Springer-Verlag, 2005.

[13] William Horne, Nikola Milosavljevic, Prasad Rao, Robert Schreiber, Robert E. Tarjan, Fast exact and heuristic methods for role minimization problems, Proceedings of the 13th ACM Symposium on Access Control Models and Technologies, SACMAT '08, 2008, pp. 1–10.

[14] Mario Frank and David Basin and Joachim M. Buhmann. A class of probabilistic models for role engineering.pages 299–310.

[15] M. P. Gallagher and A.C. O'Connor and B. Kropp. The economic impact of rolebased access control. Technical report, Planning report 02-1, National Institute of Standards and Technology (NIST), 2002.

[16] Virgil Gligor. RBAC security policy model, preliminary draft report. Technical report, R23 Research and Development Department of the National Security Agency, 1995.

[17] Wassily Hoeffding, Probability inequalities for sums of bounded random variables, Journal of the American Statistical Association 58 (301) (1963) 13–30.

[18] Paul Jaccard, Etude comparative de la distribution <sup>fl</sup>orale dans une portion des Alpes et des Jura, Bulletin del la Société Vaudoise des Sciences Naturelles 37 (1901) 547–579.

[19] A. Kern, M. Kuhlmann, A. Schaad, J. Moffett, Observations on the role life-cycle in the context of enterprise security management, Proceedings of the 7th ACM Symposium on Access Control Models and Technologies, SACMAT '02, 2002, pp. 43–51.

[20] Martin Kuhlmann and Dalia Shohat and Gerhard Schimpf. Role mining – revealing business roles for security administration using data mining technology. pages 179–186.

[21] Haibing Lu, Jaideep Vaidya, Vijayalakshmi Atluri, Optimal Boolean matrix decomposition: application to role engineering, Proceedings of the 24th IEEE International Conferene on Data Engineering, ICDE '08, 2008, pp. 297–306.

[22] Ian Molloy, Ninghui Li, Tiancheng Li, Ziqing Mao, Qihua Wang, Jorge Lobo., Evaluating role mining algorithms, Proceedings of the 14th ACM Symposium on Access Control Models and Technologies, SACMAT '09, 2009, pp. 95–104.

[23] Gustaf Neumann, Mark Strembeck, A scenario-driven role engineering process for functional RBAC roles, Proceedings of the 7th ACM Symposium on Access Control Models and Technologies, SACMAT '02, 2002, pp. 33–42

[24] M.E. Newman, S.H. Strogatz, D.J. Watts, Random graphs with arbitrary degree distributions and their applications, Phys Rev E Stat Nonlin Soft Matter Phys 64 (2) (2001).

[25] M.E. Newman, D.J. Watts, S.H. Strogatz, Random graph models of social networks, Proceedings of the National Academy of Sciences of the United States of America 99 (1) (2002) 2566–2572

[26] H. Röckle, G. Schimpf, R. Weidinger., Process-oriented approach for role-<sup>fi</sup>nding to implement role-based security administration in a large industrial organization, Proceedings of the 5th ACM Workshop on Role-Based Access Control. RBAC 2000. 2000, pp. 103–110.

[27] Thomas Schank, Dorothea Wagner, Approximating clustering coef<sup>fi</sup>cient and transitivity, Journal of Graph Algorithms and Applications (2005) 9.

[28] Jurgen Schlegelmilch and Ulrike Steffens. Role mining with ORCA. pages 168–176.

[29] Jaideep Vaidya, Vijayalakshmi Atluri, Qi. Guo, Nabil Adam, Migrating to optimal RBAC with minimal perturbation, Proceedings of the 13th ACM Symposium on Access Control Models and Technologies, SACMAT '08, 2008, pp. 11–20.

[30] Jaideep Vaidya and Vijayalakshmi Atluri and Janice Warner. RoleMiner: mining roles using subset enumeration. pages 144–153.

[31] D.J. Watts, S.H. Strogatz, Collective dynamics of ‘small-world’ networks, Nature 393 (6684) (1998) 440–442.

[32] Yang Xiang, Ruoming Jin, David Fuhry, Feodor F. Dragan., Succinct summarization of transactional databases: an overlapped hyperrectangle scheme, Proceeding of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD '08, 2008, pp. 758–766.

[33] Dana Zhang and Kotagiri Ramamohanarao and Tim Ebringer. Role engineering using graph optimisation. pages 139–144.

![](/api/attachments/HAFFY2HV/fulltext/images/47a862b4e3043d2c3b16d592d13551cf2424a1fe1010c9a9fe50a6ea1d7e67a4.jpg)

Alessandro Colantonio is currently an Identity Management & Security Specialist at Engiweb Security, a privately held company owned entirely by Engineering Ingegneria Informatica, an Italian-market leader in system and business integration and application management services. He is also a Ph.D. candidate in Mathematics at “Roma Tre” University, Roma, Italy. He received the Master's Degree in Computer Engineering with specialization in IT Systems and Applications at University of Pisa, Italy, in July 2001. He also received a Specialization Master in IT Security Management at “La Sapienza” University, Rome, Italy, in January 2008. He brings 8 years of experience in the security software industry. His main research interests

![](/api/attachments/HAFFY2HV/fulltext/images/11401e9729dc4bbf61ca5f5e588de3f27a0a961c49a576e646e60115f1dffb8c.jpg)

Alberto Ocello is General Director at Engiweb Security. He holds a master of Electronic Engineering from the University of Rome, Italy and brings more than 25 years of experience in the security software industry. Alberto Ocello began his career at Page Europa (GTE Group) working in various roles in security application development, starting as Chief Product Architect and moving on to several product development groups in international military security projects. He then served as director of engineering, focusing on the application of PKI and new cryptographic technologies for enhancement of information security in electronic business scenarios. Alberto leads the company vision of role-based solutions, ensuring that technical excellence is the company cornerstone.

include the identi<sup>fi</sup>cation of new and innovative methodologies, techniques, and models for risk management, role engineering, and data mining supporting the role lifecycle within Role-Based Identity & Access Management systems.

![](/api/attachments/HAFFY2HV/fulltext/images/7a61868a47258f371c69de7e7a23b0b38e10016305a60c5e1bbbb23d5be808b5.jpg)

Roberto Di Pietro is currently an Assistant Professor at the Department of Mathematics of “Roma Tre” University, Roma, Italy. He is also with the UNESCO Chair in Data Privacy, Universitat Rovira i Virgili (Tarragona, Spain). He received the Ph.D. in Computer Science from the Università di Roma “La Sapienza”, Italy, in 2004. In 2004 he also received from the Department of Statistics of the same University a Specialization Diploma in Operating Research and Strategic Decisions. He received the Laurea degree in Computer Science from the University of Pisa, Italy, in 1994. To date, he has published more than 80 technical papers in high quality Conferences and Journals. His main research interests include: Role mining, security for mobile, ad-hoc, and underwater wireless networks, intrusion detection, security for distributed systems, secure multicast, applied cryptography and computer forensics.

![](/api/attachments/HAFFY2HV/fulltext/images/8661a15782beab71c792bca4c0e89e765fbcc09617a8ee7f74711f45f4d6ff3f.jpg)

Nino Vincenzo Verde is currently a Ph.D. candidate in Mathematics at “Roma Tre” University, Roma, Italy. He received the Master's Degree in Computer Science at University “La Sapienza”, Rome, Italy, in September 2007. His main interests include access control and sensors/adhoc network security. In particular. he is involved in the de<sup>fi</sup>nition of new models, tools and techniques that are useful for the de<sup>fi</sup>nition of roles in Role-Based Access Control system. Also, he is currently working on the security of wireless and ad-hoc networks for the protection of Critical Infrastructures.
