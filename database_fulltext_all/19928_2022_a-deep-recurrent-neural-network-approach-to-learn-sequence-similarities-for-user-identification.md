---
otero_id: 19928
otero_key: "X4AU9AHM"
title: "A deep recurrent neural network approach to learn sequence similarities for user-identification"
authors: "Stefan Vamosi; Thomas Reutterer; Michael Platzer"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113718"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A deep recurrent neural network approach to learn sequence similarities for user-identification

![](/api/attachments/X4AU9AHM/fulltext/images/ba89b9013ef6c4da2d623d6d7631f31d50972d6c04c895df0a01f64506207acb.jpg)

Stefan Vamosi <sup>a</sup>, Thomas Reutterer <sup>a,\*</sup>, Michael Platzer <sup>a,b</sup>

<sup>a</sup> Department of Marketing, Vienna University of Economics and Business, Wirtschaftsuniversitat Wien, Viennna, Austria <sup>b</sup> MOSTLY AI Solutions, Hegelgasse 21/3, A-1010 Vienna, Austria

## A R T I C L E I N F O

Keywords: Sequence similarity Embeddings Deep learning User identification Similarity matching Sequence clustering

## A B S T R A C T

The evolving digital economy entails multifaceted behavioral tracking data such as internet clickstreams, loca tion trajectories. or taste preferences revealed by music or video streaming, Organizations are increasingly interested in using such data streams to profile customers based on their behavioral similarities for targeting purposes. However, measuring similarities in sequential data is a challenging task. We present a generic deep neural-network-based framework for quantifying the similarity of ordered sequences in observed event histories. This novel approach combines a specific type of recurrent neural nets with a triplet loss cost function used for network training. It yields an embedding space that serves as a similarity metric for complex sequential data, can handle multivariate sequential data and incorporate covariates. We empirically validate the derived similarity metric for user embeddings in the domain of re-identifying users in web browsing histories. We demonstrate its superior performance in discriminating users based on their behavioral browsing patterns by benchmarking against more conventional approaches to measure sequence similarity. In addition, we show that the method ology can be used for clustering sub-sequences and re-classifying users based on their observed clickstream behavior. Finally, we critically reflect benefits and possible downsides of the proposed framework, discuss ex tensions and promising future applications. An open-source reference implementation can be obtained from github.com/vamosi/tl\_rnn.

## 1. Introduction

In many application domains, it is essential to identify the charac teristics of individual-level event histories, which are typically repre sented as temporal, ordered sequences of single events. Sequential behavioral data can be found in a variety of contexts, such as shopping and internet browsing behavior [1,2], music and video streaming [3,4], financial transactions [5] or geo-location data [6]. Generally, such re cords reflect how individuals make dynamic choices and thus contain valuable information for managerial decision-making [7].

In this paper, we focus on a specific prerequisite for leveraging value from sequential user behavior: measuring sequence similarity. To this end, we derive an embedding space that defines a similarity metric for sequential user behavior. The ability to make inferences about sequence similarities is critical in many business settings that include such diverse cases as studying prototypical supermarket shopping paths or travel activity histories [8,9], combining clustering and visualization of sequential data [10], analyzing customer acquisition sequences and cross-selling opportunities [11,12] or studying similarities in medical event sequences to predict mortality [13]. Other areas where matching similar sequences plays an important role is object and user (re-)iden tification. For example, Zhang et al. [4] identify movie raters through subspace clustering and Jiang et al. [14] apply a graph approach to identify users of an online streaming service. Prominent applications of object identification are fingerprinting of audio or video files based on various types of hashing techniques [15].

Despite this apparent importance of the concept of sequence simi larity, it still remains opaque what it exactly means that sequentially ordered data are considered to be “similar”. Furthermore, measuring the similarities of sequences adequately and in a computationally efficient manner remains challenging because the high dimensionality of the corresponding data space. Consider, for example, the clickstream data resulting from the browsing behavior of individuals across 10,000 website domains. The number of possible sequences of length n is 10<sup>4n</sup>, and that number grows exponentially with sequence length. For a moderate sequence length of n = 20, the number of possible sequences is roughly equal to the number of atoms in the known universe. We operate in such sparse data space when looking for a useful similarity measure that reflects the characteristics of the recorded individuals. Fig. 1 illus trates the motivation behind our conceptual model for learning sequence similarities. Building on to the basic principles employed by Google’s FaceNet [16] for face recognition, our machine learning approach is learning similarities by contrasting anchor and positive examples of the same identity from negative examples of different identity. Akin to distinguishing between faces, sequences can be differentiated by looking into specific patterns as well. In the case of a signature, it could be a certain pencil stroke or writing style that dif ferentiates two specific individuals. Our approach generalizes this idea and in our empirical application study we will focus on “snippets” of internet browsing histories drawn from different users. The right-hand side of Fig. 1 displays three samples, consisting of visited domains dis played in sequential order from top to bottom. While all three sequences share some common domains, in this particular case, visits to travel sites (expedia.com and kayak.com) appear to be characteristic for subject #123.

The process required to draw such conclusions manually is prone to errors and a massive undertaking. Our presented methodology allows us to make these inference quickly in a fully automated fashion with high accuracy. The proposed method uses a specific recurrent neural network (RNN) architecture combined with a triplet loss function we use for training the network parameters. This combination allows the model to “learn” similarities in sequentially ordered data based on discriminative triplets of samples like the one presented in Fig. 1. Once network training is completed, the model is capable of capturing and trans forming the characteristic patterns of a sequence into a vector repre sentation of the sequences similarity space. The latter can serve as a measurement instrument for similarity matching, clustering of sequen tial data and other use cases including fingerprinting of sequential data streams.

We next introduce the building blocks of the model and our proposed approach for learning sequence similarity. We also discuss imple mentation of the network architecture and training using a triplet loss function. Then, we illustrate the performance and potential empirical applications of the tool in the context of user (re-)identification and clustering using browsing histories we obtained from the Comscore web behavior panel. Finally, we discuss limitations, outline potential exten sions and suggest avenues for future research.

## 2. Modeling approach and network architecture

Our approach to a general framework for learning sequence simi larities consists of two structural building blocks. As an outcome, we create an embedding space in which each sequence’s representation is an efficient summary of the key characteristics of that ordered sequence of events.

## 2.1. Long short-term memory embedding space

The core component of our sequence similarity method consists of a layer of long short-term memory (LSTM) cells. As a special type of RNNs, LSTM-based deep learning networks have been successfully applied to a variety of tasks involving complex sequential data, including speech recognition, language translation, and natural language modeling [17]. The LSTM cell was first introduced by Hochreiter and Schmidhuber [18] and was further completed by Gers, Schmidhuber and Cummins [19] with a “forget gate” to circumvent the vanishing gradient issue associ ated with RNNs. This property allows LSTM-based RNNs to handle long-term dependencies successfully and to selectively memorize in formation from the more-distant past [20]. In our proposed model ar chitecture for measuring sequence similarities the LSTM layer acts as an “embedder”, which translates a complete sequence of variables into a high-dimensional vector representation.

More precisely, the resulting cell-state vectors, c, of an LSTM network with d cells reside in $\mathbb { R } ^ { \breve { d } }$ and are bounded in a d-dimensional box of size $[ - n ^ { d } , + n ^ { d } ]$ in which n is the sequence length. To derive a sequence similarity measure using the model, we leverage the numerical vector representation of a sequence’s characteristics relevant to simi larity learning. In the special case of our use of LSTM layers, these characteristics are condensed in the cell-state vector. The cell-state propagates for successive time steps and is enriched by new informa tion from the LSTM’s input gate or degraded by its forget gate if necessary. The cell-state information is used directly in the triplet loss function for error back-propagation.

