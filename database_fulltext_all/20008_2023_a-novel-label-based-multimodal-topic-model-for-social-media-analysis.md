---
otero_id: 20008
otero_key: "V42W9RES"
title: "A novel label-based multimodal topic model for social media analysis"
authors: "Hao Li; Yang Qian; Yuanchun Jiang; Yezheng Liu; Fan Zhou"
year: "2023"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113863"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel label-based multimodal topic model for social media analysis

![](/api/attachments/V42W9RES/fulltext/images/faca2758787368d429521de09d4513ee4e5b150c1f8b0c27dd16d77d4a4edfa2.jpg)

Hao Li <sup>a</sup>, Yang Qian <sup>a,b,\*</sup>, Yuanchun Jiang <sup>a,c</sup>, Yezheng Liu <sup>a,d</sup>, Fan Zhou

<sup>a</sup> School of Management, Hefei University of Technology, Hefei, Anhui 230009, China

<sup>b</sup> Key Laboratory of Process Optimization and Intelligent Decision-making, Ministry of Education, Hefei, Anhui 230009, China

<sup>c</sup> Key Laboratory of Philosophy and Social Sciences for Cyberspace Behaviour and Management, Anhui Province

<sup>d</sup> National Engineering Laboratory for Big Data Distribution and Exchange Technologies, Shanghai 200436, China

## A R T I C L E I N F O

Keywords: Multimodal data Topic modeling Label data Supervised model Image representation

## A B S T R A C T

Extracting useful knowledge from multimodal data is the core of many multimedia applications, such as recommendation systems, and cross-modal retrieval. In this paper, we propose a label-based multimodal topic (LB-MMT) model to jointly model text and image data tagged with multiple labels. Specifically, we use the labels as supervised information to generate the text and image data. In the LB-MMT model, we assume that the textual words and visual words related to each text and image are drawn from a mixture of latent topics, where each topic is represented as a group of textual words and visual words. Moreover, we introduce multiple topics for each label, to build the top-down relationship from label to text and image. To investigate the effectiveness of the proposed approach, we conduct extensive experiments on a real-world multimodal dataset with labels. The re sults show the proposed approach obtains superior performances on topic coherence and label prediction compared with previous competitors. In addition, we show that our model yields interesting insights about multimodal topics. The proposed model provides important practical implications, e.g., designing more attrac tive multimodal contents for marketers.

## 1. Introduction

With the development of information technology, multimodal data in online social networks (e.g., Facebook) and e-commerce (e.g., Amazon) platforms, is becoming more prevalent, such as texts, images, and video clips. Mining valuable information from these multimodal data plays an important role in many applications, e.g., recommenda tion systems [1,2], cross-modal information retrieval [3], and online advertising [4].

Texts and their associated images are typical multimodal data. Recently, many previous studies have focused on modeling text and image modalities, simultaneously. Most of these works mainly can be divided into two categories. The first one based on deep learning models attempts to learn the joint representations of texts and images for tasks of image annotation and tag recommendation, etc. [5–8]. The second category of work based on probabilistic topic models tends to extract the interpretable information by modeling the semantic correlations be tween textual contents and visual features of images [9]. For instance, Blei and Jordan [10] first proposed a multimodal topic model, namely Corr-LDA, to learn the relationship between images and text modalities.

Despite the success of the existing studies, one limitation is that they ignore some other important information related to the texts and im ages, i.e., labels.

On many online platforms, the texts and their associated images are often labeled with multiple human-offered tags. For example, in Taobao. com (see Fig. 1), marketers often use textual descriptions and product images to promote products and also customize some tags or keywords related to these contents. Note that the label set conveys the key infor mation and reveals a summary of the semantic content of texts and images. In terms of platforms, the label set also plays an important role in helping users quickly retrieve the information. We conjecture that considering the label information could greatly enhance the perfor mance for understanding the textual contents and images.

In our paper, our goal is to extend multimodal topic models to detect valuable and interpretable topics by jointly leveraging the texts and associated images with labels. Due to the nature of multi-modal data, there are several challenges we have to solve. The first challenge is how to characterize the top-down relationship from label to text and image. Intuitively, the label set on a webpage (see Fig. 1) denotes higher-level information that can clearly account for the words and images (lowerlevel) used on this webpage. The second challenge is the one-to-many relationship between label and topic: each label in the label set may have multiple sub-topics. For example, one topic related the appearance of the product (representative words with “crew neck,” “loose,” “turtleneck,” and “slim”) and one topic related to fashion compatibility for the product (representative words with “casual pants,” “matching,” “shoes” and “bag”) belong to the same label, sweater. The last challenge is how to represent the visual and textual information under the constraint of their associated labels. In Fig. 1, it is evident that labels can be viewed as summaries of the semantic content of textual contents and images.

The principle mechanism of the supervised learning methods offers a promising way to address the first two challenges. Unlike Latent Dirichlet Allocation (LDA) [11] that is a popular unsupervised topic model, supervised topic models can incorporate a target variable into the learning process, to discover the latent topics. Representative at tempts contain supervised Latent Dirichlet Allocation (sLDA) [12], discriminative LDA (DiscLDA) [13], maximum entropy discrimination LDA (MedLDA) [14]. However, these works assume that each document is endowed with a single response label (or rating), thus are inapplicable to a multi-label setting. Labeled LDA (L-LDA) proposed by Ramage et al. [15], is a typical multi-label probabilistic generative model. Similar to LDA, L-LDA assumes that each document is modeled as a mixture of latent topics, whereas the topic prior is constrained by the space of the label set of this document. Although L-LDA can model the top-down relationship from label to text, it can not capture latent sub-topic within a given label. In contrast, Partially Labeled Dirichlet Allocation (PLDA) [16] is proposed to solve this issue by introducing per-label latent topics to construct the one-to-many relationship between label and topic. Successfully addressing the third challenge requires the multimodal topic model as we mentioned earlier.

Therefore, we propose a method for multimodal and multi-label corpora, called label-based multimodal topic (LB-MMT) model. The LB-MMT model is built upon the PLDA by introducing visual informa tion and integrating word embedding. In particular, based on the idea of the bag of words, we use scale-invariant feature transform (SIFT) to represent each image to visual words. We use the labels as supervised information to generate the text and image data. We assume that the textual words and visual words related to each text and image are drawn from a mixture of latent topics, where each topic is represented as a group of textual words and visual words that are semantically related to each other. For the textual data, continuous space word embeddings can efficiently capture the semantic relationships among words and thus be widely applied to improve the performance of topic models [17,18]. In the proposed model, to enhance the topic learning, we use a pre-trained BERT model to obtain the embedding vectors of textual words and then integrate these word embedding into our multimodal topic model. In addition, the LB-MMT model introduces multiple topics for each label, which allows us to better examine the relationship between labels and topics. Finally, we design a novel collapsed Gibbs sampling algorithm for LB-MMT inference.

We evaluate our proposed model using a field dataset crawled from Taobao. We collect a large number of marketer-generated contents including texts and images, tagged with multiple labels. The empirical experiments demonstrate superior performances of our model when compared with other benchmark models. Note that integrating the label and visual information into the model can enhance topic learning.

![](/api/attachments/V42W9RES/fulltext/images/26b1e3ee87257d3b9f4360d5666171ef0fa5b7b0b4d5946df6adf149195a6fc9.jpg)  
Fig. 1. Two examples of textual descriptions and product images labeled with multiple tags.

The main contributions of this paper can be summarized as follows:

(1) To our best knowledge, this paper is the first attempt that jointly analyzes text and image data tagged with multiple labels. Although previous works have explored how to model text and image modalities simultaneously, integrating the label as super vised information has not been explored yet.

(2) We propose a label-based multimodal topic model to discover more interpretable topics from the multimodal data with labels. And this model strives to address the three key challenges of our problem: the top-down relationship from label to text and image; the one-to-many relationship between label and topic; and the representation of the visual and textual information in the model.

(3) To measure the performance of our model, we collect a real-world multimodal dataset with labels. Experimental results show that our model can uncover more interpretable topics than benchmark models. In addition, the learned topics can be used as input for subsequent label classification tasks.

The rest of the article is organized as follows. In Section 2, we briefly review relevant studies to our work. Section 3 mainly introduces our model framework. We present the experimental results in Section 4. Finally, we make the conclusions in the last section.

## 2. Related work

Our work is related to the studies of multimodal learning, unsuper vised topic model, label-based supervised topic model. In this section, we review the related literature.

## 2.1. Multimodal learning

Multimodal learning is an active research field in computer science and other applications, e.g., recommendation systems [19–21] and popularity prediction [22]. Multimodal learning methods are mainly divided into two categories: traditional multimodal representation methods and deep learning frameworks.

For traditional multimodal representation learning, Li and Xie [23] first used linguistic content category variables (e.g., affect words, and social words) to encode textual contents, and then applied some open tools to extract some interpretable features (e.g., colorfulness and image quality) to encode images. Kan et al. [24] extended the discriminant analysis and proposed a multi-view discriminant analysis (MvDA) method to learn common discriminative features from multimodal data by maximizing inter-class variation and minimizing intra-class variation at the same time. By introducing Joint Representation Learning (JRL) to extract multimodal data features, Zhai et al. [25] jointly explored the relevance and semantic information in a unified optimization frame work. Although these methods have achieved good results in multi modal feature learning, they may face several issues. First, some methods [23] usually rely on feature engineering to extract useful fea tures, which consumes a lot of human efforts. If mistaken or imperfect features are obtained from multimodal data, the subsequent empirical studies and predictive analytics may be affected. Second, traditional machine learning methods are not able to capture the advanced nonlinear information in real-world multimodal data.

