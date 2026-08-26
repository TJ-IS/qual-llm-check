---
otero_id: 3158
otero_key: "4DXHW7QD"
title: "A graphical shopping interface based on product attributes"
authors: "Martijn Kagie; Michiel van Wezel; Patrick J.F. Groenen"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.06.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A graphical shopping interface based on product attributes

Martijn Kagie ⁎, Michiel van Wezel, Patrick J.F. Groenen

Econometric Institute, Erasmus University Rotterdam, Netherlands

## a r t i c l e i n f o

Article history: Received 5 March 2007 Received in revised form 27 June 2008 Accepted 30 June 2008 Available online 10 July 2008

Keywords: Recommender systems Multidimensional scaling Similarity Electronic commerce Case-based reasoning

## a b s t r a c t

Most recommender systems present recommended products in lists to the user. By doing so, much information is lost about the mutual similarity between recommended products. We propose to represent the mutual similarities of the recommended products in a two dimensional map, where similar products are located close to each other and dissimilar products far apart. As a dissimilarity measure we use an adaptation of Gower's similarity coef<sup>fi</sup>cient based on the attributes of a product. Two recommender systems are developed that use this approach. The <sup>fi</sup>rst, the graphical recommender system, uses a description given by the user in terms of product attributes of an ideal product. The second system, the graphical shopping interface, allows the user to navigate towards the product she wants. We show a prototype application of both systems to MP3-players.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

In most electronic commerce stores, consumers can choose from an enormous number of different products within a product category. Although one would assume that increased choice is better for consumer satisfaction, the contrary is often the case [30]. This phenomenon is known as the paradox of choice: a large set of options to choose from makes it more dif<sup>fi</sup>cult for the consumer to <sup>fi</sup>nd the product that she prefers most, that is, the product that is most similar to the consumer's ideal product. When the number of choice options increases, consumers often end up choosing an option that is further away from the product they prefer most. In many product categories, such as real estate and electronics, a consumer has to choose from a heterogeneous range of products with a large amount of product attributes. In most current e-commerce interfaces, the consumer can only search by constraining the values of one or more product attributes, for example, the brand of an MP3 player should be ‘Apple’, and its memory size should be larger than 2 GB. The products that satisfy these constraints are then shown in a list.

A disadvantage of this approach to product search is the use of crisp boundaries, which the consumer may <sup>fi</sup>nd too strict. For instance, 1.99 GB players are not listed with a 2 GB boundary, while a consumer may be perfectly happy with a 1.99 GB player. Another disadvantage of the traditional ‘query-and-list’ approach is its inablility to cope with substitution effects. Such an effect occurs when a shortcoming on one attribute can be compensated by another attribute. For example, a consumer can be equally happy with a cheaper MP3 player with less memory as with a more expensive one with a larger amount of memory compared to some ideal product speci<sup>fi</sup>cation. Yet, when restricting the search results to cheap MP players, the latter one will not be shown.

An alternative to this approach is to let the consumer describe an ideal product based on her ideal values for the product attributes. Then, products can be listed in order of similarity to the ideal product.

A disadvantage of the usual approach of presenting the products in a list is that no information is given on how similar the selected products are to each other. For example, two products that have almost the same similarity to the ideal product can differ from the ideal product on a completely different set of attributes and thus differ a lot from each other. Therefore, mutual similarities should be incorporated when displaying recommended products to consumers.

In this paper, we propose a graphical recommender system (GRS) that visualizes the recommended products together with the ideal product in a 2D map using the mutual similarities. To do this, multidimensional scaling (MDS) [5] will be used. Since a consumer does not always want to or is able to specify her preferences, we also introduce a graphical shopping interface (GSI) that enables the consumer to navigate through the products in a 2D map. The GSI system presents the user a map of a limited set of products of which the user has to select the product she prefers most. Based on this selection, a new map is constructed with products that are more similar to the selected product than in the previous map, and this process repeats itself.

The main contribution of this paper is that both the GRS and the GSI combine elements of existing recommendation and query techniques [26,8] on one hand with intelligent data visualisation techniques [5] for creating map based representations of recommendations on the other hand.

The remainder of this paper is organized as follows. The next section gives a brief overview of related work. In Section 3, we give a description of the methodology used with an emphasis on the measure of similarity and MDS. In Section 4, the graphical recommender system is introduced and in Section 5 we extend the GRS to the GSI. In Section 6, an application of both systems on MP3 players is given, followed by an evaluation of our approach. Finally, we give conclusions and recommendations.

## 2. Related work

Shafer, Konstan, and Riedl [28] de<sup>fi</sup>ne recommender systems as: “[Systems that] are used by e-commerce sites to suggest products to their consumers and to provide consumers with information to help them decide which products to purchase”[28, p.116]. These suggestions can be the same for each consumer, like top overall sellers on a site, but are often dependent on the user's preferences. These preferences can be derived in many ways, for example, using past purchases, navigation behavior, rating systems, or just by asking the user's preferences directly. There is a wide literature on recommender systems. For an overview we refer to [1,24].

In this paper, we limit ourselves to the recommender systems where a personalized recommendation is given. Recent overview papers [1,24] make a distinction between three types of recommender systems based on how the recommendation is computed.

• Content-based or knowledge based recommendation [6] systems suggest products that are similar to the product(s) the consumer liked in the past.

• Collaborative <sup>fi</sup>ltering [13] systems recommend products that other people with similar taste bought or liked in the past.

• Hybrid approaches [7] combine both content-based and collaborative methods.

Our systems belong to the category of content-based recommender systems. A large number of recommender systems in this group, including our approach, is based on case-based reasoning (CBR) [20] and follow the CBR recommendation cycle. In most CBR recommender systems (CBR-RS) the data used is the product catalog, that is, data describing products by their attribute values. The suggestion of products to recommend is then based on a similarity measure between the product descriptions in the catalog and a query given by the user or some sample product. These kind of systems have many similarities with k-nearest neighbor classi<sup>fi</sup>cation [10] and top-k querying [3,8]. Both techniques search for the k most similar items to a given query speci<sup>fi</sup>cation.

One speci<sup>fi</sup>c type of CBR-RS's are the systems that use recommendation by proposing [31] or inspiration seeking [26]. These systems, as does the GSI, present a limited number of sample products to the user of which the user can choose one. Then, based on the selection by the user, new products are recommended and the user can choose a new product. This approach is supported by the idea that people do not have well-de<sup>fi</sup>ned preferences in advance, but construct these preferences during the search process [4]. Recommender systems implementing this approach are, for instance, ExpertClerk [31], the comparison-based recommender system [21], SmartClient [25], and DieToRecs [26].

Other graphical applications using 2D maps, so-called inspiration interfaces, are used in the <sup>fi</sup>eld of industrial design engineering [17,32,33]. These applications are used to explore databases in an interactive way. At <sup>fi</sup>rst, a small set of items is shown in a 2D map. Then, the user can click in any point on the map and a new item that is closest to that point is added to the map. Our GSI differs from these systems by recommending more items at a time and doing so using the similarities and not the distances in the 2D map.

Also, interfaces have been developed based on a single product map [15,16] visualizing the complete product space. These maps are made using MDS [15] and non-linear principal components analysis [16]. In somewhat related <sup>fi</sup>elds like news [22], the web [9,35,37], music playlists [12,36], and image browsing [23] GUI's based on 2D visualizations have been created only using different visualization techniques like self-organizing maps [18], treemap [29], and other MDS methods like classical scaling [34] and Sammon mapping [27]. There are also a couple of commercial websites using 2D visualizations, such as Browse Goods<sup>1</sup>, Liveplasma<sup>2</sup>, Musicovery<sup>3</sup>, and Newsmap<sup>4</sup>. Also, the popular video website YouTube<sup>5</sup> has recently introduced a feature providing recommendations in a 2D map.

## 3. Methodology

An important part of the GSI is the similarity measure that is used to <sup>fi</sup>nd cases that are recommended to the user. This similarity measure will be used for the selection of products and for visualizing the similarities between all of the recommended products. The method used for creating these 2D maps is called multidimensional scaling (MDS) [5] which is discussed in Section 3.1.

To de<sup>fi</sup>ne the measure of similarity between products, we introduce some notation. Consider a data set D, which contains products {x }<sup>n</sup> having K attributes $\mathbf { x } _ { i } { = } ( x _ { i 1 } { , } x _ { i 2 } { \ldots } x _ { i K } ) .$ In most applications, these attributes have mixed types, that is, the attributes can be numerical, binary, or categorical. The most often used (dis)similarity measures, like the Euclidean distance, Pearson's correlation coef<sup>fi</sup>cient, and Jaccard's similarity measure, are only suited to handle one of these attribute types.

