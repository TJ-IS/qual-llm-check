---
otero_id: 19948
otero_key: "M7P7UHQR"
title: "Combining review-based collaborative filtering and matrix factorization: A solution to rating's sparsity problem"
authors: "Rui Duan; Cuiqing Jiang; Hemant K. Jain"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113748"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Combining review-based collaborative filtering and matrix factorization: A solution to rating's sparsity problem

![](/api/attachments/M7P7UHQR/fulltext/images/521479604ef117e120cb840235fe548f83944b5b30cec6078f3f53d2045d4632.jpg)

Rui Duan <sup>a</sup>, Cuiqing Jiang <sup>b,\*</sup>, Hemant K. Jain <sup>c</sup>

<sup>a</sup> School of Tourism Sciences, Beijing International Studies University, Beijing, China

<sup>b</sup> School of Management, Hefei University of Technology, Hefei, China

<sup>c</sup> Gary W. Rollins College of Business, The University of Tennessee at Chattanooga, USA

## A R T I C L E I N F O

Keywords: Collaborative filtering Sparsity problem Online reviews Matrix factorization Rating imputation

## A B S T R A C T

An important factor affecting the performance of collaborative filtering for recommendation systems is the sparsity of the rating matrix caused by insufficient rating data. Improving the recommendation model and introducing side information are two main research approaches to address the problem. We combine these two approaches and propose the Review-Based Matrix Factorization method in this paper. The method consists of two phases. The first phase is review-based collaborative filtering, where an item-topic rating matrix is constructed by the feature-level opinion mining of online review text. This rating matrix is used to derive item similarities which can be used to infer unknown users' ratings of the items. The second phase consists of rating imputation, where we first fill some of the empty elements of the user-item rating matrix, then conduct matrix factorization to learn the latent user and item factors to generate recommendations. Experiments on two actual datasets show that our method improves the accuracy of recommendation compared with similar algorithms.

## 1. Introduction

Personalized recommendation helps users select products or services based on their interest and preferences [2]. Since recommender systems are an important means to address the problem of information overload [36] and are conducive to stimulating sales, promoting bundling, and further improving customer satisfaction [35], they are widely available on the Web [37]. There are three basic techniques for arriving at rec ommendations: collaborative filtering [21], content-based filtering [26], and a hybrid technique [4] that combines the characteristics of the previous two.

Collaborative filtering, a widely used recommendation technique, predicts an active user's preferences and uses the similarity between different users' preferences to make recommendations [55]. A funda mental assumption of this approach is that if two users have rated some items similarly, or they have similar behavior (e.g., browsing history), they will have similar preferences on other items. The user-item rating matrix, in which ratings provided by a user on different items are used to represent the user's preferences, is the key data source of classical collaborative filtering [5,10]. For example, we can convert users' ratings of various movies into a rating matrix, as shown in Table 1. In this example, four users (Emma, Olivia, Isabella, Sophia) assign different ratings to five movies (Avatar, Zootopia, Dune, Titanic, Flipped), except Sophia has not seen the movie Flipped. Then, treating Sophia as the target user, we can predict her rating of the movie Flipped by computing the similarities of her preferences (ratings) to those of the other three users on the other four movies, and then determine if the movie Flipped should be recommended to her.

Collaborative filtering models are simple and easy to use, so in practice, the recommender systems of many large commercial sites like Amazon.com and Netflix.com are based on collaborative-filtering. However, collaborative filtering suffers from the sparsity issue [23], which refers to that there is not enough feedback data to make a reliable prediction of the similarities between users or items. This problem is widespread in large commercial recommendation systems, since the number of items is very large. Take Netflix as an example. Although we are unable to obtain the current sparsity of its recommendation system, according to records by Koren, Bell, and Volinsky [33], in the recom mendation system competition held by Netflix in 2006, the real dataset from its website contained 100 million ratings scattering among 500,000 users and 17,000 movies, and the sparsity of this dataset reached 98.82%; that is, 98.82% of the elements in the rating matrix were missing.

Model-based collaborative filtering [54] and hybrid collaborative filtering [9] are two main approaches suggested to improve the tradi tional memory-based collaborative filtering. Model-based collaborative filtering uses the rating data to train a model to make a prediction. Matrix factorization is a widely used technique to alleviate the sparsity issue in model-based collaborative filtering [33]. This technique learns the latent user and item factors and removes uncharacteristic elements resulting in much lower dimensionalities than the original user-item rating matrix [55]. Again taking movie recommendation as an example, if we conduct matrix factorization on a user-item rating matrix, both users and items are mapped into a joint latent factor space of lower dimensionality. These latent factors may correspond to a movie's genres, styles, cast and crew, director, and so on, but they are not an explicit correspondence, and there may be less well-defined and completely uninterpretable factors. As a result, a movie rating can be modeled as the dot product of an item vector and a user vector, where the former measures the extent to which the movie possesses these factors, and the latter represents the user's preferences for these factors. Nevertheless, this method may still suffer from overfitting problems if there is a high percent of empty ratings [33].

Table 1  
An example of a user-item rating matrix.

<table><tr><td></td><td>Avatar</td><td>Zootopia</td><td>Dune</td><td>Titanic</td><td>Flipped</td></tr><tr><td>Emma</td><td>3</td><td></td><td>2</td><td>4</td><td>5</td></tr><tr><td>Olivia</td><td></td><td>3</td><td></td><td>5</td><td>5</td></tr><tr><td>Isabella</td><td>4</td><td></td><td>5</td><td></td><td>3</td></tr><tr><td>Sophia</td><td>3</td><td>5</td><td></td><td>5</td><td>?</td></tr></table>

The hybrid collaborative filtering algorithms, such as the contentbased collaborative filtering algorithm [44], use the content informa tion to enhance collaborative filtering. For example, in movie recom mendation, the movie posters and trailers can enrich the item profile, and a user's tags and comments on the movie can provide his/her preferences, which play an important role in collaborative filtering. The auxiliary information of items or users is used when sufficient rating data to support traditional collaborative filtering models is not avail able. Auxiliary information, such as product specifications [54] and user-generated tags [32,43] have been used to augment the information provided by the user-item rating matrix and improve recommendation accuracy. Additionally, textual reviews have increasingly been used in review-based recommendation algorithms [6]. Compared to the nu merical ratings, which indicate only if a user likes or dislikes a product, the textual reviews can provide information on why she/he likes or dislikes the product based on her/his usage experiences. Textual reviews allow the consumers to provide multi-faceted opinions on the products, that is, feature-level opinions. These multi-faceted opinions are helpful to build more comprehensive user and item profiles and can help alle viate the problems caused by insufficient rating data [6]. For the user profiles, the textual reviews can be used to create term-based profiles [15], to infer or enhance numerical ratings [56], and most importantly, to derive the weights/preferences that the user places on the product features [7]. For the item profiles, the textual reviews can be used to enrich the item description, since the feature-level opinions reflect an assessment of the quality of the items [1]. Although textual reviews are treated as increasingly important auxiliary data to alleviate the sparsity problem, the use of textual reviews is still limited to profiling a user and items [1,15], or to eliciting a user's preferences for different item char acteristics [7,40]. Few researchers have focused on how to blend textual reviews into the matrix factorization model, combining content- and model-based recommendation to provide an integrated hybrid recom mendation framework.

In this paper, a recommendation method called Review-Based Matrix Factorization (RMF), which combines review-based hybrid collabora tive filtering and matrix factorization, is proposed to address the sparsity problem. The method has two phases. Phase I starts with review-based hybrid collaborative filtering. The product features and consumer's feature-level opinions are extracted by sentiment analysis. The itemtopic rating matrix is then built by topic modeling and sentiment quantification, which is used to infer the unknown users' ratings. Phase II focuses on rating imputation and matrix factorization based on the predicted ratings from Phase I to generate the recommendation. The contributions of this paper include the following: (1) The proposed method helps to solve the overfitting problem of matrix factorization when rating data is extremely sparse. (2) The RMF framework gives a clear path on how to use review text in collaborative filtering, that is, based on feature-level sentiment analysis of reviews and rating impu tation, which further explores the value of comment text in the recom mendation system. (3) The proposed solution optimizes the recommendation system from the two perspectives of the model (matrix factorization) and data (textual reviews), and effectively improves the accuracy of recommendation; it is in accordance with the optimization direction of the commercial recommendation system [54], and thus has clear application value in product promotion.

We arrange the rest of the paper as follows. In Section 2, the related previous research work is discussed. The framework of our method is presented in Section 3. Section 4 describes the proposed review-based matrix factorization approach. In Section 5, we present the results of experiments conducted using our model and benchmark methods using two real-world datasets. The conclusion, limitations and future research are presented in Section 6.

## 2. Related work

The sparsity problem can be alleviated from two perspectives: model and data. The former tries to optimize the recommendation model to fit the sparse environment, which mainly includes the improvement of the similarity calculation and various types of model-based algorithms; the latter relies on the introduction of different kinds of auxiliary data to compensate for the original rating data's sparsity – online reviews are one of the most valuable types of auxiliary data. In Section 2.1, we re view the related research on solving the sparsity problem by improving the recommendation model. Section 2.2 discusses different types of auxiliary data that are used in recommendation systems, especially focusing on the use of textual reviews.

## 2.1. Model perspective: adapting to the sparse environment

Since traditional similarity measures consider only co-rated items. data sparsity seriously affects the accuracy of a similarity calculation in collaborative filtering. In a sparsity situation, co-rated items between different users are almost non-existent. Thus, a solution to the sparsity problem is to improve the calculation of similarity between users or items. Hu, Shi, Li, and Hu [22] break the restriction that two users' similarity can be computed only when they have co-rated items. They utilize the similar items purchased to compute the implicit user simi larity measure. Based on this, the user similarity is measured by tradi tional explicit similarity (co-rated items) and the proposed implicit similarity (similar items). Similarly, the item similarity measure can be computed, and both measures can enhance each other. In [62], the item similarity is used as a weight in the user similarity computation. The item similarity is measured by using ratings as a sample sequence of discrete distribution and computing the similarity between two se quences based on Kullback-Leibler divergence. Patra, Launonen, Olli kainen, and Nandi [48] adopt a similar strategy to compute the similarity between users without co-rated items. The only difference is that they use the Bhattacharyya measure to get the item similarity. Suryakant and Mahara [57] compute the similarity between users without co-rated items by using the mean measure of divergence (MMD). A benefit of the MMD is that it takes a user's rating habits into account. The MMD is combined with the cosine similarity and Jaccard similarity to arrive at a hybrid user similarity.