For deep multimodal representation learning, Deng et al. [26] pro posed a novel deep network framework to capture more general se mantic relevance between cross-modal retrieval. Hu et al. [27] employed multiple feedforward neural networks and a novel eigenvalue-based multi-view objective function to capture the complex cross-modal correlation with high nonlinearity. Qian et al. [28] pro posed a text-guided attention neural network model to jointly extract features from textual and visual contents. Although the deep learning models can obtain more complex relationships between multimodal data, they often face the black-box problem, which lacks the ability to interprete the underlying processes of some phenomenon. In addition, deep learning methods rely heavily on large-scale datasets to achieve a good performance.

Our work belongs to the probabilistic graph model, which extends the topic model to the context of multimodal data. One of the major advantages of using topic models to learn multimodal representations is their generative nature, which allows a simple way to understand the model’s architecture and has good interpretability.

## 2.2. Unsupervised topic model

Probabilistic topic models are typical natural language processing techniques that are widely used in many tasks, e,g., recommendation systems and information retrieval [29]. Popular topic models include variants of LDA, and they are unsupervised topic models. For example, Slof et al. [30] used LDA to extract topics from this textual data as variables for predicting churn reasons. Cheng et al. [31] proposed a Biterm topic model (BTM) for extracting topics from short texts.

For multimodal data, Corr-LDA is one of the representative multi modal topic models, which assumes the topics of the text and image modalities have a one-to-one correspondence [10]. And these are a se ries of variants of this model. For example, Cao and Li [32] proposed a spatially coherent latent topic model (Spatial-LTM) to segment and classify objects in images. To explain correlations between different modalities, Multimodal LDA [33] introduced a regression module to connect two sets of topics, thus can obtain general forms of association and allow the number of topics in the two data modalities to be different. In terms of application scenarios, KGE-MMSLDA [34], a multi-modal topic model, combined knowledge entity priors to jointly use text de scriptions and images to discover interpretable topics for public social event analysis.

Our work also belongs to this line of work, extending topic models to the context for multimodal data. Different from these models, we introduce the label information to enhance the performance of topic learning in multimodal data.

## 2.3. Label-based supervised topic model

Supervised topic models mainly concentrate on extending unsuper vised topic models (e.g., LDA) to deal with the supervised tasks. Recent efforts are often used to analyze the textual contents and responses, which each response can be viewed as a label or review rating. The supervised topic models mainly treat labels or review ratings as valuable supervision signals to improve topic learning [35]. The sLDA [12] was first proposed to model each document associated with a response var iable. In detail, sLDA generates the numerical response variable (e.g., rating) using the generalized linear model and categorical response variable (e.g., label) using the softmax function. Another supervised topic model for label classification, DiscLDA [13], added a label dependent linear transformation to the topic mixture proportions, where the transformation matrix was trained by maximizing the con ditional marginal likelihood of the text labels. The MedLDA [14] incorporated the mechanism behind the support vector machines (SVMs) and topic models (e.g., LDA) into a unified framework. Specif ically, MedLDA needs to balance two objective functions: the loglikelihood of the topic learning and prediction error on training data. However, these methods belong to downstream supervised topic models, which focus on the label prediction based on the topic repre sentation of the document. In addition, these works assume that each document is endowed with a single response label (or rating), thus are inapplicable to a multi-label setting.

Recently, there has been a stream of methods that are designed from multi-label settings. L-LDA [15] made a strong assumption that each document can be only represented by limited topics and these topics are only sampled from the label set of this document. However, L-LDA builds a one-to-many relationship between the label and topic, which tightly restricts topic assignment for each word. To break this defect of L LDA, PLDA [16] used a topic class associated with the document labels, to infer the latent topics within each label, as well as unlabeled. Besides. based on the attention mechanism of the deep neural network, Wang and Yang [36] proposed Topic Attention Model (TAM) for label classi fication and optimized the parameters by variational inference. In TAM, labels in the document are used to improve the latent topic structure learned by the variational autoencoder. Although these models intro duce the document-level label information, it can be used only in topic extraction from a text collection, ignoring the important visual information.

Our work is built on label-based supervised topic models. We incorporate the visual information to extend these models for supervised learning. We design the collapsed Gibbs sampling algorithm to infer model parameters. To the best of our knowledge, we are the first to develop such a supervised topic model to jointly leverage the texts and associated images with multiple labels.

## 3. Proposed method

The overall framework of our proposed LB-MMT model is illustrated in Fig. 2. The input to LB-MMT includes textual contents, image con tents, and associated labels. Before we start the modeling process, we first apply an advanced language representation model, namely pretrained BERT model [37], to obtain word embedding from textual contents. Then, we use SIFT algorithm to extract invariant feature points from images as visual words, construct a vocabulary, and apply the vi sual words in the vocabulary to represent each image. Next, we design the supervised topic model, LB-MMT, which uses labels to supervise visual and textual information generation. This model can easily mine latent topics from multimodal data, and use the discovered distribution of topic probability to interpret the meaning of labels.

Before we continue to specify the model, we first formally give our problem definition. Then, we describe our proposed model in detail. Finally, we describe the inference of the proposed model.

## 3.1. Problem definition

We use $M = \{ d _ { 1 } , d _ { 2 } , . . . , d _ { M } \}$ to denote a set of multimodal documents, where each d contains three kinds of information $d = \{ w _ { d } , \pmb { \nu } _ { d } , \pmb { \Lambda } _ { d } \}$ . Let w $= \{ w _ { d , ~ 1 } , w _ { d , ~ 2 } , . . . , w _ { d , ~ i } . . . , w _ { d , ~ N _ { d } } \}$ denote a multi-set of textual words in document d from a textual vocabulary $\mathbb { W } ,$ where $w _ { d , \ i }$ is the $i ^ { t h }$ word token and $N _ { d }$ denotes the total number of words in document d. For the word token $w _ { d , \ i } ,$ we denote $e _ { d , i } \in \mathbb { R } ^ { E }$ as the embedding of this textual word, where E is the dimension of word embedding. Let $\Lambda _ { d }$ denote a set of labels from a space of labels L. Let $\pmb { \nu } _ { d } = \{ \nu _ { d , \ 1 } , \nu _ { d , \ 2 } , . . . , \nu _ { d , \ i } , . . . , \nu _ { d , \ C _ { d } } \}$ denote visual words in document d from a visual vocabulary $\mathbb { V } _ { i }$ , where $\nu _ { d , \astrosun }$ is the $i ^ { t h }$ visual word in the document d and $C _ { d }$ denote the total number of visual words in document d. In Appendix $\mathbf { A } ,$ we list all the notations used in this paper.

In our model, we define some number of topics ${ \mathbb K } _ { l }$ (indexed by $1 , 2 ,$ $\cdots , K _ { l } )$ for each label. For each topic $k \in \{ 1 , 2 , . . . , K _ { j } \}$ , we define a multivariate Gaussian distribution with mean $\pmb { \mu _ { k } }$ and covariance $\Sigma _ { k } ,$ which is used to model the word embedding in the continuous space. In addition, we define $\varphi _ { k }$ as a V-dimensional multinomial distribution over the visual words. The traditional topic model (e.g., LDA) assumes that each document has a K-dimensional multinomial distribution $\pmb { \theta } _ { d }$ over all topics. However, our model restricts $\pmb { \theta } _ { d }$ to be defined only over all topic $\textstyle \sum l \in \mathbf { \Lambda } _ { d } K _ { l }$ that correspond to its labels $\mathbf { \Delta } \Lambda _ { d } .$

Based on the above notations, we formally define our problem: Given all the documents that contain texts, images, and labels, the target is to learn topic-related parameters $\mu _ { k } ,$ $\Sigma _ { k }$ and $\varphi _ { k }$ related to each label, and infer document topic distribution $\pmb { \theta } _ { d } .$

## 3.2. Model description

## 3.2.1. BERT model for word representation

The traditional topic model (e.g., LDA) naturally represents docu ments via bag-of-words methods, while ignoring the sequential and se mantic relationships among words in the documents. In our proposed model, we use an advanced embedding method, namely pre-trained BERT model [37] to obtain each word representation in our textual contents. This BERT model can transform each word as a continuous vector into a low-dimensional Euclidian space. Due to the learned word representation revealing semantic and syntactic relations, it is widely used in enhancing topic learning [17,18].

In this paper, we independently capture word embeddings offline to reduce the computational load time during topic inference. Specifically, for each textual content, we first prepend a start token [CLS], then use sequential word tokens as input for the BERT model. Finally, the contextualized representation of each word token can be computed. Due to the Chinese data of our context, we select the pre-trained BERT-basechinese model<sup>1</sup> with 12-layer, 768-hidden, and 12-heads. We set the learning rate to $1 \mathrm { e } ^ { - 5 }$ , batch size to 100 and epoch to 50 for the task of fine-tuning in BERT. However, this tool regards each Chinese character as a word, and each Chinese character is represented as a vector with 768-dimension. To obtain the word embedding, we use an average strategy to integrate all the character embedding in each word [38].

## 3.2.2. BOVW model for image representation

The bag of visual words (BOVW) model is a traditional and basic method for automatic image representation, which has been widely used in image retrieval and classification [39,40]. Its concept is adapted from the bag of words (BOW) in natural language processing (NLP). Instead of textual words, BOVW attempts to encode the image with the statistical frequency of the visual words [41]. As shown in Fig. 3, BOVW consists of three steps: the SIFT feature extraction, K-means clustering, and representation.

