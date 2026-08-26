---
otero_id: 19966
otero_key: "NR87EWX5"
title: "Can you hold an advantageous network position? The role of neighborhood similarity in the sustainability of structural holes in social networks"
authors: "Charles Perez; I-Hsien Ting"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113783"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Can you hold an advantageous network position? The role of neighborhood similarity in the sustainability of structural holes in social networks

![](/api/attachments/NR87EWX5/fulltext/images/84e650833d458de2b9503b788a79829017415c700207089ec0b580e56f7806a6.jpg)

Charles Perez <sup>a,\*</sup>, I-Hsien Ting

<sup>a</sup> Paris School of Business, France

<sup>b</sup> Department of Information Management, National University of Kaohsiung, Taiwan

## A R T I C L E I N F O

Keywords: Structural social capital Structural holes Network science Inbound and outbound similarity

## A B S T R A C T

The literature has provided multiple metrics to measure the structural position of a node in a network or its structural social capital. However. the dynamics of social capital is rarely addressed, In this article, we analyze the sustainability of the structural position of the leaders. We explore the role of neighborhood similarity and propose inbound and outbound similarity measures to address the structural hole’s sustainability. To evaluate our approach, we use four real dynamic graphs and Susceptible, Infectious, or Recovered (SIR) model of epidemiology and regression analysis. We evaluate the power of our measures in predicting the evolution of the information spread of nodes, and compare the results with the measures from the literature. Our results confirm the relevance of neighborhood similarity for addressing the sustainability of social capital over time. In partic ular, the notions of inbound and outbound similarity proposed in this article show its relevance. The proposed framework allows better evaluation of one’s strategic position in a social network and measures the potential future impact.

## 1. Introduction

Social networks are complex networks that focus on people, their interconnections and interactions. The group of methodologies and techniques that help to analyze the mechanics observed in real life social networks is commonly known as Social Network Analysis (SNA) [1]. Multiple theories have emerged through the observation and analysis of real and artificial social networks, such as the theory of social capital.

Social capital theory suggests that a network would provide actual or potential resources to its members. This theory has proven its relevance applying to individual and group performances [2], strategic leadership, innovation [3], knowledge sharing [4] and decision-making [5]. [6] distinguishes between cognitive (shared understandings), relational (nature and quality of relationships) and structural (position in the network structure) forms of social capital

Multiple studies have related structural social capital to perfor mance: people who perform better are somehow better connected. Ac cording to [3], the advantage relies on non-redundant connections or connections to people belonging to different communities. Such con nections provide access to different sources of information and allow efficient information diffusion that favors innovation and performance [3,7]. Thus, “structural holes” separating contacts in the network and making them non-redundant (not connected directly or indirectly) assure the advantage.

The literature has provided multiple metrics to measure the struc tural position of a node in a network or its structural social capital: effective size, local clustering coefficient; efficiency, etc. However, we still have a limited understanding whether the observed topological position of a node is robust or subject to changes. If “no one is able to maintain a structural advantage in the long run” [8], whose strategic position would be the most sustainable in time?

In this article, we extend the theory of social capital and analyze the sustainability of the structural position of the leaders. Driven by the Burt’s definition of structural social capital and the notions of structural holes, we expand the definition to address the sustainability of structural social capital, and explore the role of the neighborhood similarity in predicting this sustainability.

We measure the inbound and outbound neighborhood similarity to capture the different levels of redundancy. According to link prediction approaches, the links are more likely to appear between similar nodes. As such, we suppose that the neighborhood similarity would be related to the evolution of the network and that structural advantages would be more or less sustainable depending on the similarity between the current neighbors of a node.

To evaluate our approach, we use four real dynamic graphs and Susceptible, Infectious, or Recovered (SIR) model of epidemiology and regression analysis. We evaluate the power of our measures in predicting the evolution of the information spread of nodes, and compare the re sults with the measures from the literature. Multiple configurations for graphs are tested. Our results confirm the relevance of neighborhood similarity for addressing the sustainability of social capital over time.

The implication of the findings opens the possible usage of inbound and outbound similarity as a complementary metric to the network constraints to obtain a finer-grained vision of social capital. Given similar network constraints for different nodes, in(out)bound similarity could distinguish the one which is most likely to maintain a strategic position. This complementary vision may reveal the key players in the early construction of the network, those who are able to maintain an advantageous position.

The reminder of the article is organized in the following way. Section 2 proposes the definitions and the mathematical clarification of the notations related to social networks. Section 3 provides a literature re view related to social capital and its measures, link prediction and node similarity measures, and the Susceptible, Infectious, or Recovered (SIR) model used in this study. Section 4 presents the methodology, theoret ical development and the set of metrics introduced in this study. Section 5 shows the results. We discuss theoretical and practical contributions of this work in the Section 6. The paper ends by highlighting the limitations and paths for future work.

## 2. Social networks and notations

A social graph denoted $G ( N , E )$ is a set of nodes (N) interconnected by edges (E). An edge may be directed and weighted depending on the type of graph and analysis. The egocentric graph $G _ { i }$ is a part of a graph rep resenting the direct neighborhood of a given node (node i) as shown in grey in Fig. 1.

The number of nodes - also called order - is denoted $N ,$ and the number of edges - also called size - is denoted E or L. The egocentric graph in Fig. 1 is composed of $N = 7$ nodes and $L = 1 0$ links. The set of nodes connected to a given actor i is denoted $\Gamma _ { i \cdot }$ . In the example, $\Gamma _ { i } = \{ A ,$ $B , C , D , E , F \}$ . The degree (DEG) of the node i, denoted in network science $k _ { i } ,$ which is also mentioned in sociometry as $n _ { i } ,$ is the number of elements that belong to this set. It corresponds to the number of nodes that are connected to i and also the order of the egocentric graph minus one. On the figure, the degree of i equals six: $k _ { i } = n _ { i } = \ | \Gamma _ { i } | \ = 6 .$

![](/api/attachments/NR87EWX5/fulltext/images/0d2f77be252ab4919df8f0ee5a715874bfd15e79359eac8ddb255a546f319cf4.jpg)  
Fig. 1. Egocentric graph of a node i denoted $G _ { i }$ (in grey) used in [7] extended to visualize neighbors of nodes F and E.

The number of edges that interconnect the neighbors of i is denoted t or $L _ { i }$ in the literature. In the aforementioned example, the links are highlighted in bold: $\{ ( A , B ) , ( A , E ) , ( A , F ) , ( B , D ) \}$ and $t _ { i } = L _ { i } = 4 .$ . The edges are undirected, therefore $( A , E )$ also counts for $( E , A ) .$ . We often represent a graph as a binary adjacency matrix where the $i ^ { t h }$ row and $j ^ { t h }$ column equal one if i and j are connected, and 0 otherwise. $m _ { i j }$ denotes the value of the adjacency matrix at row i and column j. The adjacency matrix of the graph $G _ { i } ,$ assuming that the nodes are numbered according to their alphabetical order, is denoted M.

All notations are summarized in Table 1.

## 3. Literature review

This state of the art section is organized in two parts. The first sub section is dedicated to the social capital, structural holes and their computation. The second part relates to the similarity measures (struc tural equivalence) existing between two nodes.

## 3.1. Structural social capital

Social capital theory views social connections as a form of human capital that can be leveraged. Structural social capital is a form of capital based on the position of the node in the network. Literature shows that positions of nodes in real graphs are not equal, and some seem to be more advantageous than others.

According to Burt [3,7], the structural advantage relies on “struc tural holes” separating members of the network and making them nonredundant or not connected directly or indirectly. A non-redundant neighborhood in the network provides a node with an access to different sources of information and more opportunities. Structural holes allow better information flow [9,10], better control over infor mation and were shown to be related to innovation and performance $[ 3 , 1 1 - 1 3 ]$ . Similarly, Granovetter [14] relates weak ties to new ideas, pointing out that people having strong ties are more likely to have overlapping contacts. Weak ties would potentially bridge different communities providing structural advantage and access to new information.