In addition to improving the computation of similarity, many studies have focused on developing effective models to avoid the negative ef fects of sparse ratings. Considering the sparsity of ratings, Guan [18] develops a regression model in which the rating is treated as a prediction and the item features as independent variables, and the estimated co efficients of the independent variables represent the weight. Thus, based on the feature-rating vector, user similarity can be derived even when the ratings are missing. Dimensionality reduction is a feasible and important approach to alleviate the sparsity problem. Nilashi, Ibrahim, and Bagherifard [46] use three common types of dimensionality reduction method in their study of users' movie preferences: clustering, ontology, and singular vector decomposition. They first conduct expectation maximization clustering on users and items, considering both content-based features and user rating data. This results in fewer users and items compared to the original rating matrix. Next, for each cluster, they design the semantic similarity measures based on the movie ontology repository. Using the ontology, the same movie genres can be merged to reduce the dimensionality. At last, they perform singular vector decomposition on the clustering matrix to decompose the original matrix into three matrices representing user, item, and singular values. This can greatly reduce the matrix dimensions.

The latent factor model is another approach to solve the sparsity problem. Matrix factorization, a widely used latent factor model, finds latent user and item factors by factorizing the rating matrix. Matrix factorization is helpful in alleviating the sparsity problem because it represents the user and item in a lower-dimensional latent space; therefore, in essence, matrix factorization is also a method of dimen sionality reduction. Further improvements to matrix factorization techniques include non-negative matrix factorization, probabilistic matrix factorization, and social matrix factorization. Jing, Wang, and Yang [30] focus on two key issues in probabilistic matrix factorization: sparsity and the long tail distribution. Considering the Laplacian dis tribution can fit the sparse points and has a heavy tail, they model the latent user and item factors as Laplacian distribution, which are bene ficial to find latent factors and recommend the tail items. Yang, Chen, and Huang [63] improve the non-negative matrix factorization algo rithm by creating blocks in the sparse rating matrix. They consider the coupling between blocks and impose consistency and homophily regu lation constraints when decomposing the matrix. Chen, Hua, Gao, and Xing [8] combines the user's social status and the item similarity to enhance the social matrix factorization. The proposed method uses the trust relationship between users and the rated items to train the model. It can avoid inaccurate predictions due to sparse ratings.

The idea of latent factor models can also be implemented by deep learning techniques. Lee, Kim, Park, and Xie [34] propose a deep learning-based method to infer the missing ratings. They analyze the process of rating generation from the perspective of user preferences and hypothesize that users' post-use preferences (ratings) is influenced by their pre-use preferences. The proposed method utilizes the variational autoencoder to learn the pre-use preferences from the observed ratings as well as to extract the latent factors that reflect user preferences and item characteristics. At last, they learn the parameters by multi-layer perceptron and predict unknown ratings based on the extracted latent factors. He and Chua [20] propose the Neural Factorization Machine for rating prediction in a sparse environment. The Neural Factorization Machine model takes advantage of the deep neural networks in modeling the non-linear feature interaction and considers the linearity of the factorization machine.

From the above literature review, it is clear that the latent factor model represented by matrix factorization has become the mainstream in the model improvement approach. However, matrix factorization is not a panacea for the sparse environment – as the rating matrix becomes increasingly sparse, the overfitting problem of matrix factorization will become more pronounced [33]. In this paper, we tackle this issue by rating imputation, which avoids conducting matrix factorization on data with a high degree of sparsity.

## 2.2. Data perspective: using textual reviews to mitigate data sparsity

Besides improving the similarity calculation and developing different prediction models, various types of auxiliary information are used to mitigate the sparsity of ratings, like homogeneous data that have the same scale as the observed ratings [29], item ontology [59], user demographics [19], check-in data [14], tag data [41,60], and contextual information [18,45,61,64]. This auxiliary information is combined with original ratings using different techniques and models such as transfer learning [29], clustering [19], and word embedding [41]. Among the varied auxiliary information, textual reviews have caught the attention of researchers because plentiful information on item characteristics and user preferences is available in the reviews.

Most e-commerce sites allow and encourage users to provide reviews after shopping. Some specialized websites, called word-of-mouth sites, focus on collecting user reviews. Thus, there exist many online reviews on the Web. Since online textual reviews contain users' opinions and pref erences, text mining techniques like topic modeling [3], feature extrac tion, and sentiment analysis [16,47] can be used for extracting the topics, features of items, and opinions of users from online reviews. These can then be used for making personalized recommendations. Aciar et al. [1] were first to introduce textual reviews into the field of recommendation. They use reviews to model items and make recommendations for product like camera. They model a camera from two aspects using ontologies: the review quality, which measures reviewers' experience and professional level, and the product quality, as determined by users' opinions on various camera features. At last, they match the user preferences and the item profile to generate recommendation results.

Online reviews can be used to elicit a consumer's preferences. Chen and Wang [7] extract users' preferences for different features from textual reviews as the reviewer-level preference; then, they get users' preference homogeneity, which is called the cluster-level preference, using the latent class regression model. For making the recommendation to the user, they look for the cluster with the most related users based on the degree of matching of the preferences and use the products those users have com mented on to generate recommendation candidates. Liu, He, Wang, Song, and Du [40] first conduct the sentiment analysis to extract product fea tures and user opinions from textual reviews. Then they identify a user's preference by analyzing the differences between the numerical ratings and the user's opinions. Finally, the recommendations are generated based on the user's preferences and the product feature model.

Jiang et al. [28] propose a hybrid collaborative filtering method based on online reviews for high-involvement products, to address the sparsity and dynamics problem. Even though this paper addressed the sparsity issue, it paid more attention to the issue of the dynamics of numerical ratings and textual reviews. To confirm the existence of dynamics and eliminate its influence on the recommendation effect, they use empirical study like regression analysis, and algorithm design like dynamics simi larity calculation, both of which differ from the present study. Additionally, Jiang et al. [28] blend online reviews into traditional user-based collabo rative filtering, while in this current study, we go further and try to inte grate the review text into matrix factorization, addressing the over-fitting problem of matrix factorization in an extremely sparse environment. Thus, the current study makes more-innovative attempts to address sparsity.

Recently, the review-based recommender systems are increasingly using deep learning techniques. Zheng, Noroozi, and Yu [65] propose a deep learning model consisting of two parallel neural networks to learn item properties and user behaviors jointly from textual reviews. The online reviews are organized as written by a user or written for an item. Then they introduce a shared layer to couple the two neural network together, like the factorization machine. In [66], the recommendation is divided into two steps: generating and ranking the candidates. In the first step, the convolutional matrix factorization is used to learn the latent user and item feature vectors with low ranks. Then, candidate ranking is performed via a three-layer denoising autoencoder. Guan, Wei, and Chen [17] take multiple sources of information including online reviews, metadata, and images into consideration and use stacked auto-encoder net works to map these multi-modality data into a unified latent space. Then, they add a layer to represent the user's heterogeneous preferences and model the interaction between the user's and item's latent factors.

Although there is an increasing trend of review-based recommen dation, most of the previous work is content-based; that is, the content of textual reviews is extracted to make a direct match between the items' characteristics and users' preferences. There is a lack of research on the application of review texts in model-based collaborative filtering, especially on blending reviews into a matrix factorization framework, which is expected to achieve a better recommendation performance than using either of them alone. In this paper, we propose an integrated framework combining matrix factorization and review-based recom mendation and optimize the recommendation system from the per spectives of the model (matrix factorization) and data (textual reviews).

## 3. Problem definition and research framework

We first define some important concepts, mainly from the field of feature-level sentiment analysis and topic modeling, that are used in developing the research framework. In the field of sentiment analysis, the concept of entity is used to represent the object that the user com ments on [38]. The entity can be any product or service. Each entity consists of components, sub-components, and attributes, forming a hi erarchy. In the field of recommender systems, each entity is called an item. Identifying a comprehensive and hierarchical entity is a difficult task and unnecessary in most cases [38]. So, the concept of a feature is proposed to simplify the entity tree and flatten it into two levels. The formal definition of concepts used in this paper are provided below:

• Entity: An entity e is the object that users comment on. It is associated with a pair, $e : ( T , W ) ,$ , where T is a hierarchy of components, subcomponents, and parts, and W is a set of attributes of e. Each component or sub-component also has its own set of attributes.

• Feature: All the components and sub-components (T) of the entity and their attributes (W) are jointly referred to as features. The feature is denoted by f, and corresponds with the feature words in the review text.

• Opinion: An opinion is user's negative or positive sentiment to a feature of an entity or the entity itself in review text. The opinion is denoted by o, and corresponds with the opinion words in the review text.

• Feature-Opinion Pair: A feature-opinion pair consists of the entity's one feature and its corresponding opinion.

• Sentiment Polarity: A feature-opinion pair's sentiment polarity refers to the positive or negative opinion orientation which the pair implies.

• Sentiment Strength: A feature-opinion pair's sentiment strength represents the opinion's quantitative intensity. The sentiment strength of user u to item i’s feature f is denoted as $s _ { u i f } .$ . The sentiment strength is measured on a continuous scale from 1 to 5. We discuss it further in Section 4.1.1.

• Feature Quality: Given a feature f of the item i, the feature quality $q _ { i f }$ is a rating of this feature that users assess. It is computed by aver aging the opinions of different reviewers on this feature, that is,

$$
q _ {i f} = \sum_ {u \in R} S _ {u i f}\tag{1}
$$

where R is the set of reviewers. Since the sentiment strength is measured on a scale of 1 to $^ { 5 , }$ the feature quality ranges from 1 to 5.

• Topic: The topic describes the product at a higher level than features. It contains several features that can be represented as

$$
t = \left(f _ {1}, f _ {2}, \dots , f _ {n}\right)\tag{2}
$$

It is extracted from text by the topic modeling method. The topic describes the product in the abstract, not by a specific component or attribute; for example, it describes the product's hardware but not specifically the screen or battery.

The proposed recommendation approach is based on multi-attribute utility theory [31] and the principle of item-based collaborative filtering [52]. According to multi-attribute utility theory, a product has multiple features; and the feature qualities of different products are usually different. For example, laptop A has a higher screen resolution (feature) but poor battery life (another feature), while laptop B has a lower screen resolution but better battery life. As revealed by the multi-attribute utility theory, the product's utility function for a user can be computed as,

$$
\operatorname{MAU} \left(q _ {i 1}, \dots , q _ {i n}\right) = \sum_ {f = 1} ^ {n} w _ {u f} \times q _ {i f}\tag{3}
$$

where n is the number of features, $q _ { i f }$ is the quality of feature f for item i, $w _ { u f }$ is the user u’s weight/preference for feature $f ,$ and ${ \Sigma _ { f = 1 } } ^ { n } w _ { u f } = 1 ( 0 \le$ $w _ { u f } \leq 1 _ { : }$ , for all f).

When a consumer makes a purchase decision, he (or she) implicitly calculates the utility of every alternative using the above multi-attribute utility function and selects the one with highest utility. In the field of multi-attribute decision making, many preference elicitation methods are proposed to model a consumer's multi-attribute utility function. In the area of review-based recommender systems, some researchers have focused on eliciting the users' preferences from online reviews. The representative works in this field are [7], in which the researchers learn users' preferences from online reviews. The derived preferences are used to compute users' similarities in line with the paradigm of user-based collaborative filtering. In contrast with their approach, we use online reviews for an item-based collaborative filtering. From all users' opinions on an item's different features, the features' quality $q _ { i f } ( f = 1 , . . . , n )$ is derived. Based on the features' quality, we construct a new measure, topic rating, and establish the similarities between items by computing the cosine values of the items' topic rating vectors. In contrast with [7], we do not need to represent users' preferences explicitly. We predict an un known item's rating of a user based on its similarities with other items and his (or her) prior ratings of these items, which is the fundamental prin ciple of item-based collaborative filtering. Thus, the unknown ratings in the user-item rating matrix can be preliminarily inferred. After the rating imputation process for the original rating matrix, we perform matrix factorization on the filled matrix to obtain the recommendation results.