We first apply the Scale Invariant Feature Transform (SIFT) [42] to identify local features in images. The SIFT is one of the most efficient and robust computer vision algorithm that has been applied to different fields of management research $[ 4 3 , 4 4 ]$ ]. The first step of SIFT is to extract a set of keypoints that reveal the most important and distinct informa tion from local regions of the image. To detect the stable keypoints, Lowe [42] applied a difference-of-Gaussian function to compute extrema location in scale-space. Then, we extract more distinctive feature descriptors for the keypoints by sampling the image gradient magnitudes and orientations around the keypoints. The descriptor is a vector in continuous space, which is used to encode the salient aspects of keypoint. Specifically, we first divide each image into several patches. Then, for each image patch, we extract its SIFT descriptor that is pre sented as a promising 128- dimension vector. For this step, we use an existing software library that is implemented by Python language, namely opencv-python.<sup>2</sup> This library has been widely used in image processing [45–47]. Fig. 4 gives three examples to show the keypoints extracted by SIFT on our dataset. The identified regions are displayed by lower images, with keypoints displayed as circles with color.

Second, using the SIFT descriptors as input, we employ the K-means clustering method to capture the discrete set of visual terms for con structing the visual vocabulary. Each cluster is regarded as a distinct visual word in the vocabulary. We select the number of k in K-means by varying the number of k and using the label classification task to eval uate the clustering performance. According to the results (see Appendix $\mathbf { B } ) ,$ , the number of k in K-means is set to 900. Finally, each image can be represented by 900 visual words. With the cluster assignments of each visual word in an image, we can obtain the visual word distribution, and create a frequency histogram as a feature vector to represent this image.

![](/api/attachments/V42W9RES/fulltext/images/b56256bb0ee95f22de73d8d63c41df8495d53dae58c36fdc8376cd6702c1fef7.jpg)  
Fig. 2. The framework of the proposed method.

## 3.2.3. LB-MMT mode

In this part, we propose a label-based multimodal topic (LB-MMT) model that is used to mine latent topics from multimodal data, and use the discovered distribution of topic probability to detect valuable topics. In the LB-MMT model, labels, textual and visual information are inte grated into a unified framework. All textual and visual words are generated in the same topic space.

Generally, many documents consist of texts and associated visual content, and these documents will carry multiple human-provided tags. To make better use of the multimodal information of documents, the proposed model integrates labels into multimodal topic modeling by using labels to supervise topic generation of text and visual contents. By doing this, the LB-MMT model improves the performance of topic learning in multimodal data. Fig. 5 shows the graphical representation of the LB-MMT, where the shaded nodes are the observed variable and unshaded nodes are the latent variable. Next, we describe the LB-MMT in detail.

Each multimodal document d consists of $N _ { d }$ textual words, $C _ { d }$ visual words and $\Lambda _ { d }$ labels. The LB-MMT model can be considered as a threelayer model with document layer, label layer, and topic layer. In the document layer, unlike the traditional topic model, the proposed model assumes that each multimodal document is a mixture of only those topics that are in a topic class related to one or more of the labels in this document. In the label layer, we argue that labels are generally avail able, and they can serve as useful supervision signals to improve topic modeling learning. Several supervised topic models have integrated the label information related to documents [35,48]. The proposed model assumes that there are a set of L labels (indexed by ${ 1 , 2 , . . . , L } )$ . We assign a number of topics ${ \mathbb K } _ { l }$ for each label. Therefore, a one-to-many relation ship is formed between the label and the topics. Based on the mecha nisms of supervised learning, we constrain the topic assignments so that the topic for the textual word or visual word is only related to the labels in the document. Because these are general or noise information that is irrelevant to labels of documents, we also define a background label to generate some background topics, to filter out these irrelevant infor mation. In the topic layer, each topic k is modeled as two types of dis tributions over the textual vocabulary W and over the visual vocabulary $\mathbb { V } .$ Since the textual words are transformed into continuous vectors by BERT, we model the word embedding using a multivariate Gaussian distribution [49]. Formally, we give the generative process of the pro posed LB-MMT model in Fig. 6.

![](/api/attachments/V42W9RES/fulltext/images/b1964602a7c7346cb80b82ba432ba51b92c1f341c9be367ecf004e2ddeb17959.jpg)  
Fig. 3. The process of BOVW representation.

![](/api/attachments/V42W9RES/fulltext/images/5b8a0f62bf78d1debc4bef76f783febb84d0adfd0ef4177c28609ce14fbe33c9.jpg)  
Fig. 4. Visualization of the keypoints extracted by SITF.

![](/api/attachments/V42W9RES/fulltext/images/9b66fea13a6c7f41b22f201f0167d9ab91965c221a8f6eb260b3e0705c7c0e4f.jpg)  
Label Content  
Fig. 5. The graphical representation of LB-MMT.

As shown in Fig. $^ { 6 , }$ textual topic $z ^ { w }$ and visual topic $z ^ { \nu }$ are generated from the same topic distribution θ. In the generative process of a multimodal document, textual and visual information are processed independently. Similar to LDA, each multimodal document is considered as a mixture of latent topics. However, these topics are shared across documents’ labels. To be more specific, for the document $d ,$ we first pick up a label $j \in \Lambda _ { d }$ and generate the per-document topic distribution $\theta _ { d , j }$ over topics $1 . . . K _ { j } .$ The $\theta _ { d , j }$ is drawn from a Dirichlet prior with param $\alpha _ { \theta _ { d , j } }$ $i ^ { t h }$ is first generated from $\theta _ { d , j } .$ Finally, the textual word embedding $e _ { d , \mathrm { ~ l ~ } }$ is chosen from a multivariate Gaussian distribution with mean $\mu _ { j , z _ { d , i } ^ { w } }$ and covariance $\Sigma _ { j , z _ { d , i } ^ { w } }$ . To improve the computational efficiency, we place conjugate priors on the parameters of the multivariate Gaussian distri bution. Thus, the covariance for each topic is drawn from an inverse Wishart distribution with parameters ψ and δ. And the mean for each topic is drawn from a multivariate Gaussian distribution with the parameters ρ and $\kappa .$ On the other hand, to generate the $i ^ { t h }$ visual word of document $d ,$ a topic $ { z _ { d , i } ^ { \nu } }$ is first generated from $\theta _ { d , j } .$ Finally, the visual word $\nu _ { d , \astrosun }$ is chosen from the per-topic visual word distribution $\varphi _ { j , z _ { d , i } ^ { \nu } }$

We can learn various probability distributions from the LB-MMT model to describe the distribution of labels, textual and visual content of multimodal documents. $\theta _ { d , j , l }$ represents the degree of preference that topic k belongs to label j in the multimodal document d. For the multi modal documents, $\mu _ { j , \mathrm { ~ } }$ <sub>k</sub> and $\Sigma _ { j , \ l }$ <sub>k</sub> is used to model the probability of textual word belonging to topic k of label $j , \varphi _ { j , k , \uparrow }$ captures the proba bility of visual word v belonging to topic k of label j.

## 3.3. Model inference

To learn the latent variables $( \mathrm { i . e . , } \mu _ { j , k } , \Sigma _ { j , k } , \theta _ { d , j , k } , \varphi _ { j , k , \nu } ) ,$ , we propose a collapsed Gibbs sampling algorithm. Deriving the joint probability distribution is the key to implementing the collapsed Gibbs sampling algorithm. During the sampling process, the new value of the latent variables is iteratively updated according to the state before the condi tional distribution. The solution processes of the latent variables are shown as follows.

The joint probability distribution of the observed textual word embedding e and visual word v with the unobserved label, unobserved textual word topic assignment $z ^ { w }$ and visual word topic assignment $z ^ { \nu }$ can be written as follows:

$$
p (e, v, z ^ {w}, z ^ {v}, l | \alpha , \beta^ {w}, \beta^ {v}) = p (e | z ^ {w}, l, \xi) p (v | z ^ {v}, l, \beta^ {v}) p (z ^ {w}, z ^ {v}, l | \alpha)\tag{1}
$$

where the tuple $\boldsymbol { \xi } = ( \boldsymbol { \psi } , \delta , \boldsymbol { \rho } , \boldsymbol { \kappa } )$ denotes the parameters of the prior dis tribution for the multivariate Gaussian distribution. We note that the first part of Eq. (1) can be derived as follows:

$$
p (e | z ^ {w}, l, \xi) = \int \int \mathcal {N} (e | \boldsymbol {\mu} _ {k}, \boldsymbol {\Sigma} _ {k}) \mathcal {N} \left(\boldsymbol {\mu} _ {k} | \rho , \frac {1}{\kappa} \boldsymbol {\Sigma} _ {k}\right) \mathscr {W} ^ {- 1} (\psi , \delta) d \boldsymbol {\mu} _ {k} d \boldsymbol {\Sigma} _ {k} = \prod_ {j \in \Lambda} \prod_ {k = 1} ^ {K _ {j}} I _ {\delta_ {j, k} - E + 1} \left(e | \mu_ {j, k}, \frac {\kappa_ {j , k} + 1}{\kappa_ {j , k}} \Sigma_ {j, k}\right)\tag{2}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Generative process of LB-MMT
1 for each topic $k \in \{1,2,\cdots,K_j\}$ do
2 Generate textual topic covariance $\Sigma_{j,k} \sim W^{-1}(\psi,\delta)$
3 Generate textual topic mean $\mu_{j,k} \sim N\left(\rho,\frac{1}{\kappa}\Sigma_{j,k}\right)$
4 Generate $\phi_{j,k}^v \sim Dir\left(\beta^v\right)$
5 end
6 for each document $d \in \{1,2,\cdots,M\}$ do
7 for each label $j \in \Lambda_d$, where $\Lambda_d \in \{1,2,\cdots,L\}$ do
8 Generate $\theta_{d,j} \sim Dir\left(\alpha_{\theta_{d,j}}\right)$
9 for $i^{th}$ textual word $w_{d,i}$ of document $d$, where $i \in \{1,2,\cdots,N_d\}$ do
10 Generate $z_{d,i}^w \sim Multinomial\left(\theta_{d,j}\right)$
11 Generate $e_{d,i}^w \sim N\left(\mu_{j,z_{d,i}^w}\Sigma_{j,z_{d,i}^w}\right)$
12 end
13 for $i^{th}$ visual word $v_{d,i}$ of document $d$, where $i \in \{1,2,\cdots,L_d\}$ do
14 Generate $z_{d,i}^v \sim Multinomial\left(\theta_{d,j}\right)$
15 Generate $v_{d,i} \sim Multinomial\left(\varphi_{j,z_{d,i}^v}^v\right)$
16 end
17 end
18 end
</div>

Fig. 6. The generative process of the LB-MMT model.

where $\ell _ { f } ( X | \pmb { \mu } ^ { \prime } , \pmb { \Sigma } ^ { \prime } )$ denotes the multivariate t-distribution with the degree of freedom f and parameters $\pmb { \mu } ^ { \prime }$ and Σ<sup>′</sup>. The posterior parameters in this tdistribution are shown in Appendix C. The second part of Eq. (1) can be derived as follows:

$$
p (v | z ^ {v}, l, \beta^ {v}) = \int p (v | z ^ {v}, l, \varphi) p (l, \varphi | \beta^ {v}) d \varphi = \prod_ {j \in \Lambda} \prod_ {k = 1} ^ {K _ {j}} \frac {\Delta \left(m _ {* , j , k , v} + \beta^ {v}\right)}{\Delta (\beta^ {v})}\tag{3}
$$

where the notation $\begin{array} { l } { { m * _ { j , k , \nu } = \sum _ { d = 1 } ^ { M } m _ { d , j , k , \nu } } } \end{array}$ denotes the number of the vi sual word v generated by the label j topic $k \in \{ 1 , 2 , . . . , K _ { j } \}$ . The third part of Eq. (1) can be derived as follows:

$$
p (z ^ {w}, z ^ {v}, l | \alpha) = \int p (z ^ {w} | l, \theta) p (z ^ {v} | l, \theta) p (\theta | \alpha) d \theta\tag{4}
$$

Eq. (4) can be considered the joint likelihood of the topic assign ments and labels. We not that:

$$
p (z ^ {w} | l, \theta) = \prod_ {d = 1} ^ {M} \prod_ {i = 1} ^ {N _ {d}} p \left(z _ {d, i} ^ {w} | l _ {d, i}, \theta_ {d, l _ {d, i}}\right) = \prod_ {d = 1} ^ {M} \prod_ {i = 1} ^ {N _ {d}} \theta_ {d, l _ {d, i}, z _ {d, i} ^ {w}} = \prod_ {d = 1} ^ {M} \prod_ {j \in \Lambda_ {d}} \prod_ {k = 1} ^ {K _ {j}} \left(\theta_ {d, j, k}\right) ^ {n _ {d, j, k}, *}\tag{5}
$$

where $n _ { d , j , k , \ast }$ represents the number of textual words corresponding to the label $j \in \varLambda _ { d }$ topic $k \in \{ 1 , 2 , . . . , K _ { j } \}$ in the document d and $n _ { d , j , k , \ast } =$ $\textstyle \sum _ { w = 1 } ^ { \mathbb { W } } n _ { d , j , k , w } . \ n _ { d , j , k , w }$ denotes the number of the textual word w gener ated by the label j’s topic $\mathfrak { k } \in \{ 1 , 2 , . . . , K _ { j } \}$ . The second part of Eq. (4) can be written as:

$$
p (z ^ {v} | l, \theta) = \prod_ {d = 1} ^ {M} \prod_ {i = 1} ^ {L _ {d}} p \left(z _ {d, i} ^ {v} \mid l _ {d, i}, \theta_ {d, l _ {d, i}}\right) = \prod_ {d = 1} ^ {M} \prod_ {i = 1} ^ {L _ {d}} \theta_ {d, l _ {d, i}, z _ {d, i} ^ {v}} = \prod_ {d = 1} ^ {M} \prod_ {j \in \Lambda_ {d}} \prod_ {k = 1} ^ {K _ {j}} (\theta_ {d, j, k}) ^ {m _ {d, j, k, *}}\tag{6}
$$

where $m _ { d , j , k , }$ represents the number of visual words corresponding to the label $j \in \varLambda _ { d }$ topic $k \in \{ 1 , 2 , . . . , K _ { j } \}$ in the document d and $m _ { d , j , k , \ast } =$ $\begin{array} { r l } {  { \sum _ { \nu = 1 } ^ { \mathbb { V } } m _ { d , j , k , \nu } . } } \end{array}$ Thus, can rewrite Eq. (4) into the following form:

$$
p (z ^ {w}, z ^ {v}, l | \alpha) = \prod_ {d = 1} ^ {M} \prod_ {j \in \Lambda_ {d}} \frac {\Delta \left(n _ {d , j , k , *} + m _ {d , j , k , *} + \alpha\right)}{\Delta (\alpha)}\tag{7}
$$

The assignment of textual words in document d is restricted to the set of observed label $\Lambda _ { d } .$ Using the above Equations, collapsed Gibbs sam pling formula for textual word w can be obtained:

Table 1 Statistics of the dataset.

<table><tr><td></td><td>Mean</td><td>Max</td><td>Min</td><td>Standard deviation</td></tr><tr><td>Number of words per document</td><td>168.01</td><td>1292</td><td>27</td><td>160.85</td></tr><tr><td>Number of images per document</td><td>5.09</td><td>44</td><td>2</td><td>5.67</td></tr><tr><td>Number of labels per document</td><td>1.94</td><td>6</td><td>1</td><td>1.04</td></tr></table>

position i of the document d. The $m _ { * _ { j , k , \nu } } ^ { - d , i }$ represents the number of the visual word v generated by the label j topic $k \in \{ 1 , 2 , . . . , K _ { j } \}$ , except for the current visual word at the position i of the document d. And $m _ { d , j , k , ^ { \prime } } ^ { - d , i }$ represents the number of visual words corresponding to the label $j \in$ $\varLambda _ { d }$ topic $k \in \{ 1 , 2 , . . . , K _ { j } \}$ in the document $d ,$ except for the current visual word at the position i of the document d.

After performing the collapsed Gibbs sampling algorithm until convergence, we can estimate the latent variable $\theta _ { d , j , k } ,$ and φ<sub>j,</sub> $k , \nu \dot { \cdot }$

$$
\theta_ {d, j, k} = \frac {n _ {d , j , k , ^ {*}} + m _ {d , j , k , ^ {*}} + \alpha}{\sum_ {k = 1} ^ {K _ {j}} \left(n _ {d , j , k , ^ {*}} + m _ {d , j , k , ^ {*}} + \alpha\right)}\tag{10}
$$

$$
\varphi_ {j, k, v} = \frac {m _ {* , j , k , v} + \beta^ {v}}{\sum_ {v = 1} ^ {\mathbb {V}} \left(m _ {* , j , k , v} + \beta^ {v}\right)}\tag{11}
$$

In addition, based on $\operatorname { E q . } \left( 8 \right)$ , we can determine topic assignments for each textual word. We define a parameter $\phi _ { j , \ k , \ w } $ which denotes the probability of textual word w belongs to topic k of label j. To simplify the calculation, we apply empirical estimation to measure $\phi _ { j , \ k , }$ <sub>w</sub>.

$$
\phi_ {j, k, w} = \frac {n _ {* , j , k , w}}{\sum_ {w = 1} ^ {\mathbb {W}} \left(n _ {* , j , k , w}\right)}\tag{12}
$$

where the notation $\begin{array} { r } { n _ { { ^ \ast } , j , k , w } = \sum _ { d = 1 } ^ { M } n _ { d , j , k , w } . } \end{array}$ As formulated above, we can obtain updated latent variables $\theta _ { d , j , k } , \varphi _ { j , k , \cdot }$ and $\phi _ { j , k , \ell }$ . We noted that the update rules of this sampler are similar to the Latent Dirichlet Allocation, with the constraint that only the topics corresponding to the document labels can be sampled. We can easily track the topic assign ments of the visual words and textual words via the Gibbs sampling algorithm, since every topic only takes part in a single label. We don’t need to allocate resources to record which label is assigned to each vi sual word or textual word. Thus, the proposed model has substantial

$$
p \Big (l _ {d, i} = j, z _ {d, i} ^ {w} = k | l _ {- d, i}, z _ {- d, i} ^ {w}, z ^ {v}, e _ {d, i} = e, v, \alpha , \xi \Big) \propto \mathbb {I} \big (j \in \Lambda_ {d} \wedge k = 1, 2,..., K _ {j} \big) \left(n _ {d, j, k, *} ^ {- d, i} + m _ {d, j, k, *} + \alpha\right) \ell_ {\delta_ {j, k} - E + 1} \Bigg (e | \mu_ {j, k}, \frac {\kappa_ {j , k} + 1}{\kappa_ {j , k}} \Sigma_ {j, k} \Bigg)\tag{8}
$$

