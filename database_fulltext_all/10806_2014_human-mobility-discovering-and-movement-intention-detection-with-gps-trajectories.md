---
otero_id: 10806
otero_key: "7263QTUB"
title: "Human mobility discovering and movement intention detection with GPS trajectories"
authors: "Hua Yuan; Yu Qian; Rui Yang; Ming Ren"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Human mobility discovering and movement intention detection with GPS trajectories

Hua Yuan <sup>a,</sup>⁎, Yu Qian <sup>a</sup>, Rui Yang <sup>a</sup>, Ming Ren

<sup>a</sup> School of Management and Economics, University of Electronic Science and Technology of China, Chengdu 610054, China

<sup>b</sup> School of Information Resource Management, Renmin University of China, Beijing 100872, China

a r t i c l e i n f o

Available online xxxx

Keywords: Stationary sub-trajectory Clustering Path network Movement intention

## a b s t r a c t

In this paper, we aim to mine the interesting locations and the frequent travel sequences in a given geo-spatial region, by taking into account the users' historic travel experiences as well as the correlation between locations. First, a new partition method is proposed to divide the trajectories into a set of line segments (which contains the stationary moving sequence), the start and end points of which are collected as characteristic points. Then some common clustering methods are introduced to cluster the geographical-similar endpoints into groups for <sup>fi</sup>xed territories detecting reason. Finally an abstract path network is generated which shows the link relations between the mined <sup>fi</sup>xed territories. The proposed method can be used to detect a user's frequent movement paths as well as <sup>fi</sup>xed territories for a better personalized geographical recommendation.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

With the widespread use of miniaturized GPS devices, such as integration of mobile phone and micro GPS chip, recording the trace data of moving objects becomes extremely easy and a useful work. In recent years, many users start recording their outdoor movements with GPS trajectories and sharing GPS logs within web-based communities. By that, individuals are able to visualize and manage their GPS trajectories for route tracing, travel experience sharing, life logging, sports activity analysis, multimedia content managing, etc. [1]. More important, people can obtain reference knowledge from others' life experiences. For instance, with the shared trajectory information, an individual can understand an unfamiliar area (city) in a fast way and plan his/her own journeys in such an area ef<sup>fi</sup>ciently. Meanwhile, such information would enable mobile guides [2] since the mobile users are more likely to enjoy the high quality travel experience of others.

The recorded trajectories are so useful that most geography related organizations have accumulated a huge amount of GPS trajectories which can provide enormous business opportunity in geographical navigation and recommendation system [3]. For the most of the current GPS applications, a common problem is that they tend to plan a stationary navigation route and recommend <sup>fi</sup>xed points of interests (POIs) for potential users according to the prede<sup>fi</sup>ned geo-spacial relations, so as to a city map is needed. However, the labeled POIs and paths in a map is stationary, relatively trivial, it may have few relationship with the user's present movement. Therefore, the geographic service system cannot do a better personalization recommendation and has no extra valuable information for those who have regular routes. For example, such geographic service system would result to loss of business opportunities from ordinary city residents since they are very familiar with the geographical environment of their daily travel. These residents have <sup>fi</sup>xed territories of their own and tend to travel along their personal favorite paths rather than a route suggested by the GPS navigation system basing on the simple distance, speed or economic principles. They do not need any navigation but the up-to-date information about their familiar paths and what are the new emerges in their own <sup>fi</sup>xed territories. Thus, a good geographic information service system must be useful for two different types of users as shown in Table 1.

For a better personalization recommendation, a necessary condition is to know the movement intention of a moving object in advance. Generally, it can be inferred from the historical trajectory data [4], such as frequent path and fixed territories. However, it is hard to get such information in view of three reasons. First, most of the current GPS applications still directly use raw GPS data, for instance, route navigation and POI labeling, without much understanding [1]. Facing such a huge mass of various trajectories, it is impossible for a user to browse each GPS trajectory one by one to <sup>fi</sup>lter out what he/she real needed. Second, GPS data are always non-uniform, sparse, lost and inconsistent with the endpoints in cases when the users turn on and off the GPS-enabled devices casually. So, any two trajectories could not be identical even if they were used to record the same path. Third, it is known to all that a large number of GPS point data is used in recording a trajectory while few of them are keys to show interesting information about the movement intention, i.e., the next destination of a moving object. Hence, so far, these applications cannot provide more support for giving people interesting information on geo-spatial locations and ef<sup>fi</sup>cient route suggestions about how to reach the people's interested destinations.

In this paper, based on the GPS trajectory analysis, we aim to mine interesting locations and the frequent travel sequences in a given geospatial region by taking the users' historic travel experiences into account as well as the correlation between locations. To that end, we <sup>fi</sup>rstly partition a trajectory into a set of line segments, i.e., the stationary sub-trajectory (SST), so that the key information of the trajectory can be represented by all the endpoints (namely characteristic points) of the segments, and lots of GPS points with little information are ignored in future computation. Fig. 1 is an example of the partition method. In addition, we know that user's different travels in the same path may result in similar movement behaviors (moving direction, turning, stop etc.) which would lead to similar line segment partitions, thus we cluster the similar endpoints into groups to detect the <sup>fi</sup>xed territories secondly. Finally, we construct an abstract path network to indicate the linkage relations between the found <sup>fi</sup>xed territories which can be used to investigate the user's movement patterns and predict future destinations. The main contributions of this paper can be summarized as follows:

Table 1  
Contents recommended for different types of users.

<table><tr><td>User type</td><td>POI recommendation</td><td>Path recommendation</td></tr><tr><td>City strangers</td><td>Interested POIs</td><td>Convenient path to POIs</td></tr><tr><td>City residents</td><td>Information (e.g., what is new) about personal fixed territories</td><td>Information (e.g., availability) about personal path</td></tr></table>

• We present a novel partition method to obtain SSTs. The primary advantage of the method is the low computational cost and it can be used to partition any trajectories with different forms of start movement (start position, speed, direction and so on). This is very important since the studied trajectories are non-uniformed and sparse.

• We propose a weighted path network model to indicate the moving sequence relationships between different <sup>fi</sup>xed territories. The network is an abstract structure of a set of trajectories and their common <sup>fi</sup>xed territories.

• We address an association rule based inference model to detect the traveler's movement intention by representing all the historic moving sequences with a set of transactional itemset. The method can be performed easily for travelers' movement detection with their path network.

The proposed method can be used to detect a traveler's frequent paths as well as <sup>fi</sup>xed territories for better personalized geographic recommendation. The remainder of this paper is organized as follows. Section 2 presents the related work. In Section 3, we sketch out the methodology as a whole and describe the function of the main parts of the framework. Sections 4 to 6 detail the methods of trajectory partition, <sup>fi</sup>xed territory identi<sup>fi</sup>cation and user's movement intention detection respectively. Section 7 shows the experimental results. We <sup>fi</sup>nally conclude our work in Section 8.

## 2. Related work

In this section, we brie<sup>fl</sup>y review the important studies related to this research.

## 2.1. Trajectory pattern mining

The trajectory pattern mining problem was introduced in [5], in which, trajectory pattern represents a set of individual trajectories that shares the property of visiting the same sequence of places with similar travel times. These patterns have two central notions of the regions of interest and the typical travel time of moving objects. Following this work, some important efforts have been devoted into mining travel sequences [6]. Cao et al. [7] de<sup>fi</sup>ned pattern elements as spatial regions around frequent line segments and patterns were detected using a substring tree structure, however, the temporal information was not assumed in this work. In [5], both space and time were taken into consideration to de<sup>fi</sup>ne a trajectory pattern.

In [8], the authors proposed a partition-and-group framework for clustering trajectories, which partitioned a trajectory into a set of line segments, and then, grouped similar line segments together into a cluster. The primary advantage of this framework was the discovery of common sub-trajectories from a trajectory database which is the main inspiration for our work. The differences lie in three aspects of partition task, optimization of goals and what is the bad result. The main difference is that we cluster the endpoints into groups (point distance based similarity) to identify frequent segments rather than clustering the trajectory segments (line direction and distance based similarity) directly as in [8].

## 2.2. Location mining and recommendation

During the past years, a bunch of research has been performed based on individual location history represented by GPS trajectories, these works include detecting individual locations [9,10], recognizing userspeci<sup>fi</sup>c activities at each location [11] to analyze location correlations [12] and predicting traveler's movement among these locations [9]. All these works aim for a better recommendation.

Typically, people need two types of recommendations during a journey: generic and personalized recommendations [13]. An ef<sup>fi</sup>cient way for the generic recommendation is using multiple users' real-world location histories to <sup>fi</sup>nd areas of common interest. Some recommender systems, such as Geowhiz [14] and CityVoyager [15], etc., have been designed to recommend geographic locations like shops or restaurants to users. Using the GPS trajectories generated by multiple users, Zheng et. al [1] mined interesting locations and classical travel sequences within a given geo-spatial region. Also in their later work [16], they proposed

![](/api/attachments/7263QTUB/fulltext/images/16446843f1b57844432d058fe224f50e0a8f9dd113446d2c2d9d5cc4f118c789.jpg)  
Fig. 1. Using partitioned stationary sub-trajectory instead of a trajectory.

Please cite this article as: H. Yuan, et al., Human mobility discovering and movement intention detection with GPS trajectories, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.010

a smart recommendation for highly ef<sup>fi</sup>cient and balanced itineraries with the multiple user-generated GPS trajectories.

There are two methods for the personalized recommendations. One method is based on the traveler's individual trajectories [17,18] and the other is on user-location similarity [19]. In [20], the authors proposed a novel User Oriented Trajectory Search for trip recommendation by taking both the spatial similarity and user-preference into consideration. Also, Ye et al. [17] proposed the novel notion of individual life pattern, which could be used to capture an individual's general life style and regularity ef<sup>fi</sup>ciently. Note that, the combination of Location Based Service (LBS) with real-time personalized recommendation is also of great concern in recent years. In [21], a POI category-based itinerary recommendation framework combining physical trajectories with LBSN was proposed. Speci<sup>fi</sup>cally, a personalized friend and location recommender for the geographical information systems (GIS) on the Web has been reported in [13], in which the authors incorporated a content-based method into a user-based collaborative <sup>fi</sup>ltering algorithm to conduct both the generic and personalized travel recommendations based on multiple users' GPS traces. Mobile tourist guide systems [2,22] typically recommend locations and sometimes provide navigation information based on a user's real-time location.

## 2.3. Inference method for location prediction

Bayesian inference was found initially in applications of location recommendation [23–25] because Bayesian updating is important in the dynamic analysis of a sequence of data. Very recently, four main methods i.e., decision tree, HITS Ranking, collaborative <sup>fi</sup>ltering and the Markov model are commonly introduced in location recommendation for reasoning and prediction.

