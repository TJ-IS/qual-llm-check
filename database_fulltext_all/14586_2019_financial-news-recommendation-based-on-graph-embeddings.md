---
otero_id: 14586
otero_key: "RCB5VZWA"
title: "Financial news recommendation based on graph embeddings"
authors: "Jiangtao Ren; Jiawei Long; Zhikang Xu"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113115"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Financial news recommendation based on graph embeddings

Jiangtao Ren\*, Jiawei Long, Zhikang Xu

![](/api/attachments/RCB5VZWA/fulltext/images/dc61ba429a5e15d48a165d271de5cc1947457235adaa03c7fdd28487faff8be9.jpg)

School of Data and Computer Science, Guangdong Province Key Lab of Computational Science, Sun Yat-sen University, Guangdong 510275, People's Republic of China

## A R T I C L E I N F O

Keywords: News recommendation Knowledge graph Graph embeddings

## A B S T R A C T

Most of the existing methods are not enough for securities companies to make their decisions on recommending the most suitable financial news to a specific user. On the one hand, such news articles often contain externa knowledge related to companies and stocks. On the other hand, it is important for financial news re commendations to dynamically measure users' interests since people are usually interested in multiple specific concepts, companies, stocks and industry categories. To address the above challenges, we start by building a heterogeneous graph consisting of users, news, companies, concepts, and industry categories. Then, the graph embeddings of the nodes are generated using node2vec, and user-news relatedness can be computed based on them. Since financial news articles are time-sensitive, we propose an incremental method for alleviating the computational eficiency problem. The combination of a node2vec-based recommendation method and the incremental method can achieve a good balance between time eficiency and recommendation accuracy in the financial news recommendation task. Our methods are evaluated on a real-world dataset from a Chinese securities company, are shown to outperform other commonly used baseline models, can provide decision support for companies choosing news to be recommended to target users and allow users to obtain personalized real-time news recommendations.

## 1. Introduction

With the development of the Internet, people prefer to read news on websites or in mobile phone applications instead of accessing tradi tional media such as newspapers and TV. A prominent problem of online news platforms is that the volume of news articles is overwhelming for users. Financial services companies are focusing on recommending news to users on mobile phones to attract them to invest in specific stocks. Therefore, personalizing financial news for specific users is a very great challenge for both academia and industry [1].

Financial news has some particular characteristics, such as the timeliness of events and complexity of company relations. Fig. 1 shows that the financial articles usually mention companies and stocks, underlined in the figure. On the one hand, such articles contain complex external knowledge related to companies and stocks; on the other hand, readers of financial news are usually interested in multiple specific concepts, companies, stocks and industry categories, which increases the dificulty of user profiling. Moreover, it is clear that financial news articles are highly time-sensitive, as indicated by the words in red in Fig. 1, and readers will switch from out-of-date news to newer news frequently, which poses an online update problem. Simple neural network models have no advantage in these problems.

To address the external knowledge problem of news, researchers have applied knowledge-based techniques to news recommendation. To this end, in 2018, Wang et al. proposed a deep knowledge-aware network [2]. The authors used a knowledge graph to extract latent knowledge-level connections among news and build user embeddings to more accurately portray users' browsing preferences. Another study proposed a safe medicine recommendation method via medical knowledge graph embeddings and introduced an interesting idea of updating embeddings to deal with the cold-start issue that merited study [3]. Zihayat et al. realized the weakness of click analysis and developed a novel news recommendation system based on the news utility model to determine users' genuine interests [4]. To improve the diversity of training data and the performance of a recommendation model, Geva et al. augmented numerical market data with textual news data and used data mining methods in forecasting stock returns during intraday trading [5].

Inspired by the above studies, this paper applies the knowledge graph and graph embedding techniques to the task of financial news recommendation. To deal with external knowledge related to companies and stocks covered by financial news, a high-quality graph called the securities subgraph, containing companies, concepts and categories, is constructed. To dynamically measure users' preferences and to

Text:A股首只“独角兽”将正式闪亮登场。据药明康德公告，公司将于2018年5月8日在上交所挂牌上市，股票代码为“603259”。市场人士认为，近来新股表现不错，药明康德又颇为“重量级”，不太可能在极短时间内开板，因此它的上市，更大是对市场产生心理上的影响，有可能助推近期表现亮丽的医药板块。今年以来，医药板块走势良好。5月7日收盘，医药板块指数大涨2.2%，本月已大涨了4.93%。

The first unicorn of A shares will be officially launched. According to WuXi Apptec's announcement, the company will be listed on the Shanghai Stock Exchange on May 8, 2018, with the stock code "603259". Market participants believe that the recent performance of new shares is good, and WuXi Apptec is so heavyweight that it is unlikely to open in a very short time. Its listing will bring more psychological impact on the market and may boost the recent performance of the medical sector. This year, the pharmaceutical sector is in good shape. In May 7, the pharmaceutical sector index rose 2.2%, which has risen 4.93% this month.

Company: WuXi Apptec

Category: Biologicals

Concept: AH Shares & Medicine

Fig. 1. Example of financial news mentioning a company, related concepts and a category.

uncover the deep correlation between news, a subgraph of users and a subgraph of news are built according to not only the click behaviors of users but also their stock transaction records. After linking the subgraphs to the securities subgraph, a heterogeneous knowledge graph is constructed, and its embeddings can be obtained using a graph embedding algorithm node2vec [6], modeling the topological relations and semantic information of the graph. The graph embedding technique can deal with the problem of user profiling and establish user-news relatedness according to the embeddings, which will be used in the recommendation process. To address the online update problem, an incremental embedding updating method is proposed in this paper that trains the embeddings of the core graph containing rarely changed nodes and represents the latest news with the embeddings of related nodes. The cold-start problem can be alleviated by this method. Given a news article that has not been viewed or rated by people, the embed ding of that article can be represented by the generated embeddings of concepts, industry categories and stock names contained in the article.

To satisfy the eficiency and performance requirements of realworld recommendation scenarios, we design a graph embeddings-based financial news recommendation framework, where an incremental embedding update model is responsible for the embeddings of the newly emerging nodes during the stock market's trading hours to ensure the eficiency of the framework, while a normal graph embedding model is utilized to train on the entire heterogeneous graph to obtain the embeddings for all nodes to ensure acceptable performance.

Fig. 2 shows several illustrative examples of various recommendation scenarios. Our models focus on solving the problems in these scenarios.

Scene 1: (General) Based on the browsing records, Cindy can be connected to Amazon. The next connection is made because Amazon belongs to the internet software and service industry; subsequently, news on “AT&T” is recommended to Cindy.

Scene 2: (User cold start) Although no browsing records are available for Alice, there are transaction records. It is known that she bought shares of Google, and she can be connected to Alphabet. Because Alphabet belongs to the internet software and service industry, news on “AT&T” is subsequently recommended to her.

