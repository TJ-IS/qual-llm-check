---
otero_id: 13248
otero_key: "5RKD92HR"
title: "Listen to me — Evaluating the influence of micro-blogs"
authors: "Feng Li; Timon C. Du"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.03.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Feng Li <sup>a</sup>, Timon C. Du <sup>b,</sup>⁎

<sup>a</sup> School of Business Administration, South China University of Technology, Guangzhou 50640, China

<sup>b</sup> Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong, Hong Kong, Shatin, NT, Hong Kong

## a r t i c l e i n f o

Article history: Received 7 November 2012 Received in revised form 11 February 2014 Accepted 25 March 2014 Available online 3 April 2014

Keywords: Social networks Micro-blog Opinion leader Persuasiveness analysis

## a b s t r a c t

Social networks have become increasingly popular in recent years. Among the many social networking tools, micro-blogging is one of the most unique and convenient because it is short, responsive, spontaneous and mobile. These properties allow micro-blogs to move beyond basic information sharing and make them a popular media for sharing opinions. In this study, we examine the persuasiveness of micro-blogs by developing a framework that <sup>fi</sup>rst identi<sup>fi</sup>es opinion leaders and then analyzes their persuasiveness. To develop the framework, we download micro-blogs, blogger information and the relationships among them into a database, identify spammers, decompose communities into sub-nets, identify opinion leaders and conduct persuasiveness analyses. The results show the framework can identify opinion leaders and their opinions effectively. It was found that negative opinions are less persuasive than positive opinions, and positive opinion leaders are more aggressive in distributing positive messages than negative opinion leaders are in distributing negative messages.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Micro-blogs have gained tremendous popularity since their introduction in 2005, with the number of registered users growing exponentially. Twitter.com is the most successful example of a micro-blogging application. According to Twitter Counter, at 10:40 on July 9, 2011, the three most popular Twitter communities were Lady Gaga, Justin Bieber and President Barack Obama. On that date, those communities had 11,496,577, 10,888,22,1 and 9,042,215 followers (readers), respectively. Six months later, at 17:37 on February 26, 2012, the three most popular communities were Lady Gaga, Justin Bieber and Katy Perry with 19,656,282, 17,762,720 and 15,462,239 followers, respectively. On that same date, President Barack Obama had 12,702,110 followers and was ranked eighth. A micro-blog platform helped Lady Gaga to reach 19,656,282 followers by February 26, 2012, not counting ‘retweets’, which re-direct information to other communities. These <sup>fi</sup>gures suggest that the in<sup>fl</sup>uence of today's media has unlimited potential. Another notable example is how young NBA star, Jeremy Lin, was recently promoted. Lin was essentially unknown, but within two months became extremely popular, to the extent that Time magazine identi<sup>fi</sup>ed him as one of the world's most in<sup>fl</sup>uential people in 2012. In addition, Madison Square Garden, which owns the New York Knicks franchise, saw its stock jump 7%, which translates into \$170 million to the company's market cap (www.forbes.com). During Lin's promotion, Twitter proved such an effective media tool that “Linsanity” was tweeted 47,083 times during a Lakers game.

Many companies have noticed that viral marketing, such as word-ofmouth (WoM) marketing and social networking, is an advantageous strategy for distributing information and attracting clients [41]. WoM marketing is effective because it is not directly linked to the merchant. In the context of a social network, WoM marketing is even more appealing, because credibility can be easily and powerfully established within a trusted community. For example, CNN Breaking News, The New York Times and many other established entities use Twitter to build followings. Dell has posted coupons on Twitter, and uses the platform to communicate directly with customers by collecting feedback and responding to complaints [33]. Comcast has also designated an employee to deal with service complaints expressed on social networks [42].

When a social network becomes an effective media outlet through which to communicate with clients, one must then ask how companies can use this new platform to maximize their in<sup>fl</sup>uence on their clients. It is useful for companies to identify ways of distributing both positive and negative news persuasively using the new platform. A company must <sup>fi</sup>rst identify the opinion leader, his/her opinions and the extent of his/ her in<sup>fl</sup>uence within the community. An opinion leader is able to in<sup>fl</sup>uence the attitudes and/or behavior of others in a desired way [48]. In a social network, an opinion leader may be either an opinion initiator or a reviewer. He/she normally expresses strong opinions that are motivated by the desire for self-enhancement, the enjoyment gained from helping others, economic rewards, or other factors [49]. The social network becomes a recommendation system that aggregates and distributes opinions to its participants. Opinion leaders are central to the relationships within groups and networks, as well as to discussions of matters of general interest [32]. The extent of their centrality and prestige may indicate their in<sup>fl</sup>uence on these relationships and discussions [50].

From a technical perspective, this study treats a social network as a simple connected graph and identi<sup>fi</sup>es the initial node that distributes information to the maximum number of nodes. This involves (1) evaluating a node's contribution (a micro-blogger in the focused social network) to other nodes (other micro-bloggers in the community); (2) identifying the preferences and attitudes of the most in<sup>fl</sup>uential node (the opinion leader in the micro-blog community); and (3) appraising the opinion leader's in<sup>fl</sup>uence (persuasiveness analysis).

There are many types of platforms with different properties within a social network. For example, weblogs are effective for sharing information whereas micro-blogs are useful for gaining in<sup>fl</sup>uence, i.e., convincing others to accept opinions. This study proposes a framework to identify opinion leaders and analyze their in<sup>fl</sup>uence. We identify the in-<sup>fl</sup>uence of opinion leaders in a directed social network, speci<sup>fi</sup>cally through micro-blogs. To identify opinion leaders, we <sup>fi</sup>rst decompose a social network into sub-nets and then use the bloggers' properties, af-<sup>fi</sup>liations with and standings in certain communities for identi<sup>fi</sup>cation purposes. We then analyze the persuasiveness of positive and negative messages according to the different attitudes of opinion leaders.

The remainder of this paper is organized as follows. Section 2 reviews related works on micro-blogs. Section 3 presents the methodology and Section 4 provides the demonstration. Section 5 presents the discussion and concludes the study.

## 2. Related works

In the age of Web 2.0, social media has drawn a signi<sup>fi</sup>cant amount of attention, with micro-blogs generating particular interest among the various networking platforms. Micro-blogs, unlike weblogs, specialize in minimal content [11,21]. For example, a Twitter post is limited to 140 characters. Accordingly, micro-bloggers and their followers normally use mobile devices, such as phones and PDAs, to input and access information. In this way, opinions are not limited by time or space and those disseminating the information can broadcast their opinions anywhere and at any time.

## 2.1. The related literature of micro-blogs

Currently, there are two major research directions related to the study of micro-blogs. The <sup>fi</sup>rst focuses on the information content. For example, Naaman et al. [35] and Boyd et al. [4] noted that the most common micro-blog posts are related to the blogger's personal status (“me, now”), including statements, random thoughts, opinions/complaints and information sharing. It has also been noted that bloggers who continuously release excess information about their lives might subconsciously do so to appear more important [40]. Hughes and Palen [19] analyzed the characteristics of users who adopt micro-blogs in various scenarios and Ehrlich and Shami [9] studied the different uses of micro-blogs in the workplace. Morris et al. [34] compared user preferences in the adoption of micro-blogs rather than alternative media tools to acquire information, whereas Krishnamurthy et al. [27] explored the time factor related to geographical distribution using micro-blogs. Letierce et al. [31] and Honeycutt and Herring [17] analyzed the use of special emotion expressions in micro-blogs.

Micro-blogs have become a new, reliable platform from which information seekers can acquire useful content and information providers can release pro<sup>fi</sup>t-making messages [22]. For example, O'Connor et al. [39] found that the collected public opinion expressed through tweets is close to actual public political opinion. In another interesting observation, the use of three months of tweets about a movie provided a highly accurate prediction of the <sup>fi</sup>lm's box-of<sup>fi</sup>ce revenues [1]. Interestingly, in unexpected crisis situations such as the Southern California wild<sup>fi</sup>re in 2007, Hurricanes Gustav and Ike in 2008 and the <sup>fl</sup>ooding of the Red River Valley in 2009, Twitter became a back-channel media tool that provided more accurate information than its mainstream counterparts [45,46]. The timely nature of micro-blogs can give the information they disseminate higher value, such as in reporting earthquakes [43].

Micro-blog discussions can also assist in the collection of media responses, which can be very useful in situations such as presidential debates [7,44]. Jansen et al. [20] found that 20% of micro-bloggers evaluate actual products or brands (50% positive and 33% negative). One study noted that a negative micro-blog would cost a company 30 customers [11].

The second research direction is from the social network perspective. A study of the differences between micro-blogs and human social networks found signi<sup>fi</sup>cant deviation in the non-power-law follower distribution, the diameter length and the level of reciprocity [28]. Studies have shown that a completely different network topology is established in micro-blogs [51]. For instance, the nodes (users) within a network are associated by keywords or topics. The links (relationships) between nodes represent information sharing. Although a link between nodes establishes a follower–followee relationship, it cannot guarantee a direct relationship unless at least two posts have been issued [18]. Some network properties, such as scale-free [21] and longtailed [30] networks, have also been studied. Yardi and Boyd [52] found that micro-blog networks could be decomposed into sub-nets with clear geographical connections.

Research on micro-blog networking is still at an early stage, and although some studies have reported interesting <sup>fi</sup>ndings, a great deal remains to be explored. For example, the integration of two key research directions may enable researchers to explore relevant problem domains, such as the relative levels of in<sup>fl</sup>uence of users in social network. In brief, proponents of the <sup>fi</sup>rst research direction address information, preferences, political standing, geographical distribution and many other aspects with reference to individuals, whereas the second research approach involves examining community-based factors. In this study, we seek to determine how individuals, speci<sup>fi</sup>cally opinion leaders, exert their in<sup>fl</sup>uence over a social network, speci<sup>fi</sup>cally in the form of micro-blogs.

## 2.2. Influence maximization

In<sup>fl</sup>uence maximization is the process of identifying the nodes within a social network that can be used to maximize the distribution of in-<sup>fl</sup>uence [6,8]. One approach is to analyze the importance of nodes with higher in<sup>fl</sup>uence by acquiring factors such as the degree, closeness and betweenness centralities of the nodes. Kiss and Bichler [26] compared the in<sup>fl</sup>uence of different centralities on nodes and discovered that out-degree centrality is a simple and effective way to identify highly persuasive nodes. Java et al. [21] and Letierce et al. [31] found that some micro-blog nodes have the properties of the types of higher hubs and authorities typically seen on web pages. Kwak et al. [28] adopted the PageRank algorithm to rank the tweets and retweets on Twitter and found that they ranked very differently. Gayo-Avello [15] compared HITS, PageRank and other algorithms and determined that spammers do actually distort analysis results. Westerman et al. [51] also suggested that spammers be removed before analyzing the importance of network nodes. In our previous work, we also suggested criteria for evaluating the importance of weblogs in social networking [32].