Decision tree was introduced in [6] as a visual and analytical decision support tool in location prediction for its close relation with the in<sup>fl</sup>uence diagram. HITS was <sup>fi</sup>rst used to expand the list of relevant pages returned by a search engine and then produced two rankings for the expanded set of pages. Similarly, Zheng et al. [1,13] presented a HITSbased inference model to infer the interest level of a location and a user's travel experience. It is known that the motivation for collaborative <sup>fi</sup>ltering comes from the idea that people often get the best recommendation from someone with similar interests. Thus, some important works have put forward a new problem for collaborative location and activity recommendations based on the GPS history data, so that people can provide more speci<sup>fi</sup>c recommendations with location or activity constraints [12,26,27,13]. In addition, the Markov model has been applied successfully on position prediction problems [28–30].

## 2.4. Summary

All these works have achieved main contributions on discovering knowledge about mobility, such as position, destination, way of moving etc. Instead, our work aims at mining an individual's moving regularity for better movement intention detection without any a priori geographic knowledge, such as a city map and geographic points with semantic meaning, whereas the similar work of [1,17] would depend more or less on their help.

## 3. Methodology

In this section, we <sup>fi</sup>rst clarify some terms used in this paper. Then, the architecture of our system is brie<sup>fl</sup>y introduced.

## 3.1. Notations

In this work, the topics of geography, graph and data mining are related. For better illustration, Table 2 lists all the mathematical notations used in this paper.

Table 2  
Mathematical notations and descriptions.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $TR_i$ </td><td>the  $i$ -th trajectory,  $i = 1, ..., N$ </td></tr><tr><td> $g_i$ </td><td>the  $i$ -th GPS point (latitude, longitude and altitude),  $i = 1, ..., n$ </td></tr><tr><td> $STR_i$ </td><td>the  $i$ -th sub-trajectory of a trajectory,  $i = 1, ..., m$ </td></tr><tr><td rowspan="2"> $\mathcal{P}(S, D)$  $\overrightarrow{g_i g_{i+1}}$ </td><td>the passage from area  $S$  to  $D$ </td></tr><tr><td>the move action from  $g_i$  to  $g_{i+1}$ </td></tr><tr><td> $\theta_{g_i}$ </td><td>the direction bias between  $g_i$  and the first move action</td></tr><tr><td> $d_{g_i}$ </td><td>the position bias between  $g_i$  and the first move action</td></tr><tr><td> $SST(g_s g_t)$ </td><td>a stationary sub-trajectory from  $g_s$  to  $g_t$ </td></tr><tr><td> $CP_i$ </td><td>the characteristic points set of  $TR_i$ </td></tr><tr><td> $CP$ </td><td> $\cup_{i=1}^{N} CP_i$  the characteristic points set of all the trajectories</td></tr><tr><td> $C_i$ </td><td>the  $i$ -th cluster of characteristic points,  $i=1,...,l$ </td></tr><tr><td> $c_i$ </td><td>the centroid point of the  $i$ -th cluster</td></tr><tr><td> $G(V,E)$ </td><td>the path network with vertex set  $V$  and edge set  $E$ </td></tr><tr><td> $\omega(C_i c_j)$ </td><td>the linkage weight of two clusters  $C_i$  and  $C_j$ </td></tr><tr><td> $map_V(CP_i)$ </td><td>mapping all the characteristic points of  $TR_i$  onto  $V$ </td></tr><tr><td> $d(c_i c_j)$ </td><td>the minimum hops between  $c_i$  and  $c_j$ </td></tr><tr><td> $p_{c_{t+1}}$ </td><td>the probability of an object moving from  $c_t$  to  $c_{t+1}$ </td></tr><tr><td> $FP$ </td><td>the set of frequent pattern</td></tr><tr><td> $fp$ </td><td>a frequent pattern</td></tr><tr><td> $conf(x \to y)$ </td><td>the confidence of association  $\{x \to y\}$ </td></tr></table>

## 3.2. The framework of the method

The presented methodology mainly consists of GPS data collection, human mobility discovering and movement intention detection. The framework is illustrated as a whole in $\mathrm { F i g } . 2$

The GPS data collection part is completed by an independent device, such as a GPS-terminal and GPS-enabled mobile phones. The recorded data includes longitude, latitude, height, timestamp and so forth, in which the <sup>fi</sup>rst two are critical for our trajectory study.

In the human mobility discovering part, we try to trim the trajectory into frequent path and fixed territory for a traveler (or a group of travelers). First, the “trajectory partition” module presents a new partition method to divide each original trajectory into a set of stationary sub-trajectories (SSTs), and records the start and end points of each SST into characteristic point set CP. Second, the “point clustering” module clusters the characteristic points into groups C basing on their geographical similarity. The “path mining” module mines the traveler's frequent path from CP. By representing the i-th clusters $C _ { i }$ with its centroid points $c _ { i } ,$ the “identi<sup>fi</sup>cation” module is used to discover the <sup>fi</sup>xed territories for traveler(s). Finally, the “network mapping” module constructs a weighted path network G(V,E) according to the linkage relationship and frequency of edge.

![](/api/attachments/7263QTUB/fulltext/images/7581769fe221ea1e188442e0a87b1bd4ae3aa062273ac62c9cf9e055bf45948c.jpg)  
Fig. 2. The main procedure.

At the movement intention detection part, the “detection” module can explore the traveler's movement intention with path network and conduct some personalized recommendation, e.g., information about feasible path and interested POIs.

## 4. Trajectory partitioning

In this section, we propose a trajectory partitioning algorithm to obtain a set of sub-trajectories, in which the movement directions are relative stable, and thus the move actions of an object on this sub-trajectory can be represented as a line segment [8].

## 4.1. Moving disturbance

Let $g _ { i }$ denote the i-th GPS point of a moving object, then a series of time-ordered GPS points

$$
T R = \left\{g _ {1} g _ {2} \dots g _ {i} g _ {i + 1} \dots g _ {n} \right\}\tag{1}
$$

denotes the trajectory of the object moving from $g _ { 1 }$ to $g _ { n } .$ . Given a start area S and a destination area D for a moving object such that $g _ { 1 } \in S$ and $g _ { n } \in D ,$ , the trajectories from S to D is in<sup>fi</sup>nite.

## De<sup>fi</sup>nition 1. Passage

The term of passage means a way through or along which someone or something may pass, which is used in this work to specify all the potential trajectories for an object moving from start area S to destination D.

According to the de<sup>fi</sup>nition, we can make a proposition that all of these potential trajectories from S to D are composed of a passage ${ \mathcal { P } } ( S , D )$

$$
\mathcal {P} (S, D) = \overset {\infty} {\cup} _ {j = 1} T R _ {j}\tag{2}
$$

where $T R _ { j } = \Big \{ g _ { 1 } g _ { 2 } . . . g _ { i _ { j } } . . . g _ { n _ { j } } \Big \} , g _ { 1 _ { j } } \in S \mathrm { ~ a n d ~ } g _ { n _ { j } } \in D .$

## De<sup>fi</sup>nition 2. Move action

For any sub-trajectory $S T R = \{ g _ { s } g _ { s + 1 } . . . . . . g _ { t } \} \subseteq T R \subset \mathcal { P } ( S , D ) , 1 \leq s \leq t$ $\leq n ,$ where $g _ { s }$ <sup>¼ þ Pð Þ</sup>is the start-point and g is the end-point of STR, the move action at point g is de<sup>fi</sup>ned as $g _ { i } g _ { i + 1 } , i = s , . . . , t - 1 , ( \overrightarrow { g _ { i } g _ { i + 1 } }$ denotes a vector constructed by two points g and $g _ { i + 1 } ) .$ And, $\overrightarrow { g _ { s } g _ { s + 1 } }$ <sup>þ</sup>is the first move action of STR.

## De<sup>fi</sup>nition 3. Direction disturbance

The direction bias between $\overrightarrow { g _ { s } g _ { s + 1 } }$ and $\overrightarrow { g _ { s } g _ { i } } ( i = s + 1 , . . . , t )$ is called <sup>þ ð Þ¼ þ</sup>the direction disturbance of GPS point g with respect to the <sup>fi</sup>rst move action of a STR. It can be denoted by

$$
\theta_ {g _ {i}} = \angle \left(\overrightarrow {g _ {s} g _ {s + 1}}, \overrightarrow {g _ {s} g _ {i}}\right).\tag{3}
$$

## De<sup>fi</sup>nition 4. Position disturbance

Suppose the projection point of $g _ { i } , ( i = s + 1 , . . . , t )$ onto $\overrightarrow { g _ { s } g _ { s + 1 } }$ is $g _ { i } ^ { \prime }$ $\mathrm { i } s g ^ { \prime } { } _ { 1 }$ <sup>þ</sup>, the Euclidean distance between g and g<sup>′</sup> is called position disturbance, and denoted by

$$
d _ {g _ {i}} = | g _ {i} g _ {i} ^ {\prime} |.\tag{4}
$$

For these two types of disturbance, we have the following properties:

$\mathrm { m i n } _ { g i \in S T } \mathrm { ~ } _ { R } \big \{ \theta _ { g _ { i } } \big \} = 0$ and min<sub>g ∈ ST</sub> <sub>R</sub> d<sub>g</sub><sup></sup> <sup></sup>  0; $d _ { g _ { i } } = 0 \Longleftrightarrow \theta _ { g _ { i } } = 0 .$

Fig. 3 shows a sample passage with geographical boundary of passage width $( w _ { \mathcal P } )$ and passage length $( l _ { \mathcal { P } } )$ . For the trajectory $T R =$ $\{ g _ { 1 } g _ { 2 } g _ { 3 } g _ { 4 } \ldots g _ { n } \} ,$ , since the first move action is $\overrightarrow { g _ { 1 } g _ { 2 } }$ , then $\theta _ { \mathbf { g } _ { 3 } }$ is the direction disturbance of point $g _ { 3 }$ and $d _ { g _ { 3 } }$ is the position disturbance.

In a city, it is rational to assume that the maximum position disturbances are equal to the street (passage) width where the moving object stands.

## 4.2. Stationary sub-trajectory

## De<sup>fi</sup>nition 5. Stationary sub-trajectory

A sub-trajectory $S T R = \{ g _ { s } g _ { s }  + 1 \ldots g _ { t } \}$ is a stationary sub-trajectory (SST) if the position disturbance of each GPS point $g _ { i } , s + 1 < i \leq t$ changes not rapidly with respect to the first move action $\overline { { g _ { s } g _ { s + 1 } } }$ while the moving behavior o $\dot { \boldsymbol { g } } _ { t + 1 }$ changes rapidly.

Now, the problem is how to calculate the “not rapidly” changes of a sub-trajectory. In [8], the authors presented a complex trajectory partition method to achieve this goal. In fact, studying the <sup>fl</sup>uctuation of ${ d _ { \mathrm { g } _ { i } } ( i = s + 1 , . . . , t ) }$ around $\overrightarrow { g _ { s } g _ { s + 1 } }$ (the <sup>fi</sup>rst move action) in $S T R =$ $\{ g _ { s } g _ { s } \scriptsize _ { + 1 } \ldots g _ { t } \}$ <sup>þ</sup>would help people to detect whether a STR is also a SST.

Proposition 1. Given a sub-trajectory $S T R \subseteq T R$ and a prede<sup>fi</sup>ned small disturbance threshold $d _ { 0 } \geq 0 ,$ , if

