---
otero_id: 19811
otero_key: "GGCJKWXH"
title: "S2SAN: A sentence-to-sentence attention network for sentiment analysis of online reviews"
authors: "Ping Wang; Jiangnan Li; Jingrui Hou"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113603"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# S2SAN: A sentence-to-sentence attention network for sentiment analysis of online reviews

Ping Wang <sup>a,b,\*</sup>, Jiangnan Li <sup>b</sup>, Jingrui Hou <sup>b</sup>

<sup>a</sup> Center for the Studies of Information Resources, Wuhan University, Wuhan, Hubei 430072, China

<sup>b</sup> School of Information Management, Wuhan University, Wuhan, Hubei 430072, China

## A R T I C L E I N F O

Keywords: Sentiment analysis Attention mechanism Hierarchical structure Sentence-to-sentence attention

## A B S T R A C T

Many existing attention-based deep learning approaches to sentiment analysis have focused on words and represent an entire review text as a word sequence. However, these approaches overlook the differences in the importance of each sentence to the complete text. To solve this problem, some work has been performed to calculate sentence-level attention, but these studies use the same approach that is applied to word-level atten tion, which leads to unnecessary sequential structures and increased complexity of sentence representation. Therefore, in this paper, we propose a sentence-to-sentence attention network<sup>1</sup> (S2SAN) using multihead selfattention. We conducted several domain-specific, cross-domain and multidomain sentiment analysis experi ments with real-world datasets. The experimental results show that S2SAN outperforms other state-of-the-art models. Some classical sentiment classifiers [e.g., convolutional neural network (CNN), recurrent neural network (RNN), and long short-term memory (LSTM) models] achieve better accuracies when they are recon figured to include sentence-to-sentence attention.

## 1. Introduction

The rise of the e-commerce industry has caused substantial changes in business models between merchants and consumers, which has enabled exponential proliferation in the number of online reviews [1–3]. Websites such as Amazon and Jingdong provide customers with a platform for sharing their perspectives and opinions on various products and services [4]. Rich sentiment information exists in online reviews that directly reflect the positive, negative or neutral sentiment polarity of users [5,6]. Note that reviews of products and services in online platforms offer value from a variety of perspectives. The ‘Electronic Word of Mouth’, which is a collection of reviews, is a key driver in decision-making [7,8]. On the other hand, reviews offer clues to users latent demands and motivations, which render them conducive for improving online merchants' products and service quality [9,10]. Moreover, the potential user interests and preferences revealed in re views provide reference information for making personalized recom mendations [11]. However, the vast number of online reviews hinder the ability of both users and merchants to comprehensively extract and analyze public opinions [12]. To fully utilize the immense value of on line reviews, there is a pressing need for a sentiment analysis model that can convert the overloaded sentiment information contained in reviews into a more easily understandable form.

Sentiment analysis, which is also known as opinion mining [13], is dedicated to classifying the sentiment polarity in individual review texts in our work. Previous approaches to sentiment analysis include labeling corpora that are intended for sentiment classification tasks [14,15], building sentiment lexicons [16,17], and training domain-specific sentiment classifiers [15,18,19], all of which have laid a solid founda tion for sentiment analysis research. With the increasing computational ability of computers and the continual development of deep learning technology, methods that combine language models and neural net works have become mainstream approaches for solving sentiment analysis problems. These approaches are superior to traditional machine learning classifier models in terms of text representation and deep se mantic understanding [12,20,21] and have greatly improved the senti ment analysis performance.

In recent vears. attention-based neural network models have achieved remarkable results in many natural language processing (NLP) tasks. Additionally, a large number of studies have applied attention mechanisms to sentiment analysis. The attention mechanism in deep learning is a simulation of the visual attention of human beings [22].

Human beings always ignore information irrelevant to the target task and allocate more attention resources to important information. The attention mechanism helps improve the robustness of deep learning models by extracting useful information from a large number of input and allocating more attention weights to this useful information. In this regard, attention mechanisms have made satisfactory progress. Gener ally, attention mechanism can tell how important every entity is in an entity sequence. An illustration of the case where the entities are words is presented in Section 3.2.1.

However, to the best of our knowledge, existing attention-based neural network models focus on words [23–25] by representing the entire text as a word sequence. The attention weights of different words are calculated based on their similarity in a word attention layer. However, in our research, we suggest that each sentence in a text ex presses a unique semantic meaning; thus, the attention weights of different sentences should be calculated individually. Although some works (such as the hierarchical attention network (HAN) proposed by Yang et al. [26]) consider sentence-level attention, most studies calcu late sentence-level attention in the same way as word-level attention. However, we suggest that the approaches that directly transplant word encoding methods into sentence-encoding have a defect: no apparent sequence-structure relationship exists between the sentences in a re view, as a result, representing sentences in a review using a sequence model adds unnecessary complexity. To fill this gap, we introduce a novel sentence-to-sentence structure where self-attention is used to calculate relation weights of every two sentences. Compared with the original attention mechanism, self-attention can provide a matrix where the relations of any two entities are represented. An illustration of the case where the entities are sentences is presented in Section 3.2.2.

Our research objectives are three-fold. The first objective is to design the sentence-to-sentence attention network (S2SAN). In S2SAN, the most suitable word encoder and sentence encoder for online review texts should be figured out. The second objective is to certify whether the S2SAN is superior to the sequence of sentences network (HAN) in terms of the classification accuracy and model training time in domainspecific, cross-domain, multidomain sentiment analysis tasks. We sug gest that the proposed sentence-to-sentence attention model has excel lent compatibility with different word encoders. Therefore, our third objective is to verify whether some extensively applied word encoders can achieve better accuracies with the reconfiguration of sentence-to sentence attention.

Overall, our contributions are summarized as follows:

• To the best of our knowledge, this is the first method that uses sentence-to-sentence attention to realize the sentence-level attention mechanism. This approach disregards sentence positional informa tion and reduces the complexity involved in building sentence sequences.

• Aimed at online reviews, S2SAN achieves excellent results in domain-specific, cross-domain and multidomain sentiment analysis experiments. The proposed model increases accuracy by 0.8% to 2.1% and reduces the training time by an average of 25% compared to another hierarchical model (HAN).

• In several parallel experiments, we verify that after optimization with a hierarchical structure and the sentence-to-sentence attention framework, the accuracies of some classical sentiment classifiers (e. g., convolutional neural network (CNN), recurrent neural network (RNN), and long short-term memory (LSTM) models) increase by 1.9% to 8%.

The remainder of this paper is organized as follows: Section 2 out lines the most relevant related research regarding sentiment analysis of online reviews and attention mechanisms. The sentence-to-sentence attention model is presented in Section 3. Section 4 reports the experi mental results, which are derived from multiple review datasets. The experimental results are discussed in Section 5. Section 6 provides the conclusions, limitations, and suggested directions for future work.

## 2. Related works

Our study focuses on online reviews in e-commerce platforms and aims to detect the sentiment of review texts using a novel attention ar chitecture. In this section, we review sentiment analysis methods of online reviews and attention mechanisms that have been reported in works on related NLP tasks.

## 2.1. Sentiment analysis of online reviews

Due to the inherent diversity of online reviews, some works on domain-specific sentiment classification models have focused on various domains or topics [27,28]. Cui et al. [29] applied several machine learning algorithms in a sentiment analysis experiment that involves approximately 100,000 online product reviews on Froogle. Zhang and He [30] suggested an ensemble approach that includes additional fea tures to enrich data representation. Deng et al. [31] presented a method in which an unannotated corpus and a dictionary are utilized to adapt existing sentiment lexicons for domain-specific social media texts. Attention mechanisms have become novel approaches in research on domain-specific sentiment analysis. Zong et al. [32] proposed a novel adaptive attention network (AAN) to explicitly model the correlations among inputs. Wu et al. [33] proposed a novel approach that in corporates user attention and product attention to improve review representations.

However, some expressions may convey different sentiments in different domains, and training a unique classifier for each domain is time-consuming [34]. To solve the domain adaption problem, some work has been conducted on cross-domain sentiment classification models and multidomain sentiment classification models. The goal of cross-domain sentiment analysis is to predict the sentiment label of a target domain using features and models that are initially trained on a source domain. Deshmukh and Tripathy [35] proposed a semisupervised approach that combines modified maximum entropy and bipartite graph clustering to address domain adaption. Blitzer et al. [36] introduced the structural correspondence learning (SCL) algorithm to cross-domain sentiment classification and identified a measure of domain similarity. However, the SCL model addresses each feature and instance using an equivalent weight strategy. To solve this problem, Tan and Cheng [37] proposed a weighted SCL model (W-SCL) and applied it to cross-domain sentiment analysis. Multidomain sentiment analysis tasks generally extract texts from different domains (e.g., movie reviews and product reviews) to build a training set and predict sentiment labels without domain information. Based on a CNN, Li et al. [38] constructed a domain-conditional model and domain-generative model and applied them to capture specific features from a single domain and common features between domains, respectively. Gupta et al. [39] proposed a unified position-sensitive multitask RNN architecture for these appli cations and constructed a novel composite-state sequence model using an auxiliary RNN that achieved better performance in multidomain classification and reasoning.

