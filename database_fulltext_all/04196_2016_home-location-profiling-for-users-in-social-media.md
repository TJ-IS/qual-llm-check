---
otero_id: 4196
otero_key: "JB75YS3Y"
title: "Home location profiling for users in social media"
authors: "Jinpeng Chen; Yu Liu; Ming Zou"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2015.09.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Jinpeng Chen \*, Yu Liu, Ming Zou

State Key Laboratory of Software Development Environment, School of Computer Science and Engineering, BeiHang University, Beijing 100191, China

A R T I C L E I N F O

Article history: Received 10 February 2015 Received in revised form 5 June 2015 Accepted 21 September 2015 Available online 30 September 2015

Keywords: Social network Tie strength Home location Social tie Labeled relationship Twitter

## A B S T R A C T

In this paper, we focus on the problem of estimating the home locations of users in the Twitter network. We propose a Social Tie Factor Graph (STFG) model to estimate a Twitter user’s city-level location based on the user’s following network, user-centric data, and tie strength. In STFG, relationships between users and locations are modeled as nodes, while attributes and correlations are modeled as factors. An efficient algorithm is proposed to learn model parameters and predict unknown relationships. We evaluate our proposed method by investigating Twitter networks. The experimental results demonstrate that our proposed method significantly outperforms several state-of-the-art methods.

\- 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

With the rapid growth of many large-scale online social networks, such as Facebook, MySpace, and Twitter, and mobile social networks, such as FourSquare, users have begun to expose increasing amounts of their lives and personal data on the Web. Publishing, sharing and discussing short messages is a part of the current trend of making personal information widely available; a trend that is likely to continue to develop in the future. Twitter, one of the largest social networks, has experienced an exponential explosion in its user base, reaching approximately 500 million users as of 2013 [21]. Twitter users publish more than 143,199 posts, or ‘tweets’, per second [19]. Current Twitter user portfolios, consisting of a user’s full name, occupation (i.e., employer), education (i.e., college), location (i.e., home city), short biography and number of tweets, span long periods of time and reveal a lot about the users themselves: their interests, their self-conceptions, where they live and what they do.

One of these user attributes, home location is important information for many advanced information services, such as localized news delivery, friend recommendations and targeted ad services [33]. In the existing literature, many methods [3,7,23,38,8] have been presented to model users’ locations in the context of social networks. Most studies profile a user’s home location by leveraging user-centric data (e.g., GPS data or tweets). However, user-centric data are often sparse. Like most social network sites, most Twitter users’ locations are missing [33]. On Twitter, only a few users (16%) register their location as granularly as a city name (e.g., Los Angeles, CA). Most leave nonsensical (e.g., ‘‘my home’’), general (e.g., ‘‘CA’’) or even blank information. Although Twitter has supported a function that attaches latitude and longitude information for the present location to each message as a geo-tag with mobile devices equipped with GPS locators since August 2009, even fewer users (0.5%) use this feature because of obvious privacy concerns [9]. Research is therefore limited to predicting users’ home locations only using geo-based features per user or per tweet signals.

Additionally, a number of studies [32,33] have predicted users home locations by considering users’ social ties (e.g., friendships). They explore both user-centric and social network data to profile users’ locations. However, the potentially strong but inconspicuous relationship between tie strength and location function is overlooked. In fact, online interaction data (specifically, Twitter interactions) can successfully identify strong real-world ties. For example, the more Alice interacts with Bob on Twitter, the more likely Alice is to name Bob as her closest friend [25]. As we know, one’s closest friends are more likely to share the same location, e.g., friends who are attending the same school.

Moreover, there are a number of existing works that explicitly investigate the relationship between social interactions and distance [5,18]. In [26], Jurgens constructed cumulative distribution functions, clarifying that the nearest neighbor is highly predictive of the individual location and determining that over half of the individuals in the Twitter network have a neighbor who has indicates their location within close proximity. In [41], their histogram of physical distances demonstrates that the uneven distribution of users’ locations is important in analyzing the distribution of tie lengths. In [36], McGee et al. investigated how social ties and geographical distances between relations correlate. They identified several factors affecting social ties: reciprocal friends, just friends, just followers and just mentioned. In an experimental analysis, they showed that the probability of these four types of friendships generally decreases as the distance between people increases. Furthermore, they sought to identify which types of relationships tend to be closer than others by considering a number of relationship features related to physical proximity. Finally, they noted that people who have stronger social ties, such as reciprocal friends, are more likely to live near each other than people who have weak ties. In [40], Sadilek et al. argued that even if online interactions are, in theory, not hampered by physical distance, nearly all researchers agree that in any social network studied, the probability of friendship commonly decreases as the distance between people increases. In [46], Yardi et al. characterized network properties in relation to local geography. They first investigated the relationship between structural properties in the Twitter network and geographic properties in the physical world. They then described the role of mainstream news in disseminating local information. Finally, they found that local networks are denser than non-local networks and that central individuals in the Twitter network are also located centrally in the physical world. Given the findings of previous research, we now know that the more strongly two people interact with each other, the more likely they are to share the same location.

In addition, tie strength can be used to remove a noisy signal when predicting user location. A user often follows friends from or publishes tweets about different locations other than his home location. For example, a user in Chicago may follow Lady Gaga in New York or President Obama in Washington and may tweet about the Houston Rockets’ game or his vacation in Honolulu. Such information can be regarded as noisy signals. However, a famous user is more likely to have a weaker tie than a regular user does; thus, tie strength is robust to noisy signals.

To the best of our knowledge, no researcher has modeled a user’s home location by considering tie strength yet. In this paper, we attempt to discern users’ home locations by considering social ties (i.e., a user’s following network), user-centric data (e.g., tweets) and tie strength. Intuitively, these three types of data give valuable signals with which to profile user location, as a user is likely to (1) connect other users who live close to her, (2) tweet her nearby locations, and (3) share the same venue as other users who interact with her strongly.

The main contributions of this research can be summarized as follows:

We study the problem of profiling ‘‘home locations’’ for Twitter users by investigating users’ following networks, user-centric data and tie strength.

We propose to leverage a social tie factor graph (STFG) model to illustrate relationship attribute information in home location prediction and identify the potential set of locations by performing similarity retrieval on various features including the basic information of two users, link homophily, node influence and tie strength.

Experiments on a real dataset indicate that our proposed method can predict home location with high accuracy in comparison to state-of-the-art unsupervised methods and supervised frameworks.

