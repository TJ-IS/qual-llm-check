---
otero_id: 13484
otero_key: "NJYNE7BC"
title: "Website browsing aid: A navigation graph-based recommendation system"
authors: "Youwei Wang; Weihui Dai; Yufei Yuan"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.05.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Website browsing aid: A navigation graph-based recommendation system

Youwei Wang <sup>a,⁎</sup>, Weihui Dai <sup>a</sup>, Yufei Yuan

School of Management, Fudan University, Shanghai, China

<sup>b</sup> DeGroote School of Business, McMaster University, Canada

Available online 18 May 2007

## Abstract

Websites nowadays are an important and popular source of publicly available information. However, due to their exploding scale and complexity, overcoming information overload to find relevant information is a major challenge. In addition to website maps and search engines, self-adaptive websites or websites with intelligent navigation aid are very useful tools in addressing this issue. In this paper, a navigation graph-based recommendation system is proposed, in which the navigation patterns of previous website visitors are utilized to provide recommendations for newcomers. The performance of the proposed recommendation algorithm is tested using the data collected from a real world website. Experimental results reveal that the proposed system can yield satisfactory recommendations, especially to the visitors in their early navigation steps. © 2007 Elsevier B.V. All rights reserved.

Keywords: Website navigation aid; Recommendation system; Access log; Graph theory

## 1. Introduction

Nowadays, websites are a popular and convenient source of all kinds of information. According to research conducted by UCLA in 2004, 55.2% of American households considered the Internet to be a very important or extremely important source of information [21]. With more and more information put on the websites, the scale and complexity of modern websites are growing rapidly. Although it appears that customers can enjoy a plethora of product choices with detailed information on large websites, it is often difficult if not impossible to find information relevant to the interests of individual users when confronted by the huge amount of possible viewing paths.

Visitors often get lost in the maze of hyper-space, and fail to locate the required information [5]. Most websites today do not provide navigation guides tailored to individual user needs. As a result, too much time is spent searching for relevant information on websites. To address the issues of information overload and information irrelevance, there is a demand for intelligent tools to make website navigation easier without diminishing the quality and completeness of the experience [18].

A sitemap seems to be the most commonly used solution to address the dual issues of too much information and excess quantities of irrelevant data. The map briefly outlines the information structure of the site to help visitors narrow down the scope of their search. After entering into certain sub-directories, visitors can find more detailed information to lead them to their targets. However, by their very nature, sitemaps generally cover only the main structures of the site, which often is not thorough enough to guide subsequent navigation. Personalized sitemaps, which can potentially be helpful to individual visitor's navigation, have also been proposed to address this issue [34].

Search engines, the popular tools for locating web pages, are the second solution to overcoming information overload. Large websites often provide in-site searching tools on their root page. By retrieving the keywords input in the web browsers, a list of URLs that are related to customers' current interests can be supplied to access directly. Besides in-site searching functions, there are also many public search engines available, e.g. Yahoo!, Google, AltaVista, Excite, Alltheweb, etc. Depending on the techniques employed, search engines can be classified into hierarchical search engines, agentbased search engines, meta search engines etc. [26]. Public search engines focus on general searching services for global users but can also be tailored to in-site searching purposes. For example, Google offers a free SiteSearch service to all educational institutions and notfor-profit organizations. All eligible websites, as long as they are publicly available on the Internet, can add one mini search toolbar on their sites, which enable users to search information within their domain. Despite their popular and powerful services, both in-site and independent search engines are vulnerable to problems such as irrelevant or incomplete information [16].

The third solution to information overload and irrelevance can be broadly termed “intelligent navigation aid tools.” These can be classified further into recommendation systems and adaptive website techniques. Recommendation systems can provide personalized recommendations as output or guides the user to interesting objects within a large number of options in a highly individualized fashion [28]. Collaborative filtering is probably the most widely implemented and most matured recommendation technique [7]. Other recommendation systems, such as content-based recommenders, utility-based recommenders, knowledgebased recommenders, and demographic recommenders, have also been well studied [4,15,29,35]. Recommendation systems are good at processing large amounts of online information. However, recommendation systems require varying degrees of user involvement. They occasionally failed to offer high quality of services under different application contexts. See reference [7] for the pros and cons of the different recommendation techniques.

Another stream of research on the quest for intelligent website navigation focuses on adaptive websites. The word “adaptive” refers to “the ability of the website or tool to change its behavior based on the way it is used” [30]. Compared to recommendation systems mentioned above, adaptive websites demand little or no explicit user participation and thus may be termed as “tacit recommendation”, which can potentially minimize any interference or interruption to the visitor. In recent years, with the parallel development of graph metrics [12], tacit recommendation systems have become a distinct field of research.

There are two different approaches to the construction of adaptive websites: improving the website design as a whole or providing personalized navigation aid for individual visitors. While the former approach usually works by rearranging regularly the whole site, the latter provides personalized suggestions to each site visitor in real time. For example, Spiliopoulou and Pohle [32] developed a web usage miner WUM that can provide concrete suggestions on how the site should be improved. Fang and Liu Sheng defined the problem of hypertext selection — selecting from a large set of hyperlinks to be included in the home page [13]. In the recent study, the authors also develop a series of studies on adaptive websites [37,41], which analyzed the website's link structure as well as user behavior, then systematically re-adjusted the website link structure by using operations research algorithms.

In recent years, many online navigation aid methods have been proposed. Letizia [22] is a client-side agent that predicts the next pages to be visited by observing the visitor's past browsing actions (e.g. the kind of links followed, the pages bookmarked, etc.). One obvious limitation of client-side navigation aid is that it can not leverage group knowledge of other visitors since it knows about actions of only one visitor. In contrast, server side approaches make use of information from all the visitors and thus can potentially yield better recommendation results. Cooley et al. [11] has proposed several log data preprocessing techniques, based on a method of dividing user sessions into semantically meaningful transactions. These identified transactions can then be used for association rule mining and navigation recommendation. In reference [10], two algorithms were proposed to find frequent traversal patterns. Borges and Levene [6] model access log data as a weighted graph where the weights represent the probabilities a user interact with the website. Then, association rules are developed to extract navigation patterns from the graphs. Website visitors can intuitively be divided into sub-groups, with each group having similar interests or browsing behaviors. If the composition of those groups can be determined in advance by algorithms such as clustering, each active browser can potentially benefit from the knowledge of similar interest groups. Yan et al. [39] proposed a simple algorithm, the leader algorithm, for user session clustering (with each session represented as a vector). Kukulenz and Pauli [19] regard navigation decisions as graphs with the nodes being the requested data objects and the edges being the decisions. A method is presented to learn the distribution of such graphs based on distances between graphs. PageGather is an adaptive website system, which recommends pages based on co-occurrence of page requests in past sessions [27]. Mobasher et al. [24] proposed an offline–online system architecture to recommend automatically web pages for each active visitor. Also there are online navigation aid systems that implemented prediction models. In reference [31], a self-organizing map (one type of artificial neural network) was proposed to organize web pages into a twodimensional map based on the user's navigation behavior. The resulting map can then provide navigation aid to active web browsers. Anderson et al. [1] proposed the MinPath algorithm, which automatically recommends shortcut links with maximal expected savings on the fly to aid mobile Internet navigation.