One similarity measure that can cope with mixed attribute types is the general coef<sup>fi</sup>cient of similarity proposed by Gower [14]. De<sup>fi</sup>ne the similarity $s _ { i j }$ between products i and j as the average of the non-missing similarity scores $s _ { i j k }$ over the K attributes

$$
s _ {i j} = \sum_ {k = 1} ^ {K} m _ {i k} m _ {j k} s _ {i j k} / \sum_ {k = 1} ^ {K} m _ {i k} m _ {j k},\tag{1}
$$

where $m _ { i k }$ is 0 when the value for attribute k is missing for product i and 1 when it is not missing.

The exact way of computing the similarity score $s _ { i j k }$ depends upon the type of attribute. However, Gower proposed that for all types it should have a score of 1 when the objects are completely identical on the attribute and a score of 0 when they are as different as possible. For numerical attributes, $s _ { i j k }$ is based on the absolute distance divided by the range, that is,

$$
s _ {i j k} ^ {N} = 1 - \frac {| x _ {i k} - x _ {j k} |}{\max (x _ {k}) - \min (x _ {k})},\tag{2}
$$

where $\mathbf { x } _ { k }$ is a vector containing the values of the kth attribute for all n products. For binary and categorical attributes the similarity score is de<sup>fi</sup>ned as

$$
s _ {i j k} ^ {C} = 1 \left(x _ {i k} = x _ {j k}\right),\tag{3}
$$

implying that objects having the same category value get a similarity score of 1 and 0 otherwise.

To use Gower's coef<sup>fi</sup>cient of similarity in our system, three adaptation have to be made. First, the similarity has to be transformed to a dissimilarity, so that it can be used in combination with MDS. Second, we want to have the possibility to make some variables more important than others. Therefore, we need to incorporate weights into the coef<sup>fi</sup>cient. Third, the in<sup>fl</sup>uence of categorical and binary attributes on the general coef<sup>fi</sup>cient turns out to be too large. The reason for this is that the similarity scores on binary or categorical attributes always have a score of 0 or 1 (that is, totally identical or totally different), whereas the similarity scores on numerical attributes almost always have a value between 0 and 1. Thus, the categorical attributes dominate the similarity measure. There is no reason to assume the categorical attributes are more important than numerical ones and we want to compensate for this. Therefore, we propose the following adaptations.

Both types of dissimilarity scores are normalized to have an average dissimilarity score of 1 between two different objects. Since the dissimilarity between the object and itself $\left( \delta _ { i i } \right)$ is excluded and $\delta _ { i j } = \delta _ { j i } ,$ , dissimilarities having $i { \geq } j$ are excluded from the sum without loss of generality. The numerical dissimilarity score becomes

$$
\delta_ {i j k} ^ {N} = \frac {\left| x _ {i k} - x _ {j k} \right|}{\left(\sum_ {i <   j} m _ {i k} m _ {j k}\right) ^ {- 1} \sum_ {i <   j} m _ {i k} m _ {j k} \left| x _ {i k} - x _ {j k} \right|}.\tag{4}
$$

The categorical dissimilarity score becomes

$$
\delta_ {i j k} ^ {C} = \frac {1 \left(x _ {i k} \neq x _ {j k}\right)}{\left(\sum_ {i <   j} m _ {i k} m _ {j k}\right) ^ {- 1} \sum_ {i <   j} m _ {i k} m _ {j k} 1 \left(x _ {i k} \neq x _ {j k}\right)}.\tag{5}
$$

Let C be the set of categorical attributes and N the set of numerical attributes. Then, the combined dissimilarity measure $\delta _ { i j }$ is de<sup>fi</sup>ned as

$$
\delta_ {i j} = \sqrt {\frac {\sum_ {k \in C} w _ {k} m _ {i k} m _ {j k} \delta_ {i j k} ^ {C} + \sum_ {k \in N} w _ {k} m _ {i k} m _ {j k} \delta_ {i j k} ^ {N}}{\sum_ {k = 1} ^ {K} w _ {k} m _ {i k} m _ {j k}}}.\tag{6}
$$

Here, a vector with weights w is incorporated to emphasize attributes differently. Note that these weights are applied to the normalized dissimilarity scores. This makes the effect of weighting independent of the original attribute scale, that is, a certain weight value has the same effect in increasing/decreasing an attribute's importance for all attributes.

In our application, the attribute weights w must be speci<sup>fi</sup>ed by the user. It is known from marketing literature, however, that setting sensible attribute weights is very dif<sup>fi</sup>cult, even for experts. Therefore, an ideal solution would be to estimate these attribute weights from choice data. This is a complex issue beyond the scope of this paper.

Note that we use the weights in a linear fashion that is equal for all products. In his paper, Gower [14] discussed several other weighting approaches that allow for differential weighting per product, such as hierarchical and resultweighting. In result-weighting, a weight depends on the speci<sup>fi</sup>c values of $x _ { i k }$ and $x _ { j k } ,$ implying that the weight is not the same for all products. Hierarchical weighting implies a nested structure of variables, which is not present in our data. Although they can be potentially useful, for reasons of simplicity we do not consider these weighting schemes.

In Eq. (6), the overall square root is taken, since these dissimilarities can be perfectly represented in a high dimensional Euclidean space, when there are no missing values [14]. In this case, the dissimilarities are city-block distances and taking the square root of city-block distances makes them Euclidean embeddable. We use Eq. (6) as dissimilarity measure in the remainder of this paper.

## 3.1. Multidimensional scaling

The dissimilarities discussed above are used in the GRS and GSI to create the 2D map where products are represented as points. A statistical technique for doing this is multidimensional scaling (MDS) [5]. Its aim is to <sup>fi</sup>nd a low dimensional Euclidean representation such that distances between pairs of points represent the dissimilarities as closely as possible. This objective can be formalized by minimizing the raw Stress function [19]

$$
\sigma_ {r} (\mathbf {Z}) = \sum_ {i <   j} \left(\delta_ {i j} - d _ {i j} (\mathbf {Z})\right) ^ {2},\tag{7}
$$

where the matrix Z is the $n \times 2$ coordinate matrix representing the n products in two dimensions, $\delta _ { i j }$ is the dissimilarity between objects i and j forming the symmetric dissimilarity matrix $\Delta ,$ and $\begin{array} { r } { d _ { i j } ( { \bf Z } ) = \big ( \sum _ { s = 1 } ^ { 2 } \big ( z _ { i s } - z _ { j s } \big ) ^ { 2 } \big ) ^ { 1 / 2 } } \end{array}$ is the Euclidean distance between row points i and j.

To minimize $\sigma _ { r } ( \mathbf { Z } ) ,$ , we use the SMACOF algorithm [11] based on majorization. One of the advantages of this method is that it is reasonably fast and that the iterations yield monotonically improved Stress values and the difference between subsequent coordinate matrices Z converges to zero [11], which is important when visualizing the iterations to the user by a smooth dynamic GRS and GSI.

## 4. Graphical recommender system

The <sup>fi</sup>rst system we introduce is the graphical recommender system (GRS). Based on a speci<sup>fi</sup>cation of an ideal product and importance weights for the different attributes, the GRS recommends a set of products most similar to the ideal product and shows them together with the ideal product in a 2D map to the user.

The input of the GRS is the vector of product attributes of the ideal product, $\mathbf { x } ^ { * }$ , and the weights of the attributes, w. Furthermore, we use the product catalog, that is, data set $D _ { * }$ The implementation of the GRS is as follows.

We start by computing the weighted dissimilarities $\delta _ { i ^ { * } }$ between $\mathbf { x } ^ { * }$ and all the products $\mathbf { x } _ { i }$ in data set D using the dissimilarity measure introduced in Section 3. This step leads to n values $\delta _ { i ^ { * } }$

