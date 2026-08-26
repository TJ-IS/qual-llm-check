---
otero_id: 12326
otero_key: "HNEHPFBA"
title: "An influence framework on product word-of-mouth (WoM) measurement"
authors: "Kun Chen; Peng Luo; Huaiqing Wang"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2016.06.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: An Influence Framework on Product Word-of-mouth (WoM) Measurement

Author: Kun Chen Peng Luo Huaiqing Wang

![](/api/attachments/HNEHPFBA/fulltext/images/c8f011c9011480a98f304559cb2349925fa117a27d9df6757bea5945772faa1c.jpg)

PII: S0378-7206(16)30066-0

DOI: http://dx.doi.org/doi:10.1016/j.im.2016.06.010

Reference: INFMAN 2923

To appear in: INFMAN

Received date: 25-12-2015

Revised date: 24-5-2016

Accepted date: 19-6-2016

Please cite this article as: Kun Chen, Peng Luo, Huaiqing Wang, An Influence Framework on Product Word-of-mouth (WoM) Measurement, Information and Management http://dx.doi.org/10.1016/j.im.2016.06.010

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# An Influence Framework on Product Word-of-mouth (WoM)

# Measurement

## Kun Chen

Department of Financial Mathematics and Financial Engineering, South University of Science and Technology,

Shenzhen 518055, China, E-mail: chenk@sustc.edu.cn, Tel: +86-755-88018668, Fax: +86-755-88018680

Peng Luo

School of Management, Harbin Institute of Technology, Harbin 150001, China, E-mail: luopeng\_hit@126.com,

Tel: +86-186-4606-5159

Huaiqing Wang

Department of Financial Mathematics and Financial Engineering, South University of Science and Technology,

Shenzhen 518055, China, E-mail: wanghq@sustc.edu.cn, Tel: +86-755-88018606, Fax: +86-755-88018680

## Corresponding Author:

Kun Chen

Department of Financial Mathematics and Financial Engineering

South University of Science and Technology

Shenzhen 518055

China

Tel.: +86-755-88018668

Fax: +86-755-88018680

E-mail: chenk@sustc.edu.cn

## Highlights:

 A product-comparative network and inter-communication network were constructed.

 The transitive influence in a network was assessed.

 Influence-based product WoM was measured.

The superior predictive power of the influence-based product WoM to other product WoM measures was illustrated.

## Abstract

With the development of e-commerce platforms, online customer reviews have become an important instrument for providing product word-of-mouth (WoM) information. Analyzing and measuring WoM is quite valuable in product design, sales prediction, marketing strategy, and other decision-making tasks. In contrast to previous studies that analyze product WoM focusing on a single product, we propose an influence framework to measure WoM from a market perspective. In this framework, we combine product competition relationships and customer intercommunication relationships to construct a two-layer network and calculate the node influence effects in the network. To compare different product WoM measures, we use product sales as a predictor and build a series of predictive models. In the experiments conducted based on Amazon.com data, we find that, first, textual sentiment analysis produces a better summary of customer opinions than rating scores. Second, product-comparative relationships provide additional information on measuring product WoM. Third, the customer intercommunication feature in social media is useful for measuring the collective opinions about a product. The influence framework and experimental findings have both theoretical and managerial implications.

## Keywords

Social influence, product network, sentiment analysis, word of mouth, product sales

## 1. Introduction

With the rapid development of e-commerce, increasing numbers of products are being sold on the Web, and these sales are accompanied by rich customer reviews and feedback. According to a survey conducted by BrightLocal , 88% of consumers read reviews to determine the quality of a local business, 85% of consumers read up to 10 reviews, and 88% of consumers say they trust online reviews as much as personal recommendations. Online customer reviews provide important electronic word-of-mouth (WoM) information about a product, service, brand, or company. Analyzing and measuring WoM is quite valuable in helping companies and consumers make decisions [1].

In various e-commerce platforms, customers often offer a rating on a specific scale as a measure of the overall evaluation and write texts of arbitrary length that may serve as a justification for the rating [2, 3]. Measuring WoM is thus a technique problem in marketing and information systems (IS) research. The simplest but most common measure is using numerical ratings to evaluate customer opinions, such as the average number of ratings, the variance or standard deviation of ratings, and the quartile of ratings [4, 5]. Although customer ratings are useful, still some studies have pointed out that the numeric ratings may suffer from “underreporting bias” – that people who think a product is of low quality are more likely to write a review in text [6]. To further analyze the review contents, text mining and sentiment analysis techniques are used to summarize customers’ opinions and product features from texts [7]. They evaluate the polarity of a review or list the pros and cons of product features. However, no matter the method applied, the basis of measuring WoM is limited to analyzing data about a single product or a single feature.

In a real-world market, products and product features are usually compared with each other, so their WoMs are valued collectively in a complex manner by humans. For example, products of the same brand often support each other, according to brand trust and brand loyalty theory [8]. A positive WoM of a product would have a potential enforce effect on other products of the same brand. Conversely, products in a category often compete with each other because when a particular product is favored it often indicates that other products in the same category are less favored [9]. In the competing environment, a positive WoM of a product would have a substantial weakening effect on other products in the same category.

The cognition of review contents also occurs in a complex manner. Considering the intercommunication natural in social media, the discussions and debates about one topic often lead to an overall opinion, which is inferred and summarized by readers. For example, a negative reply to a negative review often reflects a positive opinion. If we analyze the negative reply individually, the assessment would thus be biased. Therefore, the interaction between customers is another important dimension that should be considered when measuring product WoM, especially in mining the underlying polarity in text.

According to the above analysis, although it has received limited attention, measuring product WoM using the market structure and the intercommunication structure is a way that closely conforms to human cognition process. Therefore, this study aims at designing a two-layer influence framework to inspect the inter-product influences and intercommunication influences in measuring product WoM. Previous studies have demonstrated that product WoM is useful in predicting product sales [4, 10, 11]. Thus, we set the product sales rank as the dependent variable and build several predictive models using different product WoM measures. Based on the customer review data from Amazon.com, our experimental study illustrates that both inter-product relationships and intercommunication relationships can leverage the product WoM metric by improving its predictive power regarding sales.

The findings have both theoretical and managerial implications. On the theoretical front, social influence theory has suggested that people’s emotions, opinions, and behaviors are affected by others [12]. We extend the current social influence research by introducing product relationships and intercommunication relationships as a mediator to measure WoM influential effects. We also contribute to the marketing literature by providing a new model for product WoM measure and sales prediction. On the practical front, this research provides a good visualization tool for business intelligence, and it gives practical suggestions for WoM surveillance.

We first review the background and relevant literature in section 2. Section 3 and section 4 introduce the research framework and model design, respectively. Section 5 describes the empirical study. Section 6 discusses the findings and implications.

## 2. Background Study

## 2.1 Market Structure and Competitive Intelligence in Text Mining

Customer reviews contain substantial information about products, product features, and product relations. Mining this information using text mining and natural language processing techniques is a popular trend in both marketing and IS fields. In th is study, we aim at exploring a network structure between products to measure their relations. Thus, we focus on those studies about the product network, which is also called product map or graph (as shown in Table 1). Two representative networks, the product-associative network and the product-comparative network, are studied. The product-associative network illustrates the relationships between products and their attributes [13]. The pros and cons are often extracted according to the product’s attributes. The network is helpful in understanding the market structure and making decisions. For example, Henderson et al. [14] demonstrated the use of brand-associative networks to understand relationships among brands such as competitiveness, complementarity, segmentation, and market structure. The product-comparative network is used to identify the comparative opinions between products. It proposes an intuitive illustration about product-comparative relations for competitive intelligence [22]. Different from other studies that emphasize

<table><tr><td rowspan="2">Study</td><td rowspan="2">Network</td><td rowspan="2">Node</td><td colspan="2">Relationship Mining</td><td rowspan="2">Application</td></tr><tr><td>Method</td><td>Data</td></tr></table>

structural-level findings, Zhang et al. [19] used the comparative network as product WoM

indicators and predicted the sales rank.

Table 1. A summary on product network

<table><tr><td>Lee and Bradlow [15]</td><td>PAN</td><td>Product + attributes</td><td>ML (K-means)</td><td>message</td><td>Market structure</td></tr><tr><td>Netzer et al. [16]</td><td>PAN</td><td>Product + attributes</td><td>Statistic (frequency)</td><td>message</td><td>Market structure</td></tr><tr><td>Akiva et al. [7]</td><td>PAN</td><td>Brand</td><td>Statistic (frequency)</td><td>message</td><td>NA</td></tr><tr><td>Henderson et al. [14]</td><td>PAN</td><td>Brand + features</td><td>Algebra (matrix)</td><td>message</td><td>Market structure + Brand relations</td></tr><tr><td>Jindal and Liu [20]</td><td>PCN</td><td>Product</td><td>Rules + ML (Naïve Bayes)</td><td>sentence</td><td>NA</td></tr><tr><td>Jindal and Liu [21]</td><td>PCN</td><td>Product</td><td>Rules</td><td>sentence</td><td>NA</td></tr><tr><td>Xu et al. [22]</td><td>PCN</td><td>Product</td><td>ML (Conditional random field)</td><td>sentence</td><td>Competitive intelligence</td></tr><tr><td>Zhang et al. [19]</td><td>PCN</td><td>Product</td><td>Semantic Lexicon</td><td>message</td><td>Product WoM</td></tr></table>

PAN: product-association network; PCN: product-comparative network; ML: machine learning

