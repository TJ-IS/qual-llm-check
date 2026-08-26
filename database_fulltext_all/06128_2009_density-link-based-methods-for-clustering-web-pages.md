---
otero_id: 6128
otero_key: "CY8WX2GZ"
title: "Density link-based methods for clustering web pages"
authors: "Morteza Haghir Chehreghani; Hassan Abolhassani; Mostafa Haghir Chehreghani"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.04.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Density link-based methods for clustering web pages

Morteza Haghir Chehreghani ⁎, Hassan Abolhassani, Mostafa Haghir Chehreghani

Web Intelligence Laboratory, Department of Computer Engineering, Sharif University of Technology, Tehran, Iran

## a r t i c l e i n f o

Article history: Received 13 February 2008 Received in revised form 22 February 2009 Accepted 2 April 2009 Available online 8 April 2009

Keywords: Web clustering Density based clustering Hyperlink structure Hierarchical clustering

## a b s t r a c t

World Wide Web is a huge information space, making it a valuable resource for decision making. However, it should be effectively managed for such a purpose. One important management technique is clustering the web data. In this paper, we propose some developments in clustering methods to achieve higher qualities. At <sup>fi</sup>rst we study a new density based method adapted for hierarchical clustering of web documents. Then utilizing the hyperlink structure of web, we propose a new method that incorporates density concepts with web graph. These algorithms have the preference of low complexity and as experimental results reveal, the resultant clusters have high quality.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction and primary concepts

Clustering is an important task that can be used for improving the search engines, enhancing the web crawling operations etc. Clustering the search results provides a more meaningful view for the requested information. On the other hand (hierarchical) clustering provides a structure in which a user can <sup>fi</sup>nd his desired information via drill down into the structure and consider the position of the information inside the hierarchy. This view may be useful in several situations such as making a decision [3,25]. Clustering also can facilitate focused crawling in which the web pages with speci<sup>fi</sup>c topics are navigated and crawled.

While the web information is very useful for supporting decision making [2,6,15], the information explosion on the web makes it hard to obtain required knowledge. One way for organizing the information is to cluster web contents. The goal of clustering is to create groups of data items in an unsupervised fashion so that items in the same cluster are similar to each other yet dissimilar to data items in other clusters. Effective web clustering facilitates relevant document retrieval that itself facilitates decision making [3]. When web data is used for knowledge extraction and decision making, a user normally <sup>fi</sup>nds himself in a huge information with no organization or structure. One good way to make such organization is to cluster the data in related groups of documents. High quality clustering, therefore, assists users to access relevant information much conveniently.

A number of clustering algorithms are presented in the literature [13], such as K-Means [17], hierarchical clustering [20], graph partitioning [28] and spectral clustering [11], density based [9], grid based, model based etc. So far, only methods such as agglomerative hierarchical clustering (AHC), K-Means and some graph partitioning methods had more popularity and usage for web data clustering.

AHC combines the smaller data groups for creating bigger ones. It starts with each web page in a single cluster and iteratively merges two most similar ones iteratively until a halting criterion is reached. According to the measure used for merging (i.e. nearest, farthest and average distance), AHC methods are divided into [8]: single linkage, complete linkage and average linkage. The halting criterion in AHC is based on a predetermined constant [18]. Because of the sensitivity of AHC to the halting criterion, the algorithm may mistakenly merge two clusters.

The most well known partitioning algorithm is K-Means [17] which in the simple form selects K data points as cluster centers and assigns each data point to the nearest one. The reassigning process is continued until a convergence criterion is met. The advantage of this algorithm is that it can be performed with O(n) time complexity. For web page clustering, some of the previous works have adapted K-Means and AHC algorithms [19,23,26,27].

Web documents contain textual information as well as hyperlinks between them. There have been many efforts to use one or both of them to make clusters. In this paper we introduce methods for using both content and link information on top of density based algorithms.

Density based methods are an important category of data clustering methods developed so far only for structured data such as relational data bases. These methods have the advantages of creating clusters in various shapes (with high accuracy) and removing the noisy data. In these algorithms at <sup>fi</sup>rst a random data item is selected and its neighborhood is investigated to determine whether it has an acceptable number of data points (as a dense unit). If it does not satisfy the condition, the point is labeled as noise. Otherwise, according to various criteria, the next data item is examined. Finding the remaining dense units is followed until clustering process is completed. According to the expansion criteria, different density based methods are developed including: DBSCAN [9], OPTICS [1], and DBRS [22].

DBSCAN was the <sup>fi</sup>rst density based algorithm, in which to create a new cluster or expand an existing one, a neighborhood distance with radius Eps must contain at least a minimum number of points denoted by MinPts. It uses data structures such as R⁎-tree and SR-tree to <sup>fi</sup>nd the neighborhood distance of a point with log n time complexity, and therefore the total time complexity becomes O (n log n) [9]. DBSCAN examines the neighborhood of each clustered data point to see whether it can be added to the cluster. This process is iterated until all points in the data set have been placed in some clusters or labeled as noise. In this manner for a data set containing n points, n region queries are required.

Although DBSCAN shows very good results, it also has some shortcomings: First, if a data set has clusters with widely varying densities, DBSCAN is not able to handle them ef<sup>fi</sup>ciently. Since all neighbors are checked, much time may be spent in dense areas for examining the neighborhoods of all points.

To overcome this problem, OPTICS [1] has been introduced. It starts with a random point and if its neighborhood is dense, orders its neighbors and therefore applies a kind of priority on the development of the expansible points. By <sup>fi</sup>nding new dense neighborhoods, the points existing inside them are also sorted with previously ordered points and then for the next expansion, one point with the minimum distance is selected. Anyway, OPTICS doesn't solve the problem completely. In fact, it considers no difference between regions with high and low densities; while it may be necessary to have in some region clusters with high density and in some other regions, clusters with low density.