## 2.2. Triplet loss for learning sequence similarity

In sharp contrast to conventional similarity metrics that rely on prior assumptions, modern contrastive loss approaches make inferences about object similarities based solely on discriminative examples. Bromley et al. [21] introduced the famous approach of “Siamese” Neural Net works on the example of signature verification. Siamese networks learn similarities and dissimilarities by feeding sample pairs of the same origin and sample pairs of different origins alternately into a two-channel network with shared layers. During learning, the network is forced to push representations of two distinct origins away, whereas samples of the same origin are placed closer to each other. It is based on the general idea that the distance between samples from a single origin should be smaller than the distance between samples from different origins.

A further development in the field of similarity based loss functions is a concept called triplet learning (or triplet comparison) [22]. It combines the two-step approach of Siamese networks into a single loss calculation by feeding a triplet of samples into a shared three-layer network. This triplet consists of two samples from the same originator and one “spam” sample from another user. This way, triplet learning constructs a simi larity or distance metric by discriminating small intra-class variations from large inter-class variations. Since its introduction, it has been widely and successfully applied for various tasks, such as learning image similarities and image processing tasks like face recognition or person re-identification [23]. It was particularly popularized by Google’s FaceNet publication [16]. More recently, a quadruplet approach has been introduced which extends the triplet loss by adding an additional term (i.e., another “spam” sample from a third origin) to enlarge the inter-class variation and decrease the intra-class variation [24]. We tested and compared the triplet and the quadruplet loss in our empirical setup and found that they performed equally well. Thus, we favor the triplet loss due to simpler data-structure, pre-processing, and shorter run-time. However, to the best of our knowledge no studies have adopted the conceptual idea of triplet loss in the context of sequential data. Our goal is to generalize from training samples to new (holdout) data, which is particularly challenging in structure-seeking approaches like the one we propose.

In the case of face recognition and person re-identification, samples from a single origin denote images from one person. Fig. 2 illustrates this idea in the context of sequential data. Two sequences, the so-called anchor $\pmb { \mathrm { c } } _ { \mathbf { 0 } }$ and the positive sample $\mathbf { c } _ { + } ,$ , are from the same user but from different observation time windows, and the negative sample c is from a different user.<sup>1</sup> During network training, the cost function applied to such a triplet of samples is gradually decreased such that the distance between the anchor and the positive sample becomes smaller, while the distance between the anchor and the negative sample simul taneously becomes larger.

The triplet loss function can be formally described as follows:

![](/api/attachments/X4AU9AHM/fulltext/images/d7920ccf6ac5836ff22328b77619afad743f5035ae80acfe2094b5b6b700e7cf.jpg)  
Fig. 1. The motivation behind our approach to learning sequence similarity: from image similarity to sequence similarity. Browsing behavior is like a signature, characteristic patterns distinguish individuals from each other.

![](/api/attachments/X4AU9AHM/fulltext/images/42768f82cc50fdb1b0ed6c8c7013413bc92e530cbca6931413751f30d28d8216.jpg)  
Fig. 2. The triplet comparison operates on three different sequences from two different users.

$$
L _ {\text { triplet }} = \max [ \beta \| c _ {0} - c _ {+} \| _ {1} - \gamma \| c _ {0} - c _ {-} \| _ {1} + \alpha , 0 ]\tag{1}
$$

with c being the LSTM cell-state vectors as abstract representations of the information about a sequence.<sup>2</sup> Eq. (1) includes three hyperparameters acting as regularizers, where β and $\gamma$ control the push-pull relation depicted symbolically in Fig. 2. While some authors suggest setting $\beta > \gamma$ and thus putting more weight on the intra-class “pull” than on the inter-class “push” [25], we favor a balanced push-pull relation (i. $\mathrm { e } . , \beta = \gamma )$ after completing extensive tests of re-identification setups. As a positive side effect, this reduces the hyper-parameter space.

During the gradient descent procedure, α determines the targeted margin between samples from the same user and samples from different users. If α is too small, the push–pull relation is weak and the full discriminative potential is not fully leveraged. If α is too large, the triplet loss performance on new data is diminished because of over-fitting. Thus, in practical applications, α must be evaluated using a grid search.

A deeper analysis of the triplet loss when $\beta = \gamma$ reveals that triplet can be further categorized. The negative sample of this triplet can be classified in three domains:

• Easy negatives: $\| \mathbf { c } _ { 0 } - \mathbf { c } _ { - } \| \geq \left| \left| \mathbf { c } _ { 0 } - \mathbf { c } _ { + } \right| \right| + \alpha$

• Semi-hard negatives: $\| \mathbf { c _ { 0 } } - \mathbf { c } _ { + } \| < \left| \left| \mathbf { c _ { 0 } } - \mathbf { c } _ { - } \right| \right| < \left\| \mathbf { c _ { 0 } } - \mathbf { c } _ { + } \right\| + \alpha$

• Hard negatives: $\| \mathbf { c } _ { 0 } - \mathbf { c } _ { - } \| \leq | | \mathbf { c } _ { 0 } - \mathbf { c } _ { + } | |$

The easy negatives are triplets in which the negative sample is separated more from the anchor than from the positive sample plus margin α. Hence, it results in a loss of zero. The semi-hard negatives are triplets in which the negative sample is farther from the anchor than the positive sample, but the difference is less than α. For hard negatives, the negative sequence is closer to the anchor than to the positive sequence. Take as an example, the three sequences from two users we already discussed above and place them on a plane like the one shown in Fig. 3. According to the distances to each other and a given value of alpha, the negative sample can be categorised in this case as a semi-hard negative one. Note that during training, the network learns from hard negatives and semi-hard negatives. While Schroff et al. [16] concentrate on semi-hard negatives for each triplet, we find, through empirical vali dation of our approach, that prioritizing semi-hard samples is not beneficial when discriminating instances in the context of sequential data. Rather, we consider all kinds of triplets (including semi-hard and hard negatives) for learning and testing.

## 2.3. Network model architecture

Our model’s network architecture is inspired by the latest image recognition projects but needs to cope with some unique challenges posed by sequential data. This is accomplished by a block of LSTM layers that handle sequential data. Our model differentiates three “channels”, each of which is responsible for one part of the triplet sample (anchor, positive sample or negative sample) as shown in Fig. 4, in which batches of triplets sampled from different users flow from left to right to train the LSTM network. Furthermore, the event and timing information must be adequately represented.

Note that information for each channel flows through the same network with weights shared across channels but contributes to the triplet loss function $L _ { t r i p l e t } = m a x [ \| \mathbf { c _ { 0 } } - \mathbf { c _ { + } } \| _ { 1 } - \| \mathbf { c _ { 0 } } - \mathbf { c _ { - } } \| _ { 1 } + \alpha , ~ 0$ ] separately as the anchor channel, positive channel and negative chan nel. Thus, while conducting network training, triplet loss is calculated by using the three LSTM cell states simultaneously.

In inference mode, the trained network is used to translate each focal input sequence into one cell-state vector. As the network weights are trained to discriminate between sequences based on behavioral differ ences between users, the network can transform the sequences accord ingly. And since the three network channels (anchor, positive, and negative) consist of shared network weights, it does not matter which input is used for prediction. For this reason, we put one sequence after the other through the inference channel and pick up the vector co ordinates output by the network for further processing like performing distance comparisons between vectors or for cluster analyses on en sembles of sequences.

