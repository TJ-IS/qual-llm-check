---
otero_id: 11028
otero_key: "MA2QCY2P"
title: "User opinion classification in social media: A global consistency maximization approach"
authors: "Jiexun Li; Xin Li; Bin Zhu"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2016.06.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: User Opinion Classification in Social Media: A Global Consistency Maximization Approach

Author: <ce:author id="aut0005" biographyid="vt0005" orcid="0000-0002-1526-280X"> Jiexun Li Xin Li Bin Zhu

![](/api/attachments/MA2QCY2P/fulltext/images/d8b75c198c340cfbf755e46f91904ce24dbf0da56494e84307a3abe969651c99.jpg)

PII: S0378-7206(16)30060-X

DOI: http://dx.doi.org/doi:10.1016/j.im.2016.06.004

Reference: INFMAN 2917

To appear in: INFMAN

Received date: 17-7-2015

Revised date: 10-5-2016

Accepted date: 5-6-2016

Please cite this article as: Jiexun Li, Xin Li, Bin Zhu, User Opinion Classification in Social Media: A Global Consistency Maximization Approach, Information and Management http://dx.doi.org/10.1016/j.im.2016.06.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# User Opinion Classification in Social Media: A Global Consistency Maximization Approach

Jiexun Li<sup>a\*</sup>jiexun@gmail.com, Xin Li<sup>b</sup>xin.li.phd@gmail.com, Bin Zhu bin.zhu@oregonstate.edu

<sup>a</sup>College of Business & Economics, Department of Decision Sciences, Western

Washington University, Bellingham, WA 98225, USA

<sup>b</sup>Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon, Hong Kong SAR

<sup>c</sup>College of Business, Oregon State University, Corvallis, OR 97331, USA

\* Corresponding author. College of Business & Economics, Department of Decision Sciences, Western Washington University, Bellingham, WA 98225, USA. Tel.: +1 520 907 4205; fax: +1 541 737 4890

#

## Highlights

• A link-based approach, named global consistency maximization (GCM) is proposed for opinion classification.

• The proposed approach achieves higher accuracy than two baseline approaches.

• Link-based opinion classifiers are robust to a small training sample if selected properly.

#

## Abstract

Social media is a major platform for opinion sharing. In order to better understand and exploit opinions on social media, we aim to classify users with opposite opinions on a topic for decision support. Rather than mining text content, we introduce a link-based classification model, named global consistency maximization (GCM) that partitions a social network into two classes of users with opposite opinions. Experiments on a Twitter data set show that: (1) our global approach achieves higher accuracy than two baseline approaches and (2) link-based classifiers are more robust to small training samples if selected properly.

Keywords: big data; social media; opinion mining; collective classification

## 1. Introduction

In electronic commerce, a major challenge faced by companies is to understand their customers’ opinions to design and conduct marketing campaigns. The emergence of bigdata platforms and technologies makes it possible for e-commerce companies to access and analyze data about a large population of (potential) customers. In particular, social media is a major source and battlefield of e-commerce big-data analytics, due to its growing popularity for information distribution and opinion sharing. Mining data in social media to gain marketing intelligence have been identified as one of the major applications of big-data analytics.<sup>1</sup> The analysis of social media data not only enables businesses to have more effective “conversations” with their customers,<sup>2</sup> but also facilitates the understanding of people’s opinions about their products/services.<sup>3</sup> Zhao et al.<sup>8</sup> identified social media analytics as a critical complement to traditional survey analytics to increase the validity of market studies. Online opinions have been used in a variety of analytic solutions, such as sales prediction,<sup>4,5</sup> search engine design,<sup>6</sup> and financial market forecasting. 7

Mining social media data requires big-data solutions. For instance, microblogging sites like Twitter are growing at a high rate with hundreds of millions of active users and

#

postings generated per day. In order to mine data of such large volume and high velocity, businesses must be equipped with advanced analytical technology to obtain an accurate overview of social opinion landscape for better decision support. Furthermore, social media contains a mixture of various types of data, such as textual content, multimedia content, and social interactions. Analytical solutions for social media must be capable of modeling such data variety. Hence, among the main research directions in business intelligence and analytics, mining opinions from noisy unstructured text in streams and mining link structures in social networks pose significant challenges and opportunities for the big-data analytics research community.

In order to successfully make use of opinions in social media for decision making, it is important to classify individuals’ viewpoints into two sides of a debate. Many business questions can be formulated as a binary decision, such as “Should our product have a larger screen size?” or “Do we need a luxury version of our current product/service?” It is crucial for companies to accurately estimate the “for” and “against” populations in social media platforms and identify target groups for marketing campaigns. Because it is difficult to fully understand the demographics or opinions of all users before starting a campaign, it is a common practice to begin with a select group of seed users.

Most traditional methods of opinion mining try to classify users’ opinions analyzing text content of the postings.<sup>10</sup> In social media such as Twitter, the performance of such approaches is often unsatisfactory due to the short length of online postings and informal writing styles. Furthermore, with a limited number of seed users as training data, contentbased opinion classifiers often fail to achieve high classification accuracy.

Enlightened by the variety nature of big data, our study takes a different perspective to address the opinion classification problem. As we know, the network structure of users interacting with each other in social media contains rich information suggesting opinion groups. How opinions are formed, divided, and spread is often guided by the principles of homophily and social influence. In microblogging, as participants receive messages only from those who they choose to follow, it is highly unlikely that they will follow a person whom they do not like or care about. Hence, the following relationships among users may suggest a layer of homophily that can be exploited to identify opinion camps. Another

valuable information source for opinion mining is the retweeting relationships among users. According to studies investigating the motivation behind online activities, microblog participants usually retweet a message because they think it could help others make decisions.<sup>11</sup> They may also retweet messages to stay connected with others who receive the message or show support to the sender of the message.<sup>12</sup> As a result, in the context of microblogging, people are less likely to retweet a message if they disagree with the content of the message or dislike the sender of the message.

On the basis of social influence theories, link structures among users could also suggest users’ opinion. Most existing studies take a local view and classify each user’s opinions separately. In such approaches, early errors may propagate to later classifications and thus lead to lower accuracy. We propose a novel method that takes advantage of the global structure of social interactions to alleviate the opinion classification problem in a collective manner. In particular, we model the individuals involved in a topic discussion as a graph according to their communication linkages. Our conjecture is that this graph reflects stabilized social relations where people with common opinions tend to interact more and people with opposite opinions tend to communicate less. On the basis of this conjecture, we propose a global consistency optimization algorithm to collectively classify the opinions of users involved in debates in social media. Our research shows that our proposed opinion classifier is not only accurate but also robust to the size of seed users as long as the seeds are chosen appropriately.

We consider our study a novel and significant contribution to the design of analytical solutions in electronic commerce. Our work focuses on analyzing the large volume of everchanging opinion data generated by users in social media. In particular, our proposed approach takes advantage of the variety of social media data by leveraging the link relationships among users to achieve highly accurate classification of opinions. Furthermore, the global maximization algorithm shows significant robustness to the size of training set. This strength of our approach can help mitigate a common problem in bigdata analytics, that is, the limited amount of labeled data. Our research has significant implications for both researchers and practitioners of big-data analytics in electronic commerce.

## 2. Literature Review

