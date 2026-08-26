---
otero_id: 16580
otero_key: "E74QPJCY"
title: "Coordinated inauthentic behavior and information spreading on Twitter"
authors: "Matteo Cinelli; Stefano Cresci; Walter Quattrociocchi; Maurizio Tesconi; Paola Zola"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113819"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Coordinated Inauthentic Behavior and Information Spreading on Twitter

Matteo Cinelli<sup>b,1</sup>, Stefano Cresci<sup>a,∗</sup>, Walter Quattrociocchi<sup>b,2</sup>, Maurizio Tesconi<sup>a,3</sup>, Paola Zola<sup>a,4</sup>

<sup>a</sup>Institute of Informatics and Telematics, National Research Council (IIT-CNR), Italy <sup>b</sup>Dept. of Computer Science, Sapienza University of Rome, Italy

## Abstract

We explore the efects of coordinated users (i.e., users characterized by an unexpected, suspicious, or excep tional similarity) in information spreading on Twitter by quantifying the eficacy of their tactics in deceiving feed algorithms to maximize information outreach. In particular, we investigate the behavior of coordinated accounts within a large set of retweet-based information cascades identifying key diferences between coordi nated and non-coordinated accounts in terms of position within the cascade, action delay and outreach. On average, coordinated accounts occupy higher positions of the information cascade (i.e., closer to the root), spread messages faster and involve a slightly higher number of users. When considering cascade metrics such as size, number of edges and height, we observe clear diferences among information cascades that are associated to a systematically larger proportion of coordinated accounts, as confirmed by comparisons with statistical null models. To further characterize the activity of coordinated accounts we introduce two new measures capturing their infectivity within the information cascade (i.e., their ability to involve othe users) and their interaction with non-coordinated accounts. Finally, we find that the interaction pattern between the two classes of users follows a saturation-like process. A larger-scale targeting of non-coordinated users does not require a larger amount of coordinated accounts after a threshold value ∼ 50%, after which involving more coordinated accounts within a cascade yields a null marginal efect. Our results contribute to shed light on the role of coordinated accounts and their efect on information difusion.

Keywords: coordinated inauthentic behavior, information spreading, disinformation, Twitter

## 1. Introduction

Social media play a pivotal role in the evolution of public debates and in shaping public opinion. Plat forms that were originally designed for entertainment are nowadays one of the main gateways to information sources and the principal environment in which public opinions get shaped. Users can access and share an unprecedented amount of information, and feed algorithms afect the selection process. Such a constant in formation overload determines a new tendency of news consumption [1, 2, 3], and generates opportunities fo civic engagement and public interest [4], also eliciting the so-called “democratizing efect”. However, social media are also afected by a number of ailments, including toxicity, harassment and hateful speech [5, 6], polarization and radicalization [7], propaganda and misleading information [8]. Regarding the latter issue, many studies recently investigated the spread of fake information and propaganda [9, 10] and the role of disinformation on social media [11, 12, 13]. Within this context, scholars also investigated the role of auto mated accounts in spreading both reliable and questionable information [14, 15]. This literature highlight that whether initial social bots could be accurately identified by state-of-the-art algorithms, recent manip ulation campaigns carried out with modern bots and with human-operated accounts (i.e., trolls) are more sophisticated and thus harder to detect [16, 17].

Going beyond early literature that focused on the nature (automated or otherwise) of the accounts as a way to distinguish between malicious and legitimate actions, more recent research moved the focus on the actions themselves and on the behaviors of the accounts. In a recent report, Facebook introduced the concept of false amplifiers that are characterized by “coordinated activity by inauthentic accounts with the intent of manipulating political discussions” [18]. The Facebook report introduces two new concepts associated with online information manipulation: coordination and inauthenticity. In literature, coordination is defined as an unexpected, suspicious, or exceptional similarity between a number of users [19]. In practice, it is often measured as the number of times two accounts behaved similarly, such as when they repeatedly retweet the same posts [20, 19]. Coordination among a certain number of users is considered to be a fundamental ingredient in successful manipulations, since it is necessary for the manipulation to obtain a significant outreach. On the contrary, the importance of inauthenticity – that is, whether online users misrepresent themselves – is still debated<sup>5</sup>. To this end, harmfulness, rather than inauthenticity, appears to be more relevant for the analysis of online manipulations<sup>6</sup>.

Interestingly, coordination is an orthogonal concept with respect to the long-studied automation<sup>7</sup>. In fact, recent results demonstrated limited correlations [8], or no correlations at all [19], between coordinated and automated accounts. In other words, coordination can be achieved without resorting to automation (i.e., social bots). Coordinated harassment by trolls and the supporting activity of online fandoms are two examples – harmful and harmless, respectively – of coordinated activities by human-operated accounts. For these reasons, the study of coordinated accounts and of their role in online information spreading can complement established studies on online information manipulation and can inform the development of new and efective decision support systems against these manipulations.

In this paper, we focus on the role of coordinated accounts in information spreading online – a crucial, yet understudied, issue. In particular, we address the eficacy of their coordinated behavior in deceiving feed algorithms to maximize information outreach. We perform an analysis of a large dataset of 1.4 million tweets about the 2019 UK political elections. We find that coordinated and non-coordinated accounts significantly difer in terms of their retweeting activity and their positioning within information cascades. Additionally, their involvement in the cascades is much higher in empirical data that in randomized models. Finally, by analyzing the interactions between the two types of accounts, we uncover a saturation-like process due to which the maximal interaction between coordinated and non-coordinated accounts amounts to ∼ 50% of the cascade links, regardless of the penetration of coordinated accounts in the whole cascade.

The paper is structured as follows: Section 2 outlines our research objectives, the main findings and their significance. Section 3 presents related works on coordinated behavior and information spreading. Section 4 illustrates the dataset used for conducting the analysis and the employed measures and methods. Section 5 details the results of the analysis. Section 6 discusses the implications of our research. Finally, Section 7 reports the conclusions.

## 2. Summary of research objectives, findings and significance

## 2.1. Research objectives and findings

Our study on the diferences between the interaction patterns of coordinated and non-coordinated ac counts focuses on retweet dynamics, the primary way to spread information on Twitter [21]. Under this perspective, our overarching goal is that of investigating the role, impact and tactics of coordinated accounts in information spreading on Twitter. In particular, we currently have limited knowledge of the peculiar traits, actions and tactics of coordinated accounts, except for their similarity in posting dynamics. Ou work contributes to filling this gap by adding new insights over the limited existing knowledge.

We reach our overarching goal by achieving the following three research objectives:

RO1: Describe the role of coordinated accounts in information spreading.

In fulfillment of RO1, we identify three measures that significantly distinguish the activity of coordinated accounts from that of non-coordinated ones. Such measures are related to the position of coordinated accounts in the information cascade (i.e., the distance from the root), their action delay (i.e., the time required for retweeting a message) and their descendent counts (i.e., the number of users that a coordinated account is able to involve in the cascade). We find that, on average, coordinated accounts are closer to the root of the information cascade, are faster in retweeting original messages and are able to involve a higher number of users with respect to non-coordinated ones.

RO2: Assess the impact of coordinated accounts on information outreach and engagement of posts.

To reach RO2, we carry out a thorough statistical analysis and we propose two novel indices. By mimicking a network dismantling process [22], our indices provide a synthetic yet informative description of the impact that coordinated accounts have on information cascades. Our analysis reveals a systematic influence of coordinated accounts on the structure of the information cascades in which they participate, in that they are able to afect cascade size, number of links and depth. Our findings are validated with appropriate null models.

RO3: Investigate the tactics and targets of coordinated accounts.

In RO3 we study the behavior of coordinated accounts in terms of targeted users. While we expected the amount of links between coordinated and non-coordinated accounts to grow proportionally with the number of coordinated accounts, we instead found a diferent situation where coordinated accounts are able to involve non-coordinated accounts in the cascade only up to a certain threshold that is ∼ 50% of the links. This means that coordination requires a big efort in order to be efective and that massive coordinated actions are indistinguishable from less prominent ones in terms of involvement of non-coordinated accounts. Overall, our results contribute to shed light on the tactics of coordinated accounts and their influence on information difusion.