$$
\max _ {g _ {i} \in S T R} \left\{d _ {g _ {i}} \right\} \leq d _ {0}, \text { and } d _ {g _ {t + 1}} > d _ {0},\tag{5}
$$

then we can say that the position disturbance of all the points in STR changes “not rapidly” and STR is a stationary sub-trajectory (represented by $S S T ( g _ { s } , g _ { t } ) ,$ ).

Obviously, relation (5) indicates that $g _ { t }$ is the turning point between two SSTs, which is called characteristic points in [8].

In Fig. $4 ( \mathsf { a } ) , \overrightarrow { g _ { 1 } g _ { 2 } }$ is the first move action of $S T R = \{ g _ { 1 } g _ { 2 } g _ { 3 } g _ { 4 } g _ { 5 } g _ { 6 } g _ { 7 } \}$ the next moves are $\overrightarrow { g _ { 2 } g _ { 3 } }$ and then $\overrightarrow { g _ { 3 } g _ { 4 } } , . . . , \overrightarrow { g _ { 6 } g _ { 7 } }$ . We can say that $\{ g _ { 1 } g _ { 2 } g _ { 3 } \}$ is a SST while $d _ { g 3 }$ is relative small and {g<sub>1</sub>g<sub>2</sub>g<sub>3</sub>g<sub>4</sub>g<sub>5</sub>} is not while $d _ { \mathrm { g _ { 4 } } }$ and $d _ { g _ { 5 } }$ are big. Moreover, $g _ { 3 }$ and $g _ { 5 }$ are characteristic points of TR in Fig. 4.

Lemma 1. STR = {g g } is a SST where $i = 1 , . . . , n - 1$

Proof. According to the de<sup>fi</sup>nition of position disturbance, $d _ { g _ { i + 1 } } = 0$ with respect to $\overrightarrow { g _ { i } g _ { i + 1 } }$ □

Since the only criterion for any $S T R \subseteq T R$ being a SST is the moving behavior of each GPS point in it that changes not so rapidly, we can

![](/api/attachments/7263QTUB/fulltext/images/1dd9ce9ef473c76b991dadbcd06ee8d5cc0b1d559992d3a29a30229cda97a51b.jpg)  
Fig. 3. An example of direction and position disturbance of a GPS point in a passage.

Please cite this article as: H. Yuan, et al., Human mobility discovering and movement intention detection with GPS trajectories, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.010

partition a trajectory into a set of linked SSTs with some kinds of behavioral thresholds according to the differential theory in mathematics.

Lemma 2. Any trajectory $T R = \{ g _ { 1 } g _ { 2 } g _ { 3 } . . . . . . g _ { n } \} \subset \mathcal { P } ( S , D )$ can be par-<sup>¼ f</sup>titioned completely into a set of SSTs.

Proof. Assume $T R = \{ g _ { 1 } g _ { 2 } \ldots g _ { i } g _ { i } + 1 \ldots g _ { n } \}$ is not a SST. Without losing generality, we can further assume that $\textstyle \operatorname* { m a x } _ { i \in s _ { j } , \ldots , s _ { j } + h - 1 } \left\{ d _ { g _ { i } } \right\} \leq d _ { 0 }$ while $d _ { g _ { s _ { i } + h } } > d _ { 0 }$ ; hN1 w.r.t $\overrightarrow { g _ { s _ { j } } g _ { s _ { j } + 1 } }$ , then we can partition STR into $S T R _ { j ( 1 ) } =$ $\left\{ g _ { s _ { j } } g _ { s _ { j } + 1 } . . . g _ { s _ { j } + h - 1 } \right\}$ and $S T R _ { j ( 2 ) } = \left\{ g _ { s _ { j } + h - 1 \ldots } g _ { t _ { j } } \right\}$ and $S T R _ { j ( 1 ) }$ is a SST. Repeating the process and Lemma 1 guarantees us to partition $S T R _ { j ( 2 ) }$ (and its sub-trajectories if necessary) into a set of SST. □

Note that, the partitioned $S T R _ { j } , j = 1 , . . . , m$ , is also time-ordered and the following relation is satis<sup>fi</sup>ed:

$$
\mathrm{STR} _ {j} \cap \mathrm{STR} _ {j + 1} = g _ {t _ {j}} = g _ {s _ {(j + 1)}}, j = 1, \dots , m - 1,\tag{6}
$$

where $g _ { t _ { i } + 1 }$ is the point where the behavior of a trajectory changes rapidly, thus $g _ { t _ { i } }$ is a characteristic point of TR.

In real applications, if an object moves on a ${ \cal T } R { \subset } { \mathcal { P } } ( S , D )$ we can set the maximum position disturbance $d _ { 0 }$ of $S T R \subset T R$ <sup>Pð Þ</sup>which is the width of passage, e.g., w , where the object present stands.

## 4.3. Trajectory partitioning method

According to Proposition 1, the key issue for partitioning a TR into SSTs is to <sup>fi</sup>nd out all the characteristic points. In this section, we propose a new trajectory partitioning algorithm which aims at <sup>fi</sup>nding the points where the behavior of a trajectory changes rapidly. The main idea is to check the value of $d _ { g _ { i } } , \ i = 2 , . . . , n$ with respect to the present first move action:

• Let the <sup>fi</sup>rst SST begin with move action ${ \overrightarrow { g _ { 1 } g _ { 2 } } } , { \mathrm { i f ~ } } d _ { g _ { i } } \leq d _ { 0 } , \ i = 2 , . . . , n ,$ then $g _ { i }$ belongs to the present SST.

• Else if $\cdot { d _ { g _ { i } } }$ exceeds the threshold $d _ { 0 } ,$ then $S T R = \left\{ g _ { 1 } \ldots g _ { i - 1 } \right\}$ is a SST and $\overrightarrow { g _ { i - 1 } g _ { i } }$ is the first move action of a new SST.

• The next step is checking $d _ { g _ { k } } , k = i + 1 , . . . . , n$ with respect to $\overrightarrow { g _ { i - 1 } g _ { i } } .$

<sup>¼ þ</sup>• The process will be ended while TR is partitioned completely into SSTs.

Algorithm 1 shows the whole process of the trajectory partitioning method, and Lemma 3 presents the time complexity of the algorithm.

## Algorithm 1. Trajectory partitioning algorithm

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Input: Trajectory  $TR = \{g_{1}g_{2}g_{3}\ldots\ldots g_{n}\}$ , threshold  $d_{0}$ ;
2: Output: A set of characteristic points CP;
3:  $g_{1} \rightarrow CP$ ;
4: i = 1;
5: repeat
6: first move action= $\overrightarrow{g_{i}g_{i+1}}$ ;
7: for j = i + 2 to n do
8: if  $d_{g_{j}} \geq d_{0}$  then
9:  $g_{j-1} \rightarrow CP$ ;
10: i = j - 1;
11: Break;
12: else
13: if j = n then
14:  $g_{j} \rightarrow CP$ ;
15: end if
16: end if
17: end for
18: until  $g_{n} \rightarrow CP$ ;
19: return CP.
</div>

Lemma 3. The time complexity of the trajectory partition algorithm 1 is $O ( n )$ , where n is the length (i.e., the number of points) of a trajectory TR.

Proof. In each SST, the main computation in Algorithm 1 is to calculate $d _ { g _ { i } } , \ j = 3 , . . . , n$ with respect to the first move action and the maximum number of computations required is equal to $n - 2$ times. □

Now, the problem is how to identify SSTs from the generated $C P$ in Algorithm 1. Fortunately, if g and $g _ { t } \ ( s < { \mathfrak { t } } )$ are two adjacent points in $C P$ then $\mathsf { S T R } = \{ g _ { s } . . . g _ { t } \}$ is a SST. For example, we can obtain ${ \boldsymbol { C } } { \boldsymbol { P } } =$ {g<sub>1</sub>g<sub>3</sub>g<sub>5</sub>g<sub>7</sub>} from $S T R = \{ g _ { 1 } . . . g _ { 7 } \}$ in Fig. 4(a), which means, STR can be represented by three SSTs as $S S T ( g _ { 1 } , g _ { 3 } ) , S S T ( g _ { 3 } , g _ { 5 } )$ and $S S T ( g _ { 5 } , g _ { 7 } )$ (See Fig. 4(b)). Note that the partition results are only trajectory related, different trajectories may result in different partitions even they are from a same city street. Another important problem is the effect of the first moving direction. In the extreme case that the first moving direction is inconsistent with the path, the above method would result in a fragmentary partition of a line segment, which would then cause to great dif<sup>fi</sup>culties in distinguishing characteristic points. To avoid this problem, we call the characteristic points generated by the original GPS data as the <sup>fi</sup>rst class-CP, denoted by $C P ^ { ( \bar { 1 } ) }$ , and repeat the same partition process with $C P ^ { ( 1 ) }$ to obtain $C P ^ { ( \bar { 2 } ) }$ until

$$
C P ^ {(n)} = C P ^ {(n - 1)}.\tag{7}
$$

## 5. Fixed territory identi<sup>fi</sup>cation and path network

To identify the movement intention of a traveling object in business applications, we have to discover the frequent path and fixed territories of an object in a city. In this section, we present a new method to identify the <sup>fi</sup>xed territories and discover the frequent paths.

## 5.1. Characteristic points clustering

In real application, it is reasonable to assume that all the recorded GPS points from different trajectories for the same position would be close to each other. This idea is useful for detecting whether a place is frequently visited by a person.

Assume that there are N historic trajectories of an observed moving object. Firstly, we partition each $T R _ { i } = \left\{ g _ { 1 _ { i } } , . . . , g _ { n _ { i } } \right\} , i = 1 , . . . ,$ ; into m <sup>¼</sup>SSTs and obtain a characteristic points set $C P _ { i } = \left\{ g _ { 1 _ { i } } , . . . , g _ { c _ { i } } . . . , g _ { n _ { i } } \right\}$ where $| C P _ { i } | = m _ { i } + 1$ and ${ g _ { c _ { i } } \in T R _ { i } }$ <sup>¼</sup>is a characteristic point $( \mathrm { T a b l e } 3 ) .$

We then introduce the general clustering method to cluster all the points in $C P = \cup \mathbf { \Phi } _ { i } ^ { N } = { } _ { 1 } C P _ { i }$ into l clusters: $C _ { 1 } , . . . , C _ { l }$ basing on the Euclidean distance of paired points. The element number of each cluster is |C |, $i = 1 , . . . , l .$

A signi<sup>fi</sup>cant advantage of our method is the direct use of the characteristic points into clustering without any further data conversion or selection, for example, map-matching [31]. Moreover, since the clustering process is not our utmost concern, the measurements for the clustering results are relative loose:

• Completeness: for all the points $g \in C P ,$ , there exists at least one $C _ { i } ,$ $( i = 1 , . . . , l )$ such that $g \in C _ { i }$ (overlap clustering is allowed);

• Geographical-scale-related: different geographical scales would result in different clustering results.

Fig. 5 shows the characteristic points of six trajectories $( T R _ { 1 } , . . . , T R _ { 6 } )$ that are clustered into <sup>fi</sup>ve clusters as $C _ { 1 } , C _ { 2 } , C _ { 3 } , C _ { 4 }$ and $C _ { 5 } .$

