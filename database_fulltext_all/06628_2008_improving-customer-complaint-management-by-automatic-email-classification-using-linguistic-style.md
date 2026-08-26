---
otero_id: 6628
otero_key: "ERN4TPJM"
title: "Improving customer complaint management by automatic email classification using linguistic style features as predictors"
authors: "Kristof Coussement; Dirk Van den Poel"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.10.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Improving customer complaint management by automatic email classification using linguistic style features as predictors

Kristof Coussement, Dirk Van den Poel <sup>⁎</sup>

Ghent University, Faculty of Economics and Business Administration, Department of Marketing, Tweekerkenstraat 2, 9000 Ghent, Belgium

Received 12 January 2007; received in revised form 19 September 2007; accepted 14 October 2007 Available online 24 October 2007

## Abstract

Customer complaint management is becoming a critical key success factor in today's business environment. This study introduces a methodology to improve complaint-handling strategies through an automatic email-classification system tha distinguishes complaints from non-complaints. As such, complaint handling becomes less time-consuming and more successful. The classification system combines traditional text information with new information about the linguistic style of an email. The empirical results show that adding linguistic style information into a classification model with conventional text-classification variables results in a significant increase in predictive performance. In addition, this study reveals linguistic style differences between complaint emails and others. © 2007 Elsevier B.V. All rights reserved

Keywords: Customer Complaint Handling; Call-center email; Voice of customers (VOC); Singular Value Decomposition (SVD); Latent Semantic Indexing (LSI); Automatic email classification

## 1. Introduction

Due to the rapid development of information technology and Internet, new opportunities arise for marketing analysts nowadays. For instance, companies can easily advertise through the email channel [10] or offer products in an electronic commerce [14]. This study focuses on the usefulness of client/company interactions through email as the basis for improved customer complaint management. Nowadays, companies receive daily huge amounts of emails due to the fact that their clients become more used to sending emails as a substitute for traditional communication methods [29]. Growingly, efficient email handling is becoming a critical key success factor in today's business environment. Recently, companies start to outsource their customer-email management by relying on customer-call centers to address the voice of customers — i.e. customer complaints and service-information requests [20].

Indeed, Internet enables customers to easily express their problems with a product or a service. Consequently, customer complaint management and service recovery are becoming key drivers for improved customer relationships. Several studies have shown the positive financial impact of investments in efficient complaint handling in a wide range of industries [13,28]. It is crucial that service-recovery efforts are forceful and effective [4], because ample research has shown that failed service-recovery actions have a significant influence on customer-switching behaviour [26].

A tool to support efficient processing of customer complaint emails is the use of an automatic email-classification system. Automatic text-classification labels incoming emails into predefined categories — i.e. complaints versus non-complaints in this study. As a consequence, customer complaint management becomes more successful in mainly two ways: (i) In contrast to manual text classification, automatic text classification is time-saving and thus less expensive in terms of labor costs. It makes the email-handling process more efficient. (ii) By classifying incoming emails into complaints and non-complaints, one can optimize the complaint-handling process. By making a distinction between complaint emails and other email types (e.g. information requests on promotional deals), the company is able to set up a separate complaint-handling department with speciallytrained complaint handlers. One can create a separate treatment procedure for complaint emails. Consequently, call centers can react more helpful on occurring problems or service failures. In general, the consistency in the way complaint emails are handled increases due to the fact that not every employee in the call center needs to be trained for all email types. In summary, building an automatic email-classification system that distinguishes complaints from non-complaints is necessary for optimizing the complaint-handling process within a call center.

Automatic text-classification systems are typically built using the conventional vector-space approach proposed by Salton [24] (e.g. [16,6,1]). This means that every email is converted into a vector that contains a stream of words or terms. This is often a very highdimensional vector due to the many distinct terms in the email corpus. This study employs Latent Semantic Indexing by means of Singular Value Decomposition as proposed by Deerweester et al. [7] to reduce the dimensionality. Consequently, textual information is represented as k distinct concepts or explanatory variables. Within this study, linguistic style information is introduced as a new type of textual information. Moreover, linguistic style differences between complaint emails and other emails are explored. Furthermore, the beneficial effect of adding linguistic style characteristics to a traditional complaint-classification system is investigated.

This study offers marketing managers a valuable system for automatic email classification in order to enable them to optimize the client/company relationship through efficient and effective complaint handling. Moreover, it introduces linguistic style characteristics of an email as a new type of textual information in a customer complaint setting. Accordingly, this study contributes to the existing literature in two ways: (i) it shows that adding these linguistic style features into a conventional emailclassification model results in an additional increase in predictive performance in distinguishing complaints from non-complaints. (ii) Moreover, this study proves that linguistic style differences exist between complaints and others.

This paper is organized as follows. Section 2 describes the methodology used throughout this study. Section 3 describes how the proposed framework is applied and evaluated within a real-life call-center setting. In the last section, the findings of this study are summarized, while also some shortcomings and directions for further research are given.

## 2. Methodology

This section describes the methodology used throughout this study. In Section 2.1 the content-based approach which is often used in traditional text-classification problems is explained. In this study, a new type of information is used to predict whether the incoming email is a complaint or not — i.e. linguistic style information of an email. Section 2.2 gives an overview how the linguistic style features are extracted from the email corpus. Section 2.3 gives an overview of the classification technique. In order to compare the performance of the different classification models, some objective evaluation criteria are needed. The evaluation criteria used throughout this study are covered in Section 2.4.

## 2.1. Vector-space approach

This section gives an overview of the conventional text-classification approach using the vector-space approach proposed by Salton [24]. Original documents are converted into a vector in a feature space based on the weighted term frequencies. Each vector component reflects the importance of the corresponding term by giving it a weight if the term is present or zero otherwise. The purpose is to select the most informative terms from the number of distinct terms in the corpus dictionary. All documents are traditionally converted from the original format to word vectors following the steps as shown in Fig. 1.

