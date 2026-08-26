---
otero_id: 20385
otero_key: "84WFPFZN"
title: "Predicting product adoption intentions: An integrated behavioral model-inspired multiview learning approach"
authors: "Zhu Zhang; Xuan Wei; Xiaolong Zheng; Daniel Dajun Zeng"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103484"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting product adoption intentions: An integrated behavioral model-inspired multiview learning approach

Zhu Zhang <sup>a,b,1</sup>, Xuan Wei <sup>c,1</sup>, Xiaolong Zheng <sup>a,d,\*</sup>, Daniel Dajun Zeng <sup>a,b,d</sup>

<sup>a</sup> State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China

<sup>b</sup> Shenzhen Artificial Intelligence and Data Science Research Institute (Longhua), Shenzhen 518129, China

<sup>c</sup> Department of Information, Technology and Innovation, Antai College of Economics and Management, Shanghai Jiao Tong University, Shanghai 200030, China

<sup>d</sup> School of Artificial Intelligence, University of Chinese Academy of Sciences, Beijing 101408, China

## A R T I C L E I N F O

Keywords: Text mining Deep learning Product adoption intention Multi-view learning

## A B S T R A C T

Mining product adoption intentions from social media could provide insights for many business practices, such as social media marketing. Existing methods mainly focus on text information but overlook other types of data. In light of the Integrated Behavioral Model (IBM), in this study, we argue that it is valuable to consider users’ social connections in addition to postings for identifying product adoption intentions. Based on this rationale, we propose a novel multiview deep learning framework to identify product adoption intentions. Extensive experi ments show our proposed approach is effective, and demonstrate the benefit of incorporating social network information for intention identification

## 1. Introduction

Currently, online users are generating massive social media postings. For example, more than 500 million tweets are posted on Twitter<sup>2</sup> each day. Some of these postings are often encoded with users’ intentions on product adoption [1]. For instance, the expression “I want to try iPhone X” indicates the intention to adopt an iPhone X; a user with the intention to adopt a Nintendo Switch may post “Nintendo Switch is coming soon! So exciting!" Mining such adoption intentions from social media could benefit many business applications such as social media marketing [2, 3]. In this paper, we consider this problem as a machine learning task and focus on designing a novel technical approach to identify whether a posting’s author has the intention to adopt a specific product.

Mining adoption intentions from social media data faces many challenges. First, intentions could be expressed in an implicit way. Previous studies show that there are two categories of intentions, i.e., explicit intentions and implicit intentions [4]. Explicit expressions directly show one’s needs and desires, often with obvious signals such as intention keywords. Implicit expressions usually require logical reasoning based on the context in order to know the authors’ intentions. In the previous examples, “I want to try iPhone X” explicitly shows a product adoption intention, and “Nintendo Switch is coming soon! So exciting!” is an example of implicit expression. Identifying implicit in tentions is much harder than recognizing explicit intentions because of the lack of obvious signals (e.g., syntactic patterns) [1]. Second, social media postings are often short and contain lots of typos, symbols, hashtags, URLs, and informal expressions. Such noise in expressions makes it more difficult to understand social media postings’ semantics that is clear for humans. Hence, it is necessary to design advanced ap proaches to tackle this challenge.

Researchers have proposed many methods to solve this problem, with recent efforts focused on Deep Neural Networks (DNNs) [1,2,5], as DNNs have achieved leading performance across an array of Natural Language Processing (NLP) tasks [6]. However, existing methods mainly rely on the text content for this problem, which is not sufficient, particularly when the posting is too short or its expression is vague.

In this paper, we focus on the research question of how to identify whether a posting’s author has the intention to adopt a specific product on social media when we have a set of postings and social connections of the postings’ authors. Motivated by the Integrated Behavioral Model (IBM) theory [7], we argue it is necessary to take into account social network information in addition to text information for the identifica tion of product adoption intentions. The IBM theory states that there are three determinants of intention: attitude, perceived norm, and personal agency, which can serve as good signals to detect implicit intentions. Among these determinants, the perceived norm is a social network-related factor, which argues that one’s intention is influenced by others’ expectations and behaviors. Hence, we propose a multiview learning framework to incorporate text information and link among postings and authors to address this problem. We instantiate the pro posed framework with DNNs. For the text information, we represent each post using the bag-of-words method. For the link information, we represent the postings of an author’s social connections as a sequence of posting indices. These two types of representations are then fed into a multi-input DNN for classification. We evaluate the proposed model on two real-world datasets in comparison with multiple benchmarks. Ex periments show our method significantly outperforms other methods in the literature.

The contributions of this paper are as follows: (1) From a theoretical perspective, we propose a multiview framework motivated by the IBM theory for the detection of intentions from social media data, which incorporates both text information and social network information. The framework deepens our understanding of which information should be leveraged in the task of product adoption intention mining. (2) We instantiate the proposed framework with DNNs (i.e., MV-CLSTM) for product adoption intention mining. The model has significantly better performance than other benchmark methods. In practice, our proposed framework would be a feasible and effective approach to detect product adoption intentions.

The remainder of the paper is organized as follows. In Section 2, we review the related literature on intention mining on social media, the IBM theory, multiview representation learning, and graph neural net works (GNNs), respectively. Section 3 introduces the motivations of this research and details the proposed multiview framework and its instan tiation. In Section 4, we evaluate our model on two real-world datasets. Section 5 discusses and concludes this paper.

## 2. Related work

In this section, we first review the literature about intention mining on social media. We then review the related literature concerning the IBM theory, multiview representation learning, and GNNs.

## 2.1. Intention mining on social media

Purchase intentions are of great interest to product and service providers who would like to better pinpoint their potential customers through social media postings [1]. Recent years have witnessed the blossom of related studies. As summarized in Table 1, most of these studies focus on the detection of purchase intentions (a.k.a. consump tion intentions), particularly in the early intention mining literature [1, 8–11]. Many other kinds of intentions, such as travel intentions [12], were also studies in recent years to address application-specific chal lenges. For example, Zhang et al. [2] proposed a neural network-based modeling approach to discover user intentions from medical question-answering websites. From a technical perspective, the relevant methods are shifting from shallow machine learning algorithms with hand-crafted features to deep learning approaches, which achieve better performance than shallow methods [13,14].

Our work differs from previous studies in the following three aspects: (1) Adoption intentions are conceptually wider than purchase in tentions, because purchase intentions usually refer to product purchase intentions, while adoption intentions can be the intentions of adopting some opinions in addition to products. In this study, we focus on product adoption intentions as a case study. Adoption intentions are also prac tically more valuable than purchase intentions. For some users who want to adopt certain products (by renting, borrowing, or requesting an object) without the intention to purchase them (e.g., because of the high price), this will help locate more potential users when advertising products. Some young users may ask for some products as a gift, although such cases are relatively sparse. One example tweet is “Well, below is some gifts I’d be really happy to receive in 2016: 1) iPhone 7 Plus 128 GB. 2) A F.R.I.E.N.D.S mug ? and 3) A Harry P. Sweatshirt.” (2) We aim to identify the fine-grained intention to adopt a specific kind of product (e.g., iPhone 7) rather than a wider category of product (e.g., iPhone, cellphone, or electronic device) like previous work. (3) Although we also take advantage of the superior performance of deep learning approach in many NLP tasks [6], the major contribution of our work lies in the multiview learning framework for adoption intention prediction motivated by the theory from psychology, rather than a general DNN model without connection to the determinants of intention.

Table 1  
Summary of the literature about intention mining on social media.