Technically, the underlining theoretical basis in relationship mining is the detection of the occurrence of two terms in a sentence or a message. This detection is supported by the notion of memory-associative networks [15] and has strong roots in the co-word analysis literature [16]. The co-occurrence method is used directly to identify product (attribute) relations in the product-association network. For example, Netzer et al. [17] and Akiva et al. [7] built networks by assessing the proximity or similarity between several terms (product and attributes) based on the frequency of their co-occurrence in the text. In the product-comparative network, co-word analysis is used to select candidate data. Researchers focus on the sentences and messages that contain comparative opinions to analyze competitive relations.

In product relationship mining, machine learning, statistical, and rule-based reasoning are popular methods. Machine-learning algorithms are often used for clustering and classification. For example, Lee and Bradlow [18] use the bag-of-words model and the K-means algorithm to extract product attributes, and they further classify the attributes based on their strengths and weaknesses. Jindal and Liu [19, 20] propose using rules and Naïve Bayes classifiers to identify comparative sentences and comparative relationships in these sentences. Xu et al. [21] use a conditional random field-based method to extract the comparative relationships between products in a sentence. Different from machine learning and statistical methods, Zhang et al. [22] use a semantic lexicon method to measure the comparative relations.

We borrow Zhang’s method for product-comparative network construction in the present study because of the following reasons. First, the method filters co-occurrence data on a message level instead of a sentence level, thereby enlarging the candidate dataset. This is helpful in dealing with sparse candidate data that strictly require two product names appearing in the same sentence. Second, they use the relative sentiment (positive/negative) score to identify the comparative relationships (direct links) between two products. Using existing sentiment dictionaries (e.g., Senti-WordNet [23]), the polarity score is easy to access. It is thus more suitable for WoM numerical calculation compared with sentiment classification methods. Moreover, compared with machine-learning methods [19] and rule-based methods [20, 21], this method is more straightforward and does not rely on a training set. Actually, many opinion mining studies have been done using this lexicon method, such as [24, 25]. Last but not least, Zhang’s work is the only literature that incorporates product relations in measuring product WoM. In order to compare our work with theirs, we employ the same method to construct the product-comparative network. The difference is that they use network structural metrics to measure product WoM, but we propose two-layer network influential metrics to measure product WoM.

## 2.2 Collective Sentiment Analysis in Social Media

In traditional sentiment analysis research, attempts are made to determine the opinions, evaluations, speculations, and emotions in a document [1, 26, 27]. The context of documents and the potential connections between documents have received limited attention.

In social media environments (such as Internet forums, blogs, instant messaging, and social networking sites), a user can publish a post to share with others, and other users can read and comment on the post; these comments can, in turn, be read and commented on [28]. Therefore, the sentiment analysis of a topic in an aggregated measurement is often much more meaningful than the evaluation of every single comment individually. Representative approaches to collective sentiment include simple and weighted averages. In the WoM field, which is the focus of this paper, the simple arithmetic average of individual review polarity and the usefulness weighted average of individual review polarity, among other measurements, are used to gauge the aggregated polarity [29].

Inspired by the intercommunication feature of social media, recently, work has begun to evaluate collective sentiments by a network structure. Li et al. [28] constructed a graph model based on replies, quotations, and semantic relationships between user comments to improve a news recommendation service. Miller et al. [30] analyzed a large hyperlinked network of mass media and Weblog posts to determine how the sentiment features of a post relate to the sentiment of connected posts and the structure of the network itself. They discovered that the sentiment of a post is affected not only by the sentiment of its immediate parent but also by its position within a cascade. Tan et al. [31] showed that information regarding social relationships can be used to improve user-level sentiment analysis. They used a social network model based on Twitter to improve sentiment classification algorithms. All these previous studies show that the collective sentiment of a post is affected by its neighbors, but none of them proposes a measurement to evaluate the aggregated sentiment in a network model.

2.3 Product WoM Measurement and Sales Prediction

Product WoM is embedded in online customer reviews and ratings. How to transform textual communication information into quantitative measures is an important question in WoM research [17]. To further investigate the business applications of WoM indicators, a number of studies have established linkages between WoM and product sales. We focus on the two aspects to do a literature review (as shown in Table 2). Hyrynsalmi et al. [32] summarize that WoM dimensions include “verbal, valence, variance, volume and helpfulness of reviews.” Therefore, quantitative summaries of reviews, such as overall product ratings [4, 5] and fractions of ratings [4], as well as statistical analyses of reviews, such as the review length and review volumes [10, 33, 34], are used to assess the product WoM and predict sales. For example, Chevalier and Mayzlin [4] examine the effect of consumer reviews on the relative sales of books at Amazon.com and Barnesandnoble.com using, for example, the factors of average ratings, fractions of one-star reviews, and fractions of five-star reviews as WoM measures. Liu [34] employs the volume and valence of posts on Yahoo! Movies message boards as movie WoM measures and investigates their influences on box office sales. Conversely, Godes and Mayzlin [33] find that instead of volume itself the dispersion of conversation volumes across communities, which is another

WoM measure, has explanatory power in a dynamic model of TV ratings. Some other studies, that is, Filieri [35] and Jeong et al. [36], also investigate the information adoption and usefulness of online customer reviews, which are also important WoM dimensions.

Table 2. A summary on WoM measures

<table><tr><td>Study</td><td>WoM Dimensions</td><td>Method</td><td>Investigation</td></tr><tr><td>Chevalier and Mayzlin [4]</td><td>Average ratings, fractions of one-star reviews, fractions of five-star reviews</td><td>Statistic</td><td>Sales rank</td></tr><tr><td>Liu [33]</td><td>Volume and valence of posts</td><td>Statistic</td><td>Box office sales</td></tr><tr><td>Godes and Mayzlin [32]</td><td>Dispersion of conversation volumes</td><td>Statistic</td><td>TV rating</td></tr><tr><td>Hyrynsalmi et al. [34]</td><td>Volume, valence, variance</td><td>Statistic</td><td>Sales</td></tr><tr><td>Filieri [35]</td><td>Information helpfulness, rating</td><td>Survey</td><td>Information diagnosticity</td></tr><tr><td>Jeong et al. [36]</td><td>Valence, objectivity/subjectivity</td><td>Statistic</td><td>Usefulness</td></tr><tr><td>Zhang et al. [11]</td><td>Sentiment divergence</td><td>Sentiment analysis</td><td>Sales rank</td></tr><tr><td>Archack et al. [10]</td><td>Product features</td><td>Text mining</td><td>Sales rank</td></tr><tr><td>Zhang [29]</td><td>Lexical and syntactic features</td><td>Text mining</td><td>Sales rank</td></tr><tr><td>Ghose and Ipeirotis [37]</td><td>Subjectivity, readability, and spelling errors</td><td>Text mining</td><td>Sales rank, helpfulness</td></tr><tr><td>Zhang et al. [19]</td><td>Rating, volume, network structure</td><td>Sentiment analysis</td><td>Sales rank</td></tr><tr><td>Our study</td><td>Polarity value, helpfulness</td><td>Collective sentiment analysis + Product influence</td><td>Sales rank</td></tr></table>

Although the aforementioned studies demonstrate that the summary statistics of customer rating and review information are useful in measuring product WoM, they also highlight the need to extract extra information from text. The representative work involving text mining techniques includes sentiment analysis, feature extraction, and usefulness analysis. Zhang et al. [11] focus on sentiment divergence in consumer product reviews and report significant effects on product sales. Archak et al. [10] decompose textual reviews into segments that describe different product features and use these features as new measurements to predict sales. Zhang [29] use lexical and syntactic features in text to identify their relationships with usefulness and sales in four product categories. Ghose and Ipeirotis [37] further construct multiple text-based measurements, including subjectivity, readability, and spelling errors, to predict the effect of reviews on sales and their perceived usefulness.

In contrast to the previous research on single-entity (product)-oriented WoM analysis and single-dimension-based WoM measurement, little work has been conducted regarding multiple-product and multiple-dimension WoM analysis. Zhang et al. [22] use customer messages to build a directed network to provide extra variables about product competitive relationships, such as a product’s centrality position in a network, for sales prediction. The question of the extent to which the network structure affects a product’s WoM – in other words, the question of how to measure a product’s WoM taking into consideration the product influence effects – remains unanswered.

## 2.4 Research Gap

In summary, unlike previous studies, WoM analysis in social media has a unique underlying network structure, which has not yet been carefully studied. The network framework includes not only the product-comparative network but also the interactive customer communication network. Our research aims at applying a two-layer network model to evaluate product WoM by incorporating the inter-effect influences between products and between customers. Moreover, we further examine the predictive effects of proposed WoM measures on product sales, which have significant practical implications for marketing.

## 3. Research Design

## 3.1 A Two-layer Network Construction

Inspired by a previous study, we propose a two-layer network as a new computational construct by exploiting both product-comparative relationships and customer intercommunication relationships (as shown in Fig. 1).

![](/api/attachments/HNEHPFBA/fulltext/images/38fd987163e2599258bb771c6bf0fb89973e6b962636710d4717ef29c9da8f24.jpg)

![](/api/attachments/HNEHPFBA/fulltext/images/72eadbaae070d25f2b592553bd35d1df046c6eda0ab3a08e361b0f445c1b29e9.jpg)  
Figure 1. Two-layer network