## 2.1.1. Pre-processing

Raw text cleaning converts documents into a form which is more suitable for subsequent processing. In this step, special characters and punctuations are separated from words, while spelling errors are handled by comparing all words in the document with a reference dictionary.

![](/api/attachments/ERN4TPJM/fulltext/images/3fdd6e909222c2a179c458e9fc2ec86d8734b49639f6a60b682fc09d7885f6be.jpg)  
Fig. 1. An overview of the conventional vector-space approach for text classification.

During the tokenization step, documents are divided into tokens or words, by which white space characters are used as separators. Once the text field is divided into words, words are converted to lower case — i.e. case conversion.

All words are tagged a part of speech based on their syntactic category. All words are summarized into informative and non-informative parts of speech. The non-informative parts of speech contain determiners, conjunctions, auxiliaries, prepositions, pronouns, negative articles or possessive markers, interjections, proper nouns, abbreviations and numbers. On the other hand, words can be part of an informative part of speech like nouns, verbs, adjectives and adverbs.

The next step in the text-preprocessing phase is stemming or lemmatization. Word variations are conflated into a single representative form, called the stem. A typical example of a stem is the word ‘connect’ which is the stem for the variants ‘connected’, ‘connecting’, ‘connection’ and ‘connections’. Stemming has two advantages: it reduces the corpus dictionary enormously [3] and it increases the retrieval performance significantly [15]. A dictionary-based stemmer is used throughout this study. The huge advantage is that all morphological variations are treated naturally by comparing them with a reference dictionary. When a corpus term is unrecognizable, the stemmer applies some standard decision rules to give the term the correct stem.

In order to reduce the number of irrelevant terms in the corpus dictionary, a number of term filtering tasks are performed. Firstly, rare words are left out from further analysis because they are unable to aid in future classification. Consequently, all words appearing less then three times over the entire document corpus are eliminated for further analysis. Additionally, overly common words like for instance ‘a’ or ‘the’ are also removed from the corpus dictionary. These type of words or stopwords appear so often that they are not discriminative anymore. A stoplist is language and domain specific, as a consequence a standard stoplist is often manually adapted to avoid the risk of removing relevant words. Furthermore, only words that are part of an informative part of speech are included, because these words contain relevant information to aid in future classification. In the end, the temporary dictionary is manually checked and irrelevant words are removed from the dictionary.

The result is a high-dimensional term-by-document matrix where each cell in the matrix represents the raw frequency of appearance of a term in a document. To correct for the importance of a term in a document and its importance in the corpus dictionary, the term vectors in the term-by-document matrix are weighted.

## 2.1.2. Term-vector weighting

In the term vector weighting phase, a weighted term vector for every document in the document collection is constructed. Right now, the values in the term-bydocument matrix are simply the raw frequencies of appearance for a term in a document. Term-vector weighting is often done by determining the product of the term frequency (tf) and the inverse document frequency (idf) [27,21–23].

The tf measures the frequency of occurrence of an index term in the document text [23]. The more a term is present in a document, the more important this term is in characterizing the content of that document. As such the frequency of occurrence of a content word is used to indicate term importance for content representation e.g. [21] and [22]. In this study, the tf is obtained by taking a logarithmic transformation of the original term frequency. Taking the logarithmic transformation reduces the importance of the raw tf, which is important for document collections with a varying length. The term frequency of term i in document $j ~ ( \mathrm { t f } _ { i j } )$ is given by

$$
\mathrm{tf} _ {i j} = \log_ {2} (n _ {i j} + 1)\tag{1}
$$

with $n _ { i j }$ equal to the frequency of term i in document j.

The idf takes into account that the more rarely a term occurs in a document collection, the more discriminating that term is. Therefore, the weight of a term is inversely related to the number of documents in which the term occurs — i.e. the document frequency of the term [21,22,27]. The logarithm of the idf is taken to decrease the effect of the raw idf-factor. The inverse document frequency of term i (idf ) is given by

$$
\mathrm{idf} _ {i} = \log_ {2} \left(\frac {n}{\mathrm{df} _ {i}}\right) + 1\tag{2}
$$

with n equal to the total number of documents in the entire document collection and df equal to the number of documents where term i is present.

Finally, the weight of term i in document $j ~ ( w _ { i j } )$ is given by

$$
w _ {i j} = \operatorname{tf} _ {i j} \operatorname{idf} _ {i}\tag{3}
$$

with $\mathrm { t f } _ { i j }$ equal to the term frequency of term i in document $j ,$ idf equal to the inverse document frequency of term i.

## 2.1.3. Dimensionality reduction

This weighted term-by-document matrix is a highdimensional matrix due to the many distinct corpus terms. Moreover, this matrix is very sparse – i.e. it contains a lot of zeros – since not all documents contain all corpus terms. In order to reduce the dimensionality of the feature space, this study employs Latent Semantic Indexing by using Singular Value Decomposition (SVD) as proposed by Deerweester [7]. Latent Semantic Indexing projects documents from the high-dimensional term space to an orthonormal, semantic latent subspace by grouping together similar terms into several distinct concepts k. All textual information can be summarized into k concepts. Furthermore, these k concepts or SVD variables are often used as explanatory variables in a traditional text-classification model. In summary, one concludes that Latent Semantic Indexing approximates the original weighted term-by-document matrix in a smaller rank k – i.e. k concepts or variables that summarizes the emails content – which makes it workable from a prediction point of view. Factor-analytic literature proposes an operational criterion to find the optimal value for k [7].

## 2.2. Linguistic style features

