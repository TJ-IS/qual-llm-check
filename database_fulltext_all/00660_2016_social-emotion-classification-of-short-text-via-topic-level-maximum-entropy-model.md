---
otero_id: 660
otero_key: "KYDX8N2M"
title: "Social emotion classification of short text via topic-level maximum entropy model"
authors: "Yanghui Rao; Haoran Xie; Jun Li; Fengmei Jin; Fu Lee Wang; Qing Li"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2016.04.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Social emotion classification of short text via topic-level maximum entropy model

Author: Yanghui Rao<ce:author id="aut0010" biographyid="vt0010" orcid="0000-0003-0965-3617"> Haoran Xie Jun Li Fengmei Jin Fu Lee Wang Qing Li

![](/api/attachments/KYDX8N2M/fulltext/images/0aeccc580a3c98156e15df4920ece8efb952ade7808b3b1b7ed2c1e288198c84.jpg)

PII: S0378-7206(16)30038-6

DOI: http://dx.doi.org/doi:10.1016/j.im.2016.04.005

Reference: INFMAN 2903

To appear in: INFMAN

Received date: 14-7-2015

Revised date: 15-1-2016

Accepted date: 10-4-2016

Please cite this article as: Yanghui Rao, Haoran Xie, Jun Li, Fengmei Jin, Fu Lee Wang, Qing Li, Social emotion classification of short text via topic-level maximum entropy model, Information and Management http://dx.doi.org/10.1016/j.im.2016.04.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Social Emotion Classification of Short Text via Topic-Level Maximum Entropy Model

Yanghui Rao<sup>a</sup>, Haoran Xie<sup>b\*</sup>, Jun Li<sup>a</sup>, Fengmei Jin<sup>a</sup>, Fu Lee Wang<sup>c</sup>, Qing Li<sup>d</sup>

School of Data and Computer Science, Sun Yat-sen University, Guangzhou, China

<sup>b</sup> Department of Mathematics and Information Technology,

The Hong Kong Institute of Education, Hong Kong

<sup>c</sup> Caritas Institute of Higher Education, Hong Kong

<sup>d</sup> Department of Computer Science, City University of Hong Kong, Hong Kong

## Abstract

With the rapid proliferation of Web 2.0, the identification of emotions embedded in user-contributed comments at the social web is both valuable and essential. By exploiting large volumes of sentimental text, we can extract user preferences to enhance sales, develop marketing strategies, and optimize supply chain for electronic commerce. Pieces of information in the social web are usually short, such as tweets, questions, instant messages, messages, and news headlines. Short text differs from normal text because of its sparse word co-occurrence patterns, which hampers efforts to apply social emotion classification models. Most existing methods focus on either exploiting the social emotions of individual words or the association of social emotions with latent topics learned from normal documents. In this paper, we propose a topic-level maximum entropy (TME) model for social emotion classification over short text. TME generates topic-level features by modeling latent topics, multiple emotion labels, and valence scored by numerous readers jointly. The overfitting problem in the maximum entropy principle is also alleviated by mapping the features to the concept space. An experiment on real-world short documents validates the effectiveness of TME on social emotion classification over sparse words.

Keywords: topic-level maximum entropy model; social emotion classification; shorttext analysis; public opinion mining

## 1. Introduction

The big data era has descended on many communities including e-commerce, governments, and health organizations [2]. While there are increasingly numerous forms of multimedia content, such as images, photos, and videos, text is rapidly becoming a major part of enterprise data, especially for e-commerce firms [3]. Understanding text and extracting knowledge from it can be valuable to the business world, allowing for consolidation and promotion of customer opinions of a product, brand, or organization [4]. Social web is an important source of big data and is quite suitable for text mining [2]. With the prevalence of mobile Internet, more and more users can conveniently post messages to express their feelings through Twitter, Flickr, YouTube, and other social web apps. These messages provide a voice for customers to praise or criticize a particular product or service, which is useful for helping e-commerce firms understand the opinions of individuals, or to measure aggregated emotions of the public [5]. However, these data are not easily accessible to computers because they are not only primarily unstructured and specifically produced for human consumption [4], but also rapidly expanded and constantly evolved [6]. To analyze and better understand such large volumes of big data for e-commerce, it is indispensable to identify sentiments and opinions of users on them. A typical application of sentiment analysis is the stock price prediction, which extracts sentiment features from news articles to predict the directions of stock price movement [7, 8]. In light of these considerations and applications for ecommerce, sentiment analysis is concerned with the automatic and accurate emotion classification of an opinion holder towards either a topic or the overall tone of a document [9], which can facilitate comparison shopping, product design, marketing strategies development, and supply chain optimization [10].

Sentiment analysis has been extensively studied for product and movie reviews, which probably form a small part of the social web [11]. The other abundant sentimental documents include messages concerning politics, news and sports, and daily discussions in social network sites. Several factors hinder the application of traditional sentiment analysis methods in the above documents. First, unlike standard reviews with many words for most samples, the document length in the social web is quite diverse [11]. For instance, many documents posted in Twitter, Tumblr and other micro-blogging services only consist of a few phrases or 1–2 sentences. Second, traditional sentiment analysis research focused mainly on classifying the attitudes of authors/writers who created the reviews. Typically, this is achieved by using reviews where the author rating was expressed either with stars or with some numerical value to train machine learning algorithms [12]. In the social web, however, the emotion labels of documents (e.g., news, blog posts, and tweets) are mainly provided by readers using social annotation services such as online crowdsourcing [13]. For this reason, the aggregation of emotional responses from the reader is termed social emotion [14, 15]. Traditional sentiment analysis methods from the perspective of authors may not applicable to readers because authors and readers do not always share the same emotion for the same text [16, 17]. Thus, we aim to classify social emotions from the reader’s perspective over short documents.

Comment [A1]: AU: Please define SWAT.

Work has been performed to exploit the social emotion of individual words because words play a central role in how we describe and understand emotions [18]. The SWAT algorithm [19] was one of the top-performing lexicon-based algorithms on the SemEval ―affective text‖ task [20], which aimed to annotate news headlines according to the emotions they evoked in readers. In the SWAT algorithm, a word-emotion mapping lexicon was first constructed, in which, the emotions of each word was scored as the average of emotions of every headline contained this word. The emotion-term algorithm was created by improving the naïve Bayes classifier [14]. The algorithm differs from the traditional naïve Bayes classifier, by taking into account emotional ratings when calculating the probability of a category and the probability of a word given an emotion label. The limitation, however, of such word-level algorithms is that the words used to express certain emotions can be quite different across different contexts [21]. This difference is observed because words that have sentiment ambiguity and multiple emotions are difficult for word-level emotion lexicons to recognize [22].

As a concept-level approach [23], the topic model has emerged to measure the social emotions evoked by the online text. The emotion-topic model [14], the affective topic model [24], the multi-label supervised topic model, and the sentiment latent topic model [25] were built by introducing an additional layer of emotion modeling into latent Dirichlet allocation (LDA). Experimental results have shown that those topic-level models outperform word-level algorithms as well as support vector machines and several other methods in the classification of social emotions over normal documents.