## 2.2. Significance

Coordinated inauthentic and harmful behavior is an emerging problem on social media that has been linked to many other issues such as the spread of mis- and disinformation [23]. However, only limited knowledge, tools and results currently exist on coordinated behavior [19]. Not only does this lack of knowledge testify the existence of a scientific gap, but it also impairs the practical development of decision support systems (DSS) for supporting online platforms at maintaining safe and reliable social environments. Examples of such systems are those for assessing the veracity of online information [24]. Our theoretical results on the role played by coordinated accounts in the online spread of information contribute to filling the current scientific gap. In addition, a deeper understanding of the characteristics and behavior of coordinated users, and of their tactics to tamper with the regular flow of information, also have practical implications since our results can be used as features in future machine/deep learning systems for detecting both coordinated accounts [25] as well as inorganic or manipulated discussions [26]. Such systems will represent the next line of defense against coordinated propaganda and information manipulation, thus supporting both platform administrators and online users.

## 3. Related works

This section surveys relevant literature on online information manipulation and on online information spread.

## 3.1. Coordinated inauthentic and harmful behavior

Our present study is positioned within the growing body of work on coordinated inauthentic and harm ful behavior, a recent stream of research that focuses on the collective behavior exhibited by the account involved in online information manipulations. The rationale for this body of work stems from the observa tion that online manipulations (e.g., disinformation campaigns) must reach a wide number of users to b successful. This mandates large and coordinated eforts so that the manipulation can obtain a significant outreach, exert influence, and thus have an impact [26]. Despite often appearing together, coordination, inauthenticity and harmfulness are distinct and orthogonal concepts [19]. For example, regarding coordi nation and inauthenticity, there can exist activists and other grassroots initiatives that are characterized by coordinated but authentic behaviors. Conversely, an ill-intentioned user might maneuver a single fak account, thus exhibiting inauthentic but uncoordinated behavior. Obviously, many other combinations of coordination, inauthenticity and harmfulness are possible.

To detect coordinated behaviors, existing works either leveraged similarities in user behaviors analyzed via network science frameworks [8, 19, 20, 27, 28, 29, 30], or temporal synchronicity between user actions [25, 31, 32, 33]. The former approach typically includes analytical steps such as the construction of a weighted user-similarity network, the filtering of such network, the detection of the diferent coordinated communities in the network, and the study of their extent and patterns of coordination [34]. Contrarily to the positive results obtained for detecting coordinated behaviors, only limited results were achieved for dis tinguishing between authentic and inauthentic, or between harmless and harmful, coordination [23]. Some scholars worked around this issue by simply considering exceptional levels of coordination to be always indicative of malicious behaviors [20, 31]. Others instead proposed to combine the analysis of coordination and propaganda, as a way to identify harmful coordinated communities [8]. Anyway, independently on th methods adopted for the analyses, the majority of existing works focused on detecting coordination, leaving the characterization of coordinated users and the understanding of their tactics and influence essentially unexplored.

## 3.2. Information manipulation actors

Still marginally related to our work is the body of research on social bots and trolls, two types of malicious actors involved in online information manipulations [17]. In fact, detecting and removing these accounts is still considered to be an efecting approach for curbing online manipulations [35, 36]. The main diference between social bots and trolls is that the former is – at least partially – automatically driven via software, whereas the latter is mostly human-driven. The possibility of performing actions automatically, without the need for human intervention, makes social bots the ideal information spreading and management tool, since they can easily perform many actions (e.g., resharing certain content) in a limited time span [37]. Based on this intuition, several studies investigated the role of social bots in the spread of disinformation and, more broadly, in the emergence of several ailments that afect our online social ecosystems (e.g., polarization, hate speech). To this end, existing results are controversial, with some studies reporting a significant contribution of social bots in the spread of low-credibility content [14] and the extremization of online communities [38], while other studies only reported a marginal role [39]. Others specifically investigated the activity of bots in discussions about politics [40], finance [26, 41], health [42] and entertainment [15, 43], finding a much large bot activity than that measured on average on social media. Regarding the characteristics and the detection of social bots, there exists a consensus that such accounts are becoming more and more sophisticated as a consequence of the technological tools (e.g., deepfake videos and profile pictures<sup>8</sup>) that are increasingly used to create credible fake online personas [44]. These powerful computational means inevitably create increased challenges for the detection and removal of social bots, which also fueled criticism about the eficacy of th existing bot detection techniques [16, 45]. For this reason, recent approaches to contrast online information manipulations avoid classifying the nature (i.e., automated or human-driven) of individual accounts, and rather focus on detecting and investigating suspicious patterns of coordination. The latter approach, also used in our work, is more novel and considered to be more efective than the former.

## 3.3. Online information spreading

Independently of the type and nature of the actors involved in online information manipulations, one of their aims is to alter spreading dynamics, to amplify their messages, and to extend their reach. In particular, focusing on Twitter, the simplest action that can be used to spread messages to the Twittersphere is the retweet [21, 43]. Retweeting a message means forwarding it to the user’s followers network. Despite the simplicity of the process behind a retweet cascade graph, the free Twitter API service does not provide full information about the spreading process. Instead, it only gives information about each retweeter and the author of the original tweet. In other words, the actual path followed by an original tweet to reach its audience is unknown and must be inferred/reconstructed [46]. Initial works [47, 48, 49] derived the retweet propagation paths assuming that the user’s “screen name” reported in the tweet text, such as “RT@ screen name” indicates the user from whom the current user read the message. However, this assumption is mostly inaccurate [50] and information cascades that merge temporal data with social network information are generally considered to be more reliable. In such a vein, [51] proposed a model analyzing four diferent options based on followed accounts to derive the possible retweet graph. Since there is no ground truth to compare the possible cascade options, the authors evaluated the options computing several metrics. Other works considered additional information to derive the retweets’ propagation path such as text and topic similarity features [52] or location information [53, 54]. Few studies integrated the impact of social relationships, measured in terms of reciprocal interactions [53, 49, 55], in the analysis of retweeting dynamics.

In particular, the recent work of [55] introduced two models aimed at measuring the strength of interactions among users to build weighted retweet cascade graphs.

In this work, we are interested in studying the role of coordinated users in information cascades. For reconstructing the cascades we adopt the state-of-the-art method proposed in [56] that leverages the followerfollowing network of the users that participate to an information cascade, thus merging information deriving from users’ interests and social dynamics.

## 4. Data and Methods

## 4.1. Data

Our dataset for this study is based on a large collection of tweets related to the online debate about the 2019 United Kingdom general election<sup>9</sup>. By leveraging Twitter Streaming APIs, we collected one month of data: from 12 November to 12 December 2019 (election day). Our data collection strategy was based both on election-related hashtags and on influential political accounts. Regarding hashtags, we collected all tweets mentioning at least one hashtag from the list shown in Table 1. This list contains both polarized (i.e., labour or conservatives) hashtags, as well as neutral ones. Furthermore, we also collected all tweets published by the two parties’ oficial accounts and by their leaders, shown in Table 2, together with all the interactions (i.e., retweets and replies) they received. This data collection process allowed us to gather 11,264,820 tweets published by 1,179,659 distinct users. This dataset is publicly available for research purposes<sup>10</sup>.

Since we are particularly interested in coordinated behaviors and their efects on information difusion, we subsequently derived coordination scores for each user in our dataset by applying the state-of-the-art method proposed in [19]. This method, as well as other similar ones [20], measures coordination between accounts by analyzing the sequence of retweets of each account and by subsequently computing pairwise similaritie between all accounts. In particular, we associated each account to a TF-IDF weighted vector of the tweet IDs retweeted by that account. The TF-IDF weighting reduces the relevance of highly popular tweets, that are likely to receive many retweets, in favor of unpopular ones, whose retweets might be indicative of suspicious behaviors [43]. Then, we computed user similarities as the cosine similarity of account vectors. The similarity scores between all couples of accounts are used to build a user-similarity network whose edges are ranked by non-increasing weight. In our work, we retained the top 1% of the edges with the highest similarity scores among all those in our dataset. Following previous work [20], the nodes connected by such edges are considered to be coordinated accounts. The remaining accounts in our dataset are considered to be non-coordinated.