The linguistic style features are introduced as a new set of text-classification predictors. These variables are created using Linguistic Inquiry and Word Count [19,30]. This program searches individual text files, while it computes the percentage of words that were earlier judged to reflect the linguistic categories. These categories are described using an extensive dictionary. The word counts on the different categories are used as an additional set of features in the text-classification system. In sum, a detailed overview of the linguistic style categories is given in Table 1.

## 2.3. Classification technique

Boosting is used as the main classification technique for discriminating complaints from non-complaints throughout this study (see Sections 3.3 and 3.4). It is a relatively young, yet extremely powerful machine learning technique. The main idea behind boosting algorithms is to combine the outputs of many “weak” classifiers to produce a powerful “committee” or ensemble of classifiers [12]. Several studies show that ensembles generally achieve a significantly lower error rate than the best single model (e.g. [18]). Although being refined subsequently, the main idea of all boosting algorithms can be traced back to the first practical boosting algorithm,

Table 1  
Overview of the linguistic style features extracted from the call-center emails

<table><tr><td>Abbreviation</td><td>Dimension</td><td>Examples</td><td>Number of words</td></tr><tr><td>WC</td><td>Word Count</td><td></td><td></td></tr><tr><td>WPS</td><td>Words per sentence</td><td></td><td></td></tr><tr><td>Qmarks</td><td>Sentencesending with ?</td><td></td><td></td></tr><tr><td>Unique</td><td>Unique words(type/token ratio)</td><td></td><td></td></tr><tr><td>Sixltr</td><td>% words longerthan 6 letters</td><td></td><td></td></tr><tr><td>Pronoun</td><td>Total pronouns</td><td>I, our, they,you&#x27;re</td><td>38</td></tr><tr><td>I</td><td>1st person singular</td><td>I, my, me</td><td>7</td></tr><tr><td>We</td><td>1st person plural</td><td>we, our, us</td><td>6</td></tr><tr><td>Self</td><td>Total first person</td><td>I, we, me</td><td>13</td></tr><tr><td>You</td><td>Total secondperson</td><td>You, you&#x27;ll</td><td>7</td></tr><tr><td>Other</td><td>Total third person</td><td>She, their, them</td><td>12</td></tr><tr><td>Negate</td><td>Negations</td><td>No, never, not</td><td>36</td></tr><tr><td>Assent</td><td>Assents</td><td>Yes, OK,mmhmm</td><td>50</td></tr><tr><td>Article</td><td>Articles</td><td>A, an, the</td><td>3</td></tr><tr><td>Preps</td><td>Prepositions</td><td>On, to, from</td><td>48</td></tr><tr><td>Number</td><td>Numbers</td><td>One, thirty, million</td><td>107</td></tr><tr><td>Time</td><td>Time indication</td><td>Hour, day, o&#x27;clock</td><td>269</td></tr><tr><td>Past</td><td>Past tense verb</td><td>Walked, were, had</td><td>1773</td></tr><tr><td>Present</td><td>Present tense verb</td><td>Walk, is, be</td><td>1886</td></tr><tr><td>Future</td><td>Future tense verb</td><td>Will, might, shall</td><td>19</td></tr></table>

Adaboost [9]. Adaboost and related algorithms produce extremely competitive results to other classification algorithms in many settings, most notably for text classification (e.g. [25]).

This study concisely describes Adaboost for a two class classification problem. For more details about Adaboost, we refer to Hastie et al. [12]. Consider a training set $T = \{ ( x _ { i } , y _ { i } ) \}$ with $i { = } \left\{ 1 , 2 , . . . , N \right\}$ ; the input data $x _ { i } \in R ^ { n }$ and corresponding binary target labels coded as $y _ { i } \in \{ - 1 , 1 \}$ . The final classifier of the Adaboost procedure is given by

$$
F (\mathrm{x}) = \sum_ {m = 1} ^ {M} c _ {m} f _ {m} (x)\tag{4}
$$

with m the number of iterations, $f _ { m } ( x )$ the classifier predicting values ±1 during the mth round and $c _ { m }$ the weight of the contribution of each $f _ { m } ( x )$ in the final classifier. The purpose of Adaboost is to train classifiers $f _ { m } ( x )$ on weighted versions of the training data obtained by modifying the data at each boosting step by applying weights $w _ { 1 } , w _ { 2 } , . . . , w _ { N }$ to each of the training observations $( x _ { i } , y _ { i } )$ with $i { = } \left\{ 1 , 2 , . . . , N \right\}$ . Initially all the weights are set to $\begin{array} { r } { w _ { i } = \frac { 1 } { N } } \end{array}$ ; so the first step simply trains the classifier on the data in the usual manner. For each successive iteration $\begin{array} { r } { m { = } 2 , 3 , \ldots M , } \end{array}$ (i) the weights are individually modified giving a higher weight to cases that are currently misclassified and (ii) the classifier is reapplied to the weighted observations. Thus as the iterations proceed, observations that are difficult to classify receive ever-increasing influence due to the higher weight assigned. So each successive classifier is thereby forced to concentrate on those training observations that are missed by previous ones in the sequence. In the end when the maximum number of iterations M is reached, predictions from all classifiers are combined through a weighted majority vote to produce the final classifier F(x).

Table 2  
Overview of the data characteristic

<table><tr><td></td><td>Number of emails</td><td>Relative percentage</td></tr><tr><td colspan="3">Training set</td></tr><tr><td>Complaint emails</td><td>1890</td><td>36.37</td></tr><tr><td>Others</td><td>3306</td><td>63.63</td></tr><tr><td>Total</td><td>5196</td><td>100</td></tr><tr><td colspan="3">Test set</td></tr><tr><td>Complaint emails</td><td>838</td><td>37.61</td></tr><tr><td>Others</td><td>1390</td><td>62.39</td></tr><tr><td>Total</td><td>2228</td><td>100</td></tr><tr><td colspan="3">Validation set</td></tr><tr><td>Complaint emails</td><td>571</td><td>32.59</td></tr><tr><td>Others</td><td>1181</td><td>67.41</td></tr><tr><td>Total</td><td>1752</td><td>100</td></tr></table>