With the emergence of social media, short documents are prevalent on the Web. The existing social emotion classification methods based on conventional topic models, such as LDA, typically used statistical techniques to learn the topic proportions of each document and the topic-word distributions. Thus, those topic-level models may suffer from the severe data sparsity problem (i.e., the sparse word co-occurrence patterns in individual document), and their performance is limited on social emotion classification over short documents [26]. An effective solution to the data sparseness problem is to employ the maximum entropy (ME) method [12], whose flexible modeling capability has alleviated data sparseness more successfully than the other probabilistic models. However, the standard word-level ME method suffers from undesirable overfitting, especially for sparse words because the equality constraints on feature expectations are uncertain. Although inequality constraints [27] can be used to alleviate such problems, it introduces extra cost to determine the optimal constraint width, and again, the same word may evoke different social emotions in different topics.

Motivated by the above observation, this paper is concerned with the following research questions:

 Given a set of short documents with social emotion labels, how can one predict social emotions for the new short documents in an effective and stable way?

 How can one alleviate the overfitting problem caused by the ME method and the sparse problem caused by conventional topic models in a unified social emotion classification model for short documents?

To address the abovementioned research questions, we propose a topic-level maximum entropy (TME) model for social emotion classification over short documents. We bring the insight that the problem of overfitting when using the ME method on sparse words can be alleviated by latent topics. To mitigate the data sparsity problem of conventional topic models, and the overfitting problem of the standard ME method, we learn latent topics over short documents by modeling the word co-occurrence patterns explicitly, in addition to using the aggregated word co-occurrence patterns in both the training and testing set to smooth the equality constraints on feature expectations. A real-world corpus that contained 11,813 short documents, which were emotionally annotated by readers, was employed to evaluate the effectiveness of our model. Experimental results show that the proposed model is robust against overfitting on sparse words. The rest of this paper is organized as follows. A summary of related work on sentiment analysis, social emotion classification, and short-text topic modeling is given in Section 2. Our model and experiment analysis are presented in Section 3 and Section 4, respectively. Finally, the paper’s conclusions are presented in Section 5.

## 2. Related Work

In this section, we briefly summarize the related work from the following three perspectives: sentiment analysis, social emotion classification on normal documents, and topic modeling over short text.

## 2.1 Sentiment Analysis

The first line of work on sentiment analysis applied many pre-developed sentiment lexicons, for example, Subjectivity Wordlist [28], WordNet-Affect [29], and SentiWordNet [30] to classify documents by emotions. The Subjectivity Wordlist is built by a manually selected seed set of subjective words, a small raw corpus, and an online dictionary, which is a subjectivity lexicon distinguishing subjective versus objective words. The WordNet-Affect is a linguistic resource in which the synsets representing emotional concepts are labeled. Synset is the synonym set that represents a sense or a concept in the WordNet lexicon. As many as 2,874 synsets and 4,787 words are annotated in the WordNet-Affect. The SentiWordNet is a lexical resource developed for supporting sentiment classification. This resource scores each synset in the WordNet along three emotional dimensions: positivity, negativity, and neutrality. The second method adopted either supervised [12] or unsupervised [31] learning algorithm for sentiment classification. However, these studies focus on extracting emotions from the perspective of writers primarily.

## 2.2 Social Emotion Classification

Social emotion classification annotates reader emotions towards certain contexts. The first line of research into social emotion classification is the ―affective text‖ in SemEval-2007 tasks [19]. To annotate social emotions of unlabeled news headlines, the proposed algorithms assumed that all words, even neutral ones, can effectively convey positive or negative emotions of readers. However, due to the limited information of news headlines or sentences, it is usually difficult to annotate the emotions consistently, even for a human [22]. Thus, the emotion-term [14] and the word-emotion [26] algorithms were proposed to make use of all words in the body of a news document. These algorithms were effective for associating different words with social emotions accurately, but they struggled to distinguish the sentiment ambiguity of the same word.

In order to recognize different emotional senses of the same word, topic models such as LDA were extended for social emotion classification, in which, a topic acted as an important component of an emotion, and informative and coherent topics were extracted and grouped under different emotions. In the emotion-topic model [14], a distribution over reader ratings is first generated from a multinomial distribution for each document. Then, for each word in the document, a single emotion label is sampled according to the above distribution. Finally, a latent topic is generated from a Dirichlet distribution conditioned to the emotion label, and a word is generated from the latent topic, which is modeled by another multinomial distribution over words. To have discriminative power between affective and background topics, the multi-label supervised topic model and the sentiment latent topic model [25] were proposed by representing the set of reader ratings as a bag of emotion labels. Another way to model all words, topics, and social emotions jointly is using the exponential distribution to generate reader ratings over each emotion label [24]. The limitation, however, of such topic-level models is that they were designed for normal text that contain sufficient words in an individual document.

## 2.3 Short-Text Topic Modeling

Short text is prevalent on the Web, especially with the emergence of social network apps. The main feature of short text is the sparsity of content. Because most words only occur once in each short text, it is difficult to conduct topic modeling and other tasks accurately. To address this issue, a common solution is to aggregate short documents into long pseudo-documents before training a standard topic model, that is, to expand short text and use external knowledge for short-text topic modeling. Phan et al. [32] trained a topic model over massive external data collected from Wikipedia or MEDLINE, and then predicted the topic distribution of short text. Jin et al. [33] proposed a Dual-LDA model that learns topics over both the original short text and related long documents. External linguistic knowledge could alleviate the problem of sparsity and enhance the topic learning of short text; however, it usually leads to topic bias, and the effectiveness of such methods is highly dependent on the accuracy of the external information. Therefore, according to the empirical comparison among topic learning methods over current data of Twitter [34], it is necessary to design a specialized and universal topic model for short text. To address these issues, Cheng et al. [35] proposed a generative biterm topic model (BTM) to learn topics over short documents by directly modeling the generation of biterms (i.e., unordered word pairs co-occurring in a short context) in the whole corpus. Unfortunately, these models were designed to reveal the main topics in a collection, not directly applicable for social emotion classification in short text.

## 3. TME Model

In this section, we propose the TME model for social emotion classification over short text. The extraction of topics from short text is first defined, and the framework of TME is subsequently presented in detail. An ME model using words as features, that is, word-level maximum entropy (WME), is also briefly described for comparison. Finally, we describe the estimation and prediction of parameters for TME.

## 3.1 Topic Extraction

The aim of topic extraction in the TME model is to identify the latent topics from short documents to tackle the data sparsity problem, which always occurs in word-level features. For example, two short documents ―BMW X1 is a good suv‖ and ―The oil cost of Benz cars is really expensive‖ do not have any overlapping features (terms) in the word level, while they share the same topic ―automobile‖ in topic level.

BTM was proposed to extract topics by breaking each document into biterms and learning a global topic distribution for short documents [35]. In the BTM, a biterm is constructed by any two distinct words co-occurring in a document.

BTM is an effective topic model over short documents. The generative process of BTM is as follows:

1. For the whole corpus, draw a topic distribution $\pmb \theta \sim \mathrm { D i r } ( \alpha )$

2. For the k-th topic, draw a word distribution $\pmb { \varphi } _ { k } \sim \operatorname { D i r } ( \beta )$

3. For each biterm $( w _ { i , 1 } , w _ { i , 2 } )$

(a) draw a topic assignment $z _ { i } \sim \mathrm { M u l t i } ( \theta )$

(b) draw two words $w _ { i , 1 } , w _ { i , 2 } \sim \mathrm { M u l t i } ( \pmb { \varphi } _ { z _ { i } } )$