Then, $p - 1$ products are selected that are most similar to $\mathbf { x } ^ { * }$ , by sorting the $\delta _ { i ^ { * } } { } ^ { \prime } s$ and selecting the <sup>fi</sup>rst $p - 1$ products. We combine $\bar { \mathbf { x } } ^ { * }$ and the $p - 1$ selected products in one data set $D ^ { * }$ . We use Eq. (6) again to compute all the mutual dissimilarities of the selected objects and the ideal product and gather the dissimilarities in the symmetric matrix $\Delta ^ { * }$ of size $p \times p$ . This dissimilarity matrix $\bar { \Delta ^ { * } }$ is the input for the multidimensional scaling algorithm discussed in Section 3.1. The algorithm returns the $p \times 2$ coordinate matrix Z which is used to create the 2D map.

## 5. Graphical shopping interface

To facilitate selection of products by consumers who do not have a clear idea about what they are looking for, we propose the graphical shopping interface (GSI). The idea is to let the consumer navigate through the complete product space in steps, where at each step a set of products is represented in a 2D map. In this 2D map, the user can select a product and then a new set of products, including the selected product, is produced and visualized by MDS.

The implementation of the GSI is not straightforward. The reason is that it is not trivial to <sup>fi</sup>nd a way to recommend products more similar to the selected product without over<sup>fi</sup>tting a single selection. We analyze three different approaches: a random system, a clustering system, and a hierarchical system.

The random system uses random selection to select a small set of products that will be shown to the user out of a larger set of products that are similar to the selected product. The <sup>fi</sup>rst iteration of the GSI is an initialization iteration. We refer to this iteration as iteration $t = 0$ . The input of the user is unknown in this iteration, because the <sup>fi</sup>rst input of the user will be given after this iteration. Therefore, the product set $D _ { t }$ in this iteration will contain the complete product catalog, that is, $D _ { 0 } = D .$ . Then, p products are selected at random (without replacement) from $D _ { 0 }$ and stored in the smaller set $D _ { 0 } ^ { * }$ . Using the dissimilarity metric proposed in Section $^ { 3 , }$ we compute the dissimilarity matrix ${ \boldsymbol { \Delta } } _ { 0 } ^ { * }$ , given $D _ { 0 } ^ { * }$ . With the use of MDS we then create a 2D map $\mathbf { Z } _ { 0 }$ containing these random selected products and show this to the consumer.

The process starts when the consumer selects one of the shown products. In every iteration, the selected product is treated as the new input $\mathbf { x } _ { t } ^ { * } .$ Then, we compute the dissimilarities between $\mathbf { x } _ { t } ^ { * }$ and all other products in D. Based on these dissimilarities we create a set $D _ { t }$ with the max $( p - 1 , \alpha ^ { t } n - 1 )$ ) most similar products, where the parameter α with 0<α≤1 determines how fast the data set selection is decreased each iteration. The smaller set $D _ { t } ^ { * }$ shown to the user, consists of product $\mathbf { x } _ { t } ^ { * }$ and $p - 1$ products that are randomly selected from the $D _ { t } .$ . We again compute dissimilarity matrix $\Delta _ { t } ^ { * }$ and create the 2D map $\mathbf { Z } _ { t }$ using MDS. The procedure terminates when $D ^ { * }$ does not change anymore. This happens when the size of $D ^ { * }$ has decreased to p and the same product is chosen as was chosen in the last iteration.

When we set $\alpha = 1 ,$ the system always returns a complete random selection at each stage and the user's input is almost completely ignored, that ${ \mathrm { i } } s ,$ only the selected product is kept and $p - 1$ new random products are positioned in a new 2D map together with the kept product. When α is lower, we have more con<sup>fi</sup>dence in the selection of the user, but we also more quickly decrease the variance in $D _ { t } .$ . The random system is summarized in Fig. 1.

A disadvantage of the random system is that is dif<sup>fi</sup>cult for the user to <sup>fi</sup>nd outlying products with it. There is only a small probability of selecting such a product in $D _ { 0 } ^ { * }$ and it is likely that this product is not in $D _ { t }$ the second time. For this reason, it can be advantageous to have the products selected in $D _ { t } ^ { * }$ represent the different groups of products in $D _ { t }$ . By decreasing the size of $D _ { t }$ each time these groups will become more similar to each other and <sup>fi</sup>nally become individual products.

The clustering system is quite similar to the random system, the only difference being that the random selection procedure is replaced by a clustering algorithm. In principle, every clustering algorithm can be used that can cluster a dissimilarity matrix. We use the average linkage method which is a hierarchical clustering method, yielding a complete tree (dendrogram) T of cluster solutions. Since this clustering method is based on a dissimilarity matrix, the dissimilarity matrix $\Delta _ { t }$ based on $D _ { t }$ is computed <sup>fi</sup>rst using Eq. (6). Then, the average linkage algorithm is performed on $\Delta _ { t }$ resulting in dendrogram $T _ { t \cdot }$ The system only uses the solution with p clusters $D _ { t } ^ { c } .$ . Each of the $p$ clusters is then represented by one prototypical product in the product set $D _ { t } ^ { * } .$ For an easy navigation, the product selected in the previous iteration will always represent the cluster it belongs to. For the other clusters, we determine the product with the smallest total dissimilarity to the other products in the cluster. De<sup>fi</sup>ne $\Delta ^ { c }$ as the dissimilarity matrix (with elements $\delta _ { i j } ^ { c } )$ between all products in cluster $D ^ { c } ,$ n<sup>c</sup> as the size of this cluster, and $i _ { c }$ as the index of the prototypical product, we can de<sup>fi</sup>ne this ideal index as follows

$$
i _ {c} = \arg \min _ {i} \sum_ {j = 1} ^ {n _ {c}} \delta_ {i j} ^ {c}.\tag{8}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
M. Kagie et al. / Decision Support Systems 46 (2008) 265-276   
procedure RANDOM_GSI $(D,p,\alpha)$ $D_0 = D$ .  
Generate random $D_0^* \subset D_0$ with size $p$   
Compute $\Delta_0^*$ given $D_0^*$ using (6).  
Compute $\mathbf{Z}_0$ given $\Delta_0^*$ using MDS.  
$t = 0$   
repeat  
$t = t + 1$ . Select a product $\mathbf{x}_t^*\in D_{t - 1}^*$ . Get $D_{t}\subset D$ containing $\max (p - 1,\alpha^{t}n - 1)$ products most similar to $\mathbf{x}_t^*$ using (6). Generate random $D_{t}^{*}\subset D_{t}$ with size $p - 1$ $D_{t}^{*} = D_{t}^{*}\cup \mathbf{x}_{t}^{*}$ Compute $\Delta_t^*$ given $D_{t}^{*}$ using (6). Compute $\mathbf{Z}_t$ given $\Delta_t^*$ using MDS. until $D_{t}^{*} = D_{t - 1}^{*}$   
end procedure
</div>

Fig. 1. GSI implementation using random selection.

The resulting product set $D _ { t } ^ { * }$ is used in the same way as in the random system to compute $\boldsymbol { \Delta } _ { t } ^ { * }$ and $\mathbf { Z } _ { t } .$ The clustering system is summarized in Fig. 2.

Clustering (and especially hierarchical clustering) becomes quite slow as the product space gets larger. Since $D _ { t }$ is interactively selected each time, the clustering has to be done each time as well. Therefore, our third implementation, the hierarchical system, does not create a set $D _ { t }$ each time, but uses only one hierarchical clustering result. We start by applying the average linkage algorithm to the complete product catalog $D _ { * }$ To do this, we <sup>fi</sup>rst compute dissimilarity matrix Δ using Eq. (6). We will use the dendrogram $T ,$ created by this clustering algorithm, to navigate through the product space. In the <sup>fi</sup>rst iteration (the initialization), we start by setting $T _ { 0 } \mathrm { = } T .$ An iteration starts at the root of $T _ { t \cdot }$ We will go down $T _ { t }$ until we <sup>fi</sup>nd the $p$ cluster solution. If this clustering does not exist, the largest possible clustering solution is chosen which is equal to the number of products in the previous selected cluster. This solution exists of $p$ clusters $D _ { t } ^ { c } ,$ where each of the $p$ clusters is represented by one prototypical product in the product set $D _ { t } ^ { * }$ . The procedure for determining the prototypical products is the same as in the clustering system. Then, the dissimilarity matrix $\boldsymbol { \Delta } _ { t } ^ { * }$ of $D _ { t } ^ { * }$ is computed using Eq. (6) and used as input for the MDS algorithm to compute the 2D representation $\mathbf { Z } _ { t } .$ When a product $\mathbf { x } _ { t } ^ { * }$ is selected from this map, the cluster it represents is used as the root of $T _ { t + 1 } .$ The procedure is terminated when a selected cluster only contains a single product. This product is the <sup>fi</sup>nal recommendation of the system.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
procedure CLUSTERING_GSI(D, p, α)

 $D_{0} = D$ .

