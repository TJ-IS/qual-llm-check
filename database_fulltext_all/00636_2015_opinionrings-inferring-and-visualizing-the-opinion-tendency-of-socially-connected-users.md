---
otero_id: 636
otero_key: "8YS6W4EJ"
title: "OpinionRings: Inferring and visualizing the opinion tendency of socially connected users"
authors: "Xiaolin Du; Yunming Ye; Raymond Y.K. Lau; Yueping Li"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.04.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# OpinionRings: Inferring and visualizing the opinion tendency of socially connected users

Xiaolin Du <sup>a</sup>, Yunming Ye <sup>a,</sup>⁎, Raymond Y.K. Lau <sup>b</sup>, Yueping Li <sup>c</sup>

<sup>a</sup> Shenzhen Key Laboratory of Internet Information Collaboration, Shenzhen Graduate School, Harbin Institute of Technology, Shenzhen, China

<sup>b</sup> Department of Information Systems, City University of Hong Kong, Hong Kong Special Administrative Region

<sup>c</sup> ShenZhen Polytechnic, Shenzhen, China

## a r t i c l e i n f o

Article history: Received 10 February 2014 Received in revised form 1 March 2015 Accepted 11 April 2015 Available online 23 April 2015

Keywords: OpinionRings Opinion visualization Opinion analysis Opinion prediction Opinion networks

## a b s t r a c t

Actors (e.g., people, organizations and nations) of online social networks often express different opinions toward opinion targets (e.g., products, events and political <sup>fi</sup>gures). Extracting and visualizing the distributions of different opinions among actors facilitate policy-makers (e.g., business managers and government of<sup>fi</sup>cials) to develop informed decisions promptly. In this paper, by extending the notion of signed networks, we <sup>fi</sup>rst provide a formal de<sup>fi</sup>nition of opinion networks which are networks of actors who hold potentially different opinions against specific targets. Another main contribution of our research is the development of a visualization method called OpinionRings to infer and visualize the actual and the potential opinions of different groups of actors. In particular, the proposed OpinionRings method leverages three concentric rings with various colors and widths to highlight different groups of actors and their opinions. One unique feature of the OpinionRings method is that the inclination of an actor, who originally holds a neutral opinion polarity, to adopt a positive or negative opinion polarity can be estimated according to the color of the actor and the distance to other actors with known opinion polarities. A series of objective quantitative experiments and subjective user-based evaluation show that the proposed OpinionRings method signi<sup>fi</sup>cantly outperforms the traditional visualization methods in terms of cohesiveness of displays, informativeness of visualized contents, and inference power of the visualization scheme. The practical implication of our research is that business managers or government of<sup>fi</sup>cials can apply our proposed computational method to extract and visualize valuable social intelligence from online social networks to facilitate their decision-making processes.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

With the emergence and rapid proliferation of online social networks such as Facebook, Twitter, Linkedin, and so on, there is an explosive growth of the amount of user-contributed facts and opinions in these networks. In the era of Web 2.0, actors (e.g., individuals, organizations and government of<sup>fi</sup>cials) often voice their opinions about some targets (e.g., other individuals, events, products, or services) in online social networks. While some actors may share the same opinion, other actors may hold different opinions toward the same target. Accordingly, we can classify actors into different communities according to their common beliefs. For example, while some actors of online social networks supported Barack Obama to be re-elected as the president of the United States in the 2012 US election year, other actors felt positive and voted for Mitt Romney. Yet, some actors expressed different opinions in online social networks and supported neither Obama nor

Romney. The campaign manager of a presidential candidate is keen to know which group of actors hold a certain opinion polarity (e.g., positive or negative) about her candidate, and which group of actors have a neutral opinion polarity such that she can focus on her persuading effort. For directed marketing, a campaign manager would like to know who feels positive about her products, and then she may recruit these positive actors to write blog messages or online product reviews to in<sup>fl</sup>uence those who have a neutral opinion polarity to change their minds. Meanwhile, the campaign manager would also like to identify the group of actors who feel negative about her products, and try to understand their concerns for subsequent product redesign and enhancement. As can be seen, the sheer volume of opinionated expressions captured in online social networks provides organizations and government agencies with unprecedented opportunities to tap into the valuable collective social intelligence to enhance their decision making processes. However, there is a pressing need to develop an effective computational method that can extract and visualize actors' opinions such that business managers and government of<sup>fi</sup>cials can promptly leverage this valuable social intelligence.

The sheer volume of opinionated expressions captured in online social networks provides organizations and government agencies with unprecedented opportunities to tap into the valuable collective social intelligence to enhance their decision making processes. In this paper, opinion networks refer to networks of actors who hold different opinions against some opinion targets. Speci<sup>fi</sup>cally, actors of an opinion network are divided into three groups according to their opinion polarities: (1) actors with a positive opinion polarity about an opinion target, namely opinion A (e.g., actors supporting Obama), (2) actors with a negative opinion polarity about the opinion target, namely opinion B (e.g., actors dislike Obama), (3) actors holding a neutral opinion polarity, namely opinion U (e.g., actors neither supporting nor disfavoring Obama). The emergence of online social media has given users a venue for expressing and sharing their thoughts and opinions against different topics and events. Accordingly, there is a large body of research work toward opinion analysis and opinion mining in the past two decades [1–6]. However, most of the existing opinion visualization methods employ a simple one-dimensional display to summarize opinion orientation. Existing techniques are weak in highlighting the distributions of opinions among different groups of actors, and they lack the capabilities of inferring the opinion inclination of the neutral actors. Our research work just tries to address the aforementioned shortcomings. In particular, we combine visualization methods and machine learning techniques to enhance the inference power of the proposed opinion ring visualization method.

Information visualization techniques, when used in conjunction with data mining tools, can be of great value for mining business intelligence and knowledge from online social networks [7]. In recent years, many visualization methods have been designed for visualizing social networks. Nevertheless, few of them aim at mining and visualizing opinion networks and offer satisfactory solutions to address the following challenges: (a) automatically clustering groups of actors according to their opinions, (b) visualizing the inclinations of actors who hold a neutral opinion polarity according to the probability that they may change to adopt opinion A or opinion B, (c) supporting sophisticated opinion analysis based on a simple and intuitive display easily consumed by ordinary users. The main theoretical contribution of our research work is the design of the novel OpinionRings visualization method to address the aforementioned challenges. Speci<sup>fi</sup>cally, the proposed visualization method supports the following innovative features:

## 1.1. Concentric ring visualization layout

The proposed OpinionRings method adopts a concentric ring visualization layout to position three groups of actors, that is, the actors holding opinion A, the actors holding opinion B, and the actors with opinion U, respectively. It divides the full-screen canvas into three concentric rings, with each group of actors represented by the corresponding ring.

## 1.2. Integrating inference with visualization

The proposed OpinionRings method employs a collective classi<sup>fi</sup>cation algorithm to infer the probability that actors with opinion U may change to take opinion A or opinion B. Then, it visualizes this probability by means of the speci<sup>fi</sup>c color and position of an actor who holds opinion U. Such a visualization method greatly facilitates online interactive opinion analysis.

Through a series of objective quantitative experiments and userbased evaluations based on several publicly available benchmark data sets, the effectiveness of the proposed OpinionRings method is examined and compared to that of a well-known force-directed visualization method [8] and a fast multiscale visualization method [9]. Our experimental results consistently show that the proposed OpinionRings method signi<sup>fi</sup>cantly outperforms the two comparative methods. The practical implication of our research is that business managers or government of<sup>fi</sup>cials can apply our visualization method to extract and visualize useful social intelligence from online social networks to enhance their decision-making processes pertaining to various real-world applications. The remainder of the paper is organized as follows. Section 2 discusses several research areas related to our research work. Section 3 provides a theoretical foundation about opinion analysis and opinion network visualization. Section 4 illustrates the computational details of the proposed OpinionRings visualization method. Section 5 describes the objective quantitative experiments and userbased evaluations for the OpinionRings method based on several benchmark data sets. Finally, we offer the concluding remarks and describe the future directions of our research work.

## 2. Related work

To the best of our knowledge, research about the visualization of opinion networks is rare in existing literature. Accordingly, we discuss related work about circular layout, bipartite graph, network and opinion mining based visualization methods.

## 2.1. Visualization by circular layouts

Circular layouts were among the <sup>fi</sup>rst type of layout used by social scientists to build the initial social network visualization tools [10]. The most famous example was Northway's target sociogram that used a series of concentric circles to represent populations of actors and guides the placement of vertices (actors) by placing the most structurally central vertices in the innermost circle [11]. An approach that used the tree ring metaphor to display vertices was presented in [12]. For this visualization method, a hierarchical tree structure was applied to concentric circles to represent different time periods. Brandes et al. [13] adopted the target sociogram principle to improve the esthetics of visualizing policy networks. Yee et al. [14] proposed a radial layout for animating the transition to a new layout after a targeted vertex was selected from an existing layout. In order to keep the transition easy to be observed, the animation linearly interpolated the polar coordinates of the vertices while enforcing the ordering and orientation constraints. Farrugia et al. [15] develop a tree ring like layout for ego networks that places the time dimension in the foreground, by turning time into an element of shape. In addition to this research an interactive system that enables the visualization of multiple networks simultaneously by employing small multiples was also developed. Since circular layouts have been widely used by social scientists to visualize traditional social networks, we adopt a circular layout to visualize opinion networks.

## 2.2. Visualization by bipartite graphs

Although graph-based visualization is an active research area, very few studies have explored the visualization of graphs with labeled vertices. There are some studies that examine the visualization of objects with two possible class labels based on bipartite graphs. An interesting method called Anchored Maps (AM) [16,17] was developed. The AM method supports the visualization of bipartite graphs by means of a two-dimensional display. More speci<sup>fi</sup>cally, the <sup>fi</sup>rst subset of vertices is plotted on a circle, after which the second subset of vertices is added to the display by allocating them with respect to the positions of the <sup>fi</sup>rst subset of vertices. The Spherical Embedding (SE) algorithm [18] was primarily designed for the visualization of bipartite graphs. The objects belonging to two classes are represented by the vertices positioned on two concentric spheres under a three-dimensional Euclidean space. Zheng et al. [19] proposed an optimal visualization method to minimize the number of crossings among the vertices that were placed in a three-dimensional space de<sup>fi</sup>ned by two parallel planes. Di Giacomo et al. [20] developed an effective visualization method that plotted classi<sup>fi</sup>ed vertices along planar curves.

## 2.3. Visualization by networks