An alternate research direction focuses on information dissemination [37]. For example, Kempe et al. [23] applied a heuristic greedy algorithm using the nodes' degrees and centrality to analyze two diffusion models: a linear threshold model and an independent cascade model. Similar work was conducted by Chen et al. [36] and Kimura et al. [24], who modi<sup>fi</sup>ed the Kempe et al. [23] approach to improve computational ef<sup>fi</sup>ciency. Galstyan et al. [14] analyzed the information dissemination in two different network structures, bi-community Erdos–Renyi graphs and scale-free graphs, and found that both the structural properties of the networks and their community structures had important implications for maximizing in<sup>fl</sup>uence. Goyal et al. [16] studied a probability model of information dissemination in the human social network.

As the micro-blog is short, mobile, and high in<sup>fl</sup>uential, it is important to trace the persuasiveness of opinion leaders by taking the information dissemination path and the ontological complexity into consideration. We adopt some of the ideas from previous studies on factors such as network decomposition, spammers and community structure in our micro-blog analysis.

## 3. Framework for extracting opinions from micro-blogs

The micro-blog is responsive and mobile, and provides a high level of penetration through opinion sharing. This study seeks to establish the persuasiveness of the micro-blog. However, as the messages posted are short, it is relatively dif<sup>fi</sup>cult to analyze the content. Thus, we <sup>fi</sup>rst identify the opinion leaders and then analyze their persuasiveness.

We propose a framework that includes four phases to identify the in-<sup>fl</sup>uence that opinion leaders exert within micro-blog communities by decomposing a social network into sub-nets to discover meaningful interactions among users; identifying the opinion leaders within these sub-nets by evaluating their in<sup>fl</sup>uence on other users; and analyzing persuasiveness by exploring the attitudes of the opinion leaders on designated issues.

Fig. 1 presents the four phases. Phase 1 is the preparation stage, during which we identi<sup>fi</sup>ed the focus community and retrieved data from micro-blog platforms such as Twitter. The retrieved data were stored in a blog's database for further analysis. This design allowed us to analyze the data by taking advantage of database tools. A blog database is used to store micro-blogs after a community has been identi<sup>fi</sup>ed. Database tools can be used to maintain, update, and manage blog messages. The identi<sup>fi</sup>cation of a community is based on the needs of system users. For example, an advertiser can either identify products or user groups before conducting word-of-mouth marketing. Once the online community had been identi<sup>fi</sup>ed and downloaded, we acquired published personal information on the members and the relationships among them. We used the keywords from the micro-blogs to locate related blogs outside the community. At the same time, we established an ontology database using the keywords; for instance, the keyword ‘Apple iPod’ included extensions such as ‘iPod nano’, ‘iPod shuf<sup>fl</sup>e’ and ‘iPod Touch’, along with the parent node ‘MP3 players’. Phase 2 was the message pre-processing stage, during which we identi<sup>fi</sup>ed spammers and noted member communication updates. One of the most important tasks in this stage was the decomposition of the community network into subnets because sub-nets reveal a higher intensity of communication among members compared with outsiders. Phase 3 evaluated the identities of the opinion leaders and their opinions within the sub-nets. This phase identi<sup>fi</sup>ed the opinion leader for each subnet and evaluated the tendencies of his/her opinions. Phase 4 assesses the effectiveness of information dissemination and message intensity. These recognized attitudes expressed by the opinion leaders were then used to examine the persuasiveness of the bloggers and their micro-blogs. Sections 3.1 to 3.3 will illustrate these phases in details.

## 3.1. Network preparation and decomposition

In phase 1, we <sup>fi</sup>rst used keywords to select a micro-blog community. We assumed that the members of a community have closer interaction through discussing the keyword topic compared with other communities. Although other communities might also mention the keyword topic, they are relatively less intensive and important. We then focused on the community and acquired the personal information and posted blogs of its members. We also used words that are semantically associated with the keywords in the ontology database to retrieve information in this phase. We then establish the follower–followee relationships among members. Note that the follower–followee relationship can indicate the path of message distribution better than the tweet– retweet relationship. For example, if A and B are follower and followee, then the blog posted by B can be seen by A. However, a tweet–retweet relationship is only established for a speci<sup>fi</sup>c occasion. This phase outputs a preliminary network.

![](/api/attachments/5RKD92HR/fulltext/images/df1ef9bb765d67556418f360e4a298e928a086ca53c1a499fa171c53a00e7db9.jpg)  
Fig. 1. Four-phase approach to extracting the most in<sup>fl</sup>uential blogger set.

In phase 2, before decomposing the initial network, we identi<sup>fi</sup>ed spammers because they reduce the effectiveness of media tools such as search engines, weblogs and micro-blogs. It is important to desensitize the effect of spammers on micro-blogs in the preparation stage because the content of spam within a micro-blog has clear characteristics. For example, its URLs link to external URLs and it has a certain number of hashtags and speci<sup>fi</sup>c types of keywords (such as ‘naked’, ‘girls’ or ‘webcam’) [2,49]. Similarly, as Benevenuto et al. [2], Yardi et al. [53] and Gayo-Avello [15] suggested, the behavioral characteristics of a spammer are revealed by a variety of factors, such as the duration patterns of user accounts, the total number of followers and followees, the fraction of followers per followees, the fraction of tweets that draws replies and the number of tweets to which the user replies.

Benevenuto et al. [2] suggested that such behavioral characteristics alone could provide satisfactory identi<sup>fi</sup>cation with 84.5% accuracy. Thus, to simplify the procedure we used behavioral characteristics rather than content to identify spammers. The criteria adopted for this study were the number of followees, the number of followers and the fraction of followers per followees. The last is based on the suggestion that spammers have more followers and followees. On average, a spammer has 1097 followees and 1230 followers compared with legitimate users (387 and 536, respectively) [53]. Gayo-Avello [15] found that a legitimate user has a fraction of followers per followees of no larger than 1, whereas the fraction is normally greater than 1 for a spammer. However, Yardi et al. [41] did not <sup>fi</sup>nd a signi<sup>fi</sup>cant difference. The fraction of followers per followees is obtained using Eq. (3), which is normalized and modi<sup>fi</sup>ed from Eq. (2) in Li and Du [32]:

$$
y _ {i} ^ {j} = \left(x _ {i} ^ {j} - x _ {i} ^ {\min}\right) / \left(x _ {i} ^ {\max} - x _ {i} ^ {\min}\right)\tag{1}
$$

$$
y _ {i} ^ {j} = 1 / \left[ 1 + \exp \left(- \left(x _ {i} ^ {j} - x _ {i} ^ {\text { avg }}\right) / x _ {i} ^ {\text { avg }} \right] \right.\tag{2}
$$

$$
y _ {i} ^ {j} = 1 / \left[ 1 + \exp \left(- \left(x _ {i} ^ {j} - x _ {i} ^ {\text { med }}\right) / x _ {i} ^ {\text { med }} \right] \right.\tag{3}
$$

where x<sup>j</sup> $( i = 1 , 2 , 3 )$ is index i at micro-blogger j; x<sup>j</sup> is the number of followees; y<sup>j</sup> is the value after normalization; and $\mathrm { \bar { \Phi } } _ { X _ { i } ^ { \operatorname * { m a x } } , X _ { i } ^ { \operatorname * { m i n } } , X _ { i } ^ { a \nu g } , X _ { i } ^ { m e d } }$ indicate the maximum, minimum, average and median of all of the microbloggers in index i, respectively. Eqs. (1) to (3) represent three different methods of data preprocessing by normalizing the original data into a range between 0 and 1. This normalization allowed us to ignore the problems caused by different unit formats and ranges and is a commonly adopted data preparation stage. To prevent extreme values from skewing the data distribution, we integrated Eq. (2), used in our previous work, into Eq. (3). A comparison of results using the different normalization procedures is provided below.

We used Support Vector Machine (SVM), a supervised learning algorithm that uses the training data set to form a hyper plane of a high dimensional space [3], for classi<sup>fi</sup>cation during the pre-processing stage. Speci<sup>fi</sup>cally, we used the C-support vector classi<sup>fi</sup>cation (C-SVC) and Radial Basis Function (RBF) of the SVM kernel function. Based on the classi<sup>fi</sup>ed results, we then removed the suspected spammers and cut the connections between them and other nodes.

In the next step we decomposed the network into sub-nets (subcommunities). Galstyan et al. [14] revealed that the structural properties of sub-nets are useful for understanding information distribution. After decomposition, the nodes in a sub-net have higher interaction properties than the rest of the nodes in the same network. Because a micro-blog is a directed network, we used modularity Q to evaluate the quality of decomposition, as Leicht and Newman [29] suggested. In brief, a modularity matrix was obtained using $\operatorname { E q . } \ ( 4 )$ to <sup>fi</sup>nd the most positive eigenvalue of the symmetric matrix $B + B ^ { T }$ and the corresponding eigenvector:

$$
Q = \frac {1}{4 \cdot \mathrm{m}} \cdot S ^ {T} (B + B ^ {T}) \cdot S\tag{4}
$$

$$
B _ {i j} = A _ {i j} - \left(k _ {i} ^ {i n} \cdot k _ {j} ^ {o u t}\right) / \mathrm{m}\tag{5}
$$

where m is the number of edges, $A _ { i j }$ is the adjacency matrix, $k _ { i } ^ { i n } , k _ { j } ^ { o u t }$ are the in- and out-degrees of nodes i and j, and the elements of matrix $S , s _ { i }$ is +1 if the node i is assigned to sub-net 1 and −1 if it is assigned to sub-net $2 , S ^ { T }$ is the transpose of a matrix S. Then, each node was assigned to one of two sub-nets based on the eigenvector and <sup>fi</sup>ne-tuned to maximize the modularity. The sub-net can be further decomposed using the generalized modularity matrix in Eq. (6),

$$
\Delta Q = \frac {1}{4 \cdot M} \cdot S ^ {T} \left(B ^ {(g)} + B ^ {(g) ^ {T}}\right) \cdot S\tag{6}
$$

where $B ^ { ( \mathbf { g } ) }$ is the sub-matrix of B. We put the pseudo-code for network splitting in Fig. 2 for illustration. The decomposition ends when the positive $\Delta Q$ cannot be found. However, because the <sup>fi</sup>ne-tuning step requires a time complexity of O(m!), we simpli<sup>fi</sup>ed it using a simulated annealing algorithm [25]. The pseudo-code of simulated annealing based <sup>fi</sup>ne-tuning algorithm is presented in Fig. 3. To illustrate, it includes: (1) Use the initial result $N _ { 0 } \left( N _ { t } , t = 0 \right)$ , i.e. the decomposition of nodes from matrix $S ,$ obtained from network decomposition as the initial trial solution for the simulated annealing algorithm. $N _ { 0 } [ j ] =$ $+ 1 / - 1$ represents two different communities, and the decomposition result for Q is $Q _ { 0 }$ (from Eq. (4)). The simulated annealing parameters include a temperature of $T _ { 0 }$ decreasing at a rate of λ. (2) Select a node j to change the af<sup>fi</sup>liated community, i.e., $N _ { t } [ j ] = - N _ { t - 1 } [ j ]$ , and compute $Q _ { t } .$ If $\begin{array} { r } { Q _ { t } \geq Q _ { t - 1 } , } \end{array}$ , then the candidate becomes the initiate solution to the next trial. Otherwise, the candidate is only accepted at a probability of $P ( a ) = \exp ( ( Q _ { t } - Q _ { t - 1 } ) / T _ { k } ) . ( 3 )$ ) Repeat the second step N times $( k = 1 , . . . , \Nu )$ with a temperature decrement rule of $\dot { { } } - T _ { k } = \lambda \cdot T _ { k - 1 } .$ (4) Repeat the second and third steps K times $( t = 1 , . . . , K )$ and keep the grouping with the highest Q as the solution. The time complexity is ${ \cal O } ( N * K )$ , which is irrelevant to the number of nodes m. The outputs from phase 2 are sub-nets that contain only closely related nodes.

## 3.2. Opinion leader identification

Phase 3 <sup>fi</sup>rst identi<sup>fi</sup>es the opinion leaders and then analyzes their opinions (positive/negative/neutral). We used eight indices (F1–F8) to identify opinion leaders, shown in Fig. 2, referring to [32].

## 3.2.1. The personal properties of bloggers

A blogger's published blogs (F1) are an indication of whether he/she is active, aggressive, willing to share, willing to engage and willing to in-<sup>fl</sup>uence, among other characteristics. In some cases, a blogger's personality can provide the inner motivation needed to become an opinion leader [47]. The number of followers/friends (F2) also indicates a blogger's in<sup>fl</sup>uence: the more followers/friends a blogger has, the greater the potential in<sup>fl</sup>uence they represent. A blogger's followees (F3) also provide useful information regarding the demand for a blogger's information, opinions, feedback and community involvement.

## 3.2.2. Community affiliations

When a blogger has a large number of followers in a speci<sup>fi</sup>c discussion group compared with the total number of followers he/she has in a network (F4), it indicates that the blogger has a closer af<sup>fi</sup>liation with and commitment to that group [5,38]. Similarly, when more followers

1) Use Equation (5) to obtain matrix B