Finally, we filtered our initial dataset by only retaining the 49,331 tweets that were retweeted at least once by the accounts classified as coordinated and whose author is not a coordinated user. For each such

<table><tr><td>hashtag</td><td>users</td><td>tweets</td></tr><tr><td>#GE2019</td><td>436,356</td><td>2,640,966</td></tr><tr><td>#GeneralElection19</td><td>104,616</td><td>274,095</td></tr><tr><td>#GeneralElection2019</td><td>240,712</td><td>783,805</td></tr><tr><td>#VoteLabour</td><td>201,774</td><td>917,936</td></tr><tr><td>#VoteLabour2019</td><td>55,703</td><td>265,899</td></tr><tr><td>#ForTheMany</td><td>17,859</td><td>35,621</td></tr><tr><td>#ForTheManyNotTheFew</td><td>22,966</td><td>40,116</td></tr><tr><td>#ChangelsComing</td><td>8,170</td><td>13,381</td></tr><tr><td>#RealChange</td><td>78,285</td><td>274254</td></tr><tr><td>#VoteConservative</td><td>52,642</td><td>238,647</td></tr><tr><td>#VoteConservative2019</td><td>13,513</td><td>34,195</td></tr><tr><td>#BackBoris</td><td>36,725</td><td>157,434</td></tr><tr><td>#GetBrexitDone</td><td>46,429</td><td>168,911</td></tr><tr><td>total</td><td>668,312</td><td>4,983,499</td></tr></table>

<table><tr><td rowspan="2">account</td><td rowspan="2">tweets</td><td colspan="2">interactions</td></tr><tr><td>retweets</td><td>replies</td></tr><tr><td>@jeremycorbyn</td><td>788</td><td>1,759,823</td><td>414,158</td></tr><tr><td>@UKLabour</td><td>1,002</td><td>325,219</td><td>79,932</td></tr><tr><td>@BorisJohnson</td><td>454</td><td>284,544</td><td>382,237</td></tr><tr><td>@Conservatives</td><td>1,398</td><td>151,913</td><td>169,736</td></tr><tr><td>total</td><td>3,642</td><td>2,521,499</td><td>1,046,063</td></tr></table>

Table 2: Statistics about data collected from accounts.

Table 1: Statistics about data collected via hashtags.  
tweet in our sample, we constructed its retweet-based information cascade by following the method proposed in [56], as thoroughly detailed in the next subsection. Descriptive statistics about the retweeters (i.e., users who retweeted at least one post) are reported in Table 3.

<table><tr><td>average retweeters per cascade</td><td>number of unique retweeters</td><td>number of coordinated retweeters</td></tr><tr><td>16.38</td><td>205,277</td><td>1,192</td></tr></table>

Table 3: Summary features of retweeters. Among the 205,277 retweeters, 1,192 are labelled as coordinated.

## 4.2. Retweet information cascades

To investigate the role of coordinated accounts in spreading information, we first need to construct the information cascades themselves. The easiest way to spread a message on Twitter is through the retweet action. Thus, on Twitter, information cascades can be studied by leveraging retweet graphs. The Twitter API service provides detailed information about each tweet (e.g., engagement values, user information), but it does not provide enough information to automatically reconstruct retweet graphs. Therefore, given a use who retweeted a tweet, it is not possible to determine with certainty from which other node of the graph the user saw and retweeted the tweet. To solve this limitation and to infer the full propagation structure of a tweet, we follow the well-known approach proposed in [56] that derives the retweet graph based on the social network of each user and on the retweet timestamps. In detail, given a retweet $t _ { x }$ by user $u _ { x }$ , of an original tweet $t _ { 0 }$ by user $u _ { 0 }$ , the retweeting user $u _ { x }$ might have either retweeted the original tweet $t _ { 0 } .$ , or another retweet $t _ { i }$ of $t _ { 0 }$ posted by one of his/her friends $( u _ { i } )$ before him/her. Thus, $0 \leq i < x$ . To identify the user from which $u _ { x }$ retweeted, [56] proposes to select the one that posted/retweeted $t _ { 0 }$ most recently before $u _ { x }$ , thus leveraging the publication timestamp of the original tweet $t _ { 0 }$ and those of all other retweets $t _ { i }$ of $t _ { 0 }$ published before $t _ { x }$ . Notably, information about the social network and the timestamps are available from the Twitter APIs. The simplicity of this method for reconstructing retweet graphs made it one of the most widely used in recent literature [46]

Once reconstructed, the retweet graph C is defined as a directed graph $C = ( V , E )$ , where each node $u \in V$ represents a user u and an edge $( u , v ) \in E$ represents a link from user u to user v. The graph C is not necessarily weakly connected since some groups of interconnected nodes or singletons could be disconnected from the largest connected component of $C - \mathrm { i . e . }$ , from the largest subgraph of C made up of interconnected nodes. The largest connected component of $C ,$ , called $C ^ { \prime } = ( V ^ { \prime } , E ^ { \prime } )$ , is a directed tree having as root node r the user $u _ { 0 }$ – that is, the original author of the tweet $t _ { 0 }$ retweeted by all other nodes in V . The subset of V made up of nodes that do not belong to $V ^ { \prime }$ is called S. Users in S are those who retweeted the post of $r$ by reading it either from the Twitter trends or by using the keyword search function. Obviously, if S is an empty set then $C \equiv C ^ { \prime }$

Once obtained the retweet graph, it is possible to compute several global metrics, listed below.

• Cascade size: the number of nodes in the information cascade C. The cascade size is denoted as $s = \vert C \vert = \vert C ^ { \prime } \vert + \vert S \vert$ , where $| \cdot |$ is the cardinality of the considered set. Accordingly, the size of $C ^ { \prime }$ is denoted as $s ^ { \prime } = | C ^ { \prime } |$

• Cascade edges: the number of edges in the information cascade $C .$ . The cascade edges are denoted by their count $m = | E |$ . Accordingly, the cascade edges in $C ^ { \prime }$ are denoted as $m ^ { \prime } = | C ^ { \prime } | - 1 = s ^ { \prime } - 1$ whereas the latter equality derives from the definition of tree graph.

• Cascade height: the length of the longest path going from r to any other node in $C ^ { \prime }$ . More intuitively, the cascade height $h ^ { \prime }$ can be thought of as the number of levels in the cascade assuming that the root node is at level 0, the nodes at distance 1 from the root are at level 1, and so on. The cascade height $h ^ { \prime }$ measures the extent to which a tweet was able to reach users far from the root’s ego network.

Alongside macro measures related to $C$ and $C ^ { \prime }$ , we can introduce other measures at node-level and edge-level. The nodal measures that we take into account are:

• Node positioning level: given the node $u \in V ^ { \prime }$ , its positioning level $l _ { u } ^ { \prime }$ is an integer number that quantifies its distance from the root r.

• Node action delay: the action delay $a _ { u } ^ { \scriptscriptstyle \mathrm { < } }$ denotes the number of minutes passed since the original tweet posting time and the node u retweet time.

• Node descendants: the number of links outgoing from node u. This measure is also known as node out-degree $k _ { u } ^ { o u t }$