In the product network, following the research of Zhang et al. [22], each node represents a product and a direct link indicates a comparative relationship between two products. At the same time, the corresponding weight on each link indicates the sentiment strength of the comparison relationship. This network is formally defined as follows.

Assume that each sentence in the review text for p1 along with a mention of p2 is mapped into a comparison tuple t = {p1, p2, Polarity}, where polarity measures the sentiment value of this sentence. In each tuple, p1 is the target product and p2 is the mentioned product. The polarity value of the sentence is calculated by the algorithm shown in Table 1. As suggested by Zhang et al. [22], a positive score implies that p1 is superior to p2 and vice versa. A direct link from p2 to p1 is produced if the linguistic context conveys a considerable amount of dominating positivity:

Edge e from node p2 to node p1 is introduced when polarity > 0.

Edge e from node p1 to node p2 is introduced when polarity < 0.

Given all directed edges from p1 to p2 (or from p2 to p1), they are aggregated to produce a single link with a weight:

#

$$
\left| \sum_ {i = 1} ^ {n} P o l a r i t y _ {i} \right|\tag{1}
$$

Suppose we have two comparison tuples $\mathbf { t } = \{ \mathsf { p } \mathsf { l } , \mathsf { p } 2$ , polarity} and two comparison tuples $\mathbf { t } =$ {p2, p1, polarity} as follows:

$$
\mathrm{t1} = \{\mathrm{p1}, \mathrm{p2}, 0. 1 7 6 \}, \mathrm{t2} = \{\mathrm{p1}, \mathrm{p2}, - 0. 0 4 9 \}, \mathrm{t3} = \{\mathrm{p2}, \mathrm{p1}, 0. 1 6 6 \}, \mathrm{t4} = \{\mathrm{p2}, \mathrm{p1}, - 0. 0 9 8 \}
$$

Tuples t1 and t4 generate a link from p2 to p1, and tuples t2 and t3 generate a link from p1 to p2. Therefore, we obtain a value of $0 . 0 7 8 = ( 0 . 1 7 6 \mathrm { - } 0 . 0 9 8 )$ as the weight on the link from p2 to p1 and a value of $0 . 1 1 7 = ( - 0 . 0 4 9 + 0 . 1 6 6 )$ as the weight on the link from p1 to p2.

In the communication network, we construct a network with each node representing a product or a post (review or reply), and a direct link indicates a review on a product or a reply to a review. The corresponding weight of each link indicates the usefulness of this review or reply. This network is formally defined as follows.

Assume that V is the set of all text nodes, P is the set of all product nodes, and E is the set of edges. The product is the root, and all reviews are ordinary nodes. There is a directed edge $\pmb { e } \in \pmb { E } f$ rom nodes u to v, $u \in V , v \in P ,$ denoted by (u, v), if the corresponding review u is made on product v. Simultaneously, there is directed edge $\pmb { e } \in \pmb { E } \jmath$ from nodes t to s, $t \in V , s \in$ , denoted by (t, s), if the corresponding reply t is made on review s. The usefulness score of each text node is the weight of each link.

In the communication network, we use the polarities of reviews to measure the sentiment value of a product or a review. Using a sentiment dictionary (e.g., Senti-WordNet [23]), we measure the polarity [25] using the following process (see Table 3). We first extract all the words in a sentence. Adjectives are matched to their closest neighboring adverbs. The positive/negative degree of the adverb is added to the adjective. Finally, we calculate the average sentiment score of words in the sentence.

Table 3. Algorithm for calculating text polarity.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: a piece of text T
Output: a polarity value of text T
For each sentence
Generate word feature set F with POS tags
For each adj. word  $w_{1} \in F$ 
If find its nearest neighbor adv. Word  $w_{2} \in F$ 
Calculate the sentiment score of word pair  $(w_{1}, w_{2})$ ,  $Sentiment_{(w_{1}, w_{2})} =$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$Sentiment_{w_1} \times Sentiment_{w_2}$, and assign it to $Sentiment_{w_1}$

Calculate polarity value of sentence $p_{sentence} = \sum_{i=1}^{i=n} Sentiment_{w_i}/n$, $n = count(w_i)$

Calculate polarity value of text $p = \sum_{j=1}^{m} p_{sentence_j}$
</div>

## 3.2 Network Influence

In social networks, the peer effect of the people close to an individual is an important factor in measuring individual’s behavior [38–40]. Many previous studies construct the network and use network structure parameters, such as degree and centrality, to measure the network influence. However, there is no definition with which to measure the node-level influence. Inspired by the definition of Bonacich centrality [41], which considers the direct and indirect connection influences to measure node centrality, we define the transitive influence on the node as follows.

The n-square adjacency matrix $G$ of product network g keeps track of the direct connections. We define that i and j are directly linked if and only if $g _ { i j } > 0$ and $G ^ { k }$ is the k th power of $G$ , where $k$ is an integer. Matrix $G ^ { k }$ monitors the indirect connections in the network. The vector of nodes’ initial values is denoted by I . Given the scalar $a \ge 0$ , we define TI (the transitive influence) as follows:

$$
T I (g, a) = \sum_ {k = i} ^ {K} a ^ {k} G ^ {k} I\tag{2}
$$

where $i = 1$ in the communication network, $i = 0$ in the product network, and $K$ is a range parameter to control the maximum degree of indirect connections. Parameter a is a decay factor that scales down the relative weight of longer paths.

In a product network, the WoM of a product is affected by its neighbors. For example, if the vector of a product’s average rating is denoted by R , the TR (transitive rating) is defined as follows:

$$
T R (g, a) = \sum_ {k = 0} ^ {K} a ^ {k} G ^ {k} R\tag{3}
$$

where K begins from 0. When k=0, it means the average rating on the focal product is included. $\alpha = 1 / d$ , where d is the largest distance between two nodes in the network.

In a communication network, there are only two layers: the review layer and the reply layer. Therefore, it is much easier to calculate the transitive sentiment in the review network than in the product network. Unlike the product network, in which a link’s weight is the comparative relation (positive or negative) between two products, the link’s weight in a communication network is the reviews’ or replies’ usefulness score. Accordingly, when the sentiment of the review is negative, it constitutes a special case. If the reply to this review is positive, the transitive influence of the reply to the product is negative. Conversely, if the reply to the same review is negative, the transitive influence of the reply to the product is positive. Therefore, we add a minus in front of a reply’s transitive sentiment when the sentiment of its linked review is negative. Moreover, because the largest distance between the nodes is two in the review network, we set the decay factor $a = 0 . 5$

Given the algorithm in Table 1, the transitive sentiment in communication network ( TRS ) is defined based on the intercommunication structure. For product i , the transitive sentiment is as follows:

$$
T R S \left(g _ {i} ^ {\prime}, 0. 5\right) = \sum_ {k = 1} ^ {K} (0. 5) ^ {k} \left(G _ {i} ^ {\prime}\right) ^ {k} S ^ {\prime}\tag{4}
$$

where $g _ { i } ^ { ' }$ is the review network to product i , $\boldsymbol { G } _ { i } ^ { \prime }$ is the corresponding adjacency matrix, and $S ^ { \prime }$ is the sentiment matrix of reviews and replies. In particular, k begins from 1. This is because we want to use the communication network to measure product sentiment. Therefore, the sentiment influence on each path is added up to measure the focal product.

Combining the product network and communication network, we can calculate a two-layer transitive sentiment ( TTS ) value. Based on the product network $_ g$ and its corresponding adjacency matrix G , the two-layer transitive sentiment is defined as

$$
T T S (g, a) = \sum_ {k = 0} ^ {K} a ^ {k} G ^ {k} [ T R S ]\tag{5}
$$

where TRS denotes the column matrix constructed by products’ transitive sentiment values in the communication network.

Table 4 displays the algorithm on calculating transitive sentiment in a product network or in a communication network. We use a depth-first search method to list paths and accumulate sentiment values. The sentiment values are polarity values outputted in algorithm 1 (Table 3).

Table 4. Algorithm for calculating transitive sentiment

Input: a graph G (product graph or customer review graph), in which each node

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
has a sentiment (polarity) value  $s_{i}$  and a weight  $w_{ij}$  on the link between node i and node j

Output: a transitive sentiment value TS on node i in G

Set S as an empty FIFO queue

Do a depth-first search in G

For each node i in a path

Push vector  $v = &lt;\{s_{i}, w_{ij}\}&gt;$  into S

While s is not empty

Pop vector v from s

For k = k, k-1, ...1 //k is the number of nodes in a path

Pop vector v from S

Set c = the last element of v

TS =  $\sum_{k=0}^{k} \alpha^{k} w_{ik} s_{i}$ 

Delete c from v

Return TS
</div>

## 3.3 A Toy Example

As shown in Fig. 2, a customer posts a review (R1) about the product Samsung Galaxy S5 (P1). In this review, she/he mentions another product, (Samsung Galaxy) S3 (P2), in the following sentence: “Not bad in comparison to the S3 I had.” According to the polarity-calculating algorithm described in Table 1, the sentiment value of this sentence is 0.7982. Therefore, there is a direct link from P2 to P1 with a weight of 0.7982. By further examining the customer reviews, R1 is found to have a sentiment value of 0.2781 on the whole text, which points to P1 with a weight of $9 8 / I 0 6 ^ { 2 }$ (97 out of 105 people found the following reviews helpful). A user called “Shiran” posts a reply (C1) to R1. It says, “I believe the door is there…As it often goes one has to sacrifice a little bit of convenience….” C1 has a sentiment value of −0.0446, which points to R1 with a weight of 3/4 (two out of three people think this post adds to the discussion).

In the network graph illustrated in Fig. 2, several paths link to the target product S5. Taking the path C1->R1->S5 as an example, we demonstrate how to calculate the TRS score. We set the decay factor as (1/2), which is decided by the largest distance between the nodes in the graph. For the influence from R1 to S5, the path length is k=1, so the TRS score is $0 . 1 2 8 6 ~ =$ $( ( 9 8 / 1 0 6 ) ^ { * } 0 . 2 7 8 1 ^ { * } ( 1 / 2 ) )$ ). For the influence from C1 to S5, the path length is k=2, so the TRS score $\mathrm { i s } - 0 . 0 0 7 7 = ( ( 3 / 4 ) ^ { \ast } ( - 0 . 0 4 4 6 ) ^ { \ast } ( 9 8 / 1 0 6 ) ^ { \ast } ( 1 / 2 ) ^ { 2 } )$ . In total, the path C1->R1->S5 has a TRS score of 0.1209 = (0.1286−0.0077) on product S5.

