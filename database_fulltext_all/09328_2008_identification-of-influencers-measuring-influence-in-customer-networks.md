---
otero_id: 9328
otero_key: "5889BVGK"
title: "Identification of influencers — Measuring influence in customer networks"
authors: "Christine Kiss; Martin Bichler"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.06.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers — Measuring in<sup>fl</sup>uence in customer networks

Christine Kiss, Martin Bichler ⁎

Internet-based Information Systems, Department of Informatics, TU München, Germany

a r t i c l e i n f o

Article history: Received 3 February 2007 Received in revised form 4 June 2008 Accepted 22 June 2008 Available online 2 July 2008

Keywords: Customer relationship management Viral marketing Centrality Network theory Word of mouth marketing

## a b s t r a c t

Viral marketing refers to marketing techniques that use social networks to produce increases in brand awareness through self-replicating viral diffusion of messages, analogous to the spread of pathological and computer viruses. The idea has successfully been used by marketers to reach a large number of customers rapidly. If data about the customer network is available, centrality measures provide a structural measure that can be used in decision support systems to select in<sup>fl</sup>uencers and spread viral marketing campaigns in a customer network. Usage stimulation and churn management are examples of DSS applications, where centrality of customers does play a role. The literature on network theory describes a large number of such centrality measures. A critical question is which of these measures is best to select an initial set of customers for a marketing campaign, in order to achieve a maximum dissemination of messages. In this paper, we present the results of computational experiments based on call data from a telecom company to compare different centrality measures for the diffusion of marketing messages. We found a signi<sup>fi</sup>cant lift when using central customers in message diffusion, but also found differences in the various centrality measures depending on the underlying network topology and diffusion process.

© 2008 Elsevier B.V. All rights reserved.

## 1. Motivation

Due to the wealth of data that is available in today's marketing departments data mining and econometrics, in particular classi<sup>fi</sup>cation techniques, have gained considerable importance for tasks such as churn prediction or campaign management to raise product or brand awareness [6]. These techniques are typically based on information about individual characteristics of customers, where decision tree learners or logistic regressions are used to estimate the probability of a person to respond to a campaign, to buy a product, or to switch to another provider [53,37,12,36].

## 1.1. Customer networks and word-of-mouth marketing

Beyond individual customer characteristics, the structure of customer networks has attracted much attention in the marketing literature. Repeatedly, research has shown the importance of consumer word-of-mouth (WOM) communication in the formation of attitudes [15], in a purchasing decisionmaking context [7], and in the reduction of risk associated with consumer buying decisions [48,31]. WOM is an informal communication behavior about the experiences with speci<sup>fi</sup>c services, products or the characteristics of the providers that the consumers exchange among each other [59].

The distribution of the WOM message varies with the degree of satisfaction and dissatisfaction of the consumers [5,47]. One of the few empirical analyses of this effect shows that customer satisfaction has a positive impact on word-ofmouth, which in turn has a positive impact on sales and market share [24]. Another empirical investigation of wordof-mouth [5] con<sup>fi</sup>rms popular expectations that dissatisfaction produces more negative word-of-mouth than satisfaction produces positive word-of-mouth.

One of the challenges in measuring word of mouth is that it is dif<sup>fi</sup>cult to observe what is usually the content of private conversations. Therefore, much of this literature is based on surveys, but not on direct observations (see for example [17]). New online communities allow for direct observation. Through monitoring online conversations, Godes et al. [31] demonstrate how word of mouth can be measured. In addition, they show a relationship between the overall dispersion of online conversations across online communities and the popularity of television shows. Recently, Van den Bulte et al. [55] have described a formal model of in<sup>fl</sup>uentials in a network.

Since WOM has such an enormous impact on customer opinions and buying decisions, marketing departments try to focus more and more on in<sup>fl</sup>uential customers. ”To succeed today, you need to connect with people who are at the center of the conversation… Specifically, you should make sure you are reaching the decision makers who are influential in others decisions. Influentials are well connected, they have ties to a significantly larger number of groups than the average American.” [38].

In order to promote and manage WOM communications, marketers use for example viral marketing methods to achieve the desired behavioral response. Viral marketing refers to marketing techniques that use social networks to produce increases in brand awareness by ”viral” diffusion processes, analogous to the spread of pathological and computer viruses. It can be very useful in reaching a large number of people rapidly. The assumption is that if a campaign reaches a ”susceptible” user, that user will become ”infected” and can then go on to infect other susceptible users [40,45]. Arguably, these forms of marketing work best when centered on in<sup>fl</sup>uencers: in<sup>fl</sup>uencers supply the authority that allows a message to be conveyed quickly and reliably through WOM techniques [40].

## 1.2. DSS applications

The literature on WOM marketing describes multiple attributes of in<sup>fl</sup>uencers. For example, Keller and Berry [38] argue that in<sup>fl</sup>uencers have multiple interests, they tend to be early adopters in markets, they are trusted by others, and have a large social network. In this paper, we focus on the latter, in particular on centrality metrics that identify, how well different customers can serve as in<sup>fl</sup>uencers in their social network.

Such metrics of customer centrality can be useful in a variety of DSS applications, including message spreading in viral marketing campaigns to raise brand or product awareness, usage stimulation, or churn management. Obviously the position of a customer in the customer network does have an important impact on their ability to spread marketing messages. As already mentioned, classi<sup>fi</sup>cation techniques are typically used in DSS to predict a customer's willingness to respond to or forward a message. These predictions ignore a customers capability of forwarding based on the topology of his customer network. Classi<sup>fi</sup>cation models will provide a list of customers with a high likelyhood of forwarding or responding to a message. In addition, a centrality measure can be used to select those customers, who not only have a high likelihood of forwarding a message, but whose position in the network allows them to reach a large number of other customers. We will focus on this type of decision support for viral marketing campaigns in this paper, which aim at increasing awareness of a product or service. Examples might be new broadband services or the possibility to switch from paper-based to online bills.

Usage stimulation is similar, in the sense that the network operator actively stimulates usage of particular services such as the short message service (SMS) or the multimedia message service (MMS). Also in these cases the main barrier to usage is mostly lack of awareness and familiarity with a new service, while price is often less of an issue. Therefore, operators regularly approach customers with templates for SMS or MMS messages to be sent to friends and acquaintances, in order to stimulate usage and make customers familiar with a new service. Also here, scoring models predicting the likelihood of using such a service can be combined with the centrality measure to select customers to be included in a campaign.

Finally, centrality can be important in churn management applications, a topic of signi<sup>fi</sup>cant importance to service providers. A typical task in churn management is to identify those who are likely to churn (often also using classi<sup>fi</sup>cation techniques) and then act on those who have a high ”customer lifetime value” (CLTV). On the other hand, operators don't want to lose a customer, who interacts with many people, even if his CLTV is low, because he might infect others in his community.

## 1.3. Network analysis

Applications of this sort require knowledge about the social network of customers and their interactions, which are typically dif<sup>fi</sup>cult and expensive to elicit. Nowadays, more and more data is available on the Internet about customer networks and customer recommendations. For example, Leskovec et al. [45] have recently analyzed data from a person-to-person recommendation network. Besides these new online data sources, the telecommunication industry accumulates huge amounts of data about customer interactions in the form of call data records. Although information about the content of a communication (e.g., whether there was an explicit recommendation or not) is typically not available, the frequency of interactions and the resulting network of customer interactions contain valuable information for a marketer and can be used as an estimator for the in<sup>fl</sup>uential power of a person. In this paper, we focus on structural metrics about the in<sup>fl</sup>uential power of customers that can be estimated based on data about customer interactions, as they are available with telecommunication providers.

Network theory concerns itself with the study of graphs as a representation of relations between discrete objects. Within network theory, there are various measures of the centrality of a vertex within a graph that determine the relative importance of a vertex, for example, how important a person is within a social network. In other words, the centrality of a node in a network is a measure of the structural importance of the node. A central customer, presumably, has a stronger in<sup>fl</sup>uence on other network members. Multiple centrality measures have been de<sup>fi</sup>ned in the literature, which are used for very different purposes (e.g., layout of local area networks, web search). Some of these measures exhibit high computational complexity, while others are simple to calculate. Recent literature on network analysis has shown that the centrality measures need to be matched to the network <sup>fl</sup>ow and application for which they are appropriate [16].

## 1.4. Focus of the paper

Our main question is: “Given a customer network: How do we select the most important in<sup>fl</sup>uencers and to what extent can messages be disseminated in the network via these highly in<sup>fl</sup>uencing nodes.” In other words, we analyze how well individuals distribute messages based on the topology of their network. This will also be referred to as the “performance” of a centrality measure.

