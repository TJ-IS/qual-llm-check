---
otero_id: 7274
otero_key: "UDFMVTFH"
title: "Antisocial online behavior detection using deep learning"
authors: "Elizaveta Zinovyeva; Wolfgang Karl Härdle; Stefan Lessmann"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113362"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Antisocial online behavior detection using deep learning

Elizaveta Zinovyeva<sup>a,⁎</sup>, Wolfgang Karl Härdle<sup>a,b,c,d,e</sup>, Stefan Lessmann<sup>a</sup>

![](/api/attachments/UDFMVTFH/fulltext/images/e63c4d08f36dc391ef4cf375930f1cf0b31991a99a9180f4504fcb206be8e179.jpg)

<sup>a</sup> School of Business and Economics, Humboldt-Universität zu Berlin, Berlin, Germany

<sup>b</sup> Sim Kee Boon Institute for Financial Economics, Singapore Management University, Singapore, Singapore

<sup>c</sup> W.I.S.E. - Wang Yanan Institute for Studies in Economics, Xiamen University, Fujian, China

<sup>d</sup> Faculty of Mathematics and Physics, Charles University, Prague, Czech Republic

<sup>e</sup> Department of Information Management and Finance, National Chiao Tung University, Hsinchu, Taiwan

## A R T I C L E I N F O

Keywords: Antisocial online behavior Natural language processing Text classification Deep learning Cyberbullying Attention mechanism

## A B S T R A C T

Digitalization shifts human communication to online platforms. which has many benefits but also builds up a space for antisocial online behavior (AOB) such as harassment, insult and other forms of hateful textual content. Online platforms have good reasons to monitor and moderate such content. The paper examines the viability of automatic content monitoring using deep machine learning and natural language processing (NLP). More spe cifically, we consolidate prior work in the field of antisocial online behavior detection and compare relevant approaches to recent NLP models in an empirical study. Covering important methodological advancements in NLP including bidirectional encoding, attention, hierarchical text representations, and pre-trained transformerbased language models, and extending previous approaches by introducing a pseudo-sentence hierarchical attention network, the paper provides a comprehensive summary of the state-of-afairs in NLP-based AOB detection, clarifies the detection accuracy that is attainable with today's technology, discusses whether this degree is suficient for deploying deep learning-based text screening systems, and approaches the interpretability topic.

## 1. Introduction

The shift of human communication to online platforms is a double: edged sword. Social benefits include the opportunity to share opinions and experiences, get immediate feedback, and the opportunity to discuss the hottest topics. From an economic perspective, the data from online communications enable business organization to learn from customer experiences, improve service oferings, and raise firm performance. Examples of corresponding advancements include Liu et al. [1], who propose a method to assess a product's competitive advantages based on social media. Similarly, Zhang et al. [2] use natural language processing (NLP) to analyze knowledge payment platforms and shed light on customer satisfaction, while Siering et al. [3] examine online reviews to identify what service aspects customers value the most. On the other hand, online communication platforms also create a space for malicious behavior such as the distribution of fake news and reviews, which distort insights gained from the data and may harm the reputation of the platform [4,5]. The focus of this work is related to a similar problem: the detection of antisocial behavior, such as insulting, harassment, or threatening in online communication.

Detection of such antisocial behavior is highly important for social welfare due to social, legislative, and financial reasons. According to the Cyberbullying Research Center's annual data in 2016, 33.8% of young people aged 12–17 in the US have experienced cyberbullying in their lifetime [6]. According to one German law, social media providers like Facebook, Google, Microsoft are obliged in Germany to remove hate speech posts within 24 h and report on their progress every six months [7]. Legal requirements, social norms, and codes of conduct emphasizes the importance for online platforms to identify antisocial online behavior (AOB), which we use as an umbrella term for any malicious behavior that can be found in the textual content on online communications platforms including insult, threat, personal attack, usage of harmful, rude or ofensive language, cyberbullying and abuse.

Manual detection and monitoring of online content can be very costly, making autonomous systems for screening user-generated text content for traces of AOB a key attention point. Machine learning-based decision support systems that pre-screen transactions and flag suspicious cases for subsequent human inspection have proven efective in fraud detection [8] and may prove a viable solution for the AOB de tection problem of social media platforms.

In the paper, we elaborate on the detection of AOB using NLP. Early academic research in the field was mostly concerned with the use of traditional machine learning methods (TML) such as logistic regressions, support vector machines, and decision trees [e.g., [9]], as well as lexicon-based approaches [e.g., [10]]. These methods heavily rely on extensive feature engineering, and their performance highly depends on the representation of the data. DL methods automate the procedure of feature engineering by learning the representations of the data through non-linear transformations. Such representations often achieve better performance than handcrafted features [11]. The main contribution of the paper is the following: we consolidate prior work on AOB detection and text classification and provide a comprehensive benchmark of alternative text processing regimes. We compare methods of TML with deep learning (DL) while covering significant methodological advancements, including bidirectional encoding, attention, and techniques to exploit the hierarchical structure of text. Many of these DL techniques are new to the field of AOB detection and systematic comparisons of their potential to raise detection accuracy are, to our best knowledge, not available in prior research. Further, we extend hierarchical DL models and introduce a pseudo-sentence hierarchical at tention network. We investigate the potential of deep NLP transfer learning for AOB detection by considering transformer-based language models such as BERT in our analysis. Finally, we propose the usage of the LIME framework developed by Ribeiro et al. [12] as a final stage of AOB detection. This framework provides interpretability of the model's underlying logic, which might help moderators to decide whether to filter a post. Machine learning-based systems often reflect existing demographic biases [13], which might lead to “unfair” decisions. Interpretability also ensures that model predictions can be checked for possible unintended bias, which would require adjustment or revision of the detection model. All codes used for the experiment are available on Github at https://github.com/QuantLet/AOBDL\_code. Moreover, the reader can find an online appendix containing details on parameter tuning, used DL architectures, and additional literature on AOB detection at https://github.com/QuantLet/AOBDL\_code/blob/master/ AOBDL\_Online\_Appendix.pdf.

## 2. Related work

In only a few years, DL methods have revolutionized the fields of computer vision and NLP, in which they can now be considered a quasistandard [14]. Recently, a few DL-based approaches have appeared in the decision support literature. We review corresponding research below and distinguish between approaches that support decisionmaking based on analyzing structured versus unstructured data. This is to sketch the status-quo of DL-based decision support (DS). Thereafter, we review prior work on AOB detection, which we consider a relevant new application of model-based DS.

## 2.1. DS using structured data

