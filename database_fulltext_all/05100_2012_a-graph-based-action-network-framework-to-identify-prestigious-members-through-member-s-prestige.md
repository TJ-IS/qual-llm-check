---
otero_id: 5100
otero_key: "VS7WB3U2"
title: "A graph-based action network framework to identify prestigious members through member's prestige evolution"
authors: "Dongyuan Lu; Qiudan Li; Stephen Shaoyi Liao"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.12.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A graph-based action network framework to identify prestigious members through member's prestige evolution

Dongyuan Lu <sup>a</sup>, Qiudan Li <sup>a,</sup>⁎, Stephen Shaoyi Liao b

<sup>a</sup> Institute of Automation, Chinese Academy of Sciences, China

<sup>b</sup> City University of Hong Kong, Hong Kong

## a r t i c l e i n f o

Article history: Received 30 November 2010 Received in revised form 1 November 2011 Accepted 19 December 2011 Available online 3 January 2012

Keywords: Favor action network framework Prestigious members prediction Communication behaviour Structural properties investigation Potential favor behaviour analysis

## a b s t r a c t

Prestigious members on social networking websites are attracting increasing attentions from peers and corporations. People are used to consulting prestigious members for useful information and corporations are seeking opportunities to leverage them for “word of mouth” advertising. Identi<sup>fi</sup>cation and recognition of these prestigious members have been a crucial issue. Besides, the dynamic nature of members' behaviour determines the evolving nature of members' prestige. With the evolution of members' behaviour, currently prestigious members may be substituted by others who are not prestigious at present. The prediction of members' prestige evolution will help discover potential prestigious members, which will then help both people and corporations move to secure their long-term interests. However, little work has been done in relation to prediction of prestigious members. This paper aims to <sup>fi</sup>ll this gap specially using Flickr groups as a testbed. By investigating social actions among members, a graph-based action network framework to predict evolution of prestigious members has been proposed. Based on the social structural theory, which points out the interactive effect between social structure and users' actions, a favor action network that captures the social actions of choosing favourite photos of members is constructed. According to the network theory, properties of the nodes in the favor action network are investigated to identify currently prestigious members, and structural properties underlying the favor action network are mined to analyze the communication behaviour of members in a group. Further, the sociological theory inspires four key factors that affect members favor action intentions, which are homophily, triadic interaction rule, continuity and recency. Based on the above analysis, a hybrid algorithm taking all these four factors into account is proposed to predict members prestige evolution. Finally, several comprehensive and systematic analyses are designed and conducted to evaluate each of the functional components of the proposed framework. Results of evaluation on a realworld dataset validate its performance.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

With the emergence and growing popularity of online social networking, people are becoming used to seeking information from peers with high online status [18,34]. Meanwhile, corporations are also seeking opportunities to leverage in<sup>fl</sup>uential people for “word of mouth” advertising. Identi<sup>fi</sup>cation or recognition of prestigious members in a community thus has become a crucial issue across various domains or platforms. Particularly on social networking websites, members perform various social actions re<sup>fl</sup>ecting their attitude on other members, such as contacting, commenting and marking favourites. Based on social network theory, these actions performed can build social links among members and can be recorded using a graph. A directed link pointing from member a to b is regarded as member a holding a positive attitude on member b. Intuitively, several factors co-affect member prestige and should be taken into consideration simultaneously. For example, a member receiving more “links” from others should be highly prestigious and a member receiving a link from an in<sup>fl</sup>uential member may be more prestigious than a member who receiving a link from a beginner, etc. Therefore, a method of identi<sup>fi</sup>cation of member prestige is needed. After detecting the prestigious members, people can consult their opinion as well as product quality identi<sup>fi</sup>cation [12,36]. In addition, corporations can target prestigious members with advertising campaigns as their prestige causes their comments to have a greater in<sup>fl</sup>uence on people's choice [17]. Moreover, it is very unlikely, if not impossible, that the prestige of a member remains unchanged over a long period due to the dynamic nature of social networking. In general, people and corporations are not only interested in whether a member is currently prestigious, but also whether he will be prestigious in the near future. For instance, advertising targeted at potentially prestigious members would help corporations serve their longer term interests. Therefore, predicting the evolution of prestige of a member is an interesting topic and it is an essential component of identifying prestigious members. Devising an effective prediction method is the main objective of this study.

In order to quantify users' prestige at a given point of time, several methods have been proposed. Weng et al. [42] extended PageRank to measure the in<sup>fl</sup>uence of users in Twitter, which incorporates topical similarity and link structure of users. Goyal et al. [9] used the in<sup>fl</sup>uence model to detect leaders through maximizing the spread of in<sup>fl</sup>uence. Bodendorf et al. [1] examined three key indicators of “centrality” in social network analysis (SNA) to detect leaders from various perspectives. All these methods focus on investigating a snap-shot of the social network for detecting currently prestigious members. Aiming to identify prestigious members through members' prestige evolution, a framework which can capture and predict the evolution of members' actions is needed.

In this paper, we specially use Flickr.com,<sup>1</sup> one of the most popular social networking and photo-sharing websites, as our testbed. As photos would be largely re<sup>fl</sup>ective of the quality of cameras if without regard to the bias from photographic skill, Flickr provides a new exhibition platform for camera business [37]. A group in Flickr is a user-organized community [26,31,44], which is usually focused on a particular subject. There is a special category of groups focusing on identi<sup>fi</sup>cation of high quality photography, i.e. quality indicator groups [31]. Members in these groups are interested in pursuing high photo-taking quality instead of the photo content. From this perspective, prestigious members are those with high photography skills, and people tend to attribute the good quality of their photos to a particular brand or model of camera. At the same time, corporations can target these prestigious members with advertising new camera products. Without exception, prestige of members in quality indicator groups also varies with time due to the dynamic nature of people's behaviour. Therefore, identifying and predicting prestigious members on Flickr seem to be of interest.

On Flickr.com, social actions consist of building contacts, joining groups interested, commenting on photos, tagging photos and marking favourite photos, etc. [27]. Marking favourite photos is the main action we are concerned with in this study, which largely re<sup>fl</sup>ects the photography skill of a particular member, i.e. a member is regarded as skilful if several of his/her photos are chosen as favourites by other members. This data is with time-stamp and can be recorded to construct a relationship between a pair of members. We refer to the action of member a, choosing a favourite photo from member b, as a favor action pointing from a to b; a is regarded as a fan of b. The interactive favor actions among members thus construct a favor action network, where the nodes in the network denote the members and the links denote the favor actions. It is worthy to mention that the “action network” proposed is not speci<sup>fi</sup>c to Flickr.com. It also can be easily extended to other similar social actions performed on other websites. For example, trusting action on e-commerce sites and positive voting action on review sites both can be used to construct action networks. In this paper, we specially refer to the action network as favor action network for disambiguation.

The social structural theory has indicated that the social structure of a favor action network is more in<sup>fl</sup>uential to predict certain actions than the attributes of individual members involved [2]. On one hand, an evolving social structure affects social actions of a member through its effects on the member's interests. On the other hand, the dynamic actions can also potentially modify the social structure [2]. From this perspective, a graph-based favor action network framework is proposed to capture the interactive effect between the social structure and member's interests, which is re<sup>fl</sup>ected by social actions [4], to predict member's prestige evolution. Based on the favor action network, three factors will affect a member's prestige; favor volume, favor coverage and favor timeliness. Favor volume denotes the number of photos of a speci<sup>fi</sup>c member that are chosen as favourites by others. Favor coverage stands for the number of fans of a speci<sup>fi</sup>c member. Favor timeliness is re<sup>fl</sup>ected by the time-sensitive favor actions a member receives. These three factors codetermine a member's prestige and a member with higher volume, larger coverage and receiving more recent favor actions is intuitively more prestigious.