2) Calculate the largest positive eigenvalue $V = \left[ \nu _ { i } \right]$ of the symmetric matrix $B + B ^ { T }$

3) Decompose network into two sub-net using $V , \ s _ { i } = \left\{ { + 1 , \nu _ { i } > 0 } \right.$ , i.e., s is +1 then the node is assigned

to sub-net 1 and assigned to sub-net 2 if -1. Using Simulated Annealing Based Fine-Tuning Algorithm for improvement.

4) Use Equation (4) to evaluate Q for the quality of decomposition.

5) Repeat steps 2 and 3 to all sub-nets G to further decompose into $G _ { 1 } ^ { s } , G _ { 2 } ^ { s }$

6) Use Equation (6) to calculate ∆Q for sub-nets. If $\Delta Q > 0$ , keep current results, i.e. decomposing

network G into $G _ { 1 } ^ { s } , G _ { 2 } ^ { s }$ ; and apply steps 5 and 6 to $G _ { 1 } ^ { s } , G _ { 2 } ^ { s }$ . Otherwise, stop decomposition

Fig. 2. Pseudo-code of network splitting algorithm.

depend on the blogger, he/she has a greater chance of becoming an opinion leader. When a blogger follows the other members in a speci<sup>fi</sup>c community more than the other communities in a speci<sup>fi</sup>c network, he/ she exhibits a high af<sup>fi</sup>liation with the community. This ratio is de<sup>fi</sup>ned as (F5), such that the higher the value, the closer the af<sup>fi</sup>liation.

## 3.2.3. The network properties of bloggers

If bloggers are at the core of a community, their opinions are significantly more in<sup>fl</sup>uential than those of others, to the extent that they can increase their in<sup>fl</sup>uence by taking advantage of their attitude. We followed Freeman [12] in using centrality/in-centrality (F6), betweenness centrality (F7) and closeness centrality (F8) to measure the structural centrality of a social network. These measurements have been shown to effectively identify the information diffusion of nodes within a social network [26]. This method of measuring nodes (bloggers) was adopted from graph theory.

of node i after pre-processing of Eq. (3) are obtained as follows. Node i dominates node j if all of the indices of i are higher than those of j, such that $N _ { i } \succ N _ { j }$ if and only i $\mathsf { f } \forall k \in \{ 1 , 2 , 4 , 6 , 7 , 8 \} , n _ { i } ^ { k } \geq n _ { j } ^ { k } , \forall l \in$ $\{ 3 , 5 \} , n _ { i } ^ { k } \le n _ { j } ^ { k }$ , and ∃ k ∈ {1, 2, 4, 6, 7, 8}, n<sup>k</sup> N n<sup>k</sup> or $\exists l \in \{ 3 , 5 \} , n _ { i } ^ { k } < n _ { j } ^ { k } .$ In addition, if node i dominates node j, it also means that node j is dominated by node i, such that $N _ { j } \prec N _ { i \cdot }$ If node i does not dominate node j, then $N _ { i } \approx N _ { j } ,$ if and only if node i cannot dominate node j, and node j cannot dominate node i. If there is a structural equivalence, i.e., two nodes are connected to the same other nodes, then there is no signi<sup>fi</sup>cant difference between the nodes. Thus, all of the nodes kept in the Pareto set were considered opinion leaders and were selected for further analysis.

Fig. 4 presents the hierarchical structure of indices, whereby higher values of F1, F2, F4, F6, F7 and F8 (in contrast to F3 and F5) indicate an increase in a blogger's chances of being the opinion leader. Here, we used all eight indices to identify the opinion leader. It is possible for a leader not to score higher on all of the indices than other members. Thus, determining a leader becomes a multi-attribute decision analysis problem. It is also possible to have more than one opinion leader in a network. When no dominant leader could be found, we used a Pareto set to accommodate all of the possible opinion leaders. In other words, one blogger may score higher on one index and lower on another, while the rest of the indices are equal compared with another blogger. In such a case, both were kept in the Pareto set. The indices (F1 to F8)

Once we identi<sup>fi</sup>ed the opinion leaders, we evaluated whether their opinions were positive, negative or neutral. To do this, we established a positive- and negative-sentiment word lexicons, following O'Connor et al. [39]. It should be noted that micro-blogs are not well written in Standard English. Spelling errors, slang and emoticon usage are common. Thus, we reserved a portion of the micro-blogs studied to set up the lexicon, which we then used to analyze the remaining microblogs. We further assumed that a micro-blog is considered positive if it contains positive words and negative if it contains negative words, with the knowledge that it is also possible for a micro-blog to be both positive and negative [39]. Finally, we de<sup>fi</sup>ned a blogger's opinion as positive if his/her aggregated number of positive micro-blogs was signi<sup>fi</sup>cantly higher than the related number of negative micro-blogs. Likewise, a blogger's opinion was considered negative if he/she exhibited a majority of negative micro-blogs, and neutral if no signi<sup>fi</sup>cant difference could be found.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1)  $N_{best}=N_{c}=N_{0};Q_{best}=Q_{c}=Q_{0};T=T_{0}; n=k=0;$ 
2) WHILE ( $k++&lt;K$ ) {
3) n=0;
4) WHILE ( $n++&lt;N$ ) {
5) j=random(1,m);  $N_{n}[j]=-N_{c}[j];$ 
6)  $Q_{n}=calculate(N_{n});$ 
7) IF ( $Q_{n}\geq Q_{c}$ )  $N_{c}:=N_{n},Q_{c}:=Q_{n};$ 
8) IF ( $Q_{n}\geq Q_{best}$ )  $N_{best}:=N_{n},Q_{best}:=Q_{n};$ 
9) IF ( $Q_{n}&lt;Q_{c}$  &amp;&amp;  $exp((Q_{n}-Q_{c})/T)\leq random(0,1)$ )  $N_{c}:=N_{n},Q_{c}:=Q_{n};$ 
10) }
11) T= $\lambda$ T;
12) }
13) RETURN  $N_{best};$
</div>

![](/api/attachments/5RKD92HR/fulltext/images/80c81b0513104b00939bb505802f9246a64f4cf516e1404f52115acb9e9d66f2.jpg)  
Fig. 4. Hierarchical feature system for opinion leader identi<sup>fi</sup>cation.

## 3.3. Persuasiveness analysis

Once we had identi<sup>fi</sup>ed the opinion leaders and their attitudes toward speci<sup>fi</sup>c issues, we analyzed the persuasiveness of their messages by considering the effectiveness of their information dissemination and message intensity. We used a simulated network to illustrate information dissemination and its effectiveness. Let the index x $\lvert ( i = 1 , . . . , 8 )$ and its intensity be $\alpha _ { i } ( \boldsymbol { \chi } _ { i } ^ { j } )$ . Based on the previous discussion, factors F1, F2 and F3 indicate the signi<sup>fi</sup>cant in<sup>fl</sup>uence of nodes disseminating information. For example, when F2 is higher, more followers can be attracted when a node makes a blog post. Similarly, F4 and F5 reveal associations with communities. For example, high F4 suggests that the blogger is loyal to a community and he/she is subsequently more willing to disseminate information. Thus, we refer to the information distribution model of Kiss and Bichler [26], which indicates that the probability of a node transmitting a message to n nodes through connected m nodes is a binomial distribution:

$$
P (n) = C _ {m} ^ {n} \cdot (\alpha_ {1} \cdot \alpha_ {2} \cdot \alpha_ {3} \cdot k) ^ {n} \cdot (1 - \alpha_ {1} \cdot \alpha_ {2} \cdot \alpha_ {3} \cdot k) ^ {m - n}\tag{7}
$$

where k is the effective communication probability between nodes, $\alpha _ { 1 } ,$ α , $\alpha _ { 3 }$ are the coef<sup>fi</sup>cients for spreading information, C<sup>n</sup> is the number of n-combinations (message sent) from a given set of m elements (total connected nodes) and $\begin{array} { r } { C _ { m } ^ { n } = \frac { m ! } { n ! \cdot ( m - n ) ! } . } \end{array}$ Note that when F1 and F2 are larger and F3 is smaller, the inclination to distribute information is higher.