In order to answer this question, we conduct large numbers of experiments based on <sup>fi</sup>eld data of the customer network from a telephone operator. We measure how the selection of an initial set of customers in<sup>fl</sup>uences the reach-out to other members of the network, measured by the number of customers reached after different models of message diffusion. We found that if the set of initial customers (represented as nodes in the network) is chosen according to SenderRank or out-degree measures, the number of reached customers is substantially higher than selecting the initial set of customers according to other centrality measures across different treatments. Thus, it is these measures that the designer of a marketing campaign should use in order to achieve a wide dissemination of marketing messages. Note that centrality is orthogonal to discrete choice models of customer preferences as they are typically used in marketing. In our analysis, we assume no signi<sup>fi</sup>cant differences in the customer preferences for particular messages. Typically, both measures would be used in combination in order to select appropriate target customers for a marketing campaign. For example, centrality can be used as a metric to rank-order customers that have a high probability of being interested in a message.

Therefore, the article is structured as follows. In Section $^ { 2 , }$ we introduce related theory and empirical results from the <sup>fi</sup>eld of network theory. This includes structural measures of in<sup>fl</sup>uence and diffusion theory in a network. In Section 3 we describe the computational experiments to benchmark different centrality measures, and in Section 4, we draw conclusions and provide an outlook on future research.

## 2. Network theory

Traditionally, the study of complex networks has been the <sup>fi</sup>eld of graph theory. While graph theory initially focused on regular graphs, since the 1950′s large scale networks with no apparent design principles were described as random graphs, proposed as the simplest and most straightforward realization of a complex network [3]. Erdös and Rényi de<sup>fi</sup>ne a random graph as n labelled nodes $i \in N$ with $i = 1 , \ldots ,$ n connected by a set of E edges which are chosen randomly from the $\frac { n ( n - 1 ) } { 2 }$ possible edges [25]. In these networks, the majority of nodes have a degree that is close to the average degree of the overall network.

![](/api/attachments/5889BVGK/fulltext/images/00af6e8ecd8297d6922b86d1bcd2a3a3eb98a21f8d78e4d0b029678979bfa166.jpg)  
(a) Random network

![](/api/attachments/5889BVGK/fulltext/images/0e653e008cd3e2c5cbd886eca3202981b0bf877b82552c924f029862d14872b7.jpg)  
(b) Scale-free network  
Fig. 1. Random Networks versus Scale Free Networks [21].

Empirical analysis of large networks such as the Internet, the Web, or large phone networks found different characteristics [4]. In particular, the degree distribution mostly followed a power-law distribution. Networks that follow a power law distribution are called scale-free networks. In this section we will discuss properties of scale-free networks as well as structural measures of in<sup>fl</sup>uence of nodes in a network, and models of message diffusion to provide the underlying rationale for our computational experiments.

## 2.1. Scale-free networks

Scale-free networks tend to contain centrally located and extensively high degree “hubs”. They attach new members over time and the attachment prefers existing members that are already well connected. This principle of “preferential attachment” leads to interesting properties that have to be taken into consideration. Their behavior in terms of diffusion and communication processes is fundamentally different from that of random networks (Fig. 1).

In the past few years, there have been substantial advances in this area. Three concepts occupy a prominent place in contemporary thinking about complex networks. We will brie<sup>fl</sup>y discuss them in order to characterize our empirical data based on these characteristics:

## 2.1.1. Degree distribution

The spread in the number of edges of a node, or node degree, is characterized by a distribution function P(k), which describes the probability that a randomly selected node i has exactly $k _ { i }$ edges. Empirical results show that for most large networks, including the World Wide Web [4], Internet [26], or metabolic networks [35], the degree distribution follows a power law $P ( k ) =$ $k ^ { - \alpha }$ . Aiello et al. [2] analyzed the degree distribution of a phone call network and found a power law distribution with an exponent of $\alpha { = } 2 . 1$ . The higher a power–law coef<sup>fi</sup>cient is, the fewer edges has a network (with the same number of nodes). This also implies that with a higher power–law coef<sup>fi</sup>cient less people can be reached with a campaign.

## 2.1.2. Clustering coefficien

A common property of social networks that can often be described by a power law distribution is that cliques are formed, representing groups of friends or acquaintances in which every member knows every other member. This inherent tendency to clusters is quanti<sup>fi</sup>ed by the clustering coef<sup>fi</sup>cient [58]. The clustering coef<sup>fi</sup>cient of a node i for an undirected graph is twice the ratio between the number of edges |e |, which connect the k neighbors, divided by the total number of possible edges $k _ { i } ( k _ { i } - 1 )$ , where $N _ { i }$ is the set of neighbors of node i, and E the set of edges:

$$
C C _ {i} = \frac {2 \left| e _ {j l} \right|}{k _ {i} \left(k _ {i} - 1\right)}: j, l \in N _ {i}, e _ {j l} \in E\tag{1}
$$

The clustering coef<sup>fi</sup>cient of a whole network is the average clustering coef<sup>fi</sup>cient of all nodes $\begin{array} { r } { C C _ { i } = \frac { 1 } { n } \sum _ { i \in N } C _ { i } } \end{array}$

## 2.1.3. Average path length

The path length between two nodes of a network is de<sup>fi</sup>ned as the number of edges between them. The minimal path length is the shortest path between two nodes (also called geodesic distance). The average path length is the average of all the minimum path lengths between all pairs of nodes in a network. The small world concept in simple terms describes the fact that despite their mostly large size, in most real networks there is a relatively short path between any two nodes. These small world graphs typically exhibit a number of characteristics, such as a low diameter and a low clustering coef<sup>fi</sup>cient.

Numerous studies have been initiated by the desire to understand various real systems ranging from communication networks to ecological webs. A comprehensive survey of different real networks and their characteristics is provided in Albert and Barabasi [3].

## 2.2. Structural measures of influence in a network

In the social network community, a variety of measures were designed for the measurement of importance or prominence of nodes in a network [29,14]. In the following, we will brie<sup>fl</sup>y summarize the most well-known centrality measures, as well as a number of link topological ranking measures, which describe possible candidate indicators for the power of in<sup>fl</sup>uentials in message diffusion.

## 2.2.1. Centrality measures

A centrality measure C is a function C : NY that associates to each vertex i∊N a non negative real number $C ( i )$

2.2.1.1. Degree centrality. Degree centrality is the simplest centrality measure. The degree of a node i denoted by $k _ { i } ,$ is the number of edges that are incident with it, or the number of nodes adjacent to it. For networks where the edges between nodes are directional, we have to distinguish between indegree and out-degree. The out-degree centrality is de<sup>fi</sup>ned as

$$
C _ {D _ {0}} (i) = \sum_ {j = 1} ^ {n} a _ {i j}\tag{2}
$$

where $a _ { i j }$ is 1 in the binary adjacency matrix A if an edge from node i to j exists, otherwise it is 0. Similarly, the in-degree centrality is de<sup>fi</sup>ned as

$$
C _ {D _ {I}} (i) = \sum_ {j = 1} ^ {n} a _ {j i}\tag{3}
$$

where i describes the node i and $a _ { j i }$ is 1 if an edge from node j to i exists, otherwise it is 0.

2.2.1.2. Closeness centrality. The closeness centrality measures howclose a node is to all the other nodes in the set of vertices and is often used in social network analysis. As noted by Beauchamp [11], members occupying central locations with respect to closeness can be very productive in communicating information to the other members. Hakimi [33] and Sabidussi [52] developed a measure that central members are close, by stating that central nodes in a network have shortest paths to all other nodes. The closeness centrality index for directional relations is

$$
C _ {C} (i) = \frac {1}{\sum_ {j = 1} ^ {n} d (i , j)}\tag{4}
$$

where $d ( i , j )$ denotes the distance between node i and j, which is the minimum length of any path connecting i and $j .$

Wassermann and Faust [57] proposed the following standardization of this measure to account for the size of the network:

$$
C _ {C} (i) = \frac {(n - 1)}{\sum_ {j = 1} ^ {n} d (i , j)}\tag{5}
$$

The problem with this de<sup>fi</sup>nition of closeness centrality is that closeness is not de<sup>fi</sup>ned unless the digraph is strongly connected, in such a way as each node has a direct path from i to j, otherwise, some of the $d ( i , j )$ will be ∞ and the Eq. (5) would be unde<sup>fi</sup>ned. Therefore, Lin [46] de<sup>fi</sup>ned $J _ { i }$ as the number of nodes which are reachable from node i and propose to consider only the distances of these reachable nodes:

$$
C _ {C} (i) = \frac {j _ {i} / (n - 1)}{\left(\sum_ {j = 1} ^ {n} d (i , j)\right) / J _ {i}}\tag{6}
$$

