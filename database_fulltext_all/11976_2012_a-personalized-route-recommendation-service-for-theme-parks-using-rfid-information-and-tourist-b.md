---
otero_id: 11976
otero_key: "YYUGRPG8"
title: "A personalized route recommendation service for theme parks using RFID information and tourist behavior"
authors: "Chieh-Yuan Tsai; Shang-Hsuan Chung"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.10.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A personalized route recommendation service for theme parks using RFID information and tourist behavior

Chieh-Yuan Tsai <sup>a,</sup>⁎, Shang-Hsuan Chung b

<sup>a</sup> Department of Industrial Engineering and Management, Yuan Ze University, Taiwan, ROC

<sup>b</sup> Department of System and Engineering Management, ChipMOS Technologies Corp., Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 16 November 2010 Received in revised form 20 September 2011 Accepted 11 October 2011 Available online 18 October 2011

Keywords: Theme parks RFID Recommendation systems Visiting sequences

## a b s t r a c t

Like any other industry, theme parks are now facing severe challenges from other entertainment competitors. To survive in a rapidly changing environment, creating high quality products/services in terms of consumer preference has become a critical issue for theme park managers. To ful<sup>fi</sup>ll these needs, this paper develops a route recommendation system that supplies theme park tourists with the facilities they should visit and in what order. In the proposed system, tourist behaviors (i.e. visiting sequences and corresponding timestamps) are persistently collected through a Radio-Frequency Identi<sup>fi</sup>cation (RFID) system and stored in a route database. The database is then segmented into sub-groups based on the similarity among tourists’ visiting sequences and time lengths. Whenever a visitor requests a route recommendation service, the system identi<sup>fi</sup>es the sub-group most similar to that visitor's personal preferences and intended visitation time. Based on the retrieved visiting behavior data and current facility queuing situation identi<sup>fi</sup>ed by the RFID system, the proposed system generates a proper route suggestion for the visitor. A simulation case is implemented to show the feasibility of the proposed system. Based on the experimental results, it is clear that the recommended route satis<sup>fi</sup>es visitor requirements using previous tourists’ favorite experiences.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

A theme park, applying themes to provide visitors with interesting experiences different from daily life, is an aggregation of attractions including architecture, landscape, rides, shows, food services, costumed personnel and retail shops [18]. Theme parks, especially regional parks, spread endemically across the US in the late 1960s and 1970s. In the 1980s and into the 1990s, most parks were developed as destination parks [4]. Well-known examples include Disney World, Disneyland, Universal Studios and Six Flags. Although the theme park industry has enjoyed steady attendance growth in the past several decades, the theme park market has entered a mature stage and is no longer experiencing high growth in terms of new development [8]. The mature theme park business became highly dependent on a higher proportion of return visitors and faced new competition from other leisure and tourism products [3].

To survive in a rapidly changing environment, theme parks need to provide high quality services in terms of consumer tastes and preferences [13]. Understanding the spatial and temporal behavior of tourists could enhance the management of attractions and contribute to extending the geographical distribution of tourists and tourist expenditures within regions [21]. Knowing which rides have been taken, which shows have been attended and which shops and squares have attracted the attention of tourists, could lead to radical improvement in satisfaction performance.

Recently, the recommender technique has been regarded as a popular technique for recommending interesting items for visitors in the tourism industry [12]. Personalized tourism services are aimed at helping the user <sup>fi</sup>nd what they are looking for by comparing the user pro<sup>fi</sup>le to some reference characteristics without spending much time and effort. Therefore, a variety of approaches have been used to perform recommendations in these domains, including content based, collaborative, demographic, knowledge-based or hybrid approaches [2, 11, 15]. Abowd et al. [1] proposed a mobile context aware tour guide, called CyberGuide, which allows its users to leave messages to exhibit owners and send reports about his/her location to some central service that others can access. This system detects the user's location using GPS for an outdoor environment and RF for the indoor version. Fleck et al. [6] developed a “guidebook” system for the Exploratorium in San Francisco. The guidebook prototype provides two communication functions, named rememberer and communicator. The rememberer provides visitors with the means to build a record of their experiences. The communicator function helps visitors communicate using electronic bulletin boards for individual exhibits, instant-messaging and/or beaming information between handheld devices. Huang and Chuang [10] utilized the association rules mining technique to form a set of recommended exhibits. Based on the mining results, this guide system shows related exhibits via the active model and location-aware service when users check for a speci<sup>fi</sup>c exhibit.

Niaraki and Kim [17] presented a generic ontology-based architecture using a multi-criteria decision making technique to design a personalized route planning system. An ontology-based knowledge modeling technique uses an analytical hierarchical process to determine the choice of criteria for applying an impedance function in the route <sup>fi</sup>nding algorithm. Wang et al. [25] presented semantic web technologies for providing personalized access to digital museum collections. These technologies collect the user's pro<sup>fi</sup>le information in context including the user's personal information, objects that the user has interacted with, user activities over the objects and corresponding contextual information. A content-based <sup>fi</sup>ltering method is then employed to recommend artworks and art-history topics to cope with the typical user modeling problems. Huang and Bian [9] proposed an intelligent recommendation system that offers personalized recommendations for tourist attractions at a given destination. Through a tourism ontology application, Bayesian network technique and analytic hierarchy process method, this system provides recommendations to a user by taking into account the travel behavior of the current user and previous users. This system leads to more intelligence, collaboration and personalization in tourist attraction recommendations.

Schiaf<sup>fi</sup>no and Amandi [20] presented an expert software agent in the tourism and travel domain, named Traveler. This agent combines collaborative <sup>fi</sup>ltering with content-based recommendations and demographic information about customers to make recommendations. The agent assists users by suggesting a package of holidays that are presumably interesting for the user according to his/her pro<sup>fi</sup>le. The results revealed that a combination of these three approaches overcomes the dif<sup>fi</sup>culties in each method used in isolation. García-Crespo et al. [7] presented the SPETA system, which uses knowledge of the user's current location, preferences, as well as a history of past locations to provide the type of recommender services that tourists expect from a real tour guide. The SPETA framework, taking advantage of Web 3.0 technologies, provides a fully-<sup>fl</sup>edged platform, architecture and a proof-of-concept implementation that presents, on one hand, a combination of the mentioned cutting-edge technologies and emerging standards; and on the other hand, re<sup>fl</sup>ects research efforts and innovation.

The above tourism recommendation systems have demonstrated themselves ef<sup>fi</sup>cient tools by designing user interfaces that can smoothly interact with the environment, providing convenient information query tools, or suggesting a set of associated products (or services). However, few studies focused on how to offer tourists a customized visiting itinerary that guides them completely through their trip [24]. For example, most previous tourism recommendation systems suggest that places A, B, C, and D are worth visiting, but they do not provide information that route $\mathtt { A \to B \to C \to D }$ is better than $\mathsf { C } \to \mathsf { B } \to \mathsf { A } \to \mathsf { D } .$ However, the visiting sequence is a very important factor that helps tourists complete their trips on time. Without a personalized route suggestion, tourists tend to make an inef<sup>fi</sup>cient trip or even get lost in the complex theme park environment.

Actually, four important considerations should be included when making a theme park route recommendation. First, most visitors do not have plenty of time to visit the whole theme park and wish to <sup>fi</sup>nish their trip close to their given intended-visiting time. If the time constraint is not taken into account in the suggestion, tourists will feel very rushed or even have no time to visit their favorite rides. Second, tourists usually have a set of “must-play” rides in mind before starting their trips in the theme park. Tourists will feel disappointed if these favorite rides are not included in their visiting itinerary. Third, instead of considering the route recommendation problem as an optimization problem that minimizes the total visiting time, route suggestions should be based on the visiting behaviors of previous tourists. Finally, quite often in theme parks visitors congregate in certain areas while at the same time other adjacent areas are vacant. If the recommendation system can take the crowd situation into consideration and provide a less congested route, the service quality of the theme parks should be higher [14].

To achieve the above goals, this research developed a route recommendation system that provides personalized visiting routes for tourists in theme parks that consider a set of visiting constraints. The remainder of this paper is organized as follows. Section 2 introduces the system architecture and assumptions for the discussed theme parks. Section 3 details the proposed route recommendation system. Section 4 provides an example to show the feasibility and performance of the proposed system. Section 5 highlights the contribution and limitation of this research. Section 6 summarizes this research and points out future research directions.

## 2. System architecture and assumption

Recently, radio-frequency identi<sup>fi</sup>cation (RFID) systems have been successfully applied in many theme parks such as Legoland amusement park in Denmark, Steamboat Ski Resort (CO), Wild Rivers (CA), Dolly's (TN) and KeyLime Cove Water Resort (IL) in the USA [5, 19]. In this research, a RFID system is assumed to be available in the studied theme parks. When tourists enter a theme park, they are provided with a wristband embedded with a RFID tag with a unique electronic product code (EPC) [16, 26]. RFID readers are installed in the entrance and exit of each recreation facility (ride). Whenever a tourist enters the navigating area of a RFID reader, the reader will record the corresponding EPC code and time and transfer this information to the Ride Information Server and the Route Database Server, as shown in Fig. 1. The recording process is repeated until the tourists leave the theme park. Note that, with this process, the number of tourists in the queue of each ride is monitored in real time by the RFID system and stored into the Ride Information Server.

![](/api/attachments/YYUGRPG8/fulltext/images/889660a208bf262e4adf13d42e3e31f9bfebf9de96cb6f2c3c34d045544afa13.jpg)  
Fig. 1. The illustration of visiting sequence collection process.

![](/api/attachments/YYUGRPG8/fulltext/images/0f134c32d9dda715ffc81c59396ab3fae00c17c947f9c8f986dee085aa0ab776.jpg)  
Fig. 2. The illustration of requesting a route recommendation service

Public information booths which contain RFID readers are placed at the locations of rides, food courts, souvenir shops and information centers to provide route recommendation service to visitors. The visitor can initiate this service by approaching his/her wristband and input his/her personal preference at the booth. The booth will transfer the visitor's EPC code, booth location, current time and personal preference to the Route Recommendation System. The Route Recommendation System, which is the core component of the proposed system, generates an appropriate route recommendation based on the queue information of each ride from the Ride Information Server and visiting sequences from the Route Database Server. The route recommendation will be transferred back to the booth for the visitor's reference. Fig. 2 illustrates the route recommendation service request process.

## 3. Route recommendation system

The Route Recommendation System consists of three major modules, as shown in Fig. 3. The <sup>fi</sup>rst module, the tourist clustering module, segments all tourists’ visiting sequences in the route database into sub-groups based on the dissimilarity among the tourists’ visiting sequences and time lengths. The second module, the sub-group retrieval module, <sup>fi</sup>nds the sub-group that is most similar to a visitor's input preference. The personal preference includes the intended departure time, favorite thematic regions with preferred order and wished staying time length, and favorite rides. The last module, the route generation module, takes the visiting behavior data identi<sup>fi</sup>ed in the second module and the queuing information from each ride identi<sup>fi</sup>ed by the RFID system to generate an appropriate visiting recommendation for the visitor.