A complementary vision of social capital is presented by Coleman, who highlights the advantages of network closure to foster normative environment and trust [15]. Although, the two visions seem to diverge, [16] shows that both perspectives can be complementary: “Structural holes are the source of added value, but closure can be essential to realizing the value buried in the holes.” This observation has been confirmed, for example, for online communities where structural holes and closure were related to participants reputation scores [17].

Multiple approaches allow the structural social capital of a node to be measured. Those measures are generally considered as local or global. Local measures $( \mathbf { e . g . }$ efficiency [7] and local clustering coeffi cient [18]) are based on the neighborhood of each node. Global measures (e.g. betweenness centrality [19], PageRank [20]) are computed based on the whole graph’s structure.

Notations related to the modeling and analysis of social networks in network science and sociometry.

<table><tr><td>Notation</td><td>Meaning</td><td>Computation</td></tr><tr><td> $N$ </td><td>The number of nodes of the graph (a.k.a. Order)</td><td> $|N|$ </td></tr><tr><td> $L$ </td><td>The number of links of the graph (a.k.a. Size)</td><td> $|E|$ </td></tr><tr><td> $z_{i,j},w_{i,j}$ </td><td>The edge weight between  $i$  and  $j$ </td><td>-</td></tr><tr><td> $\Gamma_{i}$ </td><td>The set of neighbors of a node  $i$ </td><td>-</td></tr><tr><td> $\Gamma_{i} \cap \Gamma_{j}$ </td><td>The set of common neighbors between  $i$  and  $j$ </td><td>-</td></tr><tr><td> $n_{i}, k_{i}$ </td><td>The number of nodes in the egocentric network of a user, the degree of the node</td><td> $n_{i} = k_{i} = |\Gamma_{i}|$ </td></tr><tr><td> $t_{i}, L_{i}$ </td><td>The number of ties in the egocentric network of a user  $i$  excluding ties to  $i$ </td><td>-</td></tr><tr><td> $w_{ij},z_{ij}$ </td><td>The weight of the link from  $i$  to  $j$ </td><td>-</td></tr><tr><td> $m_{ij}$ </td><td>The value at row  $i$  and column  $j$  of the adjacency matrix</td><td>-</td></tr></table>

Betweenness centrality [19] is based on the number of shortest paths that pass through the node, and can help find nodes that bridge parts of the graph or are central to the graph. Burt suggests betweenness cen trality can be seen as a count of the structural holes to which a person has a monopoly access. The PageRank algorithm assumes that the importance of a node increases as it is pointed by many important nodes. PageRank was initially designed for ranking web pages [20] but may be also used for social networks. Other works, such as [21–25], measure the influence of a node based on the full graph, for example, by analyzing the impact of certain nodes on the information diffusion processes and community structure [26–28].

Newman [29] observed that global based centrality measures often exhibit high correlation with local measures (also outlined by [25]). However, global measures are much more computationally demanding. Also, real networks (like online social networks) do not always offer complete visibility of the full graphs for applying global measures. Therefore, in this article, we only focus on local or semi-local metrics summarized in Table 2.

Burt [7] provided multiple measures of social capital based on nonredundancy of contact: effective size (ES), efficiency and network constraint. The effective size (ES) of a node i varies from 1, when all contacts are redundant, to the degree of the node k when all nodes are non-redundant. The effective size formula has been greatly simplified by Borgatti [30]. The efficiency (EC) is computed as the effective size divided by the degree of the node.

Local and semi-local metrics measuring structural position of a node

