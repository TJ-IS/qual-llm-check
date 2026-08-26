---
otero_id: 2902
otero_key: "B9GDAEE7"
title: "Combining Geographical and Social Influences with Deep Learning for Personalized Point-of-Interest Recommendation"
authors: "Junpeng Guo; Wenxiang Zhang; Weiguo Fan; Wenhua Li"
year: "2018"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2018.1523564"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Combining Geographical and Social Influences with Deep Learning for Personalized Point-of-Interest Recommendation

Junpeng Guo, Wenxiang Zhang, Weiguo Fan & Wenhua Li

To cite this article: Junpeng Guo, Wenxiang Zhang, Weiguo Fan & Wenhua Li (2018) Combining Geographical and Social Influences with Deep Learning for Personalized Point-of-Interest Recommendation, Journal of Management Information Systems, 35:4, 1121-1153, DOI: 10.1080/07421222.2018.1523564

To link to this article: https://doi.org/10.1080/07421222.2018.1523564

![](/api/attachments/B9GDAEE7/fulltext/images/fb19a853984a0d24e11364f5ed3bdf10e5ee65ddf9b75773100e7e1bf31f57a0.jpg)

View supplementary material

![](/api/attachments/B9GDAEE7/fulltext/images/6dc310406b9f89d49277abcfa3b61d05bf2831ae2d42aea298e5669412a226f8.jpg)

Published online: 17 Dec 2018.

![](/api/attachments/B9GDAEE7/fulltext/images/11c624b4c622a08c427d5eaabdd0cfe400cc5464c535e93678a4930383f16ba1.jpg)

Submit your article to this journal

![](/api/attachments/B9GDAEE7/fulltext/images/bf026b43e5b141dd5b55d28a949710a2e851b67330e9d2d5a8ed244bfca60fb6.jpg)

Article views: 19

![](/api/attachments/B9GDAEE7/fulltext/images/7845fff428a1e02e621fe27ac4defe92e4279562300a86d1822d27a305a193c1.jpg)

View Crossmark data

# Combining Geographical and Social Influences with Deep Learning for Personalized Point-of-Interest Recommendation

JUNPENG GUO, WENXIANG ZHANG, WEIGUO FAN, AND WENHUA LI

JUNPENG GUO (guojp@tju.edu.cn) is a professor in the Department of Information Management and Management Science at Tianjin University, Taiwan. He received his Ph.D. in Management Science and Engineering from Tianjin University. His research interests comprise recommender systems, social media, and operations research. His work has appeared in IEEE Intelligent Systems, Computers in Human Behavior, Computational Statistics and Data Analysis, and other journals.

WENXIANG ZHANG (wenxiangzh@tju.edu.cn) is a graduate student pursuing a major in Management Science and Engineering at Tianjin University. His research interests are recommender systems and data mining.

WEIGUO FAN (weiguo-fan@uiowa.edu) is Henry Tippie Endowed Chair in Business Analytics at the University of Iowa. He received his Ph.D. from University of Michigan. His research interests include evolutionary computation, data mining, text mining, social media analytics, Big Data, social computing, and business analytics. He has published more than 200 refereed publications in various journals and conference proceedings. Dr. Fan’s publications have appeared in many premier IS/OM journals such as Information Systems Research, Journal of Management Information Systems, Production and Operations Management, Communications of ACM, IEEE Transactions on Knowledge and Data Engineering, and others.

WENHUA LI (liwh@tju.edu.cn) is an associate professor in the Institute of System Engineering at Tianjin University. She received her Ph.D. in Management Science and Engineering from that university. Her research interests are statistical analysis and financial econometrics. Dr. Li’s work has appeared in Computational Statistics and Data Analysis, Journal of Classification, and several conference proceedings.

ABSTRACT: Personalized point-of-interest (POI) recommendation is important to location-based social networks (LBSNs) for helping users to explore new places and for helping third-party services to launch targeted advertisements. Discovering effective features or representations from check-in data is the key to POI recommendation. Deep learning is a representation-learning method with multiple levels for discovering intrinsic features to better represent user preferences. We analyzed users’ check-in behavior in detail and developed a deep learning model to integrate geographical and social influences for POI recommendation tasks. We used a semirestricted Boltzmann machine to model the geographical similarity and a conditional layer to model the social influence. Experiments with real-world LBSNs showed that our method performed better than other state-of-the-art methods. Theoretically, our study contributes to the effective usage of data science and analytics for social recommender system design. In practice, our results can be used to improve the quality of personalized POI recommendation services for websites and applications.

KEY WORDS: AND PHRASES: location-based recommendations, social recommendations, POI recommendation, deep learning, auto-encoder, semi-RBM, Boltzmann machine, geographical similarity, social networks, location-based commerce.

## Introduction

In the past few years, location-based social networks (LBSNs) with check-in functionality, such as Brightkite, Gowalla, and Jiepang, have failed. A major reason for these failures was the quality of personalized services, which was insufficient to satisfy user needs, even though users were able to share their friends’ experiences of visiting preferred spatial locations [17, 34, 49]. These locations are called points of interest (POIs) and can include restaurants, museums, and stores. However, Foursquare is one of the earliest LBSNs and has been performing very well because of the evolution of its provided services. For example, they recently launched a new application called Marsbot that recommends POIs to users. With this application, there is no need to spend time and energy to research information or read reviews because Marsbot can recommend preferred POIs automatically at any given location. Foursquare not only enables users to share their check-in experience but also provides them with personalized services, especially location-based recommendations. Check-in alone can no longer satisfy the needs of users. Therefore, providing intelligent and personalized services, especially recommendations, is the key to the success of LBSNs.

Personalized POI recommendation can greatly improve the quality of LBSN services and benefits both users and POI owners. For example, users can find POIs that they potentially favor. POI providers can also utilize targeted advertising or sales promotions for specific users. These recommendations not only enhance user stickiness but also increase the revenue of POI providers [36]. To some extent, the quality of the POI recommendation services determines the development prospects of LBSNs. Hence, personalized POI recommendation has become a significant aspect of LBSNs.

However, Marsbot is mainly based on the answers users give to Foursquare’s questions and the places that users frequently visit. In the absence of sufficient analysis about geographical influence, Marsbot mainly recommends POIs near a user’s current location. Moreover, Marsbot does not adequately emphasize the aspect of social influence. Thus, it has great potential for improvement.

In traditional recommendation tasks, item rating scores are taken as representative of a user’s preferences [9]. For POI recommendations, however, the only data that LBSNs can collect at POIs is a user’s check-in frequency. In contrast to traditional rating data, which are on a scale of 1 to 5, check-in data cannot entirely represent user preferences with regard to POIs. For example, a user may check in at one place five times and at another place 100 times. However, this does not mean that the user prefers the latter 20 times more than the former. In addition, the scale of the check-in frequency is not comparable across categories; for example, visiting a museum six times a week should not be valued as equal to visiting a supermarket six times a week. However, most existing methods directly represent the user-POI data as a matrix of visiting frequency [15, 48] or binary numbers (0 or 1), indicating whether a user visited a place [61, 65]. Such representations fail to deeply examine the essentials of check-in behavior or to model user preferences for locations. To address this issue, we can apply term frequency–inverse document frequency (TF-IDF), which is one of the most commonly used term weighting schemes in text mining. It evaluates the importance of a word in a collection of documents [19] by considering not only a word’s frequency (TF) but also its rarity (i.e., IDF). Therefore, the TF-IDF can be used to evaluate how important a location is during check-ins and to derive user preferences from check-in frequency.

Discovering effective features or representations from check-in data is the key to POI recommendation. In the past few years, there has been significant progress in applying the deep learning model to machine intelligence tasks such as computer vision and natural language processing, where features can be learned effectively and deeply [25, 29, 31, 53, 67]. Deep learning is a representation-learning method with multiple levels of representation that are obtained by composing simple nonlinear modules. Each module abstracts higher level representations from lower level data [32]. For example, in computer vision, a picture can be transformed from lower level pixel features into higher level features representing the color, texture, and morphology. Hence, the deep learning model is very good at discovering intrinsic high-level features, which are useful for recommendation tasks. In this paper, we propose a deep learning method for POI recommendation tasks in LBSNs.

The most important features for POI recommendation tasks are geographical data and social influence [6, 15, 21, 38, 49, 65]. These distinguish POI recommendation from conventional recommendation tasks, such as movie recommendations. Tobler’s first law of geography states [41], “Everything is related to everything else, but near things are more related than distant things.” Similarly, POIs close to each other are more likely to be correlated with each other, the representation of which is called geographical similarity. In this research, we propose a new deep learning method based on a restricted Boltzmann machine (RBM) to model the geographical similarity. An RBM is a two-layer network that can learn a probability distribution over its set of inputs and is widely used in deep learning [26, 46]. We used the input layer to represent the POIs, and the probability distribution generates the feature layer. A regular RBM only has connections between two layers, but a semi-RBM can have connections within POIs of the input layer to learn the geographical similarity. Previous studies have rarely used a semi-RBM, but it is well-suited for modeling the correlation between POIs. Owing to the connections between input units, a semi-RBM is well-suited to modeling the geographical proximity of a POI to every other POI.

LBSN users who maintain social links with each other are more likely to share common interests in POIs than strangers [49, 54]. Most previous works derived similarity values from social links and placed them into a traditional collaborative filter [35, 61, 63, 65]. However, the social influence on human behavior is complicated [2, 20, 23, 28, 33, 39, 58, 64], so designing a proper social similarity measurement is extremely difficult. Unlike previous methods, we integrated social influence into our deep learning model by using a conditional layer. With deep learning, there is no need to carefully design a similarity measurement because a machine can be fed with raw data to automatically discover features and relations [32].

