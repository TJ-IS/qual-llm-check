---
otero_id: 19610
otero_key: "49YSUXA7"
title: "Deep learning based personalized recommendation with multi-view information integration"
authors: "Yue Guan; Qiang Wei; Guoqing Chen"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Deep learning based personalized recommendation with multi-view information integration

![](/api/attachments/49YSUXA7/fulltext/images/b7ba24ba1bb5d7e522a0bbf91bd72d4d7dc07b8bcb5954e2e14e0d623771e8e1.jpg)

Yue Guan, Qiang Wei<sup>⁎</sup>, Guoqing Chen

China Retail Research Center, School of Economics and Management, Tsinghua University, Beijing 100084, China

## A R T I C L E I N F O

Keywords: Multi-view information Deep learning Information integration Personalized recommendation Representation learning

## A B S T R A C T

With the rapid proliferation of images on e-commerce platforms today, embracing and integrating versatile information sources have become increasingly important in recommender systems. Owing to the heterogeneity in information sources and consumers, it is necessary and meaningful to consider the potential synergy between visual and textual content as well as consumers' diferent cognitive styles. This paper proposes a multi-view model, namely, Deep Multi-view Information iNtEgration (Deep-MINE), to take multiple sources of content (i.e., product images, descriptions and review texts) into account and design an end-to-end recommendation model. In doing so, stacked auto-encoder networks are deployed to map multi-view information into a unified latent space, a cognition layer is added to depict consumers' heterogeneous cognition styles and an integration module is introduced to reflect the interaction of multi-view latent representations. Extensive experiments on real world data demonstrate that Deep-MINE achieves high accuracy in product ranking, especially in the cold-start case. In addition, Deep-MINE is able to boost overall model performance compared with models taking a single view, further verifying the proposed model's efectiveness on information integration.

## 1. Introduction

The amount and variety of data are increasing exponentially in today's online marketplaces, of which multimedia and user-generated content account for a large proportion.<sup>1</sup> While consumers benefit from such rich and helpful information, they also face an information overload problem in their online shopping processes [7,22]. To alleviate this problem, some technological tools have been developed to assist con sumers in product search and decision-making. Recommender systems are one of the most widely applied decision aids that aim to provide personalized recommendation services for consumers. Recommender systems conduct in-depth mining of historical records, infer consumer preferences from the data and recommend products that consumers may like [1].

Plenty of eforts have been devoted to investigating diferent types of data, e.g., consumers' profile, online reviews, product descriptions, and social network to enhance recommendations [12,33,36,48], whereas images have not been comprehensively utilized yet because of the complexity of image processing and the dificulty of integrating images into recommendations. However, over the past few years, the advancement of deep learning techniques has made it possible to have a deeper understanding of multimedia content, in which some studies attempt to extract valuable information from visual data through deep neural networks [14,27,51].

For online consumers, their first impressions are usually derived from the visual appeal of products [23]. The perceptual and persuasive advantages of images have been well demonstrated in consumer behavior research [43]. Product images provide us with visual cues, reduce perceived risk, possess high attention-grabbing qualities and are remembered better [9,54]. Furthermore, when consumers make purchase decisions online, they naturally consider multiple sources of information together, e.g., images, descriptions, and reviews, meaning that they take a multi-view perspective.

Concerning visual and textual content, prior studies have found that visual messages are complements, but not alternatives to textual content [31]. For instance, a dress may have a description like “floral printed, round neck, long sleeve, two-side pockets”. Though helpful, the description does not provide details of floral pattern and where exactly the pockets are located, which a consumer prefers to know. Meanwhile, an image could clearly show the relevant information to fill the in formation gap, which is particularly desirable for online shoppers targeting experience goods, such as clothes. However, some features (e.g., fabrics) can only be accurately described in text and are unlikely to be inferred from images. Therefore, it is deemed intuitive and meaningful to combine image and textual content from such a multi-view per spective to efectively enhance the quality of recommendations.

Apart from the information heterogeneity caused by images and texts, there is also heterogeneity in consumers due to their diferences in cognitive styles. Cognitive style refers to the way people think, perceive and memorize information, which significantly influences people's behavior and decision-making process [29,49]. There are some studies discussing the cognitive style model, of which the Verbal-Imagery dimension in Cognitive Style Analysis in [45] is most closely related to our research. The Verbal-Imagery dimension describes individual's mode of information representation in memory during thinking. Concretely, afective users are more sensitive to visual content, while cognitive users are more sensitive to verbal clues [50]. Multi-view-based recommendation is expected to improve further by incorporating cognitive style heterogeneity and information heterogeneity.

Leveraging the heterogeneities in product content and users (users and consumers are used interchangeably in the following content) in recommender system design involves a twofold challenge. First, the heterogeneity in product content requires diferent modeling techniques to ensure an appropriate representation for each view of content, and the heterogeneity in users requires reflecting diferent attentive preferences of users on the respective content. Second, an overall mechanism needs to be developed to formulate a unified representation that embraces various representations for the respective content with users' diversified cognition styles. Note that, although some attempts have discussed the complementary relationship between visual and textual views in a general manner [31], the challenge has not be adequately addressed, which motivates our work.

This paper proposes a multi-view recommendation model, namely, Deep Multi-view Information iNtEgration (Deep-MINE), where visual and textual content are leveraged with representation learning techniques and mapped into a unified latent space. Furthermore, a cognition factor is introduced to characterize the heterogeneity in users' cognitive styles. Then, the embedding approach is deployed to automatically learn the interaction between visual and textual content enhanced with individualized cognitive styles. The efectiveness of Deep-MINE is verified through extensive experiments. It is also worth mentioning that, Deep-MINE shows merit in dealing with the cold-start problem to some extent by taking a comprehensive multi-view perspective.

The rest of the paper is organized as follows. Section 2 reviews the related literature. Section 3 presents the model framework and formulation, as well as the parameter learning process and recommendation procedure. The data experiments in Section 4 demonstrate the outperformance of the proposed model over baselines. The conclusion and future work are presented in Section 5.

## 2. Related work

## 2.1. Recommender systems

Generally, recommendation models can be grouped into three categories: content-based models, collaborative filtering (CF) and hybrid models [1]. Content-based models recommend items similar to those users have liked previously based on item or user characteristics. CF models recommend items according to the similarities among users or items. Matrix factorization (MF) [24] is an efective CF-based method. MF decomposes the feedback matrix into two low-dimension matrices, i.e., the item latent factor matrix and user latent factor matrix, and the interaction between the two matrices represents the preference score. However, it sufers from the cold start problem, as the latent factors can hardly be inferred, if there is no historical feedback available. Hybrid models that combine the two methods above have been widely used, which consider content information as well as collaborative preferences. The content information includes the user profile, item descriptions, social relations and social network [12,33,36,48]. As an important source of user-generated content, review texts are also utilized to elicit user preferences. For instance, HFT proposes to combine latent rating dimensions with latent review topics learned by topic models to make latent factors more interpretable [38]. CTR recommends scientific articles with similar ideas in online researcher communities [52]. Liu et al. [32] extract consumer opinions from reviews with aspect-based opinion mining and make recommendations based on extracted opinions.

Targeting recommendation objectives, recommender systems could be divided into point-wise recommendation and pairwise recommendation. Point-wise recommendation was widely used in the early days such as for movie recommendations, aiming to predict the rating or score for each user-item pair. By contrast, pairwise recommendation aims to optimize the ranking for potential candidates rather than focusing on the absolute rating scores, which is more realistic. One of the most influential studies is the work by Rendle et al. [44], which proposes a generalized Bayesian Personalized Ranking (BPR) framework and has been widely applied in top-n recommendation [58], session based recommendation [17], group-based recommendation [42] and point-of-interest recommendation [8].

However, existing eforts did not satisfactorily incorporate visual information, such as images. Furthermore, owing to the complexity of image processing, how to organically integrate images with other information to facilitate recommendation needs to be explored.

## 2.2. Image-aware recommendation

As mentioned earlier, images are influential and necessary in consumer decision-making on e-commerce platforms. There are some studies that apply visual signals to item recommendations in the field of computer science. In the early days, image-based recommendations mainly focus on image retrieval with feature engineering [5,21,35]. Considering the wide acceptance of deep learning in industrial and academic fields, some studies manage to leverage deep learning techniques to take advantage of image and textual information in recommendation models [57]. Wang et al. [53] prove that deep learningbased models outperform traditional topic-based models. Some representative models include VBPR [15], VPOI [55] and CKE [56]. VBPR represents each image with a 4096-dimension feature vector, which is extracted from a pre-trained image classification model [26] and adds an embedding layer on top of it to obtain a dense item representation. Similarly, Wang et al. [55] proposes a POI recommendation model that utilizes a pre-trained VGG-16 model. Nevertheless, due to the diferences of image contexts, a pre-trained model in a general-purpose image classification task may not well fit specific recommendation tasks. Moreover, there is usually a lack of well-recognized and predefined labels for images, therefore supervised models are not applicable either.

