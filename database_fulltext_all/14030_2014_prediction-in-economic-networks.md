---
otero_id: 14030
otero_key: "R2S7FXPN"
title: "Prediction in Economic Networks"
authors: "Vasant Dhar; Tomer Geva; Gal Oestreicher-Singer; Arun Sundararajan"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2013.0510"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.239.99.140] On: 27 May 2014, At: 12:13 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## 6SR

## Information Systems Research

![](/api/attachments/R2S7FXPN/fulltext/images/4e1387e06e1cdf07e86bc00536b35b553f1352f95db2ddc1a97dbe722faa5d06.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Prediction in Economic Networks

Vasant Dhar, Tomer Geva, Gal Oestreicher-Singer, Arun Sundararajan

To cite this article:

Vasant Dhar, Tomer Geva, Gal Oestreicher-Singer, Arun Sundararajan (2014) Prediction in Economic Networks. Information Systems Research

Published online in Articles in Advance 24 Mar 2014

http://dx.doi.org/10.1287/isre.2013.0510

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/R2S7FXPN/fulltext/images/adcedd011080dfb4b10f80356bbaa8425f43f8f893995a72d23d005bfb4360d5.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Prediction in Economic Networks

Vasant Dhar

Stern School of Business, New York University, New York, New York 10012, vdhar@stern.nyu.edu

Tomer Geva, Gal Oestreicher-Singer Recanati Business School, Tel-Aviv University, 69978 Israel {tgeva@tau.ac.il, galos@tau.ac.il}

Arun Sundararajan Stern School of Business, New York University, New York, New York 10012, asundara@stern.nyu.edu

W<sup>e</sup> <sup>define</sup> <sup>an</sup> <sup>economic</sup> <sup>network</sup> <sup>as</sup> <sup>a</sup> <sup>linked</sup> <sup>set</sup> <sup>of</sup> <sup>entities,</sup> <sup>where</sup> <sup>links</sup> <sup>are</sup> <sup>created</sup> <sup>by</sup> <sup>actual</sup> <sup>realizations</sup> <sup>of</sup> shared economic outcomes between entities. We analyze the predictive information contained in a specific type of economic network, namely, a product network, where the links between products reflect aggregated information on the preferences of large numbers of individuals to co-purchase pairs of products. The product network therefore reflects a simple “smoothed” model of demand for related products. Using a data set containing more than 70 million observations of a nonstatic co-purchase network over a period of two years, we predict network entities’ future demand by augmenting data on their historical demand with data on the demand for their immediate neighbors, in addition to network properties, specifically, local clustering and PageRank. To our knowledge, this is the first study of a large-scale dynamic network that shows that a product network contains useful distributed information for demand prediction. The economic implications of algorithmically predicting demand for large numbers of products are significant.

Keywords: economic networks; prediction; co-purchase network; predictive modeling; neural networks; autoregressive models; network-based prediction; PageRank

History: Rahul Telang, Senior Editor; Gautam Pant, Associate Editor. This paper was received July 6, 2012, and was with the authors 5 months for 2 revisions. Published online in Articles in Advance.

## 1. Introduction

The growth in commercial and social interaction online has made electronic networks of different kinds increasingly prevalent. One such type of network is the social network, in which the establishment of a social link between individuals denotes a selection that is driven by individual preferences. By revealing the connections among different individuals, a social network can enable us to predict various “outcomes” for network members: if we know, for example, what choice one individual has already made, we can use the network to predict the choices of neighboring individuals (see, for example, Hill et al. 2006). The expectation is that connected individuals will experience similar outcomes, as a result of homophily or influence or some combination of the two (Aral et al. 2009). In other words, links in a social network are predictive because of two reasons—they reflect inherent similarity between the nodes (the individuals) and they transmit information between those two individuals.

Another prevalent type of electronic network is the product network in which products are the nodes.

In product networks, in contrast to social networks, shared outcomes are not merely a by-product of existing connections among individuals; rather, shared economic outcomes are the basis for link formation between entities. In a co-purchase network, for example, which is the focus of our study, a link is established between two products if they happen to be purchased together frequently.<sup>1</sup>

A link in a co-purchase network has a different meaning from a link in a social network. It does not capture the decision of a network member to be associated with another network member; rather, it reflects the aggregation of preferences of many people, who are external to the network. In other words, link formation (and demand correlation) is driven not solely by the nodes’ internal properties—such as the products’ characteristics or their inherent similarity—but also by something external to the products’ space— people’s preferences, which vary over time. Herein we seek to predict the future demand of individual products in a product network.

Prediction is a difficult endeavor but an essential test of any model or theory (Popper 1968).<sup>2</sup> In social networks, outcomes of interest are typically the rare ones, and predicting rare outcomes is difficult at the individual level. For example, product adoption is usually rare, and it is difficult to predict who will adopt a product even if the individual is linked to someone who is a known adopter. Similarly, fraud occurs infrequently, which makes it difficult to predict at the individual level. Predicting the rare outcome is difficult in noisy domains—where polar opposite outcomes often result under identical observed conditions (Dhar 2011, 2013) because of random exogenous shocks or variance in individual behavior. In social networks, this variance in individual behavior arises in large part because of the “noise” or variance in the meaning of the link that connects individuals.<sup>3</sup> Still, it has been shown that it is possible to use network information to generate better-thanrandom predictions, and that such predictions can be economically useful. It is not surprising that all major social network businesses are focused on incrementally improving their targeting accuracy by generating better predictive models that exploit the links between individuals in networks.

The basis for prediction in economic networks is different from that in social networks. Co-purchase links reflect aggregated preference information of large numbers of individuals, thereby providing a simple “smoothed” model of demand for products related by such links. Specifying such a model explicitly based on each product’s individual attributes would be incredibly complex and probably futile. In contrast, the co-purchase network constitutes a decision-relevant “projection” of this complex space into a pattern of correlated temporal demand among networked products. The prediction we want to make, at the individual entity or product level, makes use of the smoothed patterns of aggregated demands among the networked products. To our knowledge, this is the first demonstration of using aggregated network information to predict future demand for each product in the network.

This paper contributes to the literature of prediction and networks on several levels. Its primary contribution is that it is the first study to demonstrate demand prediction in a product network and describe the network aspects that contribute to predictability. A secondary contribution is in the representation of a network that enables it to be dynamic and predict demand for entities that appear over time (see Figure 1). Another secondary contribution is in the identification of network variables, such as PageRank and local clustering that contribute to demand predictability. An empirical contribution is the finding that the role of network information in predictive performance is almost entirely accounted for by the first level of network neighbors. This result and the dynamic network representation provide the specification of a robust predictive model of demand for products that are related through purchasing patterns on a macro level over time. The economic implications of predicting demand patterns in large networks of this type are significant.

The product network is relevant to decision making, or actionable, only if one can predict the future demand of every product in the network on the basis of the current state of the network, that is, levels of demand reflected in the network and its current set of linkages. Oestreicher-Singer and Sundararajan (2012) showed that the visibility of a link between complementary products is associated with a significant increase in their levels of demand after controlling for alternative explanations for demand. Although this is likely a necessary condition for future demand predictability, it is not sufficient. Correspondingly, their paper does not claim to demonstrate future demand predictability, focusing instead on the different economic mechanisms that may explain variations in the level of demand spillovers across products of different popularity and vintage.

In contrast, our interest is in understanding whether past demand of neighboring products can be used to predict a focal product’s future demand. In doing so, we include the focal product’s own past demand and ask, do the past demand patterns of neighboring products coupled with their network properties provide predictive power above and beyond the focal product’s own past demand? An interesting antecedent question is to ask why or under what conditions should there be predictability at all in such a network?

The short answer is that there should be predictability in demand only if the system is inefficient, that is, if all information about prior demand for products in the network is not already reflected in current demand levels of the focal product. If the aggregatebased demand levels change in parts of the network, perhaps such smoothed trends are reliable predictors of direction or even magnitude of demand at the individual product level. If better-than-random predictions of future demand levels can be generated in a systematic manner, the resulting efficiencies in large networks are sizable. Unlike financial markets where there is considerable incentive for participants to exploit market inefficiency, which typically eliminates it, there is little incentive in product networks for exploitation of the inefficiency. This is good news for sellers since the network is likely to persist as a useful source of information for demand forecasting and resulting supply chain optimization.

The structure of the specific network we consider can provide two sources of predictive information. First, neighboring products (products that directly link to one another) may be found to be a good reference group for a given product, with high demand correlation. After all, this network is based on frequent co-purchase behavior, and when items tend to be purchased concurrently, chances are their demand is correlated and will continue to be so. In the network we study, the explicit visibility of co-purchase relationships, embodied in hyperlinks, may make them much more relevant for prediction purposes. Moreover, this information can be useful especially if what is driving the correlation is distinct from observable characteristics of the products such as author, subject category, or other attributes that describe the product. Note that for the purpose of predicting future states of a product, the drivers of such correlation and the direction of causation are irrelevant (more on this in what follows).

Second, the structural properties of a product’s network position may incorporate valuable information. Unlike offline stores, which have limited dimensionality, the online store has a complex structure, and the position of a node in that network may include predictive information. For example, it is possible that products in highly clustered areas of the network exhibit different demand patterns compared with products in less clustered areas. In such cases, the clustering coefficient of a product may be predictive of its demand. Similarly, global structural characteristics, such as product centrality, may prove to have high predictive power.

This research breaks the prediction problem into two parts: (a) does current and past information regarding neighboring entities contain predictive information? and (b) do the network’s structural properties (as measured by network measures such as PageRank and local clustering coefficient) contain additional predictive information? In other words, is there is a “gestalt” associated with the distributed information implicit in economic networks that can be exploited to build predictive models for demand?

Our emphasis on prediction is driven by our desire to motivate researchers to take prediction seriously in theory formation. In his famous treatise titled “Conjectures and Refutations,” Popper (1968) argues that the primary criterion of the scientific status of a model is its falsifiability, or refutability, or testability. Prediction, he argues, especially if it is nontrivial, is an essential validation of a model. In a recent paper, Shmueli and Koppius (2011) provide an extensive review of the literature on explanation versus prediction, showing how the former has dominated the research in information systems largely because of its emphasis on testing hypothesized causal relationships. There are several reasons why building a predictive model as opposed to an explanatory one for prediction in online product networks is a worthwhile complementary goal and an important contribution to the literature. For a review of this literature, the reader is referred to Hastie et al. (2009), Shmueli (2010), and Shmueli and Koppius (2011).

We investigate our hypotheses using a massive co-purchase data set gathered from Amazon.com. The data cover nearly one million books over two years, resulting in a total of more than 70 million daily observations. The “naïve” forecast for the next period’s demand would be today’s demand. A richer input set would include historical demand for an entity. Richer still would be input from its related entities (e.g., its network neighbors). Finally, the richest input set would include local properties of the network, such as an entity’s local clustering coefficient (Watts and Strogatz 1998) or its PageRank (Brin and Page 1998). We would expect an input set incorporating such local and global properties to provide the highest predictive accuracy.

In addition to comparing predictive models with different sets of inputs, we also compare two classes of modeling choices: The first model is a linear autoregressive (AR) model, which is widely known in the time series prediction and economic literature. The second is a neural network (NN), which is a powerful method for modeling complex nonlinear models in situations where plenty of data are available, as is the case in this study.

Evaluating performance while using these two different algorithm classes has two main purposes: First, it is interesting to discern whether inclusion of product-network-based input data improves a model’s predictive performance regardless of the type of algorithm, or whether a certain type of algorithm is better suited to exploit the network “gestalt.” Second, it is often not known in advance whether a given model’s predictions will be superior to those of another, especially for out-of-sample data. Although nonlinear algorithms such as NN are recognized for

Figure 1 Using Multiple Past States of the Network to Predict Future Demand  
![](/api/attachments/R2S7FXPN/fulltext/images/170b28092ac834229cc8bcd0cfe3c1883659bdd4a96779c803d8aa3d226ac735.jpg)  
their ability to capture complex relations, these algorithms have also been found in various cases to overfit the data. On the other hand, a simple AR model may be inferior in capturing complex relations, but it is also much less likely to overfit the data. Thus, employing the simpler AR model could serve as a benchmark. Although it is possible to use many other models, our choice reflects two standard model types that are commonly used in econometric and machine learning modeling.

## 2. Prior Work

Prior work in the information systems, computer science, and marketing literature has recognized the importance of social and economic networks in describing patterns associated with a variety of business outcomes.

In recent years, researchers have shown considerable interest in data mining that is based on social network data (Kleinberg 2007, Hill et al. 2006) and parallel interest in mining web-based data sources for developing micro-data-based decision support systems (Marsden 2008). Some of the popular applications for networked data sets include prediction of new product diffusion and churn, fraud detection, and counterterrorism. An early paper by Domingos and Richardson (2001) uses knowledge sharing sites to mine implied social relationships between consumers toward improving targeted marketing and optimizing the marketing funds allocated to each consumer. More recent work has focused largely on how electronic instantiations of “social networks” (for example, networks implied by corporate email communication patterns, online conversations, or instant messaging patterns) serve as conduits for information flow (Godes and Mayzlin 2004); how network structures affect such flows (Bampo et al. 2008, Kiss and Bichler 2008); what fraction of these flows can be ascribed to true influence (Aral et al. 2009, Ma et al. 2009); and, more broadly, how to improve the mining of information by leveraging information about social networks (Song and van der Aalst 2008).

Our current question steps away from deconstructing information flows or distinguishing influence from other drivers of correlation, and instead examines whether outcomes can be predicted in the context of network links that are created by a high fraction of co-purchases.<sup>4</sup> We focus on using state changes of an entity in predicting state changes of other entities in the network. Specifically, a change in an entity in one period results in a cascade of changes across the entire network, where the changes are predictions for the next time period. We identify the local neighbors of a given product and analyze the structural characteristics (global and local) of the product within the network as a basis for predicting future demand of related products.

It is important to emphasize that the interconnection between economic objects (agents, products) is not necessarily on account of their explicitly sharing one or more observable features or characteristics (such as author, topic, or genre in our context). As mentioned above, such features are part of what we term a product’s “intrinsic features” and are typically used as a basis for prediction in data mining.<sup>5</sup> Although we may leverage such information, our primary interest is in demonstrating that an entity’s future demand is more accurately predicted by combining its historical demand with that of its neighbors and its network “positioning” than by considering its demand alone.

Furthermore, in this sense, our work also differs from the large volume of literature on network classification methods in that rather than develop new prediction methods, its aim is to examine whether a unique type of network, a product network, can be exploited for predictive purposes. To the best of our knowledge, this is the first study to provide supportive evidence in this regard.

Our study diverges from previous studies on network classification (Chakrabarti et al. 1998, Macskassy and Provost 2007, Sen et al. 2008) or link prediction (Lichtenwalter et al. 2010) not only in its goals but also in its methodology. Although our work builds on the same basic ideas, of utilizing local and global network data for modeling and inference, it is distinct in two important respects. First, in this study we use multiple “snapshots” of past states of the network in order to make inferences regarding future states. Second, we treat time as a distinguished variable by ensuring that the network structure at a certain point in time cannot possibly be used to make inferences about the network prior to this point in time. We also allow the network to change at every point in time. The last point is subtle but important. Previous approaches have treated the network as “fixed” in terms of topology, collected information over an interval, and then made inferences. In contrast, our network structure is dynamic;<sup>6</sup> we do not know what the future network structure will be. Rather, our concern is only with using the current and past structures of the network and the states of the network entities to make a prediction about each entity’s future state.

Figure 2 An Example of Co-Purchase Links  
![](/api/attachments/R2S7FXPN/fulltext/images/15decc94cc690e78742351a11940f6b5336e1627ebf39f567a2b8390d5b2bb34.jpg)

It is worth noting that this study is peripherally related to the recommender system literature in that the co-purchase network can be regarded as a primitive collaborative recommendation-based method (Adomavicius and Tuzhilin 2005). However, the co-purchase network “recommendations” are not based on any sophisticated algorithm, other than simply displaying the top N books most commonly copurchased. Additionally, unlike user-based collaborative methods, it does not utilize “similar users” (e.g., recommending the top purchased books that were purchased by people with similar characteristics); rather, it uses data from the entire population.

## 3. Data

We use a large time-series data set of recommendation networks for nearly one million books sold on Amazon.com. Each product on Amazon.com has an associated webpage. Each page has a set of co-purchase links, which are hyperlinks to the set of products that were co-purchased most frequently with this product on Amazon.com. This set is listed under the title “Customers who bought this also bought.” An example of co-purchase links is illustrated in Figure 2.

The co-purchase network is a directed graph in which nodes correspond to products, and edges to directed co-purchase links. We collect data about this graph using a Java-based crawler, which starts from a popular book and follows the co-purchase links using a depth-first algorithm. At each page, the crawler gathers and records information for the book whose webpage it is on, as well as the co-purchase links on that page, and terminates when the entire connected component of the graph is collected. This is repeated daily. A sample part of the graph is illustrated in Figure 3. The algorithm used for data gathering is provided in Appendix A.

Figure 3 Small Segment of a Co-Purchase Network  
![](/api/attachments/R2S7FXPN/fulltext/images/95dbd369362bc3136614db5f3090402bcfcbc25177252ce8ae01eaa436b3f9dd.jpg)

We have chosen to focus on books because they are the product category with by far the largest number of individual titles; their product set is relatively stable (compared to electronics, for instance); and their network data are observable.

We use data collected from August 2005 till September 2007. The graph is traversed every day. We utilize the following data fields, which are available for each book on the co-purchase graph for each day:

• ASIN: a unique serial number given to each book by Amazon.com. Different editions and different versions have different ASIN numbers.

• Co-purchases: ASINs of the books that appear as the focal book’s co-purchases.

• SalesRank: The SalesRank is a number associated with each product on Amazon.com, which measures its demand relative to that of other products. The lower the number is, the higher the sales of that particular product.

• Category Affiliation: Amazon.com uses a hierarchy of categories to classify its books. Thus, we extract for each book its association with two categories: Cat\_h: a high-level category affiliation (e.g., Business and Investing); Cat\_l: a more specific, “lowlevel” category affiliation (e.g., Accounting).

An additional script collects the SalesRank for each book on the graph every 3 hours for the 24-hour period following the collection of the graph. We convert SalesRank data into demand since we are dealing with the prediction of demand, not SalesRank, and since demand is subject to arithmetic operations (like addition), whereas SalesRank is more nebulous in this respect as well as conceptually. The demand computed is based on the SalesRank data generated by Amazon and following a log-linear conversion model suggested by Chevalier and Goolsbee (2003) and by Brynjolfsson et al. (2003). More details are provided in Appendix B.

Based on the collected data, we construct the following variables for each node:

Neighboring Nodes’ Demand Data (InDemand). We calculate the cumulative demand for each node’s (incoming) neighbors.

Network Structure-Based Variables. For each book we calculate two variables that are based on the network structure and may include predictive information: PageRank and local clustering coefficient.<sup>7</sup>

We calculate each book’s PageRank score according to Google’s original algorithm (Brin and Page 1998). The original PageRank algorithm provides a ranking of the “importance” of webpages based on the link structure of the “web” created by the hyperlinks between the pages. In our case, we use it to compute the “importance” of each book (i) according to the network’s daily graph structure, using the following mode

$$
\operatorname{PageRank} (i) = \sum_ {j \in G (i)} \frac {\operatorname{PageRank} (j)}{\operatorname{OutDegree} (j)}\tag{1}
$$

where G4i5 is the set of books that have outgoing links to book i and OutDegree4j5 is the total number of links originating from book $j .$ For more information about the PageRank algorithm see Appendix C.

The motivation for including PageRank in the analysis is because it is a global measure of centrality and, more specifically, a global measure of “attention” given to any specific node from the network. While network neighbors’ demand (and clustering) characterize the local neighborhood of a given product, PageRank incorporates global centrality information that may have predictive power.

For each book we also calculate the local clustering coefficient (Watts and Strogatz 1998). The local clustering coefficient LocalClust(i) for a given node i is a measure of how close the node and its neighbors are to being a clique and is computed as:

LocalClust4i5

$$
= \frac {\text { Number   of   edges   between } i \text { and   its   neighbors }}{k (i) (k (i) - 1)}\tag{2}
$$

where k4i5 is the number of direct incoming neighbors of node i and $k ( i ) ( k ( i ) - 1 )$ is the maximal potential number of connections between node i<sup>0</sup>s direct incoming neighbors.<sup>8</sup>

In the context of product networks, as in the case of social networks, clustering is an important characteristic of the local network around a node and may incorporate two important types of predictive information. First, clustering may impact the flow patterns across the network. Specifically, it will influence the path that a potential consumer follows when “traveling” from product to product and hence may impact demand. Second, network members that are strongly clustered together, or that are part of a clique, are “close” to one another in some way, which may also be indicative of higher homophily. Hence, in social networks, higher clustering is often assumed to intensify the effect of neighbors’ actions. In the context of the product network, books that are part of a clique are likely to be similar to one another. This in turn could indicate similarity in audience and reflect aggregated directional demand trends of this audience.

## 3.1. Sampling and Data Cleaning

The entire book data set collected as part of this study is immense. In order to construct and evaluate prediction models, we utilized a more manageable and “cleaner” set of books involving three million instances (30,000 books per day, over 100 days). First, we filtered out time periods with unusual purchasing behavior. Specifically, we removed seven days before and after the following holidays: Christmas, New Year’s Day, Thanksgiving, and Valentine’s Day. Second, we removed books whose data were missing or partial. Third, we removed unusual or extreme observations, filtering out the top and bottom deciles for daily book demand as well as books whose daily PageRank scores (during the preceding seven days) displayed unusual behavior—going up or down by a factor of 20 (assuming that those books must be subject to unusual exogenous factors, like marketing campaigns). Last, we randomly selected 100 days from our data set. From each of these days we selected a random sample of 30,000 books. Random selection of the days forced us to sample across many periods, thereby eliminating any bias that may exist within a specific time period, and hence increasing the generalizability of the predictive model.<sup>9</sup>

## 4. Models and Data Sets

We use several sets of data inputs to predict future demand. We begin with the data set we expect to be the least predictive and successively augment the data with additional explanatory variables. The different sets are specified below:

(a) $^ { \prime \prime } N \bar { a } i \dot { v } e ^ { \prime \prime }$ Baseline: We use $\log ( \mathrm { D e m a n d } _ { i , 1 } )$ as an estimate for $\log ( \mathrm { D e m a n d } _ { i , 0 } ) .$ where $\mathrm { D e m a n d } _ { i , 0 }$ is node $i ^ { \prime } \mathrm { s }$ unobserved demand today, and $\mathrm { D e m a n d } _ { i , 1 }$ is node $i ^ { \prime } \mathrm { s }$ observed demand yesterday.

(b) Historical Demand: We use $\log ( \mathrm { D e m a n d } _ { i , 1 } ) , \ldots ,$ $\mathrm { l o g } ( \mathrm { D e m a n d } _ { i , N } )$ to predict $\log ( \bar { \mathrm { D e m a n d } _ { i , 0 } } ) .$ , where $\mathrm { D e m a n d } _ { i , 1 }$ is node $i ^ { \prime } \mathrm { s }$ observed demand yesterday, and $\mathrm { D e m a n d } _ { i , N }$ is node $i ^ { \prime } \mathrm { s }$ observed demand N days ago.

(c) Historical Demand and $( I n c o m i n g ) ~ N e i g h -$ boring Nodes’ Demand: We use $\log ( \mathrm { D e m a n d } _ { i , 1 } ) , \ldots ,$ $\log ( \mathrm { D e m a n d } _ { i , N } )$ as well as $\mathrm { l o g ( I n D e m a n d } _ { i , 1 } \mathrm { ) , \dots , }$ $\log ( \mathrm { I n D e m a n d } _ { i , N } )$ in order to predict $\log ( \mathrm { D e m a n d } _ { i , 0 } ) .$ where $\mathrm { I n D e m a n d } _ { i , 1 }$ is yesterday’s total observed demand for node $i ^ { \prime } \mathrm { s }$ direct (incoming) neighbors (nodes with directional links pointing at node i) and $\mathrm { I n D e m a n d } _ { i , N }$ is the total observed demand of node $i ^ { \prime } \mathrm { s }$ direct neighbors N days ago.

(d) Historical Demand, Neighboring Nodes’ Demand and PageRank: We use

$$
\log (\text { Demand } _ {i, 1}), \dots , \log (\text { Demand } _ {i, N}),
$$

$$
\begin{array}{c} \log (\text {InDemand} _ {i, 1}), \ldots , \log (\text {InDemand} _ {i, N}), \quad \text {and} \\ \log (\text {PageRank} _ {i, 1}), \ldots , \log (\text {PageRank} _ {i, N}) \end{array}
$$

in order to predict $\log ( \mathrm { D e m a n d } _ { i , 0 } )$ , where $\mathrm { P a g e R a n k } _ { i , 1 }$ is yesterday’s observed PageRank of node i and $\mathrm { P a g e R a n k } _ { i , N }$ is the PageRank of node i N days ago.

(e) Historical Demand, Neighboring Nodes’ Demand and Local Clustering: We use $\mathrm { l o \bar { g } ( D e m a n d } _ { i , 1 } ) , . . . ,$ $\log ( \mathrm { D e m a n d } _ { i , N } )$ 1 log4InDemand $\mathbf { \Phi } _ { \mathrm { i } _ { 1 , 1 } } ) , \dots , \log ( \mathrm { I n D e m a n d } _ { i , N } ) ,$ and $\log ( \mathrm { L o c a l C l u s t } _ { i , 1 } ) , \ldots ,$ 1 log4LocalClust 5 in order to predict $\log ( \mathrm { D e m a n d } _ { i , 0 } )$ , where $\mathrm { L o c a l C l u s t } _ { i , 1 }$ is yesterday’s observed local clustering coefficient of node i and $\mathrm { L o c a l C l u s t } _ { i , N }$ is the local clustering coefficient of node i N days ago.