The research in this paper shares some traits with the literature summarized above. We want to develop an online navigation aid using collaborative recommendation based on graph theory. Our approach differs from others in the following aspects. First, to provide a better online navigation guide, we leverage the group knowledge of similar visitors using the approach borrowed from collaborative filtering. Clustering techniques will be used to extract user groups from the access sequences left behind by visitors. This approach is better than using the knowledge of only one's own navigation history appointed by [22]. Second, we take into account not only the nodes visited but also the access sequence to provide better recommendations. To do so, navigation sequence information is coded into directional graphs as opposed to vectors which were used in prior research [24,39]. The reason is that the future behaviors of one visitor can be predicted more precisely by considering those people who took similar routes over those who visited similar group of pages. Third, we used the classical measurements of recall and precision borrowed from document retrieval literature to evaluate the performance of our navigation aid system. These measurements are different from heuristic performance indicators such as contact efficiency or conversion efficiency [32] of web pages, and expected savings [1] after adding shortcut links. The objective of our research is to develop a website browsing guide system that can make online recommendations based on group knowledge derived from similar visitors.

The remainder of this paper is organized as follows: Section 2 describes the proposed recommendation technology, which includes the metrics for measuring graph distances and recommendation algorithms; Section 3 describes the experiment design, test results, and their implications. Finally, the paper concludes with a summary and the future research directions.

## 2. Navigation graph-based recommendation systems

Website visitors usually browse web pages for quite different reasons and under a variety of contexts. In this sense, visitors are quite distinct from each other. However, they do exhibit many similar interests within certain groups of users. When browsing the same websites with similar objectives, members of the same group demonstrate similar behavior. Thus, if the group membership can be identified by some techniques, successful recommendation can be made by referencing the behavior of members within the same community. In the website browsing environment, valuable information for distinguishing different user groups is buried in the log files, where traces of users are recorded. Therefore, mining the groupings of the navigation paths seems to be a valid approach to building a navigation recommendation system.

## 2.1. Website navigation graphs

When visitors browse websites, detailed information about their website access including their IP addresses, the URL addresses of the requested pages, as well as the time when the request was processed are saved in log files. Such information may be helpful in discovering a user's interest. A website visit can be represented by a website navigation graph in which the pages visited are noted as nodes, and the hyperlink clicks are interpreted as navigation paths. Since some visitors may have similar preferences and searching patterns, their navigation graphs are likely to be similar. Therefore, a small community phenomenon may exist in the website navigation graphs. In each community, members are expected to have similar website browsing habits. If one user is identified as belonging to a certain community, that individual is expected to visit similar web pages. The notion of community forms the foundation of our navigation graph-based recommendation system. This same principle has been used in classic recommendation techniques such as collaborative filtering where people with similar ratings on items are supposed to have similar shopping interests [3,17]. The difference between collaborative filtering and the recommendation system proposed in this paper lies in the fact that while the former can be applied in a variety of application environments, the latter is devised specifically for website navigation guide purposes.

A popular website often accumulates millions, even billions, of navigation records each day. Graph theory can be used to analyze these navigation records. As a starting point, some notions need to be defined in advance.

Definition 1. A graph can be defined as a 2-tuple $g =$ $_ { ( \nu , e ) }$ , where v is a set of finite vertices and $e \subseteq \nu \times \nu$ a set of edges. We denote the number of nodes in g as |g|.

Definition 2. Given a graph $g { = } ( \nu , e )$ , a sub-graph of g is a graph $g ^ { \prime } { = } ( \nu ^ { \prime } , e ^ { \prime } )$ such that 1) $\nu ^ { \prime } \subseteq \nu , 2 ) e ^ { \prime } { = } e ^ { \prime } \cap ( \nu ^ { \prime } \times \nu ^ { \prime } )$

The notation of $g ^ { \prime } \subseteq g \mathrm { i s }$ used to indicate that $g '$ is a sub-graph of $g .$

Definition 3. Let g, g1 and $g 2$ to be graphs, g is a common sub-graph of $_ { g 1 }$ and $g 2 { \mathrm { ~ i f ~ } } g \subseteq g 1$ and $g \subseteq g 2$

The notation of $g \subseteq c s ( g 1 , g 2 ) \mathrm { i }$ is used to indicate that $g$ is a common sub-graph of $_ { g 1 }$ and $g 2$ later.

Definition 4. A common sub-graph g of g1 and $g 2$ is maximal if there exists no other common sub-graph $\mathbf { g } '$ of $_ { g 1 }$ and $g 2$ that has more nodes than g.

The notation of $g \subseteq m c s ( g 1 , g 2 )$ is used to indicate that $g$ is a maximal common sub-graph of $_ { g 1 }$ and $g 2$ later. Please note that the maximal common sub-graph of $_ { g 1 }$ and $g 2$ is not necessarily unique. However, the number of nodes of $m c s ( g 1 , g 2 )$ is fixed.

Using the definitions above, each website navigation session can be represented by a navigation graph. The set of navigation sessions in the website log can be readily presented by a graph set $G = \{ g 1 , g 2 , \ldots \}$ , with each navigation graph $_ { g i }$ being the sub-graph of the website link structure graph. In the next section, the distance between navigation graphs will be discussed.

## 2.2. Graph distance metrics

Bunke and Messmer [8] surveyed the measures of graph distances. There are many methods developed to measure the graph distance, including spectral measures, error correcting graph matching, graph edit distance, maximal common sub-graph distance and its variants, etc. However, not all these distance measures are readily interpreted as metrics. For any distance $d ( \cdot , \cdot )$ to be metric, the following three properties are required:

For any graphs $g 1 , g 2$ and $g 3$ ,

1) $0 \leq d ( g 1 , g 2 ) \leq 1 $

2) $d ( g 1 , g 2 ) = d ( g 2 , g 1 ) .$

3) $d ( g 1 , g 2 ) \leq d ( g 1 , g 2 ) + d ( g 2 , g 3 ) .$

To measure the distance among graphs, the metric requirement is very important, especially for distancebased clustering techniques introduced in the following sections. Of all the graph distance measures known, maximal common sub-graph distance and graph distance using graph union have proven to be metrics [36]. Generally, the distance metrics based on maximum common sub-graph has the form of

$$
d (g 1, g 2) = 1 - \frac {m (g 1 , g 2)}{M (g 1 , g 2)}
$$

where $m ( g 1 , g 2 )$ is a measure of similarity between g1 and $g 2$ and $M ( g 1 , g 2 )$ is a measure of the size of the set $\{ g 1 , g 2 \}$

In this paper, we adopt the maximal common subgraph distance using union as metric. According to the definition of this metric, $m ( g 1 , g 2 ) = \lvert m c s ( g 1 , g 2 ) \rvert$ and M $( g 1 , g 2 ) = \lvert g 1 \rvert + \lvert g 2 \rvert - \lvert m c s ( g 1 , g 2 ) \rvert$ . Hence, the maximal common sub-graph using union can be formally defined as:

$$
d (g 1, g 2) = 1 - \frac {| m c s (g 1 , g 2) |}{| g 1 | + | g 2 | - | m c s (g 1 , g 2) |}\tag{1}
$$