Opinion mining is an important problem in text mining,<sup>10</sup> which has been examining the subjectivity and polarity of text. In the context of this research, we are more interested in the classification of opinion polarity, that is, positive or negative. In existing literature, related work on opinion classification can be divided into content-based and link-based approaches.

## Content-based Approaches

Opinion classification is often based on textual contents, which can take two approaches: lexicon-based and learning-based methods. Lexicon-based approaches use lexicons and predefined rules to annotate sentiments of text.<sup>13</sup> For example, Demers and Vega<sup>14</sup> used a lexicon approach to measure the tone of news. Learning-based methods use machinelearning techniques upon linguistic features, including the lexicon features if available, to build opinion classification models. For example, Yang et al.<sup>15</sup> applied association rules and a Naïve Bayes (NB) classifier to classify the sentiments of online consumer reviews on e-commerce websites.

With the rise of social media, opinion mining is widely applied to social media applications such as Twitter and Facebook. Most existing studies used the textual contents to resolve this problem. Mostafa<sup>16</sup> used a lexicon-based approach to classify brand sentiments. Li and Xu<sup>17</sup> constructed a rule-based system to detect the events in microblog posts that cause emotional effects. In the machine-learning approach camp, Sayeedunnissa et al.<sup>18</sup> took a classic NB approach with the bag-of-words model and information gain-based feature selection to classify Twitter sentiments. Akaichi et al.<sup>19</sup> and Hamouda and Akaichi<sup>20</sup> used support vector machine (SVM) and NB approach to classify Facebook status sentiments. Myslin et al.<sup>21</sup> compared multiple classic machinelearning approaches to classify Twitter sentiments on tobacco products. It is worth noting that Hassan et al.<sup>22</sup> proposed a bootstrapping ensemble approach to address the Twitter sentiment classification problem. The approach provided more accurate and balanced predictions and built sentiment time series that better reflect events eliciting strong sentiments from users. There were also studies combining machine-learning with lexicon-based approaches to classify sentiments.<sup>23,24</sup> In the machine-learning approach, clustering methods were also used to analyze social media opinions. For example, Paltoglou and Thelwall<sup>25</sup> proposed an unsupervised lexicon-based approach that estimates the level of emotional intensity contained in text. Feng et al.<sup>26</sup> used PLSA to cluster blogs with sentiments as a latent variable, which was able to find sentiment coherent groups.

## Link-based Approaches

Social media provides a new platform for users to communicate and interact with each other. When a user posts a message online to express his/her opinion, it can incur a series of responses such as compliments, praises, disagreements, and even attacks from other users. Each of these responses can lead to even more responses in a spreading manner. Such response relationships form a social network of opinionated users. The linkage (i.e., relationship) information has become new evidence that can help distinguish users’ opinions. Because users are connected to each other in a social network and their class labels are intercorrelated, opinion mining has become a collective classification problem. 2

Many studies have tried to use the linkage information embedded in social networks for classifying users’ opinions in social media. However, they view the semantics of linkages in social networks differently. In an early effort of link-based opinion classification, Agrawal et al.<sup>28</sup> analyzed a social network formed by “respond-to” relationships in newsgroups. By assuming that a “respond-to” relationship represents disagreement, they use a “max-cut” graph-partitioning algorithm to break highly weighted disagreeing edges and separate users into two groups. Their assumption of “respond-to” indicating disagreement may not hold in other popular social media platforms. On Twitter, following or retweeting someone is more likely to mean that the users agree with each other or share a similar opinion. Therefore, more studies on link-based opinion mining are based on the “homophily” assumption,<sup>29</sup> that is, the phenomenon of “birds of a feather flock together.”<sup>30</sup> Users who are “connected” by a mutual relationship are more likely to share common opinions. In the context of opinion classification on a social media platform like Twitter, researchers have investigated users’ mutual relationships in a variety of forms, including “follow,”<sup>31–34</sup> “mention,”<sup>32,35</sup> or “retweet.”<sup>35–37</sup> In particular, using “@” mentions, as a way of creating connections on Twitter, may also indicate a desire to pay attention (e.g., to information of interest). Among the homophily connections, several studies suggested that the “follow” links had little positive impact on classification accuracy.<sup>31</sup> Conover et al.<sup>35</sup> found that combining attention links with follow links is superior to using follow links alone. Wong et al.<sup>36</sup> also argue that following (a tweeter) is not a robust indicator of approval or agreement on political opinions. A user may follow two sources on Twitter with opposite political stances to obtain a more unbiased comprehensive view. A follow link may exist as a stale edge in the Twitter following network, simply because a user forgets to unfollow a prominent tweeter whom he/she is no long interested in. By contrast, retweeting is often an explicit act of approval and therefore a stronger evidence for agreement in opinions.

On the basis of the homophily assumption, a variety of analytical techniques have been developed for opinion classification. One of the most popular techniques used in several studies is label propagation (LP), which analyzes the labels in a nodes’ neighborhood and tries to assign a label to each node in an iterative manner. Ren et al.<sup>38</sup> used this method for determining class labels of customer reviews based on a graph consisting of links representing similarity between nodes. In order to predict the political alignment of Twitter users, Conover et al.<sup>35</sup> studied two types of communication networks, based on “mention” edges and “retweet” edges, and proposed a solution of community detection using an LP algorithm.<sup>39</sup> Speriosu et al.<sup>31</sup> developed an opinion polarization approach by combining both lexical links (e.g., text, hash tags, and emotions) and following links in a graph. A semi-supervised LP algorithm was used for classification with different seeding methods. In addition, for tweet-level opinion classification, Rajadesingan and Liu<sup>37</sup> made an assumption that two tweets being retweeted by the same users within a short time period are likely similar in terms of opinion. They introduced a graph-based algorithm, namely ReLP (retweet label propagation) that starts with a set of seeds and iteratively propagates labels to similar tweets. Tan et al.<sup>32</sup> proposed an opinion polarization approach by incorporating social network information such as “follow” and “mention” linkages. Their graph-based classification models consist of loopy belief propagation to infer user-level sentiment labels. Rabelo et al.<sup>33,34</sup> applied a relational classifier combined with a relaxation labeling algorithm on a Twitter follower network to collectively predict political polarity of users. All the aforementioned studies showed that classification models based on links in a graph outperformed traditional content-based opinion classifiers.

Most of these existing collective opinion classifiers, such as $\mathrm { L P } ^ { 3 5 }$ or relaxation labeling,<sup>33,34</sup> take a local view and label each node based on the labels of its direct neighbors. Such a labeling process iterates in the graph until the solution converges, which may be highly computationally expensive. More importantly, propagating labels based on dependencies in local neighborhoods may not necessarily lead to a global optimal solution.

In optimization theory and graph theory, minimum cut (min-cut) is a combinatorial optimization problem that partitions the vertices of a graph into two disjointed subsets such that the total capacity of the removed edges is minimum.<sup>40</sup> The min-cut method and its dual, max-flow, have been widely used in a number of real-world applications such as project scheduling,<sup>41</sup> gene function prediction,<sup>42</sup> and image segmentation.<sup>43</sup> Unlike LP, the min-cut method takes a global view and finds an optimal partition of the entire graph to reach maximum consistency in the two subgraphs. To the best of our knowledge, no prior study has used the min-cut approach to classify users’ opinions on Twitter.

## Research Questions