<table><tr><td>Article</td><td>Name</td><td>Formula</td></tr><tr><td>Burt [7]</td><td>Effective Size (ES)</td><td> $ES_{i} = \sum_{j}(1 - \sum_{q} P_{iq} m_{jq})$ </td></tr><tr><td>Borgatti [30]</td><td>Effective size alternative (ES&#x27;)</td><td> $ES_{i} = n_{i} - \frac{2t_{i}}{n_{i}}$ </td></tr><tr><td>Burt [7]</td><td>Efficiency (EC)</td><td> $EC_{i} = \frac{ES_{i}}{n_{i}}$ </td></tr><tr><td>Burt [7]</td><td>Network constraint (CON)</td><td> $P_{ij} = w_{ij} / \sum_{q} w_{iq}$  $C_{ij} = \left( P_{ij} + \sum_{qe\Gamma_{i}\cap\Gamma_{j}} P_{iq} P_{qi} \right)^{2}$  $C_{i} = \sum_{j} C_{ij}$ </td></tr><tr><td>Barrat [31]</td><td>Average degree of neighborhood (AVD)</td><td> $k_{nn,i}^{w} = \frac{1}{s_{i}} \sum_{j \in \Gamma_{i}} w_{i,j} k_{j}$ </td></tr><tr><td>Newman [18]</td><td>Local clustering coefficient (LCC)</td><td> $LCC_{i} = \frac{2^{*} t_{i}}{k_{i}^{*}(k_{i} - 1)}$ </td></tr><tr><td>Latora [32]</td><td>Efficiency and Simmelian brokerage (SB)</td><td> $E_{i} = \frac{1}{k_{i}^{*}(k_{i} - 1)} \sum_{(l,m)e\Gamma_{i}^{2}} \frac{1}{d_{l,m}}$ </td></tr><tr><td>Su &amp; Song [33]</td><td>N-Burt (NB)</td><td> $\mathcal{B}_{i} = k_{i} - (k_{i} - 1)E_{i}$  $Q_{j} = \sum_{ve\Gamma_{j}} k_{v}$  $P_{ij} = Q_{j} / \sum_{ve\Gamma_{j}} Q_{v}$  $C_{ij} = \left( P_{ij} + \sum_{qe\Gamma_{i}\cap\Gamma_{j}} P_{iq} P_{qi} \right)^{2}$  $C_{i} = \sum_{j} C_{ij}$ </td></tr><tr><td>Ding &amp; Wang [34]</td><td>V-constraint (VC)</td><td> $s_{ij} = w_{1} p_{ij} + w_{2} p_{ij} R_{ij}$  $R_{ij} = \frac{k_{j} - |\Gamma_{i} \cap \Gamma_{j}|}{\sum_{ve\Gamma_{i}} k_{v} - |\Gamma_{i} \cap \Gamma_{j}|}$  $C_{ij} = \left( s_{ij} + \sum_{qe\Gamma_{i}\cap\Gamma_{j}} s_{iq} s_{qi} \right)^{2}$  $C_{i} = \sum_{j} C_{ij}$ </td></tr><tr><td>Zhao &amp; Guo [35]</td><td>Node influence (NI)</td><td> $F_{i} = a k_{i} + \frac{\beta}{C_{i}}, \alpha + \beta = 1$ </td></tr></table>

According to [32], efficiency is related to clustering, and both can be seen as the two sides of the same coin. The local clustering coefficient (LCC) reflects the local level of connectivity. It is computed as the number of connections between the neighbors of a node divided by the maximum number of connections that could exist [18].

The authors of [32] observe that small local efficiency would indi cate a brokerage opportunity: if a broker node disappears, many neighbors would become disconnected. The authors propose a Simme lian brokerage to measure that opportunity, based on the local efficiency of the node.

Brokerage opportunities can also be measured with Constraint (CON) [36]. The constraint measures the extent to which a manager’s time and energy is focused on a single group of colleagues who are inter connected. High constraint reveals possible redundancy in the infor mation accessed by the node. Many connections are common, and transmit to each other energy and time. When the local neighborhood of the node is less constrained, fewer connections exist between the neighbors, thus reducing the redundancy in the information flow. The constraint requires the initial measurement of the value $P _ { i j }$ which is computed as the weight of the interactions from i towards its neighbor j divided by the total weight of interactions coming from i. This value is then used to compute the constraint between the nodes i and j.

The authors of [33], [37] and [35] argued that the local vision, as shown in grey in Fig. 1, can be too restrictive to evaluate the social capital of a node. Indeed, if one observes the nodes E and F in an egocentric network in Fig. 1, one could conclude that these two nodes play an identical role. However, considering an extended scenario of Fig. 1, one may observe that node F opens access to a possible set of 3 nodes, while the node E would bring a single opportunity to M. Such semi-local observations are not captured by constraint.

N-Burt (NB) [33] is a simple semi-local adaptation of network constraint that helps to account for the impact of neighborhood of neighbors. The authors of [35] improve this measure and propose a new one called node influence (NI) based on constraint and degree of the nodes both weighted. The parameters are adapted to the network to pology to improve the identification of the most influential nodes ac cording to the information spread. V-constraint (VC) [34] is a different adaptation of constraint that considers the degree of nodes and the to pological structure of the neighbor nodes. Advantageous nodes have a high degree and their neighborhoods are not directly connected. The measure of sustainable social capital proposed in this paper, similarly, considers the semi-local vision of the node’s neighborhood.

We note that the aforementioned metrics allow structural social capital of a node in a given network to be measured. However, they do not address the evolution of this capital. Despite the fact that network dynamics were often studied [38], the authors rarely focused on the social capital sustainability.

[8] and [25] have analyzed the dynamics of social capital through game theory and strategic network formation. [8] has suggested that no one is able to maintain a structural advantage in the long run if everyone strives for structural holes. However, we suppose that some nodes could maintain their advantageous positions longer than others. [25] have used game theory in order to propose a new measure of centrality of nodes and denote that this centrality metric aligns with other centrality measures to a greater or lesser extent (e.g. clustering coefficient or constraint). The authors focus on strategic network formation where nodes would choose connections in order to optimize the personal utility obtained from the network. We argue that nodes do not always have the full vision of the network and the network would not always be a result of specific strategies of their members. In our work, we assume that social capital can be lost without the intention of the leader but by homophily: tendency of nodes to connect with similar others.

## 3.2. Susceptible-infected-recovered model

Susceptible-Infected-Recovered model is often used to evaluate the

Table 3

quality of structural social capital metrics [39]. This model considers the information diffusion process as similar to epidemic spreading. The nodes have three possible states: Susceptible, Infected, Recovered. At the beginning, some individuals are set as infected and others as susceptible. The Susceptibles have a probability B of becoming infected, as they are connected to an infected neighbor. Once infected, each individual has the possibility of being cured with a certain probability $\gamma .$ The epidemic spreads in the network until they are no more infected individuals in the network.

The model can be represented by the time evolution of the fraction of individuals in the S-I-R states. Given that the sum of the fractions of s,i,r states is 1, the model can be summarized with the following equations:

$$
\frac {d s}{d t} = - \mathcal {B} <   k > i [ 1 - r - i ]\tag{1}
$$

$$
\frac {d i}{d t} = \mathcal {B} <   k > i [ 1 - r - i ] - \gamma i\tag{2}
$$

$$
\frac {d r}{d t} = \gamma i\tag{3}
$$

When the probability of infection B is set to be slightly larger than the epidemic threshold, the individual impact of a node in the process is obtained. This threshold is obtained by computing B from the average degree and second order average degree of the graph as $\begin{array} { r } { \mathcal { B } _ { 0 } = \frac { < k > } { < k ^ { 2 } > } } \end{array}$ [40].

Under these conditions, the spreading efficiency F(t) of a node at time t is defined as the fraction of infected and recovered nodes by the total number of nodes n:

$$
F (t) = \frac {n _ {I (t)} + n _ {R (t)}}{n}\tag{4}
$$

When all infected individuals are converted to the recovered state, the spreading process stops and the final spreading score is equal to the maximum values of the recovered individuals. The larger the final spreading score triggered by the initial spreaders, the stronger their spreading abilities. A node with a high spreading capability is said to be more influential than others and have a large F(t).

## 3.3. Link prediction and nodes’ similarity

The link prediction refers to the identification of connections that are likely to appear in the future, based on a given snapshot of a social network. Most of the approaches rely on the measurement of similarity between pairs of nodes: the nodes with high similarity are assumed to be relevant for the prediction. This is theoretically supported by the homophily suggesting that people have the tendency to seek out or be attracted to those who are similar to themselves.

Two broad categories of similarity metrics of nodes can be defined: local and global indexes. A state of the art of the metrics can be found in [41] and [42]. Table 3 presents an overview of the state of the art ap proaches that will be adapted this work. Note that, we focus only on the local measures of similarity from a structural equivalence perspective. Also, the node attributes and edge weights are not considered but could be further investigated.

One of the most usual local similarity measures between a node x and a node y is the Common Neighbors (CN) index. This similarity equals the number of common neighbors between the pair of nodes. On a social network, this means that two profiles with many mutual friends are more likely to be friends than two profiles that do not share many common contacts.

The Jaccard (JA) index is a similarity metric that counts the number of common contacts [43]. However, this measure is normalized by the size of the union of the two sets of nodes neighbors.

The Preferential Attachment (PA) index assumes that the similarity between two nodes is proportional to the product of their degrees. Preferential attachment is observed in many real networks where new nodes tend to link to the most connected nodes. This phenomenon is also known as cumulative advantage or the rich get richer. Under this model, the famous profiles will be more likely to create connections than non famous profiles. For the same reason, new connections will likely involve famous profiles [44].

Local link prediction metrics.

<table><tr><td>Indices</td><td>Initial Formula</td></tr><tr><td>Common neighbors (CN)</td><td> $S_{x,y}^{CN} = |\Gamma_x \cap \Gamma_y|$ </td></tr><tr><td>Jaccard Index (JA)</td><td> $S_{x,y}^{JA} = \frac{|\Gamma(x) \cap \Gamma(y)|}{|\Gamma(x) \cup \Gamma(y)|}$ </td></tr><tr><td>Salton Index (SA)</td><td> $S_{x,y}^{SA} = \frac{|\Gamma_x \cap \Gamma_y|}{\sqrt{k_x^*k_y}}$ </td></tr><tr><td>Preferential Attachment Index (PA)</td><td> $S_{x,y}^{PA} = |\Gamma(x)|^* |\Gamma(y)|$ </td></tr><tr><td>Adamic Adar Index (AA)</td><td> $S_{x,y}^{AA} = \sum_{z \in \{\Gamma_x \cap \Gamma_y\}} \frac{1}{\log|\Gamma_z|}$ </td></tr><tr><td>Ressource Allocation Index (RAI)</td><td> $S_{x,y}^{RAI} = \sum_{z \in \{\Gamma_x \cap \Gamma_y\}} \frac{1}{|\Gamma_z|}$ </td></tr><tr><td>Hub Deprecated Index (HDI)</td><td> $S_{x,y}^{HDI} = \frac{|\Gamma_x \cap \Gamma_y|}{\min(k_x, k_y)}$ </td></tr><tr><td>Hub Promoted Index (HPI)</td><td> $S_{x,y}^{HPI} = \frac{|\Gamma_x \cap \Gamma_y|}{\max(k_x, k_y)}$ </td></tr><tr><td>Leicht Holme Newman (LHN)</td><td> $S_{x,y}^{LHN} = \frac{|\Gamma_x \cap \Gamma_y|}{k_x^*k_y}$ </td></tr></table>

The Adamic-Adar (AA) index is defined as the sum of the inverse logarithmic degree of the common neighbors of the two nodes [45]. This measure presumes that an individual with few collaborators selects his or her contacts more carefully than a person who connects with many individuals. Thus, a common friend that is a celebrity is considered to be less significant. On the other hand, a common friend that only owns a few contacts would be more important when measuring this similarity.

The Hub Promoted (HPI) and Hub Deprecated Indexes (HDI) aim to provide more or less importance to links that are adjacent to hubs [46] compared to the others. The common neighbors between the two analyzed nodes are divided by the minimum or the maximum degree of the two nodes.

The Resource Allocation (RAI) Index adds the inverse of the number of its contacts for each common neighbor z. This index, as indicated by its name, is closely related to the physical process of resource allocation [47]. The similarity evaluates the amount of information that can be sent from a node x to a node y via their common neighbors. Each common neighbor, is identified as a transmitter possessing a resource that it will distribute equally to all of its neighbors. The total amount of resources received by y from x corresponds to the similarity score.

The Leicht-Holme-Newman (LHN) index gives a high similarity score for two nodes possessing a large set of common neighbors with regard to the expected number of such neighbors in the configuration model [48]. The configuration model defined in [49] is a randomized realization of a particular network. This model proposes cutting each edge into two parts and bringing about a new random distribution of obtained stubs. In such model, the denominator $k _ { x } \mathrm { ~ } ^ { \ast } \mathrm { ~ } k _ { y }$ is equal the expected number of common neighbors.

## 4. Methodology

## 4.1. Theoretical development

Burt [3] states that nodes with high social capital have many disconnected acquaintances belonging to different groups. The social capital of an individual would increase with a higher quantity of con tacts and with their non-redundancy. Thus, social capital would decrease if connections become redundant.

Consider the egocentric network of i on Fig. 1. One can observe that the arrival of the relations $( A , D ) , ( C , D ) , ( B , C ) , ( D , F )$ and $( C , E )$ would generate greater redundancy of information in i’s egocentric network and, thus, would increase the constraint measure. The node i could lose its advantageous position if some connections appear.

Based on the observation above, we extend the definition of Burt to capture the dynamics of social capital and define a Sustainable Struc tural Hole<sup>1</sup> (definition 1).

Definition 1. Sustainable Structural Hole (SSH).

A node is said to be a sustainable structural hole if it respects the two following conditions:

## 1. It brokers connections between otherwise disconnected segments 2. Connections between its neighbors are unlikely

The likeliness of edge occurrence can be addressed by relying on the link prediction: the probability of a link appearing in the neighborhood of a node. Such a probability is related to the similarity of pairs of nodes in a given network: more similar nodes would tend to connect more easily than less similar nodes. Therefore, we assume that the similarity between neighbors of a sustainable structural hole would be small allowing the node to maintain its position.

In social networks, it is very common to observe that friends of friends are also often friends. However, one may observe nodes whose direct neighborhoods are not connected with each other (structural holes). The absence of such connections does not mean that such links would not appear in the near future. The link prediction methods are often used to identify the location of such missing links (future possible connection) are in a network.

Node similarity has shown its relevance for link prediction in a large variety of social networks [50]. Although the overall prediction ability of the similarity metrics could be relatively low (but much better than the random guesses), Newman [51] notices its usefulness to indicate where to look for the possible missing connections. Thus, the aggregated similarity score between all pairs of neighbors of a node addresses the probability that one or several links appear in a particular neighbor hood. We assume it would allow the prediction of which nodes are more likely to lose access to structural holes. In our particular case, it isn’t necessary to predict an appearance of each link, rather we need to know in which leading node’s neighborhood they are more or less likely to appear.

We note that some social networks where the link appearance fol lows particular normative rules (e.g. hierarchical networks) may pre vent some types of links to exist, despite topological similarity of nodes. Thus, similarity-based link prediction could be less relevant for such networks. However, social capital in the entrepreneurial-type of pro fessional social networks (flat, non-hierarchical) were shown to be particularly beneficial for opportunity oriented promotion [7]. Thus, similarity-based link prediction seems suitable for our context.

We also note that our approach may be less relevant for very dense (interconnected) networks as such networks already show the overall redundancy in connections and only few links are likely to be missing. However, in general, real social networks and particularly large net works exhibit very low density [52].

## 4.2. Inbound and outbound similarity

Fig. 2 shows a part of the neighbors of i focusing on two contacts x and y that are not directly connected. We can address the similarity between x and y using one of the approaches shown in Table 4, such as, for example, common neighbors. According to the common neighbor similarity, the likelihood that a link appears between the two nodes in the future is proportional to their number of common neighbors. In this case, they share 5 common neighbors that are $\{ A , B , C , D , E \}$ . Our approach aims to distinguish between the similarity that does not concern direct neighbors of i - mentioned as outbound - from the one that is part of the egocentric network of i - mentioned as inbound. When x and y share many common neighbors that are also neighbors of i, the local density increases and many closed triangles appear around i. Outbound similarity captures that two nodes are parts of the same larger com munity. On the other side, outbound similarity highlights the level of openness to resources of different groups further in the network.

![](/api/attachments/NR87EWX5/fulltext/images/5486548c0a1385c8d4fc944d16d5dabb52a43e0d39a7184e49284300bceff6e2.jpg)  
Fig. 2. Illustration of the inbound and outbound similarity between two neighbors x and y of a node i.

Inbound and outbound similarity metrics computed between two neighbors x and y of a given node i.

<table><tr><td>Indices</td><td>Outbound similarity</td><td>Inbound similarity</td></tr><tr><td>Common neighbors (CN)</td><td> $|\Gamma_x \cap \Gamma_y| - |\Gamma_x \cap \Gamma_y \cap \Gamma_i|$ </td><td> $|\Gamma_x \cap \Gamma_y \cap \Gamma_i|$ </td></tr><tr><td>Jaccard (JA)</td><td> $\frac{|\Gamma_x \cap \Gamma_y|}{|\Gamma_x \cup \Gamma_y| - (\lceil \Gamma_x \cap \Gamma_i \rceil + |\Gamma_y \cap \Gamma_i|)}$ </td><td> $\frac{|\Gamma_x \cap \Gamma_y \cap \Gamma_i|}{|\Gamma_x \cap \Gamma_i| + |\Gamma_y \cap \Gamma_i|}$ </td></tr><tr><td>Salton (SA)</td><td> $\frac{|\Gamma_x \cap \Gamma_y|}{\sqrt{(k_x - |\Gamma_x \cap \Gamma_i|)^*(k_y - |\Gamma_y \cap \Gamma_i|)}}$ </td><td> $\frac{|\Gamma_x \cap \Gamma_y \cap \Gamma_i|}{\sqrt{(|\Gamma_x \cap \Gamma_i|)^*(| \Gamma_y \cap \Gamma_i|)}}$ </td></tr><tr><td>Preferential Attachment (PA)</td><td> $(k_x - |\Gamma_x \cap \Gamma_i|)^*(k_y - |\Gamma_y \cap \Gamma_i|)$ </td><td> $|\Gamma_x \cap \Gamma_i|^{*} |\Gamma_y \cap \Gamma_i|$ </td></tr><tr><td>Adamic Adar (AA)</td><td> $\sum_{z\varepsilon\{\Gamma_x \cap \Gamma_y\} - \Gamma_i} \frac{1}{log(|\Gamma_z|)}$ </td><td> $\sum_{z\varepsilon \Gamma_x \cap \Gamma_y \cap \Gamma_i} \frac{1}{log(|\Gamma_z|)}$ </td></tr><tr><td>Ressource Allocation (RAI)</td><td> $\sum_{z\varepsilon\{\Gamma_x \cap \Gamma_y - \Gamma_i\}} \frac{1}{|\Gamma_z|}$ </td><td> $\sum_{z\varepsilon\{\Gamma_x \cap \Gamma_y \cap \Gamma_i\}} \frac{1}{|\Gamma_z|}$ </td></tr><tr><td>Hub Deprecated (HDI)</td><td> $\frac{|\Gamma_x \cap \Gamma_y| - |\Gamma_x \cap \Gamma_y \cap \Gamma_i|}{max(k_x, k_y) - |\Gamma_x \cap \Gamma_y \cap \Gamma_i|}$ </td><td> $\frac{|\Gamma_x \cap \Gamma_y \cap \Gamma_i|}{max(k_x, k_y) - |\Gamma_x \cap \Gamma_y \cap \Gamma_i|}$ </td></tr><tr><td>Hub Promoted (HPI)</td><td> $\frac{|\Gamma_x \cap \Gamma_y| - |\Gamma_x \cap \Gamma_y \cap \Gamma_i|}{min(k_x, k_y) - |\Gamma_x \cap \Gamma_y \cap \Gamma_i|}$ </td><td> $\frac{|\Gamma_x \cap \Gamma_y \cap \Gamma_i|}{min(k_x, k_y) - |\Gamma_x \cap \Gamma_y \cap \Gamma_i|}$ </td></tr><tr><td>Leicht Holme Newman (LHN)</td><td> $\frac{|\Gamma_x \cap \Gamma_y|}{(k_x - |\Gamma_x \cap \Gamma_i|)^*(k_y - |\Gamma_y \cap \Gamma_i|)}$ </td><td> $\frac{|\Gamma_x \cap \Gamma_y \cap \Gamma_i|}{(|\Gamma_x \cap \Gamma_i|)^*(| \Gamma_y \cap \Gamma_i|)}$ </td></tr></table>

The outbound similarity of x and y would be computed from the neighbors of x and y that are not connected to i. The inbound similarity would be computed from the common neighbors that are directly connected to i. In the aforementioned example, the outbound common neighbors similarity denoted CNO equals $3 \left( | \{ C , D , E \} | \right)$ and the inbound neighborhood similarity denoted CNI equals $\textbf { 2 } \ : \ : ( | \{ A , B \} | )$ . In the following, the similarity metrics will be referred to with an additional I or O to illustrate whether it is the inbound (I) or the outbound (O) version of the metric. For each similarity metric, we derive its inbound and outbound versions.

The local similarity between the neighbors of i denoted $S _ { i }$ in its In bound (I) or Outbound (O) version, is computed as stated in Eq. (5).

$$
S _ {i} ^ {I / O} = \frac {2}{k _ {i} * (k _ {i} - 1)} \sum_ {(x, y) \in \Gamma_ {i} ^ {2}} \frac {\text { Score } ^ {I / O} (x , y)}{d (x , y)}\tag{5}
$$

Where the $S c o r e ^ { I / O } ( x , y )$ refers to the inbound or outbound similarity between a couple of neighbors of the node $\therefore d ( x , y )$ refers to the distance between the two nodes x and y. Given the fact that x and y are neighbors of i their distance is 1 if they are directly connected and 2 otherwise. This formulation allows weighting the nodes that are directly connected with more importance from the others. The factor $\frac { 2 } { k _ { i } ^ { * } ( k _ { i } - 1 ) }$ allows the normalization of the score by the number of tested couples of neighbors.

Fig. 3 summarizes our proposition for social capital sustainability and the involved concepts visually.

## 4.3. Validation process

We test our proposal on four real dynamic graphs. Each social graph is observed at four different points in time calculated based on the ratio of edges to appear. We created four sets of sub-graphs where the ratio $^ { \cdot \rho }$ of unknown edges are set to 10%, 20%, 30% and 40% of edges from the final graph. The edges are filtered according to their arrival time.

For each temporal graph $G _ { i } ^ { \prime }$ and for each node, we simulate a propagation of information using the Susceptible-Infected-Recovered (SIR) model. To address the social capital change, we compute the variation of information spread score as the difference between the final ability of the node to spread information from the one observed on the past graphs, as stated in the Eq. (6).

$$
\forall i \in N; \forall t ^ {\prime} <   t;
$$

$$
\Delta F _ {i} = F (t) _ {i} - F \left(t ^ {\prime}\right) _ {i}\tag{6}
$$

F(t) is defined according to Eq. (4). If $\Delta F _ { i }$ is positive, then the node has gained spreading capabilities between time t<sup>′</sup> and t.

If $\Delta F _ { i }$ is negative, then the node has lost spreading capabilities be tween time t<sup>′</sup> and t. For each social network, we set up an infection probability β slightly above the epidemic threshold as recommended in the literature [24].

We compute all of the proposed neighborhood similarity measures. Additionally, we compute structural hole measures proposed in the literature review to compare the performances.

To focus on the leading nodes and their social capital changes, we applied different levels of node filtering in our analysis according to the constraint of each node. The parameter for the filter is denoted θ. The filter applies to the nodes with the lowest constraints scores at time t<sup>′</sup>.

![](/api/attachments/NR87EWX5/fulltext/images/ba65f8e207d31fb8102c2b2276ab5eb4f00b0c0aa77e883773756c90a21846ff.jpg)  
Fig. 3. Visual summary of the proposed approach and the concepts involved.

When setting $\theta \ : = \ : 1 0 \% ,$ only the top 10% nodes with the lowest constraint score at time t<sup>′</sup> are kept for the analysis - these are the nodes having the most preferable position according to [3]. We extend the values of θ from 10 to 80% in steps of 10%, to compare the performance of the methodology proposed on various levels of influential nodes in the social networks.

Finally, we evaluate the predictive power of the aforementioned metrics calculated from the past graph $G ^ { \prime }$ in predicting $\Delta F _ { i }$ using linear regression. We proceed for multiple variations of θ and $\rho$ for 4 different graphs, as described above, and compare the results with the literature review. We recognize that other measures could be indicative of the sustainability of the structural hole, but, as the similarity feature is particularly suitable for predicting upcoming links, the performance of our model is expected to be higher.

The regression results and the coefficients were tested with a sig nificance level of $p - \nu a l u e < . 0 0 1$ . The experiments involving a metric that did not reach the appropriate p − value of .001 were not considered in the results. The quality of the model is described using the adjusted Rsquared $( R ^ { 2 } )$ highlighting the proportion of variance in the dependent variable that can be predicted by the independent variable.

## 5. Results

The datasets used in this research are based on the exchange of professional emails within a large European research institution over 803 days [53]. The four real datasets represent the e-mail communica tion between the members of four different departments. No external communication is included into the dataset. An edge $( x , y , t )$ indicates that person x sent an e-mail to person y at time t. A separate edge is created for each recipient of the e-mail. Table 5 summarizes the char acteristics of the four datasets.

Fig. 4 illustrates the aggregated performances over all datasets and all conditions that were tested in this work. Measures from the literature are shown on the left in orange and the performance of our similaritybased metrics are shown on the right in blue. The best performance $( R ^ { 2 } = 0 . 1 6 7 )$ ) among the state of the art metric is obtained by N-Burt (NB) [33]. The other measures of structural social capital show much lower performances $( R ^ { 2 } < 0 . 1 )$ meaning that the measures do not capture the potential change in social capital well. Six of our similarity-based met rics outperform N-Burt: HDII (Hub deprecated index inbound), HPII (Hub promoted index inbound), SAO (Salton index outbound), CNO (Common neighbor outbound), CNI (Common neighbor inbound) and PAI (Preferential attachment index inbound), showing the interest of link prediction in measuring the sustainability of social capital.