<table><tr><td>Year</td><td>Author</td><td>Intention</td><td>Explicit or implicit</td><td>Data source</td><td>Method</td></tr><tr><td>2010</td><td>Ramanand et al. [8]</td><td>Purchase</td><td>Explicit</td><td>Product reviews</td><td>Rule-based methods</td></tr><tr><td>2013</td><td>Wang et al. [9]</td><td>Purchase</td><td>Explicit</td><td>Sina Weibo</td><td>Pattern-based product keyword extraction</td></tr><tr><td>2013</td><td>Hollerit et al. [10]</td><td>Purchase</td><td>Both</td><td>Twitter</td><td>Several traditional classification methods (e.g., SVM) with textual features</td></tr><tr><td>2014</td><td>Gupta et al. [11]</td><td>Purchase</td><td>Explicit</td><td>Quora, Yahoo! Answers</td><td>SVM with hand-crafted features</td></tr><tr><td>2015</td><td>Ding et al. [1]</td><td>Purchase</td><td>Both</td><td>Sina Weibo</td><td>Consumption Intention Mining Model (CIMM) based on CNN and transfer learning</td></tr><tr><td>2015</td><td>Wang et al. [12]</td><td>Six categories such as travel</td><td>Explicit</td><td>Twitter</td><td>Semi-supervised intent graph learning</td></tr><tr><td>2016</td><td>Zhang et al. [2]</td><td>To know medical information</td><td>Both</td><td>Medical QA website</td><td>CNN-based joint modeling</td></tr><tr><td>2016</td><td>Park et al. [4]</td><td>N/A</td><td>Both</td><td>Twitter</td><td>Intention corpora building and topic modeling</td></tr><tr><td>2017</td><td>Li et al. [5]</td><td>Buying cloth, eating, traveling, and fitting</td><td>Implicit</td><td>Sina Weibo</td><td>Attention-based encoder-decoder model</td></tr></table>

## 2.2. The IBM theory from psychology

The IBM theory is a behavior theory from psychology, which elab orates the determinants of intention and behavior [7]. As shown in Fig. 1, the theory states that one’s intention to perform a behavior is shaped by her/his attitude, perceived norm, and personal agency. Atti tude refers to the overall (affective) evaluation of the behavior<sup>3</sup>; injunctive norm (a.k.a. subjective norm) means the belief about whether other people will approve or disapprove the behavior or not; descriptive norm concerns the belief about whether other people perform the behavior or not; personal agency describes perceived control over the behavior (i.e., perceived control), and the ability to perform the behavior (i.e., self-efficacy). The IBM theory has proven to be applicable in many significant business applications, including health care [7,15], marketing [16], and public service [17]. Acorrding to the IBM theory, one’s intention to adopt a product may be influenced by the people having connection with her/him. Therefore, we incorporate social network information into the detection of product adoption intentions rather than only consider text content on social media. Unlike our study, previous studies have no theories like the IBM theory to explain and guide their intention mining models.

![](/api/attachments/84WFPFZN/fulltext/images/c3f0d0b3cb84a0c7466586aff6adae7caaed10361f29437b4fb250402a602c61.jpg)  
Fig. 1. The Integrated Behavior Model (redrawn after [7]).

## 2.3. Multiview representation learning

In numerous real-world applications, data concerning a phenomenon or system of interest are often collected from multiple domains or ob tained from various feature extractors, and hence exhibit multiple “views” [18–20]. For example, multimedia segments often consist of both video and audio signals [18]. Multiview representation learning introduces view-specific embeddings for multiview data and jointly optimizes the embeddings to boost some subsequent tasks such as classification. According to a recent survey [21], there are two major categories of research about multiview representation learning: multi view representation alignment and multiview representation fusion.

The main idea of multiview representation alignment is to process data of each view by a mapping function and then form a multiview aligned space using the learned representations from different views by regularization. There are different ways of alignment: distance-based, similarity-based, and correlation-based alignment. Distance and similarity-based alignment methods include: partial least squares [22], deep cross-view embedding models [23], among others. Correlation-based methods include canonical correlation analysis (CCA) [24] and its extensions (e.g., sparse CCA [25] and deep CCA [26]).

Multiview representation fusion approaches are mainly categorized into two types: graphical model-based and neural network-based. Graphical model-based method attempts to learn a compact set of latent random variables that represent a distribution over the observed multiview data. Related studies include multimodal topic learning [27], multiview sparse coding [28], information aggregation of multiple data sources [29], and so on. Neural network-based fusion aims to fuse the features learned from different views into one feature representation. It includes multimodal autoencoder [30], multiview convolutional neural network [31], multimodal recurrent neural network (RNN) [32], among others. Empowered by the development and success of DNNs [14,33], many DNNs are proposed to learn high-level feature representations from multiview data. For example, multimodal deep autoencoders were developed to learn a shared representation between several data views [30]. Multimodal RNN approaches were proposed to connect multiple views of data, which are widely applied in image captioning and visual question answering [34].

We distinguish our work from the previous studies in the following aspects: (1) in this paper, the consideration of additional data view (i.e., social network information) has its theoretical foundation in psychol ogy; (2) we utilize multiview DNNs to develop an end-to-end frame work, which implicitly learns the representation of multiple data views and is capable of identifying product adoption intentions in the mean time; and (3) we incorporate social network information into our pro posed multiview DNN model.

## 2.4. Graph neural networks

GNNs are a group of neural network models that address various graph-related tasks (e.g., node classification, link prediction, and graph classification) in an end-to-end manner. Generally, GNNs could be categorized into four types: recurrent GNNs, convolutional GNNs, graph autoencoders (GAEs), and spatial-temporal GNNs [35].

Recurrent GNNs assume that a node in a graph exchanges informa tion with its neighbor nodes until a stable equilibrium is reached and use the same set of parameters recurrently over nodes to learn node representations [36–38]. Convolutional GNNs learn node representa tions by aggregating its own features and neighbors’ features, and they are mainly divided into two classes: spectral-based and spatial-based. In spectral-based approaches, graph convolutions are inspired by the filters in graph signal processing [39–41]. Spatial-based methods define graph convolutions based on a node’s spatial relations from the perspective of information propagation, and their ideas are similar to those of recur rent GNNs [42–45]. GAEs are unsupervised deep learning architectures that map nodes into a latent feature space and decode graph information from latent representations. GAEs can be used to learn network em beddings through reconstructing graph structural information [46,47], and they can also generate new graphs in a sequential manner or in a global manner [48,49]. Spatial-temporal GNNs aim to model graph data whose nodes have dynamic features. They integrate graph convolutions for capturing spatial dependence with RNNs or convolutional neural networks (CNNs) for modeling temporal dependence [50,51].

The above GNN-based models are different from our multiview DNN model. As one important component of our model is designed to learn text representation from the social interaction-based text graph (see Fig. 3), it is possible to develop a new model by integrating multi-view learning and GNNs for product adoption intention identification in the future.

## 3. A framework to detect product adoption intentions

## 3.1. Problem definition

In this work, a posting with the intention to adopt a specific product refers to the situation that a posting explicitly or implicitly indicates the possibility for its author to adopt a product. The detection of product adoption intentions can be formulated as a binary classification prob lem. Given a set of posts and authors’ social connections $( \mathrm { i . e . , }$ , replying and retweeting), the goal is to identify whether a post’s author has the intention to adopt a specific product.

## 3.2. Theoretical foundations

Motivated by the IBM theory, we design a multiview learning framework for intention detection, which is summarized in Fig. 2. The top part presents the factors that are conceptually helpful in recognizing intentions, and the bottom part illustrates the analytical framework which takes into account where these factors are embodied in the social media context. Our focus is to leverage the perceived norm (i.e., C in Fig. 2) to help recognize product adoption intentions.

As we have mentioned in Section 1, there are two types of intentions: implicit intentions and explicit intentions. Users usually present explicit intentions through explicit expressions, which can be directly captured. For implicit intentions, we rely on attitude, perceived norm, and per sonal agency, as suggested by the IBM theory for intention mining. For instance, the tweet “I really love the newly-released iPhone X” exhibits a positive attitude toward the product, showing an implicit intention; the posting “Oh no, all of my friends are having iPhone $\mathbf { X } ^ { \ast }$ contains another implicit intention where the author is talking about others’ behavior (i. e., perceived norm). The personal agency measures one’s perceived control over certain behavior $( \mathrm { i . e . , }$ perceived control) and the ability to perform the behavior (i.e., self-efficacy). This often serves as a negative signal of implicit intentions, potentially helping rule out the postings without intentions. For example, the posting “I don’t think I have time to play the newly-released Xbox” negates the intention to adopt an Xbox. The observation is illustrated in the top part of Fig. 2.