In order to give the reader more insights into the linguistic style differences between complaints and other email types (see Section 3.2), a stepwise logistic regression that differentiates between complaint emails and other email types is run using the linguistic style variables as described in Table 1. This technique is used because it is a conceptually simple binary classifier [5], while it provides standardized parameter estimates for the explanatory variables.

## 2.4. Evaluation criteria

In order to evaluate the performance of different predictive models, two criteria are used: the percentage correctly classified (PCC) and the area under the receiving operating curve (AUC). The PCC compares the a posteriori probability of being a complaint email with the true type of the email. If TP, FP, TN and FN are respectively the number of complaints that are correctly predicted (True Positives), the number of non-complaints that are predicted as complaints (False Positives), the number of non-complaints that are classified correctly

Table 3  
Standardized parameter estimates

<table><tr><td colspan="2">Linguistic style</td><td rowspan="2">Standardized parameter estimatesa</td></tr><tr><td>Abbreviation</td><td>Dimension</td></tr><tr><td>Article</td><td>Articles</td><td>0.1438</td></tr><tr><td>Future</td><td>Future tense verb</td><td>-0.0897</td></tr><tr><td>I</td><td>1st person singular</td><td>-0.1225</td></tr><tr><td>Negate</td><td>Negations</td><td>0.4886</td></tr><tr><td>Number</td><td>Numbers</td><td>0.1078</td></tr><tr><td>Other</td><td>Total third person</td><td>-0.0548</td></tr><tr><td>Past</td><td>Past tense verb</td><td>0.1009</td></tr><tr><td>Preps</td><td>Prepositions</td><td>-0.4739</td></tr><tr><td>Present</td><td>Present tense verb</td><td>0.0628</td></tr><tr><td>Qmarks</td><td>Sentences ending with?</td><td>-0.0833</td></tr><tr><td>Sixltr</td><td>% words longer than 6 letters</td><td>-0.1295</td></tr><tr><td>Time</td><td>Time indication</td><td>0.2122</td></tr><tr><td>WC</td><td>Word count</td><td>0.1758</td></tr><tr><td>You</td><td>Total second person</td><td>0.0759</td></tr></table>

All parameter estimates are significant at 95% confidence level.

(True Negatives) and the number of complaints that are predicted as non-complaints (False Negatives), the PCC is defined as $\mathrm { ( T P + T N ) / ( T P + F P + T N + F N ) }$ . The PCC should be benchmarked to the proportional chance criterion $\mathrm { ( = \ p e r c e n t a g e _ { e v e n t } ^ { 2 } + ( 1 - p e r c e n t a g e _ { e v e n t } ) ^ { 2 } ) }$ in order to confirm the predictive capabilities of a classifier [17]. A disadvantage of the PCC is that it is not very robust concerning the chosen cut-off value on the a posteriori probabilities [2]. In order to equally compare different classification models on PCC, the cut-off value for classifying emails into complaints or non-complaints is chosen so that the a posteriori incidence equals the a priori occurrence of complaints. For instance, 35% of the emails having the highest complaint probability will be classified as complaints when the a priori frequency of complaints is 35%. In contrast to PCC, AUC takes into account all possible thresholds on the a posteriori probabilities. For all the different levels, it considers the sensitivity (TP / (TP+ FN)) and 1 minus the specificity (TN/ (TN+ FP)) in a two-dimensional graph, named the receiving operating curve (ROC). The area under the ROC curve is used to evaluate the performance of a binary classifier [11]. DeLong et al. [8] propose a non-parametric test to compare the performance of different classification models.

## 3. Empirical results

This section applies the proposed framework in a real-life call-center setting. In the first section, detailed information concerning the call-center setting is given. Section 3.2 explores the linguistic style differences between complaint emails and other email types, while Section 3.3 investigates the beneficial effect of including linguistic predictors into a traditional text-classification setting. In the last section, the robustness of the proposed methodology is investigated.

![](/api/attachments/ERN4TPJM/fulltext/images/d7758cd2f98bac993d662f93fd239b06735674e422e556986d4c33b432c4817d.jpg)  
Fig. 2. The AUC performance on the test set of ADA\_SVD, ADA\_SVD\_LS and ADA\_LS.

## 3.1. Corpus construction

In this study, emails sent to the call center of a large Belgian newspaper company are used. Subscribers of this newspaper have the possibility to send their concerns or complaints and information requests to the call center via email. When an email message comes in, the message is manually encoded into a complaint or another email type. The former email type reports all different service failures (e.g. newspaper not delivered, financial complaints…), while the latter type consists of information requests like subscription related questions or information on promotional actions. Manually encoding email messages is a very time-consuming and very inefficient task. Moreover, all types of emails are treated equally within the same department, while in fact complaint emails need a different treatment by specialized people during email handling. The email-classification problem in this context comes down to predicting whether the incoming email is a complaint or not. Consequently, complaint handling becomes more efficient due to a faster detection of the emails at risk.

All emails from July 2004 till December 2004 are used within this study. Consequently, it is possible to derive the dependent and the explanatory variables. Because historical data is used, all email messages are already manually encoded by the staff of the call center. The dependent variable is encoded as ‘1’ when the email is a complaint and ‘−1’ otherwise. There are two types of independent variables. The first type of explanatory variables is extracted using the methodology of the vectorspace approach. Email messages are converted into a high-dimensional term-by-document matrix. However, this matrix is unworkable from a prediction point of view due to the large number of terms or variables. Consequently, several reduced rank-k models (with k = {10,20, 200}) are obtained by applying Latent Semantic Indexing using SVD. The second type of independent variables is derived by processing all emails through Linguistic Inquiry and Word Count. These independent variables represent word counts for the different categories derived from the linguistic program. These variables which contain information about the linguistic styles are used to explore their beneficial effect on top of the traditionally-used SVD variables.

