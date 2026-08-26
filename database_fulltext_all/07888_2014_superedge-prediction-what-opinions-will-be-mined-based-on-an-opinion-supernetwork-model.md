---
otero_id: 7888
otero_key: "PDW79DCB"
title: "Superedge prediction: What opinions will be mined based on an opinion supernetwork model?"
authors: "Yijun Liu; Qianqian Li; Xianyi Tang; Ning Ma; Ruya Tian"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.05.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Superedge prediction: What opinions will be mined based on an opinion supernetwork model?

Yijun Liu <sup>a,b,</sup>⁎, Qianqian Li <sup>a,b</sup>, Xianyi Tang <sup>b</sup>, Ning Ma <sup>a,b,c</sup>, Ruya Tian <sup>a,b,c</sup>

<sup>a</sup> Institute of Policy and Management, Chinese Academy of Sciences, Beijing 100190, China

<sup>b</sup> Center for Interdisciplinary Studies of Natural and Social Sciences, Chinese Academy of Sciences, Beijing 100190, China

<sup>c</sup> University of Chinese Academy of Sciences, Beijing 100049, China

## a r t i c l e i n f o

Article history: Received 18 April 2013 Received in revised form 2 April 2014 Accepted 8 May 2014 Available online xxxx

Keywords: Public opinion Supernetwork Superedge prediction

## a b s t r a c t

How do Internet users' opinions evolve under the in<sup>fl</sup>uence of factors such as information environment and psychological forces? We developed an opinion supernetwork model with social, environmental, psychological and keyword subnetworks. This model integrated a combination of external and internal factors which in<sup>fl</sup>uence opinion formation. From a different perspective, we applied superedge prediction, which is a novel link prediction method based on the supernetwork model, to analyze emerging superedges in the opinion supernetwork model. Comparing the predicted network with actual network, we revealed a fair amount of consistency between them. In addition, based on the predicted opinion supernetwork model, we investigated opinion dynamics, which shed some light on public opinion governance.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

French philosopher Jean-Jacques Rousseau was the <sup>fi</sup>rst to use the concept of l'opinion publique (public opinion) in his 18th century book The Social Contract. He also believed that “there is no people on earth the choice of whose pleasures is not decided by opinion rather than nature”. Following the rapid development and widespread application of Web 2.0, the world's largest social networking site is Facebook, with over 700 million daily active users. With close to 300 million microblog users, China is currently the country with the world's most microblog users. Virtual society increasingly shows the characteristics of a small world phenomenon. During riots in London and protest movements in Russia, the instigators made use of social network to spread public opinion. Learning more about what lies behind people's thoughts and behavior has prompted many scholars to explore the complex phenomenon of public opinion, conducting research from many different angles [1,2]. Sociologists focus on the social formation process of public opinion; psychologists focus on the mental process of public opinion expression; political scientists focus on aspects such as the in<sup>fl</sup>uence of public opinion on policy-making.

Supernetworks [3] and superedge predictions [4] are both very recently introduced theories. Supernetworks possess multileveled, multilayered, multidimensional, multi-attributed, congestive, and aggregative characteristics. Conventional social network only re<sup>fl</sup>ect some essential elements of public opinion (such as agents or information about public opinion). In contrast, supernetworks can simultaneously reveal more trends in the information dissemination of public opinion events, such as people's interactions, attitude changes and the development of their perspectives. The supernetwork model acts as an effective presentation to describe the complex system of public opinion, and through calculating and analyzing its topological properties one can explore the structure and functions of a part of the public opinion system. Superedge prediction refers to using supernetworks to make predictions of existent yet unknown superedges and future superedges. Superedge prediction is an important advancement and innovation in existing supernetwork research and it has realized an evolution and modulation in the structure of complex supernetworks and prediction analysis. When applied to public opinion supernetworks, the superedge prediction process is simulation and analysis of the dynamic evolvement process of the public opinion supernetwork, creating a macroscopic view and judgment of online public opinion.

Section 2 of this paper is a review of related research, starting with a summary and analysis of the three keywords: public opinion, supernetwork and superedge prediction respectively. Section 3 establishes the public opinion supernetwork model and provides its measurement indices. Section 4 proposes the superedge prediction algorithm based on the public opinion supernetwork, while Section 5 applies it to an actual public opinion supernetwork case. The paper concludes with a discussion providing some suggestions for further research work.

Y. Liu et al. / Decision Support Systems xxx (2014) xxx–xxx

## 2. Related research

## 2.1. Public opinion

Public opinion research began with studies in the <sup>fi</sup>eld of social sciences, and is the main research content of communication studies. In the mid-20th century, public opinion expanded beyond the scope of social science when it caught the interest of a large number of academics in the area of natural sciences. The French were the earliest to apply mathematical modeling to public opinion research [5]. Harary began mathematical model analysis [6], De Groot gave his expertise on the consensus-building process from the perspective of statistics [7], and Haken introduced the order parameter from the perspective of systemic studies [8]. In the late 20th century, the main focus of public opinion research in the <sup>fi</sup>eld of natural sciences was in statistical physicists' use of the particle interaction model to model the process of public opinion dynamics [9]. The main developments in the public opinion model include the S model [10], the Majority Rule model [11], the Social In<sup>fl</sup>uence model [12], the D model [13] and the HK model [14].

With the rapid development of the Internet society, online public opinion research has already become a hot topic of public opinion research, receiving a lot of attention. So far, online public opinion research content mainly includes its formation [15,16], its dissemination [17,18], its development [19], its guidance [20,21] and intervention [22]. With natural sciences such as theoretical physics, complexity science, and computer science as the research perspective, we are mainly provided with quantitative research methods for the dissemination and development of online public opinion. With social sciences such as sociology, social psychology, and journalism and communication studies as the research perspective, more emphasis is placed on the qualitative description of the formation, guidance and intervention of online public opinion, providing a theoretical foundation for online public opinion research.

In 2012, Yijun Liu and associates applied “supernetwork” model theory to online public opinion research for the <sup>fi</sup>rst time. They established a set of social, environmental, psychological and keyword subnetworks for an integrated social public opinion supernetwork model. They combined qualitative and quantitative methods to research the formation, development and intervention of public opinion as well as identi<sup>fi</sup>ed key roles [23–26].

## 2.2. Supernetwork model

Shef<sup>fi</sup> was the <sup>fi</sup>rst to come up with the “supernetwork” concept in his study of urban transportation networks [27]. In 2002, Nagurney and Dong used supernetwork to describe networks that were above and beyond existing networks [3]. The characteristics of supernetworks [28,29] are strongly consistent with those of actual networks, and can thus be used to explore the interactions between different networks. So after its conception, the supernetwork concept quickly received much attention and was applied in numerous <sup>fi</sup>elds.

There are two ways to de<sup>fi</sup>ne a supernetwork. The <sup>fi</sup>rst de<sup>fi</sup>nition is by using a hypergraph, that is, any network that uses a hypergraph to describe it is a supernetwork [30]. Berge came up with the hypergraph concept in the 1970s [31]. Since then, research on hypergraphs has focused on areas such as hypergraph connectivity, hypertrees, hypergraph minimum cut partitioning, directed hypergraphs and hypergraph topological analysis [32]. Estrada and others also studied hypergraphs from the perspective of social network analysis [30,33]. In the second de<sup>fi</sup>nition, by Frank and others, the vertices in a supernetwork indicate a given collection of networks, and the edges or arcs indicate the joint movements and joint preferences in given concentrations. The supernetwork uniquely indicates the rule-governed network formed through the joint movements and joint preferences [34].

Supernetworks provide new perspectives and methods for our understanding and study of the variety of complex networks in the world. Currently, there are three main supernetwork research methods. The <sup>fi</sup>rst is based on variational inequality, and used to resolve equilibrium and optimization problems. Its application areas include supply chains [35–37], transportation [37,38], <sup>fi</sup>nance [39,40] and collective intelligence [41]. The second is based on hypergraphs, and used to conduct structural analysis of supernetwork topology. Its appli cation areas include electricity [42], chemistry [43], biology [44], knowledge representation [45] and information transmission [46]. The third is based on systems science and is mostly directed at analysis of network structures' own centrality, clustering and robustness qualities. Its application areas include knowledge management [47–50], organizational cooperation [51], information & communication [52] and social network [53].

As supernetwork research continued to advance, some academics have spread the parameter indices of complex networks and hypergraphs to supernetworks [30,54]. In 2012, Ma Ning and others proposed 4 kinds of supernetwork measurement indices (clustering co ef<sup>fi</sup>cient, node superdegree, superedge overlap and node distribution). They used these indices to identify leading public opinion agents in the network [26], which <sup>fi</sup>lled a blank in supernetwork measurement index research. In 2013, Ma Ning and others further improved the superedge overlap, and proposed superedge degree and superedge– superedge distance indices and a superedge ranking algorithm [55]. This <sup>fi</sup>lled a blank in four-layered supernetwork topology structure measurement and calculation research.

## 2.3. Link prediction and superedge prediction

In recent years, link prediction has already become a hot topic in the study of complex networks, receiving extensive attention from scientists in different <sup>fi</sup>elds of study. Link prediction refers to the use of known network nodes and network structure information to predict the probability of two not yet linked nodes in the network becoming linked [56]. It includes the prediction of existent yet unknown links and future links.

Link prediction research usually starts from the perspective of network structure and node attributes. Overall, there are three types of link prediction research methods [57]. The first is based on a Markov chain or machine learning and in most cases takes the attributive properties of the nodes into consideration. Although this method can achieve higher prediction precision, due to the complexity of its calculation and its use of non-universal parameters, the scope of its application is restricted. The second method is based on a maximum likelihood estimation of the network structure. This method of calculating is very complex and thus not suitable for networks of a larger scale. The third method is based on similarity, and is relatively simple compared to the previous two methods, yet can achieve very good prediction results. There are currently more than 20 different de<sup>fi</sup>nitions of similarity indices [58]. These indices are again divided into similarity indices based on local information [59], similarity indices based on trajectory [60–62], and similarity indices based on random walk [63].