The above analysis suggests that detecting the determinants of intention and explicit expressions may boost the task of intention min ing. In the social media context, the focal posting may contain the explicit expression and the determinants of intention $( \mathrm { i . e . , }$ attitude, perceived norm, and personal agency). However, not all perceived norm information is encoded in the target posting. Most information about the perceived norm exists in social networks. From the perspective of perceived norm, one’s intention to adopt a product may be influenced by the people having connection with her/him. In light of this, we propose to incorporate social link information into the task of product adoption intention detection. Specifically, we design a multiview learning framework to combine the target posting and the postings of the au thor’s social connections to detect whether a posting contains a product adoption intention. Fig. 2 presents the proposed conceptual framework and how it is linked to the IBM theory; see notations A, B, C, and D for the connections. In the following, we introduce the details of our pro posed framework.

## 3.3. Preliminaries

Given the proposed multiview framework, we can instantiate the classifier with the state-of-the-art classification methods. In this work, we resort to DNNs, as DNNs have shown leading performances across many NLP tasks, including text classification [6]. In the following, we introduce some necessary preliminary knowledge about deep learning for our paper; more details could be found in a popular book of deep learning [25].

## 3.3.1. Word embedding

Word embedding is a feature-learning technique that encodes words as high-dimensional distributional vectors, which captures the syntactic and semantic information of words [54,55]. According to the distribu tional hypothesis, words with similar meanings will occur close to each other in the embedding space. Such a technique could mitigate the noisy data issue and word variation issue.

## 3.3.2. Convolutional neural network (CNN)

CNN is a kind of neural network for processing data with grid-like topology [52], which is widely applied in areas such as sentence modeling [13,54,56]. A typical CNN structure for sentence modeling consists of a convolutional operation and a max pooling operation. The convolutional operation can be viewed as a local feature extractor by applying a convolutional kernel to every possible word window of fixed length [54]. A max pooling operation is then applied to the extracted local features to progressively reduce the spatial size of the representation.

## 3.3.3. Recurrent neural network (RNN) and long short-term memory (LSTM)

RNN is another kind of neural networks for processing an input sequence one element at a time, allowing information in previous steps to persist in the form of a hidden state variable [14]. LSTM is a special kind of RNN, which is designed to learn long-term dependency for sequential data [52,53].

## 3.4. MV-CLSTM model for adoption intention detection

In this section, we instantiate the above framework with a multiview convolutional RNN model with social network information $( \mathrm { i . e . , }$ MV-CLSTM), as illustrated in Fig. 3. The key insight of our model is to extract two types of data views from raw social media data and feed them into two DNN modules respectively. The two types of data views go through four layers of the DNN modules to jointly learn latent rep resentations that are fused together in the following merging layer. Then the fused representation is fed into a sigmoid layer for classification. We detail the input and each layer in the below part.

Input: Motivated by the IBM theory, we take into account the postings of a social media user’s social connections in the classification of a target post. Social connections can be defined in multiple ways, such as following network, replying network, and retweeting network. The IBM theory suggests that a person’s intention is also influenced by others expectations and behaviors. In social media, replying and retweeting are more direct signals reflecting interactions between one user and others. In addition, collecting the following networks among users is limited in this work. Hence, in this paper, the social connection between two users is defined as reply or retweet relation.

![](/api/attachments/84WFPFZN/fulltext/images/e9dad9c4613fe95d14af280973b381f59a138cfd8218a3bd88fb134c5cac57be.jpg)

![](/api/attachments/84WFPFZN/fulltext/images/fb7b0215dd5e03600aa49777304f76c79e012f009ef38e087e5d9b64e503098d.jpg)  
Fig. 2. Conceptual framework for adoption intention detection.

![](/api/attachments/84WFPFZN/fulltext/images/4e11cda600722584bebf6e7b4c872175d910ee7e6488bcc47cb3d650d827370a.jpg)  
Fig. 3. MV-CLSTM model for adoption intention detection.

The left part of Fig. 3 displays a small network that consists of five users $( \mathrm { i . e . , } U _ { 1 } , . . . , U _ { 5 } )$ and six social media postings $( \mathrm { i . e . , } T _ { 1 } , . . . , T _ { 6 } )$ . Solid lines among users represent social connections; a dashed line links a user and his/her social posting. To identify whether text $T _ { 1 }$ written by user $U _ { 1 }$ has a product adoption intention, we construct two types of inputs: (1) the first is the raw target text $T _ { 1 }$ that consists of words; (2) the second is a sequence of post indices, which represent postings $( \mathrm { i . e . , } T _ { 2 } , . . . , T _ { 6 } )$ of $U _ { 1 } { } ^ { \prime }$ ’s first-degree social connections $( \mathrm { i . e . , } U _ { 2 }$ and $U _ { 3 } )$ and second-degree social connections $\mathrm { ( i . e . , ~ } U _ { 4 }$ and $U _ { 5 } ) .$ . The main reason we consider second-degree social connections is that second-degree peer influence effect might also exist [57]. When constructing a sequence of post indices, the first-degree social connections’ postings are put in front of the second-degree social connections’ postings. Users within the same degree of relations are ordered randomly, which indicates all users are equally important. Similarly, the posting indices of a user are also randomly ordered to ensure equal importance. Then, the two types of data are fed into a two-view DNN structure.

Embedding layer: The first view (i.e., the target post T ) consists of a sequence of words. Assuming the length is $l ,$ we represent each word as a vector in the embedding space $\mathbb { R } ^ { d }$ and initiate the embedding with pretrained word embeddings, which are obtained by running the skipgram model on a dataset [58]. Hence, a posting of length l is repre sented as a matrix $S _ { 1 } \in \mathbb { R } ^ { l \times d }$ . The embedding matrix is also trainable to learn context-specific embeddings.

For the second view $( \mathrm { i . e . , }$ , a sequence of posting indices), we attempt to learn a posting-specific embedding in the embedding space R<sup>r</sup>. Formally, the second view is represented as a matrix $S _ { 2 } \in \mathbb { R } ^ { m \times r }$ in the embedding layer. We initialize its parameters randomly and learn them during model training, as no pretrained post embeddings are available.

CNN, LSTM, and hidden layers: The embedding layer is sequentially followed by a CNN layer, a LSTM layer, and a hidden layer. A convo lution and pooling layer can extract local features from the input, and an LSTM layer can learn long-term dependencies from sequence data. Some studies show that combining CNN and LSTM could take advantage of the local and global features of input texts [54,59]. Therefore, we also take this approach in this study. Specifically, for the learned embeddings of each view, we feed them into a CNN layer to learn coarse-grained local features, which are then processed by a LSTM layer to learn long-distance dependencies. After the LSTM layer, a fully connected hidden layer is used to learn higher-level latent features.

Merging and sigmoid layers: After processing the two types of data with two separate structures of embedding and DNN layers, we merge the two learned latent feature vectors of the same size by performing element-wise summation. Then, the merged result is fed into a sigmoid function for binary classification.

Model training: To train the proposed model, we use binary crossentropy as the loss function. We use Adam to learn model parameters due to its computational efficiency and low memory requirements [60]. We also apply the dropout strategy in the CNN and LSTM layers to reduce overfitting and improve the performance [61].

## 4. Evaluation

## 4.1. Experimental design

Datasets. We collected 239,649 tweets about iPhone 7 and 181,206 tweets about Xbox One by an API program called Twitter4J<sup>4</sup> to crawl the tweets that contain some keywords about iPhone 7 and Xbox One, respectively (e.g., “iPhone seven” and “Xbox one”). The time of the data spans from November 22, 2016 to November 28, 2016. We randomly sampled 10,000 tweets from each of the two raw datasets separately. Then, we obtained 1692 iPhone tweets and 2538 Xbox tweets by removing advertisement tweets from the sampled datasets with some manual rules. The iPhone dataset consists of 1692 iPhone 7-related tweets with 335 tweets that contain the intentions to adopt iPhone 7 cellphones: the Xbox dataset is a collection of 2538 tweets about the product Xbox One with 306 tweets that show the intentions to adopt Xbox Ones. There are 38 undirected social links based on reply or retweet relations for the iPhone dataset and the number of the links for Xbox dataset is 302.