The above designed method, called Review-Based Matrix Factor ization (RMF), can alleviate the sparsity problem of collaborative filtering because of rating imputation and matrix factorization. The research framework of RMF is illustrated as Fig. 1. Our method consists of two phases:

• Phase I: Review-Based Hybrid Collaborative Filtering. We first get product feature and opinion words from online reviews by per forming feature-level sentiment analysis; then, we reduce the feature dimension by clustering them into topics and compute the topic ratings in terms of users' opinions; finally, we construct the itemtopic rating matrix based on these ratings. We compute item simi larities using this matrix and predict the unknown ratings in useritem matrix.

• Phase II: Rating Imputation and Matrix Factorization. After pre dicting unknown user ratings on items in Phase I, we fill these ratings into the sparse user-item rating matrix. This rating imputation pro cess can help alleviate the rating sparseness. Then matrix factoriza tion is performed on the filled user-item rating matrix.

![](/api/attachments/M7P7UHQR/fulltext/images/514f8faec0ddbe76fb9882c67a3be3f5d541f939cbeca8cc9796d78978e8ae33.jpg)  
Fig. 1. Research framework of Review-Based Matrix Factorization (RMF); CF, collaborative filtering.

## 4. The proposed RMF method

## 4.1. Feature-level opinion mining

## 4.1.1. Extraction of feature-opinion pairs for products

As discussed by Liu [39] and Pang and Lee [47], there is a mature technical solution for the process of extracting feature-opinion pairs based on feature-level sentiment analysis (also called aspect-based opinion mining). The process can be divided into three steps: feature extraction, opinion word identification, and mapping the opinion to its corresponding feature. We start with feature extraction, which consists of the three sub steps of identifying feature candidates, feature words, and features.

In a study, Pang and Lee [47] have shown that the features of items mainly exist in some high-frequency nouns (including noun phrases and verbal nouns). Therefore, we first extract high-frequency nouns as feature candidates. To do this, we tag the words in online reviews by part of speech, collect the nouns, and count the frequency of the nouns. The Core-NLP package [42] provides a part-of-speech tagger to achieve this goal. The above process of identifying the feature candidates is unsupervised. However, not all high-frequency nouns are item features. Given that the unsupervised method typically returns lower identification precision, we adopted a more supervised method that is dictionary-based. Dictionaries are widely used in the field of text mining, and there are many welldefined domain dictionaries, for example, HowNet [13] and Senti wordNet [53]. To collect the feature seeds for our dataset, we use a summary of the pros and cons of each product based on user reviews provided by the review site. We then supplement these seeds by manually adding some other important missing seeds. This ensures that we get a well-defined set of feature seeds, which is critical to feature identification.

After defining the feature seeds, we compute the semantic similar ities (by using the point mutual information value [11]) of the feature candidates with feature seeds and filter out the less relevant candidate features to get feature words. Then, feature words with similar seman tics, such as image, photo, or picture for the feature image, are grouped to identify a feature.

The next two steps are to identify opinion words and map the opinion to its corresponding feature. The opinion words are used to describe the entity's features or the entity itself. If we treat the entity as a feature called “General,” then we can directly say that the opinion words are dependent on the feature words. Even though the definition of opinion is succinct, in reality, there are several kinds of opinions, for example, explicit versus implicit opinions, contextual opinions, and comparative opinions [38]. These different types of opinions are helpful in modeling the user or product profiles. However, it is technically complex and time-consuming to exactly identify different kinds of opinions. So, in this paper, we identify only the explicit opinions on the product features.

There exist two types of feature opinion extraction methods, namely supervised and unsupervised [51]. The lexicon-based method is one of the most common supervised method [12]. The lexicon-based method locates the opinion words in a sentence by matching every word with those from the lexicon, and then determines the opinion orientation and strength as implied by the lexicon. The advantage of lexicon-based method is its simplicity; however, because users express their opinions in varied words and phrases, this method is not sufficient in many cases. The other type of identification method is unsupervised, the type adopted by many review-based recommender systems [40,56]. The most widely used unsupervised method is based on the syntactic dependency relationship between opinion words and feature words, which was proposed in [50]. In this method, the syntactic dependency relations are first extracted; then the opinion words are identified by the specific dependency relations between opinion words and feature words.

In this paper, we leverage the syntactic dependency parser provided by the Stanford NLP Group [42]. It can return the syntactic dependency relationship between words in a sentence. It is typically used to identify three common dependency relationships between opinion and feature words:

• AMOD indicates that the opinion word is an adjectival modifier of the noun feature word. For example, consider the sentence “This camera takes great photos.” After parsing this sentence, “great” is identified with dependency relationship AMOD with “photos.”

• COMP indicates an open clausal complement. For example, consider the sentence “This camera is easy to use.” In this sentence, “easy” has a COMP dependency relationship with “use.”

• NSUBJ indicates that the feature word is the subject of the opinion word. In the example “The photos are great,” “great” has an NSUBJ relationship with “photos.”

After identifying the opinion words, we need to assess the opinion words' sentiment strength. We quantify the sentiment strength on a fivepoint scale. A score of three represents a neutral sentiment. A score of greater than three represents a positive sentiment, and a score of less than three means a negative sentiment. We used the SentiWordNet [53] to quantify the sentiment strength of the opinion words. SentiWordNet quantifies each opinion o from three aspects: positivity, negativity, and objectivity. It assigns triple polarity scores, denoted as Pos(o), Neg(o), and Obj(o), to each opinion word. The following constraint needs to be met:

$$
\operatorname{Pos} (o) + \operatorname{Neg} (o) + \operatorname{Obj} (o) = 1, 0 \leq \operatorname{Pos} (o), \operatorname{Neg} (o), \operatorname{Obj} (o) \leq 1\tag{4}
$$

Then the sentiment strength value S(o) is computed by weighted average of the triple polarity scores:

$$
S (o) = \operatorname{Neg} (o) \times R _ {\min} + \operatorname{Pos} (o) \times R _ {\max} + \operatorname{Obj} (o) \times \frac {R _ {\max} + R _ {\min}}{2}\tag{5}
$$

where $R _ { m a x } = 5$ and $R _ { m i n } = 1$ are the maximum and minimum value of sentiment strength, respectively.

## 4.1.2. Topic modeling

After aggregating different feature words into the feature, we may still find that some features describe the same aspect of the product; for example, shutter, shot, screen, battery, flash, and so on all relate to the hardware, whereas usefulness, flexibility, and portability relate to the performance. So a higher-level concept called topic that describes the product at a level higher than a feature is defined. The advantages of introducing the topic concept are (1) it helps to classify the extracted features, and (2) it decreases the complexity by reducing the dimen sionality of the rating matrix. Since rating matrix can be built by clus tering the feature into topics.

Methods for topic modeling can be classified as manual, semiautomatic, and automatic [24]. In the manual approach, the features are grouped into topics manually based on the features' semantics and certain classification criteria. The manual approach is usually very time consuming. In the semi-automatic approach, several topics are deter mined manually, and then features are put into these predetermined topics by computing the semantic relationship between features and topics. The automatic approach performs the clustering by using algo rithms like Latent Dirichlet Allocation [3], which we use in this paper to identify the topics in the review text.

## 4.2. Construction of item-topic rating matrix

An item can be profiled by its topics and the corresponding ratings, we first derive the item's feature qualities, also called feature ratings, based on the user's opinion strength. The feature quality is computed by averaging the opinions of different reviewers on a feature. If we denote the feature rating as $r _ { i f }$ where i represents the item and f represents the feature, then

$$
r _ {i f} = q _ {i f} = \sum_ {u \in R} S _ {u i f}\tag{6}
$$

where $q _ { i f }$ is the feature quality, R is the reviewer set, and $\boldsymbol { S } _ { u i f }$ is the user u’s sentiment strength of feature f of item i.

Since a topic consists of several features, we average the feature ratings to get the topic rating. For a given topic t of an item i containing l features, the rating corresponding to a feature $f _ { k }$ is $r _ { i f _ { k } } ;$ then the item i’s rating on the topic t is $r _ { i t } .$

$$
r _ {i t} = \frac {1}{l} \sum_ {k = 1} ^ {l} r _ {i f _ {k}}\tag{7}
$$

We can compute the ratings of each item on different topics, and thus construct the item-topic matrix $R _ { I - T } .$

$$
R _ {I - T} = [ r _ {i t} ] _ {n \times \tau} = \left[ \begin{array}{c c c} r _ {1 1} & \dots & r _ {1 \tau} \\ \vdots & \ddots & \vdots \\ r _ {n 1} & \dots & r _ {n \tau} \end{array} \right]\tag{8}
$$

where, $r _ { i t }$ is the topic t’s rating of item $i ,$ and n and τ are the number of items and topics, respectively.

Based on the item-topic rating matrix built above, we can calculate the item similarities and then predict the missing ratings in the user-item matrix by item similarities, which is in line with the fundamental idea of item-based collaborative filtering. Every row of the item-topic matrix represents an item's ratings on τ topics, and item i corresponds to a row vector: $\mathbf { i } = ( r _ { i 1 } , . . . , r _ { i \tau } )$ . We can calculate the item similarity using cosine similarity:

$$
\operatorname{sim} ^ {I} (\mathbf {i}, \mathbf {j}) = \cos (\mathbf {i}, \mathbf {j}) = \frac {\mathbf {i} \cdot \mathbf {j}}{\| \mathbf {i} \| \| \mathbf {j} \|}\tag{9}
$$

where $s i m ^ { I } ( \mathbf { i } , \mathbf { j } )$ represents the similarity between items i and j.

## 4.3. Imputation of user-item rating matrix

Before inferring the unknown user ratings, we first try to group similar items using a clustering algorithm. We then derive the missing item rating based on the known item ratings in the same cluster. Here, we use a classic clustering method, K-means, to group similar items. The cluster results are denoted as cluster $( i _ { 1 } , . . . , i _ { \lambda } )$

Next, we leverage the item similarities to predict the unknown item ratings. For user u, let us assume that he/she rated k items $( i _ { 1 } , . . . , i _ { k } ) _ { : }$ , and in these k items, λ items are in the same cluster: cluste $( i _ { 1 } , . . . , i _ { \lambda } )$ . Further if the above cluste $( i _ { 1 } , . . . , i _ { \lambda } )$ includes item $i _ { j }$ and user u has no rating for $i _ { j } ,$ then the missing rating of user u for item i can be filled as:

$$
r _ {u i _ {j}} ^ {\prime} = \frac {\sum_ {h = 1} ^ {\lambda} r _ {u i _ {h}} \times \operatorname{sim} ^ {I} \left(\mathbf {i} _ {h} , \mathbf {i} _ {j}\right)}{\sum_ {h = 1} ^ {\lambda} \operatorname{sim} ^ {I} \left(\mathbf {i} _ {h} , \mathbf {i} _ {j}\right)}\tag{10}
$$

We treat the above predicted item ratings as virtual ratings and mix them with the real ratings in the user-item matrix to solve the sparsity problem. The user-item matrix $R _ { U - I }$ can be represented as,

$$
R _ {U - I} = [ r _ {u i} ] _ {m \times n} = \left[ \begin{array}{c c c} r _ {1 1} & \dots & r _ {1 n} \\ \vdots & \ddots & \vdots \\ r _ {m 1} & \dots & r _ {m n} \end{array} \right]\tag{11}
$$

The elements of the above matrix are the users' real ratings on items. However, in real-life applications, the above user-item matrix is very sparse. We use the virtual ratings to replace the missing values in the matrix $R _ { U - I } .$ . The filled user-item matrix $R _ { U - I } { ' }$ is,

$$
R _ {U - I} ^ {'} = \left[ r _ {u i} ^ {'} \right] _ {m \times n} = \left[ \begin{array}{c c c} r _ {1 1} ^ {'} & \dots & r _ {1 n} ^ {'} \\ \vdots & \ddots & \vdots \\ r _ {m 1} ^ {'} & \dots & r _ {m n} ^ {'} \end{array} \right]\tag{12}
$$

## 4.4. Matrix factorization

In model-based collaborative filtering method, matrix factorization is commonly used to alleviate the sparsity problem. The basic idea behind matrix factorization is that it treats the rating as the inner products of a user vector $\mathbf { p } _ { u } \in \mathbb { R } ^ { f }$ and an item vector $\mathbf { q } _ { i } \in \mathbb { R } ^ { f }$ where the user factor implies the user's preferences to different item features, and the item factor represents the performances of different features. Then by multiplying the user and item vectors, we can get an overall evalu ation of user u to item i, which approximates the rating $r _ { u \dot { u } } ,$ and is denoted by ${ \widehat { r } } _ { u i } \colon$

$$
\widehat {r} _ {u i} = \mathbf {q} _ {i} ^ {\mathrm{T}} \mathbf {p} _ {u}\tag{13}
$$

However, if there is a high percentage of missing values, applying matrix factorization in collaborative filtering often results in an over fitting problem. In this paper, the matrix factorization is conducted on the filled user-item rating matrix. After rating imputation, the number of missing values is reduced. Then through matrix factorization, the spar sity problem can be further reduced.

Considering $\mathbf { q } _ { i } ^ { \mathrm { ~ T ~ } } \mathbf { p } _ { u }$ is the approximation of the known rating $r _ { u \dot { b } }$ we compute the regularized squared error as the objective function, and estimate the factor vectors $( { \bf p } _ { u }$ and $\mathbf { q } _ { i } )$ by minimizing the function:

$$
\min _ {\mathbf {q} ^ {*}, \mathbf {p} ^ {*}} \sum_ {(u, i) \in \kappa} \left(r _ {u i} - \mathbf {q} _ {i} ^ {T} \mathbf {p} _ {u}\right) ^ {2} + \lambda \left(\| \mathbf {q} _ {i} \| ^ {2} + \| \mathbf {p} _ {u} \| ^ {2}\right)\tag{14}
$$

where κ is the set of the $( u , i )$ pairs for which $r _ { u i }$ is known, including the real and virtual rating; $\| \cdot \|$ is the Euclidean norm of a vector, which is used to avoid overfitting; and the constant λ is a regularization param eter and is tuned by cross-validation. As suggested by [33], the param eters in this optimization function can be learned by the alternating least squares algorithm.

The RMF recommendation algorithm is detailed below.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm. Review-Based Matrix Factorization (RMF)

Data:
User dataset u, product set I, User-Item rating matrix  $R_{U-I}$ , and user's review text set Rev

Result:
Top N recommendation results set  $I_{N}$ 

1: for all review rev ∈ Rev do

2: Extract feature-opinion pair (f, o);

3: Add feature f into feature set F;

4: Compute opinion word o's sentiment value s(o);

5: end for

6: Perform topic modelling for feature set F and get topic set T;

7: for all product i ∈ I do

8: for all topic t ∈ T do

for all feature f ∈ F do

10: Compute product i's rating on feature f by Equation 6;

11: end for

12: Compute product i's rating on topic t by Equation 7;

13: end for

14: Construct Item-Topic rating matrix  $R_{I-T}$  by Equation 8;

15: end for

16: for all product i ∈ I do

17: for all product j ∈ I do

18: Compute the product similarity between i and j by Equation 9;

19: end for

20: end for

21: Cluster products using K-means algorithm by product similarities;

22: for all  $r_{ui} \in R_{U-I}$  do

23: if  $r_{ui}$  is null then

24: Find the cluster of products that contains i;

25: Compute the predicted rating by Equation 10 and fill into  $R_{U-I}$ ;

26: end if

27: end for

28: Learn the latent factors  $p_{u}$  and  $q_{i}$  by Equation 14;

29: Predict the unknown rating by Equation 13;
</div>

## 5. Experimental study

## 5.1. Experiment dataset and pre-processing

We use two real-world datasets obtained by crawling a commercial website, Buzzillion.com, to evaluate the proposed method: the digital SLR<sup>1</sup> camera and the laptop computer dataset. We choose the digital SLR camera and the laptop computer as the experiment objects because they are typical high-risk products [28]. Due to their durability and high cost compared with other consumable products, like books and movies, consumers do not buy them often, and thus there is a more serious rating sparsity problem. Both datasets contain textual reviews and numerical ratings (on a scale of one to five) that were assigned by the reviewers.

We first performed feature-level sentiment analysis and topic modeling on the textual reviews. We use Stanford CoreNLP [42], a freely available natural language processing package from Stanford NLP Group, for sentiment analysis. There are a series of natural language processing tools in Stanford CoreNLP including, directory of various forms of word (prefix, suffix, root, etc.), performing part-of-speech tagging, and the word dependencies marker in the sentence structure. Stanford CoreNLP was developed in Java; in our experiments, we call its functions via its Java programmatic API. As discussed in Section 4.1, there are two key steps in feature-level sentiment analysis: extracting product features and identifying opinion words.

• In the first step, we extract high-frequency nouns from review text. Then, product features are identified by filtering these high frequency nouns. The part-of-speech tagging tool (POS Tagger) of Stanford CoreNLP is used to identify the nouns in the sentences.

• In the second step, we analyze the syntactic dependency relation ships in the review text and then identify the opinion words by their specific dependency relationships with the feature words. Stanford CoreNLP provides a syntactic parser that can output a representation of grammatical relationships between words in a sentence.

As discussed in Section 4.1, product topics are extracted by the Latent Dirichlet Allocation algorithm. In the experiment, we use a Java implementation of Latent Dirichlet Allocation called JGibbLDA freely provided by Phan and Nguyen [49]. JGibbLDA uses the Gibbs sampling technique for parameter estimation and inference.

After sentiment analysis and topic modeling, 31 features and 11 topics were identified for the digital SLR camera dataset, and 23 features and 10 topics were identified for the laptop computer dataset. The topics and features identified for both datasets are listed in Tables 2 and 3. From the two tables, we can see that the meanings of different topics have very clear differences, and they describe the camera or the laptop computer from different aspects. Although features are a more finegrained description, most features still have relatively clear differences in meaning. However, some of the features' meanings may be ambig uous, like the meaning differences between an accessory and the device of the camera. We can explain this example: the device contains the cam era's own components that constitute the basic functions of the camera, while an accessory is added by the user to enhance the functions of the camera, without which the camera's basic functions are not affected. Nevertheless, we must emphasize that the possible ambiguity in the meaning of features does not affect the experiment results and the val idity of the method, because in the proposed RMF algorithm, the feature rating is an intermediate step, and the final step is computing the topic rating. Therefore, the ratings of features with similar meanings will eventually be classified into the same topic rating, so it will not affect the model.

We cleaned the dataset by (1) removing the reviews with less than four features to ensure that each review has enough information mass; and (2) removing the products with less than ten reviews to ensure that each product has sufficient ratings and reviews for analysis. The details of the dataset before and after cleaning are shown in Table 4.

Table 2  
Topics, features, and feature words of the digital SLR camera dataset.

<table><tr><td>Topic</td><td>Feature</td><td>Feature Words</td></tr><tr><td>General (1)</td><td>1. General</td><td>camera</td></tr><tr><td>Type (2)</td><td>2. Type</td><td>digicam, digital, DLSR, SLR...</td></tr><tr><td>Brand (3)</td><td>3. Brand</td><td>brand, Cannon, Coolpix, Nikon, Olympus, Panasonic, Sony...</td></tr><tr><td>Quality (4)</td><td>4. Quality</td><td>quality...</td></tr><tr><td>Photography (5,6)</td><td>5. Picture</td><td>image, photo, photograph, photography, picture...</td></tr><tr><td rowspan="5">Appearance(7–10)</td><td>6. Video</td><td>film, movie, video, videography...</td></tr><tr><td>7. Size</td><td>bulk, bulkiness, size, weight...</td></tr><tr><td>8. Body</td><td>arm, body, bracket, button, hand...</td></tr><tr><td>9. Color</td><td>color</td></tr><tr><td>10. Appearance</td><td>appearance</td></tr><tr><td rowspan="8">Hardware(11–21)</td><td>11. Shutter</td><td>shutter, snapshot...</td></tr><tr><td>12. Shot</td><td>exmor, fisheye, glass, resolution, zoom, len, lense, shot...</td></tr><tr><td>13. Screen</td><td>LCD, LED, screen, touchscreen...</td></tr><tr><td>14. Battery</td><td>battery, energy, power...</td></tr><tr><td>15. Flash</td><td>flash, flashlight, speedlight, speedlite...</td></tr><tr><td>16. Viewfinder</td><td>EVF, finder, viewfinder...</td></tr><tr><td>17. Accessory</td><td>accessory, adapter, adaptor, monopod, tripod...</td></tr><tr><td>18. Device</td><td>device, dial, equipment, instrument, machine, sensor...</td></tr><tr><td rowspan="10">Performance(22–28)</td><td>19. Memory</td><td>capacity, memory, SDHC, storage...</td></tr><tr><td>20. Processor</td><td>processing, processor, EOS...</td></tr><tr><td>21. Mode</td><td>mode, model, setting, setup...</td></tr><tr><td>22. Usefulness</td><td>control, handling, usability, usage, usefulness...</td></tr><tr><td>23. Flexibility</td><td>adjustability, adjustment, flexibility, sensitivity...</td></tr><tr><td>24. Portability</td><td>convenience, portability...</td></tr><tr><td>25. Stability</td><td>durability, reliability, stability, sturdiness...</td></tr><tr><td>26. Speed</td><td>speed</td></tr><tr><td>27. Accuracy</td><td>accuracy</td></tr><tr><td>28. Performance</td><td>ability, capability, functionality, utility, performance...</td></tr><tr><td>Price (29)</td><td>29. Price</td><td>cost, money, price, value, worth...</td></tr><tr><td>Design (30)</td><td>30. Design</td><td>design, detail, style...</td></tr><tr><td>Service (31)</td><td>31. Service</td><td>service</td></tr></table>

