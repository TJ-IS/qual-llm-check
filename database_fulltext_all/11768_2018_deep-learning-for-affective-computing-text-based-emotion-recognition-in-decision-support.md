---
otero_id: 11768
otero_key: "AWXWRDQR"
title: "Deep learning for affective computing: Text-based emotion recognition in decision support"
authors: "Bernhard Kratzwald; Suzana Ilić; Mathias Kraus; Stefan Feuerriegel; Helmut Prendinger"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.09.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Deep learning for affective computing: text-based emotion recognition in decision support

ELSEVIE Decision Support Systems

Bernhard Kratzwald, Suzana Ilić, Mathias Kraus, Stefan Feuerriegel, Helmut Prendinger

![](/api/attachments/AWXWRDQR/fulltext/images/c297e28d057fe3f4486d2197244998fa1af6e903731c4eee900c6c4aba8cb9ae.jpg)

PII: S0167-9236(18)30151-9

DOI: doi:10.1016/j.dss.2018.09.002

Reference: DECSUP 12988

To appear in: Decision Support Systems

Received date: 23 March 2018

Revised date: 4 September 2018

Accepted date: 5 September 2018

Please cite this article as: Bernhard Kratzwald, Suzana Ilić, Mathias Kraus, Stefan Feuerriegel, Helmut Prendinger , Deep learning for affective computing: text-based emotion recognition in decision support. Decsup (2018), doi:10.1016/j.dss.2018.09.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Deep learning for afective computing: text-based emotion recognition in decision support

Bernhard Kratzwald<sup>a</sup>, Suzana Ili´c<sup>b,∗</sup>, Mathias Kraus<sup>a</sup>, Stefan Feuerriegel<sup>a</sup>, Helmut Prendinger<sup>b</sup>

<sup>a</sup>ETH Zurich, Weinbergstr. 56/58, 8092 Zurich, Switzerland <sup>b</sup>National Institute of Informatics, 2-1-2 Hitotsubashi, 101-8430 Tokyo, Japan

## Abstract

Emotions widely afect human decision-making. This fact is taken into account by afective computing with the goal of tailoring decision support to the emotional states of individuals. However, the accurate recognition of emotions within narrative documents presents a challenging undertaking due to the complexity and ambiguity of language. Performance improvements can be achieved through deep learning; yet, as demonstrated in this paper, the specific nature of this task requires the customization of recurrent neural networks with regard to bidirectional processing, dropout layers as a means of regularization, and weighted loss functions. In addition, we propose sent2afect, a tailored form of transfer learning for afective computing: here the network is pre-trained for a diferent task (i.e. sentiment analysis), while the output layer is subsequently tuned to the task of emotion recognition. The resulting performance is evaluated in a holistic setting across 6 benchmark datasets, where we find that both recurrent neural networks and transfer learning consistently outperform traditional machine learning. Altogether, the findings have considerable implications for the use of afective computing.

Keywords: Afective computing, Emotion recognition, Deep learning, Natural language processing, Text mining, Transfer learning

# ACCEPTED MANUSCRIPT

## 1. Introduction

Emotions drive the ubiquitous decision-making of humans in their everyday lives (Oatley et al., 2011; Greene & Haidt, 2002; Schwarz, 2000). Furthermore, emotional states can implicitly afect human communication, attention, and the personal ability to memorize information (Derakshan & Eysenck, 2010; Dolan, 2002). While the recognition and interpretation of emotional states often comes naturally to humans, these tasks pose severe challenges to computational routines (e. g., Poria et al., 2017; Tausczik & Pennebaker, 2010). As such, the term afective computing refers to techniques for detecting, recognizing, and predicting human emotions (e. g., joy, anger, sadness, trust, surprise, anticipation) with the goal of adapting computational systems to these states (Picard, 1997). The resulting computer systems are not only capable of exhibit empathy (Picard, 1995) but can also provide decision support tailored to the emotional state of individuals.

Emotional information is conveyed through a multiplicity of physical and physiological characteristics. Examples of such indicators include vital signs such as heart rate, muscle activity or sweat production on the surface of the skin (e. g., Lux et al., 2015; Tao, Jianhua and Tan, Tieniu and Picard, Rosalind W, 2011). A diferent stream of research tries to infer emotions from the content and its mode of communication. These approaches to afective computing are primarily categorized by the modality of the message, i. e., whether it takes the form of speech, gesture, or written information (Calvo & D’Mello, 2010). In this terminology, afective computing can comprise both unimodal and multimodal analyses. For instance, videos allow for the recognition of facial expressions and vocal tone (Chen et al., 2017; El Ayadi et al., 2011; Shan et al., 2009).

The focus of this work is on the unimodal analysis of written materials in English. This choice reflects the prominence of textual materials as a widespread basis for decisionmaking (Hogenboom et al., 2016). Illustrative examples are as follows (a detailed review is given later in Section 5.3). For instance, the use of afective language as a proxy for emotional closeness can be used to measure the strength of interpersonal ties in social networks (Marsden & Campbell, 2012). Similarly, marketing utilizes the recognition of emotional states in order to predict the purchase intentions of customers (Ang & Low, 2000), satisfaction with services (Greaves et al., 2013), and even to measure the overall brand reputation (Al-Hajjar & Syed, 2015). In a related context, decision support can leverage afective signals in financial materials in order to suggest trading decisions (Gilbert & Karahalios, 2010) or forecast the economic climate (Ormerod et al., 2015). Furthermore, afect can also improve processes and decision-making in the provision of healthcare (Spiro & Ahn, 2016) or education (Rodriguez et al., 2012).

Previous research on afective computing has merely utilized methods from traditional machine learning, while recent advances from the field of deep learning – namely, recurrent neural networks and transfer learning – have been widely overlooked. However, their use promises further improvements. In fact, techniques from deep learning have become prominent in various decision support activities involving sequential data (e. g., Evermann et al., 2017) and especially linguistic materials (e. g., Kraus & Feuerriegel, 2017; Mahmoudi et al., 2018), where deep learning was able to enhance the performance when deriving decisions from unstructured data. One of the inherent advantages of deep learning is that it can successfully model highly non-linear relationships.

This work draws upon existing solution techniques from the realm of deep learning (Kraus & Feuerriegel, 2017) and applies them to a problem domain diferent from that of our research objective. First and foremost, we extend existing techniques from the discipline of deep learning to the task of text-based emotion recognition in order to expand the body of knowledge. Following Kraus & Feuerriegel (2017), we also utilize long short-term memory networks (LSTMs) that can make predictions based on running texts of varying lengths. However, afective computing difers substantially from related tasks due to the high number of often imbalanced target labels. Thus, this task requires both customized network architectures and procedures. Hence, its applicability is only made possible through the several methodological innovations that we summarize in the following.

In order to handle class imbalances in afective computing, we propose the following modifications beyond Kraus & Feuerriegel (2017): (i) bidirectional processing of the text, (ii) dropout layers as a means of regularization, and (iii) a weighted loss function. The latter becomes especially critical due to the imbalanced distribution of labels. In fact, without the weighted loss function, the network ends up resembling merely a majority class vote.

We further propose an extension of transfer learning called sent2afect. That is, the network is first trained on the basis of sentiment analysis and, after exchanging the output layer, is then tuned to the task of emotion recognition. To the best of our knowledge, this presents a novel strategy for better afective computing as the inductive knowledge transfer is not merely based on a diferent dataset, but a diferent task.

Even though afective computing has gained great traction over the past several years (Ribei et al., 2016), there is a scarcity of widely-accepted datasets for text-based emotion recognition that can be used for benchmarking and that facilitate fair comparisons. A relatively small, but more common, dataset was provided by SemEval-2007 and consists of annotated news headlines (Strapparava & Mihalcea, 2007). A significantly larger, but underutilized, corpus is composed of afect-labeled literary tales (Alm, 2008). Our literature review notes considerable diferences across datasets that vary in their linguistic style, domain, afective dimensions, and the structure of the outcome variable. With regard to the latter, the majority of datasets involve a classification task in which exactly one afective category is assigned to a document, while others request a numerical score across multiple dimensions, i. e., a regression task. Hence, it is a by-product of this research to contribute a holistic comparison that benchmarks diferent methods across datasets used in prior research. For this purpose, we conducted an extensive search for afect-labeled datasets that serves as the foundation for our computational experiments. As a result, we find that deep learning consistently outperforms the baselines from traditional machine learning. In fact, we observe performance improvements of up to 23.2 % in F1-score as part of classification tasks and 11.6 % in mean squared error as part of regression tasks.

The findings of this work have direct implications for management, practice, and research. As such, various application areas of decision support – such as customer support, marketing, or recommender systems – can be improved considerably through the use of afective computing. Similarly, all systems with human-computer interactions (e. g. chatbots and personal assistants) could further benefit from emotion recognition and a deeper understanding of empathy. In fact, emotion detection could significantly impact and refine all use cases in which sentiment analysis (i. e., only positive/negative polarity) has already proved to be a valuable approach, since these lend themselves to a more fine-grained analysis and decisionmaking beyond only one dimension. In academia, text-based emotion recognition supports the cognitive and social sciences as a new approach to measuring and interpreting individual and collective emotional states.

The rest of this paper is structured as follows. Section 2 reviews earlier works on textbased emotion recognition, including the underlying afect theories, datasets used for benchmarking, and computational approaches. This reveals a research gap with regard to both deep neural networks and transfer learning within the field of afective computing. As a remedy, Section 3 introduces our methods rooted in deep learning, which are then evaluated in Section 4. Based on our findings, we detail implications for both research and management in Section 5, while Section 6 concludes.

## 2. Background

We specifically point out that the terms “sentiment analysis” and “afective computing” are often used interchangeably (D. Munezero et al., 2014). However, comprehensive surveys (Pang & Lee, 2008; Yadollahi et al., 2017) recognize clear diferences that distinguish each concept: sentiment analysis measures the subjective polarity towards entities in terms of only two dimensions, namely, positivity and negativity. Conversely, afective computing concerns the identification of explicit emotional states and, hence, this approach is also referred to as emotion recognition. The choice of emotional dimensions depends on the underlying afect theory and involves a wide range of mental states such as happiness, anger, sadness, or fear. For reasons of clarity, we strictly distinguish between the aforementioned concepts in our terminology.