$$
\alpha_ {i} \left(x _ {i} ^ {j}\right) = \left(1 - \frac {\varphi_ {i}}{2}\right) + \varphi_ {i} / \left(1 + e ^ {- \left(\frac {x _ {i} ^ {j} - x _ {i} ^ {m e d}}{x _ {i} ^ {m e d}}\right)}\right), (i = 1, 2)\tag{8}
$$

$$
\alpha_ {i} \left(x _ {i} ^ {j}\right) = \left(1 - \frac {\varphi_ {i}}{2}\right) + \varphi_ {i} / \left(1 + e ^ {\left(\frac {x _ {i} ^ {j} - x _ {i} ^ {m e d}}{x _ {i} ^ {m e d}}\right)}\right) (i = 3)\tag{9}
$$

where φ is the range of α and $\alpha _ { i } { \in } [ 1 - \frac { \varphi _ { i } } { 2 } , 1 + \frac { \varphi _ { i } } { 2 } ]$

The information intensity β exponentially decays during transmission at a rate of q, i.e., $\mathcal { B } = \alpha _ { 4 } \cdot \alpha _ { 5 } \cdot \tau ^ { q }$ where $\alpha _ { 4 }$ and α are the coef<sup>fi</sup>cients of information intensity in F4 and F5, respectively. Both $\alpha _ { 4 }$ and α are calculated similarly to $\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 }$ . Speci<sup>fi</sup>cally, $\alpha _ { 4 }$ uses Eq. (8) and $\alpha _ { 5 }$ uses Eq. (9). During the transmission, we adopt the argument in [26] that information will only be diverted when a blogger receives it. He/ she will not redirect a repeated message. However, the trust level increases when the message is received multiple times. If a message is received s times at node i, then $\sigma _ { i } = \sum _ { r = 1 } ^ { S } \beta _ { r }$ to resolve the impact of multiple messages to the same node. A threshold value ε is set, such that if $\sigma _ { i } > \varepsilon ,$ , then node i can receive the message. ω is another threshold value that limits the number of times each message can be passed to a node.

To consider blogger preferences, we de<sup>fi</sup>ned two parameters: λ and θ, where λ indicates that compared with a neutral blogger, the distribution of messages by a positive blogger has λ times the transmission intensity and θ indicates that a negative blogger has θ times the transmission intensity. That is, when λ is greater than 1, the positive blogger tends to distribute more information than the neutral blogger, whereas when λ is less than 1, the blogger has less interest in distributing the information. Similarly, if θ is larger than 1, then the negative blogger is more interested in distributing information than the neutral blogger, but is less interested if θ is less than 1. Note that normally, positive bloggers prefer to distribute positive messages while negative bloggers choose to distribute negative messages. Thus, both λ and θ represent the possibility of distributing messages. For example, $\mathrm { i f } \lambda = 0 . 7$ , node A (an opinion leader in the example below) has a 70% probability of passing the message to node B. Note that the effectiveness of information dissemination is measured by the number of bloggers who receive a message, compared with the total number of bloggers in the network.

## 4. Microblogs in Twitter for demonstration

To demonstrate, we developed a prototype using a Java platform (J2SE Development Kit 5.0) and the following tools: the Xerces2 Java parser 2.5.0 plug-in, to download web pages from the micro-blogs of interest and to conduct the analyses; the Colt 1.2.0 plug-in, to download data and the proceeding matrix analysis; and the LIBSVM plug-in for SVM analysis [10]. The downloaded data were stored in MySQL 4.1.

We chose Twitter.com as the targeted micro-blog site due to its signi<sup>fi</sup>cant popularity. We used the keyword ‘Apple’ to locate micro-blogs from http://search.twitter.com/. Based on the data set collected at 17:13 on August 19, 2010, we selected ‘appleincnews’ for demonstration. The ‘appleincnews’ account has 26,590 followers. We assumed that these users had a common interest in following updates from Apple and subsequently formed a community. We then used the API issued by Twitter.com to collect personal information, the relationships between followers and followees and related blogs (i.e., tweets) from http://dev.twitter.com/doc. Because Twitter.com has a rate limit on calls to its API of 150 requests per hour, per IP, and because some Twitter users opt to protect their personal information for authorized use (HTTP response code: 403 Forbidden; i.e., http://dev.twitter.com/ pages/responses\_errors), we successfully collected 26,211 useful personal information elements (379 of the Twitter users in the targeted community were unavailable) and 7,130,167 useful relationships between followers and followees.

Table 1  
Comparison of different normalized results in preprocess stage.

<table><tr><td></td><td>Iterations</td><td>The optimal objective value</td><td>Support vectors</td><td>Bounded support vectors</td><td>Total support vector</td><td>Accuracy</td></tr><tr><td>Raw Data</td><td>790</td><td>-46.4224</td><td>423</td><td>30</td><td>423</td><td>93.60%</td></tr><tr><td> $Linear^a$ </td><td>59</td><td>-59.9865</td><td>65</td><td>55</td><td>65</td><td>95.10%</td></tr><tr><td>Li and Du [32] $^b$ </td><td>111</td><td>-59.9991</td><td>87</td><td>50</td><td>87</td><td>94.93%</td></tr><tr><td>This  $study^c$ </td><td>113</td><td>-59.9996</td><td>100</td><td>51</td><td>100</td><td>95.82%</td></tr></table>

<sup>a</sup> Normalized using (1).  
<sup>b</sup> Normalized using (2).  
<sup>c</sup> Normalized using (3).

Next, as discussed in phase 2, we used SVM to identify spammers. One thousand bloggers were randomly chosen. The data from 500 of them were randomly selected to train SVM and 500 were kept for testing purposes. We repeated this process 100 times and report the averaged results. Table 1 shows the results of using the normalizing Eqs. (1), (2) and (3).

Eq. (3) produced higher accuracy (one-way ANOVA with $\digamma =$ 10.02088, P-value = 0.000306 and $\mathrm { F - c r i t i c a l } = 3 . 0 9 8 3 9 1 )$ , although more iterations were needed. The results were then used in supervised learning to classify the complete data set. After removing the spammers, we decomposed the network into sub-nets. We began by removing the isolated nodes and decomposing the remaining network into connected sub-nets. We considered sub-nets with less than 10 connected nodes as too small and thus removed the whole sub-net. Thus, 703 sub-nets involving 1752 nodes were removed in this step.

We then sorted the nodes based on the out-degree and calculated the Pearson correlation coef<sup>fi</sup>cient for the structural equivalence of the <sup>fi</sup>rst 50 nodes. The directed network had N nodes. In adjacency matrix A of the network, vectors $A _ { i } = ( a _ { i 1 } , a _ { i 2 } , . . . , a _ { i N } )$ and $A _ { j } = ( a _ { j 1 } , a _ { j 2 } ,$ $a _ { j N } )$ described the connection of nodes i and j to other nodes, respectively, such that $a _ { i k } = 1$ for $( k = 1 , . . . , N )$ if a directed arc connected node i to node k; otherwise, $a _ { i k } = 0 .$ Thus, the Pearson correlation coef<sup>fi</sup>cient between nodes i and j was calculated as

$$
r _ {i j} = \frac {\sum_ {k = 1} ^ {N} \left(a _ {i k} \cdot a _ {j k}\right) - \frac {1}{N} \cdot \sum_ {k = 1} ^ {N} a _ {i k} \cdot \sum_ {k = 1} ^ {N} a _ {j k}}{\sqrt {\left(\sum_ {k = 1} ^ {N} a _ {i k} ^ {2} - \frac {1}{N} \cdot \left(\sum_ {k = 1} ^ {N} a _ {i k}\right) ^ {2}\right) \cdot \left(\sum_ {k = 1} ^ {N} a _ {j k} ^ {2} - \frac {1}{N} \cdot \left(\sum_ {k = 1} ^ {N} a _ {j k}\right) ^ {2}\right)}}.\tag{10}
$$

The structural equivalence describes the degree of similarity between two connected nodes compared with others [13]. The outcome, with the threshold value set at 0.7, is presented in Table 2.

In Table 2, nodes 20, 26, 27, 33, 35, 47 and 48 exhibit higher structural equivalence (similarity). Nodes that scored lower than the threshold value are not listed. Referring to [26], if we simultaneously choose nodes 20, 26, 27, 33 and 35, or 47 and 48 as the source nodes, the number of nodes that can receive information will be much smaller than if we only chose one from each group. However, it should be noted that the network structure, speci<sup>fi</sup>cally structural equivalence, should be taken into account when choosing the source nodes. When the coef<sup>fi</sup>cient of two nodes is too high, it is likely that they belong to the same sub-nets and they should not both be chosen as source nodes. We use Fig. 5 to further illustrate this concept. In Fig. 5, there are nine nodes that form two sub-nets. Node 1 can connect to nodes 2, 3, 4, 5 and 6, whereas node 2 can link to nodes 3, 4, 5 and 6. Meanwhile, node 7 can reach nodes 8 and 9. If the source nodes are selected solely by out-degree without considering structural equivalence, nodes 1 and 2 will be chosen. However, choosing these two nodes results in nodes 1, 2, 3, 4, 5 and 6 being the reached nodes rather than the other sub-net. Using the Pearson correlation coef<sup>fi</sup>cient, because $A _ { 1 } = ( 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 )$ for node 1 and $A _ { 2 } =$ (0,1,1,1,1,1,0,0,0) for node 2, the structural symmetry is 0.7906. Thus, we chose nodes 1 and 7 as the source nodes.

Table 2  
Pearson correlation coef<sup>fi</sup>cients of nodes, sorted by out-degrees.

<table><tr><td>Nodes</td><td>20</td><td>26</td><td>27</td><td>47</td><td>48</td></tr><tr><td>20</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>26</td><td>0.8772</td><td>1</td><td></td><td></td><td></td></tr><tr><td>27</td><td>0.7879</td><td>0.7711</td><td>1</td><td></td><td></td></tr><tr><td>33</td><td>0.6266</td><td>0.7893</td><td>0.8161</td><td></td><td></td></tr><tr><td>35</td><td></td><td></td><td>0.7512</td><td></td><td></td></tr><tr><td>47</td><td></td><td></td><td></td><td>1</td><td></td></tr><tr><td>48</td><td></td><td></td><td></td><td>0.7787</td><td>1</td></tr></table>

Regarding network decomposition, the parameters for simulated annealing were set at $T _ { 0 } = Q _ { 0 } / 2 , \lambda = 0 . 2 , N = 1 0 0 , K = 5 .$ . Table 3 compares the computation times and results for simulated annealing and [36] the <sup>fi</sup>ne-tuning of algorithms. Table 3 reveals that simulated annealing for <sup>fi</sup>ne-tuning performs better when there are many nodes (e.g., an improvement of 55% or more when there are more than 1,000 nodes). In addition, the decomposed network may have better ΔQ.

