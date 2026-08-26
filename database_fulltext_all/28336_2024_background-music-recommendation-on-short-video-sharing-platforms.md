---
otero_id: 28336
otero_key: "ECJCETUX"
title: "Background Music Recommendation on Short Video Sharing Platforms"
authors: "Jiawei Chen; Luo He; Hongyan Liu; Yinghui (Catherine) Yang; Xuan Bi"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0093"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Background Music Recommendation on Short Video Sharing Platforms

Jiawei Chen,<sup>a</sup> Luo He,<sup>b</sup> Hongyan Liu,<sup>b</sup> Yinghui (Catherine) Yang,<sup>c,</sup>\* Xuan Bi<sup>d</sup>

<sup>a</sup> School of Information Management and Engineering, Shanghai University of Finance and Economics, Shanghai 200433, China; <sup>b</sup> School of Economics and Management, Tsinghua University, Beijing 100084, China; <sup>c</sup> Graduate School of Management, University of California, Davis, Davis, California 95616; <sup>d</sup> Carlson School of Management, University of Minnesota, Minneapolis, Minnesota 55455 \*Corresponding author

Contact: chenjiawei@mail.shufe.edu.cn, https://orcid.org/0000-0001-6116-7232 (JC); heluo240808@163.com, https://orcid.org/0000-0002-5693-262X (LH); liuhy@sem.tsinghua.edu.cn, https://orcid.org/0000-0002-4902-1078 (HL); yiyang@ucdavis.edu, https://orcid.org/0000-0001-6984-0102 (Y(C)Y); xbi@umn.edu, https://orcid.org/0000-0002-4683-1411 (XB)

Received: February 5, 2022 Revised: February 3, 2023; November 16, 2023 Accepted: December 18, 2023 Published Online in Articles in Advance: January 31, 2024

https://doi.org/10.1287/isre.2022.0093

Copyright: © 2024 INFORMS

Abstract. On short video sharing platforms, users often choose background music for their videos. In this paper, we study the problem of background music recommendation for short videos on short video sharing platforms. In our recommendation setting, the item (music) is not recommended directly to the user, but to the video created by the user. When making music recommendations for videos, we consider three important players: users, videos, and music. We define a unique background music recommendation problem and design a novel background music recommendation model to address the problem. We propose a model based on the deep learning framework to effectively address the distinctive three-way relationships among users, videos, and music. Our model considers not only the conventional user–music alignment, but also the alignment between videos and music. To evaluate our model, we conduct comprehensive experiments on real-world data collected from one of the most popular short video sharing platforms. Our proposed model significantly outperforms other existing models in recommendation performance. The superiority of our proposed model remains consistent across various scenarios, including cold-start recommendations, data sets with varying density levels, and data sets spanning diverse video categories.

History: Gautam Pant, Senior Editor; Jingjing Zhang, Associate Editor. Funding: This work was partly supported by Major Program of the National Social Science Fund of China [Grant 20&ZD161].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0093.

Keywords: recommendation systems • background music recommendation • deep learning

## 1. Introduction

In recent years, short video sharing platforms have transformed the user-generated content industry with apps such as TikTok, Douyin, and Mojo becoming increasingly popular. For example, reported by Blacker (2023), TikTok has maintained its position as the most downloaded app in the world for three consecutive years. Some traditional media platforms have also incorporated short video sharing capacities, such as YouTube Shorts, Instagram Reel, Facebook Reels, and Snapchat Spotlight. A user (i.e., content producer) who posts the short video often picks a background music (BGM) clip for the original video before publishing the final video on the platform. As shown in Figure 1, a platform recommends background music clips (in Figure 1(b)) to the original video (in Figure 1(a)). Here, in this paper, we study the problem of background music recommendation for short videos on short video sharing platforms. Note that our focus is on short videos instead of longer ones because longer videos may require multiple music clips with different themes.

Choosing the right background music can potentially improve the quality of the video, enhance viewer engagement, and eventually lead to overall prosperity of the platform. Liao et al. (2009) show that matching video with appropriate music in music videos could lead to attractive effects. Given the large number of music clips available on the platform, recommending music clips can significantly improve the efficiency of the process, reducing the time a content producer may need to listen to and evaluate music pieces.

To address these problems, personalized recommendation technology can be used. There are some studies for matching music clips with videos automatically (Liao et al. 2009, Kuo et al. 2013, Lin et al. 2014, Lin and Shan 2017, Pre´tet et al. 2021, Yi et al. 2021). However, these studies on background music recommendation make recommendations mainly based on the connection between music clips and videos without taking video producers’ preferences into consideration. When making music recommendations for videos, there are actually three important players to consider: users, videos, and music. This presents the first challenge we face when designing the background music recommendation method in our setting in which the item (music) is not recommended directly to the user but to the video created by the user. Note that some existing studies, such as on user-generated content (UGC) and contextbased recommendations, also consider three different players (producer–consumer–UGC and product–buyer–- context). However, as we elaborate in Section 2, they are very different recommendation tasks, and their solutions cannot be used to effectively address our background music recommendation problem. The second challenge we encounter is that every original video introduced to the platform is new, lacking any prior interactions with music. Traditional recommendation methods typically rely on learning user preferences and item characteristics from historical user–item interaction data. However, in the context of recommending music clips for videos, each video is new, devoid of any prior data illustrating its associations with different music clips.

Figure 1. (Color online) Choose Recommended Music for the Original Video on TikTok  
(a)  
![](/api/attachments/ECJCETUX/fulltext/images/63eb7b6a82e39a476db7ebc4e455d9d950775c0e45a7a1cc89b07ec6fb6eb0dc.jpg)  
(b)  
Notes. (a) Original video. (b) Choose background music.

To address these challenges for the background music recommendation task, we propose a model based on the deep learning framework. We design user–music and video–music matching modules in order to handle the unique challenges discussed. We also propose attentionbased aggregation for more accurate music feature extraction. Our deep learning–based model can be further extended to provide cold-start recommendations for new video creators and new music clips.

To evaluate our proposed model, we conduct comprehensive experiments on real-world data collected from one of the most popular short video sharing platforms, Douyin. Our model significantly outperforms other existing models in terms of hit rate (HR), normalized discounted cumulative gain (NDCG) and average likes (AL). The superiority of our model still holds when making cold-start recommendations for new video creators and new music clips. Our performance enhancements remain robust and reliable across diverse sub–data sets with varying density levels and across different video categories. Furthermore, our results remain resilient as hyperparameters are adjusted. Additionally, we conducted ablation studies to assess the impact of individual components within the model.

Our research makes several important contributions. First, we define a novel recommendation problem: how to recommend background music clips for short videos, taking users into consideration. Existing background music recommendation does not consider the alignment between users and music clips, and existing music rec ommendation for users on music sharing platforms does not have the video aspect. Unlike existing UGC rec ommendation, which focuses on suggesting UGC for users to consume, our problem centers on the creation of UGC by pairing music with original videos to produce the final content. Furthermore, the three-way relation ships among users, videos, and music in our context deviate from conventional three-way relationships. In conventional three-way relationships, as seen in context-aware recommendation, a single context can correspond to many users and many items. In contrast, a video in our setting only corresponds to a unique user and a unique music clip. Second, the novel deep learning–based model we designed to address the challenges posed by our unique recommendation problem offers significant methodological contribution. Given the distinctive nature of our three-way relationship, tra ditional models commonly employed in recommendation systems to depict standard three-way relationships prove ineffective when it comes to representing users, videos, and music within our context. Different from existing methods, our proposed model goes beyond traditional user–music alignment and also incorporates the video–music alignment. To effectively capture these alignments, we propose two matching modules with tai lored deep learning–based structures to match features from disparate feature spaces. In these two modules, we further develop attention-based aggregation for more accurate music feature extraction. Additionally, we obtained real data from one of the most popula short video sharing platforms, Douyin, to conduct our extensive experimental studies. The data set contains users, videos, and music clips as well as interaction information among these three players. The results of our experiments demonstrate that our proposed model significantly outperforms other state-of-the-art recommendation models.

## 2. Literature Review

Our research aims to provide background music recommendations for users to choose for their videos, so it is naturally related to research on background music recommendation and music recommendation on music streaming platforms. Meanwhile, our research is also related to UGC as we make music recommendations for user-generated videos.

## 2.1. Background Music Recommendations

In the literature, background music recommendation aims to match an appropriate music clip with a video track in order to make good-quality videos. Background music recommendation learns the matching between video and music features from professionally made commercial films or music videos. Liao et al (2009) propose a model to learn content-based association patterns between music and video clips in professional music videos, and the patterns are further used to help generate music videos by matching music and video clips. Kuo et al. (2013) implement a video production system based on YouTube videos with high musicality. The background music recommendation is made based on content correlation and temporal structure alignment of video and music, in which content correlation is measured based on the co-occurrence relationship between manually designed video and audio features, and temporal structure alignment is based on music beat and video shot alignment. Lin et al. (2014) learn a model from YouTube videos by introducing textual and content semantics to measure the matching degree of a video and a song, and the model is adopted to help common users make homemade videos. Lin et al. (2016) introduce emotion labels in background music recommendation. In their pro posed method, the emotional temporal phase sequence is constructed from video and audio content features, and the similarity between video and audio content is calculated based on the sequence feature. Lin and Shan (2017) integrate the temporal sequence of local features derived from segmented audiovisual clips into the correlation model, and they use commercia films from YouTube for learning the correlation model. Yi et al. (2021) propose a hierarchical Bayesian generative model that matches relevant background music to a microvideo by constraining their latent variables to generate each other, whereas their latent embeddings can be aligned via cross-generation. Pre´tet et al. (2021) adopt the features of music clips and videos based on other neural network models to learn from the co-occurrence patterns of music clips and videos and propose a model that can not only recommend music clips to videos, but also recommend videos to music clips.

The previous studies on background music recommendation make recommendations mainly based on the connection between music and videos without model ing users’ music choices from historical data. When a video sharing platform recommends background music for a user’s video, it should not neglect the user’s preferences for music, which can be learned from historical data capturing the relationships among users, videos, and music. Therefore, in our recommendation scenario involving the three key players, the recommended music clip should not only align with the video, but also match the user’s preferences. Another difference between our research and the previous background music recommendation literature lies in the process of obtaining the matching labels between music clips and videos. Previous literature usually adopts official music videos or commercial advertisements as the ground truth of matching labels to train the model (Liao et al. 2009, Kuo et al. 2013, Lin et al. 2016, Lin and Shan 2017), whereas we use the historical data about how users match videos with music clips. Therefore, learning user preferences in our model becomes even more important because the personalized recommendations should be considered high quality by the users themselves.

## 2.2. Music Recommendations

Because of the large number of music pieces available on music streaming platforms, music recommendation systems become an indispensable and integral part of music streaming platforms. Different from commonly recommended items, music clips are usually short, repeatedly consumed, and highly context-dependent (Hansen et al. 2020). Besides, music clips naturally contain abundant acoustic features, which may help improve recommendation quality. Thus, based on basic collaborative filter ing (Linden et al. 2003, Gomez-Uribe and Hunt 2015), music recommendation systems usually introduce content or context information to make recommendations in a hybrid way (Magron and Fe´votte 2021). For contextaware music recommendation, Hansen et al. (2020) observe that session-level contextual variables, such as the time in a day or the device type used, can help predict the next music clip to which the user wants to listen. Moreover, mobile device information can be conveniently accessed with rich sensing and wireless communication abilities from which daily activity status can be inferred. Wang et al. (2012) employ such daily activity status as running, walking, sleeping, working, studying, and shopping inferred with a probability model from sensing data to satisfy users’ contextual music preferences. Location is another key contextual factor that influences recommendation performances. Differen from the usual context-based scenario, location-aware music recommendation is made based on the matching of places of interest and music clips directly without considering user information (Braunhofer et al. 2013, Kaminskas et al. 2013). Wang et al. (2018) consider sequential information of users’ historical listening records based on contextual information for capturing both general and contextual preferences to better satisfy users’ real-time requirements.