Many data-driven DS models emerge from processing structured, tabular data sets using supervised machine learning. Examples include R&D budget allocation [15], sales forecasting [16], and credit card fraud detection [17], amongst others. The common denominator across corresponding models is that they support decision-making by forecasting a quantity of interest. For example, risk managers and financial analysts require accurate estimates of the future prospect of a stock or financial instrument, which machine learning models are able to predict [e.g., [18,19]]. Likewise, marketing managers require forecasts of customer behavior, for example to inform campaign planning and prevent customer churn [e.g., [20,21]]. Aiming to raise predictive accuracy, recent papers explore the potential of DL in such settings. For example, Kim et al. [11] examine pre-training based on stacked denoising auto-encoders in a risk management case study. Kraus et al. [22] review similar applications of DL to decision problems that are traditionally approached by ordinary machine learning and highlight opportunities for research. Arguably, the literature on model-based DS from time series forecasting has up until now made the most use of DL. [e.g., [23,24,25]].

## 2.2. DS using unstructured data

In addition to structured data, the analysis of unstructured data and especially textual data has received attention in recent DS studies. The extraction of consumer sentiment and preferences with regard to product attributes provides retails with insight to inform marketing strategies [26]. Further DS applications of NLP occur in finance where text data can help to predict hazardous financial events like bankruptcy or fraud [27]. Whenever unstructured data is involved, DL is a popular vehicle to solve the problem. For example, DL has been employed for analyzing sentiment in financial disclosures to predict stock price movements [28], or automate tip-mining from processing customer reviews [29]. Kratzwald et al. [30] report on a related application concerning text-based emotion recognition in a DS setting while De Caigny et al. [31] focus on DS in marketing and use text data in the form of customer emails to predict churn using convolutional neural networks. That study highlights the potential of combining text data with more traditional structured data to raise the predictive accuracy of a DS model. Extracting predictive features from text, DL is instrumental to such combined DS models.

## 2.3. DL in AOB detection

Manual detection and monitoring of online content can be very costly, making autonomous systems for screening user-generated text content for traces of AOB a key attention point. Decision support systems that pre-screen transactions and flag suspicious cases for subsequent human inspection have been found efective and eficient in the detection of fraud [32], network outage [33] or rating system manipulation [34] and also in the scope of early warning systems for antiterrorism initiatives [35]. Such approaches ground on machine learning and may prove a viable solution for the AOB detection problem of social media platforms. The system can screen textual content upon submis sion by some user, estimate a score of the content containing traces of AOB, and enforce approval by a moderator prior to publication whenever the estimated AOB probability is high.

The amount of literature on DL for AOB detection has exponentially grown within the last two years. Diferent steps of the modeling process can use DL techniques. One can use it solely for feature extraction to learn abstract representations of data and build another TML classifier on the top, e.g., Zhong et al. [36], or one can use deep learning networks for the whole training process, the feature extraction, as well as classification. In this research, we concentrate on academic work that uses DL for the entire training process.

Earlier research concentrates on architectures such as CNN and LSTM, as well as fully connected deep neural networks (DNN) [37]. Later research on DL models in AOB detection tends to use more complex models and constructs, such as bidirectional RNN (BRNNs), attention mechanism, and even hierarchically structured data in combination with attention. Agrawal and Awekar [38] compare the performance of a CNN, LSTM, bidirectional LSTM (BLSTM), and BLSTM with attention for training and validation for task-specific as well as for transfer learning. Santosh and Aravind [39] use a hierarchical model, where data is aggregated first on the syllable level and then on word level. The attention mechanism is applied further on word level. In another work, Cheng et al. [40] applied a hierarchical attention model (HAN) on Instagram data and compared it to the performance of another TML classifiers, K-nearest neighbors, Naive Bayes, logistic regression (LR), random forest (RF), and XGBoost. For their research, van Aken et al. [41] used LSTM, BLSTM, bidirectional gated recurrent unit (BGRU), BGRU with attention and CNN on Twitter and Wikipedia data. Furthermore, they identified common challenges in cyberbullying detection, such as doubtful labels and rhetorical questions, and performed in-depth error-analysis.

Current research mostly concentrates on applying and bench marking diferent ML and DL algorithms on social media data. It rarely focuses on the implementation of the proposed method as a DS system. Therefore, in our work, we aim not only to provide a thorough benchmark of DL-based architectures including state-of-the-art models, but also to extend it to the interpretability module. Such an extension is vital as it delivers a better understanding of the underlying reasoning of a DL method and provides support for the moderation of social media posts.

![](/api/attachments/UDFMVTFH/fulltext/images/f6276f3c4eb05c8704965672ac36543eb15b825ffaa4532cdea7c7222d4e48ad.jpg)  
Fig. 1. Overview of models.

## 3. Methodology

To fully appreciate the technical content, the reader might benefit from the following overview of ML technologies. In Fig. 1, we summarize our motivation on what machine learning approaches to in clude. The figure shows diferent methods and their drawbacks, which can be handled by more complex models.

We start with methods of TML, and as mentioned in the introduc tion, these methods heavily rely on handcrafted features, whereas DL models help to learn abstract data representations and extract features automatically. A traditional fully connected neural network (NN) cannot cope with sequential data and introduces separate parameters for each time step separately, resulting in an insuficient generalization on sequences with length not seen during the training [42]. Networks with loops [43], reflecting the temporal component of data, RNN can work with such sequences. Though traditional RNNs have impaired ability to deal with very long-term dependencies, the gradients propagated through the net might either vanish or explode [44]. The models that can deal with such a “vanishing gradient” problem are LSTM [45] and gated recurrent unit (GRU) [46]. The recurrent neural networks usually have a causal structure: the state at time step t does depend only on the past information [42]. However, some applications require knowledge of the whole input sequence. In text classification, a word meaning might, in some cases, be dependent on other words at the end of the sentence. BLSTM and BGRU proposed by Schuster and Paliwal [47] are models that can deal with such dependency of the future input. In the case of AOB detection, a bidirectional model may help us to diferentiate between “idiot like me” and “idiot like you”, where one of the sentences is insulting and other not. Attention models introduced by Bahdanau et al. [48] and other reduction techniques allow a model to memorize longer sequences, whereas hierarchical models help in reflecting the hierarchical structure of a text [49], which is advantageous in long text classification. All of the above-described models do usually rely on recurrence that is dificult to parallelize. Transformers are the models, which are proposed by Vaswani et al. [50], that rely entirely on the attention mechanism and positional encoding and, subsequently, alleviate the necessity of the usage of the recurrence which allows for higher parallelization of the models. Highly parallel models, thus, enable building much deeper models. Furthermore, deep transformers benefit from pre-training on large corpora, and their fine-tuning on specific datasets may achieve state-of-the-art performance. The models that we use in this section are BERT [51] and DistilBERT [52].

## 3.1. HAN and psHAN

