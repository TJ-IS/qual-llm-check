---
otero_id: 19590
otero_key: "6KG9TE82"
title: "Virtual friend recommendations in virtual worlds"
authors: "Hsiu-Yu Liao; Kuan-Yu Chen; Duen-Ren Liu"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.11.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Hsiu-Yu Liao, Kuan-Yu Chen, Duen-Ren Liu ⁎

Institute of Information Management, National Chiao Tung University, Hsinchu, Taiwan

## a r t i c l e i n f o

Article history: Received 6 February 2014 Received in revised form 19 September 2014 Accepted 30 November 2014 Available online 8 December 2014

Keywords: Virtual worlds Friend recommendation Support vector machine Social networks

## a b s t r a c t

Virtual worlds (VWs) are becoming effective interactive platforms in the <sup>fi</sup>elds of education, social sciences and humanities. Computing similarity among users is a technique commonly used to make friend recommendations in social networks. However, user communities in virtual worlds tend to have fewer real world linkages and more entertainment-related goals than those in social networks. The above characteristics result in an ineffective modality with respect to applying existing friend recommendation methods in virtual worlds. This study develops a virtual friend recommendation approach based on user similarity and contact strengths in virtual worlds. In the proposed approach, users' contact activities in virtual worlds are characterized into dynamic features and contact types to derive their contact strengths in communication-based, social-based, transaction-based, quest-based and relationship-based contact types. Classi<sup>fi</sup>cation approaches were developed to predict friend relationships based on user similarity and contact strengths among users. A novel friend recommendation approach is further developed herein to recommend friends as regards certain virtual worlds based on friend-classi<sup>fi</sup>ers. The evaluation uses mass data collected from an online virtual world in Taiwan, and validates the effectiveness of the proposed methodology. The experiment results show that the friend classi<sup>fi</sup>er that takes into account user similarity and contact strengths can elicit stronger prediction performance than the friend-classi<sup>fi</sup>er that considers only user similarity. Moreover, the proposed friend recommendation method outperforms the traditional friend of friend (FOF) method of friend recommendation in virtual worlds.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

A virtual world (VW) is an electronic environment which visually mimics complex physical spaces, wherein people are represented by avatars and interact with each other via virtual objects. The growing trend of playing online games with friends has encouraged the now <sup>fl</sup>ourishing VW market. Ubiquitous computing has also been instrumental in the move by families away from television to participating in virtual worlds instead [3].

Increasingly more VWs have come to correlate with social network (SN) platforms. Successful friendship recommendation techniques may increase sales for these SN companies, a notion which has fuelled a number of studies on friend recommendations in the context of SNs. However, the concept of friend recommendation in VWs remains relatively unexplored.

Friend recommendation in VWs induces users to engage in more contact activities. Stable relationships are positively associated with social presence, and this enhances user immersion in the VW. In addition, social interactions in VWs may shape purchase behaviors. User immersion increases user intention to purchase, which increases sales from advertisements for the VW providers [2].

User contacts in VWs differ signi<sup>fi</sup>cantly from user interactions in SNs in the following ways:

(1) Identity difference. Players in a VW begin as strangers to other players, while users in SNs tend to associate with their realworld friends. VW players are not identi<sup>fi</sup>ed by their demographic attributes, such as their job, education or location. An avatar represents the very personality and uniqueness of each player, regardless of appearance, rather than an identity that is linked to some real-world group in an SN. Thus, virtual worlds based on models of ownership and achievements make it possible to differentiate users and build esteem [4,16].

(2) Heterogeneous activities. In a VW, players engage in more diverse activities, such as bidding, role-play, or joining lotteries and contests hosted by VW providers, than do those in SNs. Due to the variety of complex actions available in the VW, virtual contact activities within groups offer more interesting homophilic attributes for researchers to explore. Recommendations by friends in SNs focus on analyzing the similarity of user attributes, such as mutual interests [15], time and location [30]. Models focusing on attribute similarity may be suitable for SNs, however they are not suitable for VWs. For example, avatars can swiftly move to any location in a VW, so spatial dynamics become less important for virtual interactions than they are in the real world [2]. Motivating users and keeping them continually engaged is an important challenge for those who create and manage virtual world websites [31]. Therefore, an effective recommendation method that considers contact activities will enhance the success rate of recommendations and increase the degree of user <sup>fl</sup>ow in a VW.

(3) Hedonic orientation. Participants in VWs are less informationand socially-oriented than they are game- and role play-oriented [29]. Lu and Wang have shown that perceived playfulness and descriptive norms in<sup>fl</sup>uence online game addiction [22]. As such, friendships in VWs need not be based on direct interactions. Players may complete the same quests or stay in the same community without steady communication. These kinds of contacts may deepen the impression of group players. The stability of the virtual arena increases the likelihood of regular encounters with “familiar strangers”, thus establishing connections between participants and building friendships [26]. Thus, the ways that VW users make friends differ from those in SNs. In this paper we set user contacts rather than interactions in order to broaden participants' connections in VWs.

Classi<sup>fi</sup>cation and cluster methodologies have been successfully applied in merchandise recommendation, increasing related sales. Notably, there is a trend toward friend recommendation in SNs. In recent years, increasingly more research has focused on friend recommendation for weblog platforms, such as Livejournal, Amazon and Twitter. Golder et al. structurally classi<sup>fi</sup>ed friend recommendations in SNs into four categories: reciprocity, shared interests, shared audience and <sup>fi</sup>ltered people [11]. Kwon and Kim [20] and Hsu et al. [15] combine the idea of shared interests with social context and friends of friends, respectively. Shared interests are user attributes, and present effective results. However, little research has focused on friend recommendation in VWs. This study thus proposes a friend recommendation method for VWs. According to the special attributes of VWs, this paper has the following three contributions:

(1) This paper combines user-to-user virtual contacts with user (attribute) similarities. Most existing friend recommendation methodologies have focused on user similarities. Most studies have applied user attributes such as time, location [15], graph-based algorithm [27] or the friends of friends (FoF) method. This study, however, focuses on contact strengths such as quest participants and how they spend money within the context of the platforms.

(2) This study proposes a friend recommendation methodology for a complex environment in a virtual world, in which users have heterogeneous contacts with other users. Although some studies have focused on friendship recommendation in SNs, the activities are more simple, such as reading articles or replying to a message [23,15]. The proposed model decomposes the complex virtual contacts in a VW into a set of dynamic features and categories in order to derive their contact strengths in communication-based, social-based, transaction-based, quest-based and relationshipbased contact types.

(3) The experiment conducted in this study collects user activity and pro<sup>fi</sup>le data from the online Roomi (www.roomi.com.tw) database in order to build a social network in the virtual world. The data directly depicts players' lives in the VW, rather than taking information from the players' questionnaires. The proposed model performs more effectively than other recommendation models with respect to the massive amount of data and complex circumstances. This suggests that conventional SN friend recommendation models may not perform effectively in VWs. Moreover, the experiment result shows that both user similarity and contact activities affect friend-making in VWs.

The remainder of this paper is organized as follows. Section 2 reviews related works on VWs and the theory applied in this study, including the support vector machine (SVM), information gain and the principal of homophily. Section 3 elaborates on the proposed methodology. Section 4 demonstrates the experimental steps and results. Section 5 closes with conclusions and observations.

## 2. Related work and theoretic background

The essential features of social-networking web sites are such that they provide a platform in which members can easily create pro<sup>fi</sup>les containing information about themselves, and de<sup>fi</sup>ne their trusted circle of friends [24]. A virtual world is a three-dimensional space where everyone can play as an avatar, performing a variety of activities with each other, including games. In VWs, people can engage in social activities, as in SNs; however, the characteristics of the two platforms are very different. There are increasingly more research results regarding friend recommendations in SNs, but little research has been conducted with respect to friend recommendation in VWs.

This section <sup>fi</sup>rst refers to existing friend recommendation methods in SNs, and then elaborates on recent research on VWs in order to demonstrate the lack of friend recommendation methodology in literature. It then introduces classi<sup>fi</sup>cation methods, SVM and KNN, and information gaining measures applied in the proposed model.

## 2.1. Friend recommendation in social networks

The principle of homophily is the idea that contact between similar people occurs at a higher rate than between dissimilar people. Potential new ties are heavily dependent on our existing set of ties, e.g., friends of friends, and on the organizations of which we are part, such as schools, workplaces and community groups [27]. Golder et al. [11] stated that increased internal density will help an organization build a community at the lowest expense. Three of four recommendation principals suggest friends based on common interests and tracked activities.