Another stream of music recommendation research is based on music content. Cano et al. (2005) obtain descriptions about rhythm, instrumentation, and harmony from audio content features of music clips, and the similarities measured based on these features are used to make music recommendations. Magron and Fe´votte (2021) employ audio features extracted from low-level acoustic features in the recommendation framework and achieve better results compared with the models without content features as input. Different from using traditional audio content features directly, Wang and Wang (2014) propose to learn latent features of music clips through a deep learning model for music recommendation, which outperforms the traditional feature-based model as the extracted deep music features bridge the semantic gap between low-level audio features and high-level concepts of music. Besides audio features, other side information also helps improve recommendation performances. Liang et al. (2015) utilize semantic tagging information as a prior for a collaborative filtering model and obtain better results than the pure collaborative filtering model.

Our problem setting is distinct from the previous music recommendation literature. In our setting, we formulate a three-way relationship: user–video–music, providing music recommendations for user-generated videos. In contrast, existing literature for music recommendation on online music streaming platforms only formulate the relationship between user and music, providing music recommendations to meet user’s preferences. We note that the context-aware recommendation problem is also related to a three-way relationship setting: user–context–item. However, the three-way relationship among user, video, and music in our setting is not the same as that among user, context, and item in the context-aware recommendation problem. A context corresponds to many users and many items. In contrast, a video in our setting only corresponds to a unique user and a unique music clip. This problem is not well studied in the literature, which motivated our research in this paper.

## 2.3. Recommendation Systems Related to User-Generated Content

UGC platforms allow users to produce and consume content, which has become the core part of many web applications. Researchers use UGC to help generate better recommendations. For example, Galli et al. (2015) use viewers’ comments to improve YouTube video recommendation and Shen et al. (2020) recommend experts with the help of user-generated tags. UGC has also served as the items to be recommended. For example, Yang et al. (2020) study the problem of recommending user-generated lists, such as music playlists, reading lists, and movie watching lists to users and propose a method leveraging both item- and list-level information.

The recommendation problem studied in our paper is quite different from the problems studied in existing recommendation literature related to UGC. Whereas existing literature either uses item’s UGC information to improve item recommendation performance or recommends UGC itself, our study aims to use recommendation to generate UGC, which is a totally different recommendation task. From the methodology point of view, our study is also different from existing UGCrelated research. Some studies on UGC recommendation also take UGC producers into consideration (He et al. 2016, Kang and McAuley 2018, Tsukuda et al. 2019). Therefore, they also consider a three-way relationship, producer–consumer–UGC. However, this three-way relationship is very different from our user–video–music three-way relationship. In UGC recommendation, the recommended item, namely, UGC, may be consumed by many consumers; in the meantime, consumers may consume many UGC items, and a producer may generate many items. On the contrary, in our context, each video is exclusively linked to an individual user and a specific music clip. How to address the three-way relationships among users, videos, and music clips effectively in such a recommendation setting has not been well addressed in the literature.

## 3. Problem Definition

In this section, we formally define the problem of recommending background music for new videos that users are uploading, leveraging a comprehensive amalgamation of historical user–video–music interactions, music/video content, and user-specific information.

On most short video sharing platforms, a user who wants to upload a video can choose a music clip for the video. Let $\mathcal { U } = \{ u _ { i } \} , i = 1 , 2 , \dotsc , I$ be a set of users; $\nu =$ $\{ v _ { j } \} , j = 1 , 2 , \ldots , J$ be a set of videos; and $\mathcal { M } = \{ m _ { k } \} , k =$ $1 , 2 , \ldots , K$ be a set of music clips. We denote the decision of a user selecting a music clip for a video as $\mathcal { C } = \{ c _ { i , j , k } \} _ { \mathrm { { } } }$ $i = 1 , 2 , \ldots , I ; j = \bar { 1 , } 2 , \ldots , J ; k = \bar { 1 } , 2 , \ldots , K ,$ , where $c _ { i , j , k } = 1$ means user u chooses music clip $m _ { k }$ for video v and zero otherwise. Besides the user–video–music interaction information captured in ${ \mathcal { C } } ,$ we also leverage features extracted from videos and music clips as well as user features. User features include user identity information alongside other attributes such as demographic data if available. We use $\mathbf { x } _ { i } ^ { u }$ to denote the features for user $u _ { i } .$ Video features are usually extracted from video content and short texts posted along with videos. We use $\mathbf { x } _ { j } ^ { v }$ to denote the features for video $v _ { j } .$ For music clips, typical features include mel frequency cepstral coefficients (MFCCs), tempo, lyrics, genre, and popularity. We use $\mathbf { x } _ { k } ^ { m }$ to denote these features for music $m _ { k } .$

Following the notations and descriptions given, our recommendation problem is to predict the probability that a music clip $m _ { k }$ is chosen for a video $v _ { j }$ uploaded by a certain user $u _ { i } , P ( c _ { i , j , k } = 1 | u _ { i } , v _ { j } , m _ { k } ) .$ , and recommend music clips with the highest probabilities. To address this problem, we propose a novel model for background music recommendation based on deep learning techniques that demonstrate effectiveness for improving recommender systems (Zhang et al. 2019).

## 4. A Deep Learning Model for BGM Recommendation

In this section, we develop a new deep learning–based model to address the recommendation problem presented in Section 3. We name this model the deep learning for background music (DL-BGM) recommendation. This model focuses on analyzing the alignment of music clips with both users and videos by leveraging interaction and content information among users, videos, and music clips. We then provide a time complexity analysis for recommendation generation and introduce a comprehensive process to handle cold-start issues.

## 4.1. Overview of DL-BGM

The background music recommendation problem we study differs from traditional recommendation problems because it considers not only users and music clips (items), but also videos. A related problem is context-aware recommendation, in which a context corresponds to many users and many items. In contrast, a video in our setting only corresponds to a unique user and a unique music clip. Because of this difference, classic tensor factorization models often used in recommendation systems to model relationships among users, items, and contexts (Nanopoulos et al. 2009, Bi et al. 2018) become ineffective for modeling relationships among users, videos, and music clips (please see Online Appendix A for the proof).

To tackle the challenging task of providing music recommendations that are tailored not just to the user, but also to the specific video the user is posting, we design a novel approach. This approach goes beyond traditional user–music alignment and also incorporates the video–music alignment. To achieve this, we design two distinct matching modules dedicated to capturing the synergy between music and users as well as music and videos. These modules are referred to as the user–music and the video–music matching modules, respectively. This design approach is tailored to address our three-way relationship that departs from the conventional structure. In our recommendation scenario involving the three key players, the recommended music clip should not only align with the video, but also match the user’s preferences. At the same time, it is important to note that the user–video pairing remains fixed. As a result, we employ two separate two-way modules, namely, the user–music and video–music modules, without explicitly modeling the user–video relationship.

The framework of the proposed deep learning–based model DL-BGM is illustrated in Figure 2. As shown in Figure 2, the left half is the user–music matching module ,and the right half is the video–music matching module. In the user–music matching module, we leverage users historically utilized music clips and music clips’ related users to match users and music clips from both user and music feature space. In the video–music matching module, we utilize similar videos’ adopted music clips and music clips’ related videos to connect videos and music on both video and music feature space. Further elaboration on these two matching modules can be found in Sections 4.2 and 4.3. Given the shared utilization of the music feature space in both modules, we further introduce a cross-module feature aggregation component to enhance the feature extraction for music clips and improve the quality of matching in the music feature space. This aggregation component is designed based on the attention mechanism, and we explain it in detai in Section 4.4.

## 4.2. User–Music Matching Module

To capture the alignment between users and music clips, we design a user–music matching module (the left half of the framework in Figure 2) based on interaction informa tion between users and music, music content, and user features. Given that user and music features inherently belong to disparate feature spaces and convey distinct aspects of users and music, direct matching between them is not feasible. To overcome this challenge, we consider features of a user’s historically utilized music clips and features of a music clip’s associated users, augmenting the original user and music content features. Consequently, we facilitate dual-mode matching, covering both the user and the music feature spaces. In the user feature space, we conduct comparisons between the user’s features and features of the music clip’s affiliated users. Meanwhile, in the music feature space, we undertake sim ilar comparisons between the features of the music clip and the features of the user’s historically employed music clips. This approach ensures a multifaceted matching process that accommodates the intricacies of both user and music feature spaces.

To evaluate how well a user $u _ { i }$ matches with a music clip $m _ { k }$ in the user feature space, we compare the user’s features with the average features of all the users who have adopted this music clip before. Specifically, to capture user features helpful for our background music recommendation task, we first adopt a feature transformation layer to transform the user’s features from $\mathbf { x } _ { i } ^ { u }$ to $\mathbf { x } _ { i } ^ { u ^ { \prime } }$ :

Figure 2. Framework of DL-BGM  
![](/api/attachments/ECJCETUX/fulltext/images/a75620d048ca73a5c17cc18cbf1045133096a91a8a3a3354dee05817e5aa8eb4.jpg)

$$
\mathbf {x} _ {i} ^ {u ^ {\prime}} = \tanh (\mathbf {W} _ {u} \mathbf {x} _ {i} ^ {u} + b _ {u}),\tag{1}
$$

where $\mathbf { W } _ { u }$ is the weight matrix, $b _ { u }$ is the bias of the linear transformation, and tanh(·) acts as the activation function.

With the same transformation layer, we transform features of each user $u _ { i _ { k } }$ who has previously adopted $m _ { k }$ from $\mathbf { x } _ { i _ { k } } ^ { u }$ to $\mathbf { x } _ { i _ { k } } ^ { u ^ { \prime } }$ . We then calculate the average transformed features of the users who have adopted $m _ { k }$ as

$$
\overline {{\mathbf {x}}} _ {k} ^ {u ^ {\prime}} = \frac {1}{| \mathcal {U} _ {k} |} \sum_ {u _ {i _ {k}} \in \mathcal {U} _ {k}} \mathbf {x} _ {i _ {k}} ^ {u ^ {\prime}},\tag{2}
$$

where $\mathcal { U } _ { k }$ is the set of users who have adopted $m _ { k }$ before.

In the user feature space, we define the matching vector between user $u _ { i }$ and music clip $m _ { k }$ as

$$
\mathbf {h} _ {i, k} ^ {u ^ {\prime}} = \mathbf {x} _ {i} ^ {u ^ {\prime}} \otimes \overline {{\mathbf {x}}} _ {k} ^ {u ^ {\prime}},\tag{3}
$$

where $\otimes$ is a general matching operator supporting element-wise addition, element-wise product, and concatenation.

Likewise, to measure the matching degree between a user $u _ { i }$ and a music clip $m _ { k }$ in the music feature space, we compare the music clip’s features with the average features of music clips that the user has adopted before. User $u _ { i } ^ { \prime } \mathrm { s }$ music set, which contains all the music clips that $u _ { i }$ has chosen for uploaded videos in the past, is denoted by $\mathcal { M } _ { i } = \{ m _ { k _ { i } } \}$ . We introduce an average pooling layer over $\mathcal { M } _ { i }$ to aggregate features of music clips used in user $u _ { i } ^ { \prime } \mathbf { s }$ past videos and obtain the following

feature vector:

$$
\overline {{\mathbf {x}}} _ {i} ^ {m} = \frac {1}{| \mathcal {M} _ {i} |} \sum_ {m _ {k _ {i}} \in \mathcal {M} _ {i}} \mathbf {x} _ {k _ {i}} ^ {m}.\tag{4}
$$