The remainder of the paper is organized as follows. We first discuss related work in Section 2. We next introduce the background and preliminaries on Twitter networks, detailing the task of home location prediction in Section 3. We present a Social Tie Factor Graph (STFG) model to predict the home location for each user in Section 4. We report our experiments and results in Section 5, and conclude the study in Section 6.

## 2. Related work

In this section, we review two categories of related work: studies on tie strength and home location prediction in social networks.

## 2.1. Tie strength

Tie strength has recently emerged as a popular way to measure social ties between users in different activity fields [48]. Early works primarily investigated means of inferring or measuring tie strength from the different attributes of a user or the user’s friends.

In [4], the researchers provided insight into friendship on social network sites, discussing the role of such sites in the communication landscape of relationships. In [12], researchers first investigated the extent to which social ties between people can be inferred from co-occurrence in time and space, finding that users who check in at the same place and time are much more likely to become friends. In [27], researchers developed a supervised learning approach to predict link strength from transactional information. In [15], they noted that wall posts and messages are strong predictors of relationship strength and presented a predictive model that maps social media data to tie strength. In [44], the researchers built an unsupervised model of the strength of social ties on Facebook, looking at interactions such as face-tagging in photos. In [47], they found that including social features along with message content-based features in SVM classifiers resulted in a significant reduction in prediction error when learning to identify emails that a given user will consider important. In [17], they took an axiomatic approach to measure connectedness or tie strength between each pair of persons. In [25], the researchers carried out a study estimating tie strength from online extensive interactions on Facebook. They asked a set of participants to name their closest friends in real life. Researchers then utilized collected evaluations to train a classifier to distinguish between strong and weak ties. The classifier gave a membership probability calculated from a set of online interaction variables. This probability represented a prediction of tie strength.

## 2.2. Location prediction

Recent studies have explored the geographical scope of online resources, including blogs [14,34,20,13,10], query logs [2], tags [39] and photos [11]. However, these works have primarily focused on predicting locations for different types of entities with different content. In [1], the researchers used a webpage’s content to predict its geo-scope based on NLP heuristic rules. Their method extracted location signals (e.g., city names) from a page by leveraging a gazetteer. Our work is different, as we take a factor graph approach to modeling user locations. In [6], the researchers used a twolayered graph to model relationships between locations as well as the relationships between locations and users. Their proposed ranking model took into account significant propagation among locations, mutual reinforcement between location significance and user authority, and aspects such as the number of visits to a location, visit duration, and distance between locations. However, they did not differentiate between locations from different categories.

Our work is similar to [9,3,7,32,40], as these studies also model user locations. In [9], the researchers built a probabilistic framework to predict a Twitter user’s city-level location based on the content of his tweets. Specifically, they first built multi-local term classifiers to identify words in tweets with a strong geo-scope, and then refined a user’s location estimate using a lattice-based neighborhood smoothing model. In [40], researchers leveraged tweet content and location to discover the potential relationship between users. On the basis of a friendship graph, they then estimated users’ location. In [32], researchers proposed a unified discriminative influence model to integrate signals obtained from both social networks (i.e., friends) and user-centric data $( \mathrm { i . e . }$ , tweets). In [7], researchers noted that user location is strongly related to user interest. They first estimated users’ friendship by employing two features $( \mathrm { i . e . }$ , text similarity and co-location) to identify users with similar activity behavior and construct the relationship between them. They then predicted a user’s location in terms of the entire graph of the Hidden Markov Model. However, our work aims to mine users’ home locations by considering social ties (a user’s following network), user-centric data (tweets) and tie strength.

## 3. Problem definition

In this section, we first introduce Twitter and then present the problem formulation.

Twitter is a microblogging service, whereby users can follow others and publish messages. Three important types of resources can be identified for each user. First, we can look at following relationships between the user and other users. Second, we can access a user’s tweets. We note that following relationships are ‘‘directional,’’ meaning that a user can follow any other user, and the user being followed need not follow his or her followers in return. Thus, we further divide a user’s following relationships into followers who follow the user and friends who are followed by the user. Third, we examine tie strength, a (probably linear) combination of the amount of time, emotional intensity, intimacy (mutual confiding), and reciprocal services that characterize the tie [16].

As mentioned in Section 1, these three types of resources are useful in inferring a user’s locations. In this work, our goal is to build a location profile for each user; specifically, we are interested in inferring their city-level locations. All possible city-level locations can be given by a gazetteer, which can be easily obtained from various online resources (e.g., Geographic Names Information System) [33]. If a user’s followers or friends provide locations in their profiles, we can propagate their locations to him. Furthermore, if a user mentions venues in his messages, we can use these references to infer his location.

As illustrated by Fig. 1, the Twitter dataset can be represented as a heterogeneous network $G = ( V , E ) ,$ , where V is a set of nodes $\nu _ { i } ,$ and E is a set of edges $E = \left\{ \begin{array} { l } { ( \nu _ { i } , \nu _ { j } ) | \nu _ { i } , \nu _ { j } \in V \right\} } \end{array}$ . V contains two types of nodes: user nodes U representing all users and location nodes L representing all the locations related to users. E contains two types of edges: friendship edges F between user nodes and tweeting edges T between user nodes and location nodes. Let x be a set of attributes associated with user $u _ { i } .$ . An attribute can be the user’s interest, number of friends or tie strength between the user and her friends. We use $X = \{ x _ { 1 } , . . . , x _ { N } \}$ to define the attributes of all users. Next, let us give a formal definition of the output of the problem, namely, the ‘‘labeled relationship.’’

Definition 1. Labeled relationship: A labeled relationship is a triple $( e _ { i j } , \ r _ { i j } , \ p _ { i j } ) , \ e _ { i j } \in T$ is a tweeting relationship, $r _ { i j } \in Y$ is a label associated with the relationship $( Y$ is a set of all the labels) and $p _ { i j }$ is a probability achieved by an algorithm used to mine home locations for each user.

![](/api/attachments/JB75YS3Y/fulltext/images/ad74d2652ebffd327048136b8809a9d4aba23c08eede808627df5a5ef214dc26.jpg)  
Fig. 1. A sample Twitter graph. The larger the edge sizes, the stronger the tie strength between the edges’ two associated variables.

To infer a labeled relationship, we could consider three factors: social ties, user-centric data and tie strength. Moreover, a number of labeled relationships may exist. Formally, we denote the input of our problem as a partly labeled network with augmented attributes.