Also, DBSCAN is not suitable for <sup>fi</sup>nding approximate clusters in very large data sets. Since DBSCAN creates and completes a cluster fully and then starts another cluster, if we stop the clustering process early, we cannot have a suitable approximate for other clusters. DBRS [22] tries to solve this problem. It iteratively picks an un-clustered point randomly and if its neighborhood is sparsely populated, considers it as noise. Otherwise, if some points of the neighborhood belong to a previously created cluster(s) all of its points join to that cluster(s). Otherwise, a new cluster is created. Here, the next point is selected from un-clustered points and therefore DBRS <sup>fi</sup>nds several clusters simultaneously. However DBRS does not obviate the problem completely. Its samples are created fumblingly so that they may not be suitable representatives for the clusters.

Additionally one thing that is not dealt with enough until now is the use of these algorithms for clustering the web data. We need to apply some improvements on these algorithms to be suitable for the web environment. What we propose here is using web hyperlink structure to <sup>fi</sup>nd the dense units and also improve the joining process for creating hierarchical clusters.

The remaining parts of the paper are organized as follows. Section 2 provides a survey of related works. In Section 3 we explain our density based method. Section 4 includes detailed explanations of the linkbased density method and its analysis. The experimental results and their evaluations are shown in Section 5 and the <sup>fi</sup>nal conclusion is given in Section 6.

## 2. Related works

For clustering the web data initial works were based on text mining and traditional information retrieval approaches that mostly use the web page contents, and neglect the hyperlink structure. Content-based clustering [14,29]. Some content-based works have used snippets as studied in [29]. However, content-based clustering does not adapt well with web environment since it ignores the availability of hyperlinks among web pages and is susceptible to spam. There are also other dif<sup>fi</sup>culties in using term-based approach for web page clustering.

Many successive works such as those in [4,21] tried to explore link analysis to improve the quality of web search results or extract useful knowledge from the web. At the beginning, most of the works only used the direct hyperlink between pages [5,19,23]. Then, another works were developed in [16,26] that utilized hyperlink transitivity, but the web page similarity derived directly from hyperlink transitivity analysis was over-simpli<sup>fi</sup>ed or only out-links of the pages were considered.

In [23], a link-based clustering algorithm is presented by co-citation and coupling analysis. According to preliminary experimental results, link-based clustering could cluster web search results into some small size but high quality clusters. But it suffers from the facts that pages without suf<sup>fi</sup>cient in-links or out-links could not be clustered, that means the recall is low.

The next efforts inclined toward using a combination of link structure and content information. A hierarchical network search engine is proposed in [24] that clusters hypertext documents to organize a given information space for supporting various services such as querying based on the contents. Also clustering hypertext documents by cocitation analysis is explored in [19]. In [26], the link-based clustering is extended by combining contents and links information appeared in anchor text, snippet, meta-content as well as anchor window of the inlinks, which might give a brief summarization for the topic of the page [12] proposed a new metric based on hyperlinks to measure the similarity between pages within the concerned web page space, that incorporates hyperlink transitivity and page importance.

## 3. Our basic density based method

We have developed a basic clustering algorithm employing density related concepts to cluster web data using only textual contents of documents. The method is explained in enough details in [10] and here we brie<sup>fl</sup>y review it. In the next section we extend this basic algorithm to use hyperlinks between the web documents.

The formal description of the algorithm is shown in Fig. 1. At the <sup>fi</sup>rst stage, for each data item, its neighborhood region is found. If this region does not satisfy the dense conditions, another data point is selected. Otherwise, the data points resident inside the neighborhood participate in the process of ordering, i.e. all the data items of all potential dense regions are ordered incrementally based on their distances with the nearest cores (we do this sorting using a min heap). Therefore at the end of this stage, we will have a min heap that contains the sorted distances established between the border points and associated (nearest) core points.

Then, in the second stage, the stored distances are extracted one by one and checked to <sup>fi</sup>nd whether they have intersection with previously constructed clusters to be joined with them. A composite cluster may be located at a higher level. This approach, i.e. global ordering and joining, enables the method to create hierarchical clusters (compared to other density based methods).

As analyzed in [10], performing range queries (to <sup>fi</sup>nd the neighborhood distances) and sorting the distances by insertion into a min heap has O(n log n) time complexity. The condition if (NList. count NMaxPts) is added in line 3, to prevent from over crowding a dense unit. If a neighborhood distance has more than MaxPts data items, it may cause the number of resident data items in a dense unit to increase and may increase the total complexity, too. An example is shown in Fig. 2. As it is considered, since the points existing in the region between the two neighborhoods are adjacent to other (core) points too, then they can be included in the neighborhood distances of those data points.

Here, we study more details of the implementation of the proposed method. We de<sup>fi</sup>ned variable MaxLevel in the algorithm of Fig. 1, that shows the maximum level of currently constructed clusters. When one neighborhood distance becomes a single base cluster, this variable is used to determine its level in hierarchy. When a neighborhood distance has intersection with a previously created cluster, the members of this neighborhood join to that cluster and it is checked whether the resultant cluster can be located at a higher level. To do so we added two properties to each cluster. One named as Level, showing the level of a cluster in the hierarchy and Distance which stores the least distance inside a cluster and then controls the density of the cluster. During joining new data this property is used to check whether the added distance is smaller than the allowed bound. If the extracted neighborhood distance is larger than the allowed bound, a new cluster is created and its level becomes one more than the level of the previous cluster and if it is necessary, MaxLevel is updated. This process is also done while checking the intersection of the neighborhood distance with previous clusters. If the neighborhood joins more clusters than one, it is checked whether this distance is greater than the distances of the base clusters. If it is greater so, the composite cluster moves to a higher level; otherwise a greater composite cluster is replaced with the base clusters at the same level. Each cluster has another property named Active. When a new cluster is created, this property is set to true. When constructing a cluster at a higher level, its Active property becomes true and it is instead set to false for the lower level base clusters. This enables the method to solely consider those clusters that are not child of any other cluster.