Compute  $\Delta_{0}$  given  $D_{0}$  using (6).

Compute  $T_{t}$  given  $\Delta_{0}$  using average linkage.

Find p clustering solution in  $T_{0}$ .

Determine prototypical products of clusters using (8).

Store representation products in  $D_{0}^{*}$ .

Compute  $\Delta_{0}^{*}$  given  $D_{0}^{*}$  using (6).

Compute  $Z_{0}$  given  $\Delta_{0}^{*}$  using MDS.

t = 0.

repeat

 $t = t + 1$ .

Select a product  $x_{t}^{*} \in D_{t-1}^{*}$ .

Get  $D_{t} \subset D$  containing max(p - 1,  $\alpha^{t}n - 1$ ) products most similar to  $x_{t}^{*}$  using (6).

Compute  $\Delta_{t}$  given  $D_{t}$  using (6).

Compute  $T_{t}$  given  $\Delta_{t}$  using average linkage.

Find p clustering solution in  $T_{t}$ .

Determine representation products of clusters using (8).

Store prototypical products in  $D_{t}^{*}$ .

Compute  $\Delta_{t}^{*}$  given  $D_{t}^{*}$  using (6).

Compute  $Z_{t}$  given  $\Delta_{t}^{*}$  using MDS.

until  $D_{t}^{*} = D_{t-1}^{*}$ .

end procedure
</div>

Fig. 2. GSI implementation using clustering

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
procedure HIERARCHICAL_GSI(D, p)
    Compute  $\Delta$  given D using (6).
    Compute T given  $\Delta$  using average linkage.
    $T_{0} = T$ .
    t = 0.
    $n_{c} = size(D)$ .
repeat
    Find  $\min(n^{c}, p)$  clustering solution in  $T_{t}$ .
    Determine prototypical products of clusters using (8).
    Store prototypical products in  $D_{t}^{*}$ .
    Compute  $\Delta_{t}^{*}$  given  $D_{t}^{*}$  using (6).
    Compute  $Z_{t}$  given  $\Delta_{t}^{*}$  using MDS.
    Select  $x_{t}^{*} \in D_{t}^{*}$  en determine cluster  $D_{t}^{c}$  it represents.
    $n_{c} = size(D_{t}^{c})$ .
    $D_{t}^{c}$  is root of  $T_{t+1}$ .
    $t = t + 1$ .
until  $n^{c} \leq p$ .
end procedure
</div>

Fig. 3. GSI implementation using hierarchical clustering.

Note that there is no convergence parameter α in this approach. Since a cluster is selected every step and products outside this cluster are not considered anymore in the remainder of the recommendation procedure, this approach converges quickly to a recommended product. As a consequence, it may lead to worse recommendations. The hierarchical system is summarized in Fig. 3.

## 6. A prototype application to MP3 players

In this section, we show a prototype implementing both the GRS and GSI on a data set containing MP3 players. This data set consists of 22 attributes of 321 MP3-players collected from the Dutch website http://www.kelkoo.nl during June 2006. The data set is of a mixed type, which means that we have both categorical and numerical attributes and contains several missing values. An overview of these data is given in Table 1.

A prototype of our GUI is shown in Fig. 4. This prototype is available at http://people.few.eur.nl/kagie/gsi.html. The prototype is implemented as a Java Applet, which means that it can be used in a web environment. The interface uses three tabs that contain a 2D map and some buttons: The Navigate tab implementing the graphical shopping interface (GSI), the Direct Search tab implementing the graphical recommender system (GRS), and a Saved Products tab to save products in.

In a 2D map, each product is represented by a thumbnail picture. To add a selected product to the shopping basket the user presses the Save button represented by a shopping cart in the GSI or the GRS tab. The Recommend (or play) button uses the selected product for the next step in the GSI and by pressing the same button in the GRS tab recommendations are given based on the ideal values for the product attributes and weights speci<sup>fi</sup>ed by the user. The ideal product is represented by the symbol ⊗ on the GRS map. The products in the Saved Products map are represented using MDS as in the other two maps. With the Delete button saved products can be removed from this map. A panel at the right shows the product attributes of a selected product together with a picture of this product.

Furthermore, there is a Preferences tab. In this tab the user can specify the weights that are used in the dissimilarity calculation of the GRS and GSI, that is, how important the attributes are. Also, the user can deselect certain attributes, which means that their weights are set to 0. When changes are made in this tab, the 2D maps are immediately adapted.

Description of the MP3-player data set

<table><tr><td>Categorical characteristics</td><td>Missing</td><td>Levels (frequency)</td><td></td><td></td></tr><tr><td>Brand</td><td>0</td><td>Creative (53), iRiver (25), Samsung (25), Cowon (22), Sony (19), and 47 other brands (207)</td><td></td><td></td></tr><tr><td>Type</td><td>11</td><td>MP3 Player (254), Multimedia Player (31) USB key (25)</td><td></td><td></td></tr><tr><td>Memory type</td><td>0</td><td>Integrated (231), Hard Disc (81), Compact Flash (8), Secure Digital (1)</td><td></td><td></td></tr><tr><td>Radio</td><td>9</td><td>Yes (170), No (139), Optional (3)</td><td></td><td></td></tr><tr><td>Audio format</td><td>4</td><td>MP3 (257), ASF (28), AAC (11), Ogg Vorbis (9), ATRAC3 (5), and 4 other formats (6)</td><td></td><td></td></tr><tr><td>Interface</td><td>5</td><td>USB 2.0 (242), USB 1.0/1.1 (66), Firewire (6), Bluetooth (1), Parallel (1)</td><td></td><td></td></tr><tr><td>Power supply</td><td>38</td><td>AAA×1 (114), Lithium ion (101), Lithium polymer (45), AA×1 (17), AAA×2 (4), Ni Mh (3)</td><td></td><td></td></tr><tr><td>Remote control</td><td>9</td><td>No (289), In Cable (13), Wireless (10)</td><td></td><td></td></tr><tr><td>Color</td><td>281</td><td>White (7), Silver (5), Green (5), Orange (4), Purple (4), Red (4), Pink (4), Black (4), Blue (3)</td><td></td><td></td></tr><tr><td>Headphone</td><td>15</td><td>Earphone (290), Chain earphone (8), Clip-on earphone (2), Earphone with belt (2), No earphone (2), Minibelt earphone (1), Collapsible earphone (1)</td><td></td><td></td></tr><tr><td>Numerical characteristics</td><td></td><td>Missing</td><td>Mean</td><td>SD</td></tr><tr><td>Memory size (MB)</td><td></td><td>0</td><td>6272.10</td><td>13738.00</td></tr><tr><td>Screen size (inch)</td><td></td><td>264</td><td>2.16</td><td>1.04</td></tr><tr><td>Screen colors (bits)</td><td></td><td>0</td><td>2.78</td><td>5.10</td></tr><tr><td>Weight (grams)</td><td></td><td>66</td><td>83.88</td><td>84.45</td></tr><tr><td>Radio presets</td><td></td><td>9</td><td>3.06</td><td>7.84</td></tr><tr><td>Battery life (hours)</td><td></td><td>40</td><td>18.63</td><td>12.56</td></tr><tr><td>Signal-to-noise ratio (dB)</td><td></td><td>247</td><td>90.92</td><td>7.32</td></tr><tr><td>Equalizer presets</td><td></td><td>0</td><td>2.60</td><td>2.22</td></tr><tr><td>Height (cm)</td><td></td><td>28</td><td>6.95</td><td>2.48</td></tr><tr><td>Width (cm)</td><td></td><td>28</td><td>5.57</td><td>2.82</td></tr><tr><td>Depth (cm)</td><td></td><td>28</td><td>2.18</td><td>4.29</td></tr><tr><td>Screen resolution (pixels)</td><td></td><td>246</td><td>31415.00</td><td>46212.00</td></tr></table>

The data set describes 321 MP3-players using 22 product attributes.

![](/api/attachments/4DXHW7QD/fulltext/images/186b8a793bd38c37eb2de9bf338ae681c0625399c0e073539c4336972845c0b4.jpg)  
Fig. 4. Screenshot of the graphical user interface of the prototype of the GSI for MP3-players.