## 5.2. Path network

Since all the characteristic points are either start or end points of a SST, according to the clustering mechanism, any line segment between two clusters is a SST. All the SSTs then link the clusters into a SST network (see Fig. 6(a)).

```txt
Please cite this article as: H. Yuan, et al., Human mobility discovering and movement intention detection with GPS trajectories, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.010
```

H. Yuan et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/7263QTUB/fulltext/images/075e9497eaa557131c5536f8c2c9dca95ffa499e10801627da172add129d8610.jpg)  
Fig. 4. An example of stationary sub-trajectories partition.

Moreover, all these found clusters of characteristic points can be deemed as the fixed territories for the moving object. These <sup>fi</sup>xed territories could be:

• A street corner (where the object always changes moving direction);

• Point of interest (POI, a POI is associated with a coordinate and a category like restaurants, shopping malls [32], pubs, theaters, parks etc.);

• Home or of<sup>fi</sup>ce (stay for a relative long time, or common start/end points of trajectories) for the studying object; or

• Other interesting territories.

Since each SST is also the relation linkage between two <sup>fi</sup>xed territories, then we can construct an undirected path network G(V,E) (V is the vertex set and E is the weighted edge set) as follows: First, calculate the centroid point $c _ { i }$ of cluster $C _ { i } , ( i = 1 , . . . , l )$

$$
c _ {i} = \frac {1}{| C _ {i} |} \Sigma_ {g _ {j} \in} c _ {i} g _ {j}.\tag{8}
$$

Table 3  
Trajectories and their characteristic points.

<table><tr><td> $TR_{i}$ </td><td>Partition of  $TR_{i}$ (each pair of endpoints form a SST)</td><td> $CP_{i}$ </td></tr><tr><td>1</td><td> $g_{1_1}-g_{c_{11}}-g_{c_{12}}...g_{c_{1(m_1-1)}}-g_{n_1}$ </td><td> $\left\{g_{1_1},g_{c_{11}}...g_{c_{1(m_1-1)}},g_{n_1}\right\}$ </td></tr><tr><td>2</td><td> $g_{1_2}-g_{c_{21}}-g_{c_{22}}...g_{c_{2(m_2-1)}}-g_{n_2}$ </td><td> $\left\{g_{1_2},g_{c_{21}}...g_{c_{2(m_2-1)}},g_{n_2}\right\}$ </td></tr><tr><td>...</td><td>...</td><td>...</td></tr><tr><td>N</td><td> $g_{1_N}-g_{cN_1}-g_{cN_2}...g_{c_N(m_N-1)}-g_{n_N}$ </td><td> $\left\{g_{1_N},g_{cN_1}...g_{c_N(m_N-1)},g_{n_N}\right\}$ </td></tr></table>

![](/api/attachments/7263QTUB/fulltext/images/c02d23f440ae00629c1dc5f9a21d89464c7b415f71298cb454fb6d88a5e3a818.jpg)  
Fig. 5. Characteristic points clustering.

Second, each cluster is represented by its centroid point $c _ { i } , ( i = 1 , . . . , l )$ which is also a node of the path network. So, the edge between two nodes $c _ { i }$ and $c _ { j } ( i \neq j )$ can be used to represent all the possible SSTs whose start point is in C<sub>i</sub> (or $C _ { j } )$ and end point is in $C _ { j }$ (or C<sub>i</sub>). That is to say, it approximates to the passage from area c to area $c _ { j } , \mathrm { i . e . , } \mathcal { P } ( c _ { i } , c _ { j } )$ Finally, calculate the number of SSTs between any two clusters as the linkage weight of these two clusters:

$$
\omega \left(c _ {i}, c _ {j}\right) = \# \text { SST } (g _ {s}, g _ {t}) + \# \text { SST } (g _ {t}, g _ {s}), g _ {s} \in C _ {i}, g _ {t} \in C _ {j}.\tag{9}
$$

See more details about the method in Algorithm 2.

## Algorithm 2. Path network construction

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Input: All the clusters $C_i, i = 1, \ldots, l$;
2: Output: Path network $G(V, E)$;

3: for $i = 1$ to $l$ do
4:    $V \leftarrow c_i = \frac{1}{|C_i|} \Sigma_{g_j \in C_i g_j}$;
5: end for
6: for $i = 1$ to $l - 1$ do
7:    for $j = i + 1$ to $l$ do
8:    $\omega(c_i, c_j) = 0$;
9:    for $u = 1$ to $|C_i|$ do
10:    for $v = 1$ to $|C_j|$ do
11:    if $(g_u, g_v)$ is a SST $\parallel (g_v, g_u)$ is a SST then
12:    $\omega(c_i, c_j) + +$;
13:    end if
14:    end for
15:    end for
16:    end for
17:    if $\omega(c_i, c_j) &gt; 0$ then
18:    $E \leftarrow \omega(c_i, c_j)$;
19:    end if
20: end for
21: return $G(V, E)$.
</div>

Fig. 6b shows a sample path network G(V,E), $V = \{ c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } \}$ and $E = \{ ( c _ { 1 } , c _ { 2 } ) , ( c _ { 2 } , c _ { 3 } ) , ( c _ { 2 } , c _ { 4 } ) , ( c _ { 5 } , c _ { 5 } ) \}$ , derived from the SST network in Fig. 6(a).

## 5.3. Frequent path detection

According to the traditional de<sup>fi</sup>nition of frequent pattern, if edge $( c _ { i } , c _ { j } ) \in E ( i \neq j$ and $i , j = 1 , . . . , l )$ is a frequent path, we can expect that $\omega ( c _ { i } , c _ { j } )$ is relative big. We call edge $\left( c _ { i } , c _ { j } \right)$ as a frequent path while

```txt
Please cite this article as: H. Yuan, et al., Human mobility discovering and movement intention detection with GPS trajectories, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.010
```

H. Yuan et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/7263QTUB/fulltext/images/844f0527390c2e73fcae6310963bfaa8bb4fcbcd952b2cb13f872c20a1d14e0f.jpg)

![](/api/attachments/7263QTUB/fulltext/images/ddd581338e9a5d09b2a150b766214b4134a4b99382f620a65bbb25ea1d5971cb.jpg)  
b) Weighted path network $G ( V , E )$  
Fig. 6. Characteristic points formed a path network.

$\omega ( c _ { i } , c _ { j } ) \ge \omega _ { 0 }$ , where $\omega _ { 0 }$ is the minimum support threshold. It is easy to obtain all the frequent paths (FP) in a weighted path network G:

$$
F P _ {G} = \left\{\left(c _ {i}, c _ {j}\right) \mid \left(c _ {i}, c _ {j}\right) \in E \text { and } \omega \left(c _ {i}, c _ {j}\right) \geq \omega_ {0} \right\}.\tag{10}
$$

## 6. Movement intention detection

In this section, we <sup>fi</sup>rst propose an association rule based method to detect the movement intention, and then present two methods for business applications of path recommendation and POI recommendation for a moving object.

## 6.1. Mapping new trajectory onto a path network

Assume the test trajectory of an object is $\mathrm { { \cal R } } _ { n e w } = \bigl \{ g _ { 1 _ { n e w } } g _ { 2 _ { n e w } } . . . g _ { n _ { n e w } , . . . } \bigr \} ,$ in which $g _ { n e w }$ <sup>¼</sup>is the point where the moving object presently stands. The following steps will map the <sup>fi</sup>nished trajectory onto a path network $G ( V , E )$

• First, we partition $T R _ { n e w }$ into m SSTs and obtain a characteristic point set $C P _ { n e w } = \left\{ g _ { 1 _ { n e w } } , . . . , g _ { c _ { i } } , . . . , g _ { n _ { n e w } } \right\}$ with m + 1 elements.

<sup>¼</sup> • Then, each characteristic point $g _ { c _ { i } } { \in } C P _ { n e w } ( i = 1 , . . . , m + 1 )$ will be assigned to the closest cluster $C _ { j _ { i } ^ { * } }$ <sup>ð Þ¼ þ</sup>according to the distance between $g _ { c _ { i } }$ and each centroid $c _ { i } \in V \colon$

$$
j _ {i} ^ {*} = \arg \min _ {j = \{1, \dots , l \}} \left| g _ {c _ {i}} c _ {j} \right|.\tag{11}
$$

• Finally, we map all the characteristic points of $T R _ { n e w }$ onto the vertices of path network and obtain a vertex set of

$$
\operatorname{map} _ {V} \left(C P _ {\text { new }}\right) = \left\{c _ {j 1 ^ {*}}, \dots , c _ {j _ {m + 1} ^ {*}} \right\}, \quad c _ {j _ {i} ^ {*}} \in V (i = 1, \dots , m + 1).\tag{12}
$$

Note that the elements in $m a p _ { V } ( C P _ { n e w } )$ are also ordered according to the sequence ${ \sf o f } g _ { c _ { i } }$ in $T R _ { n e w } .$ That is to say, Eq. (12) means that the moving sequence is $: c _ { j 1 ^ { * } } { \longrightarrow } c _ { j 2 ^ { * } \ldots } { \longrightarrow } c _ { j i ^ { * } \ldots } { \longrightarrow } c _ { { j _ { m + 1 } } ^ { * } } .$

<sup>þ</sup>There may be two different cases for the new trajectory mapping: First, see the example un<sup>fi</sup>nished trajectory $T R _ { n e w }$ in Fig. $^ { 7 ( \mathsf { a } ) }$ , using Eq. (11), the two characteristic points of $g _ { c _ { 1 } }$ and $g _ { c _ { 2 } }$ are mapped onto $c _ { 1 }$ and $c _ { 2 }$ respectively. We obtain the present moving sequence as $c _ { 1 }  c _ { 2 }$ on path network G. Second, in Fig. 7(b), the three characteristic points of ${ \dot { g } } _ { c _ { 1 } } , g _ { c _ { 2 } }$ and $g _ { c _ { 3 } }$ are mapped onto $c _ { 1 } , c _ { 5 }$ and $c _ { 2 } ,$ and the moving sequence is $c _ { 1 }  c _ { 5 }  c _ { 2 } ,$ in which, the edge $( c _ { 1 } , c _ { 5 } ) \notin$ E is the mapping of $\mathrm { S S T } ( g _ { c _ { 1 } } , g _ { c _ { 2 } } )$

## 6.2. Detection of user's movement intention

For better recommendation to this moving object, we need to know where is the object's travel destination $g _ { t _ { n e w } }$ and which edge (passage) $\left( c _ { i } , c _ { j } \right)$ would the object go through. As there is no information about the destination of an un<sup>fi</sup>nished trajectory $T R _ { n e w } ,$ all the nodes in $c \in V$ may be the next destination of the moving object. A feasible method is to <sup>fi</sup>nd out the movement intention from its historic frequent moving patterns. In order to simplify the calculation, we introduce here the concept of destination order of a moving object.

## De<sup>fi</sup>nition 6. n-th Order destination