Various network-based visualization methods have been developed to analyze relational patterns. Heer et al. [21] developed a prototype system called Vizster for interactive exploration and navigation of large-scale online social networks. However, the Vizster system can only visualize one type of relationship. In order to visualize multiple types of relationships, Shen et al. [22] developed the OntoVis method which applied different kinds of vertices and edges to represent various concepts and relations captured by large and heterogeneous social networks. In particular, the OntoVis method separated entities and their relationships under a set of focused and unfocused concepts, respectively. Cao et al. [23] developed the FacetAtlas visualization method that supported a multifaceted display for rich text corpora; the FacetAtlas method can convey both global and local patterns using only one simple visual metaphor. More recently, Cao et al. [24] have developed the SolarMap method which supports a multifaceted visual analysis and exploration of topics for multi-relational data. Side et al. [25] developed the SocialAction method which facilitated relational pattern detection in social networks by means of smart <sup>fi</sup>ltering of important vertices, clusters, and outliers.

## 2.4. Opinion visualization methods

With the growing availability and popularity of opinion-rich resources such as online voting systems and personal blogs, researchers have developed different opinion mining methods to mine users' opinions from these resources. Opinion mining (also known as sentiment analysis) [2] aims to assist users to automatically detect relevant opinions within a large volume of review collection and create a coherent overview of these opinions. There has been growing interests for researchers to develop computational methods of visualizing opinions embedded in online customer reviews. A previous study [26] classi<sup>fi</sup>ed opinion visualization methods into two broad categories, namely document-level and feature-level opinion visualization. Documentlevel visualization focuses on generating a high-level overview of opinionated data sets. Morinaga et al. [27] proposed a 2D scatter plot called positioning map to show a group of positive or negative sentences. Gregory et al. [28] developed an adapted rose plot to visualize sentiment aspects such as positive, negative, pleasure, pain, and con<sup>fl</sup>ict. Chen et al. [29] presented a visual analysis system with multiple coordinated views such as decision trees and term variation graph to help users understand the nature and dynamics of con<sup>fl</sup>icting opinions. On the other hand, feature-level opinion visualization methods provide more detailed presentations for users to realize opinions pertaining to some certain product or product features. For example, Liu et al. [30] proposed a novel framework called Opinion Observer for analyzing and comparing consumer opinions against competing products. It extracted featurelevel opinions from customer reviews, and leveraged traditional bar charts to facilitate the visual comparison of extracted feature-level opinions. Oelke et al. [31] introduced several visualization techniques including visual summary reports, cluster analysis, and circular correlation map to facilitate the visual analysis of customer feedbacks at the feature level. Wu et al. [26] applied subjective logics to augment traditional scatter plots and radial visualizations for the representation of customer opinions at both the feature and document levels.

## 2.5. The proposed OpinionRings visualization method

Unlike previous methods, the proposed OpinionRings visualization method provides a <sup>fl</sup>exible visualization to support the analysis and display of opinion networks, and so it is different from all the aforementioned work. In addition, while existing methods do not consider the actors' uncertainty of opinions, our visualization approach explicitly accounts for uncertainty to faithfully reveal the underlying information of opinion networks. More speci<sup>fi</sup>cally, it adopts a concentric ring layout to visualize the opinions held by three groups of actors in opinion networks. By means of such a layout, the distributions of opinions held by different actors can easily be observed by users. In addition, it employs a collective classi<sup>fi</sup>cation algorithm [32] to predict the probability that an actor with a neutral opinion polarity may subsequently change to take a positive (i.e., opinion A) or a negative (i.e., opinion B) opinion polarity. The empirical justi<sup>fi</sup>cations of applying a concentric ring layout to visualize opinion networks are that such an approach has been widely used by social scientists and it has been found effective for visualizing social networks through numerous <sup>fi</sup>eld tests [10,11]. From the perspective of esthetic principles, concentric ring layout is effective to highlight the most important elements of a problem domain $( \mathrm { e . g . }$ , a community of actors holding a strong opinion) by placing these elements toward the center of a circle [33]. A circular layout rather than a zigzag pattern such as a rectangle can better guide the users' eye movements to observe important information on a graphical display [33].

## 3. The opinion network data model

## 3.1. Opinion analysis

In recent years, many studies on social networks with positive (friendly) and negative (antagonistic) opinions have been reported in literature [34–39]. These studies are mainly focusing on examining the interplay or predicting opinion polarities between positive and negative links in social media. By extending the notion of signed networks proposed by these studies, we de<sup>fi</sup>ne the opinion analysis problem as follows. Since we do not deal with evolving opinion networks in this paper, the T dimension will not be further explored for the rest of this paper.

## De<sup>fi</sup>nition 1. Opinion analysis

An opinion analysis model is de<sup>fi</sup>ned by a sextuple $O M =$ $\langle O , A , P , S , T , M _ { O M } \rangle$ , where O, A and P stand for <sup>fi</sup>nite sets of opinion targets (objects), actors (opinion holders), and opinion polarity, respectively. The opinion polarity is de<sup>fi</sup>ned by the set P = {postive, negative, neutral} and the opinion strength $S \in [ 0 ,$ 1] represents the degree of feeling perceived by an actor. The set of time points T indicates when the set of opinions O is held. Finally, the mapping function $M _ { O M }$ maps the basic elements of the opinion analysis model to form a valid opinion tuple, that is, who holds a particular opinion for a speci<sup>fi</sup>c target at a particular point of time.

## 3.2. Opiniongraph

As described in Section 1, an opinion network consists of connected actors who hold different opinions for an opinion target. In this paper, we use Opiniongraph, a relational graph, to represent an opinion network. The formal de<sup>fi</sup>nition of an Opiniongraph is as follows.

## De<sup>fi</sup>nition 2. Opiniongraph

An Opiniongraph denoted $O G = ( V , E , O _ { m } ( \cdot ) )$ is a triple where V and E are <sup>fi</sup>nite sets of vertices and edges, respectively. Each vertex $\nu \in V$ represents an actor of an opinion network and each edge $e \in E$ represents a connection between two actors. The mapping function $O _ { m } ( \cdot )$ maps each vertex $\nu \in V$ to the set of opinions $\{ - 1 , 0 , 1 \}$ , where $1 , - 1$ and 0 indicate an actor v holding opinion A (i.e., a positive opinion polarity), opinion B (i.e., a negative opinion polarity), and opinion U (i.e., a neutral opinion polarity), respectively.

In other words, the mapping function $O _ { m } ( \cdot )$ is de<sup>fi</sup>ned by:

$$
O _ {m} (v) = \left\{ \begin{array}{l l} 1 & \text { if   actor   } v \text {   holds   opinion   A } \\ 0 & \text { if   actor   } v \text {   is   neutral   to   an   opinion   target } \\ - 1 & \text { if   actor   } v \text {   holds   opinion   B } \end{array} \right.
$$

According to the opinion mapping function $O _ { m } ( \nu )$ , a set of vertices V of an Opiniongraph can be divided into three subsets denoted by $V _ { A } , V _ { U } ,$ and $V _ { B } , V _ { A }$ and $V _ { B }$ represent the subsets of actors who hold opinion A and opinion B, respectively. Moreover, the subset $V _ { U }$ represents the set of actors who is neutral to an opinion target $o \in O$ for the time being. However, an actor $\nu \in V _ { U }$ may change to hold opinion A or B at a later stage.

## 3.3. The opinion network data model

Based on De<sup>fi</sup>nition 2, the OpinionRings data model is de<sup>fi</sup>ned as follows.

Entity: Entities are instances of the actors A of an opinions network represented by OG.

Opinion: Opinions refer to the subjective feelings of actors A with respect to some opinion targets O (e.g., products, services, events and political <sup>fi</sup>gures). More precisely, each actor holds one of the three possible opinion polarities (positive, negative, and neutral) against a speci<sup>fi</sup>c opinion target.

Group: Opinion groups are subsets of entities of an opinion network divided according to different opinions. For the opinion network data model, entities are divided into three groups: group A (i.e., entities holding opinion A), group B (i.e., entities holding opinion B) and group U (i.e., entities holding opinion U).

Relation: Relations are connections between pairs of entities. There are two types of relations. Internal relations are connections among entities of the same group. External relations are connections among entities of different opinion groups. For example, an entity of group A is connected to an entity of group B via an external relation.

Opinion probability: Opinion probability is a very important element of the opinion network data model. For each entity of the group U, two opinion probabilities are estimated, the probability of the entity to change to adopt opinion A and the probability of the entity to change to adopt opinion B. The sum of these probabilities equals to 1.

A simple layout of the opinion network data model is depicted in Fig. 1. The <sup>fi</sup>gure shows a concentric ring visualization approach. In particular, three concentric rings (denoted ring A, ring B, and ring U) represent the display regions of three different opinion groups. Vertices in each ring represent the entities of the corresponding opinion group. The distance of a vertex in ring U to another vertex in ring A or B is inversely proportional to its opinion probability. A shorter distance between a vertex in ring U to another vertex in ring A (B) implies that the corresponding entity is more likely to take opinion A (B) at a later stage.

![](/api/attachments/8YS6W4EJ/fulltext/images/940914d7e347b011661a82e284b7a4fe4eed7fd86e78a9cdb9a31ca462c1dba7.jpg)  
Fig. 1. The opinion network data model.

## 4. The computational model of OpinionRings

## 4.1. The Opiniongraph layout

As shown in Fig. 1, the concentric ring layouts produced by OpinionRings have the following main characteristics:

1. The screen canvas is divided into three concentric rings for rendering different groups of entities according to their opinions. More speci<sup>fi</sup>cally, entities of Group U are placed in the middle ring, and the entities of Group A and Group B are positioned in the inner ring and the outer ring, respectively. The radiuses of these three rings are proportionally calculated with respect to the number of entities pertaining to the corresponding group.

2. A collective classi<sup>fi</sup>cation algorithm [32] is applied to predict the probability that an entity who currently holds opinion U may change to take opinion A or B. The predicted opinion probabilities are demonstrated by the entity's color and its distances to ring A and ring B, respectively.

3. The color of each entity in ring A (B) is exactly the same to indicate the fact that all entities of the same group hold the same opinion polarity against an opinion target. The two different colors for ring A and ring B are selected based on the RGB color model so that entities of the respective rings can be easily differentiated. Entities of ring U have gradient colors between color A and color B according to their opinion probabilities. If an entity of group U has a higher probability to change to adopt opinion A (B), its color is more similar to that adopted by group A (B). Accordingly, users can easily observe and analyze the opinion inclination of entities in ring U by simply taking a glance of their colors.

4. The distance of an entity of ring U to ring A (B) also indicates the predicted opinion inclination for the entity to take opinion A (B) in the future. The predicted opinion probability is inversely proportional to the distance between the entity of ring U and ring A (B). In other words, if the entity of group U is more likely to change to adopt opinion A (B), it will be closer to ring A (B).

## 4.2. The visualization of Opiniongraph

The visualization of Opiniongraph consists of 7 steps. The computational details of these steps are illustrated in this subsection.

## 4.2.1. Step 1: radius computation

We compute the radiuses of three rings according to the sizes of three opinion groups. More speci<sup>fi</sup>cally, $N _ { A } , N _ { U }$ and $N _ { B }$ represent the number of entities of group A, group U, and group B, respectively. Let $N _ { G }$ represent the number of entities of a group $G ,$ and $R _ { m a x }$ represent the radius of the largest circle in a canvas. Fig. 2 outlines the radiuses $R _ { A } , R _ { U } ,$ and $R _ { B }$ of the respective rings. In particular, the unit entity area satis<sup>fi</sup>es the following equation.

$$
u n i t A r e a = \frac {\pi R _ {m a x} ^ {2}}{N _ {G}}.\tag{1}
$$

Hence, the ring areas of group A, group U, and group B are $N _ { A }$ ∗ unitArea, $N _ { U }$ ∗ unitArea, and $N _ { B }$ ∗ unitArea, respectively. The radiuses of the three rings $R _ { A } , R _ { U } ,$ and $R _ { B }$ are computed as follows, where $R _ { A } + R _ { U } + R _ { B } = R _ { m a x } .$

![](/api/attachments/8YS6W4EJ/fulltext/images/5284695b30ac5c235782ec588251561ed0794b31d18397f11f8a6f3a97f09f7a.jpg)  
Fig. 2. Radiuses of the three opinion regions.

$$
R _ {A} = \sqrt {\frac {N _ {A} * u n i t A r e a}{\pi}}\tag{2}
$$

$$
R _ {U} = \sqrt {\frac {(N _ {A} + N _ {U}) * u n i t A r e a}{\pi}} - R _ {A}\tag{3}
$$

$$
R _ {B} = R _ {m a x} - R _ {A} - R _ {U}.\tag{4}
$$

4.2.2. Step 2: Opinion prediction

We apply a collective classi<sup>fi</sup>cation algorithm [32] to infer the probabilities that entities of Group U will change to adopt opinion A or B. These probabilities in<sup>fl</sup>uence the colors and the positions of these group U entities being placed in ring U. Accordingly, the proposed OpinionRings visualization method can reveal more information than other visualization methods, and it enables users to observe the opinion tendencies of the neutral actors easily. Collective classi<sup>fi</sup>cation (CC) is a kind of method for jointly classifying the class labels of vertices in a network based on the known class labels of other connected vertices [40], and it is often considered as a class of combinatorial problem [41]. Given some vertices with known class labels in a network, CC algorithms can infer the class labels of other vertices, or estimate the probabilities of these vertices having certain class labels according to the attributes of these vertices. Four popular approximate inference algorithms are often used to perform collective classi<sup>fi</sup>cation: iterative classi<sup>fi</sup>cation [42,43], Gibbs sampling [44,43,45], loopy belief propagation [46], and mean-<sup>fi</sup>eld relaxation labeling [32].

In this paper, we adopt the Weighted-vote Relational Neighbor with Relaxation Labeling (wvRNRL) algorithm to predict the opinion probabilities of entities in group U. wvRNRL is a classical relational-only CC algorithm and is considered the baseline method for the class of common CC algorithms [32]. The wvRNRL algorithm computes new vertex label distribution by averaging neighbors' label distributions, and then it combines old and new label distributions via relaxation labeling. By invoking the wvRNRL algorithm, we can estimate the probability $P _ { A } \ ( P _ { B } )$ which indicates the likelihood for a vertex $\nu \in V _ { U }$ to adopt opinion A (B) under the condition $P _ { A } + P _ { B } = 1$ . Our opinion prediction module is independent of other modules of the OpinionRings method. Accordingly, the opinion prediction function of our proposed method can be further enhanced based on the state-of-the-art classi<sup>fi</sup>- cation methods developed in the <sup>fi</sup>eld of machine learning.

## 4.2.3. Step 3: initial position estimation

After computing the radiuses of three rings and predicting opinion probabilities of vertices of ring U, we can compute the initial positions of vertices in the three concentric rings. The appropriate initial positions of vertices can pinpoint the correct relationships among entities, and reduce the subsequent number of iterations of the OpinionRings algorithm to improve the quality of the display. However, how can we estimate the appropriate initial positions of vertices? Let us imagine how a good painter may place all the vertices and edges on a canvas with concentric rings. One common method is to <sup>fi</sup>rst draw the vertices $V _ { A }$ in ring A (the inner ring) according to a uniform distribution. Then, all the vertices $V _ { U }$ are drawn with respect to the positions of $V _ { A } .$ One may choose a vertex $ { \boldsymbol { v } } \in V _ { U }$ which is most similar to some vertices of $V _ { A } ,$ and then draw it around the chosen vertices of $V _ { A } .$ The similarities among these vertices are computed according to common similarity functions such as the graph-based random walk with restart algorithm [47]. For our experiments, we applied the graph-based random walk with restart algorithm to compute vertices similarities [47]. Such a process is repeated until all vertices of $\mathbf { \sigma } ^ { \cdot } V _ { U }$ are drawn. Similarly, the vertices of $V _ { B }$ can be drawn around ring U. Fig. 3 depicts such a process of Opiniongraph visualization.

The proposed OpinionRings method just simulates the aforementioned heuristic approach of initializing the vertices positions. First, we put all the entities of group A in ring A according to a uniform distribution. The vertices positions are expressed in terms of polar coordinates. For each vertex $\nu \in V _ { A } ,$ the OpinionRings algorithm computes:

$$
\rho_ {v} = i * \frac {2 \pi}{N _ {A}} i = \{0, 1, 2,..., N - 1 \}\tag{5}
$$

$$
r _ {v} = \frac {2}{3} R _ {A}.\tag{6}
$$

Adhering to sound esthetic principles [33], Eqs. (5) and (6) position vertices in a circle such that the polar angle interval of every vertex is 2π and the polar radius of each vertex is ${ \scriptstyle { \frac { 2 } { 3 } } } R _ { A }$

For each vertex $\nu \in V _ { U } ,$ the OpinionRings algorithm iteratively chooses some vertices and positions these vertices according to our positioning strategy until all the vertices of $V _ { U }$ are placed in ring U. The OpinionRings position strategy is to maintain a vertex list L such that each element of L satis<sup>fi</sup>es three conditions: (a) vertices in L have not yet been positioned; (b) all vertices inserted to L come from $V _ { U } ;$ (c) each chosen vertex in L has at least one neighbor which have already been positioned in the screen canvas. The initial elements of L are selected from $V _ { U }$ which have neighbors of vertices in $V _ { A }$ according to the random walk with restart algorithm [47]. Moreover, the OpinionRings selection strategy is that a vertex $\boldsymbol { v } \in V _ { U }$ with the maximal probability $P _ { A }$ is inserted to L <sup>fi</sup>rst. Then, the algorithm positions this chosen vertex v on the screen canvas <sup>fi</sup>rst. The equations of computing the polar angle and the polar radius are as follows.

$$
\rho_ {v} = \text { Random } \left(\text { AngleOf } (u) - \frac {\pi}{N _ {A}}, \text { AngleOf } (u) + \frac {\pi}{N _ {A}}\right)\tag{7}
$$

$$
r _ {v} = R _ {A} + (1 - P _ {A v}) R _ {U}\tag{8}
$$

where u is a vertex in $V _ { A }$ and v is the most similar vertex to u; AngleO f(u) represents the polar angle of u, and $\frac { \pi } { N _ { A } }$ is half of the angle interval between vertices in $V _ { A } . P _ { A \nu }$ is vertex $\nu ^ { \prime }$ probability to take opinion A. So, the polar angle of v is a random angle between AngleO $\begin{array} { r } { f ( u ) - \frac { \pi } { N _ { A } } } \end{array}$ and AngleO $\begin{array} { r } { f ( u ) + \frac { \pi } { N _ { A } } . } \end{array}$

The polar radius $r _ { v }$ is inversely proportional to the probability $P _ { A \nu } .$ After picking up a vertex v from L for positioning, two operations will be performed. First, v will be removed from L. Second, all neighbors of v in $V _ { U }$ which have not been positioned will be inserted to L. While the initial positioning process iterates, if |L| = 0 is true and there are still vertices $\boldsymbol { v } \in V _ { U }$ not being displayed, our algorithm randomly picks a vertex without coordinate from $V _ { U }$ and inserts it to L. Then, this initial positioning process continues until all vertices of $V _ { U }$ are positioned. Algorithm 1 is the algorithm for initially positioning vertices of $V _ { U }$ in ring U.

![](/api/attachments/8YS6W4EJ/fulltext/images/17d689f84f514a1a86fdf83abf20280d768489caccaca8f499fadd531bd10c62.jpg)

![](/api/attachments/8YS6W4EJ/fulltext/images/668192dd248b4cb8f9af9e7a9e59ea68adb09bcc735973708d8b9322ed64550b.jpg)

![](/api/attachments/8YS6W4EJ/fulltext/images/42c47baf6abb46a0d89c3dfcaf4c96b847f6d86ca2c464f6b8484e7312aa2410.jpg)

![](/api/attachments/8YS6W4EJ/fulltext/images/318015868c4c603991436b7471497fdfea4af18ba10cb6e6538f2c41a00372b8.jpg)  
Fig. 3. A heuristic method of initializing vertex positions.

## Algorithm 1. Initial positioning of $V _ { u } .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Initialize L according to the rule:  $\exists(u \in V_{U})\exists(v \in V_{A})$  neighbor(u, v) → u ∈ L;
2:  $N \leftarrow \#V_{U};$ 
3: while N &gt; 0 do
4: if L.length &gt; 0 then
5: Choose the first vertex u in L;
6: Position u according to the coordinate of most similar vertex in  $V_{A}$ ;
7: Add eligible neighbors of u to L;
8: Delete u from L;
9: else
10: randomly add a vertex without coordinate in  $V_{U}$  to L;
11: end if
12:  $N \leftarrow N - 1;$ 
13: end while
</div>

The method to position vertices in $V _ { B }$ is similar to that of positioning vertices of $V _ { U } .$ For every vertex v in $V _ { B } ,$ the OpinionRings algorithm <sup>fi</sup>nds some vertices $u \in V _ { U }$ which satisfy two conditions: (a) u is the most similar vertex to v and (b) u is the neighbor of v. If condition (b) cannot be satis<sup>fi</sup>ed by any $u \in V _ { U } ,$ the vertex just satisfying condition (a) is chosen. The equations for computing the polar angle and the polar radius of $\nu \in V _ { B }$ are de<sup>fi</sup>ned as follows.

$$
\rho_ {v} = \text { Random } \left(\text { AngleOf } (u) - \frac {\pi}{N _ {A}}, \text { AngleOf } (u) + \frac {\pi}{N _ {A}}\right)\tag{9}
$$

$$
r _ {v} = R _ {A} + R _ {U} + \frac {R _ {B}}{2}.\tag{10}
$$

By applying our heuristic approach, all vertices have their initial positions determined. The reason why we employ such a heuristic strategy is to avoid edge crossings and enable vertices gradually spread from the center of a circle to its edge. Nevertheless, subsequent optimization is needed to re<sup>fi</sup>ne the concentric rings display. This re<sup>fi</sup>nement process will be illustrated in the following section.

## 4.2.4. Step 4: vertices positions optimization

As shown in Fig. 4(a), the initial Opiniongraph looks confusing since there are a large number of irregular edge crossings. These crossings may hinder users from analyzing the hidden patterns of an opinion network. If there are many entities of a group, the Opiniongraph will become even more confusing. In contrast, the Opiniongraph depicted in Fig. 4(b) is the preferred layout which contains the least number of edge crossings. Such a layout is more consistent with human esthetic principles. Fig. 4(c) shows a simple example of vertex position re<sup>fi</sup>nement which involves three vertices a, v, b and two edges (a, v), (v, b). If vertex v is moved to v′, edges (a, v) and (v, b) will be shorten and the number of edge crossings will be reduced. Accordingly, an objective function is developed to reduce the number of edge crossings and facilitate relational pattern observation by users. Formally, for any $( u , v ) \in E$ and $u ,$ v not coming from the same opinion group, an objective function P is de<sup>fi</sup>ned as follows.

$$
\mathrm{n} P (u, v) = \sum_ {u} \sum_ {v} \sqrt {\left(u _ {x} - v _ {x}\right) ^ {2} - \left(u _ {y} - v _ {y}\right) ^ {2}}.\tag{11}
$$

In Eq. (11), P(u, v) is the sum of the distance between u and v. To minimize edge crossings, P(u, v) should be minimized by adjusting the corresponding positions of vertices. The OpinionRings method allows two ways of vertex adjustment, that is, rotating clockwise or anticlock wise as demonstrated in Fig. 5. The radius of the adjusted vertex remains the same while rotation occurs. For each round of adjustment, the OpinionRings method employs a hill-climbing strategy to update the positions for all vertices such that the objective function $P ( u , v )$ is minimized. In other words, the OpinionRings method ensures that $P _ { i } ( u , \nu ) < P _ { i - 1 } ( u , \nu )$ is held for each round i of adjustment. The scale of position adjustment gradually reduces after more rounds of the adjustment process are executed. When the number of rounds of position adjustment reaches a pre-de<sup>fi</sup>ned limit, the position adjustment process is terminated.

![](/api/attachments/8YS6W4EJ/fulltext/images/49b9a60244ae03e55b59141a738335de363a2d047d2fbd3cd51e38f546b688da.jpg)  
(a) before optimizing

![](/api/attachments/8YS6W4EJ/fulltext/images/fdf4836ca92705f31bc51368ce3bfabe89d4ff7e0c117ca2323fe0c70e06cb9d.jpg)  
(b) after optimizing  
Fig. 4. Vertex positions optimization.

![](/api/attachments/8YS6W4EJ/fulltext/images/b3a4bfa3ff6857eafda7a604e13ed7fce4bd15fa1ba33689aad108ee8d8392d2.jpg)  
(c) process of optimizing

![](/api/attachments/8YS6W4EJ/fulltext/images/ec68e8f25b129d35f97ef0b360b8b8d5f068f84c7298a4ff8aef41c7d50e0f3f.jpg)  
Fig. 5. Clockwise rotating and anticlockwise rotating.

## 4.2.5. Step 5: force-based layout refinement

We employ a force-directed layout algorithm [8] to <sup>fi</sup>ne tune the layout of an Opiniongraph. Force-directed algorithm is a classical graph visualization algorithm that adheres to esthetic principles. The forcedirected layout algorithm positions the vertices of the Opiniongraph in a two-dimensional space such that edge crossings are minimized. According to the characteristics of the Opiniongraph concentric ring layout, we re<sup>fi</sup>ne the classical force-directed layout algorithm. In particular, the OpinionRings method enforces an additional constraint regarding the region where a force-directed graph re<sup>fi</sup>nement process can take place. For example, with reference to Fig. 1, the force-directed algorithm only adjusts the vertices and edges within ring A for vertices of $V _ { A } .$ In other words, vertices are not moved beyond a ring boundary.

## 4.2.6. Step 6: adjust polar radiuses of vertices

After invoking the force-directed layout algorithm for each ring area, the polar radiuses of vertices $V _ { U }$ may be changed and they may not represent the probabilities of the corresponding actors adopting opinion A and opinion B anymore. Therefore, the OpinionRings method needs to adjust the polar radiuses of these vertices again according to the opinion probabilities derived in Section 4.2.2. The polar angle of each vertex $\boldsymbol { v } \in V _ { U }$ remains the same and our algorithm only adjusts the polar radius of v as shown in Fig. 6. The same equation (i.e., Eq. (8)) de<sup>fi</sup>ned in Section 4.2.3 is applied to compute the polar radius for each $v \in V _ { U } .$

## 4.2.7. Step 7: vertex coloring

Finally, the OpinionRings method assigns different colors to vertices for the three ring areas. The colors of vertices are selected based on the RGB color model. In particular, the green color (0, 255, 0) is applied to vertices $V _ { A }$ and magenta color (255, 0, 255) is applied to plot vertices $V _ { B }$ to maximize the contrast. In addition, users are free to choose their favorite colors for different kinds of vertices apart from the default colors. The gradient color between green and fuchsia is applied to plot vertices $V _ { U }$ according to their opinion probabilities. For example, if an actor represented by a vertex $u \in V _ { U }$ has a higher probability to adopt opinion A than opinion B, its display color is closer to green than fuchsia. As a result, users can directly observe and analyze the opinion inclination of actors who hold opinion U. More speci<sup>fi</sup>cally, the color u $( R _ { u } , G _ { u } , B _ { u } )$ of a vertex $u \in V _ { U }$ is determined according to the following equations:

![](/api/attachments/8YS6W4EJ/fulltext/images/71b7883051e7a4bf39cd65354417eb7b706c9db4e64882f09bdaff2fd6c5a0f3.jpg)  
Fig. 6. Radial adjustment.

$$
R _ {u} = R _ {A} - (1 - P _ {A u}) (R _ {A} - R _ {B})
$$

$$
G _ {u} = G _ {A} - (1 - P _ {A u}) (G _ {A} - G _ {B})\tag{12}
$$

$$
B _ {u} = B _ {A} - (1 - P _ {A u}) (B _ {A} - B _ {B}).\tag{13}
$$

<sub>ð</sub><sup>14</sup><sub>Þ</sub>

## 4.3. The OpinionRings algorithm

The OpinionRings algorithm adheres to sound esthetic principles such that users <sup>fi</sup>nd it easy to directly observe and analyze the predicted opinion distributions among actors. Accordingly, the proposed algorithm facilitates users' interactive exploration of opinion networks. As depicted in Algorithm 2, the OpinionRings algorithm begins with calculating the concentric ring radiuses according to the number of entities (vertices) of each opinion group (Step 1). Then, the algorithm estimates the opinion probabilities of actors represented by vertices $V _ { U }$ (Step 2) followed by the initialization of vertices positions of the three concentric rings (Step 3). The algorithm repeatedly performs three sub-processes: optimizing the sum of distance for each pair of vertices (Step $^ { 4 ) , }$ , invoking forcedirected layout to reduce edge crossings for each ring area (Step 5), <sup>fi</sup>ne tuning the polar radiuses of vertices $V _ { U } ( { \mathrm { S t e p } } 6 )$ until the maximum number of iterations is reached. Finally, the algorithm assigns pre-de<sup>fi</sup>ned or user-chosen colors to ring areas A and B, and generate gradient colors for vertices of ring area U based on their opinion probabilities (Step 7).

## Algorithm 2. OpinionRings concentric ring layout.

Input: Opiniongraph OG; Max. No. Iterations N Output: OpinionRings concentric ring layout 1: Calculate three ring radiuses 2: Prediction opinion probabilities for V; 3: Initialize positions of all vertices: 4: n ← 0 5: while N > n do 6: Optimize sum of distance of each pair of vertices in each ring area; 7: Invoke Force-directed layout method for each ring area 8: Adjust polar radiuses of vertices Vv; 9: $n \gets n + 1 ;$ 10: end while

11: Assign colors to vertices;

For the OpinionRings algorithm, it takes $O ( 1 )$ time to compute radiuses of three rings (Step 1), O(|E|) time to predict the opinion probabilities of vertices $V _ { U }$ (Step 2) and $O ( | V | )$ time to initialize the positions of vertices (Step 3). For each iteration, the algorithm takes O(|V|) time to optimize the sum of distance of each pair of vertices (Step 4), $O ( | V | + | E | ^ { 2 } )$ time to run force-directed layout method (Step 5) and $O ( | V _ { U } | )$ time to adjust the positions of vertices $V _ { U }$ (Step 6). Finally, coloring all vertices costs $O ( | \boldsymbol { W } | )$ time (Step 7). Thus, the total time complexity is estimated based on $O ( 1 + | E | + | V | + N ( | V _ { U } | + | V | + | E | ^ { 2 } +$ $| V _ { U } | ) \ + \ | V | )$ , where N is the maximum number of iterations. As a whole, the time complexity of the OpinionRings algorithm is characterized by $O ( | V | + | E | ^ { 2 } )$

## 5. Experiments and results

In this section, we <sup>fi</sup>rst describe the experimental procedure and benchmark data sets for the evaluations of the OpinionRings visualization algorithm. Then, the experimental results are reported and analyzed in each sub-section. In general, we performed two types of empirical experiments. First, we applied some objective measures to assess the quality of the Opiniongraph layouts generated by the OpinionRings algorithm. Second, we invited some users (both experts and novices) to directly assess the quality of the layouts produced by the OpinionRings algorithm. The data sets applied to our experiments consisted of two subsets. The <sup>fi</sup>rst subset came from classical data sets used by researchers to examine and visualize social networks. For instance, the “political blogs” data set describes a directed network of hyperlinks among blogs that discuss US politics; it was generated by Adamic and Glance in 2005 [48]. The vertices of the social network of this political blogs data set have an attribute to indicate opinion polarity for an opinion target (i.e., liberal or conservative). To make this data set compatible with our opinion network data model, we excluded some vertices of the network from our experiments. In addition, the “Facebook” data set consists of friends lists of some real users in Facebook [49]. Since the Facebook data set does not include actors' opinion polarities for some opinion targets, we manually labeled actors' opinion polarities for a chosen opinion target according to actors' public pro<sup>fi</sup>les.

The second subset of our data sets was extracted based on Sina MicroBlog's Micro Topic social network application.<sup>1</sup> Thousands of hot topics are captured by the Micro Topic application everyday. These hot topics or issues (i.e., opinion targets) are displayed via the Micro Topic application so that users can express their opinions about these topics e.g., supporting or objection to a particular issue. For our experiments, we chose two hot topics from the Micro Topic application: (1) the 2012 US election, “if you were an American citizen, who would you vote?”; (2) the <sup>fi</sup>lm rating issue in China, “do you support the development of a <sup>fi</sup>lm rating scheme in China?”. More than 10,000 Sina users participated in the voting of the <sup>fi</sup>rst topic, and among these users, 8543 users supported Barack Obama to be re-elected as the US president, with the rest of the users supporting Mitt Romney. For the second topic, 1251 users expressed their opinions; 858 users supported the implementation of a <sup>fi</sup>lm rating scheme in China and the rest of the users objected to such a proposal. To apply these opinionated expressions extracted from the Sina Micro Topic application to our experiments, we <sup>fi</sup>rst transformed the data to a format compatible with our opinion network data model. For instance, each home page of a Sina user was extracted and taken as an entity in our opinion network and the opinion targets were applied to divide the opinion data into different subsets. Moreover, some information of a user home page was extracted to create the attributes of the corresponding entity.

After the data transformation process, we successfully created 8 data sets based on the publicly available benchmark data sets and the Sina data set; the details of these data sets are depicted in Table 1. To the best of our knowledge, a speci<sup>fi</sup>c visualization algorithm for opinion networks is not yet available apart from the OpinionRings experimental method illustrated in this paper. Therefore, we adopted a classical forcedirected graph visualization algorithm [8] and a fast multiscale visualization algorithm [9] created with NodeXL<sup>2</sup> as our baseline methods. Such a comparative evaluation can better highlight the characteristics and capabilities of the OpinionRings algorithm.

Table 1  
An overview of benchmark data sets.

<table><tr><td>Data set</td><td># vertex</td><td># edges</td><td># vertex (A)</td><td># vertex (B)</td><td>Source</td></tr><tr><td>1</td><td>56</td><td>75</td><td>5</td><td>20</td><td>Blogs</td></tr><tr><td>2</td><td>101</td><td>474</td><td>15</td><td>32</td><td>Facebook</td></tr><tr><td>3</td><td>175</td><td>473</td><td>43</td><td>60</td><td>Blogs</td></tr><tr><td>4</td><td>196</td><td>842</td><td>29</td><td>63</td><td>Facebook</td></tr><tr><td>5</td><td>43</td><td>55</td><td>6</td><td>8</td><td>Hot topic 1</td></tr><tr><td>6</td><td>62</td><td>178</td><td>4</td><td>18</td><td>Hot topic 2</td></tr><tr><td>7</td><td>115</td><td>698</td><td>11</td><td>23</td><td>Hot topic 1</td></tr><tr><td>8</td><td>206</td><td>2498</td><td>23</td><td>39</td><td>Hot topic 2</td></tr></table>

## 5.1. Evaluation 1: Same-group Ratio

For the <sup>fi</sup>rst experiment, we applied an objective quantitative measure to assess the positional quality of vertices of a graphical layout generated by the OpinionRings experimental system, the force-directed baseline system or fast multiscale visualization method created with NodeXL. According to sound esthetic principles [33], when users evaluate a graphical layout of a social network, they expect that vertices representing the same community (group) to be located in adjacent places to re<sup>fl</sup>ect the locality of the particular community. In contrast, vertices representing different communities are expected to be positioned far apart to demonstrate the diversities among communities. To capture such a visualization principle, we propose a quantitative measure called the Same-group Ratio to assess the positional quality of vertices.

## De<sup>fi</sup>nition 3. Same-group Ratio

For each vertex v ∈ V of a graphical layout $L ,$ we use the location of v as a center to form a circle with radius d. Let N be the set of vertices that belong to the same group of v and located within the circle, and $N _ { A }$ be the set of all vertices covered by the circle. The Same-group Ratio $r _ { v } \in [ 0 ,$ 1] of a graphical layout L is the fraction $| N _ { S } |$ | out of $| N _ { A } | .$

$$
r _ {v} = \frac {| N _ {S} |}{| N _ {A} |}\tag{15}
$$

According to the de<sup>fi</sup>nition of the Same-group Ratio, $r _ { v }$ approaches 1 if all the vertices around v are within the same group. On the other hand, $r _ { v }$ approaches 0 if most of the vertices around v come from different groups. In other words, a large value of $r _ { v }$ suggests that vertices of the same group are really visualized in adjacent locations of the layout L. Fig. 7 show a visualization example of three different opinion groups with the colors yellow, red, and blue. For the vertex v with the yellow color, there is only one more vertex with the same color plotted inside the circle as shown in Fig. 7(a), and there are <sup>fi</sup>ve other vertices with the same color plotted inside the circle as shown in Fig. 7(b). By comparing these two <sup>fi</sup>gures, it is easy to observe that the vertices of the same group are more centrally plotted in Fig. 7(b). Accordingly, we use the Same-group Ratio to assess the vertex positioning quality of different visualization methods.

Based on the eight benchmark data sets highlighted in Table 1, we applied the proposed OpinionRings visualization method and two comparative baseline methods to visualize the corresponding opinion networks. Our experimental results obtained by averaging the Samegroup Ratios over 20 randomly chosen layouts from each data set are summarized in Fig. 8. In Fig. 8, the horizontal axis represents the Same-group Ratio that is discretized into <sup>fi</sup>ve equally divided intervals; the vertical axis shows the number of vertices whose Same-group Ratio falls in the corresponding discretized Same-group Ratio interval. As can be seen, the OpinionRings visualization method achieves a Same-group Ratio of over 0.4 for most of the cases. Commonly, the same group ratio falls in the range [0.8, 1.0] or [0.6, 0.8]. The fast multiscale visualization algorithm created with NodeXL achieves a Same-group Ratio of over 0.6 for most of the cases. In contrast, the force-directed visualization method often achieves the Same-group Ratio in the range [0.2, 0.6], and its Same-group Ratios are consistently lower than that achieved by the OpinionRings method and the fast multiscale visualization method across all data sets. As a whole, our experimental results suggest that the OpinionRings method and fast multiscale visualization algorithm created with NodeXL can better visualize the vertices of an opinion network by placing the vertices of the same group centrally and vertices of different groups separately from each other.

![](/api/attachments/8YS6W4EJ/fulltext/images/bfdd25d43d7696c92cf770b58f655a0fdea759664c90815e5b95fe6e0af74245.jpg)  
(a) Low SGR

![](/api/attachments/8YS6W4EJ/fulltext/images/48a8d75c409e9e69d18fa9734116bb230241dc837b64cae2d36204f5742f082b.jpg)  
(b) High SGR  
Fig. 7. Same-group Ratio.

(a) not on the two sides  
![](/api/attachments/8YS6W4EJ/fulltext/images/558ca4b0dcf43da52637e4344373bf42da454fe654ad21358c8407337daf3b74.jpg)

![](/api/attachments/8YS6W4EJ/fulltext/images/5dc7dc7faa4463063a38e692352297bced768677343070f68843965dbcb47053.jpg)  
(b) on the two sides  
Fig. 9. Distributions of different groups of vertices.

![](/api/attachments/8YS6W4EJ/fulltext/images/ddec6cac41ece07dbb208bef7015913925ce0ed6f22d768a03f6c842c47bf371.jpg)

## 5.2. Evaluation 2: vector angle

![](/api/attachments/8YS6W4EJ/fulltext/images/96a03f4efa549fb84e13fbe6bc8669491f8f46d3d01b96bab8e88cfacde13207.jpg)

For the visualization of opinion networks, users tend to expect that vertices belonging to the positive group (i.e., opinion A group) and vertices belonging to the negative group (i.e., opinion B group) are distributed on two opposite sides of the vertices belonging to the neutral group (i.e., opinion U group) according to the semantics of the opinion analysis model. Fig. 9 shows the comparative opinion visualization quality of two Opiniongraph layouts where vertices $V _ { U }$ are plotted with yellow color, vertices $V _ { A }$ with red color, and vertices $V _ { B }$ with blue color, respectively. Fig. ${ \mathfrak { g } } ( { \mathfrak { a } } )$ demonstrates the less ideal visualization in that vertices $V _ { A }$ and $V _ { B }$ are irregularly placed around vertices $V _ { U } ,$ while Fig. 9(b) shows a better visualization of the opinion distributions among actors by placing vertices $V _ { A }$ and $V _ { B }$ on two different sides of vertices $V _ { U } .$ It is obvious that the graphical layout shown in Fig. 9(b) provides a more intuitive display that highlights the relationships and opinion distributions of three different groups of actors. Accordingly, we develop a novel quantitative measure called Average Two-group Vectors Intersection Angle (ATVIA) to measure the opinion visualization quality achieved by a visualization algorithm.

(b) dataset 2  
(a) dataset 1  
![](/api/attachments/8YS6W4EJ/fulltext/images/be3eabe9f56ac9deee5c409077bc9947067e7b53d6b260b15f003e3acd731f83.jpg)  
(c) dataset 3

![](/api/attachments/8YS6W4EJ/fulltext/images/619048443f425c135fca149d63cc042baaafa507e670903658d2ea16a188e59d.jpg)  
(d) dataset 4

![](/api/attachments/8YS6W4EJ/fulltext/images/51500a82d8932229148243d590104b37eaed683f1e021b4a4661f1b2ff640a3d.jpg)  
(e) dataset 5

![](/api/attachments/8YS6W4EJ/fulltext/images/3f26490bc31bbb7e2ef08f95b7dbcf504f15252e17e81d95dd8b2e68f5401526.jpg)  
(f) dataset 6

![](/api/attachments/8YS6W4EJ/fulltext/images/f907d59046404fc7e7ac71021329f2a15ed500d5de1ff6c26ebdf220553dc260.jpg)  
(g) dataset 7  
Fig. 8. Experimental results of Same-group Ratio comparison

![](/api/attachments/8YS6W4EJ/fulltext/images/aff17cc93c2f53f39df63dc6694a1113d42dd97ce23a42e1184652018e868cd2.jpg)  
(h) dataset 8

![](/api/attachments/8YS6W4EJ/fulltext/images/12295f704c22173dd919e0727e62ef9747adf2b842e7d7e0d20a59aafed13b27.jpg)  
(a) not on the two sides

![](/api/attachments/8YS6W4EJ/fulltext/images/530ecf5f56ece3dedd21cda56b8e28ea95e16d7e31972617cb1324925cde8652.jpg)  
(b) on the two sides  
Fig. 10. Average Two-group Vectors Intersection Angle.

## De<sup>fi</sup>nition 4. Average Two-group Vectors Intersection Angle

For each vertex $\nu \in V _ { U }$ of a graphical layout L, we use the location of v as a center to form a circle with radius d. Let vertex $u _ { A } \in V _ { A }$ within the same circle represents an actor with opinion A and vertex $u _ { B } \in V _ { B }$ within the same circle represents an actor with opinion $\ B . { \overrightarrow { \mathsf { V U } _ { \mathsf { A } } } } ^ { }$ is a vector starting at v and ending at $u _ { A } .$ Likewise, vu<sub></sub> is a vector starting at v and ending at u<sub>B</sub>. $N _ { A }$ and $N _ { B }$ represent the sets of vertices with opinion A labels and opinion B labels within the same circle, respectively. Then, the Average Two-group Vectors Intersection Angle angleθ of v is de<sup>fi</sup>ned as follows.

$$
\text { angle } \theta = \frac {\sum_ {u _ {A} \in V _ {A}} \sum_ {u _ {B} \in V _ {B}} \operatorname{arc} \cos \left(\frac {\overrightarrow {v u _ {A}} \overrightarrow {v u _ {B}}}{| \overrightarrow {v u _ {A}} | \times | \overrightarrow {v u _ {B}} |}\right)}{| N _ {A} | \times | N _ {B} |}.\tag{16}
$$

From Eq. (16), we can learn that angleθ ∈ [0, π] is the mean angle of each vertex with an A label to each vertex with a B label. Fig. 10(a)

shows two groups of vertices irregularly distributed around the vertex v, while Fig. 10(b) depicts two groups of vertices neatly separated from two sides of v. If two vertices of different groups are placed close to each other, the angle between them tends to be small. In contrast, if two vertices of different groups are positioned on two totally different sides of v, the angle between them approaches π. To make a fair comparison based on all possible layouts, we normalize the intersection angles angleθ between two groups of vertices separated around v.

Our experimental results obtained by averaging the angleθ over 20 randomly selected layouts generated based on each benchmark data set is depicted in Fig. 11. In Fig. 11, the horizontal axis represents the Average Two-group Vectors Intersection Angle which is discretized into six equally divided intervals; the vertical axis represents the number of vertices whose Average Two-group Vectors Intersection Angles fall in the corresponding intervals. According to Fig. 11, it is easy to observe that the ATVIA of the graphical layouts produced by the OpinionRings method is over ${ \scriptstyle { \frac { 2 } { 3 } } } \pi$ for most data sets. The ATVIA achieved by the OpinionRings method mostly lies in the ranges <sup>2</sup> π; <sup>5</sup> π	  and <sup>5</sup> π; π	 .

![](/api/attachments/8YS6W4EJ/fulltext/images/76a280e157b94d7e89b9ca44391fa3efc59be78ce2d40c3a21fc8fa9c2f632ff.jpg)  
(a) dataset 1

![](/api/attachments/8YS6W4EJ/fulltext/images/ae3996bc2572259bd76ef07e5758b3bb97291c74093bcb256b710b3209f333df.jpg)  
(b) dataset 2

![](/api/attachments/8YS6W4EJ/fulltext/images/78c829e534acb685b33c14b6d5858a06e947bea4c1ea394517110b2df4e417a3.jpg)  
(c) dataset 3

![](/api/attachments/8YS6W4EJ/fulltext/images/6bafa61ec82fa1e20e5f47d75bef442951d837d1ad4d72a1e94dd2154612b56c.jpg)  
(d) dataset 4

![](/api/attachments/8YS6W4EJ/fulltext/images/b43a4365d7b1135287b8189ace0d73e786b3ad26b46f4f5cdd8af2d5e7606030.jpg)  
(e) dataset 5

![](/api/attachments/8YS6W4EJ/fulltext/images/6df6a8090ef615668a8a4a6a62c7aede837e4f5f9313b46da004348c4a6d26d9.jpg)  
(f) dataset 6

![](/api/attachments/8YS6W4EJ/fulltext/images/8bc43a10a60f61fd9ad98a34006ba1db693aa2530a0dc75247d4304e0e0f25be.jpg)  
(g) dataset 7

![](/api/attachments/8YS6W4EJ/fulltext/images/0886a19fadf7dec46db532a20a6935f537390fbca5f1eb61162929aa604e969b.jpg)  
(h) dataset 8  
Fig. 11. Experimental results of Average Two-group Vectors Intersection Angle.

On the other hand, the ATVIA of the graphical layouts generated by the force-directed method often falls in the interval 0; <sup>π</sup>	  for most of the data sets and the ATVIA of the graphical layouts generated by the fast multiscale visualization algorithm created with NodeXL mostly lies in the ranges $\textstyle \left[ { \frac { 1 } { 3 } } \pi , { \frac { 1 } { 2 } } \pi \right]$ and $[ \bar { \frac { 1 } { 2 } } \pi , \frac { 2 } { 3 } \pi ]$ . These experimental results suggest that vertices of the positive opinion group and vertices of the negative opinion group tend to be plotted on two different sides of the vertices representing the neutral opinion group in the layouts generated by the OpinionRings method. In contrast, the layouts produced by the force-directed method contain irregularly displayed opinion groups and the fast multiscale visualization algorithm created with NodeXL only positioned the vertices according to their opinion groups, omitting the interrelationships between opinion groups. As a whole, the opinion visualization quality of the OpinionRings method is the highest.

## 5.3. Evaluation 3: comparative user-based evaluation

More speci<sup>fi</sup>cally, we would like to examine both expert users and novices' perceptions about the system generated graphical layouts because the proposed OpinionRings method will be used by both technical and non-technical people. We randomly invited 10 postgraduate students with research experience in graphics and visualization technology (i.e., the expert group) and 13 postgraduate students without any technical background about visualization technology (i.e., the novice group) to participate in this user study. The users were then presented with the graphical layouts generated by the OpinionRings method and two comparative methods in random order. A sample of these graphical layouts is shown in Fig. 12. Users were then asked to rate each graphical layout with respect to <sup>fi</sup>ve visual aspects according to a 10-point Likert-scale with 1 as totally unsatisfactory and 10 as totally satisfactory. The <sup>fi</sup>ve visual aspects for evaluation are: (A1) visualization of different groups of entities, (A2) positional quality of entities, (A3) easy to infer the opinion inclination of neutral entities, (A4) opinion visualization quality and (A5) informativeness of the graphical layout.

For the third experiment, we aim to evaluate real-world users' perceptions about the quality of the graphical layouts generated by the OpinionRings experimental method and two comparative methods.

The result of our user-based evaluation is depicted in Table 2. From Table 2, it is easy to observe that users' perceived ratings of the graphical layouts generated by the OpinionRings method are consistently higher than that produced by the two comparative methods for all the <sup>fi</sup>ve visualization aspects. The column with label “SD” refers to the standard deviation of user ratings in Table 2.

![](/api/attachments/8YS6W4EJ/fulltext/images/1ab21472af579c44ef9818d2313c814c2238ac96dcd0eb269f7b7ec76209ddd5.jpg)  
(a) D1 (OR)

![](/api/attachments/8YS6W4EJ/fulltext/images/2c396ec0d0771e46fb1fefdc2ff66ed22678eb8e3f3556629ac9f5860932ddf0.jpg)

(b) D1 (Force)  
![](/api/attachments/8YS6W4EJ/fulltext/images/82a6fe8f1b9b2706e2293fcae5b042c3e5856f9b09336ada628a93cdc82b99e8.jpg)  
(c) D1 (FM)

![](/api/attachments/8YS6W4EJ/fulltext/images/c67e67d5f0935573149e258633bcf539154f9117483e2b76e6c193c02e604867.jpg)

![](/api/attachments/8YS6W4EJ/fulltext/images/bbf08c916c5b92c25a3ce89a7cde52347e3d8ea02251de179260d4b620f95ae8.jpg)  
(g) D3 (OR)  
(h) D3 (Force)

(d) D2 (OR)  
![](/api/attachments/8YS6W4EJ/fulltext/images/47ec99dcb3c19bedd495c77796d9575a733eaa98a39bde3d1588929dbaceb2a3.jpg)  
(i) D3 (FM)

![](/api/attachments/8YS6W4EJ/fulltext/images/6c2312dc2eb8de3eb4c604cfefac831b65b155703f2e3aa2a0f5ec8b26dadde9.jpg)

(e) D2 (Force)  
![](/api/attachments/8YS6W4EJ/fulltext/images/200ac8345efc33de3a58437feca1e3f98700d757b9b3b47406f795b567a09833.jpg)

![](/api/attachments/8YS6W4EJ/fulltext/images/823f4ca1ca97c3d1dfc51158231490e749fe5df41280752ef8463c680818e7bb.jpg)  
(f) D2 (FM)

![](/api/attachments/8YS6W4EJ/fulltext/images/f9d5212a5e48d9cec0a3223f8ded7f85c01f2ed583be476e60ef3ffdf7e2e223.jpg)  
(j) D4 (OR)

![](/api/attachments/8YS6W4EJ/fulltext/images/225cfcd2cdf9301dbd56d71379af0fc6f702d9e7c70152adc00aa68c4c6d4549.jpg)  
(k) D4 (Force)

![](/api/attachments/8YS6W4EJ/fulltext/images/dd537902ec33efb756c6457d4cba0a7483a4adad9e337b15f591e0b27478c455.jpg)  
(l) D4 (FM)

![](/api/attachments/8YS6W4EJ/fulltext/images/684604c2e899767b0f8360ba7476cff4b4d85985d9c067d8d8686d5057eaa220.jpg)  
(m) D5 (OR)

![](/api/attachments/8YS6W4EJ/fulltext/images/94ace394c8f3bf7123c12867fa144e4f690910bc0d632261ae5adf5be29b3106.jpg)  
(n) D5 (Force)

(o) D5 (FM)  
![](/api/attachments/8YS6W4EJ/fulltext/images/064b0a3e52dd553a8b6ee5029fae1d0ea27e3749669db400873e6f1cf034166d.jpg)

![](/api/attachments/8YS6W4EJ/fulltext/images/bbb85983e931de4f5cb27c3a877b4de5a766df3070e59f700b5a3755648bd915.jpg)  
(p) D6 (OR)

![](/api/attachments/8YS6W4EJ/fulltext/images/6571d85919af814b9086aa684fb5d5d74c7b415d5c514ce964332a050d4353a7.jpg)  
(q) D6 (Force)

![](/api/attachments/8YS6W4EJ/fulltext/images/1d995bf61ea1de71ebb77dcb2a9fa4e88867ba63b29e749d6b01b790581596bd.jpg)  
(r) D6 (FM)

![](/api/attachments/8YS6W4EJ/fulltext/images/e52434a95e2589ac44b189e29dc4fb75e3a9f0a56911326c065b305a3c956194.jpg)  
(s) D7 (OR)

![](/api/attachments/8YS6W4EJ/fulltext/images/79d92808e03db543dc224aedf9b9747d9f2231c66da0b2b8a9a120a06fcc0eee.jpg)  
(t) D7 (Force)

![](/api/attachments/8YS6W4EJ/fulltext/images/5e2728cdbce4240430686ec56569b5492b315ec6de1bf79910c5f95fba45f15c.jpg)  
(u) D7 (FM)

![](/api/attachments/8YS6W4EJ/fulltext/images/e95ba21814180ddbb224726279516e30b09fbf2a753170a1a6f0e13f1676740e.jpg)  
(v) D8 (OR)

![](/api/attachments/8YS6W4EJ/fulltext/images/b106f6a0e4794454830732f611f3b98c6426c1daa9784bedbf22c2bc61abadd6.jpg)  
(w) D8 (Force)

![](/api/attachments/8YS6W4EJ/fulltext/images/96cc55ff0666fbfbc582e762f834d205c2b4b83abb26566c29516cb01f719ac3.jpg)  
(x) D8 (FM)  
Fig. 12. A sample of comparative layouts by three methods. OR: OpinionRings. Force: Force-directed. FM: Fast multiscale

Table 2  
Perceived visual quality by different types of users.

<table><tr><td rowspan="2">Type of user</td><td rowspan="2">Method</td><td colspan="2">A1</td><td colspan="2">A2</td><td colspan="2">A3</td><td colspan="2">A4</td><td colspan="2">A5</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td rowspan="3">Expert</td><td>OpinionRings</td><td>8.70</td><td>0.82</td><td>8.05</td><td>0.69</td><td>9.05</td><td>0.64</td><td>8.80</td><td>0.42</td><td>8.45</td><td>0.50</td></tr><tr><td>Force-directed</td><td>2.05</td><td>1.30</td><td>3.25</td><td>1.09</td><td>2.80</td><td>1.87</td><td>2.45</td><td>2.22</td><td>3.00</td><td>1.05</td></tr><tr><td>Fast multiscale</td><td>7.20</td><td>0.99</td><td>3.50</td><td>0.71</td><td>3.00</td><td>0.62</td><td>5.10</td><td>0.55</td><td>6.10</td><td>1.01</td></tr><tr><td rowspan="3">Novice</td><td>OpinionRings</td><td>9.08</td><td>0.76</td><td>7.31</td><td>0.75</td><td>9.38</td><td>0.77</td><td>8.38</td><td>0.87</td><td>7.85</td><td>0.99</td></tr><tr><td>Force-directed</td><td>3.85</td><td>1.21</td><td>2.62</td><td>0.77</td><td>2.00</td><td>0.82</td><td>1.92</td><td>0.64</td><td>2.92</td><td>0.95</td></tr><tr><td>Fast multiscale</td><td>8.10</td><td>0.64</td><td>4.40</td><td>0.42</td><td>2.8</td><td>1.07</td><td>4.20</td><td>1.59</td><td>5.70</td><td>1.12</td></tr></table>

The reason why different types of users rate the graphical layouts generated by the OpinionRings method much higher is that the OpinionRings method can clearly display vertices of different groups in three non-overlapping concentric ring areas and vertices within the same group are positioned according to their similarities as demonstrated by Fig. 12. Such a graphical layout enables users (experts or novices) to easily observe and analyze entities and their relationships, and the distributions of opinions held by entities. In contrast, the forcedirected visualization method randomly plots vertices on a screen canvas. The fast multiscale visualization algorithm created with NodeXL considers the groups in opinion networks. For neutral actors, fast multiscale visualization algorithm only treats them as a common opinion group in an opinion network, so it lacks the prediction to the neutral actors. As a result, it is much more dif<sup>fi</sup>cult for users to observe the relationships among entities and the distributions of opinions among different opinion groups. Moreover, one distinct advantage of the OpinionRings method is that the opinion inclinations of neutral entities are speci<sup>fi</sup>cally visualized based on their distances and colors with respect to other entities holding positive opinions or negative opinions. As a result, users generally prefer the graphical layouts produced by the OpinionRings method.

In this experiment, most users feel positive about the concentric ring graphical layout produced by the OpinionRings system. Users generally think that using three non-overlapping concentric rings to represent three groups of actors and the corresponding opinion distributions is effective. Users also feel that the speci<sup>fi</sup>c color scheme and vertices positioning scheme adopted by OpinionRings can facilitate the analysis of different kinds of opinion holders and the inference of the opinion inclinations of neutral actors.

## 5.4. Evaluation 4: validation of predicted user opinion priorities for OpinionRings

Subsequently, we evaluate the accuracy of the predicted user opinion priorities. The data set “political blogs” describes a directed network of hyperlinks among blogs that discuss US politics. Actors in the data set “political blogs” have political orientations, conservative or liberal. To make this data set compatible with our opinion network data model, we have excluded some political orientations of vertices, which we treat as neutral actors. We validate the predicted opinion priorities against their actual political orientations. For the four data sets from Sina MicroBlog's Micro Topic, we conduct an online survey to collect the actual opinions of neutral actors about the two hot topics mentioned above. 95% of the subjects that we randomly chose actually respond to our survey. The results of our experiment are depicted in Table 3. From Table 3, the prediction accuracies for two “political blogs” data sets are 0.698 and 0.734, respectively. For the four data sets based on the Sina MicroBlog's Micro Topic, the prediction accuracies by matching actors' actual opinions with the opinion inclination predicted by OpinionRings are 0.801, 0.676, 0.621 and 0.733, respectively. From our experimental results, we can conclude that the opinion inclinations predicted by OpinionRings are very close to the actual opinions of neutral actors.

Table 3  
Predicted user opinion priority validation

<table><tr><td>Data set</td><td>Accuracy</td></tr><tr><td>Data set 1</td><td>0.698</td></tr><tr><td>Data set 3</td><td>0.734</td></tr><tr><td>Data set 5</td><td>0.801</td></tr><tr><td>Data set 6</td><td>0.676</td></tr><tr><td>Data set 7</td><td>0.621</td></tr><tr><td>Data set 8</td><td>0.733</td></tr></table>

Our opinion prediction module is independent of other modules of the OpinionRings method. Accordingly, the opinion prediction function of our proposed method can be further enhanced based on the state-ofthe-art classi<sup>fi</sup>cation methods developed in the <sup>fi</sup>eld of machine learning.

## 5.5. Case study

Finally, we present a short case study to demonstrate the capabilities and usefulness of the OpinionRings layout. Data set 3 was extracted based on the data set “political blogs”. Fig. 13 shows the OpinionRings layout for data set 3.

In Fig. 13, we can observe that the actors in data set 3 are classi<sup>fi</sup>ed into 3 groups. The green-colored vertices in the central area represent conservative actors and the magenta-colored vertices in the outer ring area represent liberal actors. The neutral actors are placed in the middle ring area. We can easily observe and analyze the opinion inclinations of these neutral actors by simply taking a glance at their colors and their distances to the two groups of actors with certain opinions. For instance, since the colors of the vertices in the green rounded rectangle are close to green, it is probable that these actors would be conservative actors at a later stage. Accordingly, since the colors of the vertices in the purple oval are close to magenta, it is probable that these actors would be liberal actors at a later stage. For a vertex u, we can infer that its opinion polarity is conservative as its color is close to green and the distance between u and the vertices in group A is shorter than the distance between u and the vertices in group B. Similarly, for a vertex v, we can also infer its opinion polarity is liberal according to its color and position. If users are interesting to a certain vertex, more information (e.g., User ID, User Image, Blog Context) will be shown when you choose it. During election season, the campaign manager of a presidential candidate is easy to know which group of actors hold a certain opinion polarity (e.g., positive or negative) about his candidate, and <sup>fi</sup>nd group of actors have a neutral opinion polarity to persuade by the graphical representation of OpinionRings. Likewise, for directed marketing, managers would like to know who feels positive about their products, and then they may recruit these positive actors to write blog messages or online product reviews to in<sup>fl</sup>uence those who have a neutral opinion polarity to change their minds. Meanwhile, the managers would also like to identify the group of actors who feel negative about her products, and try to understand their concerns for subsequent product redesign and enhancement. All these information can be obtained by OpinionRings easily. Thus, the practical implication of our research is that business managers or government of<sup>fi</sup>cials can apply OpinionRings to extract and visualize valuable social intelligence from online social networks to facilitate their decision-making processes.

![](/api/attachments/8YS6W4EJ/fulltext/images/ec514a9f008edb274fdfb8af2af09731a8881d2e9c0163b7e79c99be9bc7410c.jpg)  
Fig. 13. Case study for data set 3.

## 6. Conclusions

Extracting and visualizing different opinions held by actors of online social networks provide policy-makers with valuable collective social intelligence to enhance their decision-making processes. The main contribution of our research is the design and development of a visualization method called OpinionRings for visualizing and predicting the opinion distributions among different groups of actors. More speci<sup>fi</sup>cally, the OpinionRings method leverages three concentric rings with various colors to summarize the opinions of positive, negative, and neutral opinion holders. In addition, it is underpinned by a collective classi<sup>fi</sup>cation algorithm to predict and visualize the opinion inclinations of neutral opinion holders according to their similarities with positive and negative opinion holders. Through objective quantitative evaluations, it is shown that the OpinionRings method outperforms the traditional visualization methods in terms of the qualities of graphical layouts. Moreover, user-based evaluations con<sup>fi</sup>rm that the graphical layouts generated by the OpinionRings method are perceived with higher informativeness and predictive power. Future work will apply the OpinionRings method to support a wide range of real-world applications such as the visualization of multi-relational social networks. Furthermore, more sophisticated classi<sup>fi</sup>cation methods will be explored to enhance the predictive power of the OpinionRings method. Finally, a larger scale of controlled experiments and usability studies will be performed to further examine both the effectiveness and the ef-<sup>fi</sup>ciency of the OpinionRings method under the Big Data environment.

## Acknowledgments

Yunming Ye's work was supported in part by NSFC under Grant No. 61272538, Shenzhen Science and Technology Program under Grant No. JCYJ20140417172417128, and the Shenzhen Strategic Emerging Industries Program under Grant No. JCYJ20130329142551746. Raymond Y.K. Lau's work was supported in part by Research Grants Council of the Hong Kong Special Administrative Region (China) under Grant No. CityU 145712, and the Shenzhen Municipal Science and Technology R&D Fund — Basic Research Program (JCYJ20130401145617281 and

JCYJ20140419115614350). Yueping Li's work was supported in part by NSFC under Grant No. 61303103, and the Shenzhen Science and Technology Program under Grant No. JCY20130331150354073.

## References

[1] Y.-M. Li, T.-Y. Li, Deriving market intelligence from microblogs, Decision Support Systems 55 (1) (2013) 206–217.

[2] B. Pang, L. Lee, Opinion mining and sentiment analysis, Foundations and Trends in Information Retrieval 2 (1-2) (2008).1–135

[3] K. Kim, J. Lee, Sentiment visualization and classi<sup>fi</sup>cation via semi-supervised nonlinear dimensionality reduction, Pattern Recognition 47 (2) (2014) 758–768.

[4] A. Montoyo, P. Martnez-Barco, A. Balahur, Subjectivity and sentiment analysis: an overview of the current state of the area and envisaged developments Decisior Support Systems 53 (4) (2012) 675–679.

[5] J. Gao, C. Zhang, K. Wang, S. Ba, Understanding online purchase decision making: the effects of unconscious thought, information quality, and information quantity, Decision Support Systems 53 (4) (2012) 772–781.

[6] F.H. Khan, S. Bashir, U. Qamar, Tom: Twitter opinion mining framework using hybrid classi<sup>fi</sup>cation scheme, Decision Support Systems 57 (2014) 245–257.

[7] S.K. Card, J.D. Mackinlay, B. Schneiderman, Readings in Information Visualization: Using Vision to Think, Morgan Kaufmann, 1999.

[8] P. Eades, M.L. Huang, Navigating clustered graphs using force-directed methods, Journal of Graph Algorithms and Applications 4 (3) (2000) 157–181.

[9] D.H.Y. Koren, A fast multi-scale method for drawing large graphs, Journal of Graph Algorithms and Applications 6 (3) (2002) 179–202.

[10] L.C. Freeman, Visualizing social networks, Journal of Social Structure 1 (1) (2000) 4.

[11] M.L. Northway, A method for depicting social relationships obtained by sociometric testing, Sociometry (1940) 144–150.

[12] R. Therón, Hierarchical–temporal data visualization using a tree-ring metaphor, Smart Graphics 2006, pp. 70–81.

[13] U. Brandes, P. Kenis, D. Wagner, Communicating centrality in policy network drawings, IEEE Transactions on Visualization and Computer Graphics 9 (2) (2003) 241–253.

[14] K.-P. Yee, D. Fisher, R. Dhamija, M. Hearst, Animated exploration of dynamic graphs with radial layout, Presented at IEEE Symposium on Information Visualization, 2001.

[15] M. Farrugia, N. Hurley, A. Quigley, Exploring temporal ego networks using small multiples and tree-ring layouts, ACHI 2011, The Fourth International Conference on Advances in Computer–Human Interactions 2011, pp. 79–88.

[16] K. Misue, Drawing bipartite graphs as anchored maps, Proceedings of the 2006 Asia-Paci<sup>fi</sup>c Symposium on Information Visualisation, vol. 60 2006, pp. 169–177.

[17] K. Misue, Anchored Maps: Visualization Techniques for Drawing Bipartite Graphs, 2007. 106–114.

[18] K. Saito, T. Iwata, N. Ueda, Visualization of bipartite graph by spherical embedding INNS (2004) (in Japanese)

[19] L. Zheng, L. Song, P. Eades, Crossing minimization problems of drawing bipartite graphs in two clusters, Proceedings of the 2005 Asia-Paci<sup>fi</sup>c Symposium on Information Visualisation vol, 45 2005 pp. 33–37.

[20] E. Di Giacomo, L. Grilli, G. Liotta, Drawing bipartite graphs on two curves, Graph Drawing 2007, pp. 380–385.

[21] J. Heer, D. Boyd, Vizster: visualizing online social networks, IEEE Symposium on Information Visualization 2005, pp. 32–39.

[22] Z. Shen, K.-L. Ma, T. Eliassi-Rad, Visual analysis of large heterogeneous social networks by semantic and structural abstraction, IEEE Transactions on Visualization and Computer Graphics 12 (6) (2006) 1427–1439.

[23] N. Cao, J. Sun, Y.-R. Lin, D. Gotz, S. Liu, H. Qu, FacetAtlas: multifaceted visualization for rich text corpora, IEEE Transactions on Visualization and Computer Graphics 16 (6) (2010) 1172–1181.

[24] N. Cao, D. Gotz, J. Sun, Y.-R. Lin, H. Qu, Solarmap: multifaceted visual analytics for topic exploration, IEEE 11th International Conference on Data Mining 2011, pp. 101–110.

[25] A. Perer, B. Shneiderman, Balancing systematic and <sup>fl</sup>exible exploration of social networks, IEEE Transactions on Visualization and Computer Graphics 12 (5) (2006) 693–700.

[26] Y. Wu, F. Wei, S. Liu, N. Au, W. Cui, H. Zhou, H. Qu, Opinionseer: interactive visualization of hotel customer feedback, IEEE Transactions on Visualization and Computer Graphics 16 (6) (2010) 1109–1118.

[27] S. Morinaga, K. Yamanishi, K. Tateishi, T. Fukushima, Mining product reputations on the web, Proceedings of the Eighth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2002, pp. 341–349.

[28] M.L. Gregory, N. Chinchor, P. Whitney, R. Carter, E. Hetzler, A. Turner, User-directed sentiment analysis: visualizing the affective content of documents. Proceedings of the Workshop on Sentiment and Subiectivity in Text 2006 pp. 23-30

[29] C. Chen, F. Ibekwe-SanJuan, E. SanJuan, C. Weaver, Visual analysis of con<sup>fl</sup>icting opinions, IEEE Symposium On Visual Analytics, Science And Technology 2006, pp. 59–66.

[30] B. Liu, M. Hu, J. Cheng, Opinion observer: analyzing and comparing opinions on the web, Proceedings of the 14th International Conference on World Wide Web 2005, pp. 342–351.

[31] D. Oelke, M. Hao, C. Rohrdantz, D.A. Keim, U. Dayal, L.-E. Haug, H. Janetzko, Visual opinion analysis of customer feedback data, IEEE Symposium on Visual Analytics, Science and Technology 2009, pp. 187–194

[32] S.A. Macskassy, F. Provost, Classi<sup>fi</sup>cation in networked data: a toolkit and a univariate case study The Journal of Machine Learning Research 8 (2007) 935–983.

[33] E.R. Gansner, Y. Koren, Improved circular layouts, Graph Drawing 2007, pp. 386–398.

[34] M.J. Brzozowski, T. Hogg, G. Szabo, Friends and foes: ideological social networking, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems 2008, pp. 817–820.

[35] M. Szell, R. Lambiotte, S. Thurner, Multirelational organization of large-scale social networks in an online world, Proceedings of the National Academy of Sciences 107 (31) (2010) 13636–13641.

[36] J. Leskovec, D. Huttenlocher, J. Kleinberg, Predicting positive and negative links in online social networks, Proceedings of the 19th International Conference on World Wide Web 2010, pp. 641–650.

[37] J. Leskovec, D. Huttenlocher, J. Kleinberg, Signed networks in social media, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems 2010, pp. 1361–1370.

[38] J. Kunegis, A. Lommatzsch, C. Bauckhage, The slashdot zoo: mining a social network with negative edges Proceedings of the 18th International Conference on World Wide Web 2009, pp. 741–750.

[39] B. Liu, Sentiment analysis: a multi-faceted problem, IEEE Intelligent Systems 25 (3) (2010) 76–80.

[40] L.K. McDowell, K.M. Gupta, D.W. Aha, Cautious collective classi<sup>fi</sup>cation, The Journal of Machine Learning Research 10 (2009) 2777–2836.

[41] P. Sen, G. Namata, M. Bilgic, L. Getoor, Collective classi<sup>fi</sup>cation, Encyclopedia of Machine Learning 2010, pp. 189–193

[42] Q. Lu, L. Getoor, Link-based classi<sup>fi</sup>cation, ICML, vol. 3 2003, pp. 496–503.

[43] J. Neville, D. Jensen, Relational dependency networks, The Journal of Machine Learning Research 8 (2007) 653–692.

[44] D. Jensen, J. Neville, B. Gallagher, Why collective inference improves relational classi<sup>fi</sup>cation, Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2004, pp. 593–598

[45] W.R. Gilks, S. Richardson, D.J. Spiegelhalter, Markov Chain Monte Carlo in Practice vol. 21996.

[46] B. Taskar, P. Abbeel, D. Koller, Discriminative probabilistic models for relational data, Proceedings of the Eighteenth Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence 2002, pp. 485–492.

![](/api/attachments/8YS6W4EJ/fulltext/images/a0301895ceb6e5b96120a7ab8dd77ec4d62f156acdcdb3ec84138df6ba71ac1b.jpg)

![](/api/attachments/8YS6W4EJ/fulltext/images/3962ac6e393e9294aa0e65cb91b4d4e4c5d155c213131300bf146f4b4c208981.jpg)

[47] B. Ham, D. Min, K. Sohn, A generalized random walk with restart and its application in depth up-sampling and interactive segmentation, IEEE Transactions on Image Processing 22 (7) (2013) 2574–2588.

[48] L.A. Adamic, N. Glance, The political blogosphere and the 2004 us election: divided they blog, Proceedings of the 3rd International Workshop on Link Discovery 2005, pp. 36–43.

[49] J. McAuley, J. Leskovec, Learning to discover social circles in ego networks, Advances in Neural Information Processing Systems, 25 2012, pp. 548–556.

![](/api/attachments/8YS6W4EJ/fulltext/images/b0c4e68e7fb62736a2a4ce22e1f328dbdc70fed145edb56e702520e8c2a57445.jpg)  
Xiaolin Du received her Master's Degree in Computer Science from Harbin Institute of Technology in 2009. Currently, she is a PhD candidate in the Shenzhen Graduate School. Harbin Institute of Technology. Her research interests involve data mining, social network visualization and social network discovering.

![](/api/attachments/8YS6W4EJ/fulltext/images/ba2e5bb307084769266eb53fca10fa50f2922476bc6cd97ef3fee62156d7f045.jpg)

Yunming Ye received a Ph.D. in Computer Science from Shanghai Jiao Tong University. He is now a professor in the Shenzhen Graduate School, Harbin Institute of Technology. His research interests include data mining, text mining, and ensemble learning algorithms.

Raymond Y. K. Lau is an Associate Professor in the Department of Information Systems at the City University of Hong Kong. He holds a Ph.D. in Information Technology from Oueensland University of Technology. Australia. Dr. Lau has worked at the academia and the ICT industry for over twenty years with over 100 refereed international journals and conference papers. His research work has been published in renowned journals such as ACM Transactions on Information Systems, IEEE Transactions on Knowledge and Data Engineering, IEEE Internet Computing, INFORMS Journal on Computing, MIS Quarterly, and Decision Support Systems.

Yueping Li received his PhD in Computer Science from Sun Yat-sen University in 2008. His research interests involve web mining, graph algorithm and optimization.