To clarify, we present a portion of the network decomposition outcome in Fig. 6 using the Kamada–Kawai method described in Pajek 2.03 (http://vlado.fmf.uni-lj.si/ pub/networks/pajek/). Fig. 6(a) shows the original network, with Fig. 6(b) and (c) showing the in-process network and Fig. 6(d) showing the <sup>fi</sup>nal network. Fig. 6(b) and (c) have more than one sub-net and Fig. 6(d) has a distinct one-star network. A clear opinion leader was identi<sup>fi</sup>ed in the <sup>fi</sup>nal network.

The next step is to analyze the opinions. To achieve this we used the API provided by Twitter to retrieve related micro-blogs, which were used to identify the opinion leader's attitude. Both the positive- and negative-sentiment word lexicons were adopted and we downloaded 5700 micro-blogs based on the de<sup>fi</sup>ned keywords for Apple news, including ‘Apple TV’, ‘iPad’, ‘iPhone’, ‘iPod’, ‘iPod nano’, ‘iPod shuf<sup>fl</sup>e’, ‘iTouch’, ‘iTunes’, ‘MacBook’, ‘MacBook Air’, ‘Macbook Pro’, ‘iMac’, ‘Mac mini’ and ‘Mac Pro’. Nineteen languages were used in these microblogs, including 3030 (53.16%) in English, 1002 (17.58%) in Japanese, 474 (8.31%) in Spanish and 458 (8.21%) in Portuguese. Further examination of the downloaded micro-blogs revealed that ‘iPod Shuf<sup>fl</sup>e’, ‘Apple TV’ and ‘MacBook’ were the most popular in English; ‘iTunes’, ‘MacBook Air’ and ‘iMac’ were the most popular in Japanese; ‘MacBook Pro’, ‘iPhone’ and ‘iPod’ were the most popular in Spanish; and ‘iTouch’, ‘iPad’ and ‘iPod nano’ were the most popular in Portugal. This suggests that bloggers in these countries were interested in different Apple products at the moment of download. Thus, we included English-only micro-blogs to prevent deviation from the focus. Of the 3030 English micro-blogs downloaded, we sampled 2190 for positive- and negative-sentiment words and used 840 for testing. We found that 1758 (80.27%) were neutral, 321 (14.66%) were positive and 111 (5.07%) were negative. Among all of the English micro-blogs, we identi-<sup>fi</sup>ed 402 positive-sentiment words and 126 negative-sentiment words. Ten of the most commonly used words are shown in Table 4.

![](/api/attachments/5RKD92HR/fulltext/images/5dedf1eb013aac8634c84672f4bdb9af38a5fc626a6aa4f729cf571ccb6f2c98.jpg)  
Fig. 5. Illustration of network structure.

Table 3  
Results with different <sup>fi</sup>ne-tuning algorithms. (The improvements are highlighted as bold <sup>fi</sup>gures).

<table><tr><td rowspan="2">No. of nodes</td><td colspan="2">Newman [36]</td><td colspan="2">Simulated annealing</td><td rowspan="2">Time reduced (%)</td></tr><tr><td>ΔQ</td><td>Times</td><td>ΔQ</td><td>Times</td></tr><tr><td>3861</td><td>0.1665</td><td>4 m59.16 s</td><td>0.1665</td><td>39.257 s</td><td>86.88</td></tr><tr><td>2980</td><td>0.1719</td><td>1 m44.39 s</td><td>0.1719</td><td>17.381</td><td>83.35</td></tr><tr><td>2853</td><td>0.1783</td><td>2 m0.391 s</td><td>0.1783</td><td>20.921 s</td><td>82.62</td></tr><tr><td>1727</td><td>0.2214</td><td>22.041 s</td><td>0.2217</td><td>6.484 s</td><td>70.58</td></tr><tr><td>1675</td><td>0.2399</td><td>18.532 s</td><td>0.2399</td><td>5.609 s</td><td>69.73</td></tr><tr><td>1305</td><td>0.2006</td><td>8.828 s</td><td>0.2006</td><td>3.297 s</td><td>62.65</td></tr><tr><td>1237</td><td>0.2136</td><td>11.313 s</td><td>0.2136</td><td>4.640 s</td><td>58.98</td></tr><tr><td>1126</td><td>0.2182</td><td>5.828 s</td><td>0.2182</td><td>2.579 s</td><td>55.75</td></tr><tr><td>881</td><td>0.2114</td><td>2.578 s</td><td>0.2114</td><td>1.469 s</td><td>43.02</td></tr><tr><td>578</td><td>0.1402</td><td>1.141 s</td><td>0.1431</td><td>1.000 s</td><td>12.36</td></tr><tr><td>498</td><td>0.2098</td><td>0.734 s</td><td>0.2125</td><td>0.734 s</td><td>0</td></tr><tr><td>490</td><td>0.2224</td><td>0.730 s</td><td>0.2224</td><td>0.704 s</td><td>3.56</td></tr><tr><td>383</td><td>0.2376</td><td>0.454 s</td><td>0.2376</td><td>0.328 s</td><td>27.75</td></tr></table>

The testing data were used to evaluate the sentiment word lexicons using two common performance measures: recall and precision. Note that the recall measure is the fraction of positive micro-blogs retrieved (Eq. (11)) and the precision measure is the fraction of the retrieved micro-blogs that were positive (Eq. (12)), assuming that the positive micro-blogs in the test data A were R and the actual ones were $R _ { a } .$

$$
\text { recall } = | R a | / | R |\tag{11}
$$

$$
p r e c i s i o n = | R | / | A |.\tag{12}
$$

![](/api/attachments/5RKD92HR/fulltext/images/b2f6f775cc9a558962b85618885f43e9186ef9987b06c554953e97af3bb93c57.jpg)

![](/api/attachments/5RKD92HR/fulltext/images/6efc37e353d142d535a6e6318ed72490c72439dd3c08eb2b6716b0a98f6afacd.jpg)  
a  
C

The demonstration revealed a recall of 83.64% and a precision of 70.51% for the positive micro-blogs, and a recall of 71.43% and a precision of 31.03% for the negative micro-blogs.

Note the following differences between micro-blogs and documents in the analysis.

(1) The informal use of abbreviations and verbal, slang and net terms were common in micro-blogs. Examples include ‘Wow’, ‘Woohoo’, ‘:-)’,‘:D’,‘:-(’, ‘(^\_^)’, ‘OMG’ (Oh my God) and ‘BB’ (BlackBerry smartphone).

(2) The expression in micro-blogs was simple and straightforward.

(3) Due to word limitations, a micro-blog post normally only discussed one issue. For example, “I bought a 16GB ipod touch today… Excited!!” or “How do I get rid of the songs on my ipod nano?” Complete or complex expressions were rare.

The word lexicons were set up to determine the attitudes of bloggers. Using a Pareto-optimal set searching algorithm with the threshold for the similarity of structural equivalence set at $\chi = 0 . 7 0$ bloggers with the highest scores in the sub-nets were selected as the nodes that initiated message dissemination if their attitudes were positive or neutral. The dissemination in our network followed the parameters in [26] simulated network, i.e., $k = 0 . 6 0 , \tau = 0 . 5 0 , \omega = 5 , \varepsilon = 0 . 0 5$ and $\begin{array} { r } { \varphi _ { 1 } = \varphi _ { 2 } = \varphi _ { 3 } = \varphi _ { 4 } = \varphi _ { 5 } = 0 . 1 0 , \lambda = 1 . 0 5 , \theta = 0 . 5 0 . } \end{array}$ . We replicated the analysis 500 times. The results, which are shown in Fig. 5, comprised between nodes suggested in [26] with the largest out-degree and the approach adopted in this study. EView 5.0 is used for presentation. The Quantile–Quantile in Fig. 7 shows that the results are normally distributed, which indicates that using 500 replications is suf<sup>fi</sup>cient.

We assume that if a blogger has a preference, he/she may be more willing to distribute information that is consistent with his/her attitude. In Tables 5 and 6, we compare the information distribution when the opinion leader has a preference against the case in which preference is not taken into consideration adopted in [26]. The neutral to positive attitude is presented in Table 5 and the neutral to negative attitude is presented in Table 6. It can be seen that the message dissemination in our simulation is better than [26] because the mean is higher, as shown in the ‘Improved’ column.

![](/api/attachments/5RKD92HR/fulltext/images/8ad5a27ea1cf5ac05c729dc5deaad2c061b46e3f8237f5baa2c0a35ab26bda3a.jpg)  
b

![](/api/attachments/5RKD92HR/fulltext/images/dad7e7356fc3d3b04d1203136d103244b724ee0a9fb8e2c49ff20284cbe48196.jpg)  
d  
Fig, 6. Follower-followee micro-blogger relationship network (a) the original network: (b) and (c) the in-process network: and (d) the final network

Table 4  
The top 10 words in the lexicon for ‘apple news’.

<table><tr><td>No.</td><td>Positive word</td><td>Examples (micro-blogs)</td><td>No.</td><td>Negative word</td><td>Examples (micro-blogs)</td></tr><tr><td>1</td><td>:)</td><td>Yayyy!! I finally purchased my Macbook Pro!:)</td><td>1</td><td>Damn</td><td>What is this, 1990? How do Macbook Pros not have an HDMI port? And also why should a graphic design major require one? I&#x27;m no damn hipster</td></tr><tr><td>2</td><td>love</td><td>I got apple tv it&#x27;s amazing!!! I love my apple</td><td>2</td><td>:(</td><td>I got a pop up saying I had a virus and that it would find it for me. stupid stupid stupid. apple knows about it::(</td></tr><tr><td>3</td><td>amazing</td><td>It&#x27;s so amazing how my itouch batt doesn&#x27;t die even though I keep using it...and not charging it.</td><td>3</td><td>silly</td><td>i had a dream that i was handling a macbook air. and now i wake up to this silly macbook pro.</td></tr><tr><td>4</td><td>awesome</td><td>Since I got macair I cant stop playing with it! So awesome</td><td>4</td><td>stupid</td><td>Got a ipad.. That&#x27;s shit stupids</td></tr><tr><td>5</td><td>cool</td><td>Just connected up our new Apple TV! So cool!</td><td>5</td><td>suck</td><td>Reason why apple tv sucks.. I have to convert all these</td></tr><tr><td>6</td><td>like</td><td>I&#x27;m liking the iPad I got from Apple.</td><td>6</td><td>mess</td><td>My Macbook Pro Keeps Messing Up On Me.?: I was on Facebook and all of a sudden my MacBook Pro made my page small...</td></tr><tr><td>7</td><td>:D</td><td>Woww! I just got a iPad!:D</td><td>7</td><td>fuck</td><td>dear my 17 inch macbook pro... you are heavy as fuck.... sigh</td></tr><tr><td>8</td><td>great</td><td>Iphone4 has a great screen! Use it to watch videos the easy way!</td><td>8</td><td>hate</td><td>I hate this iphone!! Like holyyy its takinn foreverrr toilet me tweet:(</td></tr><tr><td>9</td><td>proud</td><td>Proud owner of a MacBook Pro:)</td><td>9</td><td>shit</td><td>The iPhone is shit! Cost me £ 75 to replace, and wait from 2 pm till 10 pm to get it fixed:(</td></tr><tr><td>10</td><td>good</td><td>Good music and my macbook... all I really need</td><td>10</td><td>hassle</td><td>Music and video conversion for iphone is a hassle:(</td></tr></table>