```asm
Algorithm: (Data, R, MinPts, MaxPts, IR, LNum)

//R: neighborhood radius
//MinPts: Minimum required data points to be considered as a dense distance
//MaxPts: Maximum points of a neighborhood that can be inserted in the heap
//IR: Internal Radius for decreasing the neighborhood distance in the dense regions
//LNum: Number of desired Levels

1    for each object in Data:
2    NList = FindNeighbors(object, R, MinPts);
3    if (NList.count > MaxPts):
4    NList = FindNeighbors(object, IR, MinPts);
5    SortByMinHeap(NList); // while insertion, updates the previously inserted border points.
6    else:
7    SortByMinHeap(NList); // while insertion, updates the previously inserted border points.
// Inserts each point of seed in MinHeap in a form: (CoreID,BorderID,Distance)
8 Initialize e by R/LNum or other values that is dependent to application And MaxLevel by 1;
9    while (! EmptyMinHeap):
10    d=GetMin(MinHeap);
11    isFirst = true;
12    for each Cluster C_i in ClusterList that C_i.Active is true:
13    if (hasIntersection(d.Neighbors,C_i)):
14    if (isFirst == true):
15    isFirst = false;
16    if (d.Distance -C_i.Distance > e):
17    AddNewLevel(C_i,d);
18    else:
19    merge(C_i,d.Neighbors);
20    else:
21    if (d.Distance -C_i.Distance > e):
22    AddNewLevel(C_i,d);
23    else:
24    merge(C_i,d.Neighbors);
25    deleteCluster(C_i,ClusterList);
26    if (isFirst == true):
27    CreateNewCluster(null, d.Neighbors, d.Distance, MaxLevel);

Add NewLevel(&C_i, &d):
28    C_i.Active = false;
29    newCluster = CreateNewCluster(C_i, d.Neighbors, d.Distance, C_i.Level+1);
30    if (newCluster.Level > MaxLevel)
31    MaxLevel = newCluster.Level
```  
Fig. 1. Formal description of the proposed algorithm [10].

It may seem that this algorithm uses a lot of parameters. In fact the main input parameters (R and MinPts) are alike the other density based algorithms. Others such as IR and MaxPts are only used for preprocessing. Also using R and MinPts we can easily approximate the value of the other parameters. The input parameter LNum is only used to determine the number of levels (as is obvious from Fig. 1 line 8, it is used to initialize the mutation parameter from one level to higher level) and can be neglected. In fact the mutation approach may be considered as a mutation from current distance relative to the initial distance of cluster stored in Distance property.

![](/api/attachments/CY8WX2GZ/fulltext/images/d080a60814a520525c988d3f06f405fdef1c0d0f421c2600376181e49eb6ebbc.jpg)  
Fig. 2. Decreasing the complexity by using a smaller neighborhood radius.

The method includes the bene<sup>fi</sup>ts of both OPTICS and DBRS, provides advantages such as hierarchical clustering and enables clustering by sampling and incremental learning. In the following we compare different density based methods from some views. These criteria include the neighborhood graphs they construct and the forests of cluster trees they correspond to.

## 3.1. Comparison from the view of neighborhood graphs

According to [22], the graph associated with a density based method is de<sup>fi</sup>ned as a connected neighborhood sub-graph in which density reach-ability is used as the neighborhood relation. Since DBSCAN and OPTICS de<sup>fi</sup>ne clusters in a way that with respect to the de<sup>fi</sup>nition, there is a directed path between every two graph nodes, the process of constructing the clusters is similar to creating a strongly connected neighborhood graph. In the case of DBRS and as well as the proposed algorithm, according to the expansion criterion, their corresponding graphs are symmetric and so the created paths are undirected. Therefore the constructed graph is a connected graph in opposition with a strongly connected one. Since <sup>fi</sup>nding and constructing a connected component is simpler than a strongly connected one and needs less processing, we can conclude that the proposed algorithm can complete the clustering easier and faster.

## 3.2. Comparison from the view of clustering trees

When a density based algorithm is performed, a forest of trees (every tree associated with a cluster) is created. A cluster tree is a tree in which each node corresponds to a data item in the data set and each edge corresponds to a neighborhood relationship between a parent point and a newly discovered child point. DBSCAN builds each tree in depth-<sup>fi</sup>rst (DFS) way and always <sup>fi</sup>nishes one tree before starting another one. For OPTICS, the trees are built in the same way with the difference that the criterion of completing a tree is the distance between the parent node (core point) and the child node (border point).

DBRS builds its trees randomly. At every step, it selects a new point and randomly generates some branches of trees and if possible connects them to existing branches (trees). From this viewpoint, our algorithm is similar to DBRS; which instead of completing one tree altogether, it builds several trees simultaneously. But it does not generate and connect the branches in a random way; cluster trees are created in a top-down approach from small to large distances, and from this aspect it is more similar to the OPTICS cluster trees construction.

## 4. Link-based algorithm

The proposed basic method proposed in the previous section has several interesting properties. Nevertheless the method has some limitations including:

• A constant value for mutation to a higher level is not appropriate. A smaller value maybe appropriate for smaller clusters, but larger ones must take larger values.

• It is developed for web data clustering, but it doesn't use hyperlink structure of the web.

• Setting accurate values for parameters of the proposed method maybe dif<sup>fi</sup>cult.

In this section, with respect to the hyperlink structure of the web graph, we describe some improvements on the basic algorithm. As some previous research show, hyperlink structure divulges a smaller scale than the text context which brings some interesting ideas: 1) link structure in combination with text content can help to construct hierarchical clusters with the link-based clusters as the base clusters, 2) link structure can be a good suggestion to <sup>fi</sup>nd dense units. In the following subsections, we explain the improved method and argue on its computational complexity. The method consists of two steps: <sup>fi</sup>nding the dense units and joining them to complete the hierarchy.

## 4.1. Finding dense units

With respect to the ‘small world’ nature of the web structure, each web page has a short path to other pages meaning that the hyperlink structure is nearly a connected graph. However, there are a considerable number of noisy and biased links. Therefore, we must remove extra links and partition the hyperlink structure. Inspiring from the basic dense unit de<sup>fi</sup>nition, we de<sup>fi</sup>ne the link-based dense unit (LD\_Unit) as a subhyperlink structure wherein each (core) node has minimum similarity W with at most MaxN neighbors:

De<sup>fi</sup>nition 1. A subhyperlink structure is an LD\_Unit if for each core node N inside the unit there is a subset of N's neighbors that: 1) it has at most MaxN members, and 2) sum of the similarities between N and the nodes of this subset is at least W.

LD\_Unit is constructed from core and border nodes. Core nodes are those satisfying the speci<sup>fi</sup>ed condition while border nodes are terminal nodes that restrict the expansion of a unit. An example LD\_Unit is shown in Fig. 3 for W=2.5 and MaxN=4. The edge labels show the similarity between corresponding web pages. These values are computed using vector based cosine similarities. In this unit, the nodes that satisfy the condition are core and the others are border. We start from a random node and after creating the required vectors, examine the LD\_Unit condition; if it satis<sup>fi</sup>es, the process continues by examining its neighborhoods. Otherwise, its neighbors are considered to be out of the unit. This process continues until the unit is fully expanded. All LD\_Units of the data set are extracted in this way. Since a web page may have a limited number of links, we add neighbors with a signi<sup>fi</sup>cant similarity value (i.e. higher than 0.7). The number of the links connected to each node is limited (according to small world assumption), therefore, we can construct all the LD\_Units with O(n) time complexity.

## 4.2. Joining dense units

So far we have explained how to extract dense units of the web hyperlink structure, so the remaining problem is to join them to create <sup>fi</sup>nal clusters. As highlighted before, an interesting property that seems useful in web structure clustering is to create them hierarchically. Since the scales of link and content are, it is not reasonable to join all LD\_Units at the same level. Finding the best combination for constructed units is an NP-Complete problem (the proof is brought in Theorem 1).

Theorem 1. Finding the best combination of the dense units that yields the optimal clustering is an NP-Complete problem.

![](/api/attachments/CY8WX2GZ/fulltext/images/b1cbb5e2f287bcd43fa0c421e5007b56dc5cdd6e493c1fc104e72429c1664f1b.jpg)  
Fig. 3. An example from an LD\_Unit.

![](/api/attachments/CY8WX2GZ/fulltext/images/0f9fcbd063760ede523cf905c84cfbbd63d9d9ca0ffce655aac84e6706dda094.jpg)  
Fig. 4. Finding the nearest neighbors of each node.

Proof. We know that data clustering is an NP-Complete problem [21]. We can consider a hyper graph with the nodes that represent the dense units. Each node has links to two kinds of nodes: nodes that correspond to the data points inside the dense unit, and conterminous nodes (w.r.t similarity between the dense units). We know that each hyper node (dense unit) has a limited number of data points. So the number of hyper nodes is itself O(n). Therefore combining these units can be simulated as a clustering problem (clustering the hyper graph nodes) and so <sup>fi</sup>nding the optimum solution will be an NP-Complete problem. □

To solve the problem, we follow a heuristic approach. We de<sup>fi</sup>ne a measure and try to optimize it during the joining process. This measure is de<sup>fi</sup>ned in Eq. (1).

$$
\frac {\sum \text { Clustered   distances   of } C _ {i} + \sum \text { Clustered   distances   of } C _ {j} + \text { distance   between   two   clusters }}{\left(n _ {i} + n _ {j} - 1\right) \times (\text { Distance   between   two   centers })}? M\tag{1}
$$

$n _ { i }$ and $n _ { j }$ are the size of clusters i and $j ,$ respectively (the number of total distances of the compound cluster after adding the new distance will be $n _ { i } + n _ { j } - 1 )$ . M is known as the monotony of the clusters and determines whether the distances inside the clusters are nearly alike or the new distance is larger. As we will see later, we perform joining from smaller and more compact clusters (distances) to the larger and far clusters. Therefore the new distance will be greater than previous distances and can disturb the monotony of the cluster. This de<sup>fi</sup>nition has the advantage of providing the users to have their own desired granularity for created clusters (by setting parameter M).

For the distance between two clusters, the shortest distance seems to be more suitable to be checked for establishing the monotony inside the resultant cluster. The reason is that all regions of the base clusters are checked before and it remains to check the join (border) areas. However, for calculating the shortest distance, we must spend $O ( n ^ { 2 } )$ time complexity for each joining (n is the number of all nodes). If we have totally n joining, then the total complexity will be $O ( n ^ { 3 } )$ which is high (of course the complexity can be reduced to $O ( n ^ { 2 }$ log n) with some improvements and using priority queues). To reduce complexity, we propose a heuristic approach. At <sup>fi</sup>rst, for each node we <sup>fi</sup>nd some nearest external nodes. An external node is de<sup>fi</sup>ned according to De<sup>fi</sup>nition 2.

De<sup>fi</sup>nition 2. Node a is said to be external node of b if a and b do not exist in the same LD\_Unit.

For each node, <sup>fi</sup>nding the nearest external nodes takes O(n) (O $( n ^ { 2 } )$ for all nodes). We propose an alternative approach to be performed with lower complexity. The method is described in Fig. 4. At <sup>fi</sup>rst, each node is inserted in a m-tree which provides operations such as <sup>fi</sup>nding the k nearest data points and <sup>fi</sup>nding the data points inside a given distance R with O(log n) time complexity [7]. Also insertion into and deletion from this structure takes O(log n). Therefore for n nodes (each unit contains a constant number of nodes), complexity of the <sup>fi</sup>rst section becomes O(n log n). Then, the nodes inside each unit are deleted from the m-tree to provide the possibility of <sup>fi</sup>nding the nearest external nodes. This is done by calling mtree\_K-nn(no,NN) that extracts NN nearest neighbors of node no. Then these nodes are inserted again and the process is continued for the nodes of the next unit. After <sup>fi</sup>nding a new nearest distance, it is inserted into a data structure such as Min Heap taking O(log n) time complexity. This causes the distances to be sorted at the end of the process. Since each operation including insertion, deletion, querying from the m-tree and also insertion into the min heap takes O(log n) time complexity, the total complexity of this step is O(n log n).

![](/api/attachments/CY8WX2GZ/fulltext/images/3314e454380aae43cd843f410f7080cfb396aa57c32a2f646985b20507dda77b.jpg)  
Fig. 5. Extracting distances and completing the hierarchy.