The edge-level measures can be obtained using counts of edge types deriving from the node classification into coordinated and non-coordinated ones. Similar binary classifications of nodes and edges have been used also in [57, 58]. Given the information cascade $C = ( V , E )$ , the nodes in V that define the cascade size s can be divided into two subsets, the set of coordinated ones of cardinality $s _ { c }$ and the set of non-coordinated ones of cardinality $s _ { n }$ . Obviously, $s = s _ { c } + s _ { n }$ . We define coordinated to coordinated edges the set of edges connecting couples of coordinated nodes. The cardinality of such a set is $m _ { c c } .$ . Similarly, we define coordinated and non-coordinated edges, the set of edges between couples of coordinated to non-coordinated nodes. The cardinality of such a set is $m _ { c n }$ and $m _ { c n } = m _ { n c }$ . Finally, we define non-coordinated to noncoordinated edges, the set of edges connecting couples of non-coordinated nodes. The cardinality of such a set is $m _ { n n }$ . Obviously, $m = m _ { c c } + m _ { c n } + m _ { n n }$ . An example of the classification of nodes and edges is displayed in Figure 1. Accordingly, the tree represented in Figure 2 has $s _ { c } = 7 , s _ { n } = 1 6 , m _ { c c } = 4 , m _ { c n } = 8$ and $m _ { n n } = 1 0$

![](/api/attachments/E74QPJCY/fulltext/images/af0953419d0f4e79beeca6aba35e0c6af10a2d8885cad843bc2d31ea8d42f628.jpg)  
Figure 1: Node and edge types. A red node is a coordinated one (c) while a white node is a non-coordinated node (nc) Consequently, there are three types of edges: (c – c), (c – nc) and $( { \mathrm { n c } } - { \mathrm { n c } } )$ . Node counts are refereed to as $s _ { c }$ and $s _ { n } .$ , while edge counts are referred to as $m _ { c c } , m _ { c n }$ and $m _ { n n }$

## 4.3. Accounts’ Infectivity ratios

Given the features assigned for each node $u \in V$ , we introduce two novel metrics to measure the impact of coordinated users in spreading information along the cascade. The two metrics are respectively called coordinated accounts infectivity ratio $\left( \mathrm { C } _ { I R } \right)$ and coordinated to non-coordinated accounts infectivity ratio $\left( \mathrm { C t N C } _ { I R } \right)$

In particular, the $\mathrm { C } _ { I R }$ counts what proportion of nodes in the cascade depends, in a topological sense, on coordinated nodes. In other words, $\mathrm { C } _ { I R }$ counts the proportion of nodes no longer reachable from the roo r of $C ^ { \prime } .$ , after removing the coordinated nodes from the cascade (counting the coordinated nodes as well). The $\mathrm { C t N C } _ { I R }$ follows the same rationale of $\mathrm { C } _ { I R }$ , but it excludes coordinated nodes from the count. As such, it is more representative of the efect that removing coordinated accounts has on non-coordinated ones (i.e., unaware social media users). An example of both measures is reported in Figure 2.

![](/api/attachments/E74QPJCY/fulltext/images/0776908a85e4e02de411c6f28e9dc2901df76bf485c3e0dd16e1b9b9736d034c.jpg)  
Figure 2: Example of $\mathrm { C } _ { I R }$ and $\mathrm { C t N C } _ { I R }$ metrics

In the following we provide the procedure to compute the two aforementioned metrics.

1. Consider a cascade C rooted in the node r.

2. Sort the coordinated nodes by increasing distance from the root r (nodes disconnected from the largest connected component and with no incoming links are assumed to be at distance 1 from the root).

3. Choose the induced subgraph having as root node the coordinated node at the minimum distance from the root r.

4. Count the number of nodes in the subgraph excluding its root and store such a count in a vector called $v _ { C } ~ ( \mathrm { C } _ { I R } ~ \mathrm { c a s e } )$

5. Count the number of non-coordinated nodes in the subgraph excluding its root and store such a count in a vector called $v _ { C t N C } ~ ( \mathrm { C t N C } _ { I R } ~ \mathrm { c a s e } )$

6. Remove from C all the nodes in the subgraph.

7. Iterate Step 3 to Step 6 until there are no more coordinated nodes in C.

8. Sum over the elements of v and divide the sum by s − 1 to obtain $\mathrm { C } _ { I R }$

9. Sum over the elements of $v _ { C t N C }$ and divide the sum by $s - s _ { c } - 1$ to obtain $\mathrm { C t N C } _ { I R }$

## 5. Results

Based on the definitions and the metrics previously introduced, in this section we report and discuss the results of our analyses.

## 5.1. Coordination-based diference in information spreading

In order to understand if coordinated accounts difer from non-coordinated ones in their retweeting behavior, we perform a statistical analysis of the node-level measures introduced in Section 4.

Figure 3 reports the kernel density estimations of the distributions of nodes’ positioning level, action delay, and descendants count, respectively. Such densities are obtained using average values computed across 50,000 bootstrap samples on both coordinated and non-coordinated sets of nodes (summary statistics and diferences in the distributions are reported in Table 4). The reason behind using bootstrap samples is that of smoothing out the disproportion in the number of coordinated and non-coordinated accounts (as also reported in Table 3). Figure $\mathrm { 3 ( a ) }$ displays a small but significant diference for what concerns the level occupied by coordinated and non-coordinated accounts in the retweet cascade. Indeed, the former group occupies, on average, higher levels meaning that coordinated accounts tend to be closer to the root of the cascade. Accordingly, Figure 3(b) shows that coordinated accounts are much faster in retweeting information, as shown by the significantly lower action delay.

(a)  
![](/api/attachments/E74QPJCY/fulltext/images/511c76b9070b8c4baa6547e640a99ff50958ded1da463754d5066f2a73968822.jpg)

![](/api/attachments/E74QPJCY/fulltext/images/19bf2ebbb3ab725f9adc9d68dbdb4d58db0b05e30079a2a1d2f1dfa6a2ac5e53.jpg)

(c)  
![](/api/attachments/E74QPJCY/fulltext/images/030c8083fe296b0394b18f82ad2c264da94079d45b23a15c67cb6e2d03944f34.jpg)  
Figure 3: Distribution of node-level features for coordinated and non-coordinated accounts.

Analyzing Figure 3(c), it may be noticed that the two sets of users have a similar average number of descendants but, overall, we find that the two distributions difer. In particular, coordinated accounts display a right-skewed distribution of descendent count, thus being able to attract a higher number of descendants nodes, that is, the observed diference is mostly due to the right tail that characterize the descendent count distribution of coordinated accounts. For all the considered measures we find a statistically significant diference between the two sets of users. In summary, our results suggest a remarkable diference in the way information is spread by coordinated and non-coordinated accounts.

Our results also provide useful information about the diference between coordinated and merely active accounts. We remark that all accounts considered in our work were extremely active during the data collection period, since we specifically focused our analyses on superspreaders – that is, the top-1% of users who shared the most retweets in the run up to the 2019 UK general election. However, in spite of the fact that all users in our dataset were very active accounts, not all of them were coordinated, as demonstrated by our analyses. In other words, being very active does not necessarily imply being coordinated. In terms of our analyses and results, this means that there are many accounts that are very active and that often lay near the root of the information cascades to which they participate, but that are not coordinated. In turn, this suggests that coordination and “activeness” are two related, yet distinct, phenomena, which also motivates the recent interest in studying online coordination. More specifically, coordination is a stronger condition than simple “activeness”, since it mandates that an account is active, but also that its activity is done in a somewhat synchronized way with the activity of other accounts.

<table><tr><td rowspan="2"></td><td colspan="5">Coordinated</td><td colspan="5">Non-Coordinated</td><td rowspan="2">Wilcoxon Test Significance</td></tr><tr><td>Mean</td><td>St Dev</td><td>Median</td><td>min</td><td>max</td><td>Mean</td><td>St Dev</td><td>Median</td><td>min</td><td>max</td></tr><tr><td>Positioning Level</td><td>1.26</td><td>0.01</td><td>1.26</td><td>1.22</td><td>1.31</td><td>1.56</td><td>0.01</td><td>1.56</td><td>1.53</td><td>1.58</td><td>*</td></tr><tr><td>Action Delay (minutes)</td><td>258.91</td><td>4.30</td><td>258.94</td><td>240.02</td><td>274.61</td><td>353.89</td><td>1.79</td><td>353.87</td><td>347.71</td><td>360.84</td><td>*</td></tr><tr><td>Descendent Count</td><td>0.61</td><td>0.12</td><td>0.59</td><td>0.37</td><td>1.53</td><td>0.53</td><td>0.04</td><td>0.53</td><td>0.42</td><td>0.69</td><td>*</td></tr></table>