Accordingly, this section first provides an overview of prevalent emotion models as specified by afect theories and, based on their dimensions, reviews computational methods for inferring afective information from natural language. This gives rise to a variety of use cases, which are detailed subsequently.

## 2.1. Afect theory

In the field of psychology, there is no consensus regarding a universal classification of emotions (Frijda, 1988; Izard, 2009), as physiological arousal in the proposed theories varies with causes, cognitive appraisal processes, and context. Yet a conventional approach is to

# ACCEPTED MANUSCRIPT

distinguish emotions based on how the underlying constructs are defined. On the one hand, emotions can be defined as a set of discrete states with mutually-exclusive meanings, while, on the other hand, emotions can also be characterized by a combination of numerical dimensions, each associated with a rating of intensity. The categorization into either a discrete set or a combination of intensity labels yields later benefits with regard to computational implementation, as it directly aids in formalizing the diferent machine learning models.

Categorical emotion models involve a variety of prevalent examples, including the socalled basic emotions. These introduce a discrete set of emotions with innate and universal characteristics (Tomkins, 1962; Izard, 1992). One of the first attempts by Ekman et al. (1987) to classify emotions led to the categorization of six discrete items labeled as basic: namely, anger, disgust, fear, happiness, sadness, and surprise. The model was later extended by Averill (1980) to include trust and anticipation, resulting in eight basic emotions. An alternative categorization by Tomkins (Tomkins, 1962, 1963) classifies nine primary afects into positive (enjoyment, interest), neutral (surprise), and negative (anger, disgust, dissmell, distress, fear, shame) expressions.

Dimensional models of emotion locate constructs in a two- or multi-dimensional space (Poria et al., 2017). Here the assumption of disjunct categories is relaxed such that the magnitude along each dimension can be measured separately (Russell, 1980), yielding continuous intensity scores. Diferent variants have been proposed, out of which we summarize an illustrative subset in the following. One of the earliest examples is Russell’s circumplex model (Russell, 1980), consisting of bivariate classifications into valence and arousal. Depending on the strength of each component, certain regions in the two-dimensional space are given explicit interpretations (such as tense, aroused, excited) according to 28 emotional states. The Wheel of Emotions is an extension of the circumplex model whereby eight primary emotion dimensions are represented as four pairs of opposites: joy versus sadness, anger versus fear, trust versus disgust, and surprise versus anticipation (Plutchik, 2001). Recent approaches introduce complex hybrid emotion models, such as the Hourglass of Emotions (Cambria et al., 2012), which represents afective states through both discrete categories and four independent, but concomitant, afective dimensions. However, neither the Wheel of Emotions nor the Hourglass of Emotions has yet found its way into common datasets for afective computing.

<table><tr><td rowspan="2">Ref.</td><td rowspan="2">Source</td><td rowspan="2">Samples</td><td colspan="4">Emotions</td><td rowspan="2">Notes</td></tr><tr><td>Annotation</td><td>Dimensions</td><td>Count</td><td>Affect theory</td></tr><tr><td>Alm (2008)</td><td>Literary tales</td><td>1,207</td><td>Categorical (m-out-of-n)</td><td>Anger, disgust, fear, happiness, sadness, surprise (pos.), surprise (neg.), neutral</td><td>8</td><td>Basic emotions from Ekman et al. (1987)</td><td>Evaluations conventionally draw upon subset where all annotators agree</td></tr><tr><td>Mohammad et al. (2015)</td><td>Election tweets</td><td>1,646</td><td>Categorical (1-out-of-n)</td><td>Anger, anticipation, disgust, fear, joy, sadness, surprise, trust</td><td>8</td><td>Basic emotions from Averill (1980)</td><td></td></tr><tr><td>Wallbott &amp; Scherer (1986)</td><td>Self-report of experiences</td><td>7,666</td><td>Categorical (1-out-of-n)</td><td>Anger, disgust, fear, guilt, joy, sadness</td><td>7</td><td>Based on basic emotions from Ekman et al. (1987)</td><td>Referred to as ISEAR dataset in related literature</td></tr><tr><td>Strapparava &amp; Mihalcea (2007)</td><td>Newspaper headlines</td><td>1,250</td><td>Numerical (for all dimensions)</td><td>Anger, disgust, fear, joy, sadness, surprise; additional valence score</td><td>6</td><td>Basic emotions from Ekman et al. (1987) with valence score according to Russell (1980)</td><td>SemEval-2007 (task 14); one numerical score per class</td></tr><tr><td>Mohammad et al. (2018)</td><td>General tweets</td><td>7,902</td><td>Numerical (single dimension only)</td><td>Anger, fear, joy, sadness</td><td>4</td><td>n/a</td><td>SemEval-2018 (task 1); for classification tweets with moderate and high emotion</td></tr><tr><td>Preotius-Cietro et al. (2016)</td><td>Facebook posts</td><td>2,894</td><td>Numerical</td><td>Valence, arousal</td><td>2</td><td>Circumplex model from Russell (1980)</td><td></td></tr></table>

Table 1: Overview of textual datasets used for afective computing in the literature grouped into classification and regression tasks for machine learning.

## 2.2. Datasets for benchmarking

Table 1 provides a holistic overview of datasets used for text-based afective computing. These datasets exhibit fundamentally diferent characteristics and challenges, as they vary in size, domain, linguistic style and underyling afect theory. We summarize key observations in the following.

In terms of text source, the datasets refer to tasks that utilize narrative materials from classic literature (Alm, 2008), while others are based on traditional media (Strapparava & Mihalcea, 2007), and even Twitter or Facebook posts (Preotiuc-Pietro et al., 2016). Social media, in particular, tends to be informal and subject to variable levels of veracity, especially in comparison with more formal linguistic sources such as newspaper headlines. Similar variations become apparent in terms of where the annotations originate from. For instance, emotion labels can rely upon self-reporting of emotional experiences (Wallbott & Scherer, 1986) or stem from ex post labeling eforts via crowdsourcing (Mohammad et al., 2015).

The majority of datasets were annotated based on categorical emotion models, thereby defining a discrete set of labels. The chosen emotions largely follow suggestions from the diferent afect theories and predominantly focus on basic emotions (or subsets thereof) due to their prevalence. Even though the number and choice of emotions difer, one can identify four emotions that are especially common as they appear in almost all categorical models:

anger, joy (happiness), fear, and sadness. Some emotions occur more often than others in the usual routines of humans (Plutchik, 2001; Ekman et al., 1987) and one thus obtains datasets (e. g., Strapparava & Mihalcea, 2007; Mohammad et al., 2015) wherein the relative frequency of emotions is highly unbalanced. This imposes additional computational challenges as classifiers tend to overlook infrequent classes.

In contrast, dimensional models of emotions appear less frequently. Only one dataset, composed of newspaper headlines (Strapparava & Mihalcea, 2007), provides a score for each of the six emotion categories. From a methodological point of view, this categorization into dimension-based models requires diferent prediction models. While categorical models refer to machine learning with single-label classification tasks in the sense that we identify the appropriate item based on a discrete label, dimensional models allow for regression tasks in the sense that we predict a score for every item and emotion.

## 2.3. Computational methods

The automatic recognition of text-based emotions relies upon diferent computational techniques that comprise lexicon-based methods and machine learning. Due to wealth of approaches, we can only summarize the predominant streams of research in the following and refer to Calvo & D’Mello (2010); Poria et al. (2017) for detailed methodological surveys.

## 2.3.1. Lexicon-based methods

Lexicon-based approaches utilize pre-defined lists of terms that are categorized according to diferent afect dimensions (Mohammad, 2012). On the one hand, these lexicons are often compiled manually, a fact which can later be exploited for keyword matching. For instance, the Harvard IV dictionary (inside the General Inquirer software) and LIWC provide such lists with classification by domain experts (Tausczik & Pennebaker, 2010). These were not specifically designed for afective computing, but still include psychological dimensions (e. g., pleasure, arousal and emotion in the case of Harvard IV; anxiety, anger, and sadness for LIWC). The NRC Word-Emotion Association lexicon was derived analogously but with the help of crowdsourcing rather than involving experts from the field of psychology research (Mohammad & Turney, 2013). The latter dictionary includes 10 granular categories such as anticipation, trust, and anger.

# ACCEPTED MANUSCRIPT

In order to overcome the need for manual dictionary creation, heuristics have been proposed to construct afect-related wordlists. Common examples include the WordNet-Afect dictionary, which starts with a set of seed words labeled as afect and then assigns scores to all other words based on their proximity to the seed words (Strapparava & Valitutti, 2004). However, the resulting afect dictionary includes only general categories of mood- or emotion-related words, rather than further distinguishing the type of emotion. More recent methods operate, for instance, via mixture models (Bandhakavi et al., 2017), fuzzy clustering (Poria et al., 2014), or by incorporating word embeddings (Li et al., 2017). The precision of dictionaries can further be improved by embedding these in linguistic rules that adjust for the surrounding context.

Dictionary-based approaches are generally known for their straightforward use and outof-the-box functionality. However, manual labeling is error-prone, costly, and inflexible as it impedes domain customization. Conversely, the vocabulary from the heuristics is limited to a narrow set of dimensions that were selected a priori and, as a result, this procedure has dificulties when generalizing to other emotions (cf. Agrawal & An, 2012).

## 2.3.2. Machine learning

Machine learning can infer decision rules for recognizing emotions based on a corpus of training samples with explicit labels (Danisman & Alpkocak, 2008; Chafar & Inkpen, 2011). This can overcome the aforementioned limitations of lexicon-based methods concerning scalability and domain customization. Moreover, it can also learn implicit signals of emotions, since findings from a comprehensive, comparative study suggest that afect is rarely communicated through emotionally-charged lexical cues but rather via implicit expressions (Balahur et al., 2012).