For instances, for two graphs g1 and $g 2 , \mathrm { i f } | g 1 | = | g 2 | =$ 5 and |mc $\scriptstyle ( g 1 , g 2 ) = 2$ , the distance between them will be $d ( g 1 , g 2 ) = 0 . 7 5 .$

According to reference [9], there are algorithms available whose worst case time complexity of deciding the maximal common sub-graph is $O ( 2 ^ { n } )$ , where n denote the number of nodes of the graphs under consideration. Thus for n that is less than 10, real time behavior can be expected in implementation.

Under special circumstances of $| g 1 | = | g 2 | ,$ , Eq. (1) can further be simplified to $\begin{array} { r } { d ( g 1 , g 2 ) = 1 - \frac { m } { 2 n - m } , } \end{array}$ where $n { = } | g 1 | { = } | g 2 |$ and $m { = } | m c s ( g 1 , g 2 ) |$ <sup>Þ ¼ - -</sup>. It is obvious that $d ( g 1 , g 2 )$ reaches the maximum of 1 when $m { = } 0$ and the minimum of 0 when $m = n$

## 2.3. Navigation graph simplification

In previous sections, general graph distance metric was introduced. But in our current application environments, user navigation graphs have some unique properties compared to general graphs. First, each navigation graph is composed of a series of nodes, which are visited in sequence by certain website browsers. Each navigation graph begins with one entrance node and ends with one exit node. The entrance node and exit node are possibly identical. Since the nodes in the navigation graph appear in order, we have a chance to “lineate” the graph to a visiting sequence. In fact, that is just what we did in this paper. By treating a navigation graph as a sequence (a special case of a graph), the effort of calculating graph distance can be greatly reduced. More important, the visiting sequence information, especially nodes that are visited in the latter parts of the sequence, are valuable for predicting future visiting nodes of newcomers.

Second, circles may exist in the navigation graph if a visitor revisits some nodes, either by using existing links or by utilizing the “go back” button on the browser tools. This often happens in Web environments, especially when visitors recall that some important information showed up on previously visited pages. One option for processing circles is to use the original sequence literally. Another option is to ignore such revisits by sifting out repeated nodes. The choice should be related to the objectives of the particular application. In our case, for example, the navigation graphs are used for recommending relevant pages for newcomers to the website. Thus, retrospective behaviors are meaningless in our looking forward application environment. Certainly, under special application environments such as finding web pages in a website whose location is different from where visitors expect to find them, the point from where visitors backtrack includes valuable information [33].

Based on the above discussion, the original navigation graph can be simplified into a navigation sequence, in which repeated nodes are eliminated. Fig. 1 depicts the results of simplification from original navigation graph (a) to sequence (b). Please note that since the resulting sequence is one directional, the arrows can also be omitted for succinctness. In subsequent sections, we will use interchangeably the term graph and sequence since they are now identical concept. Correspondingly, the resulting graph in Fig. 1-(b) can be readily denoted by $g = \{ 1 , 2 , 4 , 5 , 3 , 6 , 7 \}$

Using Eq. (1), the similarity between any two website navigation graphs (or sequences) can be measured by the distance metric. And according to the hypothesis in Section 2.1, the smaller the distance between graph pairs, the more similar the two corresponding visitors. Moreover, the possible nodes to be visited for one certain user can be estimated by the similar navigation graphs of the earlier users. We will illustrate this recommendation process in the following case.

For example, we have three complete navigation sequence g1, g2, g3 and one incomplete navigation sequence g4 where $g 1 = \{ 1 , 4 , 3 , 5 \} , g 2 = \{ 2 , 3 , 6 , 1 \} , g 3 =$ $\{ 3 , 6 , 4 , 2 , 1 \}$ and $\mathrm { g } 4 = \{ 2 , 3 , 6 \}$ . The task now is to recommend nodes to g4 for further browsing. Since only 3 steps are known for the fourth user, the first 3 nodes visited by the other 3 users should be used accordingly for computing graph distance. Here we have $d ( g 4 , g 1 | _ { 3 } ) = 1 . 0 $ $d ( g 4 , g 2 | _ { 3 } ) = 0$ and $d ( g 4 , g 3 | _ { 3 } ) = 0 . 5 .$ where $g i | _ { 3 }$ denotes the sub-sequence generated by the first 3 nodes of corresponding complete navigation sequences. It is obvious that $g 2$ is closest to g4. Therefore, we may expect user 4 to visit the same nodes as user 2, in this case, node 1.

## 2.4. Proposed recommendation system

To make a navigation recommendation, we collect previous visitors' navigation graphs and cluster them into several sets based on their similarities. For a new visitor, we will find the nearest cluster based on the steps that the visitor has gone through and make recommendations with the most popular pages visited before by this cluster. The detailed procedures are highlighted in Fig. 2.

## 2.4.1. Offline clustering

The offline part of the system analyzes user access log files to form clusters of user sequences and thus to prepare for navigation support in the online part. It includes three steps.

First, huge amounts of log data should be preprocessed into a preferred format, in our case, the navigation sequences. Besides, visiting sequence extraction is needed since requests by different users are mixed and sorted by time in the log files. Very long and very short navigation sequences may be found after this first processing. The very short sequences, e.g. those with only one or two nodes, can be readily interpreted as guest visitors who had dropped in and left very quickly. On the other hand, very long navigation sequences may be the result of a proxy server, which represents lots of browsers' behaviors. Information about such visits is futile or purely noise and should be eliminated from the recommendation system. After the log parsing and transforming work, the website navigation sequences of all users should be saved into separate text files or databases for further processing.

![](/api/attachments/NJYNE7BC/fulltext/images/a82adfcd2fbfc0f27ff8c5b63eedd4e619a47ab51272ce76eab531b1a50d8758.jpg)

![](/api/attachments/NJYNE7BC/fulltext/images/c0dfadc2924c4ba050ef66a7d2459a14b8020cc9714d36c2e78655bd982b422c.jpg)  
Fig. 1. An example of navigation graph simplification: (a) original navigation graph (dotted lines); (b) navigation sequence after simplification

![](/api/attachments/NJYNE7BC/fulltext/images/a7f9cc5d550024fe152f2c63fbb0488629202ddcf0cacb6d586752d7c15f8000.jpg)  
Fig. 2. Recommendation algorithm scheme.

In the second step, we classify navigation sequences into sub-groups based on their sizes. We denote G as the set of all navigation sequences and $G _ { i }$ as the set of the navigation sequences with a size greater than or equal to i. The remaining work in this step is very straightforward. That is calculating the distances according to Eq. (1) for each pair of sequences in each sequence set.

In the third step, we split the sequences in each sequence set by a clustering algorithm. There are many specific algorithms available for clustering, each has its pros and cons. For offline clustering as in this paper, the efficiency of the clustering algorithms can be less of a consideration provided that the data sets are not too large. Therefore, we adopted the hierarchical agglomerative methods for navigation graph clustering. Besides simplicity, another virtue of these algorithms is that they are readily available in many large scale statistical software packages, such as SPSS, SAS, etc.