Table 4: Descriptive statistics of bootstrap experiments. The diferences in the distributions of the considered measures are evaluated by means of the non-parametric Wilcoxon signed-rank test.

## 5.2. Influence of coordinated accounts on message outreach

Here, we investigate the relationship between the number of coordinated accounts involved in a message difusion process and the message outreach (i.e., the magnitude of the information cascade generated by the message). Therefore, we analyze the structure of the retweet cascades by means of three measures, the cascade size, the cascade edges and the cascade height. Such measures are considered as covariates with respect to the incidence (i.e., the proportion) of coordinated accounts in the retweet cascade.

Qualitative results, reported in Figure 4, show structural features of the cascades (in terms of nodes, edges and height) on the x axis and the incidence of coordinated accounts (i.e., the fraction between coordinated nodes over all nodes in a cascade) on the y axis. Colors indicate the number of cascades lying in the plots diferent areas, highlighting that large cascades are rare with respect to smaller ones. This first finding from our dataset supports previous results about information difusion on Twitter [15, 59]. Next, by comparing the actual placement of coordinated accounts (Figure 4 (a), (b) and (c)) with that obtained via a null model that randomizes the node labels while fixing their proportions (Figure 4 (e), (f) and (g)), we find that coordinated accounts are present mostly in small cascades. In other words, the bigger the viral process, the smaller the likelihood of their efect. This result suggests that the use of coordinated accounts to alter information spreading works essentially only for the initial engagement of users within a cascade, and not for the later and deeper stages of the difusion process that are instead independent on the coordinated accounts and driven by spontaneous and unorganized user activity. This hypothesis is also supported and reinforced by our previous results on the placement of coordinated accounts within a cascade. Indeed, in Figure 3(a) we showed that coordinated accounts tend to reshare messages in the early stages of difusion, given that they lay relatively near to the root of the cascades.

![](/api/attachments/E74QPJCY/fulltext/images/55fd48e3ad00c6aec33adc56baa7bbf5f83a06c31fa03b344c365da090745856.jpg)

![](/api/attachments/E74QPJCY/fulltext/images/5f03a261ac25dc35a353c9efecf6d8ff512fb399f1cd7bd1c3553f85b1c240ed.jpg)

![](/api/attachments/E74QPJCY/fulltext/images/ea70f13b3131941b688ce74bb8aaedcd5bb6c05c024da5b4f774786065782cf8.jpg)

![](/api/attachments/E74QPJCY/fulltext/images/1cb0ac6a9598b673a6e1ea6ac3757d9f64bc241fb213e4ab42e1fcb4171a96ec.jpg)

![](/api/attachments/E74QPJCY/fulltext/images/e5143ba9b5e762a29cb0fa9105f3a318cc9bd158f98a0daf67c8ffa7feba0380.jpg)

![](/api/attachments/E74QPJCY/fulltext/images/8e911986c9c7a2f78a4874650aab2c5b06b86c63385475b207c0322beaa7af67.jpg)  
Figure 4: Incidence of Coordinated Account with respect to Size (left column), Edges (center column) and Height (right column) of retweets information cascades obtained for empirical data (top row) and null models (bottom row).

The findings reported in this section are fascinating in the context of the tactics used by coordinated accounts for altering information difusion. In fact, while several previous studies found that automated and coordinated accounts were used for re-sharing messages [43, 15, 60, 61, 62], little was known about how such accounts afected the information difusion process (which is instead seen from our results). When interpreting these results, care should also be taken about the expected impact of coordinated behavior as obtained by the implemented null model. In fact, panels (e) to (g) of Figure 4 show a relatively low incidence of coordinated accounts that might seem to indicate a rather weak or inefective efort. On the contrary, however, we remark that the typical goal of coordinated users is to convey their message to the largest possible number of unaware (and uncoordinated) users in the network. As such, positive results are related to large cascades having a relatively low incidence of coordinated users, rather than those with an extremely high incidence of coordinated users. In fact, the latter would mean that the message almost did not reach any user, apart from those already involved in the manipulation.

Finally, our results’ interpretation remarks an important challenge: the need to diferentiate between authentic and inauthentic activities. In fact, large cascades with a low incidence of coordinated accounts could result both from a successful manipulation activity (i.e., inauthentic behavior) and from an authenti grassroots initiative (possibly also involving a minority of coordinated accounts). Distinguishing between these two forms of online activity currently represents one of the important open issues in this field [19, 23].

## 5.3. Testing influence and targeting tactics of coordinated accounts

To better understand the dynamics of influence and targeting perpetrated by coordinated accounts, we analyze their infectivity ratios (i.e., their ability to involve other accounts in the spreading process) as well as the abundance of links with their targets in information cascades.

Infectivity ratios. We consider the two infectivity ratios, $\mathrm { C } _ { I R }$ and $\mathrm { C t N C } _ { I R }$ , introduced in Section 4.3. Such ratios count the proportion of nodes in the cascade that descend, directly or indirectly, from coordinated accounts. More precisely, the two measures are aimed at understanding which portion of the nodes in the cascade stems from the action of coordinated account $\left( \mathrm { C } _ { I R } \right)$ and which portion of non-coordinated accounts in the cascade stems from the action of coordinated accounts $\left( \mathrm { C t N C } _ { I R } \right)$

Panels (a) and (b) of Figure 5 show the coordinated accounts infectivity ratios by considering either all nodes $\left( \mathrm { C } _ { I R } \right)$ or only non-coordinated ones $\left( \mathrm { C t N C } _ { I R } \right)$ . Both panels display a very scattered dynamic, possibly more focused on low values of the index in the $\mathrm { C } _ { I R }$ case. In general, coordinated accounts do not seem to pursue an efective placement strategy, despite having a higher average position level (as shown in Section 5.1). Their removal, indeed, doesn’t systematically guarantee the structural collapse of the information cascade. Furthermore, the positioning of coordinated accounts is rarely efective regardless the cascade size.

Despite the scattered results of the infectivity ratios, a joint investigation of the distributions of the two indices provides interesting results. In Figure 6 we report some notable examples of cascades from our dataset. In figure, white nodes denote non-coordinated accounts while red nodes denote coordinated ones.

Details of Figure 6 are reported in Section 5.3 which shows four diferent relations between the two infection indices, resulting in the following observations:

• If $\mathrm { C } _ { I R } \longrightarrow 0 \& \mathrm { C t N C } _ { I R } \longrightarrow 0 \colon$ the cascade depends only on the root and coordinated nodes do not interfere in information spreading;

• If $\mathrm { C } _ { I R } \longrightarrow 1 \& \mathrm { C t N C } _ { I R } \longrightarrow 1$ : coordinated accounts play a key role in spreading information to non-coordinated accounts;

(a)  
![](/api/attachments/E74QPJCY/fulltext/images/6228dc938882c06bf746a74b77587b12f2921224ca3085516ae7c0d74b534f28.jpg)

![](/api/attachments/E74QPJCY/fulltext/images/63bfb39899ac93821b5a212dbe583eee7b05981ffadd620dfaf0d42227a63af6.jpg)

Figure 5: Infectivity ratios. Panel (a) displays the joint distribution of the Coordinated Infectivity Ratio $\left( \mathrm { C } _ { I R } \right)$ and the incidence of coordinated accounts. Panel (b) displays the joint distribution of the Coordinated to Non-Coordinated Infectivit Ratio $\left( \mathrm { C t N C } _ { I R } \right)$ and the incidence of coordinated accounts.