The transition between two steps in the GSI is implemented in a smooth way. After the selection of a product by the user, the new products are added to the map at random positions. Then, the map is optimized using MDS. This optimization is shown to the user. When the optimization has converged, the old products are gradually made less important (using a weighted version of MDS) until they have no in<sup>fl</sup>uence anymore. Finally, the old products are removed and the map of new products is optimized. This implementation yields smooth visual transitions, which are important for an effective GUI.

Fig. 5 shows an example of a 2D map created by the GRS. The description of the ideal product is shown in Table 2. The MP3-players closest to the ideal product speci<sup>fi</sup>cation are the Samsung YH-820 and the Maxian MP2220 positioned above and below the ideal product respectively. It is perhaps surprising that the distance between these two products is one of the largest in the map. However, when we have a closer look, we see that although both MP3-players are quite similar to our ideal product description, they are quite different from each other. The Samsung YH-820 is a small and light MP3 player with limited memory size and a smaller screen than we wanted. On the other hand, the Maxian has a large screen and memory size, but it is also larger and heavier than our ideal product. The Samsung YH-925 and the 20 GB versions of the Cowon iAudio and the Samsung YH-J70 are all MP3-players having a memory of 20 GB as we wanted, but having worse screens than the Maxian. Conversely, these players are somewhat smaller and lighter than the Maxian. The 30 GB versions of the Cowon iAudio and the Samsung YH-J70 only differ in memory size from the 20 GB versions. Therefore, these MP3-players are visualized somewhat farther from the ideal product than the 20 GB versions.

## 7. Evaluation of the graphical shopping interface

To test our approach, the MP3 players data introduced in the previous section are used. We study the quality of the 2D maps by considering the Stress values. Through a simulation study we evaluate how easily a consumer can <sup>fi</sup>nd the product she wants using the GSI. Finally, we have conducted a survey among 71 subjects to test the usability of the GSI.

Representing recommended solutions in a 2D map might only be an improvement when the 2D representations are of a suf<sup>fi</sup>cient quality. Solutions with a low Stress value represent, at least technically, the products in a good way. One should keep in mind that a low Stress value is merely a necessary condition for a usable system, it is not a suf<sup>fi</sup>cient one. Since we also like to compare solutions with a different number of products, Stress is normalized by dividing by the sum of squared dissimilarities, that is,

$$
\sigma_ {n} = \frac {\sum_ {i <   j} \left(\delta_ {i j} - d _ {i j} (\mathbf {Z})\right) ^ {2}}{\sum_ {i <   j} \delta_ {i j} ^ {2}}.\tag{9}
$$

This normalized Stress can be interpreted as the proportion of the unexplained sum-of-squares of the dissimilarities [5].

To estimate the average quality of a <sup>fi</sup>t in the GSI is practically impossible, because of the interactivity and randomness in the system. However, we can say something about the goodness of the representations in the GRS. Since the user has much freedom in specifying her ideal product, there is a very large number of possible plots in practice. We use a leave-oneout method to approximate the quality of the plots. Each time, we pick one product from the data set as the ideal product of the user and we use the other products as our product catalog. All attributes are used to compute the dissimilarities and all weights are set to 1. Then, the p−1 most similar products to this ideal product are selected and a 2D map of these p products is created using MDS. This procedure is repeated, until each product has functioned once as an ideal product description. This overall procedure is done for p=2 until p=10. The results for the average normalized Stress values are shown in Table 3.

![](/api/attachments/4DXHW7QD/fulltext/images/967911ae18c18e5f7cd8c84820fd12fa6d2bf8e8d3d9f31c4abe145bbefc59c2.jpg)  
Fig. 5. An example of the GRS.

It is no surprise that solutions with only two products have a Stress of (almost) zero, since there is only one dissimilarity in that case that can always be perfectly scaled on a line. Also the solutions with three points have an average Stress value very close to zero. When we increase p, the Stress values increase, as may be expected because the problem gets more dif<sup>fi</sup>cult. Since this increase seems almost linear, it is hard to identify the ideal product set size. If one wants near perfect solutions, p should be set to 3, but a map of three products is not very informative. For larger p, the Stress values are still acceptable, even for p = 10, 96% of the sum-of-squares in the dissimilarities is explained by the distances in the 2D map. Obviously, the quality of the solutions can be better or worse, when using different product catalogs.

Apart from the quality of the 2D representations, the navigation aspect was tested in the different implementations of the GSI. In an ideal system, the user will always <sup>fi</sup>nd the product she likes most in a small number of steps. We expect that there will be a trade-off between the number of steps that is necessary to <sup>fi</sup>nd the product and the probability that the consumer will <sup>fi</sup>nd the product she likes.

Table 2  
Description of ideal product used in Fig. 5

<table><tr><td>Characteristic</td><td>Value</td><td>Characteristic</td><td>Value</td></tr><tr><td>Brand</td><td>Samsung</td><td>Screen size</td><td>1.8 in.</td></tr><tr><td>Type</td><td>Multimedia</td><td>Screen colors</td><td>18 bits</td></tr><tr><td>Memory type</td><td>Hard-disk</td><td>Weight</td><td>100 g</td></tr><tr><td>Radio</td><td>No</td><td>Radio presets</td><td>0</td></tr><tr><td>Audio format</td><td>MP3</td><td>Battery life</td><td>12 h</td></tr><tr><td>Interface</td><td>USB2.0</td><td>Signal-to-noise</td><td>95 dB</td></tr><tr><td>Power supply</td><td>Lithium Ion</td><td>Equalizer presets</td><td>5</td></tr><tr><td>Remote control</td><td>No</td><td>Height</td><td>8 cm</td></tr><tr><td>Color</td><td>Black</td><td>Width</td><td>4 cm</td></tr><tr><td>Headphone</td><td>Earphone</td><td>Depth</td><td>1 cm</td></tr><tr><td>Memory size</td><td>20 GB</td><td>Screen resolution</td><td>60,000 px</td></tr></table>

Table 3  
Normalized Stress values for the experiments to determine the quality of the 2D representations in the GRS

<table><tr><td>p</td><td>Mean normalized stress</td></tr><tr><td>2</td><td> $3.36 \cdot 10^{-32}$ </td></tr><tr><td>3</td><td> $3.13 \cdot 10^{-4}$ </td></tr><tr><td>4</td><td> $5.77 \cdot 10^{-3}$ </td></tr><tr><td>5</td><td> $1.21 \cdot 10^{-2}$ </td></tr><tr><td>6</td><td> $1.96 \cdot 10^{-2}$ </td></tr><tr><td>7</td><td> $2.63 \cdot 10^{-2}$ </td></tr><tr><td>8</td><td> $3.16 \cdot 10^{-2}$ </td></tr><tr><td>9</td><td> $3.62 \cdot 10^{-2}$ </td></tr><tr><td>10</td><td> $4.05 \cdot 10^{-2}$ </td></tr></table>

Table 7  
Table 5  
Results for different speci<sup>fi</sup>cations of the random system

<table><tr><td>p</td><td>α</td><td>Successes (%)</td><td>In 5 steps (%)</td><td>Average number of steps</td></tr><tr><td rowspan="4">4</td><td>0.2</td><td>16.8</td><td>16.8</td><td>5.02</td></tr><tr><td>0.4</td><td>29.3</td><td>19.3</td><td>6.38</td></tr><tr><td>0.6</td><td>41.7</td><td>10.0</td><td>9.12</td></tr><tr><td>0.8</td><td>56.1</td><td>5.9</td><td>15.99</td></tr><tr><td rowspan="4">6</td><td>0.2</td><td>29.3</td><td>28.7</td><td>4.77</td></tr><tr><td>0.4</td><td>42.7</td><td>34.9</td><td>5.83</td></tr><tr><td>0.6</td><td>52.7</td><td>17.1</td><td>8.01</td></tr><tr><td>0.8</td><td>70.1</td><td>10.9</td><td>13.12</td></tr><tr><td rowspan="4">8</td><td>0.2</td><td>43.0</td><td>42.7</td><td>4.34</td></tr><tr><td>0.4</td><td>47.0</td><td>43.6</td><td>5.29</td></tr><tr><td>0.6</td><td>66.4</td><td>30.5</td><td>6.96</td></tr><tr><td>0.8</td><td>80.1</td><td>16.2</td><td>11.22</td></tr><tr><td rowspan="4">10</td><td>0.2</td><td>46.4</td><td>46.4</td><td>4.09</td></tr><tr><td>0.4</td><td>58.9</td><td>56.7</td><td>4.82</td></tr><tr><td>0.6</td><td>70.4</td><td>37.1</td><td>6.27</td></tr><tr><td>0.8</td><td>83.8</td><td>19.9</td><td>9.92</td></tr></table>

