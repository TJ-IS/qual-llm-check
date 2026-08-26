---
otero_id: 14538
otero_key: "UEWRRJEP"
title: "Deep learning for detecting financial statement fraud"
authors: "Patricia Craja; Alisa Kim; Stefan Lessmann"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113421"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

## Deep learning for detecting financial statement fraud

Patricia Craja, Alisa Kim, Stefan Lessmann

![](/api/attachments/UEWRRJEP/fulltext/images/0b606824b088328267761ce56655044efa750240d45b45f54383fb8d3f58be6d.jpg)

PII: S0167-9236(20)30176-7

DOI: https://doi.org/10.1016/j.dss.2020.113421

Reference: DECSUP 113421

To appear in: Decision Support Systems

Received date: 5 May 2020

Revised date: 3 September 2020

Accepted date: 30 September 2020

Please cite this article as: P. Craja, A. Kim and S. Lessmann, Deep learning for detecting financial statement fraud, Decision Support Systems (2020), https://doi.org/10.1016/ j.dss.2020.113421

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# Deep Learning for detecting financial statement fraud

Patricia Craja<sup>a,</sup>, Alisa Kim<sup>a</sup>, Stefan Lessmann

<sup>a</sup>School of Business and Economics, Humboldt University of Berlin, Berlin, Germany

## Abstract

Financial statement fraud is an area of significant consternation for potential investors, auditing companies, and state regulators. The paper proposes an approach for detecting statement fraud through the combination of information from financial ratios and managerial comments within corporate annual reports. We employ a hierarchical attention network (HAN) to extract text features from the Management Discussion and Analysis (MD&A) section of annual reports. The model is designed to offer two distinct features. First, it reflects the structured hierarchy of documents, which previous approaches were unable to capture. Second, the model embodies two different attention mechanisms at the word and sentence level, which allows content to be differentiated in terms of its importance in process of constructing the document representation. As a result of its architecture, the model captures both content and context of managerial comments, which serve as supplementary predictors to financial ratios in the detection of fraudulent reporting. Additionally, the model provides interpretable indicators denoted as “red-flag” sentences, which assist $\odot ^ { * } \mathrm { { ‰} }$ in their process of determining whether further investigation of a specific annual report is required. Empirical results demonstrate that textual features of MD&A sections extracted by HAN yield promising classification results and substantially reinforce financial ratios.

Keywords: fraud detection, financial statements, deep learning, text analytics

## 1. Introduction

Fraud is a global problem that affects a variety of different businesses with a severe negative impact on firms and relevant stakeholders. The financial implications of fraudulent activities occurring globally in the past two decades are estimated to amount up to \$5.127 trillion, with associated losses increasing by 56% in the past ten years [21]. The actual costs of fraud are potentially greater, particularly if one also considers the indirect costs including harm the to credibility of investors, creditors and, employees and the reduction in business caused by the resultant scandal. Eventually, fraudulent activities may also lead to bankruptcy. All types of businesses and industries are affected by fraud. However, smaller organizations (less than 100 employees) as well as nonprofit organizations that have weaker internal control systems and fewer resources to recover from fraud losses can be more susceptible to fraud [2].

The Association of Certified Fraud Examiners (ACFE), the world‟s largest anti-fraud organization, recognizes three main classes of fraud: corruption, asset misappropriation, and fraudulent statements [66]. All three have specific properties and successful fraud detection requires comprehensive knowledge of their particular characteristics. This study concentrates on financial statement fraud and adheres to the definition of fraud proposed by Nguyen [50], who stated that it is “the material omissions or misrepresentations resulting from an intentional failure to report financial information in accordance with generally accepted accounting principles“. For this study, the terminology “financial statement fraud“, “fraudulent financial reporting“, and “financial misstatements“ are used interchangeably and are distinguished from different factors that cause misrepresentations within financial statements, such as unintended mistakes.

According to the "2020 Report to the Nations" published by the ACFE, the median cost per instance of occupational fraud around the world amounted to \$125,000 and the median period was 14 months. Although the frequency at which asset misappropriation and corruption occur tends to be greater than for financial statement fraud, the impact of the latter crime is significantly more severe, accounting for a median loss of \$954,000 and a median duration of 24 months [2].

The Center for Audit Quality indicted that managers commit financial statement fraud for a variety of reasons, such as personal benefit, the necessity to satisfy short-term financial goals, and the intention to hide bad news. Fraudulent financial statements can be manipulated so that they bear a convincing resemblance to non-fraudulent reports, and they can emerge in various distinct types [28]. Examples of frequently used methods are net income over- or understatements, falsified or understated revenues, hidden or overstated liabilities and expenses, inappropriate valuations of assets, and false disclosures [66]. Authorities directly reacted to the increased prevalence of corporate fraud by adopting new standards for accounting and auditing.

Nevertheless, financial statement irregularities are frequently observed and complicate the detection of fraudulent instances.

Detecting financial statement abnormalities is regarded as the duty of the auditor [18]. Despite the existing guidelines, the detection of indicators of fraud can be challenging. A 2020 report revealed that only a limited number of cases of fraud were identified by internal and external auditors, with rates of 15% and 4%, respectively [2]. Hence, there has been an increased focus on automated systems for the detection of financial statement fraud [70]. Such systems have specific importance for all groups of stakeholders: for investors - to facilitate qualified decisions, for auditing companies - to speed up and improve the accuracy of the audit, and for state regulators - to concentrate their investigations more effectively [1, 3]. Therefore, efforts have been made to develop smart systems designed to detect financial statement fraud. Previous studies have examined various quantitative financial and linguistic factors as indicators of financial irregularities [5, 15]. In the context of annual reporting, quantitative financial information is supported by textual information, such as the MD&A section, which aims at providing investors with an insight into the management‟s opinions regarding the organisation‟s future prospects. The language used in the MD&A section could reveal managers‟ cognitive processes and indicate fraudulent behaviour. Even though studies have emphasised the increasing significance of textual analysis of financial documentation, no research has focused on the application of state-of-the-art deep learning (DL) models for textual feature extraction. Furthermore, minimal research focused on the combination of financial and linguistic information for the intelligent prediction of financial statement fraud as well as on the interpretability of predictions, which is a crucial aspect to support auditors.

We aim to bridge this gap and contribute to the development of decision support systems for fraud detection by offering a state-of-the-art DL model for screening submitted reports based on a combination of financial and textual data. The proposed method exhibits superior predictive performance and allows the identification of early warning indicators (red-flags) on both the wordand sentence-level for the facilitation of the audit process. Additionally, we showcase the results of comparative modeling on different data types associated with financial reports and offer the alternative performance metrics that are centered around the cost imbalance of miss-classification errors.

## 2. Research design and contributions

In line with the above goals, we pose three research questions (RQ) that frame our research:

RQ 1: Does the novel combination of financial and text data (FIN+TXT) represent a more informative data type for fraud detection as compared to using FIN or TXT in isolation?

RQ 2: Can a state-of-the-art DL model outperform the bag-of-words (BOW) approach for textual feature extraction in combination with quantitative financial features?

RQ 3: Can the proposed DL model assist in interpreting textual features signaling

To answer these research questions, we select an array of classification models for detecting fraud based on different combinations of data. We consider techniques well established in the fraud detection literature including logistic regression (LR), support vector machines (SVM) and random forest (RF). Extreme gradient Boosting (XGB) and artificial neural networks (ANN), which have not been tested for statement fraud detection, are also part of the study. The main focus of the paper is textual data processing. We introduce a novel DL method called hierarchical attention network (HAN) to the community and demonstrate it distinctive features of providing accurate and interpretable fraud predictions. In line with previous research, the paper concentrates on the MD&A sections of annual reports filed by firms within the US with the Securities and Exchange Commission (SEC), which are referenced as annual reports on form 10-K. The SEC is the preeminent financial supervisory organisation that is responsible for monitoring financial reports of firms listed on the US stock exchange.

All selected models are trained on five different combinations of data contained in the statements submitted for audit: financial indicators (FIN), linguistic features (LING) of an MD&A text, financial and linguistic features (FIN + LING), the full text of an MD&A (TXT), full text and the financial indicators (FIN + TXT). We compare the predictive performance of the models with regard to their ability to distinguish fraud cases, for which we use traditional metrics like Accuracy and area under the Receiver Operating Curve (AUC) and metrics that reflect the imbalance in classification error, namely Sensitivity, F1-score, and F2-scores. The comparative study contributes to the empirical literature on fraud detection through i) expanding the set of considered classifiers, ii) offering previously unexplored data combinations, and iii) introducing new DL methods that provide accurate fraud forecasts and interpretative features.

Following RQ 3, we offer a novel fraud detection method that provides signaling tools for scholars and practitioners. We examine words considered "red-flags" by the RF feature importance method and the HAN attention layer output. Given that the use of words for signaling fraud may be the subject of manipulation, we offer sentence-level importance indicators as a remedy and demonstrate how the latter can guide the audit process.

## 3. Decision support for fraud detection

Previous studies proposed fraud detection systems and offered systematic literature reviews on fraud detection approaches [71, 56]. Table 1 depicts the status-quo in the field of financial fraud detection along four dimensions: the technique utilized, the type of data, the country of study, and the predictive performance terms of classification accuracy and other metrics. Prior research focused on financial variables and applied a range of modeling techniques, from LR to DL. Several authors experimented with linguistic variables. These variables were based on pre-determined lists of words associated with fraud or readability measures such as the average length of words and sentences, lexical diversity, and sentence complexity [29]. Few studies applied natural language processing (NLP) techniques representing the whole textual content of 10-K reports and, to the best of our knowledge, no previous study considered DL models for text analysis in financial statements. Furthermore, most studies examined the relation between linguistic aspects and fraudulent actions. Only Hajek and Henriques [26] combined them with financial data and showed that although financial variables are essential for the detection of fraud, it is possible to enhance the performance through the inclusion of linguistic data. However, their study was not targeted at evaluating the textual content of corporate annual reports and it did not include sophisticated techniques for mining text such as BOW and DL. The majority of existing research measured performance in terms of accuracy. Some studies also considered precision and recall. Additionally, most previous studies neglected model interpretability, which is crucial to support auditors during client selection or audit planning. Hajek and Henriques [26] pointed out the importance of transparent fraud detection models and derived interpretable "green-flag" values (for which fraud is likely absent). However, because the detection of fraudulent firms requires more complex non-interpretable models, no "red-flag" values (for which fraud is likely present) could be derived. We bridge this gap by suggesting the use of textual elements as "red-flags" for auditors. Given that the cost of failing to detect statement fraud is higher than that of incorrectly flagging a legitimate statement as fraudulent [26], focusing on early warning signs of fraud is necessary and can enhance the efficiency of auditing processes. In conclusion, this paper adds to the literature by offering an integrated approach for processing both textual and financial data using interpretable state-of-the-art DL methods. Furthermore, we provide a comprehensive evaluation of different modeling techniques using cost-sensitive metrics to account for the different severities of false alarms versus missed fraud cases.