Even if both the inbound and the outbound similarity measures perform well, inbound performs better. The inbound similarity seems more essential for a node to be able to maintain a structural hole posi tion. Thus, the evolution of the efficiency on information spread is more related to the direct neighborhood where a single link can reduce or accelerate information propagation. Outbound similarity can be viewed as complementary for more fine grained observation and prediction of the future position of the node.

The best performing similarity measures express the similarity be tween local neighbors based on their common neighbors number (CN), the relative degree of these common neighbors (PA) or both (HPI, HDI, SA). These results suggest that the direct common neighbors and their degree are essential when capturing the possibility of gaining or losing

Characteristics of the four datasets from [53] used for validation process.

<table><tr><td>Dataset</td><td>#Nodes</td><td>#Edges</td><td></td></tr><tr><td>email-Eu-core-Dept1</td><td>309</td><td>61,046</td><td>7.6</td></tr><tr><td>email-Eu-core-Dept2</td><td>162</td><td>46,772</td><td>6.64</td></tr><tr><td>email-Eu-core-Dept3</td><td>89</td><td>12,216</td><td>14.9</td></tr><tr><td>email-Eu-core-Dept4</td><td>142</td><td>48,141</td><td>5.4</td></tr></table>

![](/api/attachments/NR87EWX5/fulltext/images/2f23390160cca368fe06b6c16e80487ff68136a8906218f9190a7f321c469b98.jpg)  
Fig. 4. Comparison of the percentage of variance in the ΔF explained by the state of the art metrics and the inbound and outbound neighborhood similarity metrics.