Apart from geographical and social influences, many other factors affect check-in behavior, such as the preferences and check-in time [13, 51] of the users. It is nearly impossible to consider all factors, but our deep learning method can implicitly deal with these factors to some extent with multiple levels of features. In this paper, we used a semi-RBM [43, 44] to capture geographical similarity and we used a deep auto-encoder (DAE) [3, 28, 57] with a conditional layer to extract the social correlation. We developed a deep learning model that combines the semi-RBM and DAE to effectively extract preferences and features for POI recommendation.

In summary, this paper has five main contributions:

1. To explore the nature of check-in behavior in LBSNs, the TF-IDF and log transformation were adopted to obtain preferences from the check-in frequency. The new preference data from the check-in behavior better reflects user preferences than directly using frequency or binary data.

2. The geographical and social influences on user check-in behavior were analyzed both theoretically and experimentally. Our results validated that both geographical and social influences are significant.

3. We developed a method for modeling geographical similarity with a semi-RBM [43]. The only difference between an RBM [26] and a semi-RBM is that the latter shows connections between visible layers, so it is well-suited for representing the correlations between POIs. Hence, our semi-RBM method can better explore the geographical similarity among POIs.

4. We used the DAE model to discover high-level features from input data. To model the social correlations, we added a conditional layer to the DAE model. Thus, the social influence on check-in behavior can be captured.

5. To the best of our knowledge, we are the first to combine both geographical and social influences in a deep learning method for POI recommendation tasks. Our proposed model can effectively handle both geographical and social influences to enhance the recommendation performance.

## Related Work

Here, we briefly describe several classical approaches that have been widely applied in POI recommendation tasks and their corresponding limitations. In particular, we highlight related works that consider the factors included in this paper and explain the differences compared to our method.

## POI Recommendation

The main approach to POI recommendation is collaborative filtering (CF), which heavily relies on user–POI check-ins. This approach can be further divided into memory- based and model-based algorithms [9].

Memory-based algorithms include both user-based and item-based CF. These methods predict the target user’s preferences by aggregating the scores of similar users or POIs based on similarity or some specific relationship [48, 61, 65]. POIs are commonly related according to geographical information. For example, Ye et al. [61] modeled the relationship between two POIs by using a power-law distribution (PD) of the distance between them. Zhang and Chow [65] estimated the kernel density to explore the relations of POIs with two-dimensional geographical coordinates (i.e., latitude and longitude). Sarwat et al. applied item-based CF to calculate the spatial similarity of items and considered a travel (distance) penalty [48].

Model-based algorithms recommend certain POIs to users by calculating preferences that indicate the likelihood of visiting different POIs. These preferences are calculated by deriving a model built on the whole dataset [1]. Typical examples of model-based algorithms include matrix factorization and the Bayesian probabilistic model. Matrix factorization has been applied to fuse geographical and social information [6, 15, 21]. Liu et al. predicted user preferences for POIs by using a probabilistic factor model that integrates probabilistic matrix factorization and the Poisson factor model [38]. Yin et al. proposed a probabilistic generative model for user rating profiles based on latent Dirichlet allocation [62].

Whether a memory- or model-based algorithm is used for CF, low-level features are assigned to each user and POI, such as in matrix factorization. Hence, exploring the deep features of user preferences and learning high-order interactions between features are not possible [46]. Deep learning is a representation-learning method with multiple levels of representation that are obtained by composing simple nonlinear modules. These transform the representation at one level into a representation at a higher and more abstract level [27, 32]. This approach is very good at discovering intricate structures in high-dimensional data, so it is applicable to many domains such as image recognition and speech recognition [25, 31].

Discovering effective features or representations from check-in data is the key to POI recommendation. The deep learning model is highly suitable for discovering intrinsic high-level features, which is very useful for POI recommendation tasks.

For POI recommendation, the most important information for user preferences are geographical and social influences [6, 15, 21, 35, 38, 49]. According to Tobler’s first law [41], user check-in behavior exhibits geographical clustering. For example, some researchers have modeled user check-in behaviors by using the PD for the distance between POIs [11, 22, 61]. Cheng et al. found that users tended to check in around several centers and modeled the geographical similarity as a multi-center Gaussian model [15]. Zhang and Chow captured the two-dimensional geographical coordinates by estimating the kernel density [65]. However, we used our proposed deep learning model to explore the geographical similarity among POIs.

Extensive research on social influence [2, 20, 23, 28, 33, 39, 58, 64] has shown that user behavior is greatly influenced by online social friends. Most previous works derived similarity from social links and placed them into a traditional collaborative filter [35, 61, 63, 65]. For example, Ye et al. [61] calculated the social similarity between POIs based on both social connections and check-in behavior and then integrated social similarity into CF. Meanwhile, Cheng et al. considered social influences as regularization and integrated social regularization into a probabilistic matrix factorization model [15]. In contrast to previous methods, we used deep learning to derive social influences between users and consider the check-in data of social friends.

## Deep Learning for Recommendation Tasks

There has not yet been a systematic and comprehensive study on the effect of deep learning on recommendation tasks. In one of the first related studies on neural networks, Salakhutdinov et al. used an RBM for CF [46], but their method is not suitable for POI recommendation. The field of recommender systems has recently begun to embrace the power of deep learning, but mostly in the area of music recommendation [42]. Some attempts have been made to develop deep learning methods for predicting human mobility. For example, Zhou et al. [66] proposed a trajectory embedding model that uses check-in data from LBSNs for POI recommendation and social link prediction. Song et al. [52] and Yang et al. [60] modeled sequential contexts by using deep learning methods such as the recurrent neural network (RNN) and gated recurrent unit (GRU). These methods based on deep learning focus mainly on temporal and sequential contexts.

Unlike previous studies, we tried to model geographical similarity and social influence instead of temporal and sequential contexts. Many deep learning models are available, such as the convolutional neural network (CNN), RNN, and GRU. However, the CNN was designed to process data in the form of multiple arrays; it is better to use the RNN and GRU for modeling sequential contexts [32]. Most importantly, the above models utilize supervised learning; however, human learning is largely unsupervised [32]. We focused on tapping into the potential of unsupervised deep learning methods.

## POI Recommendation with Deep Learning

We derived a data transformation function to better represent user preferences based on the TF-IDF to learn the importance of check-ins for different categories. The key characteristics among check-ins were examined, and the geographical and social influences on check-in behavior were analyzed in detail. Finally, we developed a deep learning model that integrates geographical and social influences for POI recommendation tasks.

## Data Transformation

In traditional recommendation tasks, preferences can be explicitly obtained through a rating score (e.g., on the scale of 1 to 5). However, we do not have explicit rating data in a specific range, only the check-in data of users visiting POIs [5]. In addition, the scale of check-in frequencies is not comparable across categories. Clearly, the check-in frequency data alone cannot entirely represent the degree of user preferences for POIs.

The TF-IDF is one of the most commonly used term weighting schemes in today’s information retrieval/text mining systems [47]. For example, in text mining, the TF-IDF can evaluate how important a word is in a collection of documents by considering both the frequency of the word in a document as well as the rarity of the word in the entire collection [19]. According to TF-IDF design, the importance of category c for a user’s check-ins can be similarly designed as follows:

$$
\beta_ {i c} = \frac {N _ {i c}}{\sum_ {k \in C a t} N _ {i k}} \log \frac {N _ {u s e r} + 1}{N _ {c}},\tag{1}
$$

where $N _ { i k }$ is the number of different POIs belonging to category k that user i has checked into, while all categories are in the set Cat. $N _ { u s e r }$ is the total number of users, and $N _ { c }$ is the number of users that have checked into POIs belonging to category $c . \beta _ { i c }$ is calculated from the product of two parts: the left part represents the frequency of category c in user $i \mathbf { \ ' } _ { \mathbf { S } }$ check-ins, and the right part indicates the rarity of category c in all users’ check-ins. Therefore, the product can measure the importance of category c in user $i \mathbf { \ ' } _ { \mathbf { S } }$ check-ins. For example, if the frequency of category c is higher for user i and rarer for other users, then category c is more important for user i.

Check-in counts are known to follow a highly skewed distribution, so log transformation is a standard practice in the literature [14, 24]. Hence, combining all of the above leads to the following transformation for a specific user i and their preference for location j:

$$
P _ {i j} = \frac {x _ {i j}}{\sum_ {k} x _ {i k}} \beta_ {i c} \log (x _ {i j} + 1),\tag{2}
$$

where c is the category to which location j belongs and $x _ { i j }$ is the check-in frequency of location $j .$ Because many check-in counts are 1, 1 is added to the log transformation to avoid the preference value’s being equal to 0. Here, $\sum _ { k } ^ { x _ { i j } }$ represents the fraction of check-in counts at location j over all check-in counts belonging to user i. The transformation function can alleviate the impact of skewed data so that the user preferences are better represented. In addition, $\frac { x _ { i j } } { \sum _ { k } x _ { i k } }$ is set to the weight based on the visitation frequency, which can indicate the relative preference of user i for each POI j.

## Analysis of Geographical and Social Influences

The main differences between POI recommendation in LBSNs and traditional recommendation are the geographical and social influences. Thus, we conducted a detailed analysis of the geographical and social influences on users’ check-in behavior.

## Key Characteristics of Check-In Data

Data were collected from Foursquare, which is a popular LBSN, and included three datasets: New York, Brooklyn, and San Francisco. LBSNs provide check-in counts of users to POIs and geographical information such as latitude and longitude. In addition, they provide users with direct online social links, which are not weighted. The basic dataset statistics are presented in Table 1.

We studied the key characteristics of user check-ins. The check-in frequency histogram for the distance between POIs visited by the same user is plotted in Figure 1(a). Line charts for the percentages of the number of friends are plotted on the left sides of Figures 1(b)–(d). Finally, the complementary cumulative distribution functions for the fraction of common check-ins with friends and strangers are plotted on the right sides of Figures 1(b)–(d).