Intended to methodologically correctly predict whether an email is complaint or not, the data set is divided into training, test and validation set. Emails between July 2004 and November 2004 are randomly assigned using a 70–30 split to the training and test set. The former one is used to generate and train the classifiers, while the test set is used to test the classifier on an unseen data sample. In this study, all emails of December 2004 are assigned to the validation set or out-of-period set. This dataset is used to verify the robustness of the proposed methodology. Table 2 summarizes the characteristics of the different data sets.

![](/api/attachments/ERN4TPJM/fulltext/images/b31d83c225fbc99448a11ebd28f18b28d2737389a8b4e089223fd38a049936f1.jpg)  
Fig. 3. The PCC on the test set of ADA\_SVD, ADA\_SVD\_LS and ADA\_LS.

As such, one is able to explain differences in linguistic style between complaint emails and other email types using a traditional stepwise logistic regression (see Section 3.2). Furthermore, a comparison is made in predictive performance between the models built with the k concepts (with $k { = } \left. 1 0 , 2 0 , . . . , \ 2 0 0 \right. )$ extracted using the SVD procedure (i.e. Adaboost model with SVD variables or ADA\_SVD), the model using only the linguistic style predictors (i.e. Adaboost model with linguistic style feature or ADA\_LS) and the model using both types of information or ADA\_SVD\_LS (see Section 3.3).

## 3.2. Linguistic style differences between complaint emails and other email types

This section explores if linguistic style differences exist between a complaint email and another email type. Table 3 shows the standardized parameter estimates of the linguistic style variables kept during the stepwise logistic regression whereby one tries to predict whether the received email involves a complaint or not using only the linguistic style variables as described in Table 1.

Table 3 clearly indicates that the more words (WC), the more articles (Article) and the less prepositions (Preps) are found in an email; the more likely, the email is classified as a complaint. In contrast to other types of emails (e.g. an information request), the probability of being a complaint increases when more time indications (Time) are found in an email. Moreover, the likelihood of being a complaint is positively related with the present tense (Present) – e.g. Hopefully, you can fix the misdelivery of my newspaper today (Present, Time) – and the past tense (Past) – e.g. Moreover, the newspaper was not delivered last week either (Past, Time, Time) – while the possibility of classifying an email as an information request increases when more future tenses (Future) and questions (Qmarks) are used – e.g. Will there be a reduction on my next subscription? (Future, Qmarks). When the tone of an email is more ‘aggressive’ – i.e. it contains more negations (Negate), more numbers (Numbers) and more clenched words (Sixltr) – the chance of having a complaint increases. Furthermore, complainants often directly blame the company for the service failure (I, Other, You) – e.g. Dear, the newspaper is not delivered today. It is already the sixth time this month. You must have noticed already some delivery problems. You have to fix this problem as soon as possible.(Negate, Numbers, You, You). These results indicate that differences in linguistic style exist between complaints and non-complaints.

## 3.3. Comparing predictive performance of ADA\_SVD, ADA\_LS and ADA\_SVD\_LS

This section compares the predictive performance of ADA\_SVD, ADA\_SVD\_LS and ADA\_LS in terms of AUC and PCC. Fig. 2 shows the predictive performance of the different models on the test set in terms of AUC, while a comparison in terms of PCC is shown in Fig. 3. The number of SVD concepts is represented on the X-axis, while on the Y-axis, the performance measure is shown. As a remark; (i) ADA\_LS is a horizontal line because its performance is independent of the number of SVD concepts, but it is incorporated in the figures for comparison reasons only, (ii) Appendix A includes ROCs on the test set for the models with k = {50, 100, 150, 200} in order to provide the reader with more indepth information.

As one observes from Figs. 2 and 3, all models perform enormously well in distinguishing complaint emails from non-complaint emails. Indeed, the AUC performance of all models lies between 84.55 and 91.32, while the PCC lies in the range of 77.02 and 84.65 which clearly outperforms the proportional chance criterion of $5 3 . 0 \hat { 7 } ~ ( = ~ \hat { 0 } . 3 7 6 1 ^ { 2 } + ( 1 - 0 . \hat { 3 } 7 6 1 ) ^ { 2 } )$ [17]. These results clearly indicate that all models – i.e. ADA\_SVD, ADA\_SVD\_LS and ADA\_LS – have predictive capabilities in distinguishing complaints from other emails.

Figs. 2, 3 and Table 4 give an answer to the question if adding additional linguistic style predictors to the traditional SVD dimensions is beneficial from a textclassification point of view. In other words, does ADA\_SVD\_LS significantly outperform ADA\_SVD and ADA\_LS?

Table 4 indicates that ADA\_SVD\_LS significantly outperforms ADA\_LS and ADA\_SVD on all SVD dimensions [8]. Fig. 2 confirms these results graphically in terms of AUC. Furthermore, the PCC of ADA\_SVD\_LS is always higher then ADA\_SVD and ADA\_LS as can be seen in Fig. 3. These results indicate the highly beneficial impact of combining traditional SVD predictors with linguistic style indicators into one text-classification model. As such, predictive modelers are able to build better email-classification models by incorporating this new type of information.

## 3.4. Out-of-period validation

In order to verify the robustness of the proposed methodology, all models are scored on an out-of-period validation set. This is necessary because in a realistic callcenter environment, the incoming emails lie by definition in another timeframe than the ones used during model training. As such, one is able to verify if the models built during training are still valid when validating them on another timeframe. If the proposed methodology is robust, the performance on the test set and validation set has to be stable. Figs. 4 and 5 illustrate the performance stability between the test and validation set. On the X-axis, the number of SVD variables is shown, while the Y-axis indicates the performance. The solid line represents the test-set performance, while the dashed line represents the validation-set performance. Additionally, ROCs on the validation set for the classification models with k = {50, 100, 150, 200} are presented in Appendix B.