One of the models using attention mechanisms on multiple levels is the HAN. Yang et al. [49] proposed the HAN for document classification tasks. This multi-leveled structure should enable the model to pay more or less attention to diferent parts of content when constructing a representation of the document. Diferent words are diferently important by depicting the whole essence of one sentence. Moreover, sentences are diferently important when we describe the meaning of the whole post or a document. Moreover, the same word can have diferent meanings, which depends on the context.

The first part of the model is the word encoder: every document is broken down into sentences, where each of the sentences is encoded separately. First, each word will be embedded into an embedding matrix, and afterward, using a BGRU, words are encoded by summarizing context within the sentence in both directions, so each word is represented by its surrounding context. The next part of the mechanism is the word attention. Therefore, word annotations obtained in the previous step are fed into a one-layer feed-forwarded neural network to generate hidden-state representation, which is then compared to the context vector through the softmax function resulting in normalized importance weights. These weights, afterward, are used to compute sentence vectors by weighting the sum of word annotations by their importance scores.

A similar procedure is done on the sentence level since not every sentence within a document contributes equally to the meaning of the document. Through a BGRU, each sentence within a document is encoded by its surrounding context, then hidden-representation is generated through a feed-forwarded neural network, which is then compared to a sentence level context vector. Obtained importance scores are used to weigh encoded sentences, the sum of which results in the document representation. Classification into categories is done in the very last step through a softmax one-layer network.

In the next step, we propose the pseudo-sentence HAN (psHAN) algorithm – the extension of the HAN. A psHAN is a network where the input documents are split not into real sentences but a set of sequences of an arbitrarily set length, so the input forms a list of sequences without separation into actual sentences. A pseudo-sentence is a series of words from a sentence but not necessarily the whole sentence. The length of such pseudo-sentence we treat as a meta-parameter, i.e., we choose the length during model selection and tuning.

The motivation to adjust the HAN algorithm is twofold: In the classical HAN, the pre-processing step requires an additional split of the posts into sentences according to punctuation marks, which enforces to maintain all other pre-processing steps for each sentence independently after the separation, otherwise, some pre-processing steps are not feasible. Whereas psHAN does not require additional splitting beforehand, which simplifies and accelerates the pre-processing procedure. Moreover, the technical implementation of HAN can be connected to an essential drawback: the length of a sentence, the number of sentences per post can have high variability, which is usually the case in AOB detection. During its implementation, one has to set up a threshold on the length of a sequence, and HAN has even two such thresholds. Having a positively skewed distribution of the sentence length and the number of sentences, taking the maximum values for the threshold can lead to very long computational times. Whilst cutting of twice, on the sentence and post level, can remove a lot of essential for prediction information: for some sentences which are longer than the threshold, we would remove parts of the text while adding zeros to the shorter [[example, comment, social, media, 0, 0, 0], [pseudosentence, attention, network, padded, zeros, maximum, length]. [parameter, acts, hyperparameter, chosen, during, training, 0], [0, 0, 0, 0, 0, 0, 0]]

Fig. 2. Tokenized Input for HAN.

sentences.

Hence, having psHAN, we are setting cutof only once - on the number of words per post, we will call it $N ,$ so padding procedure is also done only once. Further, we introduce two additional hyper-parameters: length of a sentence and the number of sentences per input document, as in the HAN architecture T and $L ,$ respectively. In the case of psHAN, the following equality holds $L \times T = N ,$ which is not necessarily true for the HAN model.

By rearranging data, we can gain the profit of the hierarchical structure at the same time not removing any information. Every post is just split into several sequences of a specific word amount.

We exemplify the diference on the following artificial case. Imagine having the following input sentence: This is an example of a comment on social media. In psHAN, it will be padded with zeros to the maximum length of a post parameter, which is equal for all the posts. This parameter acts as a hyper-parameter and is chosen during the training. Assuming we set T = 4 and L = 7, so i.e., for psHAN N = 28. In Figs. 2 and 3, we can see how the input will be tokenized for HAN and psHAN, respectively:

In the case of HAN we had to introduce more zeros for shorter sentences while removing some of the words for longer sentences. In this work we expect that the efect of having less reduced input will overweight the efect of having semantically completed input sequences. The rest of the psHAN's architecture remains the same as of HAN's, with only diference that instead of real sentences we have pseudo-sentences.

## 4. Experimental design

## 4.1. Dataset

The first data set used for the experiments comes from a Kaggle competition “Toxic Comment Classification”<sup>1</sup>. This competition is dedicated to the identification of diferent levels of toxicity in the Wikipedia Talk Pages. The second data set is retrieved from Twitter and was created by Davidson et al. [53], where the authors used it for au tomatic hate-speech detection. The third dataset is the English and Hindi data from Facebook created by Kumar et al. [54], which was used for aggression detection. For our project, we used only the data available in English. The final dataset comes from Formspring and is created by Reynolds et al. [55] and is available at the ChatCoder<sup>2</sup> website.

All the datasets and projects based on them mainly consider the multi-class classification problem. We decided to binarize the data to the “malicious” and “non-malicious” classes since the focus of our work lies in providing a benchmark in general rather than on multi-label classification. Therefore, we obtained four diferent datasets: Wikipedia – relatively big dataset with skewed distribution towards the “nonmalicious" class. Twitter, and Facebook – much smaller datasets with the majority of the “malicious” class and the smallest Formspring dataset, which similarly to the Wikipedia data is skewed towards the “malicious” class. In Table 1, the distribution of classes and the length of the posts are depicted.

## 4.2. Pre-processing

First, we transformed the data into the lower case. Short versions of negative contractions with apostrophes have been substituted with [[example, comment, social, media, pseudosentence, attention] [network, padded, zeros, maximum, length, post parameter] [equal, posts, parameter, acts, hyperparameter, chosen, during], [training, 0, 0, 0, 0, 0, 0]]

Fig. 3. Tokenized Input for psHAN.