In the above, the notation of ―biterm‖ denotes an unordered word pair co-occurring in a short text, that is, a small, fixed-size window over a word sequence. In short documents with limited length, each document is often used as an individual context unit. For instance, given a window size equal to three, a document with four words will generate five biterms: $( w _ { 1 } , w _ { 2 } , w _ { 3 } , w _ { 4 } ) \longrightarrow \{ ( w _ { 1 } , w _ { 2 } ) , ( w _ { 1 } , w _ { 3 } ) , ( w _ { 2 } , w _ { 3 } ) , ( w _ { 2 } , w _ { 4 } ) , ( w _ { 3 } , w _ { 4 } ) \}$ A larger size of the window will generate more biterms but weaken the probability of sharing the same topic for the two words. The biterm can also be extended to N-term (i.e., an unordered group of N words co-occurring in the same document), while the performance decreases gradually as N grows [35]. In particular, the model is equivalent to a mixture of unigrams when N is equal to or larger than the maximum length of documents in the corpus, which has a strict constraint of all the words in a document sharing the same topic.

BTM is appropriate for topic extraction of short text but is not designed for social emotion classification. In other words, BTM is an unsupervised topic model of learning topics from word co-occurrence patterns (i.e., biterms) in the whole corpus, while social emotion classification requires us to model words and multiple types of emotions voted by various readers jointly. A straightforward way to address the problem is to extend BTM by adding an extra distribution to generate reader ratings over each emotion, or using a two-layer generation process through representing the set of reader ratings as a bag of emotion labels. The challenge of these solutions, however, is that a large window size is required to generate enough biterms for each short document. Because a larger size of the window will weaken the probability of sharing the same topic for the two words, we cannot rely on tuning the window size to achieve good performance on social emotion classification of short text.

## 3.2 Model Description

In this section, we first define the issue of social emotion classification over short documents and the related notations, and then present our model that named TME

Comment [A5]: AU: ―then present our model that named TME‖ is unclear. Please clarify.

A short-text collection consists of D documents $\{ d _ { 1 } , d _ { 2 } , . . . , d _ { D } \}$ with word tokens and multiple emotion labels. We represent the set of all word tokens by $\left\{ w _ { 1 } , w _ { 2 } , . . . , w _ { V } \right\}$ where V is the number of unique word tokens. The k-th emotion label is represented as $e _ { k } \in [ 1 , E ]$ , where E is the amount of predefined emotion labels such as positive and negative. The numbers of training set with words and emotions jointly, and testing set with words only are $D _ { t r }$ and $D _ { t e } ,$ respectively. We formulate the task of social emotion classification over short text as learning an accurate classifier from the training set with sparse word co-occurrence patterns in individual documents to predict the evoked social emotions of unlabeled documents in the testing set. Following the convention of BTM, we denote the number of biterms and topics as $N _ { B }$ and $K ,$ respectively. The topic indicator of the i-th biterm $( w _ { i , 1 } , \ w _ { i , 2 } )$ is represented as $z _ { i } \in [ 1 , K ]$ . The prevalence of topics in the corpus is denoted by a multinomial distribution θ. The word distribution for topics is represented as a $K \times V$ matrix φ where the k-th row is a V-dimensional multinomial distribution. For the multiple emotion labels and reader ratings, a matrix R is used to represent the reader votes over each emotion label for all short documents in the training set. In the $D \times M$ matrix R, the element $r _ { j k }$ denotes the ratings over the k-th emotion among all users who have read the j-th short text. The reader ratings were normalized and summed to one for each short document.

To alleviate data sparseness, we associate word tokens and the generated topics with social emotions based on the ME principle. The ME principle states that from all the probability distributions, we should select the distribution that satisfies all prior conditions and constraints [37]. Different from the standard ME models using uni-grams or bi-grams as features, we generate features by the co-occurrences of w<sub>i</sub> and $e _ { k } ,$ in addition to $z _ { i }$ and $e _ { k } ,$ that is, $( z _ { i } , e _ { k } )$ . The set of all topic–emotion pairs is represented by Φ. Table 1 summarizes the notations of frequently used variables.

Table 1. Notations of frequently used variables.

<table><tr><td>Symbol</td><td>Description</td></tr><tr><td>D</td><td>Number of short documents</td></tr><tr><td> $D_{tr}$ </td><td>Number of training set</td></tr><tr><td> $D_{te}$ </td><td>Number of testing set</td></tr><tr><td>V</td><td>Number of unique word tokens</td></tr><tr><td>E</td><td>Number of predefined emotion labels</td></tr><tr><td>K</td><td>Number of topics</td></tr><tr><td>F</td><td>Number of unique features</td></tr><tr><td>Φ</td><td>Set of all topic-emotion pairs</td></tr><tr><td>R</td><td> $[r_{jk}]$ :  $D \times E$  matrix of normalized ratings for each emotion</td></tr></table>

The graphical representation of TME is shown in Figure 1, in which shaded nodes are observed data, blank ones are latent (not observed), and arrows indicate dependence. The set of all emotions and features is denoted by e and $f ,$ respectively.

![](/api/attachments/KYDX8N2M/fulltext/images/97ebb3838b40d7d5007287a7771bee0832cfcd9c415462cc2ed1c9d2175bce12.jpg)  
Fig. 1. Graphical representation of TME.

In our model, the prior conditions and constraints are the co-occurrences of word tokens, topic indicators, and emotion labels in the training set. The detail of associating word tokens with emotion labels can be found in Ref. [1], and we focus here on the additional modeling of topics and emotions. Table 2 shows the samples of a training set with topic indicators, where D = 3, K = 4, E = 3, and F = 12.

Table 2. Samples of a training set with topic indicators.

<table><tr><td>Short text</td><td>Topic indicators</td><td>Emotions and ratings</td><td>Features</td></tr><tr><td> $d_1$ </td><td>{1,2}</td><td> $e_1: r_{11}, e_2: r_{12}, e_3: r_{13}$ </td><td> $f_1(1, e_1), f_2(1, e_2), f_3(1, e_3),$  $f_4(2, e_1), f_5(2, e_2), f_6(2, e_3).$ </td></tr><tr><td> $d_2$ </td><td>{3,4}</td><td> $e_1: r_{21}, e_2: r_2, e_3: r_{23}$ </td><td> $f_7(3, e_1), f_8(3, e_2), f_9(3, e_3),$  $f_{10}(4, e_1), f_{11}(4, e_2), f_{12}(4, e_3).$ </td></tr><tr><td> $d_3$ </td><td>{2,3}</td><td> $e_1: r_{31}, e_2: r_{32}, e_3: r_{33}$ </td><td> $f_4(2, e_1), f_5(2, e_2), f_6(2, e_3),$  $f_7(3, e_1), f_8(3, e_2), f_9(3, e_3).$ </td></tr></table>

To associate multiple emotion labels annotated by users with topics generated by unsupervised topic models in short training documents, we use the following feature function based on the Bernoulli model:

$$
f _ {n} (z _ {i}, e _ {k}) = \left\{ \begin{array}{l l} 1 & z _ {i} \in [ 1, K ], e _ {k} \in [ 1, E ], (z _ {i}, e _ {k}) \in \Phi \\ 0 & o t h e r w i s e \end{array} \right.,\tag{1}
$$

where a binary indicator is assigned for each topic–emotion pair $( z _ { i } , e _ { k } )$ . For example, the second and the third columns of Table 2 present the topic indicators and reader ratings over three emotion labels of each training document, respectively. The first topic indicator in $d _ { 1 }$ is associated with each of the three emotion labels $e _ { 1 } , e _ { 2 } ,$ and $e _ { 3 } ,$ which generates three features, that is, $f _ { 1 } ( 1 , e _ { 1 } ) , f _ { 2 } ( 1 , e _ { 2 } )$ , and $f _ { 3 } ( 1 , e _ { 3 } )$ . Among various feature representation methods, the Bernoulli model works best for modeling short documents [38]. Thus, the value of all features listed in the third column of Table 2 is one.

We then measure the strength of each topic–emotion pair by aggregating the reader ratings of each training document over $e _ { k } ,$ , as follows:

$$
\overline {{p}} (z _ {i}, e _ {k}) \propto \left(\sum_ {d _ {j} \in \mathrm{T} _ {i}} r _ {j k}\right) / | \Phi |,\tag{2}
$$

where $\bar { p } ( z _ { i } , e _ { k } )$ is the empirical probability distribution of topic–emotion pair $( z _ { i } , e _ { k } )$ , Φ is the set of all topic–emotion pairs in the training set, and $\mathrm { T } _ { i }$ is the collection of training documents that contain $z _ { i } .$ In the above samples, we have $| \Phi | = 1 8 .$ , as shown in the last column of Table 2.

Given a set of features, the moment constraint is often used in the ME models [37]. It requires that the moment of the features as observed from the training set, that is, $\textstyle { \overline { { E } } } ( f _ { n } )$ , should be the same as that predicted from the model, that is, $E ( f _ { n } )$ . The expected value of each feature $f _ { n } ( z _ { i } , e _ { k } )$ with respect to the empirical distribution in the training set can be estimated by

$$
\bar {E} (f _ {n}) = \sum_ {z _ {i}, e _ {k}} \bar {p} (z _ {i}, e _ {k}) f _ {n} (z _ {i}, e _ {k}).\tag{3}
$$

The expected value of $f _ { n } ( z _ { i } , \ e _ { k } )$ with respect to the probability of emotion label $e _ { k }$ conditioned to topic indicator $z _ { i } ,$ that is, $p ( e _ { k } | z _ { i } )$ , is derived as follows:

$$
E (f _ {n}) = \sum_ {z _ {i}, e _ {k}} \overline {{p}} (z _ {i}) p (e _ {k} \mid z _ {i}) f _ {n} (z _ {i}, e _ {k}),\tag{4}
$$

where $\overline { { p } } ( z _ { i } )$ is the empirical distribution of $z _ { i }$ in the training set. Thus, the moment constraint of the TME is as follows:

$$
E (f _ {n}) = \bar {E} (f _ {n}).\tag{5}
$$

According to Eq. (3) and Eq. (4), we have

$$
\sum_ {z _ {i}, e _ {k}} \overline {{p}} (z _ {i}) p (e _ {k} \mid z _ {i}) f _ {n} (z _ {i}, e _ {k}) = \sum_ {z _ {i}, e _ {k}} \overline {{p}} (z _ {i}, e _ {k}) f _ {n} (z _ {i}, e _ {k}).\tag{6}
$$

A mathematical measure of the uniformity of the conditional distribution $p ( e _ { k } | z _ { i } )$ is provided by the conditional entropy:

$$
H (P) = - \sum_ {z _ {i}, e _ {k}} \overline {{p}} (z _ {i}) p (e _ {k} \mid z _ {i}) \log p (e _ {k} \mid z _ {i}).\tag{7}
$$

Then, the model is formulated as the following optimization problem:

$$
\begin{array}{l l} \min _ {p (e | z)} - H (P) = \sum_ {z _ {i}, e _ {k}} \overline {{p}} (z _ {i}) p (e _ {k} \mid z _ {i}) \log p (e _ {k} \mid z _ {i}) \\ \text { s.t. } & E (f _ {n}) - \overline {{E}} (f _ {n}) = 0 \quad 1 \leq n \leq F \\ & \sum_ {e _ {k}} p (e _ {k} \mid z) - 1 = 0 \quad \text { for   all } z. \end{array}\tag{8}
$$

To estimate the values of $p ( e | z )$ that minimize $H ( P )$ , we resolve the above primal optimization problem to an unconstrained dual optimization problem by introducing the Lagrange parameters $\lambda .$ The values of $p ( e | z )$ are estimated as follows:

$$
p _ {\lambda} (e \mid z) = \frac {1}{S _ {\lambda} (z)} \exp (\sum_ {n = 1} ^ {F} \lambda_ {n} f _ {n} (z, e)),\tag{9}
$$

$$
S _ {\boldsymbol {\lambda}} (z) = \sum_ {e} \exp (\sum_ {n = 1} ^ {F} \lambda_ {n} f _ {n} (z, e)).\tag{10}
$$

Next, we develop an iterative algorithm to achieve optimal values of $\lambda ,$ that is, the weight of connections between topics generated by unsupervised topic models and multiple emotion labels annotated by users, with the purpose being to predict socia emotions for the new unlabeled short documents.

## 3.3 Parameter Estimation

To estimate the topic indicator of each biterm z and the optimal values of each parameter $\lambda _ { n }$ for TME, an iterative algorithm is proposed, as shown in Algorithm 1. The number of biterms assigned to topic z is denoted by $c _ { z } ,$ and the number of times a word w is assigned to topic z is represented as $\boldsymbol { c } _ { w } ^ { z }$ . The symbol i means that the i-th biterm is excluded from the number. The model can also be simplified to a WME model when generating features $f ( w , e )$ for each word w in the 8-th step.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Iterative algorithm for TME
Input:
Topic number K, hyperparameters  $\alpha$  and  $\beta$ , window size s
Output:
Optimal values of each parameter  $\lambda_{n}$ , i.e., the weight of  $f_{n}(z, e)$ 
1. Extract a sequence of N words via a single scan over the documents
2. For b = 1 to N
3. For  $e = b + 1$  to  $b + s - 1$ 
4. Generate a biterm  $(w_{i,b}, w_{i,e})$  and  $i = i + 1$ 
5. Set  $c_{z}$ ,  $c_{w_{i,1}}^{z}$ , and  $c_{w_{i,2}}^{z}$  to 0
6. Randomly initialize the topic assignments for all the biterms
7. For each biterm  $(w_{i,1}, w_{i,2})$ , repeat until convergence
Draw topic z from  $(c_{-i,z} + \alpha)\frac{(c_{-i,w_{i,1}}^{z} + \beta)(c_{-i,w_{i,2}}^{z} + \beta)}{(c_{-i,\cdot}^{z} + V\beta + 1)(c_{-i,\cdot}^{z} + V\beta)}$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Update $c_z$, $c_{w_{i,1}}^z$, and $c_{w_{i,2}}^z$  
8. For each topic indicator $z$ and emotion label $e$  
Generate the feature $f_n(z, e)$ according to Eq. (1)  
9. Set $\lambda_n^{(0)}$ to 0  
10. For each $f_n$, repeat until convergence  
$\lambda_n^{(t+1)} = \lambda_n^{(t)} + \frac{\log\left(\overline{E}(f_n) / E^{(t)}(f_n)\right)}{M}$  
where $(t)$ is the iteration index and the constant $M$ is the length of the short text that contains the maximum number of topic indicators.
</div>

After estimating the optimal values of parameter $\lambda ,$ predicting the emotion label of unlabeled short text d is straightforward. We can first extract the topics of d using the same method of topic extraction used for the training set because the process is totally unsupervised. Next, the topic indicators of $d$ and each emotion label can be used to generate features according to Eq. (1). For example, given the topic indicators of 1 and 4 for $d ,$ the emotion label of d can be predicted as follows:

$$
p _ {\lambda} (e _ {1} \mid d) = \exp (\lambda_ {1} f _ {1} + \lambda_ {1 0} f _ {1 0}) / S _ {\lambda} (d),\tag{11}
$$

$$
p _ {\lambda} (e _ {2} \mid d) = \exp (\lambda_ {2} f _ {2} + \lambda_ {1 1} f _ {1 1}) / S _ {\lambda} (d),\tag{12}
$$

$$
p _ {\lambda} (e _ {3} \mid d) = \exp (\lambda_ {3} f _ {3} + \lambda_ {1 2} f _ {1 2}) / S _ {\lambda} (d),\tag{13}
$$

where

$$
S _ {\lambda} (d) = \exp (\lambda_ {1} f _ {1} + \lambda_ {1 0} f _ {1 0}) + \exp (\lambda_ {2} f _ {2} + \lambda_ {1 1} f _ {1 1}) + \exp (\lambda_ {3} f _ {3} + \lambda_ {1 2} f _ {1 2}).\tag{14}
$$

The difference between TME and WME on the prediction of unlabeled short text is the scope of feature utilized. For word-level models such as WME, we cannot generate features from the words that appear in the unlabeled documents but do not occur in the training set. Thus, as number of iterations increases, the prediction of social emotions will be more likely to overfit the sentiment orientation of words that only appear in the training set. The above problem is alleviated in TME by mapping the original words in both the training set and unlabeled documents to a unified concept space because the topics can be extracted without any emotion label.

## 4. Experiments

In this section, we evaluate the performance of the proposed model for social emotion classification over short text. We designed the experiments to achieve the following two goals: (i) to analyze the influence of the number of iterations on the accuracy of TME and WME and (ii) to conduct comparative analysis with various baselines.

## 4.1 Dataset

To test the adaptiveness, effectiveness, and robustness of our model on social emotion classification over short text, a real-world dataset was employed in the experiment<sup>†</sup>. The dataset contains 11,813 short documents including BBC Forum posts (BBC), Digg.com posts (Digg), MySpace comments (MySpace), Runners World forum posts (Runners World), Twitter posts (Twitter), and YouTube comments (YouTube). Each document was manually labeled by readers—who were allowed to use their own judgments rather than being trained to annotate in a predefined way—with the positive and negative sentiment strengths. The positive sentiment strength ranges from 1 (not positive) to 5 (extremely positive), and the negative sentiment strength ranges from –1 (not negative) to –5 (extremely negative). Table 3 summarizes the statistics of the dataset, where the second column presents the mean words of each document for the category.

Table 3. Statistics of the dataset.

<table><tr><td>Category</td><td>Mean words</td><td>Documents</td></tr><tr><td>BBC</td><td>64.76</td><td>1,000</td></tr><tr><td>Digg</td><td>33.63</td><td>1,077</td></tr><tr><td>MySpace</td><td>19.76</td><td>1,041</td></tr><tr><td>Runners World</td><td>64.25</td><td>1,046</td></tr><tr><td>Twitter</td><td>16.81</td><td>4,242</td></tr><tr><td>YouTube</td><td>17.38</td><td>3,407</td></tr><tr><td>All six combined</td><td>27.00</td><td>11,813</td></tr></table>

We randomly selected 50% of short documents as the training set and used the

remainder as the testing set.

## 4.2 Experimental Design

In order to evaluate the performance of the proposed TME model, as well as the ME model using words as features (WME), the following baselines were implemented for comparison:

1. SWAT algorithm, which was also designed for short text originally [19]. This algorithm scored the emotions of word w as the averaged emotional scores of every headline that contains w.

2. Emotion-term (ET) algorithm and emotion-topic model (ETM) [14]. The ET algorithm was proposed to improve the traditional naïve Bayes classifier, and the ETM was developed by introducing an additional topic layer into ET.

3. Multi-label supervised topic model (MSTM) and sentiment latent topic model (SLTM) [25]. The MSTM and SLTM designed a two-layer topic model to associate emotions with documents.

4. Affective topic model (ATM) [24]. The ATM used the exponential distribution to generate reader ratings over each emotion label.

To make an appropriate comparison between methods, all parameters in the topiclevel models (i.e., TME, ETM, MSTM, SLTM and ATM) were set as follows: (i) the hyperparameters α = 50 / K and β = 0.01. The values of them were tuned via grid search, which always works well on the short-text collection [35]. (ii) The iteration number of Gibbs sampling is 300. Here we randomly select 50% of training documents as the validation set to determine the above value. (iii) The number of topics K ranges from 100 to 300, and the validation set as mentioned earlier is used to choose the optimal K value. Although the value of K can be also determined by estimating the probability of words conditioned to topics [39], it has high time complexity.

In terms of the biterm extraction, we set the window size s to 3 for TME, because a larger size of the window will weaken the probability of sharing the same topic for the two words [35]. This is consistent with the characteristics of our experimental corpus. There are 815 (6.9%) documents with less than four words, a model with s > 3 will ―force‖ two words in many different documents to be the same topic. For instance, given $d _ { 1 } = \{ w _ { 1 } , w _ { 2 } , w _ { 3 } \}$ and $d _ { 2 } = \{ w _ { 4 } \}$ , it will generate six biterms when $s > 3 \colon ( w _ { 1 } , w _ { 2 } ,$ $w _ { 3 } , w _ { 4 } )  \{ ( w _ { 1 } , w _ { 2 } ) , ( w _ { 1 } , w _ { 3 } ) , ( w _ { 1 } , w _ { 4 } ) , ( w _ { 2 } , w _ { 3 } ) , ( w _ { 2 } , w _ { 4 } ) , ( w _ { 3 } , w _ { 4 } ) \}$ . The words from different documents, that is, $w _ { 1 }$ and $w _ { 4 } ,$ , occurred in $d _ { 1 }$ and $d _ { 2 }$ are combined to be a biterm, but they are unlikely to share the same topic. The value of s cannot be too small either, for example, when $s = 2 ,$ , the above sequence of four words will generate three biterms: $( w _ { 1 } , w _ { 2 } , w _ { 3 } , w _ { 4 } )  \{ ( w _ { 1 } , w _ { 2 } ) , ( w _ { 2 } , w _ { 3 } ) , ( w _ { 3 } , w _ { 4 } ) \}$ . In that case, although the two words within two windows have a large probability of sharing the same topic over the whole corpus, the number of biterms is even less than the original length of the documents.

## 4.3 Evaluation Metrics

We employed three evaluation metrics as indicators of performance: accuracy at top 1 $\left( \operatorname { A c c } @ 1 \right)$ , mean of average precision (MAP), and averaged Pearson’s correlation (AP). Acc@1 is essentially the micro-averaged F1 measure that weights precision and recall equally [38]. This metric was also used to evaluate the performance of various social emotion classification baselines [14, 24, 25]. Given an unlabeled document $d ,$ the topranked predicted emotion $e _ { p } ,$ and the truth emotion set $E _ { t o p @ d } ,$ , which includes the topranked emotions, $\mathsf { A c c } _ { d } @ 1$ is calculated as

$$
\operatorname{Acc} _ {d} @ 1 = \left\{ \begin{array}{l l} 1 & \text { if } e _ {p} \in E _ {\text { top@d }} \\ 0 & \text { else. } \end{array} \right.\tag{15}
$$

The emotion distribution of d is predicted correctly if $e _ { p } \in E _ { t o p @ d } .$ . Then, Acc@1 is estimated by averaging $\mathsf { A c c } _ { d } @ 1$ of all testing documents. MAP is used to measure the quality of a ranked list when there are only two coarse-grained levels: relevant and irrelevant [40]. AP is conducted using the averaged Pearson measure of correlation between the gold standard scores and the predicted scores over all emotion labels [19]. The higher the values of Acc@1, MAP, and AP, the better the model performance.

## 4.4 Influence of the Number of Iterations

To evaluate the influence of iteration number, we varied the number of iterations from 1 to 300. Figure 2 presents the Acc@1 of WME and TME over all datasets (i.e., the combined collections from BBC, Digg, MySpace, Runners World, Twitter, and YouTube)

when using different numbers of iterations.

![](/api/attachments/KYDX8N2M/fulltext/images/9548df9e63e18bd305fdb4dc14191197fe37cbb0e69199e452bda5b8d390b737.jpg)

![](/api/attachments/KYDX8N2M/fulltext/images/7280a32ae7e8fc2822ebe268a5c859ff0cba1441518afa247154501ef66343f4.jpg)  
Fig. 2. Performance of WME and TME over all datasets.

According to Figure 2, our first observation is that WME performed best in the first 50 iterations, while its performance was gradually decreased as the number of iterations increased. This is consistent with the ME principle that is employed by WME. Because the equality constraint was used for our models, as shown in Eq. (5), the weight of features (i.e., the co-occurrence of words and emotions in WME) overfitted to the training set with larger numbers of iterations. However, the drop rate of the performance was relatively slow over all datasets. The reason is that the number of generated features in all datasets is sufficient (the mean of words is 27). We also found that TME converged to its asymptote in approximately 100 iterations for 100, 200, and 300 topic numbers. This is because the topic indicator of each biterm can capture the same emotional orientation of different words. For example, in the category of electronic product reviews, the word ―compact‖ is often used to express a positive sentiment. On the other hand, in the books category the word ―exciting‖ expresses a primarily positive sentiment. The proposed TME is useful for modeling these words by combining them to biterms and mapping each biterm to the same topic indicator.

![](/api/attachments/KYDX8N2M/fulltext/images/380e231028e4bb15aee65b4a681ac0f1f2be90695d4d09f2cb5705d897c07e07.jpg)

![](/api/attachments/KYDX8N2M/fulltext/images/aafa8b214541c53b647d311af6c961ba1803b83c8150c74370f3760c737fbf9f.jpg)  
Fig. 3. Performance of WME and TME on Twitter subset.

Figure 3 illustrates the Acc@1 of WME and TME on Twitter subset. The results illustrate that the performance of WME was obviously decreased as the number of iterations increased. This is because the overfitting problem in WME becomes severe when the number of generated features is insufficient in the dataset (the mean of words is 16.81 in the Twitter subset). However, we can still find that TME has relatively flat curves for 100, 200, and 300 topic numbers over Twitter subset. The results in Figure 2 and Figure 3 indicate that the proposed TME can alleviate the problem of overfitting in ME and classify the social emotions accurately.

## 4.5 Comparison with Baselines

In this section, we measure and compare the performance of different models on social emotion classification over all datasets comprehensively, as presented in Table 4.

Table 4. Performance of different models over all datasets.

<table><tr><td>Models</td><td>Acc@1 (%)</td><td>MAP</td><td>AP</td></tr><tr><td>TME</td><td>86.06</td><td>0.87</td><td>0.46</td></tr><tr><td>WME</td><td>85.67</td><td>0.86</td><td>0.48</td></tr><tr><td>ETM</td><td>84.66</td><td>0.86</td><td>0.01</td></tr><tr><td>ET</td><td>85.72</td><td>0.87</td><td>0.00</td></tr><tr><td>SWAT</td><td>81.88</td><td>0.86</td><td>0.16</td></tr><tr><td>ATM</td><td>62.62</td><td>0.64</td><td>0.23</td></tr><tr><td>SLTM</td><td>74.38</td><td>0.85</td><td>0.11</td></tr><tr><td>MSTM</td><td>75.63</td><td>0.86</td><td>0.17</td></tr></table>

The results indicate that both TME and WME outperformed others in terms of AP and yielded performance that is competitive with various baselines in terms of Acc@1 and MAP. First, the existing topic-level models, that is, ETM, ATM, SLTM, and MSTM performed poorly on this combined corpus from six categories, because they focused on associating emotions with topics specific to one context primarily. The generated biterm in TME acted as the ―bridge‖ between different contexts, thus enhancing the social emotion classification performance in real-world environments. Second, although ET and SWAT performed well in terms of MAP, that is, the quality of a ranked list when there are only two coarse-grained levels, their performance was not satisfactory in terms of the fine-grained evaluation metric AP. This is because they used the limited words as features only, while both TME and WME generated features by exploiting reader ratings over multiple emotion labels. Third, TME performed well in terms of Acc@1 and MAP, while slightly worse than WME in terms of AP. The reason is that we used a validation set to choose the optimal number of iterations for both TME and WME, which may introduce differences on the performance over the testing set. It follows that a better method of determining the optimal iteration number deserves further research.

Table 5. Performance of different models on Twitter subset.

<table><tr><td>Models</td><td>Acc@1 (%)</td><td>MAP</td><td>AP</td></tr><tr><td>TME</td><td>85.01</td><td>0.84</td><td>0.31</td></tr><tr><td>WME</td><td>84.91</td><td>0.85</td><td>0.31</td></tr><tr><td>ETM</td><td>82.27</td><td>0.81</td><td>0.01</td></tr><tr><td>ET</td><td>85.20</td><td>0.83</td><td>0.00</td></tr><tr><td>SWAT</td><td>80.06</td><td>0.90</td><td>0.06</td></tr><tr><td>ATM</td><td>79.63</td><td>0.90</td><td>0.17</td></tr><tr><td>SLTM</td><td>78.88</td><td>0.86</td><td>0.05</td></tr><tr><td>MSTM</td><td>78.83</td><td>0.86</td><td>0.02</td></tr></table>

Table 5 presents the performance of different models on Twitter subset. We found that most models performed well in terms of the coarse-grained evaluation metric MAP, especially for SWAT and ATM. However, most existing models (e.g., ETM, ET, SWAT, SLTM, and MSTM) performed poorly in terms of AP. The experimental result shows that short documents lack enough content from which statistical conclusions can be drawn, thus the performance of these models was quite unstable. We exploited the reader ratings over multiple emotion labels to enrich features for both TME and WME, thus achieving better performance.

## 5. Conclusions

As increasing numbers of users share their experiences, ideas, and opinions on the Web [41, 42], sentiment analysis has become a popular topic for those who wish to understand public opinion from online data [43]. For instance, electronic commerce websites such as Amazon (www.amazon.com) and Epinions (www.epinions.com) allow users to write reviews on products, which have generated large volumes of data for sentiment analysis. Measuring the opinions of the general public regarding company strategies, marketing campaigns, product preferences, and social events has also steadily attracted interest in business intelligence areas [44]. Although sentiment analysis has attracted numerous investigations, little research has been performed on social web data from the reader’s perspective compared to product and movie reviews written by writers. Automatically classifying reader emotions can help us analyze the opinions/emotions embedded in user-contributed comments in the social web and further extract user preferences using big data analytics to enhance competitiveness for electronic commerce.

In this paper, we proposed a TME model to classify the social emotions evoked in readers. The topic indicators generated by unsupervised topic models were combined with word tokens to alleviate the overfitting problem in the ME principle. We conducted experiments to evaluate the effectiveness of the proposed models on real-world short documents. The results indicated that the performance of our approach is competitive when compared to various baselines. For future research, we plan to (i) explore the partof-speech information for feature generation, (ii) integrate recent learning models [45,

46, 47] to enhance the efficiency of the classification, and (iii) extend our approach to other applications, such as the emotionally aware recommendation of events in social media enhanced systems [48, 49] and multimedia retrieval systems by integrating with low-level features [50, 51, 52].

## Acknowledgments

The research described in this paper was substantially supported by the National Natural Science Foundation of China (No. 61502545), ―the Fundamental Research Funds for the Central Universities‖ (No. 46000-31610009), and a grant from the Research Grants Council of the Hong Kong Special Adminstrative Region, China (UGC/FDS/E06/14). This work has also been supported, in part, by a Strategic Research Grant (Project no. 7004218) and an Applied Research Grant (Project no. 9667095), both of City University of Hong Kong.

## Biography

Yanghui Rao is an assistant professor at the Sun Yat-sen University. He received his Ph.D. degree from the City University of Hong Kong in 2014, and his master’ s degree from the Graduate University of the Chinese Academy of Science in 2010. His research interests include social emotion classification, natural language processing, topic modeling, and event detection. Among these research areas, he has authored more than 20 papers for international journals and conferences. He has also served as the co-chair at the 1st International Workshop on User Modeling for Web-based Learning (IWUM) in conjunction with ICWL'15, and the PC member at the 2nd International Workshop on Semantic Computing and Personalization (SeCoP) in conjunction with DASFAA'15.

Haoran Xie is an assistant professor at the Hong Kong Institute of Education. He received his PhD and MSc from the City University of Hong Kong, and BEng from the Beijing University of Technology. His research interests include big data, social media, recommender systems, human computer interaction, and e-learning systems. He has published more than 60 research papers in many prestigious journals and conferences. He also served as a guest editor of Neurocomputing and International Journal of Distance Learning Technologies, a co-chair/committee member of SETE, SECOP, IWUM, ICWL, U-MEDIA, WISE, and HKWS.

Jun Li is currently pursuing his M.E. degree at the Sun Yat-sen University. His research interests include social emotion detection, natural language processing, and short-text classification.

Fengmei Jin is a student at the Sun Yat-sen University. Her research interests include sentiment analysis, natural language processing, and topic modeling.

Qing Li is a professor at the City University of Hong Kong. His research interests include object modeling, multimedia databases, social media, and recommender systems. He is a Fellow of IET, a senior member of IEEE, a member of ACM SIGMOD and IEEE Technical Committee on Data Engineering. He is the chairperson of the Hong

Kong Web Society, and is a steering committee member of DASFAA, ICWL, and WISE Society.

Fu Lee Wang is a professor and Vice-President (Research and Advancement) in Caritas Institute of Higher Education. He received BEng and MPhil from The University of Hong Kong, MSc from the Hong Kong University of Science and Technology, MBA from Imperial College London, and PhD from The Chinese University of Hong Kong. His research interests include electronic business, information retrieval, information systems, and e-learning. Before joining Caritas, he was a faculty member at the City University of Hong Kong. He is Past Chair of ACM Hong Kong Chapter and Chair of IEEE Hong Kong Section Computer Society Chapter. He served as program/conference chair of a number of international conferences.

## References

[1] Y.H. Rao, J. Li, X.Y. Xiang, H.R. Xie, Intensive maximum entropy model for sentiment classification of short text, in Proceedings of the 20th International Conference on Database Systems for Advanced Applications (DASFAA) Workshops, 2015, pp. 42-51.

[2] H. Chen, R.H.L. Chiang, V.C. Storey, Business intelligence and analytics: From big data to big impact, MIS Quarterly 36 (4) (2012) 1165-1188.

[3] E.-P. Lim, H. Chen, G. Chen, Business intelligence and analytics: Research directions, ACM Transactions on Management Information Systems 3 (4) (2013) 17-27.

[4] E. Cambria, B. Schuller, B. Liu, H.X. Wang, C. Havasi, Knowledge-based approaches to concept-level sentiment analysis, IEEE Intelligent Systems 28 (2) (2013) 12-14.

[5] X. Hu, L. Tang, J. Tang, H. Liu, Exploiting social relations for sentiment analysis in microblogging, in Proceedings of the 6th ACM International Conference on Web Search and Data Mining (WSDM), 2013, pp. 537-546.

[6] X. Wu, X. Zhu, G. Q. Wu, W. Ding, Data mining with big data, IEEE Transactions on Knowledge and Data Engineering 26(1) (2014) 97-107.

[7] X. Li, H. Xie, L. Chen, J. Wang, X. Deng, News impact on stock price return via sentiment analysis, Knowledge-Based Systems 69 (2014) 14-23.

[8] X. Li, H. Xie, Y. Song, Q. Li, S. Zhu, F. Wang, Does summarization help stock prediction? News impact analysis via summarization, IEEE Intelligent Systems 30 (3) (2015) 26-34.

[9] A. Gangemi, V. Presutti, D.R. Recupero, Frame-based detection of opinion holders and topics: A model and a tool, IEEE Computational Intelligence Magazine 9 (1) (2014) 20- 30.

[10] R.Y.K. Lau, C. Li, S.S.Y. Liao, Social analytics: Learning fuzzy product ontologies for aspect-oriented sentiment analysis, Decision Support Systems 65 (2014) 80-94.

[11] M. Thelwall, K. Buckley, G. Paltoglou, Sentiment strength detection for the social web, Journal of the American Society for Information Science and Technology 63(1) (2012) 163-173.

[12] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up? Sentiment classification using machine learning techniques, in Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP), 2002, pp. 79-86.

[13] Y. Wang and A. Pal, Detecting emotions in social media: A constrained optimization approach, in Proceedings of the 24th International Joint Conference on Artificial Intelligence (IJCAI), 2015, pp. 996-1002.

[14] S.H. Bao, S.L. Xu, L. Zhang, R. Yan, Z. Su, D.Y. Han, Y. Yu, Mining social emotions from affective text, IEEE Transactions on Knowledge and Data Engineering 24 (9) (2012) 1658-1670.

[15] Y.H. Rao, Contextual sentiment topic model for adaptive social emotion classification, IEEE Intelligent Systems, doi: http://dx.doi.org/10.1109/MIS.2015.91, 2015.

[16] Y.-J. Tang and H.-H. Chen, Mining sentiment words from microblogs for predicting writer-reader emotion transition, in: Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC), 2012, pp. 1226-1229.