Next, we used the simulation results to analyze the persuasiveness of the opinion leaders. For positive messages, when λ is greater than 1, positive bloggers (including opinion leaders) tend to distribute positive information, whereas negative bloggers (including opinion leaders) choose to ignore the message if θ is less than 1. Table 5 presents the simulation results from this study and [26] using various parameter combinations $( \varphi _ { 1 } , \varphi _ { 2 } , \varphi _ { 3 } , \varphi _ { 4 } , \varphi _ { 5 } , \lambda , \theta )$

It should be noted that the opinion leaders selected in [26] do not indicate their preference. That is, the opinion leaders selected in [26], set A in Table 5, and set B in Table 6 are different. The number represents the ratio of the numbers of nodes receiving the message in the community. Speci<sup>fi</sup>cally, observation 1 in Table 5 shows that the effectiveness of information dissemination improved by 23.94%, according to the proportion of nodes that received the message relative to the total number of nodes in the network (0.5079), compared with the proportion 0.4098 in [26]. This con<sup>fi</sup>rms that decomposing the network into sub-nets to identify the attitudes of the opinion leaders can improve the distribution effectiveness.

In Table 5, observations 2 to 12 show that changes in θ do not significantly affect the effectiveness of dissemination (from 0.5886 to 0.5888 when θ increase from 0.00 to 1.00). That is, the effect of negative bloggers distributing positive messages can be negligible. Observations 13 to 23 reveal that changing the parameter λ for positive bloggers signi<sup>fi</sup>cantly increases the effectiveness of dissemination (from 0.5881 to 0.6414 when λ increases from 1.00 to 1.50). That is, positive bloggers are more in<sup>fl</sup>uential when distributing positive information, hence λ is important to the effectiveness of information dissemination.

![](/api/attachments/5RKD92HR/fulltext/images/e3988c79d9b85d717780e610a6a94155ddc0103a2ff8a9d94ff64e8ac14a41f7.jpg)

<table><tr><td colspan="2">Series: BENCHMARKSample 1 500Observations 500</td></tr><tr><td>Mean</td><td>0.440380</td></tr><tr><td>Median</td><td>0.440572</td></tr><tr><td>Maximum</td><td>0.464701</td></tr><tr><td>Minimum</td><td>0.418677</td></tr><tr><td>Std. Dev.</td><td>0.007852</td></tr><tr><td>Skewness</td><td>0.030271</td></tr><tr><td>Kurtosis</td><td>2.951548</td></tr><tr><td>Jarque-Bera</td><td>0.125269</td></tr><tr><td>Probability</td><td>0.939287</td></tr></table>

![](/api/attachments/5RKD92HR/fulltext/images/2173615d04d02d9090d6239a44963cc131aeb96533845e38413eccb29e1d2fb8.jpg)

![](/api/attachments/5RKD92HR/fulltext/images/4bac4abbc4eb663bff6d9abb05600e7734c030a62b91ae7b12e79e73960c9607.jpg)

Theoretical Quantile-Quantile

<table><tr><td colspan="2">Series: OURS</td></tr><tr><td colspan="2">Sample 1 500</td></tr><tr><td colspan="2">Observations 500</td></tr><tr><td>Mean</td><td>0.588881</td></tr><tr><td>Median</td><td>0.588919</td></tr><tr><td>Maximum</td><td>0.615282</td></tr><tr><td>Minimum</td><td>0.563896</td></tr><tr><td>Std. Dev.</td><td>0.008762</td></tr><tr><td>Skewness</td><td>0.085832</td></tr><tr><td>Kurtosis</td><td>2.944427</td></tr><tr><td>Jarque-Bera</td><td>0.678267</td></tr><tr><td>Probability</td><td>0.712387</td></tr></table>

![](/api/attachments/5RKD92HR/fulltext/images/16d2d99b570f4d92b04e3cb942d0650b99cda53385bbec535b0b2cae45931576.jpg)  
Fig. 7. Comparison between this study and benchmarked approach in Kiss and Bichler [26].

Table 6  
Table 5  
Simulation results when distributing positive message. (The changes of θ and λ, and their impacts to the effectiveness of messages dissemination are highlighted.)

<table><tr><td>Observation</td><td> $(\varphi_1, \varphi_2, \varphi_3, \varphi_4, \varphi_5, \lambda, \theta)$ </td><td>This study (set A)</td><td>Kiss and Bichler [26]</td><td>Improved</td></tr><tr><td>1</td><td>(0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 1.00)</td><td>0.5079</td><td>0.4098</td><td>23.94%</td></tr><tr><td>2</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.00)</td><td>0.5886</td><td>0.4405</td><td>33.62%</td></tr><tr><td>3</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.10)</td><td>0.5884</td><td>0.4404</td><td>33.60%</td></tr><tr><td>4</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.20)</td><td>0.5892</td><td>0.4403</td><td>33.82%</td></tr><tr><td>5</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.30)</td><td>0.5894</td><td>0.4400</td><td>33.95%</td></tr><tr><td>6</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.40)</td><td>0.5884</td><td>0.4394</td><td>33.91%</td></tr><tr><td>7</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.50)</td><td>0.5889</td><td>0.4404</td><td>33.72%</td></tr><tr><td>8</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.60)</td><td>0.5885</td><td>0.4400</td><td>33.75%</td></tr><tr><td>9</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.70)</td><td>0.5887</td><td>0.4403</td><td>33.70%</td></tr><tr><td>10</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.80)</td><td>0.5887</td><td>0.4399</td><td>33.82%</td></tr><tr><td>11</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.90)</td><td>0.5889</td><td>0.4394</td><td>34.02%</td></tr><tr><td>12</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 1.00)</td><td>0.5888</td><td>0.4395</td><td>33.97%</td></tr><tr><td>13</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.00, 0.50)</td><td>0.5881</td><td>0.4397</td><td>33.75%</td></tr><tr><td>14</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.50)</td><td>0.5888</td><td>0.4403</td><td>33.73%</td></tr><tr><td>15</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.10, 0.50)</td><td>0.6106</td><td>0.4533</td><td>34.70%</td></tr><tr><td>16</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.15, 0.50)</td><td>0.6190</td><td>0.4685</td><td>32.12%</td></tr><tr><td>17</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.20, 0.50)</td><td>0.6267</td><td>0.4755</td><td>31.80%</td></tr><tr><td>18</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.25, 0.50)</td><td>0.6375</td><td>0.4903</td><td>30.02%</td></tr><tr><td>19</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.30, 0.50)</td><td>0.6387</td><td>0.4898</td><td>30.40%</td></tr><tr><td>20</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.35, 0.50)</td><td>0.6392</td><td>0.4914</td><td>30.08%</td></tr><tr><td>21</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.40, 0.50)</td><td>0.6406</td><td>0.4923</td><td>30.12%</td></tr><tr><td>22</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.45, 0.50)</td><td>0.6402</td><td>0.4927</td><td>29.93%</td></tr><tr><td>23</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.50, 0.50)</td><td>0.6414</td><td>0.4923</td><td>30.29%</td></tr></table>

Table 6 illustrates the results for the announcement of negative messages. The <sup>fi</sup>ndings are as follows. (1) The information distribution is improved by about 60% in our study (shown in the ‘Improved’ column). (2) Although the number of negative opinion leaders (5.07%) is generally less than the number of positive opinion leaders (14.66%), negative messages are still able to reach about 50% of the community's members. (3) If we compare observations 13 to 23 in Table 5 (positive opinion leaders distributing positive messages) with those in Table 6 (negative opinion leaders distributing negative messages), we can see that the former reach about 30% more members than the latter (e.g. 0.5881 in observation 13 of Table 5 versus 0.4561 in observation 1 of Table 6).

We then compare our approach with [26], using the original data set in which spammers have not been identi<sup>fi</sup>ed, the sub-community has not been decomposed, and opinion estimation has not been conducted. That is, the opinion leaders are selected from the nodes based merely on the number of followers in each network. Table 7 shows that when a positive message is distributed, the proposed framework can more accurately measure the effectiveness of dissemination than [26]. Table 8 displays similar results for the distribution of a negative message.

## 5. Discussion and conclusions

The aim of this study was to propose a framework to identify opinion leaders and to investigate the persuasiveness of opinion leaders in micro-blogs. To do so, we <sup>fi</sup>rst selected a community, decomposed the community network into subnets and identi<sup>fi</sup>ed an opinion leader. To identify the opinion leader, we used the personal properties of bloggers, their af<sup>fi</sup>liation with communities and their network properties. After identifying the opinion leaders, we analyzed their attitude in the community and then examined the persuasiveness of their opinions. The effectiveness of information dissemination was affected by the attitude of the opinion and also by the message itself.

As bloggers generally indicate a preference (positive, neutral or negative), messages can be considered as disseminating either positive news or negative news. In this study, we simulated the distribution of positive messages in Table 5 and negative messages in Table 6, following the proposed framework. We found that the preference of bloggers affected the distribution of their messages. For a company, selecting the right opinion leaders could in<sup>fl</sup>uence the distribution of positive or negative news in micro-blogs. However, although we found the distribution of positive messages to be more powerful than that of negatives messages, negative news still reached about 50% of the members in a micro-blogging community.

Another interesting issue is whether or not changing the attitude of a blogger can affect the dissemination of information. If this is feasible, a company can take advantage of a change in attitude to manage information distribution. We present two scenarios in Table 9. First, we tested the effect of changing the negative attitude of the opinion leaders to either neutral or positive when the message was positive, and then tested the same opinion leaders when the message was negative. We observe the following. (1) For positive messages, changing negative opinion leaders' attitudes to neutral is not worthwhile if the cost is high. However, changing their attitudes to positive can signi<sup>fi</sup>cantly enhance the effectiveness of information dissemination (from 0.6414 to 0.7242 in observation (1.50, 0.50)). (2) For negative messages, changing negative opinion leaders' attitudes to either neutral or positive decreases the distribution of negative information by about 10% (e.g. from 0.5012 to 0.4465 when neutral, and 0.4388 when positive (1.50, 0.50)).