Hierarchical agglomerative clustering (HAC) methods start with each sequence in a cluster of its own, iterate by merging the two closest clusters at each step, and terminate when some halting criterion is reached [16]. All kinds of HAC algorithm designs differ in three key aspects: (1) the distance function between sequences, (2) the inter-cluster measures, and (3) the halting criterion. We use formula (1) in Section 2.2 to measure the distance function between sequences. There are many ways to define the distance between two clusters (i.e. sets of sequences). The commonly used inter-cluster measures are single-link (minimum sequence distance between the two clusters), complete-link (the maximum distance), group-average (the average distance), Ward, etc. Ward is an inter-cluster similarity measure that enables the clustering procedure seeking to form the clusters in a manner that minimizes the “information loss” associated with each grouping, and to quantify that loss in a form that is readily interpretable. Thus, Ward was selected as the inter-cluster measure for offline clustering. Interested readers are encouraged to refer to literature [38] for details of Ward measure. HAC usually employs a fixed cluster number as the halting criteria. But the correct number of clusters for stopping criteria is often data dependent. Pilot tests will be carried out in the experiment section to select the right number of clusters.

After clustering, the medoid of each cluster can easily be determined by comparing the average distances between one center sequence and all remaining sequences. The one with the minimal average distance will become the medoid of the cluster, which can be viewed as the representative of the cluster it is in. To describe the algorithm symbolically, we introduce the following notations:

s The minimal size of navigation sequences.

S The maximal size of navigation sequences.

G The sequence set parsed from the log files.

G<sub>j</sub> The sub-set of G with the size of each sequence member equals to or larger than j.

c The predetermined number of clusters generated by the clustering algorithm.

$$
\begin{array}{l l} C _ {j, k} & \text { A   cluster   of   graphs   in } G _ {j}. \\ c _ {j, k} & \text { The   medoid   of   cluster } C _ {j, k}. \end{array}
$$

The detailed algorithm of the offline part is described as follows:

## Algorithm for offline clustering

Input: Website log files.

Output: A set of sequence clusters $\{ C j , k \}$ and corresponding medoids $\left\{ c j , k \right\}$

Step 1. In the website's user access log file, convert each user's navigation path to a graph and then simplify it into a navigation sequence. Remove sequences with length shorter than s or longer than S and denote the sequence set as $G = \left\{ g _ { \ l } \vert s \leq \vert g _ { \ l } \vert \leq S \right\}$

Step 2. Allocate navigation sequences into a series of sequence set $G _ { j } ( j \in [ s , S ] )$ where $G j = \left\{ g i \mid \begin{array} { l }  { \left| g i \right| \geq j \} } \end{array} \right.$ Compute the distance between each couple of sequences within each sequence set $G j .$

Step 3. Clustering sequences in each set $G j$ and output clusters $C _ { j , k } ( k \in [ 1 , c ] )$ . Determine the medoid $c j , k$ for each cluster $C j , k$

In summary, in the offline part, the recommendation system produces a series of sequence sets. Each sequence set is further decomposed by clustering algorithms. Finally, in each cluster gotten, one representative sequence (or medoid) is prepared for further online processing.

## 2.4.2. Online recommendation

The objective of this sub-system is to generate recommendations for an active website visitor in realtime. This online part of the recommendation system also has three steps.

The first step is to decide the most similar community for the active website user. Assuming that the current visitor $g$ has already visited j steps, where $j { = } | g |$ . We therefore should search the sequence set $G _ { j }$ in order to find a nearest cluster to g. We have already determined the clusters $C _ { j , k }$ in the sequence set $G _ { j }$ in the offline part. Since medoids are good candidates for representing clusters they are in, the distance between each medoid $c _ { j , k }$ and the current active sequence $g$ is a good indicator. So the cluster with the minimal distance of its medoid to the current visitor should be nominated as the most similar cluster. There may be several clusters equally close to g. To break the tie, the size of the clusters should be considered. Eq. (2) below takes the cluster size into consideration:

$$
p _ {j, k} = d (g, c _ {j, k} | _ {j}) \cdot \frac {1}{1 + | C _ {j , k} | / | G _ {j} |}\tag{2}
$$

where, $| C _ { j , k } |$ denotes the size of cluster $C _ { j , k } , | G _ { j } |$ is the number of graphs in graph set $G _ { j }$ and $c _ { j , k } \big | _ { j }$ is the truncated sequence formed by the first j nodes of sequence $c _ { j , k } .$ . By Eq. (2), the cluster that is nearest to $g$ with largest cluster size will be elected as the nearest cluster assigned to $g .$ . The idea of breaking a tie for clusters equally close to the active sequence originated from reference [19]. But what we used here are truncated sequences instead of original visiting sequences.

The second step is to remove some navigation sequences that are too far away from the current user g in the candidate navigation sequence cluster. Specifically, the sequence $g _ { j , k , l }$ in cluster $C _ { j , k }$ with the distance $d ( g , g _ { j , k , l } | _ { j } ) >$ $d _ { \mathrm { m i n } }$ will be sifted out of the candidate sequence set, where $d _ { \mathrm { m i n } }$ is the predetermined distance threshold. The output of this step will be the candidate navigation graph set $C _ { j , k } ^ { \phantom { \dagger } } ^ { \phantom { \dagger } }$ that is near to the current active website visitor. Please note that the large distance $d ( g , g _ { j , k , l } | _ { j } )$ does not necessarily mean the dissimilarity of g and $g _ { j , k , l } ,$ because $g _ { j , k , l } | _ { j }$ is the preceding parts of $g _ { j , k , l }$ and it is possible that some later parts of $g _ { j , k , l }$ resemble $g .$ Thus, some similar sequences to the current visitor g may be sifted out of the candidate set. Here we assume that enough train data is available, as is often the case for web sites that have collected months sometimes even years of log data. Under this assumption, some similar access sequences can be identified for each active visitor and our algorithm can still yield good recommendations. However, under special circumstance where there is minimal log data available, for example, newly launched websites, more complex algorithms that take into account more session segments would be more appropriate.

The third step is to select candidate nodes for recommendation. Any candidate node must pass two rounds of filtering. First, it should appear in the latter part of the candidate navigation sequences beyond the steps that the current visitor has taken. Those selected nodes should not appear in the visiting history of the current active visitor. Second, each candidate node should be visited with enough access frequency. All candidate nodes will be sorted according to their access frequency. The nodes with larger access frequencies will be selected for recommendation. Exactly how many nodes can pass through all these examinations is determined by the maximal number of nodes that can be recommended. This number, which is referred as “the number of recommendations” in the experiments in the next section, is a parameter that can be set up by considering particular system performance requirements. Generally, the larger the number of recommendations, the smaller the access frequency threshold to be used. The formal algorithm for online recommendation is as follows:

Notations. $\left[ G _ { j } \right] _ { j } ^ { + }$ : the set of nodes that are located beyond the jth position of the sequences in $G _ { j } .$ (Here, $G _ { j }$ is a sequence set with the size of each element equals to or larger than j.)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:
g: an active website navigation sequence.
m: the maximal number of nodes for recommendation.
 $d_{min}$ : the minimal distance threshold.
