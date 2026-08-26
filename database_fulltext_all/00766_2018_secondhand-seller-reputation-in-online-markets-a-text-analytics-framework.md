---
otero_id: 766
otero_key: "AKFV27TH"
title: "Secondhand seller reputation in online markets: A text analytics framework"
authors: "Runyu Chen; Yitong Zheng; Wei Xu; Minghao Liu; Jiayue Wang"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.02.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Secondhand seller reputation in online markets: A text analytics framework

![](/api/attachments/AKFV27TH/fulltext/images/071d57fb12adb256c0ff0963054e0d44c436e8dc1f449e136afa3e9b9d083fae.jpg)

Runyu Chen, Yitong Zheng, Wei Xu, Minghao Liu, Jiayue Wang

<table><tr><td>PII:</td><td>S0167-9236(18)30037-X</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.02.008</td></tr><tr><td>Reference:</td><td>DECSUP 12934</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>1 July 2017</td></tr><tr><td>Revised date:</td><td>9 December 2017</td></tr><tr><td>Accepted date:</td><td>20 February 2018</td></tr></table>

Please cite this article as: Runyu Chen, Yitong Zheng, Wei Xu, Minghao Liu, Jiayue Wang , Secondhand seller reputation in online markets: A text analytics framework. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi:10.1016/j.dss.2018.02.008

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Secondhand seller reputation in online markets: A text analytics framework

Runyu CHEN<sup>a</sup>, Yitong ZHENG<sup>a</sup>, Wei XU<sup>a,</sup> <sup>b,</sup>, Minghao LIU<sup>a</sup>, Jiayue WANG<sup>a</sup>

School of Information, Renmin University of China, Beijing, 100872, P.R. China

<sup>b</sup>Smart City Research Center, Renmin University of China, Beijing, 100872, P.R. China

Abstract: With the rapid development of e-commerce, a new type of secondhand e-commerce website has appeared in recent years. Any user can have his or her own shop and list superfluous items for sale online without much supervision. These secondhand e-commerce platforms maximize the economic value of secondhand markets online, but buyers risk conducting unpleasant transactions with low-reputation sellers. The main of a text analytics framework to assess secondhand sellers’ reputation. In addition, we develop a new aspect-extraction method that combines the results of domain ontology and topic modeling to extract topical features from product descriptions. We conduct our experiments based on a real-word dataset crawled from XianYu. The experimental results reveal that our ontology-based topic model method outperforms a traditional topic model method. Furthermore, the proposed framework performs well in different item categories. The managerial implication of our research is that potential buyers can prejudge the reputation of secondhand sellers when making purchase decisions. The results can support a more effective development of online secondhand markets.

Keywords: Secondhand E-commerce, Reputation Assessment, Text Analytics, Aspect Extraction

## 1. Introduction

Secondhand trading occurs when people sell used things to others. Transaction prices are usually lower for secondhand products than for firsthand products, so buyers can obtain what they want at a lower price. Secondhand markets make full use of social resources and even stretch global production networks [1, 2]. Due to their great economic value, many studies have examined secondhand markets over the past 20 years [3, 4, 5]. The pricing problem in secondhand markets [6, 7] and the motivations for buying secondhand commodities [8, 9] are the most common topics examined in the related research.

With the rapid development of e-commerce, several secondhand e-commerce websites have been launched. One type of secondhand e-commerce website is an auction website (e.g., eBay<sup>1</sup>). On such websites, sellers list their commodities, and buyers bid on them. The platforms try to guarantee the reliability of both the sellers and the descriptions of their commodities. Rational buyers mainly focus on the gap between their expected price and other bids. In recent years, a new type of secondhand e-commerce website has appeared (e.g., XianYu<sup>2</sup>). On such websites, any seller can have his or her own shop without a complex shop-opening process. Sellers provide descriptions and prices for their commodities autonomously, and buyers can chat with sellers online and then decide whether to buy their products. In our view, this type of secondhand e-commerce website maximizes the economic value of secondhand markets online. Any seller can put superfluous items online for sale without much supervision.

In contrast with traditional e-commerce websites, secondhand e-commerce platforms are still in a preliminary stage of development. In China, on most platforms, buyers do not have the right to reasonably return products they have purchased. Furthermore, on these online secondhand platforms, most product descriptions are subjective and written by the seller. Crucial aspects such as the item condition can significantly influence the actual value of a product, but effective evidence regarding the item condition is lacking. Although secondhand auction websites such as eBay provide solutions to these problems, some new types of XianYu) have an entirely different business if the buyer faces a low-reputation seller. Therefore, evaluating the reputation of an online

Previous studies have proposed a set of determinants of perceived seller reputation. From the buyer’s perspective, one study found that the longer a seller’s transaction history, the greater the buyer’s willingness to pay [10]. Additionally, consumers evaluate sellers’ reliability by gathering information from social communities [11]. However, most related studies are based on eBay, in which secondhand transactions are performed as auctions. New-type secondhand e-commerce websites (e.g., XianYu) allow sellers to autonomously determine the price. This mechanism is more convenient and time-saving than that of longer-established websites, but it also presents new challenges to identify sellers’ reputation. Our research aims to fill the aforementioned research gaps.

The information obtained by buyers to judge product quality is called a signal, according to signaling theory [12]. Related works based on this theory have focused on the signals extracted from sellers’ homepage and product information [13-16]. Buyers’ perceived risk is lower if more valuable information is provided, and they are thus more likely to complete a satisfactory bargain. One novelty of our research is that we combine textual features with numerical features extracted from both seller-level and product-level information signals, which enhances the performance of online secondhand sellers’ reputation assessment. Some data sources (original price, current price, product description and online messages) in new-type secondhand e-commerce sites are distinct from those in traditional e-commerce. On secondhand e-commerce websites such as XianYu, buyers can ask questions on a specific product’s page and leave comments on the seller’s homepage after making a purchase. As public responses are an effective reputation management strategy [17], we extract shallow textual features from online messages, including the number of online messages and the reply rate (the number of replies/messages). Moreover, in order to mine embedded textual signals, we propose a new aspect-extraction method that combines the results of domain ontology and topic modeling to extract deep textual features from product descriptions.

In sum, our study establishes a reputation assessment model for suit-dress sellers on the popular Chinese secondhand e-commerce website XianYu (2.taobao.com). Our research makes three main contributions. First, we design a novel text analytics framework to assess

# ACCEPTED MANUSCRIPT

secondhand e-commerce sellers’ reputation. Second, we develop a new aspect-extraction method that combines the domain ontology and topic modeling results to extract deep textual features from product descriptions. Finally, we perform an empirical analysis to identify the discriminatory features that reveal secondhand sellers’ reputation based on a real-world secondhand e-commerce website. To the best of our knowledge, this is the first study to apply text analytics to assess sellers’ reputation on new-type secondhand e-commerce websites. The managerial implications of our research are as follows. With the help with our reputation assessment model, buyers can refer to online secondhand sellers’ reputation when making purchase decisions. Furthermore, secondhand e-commerce platforms can provide risk warnings or restrict the selling of low-reputation sellers. This study can support the more effective development of online secondhand markets.

The rest of this paper is organized as follows. Section 2 summarizes previous studies related to secondhand markets and sellers’ reputation. Section 3 describes the proposed text analytics framework for assessing secondhand sellers’ reputation. In Section 4, the computational details of the proposed methodology are illustrated. Section 5 contains a discussion of our experiment and our experimental results. The last section presents concluding remarks and the future directions of our research.

## 2. Related Work

## 2.1. An Overview of Secondhand Markets

Secondhand markets have received considerable attention over the past 20 years. Early research mainly focused on huge secondhand items, such as ships [18, 19]. Later studies examined smaller commodities, such as clothes [2] and luxury items [20]. The research problems examined by most of the existing research include the prices of secondhand goods [3, 6, 7] and the motivation for buying them [8, 9].