Some studies have utilized user interests and friends in the context of a social graph to predict friends. Kwon and Kim [20] proposed a friend recommendation method with a friendship score. The friendship score was computed using both a physical and social contexts in an SN. The physical context was represented by the similarity of user pro<sup>fi</sup>les, such as user location and time, and the social context was taken from the friend relation in the friendship graph. Hsu et al. analyzed the friendships in LiveJournal [15], and predicted friends by means of a decreasing count of mutual interests and graph features, such as inward/ outward degree of nodes and number of mutual friends. Silva et al. [27] used the data obtained from the Oro-Aro SN in Brazil, and utilized the graph topology of the SNS (social network services) to <sup>fi</sup>lter second degree FoFs of a given node.

As customer behavior prediction has become extremely common in recent years, trust relationship recommendation in SNs has begun to receive a signi<sup>fi</sup>cant amount of interest. Ma et al. [23] predicted trust relationships between two users by using user interaction features in an online user-generated review application, with interaction features based on combinations of rating score and rating numbers.

Interpersonal communications constitute an important communication media, especially for social groups not easily accessible to mass media advertising [19]. Therefore, the application of social graphs, user pro<sup>fi</sup>les and user interests to predict friendships demonstrates a major portion of existing SN research.

## 2.2. Research on virtual worlds

With the increasingly ubiquitous nature of computing, VWs are rapidly growing in popularity. Kzero Worldwide stated that the total number of registered VW accounts reached 1400 million, and the reported revenue would increase from \$3.9bn in 2011 to \$6bn by the end of 2012 [21].

Messinger et al. [24] provided a literature review of existing VW research. Bainbridge [3] puts emphasis on the research potential of online VWs. Animesh [2] states that the 3D representation of space in VWs brings users closer to the physical world. This focuses primarily on three types of virtual experience: telepresence, social presence and <sup>fl</sup>ow. Furthermore, the work shows how those dynamics affect intention to purchase virtual goods, showing how <sup>fl</sup>ow, user immersion in a VW, is positively related to intention to purchase virtual goods.

Some research has focused on user behaviors and tendencies in VWs. Animesh states that perceived stability is positively related to the sense of <sup>fl</sup>ow [2]. Hsu and Lu indicate that users tend to play online games more as their <sup>fl</sup>ow increases [14]. Frequent, repeated interactions endorse a user's relationships with other participants, and increase their feeling of stability. Utz states that similarity in interests and attitudes are the basis of virtual relationships [29]. This paper sheds some light on which dynamics in<sup>fl</sup>uence friend relationships in VWs. However, methodology related to enhancing user relationships and stability in VWs remains largely unexplored.

## 2.3. Methods applied in the proposed model

A wide range of classi<sup>fi</sup>cation methods have been used in the context of <sup>fi</sup>elds of prediction. Of all the classi<sup>fi</sup>cation methods, the support vector machine (SVM) has been most successfully applied in human resources [8], <sup>fi</sup>nancial risk predictions [5,17,28] and trust relationship predictions [23]. The k-nearest neighbors (KNN) classi<sup>fi</sup>er is a straightforward classi<sup>fi</sup>er with respect to machine learning techniques. It is easy to implement, and can be very effective if an analysis of the neighbors is useful [7]. Due to their good recommendation results, KNN classi<sup>fi</sup>cation and SVM classi<sup>fi</sup>cation methods have been applied to seeking solutions for friend prediction problems. The experiment in [1] also shows that an SVM classi<sup>fi</sup>er with information gain feature selection produces the best classi<sup>fi</sup>cation performance. This study therefore uses information gain as a feature selection method in order to reduce the input features.

## 2.3.1. Support vector machine (SVM)

SVM is a machine learning classi<sup>fi</sup>cation method for linear or nonlinear data. It uses a non-linear mapping technique to transform the original training data into a higher dimension. Data from two classes can thus always be separated by a hyperplane. SVM <sup>fi</sup>rst builds a model according to the training data and assigns new examples into either one category or the other. The machine then <sup>fi</sup>nds the optimal hyperplane by support vectors and margins. Once the maximum marginal hyperplane is derived from the training data, the trained model can be used for class predictions [13].

$$
y _ {i} (w _ {0} + w _ {1} x _ {1} + w _ {2} x _ {2}) \geq 1, \forall i a n d y _ {i} = \{1, - 1 \}\tag{1}
$$

where training tuples are $2 { \mathrm { - D } } , { \mathrm { e . g . , X } } = ( x _ { 1 } , x _ { 2 } )$ , where $x _ { 1 }$ and x<sub>2</sub> are the values of attributes $\mathsf { A } _ { 1 }$ and $\mathsf { A } _ { 2 }$ for $\mathrm { ~ X ~ } . w _ { 0 }$ is an additional weight and $w _ { 1 }$ $w _ { 2 }$ are weight vectors of each attribute. Any training tuples that fall on hyperplanes are called support vectors. The distance from the separating hyperplane is the maximum marginal:

$$
\frac {2}{| | W | |}, \text {   where   } | | W | | = \sqrt {W \times W}\tag{2}
$$

where ||W|| is the Euclidean distance. If $W = \{ w _ { 1 } , w _ { 2 } , . . . , w _ { n } \}$ , then ${ \sqrt { w \times w } } = { \sqrt { w _ { 1 } ^ { 2 } + w _ { 2 } ^ { 2 } + \ldots + w _ { n } ^ { 2 } } }$ , n is the number of attributes.

This study uses SVM to develop the proposed virtual friend prediction model. The decisive attributes applied in this model are generated by the information gain. Section 2.3.3 elaborates on how information gain works.

## 2.3.2. k-Nearest neighbors (KNN) classifier

The KNN classi<sup>fi</sup>er is a simple but effective classi<sup>fi</sup>cation method. It is a case-based learning method, which keeps all training data for classi<sup>fi</sup>cation [12]. Nearest-neighbor classi<sup>fi</sup>ers are based on learning by analogy, that is, by comparing a given test tuple with training tuples that are similar to it. The training tuples are described by n attributes. Each tuple represents a point in an n-dimensional space, and can be represented as $X _ { 1 } ~ =$ $( x _ { 1 1 } , x _ { 1 2 } , . . . , x _ { 1 n } )$ . When given an unknown tuple, $X _ { m } = ( x _ { m 1 } , x _ { m 2 } , . . . , x _ { m n } ) ,$ a k-nearest-neighbor classi<sup>fi</sup>er searches the pattern space for the k training tuples that are closest to the unknown tuple $X _ { m } .$ The KNN classi<sup>fi</sup>er is the majority vote of k-nearest neighbors. The unknown tuple is assigned the class of the training tuples. KNN classi<sup>fi</sup>ers can also be used for prediction, that is, to return a real-valued prediction for a given unknown tuple [6].

## 2.3.3. Information gain

Information gain is the value or information content of messages [13]. It is the difference between the original information requirement (i.e., based on just the proportion of classes) and the new requirement (i.e., obtained after partitioning one attribute), as stated in Eq. (3):

$$
\operatorname{Gain} (A) = \operatorname{Info} (D) - \operatorname{Info} _ {A} (D).\tag{3}
$$

Let node N represent or hold the tuples of partition D. Gain(A) represents information gain from the A attribute, which indicates how much would be gained by branching on A. Info(D) is also known as the entropy of $D . \operatorname* { I n f } { 0 } _ { A } ( D )$ is the expected information required to classify a tuple from $D ,$ based on the partitioning by A.

This study proposes a model which integrates existing homophilic friend prediction methods in social networks and infuses the user's contact dynamics to ful<sup>fi</sup>ll the special features of virtual worlds. The model is then evaluated by a data set taken from an online virtual world in order to demonstrate its feasibility.

## 3. Friend recommendation framework

## 3.1. Research objective and approach

In a SN, friendship is a relation such that two persons have a bi-directed link between them. In contrast to the interactions in SNs, VW users may have contact activities, such as talking, gift giving and diary tracking, with those who are not yet their friends in VW. This study retains the SN's definition of friendship. Computing user similarity among users has led to the solutions for friend recommendation in social networks. However, users in virtual worlds have more heterogeneous activities, and greater hedonic purpose than those in social networks. The purpose of this paper is to propose an effective friend recommendation approach suitable for virtual worlds.

In the proposed model, friendships in online VWs are built with two things in mind: user similarity and virtual contact strength with others. Users' personal online favors and behaviors, such as the level of consumption and the duration that they are active in the platform, are user attributes; interactive behaviors, such as gift giving, visits, party attendance and transaction rate, are virtual contact activities. The proposed virtual friend recommendation framework is shown in Fig. 1. The methodology is followed by three phases. The first phase calculates the user-to-user similarities. The user similarity factor involves calculating the similarity of attributes between two users. The second phase accumulates user-to-user dynamic features, such as those that are synchronized/asynchronized or directed/bi-directed, to obtain contact strengths, derived from how two users connect with respect to their contact activities. In the third phase, classi<sup>fi</sup>cation approaches, SVM friend classi<sup>fi</sup>ers and KNN friend classi<sup>fi</sup>ers, are developed to predict friend relationships based on user similarity and contact strengths between users. A novel friend recommendation approach is then furthe developed to recommend friends in virtual worlds based on the friend-classi<sup>fi</sup>ers.