To evaluate the navigation aspect of the different systems in a simulation, some assumptions need to be made about the navigation behavior of the user. First, we assume that the consumer implicitly or explicitly can specify what her ideal product looks like in terms of its attributes. Second, we assume that the user compares products using the same dissimilarity measure as the system uses (using all attributes and all weights set to 1). Finally, it is assumed that in each step the consumer chooses the product that is most similar to the ideal product of the consumer. Note that we only evaluate the search algorithm in this way and not the complete interface, since the results would have been the same when the results were shown in a list.

We use a leave-one-out procedure to select the ideal product descriptions of the user. A random ideal product description is not used, since such a procedure will create a lot of ideal products that do not exist in reality. Each time, one product is selected as the ideal product of the consumer and all other products are used as the product catalog. We repeat this until every product is left out once. We evaluate the three different implementations (the random, the clustering, and the hierarchical system) with p set to 4, 6, 8, and 10. For the random and clustering system we also vary the parameter α by setting it to the values 0.2, 0.4, 0.6, and 0.8. Before starting a single experiment, we determine which product in the product catalog is most similar to the product we left out. During each step in a single experiment, we use the assumptions above to compute the product the user will select. We stop when the most similar product is in D<sup>⁎</sup> that is shown to the user or when the system terminates. A quite similar evaluation procedure was used in [21].

Results for different speci<sup>fi</sup>cations of the clustering system

<table><tr><td>p</td><td>α</td><td>Successes (%)</td><td>In 5 steps (%)</td><td>Average number of steps</td></tr><tr><td rowspan="4">4</td><td>0.2</td><td>14.6</td><td>14.6</td><td>4.85</td></tr><tr><td>0.4</td><td>20.3</td><td>12.2</td><td>6.68</td></tr><tr><td>0.6</td><td>19.3</td><td>8.7</td><td>8.90</td></tr><tr><td>0.8</td><td>13.7</td><td>10.0</td><td>7.83</td></tr><tr><td rowspan="4">6</td><td>0.2</td><td>22.1</td><td>21.2</td><td>4.83</td></tr><tr><td>0.4</td><td>32.7</td><td>27.1</td><td>6.17</td></tr><tr><td>0.6</td><td>44.9</td><td>19.0</td><td>8.30</td></tr><tr><td>0.8</td><td>25.9</td><td>11.5</td><td>9.10</td></tr><tr><td rowspan="4">8</td><td>0.2</td><td>31.5</td><td>29.9</td><td>4.57</td></tr><tr><td>0.4</td><td>38.9</td><td>35.5</td><td>5.38</td></tr><tr><td>0.6</td><td>60.4</td><td>25.6</td><td>7.34</td></tr><tr><td>0.8</td><td>45.8</td><td>13.7</td><td>10.20</td></tr><tr><td rowspan="4">10</td><td>0.2</td><td>39.6</td><td>38.9</td><td>4.34</td></tr><tr><td>0.4</td><td>50.5</td><td>45.5</td><td>5.04</td></tr><tr><td>0.6</td><td>72.6</td><td>29.6</td><td>6.40</td></tr><tr><td>0.8</td><td>68.2</td><td>16.2</td><td>11.02</td></tr></table>

Table 6  
Results for different speci<sup>fi</sup>cations of the hierarchical system

<table><tr><td>p</td><td>Successes (%)</td><td>In 5 steps (%)</td><td>Average number of steps</td></tr><tr><td>4</td><td>47.4</td><td>11.5</td><td>8.03</td></tr><tr><td>6</td><td>47.7</td><td>18.4</td><td>5.69</td></tr><tr><td>8</td><td>48.9</td><td>24.6</td><td>5.02</td></tr><tr><td>10</td><td>52.3</td><td>38.0</td><td>4.10</td></tr></table>

For the different systems and speci<sup>fi</sup>cations Tables 4, 5, and 6 show the percentages of success, the percentage of successes during the <sup>fi</sup>rst <sup>fi</sup>ve steps of the process, and the average number of steps the system uses before it stops. The random system in Table 4 performs better for larger p as expected: the percentage of successes is higher and the average number of steps lower. As the quality of MDS representations reduces with increasing p, it becomes more dif<sup>fi</sup>cult for the user to get an overview of the product space. Also, there is a trade-off between the number of steps necessary to <sup>fi</sup>nd a product and the probability to <sup>fi</sup>nd the product. For example, a random system with p=10 and α=0.8 <sup>fi</sup>nds the correct product in 84% of the cases, but needs on average almost 10 steps. In this case, after 5 steps in only 20% of the cases is the correct product found. However, a system with p=10 and α=0.4 has a success after 5 steps in 57% of the cases, but the total success rate is 59%. The average number of steps for this system is also 4.8.

Proportions of cases that the ranking of the recommended product was in the speci<sup>fi</sup>ed ranges for the random system

<table><tr><td rowspan="2">p</td><td rowspan="2">α</td><td colspan="8">Ranking ranges</td></tr><tr><td>1(%)</td><td>≤2(%)</td><td>≤3(%)</td><td>≤5(%)</td><td>≤10(%)</td><td>≤25(%)</td><td>≤50(%)</td><td>≤100(%)</td></tr><tr><td rowspan="4">4</td><td>0.2</td><td>16.8</td><td>24.6</td><td>29.9</td><td>36.5</td><td>47.0</td><td>66.7</td><td>84.4</td><td>95.0</td></tr><tr><td>0.4</td><td>29.3</td><td>36.5</td><td>42.4</td><td>49.5</td><td>60.1</td><td>78.5</td><td>91.0</td><td>99.4</td></tr><tr><td>0.6</td><td>41.7</td><td>50.5</td><td>58.9</td><td>64.2</td><td>75.7</td><td>87.9</td><td>94.4</td><td>100.0</td></tr><tr><td>0.8</td><td>56.1</td><td>67.3</td><td>73.2</td><td>80.4</td><td>89.4</td><td>96.0</td><td>98.4</td><td>99.7</td></tr><tr><td rowspan="4">6</td><td>0.2</td><td>29.3</td><td>40.8</td><td>45.2</td><td>49.2</td><td>60.4</td><td>75.1</td><td>86.6</td><td>96.0</td></tr><tr><td>0.4</td><td>42.7</td><td>50.5</td><td>57.9</td><td>64.5</td><td>74.1</td><td>88.5</td><td>96.0</td><td>97.8</td></tr><tr><td>0.6</td><td>52.7</td><td>64.8</td><td>69.2</td><td>75.7</td><td>84.1</td><td>91.9</td><td>96.9</td><td>97.8</td></tr><tr><td>0.8</td><td>70.1</td><td>80.1</td><td>82.2</td><td>86.3</td><td>94.1</td><td>97.8</td><td>99.7</td><td>100.0</td></tr><tr><td rowspan="4">8</td><td>0.2</td><td>43.0</td><td>54.8</td><td>59.5</td><td>64.5</td><td>75.4</td><td>89.1</td><td>95.3</td><td>98.8</td></tr><tr><td>0.4</td><td>47.0</td><td>58.6</td><td>63.9</td><td>71.3</td><td>77.3</td><td>90.0</td><td>94.7</td><td>98.1</td></tr><tr><td>0.6</td><td>66.4</td><td>76.0</td><td>79.4</td><td>84.7</td><td>91.0</td><td>96.6</td><td>97.5</td><td>98.8</td></tr><tr><td>0.8</td><td>80.1</td><td>87.2</td><td>91.0</td><td>93.2</td><td>97.5</td><td>99.4</td><td>99.4</td><td>99.4</td></tr><tr><td rowspan="4">10</td><td>0.2</td><td>46.4</td><td>56.1</td><td>60.8</td><td>67.0</td><td>79.8</td><td>92.5</td><td>96.6</td><td>99.1</td></tr><tr><td>0.4</td><td>58.9</td><td>70.4</td><td>74.8</td><td>80.4</td><td>91.0</td><td>95.3</td><td>98.8</td><td>100</td></tr><tr><td>0.6</td><td>70.4</td><td>76.0</td><td>81.6</td><td>87.5</td><td>93.2</td><td>97.2</td><td>98.4</td><td>98.8</td></tr><tr><td>0.8</td><td>83.8</td><td>89.7</td><td>92.2</td><td>93.8</td><td>96.0</td><td>98.8</td><td>99.1</td><td>99.1</td></tr></table>