Note: 1. The numbers in parentheses indicate the corresponding features included in the topic. 2. The feature seeds that were manually added include: video, size, body, use, ability and device.

## 5.2. Baseline methods and evaluation

In our experimental study, we use the following four popular and related recommendation algorithms as the baseline methods to evaluate the proposed RMF approach. Among the four methods, the first and second ones are typical memory-based collaborative filtering methods, and the third one is a typical model-based method. Since these three baseline methods consider only online ratings and do not consider on line textual reviews, we use the fourth, review-based method, “RTWCB.”

1. User-Based Collaborative Filtering (UCF): This is one of the basic collaborative filtering algorithms used in [27], which generates recommendations by finding similar users to the target user.

2. Item-Based Collaborative Filtering (ICF): This is one of the basic collaborative filtering algorithms proposed by Sarwar et al. [52], which first finds similar items and then generates recommendations based on the similarity between the items.

3. Matrix Factorization (MF): This is a commonly used model-based method proposed by Koren et al. [33]. We use MF directly on the original user-item rating matrix.

Table 3  
Topics, features, and feature words of the laptop computer dataset.

<table><tr><td>Topic</td><td>Subtopics</td><td>Feature Words</td></tr><tr><td>General (1)</td><td>1. General</td><td>computer, laptop, notebook, PC...</td></tr><tr><td>Activity (2)</td><td>2. Activity</td><td>gaming, business, personal...</td></tr><tr><td>Brand (3)</td><td>3. Brand</td><td>Acer, Apple, Dell, Google, HP, Lenovo, Samsung...</td></tr><tr><td rowspan="3">Appearance (4–6)</td><td>4. Size</td><td>bulk, bulkiness, size, weight, inch, pound...</td></tr><tr><td>5. Color</td><td>color</td></tr><tr><td>6. Appearance</td><td>appearance</td></tr><tr><td rowspan="2">Software (7–8)</td><td>7. Operating System</td><td>OS, OS X, Windows, Linux...</td></tr><tr><td>8. Internet</td><td>WLAN, Wi-Fi, 3G, 4G, Internet...</td></tr><tr><td rowspan="7">Hardware (9–15)</td><td>9. CPU</td><td>processor, Intel, AMD, core, CPU...</td></tr><tr><td>10. RAM</td><td>RAM, memory...</td></tr><tr><td>11. Drive</td><td>drive, SSD, solid state drive, mechanical hard drive, storage...</td></tr><tr><td>12. Battery</td><td>battery, energy, power...</td></tr><tr><td>13. Graphics</td><td>graphics, GPU...</td></tr><tr><td>14. Display</td><td>display, screen, resolution, LED, LCD, touchscreen...</td></tr><tr><td>15. Accessory</td><td>accessory, adapter, adaptor, keyboard, mouse, USB, HDMI...</td></tr><tr><td rowspan="5">Performance (16–20)</td><td>16. Usefulness</td><td>control, handling, usability, usage, usefulness...</td></tr><tr><td>17. Portability</td><td>convenience, portability...</td></tr><tr><td>18. Stability</td><td>durability, reliability, stability...</td></tr><tr><td>19. Speed</td><td>speed</td></tr><tr><td>20. Performance</td><td>functionality, utility, performance...</td></tr><tr><td>Price (21)</td><td>21. Price</td><td>cost, money, price, value, worth...</td></tr><tr><td>Design (22)</td><td>22. Design</td><td>design, detail, style...</td></tr><tr><td>Service (23)</td><td>23. Service</td><td>service</td></tr></table>

Note: 1. The numbers in parentheses indicate the corresponding features included in the topic. 2. The feature seeds that were manually added include: size, operation, use, ability, function and stability.

4. Content-Based recommendation based on Real-Time Web (RTWCB): Garcia Esparza et al. [15] introduce online reviews into contentbased recommendation. It profiles the users and items by extract ing the word terms from related reviews. This is a content-based technique and does not consider the feature-level opinions implied by the textual reviews.

Throughout the experiment, we compare the recommendation ac curacy between our proposed RMF method and the four baseline methods described above. Since the first three baseline methods and our method can predict the specific item ratings, we select mean absolute error (MAE) as the measurement index. MAE is defined as,

$$
\mathrm{MAE} = \frac {\sum_ {i = 1} ^ {N} \left| p _ {i} - r _ {i} \right|}{N}\tag{15}
$$

where $p _ { i }$ is the predicted rating for item i and $r _ { i }$ is the true rating.

Unlike the first three baseline methods, RTWCB generates a recom mendation list, so we use the classification accuracy metrics. Here we use three accuracy indices: precision, recall, and F1 values, as the measurements.