Link prediction solved the incomplete data problem that was prevalent in research. Its main areas of application include recommendation systems [64], network structure evolution analysis [65], and missing edge and faulty edge link prediction [66,67]. Currently, link prediction research in weighed networks, directed networks, heterogeneous networks and bipartite networks is still insuf<sup>fi</sup>cient [68–70]. These areas may become the focus of future research in link prediction.

In 2012, Yijun Liu and others employed a network structure similarity method. They introduced the super triangle concept as a similarity measurement index, and proposed a subnetwork intralayer superedge prediction algorithm for the <sup>fi</sup>rst time [4].

![](/api/attachments/PDW79DCB/fulltext/images/9f17456b7faf54d1d95dd737d5852971bdba6686db7e466507de5bfeed09d808.jpg)  
Fig. 1. Diagram of online public opinion supernetwork model.

The innovation of this research was that the foundation for superlink prediction lies in the supernetwork modeling environment. As the attributes of each layer of nodes are heterogeneous, and the superedge links between nodes in different network layers, the information is multivariate and abundant, and the network structure is more complex.

## 3. Opinion supernetwork

## 3.1. Opinion supernetwork model

A supernetwork can better re<sup>fl</sup>ect the complex and dynamic nature of online public opinion events. The elements of online public opinion in a supernetwork model include public opinion agents, external environmental factors, internal psychological forces, and opinion keywords. The correlation is that the “opinion keywords” are derived from the “public opinion agents” who are under the combined in<sup>fl</sup>uence of “external environmental forces” and “internal psychological forces”. The four elements respectively form the four subnetwork layers of the online public opinion supernetwork model, including “Social Subnetwork”, “Environmental Subnetwork”, “Psychological Subnetwork”, and “Keyword Subnetwork”.

The public opinion supernetwork is a binary related $O S N = ( V ,$ SE) hypergraph. $V = V _ { A } \cup V _ { E } \cup V _ { P } \cup V _ { K } , V _ { A } = \{ a _ { 1 } , a _ { 2 } , \cdots , a _ { m } \} , V _ { E } =$ $\{ e _ { 1 } , e _ { 2 } , \cdots , e _ { n } \} , V _ { P } = \{ p _ { 1 } , p _ { 2 } , \cdots , p _ { r } \} , V _ { K } = \{ k _ { 1 } , k _ { 2 } , \cdots , k _ { q } \} . V$ is a <sup>fi</sup>nite set, where $V _ { A }$ represents the set of nodes in the Social Subnetwork, $V _ { E }$ represents the set of nodes in the Environmental Subnetwork, V represents the set of nodes in the Psychological Subnetwork, and $V _ { K }$ represents the set of nodes in the Keyword Subnetwork. $S E = \{ S E _ { 1 } , S E _ { 2 } , \cdots , S E _ { M } \}$ is the set of superedges in the hypergraph, $\cup \ : \ : _ { i } ^ { M } = \ : _ { 1 } S E _ { i } = V$ One superedge ${ S E _ { i } } = \Big \{ { \nu _ { i _ { 1 } } } , { \nu _ { i _ { 2 } } } , \cdots , { \nu _ { i _ { j } } } \Big \} ( i = 1 , 2 , \cdots , M )$ of which $\exists \nu _ { i _ { k } } \in V _ { A } , \exists \nu _ { i _ { m } } \in V _ { E } , \exists \nu _ { i _ { n } } \in V _ { P } ,$ , and $\exists { } v _ { i _ { q } } \in { } V _ { K } .$

The four subnetworks in the online public opinion supernetwork model are connected through superedges (SE), which indicates that public opinion agent α issues opinion $k _ { n }$ under the in<sup>fl</sup>uence of external environmental forces $e _ { m }$ and internal psychological forces p (Fig. 1). After modeling, a superedge prediction algorithm can be used to predict the possible superedges in and between all subnetworks of the supernetwork.

Network structure measurement indices

<table><tr><td></td><td>Network measurement</td><td>Index</td><td>Concept</td></tr><tr><td rowspan="3">Supernetwork measurement indices</td><td>Node superdegree</td><td> $SD_i$ </td><td>The node superdegree of a particular node in the supernetwork refers to the number of connected superedges of the node [33]. This is similar to the connectivity of nodes in social network analysis (SNA), i.e. the sum of out-degree and in-degree.</td></tr><tr><td>Superedge overlap</td><td> $SO = \frac{\sum_{i,j\in N,i\neq j}^{N} SO_{ij}}{C_N^2}$ </td><td>N stands for the number of all superedges in supernetwork;  $SO_{ij}$  stands for the value of superedge overlap between  $SE_i$  and  $SE_j$  [55].</td></tr><tr><td>Superedge-superedge distance</td><td> $d_{SE}$ </td><td>Superedge-superedge distance is defined as the shortest path between two superedges. This index can be used to measure the connectivity of a supernetwork [55].</td></tr><tr><td rowspan="3">Social network measurement indices</td><td>Degree</td><td> $k_i$ </td><td>Generally, assume that a node i in the network has  $k_i$  edges linking it and other nodes together, this  $k_i$  node is then called node i&#x27;s neighbor. Intuitively, the larger a node is signifies that this node is in some way more “important.”</td></tr><tr><td>Clustering coefficient</td><td> $C_i = 2E_i/(k_i(k_i - 1))$ </td><td>Assume that node i has  $k_i$  neighbors, and between these  $k_i$  nodes there can only be as many as  $k_i(k_i - 1)/2$  edges. The ratio of the number existing edges  $E_i$  between these  $k_i$  nodes and the total number of possible edges  $k_i(k_i - 1)/2$  determines the clustering coefficient  $C_i$  of node i.</td></tr><tr><td>Average shortest path length</td><td> $L = \frac{1}{2N(N+1)} \sum_{i \ge j} d_{i,j}$ </td><td>The distance  $d_{ij}$  between the two nodes i and j in the network defines the edge with the shortest path length connecting these two nodes. The average network path length L defines the mean of the distance between all pairs of nodes in the network.</td></tr></table>

Please cite this article as: Y. Liu, et al., Superedge prediction: What opinions will be mined based on an opinion supernetwork model?, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.05.011

Y. Liu et al. / Decision Support Systems xxx (2014) xxx–xxx

$$
\begin{array}{c} \text {In Fig. 1, SE_{1} = \{a_{1} , e_{1} , p_{1} , k_{1} , k_{2} , k_{3} , k_{4} , k_{5} \} , SE_{2} = \{a_{2} ,e_{2} ,p_{1} ,k_{2} ,k_{3} \} ,} \\ S E _ {3} = \{a _ {3}, e _ {1}, e _ {2}, e _ {3}, p _ {2}, k _ {4}, k _ {5}, k _ {6}, k _ {7} \}. \end{array}
$$

## 3.2. Data collection and preparation

Using Founder Electronics' Network Public Opinion Monitoring and Analyzing System, mine for Sina Weibo microblog data relevant to the public opinion event, and collect all the data needed for the opinion supernetwork model.

✓ Social Subnetwork: after a Weibo post is published, the content of the comments can re<sup>fl</sup>ect trends in society's general public opinion. Establish the netizens' response relationship towards the information according to the formation and evolution of online public opinion.

✓ Environmental Subnetwork: a popular Weibo post represents an information node. When choosing the time period for this paper, we chose the top N popular Weibo posts speci<sup>fi</sup>c to the public opinion event to construct the Environmental Subnetwork, calculating Weibo popularity  <sup>number</sup> <sup>of</sup> <sup>Weibo</sup> <sup>reposts</sup>þ<sup>number</sup> <sup>of</sup> <sup>Weibo</sup> <sup>comments</sup>

✓ Psychological Subnetwork: there is a subtle psychological reason behind every action. 3 evaluators used a Likert 5-point scale method [71] (in a typical scale 1 stands for very negative, 2 stands for negative, 3 stands for neutral, 4 stands for positive, 5 stands for very positive) to rate the degree of positive/negative mentality in the each of the Weibo posts.

✓ Keyword Subnetwork: <sup>fi</sup>rst, use the NLPIR Chinese word segmentation system (also called ICTCLAS) to carry out word segmentation of the users' Weibo posts and conduct syntactical analysis. Then use the Barycenter clustering algorithm to conduct viewpoint phrase recognition.

## 3.3. Measurements and related definition

Based on the requirements for the public opinion supernetwork and social subnetwork structural evolution calculations in Section 5 of this paper, Table 1 lists the structure measurement indices of the traditional social network and public opinion supernetwork.

Next, we provide the de<sup>fi</sup>nitions for the super triangle and superedge similarity in the public opinion supernetwork, to be used in calculating the superedge prediction.

## 3.3.1. Definition 1 — super triangle

A super triangle is composed of three vertices $v _ { i } , v _ { j }$ and $\nu _ { k }$ and three superedges $S E _ { m } , S E _ { n }$ and $S E _ { p } \left[ 4 \right] ,$ , our super triangle will include a real super triangle and an analogous super triangle (Fig. 2). The former refers to a super triangle composed of three different vertices and three different superedges; if $\cdot _ { \nu _ { i } } \in S E _ { m } , \nu _ { j } \in S E _ { n } , \nu _ { k } \in S E _ { p }$ , and $i \neq j \neq k , m \neq n \neq p ,$ then the super triangle is a real super triangle. The latter refers to a super triangle composed of three different vertices and two different superedges; if $\cdot \nu _ { i } \in S E _ { m } , \nu _ { j } \in S E _ { n } , \nu _ { k } \in S E _ { p } , i \neq j \neq k ,$ m, n, and p, two and only two are equal, then the super triangle is an analogous super triangle.