Given two nodes $c _ { i } \in V$ and $c _ { j } \in V$ in path network $G ( V , E )$ , we called c the n-th order destination of $c _ { i } , \operatorname { i f } d ( c _ { i } , c _ { j } ) = n ,$ , where $d ( x , y )$ means the minimum hops between x and y.

There are two important properties for $d ( x , y )$ : <sup>fi</sup>rst, $d ( x , y ) \geq 0$ and $d ( x , y ) = 0 \Longleftrightarrow x = y ;$ second, $d ( x , y ) = d ( y , x )$

Now the movement intention detection problem is changed to give the present trajectory $T R _ { n e w } = \{ g _ { 1 _ { n e w } } g _ { 2 _ { n e w } } . . . g _ { n _ { n e w } } \}$ whose destination $g _ { t _ { n e w } }$ <sup>¼</sup>is unknown. Which <sup>fi</sup>xed territory in G is the possible destination for the present moving object? To archive this goal, we <sup>fi</sup>rst predict the next <sup>fi</sup>xed territory $c _ { i ^ { * } } \in V$ which the un<sup>fi</sup>nished $T R _ { n e w }$ would go through according to the frequent path.

Given a characteristic point set $C P _ { n e w } = \left\{ g _ { 1 } , g _ { c _ { 1 } } , . . . , g _ { n _ { n e w } } \right\}$ of $T R _ { n e w }$ $( g _ { n _ { n e w } }$ <sup>¼</sup>is the present position) and a path networ $: G ( \dot { V } , E )$ . The mapping of $C P _ { n e w }$ on G is $m a p _ { V } ( C P _ { n e w } ) = \{ c _ { 1 } \to c _ { 2 } \to \dots \to c _ { t } \}$ , we use following two principles to detect the movement intention:

## • Previous path dependent principle (PPDP)

The basic proposition for this principle is that: the next movement of $c _ { t }  c _ { t + }$ <sub>1</sub> is dependent on the previous move sequence m ${ \boldsymbol { \imath } } p _ { V } ( { \boldsymbol { C } } P _ { n e w } )$ The possibility of next movement to <sup>fi</sup>xed territory $C _ { t + 1 }$ is:

$$
p _ {c _ {t + 1}} = P ((c _ {t}, c _ {t + 1}) | \mathsf {m a p} _ {V} (C P _ {\text { new }})) _ {\left\{c _ {t + 1} \in V \backslash \mathsf {m a p} V (C P _ {\text { new }}), d (c _ {t}, c _ {t + 1}) = 1 \right\}}.\tag{13}
$$

If the object moves next to $c _ { t + 1 }$ , then the moving sequence is $m a p V ( C P _ { n e w } ) \cup \{ c _ { t } \to c _ { t + 1 } \}$ , and Eq. (13) indicates what is the probability of the next destination being $c _ { t + 1 }$ given the present move sequence of $m a p V ( C P _ { n e w } )$ . According to the traditional association rule mining method, measurement confidence conf $\begin{array} { r } { \dot { ( X \mathrm { - } Y ) } = \frac { s u p p o r t ( X \cup Y ) } { s u p p o r t ( X ) } } \end{array}$ de-<sup>ð Þ ¼ ð</sup> <sup>Þ</sup>termines how frequently items in Y appear in transactions that contain X, the value o $\dot { p } _ { c _ { t + } }$ can be estimated by the history data with association analysis.

Please cite this article as: H. Yuan, et al., Human mobility discovering and movement intention detection with GPS trajectories, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.010

H. Yuan et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/7263QTUB/fulltext/images/36b72ab3e62ae6cb694eeb5048892a284228a8c6072de2912590ee3d8c345351.jpg)  
a) All the SSTs in \$TR\_{new}\$ are mapped.

![](/api/attachments/7263QTUB/fulltext/images/069c89dc98ff06edf1a749ebd840f620c5bdfa658d863216d9c9756d011c7f65.jpg)  
b) Part of the SSTs in \$TR\_{new}\$ can be mapped.  
Fig. 7. Mapping a new trajectory onto path network.

Algorithm 3 shows the calculating process. First, in Algorithm 3, all the trajectories TR are mapped on G to obtain a set of moving sequence $m a p V ( C P _ { i } ) , i = 1 , . . . , N ;$ Second, the un<sup>fi</sup>nished new trajectory $T R _ { n e w } ,$ where the moving object present is moving on, is mapped on $G ( V , E )$ and obtain map $/ ( C P _ { n e w } )$ . Third, all the moving sequences that contain map $V ( C P _ { n e w } )$ are <sup>fi</sup>ltered from $m a p V ( C P _ { i } )$ and the data set $T = \cup \mathsf { \Pi } _ { i = 1 } ^ { N } \bar { \{ { m a p V ( C P _ { i } ) \} } }$ is generated, where mapV(CP ) satis<sup>fi</sup>es that map (CP ) ∩ map $( C P _ { n e w } ) = m a p _ { V } ( C P _ { n e w } ) .$ . Then, frequent patterns mining method is conducted to obtain FP from $T | m a p _ { V } ( C P _ { n e w } )$ . In fact, the mined $f p \in F P$ is the potential path with high probability (con<sup>fi</sup>- dence value). Finally, we can calculate the con<sup>fi</sup>dence of association rule map $\prime ( C P _ { n e w } ) \to \{ f p \}$

Given the sample path network G in Fig. 6(b), if we map $T R _ { 1 } , . . . , T R _ { 6 }$ (Fig. 6(a)) onto G as the results in Table 4 and map $T R _ { n e w }$ onto G as 1 $n a p _ { V } ( C P _ { n e w } ) = \{ c _ { 1 } , c _ { 2 } \}$ , then we can calculate T and $T | m a p _ { V } ( C P _ { n e w } )$ as follows:

## Algorithm 3. Calculating con<sup>fi</sup>dence

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Input: Path network G(V, E) and  $TR_{new}$ ;
2: Output: Confidence result set CONF;
3:  $CONF = \phi$ ;
4: Map  $TR_{new}$  on G to obtain  $map_{V}(CP_{new})$ ;
5:  $T = \phi$ ;
6: for i = 1 to N do
7: map  $TR_{i}$  on G to obtain  $map_{V}(CP_{i})$ ;
8: if  $map_{V}(CP_{new}) \cap map_{V}(CP_{i}) = map_{V}(CP_{new})$  then
9:  $T \leftarrow map_{V}(CP_{i}) \setminus map_{V}(CP_{new})$ ;
10: end if
11: end for
12: Mining frequent itemsets FP from T;
13: for each  $fp \in FP$  do
14:  $CONF \leftarrow conf(map_{V}(CP_{new}) \rightarrow fp)$ ;
15: end for
16: return CONF.
Table 4
Mapping sample trajectories in Fig. 6b onto path network.
Trajectory map $_{V}(CP_{i})$ $TR_{1}$ $\{c_{1}, c_{2}, c_{4}\}$ $TR_{2}$ $\{c_{1}, c_{3}\}$ $TR_{3}$ $\{c_{1}, c_{2}, c_{3}\}$ $TR_{4}$ $\{c_{1}, c_{2}, c_{5}\}$ $TR_{5}$ $\{c_{1}, c_{2}, c_{4}\}$ $TR_{6}$ $\{c_{2}, c_{3}\}$
</div>

$$
T = \left| \begin{array}{c} \overline {{\left\{c _ {1} , c _ {2} , c _ {4} \right\}}} \\ \hline \overline {{\left\{c _ {1} , c _ {2} , c _ {3} \right\}}} \\ \hline \overline {{\left\{c _ {1} , c _ {2} , c _ {5} \right\}}} \\ \hline \overline {{\left\{c _ {1} , c _ {2} , c _ {4} \right\}}} \end{array} \right|, \quad \text {and} \quad T \setminus m a p _ {V} (C P _ {n e w}) = \left| \begin{array}{c} \overline {{\left\{c _ {4} \right\}}} \\ \hline \overline {{\left\{c _ {3} \right\}}} \\ \hline \overline {{\left\{c _ {5} \right\}}} \\ \hline \overline {{\left\{c _ {4} \right\}}} \end{array} \right|.
$$

Finally, we obtain con $f ( m a p _ { V } ( C P _ { n e w } )  \{ c _ { 4 } \} ) = c o n ~ f ( \{ c _ { 1 } , c _ { 2 } \} $ $\{ c _ { 4 } \} ) = 2 / 4 ,$ , con $f ( m a p _ { V } ( C P _ { n e w } )  \{ c _ { 3 } \} ) = 1 / 4$ and con f(map $( C P _ { n e w } )  \{ c _ { 5 } \} ) = 1 / 4$ which means the possibility of next movement is: 50% to $c _ { 4 } , 2 5 \% \ t o \ c _ { 3 }$ and $c _ { 5 }$ basing on the present $T R _ { n e w }$ and historic moving patterns.

• Previous path independent principle (PPIP)

The basic proposition for this principle is that: the next movement of $c _ { t }  c _ { t + 1 }$ is independent on the previous move sequence map $v ( C P _ { n e w } )$ So the next destination is only related with the present path $\left( { { c } _ { t } } _ { - 1 } { { c } _ { t } } \right)$ and de<sup>fi</sup>ned as:

$$
p _ {c _ {t + 1}} = \frac {\omega (c _ {t + 1} , c _ {t})}{\sum_ {c _ {x} \in \{c | d (c _ {t} , c) = 1 \} \setminus \{c _ {t - 1} \}} \omega (c _ {t} , c _ {x}) .}\tag{14}
$$

Eq. (14) indicates that the next moving direction is in relation with the weight of linkage between $c _ { t }$ and its 1st-order destinations $( c _ { t - 1 }$ is excluded).

## 7. Evaluation

In this section, we present a detailed study of the proposed method with some real data of GPS trajectories.

## 7.1. Experiment setup

We test our method with two real GPS trajectory datasets, namely CD and BJ datasets. In these datasets, a trajectory is represented by a sequence of time-stamped points, each of which contains the information of latitude, longitude and altitude; and a broad range of the users' outdoor movements, including not only life routines like go home and go to work but also some entertainment and sports activities, such as shopping, sightseeing, dining and hiking had been recorded. Noting that, the original GPS data adopts the WGS-84 coordinate, all the GPS points' values had been translated into Beijing-54 coordinate in this study in order to facilitate the computation of Euclidean distance.

The CD dataset consists of a series of regular car routes generated from July to September 2012 in Chengdu city of China. In which, all the trajectories are logged in a dense representation, $\mathrm { e . g . }$ , every 5 s or every 20 m per point. Finally, 37 longer routes are selected to conduct

Please cite this article as: H. Yuan, et al., Human mobility discovering and movement intention detection with GPS trajectories, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.010

H. Yuan et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/7263QTUB/fulltext/images/102da4a5b9538507504fdc020f9ba407c88b468f1eb9d09b7669de63be2de9ae.jpg)  
a) Car routes trajectories in CD dataset.

![](/api/attachments/7263QTUB/fulltext/images/529f1bfebc4d38b467daf544fc19f64a59d94cd734a3bdd878970b0ad5c1cce5.jpg)  
b) Sample trajectories in BJ dataset.  
Fig. 8. Experiment trajectories in the Google earth system. (For interpretation of the references to color in this <sup>fi</sup>gure, the reader is referred to the web version of this article.)