In addition to the previously mentioned research on sentiment analysis based on supervised learning, there are still a large number of reviews on the Internet that have not been assigned sentiment labels; however, manual labeling of these reviews is too costly. Therefore, some works have applied unsupervised learning approaches to conduct sentiment analysis of online reviews and obtained satisfactory results [40,41]. Unsupervised learning methods do not require a large labeled corpus for training. Moreover, they have excellent adaptability and are not limited to a single topic. Therefore, unsupervised learning ap proaches have become increasingly popular in the sentiment analysis field in recent years.

## 2.2. Attention mechanism in NLP

Research on attention mechanisms began in the 1990s and was initially applied to image recognition tasks [42]. With the development of deep learning and improvements in the computational ability of computers, research on attention-based neural network models has gradually become an important branch of deep learning. In 2014, the Google Deep Mind team was the first team to employ an attention mechanism for image classification [22,43]. Since 2014, attention mechanisms have also been utilized for speech recognition [44–46], video processing [47,48], and other tasks.

Attention mechanisms are currently in common usage for NLP tasks. Bahdanau et al. [49] proposed an encoder-decoder framework that is based on an attention mechanism and applied it to machine translation tasks. Subsequently, a considerable amount of work has been performed to improve and innovate attention mechanisms for different NLP tasks. Rockt¨aschel et al. [50] introduced the word-by-word attention mecha nism to enhance a model's ability to reason about the relationship be tween pairs of words or phrases. Cui et al. [51] proposed the attentionover-attention mechanism for the cloze-style reading comprehension task. Gehring et al. [52] from Facebook's artificial intelligence labora tory employed multistep attention to capture the relationships between input sentences in an encoder and decoder. Yang et al. [26] proposed a HAN for document classification. This network has a hierarchical structure that reflects the document hierarchy and applies two levels of attention—word level and sentence level—to distinguish the importance of different content when building document representations. Vaswani et al. [53] employed a full-attention structure to replace word encoding and proposed a transformer model that is based on self-attention, which repeatedly uses a multihead self-attention mechanism in the encoder and decoder. Self-attention mechanisms, a variant of attention mecha nisms, usually focus only on themselves and extract relevant informa tion from within. Therefore, self-attention mechanisms have better performance when processing sparse data than sequence models such as BI-GRU-ATT.

Attention mechanisms are also extensively applied in sentiment analysis tasks, the most important of which combine a sequence model and an attention mechanism. Wang et al. [25] and Song et al. [23] combined an LSTM with an attention mechanism to assign different attention weights to each word in a review text. Chen et al. [54] sug gested a nonlinear combination approach that consists of multiple attention mechanisms and an RNN, which strengthened the model's expressive power and enabled it to address more complicated content. Self-attention and hierarchical attention mechanisms have also been applied to sentiment analysis tasks. Lin et al. [24] proposed a new model to extract an interpretable sentence embedding by introducing selfattention. Pergola et al. [55] proposed a topic-dependent attention model for sentiment classification and topic extraction, whose hierar chical architecture utilizes a global topic embedding that encodes topics shared among words and sentences, while the neural unit employs a new internal attention mechanism that leverages global topic embeddings to derive local topic representations for words and sentences.

Attention mechanisms have become mainstream methods for improving the efficiency of NLP, and their applications now cover all aspects of NLP. However, most studies on the application and improvement of attention mechanisms focus on calculating the attention weights for individual words; few studies address the calculation of attention weights for sentences. In this study, we consider that each sentence in the text expresses a single semantic meaning. However, because each sentence is also an important part of the review text, the attention weight of each sentence should also be calculated. To solve this problem, this paper implements a sentence-to-sentence attention mechanism to calculate sentence-level attention weights.

## 3. Proposed approach: S2SAN

In this section, we present the S2SAN. The goal is to calculate sentence-level attention weights in online reviews.

## 3.1. Sentence-to-sentence attention

Several studies on text classification have adopted the approach that an article is composed of sentences and that sentences are composed of words, which produces a hierarchical structure between documents, sentences and words $[ 2 6 , 5 5 , 5 6 ]$ . Moreover, different words and sen tences convey different sentiment information, and thus, should have different weights. Fig. 1(a) illustrates the model architecture in their work. The attention-based BI-GRU network (BI-GRU-ATT) is utilized as both the word encoder and the sentence encoder in this model. BI-GRU is a typical sequence model that specializes in processing sequence data (e. $g . ,$ , word sequences and time sequences). However, we suggest that the sequence relationship between sentences is not obvious in a document, especially in highly colloquial online reviews. BI-GRU-ATT is not a suitable choice for sentence vector encoding. Therefore, we use selfattention instead to build a hierarchical attention framework as shown in Fig.1 (b).

Consider a real-world review on Yelp as an example. As shown in Fig. 2, the review consists of 10 sentences. The head and tail sentences are conclusive, while the middle sentences present factual statements. Clearly, no strict sequence relation exists between the sentences in this review. Therefore, using BI-GRU to encode these sentences not only imposes an invalid sequence relation but also makes the entire model unnecessarily complicated. In addition, the semantics of different sen tences are usually individually related to each other in a review text. The sentence relations not only refer to sequential relations but also include parallel adversarial relations, causal relations, etc. Inspired by the BOW [57,58], we decided to instead represent the review text with sentenceto-sentence attention to solve the sequence problem by disregarding the positional information of the sentences in a review text. Instead, we focus on the relations between sentences in the document vector space.

Based on this description and discussion, we propose a novel hier archical attention framework that uses self-attention. As shown in Fig. 1 (b), the framework is still a hierarchical word-to-sentence and sentenceto-document structure; however, the input sentence vectors are calcu lated by self-attention instead of BI-GRU-ATT. and the final document representation is obtained after global average pooling. The framework is highly compatible with word embedding and word-encoding approaches.

## 3.2. Sentence-to-sentence networks

In this study, S2SAN is the sentiment classification model in our sentence-to-sentence attention framework, which consists of sentenceand document-representation architectures and a classification layer. Generally, we encode words with BI-GRU-ATT to obtain a sentence representation while encoding the sentences with multihead selfattention to obtain a document representation. The building process for S2SAN is described in the following section.

## 3.2.1. Sentence representation

Although several pretraining sentence representation models like BERT [59] have achieved many state-of-art results in many NLP tasks, they are always accused of length-sensitive problems. An experiment [60] showed that the accuracy decreases with the reduction of sentence length, and texts with length less than 50 yield the lowest accuracy when BERT is used as a text classification method. However, the average sentence length in review texts is far below 50. Therefore, a more robust model, GRU [61], is adopted. The sentence representation architecture is shown in Fig. 3. After input embedding, the words in a sentence are encoded by GRU cells and then input into the word attention layer for weight calculation. The output of the attention layer is the sentence representation.

![](/api/attachments/GGCJKWXH/fulltext/images/59e40b285a8ec3affa16d16621c616a9419efd9ac6062cae3be11931b19d878c.jpg)  
(a) Sentence attention in HAN  
(b) Sentence attention in S2SAN

Fig. 1. Sentence attention in HAN and S2SAN  
![](/api/attachments/GGCJKWXH/fulltext/images/bc018f3fde799add846fcb49f726999a4a141b139cc3ae2a1d6c4260e013c6b1.jpg)  
Fig. 2. A review example from Yelp.

![](/api/attachments/GGCJKWXH/fulltext/images/408de854c1a277ea1e5e368ded6e65c24ffc71bf2f1a47a18dc6389ca1383a07.jpg)  
Fig. 3. Sentence representation.

For the review text $r ,$ we denote the total number of sentences by M, the number of words in each sentence by N, and the dimension of each word vector. by d Thus, we can express r as the hierarchical structure in Eq. (1):

$$
\mathbf {r} = \left[ \begin{array}{c} s _ {1} \\ \dots \\ s _ {M} \end{array} \right] = \left[ \begin{array}{c} v _ {1} ^ {1}, v _ {2} ^ {1}, \ldots v _ {N} ^ {1} \\ \dots \\ v _ {1} ^ {M}, v _ {2} ^ {M}, \ldots v _ {N} ^ {M} \end{array} \right] \in R ^ {M \cdot N \cdot d}.\tag{1}
$$

After obtaining the semantic representation of the review $\mathbf { r } \in \boldsymbol { R } ^ { M \cdot N \cdot d }$ , we feed $\mathbf { v } _ { n } ^ { m } \in R ^ { d }$ to the neural network units in the forward and backward GRUs. We concatenate the outputs $\overrightarrow { \mathbf { h } } _ { n } ^ { m }$ and $\stackrel {  } { \mathtt { h } } _ { n } ^ { m }$ from the GRU units to obtain the word representation model h<sup>m</sup> from the BI-GRU layer. This process can be expressed as shown in Eqs. (2)–(4):

$$
\overrightarrow {\mathrm{h}} _ {n} ^ {m} = \overrightarrow {G R U} \left(\mathrm{v} _ {n} ^ {m}, \overrightarrow {\mathrm{h}} _ {n - 1} ^ {m}\right),\tag{2}
$$

$$
\stackrel {{\leftarrow m}} {{\mathrm{h}}} _ {n} = \stackrel {{\leftarrow}} {{G}} R U \bigg (\mathrm{v} _ {n} ^ {m}, \stackrel {{\leftarrow m}} {{\mathrm{h}}} _ {n + 1} \bigg),\tag{3}
$$