Based on the social structural theory, the proposed framework consists of four functional components. The structural property investigation component based on social network analysis theory examines the communication behaviour of the members. Three of the structural measures in social network analysis, namely, degree distribution, indegree– outdegree correlation and assortative mixing pattern are investigated. In the potential favor behavior analysis component, four key factors (homophily, triadic interaction rule, continuity and recency) are proposed, based on the sociological theory. The prestige calculation component quanti<sup>fi</sup>es the score of prestige to detect currently prestigious members. Finally, in the prestige prediction component, a hybrid algorithm taking the proposed four key factors into consideration is proposed to predict members' prestige evolution. The proposed framework is able to capture the interactive effect between favor action network structure and members' favor actions. The constructed favor action network re<sup>fl</sup>ects the dynamic communication behaviour of members. According to the theory, the favor action network structure indicates the potential favor action intentions of members, which provides the theoretical support to further functions design. From this perspective, an in-depth investigation of structural properties based on the network theory can mine communication behaviour of members. And four key factors inspired by sociological theory can analyse members' potential favor action intentions. Further, based on the above analysis, prestige calculation and prediction can quantify the evolution of members' prestige, which can be used to identify prestigious members. Several comprehensive and systematic analyses are conducted to evaluate each component of the proposed framework. Results of an evaluation performed on a real-world dataset veri<sup>fi</sup>es its validity in that favor action intentions of members implicitly recorded in the structure of favor action network can be mined to successfully predict members' prestige evolution. As aforementioned, since prestigious members play an important role on sites, the proposed framework will provide an interesting implication in future applications design, such as identi-<sup>fi</sup>cation and recommendation of key members that can be targeted by corporations for advertisement.

We begin the paper with a discussion of related work in the areas of opinion leader detection and evolution of social networks in Section 2. Then the proposed framework is described in Section 3. Section 4 describes the empirical work and reports evaluation results. Finally, some discussions and recommendations for future work are made while concluding the paper.

## 2. Related work

There has been a rich mass of literature related to employing social in<sup>fl</sup>uence within social networking websites for the viral marketing purpose. Existing works principally talk about three aspects, which include the mechanism of social contagion among customers, the reason of disproportionate in<sup>fl</sup>uence of some customers' opinions, and the identi<sup>fi</sup>cation of in<sup>fl</sup>uential people [12]. This work focuses on the third aspect and adopts a dynamic view of prestige. From this perspective, this section reviews the studies related to opinion leader detection and evolution of social networks.

## 2.1. Opinion leader identification

Opinion leaders are usually novel information contributors and have signi<sup>fi</sup>cant in<sup>fl</sup>uence on opinions of others [38]. Identifying opinion leaders has been an active research <sup>fi</sup>eld in many areas such as blogosphere [14,38], forums [1] and latest popular micro-blogs [42]. A related active line in this <sup>fi</sup>eld is to measure individual positions in social graphs such as Email networks [16], academic social networks [24], discussion groups [41] and online sharing social networks [9]. Specially, some studies are interested in a particular problem with a marketing motivation [18,20], namely, <sup>fi</sup>nding in<sup>fl</sup>uential customers for word-of-mouth advertising. Our work has a similar purpose.

According to various objectives, PageRank, information diffusion model and social network analysis are the three fundamental methods most widely used. For instance, Weng et al. [42] proposed an extension of PageRank, named TwitterRank, to measure the in<sup>fl</sup>uence of users of Twitter. They took both topical similarity and link structure of users into account. Goyal et al. [9] considered alternative de<sup>fi</sup>nitions of leader based on the way in<sup>fl</sup>uence propagates. They also developed an approach to identify leaders on the basis of maximum spread of in<sup>fl</sup>uence. Bodendorf et al. [1] proposed a novel approach to identifying opinion leaders in forums based on text mining and social network analysis (SNA). Three key indicators of “centrality” in SNA, namely, degree centrality, closeness centrality and betweenness centrality, are examined for identifying leaders from various perspectives. The authors further exploited the correlation between overall opinion trend and opinions of the leaders. We explore similar indicators in SNA to quantify members' prestige. The factors of volume and coverage are extended from the indicator “indegree” to capture various characteristics of members. In addition, we also use several measures in SNA to investigate potentially structural properties of the favor action network. These measures facilitate an in-depth analysis of communication behaviours of members. The crucial difference between our work and the above-mentioned studies is that we focus on not only detecting currently important individuals but also attempt to predict members' prestige evolution in the near future. Instead of constructing and analyzing a static snap-shot of a social network, we aim to investigate the evolution of prestige based on a sequence of snapshots of a network over a given time horizon. Therefore, some related studies on investigating evolving networks are reviewed. Especially, focus is placed on those concerning predictors relevant to our study.

## 2.2. Evolution of social network

“A dynamic network is a special type of network that consists of connected transactions that have repeated evolving interaction [25]”. There has been a large body of work on exploring evolving online social networks [19,22]. For instance, Kumar et al. [19] analyzed temporal dynamics of structures of social networks on Flickr and Yahoo! 360 and postulated an evolving graph model for social network analysis. Together with investigating the evolving nature of the social network, some studies focus on identifying in<sup>fl</sup>uential people in a dynamic environment [8,21,23]. For example, in a recent work, Lee et al. [21] took into consideration the temporal order of information adoption when detecting information spreaders in Twitter. By analyzing the information diffusion patterns, the authors proposed a measure of in<sup>fl</sup>uence based on effective readers. Ghosh and Lerman [8] argued that the detection of in<sup>fl</sup>uencers not only depended on the relationship among people, but also on the dynamic processes they implicitly emulated. Based on an empirical de<sup>fi</sup>nition of in<sup>fl</sup>uence, they compared several topological ranking measures and found acentrality metric to be stand-out. In these studies, although potential dynamics are considered, most of them still focused on <sup>fi</sup>nding current in<sup>fl</sup>uencers. While, our work aims to detect the will-be prestigious members through their prestige evolution. It is largely probable that some of the potentially prestigious members detected in our method may not be prestigious at present, and thus could not be detected by the above methods.

In many contexts, studies are devoted to exploiting temporal information for node attributes [35] or links [33] prediction. Sharan et al. [35] proposed an initial approach for improving node attribute prediction by exploiting information of dynamic relationships between entities. They incorporated time-varying links in rational statistical models based on the assumption that recent links confer more homophily than links in the distant past. The evaluations demonstrate the ef<sup>fi</sup>ciency of incorporating temporal-relational information in rational statistical models. The key difference between their study and this work is that they focused on node attribute prediction while we emphasize favor action prediction, i.e. link prediction. Nevertheless, their work inspires us to emphasize the signi<sup>fi</sup>cance of recency of favor actions in predicting evolution of prestigious members. Potgieter et al. [33] proposed a link prediction approach through topological analysis which computes various local metrics of users. Our study borrows their ideas by incorporating two static graph link prediction methods for predicting favor actions. In the context of our study, since Flickr group is treated as an entire network, members' dynamic interactions affect the entire social network structure, which in return affects the members' favor action intentions. Analysis of members' local metrics would ignore the entire structure of the favor action network. From this perspective, we propose a theoretical framework which analyzes structural properties and members' potential behaviours, and thus provides theoretical support to further prediction algorithm design. In addition, the substantially different objectives inherently distinguish our study from their work.

## 3. A framework for predicting evolution of member prestige

## 3.1. Theoretical background

Social network researchers have pointed out that the social structure of a social network is more indicative of certain actions of users than the attributes of individuals involved [2,7]. On one hand, the dynamic nature of social structure affects social actions of a user through its effects on the user's interests. On the other hand, evolution of users' interest as re<sup>fl</sup>ected by dynamic social actions can potentially modify the social structure itself [2]. Therefore, the social network structure is a good indicator for predicting potential actions of users. In the context of our study, a quality indicator group can be treated as a social network in which members perform social actions to keep relationships with each other. For identifying prestigious members who possess expert photography skills, the social action of choosing favourite photos, referred as a favor action, is considered. To capture the interactive effect between the structure of the group and members' favor actions, a favor action network needs to be constructed [7]. According to the network theory, members in the network can be regarded as nodes and relationships among members can be regarded as edges between nodes and the weight of an edge is regarded as the weight of the relationship. From this perspective, a graph-based action network framework is proposed. Construction of a favor action network is illustrated in Fig. 1. In Flickr groups, members upload personal photos denoted by links between the right member set and the photo set. On the other hand, members also endorse others by choosing their photos as favourites, denoted by links between the left member set and the photo set. The two member sets comprise the same members of the group. Through the photo set, indirect links among members can be built, which are referred as favor actions. Using the nodes in the member set and the indirect links among them, a favor action network is constructed. Over a <sup>fi</sup>xed time interval, the favor action network can be represented as a directed weighted graph $G = ( V , E , W )$ . The node set V denotes the member set. A favor action relationship pointing from member to member is established when membe $\boldsymbol { \mathrm { r } } _ { 1 }$ favors a photo of membe $\Gamma _ { 2 } ,$ denoted by a directed edge $( u , v ) \in E .$ The weight set W: $E \to \Nu$ is a function that labels each edge with a weight indicating the frequency of edge (u, v) during the given time interval. To capture the characteristics of long-term evolution of the favor action network, the time interval is divided into a series of sub-intervals. For each sub-interval, graph $G _ { t }$ denoting sub-interval t is created; a discrete-graph series representation $G = \{ G _ { 1 } G _ { 2 } . . . G _ { T } \}$ is adopted to model the evolving network, where members remain constant but edge set $E _ { T }$ and weight set $W _ { T }$ vary over time.