Scene 3: (News cold start) A news article “5G” has not been viewed by any user. Using a named entity recognition method, we can connect it to the 5G concept. Because Bob has viewed an article about this concept, the news “5G” can be recommended to Bob according to his browsing records.

Scene 4: (User interest measure) There is a hidden relationship between Alice and Bob, and their interests in fact have certain similarities. They both focus on the technology industry. We can easily measure this relationship by constructing their graph embeddings, but it is not as clear how the same can be accomplished using collaborative filtering or content-based methods.

In fact, the latter approaches can be used in the above recommendation scenarios, but using the method of embeddings can quantify the strength of the correlation.

The contributions of this paper can be summarized as follows. The first is the introduction of NNR, a graph-based method for financial news recommendation that outperforms the commonly used baselines. The second is developing INNR, an incremental approach that makes the recommendation process more eficient. The main contribution of our work is combining NNR and INNR to create a graph embeddingsbased financial news recommendation framework that can achieve a good balance between time eficiency and recommendation accuracy in the financial news recommendation task. The framework provides decision support for companies that need to choose the news to be recommended to the target users and enables the users to obtain personalized real-time news recommendations.

![](/api/attachments/RCB5VZWA/fulltext/images/718978e66a548921fcaef3e5690115dc55f83776b4cb48b4e0053359546ec743.jpg)  
Fig. 2. Examples of various recommendation scenarios.

Our method is not limited to financial news recommendations and can also be applied to other recommendation tasks. For example, our method can also be useful in recommending advertisements on the Internet. E-commerce platforms can easily obtain the records of items a user has bought on the platform and items he/she has viewed. Such records can be used to construct the item subgraph, where various items can be related to diferent price ranges, brands and functions that, together with the items themselves, can be regarded as the entities in the item subgraph. Additionally, the items can be linked to each other ac cording to some common co-occurrence relationship. The users of the platform can be used to construct the user subgraph, while the advertisements for items can be regarded as entities of the advertisement subgraph. The item subgraph acts as a bridge linking the users and the advertisements. In this scenario, we need to discover the hidden relevance between the users and the advertisements, which is similar to what we have done for users and financial news in this study.

The rest of the paper is organized as follows. Section 2 defines the financial news recommendation problem explored in this study, and Section 3 presents the proposed models. The experimental settings and detailed analysis are reported in Section 4. Then, Section 5 briefly reviews related studies of news recommendation. Finally, we conclude the paper and outline directions for future research in Section 6.

## 2. Problem definition

Due to various reasons, such as data access rights and restrictions on browsing records, we can only obtain a small quantity of browsing data of low quality in a real-world recommendation scenario. Therefore, we need to add extra information to improve recommendation performance. Considering that users regard stock transactions comparatively seriously and that securities companies can obtain historical stock transaction records of users, the usage of such records can make recommendations more accurate and reliable, providing decision support to securities companies.

We formally define the financial news recommendation problem as follows.

Problem Given a user u and datasets $D _ { b }$ and D of his/her browsing and transaction records, recommending financial news to the user is predicting the edges from u to news dataset N. The output is a set of news $N _ { u }$ with maximum user interest.

To solve the above problem well, it is necessary to efectively predict the edges from a user to some news based on complex real-world data. This requires us to properly map the users and the news to the same vector space, measure the distances between the vectors, and obtain the user-news relevance.

In what follows, our recommendation methods will be described, and a set of articles with maximum user interest will be recommended to users based on these methods.

## 3. Proposed models

In this paper, a graph embeddings-based financial news recommendation framework is proposed to attain a good balance between time eficiency and recommendation accuracy in the financial news recommendation task.

The framework is shown in Fig. 3, where a model for the incremental update of embeddings is responsible for the embeddings of the newly emerging nodes during the stock market's trading hours to ensure the eficiency of the framework, while a normal graph embeddings model is trained on the entire heterogeneous graph to obtain the em beddings for all nodes during the stock market's closing hours to ensure the good quality of the learned embeddings.

## 3.1. Node2vec-based news recommendation

An overview of the Node2vec-based news recommendation method is shown in Fig. 4. This model consists of three parts: graph construction, training embeddings, and news recommendation.

To establish the relationship between users and news, a securities knowledge graph that includes stocks, industries, concepts, and other entities should be constructed first; then, the relationships between these entities, such as the upstream and downstream relationships between stocks, relationships between stocks and industries, and relationships between stocks and concepts, can be established.

The users are linked to the securities knowledge graph based on their stock transaction records. Information extraction and labeling of news are performed to extract the stock, industry and concept information involved in the news. Based on the extracted information, the news articles are also linked to the securities knowledge graph. As a result, the relationship between users and news is established in directly.

Node2vec is utilized to generate embeddings of the entire graph and make recommendations based on the embeddings of users and news according to the cosine similarity between the embeddings that is used to calculate the preference order of the candidates.

## 3.2. Graph construction

The heterogeneous knowledge graph is composed of three parts: the securities subgraph, the user-related subgraph, and the news-related subgraph. The user-related subgraph is based on the users' stock transaction records, while the news-related subgraph is based on the stocks, categories, and concepts related to the news articles. The subgraphs facilitate dynamic measurement of users' preferences and extraction of correlations between news articles. To analyze the external knowledge of companies and stocks, the securities subgraph that includes companies, stocks, concepts, and industry categories is built. In the knowledge graph, the users can be indirectly related to the articles through the securities subgraph.

![](/api/attachments/RCB5VZWA/fulltext/images/8aba52e90697494d4fbebe2929fc5663211a6790a9957a2a919d1e16b30a5e08.jpg)  
Fig. 3. Graph embeddings-based financial news recommendation framework.

## 3.2.1. Securities subgraph

The securities subgraph describes the entities in the securities market as well as the relations among these entities. It can be regarded as a set of triples $( i , r , j )$ , where $i , j \in E , r \in R ,$ and E is a set of entities, and R is a set of the relations among them.

The entities include stocks, companies, concepts, and categories. The companies in the graph are equivalent to stocks that can be owned by users. The concepts are the most popular keywords pertaining to shares, such as blockchain, 5G, and Tesla. The categories in this paper are the industry categories released by SWS Research, a securities research institute in China. News articles can be linked to various companies, concepts, and categories, since an article may mention the respective keywords. A company is capable of investing in other companies, so there are edges among diferent companies. At the same time, there are some concepts and categories related to companies.

These entities can be regarded as tags of news articles and can be obtained using named entity recognition (NER) methods. In our study, the NER method used is based on Bi-LSTM and CRF [7], and the NER procedure is as follows:

(1) Three thousand pieces of news are randomly sampled from all articles and manually labeled with four types of entities mentioned in the text, namely, company, stock, industry, and concept.