2.2.1.3. Betweenness centrality. Interactions between two non-adjacent nodes might depend on the other nodes in the set of nodes, especially those nodes which lie on the path between the two. The node between the other two nodes can therefore control the interaction between the two nonadjacent nodes. The idea is that a node is central if it lies between other nodes on their geodesics, implying that, in order to have a large betweenness centrality, the node must be between many of the nodes via their geodesics. The betweenness centrality index is de<sup>fi</sup>ned by Freemann [28] as

$$
C _ {B} (i) = \frac {\sum_ {i \neq j \neq l} g _ {j l} (i)}{g _ {j l}}\tag{7}
$$

where $g _ { j l } ( i )$ is the number of shortest paths linking the two nodes j and l containing node i. The computation of betweenness centrality is computationally expensive. Brandes [18] proposed an algorithm for betweenness that exploits the sparseness of typical networks to reduce the time complexity of this computation from $O ( n ^ { 3 } )$ to $O ( n ^ { 2 } +$ nk) and space complexity from $O ( n ^ { 2 } )$ to $O ( n + k ) .$ . Moreover, other shortest-path based indices, like closeness, can be computed simultaneously within the same bounds.

2.2.1.4. Eigenvector centrality. The eigenvector centrality is another measure of the importance of a node in a network. Here, the centrality of a node i is a function of the centrality of the nodes connected to i. Being nominated as powerful by someone seen by others as powerful should contribute more to one's perceived power. Let A again be the binary adjacency matrix of the network and <sup>Y</sup>x be the principal eigenvector corresponding to the maximum eigenvalue θ. The eigenvector centrality for a node i can be de<sup>fi</sup>ned as a single element of the eigenvector calculated as:

$$
C _ {E} (i) = x _ {i} = \frac {1}{\theta} \sum_ {j = 1} ^ {n} a _ {j i} x _ {j}\tag{8}
$$

Here, each individual's status is merely proportional (not necessarily equal) to the weighted sum of the individuals to whom he is connected. Eigenvalues of large matrices are typically computed numerically [32]. For example, inverse iteration is an iterative eigenvalue algorithm to calculate the eigenvalues and eigenvectors of a matrix. The computational complexity of inverse iteration can be reduced to $O ( n ^ { 2 } )$ if one <sup>fi</sup>rst reduces the adjacency matrix A to a Hessenberg form.

2.2.1.5. Edge-weighted degree centrality. In the case of phone call networks, we have not only binary information about the communication of two members, but also a weighted digraph describing how often a member called another one, or how many short messages he sent. In this case, the entries of an adjacency matrix $a _ { i j }$ describe the numeric weights of a connection from node i to j. Each weighted graph can easily be transformed into a multigraph, where the same pair of vertices can be connected by multiple edges [49]. In this paper, we de<sup>fi</sup>ne edge-weighted degree centrality as:

$$
C _ {E D} (i) = \sum_ {j = 1} ^ {n} \left(a _ {i j} + a _ {j i}\right)\tag{9}
$$

## 2.2.2. Link topological ranking measures

Most of the previously described centrality measures (except eigenvector centrality) disregard the type of node. There are very in<sup>fl</sup>uential vertices to which a connection is more valuable than to others. With regard to social networks, a connection to a node with high centrality might be more valuable than to a node with only one neighbor. Web search engines leverage this information with HITS and PageRank probably being the most popular Web search algorithms.

Kleinberg [41] proposed a Web search algorithm called HITS (Hyperlink-Induced Topic Search) which identi<sup>fi</sup>es authoritative pages and a set of hub pages. Authoritative pages are pages which have many incoming links and hubs are pages that link to many related authorities. An iterative algorithm is used to <sup>fi</sup>nd the equilibrium values for the authority and hub weights of a web page or node in a network respectively. This is reached if the difference of the weights between two iterations is less than a threshold value. For each page i a nonnegative authority weight $C _ { A } ( i )$ and a nonnegative hub weight $C _ { H } ( i )$ is associated. The weights of each type are normalized so their squares sum to 1 and are de<sup>fi</sup>ned as:

$$
C _ {A} (i) = \sum_ {j = 1} ^ {n} a _ {j i} C _ {H} (j)\tag{10}
$$

$$
C _ {H} (i) = \sum_ {j = 1} ^ {n} a _ {i j} C _ {A} (j)\tag{11}
$$

where $a _ { j i }$ is 1 if an edge from node j to i exists otherwise 0. An iterative algorithm has been de<sup>fi</sup>ned to <sup>fi</sup>nd the equilibrium values for the weights. When the equilibrium is reached the most central nodes are those with the highest authority weight.

The PageRank algorithm, which was originally developed by Brin and Page [19], the founders of the Google search engine, maintains only a single metric for each web page. The so called PageRank is transmitted from the source page to the link target, and the value depends on the PageRank of the source page. So a link from a page that has large PageRank, such as the Yahoo home page, contributes more than a link from a page with low PageRank. The PageRank of page or node i is the sum of contributions from its incoming links or edges. A constant damping factor f is the probability at each page that the “random surfer” will get bored and requests another random page. Additionally (1−f) is added to each node. This is done because if a node has an out-degree of zero then his PageRank would be zero. This zero-value would be passed down to the original node. To avoid this, a constant value is added to the PageRank. The PageRank can be de<sup>fi</sup>ned as:

$$
C _ {P R} (i) = (1 - f) + f \sum_ {j \in M _ {i}} \frac {C _ {P R} (j)}{C _ {D _ {0}} (j)}\tag{12}
$$

where $M _ { i }$ is the set of source pages that link to i and $C _ { D _ { o } } ( j )$ is the out-degree of page j as described in the previous subsection. The damping factor f is often set to value of 0.85 [19].

The PageRank is a variant of the eigenvector centrality with the difference that instead of the adjacency matrix, the Markov matrix is used. This is a reason, why we will only consider the PageRank in our experiments. A Markov matrix is the transition matrix for a <sup>fi</sup>nite Markov chain. Elements of the matrix must be real numbers in the closed interval [0,1], where each element represents the transition probability from one page to the other page. Hence, if a connection exists between page i and ${ } _ { j , \ l }$ then the element of the Markov matrix in row i and column j is $1 / C _ { D _ { \circ } } ( j )$ , where $C _ { D _ { o } } ( j )$ is the outdegree or out-degree centrality of the page j.

Web search algorithms such as PageRank focus on incoming links, since they count only the weighted number of incoming links and ignore the outgoing links. For information diffusion models, the out-degree is the more important measure. For this reason, we introduce a measure called SenderRank, which is based on the PageRank calculation apart from the direction of in<sup>fl</sup>uence.

$$
C _ {S R} (i) = (1 - f) + f \sum_ {j \in L _ {i}} C _ {S R} (j)\tag{13}
$$

where $L _ { i }$ is the set of pages the page i links to.

## 2.3. Comparisons of centrality measures

Several authors compared the performance of the existing centrality measures, either on empirical or on simulated data. Wassermann and Faust [57] provide a review of the early comparative studies. The <sup>fi</sup>rst study of centrality measures was conducted by Freemann [29]. He analyzes the consistency of centrality measures with intuitions and their interpretability (e.g., control of communication, or communication activity). Freemann et al. [30] evaluated three centrality measures on four different graphs, all with n=5 and found that betweenness best measured which member in the set of members was viewed most frequently as a leader. Another observation was that degree and betweenness centrality are important indicators for group performance (with respect to ef<sup>fi</sup>ciency of problem solving) while closeness centrality was not even vaguely related to their experimental results on communication activity.

Bolland [13] studied four centrality measures. He examined a network data set giving in<sup>fl</sup>uence relationships among forty people involved in educational policy-making. In addition, he conducted a Monte Carlo analysis by adding random and systematic variation to the network to obtain a number of noisy networks. Bolland's <sup>fi</sup>ndings supported the earlier work of Freemann [29]. Speci<sup>fi</sup>cally, degree-based measures of centrality were sensitive to small changes in network structure. Betweenness-based measures of centrality were considered useful and capable of capturing small changes in the network. Closeness centrality was found to be very sensitive to network change.

Costenbader and Valente [23] evaluated the stability of centrality measures when networks are sampled in the face of inaccurate or incomplete network data. It turned out that the most robust centrality measure is eigenvector centrality as a simple raw score followed by indegree centrality. They are less affected by sampling than outdegree and betweenness centrality.

Recently, Koschtuezki and Schreiber [42] calculated <sup>fi</sup>ve different centrality measures for all the vertices of two networks and ordered the vertices according to their centrality. Using these rankings, they calculated the correlation of centrality measures and found that these correlations differ between the two networks. The correlation between eigenvector centrality and degree centrality was however high in both networks.