[17] K. Lin and H. Chen, Ranking reader emotions using pairwise loss minimization and emotional distribution regression, in Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP), 2008, pp. 136-144.

[18] A. Kazemzadeh, S. Lee, S. Narayanan, Fuzzy logic models for the meaning of emotion words, IEEE Computational Intelligence Magazine 8(2) (2013) 34-49.

[19] C. Strapparave, R. Mihalcea, Semeval-2007 task 14: Affective text, in Proceedings of the 4th International Workshop on Semantic Evaluations (SemEval), 2007, pp. 70-74.

[20] R. Snow, B.O. Connor, D. Jurafsky, A.Y. Ng, Cheap and fast-but is it good? Evaluation non-expert annotations for natural language tasks, in Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP), 2008, pp. 254-263.

[21] D. Bollegala, D. Weir, J. Carroll, Using multiple sources to construct a sentiment sensitive thesaurus for cross-domain sentiment classification, in Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics (ACL), 2011, pp. 132- 141.

[22] C. Quan and F. Ren, An exploration of features for recognizing word emotion. In Proceedings of the 23rd International Conference on Computational Linguistics (Coling), 2010, pp. 922-930.

[23] R.Y.K. Lau, Y. Xia, Y. Ye, A probabilistic generative model for mining cybercriminal networks from online social media, IEEE Computational Intelligence Magazine 9 (1) (2014) 31-43.