There are also some customized deep neural networks for imageaware recommendations. Lei et al. [28] propose a dual-net deep network to map the images and preferences of users into the same latent semantic space. Deepstyle [34] considers style features as well as category information of item to fully account for visual signals. CKE [56] proposes a collaborative knowledge embedding model that leverages image, text and structural information in a single Bayesian model. Visual embedding and textual embedding are implemented through two auto-encoder structures, i.e., stacked convolutional auto-encoder (SCAE) and stacked denoising auto-encoder (SDAE). However, the relationship between diferent types of knowledge is not well addressed, and the textual content originates from external knowledge bases, which is generally inaccessible for the online shopping recommendation context. In addition, some conceptual multi-view frameworks are highlighted in consumer behavioral and psychological research [20,30,31], which however lack technical treatments.

## 2.3. Representation learning

Representation learning is an efective tool that has been widely used in machine learning. The key idea of representation learning is to seek a low-dimensional embedding of data while preserving diferent discriminative factors of variation behind data. Several kinds of neural networks have been proposed to extract features from unstructured data, including undirected models such as the Deep Bayesian network (DBN) [18], Restricted Boltzmann Machine (RBM) [47], and directed models, such as the auto-encoder [4]. A stacked auto-encoder [41] is a kind of unsupervised model with multiple layers of auto-encoders in which the output of each layer is wired to the input of the successive layer. Aiming to reconstruct the original input as well as to compress the original high dimension input, it is composed of encoder and decoder parts. To constrain the representation from duplicating the input, auto-encoders are usually regularized and several variants of auto-encoders are proposed, including Contractive Auto-encoders (CAE) and Denoising Auto-encoder (DAE) [53,56]. For images, the Convolutional Neural Network (CNN) shows considerable advantages as it preserves the input's neighborhood relations and spatial locality in their latent higher-level feature representations [27]. Thus the convolutional stacked auto-encoder is a natural choice for image feature representation in this study.

The embedding approach is also widely adopted for information representation. To overcome the adaptation problem, an embedding layer is usually imposed on top of features extracted from pre-trained deep learning models to obtain a dense feature representation [15,55]. Based on previous achievements, this study adopts the auto-encoder structure to obtain a latent representation for each view of information and designs an embedding approach to exploring the interaction of multi-view features.

## 2.4. Cognitive styles

In the research field of psychology and education, a variety of research studies have discussed the constructs, theories and models related to cognitive styles [25]. Messick [40] defines cognitive style as stable attitudes, preferences or habitual strategies that determine in dividuals' modes of perceiving, remembering, thinking, and problem solving. Cognitive style has been widely applied in personnel selection, career guidance, task design, team composition, and conflict management [2,6]. Nevertheless, to our knowledge, few studies consider users diferent cognitive styles on an e-commerce platform.

According to Riding and Cheema [45], an individual's cognitive style can be positioned on two orthogonal dimensions, namely, Wholist-Analytic and Verbal-Imagery. The Verbal-Imagery dimension describes individuals' mode of information representation in memory. Verbalizers are those who tend to process information in words, and they learn better from textual input, while visualizers learn better from pictorial presentation [46]. A user's position on this dimension is of critical importance in deciding the relative weights of image and textual content in online purchase decisions.

Previous measurements of cognitive styles mainly focus on self-re port measures, which may not be efective in certain cases due to the questionable reliability and validity [10]. Furthermore, on a real online-shopping platform, hundreds of thousands of consumers browse product information, make purchase decisions and write product reviews from time to time. Hence, from an operational point of view, it is extremely dificult to explicitly assess these consumers' cognitive styles through the traditional measurement of cognitive style. In response to the call for utilizing multiple methods [3] and based on the similar idea in [13] where online user's cognitive styles are inferred in a Bayesian learning process through each user's clickstream data, this paper proposes a data-driven measurement to learn an individual's cognitive style through observations of a consumer's historical purchase behavior. Furthermore, the extracted individualized cognitive styles are incorporated to facilitate personalized recommendations, which con tributes to the field of recommender systems.

## 3. Model framework and computational methods

## 3.1. Problem formulation

Focusing on recommendation in the online shopping setting, in a multi-view information context, let J be the set of all items concerned; for each item j, it has at least one image $M _ { j } ,$ a description $D _ { j } ,$ and a set of reviews $R _ { j 1 } , R _ { j 2 } , \ldots , R _ { j m } .$ Let I be the set of all users; for each specific user i, his/her purchase history is known, and all users' purchase histories constitute an adjacency matrix $X ,$ in which $X _ { i j } = 1$ means that user i purchased item j, and $X _ { i j } = 0$ otherwise.

Generally, a user purchase can be treated as a kind of implicit feedback [19], as it indirectly reflects the user's preference. Without loss of generality, assume user i bought item j instead of item j $( j , j ^ { ' } \in J ) ;$ then user i implicitly prefers j to j<sup>′</sup>, denoted as $j > j ^ { ' }$ [15]. Consistently with [44], item pairs are used as training data in this paper. More specifically, suppose that for user i, the set of all the items he/she bought is denoted as ${ J _ { i } } ^ { + } ~ ( { J _ { i } } ^ { + } ~ \subset J )$ , the data set can be formalized as $S = \{ ( i , j , j ^ { ' } ) \vert j \in J _ { i } ^ { \enspace + } , \quad \bar { j ^ { ' } } \in J - J _ { i } ^ { \enspace + } \}$ , or equally, ${ \cal { S } } = \{ ( i , j , j ^ { ' } ) \vert X _ { i j } = 1$ $X _ { i j ^ { \prime } } = 0 \}$ . Therefore, the recommendation task is to derive a personalized list for each user based on those items which he/she has not provided any feedback.

## 3.2. Deep-MINE model

The overall model of Deep MINE consists of three parts: information representation, cognition layer and information integration. The model framework is as shown in Fig. 1.

## 3.2.1. Multi-view information representation

This subsection aims to map heterogeneous information into a unified latent space, in which a latent factor representing the source information is obtained through a deep neural network.

For images, a 6-layer stacked convolutional auto-encoder network [37] is designed. On the one hand, convolutional networks could preserve the input's neighborhood relations and spatial locality in their latent higher-level feature representations and show a superior performance in image classification related tasks [14,51]. On the other hand, the auto-encoder structure could preserve as much discriminative information as possible. For unstructured texts, a bag-of-word representation for each item is obtained and a 4-layer stacked auto-encoder network is designed to obtain its latent representation through layer-wise dimension reduction [41,53]. The number of layers for the auto-encoder networks is consistent with previous literature [53,56], and some empirical results for diferent number of layers are discussed in Section 4.3.5. Fig. 2 and Fig. 3 show the two types of auto-encoder networks, and the generation process of latent representations is detailed as follows.

For stacked convolutional auto-encoder, layers 1, 2, 5, and 6 are convolutional layers and layers 3 and 4 are fully connected layers. Suppose that an input image of item j is denoted as $M _ { 0 } .$ For each layerl, let each column k of its weight parameters $W _ { l }$ follows a normal distribution, namely, ${ \sf W } _ { \mathrm { l k } } { \sim } { \mathrm { N } } ( 0 , { { \lambda _ { w } } ^ { - 1 } } I )$ , and let bias parameters $\mathsf { b } _ { \mathrm { 1 } } \sim \mathsf { N }$ ${ ( 0 , \lambda _ { b } } ^ { - 1 } I ) ,$ , where I refers to the identity matrix. $\mathrm { I f } l = 1 , 2 , 5 , 6 ;$ , then the output of each layer l depends on the convolution operation of the network parameters and output of the last layer, namely, $M _ { l } = \sigma ( W _ { l } * M _ { l - 1 } + b _ { l } )$ , where ∗ represents convolution operation. If $l = 3 , 4 ,$ then $M _ { l } = \sigma ( W _ { l } \cdot M _ { l - 1 } + b _ { l } )$ , where ∙ represents matrix multiplication. The middle layer output $M _ { 3 }$ is used as the visual feature representation for item j. As implied by the name auto-encoder, the input is reconstructed at the last layer. To summarize, the encoder network and decoder, sharing the same weight matrices, are represented as Eq. (1) Eq. (2), respectively.

![](/api/attachments/49YSUXA7/fulltext/images/dff5a5516a12860c43d7ccf5fb5c3fa058814acd9ed50b6a991b734941ebb41c.jpg)  
Fig. 1. Deep-MINE Model framework.

ENCODER

![](/api/attachments/49YSUXA7/fulltext/images/010ab1bfda4cb0eb62c57d92365c546179ff793d1944cdbb7e334615659f368e.jpg)  
Fig. 2. Stacked convolutional auto-encoder for images.

$$
M _ {3} = g _ {1} (M _ {0}, W, b) = \sigma (W _ {3} \bullet \sigma (W _ {2} * \sigma (W _ {1} * M _ {0} + b _ {1}) + b _ {2}) + b _ {3})\tag{1}
$$

$$
M _ {6} = g _ {1} ^ {\prime} (M _ {3}, W, b) = \sigma (W _ {1} ^ {\prime} * \sigma (W _ {2} ^ {\prime} * \sigma (W _ {3} ^ {\prime} \bullet M _ {3} + b _ {4}) + b _ {5}) + b _ {6})\tag{2}
$$