Simulation results when distributing negative message. (The changes of θ are highlighted.)

<table><tr><td>Observation</td><td> $(\varphi_1, \varphi_2, \varphi_3, \varphi_4, \varphi_5, \lambda, \theta)$ </td><td>This study (set B)</td><td>Kiss and Bichler [26]</td><td>Improved</td></tr><tr><td>1</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.00)</td><td>0.4561</td><td>0.2801</td><td>62.83%</td></tr><tr><td>2</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.05)</td><td>0.4571</td><td>0.2805</td><td>62.96%</td></tr><tr><td>3</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.10)</td><td>0.4718</td><td>0.2938</td><td>60.58%</td></tr><tr><td>4</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.15)</td><td>0.4782</td><td>0.3015</td><td>58.61%</td></tr><tr><td>5</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.20)</td><td>0.4863</td><td>0.3076</td><td>58.09%</td></tr><tr><td>6</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.25)</td><td>0.4974</td><td>0.3099</td><td>60.50%</td></tr><tr><td>7</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.30)</td><td>0.4978</td><td>0.3121</td><td>59.50%</td></tr><tr><td>8</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.35)</td><td>0.5001</td><td>0.3130</td><td>59.78%</td></tr><tr><td>9</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.40)</td><td>0.5006</td><td>0.3134</td><td>59.73%</td></tr><tr><td>10</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.45)</td><td>0.5011</td><td>0.3133</td><td>59.94%</td></tr><tr><td>11</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.50)</td><td>0.5012</td><td>0.3131</td><td>60.08%</td></tr></table>

Table 7  
Simulation results for the distribution of a positive message without pre-processes. (The changes of θ and the effectiveness of messages dissemination are highlighted.)

<table><tr><td>Observation</td><td> $(\varphi_1, \varphi_2, \varphi_3, \varphi_4, \varphi_5, \lambda, \theta)$ </td><td>This study (set A)</td><td>Kiss and Bichler [26]</td><td>Improved</td></tr><tr><td>1</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.00, 0.50)</td><td>0.4823</td><td>0.2506</td><td>92.46%</td></tr><tr><td>2</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.05, 0.50)</td><td>0.4824</td><td>0.2511</td><td>92.11%</td></tr><tr><td>3</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.10, 0.50)</td><td>0.4873</td><td>0.2732</td><td>78.37%</td></tr><tr><td>4</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.15, 0.50)</td><td>0.4961</td><td>0.2854</td><td>73.83%</td></tr><tr><td>5</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.20, 0.50)</td><td>0.5010</td><td>0.3019</td><td>65.95%</td></tr><tr><td>6</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.25, 0.50)</td><td>0.5151</td><td>0.3185</td><td>61.73%</td></tr><tr><td>7</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.30, 0.50)</td><td>0.5152</td><td>0.3210</td><td>60.50%</td></tr><tr><td>8</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.35, 0.50)</td><td>0.5157</td><td>0.3210</td><td>60.65%</td></tr><tr><td>9</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.40, 0.50)</td><td>0.5157</td><td>0.3228</td><td>59.76%</td></tr><tr><td>10</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.45, 0.50)</td><td>0.5163</td><td>0.3226</td><td>60.04%</td></tr><tr><td>11</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 1.50, 0.50)</td><td>0.5160</td><td>0.3236</td><td>59.46%</td></tr></table>

Table 8  
Simulation results for the distribution of a negative message without pre-processes. (The changes of θ are highlighted.)

<table><tr><td>Observation</td><td> $(\varphi_1, \varphi_2, \varphi_3, \varphi_4, \varphi_5, \lambda, \theta)$ </td><td>This study (set B)</td><td>Kiss and Bichler [26]</td><td>Improved</td></tr><tr><td>1</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.00)</td><td>0.3487</td><td>0.2372</td><td>47.01%</td></tr><tr><td>2</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.05)</td><td>0.349</td><td>0.238</td><td>46.63%</td></tr><tr><td>3</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.10)</td><td>0.3633</td><td>0.2566</td><td>41.57%</td></tr><tr><td>4</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.15)</td><td>0.3705</td><td>0.2577</td><td>43.81%</td></tr><tr><td>5</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.20)</td><td>0.3744</td><td>0.2634</td><td>42.13%</td></tr><tr><td>6</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.25)</td><td>0.3801</td><td>0.2747</td><td>38.38%</td></tr><tr><td>7</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.30)</td><td>0.3803</td><td>0.2763</td><td>37.67%</td></tr><tr><td>8</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.35)</td><td>0.3808</td><td>0.277</td><td>37.49%</td></tr><tr><td>9</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.40)</td><td>0.3808</td><td>0.2781</td><td>36.92%</td></tr><tr><td>10</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.45)</td><td>0.3828</td><td>0.2786</td><td>37.43%</td></tr><tr><td>11</td><td>(0.10, 0.10, 0.10, 0.10, 0.10, 0.50, 1.50)</td><td>0.3825</td><td>0.2812</td><td>36.03%</td></tr></table>

In conclusion, social media has become increasingly well developed and accepted in recent years, with blogging gaining a great deal of popularity. The blogging platform provides a place for members to engage with and share opinions with a like-minded community. There are some basic differences between blogs and micro-blogs. For instance, a blog is mainly used to share information whereas a micro-blog is used to share opinions, probably because the word limitations on microblog posts require users to state their opinions concisely. This observation prompted us to explore the persuasiveness of micro-blogs. First, we propose a framework to identify the opinion leaders within microblog communities, and then analyzed their attitudes and the information distribution of positive and negative messages. Our results show that (1) the effectiveness of information distribution improves when considering the preferences of the opinion leaders; (2) negative opinions are relatively less persuasive than positive opinions, although negative opinions still reach about 50% of the members in the community; (3) positive opinion leaders are more aggressive in distributing positive messages than negative opinion leaders are in distributing negative messages; and (4) changing the attitude of negative opinion leaders to positive can improve the distribution of positive messages and suppress the distribution of negative messages by about 10%.

Table 9  
Simulation results of information dissemination for both positive and negative messages, i.e. (φ<sub>1</sub>, φ<sub>2</sub>, φ<sub>3</sub>, φ<sub>4</sub>, φ<sub>5</sub>) = (0.10, 0.10, 0.10, 0.10, 0.10). (The changes of θ and λ are highlighted.)

<table><tr><td colspan="4">Positive message</td><td colspan="4">Negative message</td></tr><tr><td>(λ,θ)</td><td>Negative</td><td>Neutral</td><td>Positive</td><td>(λ,θ)</td><td>Negative</td><td>Neutral</td><td>Positive</td></tr><tr><td>(1.00, 0.50)</td><td>0.5881</td><td>0.6291</td><td>0.6299</td><td>(0.50, 1.00)</td><td>0.4561</td><td>0.4109</td><td>0.4115</td></tr><tr><td>(1.05, 0.50)</td><td>0.5888</td><td>0.6289</td><td>0.6293</td><td>(0.50, 1.05)</td><td>0.4571</td><td>0.4111</td><td>0.4113</td></tr><tr><td>(1.10, 0.50)</td><td>0.6106</td><td>0.6435</td><td>0.7155</td><td>(0.50, 1.10)</td><td>0.4718</td><td>0.4206</td><td>0.4166</td></tr><tr><td>(1.15, 0.50)</td><td>0.6190</td><td>0.6426</td><td>0.7081</td><td>(0.50, 1.15)</td><td>0.4782</td><td>0.4279</td><td>0.4229</td></tr><tr><td>(1.20, 0.50)</td><td>0.6267</td><td>0.6447</td><td>0.7107</td><td>(0.50, 1.20)</td><td>0.4863</td><td>0.4361</td><td>0.4307</td></tr><tr><td>(1.25, 0.50)</td><td>0.6375</td><td>0.6496</td><td>0.7191</td><td>(0.50, 1.25)</td><td>0.4974</td><td>0.4460</td><td>0.4385</td></tr><tr><td>(1.30, 0.50)</td><td>0.6387</td><td>0.6513</td><td>0.7224</td><td>(0.50, 1.30)</td><td>0.4978</td><td>0.4462</td><td>0.4390</td></tr><tr><td>(1.35, 0.50)</td><td>0.6392</td><td>0.6506</td><td>0.7222</td><td>(0.50, 1.35)</td><td>0.5001</td><td>0.4461</td><td>0.4394</td></tr><tr><td>(1.40, 0.50)</td><td>0.6406</td><td>0.6516</td><td>0.7235</td><td>(0.50, 1.40)</td><td>0.5006</td><td>0.4461</td><td>0.4398</td></tr><tr><td>(1.45, 0.50)</td><td>0.6402</td><td>0.6510</td><td>0.7213</td><td>(0.50, 1.45)</td><td>0.5011</td><td>0.4460</td><td>0.4394</td></tr><tr><td>(1.50, 0.50)</td><td>0.6414</td><td>0.6532</td><td>0.7243</td><td>(0.50, 1.50)</td><td>0.5012</td><td>0.4465</td><td>0.4388</td></tr></table>

## Acknowledgment

This work was supported in part by the National Natural Science Foundation of China (No. 71171085 and No. 71101063).

## References

[1] S. Asur, B.A. Huberman, Predicting the future with social media, Proc. IEEE/WIC/ACM Int'l Conf. Web Intelligence and Intelligent Agent Technology (WI-IAT' 10), 2010, pp. 492–499.

[2] F. Benevenuto, G. Magno, T. Rodrigues, V. Almeida, Detecting spammers on Twitter, Proc. 7th Ann. Collaboration, Electronic Messaging, Anti-Abuse and Spam Conf. (CEAS 2010), 2010.

[3] C.J.C. Burges, A tutorial on support vector machines for pattern recognition, Data Mining and Knowledge Discovery 2 (1998) 121–167.

[4] D. Boyd, S. Golder, G. Lotan, Tweet, tweet, retweet: conversational aspects of retweeting on Twitter, Proc. Hawaii Int'l Conf. System Sciences (HICSS), 2010, pp. 1–10.

[5] L.V. Casalo, C. Flavian, M. Guinaliu, Relationship quality, community promotion and brand loyalty in virtual communities: evidence from free software communities, International Journal of Information Management 30 (4) (2010) 357–367.

[6] W. Chen, Y. Wang, S. Yang, Ef<sup>fi</sup>cient in<sup>fl</sup>uence maximization in social networks, Proc. 15th ACM SIGKDD Int'l Conf. Knowledge Discovery and Data Mining (KDD' 09), 2009, pp. 199–208.