<table><tr><td>Cascade</td><td>Nodes Count</td><td>Coordinated Count</td><td> $C_{IR}$ </td><td> $CtNC_{IR}$ </td></tr><tr><td>a</td><td>5</td><td>3</td><td>0.25</td><td>1</td></tr><tr><td>b</td><td>16</td><td>2</td><td>0.93</td><td>1</td></tr><tr><td>c</td><td>20</td><td>16</td><td>0.37</td><td>0</td></tr><tr><td>d</td><td>911</td><td>108</td><td>0.82</td><td>0.82</td></tr></table>

Table 5: Cascades and Infection rates examples.

• If $\mathrm { C } _ { I R } \longrightarrow 0 \mathrm { ~ } \& \mathrm { C t N C } _ { I R } \longrightarrow 1$ : coordinated nodes are likely to be located next to the root of the tree and have few non-coordinated descendants. Such a case could be due mainly to finite size efects thus happening only in small cascades.

• If $\mathrm { C } _ { I R } \longrightarrow 1 \& \mathrm { C t N C } _ { I R } \longrightarrow 0 \mathrm { : }$ the coordinated nodes have descendants but those descendants are coordinated as well. Thus, the impact of coordinated accounts on unaware (i.e., non-coordinated) users is negligible.

This taxonomy and the examples in Figure 6 reveal interesting phenomena and highlight the usefulness of the two indices in providing a deeper understanding about the role and the impact of coordinated accounts. In addition to their theoretical value, these results also have practical implications. For instance, the $\mathrm { C } _ { I R }$ and $\mathrm { C t N C } _ { I R }$ indices allow distinguishing between coordinated manipulations that managed to influenc unaware (non-coordinated) users with those who did not. The former are particularly worthy of attention since, by influencing unaware users, they are likely to have serious consequences. When used in conjunction, the two indices would thus allow prioritizing moderation interventions by platform administrators wher they are most needed.

(a)  
![](/api/attachments/E74QPJCY/fulltext/images/9009a65ff53a675a4e2159c81cd05b7b349977bcadd7c550b0d00964c40e40e3.jpg)

(b)  
![](/api/attachments/E74QPJCY/fulltext/images/7b790caa24b796bbb6f709ae09810de8c18b1ec1b7b69efaf52b023dff42053d.jpg)

(c)  
![](/api/attachments/E74QPJCY/fulltext/images/ed27b238281e0a870a9a1ecbf53844370cfb2a0ef9412d22b754f9b4b461aad1.jpg)

(d)  
![](/api/attachments/E74QPJCY/fulltext/images/9ac9aec76efc91e9af2df17bc81cdcea568cb7c8e73752d9acc0c33f85056e37.jpg)  
Figure 6: Examples of cascades displaying peculiar cases of $\mathrm { C } _ { I R }$ and $\mathrm { C t N C } _ { I R }$ indexes. Coordinated nodes are depicted in red while non-coordinated nodes are depicted in white.

Link classification results. To further investigate the behavior of coordinated accounts we continue the analysis by performing the classification of edges into three diferent categories, as explained in Section 4.2. Figure 7 displays the distribution of the three types of edges: coordinated to coordinated (cc); coordinated to non-coordinated (cn); and non-coordinated to non-coordinated (nn). We mainly observe that across the whole set of cascades the largest proportion of links occurs between non-coordinated accounts while edges among coordinated accounts are quite rare. Nonetheless the two categories are well connected as witnessed by the distribution of the cn edges.

Moving forward, we also evaluate how the proportion of diferent edge types evolves with respect to the incidence of coordinated accounts within information cascades. Figure 8 displays the trends of edges incidence obtained by means of curve fitting. Panels (a) and (b) report somewhat expected results. The incidence of cc edges grows with the incidence of coordinated accounts (panel (a)), while the opposite trend can be found in the case of nn edges (panel (c)). Interestingly, the curve has a steeper trend in the latter case, indicating that links between non-coordinated accounts tend to decrease rapidly when the percentage of coordinated accounts grows, most likely because of a contextual growth of links between the two categories. Anyway, the most interesting result is that reported in Figure 8 (b) where we observe a somewhat linear growth of cn edges up to a saturation point that occurs at ∼ 50% (on both axes).

![](/api/attachments/E74QPJCY/fulltext/images/299b0e6ccda0acbef05b85d03e4c7118e8cb8f67edaf4bef0e8731676d98a0f8.jpg)  
Figure 7: Kernel density estimates for the distribution of incidence of edge types. Coordinated to coordinated edges are referred to as cc; coordinated to non-coordinated edges are referred to as cn; and non-coordinated to non-coordinated edges are referred to as nn.

The presence of a saturation point is confirmed by an appropriate fitting of an exponential model of the form $y \ = \ b ( 1 - e ^ { - a x } )$ . In such a model, parameter a (typically $a > 1 )$ determines the steepness of the exponential curve while parameter b is a scaling factor. By performing non-linear least-squares fitting we find that the best fitting values of the parameters are $a = 3 . 1 0 0$ and $b = 0 . 5 7 8$ with a residual standard error of 0.0732 (on 357 degrees of freedom). The other curves are more conveniently fitted using polynomial functions of the third order in the case of panel 8 (a) and of the fourth order in the case of panel 8 (c). The selection of polynomials’ order was made by means of ANOVA on nested models searching for the lowest order polynomial able to significantly explain the variance of the data, as explained in [63]. The two curves are modeled by the following equations $y = 0 . 9 7 4 - 1 . 2 0 8 x - 0 . 3 8 6 x ^ { 2 } + 0 . 7 5 6 x ^ { 3 }$ and $y = - 0 . 0 0 2 + 0 . 1 6 8 x - 1 . 1 1 2 x ^ { 2 } + 4 . 4 4 7 x ^ { 3 } - 3 . 2 9 1 x ^ { 4 }$ for which we find a residual standard error of 0.079 (on 355 degrees of freedom), and 0.068 (on 354 degrees of freedom) respectively.

In practice, the result concerning the saturation point indicates that the incidence of coordinated accounts and, in turn, their capacity to interact with, and to influence, non-coordinated ones, is efective only up to a certain threshold value that we identify at about 50% of the size of the cascade. Past that point, injecting other coordinated accounts in the network yields no additional benefits, in terms of their capacity to involve non-coordinated accounts in the cascade. In turn, this finding suggests that the targeted use of a limited number of coordinated accounts is a particularly efective manipulation tactic, while the employment of a large number of coordinated accounts appears to be ineficient and inefective, past the saturation point. Therefore, these results suggest that particular attention should be devoted to the detection of even small groups of coordinated accounts, which calls for the development of accurate and sensitive detectors to support the work of online moderators.

![](/api/attachments/E74QPJCY/fulltext/images/e242a23ab21ea7adf9c449b3916b78ae04cba9fe3a8c98f9532e90b7d4d5ba40.jpg)

![](/api/attachments/E74QPJCY/fulltext/images/c6090477a40bf1a455fd4acdd5a01bd18e9ee854ade1400823c3dfd9b42e76bf.jpg)  
Incidence of Coordinated Accounts

![](/api/attachments/E74QPJCY/fulltext/images/5900bbc174f269f9cfc983ce4a09b81c1e459cb127945d21a216676799654acc.jpg)  
Figure 8: Incidence of diferent edge types with respect to incidence of coordinated accounts. Panel (a) refers to edges among coordinated accounts; panel (b) refers to edges among coordinated and non-coordinated accounts; panel (c) refers to edges among non-coordinated accounts.

## 6. Research Implications

The results presented in this study have important implications in the characterization and contrast of coordinated inauthentic and harmful online behavior. In particular, the peculiar position and activity of coordinated accounts acting within an information cascade, which we highlighted in our work, could b used as further signals for diferentiating between authentic and inauthentic online coordination – an issue that is still largely unsolved [23, 19]. In practice, discovering further features that characterize coordinated accounts, beyond their exceptional similarity, could be part of the inputs used by decision support systems that aim at detecting online coordination and manipulated discussions. To this end, our results allowed to identify both node-level and cascade-level features. The identification of such features is an advancement with respect to the current scientific literature on this issue that, to our knowledge, is mainly focused on the development of coordination-detection algorithms [25]. Our results are thus orthogonal to the existing literature and could support current eforts for developing efective decision support systems for detecting and protecting against coordinated online information manipulations [24].