Baseline methods: To systematically evaluate our proposed model, we select an array of representative baseline methods from prior research, including non-deep learning methods and deep learning methods. For convenience, we use shallow methods and deep methods to indicate these two classes of methods in the following. For shallow methods mentioned in the previous studies, we first represent each text using the Bag-of-Words and TF-IDF schemes. The size of an input text is the size of the vocabulary of each dataset. Then, we apply support vector machine (SVM), logistic regression (LR), random forest (RF), gradient boosted regression trees (GB), and Gaussian Naïve Bayes (NB), respectively.

To verify the contribution of each component (i.e., data view) in the proposed model, we select the deep methods in an incremental manner. For single-view methods, we first initialize the text representation with pretrained word embeddings and apply CNN [56], LSTM [52], the combination of CNN and the gated recurrent unit (GRU) (i.e., CNN-GRU) [54], and the combination of CNN and LSTM (i.e., CNN-LSTM) [54], respectively. Note that the methods proposed in previous intention mining literature cannot be directly used as baselines, because of the differences between our study and the previous studies in terms of problem definition and method.

Evaluation metrics: To evaluate the performance of each method, we adopt four commonly used metrics for binary classification: precision, recall, Macro-F1 score (i.e., harmonic mean of precision and recall), and accuracy.

Experimental settings: We randomly split each dataset into 50% for training, 25% for validation, and 25% for test. For fair comparison, we perform random search for each method to optimize hyperparameter selection [62]. All results are averaged over 20 independent runs of the experiments, with a different data splitting for each run. All the methods are implemented in Python 2. The shallow methods are implemented using scikit-learn [63]; the deep methods are implemented using Keras<sup>5</sup> with Theano as its backend [64].

## 4.2. Experimental results

## 4.2.1. Performance comparison

We first compare our proposed MV-CLSTM with the shallow methods and summarize the results in Table 2. From the results, we can conclude that: (1) our MV-CLSTM outperforms all the shallow methods with sig nificant margin across almost all datasets and evaluation metrics, which demonstrates the superiority of our model; (2) MV-CLSTM performs better in dealing with the imbalanced datasets. Particularly, for the more imbalanced dataset (i.e., Xbox), the performance gap in terms of accu racy between MV-CLSTM and other methods is marginal, while our model surpasses the other methods significantly regarding Macro-F1 score. This shows that these shallow methods tend to blindly predict an instance with a negative label in highly imbalanced datasets, which incur high accuracy yet low recall, and hence low Macro-F1 [65]. However, MV-CLSTM combines two kinds of data sources and captures deep features to identify intentions from texts, which leads to high precision and recall simultaneously.

In addition, we compare our model with other deep methods and report the results in Table 3. We can conclude that: (1) the combination of CNN and RNN performs comparably to or better than CNN under the single-view settings (e.g., CNN-GRU > CNN, CNN-LSTM > CNN). The result is consistent with the previous literature [54], which demon strates the effectiveness of combining CNN and RNN in the task of mining product adoption intentions; (2) our MV-CLSTM outperforms all these deep methods across these two datasets and four evaluation met rics, which shows the effectiveness of our model due to its multiview deep learning architecture integrating text and social interaction information.

## 4.2.2. Sensitivity analysis

To test the sensitivity of our MV-CLSTM, we conduct the following three experiments to examine the impact of training data ratio, social connections, and the density of social connections, respectively.

4.2.2.1. Impact of the ratio of training data. To demonstrate the sensi tivity of our method against the ratio of training data, we vary the ratio from 0.1 to 0.9 and examine how the performance changes, when our method is compared with other methods. As shown in Figs. 4 and 5, we observe that the performance of all methods increases in a general trend with the increasing proportion of training data, especially when the ratio is equal to and lower than 0.6. When the ratio is larger than 0.6, most methods’ performance stabilizes with the increasing ratio. Overall, our method MV-CLSTM performs better than these shallow baselines. For some methods such as SVM and LR, although they are comparable to our model on dataset iPhone, they achieve much lower performance on the larger dataset Xbox. In summary, our model performs better and more robustly in comparison with the shallow methods.

The comparison between our MV-CLSTM and other deep methods is presented in Figs. 6 and 7. We can clearly observe that our MV-CLSTM

Table 3  
Table 2  
Performance comparison of MV-CLSTM and shallow methods.

<table><tr><td rowspan="2">Algorithm</td><td colspan="2">Macro-F1</td><td colspan="2">Accuracy</td><td colspan="2">Precision</td><td colspan="2">Recall</td></tr><tr><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td></tr><tr><td>SVM</td><td>0.775</td><td>0.714***</td><td>0.859**</td><td>0.919***</td><td>0.785***</td><td>0.940***</td><td>0.769*</td><td>0.657***</td></tr><tr><td>LR</td><td>0.755*</td><td>0.758***</td><td>0.866</td><td>0.921***</td><td>0.826</td><td>0.862**</td><td>0.723**</td><td>0.711***</td></tr><tr><td>RF</td><td>0.729***</td><td>0.743***</td><td>0.844***</td><td>0.921***</td><td>0.772***</td><td>0.897</td><td>0.702***</td><td>0.688***</td></tr><tr><td>GB</td><td>0.740***</td><td>0.759***</td><td>0.849***</td><td>0.917***</td><td>0.774***</td><td>0.816***</td><td>0.721**</td><td>0.718***</td></tr><tr><td>NB</td><td>0.646***</td><td>0.671***</td><td>0.749***</td><td>0.844***</td><td>0.638***</td><td>0.654***</td><td>0.666***</td><td>0.701***</td></tr><tr><td>MV-CLSTM</td><td>0.776</td><td>0.82</td><td>0.87</td><td>0.937</td><td>0.832</td><td>0.897</td><td>0.749</td><td>0.775</td></tr></table>

Note: \* indicates that the p-value p of the t-test of MV-CLSTM and another approach meets the condition 0.05 $< p < = 0 .$ .1; similarly, \*\* indicates 0.001 $< p < = 0 . 0 5 ;$ and \*\*\* indicates $p < = 0 . 0 0 1$

Performance comparison of MV-CLSTM and other deep methods.

<table><tr><td rowspan="2">Algorithm</td><td colspan="2">Macro-F1</td><td colspan="2">Accuracy</td><td colspan="2">Precision</td><td colspan="2">Recall</td></tr><tr><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td></tr><tr><td>CNN</td><td>0.701***</td><td>0.761***</td><td>0.822***</td><td>0.921***</td><td>0.738***</td><td>0.86**</td><td>0.691***</td><td>0.715***</td></tr><tr><td>LSTM</td><td>0.746**</td><td>0.759***</td><td>0.856**</td><td>0.919***</td><td>0.799**</td><td>0.849***</td><td>0.723*</td><td>0.715***</td></tr><tr><td>CNN-GRU</td><td>0.739**</td><td>0.773***</td><td>0.852**</td><td>0.921***</td><td>0.8**</td><td>0.85**</td><td>0.719**</td><td>0.735***</td></tr><tr><td>CNN-LSTM</td><td>0.72***</td><td>0.774***</td><td>0.84**</td><td>0.925***</td><td>0.797**</td><td>0.881</td><td>0.708**</td><td>0.728***</td></tr><tr><td>MV-CLSTM</td><td>0.776</td><td>0.82</td><td>0.87</td><td>0.937</td><td>0.832</td><td>0.897</td><td>0.749</td><td>0.775</td></tr></table>

Note: the notations behind the numbers have the same meanings as those in Table 2.

![](/api/attachments/84WFPFZN/fulltext/images/9b99b636f436e28fdbb1626466d8483b713ac8886e07ab04e8ca99b17edf7e55.jpg)

![](/api/attachments/84WFPFZN/fulltext/images/3b3474e2c5beaa4979aad64b9c987fc7ee87ee5932f21bba3d27807b9014abfc.jpg)  
Fig. 4. Comparison with shallow methods on iPhone data (in Macro-F1 and accuracy).

