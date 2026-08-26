---
otero_id: 4188
otero_key: "JBXEQUXE"
title: "A multi-criteria ranking framework for partner selection in scientific collaboration environments"
authors: "Daniel Schall"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.10.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A multi-criteria ranking framework for partner selection in scienti<sup>fi</sup>c collaboration environments

Daniel Schall

Siemens Corporate Technology, Siemensstrasse 90, 1211 Vienna, Austria

a r t i c l e i n f o

Article history: Received 11 June 2013 Received in revised form 10 September 2013 Accepted 1 October 2013 Available online 9 October 2013

Keywords: Scienti<sup>fi</sup>c communities Multi-criteria selection Time-aware authority ranking Structural holes

## a b s t r a c t

Scienti<sup>fi</sup>c collaborations commonly take place in a global and competitive environment. Coalitions and project consortia are formed among universities, companies and research institutes to apply for research grants and to perform jointly collaborative projects. In such a competitive environment, individual institutes may be strategic partners or competitors. Measures to determine partner importance have practical applications such as comparison and rating of competitors, reputation evaluation or performance evaluation of companies and institutes. Many network-centric metrics exist to measure the importance of individuals or companies in social and collaborative networks. Here we present a novel approach for measuring and combing various criteria for partner importance evaluation. The presented approach is cost sensitive, aware of temporal and context-based partner authority, and takes structural information with regard to structural holes into account. Well-established graph models such as the notion of hubs and authorities provide the basis for the presented authority ranking approach and are systematically extended towards a novel uni<sup>fi</sup>ed HITS/PageRank model. The applicability of the proposed approach and the effects of parameter selection are extensively studied using real data from the European Union's research program.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Scienti<sup>fi</sup>c collaboration in an international environment takes place among partners such as organizations, universities or research institutes to jointly perform projects. The main motivation for organizations and individual research groups to collaborate is to enable knowledge and resource sharing to effectively perform research projects. Scienti<sup>fi</sup>c collaboration can be de<sup>fi</sup>ned as interaction taking place within a social context among two or more scientists that facilitates the sharing of meaning and completion of tasks with respect to a mutually shared, superordinate goal [33].

However, the success of research and innovation is based on the right balance between cooperation and competition. Hence, formation of coalitions and consortia is in<sup>fl</sup>uenced by partner reputation [14], institutional constraints, and mechanism of self-organization [35]. Scienti<sup>fi</sup>c collaboration can be analyzed at the level of researchers through co-authorship and citation networks [11,17,26] or at the level of organizations or research institutions [23]. The former has been widely studied by existing research while the latter lacks a principled approach for selecting and aggregating ranking criteria that may be in<sup>fl</sup>uenced by context. Generally, scienti<sup>fi</sup>c collaboration and endorsement can be analyzed according to three different methods [24]: (i) qualitative methods such as using a questionnaire-based approach, (ii) bibliometric methods including publication and citation counting or co-citation analysis, and (iii) complex network methods including network centrality metrics such as PageRank [28] or Hyperlink Induced Topic Search (HITS) [21]. Here we focus on the analysis of scienti<sup>fi</sup>c collaboration at the organizational or institutional level. We apply complex network methods to automate the analysis of partner importance in scienti<sup>fi</sup>c collaboration. In this work, importance is a concept that is governed by multiple factors including average cost of a partner, temporal trend and context of partner authority, and partner importance with regards to effective size of the partner's social network. Effective size in the context of structural holes and social networks means low redundancy among social contacts thereby yielding control bene<sup>fi</sup>ts of individuals. Here we apply a similar principle but focus on the organizational level rather than individuals in social networks.

In our previous work [32] we introduced an approach for measuring contextual importance in scienti<sup>fi</sup>c collaboration networks. In this work, we build upon our previous work [32] but signi<sup>fi</sup>cantly expand the concepts. Here we provide the following novel key contributions:

• We introduce a personalized partner authority model that is able to capture context-dependent and time-aware partner reputation.

• We introduce a model to measure structural importance of organizations embedded in scienti<sup>fi</sup>c collaboration networks. The idea of our structural importance metric is drawn from the notion of structural holes as established in a sociological research context.

• To support partner selection using multiple-criteria, the factors contributing to a partner importance are aggregated through a systematic approach to a single partner importance ranking score. Here we apply analytic hierarchy process (AHP) to derive the partner importance score.

• We present experimental results by providing a comprehensive study on the in<sup>fl</sup>uence of different parameters using real data from the EUs Seventh Framework Programme (FP7) for research in Information and Communication Technology (ICT).

This work is structured as follows. Section 2 gives an overview of related work and literature in the context of network formation and network analysis. Section 3 introduces basic concepts and de<sup>fi</sup>nitions used throughout this work. In Section 4 our personalized partner authority model is introduced. Section 5 introduces the structural importance model and Section 6 details the analytic hierarchy process to compute the <sup>fi</sup>nal partner importance scores. In Section 7 the evaluation results are presented followed by the conclusion and outlook to future work in Section 8.

## 2. Literature overview

We structure related work into two basic areas: network formation in the context of collaborative environments and network analysis methods with particular emphasis on authority ranking. From a technique point of view, many approaches found in both network formation and network analysis methods for authority ranking are based on graph theory and algorithms. In this section, we review literature in both areas as they will provide the foundation for our work.

## 2.1. Network formation

The rapid advancement of ICT-enabled infrastructure has fundamentally changed how businesses and companies operate. Global markets and the requirement for rapid innovation demand for alliances between individual companies [7]. It is widely agreed that knowledge of the structure of interaction among individuals or organizations is important for a proper understanding of a number of important questions such as the spread of new ideas and technologies and competitive strategies in dynamic markets [15]. Work by [34] investigated the evolutionary dynamics of network formation by analyzing how organizational units create new linkages for resource exchange. The potential gains from bridging different parts of a network were important in the early work of Granovetter [16] and are central to the notion of structural holes developed by Burt [5,6]. The theory is based on the hypothesis that individuals can bene<sup>fi</sup>t from serving as intermediaries between others who are not directly connected. A formal approach to strategic formation based on advanced game-theoretic broker incentive techniques was presented in [22]. In [2] group formation in social networks is studied.

## 2.2. Network analysis

We propose a model for importance that is based on wellestablished techniques such as the notion of hubs and authorities [21] and PageRank [28]. PageRank can be personalized [28] to estimate node importance with regard to certain topics [18–20]. After the seminal work of [28] and the far-reaching work of [19], related research (see also [4]) addressed, for example, ef<sup>fi</sup>cient computation of personalized PageRank [9,13] and a generalization of personalized PageRank towards bipartite graphs [10]. In [3], the authors proposed time-aware authority ranking by considering temporal properties of scienti<sup>fi</sup>c publication activity. Our previous work addressed PageRank personalization techniques for expertise ranking in a social network context [30,31].

In this work, we propose a new framework which utilizes both information from structural holes and authority importance scores to discover valuable collaboration partners. Here we propose a uni<sup>fi</sup>ed HITS/PageRank model that is able to measure network importance at the individual as well as the organizational or institutional level with respect to a certain context. In contrast to existing rankings such as the Shanghai academic ranking,<sup>1</sup> our approach is able to capture importance at a <sup>fi</sup>ne grained contextual level. Our approach is able to utilize various additional ranking parameters including desirable partner properties (e.g., high topic-sensitive authority) and low undesirable partner properties (e.g., partner costs). At the core of this framework are linkbased algorithms such as HITS and extensions towards personalized, time-aware PageRank, structural metrics to measure the brokerage potential of a given network node, and an analytic hierarchy process (AHP) algorithm [29] to aggregate these metrics into a single ranking score.

The proposed model is tested with data from the ICT research pro jects having received grants under the EU's FP7 program. The data as described in [25] and covers a period from 2007 to 2011.

## 3. De<sup>fi</sup>nitions and solution framework

## 3.1. Basic definitions

We start with a de<sup>fi</sup>nition of basic concepts that are used throughout this work. Let us consider a simple collaboration scenario in a scienti<sup>fi</sup>c community where individual partners (e.g., organizations, research institutes, and universities) collaborate in the context of research projects. Fig. 1 depicts a set of organizations $\{ 0 _ { 1 } , 0 _ { 2 } , 0 _ { 3 } \}$ } and a set of research projects $\{ p _ { 1 } , p _ { 2 } , p _ { 3 } \}$ . Each project is associated with a certain topic that determines the context of the performed collaboration (for example, ‘services’ or ‘internet’). Organizations are involved in projects by having certain roles. Roles include project coordinator and project partner. In addition to the involvement relation, a weighted edge is created from the project to the organization to depict the degree of involvement. For example, $o _ { 1 }$ is involved in projects $p _ { 1 }$ and $p _ { 2 }$ with weights $w _ { 1 1 }$ and $w _ { 2 1 }$ respectively. In our work, the weight will be based on the funding an organization receives in the context of a project. More funding typically means that an organization is able to allocate more (human) resources to the project and thereby perform more work. Finally, based on joint projects performed by organizations we model collaboration relations among them. Since $o _ { 1 }$ and $o _ { 2 }$ have been involved in the joint projects $p _ { 1 }$ and $p _ { 2 } ,$ , a collaboration relation between $o _ { 1 }$ and $o _ { 2 }$ is established as a dashed line. Similarly, $o _ { 2 }$ and $O _ { 3 }$ have been involved in the joint projects $p _ { 2 }$ and $p _ { 3 }$ and therefore a collaboration relation between $O _ { 2 }$ and $O _ { 3 }$ is established. Also, a collaboration relation between $o _ { 1 }$ and $O _ { 3 }$ exists because they jointly worked on $p _ { 2 } .$ . A collaboration relation is a mutual (undirected) edge. The applications of the presented concepts will be illustrated in the next section.

## 3.2. Solution framework

As already outlined before, our solution approach to support multicriteria partner selection in scienti<sup>fi</sup>c communities utilizes heavily graph-based models. Graph-based models are widely used in complexand social-network analysis. Fig. 2 shows the solution framework as a layered view.

## 3.2.1. Data management

The layer underneath the top-layer shows the data management that is responsible for retrieval of project relevant data, managing the needed graph structures to perform analysis and ranking, and persistence management of analysis and ranking results. From the top-layer (Of<sup>fl</sup>ine analysis) point of view, the data management can be accessed via the Data Manipulation Handler in a CRUD (Create-Read-Update-Delete) manner. The Data Provider offers read access to graph structures and of<sup>fl</sup>ine mining and ranking results. The Project Database contains information such as organizations, projects, project involvements, roles, funding, project descriptions, date of project contracts, and project duration. Let us de<sup>fi</sup>ne some basic graph structures that are obtained from information in the Project Database and then managed in the Graph Database.

![](/api/attachments/JBXEQUXE/fulltext/images/a9d370f9cb8b619e2ce32b190a942332bdb9e0440aa75a0200c697ef6897e792.jpg)  
a) Scientific collaboration environment.  
b) Legend.  
Fig. 1. Scienti<sup>fi</sup>c collaboration environment and de<sup>fi</sup>nitions

Based on projects, organizations, and involvement relations we de<sup>fi</sup>ne two types of graphs. First, let us de<sup>fi</sup>ne the directed projectorganization graph $G _ { P O } \left( V _ { P } , V _ { O } , \right.$ E ) that is composed of the set projects $V _ { P }$ and the set of organizations $V _ { O } \left( V _ { P } \right)$ and $V _ { O }$ depicting the vertices in the graph) and the project involvement relations denoted by the edge set E where an edge $( p , o ) \in E _ { F }$ points from the project p to organization o. Each edge $( p , o ) \in E _ { F }$ has a weight $w _ { p o }$ associated with it depending on the funding the organization o receives in project p divided by the total project funding. This type of graph is being used for organization authority ranking. Let us de<sup>fi</sup>ne the second type of graph as the undirected organization-collaboration graph $G _ { O C } ~ ( V _ { O } , E _ { O } )$ consisting of the set of organizations $V _ { O }$ depicting the vertices in the graph and the set of collaboration relations $E _ { O } .$ . Whereas the edges $E _ { P }$ in $G _ { P O }$ are based on project involvement relations pointing from projects to organizations, the edges $E _ { O }$ in $G _ { O C }$ are undirected and connect two organizations. This type of graph is being used for structural importance ranking. Details regarding these two types of graph structures will be provided in the following.

![](/api/attachments/JBXEQUXE/fulltext/images/821fb87c0a0035890d3388ea9b4f5ff3a08c6b33363ffb059b4f7041986a2d2e.jpg)  
Fig. 2. Solution framework outline.

## 3.2.2. Offline analysis