the mobility discovering experiment. The special feature of the CD dataset is that the volunteers recorded their routes (open the GPS recorder) randomly. The BJ dataset is collected by the Geolife project conducted by Microsoft Research Asia in Beijing city.<sup>1</sup> This dataset was generated by 182 users in a period of over three years (from April 2007 to August 2012). 21 trajectories with a total distance of about 1.2 million km and a total duration of 48,000+ hours. At last, 12 users are chosen randomly to conduct the movement intention experiments. We extracted the volunteer's regular routes from the above data set. The green lines in Fig. 8 are the sample trajectories shown in the Google earth system.

All algorithms in data preprocessing as well as frequent pattern mining were implemented in C++, and the k-means [33] algorithm used in clustering is implemented in MATLAB.

## 7.2. Mobility discovering

In this subsection, we use the CD dataset to demonstrate the proposed human mobility discovering method.

## 7.2.1. Trajectory partition

The <sup>fi</sup>rst process for the human mobility discovering method is about trajectory partition.

The proposed partition method has two properties: using only one important parameter $d _ { 0 } ,$ and insensitive to the starting point. In our method, the <sup>fi</sup>rst property means only one important parameter $d _ { 0 }$ is used to control the partition result. This is <sup>fl</sup>exible for scale geographic information based computation. For instance, it can be used to <sup>fi</sup>nd trajectory characteristic points either in a local area with smaller value of d (to keep more micro information with more characteristic points, see Fig. $9 ( \mathsf { a } ) \mathsf { - } ( \mathsf { b } ) )$ or in a city scale, even in a country scale level with a bigger d (to keep more macro information with few characteristic points, see Fig. $ { \sf 9 ( e ) - ( f ) } )$ . Moreover, for the city scale level geographic information study, the appropriate value of $d _ { 0 }$ is approximately between 100 and 1000 (Fig. 9(d)–(e)).

The second property means the presented algorithm can work well on any GPS trajectories with any start points. This is valuable since many users would use the GPS equipment in a random manner even if he/she is on the same way. In Fig. $\mathsf { \Omega } 9 ( \mathsf { a } ) \mathsf { - } ( \mathsf { f } )$ , it also indicates that the key geographic spots were found and retained regardless of the start points.

## 7.2.2. Characteristic points clustering and path network

The second process for human mobility discovering is characteristic points clustering, and the <sup>fi</sup>nal process is about visualizing the human mobility with a path network.

By setting $d _ { 0 } = 1 0 0$ in the experiment (Fig. 9(d)) to partition the trajectories into SSTs, all the characteristic points are clustered into 15 groups (Fig. 10(a)). Next, we calculate the centroid point $c _ { i }$ for cluster $C _ { i } ( i = 1 , . . . , 1 5 )$ to obtain the representative point. At last, a path network for the observed user is generated as in Fig. 10(b) by re-mapping the historic trajectories on these representative points. This network shows the frequency of each path and movement correlations between representative points which can be used to detect the user's movement intention in the future.

## 7.3. Movement intention detection

In this subsection, we use the BJ dataset to demonstrate the proposed movement intention detection method.

## 7.3.1. The data

The BJ dataset contains 17,621 trajectories with a total distance of about 1.2 million km and a total duration of 48,000+ hours. However, the number of trajectories reported by different users is not identical: the minimum number of trajectories, reported by USER049 and other 6 persons, is only 1; the maximum is 2,153 reported by USER126; and the median is 27. The distribution of the number of trajectories is shown in Table 5.

In the following, we choose randomly 12 users (3 of type I, 6 of II and 3 of III) for studying their movement intention.

## 7.3.2. Fixed territories and frequent path mining

In order to detect movement intention, we need to mine <sup>fi</sup>xed territories and frequent paths <sup>fi</sup>rst. The discovered top-5 <sup>fi</sup>xed territories and frequent paths for the observed users are all summarized in Table 6.

Here, we conduct two different mining methods. The <sup>fi</sup>rst is about <sup>fi</sup>xed territories mining. Given the characteristic point set CP of trajectories $T R _ { i } ,$ in our mining process, TR would be mapped onto the path network G(V,E) as map (CP ), and then we treat map (CP ) as a transactional record from which the frequently visited <sup>fi</sup>xed territories can be observed. The other is about frequent path mining. The common frequent item mining methods treat all the items in a transactional record equally, whereas the <sup>fi</sup>xed territories in map (CP ) are arranged in a sequential order. So the mining results would be weird and hard for understanding while conducting these frequent pattern mining methods on map (CP) directly. Therefore, if the <sup>fi</sup>xed territories in map (CP ) is “a b ${ \mathfrak { c } } " ,$ , then we transfer it into two paths as“a → b and $b  c "$ , and perform mining process on the transformed data set.

As we can see, a signi<sup>fi</sup>cant advantage of the method is that it can infer personal regularity information depending only on the historic trajectory data rather than any geographic a priori knowledge, such as a map or pre-labeled POIs.

H. Yuan et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/7263QTUB/fulltext/images/c5ab2819d41e0a0271f84f4aa9551cb0be751744ffd5a524499016af2abadabc.jpg)

b)  
![](/api/attachments/7263QTUB/fulltext/images/414acbafbd9f235fa31385e92c1753a04e236235eb4a32db1e89f92c0b5432fc.jpg)

![](/api/attachments/7263QTUB/fulltext/images/dae4c6827fc78454a3ae3e4bf26d24336a3e4f98853732bc528ebc44ee5b6a6a.jpg)  
d)  
e)

c)  
![](/api/attachments/7263QTUB/fulltext/images/84fab833ef5bec1aab4fc2f61fafc6cfbbc1a785835d3009a5f78b543e9de09b.jpg)

![](/api/attachments/7263QTUB/fulltext/images/a994e1b98e052a9fc055dbfb7c3756689ac604b970a2dbb7e2c900a57b92cdff.jpg)

f)  
![](/api/attachments/7263QTUB/fulltext/images/5d35ce1e8a8fe38880c3d6fbff30763ffae4c9a0c40c79ba01713fd75df0eace.jpg)  
Fig. 9. Partitioned SSTs with different threshold $d _ { 0 } .$

## 7.3.3. Recommendation evaluation

In an evaluation of movement intention prediction, we would select some trajectories as testing data <sup>fi</sup>rst. We then hide some characteristic points of the selected trajectories, and ask the detection system to predict a set of fixed territories that the user would like to pass by in the future. Typically, we then have four possible outcomes for the detection of the hidden fixed territories as shown in Table 7.

So, we can use here the two common terms in information retrieval of precision (Pre) and recall (Rec) to measure the detection results.

$$
P r e = \frac {\# t p}{\# t p + \# f p} \quad \text { and } \quad R e c = \frac {\# t p}{\# t p + \# f n}\tag{15}
$$

Note that, for the present movement detection task, no matter how many points the observed user is interested in, his next <sup>fi</sup>xed territory can only be one. This is the main difference between POI recommendation and traditional item based recommendation (e.g., commodity recommendation). Thus, there are some special properties by using relation (15) to do personalized geographic information recommendation for a speci<sup>fi</sup>c user whose historic trajectories were mapped onto a path network:

$\operatorname* { m a x } \{ \# \ t p \} = 1$ and min{# $t p \} = 0 ;$

$\operatorname* { m a x } \{ \# f n \} = 1$ and min{# $f n \} = 0 ;$

• # $t p + \# f n = 1 ,$ , which means, $R e c = \# t p ;$

• If we recommend Top-k territories to a user, then the maximum precision is $\begin{array} { r } { \mathfrak { m } \mathfrak { a } \mathbf { x } _ { T o p - \mathrm { k } } \{ P r e \} = \frac { 1 } { \mathrm { k } } } \end{array}$ and the minimum is 0.

In the experiment, we choose the <sup>fi</sup>rst 90% trajectories as the training data set, and the last 10% as the test data set. With the training data, the observed users' path networks are generated as in Fig. 11 (the blue lines are the mapped test trajectories) and frequent territories and paths in Table 6. In each path network, we can see clearly the user's historic moving patterns between their <sup>fi</sup>xed territories.

Then, we divide all the test trajectories roughly into two equally halves of sub-trajectories and the latter half would be hid for test reason. Further, we map the <sup>fi</sup>rst half trajectories onto the generated path network G(V,E), and ask the system to predict which fixed territory the user would like to pass by in the latter half. For instance, $T R = \{ g _ { 1 } , g _ { 2 } , g _ { 3 } , g _ { 4 } \}$ is a test trajectory. We <sup>fi</sup>rst divide it into two halves of sub-trajectories of

![](/api/attachments/7263QTUB/fulltext/images/5243aab25c5162b358359f48294b3df3623528f2c6d09ea9025602396ea9e3ed.jpg)  
a) Characteristic points clustering.

![](/api/attachments/7263QTUB/fulltext/images/58f185b1586306fb122badf8e602c562f47e622246af1560393107894d4aede9.jpg)  
b) Path network.  
Fig. 10. Characteristic points clustering and path network experiment results

Please cite this article as: H. Yuan, et al., Human mobility discovering and movement intention detection with GPS trajectories, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.010

Table 5  
The distribution of the number of trajectories in BJ dataset.

<table><tr><td>User type</td><td># of reported territories</td><td>Total number of users</td></tr><tr><td>I</td><td>1-10</td><td>55 (30.2%)</td></tr><tr><td>II</td><td>11-100</td><td>86 (47.3%)</td></tr><tr><td>III</td><td>≥101</td><td>41 (22.5%)</td></tr></table>

$S T R _ { 1 } = \{ g _ { 1 } , g _ { 2 } \}$ and $S T R _ { 2 } \{ g _ { 3 } , g _ { 4 } \}$ . Then, we map $g _ { 1 }$ and $g _ { 2 }$ onto $c _ { 1 } \in V$ and $c _ { 2 } \in V$ respectively. That is to say, $c _ { 2 }$ is the decision point.

Finally, the PPDP principle is conducted to predict where is the next territory, namely $c _ { 3 } \in V ,$ based on the present un<sup>fi</sup>nished trajectory $\{ c _ { 1 }  c _ { 2 } \}$ . And, PPIP is conducted to predict where is the next territory based on the connections with the present position $c _ { 2 }$ in G. The recommendation results for the experiment users are shown in Table 8.

Note that, the <sup>fi</sup>gures of $\# t p ,$ #fp, #fn, Pre and Rec are the averaged values of all the trajectories for the same user. Thinking both the PPDP and PPIP results as a whole, the averaged detection precision is 42.0% and recall is 68.7%. This is not an exciting result for our method. However, thinking the theoretic fact that maximum #tp is 1 for each test trajectory, it is acceptable. Further, we explore the raw data and <sup>fi</sup>nd that there were some extremely short trajectories (with respect to the value of $d _ { 0 } )$ in the test dataset, which would be mapped as a single node rather than an expected path onto the path network (See Fig. 11(a), (b), (d) and (k)). So, any recommendation for these trajectories would be failed. By the way, we can increase the averaged detection precision to 61.1% and recall to 100% by removing these noise data.

## 7.4. Management insight for personalization recommendation

The proposed methods and experiment results imply some managerial implications for geographic information based personalization recommendation.

## 7.4.1. Path and POI recommendations

With suf<sup>fi</sup>cient information of the movement intention, we can recommend the GPS user with 1) optimal paths for the subsequent traveling according to both the present traf<sup>fi</sup>c situation and the customers historic path preference; and 2) POIs or business opportunities around their <sup>fi</sup>xed territories.