Only recently, researchers have started to analyze and compare centrality measures based on the underlying network <sup>fl</sup>ow or diffusion model. Borgatti [16] showed how centrality measures can be matched to different kinds of network <sup>fl</sup>ow for which they are appropriate. A process can <sup>fl</sup>ow in different ways through a network. He classi<sup>fi</sup>ed network <sup>fl</sup>ow along different dimensions. For example, he makes a distinction, whether diffusion occurs via replication or transfer, if it is deterministic as in a computer network or undirected, describing a blind <sup>fl</sup>ow of traf<sup>fi</sup>c, as is the case with marketing messages. Based on the resulting classi<sup>fi</sup>cation, Borgatti [16] assigned respective centrality measures. The authors considered only <sup>fl</sup>ows with a pre-de<sup>fi</sup>ned source and a target. In this paper, we will focus on centrality measures for the diffusion of marketing messages, where no prede<sup>fi</sup>ned target exists, which is the most wide-spread application in viral marketing.

## 2.4. Diffusion in networks

Closely linked to network theory are theories about the diffusion of messages or epidemics within networks. No matter if it is a virus disease, a computer virus, or a marketing message, they all have in common that they disperse through networks by spreading from one individual to their direct neighbors.

In the marketing literature, Bass [10] published an in<sup>fl</sup>uential model on ”A new product growth model for consumer durables” that motivated a stream of research on product innovation and diffusion. The Diffusion of Innovations Theory explains the dissemination of ideas; however, the actual spread of messages in a network requires different micro-level models closer in spirit to the models that have been developed to describe the diffusion of viruses.

## 2.4.1. Models for the diffusion of viruses

A number of models have been developed describing the spread of viruses of epidemics on a micro-level. Kermack and McKendrick [39] developed a mathematical framework called SIR-model for the spread of epidemics. SIR stands for susceptible-infected-removed. The probability of an individual to change from status susceptible to infected is given by δ and the probability that the status of a person changes from infected to removed is given by ν. How an infection spreads depends on $\lambda = \delta / \nu$ and the structure of the network [34].

Pastor-Satorras and Vespignani [50] analyzed the spreading properties of viruses by using data reported by the Virus

Bulletin. They analyzed in particular the survival probability of homogeneous groups of viruses. For larger time frames, they found an exponential decay of the virus diffusion. Chrisley et al. [22] simulated the transmission of infections to identify high-risk individuals. The authors analyzed centrality measures for their ability to identify high-risk individuals and found that degree centrality appeared to perform at least as well as alternative measures for this application.

## 2.4.2. A Model for Message Spreading in Social Networks

In the following, we will introduce a general model describing the spread of marketing messages in a customer network. We de<sup>fi</sup>ne the probability $P _ { j } ( i )$ of a node with k neighbors passing on a message to $j \leq k _ { i }$ of these neighbors based on a binomial distribution and a communication probability $\kappa .$ The j nodes are then selected randomly among the neighbors.

$$
P _ {j} (i) = \binom{k _ {i}}{j} \kappa^ {j} (1 - \kappa) ^ {\kappa - j}\tag{14}
$$

The difference between spreading of viruses and the spreading of messages is that virus infection can be cured, while once a message is received, a node stays ”infected”. Instead we do have a decay of the signal because a message gets old with time and might not be forwarded with increasing age. To account for that, a decay parameter τ is de<sup>fi</sup>ned. Initially every new message has a value of 1 that will be multiplied with a decay parameter τ for every hop in the network. This decay describes the level of trust a person puts into a message. Two different diffusion models were used, a model with exponential decay, and one with power law decay. In the model with exponential decay, the signal strength $\beta _ { i }$ of a message at node i which is q hops away from the original creator of the message is de<sup>fi</sup>ned as

$$
\beta_ {i} = \tau^ {q}\tag{15}
$$

with $0 < \tau < 1$ . In contrast, the model with power law decay, $\tau { > } 0 ,$ uses

$$
\beta_ {i} = (q + 1) ^ {- \tau}\tag{16}
$$

For example, a power law decay with a power law coef<sup>fi</sup>cient of 1.75 has been found by Wu et al. [61], who provided a study in another domain of textual similarity of Stanford student homepages.

A node only forwards a message the <sup>fi</sup>rst time he receives it. If he receives a message for the second time from another source, it is considered old and will not be propagated any more. However, if a node receives a message several times, the trust level of a message at node i adds up to $\sigma _ { i } .$ If a message was received s times at a node, then

$$
\sigma_ {i} = \sum_ {r = 1} ^ {s} \beta_ {r}\tag{17}
$$

In our computational experiments, we have set a threshold value ε, and if σ Nε, then a node has received the message. In addition, ω limits the number of times each message can be passed on to a neighbor, e.g., only 10 transmissions are allowed.

## 3. Computational experiments

In a <sup>fi</sup>rst step, we would like to <sup>fi</sup>nd out, how well individuals distribute messages based on the topology of their network. For this purpose, in our experiments we sent a message to a set of customers selected by a particular centrality measure and then analyzed, how many customers could be reached overall based on a particular diffusion model.

## 3.1. Experimental Setup

We have developed a software framework for the simulation of diffusion processes in social networks which consists of two main components. A network model generates different types of networks. Based on the degree distribution and the number of nodes, we can generate different instances of networks adhering to the characteristics of ER networks or scale-free networks. In addition, we had anonymized data about the customer network of a telecom company.

The second component is a set of diffusion models that models communication and message distribution between customers. We used the model with exponential decay and the one with power law decay, as described in Section 2.3. Different treatments were evaluated in the experiments: different networks, different diffusion models with different parameter-settings and different centrality measures. In the following we will introduce these treatments in more detail and then present the results.

## 3.1.1. Network models

We got two real world networks (call detail records) from a mobile phone provider. Their main characteristics are described in the <sup>fi</sup>rst lines of Table 1. The samples NW1 and NW2 were drawn following a breadth-<sup>fi</sup>rst search, i.e., by selecting a random node and including all its neighbors in the network and then all the neighbors of these neighbors until a certain number of nodes was reached. The two samples NW1 and NW2 have different initial nodes. The networks included a number of boundary nodes, mostly customers from other phone providers, whose communication behavior is not available. The network information consisted of the two anonymized phone-numbers of the calling customer and the callee. Furthermore, we had monthly aggregates about the communication behavior between the customers which included following attributes: the number of voice calls, the number of minutes of a voice call, the number of short messages (sms), the number of multimedia messages (mms), and the average communication usage (number of sms and voice calls) of the callee. We also gathered attributes about the calling customer, certainly only if the calling customer is a customer of the telecommunication provider. The attributes included the gender, the age, and the zip-code of the customer. The <sup>fi</sup>rst network aggregated one month of call detail records for the edge weights (which was calculated as number of sms+number of voice calls+number of mms) of the network and the second network two months.

We have also drawn two smaller samples, NW3 and NW4 from NW1 using breadth-<sup>fi</sup>rst search. In NW4 the boundary nodes from external networks were excluded, while in NW1– NW3 they were included. We only used anonymized data in this study. Table 1 also provides the clustering coef<sup>fi</sup>cients and the average path lengths for different networks.

In addition to the real world networks, we generated scale-free networks NW5–NW7 with different power–law coef<sup>fi</sup>cients resembling real-world networks that have been analyzed in the literature (2.1, 2.5, and 2.8) and two ERnetworks (NW8, NW9). This allowed us to evaluate centrality measures based on networks with other power–law coef<sup>fi</sup>- cients. NW5 to NW7 did also not have the large number of boundary nodes, which are a consequence of the sampling in NW1 to NW4 and simulate a complete scale-free network.

In addition, the table provides characteristics of networks from the literature about a network of actors in the same movies, co-authorship in Mathematics, and the WWW to be able to compare them against the characteristics of NW1–9.

We analyzed the degree distribution of customers from our telecom provider. Figs. 2 and 3 illustrate the degree distributions of NW1. Based on the logarithm of the observed values, we could identify a power law coef<sup>fi</sup>cient α=2.8 for the out-degree distribution, and 2.4 for the in-degree distribution. These distributional assumptions could be con<sup>fi</sup>rmed using a Kolmogorov–Smirnov test and a signi<sup>fi</sup>- cance level of 0.05. In comparison, Aiello et al. [2] analyzed a phone network of 53,000,000 nodes and observed a power law coef<sup>fi</sup>cient of 2.1 for both in- and out-degree distributions.

Characteristics of network topology