This layer deals with components that are invoked in an of<sup>fl</sup>ine manner (e.g., triggered by changes in the Project Database). The Topic Analyzer extracts relevant topics from project descriptions by <sup>fi</sup>ltering stop words and combining synonyms to single topics. Essentially, each topic is identi<sup>fi</sup>ed by a single keyword that has a frequency associated with it to identify popularity of topics. Typical topics in the context of ICT research are, for example, ‘services’ and ‘internet’. Sophisticated topic models such as cross-topic relations or hierarchical structures are not within the focus of this work (e.g., see [31] for hierarchical topic models and topic clustering techniques). The Topic Analyzer saves topic information in the Analysis & Ranking Database. If new topics are added, other components such as the Authority Ranker are triggered (see later). The Trend Analyzer calculates trends with regard to organizations' activities in topics. The historical project information is used to calculate a trend in increasing or decreasing number of projects for given topics. In a steady state (neither increasing nor decreasing activity), the trend equals 0. Trend information is utilized by the Authority Ranker to create topic and time-aware authority scores. The detailed mechanisms will be discussed in later sections. The Authority Ranker calculates numeric values for authority scores. To explain the notion of authority as used in this work, participation of an organization in a research project (i.e., involvement relation) is understood as a carrier of authority. By being involved in certain projects, we assume that organizations develop knowledge with regards to the projects' topic(s). An organization is considered to be an authority if it has extensive or specialized knowledge about a topic. In other words, an organization must have collaborated in the context of a topic to be considered as an authority for a given topic.

## 3.2.3. Online analysis

Previously, the of<sup>fl</sup>ine analysis components were responsible for preparing the information needed to perform online analysis and ranking. Our decision to divide functionality into online and of<sup>fl</sup>ine analysis was due to computational complexity of link-based authority ranking algorithms. Computation of authority at query time without having performed of<sup>fl</sup>ine computation would result in unacceptable response times at magnitudes of hours or even longer. All information from the previous steps is made available in the Analysis & Ranking Database. The Cost Ranker is a simple ranker that provides a scoring function based on organizations' average costs. The Structural Ranker calculates numeric values for structural importance scores. The idea of our structural importance metric is drawn from the notion of structural holes as established in a sociological context. To detail the difference between structural importance and authority, the notion of authority captures the importance of an organization with regard to knowledge drawn from past project experience. Structural importance captures a different notion of importance that is based on the lack of information <sup>fl</sup>ow and connectedness of parts of the network. As stated by Burt [5], structural holes are an opportunity to broker the <sup>fl</sup>ow of information between people and control the projects that bring together people from opposite sides of the hole. Here the notion of structural holes is not applied to people-based social networks, but to organization collaboration networks $( \mathrm { i } . \mathsf { e } . , G _ { O C } )$ . The goal of our ranking approach is to identify those organizations that have the ability to bridge structural holes and to allow for the emergence of novel innovative ideas through brokerage of information. The Authority Aggregator combines the authority results of of<sup>fl</sup>ine computed authority scores.

## 3.2.4. Query processing

Suppose a coordinator attempts to establish a new consortium and thus wants to <sup>fi</sup>nd collaboration partners who are able to join the consortium. Often, previous collaborators are known from <sup>fi</sup>rst hand collaboration experience but in today's vibrant and fast-paced research environment it is also useful to see the current community standing of known collaboration partners and to discover potential new collaborators. The coordinator is able to specify a keyword-based query $Q = \{ q _ { 1 } ,$ $q _ { 2 } , . . . , q _ { n } \}$ (using the Query Frontend) with the goal of <sup>fi</sup>nding matching organizations that are ranked according to a set of criteria (i.e., cost, structural importance and authority). The idea of our ranking approach is to compute ranking scores with respect to certain areas of expertise. The demanded areas of expertise are speci<sup>fi</sup>ed via the query Q and matched with topics. Each query keyword $q _ { n }$ corresponds to a desired area of expertise. A query returns a ranked list of organizations based on the demanded set of expertise areas. The AHP Ranker is used to create a composite ranking score S (o; Q) of organization o. The score $S \left( o ; Q \right)$ is given as

$$
S (o; Q) = A H P (A (o; Q), S I (o; Q), C (o))\tag{1}
$$

where $A ( o ; Q )$ is the organization's authority score and SI(o;Q) the structural importance score with respect to the query $Q _ { ☉ }$ and C(o) the cost score. The following sections will focus on the calculation of S(o;Q).

## 4. Authority model

Here we formalize the notion of organization authority as it will be used in our ranking model. Authority is automatically calculated using network analysis techniques. The novelty of the approach is that authority is put into context by considering topic information. Wellestablished models provide the foundational concepts and basis. Specifically, we base our approach upon the model of hubs and authorities as developed by [21].

## 4.1. Hubs and authorities

Let us apply the notion of hubs and authorities to a collaboration environment as depicted by Fig. 1. A project is regarded to be important if the organizations contributing to it are also regarded to be important (e.g., knowledgeable and reputable). In turn, the importance of an organization is based on its involvement in important projects. This is a recursive de<sup>fi</sup>nition of importance and can be modeled by using the intuitive notion of hubs and authorities as proposed by [21].

$$
A (o) = \sum_ {(p, o) \in E _ {P}} H (p) \quad H (p) = \sum_ {(p, u) \in E _ {P}} A (u)\tag{2}
$$

In the model, an organization o obtains an authority score depicted by A(o) and a project p obtains a hub score denoted by H(p). The drawback of this model is the ‘stability’ of rankings. A ranking algorithm is stable if the algorithm returns similar results upon small disturbances. We follow the randomized HITS approach as proposed in [27] and expand the equations in Eq. (2) as follows:

$$
A (o) = \left(1 - \lambda_ {a}\right) \delta_ {O} (o) + \lambda_ {a} \sum_ {(p, o) \in E _ {p}} H (p)\tag{3}
$$

$$
H (p) = \left(1 - \lambda_ {h}\right) \delta_ {P} (p) + \lambda_ {h} \sum_ {(p, u) \in E _ {P}} A (u).\tag{4}
$$

This adjusted model is a natural way of designing a random-walk based algorithm following the HITS model. The randomized HITS approach is, like PageRank, stable to small perturbations [27]. The symbols $\delta _ { { \cal O } } ( o )$ and $\delta _ { P } ( p )$ depict personalization vectors that may be assigned uniformly for each node such that $\begin{array} { r } { \delta _ { 0 } ( o ) = \frac { 1 } { | V _ { 0 } | } } \end{array}$ and $\begin{array} { r } { \delta _ { P } ( p ) = \frac { 1 } { | V _ { P } | } . } \end{array}$ Non-uniform personalization vectors result in personalized rankings. The parameters $\lambda _ { a }$ and $\lambda _ { h }$ with $0 \leq \lambda \leq 1$ allow for balancing between authority/hub weights and personalization weights. A typical value for λ is 0.85 [28]. Assigning lower values to λ means that higher importance is given to the personalization weights; thereby reducing the ‘network effect’ of the ranking algorithm.

## 4.2. Query-sensitive personalization

Let us de<sup>fi</sup>ne the query-sensitive authority score:

$$
A (o; Q) = \left(1 - \lambda_ {a}\right) \delta_ {O} (o; Q) + \lambda_ {a} \sum_ {(p, o) \in E _ {p}} w _ {p o} H (p; Q)\tag{5}
$$

Similarly, let us de<sup>fi</sup>ne the query-sensitive hub score:

$$
H (p; Q) = \left(1 - \lambda_ {h}\right) \delta_ {P} (p; Q) + \lambda_ {h} \sum_ {(p, u) \in E _ {P}} w _ {p u} A (u; Q)\tag{6}
$$

The edge weights $w _ { p o }$ and $\boldsymbol { w _ { p u } }$ are based on the organizations' degree of project involvement. Particularly, the weight $w _ { p o }$ is based on the funding received by organization o in project p and is calculated as

$$
w _ {p o} = \frac {\text { funding } (p , o)}{\sum_ {v \in \operatorname{adj} (p)} \text { funding } (p , v)}\tag{7}
$$

where $a d j ( p )$ depicts the set of nodes adjacent to p (i.e., the set of organizations involved in project p). To compute authority scores using a single equation, which is the desired goal of our approach, we substitute $H ( p ; Q )$ in Eq. (5) by Eq. (6) and have:

$$
\begin{array}{l} A (o; Q) = (1 - \lambda_ {a}) \delta_ {O} (o; Q) + \lambda_ {a} (1 - \lambda_ {h}) \sum_ {(p, o) \in E _ {p}} w _ {p o} \delta_ {P} (p; Q) \\ \qquad + \lambda_ {a} \lambda_ {h} \sum_ {(p, o) \in E _ {p}} \sum_ {(p, u) \in E} w _ {p o} w _ {p u} A (u; Q). \end{array}\tag{8}
$$

Based on Eq. (8), let us de<sup>fi</sup>ne the personalization vector $\delta _ { 0 } ^ { ' } ( o ; Q )$ as follows:

$$
\delta_ {O} ^ {\prime} (o; Q) = \frac {1 - \lambda_ {a}}{1 - \lambda_ {h}} \delta_ {O} (o; Q) + \lambda_ {a} \sum_ {(p, o) \in E _ {P}} w _ {p o} \delta_ {P} (p; Q).\tag{9}
$$

If we use the same parameter values for $\lambda _ { a }$ and $\lambda _ { h }$ (due to symmetry of Eqs. (5) and (6)) such that $\lambda _ { a } = \lambda _ { h } ,$ Eq. (9) simpli<sup>fi</sup>es to:

$$
\delta_ {O} ^ {\prime} (o; Q) = \delta_ {O} (o; Q) + \lambda \sum_ {(p, o) \in E _ {P}} w _ {p o} \delta_ {P} (p; Q).\tag{10}
$$

In the following step we rewrite Eq. (8) by using the personalization vector p′(u;Q) as de<sup>fi</sup>ned in Eq. (10).

$$
A (o; Q) = (1 - \lambda) \delta_ {o} ^ {\prime} (o; Q) + \lambda^ {2} \sum_ {(p, o) \in E _ {P}} \sum_ {(p, u) \in E _ {P}} w _ {p o} w _ {p u} A (u; Q)\tag{11}
$$

As one can see, Eq. (11) has a PageRank-like structure. An important concept for personalization based on the PageRank model is the linearity theorem as introduced in [19]. The theorem states that for any personalization vectors $\delta _ { 1 } , \delta _ { 2 }$ and weights w<sub>1</sub>, w<sub>2</sub> with $w _ { 1 } + w _ { 2 } = 1$ the following equality holds:

$$
P P V (w _ {1} \delta_ {1} + w _ {2} \delta_ {2}) = w _ {1} P P V (\delta_ {1}) + w _ {2} P P V (\delta_ {2}).\tag{12}
$$

$$
\begin{array}{l} A (o; Q) = (1 - \lambda) \delta_ {P} ^ {'} (o; Q) + \lambda^ {2} \sum_ {(p, o) \in E _ {P}} \sum_ {(p, u) \in E _ {P}} w _ {p o} w _ {p u} A (u; Q) \\ \quad = (1 - \lambda) \sum_ {q \in Q} w _ {q} \delta_ {P} ^ {'} (o; q) + \lambda^ {2} \sum_ {(p, o) \in E _ {P}} \sum_ {(p, u) \in E _ {P}} \sum_ {q \in Q} w _ {q} w _ {p o} w _ {p u} A (u; q) \\ \quad = \sum_ {q \in Q} w _ {q} (1 - \lambda) \delta_ {P} ^ {'} (o; q) + \sum_ {q \in Q} w _ {q} \lambda^ {2} \sum_ {(p, o) \in E _ {P}} \sum_ {(p, u) \in E _ {P}} w _ {p o} w _ {p u} A (u; q) \\ \quad = \sum_ {q \in Q} w _ {q} \Bigg [ (1 - \lambda) \delta_ {P} ^ {'} (o; q) + \lambda^ {2} \sum_ {(p, o) \in E _ {P}} \sum_ {(p, u) \in E _ {P}} w _ {p o} w _ {p u} A (u; q) \Bigg ] \\ \quad = \sum_ {q \in Q} w _ {q} [ A (o; q) ]. \end{array}\tag{13}
$$

The linearity theorem states that personalized PageRank vectors PPV can be composed as the weighted sum of PageRank vectors. Eq. (13) shows how to derive the weighted sum of personalized authority ranking scores using Eq. (11). The goal is to obtain a structure as depicted by the right part of Eq. (12). The weight $w _ { q }$ is associated with a particular keyword q with $\begin{array} { r } { w _ { q } = \frac { 1 } { | Q | } } \end{array}$ for uniform weights and $\textstyle \sum _ { q } w _ { q } = 1$

As stated before, the bene<sup>fi</sup>t of the model is the ability to precompute authority scores for particular topics, save them in a database, and aggregate the precomputed authority scores later at query time. Suppose the set of topics, as extracted by theTopic Analyzer, is given as $T = \{ T _ { 1 } , T _ { 2 } , . . . , T _ { n } \}$ . For each topic authority scores are calculated $A ( o ; T _ { 1 } ) , A ( o ; T _ { 2 } ) , . . . , A ( o ; T _ { n } )$ and utilized by the Authority Aggregator to compute

$$
A (o; Q) = \sum_ {q \in Q} w _ {q} A \Big (o; T _ {q} \Big)\tag{14}
$$

where $T _ { q }$ is the topic matching query keyword q. Next, we describe the time-aware authority model.

## 4.3. Personalization weights and time-aware authority

We have extensively discussed the notion of authority and the idea of computing authority scores for individual topics that can be aggregated at query time. Now we turn to the de<sup>fi</sup>nition of the personalization vectors δ and $\delta _ { 0 } .$ Recall, δ holds personalization weights for projects and $\delta _ { 0 }$ holds personalization weights for organizations. For δ we use a straightforward model to calculate personalization weights