![](/api/attachments/84WFPFZN/fulltext/images/e959accddb562596bd4f5bd09bba2e700eb5a8c1b79063c1ea4fc150cf2d4403.jpg)

![](/api/attachments/84WFPFZN/fulltext/images/87418167df572d5caa00d9dfaf3f009a78bd7b1aeef633c8e376da9b5ad78b89.jpg)  
Fig. 5. Comparison with shallow methods on Xbox data (in Macro-F1 and accuracy).

generally surpasses the other competitive deep methods across the two evaluation metrics when the ratio of training data is larger than 0.1, although the performance curves of most methods are mixed. In addi tion. both CNN-GRU and CNN-LSTM are better than CNN. which is consistent with the above analysis regarding the results in Table 3.

4.2.2.2. Impact of social connections. To test the effect of social infor mation in our MV-CLSTM, we conduct the following ablation analysis shown in Tables 4 and 5. CLSTM is a variant of our MV-CLSTM without the branch of social information, MV-LSTM is another variant of our MV-CLSTM, which has a similar multiview deep learning architecture but without CNN layers. For dataset iPhone, MV-CLSTM’s performance is slightly lower than CLSTM, whereas MV-LSTM performs slightly better than LSTM. Both of the performance gaps are not statistically significant. For dataset Xbox, MV-CLSTM outperforms CLSTM significantly, and MV-LSTM are also significantly better than LSTM. The reason is that the social interactions in dataset iPhone is too sparse to contribute to the performance improvement. For the Xbox data with denser networks, we could see the obvious improvement benefited from incorporating social network information.

![](/api/attachments/84WFPFZN/fulltext/images/af941c01174ec853a2b7e276a0127ad1841fcaf52150147b786493df8ce307d3.jpg)

![](/api/attachments/84WFPFZN/fulltext/images/73a79edfc918f327da79346aae653b5cd7ff826dc9bcc7c1659a6800ac06340c.jpg)  
Fig. 6. Comparison with deep methods on iPhone data (in Macro-F1 and accuracy).

![](/api/attachments/84WFPFZN/fulltext/images/a2a9c924cccf3fcef02969156435a4569739ad2a79cbc3fd646a5d2613ef8c64.jpg)

![](/api/attachments/84WFPFZN/fulltext/images/f4f7f3d62acd256956bc0683fc20bc081c799d2793048266908ca8a63850d99f.jpg)  
Fig. 7. Comparison with deep methods on Xbox data (in Macro-F1 and accuracy).

4.2.2.3. Impact of the density of social connections. As the number of social connections varies for individual users, we conduct the experi ment in Fig. 8 to test the performance of our method for different size of social connections and different products. We randomly sample the edges of the posting network transformed from social connections from 20% to 100% for our MV-CLSTM and its variant MV-LSTM on the two datasets. In general, we could see that the macro-F1 scores of MV-CLSTM and MV-LSTM do increase with the increasing ratio of social connections on the larger dataset Xbox, but not on the smaller dataset iPhone. The situation and reason are consistent with the above analysis of Tables 4 and 5.

## 4.2.3. Visualization of the prediction results

To show the effectiveness of our MV-CLSTM in the highly imbal anced datasets, we adopt confusion matrix to visualize the prediction results for the two datasets. The ratio between the number of the true positive instances and the number of the true negative instances is 0.237:1 for dataset iPhone; the ratio is 0.146:1 for dataset Xbox. For these imbalanced data, the precision scores are 0.75 and 0.852, respectively; the recall scores are 0.556 and 0.642, respectively. The results show our MV-CLSTM can achieve acceptable prediction for imbalanced data, and its performance increases when data become larger and social connections become denser. Fig. 9.

## Discussions and conclusion

Despite the tremendous value of mining product adoption intentions from social media, existing methods for intention mining mainly focus on text information of a target posting but overlook the potential benefit of other data such as social network information. In this work, motivated by the IBM theory, we demonstrated the value of incorporating social network information in addition to text information of postings, and proposed a general multiview deep learning framework for intention mining. We also instantiated the proposed framework with DNNs and systematically evaluated our model on two real-world datasets.

Table 4  
Performance comparison of MV-CLSTM and its variant.

<table><tr><td rowspan="2">Algorithm</td><td colspan="2">Macro-F1</td><td colspan="2">Accuracy</td><td colspan="2">Precision</td><td colspan="2">Recall</td></tr><tr><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td></tr><tr><td>CLSTM</td><td>0.783</td><td>0.77***</td><td>0.872</td><td>0.919***</td><td>0.821</td><td>0.838***</td><td>0.762</td><td>0.734***</td></tr><tr><td>MV-CLSTM</td><td>0.776</td><td>0.82</td><td>0.87</td><td>0.937</td><td>0.832</td><td>0.897</td><td>0.749</td><td>0.775</td></tr></table>

Note: the notations behind the numbers have the same meanings as those in Table 2.

Table 5  
Performance comparison of MV-LSTM and its variant.

<table><tr><td rowspan="2">Algorithm</td><td colspan="2">Macro-F1</td><td colspan="2">Accuracy</td><td colspan="2">Precision</td><td colspan="2">Recall</td></tr><tr><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td><td>iPhone</td><td>Xbox</td></tr><tr><td>LSTM</td><td>0.746</td><td>0.759***</td><td>0.856</td><td>0.919**</td><td>0.799</td><td>0.849</td><td>0.723</td><td>0.715***</td></tr><tr><td>MV-LSTM</td><td>0.755</td><td>0.798</td><td>0.86</td><td>0.928</td><td>0.804</td><td>0.866</td><td>0.731</td><td>0.759</td></tr></table>

Note: the notations behind the numbers have the same meanings as those in Table 2.

![](/api/attachments/84WFPFZN/fulltext/images/1deb1e60649c1a10d0a1a973d28beb6bbdb09fe79936926b84851f70ea42b358.jpg)  
Fig. 8. Performance of MV-CLSTM and MV-LSTM with varying social connections.

![](/api/attachments/84WFPFZN/fulltext/images/1324f249825f75fc83561effc515dcd7206578a8332f8282bd8c1700e9437a25.jpg)

![](/api/attachments/84WFPFZN/fulltext/images/4ec7e205821934297841a8629d910d920994925e6cfeb2ee04770d3d9af28675.jpg)  
Fig. 9. Confusion matrix of one prediction for the two datasets.

The empirical evaluation demonstrates that integrating text and so cial interaction information in multiview deep learning improves the detection performance of product adoption intentions. Our approach significantly outperforms the non-deep learning methods with regard to F1 score and accuracy. In addition, our approach is better than a few state-of-the-art deep learning methods in terms of precision, recall, F1 score, and accuracy. The sensitivity analysis on the impact of social connections and their density shows that social interaction information is effective to help detect product adoption intentions from social media.

In line with [66], our study proposes a novel analytical method as an information technology (IT) artifact. The IT artifact contributes four general design principles to design science in information systems: (1) social information is helpful to identify product adoption intentions on social media; (2) multiview DNN is an effective representation learning model for social media analytics; (3) integrating different types of in formation is possibly better than using a single type of information; and (4) motivating analytical design with psychological theory is a feasible and effective approach. These design principles may provide some theoretical insights for other design science research, particularly in social media analytics. For instance, the proposed framework and model could be easily adapted for other business analytics problems, such as spammer detection and sentiment analysis of product reviews.

In terms of business applications, our research could contribute to personalized marketing on social media. Taking Twitter as an example, 53% of Twitter users are likely to be the first to buy new products.<sup>6</sup> How to target potential consumers is a very important problem for product providers. Our study could be used to target who have the intention to adopt a specified product on social media, which will benefit for social media marketing. In addition, our research could be used to facilitate public health management by identifying the intention to adopt certain public health-related products or services. For example, opioid abuse or misuse has raised a serious public health concern in the U.S. Our study could be used to locate possible opioid users for further public health analytics such as trend estimation and reason extraction.