![](/api/attachments/VS7WB3U2/fulltext/images/6297dea490191cf1aeb3520c53db55577dfe3e0e3ed6064db282ac5dc20e6e80.jpg)  
Fig. 1. Construction of favor action network.

Characteristics of members' prestige are re<sup>fl</sup>ected by multiple factors. In our scenario, three factors are of signi<sup>fi</sup>cance to determine the value of members' prestige: favor volume, favor coverage and favor timeliness. Favor volume is re<sup>fl</sup>ected by the number of photos of a member chosen as favourites. It is regarded as an initial measure of a member's in<sup>fl</sup>uence. Favor coverage represents how widely a member is endorsed. It is not only re<sup>fl</sup>ected by the number of fans of a member, but also takes into consideration the initial in<sup>fl</sup>uential degree of these fans. As well as complementing favor volume to avoid the bias induced by loyal fans who favor many photos of a particular member, the factor weights more heavily towards the members who have more high-in<sup>fl</sup>uential fans. Favor timeliness is re<sup>fl</sup>ected by timesensitive favor actions a member receives. Intuitively, a member with higher favor volume, larger favor coverage and receiving more recent favor actions is likely to be more skilful. The above discussions are illustrated by way of a toy taken as an example in Fig. 2 where the rounded rectangles represent the members associated with an initial measure of in<sup>fl</sup>uence, and directed edges indicate the favor actions associated with a tuplebweight, time-interval>denoting the favor action occurrence and time. In Fig. 2, four obvious prestigious members m1, m2, m3 and m4 exist. In terms of favor volume, m1 and m2 are more prestigious due to the higher number of photos favored. While, in terms of favor coverage, m3 is more prestigious, because he has more fans than m2 and m4 and has more high-in<sup>fl</sup>uential fans than m1. In terms of favor timeliness, m1 is more prestigious since he receives more new favourites than others. As a result, to determine the <sup>fi</sup>nal rank of these members, a measure method is needed depending upon a trade-off between the three factors.

![](/api/attachments/VS7WB3U2/fulltext/images/398b4e0ed4baed9638e5cd6b7a5d1c39f4576e23a2d5ef6138e095efa2050e1a.jpg)  
Fig. 2. A toy example of favor action network.

The social network analysis (SNA), related to the network theory maps relationships between individuals in social networks, is a powerful tool to investigate communication behaviour of individuals [40]. SNA offers a number of measures to investigate structural properties of the social network. In our scenario, two basic indicators of “indegree” and “outdegree” are of special importance [39,40]. In the favor action network, indegree of a speci<sup>fi</sup>c member re<sup>fl</sup>ects his/her popularity by way of the number of received favor actions. Outdegree of a member measures activity in choosing favourites. From this perspective, measures based on these two basic indicators, namely, degree distribution, indegree and outdegree relationship, and mixing pattern, can exploit communication behaviour of members. Degree distribution describes the degree characteristics of a favor action network from a global point of view. A power-law distribution of degree indicates a scale-free nature of social network, which means degree distribution is independent of network scale [6]. The indegree and outdegree relationship measures the probability that nodes with high indegree in a social network are also with high outdegree. Mixing pattern [32] describes the tendency of nodes of a network to link to other nodes with similar properties, which is a widely used indicator for investigating structural properties of networks. A coef<sup>fi</sup>cient named assortativity coef<sup>fi</sup>cient is used to quantitatively describe the mixing pattern. Both an increasing trend of correlation function and a positive assortativity coef<sup>fi</sup>cient implies an assortative mixing pattern of a social network, which would indicate that nodes with high outdegree would like to link to those with high indegree.

Social science researchers have proposed numerous theories to investigate human behaviour. Peer-to-peer in<sup>fl</sup>uence and homophily effect are two main reasons cause the correlation of members' behaviours [28]. Homophily [3] refers to the principle that “contacts between similar people occur at a higher rate than among dissimilar people”, and is vividly summarized as “birds of feathers <sup>fl</sup>ock together”. While, the triadic interaction rule [10] proposed by Heider is another theory used in this study, which says that “the friend of my friend is my friend.” It should note that, although homophile and in-<sup>fl</sup>uence are two different effects causing members' interactive actions, distinguishing the effect of one from the other is not an easy issue in practice. Like related studies which regard homophile and in<sup>fl</sup>uence as two independent factors, in our work, the effects of these two factors are investigated for the prediction of favor action intentions.

The above theoretical background provides theoretical support to the proposed framework's design, which consists of four functional components (Fig. 3). The structural properties investigation component aims to take an in-depth view of communication behaviours of members, where three measures are explored for the favor action network, namely, degree distribution, the relationship between indegree and outdegree, and mixing pattern. The potential favor behaviour component introduces four key factors that play an important role in mining the effect of the network structure on members' favor action intentions. The prestige calculation component quanti<sup>fi</sup>es the prestige value based on the favor action network and the prestige prediction component predicts the evolution of the prestige value via exploring all the four key factors introduced above.

## 3.2. Structural properties investigation

Based on the social network analysis theory, three measures are explored in this functional component to investigate communication behaviours of members. Better understanding the communication behaviours will provide an intuitive identi<sup>fi</sup>cation of prestigious members.

Indegree (outdegree) distribution expresses the fraction of members with degree $k _ { i n } \ ( k _ { o u t } )$ , denoted by $D i s ( k ) = P ( k _ { i n } > k )$ . If a large number of members are with low degree and only a few members are with high degree, the degree distribution would follow a powerlaw distribution as identi<sup>fi</sup>ed in majority of studies [5,30]. Such favor action network will display a scale-free structure with heterogeneous properties. The identi<sup>fi</sup>cation of this property can not only verify the existence of highly interconnected “central” members, but also indicate the preference behaviour of “new-arrival” members.

![](/api/attachments/VS7WB3U2/fulltext/images/95d797a549503a00d44b449e3ab357670ad31660a109f15dca386cea613dd804.jpg)  
Fig. 3. An overview of the research design framework.

The strength of the indegree and outdegree relationships of members in the favor action network is calculated by way of a linear relationship (i.e. correlation coef<sup>fi</sup>cient) between indegree and outdegree,

denoted by $c o r r = \frac { \sum _ { i = 1 } ^ { n } \left( k _ { i n } ^ { i } - \overline { { k _ { i n } } } \right) \left( k _ { o u t } ^ { i } - \overline { { k _ { o u t } } } \right) } { \sqrt { \sum _ { i = 1 } ^ { n } \left( k _ { i n } ^ { i } - \overline { { k _ { i n } } } \right) ^ { 2 } } \sqrt { \sum _ { i = 1 } ^ { n } \left( k _ { o u t } ^ { i } - \overline { { k _ { o u t } } } \right) ^ { 2 } } } .$ To further <sup>¼ ¼</sup>investigate the correlation from a global perspective, one can calculate the cumulative distribution of outdegree-to-indegree ratio, which measures the fraction of members with both high degree and high outdegree, denoted by $R ( \sigma ) = \left( \frac { k _ { o u t } } { k _ { i n } } > \sigma \right)$ . A low correlation coef<sup>fi</sup>cient indicates a weak correlation between the indegree and outdegree of a member, and vice versa. If the correlation is weak and the outdegree is higher than indegree for most members, it suggests the communication behaviour of “non-central” members turns out to favor members highly interconnected.

Mixing pattern is explored to measure the probability of a member with degree $k _ { o u t }$ preferring to connect to a member with degree $k _ { i n } .$ Formally, the outdegree-to-indegree correlation function $K _ { n n }$ is measured using “a mapping between outdegree and the average indegree of all nodes linked from the nodes of that outdegree” [30], denoted by $K _ { m } ( k _ { o u t } ) = \frac { 1 } { \left| u : k _ { u } = k _ { o u t } \right| } \sum _ { u : k _ { u } = k _ { o u t } } \frac { 1 } { \left| v : ( u , \nu ) \in E _ { 1 \sim T } \right| } \sum _ { \nu : ( u , \nu ) \in E _ { 1 \sim T } } k _ { i n } ^ { ( \nu ) } .$ Correspondingly, assortativity coef<sup>fi</sup>cient [32] is de<sup>fi</sup>ned as the Pearson correlation coef<sup>fi</sup>cient between pairs of members, characterizing the degree of similarity between connected members, denoted by