## 4.1. Prediction Models

To capture the effect on prediction accuracy of successively adding information, we use two well-known models to generate predictions based on each of the data sets (b), (c), (d), and (e), described in detail above.

1. An auto-regression (AR) Model with a leastsquares estimator. This is a simple linear model often used to model time-series data. We implement the algorithm using R software.

2. A back-propagation-based neural network (NN) algorithm. This is a nonlinear model that is estimated by the backprop algorithm (Werbos 1974) (see Appendix D for more details about the NN algorithm). We use the R software package “nnet” to implement the backprop algorithm. This implementation involves one layer of hidden neurons, and the minimization of a sum of square errors criterion.

## 5. Results

The literature on model validation is extensive. We use a validation framework that unifies several streams of literature and is described in Sobehart et al. (2001). The framework views model validation along two dimensions. The first is across time: How well does a model built on data over a certain period of time perform on future data? The second is across universe: If a model is built on a certain universe (such as books, financial instruments, etc.), how well does it perform on elements of the universe that were not used in building the model? The validation framework is presented in Figure 4. The lower rightmost quadrant represents the most stringent validation test, in which the data used for testing the model include data from future points in time and entities in the universe that were not used to build the model.

We partitioned the data sample into two sets: a training set, which included the first 66 days (1,980,000 data instances) and was used to construct the prediction models, and a test set, which included the remaining 34 days (1,020,000 data instances) and was used to independently evaluate the forecasting models. This ensured validation across time in that each model was tested only on future data. We further ensured that the test set contained books that were not included in the training set. These two guidelines provide a robust basis for model validation.