Previous research has experimented with diferent models for inferring afect from narrative materials. Examples include methods that explicitly exploit the flexibility of machine learning, such as random forests (e. g., Potapova & Gordeev, 2016) and support vector machines (e. g., Chatzakou et al., 2017; Danisman & Alpkocak, 2008), both of which have commonly been deployed in literature. Studies have shown that random forests tends to compute faster, while support vector machines yield superior performance (Chatzakou et al., 2017).

# ACCEPTED MANUSCRIPT

These classifiers are occasionally, but infrequently, restricted to the subset of afect cues from emotion lexicons (Bandhakavi et al., 2017). However, the more common approach relies upon general linguistic features, i. e., bag-of-words with subsequent tf-idf weighting (Alm et al., 2005; Strapparava & Mihalcea, 2007). Consistent with these works, we later draw upon machine learning models (i. e., random forest and support vector machine) together with tf-idf features as our baseline.

## 2.3.3. Deep learning

In the following, we discuss the few attempts at applying deep learning to afective computing, but find that actual performance evaluations are scarce. The approach in Potapova & Gordeev (2016) predicts aggression expressed through natural language using convolutional neural networks with a sliding window and subsequent max-pooling. However, this approach is subject to several limitations as the network is designed to handle only a single dimension (i. e., aggression) and it is thus unclear how it generalizes across multi-class predictions or even regression tasks that appear in dimensional emotion models. Even though the approach utilizes a “deep” network, its network architecture can only handle texts of predefined size, analogous to traditional machine learning. In this respect, it difers from recurrent networks, which iterate over sequences and thus can handle texts of arbitrary size.

The work in Felbo et al. (2017) utilizes an LSTM that is pretrained with tweets based on the appearance of emoticons; however, this work does not report a comparison of their LSTM against a baseline from traditional machine learning. A diferent approach (Gupta et al., 2017) utilizes a custom LSTM architecture in order to assign emotion labels to complete conversations in social media. However, this approach is tailored to the specific characteristics and emotions of this type of conversational-style data. In addition, the conclusion from their numerical experiments cannot be generalized to afective computing, since the authors labeled their dataset through a heuristic procedure and then reconstructed this heuristic with their classifier. Closest to our approach are experiments that include an LSTM for intensity estimation of emotions (Goel et al., 2017; Lakomkin et al., 2017; Meisheri et al., 2017; Zhang et al., 2017), but the results are limited to regression tasks where the presence of specific afective dimensions is given a priori.

Up to this point, the potential performance gains from using recurrent neural networks as the state of the art in deep learning have not yet been studied in relation to text-based emotion recognition. This fact was also noted in a recent literature survey (Poria et al., 2017).

## 2.4. Transfer learning

Transfer learning is a technique whereby knowledge from a source domain is leveraged in order to improve performance in a (possibly diferent) target domain. It is often used to overcome the constraints of limited training data, as well as for tasks that are sensitive to overfitting (Pan & Yang, 2010). A straightforward approach to transferring knowledge in natural language applications is to draw upon pretrained word embeddings (Kraus & Feuerriegel, 2017). This approach merely requires an additional dataset without labels as it operates in unsupervised fashion. However, it only facilitates the representation of words and fails to help learning parameters inside the neural network.

More complex strategies can even utilize labels and perform transfer learning from a source to a target dataset. The underlying transfer can occur either concurrently or sequentially:

• The former trains two networks concurrently on both the source and the target task with shared parameters. For instance, one network learns to translate sentences, while the other recognizes named entities (Mou et al., 2016). This is known to help the network concentrate on a shared understanding and, in practice, puts emphasis on more abstract relationships.

• The latter sequential procedure first trains a network on a source dataset and, in a second step, applies the network to the target dataset in order to fine-tune the network parameters (e. g., Kratzwald & Feuerriegel, 2018). This is often accompanied by minor modifications to network architectures (e. g., by replacing the prediction layer). While such an approach seems intriguing, it is impeded by the heterogeneous nature of baseline datasets for emotion recognition.

However, natural language applications often lack suitable source datasets (Mou et al., 2016). As a remedy, we propose sent2afect: that is, we employ not only a diferent dataset but also a diferent task (namely, sentiment analysis). To the best of our knowledge, this presents the first work on afective computing that attempts to accomplish an inductive knowledge transfer across tasks.

## 3. Methods

This section presents our methods for inferring emotional states from narrative contents. We first summarize our baselines from traditional machine learning and deep learning, while the inherent nature of afective computing requires us to come up with multiple innovations concerning the network architecture. Our proposed advances are detailed in Section 3.3. Finally, we detail our novel approach to transfer learning, called sent2afect, whereby knowledge from the related task of sentiment analysis is applied to emotion recognition. Figure 1 illustrates this pipeline.

![](/api/attachments/AWXWRDQR/fulltext/images/b0a2bf0c464d74fc739055f0da31abb349d74c0305864ed4bedf928e700099c5.jpg)  
Figure 1: Illustrative pipeline for inferring afective states from narrative materials. This can either happen through (i) traditional machine learning with feature engineering or, as proposed in this work, (ii) deep recurrent neural networks, optionally in conjunction with our proposed sent2afect transfer learning.

## 3.1. Benchmarks

## 3.2. Baselines from traditional machine learning

Traditional machine learning can only learn from a fixed-size vector of features and, for this purpose, features for machine learning are commonly built upon bag-of-words. The frequencies are further weighted by the tf-idf scheme in order to measure the relative importance of terms to a document within a corpus. Mathematically, the measure of term importance is obtained by computing the product of the term frequency and the inverse document frequency. This approach serves as a widely-accepted benchmark against which algorithms for natural language processing are evaluated.

The aforementioned features are then fed into the actual predictive models from traditional machine learning. Here we chose two approaches for both classification and regression as our baseline models: namely, random forest and support vector machine (i. e., a support vector regression for predictive numerical scores). These are known for their superior performance in previous studies (e. g., Chatzakou et al., 2017). Moreover, both approaches entail high flexibility when modeling non-linear relationships and demonstrate high accuracy even in settings where the number of potential features exceeds the number of observations.

## 3.2.1. Baselines from na¨ıve deep learning

Deep learning has triggered a paradigm shift in machine learning (Kraus et al., 2018) since it has yielded unprecedented performance results, especially for natural language processing. The theoretical argument for this is that recurrent neural networks from deep learning can iterate over the individual words of a sequence with arbitrary length. Here the input directly consists of words $x _ { 1 } , \ldots , x _ { N }$ and thus circumvents the need for feature engineering (e. g., creating bag-of-words with tf-idf) as used in traditional machine learning. As a result, recurrent neural networks store a lower-dimensional representation of the input sequence that encodes the whole document and can even maintain the actual word order with long-ranging semantics (Kraus et al., 2018). For this reason, recurrent neural networks difer from traditional machine learning, which can only adapt to short texts due to the use of n-grams.

We draw upon Kraus & Feuerriegel (2017) as the basis for our deep neural network architecture. This basic model consists of three layers: (a) an embedding layer that maps words in one-hot encoding onto low-dimensional vectors, (b) a recurrent layer to pass information on between words, and (c) a final dense layer for making the actual prediction. All three layers are described in detail in the online appendix. We experimented with this approach, but found that its performance is almost identical to a majority class vote. Therefore, we refrain from reporting the exact results; instead, we focus on the following improvements.

# ACCEPTED MANUSCRIPT

## 3.3. Proposed deep neural networks for afective computing

Using the aforementioned deep learning architectures is non-trivial for the following reasons. First, they are not suited to the small datasets from afective computing and typically lead to severe overfitting. Hence, we propose the use of a dropout layer as a form of regularization. Second, our task involves complex, open-domain language, which benefits further from bidirectional processing. Third, severe class imbalances are addressed by a weighted loss function. This loss function treats each class equally in order to avoid biases towards certain classes. Altogether, these extensions were necessary for using deep learning in our research setting.

## 3.3.1. Dropout layer

Deep neural networks can easily consist of up to millions of free parameters and, consequently, these models run the risk of overfitting. This is especially a problem when the training data is scarce. As a remedy, the weights in the network are regularized by randomly dropping out a certain share of neurons in order to improve the generalizability of the network. This prevents the neurons from co-adapting too much during training (Srivastava et al., 2014). We use dropout within the recurrent layer; that is, we randomly drop out connections between the recurrent LSTM cells. Dropout is disabled, i. e., all neurons are used, during test time in order to leverage the full predictive power of the learned parameters (cf. the online appendix for a detailed specification). Furthermore, we apply dropout between the output of the recurrent layer and the input to the prediction layer.

## 3.3.2. Bidirectional processing

To further improve the predictive performance of the base model, we draw upon so-called bidirectional recurrent layers, which have shown success in various other domains. That is, we use not only one but two LSTM layers to read the text. While one layer processes the text from left to right, a second one processes the text from right to left. More formally, let $h _ { 1 }$ determine the hidden state of the LSTM network that processes the input in the forward direction and $h _ { 2 }$ the hidden state of the LSTM that reads the text backwards. We then use the concatenation of both hidden states, e. g., $[ h _ { 1 } , h _ { 2 } ]$ , as input for the final prediction layer. Thus we are able to cover long- and short-term dependencies in both directions. We later abbreviate the bidirectional LSTM via BiLSTM and additionally run separate experiments for comparing the performance across the LSTM and BiLSTM.

## 3.3.3. Weighted loss functions for unbalanced data

Afective computing commonly involves multiple, highly imbalanced target labels. Using a na¨ıve loss function in this case would optimize towards the majority class and thus result in a performance similar to a majority vote. Such problems are typically addressed by over- or undersampling, yet these approaches yielded only marginal improvements in our experiments. As an alternative, we suggest the use of a weighted loss function. This multiplies the error of each data point with a weight that is the inverse size of the corresponding class.

Assume a training sample $x _ { i }$ with ground-truth label $y _ { i } ,$ and $p _ { i k }$ denoting the output of the prediction layer, e. g., the probability of $x _ { i }$ belonging to class k. Then the weighted loss for $x _ { i }$ is calculated via