For the stacked auto-encoder, suppose the textual description of item j is denoted as $D _ { 0 } .$ For each layer l, let each column k of its weight parameters $Q _ { l }$ follow a normal distribution, namely $\begin{array} { r } { \mathsf { Q } _ { \mathsf { l k } } { \sim } \mathbf { N } ( 0 , { \lambda _ { q } } ^ { - 1 } I ) , } \end{array}$ and let bias parameters $\mathsf { c } _ { 1 } { \sim } \mathsf { N } ( 0 , { \lambda _ { c } } ^ { - 1 } I )$ , where I is the identity matrix. The output of each layer l depends on the weight matrix, bias parameters and the output of the last layer, namely, $D _ { l } = \sigma ( Q _ { l } { \cdot } D _ { l - 1 } + c _ { l } )$ . The middle layer output $D _ { 2 }$ is used as the texual representation for item $j .$ Therefore, the encoder network and the decoder are represented as Eq. (3) and Eq. (4), respectively.

![](/api/attachments/49YSUXA7/fulltext/images/a05f7cb366e4610fdf3aeb2c7cf0fa5328c9056c8c151e60270cee3128fa6c5c.jpg)  
Fig. 3. Stacked auto-encoder for texts.

$$
D _ {2} = g _ {2} (D _ {0}, Q, c) = \sigma \left(Q _ {2} \bullet \sigma (Q _ {1} \bullet D _ {0} + c _ {1}) + c _ {2}\right)\tag{3}
$$

$$
D _ {4} = g _ {2} ^ {\prime} (D _ {2}, Q, c) = \sigma (Q _ {1} ^ {\prime} \bullet \sigma (Q _ {2} ^ {\prime} \bullet D _ {2} + c _ {3}) + c _ {4})\tag{4}
$$

Note that, as reviews are also textual, a similar 4-layer stacked autoencoder is built for $R _ { 0 }$ as that for $D _ { 0 } ,$ with $R _ { 2 } = g _ { 3 } ( R _ { 0 } , N , t ) ,$ $R _ { 4 } = g _ { 3 } \ ' ( R _ { 2 } , N , t ) .$ . Furthermore, to ensure that we obtain an efective representation for each view of information, the Mean Square Error (MSE) loss functions L1, L2, L3 are introduced with the aim of minimizing the reconstruction error, and regularization terms are also added to control the magnitude of the network parameters (i.e., Eq. (5)–(7)), where $\lambda _ { m } , \lambda _ { d } , \lambda _ { r }$ are hyperparameters and $\lambda _ { w } , \lambda _ { b } , \lambda _ { q } , \lambda _ { c } , \lambda _ { n } , \lambda _ { t }$ are parameters of the corresponding normal distributions.

$$
\min L _ {1} = \frac {\lambda_ {m}}{2} \sum_ {j} | | M _ {L} - M _ {0} | | _ {2} ^ {2} + \frac {\lambda_ {w}}{2} \sum_ {l} | | W _ {l} | | _ {2} ^ {2} + \frac {\lambda_ {\mathrm{b}}}{2} \sum_ {l} | | b _ {l} | | _ {2} ^ {2}\tag{5}
$$

$$
\min L _ {2} = \frac {\lambda_ {d}}{2} \sum_ {j} | | D _ {L} - D _ {0} | | _ {2} ^ {2} + \frac {\lambda_ {q}}{2} \sum_ {1} | | Q _ {l} | | _ {2} ^ {2} + \frac {\lambda_ {\mathrm{c}}}{2} \sum_ {1} | | c _ {l} | | _ {2} ^ {2}\tag{6}
$$

$$
\min L _ {3} = \frac {\lambda_ {r}}{2} \sum_ {j} | | R _ {L} - R _ {0} | | _ {2} ^ {2} + \frac {\lambda_ {n}}{2} \sum_ {1} | | N _ {l} | | _ {2} ^ {2} + \frac {\lambda_ {t}}{2} \sum_ {1} | | t _ {l} | | _ {2} ^ {2}\tag{7}
$$

## 3.2.2. Cognition layer

As mentioned above, according to the Verbal-Imagery dimension of cognitive style, users are heterogeneous in information processing, implying that some users may value images more, while others may pay more attention to texts. In [10], cognitive style is obtained from lab experiments where participants are asked to complete a survey on certain tasks. In a real online shopping environment, however, the consumers are usually in hundreds of thousands, i.e., it is extremely dificult to explicitly assess their cognitive styles through the above methods. Therefore, we propose an integrated model to learn their cognitive styles in a data-driven fashion from users' implicit feedback. i.e., purchase information. In this spirit, a cognition layer is added in the Deep-MINE model architecture. Specifically, a 3-dimension vector is imposed on three diferent views, i.e., images, descriptions and reviews, to represent an individual's cognitive style, which is a reasonable ex tension on Verbal-Imagery dimension, where a textual description is separated from a textual review, because they are quite diferent in terms of the content, position and form of presentation in the e-com merce context.

Concretely, user i<sup>′</sup>s cognition factor is denoted as $[ a _ { i 1 } , a _ { i 2 } , a _ { i 3 } ]$ . From Section 3.2.1, as the latent representations for the three types of information are denoted as $M _ { 3 } , D _ { 2 } , R _ { 2 } ,$ the perceived information for user i is moderated as $[ { a _ { i 1 } \cdot M _ { 3 } } , { a _ { i 2 } \cdot D _ { 2 } } , { a _ { i 3 } \cdot R _ { 2 } } ]$ . The value of the cognition factor is to be learned during the model training phase.

## 3.2.3. Multi-view information integration

With user perceived information available, an integration module is proposed to build a full picture of an item from a multi-view perspective. First, a stacking layer (concatenation) of diferent representations is formulated as Eq. (8), where c(.) represents the concatenation. Then, an embedding layer is deployed to transform the concatenated factor into a lower dimension factor as Eq. (9).

$$
\mathrm{f} ^ {\mathrm{c}} = c \left(a _ {i 1} \bullet M _ {3}, a _ {i 2} \bullet D _ {2}, a _ {i 3} \bullet R _ {2}\right)\tag{8}
$$

$$
\mathbf {f} _ {\mathrm{j}} = W _ {f u} \bullet \mathbf {f} ^ {\mathrm{c}}\tag{9}
$$

Notably, this embedding operation is deemed to be a key step to enable reorganizing and utilizing available information in the following steps [15]. Similar to the cognition factor, the specific weights in $W _ { f u }$ are not known to us beforehand and need to be learned in the model training phase, which is natural, as the integration mechanism is highly dependent on the specific context. So far, f can be deemed as content factor, as all three pieces of information have been integrated together.

Apart from images, descriptions and reviews, there may exist ad ditional information about the item outside the e-commerce platform, which could potentially afect the consumer purchase behavior. Therefore, factor $\mathbf { v } _ { \mathrm { j } }$ is introduced to capture the hidden information. Eventually, the aggregated item factor item consisting of hidden in formation and content factor is deemed to represent the item comprehensively, which is shown in Eq. (10)

$$
i t e m _ {j} = c \left(\mathrm{v} _ {\mathrm{j}}, \mathrm{f} _ {\mathrm{j}}\right).\tag{10}
$$

## 3.2.4. User preference

Based on previous discussions, for recommendation purposes, the preference $x _ { i j }$ of user i on item j can be formulated as Eq. (11), where v and $f _ { j }$ represent the hidden information and content factor of an item as introduced above, $u _ { i }$ and $\theta _ { i }$ are the user perception factors corre sponding to v and $f _ { j } ,$ and $\alpha _ { i }$ and $\beta _ { j }$ denote user bias and item bias, respectively:

$$
x _ {i j} = \alpha_ {i} + \beta_ {j} + u _ {i} ^ {T} v _ {j} + \theta_ {i} ^ {T} f _ {j}.\tag{11}
$$

To combine all the parts above, the preference of user i on item j could be formulated as Eq. (12). Consistently with [44], the probability of user i preferring item j to item j<sup>′</sup> can be formulated with a sigmoid function as Eq. (13)

$$
x _ {i j} = \alpha_ {i} + \beta_ {j} + u _ {i} ^ {T} v _ {j} + \theta_ {i} ^ {T} (W _ {f u} \bullet c (a _ {i 1} \bullet M _ {3}, a _ {i 2} \bullet D _ {2}, a _ {i 3} \bullet R _ {2}))
$$

$$
P (j > _ {i} j ^ {\prime}) = \sigma (x _ {i j} - x _ {i j ^ {\prime}}) = 1 / (1 + \exp (- (x _ {i j} - x _ {i j ^ {\prime}}))).\tag{12}
$$

(13)

## 3.2.5. Objective function

To optimize the whole model and learn the model parameters, an objective function is formulated in this subsection. As Deep-MINE has two major parts, namely, representation learning and preference learning, the objective function performs two tasks. One task is to maximize the logarithm of the ranking probability, i.e., $\textstyle \sum _ { ( i , j , j ^ { \prime } ) \in S } l n \sigma ( x _ { i j } - x _ { i j ^ { \prime } } )$ . The other task is to obtain an efective information representation. Hence the loss functions of the auto-encoder networks, $\mathrm { i } . \mathrm { e } . , L _ { 1 } + L _ { 2 } + L _ { 3 }$ , in information representation layer need to be included. In addition, regularization terms for related model parameters are added to avoid overfitting. Overall, the objective function can be formulated as Eq. (14), where S is the training set consisting of triple $( i , j , j )$ as explained in Section 3.1. $\lambda _ { m } , \lambda _ { d } , \lambda _ { r } , \lambda _ { \theta } , \lambda _ { \beta } , \lambda _ { W _ { \hbar } }$ are hy perparameters controlling the relative weights of diferent components in the objective function:

$$
\begin{array}{l} \text {ax} \mathscr {L} (W, b, Q, c, N, t, \beta , u, v, \theta , a, W _ {f u}) = \sum_ {(i, j ^ {\prime}) \in S} l n \sigma (x _ {i j} - x _ {i j ^ {\prime}}) \\ - \frac {\lambda_ {m}}{2} \sum_ {j} | | M _ {L} - M _ {0} | | _ {2} ^ {2} \\ - \frac {\lambda_ {d}}{2} \sum_ {j} | | D _ {L} - D _ {0} | | _ {2} ^ {2} - \frac {\lambda_ {r}}{2} \sum_ {j} | | R _ {L} - R _ {0} | | _ {2} ^ {2} \\ - \frac {\lambda_ {\theta}}{2} \sum_ {i} | | u _ {i} | | _ {2} ^ {2} - \frac {\lambda_ {\theta}}{2} \sum_ {j} | | v _ {j} | | _ {2} ^ {2} \\ - \frac {\lambda_ {\theta}}{2} \sum_ {i} | | \theta_ {i} | | _ {2} ^ {2} - \frac {\lambda_ {\beta}}{2} \sum_ {i} | | \beta_ {i} | | _ {2} ^ {2} \\ - \frac {\lambda_ {W _ {f u}}}{2} | | W _ {f u} | | _ {2} ^ {2} \\ - \left(\frac {\lambda_ {w}}{2} \sum_ {1} | | W _ {l} | | _ {2} ^ {2} + \frac {\lambda_ {\mathrm{b}}}{2} \sum_ {1} | | b _ {l} | | _ {2} ^ {2}\right) \\ - \left(\frac {\lambda_ {q}}{2} \sum_ {1} | | Q _ {l} | | _ {2} ^ {2} + \frac {\lambda_ {\mathrm{c}}}{2} \sum_ {1} | | c _ {l} | | _ {2} ^ {2}\right) \\ - \left(\frac {\lambda_ {\mathrm{n}}}{2} \sum_ {1} | | N _ {l} | | _ {2} ^ {2} + \frac {\lambda_ {\mathrm{t}}}{2} \sum_ {1} | | t _ {l} | | _ {2} ^ {2}\right). \end{array} \tag {14}
$$

Considering the complexity and nonlinear relationships of parameters, it is impossible to find a closed form solution [56]. An iterative algorithm is developed, as discussed in the next subsection.

## 3.3. Parameter learning

As the objective function is based on pairwise items, for each user, there are many more items for which he/she has not provided any feedback (i.e., purchase) than those that he/she has purchased. Therefore, a negative sampling strategy [56] is adopted to randomly sample one item pair from the training set S each time and update the corresponding parameters with stochastic gradient descent.

To obtain the gradient with respect to each parameter, back propagation is used during each update. The update formulas for the parameters are shown in Eqs. $( 1 5 ) \substack { - ( 2 2 ) }$ , where $x _ { i j j ^ { \prime } } = - \ ( x _ { i j } - x _ { i j } )$ , lr denotes the learning rate, t denotes the batch number. $\frac { \partial f ( a _ { i 1 } \bullet M _ { 3 } , a _ { i 2 } \bullet D _ { 2 } , a _ { i 3 } \bullet R _ { 2 } ) } { \partial ( a _ { i 1 } \bullet M _ { 3 } ) }$ is a sparse matrix with the first n rows being an identity matrix and the remaining $m + k$ rows being zeros, where n, m, k are the latent factor dimensions of images, descriptions and reviews. Both $\frac { \partial g _ { 1 } ( M _ { 0 } , W , b ) } { \bar { \partial } W _ { l } }$ and $\frac { \partial ( g _ { 1 } ^ { \prime } ( g _ { 1 } ( M _ { 0 } , W , b ) ) } { \partial W _ { l } }$ can be directly derived with back propagation, which are not expanded here for simplicity. The update formulas for $N , Q , c ,$ t are omitted, as they could be derived in a similar fashion as W, b. The algorithmic details of parameter learning process

are provided in Algorithm 1

$$
\beta_ {i} ^ {t + 1} = \beta_ {i} ^ {t} + l r \bullet (\sigma (x _ {i j j ^ {\prime}}))\tag{15}
$$

$$
\theta_ {i} ^ {t + 1} = \theta_ {i} ^ {t} + l r \bullet (\sigma (x _ {i j j ^ {\prime}}) W _ {f u} ^ {t} (f _ {j} ^ {c} - f _ {j ^ {\prime}} ^ {c}) - \lambda_ {\theta} \theta_ {i} ^ {t})\tag{16}
$$

$$
v _ {j} ^ {t + 1} = v _ {j} ^ {t} + l r \bullet (\sigma (x _ {i j j ^ {\prime}}) \bullet u _ {i} ^ {t} - \lambda_ {\theta} v _ {j} ^ {t})\tag{17}
$$

$$
u _ {i} ^ {t + 1} = u _ {i} ^ {t} + l r \bullet (\sigma (x _ {i j j ^ {\prime}}) \bullet (v _ {j} ^ {t} - v _ {j ^ {\prime}} ^ {t}) - \lambda_ {\theta} u _ {i} ^ {t})\tag{18}
$$

$$
W _ {f u} ^ {t + 1} = W _ {f u} ^ {t} + l r \bullet (\sigma (x _ {i j j ^ {\prime}}) \bullet \theta_ {i} ^ {t} \bullet (f _ {j} ^ {c T} - f _ {j ^ {\prime}} ^ {c T}) - \lambda_ {W _ {f u}} W _ {f u} ^ {t})\tag{19}
$$

$$
a _ {i 1} ^ {t + 1} = a _ {i 1} ^ {t} + l r \cdot \sigma (x _ {i j j ^ {\prime}}) \cdot \theta_ {i} ^ {t} \cdot W _ {f u} ^ {t} \cdot \frac {\partial f (a _ {i 1} \cdot M _ {3} , a _ {i 2} \cdot D _ {2} , a _ {i 3} \cdot R _ {2})}{\partial (a _ {i 1} \cdot M _ {3})} \cdot g _ {1} (M _ {0}, W, b)\tag{20}
$$

$$
\begin{array}{l}W _ {l} ^ {t + 1} = W _ {l} ^ {t} + l r \bullet (\sigma (x _ {i j j ^ {\prime}}) \bullet (\theta_ {i} ^ {t}) ^ {T} \bullet W _ {f u} ^ {t} \bullet \frac {\partial f (a _ {i 1} \bullet M _ {3} , a _ {i 2} \bullet D _ {2} , a _ {i 3} \bullet R _ {2})}{\partial (a _ {i 1} \bullet M _ {3})} \bullet a _ {i 1} ^ {t}\\\qquad \bullet \left(\frac {\partial g _ {1} (M _ {0} , W , b)}{\partial W _ {l}} - \frac {\partial g _ {1} (M _ {j ^ {\prime} 0} , W , b)}{\partial W _ {l}}\right)\\\qquad - \lambda_ {m} (M _ {6} - M _ {0}) \frac {\partial g _ {1} ^ {\prime} (g _ {1} (M _ {0} , W , b))}{\partial W _ {l}} - \lambda_ {w} \bullet W _ {l} ^ {t}\left. \right)\end{array}\tag{21}
$$

$$
\begin{array}{l} b _ {l} ^ {t + 1} = b _ {l} ^ {t} + l r \cdot \Bigg (\sigma (x _ {i j j ^ {\prime}}) \cdot (\theta_ {i} ^ {t}) ^ {T} \cdot W _ {f u} ^ {t} \cdot \frac {\partial f (a _ {i 1} \cdot M _ {3} , a _ {i 2} \cdot D _ {2} , a _ {i 3} \cdot R _ {2})}{\partial (a _ {i 1} \cdot M _ {3})} \cdot a _ {i 1} ^ {t} \\ \qquad \cdot \bigg (\frac {\partial g _ {1} (M _ {0} , W , b)}{\partial b _ {l}} - \frac {\partial g _ {1} (M _ {j ^ {\prime} 0} , W , b)}{\partial b _ {l}} \bigg) \\ \qquad - \lambda_ {m} (M _ {6} - M _ {0}) \frac {\partial g _ {1} ^ {'} (g _ {1} (M _ {0} , W , b))}{\partial b _ {l}} - \lambda_ {b} \cdot b _ {l} ^ {t} \bigg). \end{array}\tag{22}
$$

Algorithm 1. Deep-MINE parameter learning.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: S, I, J, M, D, R
Output: W, b, Q, c, N, t,  $\beta$ , u, v,  $\theta$ , a,  $W_{fu}$ 
Initialize the parameters W, b, Q, c, N, t,  $\beta$ , u, v,  $\theta$ , a,  $W_{fu}$ 
WHILE epoch &lt;= training_epoch
WHILE batch &lt;= total_batch
a) Randomly choose an item pair (i,j,j') from S.
b) Extract corresponding images, descriptions and review texts of j and j' as  $M_{0}, D_{0}, R_{0}$  and  $M_{j0}, D_{j0}, R_{j0}$ 
c) Forward phase:
i. Forward the input through the information representation module and generate visual and textual features  $M_{3} = g_{1}(M_{0}, W, b), D_{2} = g_{2}(D_{0}, Q, c), R_{2} = g_{3}(R_{0}, N, t)$ .
ii. Forward the features through the user cognition layer and obtain perceived information  $a_{i1} \cdot M_{3}, a_{i2} \cdot D_{2}, a_{i3} \cdot R_{2}$ 
iii. Forward through the information integration module and obtain the item factor  $item_{j} = c(v_{j}, W_{fu} \cdot c(a_{i1} \cdot M_{3}, a_{i2} \cdot D_{2}, a_{i3} \cdot R_{2}))$ 
iv. Calculate the user preference score and probability
 $x_{ij} = \alpha_{i} + \beta_{j} + u_{i} v_{j} + \theta_{i} f_{j}$ $x_{ij'} = \alpha_{i} + \beta_{j'} + u_{i} v_{j'} + \theta_{i} f_{j'}$ $P(j &gt; _{i} j') = \sigma(x_{ij} - x_{ij'})$ 
d) Backward phase:
i. Obtain the objective function  $\mathcal{L}(W, b, Q, c, N, t, \beta, u, v, \theta, a, W_{fu})$  as Eq. (14)
ii. Calculate gradients and update parameters using Eqs. (15)-(22).
END WHILE
IF  $|L_{epoch} - L_{epoch-1}| &lt; \delta$ , THEN
BREAK
END IF
END WHILE
</div>