Table 1. Statistical Data for the New York, Brooklyn, and San Francisco Datasets Used in This Study

<table><tr><td></td><td>New York</td><td>Brooklyn</td><td>San Francisco</td></tr><tr><td>Number of users</td><td>4,793</td><td>2,706</td><td>3,200</td></tr><tr><td>Number of POIs</td><td>22,451</td><td>5,977</td><td>10,098</td></tr><tr><td>Number of check-ins</td><td>301,548</td><td>61,422</td><td>128,086</td></tr><tr><td>Number of social links</td><td>31,829</td><td>17,499</td><td>19,266</td></tr><tr><td>Sparsity</td><td>99.72%</td><td>99.62%</td><td>99.60%</td></tr></table>

![](/api/attachments/B9GDAEE7/fulltext/images/d6898036fab09df8f6263262cf88cea77782662936c2786f601f77d1f9794cc5.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/61a0395dda3b8753deff57d97224739e7c3245564b7afeb50c32d037c0a5cb68.jpg)  
(a)

![](/api/attachments/B9GDAEE7/fulltext/images/a1bbd1bb6f12ab3213877eaa55b8e19a24a86070e8877637fbdbd833146d7431.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/0a21ca431c55c489aaf60c30ac02c2d1ecbfd58904afa1730490a3a5ddd77eba.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/fe45419c14dc7dceff41c6971c2a391e15a77c9f84e834304336f6e21a1fff7e.jpg)

(b)  
![](/api/attachments/B9GDAEE7/fulltext/images/f99d1c9843945909ccf2798fc0b2ff8d1a3756b65ecce4e9ddf818aa2178c029.jpg)  
(c)

![](/api/attachments/B9GDAEE7/fulltext/images/220877789b57d2c1d934418e873aa205bdb77e0f7f9df9e2c839a8789dddd276.jpg)  
(d)  
Figure 1. Key characteristics of check-ins in the three datasets: (a) New York, Brooklyn, and San Francisco; (b) New York; (c) Brooklyn; (d) San Francisco.

Figure 1(a) shows the check-in frequency for the distance. The distance approximately follows a PD, which is similar to the results in [11, 22, 61]. The three datasets in Figures 1(b)–(d) indicate that most users have fewer than 10 friends. Despite the relatively small number of friends for most users, the fraction of common check-ins with friends is significantly higher than that of check-ins with strangers. Thus, social influence has a certain effect on users’ check-in behaviors. Therefore, the social influence should be considered in POI recommendation tasks.

## Detailed Analysis of Geographical and Social Influences

Many studies on geographical similarity have found that the distance of POIs visited by the same user follows a PD [11, 22, 61], where the model parameters are derived from the entire check-in history of all users. Thus, we used a PD to compute the geographical similarity between POIs:

$$
s = \alpha \times D ^ {\beta},\tag{3}
$$

where α and β are parameters of the PD, D is the distance between POIs visited by the same user, and s refers to the geographical similarity between POIs. Users check-in behavior is influenced by their mobility, which is represented by the geographical distribution of POIs visited.

In LBSNs, users keep direct social links that are not necessary in the real world. The social links are relationships between users in LBSNs that indicate whether two users are friends. These social links are direct and not weighted. The central feature of LBSNs is that users maintain social relations with friends and that they are highly influenced by their friends when making decisions [35, 39, 63, 64]. In LBSNs, users share check-in experiences about places, and their attitudes toward POIs can spread among friends. The more frequently a POI appears in a friend’s check-ins, the more likely a user will check in at the POI. We argue that the social influence from check-ins —though not exactly the same—can serve as a good proxy for word-of-mouth (WOM) in traditional settings. The majority of WOM studies have focused on online consumer reviews. Users are more likely to believe reviews from people they know and trust, that is, friends and family members [12, 16]. Other research has shown that WOM among users with strong social ties is more influential [4, 12]. Thus, WOM has a stronger influence among friends. In LBSNs, users share check-in experiences about places, and a high check-in frequency usually means a positive preference. Sometimes, users share their review rating and reviews as well. However, not all check-ins have review ratings and reviews. Thus, in lieu of the missing data from online reviews and to avoid the complexity of processing them, a key challenge for location-based recommendation has been how to leverage check-in and social network information for fast and quality recommendations [15, 38, 60, 61, 63, 66].

The literature has shown that strong ties are instrumental to spreading both online and real-world behaviors through social networks [10]. To some extent, check-in behavior can act as WOM because it reflects a user’s attitudes toward places and can spread. Thus, check-ins among friends (i.e., the social influence) can be considered a stronger form of WOM. The check-in frequency can be a good proxy for WOM even without rating information. On the other hand, in contrast to ratings or online reviews, check-ins cannot indicate user attitudes, especially negative ones. However, the check-in frequency can represent the popularity of places for people that matter to users. Furthermore, the check-in frequency can influence users’ decisions according to the herding effect in economics [50]. Therefore, in the absence of user ratings or reviews, check-ins can be a good indicator of social influence.

Users’ decisions about visiting a location and their check-in behavior usually occur in real time. Thus, check-in information possesses the advantage of real time distinction. In addition, check-ins tend to continue to influence decisions among social friends. They influence a user’s decision every time his or her friends check into a place. Therefore, check-ins with social influence improve the dissemination of information about POIs among social friends and have a greater influence on a user’s decision to visit.

## Overview of Our Proposed Model

The aforementioned analysis indicates that our proposed deep learning model should not only consider geographical and social influences but also discover implicit factor features, such as preferences. The overall framework of our approach has four parts, as illustrated in Figure 2. First, the user preferences for POIs are derived from the user–POI check-in history. The check-in frequency is transformed to user preferences for POIs. Second, the semi-RBM is used to model the geographical similarity of POIs and RBM to model users’ preferences for POIs. A multilayer structure is constructed one layer at a time based on the semi-RBM and RBM. In concrete terms, the first layer comprises the semi-RBM, which represents the POIs and similarity between them. Then, the RBM is used to build the remaining layers. Note that the hidden layer of the current RBM (semi-RBM) is the visible layer of the next-level RBM. The multilayer RBM (semi-RBM) is used to pre-train the parameters of our model. Third, the model is unfolded to produce the DAE based on the semi-RBM. Fourth, a conditional layer is added to the model based on social links between users to build a deep learning model. The check-in behavior of friends is considered to integrate the social influence into our proposed deep model.

Unsupervised learning catalyzed a revival of interest in deep learning but has since been overshadowed by the successes of purely supervised learning [32]. Learning to represent and transform input features is often an unsupervised task in deep learning. Thus, we chose DAE and attempted to tap into the potential of this model. Inspired by Salakhutdinov et al. [46], who used conditional layers for extra information, we used a conditional layer for friends’ check-in information and connected it to the first hidden layer to learn the features of higher layers. In the DAE, the input and output layers represent POIs. The semi-RBM captures the geographical proximities among POIs; therefore, it is connected to the first and last layers of the DAE. We detail the steps of our method in the following section.

![](/api/attachments/B9GDAEE7/fulltext/images/53f89e2577cb0199fabb311bc3559f65c0813dbe7e5e141012fecb494dc4978a.jpg)  
Figure 2. Framework of our deep learning model.

## Exploiting Geographical and Social Influences with Our Proposed Model

The above analysis on check-in behavior showed that both the geographical and social influences cannot be ignored. Thus, we used the deep learning model to study both of these influences. To study the geographical influence, we propose a semi-RBM model and present the technical details for the proposed DAE model based on the RBM. To study the social influence, we propose a DAE model with a conditional layer and present details on the implementation to produce recommendations.

## Modeling Geographical Similarity with a Semi-RBM

We used a semi-RBM (see online Appendix B) to model the geographical similarity for the pre-training process of our deep learning model [26, 27]. The RBM in online Appendix A is a bipartite connectivity graph with no connections within a layer and is usually used to pre-train a deep learning model. Unlike the RBM, the visible units of the semi-RBM are fully or partially connected to each other. In this study, the visible units of the semi-RBM represent the POIs and the connections among visible units model the geographical similarity among POIs. The semi-RBM is rarely used in existing works, but it is suited to modeling the geographical proximities among POIs owing to the existing connections among visible units. Thus, we used it to extract the geographical proximities.

Many studies have found that the distances of POIs visited by the same user follow a PD [11, 22, 61]. Thus, we used the PD to compute the geographical similarity between POIs based on Equation (3). We considered lateral connections to only exist between POI pairs that are visited by the same user. In addition, the lateral connection weights between visible units are predetermined and equivalent to the geographical similarity between POIs. Thus, we did not need to learn the parameters of the lateral interaction term L (see online Appendix B), which accelerated the learning speed.

In our model, each semi-RBM represents a user, and each visible unit represents a POI that the user has visited. All semi-RBMs have the same number of hidden units, but each user has a different number of visible units because different users have visited different POIs. However, all semi-RBMs share the same set of weights and biases. In other words, when data is fed into the visible units of the model, there are missing values for each user because the user has not checked into some POIs. In this paper, instead of setting a missing value to 0, we ignore these values from all computations, and for the rest we update the connected weights.

The semi-RBM is not only an integral component of our deep learning model but is also used to pre-train our model [26, 27]. For each user, we can obtain a set containing the check-in data for every POI that the user has visited. Here, we refer to the set of a specific user as a training case. The details of learning the semi-RBM with geographical similarity are described in Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1. Learning a semi-RBM with predetermined lateral weights based on k-step contrastive divergence (CD-k)