$$
\mathcal {L} (x _ {i}, \theta) = w _ {i} \sum_ {k = 1} ^ {K} \mathbb {1} _ {y _ {i} = k} \log p _ {i k}\tag{1}
$$

with <sup>1</sup> denoting the indicator function. The weight $w _ { i }$ for input $x _ { i }$ depends solely on its ground truth label $y _ { i }$ and, similar to King & Zeng (2001), is calculated as

$$
w _ {i} = \frac {N}{K \sum_ {j} \mathbb {1} _ {y _ {j} = y _ {i}}},\tag{2}
$$

where K denotes the total number of classes and N the number of samples.

## 3.4. Sent2afect approach to transfer learning across tasks

Due to the large number of degrees-of-freedom, training deep neural networks is often associated with challenges (e. g., overfitting, inefective generalization). In practice, this is encountered by large datasets in order to prevent overfitting and, hence, a diferent strategy is often applied when handling smaller datasets such as those in our experiments. Here the idea is to implement transfer learning, i. e., the inductive transfer of knowledge from a diferent, yet related, task to the problem under investigation. In our case, we develop a novel approach, sent2afect, as detailed in the following.

The choice of the source task is non-trivial and it is mainly tasks of a semantically similar nature that result in the transferability of the network. For this purpose, we suggest the use of sentiment analysis as a related task, since it shares a certain similarity in the sense that positive and negative polarity is inferred from linguistic materials; however, sentiment analysis difers from afective computing, as it does not address afective dimensions or emotional states. The relatedness between both tasks enables the network to infer similar representation for both.

Formally, our approach to transfer learning optimizes the weights of a neural network for a target task T and dataset $\mathcal { D } _ { \mathcal { T } }$ based on a diferent, yet related, source task S with dataset $\mathcal { D } _ { \mathcal { S } }$ . After optimizing the parameters of our network for S on $\mathcal { D } _ { \mathcal { S } }$ we replace the task-specific prediction layer of the network to yield predictions for our target task T . Therefore, we utilize the estimated parameters as an initial value for further optimization with the help of the actual dataset $\mathcal { D } _ { \mathcal { T } }$ (Pan & Yang, 2010). The pseudocode of the overall process is stated in Algorithm 1.

In our experiments, we utilize a large-scale, public dataset<sup>1</sup> as a basis for knowledge induction. This dataset finds widespread application in sentiment analysis and includes about 100,000 samples labeled according to positive or negative sentiment. We then optimize the deep neural network with the goal of predicting the underlying sentiment scores. The resulting coeficients of the network are further trained with an actual dataset from afective computing. Here the diferences in the data type of the prediction outcome (i. e., computing a positivity/negativity score versus afective dimensions) are handled by removing the dense layer and, instead, amending a new prediction layer that targets the new output. As a result, the majority of weights benefits from transfer learning, while only the neurons in the prediction layer are training after a random initialization. The intuition of this approach is as follows: deep neural networks generally contain multiple layers, where layers closer to the final prediction layers are supposed to encode the original input at a higher level of abstraction.

<sup>1</sup>Kaggle: Twitter sentiment analysis, retrieved from https://www.kaggle.com/c/ twitter-sentiment-analysis2, March 21, 2018.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 sent2affect transfer learning
Input: Given training data $\mathcal{D}_{\mathcal{T}}$ for the affective computing task $\mathcal{T}$ and additional corpus $\mathcal{D}_{\mathcal{S}}$ for sentiment analysis $\mathcal{S}$
1: $m \leftarrow$ Initialize recurrent neural network (i.e. consisting of recurrent layer $f$, dense layer $\psi, \ldots$)
2: $m \leftarrow$ Estimate parameters w.r.t. $\mathcal{S}$ using $\mathcal{D}_{\mathcal{S}}$
3: $\psi \leftarrow$ Replace dense layer with randomly-initialized dense layer according to the dimensions of $\mathcal{T}$
4: $\psi \leftarrow$ Fine-tune $\psi$ w.r.t. $\mathcal{T}$ using $\mathcal{D}_{\mathcal{T}}$
5: return Recurrent neural network $m$
</div>

## 3.5. Model estimation

Consistent with previous research (Manning & Sch¨utze, 1999), we tokenize each document, convert all characters to lower-case, and remove punctuation, numbers, and stop words. Moreover, we perform stemming, which maps inflected words onto a base form; e. g., “played” and “playing” are both mapped onto “play”. We conducted all pre-processing operations to yield bag-of-words representations by using the natural language tookit NLTK.

For those datasets with no designated test set, we introduced a random 80/20 split in training and test data. For the random forest classifier, we manually optimized over the number of trees, maximum number of features for every split, and the depth. For the support vector classifier, we conducted an extensive grid-search over the hyperparameters following Hsu et al. (2003). In detail, we experimented with linear, radial basis function, and sigmoid kernels, optimizing the cost C over 2<sup>−5</sup>, 2<sup>−3</sup>, . . . , 2<sup>15</sup> and the radius parameter γ over $2 ^ { - 1 5 } , 2 ^ { - 1 3 } , \ldots , 2 ^ { 3 }$ . For unbalanced datasets, we weighted the loss function by class frequency in order to prevent models from predicting the majority classes only.

We used diferent deep learning models. Depending on the specification, we used pretrained GloVe<sup>2</sup> embeddings or randomly-initialized embeddings (which are learned jointly during the training phase). The models were trained using the Adam optimizer, whereby the process was stopped once we noted an increase in the validation error. For reasons of reproducibility, we report the performance metrics averaged over 10 independent runs.

## 4. Evaluation

This section reports our computational experiments evaluating the improvements gained by using deep neural networks (and especially transfer learning) for afective computing. Here we draw upon all datasets from Table 1 and, according to the type of the underlying afect theory, we divide the performance measurements into classification and regression tasks.

## 4.1. Classification according to categorical emotion models

We begin with classification tasks according to categorical emotion models, where the objective is to predict the predominant emotion(s). We follow previous literature (e. g., Chatzakou et al., 2017; Danisman & Alpkocak, 2008) and analogously choose two baselines prevalent in traditional machine learning: namely, the random forest classifier and the support vector machine. Both are fed with bag-of-words with tf-idf weighting, whereas the proposed deep neural networks circumvent the need for feature engineering. Here we compare variants that extend the $\mathrm { L S T M ^ { 3 } }$ with bidirectional encodings and pretrained word embeddings. The resulting performance is listed in Table 2, where we account for unbalanced distributions of labels by using the weight-averaged F1-score. The F1-score for a single class is given by the harmonic mean of precision and recall, i. e.,

$$
\mathrm{F1} = 2 \frac {\mathrm{precision} \cdot \mathrm{recall}}{\mathrm{precision} + \mathrm{recall}}.\tag{3}
$$

In addition, we report sensitivity and specificity scores. The sensitivity of a single class equals the recall, while the specificity measures the fraction of true negatives. Similar to the F1-score, we calculate both independently for each class, i. e.,

$$
\text {sensitivity} = T P / (T P + F N) \quad \text {and} \quad \text {specificity} = T N / (T N + F P),\tag{4}
$$

where the number of true positives and true negatives is denoted by TP and TN , and the number of false positives and false negatives is denoted by FP and FN . For the final scores, we average over all classes weighted by the class size.

# ACCEPTED MANUSCRIPT

Our results in Table 2 consistently reveal superior performance through the use of deep learning. We observe that, regardless of the architecture, models with pre-trained GloVe embeddings outperform their counterparts with randomly-initialized word embeddings. In fact, the use of pre-trained word embeddings yields performance improvements over the best baseline in 9 out of 10 experiments. An explanation stems from the fact that embeddings which have not been pre-trained result in considerably more degrees-of-freedom and thus a greater chance of overfitting. Our initial expectations are met as the imposed dropout layers and loss-weighting successfully diminish the problem of overfitting. Furthermore, our imposed architectural enhancements surpass the performance of previous deep learning architectures, such as that proposed by Kraus & Feuerriegel (2017). As such, the bidirectional recurrent layers outperform the variant with a unidirectional layer in four out of five experiments, yielding the only architecture that consistently outperforms the traditional baseline on all datasets, with improvements between 1.6 % and 23.2 % across the datasets. We experimented with the na¨ıve network from Kraus & Feuerriegel (2017), but it failed in three out of five datasets resulting in merely predicting the majority class; hence, we omitted the results.

The performance gains from our proposed architectural improvements are a result of the class imbalance and the language noise of the source. For instance, the highest relative improvement over traditional machine learning is achieved in the case of the dataset of headlines (Strapparava & Mihalcea, 2007), constructed of four equally-sized classes and proper English. On the other hand, the dataset of election tweets (Mohammad et al., 2015), which is composed of highly unbalanced classes and considerable language noise, yields the lowest improvement.

Table 3 reports sensitivity and specificity scores as an additional robustness check. The results confirm our findings, i. e., we witness the largest performance improvements for datasets with less noise. For the election tweet dataset (Mohammad et al., 2015), the best bidirectional LSTM model achieves a sensitivity of 56.9, while the best baseline achieves a slightly better score of 57.1. We can significantly strengthen our results for this challenging dataset by applying transfer learning, as reported in section 4.3.