## 3.4. Prediction and recommendation

An online recommendation for user i can be conducted as follows. For each item j, following the Deep-MINE framework, given its content information and user characteristics, the preference $x _ { i j }$ could be assessed using Eq. (12). Then, a sorting operation is performed for x s, and the top K items that constitute the recommendation list are se lected. The framework is illustrated in Fig. 4.

## 4. Empirical study and results

## 4.1. Data description

To demonstrate the efectiveness of the proposed model, two categories of real-world datasets were obtained from Amazon.com, namely, Women's Dresses and Baby Clothes. Both Women's Dresses and Baby Clothes are typical experience goods, for which images and reviews are well recognized to be highly informative, complementing the product descriptions for consumer decision-making. For the Baby Clothes dataset, only image features are available (http://jmcauley.ucsd.edu/ data/amazon/) [16,39]. Thus, the image auto-encoder network is applied to the Women's Dresses dataset.

The data preprocessing is conducted as follows. As a product usually had 3–4 images to show it from diferent angles, without loss of generality, one image was randomly chosen as the input. For textual content, a bag-of-words approach was used and words with high frequency were kept in the vocabulary. To control the dimension of the input data and prevent the negative impact of misspelled words or typos, words that appeared less than 10 times were deleted for the Women's Dresses dataset and words that appeared less than 100 times were deleted for the Baby Clothes dataset (the corpus of the Baby Clothes dataset is much larger than that of the Women's Clothes dataset, which explains the diferent thresholds), which is consistent with [52,53]. A stop words list was also kept to delete words, such as $o f$ and in. The text preprocessing steps included capital words conversion, word stemming and stop words deletion. Finally, 1461 and 1894 words were retained for the descriptions and reviews in the Women's Dresses dataset. 1516 and 1502 words were retained for the Baby Clothes dataset. Note that, most consumers would not read all of the reviews and reviews with helpful votes were usually displayed with priority by the platform. Hence, we only kept the reviews with helpful votes for preprocessing. An example of product content is presented in Table 1.

For both datasets, we ensured that each consumer had at least two feedbacks, $\mathrm { i . e . , }$ one for the training set and one for the test set, as the proposed model needs to infer consumer preferences from one's purchase history. All products were kept in the dataset, including products that had few or no feedbacks (i.e., new products released to the market), which are known as cold start products. Initially, the Women's Dresses dataset had 256,749 feedbacks and the Baby Clothes dataset had 32,419 feedbacks. After data cleaning and preprocessing, we finally had 5981 users and 2579 products for the Women's Dresses dataset and 8018 users and 3625 products for the Baby Clothes dataset.

For each user, one feedback was randomly chosen for the test set, and the other feedbacks were chosen for the training set [15,56]. Furthermore, to demonstrate Deep-MINE's performance under cold start settings, cold start test sets including products with diferent sparsity levels were also extracted from the test set, which will be elaborated in Section 4.3.3.

## 4.2. Evaluation metrics and baseline models

Aligned with the prior literature, the Area Under the ROC Curve (AUC) [15,44] and Hit Ratio [58] were chosen as two metrics for performance evaluation. The AUC is defined as $\begin{array} { r } { A U C = \frac { 1 } { \mid I \mid } \sum _ { i } \frac { 1 } { \mid J \mid } \sum _ { ( i , j , j ^ { \prime } ) \in S } \delta ( x _ { i j } > x _ { i j ^ { \prime } } ) _ { ! } } \end{array}$ , and δ(∙) is an indicator function that equals 1, if $x _ { i j } > x _ { i j }$ is true; otherwise it is 0. The AUC measures the ratio of correctly predicted product pairs to the total product pairs for all consumers. S is defined in the formulation in Section 3.1. The hit ratio is also widely used in recommender system evaluation [57]. The hit ratio is measured as the percentage of users who have at least one correctly recommended product in the top-K recommendation list. A higher hit ratio reflects a higher recommendation accuracy. In the following experiments, diferent K values were tested to prove the robustness of the proposed model.

![](/api/attachments/49YSUXA7/fulltext/images/23d0972f5d1c80ee6cda441f85c50e97184b32eac3a0f8c1b4d396abc4064524.jpg)  
Fig. 4. Framework for Deep-MINE recommender system.

Table 1  
An example of product content.

<table><tr><td>Image</td><td>Description</td><td>Review</td></tr><tr><td><img src="/api/attachments/49YSUXA7/fulltext/images/3ee4bb3109b1ac09372a58b85e25668e73f4aef6ccaafc90d42d8092888042b9.jpg"/></td><td>95% Polyester 5% Spandex. Hand wash; dry flat; Model Wearing Size 1 × . Height: 5&#x27;9&quot; Waist:37.5&quot; Hips: 42&quot; Bust:34&quot; Super soft fabric defines this curve-loving dress, while a surplice neckline and billowing silhouette add gentle whimsy.</td><td>Looks just like Brigette Bailey and Lovestitch style but the material was really thin and did not drape as nicely. The multi blue color is attractive and the price was good but I&#x27;m spoiled on the other two brands. And will stick with those.</td></tr></table>

To show the superior performance of Deep-MINE, the following baseline models were chosen for comparison.

(1) BPRMF: The pairwise Bayesian Personalized Ranking model proposed in [44], which is a state-of-the-art ranking based model only utilizing implicit feedback data.

(2) CDL: The Collaborative Deep Learning model proposed in [53] processes description content with a stacked denoising auto-en coder based on the probabilistic matrix factorization framework.

(3) VBPR: The Visual Bayesian Personalized Ranking model proposed in [15], i.e., based on BPRMF, utilizes image features from pre trained image classification model.

(4) CKE: The Collaborative Knowledge Base Embedding model, i.e., an extension of CDL proposed in [56], incorporates structural, textual and visual content. As no structural information is available in our context, descriptions and images are considered here in implementation.

A validation set sampled from the training set was used to find the optimal hyperparameters for the Deep-MINE model and all the baseline models above. The hyperparameter settings of the Deep-MINE model are listed in Table 2. Based on the previous literature [56], the node numbers of the latent layer for images, descriptions and reviews were set the same, and experiments under diferent parameter settings were also conducted in Section 4.3.5 to justify the model's robustness.

## 4.3. Experiment results

## 4.3.1. Performance comparison of Deep-MINE and baseline models

Deep-MINE and baseline models were evaluated under diferent settings in this subsection. All the models were trained using the same strategy as introduced above. To make a fair comparison, the factor numbers of hidden information and integrated content were kept the same for Deep-MINE and baseline models. The AUC results are shown in Fig. 5. For the Women's Dresses dataset, the AUC of Deep-MINE was no less than 0.85, meaning that more than 85% of the pairwise rankings were predicted accurately. With total factor number increasing from 50 to 200, the Deep-MINE model consistently performed better than baseline models. BPRMF performed the worst as it utilized only the feedback data without considering content information. CKE had the second-best performance because it utilized more information compared with VBPR and CDL. Not surprisingly, VBPR had a slightly better performance than CDL as image features are more informative than descriptions for products, such as clothes.

To examine the robustness of Deep-MINE, experiments were also conducted on the Baby Clothes dataset (Fig. 5(b)). Deep-MINE still had a better performance than all the baselines. A notable diference was that VBPR also achieved a good performance with a slightly lower AUC than Deep-MINE (0.8025 vs 0.8030). On this dataset, as the visual input was a 4096-dimension feature vector instead of raw images, the design of image convolutional auto-encoder in the Deep-MINE model was deprecated. Still, the Deep-MINE performance was satisfactory, using the mechanism of multi-view information integration. However, the high-dimensional visual feature may have a dominant efect over the other two views, which may explain the relatively poor performance of

## Table 2

Hyperparameter settings.