![](/api/attachments/6KG9TE82/fulltext/images/f612502b5fcff8ad6e63b3a28ec55d11eb73a092d7ab08e001c9b383dd90c068.jpg)  
Fig. 1. Friend recommendation framework in virtual worlds

## 3.2. Calculating user similarity

The <sup>fi</sup>rst phase of the framework calculates user similarity among user pairs. Two main procedures take place during this phase. The <sup>fi</sup>rst step is to decide upon the important attributes which affect users' friend making decisions. The proposed method involves information gain [13]. After con structing the attributes set, the second step is to compute every user pair's similarities. The similarity degrees will later be merged with contact strengths into a classi<sup>fi</sup>er for friend recommendations.

Let $d _ { i } ( u )$ and $d _ { i } ( \nu )$ be the respective values of attribute i for user u and user v. Whether the data value of attribute i is quantitative or nonquantitative varies depending on the method of similarity computation pertaining to user u and user v.

If the value of attribute i is non-quantitative data, only when the values of user u and user v's attribute i are the same, can the similarity of user u and user v be 1, otherwise 0. If the value of the attribute is quantitative, all data values 90% above the data range are counted as 1. The data values below 90% are normalized from 1 to 0, and derive each user u and user v's attribute i values $d _ { i } ( u )$ and $d _ { i } ( \nu )$ . The similarity of quantitative attributes is related to the distance between $d _ { i } ( u )$ and $d _ { i } ( \nu )$ . If user u and user v are more similar than user x and user y in terms of the i attribute, then the dis tance between $d _ { i } ( u )$ and $d _ { i } ( \nu )$ is shorter than between $d _ { i } ( x )$ and $d _ { i } ( y )$ . The similarity can be represented as $1 - | d _ { i } ( u ) - d _ { i } ( \nu ) |$ |. Therefore, the similarity is represented by the opposite of the distance between $d _ { i } ( u )$ and $d _ { i } ( \nu )$ . Table 1 summarizes how the similarity is calculated for different types of data

Moreover, a harmonized level is applied to adjust the similarity level. Comparing two users who do not play game $( d _ { i } ( u ) = d _ { i } ( \nu ) = 0 )$ and two users who both play game i, yields their attribute i with $d _ { i } ( u ) = d _ { i } ( \nu ) = 1$ . The two pairs of similarity data points have different meanings when both equations result in $d _ { i } ( u ) = d _ { i } ( \nu ) . \operatorname { I f } d _ { i } ( u ) = d _ { i } ( \nu ) = 1$ , then user u and user v both make extra efforts to reach the highest value; however, when $d _ { i } ( u ) = d _ { i } ( \nu ) = 0$ , then user u and user v don't play the game. To harmonize the level of similarity, the weighted mean distance is applied:

$$
S _ {d i} (u, v) = \alpha \times (1 - | d _ {i} (u) - d _ {i} (v) |) + (1 - \alpha) \times [ (2 \times d _ {i} (u) \times d _ {i} (v)) / (d _ {i} (u) + d _ {i} (v)) ]\tag{4}
$$

where $0 \leq \alpha \leqq$ 1. α is the weight of distance, for example $\alpha { = } 0 . 7 ; ( 1 - \alpha )$ harmonizes the value of the attribute. $S _ { d i } ( u , \nu )$ represents user u and user v's similarity degree of attribute $i . \operatorname { I f } d _ { i } ( u ) = d _ { i } ( \nu ) = 0 ,$ , then $( 2 \times d _ { i } ( u ) \times d _ { i } ( \nu ) ) / ( d _ { i } ( u ) + d _ { i } ( \nu ) ) = 0 ,$ , and the similarity of the two values is harmonized to $\begin{array} { r } { S _ { d i } ( u , \nu ) = \alpha ; \mathrm { i f } d _ { i } ( u ) = d _ { i } ( \nu ) = 1 } \end{array}$ , then $S _ { d i } ( u , \nu ) = 1$

Information gain is applied to elect the decisive attributes in friend prediction. Different attributes have different decisive power with respect to friend prediction, This study calculates user similarities for specific attributes, and applies the information gain to calculate the importance of each attribute The attributes with the top n information gain are decisive attributes selected for building friend-classifiers and recommendation methods

Similarity expression for quantitative and non-quantitative data.

<table><tr><td></td><td> $d_{i}(u) = d_{i}(v)$ </td><td> $d_{i}(u) \neq d_{i}(v)$ </td></tr><tr><td>Similarity for quantitative data</td><td>1</td><td> $1 - |d_{i}(u) - d_{i}(v)|$ </td></tr><tr><td>Similarity for non-quantitative data</td><td>1</td><td>0</td></tr></table>

Table 2 Types of contact activities.

<table><tr><td>Contact types</td><td>Example of contact activity</td></tr><tr><td>Communication based ( $C_c$ )</td><td>Read diary, leave message, read article, reply to message, read editor&#x27;s log</td></tr><tr><td>Social-activity based ( $C_s$ )</td><td>Give a gift, feast, tell a secret, visit, leave footprints</td></tr><tr><td>Transaction based ( $C_t$ )</td><td>Economic exchanges, join bidding</td></tr><tr><td>Quest based ( $C_q$ )</td><td>Go fishing together, play collaborative games</td></tr><tr><td>Relationship based ( $C_r$ )</td><td>Work for economic income, join a family</td></tr></table>

## 3.3. Aggregate contact strengths

The second phase of the model traces user-to-user virtual contact activities and frequency during a speci<sup>fi</sup>c interval, and sums up each contact weight and frequency to gain the contact strength between the two users. Contact strength is taken to represent the closeness of the two users, and the higher the score, the closer the two users are, and vice versa.

In VWs, users can experience the world through a variety of activities, including building or buying things, engaging in quests, playing sports or living with one another. Those virtual contacts have different degrees of closeness. For example, the closeness degree of a behavior where user A cohabits with user B will differ from that of a behavior where user A reads user C's articles. Therefore, each contact activity should be characterized into types of dynamic features with a speci<sup>fi</sup>cally de<sup>fi</sup>ned weighting score to represent the degree of closeness. It is then possible to determine the contact strengths of user u and user v according to the activities' dynamic features and frequencies within a certain time period.

## 3.3.1. Analyze the dynamic features and types of contact activities

Contact activities can be classified into five categories: communication based, social-activity based, transaction based, quest based and relation ship based. Contact categorization helps in explaining kinds of friend making models for different users. Most users tend to execute communication based activities before building friendships; some tend to make friends with buyers or sellers; players who focus on game-playing will make friends with those who play collaborative games. Table 2 classi<sup>fi</sup>es the most common contact activities into <sup>fi</sup>ve contact types.

Dynamic features are a contact activity's sub-characteristics. Each dynamic feature f is given a different weight according to its respective property. The closeness weight of each virtual contact activity (vc) is composed of all its dynamic features. The following de<sup>fi</sup>nes each of the dynamic fea tures and its weighting,

1. Direction $( f _ { d } ^ { v c } ) ;$ : Whether the virtual contact is directed or bi-directed results in a different degree of closeness. If two individuals mutually attend to one another, then the bond is reinforced in each direction, and both people will <sup>fi</sup>nd the tie rewarding [9]. Therefore, a directed action is given one point, and a bi-directed contact is awarded extra weighting with three points.

2. Synchronization (f <sup>vc</sup>): If the virtual contact activity has to be synchronously executed, the feature weight is set to 1. On-line co-work and video talk are synchronized actions. If the feature weight reveals asynchronized actions, such as reading articles or replying to messages, it is set to 0.

3. Intention $( f _ { p } ^ { \nu c } )$ : Intention refers to whether the user performs the contact with a speci<sup>fi</sup>c purpose or extra cost (money or time). Gift giving is a kind of activity with the purpose of spending money, while browsing another user's blog is considered effortless activity. According to [25], relationships in which individuals give something of value lead to stronger effective ties. The contacts made with intention are given a one point feature weight, otherwise 0.

4. Continuity (f <sup>vc</sup>): When users join the same quest or talk for hours, it can be a one-time job, but last a long time. The closeness degree of this kind of activity differs from that of non-continuous actions, such as reading articles or joining bids. The feature weight of these kinds of activities is set to 1.