where $\mathbb { I } ( \bullet )$ is the indicator function. The notation $n ^ { - d , }$ <sup>i</sup>denotes the corresponding count except for the current position i of the document d. And $n _ { d , j , k , } ^ { - d , i }$ represents the number of textual words corresponding to the label $j \in \Lambda _ { d }$ topic $k \in \{ 1 , 2 , . . . , K _ { j } \}$ in the document $d ,$ except for the current textual word at the position i of the document d.

Similarly, collapsed Gibbs sampling formula for visual word v can be obtained:

$$
\begin{array}{c} p \Big (l _ {d, i} = j, z _ {d, i} ^ {v} = k | l _ {- d, i}, z _ {- d, i} ^ {v}, z ^ {w}, v _ {\mathrm{d}, i} = v, e, \alpha , \beta^ {v} \Big) \propto \mathbb {I} \big (j \in \Lambda_ {d} \wedge k \\ = 1, 2,..., K _ {j} \big) \frac {m _ {* j , k , v} ^ {- d , i} + \beta^ {v}}{\sum_ {v = 1} ^ {\mathbb {V}} \left(m _ {* j , k , v} ^ {- d , i} + \beta^ {v}\right)} \Big (m _ {d j, k, *} ^ {- d, i} + n _ {d j, k, *} + \alpha \Big) \end{array}\tag{9}
$$

where $\boldsymbol { m } ^ { - d , ~ i }$ denotes the corresponding count except for the current computational advantages, especially on the dataset with more shared labels across documents. We give the process of the collapsed Gibbs sampling algorithm in Appendix D.

## 4. Experimental results

In this section, we validate the performance of our proposed model on a real-world dataset. We first describe our dataset and the preprocessing process for the raw data. Then, we give the selected com petitors for model comparison. Finally, we analyze the experimental results through quantitative evaluation and qualitative evaluation.

## 4.1. Data

We collect the dataset from the E-commerce platform Taobao to

Table 2

evaluate the performance of the proposed model. This dataset is related to marketer-generated contents. To collect the texts and their associated images, we implement a web crawler via the Java language. Due to the unstructured raw data, we perform a series of preprocessing steps to transform it into a structured format as input of the proposed model. First, we filter out the labels whose frequencies on the whole corpus are very low (<10) or very high (>500). Second, we remove the multimodal data with less than two images, one label, and 20 words in the textual content. Third, because there is no segmentation symbol in Chinese, we use a word segmentation tool (i.e., Jieba<sup>3</sup>) to process textual contents. Finally, we remove the noise information (e.g., stopwords) in textual contents to improve the performance of topic learning. We give the summary of our preprocessed dataset in Table 1. The dataset contains 12,157 multimodal documents, 59,084 images, and 122 unique labels. On average, each multimodal document consists of 168.01 words, 5.09 images, and 1.94 labels.

## 4.2. Baselines for comparison

To evaluate the performance, we compare the proposed model with several carefully selected alternative baselines. We organize these baselines into two categories: unsupervised and supervised topic models. The unsupervised topic models are the following:

LDA: LDA [11] model is one of the most classic methods in the field of topic learning. We apply the standard LDA model to extract the topics from the text descriptions in our dataset. And we use Gibbs sampling to infer the latent parameters, e.g., document-topic distribution.

G-LDA: G-LDA [49] is a variant of LDA, which assumes each docu ment is a collection of word embeddings, and each word embedding is drawn from multivariate Gaussian distributions. We use Gibbs sampling to infer the latent parameters.

Link-LDA: Similar to PLDA, Link-LDA [50] is a mixed-membership model for documents consisting of abstracts and references. We use this model for the task of multi-modal data analysis, which treats the text descriptions and visual information as words and references in the framework of Link-LDA. In addition, we apply the Gibbs sampling to learn the latent parameters.

Corr-LDA: Corr-LDA [10] is a multimodal topic model that can build the correspondences between images and text modalities. We use text descriptions and visual information as input of Corr-LDA to detect topics. Different from Link-LDA, this model first generates the visual words and subsequently generates textual words. We apply variational inference to learn the latent parameters.

The supervised topic models are the following:

L-LDA: L-LDA [15] can build the one-to-one relationship between label and topic. The input of this model is text descriptions and their corresponding labels. We use Gibbs sampling to learn the latent pa rameters of this model.

sLDA: The sLDA [12] introduces a response variable for each docu ment and uses the generalized linear model to generate this response variable. This model assumes that each document is endowed with a single response label (or rating), which is inapplicable to a multi-label setting. To run this model, we thus select only one label for each document based on the frequency of this label in the whole corpus. We use variational inference to learn the latent parameters.

PLDA: PLDA [16] is used to model documents and their related label information, simultaneously. This model can infer latent topic structure within the scope of observed labels. We use Gibbs sampling to learn the latent parameters of this model.

LB-MMT-BOW: This model is a variant of LB-MMT, which replaces the word embedding in the LB-MMT model with the bag of words (BOW). Similar to LDA, LB-MMT-BOW assumes that a topic is a multi nomial distribution over a fixed vocabulary of words. We use Gibbs sampling to learn the latent parameters of this model.

To achieve a fair comparison, we tune the hyperparameter values of all models. We empirically set the hyperparameters $\beta ^ { \nu } = 0 . 0 1 _ { \mathrm { { : } } }$ , and ${ \mathfrak { Q } } =$ 50/K for our proposed model. The hyperparameter ρ is set to the mean of all the word embeddings, δ to the number of dimensions of the word embeddings, and ψ to an identity matrix. Because our model supports latent sub-topics within a given label, we thus choose the hyper parameters $K _ { l } = 2$ for labels. For LDA and L-LDA, we set the hyper parameters $\begin{array} { r } { \ a = \ 5 0 / K , } \end{array}$ and $\beta ~ = ~ 0 . 0 1$ . For G-LDA, we set the hyperparameters α = 50/K, and other hyperparameters for multivariate Gaussian distribution are the same as our model settings. For Link-LDA and Corr-LDA, we set the hyperparameters $\alpha = 5 0 / K , \beta ^ { w } = \beta ^ { \nu } = 0 . 0 1$ . For sLDA, we set $\mathfrak { a } = 5 0 / K .$ . For PLDA, we set the hyperparameters $\alpha = 5 0 / K ,$ $\beta = 0 . 0 1$ , and the size of the sub-topics under each label $K _ { l } = 2 .$ . For LB-MMT-BOW, we set $\beta ^ { w } = 0 . 0 1$ and other hyperparameters are the same as our model settings. We implement the proposed model by Java language and run it on an Ubuntu 16.04 (GNU/Linux) server.

## 4.3. Topic coherence

The objective of this research is to learn the topic by using the method of probability topic model in the given data of associated text and images with labels. To measure the quality of topics learned from the topic model, we use a metric, namely topic coherence [51,52]. Topic coherence is considered to be an important measure of human under standing of the latent topics learned. Significantly, the superiority of this metric is that its value is evaluated over the original corpus used to train the topic models, rather than an external corpus. We apply the following equation to calculate topic coherence scores.

$$
\mathrm{C} \left(t, W ^ {(t)}\right) = \sum_ {m = 2} ^ {M} \sum_ {l = 1} ^ {m - 1} \log \frac {D \left(w _ {m} ^ {(t)} , w _ {l} ^ {(t)}\right) + \epsilon}{D \left(w _ {l} ^ {(t)}\right)}\tag{13}
$$

where $D ( w )$ denotes the document frequency of the word type w, $D ( w ,$ w<sup>′</sup>) denotes the number of times w and w<sup>′</sup> appearing together in a document. $\boldsymbol { W } ^ { ( t ) } = ( w _ { 1 } ^ { ( t ) } , w _ { 2 } ^ { ( t ) } , . . . , w _ { M } ^ { ( t ) } )$ denotes the top M words with the highest frequency under the topic t. In order to guarantee that the score yields a real number, we introduce a smoothing factor ϵ and set it to 0.1. We use the average coherence scores over all topics to evaluate the overall quality of topic models:

$$
A v g (c) = \frac {\sum_ {t = 1} ^ {K} C \big (t , w ^ {(t)} \big)}{K}\tag{14}
$$

Better topic quality is indicated by a higher value of Avg(c). To measure Avg(c), we run five experiments for each topic model on our dataset by fixing the number of words as 5, 10, 15, and 20, respectively. Table 2 displays the results. As shown in Table 2, we can see that G-LDA performs better than LDA, which shows using word embedding can improve topic learning. Corr-LDA and Link-LDA significantly outper form LDA $\bar { ( p < } 1 0 ^ { - 3 } )$ , which means considering text descriptions and visual information jointly can significantly improve topic learning. Compared to LDA and G-LDA, we note that the supervised topic models (i.e., L-LDA, sLDA, PLDA, and LB-MMT-BOW) improve a lot, which demonstrates the joint analysis of text and labels can help the topic learning. LB-MMT-BOW achieves the second-best performance, which shows leveraging the texts and associated images with labels can detect more valuable topics. The proposed model LB-MMT significantly out performs the state-of-the-art baseline methods, which means our model can identify more prominent and coherent topics. Compared to LB-MMT-BOW, the proposed LB-MMT model introduces word embed dings to ehance topic learning.

The average coherence scores compared with other models.