$$
\left\{ \begin{array}{c} \text { Precision } = \frac {| T \cap R |}{| R |} \\ \text { Recall } = \frac {| T \cap R |}{| T |} \\ \text { F1 } = \frac {2 \times \text { Precision } \times \text { Recall }}{\text { Precision } + \text { Recall }} \end{array} \right.\tag{16}
$$

where T and R are the test set and the recommended set respectively.

## 5.3. Results of experiment

We first compare the proposed method with UCF, ICF, and MF using the MAE. To compare the performance of the methods, we conduct a kfold cross-validation, a commonly used evaluation method in the field of recommender systems. In k-fold cross-validation, we partition the original sample randomly and equally into k subsamples, of which, a single subsample is kept as the test dataset, and the remaining k − 1 subsamples are treated as the training data. To guarantee that each of the k subsamples is used as the test data exactly once, we repeat the cross-validation process k times, and then average k results from the folds to get a single estimation. The advantage of this method is that all samples are used for both training and test, and each sample is used for validation exactly once.

Table 4  
Dataset information before and after cleaning.

<table><tr><td>Dataset</td><td>Statistics</td><td>Before Cleaning</td><td>After Cleaning</td></tr><tr><td>Digital SLR</td><td>Total reviews</td><td>82,179</td><td>61,537</td></tr><tr><td rowspan="11">Camera Dataset</td><td>Total reviewers</td><td>66,742</td><td>33,517</td></tr><tr><td>Total products</td><td>1143</td><td>469</td></tr><tr><td>Min. reviews per reviewer</td><td>1</td><td>1</td></tr><tr><td>Average reviews per reviewer</td><td>1.2313 (st.d. = 1.3263)</td><td>1.8360 (st.d = 1.5016)</td></tr><tr><td>Max. reviews per reviewer</td><td>39</td><td>37</td></tr><tr><td>Min. reviews per product</td><td>1</td><td>10</td></tr><tr><td>Average reviews per product</td><td>71.8976 (st.d = 286.6775)</td><td>131.2090 (st.d. = 240.4391)</td></tr><tr><td>Max. reviews per product</td><td>3785</td><td>2650</td></tr><tr><td>Min. features per reviews</td><td>1</td><td>4</td></tr><tr><td>Average features per reviews</td><td>3.3061 (st.d = 4.0226)</td><td>7.1342 (st.d. = 3.8224)</td></tr><tr><td>Max. features per reviews</td><td>17</td><td>17</td></tr><tr><td rowspan="12">Laptop Computer Dataset</td><td>Total reviews</td><td>39,977</td><td>16,912</td></tr><tr><td>Total reviewers</td><td>30,678</td><td>8747</td></tr><tr><td>Total products</td><td>435</td><td>124</td></tr><tr><td>Min. reviews per reviewer</td><td>1</td><td>1</td></tr><tr><td>Average reviews per reviewer</td><td>1.3031 (st.d. = 2.012)</td><td>1.9335 (st.d. = 1.9036)</td></tr><tr><td>Max. reviews per reviewer</td><td>67</td><td>61</td></tr><tr><td>Min. reviews per product</td><td>1</td><td>10</td></tr><tr><td>Average reviews per product</td><td>91.9011 (st.d. = 120.3047)</td><td>136.3871 (st.d. = 113.2991)</td></tr><tr><td>Max. reviews per product</td><td>5003</td><td>4538</td></tr><tr><td>Min. features per reviews</td><td>1</td><td>4</td></tr><tr><td>Average features per reviews</td><td>2.002 (st.d. = 3.8881)</td><td>4.4167 (st.d. = 3.3673)</td></tr><tr><td>Max. features per reviews</td><td>13</td><td>13</td></tr></table>

To conduct k-fold cross-validation, we need to exclude the users with less than k ratings. In the typical experimental settings, depending on the size of the dataset, a value of k between five and ten is used. For both of our datasets, we calculate the number of remaining users for k = 5 and k = 10, as shown in Table 5. From this table, we can see that if k = 10, only a small percentage of reviewers are left in the test dataset (3.21% for the laptop computer dataset and 0.84% for the digital SLR camera dataset). However, if k = 5, the remaining reviewers are enough for both datasets. So, we set k = 5.

The number of reviewers.

<table><tr><td>Dataset</td><td>Number of Total Reviewers</td><td>Number of Reviewers with More than Five Ratings</td><td>Number of Reviewers with More than Ten Ratings</td></tr><tr><td>Digital SLR Camera</td><td>33,517</td><td>1266 (Ratio = 3.78%)</td><td>282 (Ratio = 0.84%)</td></tr><tr><td>Laptop Computer</td><td>8747</td><td>746 (Ratio = 8.53%)</td><td>281 (Ratio = 3.21%)</td></tr></table>

Note: Ratio means the number's ratio to number of total reviewers

Table 6  
Fivefold cross validation results of RMF, UCF, ICF, and MF.

<table><tr><td>Dataset</td><td>Algorithm</td><td>MAE1</td><td>MAE2</td><td>MAE3</td><td>MAE4</td><td>MAE5</td><td>Mean MAE</td><td>St.d.</td></tr><tr><td rowspan="4">Digital SLR Camera Dataset</td><td>RMF</td><td>1.3223</td><td>1.4946</td><td>1.2668</td><td>1.4194</td><td>1.3042</td><td>1.3626</td><td>0.8066</td></tr><tr><td>MF</td><td>1.7263</td><td>1.9000</td><td>1.8735</td><td>1.7798</td><td>1.6271</td><td>1.7846</td><td>0.9548</td></tr><tr><td>UCF</td><td>2.3968</td><td>2.2822</td><td>2.2568</td><td>2.3682</td><td>2.3750</td><td>2.3363</td><td>0.9732</td></tr><tr><td>ICF</td><td>2.2448</td><td>2.2111</td><td>2.1878</td><td>2.2009</td><td>2.1836</td><td>2.2082</td><td>1.0209</td></tr><tr><td rowspan="4">Laptop Computer Dataset</td><td>RMF</td><td>1.1028</td><td>1.0211</td><td>1.1551</td><td>1.0428</td><td>1.1250</td><td>1.0884</td><td>0.6397</td></tr><tr><td>MF</td><td>1.4429</td><td>1.3847</td><td>1.4318</td><td>1.3571</td><td>1.4221</td><td>1.4090</td><td>0.7298</td></tr><tr><td>UCF</td><td>1.9557</td><td>2.0051</td><td>1.9859</td><td>1.9695</td><td>2.0164</td><td>1.9851</td><td>0.9920</td></tr><tr><td>ICF</td><td>1.8389</td><td>1.8981</td><td>1.8930</td><td>1.7573</td><td>1.8631</td><td>1.8514</td><td>0.9749</td></tr></table>

Notes:  
1. In UCF, ICF, and Phase I of RMF, an important factor, the number of nearest neighbours K, should be determined. This factor is tuned until obtaining the optima values are obtained: K = 13 for Phase I of RMF, K = 25 for UCF, and K = 11 for ICF in the digital SLR camera dataset; and K = 13 for Phase I of RMF, K = 30 for UCF, and K = 9 for ICF in the laptop computer dataset.  
2. St.d. is short for standard deviation.  
3. MAE1 to MAE5 represent the MAE of each fold.

![](/api/attachments/M7P7UHQR/fulltext/images/4c9a82db220e9943513c3e38127f3f89cbf4b5e75a85dd2a53be88ec2d5090c2.jpg)  
Fig. 2. The distribution of absolute error in the digital SLR camera dataset.

![](/api/attachments/M7P7UHQR/fulltext/images/9e1c0425831a52d99bf92b5d7821e689b8c2aeb851f662574a3ef0968d6b4c41.jpg)  
Fig. 3. The distribution of absolute error in the laptop computer dataset.

We removed the users who reviewed less than five brands while performing the five-fold cross-validation. Then, we partition the reviews of each user into five equal-sized folds, among which, four partitions are used for training the model, and the fifth partition is used as the test dataset. We then rotated the folds between training and validation. For each fold, we use the above four recommendation methods and get the

MAE value of each method. We then average the MAE values of the five folds for each method.

The performance (MAE) results of the RMF, UCF, ICF, and MF models on two datasets are provided in Table 6. Fig. 2 and Fig. 3 shows the distribution of the absolute errors of the different algorithms on two datasets. We divided the absolute error into eight intervals (bins) evenly from 0 to 4.0; we then counted the frequency of the absolute errors of the individual rating prediction of the four recommendation methods for each interval, and display the results in Fig. 2 and Fig. 3. These figures show that the relative magnitude of the four methods' frequencies in different bins shows a clear difference. Fig. 2 can be divided into two groups: in the left four bins, the absolute errors are less than 2.0, and RMF has the highest frequency, followed by MF, ICF, and UCF; in the right four bins, the absolute errors are between 2.0 and 4.0, UCF has the highest frequency, and our RMF method has the lowest frequency. In Fig. 3, we can see the same trend, except that the three bins on the left are one group, and the five bins on the right are the other group; how ever, the RMF method also has the highest frequency in the left group and the lowest frequency in the right group. The results show the su periority of the RMF method; that is, compared with the other three methods, RMF can achieve a more-accurate recommendation in more situations.

Table 7  
Results of paired-sample t-test.

<table><tr><td rowspan="3">Dataset</td><td rowspan="3">Methods</td><td colspan="5">Paired Differences</td><td rowspan="3">t Statistic</td><td rowspan="3">df</td><td rowspan="3">p-Value (Two-Tailed)</td></tr><tr><td rowspan="2">Mean</td><td rowspan="2">Std. Deviation</td><td rowspan="2">Std. Error Mean</td><td colspan="2">95% Confidence Interval of the Difference</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td rowspan="3">Digital SLR Camera Dataset</td><td>RMF vs. MF</td><td>-0.4199</td><td>0.1099</td><td>0.0491</td><td>-0.5563</td><td>-0.2834</td><td>-8.5435</td><td>4</td><td>0.0010</td></tr><tr><td>RMF vs. UCF</td><td>-0.9743</td><td>0.1174</td><td>0.0525</td><td>-1.1201</td><td>-0.8286</td><td>-18.5621</td><td>4</td><td>4.9578E-05</td></tr><tr><td>RMF vs. ICF</td><td>-0.8442</td><td>0.0915</td><td>0.0409</td><td>-0.9578</td><td>-0.7305</td><td>-20.6245</td><td>4</td><td>3.2646E-05</td></tr><tr><td rowspan="3">Laptop Computer Dataset</td><td>RMF vs. MF</td><td>-0.3184</td><td>0.0344</td><td>0.0154</td><td>-0.3610</td><td>-0.2757</td><td>-20.7162</td><td>4</td><td>3.2077E-05</td></tr><tr><td>RMF vs. UCF</td><td>-0.8972</td><td>0.0608</td><td>0.0272</td><td>-0.9727</td><td>-0.8216</td><td>-32.9696</td><td>4</td><td>5.0471E-06</td></tr><tr><td>RMF vs. ICF</td><td>-0.7607</td><td>0.0658</td><td>0.0294</td><td>-0.8424</td><td>-0.6791</td><td>-25.8683</td><td>4</td><td>1.3267E-05</td></tr></table>

Note: df is short for degree of freedom.

The results in Table 6 show that for both datasets, our proposed recommendation algorithm, RMF, achieves the best performance (with the lowest mean MAE values); the next best performances are MF, ICF, and UCF in that order. We conducted a paired-samples t-test of the RMF algorithm with the other three algorithms to verify if the differences in performance are statistically significant. The null hypotheses are: the difference between RMF and each other algorithm is zero. The results including the t statistics and p-values are shown in Table 7. The results show a significant difference in the MAE for RMF and MF (t = − 8.5435, $\pmb { p } = 0 . 0 0 1 0$ for the camera dataset and t = − 20.7162, p = 3.2077E − 05 for the laptop dataset), as well as for RMF and UCF (t = − 18.5621, p = 4.9578E − 05 for the camera dataset and t = − 32.9696, p = 5.0471E − 06 for the laptop dataset) and for RMF and ICF (t = − 20.6245, p = 3.2646E − 05 for the camera dataset and t = − 25.8683, p = 1.3267E − 05 for the laptop dataset). Thus, the proposed RMF method has a significantly better recommendation accuracy compared to the popular collaborative filtering techniques.

Next, we compared the proposed RMF method with the fourth baseline method, RTWCB. Since RTWCB generates the top N recom mendation, we compared the results with the top N predicted ratings generated by the RMF method. For the test dataset, we use the products that users gave a rating of more than three (representing a positive opinion of the product) and removed the other data. This assumption was also used in [40]. The recommendation performance on both datasets is shown in Table 8. The results clearly indicate that the RMF method outperforms RTWCB on all three accuracy measures. From these results, we can say that, compared with using only the traditional content-based technique (i.e., extracting only the word terms from on line reviews), deeply mining the feature-level opinions from textual reviews can improve the recommendation performance.

## 5.4. Complexity analysis

Based on the experimental results, we can confirm that the proposed RMF method enhances the recommendation performance. However, we still need to consider cost due to the increase in complexity. Therefore, we analyze the complexity of the RMF method from two perspectives: data and model (algorithm).

From the perspective of data, there is a trend in the academic research and commercial application of recommendation systems that different types of data are used together to improve recommendation

## Table 8

The precision value, recall value, and F1 value of RMF and RTWCB.

<table><tr><td>Dataset</td><td>Algorithm</td><td>Precision</td><td>Recall</td><td>F1 Value</td></tr><tr><td rowspan="2">Digital SLR Camera Dataset</td><td>RMF</td><td>0.3067</td><td>0.2461</td><td>0.2731</td></tr><tr><td>RTWCB</td><td>0.1084</td><td>0.1768</td><td>0.1344</td></tr><tr><td rowspan="2">Laptop Computer Dataset</td><td>RMF</td><td>0.3551</td><td>0.2693</td><td>0.3063</td></tr><tr><td>RTWCB</td><td>0.1361</td><td>0.1962</td><td>0.1607</td></tr></table>

Note: Precision, recall, and F1 values are related to the size of the recommendation list, denoted N. Generally, as the size of the recommendation list in creases, the precision decreases and the recall increases. In the experiment, we tune the size of the recommendation list until the optimal F1 value is obtained. In the digital SLR camera dataset. N = 15 for RMF and N = 10 for RTWCB. In the laptop computer dataset, $N = 1 5$ for RMF and N = 15 for RTWCB.

accuracy [54]. This increases the complexity of the system. In this paper, we focus on the role of one type of auxiliary data, that is, online reviews. This limits the increase in complexity of the system. In addition, we should distinguish between online and offline operations. Topic modeling and most of the feature-level sentiment analysis can be treated as offline operations, which means that we need to execute them only once, and the extracted topics and features, as well as the ratings of the topics and features, can be used repeatedly in the process of online recommendation. Therefore, the complexity of the recommendation operation, which is the online part, should not increase much.

In terms of models, when we mention the concept of complexity, it is basically equivalent to algorithm complexity. So, we analyzed the complexity of the RMF algorithm proposed in this article. The RMF al gorithm has three parts: construction of the item-topic rating matrix (from line 1 to line 15), rating imputation (from line 16 to line 27), and matrix factorization (lines 28 and 29). Assume that the number of items is $N ,$ the number of users is M, the number of topics is $T ,$ and the number of features is F; then the complexity of the first and second parts of the algorithm are, respectively, O(NTF) and $O ( \operatorname* { m a x } ( M N , N ^ { 2 } ) )$ The complexity of the third part – matrix factorization – is related to mini mizing Equation 14. We select the alternating least squares algorithm for learning the parameters in this equation. Referring to Takacs ´ and Tikk's research conclusions [58], the complexity of this algorithm is $O ( R L ^ { 2 } .$ + $( M + N ) L ^ { 3 } )$ , where M and N represent the numbers of users and items, respectively, R represents the number of ratings in the matrix, and L represents the number of latent factors. Through the above analysis, we can see that the matrix factorization has the highest complexity, which is an order of magnitude higher than the first part, and two orders of magnitude higher than the second part. Therefore, we conclude that the complexity of our proposed algorithm is the same as that of the benchmark algorithm – the classical matrix factorization.

Through the above analysis of the complexity of our proposed method from the perspectives of data and model, it can be concluded that our proposed method will not significantly increase the cost of complexity compared with the existing methods.

## 6. Conclusion

In commercial recommender systems, the data sparsity problem is widespread. Model-based collaborative filtering and hybrid collabora tive filtering are two main approaches to address this problem. Considering both approaches, we propose the RMF recommendation method to address the rating sparsity problem. Our approach is divided into two phases. In the first phase, by introducing online reviews and feature-level sentiment analysis, we create an item-topic rating matrix to compute the similarities between items. This is a hybrid collaborative filtering method. Through this phase, we can predict the values of some unknown ratings. Then, in the second phase, we replace the unknown ratings of the sparse user-item matrix with the predicted ratings and use matrix factorization on the filled matrix. The results can be easily reproduced using the same data set and method, the only subjective aspects of the method are value of K used (K=11 for digital SLR camera dataset and K=7 for laptop computer dataset) on clustering method and some important missing seeds that were manually added. As long as these are same the results should be reproduce. The major contribution of this paper is that we introduce online textual reviews into recom mendations and combine rating imputation and matrix factorization to solve the sparsity problem. The experiment demonstrates the superior performance of the proposed RMF method in increasing recommenda tion accuracy, compared with the methods that use only ratings, online reviews, or matrix factorization.

The implications of this paper for research and practice are signifi cant. For research, the proposed framework and experiment results inspire researchers to take advantage of both model and data for developing an accurate and effective recommender system. Especially in the era of big data, the role of data becomes more prominent.

Researchers should take advantage of all the available data to make up for the flaws in the model. This research provides an example where textual reviews are mined to make up for the insufficient performance of matrix factorization when the data is too sparse. In addition, it is also very important to develop models suitable for different types of data. In this paper, for the data of textual reviews, we use a feature-level senti ment analysis technique and develop an additional submodule – a rating imputation for the matrix factorization model, achieving the purpose of an organic integration of auxiliary data and the original model.

For practice, marketing in the era of big data is driven by data and technology, and a recommendation system is an effective tool for online marketing and product promotion. The proposed recommendation framework, which combines review- and model-based methods, is in accordance with the basic architecture of commercial recommender systems and the trends of corporate marketing. The recommendation algorithm motivates managers to pay attention to customer feedback, such as the online reviews used in this paper. Through in-depth mining of the review text, valuable information about consumer preferences can be gathered; then, with the appropriate model, such as the one in thi paper, marketing capabilities can be significantly enhanced. In addition, this paper presents a feasible way to solve the well-known sparsity problem, which is widespread in commercial recommendation. This is particularly important to the recommendations of “high-involvement” products. High-involvement products, also called high-risk or high-cost products, are products with high values that can be used for a long time. Users typically buy this kind of product only after detailed information collection and product comparison. Digital cameras and computers are common high-involvement products. The sparsity problem for these products is more pronounced because consumers buy them only a few times, and our proposed method is more suitable for them than are other methods.

This research has some limitations. First, we collect the review related data from a word-of-mouth website. More of the similar kinds of websites, especially e-commerce websites, should be used to verify the effectiveness of the proposed recommendation algorithm. Second, we validate our method using two types of high-involvement product. The method should be tested on more products and services. Third, in this paper, we use a relatively simple sentiment analysis technique to mine the product features and the corresponding opinions, and only explicit opinions are mined. Although the opinion-mining algorithm is not the focus of this paper, more complex algorithms can be used to further improve the recommendation performance. And last, a limita tion should be emphasized, which is also the limitation of most academic research on recommendations [25]. We evaluate the proposed recom mendation framework – RMF – using offline experiments and accuracy metrics; however, due to data limitations, the business value of the recommendation method, such as its effect on the sales and venue, clickthrough rates, adoption, conversion, and user engagements, is not determined.

Our work can be extended in several ways in the future. First, when we predict users' ratings of unknown items in the first phase, we assume that users' preferences do not change within a short time. However, the variation of users' preferences and the impact of this variation on rec ommendations is a problem worth studying. Second, when computing the topic rating of an item, we assume that the weights of different fea tures are the same, that is, we average the item's feature ratings. Different weights should be considered in future research so that more reasonable topic ratings can be obtained. Third, in this paper, we make use of online reviews as an auxiliary data source for recommendation. However, in addition to reviews, social networks are also an important data source for recommendation in the context of Web 2.0 [54]. Thus, exploring recommender systems that combine social networks and reviews is a meaningful research direction. Finally, in future research, more business related data like click-through rates, adoption, conversion, user en gagements, and even sales and venues should be collected in the field experiment research to evaluate the business value of the recommender system. If only the offline experiments are supported, survey-based methods, like user satisfaction and experience surveys, and more met rics such as novelty, diversity, serendipity, and coverage can be used to measure the value of the recommendation system more completely.

## CRediT authorship contribution statement

Rui Duan: Conceptualization, Methodology, Software, Writing – original draft, Writing – review & editing. Cuiqing Jiang: Validation, Investigation, Visualization, Supervision. Hemant K. Jain: Supervision, Writing – original draft, Writing – review & editing.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grant Numbers 72102004 and 71731005).