Table 3 summarizes the closeness weights of contact features. One contact activity can be represented by aggregating its four dynamic features to represent the closeness of the activity. The closeness weight of virtual contact vc is denoted as $m _ { v c }$ and is represented as Eq. (5):

$$
m _ {v c} = f _ {d} ^ {v c} + f _ {s} ^ {v c} + f _ {p} ^ {v c} + f _ {c} ^ {v c}, \text { where } f _ {d} ^ {v c} \in \{1, 3 \}, f _ {s} ^ {v c} \in \{1, 0 \}, f _ {p} ^ {v c} \in \{1, 0 \}, f _ {c} ^ {v c} \in \{1, 0 \}.\tag{5}
$$

Based on the above equation, the closeness weight $( m _ { \nu c } )$ of each activity category can be derived. Table 4 describes the activity closeness weight of each contact type. If user u and user v both belong to the same fan's family and attend election/discussion activities for the fan's club, these activities are relationship-based. Users get more belongingness from these activities and these activities are synchronized such that all family members should attend at the same time and continue to do so for a certain period. In this situation, the discussion in the whole group is bi-directed (multi-directed). Compared with the group discussion, the responses to user posts on a public bulletin board could be given by anyone who passes by, which makes such responses more a non-purpose coincident than synchronized or bi-directed activity. Therefore, relationship-based contact activities will have a greater activity closeness weight to represent higher closeness than will activities of other contact types.

Contact features and closeness weighting.

<table><tr><td>Dynamic features</td><td>Symbol</td><td>Closeness weight of features</td></tr><tr><td>Direction</td><td> $f_{d}^{vc}$ </td><td>Directed: 1; bi-directed: 3</td></tr><tr><td>Synchronization</td><td> $f_{s}^{vc}$ </td><td>Synchronized: 1; unsynchronized: 0</td></tr><tr><td>Intention</td><td> $f_{p}^{vc}$ </td><td>With purpose: 1; non-purpose: 0</td></tr><tr><td>Continuity</td><td> $f_{c}^{vc}$ </td><td>Continuous: 1; non-continuous: 0</td></tr></table>

Table 4  
Closeness weight of each contact type.

<table><tr><td>Contact types (ctype)</td><td>Dynamic features</td><td>Activity closeness weight</td></tr><tr><td>Communication based ( $C_c$ )</td><td> $f_{d}^{vc}=1,f_{s}^{vc}=0,f_{p}^{vc}=0,f_{c}^{vc}=0$ </td><td>1</td></tr><tr><td>Social-activity based ( $C_s$ )</td><td> $f_{d}^{vc}=1,f_{s}^{vc}=0,f_{p}^{vc}=1,f_{c}^{vc}=0$ </td><td>2</td></tr><tr><td>Transaction based ( $C_t$ )</td><td> $f_{d}^{vc}=3,f_{s}^{vc}=0,f_{p}^{vc}=0,f_{c}^{vc}=0$ </td><td>3</td></tr><tr><td>Quest based ( $C_q$ )</td><td> $f_{d}^{vc}=3,f_{s}^{vc}=1,f_{p}^{vc}=0,f_{c}^{vc}=0$ </td><td>4</td></tr><tr><td>Relationship based ( $C_r$ )</td><td> $f_{d}^{vc}=3,f_{s}^{vc}=1,f_{p}^{vc}=0,f_{c}^{vc}=1$ </td><td>5</td></tr></table>

3.3.2. Accumulate contact closeness weight and frequency in specific intervals

It is not only the closeness weight of the contact activity that represents the degree of closeness; the density of the contacts can also in<sup>fl</sup>uence a user pair's contact strength. People are usually prone to trust others with whom they are familiar through repeated contact [10]. For example, repeat edly buying goods from a speci<sup>fi</sup>c seller; the buyer and the seller could become friends because of the trust developed through repeated trade

Some contacts with continuous features are one-time events, but last a long time. The density of these contact activities should be reviewed through their duration. Therefore, the measurement of density depends on whether the contact activity is continuous or non-continuous.

Contact density is set from 0 to 1. All users' non-continuous contact activity is counted. The frequency of an activity that is over 90% for all users is counted as 1; the data value below 90% is normalized from 0 to 1. As for continuous contact activities, the duration of the same contact is compared among all users. The duration of contact that is over 90% for all users is also counted as 1; and the duration below 90% is normalized from 0 to 1.

The activity score, $A S _ { v c } ( u , v )$ , describes the closeness weighting and the density of contact activity vc between user u and user v during a speci<sup>fi</sup>c time. It is represented as Eq. (6):

$$
A S _ {v c} (u, v) = m _ {v c} (u, v) \times f r e q _ {v c} (u, v)\tag{6}
$$

where $0 \leq f r e q _ { \nu c } ( u , \nu ) \leq 1 , m _ { \nu c } ( u , \nu ) \in \{ 1 , 2 , 3 , 4 , 5 \} . A S _ { \nu c } ( u , \nu )$ is the activity score for user u's performance of the contact activity vc with user v in a certain interval; $m _ { v c } ( u , v )$ speci<sup>fi</sup>es the weight of the contact activity vc user v executes toward user v; $f r e q _ { v c } ( u , \nu )$ is the contact density or frequency with which user u performs activities with respect to user v.

The contact strength of a contact type is aggregated between user u and user v as Eq. (7):

$$
C S _ {c t y p e} (u, v) = \sum_ {v c \in Q _ {c t y p e}} A S _ {v c} (u, v)\tag{7}
$$

where $Q _ { c t y p e }$ is the set of all the contact activities belonging to type ctype, which means communication $( C _ { c } ) _  \}$ , social $( C _ { s } ) _ { \mathfrak { r } }$ , transaction $( C _ { t } ) ,$ , quest $\left( C _ { q } \right)$ and relationship-based (C ) contact types, respectively. $C S _ { c t y p e } ( u , \nu )$ is the aggregated contact strength between users u and v for a speci<sup>fi</sup>c contact type.

After computing user similarity and contact strengths, there are n user similarity degrees of decisive attributes $S _ { d i } ( u , v )$ , and <sup>fi</sup>ve contact strengths of activity types $C S _ { c t y p e } ( u , \nu )$ for each user pair. In the next phase, a two-stage approach is performed to develop the friend recommendation mech anism. The <sup>fi</sup>rst stage develops friend prediction classi<sup>fi</sup>ers to predict friend/non-friend relationships. The second stage constructs the friend recom mendation mechanism, based on contact activity, similarity and friend classi<sup>fi</sup>ers, which then recommends a list of friend candidates to a target use in the virtual world.

## 3.4. Classification-based approach to predict friend/non-friend relationships

In this phase, two classi<sup>fi</sup>ers, the SVM friend classi<sup>fi</sup>er and the KNN friend classi<sup>fi</sup>er are considered for predicting friend relationships. There are a number of available classi<sup>fi</sup>cation methods, such as decision trees, SVM, and neural networks. All of these classi<sup>fi</sup>cation methods can be adopted to build a friend classifier for predicting friend relationships. Recently, SVM has been most commonly used because of its outstanding performance: KNN is a straightforward classi<sup>fi</sup>cation method, and can also achieve good performance. A user is predicted to be the target user's friend or non friend by these friend classifiers

## 3.4.1. SVM friend classifier

The SVM friend classi<sup>fi</sup>er learns how to predict friendships by a set of training data. Given a set of training examples, each marked as belonging to either a friend or non-friend class, the SVM training algorithm builds a friend prediction model to classify unknown data into one of the two classes. The training examples include friend pairs' and non-friend pairs' similarity degrees and five contact strengths. An SVM friend classification mode represents the training examples as points in space; the examples of the two separate categories are divided by hyperplanes. New unknown exam ples are then mapped into the space and predicted to belong to either the friend or non-friend category based on which side of the hyperplane they fall on.

Let $P _ { x y } [ S _ { d i } ( u _ { x } , u _ { y } ) , C S _ { c t y p e } ( u _ { x } , u _ { y } ) ,$ , F/NF] denote user $u _ { x }$ and user ${ \boldsymbol { u _ { y } } } ^ { * } \boldsymbol { s }$ relation data. This contains n user attributes' similarity degrees, $S _ { d i } ( u _ { x } , u _ { y } )$ , and <sup>fi</sup>ve contact types' $( C _ { c } , C _ { s } , C _ { t } , C _ { q }$ and $C _ { r } )$ contact strengths $C S _ { c t y p e } ( u _ { x } , u _ { y } )$ of the pairs, and whether they are friends (F) or non-friends (NF). The training examples' relation data with similarity degrees and contact strengths are input into an SVM training algorithm to build an SVM friend classi<sup>fi</sup>er. In the prediction stage, user u and user $\nu ^ { \prime } s$ n similarity degrees $S _ { d 1 } ( u , \nu ) , S _ { d 2 } ( u , \nu ) \ldots S _ { d n } ( u , \nu )$ and <sup>fi</sup>ve contact strengths CS (u, v), CS (u, v), $C S _ { t } ( u , \nu ) , C S _ { q } ( u , \nu ) , C S _ { r } ( u , \nu )$ are input into the SVM friend classi<sup>fi</sup>er, the classi<sup>fi</sup>er returns whether the two users are friend (F) or non-friend (NF).