$$
\delta_ {P} (p) = \frac {\text { funding } (p)}{\sum_ {p r o j \in V _ {p}} \text { funding } (p r o j)}\tag{15}
$$

where funding(p) depicts the monetary funding received by project p. For simplicity, we do not consider the query context Q for the projectbased personalization vector.

The next discussion is related to the concept of time-aware and topic-based authority ranking. Thus, we establish metrics to calculate the personalization weights of $\delta _ { O } .$ . Here topic-based personalization and time-aware weighting is applied. Recall that a topic is identi<sup>fi</sup>ed by a single keyword. Organizations typically perform numerous projects that are related to one or more topic(s). Thus, each organization has a set of topics including topic frequency associated with it. Furthermore, frequencies of topics are counted by year. An example for such data would be (“OrgA”, 2011, “services”, 5) where $" \mathrm { O r g } { \tt A } '$ is the organization name, 2011 the speci<sup>fi</sup>c year, “services” the given topic and the number

5 an example of a frequency count. As a <sup>fi</sup>rst step let us de<sup>fi</sup>ne the weight function $W ^ { T } ( o , y ; T _ { x } )$ that obtains the frequency count of organization o in year y for some topic $T _ { x } .$ The frequency count is based on how many projects related to the given topic the organization has started in the year (i.e., the year when signing the project contract). To establish the notion of positive or negative change in topic speci<sup>fi</sup>c weights, we de<sup>fi</sup>ne the weight deviation function $W _ { \Delta } ^ { T } ( o , y ; T _ { x } )$ as follows:

$$
W _ {\Delta} ^ {T} (o, y; T _ {x}) = W ^ {T} (o, y; T _ {x}) - \frac {1}{| Y |} \sum_ {y ^ {\prime} \in Y} W ^ {T} \left(o, y ^ {\prime}; T _ {x}\right)\tag{16}
$$

Deviation in this context means the weight $W ^ { T } ( o , y ; T _ { x } )$ in year y minus the average weight with regard to topic $T _ { x } .$ Straightforwardly, a positive sign means increasing topic-based weight, a negative sign means decreasing topic-based weight as a result of being below the average, and 0 means no change in topic-based weights (i.e., through constant rate of projects related to topic $T _ { x } )$ . This de<sup>fi</sup>nition is quite simple and captures already a notion of ‘trend’ by analyzing the temporal project history of an organization. The positive/negative sign depicts increasing or decreasing trend. However, $W _ { \Delta } ^ { T } ( o , y ; T _ { x } )$ just analyzes the trend with respect to organization o without considering the weights and thus performance of other organizations. Personalization for authority ranking in collaboration networks must be performed by considering weights in relation to all other organizations. For brevity, let us de<sup>fi</sup>ne the set $\alpha = \{ W ^ { T } ( o _ { 1 } , y ; T _ { x } ) , W ^ { T } ( o _ { 2 } , y ; T _ { x } ) , . . . , W ^ { T } ( o _ { n } , y ; T _ { x } ) \}$ with $\{ o _ { 1 } , o _ { 2 } , . . . , o _ { n } \} { \in } V _ { O } .$ . Let us de<sup>fi</sup>ne the trend $T r ( o ; T _ { x } )$ of organization o with respect to topic $T _ { x }$ as:

$$
T r (o; T _ {x}) = \sum_ {y \in Y} w _ {y} \left[ \frac {W ^ {T} (o , y ; T _ {x})}{\max (\alpha)} \times W _ {\Delta} ^ {T} (o, y; T _ {x}) \right].\tag{17}
$$

$T r ( o ; T _ { x } )$ is based on the trend for topic $T _ { x }$ over the years $Y = \{ y _ { 1 } ,$ $y _ { 2 } , . . . , y _ { n } \}$ where $y _ { n }$ is the most recent year, $y _ { n \mathrm { ~ - ~ } 1 }$ the previous year and so forth (ordered by recency). The <sup>fi</sup>rst term within the square brackets measures the topic based weight in relation to the community performance in $T _ { x }$ by dividing $W ^ { T } ( o , y ; T _ { x } )$ by max(α). For the topperforming organizations having the most numbers of projects related to $T _ { x }$ in year y the term becomes 1. The term is multiplied by the organization speci<sup>fi</sup>c weight deviation function $W _ { \Delta } ^ { T } ( o , y ; T _ { x } )$ . The weight $w _ { y }$ puts more emphasis on recent years (recency factor) by being calculated as $\begin{array} { r } { w _ { y } { \in } \Big \{ \frac { 1 } { | Y | } , \frac { 1 } { | Y | - 1 } , \frac { 1 } { | Y | - 2 } , . . . , 1 \Big \} } \end{array}$

Finally, the personalization vector $\delta _ { 0 }$ needs to be assigned by matching organizations having performed projects related to $T _ { x }$ and trend values Tr need to be mapped to a positive interval. This is done because $\delta _ { 0 }$ represents a probability distribution (for theoretical foundations related to personalized PageRank see, for example, [18]). Let us de<sup>fi</sup>ne the set $\beta = \{ T r ( o _ { 1 } ; T _ { x } ) , T r ( o _ { 2 } ; T _ { x } ) , . . . , T r ( o _ { n } ; T _ { x } ) \}$ with $\left\{ 0 _ { 1 } , 0 _ { 2 } , . . . , \right.$ $o _ { n } \} \in V _ { O }$

$$
\delta_ {0} (o; T _ {x}) = \left\{ \begin{array}{l l} 1 - \frac {\max (\beta) - T r (o ; T _ {x})}{\max (\beta) - \min (\beta)} & , \text { if   } \text { matches } (o; T _ {x}) \\ 0 & , \text { otherwise } \end{array} \right.\tag{18}
$$

The function matches $( o ; T _ { x } )$ checks if o has performed projects related to $T _ { x }$ and evaluates to true or false. To evaluate a query $Q = \{ T _ { 1 } , T _ { 2 } \}$ a simple aggregation is performed

$$
A (o; \{T _ {1}, T _ {2} \}) = w _ {1} A (o; T _ {1}) + w _ {2} A (o; T _ {2})\tag{19}
$$

where $A ( o ; T _ { 1 } )$ is personalized for $T _ { 1 }$ and $A ( o ; T _ { 2 } )$ is personalized for $T _ { 2 } .$ In other words, both $A { \left( 0 ; T _ { 1 } \right) }$ and $A ( o ; T _ { 2 } )$ hold topic-based and time-aware authority scores for all $o \in V _ { O } .$

## 5. Structural importance model

The previous section explained in detail the authority model and ranking approach. Here we turn to the second criteria used in our overall ranking model. We de<sup>fi</sup>ne the notion of structural importance and detail a metric to calculate the importance. The obtained ranking scores for structural importance are used as a second parameter in the AHPbased aggregation (i.e., the AHP parameter $S I ( o ; Q ) )$ . By following the notion of structural holes as coined by Burt [5,6], structural holes are an opportunity to broker the <sup>fl</sup>ow of information between people in an organizational or social network. As an example, managers often act as information brokers as they talk to many people in the project.

Structural importance captures the ability of a network node to broker information between its neighbors (in our context organizations). A node can do so if potential ‘information gaps’ (or buffers) arise in the network. A broker can also be seen as a mediator that helps establishing communication between other nodes. A project partner with ‘brokerage’ capabilities is often important in project consortia to help establish and facilitate communication among other partners. As an example, a project consortium may be led by an academic partner who is in charge of coordinating the project from an administrative and scienti<sup>fi</sup>c point of view. Typically, exploitation and further use of project results is an important issue in research projects. However, the consortium leader may not be the optimal partner for transferring (or ‘translating’) scienti<sup>fi</sup>c results to business. Thus, there may be a gap between technical/ scienti<sup>fi</sup>c results and exploitation of results within an industrial context (e.g., implementing novel solutions within an industrial environment). With regards to this example, an organization may act as a broker by mediating communication and transferring the knowledge to an industrial partner within the project.

Thus, structural importance essentially focuses on mediation capabilities of an organization as opposed to expertise/authority. Such mediators help running projects more effectively and ef<sup>fi</sup>ciently by (a) establishing communication between potentially disconnected network segments that have not communicated before and (b) help making communication more <sup>fl</sup>uid and ef<sup>fi</sup>cient. To be able to act as a broker, gaps must exist in the network because otherwise a node loses its ability to establish communication. The notion of redundancy provides means to express the existence of such gaps. If there is high redundancy in terms of network edges and communication paths in a network, the need to <sup>fi</sup>ll structural gaps may be very limited. On the contrary, if a network is highly segmented and only few nodes connect individual segments, the need for brokers and mediation opportunities may be very high.

Let us consider a graph as depicted by Fig. 3. Here the graph model $G _ { O C }$ is used that consists of organizations and collaboration relations as undirected edges. Each node depicts an organization with {a, b, c, o, r, $u , v , z \} \subset V _ { O } .$ A circle surrounds nodes that belong to a particular expertise area or community identi<sup>fi</sup>ed through A and B. A query may be formulated to match the nodes and edges in either $Q ^ { A } { \mathrm { ~ o r ~ } } Q ^ { B }$ or both $Q = Q ^ { A } \cup Q ^ { B } = \{ T _ { A } , T _ { B } \}$ . An edge $( \nu , u ) \in G _ { O C }$ has a weight which is based on the number of performed projects between v and u. The weight is dynamically assigned depending on the query context Q. For example, the weight of the edge $( o , z ) \in G _ { O C }$ may be different in $Q ^ { A }$ and $Q ^ { B }$ depending on the joint projects performed by o and z (i.e., if the projects match $Q ^ { \bar { A } }$ or $Q ^ { B }$ or both). Suppose $Q = Q ^ { A } \cup Q ^ { B } $ , the node tito has the highest number of non-redundant edges in the graph because it connects the node sets $\{ a , b , c \}$ and $\{ u , v , z \}$ which are only reachable via o. Thus, o has a unique position within the network because o is able to control the information <sup>fl</sup>ow between both node sets. Furthermore, only o and z belong to both expertise areas A and B but only o is connected to {a, $b , c \}$ in A. Let us de<sup>fi</sup>ne SI(o;Q) as

![](/api/attachments/JBXEQUXE/fulltext/images/4dc6afc152f5932b35b71ec3c43b2b73c482338f2dbd8c924297db92a5cb4a57.jpg)  
Fig. 3. Network structure to illustrate structural importance metric.

$$
S I (o; Q) = \sum_ {u \in N (o)} \left[ 1 - \sum_ {v \in N (u)} W _ {N} ^ {Q} (o, v; Q) W _ {M} ^ {Q} (u, v; Q) \right]\tag{20}
$$

where v∉ $\{ \mathfrak { u } , { \mathfrak { o } } \}$ and $N ( o )$ the set of o's neighbors. For $S I ( o ; Q )$ , we follow Burt's measure of the effective size of a node's network [6]. Here the notion of structural holes is not applied to people-based social networks, but to organization collaboration networks $( \mathrm { i } . \mathsf { e } . , G _ { O C } )$ . Conceptually, the effective size is the number of nodes o is connected to, minus the redundancy in the network.

In contrast to Burt's de<sup>fi</sup>nition of effective size, we compute structural importance with respect to the query Q. As an example, while o in Fig. 3 is structurally important in $Q = Q ^ { A } \cup Q ^ { B }$ to establish a <sup>fl</sup>ow between {a, b, c} and $\{ u , v , z \}$ , o is less signi<sup>fi</sup>cant if only $Q ^ { B }$ is considered. Actually, within $Q ^ { B }$ u has a unique position because r is only reachable via u.

The weight $W _ { N } ^ { Q } ( o , v ; Q )$ in Eq. (20) depicts the query-sensitive normalized edge weight between o and v and is calculated as

$$
W _ {N} ^ {Q} (o, v; Q) = \sum_ {q \in Q} \frac {w _ {o v} ^ {q}}{\sum_ {u \in N (o)} w _ {o u} ^ {q}}\tag{21}
$$

where $w _ { o \nu } ^ { q }$ is the weight associated with $( o , v ) \in E _ { O }$ and calculated as the number of joint projects between o and v matching the query keyword q. Furthermore, the weight $W _ { M } ^ { Q } ( u , v ; Q )$ in Eq. (20) depicts the querysensitive marginal edge weight between u and v and is calculated as follows:

$$
W _ {M} ^ {Q} (u, v; Q) = \sum_ {q \in Q} \frac {w _ {u v} ^ {q}}{\max \big (\{w _ {u n} ^ {q} | \forall n \in N (u) \} \big)}.\tag{22}
$$

The marginal weight of u with neighbor v is the weight $w _ { u v } ^ { q }$ (also based on the number of matching joint projects between them) divided by u's strongest weight with anyone of its neighbors $N ( u )$ . If none of the projects match q, the weight $w _ { u \nu } ^ { q } = 0$

## 6. Multi-criteria ranking algorithm

Here we discuss the computation of the <sup>fi</sup>nal ranking score. Recall that the composite ranking score $S ( o ; Q )$ of organization o is obtained through $A H P ( A ( o ; Q ) , S I ( o ; Q ) , C ( o ) )$ ). Previously we have de<sup>fi</sup>ned the authority A(o;Q) and the structural importance $S I ( o ; Q )$ . Cost C(o) is calculated as the average funding organization o receives:

$$
C (o) = \frac {1}{\text { num\_projects } (o)} \sum_ {(p, o) \in E _ {p}} \text { funding } (p, o)\tag{23}
$$

The <sup>fi</sup>nal aggregation and computation of a composite ranking score is done using the AHP algorithm. AHP is a technique for making complex decisions in a structured way. AHP has been successfully applied in a number of <sup>fi</sup>elds including transportation [12], maintenance and con<sup>fi</sup>gurations $[ 8 ] ,$ and service quality assessment [12]. The theoretical background will not be covered in this work since AHP is a well explored technique. We refer the reader to [29] for details regarding AHP as a decision making technique.

Algorithm 1 shows the main steps at a high level. The input of the algorithm is given as the query Q and the organization-collaboration graph $G _ { O C } .$ . The graph $G _ { O C }$ is used to compute the structural importance scores in an online manner. Next four essential steps are performed: (1) create map with criteria input scores, (2) set up AHP, (3) perform AHP ranking, and (4) assign <sup>fi</sup>nal AHP ranking scores to output map.

## Algorithm 1. Multi-criteria ranking algorithm

Input: The query $Q$ and the undirected organization-collaboration graph $G _ { O C }$

1. Create map for org with individual scores. For each organization $o \in V _ { O }$ do:

• A(o) ← au\_score(o,Q)) //authority

• SI(o) ← si\_score(o,G<sub>OC</sub>,Q) //struct. imp.

$C ( o )  a v g \_ c o s t ( o ) / / c o s t$

• Add to map $( o , \{ A ( o ) , S I ( o ) , C ( o ) \} )$

2. Setup AHP attributes weights and desirability.

• Auth. attributes $( " \mathrm { a u t h o r i t y " } , \{ w _ { a u } , + 1 \} )$

• Struct. attributes $( " \mathrm { s t r u c t u r e " } , \{ w _ { s i } , + 1 \} )$

• Cost attributes $( " \mathrm { c o s t } " , \{ w _ { c o s t } , - 1 \} )$

3. Perform AHP ranking using output from previous steps.

• Compute the vector of criteria weights.

• Compute the matrix of organization scores.

• Rank the organizations.

4. Assign <sup>fi</sup>nal AHP ranking scores to map S. For each organization $o \in V _ { O }$ do:

• S(o) ← ahp\_score(o)) //<sup>fi</sup>nal score

Output: Ranked organizations based on query Q and according to composite AHP ranking score.

First, the ranking criteria scores are obtained as described in the previous sections (authority Section 4 and structural importance Section 5 respectively). These include authority, structural importance and cost. Using a map, each criteria score is associated with an organization. The map generated in this step is passed as an argument to the AHP ranking in step 3.

Second, AHP attributes are setup by assigning the weights $w _ { a u } , w _ { s i }$ $w _ { c o s t }$ to each criteria with $[ \sum _ { w } w ] = 1$ . In addition, the desirability attribute is assigned to denote if a certain criterion is desired or not. In particular, authority and structural importance should be high (desirability=+1) to obtain a better AHP ranking score whereas cost should be low to obtain a better ranking score (desirability = −1).

Third, AHP ranking is performed by using the previously setup attributes and the output map of step 1. The step 3 of Algorithm 1 is decomposed into the following steps:

• Compute the vector of criteria weights: In this step rating of the relative priority of the criteria is done by assigning a weight value to the more important criteria. The weight values are taken from the previous step of the algorithm (step 2). The weight assignment is done through a pairwise comparison of the criteria. After that, the resulting weights are normalized and the average is computed for each criterion.

• Compute the matrix of organizations scores: Here the score for each organization is determined by computing how well organization o meets some criterion Y. Afterwards, the organizations' scores are normalized and averaged.

• Rank the organizations: In a <sup>fi</sup>nal step the organizations' scores are combined with the criterion weights to produce an overall score for each organization. The extent to which the organizations satisfy the criteria is weighted according to the relative importance of the criteria. The <sup>fi</sup>nal score is simply computed as a weighted sum.

Table 1  
Popular project topics and frequencies.

<table><tr><td>Topic</td><td>Frequency</td></tr><tr><td>Systems</td><td>4126</td></tr><tr><td>Internet</td><td>2729</td></tr><tr><td>Networks</td><td>1771</td></tr><tr><td>Services</td><td>1247</td></tr><tr><td>Software</td><td>1224</td></tr><tr><td>Health</td><td>1115</td></tr><tr><td>Embedded</td><td>1054</td></tr><tr><td>Transport</td><td>890</td></tr><tr><td>Efficiency</td><td>849</td></tr><tr><td>Energy</td><td>849</td></tr></table>

Note, in our case criteria are contrasting by demanding that organizations should have high authority but low cost. In general, the organization that is recommended for selection (top-ranked in <sup>fi</sup>nal output S) is not necessarily the one which optimizes each single criterion, but rather the organization which achieves the most suitable trade-off among the different criteria. This behavior makes AHP a very <sup>fl</sup>exible and powerful tool for multi-criteria partner selection.

Fourth, the AHP scores are saved in a <sup>fi</sup>nal score map S. Organizations are ranked in descending order by ranking score.

## 7. Evaluation

Here the evaluation of the proposed concepts and model is presented. We have selected a dataset of a scienti<sup>fi</sup>c collaboration environment to test the concepts.

## 7.1. Description of dataset

The data is based on ICT research projects having received grants under the EU's Seventh Framework Programme (FP7). The data as described in detail in [25] and covers a period from 2007 to 2011. Research projects have multiple partners and an organization can be the partner of multiple projects. To date, the FP7 ICT program has allocated funding to 1469 projects for a total Union funding of 4,979,301,152 Euro. This results in 14,781 participations by 4718 distinct legal entities.

Our evaluation is performed as follows. First we select the top-20 organizations (ranked by degree and given in Table 2) and compute metrics for those 20 organizations with regard to popular topics. This evaluation is called top-k rank evaluation and is presented in Section 7.2. Second we compute cross topic ranking statistics such as overlap similarity and Kendall's τ rank difference. This evaluation is presented in Section 7.3 alongwith the de<sup>fi</sup>nition of relevant ranking metrics.

Table 1 gives an overview of popular (project) topics extracted from project information (see [25] for details). Frequency is measured by counting appearance of the topic string within project names and project short descriptions of each project partner involvement record (association of organization to project including received funding). In total, we extracted 170 topics after performing some automatic and manual processing of the data. Table 1 shows the top-10 topics with the highest frequencies among the 170 topics.

## 7.2. Top-k rank evaluation

Table 2 shows the top-20 organizations ranked by their degree in $G _ { P O }$ (project-organization graph). The <sup>fi</sup>rst column (PNr column) is a unique key associated with an organization and used throughout this section to identify a top-20 organization. The second column (Name column) depicts the organizations' legal name. The third column (Cost column) shows the average organization cost using Eq. (23). The organization in degree (Degree column) is analog to the project count as projects $p \in V _ { P }$ point to organizations $o \in V _ { O } .$ The degree-based rank will be used as a baseline ranking. This baseline results will be compared with AHP-based rankings. We have selected the degree-based rank as a baseline algorithm to show the impact of personalization based on topic information and time-aware authority ranking. Notice, the degreebased rank has no topic bias. In addition, the degree-based rank was selected because it already captures some notion of importance with regard to organization reputation. The last column (Structural Rank Score column) shows the structural rank score (using Eq. (20)) over all topics in Table 1. A higher score is better.

It is noticeable that the organization 14 has a particular high structural rank score in relation to its degree-based rank position. Organization 1 has an exceptionally high structural rank score but has also the most projects within the ICT framework program. Notice, however, the degree is calculated using G and the structural rank using $G _ { O C } .$

To compare AHP results with the rankings in Tables 2, 3 and 4 list detailed metrics for selected topics. We have selected eight out of the ten topics from Table 1 due to space reasons.

Table 2  
Top-20 organizations ranked by degree.

<table><tr><td>PNr</td><td>Name</td><td>Cost</td><td>Degree</td><td>Structural rank score</td></tr><tr><td>1</td><td>Fraunhofer-Gesellschaft zur Foerderung der Angewandten Forschung E.V.</td><td>524,515</td><td>272</td><td>516</td></tr><tr><td>2</td><td>Centre National de la Recherche Scientifique</td><td>159,983</td><td>153</td><td>175</td></tr><tr><td>3</td><td>Commissariat à l&#x27;Énergie Atomique et Aux Energies Alternatives</td><td>235,911</td><td>137</td><td>201</td></tr><tr><td>4</td><td>Ecole Polytechnique Federale de Lausanne</td><td>290,827</td><td>97</td><td>146</td></tr><tr><td>5</td><td>Consiglio Nazionale delle Ricerche</td><td>455,650</td><td>96</td><td>154</td></tr><tr><td>6</td><td>Valtion Teknillinen Tutkimuskeskus</td><td>293,240</td><td>95</td><td>190</td></tr><tr><td>7</td><td>Institut National de Recherche en Informatique et en Automatique</td><td>799,995</td><td>94</td><td>127</td></tr><tr><td>8</td><td>Interuniversitair Micro-Electronica Centrum Vzw</td><td>964,195</td><td>90</td><td>140</td></tr><tr><td>9</td><td>Eidgenoessische Technische Hochschule Zurich</td><td>389,544</td><td>90</td><td>89</td></tr><tr><td>10</td><td>Telefonica Investigacion Y Desarrollo S.A.</td><td>636,818</td><td>76</td><td>131</td></tr><tr><td>11</td><td>Katholieke Universiteit Leuven</td><td>711,085</td><td>69</td><td>98</td></tr><tr><td>12</td><td>SAP AG</td><td>1,221,665</td><td>68</td><td>168</td></tr><tr><td>13</td><td>Universidad Politecnica de Madrid</td><td>331,315</td><td>65</td><td>136</td></tr><tr><td>14</td><td>Atos Origin Sociedad Anonima Espanola</td><td>628,296</td><td>62</td><td>215</td></tr><tr><td>15</td><td>Imperial College of Science, Technology and Medicine</td><td>286,930</td><td>61</td><td>56</td></tr><tr><td>16</td><td>Politecnico di Milano</td><td>531,975</td><td>61</td><td>98</td></tr><tr><td>17</td><td>Kungliga Tekniska Hoegskolan</td><td>415,684</td><td>59</td><td>85</td></tr><tr><td>18</td><td>Technische Universiteit Delft</td><td>622,286</td><td>58</td><td>88</td></tr><tr><td>19</td><td>Karlsruher Institut Fuer Technologie</td><td>250,599</td><td>56</td><td>76</td></tr><tr><td>20</td><td>Technische Universitaet Wien</td><td>287,363</td><td>55</td><td>87</td></tr></table>

Table 3  
Top-20 list of organizations: topics include ‘networks’, ‘systems’, ‘software’, and ‘services’.