<table><tr><td>Study</td><td>Data (fraud / no fraud)</td><td>Countr y</td><td>Features</td><td>Classifiers</td><td>Used metrics</td></tr><tr><td></td><td></td><td></td><td></td><td>BIN(90.3),LTNB(89.5),RF(87.5),</td><td></td></tr><tr><td>Hajek and Henriques [26]</td><td>311/311</td><td>US</td><td>FIN+ LING</td><td>Bag(87.1),JRIP(87.0),CART(86.2),</td><td>Acc, TPR, TNR, MC, F-score,AUC</td></tr><tr><td></td><td></td><td></td><td></td><td>C4.5(86.1),LMT(85.4),SVM(78.0),</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>MLP(77.9),AB(77.3),LR(74.5),NB(57.8)</td><td></td></tr><tr><td>Kim et al. [34]</td><td>788/2156</td><td>US</td><td>FIN</td><td>LR (88.4), SVM (87.7), BBN (82.5)</td><td>Acc, TPR, G-mean, Cost Matrices</td></tr><tr><td>Goel and Uzuner [25]</td><td>180/180</td><td>US</td><td>LING+POS tags</td><td>SVM(81.8)</td><td>Acc,TPR,FPR,Precision,F-score</td></tr><tr><td>Purda and Skillicorn [58]</td><td>1407/4708</td><td>US</td><td>TXT (BOW), top 200 RF words</td><td>SVM (AUC 89.0)</td><td>AUC, Fraud Probability</td></tr><tr><td>Throckmorton et al. [68]</td><td>41/1531</td><td>US</td><td>FIN+ LING from Conference Calls</td><td>GLRT (AUC 81.0)</td><td>AUC</td></tr><tr><td>Goel and Gangolly [23]</td><td>405/622</td><td>US</td><td>LING</td><td> $\chi^2$ statistics</td><td> $\chi^2$ statistics</td></tr><tr><td>Dechow et al. [15]</td><td>293/79358</td><td>US</td><td>FIN</td><td>LR(63.7)</td><td>Acc, TPR, FPR, FNR, min F-Score</td></tr><tr><td>Humpherys et al. [29]</td><td>101/101</td><td>US</td><td>LING</td><td>C4.5 (67.5), NB (61.5), SVM (65.8)</td><td>Acc, Precision, Recall, F-score</td></tr><tr><td>Glancy and Yadav [22]</td><td>11/20</td><td>US</td><td>TXT (BOW)</td><td>hierarchical clustering (83.9)</td><td>TP, TN, FP, FN, p-value</td></tr><tr><td>Perols [54]</td><td>51/15934</td><td>US</td><td>FIN</td><td>SVM(MC 0.0025), LR(0.0026), C4.5 (0.0028), bagging(0.0028), DNN(0.0030)</td><td>Fraud Probability and MC</td></tr><tr><td>Cecchini et al. [12]</td><td>61/61</td><td>US</td><td>LING</td><td>SVM (82.0)</td><td>AUC, TPR, FPR, FNR</td></tr><tr><td>Goel et al. [24]</td><td>126/622</td><td>US</td><td>LING+TX T (BOW)</td><td>SVM(89.5), NB(55.28%)</td><td>Acc, TPR, FPR, Precision, F-score</td></tr><tr><td>Lin et al. [42]</td><td>127/447</td><td>Taiwan</td><td>FIN</td><td>DNN (92.8), CART (90.3), LR (88.5)</td><td>Acc, FPR, FNR, MC</td></tr><tr><td>Ravisankar et al. [61]</td><td>101/101</td><td>China</td><td>FIN</td><td>PNN (98.1), GP (94.1), GMDH (93.0),</td><td>Acc, TPR, TNR, AUC</td></tr><tr><td></td><td></td><td></td><td></td><td>DNN (78.8), SVM (73.4)</td><td></td></tr></table>

Table 1: Analysis of classifier comparisons in financial statement fraud detection

FIN – financial data, LING – linguistic data (word category frequency counts, readability and complexity scores, etc.), TXT - text data, BOW–bag-of-words, POS – part of speech tags (nouns, verbs, adjectives), BBN – Bayesian belief network, NB-Naive Bayes, DTNB - NB with the induction of decision tables, CART–classification and regression tree, LMT - logistic model trees, MLP - multi-layer network, Bag-Bagging, AB - AdaboostM1, GMDH – group method data handling, GP–genetic programming, GLRT - generalized likelihood ratio test, LR–logistic regression, DNN – deep neural network, PNN – probabilistic neural network, RF – random forest, SVM – support vector machine, Acc - Accuracy, AUC – area under the ROC curve, MC - misclassification cost, TPR - true positive rate, TNR - true negative rate, FPR - false-positive rate, FNR - false-negative rate.

## 3.1. Text-based indicators

Textual analysis is frequently employed for the examination of corporate disclosures. Linguistic features have been utilized in the analysis of corporate conference calls [38], earnings announcements [14], media reports [67] and annual reports [44, 11]. Several studies have concentrated on the MD&A section to examine the language used in annual reports [19, 12, 29]. The MD&A is especially relevance as it offers investors the possibility of reviewing the performance of the company as well as its future potential from the perspective of management. This part also provides scope for the management‟s opinions on the primary threats to the business and necessary actions.

A positive factor that renders the textual information contained within annual reports conducive to the detection of fraud is that it is not subject to the same degree of regulation as financial information, thus providing the organisation‟s management more opportunities when divulging textual data [29]. Given that MD&A involves predictions, presumptions, and decisions, management might be tempted to manipulate the information in order to present the organisation in a more favourable light [51]. In addition to manipulating data, management could purposely exclude important information thus leading to the same outcome. Examples for risk factors associated with financial statement fraud can be a poor financial performance, a pressure for management to meet the requirements or expectations of third parties such as investors, or a need to obtain financing or to minimize reported earnings for tax-motivated reasons. Breiman et al. [9] conducted analysis on infamous examples such as WorldCom and Enron, and determined that senior managers participated in, encouraged, approved, and had knowledge of the fraudulent activities in most cases. Social psychology research suggests that the emotions and cognitive processes of managers who intend to conceal the real situation could indicate specific linguistic cues that facilitate the identification of fraud [16]. Therefore, prior work has emphasised the increasing significance of textual analysis of financial documentation.

Studies that analyzes the use of language within annual reports usually adopts one of two strategies [40]. The first strategy draws on research in linguistics and psychology and is dependent on pre-determined lists of words that have an association with a specific sentiment, like negativity, optimism, deceptiveness, or ambiguity. Loughran and Mcdonald [44] (L&M) demonstrated that if these lists are adapted to the financial domain, it is possible to determine relationships among financial-negative, financial-uncertain, and financial-litigious word lists and 10-k filing returns, trading volume, return volatility, fraud, material weakness, and unexpected earnings. As it was developed for analyzing 10-K text, the L&M sentiment word lists have been broadly employed in fraud-detection research [26]. Accordingly, the L&M word lists enters this study as a benchmark to DL approaches for extracting features from the MD&A section of 10-Ks. Other researchers based their approaches for detecting fraud on word lists that indicate positive, negative or neutral emotions [29, 23] or more specifically anger, anxiety, and negativity according to the definitions supplied by the Linguistic Inquiry and Word Count dictionary [29, 38, 52].

The second strategy relies on ML to extract informative features for automatic differentiation between fraudulent and non-fraudulent texts. Li [40] contended that this method has various benefits compared with predetermined lists of words and cues, including the fact that no adaptation to the business context is required. ML algorithms have been used in the detection of financial statement fraud by several researchers, such as Cecchini et al. [12], Hajek and Henriques [26], Humpherys et al. [29], Goel and Uzuner [25], Goel et al. [24], Glancy and Yadav [22], and

Purda and Skillicorn [58]. Some attempts to integrate different types of data have also been made. Purda and Skillicorn [58] compared a language-based method to detect fraud based on SVM to the financial measures proposed by Dechow et al. [15], and concluded that these approaches are complementary. The methods displayed low forecast correlation and identified specific types of fraud that the other could not detect. This finding motivates us to combine financial variables and linguistic variables to complement each other in the detection of statement fraud.

The study of Hajek and Henriques [26] is closest to this work as they combined financial ratios with linguistic variables from annual reports of US firms and employed a variety of Henriques [26] was not targeted at evaluating the textual content of corporate annual reports. Hence, it did not include modern NLP approaches such as deep learning-based feature extraction.

## 3.2. Methods and evaluation metrics

Prior work has tested a variety of statistical fraud detection models including ANNs, Decision Trees (DT), SVM, evolutionary algorithms, and text analysis [26]. The BOW technique was frequently adopted for the extraction of the linguistic properties of financial documentation. The BOW approach represents a document by a vector of word counts that appear in it. as the input for the ML algorithms. This method does not consider the grammar, context, and structure of sentences and could be overly simple in terms of uncovering the real sense of the text [38]. A different technique for analyzing text is DL. Deep ANN are able to extract high-level features from unstructured data automatically. Textual analysis models based on DL can “learn” the specific patterns that underpin the text, “understand” its meaning and subsequently output abstract aspects gleaned from the text. Hence, they resolve some of the problems associated with the BOW technique, including the extraction of contextual information from documents. Due to their capacity to deal with sequences with distinct lengths, ANN have shown excellent results in recent studies on text processing [76]. Despite their achievements in NLP, there has been limited focus on the application of state-of-the-art DL methods to the analysis of a financial text, with the notable exception of [36]. For an adoption in practice, DK models should not only be precise, but also interpretable [37, 28]. However, the majority of systems designed to detect fraud reported by researchers aim to maximise the prediction accuracy, while disregarding how transparent they are [26]. This factor has particular significance as the development of interpretable models is critical for supporting the investigation procedure in auditing.

## 4. Methodology

The objective of this study is to devise a fraud detection system that classifies annual reports. While financial and linguistic variables represent structured tabular data and require no extensive preprocessing, the unstructured text data has to be transformed into a numeric format, which preserves its informative content and facilitates algorithmic processing. To achieve the latter, words are embedded as numeric vectors. The field of NLP has proposed various ways to construct such vectors. We consider two methods for text representation: frequency-based BOW embeddings and prediction-based neural embeddings (word2vec). An advantage of the BOW approach, which has been used in prior work on financial statement fraud (see Table1), is its simplicity. However, BOW represents a set of words without grammar and disrupts word order. Unlike BOW, the application of DL is still relatively new to the area of regtech (management of regulatory processes within the financial industry through technology). Therefore, the following subsections clarify neural word embeddings and address the DL components of the proposed HAN model.

## 4.1. Neural Embeddings