## 3.4.2. KNN friend classifier

The KNN friend classi<sup>fi</sup>er predicts the class of unknown data based on a majority vote. Unlike many arti<sup>fi</sup>cial classi<sup>fi</sup>ers, KNN is an instance-based lazy learner, and does not abstract information from the training data during the learning phase. The training job is postponed to the time that the classi<sup>fi</sup>cation is needed; therefore, the learning stage consists only of storing the feature vectors and class labels of the training samples. In the clas si<sup>fi</sup>cation phase, an unlabeled user–pair relation is classi<sup>fi</sup>ed by assigning the label which is most frequent among the k training samples nearest to that target user–pair relation.

The KNN friend prediction is triggered while request labeling the relationship between users u and v by input similarity degrees and contact strengths. Only at this moment does the classi<sup>fi</sup>er retrieve the training relation pairs related to the target user $r e l ( u _ { x } , u _ { y } )$ , which is represented by a vector composed from attribute similarity degrees and contact strengths between $u _ { x }$ and $u _ { y } .$ The cosine similarity algorithm is applied to <sup>fi</sup>nd knearest neighbors of relation $r e l ( u _ { x } , u _ { y } )$ . The relationship between target user–pair $u _ { x }$ and $u _ { y }$ is classi<sup>fi</sup>ed as either F or NF according to the majority vote of the user–pair's k-nearest neighbors with top k cosine similarity value. The cosine similarity value is represented as Eq. (8):

$$
\operatorname{sim} \left(\operatorname{rel} \left(u _ {x}, u _ {y}\right), \operatorname{rel} \left(u _ {w}, u _ {v}\right)\right) = \frac {\sum S _ {d _ {i}} \left(u _ {x} , u _ {y}\right) \times S _ {d _ {i}} \left(u _ {w} , u _ {v}\right) + \sum C S _ {\text { ctype }} \left(u _ {x} , u _ {y}\right) \times C S _ {\text { ctype }} \left(u _ {w} , u _ {v}\right)}{\sqrt {\sum \left(S _ {d _ {i}} \left(u _ {x} , u _ {y}\right)\right) ^ {2} + \sum \left(C S _ {\text { ctype }} \left(u _ {x} , u _ {y}\right)\right) ^ {2}} \sqrt {\sum \left(S _ {d _ {i}} \left(u _ {w} , u _ {v}\right)\right) ^ {2} + \sum \left(C S _ {\text { ctype }} \left(u _ {w} , u _ {v}\right)\right) ^ {2}}}.\tag{8}
$$

Comparing the two classi<sup>fi</sup>ers, it takes time to build the SVM friend classi<sup>fi</sup>er in the training stage, but the leading procedure helps to save time at the prediction stage. The KNN classi<sup>fi</sup>er does not build a general model in the training stage, and it searches the k-nearest neighbors during the prediction time. The algorithm thus needs to scan the training data every time the prediction is triggered. If the data set is large, or the predicted request volume is high, then the run-time performance can be very slow.

## 3.5. Develop friend recommendation mechanism

In mass virtual social worlds there are huge numbers of unknown users. The friend recommendation mechanism is used to identify possible friend candidates from a wide choice of users. This is different from predicting known user pairs' relationships. In this circumstance, the recommendation usually recommends top k candidates

## 3.5.1. Friend classifier based recommendations

The proposed method recommends virtual friends based on a hybrid of user similarity, contact strengths and an SVM classi<sup>fi</sup>er. The similarity degrees, contact strengths of training friend pairs and non-friend pairs are used to train the SVM friend classi<sup>fi</sup>er. In the recommendation stage, the trained friend classifier generates a classification result between –1 and 1, which shows the possibility that the two users are friends or non: friends. The closer the output is to 1, the more likely the two users are to be friends; if the output is closer $\mathrm { t o } - 1$ , the two users are more likely to not be friends. The trained classi<sup>fi</sup>cation recommends friends according to a descending ranking result of SVM friend classi<sup>fi</sup>ers, and can recommend top-k candidates to user u.

## 3.5.2. Friend score ranking method

The score ranking method uses factor weights to linearly combine every user pair's similarity degrees and contact strengths to obtain an aggregated friend score. It then recommends top k score candidates to target user u. A factor weight represents an attribute or a contact type's decisive power. The greater the weight, the more the factor will impact on friend decision-making. The higher the aggregated score, the more likely the two users are to be friends. The formula can be stated as Eq. (9):

$$
S R (u, v) = \sum_ {i = 1} ^ {n} s w _ {i} \times S _ {d i} (u, v) + \sum_ {v c \in Q _ {\text { ctype }}} c w _ {\text { ctype }} \times C S _ {\text { ctype }} (u, v)\tag{9}
$$

where $S R ( u , v )$ is the friend score between users u and v, which combines both user similarity and contact strengths; sw is the factor weight of sim ilarity attribute i, and $C W _ { c t y p e }$ is the factor weight of the contact strength for contact type ctype.

In this study, a performance-based weighting method is proposed to obtain every attribute and contact type's factor weights. The performancebased weighting method uses training data to obtain the performances of each attribute similarity, and each type of contact strength. Next, the performances of those decision factors are regarded as factor weights to be combined with their similarity and contact strengths. A greater weight means a more a decisive factor in predicting friends. The factor weight is derived from the ratio of the number of correctly recommended friends to the top k recommended friends, as Eq. (10):

$$
s w _ {i} = \frac {1}{N} \times \sum_ {x = 1} ^ {N} \frac {s f _ {i} (u _ {x})}{k}, c w _ {\text {   ctype   }} = \frac {1}{N} \times \sum_ {x = 1} ^ {N} \frac {c f _ {\text {   ctype   }} (u _ {x})}{k}\tag{10}
$$

where N is the number of seed users; every seed user has k recommended friends; $S f _ { i } ( u _ { x } )$ is the number of correctly recommended friends that are recommended only based on similarity attribute i for user $u _ { x } ; c f _ { c t y p e } ( u _ { x } )$ is the number of correctly recommended friends that are recommended onl based on the contact strength of contact type ctype for user $u _ { x } .$

## 3.5.3. Tuned score ranking

Both friend score ranking and tuned score ranking retrieve the weights of n attributes' similarity degrees and <sup>fi</sup>ve contact strengths from a pre-test data set, with an emphasis on a factor's importance. However, the two methods differ slightly in how they obtain weighting factors. The latter reduces the side effects of a different number of factors with respect to similarity attributes and contact categories from the former. There are <sup>fi</sup>ve <sup>fi</sup>xed contact activity categories, but the number of similarity attributes may vary according to experimental requirements in the score ranking method, which dilutes the importance of contact strength. The tuned score ranking method stresses the importance of both contact strength and user similarity; therefore, two pre-weighting adjustors are derived for the two classes of factors, as shown in Eq. (11):

$$
t s w _ {i} = s w _ {i} \times s p, t c w _ {c t y p e} = c w _ {c t y p e} \times c p\tag{11}
$$

where tsw and $t c w _ { c t y p e }$ are the tuned factor weights of similarity attribute i and ctype's contact strength, respectively. The sp is the similarity adjustor, which is the percentage of actual friends in the top k friend list recommended by the aggregated similarity degree; cp is the contact strength adjustor, which is the percentage of actual friends in the top k friend list recommended by the aggregated contact strength. The factor weights of the tuned score ranking method are adjusted by sp and cp, respectively. The tuned score ranking method uses Eq. (12) to derive friend scores.

$$
T R (u, v) = \sum_ {i = 1} ^ {n} t s w _ {i} \times S _ {d i} (u, v) + \sum_ {v c \in Q _ {c t y p e}} t c w _ {c t y p e} \times C S _ {c t y p e} (u, v).\tag{12}
$$

TR(u,v) is the tuned friend score between user u and v, which combines both user similarity and contact strengths with tuned factor weights. The higher the score, the more likely the two users are to be friends.

## 4. Experiment evaluations