<table><tr><td rowspan="2">Dataset</td><td colspan="2">Baseline: traditional machine learning</td><td colspan="2">Deep learning</td><td colspan="2">Pre-trained word embeddings</td></tr><tr><td>Random forest</td><td>SVM</td><td>LSTM</td><td>BiLSTM</td><td>LSTM</td><td>BiLSTM</td></tr><tr><td>Literary tales (Alm, 2008)</td><td>63.2</td><td>64.7</td><td>63.0(-2.6%)</td><td>61.6(-4.8%)</td><td>67.9(+4.9%)</td><td>68.8(+6.3%)</td></tr><tr><td>Election tweets (Mohammad et al., 2015)</td><td>55.0</td><td>56.8</td><td>54.5(-4.0%)</td><td>54.8(-3.5%)</td><td>55.8(-1.8%)</td><td>57.7(+1.6%)</td></tr><tr><td>ISEAR (Wallbott &amp; Scherer, 1986), i.e., self-reported experiences</td><td>47.0</td><td>54.3</td><td>54.2(-0.2%)</td><td>55.8(+1.5%)</td><td>57.7(+6.3%)</td><td>56.9(+4.8%)</td></tr><tr><td>Headlines (Strapparava &amp; Mihalcea, 2007)</td><td>35.8</td><td>35.3</td><td>39.2(+9.5%)</td><td>39.8(+11.2%)</td><td>41.7(+16.5%)</td><td>44.1(+23.2%)</td></tr><tr><td>General tweets (Mohammad et al., 2018)</td><td>52.6</td><td>54.2</td><td>56.0(+3.3%)</td><td>55.5(+2.4%)</td><td>57.7(+6.5%)</td><td>58.2(+7.4%)</td></tr></table>

Table 2: Holistic comparison of traditional machine learning and recurrent neural networks (with optional GloVe word embeddings) for afective computing, that is, models as classification tasks. Here the outcome variable represents a single label according to predefined categorical emotion model. Accordingly, the perfor mance is measured based on the F1-score; i. e., the higher the better. All models that outperform the best baseline model are highlighted in bold. The percentage changes refer to the relative improvement over the best baseline from traditional machine learning.

<table><tr><td rowspan="3">Dataset</td><td colspan="4">Baseline: traditional machine learning</td><td colspan="4">Deep learning</td><td colspan="4">Pre-trained word embeddings</td></tr><tr><td colspan="2">Random forest</td><td colspan="2">SVM</td><td colspan="2">LSTM</td><td colspan="2">BiLSTM</td><td colspan="2">LSTM</td><td colspan="2">BiLSTM</td></tr><tr><td>Sens.</td><td>Spec.</td><td>Sens.</td><td>Spec.</td><td>Sens.</td><td>Spec.</td><td>Sens.</td><td>Spec.</td><td>Sens.</td><td>Spec.</td><td>Sens.</td><td>Spec.</td></tr><tr><td>Literary tales (Alm, 2008)</td><td>64.0</td><td>87.2</td><td>66.1</td><td>87.4</td><td>63.1</td><td>88.8</td><td>62.0</td><td>88.8</td><td>68.4</td><td>90.6</td><td>68.2</td><td>91.4</td></tr><tr><td>Election tweets (Mohammad et al., 2015)</td><td>53.8</td><td>79.2</td><td>57.1</td><td>78.7</td><td>52.3</td><td>84.7</td><td>52.3</td><td>84.9</td><td>54.0</td><td>83.5</td><td>56.9</td><td>82.9</td></tr><tr><td>ISEAR (Wallbott &amp; Scherer, 1986), i.e., self-reported experiences</td><td>45.0</td><td>90.3</td><td>53.7</td><td>92.4</td><td>54.2</td><td>92.3</td><td>56.0</td><td>92.6</td><td>57.6</td><td>93.0</td><td>57.0</td><td>92.8</td></tr><tr><td>Headlines (Strapparava &amp; Mihalcea, 2007)</td><td>35.6</td><td>86.2</td><td>35.0</td><td>84.2</td><td>39.8</td><td>83.8</td><td>40.3</td><td>84.1</td><td>40.0</td><td>86.6</td><td>44.3</td><td>85.6</td></tr><tr><td>General tweets (Mohammad et al., 2018)</td><td>52.4</td><td>84.1</td><td>53.9</td><td>84.6</td><td>55.6</td><td>85.2</td><td>55.1</td><td>85.0</td><td>57.3</td><td>85.8</td><td>57.9</td><td>85.9</td></tr></table>

Table 3: Additional comparison of sensitivity and specificity. The highest values for both are highlighted for each dataset.

## 4.2. Regression according to dimensional afect models

Depending on the afect theory, one can also model emotional categories according to dimensional ratings and, as a result, this is implemented as a regression task, where the intensity of emotional states is predicted. We choose the same baselines as in the previous experiments and compare them to deep neural networks. All models are evaluated based on the mean squared error (MSE).

Table 4 reports our results. These show a consistent improvement of up to 11.6 % as a result of using deep learning as compared to traditional machine learning. Similar to the classification task, our findings identify the BiLSTM with pre-trained word embeddings as the superior method in all seven experiments. We further note that the BiLSTM appears to outperform the unidirectional LSTM in all experiments. The relative performance increases

vary between the diferent afective dimensions.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">Scale</td><td colspan="2">Baseline: Traditional machine learning</td><td colspan="2">Deep learning</td><td colspan="2">Pre-trained word embeddings</td></tr><tr><td>Random forest</td><td>SVM</td><td>LSTM</td><td>BiLSTM</td><td>LSTM</td><td>BiLSTM</td></tr><tr><td>Headlines (Strapparava &amp; Mihalcea, 2007)Valence</td><td>-100...100</td><td>1906.0</td><td>1927.3</td><td>1870.9(-1.8%)</td><td>1896.3(-0.5%)</td><td>1792.7(-5.9%)</td><td>1791.2(-6.0%)</td></tr><tr><td>Facebook posts (Preotius-Pietro et al., 2016)Valence</td><td>0...10</td><td>1.030</td><td>0.951</td><td>1.007(+5.9%)</td><td>0.990(+4.1%)</td><td>0.911(-4.2%)</td><td>0.901(-5.2%)</td></tr><tr><td>Arousal</td><td>0...10</td><td>3.960</td><td>3.616</td><td>3.519(-2.7%)</td><td>3.550(-1.8%)</td><td>3.379(-6.6%)</td><td>3.346(-7.5%)</td></tr><tr><td>General tweets (Mohammad et al., 2018)Anger</td><td>0...1</td><td>0.0314</td><td>0.0323</td><td>0.0330(+5.1%)</td><td>0.0330(+5.1%)</td><td>0.0284(-9.5%)</td><td>0.0281(-10.5%)</td></tr><tr><td>Fear</td><td>0...1</td><td>0.0245</td><td>0.0226</td><td>0.0238(+5.3%)</td><td>0.0230(+1.8%)</td><td>0.0224(-0.9%)</td><td>0.0222(-1.8%)</td></tr><tr><td>Joy</td><td>0...1</td><td>0.0339</td><td>0.0294</td><td>0.0277(-5.8%)</td><td>0.0275(-6.5%)</td><td>0.0262(-10.9%)</td><td>0.0260(-11.6%)</td></tr><tr><td>Sadness</td><td>0...1</td><td>0.0294</td><td>0.0274</td><td>0.0281(+2.5%)</td><td>0.0268(-2.1%)</td><td>0.0246(-10.2%)</td><td>0.0243(-11.3%)</td></tr></table>

Table 4: Holistic comparison of traditional machine learning and recurrent neural networks (with optional GloVe word embeddings) for afective computing, that is, models as regression tasks. Here the outcome variable represents the intensity according to predefined afective dimensions. Accordingly, the performance is measured based on the mean squared error (MSE); i. e., the lower the better. The best-performing model for each dataset is highlighted in bold. The percentage changes refer to the relative improvement over the best baseline from traditional machine learning. We point out that the first task exhibits higher errors due to the diferent scale of the outcome variable.

## 4.3. Transfer learning via sent2afect

The previous experiments revealed consistent improvements through the use of deep learning; however, several benchmark datasets entail only a fairly small set of samples, which could impede the training of deep neural networks. For instance, the dataset of inferring emotions from election tweets (Mohammad et al., 2015) comprises only 1,646 samples for training. A potential remedy is utilizing large-scale datasets from other tasks and then inducing knowledge to afective computing. More precisely, we now experiment with the potential performance improvements to be gained by additionally applying our transfer learning approach “sent2afect”. By inducing network parameters from sentiment analysis to afective computing, we benefit from the considerably larger datasets that are used in sentiment analysis, since the sentiment dataset consists of about 100,000 tweets that are associated with positive and negative labels.

Table 5 compares our transfer learning approach against two baselines: (i) a na¨ıve BiL-STM and (ii) the transfer learning approach of Kraus & Feuerriegel (2017), where only GloVe word-embeddings are pre-trained. We choose the election tweets (Mohammad et al., 2015) and general tweets (Mohammad et al., 2018) datasets to demonstrate how we can transfer the knowledge from thousands of sentiment-labeled tweets to the task of emotion recognition. Furthermore, na¨ıve deep learning alone yields an inferior performance. While the BiLSTM with pre-trained word embeddings has previously represented the best-performing architecture, we still observe that transfer learning yields additional improvements. These amount to 6.6 % for the election tweets and 5.6 % for the general tweets. Evidently, transfer learning can successfully benefit from the large-scale dataset for sentiment analysis and, as a result, optimizes the neuron weights such that these find a more generalizable representation of emotion-laden materials.

<table><tr><td>Dataset</td><td>Naïve BiLSTM</td><td>BiLSTM (pre-trained embeddings)</td><td>Transfer learning sent2affect</td></tr><tr><td rowspan="2">Election tweets (Mohammad et al., 2015)</td><td>54.8</td><td>57.7</td><td>58.4</td></tr><tr><td></td><td>(+5.3%)</td><td>(+6.6%)</td></tr><tr><td rowspan="2">General tweets (Mohammad et al., 2018)</td><td>55.5</td><td>58.2</td><td>58.6</td></tr><tr><td></td><td>(+4.9%)</td><td>(+5.6%)</td></tr></table>

Table 5: The numerical results show that transfer learning can yield additional performance improvements based on an inductive knowledge transfer across tasks (as opposed to the conventional strategy across datasets). In our sent2afect method, the neural networks are first trained on a sentiment analysis dataset in order to learn an abstract representation of emotion-laden text, while the final dense layer is subsequently replaced and fine-tuned using the task-specific dataset. Performance is measured in terms of F1-score; i. e., the higher the better. The best-performing model for each dataset is highlighted in bold. The percentage changes refer to the relative improvement over the best baseline without transfer learning.

## 5. Discussion

## 5.1. Comparison

Our series of experiments reveals considerable and consistent performance improvements over default implementations of deep learning through the use of our customized networks.