In the future, we could further improve the proposed framework from the following aspects. First, we plan to design specific represen tation learning structures for each data source to further improve the performance. We put this as a future direction because we believe that the essential novelty of our work lies in incorporating social network information into the proposed multiview DNN model. Second, we plan to verify the effectiveness of our proposed framework and model on more kinds of intentions, such as the intention to see a movie or the intention to invest in stock markets. Third, we are interested in con ducting more downstream research based on the intention detection. For example, in light of our research, we can examine whether the detected volume of tweets with the intention to see a movie can help predict box office revenue. Fourth, a person’s sentiment is possible to impact her/his behavior intentions; therefore, incorporating sentiment into the pro posed model would be an interesting topic. In addition, some advanced methods in the sentiment analysis literature could provide insights for intention detection [13,67–69]. Considering word polarity disambigu ation for intention identification is also interesting [70], as some words have varying polarities in different contexts. Fifth, we are also interested in designing a semi-supervised learning-based method for intention detection, as it has been widely used for social data analysis [71] (e.g., spammer detection [72] and multi-platform user identity linkage [73]) due to its advantage of utilizing both labeled and unlabeled data for training. Finally, as intention awareness is important for human-machine interaction systems [74,75], our proposed multiview DNN model has the potential use in such systems.

## Author statement

Zhu Zhang: Conceptualization, Methodology, Software, and Writing; Xuan Wei: Methodology, Conceptualization, and Writing; Xiaolong Zheng: Conceptualization, Methodology, and Writing; Daniel D. Zeng: Conceptualization and Supervision.

## Acknowledgments

We thank Dr. Xin Li for his help in reviewing and revising the manuscript. This work was supported in part by the Ministry of Science and Technology of China [Grant Nos 2020AAA0108401, 2019QY(Y) 0101, and 2020AAA0103405], the National Natural Science Foundation of China [Grant Nos 71974187, 71621002, 71902179, and 72074209], and the Longhua District Science and Technology Innovation Fund [Grant No. 10162a20200617b70da63]. Most of the experiments pre sented herein were run on the El Gato supercomputer that was sup ported by the National Science Foundation [Grant No. 1228509].

## References

[1] X. Ding, T. Liu, J. Duan, J.-Y. Nie, Mining user consumption intention from social media using domain adaptive convolutional neural network, in: Proceeding of the Twenty-Ninth AAAI Conference Artificial Intelligence, 2015. http://www.aaai.org/ ocs/index.php/AAAI/AAAI15/paper/view/9748 (accessed June 28, 2016).

[2] C. Zhang, W. Fan, N. Du, P.S. Yu, Mining user intentions from medical queries: a neural network based heterogeneous jointly modeling approach, in: Proceeding of the 25th International Conference World Wide Web, International World Wide Web Conferences Steering Committee, Republic and Canton of, Geneva, Switzerland. 2016, pp. 1373–1384, https://doi,org/10.1145/2872427.2874810

[3] Z. Zhang, X. Wei, X. Zheng, Q. Li, D. Zeng, Detecting product adoption intentions via multiview deep learning, Inf. J. Comput. (forthcoming).

[4] D.H. Park, Y. Fang, M. Liu, C. Zhai, Mobile app retrieval for social media users via inference of implicit intent in social media text, in: Proceeding of the 25th ACM International Conference on Information Knowledge Management, ACM, New York, NY, USA, 2016, pp. 959–968, https://doi.org/10.1145/2983323.2983843.

[5] C. Li, Y. Du, S. Wang, Mining implicit intention using attention-based RNN encoder-decoder model, Intell. Comput. Methodol. (2017) 413–424, https://doi org/10.1007/978-3-319-63315-2\_36. Springer, Cham,.

[6] R. Collobert, J. Weston, L. Bottou, M. Karlen, K. Kavukcuoglu, P. Kuksa, Natural language processing (almost) from scratch, J. Mach. Learn. Res. 12 (2011) 2493–2537.

[7] D.E. Montano, ˜ D. Kasprzyk, Theory of reasoned action, theory of planned behavior, and the integrated behavioral model. Health Behavior and Health Education Theory Research and Practice, 4th Ed, Jossey-Bass, San Francisco, CA, US, 2008, pp. 67–96.

[8] J. Ramanand, K. Bhavsar, N. Pedanekar, Wishful Thinking - Finding suggestions and “buy” wishes from product reviews, in: Proceeding of the NAACL HLT 2010 Workshop on Computational Approaches to Analysis and Generation of Emotion in Text, Association for Computational Linguistics, Los Angeles, CA, 2010, pp. 54–61. https://www.aclweb.org/anthology/W10-0207 (accessed December 31, 2019)

[9] J. Wang, W.X. Zhao, H. Wei, H. Yan, X. Li, Mining new business opportunities: identifying trend related products by leveraging commercial intents from microblogs., in: 2017. http://www.aclweb.org/anthology/D13-1132 (accessed June 1. 2017).

[10] B. Hollerit, M. Kroll, ¨ M. Strohmaier, Towards linking buyers and sellers: detecting commercial intent on twitter, in: Proceeding of the 22Nd International Conference on World Wide Web, ACM, New York, NY, USA, 2013, pp. 629–632, https://doi. org/10.1145/2487788.2488009.

[11] V. Gupta, D. Varshney, H. Jhamtani, D. Kedia, S. Karwa, Identifying purchase intent from social posts, in: Proceeding of the Eighth International AAAI Conference on Weblogs Soc. Media, 2014. https://www.aaai.org/ocs/index.php/ ICWSM/ICWSM14/paper/view/8037 (accessed June 1, 2017).

[12] J. Wang, G. Cong, W.X. Zhao, X. Li, Mining User Intents in Twitter: A Semi-Supervised Approach to Inferring Intent Categories for Tweets, AAAI, 2015, pp. 318–324.

[13] W. Zhao, Z. Guan, L. Chen, X. He, D. Cai, B. Wang, Q. Wang, Weakly-supervised deep embedding for product review sentiment analysis, IEEE Trans. Knowl. Data Eng. 30 (2018) 185–197, https://doi.org/10.1109/TKDE.2017.2756658.

[14] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (2015) 436–444, https://doi.org/10.1038/nature14539.

[15] J.M.B. PhD, M.M. Ren´ee Umstattd Meyer PhD, S.L.U. PhD, L.W.T. PhD, J.C.J. PhD, B.E.L. PhD, Gender differences in college leisure time physical activity: application of the theory of planned behavior and integrated behavioral model, J. Am. Coll. Health, 62 (2014) 173–184, https://doi,org/10.1080/07448481.2013.872648.

[16] S. Varki, M. Colgate, The role of price perceptions in an integrated model of behavioral intentions, J. Serv. Res. 3 (2001) 232–240, https://doi.org/10.1177 109467050133004

[17] M. Bravo. L. Briceño. R. Cominetti. C.E. Cortés. F. Martínez, An integrated behavioral model of the land-use and transport systems with network congestion and location externalities, Transp. Res. Part B Methodol. 44 (2010) 584–596. https://doi.org/10.1016/i.trb.2009.08.002.

[18] S. Sun, A survey of multi-view machine learning, Neural Comput. Appl. 23 (2013) 2031–2038, https://doi.org/10.1007/s00521-013-1362-6.

[19] J. Zhao, X. Xie, X. Xu, S. Sun, Multi-view learning overview: recent progress and new challenges, Inf. Fusion. 38 (2017) 43–54, https://doi.org/10.1016/j. inffus.2017.02.007

[20] C. Xu, D. Tao, C. Xu, A Survey on Multi-view Learning, ArXiy13045634 Cs, 2013. http://arxiv.org/abs/1304.5634 (accessed January 18, 2017).

[21] Y. Li, M. Yang, Z. Zhang, A survey of multi-view representation learning, IEEE Trans. Knowl. Data Eng. 31 (2019) 1863–1883, https://doi.org/10.1109 TKDE 2018 2872063

[22] W.R. Schwartz, A. Kembhavi, D. Harwood, L.S. Davis, Human detection using partial least squares analysis, in: 2009 IEEE 12th International Conference on Computer Vision, 2009, pp. 24–31, https://doi.org/10.1109/ICCV.2009.5459205.