(2) A word2vec model pretrained on all articles is used to represent the words in the news with word embeddings, while five labels (0-

![](/api/attachments/RCB5VZWA/fulltext/images/685a84b20c7b7159bc579d978d750f5fc01cf72f3f71465d7c45ad0ae33ca3d1.jpg)  
Fig. 4. Framework of the NNR model.

Input Text

[据 国外媒体 Intercept 报道 谷歌 计划 在 中国 推出符合 中国法律 规定 的 搜索引擎

(According to foreign media Intercept reports, Google plans to launch a search engine in China that complies with Chinese laws.)

Word Embeddings Sequence

Labelled Entities Sequence

$$
\left[ w _ {1}, w _ {2}, w _ {3}, w _ {4}, w _ {5}, w _ {6}, w _ {7}, w _ {8}, w _ {9}, w _ {1 0}, w _ {1 1}, w _ {1 2}, w _ {1 3}, w _ {1 4} \right]
$$

$$
[ 4 4 0 4 0 4 4 4 4 4 4 4 4 3 ]
$$

0-company, 1-stock, 2-industry, 3-concept, 4-other

Fig. 5. Example of the data representation used in the NER process.

company, 1-stock, 2-industry, 3-concept, and 4-other) are used to represent the entities in the input sequences. An example of an input text, a sequence of word embeddings and a sequence of la beled entities are shown in Fig. 5.

(3) The sequences of word embeddings are used as the input of the bi-LSTM-CRF model, and the output is the entities' labels for each word. In this part, the ground truth values are the manually labeled sequences of entities. The loss function of the model is the cross entropy.

(4) Two thousand one hundred news articles are used to train the model, and 900 articles are used for evaluation.

(5) After the model has been trained, new articles are preprocessed with the same word2vec model and input into the well-trained model to obtain the companies, stocks, industries, and concepts involved in those articles.

(6) Using the entities mentioned in the new articles, the news can be linked to the graph for subsequent operations.

## 3.2.2. User-related subgraph

The user-related subgraph is represented as $G _ { u } = ( U \cup S , r _ { u s } ) .$ , where U is a set of users and S is a set of stocks. Variable $r _ { u s }$ denotes the set of edges. If user $u _ { i }$ buys or focuses on stock $s _ { j } ,$ there will be an edge $r _ { i j }$ between them, and weight $w _ { i j }$ of the edge is defined as the total number of times user $u _ { i }$ has bought stock $s _ { j } .$ Relations between users and stocks include users' behaviors such as buying and following.

## 3.2.3. News-related subgraph

The news-related subgraph is represented as $G _ { n } = ( N \cup S \cup C o \cup C a , r _ { n } )$ , where N is a set of news, S is a set of stocks, Co is a set of concepts, and Ca is a set of categories. Variable $r _ { n }$ denotes the set of edges. If news article n mentions stock $s _ { j } ,$ there will be an edge $r _ { i j }$ between them, and weight $w _ { i j }$ of the edge will be set to 1 if edge $e _ { i j }$ exists. The same is true for concepts and categories.

## 3.3. Training embeddings

This section will discuss how the embeddings' learning model is used to encode the heterogeneous knowledge graph in the latent space and its optimization method.

Algorithms for graph embeddings, as methods of representing networks, have been applied in many practical scenarios. In particular, the efectiveness and stability of node2vec have been verified in many related studies. Thus, it is applied to the heterogeneous knowledge graph to obtain the embeddings of the nodes in this paper. In fact, using other graph embedding algorithms can still demonstrate the advantages of our financial knowledge graph. We can also apply other superior embedding algorithms to accomplish the same task if necessary.

The existing node2vec algorithm proceeds as follows. The knowl edge graph $G = ( V , E )$ is used to learn from nodes that a mapping function allows for feature representations $f \colon V \to R ^ { d }$ in the form of a matrix with $| V | \times d$ parameters. For every source node $\iota \in V , N _ { S } ( u ) \in V$ is defined as a network neighborhood of node u generated with a neighborhood sampling strategy S.

Then, the objective function is optimized, which maximizes the logprobability of observing a network neighborhood $N _ { S } ( u )$ for node u conditional on its feature representation given by f:

$$
\max _ {f} \sum_ {u \in V} \log P r (N _ {S} (u) | f (u))\tag{1}
$$

• Conditional independence implies that

$$
P r (N _ {S} (u) | f (u)) = \prod_ {n _ {i} \in N _ {S} (u)} \log P r (n _ {i} | f (u))\tag{2}
$$

Symmetry in the feature space means that

$$
P r (n _ {i} | f (u)) = \frac {\exp (f (n _ {i}) \cdot f (u))}{\sum_ {v \in V} \exp (f (v) \cdot f (u))}\tag{3}
$$

Given conditional independence and symmetry in the feature space, Eq. (4) can be written as follows:

$$
\max _ {f} \sum_ {u \in V} \left[ - \log Z _ {u} + \sum_ {n _ {i} \in N _ {S} (u)} f (n _ {i}) \times f (u) \right]\tag{4}
$$

where $Z _ { e } = \sum _ { \nu \in G }$ exp( ( ) ( ))f e f v is the per-node partition function that is approximated using negative sampling since it is expensive to compute for large networks [8]. The optimization is performed using stochastic gradient ascent over the parameters defining $f ,$ which attempts to maximize the dot product between vectors of the same neighborhood.

## 3.4. News recommendation

In this part, the node2vec-based news recommendation (NNR) model is proposed that uses the embeddings of articles and users to obtain the relevance between users and news and to subsequently complete the task of news recommendation. To calculate the preference order of the articles, a distance between two nodes is introduced. As Eq. (5) shows, the cosine similarity between the embeddings of a pair of nodes is used since the relatedness between them can be easily computed.

$$
\cos (v _ {1}, v _ {2}) = \frac {v _ {1} \cdot v _ {2}}{| v _ {1} | \times | v _ {2} |} = \frac {\sum_ {j = 1} ^ {d} (v _ {1 j} \times v _ {2 j})}{\sqrt {\sum_ {j = 1} ^ {d} (v _ {1 j}) ^ {2}} \times \sqrt {\sum_ {j = 1} ^ {d} (v _ {2 j}) ^ {2}}}\tag{5}
$$

Above, d is the dimension of embeddings.

Given a user and the candidate financial articles, the user and articles are first projected onto their latent space, and top-k articles are subsequently selected. More precisely, given a user and the candidate news, the ranking scores of news are computed using Eq. (6), and news articles n with the top-k highest ranking scores are subsequently

![](/api/attachments/RCB5VZWA/fulltext/images/d991891292d085924c1e004d9625592447fd8bcf0903d40881e6ae69a22065fd.jpg)  
Fig. 6. Framework of the model for online updates.

selected as the recommendation.

$$
S (u, n _ {i}) = \cos (u, n _ {i})\tag{6}
$$

where u is the representation of user u, and $n _ { i }$ is the financial news article considered a candidate.

$$
N _ {u} = \sum_ {k = 1} ^ {K} \operatorname * {a r g m a x} _ {n _ {i} \in N} S (u, n _ {i})\tag{7}
$$

Eq. (7) is used to choose articles to be recommended, where K is the number of news articles needed, U is the set of target users, N is the set of candidate news articles, and $N _ { u }$ is the recommendation result for a given user.

## 3.5. Incrementally updating embeddings

In practice, ten billion news articles are needed for obtaining re commendations for millions of users, and it is time-consuming to train the embeddings for a large graph with as many as hundreds of billions of entities. At the same time, financial news change all the time, and online updates are inevitable in a real-world recommendation scenario. It is impractical to spend dozens of hours to determine the embeddings, considering the timeliness of news.

As a result, it is necessary to create a new method for determining the news and users' embeddings in a few minutes. To tackle this problem, an incremental node2vec-based news recommendation (INNR) is proposed. To reduce computation time, it is only necessary to train the embeddings of the core graph of entities that change rarely instead of the entire graph. Then, various strategies can be used to represent a new user or the latest news based on the core graph embeddings. Using the embeddings, user-news correlations can be calculated to recommend articles to users.

The core graph is the securities subgraph mentioned earlier. The reasons to choose it as the core graph are as follows:

Companies, concepts, and industry categories change seldom, while users and news are updated frequently. The embeddings of the se curities knowledge graph are relatively fixed.

The relationships among companies, concepts, and industry cate gories often reflect the external knowledge contained in financial news, i.e., the content-based information of articles.

Companies, concepts, and industry categories are obtained from users' stock transaction records. The analysis of such records may reflect users' reading preferences, which can help improve user profiling.

An example is shown here to illustrate more clearly the strategies for representing the new articles or users. Suppose that there is a news article denoted by $n _ { 1 } .$ It belongs to industry categories $c a _ { 1 }$ and $c a _ { 2 } .$ Additionally, it mentions several concepts and stocks represented by $c o _ { 1 } , c o _ { 2 }$ and $s _ { 1 } .$ .

Since $c a _ { 1 } , c a _ { 2 } , c o _ { 1 } , c o _ { 2 }$ and $s _ { 1 }$ are entities of the core graph, node2vec can be used to obtain the graph embeddings of these entities. The embeddings form set V of size s. The following strategies are used to represent new articles or users.

Strategy 1: The average embedding for N can be simply calculated, and $n _ { 1 }$ can be represented as $\nu _ { S 1 }$ . The average can retain the common features of data, but data outliers can easily afect it.

$$
v _ {S 1} = \frac {1}{s} \sum_ {v _ {i} \in V} v _ {i}\tag{8}
$$

Strategy 2: To avoid the influence of the outlying nodes, the embedding of the node with the shortest Euclidean distance from other nodes is chosen to represent $n _ { 1 }$ as $\nu _ { S 2 } .$ . However, this method will lose information about other nodes.

$$
v _ {S 2} = \underset {v _ {i}} {\operatorname{argmin}} (\sum_ {v _ {i} \in V} \sum_ {v _ {j} \in V, i! = j} E (v _ {i}, v _ {j}))\tag{9}
$$

where $E ( u , \nu )$ is the Euclidean distance between vector u and vector v.

Strategy 3: To combine the strengths of the above strategies, the average embedding is calculated after dropping k outliers, and $n _ { 1 }$ is subsequently represented as v .

$$
v _ {S 3} = \frac {1}{s} \sum_ {1} ^ {s - k} \underset {v _ {i}} {\operatorname{argmin}} (\sum_ {v _ {i} \in V ^ {\prime}} \sum_ {v _ {j} \in V ^ {\prime}, i! = j} E (v _ {i}, v _ {j}))\tag{10}
$$

$$
V ^ {\prime} = V ^ {\prime} - (\underset {v _ {i}} {\operatorname{argmin}} (\sum_ {v _ {i} \in V ^ {\prime}} \sum_ {v _ {j} \in V ^ {\prime}, i! = j} E (v _ {i}, v _ {j})))\tag{11}
$$

For an existing article n, the learned embedding n is used to represent that news. For a new article n that has no relations with users, the embeddings of stocks, companies, concepts, and categories mentioned in that article are used to represent it, as shown in Fig. 6.

Similar strategies can be used to represent users.

INNR can allow for online updates and resolve the cold-start issue of users and news. Even for the articles that are never viewed or rated by users, it is still capable of computing the content-based features from the embeddings of concepts, industry categories, and other articles from similar neighborhoods.

## 4. Experiment and evaluation

## 4.1. Experiment details

## 4.1.1. Data preparation

The dataset used to evaluate the proposed models contains realworld data from GF Securities, one of the top five securities companies in China with more than 9 million customers. The browsing records used in our study were obtained from the mobile application of GF Securities, and the transaction data correspond to the actual daily stocks transactions of users. These data are authentic and highly reli able and have been rigorously anonymized to ensure the privacy of users. The diversity of user types guarantees the representativeness of the data.

The source dataset contains 22,404 users and 64,881 news articles from May 2017 to May 2018. We randomly sample users and news based on the time range of transaction records and browsing records to extract the data. Additionally, the entities referred to in the news articles are 59,267 companies, 2013 concepts, and 226 industry categories.

To ensure the adequate performance of models, we remove some poor-quality data from the source dataset. The removed data are related to the users with no trading and browsing records.

The reasons we remove such data are as follows:

(1) The data related to the mentioned users increase the sparseness of the graphs and have a negative impact on the training of our models.

(2) These users do not have browsing records that can be used as the ground truth, so it is not possible for us to validate our predicted results by comparison to users' real-world browsing behaviors.

After the removal of poor-quality data, 3800 users and 64,881 articles are considered in the following tests. The stock transaction records and the browsing records of these users are used to train and test the models.

We separate the training and testing data specifically to avoid overfitting of models and to ensure the models' generalizability. In the cold-start scenario, the training data are users' transaction data, and the testing data are users' news browsing records. In contrast, in a normal scenario. the training data are the users' transaction data and the records of browsing news set $N _ { 1 }$ , while the records of browsing news set $N _ { 2 }$ are used as the testing data. The simplified dataset contains 127,865 entities and 339,222 relations, as shown in Table 1.

## 4.1.2. Parameter configuration

Parameters P and Q of node2vec are optimized on the testing data. The values of P and Q are 0, 0.25, 1 and 4. There are nine combinations of P and Q. P is called the return parameter and controls the possibility of returning to a previously visited node. Q is called the in-out parameter and controls the movement further away from the source node. Using diferent values of P and $Q ,$ node2vec can simulate a random walk strategy similar to breadth-first or depth-first search. For INNR, the percentage of dropped out outliers should be optimized.

The other parameters are configured as follows: the dimension of the embedding vector d = 128, the walk length l = 80, the number of walks $n = 1 0 _ { : }$ , the window size $k = 1 0 ,$ , and the number of epochs $e = 1 0$

Table 1  
Entities and relations in the graph.

<table><tr><td>Entities</td><td>Relations</td></tr><tr><td>Users 3800</td><td>User-stock 14,516</td></tr><tr><td>News 64,881</td><td>User-news 2274</td></tr><tr><td>Stocks 59,517</td><td>Stock-related 102,938</td></tr><tr><td>Categories 226</td><td>News-related 194,296</td></tr><tr><td>Concepts 2059</td><td></td></tr></table>

## 4.1.3. Evaluation index

## RPI rate

It is dificult to directly assess whether the model recommendation results fit the users' preferences by only using the indicators of precision and recall. Hence, an evaluation protocol is defined to determine whether the recommendations are compatible with the users' preferences. The rate of recommendation-preference interactions (RPIs) is the ratio of the number of accurate recommendations to the total number of recommendations. Here, if the articles recommended to users belong to categories matching those of the actually browsed articles, the recommendation is considered accurate.

For example, consider three news articles, represented by $n _ { 1 } , n _ { 2 }$ and $n _ { 3 } ,$ that are recommended to a user. These articles have been assigned categories ca and $c a _ { 2 } .$ In this example, the user has browsed articles $n _ { 4 }$ and $n _ { 5 }$ belonging to categories $c a _ { 2 }$ and $c a _ { 3 } .$ The recommendation is considered successful since there is a common category $c a _ { 2 }$ for the recommendation result and browsing history.

## Computation time

The sum of the training and testing times, called the recommendation time, is used to represent the computational resource requirements of the methods. Since all evaluated methods access data in memory, the training and testing times correspond to computations. The training time reported in this paper is the time required to obtain the embeddings, and the testing time is the time needed to load the news texts and the user data, complete the similarity matching based on the trained embeddings and recommend the news to the users. All experiment have been performed on a single processor core. The hardware configuration is Intel(R) Xeon(R) E5-2620 v3 CPU operating at 2.40 GHz and 32 GB of RAM.

All experiments in this paper recommend three articles to each user. The best score of each model is chosen from ten sets of experiments to represent its performance. The average time of each group is regarded as the computation time.

## 4.2. Result summary

In this part, all the news and users in the dataset are represented by N and U, and a time point t is selected, so the articles before t are represented by $N _ { 1 } ,$ and articles after t are denoted by $N _ { 2 } ,$ where , and $\left| N _ { 1 } \right|$ $\left| N _ { 2 } \right| = 7 : 3 .$ A total of 3800 users were randomly divided into two parts, denoted by $U _ { 1 }$ and $U _ { 2 } ,$ where $\left| U _ { 1 } \right| : \left| U _ { 2 } \right|$ is 7:3. For clarity, browsing records containing news in N are denoted by $D a t a _ { N _ { 1 } } ^ { b }$ and browsing records containing news in $N _ { 2 }$ by Data $\cdot _ { N _ { 2 } } ^ { b }$ . Transaction record of users in U are denoted by Data<sup>t</sup> .

## 4.2.1. Node2vec-based news recommendation models

This section explores whether the node2vec-based models can perform well by only using the stock transaction records of users. Only Data<sup>t</sup> are used to train the models because in the real-world recommendation scenarios, it is dificult to obtain high-quality and complete users' browsing data. It is better to use only stock transaction records that are of better quality and have higher confidence to train the node2vec-based models.

NNR is efective in case of the static graph where the users and news seldom change, while INNR can do well in performing online updates and cold-start scenarios. Hence, the training and testing data are as signed to the models according to Table 2.

In the case of NNR, all news and users are considered in the construction of the knowledge graph that consists of the securities subgraph and two other subgraphs. The securities subgraph contains the stocks, companies, concepts and industry categories, preserving the relevant background knowledge of securities. The user-related subgraph links the users to stocks according to the stock transaction records, while the news-related subgraph links the news articles to stocks, companies, concepts and industry categories based on the results of short text classifiers. Since the browsing records are unused, there are no edges directly from the users to the news articles.

Table 2  
Data for the NNR and INNR models in the cold-start scenario.

<table><tr><td>Model</td><td>Train</td><td>Test</td></tr><tr><td>NNR</td><td> $Data_U^t$ , N, U</td><td> $Data_N^b$ </td></tr><tr><td>INNRn</td><td> $Data_U^t$ , N1, U</td><td> $Data_N^b$ </td></tr><tr><td>INNRu</td><td> $Data_{U1}^t$ , N, U1</td><td> $Data_N^b$ </td></tr><tr><td>INNRn&amp;u</td><td> $Data_{U1}^t$ , N1, U1</td><td> $Data_N^b$ </td></tr></table>

INNR is used in three cold-start situations: new users, new articles and the case simultaneously involving new users and articles; accordingly, the INNR models in these scenarios are denoted by $\mathrm { I N N R } _ { n } , \mathrm { I N N R } _ { u }$ and $\mathrm { I N N R } _ { n \& u }$

For $\mathrm { I N N R } _ { n } ,$ only the news in $N _ { 1 }$ can be used to build the news-related subgraph since the news in $N _ { 2 }$ are treated as new articles. Additionally, the securities subgraph and the user-related subgraph are the same as in case of NNR. The model is evaluated on the browsing records of all news articles, Data<sup>b</sup> . The embeddings of articles in $N _ { 1 }$ can be generated by applying node2vec to the entire graph, while the embeddings of new articles will be calculated according to the strategies discussed above based on other related nodes' embeddings. The $\mathrm { I N N R } _ { u }$ model only considers the users in $U _ { 1 }$ when constructing the user-related subgraph, and the other graphs are the same as in case of NNR. The $\mathrm { I N N R } _ { n \& u }$ model considers users in $U _ { 1 }$ and news in $N _ { 1 }$ at the same time because new users and articles will appear simultaneously, which is much closer to the real-world recommendation scenarios.

All models are evaluated on $D a t a _ { N } ^ { b } ,$ , and the industry categories of news are regarded as ground truth when the performance of models is evaluated by using the RPI rate, precision, and recall.

Table 3 and Table 4 show the performance and the computation time, respectively, of the models. The NNR and INNR models attain satisfactory performance, even though they only use the stock transaction records to infer the implicit links between users and news. The NNR model attains the highest RPI rate, precision, and recall among the evaluated models, but its computations take a great deal of time. The largest problem is that it needs to be trained again when new articles or users need to be analyzed.

Focusing on online updates and the cold-start problem, INNR can use the embeddings of related nodes to represent new articles or users to avoid extra computation time of training the model again. Training the core graph embeddings in advance takes approximately $3 6 0 0 s ,$ but it is normally done only once; thus, the model concurrently maintains high eficiency and efectiveness. The performance and computation time of the INNR models are quite close, and their RPI rates are only 15% worse than that of NNR, which shows that INNR ofers stable performance in the cold-start scenarios.

The RPI of INNR is lower than that of NNR because directly using the embeddings of the relevant nodes to represent the new user or article will lose some low-level feature information, such as the hop count between nodes and the sparseness of nodes. However, RPI of INNR still reaches 35%, which is much higher than the values of other collaborative filtering baseline models. Compared with NNR, INNR requires a much shorter training time, as has been fully demonstrated in the experimental analysis. Compared to the loss of approximately 7% of RPI, a nearly twofold reduction of the training time is more important in performing time-sensitive financial news recommendation tasks.

Table 3  
Performance of the node2vec-based models trained on stock transaction data.

<table><tr><td>Model</td><td>RPI rate</td><td>Precision@3</td><td>Recall@3</td></tr><tr><td>NNR</td><td>0.397297</td><td>0.1920</td><td>0.1560</td></tr><tr><td>INNRn</td><td>0.339100</td><td>0.1660</td><td>0.1323</td></tr><tr><td>INNRu</td><td>0.331371</td><td>0.1645</td><td>0.1327</td></tr><tr><td>INNRn&amp;u</td><td>0.341200</td><td>0.1757</td><td>0.1361</td></tr></table>

Table 4  
Computation time of the node2vec-based models trained on stock transaction data.

<table><tr><td>Model</td><td>Training time (seconds)</td><td>Testing time (seconds)</td></tr><tr><td>NNR</td><td>9336</td><td>217</td></tr><tr><td>INNRn</td><td>182(3686)</td><td>390</td></tr><tr><td>INNRu</td><td>192(3722)</td><td>395</td></tr><tr><td>INNRn&amp;u</td><td>173(3625)</td><td>393</td></tr></table>

## 4.2.2. Comparison between Node2vec-based models and baseline models

In this section, our methods are compared with other baseline models to prove the efectiveness and eficiency of the node2vec-based models. The following commonly used collaborative filtering models will be compared: nonnegative matrix factorization (NMF) [9], singular value decomposition (SVD) [10], SVD++ [11], centered-KNN, the Kmost popular method that ranks the articles based on their relatedness to the most popular categories, and the random method that randomly recommends articles to users.

We also implement a content-based method called RNN Recsys [12] and an online approach to embeddings based on node2vec [13] as baselines to ensure that our methods will be fully and efectively compared to other diferent types of recommendation approaches.

Triples of the form (user,rating,news) are created for the baselines. Because there is no user feedback on the news and it is only known whether a user has browsed an article, rating r = 1 is used to represent that a user has read the news according to the browsing records. For each user, some articles that have not been browsed by that user are randomly sampled as negative samples with the rating $r = 0 .$

Collaborative filtering methods are implemented using an existing software package, and their inputs are not vector representations but relational triples. The content-based approach is based on the opensource code, and its inputs are news texts as well as users' browsing records. The embedding-based method that receives relational triples as inputs is also implemented based on open-source code. All compared algorithms have been run with their default hyperparameters, as reported in their reference implementations.

The training and testing data are assigned to the models according to Table 5. In the previous section, the models were only trained with transaction data, Data<sup>t</sup> . To be consistent with the data used in the baseline models, both Data<sup>t</sup> and Data <sup>b</sup> are used to train the node2vecbased models.

For NNR, the diference in data between this section and the previous one is that records of browsing news in $N _ { 1 }$ are added into the knowledge graph. The users are linked to the news in $N _ { 1 }$ according to $D a t a _ { N _ { 1 } } ^ { b }$ , and more graph information is used when inferring the implicit links between users and news in $N _ { 2 } .$ The settings of the INNR models in

## Table 5

Data for the NNR model, the INNR models and baseline models.

<table><tr><td>Model</td><td>Train</td><td>Test</td></tr><tr><td>NNR</td><td> $Data_{U}^{t},Data_{N_1}^{b},N,U$ </td><td> $Data_{N_2}^{b}$ </td></tr><tr><td>INNR $_n$ </td><td> $Data_{U}^{t},Data_{N_1}^{b},N_1,U$ </td><td> $Data_{N_2}^{b}$ </td></tr><tr><td>INNR $_u$ </td><td> $Data_{U_1}^{t},Data_{N_1}^{b},N,U_1$ </td><td> $Data_{N_2}^{b}$ </td></tr><tr><td>INNR $_{n\&u}$ </td><td> $Data_{U_1}^{t},Data_{N_1}^{b},N_1,U_1$ </td><td> $Data_{N_2}^{b}$ </td></tr><tr><td>Baselines</td><td> $Data_{N_1}^{b},N,U$ </td><td> $Data_{N_2}^{b}$ </td></tr></table>

Table 6  
Performance of our models and the baseline models.

<table><tr><td>Model</td><td>RPI rate</td><td>Precision@3</td><td>Recall@3</td></tr><tr><td colspan="4">Our methods</td></tr><tr><td>NNR</td><td>0.428082</td><td>0.2133</td><td>0.1881</td></tr><tr><td>INNRn</td><td>0.351219</td><td>0.1871</td><td>0.1714</td></tr><tr><td>INNRu</td><td>0.353300</td><td>0.1816</td><td>0.1761</td></tr><tr><td>INNRn&amp;u</td><td>0.362843</td><td>0.1898</td><td>0.1698</td></tr><tr><td colspan="4">Collaborative filtering methods</td></tr><tr><td>Centered-KNN</td><td>0.207895</td><td>0.0825</td><td>0.0261</td></tr><tr><td>SVD</td><td>0.176316</td><td>0.0737</td><td>0.0151</td></tr><tr><td>SVD++</td><td>0.202632</td><td>0.0855</td><td>0.0231</td></tr><tr><td>NMF</td><td>0.213158</td><td>0.0886</td><td>0.0269</td></tr><tr><td>MostPop</td><td>0.219178</td><td>0.1210</td><td>0.0560</td></tr><tr><td colspan="4">Content-based method</td></tr><tr><td>RNN Recsys</td><td>0.402395</td><td>0.1995</td><td>0.2031</td></tr><tr><td colspan="4">Embeddings-based method</td></tr><tr><td>Online node2vec</td><td>0.390228</td><td>0.1925</td><td>0.1877</td></tr><tr><td colspan="4">Other method</td></tr><tr><td>Random</td><td>0.218421</td><td>0.0890</td><td>0.0220</td></tr></table>

the three scenarios are similar to those in the previous section, with additional browsing records being the only diference.

The performance of the models is depicted in Table 6, and their computation times are shown in Table 7. It is observed that the NNR model has the best performance among all models. Compared with the result in Table 3, the performance of the NNR model is improved by the addition of browsing records, and the INNR models also achieve better performance. However, computation time remains the biggest weak ness of NNR. The training time of the NNR model is 2051 times as long as that of SVD and 34 times as long as that of KNN, which is not fast enough in real-world recommendation scenarios.

The RPI rate of INNR is still satisfactory compared with values for other models. NNR performs better than INNR; however, with more nodes and edges, NNR takes approximately 3 times as long to complete training as does INNR. Eficiency remains the major advantage of INNR. Compared with the KNN model, INNR only takes approximately 200 s to obtain the representations for users and news from the existing embeddings, which is only approximately 35 times as long as the time needed by SVD and half of the training time of KNN. Moreover, INNR can still maintain its performance at close to the best level when dealing with new users or articles, which indicates that INNR has excellent stability in the cold-start scenarios.

Among the baselines, the MostPop method outperforms SVD, SVD+

## Table 7

Computation time of our models and the baseline models.

<table><tr><td>Model</td><td>Training time (seconds)</td><td>Testing time (seconds)</td></tr><tr><td colspan="3">Our methods</td></tr><tr><td>NNR</td><td>11,728</td><td>217</td></tr><tr><td>INNRn</td><td>212(3842)</td><td>379</td></tr><tr><td>INNRu</td><td>200(3976)</td><td>362</td></tr><tr><td>INNRn&amp;u</td><td>205(3929)</td><td>402</td></tr><tr><td colspan="3">Collaborative filtering methods</td></tr><tr><td>Centered-KNN</td><td>342</td><td>455</td></tr><tr><td>SVD</td><td>5.718</td><td>377</td></tr><tr><td>SVD++</td><td>14.045</td><td>406</td></tr><tr><td>NMF</td><td>9.844</td><td>384</td></tr><tr><td>MostPop</td><td>41</td><td>124</td></tr><tr><td colspan="3">Content-based method</td></tr><tr><td>RNN Recsys</td><td>10,215</td><td>322</td></tr><tr><td colspan="3">Embeddings-based method</td></tr><tr><td>Online node2vec</td><td>6012</td><td>358</td></tr><tr><td colspan="3">Other method</td></tr><tr><td>Random</td><td>0.497</td><td>410</td></tr></table>

+, KNN, and NMF, even though it is a trivial method. When there is a breaking news, users tend to focus on those articles, and MostPop will perform better in this scenario. The random baseline outperforms some collaborative methods on this task. The probable reason is that collaborative algorithms cannot accurately identify a similar users' group for a specific user due to the lack of feedback from a suficient number of users. Except for KNN-based methods, other collaborative algorithms can be trained in a few seconds, which shows their advantage in eficiency.

RNN Recsys performs comparably with NNR and has a very similar training time; however, it sufers from the same problem as does NNR that the model has to be retrained before recommending a new batch of articles. The online node2vec method yields an improvement of 7.5 percentage points in the RPI rate over the INNR method. However, its training time is 29 times as long as that of the INNR. In a real-world recommendation scenario, the time requirement is especially urgent, and reaching the minute level is required, so the online node2vec method still cannot meet the requirements. Using INNR, we update the user's embedding directly based on the relationship between the user and other nodes to greatly improve eficiency. When the market is closed, we can use the latest data to fully update the embedding to compensate for the quality loss of INNR.

## 5. Related studies

This section will briefly review the related studies on news recommendation.

## 5.1. Collaborative filtering methods

Collaborative filtering methods often sufer from the cold-start problem since news items are replaced frequently [14]. Agarwal et al. proposed a model providing a seamless mechanism to transition from cold-start to warm-start scenarios [15]. Trevisiol et al. also tried to provide recommendations in a cold-start scenario and presented a technique to predict the page a user would visit next given his or her viewing a page on the site for the first time [16]. Although researchers have made many improvements in CF-based methods, such methods still need many handcrafted features.

## 5.2. Content-based methods

Content-based approaches are the most popular methods in news recommendation. Wu et al. studied development of a personalized news filtering and summarization system, focusing on keywords of articles [17]. In 2015, Capelle et al. extended SF-IDF by also considering the synset semantic relationships and by using named entity similarities according to Bing page counts [18]. Although many studies have improved content-based methods, it is still dificult for a simple contentbased approach to describe users' preferences for news dynamically and accurately.

## 5.3. Hybrid methods

Hybrid methods combine content-based filtering and collaborative filtering. For example, Phelan et al. proposed a Bayesian method for predicting users' current news interests based on their click behaviors [19]. Son et al. proposed an explicit localized sentiment analysis method for location-based news recommendation [20]. Researchers have also started to apply neural network models to the news recommendation task. Okura et al. began with distributed representations of articles based on a variant of a denoising autoencoder and then generated user representations by using RNN with browsing histories as input sequences [12].

## 5.4. Embeddings-based methods

Knowledge graph techniques, which are based on using explicit domain knowledge to map user preferences to article features, have recently received considerable attention in recommendation task stu dies.

Graph embeddings algorithms, as methods of representing networks, have been applied to many practical scenarios. In past decades, numerous studies explored graph embeddings. Bordes et al. designed a method to learn representations of entities and relations satisfying h + l $\approx t ,$ where $( h , l , t ) \in R$ is a triple [21]. Wang et al. proposed an extension of Bordes's work, enabling entities to have diferent representations in the context of diferent relations by projecting entities on a hyperplane identified by the normal vector [22]. Lin et al. described a model that enabled entities and relations to be embedded in a vector space with diferent dimensions through a projection matrix associated with any relation [23]. Perozzi et al. proposed Deep Walk, a method simulating random walks on a graph and generating sequences that were successively processed by a neural language model [24]. Grover et al. introduced node2vec, a more flexible and complex improvement of Deep Walk [6].

Subsequently, researchers have started to consider the applications of graph embeddings-based methods. Wang et al. presented such methods, addressing the challenges in recommender systems of Taobao [25]. The authors learned the embeddings of all items in the graph constructed from users' behavior history and used them to compute pairwise similarities between all items. Grbovic et al. [26] described listing and user embedding techniques. The researchers models were specifically tailored for the Airbnb marketplace and were able to capture a guest's short-term and long-term interests. Both of the above studies focused on providing real-time recommendations based on large-scale datasets and using graph embeddings. In 2018, Wang et al. proposed a deep knowledge-aware network for news recommendation [2] that showed the efectiveness of graph embeddingsbased methods.

## 6. Conclusions

In this paper, we apply the knowledge graph techniques to the financial news recommendation task and propose a model for incremental updating of embeddings that focuses on computation time and performance. Based on the knowledge graph created to represent users, news, companies and other entities, nodes' relatedness scores are obtained with node2vec following a feature learning approach based on neural language models. Using graph embeddings, users and news can be mapped to the same vector space. Then, the articles can be recommended to users according to cosine similarity. The results of an evaluation using a real-world dataset of a securities company show that the proposed approaches outperform the collaborative filtering models based on matrix factorization, nearest neighbors and the most popular items strategy, as well as a content-based method and an embeddingsbased method. The combination of a node2vec-based recommendation method and an incremental method can attain a good balance between time eficiency and recommendation accuracy in the financial news recommendation task.

## Acknowledgments

This research is partially supported by the National Natural Science

Foundation of China (no. U1811462 and U1711263).

## References

[1] M. Karimi, D. Jannach, M. Jugovac, News recommender systems Survey and roads ahead, Inf. Process. Manag. 54 (6) (2018) 1203–1227.

[2] H. Wang, F. Zhang, X. Xie, M. Guo, DKN: deep knowledge-aware network for news recommendation, Proceedings of the 2018 World Wide Web Conference, International World Wide Web Conferences Steering Committee, 2018, pp. 1835–1844.

[3] M. Wang, M. Liu, J. Liu, S. Wang, G. Long, B. Qian, Safe Medicine Recommendation via Medical Knowledge Graph Embedding, arXiv preprint arXiv:1710.05980.

[4] M. Zihayat, A. Ayanso, X. Zhao, H. Davoudi, A. An, A utility-based news re commendation system, Decis. Support. Syst. 117 (2019) 14–27.

[5] T. Geva, J. Zahavi, Empirical evaluation of an automated intraday stock recommendation system incorporating both market data and textual news, Decis Support. Syst. 57 (2014) 212–223.

[6] A. Grover, J. Leskovec, node2vec: Scalable feature learning for networks, Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2016, pp. 855–864.

[7] Z. Huang, W. Xu, K. Yu, Bidirectional LSTM-CRF models for sequence tagging, arXiv preprint arXiv:1508.01991.

[8] T. Mikolov, I. Sutskever, K. Chen, G.S. Corrado, J. Dean, Distributed representations of words and phrases and their compositionality. Advances in Neural Informatior Processing Systems, 2013, pp. 3111–3119.

[9] X. Luo, M. Zhou, Y. Xia, Q. Zhu, An eficient non-negative matrix-factorization based approach to collaborative filtering for recommender systems, IEEE Trans. Ind Inf. 10 (2) (2014) 1273–1284

[10] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommende systems, Computer (8) (2009) 30–37.

[11] Y. Koren, Factorization meets the neighborhood: a multifaceted collaborative fil. tering model, Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2008, pp. 426–434.

[12] S. Okura, Y. Tagami, S. Ono, A. Tajima, Embedding-based news recommendation for millions of users. Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2017, pp. 1933–1942.

[13] F. Beres, R. Palovics, D.M. Kelen, D. Szabo, A.A. Benczur, Node embeddings in dynamic graphs, Book of Abstracts of the 7th International Conference on Complex Networks and Their Applications, 2018, pp. 178–180.

[14] C. Wang, D.M. Blei, Collaborative topic modeling for recommending scientific articles, Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2011, pp. 448–456.

[15] D. Agarwal, B.-C. Chen, B. Pang, Personalized recommendation of user comments via factor models. Proceedings of the Conference on Empirical Methods in Natural Language Processing, Association for Computational Linguistics, 2011, pp. 571–582.

[16] M. Trevisiol. L.M. Aiello. R. Schifanella. A. Jaimes, Cold-start news recommendation with domain-dependent browse graph, Proceedings of the 8th ACM Conference on Recommender Systems, ACM, New York, NY, USA, 2014, pp. 81–88.

[17] X. Wu, F. Xie, G. Wu, W. Ding, Personalized news filtering and summarization on the web. 2011 23rd JEEE International Conference on Tools with Artificial Intelligence, IEEE, 2011, pp. 414–421.

[18] M. Capelle, M. Moerland, F. Hogenboom, F. Frasincar, D. Vandic, Bing-SF-IDF+: a hybrid semantics-driven news recommender, Proceedings of the 30th Annual ACM Symposium on Applied Computing. ACM. 2015, pp. 732–739.

[19] O. Phelan. K. McCarthy. B. Smyth, Using twitter to recommend real-time topical news, Proceedings of the Third ACM Conference on Recommender Systems, ACM, 2009. pp. 385–388.

[2o] J.-W. Son. A. Kim. S.-B. Park. A location-based news article recommendation with explicit localized semantic analysis. Proceedings of the 36th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM 2013, pp. 293–302.

[21] A. Bordes, N. Usunier, A. Garcia-Duran, J. Weston, O. Yakhnenko, Translating embeddings for modeling multi-relational data. Advances in Neural Informatior Processing Systems, 2013, pp. 2787–2795.

[22] Z. Wang, J. Zhang, J. Feng, Z. Chen, Knowledge Graph Embedding by Translating on Hyperplanes. AAAI, 14 2014, pp. 1112–1119.

[23] Y. Lin, Z. Liu, M. Sun, Y. Liu, X. Zhu, Learning entity and relation embeddings for knowledge graph completion. AAAL. 15 2015, pp. 2181–2187

[24] B. Perozzi, R. Al-Rfou, S. Skiena, Deepwalk: online learning of social representations, Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2014, pp. 701–710.

[25] J. Wang, P. Huang, H. Zhao, Z. Zhang, B. Zhao, D.L. Lee, Billion-scale commodity embedding for e-commerce recommendation in alibaba. Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining,

ACM, 2018, pp. 839–848.

[26] M. Grbovic, H. Cheng, Real-time personalization using embeddings for search ranking at Airbnb, Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, ACM, 2018, pp. 311–320.

Jiangtao Ren is currently an Associate Professor at the School of Data and Compute Science, Sun Yat-sen University, Guangzhou, China. He received the Ph.D. degree from the Department of Automation, Tsinghua University, Beijing, China, in 2003. He has published more than 20 papers in international conferences and journals including the ICML, KDD,ICDM, ECML/PKDD, WWW, SDM, ICME, Information Science, Knowledge Based Systems and Neurocomputing, etc. His current research interests include pattern recognition, machine learning, data mining and NLP

Jiawei Long received the B.S. degree from Sun Yat-sen University, Guangzhou, China. And he is currently pursuing the M.S. degree at the School of Data and Computer Science, Sun Yat-sen University, Guangzhou, China. His current research interests include machine learning and data mining.

Zhikang Xu received the B.S. degree from East China Jiaotong University, Jiangxi, China And he is currently pursuing the M.S. degree at School of Data and Computer Science, Sun Yat-sen University, Guangzhou, China. His current research interests include knowledge graph application and graph embedding