<table><tr><td rowspan="2">PNr</td><td colspan="5">Networks</td><td colspan="5">Systems</td><td colspan="5">Software</td><td colspan="5">Services</td></tr><tr><td>D</td><td>A</td><td>P</td><td>Ch</td><td>Tr</td><td>D</td><td>A</td><td>P</td><td>Ch</td><td>Tr</td><td>D</td><td>A</td><td>P</td><td>Ch</td><td>Tr</td><td>D</td><td>A</td><td>P</td><td>Ch</td><td>Tr</td></tr><tr><td>1</td><td>29</td><td>0.11</td><td>1</td><td>2</td><td>1.08</td><td>70</td><td>0.86</td><td>1</td><td>0</td><td>7.97</td><td>7</td><td>0.15</td><td>2</td><td>3</td><td>0.23</td><td>11</td><td>0.04</td><td>5</td><td>28</td><td>-0.03</td></tr><tr><td>2</td><td>10</td><td>0.03</td><td>31</td><td>677</td><td>-0.13</td><td>39</td><td>0.00</td><td>16</td><td>196</td><td>-0.03</td><td>3</td><td>0.04</td><td>12</td><td>27</td><td>0.00</td><td>3</td><td>0.04</td><td>15</td><td>35</td><td>0.00</td></tr><tr><td>3</td><td>20</td><td>0.05</td><td>12</td><td>25</td><td>0.19</td><td>44</td><td>0.10</td><td>5</td><td>4</td><td>0.79</td><td>1</td><td>0.04</td><td>7</td><td>20</td><td>0.00</td><td>1</td><td>0.04</td><td>10</td><td>28</td><td>0.00</td></tr><tr><td>4</td><td>5</td><td>0.03</td><td>30</td><td>665</td><td>-0.05</td><td>26</td><td>0.01</td><td>19</td><td>87</td><td>0.01</td><td>1</td><td>0.04</td><td>16</td><td>27</td><td>0.00</td><td>2</td><td>0.04</td><td>17</td><td>34</td><td>0.00</td></tr><tr><td>5</td><td>4</td><td>0.05</td><td>16</td><td>27</td><td>0.17</td><td>19</td><td>0.15</td><td>3</td><td>-1</td><td>1.44</td><td>6</td><td>0.06</td><td>10</td><td>6</td><td>0.04</td><td>7</td><td>0.04</td><td>11</td><td>13</td><td>0.06</td></tr><tr><td>6</td><td>12</td><td>0.07</td><td>6</td><td>5</td><td>0.56</td><td>20</td><td>0.05</td><td>8</td><td>15</td><td>0.39</td><td>1</td><td>0.04</td><td>9</td><td>19</td><td>0.00</td><td>7</td><td>0.02</td><td>25</td><td>630</td><td>-0.18</td></tr><tr><td>7</td><td>16</td><td>0.09</td><td>5</td><td>-2</td><td>0.85</td><td>25</td><td>0.08</td><td>10</td><td>5</td><td>0.73</td><td>7</td><td>0.04</td><td>18</td><td>44</td><td>-0.01</td><td>9</td><td>0.04</td><td>22</td><td>618</td><td>-0.02</td></tr><tr><td>8</td><td>6</td><td>0.04</td><td>27</td><td>61</td><td>0.01</td><td>27</td><td>0.14</td><td>6</td><td>-3</td><td>1.21</td><td>0</td><td>0.01</td><td>42</td><td>357</td><td>0.00</td><td>1</td><td>0.04</td><td>19</td><td>25</td><td>0.00</td></tr><tr><td>9</td><td>7</td><td>0.04</td><td>32</td><td>31</td><td>0.10</td><td>33</td><td>0.09</td><td>12</td><td>-1</td><td>0.87</td><td>1</td><td>0.04</td><td>29</td><td>18</td><td>0.00</td><td>1</td><td>0.04</td><td>34</td><td>27</td><td>0.00</td></tr><tr><td>10</td><td>38</td><td>0.00</td><td>681</td><td>671</td><td>-0.55</td><td>6</td><td>0.01</td><td>26</td><td>67</td><td>0.06</td><td>11</td><td>0.01</td><td>37</td><td>353</td><td>-0.07</td><td>12</td><td>0.04</td><td>18</td><td>16</td><td>0.03</td></tr><tr><td>11</td><td>3</td><td>0.03</td><td>57</td><td>661</td><td>-0.05</td><td>23</td><td>0.05</td><td>18</td><td>8</td><td>0.48</td><td>2</td><td>0.04</td><td>25</td><td>25</td><td>0.00</td><td>2</td><td>0.04</td><td>32</td><td>32</td><td>0.00</td></tr><tr><td>12</td><td>7</td><td>0.07</td><td>7</td><td>2</td><td>0.51</td><td>6</td><td>0.01</td><td>15</td><td>56</td><td>0.06</td><td>17</td><td>0.22</td><td>3</td><td>-10</td><td>0.43</td><td>18</td><td>0.17</td><td>2</td><td>-10</td><td>1.25</td></tr><tr><td>13</td><td>6</td><td>0.06</td><td>13</td><td>6</td><td>0.38</td><td>12</td><td>0.01</td><td>22</td><td>67</td><td>0.06</td><td>10</td><td>0.03</td><td>20</td><td>349</td><td>-0.03</td><td>11</td><td>0.00</td><td>636</td><td>625</td><td>-0.34</td></tr><tr><td>14</td><td>9</td><td>0.10</td><td>3</td><td>-10</td><td>1.06</td><td>5</td><td>0.02</td><td>9</td><td>38</td><td>0.12</td><td>7</td><td>0.05</td><td>5</td><td>1</td><td>0.03</td><td>11</td><td>0.11</td><td>3</td><td>-9</td><td>0.72</td></tr><tr><td>15</td><td>0</td><td>0.00</td><td>689</td><td>667</td><td>0.00</td><td>19</td><td>0.04</td><td>42</td><td>13</td><td>0.38</td><td>1</td><td>0.04</td><td>57</td><td>28</td><td>0.00</td><td>2</td><td>0.04</td><td>59</td><td>31</td><td>0.00</td></tr><tr><td>16</td><td>3</td><td>0.04</td><td>44</td><td>88</td><td>0.00</td><td>22</td><td>0.07</td><td>14</td><td>-3</td><td>0.66</td><td>5</td><td>0.05</td><td>19</td><td>-2</td><td>0.03</td><td>5</td><td>0.04</td><td>30</td><td>16</td><td>0.02</td></tr><tr><td>17</td><td>9</td><td>0.04</td><td>42</td><td>48</td><td>0.04</td><td>19</td><td>0.09</td><td>13</td><td>-8</td><td>0.83</td><td>1</td><td>0.04</td><td>34</td><td>21</td><td>0.00</td><td>1</td><td>0.04</td><td>37</td><td>25</td><td>0.00</td></tr><tr><td>18</td><td>3</td><td>0.03</td><td>60</td><td>642</td><td>-0.03</td><td>25</td><td>0.15</td><td>7</td><td>-15</td><td>1.48</td><td>0</td><td>0.00</td><td>101</td><td>348</td><td>0.00</td><td>2</td><td>0.04</td><td>36</td><td>26</td><td>0.00</td></tr><tr><td>19</td><td>2</td><td>0.04</td><td>65</td><td>84</td><td>0.00</td><td>17</td><td>0.02</td><td>49</td><td>26</td><td>0.18</td><td>1</td><td>0.04</td><td>45</td><td>33</td><td>0.00</td><td>1</td><td>0.04</td><td>47</td><td>33</td><td>0.00</td></tr><tr><td>20</td><td>3</td><td>0.04</td><td>52</td><td>96</td><td>0.00</td><td>17</td><td>0.02</td><td>40</td><td>30</td><td>0.15</td><td>3</td><td>0.04</td><td>32</td><td>6</td><td>0.01</td><td>5</td><td>0.06</td><td>13</td><td>-9</td><td>0.20</td></tr><tr><td>D</td><td>1.0</td><td>0.2</td><td>0.3</td><td>0.0</td><td>0.1</td><td>1.0</td><td>0.8</td><td>-0.4</td><td>-0.1</td><td>0.8</td><td>1.0</td><td>0.6</td><td>-0.4</td><td>0.1</td><td>0.6</td><td>1.0</td><td>0.5</td><td>0.2</td><td>0.3</td><td>0.5</td></tr><tr><td>A</td><td></td><td>1.0</td><td>-0.6</td><td>-0.7</td><td>1.0</td><td></td><td>1.0</td><td>-0.4</td><td>-0.3</td><td>1.0</td><td></td><td>1.0</td><td>-0.5</td><td>-0.5</td><td>1.0</td><td></td><td>1.0</td><td>-0.4</td><td>-0.4</td><td>1.0</td></tr><tr><td>P</td><td></td><td></td><td>1.0</td><td>0.6</td><td>-0.5</td><td></td><td></td><td>1.0</td><td>0.2</td><td>-0.4</td><td></td><td></td><td>1.0</td><td>0.5</td><td>-0.4</td><td></td><td></td><td>1.0</td><td>0.5</td><td>-0.3</td></tr><tr><td>Ch</td><td></td><td></td><td></td><td>1.0</td><td>-0.6</td><td></td><td></td><td></td><td>1.0</td><td>-0.3</td><td></td><td></td><td></td><td>-0.3</td><td>0.0</td><td></td><td></td><td></td><td>1.0</td><td>-0.4</td></tr></table>

Each metric is computed for each topic in Tables 3 and 4 respectively. Using $G _ { P O } ,$ the degree D is based on matching projects only. Projects are matched against the given topic as depicted in the headings of Tables 3 and 4. The authority A is calculated for respective topics. The position P is the rank position index as obtained by the AHP rank using Eq. (1).

AHP is setup with the weights 0.4 for authority, 0.2 for the structural importance rank and 0.4 for cost. Thus, authority and cost are given slightly higher weights than structural importance. We regard authority as highly desirable but at the same time cost should be kept at an acceptable level. After that structural importance is also a desirable property but not equally important as the other criteria. However, since our approach is <sup>fl</sup>exible weights can be adjusted as demanded.

The position change Ch is computed between degree-based ranking positions and authority based ranking positions in the following manner

$$
C h (o) = \text { pos } (A (o; T _ {x})) - \text { pos } (\text { degree\_rank } (o))\tag{24}
$$

where pos() retrieves the position index by ranking score. This lets us show how rankings are in<sup>fl</sup>uenced by authority. Finally, the trend Tr is computed by using the Eq. (17). As state before, the sign has the following meaning:

Top-20 list of organizations: topics include ‘health’, ‘embedded’, ‘internet’, and ‘energy’.

<table><tr><td rowspan="2">PNr</td><td colspan="5">Health</td><td colspan="5">Embedded</td><td colspan="5">Internet</td><td colspan="5">Energy</td></tr><tr><td>D</td><td>A</td><td>P</td><td>Ch</td><td>Tr</td><td>D</td><td>A</td><td>P</td><td>Ch</td><td>Tr</td><td>D</td><td>A</td><td>P</td><td>Ch</td><td>Tr</td><td>D</td><td>A</td><td>P</td><td>Ch</td><td>Tr</td></tr><tr><td>1</td><td>12</td><td>0.05</td><td>3</td><td>22</td><td>0.07</td><td>11</td><td>0.12</td><td>2</td><td>10</td><td>0.51</td><td>47</td><td>0.04</td><td>3</td><td>11</td><td>0.47</td><td>17</td><td>0.43</td><td>1</td><td>0</td><td>0.56</td></tr><tr><td>2</td><td>7</td><td>0.06</td><td>10</td><td>9</td><td>0.26</td><td>12</td><td>0.23</td><td>4</td><td>1</td><td>1.22</td><td>14</td><td>0.03</td><td>24</td><td>1040</td><td>-0.21</td><td>0</td><td>0.00</td><td>25</td><td>609</td><td>0.00</td></tr><tr><td>3</td><td>3</td><td>0.06</td><td>11</td><td>14</td><td>0.19</td><td>15</td><td>0.27</td><td>3</td><td>-1</td><td>1.38</td><td>23</td><td>0.03</td><td>8</td><td>33</td><td>0.12</td><td>3</td><td>0.05</td><td>10</td><td>12</td><td>0.01</td></tr><tr><td>4</td><td>5</td><td>0.07</td><td>9</td><td>5</td><td>0.30</td><td>8</td><td>0.04</td><td>23</td><td>41</td><td>0.04</td><td>8</td><td>0.03</td><td>21</td><td>114</td><td>-0.02</td><td>4</td><td>0.03</td><td>14</td><td>24</td><td>0.00</td></tr><tr><td>5</td><td>8</td><td>0.06</td><td>14</td><td>11</td><td>0.21</td><td>1</td><td>0.03</td><td>25</td><td>49</td><td>0.00</td><td>11</td><td>0.03</td><td>15</td><td>36</td><td>0.13</td><td>3</td><td>0.04</td><td>12</td><td>14</td><td>0.01</td></tr><tr><td>6</td><td>4</td><td>0.04</td><td>20</td><td>37</td><td>0.00</td><td>3</td><td>0.03</td><td>19</td><td>46</td><td>0.01</td><td>15</td><td>0.05</td><td>6</td><td>5</td><td>0.67</td><td>14</td><td>0.08</td><td>7</td><td>3</td><td>0.07</td></tr><tr><td>7</td><td>6</td><td>0.03</td><td>37</td><td>699</td><td>-0.05</td><td>12</td><td>0.21</td><td>5</td><td>-2</td><td>1.07</td><td>27</td><td>0.05</td><td>7</td><td>0</td><td>0.83</td><td>2</td><td>0.03</td><td>19</td><td>24</td><td>0.00</td></tr><tr><td>8</td><td>0</td><td>0.00</td><td>714</td><td>706</td><td>0.00</td><td>10</td><td>0.05</td><td>20</td><td>25</td><td>0.11</td><td>6</td><td>0.03</td><td>20</td><td>65</td><td>0.01</td><td>0</td><td>0.00</td><td>49</td><td>602</td><td>0.00</td></tr><tr><td>9</td><td>9</td><td>0.02</td><td>710</td><td>703</td><td>-0.16</td><td>11</td><td>0.02</td><td>59</td><td>506</td><td>-0.05</td><td>9</td><td>0.03</td><td>33</td><td>57</td><td>0.05</td><td>1</td><td>0.03</td><td>32</td><td>20</td><td>0.00</td></tr><tr><td>10</td><td>1</td><td>0.04</td><td>28</td><td>34</td><td>0.00</td><td>2</td><td>0.03</td><td>33</td><td>48</td><td>0.00</td><td>54</td><td>0.00</td><td>1044</td><td>1034</td><td>-1.41</td><td>2</td><td>0.03</td><td>17</td><td>20</td><td>0.00</td></tr><tr><td>11</td><td>5</td><td>0.04</td><td>25</td><td>15</td><td>0.07</td><td>2</td><td>0.03</td><td>41</td><td>48</td><td>0.00</td><td>5</td><td>0.03</td><td>29</td><td>52</td><td>0.07</td><td>2</td><td>0.03</td><td>26</td><td>23</td><td>0.00</td></tr><tr><td>12</td><td>0</td><td>0.00</td><td>713</td><td>703</td><td>0.00</td><td>5</td><td>0.04</td><td>17</td><td>28</td><td>0.08</td><td>28</td><td>0.09</td><td>2</td><td>-10</td><td>2.60</td><td>6</td><td>0.21</td><td>2</td><td>-10</td><td>0.27</td></tr><tr><td>13</td><td>12</td><td>0.06</td><td>13</td><td>0</td><td>0.25</td><td>5</td><td>0.07</td><td>14</td><td>7</td><td>0.26</td><td>18</td><td>0.03</td><td>23</td><td>61</td><td>0.04</td><td>2</td><td>0.03</td><td>16</td><td>22</td><td>0.00</td></tr><tr><td>14</td><td>4</td><td>0.04</td><td>19</td><td>38</td><td>0.00</td><td>0</td><td>0.00</td><td>24</td><td>510</td><td>0.00</td><td>20</td><td>0.12</td><td>1</td><td>-13</td><td>4.42</td><td>5</td><td>0.04</td><td>9</td><td>6</td><td>0.01</td></tr><tr><td>15</td><td>9</td><td>0.11</td><td>4</td><td>-11</td><td>0.67</td><td>5</td><td>0.06</td><td>29</td><td>7</td><td>0.23</td><td>1</td><td>0.03</td><td>77</td><td>95</td><td>0.00</td><td>3</td><td>0.06</td><td>18</td><td>-2</td><td>0.05</td></tr><tr><td>16</td><td>4</td><td>0.04</td><td>34</td><td>32</td><td>0.00</td><td>9</td><td>0.04</td><td>32</td><td>23</td><td>0.10</td><td>8</td><td>0.03</td><td>27</td><td>33</td><td>0.12</td><td>3</td><td>0.03</td><td>24</td><td>16</td><td>0.00</td></tr><tr><td>17</td><td>0</td><td>0.00</td><td>720</td><td>699</td><td>0.00</td><td>9</td><td>0.05</td><td>28</td><td>14</td><td>0.15</td><td>10</td><td>0.03</td><td>39</td><td>52</td><td>0.05</td><td>0</td><td>0.00</td><td>163</td><td>597</td><td>0.00</td></tr><tr><td>18</td><td>3</td><td>0.04</td><td>31</td><td>12</td><td>0.04</td><td>10</td><td>0.15</td><td>10</td><td>-9</td><td>0.72</td><td>4</td><td>0.03</td><td>42</td><td>88</td><td>0.00</td><td>0</td><td>0.00</td><td>137</td><td>595</td><td>0.00</td></tr><tr><td>19</td><td>3</td><td>0.04</td><td>44</td><td>40</td><td>0.00</td><td>6</td><td>0.11</td><td>12</td><td>-5</td><td>0.54</td><td>3</td><td>0.03</td><td>60</td><td>120</td><td>0.00</td><td>4</td><td>0.05</td><td>21</td><td>-5</td><td>0.02</td></tr><tr><td>20</td><td>4</td><td>0.06</td><td>15</td><td>-10</td><td>0.27</td><td>11</td><td>0.02</td><td>60</td><td>494</td><td>-0.04</td><td>8</td><td>0.03</td><td>52</td><td>1004</td><td>-0.04</td><td>2</td><td>0.03</td><td>36</td><td>35</td><td>0.00</td></tr><tr><td>D</td><td>1.0</td><td>0.6</td><td>-0.4</td><td>-0.3</td><td>0.4</td><td>1.0</td><td>0.7</td><td>-0.2</td><td>-0.1</td><td>0.6</td><td>1.0</td><td>0.1</td><td>0.6</td><td>0.2</td><td>0.1</td><td>1.0</td><td>0.8</td><td>-0.4</td><td>-0.4</td><td>0.8</td></tr><tr><td>A</td><td></td><td>1.0</td><td>-0.8</td><td>-0.8</td><td>0.9</td><td></td><td>1.0</td><td>-0.7</td><td>-0.4</td><td>1.0</td><td></td><td>1.0</td><td>-0.4</td><td>-0.4</td><td>1.0</td><td></td><td>0.8</td><td>-0.4</td><td>-0.4</td><td>0.8</td></tr><tr><td>P</td><td></td><td></td><td>1.0</td><td>0.9</td><td>-0.4</td><td></td><td></td><td>1.0</td><td>0.7</td><td>-0.7</td><td></td><td></td><td>1.0</td><td>0.6</td><td>-0.4</td><td></td><td></td><td>1.0</td><td>0.7</td><td>-0.3</td></tr><tr><td>Ch</td><td></td><td></td><td></td><td>1.0</td><td>-0.5</td><td></td><td></td><td></td><td>1.0</td><td>-0.4</td><td></td><td></td><td></td><td>1.0</td><td>-0.4</td><td></td><td></td><td></td><td>1.0</td><td>-0.2</td></tr></table>