[7] N.A. Diakopoulos, D.A. Shamma, Characterizing debate performance via aggregated Twitter sentiment, Proc. the 28th Int'l Conf. Human Factors in Computing Systems (CHI 2010), 2010, pp. 1195–1198.

[8] P. Domingos, M. Richardson, Mining the network value of customers, Proc. 7th ACM SIGKDD Int'l Conf. Knowledge Discovery and Data Mining (KDD' 01), 2001, pp. 57–66.

[9] K. Ehrlich, N.S. Shami, Microblogging inside and outside the workplace, Proc. Int'l AAAI Conf. Weblogs and Social Media (ICWSM 2010), 2010.

[10] R.E. Fan, P.H. Chen, C.J. Lin, Working set selection using second order information for training support vector machines, Journal of Machine Learning Research 6 (2005) 1889–1918.

[11] E. Fischer, A.R. Reuber, Social interaction via new social media: (how) can interactions on Twitter affect effectual thinking and behavior? Journal of Business Venturing 26 (2011) 1–18.

[12] L.C. Freeman, Centrality in social networks: conceptual clari<sup>fi</sup>cation, Social Networks 1 (3) (1979) 215–239.

[13] N.E. Friedkin, E.C. Johnsen, Social positions in in<sup>fl</sup>uence networks, Social Networks 19 (3) (1997) 209–222.

[14] A. Galstyan, V. Musoyan, P. Cohen, Maximizing in<sup>fl</sup>uence propagation in networks with community structure, Physical Review E 79 (5) (2009) 056102.

[15] D. Gayo-Avello, Nepotistic relationships in Twitter and their impact on rank prestige algorithms, Information Processing and Management 49 (6) (2013) 1250–1280.

[16] A. Goyal, F. Bonchi, L.V.S. Lakshmanan, Learning in<sup>fl</sup>uence probabilities in social networks Proc, 3rd ACM Int'l Conf, Web Search and Data Mining (WSDM' 10). 2010 pp. 241–250.

[17] C. Honeycutt, S.C. Herring, Beyond microblogging: conversation and collaboration via Twitter, Proc. Hawaii Int'l Conf. System Sciences (HICSS-42), 2009, pp. 1–10.

[18] B.A. Huberman, D.M. Romero, F. Wu, Social networks that matter: Twitter under the microscope, 2009. http://journals.uic.edu/ojs/index.php/fm/article/view/2317. Volume 14, Number 1-5 January 2009.

[19] A.L. Hughes, L. Palen, Twitter adoption and use in mass convergence and emergency events, International Journal of Emergency Management 6 (3/4) (2009) 248–260.

[20] B.J. Jansen, M. Zhang, K. Sobel, A. Chowdury, Twitter power: tweets as electronic word of mouth, Journal of the American Society for Information Science and Technology 60 (11) (2009) 2169–2188.

[21] A. Java, X. Song, T. Finin, B. Tseng, Why we Twitter: understanding microblogging usage and communities, Proc. ACM SIGKDD Int'l Conf. Knowledge Discovery and Data Mining (KDD), 2007, pp. 56–65.

[22] A.M. Kaplan, M. Haenlein, Users of the world, unite! The challenges and opportuni ties of social media, Business Horizons 53 (1) (2010) 59–68.

[23] D. Kempe, J. Kleinberg, E. Tardos, Maximizing the spread of in<sup>fl</sup>uence through a social network, Proc. 9th ACM SIGKDD Int'l Conf. Knowledge Discovery and Data Mining (KDD' 03), 2003, pp. 137–146.

[24] M. Kimura, K. Saito, R. Nakano, H. Motoda, Extracting in<sup>fl</sup>uential nodes on a social network for information diffusion, Data Mining and Knowledge Discovery 20 (1) (2010) 70–97.

[25] S. Kirkpatrick, C.D. Gelatt Jr., M.P. Vecchi, Optimization by simulated annealing, Science 220 (4598)(1983) 671–680

[26] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers — measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008) 233–253

[27] B. Krishnamurthy, P. Gill, M. Arlitt, A few chirps about Twitter, Proc. the 1st Workshop on Online Social Networks (WOSP' 08), 2008, pp. 19–24.

[28] H. Kwak, C. Lee, H. Park, S. Moon, What is Twitter, a social network or a news media? Proc. the 19th Int'l Conf. World Wide Web (WWW' 10), 2010, pp. 591–600.

[29] E.A. Leicht, M.E.J. Newman, Community structure in directed networks, Physical Review Letters 100 (11) (2008) (118703-1-118703-4).

[30] K. Lerman, R. Ghosh, Information contagion: an empirical study of the spread of news on Digg and Twitter social networks. Proc. 4th Int'l AAAI Conf, Weblogs and Social Media (ICWSM-10). 2010.

[31] I. Letierce, A. Passant S. Decker LG. Breslin Understanding how Twitter is used to spread scientific messages Proc. Web Science Conference (WebSci' 10) 2010

[32] F. Li, T.C. Du, Who is talking? An ontology-based opinion leader identi<sup>fi</sup>cation framework for word-of-mouth marketing in online social networks, Decision Support Systems 51 (1) (2011) 190–197.

[33] C.C. Miller. Dell Says it has Earned \$3 Million from Twitter. New York Times. http:/ bits.blogs.nytimes.com/2009/06/12/dell-has-earned-3-million-from-twitter/. 2009

[34] M.R. Morris, J. Teevan, K. Panovich, What do people ask their social networks, and why? A survey study of status message Q&A behavior, Proc. Int'l Conf. Human Factors in Computing Systems (CHI' 10), 2010, pp. 1739–1748.

[35] M. Naaman, J. Boase, C.H. Lai, Is it really about Me? Message content in social awareness streams, Proc. ACM Conf. Computer Supported Cooperative Work (CSCW 2010), 2010, pp. 189–192.

[36] M.E.J. Newman, Modularity and community structure in networks, PNAS 203 (23) (2006) 8577–8582.

[37] Y. Ni, L. Xie, Z.Q. Liu, Minimizing the expected complete in<sup>fl</sup>uence time of a social network, Information Sciences 180 (2010) 2514–2527.

[38] B. Nonnecke, D. Andrews, J. Preece, Non-public and public online community participation: needs, attitudes and behavior, Electronic Commerce Research 6 (1) (2006) 7–20.

[39] B. O'Connor, R. Balasubramanyan, B.R. Routledge, N.A. Smith, From tweets to polls: linking text sentiment to public opinion time series, Proc. Int'l AAAI Conf. Weblogs and Social Media, 2010, pp. 1–8.

[40] A. Oulasvirta, E. Lehtonen, E. Kurvinen, M. Raento, Making the ordinary visible in microblogs, Personal and Ubiquitous Computing 14 (3) (2010) 237–249.

[41] J.E. Phelps, R. Lewis, L. Mobilio, D. Perry, N. Raman, Viral marketing or electronic word-of-mouth advertising: examining consumer responses and motivations to pass along email, Journal of Advertising Research 44 (4) (2004) 333–348.

[42] R. Reisner. Comcast's Twitter Man. BloombergBusinessweek. http://www. businessweek.com/managing/content/jan2009/ca20090113\_373506.htm. 2009

[43] T. Sakaki, M. Okazaki, Y. Matsuo, Earthquake shakes Twitter users: real-time event detection by social sensors, Proc. Int'l Conf. World Wide Web (WWW' 10), 2010, pp. 851–860.

[44] D.A. Shamma, L. Kennedy, E.F. Churchill, Tweetgeist: can the Twitter timeline reveal the structure of broadcast events? Proc. the 2010 ACM Conf. Computer Supported Cooperative Work (CSCW 2010), 2010, pp. 589–594.

[45] K. Starbird, L. Palen, A.L. Hughes, S. Vieweg, Chatter on the red: what hazards thread reveals about the social life of microblogged information, Proc. ACM Conf. Computer Supported Cooperative Work (CSCW' 10), 2010, pp. 241–250.

[46] J. Sutton, L. Palen, I. Shklovski, Backchannels on the front lines: emergent uses of social media in the 2007 Southern California wild<sup>fi</sup>res, Proc. Int'l Conf. Information Systems for Crisis Response and Management (ISCRAM 2008), 2008, pp. 1–9.

[47] Y. Tong, X. Wang, H.H. Teo, Understanding the intention of information contribution to online feedback systems from social exchange and motivation crowding perspectives, Proceedings of the 40th Hawaii International Conference on System Sciences, 2007.

[48] M.P. Venkatraman, Opinion leaders, adopters, and communicative adopters: a rol analysis, Psychology and Marketing 6 (1) (1989) 51–68.

[49] C. Wagner, M. Strohmaier, The wisdom in tweetonomies: acquiring latent conceptual structures from social awareness streams, Proc. 3rd Int'l Semantic Search Workshop, 2010.

[50] S. Wasserman, K. Faust, Social Network Analysis: Methods and Applications, Cambridge University Press, New York, 1994.

[51] D. Westerman, P.R. Spence, B.V.D. Heide, A social network as information: the effect of system generated reports of connectedness on credibility on Twitter, Computers in Human Behavior 28 (2012) 199–206.

[52] S. Yardi, D. Boyd, Tweeting from the town square: measuring geographic local networks. Proc, 4th Int'l AAAI Conf, Weblogs and Social Media (ICWSM-10), 2010.

[53] S. Yardi, D. Romero, G. Schoenebeck, D. Boyd, Detecting spam in a Twitter network, First Monday 15 (1–4) (2010) (http://<sup>fi</sup>rstmonday.org/htbin/cgiwrap/bin/ojs/index. php/fm/article/view/2793/2431)

![](/api/attachments/5RKD92HR/fulltext/images/8f6bd0115ce05c97d5c0ec7b85e8fe65a5e6b97bff803f0ac709bfef575beed7.jpg)  
Feng Li received his BS and MS degrees in control science and engineering in 1997 and 2000, respectively, and a PhD in systems engineering in 2004 from the Huazhong University of Science and Technology, China. He is currently an asso ciate professor at the School of Business Administration, South China University of Technology, China. His research interests include complex systems modeling and simulation business intelligence and operations management.

![](/api/attachments/5RKD92HR/fulltext/images/e7557136656f3800d62bd94454028cc09b437eb5b2a302a9d4670ef6a971e22e.jpg)

Timon C. Du received his BS degree in Mechanical Engineering from the National Chung-Hsing University, Taiwan. He obtained his MS and PhD degrees in Industrial Engineering from Arizona State University, USA. Dr. Du is a Professor at the Chinese University of Hong Kong. His research interests include e-business, data mining, collaborative commerce and the semantic web. He has published papers in many leading international journals, including Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, Communications of the ACM, IIE Transactions and Information and Management.