Each prediction model was recreated several times time using a different number of historical lags $( \mathrm { i . e . , }$ different values of N ), from one day up to seven days.

Since NN performance is known to be sensitive to the number of hidden neurons (HNs), we checked the robustness of our NN models using three different architectures. Each architecture used one layer of

Figure 4 Validation Framework  
![](/api/attachments/R2S7FXPN/fulltext/images/238a837824787094ea09cd3201a6aad38cd292dd61983fc1f6d36c0eccb6de40.jpg)

HNs, but the architectures differed in the proportion of HNs to the number of inputs. We set the number of HNs as either 0.5, 1, or 2 times the number of inputs (see Appendix D for motivation and a wider discussion on this topic). Although there were some differences in performance, overall, the three architectures yielded similar findings. For the sake of brevity, we report only on the simplest NN (with the number of HNs set as half the number of inputs). This network was the most conservative in terms of improving overall performance.

Figures 5 through 9 show the results of the different models (over the independent validation set). All results are presented using the Mean Square Error (MSE) criterion. We find this criterion most suitable for making the comparison between the different models, as both our AR and NN implementations share the goal of minimizing the sum of square errors. Confidence intervals (95%) for the difference in MSE values, between different data sets, are reported in Appendix E. For completeness, we also did the analysis using the Mean Absolute Percentage Error (MAPE) criterion, and the results are very similar.