$$
\mathrm{h} _ {n} ^ {m} = \left[ \overrightarrow {\mathrm{h}} _ {n} ^ {m}, \overleftarrow {\mathrm{h}} _ {n} ^ {m} \right]\tag{4}
$$

Next, we add a word attention layer to calculate the word weights. In sentence m, the attention weight $\alpha _ { n } ^ { \dot { m } }$ of word n is calculated in Eqs. (5) and (6). After obtaining the attention weight of each word, we multiply the hidden output $\mathtt { h } _ { n } ^ { m }$ of each word by the attention weight $\alpha _ { n } ^ { m }$ and sum the products of all the words to obtain an attention weight vector for the whole sentence, as shown in Eq. (7). We use this vector $\mathbf { v } _ { S }$ as the final vector of the sentence representation.

$$
u _ {n} ^ {m} = \tanh \left(W _ {\mathrm{w}} \mathrm{h} _ {n} ^ {m} + b _ {\mathrm{w}}\right),\tag{5}
$$

$$
\alpha_ {n} ^ {m} = \operatorname{softmax} \left(u _ {w} \cdot u _ {n} ^ {m T}\right),\tag{6}
$$

$$
v _ {s} = \sum_ {i = 1} ^ {| S |} \alpha_ {n} ^ {m} \cdot h _ {n} ^ {m}.\tag{7}
$$

In the equations, v represents the sum of the attention for all the words in sentence S; α<sup>m</sup> denotes the weight of attention gained by word n in sentence m; |S| represents the length of the sentence sequence $S ; u _ { w }$ is the word-level context; and $W _ { s }$ and $b _ { s }$ are the weight matrix and the bias, respectively.

For the review $r ,$ after using BI-GRU to encode the word sequence and calculating the word-level sentiment attention, we obtain the output sequence $\mathbf { v } _ { S } ,$ which contains the weight information of word attention. Next, in the document-representation process, we use v as an input to calculate sentence-to-sentence attention.

## 3.2.2. Sentence encoder and document representation

When implementing document representation, we adopted the multihead self-attention architecture proposed by Vaswani et al. [54], which uses a full-attention mechanism to encode sentence vectors and calculate the attention weight between sentences. Compared with the RNN-based structure, it is more effective in solving long-range de pendencies. Each head in this structure is a subspace, and all the heads are concatenated to ensure that the document-representation vector learns semantic information from the different subspaces. In addition, compared with the original model, we removed the position embedding layer that is used to encode the position information of each vector in the sequence to make the model better fit the “sentence-to-sentence atten tion” approach. The architecture for multihead self-attention is shown in Fig. 4.

Our document representation is concatenated from multihead self attention, which is expressed as shown in Eq. (8).

$$
\operatorname{MulitiHead} (r) = \operatorname{MultiHead} \left(\mathrm{Q} _ {r}, \mathrm{K} _ {r}, \mathrm{V} _ {r}\right) = \operatorname{Concat} \left(\mathrm{h} _ {1} ^ {r}, \mathrm{h} _ {2} ^ {r}, \dots , \mathrm{h} _ {x} ^ {r}\right) \mathrm{W} ^ {O}\tag{8}
$$

The composition of each head is shown in Eq. (9):

$$
\mathrm{h} _ {i} ^ {r} = \text { Attention } \left(\mathrm{Q} _ {r} \mathrm{W} _ {i} ^ {Q}, \mathrm{K} _ {r} \mathrm{W} _ {i} ^ {K}, \mathrm{V} _ {r} \mathrm{W} _ {i} ^ {V}\right)\tag{9}
$$

In this equation, $\mathsf { W } _ { i } ^ { Q } , \mathsf { W } _ { i } ^ { K } ,$ , and $\boldsymbol { \mathrm { W } } _ { i } ^ { V }$ are weight matrices that are randomly initialized during training.

Scaled dot-product attention was employed to perform the attention calculation, as shown in Eq. (10).

$$
\text { Attention } (Q, \mathrm{K}, \mathrm{V}) = \operatorname{softmax} \left(\frac {\mathrm{Q} \cdot K ^ {\mathrm{T}}}{\sqrt {d _ {k}}}\right) V\tag{10}
$$

where ${ \sf Q } = { \sf K } = { \sf V } = \nu _ { s 1 } , \nu _ { s 2 } , . . . \nu _ { s n }$ is a copy of the sentence representation. As shown in Fig. 4, when calculating the attention of $s _ { 1 }$ and $\boldsymbol { s } _ { i } ,$ we multiply s and the weight matrix to obtain the three vectors $Q _ { 1 } , K _ { 1 }$ and $V _ { 1 }$ and the three vectors $Q _ { i } , K _ { i } ,$ and $V _ { i }$ that correspond to $s _ { i \cdot }$ We then multiply Q by the transpose of $K _ { 1 }$ and $K _ { i }$ to obtain two attention scores. These two scores are divided by $\sqrt { d _ { k } }$ and then input into a softmax layer to obtain the attention coefficient. We can acquire $\mathrm { Z _ { 1 } }$ , which is the attention value of $s _ { 1 } ,$ by simply multiplying $V _ { 1 }$ and the attention coef ficient. In this equation, $\sqrt { d _ { k } }$ is a constant that has a regulatory role to ensure that the inner product is not too large; $d _ { k }$ is usually set to 64.

![](/api/attachments/GGCJKWXH/fulltext/images/05a23aefa17536e3777943ba52b248c177e422a977f604be1a6fc83f90b9af07.jpg)  
Fig. 4. Sentence-to-sentence attention architecture.

After the multihead attention calculation, the output vector is MulitiHead(s) $\in \boldsymbol { R } ^ { N \cdot t }$ . Compared with the input vector $\bar { ( s ) } \in R ^ { N \cdot d }$ , the multilayer attention transforms the word vector dimension d into $t ,$ where t is the product of the number of heads and the size per head. Next, we apply a global average pooling operation to MultiHead(s) to obtain the final document representation:

$$
r = G A P (\text { MulitiHead } (r)) \in R ^ {t}\tag{11}
$$

After obtaining the document-representation vector, we can input it into a softmax classifier to predict the sentiment polarity of review r.

## 4. Experiments and evaluation

In this section, we conduct four groups of experiments to validate whether S2SAN can yield better accuracy in domain-specific, crossdomain, and multidomain sentiment analysis tasks and whether the sentence-to-sentence attention framework is compatible with main stream word encoders, including CNN, DNN, RNN, and LSTM.

## 4.1. Baselines

We selected several classical neural network models for sentiment analysis tasks as baselines in this experiment; these models achieved state-of-art performances at different times. In these baselines (except for the HAN model, which also adopts a hierarchical attention mecha nism), the other models use a flat structure from words to a document.

• HAN, which was proposed by Yang et al. [26], uses a BI-GRU and an attention layer for encoding and attention calculation at the word level and sentence level, respectively, to identify the important words and sentences.

• TextCNN, which was proposed by Kim [62], obtains the n-gram feature representation from sentences via a one-dimensional convolution operation. TextCNN has a strong ability to extract the superficial features of text and works particularly well when applied to intention classification from short texts, such as search and con versation tasks.

• BI-GRU, which was proposed by Cho et al. [63], is a sequence model that regards text as a sequence of words. The model combines the output of the current moment with both the state of the previous moment and the state of the next moment, which is conducive to extracting deep text features.

• BI-GRU-ATT, which was proposed by Zhou et al. [64], is a typical model that combines BI-GRU and an attention layer and has been extensively utilized in many text classification tasks.

• RCNN, which was proposed by Lai et al. [65], combines the sequence structure of an RNN with the max pooling layer of a CNN to fully utilize the advantages of both circular neuron models and convolu tional neural models.

• The transformer classifier, which was proposed by Vaswani et al. [54], has two major components: an encoder and a decoder. Only the encoder is applied for text classification. A self-attention mechanism is utilized to implement word2word attention.

## 4.2. Experimental setup

All the programs in this experiment were executed on a GPUequipped server that is provided by the Supercomputing Center of Wuhan University.<sup>2</sup> The GPU model is a Tesla v100-SXM2 with 16 GB (dual). Our experimental scripts were written and compiled in Python $3 . 6 ,$ and we employed TensorFlow and Keras as deep learning frameworks.

In the experiment, we utilized 5-fold cross-validation and divided the samples into a training set and test set with an 8:2 ratio. The embedding dimension of the input text of the proposed model and baselines is set to 400. We employed RMSProp [66] as an optimizer and adopted cate gorical cross-entropy as the loss function.

## 4.3. Metrics

For domain-specific and cross-domain experiments, metrics of ac curacy can be simply acquired by Eq. (12):

$$
a c c = \frac {N _ {p r e \_ t r u e}}{N}\tag{12}
$$

where $N _ { p r e \_ m e }$ is the number of samples, whose sentiment labels have been correctly predicted, and N is the total number of samples under prediction. As for multidomain sentiment analysis, there are three metrics of accuracy:

$$
a c c _ {s} = \frac {N _ {p r e \_ t r u e}}{N}\tag{13}
$$