<table><tr><td colspan="9">(a) Distribution of the classes.</td></tr><tr><td rowspan="2"></td><td colspan="2">Wikipedia</td><td colspan="2">Twitter</td><td colspan="2">FB</td><td colspan="2">Formspring</td></tr><tr><td>Train</td><td>Test</td><td>Train</td><td>Test</td><td>Train</td><td>Test</td><td>Train</td><td>Test</td></tr><tr><td>1</td><td>10%</td><td>10%</td><td>83%</td><td>83%</td><td>57%</td><td>57%</td><td>6%</td><td>6%</td></tr><tr><td>0</td><td>90%</td><td>90%</td><td>17%</td><td>17%</td><td>43%</td><td>43%</td><td>94%</td><td>94%</td></tr><tr><td>All</td><td>158,719</td><td>64,830</td><td>17,549</td><td>7,168</td><td>11,300</td><td>4,616</td><td>9,342</td><td>3,817</td></tr><tr><td></td><td>223,549</td><td></td><td>24,717</td><td></td><td>15,916</td><td></td><td>13,159</td><td></td></tr><tr><td colspan="9">(b) Length of the posts.</td></tr><tr><td></td><td></td><td>Wikipedia</td><td></td><td>Twitter</td><td></td><td>FB</td><td></td><td>Formspring</td></tr><tr><td>Mean</td><td></td><td>53.68</td><td></td><td>12.80</td><td></td><td>20.42</td><td></td><td>22.16</td></tr><tr><td>Std</td><td></td><td>81.52</td><td></td><td>6.05</td><td></td><td>27.53</td><td></td><td>21.61</td></tr><tr><td>Min</td><td></td><td>81.52</td><td></td><td>1</td><td></td><td>1</td><td></td><td>2</td></tr><tr><td>25%</td><td></td><td>13</td><td></td><td>8</td><td></td><td>9</td><td></td><td>11</td></tr><tr><td>50%</td><td></td><td>28</td><td></td><td>12</td><td></td><td>13</td><td></td><td>17</td></tr><tr><td>75%</td><td></td><td>60</td><td></td><td>18</td><td></td><td>23</td><td></td><td>27</td></tr><tr><td>Max</td><td></td><td>1,963</td><td></td><td>33</td><td></td><td>740</td><td></td><td>812</td></tr></table>