Figure 5 AR Model Inputs: Naïve vs. Demand vs. Demand and InDemand  
![](/api/attachments/R2S7FXPN/fulltext/images/539c50c90f398eee9f08f38e9383404dad5f90de6438452b523b97c3f0646ff5.jpg)

Figure 6 AR Model: Adding PageRank or LocalClust to Demand and InDemand  
![](/api/attachments/R2S7FXPN/fulltext/images/de606084a8e5b46f3e90b0e2e29fe7b065f17ea7c9c38ca949d629da02d513ad.jpg)

Figure 7 DemandData: AR vs. AN  
![](/api/attachments/R2S7FXPN/fulltext/images/f7813decc9376b5e015e0fc7b68ce112eb52d0d490cf472015c902c690f5be29.jpg)

Figure 8 DemandData and InDemand Data: AR vs. NN  
![](/api/attachments/R2S7FXPN/fulltext/images/e737862591d83ac872bb5bdb7ce1d48b7496a6e50e7c245ecb8c0363561eb294.jpg)

Figure 9 Performance of NN Models with Different Sets of Inputs  
![](/api/attachments/R2S7FXPN/fulltext/images/920eafc492069b19cf6d5847734951c15671df7132f4930079e831d2d87695f8.jpg)

Several patterns are apparent in the results. Figure 5 compares a Naïve model, which uses the previous day’s demand as the next period’s demand, versus an AR model with Historical Demand, as well as versus an AR model with Historical Demand and Neighboring Nodes’ Demand (InDemand). The simple AR model with Historical Demand information does much better than the Naïve model, which is in line with expectations. The greater the number of past periods used, the better the performance. Adding

Neighboring Nodes’ Demand to the AR model provides further improvement in prediction accuracy.

Figure 6 shows the results for the AR model when network-based variables are added, namely, PageRank and LocalClust. Interestingly, incorporating the additional information does not yield significantly better predictions compared with an AR model that uses Historical Demand and InDemand information. See also Appendix E (Table E.1, two rightmost columns), which shows that in most cases the 95% confidence intervals for MSE difference include zero.

Figure 7 compares the NN model based on Historical Demand data to the AR model based on Historical Demand data. It is notable that the NN model considerably outperforms the AR model when using these data. Figure 8 compares the NN model to the AR model, for the case in which both models use both Historical Demand data and InDemand data. Again, the NN model considerably outperforms the AR model.

Figure 9 compares the performance of NN models given different sets of inputs. In general, the NN model not only performs better than the AR model but is also able to “extract” additional predictive power out of the network-based variables— something that the AR model fails to achieve. This is because NN models can inherently model more complex underlying patterns, such as interactions within the data (see, for example, our discussion of clustering in connection to interaction effects in §3). The general conclusion here is that the network-based variables provide predictive power as long as the model, in this case a nonlinear one, is capable of extracting it.

It is important to note that even small visual differences in Figure 9 have a substantial business impact. First, the 95% confidence intervals (Appendix E, Table E.4) for the difference in MSE between pairs of data sets are generally narrow and do not include zero. For instance, in Figure 9 there is a difference in MSE of ∼ 0.00035 between a model using one lag of Historical Demand and InDemand information and a model utilizing one lag of Historical Demand, InDemand and PageRank Information. Nevertheless, the 95% confidence interval for this difference is between 0.0003 and 0.0004.

In addition, for a large network such as this one, which involves the maintenance of a large inventory of books over time, small improvements in prediction have a considerable economic impact. For instance, the 0.00035 improvement in MSE in the example above could be translated into an aggregated reduction in prediction errors of approximately \$500,000 books per year.<sup>10</sup>

5.1. Sensitivity Analysis and Robustness Checks We have performed a number of sensitivity analyses to obtain additional insights into our results. Our first type of analysis seeks to discern whether predictive performance depends on network structure or product characteristics. For this analysis, we focus on the performance of NN models using seven lags of data, since this configuration provides the best results across all types of data inputs and model choices.

Figure 10 presents the performance of the different NN models across five quintiles of Demand data. In this figure, dots represent MSE values; and lines above and below the dots represent two standard deviations above and below the MSE value, respectively. From this figure it is evident that all models perform much better for products with high values of Demand (Q5). One possible explanation for this is that demand spikes are likely to be less pronounced for products whose demand is already high. Interestingly, for products with high demand, models using network-based parameters perform significantly better than models without the network-based parameters. It is also noteworthy that with the exception of (Q3), models using PageRank perform consistently well. It is also notable that across all quintiles, adding local clustering to Demandand InDemand data never makes the results worse, and in some cases yields improvements.

Figure 11 presents the performance of the different models across five quintiles of InDemand data. Network information contributes to predictive accuracy across the quintiles. The contribution of adding PageRank is more noticeable in the lower ranges of InDemand values (Q1, Q2). We note that the volatility of InDemand is the lowest in the lower quintiles; this could account for the improved performance in these quintiles.

Figure 12 presents the performance of the different models across five quintiles of PageRank data. Adding PageRank data to the prediction models provides the most significant improvement at the lower ranges of PageRank (Q1, Q2), whereas adding local clustering data provides a small improvement to the baseline (i.e., using only Demanddata) across the entire range.

Finally, a similar picture emerges from Figure 13, which presents the performance across five quintiles of LocalClust data. In this case, PageRank provides a significant improvement at the bottom and top quintiles, whereas local clustering provides a small improvement in predictive performance across the entire LocalClust range.

Figure 10 NN Model Performance: Different Inputs by DemandQuintiles  
![](/api/attachments/R2S7FXPN/fulltext/images/3bfbc51b2eb5cfea013d9b55c62db6698de0d76aad4fc90487c3c5c9b0a1ba9d.jpg)

Figure 11 NN Model Performance: Different Inputs by InDemand Quintiles  
![](/api/attachments/R2S7FXPN/fulltext/images/60073b40e15467a220d5ed038b3f95be3139dbb6b650da89ce5f3b3de82b226c.jpg)

An overall conclusion from Figures 10 through 13 is that models using network-based parameters tend to make better predictions across all quintiles, and the network metric PageRank seems to be consistently associated with improvements in predictions. Local clustering tends to provide a small and consistent improvement across the entire data range relative to the baseline.

In Figures 14 and 15 we present the effect of two additional factors: books’ vintage (measured in number of years since the book was published) and category. Figure 14 shows that predictive performance is stronger for books aged between 2 and 10 years, whereas it is somewhat weaker for very new or old books. As in our analyses above, we find that models using network-based parameters generally outperform the baseline group across all vintage quintiles.

Figure 15 shows the models’ predictive performance across different book categories (with a minimum of 1,000 books in the validation set). A few categories, such as Comics, Mysteries, and Science Fiction, have higher error rates along with larger error bars; this is due to relatively small sample size. Consistent with previous analyses, the improvement in prediction using network information is apparent across categories, as is the role of PageRank.

Figure 12 NN Model Performance: Different Inputs by PageRank Quintiles  
![](/api/attachments/R2S7FXPN/fulltext/images/687fe6279bbe11a480eadffeb0b8c8ed384bce654a1daaadd8514284bc30fec8.jpg)

Figure 13 NN Model Performance: Different Inputs by LocalClust Quintiles  
![](/api/attachments/R2S7FXPN/fulltext/images/b63a70ad91c57a0fb4ff55c8297b9ad0956e377f1958a0de47d5b4cf42d8f85f.jpg)

5.1.1. Prediction with Partial Information. The second sensitivity analysis considers the predictive accuracy of AR and NN models when less information about the network is available, specifically, when no InDemand information is available, and only Historical Demand and network-specific data are observable.

We define the following data sets:

(f) Historical Demand and PageRank: We use

$\mathrm { l o g ( D e m a n d } _ { i , 1 } ) , \dots , \mathrm { l o g ( D e m a n d } _ { i , N } ) .$ 1 and $\mathrm { l o g } ( \mathrm { P a g e R a n k } _ { i , 1 } ) , \dots , \mathrm { l o g } ( \mathrm { P a g e R a n k } _ { i , N } )$ in order to predict $\log ( \mathrm { D e m a n d } _ { i , 0 } )$

(g) Historical Demand and Local Clustering: We use $\mathrm { l o g ( D e m a n d } _ { i , 1 } ) , \dots , \mathrm { l o g ( D e m a n d } _ { i , N } )$ 1 and $\mathrm { l o g } ( \mathrm { L o c a l C l u s t } _ { i , 1 } ) , \dots , \mathrm { l o g } ( \mathrm { L o c a l C l u s t } _ { i , N } )$

in order to predict log4Demand<sub>i10</sub>5.

The results are detailed in Appendix F and can be summarized briefly as follows:

1. For the AR model, network information reduces error to a small extent consistently across the lags (Figure F.1, Table E.2). However, this reduction is much smaller than the improvements obtained by using state information about a node’s neighbors.