We can then directly use the aggregated user-related music features from the pooling layer and define the matching vector between user $u _ { i }$ and music clip $m _ { k }$ in the music feature space as

$$
\mathbf {h} _ {i, k} ^ {m} = \overline {{\mathbf {x}}} _ {i} ^ {m} \otimes \mathbf {x} _ {k} ^ {m}.\tag{5}
$$

In order to further improve music feature aggregation, we introduce an aggregation layer based on the attention mechanism and feed the new aggregated results into Equation (5). We provide a detailed explanation on how attention-based aggregation works in Section 4.4.

Finally, we combine the matching results from both the user and music feature spaces through concatenation and obtain the user-music matching vector as

$$
\mathbf {h} _ {i, k} ^ {u 2 m} = \operatorname{concat} (\mathbf {h} _ {i, k} ^ {u ^ {\prime}}, \mathbf {h} _ {i, k} ^ {m}).\tag{6}
$$

## 4.3. Video–Music Matching Module

In addition to recommending music clips aligned with users, we also aim to capture the synergy between videos and music clips to provide a more holistic recommendation solution. We propose a video–music matching module (the right half of the framework in Figure 2) based on interaction information between videos and music, music content, and video content. We also leverage dual-mode matching to handle video and music features from different feature spaces. The video–music matching model is slightly different from the user–music matching model because we are recommending music to a new and unique video that has no historical interaction with any music clip. To address this issue, we leverage a video’s similar videos as well as a music clip’s related videos in our matching process.

In the video feature space, we compare features of the original video with features of a music clip’s related videos. In order to capture useful video features for our background music recommendation task, we adopt a feature transformation layer and transform the video’s features x<sup>v</sup> to $\mathbf { x } _ { j } ^ { v ^ { \prime } }$ :

$$
\mathbf {x} _ {j} ^ {v ^ {\prime}} = \tanh (\mathbf {W} _ {v} \mathbf {x} _ {j} ^ {v} + b _ {v}).\tag{7}
$$

The features of each video that has used music clip $m _ { k }$ before are also transformed from $\mathbf { x } _ { j _ { k } } ^ { v }$ to $\mathbf { x } _ { j _ { k } } ^ { v ^ { \prime } }$ . We then calculate the average transformed features of videos related to $m _ { k }$ and obtain

$$
\overline {{\mathbf {x}}} _ {k} ^ {v ^ {\prime}} = \frac {1}{| \mathcal {V} _ {k} |} \sum_ {v _ {j _ {k}} \in \mathcal {V} _ {k}} \mathbf {x} _ {j _ {k}} ^ {v ^ {\prime}},\tag{8}
$$

where $\nu _ { k }$ is the set of videos that have adopted $m _ { k }$ before.

The matching vector between video $v _ { j }$ and music clip $m _ { k }$ in the video feature space is defined as

$$
\mathbf {h} _ {j, k} ^ {v ^ {\prime}} = \mathbf {x} _ {j} ^ {v ^ {\prime}} \otimes \overline {{\mathbf {x}}} _ {k} ^ {v ^ {\prime}}.\tag{9}
$$

Things are a little different when evaluating how well a video $v _ { j }$ matches with a music clip $m _ { k }$ in the music feature space. This is because the video to be recommended music clips has no past music adoption information. To get this video’s related music clips, we locate the top $l _ { v }$ most similar videos to video $v _ { j \cdot }$ We further discuss how similarity calculation is implemented in Section 5.4. The video’s related music clips, which are the music clips used in these most similar videos, are denoted by $\mathcal { M } _ { j } = \{ m _ { k _ { j } } \}$ . With an average pooling layer, we can obtain the aggregated features of video $v _ { j } ^ { \prime } \mathbf { s }$ related music clips as

$$
\overline {{\mathbf {x}}} _ {j} ^ {m} = \frac {1}{| \mathcal {M} _ {j} |} \sum_ {m _ {k _ {j}} \in \mathcal {M} _ {j}} \mathbf {x} _ {k _ {j}} ^ {m}.\tag{10}
$$

We can then directly compare the aggregated videorelated music features $\overline { { \mathbf { x } } } _ { j } ^ { m }$ from the pooling layer with the features of the original music clip $\mathbf { x } _ { k } ^ { m } .$ , and define the matching vector between video $v _ { j }$ and music clip $m _ { k }$ in the music feature space as

$$
\mathbf {h} _ {j, k} ^ {m} = \overline {{\mathbf {x}}} _ {j} ^ {m} \otimes \mathbf {x} _ {k} ^ {m}.\tag{11}
$$

To further enhance music feature aggregation, we also introduce an attention-based aggregation layer as in the user–music module. We provide a detailed explanation on how attention-based aggregation works in Section 4.4.

Finally, we combine the matching results from both the video and music feature spaces through concatenation and obtain the video–music matching vector as

$$
\mathbf {h} _ {j, k} ^ {v 2 m} = \operatorname{concat} (\mathbf {h} _ {j, k} ^ {v ^ {\prime}}, \mathbf {h} _ {j, k} ^ {m}).\tag{12}
$$

## 4.4. Attention-Based Aggregation for Music Feature Extraction

To predict which music clip user $u _ { i }$ will choose for video $v _ { j } ,$ our designed structure can borrow information from the features of the music clips that $u _ { i }$ has used before (M ) and the features of the music clips used in similar hit videos $( \mathcal { M } _ { j } )$ . The pooling layers designed in the user–music and video–music matching modules of the proposed model aim to extract the music features of these music clips. However, the average pooling operation used in Equation (4) weighs different music clips in $\mathcal { M } _ { i }$ equally, which cannot capture the fact that some music clips are for videos similar to video $v _ { j }$ and others are for very different videos. Likewise, the average pooling operation used in Equation (10) weighs different music clips in $\mathcal { M } _ { j }$ equally, which is not ideal because a user $u _ { i }$ may have different preferences on different music clips in $\mathcal { M } _ { j }$ . Considering these, we design aggregation layers based on the attention mechanism to assign different weights to different music clips for more accurate music feature extraction as illustrated in the middle two branches of the framework in Figure 2.

Specifically, in order to measure the matching degree of a music clip $m _ { k _ { i } }$ $( \forall m _ { k _ { i } } \in \mathcal { M } _ { i } )$ with video $v _ { j \prime }$ we use attention $\alpha _ { k _ { i } , j }$ to represent the similarity between $m _ { k _ { i } } ^ { \prime } \mathbf { s }$ music feature $\mathbf { x } _ { k _ { i } } ^ { m }$ and the music feature of video $v _ { j } ^ { \prime } \mathbf { s }$ related music clips $\overline { { \mathbf { x } } } _ { j } ^ { m }$ coming from the video–music matching module. This means that the aggregation layer with attention in the user–music matching module uses the output of the pooling layer from the video–music matching module as its input. The higher the attention, the more weights the music clip gets. The revised feature vector $\tilde { \mathbf { x } } _ { i } ^ { m }$ and the attention $\alpha _ { k _ { i } , j }$ are calculated as follows:

$$
\tilde {\mathbf {x}} _ {i} ^ {m} = \sum_ {m _ {k _ {i}} \in \mathcal {M} _ {i}} \alpha_ {k _ {i}, j} \mathbf {x} _ {k _ {i}} ^ {m}, \text {   where   } \alpha_ {k _ {i}, j} = \text { attention } (\mathbf {x} _ {k _ {i}} ^ {m}, \overline {{\mathbf {x}}} _ {j} ^ {m}).\tag{13}
$$

The vector $\tilde { \mathbf { x } } _ { i } ^ { m }$ then replaces $\overline { { \mathbf { x } } } _ { i } ^ { m }$ in Equation (5). Note that various methods for computing attention scores can be employed. The pooling and aggregation layers to extract the music features for the user’s adopted music clips are illustrated in Figure 3.

Also, the attention mechanism is used to assign differ ent weights to different music clips in $\mathcal { M } _ { j }$ according to the user’s music preferences, which come from the user–music matching module. This means that the aggregation layer with attention in the video–music matching module uses the output of the pooling layer from the user–music matching module as its input. As $\overline { { \mathbf { x } } } _ { i } ^ { m }$ captures the music features of user $u _ { i } ^ { \prime } \mathbf { s }$ adopted music clips, we use it to generate the attention weights and calculate the revised feature vector $\tilde { \mathbf { x } } _ { j } ^ { m }$ as follows:

Figure 3. The Pooling and Aggregation Layers to the Music Features for the User’s Adopted Music Clips  
![](/api/attachments/ECJCETUX/fulltext/images/8f731a306884f22e79116ae9028ade99f1c487a3c9544f4e2502cfb062b4ab17.jpg)

$\tilde { \mathbf { x } } _ { j } ^ { m } = \sum _ { m _ { k _ { j } } \in \mathcal { M } _ { j } } \beta _ { k _ { j } , i } \mathbf { x } _ { k _ { j } } ^ { m } ,$ , where $\beta _ { k _ { j } , i } = \mathrm { a t t e n t i o n } ( \mathbf { x } _ { k _ { j } } ^ { m } , \mathbf { \overline { { x } } } _ { i } ^ { m } )$

(14)

$\tilde { \mathbf { x } } _ { j } ^ { m }$ then replaces $\overline { { \mathbf { x } } } _ { j } ^ { m }$ in Equation (11). The pooling and aggregation layers to extract music features for the video’s related music clips are illustrated in Figure 4.

## 4.5. Recommendation Generation

After obtaining the user–music matching vector $\mathbf { h } _ { i , k } ^ { u 2 m }$ and video–music vector $\mathbf { h } _ { j , k } ^ { v 2 m }$ , we concatenate these two vectors and use them as input to the prediction layer to generate the probabilities describing how likely each music clip $m _ { k }$ is to be chosen by user $u _ { i }$ for video v<sub>j</sub>:

$$
\begin{array}{c} P _ {c _ {i, j, k}} = \text {softmax} (\mathbf {W} _ {u 2 m} \mathbf {h} _ {i, k} ^ {u 2 m} + \mathbf {W} _ {v 2 m} \mathbf {h} _ {j, k} ^ {v 2 m} + b) \\ = \frac {\exp (\mathbf {W} _ {u 2 m} \mathbf {h} _ {i , k} ^ {u 2 m} + \mathbf {W} _ {v 2 m} \mathbf {h} _ {j , k} ^ {v 2 m} + b)}{\sum_ {l = 1} ^ {K} \exp (\mathbf {W} _ {u 2 m} \mathbf {h} _ {i , l} ^ {u 2 m} + \mathbf {W} _ {v 2 m} \mathbf {h} _ {j , l} ^ {v 2 m} + b)}. \end{array}\tag{15}
$$

We then adopt cross-entropy loss to train the model:

$$
L (\mathcal {C}, \mathbf {P} _ {D}) = - \sum_ {(i, j) \in \mathcal {C} ^ {v}} \sum_ {k = 1} ^ {K} c _ {i, j, k} \log P _ {c _ {i, j, k}},\tag{16}
$$

where $\mathbf { P } _ { D } = \{ P _ { c _ { i , j , k } } | ( i , j ) \in \mathcal { C } ^ { v }$ and $k = 1 , 2 , \ldots , K \}$ and ${ \mathcal { C } } ^ { v } =$ $\{ ( i , j ) |$ |user u<sub>i</sub> uploaded video v<sub>j</sub>}.

Figure 4. The Pooling and Aggregation Layers to Extract Music Features for the Video’s Related Music Clips  
![](/api/attachments/ECJCETUX/fulltext/images/78a7abb1e686c6204586e0c3aadea8c37864fd2de5fb38cb9286ae437555eb52.jpg)