social capital.

Regarding the Salton Index (SA), the outbound similarity performs better and gives more weight to the similarity when: (1) the degree of nodes is not very high and when (2) the number of common neighbors is small. This suggests that some nodes with very low constraint are more subject to social capital loss if their outbound neighbor similarity is high. It seems that, in this particular case, the inbound similarity is unlikely to generate links and outbound links are more likely to occur.

Fig. 5 compares the performances of inbound and outbound simi larities with the initial similarity measures from Table 4. The constraint performance is added for reference. For the majority of the metrics, inbound and outbound similarities show better performance which justifies having separate inbound and outbound similarity measures.

Figs. 6 and 8 show more detailed results for different parameters and datasets. Fig. 6 highlights the performances of measures according to different θ filters. The best performances are obtained when 10% of nodes with the lowest constraints (θ = 10%) are used and the perfor mance drops when more nodes are added. Such results show that the metrics predict the evolution of the neighborhood surrounded by structural holes better, rather than the evolution of the nodes having low social capital. That is in line with the goal of this article and our defi nition of sustainable structural holes.

It is interesting to observe that, whatever the θ value is, multiple inbound and outbound similarity metrics obtain higher scores than the N-Burt - the best measure from the state of the art. More precisely, the SAO, HDII and HPII systematically express an adjusted R-square above 0.2 for a threshold below 40% which is satisfactory for social sciences. Such results confirm that similarity metrics are useful for distinguishing if the leader is more or less likely to keep its position. The combinations of metrics could offer more significant scores, and could be tested in future work.