2. For the NN model, adding PageRank and local clustering data to demand data reduces error (Figure F.2, Table E.5). By and large, this improvement is more noticeable than in the case of the AR model. However, for most lags, adding this network-based information still provides only limited improvement compared to adding demand information based on a node’s neighbors.

Figure 14 NN Model Performance: Different Inputs by Number of Years Since Publication  
![](/api/attachments/R2S7FXPN/fulltext/images/426d7e9063638405944d81918e2d7db1f21863a6c9cfba65c7c5c7bdc3e45519.jpg)

Figure 15 NN Model Performance: Different Inputs by Category  
![](/api/attachments/R2S7FXPN/fulltext/images/d436bfc26dee9f0a6330ab684ff447ad470d8563190a290d88c7e7fe1600761b.jpg)

5.1.2. Adding Price Information. As another form of robustness check we added book price data into our models. However, at best, price data contributed only marginally to predictive performance. We deem the cause for this occurrence to be the following: When demand is unknown it is expected that price at time t would be informative about the demand at time t + 1. Nevertheless, in this study, we already make use of a much better predictor than the price at time t: demand at time t. Furthermore, the demand at time t is already determined when taking the price at time t into account. This information overlap is even more pronounced when considering all Demand values between time t and time t − 6. Finally, it should be noted that Amazon’s price information is incomplete, for instance because many of Amazon’s buyers are influenced by different bundling and shipping cost options.

5.1.3. Comparison with Average Category Demand. In this set of sensitivity analyses, we attempt to eliminate other possible explanations for our results aside from the informative value of the network. One alternative explanation is that, for a given product, the network provides us with information about the identity of a group of products that are similar (or perhaps complementary) to the product, and any additional information is likely to be helpful for predictive purposes, especially if it is of relevant products. That is, information on demand for network neighbors is not unique by virtue of the fact that it comes from the network; rather, any information about a relevant reference group will provide the same results.

To test this alternative explanation we use a comparable reference group—the group of products belonging to the same category. Given that in most brickand-mortar book stores books are organized by category, this seems like the most natural reference group to use. If, indeed, the explanation for the improvement in prediction accuracy is the mere use of reference group information, rather than the specific use of network-based data, then adding category information on top of historical demand information should provide an improvement in prediction results similar to that achieved by adding network neighbors’ demand (InDemand).

We define the following data sets and evaluate the models’ predictions using each set:

(i) Historical Demand and Average Category Demand 4high-level category affiliation5: We use

$$
\log (\text { Demand } _ {i, 1}), \dots , \log (\text { Demand } _ {i, N}) \quad \text { and }
$$

$$
\log (\text { Avg\_Cat\_h } _ {i, 1}), \ldots , \log (\text { Avg\_Cat\_h } _ {i, N}),
$$

in order to predict $\log ( \mathrm { D e m a n d } _ { i , 0 } )$ , where Avg\_Cat $\_ h _ { i , 1 }$ is the average demand observed yesterday for the books in node $i ^ { \prime } \mathrm { s }$ category—referring to the node’s high-level category affiliation—and $\mathrm { A v g \_ C a t \_ h } _ { i , N }$ is the average demand in node $i ^ { \prime } \mathrm { s }$ high-level category N days ago.

(j) Historical Demand and Average Category Demand 4both high-level and low-level category affiliations5: We use

$$
\log \left(\text { Demand } _ {i, 1}\right), \dots , \log \left(\text { Demand } _ {i, N}\right),
$$

$$
\log (\text { Avg\_Cat\_h } _ {i, 1}), \dots , \log (\text { Avg\_Cat\_h } _ {i, N}),
$$

$$
\log (\text { Avg\_Cat\_l } _ {i, 1}), \ldots , \log (\text { Avg\_Cat\_l } _ {i, N}),
$$

in order to predict log4Demand 5, where $\mathrm { A v g \_ C a t \_ l } _ { i , 1 }$ is the average demand observed for node $i ^ { \prime } \mathrm { s }$ low-level category yesterday, and $\mathsf { A v g \_ C a t \_ l } _ { i , N }$ is the average demand in node $\dot { i ^ { \prime } } \mathrm { s }$ low-level category N days ago.

The results are presented in Appendix F, Figures F.3–F.4. The general conclusion is that adding average category demand to demand data provides at best a marginal performance improvement, and the models’ performance is inferior to that obtained with both Historical Demand and InDemand data.

Last, we also note that the percentage of neighbors whose category is the same as that of the focal node is not high. On average, only 34% of a node’s immediate neighbors share its high-level category, and only 20% of the immediate neighbors share its low-level category. This provides an additional indication that the predictive power extracted from information on network neighbors is not due to simple similarity in category.

5.1.4. Utilizing Information on Remote Network Neighbors. The last set of sensitivity analyses seeks to identify the distance at which the product network still contains useful embedded information for predictive purposes. Specifically, we evaluate the usefulness of supplying to the predictive model historical demand information originating from remote neighboring tiers.

For this purpose, we use

$$
\begin{array}{c} \log (\text {Demand} _ {i, 1}), \ldots , \log (\text {Demand} _ {i, N}), \\ \log (\text {InDemand} _ {i, 1}), \ldots , \log (\text {InDemand} _ {i, N}), \end{array}
$$

as well as

$$
\begin{array}{c} \log (\text { Second\_Tier\_InDemand } _ {i, 1}), \ldots , \\ \log (\text { Second\_Tier\_InDemand } _ {i, N}), \end{array}
$$

in order to predict $\log ( \mathrm { D e m a n d } _ { i , 0 } ) ,$ where Second $\_ { \mathrm { T i e r \_ I n D e m a n d } _ { i , 1 } }$ is yesterday’s total observed demand for node $i \prime \mathrm { s }$ second-level (incoming) neighbors (nodes with directional links pointing to node $i \prime \mathrm { s }$ first-level neighbors) and Second\_Tier $\mathrm { I n D e m a n d } _ { i , N }$ is the total observed demand for node $i ^ { \prime } \mathrm { s }$ second-level (incoming) neighbors N days ago.

Figures 16 and 17 present MSE results for AR and NN models provided with Historical Demand, InDemand and Second\_Tier\_InDemand data. See also Appendix E, Tables E.3 and $\mathrm { E } . 6 ,$ for the respective confidence intervals. As is evident from Figure $^ { 1 6 , }$ when using the AR model, information on secondlevel neighbors provides smaller (though significant) improvement compared to a model that utilizes only information on the nodes themselves and on their direct neighbors. Figure 17 shows a similar outcome for the NN model. Finally, adding information on third-level neighbors results in negligible improvement in predictive accuracy.

Figure 16 AR Model: Different Levels of Network Neighbors  
![](/api/attachments/R2S7FXPN/fulltext/images/375604bc64716c38e5a7595428b10ecbbb004492883face2729d7a3184f05195.jpg)

Figure 17 NN Model: Different Levels of Network Neighbors  
![](/api/attachments/R2S7FXPN/fulltext/images/96b75c9a49e75ca5fb567bdd3bbffe482042e27d24e31a3e8363d78897ac0193.jpg)

## 6. Discussion and Future Work

Oestreicher-Singer and Sundararajan (2012) have previously shown that visible network links may have a significant and econometrically identifiable influence on the level of demand spillovers across products. In this study, we set out to answer a different question, namely, whether changes in demand can be predicted, and specifically, whether using network information improves predictive accuracy. Our results show that this is in fact the case. To the best of our knowledge, ours is the first large-scale study to investigate whether information that is predictive of demand is contained in a product network. Specifically, we showed that compared with naïve predictions, combining network information that includes data on an entity’s neighbors, together with network properties such as centrality and local clustering, leads to a significant improvement in sales predictions for network products. This result has major economic implications for online retailers—if demand can be predicted algorithmically for large numbers of products, the potential for gains in operating efficiency can be significant. More accurate demand forecasts also create opportunities for creative marketing strategy that takes current data into account. We refrain from describing all the different ways in our results can have business value, since it seems quite evident to us that any firm, irrespective of industry, should be able to benefit in a number of ways from being able to forecast its demand better.

The theory underlying conditions under which we should expect predictability is still fairly nascent. Our high-level explanation for the existence of predictability in the product network is that it is “inefficient” in that the impact of changes in its entities are not immediately reflected in related parts of the network. Aggregated demand patterns tend to be smooth and trending in the short term, thereby providing a level of predictability at the individual product level. It would be interesting to try to extract additional reasons for these types of inefficiencies in product and social networks and identify conditions for their existence. With the explosion of Web 2.0 technologies and the growing adoption of social media, we expect that numerous new economic networks will become observable to firms and researchers over the coming years. The tight association of the links in such networks with economic outcomes of interest makes these networks especially attractive as a basis for predictive modeling. These networks are the natural place to start when looking for ways to expand beyond product-centric features to improve predictive accuracy for network entities.

A secondary avenue for future research is to consider the use of other machine-learning methods to build more accurate predictive models. Machinelearning methods can deal with problems with high levels of noise by discovering “local” models that can be applied to different partitions of the data. These localized models make more aggressive forecasts in comparison to standard econometric models, which tend to be very conservative in their predictions, restricting their forecasts to small deviations from the mean.

Finally, our data include a network that is visible to the consumers. That is, the links between the products are visible to the consumer and hence may influence demand patterns. Such co-purchase networks are now evident in almost all electronic commerce sites (see, for example, the ToysRUs.com, Walmart.com, and Target.com websites). However, demand might be correlated for reasons other than network visibility. An interesting direction for research would be to consider whether there is predictability in product networks regardless of whether its links are visible. If so, networks could be constructed automatically from transaction data that relate the products in ways other than co-purchase. In such cases the relationships might be implicit in purchase patterns across related products. The implications of predictability in such networks could be significant for more intelligent supply chain management and cross-selling.