Table 8  
Proportions of cases that the ranking of the recommended product in the speci<sup>fi</sup>ed ranges for the hierarchical system

<table><tr><td rowspan="2">P</td><td colspan="8">ranking ranges</td></tr><tr><td>1 (%)</td><td>≤2 (%)</td><td>≤3 (%)</td><td>≤5 (%)</td><td>≤10 (%)</td><td>≤25 (%)</td><td>≤50 (%)</td><td>≤100 (%)</td></tr><tr><td>4</td><td>47.4</td><td>56.4</td><td>64.2</td><td>71.3</td><td>77.6</td><td>85.4</td><td>89.7</td><td>95.6</td></tr><tr><td>6</td><td>47.7</td><td>55.1</td><td>62.3</td><td>70.1</td><td>76.0</td><td>85.4</td><td>90.3</td><td>95.6</td></tr><tr><td>8</td><td>48.9</td><td>56.4</td><td>62.3</td><td>70.4</td><td>77.3</td><td>86.9</td><td>94.1</td><td>97.5</td></tr><tr><td>10</td><td>52.3</td><td>58.6</td><td>67.9</td><td>74.8</td><td>81.6</td><td>90.0</td><td>93.8</td><td>98.8</td></tr></table>

The clustering systems perform overall worse than the random systems and seem, therefore, not to be an alternative. However, the hierarchical systems, especially the one with p=10, show similar performance as the random systems with a small α.

Tables 4, 5, and 6 only showed the success rates, but did not say anything about the cases where the most similar product was not recommended to the user. Therefore, we have also counted how many times the second, third etc. most similar product was recommended. This information is summarized for the random and hierarchical system in Tables 7 and 8. They show that many misrecommendations of the systems are recommendations of products that are quite similar to the ideal product. Looking at the top 5 of most similar products, these products are recommended in up to 94% of the cases to the consumer. In many systems that desire only a small number of steps, like the hierarchical system, products 2 until 5 are recommended in one <sup>fi</sup>fth of the cases to the user. In many cases, these products have a not much higher dissimilarity than the most similar product and in some cases their dissimilarity is the same. Therefore, recommending one of these products instead of the most similar one, will not make the recommendation much worse.

Since a simulation study only shows limited theoretical results, we also performed a usability study to get opinions of potential users on the GSI and to <sup>fi</sup>nd directions for improvement of the GSI. The usability study was carried out by means of a web survey in which the GSI was integrated and was <sup>fi</sup>lled out by the respondents in the controlled environment of a behavioral lab at Erasmus University Rotterdam. The 71 respondents who <sup>fi</sup>lled in the questionnaire were mainly business or psychology students at Erasmus University Rotterdam.

The respondents were asked to perform two tasks with both the GSI and a traditional interface we developed ourselves. This interface enables a user to restrict attribute values and displays the results in a list. This interface is available at http://people.few.eur.nl/kagie/selectioninterface. htm. In total there were four tasks and these were randomly assigned to the two interfaces for each user. Also, the order in which the users had to use both interfaces was randomized.

In the usability study, we used an implementation of the random GSI system, since this implementation performed best in the simulation study. The system parameters were set to p=8 and α=0.5. During the study the GRS tab was not incorporated in the interface, so that only the GSI could be used to perform the tasks.

After carrying out their shopping tasks, the respondents were asked to rate the satisfaction with the product that was chosen on a 5-point scale. A t-test of these data showed that there was no signi<sup>fi</sup>cant difference in satisfaction between the two interfaces, despite the fact that all users were far more familiar with the traditional interface than with the GSI. The tasks took a little more time when the GSI was used than when the traditional interface was used. We suspect that one reason for this is that users were still learning how to use the GSI.

Furthermore, the survey asked the participants for qualitative feedback regarding the GSI. The weaknesses of the GSI that were reported can be divided in two subsets. The <sup>fi</sup>rst set of weaknesses concerns the perceived complexity of the GSI. For example, some users found it dif<sup>fi</sup>cult to specify weights on the preferences tab, or found the GSI to be confusing as a whole. We suspect that these weaknesses are partially caused by limited familiarity with the GSI. The other set of weaknesses sometimes mentioned by respondents were caused by functionality that was missing in the evaluated prototype of the GSI. For instance, users missed a way to restrict the search space to a subset of products using a crisp query and the possibility of a text search.

As strengths of the GSI, the respondents reported the following aspects. First of all, many users mentioned that they found the GSI more fun to use than the traditional interface. Another positive aspect of the GSI that was mentioned was that people felt to have a better overview of the presented products, since the GSI repeatedly represents a small number of products in an organized map. Finally, some users liked it that the GSI suggested products that were useful, but previously unknown to the user.

## 8. Conclusions and discussion

In this paper, we presented two recommender systems which both use 2D maps to represent products in. Products that are similar to each other, based on their product attributes, are represented close to each other in the 2D representation. The difference between the two systems is that the GRS uses explicit input from the user, whereas the GSI can be used to navigate through the product space. Both were combined in a prototype application for MP3 players.

Some simulation tests were performed to evaluate the quality of the 2D representations and the navigation behavior in the different implementations of the GSI. The <sup>fi</sup>rst type of test showed that the quality of the 2D representations in the GRS is acceptable at least up to 2D maps with 10 products, but as expected the quality of the representations became less when p was increased. The navigation tests showed that there is a trade-off between the number of steps a user needs to <sup>fi</sup>nd the best product in a certain implementation of the GSI and the probability that the user will <sup>fi</sup>nd the best product. Results of the implementation with a clustering in each step were worse than both the random system and the hierarchical system, implying that the clustering method is not good enough to be applied in practice. To be quite certain that the best product eventually will be found, the random system with a high value for α should be preferred. If a high probability of successes in the <sup>fi</sup>rst few steps is preferred, then one should choose a random system with a low α or a hierarchical system.

A usability study was performed, which showed that people were equally satis<sup>fi</sup>ed with the products they chose in four tasks using the GSI as they were when using a traditional interface, with which they were more familiar. Reported weaknesses of the GSI were the relative high complexity and the lack of some functionality. We expect that the experienced complexity is partially caused by the unfamiliarity with the system. The lack of functionality might be solved by integrating parts of more traditional systems in the GSI, such as crisp selection and search options. Strengths of the GSI that were mentioned where the fun-factor, good representation of products, and the recommendation of previously unknown products.

Both systems show that it is possible to combine 2D product representations with recommender systems. However, several possibilities remain for extending and possibly improving the systems. Besides some practical improvements that were mentioned by users during the usability study, such as the possibility to preselect a subset of products, there are also some other interesting extensions that can be made.

The <sup>fi</sup>rst extension would be to include user or rating data. The user data could contain user account information, which means that the similarity between users is used in the recommendation process. The ratings could be given directly by the user or can be based on saved or purchased products. When product ratings are incorporated in the recommender system the weights in the dissimilarity measure can be learned by the system for the total consumer population or even for individual consumers. In a CBR-RS for traveling [2], for example, a weighting approach based on frequencies of features previously used in a query was used.

The GSI can also be further improved by not only allowing the consumer to select a product, but by allowing the consumer to select any point on the map. With the use of external unfolding [5] an invisible product can be found that is closest to the selected point and used in the next iteration. This technique is, for example, used in an application to compare roller skates in [33].

## Acknowledgements

We thank Huub van der Wart and Duy Ahn Pham for the collection of the data, the usability study participants for taking part in the study, and three anonymous reviewers for their helpful comments.

## References

[1] G. Adomavicius, A. Tuzhilin, Towards the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[2] B. Arslan, F. Ricci, N. Mirzadeh, A. Venturini, A dynamic approach to feature weighting, Management Information Systems 6 (2002) 999–1008.

[3] A. Ayanso, P.B. Goes, K. Mehta, A practical approach for ef<sup>fi</sup>ciently answering top-k relational queries, Decision Support Systems 44 (2007) 326–349.

[4] J.R. Bettman, M.F. Luce, J.W. Payne, Constructive consumer choice processes, Journal of Consumer Research 25 (3) (1998) 187–217.

[5] I. Borg, P.J.F. Groenen, Modern Multidimensional Scaling, Springer Series in Statistics, 2nd ed., Springer, New York, 2005.