ADA SVD - - - ADA SVD ADA SVD LS - - - ADA SVD LS ADA LS - - - ADA LS  
Table 4  
AUC significance test statistics of Delong et al. (1988) for ADA\_SVD\_LS — ADA\_SVD and ADA\_SVD\_LS — ADA\_LS

<table><tr><td>SVD</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td><td>70</td><td>80</td><td>90</td><td>100</td><td>110</td></tr><tr><td colspan="12">ADA_SVD_LS-ADA_SVD</td></tr><tr><td>AUC difference</td><td>3.038</td><td>1.988</td><td>2.122</td><td>1.490</td><td>1.310</td><td>1.495</td><td>1.797</td><td>1.762</td><td>1.448</td><td>1.159</td><td>1.317</td></tr><tr><td> $x^2$ </td><td>42.508</td><td>27.385</td><td>31.337</td><td>19.307</td><td>15.103</td><td>20.315</td><td>26.283</td><td>27.261</td><td>18.328</td><td>12.139</td><td>13.376</td></tr><tr><td>df</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>p</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td colspan="12">ADA_SVD_LS-ADA_LS</td></tr><tr><td>AUC difference</td><td>4.710</td><td>5.857</td><td>6.233</td><td>6.301</td><td>6.417</td><td>6.469</td><td>6.773</td><td>6.530</td><td>6.451</td><td>6.353</td><td>6.670</td></tr><tr><td> $\chi^2$ </td><td>73.6034</td><td>98.172</td><td>111.069</td><td>109.766</td><td>111.647</td><td>112.022</td><td>126.516</td><td>113.330</td><td>107.168</td><td>108.200</td><td>118.390</td></tr><tr><td>df</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>p</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.0001</td><td>&lt;0.001</td></tr></table>

Figs. 4 and 5 prove that the proposed methodology is valuable, stable and extendible to other timeframes. The conclusions as drawn in Section 3.3 are still valid on the out-of-period validation set. ADA\_SVD, ADA\_LS and ADA\_SVD\_LS perform also very well on the validation set. The AUC lies in the range of 83.51 and 90.48, while the PCC of all models exceeds the proportional chance criterion of $5 6 . 0 6 ~ ( = ~ 0 . 3 2 5 9 ^ { 2 } + ( \bar { 1 } - \bar { 0 } . 3 2 5 9 ) ^ { 2 } )$ [17]. Figs. 4 and 5 show that ADA\_SVD\_LS significantly outperforms ADA\_SVD and ADA\_LS on the validation set in terms of AUC and PCC.

Furthermore, the robustness of this complaint management system is confirmed by comparing the performance on the test set with that on the out-ofperiod validation set. The absolute value of the AUC difference between the test set and the out-of-period validation set fluctuates between 0.008 and 1.476 AUC points over all different models (see Fig. 4). This indicates that the models are robust over the proposed time period. These results are confirmed when having a look at the absolute value of the difference in PCC (see Fig. 5). This difference fluctuates between 0.063 and 1.535 PCC points.

![](/api/attachments/ERN4TPJM/fulltext/images/43502956679b1ff130009a279c592d0f8a1a4c98655e2ac6a04d5e82d5e1d3a0.jpg)  
Fig. 4. The AUC performance on the test (solid line) and validation set (dashed line) of ADA\_SVD, ADA\_SVD\_LS and ADA\_LS.

<table><tr><td>120</td><td>130</td><td>140</td><td>150</td><td>160</td><td>170</td><td>180</td><td>190</td><td>200</td></tr><tr><td>1.250</td><td>1.820</td><td>1.365</td><td>1.143</td><td>1.512</td><td>1.214</td><td>1.093</td><td>1.528</td><td>1.217</td></tr><tr><td>14.104</td><td>29.678</td><td>15.290</td><td>11.127</td><td>19.811</td><td>12.028</td><td>10.442</td><td>18.294</td><td>12.796</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>6.466</td><td>6.699</td><td>6.571</td><td>6.341</td><td>6.659</td><td>6.537</td><td>6.326</td><td>6.756</td><td>6.705</td></tr><tr><td>109.018</td><td>116.827</td><td>114.625</td><td>102.791</td><td>115.494</td><td>112.497</td><td>106.401</td><td>119.710</td><td>118.243</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr></table>

In summary, applying these classifiers to a new timeframe does not result in a drastic drop in performance. Contrary, implementing the proposed methodology within a call-center environment is a valuable strategy to improve customer complaint management.

## 4. Conclusions and direction for further research

Due to the strong increase in Internet penetration, a lot of customers write an email as a substitute for traditional communication methods as for instance a letter or a telephone call. As a consequence, companies receive daily a huge amount of emails. Nowadays, companies outsource their internal email management to a specialized call-center environment. Efficient email handling becomes one of the major key challenges in business. This study focuses on how a company can optimize its complaint-handling strategies through an automatic email-classification system. Indeed, practitioners and academics feel the need for an efficient and successful complaint-handling strategy, because recovering service failures as quick as possible results in additional benefits.

![](/api/attachments/ERN4TPJM/fulltext/images/877b62e0012eee7485b0f2cd5703e2dcfeb1ace2f03f8957711e08d6351505a1.jpg)  
ADA SVD - - - ADA SVD ADA SVD LS - - - ADA SVD LS ADA LS - - - ADA LS  
Fig. 5. The PCC on the test (solid line) and validation set (dashed line) of ADA\_SVD, ADA\_SVD\_LS and ADA\_LS.

Table 5  
Real-life call-center example