<table><tr><td>Network (NW)</td><td>Number of nodes</td><td>Number of edges</td><td>Type of network</td><td>External provider (boundary nodes)</td><td>Clustering coefficient</td><td>Avg. path length</td></tr><tr><td>NW 1</td><td>29,000</td><td>55,013</td><td>Real-world</td><td>Included (23,905)</td><td>0.1849</td><td>7.782</td></tr><tr><td>NW 2</td><td>54,839</td><td>118,475</td><td>Real-world</td><td>Included (42,227)</td><td>0.193</td><td>10.789</td></tr><tr><td>NW 3 (part of NW 1)</td><td>6721</td><td>11,309</td><td>Real-world</td><td>Included (5449)</td><td>0.182</td><td>10.44</td></tr><tr><td>NW 4 (part of NW 1)</td><td>6492</td><td>16,240</td><td>Real-world</td><td>Excluded (1115)</td><td>0.3265</td><td>10.794</td></tr><tr><td>NW 5 (power law: 2.1)</td><td>5000</td><td>14,192</td><td>Simulated</td><td>-</td><td>0.0018</td><td>8.06</td></tr><tr><td>NW 6 (power law: 2.5)</td><td>5000</td><td>12,987</td><td>Simulated</td><td>-</td><td>0.0010</td><td>8.6</td></tr><tr><td>NW 7 (power law: 2.8)</td><td>5000</td><td>12,375</td><td>Simulated</td><td>-</td><td>0.0008</td><td>8.9</td></tr><tr><td>NW 8 (ER, max. out dgr. 5)</td><td>5000</td><td>14,861</td><td>Simulated</td><td>-</td><td>0.0014</td><td>7.78</td></tr><tr><td>NW 9 (ER, max. out dgr. 10)</td><td>5000</td><td>27,814</td><td>Simulated</td><td>-</td><td>0.0025</td><td>5.32</td></tr><tr><td>Movie actors*</td><td>225,226</td><td>-</td><td>-</td><td>-</td><td>0.79</td><td>3.65</td></tr><tr><td>WWW**</td><td>153,127</td><td>-</td><td>-</td><td>-</td><td>0.108</td><td>3.1</td></tr><tr><td>Math co-authorship***</td><td>70,975</td><td>-</td><td>-</td><td>-</td><td>0.59</td><td>9.5</td></tr></table>

⁎ [58], ⁎⁎ [1], ⁎⁎⁎ [9].

![](/api/attachments/5889BVGK/fulltext/images/b3db31db5707500e7a029dc530e7f1566ed55d52e3dab9f645c879b2ca38a82c.jpg)

Fig. 2. In-degree distribution of our data sample.  
![](/api/attachments/5889BVGK/fulltext/images/ef3e0e7cb2a9b62db92645367feb8093b1767e72d6e9ffce00c985433fb47d21.jpg)  
Fig. 3. Out-degree distribution of our data sample.

As the power law coef<sup>fi</sup>cient decreases a larger number of customers has a very high number of degrees.

The power–law coef<sup>fi</sup>cients of the WWW, which were analyzed by different authors [4,44,20] were between 2.4 and 2.7 for the out-degree distribution and 2.1 for the in-degree distribution. The network of movie actors follows a power law distribution with α=2.3 for in- and out-degree [8].

## 3.1.2. Diffusion Models

In our computational experiments, we have combined different levels of the decay constant (τ), the threshold for believing a message (ε), the probability for transmission (κ), and the lifetime of a message (ω) as treatments (see Table 2) to explore the parameter space. We evaluated both kinds of diffusion models (exponential and power law) with different model parameters. For the power law diffusion we used decay factor τ of 1.75 as in Adamic and Adar [1]. In the exponential diffusion model we used a decay constant of 1 which indicates no diffusion, a decay of 0.5, 0.65, and 0.7. For the threshold value ε we used low values of 0.3 and 0.2. For the probability of transmission κ we evaluated values ranging from 23 to 100 percent. The lifetime ω of the message was set at 10 or 20. In each line of Table 2, we changed only one or two parameters, in order to analyze the impact of these changes.

## 3.1.3. Centrality measures

In addition to the centrality measures introduced in section 2.2.1, we implemented two more measures: the weighted PageRank and the weighted SenderRank. These measures take the weights of the edges into account. The formulas equal 12 and 13, with the difference that the PageRank and SenderRank are multiplied by the communication intensity, which is the sum of multimedia messages, short messages and voice calls received or sent respectively. The weighted PageRank $C _ { W P R } ( i )$ is de<sup>fi</sup>ned as:

Table 2 Treatment variables

<table><tr><td>Model</td><td>Type</td><td>τ</td><td>ε</td><td>κ</td><td>ω</td></tr><tr><td>1</td><td>Exponential</td><td>0.5</td><td>0.3</td><td>60</td><td>10</td></tr><tr><td>2</td><td>Exponential</td><td>1</td><td>0.3</td><td>60</td><td>10</td></tr><tr><td>3</td><td>Exponential</td><td>1</td><td>0.3</td><td>30</td><td>10</td></tr><tr><td>4</td><td>Exponential</td><td>0.5</td><td>0.3</td><td>100</td><td>10</td></tr><tr><td>5</td><td>Exponential</td><td>0.5</td><td>0.2</td><td>100</td><td>10</td></tr><tr><td>6</td><td>Exponential</td><td>0.7</td><td>0.3</td><td>40</td><td>10</td></tr><tr><td>7</td><td>Exponential</td><td>0.65</td><td>0.3</td><td>23</td><td>10</td></tr><tr><td>8</td><td>Power law</td><td>1.75</td><td>0.3</td><td>40</td><td>10</td></tr><tr><td>9</td><td>Power law</td><td>1.75</td><td>0.3</td><td>60</td><td>10</td></tr><tr><td>10</td><td>Power law</td><td>1.75</td><td>0.3</td><td>100</td><td>10</td></tr><tr><td>11</td><td>Power law</td><td>1.75</td><td>0.3</td><td>40</td><td>20</td></tr></table>

$$
C _ {W P R} (i) = (1 - d) + d \sum_ {j \in M _ {i}} \frac {C _ {P R} (j) \left(a _ {i j} + a _ {j i}\right)}{\sum_ {i = 1} ^ {n} a _ {j i}}\tag{18}
$$

The weighted SenderRank $C _ { W S R } ( i )$ is de<sup>fi</sup>ned as:

$$
C _ {W S R} (i) = (1 - d) + d \sum_ {j \in L _ {i}} C _ {S R} (j) \left(a _ {i j} + a _ {j i}\right)\tag{19}
$$

## 3.2. Results

We have combined all treatments resulting in 1,089 (9 networks ⁎ 11 models ⁎ 11 centrality measures) different results. Gain curves, aka lift charts [60], are regularly used to evaluate direct marketing campaigns and describe the percentage of target customers reached based on the percentage of the customers that were addressed in a campaign. In our gain charts we will use absolute numbers and plot the number of customers reached on average after 10 iterations against the number of customers that were initially addressed, i.e. the ones selected based on centrality.

In order to avoid bias in the evaluation of the random selection, we applied the message-spreading 10 times on each network and calculated averages. We selected the most important results and will present them in two steps. First we will evaluate different networks, while keeping the other treatments constant. Then the effect of different diffusion models will be analyzed, keeping the network constant.

## 3.2.1. Evaluation of different networks

3.2.1.1. Real phone networks. Within real networks the performance of the centrality measures was similarly independent of the network. As an example, Fig. 4 illustrates the evaluation of NW2 with the following parameters: $\tau = 0 . 5$ $\varepsilon { = } 0 . 3 , \kappa { = } 6 0 \% , \omega { = } 1 0 \mathrm { . }$ The histogram visualizes the results of a random selection and selections based on the 11 different centrality measures when for example 30 and 90 customers are initially addressed. This type of histogram allows us to display the performance of all metrics in one chart. In addition, Fig. 5 presents the gain curves of a number of selected centrality measures. Each point on a gain curve illustrates the average of 10 simulation rounds. The probability of transmission κ leads to some randomness and is responsible for the fact that the number of customers reached can also stay constant or even decrease in some cases although more customers have been selected initially.

The Figs. 4 and 5 illustrate that centrality based selection leads to a signi<sup>fi</sup>cant gain in reaching people compared to a random selection of customers, no matter which centrality measure is considered. The best centrality measures were out-degree centrality and SenderRank, which performed equally well across all quantiles. The weighted SenderRank and betweeness centrality were second best followed by the edge-weighted centrality and closeness centrality. The worst centrality measure for information diffusion of this sort were in-degree, authorities, and PageRank, which all stress the indegree. Very similar results could be established for NW1, NW3 and NW4.

3.2.1.2. Simulated scale-free networks. The power–law simulated scale-free networks (NW 5–7) provided results similar to the ones of the real phone networks NW 1–4 (see Figs. 6 and 7). The best measures were SenderRank, out-degree and also weighted SenderRank. Edge-weighted degree centrality was followed by closeness. A difference to real world networks in these networks was that closeness centrality performed better than betweenness centrality. This might be due to the fact that real networks contain more clusters than simulated ones. Betweenness centrality better identi<sup>fi</sup>es bridge-nodes connecting different clusters of a network.

3.2.1.3. Simulated ER-networks. ER-networks were mainly used for comparison, since most real-world networks are scale-free. In ER-networks without clusters (NW 7 and 8) the best measure was again the SenderRank followed by closeness and out-degree centrality (see Figs. 8 and 9). However, in case of ER-networks there was less difference between the different centrality measures.