When using this model to generate recommendation, we pick the top N music clips based on Equation (15). We further analyze the time complexity of this model. For a new video created by an existing user, obtaining transformed video features takes $O ( f _ { v } d _ { v } )$ , where $f _ { v }$ is the number of video features and $d _ { v }$ is the size of the transformed video feature vector. And locating top similar videos of this new video takes $O ( f _ { v } J )$ , where J is the number of videos. This term can be greatly sped up to $O ( f _ { v } \log { J } )$ by approximate nearest neighbor search techniques (Liu et al. 2004, Li et al. 2019) in which exist algorithms with sublinear time complexity. The attentionbased pooling and aggregation takes $O ( \bar { f } _ { m } S )$ , where $f _ { m }$ is the number of music features and S denotes the maximum of the number of historical adopted music clips and the number of similar videos. Then, computing matching vectors in different feature spaces and calculating final matching probabilities takes $\bar { O } ( ( d _ { u } + d _ { v } + f _ { m } ) K )$ , where $d _ { u }$ is the size of the transformed user feature vector and K is the number of music clips. Taking these terms together, the time complexity is $O ( f _ { v } d _ { v } + \bar { f } _ { v }$ log $J + f _ { m } { \boldsymbol { S } } + \bigl ( \bar { d } _ { u } + d _ { v } $ $+ f _ { m } ) K )$ . Because $d _ { u } , d _ { v } , f _ { m } , f _ { v } ,$ and S are commonly in the hundreds and K and J are in the range from thousands to millions, the time complexity can be reduced to $O ( f _ { v }$ log J $+ f _ { m } K )$ . In other words, DL-BGM has a linear time complexity with respect to the number of music clips K. And calculating final matching probabilities for all music clips can be further accelerated by parallel computing.

## 4.6. Cold-Start Recommendations

Our proposed model can be further extended to handle cold-start recommendations for new users with no previous history of video creation and new music clips with no history of being adopted. In the literature on recommender systems, the cold-start problem is commonly addressed by incorporating the content information of users or items. Schein et al. (2002) compute similarities between recently introduced items and those that have been rated based on their content information and recommend new items that exhibit similarity to rated items. Volkovs et al. (2017) propose a deep neural network based on denoising autoencoders to infer the preferences of new users and items by utilizing their content information. Inspired by previous studies, we design solutions to address the cold-start problem in our study for both new users and new music clips.

For a new user, the set of music clips adopted before $( \mathcal { M } _ { i } )$ is empty. We can construct a set of music clips adopted by neighboring users as a proxy for $\mathcal { M } _ { i }$ and use it in Equation (4). The neighboring users can be obtained by calculating similarity scores based on user features, such as demographic information, and video features together. Specifically, the similarity based on video features is calculated between the user’s first video and the average video from every existing creator. An alternative approach to obtaining a set of music clips for a new user is to proactively gather this information before the user transitions into a video creator, perhaps during the registration process or through a strategically placed survey when the user is engaged with video content on the platform. In this scenario, the platform could present the user with a curated selection of sample music clips and inquire about the user’s preferences. The selection of this sample set can be determined through the appli cation of active learning techniques (Rubens et al. 2015).

For a new music clip, the set of users that have adopted the music clip before $( \boldsymbol { \mathcal { U } } _ { k } )$ and the set of videos that have used the music clip before $( \nu _ { k } )$ are both empty. We can instead use a set of users that have adopted its neighboring music clips and a set of videos that have used its neighboring music clips as proxies. A new music clip’s neighboring music clips are obtained by computing the similarities with existing music clips based on music features.

## 5. Experiments

In this section, we first describe the data, and then we compare the performances of our model with the baseline models. Further analyses include ablation studies, comparisons for cold-start recommendations, and generalizability and robustness analysis.

## 5.1. Data Description

We collected data from a popular user-generated short video sharing platform, Douyin. First, we randomly chose about 4,000 music clips on the platform. For each music clip, we crawled about 1,600 most liked videos that adopted the music clip. The videos were generated before November 2018, and the number of likes was observed in May 2019 when the number became stable. In total, we obtained 6,746,286 videos created by 4,960,170 users. On average, each user has 1.36 videos in this data set, which is very sparse. Following the strategy used for MovieLens (Harper and Konstan 2015), we sample a subset with higher density. During sampling, we maintain the number of videos for each music clip and the number of videos for each user no smaller than 10. This data selection is also done for computational purposes, but we also conducted further experiments by sampling less dense data in Sections 5.7 and 5.8. In the selected sub–data set, the average number of videos per user increases to 19.56. The detailed statistics of the raw and final data sets are listed in Table 1. Figure 5 shows the distribution of the number of music clips chosen by a user and the number of users choosing a music clip in the final data set.

## 5.2. Extracted Features

We adopt user, music, and video features as input in our proposed model. Because of privacy restrictions, there are no user demographics in the collected data set. For now, we use a one-hot vector to represent user identification information. If other user features $( \mathrm { e . g . , }$ demographic features) become available, we can easily add them to the input. For music clips and videos, there are some commonly used methods to extract features. Whereas, in this paper, we choose some typical music and video features to feed into our model, we can easily add different feature vectors to the input.

Table 1. The Statistics of the Data Sets

<table><tr><td></td><td>#videos</td><td>#music</td><td>#users</td><td>#videos for each music</td><td>#videos for each user</td></tr><tr><td>Raw data set</td><td>6,746,286</td><td>4,049</td><td>4,960,170</td><td>1,666.20</td><td>1.36</td></tr><tr><td>Final data set</td><td>323,843</td><td>1,717</td><td>16,559</td><td>188.61</td><td>19.56</td></tr></table>

5.2.1. Music Features. The music features we used in the models are MFCCs (Zheng et al. 2001), tempo (Grosche et al. 2010), lyrics features, genre features (Sturm 2013), and popularity. We extract MFCCs and tempo through the librosa library (McFee et al. 2015), infer lyrics features with a sentence-transformers model (Reimers and Gurevych 2019), obtain genre features through a pretrained long short-term memory (LSTM) model (Hochreiter and Schmidhuber 1997), and calculate the music clip’s popularity among video creators and viewers.

MFCCs are proven to be effective features in music information retrieval (Brent 2009). MFCCs consist of coefficients that represent a sound’s short-term power spectrum. We extract 20 MFCC coefficients from every music frame in a music clip and use the average value over all frames as the features of the music clip.

Tempo refers to the rate of the music’s beat, which is often defined as beats per minute. Tempo affects the lyricism of music and reflects the intensity of emotions in music clips. As with MFCCs features, we use the average value over all frames as the tempo features of each music clip.

Lyrics features are also important music features, which perform well in genre (Mayer et al. 2008) and mood (Kumar and Minz 2013) classification. Because the music clips in our data set are multilingual, we utilize a sentence-transformers model, which is pretrained based on multilingual corpora containing 50+ languages (Reimers and Gurevych 2020), to map the lyrics of the music to a 512-dimensional dense vector space. Specifically, we first derive hidden representations of the music’s name and each sentence of the music’s lyrics and then use the average representation as the music’s lyrics features. For those music clips without lyrics, we use the representation of the music’s name as a proxy.

Unlike MFCCs, tempo and lyrics features, genre features are high-level features for music clips (Logan 2004, Nalini and Palanivel 2016, Nagawade and Ratnaparkhe 2017). We build a genre classification model based on LSTM using GTZAN (Sturm 2013) which is a music file data set with genre labels. GTZAN contains 1,000 different music clips, which are classified into 10 different gen res. The duration of each music clip in the data set is about 30 seconds, which is similar to the length of short videos in our data set. Among the 10 genres, two of them rarely appear in our data. For simplicity, we drop the two genres and use only the remaining eight genres, which are classical, country, disco, hip-hop, jazz, metal, pop, and reggae. The top-1 accuracy in the validation set is 75.38%, which shows that this classifier performs reasonably well to be used to generate our genre features. In our experiments, we have eight genre features, each of which corresponds to the probability of that genre.

Figure 5. Data Distributions in the Final Data Set  
(a)  
![](/api/attachments/ECJCETUX/fulltext/images/486580f80170b7f45abb57c40786f0fa7e42c99636c8a8515d489225c5c244e4.jpg)

(b)  
![](/api/attachments/ECJCETUX/fulltext/images/a2bd43de47252b7953bc41aa5857122a514d7d29d6eed1ac5700b72e0263654a.jpg)  
Notes. (a) Histogram of number of music clips chosen by a user (with y-axis in log scale). (b) Histogram of number of users choosing a music clip.

Table 2. The Dimensions of Music Features and Video Features

<table><tr><td></td><td>Features</td><td>Dimensions</td></tr><tr><td rowspan="5">Music features</td><td>MFCCs</td><td>20</td></tr><tr><td>Tempo</td><td>384</td></tr><tr><td>Lyrics</td><td>512</td></tr><tr><td>Genre</td><td>8</td></tr><tr><td>Popularity</td><td>2</td></tr><tr><td rowspan="2">Video features</td><td>CNN features</td><td>1,024</td></tr><tr><td>Text embeddings</td><td>768</td></tr></table>

In addition to these content features, we also include two features reflecting the music clip’s popularity: the number of times the music clip is adopted by video creators and the number of times liked by viewers. Our method can easily incorporate more music features if they become available (e.g., music emotion) (Go´mez-Can˜ o´n et al. 2021).

5.2.2. Video Features. In recent years, convolutional neural network (CNN) has become an effective way to extract features from images and videos (Simonyan and Zisserman 2014, Krizhevsky et al. 2017). CNN has its advantages in automatically generating useful features with high classification accuracy. To obtain video features, we follow the method proposed by Abu-El-Haija et al. (2016). We first extract one frame per second from each video, and then we use a CNN model pretrained on ImageNet (Simonyan and Zisserman 2014) to derive the hidden representation immediately before the classification layer. The video features we finally input into the models are the average features of the video’s extracted frames. In addition, we extract the textual features from short texts posted along with the videos. Because most of the texts in our data set are in Chinese, we adopted a bidirectional encoder representations from transformers model (Devlin et al. 2018), which is pretrained for Chinese (HuggingFace 2020), to map the short texts to a 768-dimensional dense vector space. Note that our models can be easily adapted to any kind or any combination of video features without modification. Table 2 shows the dimensions of each kind of feature.

## 5.3. Baseline Models

We compare our proposed DL-BGM model with baseline models that can be used for background music recommendation. Table 3 lists these baseline models, including Top Popular, K-Nearest Neighbors (KNN), matrix factorization (MF) (Johnson 2014), and NeuMF (He et al. 2017) only based on user–music interaction information and a latent factor model (LFM) (Liu and Chen 2018) and pseudo-song-based deep similarity matching (PDSM) (Lin et al. 2017) only based on videomusic matching information. We also designed several baseline models (FM-BGM, TF-BGM, and MF-BGM) specifically for our data context considering user, music, and video factors. FM-BGM is based on a factorization machine (Rendle 2010). Whereas classical tensor factorization models (Tucker 1966) are not well suited for our specific context, we designed TF-BGM, which improves the learning of video-related lower dimensional tensors. MF-BGM captures user–music and video–music matching under the matrix factorization framework. Details of how to implement TF-BGM and MF-BGM are provided in Online Appendix B.

Table 3. Summary of Baseline Models