$$
a c c _ {d} = \frac {N _ {p r e \_ t r u e} ^ {\prime}}{N}\tag{14}
$$

$$
a c c _ {o v e r a l l} = \frac {\left| \left\{\left(y _ {d} ^ {\prime} , y _ {s} ^ {\prime}\right) \mid y _ {d} = y _ {d} ^ {\prime} , y _ {s} = y _ {s} ^ {\prime} \right\} \right|}{N}\tag{15}
$$

Similarly, $N _ { p r e \_ m u e }$ and $N _ { p r e \ : t r u e } ^ { } /$ are the number of sentiment labels and the number of domain labels, respectively, that have been correctly predicted. $a c c _ { s }$ and acc denote the sentiment accuracy and the domain accuracy. acc is a composite metric that refers to the ratio of sam ples of the sentiment labels and domain labels that have been correctly predicted. $y _ { d } ^ { \prime }$ and $y _ { s } ^ { \prime }$ are the domain label and the sentiment label, respectively, that have been predicted, while y and $y _ { s }$ are the real domain label and the sentiment label, respectively, in the dataset.

## 4.4. Experimental results

## 4.4.1. Performance on domain-specific sentiment analysis

We conducted experiments in a domain-specific sentiment analysis using four datasets. The Amazon dataset and JD dataset contain elec tronic product reviews in English and Chinese, respectively. The Yelp dataset contains restaurant and food service reviews in English, and the Douban dataset contains film reviews in Chinese. The total number of data items in these four datasets is $^ { 1 2 0 , 0 0 0 }$ . Refer to Table 1 for details.

The classification accuracy achieved by each model is listed in Table 2. The best-performing model on each dataset is highlighted in bold.

As shown in Table 2, the S2SAN model achieves the best results and the highest average accuracy on all the datasets, except for JD. Compared with the HAN model, which uses the same hierarchical structure, S2SAN improves the accuracy scores to different extents. The final average accuracy of HAN is 0.776, while the average accuracy of S2SAN is 0.788; thus, S2SAN improves the average accuracy by 1.2%.

Although the improvements were relatively small, we further compared the average training time required by each model to train for an epoch. The results are shown in Fig. 5. CNN and Transformer do not use the sequence model and require the least amount of time, but they

## Table 2

Accuracy and standard deviations of various models in 5-fold cross-validation on four datasets.

<table><tr><td></td><td colspan="5">Data</td></tr><tr><td>Model</td><td>Amazon</td><td>Yelp</td><td>JD</td><td>Douban</td><td>Average</td></tr><tr><td>TextCNN</td><td>0.719 ± 0.056</td><td>0.654 ± 0.048</td><td>0.720 ± 0.148</td><td>0.629 ± 0.082</td><td>0.681</td></tr><tr><td>BI-GRU</td><td>0.756 ± 0.004</td><td>0.748 ± 0.005</td><td>0.791 ± 0.056</td><td>0.749 ± 0.012</td><td>0.761</td></tr><tr><td>BI-GRU Attention</td><td>0.793 ± 0.008</td><td>0.757 ± 0.005</td><td>0.823 ± 0.007</td><td>0.749 ± 0.007</td><td>0.781</td></tr><tr><td>RCNN</td><td>0.788 ± 0.004</td><td>0.756 ± 0.009</td><td>0.803 ± 0.008</td><td>0.763 ± 0.016</td><td>0.778</td></tr><tr><td>Transformer</td><td>0.747 ± 0.010</td><td>0.710 ± 0.013</td><td>0.807 ± 0.01</td><td>0.765 ± 0.011</td><td>0.757</td></tr><tr><td>HAN</td><td>0.790 ± 0.009</td><td>0.754 ± 0.008</td><td>0.807 ± 0.007</td><td>0.753 ± 0.011</td><td>0.776</td></tr><tr><td>S2SAN</td><td>0.802 ± 0.006</td><td>0.769 ± 0.006</td><td>0.813 ± 0.019</td><td>0.768 ± 0.004</td><td>0.788</td></tr></table>

The best-performing model on each dataset is highlighted in bold.

have the lowest average accuracy. In the other five sequence-based models, the training times of S2SAN and HAN were significantly shorter than those of the nonhierarchical BI-GRU, BI-GRU ATTENTION and RCNN models. This finding indicates that lengthy calculations and the model training time can be reduced by dividing long sequences into several shorter sequences. In the two hierarchical models, note that they both converge at the second epoch, but S2SAN requires less training time than HAN does. The model complexity, training parameters and training time of the two hierarchical models are shown in Table 3.

In Table 3, n represents the sequence length, and d represents the vector dimension. In this experiment, we set the sentence length to 50, the number of sentences to 15, and the dimensions of the sentence vector and word vector to 400. Both HAN and S2SAN use BI-GRU as word encoders; therefore, the model complexity and training parameters are the same at the word level. However, at the sentence level, the complexity of the HAN model is O(n ⋅ d<sup>2</sup>), while the complexity of the S2SAN model is O(n<sup>2</sup>d). Obviously, the number of sentences n is smaller than the dimension d; consequently, the S2SAN model has lower complexity at the sentence level. Compared with the HAN model, the S2SAN model improves the accuracy by 1.2%, while consuming approximately only 75% of the training time.

## 4.4.2. Performance on cross-domain sentiment analysis

We further analyze the performance of the S2SAN model for crossdomain sentiment analysis. In this experiment, reviews from four do mains in Amazon have been chosen as datasets: “CDs and Vinyl”, “Cell Phones and Accessories”, “Clothing Shoes and Jewelry” and “Electronics”.

Four domains are labeled d1, d2, d3, and d4. We then divide these four domains into six groups in a pairwise combination. There are two sub-experiments in each group. One dataset will be employed as the training set, and the other dataset will be utilized as the test set; their roles are reversed in another sub-experiment. We record the experi mental results, as shown in Table 4. The best-performing model in each task is highlighted in bold.

S2SAN achieves the highest accuracy in 7 of 12 sub-experiments, which are “d2 to d1”, “d1 to d3”, “d1 to d4”, “d4 to d1”, “d2 to d3”, “d3 to d2”, and “d4 to d3”. In the remaining 6 sub-experiments, RCNN performs best in “d2 to d4” and “d4 to d2”, while Transformer performs best in “d1to d2”, “d3 to d1”, and “d3 to d4”. The highest average ac curacy is also achieved by S2SAN, which is 0.646. Followed by the RCNN and BI-GRU, their average accuracy is 0.630 and 0.628, respectively.

Table 1  
Corpus information.

<table><tr><td>Number</td><td>Origin website</td><td>Domain</td><td>Language</td><td>Number of review items (positive/neutral/negative)</td><td>Words per sentence</td><td>Sentences per review</td></tr><tr><td>1</td><td>Amazon.com</td><td>Electronic product</td><td>English</td><td>10,000/10,000/10,000</td><td>20.03</td><td>8.07</td></tr><tr><td></td><td></td><td>prod</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Yelp.com</td><td>Food and restaurant</td><td>English</td><td>10,000/10,000/10,000</td><td>11.10</td><td>3.89</td></tr><tr><td>3</td><td>Jd.com</td><td>Electronic product</td><td>Chinese</td><td>10,000/10,000/10,000</td><td>6.27</td><td>7.19</td></tr><tr><td>4</td><td>douban.com</td><td>Movie</td><td>Chinese</td><td>10,000/10,000/10,000</td><td>7.56</td><td>7.73</td></tr></table>

![](/api/attachments/GGCJKWXH/fulltext/images/d15a7d9368c383db3e24d219638e1bebb92783a8bf57f3afc6fd82f2c2a21ae8.jpg)

![](/api/attachments/GGCJKWXH/fulltext/images/abe2c3e0794cf57cad302c3ad722e0f34023b277756143ff57dc5f875d9d4f09.jpg)

![](/api/attachments/GGCJKWXH/fulltext/images/bcbc7fcde3a67673b9f2a5b568c549276099afac3b5fede3bf3040a22da7c009.jpg)

![](/api/attachments/GGCJKWXH/fulltext/images/a58e54dc1dc458fba05ef0a66d64acbe9e40392ccebaf2f44eee407963dc7284.jpg)  
Fig. 5. Accuracy and training time of domain-specific sentiment analysis.

Table 3  
Comparison of model complexity, training parameters and training time for the two hierarchical models.

<table><tr><td rowspan="2">Model</td><td colspan="2">Complexity per Layer</td><td colspan="2">Training Parameters</td><td colspan="5">Training Time per Epoch (Seconds)</td></tr><tr><td>Word level</td><td>Sentence level</td><td>Word level</td><td>Sentence level</td><td>Amazon</td><td>Yelp</td><td>JD</td><td>Dianping</td><td>Average</td></tr><tr><td>HAN</td><td> $O(n \cdot d^{2})$ </td><td> $O(n \cdot d^{2})$ </td><td>8.32 M</td><td>8.52 M</td><td>405</td><td>514</td><td>399</td><td>390</td><td>427</td></tr><tr><td>S2SAN</td><td> $O(n \cdot d^{2})$ </td><td> $O(n^{2} \cdot d)$ </td><td>8.32 M</td><td>8.34 M</td><td>323</td><td>306</td><td>347</td><td>314</td><td>322</td></tr></table>