The experiment was separated into two phases. In the <sup>fi</sup>rst phase, the importance of contact strengths was veri<sup>fi</sup>ed under a de<sup>fi</sup>ned testbed. Two classi<sup>fi</sup>cation techniques, KNN and SVM, were implemented. The classi<sup>fi</sup>ers were trained by the same two training data sets, one containing user attribute similarities, the other containing both user similarity and contact activities to generate four (2 training set × 2 classi<sup>fi</sup>ers) prediction agents. The work also compared the performance of KNN and SVM classi<sup>fi</sup>cations to show that SVM classi<sup>fi</sup>cation demonstrates better performance, which explains why SVM was adopted in the second phase. In the second phase, the recommendation quality of the proposed mechanism and existing friend recommendation methods are evaluated.

## 4.1. Data collection

The experiment data was extracted from an online virtual platform in Taiwan, www.roomi.com,tw, which is a popular stand-alone virtual world that also allows players to enter it from Facebook. There are over 70 million registered users; 38% of the users are in the age group ranging from senior high to university (15 to 23 years old). In this platform, users may live, shop, play games, role play and engage in social activities through their own avatars. Every activity they engage in generates numbers of dynamic attributes. The number of <sup>fi</sup>shes they own, time spent on the farm, how many photographs they own, the number of times they join in bidding, the money they spend on clothes and how many monsters they kill all contribute to the attributes of the avatars. The <sup>fi</sup>rst step is to compose the decisive attribute set from among all the attributes.

The target population was a group of users registered in Roomi for more than six months, and that have been active within three months. All of the experiment data is from the Roomi database, rather than from user questionnaires, in order to explore user behavior without personal bias. The value of each attribute is normalized from 0 to 10 in order to calculate information gain. After processing all the attribute relations of each user pair with the information gain method, those with information gain of more than 0.02 were grouped into the set of decisive attributes in Table 5.

## 4.2. Evaluation measurements

A two-phase evaluation was performed to af<sup>fi</sup>rm the proposed model as effective. The <sup>fi</sup>rst phase was to evaluate the performance of classi<sup>fi</sup>cation-based friend prediction. This predicts whether a user is a friend of a target user under a de<sup>fi</sup>ned test environment. The second phase evaluated the quality of friend recommendation. This is undertaken to recommend a list of friend candidates to a target user within a mass virtual social network. The second phase is designed to evaluate the proposed mechanism with the existing recommendation mechanisms.

In the <sup>fi</sup>rst phase, two different classi<sup>fi</sup>cation methods, SVM and KNN, were input with and without contact strengths to verify the importance of user interactions in virtual worlds. The trained classi<sup>fi</sup>ers separate user lists into friend and non-friend groups for every seed user according to the input data. In this phase, if the classi<sup>fi</sup>ers with contact strengths perform better than those without contact strengths, this suggests that the contact activities are important factors for friendmaking. Different classi<sup>fi</sup>cation methods are compared with the proposed method to achieve better accuracy with regard to a combination of a later recommendation mechanism. Therefore, the experiment in this phase compares the effectiveness of four approaches: (1) SVM-Hybrid (hybrid of user similarity and contact strength), (2) SVM-Similarity (user similarity), (3) KNN-Hybrid (hybrid of user similarity and contact strength) and (4) KNN-Similarity (user similarity). If methods (1) and (3) show better performance than methods (2) and (4), then contact strengths play an important role in VW friendmaking decisions. Here, the effectiveness of contact strengths in friendship identi<sup>fi</sup>cation is evaluated; grouping (1) with (2), and (3) with (4) into two categories helps in selecting a better classi<sup>fi</sup>er method for combination with the proposed model.

Seed users as well as their friends and non-friends are randomly selected in the <sup>fi</sup>rst phase of the experiment. The four approaches are applied to see whether they can accurately predict a user as a seed user's friend or non-friend. The friend-prediction performance of the four methods will be evaluated with precision, recall and F1 measures.

Decisive attributes set generated by information gain.

<table><tr><td></td><td>Static attributes</td><td colspan="2">Information gain</td><td>Static attributes</td><td>Information gain</td></tr><tr><td>1</td><td>Number of rooms visited</td><td>0.306</td><td>9</td><td>Money spent</td><td>0.027</td></tr><tr><td>2</td><td>Number of check-in</td><td>0.267</td><td>10</td><td>Number of votes</td><td>0.021</td></tr><tr><td>3</td><td>Number of monthly logins</td><td>0.239</td><td>11</td><td>Number of articles written</td><td>0.019</td></tr><tr><td>4</td><td>Number of friends</td><td>0.178</td><td>12</td><td>Number of promotions joined</td><td>0.017</td></tr><tr><td>5</td><td>Mico dollars spent</td><td>0.104</td><td>13</td><td>Number of short-term jobs</td><td>0.015</td></tr><tr><td>6</td><td>Number of shops visited</td><td>0.053</td><td>14</td><td>Number of photos uploaded</td><td>0.011</td></tr><tr><td>7</td><td>Number of bids</td><td>0.053</td><td>15</td><td>Time spent on farming</td><td>0.009</td></tr><tr><td>8</td><td>Time spent on fishing</td><td>0.036</td><td>16</td><td>Time spent on pasturing</td><td>0.007</td></tr></table>

Three measurement indices, recall, precision and macro averaged F1 score, are introduced in the <sup>fi</sup>rst phase of the experiment to validate the prediction quality of the proposed model. Recall index indicates the model's effectiveness in predicting real friends. The precision index represents the extent to which the model predicts friends of users, and who really are their friends. The F1 measure balances the trade-off between precision and recall. Each of the indices reaches its best value at 1.

$$
\text { recall } = \frac {\text { number   of   correctly   predicted   friend   relationships }}{\text { total   number   of   actual   friend   relationships }}
$$

$$
\text { precision } = \frac {\text { number   of   correctly   predicted   friend   relationships }}{\text { total   number   of   predicted   friend   relationships }}
$$

$$
F 1 = \frac {2 \times \text { precision } \times \text { recall }}{\text { precision } + \text { recall }}.
$$

In the second evaluation phase, the test scope was expanded to verify whether the proposed mechanism exhibits better performance than the existing recommendation methods used in social networks. Most social networks apply the Friend of Friend (FoF) method to recommend friends. However, virtual worlds have more heterogeneous activities and greater hedonic purpose than social networks. In the second phase, the proposed friend recommendation approaches: the SVM-Hybrid, friend score ranking and tuned score ranking methods are compared with the FoF method. The proposed SVM-Hybrid method recommends virtual friends based on the hybrid of user similarity, contact strengths and an SVM classi<sup>fi</sup>er. FoF is applied to verify whether the existing friend recommendation model for social networks is <sup>fi</sup>t for virtual worlds. In this phase, the precision, recall and F1 index are evaluated to compare the effectiveness among different recommendation approaches in virtual worlds.

$$
\text { precision } = \frac {\text { number   of   correctly   recommended   friends }}{\text { total   number   of   recommended   friends }}
$$

$$
\text { recall } = \frac {\text { number   of   correctly   recommended   friends }}{\text { total   number   of   actual   friends   in   Social   Network }}.
$$

## 4.3. Experiment results

The extracted data for model veri<sup>fi</sup>cation were those friendships built in June 2014 and the one-month contact activities of the pairs before building relationships. The <sup>fi</sup>rst step was to randomly select 500 seed users in the <sup>fi</sup>rst and second phase experiments, respectively. A time-based validation was used to estimate model performance. The data was separated into two parts: The 1st of June to the 20th of June as training data, and the 21st of June to the 30th of June as test data.

The SVM classi<sup>fi</sup>cation was run using the SVM light package [18]. Different kernel functions and the parameters were pre-test to reach the best performance. In both phase I and phase II evaluations, radial basis kernel function (RBF) under margin = 0.1 and gamma = 10 are applied because the best performance was reached under the above conditions.

## 4.3.1. Friend prediction evaluation

After including each seed user's friend/non-friend pairs and excluding users with at least three attribute values equal to zero, the total number of user pairs included in the experiment was 15,653. In the friend prediction evaluation, there are 3393 friend pairs and 6506 non-friend pairs in the training data set; 2515 friend pairs and 3239 non-friend pairs in the test data set.

Table 6 shows that the SVM-Hybrid outperforms the other three methods regardless of precision, recall and F1 measure. Friendclassi<sup>fi</sup>ers (predictions) considering both user similarity and contact strengths perform better than friend-classi<sup>fi</sup>ers (predictions) based only on user similarity. This con<sup>fi</sup>rms that user interactions (virtual contact activities) enhance friendship prediction in virtual worlds. The KNN classi<sup>fi</sup>er shows poorer friend prediction performance than the SVM classi<sup>fi</sup>er. Moreover, the KNN classi<sup>fi</sup>er shows poorer run-time performance than the SVM classi<sup>fi</sup>er, since the training set is large, and all the work is done at run-time for the KNN-classi<sup>fi</sup>er, while the SVM classi<sup>fi</sup>er is a learned model, which trains the classi<sup>fi</sup>er according to the training data in order to classify new data.