## Appendix A. Algorithm for Data Collection

We use two computer programs for data collection. The first collects graph information and the second collects SalesRank information. Both use Amazon.com’s XML data service. This service is part of the Amazon Web Services, which provide developers with direct access to Amazon’s platform and databases.

Graph Collection: The program (crawler) that collects the graph starts at a popular book. It then traverses the copurchase network using a depth-first search. Intuitively, in a depth-first search one starts at the root (in our case, the one popular book chosen) and traverses the graph as far as possible along each branch before backtracking. At each page, the crawler gathers and records information for the book whose webpage it is on, as well as the co-purchase links on that page. The ASINs of the co-purchase links are entered into a LIFO (Last-In-First-Out) stack. If the algorithm finds it is on the page of a product that it has visited already, it “backtracks” and returns to the most recent product it has not yet finished exploring. The program terminates when the entire connected component of the graph is collected.

For example, in the graph in Figure A.1, the nodes are numbered in the order in which the crawler will traverse the graph. In this case, the collection starts at node 1. Its co-purchase links are nodes 2, 6, and 7. Therefore, those numbers are added to a LIFO stack. The script will then proceed to node 2, whose co-purchases are nodes 3, 4, and 5, and thus, those numbers will be added to the LIFO stack, which will now include: 3, 4, 5, 6, and 7. The script will continue to node 3. Since there are no co-purchase links to that node, it will move on to node 4. In the same way, the script will collect data about node $5 ,$ node 6, and node 7.

Since node 7 has co-purchase links—nodes 8 and 9—they will be added to the stack. After visiting nodes 8, 9, and 10, the data collection will terminate. As can be seen, the script only stops once it has collected information about the entire connected component. The collection of the entire connected component on Amazon.com takes between four and five hours. The script is run each day at midnight.

## Figure A.1 Illustrates Depth-First Search Used for Graph Traversal

![](/api/attachments/R2S7FXPN/fulltext/images/0ef6921dc9da367cfe26918f5d5d0215cb63c1334b356f632fda46a44e4b5ccb.jpg)

SalesRank Collection: A second computer program collects the demand information for all books on the graph every 3 hours for the 24-hour period following the collection of the graph. This script collects the SalesRank of each book that has ever appeared on the graph. Therefore, it follows the sales of some books that are no longer on the graph.

## Appendix B. Converting SalesRank to Demand

SalesRank is a number associated with each product on Amazon.com that measures the product’s demand relative to that of the other products sold on Amazon.com. The lower the number is, the higher the sales of that particular product. The SalesRank of a book is updated each hour to reflect recent and historical sales of every item sold on Amazon.com.

A formula to convert SalesRank information into demand information was first introduced by Chevalier and Goolsbee (2003). Their goal was to estimate demand elasticity. Their approach was based on making an assumption about the probability distribution of book sales, and then fitting some demand data to this distribution. They chose the standard distributional assumption for this type of rank data, which is the Pareto distribution (i.e., a power law). In the Pareto distribution, the probability that an observation’s value exceeds some level S is an exponential function

$$
\operatorname * {P r} (s > S) = \left(\frac {k}{s}\right) ^ {\theta},\tag{B1}
$$

where k and  are the parameters of the distribution. The more important parameter is $\theta ,$ the shape parameter that indicates the relative frequency of large observations. If  is 2, for example, the probability of an observation decreases in the square of the size of the observation. With a value of 1, it decreases linearly.

For a given book j, the number of books that have sales greater than those of that book is just one less than the book’s rank. Therefore, the fraction of all books that have sales greater than those of a book j is just 6SalesRank4j5 − 17/ TotalNumberOfBooks. If there is a sufficient number of books to eliminate the approximation introduced by discreteness, then one can replace the equation above with:

$$
\frac {\text { SalesRank } (j) - 1}{\text { TotalNumberOfBooks }} = \left(\frac {k}{\text { Demand } (j)}\right) ^ {\theta}.\tag{B2}
$$

Taking logs on both sides, and substituting  with −1/b, this translates ranks into sales as follows:

$$
\log [ \text { Demand } (j) ] = a + b \log [ \text { SalesRank } (j) ].\tag{B3}
$$

Chevalier and Goolsbee estimated the parameters a and b using several methods: by using data from the Wall Street Journal book sales index, which gives the actual quantity sold; by using sales information given by a publisher who sells on Amazon.com; and by conducting an experiment, buying copies of books with a steady SalesRank.

In a later study, Brynjolfsson et al. (2003) used data provided by a publisher selling on Amazon.com to conduct a more robust estimation of the parameters of the formula. They estimated the parameters as: $a = 1 0 . 5 2 6 , b = - 0 . 8 7 1$

## Appendix C. A More Detailed Description of PageRank

The PageRank algorithm was first introduced by Brin and Page (1998), and it estimates the probability that a random surfer will reach a focal webpage. It is computed in the following way. Let u be a webpage: let $F ( u )$ be the set of pages u points to, and let $B ( u )$ be the set of pages that point to u. Let $N ( u ) = \vert F ( u ) \vert$ be the number of links from $u ,$ and let c be a factor used for normalization (so that the sum of ranks across all web pages is constant). A simple ranking, $R ( u )$ , is defined as:

$$
R (u) = c \sum_ {v \in B (u)} \frac {R (v)}{N (v)}.\tag{C1}
$$

This is a simplified version of PageRank. The rank of a page is divided among its outgoing (forward) links evenly to contribute to the ranks of the pages they point to. Note that $c < 1$ because there are a number of pages with no forward links, and their weight is lost from the system. The equation is recursive, but it may be computed by starting with any set of ranks (commonly, equal rank for all pages) and iterating until convergence.

Stated another way, let A be a square matrix with the rows and columns corresponding to numbered web pages. Let $A ( u , v ) = 1 / n ( u )$ if there is an edge from u to $v ,$ and $A ( u , v ) = 0$ otherwise. If we treat the rankings as a vector R over the linked pages, we have

$$
R = c A R.\tag{C2}
$$

So R is an eigenvector of A with eigenvalue c. In fact, the dominant eigenvector of A is the interesting one. It may be computed by repeatedly applying A to any nondegenerate start vector.

There is a small problem with this simplified ranking function. Consider two webpages that point to each other but not to any other page. Suppose there is some webpage that points to one of them. Then, during iteration, this loop will accumulate rank but never distribute any rank (since there are no outgoing edges). The loop forms a sort of trap which is called a “rank sink.” To overcome this problem of rank sinks, a “damping factor” $( 1 - \alpha )$ is introduced. The normalization factor c is then set to . Thus, the full ranking formula is:

$$
R ^ {\prime} (u) = \alpha \sum_ {v \in B (u)} \frac {R ^ {\prime} (v)}{N (v)} + (1 - \alpha).\tag{C3}
$$

Appendix D. Neural Network Prediction Models An artificial neural network (ANN) builds models by using a simple computer emulation of biological neural systems. Neural networks attempt to “learn” patterns from data directly, by sifting the data repeatedly, searching for relationships, automatically building models, and correcting over and over again the models’ own mistakes. The data from which the neural network learns models are referred to as the training data. The technique can derive good models even when the data are incomplete or noisy as long as they are plentiful and representative of the variety of situations in which the models will make predictions (Dhar and Stein 1997). For a rich historical perspective on neural networks, see Hinton (2002) and Rumelhart and McClelland (1984).

Figure D.1 An Illustration of an NN that Contains Four Input Nodes (Blue), One Layer with Four Hidden Nodes (Green), and a Single Output Node (Red)

![](/api/attachments/R2S7FXPN/fulltext/images/84685ee248e83a9fea776998b611357b9d7bcb1a7f6f9aec2a89b849573bf83b.jpg)

Neural networks have been dubbed universal approximators because of their ability to uncover and approximate relationships—often complex nonlinear ones—in many types of data. They derive this ability by connecting the inputs to a problem to its predictions via “hidden” neurons and connections between these neurons. A neuron performs a simple addition of its inputs that come in via directed links from other neurons connected to it, and produces an output based on a simple nonlinear function such as a sigmoid or radial basis function (Lippman 1987) that it directs in turn into neurons toward the output of the neural network (see Figure D.1 for an illustration of a simple NN). This simple nonlinear transformation of inputs into output within a neuron, conducted simultaneously over large numbers of neurons between the inputs and the output, give neural networks their ability to approximate any continuous function as long as training data are plentiful and adequately reflect the variety of situations for which the network will be required to make future predictions. The learned model is said to represent the generalization of the training data. The first algorithm for learning the weights of links that connect neurons using hidden layers—i.e., the layers of neurons located between the inputs and output— was proposed by Werbos (1974) and called “backprop.” This algorithm led to a flurry of research in artificial intelligence that ultimately resulted in the use of neural networks for speech recognition, facial and image recognition, and a variety of problems involving classification.

A neural network is an obvious tool of choice for our prediction task because we have a huge amount of data, and there is no reason a priori to expect the relationship between the inputs and outputs to be a simple one. If anything, the data are noisy, and the relationship is likely to be nonlinear, making a neural network a good choice.

In specifying a neural network architecture, we must choose the number of neurons in the hidden layer. As one might guess, the larger the number of such neurons, the greater the power of the network in its ability to learn complex patterns. However, the added complexity of the network also makes it susceptible to “overfitting,” that is, “memorizing” instead of “generalizing” the data (Hinton 2002). In general, however, added complexity of the network is justified for complex problems, but this also requires that there be plenty of data to enable the network to generalize properly instead of overfitting to the data.