## 3.1. Data preparation and preprocessing

In general, a theme park might contain more than a hundred recreation facilities (also called rides), and each of them belongs to a speci<sup>fi</sup>c thematic region. Let $R = \{ R _ { 1 } , R _ { 2 } , . . . , R _ { N } \}$ be the set of rides in the theme park and $T = \{ T _ { 1 } , T _ { 2 } , . . . , T _ { M } \}$ be the set of thematic regions in the theme park. Based on theme park practices, a transformation function that describes the hierarchical relationship between $R _ { i 2 } { \in } R$ and $T _ { j \ell } { \in } T .$ is:

$$
f: R _ {i} \to T _ {j}.\tag{1}
$$

For example, based on the hierarchical structure de<sup>fi</sup>ned in Fig. 4, the transformation function is de<sup>fi</sup>ned as $f ( R _ { 1 } ) = f ( R _ { 2 } ) = f ( R _ { 3 } ) = T _ { 1 } , f$ $( R _ { 4 } ) = f ( R _ { 5 } ) = f ( R _ { 6 } ) = f ( R _ { 7 } ) = T _ { 2 } ,$ and so on.

![](/api/attachments/YYUGRPG8/fulltext/images/2264a5df341dc89d27c5f1e1b0867e61307681528bfa655ca325f0e0bf1636bd.jpg)  
Fig. 3. The three modules in the Route Recommendation System.

Table 1  
![](/api/attachments/YYUGRPG8/fulltext/images/651c389401d46ce9b49370e38c0bed6e1919d62f478abbbc457af02282b3209f.jpg)  
Fig. 4. An example hierarchical structure.

Let a visiting record in the route database RD be represented by bcid, vs>, where cid is a record identi<sup>fi</sup>er and vs is a visiting sequence. The visiting sequence vs is represented as $( ( r _ { 1 } , t s _ { 1 } , t e _ { 1 } ) , ( r _ { 2 } , t s _ { 2 } , t e _ { 2 } ) , . . . ,$ $\left( r _ { n } , t s _ { n } , t e _ { n } \right) )$ where $r _ { i 2 } \in R ,$ , and $t s _ { i }$ is the arrival time to $r _ { i } , t e _ { i }$ is the departure time from $r _ { i } ,$ and $t s _ { i } { < } t e _ { i }$ for $i { = } 1 , . . . , n .$ . Table 1 illustrates an example visiting sequence in a route database RD.

In practice, visiting sequences collected by the RFID system might contain many inappropriate sequences. For example, in a theme park, tourists tend to traverse popular rides more than one time. However, a recommendation system should not suggest the same activities again and again. Therefore, a redundancy check should be conducted. That is, if a ride is visited more than once, the redundancy check procedure will keep the <sup>fi</sup>rst ride in the sequence and remove the recurring visits to that ride since the ride taken in the front position of the visiting sequence is considered as having higher preference. For example, the visiting sequence cid 1 in Table 1 should be remedied as $\left( ( R _ { 1 } , 1 0 , 3 0 ) \right)$ $( R _ { 3 } , 4 0 , 8 0 ) , ~ ( R _ { 9 } , 8 5 , 9 5 ) , ~ ( R _ { 5 } , 1 0 0 , 1 2 0 ) , ~ ( R _ { 7 } , 1 2 6 , 1 4 6 ) , ~ ( R _ { 2 1 } , 1 5 0 , 1 9 0 )$ $( R _ { 2 3 } , 2 0 0 , 2 5 0 ) )$ since redundancies $( R _ { 9 } , 1 2 5 , 1 8 0 ) )$ and $( ( R _ { 5 } , 2 0 0 , 3 0 0 ) )$ appear in the sequence. In addition, if a visiting sequence contains only one ride, it should be eliminated. For instance, cid 5 in Table 1 poses only one ride experience and should be removed. Table 2 shows the visiting sequences after taking data preprocessing for the route database in Table 1.

## 3.2. Tourist clustering module

The tourist clustering module segments all visiting sequences in RD into a set of sub-groups in which each sub-group contains a set of similar visiting sequences. However, clustering visiting sequences at the ride level might produce two problems. First, it is dif<sup>fi</sup>cult and trivial to <sup>fi</sup>nd similar visiting sequences at the ride level because there are a great number of rides in a visiting sequence. Second, tourists at a theme park tend to visit thematic regions one by one. That is, they select a target thematic region <sup>fi</sup>rst and then move to the next thematic region after completing the activities in the <sup>fi</sup>rst region. Therefore, instead of clustering similar visiting sequences at the ride level, this research transforms the visiting sequences represented at the ride level into sequences represented at the theme level. The ride sequences are then clustered at the theme level.

An example route database RD.

<table><tr><td>Cid</td><td>Visiting sequence</td></tr><tr><td>1</td><td> $((R_1,10,30),(R_3,40,80),(R_9,85,95),(R_5,100,120),(R_7,126,146),(R_{21},150,190), (R_{23},200,250),(R_9,125,180),(R_5,200,300))$ </td></tr><tr><td>2</td><td> $((R_1,10,45),(R_2,35,45),(R_5,70,95),(R_6,100,135),(R_7,140,180),(R_6,190,250))$ </td></tr><tr><td>3</td><td> $((R_1,10,50),(R_2,60,65),(R_6,85,125),(R_1,210,330))$ </td></tr><tr><td>4</td><td> $((R_9,5,30),(R_7,45,65),(R_3,70,95),(R_5,100,140))$ </td></tr><tr><td>5</td><td> $((R_1,50,100))$ </td></tr></table>

## 3.2.1. Transformation process

The transformation process transforms a visiting sequence represented at the ride level into a sequence represented at the theme level according to the following four steps. First, ride r in a visiting sequence is replaced by the corresponding theme $t _ { j }$ for all visiting sequences in RD according to the transformation function in Eq. (1). The visiting sequence $( ( r _ { 1 } , t s _ { 1 } , t e _ { 1 } ) , ( r _ { 2 } , t s _ { 2 } , t e _ { 2 } ) , . . . , ( r _ { n } , t s _ { n } , t e _ { n } ) )$ is represented at the ride level where $r _ { i 2 } \in R$ is transformed to the visiting sequence represented at the theme level as $( ( t _ { 1 } , t s _ { 1 } , t e _ { 1 } ) , ( t _ { 2 } , t s _ { 2 } , t e _ { 2 } )$ $\left( t _ { n } , t s _ { n } , t e _ { n } \right) )$ where $t _ { j ? } \in T .$ Second, in a visiting sequence, if the number of rides consecutively taken within the same theme $t _ { j } \mathrm { i } s$ less than a userde<sup>fi</sup>ned consecutive ride threshold, $\rho _ { j } ,$ those rides will be removed from the sequence because those rides are not signi<sup>fi</sup>cant enough to be represented in a visiting experience at the theme level. For simplicity, $\rho _ { j }$ can be set as the average number of rides consecutively taken by all tourists in theme $t _ { j } .$

Third, rides consecutively taken within the same thematic region are aggregated into their corresponding thematic region. After aggregation, a sequence is represented as $( ( t _ { 1 } , \ t s _ { 1 } , \ t e _ { 1 } ) , \ ( t _ { 2 } , \ t s _ { 2 } , \ t e _ { 2 } )$ $( t _ { m } , t s _ { m } , t e _ { m } ) )$ where $t s _ { j }$ is the starting time of the <sup>fi</sup>rst ride belonging to theme t and $t e _ { j }$ is the departure time for the last ride belonging to theme $t _ { j } .$ If the time length staying at a theme $t _ { j }$ is less than a userde<sup>fi</sup>ned minimum time threshold, $\varphi _ { j } ,$ that theme experience should be ignored and eliminated from the sequence. In this study, $\varphi _ { j }$ can be set as the average time length spent by all tourists for theme $t _ { j }$ and the time length at theme $t _ { j } ,$ denoted as $t l _ { j } ,$ is calculated according to Eq. (2). After completing steps one to four, a visiting sequence is then represented as $( ( t _ { 1 } , t l _ { 1 } ) , ( t _ { 2 } , t l _ { 2 } ) , . . . , ( t _ { m } , t l _ { m } ) )$ .