$$
r = \frac {M ^ {- 1} \sum_ {i} j _ {i} k _ {i} - \left[ M ^ {- 1} \sum_ {i} \frac {1}{2} (j _ {i} + k _ {i}) \right] ^ {2}}{M ^ {- 1} \sum_ {i} \frac {1}{2} \left(j _ {i} ^ {2} + k _ {i} ^ {2}\right) - \left[ M ^ {- 1} \sum_ {i} \frac {1}{2} (j _ {i} + k _ {i}) \right] ^ {2}}.
$$

trend of the outdegree-to-indegree correlation function and a positive value of assortativity coef<sup>fi</sup>cient further con<sup>fi</sup>rm the communication behaviour of “non-central” members and also con<sup>fi</sup>rm the existence of “central-like” prestigious members.

## 3.3. Potential favor behaviour analysis

Since the basic idea behind identifying evolving prestigious members is to capture an evolving favor action network, the prediction of members' favor intensions is thus needed. In this sub-section, we analyze members' potential favor behaviours, which is crucial in predicting members' favor intensions. Based on the sociology theory, four key factors which indicate the potential favor behaviours are introduced.

The <sup>fi</sup>rst factor is the homophily factor. Based on the homophily theory [29], members ”<sup>fl</sup>ocking” together are more likely to appreciate each other's photos. This factor leads members with more similar interests to perform favor actions on each other, which will modify the favor action network. In quantifying the degree of their common interests, the number of favored people common to a pair of members is explored.

The second factor is the triadic interaction factor. In an evolving favor action network, the triadic interaction rule [10] can be speci<sup>fi</sup>- cally interpreted as “the favourites of my favored people are also my favourites.” This factor re<sup>fl</sup>ects that individual members may tend to be in<sup>fl</sup>uenced by their favored people, and thus choose the favourite photos of their favored people as own favourites. This favor action intention will modify the favor action network and need to be considered in identifying evolving prestigious members.

Thirdly, from the perspective of psychology, an individual's interest may not change frequently or, in other words, one would probably favor the same members over a short period. This can be seen as continuous nature of an individual's interest, referred as the recency factor.

Lastly, we conjecture that the temporal sequence of favor action networks provides diversity weight of information for prediction. Since members' activities evolve over time, it is quite likely the more recent favor action constitutes a heavier indicator for prediction.

## 3.4. Prestige calculation

As aforementioned, since three factors, namely, volume, coverage and timeliness, codetermine members' prestige, the prestige value at time step T is quanti<sup>fi</sup>ed using a two-phase process, taking the temporal sequence of graphs $G = \{ G _ { 1 } ~ G _ { 2 } . . . G _ { T } \}$ as input. Let $S _ { T }$ denote the n-dimensional prestige score vector, where $S _ { T } ( i )$ denotes i-th coordinate of the vector representing the prestige score of member i. The temporal sequence of graphs G is <sup>fi</sup>rst transformed into a static graph $G _ { 1 \sim T }$ based on an exponential weighting scheme proposed by Hill [11]. This scheme summarizes the dynamic nature of favor actions between related members by frequency and recency of the relationship. More precisely, historical activities on edges are summarized into a single edge by an exponentially weighted moving average [43] (parameterized by $\theta ) .$ The form of this function is conveniently expressed in a recurrent form. Let $G _ { 1 \sim T } = ( V , E _ { 1 \sim T } , W _ { 1 \sim T } )$ denote the static representation, where

$$
\begin{array}{l} E _ {1 \sim T} = \{(u, v) | (u, v) \in E _ {1 \sim T - 1} \vee (u, v) \in E _ {T} \}, \text { and } \\ W _ {1 \sim T} = \{w _ {1 \sim T} (u, v) = \theta w _ {1 \sim T - 1} (u. v) + (1 - \theta) w _ {T} (u, v), \forall (u, v) \in E _ {1 \sim T} \}. \end{array}\tag{1}
$$

where θ is used to adjust the proportion of the historical favor activities in summarization.

Based on static representation $G _ { 1 \sim T } ,$ quantifying the prestige needs a trade-off between the favor volume and the favor coverage. As aforementioned, the favor volume refers to the number of photos chosen by other members as favourites. For user u, the favor volume can be calculated by $\sum _ { ( \nu , u ) \in E ( 1 \sim \mathrm { T } ) } w _ { 1 \sim T } ( \nu , u )$ . The favor coverage stands for the number of in<sup>fl</sup>uential fans of a member. Therefore, the favor coverage should not only consider the number of fans but also take the initial in<sup>fl</sup>uential degree of these fans into account. In this work, we use the favor volume value of a fan to measure his initial in<sup>fl</sup>uential degree. So the favor coverage can be calcu-

$$
\sum_ {(v, u) \in E _ {1 \sim T}} \left(I (v, u) \sum_ {(x, v) \in E _ {1 \sim T}} w _ {1 \sim T} (x, v)\right)
$$

$$
I _ {1 \sim T} (v, u) = 1
$$

$W _ { 1 \sim T } ( \nu , u ) { > } 0 ,$ , otherwise $I _ { 1 \sim T } ( \nu , u ) = 0 .$ . To combine the favor volume and the favor coverage, we utilize a smoothing technique. By using two normalization constants $N _ { w }$ and $N _ { I } ,$ the volume and coverage are respectively normalized into the same scale between 0 and 1. Using a smoothing parameter a, the prestige value can be formalized as:

$$
\begin{array}{l} S _ {T} (u) = \alpha N _ {w} \sum_ {(v, u) \in E (1 \sim T)} w _ {1 \sim T} (v, u) \\ \quad + (1 - \alpha) N _ {I} \sum_ {(v, u) \in E _ {1 \sim T}} \left(I (v, u) \sum_ {(x, v) \in E _ {1 \sim T}} w _ {1 \sim T} (x, v)\right) \end{array}\tag{2}
$$

where α is a parameter to moderate the proportion between favor volume and coverage. Fig. 4 summarizes the calculation procedure.

## 3.5. Prestige prediction

The calculation of prestige focuses on detecting currently prestigious members. While in this sub-section, the prediction of prestige adopts a dynamic view. As discussed in Section 3.3, four key indictors play an important role in predicting the member's communication behaviour. To properly take into consideration these indicators, we resort to a hybrid algorithm by incorporating the extended Common Neighbors [10] method and the variation of Katz [15] method. Common Neighbors (CN) $( C N ( u , \nu ) = | N e i g h b o r s ( u ) \cap N e i g h b o r s ( \nu ) | )$ is proposed following a natural intuition that two individuals who share many colleagues in common would be more likely to come in contact each other [25]. Katz (KZ) $\begin{array} { r } { \bigg ( K a t z ( u , \nu ) = \sum _ { l = 1 } ^ { 2 } \beta ^ { l } \cdot | | p a t h s _ { u , \nu } ^ { l } | | \bigg ) } \end{array}$ is proposed to capture an intuition that the more paths there are between two nodes and the shorter these paths are, the stronger will be the relationship between these two nodes [25]. ||paths<sup>l</sup> || represents the sum of paths between member u and member v of length $l . \beta ^ { l }$ is an exponential delay function. Their consistent superior performances in predicting links in social network have been proved in [25] when compared with a number of other algorithms. However, according to the de<sup>fi</sup>nition of prestige, direction and weight of edges in the favor network play a signi<sup>fi</sup>cant role in determining the prestige score. This makes it different from the traditional link prediction problem in undirected unweighted social graph [25], which is only concerned with edge occurrence. Therefore, we adapt these two algorithms by taking both weight and direction into account in the context of our study.

![](/api/attachments/VS7WB3U2/fulltext/images/cc9e4b7f2c41c8a373e2a92ff74fb1f525f6a851c0d54c3df7ce46082f4605fe.jpg)  
Fig. 4. Summarization of the procedure of prestige calculation

$$
w _ {T + 1} ^ {(C N)} (u, v) = N _ {C N} \sum_ {k \in V, (u, k) \in E _ {1 \sim T}, (v, k) \in E _ {1 \sim T}, k \neq u, v} w _ {1 \sim T} (u, k) \times w _ {1 \sim T} (v, k)\tag{3}
$$