Input: semi-RBM ($v_1, \ldots, v_m; h_1, \ldots, h_n$), training batch $S$, step $k$ (CD-$k$)
Output: gradient approximations $\Delta w_{ij}, \Delta a_i$, and $\Delta b_j$ for $i = 1, \ldots, m$ and $j = 1, \ldots, n$
Begin

1. For each $v$ in $S$
2. $v^{(0)} = v$
3. For $t = 0, \ldots, k - 1$ do
4. For $j = 1, \ldots, n$ do
5. Sample $h_j^{(t)}$ with Equation (A2) in online Appendix A
6. For $i = 1, \ldots, m$ do
7. For $p = 1, \ldots, m$ do
8. Calculate the distance $D_{ip}$ between POIs $i$ and $p$ based on their physical address
9. Calculate the lateral connection weight (geographical similarity) between POI $i$ and $p$, $L_{ip}$ with Equation (3)
10. Sample $v_i^{(t + 1)}$ with Equation (A6) in online Appendix B
11. For $j = 1, \ldots, n$ do
12. Sample $h_j^{(k)}$ with Equation (A2) in online Appendix A
13. For $i = 1, \ldots, m$, $j = 1, \ldots, n$ do
14. Update $\Delta w_{ij}, \Delta a_i$, and $\Delta b_j$ with Equation (A3) in online Appendix A
End
</div>

In the semi-RBM, $( \nu _ { I } , . . . . , \nu _ { m } )$ represents the units of the visible layer, and $( h _ { I } , . . . , h _ { n } )$ represents the units of the hidden layer. S represents the training batch, and k represents the CD step. In Algorithm 1, one training case is fetched and assigned to the visible units (Steps 1–2). Then, hidden units are sampled from visible units based on the conditional distribution (Steps 4–5). When the hidden units are obtained, the visible units can be reconstructed (Steps 6–10). The above steps are repeated k times $( k = 1$ in most cases) (Steps 3–10). Because the sampling is missing in step $k ,$ for the last iteration the hidden units are sampled from the visible units obtained in step k (Steps 11–12). Finally, the parameters are updated based on CD theory (Steps 13–14).

## DAE with the Geographical Influence based on the Semi-RBM

Here, we introduce the deep learning model based on the semi-RBM for capturing the geographical influence. The auto-encoder comprises an adaptive multilayer encoder network that transforms data into high-level representations (i.e., features) and a similar decoder network that recovers the data from such features [3, 27]. Each layer of features captures strong and high-order correlations between activities of units in the layer below. The encoder network comprises a multilayer semi-RBM and

![](/api/attachments/B9GDAEE7/fulltext/images/e1f84e89ddeb1bedb92983fe57b6e3d6ec4e3bc900ab3182991b162681c0490b.jpg)  
Figure 3. DAE based on the semi-RBM.

RBM that have been pre-trained. Then, the model is unfolded to decoder networks that initially use the same weights, as shown in Figure 3.

## Modeling the User–POI Check-In Preference

Suppose that there are M POIs and N users. Then, there are M units in the input layer (i.e., visible layer of the semi-RBM) that represent all POIs. Each user i has a POI set $L _ { i }$ that represents the locations that user i has checked into. For each user i among N users, the POIs in set $L _ { i }$ correspond to the units in the input layer. Suppose that there are 2R layers in our auto-encoder. We use $\boldsymbol { W } ^ { ( r ) }$ and $\pmb { b } ^ { ( r ) }$ to represent the weights and biases of layer r.

However, each user has visited different locations, which means that there are some missing values in the input layer for each user. We cannot simply set missing values to 0 because the model will learn a negative preference. Instead, each user i has a different auto-encoder, as shown in Figure 3, and every auto-encoder has different input units indicating the corresponding POIs in $L _ { i }$ . However, all auto-encoders for every user share all the corresponding weights and biases (e.g., if the same POI has been visited by some users, the auto-encoders for these users share the same corresponding weights and biases connected to that POI). Users are likely to share more weights if they are more similar to each other. In the training procedure, the corresponding weights are updated only by users associated with those weights. Thus, weight sharing not only captures the similarity among users but also simplifies model learning.

The semi-RBM-based auto-encoder in Figure 3 is obtained by unfolding the multilayer semi-RBM and RBM. Hence, the first layer (input layer) has connections between visible units, and the final layer (output layer) has connections between hidden units that represent the POIs. In our auto-encoder, the visible input of the first layer is the POI’s preference, and the output is the user’s preference for POIs as predicted by the model.

Deep learning usually contains multiple levels of abstract representation that are learned implicitly [32]. Some brief examples are given here for an intuitive illustration. For a POI recommendation, each level contains the POI features or representations. For instance, the first hidden layer may represent more detailed POI features, such as Chinese Sichuan cuisine, Japanese cuisine, western food, supermarkets, bookstores, cafés, and bars. A higher level may represent more abstract features such as food, shops, and entertainment. Similar to image recognition [31] or language processing [25], the features are not explicitly present in the input and are discovered by factorizing the structured relationships between the input and output into multiple micro-rules [32]. Based on the users’ historical data, the model can learn user preferences by discovering multiple features. For example, if a user’s data have stronger associations to Japanese cuisine than western food, the user may like Japanese cuisine better. At a higher level, if a user’s data are more strongly associated with food than with shopping, the user may prefer delicious food rather than shopping. The key aspect for deep learning is that these feature layers are learned from data instead of being designed by human engineers [32].

## Training the Auto-encoder

Pre-training. Optimizing the parameters is difficult with the traditional training method of backpropagation to reduce the reconstruction error. The pre-training procedure [27, 45] has become a popular way to initialize parameters. The greedy training method can perform a global search for a good and sensible region in the parameter space. We used the semi-RBM and RBM to pre-train the auto-encoder. For the first layer (input layer), we use the semi-RBM to pre-train the corresponding parameters (described in Algorithm 1), but for the remaining layers we use the RBM to pre-train the parameters. For each RBM, we consider the hidden units of the previous layer to be the visible units of the current layer, as shown in Figure 3.

Training. After the multi-layer RBMs are pre-trained, we unfold the model to construct an auto-encoder that initially uses the parameters from the pre-trained RBMs. Suppose that T is the training set with N training cases (user-specific) and Outputs is the units of the output layer. As noted previously, each training case t (user-specific) in T is for one unique auto-encoder, and all auto-encoders (based on each training case) share the same corresponding weights and biases. First, we take each training case t (user-specific) in T in the model as the input layer. Then, we construct the hidden units layer-by-layer until the output units are obtained in the final layer based on Equation (A2) in online Appendix A.

In the training procedure, we use the backpropagation method with the chain rule (see online Appendix C). Moreover, we attempt to optimize the parameters by minimizing the squared-error function. Specifically, for a training case t (user-specific) that contains the users visited POI set $L _ { t }$ , we define the cost as a total instantaneous squared-error function:

$$
\operatorname{Loss} (\boldsymbol {w}, \boldsymbol {b}, t) = \frac {1}{2} \sum_ {i \in L _ {t}} \left(y _ {i} - o _ {i}\right) ^ {2},\tag{4}
$$

where $y _ { i }$ is the input value of unit i in the input layer and $o _ { i } \in O u t p u t s$ is the output value of units i in the output layer. For a training case t, we only calculate the units in $L _ { t }$ , and the missing values are not included in the cost function.

Given a training set T of N training cases (users), we can then define the overall cost function as follows:

$$
L o s s (\boldsymbol {w}, \boldsymbol {b}) = \frac {1}{N} \sum_ {t \in T} L o s s (\boldsymbol {w}, \boldsymbol {b}, t) + \frac {\lambda}{2} \| \boldsymbol {w} \| ^ {2}.\tag{5}
$$

The first item in Equation (5) is the total error averaged over the training cases, and the regularization term (i.e., second term) is added to decrease the magnitude of the parameters and prevent overfitting of the problem. The details of the training procedure are provided in Algorithm 2.

```txt
Algorithm 2. Training the auto-encoder

Input: auto-encoder (w, b), training set T, number of layers 2R
Output: auto-encoder (w, b) with optimizing parameters
Begin
1. For i = 1, ..., R do (pre-train procedure)
2. Repeat until converged
3. Pre-train parameters w and b with the semi-RBM (or RBM) training algorithm as described in Algorithm 1 (omitting steps 7–9 in the case of RBM)
4. Unfold the model to produce an auto-encoder containing 2R layers
5. Repeat until converged (fine-tune procedure)
6. For t in T do
7. Construct the auto-encoder layer by layer with Equation (A2) in online Appendix A
8. Calculate Loss(w, b) by summing all of the Loss(w, b, t) based on Equation (5)
9. Update parameters backward (backpropagation).
End
```

As presented in Algorithm 2, we first pre-train the parameters (steps 1–3) and then fine-tune them (steps 5–9). Especially, we unfold the pre-trained multilayer semi-RBM and RBM to initialize the auto-encoder in step 4. In the pre-training procedure, we construct an R-layer semi-RBM (or RBM) matrix and pre-train the parameters layer-by-layer (steps 1 to 3) with Algorithm 1 (steps 7–9 are omitted in the case of the RBM). In the pre-training procedure, the first layer of feature detectors then becomes the visible units for training the next RBM, and this layer-by-layer training can be repeated as many times as desired. In the fine-tuning procedure (steps 5–9), we use the reconstruction error between the input and output data to update the parameters from backward to forward.

## Conditional DAE with the Social Influence

As discussed above, LBSN users keep direct social links that are not weighted, and their check-in behavior is influenced by social links. Hence, we integrated the social influence into our auto-encoder model as a conditional layer that is connected to the first hidden layer, as shown in Figure 4. There have been some applications with a conditional RBM such as motion capture [56] or CF [46], but these conditional layers are not applicable to modeling social information.