$$
t l _ {j} = \left\{ \begin{array}{l l} \left[ t e _ {j} + \left(t s _ {j + 1} - t e _ {j}\right) / 2 \right] - t s _ {j}, & \text { if   } j = 1 \\ \left[ t e _ {j} + \left(t s _ {j + 1} - t e _ {j}\right) / 2 \right] - \left[ t s _ {j} - \left(t s _ {j} - t e _ {j - 1}\right) / 2 \right], & \text { if   } 1 <   j <   m \\ t e _ {j} - \left[ t s _ {j} - \left(t s _ {j} - t e _ {j - 1}\right) / 2 \right], & \text { if   } j = m \end{array} \right.\tag{2}
$$

Let's take the route database in Table 2 and the hierarchical structure in Fig. 4 as an example. The visiting sequence for cid 1 $( ( R _ { 1 } , 1 0 , 3 0 )$ $( R _ { 3 } , 4 0 , 8 0 ) , \quad ( R _ { 9 } , 8 5 , 9 5 ) , \quad ( R _ { 5 } , 1 0 0 , 1 2 0 ) , \quad ( R _ { 7 } , 1 2 6 , 1 4 6 ) , \quad ( R _ { 2 1 } , 1 5 0 , 1 9 0 )$ $( R _ { 2 3 } , 2 0 0 , 2 5 0 ) )$ is transferred as ((T , 10, 30), (T , 40, 80), (T , 85, 95), $( T _ { 2 } , 1 0 0 , 1 2 0 ) , ( T _ { 2 } , 1 2 6 , 1 4 6 ) , ( T _ { 4 } , 1 5 0 , 1 9 0 ) , ( T _ { 4 } , 2 0 0 , 2 5 0 ) )$ in step one. If the consecutive ride threshold $\rho _ { j }$ is set as 2 for all themes, (T , 85, 95) will be removed because only one ride is taken in theme $T _ { 3 } .$ Therefore, the visiting sequence for cid 1 will be modi<sup>fi</sup>ed as $( ( T _ { 1 } , 1 0 , 3 0 ) , ( T _ { 1 } , 4 0 ,$ 80), (T<sub>2</sub>, 100, 120), (T<sub>2</sub>, 126, 146), (T<sub>4</sub>, 150, 190), (T<sub>4</sub>, 200, 250)) in step two. cid 1 is then aggregated as $( ( T _ { 1 } , 1 0 , 8 0 ) , ( T _ { 2 } , 1 0 0 , 1 4 6 ) , ( T _ { 4 } , 1 5 0 ,$ 250)) in step three. Based on Eq. (2), $t l _ { 1 } = [ 8 0 + ( 1 0 0 - 8 0 ) / 2 ] -$ $1 0 = 8 0 , t l _ { 2 } = [ 1 4 6 + ( 1 5 0 - 1 4 6 ) / 2 ] - [ 1 0 0 - ( 1 0 0 - 8 0 ) / 2 ] = 5 8 , t l _ { 4 } =$ $2 5 0 - [ 1 5 0 - ( 1 5 0 - 1 4 6 ) / 2 ] = 1 0 2$ . If the minimum time threshold $\varphi _ { j }$ is set at 70 for all themes, the visiting sequence cid 1 is transformed as $( ( T _ { 1 } , 8 0 ) , ( T _ { 4 } , 1 0 2 ) )$ in step four since the time staying in theme T is not signi<sup>fi</sup>cant enough.

The modi<sup>fi</sup>ed route database after conducting data preprocessing.

<table><tr><td>Cid</td><td>Visiting sequence</td></tr><tr><td>1</td><td> $((R_1,10,30),(R_3,40,80),(R_9,85,95),(R_5,100,120),(R_7,126,146),(R_{21},150,190),(R_{23},200,250))$ </td></tr><tr><td>2</td><td> $((R_1,10,45),(R_2,35,45),(R_5,70,95),(R_6,100,135),(R_7,140,180))$ </td></tr><tr><td>3</td><td> $((R_1,10,50),(R_2,60,65),(R_6,85,125))$ </td></tr><tr><td>4</td><td> $((R_9,5,30),(R_7,45,65),(R_3,70,95),(R_5,100,140))$ </td></tr></table>

## 3.2.2. Dissimilarity measurement

Let a visiting sequence S be $( ( t _ { 1 } ^ { a } , t l _ { 1 } ^ { a } ) , ( t _ { 2 } ^ { a } , t l _ { 2 } ^ { a } ) . . . , ( t _ { p } ^ { a } , t l _ { p } ^ { a } ) )$ and $S _ { b }$ be $( ( t _ { 1 } ^ { b } , t _ { 1 } ^ { l _ { 1 } ^ { b } } ) , ( t _ { 2 } ^ { b } , t _ { 2 } ^ { l _ { 2 } ^ { b } } ) , . . . , ( t _ { q } ^ { b } , t _ { q } ^ { l _ { q } ^ { b } } ) )$ where $t _ { i } ^ { a } \in T , t _ { j } ^ { b } \in T , t l _ { i } ^ { a }$ and tl<sub>j</sub><sup>b</sup> are the corresponding time lengths. The dissimilarity measure between $S _ { a }$ and $S _ { b } ,$ denoted as $D S i m ( S _ { a } , S _ { b } )$ , is de<sup>fi</sup>ned as:

$$
D S i m (S _ {a}, S _ {b}) = \sum_ {k = 1} ^ {l} \left(w _ {k} \times C o s t _ {a, b, k}\right) / \sum_ {k = 1} ^ {l} w _ {k}\tag{3}
$$

where $l = M a x \ ( - S _ { a } | , | S _ { b } | )$ is the maximal sequence length among $S _ { a }$ and $S _ { b } ,$ and $w _ { k } = ( l - k + 1 ) / l$ is the penalty weight in position k. In addition, $C o s t _ { a , b , k }$ is the cost that changes $( t _ { k } ^ { b } , ~ t l _ { k } ^ { b } )$ in $S _ { b }$ to (t<sup>a</sup>, tl<sup>a</sup>) in $S _ { a }$ according to the edit distance (or Levenshtein distance) concept which is based on the following rule:

$$
C o s t _ {a, b, k} = \left\{ \begin{array}{l l} \psi_ {a, b, k}, & \text { if   no   change   between   } t l _ {k} ^ {a} \text {   and   } t l _ {k} ^ {b} \\ 1, & \text { if   deletion,   insertion,   or   substitution } \end{array} \right.\tag{4}
$$

where $\psi _ { a , \ b , \ k }$ is the time dissimilarity between tl<sup>a</sup> and tl<sup>b</sup> which is de<sup>fi</sup>ned as:

$$
\psi_ {a, b, k} = \left| \left(t l _ {k} ^ {a} - t l _ {k} ^ {b}\right) / M a x \left(t l _ {k} ^ {a}, t l _ {k} ^ {b}\right) \right|.\tag{5}
$$

If the two sequences are exactly the same, the dissimilarity between the two sequences is 0. Conversely, if both sequences have no match, the dissimilarity is 1. The detailed cost evaluation algorithm can be found in [22, 23].

## 3.2.3. K-Medoids clustering algorithm

When the dissimilarities between all pairs of visiting sequences are derived using Eq. (3), the K-Medoids clustering algorithm is applied to cluster all visiting sequences in RD. The K-Medoids algorithm is derived from the K-Means algorithm and is more robust in handling noisy data and outliers. A typical K-Means algorithm randomly chooses K initial centroids, where a centroid is a virtual point. In contrast, the K-

Medoids algorithm begins by randomly selecting an actual data point, called a medoid. In this study, the number of K sub-groups and dissimilarities between all pairs of visiting sequences are the input to the K-Medoids algorithm, while the output is the K subgroups $\{ R D _ { i } | \ i = 1 , . . . , K \}$ where RD contains the visiting sequences for the ith sub-group. Fig. 5 illustrates the pseudo-code for the K-medoids algorithm for clustering all visiting sequences into K sub-groups.

## 3.3. Sub-group retrieval module

When a visitor wants to request a route recommendation, he/she simply holds his/her wristband to the RFID reader in a public information booth and enters their personal preferences to the booth. The visitor's preference includes (1) the intended departure time, LT; (2) a set of wished visiting sequences at the theme level FT where $F T = ( ( t _ { 1 } , t l _ { 1 } ) , ( t _ { 2 } , t l _ { 2 } ) , . . . , ( t _ { j } , t l _ { j } ) )$ in which $t _ { j ? } \in T$ is the jth thematic region the visitor wishes to visit and $t l _ { j }$ is the time length the visitor wished to stay in $t _ { j } ;$ and (3) a set of favorite rides FR where $F R = \{ t _ { j } | t _ { j ? } { \in } T \}$ . In addition, the time a route recommendation is requested is denoted as CT and the public information booth location denoted as BL are automatically collected by the system. The request information (RI) vector sent to the Route Recommendation System is:

$$
R I = C T, B L, L T, F T, F R\tag{6}
$$

For example, assume that the theme park opens at 8:00 am. If a visitor requests a route recommendation from booth B05 at 8:30 am and enters his intended departure time as 6:30 pm, CT=30, BL=B05, and LT=630 will be collected. The visitor wishes to spend 4 h for his/her <sup>fi</sup>rst priority thematic region - theme 3 (T ) and 3 h for his/her second priority area - theme 2 (T<sub>2</sub>), so that $F T = ( ( T _ { 3 } , 2 4 0 ) , ( T _ { 2 } , 1 8 0 ) )$ . Finally, he/she inputs <sup>fi</sup>ve favorite rides (rides $1 , 2 , 3 , 5 ,$ and 6) that he/she wishes to play, which results in $F R = \{ R _ { 1 } , R _ { 2 } , R _ { 3 } , R _ { 5 } , R _ { 6 } \} $ . Based on the above information, RI=b30, B05, 630, $( ( T _ { 3 } , 2 4 0 ) , ( T _ { 2 } , 1 8 0 ) ) , \{ R _ { 1 } , R _ { 2 } ,$ $R _ { 3 } , R _ { 5 } , R _ { 6 } \} >$

The sub-group retrieval module <sup>fi</sup>rst evaluates the dissimilarity values between all medoids for sub-groups and the set of wished visiting sequences at the theme level FT of the RI vector using $\operatorname { E q . } \left( 3 \right) .$ . The module then returns all visiting sequences in the sub-group RD<sub>retrieved</sub> in which the medoid of $R D _ { r e t r i e v e d }$ is most similar to FT among all RD where $i { = } 1 , { \ldots } , K .$ If more than one sub-group has the same dissimilarity value, the sub-group having the largest data size is selected.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
K-Medoids algorithm:
Input: the number of sub-groups K and the route database RD
Output: K sub-groups  $\{RC_{i} | i=1, \ldots, K\}$ 

1 Begin
2 Randomly choose K data points from RD as medoids  $m_{1}, m_{2}, \ldots, m_{K}$ ;
3 Repeat
4 Assign remaining non-medoid data points to its closest medoid;
5 Compute total distance of  $RC_{i}, TD_{i}$ , between  $m_{i}$  and non-medoid  $r_{j}, j=1, \ldots, |RC_{i}|, i=1, \ldots, K$ ;
6 For each medoid  $m_{i}$  do
7 Select the non-medoid  $r_{j}$  for which  $TD_{i}$  is minimal;
8 Compute  $TD_{i}(r_{j}\rightarrow m_{i})$ ;
9 If  $TD_{i}(r_{j}\rightarrow m_{i})$  is smaller than the current  $TD_{i}$ ;
10 Swap  $m_{i}$  and  $r_{j}$ ;
11 End if
12 End for
13 Until no  $m_{i}$  changes;
14 End
</div>

Fig. 5. The pseudo-code for the K-medoids algorithm.

The visiting sequences after taking discretization.

<table><tr><td>Cid</td><td>Visiting sequence</td></tr><tr><td>1</td><td> $((R_1,2), (R_3,4), (R_9,1), (R_5,2), (R_7,2), (R_{21},4), (R_{23},5))$ </td></tr><tr><td>2</td><td> $((R_1,4), (R_2,1), (R_5,3), (R_6,4), (R_7,4))$ </td></tr><tr><td>3</td><td> $((R_1,4), (R_2,1), (R_6,4))$ </td></tr><tr><td>4</td><td> $((R_9,3), (R_7,2), (R_3,3), (R_5,4))$ </td></tr></table>

## 3.4. Route generation module

To generate a proper route recommendation, both of the previous tourist visiting experiences and real-time queuing situation of each ride should be considered. The previous tourist visiting experience can be derived from the visiting sequences in the sub-group RD<sub>retrieved</sub>, while the real-time queuing situation of each ride can be obtained by the RFID system in the theme park. Therefore, a recommendation matrix containing the above information is constructed <sup>fi</sup>rst in the route generation module. Based on the recommendation matrix and the visitor's personal preference, a route generation algorithm is then developed to generate a proper visiting sequence for the visitor's reference.

## 3.4.1. Recommendation matrix

In general, if the ride utilization is high or the staying time at a ride is long, the ride is popular and interesting to tourists. Therefore, the previous tourists’ experience can be evaluated in terms of how often a ride is visited and how long tourists stay at a ride. Let X and Y be two rides in the theme park where X and Y ∈R. The selection preference SP(X, Y) is de<sup>fi</sup>ned as the occurrence frequency that tourists visit ride Y right after visiting ride X, and is evaluated as:

$$
S P (X, Y) = S _ {(X \to Y)} / S _ {(X)}\tag{7}
$$

where support count $S _ { ( X  Y ) }$ is the total number of sequences in RD-<sub>retrieved</sub> in which Y is visited right after X is visited; support count $S _ { ( X ) }$ is the total number of sequences in $R D _ { r e t r i e v e d }$ where any ride is visited right after X is visited. The SP(X, Y) value is within [0, 1]. In addition, the time preference TP(X, Y) is de<sup>fi</sup>ned as the time length staying at ride Y if its immediate preceding ride is X, and is evaluated as:

$$
T P (X, Y) = T _ {(X \rightarrow Y)} / T _ {(X)}\tag{8}
$$

where $T _ { ( X  Y ) }$ is the sum of all discretized stay time lengths at Y when tourists visit Y right after visiting $\mathrm { X } ; T _ { ( X ) }$ is the sum of all discretized stay time lengths for any ride right after X is visited. The value of TP(X, Y) is within [0, 1]. If a visiting sequence vs is represented as $( ( r _ { 1 } , t s _ { 1 } , t e _ { 1 } ) , ( r _ { 2 } , t s _ { 2 } , t e _ { 2 } ) , . . . , ( r _ { n } , t s _ { n } , t e _ { n } ) )$ ) where $r _ { i ? } { \in } R ,$ the time length tl of ride r can be derived by $t s _ { n } - t e _ { i }$ . The discretized time length of tl can be obtained by:

$$
\text { Discre } (t l _ {i}) = \left\{ \begin{array}{l l} j, & \text { if   } I W \times (j - 1) <   t l _ {i} \leq I W \times j, \text {   for   } j \in \{1,..., N - 1 \} \\ N, & \text { if   } t l _ {i} > I W \times (N - 1) \end{array} \right.\tag{9}
$$

The discretization function enforces time length tl falls into be one of N intervals where IW is a user-de<sup>fi</sup>ned time interval width. The discretization function can reduce the number of continuous values and make the analysis more meaningful.

Based on Eqs. (7) to (9), an integrated preference that stands for the previous behavior in taking ride Y right after taking ride X, denoted as $I P ( X , Y ) ,$ , is de<sup>fi</sup>ned as:

$$
I P (X, Y) = S P (X, Y) \times T P (X, Y) = \frac {S _ {(X \rightarrow Y)} \times T _ {(X \rightarrow Y)}}{S _ {(X)} \times T _ {(X)}}\tag{10}
$$

The integrated preference value is within [0, 1]. If tourists do not prefer the experience $X  Y ,$ the integrated preference value should be low. Based on Eq. (10), the integrated preference values between all pairs of rides are calculated and stored in a previous tourist preference (PTE) matrix as shown in Eq. (11). Notes that PTE matrix is a non-symmetric matrix recording the previous tourist visiting preference from ride X to ride Y

```c
Route generation algorithm:
Input: The recommendation matrix (RM) and the request information vector RI = <CT, BL, LT, FT, FR>.
Output: a visiting sequence recommendation (RecRt).
1 Begin
2 TC = LT - CT;
3 MtVist = FR;
4 UnVist = {R - FR};
5 Assign BL to RecRt[0];
6 i=1;
7 While MtVist == { }
9 RecRt[i] = Search_Next_Ride(RecRt[i-1], MtVist, RM);
10 Recalculate TotVisT of RecRt;
11 Remove RecRt[i] from MtVist;
12 If TotVisT > TC
13 Remove RecRt[i] from RecRt;
14 Output RecRt and Stop;
15 Else
16 i=i+1;
17 End if
18 End while
19 While TotVisT < TC
20 If UnVist is empty
21 Output RecRt and Stop;
22 Else
24 r = Search_Inserted_Ride(RecRt, UnVist, RM, &Position);
25 Insert r into RecRt[Position] and RecRt[Position + 1]);
26 Recalculate TotVisT of RecRt;
27 Remove r from UnVist;
28 End while
29 Remove r from RecRt;
30 Output RecRt and Stop;
31 End
```  
Fig. 6. The pseudo-code for the route generation algorithm.

```txt
Function Search_Next_Ride (CurrentRride, MtVistList, RM)
1 MaxRecV = 0;
2 For each PotentialRide in MtVistList do
3 Assign RM [Index(CurrentRide), Index(PotentialRide)] to RecValue;
4 If RecValue > MaxRecV
5 Assign RecValue to MaxRecV;
6 Assign PotentialRide as r;
7 End if
8 End for
9 Return r;
End function
```  
Fig. 7. The pseudo-code for the Search\_Next\_Ride function.

$$
P T E = \left[ \begin{array}{c c c c c} 0 & I P (R _ {1}, R _ {2}) & I P (R _ {1}, R _ {3}) & \dots & I P (R _ {1}, R _ {N}) \\ I P (R _ {2}, R _ {1}) & 0 & I P (R _ {2}, R _ {3}) & \dots & I P (R _ {2}, R _ {N}) \\ I P (R _ {3}, R _ {1}) & \vdots & 0 & \dots & \vdots \\ \vdots & \vdots & \vdots & 0 & \vdots \\ I P (R _ {N}, R _ {1}) & I P (R _ {N}, R _ {2}) & \dots & \dots & 0 \end{array} \right] _ {N \times N}\tag{11}
$$

Taking Table 2 as an example, if the time interval width IW in Eq. (9) is set as 10 min and the largest time length in a ride is 40 min, 5 time intervals are obtained. Therefore, the discretization function can be de<sup>fi</sup>ned as: Discre(lt )=1 if 0b tl ≤10; Discre(lt )=2 if 10b tl ≤20; …; Discre(lt )=5 if $t l _ { i } > 4 0$ . After taking discretization, the visiting sequences are displayed in Table 3. Based on Eqs. (7) to (10), the integrated preference IP(R , $R _ { 2 } ) = ( 2 \times 2 ) / ( 3 \times 6 ) = 0 . 2 2 2 2$ since <sub>?</sub> $S _ { ( R _ { 1 }  R 2 ) } = 2 , \ : T _ { ( R _ { 1 }  R 2 ) } = 1 + 1 = 2 , \ : { , } S _ { ( R _ { 1 } ) } = 3 , \ : \mathrm { a n d } \ : _ { 7 } T _ { ( R _ { 1 } ) } = 4 + 1 + 1 = 6 .$

In addition to the previous tourist preference, tourists prefer the ride with shorter waiting time because most tourists wish to take more rides within a limited time. Therefore, to avoid a long queue waiting time, the ride queuing situation should be used to adjust the preference value for each ride. In the proposed system, the number of tourists in the queue for rides $r _ { i } ,$ denoted as CQ (r ), can be monitored in real-time through the RFID system. Therefore, the current ride preference (CRP) vector can be represented as:

$$
C R P = 1 / C Q (r _ {1}), \quad 1 / C Q (r _ {2}), \quad \dots , \quad 1 / C Q (r _ {i}), \quad \dots , \quad 1 / C Q (r _ {N})\tag{12}
$$

If the number of tourists in the queue for ride r is large, the ride is less preferred. Note that the min-max normalization is applied for CRP so that each element in the vector is within [0.0, 1.0].

Based on previous tourist preference PTE matrix and current ride preference CRP vector, the recommendation matrix is constructed as:

$$
R M = C R P \times P T E\tag{13}
$$

## 3.4.2. The route generation algorithm

The route generation algorithm is proposed in this research to generate a route recommendation for the visitor. The input to the algorithm includes the recommendation matrix RM of Eq. (13) and the RI vector (bCT, BL, LT, FT, FR>) of Eq. (6). The algorithm output is a visiting sequence recommendation, RecRt. The time constraint TC is set as LT-CT to ensure the recommended route can be <sup>fi</sup>nished in time. In addition, the MtVist list stores the rides the visitor wishes to visit, while the UnVist list stores the rides the visitor has not visited yet. Initially, the MtVist list is set as FR and the UnVist list is set as {R−FR} where R is the set of rides in the theme park. The pseudo-code of the proposed route generation algorithm is shown in Fig. 6.

This algorithm consists of two major phases. The <sup>fi</sup>rst phase, shown from lines 5 to 18, constructs a primary visiting sequence based on the MtVist list. The <sup>fi</sup>rst position in the primary sequence is the booth location (BL) where the visitor makes a request. The next ride is then selected from the ride in the MtVist list that has the largest recommendation value using the proposed Search\_Next\_Ride function. Once the ride is added into the sequence, the total visiting time (TotVisT) for the new sequence is recalculated and the ride is removed from the

```txt
Function Search_Inserted_Ride (RecRt, UnVist_list, RM, Position)
1 MaxRecV = 0;
2 For each CurrentRide in RecRt do
3 For each PotentialRide in UnVist_list do
4 If Index(CurrentRide) == |RecRt|
5 RecValue = RM [Index(RecRt[Index(CurrentRide)]), Index(PotentialRide)];
6 Else
7 RecValue = RM [Index(RecRt[Index(CurrentRide)]), Index(PotentialRide)] +
8 RM[Index(PotentialRide), Index(RecRt[Index(CurrentRide)+1)]);
9 End if
10 If RecValue > MaxRecV
11 Assign RecValue to MaxRecV;
12 Assign PotentialRide as r;
13 Assign Index(PotentialRide) to Position;
14 End if
15 End for
16 End for
17 Return r;
End function
```  
Fig. 8. The pseudo-code for the Search\_Inserted\_Ride function

![](/api/attachments/YYUGRPG8/fulltext/images/ab689523f0a304893b091f6742e98e24692487f74c0bf200b7561f54796f93bf.jpg)  
Fig. 9. The layout of the example theme park.

MtVist list. If TotVisT is larger than TC, the ride is removed and the primary visiting sequence is output as a route recommendation. Otherwise, the algorithm will repeat until there are no rides in the MtVist list. In this case, the algorithm will move to the second phase. The second phase of the algorithm as shown from lines 19 to 30 and expands the primary visiting sequence until TotVisT of the recommended sequence is greater than or equal to TC. To ful<sup>fi</sup>ll this requirement, the Search\_Inserted\_Ride function is proposed to <sup>fi</sup>nd the ride in the UnVist list that has the largest recommendation value if the ride is inserted between two adjacent rides in the sequence. The position of the insertion into the sequence is returned by the &Position variable. In this way, rides in the UnVist list are inserted into the primary visiting sequence gradually until TotVisT is greater than TC. The algorithm stops when the sequence ful<sup>fi</sup>lls the time constraint or no rides remain in the UnVist list.

Fig. 7 illustrates the pseudo-code for the Search\_Next\_Ride function. This function searches the ride in MtVist list having the largest recommendation value based on the recommendation matrix RM. Note that the Index(r) function returns the index number of ride r in the RM matrix. Fig. 8 shows the pseudo-code for the Search\_Inserted\_Ride function that searches for ride r from UnVist list and returns its inserted position. Because the ride is inserted between the current ride and the next ride in the sequence, the sum of the recommendation values from the current ride to the inserted ride and from the inserted ride to the next ride should be the largest.

Let us use an example to explain the second phase of the algorithm. Assume that a primary visiting sequence $R e c R t = R _ { 3 } \to R _ { 1 } \to R _ { 2 } \to R _ { 5 } \to R _ { 4 }$ is derived from the <sup>fi</sup>rst phase and UnVist l $s \mathrm { t } = \{ R _ { 6 } , R _ { 7 , } R _ { 8 } \}$ . The Search\_Inserted\_Ride function will evaluate the recommendation values of $R _ { 3 } \to R _ { 6 } \to R _ { 1 } , R _ { 3 } \to R _ { 7 } \to R _ { 1 } , R _ { 3 } \to R _ { 8 } \to R _ { 1 } , R _ { 1 } \to R _ { 6 } \to R _ { 2 } , R _ { 1 } \to R _ { 7 } \to R _ { 2 } ,$

Table 4  
The hierarchical structure between themes and rides.

<table><tr><td>Thematic region</td><td>Recreation facilities (Rides)</td></tr><tr><td> $T_1$ </td><td> $R_1, R_2, R_3$ </td></tr><tr><td> $T_2$ </td><td> $R_4, R_5, R_6, R_7, R_8$ </td></tr><tr><td> $T_3$ </td><td> $R_9, R_{10}, R_{11}, R_{12}$ </td></tr><tr><td> $T_4$ </td><td> $R_{13}, R_{14}$ </td></tr><tr><td> $T_5$ </td><td> $R_{15}, R_{16}, R_{17}, R_{18}, R_{19}, R_{20}, R_{21}, R_{22}, R_{23}, R_{24}$ </td></tr><tr><td> $T_6$ </td><td> $R_{25}, R_{26}, R_{27}, R_{28}, R_{29}, R_{30}, R_{31}, R_{32}, R_{33}$ </td></tr><tr><td> $T_7$ </td><td> $R_{34}, R_{35}, R_{36}, R_{37}, R_{38}, R_{39}, R_{40}$ </td></tr></table>

$R _ { 1 } \to R _ { 8 } \to R _ { 2 } ,$ and so on. This process is repeated until all possible combinations are checked. If $R _ { 1 } \to R _ { 7 } \to R _ { 2 }$ has the largest summarized recommendation value among all, for example, Position will be 2 and r will be $R _ { 7 }$ at the end of the function. The visiting sequence $R _ { 3 } \to R _ { 1 } \to$ $R _ { 7 } \to R _ { 2 } \to R _ { 5 } \to R _ { 4 }$ is then generated.

## 4. Experimental illustration

An example theme park as illustrated in Fig. 9 to demonstrate the feasibility of the proposed route recommendation system. The theme park includes 7 theme regions, 40 recreation facilities (rides) and 1 entrance/exit. The theme park operating hours are from 9 a.m. to

The visiting sequences collected from tourists.

<table><tr><td>Cid</td><td>Visiting sequence</td><td>Total time (min.)</td></tr><tr><td>1</td><td> $((R_4, 64.49, 90.13), (R_6, 93.88, 108.28), (R_5, 109.30, 131.90), (R_{12}, 139.16, 160.51), (R_{13}, 166.39, 179.71), (R_{21}, 187.27, 229.44), (R_{24}, 236.80, 304.32), (R_{26}, 306.20, 315.20), (R_{31}, 319.19, 346.76), (R_{30}, 348.34, 374.57), (R_{34}, 379.67, 400.77), (R_{38}, 406.76, 467.31), (R_{36}, 471.93, 515.48), (R_{39}, 520.93, 561.29))</td><td>496.80</td></tr><tr><td>2</td><td>\( ((R_1, 60.06, 85.77), (R_{40}, 90.20, 139.65), (R_{38}, 144.23, 210.61), (R_{36}, 215.23, 256.66), (R_{28}, 264.23, 321.64), (R_{25}, 326.34, 356.17), (R_{24}, 359.04, 424.84), (R_{18}, 427.69, 439.29), (R_{15}, 444.71, 465.32), (R_{21}, 469.55, 514.99), (R_{14}, 519.92, 557.50), (R_{13}, 560.40, 576.00), (R_{11}, 579.54, 636.42), (R_9, 638.52, 650.80), (R_5, 655.90, 686.01), (R_4, 688.83, 704.66))</td><td>644.60</td></tr><tr><td>5</td><td>\( ((R_4, 64.57, 92.25), (R_{11}, 101.62, 167.01), (R_{14}, 172.18, 214.40), (R_{20}, 219.11, 227.17), (R_{35}, 236.98, 252.45))$ </td><td>187.88</td></tr><tr><td>16</td><td> $((R_1, 60.42, 85.50), (R_3, 88.32, 100.02), (R_5, 107.55, 136.50), (R_8, 140.04, 154.78), (R_{11}, 158.23, 221.55), (R_{14}, 226.72, 264.62), (R_{13}, 267.52, 285.55), (R_{16}, 294.79, 324.40), (R_{17}, 326.51, 334.63), (R_{24}, 339.68, 406.58), (R_{27}, 410.79, 459.67), (R_{28}, 460.79, 523.35), (R_{30}, 525.40, 552.66), (R_{35}, 556.48, 576.50), (R_{36}, 578.78, 617.86), (R_{38}, 622.48, 675.48), (R_{40}, 680.06, 718.63))$ </td><td>658.21</td></tr><tr><td>54</td><td> $((R_1, 62.06, 96.69), (R_3, 99.51, 108.90), (R_7, 115.29, 129.09), (R_8, 131.19, 146.36), (R_{16}, 153.12, 180.54), (R_{17}, 182.65, 197.09), (R_{19}, 201.06, 222.80), (R_{18}, 227.97, 241.90), (R_{20}, 248.39, 261.27), (R_{21}, 264.25, 307.93), (R_{24}, 315.29, 380.78), (R_{28}, 385.96, 456.83), (R_{29}, 458.24, 470.85), (R_{33}, 475.75, 492.15), (R_{35}, 493.93, 512.19), (R_2, 520.18, 533.59))$ </td><td>471.53</td></tr><tr><td colspan="3">Note: minimum total time: 187.88 (min.), maximum total time: 658.21 (min.), average total time: 547.24 (min.)</td></tr></table>

Table 6  
The average number of consecutive rides and average time length spent in each theme area.

<table><tr><td>Theme</td><td>Average number of consecutive rides</td><td>Average time length (min.)</td></tr><tr><td>1</td><td>2</td><td>99.76</td></tr><tr><td>2</td><td>3</td><td>101.43</td></tr><tr><td>3</td><td>3</td><td>136.70</td></tr><tr><td>4</td><td>2</td><td>100.66</td></tr><tr><td>5</td><td>3</td><td>163.16</td></tr><tr><td>6</td><td>3</td><td>137.78</td></tr><tr><td>7</td><td>4</td><td>224.69</td></tr></table>

Table 7  
The summary of the four sub-groups.

<table><tr><td>Sub-Group</td><td>No. of sequences</td><td>Cid of medoid</td><td>Medoid represented at the theme level</td></tr><tr><td> $RD_{1}$ </td><td>15</td><td>4</td><td> $((T_{3}, 109.54), (T_{4}, 110.40), (T_{6}, 147.75), (T_{7}, 196.52))$ </td></tr><tr><td> $RD_{2}$ </td><td>8</td><td>7</td><td> $(T_{3}, 157.91)$ </td></tr><tr><td> $RD_{3}$ </td><td>10</td><td>17</td><td> $((T_{5}, 145.24), (T_{6}, 183.03))$ </td></tr><tr><td> $RD_{4}$ </td><td>9</td><td>54</td><td> $(T_{5}, 252.36)$ </td></tr></table>

10:00 $\mathrm { p . m . }$ . Table 4 shows the hierarchical structure between themes and rides in this theme park.

However, the RFID system is not deployed in this example theme park right now. Thus, a web questionnaire accompanying the theme park map is developed to collect the tourist visiting sequences. When a tourist (tester) moves a mouse over the ride position in the map, further information such as the thrill rating, ride time and the average queue time for each ride is presented so that the tourist can decide whether he/she will take that ride or not. Through the user friendly interface tourists answer the web questionnaire by imagining that he/she is traveling in the theme park. Table 5 summarizes the visiting sequences in the route database RD collected from 54 tourists.

## 4.1. Route recommendation generation

The proposed route recommendation system is implemented in C++ with STL (Standard Template Library) and tested on a PC with Core 2 Duo 2.20 GHz CPU and 2 GB memory. Before executing the system, data preprocessing is conducted including a redundancy check and singleton check. Fortunately, no inappropriate sequence in the route database was detected. Therefore, after conducting the data preprocessing procedure, the route database remained the same.

In the tourist clustering module, all visiting sequences represented at the ride level are transformed into the sequences represented at the theme level based on the hierarchical structure in Table 4. To exclude meaningless theme experiences in a sequence, $\rho _ { j }$ is set as the average number of consecutive rides taken by all tourists in theme $t _ { j } ,$ and $\varphi _ { j }$ is set as 80% of the average time length spent by all tourists in theme $t _ { j } .$ According to the data in Table 5, the average number of consecutive rides taken by all tourists and the average time length spent by all tourists in each theme area are derived and shown in Table 6.

After the transformation process, 12 visiting sequences are eliminated and 42 sequences are left. The dissimilarity values between all pairs of visiting sequences represented at the theme level is then evaluated. The K-Medoids algorithm is applied to divide the 42 visiting sequences into K sub-groups. To obtain a meaningful result, the number of clusters K is set as 4 in this implemented, so that four sub-groups whose medoid is cid 4 (called $R D _ { 1 } )$ , cid 7 (called $R D _ { 2 } )$ , cid 17 (called $R D _ { 3 } )$ and cid 54 (called $R D _ { 4 } )$ are constructed as shown in Table 7.

We assumed that a visitor requests a route recommendation at booth location $R _ { 1 }$ at 10:30 am. He inputs the intended departure time as 9:00 pm, the set of wished visiting sequences at the theme level as $( ( T _ { 2 } , 4 5 ) , ( T _ { 4 } , 6 0 ) , ( T _ { 5 } , 1 0 0 ) , ( T _ { 6 } , 1 4 0 ) , ( T _ { 7 } , 1 5 0 ) )$ , and the set of favorite rides as $\{ R _ { 3 8 } , R _ { 2 4 } , R _ { 1 3 } , R _ { 5 } , R _ { 2 8 } \}$ . Therefore, the RI vector is $< 9 0 , R _ { 1 } , 7 2 0 , ( ( T _ { 2 } , 4 5 ) , ( T _ { 4 } , 6 0 ) , ( T _ { 5 } , 1 0 0 ) , ( T _ { 6 } , 1 4 0 ) , ( T _ { 7 } , 1 5 0 ) )$ ), {R<sub>38</sub>, R<sub>24</sub>, R<sub>13</sub>, $R _ { 5 } ,$ R<sub>28</sub>}>. With the RI vector, the sub-group retrieval module identi<sup>fi</sup>es $R D _ { 1 }$ as the sub-group which is the most similar to the visitor's personal preference. Since the dissimilarity value between the input data and $R D _ { 1 }$ is 0.491, $R D _ { 2 }$ is 1.000, $R D _ { 3 }$ is 0.519, and $R D _ { 4 }$ is 0.793. This result is expected according to Table 7 since the medoid of $R D _ { 1 }$ has three common themes $( T _ { 4 } , T _ { 6 }$ and $T _ { 7 } )$ in the same appearance order matched with the input data $( ( T _ { 2 } , 4 5 ) , ( T _ { 4 } ,$ $6 0 ) , ( T _ { 5 } , 1 0 0 ) , ( T _ { 6 } , 1 4 0 ) , ( T _ { 7 } , 1 5 0 ) $ .

Based on the visiting sequences in $R D _ { 1 } , \mathsf { a } 4 0$ by 40 previous tourist preference (PTE) matrix is constructed using Eqs. (7) to (11). Note that the time interval width (IW) in Eq. (9) is set as 30 min in this implementation. The number of tourists in the queue of rides $r _ { i } ,$ denoted as CQ (r<sub>i</sub>), is generated by a data generation program to simulate the RFID system real-time data collection process. Therefore, the current ride preference (CRP) vector can be obtained. Based on the PTE matrix and the CRP vector, a recommendation matrix is constructed using $\operatorname { E q . } \left( 1 3 \right)$

![](/api/attachments/YYUGRPG8/fulltext/images/493975a6d6e3e752e49426b17bfb4f7f2da8cfb1d8f8fbfc5536b9e589fc5915.jpg)  
Fig. 10. The suggested route and visiting sequence of cid 16.

According to the RI vector, the route generation algorithm recognizes that the time constraint (TC) is 630.00 min, the must-visit list (MtVist) is rides 38, 24, 13, 5 and 28, and the un-visit list (UnVist) is the remaining 35 rides. After running the algorithm, the <sup>fi</sup>rst phase of the algorithm generates a primary visiting sequence as $R _ { 1 } {  } R _ { 5 } {  } R _ { 1 3 } {  } R _ { 2 4 } {  } R _ { 2 8 } {  } R _ { 3 8 } .$ Since the total visiting time (TotVisT) of the primary sequence (282.70 min) is less than TC, the algorithm is enforced to the second phrase. Finally, a route recommendation (RecRt) is generated as $R _ { 1 }  R _ { 3 }  R _ { 4 }  R _ { 2 }  R _ { 5 }  R _ { 9 }  R _ { 1 0 }  R _ { 8 }  R _ { 7 } $ $R _ { 6 } \to R _ { 1 1 } \to R _ { 1 2 } \to R _ { 1 3 } \to R _ { 2 4 } \to R _ { 3 1 } \to R _ { 3 3 } \to R _ { 2 6 } \to R _ { 3 2 } \to R _ { 2 8 } \to R _ { 2 9 } \to R _ { 3 8 } .$ The RecRt suggests 21 rides which cross 7 themes, and its TotVisT is 588.04 min which is less than but close to TC. It is clear that the RecRt not only meets the requirement of the visitor's <sup>fi</sup>ve wished thematic regions in the desired order $( T _ { 2 } {  } T _ { 4 } {  } T _ { 5 } {  } T _ { 6 } {  } T _ { 7 } )$ but also the visitor's <sup>fi</sup>ve favorite rides $( R _ { 5 } , R _ { 1 3 } , R _ { 2 4 } , R _ { 2 8 }$ and $R _ { 3 8 } )$

## 4.2. System validation

It is dif<sup>fi</sup>cult to compare the proposed route recommendation system with previous recommendation systems, since no route suggestion function is found in previous works. However, to show the bene<sup>fi</sup>t of the proposed system, the route suggestion generated by the proposed methods is compared with the original visiting sequence obtained from tourists. In this case, we compared the route suggested for the visitor in Section 4.1 with the cid 16 visiting sequence obtained from the route database in Table 5, since the cid 16 has the identical personal preference with the visitor discussed in Section 4.1 (actually the personal preference of the visitor is created by mimicking the visiting sequence of cid 16). The route suggested for the visitor is visually displayed in Fig. 10 with a solid line, while the cid 16 visiting sequence is displayed with a dashed line. Based on the <sup>fi</sup>gure it is clear that the route suggested for the visitor and the cid 16 visiting sequence have the same visiting order at the theme level $( T _ { 1 } {  } T _ { 2 } {  } T _ { 3 } {  } T _ { 4 } {  } T _ { 5 } {  } T _ { 6 } {  } T _ { 7 } )$ . However, the route for the visitor suggests 21 rides while the original visiting sequence of cid 16 contains only 17 rides. Four more rides were suggested for the visitor, the expected time to <sup>fi</sup>nish the suggested route is 630.00 min which is less than the total cid 16 visiting time (658.21 min). The result shows that the proposed system can ful<sup>fi</sup>ll the visitor's requirements and provide a richer visitation route.

![](/api/attachments/YYUGRPG8/fulltext/images/087c2def3afa5a590e33bc9997d3c774a9345bc1de7fc03b85c366f0d0ff7a1a.jpg)  
b

![](/api/attachments/YYUGRPG8/fulltext/images/7aa7590e53962f417958d32f6ff4f17bc50d2829748cb42ab52e160ac6cff96f.jpg)

## 4.3. The influence of personal preferences

Booth location (BL) where a visitor requests a route recommendation is an important factor for the proposed system. To know how BL affects the result, the booth location at rides 1, 4, 17, and 40 are tested while other settings are kept the same as the ones in Section 4.1. Fig. 11 (a) to 11(d) visually illustrate the RecRts generated by the four booth locations $R _ { 1 } , R _ { 4 } , R _ { 1 7 } ,$ , and $R _ { 4 0 }$ respectively. When BL is at $R _ { 1 }$ of theme $1 , R _ { 4 }$ of theme 2, R of theme $5 ,$ , and $R _ { 4 0 }$ of theme 7, the number of suggested rides is 21, 20, 18, and 18 respectively. In addition, all the four RecRts cover 7 themes and their routes tend to follow a clockwise direction.

The intended departure time (LT) is another important factor that a visitor is concerned about. To know the in<sup>fl</sup>uence of LT to the RecRt, we assume that the visitor intends to leave the theme park at 1:30 pm, 3:30 pm, 5:30 pm, and 9:00 pm. That is, the visitor wishes to spend 3, 5, and 7, 10.5 h to visit the theme park since CT is 10:30 am. Therefore, LT is 270, 390, 510, and 720 while other settings are kept the same. Fig. 12(a) to 12(b) visually display the RecRts for the four cases. Fig. $1 2 ( \mathsf { a } )$ indicates that 4 rides in 4 different themes are suggested $\left( R _ { 1 } \to R _ { 5 } \to R _ { 1 3 } \to R _ { 2 4 } \right)$ , since only 3 h is allowed in the theme park. For the rest of the three cases, all favorite rides provided by the user $\{ R _ { 3 8 } , R _ { 2 4 } , R _ { 1 3 } , R _ { 5 } , R _ { 2 8 } \}$ are in their RecRts. Fig. 12(b) indicates that $R _ { 1 } {  } R _ { 5 } {  } R _ { 1 3 } {  } R _ { 2 4 } {  } R _ { 2 8 } {  } R _ { 2 9 } {  } R _ { 3 8 }$ is recommended if the visitor can spend 5 h in the theme park. Similarly, Fig. 12(c) and (d) shows that 13 rides and 21 rides are suggested when the visitor can spend 7 and 10.5 h respectively.

![](/api/attachments/YYUGRPG8/fulltext/images/fee57fa45c9dba1fdf3bf785dc3850e16a5cacb3324f83dedcc6e0ef8e919b19.jpg)

![](/api/attachments/YYUGRPG8/fulltext/images/d84cbbec9d50891ab0e6db6a199d4acb92850d0e619272ad583665e10392fa7c.jpg)  
Fig. 11. The route recommendations when BL is at $R _ { 1 } , R _ { 4 } , R _ { 1 7 } ,$ and $R _ { 4 0 } .$

![](/api/attachments/YYUGRPG8/fulltext/images/47d5c121b4dc9b5c1dea24f50302b3216926b06e20cc2bb7769d3b536193abe2.jpg)  
Fig. 12. The route recommendations when the visitor spends 3, 5, 7, and 10.5 h.

## 4.4. System parameter analysis

A set of system parameters might affect the performance of the proposed system. These parameters include the consecutive ride threshold $\rho _ { j } ,$ the minimum time threshold $\varphi _ { j } ,$ the number of subgroups $K ,$ and the time interval width IW. Therefore, a set of experiments are conducted to observe the affection caused by these parameters. In the following discussion, the initial system parameter and visitor preference settings are summarized in Table 8.

## 4.4.1. The consecutive ride threshold

As discussed in Section 3.2.1, the transformation process transforms a visiting sequence represented at the ride level to the sequence represented at the theme level according to the four steps. In step two, if the number of rides consecutively taken within theme $t _ { j }$ is less than a userde<sup>fi</sup>ned consecutive ride threshold, $\rho _ { j } ,$ those rides will be removed from the sequence since they are considered not signi<sup>fi</sup>cant enough to represent a visiting experience at the theme level. To observe how $\rho _ { j }$ impacts the system, $\rho _ { j }$ is set as the value ranging from 40% to 220% of $\mu _ { C R , j }$ where $\mu _ { C R , j }$ is the average number of rides consecutively taken by all customers in theme $t _ { j } ,$ while other settings remain the same as the ones in Table 8. Table 9 shows a set of $\rho _ { j }$ values when different $\mu _ { C R , j }$ values are applied. For example, when $\rho _ { j }$ is set as 180% of $\mu _ { C R , j } ,$ $\rho _ { 1 } = 4 , \rho _ { 2 } = 5 , \rho _ { 3 } = 5 , \rho _ { 4 } = 4 , \rho _ { 5 } = 6 , \rho _ { 6 } = 6 , \rho _ { 7 } = 6$ . That means that 4 consecutive rides are required to make the ride experience for theme 1 signi<sup>fi</sup>cant, 5 consecutive rides are required to make the ride experience for theme 2 signi<sup>fi</sup>cant, and so on.

Table 8  
The initial settings for system parameters and visitor preferences.

<table><tr><td>System parameters</td><td>Value</td><td>Personal preferences</td><td>Value</td></tr><tr><td rowspan="2"></td><td rowspan="2">The average number of rides consecutively been taken in theme  $t_j$ </td><td>BL</td><td> $R_1$ </td></tr><tr><td>CT</td><td>90</td></tr><tr><td></td><td>The average time length spent for theme  $t_j$ </td><td>LT</td><td>720(( $T_2$  45), ( $T_4$  60),( $T_5$  100), ( $T_6$  140),( $T_7$  150))</td></tr><tr><td>K</td><td>3</td><td></td><td></td></tr><tr><td>IW</td><td>30 (min.)</td><td>FR</td><td> $\{R_{38}, R_{24}, R_{13}, R_5, R_{28}\}$ </td></tr></table>

After conducting the transformation process using $\rho _ { j }$ values in Table 9, the number of sequences passing the screening test is illustrated in Fig. 13. As shown in the <sup>fi</sup>gure, when $\rho _ { j }$ is set as 40% of μ , the number of remaining sequences equals the total number of sequences in the route database (54). It indicates that this setting does not have the screening capability for all themes, since all sequences survived. On the other hand, $\operatorname { i f } \rho _ { j }$ is set at a higher value, the number of remaining sequences is fewer because many sequences are deleted. Fig. 14 shows the average number of themes among those sequences passing the screening test when different $\rho _ { j }$ values are adopted. $\operatorname { I f } \rho _ { j }$ is set as the value from 60% to 160% of $\mu _ { C R , j } ,$ the average number of themes declines signi<sup>fi</sup>cantly from 2.27 to 1.22. Therefore, based on the observation from the two <sup>fi</sup>gures, this implementation suggests that $\rho _ { j }$ is as 120% of $\mu _ { C R , j } .$

The corresponding ρ values.

<table><tr><td rowspan="2"> $\mu_{CR,j}$ </td><td colspan="7">Theme</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>40%</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>60%</td><td>1</td><td>2</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td></tr><tr><td>80%</td><td>2</td><td>2</td><td>2</td><td>2</td><td>3</td><td>2</td><td>3</td></tr><tr><td>100%</td><td>2</td><td>3</td><td>3</td><td>2</td><td>3</td><td>3</td><td>4</td></tr><tr><td>120%</td><td>3</td><td>3</td><td>3</td><td>2</td><td>4</td><td>4</td><td>4</td></tr><tr><td>140%</td><td>3</td><td>4</td><td>4</td><td>3</td><td>4</td><td>4</td><td>5</td></tr><tr><td>160%</td><td>3</td><td>4</td><td>4</td><td>3</td><td>5</td><td>5</td><td>6</td></tr><tr><td>180%</td><td>4</td><td>5</td><td>5</td><td>4</td><td>6</td><td>6</td><td>6</td></tr><tr><td>200%</td><td>4</td><td>5</td><td>5</td><td>4</td><td>6</td><td>6</td><td>7</td></tr><tr><td>220%</td><td>5</td><td>6</td><td>6</td><td>4</td><td>7</td><td>7</td><td>8</td></tr></table>

![](/api/attachments/YYUGRPG8/fulltext/images/c0f67049709a54a2aa89ab755a3fb744713b0f4010f0d0f26b0139a20945361a.jpg)  
Fig. 13. The number of sequences passing the screening test under different $\rho _ { j }$ settings.

## 4.4.2. The minimum time threshold

Similar to the consecutive rides threshold $\rho _ { j }$ in step two of transformation process, the minimum time threshold, $\varphi _ { j } ,$ in step four is another critical threshold that should be decided. If the time length a visitor stays in theme $t _ { j }$ is less than a user-de<sup>fi</sup>ned $\varphi _ { j } ,$ the theme experience should be ignored and eliminated from the sequence. To observe how $\varphi _ { j }$ impacts the system, $\varphi _ { j }$ is set at a value ranging from 40% to 220% of $\mu _ { M T , j }$ where $\mu _ { M T , j }$ is the average time length spent by all customers in theme $t _ { j } ,$ while other settings remain the same as the one in Table 8. Table 10 shows the relationship between $\varphi _ { j }$ and $\mu _ { M T , j } ,$ where the unit of value in the table is minute.

Fig. 15 illustrates the number of sequences passing the screening test after conducting the transformation process. It is clear that the screening ability is very limited when $\varphi _ { j }$ ranges from 40% to 80% of μ ,. Conversely, no sequence passes the test if $\varphi _ { j }$ is set at a value greater than 180% of $\mu _ { \boldsymbol { M T } , j } .$ Fig. 16 indicates the average number of rides in the RecRt generated by the route recommendation generation module after 30 experimental runs. The largest average number of rides is 20.37 when φ is set at 100% of $\mu _ { \boldsymbol { M T } , j } .$ Based on the observation from the two <sup>fi</sup>gures, this implementation suggests that $\varphi _ { j }$ be set at 100% of $\mu _ { M T , j } .$

## 4.4.3. The number of sub-groups

As mentioned in Section 3.2.3, the K-Medoids clustering algorithm was applied to cluster visiting sequences in RD. To observe how the number of sub-groups K affects the system, this experiment changes K from 2 to 5 while the other settings remain the same as the one in Table 8. The clustering results are summarized in Table 11. It is clear that the clustering result might be either too rough or trivial if K is set at 2 or 5, respectively.

Fig. 17 illustrates that the average number of rides in the RecRt generated from the route recommendation generation module after 30 experiment runs. The largest average number of rides in the

![](/api/attachments/YYUGRPG8/fulltext/images/1c38292609eedcdeeb1c2da58a815ea7b03e355279a9964daf2a71a55b879ecd.jpg)  
Fig. 14. The average number of themes under different ρ settings.

Table 10  
The corresponding φ values

<table><tr><td rowspan="2"> $\mu_{MT,j}$ </td><td colspan="7">Theme</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>40%</td><td>20.0</td><td>20.3</td><td>27.3</td><td>20.1</td><td>32.6</td><td>27.6</td><td>44.9</td></tr><tr><td>60%</td><td>39.9</td><td>40.6</td><td>54.7</td><td>40.3</td><td>65.3</td><td>55.1</td><td>89.9</td></tr><tr><td>80%</td><td>59.9</td><td>60.9</td><td>82.0</td><td>60.4</td><td>97.9</td><td>82.7</td><td>134.8</td></tr><tr><td>100%</td><td>79.8</td><td>81.1</td><td>109.4</td><td>80.5</td><td>130.5</td><td>110.2</td><td>179.7</td></tr><tr><td>120%</td><td>99.8</td><td>101.4</td><td>136.7</td><td>100.7</td><td>163.2</td><td>137.8</td><td>224.7</td></tr><tr><td>140%</td><td>119.7</td><td>121.7</td><td>164.0</td><td>120.8</td><td>195.8</td><td>165.3</td><td>269.6</td></tr><tr><td>160%</td><td>139.7</td><td>142.0</td><td>191.4</td><td>140.9</td><td>228.4</td><td>192.9</td><td>314.6</td></tr><tr><td>180%</td><td>159.6</td><td>162.3</td><td>218.7</td><td>161.1</td><td>261.1</td><td>220.4</td><td>359.5</td></tr><tr><td>200%</td><td>159.6</td><td>162.3</td><td>218.7</td><td>161.1</td><td>261.1</td><td>220.4</td><td>359.5</td></tr><tr><td>220%</td><td>159.6</td><td>162.3</td><td>218.7</td><td>161.1</td><td>261.1</td><td>220.4</td><td>359.5</td></tr></table>

RecRt is obtained when K is set as 4, while the smallest one is the case that no clustering is performed $( K = 0 ) .$ A one way ANOVA test was conducted to know whether the above <sup>fi</sup>ve cases are signi<sup>fi</sup>cantly different in terms of the average number of recommended rides. Based on the result in Table 12, the difference between them is significant since p-value (0.000) is less than the signi<sup>fi</sup>cance level (0.05). A two-sample t-test was further conducted to test whether the difference between the clustering result with $K { = } 4$ and non-clustering was signi<sup>fi</sup>cant. The result indicates the two approaches are signi<sup>fi</sup>- cantly different in term of the average number of recommended rides. Based on the above observation, this implementation suggests that the number of sub-groups K is 4.

## 4.4.4. The time interval width

According to Eq. (9), different time interval widths IW might affect the discretization result in the route recommendation generation module. To observe how IW affects the recommendation result, IW was set as a value ranging from 10 to 50 min while other settings remained the same as those shown in Table 8. Fig. 18 shows the relationship between IW and the number of time intervals. When IW is 1, the number of time intervals is 74 because the longest staying time at a ride is 73.7 min in RD. Fig. 19 shows the average number of recommended rides in the RecRt generated by the route recommendation generation module after 30 experimental runs. The <sup>fi</sup>gure indicates that if IW is too large, the staying time at a ride tends to fall into a few time intervals. This makes the system hard to discriminate the time preference among sequences. Conversely, if IW is too small, the discrimination for the time preference is too strong so that few general behaviors are found. Therefore, this implementation suggests that IW be set to 30 min because the setting generates the largest average number of recommended rides.

![](/api/attachments/YYUGRPG8/fulltext/images/6a5d99c948d027ca0c0fbed9529213b11ef3751713beca2b277713ba4753a539.jpg)  
Fig. 15. The number of sequences passing the screening test under different φ settings.

![](/api/attachments/YYUGRPG8/fulltext/images/30370043731f69c89efc6245dc17b79f7001384c286349b59eb1ada3d33fea9b.jpg)  
Fig. 16. The average number of rides in the RecRt under different φ<sub>j</sub> settings.

Table 11  
The relationship between K and the number of sequences.

<table><tr><td>K</td><td>Number of sequences and its medoid in sub-groups</td></tr><tr><td>2</td><td>11 (cid 16), 23 (cid 50)</td></tr><tr><td>3</td><td>5 (cid 5), 8 (cid 54), 21 (cid 16)</td></tr><tr><td>4</td><td>5 (cid 7), 7 (cid 5), 8 (cid 16), 14 (cid 50)</td></tr><tr><td>5</td><td>5 (cid 10), 5 (cid 27), 6 (cid 6), 8 (cid 17), 10 (cid 11)</td></tr></table>

![](/api/attachments/YYUGRPG8/fulltext/images/c92931561edc74a64be7b4996acb4e8306a1783e9b1eaf8d813e2ba6515fafa6.jpg)  
Fig.17. The average number of rides in the RecRt under different K values.

## 5. Discussion

The major goal of this research is to provide tourists a visiting itinerary service that guides them completely through their trip. This service is not found in previous tourism recommendation systems, which focuses primarily on designing user friendly interfaces that can smoothly interact with the environment, provide convenient information query tools or suggest a set of associated products (or services). However, helpful visiting sequence information such as “you can follow the route $\mathsf { C } \to \mathsf { B } \to \mathsf { A } \to \mathsf { D }$ to complete your visit” is critical to assisting tourists complete their trips instead of “you are suggested to visit A, B, C, and D.” Without a route suggestion, tourists tend to have an inef<sup>fi</sup>cient trip or even get lost in the complex theme park environment. Based on the above goal, the contribution of this research is to generate a customized itinerary service based on tourists’ personal needs and the visiting experiences of previous tourists. First, most visitors do not have plenty of time to visit the whole theme park and wish to <sup>fi</sup>nish their trip close to their given intended-visiting time. Second, tourists usually have a set of “must-play” rides in mind before starting their trips in the theme park. Third, instead of considering the route recommendation problem as an optimization problem that minimizes the total visiting time, route suggestions should be based on the visiting behaviors of previous tourists. Finally, quite often in theme parks visitors congregate in certain areas while at the same time other adjacent areas are vacant. Route suggestions should lead visitors to escape the crowded area by providing a less congested route.

This research is based on the assumption that the tourist location is collected correctly and instantly. Therefore, a RFID system is suggested to collect tourist visiting behavior in the studied theme parks. When tourists enter a theme park, they are provided a wristband embedded with a RFID tag. RFID readers installed in the entrance and exit of each recreation facility (ride) will record the tag code and event time of each tourist into databases. With this recording process, the visiting sequence of all tourists and the queue length of each ride can be obtained in real time. However, when more people have intelligent mobile phones, the proposed route recommendation system can be packaged as an App and installed in tourists’ personal mobile devices before they visit the parks. In the App, the routing algorithm is executed on the server side while the route suggestion result is shown on the client side. Moreover, if the mobile phones have NFC (Near <sup>fi</sup>eld communication) capability which is an extension of RFID technology, the data collection process can be completed by tourists own mobile phones instead of using RFID wristbands.

Table 12  
ANOVA analysis for the <sup>fi</sup>ve cases.

<table><tr><td colspan="6">One-way ANOVA</td></tr><tr><td>Source</td><td>DF</td><td>SS</td><td>MS</td><td>F</td><td>P</td></tr><tr><td>K</td><td>4</td><td>33.893</td><td>8.473</td><td>16.43</td><td>0.000</td></tr><tr><td>Error</td><td>145</td><td>74.800</td><td>0.516</td><td></td><td></td></tr><tr><td>Total</td><td>149</td><td>108.693</td><td></td><td></td><td></td></tr><tr><td colspan="6"> $F(4,145) = 2.3808, p<.05$ </td></tr></table>

![](/api/attachments/YYUGRPG8/fulltext/images/7af0edeaf869258746c70640e47f8ed123d64c9658a7d64bd7f43c8f51823387.jpg)  
Fig. 18. The relationship between IW and the number of time intervals

## 6. Conclusions

Like any other industry, theme parks are now facing severe challenges from other entertainment competitors. To survive in this rapidly changing environment, creating high quality products/services in terms of consumer preferences has become a critical issue for theme park managers. Knowing which rides have been taken, which shows have been attended (and how much they've been enjoyed) and which shops and squares have attracted the attention of tourists, could lead to a radical improvement in satisfaction performance. This study proposed a route recommendation system that provides theme park tourists with which facilities (rides) they should visit and in what order.

When tourists enter a theme park, they are provided a wristband embedded with a RFID tag with a unique electronic product code (EPC). RFID readers are installed in the entrance and exit of each recreation facility (ride). Whenever a tourist enters the navigating area of a RFID reader, the reader will record the corresponding EPC code and time and transfer that information to the route database. In this way, tourist visiting behaviors (sequences) are continuously and persistently collected through a RFID system. The Route Recommendation System consists of three major modules. The <sup>fi</sup>rst module, the tourist clustering module, segments all tourist visiting sequences in the route database into sub-groups based on the dissimilarity among tourist visiting sequences and time lengths. The second module, the sub-group retrieval module, <sup>fi</sup>nds the sub-group which is the most similar to the preference of a visitor's input. The personal preference includes the intended departure time, favorite thematic regions with preferred order and wished staying time and favorite rides. The last module, the route generation module, takes the visiting behavior data identi<sup>fi</sup>ed in the second module and the queuing information from each ride identi<sup>fi</sup>ed by the RFID system to generate an appropriate visiting recommendation for the visitor.

![](/api/attachments/YYUGRPG8/fulltext/images/5c2468d45388605ff842f3687f8050e5ab2a22c2d2aa0160a34f21b2d64cac76.jpg)  
Fig. 19. The average number of rides in the RecRt under different IW settings.

There are some directions to improve the proposed system in the future. First, a set of system parameters including the consecutive ride threshold, the minimum time threshold, the number of subgroups, and the time interval width will affect the performance of the proposed system. Although their suitable ranges can be found through a set of experimental designs, it is a time-consuming task. It is suggested that researchers adopt optimization approaches to <sup>fi</sup>nd the best values in these parameters. Second, to enrich the proposed route recommendation, factors such as personal spending habits and diet favorites can be taken into consideration when generating the visiting sequence recommendation. Finally, some theme parks might have multi-entrances and multi-exits. It would be interesting if more complicated layouts can be explored and studied.

## Acknowledgement

This work was partially supported by the National Science Council of Taiwan, ROC, No. NSC 99-2221-E-155-055.

## References

[1] G.D. Abowd, C.G. Atkeson, J. Hong, S. Ling, R. Kooper, M. Pinkerton, Cyberguide: a mobile context‐aware tour guide, Wireless Networks 3 (5) (1997) 421–433.

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, Journal of IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[3] B.M. Braun, M.D. Soskin, Theme park competitive strategies, Annals of Tourism Research 26 (2) (1998) 438–442.

[4] Economics Research Associates, The future theme parks in international tourism, http://www.hotel-online.com/Trends/ERA/ERARoleThemeParks.html2008.

[5] G. Ferrer, N. Dew, U. Apte, When is RFID right for your service? International Journal of Production Economics 124 (2) (2010) 414–425.

[6] M. Fleck, M. Frid, T. Kindberg, E. O'Brien-Strain, R. Rajani, M. Spasojevic, From informing to remembering: ubiquitous systems in interactive museums, Pervasive Computing 1 (2) (2002) 13–21.

[7] A. García-Crespo, J. Chamizo, I. Rivera, M. Mencke, R. Colomo-Palacios, J.M. Gómez-Berbís, SPETA: social pervasive e-tourism advisor, Telematics and Informatics 26 (3) (2009) 306–315.

[8] C.Y. Heo, S. Lee, Application of revenue management practices to the theme park industry, International Journal of Hospitality Management 28 (3) (2009) 446–453.

[9] Y. Huang, L. Bian, A bayesian network and analytic hierarchy process based personalized recommendations for tourist attractions over the Internet, Expert Systems with Applications 36 (1) (2009) 933–943.

[10] Y.P. Huang, W.P. Chuang, Improving the museum's service by data mining and location-aware approach, Proceedings of 2004 IEEE International Conference on Systems, Man and Cybernetics, , 2004, pp. 2646–2651.

[11] Y. Jiang, J. Shang, Y. Liu, Maximizing customer satisfaction through an online recommendation system: a novel associative classi<sup>fi</sup>cation model, Decision Support Systems 48 (3) (2010) 470–479.

[12] K. Kabassi, Personalizing recommendation for tourists, Telemetric and informatics 27 (1) (2010) 51–66.

[13] W.H. Martin, S. Mason, Social trends and tourism futures, Tourism Management 8 (2) (1987) 112–114.

[14] A. Milman, The future of the theme park and attraction industry: a management perspective, Journal of Travel Research 40 (2) (2001) 139–147.

[15] M. Montaner, B. Lopez, J.L. de la Rosa, A taxonomy of recommender agents on the Internet, Arti<sup>fi</sup>cial Intelligence Review 19 (4) (2003) 285–330.

[16] E.W.T. Ngai, T.C.E. Cheng, S. Au, K.H. Lai, Mobile commerce integrated with RFID technology in a container depot, Decision Support Systems 43 (1) (2007) 62–76.

[17] A.S. Niaraki, K. Kim, Ontology based personalized route planning system using a multi-criteria decision making approach, Expert Systems with Applications 36 (2) (2009) 2250–2259.

[18] P.L. Pearce, The Ulysses Factor: Evaluating Visitors in Tourist Settings, Springer-Verlag, New York, 1988.

[19] J.J. Roh, A. Kunnathur, M. Tarafdar, Classi<sup>fi</sup>cation of RFID adoption: an expected bene<sup>fi</sup>ts approach, Information & Management 46 (6) (2009) 357–363.

[20] S. Schiaf<sup>fi</sup>no, A. Amandi, Building an expert travel agent as a software agent, Expert Systems with Applications 36 (2) (2009) 1291–1299.

[21] P.R. Thornton, A.M. Williams, G. Shaw, Revisiting time-space diaries: an exploratory case study of tourist behaviour in Cornwall, England, Environment and Planning A 29 (10) (1997) 1847–1867.

[22] C.Y. Tsai, Y.C. Shieh, A change detection method for sequential patterns, Decision Support Systems 46 (2) (2009) 501–511.

[23] C.Y. Tsai, C.C. Lo, C.W. Lin, A time-interval sequential pattern change detection method, International Journal of Information Technology and Decision Making 10 (1) (2011) 83–108.

[24] C.Y. Tsai, P.H. Lo, A sequential pattern based route suggestion system, International Journal of Innovative Computing, Information and Control 6 (10) (2010) 4389–4408.

[25] Y. Wang, N. Stash, L. Aroyo, P. Gorgels, L. Rutledged, G. Schreiberb, Recommendations based on semantically enriched museum collections, Web Semantics: Science, Services and Agents on the World Wide Web 6 (4) (2008) 283–-290

[26] W. Zhou, Y.J. Tu, S. Piramuthu, RFID-enabled item-level retail pricing, Decision Support Systems 48 (1) (2009) 169–179.

Chieh-Yuan Tsai is a professor in the Department of Industrial Engineering and Management at Yuan-Ze University, Taiwan. He received his M.S. and Ph.D. degrees in Department of Industrial and Manufacturing Systems Engineering from the University of Missouri-Columbia, U.S.A. His research activities include data mining, customer relationship management, e-commerce, and RFID applications

Shang-Hsuan Chung is an Industrial Engineer at System and Engineering Management Department of ChipMOS Technologies Corp., Taiwan. She graduated with a master degree in Department of Industrial Engineering and Management, Yuan Ze University, Taiwan. Her research interests include data mining, RFID applications, and theme park management.