[24] Y.H. Rao, Q. Li, L. Wenyin, Q.Y. Wu, X.J. Quan, Affective topic model for social emotion detection, Neural Networks 58 (2014) 29-37.

[25] Y.H. Rao, Q. Li, X.D. Mao, L. Wenyin, Sentiment topic models for social emotion mining, Information Sciences 266 (2014) 90-100.

[26] Y.H. Rao, J.S. Lei, L. Wenyin, Q. Li, M.L. Chen, Building emotional dictionary for sentiment analysis of online news, World Wide Web: Internet and Web Information Systems 17 (2014) 723-742.

[27] J. Kazama and J. Tsujii, Maximum entropy models with inequality constraints: A case study on text categorization, Machine Learning 60 (2005) 159-194.

[28] C. Banea, R. Mihalcea, J. Wiebe, A bootstrapping method for building subjectivity lexicons for languages with scarce resources, in Proceedings of the 6th International Conference on Language Resources and Evaluation (LREC), 2008, pp. 2764-2767.

[29] C. Strapparava and A. Valitutti, Wordnet-affect: An affective extension of wordnet, in Proceedings of the 4th International Conference on Language Resources and Evaluation (LREC), 2004, pp. 1083-1086.

[30] S. Baccianella, A. Esuli, F. Sebastiani, Sentiwordnet 3.0: An enhanced lexical resource for sentiment analysis and opinion mining, in Proceedings of the 7th Conference on Language Resources and Evaluation (LREC), 2010, pp. 2200-2204.