<table><tr><td rowspan="3">Call-center setting</td><td colspan="5">Discounted Cost per Year (in Euro)</td><td rowspan="3">Total Cost after 5 year (in Euro)</td><td rowspan="3">Additional savings over manual labeling after 5 year (in Euro)</td></tr><tr><td colspan="5">Year</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Manual labeling</td><td>7250</td><td>6971</td><td>6703</td><td>6445</td><td>6197</td><td>33,567</td><td></td></tr><tr><td>Automatic email classification</td><td>1813</td><td>1743</td><td>1676</td><td>1611</td><td>1549</td><td>8392</td><td>25,175</td></tr></table>

This study offers an automatic email-classification system that distinguishes complaints from non-complaints. In contrast to manually encoding the incoming emails, this study offers a feasible methodology to automate this process. As a result, email handling becomes less timeconsuming and less expensive due to the lower labor costs. Table 5 indicates that implementing the current methodology in a real-life call-center setting saves a lot of resources within this specific case.

Suppose that in the current situation, an employee labels an incoming email at a realistic 45 s per email or 80 email messages per hour, whereas the explicit cost of relabeling falsely called complaints as non-complaints or visa versa is similar. Moreover, the call center receives about 20,000 emails a year. Table 5 shows that the total costs over 5 years with 20,000 email messages a year for manually labeling is about 33,567 Euros having a discount rate of 4% and a gross employee cost of 29 Euros per hour. If the call center implements the proposed methodology, resources are saved. Knowing that the email-classification system easily succeeds in classifying 83% of the email messages correctly, the call center saves approximately 25,175 Euros over a 5-year period supposing a labeling efficiency gain of 75%. Indeed, the employee's timeconsuming labeling task gives way to a less expensive rearranging task of the correctly classified email set.

Furthermore, there is a possibility to treat incoming complaints in a separate way than other email types during the email-handling process. Transferring complaints to a separate complaint-handling department with well-trained complaint handlers should result in a more successful and faster complaint treatment which results in an overall increase of customer satisfaction.

Moreover, this study explores the differences in linguistic style between complaints and non-complaints. The probability of having a complaint email increases when more words and time indications are used. In contrast to for instance an information request, the likelihood of being a complaint is positively related with the present and past tense, while it decreases when more future tenses and question marks are used. Furthermore, the possibility of classifying an incoming email as a complaint increases when the tone of email becomes more antagonistic — i.e. it contains more negations, more numbers and more clenched words. Offending the company by using a lot of second person pronouns – e.g. you are responsible for the misdelivery of the newspaper – increases the chance of having a complaint.

Furthermore, this study proves that adding linguistic style features as an additional set of predictors in a traditional text-classification model significantly increases the predictive performance. In addition, the robustness of the proposed methodology is confirmed by validating the text-classification models on an out-ofperiod dataset.

While we believe that this study contributes to today's literature, some shortcomings and directions for future research are given. First of all, it is not clear whether adding linguistic style predictors in other text-classification tasks will result in the same highly beneficial increase in predictive performance. Additional experiments need to be done to answer this question. Moreover, additional efforts can be done to refine the proposed methodology. For instance, automatically detecting different types of complaints (e.g. delivery problems, financial problems…) would give us valuable and in-depth information on the occurring problems and service failures that customer encounter.

## Acknowledgments

We would like to thank (1) the anonymous Belgian company for providing us with data for testing our research questions, (2) Ghent University for funding the PhD project of Kristof Coussement (BOF 01D26705), (3) Bart Larivière, Jonathan Burez and Ilse Bellinck for their insights during this project. This project was realized using SAS v9.1.3, SAS Text Miner v2.3 and Matlab v7.0.4.

## Appendix A

ROCs on test set for ADA\_SVD, ADA\_SVD\_LS and ADA\_LS for k={50, 100, 150, 200}.

![](/api/attachments/ERN4TPJM/fulltext/images/7079291a2de6aa8bcf422b7a80a620180c80c82bd33bcf3c18836bea8f02728c.jpg)

![](/api/attachments/ERN4TPJM/fulltext/images/ca1df72047bb08601e6386eee9b4b86d923c6d8f60816923e9cce6ed1db26a1d.jpg)

![](/api/attachments/ERN4TPJM/fulltext/images/0e6cee1a3479cb4d121f03172a0b36d74c7fc6ec41afebf993bdc64468b18e23.jpg)

![](/api/attachments/ERN4TPJM/fulltext/images/6120d9b6b7c7a529991dd0f31464d326f216af29dbc7988d99ff4517901abd34.jpg)

## Appendix B

ROCs on validation set for ADA\_SVD, ADA\_ SVD\_LS and ADA\_LS for k={50, 100, 150, 200}.

![](/api/attachments/ERN4TPJM/fulltext/images/e5b50538c6b2b501e6c622244a600cc49e817950a4d63e456cf2a645d773fd67.jpg)

![](/api/attachments/ERN4TPJM/fulltext/images/8249a9bbae76377d4433da4a6573439411fd07cc0cc92b69a9e7882bd4dfa326.jpg)

![](/api/attachments/ERN4TPJM/fulltext/images/5dd48b21369477a91ca1b602cc99cdc2a62eaeb969d1ed68bbfe706d86461bb8.jpg)

![](/api/attachments/ERN4TPJM/fulltext/images/c5b9c96419f7d2fd3b86795e40d4a36f120fa984538a4ad81610863dbcc529c1.jpg)

## References

[1] C. Aasheim, G.J. Koehler, Scanning world wide web documents with the vector space model, Decision Support Systems 42 (2) (2006).

[2] B. Baesens, S. Viaene, D. Van den Poel, J. Vanthienen, G. Dedene, Bayesian neural network learning for repeat purchase modeling in direct marketing, European Journal of Operational Research 138 (1) (2002).

[3] C. Bell, K.P. Jones, Toward everyday language information retrieval systems via minicomputers, Journal of the American Society for Information Science 30 (1979).