Table 4  
Accuracy of cross-domain analysis.

<table><tr><td rowspan="2">Domain</td><td colspan="7">Model</td></tr><tr><td>TextCNN</td><td>BI-GRU</td><td>BI-GRU Attention</td><td>RCNN</td><td>Transformer</td><td>HAN</td><td>S2SAN</td></tr><tr><td>d1 to d2</td><td>0.516</td><td>0.523</td><td>0.540</td><td>0.558</td><td>0.590</td><td>0.556</td><td>0.575</td></tr><tr><td>d2 to d1</td><td>0.549</td><td>0.575</td><td>0.583</td><td>0.610</td><td>0.603</td><td>0.572</td><td>0.624</td></tr><tr><td>d1 to d3</td><td>0.502</td><td>0.586</td><td>0.574</td><td>0.573</td><td>0.591</td><td>0.583</td><td>0.607</td></tr><tr><td>d3 to d1</td><td>0.512</td><td>0.567</td><td>0.542</td><td>0.596</td><td>0.619</td><td>0.596</td><td>0.594</td></tr><tr><td>d1 to d4</td><td>0.440</td><td>0.546</td><td>0.545</td><td>0.535</td><td>0.571</td><td>0.557</td><td>0.587</td></tr><tr><td>d4 to d1</td><td>0.543</td><td>0.571</td><td>0.605</td><td>0.551</td><td>0.610</td><td>0.599</td><td>0.616</td></tr><tr><td>d2 to d3</td><td>0.619</td><td>0.685</td><td>0.690</td><td>0.693</td><td>0.643</td><td>0.697</td><td>0.712</td></tr><tr><td>d3 to d2</td><td>0.624</td><td>0.657</td><td>0.671</td><td>0.641</td><td>0.650</td><td>0.675</td><td>0.688</td></tr><tr><td>d2 to d4</td><td>0.635</td><td>0.642</td><td>0.680</td><td>0.699</td><td>0.636</td><td>0.679</td><td>0.686</td></tr><tr><td>d4 to d2</td><td>0.585</td><td>0.647</td><td>0.681</td><td>0.711</td><td>0.658</td><td>0.684</td><td>0.691</td></tr><tr><td>d3 to d4</td><td>0.614</td><td>0.624</td><td>0.650</td><td>0.639</td><td>0.693</td><td>0.642</td><td>0.674</td></tr><tr><td>d4 to d3</td><td>0.650</td><td>0.684</td><td>0.661</td><td>0.681</td><td>0.695</td><td>0.658</td><td>0.702</td></tr><tr><td>average</td><td>0.566</td><td>0.628</td><td>0.618</td><td>0.624</td><td>0.630</td><td>0.625</td><td>0.646</td></tr></table>

The best-performing model in each task is highlighted in bold.

One notable result is that in cross-domain sentiment analysis, although integrating a word-level attention layer, BI-GRU Attention yields lower accuracy than BI-GRU, which means that word attention fails to extract cross-domain sentiment information. However, with the improvement in sentence-level attention, both HAN and S2SAN, the two models that use BI-GRU Attention as the word encoder, achieve better accuracy, which indicates that sentence-level attention, especially sentence-to-sentence attention, helps to capture cross-domain sentiment information and enables basic word encoders to acquire better accuracy.

Fig. 6 further reveals the performance of S2SAN on different senti mental polarities. It can be shown that there is a large accuracy change range. For example, with the positive sentiment polarity, the accuracy of d2 for predicting d1 reaches 0.86, while the accuracy is merely 0.565 after switching the order to d1 for predicting d2. The accuracy of d2 for predicting d1 with negative and neutral polarity is 0.507 and 0.472, respectively, which lags the positive polarity. In addition, the overall color of (a) and (c) in Fig. 6 is deeper than that of (b). Combined with Fig. 7, we discover that S2SAN has a satisfactory performance in pre dicting positive sentimental polarity, with an accuracy of 0.71, followed by a negative polarity (0.66), and the performance on neutral polarity is the worst, only 0.57. There is a low prediction error between positive polarity and negative polarity. Only 11% of negative samples are pre dicted to be positive, and 10% of positive samples are predicted to be negative. However, in the neutral samples, 21% of the samples are predicted to be negative, and 22% of the samples are predicted to be positive.

Table 5

<table><tr><td>s\t</td><td>d1</td><td>d2</td><td>d3</td><td>d4</td></tr><tr><td>d1</td><td></td><td>0.726</td><td>0.651</td><td>0.717</td></tr><tr><td>d2</td><td>0.507</td><td></td><td>0.709</td><td>0.752</td></tr><tr><td>d3</td><td>0.726</td><td>0.765</td><td></td><td>0.672</td></tr><tr><td>d4</td><td>0.395</td><td>0.585</td><td>0.689</td><td></td></tr></table>

(a) accuracy on negative polarity

<table><tr><td>ts\t</td><td>d1</td><td>d2</td><td>d3</td><td>d4</td></tr><tr><td>d1</td><td></td><td>0.430</td><td>0.557</td><td>0.444</td></tr><tr><td>d2</td><td>0.472</td><td></td><td>0.638</td><td>0.527</td></tr><tr><td>d3</td><td>0.438</td><td>0.653</td><td></td><td>0.743</td></tr><tr><td>d4</td><td>0.620</td><td>0.735</td><td>0.585</td><td></td></tr></table>

(b) accuracy on neutral polarity

<table><tr><td>s\t</td><td>d1</td><td>d2</td><td>d3</td><td>d4</td></tr><tr><td>d1</td><td></td><td>0.565</td><td>0.595</td><td>0.597</td></tr><tr><td>d2</td><td>0.860</td><td></td><td>0.797</td><td>0.796</td></tr><tr><td>d3</td><td>0.681</td><td>0.661</td><td></td><td>0.579</td></tr><tr><td>d4</td><td>0.793</td><td>0.722</td><td>0.847</td><td></td></tr></table>

(c) accuracy on positive polarity  
Fig. 6. Accuracy on different polarities of cross-domain sentiment analysis (s denotes the source domain, and s represents the target domain).

## 4.4.3. Performance on multidomain sentiment analysis

Next, we conduct an experiment on multidomain sentiment analysis. Compared with domain-specific and cross-domain sentiment analysis, multidomain sentiment analysis should consider not only sentiment classification accuracy but also domain classification and overall clas sification accuracy. In this experiment, we further add four additional domains extracted from Yelp, including “Hotels”, “Arts”, “Shops” and “Restaurant”.

Table 5 gives the performance of S2SAN and baselines on three metrics. The best-performing model on each metric is highlighted in bold. As shown in Table 5, S2SAN achieves the best accuracy on all three metrics. The accuracy of sentiment classification is 0.788, and that of domain classification is 0.829, which is the same as the BI-GRU domain accuracy. The overall accuracy of S2SAN is 0.650, which is slightly higher than that of HAN. Unlike the cross-domain sentiment analysis, the three accuracy metrics of BI-GRU Attention are better than the metrics of BI-GRU. Thus, the word-level attention does not yield a negative optimization.

![](/api/attachments/GGCJKWXH/fulltext/images/08d7c69f048d6adfc2f04cc19d89b0d9354f177b22df8dea3be87b27b8bb146d.jpg)  
Fig. 7. Confusion matrix of cross-domain sentiment analysis.

Accuracy of multidomain analysis.

<table><tr><td rowspan="2">Model</td><td colspan="3">Accuracy</td></tr><tr><td>sentiment</td><td>domain</td><td>overall</td></tr><tr><td>TextCNN</td><td>0.704</td><td>0.779</td><td>0.547</td></tr><tr><td>BI-GRU</td><td>0.765</td><td>0.822</td><td>0.625</td></tr><tr><td>BI-GRU Attention</td><td>0.771</td><td>0.829</td><td>0.635</td></tr><tr><td>RCNN</td><td>0.772</td><td>0.813</td><td>0.624</td></tr><tr><td>Transformer</td><td>0.770</td><td>0.822</td><td>0.629</td></tr><tr><td>HAN</td><td>0.785</td><td>0.822</td><td>0.642</td></tr><tr><td>S2SAN</td><td>0.788</td><td>0.829</td><td>0.650</td></tr></table>

The best-performing model on each metric is highlighted in bold.

After applying two sentence-level attention to BI-GRU Attention, two hierarchical models (HAN and S2SAN) improve the sentimental accu racy and overall accuracy. However, the domain accuracy has not been optimized. HAN has decreased by 0.007, and S2SAN remains unchanged.

We further analyze the overall accuracy of S2SAN. Fig. 8 lists the detailed accuracy of S2SAN in different domains and sentiment polar ities. It can be seen that there is still a considerable difference among the accuracies. When the domain is hotel and the sentiment is negative, the highest accuracy rate of 0.808 is achieved. Regarding art and neutral, the accuracy rate is 0.532. Intuitively, we determine that the overall accu racy of the negative samples is better than that of the positive and neutral samples.