$$
\begin{array}{l} w _ {T + 1} ^ {(K Z)} (u, v) = \gamma | | p a t h s _ {u, v} ^ {1} | | + (1 - \gamma) | | p a t h s _ {u, v} ^ {2} | | \\ \qquad = \gamma N _ {K Z} ^ {(1)} \cdot w _ {1 \sim T} (u, v) \\ \qquad + (1 - \gamma) N _ {K Z} ^ {(2)} \cdot \sum_ {k \in V, (u, k) \in E _ {1 \sim T}, (k, v) \in E _ {1 \sim T}, k \neq u, v} w _ {1 \sim T} (u, k) \\ \qquad \times w _ {1 \sim T} (k, v) \end{array}\tag{4}
$$

where $N _ { C N } , N _ { K Z } ^ { ( 1 ) }$ and $N _ { K Z } ^ { ( 2 ) }$ are three normalization constants calculated to limit $w _ { T + 1 } ^ { ( C N ) }$ and $w _ { T + 1 } ^ { ( \widetilde { K Z } ) }$ within a controllable interval. For instance, $W _ { T + 1 }$ should be comparable with historical $W _ { t } \left( t { < } T + 1 \right)$ . Therefore, the maximum values of $W _ { T + 1 } ^ { ( C N ) } , W _ { T + 1 } ^ { ( K Z ) 1 }$ and $W _ { T + 1 } ^ { ( K Z ) 2 }$ are limited to the historical maximum value of $W _ { t } \left( t { < } T + 1 \right)$

The measure of $w _ { T + 1 } ^ { ( C N ) } ( u , \nu )$ extends from CN algorithm by considering the weight of each edge between pairs of members. It measures a weighted “common favored people” of a pair, re<sup>fl</sup>ecting their “homophily” degree. The measure of $w _ { T + 1 } ^ { ( K Z ) } ( u , \nu )$ is a variation of the KZ algorithm. The former component with $l = 1$ measures the weight of historical relationship pointing from member u to member v. It gives us approximate access to the measure of “continuity” degree of how member u continuously favors towards member v. The latter component of $w _ { T + 1 } ^ { ( K Z ) } ( u , \nu )$ with $l = 2$ measures the degree of member u favoring towards v as affected by k, representing the “triadic interaction rule” degree. $W _ { 1 \sim T }$ in both equations is a summarization of $W _ { 1 } \sim W _ { T }$ using an exponential smoothing scheme (Eq. (1)). This scheme assigns higher weight to more recent favor actions which constitute higher indication of favor intentions. It considers the feature of “recency”.

In order to take all four features into account, a hybrid algorithm is proposed following an aggregation scheme of weighted summation of these two measures.

$$
w _ {T + 1} (u, v) = \eta w _ {T + 1} ^ {(C N)} (u, v) + (1 - \eta) w _ {T + 1} ^ {(K Z)} (u, v)\tag{5}
$$

$w _ { T + 1 } ( u , \nu )$ measures the predicted interactions among members at time-step $T + 1$ . Parameter η controls the mixing proportion of the two components. According to the problem formulation in Section 3, the key challenge of predicting prestigious members is solved. More concretely, the procedure of the proposed algorithm is summarized as follows:

Input: the temporal sequence of graphs $G = \{ G _ { I } G _ { 2 } . . . G _ { T } \}$

Output: the prestige vector $S _ { T + 1 }$

• Step 1: Based on $G ,$ calculate the statistic representation $G _ { 1 \sim T }$ using Eq. (1).

• Step 2: Based on $G _ { 1 \sim T } ,$ calculate $W _ { 1 \sim T } ^ { ( C N ) }$ and $W _ { 1 \sim T } ^ { ( K Z ) }$ using Eqs. (3) and (4), respectively.

• Step 3: Aggregate these two measures using Eq. (5) to achieve $W _ { T + 1 }$ (meanwhile $G _ { T + 1 }$ is achieved).

• Step 4: Given $G _ { T + 1 }$ , calculate the statistical representation $G _ { I \sim T  I }$ using Eq. (1).

• Step 5: Based on $G _ { 1 \sim T + 1 } ,$ , calculate $S _ { T + 1 }$ using Eq. (2) to accomplish prediction.

## 4. Empirical evaluation

In this section, comprehensive and systematic analyses are conducted to evaluate the proposed prestige prediction framework. The collection of dataset used in the empirical work and the evaluation metric are presented <sup>fi</sup>rst. Then four designed analyses are conducted. According to the social structure theory which points out that the dynamic nature of the favor action network structure will affect members' favor actions, the characteristic of prestige evolution is <sup>fi</sup>rst examined. Then using SNA which is based on the network theory, structural properties of the favor action network are investigated to mine the communication behaviour of members. Next, the four key features proposed, based on the sociological theory, are veri<sup>fi</sup>ed by analyzing favor behaviours of members. Finally, calculation and prediction of prestige values are performed using formulas proposed in Sections 3.4 and 3.5. The performance is compared with results of another four prediction methods; results of the comparison verify the ef<sup>fi</sup>cacy of the proposed framework.

## 4.1. Dataset

To illustrate the mechanism, one randomly chosen quality indicator group is crawled from Flickr.com through its $\mathsf { A P I } . ^ { 2 }$ In our problem setting, the relationship between a pair of members is established in the form of favor action. Since no straightforward API tool exists for collecting data of favor relationships among members, we proceeded to construct a favor action log to record these relationships. A triplet (Photo, Owner, bFan, Time-stamp>) of each photo in the group photo pool is <sup>fi</sup>rst crawled. This gave us 50,173 photos with 3875 unique owners and 0.25 million favor marks in total. Each favor action in the log is represented as a triplet $( m _ { o w n e r } , m _ { f a n } , t )$ indicating that member $m _ { f a n }$ favored a photo of member $m _ { o w n e r }$ at time t. Since in this study we are only concerned with members who joined this group, the number of dissatisfying fans is pruned. After further being limited to a time interval between 1st September 2007 and

1st April 2010, the <sup>fi</sup>nal favor action log comprised 3875 member and 85,633 favor action relationships among them.

Since the sub-interval length should be long enough to imply suf-<sup>fi</sup>cient interactions among members and yet be short enough to capture the evolution of the favor action network, our <sup>fi</sup>nal investigation is performed on a sequence of monthly sub-intervals. This gives us 31 sub-intervals in total. The former 30 sub-intervals (i.e. September, 2007–March, 2010) are treated as background data, and the objective is to predict prestigious members in the last sub-interval (April, 2010).

## 4.2. Evaluation metric

In the sense of predicting members' prestige evolution, prediction results are evaluated by ranking members according to their predicted prestige results. Since customers and corporations are usually more concerned with the most prestigious members, top ranked members in the results should be rewarded more heavily than those ranked lower. The metrics of Normalized Discounted Cumulative Gain (NDCG) [13] is therefore adopted, which was initially devised to measure retrieval results. In the context of our study, the metrics of NDCG@k is adapted to capture evolution of top k prestigious members.

$$
N D C G @ k = M _ {k} \sum_ {j = 1} ^ {k} \left(2 ^ {S _ {T + 1} (j)}\right) / \log (1 + j)\tag{6}
$$

where $S _ { T + 1 } ( j )$ is the prestige value of ranking results returned at position $j , M _ { k }$ is a normalization constant calculated so that an ideal ordering would obtain a value of 1 for NDCG.

## 4.3. Analysis of the evolution of prestige

This analysis aims to take an intuition of the prestige evolution and Fig. 5 shows prestige scores of <sup>fi</sup>ve sampled members, where the prestige curves rise and fall as time unfolds. This is in accordance with the expectation that the top prestigious members vary over time. Since the prestige score cannot be predicted by simply exploring the trend of curves, it is necessary to mine in-depth structural properties of the favor action network. More precisely, the objective of this study is to predict $S _ { T + 1 }$ based on communications among members, which is recorded in discrete-graph series $G = \{ G _ { 1 } G _ { 2 } . . . G _ { T } \}$

## 4.4. Investigation on structural properties of favor action network

This analysis is conducted to examine potential structural properties of the network using the three measures introduced in Section 3.2, i.e. degree distribution, indegree and outdegree relationship, and mixing pattern.