![](/api/attachments/CY8WX2GZ/fulltext/images/f03318b92bd13b978d3f1bbdb93710c6f32d15d728f52275954aaed0ea298955.jpg)

Fig. 6. Results of applying proposed algorithm (right) and OPTICS (left) on a data set and for different parameter values.  
![](/api/attachments/CY8WX2GZ/fulltext/images/33d6d9abe400de1d1336f5e44452b72e0e00602af22ce05446067f14c1f6f6f0.jpg)  
a) Results of clustering by the algorithm

![](/api/attachments/CY8WX2GZ/fulltext/images/155d8d0ec726df2c0a3d106a480f1fe5995c402af298f588b0e69d1df4a28913.jpg)  
b) Results of clustering by DBRS  
Fig. 7. Results of <sup>fi</sup>nding dense regions of the data set for clustering by sampling.

Now we extract the sorted distances one by one and examine their effects on the clustering process using relation (1). After extracting each distance and evaluating Eq. (1), two different situations can occur (L denotes the left side of the formula, before ? in relation (1)):

1. If L≥M, corresponding units are joined to construct a unique unit at the same level.

2. If LbM, a new unit at a higher level is constructed and set the units as its children.

Description of the method is detailed in the algorithm of Fig. 5. There are totally O(n) stored distances, the cost of reconstructing the min heap is O(log n) and other operations are performed with a constant time, so the total time complexity is O(n log n).

## 5. Experimental results

In this section we explain various experiments to examine the proposed methods different aspects. At the <sup>fi</sup>rst test, we examine the proposed density based algorithm in comparison with the other density based methods in terms of accuracy, speed and ability of hierarchical clustering. At the second test we will apply the density based algorithm on the web data and will evaluate its ef<sup>fi</sup>ciency in term of F-measure. Also we discuss on the parameter setting issues. Finally, the last test contains some experiments for the link-based method.

![](/api/attachments/CY8WX2GZ/fulltext/images/90818b77ebc18a14187049f3014c79855fb8dc8c439fec895110bfc7f1cf20cf.jpg)  
Fig. 8. Different hierarchies according to the values of parameter mutation.

Evaluation results on the web data, a) density based algorithm, b) K-Means.

<table><tr><td colspan="3">a)</td><td colspan="3">b)</td></tr><tr><td>Cluster ID</td><td>N</td><td>F</td><td>Cluster ID</td><td>N</td><td>F</td></tr><tr><td>1</td><td>407</td><td>0.7333783</td><td>1</td><td>17</td><td>0.4838</td></tr><tr><td>2</td><td>44</td><td>0.6884285</td><td>2</td><td>68</td><td>0.5483636</td></tr><tr><td>3</td><td>209</td><td>0.7132867</td><td>3</td><td>34</td><td>0.6260317</td></tr><tr><td>4</td><td>131</td><td>0.6343939</td><td>4</td><td>117</td><td>0.5687394</td></tr><tr><td>5</td><td>98</td><td>0.7246896</td><td>5</td><td>26</td><td>0.6676119</td></tr><tr><td>6</td><td>57</td><td>0.5929411</td><td>6</td><td>41</td><td>0.5483636</td></tr><tr><td>7</td><td>41</td><td>0.6908571</td><td>7</td><td>37</td><td>0.6293650</td></tr><tr><td>8</td><td>19</td><td>0.8498823</td><td>8</td><td>84</td><td>0.7061111</td></tr><tr><td>9</td><td>32</td><td>0.7734193</td><td></td><td></td><td></td></tr><tr><td>10</td><td>53</td><td>0.7649673</td><td></td><td></td><td></td></tr></table>

## 5.1. Comparison of density based algorithms from different aspects

For this test, the employed data sets contain spatial data items where clusters can be located in several levels. They are extremely used in evaluation of many other data clustering methods.

At <sup>fi</sup>rst and similar to [10] we compare the proposed method and OPTICS as shown in Fig. 6. By tracing the <sup>fi</sup>gure several results can be observed. First, both algorithms construct similar base clusters that have suitable accuracies. However, those that are created by the proposed algorithm are larger than those of OPTICS (growing happens faster). In the proposed algorithm if two or more clusters are connected by a neighborhood distance, a unique cluster is constructed; while in OPTICS the combination does not occur and only the clusters are expanded. This results in faster convergence of the proposed method.

The most important observation is the ability of constructing clusters at several levels. Algorithms such as OPTICS and DBSCAN are unable to create hierarchical clusters. This matter is shown in Fig. 6, in which there exist three clusters that should be combined and construct a larger and more general cluster at a higher level. OPTICS <sup>fi</sup>rst <sup>fi</sup>nds one of the small dense clusters and then expands it until encompassing the second and third clusters. So only one cluster has connected to two others and the two other clusters are disjoint from each other. On the other hand, in the proposed method, at <sup>fi</sup>rst the three base dense clusters are created and then they are joined at a higher level.

In the following we compare the sampling abilities of the proposed method and DBRS. This test is important since it reveals the blind nature of DBRS for sampling. A fast and ef<sup>fi</sup>cient approach for sampling is to select a small value for R and a large value for MinPts. This is because when we encounter processing limitations, the wise way is to present the most dense regions of the entire data set. Selecting small value of R and large value for MinPts satis<sup>fi</sup>es this requirement.

According to the results of Fig. 7, this technique works well for the proposed algorithm, but DBRS can not utilize it in a suitable manner. This occurs because DBRS in contrast with the proposed algorithm applies no priority on the order of scanning of the data points and on the expansion of the clusters and therefore using DBRS may lead to many island clusters. Results of Fig. 7 are obtained with R=2 and MinPts=15. As is clear from it, the proposed algorithm selects dense regions of the entire data set which can be a good choice.

## 5.2. Use of the density based method for clustering web pages

In this section, we apply the density based algorithm on web data and evaluate the results. Also in the following we argue on the parameter setting issues. At <sup>fi</sup>rst 424 web documents are selected in Politics domain and after creating frequency vectors, LSI (Latent Semantic Indexing) technique is applied on the vectors to reduce the number of dimensions to 2 that provides the applicability of the algorithms in a more feasible manner. By reducing the number of dimensions, we can use distance (or similarity) measures such as Euclidean distance (used in our experiments) more ef<sup>fi</sup>ciently.