Another implication of our research involves the presence of a saturation process in the ability of coordinated accounts to involve non-coordinated ones. This indicates that even an imperfect detection of the number of coordinated accounts provides a rather precise estimate of the number of non-coordinated ones. Furthermore, the saturation process signals the inefectiveness of coordinated actions after a certain threshold value that starts at nearly a half of the cascade size. In turn, a better understanding of th tactics adopted for information manipulation, and their efectiveness, can contribute to prioritize and direct moderation interventions against the coordinated accounts and the manipulated discussions that have the potential of influencing a large number of unaware (non-coordinated) users.

Our work also opens additional research questions. In particular, our results highlighted the challenge of distinguishing between successful coordinated activities, which manage to infect large numbers of noncoordinated users, and non-coordinated activities. The latter, in fact, would appear similar to the former with respect to the number and incidence of coordinated accounts in the information cascade. This calls for additional research and experimentation.

## 7. Conclusions

In this work we have investigated the role of coordinated accounts in information spreading on Twitter considering the case of the 2019 UK political elections. In particular, we have considered a set of about 50,000 information cascades reconstructed using information deriving from the retweeting activity and from the follower/following network. Overall, we found a small but significant diference in the behavior of coordinated and non-coordinated accounts in terms of node-level measures, namely: positioning level, action delay and descendants count. Coordinated accounts tend to occupy higher positions in the information cascade, share information more rapidly and infect a higher number of users. Furthermore, their incidence in information cascades, especially of small size, seems to derive from strategic actions as confirmed by the departure of the real data from ad-hoc statistical null models. The presence of a strategy is consistent with the definition of coordinated accounts. We tested the ability of coordinated accounts in involving other users by means of novel indices (called infectivity ratios) and link classification in information cascades. In summary, the results of our analyses show that the ability of coordinated accounts to involve non-coordinated ones follows a saturation-like process characterized by a threshold after which injecting more coordinated accounts within a cascade yields negligible efects.

## References

[1] E. Bakshy, I. Rosenn, C. Marlow, L. Adamic, The role of social networks in information difusion, in: The 21st International Conference on World Wide Web (WWW’12), 2012, pp. 519–528.

[2] S. Flaxman, S. Goel, J. M. Rao, Filter bubbles, echo chambers, and online news consumption, Public Opinion Quarterly 80 (S1) (2016) 298–320.

[3] A. L. Schmidt, F. Zollo, M. Del Vicario, A. Bessi, A. Scala, G. Caldarelli, H. E. Stanley, W. Quattrociocchi, Anatomy of news consumption on Facebook, Proceedings of the National Academy of Sciences 114 (12) (2017) 3035–3039.

[4] L. Hagen, S. Neely, T. E. Keller, R. Scharf, F. E. Vasquez, Rise of the machines? examining the influence of social bots on a political discussion network, Social Science Computer Review (2020) 0894439320908190.

[5] A. Trujillo, S. Cresci, Make Reddit Great Again: Assessing community efects of moderation interventions on r/The Donald, arXiv preprint arXiv:2201.06455 (2022).

[6] E. Zinovyeva, W. K. H¨ardle, S. Lessmann, Antisocial online behavior detection using deep learning, Decision Suppor Systems 138 (2020) 113362.

[7] F. P. Santos, Y. Lelkes, S. A. Levin, Link recommendation algorithms and dynamics of polarization in online social networks, Proceedings of the National Academy of Sciences 118 (50) (2021).

[8] K. Hristakieva, S. Cresci, G. D. S. Martino, M. Conti, P. Nakov, The spread of propaganda by coordinated communities on social media, in: The 14th International ACM Web Science Conference (WebSci’22), ACM, 2022.

[9] M. Cinelli, S. Cresci, A. Galeazzi, W. Quattrociocchi, M. Tesconi, The limited reach of fake news on Twitter during 2019 European elections, PLoS ONE 15 (6) (2020) e0234689.

[10] H. Yuan, J. Zheng, Q. Ye, Y. Qian, Y. Zhang, Improving fake news detection with domain-adversarial and graph-attention neural network, Decision Support Systems (2021) 113633.

[11] M. Del Vicario, A. Bessi, F. Zollo, F. Petroni, A. Scala, G. Caldarelli, H. E. Stanley, W. Quattrociocchi, The spreading of misinformation online, Proceedings of the National Academy of Sciences 113 (3) (2016) 554–559.

[12] D. M. Lazer, M. A. Baum, Y. Benkler, A. J. Berinsky, K. M. Greenhill, F. Menczer, M. J. Metzger, B. Nyhan, G. Pennycook, D. Rothschild, M. Schudson, S. Sloman, C. Sunstein, E. A. Thorson, D. J. Watts, J. L. Zittrain, The science of fake news, Science 359 (6380) (2018) 1094–1096.

[13] X. Zhang, A. A. Ghorbani, An overview of online fake news: Characterization, detection, and discussion, Information Processing & Management 57 (2) (2020) 102025.

[14] C. Shao, G. L. Ciampaglia, O. Varol, K.-C. Yang, A. Flammini, F. Menczer, The spread of low-credibility content by social bots, Nature communications 9 (1) (2018) 1–9.

[15] M. Mendoza, M. Tesconi, S. Cresci, Bots in social and interaction networks: Detection and impact estimation, ACM Transactions on Information Systems 39 (1) (2020) 1–32.

[16] D. Boneh, A. J. Grotto, P. McDaniel, N. Papernot, How relevant is the turing test in the age of sophisbots?, IEEE Securit & Privacy 17 (6) (2019) 64–71.

[17] K. Starbird, Disinformation’s spread: bots, trolls and all of us, Nature 571 (7766) (2019) 449–450.

[18] J. Weedon, W. Nuland, A. Stamos, Information operations and Facebook, Tech. rep., Facebook (2017).

[19] L. Nizzoli, S. Tardelli, M. Avvenuti, S. Cresci, M. Tesconi, Coordinated behavior on social media in 2019 UK General Election, in: The 15th International AAAI Conference on Web and Social Media (ICWSM’21), AAAI, 2021.

[20] D. Pacheco, P.-M. Hui, C. Torres-Lugo, B. T. Truong, A. Flammini, F. Menczer, Uncovering coordinated networks on social media, in: The 15th International AAAI Conference on Web and Social Media (ICWSM’21), AAAI, 2021.

[21] S. N. Firdaus, C. Ding, A. Sadeghian, Retweet: A popular information difusion mechanism – a survey paper, Online Social Networks and Media 6 (2018) 26–40.

[22] X.-L. Ren, N. Gleinig, D. Helbing, N. Antulov-Fantulin, Generalized network dismantling, Proceedings of the National Academy of Sciences 116 (14) (2019) 6554–6559.

[23] L. Vargas, P. Emami, P. Traynor, On the detection of disinformation campaign activity with network analysis, in: Pro ceedings of the 2020 ACM SIGSAC Conference on Cloud Computing Security Workshop (SIGSAC’20), 2020, pp. 133–146.

[24] M. G. Lozano, J. Brynielsson, U. Franke, M. Rosell, E. Tj¨ornhammar, S. Varga, V. Vlassov, Veracity assessment of online data, Decision Support Systems 129 (2020) 113132.

[25] T. Magelinski, L. H. X. Ng, K. M. Carley, A synchronized action framework for responsible detection of coordination on social media, arXiv preprint arXiv:2105.07454 (2021).

[26] S. Tardelli, M. Avvenuti, M. Tesconi, S. Cresci, Detecting inorganic financial campaigns on Twitter, Information Systems (2021) 101769.