![](/api/attachments/B9GDAEE7/fulltext/images/6940503f0dcd84c482e87194f43538b133978eafe7b233ea357bf5bbc249afcb.jpg)  
Figure 4. Conditional auto-encoder based on the semi-RBM.

Unlike previous approaches that considered social influence as some type of similarity or regularization [15, 61], we took the check-in data of the user’s friends as another input for integrating social influence into the model instead of calculating the similarity between users explicitly. Thus, we allow the model to learn social influence on its own. In other words, our model extracts high-level features based not only on the user’s check-in behavior but also on the friends’ check-in preferences in LBSNs. We used the conditional layer to model social influence in the hidden layers.

Let f be a vector of length M (total number of POIs) that indicates the average preference of check-ins among all of the user’s friends. Similar to visible units, we ignore the missing values in f . The conditional auto-encoder can be trained with Algorithm 2. The only difference is the conditional distribution of the first hidden layer, which has the following form:

$$
p \left(h _ {j} | \boldsymbol {v}, \boldsymbol {f}\right) = R e L U \left(\sum_ {i} W _ {i j} v _ {i} + \sum_ {i} f _ {i} C _ {i j} + b _ {j}\right),\tag{6}
$$

where $h _ { j }$ is unit j in the hidden layer, $\nu _ { i }$ is unit i in the visible layer, and C is the connection weight between the conditional layer and first hidden layer. In the pretraining procedure, C is learned with the CD method, similar to learning the biases. This is given by

$$
\Delta C _ {i j} = \varepsilon \big (\langle h _ {j} \rangle_ {d a t a} - \langle h _ {j} \rangle_ {r e c o n} \big) f _ {i}.\tag{7}
$$

During the fine-tuning procedure, the backpropagation algorithm and chain rule can also be applied to update C.

## Generating the Recommendation List

Our model outputs user preferences for all POIs. The POIs are all sorted in descending order of overall preference, and the top K candidates are recommended to the user. Users may keep visiting POIs for which they have a high preference, but they may stop visiting POIs with a low preference. In addition, even if a user has visited a specific POI, LBSNs still need to recommend the POI to the user and notify the user about relevant discounts or promotions. Thus, our model considers all POIs, including those that have already been visited by the user prior to the recommendation.

## Experiments

We conducted several experiments to evaluate the performance of our proposed recommendation method. Separate experiments were conducted to evaluate the geographical and social influences. Other experiments were then conducted to compare the performance of the proposed method with baseline algorithms. The experimental configurations and results are presented here.

## Experimental Data and Metrics

Table 1 presents the datasets used to evaluate the model. Based on the time sequence of the users’ check-in behavior, we divided each dataset into a training set (70%) and test set (30%) for each experiment. In other words, the check-in records in the training set occurred before the records in the test set. This conforms to the actual situation of recommendation tasks.

To evaluate the quality of the POI recommendation, we applied the following evaluation metrics: precision, recall, and F1. Given the top-K (K = 5, 10, 15, 20, 25, 30) recommendation list $L ,$ these metrics are defined below:

$$
P r e c i s i o n @ K = \frac {| L \cap S |}{K} ,\tag{8}
$$

$$
\text { Recall } @ K = \frac {| L \cdot S |}{| S |},\tag{9}
$$

$$
F 1 @ K = \frac {2 * P r e c i s i o n * R e c a l l}{P r e c i s i o n + R e c a l l}.\tag{10}
$$

For precision, S represents the list of POIs visited by the user in the test set. For recall, however, the check-in frequency in the test set is considered. L represents a vector that indicates whether the POI is included in the recommendation list. S is the vector that represents the check-in frequency in the test set.   S represents the sum of the check-in frequencies in the test set. Thus, the recall is the relevant fraction of the retrieved check-in frequency.

The batch gradient descent was used to train the auto-encoder. After the model was validated, the auto-encoder (2R) was set to six layers and a batch size of 256. The detailed model validation procedure is provided in online Appendix D. For the New York dataset, the auto-encoder consisted of an encoder with layers of 10,000, 5,000, and 2,000 POIs, as well as a symmetric decoder. The learning rate was 0.001, and there were 50 epochs. For the Brooklyn dataset, layers contained 2,000, 1,000, and 500 POIs, and were symmetric. The learning rate was 0.0005, and there were 30 epochs. For the San Francisco dataset, layers contained 4,000, 2,000, and 1,000 POIs, and were symmetric. The learning rate was 0.0005, and there were 40 epochs.

## Baseline Algorithms

We selected several typical and classical models as baselines for comparison with our proposed model: traditional CF with geographical and social information (Geo-CF) [61], the geographical similarity-based probabilistic factor model (Geo-PFM) [38], and the RBM for movie recommendations (RBM) [46].

## Geo-CF

This is a traditional memory-based CF algorithm that integrates the geographical similarity from the distance distribution and social influence from social CF. Memory-based CF is a classical and typical method for recommendation tasks. Because our proposed method also considers geographical similarity and social influences, we compared our deep learning model with the traditional CF method to determine which better models both the geographical similarity and social influence.

## Geo-PFM

This method models the geographical similarity based on the probabilistic factor model (PFM) framework, which integrates the probabilistic matrix factorization and Poisson factor model. Geo-PFM is a typical CF algorithm based on the latent factor model that considers geographical similarity for POI recommendation tasks. We attempted to prove that the deep learning method is a better alternative than the existing latent factor model for POI recommendation tasks.

## RBM

This is used for movie recommendations. We compared our deep learning model with the RBM for POI recommendation tasks to demonstrate its advantages for POI recommendation tasks.

## Semi-DAE

This is our proposed deep learning method without a conditional layer.

## CDAE

This is our proposed deep learning method without the semi-RBM layer but with a social conditional layer.

## Semi-CDAE

This is our proposed deep learning method that integrates both geographical similarity and social influence.

## Performance Evaluation of Geographical Similarity and Social Influence in Our Proposed Model

We compared the recommendation accuracies of Semi-DAE, CDAE, and Semi-CDAE for the three datasets to demonstrate the effectiveness of the semi-RBM layer and conditional social layer as well as our model’s ability to manage additional implicit information. We first generated recommendations by using our proposed model with the semi-RBM layer but without the social conditional layer. We then used our proposed model without the semi-RBM layer but with the social conditional layer to generate recommendations. Finally, we added both the conditional social layer and semi-RBM layer to the model to recommend POIs to users.

Figure 5 shows that Semi-CDAE performed better than Semi-DAE for the three datasets. Including the conditional social layer clearly improved the performance in terms of the precision, recall, and F1.

The experimental results with Semi-DAE, CDAE, and Semi-CDAE are presented in Table A1 of online Appendix E. Compared with Semi-DAE, Semi-CDAE improved the performance by 10%–20%. Hence, social information plays an important role in POI recommendation tasks. Our proposed method extracts high-level features based on both the user’s check-in behavior and friends’ check-in preferences in LBSNs.

(a)  
![](/api/attachments/B9GDAEE7/fulltext/images/1cc60c547c90201135ca22b5e4a30145283b76546d5b1c15345c30e187221428.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/9fd3ed8e5be47261fa9d12cc9807800e05693ff458a304448fc51fea9ab4f8f1.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/db06918ee7da348c43806fc77a8fcf37235b0816c8bcd4b6b70ac482bfbc8c63.jpg)

(b)  
![](/api/attachments/B9GDAEE7/fulltext/images/0c77576d2fd1c064c73791a7507f257e8995531a50f038d7872e05bcd32ac631.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/56e150c27e8619d29cc095f9fdac7e718077b15be89150a5be7ed71f0b3c9c04.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/6a330b6116580a7335f2b54bbaf6b1cf24b26bde22da24e5c96b253a430343ab.jpg)

(c)  
![](/api/attachments/B9GDAEE7/fulltext/images/7d13e3e05c4116955b81f17771b083754c8314feeb3d448284f29b92fadfba49.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/e8a82b6f87a5f30e6c71c0da5ad1741aa81174d6e8e07eef99f220ca93f1ee92.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/1de630ebf309e169ea52ac5f4a6e721db3d46c5faeaede4a9d13cd74d7481c1a.jpg)  
Figure 5. Performances of Semi-DAE, CDAE, and Semi-CDAE with three datasets: (a) New York, (b) Brooklyn, and (c) San Francisco.

Compared with CDAE, Semi-CDAE performed much better with the three datasets. Integrating the semi-RBM layer to consider the geographical influence improved the performance of our proposed model. Thus, the experimental results showed that our proposed method effectively handles the social and geographical influences to enhance the accuracy.

These results not only demonstrate that geographical and social influences actually affect a user’s decisions to visit POIs but also show the potential of our algorithm to model these influences and learn user preferences.

Performance Evaluation of Our Proposed Algorithm Compared with Other Approaches

We compared the recommendation accuracies of our proposed model and the baseline algorithms for the three datasets. In addition to our proposed Semi-CDAE, we also generated recommendations with Geo-CF, Geo-PFM, and RBM.

The experimental results are presented in Table A2 of online Appendix E. In most cases, our proposed method achieved improvements of more than 10% compared to the baseline algorithms, which demonstrates its effectiveness for POI recommendation tasks. Figure 6 compares the different methods in terms of precision, recall, and F1.

The experimental results demonstrated that our proposed approach performed much better with the three datasets compared to the other methods. The next-best performance was shown with Geo-CF followed by RBM and Geo-PFM in that order.

Both Geo-CF and Semi-CDAE consider geographical similarity and social influence. Our approach performed much better, which indicates that it models the geographical similarity and social influence more effectively. Hence, the experiment showed that our proposed deep learning method can better extract features from geographical similarity and social information than traditional CF.