![](/api/attachments/HNEHPFBA/fulltext/images/0dc7e1b2810ad02f0ad1c01acbca3617bd0913abac7d0ef77f9332a6578b0709.jpg)

![](/api/attachments/HNEHPFBA/fulltext/images/1050e6deec87303f971e8edffc830548e54d5c0d3d10ca81f7b7c1af3307138d.jpg)  
Figure 2. An example

## 3.4 Proposed Hypotheses

## 3.4.1 Sentiment Analysis Provides Better WoM Measures Than Rating Scores

There is a growing volume of product reviews on the Web, which help customers make decisions. Customers post these reviews along with numerical ratings. Previous studies have determined that there is not always a clear and consistent relationship between the text of reviews and the ratings [42, 43]. That is, from a reader’s perspective, there is a discrepancy between what the reviewer expresses as the numerical rating and what he/she expresses in the text. Therefore, in this article, we aim at investigating the different effects of rating and text sentiment analyses on sales-prediction performance. Because textual contents contain richer information than rating scores, we posit the following:

H1: Sentiment analysis provides better WoM measures than rating scores.

## 3.4.2 Transitive Influence Between Products Affects Product WoM

Products have potential relationships. These relationships can be either complementary or substitutable. The representative complementary relationship is the brand affect. According to Chaudhuri and Holbrook [8], brand trust and brand affect combine to determine purchase loyalty, which in turn leads to greater market share or product sales. Specifically, brand-loyal consumers are willing to buy a particular product brand because they perceive some unique value in the brand that no alternative can provide [44]. The substitutable relationships often occur between products in the same category. From the consumer’s perspective, choosing products from one category is a noncomparable process [9]; that is, favoring a particular product often indicates that other products in the same category are less favored. Both relationships affect product sales. In this paper, we propose identifying product relationships based on customer reviews, in which products are often compared with each other. Given the product relationships, we further argue that product WoM is measured not only by the focal product but also by related products. Therefore, we propose the following:

H2: The transitive influence between products affects product WoM.

## 3.4.3 The Transitive Influence Between Customer Reviews Affects Product WoM

In social media environments, intercommunication occurs between users. As discussed in the background analysis, the sentiment of a post is affected not only by the sentiment of its immediate parent but also by its cascade [30]. Therefore, in this study, we use a social intercommunication structure and investigate the transitive influence of sentiment on customer reviews and replies.

H3: The transitive influence between customer reviews affects product WoM.

## 4. Model Development

## 4.1 Variables

Sales rank ( SR ): As in many other studies [10, 11, 37], sales rank is adopted as a parameter to measure the sales performance and popularity of products. Because we aim at testing the predictive power of different WoM measures on product sales, we adopt SR as the focused dependent variable for two reasons. First, sales rank is the only sales performance measure available in Amazon’s electronic market [11]. Second, sales rank is a proxy of demand according to earlier studies [45, 46], showing that sales rank has a Pareto distribution, that is, a power law. It is possible to convert the sales rank into demand levels using a linear function, $\ln ( D e m a n d ) =$

#

$a + b l n ( s a l e s \ r a n k )$ , where $a > 0$ and $b < 0$

Average rating $( A R )$ : Average rating is the average score of all reviewers’ ratings, and it is a highly compact summary of overall consumer opinions. It is a popular variable in WoM research.

Average sentiment ( AS ): Instead of using customer ratings to measure products’ WoM value, some studies have also adopted sentiment analysis to calculate a sentiment score from the review context. In this study, we apply the polarity value of a text to measure the WoM of a post.

Transitive rating (TR): According to the network influence theory proposed in this study, a node’s rating is influenced by its direct or indirect neighbors. Thus, we propose a transitive rating measure to evaluate products’ WoM in an entire market network.

Transitive sentiment in review network ( TRS ): In the review network, the sentiment of a reply influences a product’s WoM value through its directly linked review. When just considering the review network, we construct the transitive sentiment measure to evaluate products’ WoM value.

Two-layer Transitive Sentiment (TTS ): Similar to the transitive rating measure, we use the transitive sentiment in a product network to replace individual product’s average rating. Both the communication network effects and product network effects are incorporated in this measurement.

Other variables: Product price ( P ) plays an important role in influencing consumers decisions. Sales performance is sensitive to the price of a product, so the price should be one of the model’s variables.

Moreover, we collect other WoM measures used in previous studies [3, 33], including the number of reviews ( RN ), the review length $( R L )$ , the number of replies ( RPN ), and the reply length ( RPL ).

To mitigate the influence of unobservable variables, we introduce category dummies ( CD ) and time dummies (TD), similar to Duan et al. [47] and Li and Hitt [48]. We include category dummies because we assume that heterogeneous properties of product comparisons exist across different categories. In addition, time dummies help control some of the time variance, which can be a potential estimation bias. Given our dataset, we have three category dummies and nine time dummy variables.

## 4.2 Predictive Models

Given the above variables, we construct five predictive models (as shown in Table 5) with different variables. Following the work of Archak [10], our prediction task is as follows: Given the set of product reviews posted and other variables, such as the price during the last month, we predict (1) whether product sales (as measured by the sales rank) will increase or decrease within the next month and (2) what the precise product sales rank will be in the next month.

Table 5. Models and features.

<table><tr><td></td><td>Dependent variable</td><td>Independent variable</td></tr><tr><td>Model 1</td><td>SR</td><td>P, RN, RL, CD, TD, AR</td></tr><tr><td>Model 2</td><td>SR</td><td>P, RN, RL, CD, TD, AS</td></tr><tr><td>Model 3</td><td>SR</td><td>P, RN, RL, CD, TD, AR, TR</td></tr><tr><td>Model 4</td><td>SR</td><td>P, RN, RL, RPN, RPL, CD, TD, TRS</td></tr><tr><td>Model 5</td><td>SR</td><td>P, RN, RL, RPN, RPL, CD, TD, TRS, TTS</td></tr></table>

## 4.2.1 Regression Model

Following Chevalier and Mayzlin [4], we model the predictive power of product WoM regarding sales performance by directly incorporating product review information in a linear equation used to calculate the sales rank. We construct five different regression models to compare the different WoM measures. These linear regression models are built on panel data and use log transformation [10, 11] because of the broad dispersion of the variables’ values. The dependent variable is LogSalesRank in the current time period, and the independent variables are delayed by 1 month. We compare the performance of these models in terms of the root mean square error (RMSE):

Model 1:

$$
\begin{array}{r l} \operatorname{Log} \left(S R _ {i, t}\right) & = \alpha + \beta_ {1} A R _ {i, t - 1} + \beta_ {2} \operatorname{Log} \left(P _ {i, t - 1}\right) + \beta_ {3} \operatorname{Log} \left(R N _ {i, t - 1}\right) \\ & + \beta_ {4} \operatorname{Log} \left(R L _ {t, t - 1}\right) + \lambda_ {1} C D _ {i} + \lambda_ {2} T D _ {t} + \varepsilon_ {i, t} \end{array}
$$

Model 2:

$$
\begin{array}{r l} \operatorname{Log} \left(S R _ {i, t}\right) & = \alpha + \beta_ {1} A S _ {i, t - 1} + \beta_ {2} \operatorname{Log} \left(P _ {i, t - 1}\right) + \beta_ {3} \operatorname{Log} \left(R N _ {i, t - 1}\right) \\ & + \beta_ {4} \operatorname{Log} \left(R L _ {i, t - 1}\right) + \lambda_ {1} C D _ {i} + \lambda_ {2} T D _ {t} + \varepsilon_ {i, t} \end{array}
$$

Model 3:

$$
\begin{array}{r l} \operatorname{Log} \left(S R _ {i, t}\right) & = \alpha + \beta_ {1} A R _ {i, t - 1} + \beta_ {2} T R _ {i, t - 1} + \beta_ {3} \operatorname{Log} \left(P _ {i, t - 1}\right) + \beta_ {4} \operatorname{Log} \left(R N _ {i, t - 1}\right) \\ & + \beta_ {5} \operatorname{Log} \left(R L _ {i, t - 1}\right) + \lambda_ {1} C D _ {i} + \lambda_ {2} T D _ {t} + \varepsilon_ {i, t} \end{array}
$$

Model 4:

$$
\begin{array}{r l} \operatorname{Log} \left(S R _ {i, t}\right) & = \alpha + \beta_ {1} T R S _ {i, t - 1} + \beta_ {2} \operatorname{Log} \left(P _ {i, t - 1}\right) + \beta_ {3} \operatorname{Log} \left(R N _ {i, t - 1}\right) + \beta_ {4} \operatorname{Log} \left(R L _ {\hat {t}, t - 1}\right) \\ & + \beta_ {5} \operatorname{Log} \left(R P L _ {\hat {t}, t - 1}\right) + \beta_ {6} \operatorname{Log} \left(R P L _ {\hat {t}, t - 1}\right) + \lambda_ {1} C D _ {i} + \lambda_ {2} T D _ {t} + \varepsilon_ {i, t} \end{array}
$$

Model 5:

$$
\begin{array}{l} \operatorname{Log} \left(S R _ {i, t}\right) = \alpha + \beta_ {1} T R S _ {i, t - 1} + \beta_ {2} T T S _ {i, t - 1} + \beta_ {3} \operatorname{Log} \left(P _ {i, t - 1}\right) + \beta_ {4} \operatorname{Log} \left(R N _ {i, t - 1}\right) + \beta_ {5} \operatorname{Log} \left(R L _ {\hat {t}, t - 1}\right) \\ \quad + \beta_ {6} \operatorname{Log} \left(R P L _ {\hat {t}, t - 1}\right) + \beta_ {7} \operatorname{Log} \left(R P L _ {\hat {t}, t - 1}\right) + \lambda_ {1} C D _ {i} + \lambda_ {2} T D _ {t} + \varepsilon_ {i, t} \end{array}
$$

## 4.2.2 Classification Model

In the second task, we adopt a purely forecasting perspective and show different impacts of product WoM measures, predicting short-term future changes in the product’s sale performance [10]. The classification task is to forecast whether the product sales rank will go up or down within the next month. To do this, we predict the sign of the value SalesRank (t + 1) − ?????????????????? (??) at time t (measured in months).

We adopt widely accepted performance metrics – accuracy, precision, recall, and f-measure – for this classification task [49]. We annotate the number of correctly predicted sales increasing as TP, the number of correctly predicted sales decreasing as TN, the number of sales decreasing predicted as sales increasing as FP, the number of sales increasing as P, and the number of sales decreasing as N. Accuracy assesses the percentage of correct predictions among all predictions, say, (TP+TN)/(P+N). Precision is measured by TP/(TP+FP), and recall is measured by TP/P. They catch the correctness and coverage of prediction on sales increasing, respectively. The f-measure combines them for an overall assessment: F=2\*Precision\*Recall/(Precision+Recall).

To properly reflect a trade-off between precision and recall, metrics on binary classification are not enough. Thus, we report the receiver operating characteristic (ROC) curve, which captures the classifier’s dynamic performance. A ROC curve closer to the top-left corner indicates better dynamic performance. How close the ROC curve is to the top-left corner can be reflected in the area under curve (AUC) measure, which is also used as an evaluation metric in this paper.

## 5. Empirical Studies

## 5.1 Data Collection and Processing

#

The data were gathered from Amazon.com, a popular e-commerce platform, from January 2014 to October 2014. This website has a large consumer base and a large number of consumer reviews. The dataset contained four different product categories: charger, headset, clock, and GPS. These small electronic products are chosen because they are easy to replace, so the comparisons between products are very common. During the 10-month data collection period, we collected the daily price and sales rank information for the products, which included the collection date, product ID, and product title. Moreover, we collected the product review information, including the text of the review, the rating of the review, and the information in the replies. Each product review contains a numerical rating on a scale of one to five stars; the date the review was posted; the helpfulness rating, as voted by other consumers; and the entire text posted by the reviewer. We downloaded 10 months’ worth of data that were relevant to 555 products and corresponded to approximately 55,694 customer reviews and ratings. The product network was built using these reviews. Table 6 provides a brief summary of our data. Charger and headset products were found to have many more reviewers than clock and GPS products. This is because clock and GPS are durable products, and they are often shared in a family. Therefore, their buying frequency and comparisons are much lower than those of other products.

Table 6. Data summary statistics.

<table><tr><td colspan="2">Data summary</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td rowspan="4">Overall</td><td>Products</td><td>555</td><td>555</td><td>555</td><td>555</td><td>555</td><td>555</td><td>555</td><td>555</td><td>555</td><td>555</td></tr><tr><td>Reviews</td><td>5520</td><td>4558</td><td>4775</td><td>4381</td><td>4236</td><td>4535</td><td>7439</td><td>7337</td><td>6772</td><td>6141</td></tr><tr><td>Replies</td><td>466</td><td>377</td><td>453</td><td>381</td><td>343</td><td>469</td><td>492</td><td>462</td><td>420</td><td>317</td></tr><tr><td>Products in network</td><td>354</td><td>361</td><td>365</td><td>371</td><td>373</td><td>377</td><td>380</td><td>385</td><td>386</td><td>386</td></tr><tr><td rowspan="4">Category 1 (Charger)</td><td>Products</td><td>372</td><td>372</td><td>372</td><td>372</td><td>372</td><td>372</td><td>372</td><td>372</td><td>372</td><td>372</td></tr><tr><td>Reviews</td><td>3685</td><td>2947</td><td>3128</td><td>2779</td><td>2726</td><td>2937</td><td>4921</td><td>4951</td><td>4544</td><td>3997</td></tr><tr><td>Replies</td><td>287</td><td>197</td><td>293</td><td>204</td><td>206</td><td>282</td><td>322</td><td>337</td><td>306</td><td>254</td></tr><tr><td>Products in network</td><td>209</td><td>214</td><td>217</td><td>222</td><td>224</td><td>228</td><td>231</td><td>234</td><td>234</td><td>134</td></tr><tr><td rowspan="2">Category 2 (Headset)</td><td>Products</td><td>88</td><td>88</td><td>88</td><td>88</td><td>88</td><td>88</td><td>88</td><td>88</td><td>88</td><td>88</td></tr><tr><td>ReviewsReplies</td><td>141970</td><td>129786</td><td>129855</td><td>123880</td><td>113055</td><td>118445</td><td>190955</td><td>172845</td><td>166258</td><td>165232</td></tr><tr><td></td><td>Products in network</td><td>79</td><td>80</td><td>81</td><td>82</td><td>82</td><td>82</td><td>82</td><td>83</td><td>83</td><td>83</td></tr><tr><td rowspan="4">Category 3 (Clock)</td><td>Products</td><td>25</td><td>25</td><td>25</td><td>25</td><td>25</td><td>25</td><td>25</td><td>25</td><td>25</td><td>25</td></tr><tr><td>Reviews</td><td>76</td><td>61</td><td>68</td><td>53</td><td>49</td><td>59</td><td>73</td><td>73</td><td>59</td><td>61</td></tr><tr><td>Replies</td><td>5</td><td>6</td><td>2</td><td>5</td><td>2</td><td>2</td><td>3</td><td>5</td><td>9</td><td>1</td></tr><tr><td>Products in network</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td rowspan="4">Category 4 (GPS)</td><td>Products</td><td>70</td><td>70</td><td>70</td><td>70</td><td>70</td><td>70</td><td>70</td><td>70</td><td>70</td><td>70</td></tr><tr><td>Reviews</td><td>340</td><td>253</td><td>281</td><td>311</td><td>331</td><td>355</td><td>536</td><td>585</td><td>507</td><td>431</td></tr><tr><td>Replies</td><td>104</td><td>88</td><td>103</td><td>92</td><td>80</td><td>140</td><td>112</td><td>75</td><td>47</td><td>30</td></tr><tr><td>Products in network</td><td>63</td><td>63</td><td>63</td><td>63</td><td>63</td><td>63</td><td>63</td><td>64</td><td>65</td><td>65</td></tr></table>

The primary task of textual data processing is to identify comparison relationships between products. The first step is to match product names in customer reviews. As shown in Fig. 2, the product title is “Samsung Galaxy S5, Black 16 GB (Version Wireless) (Wireless Phone).” In accordance with the work of Zhang et al. [22], we identify the product by the first three words of the title. “Samsung” is a manufacturer-level entity, “Galaxy” is a series-level entity, and “S5” is a product-level entity. We give the product-level entity the highest priority, and we match it to a product name with the terms of product-level entity, product-level entity + series-level entity, and series-level entity + manufacture-level entity. In this way, we find a sentence that says, “Not bad in comparison to the S3 I had,” which mentions another Samsung Galaxy product, the “S3.”

## 5.2 Regression Results

The regression results are shown in Table 7, including the coefficients of the variables of interest, standard errors of estimation, and adjusted R squared values. The price, review numbers, and review length clearly influence the sales rank significantly (p<0.001) across all five models. This result is in agreement with previous studies [4, 10, 22]. In model 1, AvgRating, which measures the average rating stars, has a negative effect on LogSalesRank, but its coefficient is not significant. The finding was also observed in a previous work [22], and it shows that rating is not a good summary for WoM. In model 2, AvgSentiment, which measures the average polarity value, has a significant negative effect on LogSalesRank, indicating that products with a higher WoM

#