<table><tr><td>Name</td><td>Description</td></tr><tr><td>Top Popular</td><td>Recommend all videos with the most frequent music clips.</td></tr><tr><td>KNN</td><td>Recommend the most similar videos&#x27; background music to the target video.</td></tr><tr><td>MF</td><td>The basic matrix factorization method. Recommend music clips to the user regardless of the video.</td></tr><tr><td>NeuMF(logit)</td><td>Neural matrix factorization with logit loss function. Recommend music clips to the user regardless of the video.</td></tr><tr><td>NeuMF(BPR)</td><td>Neural matrix factorization with Bayesian personalized ranking loss function. Recommend music clips to the user regardless of the video.</td></tr><tr><td>LFM</td><td>Latent factor model for background music recommendation. Recommend music clips to the video regardless of the user.</td></tr><tr><td>PDSM</td><td>Pseudo-song-based deep similarity matching method. Recommend music clips to the video regardless of the user.</td></tr><tr><td>MF+LFM</td><td>First recommend music clips to the user using MF, and then recommend music clips to the video within the previous recommendation results using LFM.</td></tr><tr><td>MF+PDSM</td><td>First recommend music clips to the user using MF, and then recommend music clips to the video within the previous recommendation results using PDSM.</td></tr><tr><td>NeuMF(logit)+LFM</td><td>First recommend music clips to the user using NeuMF(logit), and then recommend music clips to the video within the previous recommendation results using LFM.</td></tr><tr><td>NeuMF(logit)+PDSM</td><td>First recommend music clips to the user using NeuMF(logit), and then recommend music clips to the video within the previous recommendation results using PDSM.</td></tr><tr><td>NeuMF(BPR)+LFM</td><td>First recommend music clips to the user using NeuMF(BPR), and then recommend music clips to the video within the previous recommendation results using LFM.</td></tr><tr><td>NeuMF(BPR)+PDSM</td><td>First recommend music clips to the user using NeuMF(BPR), and then recommend music clips to the video within the previous recommendation results using PDSM.</td></tr><tr><td>FM-BGM</td><td>Factorizing-machine-based method tailored for our BGM problem.</td></tr><tr><td>TF-BGM</td><td>Tensor-factorization-based method tailored for our BGM problem.</td></tr><tr><td>MF-BGM</td><td>Matrix-factorization-based method tailored for our BGM problem.</td></tr><tr><td>DL-BGM</td><td>Our proposed deep-learning-based method for recommending music clips to a video created by a user.</td></tr></table>

In the industry, two-step strategies based on personalized recall and video content similarity are often used for background music recommendations on short video sharing platforms. We further design several two-step models as baselines. Specifically, we first recall a candidate music recommendation list based on personalized user preferences using MF, NeuMF(logit), or NeuMF(- Bayesian personalized ranking (BPR)). Subsequently, we generate the final recommendation within the candidate recommendation list based on the alignment between the video and the candidate music clip using either LFM or PSDM. The combination leads to six baselines: MF+LFM, MF+PDSM, NeuMF(logit)+LFM, NeuMF(logit)+PDSM, NeuMF(BPR)+LFM, and NeuMF(BPR)+PDSM.

## 5.4. Experimental Settings

The data set is partitioned into three subsets chronologically with two thirds for training, one sixth for validation, and one sixth for testing. We select the hyperparameters based on the validation set and evaluate the models’ performances on the test set.

As our model and baseline models provide a recommendation list for a user–video pair, we conduct comprehensive evaluation for top-N recommendation tasks. To examine whether the recommended music clip is aligned with the video creator’s preference, we adopt the commonly used top-N recommendation metrics: HR and NDCG. We calculate HR by examining whether the ground truth appeared in top-N recommendation lists. And NDCG considers the rank of the ground truth in the top-N lists. Moreover, to evaluate whether the recommended music clip is suitable for the video and, thus, liked by viewers, we introduce a metric named AL, which is the average number of likes received by videos with recommended music clips. For HR, NDCG, and AL, higher scores mean better performance. In the following, we use HR@N, NDCG@N, and AL@N to represent the average results in top-N recommendation lists.

When locating similar videos in our proposed model, we adopt Euclidean distance based on video features to calculate the similarity between two videos. For the calculation of the matching vectors, we use element-wise addition as the matching operator. For the calculation of the attention weights, we adopt the method proposed by Wang et al. (2017), in which attention weights are obtained through the direct inner product without being normalized by softmax function.

## 5.5. Comparison with Baseline Models

We conduct comprehensive comparisons between our proposed model and the baseline models. Table 4 reports HR@N and NDCG@N results (N � 1, 5, and 10) for all the models and the percentage of improvement DL-BGM has over each model, respectively. We can see that DL-BGM shows significant superiority over all baselines based on HR and NDCG. Based on HR@5, ou proposed DL-BGM outperforms all the baselines by 26.2%–3,739.3%. Results based on NDCG show similar improvements.

Table 5 lists AL@N results (n � 1, 5, and 10) for all the models and the relative increase DL-BGM has over each model. Our proposed DL-BGM demonstrates significant superiority over all baselines in terms of ${ \mathrm { A L } } ,$ which indicates that the music clips recommended by our model can produce videos liked by more viewers. This could imply that the music clip recommended is suitable for the video and, thus, increases the likeability of the video.

## 5.6. Ablation Studies

Besides comparing across different models, we conduct ablation studies to further assess the components and the features incorporated in our DL-BGM model.

First, we study the contribution of the user–music and video–music matching modules. Because these two modules are not entirely independent of each other, we need to make some modifications to the model when removing one of them. If we remove the user–music matching module (the left half of the framework in Figure 2), the pooling layer whose output is used by the video–music matching module is also removed. Therefore, we define a context vector to replace the pooling layer output. The context vector represents the features of music matching with the video and is learned via model training (Bahdanau et al. 2015). A similar procedure is conducted when removing the video–music matching module from the model.

In these two matching modules, we further assess the contribution of the component based on user- and videorelated music features. If we remove the component based on user-related music features in the user–music matching module, the pooling layer whose output is used by the video–music matching module is also removed. We also adopt a context vector to replace the pooling layer output. A similar procedure applies to removing the aggregation and pooling layers in the video–music matching module. Moreover, we examine the effect of the attention mechanism used in the two aggregation layers. Removing attention from the aggregation layers degrades the aggregation layers to the pooling layers, which means we use the results of the pooling layer as the input to the prediction layer without going through weighted aggregation.

Table 4. Comparison with Baselines Based on HR@N and NDCG@N

<table><tr><td>Model</td><td>HR@1</td><td>HR@5</td><td>HR@10</td><td>NDCG@1</td><td>NDCG@5</td><td>NDCG@10</td></tr><tr><td>Top Popular</td><td>0.000233(+32,013.3%)</td><td>0.00510(+3,739.3%)</td><td>0.0162(+1,610.5%)</td><td>0.000233(+32,013.3%)</td><td>0.00256(+5,201.2%)</td><td>0.00605(+2,578.7%)</td></tr><tr><td>KNN</td><td>0.0419(+78.6%)</td><td>0.0836(+134.0%)</td><td>0.1109(+149.2%)</td><td>0.0419(+78.6%)</td><td>0.0633(+114.8%)</td><td>0.0721(+124.7%)</td></tr><tr><td>MF</td><td>0.0153(+388.5%)</td><td>0.0694(+182.0%)</td><td>0.1203(+129.8%)</td><td>0.0153(+388.5%)</td><td>0.0421(+223.1%)</td><td>0.0584(+177.4%)</td></tr><tr><td>NeuMF (Logit)</td><td>0.0111(+575.6%)</td><td>0.0601(+225.7%)</td><td>0.1148(+140.7%)</td><td>0.0111(+575.6%)</td><td>0.0351(+287.7%)</td><td>0.0526(+208.1%)</td></tr><tr><td>NeuMF (BPR)</td><td>0.0161(+365.0%)</td><td>0.0700(+179.4%)</td><td>0.1261(+119.1%)</td><td>0.0161(+365.0%)</td><td>0.0427(+218.6%)</td><td>0.0606(+167.2%)</td></tr><tr><td>LFM</td><td>0.0156(+379.8%)</td><td>0.0551(+254.8%)</td><td>0.0926(+198.5%)</td><td>0.0156(+379.8%)</td><td>0.0352(+285.7%)</td><td>0.0472(+243.1%)</td></tr><tr><td>PDSM</td><td>0.0150(+397.6%)</td><td>0.0548(+256.7%)</td><td>0.0916(+201.7%)</td><td>0.0150(+397.6%)</td><td>0.0348(+290.3%)</td><td>0.0466(+247.3%)</td></tr><tr><td>MF+LFM</td><td>0.0201(+272.0%)</td><td>0.0766(+155.2%)</td><td>0.1295(+113.5%)</td><td>0.0201(+272.0%)</td><td>0.0481(+182.7%)</td><td>0.0650(+149.1%)</td></tr><tr><td>NeuMF (Logit)+LFM</td><td>0.0225(+232.2%)</td><td>0.0853(+129.4%)</td><td>0.1439(+92.0%)</td><td>0.0225(+232.2%)</td><td>0.0537(+153.0%)</td><td>0.0725(+123.3%)</td></tr><tr><td>NeuMF (BPR)+LFM</td><td>0.0222(+236.4%)</td><td>0.0832(+135.3%)</td><td>0.1393(+98.4%)</td><td>0.0222(+236.4%)</td><td>0.0525(+158.8%)</td><td>0.0705(+129.8%)</td></tr><tr><td>MF+PDSM</td><td>0.0205(+265.5%)</td><td>0.0775(+152.3%)</td><td>0.1299(+112.7%)</td><td>0.0205(+265.5%)</td><td>0.0489(+177.8%)</td><td>0.0657(+146.5%)</td></tr><tr><td>NeuMF (Logit)+PDSM</td><td>0.0231(+223.7%)</td><td>0.0866(+125.8%)</td><td>0.1440(+91.9%)</td><td>0.0231(+223.7%)</td><td>0.0547(+148.4%)</td><td>0.0731(+121.5%)</td></tr><tr><td>NeuMF (BPR)+PDSM</td><td>0.0224(+234.7%)</td><td>0.0837(+133.9%)</td><td>0.1403(+97.0%)</td><td>0.0224(+234.7%)</td><td>0.0530(+156.6%)</td><td>0.0711(+127.7%)</td></tr><tr><td>FM-BGM</td><td>0.0350(+113.7%)</td><td>0.1091(+79.2%)</td><td>0.1689(+63.6%)</td><td>0.0350(+113.7%)</td><td>0.0724(+87.8%)</td><td>0.0915(+76.9%)</td></tr><tr><td>TF-BGM</td><td>0.0158(+372.7%)</td><td>0.0752(+160.1%)</td><td>0.1356(+103.8%)</td><td>0.0158(+372.7%)</td><td>0.0449(+202.8%)</td><td>0.0642(+152.4%)</td></tr><tr><td>MF-BGM</td><td>0.0504(+48.5%)</td><td>0.1550(+26.2%)</td><td>0.2319(+19.2%)</td><td>0.0504(+48.5%)</td><td>0.1030(+31.9%)</td><td>0.1277(+26.8%)</td></tr><tr><td>DL-BGM</td><td>0.0748</td><td>0.1956</td><td>0.2764</td><td>0.0748</td><td>0.1359</td><td>0.1620</td></tr></table>

Table 6 reports HR@5 results for the ablation study for component contribution of DL-BGM. Detailed results are provided in Online Appendix C. Note that U2M means that the user–music matching module is included, and V2M means that the video–music matching module is contained. U2M/R implies that the component based on user-related music features is excluded. U2M/A means that the attention mechanism in the component based on user-related music features is removed. V2M/R and V2M/A are defined similarly.

Table 5. Comparison with Baselines Based on AL@N