The RBM is a class of two-layer undirected graphical models for traditional recommendation tasks such as movies. The RBM can be considered as a preliminary version of deep learning, but it is simply a two-layer model. However, because the RBM does not consider geographical similarity, its performance is reasonable. Our proposed deep learning model is based on the semi-RBM, which is perfect for modeling geographical similarity between POIs. Our approach performed better than the RBM, which means that the semi-RBM can better model geographical similarity, and our proposed deep network works much better.

Geo-PFM is a classical latent factor model for CF. Although Geo-PFM also considers geographical similarity, our method performed much better, which proves that our deep learning method can be a better alternative than the existing latent factor model. However, Geo-PFM did not perform better than Geo-CF. This may be because Geo-PFM considers the geographical factor by dividing POIs into different areas, but the geographical modeling in Geo-CF where the distance between POIs is considered as a PD seems more reasonable. In addition, the social information included in Geo-CF plays an important role in enhancing the recommendation accuracy.

The experimental results not only demonstrate the effectiveness of the deep learning method but also validate our proposed Semi-CDAE for POI recommendations.

## Discussion

Here, we discuss the propensity to disclose location information in LBSNs and the representative problem of datasets used in this study.

(a)  
![](/api/attachments/B9GDAEE7/fulltext/images/dc9b75810e6725d0ed857bfdf7c9bed524abeb914d27ced7baee37adef31cfe6.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/5e34fdb03209b1dfde4de3010ebfb3ae44dbe18fde951ab4607e76b28d4f04c3.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/e5af3d5a7383ef4f61903d42eeb6c0f0d36b3b525f9b96559d696a15b9acee19.jpg)

(b)  
![](/api/attachments/B9GDAEE7/fulltext/images/aa5ab0c0f73c8f5435c4a6f5016782703aab097d1af4b56b6c643732e44324c6.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/668acaf2394e806cd02b4bd8aaf3c0175a2e015de496bb58c033e083da97a89b.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/1a35ca8506f01fb65b603572ca435a92cca5a5149ffee55ac30fc19f73f2f676.jpg)

(c)  
![](/api/attachments/B9GDAEE7/fulltext/images/59a91f99f0dcd5c5fc0f5da40d48bc4399a0b61e47317769881b57621454d8af.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/d94109fa978d000ad8035ecc1c354f06311bd16f6b009b2794dd96397f6d532d.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/b1b9c068ee9088fd7a4dc2b767c5a3a3394d31a9d8821db578533b653fe75bd8.jpg)  
Figure 6. Performances of different approaches with three datasets: (a) New York, (b) Brooklyn, and (c) San Francisco.

## Propensity for Disclosing Location Information

There is a strong self-selection bias on the part of individual users who agree to disclose check-in information (or selectively do so). Information disclosure allows users on LBSNs to maintain relations with friends, to develop new friendships, and to find support and information [8, 55]. A few studies [18, 37] have shown that users tend to disclose and check into places that they find interesting. Thus, the information that users choose to disclose can better represent their preferences. Automatic check-in data based on GPS trajectories have been researched [40], and the distribution that describes human mobility with manual check-in data has been found to hold for automatic check-ins as well. The PD of human mobility, which is similar to the distribution in LBSNs, has also been noted with many other programs, such as tracking with banknotes [11], cellular towers [22], and GPS [7, 30].

However, the propensity to disclose location information may influence POI recommendation. Thus, we tried to compare user types by dividing users into four groups based on the numbers of POIs at which users checked in: <10 POIs, 11–50 POIs, and so on. We compared the performances of all algorithms for different user groups given a recommendation list number of k = 15.

While not perfect, these four groups represented users with different degrees of propensity to disclose location information. Figure 7 shows that the recommendation performance was better when users disclosed more check-in information. Our proposed method performed better than the benchmarks for all four groups. Therefore, the propensity to disclose location information may influence the performance, but our proposed method still performed the best in all cases.

Owing to our limited data sources, we could not compare users who do and do not disclose their location information. In addition, we did not have information on automatic check-ins, so a comparison was difficult. In future work, we will focus on different types of users and analyze their influence on our proposed model.

## Representativeness of the datasets

The datasets contained different types of users; some checked into less than 10 POIs, while others checked into more than 100. The distribution of our datasets is consistent with prior research studies using the same data source [15, 38, 60, 61, 63, 66].

To further address the potential self-selection bias issue and representativeness of the datasets, we divided users into two groups according to their check-in times and compared the performances. Users in group 1 checked in before users in group 2. We found the distributions of the two groups were quite similar. We evaluated the performances of our algorithm and the benchmarks for the two split datasets, and the results are summarized in the following section.

Figures 8 and 9 show that groups 1 and 2 contained different users who checked in at different time periods. The performance remained nearly the same for both groups, and our proposed method performed the best. This indicates that the performance of these methods varies minimally over time. In other words, our performance advantage still holds for users newly checked in. Therefore, our dataset is fairly representative, and selfselection bias does not pose a serious issue regarding the validity of the results.

## Implications and Conclusions

In this section, we discuss the implications of our study and conclude with future works and the contributions of our paper.

(a)  
![](/api/attachments/B9GDAEE7/fulltext/images/2c5efd3cfe30b3053b8c7562f630bb2d94424cfb0b099ffab066768f17d56e68.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/3419534586013e4ec7a82787f7b902a78e3999920d987187470db111734321dd.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/2f92b005d13b8017ca59e8dfcf87cfa10a4de227b61185b330366a553942eb45.jpg)

(b)  
![](/api/attachments/B9GDAEE7/fulltext/images/a315e3f273eb92ee5749144a240131980d3e2213fee8a0dbb663b4443b15b274.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/3cd7e463e0c21f48d8ec6257fdd7532dffd1c93b17fff7415d85d9f6938ffc66.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/662c8b86b5701242ccfd287d39360bff6e90a2d40942a4f3409ae04f02d7fbfc.jpg)

(c)  
![](/api/attachments/B9GDAEE7/fulltext/images/754f6fbc4151f54e84c3bb9821018e8005345dee05e80eaf055425e8bd8d2e9f.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/f192c83708f66a724fd8337aab2c0a4a7c94844f8f79ec55d770968d3fc157e3.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/437d925400da8e32bcf3d7b95f9f681a9485eb7cdb088dbc51cd66907576e43a.jpg)  
Figure 7. Performances of different users with three datasets: (a) New York, (b) Brooklyn, and (c) San Francisco.

## Implications

The results suggest that geographical and social influences are extremely important for enhancing POI recommendation services. The proposed deep learning method can be a better alternative than current approaches for POI recommendation tasks. In addition, personalized services, especially recommendation services based on location, play a critical role in LBSN development. The theoretical and practical implications are discussed in the following section in detail.

(a)  
![](/api/attachments/B9GDAEE7/fulltext/images/81678bef080e1a1c6bc7b52fbc9e8d1d123da9ad83395b921ee3e050522b8d73.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/69f54aa8dcce84b0f821106d531299e6aebccc3e9b69eb3a20a895c22174e3a4.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/2016d355e56bbc3f36dd53b3bc5195afaa1eee51766349908dacf392aeb4c182.jpg)

(b)  
![](/api/attachments/B9GDAEE7/fulltext/images/f51b94fdffcc96dad76efd85622748a818839cbd2c34eeae431d7ec4d157b1b8.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/d848803171e33da2cbf0af7a45885590639e919da6b40ea76a1407e872590858.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/c8d9d08c1b63ae55959911b822e575d2f32fd664161060fb900e4acf4203c9f7.jpg)

(c)  
![](/api/attachments/B9GDAEE7/fulltext/images/9e9be834d3b45677b33ea39a70327ad91f74c65e0b47c644aaf063622f605e2b.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/f852a58c14bc4b989ad8d1b4428ca0cb2c8f61488701a9481a257f4c7582c4a4.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/5ba2a76c3ad117da873c829cd64cf6f236ebd425fc81916b8b6fbec05e9e3a1f.jpg)  
Figure 8. Performance of user group 1 with three datasets: (a) New York, (b) Brooklyn, and (c) San Francisco.

## Theoretical Implications

Our study contributes to the design science paradigm in social recommender system design by the effective usage of data science and analytics.

To the best of our knowledge, we are one of the first groups to leverage deep learning for social recommendation in the LBSN context. Prior research on recommender systems focused mostly on developing and evaluating the underlying algorithms that generate recommendations. However, the effectiveness of the recommendations is determined by many factors other than the algorithms, including the recommendation input [59]. We designed not only a deep learning algorithm for POI recommendations but also a function to transform check-in data into preferences. Better input is the key to successful recommendations. We used implicit information such as check-ins and friendships to obtain very satisfactory results. Prior recommender systems with explicit preferences often required more effort by users. However, the implicit data that we used are less burdensome and lead to a greater perceived ease of use and satisfaction with the recommender system. Therefore, future recommender system design should seriously consider using implicit data, and more research should be conducted in this direction.

(a)  
![](/api/attachments/B9GDAEE7/fulltext/images/100da43d6323b63ab308f6230e473dcd13262839d742cbf0d46cfdddd1f04262.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/8ae3f7b16d89b56a5b5bdaefffe95439f28a160245b92ad4e5183c99f5dcd54e.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/75f51351fd52f05c86382739b2a1a6ffe501350bac58f12534e0d5ca80c10049.jpg)

(b)  
![](/api/attachments/B9GDAEE7/fulltext/images/99e5cd144f0a2e538e6d34ed0745ac951114e0eab05520d9461a83f650fa79f4.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/87dff7a1e3f9411d4736143d50788d686324a86c341770f6f17a12e932d68ea5.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/193bdc0a9f0430b86075a200c31a0ef7c2b56990af7607e60f0cc06a8c11c318.jpg)

(c)  
![](/api/attachments/B9GDAEE7/fulltext/images/a9822be3af088d79d7f7f8bb1d873be87a6587bd04d7f79cb247ec1257caf995.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/9dacbea70dd56dc3e08f643fd637d5fc4382c59a08d092d9782be4b7e71c7d93.jpg)

