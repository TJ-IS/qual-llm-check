---
otero_id: 20317
otero_key: "RNKDRDU8"
title: "DNCP: An attention-based deep learning approach enhanced with attractiveness and timeliness of News for online news click prediction"
authors: "Jie Xiong; Li Yu; Dongsong Zhang; Youfang Leng"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103428"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# DNCP: An attention-based deep learning approach enhanced with attractiveness and timeliness of News for online news click prediction

![](/api/attachments/RNKDRDU8/fulltext/images/c58afb06288c5b617fe231f2b8dba4d35a16ae3191e6cb22dfc08e674c172bbe.jpg)

Jie Xiong <sup>a</sup>, Li Yu <sup>a,</sup>\*, Dongsong Zhang <sup>b</sup>, Youfang Leng

<sup>a</sup> School of Information, Renmin University of China, Beijing, BJ 100872, China

<sup>b</sup> The University of North Carolina at Charlotte, Charlotte, North Carolina, USA

## A R T I C L E I N F O

Keywords: News click prediction Deep learning Attention mechanism Topic model

## A B S T R A C T

Predicting news clicks or popularity is of great importance to news providers and recommender systems. Attractiveness and timeliness of news are two prominent drivers of news clicks. Attractiveness represents the appealingness or interestingness of news to an individual, while timeliness indicates the recency of news. Existing research on news click prediction models has ignored those two important variables. There is a lack of exploration and understanding of how to represent them in a predictive model and how effective and valuable they are to the prediction performance of a model. To fill these gaps, in this research, we propose a deep news click prediction (DNCP) model that integrates attractiveness and timeliness of news in an attention-based deep neural network for predicting news clicks. We also propose new measures for those two variables. Empirical evaluation using two real-world datasets shows that the DNCP model outperforms a variety of baseline models. The findings of this research provide several novel research contributions and practical implications for improving news click prediction.

## 1. Introduction

In the digital era, the information overload problem becomes increasingly severe due to explosive growth of information. According to the sixth edition of DOMO’s report<sup>1</sup>, 2.5 quintillion bytes of data are created on a daily basis, including hundreds of thousands of news. How to make news eye-catching to attract more views has made the craft of news content an art. Content distribution or sharing platforms, given the ever-growing Internet traffic, often rely on methods for content popu larity prediction in order to better allocate resources to meet readers evolving information needs [1]. One typical example is the news ranking service at Google News<sup>2</sup>, a well-known news online portal that recom mends potentially popular news to readers. Therefore, predicting the popularity of individual news articles is essential to news filtering and recommender systems.

According to the timing of prediction, prediction of news clicks can occur before or after news is released. This study focuses on the latter, aiming to predict future news clicks using the aggregated existing attention that individual news has received. In general, prediction of news clicks can be divided into click number prediction or click number range prediction [1], which is usually treated as a regression or classi fication problem that relies on textual and meta features as predictive features. Textual features are extracted from the textual content of a news article [4.8.9], while meta features contain information associated with each news, such as the author, news agency, and release date. So far, simple linear regression and decision tree (DT) models have been the most commonly used methods for predicting news clicks [2–4]. How ever, those approaches have a few limitations. First, laborious and ad hoc feature engineering is required, which makes the performance of prediction models highly sensitive to the quality of the selected features [5]. Also, it is difficult for those models to deal with textual features effectively because of the huge semantic space [6]. Second, prior studies have never examined potential impact of high-order and implicit in teractions among meta features of news on news click prediction. For example, financial news has higher click ratios on weekdays than on weekends [7], which suggests that the interaction between news cate gory and release date should be considered in news click prediction. Third, some key factors that affect news clicks have not been considered in existing research. such as the attractiveness and timeliness of news content. Attractiveness of news is referred to as its appealingness or interestingness to an individual. Attractiveness is not just about clickbait [11]. It can be affected by content quality, controversial topics, touching stories, and other factors of news that draw people’s interest. Timeliness is referred to as the popularity trend of an event reported in the news, which changes over time and reveals news’ life cycle. It is different from the concept of news freshness [2], which is defined as whether the presented events have ever been reported in the past or not. In other words, freshness emphasizes whether a news article contains new information.

To address the above limitations of existing research, this study proposes a new attention-based deep learning approach called deep news click prediction (DNCP) for news click prediction that consists of two key parts. One is text representation learning, and the other is meta feature representation learning. The former integrates two new concepts, namely attractiveness and timeliness of news, with bidirectional gated recurrent units (BiGRUs) [10]. DNCP uses a concatenation-based attention mechanism (CAM) to incorporate attractiveness and timeliness of terms into an attentive representation by focusing more on significant terms and generating a high-quality representation of a news article. Consid ering that people may express their sentiments through commenting news articles, including approval, opposition, fun, like/dislike, etc. [1], we propose a behavior-based topic model (BTM) that extends latent Dirichlet allocation (LDA) [12] based on news reading-commenting behaviors of readers to model attractiveness of a news article in DNCP. Furthermore, the trends of hot terms that the public has used during a period of time represent the evolving public interest, which can be considered as an indicator of timeliness of news. Accordingly, we represent the timeliness of news based on the trends of search terms obtained from search engines or online public opinion platforms. In order to take into consideration high-order interaction among meta features of a news article, DNCP incorporates factorization machine (FM) [13] to improve effectiveness and efficiency of meta feature rep resentation learning. The results of an empirical evaluation using two real-world datasets demonstrate the effectiveness of DNCP.

This study makes multi-fold theoretical and technical contributions. First, it proposes the concepts and metrics of attractiveness and timeli ness of news. To the best of our knowledge, this is the first attempt to incorporate these two critical factors in online news click prediction. Second, we propose a deep learning approach, DNCP, that integrates attractiveness, timeliness, and textual and meta features of news for news click prediction. More importantly, DNCP incorporates an atten tion mechanism based on the attractiveness and timeliness of individual terms contained in a news article. Third, this study provides empirical evidence about the effectiveness of not only DNCP as a whole, but also attractiveness and timeliness factors, in news click prediction, creating novel technical and practical insights.

The rest of the paper will be organized as follows. The related work will be discussed in next section. Section 3 introduces the proposed DNCP approach, followed by the description of evaluation in Section 4. The evaluation result will be presented in Section 5. Finally, the paper discusses the major findings and their research and practical implica tions, as well as limitations of this study and future research, in Section 6.

## 2. Related work

In general, prediction of news clicks is limited to a single domain where an individual news article resides, regardless of whether it is created or shared from an external source. Methodologically, automatic prediction of news clicks mainly involves extracting a set of features from news articles first, then training and deploying a machine learning model to make a prediction. In general, those predictive models can be divided into two classes: classic machine learning methods and deep learning methods.

## 2.1. Classic machine learning methods for news click prediction

Classic machine learning methods require feature engineering for selecting predictive features. We classify predictive features for news click prediction into two categories: textual and meta features. Extensive work on feature engineering and feature importance analysis for news click prediction has been done [1]. For example, Bandari et al. [4] found that the features of news agencies were part of the strongest predictors of news clicks among meta features. Tatar et al. [1] suggested that certain words or key phrases about hot or controversial topics in news content would often produce a significant amount of attention to news.

Regression models have been frequently used for predicting the number of clicks. Szabo et al. [14] found that the final click number of an online article was correlated with its early view patterns. They used a linear regression model with a logarithmic transformation to predict the number of future views based on the number of early views. However, in reality, a news article may not get the same attention from viewers over time. With this assumption, Pinto et al. [15] designed a weighted model that assigned weights to time intervals, which improved the accuracy of prediction. Gursun et al. [16] suggested a time series prediction model using autoregressive moving average (ARMA) to predict daily number of views. Keneshloo et al. [2] compared the effects of temporal, content, and meta features of news on regression and found that the use of meta features led to performance improvement. They proposed the concept of freshness and found that this feature led to prediction performance improvement. With the advances of feature engineering, additional features (e.g., named entity identification, sentiment analysis) and models have been applied to prediction tasks [17–20].

Other classification methods have also been used. For example, Jamali et al. [21] predicted the popularity of stories with different classic machine learning methods, such as DT, K-nearest neighbors (KNN), and support vector machine (SVM). Bandariet et al. [4] used meta and textual features extracted from news articles as input of news popularity prediction models constructed by SVM, DT, and bagging al gorithms. A key step in those traditional methods was the extraction of predictive features, which required laborious and time-consuming feature engineering and data processing skills.

There are several issues with classic machine learning approaches to news click prediction. First, the performances of those approaches are highly sensitive to the quality of predictive features selected as the model input. Second, those approaches usually use the bag-of-words method to represent textual features of news, which loses word sequence and context and does not consider text semantics. Third, although meta features of news have been used in existing work [1,4], none of the previous studies investigated the impact of high-order in teractions of meta features on news click prediction. Finally, timeliness and attractiveness of news have received no attention up to date.