Fig. 6 (a) and (b) illustrates distributions of probability when <sup>fi</sup>nding a member with indegree $k _ { \mathrm { i n } }$ and outdegree $k _ { \mathrm { o u t } }$ , respectively.

![](/api/attachments/VS7WB3U2/fulltext/images/01db19c0064dfebad66468ad778cee848c0d6a1be111a6ccf2e9fe7b9657916c.jpg)  
Fig. 5. Evolving trend of prestige of 5 sampled members

![](/api/attachments/VS7WB3U2/fulltext/images/2ac35114692e94afa08aa02176c74ffc4c4a83d8d0adfe7553e3d3f6290d3811.jpg)

![](/api/attachments/VS7WB3U2/fulltext/images/ecb4171deed945199402a680491a17d1d854415c2872d44ab884981692ade486.jpg)  
Fig. 6. Log–log plot of indegree and outdegree distributions.

Consistent with the <sup>fi</sup>ndings from the literature [5,30], the networks follow the power-law distributions [6], which thus can be called scale-free networks. Moreover, an observation that these distributions are broad indicates that both indegree and outdegree patterns of members are highly heterogeneous. Validation is carried out by an average of 4.41 and variances of 231.6 (223.1) for indegree (outdegree). These characteristics indicate that the network tends to contain centrally located members and “new-arrival” members prefer the existing highly interconnected central ones. This property of the member's behaviour con<sup>fi</sup>rms the identi<sup>fi</sup>cation of prestigious members and their in<sup>fl</sup>uence on information diffusion.

A correlation coef<sup>fi</sup>cient of 0.2 (p-valueb0.001) indicates the indegree of a member is not strongly correlated with the outdegree. For further investigation, Fig. 7 displays the cumulative distribution of the outdegree-to-indegree ratio for the favor action network. It can be seen that most members have outdegree higher than indegree and only a small fraction of members have indegree higher than outdegree. This observation provides a strong indication that members with high outdegree are more likely to favor photos of members with high indegree, rather than members with high outdegree. To verify this assumption, mixing patterns [32] of the favor action network are examined.

Fig. 8 exhibits the distribution result of mixing pattern, where a slightly assortative trend is observed. Calculating the assortativity coef<sup>fi</sup>cient [32], a positive value of 0.0098 con<sup>fi</sup>rms the observation. In line with our assumption, the increasing $K _ { \mathrm { n n } }$ indicates that members with high outdegree prefer to link to members with high indegree in the group. Consequently, these observations identify the existence of a small fraction of relatively prestigious members in the group; in addition, comparably rich interactions among members would be a good indicator for prestige prediction.

![](/api/attachments/VS7WB3U2/fulltext/images/a60a97b996568cd2d16fbc9abea5d35fc14bd1a952488be757bf133d698b6bfb.jpg)  
Fig. 7. The cumulative distribution of outdegree-to-indegree ratio.

## 4.5. Analysis of potential favor behaviour

This analysis is designed to verify the four key features proposed in Section 3.3 by analyzing favor behaviours of members, i.e. homophily, triadic interaction rule, continuity and recency. Four questions corresponding to the analysis of potential favor behaviour in prior section are presented.

• Question 1: Does the number of common favored people of a pair of members have a positive effect on the intention to favor towards each other?

• Question 2: Does the favor intention of members follow the triadic interaction rule?

• Question 3: Does the historical interest of a member affect his favor intentions?

• Question 4: Do recent favor actions constitute better indications than those in the distant past?

To qualitatively answer these questions, we proceed in the following fashion. For the <sup>fi</sup>rst question, the intuition seems to be that pairs with bi-directional links are likely to achieve a higher degree of common interest than pairs with uni-directional links or no links. Therefore, we proceed as follows. All pairs of members are <sup>fi</sup>rst divided into three categories based on their link types at time-step T: unidirection, bidirection and non-link. Then 100 pairs from each category are sampled. For each pair, their common favored members at timestep T−1 are counted as the degree of common interest. Fig. 9 shows the log-plot results (zero values are removed) of each pair in an increasing order. In order to exclude the biases caused by the sampling process, the data is resampled ten times. Similar curves show the robustness of the observed behaviour. A comparison of three lines obviously expresses that historical similarity values of bidirectionally connected pairs are suf<sup>fi</sup>ciently higher than the other two categories. Therefore, the answer for Question 1 is “yes”.

![](/api/attachments/VS7WB3U2/fulltext/images/a68b9da8e47927bfdf12fb398e777c7beb21782b13af2f4cdf4c0922917ca307.jpg)  
Fig. 8. Log–log plot o $\mathrm { K } _ { \mathrm { n n } }$ values over outdegree.

![](/api/attachments/VS7WB3U2/fulltext/images/6256c58d51fb147e32a1b3054fa470fc8e43d504132d763d6358986fef30fdd2.jpg)  
Fig. 9. Log-plot similarities of each sampled pair in an increasing order.

For the second question, if members are in<sup>fl</sup>uenced by others through favor action channel, member m would favor n if there is a member k favoring n and favored by m. Therefore, the following procedures are performed. First, based on the historical static group $G _ { 1 \sim t }$ at time-step t, two predicted graphs denoting time-step T $( T > t )$ are generated by adding new edges to a null-edge graph (G<sup>t</sup> = $\langle V ^ { t } = V , E _ { T } ^ { t } = n u l l \rangle )$ following two different rules. One graph $G _ { T } ^ { t ( 1 ) }$ is generated following the triadic interaction rule. That's to say, if member u favors towards member k and member k favors towards member v, then add an edge pointing from u to v in $G _ { T } ^ { t ( 1 ) }$ . The other predicted graph $G _ { T } ^ { t ( 2 ) }$ is generated following a random generating rule, where edges are randomly assigned to pairs of members. Then, the predicted graphs are evaluated by comparing them with the actual graph $G _ { T } .$ . Alternately, the accuracy can be measured using a normalized frequency of common links between $G _ { T } ^ { t }$ and $G _ { T } .$ For instance, $P ( E _ { T } ^ { t } | E _ { T } ) \colon = | E _ { T } ^ { t } \cap E _ { T } | / | E _ { T } | .$ Fig. 10 shows $P ( E _ { T } ^ { t ( 1 ) } | E _ { T } )$ and $P ( E _ { T } ^ { t ( 2 ) } | E _ { T } )$ over t, where $t { = } T { - } 1 0 , T { - } 9 { , } { \ldots } , T { - } 1 .$ It can be seen that apparently, for all time-steps, measures following triadic rule perform signi<sup>fi</sup>cantly better than the baseline. This observation suggests that triadic interaction indeed bears a relation to the favor action behaviour. Therefore, the answer for Question 2 is also positive.

For the third question, it intuitively seems that if individuals' interest is continuous, the correlation between current interactions among members and historical interactions would be strong. Therefore, the Pearson correlation coef<sup>fi</sup>cients between $G _ { T }$ (recording current interactions) and $G _ { t }$ (recording historical interactions, t b T) are measured. Fig. 11 shows values over $t ~ \left( t = T - 1 0 , ~ T - 9 , . . . , T - 1 \right)$ where a monotonically increasing trend is visible. A value of 0.53 at T−1 shows a strong correlation between members' historical interactions and current interactions, which implies a positive answer to Question 3.

![](/api/attachments/VS7WB3U2/fulltext/images/38aceb5a2cd4cfcd7100c086ff5317d29c91b5b9a6427230911544e107d232d3.jpg)  
Fig. 10. Normalized frequency of common links between ${ \bf { G } } _ { \mathrm { { t } } } { } ^ { \prime }$ and $G _ { \mathrm { T } }$ over t.

![](/api/attachments/VS7WB3U2/fulltext/images/3de7ba8eb47e521a3129c300b13d199bb0d036677ce9deb08032ee929c3d47fe.jpg)  
Fig. 11. Correlation coef<sup>fi</sup>cients between $G _ { \mathrm { T } }$ and $\mathrm { G } _ { \mathrm { t } }$ over t.

It's important to note that the increasing trend gives a suggestion of how the correlation between two favor actions depends on their distance along the temporal dimension. As the distance increases, the correlation coef<sup>fi</sup>cient drops rapidly, and it becomes smaller than 0.1 when $t { < } T { - } 4 .$ . Recalling the similar observation exhibited in Fig. 10, it's quite likely that recent interactions are more indicative than interactions in the distant past, implying a positive answer to Question 4. In summary, a series of evaluation results verify the validity of the analysis conclusion of potential favor behaviours.