![](/api/attachments/B9GDAEE7/fulltext/images/2754c4eb6394f178e865ad7601cb88cf73573170a50c5b61efba1842c2465e57.jpg)  
Figure 9. Performance of user group 2 with three datasets: (a) New York, (b) Brooklyn, and (c) San Francisco.

We demonstrated the value of leveraging social influence information for effective social recommendation in the LBSN context. Our results showed that geographical and social influences are very important with regard to POI recommendation services. Social influence is an effective predictor for LBSN POI recommendations when rating and review texts are not available. Our results suggest that both geographical and social influences are significant. In reality, many other factors may affect users’ check-in behavior. Thus, we should consider as many factors as possible for POI recommendation tasks in LBSNs.

From a data science perspective, we present a new way of combining geographical and social influence information by using deep learning techniques. Conventional techniques are limited because they require careful engineering and considerable domain expertise to design a feature extractor for each factor [32]. Therefore, it is nearly impossible to include all factors for POI recommendation explicitly. However, the deep learning model is extremely good at discovering implicit features automatically. Our results suggest that the deep learning model is very effective at learning these factors at abstract high levels. Thus, deep learning is a superior alternative for recommendations in LBSNs, especially when multiple unknown features exist, because of its ability to discover features implicitly.

We demonstrated the practical value of using a semi-RBM model to model geographical similarity in the LBSN context. Our experiments demonstrated that the semi-RBM model and proposed Semi-CDAE method learn geographical similarity well. The most distinct characteristic of these models is that internal connections exist within certain layers, which can be used to represent the geographical similarities among POIs. For location-based tasks such as POI recommendation, geographical similarity is the most important characteristic. Thus, we proposed a deep learning model with some modifications for this specific task. In other words, the deep learning model can be modified for location-based tasks such as POI recommendation. This design philosophy goes beyond location-based tasks and can be applied to other tasks with obvious correlations among objects.

Our study on applying deep learning to POI recommendation is just the beginning of a long series of studies that have leveraged deep learning and other data science techniques for social recommendation. We hope that our research can spark and inspire others, especially data science researchers, to continue explore this exciting area by leveraging available information from user demographics and behavior.

## Implications for Practice

Currently, most social websites or applications include a check-in service or similar services for users to share their experience. For example, Facebook or Twitter users can share their pictures, feelings, and locations with others. On the Meituan-Dianping website,<sup>2</sup> which is the largest Chinese online-to-offline platform, users can share their experience of visiting locations and provide comments on food. However, personalized services, especially POI recommendation, have not been adequately provided. Moreover, the check-in data contain rich information about users and POIs, which can be used to improve such personalized services. These services, especially those based on location, have a critical role in LBSN development. Therefore, improving the POI recommendation service of LBSNs for mobile users should be treated as a top priority.

Our analysis demonstrated that both geographical and social influences are very important to check-in behavior. Considering the geographical influence through the integration of a semi-RBM layer and the social influence through the integration of a conditional layer improved the performance of our proposed model in the experiments. Therefore, both geographical and social influences should be considered for POI recommendation tasks.

The key to improving service quality is to adopt effective and accurate approaches for personalized POI recommendations in LBSNs. Our proposed method can predict user preferences accurately with regard to spatial items and can be applied to any recommendation service related to locations. The proposed method can be used to help users discover POIs aligned to their personal preferences in order to enrich their lives and reduce the search time. User preferences can be used to deliver POI ads to specific audiences in a targeted one-to-one manner. POI recommendation makes this delivery possible and is important for increasing user engagement and improving conversion rates for POI providers to increase their revenue. Our method allows LBSNs to target POI ads to specific individuals and build a connection between users and POIs. Through such a connection, LBSNs can achieve stable and longterm development with strong loyalties from users and POIs. Our proposed method can be used for personalized POI recommendation.

Geographical influence is very important to location-based services, and the geographical similarity to a PD is applicable to these location-based services. Thus, recommender systems should adopt geographical similarity for the design of location-based services. Moreover, considering the social influence was found to significantly improve recommendations. Thus, the social influence should be included in recommender system design.

## Conclusions

The main differences between POI recommendation in LBSNs and traditional recommendation are the geographical and social influences. We conducted a detailed analysis and validated the significance of geographical and social influences on user check-in behavior. We then proposed and validated a deep learning model that considers both geographical and social influences. We showed that our deep learning model can learn factors such as preferences and categorize information by transforming raw input data into a suitable internal representation or feature [32].

To explore user preferences from check-in history, we developed a method of transforming check-in data to POI preferences that represent users’ true interest. We developed a deep learning method with a semi-RBM to model the geographical similarity. We then added a conditional layer to extract the social influence and similar interests among friends. To evaluate the performance of our proposed algorithm, we conducted several experiments with real check-in records of LBSNs. The results demonstrated that our proposed algorithm improves the recommendation accuracy compared to other methods.

Because we only used social and check-in data in this study, further research on modeling different types of data will be performed in future work. Data are the key to deep learning methods. Thus, we need to study the integration of different types of data such as time and reviews into our existing model to further improve the recommendation accuracy. Owing to limited data, we could not perform a full comparison between users with different propensities for disclosing their location information. Future studies can leverage such data if available to examine different types of users and their influence on our proposed model.

## Supplemental Material

Supplemental data for this article can be accessed on the publisher’s website.

## NOTES

1. https://support.foursquare.com/hc/en-us/articles/217988268-Foursquare-Marsbot 2. www.meituan.com/www.dianping.com

## REFERENCES

1. Adomavicius, G.; and Tuzhilin, A. Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Transactions on Knowledge and Data Engineering, 17, 6 (2005), 734749.

2. Ajorlou, A.; Jadbabaie, A.; and Kakhbod, A. Dynamic pricing in social networks: The word-of-mouth effect. Management Science, 64, 2 (2018), 971–979.

3. Alain, G.; and Bengio, Y. What regularized auto-encoders learn from the data-generating distribution. The Journal of Machine Learning Research, 15, 1 (2014), 3563–3593.

4. Amblee, N.; and Bui, T. Harnessing the influence of social proof in online shopping: The effect of electronic word of mouth on sales of digital microproducts. International Journal of Electronic Commerce, 16, 2 (2011), 91–114.

5. Bao, J.; Zheng, Y.; Wilkie, D.; and Mokbel, M. Recommendations in location-based social networks: A survey. GeoInformatica, 19, 3 (2015), 525–565.

6. Baral, R.; and Li, T. Exploiting the roles of aspects in personalized POI recommender systems. Data Mining and Knowledge Discovery, 32, 2 (2018), 320–343.

7. Bazzani, A.; Giorgini, B.; Rambaldi, S.; Gallotti, R.; and Giovannini, L. Statistical laws in urban mobility from microscopic GPS data in the area of Florence. Journal of Statistical Mechanics: Theory and Experiment, 2010, 05 (2010), 823–831.

8. Belk, R. Sharing. Journal of Consumer Research, 36, 5 (2009), 715–734.

9. Bobadilla, J.; Ortega, F.; Hernando, A.; and Gutiérrez, A. Recommender systems survey. Knowledge-Based Systems, 46(2013), 109–132.

10. Bond, R.M.; Fariss, C.J.; Jones, J.J.; Kramer, A.D.; Marlow, C.; Settle, J.E.; and Fowler, J.H. A 61-million-person experiment in social influence and political mobilization. Nature, 489, 7415 (2012), 295–298.

11. Brockmann, D.; Hufnagel, L.; and Geisel, T. The scaling laws of human travel. Nature, 439, 7075 (2006), 462–465.

12. Brown, J.J.; and Reingen, P.H. Social ties and word-of-mouth referral behavior. Journal of Consumer Research, 14, 3 (1987), 350–362.

13. Cai, G.; Lee, K.; and Lee, I. Itinerary recommender system with semantic trajectory pattern mining from geo-tagged photos. Expert Systems with Applications, 94, (2018), 32–40.

14. Chai, H.S.; and Bailey, K.R. Use of log‐skew‐normal distribution in analysis of continuous data with a discrete component at zero. Statistics in Medicine, 27, 18 (2008), 3643– 3655.

15. Cheng, C.; Yang, H.; King, I.; and Lyu, M.R. A unified point-of-interest recommendation framework in location-based social networks. ACM Transactions on Intelligent Systems and Technology, 8, 1 (2016), 10.

16. Cheung, C.M.K.; and Thadani, D.R. The impact of electronic word-of-mouth communication: A literature analysis and integrative model. Decision Support Systems, 54, 1 (2012), 461–470.

17. Costa, H.; Merschmann, L.H.C.; Barth, F.; and Benevenuto, F. Pollution, bad-mouthing, and local marketing: The underground of location-based social networks. Information Sciences, 279, (2014), 123–137.

18. Cramer, H.; Rost, M.; and Holmquist, L.E. Performing a check-in: Emerging practices, norms and ‘conflicts’ in location-sharing using foursquare. In Proceedings of the 13th International Conference on Human Computer Interaction with Mobile Devices and Services. New York: ACM, 2011, pp. 57–66.

19. Erra, U.; Senatore, S.; Minnella, F.; and Caggianese, G. Approximate TF–IDF based on topic extraction from massive message stream using the GPU. Information Sciences, 292, (2015), 143–161.

20. Fang, X.; and Hu, P.J. Top persuader prediction for social networks. MIS Quarterly, 42, 1 (2018), 63–82.

21. Gao, R.; Li, J.; Li, X.; Song, C.; and Zhou, Y. A personalized point-of-interest recommendation model via fusion of geo-social information. Neurocomputing, 273, (2018), 159–170.