In $\mathrm { F i g . } 2 , e _ { 2 } , S E _ { 3 } , k _ { 4 } , S E _ { 1 } , p _ { 1 } , S E _ { 2 }$ and e form a real super triangle (the red one); $e _ { 1 } , S E _ { 3 } , p _ { 2 } , S E _ { 3 } , k _ { 5 } , S E _ { 2 }$ and $e _ { 1 }$ form an analogous super triangle (the green one).

## 3.3.2. Definition 2 — superedge similarity

Superedge similarity is a measure of the similarity of superedges based on the quantity of super triangles formed by two superedges. The more super triangles formed by the two superedges, the higher similarity between them, and the higher probability of linked edges between them in the next instant. For the similarity of any two superedges $S E _ { i }$ and $S E _ { j } ,$ the following

![](/api/attachments/PDW79DCB/fulltext/images/7c410de9280085a50f9c0928886f71205f66892486e5d5866c58a638f21ccd0f.jpg)  
Fig. 2. Real super triangle and analogous super triangle. (For interpretation of the references to color in this <sup>fi</sup>gure, the reader is referred to the web version of this article.)

situations exist:

$$
\left\{ \begin{array}{c} \text {similarity} _ {S E _ {i} S E _ {j}} = 1, S E _ {i} \text {and} S E _ {j} \text {are identical} \\ \text {similarity} _ {S E _ {i} S E _ {j}} = 0, S E _ {i} \text {and} S E _ {j} \text {are totally different}. \\ \text {similarity} _ {S E _ {i} S E _ {j}} \in (0, 1), S E _ {i} \text {and} S E _ {j} \text {are similar} \end{array} \right.
$$

## 4. Superedge prediction

## 4.1. Basic algorithms

The computing ideas for the superedge prediction algorithm are as shown in Fig. 3. First, from the established opinion supernetwork model, devise supernetwork link matrix H. Based on this matrix, calculate superedge adjacency matrix $A _ { S E }$ Based on the above matrices, the super triangle number of the opinion supernetwork model can be calculated, with further calculation determining the similarity between any two superedges. We then proposed the prediction algorithm and evaluation method for superedge prediction within each subnetwork in the opinion network [4]. On this foundation, this paper takes another

![](/api/attachments/PDW79DCB/fulltext/images/13ce788befcddec0382ea2a9f43ee0d23dee71aa0fbb53939bc632c910b73ea3.jpg)  
Fig. 3. Superedge prediction algorithm <sup>fl</sup>owchart.

Please cite this article as: Y. Liu, et al., Superedge prediction: What opinions will be mined based on an opinion supernetwork model?, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.05.011

Y. Liu et al. / Decision Support Systems xxx (2014) xxx–xxx

step forward and extends a superedge prediction algorithm to the entire network.

## 4.1.1. Establish supernetwork connection matrix

The supernetwork connection matrix H consists of m lines and n columns. Each line represents a superedge $S E _ { m }$ including an opinion agent from social subnetwork. Each column represents a node $\nu _ { n }$ from the other 3 subnetworks. If the superedge $S E _ { m }$ contains node $\nu _ { n } ,$ the value of $H _ { m n }$ is 1. If not, it is 0.

## 4.1.2. Calculate superedge adjacency matrix

Superedge connections between nodes in the 3 subnetwork layers outside the social subnetwork are presented through superedge adjacency matrix $A _ { S E }$ of the nodes.

$$
A _ {S E} = H ^ {T} \cdot H - D.
$$

Element $A _ { S E }$ is the quantity of superedges containing nodes $\nu _ { i }$ and $\nu _ { j }$ and it is used to judge the existence of superedges in a super triangle. $D$ refers to a diagonal matrix and the diagonal element is the quantity of superedges containing node $\nu _ { i }$ while the off-diagonal element is 0. Element $( A _ { S E } ) _ { i j }$ shows whether there is a superedge connected between node $\nu _ { i }$ and node $\nu _ { j } .$ If the value of this element is nonzero, there is at least one superedge between the two nodes.

## 4.1.3. Determine super triangle

Generally, determining whether nodes $\nu _ { x }$ and $\nu _ { y }$ form a speci<sup>fi</sup>ed superedge SE<sub>i</sub> is the act of determining whether superedge SE<sub>i</sub> goes through nodes $\nu _ { x }$ and $\nu _ { y } ,$ and gives the calculation for <sup>fi</sup>nding the value of $\left( A _ { S E _ { i } } \right) _ { x y } .$

$$
\left(A _ {S E _ {i}}\right) _ {x y} = H _ {i x} \cdot H _ {i y} - \delta_ {x y} \cdot H _ {i x}
$$

$$
\delta_ {x y} = \left\{ \begin{array}{c c} 1 & x = y \\ 0 & x \neq y \end{array} \right..
$$

The ith row of matrix H is reserved as $H _ { S E _ { i } } . H _ { i x }$ and $H _ { i y }$ are the elements in the x column and y column of matrix $H _ { S E _ { i } }$ . Function $\delta _ { x y }$ is introduced to eliminate the effect of the diagonal element. If the value of $\left( A _ { S E _ { i } } \right) _ { x v }$ is 1, node $\nu _ { x }$ and $\nu _ { y }$ pass through superedge $S E _ { i }$ otherwise, they do not.

![](/api/attachments/PDW79DCB/fulltext/images/79716778065169234a30bc426031db3c54946a80bd2c18441bb213dcb0306a61.jpg)  
Fig. 5. “Jingwen Rumor Event” opinion supernetwork (partial view)

Suppose that a super triangle is composed of nodes $\nu _ { i } , \nu _ { j } ,$ , and $\boldsymbol { v _ { k } }$ and contains superedges $S E _ { 1 } , S E _ { 2 } ,$ and $S E _ { m } .$ . The following assumptions will become true under all conditions. 1) The sequence of nodes does not in<sup>fl</sup>uence the existence of superedges in the super triangle so it can be assumed that nodes $\nu _ { i }$ and $\nu _ { j }$ form superedge $S E _ { 1 }$ of the super triangle, $\nu _ { j }$ and $\boldsymbol { v } _ { k }$ form superedge $S E _ { 2 }$ of the super triangle, and $\boldsymbol { v } _ { k }$ and $\nu _ { i }$ form superedge $S E _ { m }$ of the super triangle. 2) As there is a corresponding relation between the nodes and superedges of the super triangle, determining whether vertices $\nu _ { i }$ and $\nu _ { j }$ form superedge $S E _ { 1 }$ is converted to determining whether nodes $\nu _ { i }$ and $v _ { j }$ pass through superedge $S E _ { 1 }$ . Consequently, only the value of $\left( A _ { S E _ { 1 } } \right) _ { i j }$ needs to be calculated.

For determining whether superedges $S E _ { 1 }$ and $S E _ { 2 }$ can form a super triangle, one can select any three nodes $\nu _ { i } , \nu _ { j } ,$ and $\boldsymbol { v _ { k } }$ from

![](/api/attachments/PDW79DCB/fulltext/images/6dd32fd1cbfa1d4d9482e034232f165cd0b34bddf68e1ef8a85e96128e193278.jpg)  
Fig. 4. “Jingwen Rumor Event” important public opinion agents.

Please cite this article as: Y. Liu, et al., Superedge prediction: What opinions will be mined based on an opinion supernetwork model?, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.05.011

Table 3  
Table 2  
“Jingwen Rumor Event” opinion supernetwork composition.

<table><tr><td>Subnetwork nodes</td><td>Type</td><td>Number</td><td>Explanation</td></tr><tr><td rowspan="3">Environmental information</td><td>Neutral</td><td> $e_1$ </td><td>Event occurrence: a young woman fell to her death at the Beijing Jingwen shopping mall</td></tr><tr><td>Negative</td><td> $e_2$ </td><td>Rumor information: her death was rumored to be a homicide</td></tr><tr><td>Positive</td><td> $e_3$ </td><td>Rebuttal information: provided strong evidence to refute any rumors</td></tr><tr><td rowspan="5">Psychological scale</td><td>Neutral (fluctuating)</td><td> $p_1$ </td><td>Onlooker status, waited for new relevant information</td></tr><tr><td>Negative (this event)</td><td> $p_2$ </td><td>Negative mentality caused by this event, believed it to be a homicide</td></tr><tr><td>Negative (enlarged derivative)</td><td> $p_3$ </td><td>Expanded negative mentality caused by this event, asserted that society is dark and corrupted</td></tr><tr><td>Positive (this event)</td><td> $p_4$ </td><td>Positive mentality caused by this event, trusted in the police</td></tr><tr><td>Positive (enlarged spread)</td><td> $p_5$ </td><td>Expanded positive mentality caused by this event, attitude approving of government and trusting in justice</td></tr><tr><td rowspan="15">Mainstream viewpoints</td><td rowspan="7">Discussion buzzwords created by the event</td><td> $k_1$ </td><td>Beijing shopping mall/Jingwen shopping mall/clothing shopping mall</td></tr><tr><td> $k_2$ </td><td>Girl/migrant worker/22 year old/youth</td></tr><tr><td> $k_3$ </td><td>Jumped from a building/fell to her death/jumped to her death</td></tr><tr><td> $k_4$ </td><td>Pitiful/what a pity/life is fragile</td></tr><tr><td> $k_5$ </td><td>Investigation organized/crime scene investigation/autopsy results</td></tr><tr><td> $k_6$ </td><td>Family members/relatives/friends</td></tr><tr><td> $k_7$ </td><td>Facts/onlookers/surveillance</td></tr><tr><td rowspan="2">Neutral viewpoints</td><td> $k_8$ </td><td>Waiting for new evidence/looking forward to surveillance tape</td></tr><tr><td> $k_9$ </td><td>Look forward to police reinvestigation</td></tr><tr><td rowspan="3">Negative viewpoints</td><td> $k_{10}$ </td><td>Raped by security guards/murdered/pushed to her death</td></tr><tr><td> $k_{11}$ </td><td>Police cover-up/case hastily settled/not on record</td></tr><tr><td> $k_{12}$ </td><td>Society cover-up/corrupt government/incompetent police</td></tr><tr><td rowspan="3">Positive Viewpoints</td><td> $k_{13}$ </td><td>Believe the results of the police investigation</td></tr><tr><td> $k_{14}$ </td><td>Believe the government will settle the case justly</td></tr><tr><td> $k_{15}$ </td><td>Believe Weibo&#x27;s official rumor rebuttal information</td></tr></table>