Fig. 9 reveals the performance of S2SAN in domain classification and sentiment classification. The performance of sentiment classification is similar to that of overall classification. The negative sentiment accuracy is the highest at 0.86, followed by the positive sentiment accuracy at 0.79; the neutral sentiment is the worst at 0.71. In domain classification, the accuracy of domains from Amazon is higher than that from Yelp. The best performance is obtained by CDs and Vinyl, and the worst perfor mance is obtained by Art. It can also be seen that the inner domains of

<table><tr><td>ds/d</td><td>CDs and Vinyl</td><td>Cell Phones and Accessories</td><td>Clothing Shoes and Jewelry</td><td>Electronics</td><td>Hotels</td><td>Art</td><td>Shop</td><td>Restaurant</td></tr><tr><td>Negative</td><td>0.766</td><td>0.714</td><td>0.753</td><td>0.650</td><td>0.808</td><td>0.582</td><td>0.721</td><td>0.688</td></tr><tr><td>Neutral</td><td>0.631</td><td>0.554</td><td>0.625</td><td>0.532</td><td>0.634</td><td>0.524</td><td>0.558</td><td>0.681</td></tr><tr><td>Positive</td><td>0.676</td><td>0.656</td><td>0.738</td><td>0.538</td><td>0.650</td><td>0.589</td><td>0.626</td><td>0.709</td></tr></table>

Fig. 8. Overall accuracy on different polarities and domains of multi-domain sentiment analysis (s denotes the sentiment and d represents the domain).

![](/api/attachments/GGCJKWXH/fulltext/images/c6def82c3c52cc6d65db8195d92b5450c22e23a8f5114f357ff8ddc95749501b.jpg)  
(a) confusion matrix of domain analysis

![](/api/attachments/GGCJKWXH/fulltext/images/013c0a2bc8af7578294a87bf78b0393b4e2cb77df768408b97a38c3c59d1aa2d.jpg)  
(b) confusion matrix of sentiment analysis  
Fig. 9. Confusion matrix of multi-domain sentiment analysis.

Amazon and Yelp have a larger prediction error, as shown in the upper left corner and lower right corner, respectively, of the confusion matrix in Fig. 9(b), while the prediction error between Amazon's domains and Yelp's domains is small, as shown in the upper right corner and lower left corner in Fig. 9(b).

## 4.4.4. Improvement of sentence-to-sentence attention on different word encoders

In Section 3, we mentioned that sentence-to-sentence attention is a framework that is independent of the underlying word encoder. In the previously described experiments, we also verified the performance advantages of the S2SAN model using BI-GRU and attention as the word encoder. In this section, we continue to explore whether sentence-to sentence attention improves the effect with different word encoders. Therefore, we chose a multilayer perceptron (MLP), CNN, RNN and LSTM as word encoders and conducted an experiment on the Amazon dataset. In this experiment, the model that integrates sentence-tosentence attention is denoted by S2S-MLP, S2S-CNN, S2S-RNN and S2S-LSTM.

As shown in Fig. 10, except for S2S-MLP, all S2S-models achieve higher best accuracy than the base models. In the CNN group experi ment, the initial accuracy of the standard CNN model is higher than that of the S2S-CNN model in the first epoch. However, in epochs 2 to 5, the S2SAN model performs better. The standard CNN model remains at approximately 0.72, while the S2S-CNN increases rapidly from 0.667 to 0.789. The highest accuracy achieved by the S2S-CNN is 0.779 in the third epoch, while the highest accuracy of the standard CNN model is 0.754 in the seventh epoch. The two models in the CNN group show greater volatility throughout the 10 rounds of testing than the other models. In the MLP group experiment, S2S-MLP also shows a greater advantage than the standard MLP model in the first 5 epochs. The ac curacy of S2S-MLP increases from 0.643 to 0.717, while that of the standard MLP increases from 0.567 to 0.701. After the fifth epoch, the accuracy of S2S-MLP tends to remain stable at approximately 0.72, while the standard MLP model shows a fluctuating ascending trend and the accuracy gradually increases until it exceeds 0.77. In the LSTM group, after the fourth epoch, a similar trend occurs for both the stan dard LSTM and the S2S-LSTM, and their accuracy is significantly lower than in the first four epochs. In the first four epochs, the accuracy of S2S-LSTM is higher than that of the standard LSTM. The accuracy of S2S-LSTM reaches its highest value (0.792) in the third epoch, while the accuracy of the standard LSTM reaches its highest value (0.733) in the fourth epoch. In the experimental RNN group, the test accuracy curves of both models are very stable, but S2S-RNN achieves higher accuracies than the standard RNN model throughout the process. The highest test accuracy of the S2S-RNN model is 0.735 in the second epoch, while the highest accuracy of the standard RNN model in the first three epochs is 0.665, which is also the highest accuracy achieved by the model.

![](/api/attachments/GGCJKWXH/fulltext/images/b5f34d3e76d018c15d529c8a22bd03a1d192c489a61dea8b4e9d6a6a0711fff4.jpg)  
Fig. 10. Accuracy comparison of base model and sentence-to-sentence attention model.

## 5. Discussion

In this study, we conducted several groups of experiments on four data sets. The first group of experiments involved a typical domainspecific sentiment analysis task. In this group of experiments, the S2SAN model not only slightly improves the accuracy but also reduces the training time. We discovered that the two hierarchical document representation models (HAN and S2SAN) require less training time than the general sequence models. The second experiment involved cross-domain sentiment analysis. We combined four domains from Amazon to form the cross-domain datasets. In this group of experiments, the S2SAN model reached the highest accuracy, which shows that sentence-to-sentence attention yields a positive optimization toward cross-domain sentiment analysis. However, S2SAN also lagged behind the RCNN and BI-GRU in some individual tests. We discovered that ac curacies with different source domains and target domains exhibit a significant gap. The third experiment is aimed at multidomain sentiment analysis. S2SAN also performs best in all three accuracy metrics. S2SAN yields a higher accuracy in positive and negative sentiment than neutral sentiment in both cross-domain experiments and multidomain experi ments. The last experiment verified whether sentence-to-sentence attention also improves the effect when using other word encoders. We selected four different word encoders: CNN, MLP, LSTM and RNN. Except for the MLP group, the other groups of comparative experiments showed a common phenomenon: the sentence-to-sentence models converge faster than standard models, and all the models showed greater advantages in the early training epochs.

S2SAN is a hierarchical text representation-based classification model for online comment text. The model adopts a new sentence-to sentence structure instead of the widely used sequence structure in sentence-level representation. This structure helps learn more about the relationship between different sentence semantics in multiple subspaces and obtain a better text representation vector. Abandoning the sequence structure also reduces the training time. S2SAN performs better than the baselines in most experiments. After being improved by the sentence-tosentence structure, the performance of some basic classifiers has been improved to varying degrees. However, S2SAN also has some limita tions. The accuracy of S2SAN is not much higher than that of other baselines; in cross-domain and multidomain sentiment analysis tasks, the accuracy has not reached a high level; the sentence-to-sentence structure does not have a good optimization effect on MLP. These are the directions that need improvement.

## 6. Conclusions

Online reviews contain a vast amount of sentiment information and have substantial value. Sentiment analysis of online reviews is a popular topic in the field of NLP. In addition, calculating the attention weights of different words in the review text using an attention mechanism has become a mainstream approach that has achieved considerable success. However, the semantics of each sentence in an online review text are individual rather than sequential, and less work has been performed on methods to calculate the weight of sentence-level attention. To fill these research gaps, we propose the sentence-to-sentence attention model, which can be employed with any underlying word encoder. We imple mented the S2SAN model using BI-GRU ATTENTION as the word encoder and achieved better results than those of several other baselines in multiple groups of domain-specific, cross-domain and multidomain sentiment analysis experiments. In addition, the accuracy and conver gence rates of some mature neural network models, such as CNN, RNN and LSTM, are improved by different degrees when reformed by the sentence-to-sentence attention framework.

The results of our research have meaningful theoretical and practical implications. Currently, many sentiment analysis methods disregard the semantic independence of sentences in a review and the diversity of sentence relations. Theoretically, our research proposed the S2SAN to fill this gap. This method provides a new perspective for sentence rep resentation and not only has lower computational complexity but also can learn a larger number of dependency relationships between sen tences. Meanwhile, with reasonable word-encoding compatibility, sentence-to-sentence attention can provide a simple but useful sentence representation framework for related research in NLP.

Practically, we know that there are many review texts without emotion tags on the Internet, and the sentiment attributes of these texts have not been identified, so it is difficult to make use of these valuable data. The proposed S2SAN can balance the accuracy of the sentiment analysis task with the training time. If this model is deployed, it can quickly and effectively analyze the sentiment polarity of massive online reviews and ensure the accuracy at a relatively high level, which is convenient for vendors and e-commerce platforms to find reviews with certain sentiment and thus enhance their understanding of users' atti tude toward their products and services. Moreover, S2SAN highly fo cuses on online comment text. In addition to measuring sentiment polarity, it can be used to detect other attributes of online reviews, such as usefulness, authority, and popularity when we use the relevant datasets to train the accuracy of S2SAN to a certain standard.