To study price discrimination in secondhand markets, Stroeker and Antonides [3] proposed a model to empirically estimate predicted negotiated prices based on reservation prices and the corresponding probability of reaching an agreement, as perceived by potential buyers and sellers. Berg [6] analyzed the structural differences and price dynamics on the secondhand market for Swedish family houses. He found that the real price changes in house prices for different regions displayed a high degree of autocorrelation, and the correlation revealed a mean-reverting pattern. Shafiee and Chukova [7] proposed an optimization model for upgrading warranty policies and sale prices. The model aimed to maximize the dealer’s profit. To study the motivations for buying secondhand commodities, Guiot and Roux [8] proposed a reliable, valid, eight-factor scale of secondhand shopping motivations that includes motivations related to products and distribution channels. Yan et al. [9] interviewed 152 college students to examine the differences between secondhand shoppers and non-shoppers with regard to psychographic variables. The results showed that compared with those who did not shop at secondhand clothing stores, college students who shopped at secondhand clothing stores were more likely to be environmentally conscious, more sensitive to higher prices, and more likely to wear used clothing for a vintage look.

Other studies have examined other topics related to secondhand markets. Thomas [19] explained that the growth of secondhand markets has reduced the demand for new goods.

Kogan [4] considered a supply chain that provides services for both new and secondhand goods. Interaction with the secondhand market and the profits of the supply chain have been well studied. Diverging from these related works, our study focuses on online secondhand markets, which have been developed in recent years but have not been well studied. As a combination of traditional secondhand markets and e-commerce, online secondhand markets are of great research value.

## 2.2. Seller Reputation Assessment

In consumer-to-consumer (C2C) e-commerce markets, buyers and sellers may have insufficient information about their counterparts [21, 22]. For example, buyers may pay for high-quality products but receive relatively low-quality ones. Fortunately, most e-commerce websites have set up efficient regulations to solve this problem [23]. For example, a buyer can return a purchase within seven days without providing a reason.

Even if a buyer can return purchased goods to sellers, the number of bad trades is a significant issue. A similar problem is observed in traditional e-commerce research studies: A seller’s reputation indicates the degree of approbation [24]. Reputation is formed by others perception of an individual’s personality, trustworthiness or other qualities and by their esteem for the individual based on direct or indirect interactions [25]. Reputation is vital in various fields, especially in business activity [24]. Sellers who have a good reputation attract more buyers, and sellers’ reputation improves as more buyers buy their products [26].

Many e-commerce websites have applied reputation mechanisms to provide information about sellers’ reputations. To enhance their reputations, some fraudulent sellers record artificial positive feedback [27]. Therefore, correctly evaluating a seller’s reputation is a challenge. Standifird [28] explored the impact and nature of reputation on e-commerce websites by looking at the influence of a seller’s reputational rating on the final bid prices in eBay auctions. He found strong evidence for the importance of reputation when engaging in e-commerce and equally strong evidence concerning the exaggerated influence of a negative reputation. Zhang et al. [29] analyzed the sentiments of online reviews in relation to sellers reputations. Acampora et al. [30] presented an interval type-2 fuzzy-logic-based framework for reputation management in P2P e-commerce that is more capable of handling uncertainties than other frameworks.

Seller reputation is even more vital while selling secondhand products in online markets. Auction websites (e.g., eBay), one type of well-studied e-commerce website, allow sellers to sell secondhand products. On traditional auction websites, transaction completion depends on not only the price and quality of products but also the reputation of the participants [31]. On new-type secondhand e-commerce websites (e.g., XianYu), many sellers do not have records of successful trading; therefore, it is difficult for buyers to prejudge sellers’ reputation based on former ratings or customer reviews. The concept of signaling theory stems from the concept of information economy, according to which sellers may send signals to help consumers address the information asymmetry problem [32]. A secondhand seller with a high reputation is more likely to provide valuable signals about products, which reduces buyers perceived risk. Therefore, our reputation assessment approach combines textual features with numerical features extracted from both seller-level and product-level information signals, which is meaningful in assessing secondhand sellers’ reputation.

## 2.3. Ontology-based Text Analysis

Ontology refers to the formal and proper modification of a shared conceptualization in a specific domain that presents knowledge in a format that humans can understand [33, 34]. In the past few years, many researchers in different fields have applied ontology to the storing and exploitation of domain knowledge [35]. Ontologies that are arranged by different topics in different fields are constructed through collections of various links on websites [36]. More specifically, a product ontology can be constructed to describe the classes and relations based on the number of reviews, which contributes to the semantic analysis of context [37]. Classical ontologies work excellently in extracting data from organized information and classifying the features of a context [38].

However, classical ontologies can hardly process fuzzy data, as data from networks are commonly unstructured and uncertain. Currently, most researchers combine fuzzy logic with classical ontology to address the problem of uncertain input data [39]. A fuzzy product ontology underpinned by fuzzy sets and fuzzy relations helps identify uncertainty and predict popularity among researchers in various fields, and thus, the effectiveness of text analysis has improved. Fuzzy product ontologies can be applied to develop the classical learning method and product review classification. The methodology that applies product ontology to construct aspect-oriented rather than feature-based sentiment analysis performs well in social analytics [41]. The classical text analysis method, which needs structured and well-labeled train data to achieve accurate results, can hardly handle accidents from unstructured texts and recognize the domain-valuable topic [42]. Meanwhile, the ontology-based text analysis method constructs the domain knowledge, which benefits domain extraction and unstructured text processing. Additionally, the ontology-based text semantic method provides features that can be applied for identifying and validating consistency [43].

Our study differs from previous research in that we develop a domain ontology-based latent Dirichlet allocation (LDA) mining method in a secondhand e-commerce market. The product ontology based on classical e-commerce markets is not applicable to the secondhand domain. The topic information from the LDA mining method is fed to the product ontology miner, which could help build a fuzzy product ontology for secondhand products.

## 2.4. The Main Differences between Our Work and Previous Studies

Our work differs from previous studies in the following four ways. First, while previous studies model seller reputation on traditional e-commerce websites or auction websites, no study has examined the new-type secondhand online markets that have launched in recent years. We aim to study seller reputation assessment on new-type secondhand e-commerce websites, which allow sellers to autonomously determine the price of their products. Second, secondhand online markets have different attributes than traditional e-commerce markets. We combine these new features with common evaluating determinants to model seller reputation. Third, though machine learning methods having been used in modeling seller reputation, no previous studies have applied an ontology-based LDA method for mining topical features from product descriptions. Fourth, most previous studies have examined global e-commerce websites such as e-Bay. Our research aims to analyze seller reputation based on Chinese secondhand online markets.

## 3. A Text Analytics Framework for Secondhand Seller Reputation

Although previous studies have considered some influential factors of people’s reputations [22, 29], the proposed framework considers many factors peculiar to secondhand online markets. In particular, we design a new aspect-extraction method that combines the domain ontology and topic modeling results to extract deep textual features from product descriptions. The mined topical features, along with some common evaluation attributes, are then fed into the ensemble classifier to evaluate secondhand sellers’ reputation. The proposed text analytics framework for secondhand sellers’ reputation, outlined in Figure 1, consists of three main processes: data collection, feature extraction, and reputation assessment.

![](/api/attachments/AKFV27TH/fulltext/images/e2ae31b9b6178d67a2d9821e1b6e442ea66b628b319d24f8e3c6e6fdb8e39832.jpg)  
Figure 1. A Text Analytics Framework for Secondhand Seller Reputation

## 3.1. Data Collection

The data used in our study are crawled from a popular secondhand e-commerce platform in China. Numerous secondhand sellers’ information is collected, including their basic information and all product-specific information. The datasets include both numerical data (e.g., browsing volume) and textual data (e.g., buyers’ comments). As for numerical features, the proposed model utilizes eight common attributes, as shown in Table 1. As for textual features, product description, bargaining messages and buyer comments are three different textual data sources on this platform. Sellers provide product descriptions to introduce their products. Before making purchase decisions, buyers can ask sellers questions and bargain on bargaining boards. The final price of the secondhand product is usually set after the bargaining. The process of bargaining between buyers and sellers is displayed to new buyers. Bargaining messages express the buyers’ expectation for the secondhand products before buying them, and buyer comments show their assessment of the secondhand products after they buy them. In addition to some statistical features calculated from textual data (e.g., comment volume), we also mine topical features from product descriptions.

Table 1. Numerical Reputation Features

<table><tr><td>Feature</td><td>Description</td></tr><tr><td>Browsing Volume</td><td>Number of pages browsed</td></tr><tr><td>Collection Volume</td><td>Number of products on a seller&#x27;s website</td></tr><tr><td>Discount Rate</td><td>Current price/original price</td></tr><tr><td>Outlier Volume</td><td>Number of abnormal prices (such as 99999 for the original price or 0 for the current price)</td></tr><tr><td>Comment Volume</td><td>Number of reviews for a seller</td></tr><tr><td>Bargain Volume</td><td>Number of bargaining messages sent to/sent by a seller</td></tr><tr><td>Reply Rate</td><td>Number of seller&#x27;s replies/bargain volume</td></tr><tr><td>Resale Volume</td><td>Number of successful transactions of a seller</td></tr></table>