## 4.3.2. Friend recommendation evaluation

The phase II experiment randomly selected 500 users and all of their friends from the Roomi platform to constitute a social network in a virtual world. The average number of friends for each user was 21.1 in this experimental social network. The social network was separated into the test and training portions based on time-based validation. There are 5373 friends and 211,763 non-friends in the training data set; 5153 friends and 104,808 non-friends in the test data set. The four recommendation agents provided the top 3 and top 5 possible friend candidates for the seed participants. If one of the top k candidates already appeared in the training data, the candidate would be replaced by the 4th candidate, and so on.

Table 7 shows attribute weights, contact type weights, aggregated weights of similarity attributes and contact types for the score ranking and tuned ranking methods. The factor weight is derived from the ratio of the number of correctly recommended friends to the top k recommended friends, recommended based only on the factor (attribute or contact type). The aggregated weights of user similarity and contact strengths are the percentage of actual friends in the top k friend list recommended by the aggregated similarity degrees and aggregated contact strengths, respectively. Even if the weight is only applied in the ranking methods, it reveals a strong evidence that interactions in these virtual worlds play an important role for friend recommendation. It is noticeable that all of the three highest weights for the top 3 score ranking and tuned ranking fall in the interaction categories. Compared with the aggregated weight for similarity attributes and contact types, the latter is triple higher than the former $( 0 . 4 4 3 / 0 . 1 3 4 = 3 . 3 )$ . The social activity has the highest weight, which indicates the highest hit rate in recommending friends. It suggests that virtual world platform providers may help users build robust connections by recommending friends through judging users' gift-giving and visiting activities. The communication activity ranks the second weight, which indicates that VW providers may build connections through users' communication behaviors, such as reading a diary, reading an article or replying to a message in recommending a mutual friendship. The relationshipbased activity is the third decisive factor in the score ranking method. Relationship-based activities in virtual worlds refer to users in the same family having common interests, such as the same fan or game. These users may build deeper connections through group discussion or continuous family activities.

Table 8 shows the precision, recall and F1 performance of the four friend recommendation methods. The recall performance of all four friend recommendation methods is low because friend recommendations in virtual worlds tend to recommend very few friends every

## Table 6

Experiment results of friend prediction approaches.

<table><tr><td>Classifier</td><td>Precision</td><td>Recall</td><td>F1</td></tr><tr><td>SVM-Hybrid</td><td>76.03%</td><td>80.48%</td><td>78.19%</td></tr><tr><td>SVM-Similarity</td><td>59.34%</td><td>61.51%</td><td>60.41%</td></tr><tr><td>KNN-Hybrid</td><td>67.63%</td><td>43.62%</td><td>53.03%</td></tr><tr><td>KNN-Similarity</td><td>62.64%</td><td>44.14%</td><td>51.78%</td></tr></table>

Table 7  
Attribute weights and contact weights of score ranking and tuned ranking methods.

<table><tr><td>Factors</td><td></td><td colspan="2">Weights for score ranking</td><td colspan="2">Weights for tuned ranking</td></tr><tr><td>Similarity attributes &amp; contact types</td><td></td><td>Top 3</td><td>Top 5</td><td>Top 3</td><td>Top 5</td></tr><tr><td>Number of monthly logins</td><td>s1</td><td>0.14</td><td>0.14</td><td>0.02</td><td>0.02</td></tr><tr><td>Number of check-in</td><td>s2</td><td>0.04</td><td>0.04</td><td>0.01</td><td>0.00</td></tr><tr><td>Time spent on fishing</td><td>s3</td><td>0.15</td><td>0.14</td><td>0.02</td><td>0.02</td></tr><tr><td>Money spent</td><td>s4</td><td>0.18</td><td>0.18</td><td>0.02</td><td>0.02</td></tr><tr><td>Mico dollars spent</td><td>s5</td><td>0.15</td><td>0.15</td><td>0.02</td><td>0.02</td></tr><tr><td>Number of check-in</td><td>s6</td><td>0.18</td><td>0.17</td><td>0.02</td><td>0.02</td></tr><tr><td>Number of rooms visited</td><td>s7</td><td>0.17</td><td>0.18</td><td>0.02</td><td>0.02</td></tr><tr><td>Number of shops visited</td><td>s8</td><td>0.10</td><td>0.09</td><td>0.01</td><td>0.01</td></tr><tr><td>Number of votes</td><td>s9</td><td>0.14</td><td>0.14</td><td>0.02</td><td>0.02</td></tr><tr><td>Number of bids</td><td>s10</td><td>0.08</td><td>0.07</td><td>0.01</td><td>0.01</td></tr><tr><td>Aggregate weight of similarity attributes</td><td></td><td>0.134</td><td>0.131</td><td></td><td></td></tr><tr><td>Communication-based</td><td>i1</td><td>0.60</td><td>0.51</td><td>0.27</td><td>0.19</td></tr><tr><td>Social activity-based</td><td>i2</td><td>0.73</td><td>0.65</td><td>0.32</td><td>0.25</td></tr><tr><td>Quest-based</td><td>i3</td><td>0.17</td><td>0.14</td><td>0.08</td><td>0.05</td></tr><tr><td>Relationship-based</td><td>i4</td><td>0.57</td><td>0.52</td><td>0.25</td><td>0.20</td></tr><tr><td>Transaction-based</td><td>i5</td><td>0.14</td><td>0.11</td><td>0.06</td><td>0.04</td></tr><tr><td>Aggregate weight of contact types</td><td></td><td>0.443</td><td>0.385</td><td></td><td></td></tr></table>

time under least user interference. The recall of top 5 friend recommendation is better than that of the top 3 recommendation because more candidates are recommended. Even the three measurements are different in numbers, but all demonstrate the same performance distribution. The SVM-Hybrid method performs the best of the four, while the tuned score ranking method performs better than the friend score ranking method. Surprisingly, the FOF method applied in most social networks shows poor performance. The users in the latter tend to contact users they are friends with in real life, while VW friendships are not built on friendships in the real world. This also corresponds to the claim that avatars tend to contact others before making friends. In a VW, there are more heterogeneous activities, such as attending a social party, roleplaying or joining lotteries than there are in SNs. Thus a friend recommendation model considering contact activities will enhance the successful recommendation rate in VWs.

SVM-Hybrid, score ranking and tuned ranking all take contact activities into account and show similar performance. The difference therefore only becomes evident when their calculation methods are examined. The SVM classifier has better performance than the two scoring methods under the same conditions; however, the score ranking method provides VW developers with a picture of what attributes are important to players. The result suggests that the SVM-Hybrid model is more suitable for recommending friend candidates in virtual worlds.

## 5. Conclusion and future research

## 5.1. Discussion

The virtual world is becoming increasingly more important to today's generation. This paper proposes a novel friend recommendation model, namely a hybrid SVM classi<sup>fi</sup>er considering user similarity and virtual contact strengths. In the proposed approach, users' contact activities in virtual worlds are characterized into dynamic features and

## Table 8

Performance of different approaches for top 3 and top 5 recommendations.

<table><tr><td></td><td>Top k</td><td>Precision</td><td>Recall</td><td>F1</td></tr><tr><td rowspan="2">SVM-Hybrid</td><td>Top 3</td><td>75.9%</td><td>22.1%</td><td>34.2%</td></tr><tr><td>Top 5</td><td>68.4%</td><td>33.2%</td><td>44.7%</td></tr><tr><td rowspan="2">Tuned Ranking</td><td>Top 3</td><td>72.6%</td><td>21.1%</td><td>32.7%</td></tr><tr><td>Top 5</td><td>64.0%</td><td>31.1%</td><td>41.8%</td></tr><tr><td rowspan="2">Score Ranking</td><td>Top 3</td><td>70.1%</td><td>20.4%</td><td>31.6%</td></tr><tr><td>Top 5</td><td>61.0%</td><td>29.6%</td><td>39.9%</td></tr><tr><td rowspan="2">FOF</td><td>Top 3</td><td>28.7%</td><td>8.4%</td><td>13.0%</td></tr><tr><td>Top 5</td><td>26.1%</td><td>12.7%</td><td>17.0%</td></tr></table>

contact types in order to derive their contact strengths. Classi<sup>fi</sup>cation approaches, the SVM friend classi<sup>fi</sup>er and the KNN friend classi<sup>fi</sup>er are developed to predict friend relationships based on user similarity and contact strengths among users.