[31] P.D. Turney, Thumbs up or thumbs down? Semantic orientation applied to unsupervised classification of reviews, in Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics (ACL), 2002, pp. 417-424.

[32] X.H. Phan, L.M. Nguyen, S. Horiguchi, Learning to classify short and sparse text & web with hidden topics from large-scale data collections, in Proceedings of the 17th International World Wide Web Conference (WWW), 2008, pp. 91-100.

[33] O. Jin, N.N. Liu, K. Zhao, Y. Yu, Q. Yang, Transferring topical knowledge from auxiliary long texts for short text clustering, in Proceedings of the 20th ACM International Conference on Information and Knowledge Management (CIKM), 2011, pp. 775-784.

[34] L. Hong and B.D. Davison, Empirical study of topic modeling in Twitter, in Proceedings of the 1st Workshop on Social Media Analytics (SOMA), 2010, pp. 80-88.

[35] X. Cheng, X. Yan, Y. Lan, J. Guo, BTM: Topic modeling over short texts, IEEE Transactions on Knowledge and Data Engineering 26 (12) (2014) 2928-2941.

[36] K. Nigam, A. McCallum, S. Thrun, T. Mitchell, Text classification from labeled and unlabeled documents using EM, Machine Learning 39 (2) (2000) 103-134.