Output:
A set of nodes as recommendation for the current visitor.
Step 1. Allocate the active sequence g to the sequence set  $G_{j}$ , where  $j = |g|$ . Assign g to the cluster  $C_{j,k}$  with the greatest possibility according to Eq. (2).
Step 2. Generate candidate sequence set  $C_{j,k}'$  from cluster  $C_{j,k}$  by excluding any sequence with distance  $d(g, g_{j,k,l}|_{j}) \geq d_{\min}$ , where  $g_{j,k,l} \in C_{j,k,l}$ .
Step 3. Sort the nodes in  $[C_{j,k'}]_{j}^{+} - g$  in descending order according to their access frequency. Recommend at most m nodes with higher access frequency.
</div>

The online recommendation system screens candidate nodes for navigation aid purposes. To be qualified as candidate nodes, they must pass three stages of careful examination. The selected nodes will appear in a separated area of the web browsing tools. Customers then have many more optional links to choose from on each web page. If they find any of the recommended URLs inviting, they can jump directly to those web pages with one click.

## 3. Experiments

## 3.1. Experiment data

In this section, we evaluate the effectiveness of the recommendation system using navigation data from a real world website: Music Machines (http://machines. hyperreal.org). This website was constructed by professors at Washington University and is used mainly for experimental purposes. The website lists all kinds of musical instruments including drums, music synthesizers, accordions, pianos, etc. All the information about the musical instruments including images, music samples, brief introductions, etc., is catalogued by manufacturer and the instrument type. More than two years of web log data (from February 1997 to April 1999 comprising 14,722,468 access records) as well as the original webpage files are available for downloading for free. This small scale, well structured website is perfectly suited for our experiments.

We conducted a series of experiments using the log data from January 1st 1999 to January 31st 1999 listing the log records of the more than 40,000 visitors who accessed the website during those 31 days. In our experiments, we used the log data from 24 consecutive days for training purposes and the data from the subsequent 25th day for testing. The experiments were carried out in a rolling manner. In the first experiment, the training set included log data from January 1st to 24th and the corresponding test set consisted of the January 25th data. The subsequent experiment absorbs one new day's data (i.e. the test data in the previous experiment) into the training set while culling the first day's data. Correspondingly, the test set was moved forward to the following day. In short, the experiments adopted a time window of 25 days which was repeated 7 times. Throughout the experiments, offline clustering was applied to the training set. Then using the online recommendation algorithm, we predicted the web nodes that users would select. Finally, we compared the actual navigation behavior of users in the test set with the recommendations to evaluate the performance of our proposed recommendation system.

## 3.2. Data pre-processing

We adopted the IBM VisualAge for JAVA as the coding platform and the SAS 8.0 software package for clustering analysis. To analyze the link structure of the website, we wrote a JAVA program to automatically open each web page and parse the link structure of the website's files. On the Music Machine website, a total of 916 pages and 7630 links were identified. For ease of processing, a unique identification number was created to represent each web page identified. The mapping relationship and link structure of the site was then used to parse the access log file into navigation sequences.

The result of parsing the log file revealed that 65% of the visitors only browsed one or two pages and then left. It seemed that they were in a hurry and impatient. We categorized such visitors as guests and they were not the focus of our experiments. About 34% of the browsers read 3 to 20 pages. These were the target customers of our recommendation system. The frequency distribution of the number of pages visited is shown in Fig. 3. And last, less than 1% of web visitors read more than 20 pages. Among this group, a substantial number of the visitors browsed 200 or more pages. Such visitors, due to this unusual pattern, could be readily interpreted as visitors behind certain proxy servers. This group was also not the focus of our experiments.

![](/api/attachments/NJYNE7BC/fulltext/images/d092f7f079ff1a00f69f1939fe41ea7c72d1f19b4df70acc3585f9b66f8af125.jpg)  
Fig. 3. Ratio of visitors browsing 3 to 20 web pages.

## 3.3. Performance indicators and clustering parameter settings

The objective of this experiment is to test how well the proposed recommendation system could make predictions. Therefore, certain indicators needed to be defined in advance to evaluate the performance of the system. The indicators used in our experiments were precision and recall, two well accepted performance indicators in the information retrieval field [2]. To illustrate these two indicators, suppose that the set of documents returned by a certain query system is {Retrieved} and the set of relevant documents is {Relevant}. The documents that are not only relevant but also retrieved is {Relevant} ∩ {Retrieved}. Then, precision is defined as the percentage of retrieved documents that are relevant to the query. Formally,

$$
p r e c i s i o n = \frac {\left| \left\{R e l e v a n t \right\} \cap \left\{R e t r i e v e d \right\} \right|}{\left| \left\{R e t r i e v e d \right\} \right|}.
$$

Recall is defined as the percentage of documents that are relevant to the query and were, in fact, retrieved. It is formally defined as:

$$
\text { recall } = \frac {\left| \left\{\text { Relevant } \right\} \cap \left\{\text { Retrieved } \right\} \right|}{\left| \left\{\text { Relevant } \right\} \right|}.
$$

For example, if a particularly active visitor on Music Machine website browsed several pages and the system recommended five other web pages for browsing, of which two pages appeared in the actual visiting history, then the precision of this recommendation is 2/5 or 40%. If the relevant page number of the current user was in fact three, then the recall of this recommendation would be 2/3 or 67%.

Although the above definitions are clear, it is not easy to determine exactly how many pages are relevant to a current user. Website visitors may browse many unrelated pages during their navigation process. We assume that website visitors can eventually locate the pages that they are interested in and those web pages are likely to appear in the later parts of the navigation sequences. With this assumption, we used the last three nodes as the relevant pages of the visitors. If a visitor visited less than three more pages before leaving the website, we assumed that all the subsequent pages were relevant. The size of the relevant page set, therefore, varies between 1 and 3.

We selected the hierarchical agglomerative clustering algorithm with Ward's minimum-variance method [23] for clustering. This algorithm merges clusters iteratively until some predetermined number of clusters has been reached. There are some improved versions such as BIRCH and CURE [14,40], which surpass the original hierarchical agglomerative clustering algorithm in scalability or flexibility [16]. But in this paper we adopted the original hierarchical agglomerative clustering algorithm because it met our requirement of offline clustering. Ward was selected over other inter-cluster similarity measures (e.g. single-link, complete-link and groupaverage-link) because it can potentially yield better clustering outcomes (at the expense of more computing efforts). For hierarchical clustering, the cluster number threshold is a predetermined parameter that determines the output of the algorithm. Therefore, before the main study, we did a pilot test to decide the proper number of clusters. For this pre-test, we selected the first group of experimental data (from January 1st to 25th). We then set up 9 groups of parameter settings with different user steps (5, 7 and 10) and prediction numbers (5, 10 and 20). The performance indicators of precision and recall were then compared using different numbers of clusters ranging from 30 to 100 in increments of 10. This pilot test revealed that while the optimal cluster numbers (in terms of good precision and recall) differ depending on different parameter combinations, the number of clusters ranging from 40 to 70 proved robust enough to be the halting criterion. Therefore, we used the unified cluster number of 50 in the subsequent experiments.

![](/api/attachments/NJYNE7BC/fulltext/images/9e1806b128f62c88750449316c928da8906354418d0370e1f0316fe6f745837f.jpg)

(b)  
![](/api/attachments/NJYNE7BC/fulltext/images/a1065cb856c8e57cd42114d3de5db8b55a70ddc17741007973035d369f6df648.jpg)  
Fig. 4. Recalls under different parameter settings: (a) prediction number from 1 to 10; (b) prediction number from 10 to 100.

In our experiments, the distance threshold $d _ { \mathrm { m i n } }$ is set to 1.0 for any candidate sequence to be used for recommendation. Therefore only sequences which are totally dissimilar to the current active sequence would be excluded from the candidate sequence set. This setting is based on observations made during the experiments that the experiences of most past visitors (provided they behaved like the current visitor to some extent) are helpful in improving the recall rates of the algorithm, especially when the number of recommendations is set large.

## 3.4. Experiment results

The proposed system can be designed to provide recommendations for visitors at various steps of browsing. For example, one daemon procedure may be triggered as soon as a visitor opens any page on the website. However, since little information is acquired about the new visitor with such few steps, poor system performance results. Hence, our system will not make recommendations until the visitor has taken at least three steps. The system can also be designed to recommend varying numbers of web pages. Intuitively, it might seem that the more recommendations there are, the higher the recall (at the expense of low precision). We carried out experiments to investigate the performance of the proposed recommendation system when providing different numbers of recommendations at different user steps. The results are shown in Figs. 4 and 5.

As indicated in Fig. 4-(a), with the maximal number of recommendations increasing from 1 to 10, the recalls also increase. When only one web page is recommended, the recall is at its lowest, with a value of about 5%. If a maximum of 10 pages is recommended, the recalls fluctuate between 17% and 30%, depending on the user step at which a particular recommendation is made. When more recommendations are provided, as illustrated in Fig. 4-(b), the recall increases with the prediction number growing larger. When a total of 30 recommendations are provided, the recall fluctuates in a range between 30% and 46%. The largest recall of 66% occurred when 100 recommendations were supplied to the website visitor. Since we have assumed for testing purposes that only the last three pages are relevant pages for each visitor, a recall rate of 33% means that there is at least one relevant page being recommended, while a recall rate of 66% means that there are at least two relevant pages being recommended.

(a)  
![](/api/attachments/NJYNE7BC/fulltext/images/76fd79437059164abbfd5009dcf871b7ffb885ea6eb5512924f022fce1af79de.jpg)

![](/api/attachments/NJYNE7BC/fulltext/images/9a4f64f049294000f6fe61c0d2c25a9e9a205ce6a68bd1e6c4ffe8c3b73dd17c.jpg)  
Fig. 5. Precisions under different parameter settings: (a) prediction number from 1 to 10; (b) prediction number from 10 to 100.

Table 1  
![](/api/attachments/NJYNE7BC/fulltext/images/ac67079b7fdc8360f6bdb589cd28b7fa5e66c5cacb584b3e03a5261a010601e3.jpg)  
Fig. 6. Average recalls for various user steps.

Fig. 5 shows the precision of the recommendation under different parameter settings. When more recommendations are made, the precision declines. However, our recommendation precision seems very low from less than 12% to only 1%. This phenomenon is not unusual since the number of relevant pages is at most three in our experimental settings. Therefore, according to our definitions, the maximum precision for a given number of recommendations R is less than 3/R. For example, if we make 10 recommendations the maximum precision is 30%. This differs from other recommendation systems or document retrieval systems where recall and precision can approach 100%. Based on the data, it is clear that the precision is higher with a lower number of recommendations.

Another important observation in Figs. 4 and 5 is that recommendation recall and precision is higher for users in their early steps. The recall rate is highest for visitors in their third step. This phenomenon is very important. It means that we can make useful recommendations without the need to wait longer and collect more information from the user. It is also more useful from the user's perspective. It is better to receive good recommendations as early as possible in order to avoid unnecessary browsing.

We did a second experiment to further probe the relationship between user steps and system performance. The results are shown in Fig. 6. Basically, three lines representing recall under different numbers of recommendations shift slightly downward within 12 steps. One may wonder the reason for this drop. When the number of steps increases, the number of visitors decreases quickly. In our experiments, the number of visitors taking more than 10 steps accounted for only about 5% of the customer base, about 300 or fewer within the current experiments. Thus the quickly decreasing scale of knowledge base may account for the poor system performance. Besides, the number of possible navigation graph increases exponentially with the number of steps increasing, which may also attribute to this phenomenon. On the other hand, some visitors are prone to change their visiting objectives, a phenomenon known as interest drifting [20], as was observed in the access log of the Music Machine website. For this type of visitors, it is essential to devise more advanced algorithms and to keep track of their volatile interests in order to provide useful recommendations [20].

![](/api/attachments/NJYNE7BC/fulltext/images/c22bf3438c163e2be9acc0220aaef2c58d8d324dd5fae6f9b73a5c7a225ebd3a.jpg)  
Fig. 7. Average precisions for various user steps.

Despite the deteriorating trends of recalls, the precision of the system drops only slightly (see Fig. 7). This is an important result in that it verifies a stable system performance on precision for various user steps. Based on this finding, we can further conclude that the numbers of recommendations (not user steps) are the main factors leading to low precision.

Based on the findings above, we concluded that the best chance for the proposed system to provide recommendations comes at the early stages of browsing, especially in a customer's first 3 to 5 steps. At this stage, our system can recommend pages with the largest recall rate and the highest precision. This property of the system is very important for at least two reasons. First, most of the website visitors are impatient and in a hurry, as shown by the shrinking percentage of visitors as the number of steps increases (see Fig. 3). Thus, the earlier the website provides recommendations, the more the customers are absorbed and thus prolongs the length of time spent on the website. Retaining customers is the objective of most information publication websites and our system serves this objective. Second, less experienced visitors compared to more experienced users tend to rely more on navigation tools [25]. After extensive browsing, visitors will become accustomed to the website both in terms of information content and link structure. Thus, their need for navigation guides decreases. The proposed recommendation system, with its feature of best performance at the initial stage of a visitor's browsing experience, becomes especially useful for the unskilled and unfamiliar visitor.

Statistics on recalls over a 7 day period

<table><tr><td>Prediction number</td><td colspan="2">5</td><td colspan="2">10</td><td colspan="2">20</td></tr><tr><td>User steps</td><td>Average (%)</td><td>SD</td><td>Average (%)</td><td>SD</td><td>Average (%)</td><td>SD</td></tr><tr><td>3</td><td>33.4</td><td>0.9</td><td>45.2</td><td>0.9</td><td>56.6</td><td>1.3</td></tr><tr><td>5</td><td>27.5</td><td>1.9</td><td>34.8</td><td>2.5</td><td>44.7</td><td>3.0</td></tr><tr><td>7</td><td>25.0</td><td>2.2</td><td>32.1</td><td>2.4</td><td>41.4</td><td>3.5</td></tr><tr><td>10</td><td>21.8</td><td>5.7</td><td>29.9</td><td>6.9</td><td>39.8</td><td>5.0</td></tr></table>

Table 2  
Statistics on precisions over a 7 day period

<table><tr><td>Prediction number</td><td colspan="2">5</td><td colspan="2">10</td><td colspan="2">20</td></tr><tr><td>User steps</td><td>Average (%)</td><td>SD</td><td>Average (%)</td><td>SD</td><td>Average (%)</td><td>SD</td></tr><tr><td>3</td><td>7.8</td><td>0.4</td><td>5.6</td><td>0.1</td><td>3.9</td><td>0.1</td></tr><tr><td>5</td><td>6.6</td><td>0.3</td><td>4.5</td><td>0.3</td><td>3.2</td><td>0.3</td></tr><tr><td>7</td><td>6.6</td><td>0.7</td><td>4.5</td><td>0.4</td><td>3.2</td><td>0.3</td></tr><tr><td>10</td><td>5.7</td><td>1.2</td><td>4.1</td><td>0.9</td><td>2.9</td><td>0.5</td></tr></table>

We ran the experiment over consecutive 7 day periods using the time window technique described in Section 3.1. The results are summarized in Tables 1 and 2. Based on this data, appropriate parameters can therefore be selected with expected performance. It is clear that offering a small number of recommendations at the early steps of a user's navigation is the most effective system setting.

## 4. Conclusions and future directions

This paper proposed a website navigation aid system based on navigation graph clustering. The separated offline and online system architecture design makes it quite efficient in terms of memory space and computation efforts. Our recommendation system requires only the website link structure and log files, which are available for most websites. Hence, most of the websites today are able to implement the techniques proposed in this paper. We also demonstrated that the recommendation system reaches a reasonable performance level in terms of recall and precision. It is also effective in making recommendations with a small number of pages at the early stages of user navigation thus significantly reducing information overload when browsing a complex website. Despite the virtues of this system, there are some issues that need to be addressed by future research.

First, in Section 3.3, we assumed that the last few web pages are potentially the most interesting pages for visitors. Two performance indicators of recall and precision were then proposed for subsequent experimental study. This assumption is intuitively reasonable. But further experimental study is necessary to validate this. One possible approach is to explicitly query visitors as to what their favorite web pages are just before they leave the website. The recommendation system can then utilize the visitors' feedback to make more precise predictions.

Second, in the offline part of our recommendation algorithms, we conducted clustering analysis using the hierarchical agglomerative clustering (HAC) method, in which Ward was adopted as the inter-cluster measure. In circumstances when efficiency is not the key determinant, HAC with Ward can readily yield acceptable clustering results, as our experiments indicated. However, when the proposed algorithms are implemented in large-scale websites with huge amounts of log data to be analyzed, scalability problem may arise. On the other hand, the effectiveness and flexibility of HAC in the presence of outliers is obviously inferior to other algorithms such as BIRCH and CURE [14,40]. Hence, other clustering algorithms with different inter-cluster measures (such as single-link, complete-link, groupaverage-link, etc.) need to be explored in future studies for comparison with our experimental results.

Finally, our recommendation system did not take into account the content of web pages. However, if domain knowledge of a website is included in our system, it is possible to provide better recommendations for the more knowledgeable visitors. A combination of classic knowledge-based and utility-based recommendation methods and techniques with our methods may prove to have enormous potential. For example, navigation graph-based recommendations can be carried out at the early stages to fully utilize the proposed algorithm's advantages. As customers probe into details of the site, more information about their interests will be collected. Such information can serve as inputs for knowledgebased systems which function best when lot of data is available. The particular combination methods and the performance of the combined system are thus promising research directions to pursue.

Our research can be used to develop a website system that can automatically recommend web page URLs in real time. Such a system can save website visitors' time, lead to better information service and improve customer loyalty. With better understanding and prediction of users' navigation behavior, it is also possible for webmasters to systematically improve the website's hyperlink structure.

## Acknowledgements

The authors are grateful for the comments and suggestions from the editors and anonymous reviewers. They would like to thank professor Mike Perkowitz and professor Oren Etzioni from the University of Washington for sharing Web log data and the original Music Machine site files.

This research is partially supported by the National Nature Science Foundation of China (under grant 70401010), the China Scholarship Council, and the Natural Sciences and Engineering Research Council of Canada.

## References

[1] C. Anderson, P. Domingos, D. Weld, Adaptive Web Navigation for Wireless Devices, Proceedings of the 17th Joint Conference on Artificial Intelligence, Seattle, WA, 2001, pp. 879–884.

[2] R. Baeza-Yates, B. Ribeiro-Neto, Mordern Information Retrieval, Addison–Wesley, 1999.

[3] M. Balabanovic, Y. Shoham, Fab: content-based, collaborative recommendation, Communications of the ACM 40 (3) (1997) 66–72.

[4] N.J. Belkin, W.B. Croft, Information filtering and information retrieval: two sides of the same coin? Communications of the ACM 35 (12) (1992) 29–38.

[5] H. Berghel, Cyberspace 2000: dealing with information overload, Communications of the ACM 40 (2) (1997) 19–24.

[6] J. Borges, M. Levene, Mining association rules in hypertext databases, Proc. of the fourth International Conference on Knowledge Discovery and Data Mining, New York, USA, 1998, pp. 149–153.

[7] R. Burke, Hybrid recommender systems: survey and experiments, User Modeling and User-Adapted Interaction 12 (4) (2002) 331–370.

[8] H. Bunke, B. Messmer, Recent advances in graph matching, International Journal of Pattern Recognition and Artificial Intelligence 11 (1) (1997) 169–203.

[9] H. Bunke, K. Shearer, A graph distance metric based on maximal common subgraph, Pattern Recognition Letters 19 (3–4) (1998) 255–259.

[10] M.S. Chen, J.S. Park, P.S. Yu, Data mining for path traversal patterns in a Web environment, Proc. 16th IEEE International Conference on Distributed Computing Systems, 1996, pp. 385–392.

[11] R. Cooley, B. Mobasher, J. Srivastava, Data preparation for mining World Wide Web browsing patterns, Knowledge and Information Systems 1 (1) (1999) 5–32.

[12] D. Dhyani, W.K. Ng, S.S. Bhowmick, A survey of web metrics, ACM Computing Surveys 34 (4) (2002) 469–503.

[13] X. Fang, O.R. Liu Sheng, LinkSelector: a web mining approach to hyperlink selection for web portals, ACM Transactions on Internet Technology 4 (2) (2004) 209–237.

[14] S. Guha, R. Rastogi, K. Shim, CURE: an efficient clustering algorithm for large databases, Proc. 1998 ACM-SIGMOD Int. Conf. Management of Data (SIGMOD'98), Seattle, WA, ACM Press, New York, USA, June 1998, pp. 73–84.

[15] R.H. Guttman, A.G. Moukas, P. Maes, Agent-mediated electronic commerce: a survey, Knowledge Engineering Review 13 (2) (1998) 147–159.

[16] J.W. Han, M. Kamber, Data Mining: Concepts and Techniques, Morgan Kaufmann Publishers, 2001.

[17] J.L. Herlocker, J.A. Konstan, A. Borchers, J. Riedl, An Algorithmic Framework for Performing Collaborative Filtering, Proceedings of the 22nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Berkeley, CA, 1999, pp. 230–237.

[18] M. Kilfoil, A. Ghorbani, W. Xing, Z. Lei, J. Lu, J. Zhang, X. Xu, Toward an adaptive web: the state of the art and science, Communication Networks and Services Research (CNSR) 2003 Conference, New Brunswick, CA, 2003, pp. 108–119, 130.

[19] D. Kukulenz, J. Pauli, Prediction of navigation profiles in a distributed Internet environment through learning of graph distributions, International Journal of Computational Intelligence and Applications, vol. 2 (3), Imperial College Press, 2002, pp. 303–312.

[20] W. Lam, J. Mostafa, Modeling user interest shift using a Bayesian approach, Journal of the American Society for Information Science and Technology 52 (5) (2001) 416–429.

[21] H. Lebo, The Digital Future Report: Surveying the Digital Future, Year Four, University of Southern California, http:// www.digitalcenter.org/downloads/DigitalFutureReport-Year4- 2004.pdf. Sep. 2004.

[22] H. Lieberman, Letizia: an agent that assists web browsing, Proc. 14th Intl. joint Conf. on Artificial Intelligence, 1995.

[23] P. Mangiameli, S.K. Chen, D. West, A comparison of SOM neural network and hierarchical clustering methods, European Journal of Operational Research 93 (1996) 402–417.

[24] B. Mobasher, R. Cooley, J. Srivastava, Automatic personalization based on web usage, Communications of the ACM 43 (8) (2001) 142–151.

[25] H. Nysveen, P.E. Pedersen, An exploratory study of customers' perception of company web sites offering various interactive applications: moderating effects of customers' Internet experience, Decision Support Systems 37 (2004) 137–150.

[26] A. Perkins, White paper: The classification of search engine spam, http://www.silverdisc.co.uk/articles/spam-classification Sept. 2001.

[27] M. Perkowitz, Adaptive Web Sites: Cluster Mining and Conceptual Clustering for Index Page Synthesis. PhD Thesis, Dept. of Comp. Sci. and Eng., Univ. of Washington, 2001.

[28] P. Resnick, H.R. Varian, Recommender Systems, Communications of the ACM 40 (3) (1997) 56–58.

[29] E. Rich, User modeling via stereotypes, Cognitive Science 3 (1979) 329–354.

[30] J.B. Schafer, J. Konstan, J. Riedl, Recommender Systems in e-Commerce, EC '99: Proceedings of the First ACM Conference on Electronic Commerce, Denver, CO, 1999, pp. 158–166.

[31] K.A. Smith, A. Ng, Web page clustering using a self-organizing map of user navigation patterns, Decision Support Systems 35 (2003) 245–256.

[32] M. Spiliopoulou, C. Pohle, Data mining to measure and improve the success of web sites, Data Mining and Knowledge Discovery 5 (1–2) (2001) 85–114.

[33] R. Srikant, Y. Yang, Mining Web Logs to Improve Web Site Organization, Proc. of World Wide Web (WWW01), 2001, pp. 430–437.

[34] F. Toolan, N. Kushmetick, Mining Web Logs for Personalized Site Maps, The Third International Conference on Web Information Systems Engineering Workshops (WISEw'02) Singapore, 2002, pp. 232–237.

[35] B. Towle, C. Quinn, Knowledge based recommender systems using explicit user models, Knowledge-Based Electronic Markets, Papers

from the AAAI Workshop, AAAI Technical Report WS-00-04, AAAI Press, Menlo Park, CA, 2000, pp. 74–77.

[36] W.D. Wallis, P. Shoubridge, M. Kraetz, D. Ray, Graph distances using graph union, Pattern Recognition Letters 22 (6–7) (2001) 701–704.

[37] Y.W. Wang, D.W. Wang, W.H. Ip, Optimal design of link structure for e-supermarket website, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 36 (2) (2006) 338–355.

[38] J.H. Ward, Hierarchical grouping to optimize an objective function, Journal of American Statistical Association 58 (301) (1963) 236–244.

[39] T. Yan, M. Jacobsen, H. Garcia-Molina, U. Dayal, From User Access Patterns to Dynamic Hypertext Linking, Proceedings of the 5th International World Wide Web Conference, Paris, France, May 1996.

[40] T. Zhang, R. Ramakrishnan, M. Livny, BIRCH: an efficient data clustering method for very large databases, Proc. 1996 ACM-SIGMOD Int. Conf. Management of Data (SIGMOD'96), Montreal, Canada, ACM Press, New York, USA, June 1996, pp. 103–114.

[41] Y. Zhou, Y.W. Wang, Y.Y. Zhang, W.H. Dai, Hyperlink Structure-based Recommender System, The Eighth Pacific-Asia Conference on Information Systems (PACIS2004), 8–11 July 2004, Shanghai, China, http://www.pacis-net.org/.

![](/api/attachments/NJYNE7BC/fulltext/images/64536ca20eb181ea4209167e15ee44155f078ebefd9eb5cd8de0cce7da4a01ef.jpg)

Youwei Wang earned both his MS and PhD degrees in Systems Engineering from Northeastern University, Shenyang, China, in 2000 and 2003, respectively. He has served as a Postdoctoral Fellow at McMaster University, Canada. He has worked as a visiting professor at Richard Ivey School of Business, The University of Western Ontario, Canada. At present, he is an Associate Professor of the Department of Information Management and Information Systems,

School of Management, Fudan University, China. He has published two books and more than 20 papers in professional journals and conferences such as IEEE Transactions on Systems, Man and Cybernetics, Telecommunications Policy, International Conference on Information Systems (ICIS), etc. His research interests include modeling and optimization of online shopping systems, mobile commerce, Decision Support Systems, etc. E-mail: ywwang@fudan edu.cr E-mail: ywwang@fudan.edu.cn

![](/api/attachments/NJYNE7BC/fulltext/images/78a70304030551bbfe9732d0e549ac97d85e36a43280e9fc9f4d305a04204748.jpg)

Weihui Dai received his BS degree in Automation Engineering in 1987, his MS degree in Automobile Electronics in 1992, and his PhD in Biomedical Engineering in 1996, all from Zhejiang University, China. He is currently an Associate Professor at the Department of Information Management and Information Systems, School of Management, Fudan University, China. He has published more than 30 journals and conference articles in the area of Intelligent

Decision Support Systems, Net-ecology, e-Business, etc. Dr. Dai is a member of IEEE and AIS. E-mail: whdai@fudan.edu.cn

![](/api/attachments/NJYNE7BC/fulltext/images/2d9325e1ea4944fa128c906ac5aa31711dcfb93abd76ac00cff5d3ae569f2863.jpg)

Yufei Yuan received his PhD in Computer Information Systems from the University of Michigan in the U.S. and his B.S. in Mathematics from Fudan University in China. He is the Wayne C. Fox Chair in Business Innovation and a professor of Information Systems at Michael G. DeGroote School of Business, McMaster University, Canada. His research interests are in the areas of mobile commerce, web-based negotiation support system, business model of electro-

nic commerce, approximate reasoning with fuzzy logic, matching problems, and decision support in health care. He has published more than 50 papers in professional journals such as Communications of the ACM, International Journal of Electronic Markets, Internet research, International Journal of Mobile Communication, Fuzzy Sets and Systems, European Journal of Operational Research, Management Sciences, Decision Sciences, Academic Medicine, Medical Decision Making, International Journal of Human-Computer Systems, Human Systems Management, IEEE Security and Privacy, Journal of Information & management and others. His name is listed in Who's Who in Canada.

E-mail: yuanyuf@mcmaster.ca