Fig. 7 shows the results over the four datasets for different ρ - amount of links to be added to the graph. We observe that the performances of most of the metrics increase as the number of unknown edges increases. Such results suppose that small variations of ΔF when only slight changes appeared in the network are not easily predictable. Greater evolution in the network makes the evolution of social capital more predictable.

Considering the case when 6 equals 10%, SAO and JAO explain about 10% of social capital change that is relatively low. However, when 30 to 40% of edges are removed in the network, HDII and HPII show satis factory prediction results with $R ^ { 2 } = 0 . 3$

Fig. 8 compares the metrics’ performances across the four datasets used for our analysis. We note that the performances are consistent with the other figures and are similar along the four datasets. Thus, we conclude that similarity measures can be helpful in predicting the

![](/api/attachments/NR87EWX5/fulltext/images/72462dac831605ded31a332559e70a34a46151da5fbb3a440815cdb949c16d72.jpg)  
Fig. 5. Inbound and outbound similarities compared to the initial measures.

![](/api/attachments/NR87EWX5/fulltext/images/a6919070bd918278b139d1f2291615073e3cf7c6f6c18037f2eafac8778dcaf9.jpg)  
Fig. 6. The summary of $R ^ { 2 }$ performances for different θ parameters. The dashed lines represent the metrics proposed in this study; the plain lines represent the metrics from the literature.

![](/api/attachments/NR87EWX5/fulltext/images/54f9e25ea2e06f7a538a6ca01074d2dfe310b6aa6cd2d542abc9fdf9a5567476.jpg)  
Fig. 7. Performance of the metrics over the four datasets and along different filtered time ρ from 10 to 40%.

sustainability of social capital and, as such, can be used to identify sustainable leaders, or sustainable structural holes, as defined in this paper.

## 6. Discussion

We contribute to the literature on structural social capital by extending the theory of social capital with the notion of sustainability. First, we extend the definition of social capital and propose a definition of sustainable structural hole. Our results confirm the relevance of neighborhood similarity for addressing the sustainability of social cap ital over time. In particular, the notions of inbound and outbound similarity proposed in this article show its relevance. The theoretical and practical implications are discussed in this section.

## 6.1. Complementarity of neighborhood similarity and network constraint

Our results suggest that the network constraint and local similarity metrics could be complementary when trying to understand the influ ence of a node in the network and the sustainability of its strategic po sition. Constraint provides a rich understanding of the position of the actors in the network and the related structural social capital. Analyzing their associated neighborhood similarity allows us to capture another strategic dimension. We aim to illustrate this complementarity in this

![](/api/attachments/NR87EWX5/fulltext/images/0d8ac2d1592648db2643851de6e5b0a5e7eb9e21f2cd5d74e082ee0409901f15.jpg)  
Fig. 8. Performance of metrics on the four different datasets used for analysis.

section.

As an example, we use a research collaboration network: a coauthorship network built among scientists working on network science [29]. It is composed of 1589 scientists and 2742 collaborations.

Fig. 9 plots all the researchers according to their constraint and normalized common neighborhood similarity. Multiple authors with the same constraint scores but different neighborhood similarity can be observed, suggesting that their position can be more or less robust over time.

For example, Claus C. Hilgetag and Jon Kleinberg are two re searchers having the same low constraint (C = 0.21) but different neighborhood similarity scores (0.5 and 0.38 respectively). Based on our results, the central position of Pr. Kleinberg is more sustainable in the network than the position of Pr. Hilgetag due to the smaller neighbor hood similarity.

By visually comparing the local neighborhood of both authors (Fig. 10 for Jon Kleinberg and Fig. 11 for Claus C. Hilgetag), one can observe that the topological differences are very pronounced. Pr. Jon

Kleinberg clearly appears in-between multiple, completely disconnected clusters with no common contacts. The likelihood that people from these clusters connect together is low which explains the small similarity measure. Pr. Kleinberg has access to structural holes that are unlikely to disappear. Pr. Hilgetag appears between communities that exhibit a higher level of similarity. Many of his direct contacts have at least a few common contacts in the community and the network seems more interconnected. The neighborhood similarity increases to 0.5. The notion of the sustainable structural hole proposed in this work can capture these observable differences and, thus, provide a finer-grained vision of social capital compared to the literature.

## 6.2. Complementarity of inbound and outbound similarities

Inbound and outbound similarities are also complementary and indicative of the actual presence of the structural holes in the network. Fig. 12 visually summarizes this complementarity with the quadrant (PSH indicates primary structural holes and SSH indicated secondary

![](/api/attachments/NR87EWX5/fulltext/images/1834fb649326b9866845abbac45965bf0a2e29188a70fbfaaecee959b491af96.jpg)  
Fig. 9. Network science authors plotted according to their neighborhood similarity and constraint scores.

![](/api/attachments/NR87EWX5/fulltext/images/1a1a6e9dc087d703af60b6eb48a11d115476501f86f068c6f40cb470ceafa91a.jpg)  
Fig. 10. Snapshot of the netscience graph containing the neighborhood of Jon Kleinberg.

![](/api/attachments/NR87EWX5/fulltext/images/b0b42a6a0c88a5201cf14bd870af667a5d96db3ea5827fdeea9267c19ffe8436.jpg)  
Fig. 11. Snapshot of the network science graph containing the neighborhood of Claus C. Hilgetag.

structural holes). The inbound similarity reflects the dynamics of the local neighborhood while the outbound similarity focuses on the semilocal neighborhood. High inbound similarity would be indicative for the absence of structural holes in the close neighborhood of the node (the bottom of the image). High inbound and outbound similarities are indicative of a cluster (the absence of structural holes) and low social capital according to Burt [3]. Such a configuration shows that the node is part of a strongly interconnected community that, according to Coleman [15] and its vision of social capital, fosters cohesion and trust in-between members. When the inbound similarity is high but the outbound similarity is low, the local neighborhood would be redundant but secondary structural hole or a shallow would exist in the indirect neighborhood.