Definition 2. Attribute augmented network: An augmented social network can be denoted as $G = ( V , F , T ^ { \mathrm { L } } , T ^ { \mathrm { U } } , R ^ { \mathrm { L } } , W ) ,$ , where F is a set of following relationships between users; T<sup>L</sup> is a set of labeled relationships between users and locations; $T ^ { \mathrm { U } }$ is a set of unlabeled relationships between users and locations with $T ^ { \mathrm { L } } \cup T ^ { \mathrm { U } } = T ; R ^ { \mathrm { L } }$ is a set of labels corresponding to the relationships in $T ^ { \mathrm { L } . } ;$ and W is an attribute matrix associated with users in $V$ whereby each row corresponds to a user, each column corresponds to an attribute, and an element $w _ { i j }$ denotes the value of the jth attribute of user u .

Based on the above concepts, our research problem can be instantiated. Given a partly labeled network with augmented attributes, our goal is to detect the labels of all unknown relationships in the network.

Problem. Given a partly labeled network with augmented attributes $G = ( V , \ : F , \ : T ^ { \perp } , \ : \dot { T } ^ { \mathrm { U } } , \ : \dot { R } ^ { \mathrm { L } }$ , W), the target is to learn a predictive function:

$$
f: G = (V, F, T ^ {\mathrm{L}}, T ^ {\mathrm{U}}, R ^ {\mathrm{L}}, W) \to R
$$

Our formulation of inferring home locations for each user is very different from existing works on home location mining. In [3], Backstrom et al. estimate a user’s location based on his friends on Facebook. Both Cheng et al. [9] and Ikawa et al. [23] investigate the problem of home location identification. They focus on detecting home location from the content of users’ tweets. Our work is motivated by researchers such as [32], who proposed a unified discriminative influence model integrating signals observed from both social networks (friends) and user-centric data (tweets). Our work, however, differs from this previous approach; we consider another important factor, namely, tie strength. Notations used in definitions as well as throughout the rest part of the paper can be found in Table 1.

## 4. Model framework

In this section, we propose a Social Tie Factor Graph (STFG) model, which formulates the home location mining problem in a unified learning framework. The STFG model simultaneously incorporates three types of social network resources to generate high-quality home location data for each user.

Table 1 Notations.

<table><tr><td>Symbols</td><td>Description</td></tr><tr><td>U</td><td>A set of users</td></tr><tr><td>L</td><td>A set of locations</td></tr><tr><td>F</td><td>A set of following relationship</td></tr><tr><td>T</td><td>A set of tweeting relationship</td></tr><tr><td>X</td><td>The attributes of all users</td></tr><tr><td> $T^L$ </td><td>A set of labeled relationship between users and locations</td></tr><tr><td> $T^U$ </td><td>A set of unlabeled relationship between users and locations</td></tr><tr><td>Y</td><td>A set of all the labels</td></tr></table>

## 4.1. Basic idea

In this study, we construct each relationship as a node in the graphical model. By using this methodology, our goal – understanding the relationship between users and home locations mining task – becomes how to predict the labeled relationship for each relationship node in the model. This method is intuitive, easily modeling correlations between two relationships with low computational complexity. More importantly, this model can incorporate different correlations between relationships.

As mentioned in Section 1, to mine home location for each user, three types of resources are useful in profiling a user’s location. A user is likely to (1) follow and be followed by users who live close to her, (2) tweet ‘‘location names’’ that may indicate her locations (here, we refer a location name as the name of a geo-signal, which could be a city (e.g., New York City), a place (e.g., Las Vegas Strip), or local entity (e.g., Stanford University)) and (3) share the same venue as other users who interact with her strongly. In addition, different relationships between users and locations may have a correlation. For example, if there is a strong interaction between user u and user u at the location ‘Stanford University’, then the relationship between user u and user $\mathbf { u } _ { \mathrm { j } }$ may be school-related (i.e., peers or colleagues).

Based on the above descriptions, we propose a Social Tie Factor Graph (STFG) model. Fig. 2 provides a graphical representation of the STFG. There are two types of relationships in Fig. 2: a following relationship and a tweeting relationship. In this study, we model the following relationship using tie strength. In the next section, we will introduce methods by which to measure tie strength. We map each tweeting relationship $T _ { i j }$ in an attribute augmented network G to a relationship node $r _ { i j }$ in STFG. A set of relationship nodes can be defined as $Y = \{ y _ { 1 } , ~ y _ { 2 } , ~ . . . , ~ y _ { M } \}$ . The tweeting relationships in G are partially labeled, thus all nodes in STFG can be divided into two subsets $Y _ { \mathrm { L } }$ and $Y _ { \mathrm { U } } ,$ which correspond to labeled and unlabeled tweeting relationships, respectively. For each tweeting relationship node $y _ { i } = \left( u _ { i } , ~ \nu _ { j } , ~ r _ { i j } \right)$ , we combine the attributes $\{ w _ { i } , w _ { j } \}$ into a relationship attribute vector x<sub>i</sub>.

![](/api/attachments/JB75YS3Y/fulltext/images/87c17e28da0630c03f2e2609f5fde07bfcb0e45e9c74a25aafdf20ef53f3cf01.jpg)  
Fig, 2. Graphical representation of the STFG model, ua is the given user whose home location will be predicted; {l , l } are two candidate locations extracted by considering social tie and user-centric data; $\{ y _ { 1 } , y _ { 7 } \}$ are latent variables denoting pairs between users and locations, with each representing whether the corresponding user-location pair will have a label relationship; f(.) represents a factor function denoting each user-location pair; and g(.) represents a correlation factor function denoting latent variables.

Next we will introduce the STFG in detail. Tweeting relationships in the input are modeled by relationship nodes in STFG. We denote two types of factors that may influence the formation of tweeting relationships.

Attribute factor: $f ( y _ { i } , u _ { i } , u _ { j } )$ captures the posterior probability of the tweeting relationship y given the characteristics of the two users, e.g., the following relationships between two users.

Correlation factor: $g ( y _ { i } , G ( y _ { i } ) )$ denotes the correlation between tweeting relationships, where $G ( y _ { i } )$ is the set of correlated relationships to $y _ { i \cdot }$

We can adopt different ways in which to instantiate the above factors. In this study, we use exponential-linear functions, denoting the attribute factor as

$$
f (y _ {i}, x _ {i}, x _ {j}) = \frac {1}{Z _ {\alpha}} \exp \{\alpha^ {T} \phi (y _ {i}, x _ {i}, x _ {j}) \}
$$

where $Z _ { \alpha }$ is a normalization factor, a is a weighting vector, $\phi$ is a vector of feature functions denoted between u and $u _ { j }$ with respect to the value of y , and x and $x _ { j }$ are attributes associated with $u _ { i }$ and $u _ { j } ,$ respectively. Similarly, we can denote the correlation factor function as