[4] R. Bougie, R. Pieters, M. Zeelenberg, Angry customers don't come back, they get back: the experience and behavioural implications of anger and dissatisfaction in services, Journal of the Academy of Marketing Science 31 (4) (2003).

[5] R.E. Bucklin, S. Gupta, Brand Choice, purchase incidence and segmentation: an integrated modeling approach, Journal of Marketing Research 29 (1992).

[6] R.C. Chen, C.H. Hsieh, Web page classification based on a support vector machine using a weighted vote schema, Expert Systems with Applications 31 (2) (2006).

[7] S. Deerweester, S. Dumais, G. Furnas, T. Landauer, R. Harshman, Indexing by latent semantic analysis, Journal of the American Society for Information Science 41 (6) (1990).

[8] E.R. DeLong, D.M. DeLong, D.L. Clarke-Pearson, Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach, Biometrics 44 (3) (1988).

[9] Y. Freund, R.E. Schapire, A decision-theoretic generalization of on-line learning and an application to boosting, Journal of Computer and System Sciences 55 (1) (1997).

[10] R.D. Gopal, A.K. Tripathi, Z.D. Walter, Economics of first-contact email advertising, Decision Support Systems 42 (3) (2006).

[11] J.A. Hanley, B.J. McNeil, The meaning and use of the area under a receiver operating characteristic (ROC) curve, Radiology 143 (1) (1982).

[12] T. Hastie, R. Tibshirani, J. Friedman, The elements of statistical learning: data mining, inference and prediction, Springer Series in Statistics, Springer-Verlag, New York, 2003.

[13] J.L. Heskett, T.O. Jones, G.W. Loveman, W.E. Sasser, L.A. Schlesinger, Putting the service-profit chain to work, Harvard Business Review 72 (March–April 1994).

[14] M.Y. Kiang, T.S. Raghu, K.H.M. Shang, Marketing on the Internet — who can benefit from an online marketing approach? Decision Support Systems 27 (4) (2000).

[15] W. Kraaij, R. Pohlmann, Viewing stemming as recall enhancement, Proceedings of the 19th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (Zurich Switzerland), 1996.

[16] C.Y. Liang, L. Guo, Z.H. Xia, F.G. Nie, X.X. Li, L.A. Su, Z.Y. Yang, Dictionary-based text categorization of chemical web pages, Information Processing and Management 42 (4) (2006).

[17] D.G. Morrison, On the interpretation of discriminant analysis, Journal of Marketing Research 6 (1969).

[18] P. Mangiameli, D. West, R. Rampal, Model selection for medical diagnosis decision support systems, Decision Support Systems 36 (3) (2004).

[19] J.W. Pennebaker, M.E. Francis, R.J. Booth, Linguistic Inquiry and Word Count (LIWC), Erlbaum Publishers, Mahwah, N.J., 2001.

[20] M. Pontes, C. Kelly, The identification of inbound call center agents' competencies that are related to callers' repurchase intentions, Journal of Interactive Marketing 14 (2000).

[21] G. Salton, A Theory of Indexing, J.W. Arrowsmith, Bristol, UK, 1975.

[22] G. Salton, Automatic Text Processing: The Transformation, Analysis and Retrieval of Information by Computer, Addison-Wesley, Reading, MA, 1989.

[23] G. Salton, C. Buckley, Term-weighting approaches in automatic text retrieval, Information Processing and Management 24 (5) (1988).

[24] G. Salton, The SMART Retrieval System: Experiments in Automatic Document Processing, Prentice Hall, Englewood Cliffs, NJ, 1971.

[25] R.E. Schapire, Y. Singer, BoosTexter: a boosting-based system for text categorization, Machine Learning 39 (2–3) (2000).

[26] A.K. Smith, R.N. Bolton, The effect of customers' emotional responses to service failures on their recovery effort evaluations and satisfaction judgments, Journal of the Academy of Marketing Science 30 (2002).

[27] K. Sparck Jones, Index term weighting, Information Storage and Retrieval 9 (11) (1973).

[28] S.S. Tax, S.W. Brown, Recovering and learning from service failures, Sloan Management Review 40 (1) (1998).

[29] S.S. Weng, C.K. Liu, Using text classification and multiple concepts to answer emails, Expert Systems with Applications 26 (4) (2004).

[30] H. Zijlstra, T. van Meerveld, H. van Middendorp, J.W. Pennebaker, R. Geenen, Dutch version of the Linguistic Inquiry and Word Count (LIWC); a computerized text analysis program, Behaviour and Health (Dutch journal) 32 (2004).

![](/api/attachments/ERN4TPJM/fulltext/images/05b35cd2a6b70c0835f7112fe609ad4e6abcb5f34ad293edea0cc05fd37917b6.jpg)

Kristof Coussement is a Customer Intelli gence researcher in the Faculty of Applied Economics and Business Administration at Ghent University, (Belgium). He received his Master degree in Applied Economics as well as his Master after Master degree in Marketing Analysis at Ghent University (Belgium). During his research project, he investigates the impact of client/company interactions through verbalized information sources on Customer Relationship Marketing (churn ana

lysis, customer complaint management, etc.).

![](/api/attachments/ERN4TPJM/fulltext/images/ee130458729835ee9a3e6ac9fdbc5589ae9eee03b2ba4c958e18397c9f3b1ec3.jpg)

Dirk Van den Poel is professor of marketing at the Faculty of Economics and Business Administration of Ghent University, Belgium. He heads a competence center on analytical customer relationship management (aCRM). He received his degree of management/business engineer as well as his PhD from K.U. Leuven (Belgium). His main interest fields are the quantitative analysis of consumer behavior (CRM), data mining (genetic algorithms, neural networks, random forests, random

multinomial logit: RMNL), text mining, optimal marketing resource allocation (DIMAROPT) and operations research.