## 3.2. Feature Extraction

Feature extraction is a crucial task for data mining exercises [44]. We gather sellers’ basic information and all of their product information. Our dataset contains numerical data and textual data. We preprocess the numerical data to represent concrete features. Additionally, we preprocess textual data, i.e., word segmentation, part-of-speech (POS) tagging, and stop-word removal. After we collect product descriptions, we apply a word segmentation process to divide each Chinese sentence into words and identify the POS of each word. We consider only nouns because they are regarded as the most representative POS [45]. We apply the preprocessed contexts to construct an ontology-based topic model, which we use to determine the topical features. The extracted topical features represent the aspect-level descriptions of secondhand suit-dresses, which are combined with common numerical features to predict the reputation of secondhand sellers.

## 3.3. Reputation Assessment

Ensemble learning techniques combine several base learners to obtain an integrated output, as proven both theoretically and empirically [46, 47]. Random forest (RF) [48] is a widely used ensemble learning method based on a set of decision trees, which are the base learners. In our study, we employ different well-known classifiers to establish our evaluation model. We finally choose an RF classifier due to its strong performance.

For our reputation assessment evaluation dataset, we label the reputation ranking of some sellers based on customer comments. To do so, we apply sentiment analysis for comments that customers posted after completing a transaction. In our evaluation dataset, each seller reputation (i.e., a classification instance) is marked with a ranking label based on the sentiment score from customers’ comments. We use two classification criteria methods. One is the three-classifications method, which divides the seller’s reputation into “trustworthy”, “ambiguous” and “untrustworthy” based on the sentiment score. The other is the five-classifications method, in which seller reputation is grouped into five categories-“reputable”, “trustworthy”, “ambiguous”, “untrustworthy” and “infamous”-following the same rule as before. In the evaluation, a balanced class distribution (i.e., a similar number of sellers in different reputation categories) is maintained because an imbalanced train may lead to negative results [49]. The whole evaluation dataset is divided into a training set and a test set. The training set is applied to train the ensemble learning model in advance. After the training process, the test set is used for evaluating sellers reputation.

## 4. The Computational Methods

## 4.1. Topic Modeling Based on LDA

The topic modeling method is a popular type of technology in the field of text mining. Representative topics can be extracted from massive textual data. LDA is one of the most effective topic modeling methods. This method introduces a latent topic variable and assumes that both the topic-word distribution and document-topic distribution are Dirichlet distributions [50]. Using an estimation method (e.g., Markov Chain Monte Carlo), the prior parameters of the distributions can be inferred [51]. Semantically related words are more likely to be grouped into the same topic according to their co-occurrences in different documents. In our study, we apply LDA to obtain a topic-level description of secondhand suit-dresses. Hence, we can obtain the topic-level completeness of the descriptions for each secondhand seller.

However, LDA also has some demonstrated drawbacks [52]. One of the major weaknesses is that the topics can be very noisy, especially on short texts. As some topics contain many irrelevant words, it is a difficult task to map topic results into interpretable concepts. Furthermore, although LDA ensures the objectiveness of the results, some valuable topics could be missed due to the limitations of the original datasets. For example, if a topic were vital in the real-word domain but barely existed in all experimental documents, it would not be reflected in LDA results.

## 4.2. Domain Ontology Construction