$$
g \left(y _ {i}, G \left(y _ {i}\right)\right) = \frac {1}{Z _ {\beta}} \exp \left\{\sum_ {y _ {i} \in G \left(y _ {i}\right)} \beta^ {T} \varphi \left(y _ {i}, y _ {j}\right) \right\}
$$

where $\varphi$ is a vector of indicator functions.

Given $G = ( V , F , T ^ { \mathrm { L } } , T ^ { \mathrm { U } } , R ^ { \mathrm { L } } , W ) .$ , by integrating the denoted factor functions, we can define the joint distribution over Y as

$$
\begin{array}{l} P (Y | G) = \prod f (y _ {i}, x _ {i}, x _ {j}) g (y _ {i}, G (y _ {i})) = \frac {1}{Z} \prod \exp \{\varsigma^ {T} h (y i) \} \\ = \frac {1}{Z} \exp \{\varsigma^ {T} \sum h (y _ {i}) \} \end{array}
$$

where $Z = Z _ { \alpha } Z _ { \beta } \stackrel { \mathrm { i } s } { \mathrm { ~ \bf ~ a ~ } }$ normalization factor, ${ \bf S } = ( \alpha , ~ \beta ) ,$ , and $h ( \boldsymbol { y _ { i } } ) = \big ( f ( \boldsymbol { y _ { i } } , \boldsymbol { x _ { i } } , \boldsymbol { x _ { j } } ) ^ { T } , g ( \boldsymbol { y _ { i } } , G ( \boldsymbol { y _ { i } } ) ) ^ { T } \big ) ^ { \boldsymbol { l } }$

## 4.2. Feature definitions

We use a variety of ways to denote the factor functions $\phi ( y _ { i } ,$ $x _ { i } , x _ { j } )$ and $\varphi ( y _ { i } , y _ { j } ) .$ . In theory, we can instantiate factor functions in different methods to reflect our prior knowledge (or intuitions) for different applications. Here, we define the factor function as either a binary function or a real-valued function. For instance, for the attribute factor function, a binary feature function can be denoted according to an attribute in X: if two users live close to each other, then a feature $\phi ( y _ { i } ,$ $| x _ { i k } - x _ { j k } | < d \ m i l e s ) = 1$ , where k is the attribute of distance. In total, we denote seven factor functions that can be disaggregated into four categories: basic information of two users, link homophily, node influence, and tie strength.

## 4.2.1. Basic information

We calculate a set of statistics for each potential following relationship: the average time gap when two users post tweets and the cosine similarity of the interests of two users [43], whereby we consider keywords appearing in the user’s profile as her interests.

## 4.2.2. Link homophily

Two features can be defined as [35]: the number of common links between a user and her followers and the number of common links between a user and her followees.

## 4.2.3. Node influence

We use the method in [32] to model a node’s influence scope. The authors chose a Gaussian distribution to capture a node’s influence model. Two features can be denoted as follows: influence scope of a friend and influence scope of a venue.

## 4.2.4. Tie strength

To measure the tie strength, we implement multiple strategies in this study. These strategies can be outlined as follows.

Common Friends (CF). This is the simplest strategy with which to measure tie strength and is equal to the total number of common topics that both u and v are interested in.

$$
C F (u, v) = | \psi (u) \cap \psi (v)
$$

where c(u) represents a set of topics that a user u is interested in. The Jaccard Coefficient (JC). A more refined measure of tie strength is given by the Jaccard Coefficient. According to the definition in [42], we normalize the connection of two users u and v by calculating:

$$
J C (u, v) = \frac {| \psi (u) \cap \psi (\nu) |}{| \psi (u) \cup \psi (\nu) |}
$$

Katz. This measure counts the number of paths between user u and user v [28]. Here, each path is discounted exponentially by the length of path.

$$
K (u, v) = \sum_ {q \in \boldsymbol {P}} \gamma^ {- | q |}
$$

where P is a set of paths existing between user u and user v, $0 \leq \gamma \leq 1$

Random Walk with Restart (RWR). RWR is a widely used nodeto-node similarity in graph data. It defines a non-symmetric measure of tie strength [17]. For each user u, we give a random walk centered at u by using the following rules. At each random step, the random walk jumps to the original node u according to the restart probability $\alpha ,$ then randomly jumping to a neighbor of the current node with probability $1 - \alpha .$ The tie strength between u and v is the stationary probability that we end at node v through this process.

SimRank (SR). SimRank is a measure that says ‘‘two objects are considered to be similar if they are referenced by similar objects $[ 2 2 ] . "$ It captures the similarity between two users u and v by recursively computing the similarity of their neighbors.