[37] D. Yu, L. Deng, A. Acero, Using continuous features in the maximum entropy model, Pattern Recognition Letters 30 (2009) 1295-1300.

[38] C.D. Manning, P. Raghavan, H. Schütze, Introduction to information retrieval, Cambridge University Press, 2008.

[39] T.L. Griffiths and M. Steyvers, Finding scientific topics, Proceedings of the National Academy of Sciences of the United States of America 101 (Suppl 1) (2004) 5228-5235.

[40] Q. Wang, O. Wu, W. Hu, J. Yang, W. Li, Ranking social emotions by learning listwise preference, in: Proceedings of the 1st Asian Conference on Pattern Recognition (ACPR), 2011, pp. 164-168.

[41] H. Xie, Q. Li, X. Mao, X. Li, Y. Cai, Q. Zheng, Mining latent user community for tagbased and content-based search in social media. Computer Journal 57(9) (2014) 1415- 1430

[42] T. Ma, J. Zhou, M. Tang, Y. Tian, A. Al-Dhelaan, M. Al-Rodhaan, S. Lee, "Social network and tag sources based augmenting collaborative recommender system," IEICE transactions on Information and Systems E98-D (4) (2015) 902-910.

[43] A. Tsai, C. Wu, R. Tsai, J. Hsu, Building a concept-level sentiment dictionary based on commonsense knowledge, IEEE Intelligent Systems 28 (2) (2013) 22-30.

[44] J.L. Zhao, S. Fan, D. Hu, Business challenges and research directions of management analytics in the big data era, Journal of Management Analytics 1 (3) (2014) 169-174.

[45] B. Gu, V.S. Sheng, K. Y. Tay, W. Romano, S. Li, Incremental Support Vector Learning for Ordinal Regression, IEEE Transactions on Neural Networks and Learning Systems, 26 (7) (2015) 1403-1416.

[46] B. Gu, V.S. Sheng, Z.J. Wang, D. Ho, S. Osman, S. Li, Incremental learning for ν- Support Vector Regression, Neural Networks, 67 (2015), 140-150.

[47] X.Z. Wen, L. Shao, Y. Xue, W. Fang, A rapid learning algorithm for vehicle classification, Information Sciences, 295 (1) (2015) , 395-406.

[48] H. Xie, X. Li, T. Wang, R.Y. K. Lau, T.-L. Wong, L. Chen, F. L. Wang, Q. Li, Incorporating sentiment into tag-based user profiles and resource profiles for personalized search in folksonomy. Information Processing and Management 52(1) (2016) 61-72.

[49] H. Xie, D. Zou, R. Y. K. Lau, F. L. Wang, T.-L. Wong, Generating incidental word learning tasks via topic-based and load-based profiles. IEEE MultiMedia 23(1) (2016) 60- 70.

[50] Z.Q. Pan, Y. Zhang, S. Kwong, Efficient motion and disparity estimation optimization for low complexity multiview video coding, IEEE Transactions on Broadcasting, 61 (2), (2015) 166-176.

[51] Y.H. Zheng, B. Jeon, D.H. Xu, Q.M Wu. Jonathan, H. Zhang, Image segmentation by generalized hierarchical fuzzy C-means algorithm, Journal of Intelligent and Fuzzy Systems, 28(2), (2015), 961-973.

[52] Z.H. Xia, X.H. Wang, X.M. Sun, Q.S. Liu, N.X. Xiong, Steganalysis of LSB matching using differences between nonadjacent pixels, Multimedia Tools and Applications, 75 (4) (2016), pp. 1947-1962.