We have also looked at the correlation of the different centrality scores. While the correlation was typcially low between 0 and 0.5 for the different networks. The notable exception was the correlation between SenderRank and outdegree centrality, which was sometimes even close to 1. Also in-degree, authorities and PageRank were highly correlated (0.8–0.9). In other words, out-degree centrality turns out to implement the SenderRank in many scale-free networks with considerably lower computational complexity.

## 3.2.2. Evaluation of diffusion models

In the previous section we could already see that SenderRank and out-degree centrality performed very well. Much of this might be due to the assumptions of the diffusion model (signal strength τ, probability of message transmission $\kappa ,$ threshold ε, power law and exponential diffusion). Our diffusion model described in Section 2.3 is very generic, and allows a variety of parameter settings modeling very different real-world diffusion processes. We analyzed different diffusion models based on network NW 2, in order to provide a sensitivity analysis of this <sup>fi</sup>nding with respect to different assumptions about the message diffusion. We have analyzed the parameter settings also on the other networks but since the results were similar we present these results as an example. We have evaluated all the parameter settings in Table 2. Due to space restrictions we will illustrate addtional treatments in the Appendix. Interestingly, out-degree and SenderRank were the top-ranked centrality measures in almost all treatments.

## 3.2.3. Evaluation of cluster centralities

We have already seen, that based on the above network topology and diffusion models, the local vicinity of a node does play a role. So instead of calculating the global centrality for the entire network, an alternative might be to <sup>fi</sup>rst derive clusters of highly connected nodes (e.g., groups of friends) and then <sup>fi</sup>nd the most central customer among them.

The following analysis is based on NW 1 with diffusion model parameter $\tau = 0 . 5 , \varepsilon = 0 . 3 , \kappa = 6 0 \% , \omega = 1 0$ . Different cluster centrality measures were evaluated. The best performing measures of the previous evaluations were chosen for cluster centralities, namely out-degree, degree (which is the sum of in-

![](/api/attachments/5889BVGK/fulltext/images/2c06aef0fd5b68be1cfb39fec76f618cdeb769d9bed40dfb17da6a9ab3951add.jpg)  
Fig. 4. Evaluation of centrality measures of real world network NW2, histogram.

degree and out-degree), SenderRank, betweenness and closeness centrality. The Minimum Spanning Tree clustering algorithm (see [56,51,43]) was used, because it has low computational complexity and is therefore applicable to large networks. We got 752 clusters, most of them having less than 30 nodes, but also a few big clusters of several hundred nodes. Only clusters with at least 5 nodes were taken into account, which has shown to improve the performance of the approach.

There are several ways, how one can rank-order these central cluster nodes. One way is to sort the clusters based on their size. During the selection, we iterated through all clusters, which exhibit the minimum size, and selected the

![](/api/attachments/5889BVGK/fulltext/images/68dfd1209acf1361b2104274d77a45b44b93a826e6cadca9812f79bf0fd4ad3f.jpg)  
Fig. 5. Evaluation of centrality measures of real world network NW2, gain-chart.

![](/api/attachments/5889BVGK/fulltext/images/7bb5f3cab5e34f17920577db4adca1a6c8cef5ac86587e7e20b08e1e10bad939.jpg)  
Fig. 6. Scale-free network NW6, histogram.

most central node in the largest cluster followed by the most central node in the second largest cluster, until the most central nodes of all clusters were selected. In the next iteration we selected the second node ranked by centrality, etc. When one third of the nodes in a cluster was selected the cluster was not considered any more.

The results of the cluster centrality based selection compared to a network centrality based selection of NW1

![](/api/attachments/5889BVGK/fulltext/images/c4766d54b94b22038e9bf9813fb8d9c6d797906a434dd812bd430d75a58e171d.jpg)  
Fig. 7. Scale-free network NW6, gain chart.

![](/api/attachments/5889BVGK/fulltext/images/9816acac10e61d2a67b941aa3a23d89b0788aac989766f04a1ce543be5d0c562.jpg)  
Fig. 8. ER network NW8, histogram.

are illustrated in Fig. 10. Cluster centralities are marked with the pre<sup>fi</sup>x “Clustered”. The cluster centrality measures which performed best are also out-degree, degree and SenderRank. However, clustering centralities performed worse than their equivalents calculated on the entire network. One reason might be the network topology. Sending a message to a node which has the highest outdegree of a cluster might ignore the fact that nodes with much higher out-degree centrality exist in another cluster, but were ignored in the iterative selection process described above. Overall, the nearest vicinity of a node turns out to be most important for various diffusion models. So, even modi<sup>fi</sup>ed strategies for the selection of initial nodes have little impact on the result. Additional analyses of different networks with different parameter settings con<sup>fi</sup>rmed these <sup>fi</sup>ndings.

![](/api/attachments/5889BVGK/fulltext/images/bc639493e11d604a004b4b5fde6a84ed38d87b43090db03bced9206cca57178c.jpg)  
Fig. 9. ER network NW8, gain chart.

![](/api/attachments/5889BVGK/fulltext/images/5339c2c4662162bcb98237949c2700a98719c1dd7feacca78bd5a265ad272c90.jpg)  
Fig. 10. Evaluation of cluster centralities in NW1.

## 3.2.4. Diffusion processes over time

In particular, for campaigns that need to reach many people in very short time, it can be of interest to analyze how many customers can be reached after only a few transmissions. If we assume each transmission is one step in time, we can analyze, which is the fastest way to reach customers. In Fig. 11 we assumed a transmission probability κ=100% and no decay (τ). For the illustration of these effects, we generated a small power law distributed network (with a power law coef<sup>fi</sup>cient α=2.1) with 300 nodes and 458 edges only, where the performance differences on the <sup>fi</sup>rst few transmissions are easier to identify.

Fig. 11 shows that in steps 2–5, the complex SenderRank performed best, and was slightly better than the simple outdegree measure. In step 4 betweenness and closeness outperform out-degree and in step 6 they also outperform SenderRank. This might be due to the fact that these centralities take into account all the nodes in a network and not only the close vicinity. In step 7, out-degree outperforms SenderRank and closeness centrality. After 15 steps the centrality measures converged since all nodes were reached. Since betweenness and closeness centrality had exactly the same values we described only one of them in the chart.

![](/api/attachments/5889BVGK/fulltext/images/506fbed3f10399c890f571bd2265dd8daf8d3d3aad6b287282ce50e262bc0889.jpg)  
Fig. 11. Time-dependent analysis of centrality measures.

These experiments provide also information on how well the different centrality measures are doing, if you expect them to spread very far, i.e., the message is passed on many times from neighbor to neighbor, as might be the case for important information (such as hurricane warnings), or if you are talking about short-lived marketing messages about a new product, that might only be passed on a few times to friends that are interested in a particular product.

## 3.2.5. Summary

Overall, centrality measures achieved a very high lift of up to 20 compared to a random selection in our message spreading experiments. The lift can be calculated as the number of customers reached divided by the number of customers selected. In most cases SenderRank performed best, but is closely followed by or even equal to the simple out-degree centrality, which has a constant computational complexity. In scale-free networks the scores of both measures were highly correlated. Along the same lines, Fortunato et al. [27] showed recently for an analysis of Web search algorithms that the approximation of PageRank via the in-degree can be highly accurate.

This result is robust against different types of network topologies and different assumptions about message distribution. Only for treatments with a very high signal strength (see the sensitivity analysis for τ in the Appendix) those metrics which emphasize not only the nearest vicinity perform much better. We did not <sup>fi</sup>nd a different ranking of the centrality measures for the different samples of our real network, and also found a roughly similar ranking for simulated scale-free networks. Within a certain type of network (real, power–law simulated and ER simulated) the rankings of the metrics are highly correlated. Between different types of networks the correlation was lower, but still SenderRank and out-degree came out best most of the time. Also, the size of the network n did not lead to differences in the rankings.

The results provide marketing decision makers with a clear recommendation of what measure best describes the structural capability of a customer to spread a message. It is worthwile to emphasize, however, that this advice is suitable for viral marketing campaigns increasing the awareness of a product, as outlined in Section 1. In cases where we can assume that all consumers are aware of the product's existence, and seeding merely affects their expected value from adopting it, Sundararajan [54] has recently shown that under certain assumptions it might be a better strategy to seed the fringes rather than the hubs of a network.

## 4. Conclusions

Data mining, in particular classi<sup>fi</sup>cation, has become an integral part of decision support in CRM in areas such as campaign management or churn prediction. Respective CRM applications typically ignore the position of a person in the customer network. Many companies do not only have data about individual customer behavior, but also about the social network of customers. Although information about the content of a communication is typically not available, the frequency of interactions and the resulting topological information about the customer network can be leveraged in viral marketing campaigns, for purposes of usage stimulation, or churn management (see Section 1.2).