Although there are no hard and fast rules determining the optimal complexity of the network in terms of hidden nodes, some guidelines have been proposed in the literature (Zhang et al. 1998). One such guideline is that the number of hidden units should be proportional to the number of inputs. Specific architectures have been proposed, such as the number of inputs times 0.5, 1, and 2. In our experiments, we use these three levels of complexity, choosing architectures in which the number of hidden neurons is half, equal to, or twice the number of inputs.<sup>11</sup>

## Appendix E. Confidence Intervals

Confidence intervals of 95% for the difference in MSE between various models were calculated by a bootstrapping procedure. For this purpose we used the “boot” library in R software (500 iterations, “basic” bootstrap category).

## AR Models

Table E.1 AR, 95% Confidence Intervals

<table><tr><td>Lag</td><td colspan="2">MSE(Demand) – MSE(Demand, InDemand)</td><td colspan="2">MSE(Demand, InDemand) – MSE(Demand, InDemand, PageRank)</td><td colspan="2">MSE(Demand, InDemand) – MSE(Demand, InDemand, Local_Clust)</td></tr><tr><td>1</td><td>0.0038</td><td>0.0040</td><td>-0.0001</td><td>-0.0001</td><td>0.0001</td><td>0.0001</td></tr><tr><td>2</td><td>0.0031</td><td>0.0033</td><td>0.0000</td><td>0.0000</td><td>0.0001</td><td>0.0001</td></tr><tr><td>3</td><td>0.0024</td><td>0.0026</td><td>-0.0001</td><td>-0.0001</td><td>0.0001</td><td>0.0001</td></tr><tr><td>4</td><td>0.0019</td><td>0.0020</td><td>-0.0001</td><td>-0.0001</td><td>0.0000</td><td>0.0001</td></tr><tr><td>5</td><td>0.0016</td><td>0.0017</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0001</td></tr><tr><td>6</td><td>0.0014</td><td>0.0015</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0001</td></tr><tr><td>7</td><td>0.0012</td><td>0.0014</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr></table>

Table E.2 AR, Partial Information, 95% Confidence Intervals

<table><tr><td>Lag</td><td colspan="2">MSE(Historical Demand) – MSE(Historical Demand, PageRank)</td><td colspan="2">MSE(Historical Demand) – MSE(Historical Demand, LocalClust)</td></tr><tr><td>1</td><td>0.0010</td><td>0.0012</td><td>0.0003</td><td>0.0004</td></tr><tr><td>2</td><td>0.0009</td><td>0.0010</td><td>0.0003</td><td>0.0003</td></tr><tr><td>3</td><td>0.0007</td><td>0.0008</td><td>0.0002</td><td>0.0003</td></tr><tr><td>4</td><td>0.0005</td><td>0.0007</td><td>0.0002</td><td>0.0003</td></tr><tr><td>5</td><td>0.0004</td><td>0.0005</td><td>0.0002</td><td>0.0002</td></tr><tr><td>6</td><td>0.0004</td><td>0.0005</td><td>0.0002</td><td>0.0002</td></tr><tr><td>7</td><td>0.0003</td><td>0.0004</td><td>0.0002</td><td>0.0002</td></tr></table>

Table E.3 AR, Remote Network Neighbors, 95% Confidence Intervals

<table><tr><td>Lag</td><td colspan="2">MSE(Demand, InDemand) — MSE(Demand, InDemand, Second Tier InDemand)</td></tr><tr><td>1</td><td>0.0003</td><td>0.0003</td></tr><tr><td>2</td><td>0.0002</td><td>0.0003</td></tr><tr><td>3</td><td>0.0002</td><td>0.0003</td></tr><tr><td>4</td><td>0.0001</td><td>0.0002</td></tr><tr><td>5</td><td>0.0001</td><td>0.0001</td></tr><tr><td>6</td><td>0.0001</td><td>0.0001</td></tr><tr><td>7</td><td>0.0001</td><td>0.0001</td></tr></table>

<sup>11</sup> For the NN with half the number of HNs—in cases in which the number of inputs was an odd number—we rounded up the number of HNs.

## NN Models

Table E.4 NN, 95% Confidence Intervals

<table><tr><td>Lag</td><td colspan="2">MSE(Demand) – MSE(Demand, InDemand)</td><td colspan="2">MSE(Demand, InDemand) – MSE(Demand, InDemand, PageRank)</td><td colspan="2">MSE(Demand, InDemand) – MSE(Demand, InDemand, LocalClust)</td></tr><tr><td>1</td><td>0.0030</td><td>0.0031</td><td>0.0003</td><td>0.0004</td><td>0.0002</td><td>0.0003</td></tr><tr><td>2</td><td>0.0066</td><td>0.0063</td><td>-0.0023</td><td>-0.0020</td><td>0.0001</td><td>0.0001</td></tr><tr><td>3</td><td>0.0020</td><td>0.0022</td><td>0.0009</td><td>0.0010</td><td>0.0009</td><td>0.0010</td></tr><tr><td>4</td><td>0.0029</td><td>0.0031</td><td>-0.0002</td><td>-0.0001</td><td>0.0005</td><td>0.0007</td></tr><tr><td>5</td><td>0.0023</td><td>0.0024</td><td>0.0005</td><td>0.0007</td><td>0.0001</td><td>0.0002</td></tr><tr><td>6</td><td>0.0026</td><td>0.0023</td><td>0.0002</td><td>0.0003</td><td>0.0005</td><td>0.0007</td></tr><tr><td>7</td><td>0.0032</td><td>0.0034</td><td>0.0021</td><td>0.0024</td><td>0.0003</td><td>0.0004</td></tr></table>

Table E.5 NN, Partial Information, 95% Confidence Intervals

<table><tr><td>Lag</td><td colspan="2">MSE(Historical Demand) – MSE(Historical Demand, PageRank)</td><td colspan="2">MSE(Historical Demand) – MSE(Historical Demand, LocalClust)</td></tr><tr><td>1</td><td>0.0012</td><td>0.0013</td><td>0.0003</td><td>0.0003</td></tr><tr><td>2</td><td>0.0054</td><td>0.0057</td><td>0.0049</td><td>0.0051</td></tr><tr><td>3</td><td>0.0007</td><td>0.0008</td><td>0.0004</td><td>0.0005</td></tr><tr><td>4</td><td>0.0010</td><td>0.0011</td><td>0.0017</td><td>0.0018</td></tr><tr><td>5</td><td>0.0041</td><td>0.0045</td><td>0.0005</td><td>0.0007</td></tr><tr><td>6</td><td>0.0021</td><td>0.0022</td><td>0.0015</td><td>0.0017</td></tr><tr><td>7</td><td>0.0011</td><td>0.0013</td><td>0.0022</td><td>0.0024</td></tr></table>

Table E.6 NN, Network Neighbors, 95% Confidence Intervals

<table><tr><td>Lag</td><td colspan="2">MSE(Demand, InDemand) — MSE(Demand, InDemand, Second Tier InDemand)</td></tr><tr><td>1</td><td>0.0015</td><td>0.0017</td></tr><tr><td>2</td><td>0.0001</td><td>0.0002</td></tr><tr><td>3</td><td>0.0011</td><td>0.0012</td></tr><tr><td>4</td><td>0.0004</td><td>0.0006</td></tr><tr><td>5</td><td>-0.0004</td><td>-0.0002</td></tr><tr><td>6</td><td>0.0001</td><td>0.0003</td></tr><tr><td>7</td><td>0.0005</td><td>0.0007</td></tr></table>

Appendix F. Sensitivity Analysis  
Figure F.1 AR Model (No InDemand Information)  
![](/api/attachments/R2S7FXPN/fulltext/images/c61543cc9c82f9f55ed6086fd7541d6ba93d1fc5d1a6002b9750bfdd5f02a1f0.jpg)

Figure F.2 NN Model (No InDemand Information)  
![](/api/attachments/R2S7FXPN/fulltext/images/2968a8092fb9273b020b9ed9ee005ad127b256ebfb34dd7733889f5a75e6b7fc.jpg)

Figure F.3 AR Model: Demand and InDemand vs. Demand and Average Category Demand  
![](/api/attachments/R2S7FXPN/fulltext/images/9f41ed7e418d8b151e14f2c0459cfd2c3f285d5f7dae0c7c7d5ac1cb738b4858.jpg)

Figure F.4 NN Model: Demand and InDemand vs. Demand and Average Category Demand  
![](/api/attachments/R2S7FXPN/fulltext/images/da95b7d6ecf8c36aadb20482e23ea38baecac564362a95293eddb3db8d9f742c.jpg)

## Appendix G. Robustness Check—Using an Alternate Product Network

We utilize a product network from another retailer to evaluate the robustness of our main finding, i.e., that an entity’s future demand is more accurately predicted when combining its historical demand with additional network information.

Table G.1 AR, 95% Confidence Intervals

<table><tr><td>Lag</td><td colspan="2">MSE(Demand) – MSE(Demand, InDemand)</td><td colspan="2">MSE(Demand, InDemand) – MSE(Demand, InDemand, PageRank)</td><td colspan="2">MSE(Demand, InDemand) – MSE(Demand, InDemand, Local clustering)</td></tr><tr><td>1</td><td>0.00005</td><td>0.00009</td><td>0.00000</td><td>0.00000</td><td>0.00000</td><td>0.00000</td></tr><tr><td>2</td><td>0.00004</td><td>0.00008</td><td>0.00000</td><td>0.00000</td><td>0.00000</td><td>0.00000</td></tr><tr><td>3</td><td>0.00004</td><td>0.00007</td><td>0.00000</td><td>0.00000</td><td>0.00000</td><td>0.00000</td></tr><tr><td>4</td><td>0.00004</td><td>0.00007</td><td>0.00000</td><td>0.00000</td><td>0.00000</td><td>0.00000</td></tr><tr><td>5</td><td>0.00004</td><td>0.00007</td><td>0.00000</td><td>0.00000</td><td>0.00000</td><td>0.00000</td></tr></table>