This points towards the need to customize deep neural networks according to the unique characteristics of the underlying task.

In this paper, we refrained from evaluating performance on the basis of a single dataset and, instead, perform a holistic analysis, demonstrating that our customized networks outperformed the baselines in all experiments by up to 23.2 %. Interestingly, our proposed modifications, such as with regard to regularization, were even able to learn the underlying relationships from the rather small datasets of merely 1,000 observations. However, we observe an overall pattern whereby the performance improvements tend to be higher when there is less language noise. In addition, we observe further improvement through the use of word embeddings, as these reduce the high-dimensional vectors with terms as one-hot encoding to lower-dimensional spaces.

In the majority of experiments, the superior results stem from using a bidirectional LSTM as compared to a simple LSTM. We note that not only traditional machine learning but all network architectures required extensive training in order to ensure that embeddings and dropout layer functioned well together. Finally, the task of emotion recognition in afective computing is related to sentiment analysis, which infers a positive/negative polarity from linguistic materials. Hence, it is interesting to study whether one can further improve performance through an inductive transfer of knowledge from a diferent task (rather than a diferent dataset), despite the distinct objective, linguistic style, and annotation scheme. As a result, our sent2afect implementation of transfer learning establishes additional improvements of up to 6.6 %.

## 5.2. Deep-learning-based afect computing for decision support in social media

As a proof of concept, we utilize our bidirectional LSTM to support the notoriously dificult task of classifying news into factual and non-factual. This demonstrates how afective computing can eventually facilitate decision support for social media platforms seeking to recognize and prevent the spread of “false news”. We utilize the dataset of Shu et al. (2017) and predict whether a news item is factual. The prediction model is given by a logistic regression that is fed with the output of our afect prediction layer. Our approach achieves an accuracy of 53.2 % when using the afective dimensions of the headlines and 58.1 % when using separate afective dimensions of both headlines and content. This almost matches the reported baseline performance from prior research (Rubin et al., 2015), where a content-based classifier was used to detect fabricated news items. However, we refrain from learning towards certain linguistic devices or individual stories. Instead, our approach ensures generalizability by identifying highly polarizing language as part of its decision support.

## 5.3. Further use cases of deep-learning-based afective computing for better decision support

Text-based afective computing drives decision support in a variety of application areas in which understanding the emotional state of individuals is crucial. Table 6 provides an overview of interesting examples from research, as well as actual use cases from businesses. This table is intended to give an overview of areas where decision support could potentially be improved through the use of our deep-learning-based models for afective computing. It is evident that afective computing facilitates decision-making in all operational areas of businesses, such as management, marketing, and finance. For instance, firms can infer the perceived emotion of customers from online product reviews and base managerial decisions on this data in order to support product development (Ullah et al., 2016) and advertising (Ang & Low, 2000). In a financial context, emotional media content has been identified as a driver in the decision-making of investors (Pr¨ollochs et al., 2016), which can thus serve as a decision rule for stock investments (Gilbert & Karahalios, 2010).

Beyond that, deep learning for emotion recognition could also facilitate public decision support with respect to politics and even education, as well as healthcare for individuals. For instance, afective computing can infer emotion concerning personal health conditions (Anderson & Agarwal, 2011; Desmet & Hoste, 2013; Greaves et al., 2013; van der Zanden et al., 2014) and during learning processes (Rodriguez et al., 2012). Notably, all of the prior references engage in afect-aware decision-making, but have not yet evaluated the use of deep learning.

## 5.4. Implications for management and practice

Even though deep learning has gained considerable traction lately, its use cases outside of academia remain scarce. A possible reason is located in the complexity of operationalizing deep neural networks. While recurrent architectures have previously been applied to sentiment analysis, the task of emotion recognition requires several modifications in order to obtain a better-than-random performance. This specifically applies to the proposed bidirectional processing of texts, regularization, and loss functions that can handle highly imbalanced datasets. As a direct recommendation for use cases of afective computing, we propose a shift towards customized network architectures, even for fairly small datasets of around 1,000 training samples, as in our case. Altogether, this highlights the need for a thorough understanding by practitioners of the available tools in order to benefit from deep learning.

Afective computing for linguistic materials yields new opportunities for business models and consumer-centered services (Li et al., 2011; Doucet et al., 2012; Dai et al., 2015; Yin et al., 2014). Detecting and subsequently responding to the emotional states of users, customers, patients, and employees has the potential to significantly accelerate and improve management processes and optimize human-computer interactions. Here text remains a critical form of communication, while attempts have also been made to apply afective computing to speech or other multimodal input (Calvo & D’Mello, 2010), including visual data (Chen et al., 2017; El Ayadi et al., 2011; Shan et al., 2009). Management should assess potential use cases in critical areas of operations from their own organizations. Our overview in Section 2 provides illustrative examples, while further applications are likely to arise with recent methodological innovations.

## 5.5. Implications for research

The process of improving the performance of afective computing would benefit considerably from a rigorous suite of baseline datasets. In the status quo, a variety of datasets with distinct goals and purposes is commonly used for benchmarking methodological innovations for afective computing. For instance, our literature survey identified four diferent strategies for annotating, including simple labels, multi-class labels, and numerical scores. Moreover, the set of afective dimensions varied between two (i. e., valence, arousal without explicitly naming emotions) and a set of 8 emotions (e. g., anger, disgust, surprise). However, this directly links to challenges concerning comparability and generalizability. In this sense, a network architecture that has been found efective for one annotation scheme might not work out for other datasets. On top of that, diferent labels prohibit transfer learning and thus impede performance. We therefore suggest a standardized approach to annotations.

# ACCEPTED MANUSCRIPT

According to our literature review, datasets for afective computing vary in size from 1,000 instances to 7,902, and yet all of them remain fairly small when compared to other applications of deep learning. As a result, this is known to limit the performance of bidirectional LSTMs and other deep neural network architectures, which generally require large-scale datasets. For instance, datasets for sentiment analysis, such as the one used for our transfer learning approach, consist of up to 100,000 labeled samples. Future research should thus aim at creating larger datasets in order to enable the efective exploitation of deep learning.

## 6. Conclusion

Afective computing allows one to infer individual and collective emotional states from textual data and thus ofers an anthropomorphic path for the provision of decision support. Even though deep learning has yielded considerable performance improvements for a variety of tasks in natural language processing, na¨ıve network architectures struggle with the task of emotion recognition. As a remedy, several modifications are presented in this paper: namely, bidirectional processing, dropout regularization, and weighted loss functions in order to cope with imbalances in the datasets.

Our computational experiments span categorical and dimensional emotion models, which require tailored algorithmic implementations involving, e. g., multi-class classification, as well as regression tasks and transfer learning. Our results show that pre-trained bidrectional LSTMs consistently outperform the baseline models from traditional machine learning. The performance improvements can even range up to 23.2 % in F1-score for classification and 11.6 % in MSE for regression. We propose sent2afect, a customized strategy of transfer learning that draws upon the diferent task of sentiment analysis (as opposed to diferent datasets, as is usually the case), which is responsible for further performance improvements of between 5.6 % and 6.6 %.

## Acknowledgments

The authors gratefully acknowledge the financial support for Suzana Ili´c from Prof. Kotaro Nakayama and Prof. Yutaka Matsuo, Graduate School of Engineering, University of Tokyo, Japan.

<table><tr><td>Domain</td><td>Application</td><td>Details</td><td>Reference</td></tr><tr><td rowspan="4">Management &amp; marketing</td><td>Strategy development</td><td>Identification of perceived emotion towards products as a lever for product development</td><td>(Ullah et al., 2016)</td></tr><tr><td>Brand management</td><td>Emotion analysis of firm-related tweets for reputation management</td><td>(Al-Hajjar &amp; Syed, 2015)</td></tr><tr><td>Churn prediction</td><td>Emotions within customer responses to marketing content serve as a predictor of purchase intention</td><td>(Ang &amp; Low, 2000)</td></tr><tr><td>Preference learning</td><td>Examination of consumer behavior and emotional attitudes related to product preferences</td><td>(Chitturi et al., 2007)</td></tr><tr><td rowspan="2">User interaction</td><td>Chatbots</td><td>Regulation of emotion of stranded passengers through chatbots</td><td>(Medeiros &amp; van der Wal, 2017)</td></tr><tr><td>Social networks</td><td>Measurement of relationship strength in social networks with affective language as an indicator of emotional closeness</td><td>(Marsden &amp; Campbell, 2012)</td></tr><tr><td rowspan="2">Finance</td><td>Investment decision</td><td>Prediction of stock market movements based on emotionally-charged content</td><td>(Gilbert &amp; Karahalios, 2010)</td></tr><tr><td>Economic growth indicator</td><td>Excitement and anxiety in media articles as indicators of financial stability and economic shifts</td><td>(Ormerod et al., 2015)</td></tr><tr><td rowspan="2">Politics</td><td>Political participation</td><td>Emotion recognition for political participation and mobilization</td><td>(Valentino et al., 2011)</td></tr><tr><td>Public monitoring</td><td>Hate speech detection on Twitter</td><td>(Burnap &amp; Williams, 2015)</td></tr><tr><td rowspan="5">Health</td><td>Depression treatment</td><td>Analysis of emotional content for recognizing depressive symptoms in chat transcripts</td><td>(van der Zanden et al., 2014)</td></tr><tr><td>Suicide prevention</td><td>Early warning of suicide-related emotions in written notes</td><td>(Desmet &amp; Hoste, 2013)</td></tr><tr><td>Public health forecast</td><td>Prediction of mortality from heart disease based on emotions expressed on Twitter</td><td>(Eichstaedt et al., 2015)</td></tr><tr><td>Diagnosis</td><td>Emotional states as predictors of the willingness to disclose personal health information</td><td>(Anderson &amp; Agarwal, 2011)</td></tr><tr><td>Diagnosis</td><td>Social media emotion analysis for detecting poor healthcare conditions</td><td>(Greaves et al., 2013)</td></tr><tr><td>Education</td><td>E-learning</td><td>Improvement of learning experience through classifying and regulating e-learners&#x27; emotions</td><td>(Rodriguez et al., 2012)</td></tr></table>