Recent research has found that centrality measures need to be matched to the network <sup>fl</sup>ow for which they are appropriate. This topic has found little attention in the viral marketing literature, which exhibits diffusion patterns that are different to the ones in disease spreading or other domains. While much of the communication among customers cannot be observed, call detail records provide a sample of communication relationships that can be used to derive an estimator for the in<sup>fl</sup>uence of a customer. Centrality can be used as such an estimator.

In this paper, we have compared different centrality measures with respect to their impact on message diffusion in social networks. We have evaluated existing measures and also introduced the SenderRank as a new one focused on message distribution in social networks. Based on a number of computational experiments on arti<sup>fi</sup>cial and on real networks we observed a signi<sup>fi</sup>cant lift when using central customers in message diffusion, but also observed differences in the various centrality measures depending on the underlying network topology and diffusion process. We also found that the simple out-degree centrality achieves very good results compared to computationally more complex centrality measures. Only the SenderRank achieved a comparable performance.

There are a number of caveats, one might want to keep in mind. As indicated, call detail records can be used to derive an estimator for the social interaction pattern of a customer. However, this data re<sup>fl</sup>ects only parts of the social interaction of a customer and might be biased. Also, in this study, we ignore customer preferences for speci<sup>fi</sup>c messages. The centrality of a customer describes only his basic capability to distribute a message in a network. It does say nothing about the tastes or preferences of this customer. It is, therefore, important to complement these metrics with the results of other predictive models, such as logit models or decision trees as they are regularly used nowadays in campaign management to predict the af<sup>fi</sup>nity of a customer for a certain product or brand. The centrality of a customer in his network is orthogonal information. It might be used to select target customers in combination with the likelihood of a customer of responding to a message, or one might also include only those customers in the network analysis that have a certain likelihood of being interested in a message.

While knowledge about the merits of different centrality measures can be helpful, when important messages should be distributed in a network, data privacy is a crucial aspect in all campaign management applications. The concerns that people have over the collection of personal data naturally extends to any analytic capabilities applied to the data. Respective applications are typically regulated by privacy laws and company guidelines. Misuse of campaigns can always have many adverse effects such as customer churn that marketers need to consider. On the other hand, intelligent use of analytical techniques can help companies with large numbers of customers to <sup>fi</sup>nd and address the right customers with information that is of interest to them.

![](/api/attachments/5889BVGK/fulltext/images/88331448964e118c8cfad7531d519388c19474aaae1ae5c96a621dad4b0d52e5.jpg)  
Fig. 12. Model 1, τ=0.5, histogram.

![](/api/attachments/5889BVGK/fulltext/images/6e85dfc279fd618c87ed795dcd033fe9e03af868cecd814e8e7cbceb7cce9bde.jpg)  
Fig. 13. Model 1, τ=0.5, gain-chart.

## Appendix A. Evaluation of centrality measures for different diffusion models

In the following, we provide more detailed results with respect to the different treatment variables in our diffusion models in Section 3.2.2.

Decay of signal strength τ.

First we show in Figs. 12–15 how changes in the decay factor τ impact the outcome by describing Model 1 and Model 2 of Table 2, i.e., if the decay parameter τ=0.5 changes to τ=1.

The difference between the two decay factors is that a high number of persons are reached very fast when the decay factor

![](/api/attachments/5889BVGK/fulltext/images/a568bf1f3b8dba0715fc6b4fe1f16eb836e26d08c2768e3a53ca1a5fa20503f7.jpg)  
Fig. 14. Model 2, τ=1, histogram

![](/api/attachments/5889BVGK/fulltext/images/b8e0007a96a67aa2830c77302f3c5591c10ec4062227df5b84c19260d12c4ab6.jpg)  
Fig. 15. Model 2, τ=1, gain-chart.

τ =1, i.e., the strength of the signal or message does not get weaker. In this case, there is little difference between the topranked centrality measures. If we assume a message to get weaker, however, the close vicinity of a node is of higher importance and SenderRank and out degree centrality outperform all other measures. The randomness in κ and the structure of the network lead to non-monotonous gain curves in Fig. 15. We have observed the same pattern for the other networks.

Probability of message transmission κ

Figs. 16–19 presents the differences of Model 9 and Model 10 of Table 2, with the transmission probability changing from κ=60% to κ=100%.

![](/api/attachments/5889BVGK/fulltext/images/263b3087cc16c2b7546b34457279e840005097ee5037fd5f4ac107da8ddf4333.jpg)  
Fig. 16. Model 9, κ= 60%, histogram.

![](/api/attachments/5889BVGK/fulltext/images/b4c1957a97d5070e16f8114e8fb013c0258b12dade8b46bfe02acf1dbad64324.jpg)  
Fig. 17. Model 9, κ=60%, gain-chart.

![](/api/attachments/5889BVGK/fulltext/images/dab2a91759e43af5b089b5a46cf7bdf6af1aef38c671f8b060e33661df7f99f1.jpg)  
Fig. 18. Model 10, κ= 100%, histogram.

![](/api/attachments/5889BVGK/fulltext/images/d466ce5d4eed0ca6c176cc4944e885064a5a30cc6dd9e22bae787be68a7ace59.jpg)  
Fig. 19. Model 10, κ=100%, gain chart.

Except for closeness centrality and the hubs score, we get the same ranking, although, as expected, with a higher κ also many more customers could be reached. Again, SenderRank and out degree were best if a certain minimum number of initial customers was addressed.

Threshold ε

The threshold ε describes the signal strength at which we consider a message received. In the previous experiments it was set to 0.3. Figs. 20–23 show how the ranking of centrality measures when ε changed from 0.3 to 0.2, as in Model 4 and 5.

![](/api/attachments/5889BVGK/fulltext/images/fe624f360a6a3415b74c6206905475d8e9736b673bb4e3db32ea3fddd2034a02.jpg)  
Fig. 20. Model 4, ε=0.3, histogram.

![](/api/attachments/5889BVGK/fulltext/images/9931c636b3a05fa3b545dcf5f9350c35cfbfcbd8dedd66ba58a7b5060f969f1f.jpg)  
Fig. 21. Model 4, ε=0.3, gain-chart.

A noticeable difference is that the betweenness centrality did best when the threshold was only 0.2. We could, however, not observe this in the simulated networks or with other treatments, were always SenderRank and out-degree centrality performed best. Overall, betweenness centrality did well when the threshold ∊ and the probability for transmission κ were set such that the message spreads widely. Different values of ω did not exhibit a signi<sup>fi</sup>cant impact on the ranking of the centralities.

We could also <sup>fi</sup>nd no signi<sup>fi</sup>cant differences in the ranking of centrality measures using different diffusion models. This can be seen, for example, in Fig. 17 for a power law decay $( \tau = 1 . 7 5 , \ \varepsilon = 0 . 3 , \ K = 6 0 \% , \ \omega = 1 0 ) ,$ , and in Fig. 13 with an exponential decay $( \tau { = } 0 . 5 , \varepsilon { = } 0 . 3 , \kappa { = } 6 0 \% , \omega { = } 1 0 )$

![](/api/attachments/5889BVGK/fulltext/images/396697440106760748e5e097c8b501c597fcf7226c704b6cfaabe6c01eebdfd7.jpg)  
Fig. 22. Model 5, ε = 0.2, histogram

![](/api/attachments/5889BVGK/fulltext/images/ba14b62f5143624fb5288f2d9c6f04cac86c4c32ee6f4e6f7af2b22fadcce790.jpg)  
Fig. 23. Model 5, ε =0.2, gain-chart.

## References

[1] L.A. Adamic, E. Adar, Friends and neighbors on the web, Social Networks 25 (3) (2003) 211–230.

[2] W. Aiello, F. Chung, L. Lu, A random graph model for massive graphs, Proceedings of the 32nd Annual ACM Symposium on Theory of Computing, 2000.

[3] R. Albert, A. Barabasi, Statistical mechanics of complex networks, Reviews of Modern Physics 74

[4] R. Albert, H. Jeong, A. Barabási, Diameter of the world-wide web, Nature 401 (1999) 130–131

[5] E.W. Anderson, Customer satisfaction and word of mouth, Journal of Service Research 1 (1) (1998) 5–17

[6] C. Apte, B. Liu, E. Pednault, P. Smyth, Business applications of data mining, CACM 45.

[7] H.S. Bansal, P.A. Voyer, Word of mouth processes within a services purchase decision context, Journal of Service Research 3 (2) (2000) 166–177.

[8] A. Barabasi, R. Albert, Emergence of scaling in random networks, Science 286 no. 5439, 1999, pp. 509–512.