their full version. The negation “not” has usually shown good predictive performance, therefore it was not removed. Textual data in social media often includes emojis. A suitable pre-processing of emojis is vital to capture the sentiment of a piece of text [56]. To that end, we substitute emojis with their semantic representation. For example, we replace “:-)”, “:)” with the word “good” and “:-(“, “:(“with “bad”. Moreover, we removed stopwords. The pronoun “you” showed the importance in the identification of malicious content, therefore it was not removed. Besides, we deleted URLs. Moreover, the removal of all non-alphanumeric characters was performed.

For TML classifiers, the TF-IDF tokenization was performed on the n-gram wording level, where n = 1. For all DL models, tokenization was performed on the word level. The meta-parameters, such as the maximum amount of features, the length of the post, or for the hierarchical models, the number of sentences for one post, and the highest number of the words within one sentence were selected using a manual grid search and cross-validation. For hierarchical models, splitting into sentences was first established, and only afterward, we removed all the punctuation marks. For all DL models, we use RMSprop optimizer with learning rate of 0.00003 for pre-trained transformers and of 0.01 for all other DL models. The learning rate grid was [0.01, 0.001, 0.00003]. More details, the reader can find in the online appendix.

## 4.3. Evaluation

Stratified cross-validation with k = 5, where k is the number of folds, was used. For all models, we perform manual hyper-parameter tuning.

While dealing with AOB detection, we quite often have to deal with a very small portion of the positive class observation. Therefore, we decided to use the average precision (Av. Prec.), to reflect the problem of imbalance in some datasets. Thus, in the analysis, we report Av. Prec., the area under receiver operating characteristic curve (AUC), and the F1-score. The threshold for the F1 was set for each model individually in the range between [0.1, 0.9] using the cross-validation.

## 5. Experiments

## 5.1. TML vs. DL

As a first experiment, we compare TML methods with CNN and GRU, two basic DNN architectures, which many more sophisticated models are based on. To that end, we select TML methods that have been used frequently in the AOB literature, including support vector machines (SVM), logistic regression with l2 regularization (LR), and random forest (RF) [e.g., 9,38]. Moreover, we consider gradient boosting (LightGBM) due to this model's good performance in predic tion benchmarks. Finally, we consider a detection model that pursues a lexicon-based (LB) approach: if a sentence contains a word from a dictionary of banned words, the sentence is classified as malicious. To implement the LB classifier, we use the list from the website bannedwordlist.com<sup>3</sup>.

In Table 2, we depict the results in terms of Av. Prec., AUC, and the F1-score. The highlighted numbers represent the best performance in each category. The first impression of the results is that there is no unique “treatment” for all datasets. LB approach shows the most inferior performance amongst all other methods. DL models outperform TML for all datasets except the Formspring data. For the Formspring data, on the other side, a simple logistic regression achieves the best performance. One possible reason could be that DL models, by the presence only a small dataset, do not merely manage to train properly. This result is not surprising since the DL is seen to be beneficial for the large datasets.

For the large Wikipedia dataset with a small portion of malicious cases GRU network outperforms all other models. For the smaller Twitter dataset with a high amount of malicious observations, a GRU and a CNN share the top position, whereas, for another dataset, where the majority of observations are malicious – from Facebook, CNN is the best model in terms of Av. Prec. and AUC. The logistic regression shows the best F1. Twitter data shows the least variability in the models performance in terms of Av. Prec., and although DL models outperform TML, the discrepancy in the performance is very low. Interestingly, the methods based on the decision trees, which are usually seen as state-ofthe-art for structured data, perform relatively poorly on our text clas sification task.

Another interesting tendency we can see in the metrics: in the case where the malicious class prevails, the F1 score is closer to the AUC, while for the data where the malicious class is just a minority, the F1 score tends to proximate the Av. Prec.

## 5.2. Bidirectionality, attention and pooling

In the second experiment, we added bidirectionality to our recurrent network to understand whether the AOB detection classification process depends on future input. Moreover, in the introductory and literature parts, we mentioned that AOB research quite often compares models with sophisticated reduction techniques with models without reduction techniques at all. Further, we introduce reduction techniques: we compare the attention mechanism with global maximum and average pooling by using BGRU + diferent reduction techniques. The Table 3 depicts the results of the second experiment.

Compared to the results in experiment 1, we can see a marginal improvement of the performance in terms of Av. Prec. of the GRU model for Wikipedia and Facebook data. Nonetheless, the increase is minimal, so when using the models in production, one could consider using a model with fewer parameters to reduce computational costs. For smaller datasets, Maximum Pooling achieves the best performance. Even though the attention mechanism gained much popularity, our results convey that the simple pooling techniques or not using any reduction techniques may produce better performance.

## 5.3. Hierarchical attention model

In the last step, we dive into hierarchical attention models to investigate whether reflecting hierarchical structure that benefits the document classification might improve the performance of machine learning models in the case of AOB detection. Therefore we use HAN and psHAN proposed in the Methodology section.

In other words, we investigate whether there is a need to separate social media comments into sentences and use this hierarchical structure to improve predictive performance. As we can see in Table 4, the use of such hierarchy only reduces Av. Prec. and AUC, i.e., HAN performs worse than just GRU or BGRU. Interestingly, the use of pseudosentences in psHAN shows better results than the original HAN, nonetheless, still loosing to the simpler architectures. One possible explanation for the hierarchical models' poor performance is the length of the posts in our data. HAN is initially designed for document classification, where texts tend to have a longer length, while the posts from social media are relatively short. The hierarchical models summarize the signal over many levels, e.g., sentence and word level, and thus too much information is lost through this summarization.

## 5.4. Pre-trained transformers

In the last experiment, we want to investigate whether pre-trained language models based on the transformer architecture may improve predictive performance. For that purpose, we use BERT and its lighter version DistilBERT models with two diferent types of training. BERT/ DistilBERT last implies that we took a pre-trained architecture and finetuned it on our data while adjusting the weights only of the last sigmoid layer. BERT/DistilBERT full means that all the weights were trainable during the model fitting.

In Table 5, we can see the results of this experiment. At first glance, a fully trained BERT model shows superior performance for all data sets in at least one performance metric, and therefore, it could be the model chosen by default as a candidate for the task of AOB detection. On the other hand, the discrepancy in the performance for some datasets is not very high, e.g., for the Twitter data, there is no diference. Thus one can choose an architecture with less trainable parameters without losing much in the performance. Overall, compared with the previous experiments, we see that pre-trained transformers outperform other models, which supports the idea that the transformer-based models, allowing pre-training, may help to apply DL not only to the large but also to the smaller datasets.

## 5.5. Best models

In this section, we summarize the results of all models used throughout the experiments. Overall, the results show that DL methods, on average, outperform the methods of TML. GRU wins in performance for the large Wikipedia dataset, achieves the same performance as CNN for the Twitter data, while losing to CNN and logistic regression on FB and Formspring data. Although RNNs are seen as one of the standards for the textual data, CNNs may also achieve suficient or even superior performance. Bidirectionality does not necessarily improve the performance of the recurrent neural network. In our setup, it helped to gain a better result in two out of four dataset settings, and the improvement was marginal. In such a context, we might tend to choose the model of lower complexity. Popular attention mechanism loses to Maximum pooling in all four settings, while in the case of Wikipedia data, all reduction techniques are inefective. Therefore, this type of increasing complexity of the model might even worsen the result. Our results emphasize the fact that it is not always recommendable to use reduction over diferent time-steps of our encoder, but sometimes having just the last hidden-state is more eficient.

Table 2  
Results of Experiment 1: TML vs. DL.

<table><tr><td rowspan="2">Model</td><td colspan="3">Wikipedia</td><td colspan="3">Twitter</td><td colspan="3">FB</td><td colspan="3">Formspring</td></tr><tr><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td></tr><tr><td>LB</td><td>0.375</td><td>0.718</td><td>0.531</td><td>0.934</td><td>0.805</td><td>0.780</td><td>0.573</td><td>0.510</td><td>0.058</td><td>0.203</td><td>0.705</td><td>0.308</td></tr><tr><td>LR</td><td>0.833</td><td>0.967</td><td>0.745</td><td>0.995</td><td>0.978</td><td>0.964</td><td>0.805</td><td>0.784</td><td>0.778</td><td>0.607</td><td>0.906</td><td>0.580</td></tr><tr><td>RF</td><td>0.813</td><td>0.962</td><td>0.741</td><td>0.995</td><td>0.978</td><td>0.962</td><td>0.781</td><td>0.762</td><td>0.775</td><td>0.498</td><td>0.880</td><td>0.497</td></tr><tr><td>SVM</td><td>0.827</td><td>0.962</td><td>0.743</td><td>0.996</td><td>0.982</td><td>0.970</td><td>0.813</td><td>0.786</td><td>0.776</td><td>0.587</td><td>0.891</td><td>0.562</td></tr><tr><td>LightGBM</td><td>0.819</td><td>0.958</td><td>0.736</td><td>0.996</td><td>0.980</td><td>0.969</td><td>0.777</td><td>0.745</td><td>0.760</td><td>0.492</td><td>0.824</td><td>0.487</td></tr><tr><td>GRU</td><td>0.859</td><td>0.973</td><td>0.768</td><td>0.997</td><td>0.983</td><td>0.971</td><td>0.800</td><td>0.776</td><td>0.774</td><td>0.537</td><td>0.867</td><td>0.516</td></tr><tr><td>CNN</td><td>0.850</td><td>0.971</td><td>0.762</td><td>0.997</td><td>0.985</td><td>0.971</td><td>0.818</td><td>0.788</td><td>0.775</td><td>0.586</td><td>0.906</td><td>0.552</td></tr></table>

Table 3  
Results of Experiment 2: Bidirectionality, Attention and Pooling.

<table><tr><td rowspan="2">Model</td><td colspan="3">Wikipedia</td><td colspan="3">Twitter</td><td colspan="3">FB</td><td colspan="3">Formspring</td></tr><tr><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td></tr><tr><td>BGRU</td><td>0.860</td><td>0.973</td><td>0.758</td><td>0.996</td><td>0.981</td><td>0.963</td><td>0.801</td><td>0.773</td><td>0.771</td><td>0.514</td><td>0.860</td><td>0.405</td></tr><tr><td>BGRU + Max</td><td>0.857</td><td>0.972</td><td>0.764</td><td>0.997</td><td>0.984</td><td>0.971</td><td>0.816</td><td>0.788</td><td>0.779</td><td>0.549</td><td>0.883</td><td>0.511</td></tr><tr><td>BGRU + Att</td><td>0.856</td><td>0.972</td><td>0.757</td><td>0.996</td><td>0.983</td><td>0.970</td><td>0.807</td><td>0.776</td><td>0.770</td><td>0.520</td><td>0.874</td><td>0.510</td></tr><tr><td>BGRU + Avg</td><td>0.855</td><td>0.971</td><td>0.769</td><td>0.996</td><td>0.982</td><td>0.969</td><td>0.806</td><td>0.783</td><td>0.778</td><td>0.544</td><td>0.874</td><td>0.324</td></tr></table>

Table 4  
Results of Experiment 3: Hierarchical models.

<table><tr><td rowspan="2">Model</td><td colspan="3">Wikipedia</td><td colspan="3">Twitter</td><td colspan="3">FB</td><td colspan="3">Formspring</td></tr><tr><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td></tr><tr><td>HAN</td><td>0.833</td><td>0.964</td><td>0.748</td><td>0.995</td><td>0.978</td><td>0.960</td><td>0.795</td><td>0.768</td><td>0.767</td><td>0.579</td><td>0.899</td><td>0.554</td></tr><tr><td>psHAN</td><td>0.853</td><td>0.971</td><td>0.768</td><td>0.996</td><td>0.981</td><td>0.969</td><td>0.809</td><td>0.782</td><td>0.778</td><td>0.596</td><td>0.879</td><td>0.576</td></tr></table>

Table 5  
Results of Experiment 4: Transformers.

<table><tr><td rowspan="2">Model</td><td colspan="3">Wikipedia</td><td colspan="3">Twitter</td><td colspan="3">FB</td><td colspan="3">Formspring</td></tr><tr><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td><td>Av. Prec.</td><td>AUC</td><td>F1</td></tr><tr><td>BERT full</td><td>0.869</td><td>0.976</td><td>0.780</td><td>0.997</td><td>0.988</td><td>0.973</td><td>0.828</td><td>0.813</td><td>0.779</td><td>0.612</td><td>0.924</td><td>0.573</td></tr><tr><td>BERT last</td><td>0.864</td><td>0.974</td><td>0.779</td><td>0.997</td><td>0.988</td><td>0.975</td><td>0.832</td><td>0.811</td><td>0.751</td><td>0.593</td><td>0.912</td><td>0.531</td></tr><tr><td>DistilBERT full</td><td>0.867</td><td>0.975</td><td>0.777</td><td>0.997</td><td>0.986</td><td>0.975</td><td>0.818</td><td>0.804</td><td>0.790</td><td>0.599</td><td>0.915</td><td>0.547</td></tr><tr><td>DistilBERT last</td><td>0.867</td><td>0.976</td><td>0.775</td><td>0.997</td><td>0.987</td><td>0.975</td><td>0.824</td><td>0.805</td><td>0.751</td><td>0.584</td><td>0.912</td><td>0.538</td></tr></table>

Reflecting the hierarchical structure for AOB detection has also decreased the performance. A probable explanation for this is the higher variability of the length in the posts and, in general, shorter texts, compared to the HAN domain – document classification.

The usage of pre-trained language models achieves the best result overall. The most complex architecture, in terms of the amount of trainable parameter – full BERT, beats all other models in almost all settings. It supports the idea that AOB detection can benefit from finetuning of the language models.

## 5.6. Interpretability

We conclude the empirical part of the paper with an analysis of model interpretability. DL models are considered ‘black boxes' and this may impede their successful deployment for DS. Local regulation may even enforce the use of interpretable models. For example, the EU data protection act prescribes that in the case of automated DS systems, including profiling, “meaningful information about the logic involved” should be provided<sup>4</sup>. Although DS systems fighting AOB based solely on the textual content do not necessarily involve profiling, such models may face unintended bias [57], meaning that a model performs better for some demographic groups than others [58]. For example, a mention of gender, religion, or sexual orientation in a post may achieve higher prediction scores of being malicious even if the comment is not intended to be malicious. Usually, such bias enters the model due to the way the data is retrieved. Subsequently, the model just captures the overall tonality of the data. However, it leads to “unfair” decisions, as the model discriminates diferent groups diferently. These decisions may negatively impact society [57] or harm the reputation of the institution implementing the AOB detection DS system.

The importance of interpretability is twofold: not only a company or an authority needs to understand on what basis the model makes a decision, so it can comply to the regulations or be clear to the stakeholder, but also to make sure that the system does not discriminate diferent groups of individuals. Therefore, we propose using the LIME framework developed by Ribeiro et al. [12] as a final stage of AOB detection, which stands for local interpretable model-agnostic explanations. LIME pursues a post hoc analysis of model-based predictions. LIME approximates a black-box ML model locally with an interpretable model and highlights what features are essential for the calculated prediction. Applied to an AOB detection case, LIME provides

(b) Example of LIME highlighting  
![](/api/attachments/UDFMVTFH/fulltext/images/bef2be7a064b16d401b9cceaafc82b3c4c0b31b7d355de4ac8e26c5b5e3da566.jpg)  
Fig. 4. Output of the LIME framework.

# Text with highlighted words this is completely wrong, are you anidiotor what

(b) Example of LIME highlighting

explanations in the form of highlighting the words in an input text that are most important for the model prediction of the text being malicious or not. This highlighting could help a moderator to make a final decision whether to filter a post, help building trust in the detection model, and also serve as a confirmation that the model-internal logic is sound. In Fig. 4, we exemplify LIME explanations for a hypothetical ofensive post.

In addition to supporting moderators, the LIME framework may also reveal additional information concerning model bias. Unintended bias is not always discovered beforehand. It may be that not all the groups that could be discriminated are known to the system a priori when training the AOB detection model. However, using LIME, the moderator may receive an additional hint that the predictive system puts too high weights on the words that should not be considered malicious, such as race, religion, gender, etc. Identifying such cases promptly and reporting it to the designers of the ML model ofers the opportunity to retrain the model and remedy its “unfairness” in a timely manner. In Fig. 5, we depict such an “unfair” situation. The example sentence receives a 65% score of being malicious and LIME reveals that this comes large from the occurrence of the word “gay”. This word is not malicious per se, which is exactly the reason why lexicon-based approaches cannot provide satisfactory performance in AOB detection. Adding ex plainability to the DS system helps to detect such “unfair” treatment early, remove unintended bias from the data, and re-train the model.

## 6. Conclusion and further work

Detection and prevention of AOB in online content have become an essential problem for social welfare and companies that provide platforms where user-generated content is shared. Manual monitoring of such behavior can be very costly and time-consuming. On the other hand, the absence of moderation can lead to regulatory consequences. This is why support systems that screen user-generated text content and identify cases that warrant manual inspection are of high importance. DL methods are a natural candidate for the analytical core of corresponding support systems due to high predictive performance in text classification.

The goal of the paper was to compare a broad range of text classification methods for AOB detection. Given the many degrees of freedom in devising DL-based text classifiers, a related goal was to identify structures and architectural components that work well in AOB detection. The most important and probably also the most prominent finding is that there is no unique “treatment” for AOB detection. Neither the architecture nor the metric can be uniquely defined for all possible AOB detection settings. Although, AOB detection is usually seen as a classification problem with a class imbalance towards the “non-malicious” class, due to diferent data retrieval approaches we might end with a dataset highly skewed towards the “malicious” class. These two different settings require diferent performance metrics, which complicates the benchmarking of models. Moreover, there is no unique architecture that beats all other models in all settings.

We have shown that DL models consistently outperform TML methods in the majority of settings. Further, we were able to show that the accuracy of AOB detection slightly improves when we introduce a bidirectional recurrent layer. Additionally, we concluded that in the case of Wikipedia data, we do not need reduction techniques. A relatively simple GRU and bidirectional GRU outperform more complex models with additional structures. For other datasets, CNNs show

![](/api/attachments/UDFMVTFH/fulltext/images/8477bab73b9bce3f491b819d2b8c436bd93316a0b9f15b1f0542fdcf063a8c9a.jpg)  
(a) Example of LIME output  
Fig. 5. Example of unintended bias in the model.

Text with highlighted words In summer 2017, the German parliament passed a bill for legislation of gay marriage similar or even superior performance, therefore showing that RNNs are not the only option in the AOB detection. We found the psHAN model, which we introduce in this paper, to outperform the original HAN. Nonetheless, the hierarchical structure has only decreased the perfor mance for all datasets.

Furthermore, we have shown that pre-trained language models, such as BERT and DistilBERT, achieve the best performance for the AOB detection, independently of the size of the dataset. However, the variability in the performance for some datasets, such as Twitter, is so small that question arises whether we need to deploy such a computationally “heavy” model to achieve a very marginal improvement. Finally, we introduced the interpretability module that not only helps to understand underlying logic but also might give additional hints if a model is “unfair” and needs to be readjusted. For further work, we are planning to address the problem of noisy labels to correct wrongly assigned classes. Moreover, we want to investigate whether it is possible to design an interpretable lexicon-based classifier using the knowledge from the LIME framework and DL state-of-the-art-architectures.

## Declaration of Competing Interest

None.

## Acknowledgements

Financial support from the Deutsche Forschungsgemeinschaft via the IRTG 1792 “High Dimensional Nonstationary Time Series”, Humboldt-Universität zu Berlin, is gratefully acknowledged.

## References

[1] Y. Liu, C. Jiang, H. Zhao, Assessing product competitive advantages from the per spective of customers by mining user-generated content on social media, Decis. Support. Syst. 123 (2019) 113079.

[2] J. Zhang, J. Zhang, M. Zhang, From free to paid: customer expertise and customer satisfaction on knowledge payment platforms, Decis. Support. Syst. 127 (2019) 113140.

[3] M. Siering, A.V. Deokar, C. Janze, Disentangling consumer recommendations: explaining and predicting airline recommendations based on online reviews, Decis. Support. Syst. 107 (2018) 52–63.

[4] C. Zhang, A. Gupta, C. Kauten, A.V. Deokar, X. Qin, Detecting fake news for reducing misinformation risks using analytics approaches. Eur, J. Oper. Res. 279 (3) (2019)1036–1052.

[5] A. Heydari, M. Tavakoli, N. Salim, Detection of fake opinions using time series, Expert Syst. Appl. 58 (2016) 83–92

[6] J.W. Patchin, 2016 Cyberbullying Data, (2016) https://cyberbullying.org/2016- cyberbullving-data.

[7] Deutsche Welle, Germany Fines Facebook for Underreporting Hate Speech Complaints, (2019) https://www.dw.com/en/germany-fines-facebook-forunderreporting-hate-speech-complaints/a-49447820-0.

[8] E. Stripling, B. Baesens, B. Chizi, S. vanden Broucke, Isolation-based conditional anomaly detection on mixed-attribute data to uncover workers’ compensation fraud, Decis. Support. Syst. 111 (2018) 13–26.

[9] T. Davidson, D. Warmsley, M. Macy. I. Weber, Automated hate speech detection and the problem of offensive language, Eleventh International Aaai Conference on Web and Social Media 2017

[10] U. Bretschneider, R. Peters, Detecting Cyberbullying in Online Communities, ECIS, 2016 ResearchPaper61.

[11] A. Kim, Y. Yang, S. Lessmann, T. Ma, M.-C. Sung, J.E. Johnson, Can deep learning predict risky retail investors? A case study in financial risk behavior forecasting,

[12] M.T. Ribeiro, S. Singh, C. Guestrin, “Why should i trust you?” explaining the pre dictions of any classifier, Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016, pp. 1135–1144.

[13] M.R. Costa-jussà, An analysis of gender bias studies in natural language processing

[14] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (2015) 436–444.

[15] H. Jang, A decision support framework for robust r&d budget allocation using machine learning and optimization, Decis. Support, Syst, 121 (2019) 1–12

[16] Z.-L. Sun, T.-M. Choi, K.-F. Au, Y. Yu, Sales forecasting using extreme learning machine with applications in fashion retailing, Decis. Support. Syst. 46 (2008)

[17] N. Carneiro, G. Figueira, M. Costa, A data mining based system for credit-card fraud

[18] N.N. Vo, X. He, S. Liu, G. Xu, Deep learning for decision making and the optimization of socially responsible investments and portfolio, Decis. Support. Syst. 124

(2019) 113097.

[19] P. Hájek, Municipal credit rating modelling by neural networks, Decis. Support. Syst. 51 (2011) 108–118.

[20] K. Coussement, S. Lessmann, G. Verstraeten, A comparative analysis of data pre paration algorithms for customer churn prediction: a case study in the tele communication industry, Decis. Support. Syst. 95 (2017) 27–36.

[21] A. De Caigny, K. Coussement, K.W. De Bock, Leveraging fine-grained transaction data for customer life event predictions, Decis. Support. Syst. 130 (2020) 113232.

[22] M. Kraus, S. Feuerriegel, A. Oztekin, Deep learning in business analytics and operations research: models, applications and managerial implications, Eur. J. Oper Res. 281 (2020) 628–641.

[23] A.L. Loureiro, L. Miguéis, L.F. da Silva, Exploring the use of deep neural networks for sales forecasting in fashion retail, Decis. Support. Syst. 114 (2018) 81–93.

[24] D. Koehn, S. Lessmann, M. Schaal, Predicting online shopping behaviour from clickstream data using deep learning. Expert Syst. Appl. 150 (2020) 113342.

[25] T. Fischer, C. Krauss, Deep learning with long short-term memory networks for financial market predictions. Eur, J. Oper. Res. 270 (2018) 654–669.

[26] X. Bai, Predicting consumer sentiments from online text, Decis. Support. Syst. 50 (2011) 732–742.

[27] M. Cecchini, H. Aytug, G.J. Koehler, P. Pathak, Making words work: using financial text as a predictor of financial events, Decis. Support. Syst. 50 (2010) 164–175

[28] M. Kraus, S. Feuerriegel, Decision support from financial disclosures with deep neural networks and transfer learning, Decis. Support. Syst. 104 (2017) 38–48.

[29] D. Zhu, T. Lappas, J. Zhang, Unsupervised tip-mining from customer reviews, Decis. Support, Syst. 107 (2018) 116–124.

[30] B. Kratzwald, S. Ilić, M. Kraus, S. Feuerriegel, H. Prendinger, Deep learning for afective computing: text-based emotion recognition in decision support, Decis Support. Syst. 115 (2018) 24–35.

[31] A. De Caigny, K. Coussement, K.W. De Bock, S. Lessmann, Incorporating textual information in customer churn prediction models based on a convolutional neural network, Int. J. Forecast. (2019) In Press

[32] Y. Wang, W. Xu, Leveraging deep learning with lda-based text analytics to detect automobile insurance fraud, Decis. Support. Syst. 105 (2018) 87–95.

[33] Ž. Deljac, M. Randić, G. Krčelić, Early detection of network element outages based on customer trouble calls, Decis. Support. Syst. 73 (2015) 57–73.

[34] O. Ivanova, M. Scholz, How can online marketplaces reduce rating manipulation? A new approach on dynamic aggregation of online ratings, Decis. Support. Syst. 104 (2017) 64–78.

[35] H. Dutta, K.H. Kwon, H.R. Rao, A system for intergroup prejudice detection: the case of microblogging under terrorist attacks. Decis, Support, Syst. 113 (2018 11–21.

[36] H. Zhong, H. Li, A.C. Squicciarini, S.M. Rajtmajer, C. Grifin, D.J. Miller, C. Caragea, Content-Driven Detection of Cyberbullying on the Instagram Social Network, IJCAI, 2016, pp. 3952–3958.

[37] N. Potha, M. Maragoudakis, Cyberbullying detection using time series modeling, 2014 IEEE International Conference on Data Mining Workshop, 2014, pp. 373–382.

[38] S. Agrawal, A. Awekar, Deep learning for detecting cyberbullying across multiple social media platforms, Advances in Information Retrieval, Springer International Publishing, Cham, 2018, pp. 141–153

[39] T.Y.S.S. Santosh, K.V.S. Aravind, Hate speech detection in hindi-english code-mixed social media text. Proceedings of the ACM India Joint International Conference on Data Science and Management of Data. 2019. pp. 310–313.

[40] L. Cheng, R. Guo, Y. Silva, D. Hall, H. Liu, Hierarchical attention networks for cyberbullving detection on the instagram social network. Proceedings of the 2019 SIAM International Conference on Data Mining. 2019. pp. 235–243

[41] B. van Aken, J. Risch, R. Krestel, A. Löser, Challenges for Toxic Comment Classification: An in-Depth Error Analysis, in: Proceedings of the 2nd Workshop on Abusive Language Online, Association for Computational Linguistics, Brussels, Belgium, 2018, pp. 33–42.

[42] I. Goodfellow, Y. Bengio, A. Courville, Y. Bengio, Deep Learning, Volume 1, MIT press Cambridge, 2016.

[43] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning representations by back-propagating errors, nature 323 (1986) 533–536.

[44] S. Hochreiter, Y. Bengio, P. Frasconi, J. Schmidhuber, et al., Gradient Flow in Recurrent Nets: The Difficulty of Learning Long-Term Dependencies, (2001)

[45] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural Comput. 9 (1997) 1735-1780

[46] K. Cho, B. Van Merriënboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, Y. Bengio, Learning Phrase Representations Using Rnn Encoder-Decoder for Statistical Machine Translation, arXiv Preprint arXiv:1406.1078 (2014).

[47] M. Schuster, K.K. Paliwal, Bidirectional recurrent neural networks, IEEE Trans. Signal Process. 45 (1997) 2673–2681.

[48] D. Bahdanau, K. Cho, Y. Bengio, Neural Machine Translation by Jointly Learning to Align and Translate, arXiv Preprint arXiv:1409.0473 (2014).

[49] Z. Yang, D. Yang, C. Dyer, X. He, A. Smola, E. Hovy, Hierarchical attention networks American Chapter of the Association for Computational Linguistics: Human Language Technologies, 2016, pp. 1480–1489

[50] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A.N. Gomez, Ł. Kaiser, I. Polosukhin, Attention is all you need, Advances in Neural Information Processing Systems, 2017, pp. 5998–6008.

[51] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, Bert: Pre-training of deep bidirec tional transformers for language understanding, arXiv preprint arXiv:1810.04805 (2018).

[52] V. Sanh, L. Debut, J. Chaumond, T. Wolf, Distilbert, a Distilled Version of Bert: Smaller, faster, Cheaper and Lighter, arXiv Preprint arXiv:1910.01108, (2019).

[53] T. Davidson, D. Warmsley, M. Macy, I. Weber, Automated hate speech detection and the problem of ofensive language, Proceedings of the 11th International AAAI Conference on Web and Social Media, ICWSM ‘17, 2017, pp. 512–515.

[54] R. Kumar, A.N. Reganti, A. Bhatia, T. Maheshwari, Aggression-annotated Corpus of Hindi-English code-mixed data. Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018), 2018.

[55] K. Reynolds, A. Kontostathis, L. Edwards, Using machine learning to detect cyber bullying, 2011 10th International Conference on Machine Learning and Applications and Workshops, vol. 2, IEEE, 2011, pp. 241–244.

[56] N. Mahmoudi, P. Docherty, P. Moscato, Deep neural networks understand investors better, Decis. Support. Syst. 112 (2018) 23–34.

[57] L. Dixon, J. Li, J. Sorensen, N. Thain, L. Vasserman, Measuring and mitigating unintended bias in text classification, Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society, 2018, pp. 67–73.

[58] M. Hardt, E. Price, N. Srebro, Equality of opportunity in supervised learning, Advances in Neural Information Processing Systems, 2016, pp. 3315–3323.

Elizaveta Zinovyeva is a PhD student of of the International Research Training Group IRTG1792 “High dimensional nonstationary time series” at the Humboldt-Universität zu Berlin. Previously she has completed her Master's studies in Information Systems and Bachelor's studies in Business Administration at the Humboldt-Universität zu Berlin. He research focuses on application of deep neural networks on sequential data.

Wolfgang Karl Härdle attained his Dr. rer. nat. in Mathematics at Universität Heidelberg in 1982 and in 1988 his habilitation at Universität Bonn. He is Ladislaus von Bortkiewicz Professor of Statistics at Humboldt-Universität zu Berlin and the director of the Sino

German International Research Training Group IRTG1792 “High dimensional nonsta tionary time series”, a joint project with WISE, Xiamen University.

His research focuses on data sciences, dimension reduction and quantitative finance. He has published over 30 books and more than 300 papers in top statistical, econometrics and finance journals. He is highly ranked and cited on Google Scholar, REPEC and SSRN. He has professional experience in financial engineering, smart (specific, measurable, achievable, relevant, timely) data analytics, machine learning and cryptocurrency mar kets.

Stefan Lessmann received a diploma in business administration and a PhD from the University of Hamburg in 2002 and 2007, respectively. Stefan worked as a lecturer and senior lecture in business informatics at the Institute of Information Systems of the University of Hamburg. Since 2008, Stefan is a guest lecturer at the School of Management of University of Southampton, where he teaches under- and postgraduate courses on quantitative methods, electronic business, and web application development. Stefan completed his habilitation in the area of predictive analytics in 2012. In 2014, Stefan joined the Humboldt-University of Berlin, where he heads the Chair of Information Systems at the School of Business and Economics. Stefan published several papers in leading international journals and conferences, including the European Journal of Operational Research, the IEEE Transactions of Software Engineering, and the International Conference on Information Systems. He actively participates in knowledge transfer and consulting projects with industry partners; from small start-up companies to global players.