When the outbound similarity is high but inbound similarity is low, structural holes should be observed in the local neighborhood of the node, while the indirect neighborhood would be more redundant. Thus, the local neighborhood, even if the nodes are not directly connected, would be part of the same community or would only provide access to a few different communities. Deep holes would be present if both inbound and outbound similarities are observed to be low. In this situation, structural holes would be sustainable, as the probability of links appearing between non-similar neighbors would be low.

Thus, inbound and outbound similarities would not only help to predict the sustainability of elevated social capital in the network but, more generally, are also indicative of the presence of structural holes in the nodes’ neighborhoods.

![](/api/attachments/NR87EWX5/fulltext/images/147e4eb8a9bd8c5b4002e45b3b9212a7cd043eaf039d643c272ae680f75aa139.jpg)  
Fig. 12. Structural holes quadrant.

## 6.2.1. Local clustering coefficient

We note that the clustering coefficient of a node can be seen as a very specific and trivial case of our inbound similarity metrics. The clustering coefficient of a node i measures the connectivity of its neighbors. It counts the number of existing connections in the neighborhood and normalize the score by the number of couples that exist in the direct neighborhood of a node. If we simplify the inbound similarity between two nodes to its most trivial definition, we can say that two nodes are similar if they are connected and non-similar otherwise. Under this condition, our formula will count the number of connected couples and normalize it as the formula of the local clustering coefficient.

For demonstration, we set the similarity Score(x, y) to the most trivial similarity metric: it equals one when the nodes are connected and zero otherwise. This is equivalent to $S c o r e ( x , y ) = m _ { x , \ y } .$ . Where $m _ { x , \ y }$ is the value of the adjacency matrix at position $x , y .$ Under this condition, we observe that: $\begin{array} { r } { S _ { i } = \frac { 2 } { k _ { i } * ( k _ { i } - 1 ) } { \sum } _ { ( x , y ) \in \Gamma _ { i } ^ { 2 } } \frac { m _ { x , y } } { d ( x , y ) } } \end{array}$

When $m _ { x , y } = 1$ , meaning that the nodes are directly connected, then their distance also equals one. Thus, $\begin{array} { r } { \frac { m _ { x , y } } { d ( x , y ) } = 1 } \end{array}$ . However, when they are not connected $m _ { x , \ y } = 0$ thus $\begin{array} { r } { \frac { m _ { x , y } } { d ( x , y ) } = 0 . } \end{array}$ , This means that $\textstyle \sum _ { ( x , y ) \in \Gamma _ { i } ^ { 2 } } { \frac { m _ { x , y } } { d ( x , y ) } }$ equals the number of ties in the egocentric network of i. This number is denoted t (as indicated in Table 1). Thus, we obtain $\begin{array} { r } { S _ { i } = \frac { 2 ^ { * } t _ { i } } { k _ { i } ^ { * } ( k _ { i } - 1 ) } } \end{array}$ which is the equation of LCC(i).

## 6.3. Practical implications

Social capital has shown its importance for the performances of groups and individuals. Burt [7] acknowledges that the social capital, once gained through access to structural holes, would be turned into link creation to obtain certain advantages or rewards. For example, a busi ness man could have a financial gain for putting two individuals in relation. However, the nodes do not have full control over the re lationships of their neighbors, and links could be made without any intention from the leader. In such case, the social capital slowly de creases such as the potential rewards. Our approach allows such po tential loss to be detected.

Recommendation systems on online social networks are frequently based on link prediction and topological similarities of nodes. People are frequently invited to connect to nodes from the community to which they belong to. Such recommendations tend to create cliques (closed triangles) of strongly interconnected communities penalizing the entrepreneurial networks and existence of structural holes. As such, leading nodes could burn their structural capital even faster online as their similar connections would tend to connect via recommendation systems.

We would encourage social actors not only to value their network based on their strategic position at any given time, but also sense the evolution of their neighborhood similarly to a chess game player. While many casual gamers play one step at a time (a.k.a one hop chess players), the grand masters take decisions by projecting their move into the future state of the board. The framework proposed in this paper allows a decider to evaluate his/her connections and develop a strategy for the long term thus optimizing a sustainable access to structural holes and social capital.

## 6.4. Limitations and future works

Our work extends the theory of social capital with the notion of sustainability and shows the relevance of neighborhood similarity in the evolution of structural social capital. However, we would like to acknowledge some limitations and paths for further studies in thi section.

The proposed model opens possibilities for future works on the application of structural social capital sustainability. The contribution could lead to a new set of tools for deciders to manage their collabora tion and business networks. Also, identification and characterization of sustainable structural holes could help to better understand better the evolution of performances and level of innovation at an individual and institutional scale.

The current study is based on unweighted graphs. However, all edges in a social graph do not necessarily have the same impact in the evo lution of structural social capital. Future works could consider this in their measures. Also, other than topological similarity measures, simi larity (attributes or hybrid approaches) could be considered while evaluating the similarity of a node’s neighborhood.

Finally, we analyze the dynamics of social capitals supposing the arrival of links. However, the arrival of new nodes and link disappear ance could be considered in further studies.

## CRediT authorship contribution statement

Charles Perez: Conceptualization, Methodology, Formal analysis, Validation. I-Hsien Ting: Investigation, Methodology, Supervision, Resources.

## References

[1] R. Alhajj, J. Rokne, Encyclopedia of Social Network Analysis and Mining, Springer Publishing Company, Incorporated, 2014.

[2] M.J. Ashworth, K.M. Carley, Who you know vs. what you know: the impact of social position and knowledge on team performance, J. Math. Sociol. 30 (1) (2006) 43–75.

[3] R.S. Burt, Structural holes and good ideas 1, Am. J. Sociol. 110 (2) (2004) 349–399.

[4] A. Styhre, The role of social capital in knowledge sharing: the case of a specialist rock construction company, Constr, Manag, Econ, 26 (9) (2008) 941–951.

[5] J.C. Shafer, S. Paparizos, R. Agrawal, A. Nandi, With a little help from my friends, in: Proceedings of the 2013 IEEE International Conference on Data Engineering (ICDE 2013), ser, ICDE ′13. JEEE Computer Society, Washington, DC. USA, 2013. pp. 1288–1291.

[6] J. Nahapiet and S. Ghoshal, “Social capital, intellectual capital, and the organizational advantage,” Acad. Manag. Rev., vol. 23, no. 2, pp. 242–266, April 1998.

[7] R.S. Burt, Structural Holes: The Social Structure of Competition, Harvard University Press, Cambridge, MA, 1992.

[8] V. Buskens, A. van de Rijt, Dynamics of networks if everyone strives for structural holes, Am. J. Sociol. 114 (2) (2008) 371–407.

[9] J. Yan, D.E. Leidner, H. Benbva, W. Zou, Social capital and knowledge contribution in online user communities: one-way or two-way relationship? Decis. Support. Syst.

[10] O. Nov, C. Ye, N. Kumar, A social capital perspective on meta-knowledge [10] O. Nov, C. Ye, N. Kumar, A social capital perspective on meta-knowledge

contribution and social computing, Decis, Support, Syst, 53 (1) (2012) 118–126.

[11] G. Ahuja, Collaboration networks, structural holes, and innovation: a longitudina

[12] Q. Zhang, D.D. Zeng, F. Wang, R. Breiger, J.A. Hendler, Brokers or bridges? Exploring structural holes in a crowdsourcing system, Computer 49 (6) (June 2016) 56–64.

[13] A. Zaheer, G.G. Bell, Benefiting from network position: firm capabilities, structural holes, and performance, Strateg. Manag. J. 9 (6) (Sep. 2005) 809–825.

[14] M.S. Granovetter, The strength of weak ties, Am. J. Sociol. 78 (6) (1973) 1360-1380.

[15] J.S. Coleman, Foundations of Social Theory, Harvard University Press, Cambridge,

[16], R.S. Burt. The network structure of social capital, in: Research in Organizational Behavior. 2000. Press.