[9] A. Barabasi, H. Jeong, E. Ravasz, Z. Nda, A. Schubert, T. Vicsek, Deterministic scale-free networks, Physica A 311 (3–4) (2002) 590–614.

[10] F.M. Bass, A new product growth model for consumer durables. Management Science 18 (1969) 215–227.

[11] M. Beauchamp, An improved index of centrality, Behavioral Science 10 (1965) 161–163.

[12] M. Bichler, C. Kiss, A comparison of logistic regression, k-nearest neighbor, and decision tree induction for campaign management, Tenth Americas Conference on Information Systems (AMCIS), New York, 2004

[13] J.M. Bolland, Sorting out centrality: an analysis of the performance of four centrality models in real and simulated networks, Social Networks 10 (1988) 233–253.

[14] P. Bonacich, Power and centrality: a family of measures, American Journal of Sociaology 92 (1987) 1170–1182.

[15] P.F. Bone, Word of mouth effects on short-term and long-term product judgements, Journal of Business Research 32 (3) (1995) 213–223.

[16] S.P. Borgatti, Centrality and network <sup>fl</sup>ow, Social Networks 27 (2005) 55–71.

[17] D. Bowman, D. Narayandas, Managing customer-initiated contacts with manufacturers: The impact on share of category requirements and wordof-mouth behavior, Journal of Marketing Research 38 (2001) 291–297.

[18] U. Brandes, A faster algorithm for betweenness centrality, Journal of Mathematical Sociology 25 (2) (2001) 163–177.

[19] S. Brin, L. Page, The anatomy of a largescale hypertextual web search engine, 7th International Word Wide Web Conference, Brisbane Australia 1998

[20] A. Broder, R. Kumar, F. Maghoul, P. Raghavan, S. Rajalopagan, R. Stata, A. Tomkins, J. Wiener, Graph structures in the web, WWW9/Computer Networks 33 (16) (2000) 309–320.

[21] M. Castells, Informationalism, Networks, and the Network Society: A Theoretical Blueprint, The network society: a cross-cultural perspective, Northampton, 2004.

[22] R.M. Chrisley, G.L. Pinchbeck, R.G. Bowers, D. Clancy, N.P. French, R. Bennett, J. Turner, Infection in social networks: using network analysis to identify high-risk individuals, American journal of epidemiology 162 (10) (2005) 1024–1031.

[23] E. Costenbader, T.W. Valente, The stability of centrality measures when networks are sampled, Social Networks 25 (2003) 283–307.

[24] P.J. Danaher, R.T. Rust, Indirect <sup>fi</sup>nancial bene<sup>fi</sup>ts from service quality, Quality Management Journal 3 (2) (1996) 63–75.

[25] P. Erdoes, A. Renyi, On random graphs, Publicationes Mathematicae 6 (1959) 290–297.

[26] M. Faloutsos, P. Faloutsos, C. Faloutsos, On power–law relationships of the internet topology, ACM SIGCOMM, Comput. Commun. Rev. 29 (251).

[27] S. Fortunato, M. Buguna, A. Fammini, F. Menczer, How to make the top ten: Approximating pagerank from in-degree, in: WWW 2006, Edinburgh, UK, 2006.

[28] L.C. Freemann, A set of measures of centrality based on betweenness, Sociometry 40 (1977) 35–41

[29] L. C. Freemann, Centrality in social networks: I. conceptual clari<sup>fi</sup>cation, Social Networks 1 (215–239).

[30] L.C. Freemann, D. Roeder, R.R. Mulholland, Centrality in social networks: Ii. experimental results, Social Networks 2 (1980) 119–141.

[31] D. Godes, D. Mayzlin, Using online conversation to study word-ofmouth communication, Marketing Science 23 (4) (2004) 545–560.

[32] G.H. Golub, C.F. Van Loan, Matrix Computations, 3rd ed., Johns Hopkins University Press 1996

[33] S. Hakimi, Optimum locations of switching centers and the absolute centers and medians of a graph, Operations Reserach 12 (1965) 450–459.

[34] O. Hein, M. Schwind, W. Koenig, The impact of fat tailed degree distribution on diffusion and communication processes, Wirtschaftsinformatik 48 (4) (2006) 267–275.

[35] H. Jeong, B. Tombor, R. Albert, Z.N. Oltvai, A. Barabsi, The large-scale organization of metabolic networks, Nature 407 (2000) 651.

[36] J.J. Jonker, N. Piersma, R. Potharst, A decision support system for direct mailing decisions, Decision Support Systems 42 (2006) 915–925.

[37] P. Kannan, R. Rao, Introduction to the special issue: decision support issues in customer relationship management and interactive marketing for e-commerce, Decision Support Systems 32 (2001) 83–84.

[38] E. Keller, J. Berry, The In<sup>fl</sup>uentials, Free Press, 2003.

[39] W. Kermack, A. McKendrick, A contribution to the mathematical theory of epidemics, Proceedings of the Royal Society of London Series A 115 (1927) 700–721.

[40] J. Kirby, Connected Marketing, Butterworth-Heineman, 2005 an imprin of Elsevier.

[41] J. Kleinberg, Auth. sources in hyperlinked environment, CM-SIAM Symposium on Discrete Algorithms, 1998.

[42] D. Koschuetzki, F. Schreiber, Comparison of centralities for biological networks, German Conference Bioinformatics (GCB'04), 2004, vol. P-53.

[43] J.B. Kruskal, On the shortest spanning subtree and the traveling salesman problem, vol. 7, 1956.

[44] R. Kumar, P. Raghavan, S. Rajalopagan, A. Tomkins, Trawling the web for emerging cyber-communities, 8th International World Wide Web Conference, 1999.

[45] J. Leskovec, L. Adamic, B. Huberman, The dynamics of viral marketing, ACM Transactions on the Web 1.

[46] N. Lin, Foundations of Social Research, New York, 1976

[47] W. Mangold, F. Miller, G. Brockway, Word-of-mouth communication in service marketplace, Journal of Service Marketing 13 (1) (1999) 73–88.

[48] K.B. Murray, A test of services marketing theory: consumer information acquisition activites, Journal of Marketing 55 (1991) 10–25.

[49] M. E. J. Newman, Analysis of weighted networks, Physical Review E 70. [50] R. Pastor-Satorras, A. Vespignani, Epidemic spreading in scale-free networks, Physical Review Letters 86 (14) (2001) 3200–3203.

[51] R.C. Prim, Shortest connection networks and some generalisations, Bell System Technical Journal 36 (1957) 13891401.

[52] G. Sabidussi, The centrality index of a graph, Psychometrika 31 (1966) 581–603.

[53] M.J. Shaw, C. Subrmaniam, G.W. Tan, M.E. Welge, Knowledge management and data mining for marketing, Decision Support Systems 31 (2001) 127–137.

[54] A. Sundararajan, Network seeding, Workshop on Information System and Economics, Evanston, IL, USA, 2006.

[55] C. Van den Bulte, Y.V. Joshi, New product diffusion with in<sup>fl</sup>uentials and imitators, Marketing Science 26 (2007) 400–421.

[56] S. van Dongen, Graph clustering by <sup>fl</sup>ow simulation, Ph.D. thesis, University of Utrecht (2000)

[57] S. Wassermann, K. Faust, Social Network Analysis: Methods and Applications, Cambridge University Press, 1994

[58] D.J. Watts, S.H. Strogatz, Collective dynamics of ‘smallworld’ networks, Nature 393 (1998) 440–442.

[59] R.A. Westbrook, Product/consumption-based affective responses and post purchase processes, Journal of Marketing Research 24 (3) (1987) 258–270.

[60] I.H. Witten, E. Frank, Data Mining, Carl Hanser, Mnchen, Wien, 2001.

[61] F. Wu, B.A. Huberman, L.A. Adamic, J. Tyler, Information <sup>fl</sup>ow in social groups, Tech. rep., Physics Department, Stanford University HP Laboratories, 2003.

Christine Kiss studied Information Systems at the Technical University of Vienna, where she received her MSc degree in 2002. In 2001 she studied at the University of Middlesex in London. During her studies Christine was employed at several IT-companies as a software developer and as an ITconsultant. Christine's research interests are in the <sup>fi</sup>elds of data mining and data warehousing applied to business problems. Since February 2003 she is a PhD student at the Department of Informatics at the TU München

Martin Bichler is a full professor at the Department of Informatics at TU München. He received his MSc in Information Systems from the Technical University of Vienna and his Ph. D. as well as his Habilitation from the Vienna University of Economics and Business Administration. Martin was working as a research fellow at UC Berkeley and as a research staff member at the IBM T. J. Watson Research Center, Yorktown Heights, New York. Since 2003 he is a full professor at the TU München. Martin has been involved in research and development in the areas of electronic market design, analytical CRM, data mining, and service operations management.