among all nodes of the two superedges. Then, 1) calculate $\left( A _ { S E _ { 1 } } \right) _ { i }$ to determine whether nodes $\nu _ { i }$ and $\nu _ { j }$ pass through superedge $S E _ { 1 } ; 2 )$ calculate $\left( A _ { S E _ { 2 } } \right) _ { j k }$ to determine whether nodes $v _ { j }$ and v pass through superedge $S E _ { 2 } ;$ and 3) determine whether there is a superedge between nodes $\boldsymbol { v } _ { k }$ and $\nu _ { i }$ through matrix $A _ { S E } .$ . If all of the above three conditions are met, superedges $S E _ { 1 }$ and $S E _ { 2 }$ can form a super triangle.

## 4.1.4. Calculate superedge similarity

Calculate the similarity between superedge SE and superedge SE .

similarit $\forall S E _ { 1 } S E _ { 2 }$

$$
= \frac {\frac {1}{6} \sum_ {v _ {i} , v _ {j} , v _ {k} \in S E _ {1} \cup S E _ {2}} \operatorname{sign} \left[ \sum_ {\alpha , \beta , \gamma = v _ {i} , v _ {j} , v _ {k}} \left(A _ {S E _ {1}}\right) _ {\alpha \beta} \left(A _ {S E _ {2}}\right) _ {\beta \gamma} \left(A _ {S E}\right) _ {\gamma \alpha} \right]}{C _ {| S E _ {1} \cup S E _ {2} |} ^ {3}}
$$