[27] M. Alassad, B. Spann, N. Agarwal, Combining advanced computational social science and graph theoretic techniques to reveal adversarial information operations, Information Processing & Management 58 (1) (2021) 102385.

[28] D. Weber, F. Neumann, Who’s in the gang? Revealing coordinating communities in social media, in: The 2020 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM’20), IEEE, 2020, pp. 89–93

[29] L. H. X. Ng, I. Cruickshank, K. M. Carley, Coordinating narratives and the capitol riots on parler, arXiv preprint arXiv:2109.00945 (2021).

[30] D. Schoch, F. B. Keller, S. Stier, J. Yang, Coordination patterns reveal online political astroturfing across the world, Scientific reports 12 (1) (2022) 1–10.

[31] F. Giglietto, N. Righetti, L. Rossi, G. Marino, It takes a village to manipulate the media: Coordinated link sharing behavior during 2018 and 2019 Italian elections, Information, Communication & Society 23 (6) (2020) 867–891.

[32] Y. Zhang, K. Sharma, Y. Liu, Vigdet: Knowledge informed neural temporal point process for coordination detection on social media, Advances in Neural Information Processing Systems (NeurIPS’21) 34 (2021).

[33] K. Sharma, Y. Zhang, E. Ferrara, Y. Liu, Identifying coordinated accounts on social media through hidden influence and group behaviours, in: The 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD’21), ACM, 2021, pp. 1441–1451.

[34] D. Weber, F. Neumann, Amplifying influence through coordinated behaviour in social networks, Social Network Analysis and Mining 11 (1) (2021) 1–42.

[35] E. Ferrara, O. Varol, C. Davis, F. Menczer, A. Flammini, The rise of social bots, Communications of the ACM 59 (7) (2016) 96–104.

[36] P. Fornacciari, M. Mordonini, A. Poggi, L. Sani, M. Tomaiuolo, A holistic system for troll detection on Twitter, Computers in Human Behavior 89 (2018) 258–268.

[37] S. Kang, X. J. Liu, Y. Kim, V. Yoon, Can bots help create knowledge? the efects of bot intervention in open collaboration, Decision Support Systems 148 (2021) 113601.

[38] M. Stella, E. Ferrara, M. De Domenico, Bots increase exposure to negative and inflammatory content in online socia systems, Proceedings of the National Academy of Sciences 115 (49) (2018) 12435–12440.

[39] S. Vosoughi, D. Roy, S. Aral, The spread of true and false news online, Science 359 (6380) (2018) 1146–1151.

[40] S. C. Woolley, Automating power: Social bot interference in global politics, First Monday (2016).

[41] M. Mirtaheri, S. Abu-El-Haija, F. Morstatter, G. Ver Steeg, A. Galstyan, Identifying and analyzing cryptocurrency manipulations in social media, IEEE Transactions on Computational Social Systems 8 (3) (2021) 607–617.

[42] X. Yuan, R. J. Schuchard, A. T. Crooks, Examining emergent communities and social bots within the polarized online vaccination debate in Twitter, Social Media+ Society 5 (3) (2019) 2056305119865465.

[43] M. Mazza, S. Cresci, M. Avvenuti, W. Quattrociocchi, M. Tesconi, RTbust: Exploiting temporal patterns for botnet detection on Twitter, in: The 11th International ACM Web Science Conference (WebSci’19), ACM, 2019, pp. 183–192.

[44] S. Cresci, M. Petrocchi, A. Spognardi, S. Tognazzi, From reaction to proaction: Unexplored ways to the detection of evolving spambots, in: Companion Proceedings of the The Web Conference 2018 (WWW’18), 2018, pp. 1469–1470.

[45] A. Rauchfleisch, J. Kaiser, The false positive problem of automatic bot detection in social science research, PLoS ONE 15 (10) (2020) 1–20.

[46] S. Vosoughi, M. N. Mohsenvand, D. Roy, Rumor gauge: Predicting the veracity of rumors on Twitter, ACM transactions on knowledge discovery from data (TKDD) 11 (4) (2017) 1–36.

[47] C. Yang, R. C. Harkreader, J. Zhang, S. Shin, G. Gu, Analyzing spammers’ social networks for fun and profit: a case study of cyber criminal ecosystem on Twitter, in: Proceedings of the 21st World Wide Web Conference (WWW’12),

ACM, 2012, pp. 71–80.

[48] T. Zaman, E. B. Fox, E. T. Bradlow, A bayesian approach for predicting the popularity of tweets, Annals of Applied Statistics 8 (3) (2014) 1583–1611.

[49] Q. Cao, H. Shen, K. Cen, W. Ouyang, X. Cheng, Deephawkes: Bridging the gap between prediction and understanding of information cascades, in: Proceedings of the 2017 Conference on Information and Knowledge Management (CIKM’17) ACM, 2017, pp. 1149–1158.

[50] R. Cazabet, N. Pervin, F. Toriumi, H. Takeda, Information difusion on Twitter: Everyone has its chance, but all chance are not equal, in: Proceedings of the 9th International Conference on Signal-Image Technology & Internet-Based Systems (SITIS’13), IEEE, 2013, pp. 483–490.

[51] I. Taxidou, P. M. Fischer, Online analysis of information difusion in Twitter, in: The 23rd International World Wide Web Conference (WWW’14), ACM, 2014, pp. 1313–1318.

[52] J. Yang, S. Counts, Predicting the speed, scale, and range of information difusion in Twitter, in: Proceedings of the International AAAI Conference on Web and Social Media (ICWSM’10), Vol. 4, 2010

[53] B. Wu, W.-H. Cheng, Y. Zhang, J. Cao, J. Li, T. Mei, Unlocking author power: On the exploitation of auxiliary author retweeter relations for predicting key retweeters, IEEE Transactions on Knowledge and Data Engineering 32 (3) (2018) 547–559.

[54] T. Rodrigues, T. Cunha, D. Ienco, P. Poncelet, C. Soares, RetweetPatterns: Detection of spatio-temporal patterns of retweets, in: New Advances in Information Systems and Technologies, Springer, 2016, pp. 879–888.

[55] P. Zola, G. Cola, M. Mazza, M. Tesconi, Interaction strength analysis to model retweet cascade graphs, Applied Sciences 10 (23) (2020) 8394.

[56] T. De Nies, I. Taxidou, A. Dimou, R. Verborgh, P. M. Fischer, E. Mannens, R. Van de Walle, Towards multi-level prove nance reconstruction of information difusion on social media, in: Proceedings of the 24th ACM International Conference on Information and Knowledge Management (CIKM’15), 2015, pp. 1823–1826.

[57] J. Park, A.-L. Barab´asi, Distribution of node characteristics in complex networks, Proceedings of the National Academy of Sciences 104 (46) (2007) 17916–17920.

[58] M. Cinelli, L. Peel, A. Iovanella, J.-C. Delvenne, Network constraints on the mixing patterns of binary node metadata Physical Review E 102 (6) (2020) 062310.

[59] C. Zang, P. Cui, C. Song, C. Faloutsos, W. Zhu, Quantifying structural patterns of information cascades, in: Proceedings of the 26th International Conference on World Wide Web Companion (WWW’17 Companion), 2017, pp. 867–868.

[60] M. Giatsoglou, D. Chatzakou, N. Shah, C. Faloutsos, A. Vakali, Retweeting activity on Twitter: Signs of deception, in: Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKKD’15), Springer, 2015, pp. 122–134.

[61] N. Vo, K. Lee, C. Cao, T. Tran, H. Choi, Revealing and detecting malicious retweeter groups, in: The 2017 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM’17), IEEE, 2017, pp. 363–368.

[62] S. Gupta, P. Kumaraguru, T. Chakraborty, Malreg: Detecting and analyzing malicious retweeter groups, in: Proceedings of the ACM India Joint International Conference on Data Science and Management of Data (CoDS-COMAD’19), 2019, pp. 61–69.

[63] G. James, D. Witten, T. Hastie, R. Tibshirani, An introduction to statistical learning, Vol. 112, Springer, 2013.