Among the state-of-the-art techniques for opinion classification, content-based approaches (e.g., NB classifiers)<sup>18–20</sup> ignore the rich information of social linkages among users, while link-based approaches (e.g., LP)<sup>31,35,39</sup> exploit linkage information but take a local view. Our study, based on the homophily assumption and taking a global view, is aimed at modeling users’ opinions collectively in the entire structure of the network. In this study, we investigate whether such a global optimization approach can outperform the state-of-the-art opinion classifiers in terms of accuracy.

Furthermore, traditional content-based opinion classification methods generally require a training data set with a reasonably large number of labeled instances. Data annotation is known to be a tedious task that requires a large amount of time, effort, and domain expertise. Given the enormous volume of data on social media platforms, how many data instances (e.g., tweets) do we need to review and label for training to guarantee the

potential capability of the classifier? We are interested in determining the robustness of opinion classifiers to the training set size and the method of choosing the most important data instances for training opinion classifiers. In particular, this study is aimed at addressing the following research questions:

Q1. Can a collective classifier based on global optimization outperform existing models for opinion classification?

Q2. How robust are opinion classifiers to different sizes of training data sets?

Q3. What is the best strategy to choose seed users as training data for opinion classification?

## 3. Model

Debates in social media are often a dynamic process involving heated discussion between two sides. The involved users, however, may only interact with a portion of users to express their opinion. In circumstances where one feels that his/her opinion is fully expressed, he/she may not generate much content. In such circumstances, predicting each user’s opinion by analyzing his/her postings and relationships separately, as in most existing work, may not be the best solution. Rather, we introduce a novel approach that takes into account the interdependencies between users and classifies user opinions in a collective manner. Our approach builds an undirected graph to represent users involved in an online debate. On the basis of the homophily assumption, we model opinion classification as a global consistency maximization (GCM) problem.<sup>42</sup> Our collective opinion classifier can find an optimal solution by partitioning the graph into two components, each representing one side of the debate.

## Problem Formulation

We represent a social network as an undirected graph: $G ( V , E )$ . In such a graph, $V : \{ \nu _ { I } , \nu _ { 2 } .$ $\ldots , \nu _ { n } \}$ is a set of n vertices/nodes, in which each node represents an online user. $E \mathrm { : } \left\{ e _ { i j } \right\}$ is a set of edges/links, in which each link $e _ { i j }$ represents a certain relationship(s) between two users i and j. The users discuss certain topics. For a specific topic, a user i may hold an opinion state x<sub>i</sub>. We assume only two possible opinion states in this study and set $x _ { i } =$

1 if user i is a supporter $( ^ { 6 6 } \mathrm { f o r } ^ { , 9 } )$ and $x _ { i } = - 1$ if user i is an opponent (“against”) of a certain topic.

In practice, it is often easier to identify some highly visible opinion leaders. This group consists of the most vocal and opinionated users such as activists, politicians, and celebrities. We can manually assign the opinion labels (either 1 or −1) to such users as “seeds” (or training data), denoted by $V _ { \nu } .$ . For the remaining (majority) users in the network, the opinions are unknown $( x _ { i } = 0 )$ . Our goal is to assign a state value $x _ { i }$ to each user i with $x _ { i } = 0$ by analyzing the linkage between users in the social network.

## Global Consistency Maximization

On Twitter, two nodes i and j can have different relationships/interactions, for example:

• Following: user i follows user j, which indicates that i is interested in $j .$

• Retweeting: user i retweets messages by user $j ,$ which often indicates that i is distributing $j ^ { \prime } s$ opinion, possibly adding his/her own opinion on the topic.

• Commenting/replying: user i comments on messages posted by user $j ,$ which indicates that i is expressing an opinion to either agree or disagree with $j .$

• Liking/favoriting: user i likes messages by user $j ,$ which often indicates that i agrees with j.

Each of these relationships between i and j can be regarded as evidence of (dis)agreement between the two users. All the evidence can be aggregated to an agreement score $w _ { i j }$ (associated with each edge $e _ { i j } )$ of their opinions on the topic. It is important to note that $w _ { i j }$ can be either positive (agreement) or negative (disagreement). In this study, we focus only on retweeting relationships. Retweeting is often considered an explicit act of approval and a more robust indicator of agreement than other relationships such as following.<sup>36</sup> Like most related work,<sup>35–37</sup> our approach is based on the homophily assumption, that is, when a user i retweets another user $j ,$ they tend to share the same opinion on this topic. Therefore, the agreement score $w _ { i j }$ between the two users is proportional to the number of retweets between them (either i retweeting j or j retweeting i).

For each pair of users i and j with opinion states x<sub>i</sub> and $x _ { j } ,$ we define $w _ { i j } x _ { i } x _ { j }$ as a consistency score of the edge connecting i and j. As $w _ { i j } > 0$ indicates they are likely to agree each other, we generally want to set $x _ { i }$ and $x _ { j }$ to be the same (either 1 $\mathrm { o r } - 1 )$ . Accordingly, if $w _ { i j } < 0$ , we generally expect the two disagree, and $x _ { i }$ and $x _ { j }$ have opposite values. Thus, at the social network level, we argue that the “optimal” opinion state assignment should provide us the highest overall “consistency” across the network:

$$
\begin{array}{l} \text { Maximize } E = \sum_ {i} \sum_ {j} w _ {i j} x _ {i} x _ {j} \\ \text { s.t. } \quad x _ {i}, x _ {j} = \{1, - 1, 0 \} \end{array}
$$

In order to solve this optimization problem, we construct a new directed graph H from the undirected graph G (which has users with unknown opinion states). Each node of H corresponds to a node of G. H also contains two new nodes: a source node $s ( ^ {  } \mathrm { f o r } ^ { \ ' } )$ and sink node t (“against”). Unlike edges in G, each edge in H is directed. Figure 1 illustrates how to transform an undirected graph G (Fig. 1(a)) into a directed graph H (Fig. 1(b)) by creating six different types of edges based on the following rules:

1) For each node i in G with $x _ { i } = 1$ , we create a direct edge from node s to node i with $w _ { s i } = \infty .$

2) For each node i in G with $x _ { i } = - 1$ , we create a direct edge from node i to node t with $w _ { i t } = \infty$

3) For each edge in $G$ connecting node i and node j such that $x _ { i } = 1$ and $x _ { j } = 0$ , we create a direct edge from node i to node j with edge weight $w _ { i j }$ copied from G.

4) For each edge in G connecting node i and node j such that $\mathbf { \boldsymbol { X } } _ { i } = 0$ and $\mathbf { X } _ { j } = - 1$ , we create a direct edge from node i to node j with edge weight $w _ { i j }$ copied from G.

5) For each edge in G connecting node i and node j such that $x _ { i } = 0$ and $x _ { j } = 0$ , we create a direct edge from node i to node j and a direct edge from j to i, with $w _ { i j } =$ $w _ { j i }$ copied from G.

6) The edges in G that are not incident on a node in state 0 are ignored. With this new directed graph H, classifying opinions of users is converted to a min-cut problem. An s–t cut in graph H is a partition of the nodes of H into two sets S and T,

#