<table><tr><td></td><td>Number of words</td><td>M = 5</td><td>M = 10</td><td>M = 15</td><td>M = 20</td></tr><tr><td rowspan="4">Unsupervised topic model</td><td>LDA</td><td>-27.6</td><td>-134.0</td><td>-336.5</td><td>-622.7</td></tr><tr><td>G-LDA</td><td>-19.0</td><td>-102.4</td><td>-260.3</td><td>-489.6</td></tr><tr><td>Link-LDA</td><td>-18.8</td><td>-99.2</td><td>-242.6</td><td>-496.7</td></tr><tr><td>Corr-LDA</td><td>-19.1</td><td>-102.8</td><td>-257.9</td><td>-504.3</td></tr><tr><td rowspan="4">Supervised topic model</td><td>L-LDA</td><td>-18.5</td><td>-97.6</td><td>-243.5</td><td>-468.7</td></tr><tr><td>sLDA</td><td>-18.7</td><td>-98.5</td><td>-246.7</td><td>-475.3</td></tr><tr><td>PLDA</td><td>-18.4</td><td>-96.5</td><td>-231.7</td><td>-463.3</td></tr><tr><td>LB-MMT-BOW</td><td>-11.7</td><td>-62.1</td><td>-165.9</td><td>-335.8</td></tr><tr><td>Our approach</td><td>LB-MMT</td><td>-10.3</td><td>-56.0</td><td>-156.4</td><td>-315.6</td></tr></table>

## 4.4. Label classification

Following the prior work [53], we first use the proposed model and the baseline methods to extract latent topics and represent documenttopic distributions to construct new variables, and subsequently, these variables are as input into a deep learning method for the multi-label classification task. Specifically, we randomly select a set of multi modal documents to train the LB-MMT model. In this process, the label information serves as supervision signals to control the topic assign ments. Then, based on the observable data (i.e., visual words and textual words), we can easily infer document-topic distributions for new multimodal documents, similar to previous studies [54,55].

For the classification task, we select the Deep & Cross network (DCN) method [56], which can jointly train feed-forward neural networks with document-topic distributions and linear models with feature trans formations for label classification. The superiority of this deep learning model is that it can capture feature interactions, thus bringing additional improvement for label classification. Fig. 7 gives the framework of the DCN method. In addition, we randomly split the dataset into a training set (80%), a test set (10%), and a validation set (10%).

To evaluate the performance of the classification with different topic models, we adopt two different evaluation metrics: average Precision@N and Recall@N. For the robust comparison, we run the DCN method five times based on the document-topic distributions of our proposed model and each baseline. The higher the values of Precision@N and Recall@N indicate better classification results. Fig. 8 shows the comparison results. We find consistently, the proposed model (LB-MMT) achieves a better performance than other comparison methods over these two metrics. This suggests that our model is reasonable to explicitly model the mapping between multimodal topics and labels. In contrast with LB-MMT, LB-MMT-BOW achieves the second-best performance, which re veals that introducing word embedding learned by BERT can obtain more discriminated topics for label classification. In addition, we note that the improvements of LB-MMT and LB-MMT-BOW over PLDA are significant $( p < 0 . 0 1 )$ by using a paired t-test.

To analyze the impact of introducing images into the topic model, Table 3 gives the case studies of label predictions by LB-MMT and PLDA. As shown in this table, we give the ground-truth labels as references and list the top-3 highest-scoring predicted labels for the LB-MMT and PLDA. And we mark the correct predictions in blue and incorrect predictions in red. It is clear that our approach produces higher quality results than PLDA.

## 4.5. Robustness analysis

To evaluate the stability of the proposed model, we conduct robustness analysis. To this end, we first verify the impact of different word embed ding methods on the model performance. We compare the experimental results with GloVe [57], Word2Vec [58] and BERT. For a fair comparison, the word embedding size of these three methods is all set to 768. The performance of each model is assessed by topic coherence scores. Table 4 shows the performance comparisons on these word embedding methods. We find that LB-MMT with GloVe performs similarly to LB-MMT (Word2Vec). Although the overall performances of the proposed model with BERT are better than that with GloVe and Word2Vec, the improve ment is not very significant $( p < 0 . 1 )$ by using a paired t-test.

Although SIFT is among the most prevalent and influential image representation methods, it still needs to be compared with alternative algorithms to investigate whether this method is suitable for our image data. To achieve this goal, we employ two robust algorithms, namely ORB [59], and SURF [60] as the alternatives, to extract feature (or descriptor) for each image patch. Based on these features, we use the K-Means to construct visual vocabulary and then obtain representations for all images. We set the number of visual vocabulary to 900. Table 5 reports the comparative results with ORB, SURF, and SIFT. We find that LB-MMT with SIFT performs better than that with SURF and ORB. We

![](/api/attachments/V42W9RES/fulltext/images/7b3e12c0f301fd42e5308ee848d7d67aeaede51c42e90ffd09c3e4e7ba420a0b.jpg)  
Fig. 7. The Deep & Cross network method for label prediction.

![](/api/attachments/V42W9RES/fulltext/images/68dceebd78d36b0e0c4466ff46c432924478ece10c99ab1fb3256173fe93d7c7.jpg)

![](/api/attachments/V42W9RES/fulltext/images/c86218b5bfd202dcd4ffe6f6addb5ed0937ca13f2747c9e943ec8f71c7774323.jpg)  
Fig. 8. The results of the Label classification.

Table 3  
Prediction results with six randomly selected samples.

<table><tr><td>Index</td><td>True label</td><td>PLDA</td><td>LB-MMT</td><td colspan="2">Image</td></tr><tr><td>1</td><td>Retro/Japanese/Autumn-winter</td><td>Japanese/Literary/Autumn-winter</td><td>Autumn-winter/Retro/Japanese</td><td><img src="/api/attachments/V42W9RES/fulltext/images/83bdb80bde5ebfe24e34176ad9d989b5525100de146ea0178e70792d7b96511a.jpg"/></td><td></td></tr><tr><td>2</td><td>Board shoes/Men&#x27;s shoe</td><td>Board shoes/Men&#x27;s shoe/Jeans</td><td>Board shoes/Men&#x27;s shoes/Manly</td><td><img src="/api/attachments/V42W9RES/fulltext/images/b53049d7e4a2309bb1d1355305c91cee96fa9cc90a14ffadd8793ba3e6925ad1.jpg"/></td><td></td></tr><tr><td>3</td><td>Original/Loose/Coat/</td><td>Original/Coat/Casuals</td><td>Coat/Loose/Original</td><td><img src="/api/attachments/V42W9RES/fulltext/images/803377e2f61892d7d4d6e4801dde556b2ac2da2fa87390ef125ee3e43732b2a8.jpg"/></td><td></td></tr><tr><td>4</td><td>Sweet/Fresh/Playful</td><td>Fresh/Sexy/Sweet</td><td>Fresh/Playful/Sweet</td><td><img src="/api/attachments/V42W9RES/fulltext/images/df800240fd7c536cbf5cf4c79694e05d0e93c564eb29ed4da1a39af0b35eede9.jpg"/></td><td></td></tr><tr><td>5</td><td>Shoulder-bag/Sweet/Delicate</td><td>Delicate/Shoulder-bag/Generous</td><td>Delicate/Sweet/Shoulder-bag</td><td><img src="/api/attachments/V42W9RES/fulltext/images/1d19ce2402bfa56bd71cfc177facb84ff671170c911b6e7d8e1a3c20b7d5b972.jpg"/></td><td></td></tr><tr><td>6</td><td>Sweater</td><td>Sweater/Sweatpants/Autumn-winter/</td><td>Sweater/Leisure/Autumn-winter/</td><td><img src="/api/attachments/V42W9RES/fulltext/images/bbc631bfdde7d365ef907220bfa148c828ed33c680c77ca0432d935d42207cba.jpg"/></td><td></td></tr></table>

Table 4  
Performance comparisons on different word embedding methods.

<table><tr><td>Number of words</td><td>M = 5</td><td>M = 10</td><td>M = 15</td><td>M = 20</td></tr><tr><td>LB-MMT (GloVe)</td><td>-10.1</td><td>-59.2</td><td>-165.7</td><td>-320.5</td></tr><tr><td>LB-MMT (Word2Vec)</td><td>-10.2</td><td>-58.3</td><td>-162.4</td><td>-325.8</td></tr><tr><td>LB-MMT (BERT)</td><td>-10.3</td><td>-56.0</td><td>-156.4</td><td>-315.6</td></tr></table>

suggest that SIFT has stable and good performance in keypoints detec tion, compared with the other two alternatives. This is possible because that SURF and ORB are not good at processing images with varying intensity and color composition values [61].

Table 5  
Performance comparisons for different image features.

<table><tr><td>Number of words</td><td>M = 5</td><td>M = 10</td><td>M = 15</td><td>M = 20</td></tr><tr><td>LB-MMT (ORB)</td><td>-11.8</td><td>-65.9</td><td>-175.6</td><td>-350.4</td></tr><tr><td>LB-MMT (SURF)</td><td>-11.3</td><td>-63.2</td><td>-168.7</td><td>-330.6</td></tr><tr><td>LB-MMT (SIFT)</td><td>-10.3</td><td>-56.0</td><td>-156.4</td><td>-315.6</td></tr></table>

## 4.6. Qualitative analysis of multimodal topics