value are more likely to achieve good sales performance. In model 3, transitive rating, which measures the overall opinion of a product in a product network, has a significantly positive effect on LogSalesRank. It is notable that the positive effect indicates that a higher overall WoM value would cause worse sales performance. A possible explanation is that we add other products WoMs to the product of interest. In a competitive situation, if related products have poor WoMs, the focused product is positively affected. In model 4, transitive sentiment in review network, which measures the effects of reviews and replies, has a significantly negative influence on LogSalesRank, indicating that the product will gain better sales performance if its WoM value is higher. Moreover, in model 4, we consider additional information in replies (reply number and reply length), which is also significant. In model 5, the two-layer transitive sentiment, which measures the transitive sentiment influence of the review network and the product network, exerts a significantly positive effect on LogSalesRank. Similar to the transitive rating, the possible explanation for this positive effect is that this measure considers other products’ WoM values. Therefore, this measure describes a relative WoM considering potential competitive products.

Table 7. Results of linear regression models

<table><tr><td>Variable</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td></tr><tr><td>Intercept</td><td>9.491***(0.120)</td><td>9.403***(0.112)</td><td>9.543***(0.120)</td><td>8.973***(0.125)</td><td>8.971***(0.124)</td></tr><tr><td>Log Price</td><td>-0.108***(0.015)</td><td>-0.092***(0.015)</td><td>-0.103***(0.015)</td><td>-0.058***(0.016)</td><td>-0.043***(0.016)</td></tr><tr><td>Log NumReview</td><td>-0.299***(0.010)</td><td>-0.302***(0.010)</td><td>-0.318***(0.010)</td><td>-0.181***(0.017)</td><td>-0.182***(0.017)</td></tr><tr><td>Log ReviewLength</td><td>0.193***(0.031)</td><td>0.202***(0.030)</td><td>0.203***(0.031)</td><td>0.233***(0.030)</td><td>0.229***(0.030)</td></tr><tr><td>Log NumReply</td><td></td><td></td><td></td><td>-0.060**(0.019)</td><td>-0.062***(0.018)</td></tr><tr><td>Log ReplyLength</td><td></td><td></td><td></td><td>-0.085***(0.013)</td><td>-0.081***(0.013)</td></tr><tr><td>AvgRating</td><td>-0.032(0.021)</td><td></td><td>-0.041*(0.021)</td><td></td><td></td></tr><tr><td>AvgSentiment</td><td></td><td>-0.383***(0.086)</td><td></td><td></td><td></td></tr><tr><td>Transitive Rating</td><td></td><td></td><td>0.001***(0.0002)</td><td></td><td></td></tr></table>

##

<table><tr><td>Transitive</td><td></td><td></td><td></td><td>-0.001***</td><td>-0.002***</td></tr><tr><td>Sentiment in Review Network</td><td></td><td></td><td></td><td>(0.0003)</td><td>(0.0003)</td></tr><tr><td>Two-layer</td><td></td><td></td><td></td><td></td><td>0.0001***</td></tr><tr><td>Transitive Sentiment</td><td></td><td></td><td></td><td></td><td>(0.00002)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.202</td><td>0.204</td><td>0.208</td><td>0.213</td><td>0.222</td></tr><tr><td>N</td><td>5550</td><td>5550</td><td>5550</td><td>5550</td><td>5550</td></tr><tr><td colspan="6">Coefficients of category and time dummies are not reported. Significance level: *p&lt;0.1, **p&lt;0.01, ***p&lt;0.001</td></tr></table>

By comparing different models’ performances, we find that model 2 (adjusted $R ^ { 2 } = 0 . 2 0 4 )$ is better than model 1 (adjusted $R ^ { 2 } = 0 . 2 0 2 )$ , and model 5 (adjusted $R ^ { 2 } = 0 . 2 2 2 )$ outperforms model 3 (adjusted $R ^ { 2 } = 0 . 2 0 8 )$ ). It means the sentiment analysis of text provides a better indicator on WoM than counting the rating stars. Model 3 (adjusted $R ^ { 2 } = 0 . 2 0 8 )$ is better than model 1 (adjusted $R ^ { 2 } =$ 0.202), and model 5 shows a better performance in forecasting the sales rank than model 4 (adjusted $R ^ { 2 } = 0 . 2 2 2 ~ \mathrm { v s }$ . adjusted $R ^ { 2 } = 0 . 2 1 3 )$ . The results reflect that the influence between products exists, and it can affect the product WoM measurement. Moreover, we can conclude that the transitive influence in the review network provides a better measure than the sentiment analysis on a single review by comparing the performances of model 4 (adjusted $R ^ { 2 } = 0 . 2 1 3 )$ and model 2 (adjusted $R ^ { 2 } = 0 . 2 0 4 )$

To test the significance of these reports, we remove 1 month of data and create a predictive model with the remaining data. By using the out-of-sample data, we compare the performances of these models statistically in terms of the RMSE. As presented in Table 8, the RMSE of model 2 is significantly smaller than that in model 1 (1.114<1.116, p<0.0001). Model 5 shows much better predictive power for sales rank with an average RMSE of 1.101, outperforming model 3, which has an average RMSE of 1.111 (T=48.258, p<0.0001). These two results strongly support H1; that is, that sentiment polarity provides better WoM measure than rating scores. Furthermore, to test H2, we find that the average RMSE value of model 3 is significantly smaller than that of model 1 (1.111<1.116, p<0.0001). Furthermore, model 4 performs much worse than model 5 (RMSE $1 . 1 0 7 { > } 1 . 1 0 1 )$ , and the paired t-test shows a significant difference (T=40.417, p<0.0001). Thus, H2 is well supported. Moreover, comparing the results of model 4 and model 2 (RMSE 1.107<1.114) significantly (T=41.243, p<0.0001) supports H3 (i.e., the transitive influence between customer

reviews affects product WoM).

Table 8. Results of predictive modeling in RMSE

<table><tr><td>Month</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td></tr><tr><td>overall</td><td>1.116</td><td>1.114</td><td>1.111</td><td>1.108</td><td>1.101</td></tr><tr><td>1</td><td>1.111</td><td>1.109</td><td>1.106</td><td>1.103</td><td>1.096</td></tr><tr><td>2</td><td>1.117</td><td>1.115</td><td>1.112</td><td>1.109</td><td>1.103</td></tr><tr><td>3</td><td>1.117</td><td>1.115</td><td>1.113</td><td>1.109</td><td>1.102</td></tr><tr><td>4</td><td>1.119</td><td>1.117</td><td>1.114</td><td>1.111</td><td>1.104</td></tr><tr><td>5</td><td>1.118</td><td>1.116</td><td>1.114</td><td>1.110</td><td>1.103</td></tr><tr><td>6</td><td>1.111</td><td>1.109</td><td>1.107</td><td>1.103</td><td>1.096</td></tr><tr><td>7</td><td>1.114</td><td>1.113</td><td>1.110</td><td>1.106</td><td>1.099</td></tr><tr><td>8</td><td>1.119</td><td>1.117</td><td>1.114</td><td>1.110</td><td>1.104</td></tr><tr><td>9</td><td>1.112</td><td>1.111</td><td>1.108</td><td>1.104</td><td>1.098</td></tr><tr><td>10</td><td>1.119</td><td>1.117</td><td>1.115</td><td>1.111</td><td>1.105</td></tr><tr><td>means</td><td>1.116</td><td>1.114</td><td>1.111</td><td>1.107</td><td>1.101</td></tr><tr><td colspan="6">Paired t-test</td></tr><tr><td rowspan="2" colspan="2">H1</td><td colspan="2">Model 2 &lt; Model 1</td><td colspan="2">13.500***</td></tr><tr><td colspan="2">Model 5 &lt; Model 3</td><td colspan="2">48.258***</td></tr><tr><td rowspan="2" colspan="2">H2</td><td colspan="2">Model 3 &lt; Model 1</td><td colspan="2">26.944***</td></tr><tr><td colspan="2">Model 5 &lt; Model 4</td><td colspan="2">40.417***</td></tr><tr><td colspan="2">H3</td><td colspan="2">Model 4 &lt; Model 2</td><td colspan="2">41.243***</td></tr></table>

\*\*\* $p { < } 0 . 0 0 1$

## 5.3 Classification Results

We experiment with four different classifier types: logistic regression, support vector machines, decision trees, and random forests. Because the decision tree outperforms (8–10% according to the f-measure) the other classifiers, we report the results using this classifier type. It should be noted that the classification accuracy is not very high because we consider only WoM and price features in the predictive models. However, compared with the previous classification results (the AUC ranges from 0.544 to 0.644) of [10], who build sales predictive models with product features, our results are acceptable.

Table 9. Predictive accuracy for the sales-rank classifier

<table><tr><td>Model</td><td>Precision</td><td>Recall</td><td>f-measure</td><td>AUC</td></tr><tr><td>Model 1</td><td>0.564</td><td>0.793</td><td>0.659</td><td>0.625</td></tr><tr><td>Model 2</td><td>0.563</td><td>0.805</td><td>0.663</td><td>0.663</td></tr><tr><td>Model 3</td><td>0.564</td><td>0.794</td><td>0.660</td><td>0.626</td></tr><tr><td>Model 4</td><td>0.559</td><td>0.825</td><td>0.666</td><td>0.663</td></tr><tr><td>Model 5</td><td>0.558</td><td>0.841</td><td>0.671</td><td>0.664</td></tr><tr><td colspan="5">Paired t-test on f-measure</td></tr></table>

<table><tr><td rowspan="2">H1</td><td>Model 2&gt; Model 1</td><td>2.174**</td></tr><tr><td>Model 5&gt; Model 3</td><td>1.254</td></tr><tr><td rowspan="2">H2</td><td>Model 3&gt; Model 1</td><td>-0.949</td></tr><tr><td>Model 5&gt; Model 4</td><td>2.986*</td></tr><tr><td>H3</td><td>Model 4&gt; Model 2</td><td>1.395</td></tr></table>