In the next step, these vectors are used by the algorithm to create the clusters. Nevertheless the value of different parameters may affect the quality of the clusters, we perform the clustering with parameters R=20, MinPts=7, and mutation=1.8 (parameter e) and evaluate the results. The resulted clusters are shown in Fig. 8-b. We enumerate the clusters in a top-down and left to right BFS order.

Several methods have been presented in the literature for evaluation of clustering methods, in which the most important methods are based on entropy and F-measure. F-measure combines precision and recall measures as de<sup>fi</sup>ned in Eq. (2) where precision (P) and recall (R) are calculated using Eq. (3). n shows the size of cluster j, g shows the size of class j and N (i,j) shows the number of pages of class i in cluster j.

F-measure (like entropy) only is developed for evaluation of <sup>fl</sup>at clusters (or the lowest level of hierarchical clusters). In [10] we adapted F-measure for evaluation of hierarchical clustering. We <sup>fi</sup>rst apply F-measure on the clusters of lowest level and then obtain the Fmeasure of the higher clusters from their children using Precision de<sup>fi</sup>ned in Eq. (4).

![](/api/attachments/CY8WX2GZ/fulltext/images/7a06fc400e5be1b54d2ec518ed9ef31bcbb0e918ca6e8d9debc843b7338cd5f0.jpg)  
a) The effects of changes in MinPts and mutation on Number of levels.

![](/api/attachments/CY8WX2GZ/fulltext/images/e41f07e2182958c9cb3b0e49c0f326fafaf78c8daa9218627d2004912cce6fe3.jpg)  
b) The effects of changes in MinPts and mutation on Number of clusters  
Fig. 9. Analysis of MinPts and mutation w.r.t number of levels and clusters.

The properties of each examined data set.

<table><tr><td>Data set name</td><td>Number of nodes</td><td>Number of links</td><td>Average number of links per each node</td><td>M</td><td>W</td><td>MaxN</td><td>NN</td></tr><tr><td>DS1</td><td>483</td><td>3558</td><td>7.36</td><td>.7</td><td>2.5</td><td>5</td><td>8</td></tr><tr><td>DS2</td><td>674</td><td>4537</td><td>6.73</td><td>.7</td><td>2</td><td>4</td><td>8</td></tr></table>

$$
F (i, j) = \frac {2 (P (i , j) * R (i , j))}{(P (i , j) + R (i , j))}, F = \sum_ {i} \frac {g _ {t}}{n} \max _ {j} \{F (i, j) \}\tag{2}
$$

$$
P (i, j) = N (i, j) / n _ {j}, R (i, j) = N (i, j) / g _ {i}\tag{3}
$$

$$
P _ {C} = \sum_ {\forall k \in C \cdot \text { children }} \frac {n _ {k}}{n} P _ {k} + \frac {n - \sum_ {\forall k \in C \cdot \text { children }} n _ {k}}{n} P _ {R}\tag{4}
$$

$P _ { R }$ shows the precision of cluster members not belonging to subclusters. For the recall values, we must calculate the $R _ { R }$ by traversing all the relevant web pages, while a simpler method is to obtain its value by calculating straightly and without considering pre-calculated values for sub-clusters. Using this process the results are shown in Table 1a. For more evaluations, we apply K-Means and compare the results. Since K-Means is sensitive to the value of K (number of clusters), it is repeated with K =8, 10, 12 and the best result is selected (Table 1b, with $K = 8 )$ . Total F-measure for the proposed algorithm is 0.710853 while for K-Means is 0.603258. These values show the effectiveness of the proposed algorithm.

In the following we study the effect of different parameters on the behavior of the algorithm. Our experiments show that the value of R is not so important and an estimate value that covers the ranges is enough. So we argue on the mutation and MinPts. We <sup>fi</sup>rst apply the algorithm with R=20, MinPts=7, and mutation=1.2, 1.8, and 2.3. The results are shown in Fig. 8. As is obvious from Fig. 8-b, mutation =1.8 constructs more appropriate clusters. If we decrease mutation (Fig. 8-a, with mutation= 1.2), the number of clusters and levels increases, that in this manner some of the clusters are created only by partial extension of a lower cluster. In contrast, by increasing mutation to 2.3 (Fig. 8-c), mutation from one level to the higher does not occur and the constructed clusters are located at one or some limited levels.

In the following we consider several values for MinPts (5, 7, and 9) and by changing the value of mutation, investigate the effects on the results as shown in Fig. 9. It is clear that both the number of clusters and the number of levels have a reverse relation with mutation. Also it is concluded that selecting rather near values for both the parameters doesn't cause a deep change in the number of levels and clusters. This conclusion is very useful; we can only have an estimation of these parameters and it is not necessary to determine their values de<sup>fi</sup>nitely.

The properties of the clusters created for each data set.

<table><tr><td>Data set name</td><td>Number of clusters</td><td>Number of levels</td><td>Number of noisy data</td><td>Number of LD_Units</td></tr><tr><td>Academic and scientific pages</td><td>14</td><td>4</td><td>22</td><td>36</td></tr><tr><td>Politic news</td><td>21</td><td>6</td><td>47</td><td>71</td></tr></table>

Evaluation of the link-based method for the <sup>fi</sup>rst (a) and the second (b) data sets.