The BOW model represents every word as a feature. The amount of features denotes the typically only represents a small proportion of the overall amount of unique words within the whole corpus, BOW document vectors are very sparse. A more advanced model for creating lower dimensional, dense embeddings of words is word2vec. As opposed to BOW, word2vec embeddings enable words that have similar meanings to be given similar vector representations and capture the syntactic and semantic similarities. Word2vec [48] is an example of a NN model that is capable of learning word representations from a large corpus. Every word within the corpus is mapped to a vector of 50 to 300 dimensions. Mikolov et al. [48] demonstrated that such vectors offer advanced capabilities to measure the semantic and syntactic similarities between words. The generated word embeddings are a suitable input for text mining algorithms based on DL, as will be observed in the next part. They constitute the first layer of the model and allow further processing of text input within the DL architecture.

The initial word2vec algorithm is followed by GloVe [53], FastText [8], and GPT-2 [59], as well as the appearance of publicly available sets of pre-trained embeddings that are acquired by applying the above-mentioned algorithms on large text corpora. Pre-trained word embeddings accelerate training DL models and were successfully used in numerous NLP tasks. We apply several types of pre-trained embeddings for HAN model and a neural network with a bidirectional Gated Recurrent Unit (GRU) layer that serves as a benchmark from the field of DL. As a result of a performance-based selection, the HAN model is built with word2vec embeddings with 300 neurons, trained on the Google News corpus, with a vocabulary size of 3 million words. The DL benchmark is used with the GPT-2 pre-trained embeddings from the WebText, offered by Radford et al. [59], as they arguable constitute the current state-of-the-art language model. The DL benchmark model is thus referred to as GPT-2 and is used together with the attention mechanism, discussed further.

## 4.2. Deep learning

After representing unstructured textual data in a numerical format, it can be used for predictive modeling. Conventional methods for classifying text involve the representation of sparse lexical features, like TF-IDF, and subsequently utilize a linear model or kernel techniques upon this representation [30].

Recently, DL has incorporated new techniques, including Convolutional Neural Networks (CNN) [32] and Recurrent Neural Networks (RNN) [27] for learning textual representations [73]. The RNN architecture allows retaining the input sequence, which made it widely used for natural language understanding, language generation, and video processing [47, 31]. An LSTM is a special type of RNN, comprised of various gates determining whether the information is kept, forgotten or updated and enabling long-term dependencies to be learned by the model [27]. An LSTM retains or modifies previous information on a selective basis and stores important information in a separate cell, which acts as a memory [69]. Consequently, overwriting of important information by the new inputs does not occur, it can persist for extended periods.

## 4.3. Hierarchical Attention Network

More advanced DL approaches also address hierarchical patterns of language such as the hierarchy between words, sentences, and documents. Some methods have covered the hierarchical construction of documents [74, 60]. The specific contexts of words and sentences, whereby the meaning of a word or sentence could change depending on the document, is a comparatively new concept for the process of text classification, and the HAN was developed to address this issue [72]. When computing the document encoding, HAN firstly detects the words that have importance within a sentence, and subsequently, those sentences that have importance within a document while considering the context (see Figure 1). The model recognizes the fact that an occurrence of a word may be significant when found in a particular sentence, whereas another occurrence of that word may not be important in another sentence (context).

## Figure 1: HAN Architecture. Image based on Yang et al. [72]

The HAN builds a document representation via the initial construction of sentence vectors based on words followed by the aggr representation through the application of $\therefore$ attention mechanism. The model consists of an encoder that generates relevant contexts and an attention mechanism, which calculates importance weights. The same algorithms are consecutively implemented at the word level and then at the sentence level.

Word Level. The input is transformed into structured tokens $w _ { i t }$ that denote word i in sentence $t \in [ 1 , T ]$ . Tokens are further passed through a pre-trained embedding matrix $W _ { e }$ that allocates multidimensional vectors ${ x _ { i t } = W _ { e } w _ { i t } }$ to every token. As a result, words are denoted in numerical format by $x _ { i t }$ as a projection of the word in a continuous vector space.

Word Encoder. The vectorized tokens represent the inputs for the following layer. While Yang et al. [72] employed GRU for encoding, we use LSTM as it showed better performance on the large text sequences at hand [13]. In the context of the current model, a bidirectional LSTM is implemented to obtain the annotations of words. The model consists of two uni-directional LSTMs, whose parameters are different apart from the word embedding matrix. Processing of the sentences in the initial forward LSTM occurs in a left to the right manner, whereas in the backward LSTM, sentences are processed from right to left. The pair of sentence embeddings are concatenated at every time step t to acquire the internal representation of the bi-directional LSTM $h _ { i t }$

Word Attention. The annotations $h _ { i t }$ construct the input for the attention mechanism that learns enhanced annotations denoted by $u _ { i t }$ . Additionally, the tanh function adjusts the input values so that they fall in the range of -1 to 1 and maps zero to near-zero. The newly generated annotations are then multiplied again with a trainable context vector $u _ { { _ w } }$ and subsequently normalized to an importance weight per word $\alpha _ { i t }$ via a softmax function. As part of the training procedure, the word context vector $u _ { { _ w } }$ is initialized randomly and concurrently learned. The total of these importance weights concatenated with the already computed context annotations is defined as the sentence vector $s _ { i }$ :

$$
u _ {i t} = \tanh (W _ {w} h _ {i t} + b _ {w})\tag{1}
$$

$$
\alpha_ {i t} = \frac {\exp \left(u _ {i t} ^ {T} u _ {w}\right)}{\sum_ {t} \exp \left(u _ {i t} ^ {T} u _ {w}\right)}\tag{2}
$$

$$
s _ {i} = \sum_ {t} x _ {i t} h _ {i t}\tag{3}
$$

Sentence Level and Sentence Encoder. Subsequently, the entire network is run at the sentence level using the same fundamental process used for the word level. An embedding layer is not required as $s _ { i }$ of sentence contexts is performed using a bi-directional LSTM, which analyzes the document in both forward and backward directions:

$$
\vec {h} _ {i} = \overrightarrow {L S T M} (s _ {i}), i \in [ 1, L ]\tag{4}
$$

$$
\overleftarrow {h} _ {i} = \overleftarrow {L S T M} (s _ {i}), i \in [ T, 1 ]\tag{5}
$$

$$
h _ {i} = [ \vec {h} _ {i}, \vec {h} _ {i} ]\tag{6}
$$

Sentence Attention. For rewarding sentences that are indicators of the correct document classification, the attention mechanism is applied once again along with a sentence-level context vector $u _ { s }$ , which is utilized to measure the sentence importance. Both trainable weights and biases are initialized randomly and concurrently learned during the training procedure, thus yielding:

$$
u _ {i} = \tanh (W _ {s} h _ {i} + b _ {s})\tag{7}
$$

$$
\alpha_ {i} = \frac {\exp (u _ {i} ^ {T} u _ {s})}{\sum_ {i} \exp (u _ {i} ^ {T} u _ {s})}\tag{8}
$$

$$
d = \sum_ {i} \alpha_ {i} h _ {i}\tag{9}
$$

where $d$ denotes the document vector summarising all the information contained within each of the document‟s sentences. Finally, the document vector d is a high-level representation of the overall document and can be utilized as features for document classification to generate output vector $\hat { y }$ :

$$
\hat {y} = \operatorname{softmax} \left(W _ {c} d + b _ {c}\right)\tag{10}
$$

$\hat { y }$ $\dot { \boldsymbol { \mathbf { \rho } } } _ { \mathcal { k } }$ model the probability that $d$

The application of the HAN follows the application of Kränkel and Lee [35]. Training of the DL model is performed on the training data set using both textual and quantitative features. Hence, the textual data acquired in the previous section is concatenated with the financial ratios. The model is employed to predict fraud $\boldsymbol { \mathrm { f } }$ robabilities of annual statements in the corresponding validation and test partitions, which were constructed with random sampling with stratification. Figure 2 shows the architecture of $\bf { U } \cdot \Pi _ { \mathrm { 1 } } \bf { i } \bf { A } \cal { N }$ based fraud detection model and the output dimensions of each layer.

Figure 2: Architecture of the HAN based Fraud Detection Model

The LSTM layer consists of 150 neurons, a HAN dense dimension of 200, and a last dense layer dimension of 6. In this case, a combination of forward and backward LSTMs gives 300 dimensions for word and sentence annotation. The last layer of the HAN involves the application of dropout regularization to prevent over-fitting. In a final step, the resulting document-representation of dimension 200 is concatenated with 47 financial ratios and inputted to a dense layer before running through a softmax function that outputs the fraud probabilities. For training, a batch size of 32 and 17 epochs was used after hyperparameter tuning on the train validation set.

## 4.4. Evaluation metrics

Financial statement fraud detection is approached as a binary classification problem with four possible outcomes: True positive (TP) denotes the correct classification of a fraud case, false negative (FN) denotes the incorrect classification of a fraud case as non-fraud, true negative (TN) denotes the correct classification of a non-fraud case, and false positive (FP) denotes the incorrect classification of a non-fraud case as fraud.

To estimate predictive performance, many previous studies considered a combination of measures such as accuracy, sensitivity (also called TP rate or recall), specificity (also called TN rate), precision, and F1-score [71]. In this study, model performance is evaluated by the AUC, sensitivity, specificity, F1-score, F2-score, and accuracy.

The F-score is a combination of precision (correct classification of fraud cases as a percentage of all instances classified as fraudulent) and sensitivity (indicates how many fraudulent instances the classifier misses). It measures how precise and how robust the models classify fraudulent cases:

$$
F _ {\beta} - \text { score } = (1 + \beta^ {2}) \times - \frac {\text { precision } \times \text { sensitivity }}{(p ^ {2} \times \text { precision }) + \text { sensitivity }}\tag{11}
$$

Prior research emphasized that a higher sensitivity is preferred to higher specificity in financial statement fraud detection. Nevertheless, the majority of models have exhibited higher performance in detecting truthful transactions in comparison to those that are fraudulent [71, 61]. An explanation for this preference is that FN rate (type II error) and FP rate (type I error) result in different misclassification costs (MC). Hajek and Henriques [26] estimated the cost of failing to detect fraudulent statements (type II error) to be twice as high as the cost of incorrectly classifying fraudulent statements (type I error). Hence, effective models should concentrate on high sensitivity and classify correctly as many positive samples as possible, rather than maximizing the number of correct classifications. To that end, this study employs the F2-score in addition to the F1-score (harmonic mean of precision and sensitivity), as it weights sensitivity higher than precision and is, therefore, more suitable for fraud detection. The AUC captures the ability of a model to rank fraud and non-fraud cases in the right order. The higher the AUC, the better the model can distinguish between fraud and non-fraud cases. Being robust toward imbalanced class distributions, the AUC is preferred to accuracy in fraud detection [68, 58] and also used in this study.