Our future work includes the following three points. (1) In the field of sentiment analysis, we intend to continue improving aspect level sentiment analysis and multiclass sentiment analysis experiments and observe whether the S2SAN model has the same advantages in these subfields. (2) The S2SAN model proposed in this study is aimed at online reviews. Whether this model has satisfactory performance in some longer texts with stronger logic, such as news and scientific and tech nological literature classification tasks, is another direction worth exploring. (3) In recent years, some pretraining models (e.g., BERT [59] and ELMo [67]) have refreshed many NLP records. The performance of the sentence-to-sentence attention model combined with the pretraining model is a future research interest.

## Funding

This work was supported by the National Natural Science Foundation of China [No. 72074171] and [No. 71774121].

## Acknowledgements

The numerical calculations in this paper were conducted on the supercomputing system in the Supercomputing Center of Wuhan University.

## References

[1] S.S.C. Shang, E.Y. Li, Y.L. Wu, O.C.L. Hou, Understanding web 2.0 service models: a knowledge-creating perspective, Inf. Manag. 48 (2011) 178–184, https://doi.org/ 10.1016/j.im.2011.01.005

[2] M. Sigala, E-service quality and web 2.0: expanding quality models to include customer participation and inter-customer support, Serv. Ind. J. 29 (2009) 1341–1358, https://doi.org/10.1080/02642060903026239.

[3] D. Yuan, Z. Lin, R. Zhuo, What drives consumer knowledge sharing in online travel communities?: personal attributes or e-service factors? Comput. Hum. Behav. 63 (2016) 68–74, https://doi.org/10.1016/j.chb.2016.05.019.

[4] S. Mudambi, D. Schuff, What makes a helpful online review? A study of customer reviews on amazon.com, MIS Q. 34 (2010) 185–200, https://doi.org/10.2307/ 20721420

[5] B. Liu, Sentiment analysis and subjectivity, in: N. Indurkhya, F.J. Damerau (Eds.), Handbook of Natural Language Processing, ACM Press, New York, NY, 2010, pp. 1–38.

[6] B. Pang, L. Lee, Opinion mining and sentiment analysis, Found. Trends Inf. Retr. 2 (2008)1–135. https://doi.org/10.1561/9781601981516

[7] T.L. Ngo-Ye, A.P. Sinha, The influence of reviewer engagement characteristics on online review helpfulness: a text regression model, Decis. Support. Syst. 61 (2014) 47–58, https://doi.org/10.1016/i.dss.2014.01.011.

[8] J. He, X. Wang, M.B. Vandenbosch, B.R. Nault, Revealed preference in online reviews: purchase verification in the tablet market, Decis. Support. Syst. 132 (2020) 113281, https://doi.org/10.1016/j.dss.2020.113281

[9] Y.C. Ku, C.P. Wei, H.W. Hsiao, To whom should I listen? Finding reputable reviewers in opinion-sharing communities, Decis. Support. Syst. 53 (2012) 534–542, https://doi.org/10.1016/j.dss.2012.03.003.

[10] X. Xu, Examining the role of emotion in online consumer reviews of various attributes in the surprise box shopping model, Decis. Support. Syst. 136 (2020) 113344, https://doi.org/10.1016/j.dss.2020.113344.

[11] X. Li, L.M. Hitt, Self selection and information role of online product reviews, Inf. Syst. Res. 19 (2008) 456–474, https://doi.org/10.1287/isre.1070.0154.

[12] A. Abdi, S.M. Shamsuddin, S. Hasan, J. Piran, Deep learning-based sentiment classification of evaluative text based on multi-feature fusion, Inf. Process. Manag. 56 (2019) 1245–1259, https://doi.org/10.1016/j.ipm.2019.02.018.

[13] L. Zhang, B. Liu, Sentiment analysis and opinion mining, in: C. Sammut, G. Webb (Eds.), Encyclopedia of Machine Learning and Data Mining, Springer, Boston, MA, 2016. http://iras.lib.whu.edu.cn:8080/rwt/SPRINGER/https/MSYXTLUQPJUB/ 10.1007/978-1-4899-7687-1\_907.

[14] M. Hu, B. Liu, Mining opinion features in customer reviews, in: Proceedings of the 19th National Conference on Artifical Intelligence, AAAI Press, San Jose, California, 2004, pp. 755–760.

[15] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up? Sentiment classification using machine learning techniques, in: Proceedings of the 2002 Conference on Empirical Methods in Natural Language Processing (EMNLP 2002), Association for Computational Linguistics, Philadelphia, PA, 2002, pp. 79–86.

[16] Y. Jiaiun, D. Bracewell, E. Ren, S. Kuroiwa, The creation of a Chinese emotion ontology based on hownet, Eng, Lett. 16 (2008) 166–171.

[17] R.M. Tong, An operational system for detecting and tracking opinions in on-line discussion, in: SIGIR Workshop on Operational Text Classification, OTC, New Orleans, Louisianna, 2001, pp. 1–6.

[18] H. Kanayama, T. Nasukawa, H. Watanabe, Deeper sentiment analysis using machine translation technology, in: COLING 2004: Proceedings of the 20th International Conference on Computational Linguistics, COLING, Geneva, Switzerland, 2004, pp. 494–500.

[19] B. Pang, L. Lee, A sentimental education: Sentiment analysis using subjectivity summarization based on minimum cuts, in: Proceedings of the 42nd Annual Meeting of the Association for Computational Linguistics (ACL-04). ACL Barcelona, Spain, 2004, pp. 271–278.

[20] M. Fern´andez-Gavilanes, T. Alvarez-L<sup>´</sup> opez, ´ J. Juncal-Martínez, E. Costa-Montenegro, F.J. Gonzalez-Casta´ no, ˜ Unsupervised method for sentiment analysi in online texts, Expert Syst. Appl. 58 (2016) 57–75, https://doi.org/10.1016/j eswa.2016.03.031.

[21] D. Tang, F. Wei, B. Qin, N. Yang, T. Liu, M. Zhou, Sentiment embeddings with applications to sentiment analysis, IEEE Trans. Knowl. Data Eng. 28 (2016) 496–509 https://doi org/10.1109/TKDE 2015.2489653

[22] V. Mnih, N. Heess, A. Graves, K. Kavukcuoglu, Recurrent models of visual attention, in: Proceedings of the 27th International Conference on Neural Information Processing Systems, MIT Press, Montreal, Canada, 2014, pp. 2204–2212.

[23] M. Song, H. Park, K.S. Shin, Attention-based long short-term memory network using sentiment lexicon embedding for aspect-level sentiment analysis in Korean. Inf. Process. Manag. 56 (2019) 637–653, https://doi.org/10.1016/j. ipm.2018.12.005.

[24] Z. Lin. M. Feng. C.N.D. Santos. M. Yu. B. Xiang. B. Zhou, Y. Bengio, A structured self-attentive sentence embedding, in: Proceedings of the 5th International Conference on Learning Representations, ICLR, Toulon, France, 2017, pp. 1–15

[25] Y. Wang, M. Huang, X. Zhu, L. Zha, Attention-based LSTM for aspect-level sentiment classification, in: Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing, Association for Computational Linguistics, Austin, Texas, 2016, pp. 606–615.

[26] Z. Yang, D. Yang, C. Dyer, X. He, A. Smola, E. Hovy, Hierarchical attention networks for document classification. in: Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Association for Computational Linguistics, San Diego CA 2016 pp 1480-1489

[27] A.S.H. Basari, B. Hussin, I.G.P. Ananta, J. Zeniarja, Opinion mining of movie review using hybrid method of support vector machine and particle swarm optimization, Procedia Eng. 53 (2013) 453–462, https://doi.org/10.1016/j proeng.2013.02.059.

[28] D. Garcia, F. Schweitzer, Emotions in product reviews–empirics and models, in: 2011 IEEE Third International Conference on Privacy, Security, Risk and Trust and 2011 IEEE Third International Conference on Social Computing, IEEE, Boston, MA, 2011, pp. 483–488.

[29] H. Cui, V. Mittal, M. Datar, Comparative experiments on sentiment classification for online product reviews, in: Proceedings of the Twenty-First National Conference on Artificial Intelligence and the Eighteenth Innovative Applications of Artificial Intelligence Conference, AAAI, Boston, Massachusetts, 2006, pp. 1265–1270.

[30] P. Zhang, Z. He, Using data-driven feature enrichment of text representation and ensemble technique for sentence-level polarity classification, J. Inf. Sci. 41 (2015) 531–549, https://doi.org/10.1177/0165551515585264.

[31] S. Deng, A.P. Sinha, H. Zhao, Adapting sentiment lexicons to domain-specific social media texts, Decis. Support. Syst. 94 (2017) 65–76, https://doi.org/10.1016/j. dss.2016.11.001.

[32] C. Zong, W. Feng, V.W. Zheng, H.H. Zhuo, Adaptive attention network for review sentiment classification, in: D. Phung, V. Tseng, G. Webb, B. Ho, M. Ganji, L. Rashidi (Eds.). Advances in Knowledge Discovery and Data Mining, PAKDD 2018, Lecture Notes in Computer Science, Springer, Cham, 2018, pp. 668–680

[33] Z. Wu, X.Y. Dai, C. Yin, S. Huang, J. Chen, Improving review representations with user attention and product attention for sentiment classification, in: The 31st AAAI Conference on Artificial Intelligence, AAAI Press, Honolulu, Hawaii, 2019, pp. 5989–5996.