<table><tr><td>Model</td><td colspan="2">AL@1</td><td colspan="2">AL@5</td><td colspan="2">AL@10</td></tr><tr><td>Top Popular</td><td>1.30</td><td>(+70,990.1%)</td><td>42.1</td><td>(+5,137.2%)</td><td>82.2</td><td>(+3,462.7%)</td></tr><tr><td>KNN</td><td>684.6</td><td>(+34.7%)</td><td>1,190.1</td><td>(+85.2%)</td><td>1,543.1</td><td>(+89.8%)</td></tr><tr><td>MF</td><td>185.7</td><td>(+396.5%)</td><td>813.7</td><td>(+170.9%)</td><td>1,219.8</td><td>(+140.1%)</td></tr><tr><td>NeuMF (Logit)</td><td>90.6</td><td>(+917.7%)</td><td>590.2</td><td>(+273.5%)</td><td>1,228.0</td><td>(+138.5%)</td></tr><tr><td>NeuMF (BPR)</td><td>250.7</td><td>(+267.9%)</td><td>943.3</td><td>(+133.7%)</td><td>1,479.9</td><td>(+97.9%)</td></tr><tr><td>LFM</td><td>233.4</td><td>(+295.2%)</td><td>622.5</td><td>(+254.1%)</td><td>1,095.9</td><td>(+167.3%)</td></tr><tr><td>PDSM</td><td>219.6</td><td>(+320.0%)</td><td>595.1</td><td>(+270.4%)</td><td>1,026.9</td><td>(+185.2%)</td></tr><tr><td>MF+LFM</td><td>290.7</td><td>(+217.2%)</td><td>957.4</td><td>(+130.2%)</td><td>1,514.0</td><td>(+93.5%)</td></tr><tr><td>NeuMF (Logit)+LFM</td><td>309.5</td><td>(+198.0%)</td><td>922.7</td><td>(+138.9%)</td><td>1,549.7</td><td>(+89.0%)</td></tr><tr><td>NeuMF (BPR)+LFM</td><td>273.4</td><td>(+237.3%)</td><td>1,090.7</td><td>(+102.1%)</td><td>1,705.7</td><td>(+71.7%)</td></tr><tr><td>MF+PDSM</td><td>279.8</td><td>(+229.7%)</td><td>836.7</td><td>(+163.4%)</td><td>1,575.7</td><td>(+85.9%)</td></tr><tr><td>NeuMF (Logit)+PDSM</td><td>265.4</td><td>(+247.5%)</td><td>851.9</td><td>(+158.7%)</td><td>1,511.5</td><td>(+93.8%)</td></tr><tr><td>NeuMF (BPR)+PDSM</td><td>227.4</td><td>(+305.6%)</td><td>861.2</td><td>(+155.9%)</td><td>1,664.1</td><td>(+76.0%)</td></tr><tr><td>FM-BGM</td><td>291.3</td><td>(+216.6%)</td><td>1,105.1</td><td>(+99.4%)</td><td>1,825.8</td><td>(+60.4%)</td></tr><tr><td>TF-BGM</td><td>171.9</td><td>(+436.5%)</td><td>753.6</td><td>(+192.5%)</td><td>1,320.9</td><td>(+121.7%)</td></tr><tr><td>MF-BGM</td><td>482.7</td><td>(+91.1%)</td><td>1,579.1</td><td>(+39.6%)</td><td>2,229.4</td><td>(+31.4%)</td></tr><tr><td>DL-BGM</td><td>922.3</td><td></td><td>2,204.1</td><td></td><td>2,929.0</td><td></td></tr></table>

Table 6. Ablation Study for Component Contribution of DL-BGM

<table><tr><td rowspan="3">Model</td><td colspan="3">User-music matching</td><td colspan="3">Video-music matching</td><td rowspan="3">HR@5</td></tr><tr><td rowspan="2">User features</td><td colspan="2">User-related music features</td><td rowspan="2">Video features</td><td colspan="2">Video-related music features</td></tr><tr><td>Aggregation</td><td>Attention</td><td>Aggregation</td><td>Attention</td></tr><tr><td>V2M</td><td>×</td><td>×</td><td>×</td><td>√</td><td>√</td><td>√</td><td>0.1136(+72.3%)</td></tr><tr><td>U2M/R+V2M</td><td>√</td><td>×</td><td>×</td><td>√</td><td>√</td><td>√</td><td>0.1859(+5.22%)</td></tr><tr><td>U2M/A+V2M</td><td>√</td><td>√</td><td>×</td><td>√</td><td>√</td><td>√</td><td>0.1870(+4.64%)</td></tr><tr><td>U2M</td><td>√</td><td>√</td><td>√</td><td>×</td><td>×</td><td>×</td><td>0.1594(+22.7%)</td></tr><tr><td>U2M+V2M/R</td><td>√</td><td>√</td><td>√</td><td>√</td><td>×</td><td>×</td><td>0.1861(+5.11%)</td></tr><tr><td>U2M+V2M/A</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>×</td><td>0.1865(+4.87%)</td></tr><tr><td>DL-BGM</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>0.1956</td></tr></table>

Compared with V2M, DL-BGM improves HR@5 by 72.3%, which demonstrates the importance of the user– music matching module. DL-BGM outperforms U2M by 22.7%, showing the contribution of the video–music matching module. The 5.22% improvement DL-BGM has over U2M/R+V2M shows that the user’s related music clips matter. The performance difference between U2M+V2M/R and DL-BGM is 5.11%, which shows the contribution of the video’s related music clips.

If we remove the aggregation layer with attention from the user–music matching module, the model becomes U2M/A+V2M. The improvement DL-BGM has over U2M/A+V2M is 4.64%, showing the contribution of the attention layer. Similarly, U2M+V2M/A is the model after we remove the attention layer with attention in the video–music matching module. DL-BGM has an improvement of 4.87% over U2M+V2M/A, showing that the attention weights for the music features of the video’s related music clips contribute much higher than those for the music features of the user’s adopted music clips.

In addition, we also study the contribution of each type of music and video features used in the proposed model. We design the ablation study as shown in Table 7. The first five models (GLMP/GLMT/GLPT/GMPT/ LMPT+CT) keep all the model components, but each misses a type of music feature, and the following two mod els (GLMPT+C/T) also keep all the model components, but each misses a type of video feature. We present the HR@5 results and the percentage improvement DL-BGM has over that model in the last column of Table 7. Please refer to Online Appendix C for detailed results.

Comparing DL-BGM-GLMP/GLMT/GLPT/GMPT/ LMPT+CT with DL-BGM, we can see that adding one type of music feature improves HR@5 by about 4%, and the tempo features contribute a little more than other features. Comparing DL-BGM-GLMPT+C and DL-BGM-GLMPT-T with DL-BGM, we can find that the text embeddings contribute more than the CNN features.

Table 7. Ablation Study for Feature Contribution of DL-BGM

<table><tr><td rowspan="2">Model</td><td colspan="5">Music features</td><td colspan="2">Video features</td><td rowspan="2">HR@5</td></tr><tr><td>Genre</td><td>Lyrics</td><td>MFCCs</td><td>Popularity</td><td>Tempo</td><td>CNN features</td><td>Text embeddings</td></tr><tr><td>GLMP+CT</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>0.1859(+5.25%)</td></tr><tr><td>GLMT+CT</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>0.1867(+4.78%)</td></tr><tr><td>GLPT+CT</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>0.1863(+4.99%)</td></tr><tr><td>GMPT+CT</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>0.1863(+5.02%)</td></tr><tr><td>LMPT+CT</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>0.1869(+4.66%)</td></tr><tr><td>GLMPT+C</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>0.1741(+12.4%)</td></tr><tr><td>GLMPT+T</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>0.1858(+5.29%)</td></tr><tr><td>DL-BGM</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>0.1956</td></tr></table>

Panel B. New music clips  
Figure 6. Data Distributions in the Raw Data Set  
(a)  
![](/api/attachments/ECJCETUX/fulltext/images/4af790224650876fb5735aafe23e409ac1e09a8d84f0f92a574a753e22021607.jpg)

(b)  
![](/api/attachments/ECJCETUX/fulltext/images/4db73fccba2b6acc7ed43530368edcf1e281538a1fa7f8c120a1a1b4d5ec5fb7.jpg)  
Notes. (a) Histogram of number of music clips chosen by a user (with y-axis in log scale). (b) Histogram of number of users choosing a music clip.

## 5.7. Cold-Start Recommendations

In the raw data set, most users have very few historical videos, and not many music clips are chosen by a lot of users as illustrated in Figure 6. In order to show that our methods also work on users with few videos and music clips adopted by few users, we further investigate coldstart recommendations for new users with no published videos and new music clips with no user adoption.

For a new creator, we obtain neighboring users and then aggregate information from similar creators to represent the new creator. Likewise, we represent a new music clip using aggregated information from its neighboring music clips. The results are presented in Table 8. We can see that DL-BGM outperforms all the baselines based on HR@5, which indicates the capability of our proposed model to tackle cold-start problems. Note that DL-BGM performs 172.7% better than MF-BGM in handling new video creators and 25.3% better in handling new music clips. Please refer to Online Appendix D for more detailed results.

## 5.8. Generalizability and Robustness

In our main experiments presented in Section 5.5, we use a dense data set in which the number of videos for each music clip and the number of videos for each user is no smaller than a threshold of 10. To investigate our model’s performance on the original data distribution, we randomly select a subset (with 16,559 users) from the raw data set and conduct further experiments. Table 9 reports comparison results between our proposed model and representative baselines. Our DL-BGM still maintains considerable relative improvements over KNN, NeuMF (Logit)+PDSM (the best among all two-step models), FM-BGM (the best among baselines considering user, music clip, and video factors), and MF-BGM (the best among all the baselines), which indicates the generalizability of our proposed model.

Table 8. Comparison for Cold-Start Recommendations Based on HR@5

<table><tr><td>Model</td><td colspan="2">HR@5</td></tr><tr><td colspan="3">Panel A. New video creators</td></tr><tr><td>Top Popular</td><td>0.00172</td><td>(+3,104.0%)</td></tr><tr><td>KNN</td><td>0.00944</td><td>(+482.3%)</td></tr><tr><td>MF</td><td>0.00546</td><td>(+906.1%)</td></tr><tr><td>NeuMF (Logit)</td><td>0.00603</td><td>(+811.6%)</td></tr><tr><td>NeuMF (BPR)</td><td>0.00657</td><td>(+736.2%)</td></tr><tr><td>LFM</td><td>0.0178</td><td>(+208.4%)</td></tr><tr><td>PDSM</td><td>0.0197</td><td>(+178.5%)</td></tr><tr><td>MF+LFM</td><td>0.00793</td><td>(+593.5%)</td></tr><tr><td>NeuMF (Logit)+LFM</td><td>0.00948</td><td>(+480.0%)</td></tr><tr><td>NeuMF (BPR)+LFM</td><td>0.00690</td><td>(+696.7%)</td></tr><tr><td>MF+PDSM</td><td>0.00859</td><td>(+539.8%)</td></tr><tr><td>NeuMF (Logit)+PDSM</td><td>0.0104</td><td>(+426.0%)</td></tr><tr><td>NeuMF (BPR)+PDSM</td><td>0.00756</td><td>(+627.1%)</td></tr><tr><td>FM-BGM</td><td>0.00641</td><td>(+757.8%)</td></tr><tr><td>TF-BGM</td><td>0.00604</td><td>(+809.2%)</td></tr><tr><td>MF-BGM</td><td>0.0202</td><td>(+172.7%)</td></tr><tr><td>DL-BGM</td><td>0.0550</td><td></td></tr></table>