The rank position index as obtained by the AHP rank is depicted as bold face entry.

$$
T r = \left\{ \begin{array}{l l} \text { positive   sign } & , \text { if   trend   is   increasing } \\ \text { negative   sign } & , \text { if   trend   is   decreasing } \\ 0 & , \text { otherwise. } \end{array} \right.
$$

To show the relationship between two metrics, at the bottom of Tables 3 and 4 we show the correlation coef<sup>fi</sup>cient among various metrics. As usual, the correlation coef<sup>fi</sup>cient takes a value between [−1, 1], with 1 or −1 indicating perfect correlation. A positive correlation depicts a positive association between the variables. Thus, increasing values of one variable correspond to increasing values of the other variable. On the other hand, negative correlation indicates a negative association between the variables. Thus, increasing values of one variable correspond to decreasing values of the other variable. A correlation value close to 0 indicates no association between the variables.

Table 3 shows the results for the topics ‘networks’, ‘systems’, ‘software’, and ‘services’. The organization PNr 1 has been ranked by AHP at position 1 in ‘networks’, position 1 in ‘systems’, position 2 in ‘software’, and position5 in ‘services’. With regards to ‘services’, a negative trend is shown for PNr 1 and thus the position has dropped in this topic. In the other topics, positive trend can be observed and thus the ranking position was mostly preserved. With regards to the topic ‘systems’, a very good trend of 7.97 can be observed and highest authority score of 0.86 within the table. As one can see, by applying our approach, much more <sup>fi</sup>ne-grained ranking can be performed by considering topic information.

With regards to correlation, A always correlates perfectly with Tr because time-aware authority takes trend through personalization into account. D shows good correlation with Tr in the topic ‘systems’. This is a result of the broad scope of ‘systems’ and the high frequency of the topic within projects (see also Table 1).

Table 4 shows the results for the topics ‘health’, ‘embedded’, ‘internet’, and ‘energy’. The organization PNr 1 was only ranked in ‘energy’ at position 1 but not for the other topics. One exceptionally high change in the ranking position can be seen for organization PNr 10 in ‘internet’ which ranks by AHP at 1044. PNr 10 had some substantial amounts of projects with regard to ‘internet’ in the past (54 matching projects as indicated by D) but the trend is highly negative (Tr is −1.41, which is the lowest in the table) and time-aware A is 0.00. Thus, we believe that negative trend and limited recent activity in the context ‘internet’ justi<sup>fi</sup>es a change in the rank position.

With regards to correlation, A correlates perfectly only in ‘embedded’ and ‘internet’ but not for the other topics (although a high correlation is still achieved). D shows good correlation with Tr in the topic ‘energy’. As in Table 3, A shows good correlation with P. Indeed, authority is part of AHP's ranking criteria so a correlation can be expected. Recall, higher authority yields better positions. Thus, negative correlation means increasing values of authority correspond to decreasing values of the rank position (lower position value is better).

Based on the data in Tables 3 and 4, average values of degree, position, and change are depicted in Fig. 4 and average values of authority and trend are shown in Fig. 5. Average values are based on the metric values of the top-20 list of organizations. Again, the baseline algorithm for ranking is the degree-based rank.

The topic ‘networks’ has the highest average value with regard to change. Thus, AHP rankings based on topic information have signi<sup>fi</sup>cant impact on the ranking position of organizations and a lot of changes are observed within the top-20 list. Also the topics ‘health’ and ‘internet’ yield high changes on average. However, only ‘health’ yields also high average values with regards to position. This means that organizations ranked within top-20 positions by the degree-based rank would be ranked at much higher positions by AHP in the ‘health’ topic. As mentioned before, since ‘systems’ is a very broad topic also the positions by AHP are quite similar when compared with the degree-based rank (the lowest average value as depicted by Fig. 4). The average degree does not signi<sup>fi</sup>cantly change across topics. Generally, topic based personalization has the effect that signi<sup>fi</sup>cant changes of rank position can be expected.

![](/api/attachments/JBXEQUXE/fulltext/images/6f07b67d55b64e1ccb99f98e0639da635dc58b1d51ac0f00629ca64229f3286b.jpg)  
Fig. 4. Average degree, position, and change.

Next, Fig. 5 shows the average values for authority and trend. The topic ‘systems’ shows the highest average authority and the highest average trend. This observation is also consistent with the previous discussion. The topic ‘software’ shows the lowest trend and also a low average value for authority. In general, deviations in authority across topics are very high.

To summarize the main observations in this section:

• Our proposed model enables more <sup>fi</sup>ne-grained ranking by considering topic information.

• Authority correlates to a high degree with trend because time-aware authority takes trend through personalization into account.

• Generally, topic based personalization has the effect that signi<sup>fi</sup>cant changes of rank position can be observed.

• Topics that play a role in many projects (having a broad scope) correlate better with degree-based ranking. Thus, no signi<sup>fi</sup>cant changes through personalization can be expected.

• As a consequence of the previous observation, by focusing on narrow and more specialized topics organizations with fewer projects are able to build up authority and are thereby ranked at better positions in those topics.

## 7.3. Statistical comparison

Here a statistical comparison of ranking techniques is performed. In the previous section, a top-20 list of organizations was selected (as ranked by the organizations' degree) and evaluated by using different metrics. In this section we use a set overlap and distance based ranking metric to compare the AHP based results with non-personalized rankings including the degree-based rank, a funding based rank, and the structural rank.

![](/api/attachments/JBXEQUXE/fulltext/images/c13ea842f33ec47ca85aa649f2cf0eea4992df6867e875d580ce9f0782624bd5.jpg)  
Fig. 5. Average authority score and trend.

The funding based rank uses the total amount of funding received by an organization to perform ranking (the higher the total funding the better the rank). The structural importance rank is used in isolation of AHP and compared with the regular AHP using the criteria authority, structural importance, and cost. After that a cross topic comparison is performed by using AHP and authority based rankings and AHP-based rankings personalized for different topics. AHP is setup with the weights 0.4 for authority, 0.2 for the structural importance rank and 0.4 for cost.

To systematically compare results of two ranking algorithms, let us de<sup>fi</sup>ne two standard ranking metrics.

## 7.3.1. OSim@k

To measure similarity of top-k sets, let us de<sup>fi</sup>ne overlap similarity as follows:

$$
\mathrm{OSim} @ \mathrm{k} = \frac {O _ {k 1} \cap O _ {k 2}}{k}.\tag{25}
$$

OSim@k de<sup>fi</sup>nes the overlap similarity of the top-k sets $O _ { k }$ ranked by two algorithms. Each set consists of organizations such that $O _ { k } \subset V _ { O } .$ The <sup>fi</sup>rst algorithm is always AHP, which has been parameterized using the same weights as de<sup>fi</sup>ned previously.

## 7.3.2. Kendall's τ

The next ranking metric used in this work is the well-known Kendall's τ metric (for example, see [30]):

$$
\text { Kendall's } \tau = \frac {2 (\text { num\_concordant } - \text { num\_disconcordant })}{| V _ {0} | (| V _ {0} | - 1)}.\tag{26}
$$

Consider the pair of nodes o,u. The pair is concordant if two rankings agree on the order and disconcordant if both rankings disagree on the order. Denote the number of these pairs by num\_concordant and num\_disconcordant respectively. The total number of pairs is given as <sub>j</sub> <sub>j</sub> <sup>V</sup>O <sub>ð</sub> <sub>Þ</sub> <sub>j</sub> <sub>j</sub> <sup>V</sup>O <sup>−1</sup> . Kendall's τ is de<sup>fi</sup>ned between the interval τ∈[−1,1]. Kendall's τ helps in analyzing if two ranking algorithms are rank similar. If τ equals 1, there are no cases where the pair o, u is ranked in a different order.

Table 5 shows the comparison results of AHP-based rankings (for the top-10 topics in Table 1) and the degree-based, funding-based, and structural importance rank. The highest values for OSim and Kendall's τ are depicted as bold-face numbers. The topic ‘systems’ clearly shows the highest overlap with the other (non-topic based) rankings. OSim@ 10, OSim@20, and OSim@50 show the highest overlap in each topic. This observation is again in line with the previous discussion. Previously ‘systems’ showed the highest average authority and the highest average trend within the top-20 list of organizations. The structural importance rank shows the highest overlap of 0.70 in the top-10 segment (depicted as OSim@10). However, a higher agreement in the rank order as measured through Kendall's τ is given in the topic ‘software’. Kendall's τ is calculated by using the whole list of ranked organizations. Whereas the highest overlap of AHP-based rankings with the degree-based, funding-based, and structural importance rank is given in ‘systems’, higher agreement in terms of Kendall's τ is given in ‘software’.

![](/api/attachments/JBXEQUXE/fulltext/images/7e73fd55036f1a71ce8260b0a0521b89911e44265b6efe3771fae88adde28d93.jpg)  
Fig. 6. OSim and Kendall's τ for comparison of AHP with authority-based rankings (detailed numbers are available in Table 6)

Fig. 6 shows the comparison results of AHP-based rankings (again for the top-10 topics in Table 1) and the authority-based rankings. Here, for each topic ranking is performed using AHP as de<sup>fi</sup>ned in Eq. (1) and authority as de<sup>fi</sup>ned in Eq. (19). The results are then compared using OSim and Kendall's τ. Further details are provided in Table 6. The <sup>fi</sup>rst set of rows (1–10) depicts OSim@10, the second set of rows (11–20) depicts OSim@20, the third set of rows (21–30) depicts OSim@50, and the fourth set of rows (31–40) depicts Kendall's τ.

The values below the matrix diagonal (from top-left to bottom right corner) are all set to 0 because of symmetry. For example, overlap similarity OSim for the topics ‘networks’ and ‘systems’ yields the same results as ‘systems’ and ‘networks’. At the diagonal values comparison of AHP and authority rankings for the same topic was performed. Thus, high overlap and agreement with regard to OSim and Kendall's τ, respectively, can be observed. Fig. 7 shows the average values of OSim@10, OSim@20, OSim@50, and Kendall's τ for each topic. With regard to OSim@10, ‘health’ yields the lowest average overlap similarity. The topics ‘ef<sup>fi</sup>ciency’ and ‘energy’ have the highest overlap similarities in the top-10 segment.

## Table 5

OSim and Kendall's τ for comparison of AHP with degree, funding, and structural rank.

<table><tr><td colspan="2"></td><td>Networks</td><td>Systems</td><td>Software</td><td>Services</td><td>Transport</td><td>Efficiency</td><td>Health</td><td>Embedded</td><td>Internet</td><td>Energy</td></tr><tr><td rowspan="4">Degree</td><td>OSim@10</td><td>0.30</td><td>0.60</td><td>0.40</td><td>0.20</td><td>0.30</td><td>0.30</td><td>0.30</td><td>0.40</td><td>0.40</td><td>0.30</td></tr><tr><td>OSim@20</td><td>0.40</td><td>0.75</td><td>0.55</td><td>0.50</td><td>0.40</td><td>0.55</td><td>0.50</td><td>0.50</td><td>0.40</td><td>0.55</td></tr><tr><td>OSim@50</td><td>0.56</td><td>0.86</td><td>0.72</td><td>0.74</td><td>0.70</td><td>0.78</td><td>0.66</td><td>0.68</td><td>0.70</td><td>0.78</td></tr><tr><td>Kendall&#x27;s τ</td><td>0.44</td><td>0.42</td><td>0.46</td><td>0.45</td><td>0.44</td><td>0.41</td><td>0.41</td><td>0.45</td><td>0.43</td><td>0.41</td></tr><tr><td rowspan="4">Funding</td><td>OSim@10</td><td>0.30</td><td>0.50</td><td>0.50</td><td>0.30</td><td>0.30</td><td>0.40</td><td>0.30</td><td>0.30</td><td>0.40</td><td>0.40</td></tr><tr><td>OSim@20</td><td>0.40</td><td>0.70</td><td>0.50</td><td>0.55</td><td>0.40</td><td>0.55</td><td>0.40</td><td>0.40</td><td>0.60</td><td>0.55</td></tr><tr><td>OSim@50</td><td>0.56</td><td>0.84</td><td>0.76</td><td>0.72</td><td>0.70</td><td>0.76</td><td>0.74</td><td>0.66</td><td>0.70</td><td>0.76</td></tr><tr><td>Kendall&#x27;s τ</td><td>0.63</td><td>0.54</td><td>0.65</td><td>0.64</td><td>0.60</td><td>0.58</td><td>0.61</td><td>0.61</td><td>0.62</td><td>0.58</td></tr><tr><td rowspan="4">Structural</td><td>OSim@10</td><td>0.40</td><td>0.70</td><td>0.60</td><td>0.40</td><td>0.40</td><td>0.60</td><td>0.30</td><td>0.30</td><td>0.50</td><td>0.60</td></tr><tr><td>OSim@20</td><td>0.40</td><td>0.70</td><td>0.65</td><td>0.55</td><td>0.45</td><td>0.60</td><td>0.40</td><td>0.45</td><td>0.60</td><td>0.60</td></tr><tr><td>OSim@50</td><td>0.56</td><td>0.86</td><td>0.80</td><td>0.82</td><td>0.80</td><td>0.84</td><td>0.66</td><td>0.72</td><td>0.68</td><td>0.84</td></tr><tr><td>Kendall&#x27;s τ</td><td>0.48</td><td>0.47</td><td>0.51</td><td>0.49</td><td>0.49</td><td>0.46</td><td>0.46</td><td>0.50</td><td>0.46</td><td>0.46</td></tr></table>

The rank position index as obtained by the AHP rank is depicted as bold face entry.

Table 6  
OSim and Kendall's τ for comparison of AHP with authority-based rankings.

<table><tr><td colspan="2"></td><td>Networks</td><td>Systems</td><td>Software</td><td>Services</td><td>Transport</td><td>Efficiency</td><td>Health</td><td>Embedded</td><td>Internet</td><td>Energy</td></tr><tr><td rowspan="10">OSim@10</td><td>Networks</td><td>0.80</td><td>0.10</td><td>0.30</td><td>0.30</td><td>0.10</td><td>0.30</td><td>0.10</td><td>0.10</td><td>0.80</td><td>0.30</td></tr><tr><td>Systems</td><td>0.00</td><td>0.70</td><td>0.10</td><td>0.10</td><td>0.20</td><td>0.30</td><td>0.00</td><td>0.30</td><td>0.20</td><td>0.30</td></tr><tr><td>Software</td><td>0.00</td><td>0.00</td><td>0.60</td><td>0.40</td><td>0.10</td><td>0.30</td><td>0.00</td><td>0.10</td><td>0.30</td><td>0.30</td></tr><tr><td>Services</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.00</td><td>0.20</td><td>0.00</td><td>0.10</td><td>0.40</td><td>0.20</td></tr><tr><td>Transport</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.30</td><td>0.00</td><td>0.10</td><td>0.00</td><td>0.30</td></tr><tr><td>Efficiency</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.00</td><td>0.10</td><td>0.20</td><td>0.80</td></tr><tr><td>Health</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.20</td><td>0.10</td><td>0.10</td></tr><tr><td>Embedded</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.90</td><td>0.10</td><td>0.10</td></tr><tr><td>Internet</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.70</td><td>0.30</td></tr><tr><td>Energy</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td></tr><tr><td rowspan="10">OSim@20</td><td>Networks</td><td>0.85</td><td>0.25</td><td>0.35</td><td>0.40</td><td>0.15</td><td>0.30</td><td>0.20</td><td>0.20</td><td>0.70</td><td>0.30</td></tr><tr><td>Systems</td><td>0.00</td><td>0.75</td><td>0.25</td><td>0.20</td><td>0.20</td><td>0.35</td><td>0.25</td><td>0.40</td><td>0.30</td><td>0.35</td></tr><tr><td>Software</td><td>0.00</td><td>0.00</td><td>0.65</td><td>0.35</td><td>0.20</td><td>0.35</td><td>0.25</td><td>0.30</td><td>0.40</td><td>0.35</td></tr><tr><td>Services</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.65</td><td>0.10</td><td>0.30</td><td>0.30</td><td>0.20</td><td>0.40</td><td>0.30</td></tr><tr><td>Transport</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.75</td><td>0.40</td><td>0.15</td><td>0.20</td><td>0.20</td><td>0.40</td></tr><tr><td>Efficiency</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.75</td><td>0.25</td><td>0.20</td><td>0.25</td><td>0.75</td></tr><tr><td>Health</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.85</td><td>0.30</td><td>0.20</td><td>0.30</td></tr><tr><td>Embedded</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.85</td><td>0.25</td><td>0.25</td></tr><tr><td>Internet</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.75</td><td>0.35</td></tr><tr><td>Energy</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.75</td></tr><tr><td rowspan="10">OSim@50</td><td>Networks</td><td>0.74</td><td>0.40</td><td>0.48</td><td>0.46</td><td>0.26</td><td>0.42</td><td>0.24</td><td>0.26</td><td>0.70</td><td>0.42</td></tr><tr><td>Systems</td><td>0.00</td><td>0.78</td><td>0.56</td><td>0.56</td><td>0.38</td><td>0.64</td><td>0.48</td><td>0.52</td><td>0.38</td><td>0.64</td></tr><tr><td>Software</td><td>0.00</td><td>0.00</td><td>0.72</td><td>0.64</td><td>0.32</td><td>0.54</td><td>0.42</td><td>0.40</td><td>0.48</td><td>0.54</td></tr><tr><td>Services</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.70</td><td>0.36</td><td>0.52</td><td>0.42</td><td>0.38</td><td>0.50</td><td>0.52</td></tr><tr><td>Transport</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.58</td><td>0.54</td><td>0.40</td><td>0.38</td><td>0.34</td><td>0.54</td></tr><tr><td>Efficiency</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.76</td><td>0.46</td><td>0.42</td><td>0.34</td><td>0.76</td></tr><tr><td>Health</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.70</td><td>0.38</td><td>0.28</td><td>0.54</td></tr><tr><td>Embedded</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.74</td><td>0.28</td><td>0.54</td></tr><tr><td>Internet</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.66</td><td>0.52</td></tr><tr><td>Energy</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.76</td></tr><tr><td rowspan="10">Kendall&#x27;s τ</td><td>Networks</td><td>0.88</td><td>0.43</td><td>0.61</td><td>0.58</td><td>0.52</td><td>0.51</td><td>0.51</td><td>0.56</td><td>0.77</td><td>0.51</td></tr><tr><td>Systems</td><td>0.00</td><td>0.82</td><td>0.52</td><td>0.47</td><td>0.47</td><td>0.48</td><td>0.50</td><td>0.61</td><td>0.43</td><td>0.48</td></tr><tr><td>Software</td><td>0.00</td><td>0.00</td><td>0.84</td><td>0.71</td><td>0.55</td><td>0.57</td><td>0.55</td><td>0.61</td><td>0.66</td><td>0.57</td></tr><tr><td>Services</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.87</td><td>0.59</td><td>0.52</td><td>0.54</td><td>0.55</td><td>0.64</td><td>0.52</td></tr><tr><td>Transport</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.83</td><td>0.52</td><td>0.47</td><td>0.53</td><td>0.50</td><td>0.52</td></tr><tr><td>Efficiency</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.85</td><td>0.46</td><td>0.52</td><td>0.49</td><td>0.85</td></tr><tr><td>Health</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.87</td><td>0.52</td><td>0.48</td><td>0.44</td></tr><tr><td>Embedded</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.85</td><td>0.53</td><td>0.51</td></tr><tr><td>Internet</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.89</td><td>0.47</td></tr><tr><td>Energy</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.85</td></tr></table>

Fig. 9 shows the comparison results of AHP-based rankings for the top-10 topics in Table 1 across topics. This comparison shows how ranking results change by considering different topics. Further details are provided in Table 7.

Rows are segmented in the same manner as already described previously. Values at the matrix diagonal (from top-left to bottom right corner) are all 1. The values below the matrix diagonal are all set to 0 for the previously mentioned reason. Fig. 8 shows the average values of OSim@10, OSim@20, OSim@50, and Kendall's τ for each topic.

![](/api/attachments/JBXEQUXE/fulltext/images/4f99f6ea8a18f98843324c9434bced9d9b5baeb13aa81a8a82d6f661daafc1bf.jpg)  
Fig. 7. Average values of OSim@10, OSim@20, OSim@50, and Kendall's based on Table 6.

In OSim@10 the topic ‘health’ results in the lowest average overlap similarity followed by the topic ‘embedded’, which has also low overlap similarity. In general, higher average values of OSim@10, OSim@20, OSim@50 as well as Kendall's τ can be observed when compared with the previous discussion. Higher values are the result of the same ranking technique being used (AHP-based rankings) and results being compared across topics. Before the AHP-based rankings were compared with authority, which is only one of the ranking criteria being used in AHP.

![](/api/attachments/JBXEQUXE/fulltext/images/dad79b5efe24fccb337c2dfcb1ac8f9256dcd797b5c0a86cae79be8b76f5beea.jpg)  
Fig. 8. Average values of OSim@10, OSim@20, OSim@50, and Kendall's based on Table 7.

![](/api/attachments/JBXEQUXE/fulltext/images/a294752b7cff4f6c1dd027a8f7cda5cf4759ef5b5da12ecd9725f0bb115c05e8.jpg)  
Fig. 9. OSim and Kendall's τ for comparison of AHP-based rankings across topics (detailed numbers are available in Table 7).

Overall, the overlap in the top-10 segment is on average 42%, in the top-20 segment 49%, and in the top-50 segment 69%. This means that around 6 out of 10 organizations in the top-10 would be ranked differently across topics. Thus, personalization using topic information has a strong impact on ranking results. For the topic ‘health’, for example, it has the largest impact with average OSim@10 being 23%. We observe changes of more than 49% in some topics by looking at OSim@10.

## 8. Conclusions

This work introduced various metrics for importance ranking in scienti<sup>fi</sup>c collaboration environments. We proposed a novel topic-sensitive authority model that is based on well-established ranking techniques. We systematically derived a uni<sup>fi</sup>ed HITS/PageRank-based model that can be fully personalized. The second metric measures organizations' structural importance based on the notion of structural holes. In our approach structural importance is computed with respect to certain topics of interest. Thus, structural importance helps in identifying organizations that may be valuable partners for strategic alliances. Combined with authority, this provides a powerful approach for ranking and discovering new partners. Finally, authority and structural importance are systematically combined with cost. For that purpose we utilize AHP to achieve a trade-off among various ranking criteria. The proposed approach delivers very good results and provides more accurate, topicsensitive results when compared with other ranking techniques.

In our future work we will study the application of online formation algorithms [1] to scienti<sup>fi</sup>c collaboration networks to suggest competitive alliances and consortia. The metrics used in the formation algorithm to rank partners will be based on the techniques as presented in this work.

OSim and Kendall's τ for comparison of AHP-based rankings across topics.

<table><tr><td colspan="2"></td><td>Networks</td><td>Systems</td><td>Software</td><td>Services</td><td>Transport</td><td>Efficiency</td><td>Health</td><td>Embedded</td><td>Internet</td><td>Energy</td></tr><tr><td rowspan="10">OSim@10</td><td>Networks</td><td>1.00</td><td>0.40</td><td>0.40</td><td>0.40</td><td>0.20</td><td>0.40</td><td>0.20</td><td>0.20</td><td>0.80</td><td>0.40</td></tr><tr><td>Systems</td><td>0.00</td><td>1.00</td><td>0.50</td><td>0.30</td><td>0.40</td><td>0.50</td><td>0.10</td><td>0.40</td><td>0.50</td><td>0.50</td></tr><tr><td>Software</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.60</td><td>0.30</td><td>0.50</td><td>0.10</td><td>0.20</td><td>0.60</td><td>0.50</td></tr><tr><td>Services</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.20</td><td>0.40</td><td>0.10</td><td>0.20</td><td>0.60</td><td>0.40</td></tr><tr><td>Transport</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.40</td><td>0.10</td><td>0.20</td><td>0.30</td><td>0.40</td></tr><tr><td>Efficiency</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.10</td><td>0.20</td><td>0.50</td><td>1.00</td></tr><tr><td>Health</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.30</td><td>0.20</td><td>0.10</td></tr><tr><td>Embedded</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.30</td><td>0.20</td></tr><tr><td>Internet</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.50</td></tr><tr><td>Energy</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td rowspan="10">OSim@20</td><td>Networks</td><td>1.00</td><td>0.35</td><td>0.45</td><td>0.40</td><td>0.30</td><td>0.40</td><td>0.35</td><td>0.30</td><td>0.65</td><td>0.40</td></tr><tr><td>Systems</td><td>0.00</td><td>1.00</td><td>0.55</td><td>0.50</td><td>0.45</td><td>0.45</td><td>0.40</td><td>0.55</td><td>0.50</td><td>0.45</td></tr><tr><td>Software</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.60</td><td>0.40</td><td>0.55</td><td>0.40</td><td>0.35</td><td>0.55</td><td>0.55</td></tr><tr><td>Services</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.35</td><td>0.40</td><td>0.35</td><td>0.30</td><td>0.55</td><td>0.40</td></tr><tr><td>Transport</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.50</td><td>0.30</td><td>0.35</td><td>0.35</td><td>0.50</td></tr><tr><td>Efficiency</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.40</td><td>0.30</td><td>0.45</td><td>1.00</td></tr><tr><td>Health</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.35</td><td>0.30</td><td>0.40</td></tr><tr><td>Embedded</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.35</td><td>0.30</td></tr><tr><td>Internet</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.45</td></tr><tr><td>Energy</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td rowspan="10">OSim@50</td><td>Networks</td><td>1.00</td><td>0.58</td><td>0.62</td><td>0.58</td><td>0.50</td><td>0.52</td><td>0.40</td><td>0.46</td><td>0.76</td><td>0.52</td></tr><tr><td>Systems</td><td>0.00</td><td>1.00</td><td>0.74</td><td>0.74</td><td>0.68</td><td>0.78</td><td>0.68</td><td>0.78</td><td>0.72</td><td>0.78</td></tr><tr><td>Software</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.82</td><td>0.70</td><td>0.72</td><td>0.60</td><td>0.64</td><td>0.74</td><td>0.72</td></tr><tr><td>Services</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.72</td><td>0.74</td><td>0.60</td><td>0.62</td><td>0.72</td><td>0.74</td></tr><tr><td>Transport</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.72</td><td>0.54</td><td>0.60</td><td>0.62</td><td>0.72</td></tr><tr><td>Efficiency</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.68</td><td>0.66</td><td>0.62</td><td>1.00</td></tr><tr><td>Health</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.58</td><td>0.54</td><td>0.68</td></tr><tr><td>Embedded</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.56</td><td>0.66</td></tr><tr><td>Internet</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.62</td></tr><tr><td>Energy</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td rowspan="10">Kendall&#x27;s τ</td><td>Networks</td><td>1.00</td><td>0.56</td><td>0.72</td><td>0.67</td><td>0.63</td><td>0.62</td><td>0.60</td><td>0.66</td><td>0.86</td><td>0.62</td></tr><tr><td>Systems</td><td>0.00</td><td>1.00</td><td>0.62</td><td>0.54</td><td>0.57</td><td>0.57</td><td>0.57</td><td>0.70</td><td>0.50</td><td>0.57</td></tr><tr><td>Software</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.82</td><td>0.67</td><td>0.68</td><td>0.65</td><td>0.73</td><td>0.74</td><td>0.68</td></tr><tr><td>Services</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.70</td><td>0.62</td><td>0.63</td><td>0.65</td><td>0.72</td><td>0.62</td></tr><tr><td>Transport</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.64</td><td>0.57</td><td>0.64</td><td>0.58</td><td>0.64</td></tr><tr><td>Efficiency</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.55</td><td>0.63</td><td>0.56</td><td>1.00</td></tr><tr><td>Health</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.62</td><td>0.56</td><td>0.55</td></tr><tr><td>Embedded</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.60</td><td>0.63</td></tr><tr><td>Internet</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.56</td></tr><tr><td>Energy</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td></tr></table>

## References

[1] A. Anagnostopoulos, L. Becchetti, C. Castillo, A. Gionis, S. Leonardi, Online team formation in social networks, Proceedings of the 21st International Conference on World Wide Web. WWW '12, ACM, New York, NY, USA, 2012, pp. 839–848.

[2] L. Backstrom, D. Huttenlocher, J. Kleinberg, X. Lan, Group formation in large social networks: membership, growth, and evolution, Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. KDD '06, ACM, New York, NY, USA, 2006, pp. 44–54.

[3] K. Berberich, M. Vazirgiannis, G. Weikum, T-rank: time-aware authority ranking, in: S. Leonardi (Ed.), Algorithms and Models for the Web-Graph, Lecture Notes in Computer Science, vol. 3243, Springer, Berlin Heidelberg, 2004, pp. 131–142.

[4] P. Berkhin, Survey: a survey on PageRank computing, Internet Mathematics 2 (1) (2005) 73–120.

[5] R.S. Burt, Structural Holes: The Social Structure of Competition, Harvard University Press, 1992.

[6] R.S. Burt, Structural holes and good ideas, American Journal of Sociology 110 (2) (Sept. 2004) 349–399.

[7] L.M. Camarinha-Matos, H. Afsarmanesh, Collaborative networks, PROLAMAT, 2006, pp. 26–40.

[8] A. Certa, M. Enea, T. Lupo, ELECTRE III to dynamically support the decision maker about the periodic replacements con<sup>fi</sup>gurations for a multi-component system, Decision Support Systems 55 (1) (Apr. 2013) 126–134.

[9] S. Chakrabarti, Dynamic personalized PageRank in entity-relation graphs, Proceedings of the 16th International Conference on World Wide Web WWW '07 ACM New York, NY, USA, 2007, pp. 571–580, http://dx.doi.org/10.1145/1242572.1242650.

[10] H. Deng, M.R. Lyu, I. King, A generalized co-hits algorithm and its application to bipartite graphs, Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. KDD '09, ACM, New York, NY, USA, 2009, pp. 239–248, http://dx.doi.org/10.1145/1557019.1557051.

[11] Y. Ding, Scienti<sup>fi</sup>c collaboration and endorsement: network analysis of coauthorship and citation networks, Journal of Informetrics 5 (1) (2011) 187–203.

[12] P. Ferrari, A method for choosing from among alternative transportation projects, European Journal of Operational Research 150 (1) (2003) 194–203.

[13] D. Fogaras, K. Csalogany, B. Racz, T. Sarlos, Towards scaling fully personalized PageRank: algorithms. lower bounds, and experiments. Internet Mathematics 2 (3) (2005) 333–358.

[14] F. Fu, C. Hauert, M.A. Nowak, L. Wang, Reputation-based partner choice promotes cooperation in social networks, Physical Review E 78 (Aug 2008) 026117.

[15] S. Goyala, F. Vega-Redondo, Structural holes in social networks, Journal of Economic Theory 137 (1) (November 2007) 460–492.

[16] M.S. Granovetter, The strength of weak ties, The American Journal of Sociology 78 (6) (1973) 1360–1380.

[17] R. Guns, Y. Liu, D. Mahbuba, Q-measures and betweenness centrality in a collaboration network: a case study of the <sup>fi</sup>eld of informetrics, Scientometrics 87 (1) (2011) 133–147, http://dx.doi.org/10.1007/s11192-010-0332-3

[18] T. Haveliwala, S. Kamvar, G. Jeh, An analytical comparison of approaches to personalizing PageRank, Tech. Rep, Stanford University, 2003.

[19] T.H. Haveliwala, Topic-sensitive PageRank, Proceedings of the 11th International Conference on World Wide Web. WWW '02, ACM, New York, NY, USA, 2002, pp. 517–526, http://dx.doi.org/10.1145/511446.511513.

[20] G. Jeh, J. Widom, Scaling personalized web search, Proceedings of the 12th International Conference on World Wide Web. WWW '03, ACM, New York, NY, USA, 2003, pp. 271–279, http://dx.doi.org/10.1145/775152.775191.

[21] J. Kleinberg, Authoritative sources in a hyperlinked environment, Journal of the ACM 46 (1999) 668–677.

[22] J. Kleinberg, S. Suri, E. Tardos, T. Wexler, Strategic network formation with structural holes, SIGecom Exchanges 7 (3) (2008).

[23] N. Lavrac, P. Ljubic, T. Urbancic, G. Papa, M. Jermol, S. Bollhalter, Trust modeling for networked organizations using reputation and collaboration estimates, IEEE Transactions on Systems, Man, and Cybernetics. Part C: Applications and Reviews 37 (3) (May 2007) 429–439.

[24] S. Milojević, Modes of collaboration in modern science: beyond power laws and preferential attachment, Journal of the American Society for Information Science and Technology 61 (7) (Jul. 2010) 1410–1423.

[25] F. Munisteri, ICT statistical report for annual monitoring 2011, http://ec.europa.eu/ digital-agenda/sites/digital-agenda/files/stream. 2012 0.pdf Feb. 2012

[26] M.E.J. Newman, Coauthorship networks and patterns of scienti<sup>fi</sup>c collaboration, Proceedings of the National Academy of Sciences of the United States of America 101 (Suppl. 1) (2004) 5200–5205.

[27] A.Y. Ng, A.X. Zheng, M.I. Jordan, Stable algorithms for link analysis, Proceedings of the 24th Annual International ACM SIGIR Conference on Research and Development in x. SIGIR '01, ACM, New York, NY, USA, 2001, pp. 258–266.

[28] L. Page, S. Brin, R. Motwani, T. Winograd, The PageRank citation ranking: bringing order to the web, Tech. Rep, Stanford University, 1998.

[29] T.L. Saaty, Decision making with the analytic hierarchy process, International Journal of Services Sciences 1 (Nov. 2008) 83–98

[30] D. Schall, Expertise ranking using activity and contextual link measures, Data & Knowledge Engineering 71 (1) (2012) 92–113.

[31] D. Schall, Service oriented crowdsourcing: architecture, protocols and algorithms, Springer Briefs in Computer Science, Springer, New York, New York, NY, USA 2012.

[32] D. Schall, Measuring contextual partner importance in scienti<sup>fi</sup>c collaboration networks, Journal of Informetrics 7 (3) (July 2013) 730–736.

[33] D.H. Sonnenwald, B. Cronin, Anonymous, Scienti<sup>fi</sup>c collaboration: a synthesis of challenges and strategies, Annual Review of Information Science and Technology, vol. 4, Information Today, 2007, pp. 2–37.

[34] W. Tsai, Social capital, strategic relatedness, and the formation of intra-organizational strategic linkages, Strategic Management Journal 21 (9) (2000) 925–939.

[35] C.S. Wagner, L. Leydesdorff, Network structure, self-organization, and the growth of international collaboration in science, Research Policy 34 (10) (2005) 1608-1618

Daniel Schall is currently employed as a senior research scientist at Siemens Corporate Technology. From 03/2009 to 10/2011, he worked as a senior research scientist at the Vienna University of Technology. Daniel defended his PhD in 02/2009 with a thesis on ‘Human Interactions in Mixed Systems — Architecture, Protocols, and Algorithms’, which he performed while working as a research assistant at the Vienna University of Technolog (05/2006–02/2009). Prior to that, he worked at Siemens Corporate Research in Princeton, New Jersey USA