[17] D. Ganley, C. Lampe, The ties that bind: Social network principles in online communities, Decis. Support. Syst. 47 (3) (2009) 266–274, online Communities and Social Network.

[18] M. Newman, The structure and function of complex networks, Soc. Indus. Appl. Math. Rey, 45 (2003) 167–256.

[19] L.C. Freeman. Centrality in social networks conceptual clarification, Soc. Networks

[20] L. Page, S. Brin, R. Motwani, T. Winograd, The pagerank citation ranking: Bringing order to the web, in: Proceedings of the 7th International World Wide Web Conference, Brisbane, Australia, 1998, pp. 161–172.

[21] Mining structural hole spanners through information diffusion in social networks, in: T. Lou, J. Tang, D. Schwabe WWW, V.A.F. Almeida, H. Glaser, R. Baeza-Yates, S. B. Moon (Eds.), International World Wide Web Conferences Steering Committee ACM, 2013, pp. 825–836.

[22] J. Zhu, Y. Liu, X. Yin, A new structure-hole-based algorithm for influence maximization in large online social networks, IEEE Access 5 (2017), pp. 23 405–23 412.

[23] L. Gallos, S. Havlin, M. Kitsak, F. Liljeros, H. Makse, L. Muchnik, H. Stanley, Identification of influential spreaders in complex networks, Nat. Phys. 6 (11) (Aug 2010) 888–893.

[24] M. Piraveenan, M. Prokopenko, L. Hossain, Percolation centrality: quantifying graph-theoretic impact of nodes during percolation in networks, PLoS One 8 (1) (2013), pp. 1–14, 01.

[25] F. Ghaffar, N. Hurley, Structural hole centrality: evaluating social capital through strategic network formation, Comp. Social Networks 7 (5) (2020).

[26] Z. Liao, L. Gu, X. Fan, Y. Zhang, C. Tang, Detecting the structural hole for social communities based on conductancedegree, Appl. Sci. 10 (2020), p. 4525, 06.

[27] Identifying top-k structural hole spanners in large-scale social networks, in: Rijke, R. Kumar, V. Murdock, T.K. Sellis, J.X. Yu (Eds.), CIKM, ACM, 2015, pp. 263–272.

[28] B. Krishnapuram, Joint community and structural hole spanner detection via harmonic modularity, in: L. He, C.-T. Lu, J. Ma, J. Cao, L. Shen, P.S. Yu, M. Shah, A. J. Smola, C.C. Aggarwal, D. Shen, R. Rastogi (Eds.), KDD, ACM, 2016, pp. 875–884.

[29] M.E.J. Newman, Finding community structure in networks using the eigenvectors of matrices, Phys. Rev. E 74 (3) (Sep 2006).

[30] S.P. Borgatti, Structural holes: unpacking Burt’s redundancy measures, Connections 20 (1) (1997) 35–38

[32] V. Latora, V. Nicosia. P. Panzarasa, Social cohesion, structural holes, and a tale of two measures. CoRR abs/1211.0719 (2012).

[33] Y. Su, X.P. Song, Leveraging neighborhood structural holes to identifying key spreaders in social networks, Acta Phys. Sin. Chin. 64 (2) (2015) 1–11.

[34] L. Ding, J. Wang, W. Wei, Method for detecting key nodes who occupy structural holes in social network sites, in: T.-P. Liang, S.-Y. Hung, P.Y.K. Chau, S.-I. Chang (Eds.), PACIS, 2016, p. 174.

[35] X. Zhao, S. Guo, Y. Wang, The node influence analysis in social networks based on structural holes and degree centrality, in: International Conference on Computational Science and Engineering, 2017, pp. 708–711.

[36] R.S. Burt, Structural holes versus network closure as social capital, in: N. Lin, K. Cook. R.S. Burt (Eds.). Social Capital: Theory and Research. Gruvter. Juni 2001

[37] D. Chen, L. Lü, M.-S. Shang, Y.-C. Zhang, T. Zhou, Identifying influential nodes in complex networks, Phys, A 391 (4) (Feb. 2012) 1777–1787.

[38] G. Bianconi, A.-L. Barab´asi, Competition and multiscaling m evolving networks, in: The Structure and Dynamics of Networks, Princeton University Press, 2011. pp. 361–367.

[39] D. Zhang, Y. Wang, Z. Zhang, Identifying and quantifying potential super-spreaders in social networks, Sci. Rep. 9 (2019), pp. 1–11, 10.

[40] C. Castellano, R. Pastor-Satorras, Thresholds for epidemic spreading in networks, Phys. Rev. Lett. 105 (21) (Noy 2010).

[41] L. Lu, T. Zhou, Link prediction in complex networks: a survey, Phys. A 390 (6 (2011) 11501170.

[42] D. Liben-Nowell, J. Kleinberg, The link-prediction problem for social networks, J. Am. Soc. Inf. Sci. Technol. 58 (7) (May 2007) 1019–1031.

[43] P. Jaccard, The distribution of the flora in the alpine zone, New Phytol. 11 (2) (Feb.

[44] R. Albert, A.-L. Barabasi, Statistical mechanics of complex networks, Rev. Mod. Phys. 74 (47) (2002) 1–54.

[45] L.A. Adamic, E. Adar, Friends and neighbors on the web, Soc. Networks 25 (2001) 211–230.

[46] E. Ravasz, A.-L. Barabsi, Hierarchical organization in complex networks, Phys. Rev.

[47] T. Zhou, L. Lü, Y.-C. Zhang, Predicting missing links via local information, Eur. Phys. J. B 71 (4) (Oct 2009) 623–630.

[48] E.A. Leicht, P. Holme, M.E.J. Newman, Vertex similarity in networks, Phys. Rev. E 73 (Feb 2006) 026120

[49] M. Molloy, B. Reed, A critical point for random graphs with a given degre sequence, Random Struct. Algorithms 6 (2–3) (Mar. 1995) 161–180.

[50]JM. Kleinberg. Authoritative sources in a hyperlinked environment. J. ACM 46 (5) (Sep. 1999) 604–632.

[51] M.E.J. Newman, Networks : An Introduction, Oxford University Press, Oxford New York. 2010.

[52] A.-L. Barabasi, R. Albert. H. Jeong, Mean-field theory for scale-free random

[53] A. Paranjape, A.R. Benson, J. Leskovec, Motifs in temporal networks, in: Proceedings of the Tenth ACM International Conference on Web Search and Data Mining, 2017, pp. 601–610.

![](/api/attachments/NR87EWX5/fulltext/images/d0a1a78a23938c4c77e3e32f56e0fd17f457a86dcf039226af23ed8479476f85.jpg)

Charles Perez is Associate Professor in the Department of Digital Entrepreneurship & Society, Paris School of Business, France. He received his Ph.D. from the University of Technol ogy of Troyes in 2014. He was the head of the digital, data, design research chair from 2017 to 2019. His research interests include social network analysis, big data, data mining and entrepreneurship. In addition to the 5 books he has written on digital, he has published in ranked journals including Journal o Decision Systems, Technological Forecasting and Social Change or Journal or Retailing and Consumers Services.

![](/api/attachments/NR87EWX5/fulltext/images/8a2dfef16ab2590e27b73322a113e8e922698414b724f4f97a5cd66d46bd4015.jpg)  
more than 10 Internation al journals.

I-Hsien Ting is an Associate Professor in the Department of Information Management, National University of Kaohsiung, TAIWAN. He has a PhD degree in Computer Science, the Uni versity of York, UK, His research interests are focusing on Data Mining and E-commerce, particular on Web Mining, Social Network Analysis, Web Intelligence, E-commerce and Semantic Web. He used to be a program chair of ASONAM 2011 in Kaohsiung and program chair of KMO conference from 2013– 2022. Besides, he joins as chair of more than 30 International conference and as the member of program committee for more than 100 International conferences. Furthermore, he is now the managing editor of international journal of Information Pri vacy, Security and Integrity as well as in the editor board for