[23] A.M. Elkahky, Y. Song, X. He, A multi-view deep learning approach for cross domain user modeling in recommendation systems, in: Proceeding of the 24th International Conference on World Wide Web, ACM, New York, NY, USA, 2015, pp. 278–288, https://doi.org/10.1145/2736277.2741667.

[24] H. Hotelling, Relations between two sets of variates, in: S. Kotz, N.L. Johnson (Eds.). Breakthr. Stat, Methodol, Distrib., Springer, New York, NY. 1992. pp. 162–190. https://doi.org/10.1007/978-1-4612-4380-9.14.

[25] X. Chen, L. Han, J. Carbonell, Structured sparse canonical correlation analysis, Artif. Intell. Stat., PMLR (2012) 199–207, in: http://proceedings.mlr.press/v22/ chen12a.html (accessed December 8. 2020).

[26] G. Andrew, R. Arora, J. Bilmes, K. Livescu, Deep canonical correlation analysis, Int. Conf. Mach. Learn., PMLR (2013) 1247–1255, in: http://proceedings.mlr.press/ v28/andrew13.html (accessed December 8, 2020)

[27] D.M. Blei, M.I. Jordan, Modeling annotated data, in: Proceeding of the 26th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Association for Computing Machinery, New York, NY, USA, 2003, pp. 127–134, https://doi.org/10.1145/860435.860460.

[28] Y. Jia, M. Salzmann, T. Darrell, Factorized latent spaces with structured sparsity, Ady, Neural Inf, Process, Syst, 23 (2010) 982–990.

[29] X. Wei, Z. Zhang, M. Zhang, D.D. Zeng, Combining crowd and machine intelligence to detect false news in social media, Available SSRN 3355763 (2019).

[30] J. Ngiam, A. Khosla, M. Kim, J. Nam, H. Lee, A.Y. Ng, Multimodal deep learning, in: Proceeding of the 28th International Conference on Machine Learning ICML-11, 2011, pp. 689–696. http://machinelearning.wustl.edu/mlpapers/paper\_files/IC ML2011Ngiam\_399.pdf (accessed February 22, 2017).

[31] C. Feichtenhofer, A. Pinz, A. Zisserman, Convolutional two-stream network fusion for video action recognition, in: 2016: pp. 1933–1941. https://www.cy-foundat ion.org/openaccess/content cypr 2016/html/Feichtenhofer Convolutional Two-St ream Network CVPR 2016 paper,html (accessed December 8. 2020).

[32] A. Karpathy, L. Fei-Fei, Deep visual-semantic alignments for generating image descriptions, in: 2015: pp. 3128–3137. https://www.cv-foundation.org/openacce ss/content\_cvpr\_2015/html/Karpathy\_Deep\_Visual-Semantic\_Alignments\_20 15\_CVPR\_paper.html (accessed December 8, 2020)

[33] M. Zhang, X. Wei, X. Guo, G. Chen, Q. Wei, Identifying complements and substitutes of products: a neural network framework based on product embedding, ACM Trans. Knowl. Discov. Data TKDD. 13 (2019) 1–29.

[34] S. Antol, A. Agrawal, J. Lu, M. Mitchell, D. Batra, C.L. Zitnick, D. Parikh, VQA: visual question answering, in: 2015 IEEE International Conference on Computer Vision ICCV, 2015, pp. 2425–2433, https://doi.org/10.1109/ICCV.2015.279.

[35] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, P.S. Yu, A comprehensive survey on graph neural networks, IEEE Trans. Neural Netw. Learn. Syst. (2020) 1–21, https://doi.org/10.1109/TNNLS.2020.2978386.

[36] F. Scarselli, M. Gori, A.C. Tsoi, M. Hagenbuchner, G. Monfardini, The graph neural network model, IEEE Trans. Neural Netw. 20 (2009) 61–80, https://doi.org/ 10.1109/TNN.2008.2005605.

[37] C. Gallicchio, A. Micheli, Graph echo state networks, in: 2010 International Jt. Conference on Neural Network IJCNN, 2010, pp. 1–8, https://doi.org/10.1109/ LJCNN.2010.5596796.

[38] H. Dai, Z. Kozareva, B. Dai, A. Smola, L. Song, learning Steady-States of Iterative Algorithms over Graphs, in: International Conference on Machine Learning, PMLR, 2018, pp. 1106–1114, in: http://proceedings.mlr.press/v80/dai18a.html (accessed December 7, 2020).

[39] T.N. Kipf. M. Welling, Semi-supervised classification with graph convolutional networks. in: Proceeding of the 5th International Conference on Learning Represent, Toulon, France, 2017. https://openreview.net/forum?id=SJU4ayYgl (accessed December 7, 2020)

[40] R. Levie, F. Monti, X. Bresson, M.M. Bronstein, CayleyNets: graph convolutional neural networks with complex rational spectral filters, IEEE Trans. Signal Process. 67 (2019) 97–109, https://doi.org/10.1109/TSP.2018.2879624.

[41] C. Zhuang, Q. Ma, Dual graph convolutional networks for graph-based semisupervised classification, in: Proceeding of the 2018 World Wide Web Conference, International World Wide Web Conferences Steering Committee, CHE, Republic and Canton of Geneva, 2018, pp. 499–508, https://doi.org/10.1145/ 3178876.3186116.

[42] A. Micheli, Neural network for graphs: a contextual constructive approach, IEEE Trans. Neural Netw. 20 (2009) 498–511, https://doi.org/10.1109 TNN.2008.2010350.

[43] M. Niepert, M. Ahmed, K. Kutzkov, Learning convolutional neural networks for graphs, Int. Conf. Mach. Learn., PMLR (2016) 2014–2023, in: http://proceedings. mlr.press/v48/niepert16.html (accessed December 7. 2020).

[44] H. Gao, Z. Wang, S. Ji, Large-scale learnable graph convolutional networks, in: Proceeding of the 24th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Association for Computing Machinery, New York, NY, USA, 2018, pp. 1416–1424, https://doi.org/10.1145/3219819.3219947.