<table><tr><td colspan="4">a)</td><td colspan="4">b)</td></tr><tr><td>Center ID</td><td>Parent cluster</td><td>N</td><td>F</td><td>Center ID</td><td>Parent cluster</td><td>N</td><td>F</td></tr><tr><td>C1</td><td>C10</td><td>23</td><td>0.74407</td><td>C1</td><td>C13</td><td>43</td><td>0.7924528</td></tr><tr><td>C2</td><td>C10</td><td>58</td><td>0.74940</td><td>C2</td><td>C13</td><td>19</td><td>0.7834394</td></tr><tr><td>C3</td><td>C10</td><td>42</td><td>0.77987</td><td>C3</td><td>C17</td><td>78</td><td>0.8249696</td></tr><tr><td>C4</td><td>C11</td><td>84</td><td>0.73987</td><td>C4</td><td>C14</td><td>52</td><td>0.7842038</td></tr><tr><td>C5</td><td>C11</td><td>75</td><td>0.73386</td><td>C5</td><td>C14</td><td>66</td><td>0.79421383</td></tr><tr><td>C6</td><td>C13</td><td>68</td><td>0.74335</td><td>C6</td><td>C14</td><td>47</td><td>0.8698850</td></tr><tr><td>C7</td><td>C12</td><td>71</td><td>0.81987</td><td>C7</td><td>C15</td><td>32</td><td>0.7694805</td></tr><tr><td>C8</td><td>C12</td><td>26</td><td>0.68619</td><td>C8</td><td>C15</td><td>49</td><td>0.9049723</td></tr><tr><td>C9</td><td>C12</td><td>14</td><td>0.66703</td><td>C9</td><td>C16</td><td>72</td><td>0.8289156</td></tr><tr><td>C10</td><td>C13</td><td>123</td><td>-</td><td>C10</td><td>C16</td><td>61</td><td>0.774709</td></tr><tr><td>C11</td><td>C13</td><td>159</td><td>-</td><td>C11</td><td>C18</td><td>15</td><td>0.8198780</td></tr><tr><td>C12</td><td>C14</td><td>111</td><td>-</td><td>C12</td><td>C21</td><td>93</td><td>0.8198780</td></tr><tr><td>C13</td><td>C14</td><td>350</td><td>-</td><td>C13</td><td>C17</td><td>62</td><td>-</td></tr><tr><td>C14</td><td>-</td><td>461</td><td>-</td><td>C14</td><td>C19</td><td>165</td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td>C15</td><td>C18</td><td>81</td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td>C16</td><td>C18</td><td>133</td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td>C17</td><td>C19</td><td>140</td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td>C18</td><td>C20</td><td>229</td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td>C19</td><td>C20</td><td>305</td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td>C20</td><td>C21</td><td>534</td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td>C21</td><td>-</td><td>627</td><td>-</td></tr></table>

## 5.3. Examination of link-based method for clustering web pages

In this section, we report our experiments as well as evaluations on the proposed link-based method. We have collected two data sets; one from academic and scienti<sup>fi</sup>c web pages and another from Politics sites. Each data set constructs a hypertext graph with the web pages as its nodes connected by the hyper links. Their properties are shown in Table 2. In it, we have calculated the average number of links per node that gives us a good sense for estimating the values of MaxN and W parameters. The selected values are shown in the right columns of Table 2. Of course these values are not completely precise and like other density based approaches, some experimental tests are necessary for estimating them. The value of NN speci<sup>fi</sup>ed in the rightmost column is not so important; it should be determined large enough such that the corresponding extracted distances can satisfy the desired hierarchy.

The speci<sup>fi</sup>cation of the resultant clusters is described in Table 3 and is compared to two popular web clustering algorithms, i.e. K-Means and Single Linkage. We run K-Means <sup>fi</sup>ve times with different centers and select the best results. Single Linkage is a hierarchical agglomerative method that from some aspects, its behavior is similar to the proposed method, so we enter it in our examination.

The results of the link-based algorithm are shown in Table 4a and b for the two data sets, respectively (since all the web pages are included at the lowest clusters, so we have calculated only the parameters of the lowest clusters). We showed the F-measure values of K-Means and Single Linkage algorithms; which along with the proposed methods are compared in Table 5.

Considering Tables 4 and 5, it is obvious that the proposed methods perform better than other methods. This is because the proposed methods <sup>fi</sup>nd and combine the dense units and then constructs the hierarchy in a more accurate manner treating noisy and outlier data, too. These improvements increase the quality of the clusters. In addition the density and the link-based methods are compared in Table 5. According to the results, the link-based method produces clusters with higher quality.

Comparison of the F-measure value of different methods.

<table><tr><td>Name of the algorithm</td><td>K-Means</td><td>Single linkage</td><td>Density based method</td><td>Link-based method</td></tr><tr><td>Total F-measure of the first data set</td><td>0.61280</td><td>0.52864</td><td>0.72458</td><td>0.75154</td></tr><tr><td>Total F-measure of the second data set</td><td>0.59058</td><td>0.55387</td><td>0.69169</td><td>0.73884</td></tr></table>

## 6. Conclusion

This paper presented a new density and link-based methods that try to use the properties of the web environment to adjust the density based algorithms for attaining higher quality. At <sup>fi</sup>rst we discussed a new density based algorithm that creates hierarchical clusters with faster convergence and ability to do clustering by sampling. Also as experiments show, the method has preference in <sup>fi</sup>nding the good representatives of entire data.

We also introduced new concepts to use density based algorithms for the web data. The method, at <sup>fi</sup>rst <sup>fi</sup>nds the dense units according to the hypertext structure of the web. In the next step, these dense units are joined together to complete the hierarchy. For joining, we offered a measure to be optimized that provides the possibility of determining the cluster boundaries dynamically.

While the time complexity of the most hierarchical algorithms is O (n<sup>2</sup>), the proposed method bene<sup>fi</sup>ts from the complexity of O(n log n). In addition, the experimental results show higher clustering quality. Finally additional experiments revealed that the link-based method has some preferences over the density based method.

## References

[1] M. Ankerst, M.M. Breunig, H.-P. Kriegel, J. Sander, OPTICS: ordering points to identify the clustering structure, ACM SIGMOD'99, 1999, pp. 49–60.

[2] H.K. Bhargava, Progress in web-based decision support technologies, Decision Support Systems 43 (4) (2007) 1083–1095.

[3] R.M. Bittmann, R. Gelbard, Visualization of multi-algorithm clustering for better economic decisions — The case of car pricing, Decision Support Systems 47 (1) (2009) 42–50.

[4] S. Brin, L. Page, The anatomy of a large scale hypertextual web search engine Computer Networks and ISDN Systems 30 (1–7) (1998) 107–117.