Table G.2 NN, 95% Confidence Intervals

<table><tr><td>Lag</td><td colspan="2">MSE(Demand) – MSE(Demand, InDemand)</td><td colspan="2">MSE(Demand, InDemand) – MSE(Demand, InDemand, PageRank)</td><td colspan="2">MSE(Demand, InDemand) – MSE(Demand, InDemand, Local clustering)</td></tr><tr><td>1</td><td>0.000006</td><td>0.00001</td><td>0.0007</td><td>0.0012</td><td>0.0008</td><td>0.001</td></tr><tr><td>2</td><td>0.0007</td><td>0.0011</td><td>0.0001</td><td>0.0003</td><td>0.0001</td><td>0.0003</td></tr><tr><td>3</td><td>0.0002</td><td>0.0005</td><td>0.0009</td><td>0.0013</td><td>0.0005</td><td>0.0007</td></tr><tr><td>4</td><td>0.0001</td><td>0.0004</td><td>0.0006</td><td>0.0008</td><td>0.0001</td><td>0.0002</td></tr><tr><td>5</td><td>0.0005</td><td>0.0009</td><td>-0.0001</td><td>0.0003</td><td>-0.0005</td><td>-0.0003</td></tr></table>

Data. We collected 10 consecutive days’ worth of data from the Barnes & Noble website (approximately ∼5 million books).

We conducted SalesRank-to-demand conversions and outlier cleaning processes similar to those described above for the Amazon sales data. For each book, we generated a five-day history of demand, PageRank, and local clustering coefficient values, as well data on the demand for the book’s immediate neighbors.<sup>12</sup> Finally, we generated a sample of approximately \$540,000 observations, evenly divided over five days.

The first three days (about 320,000 observations) were used as a training set, and the remaining two days (about \$220,000 observations) were utilized as a validation set.

Results. Figure G.1 presents prediction accuracy results for a Naïve model (using the node’s past demand at time t − 1 as a proxy for its demand at time t), an AR model using the nodes’ Historical Demand, and for an AR model that also utilizes neighboring nodes’ demand. Figure G.2 presents prediction accuracy results for an NN model using the nodes’ Historical Demand and for NN models that also take into account neighboring nodes’ demand, as well as PageRank and local clustering information. Tables G.1 and G.2 respectively present the 95% bootstrap confidence intervals.

As is evident from these results, adding information on neighboring nodes significantly improves predictive accuracy also in the case of an alternative product network for both AR and NN models. In addition, as in the case of the Amazon network, the NN model provides considerably better predictive accuracy compared with the AR model, and

Figure G.1 Barnes and Noble Network: AR Model  
![](/api/attachments/R2S7FXPN/fulltext/images/4e5b701309c71eb3f6c1dbf40a085b953d1ee66bf686ecfbd7d72f3d5f6dd35a.jpg)  
Note. Results for models including Demand and InDemand as well as PageRank or local clustering are not presented in Figure G.1, since their lines totally overlap with the lines presenting the results for the AR model with Demand and InDemand.

Figure G.2 Barnes and Noble Network: NN Model  
![](/api/attachments/R2S7FXPN/fulltext/images/4699cfcd5154afc51a626b2e47b2f7ef22f0567c408fb404d1fa8d62d69ed07c.jpg)  
inclusion of PageRank or local clustering information generally adds more power to the NN-based prediction model than to the AR model.

## Appendix H. Demand Distribution

Figure H.1 shows the demand distribution over the validation set. Note that, by definition, books with no incoming links (i.e., in degree = 0) could not be included in our

Figure H.1 Demand Distribution  
![](/api/attachments/R2S7FXPN/fulltext/images/291c6ecb883130f5ca9d71dc12e25b773d1881f87c5ad8817aecb44e253814d9.jpg)  
data set. As detailed in §3.1 we also filtered out the top and bottom deciles.

## References

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6):734–749.

Aral L, Muchnik S, Sundararajan A (2009) Distinguishing influencebased contagion from homophily-driven diffusion in dynamic networks. Proc. Natl. Acad. Sci. USA 106(51):21544–21549.

Bampo M, Ewing M, Mather D, Stewart D, Wallace M (2008) The effects of the social structure of digital networks on viral marketing performance. Inform. Systems Res. 19(3):273–290.

Bapna R, Gupta A, Rice S, Sundararajan A (2013) Trust, reciprocity and the strength of ties in online social networks. Working paper,

Brin S, Page L (1998) The anatomy of a large-scale hypertextual web search engine. Comput. Networks ISDN Systems 30(1–7):107–117.

Brynjolfsson E, Hu Y, Smith MD (2003) Consumer surplus in the digital economy: Estimating the value of increased product variety at online booksellers. Management Sci. 49(11):1580–1596.

Chakrabarti S, Dom B, Indyk P (1998) Enhanced hypertext categorization using hyperlinks. Proc. 1998 ACM SIGMOD Internat. Conf. Management of Data (ACM Press, New York), 307–319.

Chevalier J, Goolsbee A (2003) Measuring prices and price competition online: Amazon.com and BarnesandNoble.com. QME-Quant. Mark. Econom. 1(2):203–222.

Dhar V (2011) Prediction in financial markets: The case for small disjuncts. ACM Trans. Intelligent Systems Technologies 2(3):79.

Dhar V (2013) Data science and prediction. Comm. ACM 56(12): 64–73.

Dhar V, Stein R (1997) Seven Methods for Transforming Corporate Data into Business Intelligence (Prentice-Hall, Upper Saddle River, NJ).

Domingos P, Richardson M (2001) Mining the network value of customers. Proc. Seventh ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining (ACM Press, New York), 57–66.

Godes D, Mayzlin D (2004) Using online conversations to study word-of-mouth communication. Marketing Sci. 23(4):545–560.

Hastie T, Tibshirani R, Friedman J (2009) The Elements of Statistical Learning: Data Mining, Inference, and Prediction (Springer-Verlag, New York).

Hill S, Provost F, Volinsky C (2006) Network-based marketing: Identifying likely adopters via consumer networks. Statist. Sci. 21(2):256–276.

Hinton GE (2002) How neural networks learn from experience. Polk TA, Seifert C, eds. Cognitive Modeling (MIT Press, Cambridge, MA), 181–195.

Kiss C, Bichler M (2008) Identification of influencers: Measuring influence in customer networks. Decision Support Systems 46(1):233–253.

Kleinberg J (2007) Challenges in mining social network data: Processes, privacy, and paradoxes. Proc. 13th ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining (ACM Press, New York), 4–5.

Lichtenwalter RN, Lussier JT, Chawla NV (2010) New perspectives and methods in link prediction. Proc. 16th ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining (KDD’10) (ACM, New York), 243–252.

Lippman RP (1987) An introduction to computing with neural nets. IEEE ASSP Magazine (April) 4(2):4–22.

Ma L, Montgomery A, Krishnan R (2009) Homophily or influence? An analysis of purchase decisions in a social network context. Workshop Inform. Systems Econom., 270–286

Macskassy SA, Provost F (2007) Classification in networked data: A toolkit and a univariate case study. J. Machine Learn. Res. 8(May):935–983.

Marsden J (2008) The Internet and DSS: Massive, real-time data availability is changing the DSS landscape. Inform. Systems E-Bus. Management 6(2):193–203.

Oestreicher-Singer G, Sundararajan A (2012) The visible hand? Demand effects of recommendation networks in electronic markets. Management Sci. 58(11):1963–1981.

Popper K (1968) Conjectures and Refutations: The Growth of Scientific Knowledge (Basic Books, New York).

Provost F, Zhang X, Dalessandro B, Murray A, Hook R (2009) Audience selection for on-line brand advertising: Privacy-friendly social network targeting. Proc. Fifteenth ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining (ACM Press, New York).

Rumelhart DE, McClelland JL (1984) Parallel Distributed Processing: Explorations in the Microstructure of Cognition (MIT Press, Cambridge, MA).

Sen P, Namata G, Bilgic M, Getoor L, Gallagher B, Eliassi-Rad T (2008) Collective classification in network data. AI Magazine 29(3):93.

Shmueli G (2010) To explain or to predict?. Statist. Sci. 25(3): 289–310.

Shmueli G, Koppius O (2011) Predictive analytics in information systems research. MIS Quart. 35(3):553–572.

Sobehart J, Keenan S, Stein R (2001) Benchmarking quantitative default risk models: A valuation methodology. Algo Risk Quart. 4(1/2):55–69.

Song M, van der Aalst W (2008) Towards comprehensive support for organizational mining. Decision Support Systems 46(1): 300–317.

Watts DJ, Strogatz S (1998) Collective dynamics of “small-world” networks. Nature 393(6684):440–442.

Werbos PJ (1974) Beyond regression: New tools for prediction and analysis in the behavioral sciences. Unpublished doctoral dissertation, Harvard University, Cambridge, MA.

Zhang G, Patuwo BE, Hu MY (1998) Forecasting with artificial neural networks: The state of the art. Int. J. Forecasting 14(1):35–62.