## 2.2. Deep learning for news click prediction and text representation

So far, very few studies have developed deep learning models for predicting news clicks. Guan et al. [22] proposed a hierarchical neural network to learn text representation for news click prediction. Bidirec tional long short-term memory (BiLSTM) [23,24] has been used for learning the representation of text sequences, which simplifies feature processing. The existing work has achieved notable success, indicating the great potential of deep learning methods in predicting news clicks. In particular, text representation learning is always an important part of deep learning methods for news click prediction.

The goal of representation learning is to find an appropriate repre sentation of data in order to perform a machine learning task. Text representation learning is aimed to learn how to represent words in text by a vector in a hyperspace from a training corpus automatically. Word2Vec [25] and GloVe [26] are widely used methods for such word representation learning. Recurrent neural networks (RNNs), with long short-term memory (LSTM) and gated recurrent units (GRUs) being the most popular ones [27], have long been considered as a natural option when applying deep neural networks to text sequence modeling. Of course, many high-performance convolutional neural networks (CNNs) have also been developed, such as CNN-text [28] and gated convolution networks [29], for language modeling. Transformer [30] is one of the most promising architectures, which relies on multi-head attention to convey spatial information. However, its biggest disadvantage lies in its difficulty for running a warm start to yield convincing results.

Advanced pre-training techniques, such as bidirectional encoder representations from transformers (BERT) [31] for text representation have been gaining increasing momentum recently. They apply bidirec tional training on a transformer and have achieved promising results in a wide variety of natural language processing tasks [31]. Moreover, pre-training techniques are computationally intensive and require very large training data. To address those challenges, many new pre-training models have been proposed, such as ELECTRA [32], RoBERTa [33], and XLNet [34]. However, the focus of this study is mainly on the effect of attractiveness, timelines, and high-order interactions among meta fea tures of news on click prediction through the design of a deep neural network model, not to assess those pre-training models for text repre sentation learning. Therefore, we used the conventional RNNs to learn the representation of news in this research.

There has been some recent research progress in optimization of neural network architectures for text representation learning in text classification tasks. For example, Yang et al. [35] proposed a hierar chical attention network (HAN) model, which was a double-layer attention neural network, for word and sentence representation learning. Lai et al. [36] proposed a recurrent convolutional neural network (RCNN) for text classification, which added a CNN layer before an RNN layer to alleviate the problem of the long sequence bias. An attention pooling-based convolutional neural network (APCNN) for sentence modeling [37] combined an attention pooling layer with a CNN layer to distinguish the importance of individual words in sentences.

These variations or extensions of deep learning methods for text representation learning have achieved some remarkable success in text classification tasks but have not been leveraged for news click predic tion. In addition, attractiveness and timeliness of news articles, which theoretically may have significant influence on news clicks, have never been considered in existing research on prediction of news clicks.

## 3. DNCP

In order to address the limitations of existing studies, in this research, we propose DNCP, a multi-layer deep learning approach, to news click prediction. Compared with the conventional deep learning-based text representation, DNCP integrates attractiveness and timeliness of news via an attention mechanism to enhance text representation of news. Its architecture mainly consists of two core parts (Fig. 1): 1) a text feature representation learning module that integrates three types of input, including attractiveness, timeliness, and text content features encoded by BiGRU, and 2) a meta feature representation learning module based on FM. Those two parts are connected to an output node that uses the Softmax activation function to predict the range of news click numbers, as shown in Fig. 1.

## 3.1. Text representation learning

## 3.1.1. A behavior-based topic model for attractiveness

The attractiveness of a news article can be determined by the attractiveness of individual terms in the news. The former can be considered as an aggregation of the latter. However, the attractiveness of terms also depends on their context. For example, the term "Red Sox" is more attractive in sports news than in political news. Readers’ online behavior, especially their news commenting behavior after reading a news article, is an effective indicator of the attractiveness of news. In fact, higher quality news content, more appealing headlines, and more important issues discussed in a news article are likely to induce more comments from readers [1]. Thus, in this research, we assess news attractiveness based on reading-commenting behaviors of readers through topic analysis.

We propose BTM to determine the attractiveness of a news article through a probabilistic model that extends the LDA algorithm [12] by integrating reader behavior. As shown in Fig. 2, BTM uses c as a new observable variable for readers’ comments and introduces a new latent variable η to denote the topic-specific attractiveness for each word, which determines the likelihood that readers will click and comment on a news article containing that word. When a reader is attracted to d by its headline and clicks the news link, it leads to a reading action r. If he/she makes a comment c on d after reading it, then $c _ { r } ^ { d } = 1$ . Otherwise, $c _ { r } ^ { d } = 0$ Because a reader may choose to either comment on a news article or not (i.e., a binary decision), readers’ reading-commenting behaviors can be regarded as independently distributed Bernoulli trials, with the proba bility density function being $\eta ^ { c } ( 1 - \eta ) ^ { ( 1 - c ) }$ . Therefore, given the number of reading times of a news article, the number of comments on the article, that is, the number of successful Bernoulli trials, is an observable random variable that would follow the Binomial distribution. According to the traditional Bayesian approach, it is general to make conjugate priors for latent variables, which are parameters of distribution of observable variables. In order to utilize the Beta-Binomial conjugacy in posterior inference for the distribution of, BTM models the prior distri bution of η as Beta distribution. In other words, the prior belief proba bility of success or failure on the Bernoulli trial of reading-commenting behavior $c _ { r } ^ { d }$ is determined by a Beta distribution.

![](/api/attachments/RNKDRDU8/fulltext/images/141e463206b0795a0bfeadc683a9ffa21b8d3f4e16c769786e1c18958792cf35.jpg)  
Fig. 1. The Architecture of DNCP.

Compared with LDA, other than the generation process of com menting behavior c, as shown in the dotted box in Fig. 2, BTM also in cludes the generation of the topic z and word w using Dirichlet Multinomial conjugacy [12]. Thus, BTM is also a full generative Bayesian model.

Fig. 2 is a graphical diagram of BTM, where N, K, and V represent the total numbers of news documents, topics, and vocabularies, respec tively; R is the total number of reading (i.e., clicking) times of all news articles in a corpus and $R _ { d }$ denotes the number of times that an article d has been read (i.e., clicked); w and c are observable variables, which are marked in gray color in Fig. 2; θ, ϕ, z, and η are latent variables. A formal description of the generative process can be represented as follows:

• For each news article $d \in N \colon$ it generates topic distribution $\theta _ { d } \sim D i r ( \alpha _ { 1 } )$ , and chooses a topic $z _ { d } \sim M u l t ( \theta _ { d } )$ ;

• For each word i in d: it generates word distribution $\phi _ { k } \sim D i r ( \beta _ { 1 } ) , k =$ $z _ { d } , k \in K ,$ , and chooses a word $w _ { i d } \sim M u l t ( \phi _ { k } ) ;$

• For each topic-word pair $( z , w ) \in K \times V ;$ it generates attractiveness distribution $\eta _ { z w } \sim B e t a ( \alpha _ { 2 } , \beta _ { 2 } )$ . For each reading $r \in [ 1 , R _ { d } ]$ of d, it determines comment status $c _ { r } ^ { d } \sim B i n ( 1 , \eta _ { z _ { r } ^ { d } , w _ { r } ^ { d } } )$

BTM extends the classic LDA by involving attractiveness assessment. To enable posterior inference, BTM uses the collapsed Gibbs sampling method [38] to acquire attractiveness distribution of words. The joint probability of BTM is formulated as follows:

$$
\begin{array}{l} p (\boldsymbol {c}, \boldsymbol {w}, z | \alpha_ {1}, \beta_ {1}, \alpha_ {2}, \beta_ {2}) \\ = \prod_ {d = 1} ^ {N} p (z _ {d} | \alpha_ {1}) \prod_ {k = 1} ^ {K} p (\boldsymbol {w} _ {k} | \beta_ {1}, z = k) \\ \prod_ {k = 1} ^ {K} \prod_ {\nu = 1} ^ {V} p (\boldsymbol {c} _ {k \nu} | \alpha_ {2}, \beta_ {2}, z = k, w = v) \end{array}\tag{1}
$$