22. Gonzalez, M.C.; Hidalgo, C.A.; and Barabasi, A.L. Understanding individual human mobility patterns. Nature, 453, 7196 (2008), 779.

23. Hao, H.; Padman, R.; Sun, B.; and Telang, R. Quantifying the impact of social influence on the information technology implementation process by physicians: A hierarchical Bayesian learning approach. Information Systems Research, 29, 1 (2018), 25–41.

24. Hassanzadeh, F.; and Kazemi, I. Analysis of over-dispersed count data with extra zeros using the Poisson log-skew-normal distribution. Journal of Statistical Computation and Simulation, 86, 13(2016), 2644–2662.

25. Hinton, G.; Deng, L.; Yu, D.; Dahl, G.E.; Mohamed, A.; Jaitly, N.; Senior, A; Vincent, V.; Nguyen, P; Sainath, T.N.; and Kingsbury, B. Deep neural networks for acoustic modeling in speech recognition: The shared views of four research groups. IEEE Signal Processing Magazine, 29, 6 (2012), 82–97.

26. Hinton, G. E. A practical guide to training restricted Boltzmann machines. In Neural Networks: Tricks of the Trade. Berlin: Springer, 2012, pp. 599–619.

27. Hinton, G. E.; and Salakhutdinov, R. R. Reducing the dimensionality of data with neural networks. Science, 313, 5786 (2006), 504–507.

28. Hong, Y.; Pavlou, P.; Wang, K.; and Shi, N. On the role of fairness and social distance in designing effective social referral systems. MIS Quarterly, 41, 3 (2017), 787–809.

29. Ioannidou, A.; Chatzilari, E.; Nikolopoulos, S.; and Kompatsiaris, I. Deep learning advances in computer vision with 3d data: A survey. ACM Computing Surveys, 50, 2 (2017), 20.

30. Jiang, B.; Yin, J.; and Zhao, S. Characterizing the human mobility pattern in a large street network. Physical Review E, 80, 2 (2009), 21136.

31. Krizhevsky, A.; Sutskever, I.; and Hinton, G.E. Imagenet classification with deep convolutional neural networks. In Proceedings of the 25th International Conference on

Neural Information Processing Systems. Vol. 1. Red Hook, NY: Curran Associates Inc., 2012, pp. 1097–1105.

32. LeCun, Y.; Bengio, Y.; and Hinton, G. Deep learning. Nature, 521, 7553 (2015), 436.

33. Lee, G. M.; Qiu, L.; and Whinston, A.B. A friend like me: Modeling network formation in a location-based social network. Journal of Management Information Systems, 33, 4 (2016), 1008–1033.

34. Li, N.; and Chen, G. Sharing location in online social networks. IEEE Network, 24, 5 (2010), 20–25.

35. Li, Y.M.; Chou, C.L.; and Lin, L.F. A social recommender mechanism for locationbased group commerce. Information Sciences, 274, (2014), 125–142.

36. Liang, T.P.; Lai, H.J.; and Ku, Y.C. Personalized content recommendation and user satisfaction: Theoretical synthesis and empirical findings. Journal of Management Information Systems, 23, 3 (2006), 45–70.

37. Lindqvist, J.; Cranshaw, J.; Wiese, J.; Hong, J.; and Zimmerman, J. I’m the mayor of my house: Examining why people use Foursquare – a social-driven location sharing application. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. New York: ACM, 2011, pp. 2409–2418.

38. Liu, B.; Xiong, H.; Papadimitriou, S.; Fu, Y.; and Yao, Z. A general geographical probabilistic factor model for point of interest recommendation. IEEE Transactions on Knowledge and Data Engineering, 27, 5 (2015), 1167–1179.

39. Ma, L.; Krishnan, R.; and Montgomery, A.L. Latent homophily or social influence? An empirical analysis of purchase within a social network. Management Science, 61, 2 (2014), 454–473.

40. Malmi, E.; Do, T.M.T.; and Gatica-Perez, D. Checking in or checked in: comparing large-scale manual and automatic location disclosure patterns. In Proceedings of the 11th International Conference on Mobile and Ubiquitous Multimedia. New York: ACM, 2012, p. 26.

41. Miller, H. J. Tobler’s first law and spatial analysis. Annals of the Association of American Geographers, 94, 2 (2004), 284–289.

42. Van den Oord, A.; Dieleman, S.; and Schrauwen, B. Deep content-based music recommendation. In Proceedings of the 26th International Conference on Neural Information Processing Systems. Volume 2. Red Hook, NY: Curran Associates Inc., 2013, pp. 2643–2651.

43. Osindero, S.; and Hinton, G. Modeling image patches with a directed hierarchy of Markov random fields. In Proceedings of the 20th International Conference on Neural Information Processing Systems. Red Hook, NY: Curran Associates Inc., 2007, pp. 1121-1128.

44. Salakhutdinov, R. Learning and evaluating Boltzmann machines. Technical Report UTML TR 2008-002. Toronto: University of Toronto, 2008.

45. Salakhutdinov, R.; and Hinton, G. An efficient learning procedure for deep machines. Neural Computation, 24, 8 (2012), 1967-2006.

46. Salakhutdinov, R.; Mnih, A.; and Hinton, G. Restricted Boltzmann machines for collaborative filtering. In Proceedings of the 24th International Conference on Machine Learning. New York: ACM, 2007, pp. 791–798.

47. Salton, G.; and McGill, M.- J. Introduction to Modern Information Retrieval. New York: McGraw-Hill, Inc., 1986.

48. Sarwat, M.; Levandoski, J.- J.; Eldawy, A.; and Mokbel, M.- F. LARS\*: An efficient and scalable location-aware recommender system. IEEE Transactions on Knowledge and Data Engineering, 26, 6 (2014), 1384–1399.

49. Shi, Z.; and Whinston, A.B. Network structure and observational learning: Evidence from a location-based social network. Journal of Management Information Systems, 30, 2 (2013), 185–212.

50. Shiller, R.J. Conversation, information, and herd behavior. The American Economic Review, 85, 2 (1995), 181–185.

51. Si, Y.; Zhang, F.; and Liu, W. CTF-ARA: An adaptive method for POI recommendation based on check-in and temporal features. Knowledge-Based Systems, 128, (2017), 59–70.

52. Song, X.; Zhang, Q.; Sekimoto, Y.; Shibasaki, R.; Yuan, N.J.; and Xie, X. Prediction and simulation of human mobility following natural disasters. ACM Transactions on Intelligent Systems and Technology (TIST), 8, 2 (2017), 29.

53. Sun, S.; Luo, C.; and Chen, J. A review of natural language processing techniques for opinion mining systems. Information Fusion, 36, (2017), 10–25.

54. Susarla, A.; Oh, J.H.; and Tan, Y. Influentials, imitables, or susceptibles? Virality and word-of-mouth conversations in online social networks. Journal of Management Information Systems, 33, 1 (2016), 139–170.

55. Taddei, S.; and Contena, B. Privacy, trust and control: Which relationships with online self-disclosure? Computers in Human Behavior, 29, 3 (2013), 821–826.

56. Taylor, G.W.; Hinton, G.E.; and Roweis, S.T. Modeling human motion using binary latent variables. In Advances in Neural Information Processing Systems 19. La Jolla, CA: NIPS Foundation, 2007, pp. 1345–1352.

57. Vincent, P.; Larochelle, H.; Lajoie, I.; Bengio, Y.; and Manzagol, P. A. Stacked denoising autoencoders: Learning useful representations in a deep network with a local denoising criterion. Journal of Machine Learning Research, 11 (Dec. 2010), 3371–3408.

58. Wang, W.; and Benbasat, I. Empirical assessment of alternative designs for enhancing different types of trusting beliefs in online recommendation agents. Journal of Management Information Systems, 33, 3 (2016), 744–775.

59. Xiao, B.; and Benbasat, I. E-commerce product recommendation agents: Use, characteristics, and impact. MIS Quarterly, 31, 1 (2007), 137–209.

60. Yang, C.; Sun, M.; Zhao, W.X.; Liu, Z.; and Chang, E.Y. A neural network approach to jointly modeling social networks and mobile trajectories. ACM Transactions on Information Systems, 35, 4 (2017), 36.

61. Ye, M.; Yin, P.; Lee, W.C.; and Lee, D.L. Exploiting geographical influence for collaborative point-of-interest recommendation. In Proceedings of the 34th International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM, 2011, pp. 325–334.

62. Yin, H.; Cui, B.; Chen, L.; Hu, Z.; and Zhang, C. Modeling location-based user rating profiles for personalized recommendation. ACM Transactions on Knowledge Discovery from Data, 9, 3 (2015), 19.

63. Ying, J.J.C.; Kuo, W.N.; Tseng, V.S.; and Lu, E.H.C. Mining user check-in behavior with a random walk for urban point-of-interest recommendations. ACM Transactions on Intelligent Systems and Technology, 5, 3 (2014), 40.

64. Yuan, T.; Cheng, J.; Zhang, X.; Liu, Q.; and Lu, H. How friends affect user behaviors? An exploration of social relation analysis for recommendation. Knowledge-Based Systems, 88, (2015), 70–84.

65. Zhang, J.D.; and Chow, C.Y. CoRe: Exploiting the personalized influence of twodimensional geographic coordinates for location recommendations. Information Sciences, 293, (2015), 163–181.

66. Zhou, N.; Zhao, W.X.; Zhang, X.; Wen, J.R.; and Wang, S. A general multi-context embedding model for mining human trajectory data. IEEE Transactions on Knowledge and Data Engineering, 28, 8 (2016), 1945-1958.

67. Zhou, S.; Qiao, Z.; Du, Q.; Wang, A.; Fan, W.; and Yan, X. Measuring customer agility using big data text analytics. Journal of Management Information Systems, 35, 2, (2018), 510–539.