Calculating F1- and F2-scores requires a cutoff to threshold model-based fraud probabilities. We select the threshold that maximizes the difference between sensitivity and FP rate and use it to evaluate the classification results. For the HAN model, the optimal threshold is set at 0.03, implying that a statement is classified as fraudulent if its fraud probability is higher than 3%.

## 5. Data

Fraud detection is a challenging task because of the low number of known fraud cases. A severe imbalance between the positive and the negative class impedes classification. For example, the proportion of statements that were fraudulent and non-fraudulent in the annual reports submitted to the SEC for the period from 1999 to 2019 was 1:250. In past research, the number of firms that committed fraud contained in the data varied between 12 and 788 [68, 34]. The data used here consists of 208 fraudulent and 7 341 non-fraud cases, making it the largest data set with a textual component so far (c.f., Table1). The data set consists of US companies‟ annual financial reports (10-K filings) that are publicly available through the EDGAR database of the SEC‟s website <sup>1</sup> and quantitative financial data, sourced from the Compustat database 2

## 5.1. Labeling

Companies submit yearly reports that undergo an audit. Labeling these reports requires several filtering decisions: when can a report be considered fraudulent and what type of fraud "fraudulent" if the company that filed it was convicted. The SEC publishes statements called "Accounting and Auditing Enforcement Releases" (AAER) that describe financial reporting related enforcement actions taken against companies that violated the reporting rules <sup>3</sup>. SEC concentrates on cases with high importance and applies enforcement actions where the evidence of manipulation is sufficiently robust [26, 33]. This provides a high degree of trust to this source. Labeling reports based on the AAER offers simplicity and consistency with easy replication and avoids possible bias from a subjective categorization. Following [58], we select the AAERs concerning litigations issued during the period from 1999 to 2019 with identified manipulation instances between the year 1995 and 2016 that discuss the words "fraud", "fraudulent", "anti-fraud" and "defraud" as well as "annual reports" or "10-K". Addressing the second question, we follow [12, 24, 29, 58, 26] and focus on binary fraud classification. This implies that we do not distinguish between truthful and unintentionally misstated annual reports. The resulting data set contains 187 869 annual reports filed between 1993 and 2019, with 774 firm-years subject to enforcement actions. However, due to missing entries and mismatches in existing CIK indexation, the final data set is reduced to 7 757 firm-year observations with 208 fraud and 7 549 non-fraud

## 5.2. Text data

The MD&A section constitutes the primary source of raw text data in this study. In selection of these features is influenced $^ { \textsf { \textsf { F } } _ { \textsf { y \textsf { I } } } }$ ast studies that demonstrated several patterns of fraudulent agents, like an increased likelihood of using words that indicate negativity [68, 49], absence of process ownership implying lack of assurance and resulting in statements containing less certainty [38] or an average of three times more positive sentiment and four times more negative sentiment in comparison to honest reports Goel and Uzuner [25]. Additionally, the general tone (sentiment) and the proportion of constraining words, were included by Hajek and Henriques [26], Loughran and Mcdonald [44], and Bodnaruk et al. [7]. Lastly, the average length of sentence, the proportion of compound words, and the fog index are incorporated as measures of complexity and legibility because prior work suggests that reports produced by misstating firms had reduced readability [29, 39].

## 5.3. Quantitative data

Along with text features, we used 47 quantitative financial predictors (described in the online appendix), which are capable of capturing financial distress as well as managerial motivations to misrepresent the performance of the firm. Past studies have presented robust theoretical evidence supporting the utilization of financial variables [20, 64, 1, 26]. Following the guidelines of existing research, the financial ratios and balance sheet variables presented in the online appendix are extracted from Compustat, based on formulas presented by Dechow et al. [15] and Beneish [6]. Financial variables include indicators like total assets (adopted as a proxy for company size [68, 4]), profitability ratios [26], accounts receivable and inventories as non-cash working capital drivers [1, 12, 55]. Additionally, a reduced ratio of sales general and administrative expenses (SGA) to revenues (SGAI) is found to signalize fraud [1]. Missing values are imputed using the RF algorithm. However, observations with more than 50% of the variables missing are excluded.

## 5.4. Imbalance treatment

The majority of previous research has balanced the fraud and non-fraud cases in a data set using undersampling [26, 29, 61]. We follow this approach and consider a fraud-to-non-fraud-ratio of 1:4, which reflects the fact that the majority of firms have no involvement in fraudulent behaviour. Both year and sector are utilized for balancing, in order to take into account different economic conditions, change in regulation, as well as to eradicate any differences across distinct sectors [29, 34]. The latter is extracted with $\mathrm { \Omega } _ { { \mathrm { L } } , \mathrm { \Omega } } \mathrm { \Omega } \stackrel { \mathrm { S I C } } { \mathrm { \Omega } }$ code [65] and is of particular importance for text mining, as the utilization of words within financial documentation could differ according to the sector. The resulting balanced data set consists of 1 163 reports, out of which 201 are fraudulent, and 962 are non-fraudulent annual reports. In the years 2002 to 2004 more financial misstatements than in other years can be observed. This could be attributed to the tightened regulations after the big fraud scandals in 2001 and the resulting implementation of the Sarbanes-Oxley Act (SOX) in 2002. Also, fewer misstatements are noted in recent years since the average period between the end of the fraud and the publication of an AAER is three years [57].

## 6. Classification results

We answer RQ 1 and 2 by means of empirical analysis and compare a set of classification models in terms of their fraud detection performance. The models generate fraud classifications based on financial indicators, linguistic features of reports, the reports‟ text, and combinations of these groups of features. Table 2 reports corresponding results from the out-of-sample test set. The baseline accuracy of classifying all cases of the test set as non-fraudulent (majority class) is

<table><tr><td colspan="7">Finance data (FIN)</td><td></td><td></td></tr><tr><td></td><td>AUC</td><td>Sensitivity</td><td>Specificity</td><td>F1-score</td><td>F2-score</td><td>Accuracy</td><td></td><td></td></tr><tr><td>LR</td><td>0.7620</td><td>0.6833</td><td>0.7543</td><td>0.4767</td><td>0.7480</td><td>0.8252</td><td></td><td></td></tr><tr><td>RF</td><td>0.8609</td><td>0.7666</td><td>0.7889</td><td>0.5508</td><td>0.7892</td><td>0.8653</td><td></td><td></td></tr><tr><td>SVM</td><td>0.7561</td><td>0.6166</td><td>0.7820</td><td>0.4625</td><td>0.7595</td><td>0.8280</td><td></td><td></td></tr><tr><td>XGB</td><td>0.8470</td><td>0.6660</td><td>0.8719</td><td>0.5839</td><td>0.8391</td><td>0.8481</td><td></td><td></td></tr><tr><td>ANN</td><td>0.7564</td><td>0.7833</td><td>0.6574</td><td>0.4563</td><td>0.6835</td><td>0.6790</td><td></td><td></td></tr><tr><td colspan="7">Linguistics data (LING)</td><td colspan="2">Comparison to FIN</td></tr><tr><td></td><td>AUC</td><td>Sensitivity</td><td>Specificity</td><td>F1-score</td><td>F2-score</td><td>Accuracy</td><td>Delta AUC</td><td>Delta F1</td></tr><tr><td>LR</td><td>0.6719</td><td>0.7000</td><td>0.6193</td><td>0.3962</td><td>0.6398</td><td>0.8280</td><td>-0.0901</td><td>-0.0805</td></tr><tr><td>RF</td><td>0.7713</td><td>0.7500</td><td>0.7197</td><td>0.4339</td><td>0.7302</td><td>0.8424</td><td>-0.0896</td><td>-0.0669</td></tr><tr><td>SVM</td><td>0.7406</td><td>0.7000</td><td>0.6747</td><td>0.4285</td><td>0.6857</td><td>0.8280</td><td>-0.0155</td><td>-0.0340</td></tr><tr><td>XGB</td><td>0.7219</td><td>0.3666</td><td>0.9446</td><td>0.4489</td><td>0.8385</td><td>0.8338</td><td>-0.1251</td><td>-0.1350</td></tr><tr><td>ANN</td><td>0.6782</td><td>0.6333</td><td>0.6747</td><td>0.3958</td><td>0.6758</td><td>0.6676</td><td>-0.0782</td><td>-0.0605</td></tr><tr><td colspan="7">Finance data + Linguistics data (FIN + LING)</td><td colspan="2">Comparison to FIN</td></tr><tr><td></td><td>AUC</td><td>Sensitivity</td><td>Specificity</td><td>F1-score</td><td>F2-score</td><td>Accuracy</td><td>Delta AUC</td><td>Delta F1</td></tr><tr><td>LR</td><td>0.7682</td><td>0.7666</td><td>0.6782</td><td>0.4623</td><td>0.6984</td><td>0.8280</td><td>0.0062</td><td>-0.0144</td></tr><tr><td>RF</td><td>0.8606</td><td>0.7666</td><td>0.7543</td><td>0.5197</td><td>0.7610</td><td>0.8567</td><td>-0.0003</td><td>-0.0311</td></tr><tr><td>SVM</td><td>0.7973</td><td>0.7166</td><td>0.7439</td><td>0.4858</td><td>0.7448</td><td>0.8280</td><td>0.0567</td><td>0.0573</td></tr><tr><td>XGB</td><td>0.8651</td><td>0.8166</td><td>0.7543</td><td>0.5444</td><td>0.7687</td><td>0.8653</td><td>0.0181</td><td>-0.0395</td></tr><tr><td>ANN</td><td>0.7733</td><td>0.8333</td><td>0.6228</td><td>0.4566</td><td>0.6614</td><td>0.6590</td><td>0.0169</td><td>0.0003</td></tr><tr><td colspan="7">Text data, TF-IDF (TXT)</td><td colspan="2">Comparison to LING</td></tr><tr><td></td><td>AUC</td><td>Sensitivity</td><td>Specificity</td><td>F1-score</td><td>F2-score</td><td>Accuracy</td><td>Delta AUC</td><td>Delta F1</td></tr><tr><td>LR</td><td>0.8371</td><td>0.7333</td><td>0.8269</td><td>0.5714</td><td>0.8145</td><td>0.8281</td><td>0.1652</td><td>0.1752</td></tr><tr><td>RF</td><td>0.8740</td><td>0.7166</td><td>0.9377</td><td>0.7107</td><td>0.8998</td><td>0.8681</td><td>0.1027</td><td>0.2268</td></tr><tr><td>SVM</td><td>0.8836</td><td>0.8382</td><td>0.7544</td><td>0.5876</td><td>0.7731</td><td>0.8796</td><td>0.1275</td><td>0.1251</td></tr><tr><td>XGB</td><td>0.8785</td><td>0.7660</td><td>0.8581</td><td>0.6258</td><td>0.8451</td><td>0.8853</td><td>0.1566</td><td>0.1769</td></tr><tr><td>ANN</td><td>0.8829</td><td>0.7121</td><td>0.9434</td><td>0.7286</td><td>0.8993</td><td>0.8990</td><td>0.2047</td><td>0.3328</td></tr><tr><td>HAN</td><td>0.9108</td><td>0.8000</td><td>0.8896</td><td>0.5744</td><td>0.7982</td><td>0.8457</td><td></td><td></td></tr><tr><td>GPT-2+Att n</td><td>0.7729</td><td>0.7619</td><td>0.6697</td><td>0.4423</td><td>0.6905</td><td>0.6484</td><td></td><td></td></tr><tr><td colspan="7">Finance data + Text data, TF-IDF (FIN + TXT)</td><td colspan="2">Comparison to FIN + LING</td></tr><tr><td></td><td>AUC</td><td>Sensitivity</td><td>Specificity</td><td>F1-score</td><td>F2-score</td><td>Accuracy</td><td>Delta AUC</td><td>Delta F1</td></tr><tr><td>LR</td><td>0.8598</td><td>0.7833</td><td>0.7854</td><td>0.5562</td><td>0.7890</td><td>0.8424</td><td>0.0916</td><td>-0.0795</td></tr><tr><td>RF</td><td>0.8797</td><td>0.6660</td><td>0.9550</td><td>0.7079</td><td>0.9043</td><td>0.8739</td><td>0.0191</td><td>-0.1571</td></tr><tr><td>SVM</td><td>0.8902</td><td>0.7833</td><td>0.8961</td><td>0.6361</td><td>0.8784</td><td>0.8280</td><td>0.0929</td><td>-0.2576</td></tr><tr><td>XGB</td><td>0.8983</td><td>0.7000</td><td>0.9653</td><td>0.7500</td><td>0.9187</td><td>0.9083</td><td>0.0332</td><td>-0.1661</td></tr><tr><td>ANN</td><td>0.8911</td><td>0.7460</td><td>0.9405</td><td>0.7401</td><td>0.9055</td><td>0.9054</td><td>0.1178</td><td>-0.2838</td></tr><tr><td>HAN</td><td>0.9264</td><td>0.9000</td><td>0.8296</td><td>0.6506</td><td>0.8361</td><td>0.8457</td><td></td><td></td></tr><tr><td>GPT-2+Att n</td><td>0.7776</td><td>0.7678</td><td>0.6791</td><td>0.4455</td><td>0.6991</td><td>0.6934</td><td></td><td></td></tr></table>