$$
S R ^ {\gamma} (u, v) = \left\{ \begin{array}{l l} 1 & \text { if } u = v \\ \gamma \frac {\sum_ {a \in \psi (u)} \sum_ {b \in \psi (v)} S R (a , b)}{| \psi (u) | | \psi (v) |} & \text { else } \end{array} \right.
$$

where $0 \leq \gamma \leq 1$

## 4.3. Model learning

We now address the problem of estimating the free parameters and inferring users’ home locations. Given a set of labeled nodes in the STFG, learning the model is to find a parameter configuration $\mathsf { \boldsymbol { S } } = \left( \alpha , \beta \right)$ so that the log-likelihood of observation information (labeled relationships) is maximized. Thus, we can denote the log-likelihood objective function as

$$
\begin{array}{l} O (\varsigma) = \log (Y ^ {L} | G) = \log \sum_ {Y | Y ^ {L}} \frac {1}{Z} \exp \{\varsigma^ {T} \sum h (y _ {i}) \} \\ \quad = \log \sum_ {Y | Y ^ {L}} \exp \{\varsigma^ {T} \sum h (y _ {i}) \} - \log Z \\ \quad = \log \sum_ {Y | Y ^ {L}} \exp \{\varsigma^ {T} \sum h (y _ {i}) \} - \log \sum_ {Y} \exp \{\varsigma^ {T} \sum h (y _ {i}) \} \end{array}
$$

where $Y ^ { \mathrm { L } }$ defines the known labels, and $Y | Y ^ { \mathrm { L } }$ is a labeling configuration Y inferred from the known labels.

To maximize the objective function, we adopt a gradient decent method (or the Newton–Raphson method). In particular, we calculate the gradient for each parameter $\mathbf { s }$

$$
\begin{array}{l l} \frac {\partial O (\varsigma)}{\partial \varsigma} & = \frac {\partial (\log \sum_ {Y | Y ^ {L}} \exp \{\varsigma^ {T} \sum h (y _ {i}) - \log \sum_ {Y} \exp \{\varsigma^ {T} \sum h (y _ {i}) \} \})}{\partial \varsigma} \\ & = \frac {\sum_ {Y | Y ^ {L}} \exp \{\varsigma^ {T} \sum h (y _ {i}) \} \cdot \sum h (y _ {i})}{\sum_ {Y | Y ^ {L}} \exp \{\varsigma^ {T} \sum h (y _ {i}) \}} - \frac {\sum_ {Y} \exp \{\varsigma^ {T} \sum h (y _ {i}) \} \cdot \sum h (y _ {i})}{\sum_ {Y} \exp \{\varsigma^ {T} \sum h (y _ {i}) \}} \\ & = \epsilon_ {p \theta (Y | Y ^ {L})} \sum h (y _ {i}) - \epsilon_ {p \theta (Y)} \sum h (y _ {i}) \end{array}
$$

As the graphical structure in the STFG model can be arbitrary and may contain cycles, it is intractable to directly calculate two expectations o $\sum h ( y _ { i } ) , \epsilon _ { p \theta ( Y | Y ^ { L } ) } \sum h ( y _ { i } )$ and $\varepsilon _ { p \theta ( Y ) } \sum h ( y _ { i } )$ . A number of approximate algorithms have been considered, such as Loopy Belief Propagation (LBP) [37] and Mean-field [45]. In this work, we leverage Loopy Belief Propagation due to its ease of implementation and effectiveness. In particular, we use Loopy Belief Propagation (LBP) to approximate marginal probabilities $p ( y _ { i } | \mathbf { S } )$ and $p ( y _ { i } , y _ { j } | \mathbf { S } ) .$ . The general idea is to perform the LBP process twice, once to calculate $\epsilon _ { p \theta ( Y \mid Y ^ { L } ) } \sum h ( y _ { i } )$ and the second time to calculate $\varepsilon _ { p \theta ( Y ) } \sum h ( y _ { i } )$ , to estimate the gradient of a parameter . Finally with the gradient, we update each parameter with a learning rate $\xi .$ The learning algorithm is shown in Algorithm 1.

Next, we will introduce the method by which to infer the unknown labels. Based on the learned optimal parameters , we can predict the unknown labels by finding a label configuration that maximizes the joint probability $P ( Y | G ) , Y ^ { * } = \mathrm { a r g m a x } _ { Y | Y ^ { L } } p ( Y | G )$

We again perform a two-step LBP to compute the margina probability of each relationship node $p \left( y _ { i } | Y ^ { \mathrm { L } } , G \right)$ and then infer the tweeting relationship as the label with largest marginal probability.

## Algorithm 1. Learning algorithm for the STFG model

Input: a network G and the learning rate j

Output: estimated parameters $\mathbf { S } = ( \alpha , \beta )$

$$
\text { Initialize } \xi \leftarrow 0
$$

$$
\text { While   not   converged: } \backslash \backslash
$$

$$
\epsilon_ {p \theta (Y | Y ^ {L})} \sum h (y _ {i})
$$

4. Perform LBP to calculate $\varepsilon _ { p \theta ( Y ) } \sum h ( y _ { i } )$

Calculate the gradient of \$\zeta\$ based on

$$
\frac {\partial O (\varsigma)}{\partial \varsigma} = \epsilon_ {p \theta (Y | Y ^ {L})} \sum h (y _ {i}) - \epsilon_ {p \theta (Y)} \sum h (y _ {i});
$$

$$
\nabla \varsigma = \epsilon_ {p \theta (Y | Y ^ {L})} \sum h (y _ {i}) - \epsilon_ {p \theta (Y)} \sum h (y _ {i})
$$

Update $\mathbf { S }$ with the learning rate $\xi \colon$

$$
\varsigma_ {n e w} = \varsigma_ {o l d} - \xi \cdot \nabla \varsigma
$$

## 5. Experiments

In this section, we conduct experiments on a large-scale dataset generated by Li [32] and show the effectiveness of our methods from several different perspectives. Specifically, we first describe our experimental setup and then discuss the performance of the proposed method and present comparison methods. Finally, we provide some analyses and discussions.

## 5.1. Experimental setup

## 5.1.1. Dataset

The dataset was originally collected in May 2011 by Li [32]. Li et al. constructed this dataset by crawling Twitter with Twitter API. This dataset contains 284 million following relationships, 3 million user profiles and 50 million tweets. For each user, we can obtain the following information: profiles, followers and friends. Here, Li et al. further enriched this dataset using two methods: extracting users’ registered locations from their profiles based on the rules depicted in [9] and extracting home locations with city-level labels in the form of ‘‘cityName, stateName’’ and ‘‘cityName, stateAbbreviation,’’ whereby all cities listed in the Census 2000 U.S. Gazetteer were considered. Due to users’ privacy settings or lack of tweets, we also use the 139,180 users and their relationships and tweets, as our dataset. By performing a statistical analysis based on this dataset, we see that there are 14.8 friends, 14.9 followers, and 29.0 tweeted venues per user, on average. The properties of this dataset are shown in Table 2.

Sometimes, we observe noisy data for users’ home locations, such as users’ past locations and multiple active locations. To make our results more reliable, we first check the users’ home locations in the dataset. We adopt the Probability Distribution Model in [29,9] to the verify users’ home locations. Specifically, we first obtain the actual distribution of each word across cities in the dataset. On the basis of maximum likelihood estimation, the probabilistic distribution of each word w over cities can be calculated as p(cjw). This probabilistic distribution indicates a probability of the user u being located in city c. By collecting across all words in tweets posted by a particular user (e.g., users with noisy data), the home location of the user will become clear. Assuming a set of words $S _ { \mathbf { w } ( \mathbf { u } ) }$ is drawn from this user’s tweets, the probability of this user being located in city c can be denoted as $\begin{array} { r } { p ( c | S w ( u ) ) = \sum _ { w \in S w ( u ) } p ( c | w ) \cdot p ( w ) } \end{array}$ . Thus, we obtain a set of usercity probabilities across all cities, taking the city with the highest probability to be the user’s estimated home location.

## 5.1.2. Comparison methods

We compare our approach with the following methods used to infer users’ home locations.

SVM. SVM, which is similar to the logistic regression model used in [31], utilizes attributes associated with each edge as features x to train a classification model and then predicts edges’ labels by using the classification model in the test dataset. We employ SVM-light [24] as our model.

CRF. CRF trains a conditional random field [30] with attributes associated with each edge and correlations between edges.

LRC. LRC uses the same attributes associated with each edge as features to train a logistic regression classification model [31] and then predicts edges’ labels in the test data.

## Table 2

Properties of the dataset.

<table><tr><td>Property</td><td>Twitter</td></tr><tr><td>Number of users</td><td>3 million</td></tr><tr><td>Number of tweets</td><td>50 million</td></tr><tr><td>Number of following relationships</td><td>284 million</td></tr><tr><td>Number of users with one labeled friend or follower</td><td>158,220</td></tr><tr><td>Friends per user</td><td>14.8</td></tr><tr><td>Followers per user</td><td>14.9</td></tr><tr><td>Tweeted venues per user</td><td>29.0</td></tr><tr><td>Tweets per user</td><td>600</td></tr></table>

DBN. DBN utilizes a probabilistic model to estimate users’ locations as well as social ties. This probabilistic model leverages some significant patterns that the characterize locations of individuals and their friends [40].

IML. IML first mines user interests from posts and establishes the mapping between location function and user interest. It then leverages an efficient framework to predict user location [7].

UDI. UDI integrates signals observed from both social networks (friends) and user-centric data (tweets) in a unified probabilistic framework [32]. UDI differs from our method in that it does not consider the factor of tie strength.

## 5.1.3. Evaluation measures

To evaluate the quality of our proposed method, we consider three popular metrics in this work [9,7]: error distance (ED), average error distance (AED) and accuracy (ACC). Our method defines error distance in miles between a user’s actual location and an estimated location. ED can be denoted as:

$$
\operatorname{ED} (u) = d (l a (u), l e (u))
$$

where la(u) is the actual location of the user u and le(u) is the estimated location of u.

In regard to average error distance, we measure the overall performance of our proposed method. We denote the AED across a set of users U as following:

$$
\operatorname{AED} (u) = \frac {\sum_ {u \in U} \operatorname{ED} (u)}{| U |}
$$

In regard to accuracy, this method considers the percentage of users with an error distance less than or equal to a specific threshold (Thresh), denoted in the following equation:

$$
\operatorname{ACC} (u) = \frac {\left| \left\{u \mid u \in U \wedge \operatorname{ED} (U) \leq \text { Thresh } \right\} \right|}{\left| U \right|}
$$

where Thresh is in the range of 0–100 miles.

## 5.2. Results

In this section, we first evaluate the performance of five different methods used to measure tie strength. We then compare the performance of our proposed STFG with six other baselines.

## 5.2.1. The optimal measure method

In Fig. 3, we see that the measure SR outperforms all other measures, producing the best prediction performance in terms of AED. In Fig. 4, according to ACC, SR also significantly outperforms the other four measures. Specifically, SR can increase average accuracy by 7.1%, 15.2%, 29% and 37% compared with RWR, K, JC and CF, respectively. Interestingly, CF exhibits the worst performance, possibly because using the raw frequency, which does not take the frequency of individual users into account, to compute the quality of the relationship between two users is not very meaningful. In this work, we adopt SR to measure tie strength to more accurately mine the home location for each user.

## 5.2.2. The performance of proposed method

In this section, we compare the predictive performance of our proposed STFG with the baselines mentioned above. We illustrate how our STFG can serve as a powerful model to predict home locations. Prediction processing performance results can be found in Figs. 5 and 6. We use two prediction processing measures to evaluate the performance of each method on the Twitter dataset, namely, AED and ACC. In terms of these two measurements, one can observe that in general, our proposed STFG produces more accurate home location information than other baselines.

Fig. 4. ACC.  
![](/api/attachments/JB75YS3Y/fulltext/images/eca3564f37e84e642e880afa325d2294fefa2664190b7cf70c9871aab8743b7f.jpg)

![](/api/attachments/JB75YS3Y/fulltext/images/d1ebe9ec982f5ce7bc551dc7d24d7503e7fec96bee95be5f4883d82a31e18650.jpg)

![](/api/attachments/JB75YS3Y/fulltext/images/52a0f4c1f6a26482ba4048367ab0227b3da57810f047d283a738c55192e08537.jpg)  
Fig. 5. Performance comparison with the different methods on ACC.

Fig. 5 plots an accumulative accuracy at distances curve for each method. Each point (X, Y) on the curve represents that Y percentages of users are accurately predicted within X miles. In Fig. 5, we see that STFG has higher accuracy than the other six methods at different distances. On average, STFG achieves a 29.7%,

![](/api/attachments/JB75YS3Y/fulltext/images/dbdae064a1966d91333f89ec91d6840574c133fd1d452d6ca763feb602bec903.jpg)  
Fig. 6. Performance comparison with the different methods on AED.

22.2%, 12.3%, 10.6% and 18% improvement compared with SVM, LRC, CRF, DBN and IML, respectively, in terms of ACC. These five methods also use training data; however, they do not consider the correlation among user-location pairs, and thus perform worse than our method, STFG. In addition, STFG can increase the average accuracy by 2.5% compared with UDI. This result verifies that tie strength mining plays a positive role in home location estimation. It is worth noting that when the distance increases, the accuracy of IML quickly decreases, dropping to almost the worst performance when the distance is 30 miles. This outcome can be attributed to the fact that their method relies on users’ history location information, yet POI is almost unrelated to user location. On the contrary, when user number increases, a growing number of noisy POI data may be produced, thus resulting in a negative impact on location estimation. A similar analysis is shown in Fig. 6. Interestingly, the AED of DBN quickly decreases when the distance is greater than 10 miles. This outcome may be attributable to the fact that their method attempts to find users with similar patterns; whereas here, with the increase in user number, their method is more likely to identify users with similar motion patterns.

## 5.2.3. Factor contribution analysis

We now analyze the ways in which different factors can help mine home locations. In the STFG model, we consider five major factors: link homophily (LH), friends’ influence (FI), venues’ influence (VI), tie strength (TS) and basic information. Here, we examine the contribution of different factors defined in our STFG model. In particular, in this study, we use basic information as the basic features in the model and explore the contribution of the other four factors.

We first remove four factors, namely, LH, FI, VI and TS, only keeping the basic information factor. We then add each of the four factors into the model and evaluate the performance improvement by each factor. Table 3 shows the results of factor analysis. We can observe that almost all the factors are useful in predicting home location; however, their individual contributions are very different. Consider ACC as an example. STFG can, on average, increase by 2.2%, 7.9%, 8.8%, and 10.1% in relation to LH, FI, VI, and TS, respectively. We often observe that in mining home locations, tie strength is more important than other factors. This analysis confirms that our method works well when combining all features together.

## 5.2.4. Convergence analysis

We carry out an experiment related to the effect of the number of iterations of the Loopy Belief Propagation (LBP). Figs. 7 and 8 show the results of a convergence analysis of the STFG learning algorithm. In these test cases, we observe that the learning algorithm can converge after less than 13 iterations. After approximately 10 iterations, the performance becomes stable. This outcome indicates that the learning algorithm is very efficient and has a good convergence property.

Table 3  
Factor contribution analysis.

<table><tr><td>Factors used</td><td>ACC</td><td>AED</td></tr><tr><td>Basic features</td><td>0.392</td><td>66.8</td></tr><tr><td>+LH</td><td>0.414 (+2.2%)</td><td>60.1</td></tr><tr><td>+FI</td><td>0.471 (+7.9%)</td><td>57.2</td></tr><tr><td>+VI</td><td>0.480 (+8.8%)</td><td>56.4</td></tr><tr><td>+TS</td><td>0.493 (+10.1%)</td><td>53.2</td></tr><tr><td>All</td><td>0.558 (+16.6%)</td><td>41.6</td></tr></table>

![](/api/attachments/JB75YS3Y/fulltext/images/344b8232d138a88b4a34a92766913a731cd53afc2835a9f08686ffcc0afaea91.jpg)  
Fig. 7. Convergence analysis of the learning algorithm on ACC.

![](/api/attachments/JB75YS3Y/fulltext/images/6d3e0421cbe311c8fd3e5c2acb452e5b70fd2d163e943cd0a41fbdf88c550581.jpg)  
Fig. 8. Convergence analysis of the learning algorithm on AED.

## 5.2.5. Discussion and limitations

In this section, we first discuss how our method will be affected by tie strength. We then analyze the shortcomings of our method.

We observe that in Fig. 9, the Average Error Distance (AED) for our proposed method shows a decreasing trend with the increase in tie strength. It is worth noting that the AED for our proposed method quickly decreases when the value of tie strength reaches 0.5, while the AED for our proposed method shows a stable tendency when the value of tie strength is greater than 0.7. In terms of ACC, we easily obtain a similar conclusion. Therefore, we conclude that our proposed method performs better when the value of tie strength is configured between 0.5 and 0.7.

![](/api/attachments/JB75YS3Y/fulltext/images/91c7ab4da361a28812f37c29dde3c1ee7ce5933bc1bb21be0a9c17b85d5d22ab.jpg)  
Fig. 9. Performance comparison with different tie strengths.

As a whole, our proposed method, STFG, exceeds state-of-theart methods. However, this study admittedly has some limitations. First, we consider only tweets in English, that is, we extract locations in English from tweets. Twitter allows users to post in multiple languages, and users may also use different languages to communicate. Thus, we fail to capture locations in other languages in our sample. Second, our method cannot precisely estimate the home location for users who frequently move. Fortunately, these users are very rare. Most users engage in activities within a certain regional range. In the future, we will consider a time factor to infer users’ home locations, that is, we can estimate users’ home locations in different time intervals.

## 6. Conclusions

In this paper, we study the problem of inferring a home location for each user in Twitter social networks. We detail the problem and propose a social tie factor graph (STFG) model to estimate a Twitter user’s city-level location. We discover several interesting patterns via careful investigation. We incorporate social network data, usercentric data and tie strength into the proposed STFG model to profile user location. In STFG, labeled relationships in social networks are modeled as nodes, while attributes and correlations are modeled as factors. An efficient algorithm is proposed to learn model parameters and predict unknown relationships. We evaluate our proposed model on a large Twitter dataset, and the experimental results show that the proposed model can significantly improve performance for inferring home locations compared with several state-of-the-art methods.

In the future, we intend to extend our work in the following two directions. First, we will consider a time factor to estimate the home location for users who move frequently. Second, we will also further study our proposed STFG to improve the predictive performance by incorporating other social networks, e.g., Facebook.

## Acknowledgements

This work is supported by the National Natural Science Foundation of China under Grant No. 61202238, No. 61300006,

No. 61035004, and No. 61273213; the Fundamental Research Funds for the Central Universities under Grant No. YWF-13-D2- XX-07; the Project of the State Key Laboratory of Software Development Environment under Grant No. SKLSDE-2011ZX-08; and the award from the China Scholarship Council (student No. is 201406020044).

## References

[1] E. Amitay, N. Har’El, R. Sivan, A. Soffer, Web-a-where: geotagging web content, SIGIR’04, 2004, pp. 273–280.

[2] L. Backstrom, J. Kleinberg, R. Kumar, J. Novak, Spatial variation in search engine queries. WWW. 2008.

[3] L. Backstrom, E. Sun, C. Marlow, Find me if you can: improving geographica prediction with social and spatial proximity, WWW, 2010, pp. 61–70.

[4] N.K. Baym, A. Ledbetter, Tunes that bind? Predicting friendship strength in a music-based social network Inf. Commun. Soc. 12 (3), 2009, pp. 408–427.

[5] B. Bishop, The Big Sort: Why the Clustering of Like-Minded America is Tearing Us Apart, Houghton Mifflin Harcourt, 2009.

[6] X. Cao, G. Cong, C.S. Jensen, Mining significant semantic locations from GPS data, Proc. VLDB Endow. 3 (1–2), 2010, pp. 1009–1020.

[8] J. Chen, Y. Liu, Z. Wu, et al., Recommending interesting landmarks in photo sharing sites, Neural Netw. World 24 (3), 2014, pp. 285–308.

[9] Z. Cheng, J. Caverlee, K. Lee, You are where you tweet: a content-based approach to geo-locating twitter users, in: Proceedings of the 19th ACM international confer ence on Information and knowledge management, ACM, 2010, pp. 759–768.

[10] E. Cho, S.A. Myers, J. Leskovec, Friendship and mobility: user movement in location-based social networks, in: Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2011, pp. 1082–1090.

[11] D.J. Crandall, L. Backstrom, D. Huttenlocher, J. Kleinberg, Mapping the world’s photos, WWW, 2009, pp. 761–770.

[12] D.J. Crandall, L. Backstrom, D. Cosley, S. Suri, D. Huttenlocher, J.M. Kleinberg, Inferring social ties from geographic coincidences, Proc. Natl. Acad. Sci. U. S. A. 107 (52), 2010, pp. 22436–22441.

[13] V. de Graaff, V. van Keulen, R.A. de By, Towards geosocial recommender systems in: Proceedings of the 4th International Workshop on Web Intelligence & Com munities, ACM, 2012, p. 8.

[14] C. Fink, C. Piatko, J. Mayfield, T. Finin, J. Martineau, Geolocating blogs from their textual content, AAAI 2009 Spring Symposia on Social Semantic Web: Where Web 2.0 Meets Web 3.0, 2009.

[15] E. Gilbert, K. Karahalios, Predicting tie strength with social media, in: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, April, 2009, pp. 211–220.

[16] M.S. Granovetter, The strength of weak ties, Am. J. Sociol. 1973, pp. 1360–1380.

[17] M. Gupte, T. Eliassi-Rad, Measuring tie strength in implicit social networks, in: Proceedings of the 3rd Annual ACM Web Science Conference, ACM, 2012, pp. 109–118.

[18] C.A. Haythornthwaite, The Internet in Everyday Life, Blackwell, Oxford, 2002.

[19] https://blog.twitter.com//new-tweets-per-second-record-2013and-how.

[20] B. Hecht, L. Hong, B. Suh, et al., Tweets from Justin Bieber’s heart: the dynamics of the location field in user profiles, in: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, 2011, pp. 237–246.

[21] http://www.telegraph.co.uk/technology/twitter/9945505/Twitter-in-numbers. html.

[22] http://zh.wikipedia.org/wiki/SimRank.

[23] Y. Ikawa, M. Enoki, M. Tatsubori, Location inference using microblog messages, in: Proceedings of the 21st international conference companion on World Wide Web, ACM, 2012, pp. 687–690.

[24] T. Joachims, Making Large-Scale SVM Learning Practical, MIT-Press, 1999.

[25] J.J. Jones, J.E. Settle, R.M. Bond, et al., Inferring tie strength from online directed behavior, PLOS ONE 8 (1), 2013, p. e52168.

[26] D. Jurgens, That’s What Friends Are For: Inferring Location in Online Social Media Platforms Based on Social Relationships, ICWSM, 2013.

[27] I. Kahanda, J. Neville, Using transactional information to predict link strength in online social networks, ICWSM, June, 2009.

[28] L. Katz, A new status index derived from sociometric analysis, Psychometrika 18 (1), 1953, pp. 39–43

[29] L. Khan, F.B. Muhaya, Estimating twitter user location using social interactions – a content based approach, Privacy, Security, Risk and Trust (PASSAT) and 2011 IEEE Third International Conference on Social Computing (SocialCom), 2011, pp. 838–843.

[30] J.D. Lafferty, A. McCallum, F.C.N. Pereira, Conditional random fields: probabilistic models for segmenting and labeling sequence data, ICML’01, 2001, pp. 282–289

[31] J. Leskovec, D. Huttenlocher, J. Kleinberg, Predicting positive and negative links in online social networks, WWW’10, 2010, pp. 641–650.

[32] R. Li, S. Wang, H. Deng, et al., Towards social user profiling: unified and discriminative influence model for inferring home locations, in: Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2012, pp. 1023–1031.

[33] R. Li, S. Wang, K.C.C. Chang, Multiple location profiling for users and relationships from social network and content, Proc. VLDB Endow. 5 (11), 2012, pp. 1603–1614.

[34] J. Lin, A. Halavais, Mapping the blogosphere in America, Workshop on the Weblogging Ecosystem at the 13th International World Wide Web Conference 2004.

[35] T. Lou, J. Tang, J. Hopcroft, et al., Learning to predict reciprocity and triadic closure in social networks, ACM Trans. Knowl. Discov. Data 7 (2), 2013, p. 5.

[36] J. McGee, Caverlee J.A., Z. Cheng, A geographic study of tie strength in social media, in: Proceedings of the 20th ACM International Conference on Information and Knowledge Management, ACM, 2011, pp. 2333–2336.

[37] K. Murphy, Y. Weiss, M. Jordan, Loopy belief propagation for approximate inference: an empirical study, UAI, vol. 9, 1999, pp. 467–475.

[38] A. Popescu, G. Grefenstette, Mining user home location and gender from flickr tags, ICWSM, 2010.

[39] T. Rattenbury, N. Good, M. Naaman, Towards automatic extraction of event and place semantics from flickr tags, SIGIR, 2007, pp. 103–110.

[40] A. Sadilek, H. Kautz, J.P. Bigham, Finding your friends and following them to where you are, in: Proceedings of the fifth ACM international conference on Web search and data mining. ACM. 2012, pp. 723–732

[41] Y. Takhteyev, A. Gruzd, B. Wellman, Geography of Twitter networks, Soc. Netw. 34 (1), 2012, pp. 73–81.

[42] C.E. Thormann, M.E. Ferreira, L.E.A. Camargo, J.G. Tivang, T.C. Osborn, Comparison of RFLP and RAPD markers to estimating genetic relationships within and among cruciferous species, Theor. Appl. Genet. 88 (8), 1994, pp. 973–980.

[43] S. Wu, J. Sun, J. Tang, Patent partner recommendation in enterprise social networks, in: Proceedings of the Sixth ACM International Conference on Web Search and Data Mining, ACM, 2013, pp. 43–52.

[44] R. Xiang, J. Neville, M. Rogati, Modeling relationship strength in online social networks, in: Proceedings of the 19th international conference on World Wide Web, ACM, April, 2010, pp. 981–990.

[45] E.P. Xing, M.I. Jordan, S. Russell, A generalized mean field algorithm for variational inference in exponential families, UAI’03, 2003, pp. 583–591.

[46] S. Yardi, D. Boyd, Tweeting from the town square: measuring geographic local networks, ICWSM, 2010

[47] S. Yoo, Y. Yang, F. Lin, I.C. Moon, Mining social networks for personalized email prioritization, in: Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, June, 2009, pp. 967–976.

[48] X. Zhao, J. Yuan, G. Li, X. Chen, Z. Li, Relationship strength estimation for online social networks with the study on Facebook, Neurocomputing 95, 2012, pp. 89–97.

Jinpeng Chen is a PhD candidate in the School of Computer Science and Engineering at Beihang University. He received his Master’s degree from Beijing jiaotong University, Beijing, China in 2009. His research interests include social network analysis, recommendation systems, data mining methodologies, machine learning algorithms, and information retrieval techniques.

Yu Liu received a PhD from Beihang University in 2010. He is now an assistant professor in the Department of Computer Science and Technology at Beihang University. His research interests include data mining, cloud computing, and natural language processing. He is a member of CCF.

Ming Zou is a Master’s student in the School of Computer Science and Engineering at Beihang University. His research interests include large-scale data analysis and information retrieval techniques.