Traf<sup>fi</sup>c information is the utmost concern for traveling people, particularly important for those who are in a hurry. If we know the exact destination and path to destination previously, then the forecasted traf<sup>fi</sup>c information for those speci<sup>fi</sup>c paths may help people to arrange their travel plan properly. However, predicting ef<sup>fi</sup>ciently the user's real destination is a hard work. The traditional methods would like to recommend the Top-k traf<sup>fi</sup>c information to people according to the rank of path possibility. They can work well in some cases but far from personalized.

In fact, this work presents a key method for identi<sup>fi</sup>cation of personal <sup>fi</sup>xed territories which is the main drive for personal path recommendation. Based on the historic data, there is another important way to do personalization recommendation with the proposed previous path dependent principle in this work. With which, the next path would be recommended according to the optimal con<sup>fi</sup>dence value of a “path association rule”:

Table 7  
Classi<sup>fi</sup>cation of the possible results of a detection.

<table><tr><td></td><td>Detected</td><td>Not detected</td></tr><tr><td>User passed</td><td>True-Positive (tp)</td><td>False-Negative (fn)</td></tr><tr><td>User not passed</td><td>False-Positive (fp)</td><td>True-Negative (tn)</td></tr></table>

$$
p _ {c _ {t + 1}} = \operatorname{conf} \left(\operatorname{map} _ {V} \left(C P _ {\text { new }}\right)\rightarrow c _ {t + 1}\right)\left\{c _ {t + 1} \notin \operatorname{map} _ {V} \left(C P _ {\text { new }}\right), d \left(c _ {t}, c _ {t + 1}\right) = 1 \right\}.\tag{16}
$$

In addition, the optimal recommended path will be measured by the Eq. (14) with the previous path independent principle, which is mainly affected by the path weight. For any $C P \subset G , { \mathrm { i f } } C P _ { n e w } \subset C P _ { \ l }$ , then the prediction precision is $\frac { | C P _ { n e w } | } { | C P | } .$ . This property shows us, that the more charac-<sup>j j</sup>teristic points included in the present trajectory, the better path prediction results.

Note that, recommending a city's POIs to a stranger is the famous “cold start” problem for any recommendation system. Fortunately, the interest of a location does not only depend on the number of users visiting this location but also lie in these users' travel experiences [1]. Thus, we can label almost all the POIs of a city with multiple people's trajectories under the help of data mining method [34]

## 7.4.2. Recommendation strategy

For a user with regular moving behaviors, the path network based movement detection results are rational and acceptable. If we have more trajectory data about the user, the detection system would get a thorough understanding about the mobility of the user we studied, thus more accurate and diverse predictions can be made. So, if people are driving or <sup>fi</sup>nding some <sup>fi</sup>xed territories on purpose, the PPDP principle will give them some precise and useful suggestions. Whereas, the PPIP provides more casual results. If people move slowly and wander in a city, then the PPIP will push them more information nearby the present position.

In fact, the GPS user's concern is about the recommendation rationality (more precision) whereas the geographic information provider's concern is not to lose any business opportunity (more recall). However, users often feel uncomfortable while too much less related information are pushed. In real application, the geographic information service system can use the following strategy to conduct an ef<sup>fi</sup>cient recommendation: <sup>fi</sup>rst, the recommended results are inferred by PPDP, then by PPIP, and the <sup>fi</sup>nal are results of current hot zones collaboratively <sup>fi</sup>ltered by the multi users' experiences.

## 8. Conclusion

Information about interesting locations and classical travel sequences within a given geo-spatial region can help us understand the correlation between users and locations, and enable travel recommendation as well as mobile tourist guidance.

Table 6  
Top 5 <sup>fi</sup>xed territories and frequent paths for the observed users

<table><tr><td>User</td><td>Fixed territories (%)</td><td>Frequent path (%)</td></tr><tr><td>31</td><td>4(100);9(40);2(40);6(40);10(40)</td><td>9-14-6(40);10-2-4(40)</td></tr><tr><td>21</td><td>8(50.0);10(50.0);1(33.3);2(33.3)</td><td>10-8(25)</td></tr><tr><td>105</td><td>5(62.5);6(50);2(50);7/15/3(37.5)</td><td>7-2(37.5);15-6(37.5);3-5(25);4-3(25)</td></tr><tr><td>70</td><td>14(55.6);4(33.3);8(22.2);13(22.2)</td><td>13-4(22.2)</td></tr><tr><td>6</td><td>7(96);10(28);15(16);9(16);6(12)</td><td>10-7(28);9-10(16);8-12(12);14-13(12);11-7/11-14(12)</td></tr><tr><td>46</td><td>5(80.6);8(74.2);10(67.7);12(67.7);2(54.8)</td><td>12-8(64.5);8-5(64.5);2-8(51.6);2-12(51.6);9-10(41.9)</td></tr><tr><td>155</td><td>12(65.8);15(47.4);14(39.5);4(28.9);5(28.9)</td><td>5-4(15.8);5-12(28.9);1-14(18.4);13-15(18.4);2-12(18.4)</td></tr><tr><td>174</td><td>11(11.1);12(14.3);7(33.3);14(34.9);1(74.6)</td><td>14-1(28.6);7-1(23.8);12-1(11.1);7-14(9.5);3-11(9.5)</td></tr><tr><td>5</td><td>15(87);9(68.8);14(44.2);10(33.8);13(20.8)</td><td>9-15(62.3);14-15(39);14-9(37.7);10-15(31.2);13-10(20.8)</td></tr><tr><td>24</td><td>3(83.5);9(60.4);11(31.9);6(24.2);13(17.6)</td><td>9-3(50.5);11-3(31.9);6-3(24.2);13-11(13.2);12-9(16.5)</td></tr><tr><td>13</td><td>7(77.8);11(60.4);8(42.4);12(33.3);10(33.3)</td><td>8-7(42.4);10-11(30.6);10-8(33.3);14-7(27.8);14-12(25.7)</td></tr><tr><td>0</td><td>12(89);10(86.5);6(12.9);9(6.5);7(5.8)</td><td>10-12(78.7);6-12(11.6);9-12(6.5);9-10(6.5);7-12(5.8)</td></tr></table>

Please cite this article as: H. Yuan, et al., Human mobility discovering and movement intention detection with GPS trajectories, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.010

Table 8  
![](/api/attachments/7263QTUB/fulltext/images/f1f17f04f2daa29d6b416569a89efb9d01d97c2ec51b8c9e209a4ccaa158f14d.jpg)

b)  
![](/api/attachments/7263QTUB/fulltext/images/73d9246f1ee4dd3dcef1a7886a736ee182c81c0918d5b7b8f3ffc85a00e22be3.jpg)

![](/api/attachments/7263QTUB/fulltext/images/93fb0af1ebb9f2204249d7d06b16df7ed76c0a45342352f9940da9c763bdbdd8.jpg)

![](/api/attachments/7263QTUB/fulltext/images/636daca249c549adad5664b4d3350e85a674638ed931509f19ecf2dc69779e18.jpg)

![](/api/attachments/7263QTUB/fulltext/images/56e1fcf1a6f7b82276d303c4011588cc9c25a1b6b6fba20554afe4cc22506eaa.jpg)

![](/api/attachments/7263QTUB/fulltext/images/1539a711bb967425b8792362bff1c05239eef3d091de562560d8042c76a5d0e3.jpg)

![](/api/attachments/7263QTUB/fulltext/images/ccd5c57848fe14e07dde80303cb8fca9c856d1dd119357ea3ca2033f069a28fe.jpg)

![](/api/attachments/7263QTUB/fulltext/images/4999007cdb8ea67b7087fab4ef47df9115dfedac9c6057929fd4ab8f534417c4.jpg)

![](/api/attachments/7263QTUB/fulltext/images/f5eb6f8637049ece9fd895e7e9b7a28169a6b94215ed636ee25a309704b4a5c3.jpg)

![](/api/attachments/7263QTUB/fulltext/images/3fa2adfe57c1968f361a9e5b756acaa3f436d925c816948203a33f0099ae74ae.jpg)

k)  
![](/api/attachments/7263QTUB/fulltext/images/d8ccdf67d2cfb26a57194d0539137dcc1612981825b00c649a0d2a21b3566398.jpg)