<table><tr><td colspan="3">Panel B. New music clips</td></tr><tr><td>Top Popular</td><td>0.00492</td><td>(+3,694.1%)</td></tr><tr><td>KNN</td><td>0.0807</td><td>(+131.2%)</td></tr><tr><td>MF</td><td>0.0669</td><td>(+178.7%)</td></tr><tr><td>NeuMF (Logit)</td><td>0.0579</td><td>(+222.3%)</td></tr><tr><td>NeuMF (BPR)</td><td>0.0675</td><td>(+176.2%)</td></tr><tr><td>LFM</td><td>0.0536</td><td>(+248.1%)</td></tr><tr><td>PDSM</td><td>0.0528</td><td>(+253.5%)</td></tr><tr><td>MF+LFM</td><td>0.0733</td><td>(+154.5%)</td></tr><tr><td>NeuMF (Logit)+LFM</td><td>0.0822</td><td>(+127.0%)</td></tr><tr><td>NeuMF (BPR)+LFM</td><td>0.0794</td><td>(+134.9%)</td></tr><tr><td>MF+PDSM</td><td>0.0750</td><td>(+148.6%)</td></tr><tr><td>NeuMF (Logit)+PDSM</td><td>0.0832</td><td>(+124.1%)</td></tr><tr><td>NeuMF (BPR)+PDSM</td><td>0.0807</td><td>(+131.1%)</td></tr><tr><td>FM-BGM</td><td>0.1054</td><td>(+77.1%)</td></tr><tr><td>TF-BGM</td><td>0.0764</td><td>(+144.1%)</td></tr><tr><td>MF-BGM</td><td>0.1489</td><td>(+25.3%)</td></tr><tr><td>DL-BGM</td><td>0.1866</td><td></td></tr></table>

To examine the sensitivity of the data filtering threshold, we vary the threshold among {1, 3, 5, 10, 15, 20}. Results demonstrate that the superiority of our proposed model still holds across data sets with different density levels. Please refer to Online Appendix E.1 for more details.

To further validate the cross–data set generalizability of our proposed model, we extract videos in different categories and conduct comparisons with representative baselines. Specifically, we constructed two data sets comprising videos that contain text pertaining to two representative categories, namely, “food” and “location,” respectively. As shown in Table 10, our DL-BGM still performs better than other alternatives in both the food- and location-related data sets. Details of data extraction and performance comparisons are provided in Online Appendix E.2.

We also conduct experiments to evaluate the robustness of DL-BGM against hyperparameter changes. We need to choose parameters for the number of similar videos, the dimension of user embedding, and the dimension of video embedding. We run experiments with the number of similar videos among {50, 100, 150, 200, 250} and get the best HR@5 result of 0.1956 at 100 and the worst result of 0.1945 at 150. We also run experiments with the dimension of user embedding among {100, 200, 300, 400, 500} and the dimension of video embedding among {800, 1,200, 1,600, 2,000, 2,400}, respectively. We can get stable results for different dimensions of user and video embedding. Please refer to Online Appendix F for the detailed results of the robustness study.

## 6. Discussion

## 6.1. Managerial Implication

Our improved recommendation systems can have significant managerial implications for content creators, content consumers, platforms, and even the music industry.

Table 9. Results on a Random Sample of the Raw Data Set

<table><tr><td>Model</td><td colspan="2">HR@5</td></tr><tr><td>KNN</td><td>0.0521</td><td>(+255.0%)</td></tr><tr><td>NeuMF (Logit)+PDSM</td><td>0.1328</td><td>(+39.2%)</td></tr><tr><td>FM</td><td>0.1406</td><td>(+31.5%)</td></tr><tr><td>MF-BGM</td><td>0.1641</td><td>(+12.7%)</td></tr><tr><td>DL-BGM</td><td>0.1849</td><td></td></tr></table>

Table 10. Results on Data Sets with Different Video Categories

<table><tr><td>Model</td><td colspan="2">HR@5</td></tr><tr><td colspan="3">Panel A. Results for the food-related data set</td></tr><tr><td>KNN</td><td>0.0769</td><td>(+83.2%)</td></tr><tr><td>NeuMF (Logit)+PDSM</td><td>0.0607</td><td>(+132.2%)</td></tr><tr><td>FM</td><td>0.0923</td><td>(+52.7%)</td></tr><tr><td>MF-BGM</td><td>0.1256</td><td>(+12.3%)</td></tr><tr><td>DL-BGM</td><td>0.1410</td><td></td></tr><tr><td colspan="3">Panel B. Results for the location-related data set</td></tr><tr><td>KNN</td><td>0.1194</td><td>(+75.7%)</td></tr><tr><td>NeuMF (Logit)+PDSM</td><td>0.0908</td><td>(+131.1%)</td></tr><tr><td>FM</td><td>0.1263</td><td>(+66.1%)</td></tr><tr><td>MF-BGM</td><td>0.1581</td><td>(+32.7%)</td></tr><tr><td>DL-BGM</td><td>0.2098</td><td></td></tr></table>

From the content producer’s perspective, our recommendation models can help them find the right music clip more efficiently without spending time testing, evaluating, and comparing different music clips. This increases productivity and improves the experience in the creation process. Also, because the music recommendations consider producers’ preferences, content producers can be more satisfied with their creations (i.e., user-generated short videos with desirable music clips), which will encourage them to upload more videos and, hence, improve their participation. Our recommendations also consider the matching between music clips and videos; therefore, the videos created tend to have higher quality because of more suitable background music and can be received better by viewers, which could potentially encourage content producers to create more videos.

From the content consumer’s perspective, they will enjoy higher quality videos with suitable background music. The fit between music and video can increase the satisfaction and engagement of viewers. Viewers give likes to satisfactory videos and share them on social media. The improvement of the overall experience on the platform may encourage viewers to spend more time watching short videos and may even motivate them to add background music to their own videos.

Our background music recommender systems can potentially benefit stakeholders in the music industry. As our system produces good-quality videos with background music, it may promote more video producers to add background music to their videos, which could increase the adoption of music on the video platform. Exposure to a short music clip on the short video platform could potentially increase the viewer’s interest for the music itself, which could trigger the viewer to purchase the whole music from other music platforms, further increasing the revenue for different players behind the music, including the music copyright owner, singer, producer, etc.

The video platform is probably the biggest beneficiary of an excellent background music recommendation system. A good recommender system makes it easier for content producers to accomplish their creative work on the platform, increasing productivity and attracting more producers to the platform. With more creators joining the platform to produce good-quality videos, it can build a better platform ecosystem, which can promote the platform’s growth and development.

## 6.2. Practical Applicability

The fundamental design principles that underlie our DL-BGM model can be readily applied to a variety of contexts characterized by similar three-way relationships. When a user is crafting original content and seeking recommendations to enhance it, the underlying dynamics resemble the three-way relationship encountered in our background music recommendation problem. Examples of such applications include but are not limited to assisting users in selecting postprocessing effects to enhance their content (e.g., adding photo/video effects), offering prebuilt templates to elevate the design of users’ content (e.g., slide design), facilitating the expansion of users’ existing content selections (e.g., suggesting songs to add to their playlists), and other scenarios in which recommendation is used within the process of content creation (e.g., suggesting emojis as users input text). The core design principles that empower our DL-BGM model can be harnessed effectively across this spectrum of applications.

In these recommendation scenarios, their three-way relationships are similar to ours, and our proposed model can be customized to address their recommendation problem effectively. Consider the context of postprocessing effect recommendations, in which users often seek to enhance their content using tools, such as photo filters for image refinement or video effects for video editing. Let’s take the example of adding photo filters. Each photo is associated with a single user as its owner, and each photo is paired with just one filter, mirroring the three-way relationship in our model. To model the user–content–effect relationship, we can design user–effect and content–effect matching modules similar to our proposed model. When it comes to template recommendation, for tasks such as blog editing or slide design, our proposed model can effectively capture the user–content–template relationship by evaluating the template’s alignment with the user and its appropriateness for the content. In the scenario of expanding users’ existing content selections, our proposed model can also be applied to provide recommendations on what content to add next. For instance, it can determine the next curated item for user-generated lists, such as song playlists or book lists. In these scenarios, our model can be tailored to accurately capture the user–content–next relationship. In situations in which the next content is similar in nature to the existing content, we can enhance the proposed model to take this connection into consideration. Taking song playlist expansion as an example, the song playlists consist of songs and contain information about song co-occurrence in playlists. In the model framework, we can incorporate an enhanced representation learning component designed for songs and playlists within the playlist–song matching module. In the emoji recommendation scenario, the user–text–emoji relationship can be captured by considering both the user’s and the text’s matching with emojis.

## 7. Conclusion

In this paper, we study how to recommend suitable background music for short videos on short video sharing platforms. To the best of our knowledge, this is the first work that studies this problem by incorporating user, video, and music clip information simultaneously. To address the unique background music recommendation problem and properly model the unique user–video–music three-way relationship, we propose a deep learning–based model (DL-BGM), which considers the user’s matching with music and the video’s matching with music. DL-BGM contains a user–music matching module and a video–music matching module to deal with the threeway relationship. For the user–music matching module, we model the relationship between user and music from both the user and the music space. Likewise, for the video–music matching module, we model the relationship between video and music from both the video and the music space. We design specific components to borrow information from music clips that the user has used before and music clips used in similar hit videos to deal with the different space problems in the two modules. We further propose attention-based aggregation for more accurate music feature extraction. We also extend the proposed model to handle cold-start recommendations for new users with no previous history of video creation and new music clips with no history of being adopted.

We conducted extensive experiments to evaluate the proposed model. Results show that DL-BGM significantly outperforms all baseline models in terms of HR, NDCG, and AL. Specifically, the user–music matching module offers an impressive lift in the performances by about 70%, whereas the video–music matching mod ule improves the performances by about 20%. The attention-based aggregation layers in the two modules increase the performances by about 5%, respectively. These experimental results show the importance of capturing the alignment between users and music clips and the effectiveness of considering the matching between videos and music clips in background music recommendation. The superiority of our proposed model still holds for cold-start recommendations for new video creators and new music clips. DL-BGM also performs best among all alternative models across data sets with different density levels and from different video categories, which indicates the generalizability of our proposed model.

Our research has several limitations that can be further studied in the future. On the short video platform from which we collected our data, the background music might have been decided before the video is created (e.g., creating a video based on trendy music). For the model training purpose, it should not be a significant concern to have some music-first entries in the data because our model mostly learns the matching between music and video and is not reliant on which comes first in the process. When platforms adopt our model, they can just use the video-first data to train the model and apply the model to only recommend music to videos. Another data limitation is that we only use a one-hot vector capturing user identification to represent users in the experiments because there are no other user features available in our collected data. If other user features, such as demographic features, become available in the future, we can directly feed them into the proposed model to capture features useful for the prediction task. If we get access to more user-related information, we can also implement the more comprehensive solutions we offer for addressing the cold-start problem. In addition, users’ music selections collected in the data may be slightly influenced by existing recommendation engines, which is a common issue in recommender systems research. In future research, we can dedicate special attention to designing ways to reduce this type of data bias. Besides, content producers as consumers are not considered in this study. In future studies, we can design methods to incorporate four players (users as content producers, users as content consumers, videos, and music clips) because content producers’ consumption behavior may also affect their preferences toward background music selection. Furthermore, should pertinent data become accessible, we can augment our model evaluation with additional metrics beyond hit rate and average likes. These additional metrics may encompass factors such as individual video-specific financial returns, among others.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three anonymous reviewers for their insightful comments and suggestions throughout the review process.

## References

Abu-El-Haija S, Kothari N, Lee J, Natsev P, Toderici G, Varadarajan B, Vijayanarasimhan S (2016) Youtube-8m: A large-scale video classification benchmark. Preprint, submitted September 27, https://arxiv.org/abs/1609.08675.