where S contains the source node s and T contains node t. An edge (u, v) crosses the cut if u lies in S and v lies in T. The weight of the cut is the sum of the weights of the edges crossing the cut. Because a high weight represents a high degree of agreement between two users, separating two highly agreeing nodes on two sides is considered a reduction in consistency. Therefore, our objective is to find the s–t cut C with the smallest weight in H. For each node i in S, we set $x _ { i } = 1$ ; for each node i in T, we set $x _ { i } = - 1$ . Because we have set the weights of edges incident on s and t (edges of types 1 and 2) to be infinity, they will not be selected to participate in C. Hence, the only edges in C are those incident on nodes with state equal to 0. Each edge in C of types 3 or 4 corresponds to one inconsistent edge in G, an edge between two users who retweeted one another but have opposite opinions. In each pair of edges of type 5, at most one edge can belong to C; according to the definition of the s–t cut, the edge in the pair directed from a node in T to a node in S does not belong to the cut. Therefore, each edge in C corresponds to exactly one inconsistent edge in G in a one-to-one manner. Hence, the cut C with the smallest weight gives the optimal state assignment that minimizes the total weight of inconsistent edges in G.

In the example in Figure 1, suppose the weights of all edges not incident on s or t are 1 and the min-cut in H is the edge connecting the node in state 0 to the one in state −1. Thus, the algorithm should assign a state of 1 to both nodes in state 0.

## 4. Experimental Evaluation

## Data set

In order to compare and evaluate different opinion classification methods, we use a realworld Twitter data set from ref. [37]. This data set spans a period of 5 days during the heated debate on gun reform from 15 April 2013 to 18 April 2013. This data set was collected using Twitter’s streaming API with keywords such as “gun” and “gun control.” The data set consists of 916,171 postings (505,637 original tweets and 410,534 retweets) by 491,860 users. Among the users, there are visibly opinionated users, who are used as seeds for model training, and moderately opinionated users, who are used for performance evaluation.

Visibly opinionated users: On Twitter, lists are created and maintained by users as a form of groups. For example, lists such as “Protect 2nd Amendment” or “Guns Save Lives” are clearly against gun reform; other lists such as “Prevent Gun Violence” and “Gun Safety” are apparently supporters for gun reform. In this data set, 262 users (84 for and 178 against gun reform) were identified as visibly opinionated users from such related lists. This subset of users (V<sub>v</sub>) is used as a “training set” in our experiments.

Moderately opinionated users: This group contains users who posted between 2 and 4 tweets during the collection cycle, do not belong to any relevant list, and do not label themselves as for/against gun reform in their Twitter profile page. From a randomly selected sample of 500 users in this group, each was manually annotated as for or against based on their tweets. Out of the 500 users, 276 are for gun reform, 120 are against, and the rest shared information tweets (such as gun reform-related news) but did not voice their personal opinions and were hence ignored. This subset of 396 users is considered as the “test set” in our experiments.

Given this data set, we build a graph G that represents the social network of all users. In this graph G, each vertex represents a user and each edge represents a relationship between two users. This study only considers the retweet relationship between users. Thus, an edge $e _ { i j }$ between vertices i and j indicates user i retweeted j and/or j retweeted i. The weight of $e _ { i j } , w _ { i j } ,$ is defined as the number of retweets between i and j. It is worth noting that 215,669 out of the 491,860 users are isolated vertices in the graph, because they did not retweet or were not retweeted by others. Table 1 provides an overall description of this Twitter data set.

## Baseline Methods and Implementation

For comparison, we develop two baseline methods for classifying users of opposing opinions.

• Content-based Classifier

#

A content-based classifier (CC) differentiates two sides of a debate, supporters, and opponents, solely based on the content of their postings. During a Twitter debate, each user $\nu _ { i }$ may express his/her opinion via multiple tweets or retweets $\left\{ t _ { i j } \right\}$ . We use a basic “bag-of-words” method to represent each posting as a feature vector of word occurrences. For each visibly opinionated user, who always takes one side of two opinions, we can label all his/her postings as 1 $( ^ { 6 6 } \mathrm { f o r } ^ { , 9 } )$ if he/she is a supporter $\mathrm { o r } - 1$ (“against”) if an opponent. Such a collection of postings is used as the training set for CC. In previous opinion-mining research, NB classifiers are found among the top-performing $\mathrm { C C } .$ 18–20 Hence, in our experiments, we also choose NB to build an opinion classification model as a baseline. In our experiments, we choose the commonly used algorithm, NB classifier, to build an opinion classification model. Then, for a user $\nu _ { i } ,$ whose opinion is to be determined, we use the trained NB classifier to predict the opinion of each of his/her postings. For each posting $t _ { i j }$ by $\nu _ { i } ,$ the NB classifier gives a probability score ${ p _ { i j } } ^ { + }$ of the posting $t _ { i j }$ being positive and ${ p _ { i j } } ^ { - }$ of it being negative. Then, all predicted probability scores of his/her postings are aggregated by class to determine user $\nu _ { i } \mathrm { ^ { * } s }$ class label $x _ { i }$ as follows:

$$
x _ {i} = \left\{ \begin{array}{l l} 1 & \text { if } \sum_ {j} p _ {i j} ^ {+} > \sum_ {j} p _ {i j} ^ {-} \\ - 1 & \text { if } \sum_ {j} p _ {i j} ^ {+} <   \sum_ {j} p _ {i j} ^ {-} \\ 0 & \text { otherwise } \end{array} \right.
$$

If the sum of positive scores is higher than the sum of negative scores, this user is labeled 1; if the sum of positive scores is less than the sum of negative scores, this user is labeled −1; otherwise, the user’s opinion is undetermined and labeled 0.

## • Label Propagation

Among the link-based opinion classifiers, LP is one of the most popular and effective techniques in several studies.<sup>31,35,39</sup> In our experiments, we implement an LP algorithm for opinion classification as a second baseline. Like GCM, LP is based on the same homophily assumption, that is, a user tends to share the same opinion as his/her neighbors. Figure 2 shows the pseudo-code for the LP algorithm. The algorithm starts with graph G, including a subset of seeds $V _ { \nu } ,$ that is, visibly opinionated users, whose

#

class labels are known. In each iteration, the algorithm traverses all vertices in G in a random sequence. Each vertex i is assigned the majority label of its neighbors. In order to determine the majority label, we take into account the weight $w _ { i j }$ of the edge between vertices i and j, which can be calculated in the same manner as in GCM. In this study, we only consider the number of retweets between two users. The propagation process stops when there is no further change on the vertices’ labels.

Our experiments are conducted on a laptop computer with the following configuration: Intel Core i5-4310U CPU @ 2.00 GHz 2.60 GHz, 8 GB RAM, 64-bit Operating system, Windows 8.1 Enterprise. All three opinion classification models are implemented in Python. For both link-based classifiers, LP and GCM, we use a well-known Python package for network analysis called NetworkX (Version 1.8.1)

(https://networkx.github.io/) to build the undirected graph G and the directed graph H for GCM. A function named minimum\_edge\_cut() in NetworkX is used to compute the mincut for GCM. In our evaluation, CC trains the classifier using the tweets by the 262 visibly opinionated users and predicts the labels of the 396 moderately opinionated users, with no need to classify all other users in the large network of approximately 500,000 users. The computing time (including training and testing) for CC was 105 s. By contrast, both LP and GCM require computing over the entire network(s) of connected nodes, not just those 396 in the test set, and hence consume more time. In particular, in our experiments, the computing time for LP was 5013 s and that for GCM was 6351 s. It is worth noting that, although seemingly more time-consuming, LP and GCM complete classifying all 276,191 connected users in the network, while CC classifies only 396 for evaluation. Nevertheless, the efficiency of the link-based classifiers is not yet satisfactory and we encourage further research for improvement.

## Evaluation Metrics

Our experiments compare the performance of three opinion classifiers: CC, LP, and GCM. This task is a binary classification of users into two categories of opinions: for versus against. We use standard measures, that is, accuracy, precision, recall, and Fmeasure. Accuracy assesses the overall correctness of classification. Precision, recall, and F-measure evaluate the accuracy of each class. These four metrics are defined as follows:

$$
\text { accuracy } = \frac {\# \text {   of   correctly   classified   instances }}{\# \text {   of   all   classified   instances }}
$$

$$
\operatorname{precision} (i) = \frac {\# \text {   of   instances   correctly   classified   in   class   } i}{\# \text {   of   instances   classified   in   class   } i}
$$

$$
\operatorname{recall} (i) = \frac {\# \text {   of   instances   correctly   classified   in   class   } i}{\# \text {   of   instances   in   class   } i}
$$

$$
\mathrm{F-measure} (i) = \frac {2 \cdot \text { precision } (i) \cdot \text { recall } (i)}{\text { precision } (i) + \text { recall } (i)}
$$

It is worth noting that, for the two link-based classifiers LP and GCM, if a user is an isolated vertex in the graph without any retweeting edges with others, the classifiers are unable to determine its label. Hence, such vertices will be labeled as “undetermined.” In our evaluation, such undetermined users are also counted as errors.

## Results

## Classification Performance

In order to answer our research question Q1, Tables 2 and 3 show the results of the three opinion classification models. The two link-based classifiers, LP and GCM, achieve higher classification accuracy than the CC by >20%. In particular, GCM achieves the highest overall accuracy of 93.43%. For both classes, GCM achieves the highest precision, recall, and F-measure: 94.35%, 96.74%, and 95.53% for class “for”; 92.79%, 85.83%, and 89.18% for class “against,” respectively. Of the 396 users in the test set, LP and GCM provide almost identical classification results, except for three users. In particular, of these three users, GCM incorrectly classifies one to the “against” category, while LP incorrectly classifies two, one to “for” and the other to “against.” By checking

#

the linkages of these three users, we find that each of them has two “retweeting” linkages to other users. When the two linked nodes are assigned opposite labels, link-based classifiers have difficulty in determining the correct label for this node, unless additional information (e.g., content and weights on linkages) is available and considered.

Nevertheless, it is worth noting that the link-based classifiers have a limitation to predict the label of a node: this node has to be directly or indirectly connected with some labeled nodes in the graph. In our experiments, because the test set contains two moderately opinionated users who are isolated vertices in the graph, neither LP nor GCM can determine their class label. This limitation, however, is not a problem for CC, because it predicts the class label of a user based on the content of his/her tweets. For the 215,669 isolated users of the 491,860 users in our data set, predicting their class labels would require a CC, like CC that we implemented in this study, which results in a classification accuracy of 75.47%.

## Training Sample Selection

Because both LP and GCM are link-based, they can infer the class label of a user based on what is known of his/her associations. In order to answer our research questions Q2 and Q3, we conducted further experiments and investigated how the link-based methods perform in response to different sizes of training samples.

In our Twitter data set of 491,860 users, 262 are identified as visibly opinionated users (for: 84; against: 178). We then examine the robustness of the three classifiers by reducing the number of visibly opinionated users in the training set. In the context of Twitter, there are different ways of choosing users to create a training set. We consider the following four ranking methods in our experiments:

1. Rank by the number of tweets (# tweets): This indicates how active a user is when disseminating information and promoting his/her opinions.

2. Rank by the number of followers (# followers): This number is directly available on Twitter to show the popularity of the user.

3. Rank by the number of times being retweeted (# retweeted): Retweeting is a major mechanism on Twitter for disseminating information and opinions. A highly retweeted user tends to be one with strong opinions and high influence on a particular topic.

4. Rank by the number of times being retweeted and retweeting others (degree): In a directed graph, that shows the retweeting network among users, this number is the degree (in-degree + out-degree) centrality score of each node.

For each ranking method, we compare the performance of the three opinion classifiers (CC, LP, and GCM) by varying the percentage of top-ranked users included in the training set. In particular, when the percentage of top users is 100%, all visibly opinionated users were included in the training set. Then, we gradually decrease the percentage until only the topmost user from each class is included. Figures 3–5 show the average precision, recall, and F-measure scores of robustness tests for the three classifiers.

As shown in Figure 3, as the size of the training set decreases, the performance of CC is initially stable in the beginning and starts decreasing when the percentage reaches about 25%. The irregular shapes of the curves near the left end (percentage < 10%) indicate that the classifiers fail due to insufficient training data and therefore assign all or most instances in the test set to only one of the two classes. Among the four ranking methods, the “rank by # tweets” method seems to be more robust and can maintain performance until the training set size is below approximately 10%. This is because the selected users are the most active ones who posted the most tweets, which provides sufficient data instances to achieve the best performance possible for this classifier.

Figures 4 and 5 show the results for the two link-based methods, LP and GCM. For all four ranking methods, with only minor fluctuations, LP shows consistently high performance for classification, even when only a very low percentage of data instances are included in the training set. In particular, for “rank by # retweeted” and “rank by degree,” even if only one positive and one negative instance are available in the training set, due to the high connectivity of the graph, LP can still successfully propagate the correct class labels to nodes and achieve almost the same performance. For “rank by # tweets” and “rank by # followers,” LP also maintains good classification performance

#

until the training set is reduced below 1.5% (i.e., two instances for each class) and 1% (one instance for each class), respectively.

GCM achieves slightly better results than LP when 100% of the opinionated users are used as training data. However, the robustness of GCM against the training data size varies for different ranking methods used to select the seed users. In particular, for “rank by # tweets” and “rank by # followers,” GCM’s classification performance starts dropping drastically when the training set’s size is below 75%. It is highly likely that some key nodes that are critical to graph partition in GCM classifiers were excluded in the training set due to low number of tweets and/or followers. Therefore, GCM fails to work for the remaining nodes in the graph. Nevertheless, for the other two ranking methods “rank by # retweeted” and “rank by degree,” GCM’s performance is a lot more robust. When the training set percentage is reduced from 100% to 2%, GCM constantly gives exactly the same classification results (best among all: 96.96% precision, 95.63% recall, and 96.29% F-measure). Only when the training set is reduced below 2% (i.e., less than two positive and two negative instances), the GCM classifier fails to work.

## Discussion

Our experimental study helps us answer the three research questions. The results also provide us with several interesting insights into the interaction dynamics of online debates on social media such as Twitter.

The main challenges for opinion mining on Twitter data include the short length (i.e., 140-character limit) and informal style. Given limited word features and high variations in style, traditional CC showed poor predictive capability for differentiating users with opposite opinions. People can say different entities to express their opinions. However, their precise words may not clearly reveal which side they take in a debate. It is important to consider that a debate must involve people from two sides arguing against each other. On each side, remarks of opinionated leaders can be widely spread by supporters via actions such as “retweet” and “like” on a social media platform. Such interaction and

#

communication results in a high degree of connectivity in social networks. These linkages between users become an additional and evidently more reliable source for opinion classification. Link-based classifiers, such as LP and GCM, consider that users opinions are not independent, but interrelated. Rather than predicting the opinion of each individual user separately, LP and GCM try to collectively classify users based on their linkage structures. In a social network involving two sides debating, linkages may carry a variety of meanings regarding the relationship between the two connected users. In our study, we design the classification algorithm based on a highly simplified assumption that a retweeter tends to share the same opinion as the retweetee. Even under such a strong assumption, the classifiers can give surprisingly high accuracy.

Moreover, the results of robustness tests further strengthen our conclusion on the superiority of link-based opinion classifiers over CC, particularly when only a small training set is available. As shown in Figure 3, CC show fine robustness against reduced training set size. Particularly for the “rank by # tweets” method, the classification accuracy (\~72%) did not drop much until the training set was reduced to approximately 10%. This might be partly attributed to the high degree of information redundancy exhibited in tweets and retweets, especially during a short time period of debate on one specific topic. Even visibly opinionated users do not always post original tweets. They retweet, too. As long as we have enough content (tweets and retweets) from the most active users, CC can still show appreciable performance. By contrast, for link-based classifiers, if chosen wisely (e.g., based on “rank by # retweeted” and “rank by degree”), only a handful (e.g., one or two instances from each class) of visibly opinionated users could be sufficient as training data instances to achieve the highest classification accuracy (\~93%). Nevertheless, the link-based classifier, GCM, could become unpredictable if some critical annotated nodes are left out (e.g., based on “rank by # tweets” and “rank by # followers”). Therefore, the connectivity to other nodes in the graph is key to robust performance of link-based classifiers. During an online debate, opinion leaders may not necessarily be the most active tweeters or well-known celebrities with the most followers. Rather, given a reasonable size of followers, someone who posts tweets with sharp opinions or brilliant remarks, as long as they get more retweets, can stand out as real leaders of public opinion. Successfully identifying these “critical” opinionated users could guarantee a high accuracy for opinion classification with only minimum effort to create a training data set. On the contrary, if inappropriate ranking methods were chosen, one may fail to identify the real critical opinionated users, which can lead to low accuracy of opinion classification. Furthermore, identification of the critical users and further analyzing their content and behaviors can provide better insights into the key arguments and political appeal.

## 5. Conclusions and Future Directions

In this study, we propose a GCM algorithm to address the collective opinion classification problem. Our algorithm collectively assigns users’ states in Twitter discussions that match their retweeting behaviors to others’ postings. In experiments on a real-world data set, the proposed approach is significantly more accurate than the stateof-the-art approach. Further analysis shows that our proposed algorithm performs exceptionally well even with only a handful of training users.

Classifying user opinions is a critical challenge for e-commerce companies. This study provides a novel opinion classification solution that addresses the volume, velocity, and variety issues of big social media data. By analyzing a large amount of opinion-related data in microblogging sites, our solution based on GCM exploits the social interactions among users for classification. It shows high accuracy and robustness to the limited size of labeled data for training.

This study has significant practical and theoretical implications for big data analytics in e-commerce. For practitioners, a more accurate classifier that requires a smaller training data set can significantly reduce the effort needed to plan and conduct marketing campaigns. Facing a social network of competitive opinions, companies need to develop different marketing strategies for populations that are for or against their products. By conducting opinion classification on a topic at multiple time points, companies can obtain a dynamic view of how opinions evolve over time so that they can react and adjust their strategies accordingly. In the big-data era, such data-driven analytics will become increasingly important to commerce. Moreover, our results provide support for further theoretical studies on the global consistency of social networks in social media analytics.

As we have argued, global consistency may be accounted for by the joint force of network connectivity and social influence. Unlike most previous research focused on individual-level influences, our study indicates the existence of global-level selforganization phenomenon, which is worth further investigation.

In the future, we will explore the following directions to extend this study. (1) We will investigate the combination of content data and linkage data for collective opinion classification. (2) We will investigate social network structures other than two-sided debates on social media and develop new opinion classification algorithms. (3) We will continue studying factors (e.g., topics and stages of events) that can affect the performance of opinion classification in more social media data sets and contexts. Our ultimate goal is to build an effective approach that is scalable to incorporate insights from social relationships for opinion mining.

## References

[1] H. Chen, R.H.L. Chiang, V.C. Storey, Business Intelligence and Analytics: From Big Data To Big Impact, Mis Q. 36 (2012) 1165–1188. doi:10.1145/2463676.2463712.

[2] R.F. Lusch, Y. Liu, Y. Chen, The phase transition of markets and organizations: The new intelligence and entrepreneurial frontier, in: IEEE Intell. Syst., 2010: pp. 71–75. doi:10.1109/MIS.2010.27.

[3] A. Doan, R. Ramakrishnan, A.Y. Halevy, Crowdsourcing systems on the World-Wide Web, Commun. ACM. 54 (2011) 86. doi:10.1145/1924421.1924442.

[4] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets, Inf. Syst. Res. 19 (2008) 291–313. doi:10.1287/isre.1080.0193.

[5] N. Archak, A. Ghose, P.G. Ipeirotis, Deriving the Pricing Power of Product Features by Mining Consumer Reviews, Manage. Sci. 57 (2011) 1485–1509. doi:10.1287/mnsc.1110.1370.

[6] A. Ghose, P.G. Ipeirotis, B. Li, Designing Ranking Systems for Hotels on Travel Search Engines by Mining User-Generated and Crowdsourced Content, Mark. Sci. 31 (2012) 493–520. doi:10.1287/mksc.1110.0700.

[7] C. Oh, O. Sheng, Investigating Predictive Power of Stock Micro Blog Sentiment in Forecasting Future Stock Price Directional Movement, ICIS. (2011) 1–19.

[8] J.L. Zhao, S. Fan, D. Hu, Business challenges and research directions of management analytics in the big data era, J. Manag. Anal. 1 (2014) 169–174. doi:10.1080/23270012.2014.968643.

[9] E.-P. Lim, H. Chen, G. Chen, Business Intelligence and Analytics<sup> </sup>: Research Directions, ACM Trans. Manag. Inf. Syst. 3 (2013) 1–10. doi:10.1145/2407740.2407741.

[10] B. Pang, L. Lee, Opinion Mining and Sentiment Analysis, Found. Trends® Inf. Retr. 2 (2008) 1–135. doi:10.1561/1500000011.

[11] G. Walsh, K.P. Gwinner, S.R. Swanson, What makes mavens tick? Exploring the motives of market mavens’ initiation of information diffusion, J. Consum. Mark. 21 (2004) 109–122. doi:10.1108/07363760410525678.

[12] J.E. Phelps, R. Lewis, L. Mobilio, D. Perry, N. Raman, Viral marketing or electronic word-of-mouth advertising: Examining consumer responses and motivations to pass along email, J. Advert. Res. 44 (2004) 333–348. doi:10.1017/S0021849904040371.

[13] Z. Zhang, X. Li, Y. Chen, Deciphering word-of-mouth in social media, ACM Trans. Manag. Inf. Syst. 3 (2012) 1–23. doi:10.1145/2151163.2151168.

[14] E. Demers, C. Vega, Soft information in earnings announcements: News or noise?, INSEAD Bus. Sch. World. (2010) 1–70. doi:10.2139/ssrn.1153450.

[15] C.C. Yang, Understanding Online Consumer Review Opinions with Sentiment Analysis using Machine Learning Sentiment Analysis using Machine Learning, Pacific Asia J. Assoc. Inf. Syst. 2 (2010) 6.

[16] M.M. Mostafa, More than words: Social networks’ text mining for consumer brand sentiments, Expert Syst. Appl. 40 (2013) 4241–4251. doi:10.1016/j.eswa.2013.01.019.

[17] W. Li, H. Xu, Text-based emotion classification using emotion cause extraction, Expert Syst. Appl. 41 (2014) 1742–1749. doi:10.1016/j.eswa.2013.08.073.

[18] S. Fouzia Sayeedunnissa, A. Hussain, M. Hameed, Supervised Opinion Mining of Social Network Data Using a Bag-of-Words Approach on the Cloud, in: J.C. Bansal, P. Singh, K. Deep, M. Pant, A. Nagar (Eds.), Proc. Seventh Int. Conf. Bio-Inspired Comput. Theor. Appl. (BIC-TA 2012), Springer India, 2012: pp. 299– 309. doi:10.1007/978-81-322-1041-2\_26.

[19] J. Akaichi, Z. Dhouioui, M.J. Lopez-Huertas Perez, Text mining facebook status updates for sentiment classification, in: 2013 17th Int. Conf. Syst. Theory, Control Comput. ICSTCC 2013; Jt. Conf. SINTES 2013, SACCS 2013, SIMSIS 2013 - Proc., 2013: pp. 640–645. doi:10.1109/ICSTCC.2013.6689032.

[20] S. Ben Hamouda, J. Akaichi, Social Networks’ Text Mining for Sentiment Classification<sup> </sup>: The case of Facebook’ statuses updates in the “Arabic Spring” Era, Int. J. Appl. or Innov. Eng. Manag. 2 (2013) 470–478.

[21] M. Myslín, S.H. Zhu, W. Chapman, M. Conway, Using twitter to examine smoking behavior and perceptions of emerging tobacco products, J. Med. Internet Res. 15 (2013). doi:10.2196/jmir.2534.

[22] A. Hassan, A. Abbasi, D. Zeng, Twitter sentiment analysis: A bootstrap ensemble framework, in: Proc. - Soc. 2013, 2013: pp. 357–364. doi:10.1109/SocialCom.2013.56.

[23] F.H. Khan, S. Bashir, U. Qamar, TOM: Twitter opinion mining framework using hybrid classification scheme, Decis. Support Syst. 57 (2014) 245–257. doi:10.1016/j.dss.2013.09.004.

[24] W. Maharani, Microblogging sentiment analysis with lexical based and machine learning approaches, in: Inf. Commun. Technol. (ICoICT), 2013 Int. Conf., 2013: pp. 439–443. doi:10.1109/ICoICT.2013.6574616.

[25] G. Paltoglou, M. Thelwall, Twitter, MySpace, Digg: Unsupervised Sentiment Analysis in Social Media, ACM Trans. Intell. Syst. Technol. 3 (2012) 1–19. doi:10.1145/2337542.2337551.

[26] S. Feng, D. Wang, G. Yu, W. Gao, K.F. Wong, Extracting common emotions from blogs based on fine-grained sentiment clustering, Knowl. Inf. Syst. 27 (2011) 281– 302. doi:10.1007/s10115-010-0325-9.

[27] P. Sen, G.M. Namata, M. Bilgic, L. Getoor, B. Gallagher, T. Eliassi-Rad, Collective Classification in Network Data, AI Mag. 29 (2008) 93–106. doi:10.1145/1217299.1217304.

[28] R. Agrawal, S. Rajagopalan, R. Srikant, Y. Xu, Mining newsgroups using networks arising from social behavior, in: Proc. Twelfth Int. Conf. World Wide Web - WWW ’03, 2003: p. 529. doi:10.1145/775152.775227.

[29] P.F. Lazarsfeld, R.K. Merton, Friendship as a Social Process: A Substantive and Methodological analysis, Free. Control Mod. Soc. 18 (1954) 18–66. doi:10.1111/j.1467-8705.2012.02056\_3.x.

[30] M. McPherson, L. Smith-Lovin, J.M. Cook, Birds of a Feather: Homophily in Social Networks, Annu. Rev. Sociol. 27 (2001) 415–444. doi:10.1146/annurev.soc.27.1.415.

[31] M. Speriosu, N. Sudan, S. Upadhyay, J. Baldridge, Twitter Polarity Classification with Label Propagation over Lexical Links and the Follower Graph, Proc. Conf. Empir. Methods Nat. Lang. Process. (2011) 53–56.

[32] C. Tan, L. Lee, J. Tang, L. Jiang, M. Zhou, P. Li, User-level sentiment analysis incorporating social networks, Proc. 17th ACM SIGKDD Int. Conf. Knowl. Discov. Data Min. - KDD ’11. 136 (2011) 1397. doi:10.1145/2020408.2020614.

[33] J. Rabelo, R.B.C. Prudencio, F. Barros, Collective Classification for Sentiment Analysis in Social Networks, 2012 IEEE 24th Int. Conf. Tools with Artif. Intell. (2012) 958–963. doi:10.1109/ICTAI.2012.135.

[34] J. Rabelo, R.B.C. Prudencio, F. Barros, Using Link Structure to Infer Opinions in Social Networks, in: IEEE Int. Conf. Syst. Man, Cybern., Seoul, Korea, 2012: pp. 681–685.

[35] M.D. Conover, B. Gonçalves, J. Ratkiewicz, A. Flammini, F. Menczer, Predicting the political alignment of twitter users, in: Proc. - 2011 IEEE Int. Conf. Privacy, Secur. Risk Trust IEEE Int. Conf. Soc. Comput. PASSAT/SocialCom 2011, 2011: pp. 192–199. doi:10.1109/PASSAT/SocialCom.2011.34.

[36] F. Wong, C. Tan, S. Sen, M. Chiang, Quantifying Political Leaning from Tweets and Retweets., in: Int. AAAI Conf. Weblogs Soc. Media, 2013.

[37] A. Rajadesingan, H. Liu, Identifying users with opposing opinions in Twitter debates, in: Lect. Notes Comput. Sci. (including Subser. Lect. Notes Artif. Intell. Lect. Notes Bioinformatics), 2014: pp. 153–160. doi:10.1007/978-3-319-05579-4- 19.

[38] Y. Ren, N. Kaji, N. Yoshinaga, M. Toyoda, M. Kitsuregawa, Sentiment Classification in Resource-Scarce Languages by using Label Propagation, in: 25th Pacific Asia Conf. Lang. Inf. Comput., 2011: pp. 420–429.

[39] U.N. Raghavan, R. Albert, S. Kumara, Near linear time algorithm to detect community structures in large-scale networks, Phys. Rev. E - Stat. Nonlinear, Soft Matter Phys. 76 (2007). doi:10.1103/PhysRevE.76.036106.

[40] J.X. Hao, J.B. Orlin, A Faster Algorithm for Finding the Minimum Cut in a Directed Graph, J. Algorithms. 17 (1994) 424–446. doi:http://dx.doi.org/10.1006/jagm.1994.1043.

[41] R.H. Möhring, A.S. Schulz, F. Stork, M. Uetz, Solving Project Scheduling Problems by Minimum Cut Computations, Manage. Sci. 49 (2003) 330–350. doi:10.1287/mnsc.49.3.330.12737.

[42] T.M. Murali, C.-J. Wu, S. Kasif, The art of gene function prediction, Nat Biotech. 24 (2006) 1474–1475. http://dx.doi.org/10.1038/nbt1206-1474.

[43] P.F. Felzenszwalb, D.P. Huttenlocher, Efficient graph-based image segmentation, Int. J. Comput. Vis. 59 (2004) 167–181. doi:10.1023/B:VISI.0000022288.19776.77.

## Jiexun Li

Jiexun Li is an assistant professor in the Department of Decision Sciences, College of Business & Economics, at Western Washington University. He pursued his PhD in Management Information Systems (MIS) from the Eller College of Management at the University of Arizona, MS and BS in MIS at Tsinghua University in China. His research interests include data mining, business analytics, social media analytics, and health informatics. His research works have appeared in journals including JMIS, DSS, IEEE Transactions, JASIST, JAIS, Bioinformatics, CACM, ESA, and ISF.

## Xin Li

Xin Li is an assistant professor in the Department of Information Systems at the City University of Hong Kong. He received his PhD in Management Information Systems from the University of Arizona. He received his BS and MS degrees from the Department of Automation at Tsinghua University, China. His works have appeared in the MISQ, JMIS, INFORMS JOC, DSS, JASIST, ACM and IEEE Transactions, among others.

## Bin Zhu

Bin Zhu is an associate professor of Business Information Systems at Oregon State University. She received her PhD in Management Information Systems from University of Arizona. Her current research interests include business intelligence, information analysis, social network, human–computer interaction, information visualization, computer-mediated communication, and knowledge management systems. Her works have appeared in ISR, DSS, JASIST, IEEE Transactions, D-Lib Magazine, and so on.

Figure captions  
![](/api/attachments/MA2QCY2P/fulltext/images/2be5b5ff5ad06d538566c2ab67d8940b7be3243f54270e354750acee254d3d5b.jpg)  
Figure 1. Transforming an Undirected Graph G into Directed Graph H

![](/api/attachments/MA2QCY2P/fulltext/images/ba1f2ea3f9c809b5a8c489db6b493823691880c8b899e6ffc971dcdc9f2c0295.jpg)  
Figure 2. Pseudo-Code of a Label Propagation Algorithm

![](/api/attachments/MA2QCY2P/fulltext/images/0d0162e0f88dc08de664e72b014c8a7d38bc64cfd2e61c1bec4697059bf1d8e4.jpg)  
(a) rank by # tweets

![](/api/attachments/MA2QCY2P/fulltext/images/37b37df53536c108ae2507878ff1924af79d1f0dd6783640924c291fb61c9bca.jpg)  
(b) ranked by # followers

![](/api/attachments/MA2QCY2P/fulltext/images/d4261df5f050793304d92c5ceb241b62c04c9371d9cbcef3e489d0f09b65108c.jpg)  
(c) rank by # retweeted

![](/api/attachments/MA2QCY2P/fulltext/images/b55e9a83b87803936d7fe36c6d330a61dbd00acb493d340ca6bf9434e54da1f4.jpg)  
(d) rank by degree  
Figure 3. Robustness Test for CC (performance vs. % of training data used)

![](/api/attachments/MA2QCY2P/fulltext/images/c47646de4e47e6f1b11d2e7d710f982f9e8a898c1d0a397c89657e3088d1b0b1.jpg)  
(a) rank by # tweets

![](/api/attachments/MA2QCY2P/fulltext/images/519ac81b945838699fdda814d11169b1acb8f2e06b56544b9b8e88a12fcabcbe.jpg)  
(b) ranked by # followers

![](/api/attachments/MA2QCY2P/fulltext/images/62160d1ba4e3e16ba1d872dac6ce775b976b21e435bd3b9bc5fc7a9b48e7dab5.jpg)  
(c) rank by # retweeted

![](/api/attachments/MA2QCY2P/fulltext/images/ed8212bf1f0adc7451ab1b67f25e51fef240b51da03774092176b083438b3350.jpg)  
(d) rank by degree  
Figure 4. Robustness Test for LP (performance vs. % of training data used)

![](/api/attachments/MA2QCY2P/fulltext/images/6c8091a4032e3126b730168eadc9d9f9e679e93578651196db9e8b94410ed0f1.jpg)  
(a) rank by # tweets

![](/api/attachments/MA2QCY2P/fulltext/images/26ecbda28723965e780b077fb6bb9f48724c7ab8337331a2d3320d70c490f328.jpg)

![](/api/attachments/MA2QCY2P/fulltext/images/203c95a263385b3a775f216a4654cd5965e6c35562cfb9a39e65764c5ee5f21b.jpg)  
(c) rank by # retweeted

(b) ranked by # followers  
![](/api/attachments/MA2QCY2P/fulltext/images/d3c974bc8a248e0135dcca23a72ee22b36ad9f6511757875cac07db393fcd2be.jpg)  
(d) rank by degree  
Figure 5. Robustness Test for GCM (performance vs. % of training data used)

Tables

<table><tr><td colspan="2">Table 1. Data Description of the Twitter Data set</td></tr><tr><td># users (vertices)</td><td>491,860</td></tr><tr><td># isolated users</td><td>215,669</td></tr><tr><td># connected users</td><td>276,191</td></tr><tr><td># visibly opinionated users</td><td>262 (84 for; 178 against)</td></tr><tr><td># moderately opinionated users</td><td>396 (276 for; 120 against)</td></tr><tr><td># of postings</td><td>916,171</td></tr><tr><td># of original tweets</td><td>505,637</td></tr><tr><td># of retweets</td><td>410,534</td></tr><tr><td># edges</td><td>384,331</td></tr></table>

Table 2. Classification Matrices of Three Opinion Classification Methods

<table><tr><td colspan="2">Predicted\Actual</td><td>For</td><td>Against</td></tr><tr><td>CC</td><td>For</td><td>184</td><td>17</td></tr><tr><td></td><td>Against</td><td>92</td><td>103</td></tr><tr><td></td><td>Undetermined</td><td>0</td><td>0</td></tr><tr><td>LP</td><td>For</td><td>267</td><td>17</td></tr><tr><td></td><td>Against</td><td>8</td><td>102</td></tr><tr><td></td><td>Undetermined</td><td>1</td><td>1</td></tr><tr><td>GCM</td><td>For</td><td>267</td><td>16</td></tr><tr><td></td><td>Against</td><td>8</td><td>103</td></tr><tr><td></td><td>Undetermined</td><td>1</td><td>1</td></tr></table>

Table 3. Prediction Performance of the Three Opinion Classification Methods

<table><tr><td>Methods</td><td colspan="2">Accuracy (%)</td><td></td><td>For</td><td></td><td colspan="2"></td><td>Against</td><td></td></tr><tr><td colspan="2"></td><td></td><td colspan="4">Precision (%) Recall (%) F-measure (%)</td><td colspan="3">Precision (%) Recall (%) F-measure (%)</td></tr><tr><td>CC</td><td colspan="2">72.47</td><td>91.54</td><td>66.67</td><td>77.15</td><td colspan="2">52.82</td><td>85.83</td><td>65.40</td></tr><tr><td>LP</td><td colspan="2">93.18</td><td>94.01</td><td>96.74</td><td>95.36</td><td colspan="2">92.73</td><td>85.00</td><td>88.70</td></tr><tr><td>GCM</td><td colspan="2">93.43</td><td>94.35</td><td>96.74</td><td>95.53</td><td colspan="2">92.79</td><td>85.83</td><td>89.18</td></tr></table>