Besides data structure and neural network type, our approach also differs from applications of triplet learning for static data in that we take advantage of embedding layers between the input layer and the LSTM layer. This embedding layer acts on each time-step (event) and trans forms each input into a lower-dimensional vector representation in which similar objects are placed closer to each other. For example, booking holiday flights might always involve comparing prices on several sites (e.g., booking.com, expedia.com). Thus, similarity of events is established when they appear in the same sequence. Note that this embedding layer differs from pre-embeddings of the word2vec type, because we optimized the embedding on the triplet loss function in order to increase the performance on the specific re-identification task. In addition to capturing relations between the specific events to enhance the network’s overall performance, embedding drastically reduces the input vector dimension. For one-hot encoding, the input dimension equals the cardinality of events, 10,000 components in our case. This procedure is similar to a word embedding [26] in which similar words are placed closer together in the embedding space. Though embeddings improve performance by only about 0.5% (and therefore are not crucial for the success of our application), they speed up computation by a factor of ten and thus are used in the model.

Note that the embedding layer must not be confused with the entire modeling framework, which in turn represents an embedding for se quences, since it provides an injective function $f : S ( \mathbf { x } _ { \mathrm { n } } ( t ) ) {  } \mathbb { R } ^ { d }$ where S represents the originating space of raw sequences and $\mathbb { R } ^ { d }$ is the cell-state vector space of c.

## 2.4. Network training and model implementation

Our goal is to learn an embedding space for sequential data which consist of discrete events over time: $S = ( \mathbf { x } _ { 1 } ( t _ { 1 } ) , \mathbf { x } _ { 2 } ( t _ { 2 } ) , \mathbf { x } _ { 3 } ( t _ { 3 } ) , \ldots , \mathbf { x } _ { \mathbf { n } } ( t _ { n } ) )$ with $\mathbf { x } _ { 1 } \in \mathbb { R } ^ { \Omega }$ being Ω-dimensional vectors with numerical components and t ∈ ℝ being the continuous time index associated with event $\mathbf { x } _ { \mathrm { l } } ,$ which can be recurrent [27]. Training of our neural net is conducted via error back-propagation [28] performed on small batches of input sam ples and calculating the sum of the batch sample losses. When each sample has been used once for training, that cycle is called an epoch and the model then calculates the validation error using a reserved set of triplets that are not used for training. The error measure is the per-sample loss according to our triplet loss function. This procedure allows training to stop at the point at which the model best generalizes without over-fitting (bias-variance trade-off [29]). Each epoch starts with a fresh draw of sampled triplets, to increase variance in anchor-negative-user combinations.

At the end of training the network has “learned” to project sequences of the same user close to each other and to push sequences of different users farther apart in the cell-state space. This property allows us to establish a user embedding space that quantifies the observed (dis) similarities as abstract representations of the distance between sequences.

The comparative metric used in the triplet loss function in Eq. (1) to evaluate disparities between the anchor and the positive/negative samples must be defined beforehand. Though the Euclidean distance metric $( L _ { 2 }$ norm) has been used in most image recognition tasks, Aggarwal et al. [30] have shown that, for high-dimensional problems, the $L _ { 1 }$ norm (Manhattan distance or Taxi norm) is preferable. They formally proved that the contrast between the average distance of two vectors (i) vanishes for every $L _ { \lambda }$ norm with $\lambda > 2 ,$ , (ii) is constant for the Euclidean norm $\left( \lambda = 2 \right)$ and (iii) is maximized for $\lambda = 1$ as d → inf (d is the number of dimensions). We confirmed this in our proposed model architecture, which involves 512 dimensional state vectors and renders the most accurate and stable results when using the $L _ { 1 }$ norm. In our case, greater stability means a lower sensitivity to α.

As illustrated in our above discussion of Fig. 3, the hyper-parameter α determines the targeted separation between positive and negative samples. We evaluate α using a grid search since there is no analytical formula to estimate it. To determine the bes $\alpha ,$ its value must be iterated through a reasonable interval. After each training run, the inferential power is validated on the holdout dataset according to the performance evaluation presented in Section 3.3. Note that the optimal α depends strongly on sequence length.

We implemented the neural network model in Python using the Keras open source deep learning library running on top of Tensorflow.<sup>3</sup> The models were trained on a machine equipped with an 8-core CPU and an Nvidia Titan V GPU to accelerate neural network training. As an optimizer for gradient descent, the well-established Adam method [31] for stochastic optimization was used. The number of LSTM cells inside the LSTM layer determines the dimensionality of the output state vector since it is the last laver.

The best results were achieved with a neural network structure composed of one LSTM layer and a relatively large number of 512 cells. Note that larger cell numbers would result in faster over-fitting ac cording to our validation procedure without increasing accuracy. A smaller number of cell-states would lead to under-fitting and reduced accuracy. Therefore, we chose 512 cells as a number of powers of 2 for computational reasons. The fully connected network contains about 1.5 million trainable parameters (weights).