We further study the content of the multimodal topics for qualitative analysis. Because of the space limitation, we randomly select four labels with eight topics in our results for visualization. The LB-MMT model yields distributions of textual words and visual words for each topic. Based on these probabilities, we can easily obtain how likely a given textual word or visual word assigns to that topic. We use these proba bilities to rank the words and images in each topic. For each topic of labels, we present its 10 most probable words and 5 images in Fig. 9.

![](/api/attachments/V42W9RES/fulltext/images/c271a7d4200a5dc5ec6b6c9d0a20d3ae8ae0ac1c813ff669d1a167f169087f3a.jpg)  
Fig. 9. Examples of multimodal topics.

From Fig. 9, we note that our model can yield a one-to-many rela tionship between labels and multimodal topics. Under the constraints of labels, it is very interesting to see how certain textual words and images congregate to form meaningful and interpretable multimodal topics. For example, in Fig. 9 (a), topic 9 is about the appearance of the sweater, since textual words “turtleneck." “loose." “pullover." and “slim” allow people to quickly sketch what a sweater looks like. This is also confirmed by the images on topic 9. Interestingly, topic 10 talks about fashion compatibility for the sweater, as evidenced by the use of words such as “casual pants,” “matching,” “shoes” and “bag.” We found that although these two topics belong to the same label (i.e., sweater), there are obvious differences in the content described. In Fig. 9 (b), we note topic 29 contains the words “retro,” “niche” and “minimalist style,” and topic 29 contains the words “latest products,” “fashion” and “celebrity.” While the textual words and images in topic 29 and topic 30 both focus on describing the style of the crossbody bag, the former is related to the niche retro style, and the latter is related to the popular style of celeb rities. These results not only reflect the public opinion trend of market products, but also help marketers to analyze the style of their products. In Fig. 9 (c), topic 41 is concerned with stilettos, as evidenced by the use of words such as “fine-heels” and “pointy.” From the textual words and images in topic 42, we find this topic is associated with fashion compatibility for stilettos. Similarly, topic 73 is about the material of the bedding (e.g., “100% cotton,” “coral fleece,” and “down cotton”) and topic 74 is about the style of the bedding (e.g., “Nordic style,” “Ins style” and “Curtain”). According to the above analysis, we conclude that our model can generate deep qualitative insights into how multimodal data is organized under the constraints of labels.

## 4.7. Practical implication

The spread of the Internet and mobile applications have led to large scale multimodal information posted by users online through media, e. g., Taobao and Amazon. This paper contributes to providing a powerful framework for discovering interesting patterns from these multimodal data. The results of this study provide several important practical implications.

First, marketers in online platforms (e.g., Taobao) may take advan tage of our results to design more attractive multimodal contents that can influence consumer attention and promote consumers’ purchase intentions. For example, the proposed framework provides a reliable and reasonable way to extract meaningful features (i.e., multimodal topics) from the large-scale multimodal data. For a product to be promoted, marketers can easily retrieve the related tags, textual topics, and images through the model results. This information makes it possible for mar keters to quickly track market dynamics, and further determine which labels, textual descriptions, and pictures may improve their campaign

performance.

Second, online platforms can apply our results to actively monitor the multimodal contents, which is better gain the business points and optimize their search engine. For example, for sweaters, the platform can have close to perfect insight into which styles and designs are the most popular at present, and which clothes can match with products. This enables the platform to provide consumers with better services, not only recommending popular products for consumers, but also giving advice on outfit matching. In addition, our method can clearly build the relationship between tags and their textual contents and images. The online platforms take into account these results to optimize search en gines to match target consumers’ search interests.

## 5. Conclusion

In this study, we propose a new probabilistic topic model called the label-based multimodal topic (LB-MMT) model for the analysis of multimodal data in social media. The LB-MMT model integrates labels, textual and visual information into a unified framework to explore latent topics in data space. Different from other works, we use the labels as supervised signals to generate the text and image data. And we assume that the textual words and visual words related to each text and image are drawn from a mixture of latent multimodal topics. We conduct extensive experiments using a real-world dataset to validate the effec tiveness of the proposed model. The results of the experiment demon strate that the LB-MMT model outperforms all the baselines in quantitative evaluations, and yields several interesting insights regarding multimodal topics.

We close by highlighting broad areas for future research. First, future research may use deep learning methods (e.g., pre-trained VGG-16 CNNs) to extract the image features, and design a new model for fitting image data. Second, our proposed modeling framework does not consider the label irrelevant information in textual contents and images. As a future direction, we can introduce new latent variables to filter out the irrelevant information related to labels. Third, in this study, we focus on detecting multimodal topics based on social media data. Future research would be to build a new model that uses the multimodal topics learned by our model in other areas, e.g., predicting the popularity of contents on social media.

## CRediT authorship contribution statement

Hao Li: Idea, Experiment. Yang Qian: Idea, Writing the manuscript. Yuanchun Jiang: Design of the study, Final proofreading. Yezheng Liu: Design of the study, Final proofreading. Fan Zhou: Experiment, Result analysis.

## Declaration of Competing Interest

The authors certify that there is no conflict of interest in the subject matter discussed in the manuscript.

## Data availability

Data will be made available on request.

## Acknowledgment

We appreciate the constructive comments from the anonymous re viewers. This work is supported by the National Natural Science Foun dation of China (72101072, 72171071, 91846201), the China Postdoctoral Science Foundation (2021M690852), the Fundamental Research Funds for the Central Universities (JZ2022HGTB0282, JZ2021HGQB0272), and the National Engineering Laboratory for Big Data Distribution and Exchange Technologies.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi. org/10.1016/j.dss.2022.113863.

## References

[1] Y. Ma, J. Jia, S. Zhou, J. Fu, Y. Liu, Z. Tong, Towards better understanding the clothing fashion styles: A multimodal deep learning approach, in: Thirty-First AAAI Conference on Artificial Intelligence, 2017.

[2] A. Salah, Q.-T. Truong, H.W. Lauw, Cornac: a comparative framework for multimodal recommender systems, J. Mach. Learn. Res. 21 (2020) 91–95.

[3] Y. Zeng, D. Cao, X. Wei, M. Liu, Z. Zhao, Z. Qin, Multi-modal relational graph for cross-modal video moment retrieval, in, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). 2021. pp. 2215–2224.

[4] W. Zhang, W. Wang, J. Wang, H. Zha, User-guided hierarchical attention network for multi-modal social image popularity prediction, in: Proceedings of the 2018 World Wide Web Conference, 2018, pp. 1277–1286.

[5] Y. Ma, J. Jia, S. Zhou, J. Fu, Y. Liu, Z. Tong, Towards Better Understanding th Clothing Fashion Styles: A Multimodal Deep Learning Approach, 2017.

[6] K. Sohn, W. Shang, H. Lee, Improved multimodal deep learning with variation of information, in: Proceedings of the 27th International Conference on Neura Information Processing Systems Volume 2, 2014, pp. 2141–2149.

[7] N. Srivastava, R. Salakhutdinov, Learning representations for multimodal data with deep belief nets, in: International Conference on Machine Learning Workshop, 2012.

[8] Y.C. Chen, K.T. Lai, D. Liu, M.S. Chen, TAGNet: triplet-attention graph networks for hashtag recommendation, in: IEEE Transactions on Circuits and Systems for Video Technology, 2021.

[9] Y. Zheng, Y. Zhang, H. Larochelle, Topic modeling of multimodal data: An autoregressive approach, in: IEEE Conference on Computer Vision and Pattern Recognition 2014, 2014, pp. 1370–1377.

[10] D.M. Blei, M.I. Jordan, Modeling annotated data, in: Proceedings of the 26th Annual International ACM SIGIR Conference on Research and Development in Informaion Retrieval, 2003, pp. 127–134.

[11] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, J. Mach. Learning Res. 3 (2003) 993–1022.

[12] D.M. Blei, J.D. McAuliffe, Supervised topic models, in: Proceedings of the 20th International Conference on Neural Information Processing Systems. 2007.

[13] S. Lacoste-Julien. F. Sha. M.J. Jordan. DiscLDA: discriminative learning for dimensionality reduction and classification. in: Proceedings of the 21st International Conference on Neural Information Processing Systems, 2008. pp. 897–904.

[14] J. Zhu. A. Ahmed. E.P. Xing, MedLDA: Maximum Margin Supervised Topic Models

[15] D. Ramage, D. Hall, R. Nallapati, C.D. Manning, Labeled LDA: a supervised topic model for credit attribution in multi-labeled corpora, in: Proceedings of the 200g Conference on Empirical Methods in Natural Language Processing: Volume 1 Volume 1, 2009, pp. 248–256.

[16] D. Ramage, C.D. Manning, S. Dumais, Partially labeled topic models for interpretable text mining, in, in: Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2011 pp. 457–465.

[17] P. Zhang, S. Wang, D. Li, X. Li, Z. Xu, Combine topic modeling with semantic embedding: embedding enhanced topic model, IEEE Trans. Knowl. Data Eng. 32 (2019) 2322–2335

[18] H. Xu, W. Wang, W. Liu, L. Carin, Distilled wasserstein learning for word embedding and topic modeling, Adv. Neural Inf. Proces. Syst. 31 (2018).

[19] X. Chen, H. Chen, H. Xu, Y. Zhang, Y. Cao, Z. Qin, H. Zha, Personalized fashion recommendation with visual explanations based on multimodal attention network: Towards visually explainable recommendation, in: Proceedings of the 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval, 2019, pp. 765–774.

[20] R. Ma, X. Qiu, Q. Zhang, X. Hu, Y.-G. Jiang, X. Huang, Co-attention memory network for multimodal microblog’s hashtag recommendation, IEEE Trans. Knowl. Data Eng, 33 (2019) 388–400.