![](/api/attachments/7263QTUB/fulltext/images/93890ac0451e06deac7f4b4ab7065c6fc71e3c4bb5bdf50dc8e0e9b9bc52221a.jpg)  
Fig, 11. Path networks generated for the 12 selected users. (For interpretation of the references to color in this figure, the reader is referred to the web version of this article.

Recommendation results for test users.

<table><tr><td>User</td><td>Training TR.#</td><td>Test TR.#</td><td>#tp (Rec)</td><td>#fp</td><td>#fn</td><td>Pre</td></tr><tr><td>31</td><td>5</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>21</td><td>6</td><td>2</td><td>0.5</td><td>1.5</td><td>0.5</td><td>0.25</td></tr><tr><td>105</td><td>8</td><td>2</td><td>1</td><td>1.5</td><td>0</td><td>0.417</td></tr><tr><td>70</td><td>9</td><td>2</td><td>1</td><td>0</td><td>0</td><td>1.0</td></tr><tr><td>6</td><td>25</td><td>3</td><td>0</td><td>2</td><td>1</td><td>0</td></tr><tr><td>46</td><td>31</td><td>4</td><td>1</td><td>2.25</td><td>0</td><td>0.479</td></tr><tr><td>155</td><td>38</td><td>4</td><td>1</td><td>2.25</td><td>0</td><td>0.653</td></tr><tr><td>174</td><td>63</td><td>7</td><td>1</td><td>0.857</td><td>0</td><td>0.679</td></tr><tr><td>5</td><td>77</td><td>9</td><td>0.667</td><td>1.667</td><td>0.333</td><td>0.398</td></tr><tr><td>24</td><td>91</td><td>10</td><td>0.7</td><td>1.9</td><td>0.3</td><td>0.367</td></tr><tr><td>13</td><td>130</td><td>14</td><td>0.5</td><td>2.143</td><td>0.5</td><td>0.171</td></tr><tr><td>0</td><td>154</td><td>17</td><td>0.882</td><td>1.353</td><td>0.117</td><td>0.623</td></tr><tr><td>Avg.</td><td></td><td></td><td>0.687</td><td>-</td><td>-</td><td>0.420</td></tr></table>

In this work, we try to trim the sequence data series such as trajectory into frequent path and fixed territories. First, we present a new partition method to divide each original trajectory into a set of SSTs and record the start point and the end point of each SST into characteristic points set of CP. Second, we cluster the geographical similar points into groups C to <sup>fi</sup>nd the <sup>fi</sup>xed territories and then mine frequent path from CP. Then, we represent each cluster with its centroid point c and construct a weighted path network G according to the linkage relationship and frequency of $\left( { { C _ { i } } , { C _ { j } } } \right)$ . Finally, we can detect the person's movement intention with the generated path network.

The methods proposed in this work are ef<sup>fi</sup>cient for mining information hidden in trajectory data, especially the frequent path, <sup>fi</sup>xed territories and movement intention, which can provide tremendous business opportunities in geographic information service.

Please cite this article as: H. Yuan, et al., Human mobility discovering and movement intention detection with GPS trajectories, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.010

## Acknowledgment

The work was partly supported by the National Natural Science Foundation of China (71271044, 71102055, U1233118) and the Specialized Research Fund for the Doctoral Program of Higher Education (20100185120024).

## References

[1] Y. Zheng, L. Zhang, X. Xie, W.-Y. Ma, Mining interesting locations and travel sequences from GPS trajectories, Proceedings of the 18th International Conference on World Wide Web, WWW'09, ACM, 2009, pp. 791–800.

[2] A.K. Beeharee, A. Steed, Exploiting real world knowledge in ubiquitous applications, Personal and Ubiquitous Computing 11 (6) (2007) 429–437.

[3] In: Y. Zheng, X. Z. (Eds.), Computing with Spatial Trajectories, Springer, Berlin, 2011.

[4] X. Li, J. Han, J.-G. Lee, H. Gonzalez, Traf<sup>fi</sup>c density-based discovery of hot routes in road networks, Proceedings of the 10th International Conference on Advances in Spatial and Temporal Databases, SSTD'07, Springer-Verlag, 2007, pp. 441–459.

[5] F. Giannotti, M. Nanni, F. Pinelli, D. Pedreschi, Trajectory pattern mining, Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD'07, ACM, 2007, pp. 330–339.

[6] A. Monreale, F. Pinelli, R. Trasarti, F. Giannotti, WhereNext: a location predictor on trajectory pattern mining, Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data mining, KDD'09, ACM, 2009, pp. 637–646.

[7] H. Cao, N. Mamoulis, D.W. Cheung, Mining frequent spatio-temporal sequential patterns, Proceedings of the Fifth IEEE International Conference on Data Mining, ICDM'05, IEEE, 2005, pp. 82–89.

[8] J.-G. Lee, J. Han, K.-Y. Whang, Trajectory clustering: a partition-and-group framework, Proceedings of the 2007 ACM SIGMOD International Conference on Management of Data, ACM, 2007, pp. 593–604.

[9] D. Ashbrook, T. Starner, Using GPS to learn signi<sup>fi</sup>cant locations and predict movement across multiple users, Personal and Ubiquitous Computing 7 (5) (2003) 275–286.

[10] R. Hariharan, K. Toyama, Project Lachesis: parsing and modeling location histories, in: M.J. Egenhofer, C. Freksa, H.J. Miller (Eds.), GIScience, Lecture Notes in Computer Science, vol. 3234, Springer, 2004, pp. 106–124.

[11] D.J. Patterson, L. Liao, D. Fox, H.A. Kautz, Inferring high-level behavior from low-level sensors, in: A.K. Dey, A. Schmidt, J.F. McCarthy (Eds.), Ubicomp, Lecture Notes in Computer Science, vol. 2864, Springer, 2003, pp. 73–89.

[12] Y. Zheng, X. Xie, Learning location correlation from GPS trajectories, Proceedings of the 2010 Eleventh International Conference on Mobile Data Management, MDM'10, IEEE, 2010, pp. 27–32.

[13] Y. Zheng, X. Xie, Learning travel recommendations from user-generated GPS traces, ACM Transaction on Intelligent Systems and Technology 2 (1) (2011) 2:1–2:29.

[14] T. Horozov, N. Narasimhan, V. Vasudevan, Using location for personalized POI recommendations in mobile environments SAINT JEEE Computer Society 2006 pp. 124-129

[15] Y. Takeuchi, M. Sugimoto, CityVoyager: an outdoor recommendation system based on user location history, in: J. Ma, H. Jin, L.T. Yang, J.J.P. Tsai (Eds.), UIC, Lecture Notes in Computer Science, vol. 4159, Springer, 2006, pp. 625–636.

[16] H. Yoon, Y. Zheng, X. Xie, W. Woo, Smart itinerary recommendation based on user-generated GPS trajectories, Proceedings of the 7th International Conference on Ubiquitous Intelligence and Computing, UIC'10, Springer-Verlag, 2010, pp. 19–34.

[17] Y. Ye, Y. Zheng, Y. Chen, J. Feng, X. Xie, Mining individual life pattern based on location history, Proceedings of the 2009 Tenth International Conference on Mobile Data Man agement: Systems, Services and Middleware, MDM'09, IEEE, 2009, pp. 1–10.

[18] Y. Zheng, L. Zhang, Z. Ma, X. Xie, W.-Y. Ma, Recommending friends and locations based on individual location history, ACM Transactions on the Web 5 (1) (2011) 5:1–5:44.

[19] O. Li. Y. Zheng, X. Xie, Y. Chen, W. Liu, W.-Y, Ma, Mining user similarity based on location history, Proceedings of the 16th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, GIS'08, ACM, 2008, pp. 34:1–34:10.

[20] S. Shang, R. Ding, B. Yuan, K. Xie, K. Zheng, P. Kalnis, User oriented trajectory search for trip recommendation, Proceedings of the 15th International Conference on Extending Database Technology, EDBT'12, ACM, New York, NY, USA, 2012, pp. 156–167.

[21] X. Meng, X. Lin, X. Wang, Intention oriented itinerary recommendation by bridging physical trajectories and online social networks, Proceedings of the ACM SIGKDD International Workshop on Urban Computing, UrbComp'12, ACM, New York, NY, USA, 2012, pp. 71–78.

[22] R. Simon, P. Fröhlich, A mobile application framework for the geospatial web, in: C.L. Williamson, M.E. Zurko, P.F. Patel-Schneider, P.J. Shenoy (Eds.), WWW, ACM, 2007, pp. 381–390.

[23] M.-H. Park, J.-H. Hong, S.-B. Cho, Location-based recommendation system using Bavesian user's preference model in mobile devices Proceedings of the 4th International Conference on Ubiquitous Intelligence and Computing, UIC'07, Springer-Verlag, 2007 pp. 1130-1139

[24] Y. Huang, L. Bian, A Bayesian network and analytic hierarchy process based personalized recommendations for tourist attractions over the internet, Expert Systems with Applications 36 (1) (2009) 933–943.

[25] M. Ye, P. Yin, W.-C. Lee, D.-L. Lee, Exploiting geographical in<sup>fl</sup>uence for collaborative point-of-interest recommendation, Proceedings of the 34th International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR'11, ACM, 2011, pp. 325–334.

[26] V.W. Zheng, B. Cao, Y. Zheng, X. Xie, Q. Yang, Collaborative <sup>fi</sup>ltering meets mobile recommendation: a user-centered approach, Proceedings of the Twenty-Fourth AAAI Conference on Arti<sup>fi</sup>cial Intelligence (AAAI 2010), Atlanta, Georgia, USA, July 11–15, 2010, 2010, pp. 236–241.

[27] V.W. Zheng, Y. Zheng, X. Xie, Q. Yang, Collaborative location and activity recommendations with GPS history data, Proceedings of the 19th International Conference on World Wide Web, WWW'10, ACM, 2010, pp. 1029–1038.

[28] T. Kurashima, T. Iwata, G. Irie, K. Fujimura, Travel route recommendation using geotags in photo sharing sites, Proceedings of the 19th ACM International Conference on Information and Knowledge Management, CIKM'10, ACM, 2010, pp. 579–588.

[29] Z. Chen, H.T. Shen, X. Zhou, Discovering popular routes from trajectories, Proceedings of the 2011 IEEE 27th International Conference on Data Engineering, ICDE'11, IEEE, 2011, pp. 900–911.

[30] W. Mathew, R. Raposo, B. Martins, Predicting future locations with hidden Markov models, Proceedings of the 2012 ACM Conference on Ubiquitous Computing, UbiComp'12, ACM, 2012, pp. 911–918.

[31] Y. Lou, C. Zhang, Y. Zheng, X. Xie, W. Wang, Y. Huang, Map-matching for low-sampling-rate GPS trajectories, Proceedings of the 17th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, GIS'09, ACM, 2009, pp. 352–361.

[32] J. Yuan, Y. Zheng, X. Xie, Discovering regions of different functions in a city using human mobility and POIs, Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2012, pp. 186–194.

[33] S. Lloyd, Least squares quantization in PCM, IEEE Transactions on Information Theory 28 (2) (2006) 129–137.

[34] L.-Y. Wei, Y. Zheng, W.-C. Peng, Constructing popular routes from uncertain trajectories, Proceedings of the 18th SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2012, pp. 195–203.

![](/api/attachments/7263QTUB/fulltext/images/71f1a7bfc0ea938c190c8e20f00932ee9a3b4528faee9c93b8874c1c10c724b2.jpg)

Hua Yuan received his BS degree in MIS from Tongji University, and the PhD degree in management science and engineering from Tsinghua University, China. He is currently an Associate Professor of information systems at the University of Electronic Science and Technology of China. His research interests focus on business intelligence, information technology management, social media and networks, and information security management. His research has been published in Decision Support Systems, Information Sciences, The Computer Journal. and Applied Mathematics and Computation, and presented at a number of computer science and information system conferences.

![](/api/attachments/7263QTUB/fulltext/images/a68cf83d0feda83b78c295cc85502a14e53d7358eca6312530c03fa2a32612e0.jpg)

Yu Qian is an Associate Professor of management science at the University of Electronic Science and Technology of China (UESTC). She received her PhD degree in Management Science and Engineering from UESTC in 2008. Her general research interests include supply chain management. operation management. information economics and e-commerce, Her papers have been published and presented in journals and conferences such as the Flexible Services and Manufacturing Journal, Journal of Systems Science and Systems Engineering, and POMS annual conference.

![](/api/attachments/7263QTUB/fulltext/images/0c100a4c8a9afec6f92fe5976d2393d43b71a0a50ab4e1069cde4a49f2fa010c.jpg)

Rui Yang is an Assistant Researcher at Sichuan Science and Technology for Development Research Center. She received his Master's degree in Management from the University of Electronic Science and Technology of China in 2012. Her research interests include information management, data mining and business intelligence.

![](/api/attachments/7263QTUB/fulltext/images/97b7abdd345fcbe9b2edb562ed42fcc986713676420cbe86c864a80dad6875f7.jpg)

Ming Ren is an Associate Professor in the School of Information Resource Management at Renmin University of China. She received her PhD. in Management Science and Engineering from Tsinghua University in 2007. Her research interests include business intelligence, recommender systems and conceptual modeling. She has published papers in Information Sciences, International Journal of Intelligent Systems, and Journal of Enterprise Information Management