![](/api/attachments/X4AU9AHM/fulltext/images/0edebc46a3eadc528187d636e959d98b79d86f03658f44a772daee6dd8adef1f.jpg)  
Fig. 3. Three regions of the negative sample related to the anchor and the positive sample. (Adapted from https://omoindrot.github.io/triplet-loss)

![](/api/attachments/X4AU9AHM/fulltext/images/1dbc3340a97e2d23fb7416fea1bf9a02358d52ec4cedd84b4721fd646f37be1d.jpg)  
Fig. 4. Network structure of the proposed triplet loss RNN model.

## 3. Empirical performance evaluation

As a potential application that can benefit from the derived sequence similarity embeddings, we demonstrate the empirical performance of the proposed triplet loss RNN (TL-RNN) in the context of user (re-) identification by sequentially tackling tasks of increasing difficulty: (i) user re-identification in a dual choice set-up, (ii) re-identification of multiple users, and (iii) predictions of the active number of users in given sequence records.

Note that we examine the model’s performance using different sequence lengths in all of these task settings. For network training, the hyper-parameter α is optimized specifically for each sequence length. Although the model is capable of coping with variable and unlimited sequence length, we concentrate in this study on fixed sequence lengths to avoid arbitrary session cut-offs and to get a better sense of the impact of various sequence lengths on the model’s behavior and task perfor mance. Once a network is fully trained and optimized, it serves as a similarity measure for all three applications.

## 3.1. Dataset and preparation

To study the empirical performance of our approach, we use click stream data acquired from the Comscore Web Behavior Panel (com score.com). The dataset contains web browsing activity from a U.S. household panel for 2014 and consists of almost 70 million recorded visits across 1.7 million distinct websites. Each visit record includes the top-level domain, date and time, number of viewed pages and visit duration in seconds. The overall level of activity of the users varies widely, and ranging from a few hundred to tens of thousands of site visits per year. We restrict the analysis to users who browsed between 1000 and 10,000 times in 2014. This way, we ended up with 21,000 users in the studied dataset out of approximately 40,000 users included in the panel. Fig. 5 shows a histogram of the selected users, which represents the majority of the users in the panel and challenge the model with a heterogeneous cohort.

To test the model’s performance, we focus our evaluation on the 10,000 most visited sites, which covered around 80% of the domain visits. The log-scaled frequency distribution of total visits in 2014 for the top 10,000 domains shows an inverse decay of domain presence, illus trated in Fig. 5b. In linguistic word distributions, this phenomenon is well-known as Zipf’s law and can be observed in various contexts, including distributions of city population sizes, purchase behavior, and web browsing [32]. The average user visited 675 top-level domains during the observation period with a strongly peaked distribution around the mean value. Note that a large number of commonly visited domains implies that those domains will be observed in many sequences, making them comparable but more difficult to discriminate. On the other hand, rare domains can be stronger identifiers of a specific users behavior; at some point, however, domains that are highly unlikely to appear in two randomly selected snippets of user histories. Take the case from our running example in Fig. 1, for instance; kayak.com (ranked # 902) was a stronger indicator of similarity than the more frequently visited usatoday.com (ranked # 352). Our sensitivity analyses support this observation, showing that incorporation of a greater number of domain types does not improve the accuracy of the model and just negatively affects the computation time.

The 10 most-visited sites are reported in Fig. 6; those sites account for 24.6% of all visits, with google.com accounting for 7.55% of all visits. Furthermore, almost all users visited the top four domains at least once in the observation period (Fig. 6b). For example, 99.57% of all users visited google.com at least once in 2014. Fig. 7 depicts variations in the shares of visits to specific sites as boxplots. We observe narrow inter quartile ranges but also numerous outliers. The figure displays visits to the four most popular and four least popular domains considered in our subsequent empirical study. Most users are characterized by a relatively small bandwidth of visitation shares, but many users fall at the extremes of the spectrum with very small or very large numbers of visits to a particular site.

Our proposed methodology for measuring sequence similarity is flexible to incorporate additional event-specific information (i.e., covariates) that potentially contributes to the ability to discriminate between sequences. Following Ferraz Costa et al. [33], who focus on detecting suspicious fraudulent behavior in online media channels, we consider inter-visitation times (IVTs) as covariates to add more context to each event. Note that this approach is in line with previous work on studying the temporal periodicity of behavioral patterns [12,34]. To represent the flow of sequential timing information for network training and inference, we encode the IVTs categorically in weeks, days, hours and seconds. Thus, when covariates are included in the model, the input features are represented by a vector of five components or by raw sequence records accordingly.

Recall that our proposed method for learning sequence similarities relies on processing samples (more specifically, triplets) from the com plete event history collected from a user. As we can conjecture when inspecting projections of the derived embedded similarity space in Fig. 8, we are also interested in examining how sensitive our method is to varying sequence lengths. Thus, in our experiments, we need to decompose the records collected for the Comscore users into sub sequences or “snippets” of their overall browsing histories.

To sample and form triplets for training and model validation, we consider the following constraints. As there is no clear definition in the data that allows us to differentiate between sessions (streams of visits), we apply the obvious constraint to use a sub-sequence S with fixed length n by extracting a random sliding window. The randomness over the temporal axis allows us to cover the whole spectrum of browsing histories and thus increases the heterogeneity of the training data to facilitate generalization. Further, each sub-sequence S always starts with the first visit of the day. This constraint ensures that a truly “new” ses sion had started (which otherwise would be difficult to define) and captures some typical initial browsing session behavior.

For our dataset with 21,000 users, the upper bound of the total number of possible triplets can be estimated with $\textstyle \sum _ { j = 1 } ^ { m } ( { A ( j ) } _ { 2 } ) \approx 1 \times 1 0 ^ { 9 }$ which basically represents the sum of all permutations of the anchor and positive sequences. The sum goes over all users j with m = 21, 000 and A

![](/api/attachments/X4AU9AHM/fulltext/images/139ad1a724f40b71bc2807aa1853d4e9b206ae04fd107b76a0de500e3cb5736b.jpg)  
(a)

![](/api/attachments/X4AU9AHM/fulltext/images/1e95b253f99843234641b0a95ad555004e6930d09888703a9a9b1de6a87c2222.jpg)  
(b)  
Fig. 5. Histogram of the number of visited sites per user (left); log-scaled frequencies of total visits in 2014 (right).

![](/api/attachments/X4AU9AHM/fulltext/images/169df8ac116e62f1599a94f561bc1fb68e81876c1c20813736c1649bb5b17192.jpg)  
(a)

![](/api/attachments/X4AU9AHM/fulltext/images/851e9cc98faaf72c379d21c08011e81c460b498f3e7a870f6c041525477f69dc.jpg)  
(b)

Fig. 6. Ten most visited domains in terms of total shares of overall visits (left) and share of users who visited at least once in 2014 (right).  
![](/api/attachments/X4AU9AHM/fulltext/images/45a8478dd3a2123d39a9e43f1bf59dac82b7563f6f7ee5cb0d96ad72b89c7d29.jpg)  
(a)

![](/api/attachments/X4AU9AHM/fulltext/images/b8dce2423a92acab4b733f2fc83460dc7e83539f7918f3d6cf909db60d751727.jpg)  
(b)  
Fig. 7. Boxplots of percentages of visits by specific users to one of the top four most popular (left) and four least popular (right) domains in 2014. Mean values are plotted by rhombus symbols.

(j) represents the distribution of number of days that user j is active in 2014. A(j) has a mean value of 203 days. This is the upper bound because the formula assumes that all users produce sequences that start and end within a day.

The split into training and test data is based on the user axis. For this reason, 18,000 training dataset users and 3000 test dataset (holdout) users are randomly drawn. Then, the corresponding triplets or records are created within these disjoint sets.

## 3.2. Benchmark methods

To gain an understanding of the usefulness of our presented approach for quantifying sequence similarities in the context of user reidentification, we use two methods for comparison: The first approach is based on sequence alignment, which is a widely used method for mo lecular biological identification tasks [35] but also has been successfully applied to analyze activity-travel behavior [36] and for modeling behavioral patterns predating product purchases [12] or customer churn [37]. We use an algorithm proposed by Smith and Waterman [35] that can efficiently perform local sequence alignments. It has the ability to detect common sub-sequences in two samples with implied penalties for gaps. As a second method for comparison we use a modified term-frequency metric inspired by the term frequency inverse document frequency measure (aka, tf-idf) commonly used in document analysis [38]. The measure is defined as $\begin{array} { r } { t f - i d f = t f ( t , } \end{array}$ d)idf(t, D) where tf(t, d) represents the frequency of word t in document d. The inverse document frequency idf(t, D) is a measure of how much information a word carries determined by the inverse fraction of all documents D that contain word t scaled logarithmically:

![](/api/attachments/X4AU9AHM/fulltext/images/c05a920f2411b2a2e14a27e5335e28eb2dade8af41f147dea36ecc9d7d94e46b.jpg)  
(a)

![](/api/attachments/X4AU9AHM/fulltext/images/2c55b21d8b161f925bd044412e9225afc87db7c2a85f17fab83b20b99f0e1daa.jpg)  
(b)  
Fig. 8. Two-dimensional representations of the positions of randomly selected sequences from different users in the embedding Space; (a) sequence lengths = 20 and (b) sequence lengths = 200.

$$
\operatorname{idf} (t, D) = \log \frac {N}{| d \in D : t \in d |}.\tag{2}
$$

We extend this idea by taking each sequence as the equivalent of a document, each domain as the equivalent of a word, and the whole training set as D. To adopt the measure for our problem domain, we replace the idf-weight from the standard tf-idf metric with the domain’s rank to account for the Zipf-like distribution. The rankings are deter mined at the dataset level and decreasing rank reflects the domain’s global popularity (with rank 1 being google, rank 2 being facebook, etc.). This rank-based weighting scheme dominates alternative ap proaches such as logarithmic and proportional scales and is denoted as a term-frequency rank-weighted measure (TF-RW). The intuition behind the metric is that rareness of visits to a domain is positively associated with the amount of information provided about a user. Formally, the TF-RW measure is defined as

$$
\mathrm {TF\_RW} = \sum_ {i = 1} ^ {i _ {\max} = 1 0, 0 0 0} \min \left(i \cdot f _ {i} ^ {(S _ {a})}, i \cdot f _ {i} ^ {(S _ {b})}\right)\tag{3}
$$

for sequences $s _ { a }$ and $s _ { b } .$ The sum is over all 10,000 ranked domains i and the index also represents the rank. The domain frequencies in sequences $S _ { a }$ and $s _ { b }$ are known and defined as $f ^ { ( S _ { a } ) }$ and $f ^ { ( S _ { b } ) }$

Besides these two easy-to-implement methods, there are several other potential approaches to support user identification tasks. For example, locally sensitive hashing (LSH) techniques are widely used for comparing word n-grams between samples in a numerically extremely effective way by looking only at items that share a set of hash values. LSH is a popular method for efficiently performing nearest-neighbor search in high-dimensional data sets [39] and, among others, is suc cessfully used for scalable online collaborative filtering [40]. Another potential alternative approach is based on event frequencies that scale relative well with large data sets. One such method can be derived from techniques for finding frequent itemsets which are popular for deriving association rules in settings like market basket analysis (see, e.g. [41, 42]) and can be generalized for frequent sequence mining [43]. How ever, frequent sequence mining typically operates on the aggregate level, while we are interested in user-level inferences of sequence sim ilarity. Furthermore, while the primary task of our proposed TL-RNN framework is to establish a data-driven approach for deriving a mea surement instrument for similarities in sequential data, methods like LSH and frequent sequence mining are based on some predefined sim ilarity metric (such as Jaccard distances or cosine similarities for co-occurences) and are thus not directly comparable in the present application task.

## 3.3. Dual choice user re-identification experiment

Once the sequences of clickstream data are presented to the model, they are translated via the model’s inference channel (dashed arrows in Fig. 4) into cell-state vectors inside the 512-dimension embedding space. In this embedding space, we can easily compare sequences. To facilitate providing an intuition of such representations, Fig. 8 gives an example of a fully trained embedded similarity space. It depicts two examples of 1000 sequences: a sequence length of 20 in Fig. 8a and a sequence length of 200 in Fig. 8b. The sequences were randomly drawn from 10 holdout users in our test dataset. To facilitate projection of the output vectors onto a two-dimensional plane, we use a smaller 32-cell LSTM network. For the projection itself, we apply the Barnes-Hut t-distributed stochastic neighbor embedding (t-SNE) algorithm to reduce dimensionality [44].

A simple visual inspection shows that the model was able to discriminate the sequences by user accurately (marked by different shapes and colors). This is particularly true for the larger sequences (sequence length of 200 plotted in Fig. 8b). The users are separated flawless for all but one sequence of user 4 (plotted as +), which seems to be more similar to the behavior of user 7. For the shorter sequences presented in Fig. 8a, we find a few are positioned close to the groups of sequences from other users because of their very similar behavior or indistinguishability. Though the separation is not perfect, significant clustering of user groups is observed. Some clusters of sequences show a wider spread, at times nearly merging with other user groups. As we next explore in greater detail, these observations stem from the fact that sequence length naturally limits the degree of observable variability and affects the amount of information available from which to make in ferences about the underlying similarity structure.

Our first evaluation experiment mimics a user re-identification task. To this end, the fully trained network model is repeatedly presented with three sample sequences from two users from the holdout dataset $( \mathrm { i . e . }$ , unseen users) as inputs. This process is similar to a series of normal triplet comparison tasks (anchor, positive, negative). Then, the model is challenged to select the corresponding sequence (positive) that belongs to the same user as the anchor sequence, by choosing between the positive and the negative sample. This is done by determining their distances from the anchor sequence, $\mathcal { D } _ { 1 } = \parallel \mathbf { c } _ { 0 } - \mathbf { c } _ { + }$ ‖ and $\mathcal { D } _ { 2 } = \Vert \mathbf { c } _ { 0 } -$ $\mathbf { c } _ { - } \parallel$ . The labels of $\mathbf { c } _ { + }$ (positive) and c (negative) are unknown. If $\mathcal { D } _ { 1 } < \mathcal { D } _ { 2 } ,$ the model’s inference is correct and counted as a success whereas $\mathcal { D } _ { 1 } \geq \mathcal { D } _ { 2 }$ is a failed decision. This task is repeated for hundred of thousands independent random draws from the holdout dataset of 3000 users. The total success rate is reported in Table 1. Four sequence lengths are considered: 10, 20, 100, and 200 site visits per sequence. We train our TL-RNN model twice, once with and once without consideration of IVTs as covariates. Note that the benchmark methods are not capable of incorporating any further covariates.

We find that the model significantly improves the re-identification rates of alternative models, especially with short sequences. With very long sequences, the TF-RW competes surprisingly well. For such long sequences, the pure frequency of domain visits seems to be much more informative than the sequential order of the timing pattern. Still, for such tasks that rely heavily on counting occurrences, our TL-RNN per forms similarly well. This is no surprising observation since LSTM-based models are capable of “learning” unbounded counting. Interestingly, adding IVT covariates to our proposed model does not contribute much to its performance (see the last column in Table 1). In terms of compu tation time, inferring sequence similarities using our implementation of the model as described in Section 2.4 is ten times faster than when using the Smith-Waterman algorithm and even faster than when using the TF-RW benchmark, once the network is trained.

## 3.4. Evaluation of user allocation for multi-user accounts

In many cases, it is essential to identify specific users in a stream of mixed sequences from multiple users. This is the case for loyalty pro grams in which multiple household members share the same loyalty card and when several persons share a video or audio streaming account. To test the usefulness of our TL-RNN model for such a task, we construct an artificial dataset consisting of several sequences from different Comscore users. The sequences were drawn and concatenated into re cords using available user labels. Fig. 9 depicts this process for three different users. The sequences are always drawn in a random order from random users and each sequence is a random window of one sequence length drawn from the user’s history. Each record consists of 50 se quences with 20 (short) or 200 (long) visits each.

Model comparisons in respect to the share of correctly assigned triplets (P), computation time for one triplet decision $( t _ { p r e d } )$ and the training time to reach early stopping $( t _ { t r a i n } ) .$ Best results highlighted in bold.

<table><tr><td colspan="2">Seq. length</td><td>Smith-Waterman</td><td>TF-RW</td><td>TL-RNN</td><td>TL-RNN w/ IVT</td></tr><tr><td></td><td>P</td><td>68.26%</td><td>78.88%</td><td>89.31%</td><td>91.23%</td></tr><tr><td rowspan="3">10</td><td> $t_{pred}$ </td><td>1.1 ms</td><td>11.6 ms</td><td>0.14 ms</td><td>0.15 ms</td></tr><tr><td> $t_{train}$ </td><td>0</td><td>0</td><td>315 min</td><td>286 min</td></tr><tr><td>P</td><td>75.48%</td><td>87.43%</td><td>93.37%</td><td>94.71%</td></tr><tr><td rowspan="3">20</td><td> $t_{pred}$ </td><td>4.3 ms</td><td>11.6 ms</td><td>0.19 ms</td><td>0.23 ms</td></tr><tr><td> $t_{train}$ </td><td>0</td><td>0</td><td>542 min</td><td>589 min</td></tr><tr><td>P</td><td>84.57%</td><td>96.70%</td><td>98.00%</td><td>98.51%</td></tr><tr><td rowspan="3">100</td><td> $t_{pred}$ </td><td>110.3 ms</td><td>12.3 ms</td><td>0.47 ms</td><td>0.75 ms</td></tr><tr><td> $t_{train}$ </td><td>0</td><td>0</td><td>349 min</td><td>713 min</td></tr><tr><td>P</td><td>86.91%</td><td>98.18%</td><td>98.88%</td><td>98.98%</td></tr><tr><td rowspan="2">200</td><td> $t_{pred}$ </td><td>398.7 ms</td><td>12.3 ms</td><td>0.81 ms</td><td>1.00 ms</td></tr><tr><td> $t_{train}$ </td><td>0</td><td>0</td><td>349 min</td><td>409 min</td></tr></table>

Using this procedure, we create a dataset of synthetic mixed user histories with known labels so we assume that we observe records from different users over time. The task is to assign a sequence to the correct user. Again, only sequences from holdout users (not used for training) are considered for this task. We study all cases of two to five “synthetic” users in a record with the share of sequences per user in a record being equally distributed. To make inferences about sequence similarities, we re-use the optimized and trained models from the previous reidentification experiment so no re-training is required.

This evaluation is based on the following assumptions.

• We know when a sequence in a record starts and ends.

• We know k, the number of users, but do not know when and how many times a user is active in a given series of sequences.

We sample sequences of randomly selected users (1 to k) from the dataset and present them to the model. The TL-RNN transforms each sequence separately into a cell-state vector by feeding it through the inference channel of the fully trained model as highlighted in Fig. 4. Doing this for all 50 sequences of a multi-user record results in a vector space containing 50 vectors. The vectors are then clustered using the kmeans algorithm [45] in which labels from 1 to k are assigned to each discovered cluster. To evaluate recovery of the original partition, we use the (widely used) adjusted rand index (ARI) [46] as a measure of the quality of cluster agreement. The ARI compares two partitions and is insensitive to different labelling of the elements. Furthermore, the ARI controls for random label assignment in which a random draw translates into an ARI close to 0.0. The ARI is defined for a range of [− 1, 1]; a negative score indicates independent (poor) labels and a positive score indicates similar clusters. An ARI of 1.0 represents a perfect match.

Table 2 presents the resulting ARI scores and the percentage of perfectly clustered sequences in which all sequences are assigned to the correct user. These results clearly show that user allocation becomes more difficult with greater numbers of users. This is expected from a statistical standpoint since the number of combinations increases with

$\binom { n } { k }$ . Though the clustering ability of the model is almost flawless for long sequences, we have to accept imperfect allocations for the shorter sequences of 20 visits. Nevertheless, ARI scores of 0.89, 0.84 and 0.80 are highly accurate. This accuracy is also reflected in a visual inspection of a few examples as depicted in Fig. 10 (for illustrative purposes, we use a shorter record length of 20 sequences rather than 50). As can be seen, only one or two errors occur in a record.

## 3.5. Estimation of the number of users in a record

In many business cases, there is tremendous interest in determining the number of users in a behavioral sequence. Examples include profiling in multi-user accounts and detecting fraud by a user of a multiuser or shared account. To perform this evaluation, we use the same artificially created records as previously. When we use the proposed vector representation of sequences, estimating the number of users boils down to determining the “correct” number of clusters (evaluation of k). The relevant literature offers a wide variety of internal “validity" metrics and most common approaches are based on comparing within-cluster variances to between-cluster variances [46]. We use the well-known Silhouette coefficient [47]. The Silhouette method compares the mean distance of a point to (i) all other points in the same cluster and (ii) all other points in another cluster. Then, the difference between those two mean values is calculated and normalized by the maximal distance available. The coefficient represents a contrast measure in which greater contrast represents a more accurate classification. Because of the applied normalization, the Silhouette index takes values in the range of [− 1, 1].

![](/api/attachments/X4AU9AHM/fulltext/images/f7ea243b2af0630ee7666197a9df511d5bf875523a88cbd9f3e4743b26560526.jpg)  
Fig. 9. Example of a concatenated record used for the multi-user re-identification task.

The average ARI and PCS scores for various sequence lengths and numbers of distinct users.

<table><tr><td>Seq. length</td><td></td><td>k=2</td><td>k=3</td><td>k=4</td><td>k=5</td></tr><tr><td rowspan="2">200</td><td> $\overline{ARI}$ </td><td>0.991</td><td>0.986</td><td>0.979</td><td>0.970</td></tr><tr><td>perfect</td><td>97.2%</td><td>92.1%</td><td>85.2%</td><td>77.1%</td></tr><tr><td rowspan="2">20</td><td> $\overline{ARI}$ </td><td>0.898</td><td>0.864</td><td>0.820</td><td>0.778</td></tr><tr><td>perfect</td><td>60.6%</td><td>35.6%</td><td>18.74%</td><td>9.0%</td></tr></table>

The partition having the “optimal” number of clusters is the one with the highest Silhouette coefficient.

We evaluate the precision and recall of this classification task. The precision is defined as $\textstyle \mathbf { : } p = { \frac { \mathrm { T P } } { \mathrm { T P } + \mathrm { F P } } }$ where TP is the number of true positives (i.e., correctly classified sequences) and FP is the number of false posi tives. Recall is defined as $\begin{array} { r } { r = \frac { \mathrm { T P } } { \mathrm { T P } + \mathrm { F N } } , } \end{array}$ , which measures the percentage of all samples of a specific class $( \mathbf { e } . \mathbf { g } . , k = 2 )$ that were correctly classified as belonging to that class. Precision, on the other hand, measures the percent of samples assigned to a class (e.g., k = 3) that truly belong there.

The results of this evaluation are presented in Table 3 for the arti ficially created records consisting of 50 sequences sampled from 2 to 5 randomly selected users. A priori, a model without knowledge returns recall and precision of 25%. As shown in Table 3, the results significantly exceed those expectations. Hence, we find that our approach is a good guide for estimating the number of active users in a mixed stream.

## 4. Discussion and further application domains

We proposed a novel deep recurrent neural network model with a triplet loss cost function for “learning” and generalizing similarity structures in sequential data. The specific model architecture of the TL-RNN approach allows us to fully benefit from its automatic feature en gineering capability for extracting those individual sequence-level characteristics that define a similarity space for a given domain of sequential data streams. This property turns our approach into a unique data-driven instrument for measuring distances between sequence which differs substantially from more established measure sequence similarities. We demonstrate the capability of the derived similarity metric in the context of clickstream behavior collected from a hetero geneous sample of internet users. Our empirical performance demon stration shows that the proposed model clearly outperforms more conventional methods in a user re-identification task. This improvement in predictive accuracy is achieved by an embedding of “new” sequences into a high-dimension vector representation. In contrast to simpler similarity measures, our behavioral sequence embeddings allow not only for distance comparisons, but also for straightforward clustering of the resulting representations. We demonstrate this property in the context of detecting multiple users in settings involving extended sequential data.

Besides predictive accuracy, the proposed sequence similarity metric is extremely flexible and can easily extended to account for eventspecific covariates without making any prior distributional assump tions. In our empirical illustration we demonstrate this by considering inter-event timings. This gain in flexibility certainly requires extensive model training time. Once the network is trained, however, the model is able to generalize on new data and the computational cost of similarity “mapping” is marginal and scales linearly with the number of sequences, which is crucial for real-time calculations in online settings.

As Table 4 summarizes, the gains in predictive power and flexibility come at the cost of significantly higher model complexity. Despite the model’s performance was validated in a holdout data set, the general izability of such excessively high-parameter models is difficult to eval uate. As with any data-driven methodology, the scope of validity established by the “learned” similarity metric is limited to the specific application domain. While transferring an existing similarity embedding to different domains is difficult, it can be fine-tuned in real-world set tings once new data accrue. In addition, the software stack and hardware requirements are clearly higher compared to the more simpler alternatives. This results in higher computational costs for training and running the model, and it comes along with higher labour costs for maintenance and higher skill levels.

Recall and precision of estimating the number of classes using the silhouette index.

<table><tr><td>Seq. length</td><td></td><td>k=2</td><td>k=3</td><td>k=4</td><td>k=5</td></tr><tr><td rowspan="2">200</td><td>Recall</td><td>87.9%</td><td>59.5%</td><td>48.6%</td><td>52.4%</td></tr><tr><td>Precision</td><td>83.4%</td><td>65.2%</td><td>46.0%</td><td>53.6%</td></tr><tr><td rowspan="2">20</td><td>Recall</td><td>78.1%</td><td>43.4%</td><td>34.3%</td><td>51.8%</td></tr><tr><td>Precision</td><td>64.0%</td><td>52.6%</td><td>39.4%</td><td>47.8%</td></tr></table>

![](/api/attachments/X4AU9AHM/fulltext/images/17096f3b894989fcc76a835132ee89bb3f5b11b5380ec13fb8f33441f92ed81d.jpg)  
Fig. 10. Examples for real user allocations by the model, when compared to the real labels.

Table 4  
Comparison of features and properties of examined models.

<table><tr><td></td><td>Smith-Waterman</td><td>TF-RW</td><td>TL-RNN</td><td>TL-RNN w/IVT</td></tr><tr><td>Number of parameters</td><td>3</td><td>10,000 $( \alpha i_{max})$ </td><td>1,450,322</td><td>1,629,170</td></tr><tr><td>Flexibility</td><td>Medium</td><td>Low</td><td>High</td><td>High</td></tr><tr><td>Requirements</td><td>Medium</td><td>Medium</td><td>High</td><td>High</td></tr><tr><td>Embedding Space</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr></table>

In contrast to existing approaches, that rely on hand-engineered similarity metrics, the proposed architecture allows (i) to derive a purely data-driven sequence similarity metric based on subject-level characteristics, (ii) enabling analysts to explore similar events repre sented in an embedding layer, (iii) automatically associating cooccurring events within a sequence (network embedding layer), and (iv) to effectively incorporate any number of covariates for such simi larity. Consider retail bank data, for example, where each customer transaction has a variety of attributes associated with it, such as trans action type, transaction amount, beneficiary bank, and event time stamps. Our method allows incorporating all of these attributes for each transaction to define a meaningful similarity between sequences of transactions, where the neural network learns based on the existing data whether the downpayment of a loan is more characteristic for an indi vidual than a receipt for “Pizza” on a “Saturday evening”. Furthermore, the method does not only rely on pure counting statistics but can extract temporal patterns to yield similarity. On the other hand, the model is also able to connect co-occurring events like “Shell” and “BP” as very similar actions. which would be treated differently in alternative models.

The generic nature of the proposed framework allows for many ap plications in multiple research domains, including user re-identification and anomaly or fraud detection. Furthermore, the framework can be used to measure similarities in playlists or usage patterns in the growing field of online services for audio and video streaming (see, e.g., [3,4]). Applications for the presented approach are not limited to processing behavioral data. Since texts are sequential data as well, our method can be used to re-identify authors, detect plagiarism, and to identify fraud in text. In these and related contexts, methods like LSH could serve as excellent candidate tools to perform fast and scalable nearest neighbour searches in a high-dimensional embedding space (established by TL-RNN) for large numbers of objects.

Our method’s demonstrated high precision of user re-identification suggests that the derived vector representations of sequences can un cover meaning beyond distance comparisons. For example, vector rep resentations could serve as a basis for performing behavioral-based customer segmentation and/or mapping user sequences to an already existing segmentation. Our empirical application study and the discus sion around Fig. 8 points towards promising directions on the benefits and usefulness of representing sequence similarities in an embedding space.

Previous demonstrations of vector analyses for word-embedding models (see, e.g., Gittens et al. [48]) suggest that controlled in terpolations and performing vector arithmetics in embedding similarity spaces can provide novel insights into the composition of hypothetical sequences. Potential applications include studying morphing of one sequence into another (hypothetical) one conditional on changes in a specific sub-pattern of interest to the researcher. Against this back ground, we also note that our methodology can be extremely beneficial in studies of the accuracy and realism of synthetic data generated by anonymization techniques for sequential data. However, there is also room for further improving the method’s flexibility. A potential extension is to modify the training process such that network learning is conditioned on an event (such as churn or purchase), which would turn the framework into a predictive tool. We view our research as a good first step toward these and similar extensions and applications.

## Acknowledgement

The authors gratefully acknowledge financial support from the "ICT of the Future” funding program of the Austrian Federal Ministry for Transport, Innovation and Technology (BMVIT).

## References

[1] R.E. Bucklin, C. Sismeiro, Click here for internet insight: advances in clickstream data analysis in marketing, J. Int. Market. 23 (2009) 35–48.

[2] N. Schroder, ¨ A. Falke, H. Hruschka, T. Reutterer, Analyzing the browsing basket: a latent interests-based segmentation tool, J. Int. Market. 47 (2019) 181–197.

[3] B. Zhang, G. Kreitz, M. Isaksson, J. Ubillos, G. Urdaneta, J.A. Pouwelse, D. Epema, Understanding user behavior in spotify, in: Proceedings IEEE INFOCOM, 2013 pp. 220–224.

[4] A. Zhang, N. Fawaz, S. Ioannidis, A. Montanari, Guess who rated this movie: identifying users through subspace clustering, in: Proceedings of the Twenty Eighth Conference on Uncertainty in Artificial Intelligence, UAI’12, AUAI Press Arlington, Virginia, USA, 2012, pp. 944–953.

[5] B. Noori, An analysis of mobile banking user behavior using customer segmentation, Int. J. Global Busin. 8 (2015) 55–64.

[6] C. Comito, D. Falcone, D. Talia, Mining human mobility patterns from social geotagged data, Pervasive Mob. Comput. 33 (2016) 91–107.

[7] S.K. Hui, P.S. Fader, E.T. Bradlow, Path data in marketing: an integrative framework and prospectus for model building, Market, Sci, 28 (2009) 320–335.

[8] J.S. Larson, E.T. Bradlow, P.S. Fader, An exploratory look at supermarket shopping paths. Int. J. Res, Market. 22 (2005) 395–414.

[9] B. Bargeman, C. Joh, H. Timmermans, Vacation behavior using a sequence alignment method, Annal, Tour. Res, 29 (2002) 320–337

[10] S. Nestorov, B. Jukic, N. Jukic, A. Sharma, S. Rossi, Generating insights through data preparation, visualization, and analysis: framework for combining clustering and data visualization techniques for low-cardinality sequential data, Decision Supp. Sys. 125 (2019) 113119.

[11] A. Prinzie, D. Van den Poel, Investigating purchasing-sequence patterns for financial services using markov, mtd and mtdg models, Eur. J. Operat. Res. 170 (2006) 710–734.

[12] A. Prinzie, D. Van den Poel, Predicting home-appliance acquisition sequences: markov/markoy for discrimination and survival analysis for modeling sequential information in nptb models. Decision Supp. Sys. 44 (2007) 28–45

[13] J. Fredrickson, M. Mannino, O. Alqahtani, F. Banaei-Kashani, Using similarity measures for medical event sequences to predict mortality in trauma patients, Decision Supp. Sys. 116 (2019) 35–47.

[14] J.-Y. Jiang, C.-T. Li, Y. Chen, W. Wang, Identifving users behind shared accounts in online streaming services, in: The 41st International ACM SIGIR Conference on Research & Development in Information Retrieval, SIGIR ’18, ACM New York, NY, USA, 2018, pp. 65–74

[15] B. Charyyev, M.H. Gunes, Voice command fingerprinting with locality sensitive hashes, in: Proceedings of the 2020 Joint Workshop on CPS&IoT Security and Privacy, CPSIOTSEC'20, Association for Computing Machinery New York, NY USA, 2020, pp. 87–92.

[16] F. Schroff, D. Kalenichenko, J. Philbin, Facenet:, A unified embedding for face recognition and clustering, in: 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2015, pp. 815–823.

[17] M. Sundermeyer, H. Ney, R. Schlüter, From feedforward to recurrent lstm neural networks for language modeling, IEEE/ACM Trans. Audio Speech Lang. Proc. 23 (2015) 517–529.

[18] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neur. Comput. 9 (1997)

[19] F.A. Gers, J. Schmidhuber, F. Cummins, Learning to forget: continual prediction with lstm, Neur. Comput. 12 (1999) 2451–2471.

[20] Y. Bengio, P. Simard, P. Frasconi, Learning long-term dependencies with gradient descent is difficult. JEEE Trans, Neur. Net. 5 (1994) 157–166.

[21] J. Bromley, I. Guyon, Y. LeCun, E. S¨ackinger, R. Shah, Signature verification using a “siamese” time delay neural network, in: J. Cowan, G. Tesauro, J. Alspector (Eds.), Advances in Neural Information Processing Systems, 6, Morgan-Kaufmann, Burlington. Massachusetts. USA. 1994, pp. 737–744

[22] K.O. Weinberger. L.K. Saul. Distance metric learning for large marginnearest neighbor classification, J. Mach, Learn, 10 (2010) 204–244.

[23] G. Chechik, V. Sharma, U. Shalit, S. Bengio, Large scale online learning of image similarity through ranking, J. Mach. Learn. 11 (2010) 1109–1135.

[24] W. Chen, X. Chen, J. Zhang, K. Huang, Beyond triplet loss: a deep quadruplet network for person re-identification, in: IEEE Conference on Computer Vision and Pattern Recognition (CVPR). 2017, pp. 1320–1329

[25] W. Liao, M.Y. Yang, N. Zhan. B. Rosenhahn. Triplet-based deep similarity learning for person re-identification, in: IEEE International Conference on Computer Vision Workshops (ICCVW). 2017, pp. 385–393.

[26] T. Mikolov, I. Sutskever, K. Chen, G.S. Corrado, J. Dean, Distributed representations of words and phrases and their compositionality, in: C.J.C. Burges, L. Bottou, M. Welling, Z. Ghahramani, K.Q. Weinberger (Eds.), Advances in Neural Information Processing Systems 26, Curran Associates, Inc., Red Hook, NY, USA,

[27] A. Abbott, Sequence analysis: new methods for old ideas, Ann. Rev. Sociol. 21 (1995) 93–113.

[28] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning Representations by back propagating errors, Nature 323 (1986) 533–536.

[29] S. Geman. E. Bienenstock. R. Doursat. Neural networks and the bias/variance dilemma, Neur. Comput. 4 (1992) 1–58.

[30] C.C. Aggarwal, A. Hinneburg, D.A. Keim, On the surprising behavior of distance metrics in high dimensional spaces, in: Proceedings of the 8th International Conference on Database Theory, ICDT ’01, Springer-Verlag, Berlin, Heidelberg, 2001, pp. 420–434.

[31] D.P. Kingma, J. Ba, Adam: a method for stochastic optimization, 2014., in: 3rd International Conference for Learning Representations, San Diego, 2015. https:/ arxiv.org/abs/1412.6980

[32] D.M.W. Powers, Applications and explanations of zipf’s law, in: Proceedings of the Joint Conferences on New Methods in Language Processing and Computational Natural Language Learning, Association for Computational Linguistics, USA, 1998, pp. 151–160.

[33] A. Ferraz Costa, Y. Yamaguchi, A. Juci Machado Traina, C. Traina, C. Faloutsos, Rsc: mining and modeling temporal activity in social media, in: Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD ’15, ACM, New York NY, USA, 2015, pp. 269–278.

[34] Y.C. Yang, B. Padmanabhan, H. Liu, X. Wang, Discovery of periodic patterns in sequence data: a variance-based approach, INFORMS J. Comput. 24 (2011) 343–515.

[35] T.F. Smith, M.S. Waterman, Identification of common molecular subsequences,

[36] B. Bargeman, C. Joh, H. Timmermans, Vacation behavior using a sequence alignment method, Annal. Tour. Res. 29 (2002) 320–337.

[37] A. Prinzie, D. Van den Poel, Incorporating sequential information into traditiona classification models by using an element/position-sensitive sam, Decision Supp. Sys. 42 (2006) 508–526.

[38] A. Aizawa, An information-theoretic perspective of tf-idf measures, Inf. Process. Manage. 39 (2003) 45–65.

[39] J. Leskovec, A. Rajaraman, J.D. Ullman, in: Mining of Massive Datasets, 2nd ed., Cambridge University Press, USA, 2014.

[40] A.S. Das, M. Datar, A. Garg, S. Rajaram, Google news personalization: scalable online collaborative filtering. in: Proceedings of the 16th International Conference on World Wide Web. WWW '07. Association for Computing Machinery. New York NY. USA, 2007, pp. 271–280.

[41] T. Brijs, G. Swinnen, K. Vanhoof, G. Wets, Building an association rules framework to improve product assortment decisions, Data Min. Knowl. Disc. 8 (2004) 7–23.

[42] T. Reutterer, K. Hornik, N. March, K. Gruber, A data mining framework for targeted category promotions, J. Busin. Econ. 87 (2017) 337–358.

[43] M.J. Zaki, Spade: an efficient algorithm for mining frequent sequences, Mach. Learn, 42 (2001) 31–60.

[44] L. van der Maaten, G. Hinton, Visualizing data using t-SNE, J. Mach. Learn. Res. 9 (2008) 2579–2605.

[45] J. MacQueen, Some methods for classification and analysis of multivariate observations, in: In 5-th Berkeley Symposium on Mathematical Statistics and Probability, 1967, pp. 281–297.

[46] L. Hubert, P. Arabie, Comparing partitions, J. Int. Market. 2 (1985) 193–218.

[47] P. Rousseeuw, Silhouettes: a graphical aid to the interpretation and validation of cluster analysis, J. Comput. Appl. Math. 20 (1987) 53–65.

[48] A. Gittens, D. Achlioptas, M.W. Mahoney, Skip-gram − zipf + uniform = vector additivity, in: Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Association for Computational Linguistics, Vancouver, Canada, 2017, pp. 69–76.

![](/api/attachments/X4AU9AHM/fulltext/images/e80ce88dfee25b7ca8c8639efbac7c408cb0d6612bb7a9f6b4e92358ff84ca50.jpg)

Stefan Vamosi is a research and teaching associate and doctoral student at the Vienna University of Economics and Business (WU Vienna). He holds a master’s degree in Physics, with specialization in Computational Physics. During his mas ter’s thesis he was based at CERN, where he developed a simulation software for an anti-hydrogen beam experiment. Prior to joining WU’s doctoral program in May 2018, he gained professional experience in a consulting firm. His research in terests are time-series analysis, behavioral customer segmen tation, and data prediction with deep learning approaches.

![](/api/attachments/X4AU9AHM/fulltext/images/183c8ab7a0881d5a64a0d8a57a164bb0174b3c184accbfb7569fcd4492f7da4a.jpg)

Thomas Reutterer is Professor of Marketing and Customer Analytics at the Vienna University of Economics and Business (WU Vienna). His research focuses on analyzing, modeling and forecasting customer behavior in data-rich environments. In his research projects, he employs advanced statistical or machine learning methods to provide decision support for various business applications. His recent research is in the area of customer value and relationship management, customer base analysis, as well as content marketing supported by generative natural language models.

![](/api/attachments/X4AU9AHM/fulltext/images/545bd1156b57fc64e616227893a0b66740add1c5bef0265bde8426b42fcc7fd2.jpg)

Michael Platzer is Founder and Chief Strategy Officer at MOSTLY AI, a VC-backed DeepTech company, building enter prise solutions for Generative AI. Prior to that, he joined Microsoft as Senior Data Scientist, contributing to their global Consumer Analytics initiatives. He earned a Master’s degrees in Mathematics from the Technical University of Vienna, and received a Ph.D. degree in marketing science from WU Vienna. For his contributions to the field of marketing research, he was recognized with the Robert Lavidge global research award by the American Marketing Association.