where $z _ { d } = ( n _ { d } ^ { ( 1 ) } , n _ { d } ^ { ( 2 ) } , \cdots , n _ { d } ^ { ( K ) } ) ; n _ { d } ^ { ( k ) }$ is the number of times that a word related to the kth topic appears in article d; $w _ { k } = ( n _ { k } ^ { ( 1 ) } , n _ { k } ^ { ( 2 ) } , \cdots , n _ { k } ^ { ( V ) } ) ; n _ { k } ^ { ( \nu ) }$ is the number of times that the vth word is assigned to the kth topic; $c _ { k \nu } =$ $( n _ { k \nu } ^ { ( 1 ) } , n _ { k \nu } ^ { ( 0 ) } )$ is the number of comment status of the vth word in the kth topic, where 1 denotes commented, or 0 otherwise (i.e., $R = \sum _ { k } \sum _ { \nu } n _ { k \nu } ^ { ( \cdot ) } ) .$ The generative process and joint probability of BTM establish a connection between topic analysis and readers’ commenting behaviors, where $\theta , \phi ,$ and η are parameters to be estimated.

DNCP uses Gibbs sampling to construct a Markov chain to converge to the target distribution. The transition between adjacent states of the chain follows a simple rule, in which the next state is reached by sequentially sampling all variables from their distribution conditioned on the current values of all other variables [38]. In other words, the conditional distribution of word w can be derived based on the Dirichlet-Multinomial conjugacy:

$$
p (w _ {i d} \boldsymbol {w} _ {- i d}, z _ {i d} = j) = \frac {n _ {- i , j} ^ {(w _ {i d})} + \beta_ {1}}{\sum_ {v = 1} ^ {V} (n _ {- i , j} ^ {(v)} + \beta_ {1})}\tag{2}
$$

where ${ z } _ { i d }$ is the topic of $w _ { i d } , j \in K , n _ { - i , j } ^ { ( \cdot ) }$ denotes the number of words that are not assigned to topic z ; w is the set of observed data, and z is a latent variable, so the distribution p(z|w) is to be sampled. The conditional distribution of ${ z } _ { i d }$ given word $w _ { i d }$ and η is proportional to the number of times that the topic is mentioned in the document d. Associated with reading-commenting data, the conditional distribution of ${ z } _ { i d }$ can be formulated as follows:

$$
\begin{array}{l} p (z _ {i d} = j | \boldsymbol {z} _ {- i d}, \boldsymbol {w}, \boldsymbol {c}) \\ \propto \big (n _ {- i, j, d} + \alpha_ {1} \big) p (w _ {i d} | \boldsymbol {w} _ {- i d}, z _ {i d} = j) \prod_ {r} p \big (c _ {r} ^ {d} | \eta_ {j, w _ {i d}} \big) \end{array}\tag{3}
$$

where $z _ { - i d }$ denotes the topic distribution of the ith word in document d with the cancellation of the current assignment of z . The last multipli cation in Eq. 3 denotes the joint conditional probability of each comment associated with the word $w _ { i d } .$ . The sampling of $\bar { z } _ { i d }$ involves distribution of attractiveness, which keeps getting updated with the topic probability in each iteration of sampling. Using the Beta-Binomial conjugacy to formulate the conditional distribution of η given observa tions of comments, words, and topics, the posterior distribution of η follows the beta distribution with changed parameters:

$$
\eta_ {z w} | \boldsymbol {z}, \boldsymbol {w}, \boldsymbol {c} \sim B e t a (n _ {z w} ^ {1} + \alpha_ {2}, n _ {z w} ^ {0} + \beta_ {2})\tag{4}
$$

where $n _ { z w } ^ { ( \cdot ) }$ is the number of observed comments, $\alpha _ { 2 }$ and $\beta _ { 2 }$ are initial parameters of the prior distribution of $\eta _ { z w }$

Based on the above analysis, the distribution of attractiveness can be calculated for each word in a given topic. For an entire news corpus, considering the probability distributions of topics, topic-specific words, and attractiveness of topic-specific words, the final generated attrac tiveness score of the i th word in the d th news in a corpus can be formulated as follows:

![](/api/attachments/RNKDRDU8/fulltext/images/317921c0a20bed243fb049dbe09599f85924f57e31f2586174efee38b5981517.jpg)  
Fig. 2. The Representation of BTM Derived from Reader Behaviors with Topic Analysis.

$$
c _ {i d} = \sum_ {z = 1} ^ {K} \theta_ {d z} \phi_ {z w _ {i}} \eta_ {z w _ {i}}\tag{5}
$$

The higher the value of $c _ { i d } ,$ the more attractive a word would be. In addition, it is worth noting that the life cycle of news is short. People are mostly interested in reading and commenting on the latest news (e.g., Coronavirus). An outdated news will likely receive fewer reads or comments. Furthermore, in our study, attractiveness was determined not by the accumulative number of comments made on news, but by the ratio of the number of comments to the number of views without com ments, which should remain relatively stable over time.

## 3.1.2. A hot trend vector for timeliness

Timeliness of news is another critical factor that influences news clicks [1]. Generally, the hotness of a search query term represents the degree of public interest [2], and search engines or public opinion platforms can provide cues to the trend of search terms. Therefore, the hotness of terms can be identified through analysis of search queries or click logs. In this study, we crawled hotness trends of terms from Sina Micro index, which is the largest Chinese public opinion platform. Then, we built a two-dimensional hot trend matrix T of terms, in which any cell in the matrix represented the value of hotness of a specific term in a specific day.

We made the following assumptions when modeling the timeliness of news based on hotness of terms contained in news. First, due to the short life cycle of news, the timeliness of a news article decays over time. Second, the contribution of timeliness to clicks is correlated with the topic distribution of the article because the hotness of terms may vary with different topics. Therefore, the topic distribution should be considered in the measure of timeliness. Based on the above consider ations, there is a timeliness vector t for each term w in an article. t is a time series vector for hotness, where each element is computed as fol lows:

$$
t _ {i j} = \lambda^ {*} (1 - \mu) ^ {j} \boldsymbol {T} _ {p j} \sum_ {z = 1} ^ {K} \theta_ {d z} \phi_ {z w _ {i}}\tag{6}
$$

where j represents the elapsed time since the release of a news article; T is the hotness trend matrix, which shows the usage trend of each term at a daily level; $p$ is the position or index of term w in ; μ is a hyper parameter that controls the decay rate; λ is a hyper parameter that adapts the value of the trend vector; and the summation is the aggre gation of the correlation scores between topic and term distribution generated by BTM. It is worth noting that the terms are derived from segmenting sentences in a corpus. However, not all the segmented terms can be found in the trend matrix. We use a zero vector as the default for the missing terms.

## 3.1.3. Text encoder

Text encoding is a process of implicit extraction of text semantics. DNCP is initialized with word embedding pre-trained by Word2Vec as the representation of textual news content. Because a single-direction GRU is insufficient to capture contextual information of incoming words, DNCP uses BiGRU to get the context of words from both forward and backward directions. Finally, the latent semantic representation of word $w _ { i }$ can be summarized by the concatenation of two hidden vectors:

$$
\boldsymbol {h} _ {i} = \left[ \overrightarrow {\boldsymbol {h} _ {i}}, \overleftarrow {\boldsymbol {h} _ {i}} \right]\tag{7}
$$

where $\overrightarrow { \pmb { h } _ { i } }$ and $\stackrel { \longleftarrow } { h _ { i } }$ are the forward and backward hidden vectors, respec tively.

3.1.4. CAM: a concatenation-based attention mechanism to enhance prediction performance

Attention in deep learning can be interpreted as a vector of impor tance weights to improve the learning of a deep neural network. In the context of this study, an attention vector represents how strongly a word is correlated with its sentence. Usually, researchers take the sum of representations of words weighted by the attention vector as the approximation of the target sentence. The CAM is a general solution to enhancing the performance of the classic attention mechanism [39–41]. CAM integrates extra auxiliary feature vectors into the final attentive representations of words. The naive score function of CAM to calculate the importance of each element of a sequence of words is defined as follows:

$$
s \left(\boldsymbol {h} _ {i}, \boldsymbol {h} _ {i} ^ {*}\right) = \boldsymbol {u} ^ {T} f \left(\boldsymbol {W} _ {1} \boldsymbol {h} _ {i} + \boldsymbol {W} _ {2} \boldsymbol {h} _ {i} ^ {*} + \boldsymbol {b}\right)\tag{8}
$$

where $\mathbf { \delta } _ { h _ { i } }$ is a hidden vector of a word in the input sequence; $\boldsymbol { h } _ { i } ^ { * }$ is an auxiliary vector to be concatenated; $f ( \cdot )$ is a non-linear activation function such as hyperbolic tangent transformation; u is a weight vector; $u ^ { T }$ denotes its transpose; and $\small { W _ { 1 } , W _ { 2 } , \boldsymbol { b } , }$ and u are parameters to be learned.