In the evaluation phase, it was found that diverse activities in VWs make social-based activities and communication-based activities important factors in friend-making. Moreover, the proposed SVM-Hybrid, friend score and tuned score ranking methods outperform the conventional FOF method. The result demonstrates that the FOF method's good <sup>fi</sup>t for social networks may not be suitable for virtual worlds. There has been a fruitful research focus on the mediations of virtual goods; however, there are few studies on friend recommendations in virtual worlds and the methods regarding how to recommend friends. In this paper, the proposed model can be applied in virtual worlds to increase the network density while user volume remains the same. Notably, user immersion will be enhanced as a consequence, and the connection power of these networks takes users into a more diverse and interesting consumption future. Therefore, the concept of friend recommendations underpins new possibilities in the virtual worlds.

## 5.2. Limitation and future works

The experiment was conducted using data taken from Roomi in Taiwan. The attributes and the interaction activities are constrained within this scope; therefore, we cannot fully generalize our <sup>fi</sup>ndings to other virtual worlds, which may differ in terms of volume, sociodemographics and culture.

In the proposed model, friends are predicted according to their previous behaviors and similarity with others in the VW. Users may have more activities in one kind of activity category. In this paper, we classi-<sup>fi</sup>ed activities into <sup>fi</sup>ve contact types; how different types of users immerse themselves in VWs is of future interest. We may cluster users by their contact activities and observe different types of users' communication behaviors. Different user clusters may have different ways of living and different purchase behaviors in a VW. Recommending the right virtual commodities to different types of users will help platform providers gain real pro<sup>fi</sup>t and retain players on the platform. Categorizing types of avatars is also a starting point for new research possibilities.

## Acknowledgment

This research was supported by the National Science Council of Taiwan under Grant No. 102-2410-H-009-050-MY3.

## References

[1] A.S. Abrahams, J. Jiao, W. Fan, G.A. Wang, Z. Zhang, What's buzzing in the blizzard of buzz? Automotive component isolation in social media postings, Decision Support Systems 55 (4) (2013) 871–882.

[2] A. Animesh, A. Pinsonneault, S.-B. Yang, W. Oh, An odyssey into virtual worlds: exploring the impacts of technological and spatial environments on intention to pur chase virtual products, MIS Quarterly 35 (3) (2011) 25.

[3] W.S. Bainbridge, The scienti<sup>fi</sup>c research potential of virtual worlds, Science 317 (5837) (2007) 472–476.

[4] S.J. Barnes, A.D. Pressey, Who needs cyberspace? Examining drivers of needs in Second Life, Internet Research 21 (3) (2011) 236–254

[5] T. Bellotti, J. Crook, Support vector machines for credit scoring and discovery of signi<sup>fi</sup>cant features, Expert Systems with Applications 36 (2, Part 2) (2009) 3302–3308.

[6] M.-S. Chen, J.-W. Han, P.S. Yu, Data mining: an overview from a database perspective, IEEE Transactions on Knowledge and Data Engineering 8 (6) (1996) 377–378.

[7] P. Cunningham, S.J. Delany, k-Nearest neighbour classi<sup>fi</sup>ers, Multiple Classi<sup>fi</sup>er Systems, Dublin Institute of Technology Technical Report UCD-CSI-2007-4, 2007, pp. 1–17.

[8] D. Delgado-Gómez, D. Aguado, J. Lopez-Castroman, C. Santacruz, A. Artés-Rodriguez, Improving sale performance prediction using support vector machines, Expert Systems with Applications 38 (5) (2011) 5129–5132

[9] R.M. Emerson, Exchange theory, part I and II, Sociological Theories in Progress, 2, 1972, pp. 58–87.

[10] D. Gefen, E. Karahanna, D.W. Straub, Trust and TAM in online shopping: an integrated model, MIS Quarterly 27 (1) (2003) 51–90.

[11] S.A. Golder, S. Yardi, A. Marwick, A structural approach to contact recommendations in online social networks, Workshop on Search in Social Media at ACM SIGIR Conference on Information Retrieval, ACM, Boston, 2009.

[12] G. Guo, H. Wang, D. Bell, Y. Bi, K. Greer, KNN model-based approach in classi<sup>fi</sup>cation, in: R. Meersman, Z. Tari, D. Schmidt (Eds.), On The Move to Meaningful Internet Systems 2003: CoopIS, DOA, and ODBASE, Springer, Berlin Heidelberg, 2003, pp. 986–996.

[13] J. Han, M. Kamber, J. Pei, Data Mining: Concepts and Techniques, Morgan Kaufmann, 2006.

[14] C.-L. Hsu, H.-P. Lu, Why do people play on-line games? An extended TAM with social in<sup>fl</sup>uences and <sup>fl</sup>ow experience, Information Management 41 (7) (2004) 853–868.

[15] W.H. Hsu, A. King, M. Paradesi, T. Pydimarri, T. Weninger, Collaborative and structural recommendation of friends using weblog-based social network analysis, AAAI Spring Symposium on Computational Approaches to Analysing Weblogs AAAI Press, Menlo Park, California, 2006, pp., 55-60.

[16] E. Huang, Online experiences and virtual goods purchase intention, Internet Research 22 (3) (2012) 252–274.

[17] Z. Huang, H. Chen, C.-J. Hsu, W.-H. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[18] T. Joachims, A probabilistic analysis of the Rocchio algorithm with TFIDF for text categorization, in: D. Fisher (Ed.), Proceedings of 14th International Conference on Machine Learning (ICML), Morgan Kaufmann Publishers, San Francisco, US, 1997, pp. 143–151.

[19] L. Kuandykov, M. Sokolov, Impact of social neighborhood on diffusion of innovation S-curve, Decision Support Systems 48 (4) (2010) 531–535.

[20] J. Kwon, S. Kim, Friend recommendation method using physical and social context, International Journal of Computer Science and Network Security 10 (11) (2010) 116.

[21] KZeroWorldwide, Virtual worlds: industry & user data, Universe Chart for Q4 2011, KZero Worldwide, 2011.

[22] H.-P. Lu, S.-m. Wang, The role of internet addiction in online game loyalty: an exploratory study, Internet Research 18 (5) (2008) 499–519.

[23] N. Ma, E.-P. Lim, V.-A. Nguyen, A. Sun, H. Liu, Trust relationship prediction using online product review data, Proceedings of the 1st ACM International Workshop on Complex Networks Meet Information & Knowledge Management, ACM, 2009, pp. 47–54.

[24] P.R. Messinger, E. Stroulia, K. Lyons, M. Bone, R.H. Niu, K. Smirnov, S. Perelgut, Virtual worlds—past, present, and future: new directions in social computing, Decision Support Systems 47 (3) (2009) 204–228.

[25] L.D. Molm, Theoretical comparisons of forms of exchange, Sociological Theory 21 (1) (2003) 1–17.

[26] E. Paulos, E. Goodman, The familiar stranger: anxiety, comfort, and play in public places, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, Vienna, Austria, 2004.

[27] N.B. Silva, I.-R. Tsang, G.D.C. Cavalcanti, I.-J. Tsang, A graph-based friend recommendation system using genetic algorithm, Proceedings of the 2010 IEEE Congress on Evolutionary Computation (CEC), IEEE, Barcelona, 2010, pp. 1–7.

[28] J. Sun, H. Li, Financial distress prediction using support vector machines: ensemble vs. individual, Applied Soft Computing 12 (8) (2012) 2254–2265.

[29] S. Utz, Social information processing in MUDs: the development of friendships in virtual worlds, Journal of Online Behavior 1 (1) (2000) 1–25.

[30] X. Xie, Potential friend recommendation in online social network, Proceedings of the 2010 IEEE/ACM Int'l Conference on Green Computing and Communications & Int'l Conference on Cyber, Physical and Social Computing, IEEE Computer Society, 2010, pp. 831–835.

[31] N.-C. Yeh, J.C.-C. Lin, H.-P. Lu, The moderating effect of social roles on user behaviour in virtual worlds, Online Information Review 35 (5) (2011) 747–769.

Hsiu-Yu Liao is a PhD student of the Institute of Information Management at the National Chiao Tung University of Taiwan. She received the MS degree in Information Management from the National Chiao Tung University. Her research interests include information systems, electronic commerce, and recommender systems.

Kuan-YuChen is a PhD student of the Institute ofInformation Management at the National Chiao Tung University of Taiwan. His research interests include virtual worlds, Web applications, and recommender systems.

Dr. Duen-Ren Liu is a professor of the Institute of Information Management at the Nation al Chiao Tung University of Taiwan. He received the BS and MS degrees in Computer Science from the National Taiwan University and his PhD in Computer Science from the University of Minnesota. His research interests include data mining, data and knowledge engineering, electronic commerce and recommender systems.