Table 6: Selected use cases in research and industry where deep-learning-based afective computing could help in improving decision support. Importantly, these works still rely upon traditional machine learning for emotion recognition and thus present viable opportunities for the use of our proposed deep learning framework.

## References

Agrawal, A., & An, A. (2012). Unsupervised emotion detection from text using semantic and syntactic relations. In International Conference on Web Intelligence and Intelligent Agent Technology.

Al-Hajjar, D., & Syed, A. Z. (2015). Applying sentiment and emotion analysis on brand tweets for digital marketing. In Applied Electrical Engineering and Computing Technologies. IEEE.

Alm, C. O., Roth, D., & Sproat, R. (2005). Emotions from text. In Human Language Technology and Empirical Methods in Natural Language Processing (pp. 579–586).

Alm, E. C. O. (2008). Afect in Text and Speech. Ph.D. thesis University of Illinois at Urbana-Champaign Illinois.

Anderson, C. L., & Agarwal, R. (2011). The digitization of healthcare: Boundary risks, emotion, and consumer willingness to disclose personal health information. Information Systems Research, 22 , 469–490.

Ang, S. H., & Low, S. Y. M. (2000). Exploring the dimensions of ad creativity. Psychology & Marketing, 17 , 835–854.

Averill, J. R. (1980). A constructivist view of emotion. Theories of Emotion, (pp. 305–339).

Balahur, A., Hermida, J. M., & Montoyo, A. (2012). Detecting implicit expressions of emotion in text: A comparative analysis. Decision Support Systems, 53 , 742–753.

Bandhakavi, A., Wiratunga, N., Padmanabhan, D., & Massie, S. (2017). Lexicon based feature extraction for emotion text classification. Pattern Recognition Letters, 93 , 133– 142.

Burnap, P., & Williams, M. L. (2015). Cyber hate speech on Twitter: An application of machine classification and statistical modeling for policy and decision making. Policy & Internet, 7 , 223–242.

Calvo, R. A., & D’Mello, S. (2010). Afect detection: An interdisciplinary review of models, methods, and their applications. IEEE Transactions on Afective Computing, 1 , 18–37.

Cambria, E., Livingstone, A., & Hussain, A. (2012). The hourglass of emotions. In Cognitive Behavioural Systems (pp. 144–157). Berlin, Heidelberg: Springer volume 7403.

Chafar, S., & Inkpen, D. (2011). Using a heterogeneous dataset for emotion analysis in text. In Advances in Artificial Intelligence (pp. 62–67).

Chatzakou, D., Vakali, A., & Kafetsios, K. (2017). Detecting variation of emotions in online

activities. Expert Systems with Applications, 89 , 318–332.

Chen, Y.-L., Chang, C.-L., & Yeh, C.-S. (2017). Emotion classification of YouTube videos. Decision Support Systems, 101 , 40–50.

Chitturi, R., Raghunathan, R., & Mahajan, V. (2007). Form versus function: How the intensities of specific emotions evoked in functional versus hedonic trade-ofs mediate product preferences. Journal of Marketing Research, 44 , 702–714.

D. Munezero, M., Montero, C. S., Sutinen, E., & Pajunen, J. (2014). Are they diferent? Afect, feeling, emotion, sentiment, and opinion detection in text. IEEE Transactions on Afective Computing, 5 , 101–111.

Dai, H., Luo, X., Liao, Q., & Cao, M. (2015). Explaining consumer satisfaction of services: The role of innovativeness and emotion in an electronic mediated environment. Decision Support Systems, 70 , 97–106.

Danisman, T., & Alpkocak, A. (2008). Feeler: Emotion classification of text using vector space model. In Communication, Interaction and Social Intelligence. volume 1.

Derakshan, N., & Eysenck, M. W. (2010). Introduction to the special issue: Emotional states, attention, and working memory. Cognition & Emotion, 24 , 189–199.

Desmet, B., & Hoste, V. (2013). Emotion detection in suicide notes. Expert Systems with Applications, 40 , 6351–6358.

Dolan, R. J. (2002). Emotion, cognition, and behavior. Science, 298 , 1191–1194.

Doucet, L., Thatcher, S. M., & Thatcher, M. E. (2012). The efects of positive afect and personal information search on outcomes in call centers: An empirical study. Decision Support Systems, 52 , 664–673.

Eichstaedt, J. C., Schwartz, H. A., Kern, M. L., Park, G., Labarthe, D. R., Merchant, R. M., Jha, S., Agrawal, M., Dziurzynski, L. A., Sap, M., Weeg, C., Larson, E. E., Ungar, L. H., & Seligman, M. E. P. (2015). Psychological language on Twitter predicts county-level heart disease mortality. Psychological Science, 26 , 159–169.

Ekman, P., Friesen, W. V., O’Sullivan, M., Chan, A., Diacoyanni-Tarlatzis, I., Heider, K., Krause, R., LeCompte, W. A., Pitcairn, T., & Ricci-Bitti, P. E. (1987). Universals and cultural diferences in the judgments of facial expressions of emotion. Journal of Personality and Social Psychology, 53 , 712–717.

El Ayadi, M., Kamel, M. S., & Karray, F. (2011). Survey on speech emotion recognition: Features, classification schemes, and databases. Pattern Recognition, 44 , 572–587.

Evermann, J., Rehse, J.-R., & Fettke, P. (2017). Predicting process behaviour using deep learning. Decision Support Systems, 100 , 129–140.

Felbo, B., Mislove, A., Søgaard, A., Rahwan, I., & Lehmann, S. (2017). Using millions of emoji occurrences to learn any-domain representations for detecting sentiment, emotion and sarcasm. In Conference on Empirical Methods in Natural Language Processing (pp. 1615–1625).

Frijda, N. H. (1988). The laws of emotion. American Psychologist, 43 , 349–358.

Gilbert, E., & Karahalios, K. (2010). Widespread worry and the stock market. In AAAI Conference on Web and Social Media (pp. 59–65).

Goel, P., Kulshreshtha, D., Jain, P., & Shukla, K. K. (2017). Prayas at EmoInt 2017: An ensemble of deep neural architectures for emotion intensity prediction in tweets. In Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (pp. 58–65).

Greaves, F., Ramirez-Cano, D., Millett, C., Darzi, A., & Donaldson, L. (2013). Harnessing the cloud of patient experience: Using social media to detect poor quality healthcare. BMJ Quality & Safety, 22 , 251–255.

Greene, J., & Haidt, J. (2002). How (and where) does moral judgment work? Trends in Cognitive Sciences, 6 , 517–523.

Gupta, U., Chatterjee, A., Srikanth, R., & Agrawal, P. (2017). A sentiment-andsemantics-based approach for emotion detection in textual conversations. arXiv preprint arXiv:1707.06996 , .

Hogenboom, F., Frasincar, F., Kaymak, U., de Jong, F., & Caron, E. (2016). A survey of event extraction methods from text for decision support systems. Decision Support Systems, 85 , 12–22.

Hsu, C.-W., Chang, C.-C., & Lin, C.-J. (2003). A practical guide to support vector classification. Tech. rep. Department of Computer Science, National Taiwan University, .

Izard, C. E. (1992). Basic emotions, relations among emotions, and emotion-cognition relations. Psychological Review, 99 , 561–565.

Izard, C. E. (2009). Emotion theory and research: Highlights, unanswered questions, and emerging issues. Annual Review of Psychology, 60 , 1–25.

King, G., & Zeng, L. (2001). Logistic regression in rare events data. Political analysis, 9 , 137–163.

## ACCEPTED MANUSCRIPT

Kratzwald, B., & Feuerriegel, S. (2018). Putting question-answering systems into practice: Transfer learning for eficient domain customization. arXiv preprint arXiv:1804.07097 , .

Kraus, M., & Feuerriegel, S. (2017). Decision support from financial disclosures with deep neural networks and transfer learning. Decision Support Systems, 104 , 38–48.

Kraus, M., Feuerriegel, S., & Oztekin, A. (2018). Deep learning in business analytics and operations research: Models, applications and managerial implications. arXiv preprint arXiv:1806.10897 , .

Lakomkin, E., Bothe, C., & Wermter, S. (2017). Gradascent at EmoInt 2017: Character and word level recurrent neural network models for tweet emotion intensity detection. In Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (pp. 169–174).

Li, H., Sarathy, R., & Xu, H. (2011). The role of afect and cognition on online consumers’ decision to disclose personal information to unfamiliar online vendors. Decision Support Systems, 51 , 434–445.

Li, M., Lu, Q., Long, Y., & Gui, L. (2017). Inferring afective meanings of words from word embedding. IEEE Transactions on Afective Computing, 8 , 443–456.

Lux, E., Hawlitschek, F., Adam, M. T. P., & Pfeifer, J. (2015). Using live biofeedback for decision support: Investigating influences of emotion regulation in financial decision making. European Conference on Information Systems, .

Mahmoudi, N., Docherty, P., & Moscato, P. (2018). Deep neural networks understand investors better. Decision Support Systems, 112 , 23–34.

Manning, C. D., & Sch¨utze, H. (1999). Foundations of statistical natural language processing. Cambridge, MA: MIT Press.

Marsden, P. V., & Campbell, K. E. (2012). Reflections on conceptualizing and measuring tie strength. Social Forces, 91 , 17–23.

Medeiros, L., & van der Wal, C. N. (2017). An agent-based model predicting group emotion and misbehaviours in stranded passengers. In Portuguese Conference on Artificial Intelligence (pp. 28–40).

Meisheri, H., Saha, R., Sinha, P., & Dey, L. (2017). Textmining at EmoInt 2017: A deep learning approach to sentiment intensity scoring of english tweets. In Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (pp. 193–199).

Mohammad, S. M. (2012). From once upon a time to happily ever after: Tracking emotions in mail and books. Decision Support Systems, 53 , 730–741.