<table><tr><td>Deep-MINE model</td><td>Hyperparameter setting</td></tr><tr><td>Image auto-encoder</td><td> $N_{m1} = 64, N_{m2} = 64, N_{m3} = 100,$  $\lambda_m = \frac{1}{\#img\_dim}$ </td></tr><tr><td>Description auto-encoder</td><td> $N_{d1} = 400, N_{d2} = 100, \lambda_d = \frac{1}{\#des\_dim}$ </td></tr><tr><td>Review auto-encoder</td><td> $N_{r1} = 400, N_{r2} = 100, \lambda_r = \frac{1}{\#rev\_dim}$ </td></tr><tr><td>Regularization and variance parameters</td><td> $\lambda_\theta = 0.1, \lambda_\beta = 0.001, \lambda_{W_{fu}} = 0.001,$  $\lambda_w = \frac{1}{\#W\_dim}, \lambda_q = \frac{1}{\#Q\_dim}, \lambda_n = \frac{1}{\#N\_dim},$  $\lambda_b = \lambda_t = \lambda_c = 0$ </td></tr></table>

Note: Nm , Nm , and Nm refer to the number of hidden units for layers 1, 2, and 3 in the image auto-encoder, respectively; img\_dim, des\_dim, and rev\_dim refer to the dimensions of image, description and review input, respectively; #W\_ dim , $\# Q _ { d i m s }$ and $\# N _ { d i m }$ refer to the dimensions of corresponding weight matrix W, Q, and N, respectively.

![](/api/attachments/49YSUXA7/fulltext/images/03e2ac37166bc69d747eb4e0d5858016770d465ebe6f163c2ff2351f6cd7efc7.jpg)  
(a) Women's Dresses

![](/api/attachments/49YSUXA7/fulltext/images/6728decc13c746a05bd4ec6611da2a308242e292bb48323a3fd61db5fd809259.jpg)  
(b) Baby Clothes  
Fig. 5. AUC comparison of our model and baseline models.

CDL and CKE. Consistently, BPRMF performed the worst in all the baselines. As the model performance was not sensitive to the factor number on both datasets, the factor number was fixed at 100 in the following experiments.

In addition to the AUC, the hit ratio is another metric that measures the ranking-based recommendation accuracy. When K varied from 50 to 200, the hit ratio was plotted in Fig. 6. On the Women's Dresses dataset, Deep-MINE beaten all the other baseline models and achieved a performance similar to that of CKE. On the Baby Clothes dataset, Deep-MINE performed the best across all K levels.

Through the above results, Deep-MINE revealed its efectiveness for integrating information in comparison with other content-aware recommendation models. In addition, Deep-MINE also showed a significant improvement over BPRMF, which signifies the considerable advantages of incorporating content information into recommendation models.

## 4.3.2. Efect of multi-view information integration

As mentioned previously, Deep-MINE can organically integrate multi-view information to enhance recommendations. Therefore, Deep-MINE (i.e., the entire model) was further examined with its degenerated forms (i.e., single models), where one view from only a single in formation source was considered, namely, Image-MINE, Description-MINE and Review-MINE. From Fig. 7 and Fig. 8, it is clear that the entire model performed better than single models on the AUC and hit ratio. Concretely, Review-MINE performed better than the other single models, which may signify that reviews contain more valuable in formation compared with information provided by e-retailers, such as images and descriptions. Image-MINE and Description-MINE had slightly diferent performances on the two datasets. On the Women's Dresses dataset, product images mattered more, while for the Baby

Clothes dataset, descriptions mattered more, possibly because baby clothes were more functional than women's dresses, and therefore, descriptions contained more relevant and decisive information for consumers. From an overall point of view, the proposed Deep-MINE model showed its advantage by organically integrating multi-view information. Furthermore, all the Deep-MINE related models performed significantly better than the BPRMF model.

## 4.3.3. Performance on cold start datasets

As Deep-MINE leverages multi-view content information to make recommendations, it is expected to sufer less in cold start product settings, i.e., products having no or few purchase feedbacks could hardly be recommended. To verify this, cold start test sets of diferent sparsity levels were extracted from the full test set. The “Sparsity Level = 1” group refers to cold start products that have no historical feedback in the training set and only appear once in the test set. The “Sparsity Level = 10” group refers to cold start products that have no more than 10 feedbacks in the dataset. All of the baseline models were tested, and results are listed in Table 3.

The results further demonstrate that through a better exploitation of visual and textual content, Deep-MINE outperformed all the baseline models with remarkable advantages. In particular, in the “Sparsity Level = 1” group, the AUC of Deep-MINE surpassed that of the best baseline model (i.e., CKE) by 30.13% (0.5001 vs 0.3843). As feedbacks for each product increased, the recommendation performances improved for all models. CKE performed the best in the baseline models as it takes account of various contents as well. As expected, BPRMF performed the worst as it only considers feedback data.

## 4.3.4. Efect of incorporating cognitive style

To further examine the impact of incorporating the heterogeneity in user cognitive styles and demonstrate the reliability of the cognitive style values obtained by Deep-MINE, we proposed a series of initial cognitive indexes as benchmark indexes and compared their recommendation performances with the Deep-MINE model. Higher re commendation performance could imply, to some extent, that the corresponding cognitive index configuration reflects a more accurate representation of the user's cognition characteristics.

![](/api/attachments/49YSUXA7/fulltext/images/a4d3bc6a7cca038cdc24b0db30400b501c812dd90d4500b3e8573b74ac6b3b33.jpg)  
(a) Women's Dresses

![](/api/attachments/49YSUXA7/fulltext/images/deee48db38433d9f428d7dbe2ad56f3dfdab0d29e593b92e246df8db5f0c5e51.jpg)  
(b) Baby Clothes  
Fig. 6. Hit ratio comparison of our model and baseline models.

![](/api/attachments/49YSUXA7/fulltext/images/544d6bba8b95146623a7081920d9a14151f68ef607a5e55f8eb4a21d7e2b679c.jpg)  
(a) Women's Dresses

![](/api/attachments/49YSUXA7/fulltext/images/62fa5cfc800bbf4694a8ca770fe3b2d4dddd029ef1c920d6cbf4b278b8f3c0ef.jpg)  
(b) Baby Clothes  
Fig. 7. AUC comparison of the entire model and single models (Factor No = 100)

The benchmark indexes include: (1) No cognitive styles. This con figuration represents that cognitive style information is not considered in the model and recommendation. (2) Uniform cognitive styles. Uniform cognitive styles assume the cognitive weights of all consumers on the three pieces of information, i.e., descriptions, reviews and images, are the same, which is [1/3, 1/3, 1/3]. This index assumes that not only the cognitive styles of all consumers are homogenous, but also the consumers' inclinations to the three diferent forms of information representations are indiferent. (3) Ordered cognitive styles. This index assumes all consumers have the same priority order on diferent in formation formats, i.e., with weight [3/6] being high priority, [2/6] being medium priority and [1/6] being low priority, thus generating 6 combinations of cognitive style indexes, e.g., [high-image, mediumdescription, low-review], [high-description, medium-review, low image], etc. (4) Random cognitive styles. A randomization could ensure that each consumer has a diferentiated cognition vector. This is a general treatment to represent consumer's cognition heterogeneity without further information. (5) Average cognitive styles. In this configuration, the cognitive style of each consumer is derived using our proposed model. Then the average cognitive style values across all consumers are calculated and used as the unified cognitive style.

The comparison results on the hit ratio and AUC are shown in Fig. 9(a) and (b), and clearly the proposed Deep-MINE showed the best performance. Further findings can also be derived. First, all the models equipped with cognitive styles significantly outperformed the model without cognitive styles, further emphasizing the power of integrating cognitive styles into personalized recommendation. Second, diferent cognitive style distributions on three information representations did significantly impact the recommendation performance, which demonstrates the importance of detecting appropriate cognitive styles of consumers. Third, the Deep-MINE model (which treats consumer's cognitive style in an individualized manner) outperformed other models only considering unified cognitive style across all consumers, showing the strength of cognitive style personalization. It is also worth mentioning that, though configuration (5) of Average Cognitive Style to a large extent incorporates the learnt cognitive styles of all consumers, the final performance was weakened due to the average treatment compared with the Deep-MINE model.

![](/api/attachments/49YSUXA7/fulltext/images/bc65c0b71238f4037e45b3489e97f2a4bb2fb6c9eccb223eb294ca80348d30fd.jpg)  
(a) Women's Dresses

To visualize the cognition values, an extracted sample of ten consumers' cognition value distributions from the Women's Dresses dataset is shown in Fig. 9(c), in which we observed that consumers 1 and 8 cared much more about images and reviews than descriptions; consumers 2, 3, 5 and 9 were more inclined to descriptions; consumer 6 valued reviews more; consumer 7 valued images more; and consumers 4 and 10 paid roughly equal attention to all three views. Such observations further confirm the prevalence of cognition heterogeneity, and highlight the significance of treating multiple information sources diferently for diferent types of consumers in recommendations. For instance, from the perspective of online shopping platform, platform managers could consider a personalized webpage layout design that is consistent with the consumer's individualized cognitive style to provide a better shopping experience, which is also supported by Engin and Vetschera [11].

## 4.3.5. Sensitivity analysis

As mentioned in Section 4.2, the node numbers of the latent layer for three auto-encoders were all set to 100. To further prove the robustness, we also conducted experiments by varying the latent node number for the image auto-encoder (Table 4). It was observed that the performance remained stable across diferent numbers, and more image nodes did not necessarily lead to a better performance, possibly because the learning process can ensure an efective representation and integration of all information through back propagation to minimize the objective function, regardless of the initial hyperparameter settings.

![](/api/attachments/49YSUXA7/fulltext/images/9577a1c5658ebff6f0dd2a8cd452ba416d5715a216a1ef0f173b97fb6b98d1ca.jpg)  
(b) Baby Clothes  
Fig. 8. Hit ratio comparison of the entire model and single models.

Table 3  
AUC performance on test sets of diferent sparsity levels.

<table><tr><td>Sparsity Level</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>BPRMF</td><td>0.3020</td><td>0.3368</td><td>0.3672</td><td>0.3950</td><td>0.4260</td><td>0.5732</td><td>0.6047</td><td>0.6275</td><td>0.6454</td><td>0.6587</td></tr><tr><td>CDL</td><td>0.3213</td><td>0.3601</td><td>0.3870</td><td>0.4307</td><td>0.4632</td><td>0.6245</td><td>0.6543</td><td>0.6751</td><td>0.6924</td><td>0.7046</td></tr><tr><td>VBPR</td><td>0.1441</td><td>0.2276</td><td>0.3066</td><td>0.3650</td><td>0.4148</td><td>0.6245</td><td>0.6520</td><td>0.6721</td><td>0.6910</td><td>0.7032</td></tr><tr><td>CKE</td><td>0.3843</td><td>0.4214</td><td>0.4484</td><td>0.4709</td><td>0.4940</td><td>0.6193</td><td>0.6484</td><td>0.6693</td><td>0.6864</td><td>0.6966</td></tr><tr><td>Deep-MINE</td><td>0.5001</td><td>0.5014</td><td>0.5377</td><td>0.5623</td><td>0.5799</td><td>0.6887</td><td>0.7085</td><td>0.7252</td><td>0.7390</td><td>0.7484</td></tr></table>

![](/api/attachments/49YSUXA7/fulltext/images/44c9eba472ec6265eac61b352bb22f80279e073b73e724b95cc0a810a6c52435.jpg)  
(a)

![](/api/attachments/49YSUXA7/fulltext/images/79c9c3a70c3cc22741de0abc46c75bf9cf0d22b0bf68e343b9660e6c92601163.jpg)  
(b)

![](/api/attachments/49YSUXA7/fulltext/images/ed9a23011e234fdc8760340b63a7590742d6136a12c211a9e2d09633cfd75398.jpg)  
(c)  
Fig. 9. The efect of incorporating cognitive styles. (a) Hit ratio performance; (b) AUC performance; (c) 10 random consumers' cognition style distribution.

Table 4  
Model performance with diferent node numbers for images.

<table><tr><td>Image auto-encoder</td><td>AUC</td><td>HIT@50</td><td>HIT@100</td><td>HIT@150</td><td>HIT@200</td></tr><tr><td>50-Node</td><td>0.8564</td><td>0.2816</td><td>0.3986</td><td>0.4742</td><td>0.5345</td></tr><tr><td>100-Node</td><td>0.8564</td><td>0.2936</td><td>0.4009</td><td>0.4695</td><td>0.5250</td></tr><tr><td>200-Node</td><td>0.8554</td><td>0.2826</td><td>0.3901</td><td>0.4631</td><td>0.5198</td></tr><tr><td>300-Node</td><td>0.8526</td><td>0.2821</td><td>0.3941</td><td>0.4685</td><td>0.5227</td></tr></table>

A 6-layer convolutional auto-encoder was designed in this study to represent information on product images, which is consistent with [56]. Some trial experiments were also conducted to help determine the number of lavers. Specifically, a subset of product images was selected from the training set, and networks with diferent number of layers were trained to achieve their local optimum. To compare their relative performance, we measured their loss function values $( \mathrm { i . e . , }$ as defined in Section 3.2.1 denoted by L1, which consists of reconstruction error terms and regularization terms for the weight matrix). It is obvious from Table 5 that the 6-layer structure had a better performance than the 4-layer and 8-layer networks.

## 4.3.6. Visualization of the recommendation results

To better illustrate the recommendation performance of Deep-MINE, four consumers in the Women's Dresses data were randomly selected with the top-5 recommendation image results generated by Deep-MINE, BPRMF, CDL, VBPR and CKE, respectively (see Fig. 10). The first row is the dresses that the consumers previously purchased, reflecting the consumers' historical tastes. The other five rows are the top-5 dresses recommended by Deep-MINE, BPRMF, CDL, VBPR and CKE, respectively. It can be intuitively observed that Deep-MINE had more recommendation variety compared with the baseline models. Concretely, BPRMF and VBPR tended to recommend the most popular products without much personalization for diferent consumers, i.e., 3–4 popular dresses could be repeatedly found in the recommendation results for the four consumers. In addition, Deep-MINE recommended more relevant dresses based on the tastes reflected in the consumers historical purchases, such as color (e.g., dark or colorful), size (e.g., long or short) and style (e.g., casual or formal). Although CKE and CDL showed some variety, they were not very consistent in taste with consumers' previous purchases.

## 5. Conclusion and future work

This study proposed a personalized recommendation model with multi-view information integration, i.e., Deep-MINE, which organically and comprehensively utilizes multiple sources of product content and considers users' heterogeneity in cognitive styles. A unified deep neural network was designed as an end-to-end model composed of three main parts: multi-view information representation, cognition treatment, and information integration, by which preferable recommendation perfor mances can be achieved. Extensive data experiments revealed the better of Deep-MINE in comparison to the baseline models. This study also shed light on the potential of a data-driven view of cognitive style.

## Table 5

Loss function values with diferent layers of image auto-encoder.

<table><tr><td>Image auto-encoder</td><td>4-Layer</td><td>6-Layer</td><td>8-Layer</td></tr><tr><td>Loss function value</td><td>0.0247</td><td>0.0137</td><td>0.0567</td></tr></table>

Consumer 2

![](/api/attachments/49YSUXA7/fulltext/images/4faabb9397e137bf9c5953a752534c598227429acdce5071a8469568ec956584.jpg)  
Fig. 10. Visualization of the top-5 recommendations by Deep-MINE and baseline models

Future work could be extended in the following directions. First, this study only considered a single kind of implicit feedback, namely, consumer purchase behavior. Some other feedback, such as product returns, consumer browsing and clicking behavior, provides more detailed information about consumer preferences and thus could be fur ther exploited in the design of recommender systems. For instance, the information representation part in the Deep-MINE model could be enriched by integrating such knowledge. Furthermore, this study incorporated the heterogeneity of cognitive style into a recommender system and proposed an integrated deep learning framework to solve the problem. Future research may consider representing user's cognitive styles from the perspective of other dimensions in addition to the Verbal-Imagery dimension considered in this study, to enrich the measurement of cognitive styles.

## Acknowledgements

The work was partly supported by the National Natural Science Foundation of China (71490724/71772101) and the MOE Project of Key Research Institute of Humanities and Social Sciences at Universities (17JJD630006).

## References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state of the art and possible extensions, IEEE Trans. Knowl. Data Eng. 17 (2005) 734–749.

[2] C. Allinson, J. Hayes, The Cognitive Style Index: a measure of intuition-analysis for organizational research, J. Manag. Stud. 33 (1) (1996) 119–135.

[3] R. Bendall, A. Galpin, L. Marrow, S. Cassidy, Cognitive style: time to experiment, Front. Psychol. 7 (2016) 1786.

[4] Y. Bengio, A. Courville, P. Vincent, Representation learning: a review and new perspectives, JEEE Trans, Pattern Anal, Mach, Intell, 35 (2013) 1798–1828.

[5] S. Boutemedjet, D. Ziou, A graphical model for context-aware visual content recommendation, JEEE Trans, Multimedia 10 (2008) 52–62

[6] I. Chakraborty, P. Hu, D. Cui, Examining the efects of cognitive style in individuals technology use decision making, Decis, Support, Syst, 45 (2008) 228–241.

[7] M. Chen, Improving website structure through reducing information overload, Decis, Support, Syst, 110 (2018) 84–94.

[8] C. Cheng, H. Yang, M.R. Lyu, I. King, Where you like to go next: successive point-ofinterest recommendation. Proceedings of the Twenty-Third International Joint Conference on Artificial Intelligence (IJCAI), 2013, pp. 2605–2611

[9] T.L. Childers, M.J. Houston, Conditions for a picture-superiority efect on consumer memory, J. Consum, Res, 11 (1984) 643–654.

[10] F. Cofield, D. Moseley, E. Hall, K. Ecclestone, Learning Styles and Pedagogy in Post 16 Learning: A Systematic and Critical Review. Learning & Skills Research Centre London, 2004.

[11] A. Engin, R. Vetschera, Information representation in decision making: the impact of cognitive style and depletion efects, Decis. Support. Syst. 103 (2017) 94–103.

[12] M. De Gemmis, P. Lops, C. Musto, F. Narducci, G. Semeraro, Recommender System Handbook, 2nd ed., Springer, 2015

[13] J.R. Hauser, G.L. Urban, G. Liberali, M. Braun, Website morphing, Mark. Sci. 28 (2) (2009) 202-223.

[14] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition,

Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 770–778.

[15] R. He, J. McAuley, VBPR: visual Bayesian personalized ranking from implicit feedback, Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence (AAAI-16), 2016, pp. 144–150.

[16] R. He, J. McAuley, Ups and downs: modeling the visual evolution of fashion trends with one-class collaborative filtering, Proceedings of the 25th International Conference on World Wide Web (WWW), 2016, pp. 507–517.

[17] B. Hidasi, A. Karatzoglou, L. Baltrunas, D. Tikk, Session-based recommendations with recurrent neural networks, Proceedings of the Fourth International Conference on Learning Representations (ICLR). 2015

[18] G.E. Hinton, S. Osindero, Y.W. Teh, A fast learning algorithm for deep belief nets, Neural Comput, 18 (2006) 1527–1554.

[19] Y. Hu, C. Volinsky, Y. Koren, Collaborative filtering for implicit feedback datasets, Proceedings of the Eighth IEEE International Conference on Data Mining (ICDM) 2008, pp. 263–272.

[20] Z. Jiang, I. Benbasat, Virtual product experience: efects of visual and functional control of products on perceived diagnosticity and flow in electronic shopping, J Manag. Inf. Syst. 21 (2004) 111–147.

[21] X. Jin, J. Luo, J. Yu, G. Wang, D. Joshi, J. Han, Reinforced similarity integration in image-rich information networks, IEEE Trans. Knowl. Data Eng. 25 (2013) 448-460.

[22] Q. Jones, G. Ravid, S. Rafaeli, Information overload and the message dynamics of online interaction spaces: a theoretical model and empirical exploration, Inf. Syst Res. 15 (2004) 194–211

[23] J. Kisielius, B. Sternthal, Detecting and explaining vividness efects in attitudinal judgments. J. Mark. Res, 21 (1984) 54–64.

[24] Y. Koren. R. Bell. C. Volinsky, Matrix factorization techniques for recommender systems, Computer (8) (2009) 30–37.

[25] M. Kozhevnikov, Cognitive styles in the context of modern psychology: toward an integrated framework of cognitive style, Psychol. Bull. 133 (3) (2007) 464–481.

[26] A. Krizhevsky, Ii. Sulskever, G.E. Hinton, ImageNet classification with deep convolutional neural networks, Advances in Neural Information Processing Systems (NIPS), 2012, pp. 1097–1105.

[27] Y.A. LeCun, Y. Bengio, G.E. Hinton, Deep learning, Nature 521 (2015) 436–444.

[28] C. Lei, D. Liu, W. Li, Z. Zha, H. Li, Comparative deep learning of hybrid representations for image recommendations, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 2545–2553.

[29] N.H. Leonard, R.W. Scholl, K.B. Kowalski, Information processing style and decision making, J. Organ. Behav. (1999) 407–420.

[30] K.H. Lim, I. Benbasat, The efect of multimedia on perceived equivocality and perceived usefulness of information systems, MIS O. 24 (2000) 449–471.

[31] K.H. Lim, I. Benbasat, L.M. Ward, The role of multimedia in changing first impression bias, Inf. Syst. Res. 11 (2) (2000) 115–136.

[32] H. Liu, J. He, T. Wang, W. Song, X. Du, Combining user preferences and user opinions for accurate recommendation, Electron. Commer. Res. Appl. 12 (1) (2013) 14–23.

[33] J. Liu. C. Wu, W. Liu. Bavesian probabilistic matrix factorization with social relations and item contents for recommendation, Decis. Support. Syst. 55 (2013) 838-850.

[34] Q. Liu, S. Wu, L. Wang, DeepStyle: learning user preferences for visual recommendation. Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Inf Retr (2017) 841-844

[35] S. Lu. L. Xiao, M. Ding, A video-based automated recommender (VAR) system for garments, Mark. Sci. 35 (2016) 484–510.

[36] H. Ma, T.C. Zhou, M.R. Lyu, I. King, Improving recommender systems by incorporating social contextual information, ACM Trans. Inf. Syst. 29 (2) (2011) 1-23.

[37] J. Masci, U. Meier, D. Cireşan, J. Schmidhuber, Stacked convolutional auto-encoders for hierarchical feature extraction, International Conference on Artificia Neural Networks, 2011, pp. 52–59.

[38] J. McAuley, J. Leskovec, Hidden factors and hidden topics: understanding rating dimensions with review text, Proceedings of the 7th ACM Conference on Recommender Systems (RecSys), 2013, pp. 165–172.

[39] J. McAuley, C. Targett, Q. Shi, A. Van Den Hengel, Image-based recommendation on styles and substitutes, Proceedings of the 38th International ACM SIGIR Conference on Research and Development in Information Retrieval, 2015, pp. 43–52.

[40] S. Messick, The nature of cognitive styles: problems and promise in educationa practice, Educ. Psychol. 19 (2) (1984) 59–74.

[41] Y. Ouyang, W. Liu, W. Rong, Z. Xiong, O. Yuanxin, L. Wenqi, R. Wenge, X. Zhang, Autoencoder-based collaborative filtering, International Conference on Neural Information Processing, 2014, pp. 284–291.

[42] W. Pan, L. Chen, GBPR: group preference based Bayesian personalized ranking for one-class collaborative filtering. Proceedings of the Twenty-Third International Joint Conference on Artificial Intelligence (IJCAI), 2013, pp. 2691–2697.

[43] L.A. Peracchio, J. Meyers-Levy, Using stylistic properties of ad pictures to com municate with consumers, J. Consum. Res. 32 (1) (2005) 29–40.

[44] S. Rendle, C. Freudenthaler, Z. Gantner, L. Schmidt-Thieme, BPR: Bayesian personalized ranking from implicit feedback, Proceedings of the Twenty-fifth Conference on Uncertainty in Artificial Intelligence, 2009, pp. 452–461.

[45] R. Riding, I. Cheema, Cognitive styles—an overview and integration, Educ. Psychol. 11 (3–4) (1991) 193–215.

[46] R. Riding, S. Rayner, Cognitive Styles and Learning Strategies: Understanding Style Diferences in Learning and Behavior, David Fulton Publishers, 2013.

[47] R. Salakhutdinoy, A. Mnih, G. Hinton, Restricted Boltzmann machines for collaborative filtering, Proceedings of the 24th International Conference on Machine learning (ICML), 2007, pp. 791–798.

[48] M. Siering, A.V. Deokar, C. Janze, Disentangling consumer recommendations: explaining and predicting airline recommendations based on online reviews, Decis. Support. Syst. 107 (2018) 52–63.

[49] J.Z. Sojka, J.L. Giese, The influence of personality traits on the processing of visua and verbal information Mark, Lett, 12 (2001) 91–106

[50] J.Z. Sojka, J.L. Giese, Communicating through pictures and words: understanding the role of afect and cognition in processing visual and verbal information, Psychol. Mark. 23 (12) (2006) 995–1014.

[51] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan, V. Vanhoucke, A. Rabinovich, C. Hill, A.S. Arbor, Going deeper with convolutions, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition

(CVPR), 2015, pp. 1–9.

[52] C. Wang, D.M. Blei, Collaborative topic modeling for recommending scientific articles. Proceedings of the 1Zth ACM SIGKDD International Conference or Knowledge Discovery and Data Mining (KDD), 2011, pp. 448–456.

[53] H. Wang, N. Wang, D.-Y. Yeung, Collaborative deep learning for recommender systems, Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), 2015, pp. 1235–1244.

[54] M. Wang, X. Li, P.Y. Chau, The impact of photo aesthetics on online consumer shopping behavior: an image-processing-enabled empirical study, Proceedings o 2016 International Conference on Information Systems (ICIS), 2016.

[55] S. Wang, Y. Wang, J. Tang, K. Shu, S. Ranganath, H. Liu, What your images reveal: exploiting visual contents for point-of-interest recommendation, Proceedings of th 26th International Conference on World Wide Web (WWW), 2017, pp. 391–400.

[56] F. Zhang, N.J. Yuan, D. Lian, X. Xie, W. Ma, Collaborative knowledge base embedding for recommender systems, Proceedings of the 22th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), 2016, pp. 353–362.

[57] S. Zhang, L. Yao, Deep learning based recommender system: a survey and new perspectives, ACM Comput. Surv. 1 (1) (2018).

[58] Y. Zhang, Q. Ai, X. Chen, W.B. Croft, Joint representation learning for top-N re commendation with heterogeneous information sources, Proceedings of the 2017 ACM on Conference on Information and Knowledge Management (CIKM), 2017, pp. 1449–1458.

Yue Guan is currently pursuing her PhD degree at the School of Economics and Management, Tsinghua University, Beijing, China. Her research interests include deep learning, business analytics, and online recommendation

Qiang Wei is an associate professor in the Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, Beijing, China. His current research interests include deep learning, information management, business analytics, and business intelligence.

Guoqing Chen received his PhD from the Catholic University of Leuven (K.U. Leuven, Belgium) and now is Professor of Information Systems at the School of Economics and Management, Tsinghua University, Beijing, China. His research interests include information systems management, business analytics and decision support systems.