[6] R. Burke, Knowledge based recommender systems, in: J.E. Daily, A. Kent, H. Lancour (Eds.). Encyclopedia of Library and Information Science, vol. 69, Supplement 32, Marcel Dekker, New York, 2000.

[7] R. Burke, Hybrid recommender systems: survey and experiments, User Modeling and User-Adapted Interaction 12 (2002) 331–370.

[8] S. Chaudhuri, L. Gravano, Evaluating top-k selection queries, in: M.P. Atkinson M.E. Orlowska, P. Valduriez, S.B. Zdonik, M.L. Brodie (Eds.), Proceedings of the 25th VLDB Conference, Morgan Kaufmann, 1999, pp. 397–410.

[9] W. Chung, A. Bonillas, G. Lain, W. Xi, H. Chen, Supporting non-English Web searching: an experiment on the Spanish business and the Arabic medical intelligence portals, Decision Support Systems 42 (2006) 1697–1714.

[10] T. Cover, P. Hart, Nearest neighbor pattern classi<sup>fi</sup>cation, IEEE Transac tions on Information Theory 13 (1) (1967) 21–27.

[11] J. De Leeuw, Convergence of the majorization method for multidimensional scaling, Journal of Classi<sup>fi</sup>cation 5 (1988) 163–180.

[12] J. Donaldson, Music recommendation mapping and interface based on structural network entropy, in: V. Oria, A. Elmagarmid, F. Lochovsky, Y. Saygin (Eds.), Proceedings of the 23rd International Conference on Data Engineering Workshops, IEEE Computer Society, 2007, pp. 811–817.

[13] D. Goldberg, D. Nichols, B.M. Oki, D. Terry, Using collaborative <sup>fi</sup>ltering to weave an information tapestry, Communications of the ACM 35 (12) (1992) 61–70.

[14] J.C. Gower, A general coef<sup>fi</sup>cient of similarity and some of its properties, Biometrics 27 (1971) 857–874

[15] M. Kagie, M. Van Wezel, P.J.F. Groenen, Online shopping using a two dimensional product map, in: G. Psaila, R. Wagner (Eds.), E-Commerce and Web Technologies; 8th International Conference, EC-Web 2007. Proceedings., vol. 4655 of Lecture Notes in Computer Science, Springer, Heidelberg, 2007, pp. 89–98.

[16] M. Kagie, M. Van Wezel, P.J.F. Groenen, An online shopping interface based on a joint product and attribute category map, Proceedings of IUI Workshop on Recommendation and Collaboration ReColl 2008, 2008.

[17] I. Keller, MDS-i for 1 to 1 e-commerce: a position paper, Proceedings of the CHI 2000 Workshop on 1-to-1 E-commerce, 2000.

[18] T. Kohonen, Self-Organizing Maps, Springer Series in Information Sciences, 3rd ed.Springer, New York, 2001.

[19] J.B. Kruskal, Multidimensional scaling by optimizing goodness of <sup>fi</sup>t to a nonmetric hypothesis, Psychometrika 29 (1) (1964) 1–27.

[20] F. Lorenzi, F. Ricci, Case-based recommender systems: a unifying view, in: B. Mobasher, S.S. Anand (Eds.), Intelligent Techniques for Web Personalization, vol. 3169 of Lecture Notes in Computer Science, Springer, Heidelberg, 2005, pp. 89–113.

[21] L. McGinty, B. Smyth, Comparison-based recommendation, in: S. Craw, A. Preece (Eds.), Advanced in Case-Based Reasoning; 6th European Conference, ECCBR 2002. Proceedings, vol. 2416 of Lecture Notes in Computer Science, Springer, Heidelberg, 2002, pp. 731–737.

[22] T.-H. Ong, H. Chen, W. Sung, B. Zhu, Newsmap: a knowledge map fo online news, Decision Support Systems 39 (2005) 583–597.

[23] Z. Pečenović, M.N. Do, M. Vetterli, P. Pu, Integrated browsing and searching of large image collections, in: G. Goos, J. Hartmanis, J. van Leeuwen (Eds.), Advances in Visual Information Systems: 4th International Conference, VISUAL 2000. Proceedings., vol.1929 of Lecture Notes in Computer Science, Springer, Heidelberg, 2000, pp. 173–206.

[24] B. Prasad, Intelligent techniques for e-commerce, Journal of Electronic Commerce Research 4 (2) (2003) 65–71.

[25] P.H.Z. Pu, P. Kumar, Evaluating example-based search tools, Proceedings of the 5th ACM Conference on Electronic Commerce, ACM Press, New York, 2004, pp. 208–217.

[26] F. Ricci, K. Wöber, A. Zins, Recommendation by collaborative browsing, in: A.J. Frew (Ed.), Information and Communication Technologies in Tourism, Springer, Vienna, 2005, pp. 172–182.

[27] J.W. Sammon, A nonlinear mapping for data structure analysis, IEEE Transactions on Computers 18 (5) (1969) 401–409.

[28] J.B. Schafer, J.A. Konstan, J. Riedl, E-commerce recommendation applications, Data Mining and Knowledge Discovery 5 (2001) 115–153.

[29] B. Schneiderman, Tree visualizations with tree-maps: 2-d space <sup>fi</sup>lling approach, ACM Transactions on Graphics 11 (1) (1992) 92–99.

[30] B. Schwartz, The Paradox of Choice: Why More Is Less, HarperCollins New York, 2004.

[31] H. Shimazu, ExpertClerk: a conversational case-based reasoning tool for developing salesclerk agents in e-commerce webshops, Arti<sup>fi</sup>cial Intelligence Review 18 (2002) 223–244.

[32] P.J. Stappers, G. Pasman, Exploring a database through interactive visualised similarity scaling, in: M.W. Altom, M.G. Williams (Eds.), Human Factors in Computer Systems. CHI99 Extended Abstracts, 1999 pp. 184–185.

[33] P.J. Stappers, G. Pasman, P.J.F. Groenen, Exploring databases for taste or inspiration with interactive multi-dimensional scaling, In Proceedings IEA 2000 / HFES 2000, Ergonomics for the new Millennium, Santa Monica CA, 2000, pp. 3–575–3-578.

[34] W.S. Torgerson, Multidimensional scaling: I. Theory and method, Psychometrika 17 (1952) 401-419

[35] O. Turetken, R. Sharda, Development of a fisheve-based information search processing aid (FISPA) for managing information overload in the web environment. Decision Support Systems 37 (2004) 415–434

[36] R. Van Gulik, F. Vignoli, H. Van der Wetering, Mapping music in the palm of your hand, explore and discover your collection, Proceedings of the 5th International Conference on Music Information Retrieval, 2004.

[37] C.C. Yang, H. Chen, K. Hong, Visualization of large category map for Internet browsing, Decision Support Systems 35 (2003) 89–102.

![](/api/attachments/4DXHW7QD/fulltext/images/a3be2aa27cad7476a0156e26718903499b788bdbb02a8d24b6fcfa8d6a7f5d8b.jpg)

Martijn Kagie received a master degree in computational economics from Erasmus University Rotterdam in 2005. Currently he is a PhD candidate at the Erasmus Research Institute of Management af<sup>fi</sup>liated with the Econometric Institute of the Erasmus School of Economics. His research interests are in applications of data mining and data visualization in the <sup>fi</sup>eld of electronic commerce. He has published in Lecture Notes in Computer Science and Intelligent Systems in Accounting, Finance and Management.

![](/api/attachments/4DXHW7QD/fulltext/images/f0066c486fed50ec72d10fe17d4f3470a956d647c7f537bc82dcf882cf138cbb.jpg)  
Patrick Groenen is full professor in statistics at the Econometric Institute, Erasmus University Rotterdam, The Netherlands. His research interests lies in data visualization, dynamic user interfaces, multidimensional scaling, multivariate analysis, and optimization. He has written severa papers in the scienti<sup>fi</sup>c literature and is coauthor of a textbook on multidimensional scaling.

Michiel van Wezel received a masters degree in computer science from Utrecht University in 1994 and a PhD in arti<sup>fi</sup>cial intelligence from Leiden University in 2002. Currently he works as an assistant professor on computer science and Internet marketing at the Erasmus School of Economics. His research interests are the application of machine learning techniques in marketing and intelligent user interfaces for Internet shop ping.

![](/api/attachments/4DXHW7QD/fulltext/images/0fca14fa1121356e2267d2a8b4c8c0fd3adde95c22797897bcd8a6236be16395.jpg)