Note: \* p<0.1, \*\* p<0.05

Table 9 reports the results of 30 rounds of 10-fold cross validations [50] based on classification performance metrics. According to the average values, we find that model 2 has larger values (0.663 and 0.663) than model 1 (0.659 and 0.625). The paired t-test on the f-measure is significant (p=0.038) at the 0.05 level. Furthermore, model 5 (0.671 and 0.664) is better than model 3 (0.660 and 0.626) in terms of both the f-measure and AUC metrics. However, the t-test is not significant (p=0.220). Therefore, H1, that is, sentiment analysis that provides better WoM measure than rating scores, is partially supported. To test H2, we compare model 3 versus model 1 and model 5 versus model 4. Model 3 (0.660 and 0.626) is slightly better than model 1 (0.659 and 0.625) in terms of both the f-measure and AUC metrics. However, the t-test is not significant (p=0.351). Model 5 (0.671 and 0.664) is better than model 4 (0.666 and 0.663), and the t-test is significant at the 0.01 level (p=0.006). Therefore, H2 is partially supported. We then compare model 4 and model 2 to test H3. We find that model 4 (0.666 and 0.663) is better than model 2 (0.663 and 0.663) in terms of the f-measure and AUC metrics, but the t-test is not significant (p=0.174). Therefore, H3 is not well supported.

Figure 3 shows the ROC curves for model 1 and model 5. It is clear that using the two-layer transitive measures for WoM provides much better predictive power than using single-product rating scores, and the AUC improves from 0.625 to 0.664.

![](/api/attachments/HNEHPFBA/fulltext/images/190fcb8d92c0de56c08300c8602fdd2a56410d05f56d53d7c48a736f6af7ac8a.jpg)  
Figure 3. ROC curves for model 1 and model 5

## 6. Discussion and Conclusion

## 6.1 Major Findings

This study aims at investigating transitive influence effects on WoM in a two-layer network. The underlying customer communication network is useful for summarizing a comprehensive opinion from discussions among customers. The product network is then used to measure product-comparative relations and WoM influences. The work is thus a combinational innovation of collective sentiment analysis and market structure analysis. Through the experiments, we have the following major findings.

First, it is notable that in the prediction coefficient values on different WoM constructs have different signs. The average rating, average sentiment, and transitive sentiment have negative coefficient values in the regression model. It means a good product WoM, which is measured in an individual product, indicates good sales. Conversely, the constructs of transitive rating and two-layer transitive sentiment have positive coefficient values. It means a good product WoM, which is measured in a competitive market structure, often indicates bad sales. This finding is totally different from previous studies on WoM and sales. Subsequently, when using different WoM constructs to make decisions about sales, they may lead to totally different conclusions.

Second, the experiments illustrate that incorporating influence factors in both sentiment analysis and WoM measurement can improve the sales prediction power. In regression models, when controlling other sales-related factors in the same manner, using the two-layer sentiment measure can improve the model’s adjusted $R ^ { 2 }$ by about 2% compared with using the traditional average rating measure. Although the absolute number on improvement is not very large, it has significant economic meanings. In monetary terms, if the sales income is 100,000 dollars this month, the different measures would cause a 2000-dollar difference in stock for the next month’s sales.

Third, for general prediction on sales increase or decrease, the new influential WoM constructs demonstrate a slight improvement compared with average measures, that is, average rating and average sentiment. A possible reason is that the market structure is rather stable, so a small change in influential WoM features hardly predicts the increase or decrease of sales. However, experiments have shown that the influential WoM measures predict well the sales change in regression models.

These findings also provide important and novel implications for both research and management.

## 6.2 Theoretical Contributions

This study contributes to the social influence and marketing literature in several ways. First, it contributes to the social influence research by introducing a new transitive influence assessment method. The method provides a way to directly calculate the influential effects on nodes, thus reflecting on both the node attributes and network structures. Social influence theory suggests that people’s emotions, opinions, and behaviors are affected by others [12]. Therefore, previous studies on social influence have focused primarily on friendship networks [38, 51, 52] and studies on measured influences have focused on network structures [38, 53]. By contrast, in this study, we propose a novel network that is built using product relationships and intercommunication relationships. In these networks, nodes are objective entities (e.g., product or review). To measure the influential effects on nodes, we propose a transitive influence assessment method. The proposed method is useful in measuring node attributes and their influences in various networks.

Second, this study gives a new method to measure product WoM from a market structure perspective, thus improving its prediction power on sales. Previous works in the literature focus on a single-product-based WoM measurement [6, 10, 34], but have paid little attention to the potential influences between comparative products. This study aims at exploring and measuring the influences between products. Some novel features are found through experiments. Hence, the work indicates a new decision support research stream that incorporates the market structure and

inter-product influences.

Finally, it contributes to the sentiment analysis studies to catch a collective opinion, especially in the social media environment. Although text mining and sentiment analysis techniques have been used to analyze online customer reviews for a long time [1, 25–27, 43], text mining is still not adequate for catching a comprehensive understanding of opinions in a conversation situation. This study uses the intercommunication structure and proposes a method for collective sentiment analysis. It can be applied in various sentiment analysis tasks.

## 6.3 Managerial Implications

This study contributes to managerial strategies by providing tools and suggestions. First, the product-comparative network yields a good visualization tool for business intelligence, typically in a coherent product category section. It helps in decision-making on product development and on purchase for managers and customers. As shown in Fig. 4, product “B000CSQJ8C” is a GPS product within the “Garmin” brand. We can easily identify its related products using the graphical visualization – that most related products are other series of GPS products within the “Garmin” brand (e.g., “B000CSWCQA,” B000EXS1BS,” and “B001ELJ9QK”). We also find that some other GPS products within the “TomTom” and “Magellan” brands are linked (e.g., “B000SATCUQ” and “B007CRWQ0Q”), but with a smaller weight (a thinner link). Therefore, managers can learn about how many products in the same brand are related and which products are competitors in other brands. It is helpful to managers making decisions on new product design and marketing strategies, leading to competitive advantage [54]. As for customers, the graphical visualization provides a tool to compare and pick up products.

![](/api/attachments/HNEHPFBA/fulltext/images/f203b6d1a831d2ff647d6e90233cbe65ab0ff24e9de65b7318ab40ea62acbf46.jpg)  
Figure 4. A visualization example

Second, the work provides practical tools for WoM monitoring. Our findings indicate that not only the focused products’ reviews but also related products’ reviews can affect product sales. Thus, the range of WoM monitoring is enlarged and the market structure is emphasized. Given the large number of customer reviews posted online every day, WoM monitoring is laborious. Currently, the most popular method is to collect rating stars, because it is easy to access and measure. However, the rating method provides a less accurate value as proven in the study. In this regard, our research provides a new set of advanced WoM monitoring methods and algorithms, including product relationship identification, collective sentiment analysis, and WoM influence measurement.

Last but not least, the proposed WoM measure is especially helpful in preventing WoM manipulation or fraud. In e-commerce platforms, many shop owners hire some people to write positive comments and give high rating scores. By studying book reviews on Amazon, Hu et al. [55] estimate that about 10% of the books are subject to manipulated reviews. In traditional methods, these fake reviews are hardly identified and often contribute much to the WoM value [6]. In our method, we reduce the fake review influence by evaluating both the focal product review and other related products’ reviews. Moreover, we consider the intercommunications between customers. Even if a fake comment is posted, its replies might tell the truth. Therefore, employing the proposed WoM measure can help managers and customers get a more accurate evaluation on products.

## 6.4 Limitations and Future Research

Nevertheless, this study has several limitations that present opportunities for future research. First, this study uses only 555 products in four electronic product categories as subjects in experiments. The number of products in each category is small. The small number of products leads to the identification of only a few of comparative relations. Therefore, the product transitive influence might not be well emphasized. Second, the four product categories are all in electronics, so the study does not reveal the category feature of products on WoM influence. Third, this study only compares the influential WoM constructs and traditional WoM variables. From a network perspective, the network structure’s parameters, that is, centrality, degree, PageRank, and HITS, are other possible variables that should be investigated and compared in the future.

#

## Biographies

Kun Chen is an assistant professor in the Department of Financial Mathematics and Financial Engineering at South University of Science and Technology of China. She received her Ph.D. from the Department of Information Systems at the City University of Hong Kong. Dr. Chen’s research deals with business intelligence, text mining, and big data analytics. She has published in academic journals such as INFORMS Journal on Computing, Journal of Management Information Systems, and Information and Management.

Peng Luo is a Ph.D. student in Harbin Institute of Technology. His research focuses on network topology and social networks. Mr. Luo has published in academic journals such as Physica A, Journal of Informetrics, and Management Decisions.

Huaiqing Wang is a professor in the Department of Financial Mathematics and Financial Engineering at South University of Science and Technology of China. He is also the honorary dean and a guest professor of the School of Information Engineering, Wuhan University of Technology, China. He received his Ph.D. from University of Manchester, UK, in 1987. Dr. Wang specializes in research on financial Intelligence and intelligent systems (such as intelligent financial systems, intelligent learning systems, business process management systems, knowledge management systems, conceptual modeling, and ontology). He has published more than 70 international refereed SCI/SSCI journal articles and received more than 700 SCI citations.

## References