## References

[1] S. Aciar, D. Zhang, S. Simoff, J. Debenham, Informed recommender: basing recommendations on consumer product reviews, IEEE Intell. Syst. 22 (3) (2007 39–47, https://doi.org/10.1109/mis.2007.55.

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Trans. Knowl. Data Eng. 17 (6) (2005) 734–749, https://doi.org/10.1109/tkde.2005.99.

[3] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, J. Mach. Learn. Res. 3 (2003) 993–1022.

[4] R. Burke, Hybrid recommender systems: survey and experiments, User Model. User-Adap. Inter. 12 (4) (2002) 331–370, https://doi.org/10.1023/A: 1021240730564.

[5] W.-L. Chang, C.-F. Jung, A hybrid approach for personalized service staff recommendation, Inf. Syst. Front. 19 (1) (2017) 149–163, https://doi.org 10.1007/s10796-015-9597-7.

[6] L. Chen, G. Chen, F. Wang, Recommender systems based on user reviews: the state of the art, User Model. User-Adap. Inter. 25 (2) (2015) 99–154, https://doi.org/ 10.1007/s11257-015-9155-5

[7] L. Chen, F. Wang, Preference-based clustering reviews for augmenting e-commerce recommendation, Knowl.-Based Syst. 50 (2013) 44–59, https://doi.org/10.1016/j. knosys.2013.05.006

[8] R. Chen, Q. Hua, Q. Gao, Y. Xing, A hybrid recommender system for Gaussian mixture model and enhanced social matrix factorization technology based on multiple interests, Math. Probl. Eng, 2018 (2018). https://doi,org/10.1155/2018 9109647.

[9] Y.-N. Chen, M. Yu, A hybrid collaborative filtering algorithm based on user-item, in: 2010 International Conference on Computational and Information Sciences, IEEE, Chengdu, China, 2010, pp. 618–621, https://doi.org/10.1109/ iccis.2010.156.

[10] J. Chung, V.R. Rao. A general consumer preference model for experience products application to internet recommendation services, J. Mark. Res. 49 (3) (2012) 289–305.https://doi org/10.1509/imr 09.0467

[11] K.W. Church, P. Hanks, Word association norms, mutual information, and lexicography, Comput. Linguist. 16 (1) (1990) 22–29.

[12] X. Ding, B. Liu, P.S. Yu, A holistic lexicon-based approach to opinion mining, in: Proceedings of the 2008 International Conference on Web Search and Data Mining, ACM, Palo Alto, CA, USA, 2008, pp. 231–240, https://doi.org/10.1145/ 1341531.1341561.

[13] Z. Dong, Q. Dong, HowNet-a hybrid language and knowledge resource, in: International Conference on Natural Language Processing and Knowledge Engineering, 2003. Proceedings. 2003, IEEE, 2003, pp. 820–824, https://doi.org 10.1109/NLPKE.2003.1276017.

[14] R. Duan, C. Jiang, H.K. Jain, Y. Ding, D. Shu, Integrating geographical and temporal influences into location recommendation: a method based on check-ins, Inf, Technol, Manag, 20 (2) (2019) 73–90. https://doi,org/10.1007/s10799-018- 0293-4.

[15] S. Garcia Esparza, M.P. O’Mahony, B. Smyth, Mining the real-time web: a novel approach to product recommendation, Knowl.-Based Syst. 29 (2012) 3–11, https:// doi.org/10.1016/j.knosys.2011.07.007.

[16] R. Ghani, K. Probst, Y. Liu, M. Krema, A. Fano, Text mining for product attribute extraction, ACM SIGKDD Explor, Newslett, 8 (1) (2006) 41–48, https://doi,org 10.1145/1147234.1147241

[17] Y. Guan, Q. Wei, G. Chen, Deep learning based personalized recommendation with multi-view information integration, Decis. Support. Syst. 118 (2019) 58–69, https://doi.org/10.1016/i.dss.2019.01.003.

[18] Z. Guan, Multi-feature collaborative filtering recommendation for sparse dataset, in: International Conference on Swarm Intelligence. Springer. Cham. 2018. pp. 286–294. https://doi.org/10.1007/978-3-319-93818-9 27.

[19] J. Gupta, J. Gadge, Performance analysis of recommendation system based on collaborative filtering and demographics, in: 2015 International Conference on Communication, Information & Computing Technology (ICCICT), IEEE, Mumbai, India. 2015. pp. 1–6. https://doi,org/10.1109/iccict,2015.7045675.

[20] X. He, T.-S. Chua, Neural factorization machines for sparse predictive analytics, in: Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, Shinjuku, Tokyo, Japan, 2017, pp. 355–364, https://doi.org/10.1145/3077136.3080777.

[21] JL.. Herlocker, JA. Konstan, A. Borchers, J. Riedl. An algorithmic framework for performing collaborative filtering, in: Proceedings of the 22nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, Berkeley, California, USA, 1999, pp. 230–237, https://doi.org 10.1145/312624.312682

[22] Y. Hu, W. Shi, H. Li, X. Hu, Mitigating data sparsity using similarity reinforcementenhanced collaborative filtering, ACM Trans. Internet Technol. (TOIT) 17 (3) (2017) 1–20, https://doi.org/10.1145/3062179.

[23] N. Idrissi, A. Zellou, A systematic literature review of sparsity issues in recommender systems, Soc. Netw. Anal. Min. 10 (1) (2020) 1–23, https://doi.org/ 10.1007/s13278-020-0626-2.

[24] N. Jakob, S.H. Weber, M.C. Müller, I. Gurevych, Beyond the stars: Exploiting freetext user reviews to improve the accuracy of movie recommendations, in: Proceedings of the 1st International CIKM Workshop on Topic-Sentiment Analysis for Mass Opinion, ACM, Hong Kong, China, 2009, pp. 57–64, https://doi.org 10.1145/1651461.1651473

[25] D. Jannach, M. Jugovac, Measuring the business value of recommender systems, ACM Trans. Manag. Inf. Syst. 10 (4) (2019), https://doi.org/10.1145/3370082. Article 16.

[26] D. Jannach, M. Zanker, A. Felfernig, G. Friedrich, Content-based recommendation, in: Recommender Systems, Cambridge University Press, Cambridge, 2022, pp. 51–80, https://doi.org/10.1017/cbo9780511763113.005.

[27] Z. Jia, Y. Yang, W. Gao, X. Chen, User-based collaborative filtering for tourist attraction recommendations, in: 2015 IEEE International Conference on Computational Intelligence & Communication Technology, IEEE, Ghaziabad, U.P., India, 2015, pp. 22–25, https://doi.org/10.1109/cict.2015.20.

[28] C. Jiang, R. Duan, H.K. Jain, S. Liu, K. Liang, Hybrid collaborative filtering for high-involvement products: a solution to opinion sparsity and dynamics, Decis. Support. Syst. 79 (2015) 195–208, https://doi.org/10.1016/j.dss.2015.09.002.

[29] H. Jing, A.-C. Liang, S.-D. Lin, Y. Tsao, A transfer probabilistic collective factorization model to handle sparse data in collaborative filtering, in: 2014 IEEE International Conference on Data Mining, IEEE, Shenzhen, China, 2014, pp. 250–259, https://doi.org/10.1109/icdm.2014.68.

[30] L. Jing, P. Wang, L. Yang, Sparse probabilistic matrix factorization by Llaplace distribution for collaborative filtering, in: Proceedings of the 24th Internationa Conference on Artificial Intelligence, AAAI Press, Buenos Aires, Argentina, 2015, pp. 1771–1777.

[31] R.L. Keeney, H. Raiffa, R.F. Meyer, Decisions with Multiple Objectives: Preferences and Value Trade-Offs. Cambridge university press. Cambridge. 1993. https://doi. org/10.1017/CB09781139174084.

[32] H.-N. Kim, A. Alkhaldi, A. El Saddik, G.-S. Jo, Collaborative user modeling with user-generated tags for social recommender systems, Expert Syst. Appl. 38 (7) (2011) 8488–8496. https://doi.org/10.1016/i.eswa.2011.01.048

[33] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommender systems, Computer 42 (8) (2009) 30–37, https://doi,org/10.1109/MC,2009.263.

[34] Y. Lee, S.-W. Kim, S. Park, X. Xie, How to impute missing ratings? Claims, solution, and its application to collaborative filtering, in: Proceedings of the 2018 World Wide Web Conference, International World Wide Web Conferences Steering Committee, Lyon, France, 2018, pp. 783–792, https://doi.org/10.1145/ 3178876.3186159.

[35] T.-P. Liang, H.-Y. Chen, E. Turban, Effect of personalization on the perceived usefulness of online customer services: a dual-core theory, in: Proceedings of the 11th International Conference on Electronic Commerce, ACM, Taipei, Taiwan. 2009, pp. 279–288, https://doi.org/10.1145/1593254.1593296.

[36] T.-P. Liang, H.-J. Lai, Y.-C. Ku, Personalized content recommendation and user satisfaction: theoretical synthesis and empirical findings, J. Manag. Inf. Syst. 23 (3) (2006) 45–70.https://doi org/10.2753/MIS0742-1222230303

[37] G. Linden, B. Smith, J. York, Amazon. com recommendations: item-to-item collaborative filtering, IEEE Internet Comput. 7 (1) (2003) 76–80, https://doi.org 10.1109/MIC.2003.1167344

[38] B. Liu, Sentiment analysis and subjectivity, in: Handbook of Natural Language Processing, Second ed., CRC Press, Boca Raton, FL, USA, 2010, pp. 627–666.

[39] B. Liu, Sentiment analysis and opinion mining, Synth. Lecture Hum. Lang. Technol. 5 (1) (2012) 1–167, https://doi,org/10.2200/S00416ED1V01Y201204HLT016.

[40] H. Liu, J. He, T. Wang, W. Song, X. Du, Combining user preferences and user opinions for accurate recommendation, Electron. Commer. Res. Appl. 12 (1) (2013) 14–23, https://doi.org/10.1016/j.elerap.2012.05.002.

[41] L. Luo, H. Xie, Y. Rao, F.L. Wang, Personalized Recommendation by Matrix Co-Factorization with Tags and Time Information, Expert Systems with Applications 119, 2019, pp. 311–321, https://doi.org/10.1016/j.eswa.2018.11.003.

[42] C.D. Manning, M. Surdeanu, J. Bauer, J.R. Finkel, S. Bethard, D. McClosky, The Stanford CoreNLP natural language processing toolkit, in: Proceedings of 52nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations, Association for Computational Linguistics, Baltimore, Maryland, 2014. pp. 55–60. https://doi.org/10.3115/v1/p14-5010.

[43] L.B. Marinho, A. Nanopoulos, L. Schmidt-Thieme, R. Jäschke, A. Hotho, G. Stumme, P. Symeonidis, Social tagging recommender systems, in: Recommender Systems Handbook, Springer, Boston, MA, 2011, pp. 615–644, https://doi,org/ 10.1007/978-0-387-85820-319

[44] P. Melville, R.J. Mooney, R. Nagarajan, Content-boosted collaborative filtering for improved recommendations, in: Eighteenth National Conference on Artificial Intelligence, AAAI, Edmonton, Alberta, Canada, 2002, pp. 187–192.

[45] V.-D. Nguyen, V.-N. Huynh, A Community-Based Collaborative Filtering System Dealing with Sparsity Problem and Data Imperfections, Springer International Publishing, Cham, 2014, pp. 884–890, https://doi.org/10.1007/978-3-319-13560- 1\_74.

[46] M. Nilashi, O. Ibrahim, K. Bagherifard, A recommender system based on collaborative filtering using ontology and dimensionality reduction techniques, Expert Syst. Appl. 92 (2018) 507–520, https://doi.org/10.1016/j. eswa.2017.09.058.

[47] B. Pang. L. Lee, Opinion Mining and Sentiment Analysis. Foundations and Trends® in Information Retrieval2 (1–2). 2008. pp. 1–135

[48] B.K. Patra, R. Launonen, V. Ollikainen, S. Nandi, A new similarity measure using Bhattacharyya coefficient for collaborative filtering in sparse data, Knowl.-Based Syst. 82 (2015) 163–177, https://doi.org/10.1016/j.knosys.2015.03.001.

[49] X.-H. Phan, C.-T. Nguyen, A java implementation of latent dirichlet allocation (lda) using gibbs sampling for parameter estimation and inference, JGibbLDA (2008). http://jgibblda.sourceforge.net.

[50] G. Oiu, B. Liu, J. Bu, C. Chen, Expanding domain sentiment lexicon through double propagation, in: Proceedings of the 21st International Jont Conference on Artifical Intelligence, Morgan Kaufmann Publishers Inc., Pasadena, CA, 2009, pp. 1199–1204.

[51] G. Qiu, B. Liu, J. Bu, C. Chen, Opinion word expansion and target extraction through double propagation, Comput. Linguist. 37 (1) (2011) 9–27, https://doi. org/10.1162/coli\_a\_00034.

[52] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative filtering recommendation algorithms, in: Proceedings of the 10th International Conference on World Wide Web, ACM, Hong Kong, Hong Kong, 2001, pp. 285–295, https:// doi.org/10.1145/371920.372071.

[53] F. Sebastiani, A. Esuli, Sentiwordnet: A publicly available lexical resource for opinion mining, in: Proceedings of the 5th International Conference on Language Resources and Evaluation, European Language Resources Association (ELRA), Genoa, Italy, 2006, pp. 417–422.

[54] Y. Shi, M. Larson, A. Hanjalic, Collaborative filtering beyond the user-item matrix: a survey of the state of the art and future challenges, ACM Comput. Surv. 47 (1) (2014) 1–45, https://doi.org/10.1145/2556270.

[55] X. Su, T.M. Khoshgoftaar, A survey of collaborative filtering techniques, Adv. Artif. Intell. 2009 (2009) 1–19, https://doi.org/10.1155/2009/421425.

[56] J. Sun, G. Wang, X. Cheng, Y. Fu, Mining affective text to improve social media item recommendation, Inf. Process. Manag. 51 (4) (2015) 444–457, https://doi. org/10.1016/j.ipm.2014.09.002.

[57] T. Mahara Suryakant, A new similarity measure based on mean measure of divergence for collaborative filtering in sparse environment, Proc. Comput. Sci. 89 (2016) 450–456. https://doi.org/10.1016/i.procs.2016.06.099.

[58] G. Tak´acs, D. Tikk, Alternating least squares for personalized ranking, in: Proceedings of the Sixth ACM Conference on Recommender Systems. 2012 pp. 83–90. https://doi.org/10.1145/2365952.2365972.

[59] J.K. Tarus, Z. Niu, A. Yousif, A hybrid knowledge-based recommender system for elearning based on ontology and sequential pattern mining. Futur. Gener. Comput Syst. 72 (2017) 37–48, https://doi.org/10.1016/j.future.2017.02.049.

[60] W.-F. Tung, T.-Y. Lee, Rank-mediated collaborative tagging recommendation service using video-tag relationship prediction, Inf. Syst. Front. 15 (4) (2013) 627-635, https://doi.org/10.1007/s10796-013-9436-7

[61] Q. Wang, J. Ma, X. Liao, W. Du, A context-aware researcher recommendation system for university-industry collaboration on R&D projects, Decis. Support. Syst. 103 (2017) 46–57, https://doi,org/10.1016/i.dss.2017.09.001.

[62] Y. Wang, J. Deng, J. Gao, P. Zhang, A hybrid user similarity model for collaborative filtering, Inf. Sci. 418 (2017) 102–118, https://doi.org/10.1016/j.ins.2017.08.008.

[63] Z. Yang, W. Chen, J. Huang, Enhancing recommendation on extremely sparse data with blocks-coupled non-negative matrix factorization, Neurocomputing 278 (2018) 126–133, https://doi.org/10.1016/j.neucom.2017.04.080.

[64] P. Yu, L. Lin, J. Wang, A novel framework to alleviate the sparsity problem in context-aware recommender systems, New Rev. Hypermedia Multimedia 23 (2) (2017) 141–158, https://doi.org/10.1080/13614568.2016.1152319.

[65] L. Zheng, V. Noroozi, P.S. Yu, Joint deep modeling of users and items using reviews for recommendation, in: Proceedings of the Tenth ACM International Conference on Web Search and Data Mining, ACM, Cambridge, United Kingdom, 2017, pp. 425–434, https://doi.org/10.1145/3018661.3018665.

[66] W. Zhou, J. Li, M. Zhang, Y. Wang, F. Shah, Deep learning modeling for top-n recommendation with interests exploring, JEEE Access 6 (2018) 51440–51455. https://doi.org/10.1109/ACCESS.2018.2869924.

Rui Duan is a lecturer in School of Tourism Sciences, Beijing International Studies Uni versity. He received his PhD degree in 2017 from from Hefei University of Technology. His research interests include big data analysis. recommendation systems and tourism marketing.

Cuiqing Jiang is a professor in School of Management, Hefei University of Technology. He received his PhD degree in 2007 from Hefei University of Technology. His research in terests include knowledge management, business intelligence and management informa tion systems.

Hemant K. Jain is W. Max Finley Chair in Business. Free Enterprise and Capitalism. in College of Business at University of Tennessee Chattanooga. He received his Ph. D. in information system from Lehigh University. His research focuses on analysis of social networking communities, support for multidisciplinary cancer care, using virtual worlds for providing medical services, and internet of things and real time enterprises.