Mohammad, S. M., Bravo-Marquez, F., Salameh, M., & Kiritchenko, S. (2018). SemEval-2018 task 1: Afect in tweets. In Proceedings of International Workshop on Semantic Evaluation.

Mohammad, S. M., & Turney, P. D. (2013). Crowdsourcing a word-emotion association lexicon. Computational Intelligence, 29 , 436–465.

Mohammad, S. M., Zhu, X., Kiritchenko, S., & Martin, J. (2015). Sentiment, emotion, purpose, and style in electoral tweets. Information Processing & Management, 51 , 480– 499.

Mou, L., Meng, Z., Yan, R., Li, G., Xu, Y., Zhang, L., & Jin, Z. (2016). How transferable are neural networks in nlp applications? In Conference on Empirical Methods in Natural Language Processing (pp. 479–489).

Oatley, K., Parrott, W. G., Smith, C., & Watts, F. (2011). Cognition and emotion over twenty-five years. Cognition & Emotion, 25 , 1341–1348.

Ormerod, P., Nyman, R., & Tuckett, D. (2015). Measuring financial sentiment to predict financial instability: A new approach based on text analysis. arXiv preprint arXiv:1508.05357 , .

Pan, S. J., & Yang, Q. (2010). A survey on transfer learning. IEEE Transactions on Knowledge and Data Engineering, 22 , 1345–1359.

Pang, B., & Lee, L. (2008). Opinion mining and sentiment analysis. Foundations and Trends in Information Retrieval, 2 , 1–135.

Picard, R. W. (1995). Afective computing. Perceptual Computing Section, Media Laboratory, Massachusetts Institute of Technology, .

Picard, R. W. (1997). Afective computing. Cambridge, MA: MIT Press.

Plutchik, R. (2001). The nature of emotions: Human emotions have deep evolutionary roots. American Scientist, 89 , 344–350.

Poria, S., Cambria, E., Bajpai, R., & Hussain, A. (2017). A review of afective computing: From unimodal analysis to multimodal fusion. Information Fusion, 37 , 98–125.

Poria, S., Gelbukh, A., Cambria, E., Hussain, A., & Huang, G.-B. (2014). Emosenticspace: A novel framework for afective common-sense reasoning. Knowledge-Based Systems, 69 , 108–123.

Potapova, R., & Gordeev, D. (2016). Detecting state of aggression in sentences using CNN. Lecture Notes in Computer Science, 9811 , 240–245.

## ACCEPTED MANUSCRIPT

Preotiuc-Pietro, D., Schwartz, H. A., Park, G., Eichstaedt, J., Kern, M., Ungar, L., & Shulman, E. (2016). Modelling valence and arousal in facebook posts. In Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (pp. 9– 15).

Pr¨ollochs, N., Feuerriegel, S., & Neumann, D. (2016). Is human information processing afected by emotional content? Understanding the role of facts and emotions in the stock market. International Conference on Information Systems, .

Ribeiro, F. N., Ara´ujo, M., Gon¸calves, P., Andr´e Gon¸calves, M., & Benevenuto, F. (2016). Sentibench: a benchmark comparison of state-of-the-practice sentiment analysis methods. EPJ Data Science, 5 .

Rodriguez, P., Ortigosa, A., & Carro, R. M. (2012). Extracting emotions from texts in elearning environments. In International Conference on Complex, Intelligent, and Software Intensive Systems (pp. 887–892). IEEE.

Rubin, V. L., Conroy, N. J., & Chen, Y. (2015). Towards news verification: Deception detection methods for news discourse. In Proceedings of the Hawaii International Conference on System Sciences (HICSS48) Symposium on Rapid Screening Technologies, Deception Detection and Credibility Assessment Symposium, January (pp. 5–8).

Russell, J. A. (1980). A circumplex model of afect. Journal of Personality and Social Psychology, 39 , 1161–1178.

Schwarz, N. (2000). Emotion, cognition, and decision making. Cognition & Emotion, 14 , 433–440.

Shan, C., Gong, S., & McOwan, P. W. (2009). Facial expression recognition based on local binary patterns: A comprehensive study. Image and Vision Computing, 27 , 803–816.

Shu, K., Sliva, A., Wang, S., Tang, J., & Liu, H. (2017). Fake news detection on social media: A data mining perspective. ACM SIGKDD Explorations Newsletter , 19 , 22–36.

Spiro, E., & Ahn, Y.-Y. (2016). Social Informatics. Cham: Springer.

Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). Dropout: A simple way to prevent neural networks from overfitting. Journal of Machine Learning Research, 15 , 1929–1958.

Strapparava, C., & Mihalcea, R. (2007). SemEval-2007 task 14: Afective text. In Workshop on Semantic Evaluations (pp. 70–74).

Strapparava, C., & Valitutti, A. (2004). WordNet-Afect: An afective extension of WordNet. In Conference on Language Resources and Evaluation (pp. 1083–1086).

Tao, Jianhua and Tan, Tieniu and Picard, Rosalind W (2011). Afective computing and intelligent interaction. Heidelberg: Springer.

Tausczik, Y. R., & Pennebaker, J. W. (2010). The psychological meaning of words: Liwc and computerized text analysis methods. Journal of Language and Social Psychology, 29 , 24–54.

Tomkins, S. (1963). Afect imagery consciousness: Volume II: The negative afects. New York, NY: Springer.

Tomkins, S. S. (1962). Afect, Imagery, and Consciousness, Vol. 1: The Positive Afects volume 139. New York, NY: Springer.

Ullah, R., Amblee, N., Kim, W., & Lee, H. (2016). From valence to emotions: Exploring the distribution of emotions in online product reviews. Decision Support Systems, 81 , 41–53.

Valentino, N. A., Brader, T., Groenendyk, E. W., Gregorowicz, K., & Hutchings, V. L. (2011). Election night’s alright for fighting: The role of emotions in political participation. The Journal of Politics, 73 , 156–170.

van der Zanden, R., Curie, K., van Londen, M., Kramer, J., Steen, G., & Cuijpers, P. (2014). Web-based depression treatment: Associations of clients’ word use with adherence and outcome. Journal of Afective Disorders, 160 , 10–13.

Wallbott, H. G., & Scherer, K. R. (1986). How universal and specific is emotional experience? Evidence from 27 countries on five continents. Social Science Information, 25 , 763–795.

Yadollahi, A., Shahraki, A. G., & Zaiane, O. R. (2017). Current state of text sentiment analysis from opinion to emotion mining. ACM Computing Surveys, 50 , 1–33.

Yin, D., Bond, S. D., & Zhang, H. (2014). Anxious or angry? Efects of discrete emotions on the perceived helpfulness of online reviews. MIS Quarterly, 38 , 539–560.

Zhang, Y., Yuan, H., Wang, J., & Zhang, X. (2017). YNU-HPCC at EmoInt 2017: Using a CNN-LSTM model for sentiment intensity prediction. In Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (pp. 200–204).

# ACCEPTED MANUSCRIPT

## Bernhard Kratzwald

Bernhard Kratzwald is a PhD student at the Chair of Management Information Systems at ETH Zurich. Previously, he has completed his Bachelor’s and Master’s studies in computer science at ETH Zurich and the Technical University of Vienna. His research focuses on applications of machine learning and statistics for natural language understanding, including but not limited to affective computing, question answer systems and chatbots.

![](/api/attachments/AWXWRDQR/fulltext/images/772e487b968fb5b6e4752ea1274adaf41cfac89cfcc07fb4be610dbd47bddf32.jpg)

## Suzana Illic

Suzana Illic is a visiting researcher at the National Institute of Informatics, Tokyo. Previously she completed her Bachelor’s and Master’s studies in Applied Linguistics at Leopold-Franzens University Innsbruck. Her research focus on computational linguistics including sentiment analysis, affective computing and sarcasm detection in natural language.

![](/api/attachments/AWXWRDQR/fulltext/images/17725df42a12373b99bec7c44c453dcd2ec402288885fa7f7365e55a9ba5b1e7.jpg)

## Mathias Kraus

Mathias Kraus is a PhD student at the Chair of Management Information Systems at ETH Zurich. Previously, he has completed his Bachelor’s and Master’s studies in computer science and mathematics at the Karlsruhe Institute of Technology. His research focuses on applications of machine learning and statistics for data analytics, with a focus on deep neural networks and Bayesian inference.

![](/api/attachments/AWXWRDQR/fulltext/images/5c38576dcf7693de12115e32e01ad6696d1f579876892d4b276c30b09a5b6d18.jpg)

## Stefan Feuerriegel

Stefan Feuerriegel is an assistant professor for management information systems at ETH Zurich. His research focuses on cognitive information systems and business intelligence, including text mining and sentiment analysis of financial news. Previously, he obtained his Ph.D. from the University of Freiburg where also worked as a research group leader at the Chair for Information Systems Research. He has co-authored research publications in the European Journal of

Operational Research, the European Journal of Information Systems, the Journal of Information Technology and Decision Support Systems.

![](/api/attachments/AWXWRDQR/fulltext/images/521c849d2abccafc29af0a4bc367292e6fc6fb49b571101666ff3eb06b84410b.jpg)

## Helmut Prendinger

Helmut Prendinger is a professor at the National Institute of Informatics, Tokyo, where he works in the Digital Content and Media Sciences Research Division. He carries out research in the areas of 3D Internet, cyber social simulation, data analytics, virtual agents, intelligent multimodal interfaces, and emotion/attitude recognition from text. He has published more than 200 papers in peerreviewed journals and conferences.

![](/api/attachments/AWXWRDQR/fulltext/images/beba6ee252db7676270fc055f3d49b12f9148e268a893e435deb5797c0e6c12d.jpg)

## Highlights

• Afective computing infers the emotional state of humans from text

• We propose the use of deep learning: recurrent neural networks & transfer learning

• This yields considerable improvements in predictive accuracy

• Holistic evaluation and implications for decision support are derived

![](/api/attachments/AWXWRDQR/fulltext/images/f9bf13f474618a3186ec5597c0fdab9defa68b0a54ebaaf1ea37a21cdbecb18b.jpg)  
Figure 1