## 4.6. Evaluation of prestige prediction

This sub-section calculates and predicts prestige values of all members in the dataset. Since there are several parameters which will affect the performance of prestige prediction, parameters are selected <sup>fi</sup>rst. Then, evaluation results are compared with another four baseline methods.

## 4.6.1. Setting the parameters

There are four key parameters in our problem setting that determine the performance of the prediction:

• θ in Eq. (1) is used to adjust the proportion of historical interactions in the static representation.

• α in Eq. (2) is used to moderate the proportion between favor vol ume and coverage.

• γ in Eq. (4) and η in Eq. (5) are used to moderate the proportion among in<sup>fl</sup>uences from homophily, triadic interaction rule and continuity.

The former two are empirical parameters used in the de<sup>fi</sup>nition of prestige. They are determined by human expectation of characteristics of prestigious members. In our study, θ is <sup>fi</sup>xed at 0.2 to assign more weight to recent interactions, and α is <sup>fi</sup>xed to 0.2 to attach more importance to favor coverage than volume.

The latter two are tuneable parameters, which determine the performance of the proposed algorithm. Based on the historical data, we enumerate a list of values for different parameters and pick up values with which the algorithm performs best. For parameter selection, data of March 2010 is regarded as the ground-truth, and historical data is used for prediction. The reciprocal Euclidean distance between measured NDCG@k $( k = 1 - 2 0 )$ and 1-vector denoting ideal performance is calculated to evaluate the parameters. Fig. 12 (a) and (b) shows the results. As expected, the curves peak at some suitable value of γ and η between 0 and 1. According to Fig. 12, we set η=0.85 and $\gamma { = } 0 . 7 5$ in our following empirical work.

![](/api/attachments/VS7WB3U2/fulltext/images/924c54fce8fb352c10fe7b646d6ffee8c5f22404a351422fd740da56491f9de4.jpg)

![](/api/attachments/VS7WB3U2/fulltext/images/c540b7e615253cc26a28017d16adc1cbe616c37ffd69d0e78233378ccd578604.jpg)  
Fig. 12. Evaluation of different values of ηγ and γ.(a) Different ηs $( \theta = 0 . 2 , \alpha = 0 . 2$ γ=0.75). (b) Different γs (θ=0.2, α=0.2, η=0.6).

## 4.6.2. Evaluation result

To evaluate the performance of the proposed algorithm, prestigious members are predicted using <sup>fi</sup>ve different designed methods:

• T-baseline: As the most recent favor action graph G may contain the most critical temporal dependency for predicting popular members at $T + 1$ , the method of using $S _ { T }$ as the prediction of $S _ { T + 1 }$ is referred to as T-baseline.

• Homophily-baseline: In this method, the dependency of favor intention on homophily is measured in spite of other features when predicting $G _ { T + 1 }$

• Triadic-baseline: Correspondingly, the dependency of favor intention on triadic interaction rule is measured in spite of other features in this baseline.

• Sum-baseline: In this method, a simple summation of historical favor actions is performed to replace the weighted smoothing scheme.

• Hybrid-method: This is the algorithm detailed in the previous section.

Each of the <sup>fi</sup>ve above-described methods is performed to predict k most prestigious members and the corresponding results are evaluated in terms of NDCG@k. The ground-truth judgment of the order of prestigious members is the actual order generated by calculating $S _ { T + 1 }$ at time-step $T + 1$ (i.e. April, 2010). Evaluation results obtained when focusing on a sequence of monthly sub-intervals are shown in Fig. 13. It's observed that the hybrid method performs better than all the other four methods, with an exception at $k = 4 .$ The comparison between hybrid-method and T-baseline shows a clear additional bene<sup>fi</sup>t of interactions among members for prediction of prestigious members.

![](/api/attachments/VS7WB3U2/fulltext/images/15f2f3747614eeed2e9e0cc7351240456446976bfca3725a8fb28362ec562523.jpg)  
Fig. 13. Evaluation results in terms of NDCG@k.

The obvious improvement indicates the positive affection of the CN and Katz method. In cases of homophily-baseline and triadic-baseline, although neither of them exhibits a satisfactory performance, the distance compared with hybrid-method reveals that the two features add additional and complementary predictive power by looking into in-depth favor behaviour of members. Among all the <sup>fi</sup>ve methods, the static-baseline method performs the worst as it ignores the recency factor of favor actions. This <sup>fi</sup>nding helps con<sup>fi</sup>rm the earlier observations in Section 4.4 about the temporal dependency of correlation between favor actions of a particular member. This appears in line with our expectation that recent relationships in favor action network tend to contain more indication of individual intentions than old ones. In summary, in line with our preliminary analyses, historical interactions among members (i.e. the favor action network) can be mined to successfully predict prestigious members in Flickr groups. In addition, the improvement achieved by our proposed hybrid algorithm guarantees that both customers and corporations can discover prestigious members more precisely. Especially for business applications such as target advertisement, the improvement of precision would evoke more interest from companies.

## 5. Conclusion

In this paper, we propose a way to address the problem of predicting evolution of prestigious members using quality indicator Flickr groups as a testbed. Based on the network structural theory, we introduce a graph-based framework to capture interactions among members. The dynamic communication behaviour of members is constructed as a favor action network. According to the theory, the favor action network structure implies the potential favor action intentions of members. Therefore, an investigation of structural properties of favor action network is involved in the framework. Besides, based on analysis of members' interaction behaviour, we present four indicator features for predicting favor action intentions of members. It can be concluded that <sup>fi</sup>rst, members with similar interests are more likely to appreciate each other's photos in future, which is referred to as the homophily feature. Second, members would be in<sup>fl</sup>uenced by others through favor action channel, namely, member m would favor n if there is a member k favoring n and favored by m. This <sup>fi</sup>nding can be well explained by triadic interaction rule. Third, a member would continuously favor the same member whom he has favored before, for the reason that the interest of a member may not vary frequently. This can be regarded as the continuous nature of favor intention. Last, the increasing curves in Fig. 10 and Fig. 11 indicate that recent interactions constitute a higher indication than interactions in the distant past. Based on the four key features, we predict the value of prestige by aggregating two extended typical static graph link prediction methods (i.e. Common Neighbors and Katz). Comprehensive and systematic analyses verify the ef<sup>fi</sup>cacy of the proposed framework. Compared with the four designed baseline methods, evaluation results shown in Fig. 13 illustrate the ef<sup>fi</sup>cacy of the features considered in the proposed algorithm.

The framework for predicting members' prestige evolution is illustrated using an empirical work. Since prestigious members play an important role on Flickr platform as aforementioned, our study suggests an interesting implication for future e-commerce application designs. For instance, in our ongoing work, we are interested in implementing a demonstration system devoted to identifying and predicting prestigious members standing for different camera brands and models. These members would be recommended to both customers and corporations. Customers can consult the photo pool of these recommended members when comparing different brands or models. For corporations, these recommended members are perfect advertising targets for either static advertisement or word-of-mouth advertising.

## Acknowledgements

This research is supported by the NNSFC projects 61172106 and 61005029 and the BJNSF 4112062.

## References

[1] F. Bodendorf, C. Kaiser, Detecting opinion leaders and trends in online social networks, Proceeding of the 2nd ACM Workshop on Social Web Search and Mining, SWSM'09, ACM, Hong Kong, China, 2009.

[2] R.S. Burt, Toward a Structural Theory of Action: Network Models of Social Structure, Perception and Action, in, Academic Press, New York, 1983.

[3] M. Cha, A. Mislove, K.P. Gummadi, A measurement-driven analysis of information propagation in the Flickr social network, Proceedings of the 18th international conference on World wide web, WWW'09, ACM, Madrid, Spain, 2009, pp. 721–730.

[4] C.M.K. Cheung, M.K.O. Lee, A theoretical model of intentional social action in online social networks, Decision Support Systems 49 (1) (2009) 24-30

[5] A. Clauset, C.R. Shalizi, M.E.J. Newman, Power-law distributions in empirical data, SIAM Review 51 (4) (2009) 661–703.

[6] M. Faloutsos, P. Faloutsos, C. Faloutsos, On power-law relationships of the Internet topology, SIGCOMM Comput, Communications of Reviews 29 (4) (1999) 251–262.

[7] D. Ganley, C. Lampe, The ties that bind: social network principles in online communities, Decision Support Systems 47 (3) (2009) 266–274.