In this study, DNCP integrates attractiveness and timeliness through CAM as auxiliary features. We use $\pmb { h } _ { i } , \pmb { c } _ { i }$ , and $t _ { i }$ to denote text semantics, attractiveness, and timeliness vectors of the i th word w in a news article, respectively. Considering those three factors in CAM, as shown in the center of Fig. 1, the score function that determines the importance of an element in the input sequence is defined as follows:

$$
s (\boldsymbol {h} _ {i}, \boldsymbol {c} _ {i}, t _ {i}) = \boldsymbol {u} ^ {T} \tanh \left(\boldsymbol {W} _ {h} \boldsymbol {h} _ {i} + \boldsymbol {W} _ {c} \boldsymbol {c} _ {i} + \boldsymbol {W} _ {t} \boldsymbol {t} _ {i} + \boldsymbol {b}\right)\tag{9}
$$

Then, the Softmax function is used to calculate the attentive weights α. The latent representation $\pmb { h } _ { a }$ of an article is generated by weighted summation:

$$
\alpha_ {i} = \frac {\exp (s (\boldsymbol {h} _ {i} , \boldsymbol {c} _ {i} , \boldsymbol {t} _ {i}))}{\sum_ {i} \exp (s (\boldsymbol {h} _ {i} , \boldsymbol {c} _ {i} , \boldsymbol {t} _ {i}))}\tag{10}
$$

$$
\boldsymbol {h} _ {a} = \sum_ {i} \alpha_ {i} \boldsymbol {h} _ {i},\tag{11}
$$

where the output vector $\scriptstyle h _ { a }$ is the final representation of text features, which is partial input to the classifier at the top layer of Fig. 1.

## 3.2. Meta feature representation learning

Besides content, a news article also possesses a number of meta features, such as author, organization, category, and tags, which may also have important impact on news clicks. Encoding them using simple one-hot encoding potentially makes the size of input dimension huge. Furthermore, the interactions among meta features, such as article category and news release date, may also influence news clicks. There fore, learning representation of meta features is necessary to reduce input dimension size and extract high-order interactions, which has not been studied in existing news click prediction research.

The wide & deep model [42] has been widely used for representation learning of meta features. However, it is labor-intensive and time-consuming to handcraft features and combine high-order in teractions. In this study, we used an FM [13], which models pairwise feature interactions as an inner product of latent vectors, to minimize manual effort in feature selection. Generally, discrete and sparse meta features are initially represented by one-hot encoding with a large number of dimensions. We embedded sparse features into dense vectors. Although FM is able to model high-order feature interactions in princi ple, usually only order-2 feature interactions are considered due to high complexity in practice [7]. Therefore, DNCP focuses on order-2 feature interactions. The core of the FM layer is represented as follows:

$$
\boldsymbol {h} _ {f} = b + w x + \sum_ {i = 1} ^ {L - 1} \sum_ {j = i + 1} ^ {L} <   \boldsymbol {v} _ {i}, \boldsymbol {v} _ {j} > x _ {i} x _ {j}\tag{12}
$$

where x is the concatenation of meta feature embeddings; $x _ { i }$ and $x _ { j }$ are elements of $x ,$ and $\pmb { x } \in \mathbb { R } ^ { L } : I$ L is the size of ${ \mathfrak { c } } ; { \pmb { h } } _ { f } ,$ the latent output of the FM layer, is a vector with F dimensions; b is a global bias; w models the strength of x $\} ; b \in \mathbb { R } ^ { F } , \pmb { w } \in \mathbb { R } ^ { F \times L } , \pmb { \nu } _ { i } \in \mathbb { R } ^ { F \times D } ; < \pmb { \nu } _ { i } , \pmb { \nu } _ { j } >$ is the dot product of two corresponding row vectors of size D in matrices $\nu _ { i }$ and $\nu _ { j } ; D \in \mathbb { N } _ { 0 } ^ { + }$ is a hyperparameter that defines the dimensionality of factorization; and $h _ { f }$ is the final latent representation of meta features, which is a part of input to the classifier.

## 3.3. The Output layer

After text and meta feature representation learning, the latent vec tors of text $\left( h _ { a } \right)$ and meta features $( h _ { f } )$ were generated. They were then concatenated and fed into the Softmax classifier, which would predict the click number range of a news article. We have adopted cross-entropy loss, which measures the performance of a classification model that produces a probability value between 0 and 1 as the output, as the loss function of the model. All variables in the model were trained by the Adam Optimizer [43] with back propagation.

## 4. Evaluation

## 4.1. Datasets

In order to test the generalizability of DNCP and avoid the conclusion bias caused by a single dataset, we evaluated the DNCP model with two real-world news datasets, including 230,322 news articles collected from Sohu News and 213,094 news articles from Toutiao News, with the release date between February $^ { 5 , }$ 2018 and May 5, 2018. Both textual and meta features of news articles were extracted, as well as the number of times that each news had been clicked since it was released. A lexicon that excluded stopwords and non-stopwords that appeared fewer than three times in the entire corpus was generated via the segmentation of news content. We crawled the hotness trends of terms in the lexicon according to the duration of articles between the news release date and the collection date from Sina Micro index and built a hotness trend matrix T of terms.

Previous research usually classified news articles into high- or low click news, with $^ { 1 0 , 0 0 0 }$ clicks being the cutoff point $( \mathbf { e } . \mathbf { g } . , \ [ 1 , 2 2 , 4 4 ] )$ Accordingly, in this study, we used 2-class classification by dividing the predictive model output $( \mathrm { i . e . , }$ the predicted number of clicks of a news article) into two intervals, with [0, 10<sup>4</sup>] being the low-click class (0) and (10<sup>4</sup>, ∞) being the high-click class (1), respectively. In addition, considering that the distributions of the number of news clicks in the original dataset were unbalanced (i.e., the number of low-click samples was much larger than that of high-click samples), we used the under sampling technique to make the numbers of samples in the two classes balanced. Undersampling is a well-known method to deal with the data imbalance problem by randomly selecting a subset of instances from the majority class to generate a dataset with balanced class distributions [1]. The final distributions of sample categories are shown in Table 1.

## 4.2. Experiment setup

For text representation learning, we used features of the headline and abstract, while ignoring the main body, of news because a reader would not see news content before clicking the news. We used a Chinese word segmentation tool, Jieba<sup>3</sup>, to segment the headline and abstract of news into terms, and calculated the occurrence frequency of all terms in the news corpus and removed those that occurred fewer than three times or too frequently $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } _ { }$ , top 5 %). Because 94.5% of Sohu News articles and 98.4 % of Toutiao News articles had fewer than 80 words after removing noisy and stop words, we set the maximum word sequence length as 80, and padded shorter or truncated longer sequences. A 300-dimensional word embedding pre-trained by Word2Vec [45] was utilized in the embedding layer. The cell size of GRU was empirically set as 50.

Table 1  
The Balanced Distributions of Sample Categories in the Evaluation Datasets.

<table><tr><td>Dataset</td><td>low-click</td><td>high-click</td></tr><tr><td>Sohu News</td><td>60,000</td><td>57,163</td></tr><tr><td>Toutiao News</td><td>60,000</td><td>60,690</td></tr></table>

For the hyperparameter settings of BTM, we empirically set the number of topics K = 30, α = α = 0.1, and $\beta _ { 1 } = \beta _ { 2 } = 0 . 0 1$ . The news corpus was shuffled and divided evenly into two parts, with one for BTM to generate attractiveness of words and the other for click prediction. Attractiveness, i.e., η , was independently pre-calculated based on Eq. $\eta _ { z w } ,$ 4. For the timeliness vector $t _ { i } ,$ , its dimension size was set to be 90, which was the same as the size of the hotness trend vector. The value of each element of vector $t _ { i }$ was calculated based on Eq. $^ { 6 , }$ where the temporal decay parameter $\mu$ and the hotness trend global parameter λ were empirically set as 0.03 and 0.05, respectively.

For meta feature representation learning, the size of embedding di mensions was empirically set as 50. The output dimension F of the FM method was also set as $5 0 ,$ which was the same as the dimension size of the text representation vector $\quad h _ { a } .$ The dimensionality of the factorization D was set to be 3 based on literature [46]. The meta features that we used included author, source of news, tag, category, release date, release time, release weekday, collection date, and collection time of news.

## 4.3. Baselines

In order to examine the effectiveness of DNCP, we compared its prediction performance with those of a traditional SVM model and other deep learning classification models, such as CNN-text [28], RCNN [36], and HAN [35]. We selected those models as baselines because they are commonly used text classification methods nowadays. Also, in order to investigate the impact of high-order interactions of meta features, we selected DeepFM [7] as one of the baselines, which is the state-of-the-art method of meta feature learning. The details of the baselines used in the evaluation are as follows:

$\mathbf { B O W } + \mathbf { S V M }$ used the SVM algorithm with bag-of-words (10,000 term features) as input features (term occurrence frequency).

• Avg.Emb þ SVM used the average of word embedding vectors of individual words that a news article contained as input features for an SVM classifier.

• CNN-text was a deep neural network for text representation and classification. The open implementation<sup>4</sup> of CNN-text was used in our evaluation. The sequence of words in an article was used as input features.

• RCNN added RNN layers to process the intermediate result of CNN. The model input was similar to that of CNN-text. The open imple mentation<sup>5</sup> of RCNN was used.

• HAN, which stacked BiGRU and attention layers, was aimed to capture important words in sentences. We used the open imple mentation<sup>6</sup> of HAN. The sequence of words was used as input features.

• DeepFM combined FM with a deep neural network. We used the open implementation<sup>7</sup> of DeepFM with meta features as input features.

DNCP is an integrated model, including text and meta feature rep resentation learning. We performed an ablation study to investigate the importance of each design choice based on two datasets with diverse characteristics. We developed several ablation models with different feature variations in order to gain insights into the effectiveness and impact of the attention component. Text representation learning com bined three inputs, including word sequence, attractiveness, and time liness. As a result, DNCP and the ablation models with different inputs are shown as follows:

• BiGRU scanned word sequence and used the final output state of recurrent process unit as features for classification.

• AM represented the classic attention mechanism that calculated attention weights with latent text semantic vectors.

$\mathbf { A M } ^ { * }$ included attention weights with attractiveness vectors only.

• AM^ included attention weights with timeliness vectors only.

• CAM\* included attention weights with attractiveness vectors and latent text semantic vectors.

• CAM^ integrated attention weights with timeliness vectors and latent text semantic vectors

• CAM integrated attention weights with attractiveness, timeliness, and latent text semantic vectors, namely the left part of Fig. 1 without meta features.

• DNCP included all components and used all available features.

Finally, we compared the performance of DNCP with those of the other 13 methods outlined above.

## 4.4. Evaluation metric

We divided each dataset listed in Table 1 into two sets, with 90 % for training and 10 % for testing. We trained the predictive models with the training data using different algorithms/techniques and ten-fold crossvalidation. The constructed model with the highest accuracy with the validation data among the ten models trained by each algorithm was selected as the final model for that algorithm, which was then formally evaluated with the testing data. The performance of the models with testing data was reported as the final performance of each algorithm.

The performances of the constructed prediction models were evalu ated using four metrics that have been commonly used for evaluating classification models, including precision (P), recall (R), F1-score (F), and accuracy (A) [1], which are defined in Eqs. (13)–(16). Precision is the percentage of all news identified as positive samples that are indeed positive ones; recall is the percentage of positive predictions (e.g., high-click news) that are correctly recognized; F1-score is a harmonic mean of precision and recall; and accuracy is the ratio of correctly predicted samples to the total samples.

$$
p r e c i s i o n = \frac {T P}{T P + F P}\tag{13}
$$

$$
\text { recall } = \frac {T P}{T P + F N}\tag{14}
$$

$$
F 1 = \frac {2 ^ {*} p r e c i s i o n ^ {*} r e c a l l}{p r e c i s i o n + r e c a l l}\tag{15}
$$

$$
a c c u r a r y = \frac {T P + T N}{T P + F P + T N + F N}\tag{16}
$$

where TP (true positive) denotes the number of news correctly detected as high-click news; FP (false positive) denotes the number of low-click news that are incorrectly classified as high-click news; FN (false nega tive) represents the number of high-click news that are identified as lowclick news; and TN (true negative) represents the number of correctly classified low-click news. Values of these four metrics range from 0 to 100 percent.

## 5. Results

## 5.1. Experimental results