[34] Z. Yuan, S. Wu, F. Wu, J. Liu, Y. Huang, Domain attention model for multi-domain sentiment classification, Knowl.-Based Syst. 155 (2018) 1–10, https://doi.org/ 10.1016/j.knosys.2018.05.004.

[35] J.S. Deshmukh, A.K. Tripathy, Entropy based classifier for cross-domain opinion mining, Appl. Comput. Inform. 14 (2018) 55–64, https://doi.org/10.1016/j aci.2017.03.001.

[36] J. Blitzer, M. Dredze, F. Pereira, Biographies, bollywood, boom-boxes and blenders: Domain adaptation for sentiment classification, in: A. Zaenen, A. van den Bosch (Eds.). Proceedings of the 45th Annual Meeting of the Association of Computational Linguistics, Prague, Czech Republic, Association for Computational Linguistics, 2007, pp. 440–447.

[37] S. Tan, X. Cheng, Improving SCL model for sentiment-transfer learning, in: Proceedings of NAACL HLT 2009: Short Papers, Association for Computationa Linguistics, Boulder, Colorado, 2009, pp. 181–184.

[38] Y. Li, T. Baldwin, T. Cohn, What’s in a domain? Learning domain-robust text representations using adversarial training, in: M. Walker, H. Ji, A. Stent (Eds.), Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Association for Computational Linguistics. New Orleans. Louisiana. 2018.

[39] D. Gupta. T. Chakraborty. S. Chakrabarti. Girnet: interleaved multi-task recurrent state sequence models. in: The 31st AAAI Conference on Artificial Intelligence (AAAI 2019), AAAI Press, Honolulu, Hawaii, 2019, pp. 6497–6504.

[40] Z. Chen, B. Liu, Mining topics in documents: standing on the shoulders of big data, in: Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, New York, NY, 2014, pp. 1116–1125

[41] J. Qiu, C. Liu, Y. Li, Z. Lin, Leveraging sentiment analysis at the aspects level to predict ratings of reviews, Inf. Sci. 451-452 (2018) 295–309, https://doi.org/ 10.1016/i.ins.2018.04.009

[42] K. Xu, J.L. Ba, R. Kiros, K. Cho, A. Courville, R. Salakhutdinov, R.S. Zemel, Y. Bengio, Show, attend and tell: Neural image caption generation with visual attention, in: Proceedings of the 32nd International Conference on International Conference on Machine Learning, JMLR, Lille, France, 2015, pp. 2048–2057.

[43] J. Ba, V. Mnih, K. Kavukcuoglu, Multiple object recognition with visual attention, in: 3rd International Conference on Learning Representations (ICLR 2015), San Diego, CA, 2015.

[44] D. Bahdanau, J. Chorowski, D. Serdyuk, P. Brakel, Y. Bengio, End-to-end attentionbased large vocabulary speech recognition, in: 2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), IEEE, Shanghai, China, 2016, pp. 4945–4949.

[45] J. Chorowski, D. Bahdanau, D. Serdyuk, K. Cho, Y. Bengio, Attention-based models for speech recognition, Comput. Therm. Sci. 10 (2015) 429–439.

[46] S. Kim, T. Hori, S. Watanabe, Joint CTC-attention based end-to-end speech recognition using multi-task learning, in: 2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE. New Orleans, LA. 2017.

[47] C. Yan, Y. Tu, X. Wang, Y. Zhang, X. Hao, Y. Zhang, Q. Dai, STAT: spatial-temporal attention mechanism for video captioning. JEEE Trans. Multimed. 22 (2020) 229–241. https://doi.org/10.1109/TMM.2019.2924576

[48] L. Yao, A. Torabi, K. Cho, N. Ballas, C. Pal, H. Larochelle, A. Courville, Describing videos by exploiting temporal structure, in: 2015 International Conference on Computer Vision (ICCV), IEEE, Santiago, 2015, pp. 4507–4515.

[49] D. Bahdanau, K. Cho, Y. Bengio, Neural machine translation by jointly learning to align and translate, in: 3rd International Conference on Learning Representations (ICLR 2015), San Diego, CA, 2015.

[50] T. Rocktäschel. E. Grefenstette. K.M. Hermann,. T. Kočiský. P. Blunsom. Reasoning about entailment with neural attention. in: The 4th International Conference or Learning Representations (ICLR 2016), San Juan, Puerto Rico, 2016, pp. 1–9.

[51] Y. Cui, Z. Chen, S. Wei, S. Wang, T. Liu, G. Hu, Attention-over-attention neural networks for reading comprehension, in: Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics. Association for Computational Linguistics, Vancouver, Canada, 2017, pp. 593–602

## P. Wang et al.

[52] J. Gehring, M. Auli, D. Grangier, D. Yarats, Y.N. Dauphin, Convolutional sequence to sequence learning, in: Proceedings of the 36th International Conference on Machine Learning, Long Beach, CA, 2017, pp. 1243–1252.

[53] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A.N. Gomez, Ł. Kaiser, I. Polosukhin, Attention is all you need, in: Proceedings of the 31st Annual Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, 2017, pp. 5998–6008.

[54] P. Chen, Z. Sun, L. Bing, W. Yang, Recurrent attention network on memory for aspect sentiment analysis, in: M. Palmer. R. Hwa, S. Riedel (Eds.). Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing, Association for Computational Linguistics, Copenhagen, Denmark, 2017, pp. 452–461.

[55] G. Pergola, L. Gui, Y. He, TDAM: a topic-dependent attention model for sentiment analysis, Inf. Process. Manag. 56 (2019) 102084, https://doi.org/10.1016/j. ipm.2019.102084.

[56] S. Gao, M.T. Young, J.X. Qiu, H.J. Yoon, J.B. Christian, P.A. Fearn, G.D. Tourassi, A. Ramanthan, Hierarchical attention networks for information extraction from cancer pathology reports, J. Am. Med. Inform. Assoc. 25 (2018) 321–330, https:/ doi.org/10.1093/iamia/ocx131

[57] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, J. Mach. Learn. Res. 3 (2003) 993–1022.

[58] T. Hofmann, Probabilistic latent semantic indexing, in: Proceedings of the 22nd Annual Internal ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR, Berkeley, CA, 1999, pp. 50–57.

[59] J. Devlin, M.W. Chang, K. Lee, K. Toutanova, Bert: pre-training of deep bidirectional transformers for language understanding, in: 2019 North American Chapter of the Association for Computational Linguistics, Minneapolis, Minnesota, 2019, pp. 4171–4186.

[60] Y. Song, MIHNet: combining N-gram, sequential and global information for text classification, J. Phys. Conf. Ser. 1453 (2020), 012156, https://doi.org/10.1088/ 1742-6596/1453/1/012156

[611 N. Gruber. A. Jockisch. Are GRU cells more specific and LSTM cells more sensitive in motive classification of text? Front. Artif. Intell. 3 (2020) 40, https://doi.org/ 10.3389/frai,2020.00040.

[62] Y. Kim, Convolutional neural networks for sentence classification, in: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), Doha, Qatar, 2014, pp. 1746–1751.

[63] K. Cho, B. van Merri¨enboer, D. Bahdanau, Y. Bengio, On the properties of neura machine translation: Encoder-decoder approaches, in: D. Wu, M. Carpuat, X. Carreras, E.M. Vecchi (Eds.), Proceedings of SSST-8, Eighth Workshop on Syntax, Semantics and Structure in Statistical Translation, Association for Computational Linguistics, Doha, Qatar, 2014, pp. 103–111.

[64] P. Zhou, W. Shi, J. Tian, Z. Qi, B. Li, H. Hao, B. Xu, Attention-based bidirectional long short-term memory networks for relation classification, in: K. Erk, N.A. Smith (Eds.). Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics. Association for Computational Linguistics. Berlin Germanv. 2016, pp. 207–212

[65] S. Lai, L. Xu, K. Liu, J. Zhao, Recurrent convolutional neural networks for text classification. in: Proceedings of the Twenty-Ninth AAAI Conference on Artificia Intelligence, AAAI Press, Austin, Texas, 2015, pp. 2267–2273.

[66] T. Tieleman, G. Hinton, Lecture 6.5-RMSprop: divide the gradient by a running average of its recent magnitude, COURSERA: neural Netw, Mach. Learn. 4 (2012) 26–30.

[67] M.E. Peters, M. Neumann, M. Iyyer, M. Gardner, C. Clark, K. Lee, L. Zettlemoyer, Deep contextualized word representations, in: Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2018), Minneapolis, MN, 2018, pp. 2227–2237.

Ping Wang, associate professor, he is working at School of Information Management, Wuhan University, Wuhan, China, 430072. He will be able to contact at wangping@whu. edu.cn if you have any questions. His research interests focus on data mining and data analysis, governmental information management, social media

Jiangnan Li, master student, she is studying at School of Information Management, Wuhan University, Wuhan, China, 430072. She will be able to contact at jiangnanli@whu. edu.cn if vou have any questions. Her research interests focus on data mining, sentiment analysis. social media

Jingrui Hou, master student, he is studying at School of Information Management, Wuhan University, Wuhan, China, 430072, he will be able to contact at houjingrui@whu.edu.cn if you have any questions. His research interests focus on natural language processing, sentiment analysis, deep learning.