The concept of ontology originated in the field of philosophy and is now widely used in information systems studies [41, concepts with their relationships and some constraints. Due to its reusability, domain ontology is widely used to represent specific domain knowledge. In ontology-based text analytics tasks, researchers often manually construct a domain ontology before the text mining process [55]. A powerful reference is necessary to ensure the semantic relationships among different concepts. Otherwise, the constructed domain ontology would be ambiguous. Particularly in the e-commerce context, classical ontologies grow very large and quickly and become cumbersome to use. Hence, to construct a secondhand product ontology, we use fuzzy ontology, where similar words and words with similar meanings are combined in the same class. This can simplify the construction of the ontology.

# ACCEPTED MANUSCRIPT

In our study, a domain ontology for secondhand products would be the optimal solution for examining the topic-level completeness of product descriptions. However, as mentioned before, references are lacking for secondhand products, as they represent an immature domain. On the contrary, we can construct a precise domain ontology for the corresponding new products based on well-known e-commerce platforms (e.g., Taobao.com<sup>3</sup>). Taobao is the largest e-commerce platform with the highest user activity and the most comprehensive categories, and it has abundant consumer feedback. As the states of these products are constantly changing and user-driven, a complete topic-level description for secondhand products contains all of the concepts in its domain ontology. To examine the domain ontology, we summarize the aspects closely related to the product attributes based on the high-frequency information extracted from users’ product reviews. Therefore, the domain ontology of different products can be inferred.

## 4.3. The Computational Details of the Ontology-based Topic Model

Both the topic modeling method and the domain ontology-based method are appropriate for identifying topic-level descriptions. However, as discussed in the previous section, they also have defects. Chen and Xu [56] first considered combining the domain ontology and topic mode new topics from customer reviews. In this study, we make two improvements to the ontology-based topic modeling method. First, we solve the problem of the difficulty of directly constructing a special domain ontology. Second, we introduce a domain corpus in advance; therefore, the combining process is more automatic and requires little manual intervention.

For some immature domains, it is difficult to construct a comprehensive domain ontology. In our proposed method, we primarily construct the ontology of the subdomain instead. Taking suit-dresses as an example, we construct a domain ontology for a suit-dress market. For each concept, the ontology contains concrete features (words) as the basic elements. Moreover, we establish a domain corpus of suit-dresses. Compared with the product descriptions for secondhand suit-dresses on XianYu, the product descriptions for suit-dresses on traditional e-commerce platforms (e.g., Taobao.com) are much more normative. After crawling massive numbers of product descriptions for suit-dresses, we apply word segmentation and a word frequency count on all textual descriptions.

As a supplement to domain ontology, LDA is applied to extract topics from secondhand sellers’ product descriptions. All product descriptions written by the same seller are gathered together as one document. A perplexity-based approach is applied to estimate the number of topics in all documents [57]. To guarantee the objectivity of the topic modeling results, the classical realization process of LDA is employed. The domain corpus of suit-dresses is then used to screen out the peculiar topics of secondhand suit-dresses from the LDA results. As the volume of suit-dress description data is much larger than that of secondhand suit-dresses, the topic is peculiar as long as it contains 10% words outside the corpus. The final topic-level description of secondhand suit-dresses combines both the concepts from ontology and the selected peculiar topics from the LDA results. The pseudo code of our ontology-based topic

modeling method is illustrated in Algorithm 1.

## Algorithm 1: Ontology-based Topic Model

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs: A collection of product descriptions PD1 for products.
A collection of product descriptions PD2 for secondhand products.
Output: Topic-level description of secondhand products.
// Phase 1: Build a domain corpus and construct a domain ontology for products
1. Extract nouns from DC after word segmentation and POS tagging;
2. for each noun n in PD1
3.    $WC_{n} = \text{count(n)}$;
4.    $WF_{n} = WC_{n}/\text{count(PD1)}$;
5.    if $WF_{n} &gt; 0.01$ then
6.    Add noun n =&gt; domain corpus;
7.    end if
8. end for
9. Construct a domain ontology for products;
// Phase 2: Use LDA to extract topics from PD2
10. Group product descriptions of the same seller as one document (D);
11. Apply TF/IDF to identify keywords for each document;
12. Estimate the number of topics (K) by perplexity-based approach;
13. repeat
14. Choose a topic distribution $\theta_{d} \sim Dir(\alpha)$;
15. for each topic k
16.    Choose a word distribution $\varphi_{k} \sim Dir(\beta)$;
17. end for
18. Adjust the topic-word distribution by $\varphi_{k,v} = \varphi_{k,v} \cdot \phi_{k,v}^{T}$;
19. for each document d
20.    Generate a specific topic $z_{i} \sim Mul(\theta_{d})$;
21.    Generate a specific word $w_{i} \sim Mul(\varphi_{z_{i}})$;
22. end for
23. until convergence
// Phase 3: Combine ontology concepts and LDA topic results
24. for each topic k
25.    remain = 0;
26.    for each word w
27.    if word w not in domain corpus then
28.    remain = remain+1;
29.    end if
30. end for
31. if (remain &gt;= count (w)/10) then
32.    Add topic k =&gt; topic-level description;
33. end if
34. end for
35. Add concepts from domain ontology =&gt; topic-level description;
36. Remove irrelevant words in topic-level description
</div>

## 5. Empirical Study and Results

## 5.1. Data Description and Evaluation Criteria

# ACCEPTED MANUSCRIPT

The data we use in the experiments are crawled from XianYu, a well-known secondhand e-commerce website in China. XianYu is described as a website where people sell secondhand items that they purchased in the past but no longer need. Among all the categories in XianYu, we choose six with abundant data over a three-month period, from 2016/06/01 to 2016/09/19. The raw dataset consists of 11598 “suit-dress” products, 10921 “camera” products, 10024 “phone” products, 10672 “watch” products, 9321 n’s shoes” products and 8196 “jewelry” products on the website. Each product belongs to one seller; hence, information on the corresponding seller and all of his/her products are also collected. We classify sellers into six seller categorie cording to the category of product that they sell. When a seller sells products from more than one on the website, the seller is included in all of these seller categories. However, some sellers are omitted from the dataset because some of their important information is lacking. Most of the omitted sellers do not have any trading records or buyer evaluation information. Therefore, their reputation cannot be prejudged in our proposed method, and they are of little value to our study. Data cleaning leaves 4071 sellers of products from six categories who have been registered more than one year. For sellers in each category, we collect both their basic information and product-specific information. Among all six category sellers, 1371 are labeled “trustworthy”, 1339 are labeled “ambiguous”, and the other 1361 are labeled “untrustworthy” with the three-classifications method. With the five-classifications method, 821 are labeled “reputable”, 813 “trustworthy”, 812 “ambiguous”, 801 “untrustworthy” and 824 “infamous”.

## 5.2. Ontology Feature Description

# ACCEPTED MANUSCRIPT

Based on well-known e-commerce platforms (e.g., Taobao.com), we construct a precise domain ontology for six different product categories. As the newness of a product is a changing state, a complete topic-level description for secondhand products contains all of the concepts in domain ontology. Therefore, one domain ontology for one product category is constructed, and a segment of the results is shown in Figure 2. For example, the concept “fabric” is related to “suit-dress”. The fabric of a dress may influence the suit-dress expectations of buyers, which leads to buyers’ comments on the merchants’ reputation. By constructing these ontologies, relevant concepts that are related to these product categories can be easily retrieved.

![](/api/attachments/AKFV27TH/fulltext/images/d364607b7367d00514a01327424c56801cc5d89498a52e94341a84922509ff18.jpg)

## 5.3. Topical Feature Description

The proposed text analytics framework combines textual features and numerical features to enhance the reputation assessment of online secondhand sellers. For textual features, we develop an ontology-based topic model method to obtain topic-level descriptions of secondhand products. For the traditional LDA method, the topic modeling results of the product descriptions for secondhand products are broad but not focused. Some topics contain many irrelevant words; thus, it is difficult to explain the general ideas of the topics.

Our proposed method automatically selects valuable topics from the raw results. After adjusting some noisy words, these topics are combined with concepts from the constructed domain ontology. Table 2 displays some of the key words of the final results of our topic-level description of secondhand products. It contains several topical features that represent the degree of integrity of secondhand sellers’ product descriptions.

Table 2. Topic-level Descriptions of Secondhand Products

<table><tr><td>Topic</td><td>Suit-dress</td><td>Topic</td><td>Women's shoes</td></tr><tr><td>Color</td><td>Black, Ivory, Denim, Navy Blue, Colorful</td><td>Color</td><td>Black, White, Multi-color</td></tr><tr><td>Size</td><td>Large, Medium, Small, X-small</td><td>Shoes-size</td><td>Medium, X-large, X-small</td></tr><tr><td>Style</td><td>Blouse, Lovable, Leisure, Temperament</td><td>Style</td><td>Classic, Latest, Business, Casual</td></tr><tr><td>Fabric</td><td>Rayon, Spandex, Tencel, Polyester, Cotton</td><td>Material</td><td>Crystal, Cubic Zirconia, Fur, Gold, Manmade, Metal, Rubber</td></tr><tr><td>Design</td><td>Halter Neckline, Keyhole Back, Circle Skirt, Matching Belt, Sleeveless</td><td>Category</td><td>Casual Shoes, Jogging, Boots, High Heels</td></tr><tr><td>Suitable season</td><td>Summer Preferred, Winter, Hot Weather Preferred, Spring &amp; Fall</td><td>Appearance</td><td>Brogue, Plain-toe, Flip-flops, Mules</td></tr><tr><td>Condition</td><td>New, Once, 99% new, 95% new</td><td>Comfort</td><td>Grind-feet, Portability, Lightweight</td></tr><tr><td>Topic</td><td>Watch</td><td>Topic</td><td>Phone</td></tr><tr><td>Color</td><td>Various, White, Dark Blue, Gray, Black</td><td>Color</td><td>Gold, White, Black, Crimson</td></tr><tr><td>Brand</td><td>Roamer, Mido, Tissot, Omega, Rolex</td><td>Brand</td><td>Huawei, Vivo, Samsung, Apple</td></tr><tr><td>Usage</td><td>GPS, Chronometer, Sports Watch, Waterproof</td><td>Function</td><td>Fingerprint Recognition, NFC, Face Recognition</td></tr><tr><td>Design</td><td>Band Shape, Display Type, Buckle, Clasp</td><td>Appearance</td><td>Color, Screen Size, Rounded Corners</td></tr><tr><td>Accuracy</td><td>Inaccurate Time, Digital Accuracy</td><td>Performance</td><td>Device Compatibility, Operating, System Performance</td></tr><tr><td>Material</td><td>Steel, Mechanical, Waterproof, Gold</td><td>Service</td><td>Sales Support, Customer Service</td></tr><tr><td>Topic</td><td>Camera</td><td>Topic</td><td>Jewelry</td></tr><tr><td>Accessories</td><td>Battery, Charger, Lens, Partition, Hood</td><td>Material</td><td>Gold-plated, Quartz, Gem, Metal, Crystal</td></tr><tr><td>Function</td><td>Contrast Detect, Selective Single-point</td><td>Process</td><td>Mosaic, Sculpture, Natural, Polishing</td></tr><tr><td>Origin</td><td>Domestic, German, Japan</td><td>Design</td><td>Classic-style, Blue Heart, Rose-like</td></tr><tr><td>Brand</td><td>Canon, Fujifilm, Nikon, Sony, Matsushita</td><td>Packaging</td><td>Gift Packaging, Rough Packaging</td></tr><tr><td>Length</td><td>Mm, Long, Short, 2000</td><td>Size</td><td>Suitable, Small, Large, Chain-length</td></tr><tr><td>Pixel</td><td>1800 pixel, 2400 pixel</td><td>Carat</td><td>2.4 CT, 1.8 CT</td></tr></table>

## 5.4. Experimental Results for Predictive Models

We compare the prediction performance of the proposed RF classifier with that of some other machine learning classifiers, including Naive Bayes [58], Support Vector Machine [59] and Back-propagation Neutral Network [60]. The input features for different classifiers include numerical features and the topical features extracted from our proposed method. We implement these experiments in Weka and train the model by cross-validation (folds 10). The experimental results of the different classifiers are listed in Table 3. The results demonstrate that the proposed RF classifier outperforms the baseline classifiers in most cases.

The experimental results vary for different product categories. The prediction performance for watches is the best, achieving F1 scores of 0.79 in the three-classifications method and 0.64 in the five-classifications method. The results for suit-dresses and women’s shoes are slightly lower than those of other product categories.

Table 3. Prediction Performance of Various Classifiers

<table><tr><td>Method</td><td>Dataset</td><td colspan="4">Suit-dress</td><td colspan="4">Camera</td><td colspan="4">Phone</td></tr><tr><td rowspan="3">Three-classifications method</td><td>Classifier</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td></tr><tr><td>Accuracy</td><td>0.69</td><td>0.51</td><td>0.58</td><td>0.55</td><td>0.72</td><td>0.59</td><td>0.72</td><td>0.71</td><td>0.75</td><td>0.60</td><td>0.67</td><td>0.70</td></tr><tr><td>Precision</td><td>0.71</td><td>0.56</td><td>0.75</td><td>0.60</td><td>0.74</td><td>0.60</td><td>0.69</td><td>0.75</td><td>0.82</td><td>0.58</td><td>0.61</td><td>0.68</td></tr><tr><td rowspan="8"></td><td>Recall</td><td>0.75</td><td>0.60</td><td>0.60</td><td>0.62</td><td>0.78</td><td>0.64</td><td>0.77</td><td>0.69</td><td>0.76</td><td>0.64</td><td>0.76</td><td>0.76</td></tr><tr><td> $F_1$ </td><td>0.73</td><td>0.58</td><td>0.67</td><td>0.61</td><td>0.76</td><td>0.62</td><td>0.73</td><td>0.72</td><td>0.79</td><td>0.61</td><td>0.68</td><td>0.72</td></tr><tr><td>Dataset</td><td colspan="4">Watch</td><td colspan="4">Women's shoes</td><td colspan="4">Jewelry</td></tr><tr><td>Classifier</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td></tr><tr><td>Accuracy</td><td>0.78</td><td>0.62</td><td>0.73</td><td>0.69</td><td>0.66</td><td>0.54</td><td>0.61</td><td>0.58</td><td>0.71</td><td>0.64</td><td>0.68</td><td>0.72</td></tr><tr><td>Precision</td><td>0.76</td><td>0.61</td><td>0.69</td><td>0.73</td><td>0.67</td><td>0.58</td><td>0.63</td><td>0.59</td><td>0.75</td><td>0.60</td><td>0.72</td><td>0.67</td></tr><tr><td>Recall</td><td>0.82</td><td>0.67</td><td>0.79</td><td>0.67</td><td>0.69</td><td>0.56</td><td>0.65</td><td>0.65</td><td>0.79</td><td>0.75</td><td>0.66</td><td>0.80</td></tr><tr><td> $F_1$ </td><td>0.79</td><td>0.64</td><td>0.74</td><td>0.70</td><td>0.68</td><td>0.57</td><td>0.64</td><td>0.62</td><td>0.77</td><td>0.67</td><td>0.69</td><td>0.73</td></tr><tr><td>Method</td><td>Dataset</td><td colspan="4">Suit-dress</td><td colspan="4">Camera</td><td colspan="4">Phone</td></tr><tr><td rowspan="11">Five-classifications method</td><td>Classifier</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td></tr><tr><td>Accuracy</td><td>0.55</td><td>0.45</td><td>0.48</td><td>0.47</td><td>0.57</td><td>0.41</td><td>0.46</td><td>0.44</td><td>0.60</td><td>0.52</td><td>0.54</td><td>0.54</td></tr><tr><td>Precision</td><td>0.58</td><td>0.43</td><td>0.53</td><td>0.53</td><td>0.54</td><td>0.43</td><td>0.51</td><td>0.48</td><td>0.63</td><td>0.53</td><td>0.61</td><td>0.54</td></tr><tr><td>Recall</td><td>0.64</td><td>0.51</td><td>0.55</td><td>0.51</td><td>0.62</td><td>0.56</td><td>0.47</td><td>0.54</td><td>0.59</td><td>0.57</td><td>0.55</td><td>0.64</td></tr><tr><td> $F_1$ </td><td>0.61</td><td>0.47</td><td>0.54</td><td>0.52</td><td>0.58</td><td>0.49</td><td>0.49</td><td>0.51</td><td>0.61</td><td>0.55</td><td>0.58</td><td>0.59</td></tr><tr><td>Dataset</td><td colspan="4">Watch</td><td colspan="4">Women's shoes</td><td colspan="4">Jewelry</td></tr><tr><td>Classifier</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td><td>RF</td><td>NB</td><td>SVM</td><td>NN</td></tr><tr><td>Accuracy</td><td>0.63</td><td>0.51</td><td>0.57</td><td>0.55</td><td>0.52</td><td>0.43</td><td>0.51</td><td>0.45</td><td>0.61</td><td>0.49</td><td>0.53</td><td>0.58</td></tr><tr><td>Precision</td><td>0.60</td><td>0.53</td><td>0.56</td><td>0.58</td><td>0.51</td><td>0.44</td><td>0.50</td><td>0.52</td><td>0.61</td><td>0.50</td><td>0.55</td><td>0.59</td></tr><tr><td>Recall</td><td>0.68</td><td>0.51</td><td>0.62</td><td>0.56</td><td>0.55</td><td>0.48</td><td>0.56</td><td>0.46</td><td>0.67</td><td>0.54</td><td>0.59</td><td>0.63</td></tr><tr><td> $F_1$ </td><td>0.64</td><td>0.52</td><td>0.59</td><td>0.57</td><td>0.53</td><td>0.46</td><td>0.53</td><td>0.49</td><td>0.64</td><td>0.52</td><td>0.57</td><td>0.61</td></tr></table>

## 5.5. Experimental Results for Various Feature Sets

We also explore the effectiveness of different features. As shown in Table 4, we separate common to both traditional e-commerce platforms and secondhand e-commerce platforms, while the features in C and D are peculiar to secondhand e-commerce platforms. Based on these four discriminative feature sets, we establish four testing feature sets—E1, E2, E3 and E4—by adding them one by one. The descriptions of these four feature sets are presented in Table 5. In E1 and E2, topical features are extracted based on the original domain ontology, while in E3 and E4, we apply our ontology-based topic model method to mine topical features.

Table 4. Feature Classification Matrix

<table><tr><td>Feature Source</td><td>Text</td><td>Numerical</td></tr><tr><td>Product</td><td>A</td><td>B</td></tr><tr><td>Secondhand product</td><td>C</td><td>D</td></tr></table>

Table 5. Feature Set Description

<table><tr><td>Feature Set</td><td>Description</td></tr><tr><td>E1(A)</td><td>Topical Features from Product Description, Comment Volume</td></tr><tr><td>E2(A+B)</td><td>Browsing Volume, Collection Volume, Topical Features from Product Description, Comment Volume</td></tr><tr><td>E3(A+B+C)</td><td>Bargain Volume, Reply Rate, Browsing Volume, Collection Volume, Topical Features from Product Description, Comment Volume</td></tr><tr><td>E4(A+B+C+D)</td><td>Discount Rate, Outlier Volume, Resale Volume, Bargain Volume, Reply Rate, Browsing Volume, Collection Volume, Topical Features from Product Description, Comment Volume</td></tr></table>

Our experimental results are depicted in Table 6. For most of the product categories, the performance continuously improves from E1 to E3. These results confirm the effectiveness of most of the constructed features. On one hand, this confirms that topical features extracted from textual descriptions are the other hand, some features (e.g., browsing volume and collection volume) that have been used in traditional e-commerce platforms also work in this well-known new-type secondhand e-commerce platform. However, for some of the product categories, the prediction performance on feature set E4 is not improved. The reason may be that the added features cause an over-fitting problem for the predictive model. Therefore, as we can observe from our experimental results, product descriptions written by sellers themselves may be a more valuable data source to mine deep relevant textual features. On the contrary, some particular numerical features on secondhand e-commerce platforms, such as discount rate and outlier volume, are not effective indicators for sellers’ reputation assessment in all product categories. Only for some products with higher prices, such as phones and jewelry, does the prediction performance of feature set E4 slightly increase.

Table 6. Prediction Performance of Various Feature Sets

<table><tr><td>Method</td><td>Dataset</td><td colspan="4">Suit-dress</td><td colspan="4">Camera</td><td colspan="4">Phone</td></tr><tr><td rowspan="11">Three-classifications method</td><td>Feature Set</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td></tr><tr><td>Accuracy</td><td>0.51</td><td>0.58</td><td>0.69</td><td>0.67</td><td>0.54</td><td>0.69</td><td>0.72</td><td>0.73</td><td>0.58</td><td>0.56</td><td>0.75</td><td>0.79</td></tr><tr><td>Precision</td><td>0.54</td><td>0.69</td><td>0.71</td><td>0.69</td><td>0.62</td><td>0.73</td><td>0.74</td><td>0.71</td><td>0.59</td><td>0.61</td><td>0.82</td><td>0.78</td></tr><tr><td>Recall</td><td>0.58</td><td>0.61</td><td>0.75</td><td>0.73</td><td>0.58</td><td>0.69</td><td>0.78</td><td>0.77</td><td>0.63</td><td>0.71</td><td>0.76</td><td>0.86</td></tr><tr><td> $F_1$ </td><td>0.56</td><td>0.65</td><td>0.73</td><td>0.71</td><td>0.60</td><td>0.71</td><td>0.76</td><td>0.74</td><td>0.61</td><td>0.66</td><td>0.79</td><td>0.82</td></tr><tr><td>Dataset</td><td colspan="4">Watch</td><td colspan="4">Women&#x27;s shoes</td><td colspan="4">Jewelry</td></tr><tr><td>Feature Set</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td></tr><tr><td>Accuracy</td><td>0.52</td><td>0.63</td><td>0.78</td><td>0.78</td><td>0.49</td><td>0.56</td><td>0.67</td><td>0.63</td><td>0.53</td><td>0.62</td><td>0.71</td><td>0.72</td></tr><tr><td>Precision</td><td>0.57</td><td>0.75</td><td>0.76</td><td>0.73</td><td>0.54</td><td>0.68</td><td>0.64</td><td>0.61</td><td>0.67</td><td>0.65</td><td>0.75</td><td>0.76</td></tr><tr><td>Recall</td><td>0.67</td><td>0.69</td><td>0.82</td><td>0.81</td><td>0.60</td><td>0.58</td><td>0.72</td><td>0.69</td><td>0.59</td><td>0.71</td><td>0.79</td><td>0.82</td></tr><tr><td> $F_1$ </td><td>0.62</td><td>0.72</td><td>0.79</td><td>0.77</td><td>0.57</td><td>0.63</td><td>0.68</td><td>0.65</td><td>0.63</td><td>0.68</td><td>0.77</td><td>0.79</td></tr><tr><td>Method</td><td>Dataset</td><td colspan="4">Suit-dress</td><td colspan="4">Camera</td><td colspan="4">Phone</td></tr><tr><td rowspan="11">Five-classifications method</td><td>Feature Set</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E 1</td><td>E2</td><td>E3</td><td>E4</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td></tr><tr><td>Accuracy</td><td>0.41</td><td>0.49</td><td>0.55</td><td>0.51</td><td>0.47</td><td>0.52</td><td>0.57</td><td>0.58</td><td>0.48</td><td>0.56</td><td>0.60</td><td>0.63</td></tr><tr><td>Precision</td><td>0.48</td><td>0.51</td><td>0.58</td><td>0.57</td><td>0.49</td><td>0.52</td><td>0.62</td><td>0.58</td><td>0.49</td><td>0.55</td><td>0.63</td><td>0.67</td></tr><tr><td>Recall</td><td>0.42</td><td>0.57</td><td>0.64</td><td>0.53</td><td>0.53</td><td>0.56</td><td>0.54</td><td>0.54</td><td>0.53</td><td>0.58</td><td>0.59</td><td>0.69</td></tr><tr><td> $F_1$ </td><td>0.45</td><td>0.54</td><td>0.61</td><td>0.55</td><td>0.51</td><td>0.54</td><td>0.58</td><td>0.56</td><td>0.51</td><td>0.56</td><td>0.61</td><td>0.68</td></tr><tr><td>Dataset</td><td colspan="4">Watch</td><td colspan="4">Women&#x27;s shoes</td><td colspan="4">Jewelry</td></tr><tr><td>Feature Set</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td></tr><tr><td>Accuracy</td><td>0.49</td><td>0.54</td><td>0.63</td><td>0.64</td><td>0.38</td><td>0.51</td><td>0.52</td><td>0.47</td><td>0.43</td><td>0.48</td><td>0.61</td><td>0.63</td></tr><tr><td>Precision</td><td>0.59</td><td>0.51</td><td>0.71</td><td>0.57</td><td>0.48</td><td>0.46</td><td>0.51</td><td>0.46</td><td>0.50</td><td>0.56</td><td>0.67</td><td>0.70</td></tr><tr><td>Recall</td><td>0.46</td><td>0.67</td><td>0.58</td><td>0.65</td><td>0.44</td><td>0.50</td><td>0.55</td><td>0.59</td><td>0.44</td><td>0.48</td><td>0.61</td><td>0.64</td></tr><tr><td> $F_1$ </td><td>0.52</td><td>0.58</td><td>0.64</td><td>0.61</td><td>0.46</td><td>0.48</td><td>0.53</td><td>0.52</td><td>0.47</td><td>0.52</td><td>0.64</td><td>0.67</td></tr></table>

## 5.6. Comparative Evaluation

We also compare different text analytics methods to evaluate the effectiveness of our proposed ontology-based topic model method. Feature sets E5-E8 correspond, respectively, to

E1-E4, but only numerical features remain (e.g., only comment volume remains in feature set E5). Domain ontology and classical LDA are used as two baseline topical extraction methods. The extracted topical features are added to feature sets E5-E8, and the RF classifier is applied as the prediction model. Table 7 shows the F1 score for the three classifications and indicates that our proposed textual analytics method outperforms the other two methods for all feature sets. In particular, for the E7 feature set, the average F1 score for the six product categories in our ontology-based topic model is 8% and 12% higher than that in the domain ontology and classical LDA methods, respectively. The main reason for the performance improvement achieved by our ontology-based topic model is that our method can comprehensively mine topic-level descriptions of a rarely discussed domain. Moreover, in contrast to the classical LDA method, our proposed method does not introduce many noisy topics.

Table 7. Prediction Performance of Different Methods

<table><tr><td>Method</td><td>Dataset</td><td colspan="4">Suit-dress</td><td colspan="4">Camera</td><td colspan="4">Phone</td></tr><tr><td rowspan="5">Domain Ontology Method</td><td>Feature Set</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td></tr><tr><td> $F_1$ </td><td>0.55</td><td>0.61</td><td>0.65</td><td>0.63</td><td>0.58</td><td>0.65</td><td>0.69</td><td>0.68</td><td>0.59</td><td>0.63</td><td>0.72</td><td>0.75</td></tr><tr><td>Dataset</td><td colspan="4">Watch</td><td colspan="4">Women's shoes</td><td colspan="4">Jewelry</td></tr><tr><td>Feature Set</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td></tr><tr><td> $F_1$ </td><td>0.60</td><td>0.67</td><td>0.72</td><td>0.70</td><td>0.53</td><td>0.60</td><td>0.62</td><td>0.59</td><td>0.60</td><td>0.65</td><td>0.70</td><td>0.72</td></tr><tr><td rowspan="6">Classical LDA Method</td><td>Dataset</td><td colspan="4">Suit-dress</td><td colspan="4">Camera</td><td colspan="4">Phone</td></tr><tr><td>Feature Set</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td></tr><tr><td> $F_1$ </td><td>0.52</td><td>0.54</td><td>0.59</td><td>0.53</td><td>0.54</td><td>0.58</td><td>0.64</td><td>0.61</td><td>0.56</td><td>0.62</td><td>0.67</td><td>0.69</td></tr><tr><td>Dataset</td><td colspan="4">Watch</td><td colspan="4">Women's shoes</td><td colspan="4">Jewelry</td></tr><tr><td>Feature Set</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td></tr><tr><td> $F_1$ </td><td>0.56</td><td>0.61</td><td>0.67</td><td>0.64</td><td>0.49</td><td>0.54</td><td>0.57</td><td>0.55</td><td>0.55</td><td>0.61</td><td>0.64</td><td>0.65</td></tr><tr><td rowspan="4">Ontology-based LDA Method</td><td>Dataset</td><td colspan="4">Suit-dress</td><td colspan="4">Camera</td><td colspan="4">Phone</td></tr><tr><td>Feature Set</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td></tr><tr><td> $F_1$ </td><td>0.56</td><td>0.69</td><td>0.73</td><td>0.71</td><td>0.60</td><td>0.71</td><td>0.76</td><td>0.74</td><td>0.61</td><td>0.73</td><td>0.79</td><td>0.82</td></tr><tr><td>Dataset</td><td colspan="4">Watch</td><td colspan="4">Women's shoes</td><td colspan="4">Jewelry</td></tr><tr><td rowspan="2"></td><td>Feature Set</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td></tr><tr><td> $F_1$ </td><td>0.62</td><td>0.72</td><td>0.79</td><td>0.77</td><td>0.57</td><td>0.63</td><td>0.68</td><td>0.65</td><td>0.63</td><td>0.68</td><td>0.77</td><td>0.79</td></tr></table>

## 5.7. Discussion

In this study, we propose an effective method for assessing secondhand sellers’ reputation. Along with some numerical features, the prediction model considers topical features extracted by our ontology-based topic model method. Our experimental results show the effectiveness of most of the variables we used in predicting secondhand sellers’ reputation. This is the first study to predict sellers’ reputation in new-type secondhand e-commerce platforms, and many of the features used in traditional e-commerce platforms also proved valuable on secondhand e-commerce platforms. Meanwhile, for secondhand products, the topical features for the corresponding new products are valuable for testing the degree of integrity of product descriptions. To further improve the performance of reputation prediction, topical features peculiar to secondhand products are also extremely important. Our proposed text analytics method considers both the comprehensiveness and the interpretability of topical features for describing secondhand products. The empirical results reveal the effectiveness of these topical features in secondhand sellers’ reputation assessment. They also reveal that the impact of topical features on secondhand sellers’ reputation assessment varies by product category. Furthermore, our proposed method can be used not only in secondhand sellers’ reputation assessment but also in financial risk assessment or in other fields, such as fraud detection in e-commerce and financial markets.

Secondhand e-commerce platforms contain particular variables that do not exist in traditional e-commerce platforms. According to their data source type, we classify them into textual features and numerical features. The experimental results show that for sellers reputation assessment, textual features are better indicators than numerical features. More specifically, a high-reputation secondhand seller has a high probability to write a comprehensive topic-level product description and actively interact with buyers on bargain boards. However, for most of the product categories, the discount rate for the secondhand product appears irrelevant to secondhand sellers’ reputation. Only for some products with higher prices, such as phones and jewelry, does the discount rate appear more effective in sellers’ reputation assessment. Moreover, the empirical results verify the effectiveness of ensemble learning methods in prediction tasks. The prediction performance improves we use single classifiers.

## 6. Conclusions and Future Work

This paper proposes a text analytics framework for assessing secondhand sellers’ reputation in online markets. Based on the proposed ontology-based topic model method and ensemble three-classifications method on a real-word dataset crawled from XianYu. Previous studies have concentrated on the issue of sellers’ reputation on traditional e-commerce platforms or auction platforms; little research has been conducted on new-type secondhand e-commerce platforms such as XianYu. As any user can open his or her own shop without a complex shop-opening process and list superfluous items for sale online without much supervision, it is crucial to predict sellers’ reputation on these type of platforms. Our research fills the aforementioned research gap with the following main contributions. First, we have designed a novel text analytics framework for assessing secondhand e-commerce sellers’ reputation. Second, we have developed a new aspect-extraction method that combines the domain ontology and topic modeling results to extract topical features from product descriptions. Third, we have conducted an empirical analysis to identify the discriminatory features that reveal secondhand sellers’ reputation based on a real-world secondhand e-commerce website.

Since these new-type secondhand e-commerce platforms are still in a preliminary stage of development, our work has important managerial implications. Potential buyers on secondhand e-commerce platforms can apply the proposed text analytics framework to prejudge the reputation of secondhand sellers while making purchase decisions. Secondhand e-commerce platform managers can use our research finding to put up risk warnings or restrict low-reputation sellers from selling. This may decrease the volume of unpleasant transactions. The research findings can support a more effective development of online secondhand markets.

The study contains several limitations. First, the online secondhand sellers were preselected before our experiments. The reason is that some sellers do not have selling records or are missing some basic information. To standardize our model, these sellers were removed before the experiments. However, as mentioned, online secondhand markets are still immature, and new sellers constitute a large portion of the market. It would be better to establish a complete reputation assessment system for all online secondhand sellers. Second, some advanced computational tools can be employed and re-designed the secondhand sellers’ reputation assessment model. For example, advanced fuzzy ontology can be introduced to extract textual features, and deep neural networks can be used to model the relationship between textual features and secondhand sellers’ reputation effectively. Third, although we used many numerical features and textual features, we ignored some information. For example, some sellers also provide their Taobao links or Weibo links. We could try to further extract some valuable features from these links. In addition, the social network relationships between sellers could be considered in the model. Therefore, in future studies, we will focus mainly on a more effective credit evaluation model for online secondhand sellers. Specifically, a higher number of sellers (or even some new sellers without basic information or selling records) can be evaluated in the developed model. Meanwhile, to enhance the accuracy of the evaluation model, we will try to extract more valuable features.

## Acknowledgements

This work was supported in part by the National Natural Science Foundation of China (Grant Nos. 71301163 and 71771212), the Humanities and Social Sciences Foundation of the Ministry of Education (Nos. 14YJA630075 and 15YJA630068), the Fundamental Research Funds for the Central Universities, and the Research Funds of Renmin University of China (No. 15XNLQ08).

## References

[1] A. Brooks, Stretching global production networks: The international second-hand clothing trade, Geoforum 44 (2013) 10-22.

[2] L. Norris, The limits of ethicality in international markets: Imported second-hand clothing in India, Geoforum 67 (2015) 183-193.

[3] N. E. Stroeker, G. Antonides, The process of reaching an agreement in second-hand markets for consumer durables, Journal of Economic Psychology 18(4) (1997) 341-367.

[4] K. Kogan, Second-hand markets and intrasupply chain competition, Journal of Retailing 87(4) (2011) 489-501.

[5] Y. Xiong, P. Zhao, Z. Xiong, G. Li, The impact of product upgrading on the decision of entrance to a secondary market, European Journal of Operational Research 252(2) (2016) 443-454.

[6] L. Berg, Prices on the second-hand market for Swedish family houses: correlation, causation and determinants, European Journal of Housing Policy 2(1) (2002) 1-24.

[7] M. Shafiee, S. Chukova, Optimal upgrade strategy, warranty policy and sale price for second-hand products, Applied Stochastic Models in Business and Industry 29(2) (2013) 157-169.

[8] D. Guiot, D. Roux, A second-hand shoppers’ motivation scale: Antecedents, consequences, and implications for retailers, Journal of Retailing 86(4) (2010) 355-371.

[9] R. N. Yan, S. Y. Bae, H. Xu, Second-hand clothing shopping among college students: the role of psychographic characteristics, Young Consumers 16(1) (2015) 85-98.

## ACCEPTED MANUSCRIPT

[10] P. Resnick, R. Zeckhauser, J. Swanson, K. Lockwood, The value of reputation on eBay: a controlled experiment, Experimental Economics 9 (2) (2006) 79–101.

[11] S. Bertarelli, On the efficacy of imperfect public-monitoring of seller reputation in e-commerce, Electronic Commerce Research and Applications 14(2) (2015) 75-80.

[12] A. R. Rao, L. Qu, R. W. Ruekert, Signaling unobservable product quality through a Brand Ally, Journal of Marketing Research 36(2) (1999) 258-268.

[13] E. J. Johnson, W. W. Moe, P. S. Fader, S. Bellman, G. L. Lohse, On the depth and dynamics of online search behavior, Management Science 50(3) (2004) 299-308.

[14] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Information Systems Research 19(3) (2008) 291-313.

[15] S. Li, K. Srinivasan, B. Sun, Internet auction features as quality signals, Journal of

[16] M. X. Li, K. K. Wei, C. K. Tayi, C. H. Tan, The moderating role of information load on online product presentation, Information & Management 53(4) (2016) 467-480.

[17] D. Proserpio, G. Zervas, Online reputation management: Estimating the impact of management responses on consumer reviews, Marketing Science 36(5) (2017) 645-665.

[18] S. D. Tsolakis, C. Cridland, H. E. Haralambides, Econometric modelling of second-hand ship prices, Maritime Economics & Logistics 5(4) (2003) 347-377.

[19] V. M. Thomas, Demand and Dematerialization Impacts of Second-Hand Markets, Journal of Industrial Ecology 7(2) (2003) 65-78.

[20] L. L. M. Turunen, H. Leipämaa-Leskinen, Pre-loved luxury: identifying the meanings of second-hand luxury possessions, Journal of Product & Brand Management 24(1) (2015) 57-65.

[21] A. Jøsang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decision Support Systems 43(2) (2007) 618-644.

[22] K. Jones, L. N. Leonard, Trust in consumer-to-consumer electronic commerce, Information & Management 45(2) (2008) 88-95.

[23] X. Hui, M. Saeedi, Z. Shen, N. Sundaresan, Reputation and regulations: evidence from eBay, Management Science 62(12) (2016) 3604-3616.

[24] C. Dellarocas, The digitization of word of mouth: promise and challenges of online feedback mechanisms, Management Science 49(10) (2003) 1407-1424.

[25] F. Wu, H. H. Li, Y. H. Kuo, Reputation evaluation for choosing a trustworthy counterparty in C2C e-commerce, Electronic Commerce Research and Applications 10(4) (2011) 428-436.

[26] Z. Wang, H. Li, Q. Ye, R. Law, Saliency effects of online reviews embedded in the description on sales: Moderating role of reputation, Decision Support Systems 87 (2016)

[27] F. Dini, G. Spagnolo, Buying reputation on eBay: do recent changes help? International Journal of Electronic Business 7(6) (2009) 581–598.

[28] S. S. Standifird, Reputation and e-commerce: eBay auctions and the asymmetrical impact of positive and negative ratings, Journal of Management 27(3) (2001) 279-295.

[29] Y. Zhang, J. Bian, W.Zhu, Trust fraud: A crucial challenge for China’s e-commerce market, Electronic Commerce Research and Applications 12(5) (2013) 299-308.

[30] G. Acampora, D. Alghazzawi, H. Hagras, A. Vitiello, An interval type-2 fuzzy logic based framework for reputation management in Peer-to-Peer e-commerce, Information Sciences 333 (2016) 88- 107.

[31] Y. Yang, R. Sun, S. Kay, Q. Yang, Defending online reputation systems against collaborative unfair raters through signal modeling and trust, Proceedings of the 24th Annual Symposium on Applied Computing 2009, pp. 1308–1315.

[32] W. Boulding, A. Kirmani, A consumer-side experimental examination of signaling theory: do consumers perceive warranties as signals of quality? Journal of Consumer Research 20(1) (1993) 111-123.

[33] F. Ali, E. K. Kim, Y. G. Kim, Type-2 fuzzy ontology-based opinion mining and information extraction: A proposal to automate the hotel reservation system, Applied Intelligence 42(3) (2015) 481-500.

[34] F. Ali, E. K. Kim, Y. G. Kim, Type-2 fuzzy ontology-based semantic knowledge for collision avoidance of autonomous underwater vehicles, Information Sciences 295 (2015)

[35] A. C. Bukhari, Y. G. Kim, A research on an intelligent multipurpose fuzzy semantic enhanced 3D virtual reality simulator for complex maritime missions, Applied intelligence 38(2) (2013) 193-209.

[36] E. Xamena, N. B. Brignole, A. G. Maguitman, A structural analysis of topic ontologies, Information Sciences 421 (2017) 15-29.

[37] T. Narock, L. Zhou, V. Yoon, Semantic similarity of ontology instances using polarity mining, Journal of the Association for Information Science and Technology 64(2) (2013) 416-427.

[38] L. Zhao, C. Li, Ontology Based Opinion Mining for Movie, Proceedings of the Third International Conference on Knowledge Science, Engineering and Management (KSEM) 2009, 5914, pp.204

[39] F. Ali, D. Kwak, P. Khan, S. R. Islam, K. H. Kim, K. S. Kwak, Fuzzy ontology-based sentiment analysis of transportation and city feature reviews for safe traveling, Transportation Research Part C: Emerging Technologies 77 (2017) 33-48.

[40] D. Dubois, H. Prade, H, Rough fuzzy sets and fuzzy rough sets, International Journal of General System 17(2-3) (1990) 191-209.

[41] R. Y. Lau, C. Li, S. S. Liao, Social analytics: learning fuzzy product ontologies for aspect-oriented sentiment analysis, Decision Support Systems 65 (2014) 80-94.

[42] N. Sanchez-Pi, L. Martí, A. C. B. Garcia, Improving ontology-based text classification: An occupational health and security application, Journal of Applied Logic 17 (2016) 48-58.

[43] M. Chmielewski, P. Stąpor, Medical data unification using ontology-based semantic model structural analysis, Proceedings of 36th International Conference on Information Systems Architecture and Technology 2015, pp.139-151.

[44] C.F. Tsai, Y.C. Hsiao, Combining multiple feature selection methods for stock prediction: union, intersection, and multi-intersection approaches, Decision Support Systems 50 (1) (2010) 258–269.

[45] Y. Lu, C. Zhai, Opinion integration through semi-supervised topic modeling, Proceedings of the 17th International Conference on World Wide Web 2008, pp. 121–130.

[46] R. Xia, C. Zong, S. Li, Ensemble of feature sets and classification algorithms for sentiment classification, Information Sciences 181(6) (2011) 1138-1152.

[47] M. Tahir, A. Khan, Protein subcellular localization of fluorescence microscopy images: Employing new statistical and Texton based image features and SVM based ensemble classification, Information Sciences 345 (2016) 65-80.

[48] L. Breiman, Random forests, Machine Learning 45(1) (2001) 5-32.

[49] S. Cang, H. Yu, Mutual information based input feature selection for classification problems, Decision Support Systems 54 (1) (2012) 691–698.

[50] D. M. Blei, A. Y. Ng, M. I. Jordan, Latent Dirichlet allocation, The Journal of Machine Learning Research 3 (2003) 993-1022.

[51] T. L. Griffiths, M. Steyvers, Finding scientific topics, Proceedings of the National Academy of Sciences 101(suppl 1) (2004) 5228-5235.

[52] T. Wang, Y. Cai, H. F. Leung, R. Y. Lau, Q. Li, H. Min, Product topic extraction supervised with online domain knowledge, Knowledge-Based Systems 71 (2014) 86-100.

[53] Z. Li, W. Xu, L. Zhang, R. Y. Lau, An ontology-based Web mining method for unemployment rate prediction, Decision Support Systems 66 (2014) 114-122.

[54] J. A. Morente-Molinera, R. Wikström, E. Herrera-Viedma, C. Carlsson, A linguistic mobile decision support system based on fuzzy ontology to facilitate knowledge mobilization, Decision Support Systems 81 (2016) 66-75.

[55] T. Narock, L. Zhou, V. Yoon, V. Semantic, Similarity of ontology instances using polarity mining, Journal of the American Society for Information Science and Technology 64(2) (2013) 416-427.

[56] R. Y. Chen, W. Xu, The determinants of online customer ratings: a combined domain ontology and topic text analytics approach, Electronic Commerce Research 17 (2017) 31-50.

[57] K. P. Murphy, Machine Learning: A Probabilistic Perspective, MIT Press, 2012.

[58] I. Rish, An empirical study of the naive Bayes classifier, Proceedings of IJCAI 2001 workshop on empirical methods in artificial intelligence 2001 pp. 41-46.

[59] T. Joachims, Making large scale SVM learning practical, Universität Dortmund, 1999.

[60] K. Hornik, M. Stinchcombe, H. White, Multilayer feedforward networks are universal approximators, Neural Networks 2(5) (1989) 359-366.

## Biographical Note

Mr. Chen is a PhD student at School of Information, Renmin University of China. He got his bachelor degree in Telecommunications Engineering with Management at International School, Beijing University of Posts and Telecommunications. His research interests include big data analytics, business intelligence and decision support systems. He has published several papers in international journals and conferences, such as Electronic Commerce Research.

Ms. Zheng is a master student at School of Information, Renmin University of China. Her interests include big data analytics, business intelligence and decision support systems.

Dr. Xu is an associate professor at School of Information, Renmin University of China. He is a research fellow at Department of Information Systems, City University of Hong Kong. He got his bachelor and master degree in Mathematics at Xi’an Jiaotong University and doctor degree in Management Science at Chinese Academy of Sciences. His research interests include big data analytics, business intelligence and decision support systems. He has published over 90 research papers in international journals and conferences, such as Annals of Operations Research, Decision Support Systems, Electronic Commerce Research, European Journal of Operational Research, IEEE Trans. Systems, Man and Cybernetics, International Journal of Production Economics, and Production and Operations Management.

Mr. Liu is a master student at School of Information, Renmin University of China. His interests include big data analytics, business intelligence and decision support systems.

Ms. Wang is an undergraduate student at School of Information, Renmin University of China. Her interests include big data analytics, business intelligence and decision support systems.

## Highlights

1 We propose a text analytics framework for secondhand sellers’ reputation assessment;

2 We design a novel aspect-extraction method that combines domain ontology and topic modeling;

3 Our research contributes to advance the assessment method for secondhand sellers’ reputation;

4 Our research results can support a more effective development of online secondhand markets.