[45] Z. Liu, C. Chen, L. Li, J. Zhou, X. Li, L. Song, Y. Qi, GeniePath: Graph Neural Networks with Adaptive Receptive Paths. Proc, AAAI Conf, Artif, Intell. 33 (2019 4424–4431, https://doi.org/10.1609/aaai.v33i01.33014424

[46] S. Cao, W. Lu, Q. Xu, Deep neural networks for learning graph representations, in: Thirtieth AAAI Conference on Artificial Intelligence, 2016. http://www,aaai org/ocs/index.php/AAAI/AAAI16/paper/view/12423 (accessed June 25. 2016).

[47] K. Tu, P. Cui, X. Wang, P.S. Yu, W. Zhu, Deep recursive network embedding with regular equivalence, in: Proceeding of the 24th ACM SIGKDD International Conference on Knowledge Discovery Data Mining, Association for Computing Machinery, New York, NY, USA, 2018, pp. 2357–2366, https://doi.org/10.1145/ 3219819.3220068.

[48] M.J. Kusner, B. Paige, J.M. Hern´andez-Lobato, Grammar variational autoencoder, in: International Conference on Machine Learning, PMLR, 2017, pp. 1945–1954, in: http://proceedings.mlr.press/v70/kusner17a.html (accessed December 7, 2020).

[49] T. Ma, J. Chen, C. Xiao, Constrained Generation of Semantically Valid Graphs via Regularizing Variational Autoencoders, Ady. Neural Inf. Process. Syst. 31 (2018)

[50] A. Jain, A.R. Zamir, S. Savarese, A. Saxena, Structural-RNN: deep learning on Spatio-temporal graphs, in: 2016 IEEE Conference on Computer Vision and Pattern Recognition CVPR, 2016, pp. 5308–5317, https://doi.org/10.1109/ CVPR 2016.573

[51] S. Guo, Y. Lin, N. Feng, C. Song, H. Wan, Attention based spatial-temporal graph convolutional networks for traffic flow forecasting, Proc. AAAI Conf. Artif. Intell 33 (2019) 922–929, https://doi.org/10.1609/aaai.v33i01.3301922.

[52] I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016.

[53] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural Comput. 9 (1997) 1735–1780, https://doi.org/10.1162/neco.1997.9.8.1735.

[54] X. Wang, W. Jiang, Z. Luo, Combination of convolutional and recurrent neura network for sentiment analysis of short texts. in: Proceeding of the COLING 2016 26th International Conference on Computer Linguist, 2016, pp. 2428–2437. htt ps://www.aclweb.org/anthology/C/C16/C16-1229.pdf (accessed July 29. 2017)

[55] T. Mikoloy, I. Sutskever, K. Chen, G.S. Corrado, J. Dean, Distributed representations of words and phrases and their compositionality, in: C.J.C. Burges, L. Bottou, M. Welling, Z. Ghahramani, K.Q. Weinberger (Eds.), Advance Neural Information Processing System 26, Curran Associates, Inc., 2013: pp. 3111–3119. http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-ph rases-and-their-compositionality.pdf (accessed July 20, 2018).

[56] Y. Kim, Convolutional neural networks for sentence classification, in: Proceeding of the 2014 Conference on Empirical Methods in Natural Language Processing EMNLP, 2014, pp. 1746–1751

[57] D. Rajchwald, N. Markuzon, E. Airoldi, Bias reduction of peer influence effects with latent coordinates and community membership, in: 2017 IEEE Int. Conf. Big Data Big Data, 2017, pp. 3098–3103, https://doi.org/10.1109/BigData.2017.8258284.

[58] T. Mikolov, G. s Corrado, K. Chen, J. Dean, Efficient Estimation of Word Representations in Vector Space, 2013.

[59] S. Vosoughi, P. Vijayaraghavan, D. Roy, Tweet2Vec: learning tweet embedding using character-level CNN-LSTM encoder-decoder, in: Proceeding of the 39th International ACM SIGIR Conference on Research Development in Information Retrieval, ACM, New York, NY, USA, 2016, pp. 1041–1044, https://doi.org/ 10.1145/2911451.2914762.

[60] D.P. Kingma, J. Ba, Adam: a method for stochastic optimization, in: Proceeding of the 3rd International Conference on Learning Represent, San Diego, 2015. http:// arxiv.org/abs/1412.6980 (accessed February 10, 2018).

[61] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, R. Salakhutdinov, Dropout: a simple way to prevent neural networks from overfitting, J Mach Learn Res 15 (2014) 1929–1958.

[62] J. Bergstra, Y. Bengio, Random search for hyper-parameter optimization, J. Mach.

[63] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, E. <sup>´</sup> Duchesnay, Scikit-learn: machine learning in python, J Mach Learn Res 12 (2011) 2825–2830.

[64] R. Al-Rfou, et al., Theano: A Python Framework for Fast Computation of Mathematical Expressions. 2016. ArXiv E-Prints, abs/1605.02688. http://arxiv org/abs/1605.02688.

[65] H. He, E.A. Garcia, Learning from imbalanced data, IEEE Trans. Knowl. Data Eng. 21 (2009) 1263–1284, https://doi.org/10.1109/TKDE.2008.239

[66] A.R. Heyner. S.T. March. J. Park. S. Ram. Design science in information systems research. MIS Q. 28 (2004) 75–105

[67] E. Cambria, Affective computing and sentiment analysis, IEEE Intell. Syst. 31 (2016) 102–107, https://doi.org/10.1109/MIS.2016.31.

[68] P. Zhu, Z. Chen, H. Zheng, T. Qian, Aspect aware learning for aspect category sentiment analysis, ACM Trans. Knowl. Discov. Data. 13 (2019), https://doi.org/ 10.1145/3350487, 55:1-55:21

[69] L. Wang, J. Niu, S. Yu. SentiDiff: combining textual information and sentiment diffusion patterns for twitter sentiment analysis, IEEE Trans. Knowl. Data Eng. 32 (2020) 2026–2039, https://doi.org/10.1109/TKDE.2019.2913641

[70] Y. Xia, E. Cambria, A. Hussain, H. Zhao, Word polarity disambiguation using bayesian model and opinion-level features, Cogn. Comput. 7 (2015) 369–380.

[71] A. Hussain, E. Cambria, Semi-supervised learning for big social data analysis, Neurocomputing 275 (2018) 1662–1673, https://doi.org/10.1016/j. neucom 2017.10.010

[72] C. Li, S. Wang, L. He, P.S. Yu, Y. Liang, Z. Li, SSDMV: semi-supervised deep social spammer detection by multi-view data fusion, in: 2018 IEEE International Conference on Data Mining ICDM, 2018, pp. 247–256, https://doi.org/10.1109/ JCDM.2018.00040.

[73] C. Li, S. Wang, H. Wang, Y. Liang, P.S. Yu, Z. Li, W. Wang, Partially shared adversarial learning for semi-supervised multi-platform user identity linkage, in: Proceeding of the 28th ACM International Conference on Information Knowledg Management, Association for Computing Machinery, New York, NY, USA, 2019, pp. 249–258. https://doi.org/10.1145/3357384.3357904

[74] N. Howard, E. Cambria, Intention awareness: improving upon situation awareness in human-centric environments, Hum.-Centric Comput. Inf. Sci. 3 (2013) 9, https://doi.org/10.1186/2192-1962-3-9.

[75] T. Rehder, A. Koenig, M. Goehl, L. Louis, D. Schramm, Lane change intention awareness for assisted and automated driving on highways, IEEE Trans. Intell. Veh. 4 (2019) 265–276, https://doi.org/10.1109/TIV.2019.2904386.

Zhu Zhang received the B.S. degree in automation from Zhejiang University in 2008 and the Ph.D. degree in computer science from the Institute of Automation. Chinese Academy of Sciences in 2015. He is currently an associate professor at the Institute of Automation Chinese Academy of Sciences. His-research interests include artificial intelligence, data mining, information systems health informatics, and business analytics He has published more than 20 articles in major journals and conferences such as JOC, JMIS, KBS, JMIR, ACM TMIS, and ICIS.

Xuan Wei is an assistant professor at the Department of Information, Technology and Innovation, Antai College of Economics and Management, Shanghai Jiao Tong University. He received his B.S. degree from the Shanghai Jiao Tong University in 2014. Then he received his Ph.D. degree in management information systems at the University of Arizona in 2020. His-research interests include crowd intelligence and crowdsourcing, social media analytics, statistical machine learning, probabilistic modeling and interference, and deep learning. His-work has been published in major information systems journals such as JOC, DSS and TKDD.

Xiaolong Zheng received the B.S. degree from China Jiliang University, the M.S. degre from Beijing Jiaotong University, and the Ph.D. degree from the Chinese Academy of Sciences. He is currently a professor at the Institute of Automation, Chinese Academy of Sciences. His-research interests include big data analytics, network dynamics, and finan cial technology. He has published over 90 peer-reviewed articles and edited 8 books. He served as the program co-chair of several conferences or workshops such as IEEE

International Conference on Intelligence and Security Informatics 2017 (IEEE ISI 2017). His-work has been published in major information systems journals such as DSS, Infor mation and Management, and Information Systems Frontiers. He is a member of the IEEE.

Daniel Dajun Zeng received the M.S. and Ph.D. degrees in industrial administration from Carnegie Mellon University. He is a professor at the Institute of Automation, Chinese Academy of Sciences. He was a Gentile Family Professor of MIS at the Department of Management Information Systems, the University of Arizona. His-research interests include social computing, recommender systems, intelligence and security informatics, infectious disease informatics, applied operations research, and game theory. He has published one monograph as well as more than 300 peer-reviewed articles and coedited 22 books and proceedings. His-work has been published in major information systems jour nals such as MISQ, INFORMS JOC, DSS, JASIST, IEEE TKDE, among others. Now he serves as the editor-in-chief of ACM Transactions on Management Information Systems. He is a fellow of the IEEE and the AAAS.