As shown in Table 2, DNCP outperformed all the baseline models across all metrics. In order to investigate the statistical significance of superior performance of the DNCP model, we performed paired-sample t-tests to compare the performances of those baseline models against that of DNCP. The results revealed that DNCP consistently and signifi cantly outperformed all of the baseline models across all performance measures $( p < 0 . 0 0 1$ for all models except for the difference in precision between DNCP vs. CAM for Sohu News $( p < 0 . 0 1 ) $ for both datasets. The results show that DNCP has significantly superior performance of news click prediction.

In order to gain insights into the relative contribution of individual parts of DNCP to prediction performance, we further conducted a post hoc Tukey honestly significant difference (HSD) test on the perfor mances of ablation models (i.e., BiGRU, AM, AM\*, AM^, CAM\*, CAM^, CAM). The results are shown in Table 3. BiGRU was significantly inferior to most of other models, which may be attributable to the long sequence deviation that made BiGRU ineffective when memorizing long terms. Compared with BiGRU. AM, which added a laver of attention, achieved significant improvement in all four evaluation metrics $\begin{array} { r } { ( p < 0 . 0 0 1 ) , } \end{array}$ demonstrating the positive impact of the attention mechanism on alle viating sequence deviation. AM\* and AM used only attractiveness and timeliness features alone, respectively, to calculate attention weight. The differences in model performances between AM\*/AM^ and othe models (i.e., AM\*–BiGRU. AM^–BiGRU. AM\*-AM. AM^–AM. AM^–AM\*) were mostly insignificant. CAM\* concatenated the attractiveness feature as one of input sources for the attention mechanism. Compared with AM, CAM\* improved recall and accuracy significantly $( p < 0 . 0 1 )$ for both datasets. In addition, it improved precision and F1-score significantly for Toutiao News $( p < 0 . 0 1 )$ as well. After adding the timeliness feature to the input, the improvement of CAM^ in recall was even more significant than that of CAM\*, but the improvement of precision, F1-score, and accuracy was not statistically significant $( p = n . s . )$ . The timeliness feature strengthened the distinction between positive and negative samples, which could make hot news be easily found as positive samples However, it also produced a certain number of false positives, which led to insignificant improvement of precision. We noticed that CAM\* ach ieved a significant and consistent improvement over $\mathsf { A M } ^ { \ast } \left( p < 0 . 0 0 1 \right)$ which indicated that text semantics played an indispensable role in the calculation of attention weight. Similarly, the results of CAM and AM could also lead to the same conclusion. By combining attractiveness and timeliness. CAM significantly improved all performance metrics in comparison with AM $( p < 0 . 0 1 )$ , indicating that the combination of attractiveness and timeliness features drastically improved the ability of predicting news clicks. Overall, the above results clearly demonstrate that incorporating attractiveness and timeliness features of news, both individually and simultaneously, improves the performance of news click prediction models.

In order to examine the differences among attention strategies, we generated a thermodynamic diagram (Table 4) on two news headlines based on attention weight, which displays the effects of attractiveness and timeliness via a heat map. The greater a weight is, the denser the color would be. Some interesting findings have been obtained. First, conventional AM focuses on nouns and verbs, which construct the core semantics of a sentence, such as "Trump" and "make" in this example. Second, the timeliness, representing the public’s interest, is able to guide the model to pay more attention to the hot terms, such as "China" and "trade war", as shown in AM^. Compared with AM^, CAM^ achieves a compromise between the semantics of a sentence and hot trends. Third, the attractiveness suggests the eye-catching potential of words. We find that nouns, especially specific entities or celebrities, attract more clicks, as shown in AM\* and CAM\*. Finally, CAM effectively enhanced the prediction performance by integrating and balancing semantics and auxiliary features such as attractiveness and timeliness of news.

Table 2  
Means of Model Performance (%).  
Table 3

<table><tr><td rowspan="2">Models</td><td colspan="4">Sohu News</td><td colspan="4">Toutiao News</td></tr><tr><td>Precision</td><td>Recall</td><td>F1-score</td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1-score</td><td>Accuracy</td></tr><tr><td>BOW + SVM</td><td>66.54</td><td>64.34</td><td>65.42</td><td>66.02</td><td>60.39</td><td>63.86</td><td>62.08</td><td>61.64</td></tr><tr><td>Avg.Emb + SVM</td><td>62.69</td><td>66.51</td><td>64.55</td><td>63.49</td><td>60.89</td><td>69.60</td><td>64.95</td><td>63.16</td></tr><tr><td>CNN-text</td><td>74.35</td><td>69.43</td><td>72.25</td><td>71.68</td><td>73.76</td><td>74.87</td><td>73.92</td><td>74.72</td></tr><tr><td>RCNN</td><td>72.84</td><td>76.58</td><td>74.44</td><td>73.49</td><td>73.12</td><td>74.25</td><td>73.63</td><td>74.09</td></tr><tr><td>HAN</td><td>72.37</td><td>73.56</td><td>73.03</td><td>71.99</td><td>72.81</td><td>71.69</td><td>71.90</td><td>71.22</td></tr><tr><td>DeepFM</td><td>76.42</td><td>79.24</td><td>78.55</td><td>77.91</td><td>77.55</td><td>79.95</td><td>78.36</td><td>78.94</td></tr><tr><td>BiGRU</td><td>72.80</td><td>65.81</td><td>67.89</td><td>69.68</td><td>72.01</td><td>63.92</td><td>66.34</td><td>67.59</td></tr><tr><td>AM</td><td>75.41</td><td>70.18</td><td>72.81</td><td>73.54</td><td>76.26</td><td>70.35</td><td>72.29</td><td>73.03</td></tr><tr><td>AM*</td><td>73.17</td><td>70.37</td><td>71.69</td><td>72.01</td><td>71.92</td><td>67.83</td><td>69.43</td><td>69.95</td></tr><tr><td>AM</td><td>71.07</td><td>69.52</td><td>70.53</td><td>70.22</td><td>69.73</td><td>70.81</td><td>70.14</td><td>70.30</td></tr><tr><td>CAM*</td><td>77.72</td><td>74.86</td><td>75.70</td><td>75.66</td><td>78.82</td><td>74.15</td><td>76.58</td><td>76.61</td></tr><tr><td>CAM</td><td>76.94</td><td>77.63</td><td>77.30</td><td>75.94</td><td>78.66</td><td>75.36</td><td>77.04</td><td>76.76</td></tr><tr><td>CAM</td><td>79.63</td><td>78.72</td><td>79.01</td><td>79.67</td><td>80.22</td><td>78.41</td><td>79.18</td><td>79.59</td></tr><tr><td>DNCP</td><td>82.67</td><td>85.75</td><td>83.60</td><td>83.24</td><td>84.87</td><td>83.89</td><td>83.98</td><td>84.59</td></tr></table>

Tukey’s HSD Test of All Ablation Model Performances (Mean Difference).

<table><tr><td rowspan="2">Comparisons</td><td colspan="4">Sohu News</td><td colspan="4">Toutiao News</td></tr><tr><td>Precision</td><td>Recall</td><td>F1-score</td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1-score</td><td>Accuracy</td></tr><tr><td>AM-BiGRU</td><td>2.61***</td><td>4.37***</td><td>4.92***</td><td>3.86***</td><td>4.25***</td><td>6.43***</td><td>5.95***</td><td>5.44***</td></tr><tr><td>AM*-BiGRU</td><td>0.37</td><td>4.56**</td><td>3.8</td><td>2.33</td><td>-0.09</td><td>3.91</td><td>3.09</td><td>2.36</td></tr><tr><td>AM-BiGRU</td><td>-1.73</td><td>3.71*</td><td>2.64</td><td>0.54</td><td>-2.28</td><td>6.89***</td><td>3.8</td><td>2.71</td></tr><tr><td>CAM*-BiGRU</td><td>4.92**</td><td>9.05***</td><td>7.81***</td><td>5.98**</td><td>6.81***</td><td>10.23***</td><td>10.24***</td><td>9.02***</td></tr><tr><td>CAM-BiGRU</td><td>4.14***</td><td>11.82***</td><td>9.41***</td><td>6.26***</td><td>6.65***</td><td>11.44***</td><td>10.7***</td><td>9.17***</td></tr><tr><td>CAM-BiGRU</td><td>6.83***</td><td>12.91***</td><td>11.12***</td><td>9.99***</td><td>8.21***</td><td>14.49***</td><td>12.84***</td><td>12.0***</td></tr><tr><td>AM*-AM</td><td>-2.24</td><td>0.19</td><td>-1.12</td><td>-1.53</td><td>-4.34**</td><td>-2.52</td><td>-2.86</td><td>-3.08</td></tr><tr><td>AM-AM</td><td>-4.34**</td><td>-0.66</td><td>-2.28*</td><td>-3.32*</td><td>-6.53***</td><td>0.46</td><td>-2.15</td><td>-2.73</td></tr><tr><td>CAM*-AM</td><td>2.31</td><td>4.68**</td><td>2.89</td><td>2.12**</td><td>2.56**</td><td>3.8***</td><td>4.29**</td><td>3.58***</td></tr><tr><td>CAM-AM</td><td>1.53</td><td>7.45***</td><td>4.49</td><td>2.4*</td><td>2.4</td><td>5.01***</td><td>4.75*</td><td>3.73*</td></tr><tr><td>CAM-AM</td><td>4.22**</td><td>8.54***</td><td>6.2***</td><td>6.13***</td><td>3.96**</td><td>8.06***</td><td>6.89***</td><td>6.56***</td></tr><tr><td>AM-AM*</td><td>-2.1</td><td>-0.85</td><td>-1.16</td><td>-1.79</td><td>-2.19</td><td>2.98</td><td>0.71</td><td>0.35</td></tr><tr><td>CAM*-AM*</td><td>4.55***</td><td>4.49***</td><td>4.01***</td><td>3.65**</td><td>6.9***</td><td>6.32***</td><td>7.15***</td><td>6.66***</td></tr><tr><td>CAM-AM*</td><td>3.77***</td><td>7.26***</td><td>5.61***</td><td>3.93***</td><td>6.74***</td><td>7.53***</td><td>7.61***</td><td>6.81***</td></tr><tr><td>CAM-AM*</td><td>6.46***</td><td>8.35***</td><td>7.32***</td><td>7.66***</td><td>8.3***</td><td>10.58***</td><td>9.75***</td><td>9.64***</td></tr><tr><td>CAM*-AM</td><td>6.65***</td><td>5.34***</td><td>5.17***</td><td>5.44***</td><td>9.09***</td><td>3.34***</td><td>6.44***</td><td>6.31***</td></tr><tr><td>CAM-AM</td><td>5.87***</td><td>8.11***</td><td>6.77***</td><td>5.72***</td><td>8.93***</td><td>4.55***</td><td>6.9***</td><td>6.46***</td></tr><tr><td>CAM-AM</td><td>8.56***</td><td>9.2***</td><td>8.48***</td><td>9.45***</td><td>10.49***</td><td>7.6***</td><td>9.04***</td><td>9.29***</td></tr><tr><td>CAM-CAM*</td><td>-0.78</td><td>2.77**</td><td>1.6</td><td>0.28</td><td>-0.16</td><td>1.21*</td><td>0.46</td><td>0.15</td></tr><tr><td>CAM-CAM*</td><td>1.91</td><td>3.86**</td><td>3.31</td><td>4.01***</td><td>1.4</td><td>4.26***</td><td>2.6</td><td>2.98*</td></tr><tr><td>CAM-CAM</td><td>2.69**</td><td>1.09</td><td>1.71</td><td>3.73**</td><td>1.56</td><td>3.05**</td><td>2.14</td><td>2.83*</td></tr></table>

Note: \*\*\*, \*\*, and \* denote statistical significance at 0.001, 0.01, and 0.05 levels, respectively.

A Thermodynamic Diagram of Attention Weights of Terms with Different Strategies.

<table><tr><td>AM</td><td>特朗普 为何 铁了心 要 和 中国 打 贸易战?Why does Trump want to make a trade war with China?</td></tr><tr><td>AM*</td><td>特朗普 为何 铁了心 要 和 中国 打 贸易战?Why does Trump want to make a trade war with China?</td></tr><tr><td>AM^</td><td>特朗普 为何 铁了心 要 和 中国 打 贸易战?Why does Trump want to make a trade war with China?</td></tr><tr><td>CAM*</td><td>特朗普 为何 铁了心 要 和 中国 打 贸易战?Why does Trump want to make a trade war with China?</td></tr><tr><td>CAM^</td><td>特朗普 为何 铁了心 要 和 中国 打 贸易战?Why does Trump want to make a trade war with China?</td></tr><tr><td>CAM</td><td>特朗普 为何 铁了心 要 和 中国 打 贸易战?Why does Trump want to make a trade war with China?</td></tr></table>

By comparing with the baselines, both DNCP and DeepFM, which included high-order interactions of meta features through the FM component, improved the recall significantly. Therefore, the high-order interactions of meta features can significantly improve the performance of predicting news clicks.

The models based on SVM, such as BOW + SVM and Ave.Emb + SVM, performed poorly in this task, likely due to the fact that their input features ignored word context. In contrast, both CNN-text and RCNN achieved a certain level of improvement across all performance mea sures, indicating that a deep learning network can learn and use better features from news and make better predictions.

![](/api/attachments/RNKDRDU8/fulltext/images/e2476c008b00f4c4367af160de2ae50da50cbcfdc29df27f7d1e5505b292d49e.jpg)  
Fig. 3. A Correlation Analysis on Attractiveness and Timeliness with News Clicks.

## 5.2. Correlation analysis

In ablation analysis, we found that adding attractiveness and time liness features significantly improved prediction performance. There fore, we also performed a correlation analysis on attractiveness and timeliness with news clicks to explore whether high-clicked news is associated with high levels of attractiveness and timeliness. We randomly sampled 30,000 articles from the original Sohu and Toutiao datasets and made a logarithmic transformation of the number of new clicks to reduce the right skewness of data distribution. The attractive ness value of each news was calculated by averaging the attractiveness of each word in the news title.

The results of correlation analysis are shown in the two subgraphs at the top of Fig. 3, with the left one corresponding to the Sohu dataset $( r =$ $0 . 6 1 7 3 , p < 0 . 0 0 1 )$ and the right one corresponding to the Toutiao dataset $( r = ~ 0 . 5 5 7 0 , \ p < 0 . 0 0 1 )$ , respectively. The correlation co efficients are presented in Table $^ { 5 , }$ , indicating that the number of hits and attractiveness are highly correlated. Therefore, we can conclude that the attractiveness of news titles is positively correlated with the number of news clicks.

The correlation between timeliness and news clicks is also very high in both Sohu $( r = ~ 0 . 7 8 4 1 , ~ p < 0 . 0 0 1 )$ and Toutiao $( r = ~ 0 . 7 7 2 1$ $p < 0 . 0 0 1 )$ datasets, indicating that the timeliness feature plays an important role in catching readers’ attention and having them click a news link. The positive correlations between attractiveness and news clicks and between timeliness and news clicks shown above also help explain why the DNCP model outperforms the partial input models in the ablation experiment.

Table 5  
Correlation Coefficients and Significance.

<table><tr><td>Dataset</td><td>Attractiveness</td><td>Timeliness</td></tr><tr><td>Sohu News</td><td>0.6173***</td><td>0.7841***</td></tr><tr><td>Toutiao News</td><td>0.5570***</td><td>0.7721***</td></tr></table>

Note: \*\*\* denotes statistical significance at a 0.001 level.

## 6. Discussion

There has been increasing research on news click prediction due to the increasing importance of news filtering, recommendation, and optimization for news distribution and sharing. Accurate prediction of news clicks can significantly improve the efficacy of news distribution and discover news articles of high value for businesses and readers.

This study proposes an attention-based deep learning method that incorporates news attractiveness and timeliness for predicting news clicks. An empirical evaluation that involved two different news datasets clearly demonstrated the significant positive impact of the proposed news attractiveness and timeliness on prediction performance. This study makes several novel research contributions. First, we defined attractiveness and timeliness of news, and designed BTM to measure attractiveness and the hotness trend of words to reflect timeliness of news. Recent studies have started exploring the relationship between comments and views of news and provided preliminary evidence for the feasibility of news click prediction based on the number of comments on news [3]. In this study, we extended LDA by providing a quantitative measure of attractiveness based on news reading-commenting behav iors. In addition, we incorporated the concept of news timeliness in a deep neural network in that the public interest in news articles fades quickly, often within days after their release. Correlation analysis shows that attractiveness and timeliness are highly and positively correlated with news clicks.

Second, we designed, developed, and evaluated a novel, integrated deep learning model that leveraged both text and meta features, which significantly improved prediction result. Specially, we proposed CAM that combined attractiveness and timeliness of news as auxiliary features with text semantic features to achieve an enhanced attentive represen tation. Comparisons between DNCP and other ablation models in eval uation showed that the incorporation of attention weights determined based on attractiveness and timeliness of words in news articles into a prediction model led to higher quality of attentive representation. The proposed idea of incorporating auxiliary features into an attention mechanism to find more important words is generic and can thus be generalized to enhance text representation in many other scenarios.

Third, we enhanced processing of meta features with FM to address the problem of feature sparsity and high-order interaction of meta fea tures effectively, which further improves prediction accuracy. More importantly, meta and text features are processed simultaneously in DNCP, which reduces training complexity.

This research also offers several practical implications. Predicting news clicks is of great value to business and individuals. First, predicting future clicks of news can help news agencies, marketing companies, internet search engines, and news recommendation systems allocate more resources to news that are more likely to receive more clicks (i.e., views), optimize news content and layout, upgrade news ranking stra tegies, and improve recommendation algorithms, etc. Second, the measure of attractiveness proposed in this study can help news writers improve writing quality and create more attractive news. Third, time liness provides a quantitative measure of the life cycle of news, which can be used to identify hot news articles. Last but not least, the findings of this research imply that it would be beneficial to combine text and meta features while building news click prediction models. The high order interactions of meta features can also significantly improve pre diction performance.

This study has some limitations that offer potential opportunities for future research. First, the data used in evaluation were collected from two Chinese online news sources (Sohu,com and Toutiao.com). It would be beneficial to validate the proposed approach with news corpora in different languages in future research. Second, we used FM in this study because of its rigorous theoretical derivation and high computational efficiency. It has been widely used in research and industry [13]. Although using other extensions of FM such as attentional factorization machine (AFM) [47], eXtreme deep factorization machine (XDeepFM) [48], and interaction-aware factorization machine (IFM) [49] in DNCP may lead to different model performance, the main intention of this study is not to investigate which one of those alternative methods is the best, but to investigate if the meta features of news and their high-order interactions can improve news click prediction, in which FM is appro priate and sufficient. Also, we included a variety of baseline models in this study, including DeepFM, which enabled us to isolate the effects of the target variables. We plan to assess the performance of DNCP with other variations of FM in future research to explore the impact of such a method on the prediction of news clicks.

## CRediT authorship contribution statement

Jie Xiong: Methodology, Validation. Li Yu: Supervision, Writing - review & editing, Conceptualization, Methodology. Dongsong Zhang: Supervision, Writing - review & editing. Youfang Leng: Validation.

## Acknowledgement

This research was supported in part by the National Science Foun dation (SES-152768, CNS 1704800). Any opinions, findings or recom mendations expressed here are those of the authors and are not necessarily those of the sponsor of this research.

## References

[1] A. Tatar, M.D. de Amorim, S. Fdida, P. Antoniadis, A survey on predicting the popularity of web content, J. Internet Serv. Appl. 5 (August 1) (2014) 8.

[2] Y. Keneshloo, S. Wang, E.H. Han, N. Ramakrishnan, Predicting the popularity of news articles, Siam International Conference on Data Mining (2016) 441–449.

[3] A. Tatar, P. Antoniadis, M.D. de Amorim, S. Fdida, From popularity prediction to ranking online news, Soc. Netw. Anal. Min. 4 (February 1) (2014) 174.

[4] R. Bandari, S. Asur, B.A. Huberman, The Pulse of News in Social media: Forecasting Popularity, vol. 12, 2012, pp. 26–33. Feb.

[5] Q. Zhao, M.A. Erdogdu, H.Y. He, A. Rajaraman, J. Leskovec, Seismic: a self-exciting point process model for predicting tweet popularity, Proceedings of the 21th Acm Sigkdd International Conference on Knowledge Discovery and Data Mining (2015) 1513–1522.

[6] T. Young, D. Hazarika, S. Poria, E. Cambria, Recent trends in deep learning based natural language processing, IEEE Comput. Intell. Mag. 13 (3) (2018) 55–75.

[7] H. Guo, R. Tang, Y. Ye, Z. Li, X. He, DeepFM: a factorization-machine based neural network for ctr prediction, Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence, IJCAI-17 (2017) 1725–1731.

[8] M. Tsagkias, W. Weerkamp, M. de Rijke, Predicting the volume of comments on online news stories. Proceedings of the 18th Acm Conference on Information anc Knowledge Management (2009) 1765–1768.

[9] L. Marujo, M. Bugalho, J. Pda S. Neto, A. Gershman, J. Carbonell, Hourly traffic prediction of news stories, arXiv preprint arXiv 1306 (4608) (2013).

[10] K. Cho, et al., Learning phrase representations using rnn encoder-decoder fo statistical machine translation, arXiv preprint arXiv 1406 (1078) (2014).

[11] P. Biyani, K. Tsioutsiouliklis, J. Blackmer, “8 Amazing Secrets for Getting More Clicks”: Detecting Clickbaits in News Streams Using Article Informality, AAAI, 2016, pp. 94–100.

[12] D.M. Blei. A.Y. Ng, M.J. Jordan. Latent dirichlet allocation, J. Mach. Learn. Res. 3 (January) (2003) 993–1022.

[13] S. Rendle, Factorization machines, IEEE International Conference on Data Mining (2011) 995–1000.

[14] G. Szabo, B.A. Huberman, Predicting the popularity of online content, Commun. ACM 53 (August 8) (2010) 80–88.

[15] H. Pinto, J.M. Almeida, M.A. Gonçalves, Using early view patterns to predict the popularity of youtube videos, Proceedings of the Sixth Acm Internationa Conference on Web Search and Data Mining (2013) 365–374.

[16] G. Gürsun, M. Crovella, I. Matta, Describing and Forecasting Video Access Patterns, INFOCOM, 2011 proceedings ieee, 2011, pp. 16–20.

[17] X. He, M. Gao, M.Y. Kan, Y. Liu, K. Sugiyama, Predicting the popularity of web 2.0 items based on user comments, International Acm Sigir Conference on Research & Development in Information Retrieval (2014) 233–242.

[18] K. Lerman, T. Hogg, Using stochastic models to describe and predict social dynamics of web users. ACM Trans. Intell, Syst, Technol, 3 (4) (2012) 1–33.

[19] P. Yin, L. Ping, W. Min, W.C. Lee, A straw shows which way the wind blows: ranking potentially popular items from early votes. Acm International Conference on Web Search & Data Mining (2012).

[20] S. Van Canneyt, P. Leroux, B. Dhoedt, T. Demeester, Modeling and predicting the popularity of online news based on temporal and content-related features, Multimed, Tools Appl, 77 (January 1) (2018) 1409–1436

[21] S. Jamali, H. Rangwala, Digging digg: comment mining, popularity prediction, and social network analysis, International Conference on Web Information Systems & Mining (2009).

[22] X. Guan, Q. Peng, Y. Li, Z. Zhu, Hierarchical neural network for online news popularity prediction. 2017 Chinese Automation Congress (CAC), 2017, pp. 3005–3009.

[23] W. Stokowiec. T. Trzciński. K. Wołk. K. Marasek. P. Rokita, Shallow reading with deep learning: predicting popularity of online content using only its title International Symposium on Methodologies for Intelligent Systems (2017 136-145.

[24] Y. Guo, Z. Cheng, L. Nie, Y. Wang, J. Ma, M. Kankanhalli, Attentive long short-term preference modeling for personalized product search, Acm Trans. Inf. Syst. Secur. 37 (January 2) (2019) 19. 1–19:27

[25] T. Mikoloy. I. Sutskever. K. Chen. G.S. Corrado, J. Dean. Distributed representations of words and phrases and their compositionality. Advances in Neural Information Processing Systems, 2013, pp. 3111–3119.

[26] J. Pennington, R. Socher, C.D. Manning, Glove: global vectors for word representation, Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (Emnlp) (2014) 1532–1543.

[27] D.R. So, C. Liang, Q.V. Le, The evolved transformer, arXiv preprint arXiv 1901 (11117) (2019).

[28] Y. Kim, Convolutional neural networks for sentence classification, arXiv preprint arXiv 1408 (5882) (2014).

[29] Y.N. Dauphin, A. Fan, M. Auli, D. Grangier, Language modeling with gated convolutional networks, in: Proceedings of the 34th International Conference on Machine Learning, 70, 2017, pp. 933–941.

[30] A. Vaswani, et al., Attention is all you need. Advances in Neural Information

[31] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, Bert: pre-training of deep bidirectional transformers for language understanding, arXiv preprint arXiv 1810 (04805) (2018).

[32] K. Clark, M.-T. Luong, Q.V. Le, C.D. Manning, Electra: pre-training text encoders as discriminators rather than generators, arXiv preprint arXiv 2003 (10555) (2020)

[33] Y. Liu, et al., Roberta: a robustly optimized bert pretraining approach, arXiv preprint arXiv 1907 (11692) (2019).

[34] Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R.R. Salakhutdinov, Q.V. Le, Xlnet: generalized autoregressive pretraining for language understanding, Adv. Neural Inf. Process. Syst. (2019) 5754–5764.

[35] Z. Yang, D. Yang, C. Dyer, X. He, A. Smola, E. Hovy, Hierarchical attention networks for document classification, Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (2017) 1480–1489.

[36] S. Lai, L. Xu. K. Liu, J. Zhao. Recurrent Convolutional Neural Networks for Text Classification, 333. AAAI. 2015. pp. 2267–2273.

[37] J.E. Meng, Y. Zhang, N. Wang, M. Pratama, Attention pooling-based convolutional neural network for sentence modelling, Inform. Sci. Int. J. 373 (C) (2016) 388–403.

[38] T.L. Griffiths, M. Steyvers, Finding scientific topics, Proc. Natl. Acad. Sci. 101 (suppl 1) (2004) 5228–5235.

[39] Q. Chen, Q. Hu, J.X. Huang, L. He, W. An, Enhancing recurrent neural networks with positional attention for question answering, Proceedings of the 40th International Acm Sigir Conference on Research and Development in Information Retrieval (2017) 993–996.

[40] J. Wang, et al., Dynamic attention deep model for article recommdation by learning human editors’ demonstration, ACM Sigkdd International Conference on Knowledge Discovery and Data Mining (2017) 2051–2059.

[41] J. Chen, H. Zhang, X. He, W. Liu, W. Liu, T.S. Chua, Attentive collaborative filtering: multimedia recommendation with item- and component-level attention, International Acm Sigir Conference on Research and Development in Information Retrieval (2017) 335–344.

[42] H.-T. Cheng, et al., Wide & deep learning for recommender systems, Proceedings of the 1st Workshop on Deep Learning for Recommender Systems (2016) 7–10

[43] D.P. Kingma, J. Ba, Adam: a method for stochastic optimization, International Conference on Learning Representations (2015)

[44] L. Hong, O. Dan, B.D. Davison, Predicting popular messages in twitter, International Conference on World Wide Web (2011).

[45] S. Li, Z. Zhao, R. Hu, W. Li, T. Liu, X. Du, Analogical reasoning on chinese morphological and semantic relations, Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) (2018) 138–143.

[46] S. Rendle, Factorization machines with libfm, ACM Trans. Intelligent Syst. Technol. (TIST) 3 (3) (2012) 57.

[47] J. Xiao, H. Ye, X. He, H. Zhang, F. Wu, T.-S. Chua, Attentional factorization machines: learning the weight of feature interactions via attention networks, arXiv preprint arXiv 1708 (04617) (2017).

[48] J. Lian, X. Zhou, F. Zhang, Z. Chen, X. Xie, G. Sun, XDeepFM: combining explicit and implicit feature interactions for recommender systems, Proceedings of the 24th

Acm Sigkdd International Conference on Knowledge Discovery & Data Mining (2018) 1754–1763

[49] F. Hong, D. Huang, G. Chen, Interaction-aware factorization machines for recommender systems, in: Proceedings of the AAAI Conference on Artificia Intelligence, 33, 2019, pp. 3804–3811.

Jie Xiong is a pH.D. student at the School of Information, Renmin University of China. He received his master’s degree in computer science and technology from University of Chinese Academy of Sciences. His research focuses on big data analysis, natural language processing.

Li Yu is Associate Professor with the Vice Chair of Economic Information Management of Renmin University of China. His research topics focus on big data analysis and application, recommendation system, deep learning, Internet plus and innovation, data mining and business intelligence, social network marketing, financial data mining and analysis, ecommerce, Web2.0 and social computing, knowledge management, IT project manage ment, etc. He received a Doctor of System Engineering from Beijing University of Aero nautics and Astronautics (BUAA) in 2004. He has published more than 40 papers in important academic journals and conferences, and won awards for outstanding scientific research achievements and teaching achievements of Renmin University of China

Dongsong Zhang joined the Department of Business Information Systems & Operations Management at UNC Charlotte as a Belk Distinguished Professor in Business Analytics. Before joining UNC Charlotte, he was a tenured Full Professor in the Department of In formation Systems at the University of Maryland, Baltimore County. He received his pH.D. in Management Information Systems from the Eller School of Management at the Uni versity of Arizona in 2002. His current research interests include social computing, health IT, mobile HCI, business intelligence, and online communities. Zhang has published approximately 150 research articles in journals and conference proceedings, and has received a dozen research grants and awards from the National Science Foundation (NSF) National Institutes of Health (NIH). U.S. Department of Education, Google Inc., National Natural Science Foundation of China, Chinese Academy of Sciences, and the Royal Society of British, etc. He has served as a conference chair or program chair of a number of in ternational conferences and workshops, and is currently a senior or associate editor of multiple international journals.

Youfang Leng is a pH.D. student at the School of Information, Renmin University of China. He received his master’s degree in computer science and technology from Chengdu University. His research focuses on natural language processing and recommendation system.