Table 2: Comparative performance of selected binary classifiers on the different types of test data. The baseline accuracy is 0.8281

## 6.1. Modeling of financial data

Modeling using financial data (FIN) has been the most popular approach (Table 1). The approach serves this study as a benchmark, to which we compare modeling on linguistic features (LING) and the combination of both (FIN + LING). The last two columns of Table 2 show the results of the comparison. In terms of AUC and accuracy, the tree-based models RF [10] and XGB appear to excel at predicting fraud on FIN, indicating a non-linear dependency between financial indicators and the fraud status of a report. This result is in line with Liu et al. [43] who showed that

RF performed especially well in case of high-dimensional financial fraud data. Hajek and Henriques [26] also reported an accuracy of 88.1% on FIN data and concluded that the ensemble of tree-based algorithms is superior to SVM, LR and ANN due to a relatively low dimensionality achieved during feature selection. The predictive performance aligns with the results of Kim et al. [34], offering the LR and SVM models as the most accurate. Lin et al. [42] and Ravisankar et al. [61] showcased that the DNN models (ANN with more than one hidden layer) outperform LR and SVM, offering an accuracy higher by around 4.5%. The SVM is a widely recognized model and was applied both for fraud detection [54] and in other fields [17]. However, the results show that less impressive predictive performance but proved to be the most efficient in terms of sensitivity. However, for model evaluation, a balanced indicator like F1- and F2-scores provide a better perspective. These metrics suggest XGB to outperform other models. XGB represents an advancement in the in the field of ML, its high performance is noteworthy since it was not considered in prior work on fraud detection. Given the much higher cost of missing actual fraud indicator of model performance. Therefore, we emphasize the F2-score together with the AUC, which allows the tuning of the threshold.

## 6.2. Modeling of linguistic data

The modeling on linguistic data (LING) was the first step towards including text in fraud detection. The earlier experiments by Cecchini et al. [12], Humpherys et al. [29] and Goel et al. [24] employed SVM and achieved accuracy of 82%, 65.8%, and 89.5% respectively. The latter additionally included the BOW method that we will discuss further. Our modeling falls in line with the previous work and exhibits SVM as the second strongest predictor, yielding an AUC of 74% and accuracy of 82%. RF remained the most reliable predictor with the highest AUC, accuracy, and F2-score. Modeling done solely on LING will allow us to assess the degree to which both sources of data contribute to accurate classification. In line with Hajek and Henriques [26], all models exhibit higher performance on FIN data than on LING data solely, leading to the conclusion that financial covariates have more predictive power than linguistic variables. However, the performance differences are not substantial and suggest a strong relationship between linguistic features and fraudulent behavior, which agrees with previous studies.

Following the ideas of Hajek2017MiningMethods, we combine FIN and LING data to evaluate if the classifier can make use of both data sources. Our results differ in terms of the leading models, with RF and XGB offering the highest AUCs of 86%. XGB is showing an improvement, performing well on FIN data, falling back a little in the LING set up but making better use of the combined input. Once again we observe the superior performance of XGB in terms of F2-score with 76.87% followed closely by 76.10% of RF and 74.48% of SVM, which once again advocates for the usefulness of advanced ML methods for practical tasks. Interestingly, for the rest of classifiers, the accuracy dropped a little in comparison to FIN, but the AUCs improved (with a minor exception for RF). This serves as an indication that LING and FIN data combined may provide conflicting signals to the classifier. However, the data mix is a definite improvement as it performance.

## 6.3. Modeling of text data

Researchers have been taking a step forward from aggregated linguistic features in an attempt to derive more predictive power from the vast amounts of text contained in annual reports. We offer the advanced methods of NLP, previously unexplored for fraud detection, and compare them to the performance of more traditional models. Goel et al. [24], Glancy and Yadav [22] and Purda and Skillicorn [58] applied the BOW model to perform modeling on text data, while Goel and Uzuner [25] made use of part-of-speech tagging. They utilized SVM and hierarchical clustering as classifiers and achieved accuracies of 89.5%, 83.4%, 89%, and 81.8%, respectively.

Table 2 offers an overview of the modeling results, starting with purely textual input (TXT) and continuing with text enhanced by financial data (FIN+TXT). Two new DL methods are included in TXT modeling, namely HAN and GPT-2. While traditional benchmarks take the TF-IDF transformations of word input, the DL models make use of pre-trained embeddings. We can observe that modeling on TXT improves all models in comparison to LING, with the largest AUC delta of 0.2 in the case of ANN. This increase can be attributed to the richer input of the actual MD&A content. While the more basic feature input of the LING models solely incorporated linguistic information (e.g., frequency counts of word categories based on LM word lists, readability and complexity ratios, etc.) the textual input (TXT) is based on advanced text mining techniques and vector space representations containing the information of the whole MD&A content (TF-IDF based embedding), as well as grammar, context, and structure of sentences (DL based embeddings). ANN demonstrates the highest accuracy, 89%, and the best F1- and F2-scores, which constitutes a strong signal that the neural network architecture is a favorable candidate for the task, regardless of the BOW input. Given the complexity of text processing, ANN proves its capacity to pick up on complex relationships between the target and explanatory variables. The improvement is also visible for the F2-score of 89.93% that closely follows that of RF (89.98%). It is interesting to compare the BOW-based ANN with GPT-2 and HAN, all of which represent a NN architecture. GPT-2 performs better on TXT than any other model on LING. Though it fails to show superior accuracy, its sensitivity is one of the highest, leading to the conclusion that with some threshold adjustment, it could provide better predictive performance than other models like LR or tree-based models. This example underlines the potential gains of implementing the new DL methods that allow superior insights into unstructured data. Unlike BOW-based benchmarks, embeddings-based HAN and GPT-2 retained the structure and context of the input. HAN showed sensitivity is exceeding those of all other benchmarks except SVM, making it a promising model for fraud detection. The appealing performance of HAN can be explained by its intrinsic capacity to extract significant contextual similarities within documents and that pertinent cues, which allow truthful text to be distinguished from deceitful ones, are dependent on the context rather than the content [75]. All in all, the results suggest that textual data can offer much more insight than LING across all classifiers.

We conclude the analysis by examining the feature combination FIN+TXT, which is at the core of our study. The input setup is done in two ways: a combination of word vectors with financial indicators into data set and a 2-step modeling approach. The latter comprises building a TXT model and using its probability prediction as an input to another DL model that will concoct it with FIN and output the final binary prediction. The first approach is applied in the case of benchmark models, including ANN. The second one is implemented for HAN and GPT-2.

Based on a comparison of models using only TXT or FIN data, Purda and Skillicorn [58] concluded that these data sources are complementary with each source identifying specific types of fraud that the other cannot detect. In our case, all benchmarks exhibit improved performance in comparison to the FIN + LING setup, especially LR and SVM. However, the same unanimity is observed in decreased F1-score. We observe the superiority of predictive powers of full-textual input over the linguistic metrics. If we compare the additional value of FIN for the performance, we can see only a minor increase in almost all metrics, once again underlying the complexity and potential misalignment of FIN and TXT data. However, it is essential to note that unlike F1-score, F2-score increases across the ML benchmarks, which brings us to the initial assumption behind the preference toward the F2-score as key to model evaluation for practical use. We conclude that with the increased complexity of input, one should opt for advanced ML techniques for the extraction of extra insight.

The best performance is again yielded by HAN with AUC 92.64%, followed by XGB and ANN with AUCs of 89%. HAN is also offering the highest sensitivity of 90% across all datasets and models, making it the recommended solution for statement fraud detection. Going back to the triad comparison between ANN, HAN, and GPT-2, we can see that the latter does not show much improvement with added FIN data. This signals the potentially poor choice of pre-trained embeddings, highlighting the importance of this decision in the design of a DL classifier and reminding that state-of-the-art solutions do not guarantee superior results. ANN does not catch up with HAN AUC-wise. However, it showcases the $\mathfrak { h } ^ { \ i } \mathrm { g } _ { \mathrm { \lambda } } ^ { \mathtt { l } }$ er F2-score of 90.55%, surpassed only by XGB, which proved to be a promising alter native to the DL methods. The results of modeling on HAN showed its capacity to incorporate and extract additional values from the diversified input, exploration of data enrichment for fraud detection.