[21] J. Ni. Z. Huang. Y. Hu. C. Lin. A two-stage embedding model for recommendation with multimodal auxiliary information. Inf. Sci. 582 (2022) 22–37.

[22] J. Lv, W. Liu, M. Zhang, H. Gong, B. Wu, H. Ma, Multi-feature fusion for predicting social media popularity, in: Proceedings of the 25th ACM international conference on Multimedia, 2017, pp. 1883–1888.

[23] Y. Li, Y. Xie, Is a picture worth a thousand words? An empirical study of image

[24] M. Kan, S. Shan, H. Zhang, S. Lao, X. Chen, Multi-view discriminant analysis, IEEE Trans, Pattern Anal, Mach, Intell, 38 (2016) 188–194.

[25] X. Zhai, Y. Peng, J. Xiao, Learning cross-media joint representation with sparse and Semisupervised regularization, IEEE Transact, Circ. Syst. Video Technol. 24 (2014) 965-978.

[26] C. Deng, Z. Chen, X. Liu, X. Gao, D. Tao, Triplet-based deep hashing network fo cross-modal retrieval, JEEE Trans, Image Process. 27 (2018) 3893–3903.

[27] P. Hu, D. Peng, Y. Sang, Y. Xiang, Multi-view linear discriminant analysis network, IEEE Trans. Image Process. 28 (2019) 5352–5365.

[28] Y. Qian, W. Xu, X. Liu, H. Ling, Y. Jiang, Y. Chai, Y. Liu, Popularity prediction for marketer-generated content: a text-guided attention neural network for multimodal feature fusion, Inf. Process. Manag. 59 (2022), 102984.

[29] M. Zihayat, A. Ayanso, X. Zhao, H. Davoudi, A. An, A utility-based news recommendation system, Decis, Support, Syst, 117 (2019) 14–27

[30] D. Slof, F. Frasincar, V. Matsiiako, A competing risks model based on latent Dirichlet allocation for predicting churn reasons, Decis. Support. Syst. 146 (2021), 113541.

[311 X. Cheng, X. Yan. Y. Lan. J. Guo. Btm: topic modeling over short texts, JEEE Trans. Knowl. Data Eng. 26 (2014) 2928–2941.

[32] L. Cao, L. Fei-Fei, Spatially coherent latent topic model for concurrent segmentation and classification of objects and scenes, in: 2007 IEEE 11th International Conference on Computer Vision, IEEE, 2007, pp. 1–8.

[33] D. Putthividhy, H.T. Attias, S.S. Nagarajan, Topic regression multi-modal Latent Dirichlet Allocation for image annotation, in: 2010 IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 2010, pp. 3408–3415.

[34] F. Xue, R. Hong, X. He, J. Wang, S. Qian, C. Xu, Knowledge-based topic model for multi-modal social event analysis, IEEE Transact. Multimedia 22 (2020) 2098-2110.

[35] Y. Yang, K. Zhang, Y. Fan, sDTM: a supervised Bayesian deep topic model for text analytics, Inf. Syst. Res. (2022) 1–20.

[36] X. Wang, Y. Yang, Neural topic model with attention for supervised learning, in: Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics, 2020, pp. 1147–1156.

[37] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, Bert: Pre-training of deep bidirectional transformers for language understanding, Proceedings of NAACL-HLT (2019) 4171–4186.

[38] W. Liu, T. Xu, Q. Xu, J. Song, Y. Zu, An encoding strategy based word-character LSTM for Chinese NER, in: Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), 2019, pp. 2379–2389.

[39] H. Kato, T. Harada, Image reconstruction from bag-of-visual-words, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2014, pp. 955–962.

[40] J. Yang, Y.-G. Jiang, A.G. Hauptmann, C.-W. Ngo, Evaluating bag-of-visual-words representations in scene classification, in: Proceedings of the Internationa Workshop on Workshop on Multimedia Information Retrieval, 2007, pp. 197–206.

[41] B. Fernando, E. Fromont, D. Muselet, M. Sebban, Discriminative feature fusion for image classification, in: IEEE Conference on Computer Vision and Pattern Recognition 2012, 2012, pp. 3434–3441.

[42] D.G. Lowe, Distinctive image features from scale-invariant keypoints, Int. J.

[43] Q. Wang, B. Li, P.V. Singh, Copycats vs. original mobile apps: a machine learning copycat-detection method and empirical analysis, Inf. Syst. Res. 29 (2018) 273-291.

[44] Z. Jiang, Y. Huang, D.R. Beil, The role of feedback in dynamic crowdsourcing contests: a structural empirical analysis. Manag, Sci. 68 (7) (2022) 4858–4877.

[45] X. Yang, L. Hou, Y. Zhou, W. Wang, J. Yan, Dense label encoding for boundary on Computer Vision and Pattern Recognition, 2021, pp. 15819–15829.

[46] Z. Ying, H. Niu, P. Gupta, D. Mahajan, D. Ghadiyaram, A. Bovik, From patches to pictures (PaQ-2-PiQ): Mapping the perceptual space of picture quality, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020, pp. 3575–3585.

[47] P. Majumdar, S. Mittal. R. Singh, M. Vatsa, Unravelling the effect of image distortions for biased prediction of pre-trained face recognition models, in: Proceedings of the IEEE/CVF International Conference on Computer Vision, 2021. pp. 3786–3795.

[48] D. Ramage, D. Hall, R. Nallapati, C.D. Manning, Labeled LDA: A supervised topic model for credit attribution in multi-labeled corpora, in: Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing, 2009, pp. 248–256.

[49] R. Das, M. Zaheer, C. Dyer, Gaussian LDA for topic models with word embeddings, in, in: Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), 2015, pp. 795–804.

[50] E. Erosheva, S. Fienberg, J. Lafferty, Mixed-membership models of scientifi publications, Proc. Natl. Acad. Sci. 101 (2004) 5220–5227.

[51] Z. Chen, B. Liu, Mining topics in documents: Standing on the shoulders of big data, in: Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 2014. pp. 1116–1125

[52] D. Mimno, H. Wallach, E. Talley, M. Leenders, A. McCallum, Optimizing semantic coherence in topic models, in: Proceedings of the 2011 Conference on Empirical Methods In Natural Language Processing, 2011, pp. 262–272.

[53] J. Zhu, A. Ahmed, E.P. Xing, MedLDA: maximum margin supervised topic models, J. Mach. Learning Res. 13 (2012) 2237–2278

[54] Y. Feng, M. Lapata, Topic models for image annotation and text illustration, in: Human Language Technologies: The 2010 Annual Conference of the North American Chapter of the Association for Computational Linguistics, 2010, pp. 831–839.

[55] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, J. Mach. Learn. Res. 3 (2003) 993–1022.

[56] R. Wang, B. Fu, G. Fu, M. Wang, Deep & cross network for ad click predictions, in: Proceedings of the ADKDD'17. 2017. Article 12.

[57] J. Pennington, R. Socher, C.D. Manning, Glove: Global vectors for word representation, in: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2014, pp. 1532–1543.

[58] T. Mikolov, I. Sutskever, K. Chen, G.S. Corrado, J. Dean, Distributed representations of words and phrases and their compositionality, Adv. Neural Inf. Proces. Syst. 26 (2013).

[59] E. Rublee, V. Rabaud, K. Konolige, G. Bradski, ORB: An efficient alternative to SIFT or SURF, in: 2011 International Conference on Computer Vision, 2022

[60] H. Bay, T. Tuytelaars, L.V. Gool, Surf: Speeded up robust features, in: European Conference on Computer Vision, Springer, 2006, pp. 404–417.

[61] E. Karami, S. Prasad, M. Shehata, Image matching using SIFT, SURF, BRIEF and ORB: performance comparison for distorted images, The 24th Annua Newfoundland Electrical and Computer Engineering Conference, NECEC (2015 arXiv:1710.02726.

Hao Li is working toward a Master’s degree in Management Science and Engineering from the Hefei University of Technology. He received his bachelor’s degree from Hefei Uni versity of Technology. His research interests include machine learning and data mining, and visual marketing.

Yang Qian is a postdoctoral fellow at the School of Management, Hefei University of Technology. He received his Ph.D. in Management Science and Engineering from Hefei University of Technology in 2020. His research interests include electronic commerce online marketing, and machine learning. His work has appeared in journals including European Journal of Operational Research, ACM Transactions on Knowledge Discovery from Data. Information Processing & Management. and World Wide Web

Yuanchun Jiang is a professor at School of Management, Hefei University of Technology, China. He received his Ph.D. in Management Science and Engineering from Hefei Uni versity of Technology, Hefei, China. He teaches electronic commerce, business intelligence and business research methods. His research interests include online marketing, electronic commerce and data mining. He has published papers in journals such as Marketing Science, European Journal of Operational Research, Decision Support Systems, and IEEE Transactions on Dependable and Secure Computing.

Yezheng Liu is a professor of Electronic Commerce at Hefei University of Technology, China. He received his Ph.D. in Management Science and Engineering from Hefei University of Technology in 2001. His main research interests include decision science electronic commerce, intelligent decision support systems and data mining. His work has appeared in journals including Marketing Science, IEEE Transaction on Software Engineering, Information Sciences, and ACM Transactions on Information Systems.

Fan Zhou is working toward a Master’s degree in Management Science and Engineering from the Hefei University of Technology. She received her bachelor’s degree from Hefe University of Technology. Her research interests include machine learning and text mining.