$$
\operatorname{sign} (x) = \left\{ \begin{array}{l l} 1 & x > 0 \\ 0 & x = 0 \\ - 1 & x <   0 \end{array} \right..
$$

The numerator refers to the number of super triangles formed by the two superedges, while the denominator represents the max number of any combination of three nodes in $S E _ { 1 }$ and $S E _ { 2 }$ . Function sign is used to judge whether the three vertices $\alpha , \beta ,$ and γ can form a super triangle. When the value of $\left( A _ { S E _ { 1 } } \right) _ { \alpha \beta } \mathrm { i } s 1$ , vertices α and β pass through superedge $S E _ { 1 }$ , otherwise, the value would be $0 ;$ when the value of $\left( A _ { S E _ { 2 } } \right) _ { \beta \gamma }$ is 1, vertices $\beta$ and $\gamma$ pass through superedge $S E _ { 2 } .$ . Otherwise, the value would be 0; When the value of $( A _ { S E } ) _ { \gamma \alpha } \mathrm { i s } 1$ , there is a superedge between vertices $\gamma$ and α. Otherwise, the value would be 0. In the case that all three values are 1, vertices α, $\beta ,$ and γ can form a super triangle. $\mathrm { I f } { S E } \ne { S E } _ { 1 }$ and $S E \neq S E _ { 2 } ,$ , then α, β, and γ form a real super triangle; if $S E = S E _ { 1 }$ or $S E = S E _ { 2 }$ , then α, $\beta ,$ and γ form an analogous super triangle.

Dataset required for the superedge prediction and evaluation based on an actual case.

<table><tr><td></td><td>Data collection period</td><td>Constructed matrix</td></tr><tr><td>Data needed for superedge prediction calculation</td><td>May 3, 2013–May 7,2013</td><td> $H$  matrix &amp;  $A$  matrix</td></tr><tr><td>Data needed for evaluation of superedge prediction results</td><td>May 8,2013</td><td> $E^{P}$  matrix</td></tr></table>

$$
\sum_ {v _ {i}, v _ {j}, v _ {k} \in S E _ {1} \cup S E _ {2}} \text { sign } \left[ \sum_ {\alpha , \beta , \gamma = v _ {i}, v _ {j}, v _ {k}} \left(A _ {S E _ {1}}\right) _ {\alpha \beta} \left(A _ {S E _ {2}}\right) _ {\beta \gamma} (A _ {S E}) _ {\gamma \alpha} \right]\tag{to}
$$

refers

adding super triangles determined through function sign, namely, selecting any three nodes $\nu _ { k } , \nu _ { j } ,$ and $\boldsymbol { v } _ { k }$ from all nodes of superedges $S E _ { 1 }$ and $S E _ { 2 }$ to ascertain how many super triangles can be formed by them. Any equivalent three nodes $\nu _ { j } , \nu _ { j } ,$ and $\boldsymbol { v } _ { k }$ can be evaluated in turn. As calculating the elements in different orders yields redundant calculations, only $1 / 6$ may be selected. The denominator is the quantity of triplets formed by any set of three nodes from among all nodes of superedges $S E _ { 1 }$ and $S E _ { 2 } .$ . It yields the maximum number of possible super triangles through superedges $S E _ { 1 }$ and $S E _ { 2 } .$ . The values of the similarity between the superedges compose superedge similarity matrix $A _ { s i m } .$ . The values of elements at corresponding positions of the matrix are the similarity values of the two superedges. Additionally, a mapping relation exists between superedges and nodes in the social subnetwork, so this matrix is the similarity matrix of nodes in the social subnetwork.

## 4.2. Subnetwork intralayer superedge prediction

## 4.2.1. Prediction algorithm

The super common neighbor index was proposed based on a single layered network common neighbor method [57,58]. The more super common neighbors between two nodes, the higher the probability that a superedge exists between them. Once the superedge

Table 4  
Dataset required for analysis of superedge prediction results based on an actual case

<table><tr><td></td><td>Data collection period</td><td>Constructed matrix</td></tr><tr><td>Data needed for superedge prediction calculation</td><td>May 3, 2013–May 8,2013</td><td>H matrix &amp; A matrix</td></tr><tr><td>Results of superedge prediction algorithm</td><td>May 9,2013</td><td>-</td></tr></table>

Please cite this article as: Y. Liu, et al., Superedge prediction: What opinions will be mined based on an opinion supernetwork model?, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.05.011

Table 5  
Table 7  
Dataset required for analysis of superedge prediction results based on an actual case.

<table><tr><td></td><td>Data collection period</td><td>Analysis content</td></tr><tr><td>Actual case opinion</td><td>May 3, 2013–</td><td>Supernetwork structure</td></tr><tr><td>supernetwork</td><td>May 8, 2013</td><td>evolution and subnetwork</td></tr><tr><td>Actual case opinion</td><td>May 3, 2013–</td><td>evolution</td></tr><tr><td>supernetwork + predicted supernetwork</td><td>May 9, 2013</td><td></td></tr></table>

similarity matrix $A _ { s i m }$ for a supernetwork is acquired via the basic algorithm shown in Section 4.1 of this paper, the superedge adjacency matrix A of the social subnetwork and superedge similarity matrix $A _ { s i m }$ get <sup>fi</sup>ltered (<sup>fi</sup>ltration refers to replacing the nonzero elements in matrix A with similarity values corresponding to their positions in matrix $A _ { s i m } )$ . This is done to acquire the improved superedge adjacency matrix super A based on the similarity of the nodes in the social subnetwork. Then, the super common neighbor index is de<sup>fi</sup>ned as [4]:

$$
S _ {x y} ^ {S C N} = \left(\text { super } A ^ {2}\right) _ {x y}.
$$

The higher the fractional value of the corresponding position of the super common neighbor matrix ${ \mathrm { i } } s ,$ the higher the probability that an edge exists between the two nodes. K edges with relatively high scores are selected as probable edges for node $\nu _ { ( a ) _ { i } }$ in the social subnetwork.

## 4.2.2. Evaluation method

To verify the accuracy of the superedge prediction algorithm, this article adopts the AUC (area under the receiver operating characteristic curve) [72] method for evaluating the overall accuracy of the superedge prediction algorithm. In AUC, the observation set SE is randomly divided into a training set SE<sup>T</sup> and a probe set $S E ^ { P } .$ . Then, by randomly selecting a superedge from the probe set and comparing it with a randomly selected, non-existent superedge, AUC can be calculated as:

$$
\mathrm{AUC} = \frac {n ^ {\prime} + 0 . 5 n ^ {\prime \prime}}{m \times n}
$$

n′ refers to the number of fractional values of superedges in the probe set that is greater than those of the non-existent superedge. $n ^ { \prime \prime }$ refers to the number of fractional values of superedges in the probe set that is equal to those of the non-existent superedge. m represents the scale of the probe set, and n is the scale of the set of the non-existent superedge. An AUC value of 0.5 would indicate that all fractions were generated randomly, so the degree by which the AUC value is greater than 0.5 can be used to measure to what degree the algorithm is more accurate than the random selection method.

Table 6  
AUC evaluation of link prediction and intralayer superedge prediction.

<table><tr><td></td><td>CN</td><td>SCN</td><td>Accuracy improved by</td></tr><tr><td>AUC evaluation</td><td>0.578</td><td>0.661</td><td>14.36%</td></tr></table>

Subnetwork intralayer superedge prediction results

<table><tr><td>Rank</td><td>Public opinion agent</td><td>SCN</td><td>Rank</td><td>Public opinion agent</td><td>SCN</td></tr><tr><td>1</td><td> $a_5$  and  $a_{17}$ </td><td>0.0178</td><td>6</td><td> $a_8$  and  $a_{16}$ </td><td>0.0108</td></tr><tr><td>2</td><td> $a_3$  and  $a_{16}$ </td><td>0.0159</td><td>7</td><td> $a_3$  and  $a_{22}$ </td><td>0.0106</td></tr><tr><td>3</td><td> $a_3$  and  $a_4$ </td><td>0.0127</td><td>8</td><td> $a_5$  and  $a_9$ </td><td>0.0099</td></tr><tr><td>4</td><td> $a_3$  and  $a_8$ </td><td>0.0121</td><td>9</td><td> $a_9$  and  $a_{17}$ </td><td>0.0099</td></tr><tr><td>5</td><td> $a_4$  and  $a_{16}$ </td><td>0.0113</td><td>10</td><td> $a_{16}$  and  $a_{22}$ </td><td>0.0094</td></tr></table>

## 4.3. Supernetwork interlayer superedge prediction

## 4.3.1. Prediction algorithm

The above methods enable the acquisition of the subnetwork intralayer relation between nodes in the social subnetwork (represented as $S ( a ) )$ of the supernetwork This is the acquisition of newly added next instant neighbors $\nu _ { ( a ) _ { 1 } } , \nu _ { ( a ) _ { 2 } } , \cdots , \nu _ { ( a ) _ { j } }$ of any node in the social subnetwork $S ( a )$ . The superedge of node $\nu _ { ( a ) _ { i } }$ is $S E _ { i } ;$ superedges of all j new neighbors are therefore $S E _ { 1 } , S E _ { 2 } , \cdots , S E _ { j }$ . All the superedges contain nodes in the social subnetwork as well as in the other 3 subnetwork layers. The several most frequent nodes of the other 3 subnetwork layers in superedges are nodes connected to next instant node $\nu _ { ( a ) _ { i } }$ . Superedges formed by such nodes and node $\nu _ { ( a ) _ { i } }$ are the new superedges formed by node $\nu _ { ( a ) _ { i } }$ in the next instant. The speci<sup>fi</sup>c algorithm is: in instant $t + 1$ , if a new connection edge in the social subnetwork exists at node $\nu _ { ( a ) _ { i } }$ , based on the newly added neighbor's superedge information, the superedge evolution of node $\nu _ { ( a ) _ { i } }$ can be predicted as follows:

$$
\left\{ \begin{array}{l} S E _ {(i)} (t + 1) = \Big (S (a) _ {i}, S (e) _ {\varphi_ {e}}, S (p) _ {\varphi_ {p}}, S (k) _ {\varphi_ {k}} \Big) \\ \varphi_ {(e)} (i, U (i)) = \arg \max \Big (S (a) S (e) _ {(i)} ^ {T} S (a) S (e) _ {U (i)} \Big) \\ \varphi_ {(p)} (i, U (i)) = \arg \max \Big (S (a) S (p) _ {(i)} ^ {T} S (a) S (p) _ {U (i)} \Big) \\ \varphi_ {(k)} (i, U (i)) = \arg \max \Big (S (a) S (k) _ {(i)} ^ {T} S (a) S (k) _ {U (i)} \Big) \\ U (i) = S (a) _ {(i)} (t + 1) - S (a) _ {(i)} (t). \end{array} \right.
$$

U(i) is the index of new neighbors in the social subnetwork of node $\nu _ { ( a ) _ { i } \cdot } \varphi _ { ( e ) } ( i , U ( i ) )$ is the index of the most frequent nodes of new individual neighbors in the environmental subnetwork. $\varphi _ { ( p ) } ( i , U ( i ) )$ is the index of the most frequent nodes of new individual neighbors in the psychological subnetwork. $\varphi _ { ( k ) } ( i , U ( i ) )$ is the index of the most frequent nodes of new individual neighbors in the keyword subnetwork.

![](/api/attachments/PDW79DCB/fulltext/images/ab5a728e80bf2c077741f27b3375560dd6a58dbcfe1662eac8dbdf98d95ae90e.jpg)  
Fig. 6. Social subnetworks for “Jingwen Rumor Event” (May 3, 2013–May 7, 2013) (partial view).  
Please cite this article as: Y. Liu, et al., Superedge prediction: What opinions will be mined based on an opinion supernetwork model?, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.05.01

![](/api/attachments/PDW79DCB/fulltext/images/2d8bab495f93a6a3819d7dd84c0d20dfd0da1b7ba5a7e48cd0a0aaa4b773926c.jpg)  
Fig. 7. “Jingwen Rumor Event” opinion supernetwork structural evolution (partial view).

## 4.3.2. Evaluation method

Divide the existent superedges into two sets: a test set (predicted superedge $S E _ { p i } )$ and a training set (actual superedge $S E _ { r _ { i } } )$ . Assume that in instant t + 1, the superedge quantity obtained through the superedge between supernetwork layer prediction algorithm is L. Take the predicted superedges one by one and compare them with the actual superedge. If nodes contained in one superedge in the test set also exist in the corresponding superedge in the training set, record the fraction $( 1 / | S E _ { r _ { i } } | )$ corresponding to this node. Repeat the above calculation for L superedges in test set, and then calculate the mean value, which represents SuperEdge Prediction Accuracy (SEPA):

$$
S E P A = \frac {\sum_ {i = 1} ^ {L} \left| S E _ {p _ {i}} \cap S E _ {r _ {i}} \right| \times \frac {1}{\left| S E _ {r _ {i}} \right|}}{L}.
$$

## 5. A case study

## 5.1. Brief introduction and data processing

Early in the morning of May 3, 2013, a young woman fell to her death at the Beijing Jingwen shopping mall. After a police investigation, it was stated to be a case of suicide. Soon after, rumors started

## Table 9

Supernetwork structure indices.

<table><tr><td>Measurement index</td><td>Actual supernetwork May 3, 2013–May 8, 2013</td><td>Actual supernetwork + predicted superedges May 3, 2013–May 9, 2013</td></tr><tr><td>Node superdegree</td><td>3.565</td><td>4.065</td></tr><tr><td>Superedge–superedge distance</td><td>0.478</td><td>0.388</td></tr><tr><td>Superedge overlap</td><td>0.227</td><td>0.241</td></tr></table>

circulating on Sina Weibo microblogs that the deceased had been murdered, unleashing a torrent of criticism. On May 8, Sina Weibo's of<sup>fi</sup>cially recognized “Weibo Rumor Rebuttals” microblog channel carried out a rebuttal directed at the rumors circulating about this incident, and the matter gradually subsided. In this paper the incident will be simply be referred to as the “Jingwen Rumor Event.”

We constructed this event's opinion supernetwork based on data from Sina Weibo microblog users who participated in discussions on this incident as well as data from microblog content during the time period (May 3, 2013–May 8,2013), all collected through Founder Electronics' Network Public Opinion Monitoring and Analyzing System. The opinion supernetwork involves 22 people (Fig. 4) as important public opinion agents (A), 3 sets of environmental information (E), 5-point scale psychology (P) and 15 mainstream viewpoints (K) (Fig. 5, Table 2)

To process the above data, we chose data from different time periods to construct the actual case H and A matrices (where H matrix is the opinion supernetwork connection matrix, and A matrix is the social subnetwork adjacency matrix), and $E ^ { P }$ evaluation matrix respectively. We mainly carried out the following different research objectives:

(1) Evaluation and prediction methods: we selected the May 3, 2013– May 7, 2013 time period data to construct the H and A matrices needed for the superedge prediction analysis. We selected all the data from the day of May 8, 2013 to construct the $E ^ { P }$ matrix. We then conducted superedge prediction calculation and evaluation based on the above three matrices (Table 3).

(2) Calculate prediction results: we selected all the collected data, that is to say the data from the entire May 3, 2013–May 8, 2013 time period used to construct the H and A matrices. We then conducted superedge prediction calculations, producing the superedge prediction results for day May 9, 2013 (Table 4).

(3) Analysis of evolution process: we selected the May 3, 2013– May 8, 2013 actual opinion supernetwork and May 3, 2013– May 9, 2013 opinion supernetwork (which includes the May 3, 2013–May 8, 2013 actual opinion supernetwork and the May 9, 2013 predicted supernetwork) to be used as the dataset for comparative analysis. We analyzed the evolutionary process of the actual case opinion supernetwork and all the subnetworks (Table 5).

## Table 8

Subnetwork interlayer superedge prediction results.

<table><tr><td></td><td>Actual superedges during May 3, 2013–May 8, 2013</td><td>Predicted superedges on May 9, 2013</td><td>Nodes changed as predicted</td></tr><tr><td> $SE_{a_3}$ </td><td> $\{a_3, e_2, p_1, k_8, k_{10}\}$ </td><td> $\{a_3, \boldsymbol{e}_3, \boldsymbol{p}_4, \boldsymbol{k}_4, k_8, \boldsymbol{k}_9, \boldsymbol{k}_{14}\}$ </td><td>Environment &amp; psychology &amp; keywords</td></tr><tr><td> $SE_{a_4}$ </td><td> $\{a_4, e_2, p_1, k_4, k_8, k_9, k_{10}\}$ </td><td> $\{a_4, \boldsymbol{e}_3, p_1, \boldsymbol{k}_6, k_8, k_{11}, \boldsymbol{k}_{12}, \boldsymbol{k}_{15}\}$ </td><td>Environment &amp; keywords</td></tr><tr><td> $SE_{a_5}$ </td><td> $\{a_5, e_2, p_1, k_1, k_9, k_{10}\}$ </td><td> $\{a_5, \boldsymbol{e}_3, \boldsymbol{p}_4, \boldsymbol{k}_8, k_9, \boldsymbol{k}_{12}, \boldsymbol{k}_{13}\}$ </td><td>Environment &amp; psychology &amp; keywords</td></tr><tr><td> $SE_{a_8}$ </td><td> $\{a_8, e_2, p_4, k_3, k_8, k_{10}\}$ </td><td> $\{a_8, e_2, \boldsymbol{p}_1, k_8, \boldsymbol{k}_9, \boldsymbol{k}_{14}\}$ </td><td>Psychology &amp; keywords</td></tr><tr><td> $SE_{a_9}$ </td><td> $\{a_9, e_2, p_2, k_4, k_6, k_8, k_{10}, k_{12}\}$ </td><td> $\{a_9, \boldsymbol{e}_3, \boldsymbol{p}_4, k_8, \boldsymbol{k}_{15}\}$ </td><td>Environment &amp; psychology &amp; keywords</td></tr><tr><td> $SE_{a_{16}}$ </td><td> $\{a_{16}, e_2, p_4, k_6, k_8, k_{10}\}$ </td><td> $\{a_{16}, e_2, \boldsymbol{p}_1, \boldsymbol{k}_1, k_6, k_8, \boldsymbol{k}_9, \boldsymbol{k}_{13}\}$ </td><td>Psychology &amp; keywords</td></tr><tr><td> $SE_{a_{17}}$ </td><td> $\{a_{17}, e_2, p_4, k_6, k_8, k_9, k_{10}\}$ </td><td> $\{a_{17}, e_2, \boldsymbol{p}_1, k_6, k_8, k_9, k_{10}\}$ </td><td>Psychology</td></tr><tr><td> $SE_{a_{22}}$ </td><td> $\{a_{22}, e_2, p_2, k_1, k_8, k_9, k_{11}, k_{12}\}$ </td><td> $\{a_{22}, \boldsymbol{e}_3, p_2, k_1, k_9, \boldsymbol{k}_{15}\}$ </td><td>Environment &amp; keywords</td></tr></table>

Note: The bold elements are the changed nodes in predicted superedges.

Please cite this article as: Y. Liu, et al., Superedge prediction: What opinions will be mined based on an opinion supernetwork model?, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.05.011

![](/api/attachments/PDW79DCB/fulltext/images/21a1007c1f023aa2f9e5dd2b2073e0c983a755148090718c29daedad7072344e.jpg)  
Fig. 8. “Jingwen Rumor Event” social subnetwork structural evolution (partial view).

Table 10  
Social subnetwork structure indices

<table><tr><td>Measurement index</td><td>Actual networkMay 3, 2013-May 8, 2013</td><td>Actual network + predicted linksMay 3, 2013-May 9, 2013</td></tr><tr><td>Node degree</td><td>2.045</td><td>2.500</td></tr><tr><td>Average shortest path length</td><td>2.678</td><td>2.623</td></tr><tr><td>Clustering coefficient</td><td>0.097</td><td>0.277</td></tr></table>

5.2. What relationships among agents in social subnetwork will be mined based on intralayer superedge prediction?

## 5.2.1. Predicted relationship evaluation

We applied the established supernetwork connection matrix H (May 3, 2013–May 7, 2013), social subnetwork adjacency matrix A (May 3, 2013–May 7, 2013), and evaluation matrix $\mathbf { \bar { \boldsymbol { E } } } ^ { P }$ (May 8, 2013) data to calculate the AUC evaluation (Table 6) of link prediction for the main agents of the “Jingwen Rumor Event”. We used MATLAB tools based on the aforementioned superedge similarity subnetwork intralayer superedge prediction evaluation. The AUC evaluation results indicate that the algorithm based on superedge similarity subnetwork intralayer superedge prediction can ensure more accurate prediction, with prediction accuracy up to 66.1%. This is 14.36% higher than single-layered link prediction accuracy based on common neighbors alone.

## 5.2.2. Relationship prediction

Based on data processing using MATLAB tools, we calculated the superedge similarity of the main agents in this public opinion event (May 3, 2013–May 8, 2013) namely, the similarity of environmental information e, psychological type p, and main opinion k. In a superedge formed with the participation of various agents, a link may be found that exists between two agents with relatively high superedge similarity. Based on the above results, we can predict which agents may have a link in the social subnetwork during the prediction day (May 9, 2013) of the evolution of this public opinion event. Table 7 displays the top ten pairs of agents. They are $a _ { 5 }$ and $a _ { 1 7 } , a _ { 3 }$ and $a _ { 1 6 } , a _ { 3 }$ and ${ a } _ { 4 } ,$ $a _ { 3 }$ and $a _ { 8 } ,$ a and $a _ { 1 6 } ,$ etc.

5.3. What opinion in predicted supernetwork will be mined based on interlayer superedge prediction?

## 5.3.1. Predicted opinion evaluation

Existing superedges in the established supernetwork model of this public opinion event are divided into two sets. The training set refers to the actual superedges during May 3, 2013–May 7, 2013. The test set refers to the predicted superedges for May 8, 2013 based on the algorithm. In Fig. $6 ,$ the basis for calculation of superedges corresponding to agent $\alpha _ { 3 }$ includes the most frequent environment, psychology, and keywords in the superedges of the neighbor agents $\alpha _ { 9 } , \alpha _ { 1 4 } , \alpha _ { 1 5 } , \alpha _ { 1 7 }$ $\alpha _ { 6 } , \alpha _ { 1 2 }$ and $\alpha _ { 5 } .$ Based on their one by one comparison, superedge prediction accuracy (SEPA) of this algorithm is 0.5966.

## 5.3.2. Opinion prediction

Superedges of this public opinion event during the period May 3, 2013–May 8, 2013 were predicted based on the supernetwork interlayer superedge prediction algorithm. Agents involved in the top eight agent nodes of edges newly formed in the social subnetwork on May 9, 2013 are $\alpha _ { 3 } , \alpha _ { 4 } , \alpha _ { 5 } , \alpha _ { 8 } , \alpha _ { 9 } ,$ etc. The superedge composition of the above agents was predicted through environment e, psychology $p ,$ and keyword k of the superedges formed through their neighbors. The newly formed superedges are $S E _ { a _ { 3 } } , S E _ { a _ { 4 } } , S E _ { a _ { 5 } } , S E _ { a _ { 8 } } , S E _ { a _ { 9 } }$ , etc. (Fig. 7, Table 8).

## 5.4. What opinion dynamics will be mined?

## 5.4.1. Opinion supernetwork dynamics

(1) Social subnetwork node superdegree increased: the actual supernetwork increased by 14.03%, this change was due to newly formed superedges in the social subnetwork determined by the 8 public opinion agents.

(2) Superedge–superedge distance decreased: the actual supernetwork decreased by 18.83%. The edges that were formed after the prediction mainly include the psychological subnetwork $p _ { 1 }$ and $p _ { 4 } ,$ , as well as the keyword subnetwork $k _ { 1 3 } \sim k _ { 1 5 }$ . When calculating the minimum distance between

![](/api/attachments/PDW79DCB/fulltext/images/2f66ad8fb282cd1b999fd27c813b971c3270a6ebb6cad9708d9e877a2a4b4eb3.jpg)  
Fig. 9. “Jingwen Rumor Event” environmental subnetwork evolution sketch.

Please cite this article as: Y. Liu, et al., Superedge prediction: What opinions will be mined based on an opinion supernetwork model?, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.05.011

![](/api/attachments/PDW79DCB/fulltext/images/fd2a70ebc7a0bccc6d7f17f742d9b3450756b78b54720100dfe76f0b12be1428.jpg)  
Actual supernetwork + Predicted superedges (2013.5.3-2013.5.9)

Fig. 10. “Jingwen Rumor Event” evolution of psychological subnetwork.

superedges, the larger the number of identical nodes that are commonly included in superedges, the more likely the distance between “hyper nodes” is to decrease [55], thus resulting in a decrease in the minimum distance between superedges.

(3) Superedge overlap increased: the actual supernetwork increased by 6.17%. This change was also due to newly added superedges, mainly determined by the psychological subnetwork nodes $p _ { 1 }$ and $p _ { 4 }$ and keyword subnetwork nodes $k _ { 1 3 } \sim$ $k _ { 1 5 }$ which included identical nodes. The more identical nodes included, the higher the superedge overlap will be (Table 9).

## 5.4.2. Social subnetwork dynamics

(1) The social subnetwork produced 10 subnetwork intralayer links, of which 4 links were connected to public opinion agent $\alpha _ { 3 } ,$ which thus covered 40% of the predicted intralayer superedges (Fig. 8).

(2) The network structure measurement indices show that the node degree and clustering coef<sup>fi</sup>cient increased, while the average shortest path length decreased, making the network structure more compact (Table 10).

## 5.4.3. Environmental subnetwork dynamics

After the “Of<sup>fi</sup>cial Weibo Rumor Rebuttal” of the “Jingwen Rumor Event” (e ) was published, this piece of positive information made its impact. After the prediction, mostly new superedges containing the rebuttal information $e _ { 3 }$ were formed, covering 62.5% of newly formed superedges. Major rebuttal information links were made with the psychological subnetwork nodes $p _ { 1 }$ and $p _ { 4 } ,$ , as well as keyword subnetwork nodes $k _ { 1 3 } \sim k _ { 1 5 } \ ( \mathrm { F i g . 9 } )$

## 5.4.4. Psychological subnetwork dynamics

(1) After the of<sup>fi</sup>cial rebuttal information $e _ { 3 }$ was published, the positive environmental information made its impact, and the ratio of the negative side negative mentality $( p _ { 2 }$ and $p _ { 3 } )$ public opinion agents decreased to some extent.

(2) Impacted by the information, the ratio of neutral mentality $\left( { { p } _ { 1 } } \right)$ public opinion agents increased to some extent. This change could be a result of the process of negative mentality $( p _ { 2 }$ and $p _ { 3 } )$ public opinion agents transforming into positive mentality $( p _ { 4 }$ and $p _ { 5 } )$ public opinion agents.

(3) Without a doubt, there is a direct relationship between the publishing of $e _ { 3 }$ information and the increase in the ratio of positive side positive mentality $( p _ { 4 }$ and p<sub>5</sub>) public opinion agents (Fig. 10).

## 5.4.5. Keyword subnetwork dynamics

(1) Impacted by positive environmental information, the proportion of buzzwords related to this event $\left( k _ { 1 } \sim k _ { 7 } \right)$ decreased to an extent. More of the viewpoints of public opinion agents after the information was published were transformed into positive side viewpoints of positive public opinion agents.

(2) The neutral viewpoint proportion increased. This could be due to more neutral viewpoints being published, or a result of the process of negative mentality $( p _ { 3 }$ and $p _ { 3 } )$ public opinion agents transforming into positive mentality $( p _ { 4 }$ and $p _ { 5 } )$ public opinion agents.

(3) The other two opposing viewpoints also changed. The proportion of negative viewpoints $\left( { { k } _ { 1 0 } } \sim { { k } _ { 1 2 } } \right)$ declined sharply (−19.48%). The proportion of positive viewpoints $\left( k _ { 1 3 } \sim k _ { 1 5 } \right)$ rose sharply (54.57%). This shows a direct relation between the evolution of the viewpoints and the publishing of the positive “Of<sup>fi</sup>cial Weibo Rumor Rebuttal” information (Fig. 11, Table 11).

## 6. Discussion

(1) This paper elaborated clearly on the formation and de<sup>fi</sup>nition of the public opinion supernetwork model and relevant data extraction. In future work, there are two areas which need improvement. (a) Model extension: currently, the public opinion supernetwork model uses a static four-layered network. In order to satisfy the different demands of researchers, and to attempt to

![](/api/attachments/PDW79DCB/fulltext/images/80b4c6a1eed3914367b56620025311e10c4099afcc8953ede02c663563a47130.jpg)  
Actual supernetwork + Predicted superedges(2013.5.3-2013.5.9)  
Fig. 11. “Jingwen Rumor Event” keyword subnetwork evolution.

Please cite this article as: Y. Liu, et al., Superedge prediction: What opinions will be mined based on an opinion supernetwork model?, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.05.011

Table 11  
“Jingwen Rumor Event” evolution of different attitude trends in viewpoints

<table><tr><td></td><td>Actual supernetwork (May 3, 2013-May 8, 2013)</td><td>Actual supernetwork + predicted superedges (May 3, 2013-May 9, 2013)</td><td>Degree of change</td></tr><tr><td>Event buzzwords</td><td>32.95%</td><td>29.75%</td><td>-9.71% ↓</td></tr><tr><td>Neutral viewpoint</td><td>26.14%</td><td>30.58%</td><td>16.99% ↑</td></tr><tr><td>Negative viewpoint</td><td>31.82%</td><td>25.62%</td><td>-19.48% ↓</td></tr><tr><td>Positive viewpoint</td><td>9.09%</td><td>14.05%</td><td>54.57% ↑</td></tr></table>

establish public opinion domain ontology, the goal of a dynamic adjusted model must be achieved. (b) Automatic extraction of psychological data: the psychological nodes constructed in this paper were obtained through 3 evaluators' manual labeling of linguistic data. This method is only suitable for situations that require a smaller scale of data. In order to enhance the maneuverability of large scale data, our research group is currently exploring the use of the NLPIR Chinese word segmentation system (also called ICTCLAS) to achieve word segmentation when users post messages, part-of-speech tagging, to combine it with Hownet emotion word sets in order to distinguish the users' psychological leanings automatically.

(2) This paper used a superedge similarity algorithm, introducing the super triangle in a hypergraph as a measurement of similarity, using super common neighbor indices to conduct superedge prediction, and achieving better prediction results. In future work, the Salton Index, Jaccard Index, and Hub Promoted Index of link prediction could be used as references for superedge prediction. With improvement, these could become new superedge prediction indices. Aimed at the speci<sup>fi</sup>c topological structure characteristics of supernetworks in different areas of application, they could produce even more brand new superedge prediction indices.

(3) This paper innovatively used a superedge prediction algorithm and applied it to a speci<sup>fi</sup>c actual public opinion supernetwork case. It made a thorough prediction and researched the evolutionary process of this speci<sup>fi</sup>c actual opinion supernetwork case. Further work would be to see the next instant of the supernetwork structure through superedge prediction. It could systematically, quantitatively and effectively propose guidance and intervention strategies for network public opinion. It could simulate the development trends of network public opinion. Furthermore, besides its application in network public opinion analysis, the superedge prediction algorithm could be used in areas such as the complex online “Friend Recommendation” of social network and “Product Recommendation” in the <sup>fi</sup>eld of online marketing. We will strive to come up with superedge prediction methods which have multiple applications, and can be used in even more areas of research.

## Acknowledgments

Thanks to the National Natural Science Foundation of China (NSFC) (91024010, 91324009), Innovative Research Team Program of Chinese Academy of Sciences (GH13041), Major Research Program of Institute of Policy and Management, Chinese Academy of Sciences (Y201201Z06) and the Youth Foundation of the Institute of Policy and Management, Chinese Academy of Sciences (Y200571Q01).

## References

[1] S.F. Wang, Public Opinion Theory and Practice, Li Ming Cultural Enterprise Co., Ltd Taiwan, 1995.

[2] W. Lippmann, Public Opinion, Simon & Schuster Inc., New York, 1997.

[3] A. Nagurney, J. Dong, Supernetworks: Decision-making for the Information Age, Edward Elgar Publishing, Cheltenham, 2002.

[4] Y.J. Liu, X.Y. Tang, Q.Q. Li, R.Y. Tian, N. Ma, Superlink prediction, Management Review 24 (12) (2012) 137–145.

[5] R.P. John French Jr., A formal theory of social power, Psychological Review 63 (3) (1956) (181–121).

[6] F. Harary, A criterion for unanimity in French's theory of social power, in: D. Cartwright (Ed.), Studies in Social Power, Inst. Soc. Res, Ann Arbor, MI, 1959, pp. 168–182.

[7] M.H. DeGroot, Reaching a consensus, Journal of the American Statistical Association 69 (345) (1974) 118–121.

[8] H. Haken, Synergetics, Springer, New York, 1977.

[9] C. Castellano, S. Fortunato, V. Loreto, Statistical physics of social dynamics, Reviews of Modern Physics 81 (2) (2009) 591.

[10] K. Sznajd-Weron, J. Sznajd, Opinion evolution in closed community, International Journal of Modern Physics C 11 (6) (2000) 1157–1165.

[11] S. Galam, Minority opinion spreading in random geometry, The European Physical Journal B-Condensed Matter and Complex Systems 25 (4) (2002) 403–406.

[12] J. Lyst, K. Kacperski, F. Schweitzer, Social impact models of opinion dynamics, Annual Reviews of Computational Physics 9 (2002) 253–273.

[13] G. Deffuant, D. Neau, F. Amblard, G. Weisbuch, Mixing beliefs among interacting agents, Advances in Complex Systems 3 (01n04) (2000) 87–98.

[14] R. Hegselmann, U. Krause, Opinion dynamics and bounded con<sup>fi</sup>dence models analysis, and simulation, Journal of Arti<sup>fi</sup>cial Societies and Social Simulation 5 (3) (2002).

[15] J.L. Jiang, How network public opinion formation and its effect, Journal of Beijing Institute of Technology (Social Sciences Edition) 8 (4) (2006) 10–14.

[16] C. Hu, R. Wu, A. Zhou, et al., Study on the formation models of network public opinion based on incline degrees of opinions of agents, Journal of Sichuan University (Engineering Science Edition) 41 (4) (2009) 196–201.

[17] C.Y. Liu, X.F. Hu, G.Y. Si, P. Luo, Public opinion propagation model based on small world networks, Journal of System Simulation 18 (12) (2006) 3608–3610.

[18] Q.Q. Li, Y.J. Liu, W.Y. Niu, J.F. Gu, Theory and application on the Internet opinion circulation based on “Three-Degree” method, Journal University of Shanghai for Science and Technology 33 (4) (2011) 337–344.

[19] F. Xiong, Y. Liu, X.M. Si, H. Cheng, Simulation of collective decision-making with incomplete information, Systems Engineering Theory & Practice 31 (1) (2011) 151–157.

[20] H. Wan, Z.H. Chen, A brief discussion on network consensus and its guidance, Journal of Yangzhou University (Humanities & Social Sciences) 11 (3) (2007) 91–94.

[21] Y.J. Liu, N. Ma, H.B. Wang, Study on the guidance of online public opinion for innovation social management, Bulletin of Chinese Academy of Science 27 (1) (2012) 9–16.

[22] X.F. Wang, H.S. Su, Recent progress in control of complex dynamical networks, Advances In Mechanics 38 (6) (2008) 751–756.

[23] Y.J. Liu, Q.Q. Li, R.Y. Tian, N. Ma, Formation and application of public opinion based on supernetwork analysis, Bulletin of Chinese Academy of Science 27 (5) (2012) 560–568.

[24] R.Y. Tian, Y.J. Liu, Intervention of public opinion and its application based on supernetwork analysis, Bulletin of Chinese Academy of Science 27 (5) (2012) 578–585.

[25] Q.Q. Li, Y.J. Liu, Dynamical model of public opinion and its application based on supernetwork, Bulletin of Chinese Academy of Science 27 (5) (2012) 569–577.

[27] Y. Sheffi, Urban Transportation Networks: Equilibrium Analysis With Mathematical Programming Methods. Prentice Hall, New Jersey, 1985

[28] A. Nagurney, Supernetworks: the science of complexity, Journal of University of Shanghai for Science and Technology 33 (2011) 205–228.

[29] Z.T. Wang, Z.P. Wang, Elementary study of supernetworks, Chinese Journal of Management 5 (1) (2008) 1–8.

[30] E. Estrada, J.A. Rodríguez-Velázquez, Subgraph centrality and clustering in complex hyper-networks, Physica A 364 (1) (2006) 581–594.

[31] C. Berge, Graphs and Hypergraphs, North-Holland, Amsterdam, 1973.

[32] X.M. Xu, Y.G. Sun, S. Yang, Hypergraph theory with applications, Acta Electronica Sinica 22 (8) (1994) 65–71.

[33] G. Ghoshal, V. Zlatić, G. Caldarelli, M.E.J. Newman, Random hypergraphs and their applications, Physical Review E 79 (6) (2009) 066118.

[34] H. Frank, J. Page, H.W. Myrna, et al., Networks and farsighted stability, Journal of Economics Theory 120 (2) (2005) 257–269.

[35] A. Nagurney, J. Dong, D. Zhang, A supply chain network equilibrium model, Transportation Research E 38 (5) (2002) 281–303.

[36] T. Wakolbinger, A. Nagurney, Dynamic supernetworks for the integration of social networks and supply chains with electronic commerce: modeling and analysis of buyer–seller relationships with computations, Netnomics: economic research and electronic networking 6 (2) (2004) 153–185.

[37] A. Nagurney, On the relationship between supply chain and transportation network equilibria: a supernetwork equivalence with computations, Transportation Research Part E 42 (4) (2006) 293–316.

[38] T. Yamada, K. Imai, T. Nakamura, et al., A supply chain-transport supernetwork equilibrium model with the behaviour of freight carriers, Transportation Research Part E: Logistics and Transportation Review 47 (6) (2011) 887–907

[39] P. Daniele, Variational inequalities for evolutionary <sup>fi</sup>nancial equilibrium, Innovations in Financial and Economic Networks (2003) 84–108.

[40] Z.P. Wang, S.B. Zhou, J.F. Guo, Z.T. Wang, Supernetwork model for resource allocation of network-advertisement based on variational ineguality. Journal of Dalian Maritime University 33 (4) (2007) 69–72.

[41] A. Nagurney, J. Dong, Management of knowledge intensive systems as supernetworks: modelling, analysis, computations, and applications, Mathematical and computer modelling 42 (3/4) (2005) 397–417.

Y. Liu et al. / Decision Support Systems xxx (2014) xxx–xxx

[42] R.J. Huang, Realization of directed fundamental cutset matrix by hypergraph theory, Journal of Electronics 14 (1) (1992) 50–60.

[43] E.V. Konstantinova, V.A. Skorobogatov, Application of hypergraph theory in chemistry, Discrete Mathematics 235 (1) (2001) 365–383.

[44] J.L. Segovia-Juarez, S. Colombano, D. Kirschner, Identifying DNA splice sites using hypernetworks with arti<sup>fi</sup>cial molecular evolution, Bio Systems 87 (2) (2007) 117–124.

[45] Z.T. Wang, Re<sup>fl</sup>ection on supernetwork, Journal University of Shanghai for Science and Technology 33 (3) (2011) 229–237.

[46] Y.C. Shang, H.S. Wang, Y.L. Wang, The supernetwork model of information transmission based on the microblog, Technology and Innovation Management 33 (2) (2012) 175–179.

[47] Y.J. Xi, Y.Z. Dang, The method to analyze the robustness of knowledge network based on the weighted supernetwork model and its application, Systems Engineering — Theory & Practice 27 (4) (2007) 134–140.

[48] Y.J. Xi, Y.Z. Dang, K.J. Liao, Knowledge supernetwork model and its application in organizational knowledge systems, Journal of Management Sciences in China 12 (3) (2009) 12–21.

[49] Y. Yu, Y.Z. Dang, J.N. Wu, Q.H. Deng, Supernetwork-based-analysis of knowledge diffusion trend, Journal of the Society for Scienti<sup>fi</sup>c and Technical Information 29 (2) (2010) 356–361.

[50] S.H. Xu, H. Zou, Analysis of dynamics of knowledge transfer based on supernetwork, Journal of Intelligence 30 (7) (2011) 94–98.

[51] J.N. Qiu, C.L. Nian, Y.S. Xu, Innovative super-network model and its application, Journal of Intelligence 30 (10) (2011) 139–145.

[52] F.L. Shi, Y.F. Zhu, Measuring the complexity of military communication network based on supernetwork theory, Journal on Communications 32 (12) (2011) 51–60.

[53] Y.F. Zhu, F.L. Shi, Y.L. Lei, A military communication supernetwork structure model in network-centric environment, Fire Control Command Control 37 (4) (2012) 9–13.

[54] V. Zlatić, G. Ghoshal, G. Caldarelli, Hypergraph topological quantities for tagged social network, Physical Review E 80 (3) (2009) 036–118.

[55] N. Ma, Y.J. Liu, SuperedgeRank algorithm and its application in identifying opinion leader of online public opinion supernetwork, Expert Systems with Applications 41 (4) (2014) 1357–1368.

[56] L. Getoor, C.P. Diehl, Link mining: a survey, ACM SIGKDD Explorations Newsletter 7 (2) (2005) 3–12.

[57] L.Y. Lv, Link prediction on complex networks, Journal of University of Electronic Science and Technology of China 39 (5) (2010) 651–661.

[58] L.Y. Lv, T. Zhou, Link prediction in complex networks: a survey, Physica A: Statistical Mechanics and its Applications 390 (6) (2011) 1150–1170.

[59] T. Zhou, L.Y. Lv, Y.C. Zhang, Predicting missing links via local information, The European Physical Journal B 71 (4) (2009) 623–630.

[60] E.A. Leicht, P. Holme, M.E.J. Newman, Vertex similarity in networks, Physical Review E 73 (2) (2006) 026120.

[61] L.Y. Lv, C.H. Jin, T. Zhou, Similarity index based on local paths for link prediction of complex networks, Physical Review E 80 (4) (2009) 046122.

[62] L. Katz, A new status index derived from sociometric analysis, Psychometrika 18 (1) (1953) 39–43.

[63] W. Liu, L.Y. Lv, Link prediction based on local random walk, Europhysics Letters 89 (5) (2010) 58007.

[64] X. Li, H. Chen, Recommendation as link prediction in bipartite graphs: a graph kernel-based machine learning approach, Decision Support Systems 54 (2013) 880-890.

[65] R. Kumar, J. Novak, A. Tomkins, Structure and evolution of online social networks, Proceedings of the ACM SIGKDD, 2006, pp. 611–617.

[66] A. Clauset, C. Moore, M.E.J. Newman, Hierarchical structure and the prediction of missing links in networks, Nature 453 (7191) (2008) 98–101

[67] R. Guimerà, M. Sales-Pardo, Missing and spurious interactions and the reconstruction of complex networks, Proceedings of the National Academy of Sciences 106 (52) (2009) 22073–22078.

[68] L. Lv, T. Zhou, Link prediction in weighted networks: the role of weak ties, Europhysics Letters 89 (1) (2010) 18001.

[69] J. Leskovec, D. Huttenlocher, J. Kleinberg, Predicting positive and negative links in online social networks, Proceedings of the 19th International Conference On, World Wide Web, 2010, pp. 641–650.

[70] T. Murata, S. Moriyasu, Link prediction of social networks based on weighted proximity measures, IEEE/WIC/ACM International Conference on Web Intelligence, 2007, pp. 85–88.

[71] R. Likert, A technique for the measurement of attitudes, Archives of Psychology 140 (1932) 1–55.

[72] J.A. Hanley, B.J. Mcneil, The meaning and use of the area under a receiver operating characteristic (ROC) curve, Radiology 143 (1) (1982) 29–36.

![](/api/attachments/PDW79DCB/fulltext/images/d20594aa024db6e73193ed939c6836d3350cb71a9706f21d64ef29f9d0de2251.jpg)

![](/api/attachments/PDW79DCB/fulltext/images/d1d21cf4e315cfa181a501f61006dbd078a1a5657220126f403de27f15c87f23.jpg)

![](/api/attachments/PDW79DCB/fulltext/images/a335cb1bf0b9d700188eebfdf8dee9fb8b32e580dea282081228339f1e080c52.jpg)

![](/api/attachments/PDW79DCB/fulltext/images/10f0c9281ab1425bb8ee2174f57f327eada8e6176f5afce36daede7bd9559590.jpg)

Yijun Liu is an associate research fellow of Institute of Policy and Management of Chinese Academy of Sciences. Her research includes opinion dynamics, complex network and sustainable development strategies.

Qianqian Li is an assistant research fellow of the Institute of Policy and Management of Chinese Academy of Sciences. She got her Ph.D. in Management of Science and Engineering from the Institute of Policy and Management of the Chinese Academy of Sciences, and her research interests include opinion dynamics and complex network.

Xianyi Tang is a visiting fellow of the Intercross-Science Research Centre for Natural Science and Social Science, CAS His research includes social physics, opinion dynamics and philosophy of science.

Ning Ma is a Ph.D. candidate in the Institute of Policy and Management of the Chinese Academy of Sciences and Graduate University of the Chinese Academy of Sciences. Her research focuses on complex network and opinion dynamics.

![](/api/attachments/PDW79DCB/fulltext/images/413502931c8f706260fb4318f2c56e16e189a5b72e9c37570e74f486343dde44.jpg)

Ruya Tian is a Ph.D. candidate in the Institute of Policy and Management of the Chinese Academy of Sciences and Graduate University of the Chinese Academy of Sciences. Her research focuses on opinion dynamics and complex network.