[5] S. Chakrabarti, B. Dom, P. Indyk, Enhanced hypertext categorization using hyperlinks, Proceedings of SIGMOD98, 1998, pp. 307–318.

[6] M. Chen, TeamSpirit: design, implementation, and evaluation of a web-based group decision support system, Decision Support Systems 43 (4) (2007) 1186–1202.

[7] P. Ciaccia, M. Patella, P. Zezula, M-tree: an ef<sup>fi</sup>cient access method for similarity search in metric spaces, Proceedings of the 23rd VLDB, 1997

[8] W.H.E. Day, H. Edelsbrunner, Investigation of Proportional Link Linkage Clustering Methods, Journal of Classi<sup>fi</sup>cation, vol. 2, Springer-Verlag, 1985, pp. 239–254.

[9] M. Ester, H.-P. Kriegel, J. Sander, X. Xu, A Density-Based Algorithm for Discoverin Clusters in Large Spatial Databases with Noise, KDD'96, 1996, pp. 226–231.

[10] M. Haghir Chehreghani, H. Abolhassani, M.H. Chehreghani, Attaining higher quality for density based algorithms, International Conference on Web Reasoning and Rule Systems, LNCS, 2007, pp. 329–338.

[11] X. Hea, H. Zhaa, C.H.Q. Ding, H.D. Simon, Web document clustering using hyperlink structures, Computational Statistics & Data Analysis 41 (1) (2002) 19–45.

[12] J. Hou, Y. Zhang, J. Cao, Web page clustering: a hyperlink-based similarity and matrix-based hierarchical algorithms Proceedings of APWeb'03 LNCS 2003

[13] A.K. Jain, M.N. Murty, P.J. Flynn, Data clustering: a review, ACM Computing Surveys (CSUR) 31 (3) (1999) 264–323.

[14] B. Larsen, C. Aone, Fast and effective text mining using linear-time document clustering, Proceedings of SIGKDD'99, CA, 1999, pp. 16–22.

[15] W.-H. Lu, et al., Using web resources to construct multilingual medical thesaurus for cross-language medical information retrieval, Decision Support Systems 45 (3) (2008) 585–595.

[16] M. Marchiori, The quest for correct information on the web: hyper search engines, Proceedings of the 6th International Word Wide Web Conference, 1997, pp, 1225–1235.

[17] J. McQueen, Some methods for classi<sup>fi</sup>cation and analysis of multivariate observations. Fifth Berkeley Symposium on Mathematical Statistics and Probability, 1967, pp. 281–297.

[18] G.W. Milligan, M.C. Cooper, An examination of procedures for detecting the number of clusters in a data set, Psychometrika 50 (1985) 159–179.

[19] J. Pitkow, P. Pirolli, Life, death, and lawfulness on the electronic frontier, Proceedings of ACM CHI'97, 1997, pp. 383–390

[20] G. Salton, Automatic Text Processing: The Transformation, Analysis, and Retrieval of Information by Compute, Addison-Wesley, Reading, 1989.

[21] A. Schenker, et al., A comparison of two novel algorithms for clustering web documents, International Workshop on Web Document Analysis, 2004, pp. 71–74.

[22] X. Wang, H.J. Hamilton, DBRS: A Density-Based Spatial Clustering Method with Random Sampling, PAKDD, Korea, 2003, pp. 563–575.

[23] Y. Wang, M. Kitsuregawa, Use link-based clustering to improve web search results, International Conference on Web Information Systems Engineering (WISE), 2001, pp. 119–128.

[24] Y. Wang, M. Kitsuregawa, On combining link and contents information for web page clustering, Database and Expert Systems Applications (2003) 902–913.

[25] C.-P. Wei, H.-S. Yang, H.-W. Hsiao, A collaborative <sup>fi</sup>ltering-based approach to personalized document clustering, Decision Support Systems 45 (3) (2008) 413–428.

[26] R. Weiss, et al., HyPursuit: a hierarchical network search engine that exploits content-link hypertext clustering, Seventh ACM Conference on Hypertext, 1996, pp. 180–193.

[27] C.W. Wen, et al., A distributed hierarchical clustering system for web mining International Conference on Web-Age Information Management (WAIM2001), 2001, pp. 103–113.

[28] C.T. Zahn, Graph-theoretical methods for detecting and describing gestalt structures, IEEE Transactions on Computers C-20 (1971) 68–86.

[29] O. Zamir, O. Etzioni, Web document clustering: a feasibility demonstration, Proceed ings of SIGIR' 98 Melbourne, Australia, 1998, pp. 46–54.

![](/api/attachments/CY8WX2GZ/fulltext/images/ff51e281952f28313f6984c81ef5a8ec065e29ff2603e7277bb916d3058fa533.jpg)  
Morteza Haghir Chehreghani received his Bsc. in Computer Engineering from Amirkabir University of Technology in 2005. Then in Dec. 2008 he <sup>fi</sup>nished his Msc education at Sharif University of Technology. Currently he is member of Web Intelligence Lab in Sharif University of Technology. His research interests are Data and Web Mining, Machine Learning, Mathematical Modeling of Data and related areas.

![](/api/attachments/CY8WX2GZ/fulltext/images/388e4d38022d1132b0d28e574cae78bbaeb70cd153a243e24405937194cc011e.jpg)  
Hassan Abolhassani received his Bsc. in Computer Engineering from Esfahan University, his Msc, in Software Engineering from Sharif University of Technology and his Ph.D. in Automatic Software Engineering from Saitama University. He joined the Computer Engineering Department of Sharif University of Technology in September 2003 and is now an Assistant Professor lecturing courses in Web Intelligence area and directing the Web Intelligence Laboratory.

![](/api/attachments/CY8WX2GZ/fulltext/images/c6c1d45cb1ace8ac876c325727e4c46b3d6b9f9441f20fee06929263b6318dc4.jpg)

Mostafa Haghir Chehreghani after obtaining his Bsc. of Computer Engineering from Science and Industry University in 2004, he received his Master's degree in Computer Engineering from University of Tehran in 2007. His research interests include database systems, web information systems and data mining, especially structure mining and management.