1. Yang, C., et al., Understanding online consumer review opinion with sentiment analysis using machine learning. Pacific Asia Journal of the Association for Information Systems, 2010. 2(3): p. 73-89.

2. Lee, J., J.-N. Lee, and H. Shin, The long tail or the short tail: The category-specific impact of eWOM on sales distribution. Decision support systems, 2011. 51(3): p. 466-479.

3. Mudambi, S.M. and D. Schuff, What makes a helpful online review? A study of customer reviews on Amazon.com. MIS Quarterly, 2010. 34(1): p. 185-200.

4. Chevalier, J.A. and D. Mayzlin, The effect of word of mouth on sales: Online book reviews. Journal of Market Research, 2006. 43(3): p. 345-354.

5. Chintagunta, P., S. Gopinath, and S. Venkataraman, The effects of online user reviews on movie box office performance: Accounting for sequential rollout and aggregation across local markets. Market Science, 2010. 29(5): p. 944-957.

6. Trenz, M. and B. Berger. Analyzing online customer reviews - An interdisciplinary literature review and research agenda. in European Conference on Information Systems. 2013. Utrecht, The Netherlands: AIS.

7. Akiva, N., et al. Mining and visualizing online Web content using BAM: Brand association map. in Second International Conference of Weblogs Social Media. 2008.

8. Chaudhuri, A. and M.B. Holbrook, The chain of effects from brand trust and brand affect to brand performance: The role of brand loyalty. Journal of Marketing, 2001. 65(2): p. 81-93.

9. Johnson, M.D., The Differential Processing of Product Category and Noncomparable Choice Alternatives. Journal of Consumer Research, 1989. 16(3): p. 300-309.

10. Archak, N., A. Ghose, and P. Ipeirotis, Deriving the pricing power of product features by mining consumer reviews. Management Science, 2011. 57(8): p. 1485-1509.

11. Zhang, Z., X. Li, and Y. Chen, Deciphering word-of-mouth in social media: Text-based metrics of consumer reviews. ACM Transactions on Management Information Systems (TMIS), 2012. 3(1): p. 5.

12. Deutsch, M. and H.B. Gerard, A study of normative and informational social influences upon individual judgement. The Journal of Abnormal and Social Psychology, 1955. 51(3): p. 629-636.

13. Yan, Z., et al., EXPRS: An extended pagerank method for product feature extraction from online consumer reviews. Information & Managment, 2015. 52: p. 850-858.

14. Henderson, G.R., D. Iacobucci, and B.J. Calder, Brand diagnostics: mapping branding effects using consumer associative networks. European Journal of Operational Research, 1998. 111(2): p. 306-327.

15. Anderson, J.R. and G.H. Bower, Human associative memory. 1973: Psychology press.

16. He, Q., Knowledge Discovery Through Co-Word Analysis. Library trends, 1999. 48(1): p. 133-59.

17. Netzer, O., et al., Mine your own business: Market structure surveillance through text mining. Market Science, 2012. 31(3): p. 521-543.

18. Lee, T. and E. Bradlow, Automated marketing research using online customer reviews. Journa of Market Research, 2011. 48(5): p. 881-894.

19. Jindal, N. and B. Liu. Identifying comparative sentences in text documents. in Proceedings of the 29th annual international ACM SIGIR conference on Research and development in information retrieval. 2006. ACM.

20. Jindal, N. and B. Liu. Mining comparative sentences and relations. in AAAI. 2006.

21. Xu, K., et al., Mining comparative opinions from customer reviews for Competitive Intelligence. Decision support systems, 2011. 50(4): p. 743-754.

22. Zhang, Z., C. Guo, and P. Goes, Product comparison networks for competitive analysis of online word-of-mouth. ACM Transactions on Management Information Systems (TMIS), 2013. 3(4): p. 20:1-20:22.

23. Baccianella, S., A. Esuli, and F. Sebastiani, SentiWordNet3.0: An enhanced lexical resource for sentiment analysis and opinion mining, in International Conference on Language Resources and Evaluation. 2010: Valletta, Malta. p. 2200-2204.

24. Nokelainen, T. and O. Dedehayir, Technological adoption and use after mass market displacement: The case of the LP record. Technovation, 2015. 36: p. 65-76.

25. Hamouda, A. and M. Rohaim, Reviews classification using sentiwordnet lexicon. The Online Journal on Computer Science and Information Technology, 2011. 2(1): p. 120-123.

26. Pang, B. and L. Lee, Opinion mining and sentiment analysis. Foundations and Trends in Information Retrieval, 2008. 2(1-2): p. 1-135.

27. Thelwall, M., et al., Sentiment strength detection in short informal text. Journal of American Society for Information Science and Technology, 2010. 61(12): p. 2544-2558.

28. Li, Q., et al., User comments for news recommendation in forum-based social media. Information Sciences, 2010. 180: p. 4929-4939.

29. Zhang, Z., Weighting stars: Aggregating online product reviews for intelligent e-commerce applications. IEEE Intelligent Systems, 2008. September-October: p. 42-49.

30. Miller, M., et al. Sentiment flow through hyperlink networks. in the Fifth International AAA Conference on Weblogs and Social media. 2011.

31. Tan, C., et al. User-level sentiment analysis incorporating social networks. in the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 2011.

32. Hyrynsalmi, S., et al., Busting myths of electronic word of mouth: the relationship between customer ratings and the sales of mobile applications. Journal of theoretical and applied electronic commerce research, 2015. 10(2): p. 1-18.

33. Godes, D. and D. Mayzlin, Using online conversations to study word-of-mouth communication. Marketing Science, 2004. 23(4): p. 545-560.

34. Liu, Y., Word-of-mouth for movies: Its dynamics and impact on box office revenue. Journal of Marketing, 2006. 70(3): p. 74-89.

35. Filieri, R., What makes online reviews helpful? A diagnosticity-adoption framework to explain informational and normative influences in e-WOM. Journal of Business Research, 2015. 68: p. 1261-1270.

36. Jeong, H.J. and D.M. Koo, Combined effects of valence and attributes of e-WOM on consumer for message and product: The moderating effect of brand community type. Internet Research, 2015. 25(1): p. 2-29.

37. Ghose, A. and P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions on Knowledge and Data Engineering, 2011. 23(10): p. 1498-1512.

38. Lewis, K., M. Gonzalez, and J. Kaufman, Social selection and peer influence in an online social network. Proceedings of the National Academy of Sciences, 2012. 109(1): p. 68-72.

39. Neaigus, A., et al., Transitions to injecting drug use among noninjecting heroin users: social network influence and individual susceptibility. Journal of Acquired Immune Deficiency Syndromes, 2006. 41(4): p. 493-503.

40. Pescosolido, B.A. and C.A. Boyer, How do people come to use mental health services? Current knowledge and changing perspectives, in A handbook for the study of mental health: Social context, theories, and systems, A.V. Horwitz and T.L. Scheid, Editors. 1999, Cambridge University Press: New York. p. 392-411.

41. Ballester, C., A. Calvo-Armengol, and Y. Zenou, Who's who in networks. wanted: the key player. Econometrica, 2006. 74(5): p. 1403-1417.

42. Carrillo de Albornoza, J., L. Plaza, and A. Diaz. A joint model for feature mining and sentiment analysis for product review rating. in The 33rd European Conference on Information Retrieval. 2011. Dublin, Ireland.

43. Maks, I. and P. Vossen. Sentiment analysis of reviews: Should we analyze writer intentions or reader perceptions? in Recent Advances in Nature Language Processing. 2013. Hissar, Bulgaria.

44. Pessemier, E.A., A new way to determine buying decisions. Journal of Marketing, 1959. 24(October): p. 41-46.

45. Brynjolfsson, E., Y. Hu, and M.D. Smith, Consumer surplus in the digital economy: Estimating the value of increased product variety at online booksellers. Management Science, 2003. 49(11): p. 1580-1596.

46. Chevalier, J. and A. Goolsbee, Measuring prices and price competition online: Amazon. com and BarnesandNoble. com. Quantitative marketing and Economics, 2003. 1(2): p. 203-222.

47. Duan, W., B. Gu, and A.B. Whinston, Do online reviews matter? - An empirical investigation of panel data. Decision Support Systems, 2008. 45(4): p. 1007-1016.

48. Li, X. and L.M. Hitt, Price effects in online product reviews: an analytical model and empirical analysis. MIS Quarterly, 2010. 34(4): p. 809-831.

49. Li, X., et al., A commonsense knowledge-enabled textual analysis approach for financia market surveillance. INFORMS Journal on Computing, 2016. 28(2): p. 278-294.

50. Kohavi, R. A study of cross-validation and bootstrap for accuracy estimation and model selection. in the 14th International Joint Conference on Artificial Intelligence. 1995.

51. Kwon, K.H., M.A. Stefanone, and G.A. Barnett, Social network influence on online behavioral choices exploring group formation on social network sites. American Behavioral Scientist, 2014. 58(10): p. 1345-1360.

52. Shoham, D.A., et al., An actor-based model of social network influence on adolescent body size, screen time, and playing sports. PloS one, 2012. 7(6).

53. Iyengar, R., S. Han, and S. Gupta, Do friends influence purchases in a social network? 2009, Harvard Business School Marketing Unit Working Paper.

54. Poter, M.E., The competitive advantage: Creating and sustaining superior performance. 1985, New York: Free Press.

55. Hu, N., et al., Manipulation of online reviews: An analysis of ratings, readability, and sentiments. Decision support systems, 2012. 52(3): p. 674-684.