Bahdanau D, Cho KH, Bengio Y (2015) Neural machine translation by jointly learning to align and translate. Proc. Third Internat. Conf. Learn. Representation (ICLR, Appleton, WI), 1–5.

Bi X, Qu A, Shen X (2018) Multilayer tensor factorization with appli cations to recommender systems. Ann. Statist. 46(6B):3308–3333.

Blacker A (2023) Worldwide and US download leaders 2022. Accessed January 17, 2024, https://blog.apptopia.com/worldwideand-us-download-leaders-2022.

Braunhofer M, Kaminskas M, Ricci F (2013) Location-aware music recommendation. Internat. J. Multimedia Inform. Retrieval 2(1): 31–44.

Brent W (2009) Cepstral analysis tools for percussive timbre identifi cation. Proc. Third Internat. Pure Data Convention, 1–7.

Cano P, Koppenberger M, Wack N (2005) Content-based music audio recommendation. Proc. 13th Annual ACM Internat. Conf. Multimedia (ACM, New York), 211–212.

Devlin J, Chang MW, Lee K, Toutanova K (2018) BERT: Pre-training of deep bidirectional transformers for language understanding Preprint, submitted October 11, https://arxiv.org/abs/1810. 04805.

Galli M, Gurini DF, Gasparetti F, Micarelli A, Sansonetti G (2015) Analysis of user-generated content for improving YouTube video. Proc. 9th RecSys Posters (ACM, New York), 1–2.

Go´mez-Can˜o´n JS, Cano E, Eerola T, Herrera P, Hu X, Yang YH, Go´mez E (2021) Music emotion recognition: Toward new, robust standards in personalized and context-sensitive applica tions. IEEE Signal Processing Magazine 38(6):106–114.

Gomez-Uribe CA, Hunt N (2015) The netflix recommender system: Algorithms, business value, and innovation. ACM Trans. Man agement Inform. Systems 6(4):1–19.

Grosche P, Mu¨ ller M, Kurth F (2010) Cyclic tempogram—A midlevel tempo representation for music signals. Proc. 2010 IEEE Internat. Conf. Acoustics Speech Signal Processing (IEEE, Piscataway, NJ), 5522–5525.

Hansen C, Hansen C, Maystre L, Mehrotra R, Brost B, Tomasi F, Lalmas M (2020) Contextual and sequential user embeddings for large-scale music recommendation. Proc. 14th ACM Conf. Recommender Systems (ACM, New York), 53–62.

Harper FM, Konstan JA (2015) The MovieLens datasets: History and context. ACM Trans. Interactive Intelligent Systems 5(4):1–19.

He R, Fang C, Wang Z, McAuley J (2016) Vista: A visually, socially, and temporally-aware model for artistic recommendation. Proc. 10th ACM Conf. Recommender Systems (ACM, New York), 309–316.

He X, Liao L, Zhang H, Nie L, Hu X, Chua TS (2017) Neural collaborative filtering. Proc. 26th Internat. Conf. World Wide Web (ACM, New York), 173–182.

Hochreiter S, Schmidhuber J (1997) Long short-term memory. Neural Comput. 9(8):1735–1780.

HuggingFace (2020) BERT-base-Chinese. Accessed December 28, 2023, https://huggingface.co/bert-base-chinese.

Johnson CC (2014) Logistic matrix factorization for implicit feedback data. Adv. Neural Inform. Processing Systems 27(78):1–9.

Kaminskas M, Ricci F, Schedl M (2013) Location-aware music recommendation using auto-tagging and hybrid matching. Proc. 7th ACM Conf. Recommender Systems (ACM, New York), 17–24.

Kang WC, McAuley J (2018) Learning consumer and producer embeddings for user-generated content recommendation. Proc 12th ACM Conf. Recommender Systems (ACM, New York), 407–411.

Krizhevsky A, Sutskever I, Hinton GE (2017) ImageNet classification with deep convolutional neural networks. Comm. ACM 60(6):84–90

Kumar V, Minz S (2013) Mood classification of lyrics using Senti-WordNet. Proc. 2013 Internat. Conf. Computer Comm. Inform. (IEEE, Piscataway, NJ), 1–5.

Kuo FF, Shan MK, Lee SY (2013) Background music recommendation for video based on multimodal latent semantic analysis. Proc. 2013 IEEE Internat. Conf. Multimedia Expo (IEEE, Piscat away, NJ), 1–6.

Li W, Zhang Y, Sun Y, Wang W, Li M, Zhang W, Lin X (2019) Approximate nearest neighbor search on high dimensional

data—Experiments, analyses, and improvement. IEEE Trans. Knowledge Data Engrg. 32(8):1475–1488.

Liang D, Zhan M, Ellis DP (2015) Content-aware collaborative music recommendation using pre-trained neural networks. Proc. 16th Internat. Soc. Music Inform. Retrieval Conf. (ISMIR, Canada), 295–301.

Liao C, Wang PP, Zhang Y (2009) Mining association patterns between music and video clips in professional MTV. Proc. 15th Internat. Conf. Multimedia Model. (Springer, New York), 401–412.

Lin TW, Shan MK (2017) Correlation-based background music recommendation by incorporating temporal sequence of local features. Proc. Third IEEE Internat. Conf. Multimedia Big Data (IEEE, Piscataway, NJ), 158–164.

Lin JC, Wei WL, Wang HM (2016) DEMV-matchmaker: Emotiona temporal course representation and deep similarity matching for automatic music video generation. Proc. 2016 IEEE Internat. Conf. Acoustics Speech Signal Processing (IEEE, Piscataway, NJ), 2772–2776.

Lin YT, Tsai TH, Hu MC, Cheng WH, Wu JL (2014) Semantic based background music recommendation for home videos. Internat. Conf. Multimedia Model. (Springer International Publishing, Cham, Switzerland), 283–290.

Lin JC, Wei WL, Yang J, Wang HM, Liao HYM (2017) Automatic music video generation based on simultaneous soundtrack recommendation and video editing. Proc. 25th ACM Internat. Conf. Multimedia (ACM, New York), 519–527.

Linden G, Smith B, York J (2003) Amazon.com recommendations: Item to-item collaborative filtering. IEEE Internet Comput. 7(1): 76–80

Liu CL, Chen YC (2018) Background music recommendation based on latent factors and moods. Knowledge Based Systems 159: 158–170.

Liu T, Moore A, Yang K, Gray A (2004) An investigation of practical approximate nearest neighbor algorithms. Adv. Neural Inform. Processing Systems 17 (MIT Press, Cambridge, MA).

Logan B (2004) Music recommendation from song sets. Proc. Fifth Inter nat. Soc. Music Inform. Retrieval Conf. (ISMIR, Canada), 425–428.

Magron P, Fe´votte C (2021) Leveraging the structure of musical preference in content-aware music recommendation. Proc. 2021 IEEE Internat. Conf. Acoustics Speech Signal Processing (IEEE, Piscataway, NJ), 581–585.

Mayer R, Neumayer R, Rauber A (2008) Combination of audio and lyrics features for genre classification in digital audio collections. Proc. 16th ACM Internat. Conf. Multimedia (ACM, New York), 159–168.

McFee B, Raffel C, Liang D, Ellis DP, McVicar M, Battenberg E, Nieto O (2015) Librosa: Audio and music signal analysis in Python. Proc. 14th Python Sci. Conf., vol. 8, 18–25.

Nagawade MS, Ratnaparkhe VR (2017) Musical instrument identification using MFCC. Proc. Second IEEE Internat. Conf. Recent Trends Electronics Inform. Comm. Tech. (IEEE, Piscataway, NJ), 2198–2202.

Nalini N, Palanivel S (2016) Music emotion recognition: The combined evidence of MFCC and residual phase. Egyptian Inform. J. 17(1):1–10.

Nanopoulos A, Rafailidis D, Symeonidis P, Manolopoulos Y (2009) Musicbox: Personalized music recommendation based on cubic analysis of social tags. IEEE Trans. Audio Speech Language Proces sing 18(2):407–412.

Pre´tet L, Richard G, Peeters G (2021) Cross-modal music-video recommendation: A study of design choices. Proc. 2021 Internat. Joint Conf. Neural Networks (IEEE, New York), 1–9.

Reimers N, Gurevych I (2019) Sentence-BERT: Sentence embeddings using Siamese BERT-networks. Proc. 2019 Conf. Empirical Methods Natl. Language Processing Ninth Internat. Joint Conf. Natl. Language Processing (Association for Computational Linguistics, Stroudsburg, PA), 3982–3992.

Reimers N, Gurevych I (2020) Making monolingual sentence embeddings multilingual using knowledge distillation. Proc. 2020 Conf Empirical Methods Natl. Language Processing (Association fo Computational Linguistics, Stroudsburg, PA), 4512–4525.

Rendle S (2010) Factorization machines. Proc. 2010 IEEE Internat. Conf. Data Mining (IEEE, Piscataway, NJ), 995–1000

Rubens N, Elahi M, Sugiyama M, Kaplan D (2015) Active learning in recommender systems. Recommender Systems Handbook (Springer, Boston), 809–846.

Schein AI, Popescul A, Ungar LH, Pennock DM (2002) Methods and metrics for cold-start recommendations. Proc. 25th Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (ACM, New York), 253–260.

Shen M, Wang J, Liu O, Wang H (2020) Expert detection and recommendation model with user-generated tags in collaborative tagging systems. J. Database Management 31(4):24–45.

Simonyan K, Zisserman A (2014) Very deep convolutional networks for large-scale image recognition. Preprint, submitted Septem ber 4, https://arxiv.org/abs/1409.1556.

Sturm BL (2013) The GTZAN data set: Its contents, its faults, their effects on evaluation, and its future use. Preprint, submitted June 6, https://arxiv.org/abs/1306.1461.

Tsukuda K, Fukayama S, Goto M (2019) ABCPRec: Adaptively bridging consumer and producer roles for user-generated content recommendation. Proc. 42nd Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (ACM, New York), 1197–1200.

Tucker LR (1966) Some mathematical notes on three-mode factor analysis. Psychometrika 31(3):279–311.

Volkovs M, Yu G, Poutanen T (2017) Dropoutnet: Addressing cold start in recommender systems. Adv. Neural Inform. Processing Systems 30 (The MIT Press, Cambridge, MA).

Wang X, Wang Y (2014) Improving content-based and hybrid music recommendation using deep learning. Proc. 22nd ACM Internat. Conf. Multimedia (ACM, New York), 627–636.

Wang D, Deng S, Xu G (2018) Sequence-based context-aware music recommendation. Inform. Retrieval J. 21(2):230–252.

Wang X, Rosenblum D, Wang Y (2012) Context-aware mobile music recommendation for daily activities. Proc. 20th ACM Internat. Conf. Multimedia (ACM, New York), 99–108.

Wang X, Yu L, Ren K, Tao G, Zhang W, Yu Y, Wang J (2017) Dynamic attention deep model for article recommendation by learning human editors’ demonstration. Proc. 23rd ACM SIGKDD Inter nat. Conf. Knowledge Discovery Data Mining (ACM, New York), 2051–2059.

Yang C, Miao L, Jiang B, Li D, Cao D (2020) Gated and attentive neural collaborative filtering for user generated list recommendation. Knowledge Based Systems 187:104839.

Yi J, Zhu Y, Xie J, Chen Z (2021) Cross-modal variational autoencoder for content-based micro-video background music recommendation. JEEE Trans. Multimedia 25:515–528

Zhang S, Yao L, Sun A, Tay Y (2019) Deep learning based recommender system: A survey and new perspectives. ACM Comput Surveys 52(1):1–38

Zheng F, Zhang G, Song Z (2001) Comparison of different imple mentations of MFCC. J. Comput. Sci. Tech. 16(6):582–589

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