The results of HAN address the RQ 1 and 2, allowing us to conclude that the proposed DL architecture offers a substantial improvement for fraud detection facilitation. Additionally, its properties allow us to offer a look into the "black box" of the DL models and provide the rationale practitioners, given the need to substantiate the audit judgment, and will be further explored in the next Section.

## 7. Interpretation and decision support application

SEC developed software specifically focused on the MD&A section [58] to examine the use of language for indications of fraud. The importance of the MD&A section can be observed in reforms introduced by SOX in 2002, which demanded that the relevant section should present and offer full disclosure on critical accounting estimates and policies [62]. The length of MD&A sections increased after SOX became effective; nevertheless, Li [41] concluded that no changes were made to the information contained within MD&A sections or the style of language adopted. Taking further the fraud detection efforts, we developed a method to facilitate the audit of the MD&A section. We employ state-of-the-art textual analysis to shed light on managers‟ cognitive processes, which could be revealed by the language used in the MD&A section. Zhou et al. [75] demonstrated that it is plausible to detect lies based on textual cues. Nonetheless, the pertinent cues that allow truthful texts to be distinguished from deceitful ones are dependent on the context. One way to support auditors would be the "red-flag" indication in the body of the MD&A section. Hajek and Henriques [26] explored the use of "green-flag" and "red-flag" values of financial indicators and concluded that the identification of non-fraudulent firms is less complex and can be accompanied by interpretable "green-flag" values, however because the detection of fraudulent firms requires more complex non interpretable ML models, no "red-flag" values could be derived. We will take it further and provide the suggestion for the use of textual elements as "red-flags" for auditors. This can be done on the word level or th $\texttt { e } , \mathrm { e } \mathrm { ~ } \mathrm { 1 t e n c e - l e v e l }$ and is to our best knowledge, new to the field. The HAN model allows a holistic analysis of the text structure and the underlying semantics. In contrast to BOW that ignores specific contextual meanings of words, the HAN model considers the grammar, structure, and context of words within a sentence and of sentences within a document, which is essential $\mathrm { f } ( \boldsymbol { \mathbf { \rho } } , \boldsymbol { \mathbf { r } }$ the identification of fraudulent behaviour. The attention mechanisms of the HAN logical dependencies of the content and enable the identification of the words $\arctan ^ { \ J }$ sentences that contribute the most in attributing the fraudulent behaviour by extracting the wor and sentence attention weights defined in Equation 2 and 8. These valuable insights $\mathbf { L } _ { \mathbf { a } _ { - } } ^ { \mathbf { \alpha } \setminus + \varepsilon }$ the internal document structure together with strong predictive performance, make HAN notably advantageous in comparison to BOW-based traditional benchmarks.

Based on the assumption that fraudulent actors are capable of manipulating their writings so that they have convincing similarities to those that are non-fraudulent, only concentrating on words that focus on the content of the text while disregarding the context could be overly simplistic for differentiating truthful from misleading statements. We assume that due to their inherently higher complexity, sentence-level indicators are less prone to manipulation and provide robust insight for auditing.

## 7.1. Word-level

We provide a comparative analysis of words considered to be "red-flags" by the more traditional RF model and those offered by HAN. The RF model proved to be a potent and consistent classifier throughout the comparative analysis. We apply the lime methodology of Ribeiro et al. [63] to gain insight into the role of different words in the model‟s classification decision. lime stands for Local Interpretable Model-Agnostic Explanations and is based on explaining the model functioning in the locality of the chosen observation. Ribeiro et al. [63] explains every input separately; the example of its application to one of the fraud texts can be found in Figure 3:

Figure 3: Words with top weights indicating fraud from a sample MD&A

We supply all fraud cases through the lime package and extract the top ten words, that have the strongest effect on the model in terms of fraud indication. We further aggregate these words and gain a "red-flag" vocabulary. Addition ally, we perform the same analysis with the DNN model and extract the weights assigned by the HAN attention layer. The results are summarized in Figure 4:

Figure 4: "Red-flag" words identified by RF and HAN, the bottom section contains the words matching both sets

Fifteen words are found to be important for an indication of fraudulent activity by both algorithms, including " government", "certain", "gross", potentially indicating adverse involvement of the state institutions. It would seem that RF derives judgment from the industry: "aerospace", medical terms, "pilotless", "armourgroup". HAN picks up on financial and legal terms like "cost", "acquisition", "property". Both classifiers also include time- and calendar-related words like names of the month. It is not obvious how much the context affects this selection. Additionally, derivation of a word-based rule might potentially lead to a quick adaptation of the reporting entities for audit circumvention. Ambiguous interpretation and manipulation risks motivate the creation of the sentence-level decision support system.

## 7.2. Sentence-level

The added contextual information extracted by the HAN shows improved performance on the test set in comparison to linguistic features and other DNN models. It can be partially explained by the hierarchical structure of language, which entails the unequal roles of words in the overall structure. Following RQ 3, we want to benefit from the structural and context insight retained in sentence-level analysis, provided uniquely by the HAN model.

We extract the sentence-level attention weights for 200 fraudulent reports gained as a result of prediction by HAN and filter the top ten most important sentences per report. The mean weight of a sentence that can be considered a "red-flag" is 0.05, with a maximum at 0.61. We devise a rule, "important" and those between highlighted in the considered MD&A, as depicted in Figure 5.

We propose to use the probability prediction of the HAN model and assign sentence weights as a two-step decision suppor t system for auditors. Given its strong predictive performance, HAN can provide an initial signal about the risks of fraud. Based on a selected sensitivity threshold, auditors may select to evaluate a potentially fraudulent report with extra caution and use the highlighted sentences as additional guidance. Given the lengthiness of an average MD&A and limited physical concentration capacities associated with the manual audit, this sort of visual guidance can offer higher accuracy of fraud detection.

Figure 5: A page from MD&A (on the left) and its extract with "red-flag" phrases for the attention of the auditor (on the right). Sentences that contributed the most to the decision towards "fraud" are labeled by HAN as extra important and important. Additional examples are provided in the Online Appendix.

## 8. Discussion

As reported in the literature review, Hajek and Henriques [26] and Throckmorton et al. [68] have tackled the task of combined mining financial and linguistic data for financial statement fraud prediction, and no study was found on the combination of financial and textual data. Given the managerial efforts to conceal bad news by using particular wording [29] and by generating less understandable reports [39, 45], it is pivotal to adopt more advanced text processing techniques.

SVM showed good performance across most experimental setups.Due to its ability to deal with high dimensional, sparse feature spaces, SVM has achieved the best performances in previous studies that incorporated the BOW approach [23, 58]. in this study, RF showed the best predictive performance, managing to extract knowledge from both financial and BOW-based textual sources. DL models also proved capable of distinguishing fraudulent cases. However, only the HAN architecture showcased exceptional capacity to extract signals from the FIN + TXT setting, which is in the center of the current research. The HAN detects a high number of fraudulent cases compared to remaining models, strengthening the statement by Zhou et al. [75] that the detection of deception based on text necessitates contextual information.

The results of the AUC measures indicate that the linguistic variables extracted with HAN and TF-IDF add significant value to fraud detection models in combination with financial ratios. The heterogeneity in performance shifts among different data types for models, showing that different models pick up on different signals, and a combination of these models might be more appropriate to support the decision-making processes of stakeholders in the determination of fraud than the choice of a single model. The use of additional performance metrics like F2-score addressed the practical applicability of the classification models, given the imbalance of error should be considered in combination with the model‟s sensitivity in order to account for the implications of non-detecting the fraudulent case.

We have explored the interpretation capacities of RF and HAN models on the word and agreed on a specific "red-flag" vocabulary; however, mostly, they picked up on different terms. Also, out of context, these words might be misleading. The indication of "red-flags" words is becoming increasingly unreliable with the adaptive response of the alleged offending parties. The offered sentence-level markup showed a more robust approach to the provision of decision support for the auditors.

Auditors must devote effort and time to risk assessment of financial misstatements, which is tedious and complex. The utilisation of interpretable state-of-the-art technology is essential to facilitate the detection of fraud by auditors and will significantly enhance effectiveness and efficiency of audit work. Moreover, the presence of enhanced anti-fraud controls will prevent individuals from committing fraudulent acts and therefore reduces fraud risks.

## 9. Conclusion

The detection of financial fraud is a challenging endeavor. The continually adapting and complex nature of fraudulent activities necessitates the application of the latest technologies to confront fraud. The paper examined the potential of a state-of-the-art DL model to add to the development of advanced financial fraud detection methods. Minimal research has been conducted on the subject of methods that combine the analysis of financial and linguistic information, and no studies were discovered on the application of text representation based on DL to detect financial statement fraud. In addition to quantitative data, we investigated the potential of the accompanying text data in annual reports, and have emphasized the increasing significance of textual analysis for the detection of signals of fraud within financial documentation. The proposed HAN method concentrates on the content as well as the context of textual information. Unlike the BOW method, which disregards word order and additional grammatical information, DL is capable of capturing semantic associations and discerning the meanings of different word and phrase combinations.

The results have shown that the DL model achieved considerable improvement in AUC compared to the benchmark models. The findings indicate that the DL model is well suited to identify the fraudulent cases correctly, whereas most ML models fail to detect fraudulent cases while performing better at correctly identifying the truthful statements. The detection of fraudulent specifically in the highly unbalanced case of fraud detection, it is advisable to use multiple models designed to capture different aspects. Based on these findings, we conclude that the textual information of the MD&A section extracted through HAN has the potential to enhance the predictive accuracy of financial statement fraud models, particularly in the generation of warning signals for the fraudulent behavior that can serve to support the decision making-process of stakeholders. The distorted word order handicaps the ability of the BOW-based ML benchmarks to offer a concise indication of the "red-flags". We offered the decision support solution to the auditors that allows a sentence-level indication of text fragments that trigger the classifier to treat the submitted case as fraudulent. The user can select the degree of impact of indicated sentences and improve the timing and accuracy of the audit process.

## Acknowledgement

Funding: This work was supported by Deutsche Forschungsgemeinschaft in the scope of the International Research Training Group (IRTG) 1792.

## References

[1] A. Abbasi, C. Albrecht, A. Vance, and J. Hansen. “Metafraud: A meta-learning framework for detecting financial fraud”. In: MIS Quarterly: Management Information Systems 36.4 (2012), pp.1293–1327.

[2] ACFE. Report to the Nations 2020 Global Study on Occupational Fraud and Abuse. Tech. rep. 2020. URL: o-the-Nations.pdf.

[3] W. S. Albrecht, C. Albrecht, and C. C. Albrecht. “Current trends in fraud and its detection”. In: Information Security Journal 17.1 (2008), pp. 2–12.

[4] B. Bai, J. Yen, and X. Yang. “False financial statements: Characteristics of China‟s listed

[5] M. D. Beneish. “Detecting GAAP violation: Implications for assessing earnings management among firms with extreme financial performance”. In: Journal of Accounting and Public Policy 16.3 (1997), pp. 271–309.

[6] M. D. Beneish. “The Detection of Earnings Manipulation”. In: Financial Analysts Journal 55.5 (1999), pp. 24–36.

[7] A. Bodnaruk, T. Loughran, and B. McDonald. “Using 10-K text to gauge financial constraints”. In: Journal of Financial and Quantitative Analysis 50.4 (2015), pp. 623–646.

[8] P. Bojanowski, E. Grave, A. Joulin, and T. Mikolov. “Enriching Word Vectors with Subword Information”. In: arXiv preprint arXiv:1607.04606 (2016).

[9] L. Breiman, J. H. Friedman, R. A. Olshen, and C. J. Stone. Classification and Regression Trees. Vol. 19. 1984, p. 368.

[10] L. Breiman. “Random forests”. In: Machine Learning 45.1 (2001), pp. 5–32.

[11] S. V. Brown and J. W. Tucker. “Large-Sample Evidence on Firms‟ Year-over-Year

MD&A Modifications”. In: Journal of Accounting Research 49.2 (2011), pp. 309–346.

[12] M. Cecchini, H. Aytug, G. J. Koehler, and P. Pathak. “Making words work: Using financial text as a predictor of financial events”. In: Decision Support Systems 50.1 (2010), pp. 164–175.

[13] J. Chung, C. Gulcehre, K. Cho, and Y. Bengio. “Empirical evaluation of gated recurrent neural networks on sequence modeling”. In: arXiv preprint arXiv:1412.3555 (2014).

[14] A. K. Davis, J. M. Piger, and L. M. Sedor. “Beyond the Numbers: Measuring the Information Content of Earnings Press Release Language”. In: Contemporary Accounting Research 29.3 (2012), pp. 845–868.

[15] P. M. Dechow, W. Ge, C. R. Larson, and R. G. Sloan. “Predicting Material Accounting Misstatements”. In: Contemporary Accounting Research 28.1 (2011), pp. 17–82.

[16] B. M. DePaulo, R. Rosenthal, J. Rosenkrantz, and C. Rieder Green. “Actual and Perceived Cues to Deception: A Closer Look at Speech”. In: Basic and Applied Social Psychology 3.4 (1982), pp. 291–312.

[17] S. Dumais, J. Platt, D. Heckerman, and M. Sahami. “Inductive learning algorithms and representations for text categorization”. In: Proceedings of the 7th International Conference on Information and Knowledge Management (1998), pp. 148–155.

[18] A. Dyck, A. Morse, and L. Zingales. “Who blows the whistle on corporate fraud?” In: Journal of Finance 65.6 (2010), pp. 2213–2253.

[19] R. Feldman, S. Govindaraj, J. Livnat, and B. Segal. “Management‟s tone change, post pp. 915–953.

[20] C. Gaganis. “Classification techniques for the identification of falsified financial statements: a comparative analysis”. In: Intelligent Systems in Accounting, Finance & Management 16.3 (2009), pp. 207–229.

[21] J. Gee and M. Button. The Financial Cost of Fraud 2019. Tech. rep. Crowe, 2019.

[22] F. H. Glancy and S. B. Yadav. “A computational model for financial reporting fraud detection”. In: Decision Support Systems 50.3 (2011), pp. 595–601.

[23] S. Goel and J. Gangolly. “Beyond the numbers: Mining the annual reports for hidden cues indicative of financial statement fraud”. In: Intelligent Systems in Accounting, Finance and Management 19.2 (2012), pp. 75–89.

[24] S. Goel, J. Gangolly, S. R. Faerman, and O. Uzuner. “Can linguistic predictors detect fraudulent financial filings?” In: Journal of Emerging Technologies in Accounting 7.1 (2010), pp. 25–46.

[25] S. Goel and O. Uzuner. “Do Sentiments Matter in Fraud Detection? Estimating Semantic Orientation of Annual Reports”. In: Intelligent Systems in Accounting, Finance and Management 23.3 (2016), pp. 215–239.

[26] P. Hajek and R. Henriques. “Mining corporate annual reports for intelligent detection of financial statement fraud – A comparative study of machine learning methods”. In: Knowledge- Based Systems 128 (2017), pp. 139–152.

[27] S. Hochreiter and J. Schmidhuber. “Long Short-Term Memory”. In: Neural Computation 9.8 (1997), pp. 1735–1780.

4360–4372.

[29] S. L. Humpherys, K. C. Moffitt, M. B. Burns, J. K. Burgoon, and W. F. Felix. Decision Support Systems 50.3 (2011), pp. 585–594.

[30] T. Joachims. “A probabilistic analysis of the Rocchio algorithm with TFIDF for text categorization”. In: the 14th International Conference on Machine Learning (ICML ’97) (1997), pp. 143–151.

[31] N. Kalchbrenner and P. Blunsom. “Recurrent continuous translation models”. In: EMNLP 2013 - 2013 Proceedings of the Conference. Association for Computational Linguistics (ACL), 2013, pp. 1700–1709.

[32] N. Kalchbrenner, E. Grefenstette, and P. Blunsom. “A convolutional neural network for modelling sentences”. In: 52nd Annual Meeting of the Association for Computational Linguistics, ACL 2014 - Proceedings of the Conference. Vol. 1. Association for Computational Linguistics (ACL), 2014, pp. 655–665.

[33] J. M. Karpoff, A. Koester, D. S. Lee, and G. S. Martin. “Database Challenges in Financial Misconduct Research”. In: Working Paper (2014), pp. 1–66.

[34] Y. J. Kim, B. Baik, and S. Cho. “Detecting financial misstatements with fraud intention

using multi-class cost-sensitive learning”. In: Expert Systems with Applications 62 (2016), pp. 32–43.

[35] M. Kränkel and H.-E. L. Lee. “Text Classification with Hierarchical Attention Networks”. In: (2019). URL: https://humboldt-wi.github.io/blog/research/information\_sys tems\_1819/group5\_han/.

[36] M. Kraus and S. Feuerriegel. “Decision support from financial disclosures with deep neural networks and transfer learning”. In: Decision Support Systems 104 (2017), pp. 38–48.

[37] M. Kraus, S. Feuerriegel, and A. Oztekin. “Deep learning in business analytics and operations research: Models, applications and managerial implications”. In: European Journal of Operational Research 281.3 (2020), pp. 628–641.

[38] D. F. Larcker and A. A. Zakolyukina. “Detecting Deceptive Discussions in Conference Calls”. In: Journal of Accounting Research 50.2 (2012), pp. 495–540.

[39] F. Li. “Annual report readability, current earnings, and earnings persistence”. In: Journal of Accounting and Economics 45.2-3 (2008), pp. 221–247.

[40] F. Li. “Textual analysis of corporate disclosures: A survey of the literature”. In: Journal of accounting literature 29 (2010), p. 143.

[41] F. Li. “The information content of forward- looking statements in corporate filings-A naïve bayesian machine learning approach”. In: Journal of Accounting Research 48.5 (2010), pp. 1049–1102.

[42] C. C. Lin, A. A. Chiu, S. Y. Huang, and D. C. Yen. “Detecting the financial statement fraud: The analysis of the differences between data mining techniques and experts‟ judgments”. In: Knowledge-Based Systems 89 (2015), pp. 459–470.

[43] C. Liu, Y. Chan, S. H. Alam Kazmi, and H. Fu. “Financial Fraud Detection Model: Based on Random Forest”. In: International Journal of Economics and Finance 7.7 (2015).

[44] T. I. M. Loughran and B. Mcdonald. “When is a Liability not a Liability ? Textual Analysis , Dictionaries , and 10-Ks Journal of Finance , forthcoming”. In: Journal of Finance 66.1 (2011), pp. 35–65.

[45] T. Loughran and B. Mcdonald. “Measuring readability in financial disclosures”. In: Journal of Finance (2014).

[46] C. D. Manning, P. Ragahvan, and H. Schutze. “An Introduction to Information Retrieval”. In: Information Retrieval c (2009), pp. 1–18.

[47] T. Mikolov, M. Karafiát, L. Burget, J. „ Cernocký, and S. Khudanpur. “Recurrent Neural Network Language Modeling”. In: Interspeech. September. 2010, pp. 1045–1048.

[48] T. Mikolov, I. Sutskever, K. Chen, G. Corrado, and J. Dean. “Efficient Estimation of Word Representations in Vector Space Tomas”. In: IJCAI International Joint Conference on Artificial Intelligence (2013). URL: http://arxiv.org/abs/1301.3781.

[49] M. L. Newman, J. W. Pennebaker, D. S. Berry, and J. M. Richards. Lying words: Predicting deception from linguistic styles. 2003.

[50] K. Nguyen. “Financial statement fraud:Motives, Methods, Cases and Detection”. In: The Secured Lender 51.2 (1995), p. 36.

manipulation by using support vector machine and probabilistic neural network”. In: Expert Systems with Applications 36.3 PART 1 (2009), pp. 5419–5423.

[52] J. W. Pennebaker, M. R. Mehl, and K. G. Niederhoffer. “Psychological Aspects of Natural 547–577.

[53] J. Pennington, R. Socher, and C. D. Manning. “GloVe: Global vectors for word representation”. In: EMNLP 2014 - 2014 Conference on Empirical Methods in Natural Language Proc Linguistics (ACL), 2014, pp.1532–1543.

[54] J. Perols. “Financial statement fraud detection: An analysis of statistical and machine learning algorithms”. In: Auditing 30.2 (2011), pp. 19–50.

[55] O. S. Persons. “Using Financial Statement Data To Identify Factors Associated With Fraudulent Financial Reporting”. In: Journal of Applied Business Research (JABR) 11.3 (2011), p. 38.

[56] T. Pourhabibi, K.-L. Ong, B. H. Kam, and Y. L. Boo. “Fraud detection: A systematic literature review of graph-based anomaly detection approaches”. In: Decision Support Systems 133 (2020), p. 113303. URL: https://www.sciencedirect.com/science/article/pii/S01679236 20300580?via%3Dihub.

[57] L. D. Purda and D. Skillicorn. “Reading between the Lines: Detecting Fraud from the Language of Financial Reports”. In: SSRN Electronic Journal (2012).

[58] L. Purda and D. Skillicorn. “Accounting Variables, Deception, and a Bag of Words: Assessing the Tools of Fraud Detection”. In: Contemporary Accounting Research 32.3 (2015), pp. 1193–1223.

[59] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever. “Language models are unsupervised multitask learners”. In: OpenAI Blog 1.8 (2019), p. 9.

[60] G. Rao, W. Huang, Z. Feng, and Q. Cong. “LSTM with sentence representations for document-level sentiment classification”. In: Neurocomputing 308 (2018), pp. 49–57.

[61] P. Ravisankar, V. Ravi, G. Raghava Rao, and I. Bose. “Detection of financial statement fraud and feature selection using data mining techniques”. In: Decision Support Systems 50.2 (2011), pp. 491–500.

[62] Z. Rezaee. “Causes, consequences, and deterence of financial statement fraud”. In: Critical Perspectives on Accounting 16.3 (2005), pp. 277–298.

[63] M. T. Ribeiro, S. Singh, and C. Guestrin. “"Why Should I Trust You?": Explaining the Predictions of Any Classifier”. In: Proceedings of the 22nd ACM SIGKDD International

[64] S. A. Richardson, R. G. Sloan, M. T. Soliman, and I. Tuna. “Accrual reliability, earnings persistence and stock prices”. In: Journal of Accounting and Economics 39.3 (2005), pp. 437–485.

[65] Securities and Exchange Commission. “Division of Corporation Finance: Standard Industrial Classification (SIC) Code List”. In: (2019). URL: https://www.sec.gov/info/edgar/siccodes.htm.

[66] T. W. Singleton and A. J. Singleton. Fraud Auditing and Forensic Accounting, Fourth Edition. 2011.

[67] P. C. Tetlock. “Giving content to investor sentiment: The role of media in the stock market”. In: Journal of Finance 62.3 (2007), pp. 1139–1168.

[68] C. S. Throckmorton, W. J. Mayew, M. Venkatachalam, and L. M. Collins. “Financial fraud detection using vocal, linguistic and financial cues”. In: Decision Support Systems 74 (2015), pp. 78–87.

[69] A. J.-P. Tixier. “Notes on Deep Learning for NLP”. In: (2018). URL: https://arxiv.org/abs/1808.09772.

[70] US Securities and Exchange Comission. “Agency Financial Report”. In: US Department of State (2019). URL: https://www.sec.gov/files/sec-2019-agency-financial-report. pdf#mission.

[71] J. West and M. Bhattacharya. Intelligent financial fraud detection: A comprehensive review. 2016.

[72] Z. Yang, D. Yang, C. Dyer, X. He, A. Smola, and E. Hovy. Hierarchical Attention Networks for Document Classification. Tech. rep. In Proc. of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 2016, pp. 1480–1489.

[73] W. Yin, K. Kann, M. Yu, and H. Schütze. “Comparative Study of CNN and RNN for Natural Language Processing”. In: (2017). URL: http://arxiv.org/abs/1702.01923.

[74] C. Zhou, C. Sun, Z. Liu, and F. C. M. Lau. “A C-LSTM Neural Network for Text Classification”. In: (2015). URL: http://arxiv.org/abs/1511.08630.

[75] L. Zhou, J. K. Burgoon, J. F. Nunamaker, and D. Twitchell. “Automating detecting deception in text-based asynchronous 81–106.

[76] E. Zinovyeva, W. K. Härdle, and S. Lessmann. “Antisocial online behavior detection using deep learning”. In: Decision Support Systems online first, doi:10.1016/j.dss.2020.113362 (2020).

# Journal Pre-proof

## Biographical Note

## Patricia Craja

Patricia Craja received her B.Sc. degree in Mathematics and M.Sc. degree in Statistics, from the Technical University of Berlin and the Humboldt University of Berlin, Germany, in 2013 and 2020, respectively. Currently, she is working as a Data Science Freelancer. Her current research interests are in the fields of natural language processing and decision making.

## Alisa Kim

Alisa Kim is a researcher at Humboldt University, focusing on the application of deep learning and natural language processing in financial and regulatory sectors. She got her Master's degree in Management from St. Andrews University and worked in investment banking and consulting before joining the Business Informatics Chair of HU as a full-time researcher and educator.

## Stefan Lessmann

Stefan Lessmann received a diploma in business administration and a PhD from the University of Hamburg in 2002 and 2007, respectively. Stefan worked as a lecturer and senior lecture in business informatics at the Institute of Information Systems of the University of Hamburg. Since 2008, Stefan is a guest lecturer at the School of Management of University of Southampton, where he teaches under- and postgraduate courses on quantitative methods, electronic business, and web application development. Stefan completed his habilitation in the area of predictive analytics in 2012. In 2014, Stefan joined the Humboldt-University of Berlin, where he heads the Chair of Information Systems at the School of Business and Economics. Stefan published several papers in leading international journals and conferences, including the European Journal of Operational Research, the IEEE Transactions of Software Engineering, and the International Conference on Information Systems. He actively participates in knowledge transfer and consulting projects with industry partners; from small start-up companies to global players.

## CRediT author statement

Patricia Craja: Conceptualization, Methodology, Software, Validation, Formal analysis,Investigation,Writing - Original Draft, Visualization

Alisa Kim: Conceptualization, Methodology, Software, Validation, Formal analysis,Writing - Review & Editing, Visualization

Stefan Lessmann: Conceptualization,Validation, Supervision

## Highlights

● Combining financial and text data enhances fraudulent financial statements detection

● HAN, GPT-2, ANN and XGB detect financial misstatements based on textual cues

● Novel NLP techniques allow to capture content and context of MD&As

● Interpretability offered with “red-flag” sentences in the MD&As of annual reports

● The proposed models provide decision support for stakeholders response to survey questions concerning their backgrounds, interests and preferences. Our products augment these profiles over time by privacy concerns nevertheless may cause visitors to resist providing Because Our Products Require The Transfer Of Information Over The Internet, Serious Harm To Our Business Could Result If Our Encryption Transactions. The secure exchange of confidential information over public networks is a significant concern of consumers engaging in or line transactions and interaction. Our customer manacement software applications use encryption technology to provide the security necessary to effect the secure exchange ofaluable and confidential information. Advances in cemputer capabilities, new discoveries in the field of cryptography or other evorcs or developments could result in a compromise or breach of the algorithms that these applications use to protect customer transaction data. If any compromise or breach were to occur, it conld seriously harmbur business, financial condition and operating reaults. We May Not Successfully Integrate The Products, Technologies r Businesses Fron, Or Realize The Intended Benefits of Recent Acquisiions, And We May Make Future Acquisitions Or Enter Intc Joint Ventures That Are Noe Successful. In the future, we could acguire additional products. technologies or businesses. or enter into joint venture arrangements, for the purpose of complementing or expanding our business. Managements negotiations of potential acquisitions or joint ventures and managements integration of acquired products, technologies or businesses. could divert managements time and resources. Future acguisitions could cause us to issue eguity securities that would amortize intangible assets, or write off in process research and development and other acguisition related expenses that could seriously harm our financial condition and operating results. Further, we may not be able to properly integrate acguired products. technologies or businesses, with our existing products and operations, train, retair integrate acguired products. technologies or businesses. or train. retain and motivate personnel from the acguired businesses, we may not receive the intended benefits of those acguisitions. which could Additional Personnel Could Seriously Harm Our Company, We rely upon the continued service of a relatively small number of key technical, sales and senior management personnel. Our future success depends on retaining our key employees and our continuing ability to 33 Table of Contents attract. train and retain other highly gualified technical. sales and managerial personnel. We have employment agreements with

![](/api/attachments/UEWRRJEP/fulltext/images/5b19ab35c8f0e4ffc283939e07b60805d4e6d87838e7029a761961073956cf73.jpg)  
Figure 1

![](/api/attachments/UEWRRJEP/fulltext/images/4f1874b40719eb8cdd61b50f29b1568d577853acc8088be4cd959260c7110b4c.jpg)  
Figure 2

![](/api/attachments/UEWRRJEP/fulltext/images/2c53c0a62ee4aa67a0da7dbd181e7469e9dacab6253a187a3ba4edc9bb499d38.jpg)  
Figure 3

<table><tr><td>RF lime</td><td>DNN Attention</td></tr><tr><td>aerospac, align, america, amnesti, api, arcapita, arduou, armorgroup, artisan, astound, ballist, belief, broadest, brokerag, canton, carbon, categori, cdc, contain, copley, cork, dealer, decemb, deeper, defect, depend, diamond, discuss, doughnut, dysfunct, elig, endow, ensuit, epidem, erp, especi, fashion, forgiv, grain, grand, groundwat, grown, harbing, health, help, hemispher,immun, interrupt, itsunfavor, keyboard, kraken, liabl, lingyun, mainli, mammographi, mancelona, mard, marian, maverick, maxim, militia, mobiapp, monocular, necessari, nitrat, nonsteroid, offlin, operatingloss, orthovisc, paint, paramagnet, payabl, pilotless, predomin, reagent, reengin, referenc, reformul, reincentiv, remex, reprograph, resin, rubber, satur, sec, semisubmers, shoot, sophist, spectromet, state, strain, suitabl, sunnyval, trailer, transact, trundl, tucson, understood, undistribut, unwil, updat, upsid, valencia, visitor, websit, withdrawn</td><td>according, acquisition, addition, additionally, agreement, also, although, april, august, average, based, believe, biotin, business, chairman, company, competitor, completed, corporate, cost, course, criterion, currently, customer, decrease, dev, diverse, entered, enterprise, event, expect, factor, february, following, ft, future, generally, government, gross, home, increase, increasing, industry, intend, july, june, management, many, march, market, may, merchandise, million, network, new, non, november, number, october, one, opened, operate, operates, organized, overview, patent, payment, primary, product, property, recent, region, remaining, representative, result, revenue, rig, risk, sale, segment, sell, september, service, since, solution, store, strategy, table, technology, time, total, truck, two, type, typical</td></tr><tr><td colspan="2">april, certain, chairman, government, gross, june, million, network, new, product, rig, sale, store, truck, year</td></tr></table>

Figure 4

line transactions and interaction. Our customer management software applications use encryption technology to provide the security necessary to effect the secure exchange of valuable and confidential information. Advances in computer capabilities, new discoveries in the field of cryptography or other events or developments could result in a compromise or breach of the algorithms that these applications use to protect customer transaction data. If any compromise or breach were to occur, it could seriously harm our business, financial condition and operating results. We May Not Successfully Integrate The Products Technologies Or Businesses From, Or Realize The Intended Benefits Of Recent Acquisitions, And We May Make Future Acquisitions Or Enter Into Joint Ventures That Are Not Successful. In the future, we could acquire additional products, technologies or businesses, or enter into joint venture arrangements for the purpose of complementing or expanding ouz business. Managements negotiations of potential acquisitions or joint harm our financial condition and operating results. Further, we may not be able to properly integrate acquired products, technologies or businesses, with our existing products and operations, train, retain and motivate personnel from the acguired businesses, or combine potentially different corporate cultures. If we are unable to fully integrate acquired products, technologies or businesses, or train, retain and motivate personnel from the acquired businesses, we may not receive the intended benefits of those acquisitions, which could seriously harm our business, operating results and financial condition The Loss Of Any Of Our Key Personnel Or Our Failure To Attract Additional Personnel Could Seriously Harm Our Company. We rely upon the