[8] R. Ghosh, K. Lerman, Predicting in<sup>fl</sup>uential users in online social networks, The fourth SNA-KDD Workshop with The 16th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2010.

[9] A. Goyal, F. Bonchi, L.V.S. Lakshmanan, Discovering leaders from community actions, Proceeding of the 17th ACM conference on Information and knowledge management, CIKM'08, ACM, Napa Valley, California, USA, 2008, pp. 499–508.

[10] F. Heider, Attitude and cognitive organization, The Journal of Psychology 21 (1946) 107–112.

[11] S. Hill, D.K. Agarwal, R. Bell, C. Volinsky, Building an effective representation for dynamic networks, Journal of Computational and Graphical Statistics 15 (3) (2006) 584–608.

[12] R. Iyengar, C. Van den Bulte, T.W. Valente, Opinion leadership and social contagion in new product diffusion, Marketing Science, 30(2) (2011) 195–212.

[13] K. Jarvelin, J. Kekalainen, Cumulated gain-based evaluation of IR techniques, ACM Transactions on Information Systems 20 (4) (2002) 422–446.

[14] A. Java, P. Kolari, T. Finin, T. Oates, Modeling the spread of in<sup>fl</sup>uence on the blogosphere, Proceeding of WWW 2006 Workshop on Weblogging Ecosystem: Aggregation, Analysis and Dynamics, 2006, Edinburgh, UK.

[15] L. Katz, A new status index derived from sociometric analysis, Psychometrika 18 (1) (1953) 39–43.

[16] P. Kazienko, K. Musial, A. Zgrzywa, Evaluation of node position based on Email communication, Control and Cybernetics 38 (1) (2009) 67–86.

[17] D. Kempe, J. Kleinberg, E. Tardos, Maximizing the spread of in<sup>fl</sup>uence through a social network, Proceedings of the ninth ACM SIGKDD international conference on Knowledge discovery and data mining, KDD'03, ACM, Washington, D.C, 2003, pp. 137–146.

[18] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers — measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008) 233–253

[19] R. Kumar, J. Novak, A. Tomkins, Structure and evolution of online social networks, Link Mining: Models, Algorithms, and Applications, Springer, New York, 2010, pp. 337–357.

[20] H.W. Lam, C. Wu, Finding in<sup>fl</sup>uential ebay buyers for viral marketing a conceptual model of BuyerRank, International Conference on Advanced Information Networking and Applications, AINA'09, IEEE, 2009, pp. 778–785

[21] C. Lee, H. Kwak, H. Park, S. Moon, Finding in<sup>fl</sup>uentials based on the temporal order of information adoption in twitter, Proceedings of the 19th international conference on World wide web, ACM, Raleigh, North Carolina, USA, 2010, pp. 1137–1138.

[22] J. Leskovec, J. Kleinberg, C. Faloutsos, Graphs over time: densi<sup>fi</sup>cation laws, shrinking diameters and possible explanations, Proceedings of the eleventh ACM SIGKDD international conference on Knowledge discovery in data mining, KDD'05, ACM, Chicago, Illinois, USA, 2005, pp. 177–187.

[23] Y. Li, J. Tang, Expertise search in a time-varying social network, The Ninth International Conference on Web-Age Information Management, IEEE, 2008, pp. 293–300.

[24] Y. Li, J. Tang, Expertise search in a time-varying social network, Proceedings of the 2008 The Ninth International Conference on Web-Age Information Management, WAIM'08, IEEE Computer Society, 2008, pp. 293–300.

[25] D. Liben-Nowell, J. Kleinberg, The link-prediction problem for social networks, Journal of the American Society for Information Science and Technology 58 (7) (2007) 1019–1031.

[26] D. Lu, Q. Li, Exploiting semantic hierarchies for Flickr group, Active Media Technology, Springer Berlin, Heidelberg, 2010, pp. 74–85.

[27] D. Lu, Q. Li, Personalized search on Flickr based on searcher's preference prediction, Proceedings of the 20th international conference companion on World wide web, ACM, Hyderabad, India, 2011, pp. 81–82.

[28] C.F. Manski, Identi<sup>fi</sup>cation of endogenous social effects: the re<sup>fl</sup>ection problem The Review of Economic Studies 60 (3) (1993) 531.

[29] M. McPherson, L. Smith-Lovin, J.M. Cook, Birds of a feather: homophily in social networks, Annual Review of Sociology 27 (1) (2001) 415–444.

[30] A. Mislove, M. Marcon, K.P. Gummadi, P. Druschel, B. Bhattacharjee, Measurement and analysis of online social networks, Proceedings of the 7th ACM SIG-COMM conference on Internet measurement, MM'07, ACM, San Diego, California, USA, 2007, pp. 29–42.

[31] R.A. Negoescu, D. Gatica-Perez, Analyzing Flickr groups, Proceedings of the 2008 international conference on Content-based image and video retrieval, ACM, Niagara Falls, Canada, 2008, pp. 417–426.

[32] M.E.J. Newman, Assortative mixing in networks, Physical Review Letters 89 (20) (2002) 208701.

[33] A. Potgieter, K.A. April, R.J.E. Cooke, I.O. Osunmakinde, Temporality in link prediction: understanding social complexity, Sprouts: Working Papers on Information Systems 7 (9) (2007).

[34] E.M. Rogers, Diffusion of Innovations, The Free Press, New York, 1962.

[35] U. Sharan, J. Neville, Exploiting time-varying relationships in statistical relational models, Proceedings of the 9th WebKDD and 1st SNA-KDD 2007 workshop on Web mining and social network analysis, WebKDD'07, ACM, San Jose, California, 2007, pp. 9–15.

[36] M.J. Shaw, C. Subramaniam, G.W. Tan, M.E. Welge, Knowledge management and data mining for marketing, Decision Support Systems 31 (1) (2001) 127–137.

[37] A. Singla, I. Weber, Camera brand congruence in the Flickr social graph, Proceedings of the Second ACM International Conference on Web Search and Data Mining, WSDM'09, ACM, Barcelona, Spain, 2009, pp. 252–261.

[38] X. Song, Y. Chi, K. Hino, B. Tseng, Identifying opinion leaders in the blogosphere, Proceedings of the sixteenth ACM conference on Conference on information and knowledge management, CIKM'07, ACM, Lisbon, Portugal, 2007, pp. 971–974.

[39] M.M. Wasko, R. Teigland, S. Faraj, The provision of online public goods: examining social structure in an electronic network of practice, Decision Support Systems 47 (3) (2009) 254–265

[40] S. Wasserman, K. Faust, Social Network Analysis, Cambridge Univ. Press, 1994.

[41] H.T. Welser, E. Gleave, D. Fisher, M. Smith, Visualizing the signatures of social roles in online discussion groups, Journal of Social Structure 8 (2007).

[42] J. Weng, E.P. Lim, J. Jiang, Q. He, TwitterRank: <sup>fi</sup>nding topic-sensitive in<sup>fl</sup>uential twitterers, Proceedings of the third ACM international conference on Web search and data mining, WSDM'10, ACM, New York, New York, USA, 2010, pp. 261–270

[43] P.R. Winters, Forecasting sales by exponentially weighted moving averages, Management Science 6 (3) (1960) 324–342.

[44] N. Zheng, Q. Li, S. Liao, L. Zhang, Which photo groups should I choose? A comparative study of recommendation algorithms in Flickr, Journal of Information Science 36 (6) (2010) 733–750.

Dongyuan Lu is a Ph.D. candidate in the State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences. She received her B.S. degree in Information Science and Technology from Beijing Normal University, China, 2007. Her research interests include information retrieval, web/text mining.

Qiudan Li is an Associate Professor in the State Key Laboratory of Management and Control for Complex Systems, at the Institute of Automation, Chinese Academy of Sciences. She received a Ph.D. in Computer Science from Da Lian University of Technology, China, 2004. Her research interests include web mining and mobile commerce applications. Her articles are published in Communications of the AIS, Decision Support Systems, Journal of the American Society for Information Science and Technology, IEEE Transactions on SMC, Expert Systems with Applications.

Stephen Shaovi Liao is an Associate Professor of Information Systems at City University of Hong Kong. He earned a Ph.D. from the University of Aix-Marseille III and Institute of France Telecom in 1993, He has been working at City University of Hong Kong since 1993 and his research has focused on use of IT in e-business systems. His articles have been published in Decision Support Systems JEEE transactions Communications of the ACM, Information Science, Computer Software and other SCI journals.
