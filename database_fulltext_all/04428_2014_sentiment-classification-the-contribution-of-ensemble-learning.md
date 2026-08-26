---
otero_id: 4428
otero_key: "ABQKEKXN"
title: "Sentiment classification: The contribution of ensemble learning"
authors: "Gang Wang; Jianshan Sun; Jian Ma; Kaiquan Xu; Jibao Gu"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.08.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning

Gang Wang <sup>a,b,c,</sup>⁎, Jianshan Sun <sup>c,d</sup>, Jian Ma <sup>c</sup>, Kaiquan Xu <sup>e</sup>, Jibao Gu <sup>d</sup>

<sup>a</sup> School of Management, Hefei University of Technology, Hefei, Anhui 230009, PR China

<sup>b</sup> Key Laboratory of Process Optimization and Intelligent Decision-making, Ministry of Education, Hefei, Anhui, PR China

<sup>c</sup> Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon, Hong Kong

<sup>d</sup> School of Management, University of Science and Technology of China, Hefei, Anhui, PR China

<sup>e</sup> Department of Electronic Commerce, School of Business, Nanjing University, Nanjing, Jiangsu 210093, PR China

## a r t i c l e i n f o

Article history: Received 27 August 2012 Received in revised form 1 August 2013 Accepted 5 August 2013 Available online xxxx

Keywords: Sentiment classi<sup>fi</sup>cation Ensemble learning Bagging Boosting Random Subspace

## a b s t r a c t

With the rapid development of information technologies, user-generated contents can be conveniently posted online. While individuals, businesses, and governments are interested in evaluating the sentiments behind this content, there are no consistent conclusions on which sentiment classi<sup>fi</sup>cation technologies are best. Recent studies suggest that ensemble learning methods may have potential applicability in sentiment classi<sup>fi</sup>cation. In this study, we conduct a comparative assessment of the performance of three popular ensemble methods (Bagging, Boosting, and Random Subspace) based on <sup>fi</sup>ve base learners (Naive Bayes, Maximum Entropy, Decision Tree, K Nearest Neighbor, and Support Vector Machine) for sentiment classi<sup>fi</sup>cation. Moreover, ten public sentiment analysis datasets were investigated to verify the effectiveness of ensemble learning for sentiment analysis. Based on a total of 1200 comparative group experiments, empirical results reveal that ensemble methods substantially improve the performance of individual base learners for sentiment classi<sup>fi</sup>cation. Among the three ensemble methods, Random Subspace has the better comparative results, although it was seldom discussed in the literature. These results illustrate that ensemble learning methods can be used as a viable method for sentiment classi<sup>fi</sup>cation

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

With the rapid development of information technologies, usergenerated contents can be easily posted online [1]. The sheer volume and exponential growth of this information provide potential value to governments, businesses, and users themselves. For instance, governments can evaluate online citizen-generated texts to assess public sentiment for making policies. Furthermore, many customer-generated reviews of products and services have become valuable sources for market analysis; these reviews are used to set business strategy of E-commerce websites, such as Amazon.com and Epinion.com [50]. Online users can also bene<sup>fi</sup>t from reading others' opinions through recommender systems.

There is an inherent property called sentiment involved in the vast majority of online-generated content. Sentiment is an opinion or feeling you have about something [12]. In this study of sentiment classi<sup>fi</sup>cation, we focus on attempts to identify the sentiment polarity of a given text, which is traditionally classi<sup>fi</sup>ed as either positive or negative. Analyzing and predicting the polarity of the sentiment plays an important role in understanding social phenomena and general society trends [6].

Accordingly, sentiment classi<sup>fi</sup>cation has become a popular research topic [1,4,6]. The sentiment classi<sup>fi</sup>cation problem was initially tackled granularly at the levels of document, sentence, clause, phrase, and word, depending on the speci<sup>fi</sup>c objectives of applications. Heuristicbased methods and machine learning approaches were frequently employed in previous research. Heuristic-based methods were primarily used in conjunction with linguistic characters and semantic features. For example, Turney [38] used mutual information with prede<sup>fi</sup>ned sentiment words to score other phrase tags, therefore identifying the sentiment of documents. In parallel, many studies focused on using machine learning algorithms to classify sentiment. For instance, Support Vector Machines (SVM) and Naive Bayes (NB) are commonly used to identity sentiment, due to their predictive power. Pang et al. [29] conducted an empirical study in sentiment classi<sup>fi</sup>cation, concluding that SVM outperformed other classi<sup>fi</sup>ers such as NB. In recent years, there has been a growing interest in using ensemble learning techniques, which combine the outputs of several base classi<sup>fi</sup>cation techniques to form an integrated output, to enhance classi<sup>fi</sup>cation accuracy [43,48]. However, compared with other research domains, related work about ensemble methods contributing to sentiment classi<sup>fi</sup>cation are still limited and more extensive experimental work is needed in this area.

To <sup>fi</sup>ll this research gap, this paper makes a comparative study of the effectiveness of ensemble learning for sentiment classi<sup>fi</sup>cation and demonstrates that three popular ensemble methods (Bagging [5], Boosting [33] and Random Subspace [19]) can be useful. Research in many areas has shown the advantages of ensemble methods both theoretically and empirically [30,51]. In ensemble methods, learners composing an ensemble are usually called base learners. In Bagging, the base learners are constructed using random independent bootstrap replicates from a training dataset, and the <sup>fi</sup>nal result is calculated by a simple majority vote [5,51]. In Boosting, the base learners are constructed on weighted versions of the training set, which are dependent on previous base learners' results and the <sup>fi</sup>nal result is calculated by a simple vote or a weighted majority vote [33,51]. In Random Subspace, the base learners are constructed in random subspaces of the feature space [19,51].

Table 1  
Selected previous studies in ensemble learning for sentiment analysis

<table><tr><td>Study</td><td>Year</td><td>Feature set</td><td>Base learner</td><td>Ensemble methods</td><td>Dataset</td></tr><tr><td>Wilson et al. [45]</td><td>2006</td><td>N-gram, syntactic features</td><td>DT</td><td>Boosting</td><td>MPQA dataset</td></tr><tr><td>Tsutsumi et al. [37]</td><td>2007</td><td>N-gram</td><td>SVM, ME, Scoring</td><td>Stacking</td><td>Movie review dataset</td></tr><tr><td>Abbasi et al. [2]</td><td>2008</td><td>N-gram, lexicon</td><td>SVM</td><td>SVRCE</td><td>Two web forum datasets</td></tr><tr><td>Lu &amp; Tsou [26]</td><td>2010</td><td>N-gram, lexicon</td><td>NB, ME, SVM, Scoring</td><td>Stacking</td><td>NTCIR opinion dataset</td></tr><tr><td>Whitehead &amp; Yaeger et al. [43]</td><td>2010</td><td>N-gram</td><td>SVM</td><td>Bagging, Boosting and Random Subspace</td><td>Five product review datasets</td></tr><tr><td>Xia et al. [48]</td><td>2011</td><td>POS and word-relation based features</td><td>NB, ME, SVM</td><td>Stacking</td><td>Five product review datasets</td></tr><tr><td>Su et al. [34]</td><td>2012</td><td>N-gram</td><td>NB, CB, KNN, ME, SVM</td><td>Stacking</td><td>Three product review datasets</td></tr><tr><td>Li et al. [24]</td><td>2012</td><td>N-gram, lexicon</td><td>SVM, KNN, Scoring</td><td>Stacking</td><td>Chinese review dataset</td></tr></table>

We employed ten public sentiment analysis datasets to verify the effectiveness of these three ensemble methods when using <sup>fi</sup>ve base learners (NB, Maximum Entropy (ME), Decision Tree (DT), K Nearest Neighbors (KNN), and SVM). Based on a total of 1200 comparative group experiments, empirical results show that ensemble learning methods achieve better performances than base learners. Among the three ensemble methods, Random Subspace has the better comparative results except with NB as base learner, although it was seldom discussed in the literature. In addition, RS-SVM had the highest average accuracy in 6 datasets and similar results with other methods in the other 4 datasets. These results illustrate that ensemble learning methods can be used as a viable method for identifying sentiment polarities.

The main contribution of this paper is to verify the effectiveness of using ensemble learning for sentiment classi<sup>fi</sup>cation. The remainder of the paper is organized as follows. In Section 2, we survey the related work about sentiment classi<sup>fi</sup>cation. The details of three different types of ensemble methods are introduced in Section 3. Section 4 presents the design and methodology used in the experiments, while the results are analyzed in Section 5. Section 6 discusses conclusions and future research directions.

## 2. Literature review

Since the late 1990s, sentiment classi<sup>fi</sup>cation has been a hot research topic in the areas of data mining, information retrieval, and natural language processing [4,28]. Many researchers have investigated sentiment classi<sup>fi</sup>cation from different perspectives. Due to the linguistic characteristics involved, sentiment analysis is done at different levels of text units. A word, phrase, clause, sentence, or document may become the text unit in analysis [28]. In order to capture the sentiment of individual words or phrases, a measure of the strength of sentiment polarity is often de<sup>fi</sup>ned to quantify how strongly a word or phrase is judged to be positive or negative [9,22,35,38]. Furthermore, Thet et al. [36] computed the sentiment of a clause from individual word sentiment scores, considering the grammatical dependency structure of the clause. Other studies used sentence-level attempts to classify the positive or negative sentiments for each sentence [49,50]. The greatest amount of work has been done on document level polarity categorization [1,4,11,29,43,48]. This is also the focus level of our study. The techniques for sentiment classi<sup>fi</sup>cation in prior research can be classi<sup>fi</sup>ed into heuristic-based methods and machine learning methods.

## 2.1. Heuristic-based methods for sentiment classification

By means of prede<sup>fi</sup>ned lexicons and calculation rules, heuristicbased methods generally classify text sentiments based on the total number of derived positive or negative sentiment features [28]. For example, Hatzivassiloglou and McKeown [18] considered that adjectives are more predictive of sentiment classi<sup>fi</sup>cation and predicted the sentiment of adjectives by inspecting them in conjunction with “and,” “or,” “but,” “either/or,” and “neither/nor.” However this approach may overestimate the importance of adjectives and underestimate some

![](/api/attachments/ABQKEKXN/fulltext/images/49586fc56b77473664012b3a98729c51692a26cc0b24497f0f2edd6faba98b14.jpg)  
Fig. 1. The Bagging process.

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

G. Wang et al. / Decision Support Systems xxx (2013) xxx–xxx

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Data set  $D=\left\{(x_{1},y_{1}),(x_{2},y_{2}),\cdots,(x_{m},y_{m})\right\}$ ;
Base learning algorithm L;
Number of learning rounds T.
Process:
For  $t=1,2,\cdots,T$ :
 $D_{t}=Bootstrap(D)$ ; % Generate a bootstrap sample from D
 $h_{t}=L(D_{t})$  % Train a base learner  $h_{t}$  from the bootstrap sample end.
Output:  $H(x)=\arg\max_{y\in Y}\sum_{t=1}^{T}1(y=h_{t}(x))$  % the value of  $1(\alpha)$  is 1 if  $\alpha$  is true
% and 0 otherwise
</div>

Fig. 2. The Bagging algorithm.

![](/api/attachments/ABQKEKXN/fulltext/images/8d6052f2bbe663b7fa12099ffb5409a04df5538f6f1aa15377f5efa2f6c250a1.jpg)  
Fig. 3. The AdaBoost process.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Data set  $D=\left\{(x_{1},y_{1}),(x_{2},y_{2}),\cdots,(x_{m},y_{m})\right\}$ ;
Base learning algorithm L;
Number of learning rounds T.
Process:
 $D_{1}(i)=1/m.\quad\%$  Initialize the weight distribution
For  $t=1,2,\cdots,T:$ $h_{t}=L(D,D_{t});\quad\%$  Train a base learner  $h_{t}$  from D using distribution  $D_{t}$ $\varepsilon_{t}=\operatorname{Pr}_{i\sim D_{t}}[h_{t}(x_{i}\neq y_{i})];\quad\%$  Measure the error of  $h_{t}$ $\alpha_{t}=\frac{1}{2}\ln\frac{1-\varepsilon_{t}}{\varepsilon_{t}};\quad\%$  Determine the weight of  $h_{t}$ $D_{t+1}(i)=\frac{D_{t}(i)}{Z_{t}}\times\left\{\begin{aligned}\exp(-\alpha_{t})&amp;if h_{t}(x_{i})=y_{i}\\ \exp(\alpha_{t})&amp;f h_{t}(x_{i})\neq y_{i}\end{aligned}\%\right.$  Update the distribution, where  $Z_{t}$  is a
 $=\frac{D_{t}(i)\exp(-\alpha_{t}y_{i}h_{t}(x_{i}))}{Z_{t}}\%$ normalization factor which enables  $D_{t+1}$  to be a distribution end.
Output:  $H(x)=\text{sign}(f(x))=\text{sign}\sum_{t=1}^{T}\alpha_{t}h_{t}(x)$
</div>

Fig. 4. The AdaBoost algorithm.  
```txt
Please cite this article as: G. Wang, et al., Sentiment classification: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002
```

![](/api/attachments/ABQKEKXN/fulltext/images/200f35fe4101a2aee031c6bed12f82ad0a90178309427032a1d58bdb085eb829.jpg)  
Fig. 5. The Random Subspace process.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Data set  $D=\left\{(x_{1},y_{1}),(x_{2},y_{2}),\cdots,(x_{m},y_{m})\right\}$ ;
Base classifier algorithm L;
Number of random subspace rate k;
Number of learning rounds T.
Process:
For  $t=1,2,\cdots,T$ :
 $D_{t}=RS(D,k)$ ; % Random generate a subspace sample from D
 $h_{t}=L(D_{t})$ ; % Train a base classifier  $h_{t}$  from the subspace sample end.
Output:  $H(x)=\arg\max_{y\in Y}\sum_{t=1}^{T}1(y=h_{t}(x))$ ; % the value of  $1(\alpha)$  is 1 if  $\alpha$  is true
% and 0 otherwise
</div>

Fig. 6. The Random Subspace algorithm.

Table 2  
Description of sentiment analysis datasets.

<table><tr><td>Dataset</td><td>Description</td><td># of features (Unigram)</td><td># of features (Bigram)</td><td># of instances</td><td>Source</td></tr><tr><td>Camera</td><td>Digital camera reviews from Amazon.com. These reviews were taken from cameras that had a large number of ratings. This dataset and the laptop review set both fall under the broader domain of consumer electronics.</td><td>1352</td><td>1704</td><td>498 (250:248)</td><td>[42]</td></tr><tr><td>Camp</td><td>Summer camp reviews from CampRatingz.com. A significant number of these reviews were written by the young people who attended the summer camps.</td><td>2045</td><td>1735</td><td>804 (402:402)</td><td>[42]</td></tr><tr><td>Doctor</td><td>Reviews of physicians from RateMDs.com. This dataset and the lawyer review set could both be considered part of the larger “ratings of people” domain.</td><td>1578</td><td>1679</td><td>1478 (739:739)</td><td>[42]</td></tr><tr><td>Drug</td><td>Reviews of pharmaceutical drugs from DrugRatingz.com.</td><td>1438</td><td>1662</td><td>802 (401:401)</td><td>[42]</td></tr><tr><td>Laptop</td><td>Laptop reviews from Amazon.com. Various laptops are reviewed from different manufacturers.</td><td>2010</td><td>3136</td><td>176 (88:88)</td><td>[42]</td></tr><tr><td>Lawyer</td><td>Reviews of lawyers from LawyerRatingz.com.</td><td>2474</td><td>7734</td><td>220 (110:110)</td><td>[42]</td></tr><tr><td>Movie</td><td>Movie reviews of various movies from (Pang and Lee [27,29]).</td><td>1165</td><td>1232</td><td>2000 (1000:1000)</td><td>[27,29]</td></tr><tr><td>Music</td><td>Musical CD reviews from Amazon.com. The albums being reviewed were recently released popular music from a variety of musical genres.</td><td>1398</td><td>1705</td><td>582 (291:291)</td><td>[42]</td></tr><tr><td>Radio</td><td>Reviews of radio shows from RadioRatingz.com. This dataset and the TV dataset had the shortest reviews on average.</td><td>1923</td><td>3054</td><td>1004 (502:502)</td><td>[42]</td></tr><tr><td>TV</td><td>Television show reviews from TVRatingz.com. These reviews were typically very short and not very detailed.</td><td>2834</td><td>9195</td><td>470 (235:235)</td><td>[42]</td></tr></table>

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

Confusion matrix for sentiment classi<sup>fi</sup>cation.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Actual condition</td></tr><tr><td>Positive sentiment</td><td>Negative sentiment</td></tr><tr><td rowspan="2">Test result</td><td>Positive sentiment</td><td>True positive (TP)</td><td>False positive (FP)</td></tr><tr><td>Negative sentiment</td><td>False negative (FN)</td><td>True negative (TN)</td></tr></table>

predictive words of other parts-of-speech. Along this line, Turney [38] determined the semantic orientation of a phrase using its point-wise mutual information with prede<sup>fi</sup>ned sentiment words, such as “excellent”

and “poor.” Therefore, sentiment classi<sup>fi</sup>cation can be achieved by aggregating the overall sentiment information of phrases. The adjective– verb–adverb (AVA) combinations were thoroughly analyzed in [35] for sentiment polarity predication. There are also other fruitful studies following this line [20,49].

The heuristic-based methods are similar to using knowledge engineering methods to classify text sentiment. One of the problems of this approach is it relies heavily on pre-de<sup>fi</sup>ned lexicons and rules that are dif<sup>fi</sup>cult to update and use in multiple domains [28]. In this research, we focus on machine learning methods for sentiment classi<sup>fi</sup>cation.

![](/api/attachments/ABQKEKXN/fulltext/images/7fc910bdce12c4a18e40e3b002c92ec442f6058ebfa7cddc8a3f22fb5629145b.jpg)  
Fig. 7. Experimental procedure.

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

G. Wang et al. / Decision Support Systems xxx (2013) xxx–xxx

## 2.2. Machine learning methods for sentiment classification

Machine learning approaches for sentiment classi<sup>fi</sup>cation have been extensively studied, due to their predominant classi<sup>fi</sup>cation performance [2,28]. By constructing predictive models from labeled training datasets, these methods can model more features and adapt to changing inputs more robustly, than heuristic-based methods [28]. Machine learning methods for sentiment classi<sup>fi</sup>cation typically consist of two steps: (1) extraction of features from training data and their conversion to feature vectors and (2) training of the classi<sup>fi</sup>er on the feature vectors and application of the classi<sup>fi</sup>er to unseen instances [23]. Accordingly, both feature construction and learning method are crucial for accurate sentiment classi<sup>fi</sup>cation.

sentiment classi<sup>fi</sup>cation, they need speci<sup>fi</sup>c domain knowledge and are dif<sup>fi</sup>cult to update [28]. Since the aim of this study is to verify the effectiveness of using ensemble learning for sentiment classi<sup>fi</sup>cation, we use N-gram features to present the text in this research.

## 2.2.1. Feature construction

Another important problem is feature selection, a problem that has been tackled by many researchers in different ways [15,28]. However, recent studies have drawn no consistent conclusions that one technique is superior. In addition, some studies have found that feature selection was not always effective in enhancing sentiment classi<sup>fi</sup>cation accuracy [23]. Since discussions of effective feature selection are beyond the scope of this research, in this study we follow [29] and use Unigram and Bigram features.

Converting a piece of text into a feature vector is an important part of machine learning methods for sentiment classi<sup>fi</sup>cation. From the machine learning perspective, it is useful for the features to include only relevant information and also to be independent of each other [15].

The feature representation method dominating the sentiment classi-<sup>fi</sup>cation literature is known as the bag-of-words (BOW) framework [28]. In this framework, the text is considered as a bag of words and represented by a vector containing all the words appearing in the corpus. Besides BOW features, many other types of features are proposed, such as part-of-speech (POS), syntax, negation, and topic-oriented features [28]. However, these features rely heavily on linguistic resources. Popular among them are lexicons, such as SentiWordNet, General Inquire, and POS tagger [32]. In addition, the construction of these features is time consuming and tedious. Just like heuristic-based methods for

In the area of text classi<sup>fi</sup>cation, term frequency–inverse document frequency (TF–IDF) weighting has been successful. In sentiment classi-<sup>fi</sup>cation, Pang et al. pointed out that a topic is more likely to be emphasized by occurrences of certain keywords, and overall sentiment may not usually be highlighted through repeated use of the same terms [29]. To verify this point, we use three types of weights, i.e., term present (TP), term frequency (TF), and TF–IDF.

## 2.2.2. Learning methods

Many machine learning methods have been investigated for sentiment classi<sup>fi</sup>cation in the literature. Employing learning-based methods on sentiment analysis, Pang et al. [29] compared three different leaning algorithms (NB, ME, and SVM), concluding that SVM generally achieved the best results. Subsequently, many other studies attempted to improve the performance of machine learning-based sentiment classi<sup>fi</sup>cation [28]. However, within the sentiment classi<sup>fi</sup>cation community, techniques and methods are often used in narrow and separate domains and datasets, and which classi<sup>fi</sup>cation algorithms consistently perform better than others is often unclear. There is no consensus as to which methodology an algorithm developer should adopt for a given problem in a given domain. With respect to this uncertainty, it is not uncommon to construct multiple classi<sup>fi</sup>ers and then create an integrated classi<sup>fi</sup>er based on overall performance [2,45,48]. Table 1 presents selected previous studies dealing with sentiment analysis using ensemble methods.

Experiment results (Unigram-TP).

<table><tr><td colspan="6">Camera</td><td colspan="6">Camp</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $78.19 \pm 4.98$ </td><td> $78.12 \pm 5.64$ </td><td> $65.52 \pm 6.72$ </td><td> $60.02 \pm 5.92$ </td><td> $74.69 \pm 5.79$ </td><td>BL</td><td> $81.19 \pm 4.58$ </td><td> $80.06 \pm 4.81$ </td><td> $75.11 \pm 5.06$ </td><td> $67.90 \pm 4.43$ </td><td> $83.05 \pm 4.26$ </td></tr><tr><td>Bagging</td><td> $77.89 \pm 5.28$ </td><td> $76.86 \pm 5.57$ </td><td> $71.49 \pm 6.70$ </td><td> $59.25 \pm 5.92$ </td><td> $76.42 \pm 6.01$ </td><td>Bagging</td><td> $81.31 \pm 4.27$ </td><td> $80.21 \pm 4.03$ </td><td> $79.08 \pm 5.01$ </td><td> $67.50 \pm 4.47$ </td><td> $83.46 \pm 3.88$ </td></tr><tr><td>Boosting</td><td> $76.24 \pm 6.10$ </td><td> $76.72 \pm 5.64$ </td><td> $69.96 \pm 6.13$ </td><td> $60.02 \pm 5.92$ </td><td> $74.69 \pm 5.79$ </td><td>Boosting</td><td> $82.17 \pm 4.16$ </td><td> $80.06 \pm 4.81$ </td><td> $79.54 \pm 4.20$ </td><td> $67.90 \pm 4.43$ </td><td> $82.79 \pm 4.25$ </td></tr><tr><td>RS</td><td> $77.93 \pm 5.82$ </td><td> $77.71 \pm 6.13$ </td><td> $70.98 \pm 6.22$ </td><td> $62.13 \pm 6.39$ </td><td> $76.52 \pm 5.47$ </td><td>RS</td><td> $80.82 \pm 5.25$ </td><td> $81.98 \pm 3.50$ </td><td> $80.20 \pm 4.01$ </td><td> $72.71 \pm 4.72$ </td><td> $85.48 \pm 3.54$ </td></tr><tr><td colspan="6">Doctor</td><td colspan="6">Drug</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $75.02 \pm 3.51$ </td><td> $74.01 \pm 3.97$ </td><td> $74.74 \pm 3.27$ </td><td> $65.98 \pm 3.26$ </td><td> $83.13 \pm 2.81$ </td><td>BL</td><td> $68.87 \pm 5.23$ </td><td> $60.54 \pm 6.54$ </td><td> $56.10 \pm 5.29$ </td><td> $52.98 \pm 5.22$ </td><td> $67.29 \pm 4.94$ </td></tr><tr><td>Bagging</td><td> $74.93 \pm 3.49$ </td><td> $73.88 \pm 3.38$ </td><td> $80.71 \pm 3.06$ </td><td> $64.80 \pm 3.35$ </td><td> $84.74 \pm 2.72$ </td><td>Bagging</td><td> $68.70 \pm 5.61$ </td><td> $63.79 \pm 6.17$ </td><td> $62.19 \pm 4.73$ </td><td> $53.94 \pm 4.98$ </td><td> $68.24 \pm 4.63$ </td></tr><tr><td>Boosting</td><td> $81.12 \pm 3.90$ </td><td> $68.20 \pm 4.77$ </td><td> $79.67 \pm 2.99$ </td><td> $65.70 \pm 3.28$ </td><td> $83.67 \pm 2.97$ </td><td>Boosting</td><td> $68.56 \pm 5.09$ </td><td> $62.34 \pm 6.61$ </td><td> $60.89 \pm 5.17$ </td><td> $52.98 \pm 5.22$ </td><td> $66.88 \pm 4.74$ </td></tr><tr><td>RS</td><td> $74.78 \pm 3.69$ </td><td> $73.46 \pm 4.00$ </td><td> $80.59 \pm 2.98$ </td><td> $67.59 \pm 3.66$ </td><td> $85.97 \pm 2.94$ </td><td>RS</td><td> $68.69 \pm 5.42$ </td><td> $61.89 \pm 5.37$ </td><td> $62.58 \pm 4.88$ </td><td> $56.18 \pm 5.29$ </td><td> $70.26 \pm 5.41$ </td></tr><tr><td colspan="6">Laptop</td><td colspan="6">Lawyer</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $79.90 \pm 9.38$ </td><td> $71.38 \pm 8.69$ </td><td> $64.42 \pm 11.50$ </td><td> $51.76 \pm 11.69$ </td><td> $79.29 \pm 9.00$ </td><td>BL</td><td> $80.93 \pm 7.14$ </td><td> $76.73 \pm 8.91$ </td><td> $66.25 \pm 10.18$ </td><td> $64.27 \pm 10.52$ </td><td> $83.55 \pm 7.47$ </td></tr><tr><td>Bagging</td><td> $79.52 \pm 9.16$ </td><td> $69.33 \pm 8.12$ </td><td> $68.45 \pm 11.11$ </td><td> $51.29 \pm 11.34$ </td><td> $79.96 \pm 8.90$ </td><td>Bagging</td><td> $81.14 \pm 7.63$ </td><td> $75.09 \pm 9.20$ </td><td> $72.00 \pm 9.40$ </td><td> $63.45 \pm 10.61$ </td><td> $83.36 \pm 7.89$ </td></tr><tr><td>Boosting</td><td> $77.87 \pm 9.66$ </td><td> $70.59 \pm 8.69$ </td><td> $69.83 \pm 10.38$ </td><td> $51.76 \pm 11.69$ </td><td> $79.29 \pm 9.00$ </td><td>Boosting</td><td> $81.19 \pm 8.73$ </td><td> $75.91 \pm 8.91$ </td><td> $72.82 \pm 9.14$ </td><td> $64.27 \pm 10.52$ </td><td> $83.55 \pm 7.47$ </td></tr><tr><td>RS</td><td> $78.78 \pm 9.38$ </td><td> $71.09 \pm 9.18$ </td><td> $71.05 \pm 11.37$ </td><td> $57.58 \pm 10.96$ </td><td> $78.48 \pm 9.51$ </td><td>RS</td><td> $80.96 \pm 7.32$ </td><td> $79.18 \pm 9.67$ </td><td> $72.64 \pm 9.78$ </td><td> $68.41 \pm 10.42$ </td><td> $83.82 \pm 7.65$ </td></tr><tr><td colspan="6">Movie</td><td colspan="6">Music</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $81.36 \pm 2.92$ </td><td> $61.57 \pm 3.56$ </td><td> $65.85 \pm 3.53$ </td><td> $55.95 \pm 3.25$ </td><td> $79.21 \pm 2.30$ </td><td>BL</td><td> $65.86 \pm 5.50$ </td><td> $67.49 \pm 6.58$ </td><td> $59.23 \pm 5.45$ </td><td> $49.83 \pm 5.75$ </td><td> $68.73 \pm 5.81$ </td></tr><tr><td>Bagging</td><td> $81.12 \pm 2.97$ </td><td> $71.81 \pm 3.25$ </td><td> $74.39 \pm 2.95$ </td><td> $56.39 \pm 3.27$ </td><td> $81.26 \pm 2.33$ </td><td>Bagging</td><td> $66.13 \pm 5.79$ </td><td> $70.03 \pm 5.81$ </td><td> $64.48 \pm 6.42$ </td><td> $50.14 \pm 5.48$ </td><td> $70.03 \pm 5.45$ </td></tr><tr><td>Boosting</td><td> $82.49 \pm 2.87$ </td><td> $61.15 \pm 3.56$ </td><td> $73.35 \pm 3.15$ </td><td> $55.95 \pm 3.25$ </td><td> $79.21 \pm 2.30$ </td><td>Boosting</td><td> $69.83 \pm 4.95$ </td><td> $68.72 \pm 6.58$ </td><td> $63.92 \pm 5.46$ </td><td> $49.83 \pm 5.75$ </td><td> $68.73 \pm 5.81$ </td></tr><tr><td>RS</td><td> $80.95 \pm 2.89$ </td><td> $79.92 \pm 3.05$ </td><td> $74.61 \pm 3.10$ </td><td> $60.79 \pm 3.64$ </td><td> $82.54 \pm 2.50$ </td><td>RS</td><td> $65.89 \pm 5.90$ </td><td> $65.98 \pm 5.84$ </td><td> $63.35 \pm 6.31$ </td><td> $54.55 \pm 4.87$ </td><td> $71.41 \pm 5.05$ </td></tr><tr><td colspan="6">Radio</td><td colspan="6">TV</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $67.79 \pm 5.57$ </td><td> $65.08 \pm 4.43$ </td><td> $62.00 \pm 5.11$ </td><td> $59.46 \pm 4.33$ </td><td> $72.36 \pm 4.25$ </td><td>BL</td><td> $71.90 \pm 6.17$ </td><td> $72.04 \pm 6.61$ </td><td> $62.87 \pm 6.72$ </td><td> $60.64 \pm 5.61$ </td><td> $77.94 \pm 5.55$ </td></tr><tr><td>Bagging</td><td> $67.99 \pm 5.56$ </td><td> $63.96 \pm 3.39$ </td><td> $66.17 \pm 5.69$ </td><td> $59.30 \pm 4.21$ </td><td> $72.39 \pm 4.32$ </td><td>Bagging</td><td> $71.87 \pm 6.16$ </td><td> $69.79 \pm 6.66$ </td><td> $68.66 \pm 7.21$ </td><td> $59.64 \pm 5.91$ </td><td> $77.26 \pm 5.62$ </td></tr><tr><td>Boosting</td><td> $70.84 \pm 5.39$ </td><td> $64.27 \pm 4.26$ </td><td> $65.09 \pm 5.06$ </td><td> $59.13 \pm 4.23$ </td><td> $71.74 \pm 4.50$ </td><td>Boosting</td><td> $73.65 \pm 5.83$ </td><td> $72.04 \pm 6.61$ </td><td> $66.89 \pm 7.07$ </td><td> $60.64 \pm 5.61$ </td><td> $77.94 \pm 5.55$ </td></tr><tr><td>RS</td><td> $67.31 \pm 5.60$ </td><td> $65.46 \pm 3.73$ </td><td> $65.41 \pm 5.14$ </td><td> $59.25 \pm 4.04$ </td><td> $74.14 \pm 4.40$ </td><td>RS</td><td> $70.97 \pm 6.55$ </td><td> $72.04 \pm 6.67$ </td><td> $66.89 \pm 6.16$ </td><td> $62.47 \pm 5.91$ </td><td> $76.34 \pm 6.10$ </td></tr></table>

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

Prior studies have shown that such ensemble methods have performed better than single machine learning techniques for sentiment classi<sup>fi</sup>cation [2,34,43]. For example, Wilson et al. [45] <sup>fi</sup>rst used Boosting for sentiment classi<sup>fi</sup>cation and achieved 23% to 96% improvement in accuracy. Abbasi et al. [2] proposed a new correlation ensemble method, named Support Vector Regression Correlation Ensemble (SVRCE), for affect analysis. Whitehead and Yaeger [43] compared Bagging, Boosting, and Random Subspace for sentiment classi<sup>fi</sup>cation, but in this case only one type of base learner (SVM) was considered. Xia et al. [48] made a comparative study of the effectiveness of Stacking for sentiment classi<sup>fi</sup>cation.

Although some foundational studies have investigated potential ensemble approaches in the area of sentiment classi<sup>fi</sup>cation, research has been limited and more in-depth empirical comparative work is needed. In addition, it is not known whether the ensemble learning methods will accurately predict sentiment across different domains. To <sup>fi</sup>ll this research gap, this study will conduct comprehensive empirical experiments over ten multi-domain datasets to systematically compare performance of ensemble learning methods in sentiment classi<sup>fi</sup>cation. Although Stacking method is often used for sentiment classi<sup>fi</sup>cation, the performance of Stacking is dif<sup>fi</sup>cult to analyze theoretically [30,51]. Similarly, little guidance is available on how to select base learners [30,51]. In this research, therefore, three ensemble techniques (Bagging, Boosting, and Random Subspace), using <sup>fi</sup>ve well-known base learner classi<sup>fi</sup>cation methods, are tested on ten public sentiment analysis datasets. Undoubtedly, this research will provide more insights into sentiment classi<sup>fi</sup>cation.

## 3. Ensemble learning for sentiment classi<sup>fi</sup>cation

Ensemble learning is a machine learning paradigm where multiple learners are trained to solve the same problem [30,51]. In contrast to ordinary machine learning approaches that try to learn one hypothesis from the training data, ensemble methods try to construct a set of hypotheses and combine them for use [25].

One of the earliest studies on ensemble learning is Dasarathy and Sheela's research [10], which discussed partitioning the feature space using two or more classi<sup>fi</sup>ers. In 1990, Hansen and Salamon showed that the generalization performance of an Arti<sup>fi</sup>cial Neural Network (ANN) can be improved using an ensemble of similarly con<sup>fi</sup>gured ANNs [17]. Schapire demonstrated that a strong classi<sup>fi</sup>er in Probably Approximately Correct (PAC) sense can be generated by combining weak classi<sup>fi</sup>ers through Boosting [33], the predecessor of the suite of AdaBoost algorithms. Since these seminal works, studies in ensemble learning have expanded rapidly, appearing often in the literature under many creative names and ideas [30].

The generalization ability of an ensemble method is usually much stronger than that of a single learner, which makes ensemble methods very attractive. Dietterich [14] gave three reasons based on viewing the nature of machine learning as searching a hypothesis space for the most accurate hypothesis. Firstly, the training data might not provide

Experiment results (Unigram-TF).

<table><tr><td colspan="6">Camera</td><td colspan="6">Camp</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $78.19 \pm 5.40$ </td><td> $75.77 \pm 7.25$ </td><td> $64.29 \pm 6.50$ </td><td> $59.63 \pm 6.04$ </td><td> $74.89 \pm 6.11$ </td><td>BL</td><td> $81.13 \pm 4.75$ </td><td> $82.56 \pm 5.42$ </td><td> $74.48 \pm 4.54$ </td><td> $68.02 \pm 4.67$ </td><td> $83.29 \pm 4.65$ </td></tr><tr><td>Bagging</td><td> $78.72 \pm 5.75$ </td><td> $73.93 \pm 6.52$ </td><td> $71.44 \pm 5.43$ </td><td> $58.55 \pm 6.29$ </td><td> $75.94 \pm 6.11$ </td><td>Bagging</td><td> $81.90 \pm 4.39$ </td><td> $82.42 \pm 4.21$ </td><td> $80.08 \pm 3.75$ </td><td> $67.52 \pm 5.06$ </td><td> $83.69 \pm 4.71$ </td></tr><tr><td>Boosting</td><td> $75.90 \pm 6.49$ </td><td> $75.77 \pm 7.25$ </td><td> $70.58 \pm 6.91$ </td><td> $59.63 \pm 6.04$ </td><td> $74.89 \pm 6.11$ </td><td>Boosting</td><td> $81.85 \pm 4.78$ </td><td> $82.56 \pm 5.42$ </td><td> $79.58 \pm 4.83$ </td><td> $68.02 \pm 4.67$ </td><td> $83.16 \pm 4.32$ </td></tr><tr><td>RS</td><td> $78.03 \pm 6.18$ </td><td> $71.35 \pm 6.43$ </td><td> $71.08 \pm 5.76$ </td><td> $61.45 \pm 5.68$ </td><td> $75.61 \pm 5.53$ </td><td>RS</td><td> $80.90 \pm 4.81$ </td><td> $76.97 \pm 3.97$ </td><td> $80.13 \pm 3.77$ </td><td> $72.21 \pm 5.24$ </td><td> $84.86 \pm 4.33$ </td></tr><tr><td colspan="6">Doctor</td><td colspan="6">Drug</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $74.73 \pm 3.01$ </td><td> $67.79 \pm 3.84$ </td><td> $73.66 \pm 4.02$ </td><td> $66.09 \pm 3.37$ </td><td> $82.05 \pm 2.94$ </td><td>BL</td><td> $68.78 \pm 4.59$ </td><td> $64.48 \pm 5.06$ </td><td> $57.41 \pm 5.49$ </td><td> $52.75 \pm 4.58$ </td><td> $66.72 \pm 4.95$ </td></tr><tr><td>Bagging</td><td> $74.88 \pm 3.02$ </td><td> $70.51 \pm 3.86$ </td><td> $80.37 \pm 3.19$ </td><td> $64.65 \pm 3.32$ </td><td> $84.21 \pm 3.07$ </td><td>Bagging</td><td> $69.08 \pm 4.80$ </td><td> $62.75 \pm 4.84$ </td><td> $61.90 \pm 5.05$ </td><td> $52.61 \pm 3.98$ </td><td> $67.68 \pm 4.71$ </td></tr><tr><td>Boosting</td><td> $81.58 \pm 2.90$ </td><td> $71.08 \pm 4.30$ </td><td> $78.56 \pm 4.07$ </td><td> $65.94 \pm 3.32$ </td><td> $82.66 \pm 3.53$ </td><td>Boosting</td><td> $68.07 \pm 4.73$ </td><td> $64.48 \pm 5.06$ </td><td> $61.28 \pm 6.10$ </td><td> $52.75 \pm 4.58$ </td><td> $66.81 \pm 4.78$ </td></tr><tr><td>RS</td><td> $74.70 \pm 2.91$ </td><td> $73.04 \pm 3.35$ </td><td> $80.04 \pm 3.22$ </td><td> $67.80 \pm 4.33$ </td><td> $85.84 \pm 2.50$ </td><td>RS</td><td> $68.36 \pm 4.45$ </td><td> $58.24 \pm 4.62$ </td><td> $62.38 \pm 5.05$ </td><td> $54.85 \pm 4.68$ </td><td> $68.70 \pm 5.09$ </td></tr><tr><td colspan="6">Laptop</td><td colspan="6">Lawyer</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $78.65 \pm 9.57$ </td><td> $81.35 \pm 8.37$ </td><td> $62.15 \pm 11.79$ </td><td> $51.31 \pm 10.72$ </td><td> $77.50 \pm 9.31$ </td><td>BL</td><td> $79.91 \pm 7.48$ </td><td> $87.91 \pm 6.30$ </td><td> $64.55 \pm 9.71$ </td><td> $64.27 \pm 7.91$ </td><td> $84.09 \pm 7.66$ </td></tr><tr><td>Bagging</td><td> $77.93 \pm 10.30$ </td><td> $81.33 \pm 8.29$ </td><td> $66.82 \pm 11.10$ </td><td> $52.42 \pm 9.40$ </td><td> $77.05 \pm 9.87$ </td><td>Bagging</td><td> $80.73 \pm 6.75$ </td><td> $83.50 \pm 6.82$ </td><td> $70.73 \pm 8.96$ </td><td> $63.82 \pm 8.47$ </td><td> $83.27 \pm 7.33$ </td></tr><tr><td>Boosting</td><td> $78.74 \pm 10.62$ </td><td> $81.35 \pm 8.37$ </td><td> $70.25 \pm 12.31$ </td><td> $51.31 \pm 10.72$ </td><td> $77.50 \pm 9.31$ </td><td>Boosting</td><td> $81.09 \pm 7.61$ </td><td> $87.91 \pm 6.30$ </td><td> $72.79 \pm 8.06$ </td><td> $64.27 \pm 7.91$ </td><td> $84.09 \pm 7.66$ </td></tr><tr><td>RS</td><td> $78.31 \pm 11.14$ </td><td> $84.14 \pm 8.53$ </td><td> $66.95 \pm 13.98$ </td><td> $56.99 \pm 11.85$ </td><td> $76.61 \pm 9.52$ </td><td>RS</td><td> $80.91 \pm 7.02$ </td><td> $86.00 \pm 6.19$ </td><td> $71.00 \pm 9.13$ </td><td> $69.00 \pm 8.10$ </td><td> $83.45 \pm 7.30$ </td></tr><tr><td colspan="6">Movie</td><td colspan="6">Music</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $81.15 \pm 3.33$ </td><td> $63.58 \pm 3.18$ </td><td> $66.58 \pm 2.53$ </td><td> $56.19 \pm 2.66$ </td><td> $79.11 \pm 2.40$ </td><td>BL</td><td> $66.02 \pm 7.07$ </td><td> $64.37 \pm 6.65$ </td><td> $58.32 \pm 6.78$ </td><td> $50.18 \pm 6.27$ </td><td> $68.87 \pm 6.56$ </td></tr><tr><td>Bagging</td><td> $80.98 \pm 3.17$ </td><td> $70.50 \pm 2.89$ </td><td> $74.09 \pm 3.12$ </td><td> $56.55 \pm 2.70$ </td><td> $80.79 \pm 2.76$ </td><td>Bagging</td><td> $66.12 \pm 6.77$ </td><td> $63.85 \pm 5.43$ </td><td> $64.65 \pm 6.37$ </td><td> $51.25 \pm 5.60$ </td><td> $69.69 \pm 5.49$ </td></tr><tr><td>Boosting</td><td> $82.90 \pm 2.83$ </td><td> $63.58 \pm 3.18$ </td><td> $73.03 \pm 3.18$ </td><td> $56.19 \pm 2.66$ </td><td> $79.11 \pm 2.40$ </td><td>Boosting</td><td> $70.79 \pm 6.86$ </td><td> $64.37 \pm 6.65$ </td><td> $64.65 \pm 5.68$ </td><td> $50.18 \pm 6.27$ </td><td> $68.87 \pm 6.56$ </td></tr><tr><td>RS</td><td> $80.69 \pm 3.28$ </td><td> $81.29 \pm 2.94$ </td><td> $74.79 \pm 2.93$ </td><td> $60.38 \pm 3.16$ </td><td> $81.94 \pm 2.88$ </td><td>RS</td><td> $66.40 \pm 6.78$ </td><td> $61.19 \pm 5.71$ </td><td> $63.68 \pm 6.24$ </td><td> $55.44 \pm 5.71$ </td><td> $71.21 \pm 5.68$ </td></tr><tr><td colspan="6">Radio</td><td colspan="6">TV</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $67.34 \pm 4.53$ </td><td> $63.18 \pm 6.27$ </td><td> $61.07 \pm 4.23$ </td><td> $59.10 \pm 5.35$ </td><td> $72.60 \pm 4.93$ </td><td>BL</td><td> $71.15 \pm 6.05$ </td><td> $74.43 \pm 5.68$ </td><td> $63.11 \pm 6.48$ </td><td> $61.15 \pm 6.83$ </td><td> $77.15 \pm 5.95$ </td></tr><tr><td>Bagging</td><td> $67.51 \pm 4.45$ </td><td> $69.23 \pm 4.36$ </td><td> $67.08 \pm 4.70$ </td><td> $58.39 \pm 5.35$ </td><td> $72.18 \pm 5.16$ </td><td>Bagging</td><td> $71.40 \pm 6.37$ </td><td> $71.13 \pm 6.01$ </td><td> $68.68 \pm 5.46$ </td><td> $59.87 \pm 6.42$ </td><td> $76.85 \pm 6.54$ </td></tr><tr><td>Boosting</td><td> $70.26 \pm 4.08$ </td><td> $69.39 \pm 5.39$ </td><td> $64.93 \pm 4.77$ </td><td> $58.18 \pm 5.41$ </td><td> $71.68 \pm 4.42$ </td><td>Boosting</td><td> $72.55 \pm 6.29$ </td><td> $74.43 \pm 5.68$ </td><td> $65.87 \pm 6.99$ </td><td> $61.15 \pm 6.83$ </td><td> $77.15 \pm 5.95$ </td></tr><tr><td>RS</td><td> $66.88 \pm 4.42$ </td><td> $62.57 \pm 4.85$ </td><td> $64.34 \pm 4.48$ </td><td> $59.00 \pm 3.52$ </td><td> $73.60 \pm 3.83$ </td><td>RS</td><td> $71.19 \pm 7.50$ </td><td> $75.23 \pm 6.00$ </td><td> $67.45 \pm 6.20$ </td><td> $62.55 \pm 6.96$ </td><td> $76.51 \pm 5.74$ </td></tr></table>

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

TV

$$
7 8. 2 2 \pm 5. 1 9
$$

$$
7 7. 0 1 \pm 6. 0 0
$$

$$
6 6. 2 4 \pm 7. 1 8
$$

$$
7 8. 1 4 \pm 5. 3 3
$$

$$
7 5. 3 6 \pm 5. 7 9
$$

$$
5 9. 1 4 \pm 6. 3 3
$$

$$
7 3. 4 0 \pm 6. 6 0
$$

$$
7 3. 0 4 \pm 6. 5 9
$$

$$
5 9. 5 2 \pm 6. 0 9
$$

$$
7 7. 0 1 \pm 6. 0 0
$$

$$
7 1. 9 9 \pm 6. 3 3
$$

$$
7 2. 2 6 \pm 6. 7 6
$$

$$
7 5. 4 1 \pm 6. 4 7
$$

$$
8 1. 6 4 \pm 4. 2 2
$$

$$
5 9. 1 4 \pm 6. 3 3
$$

$$
8 0. 3 0 \pm 3. 8 0
$$

$$
7 3. 0 4 \pm 6. 5 9
$$

$$
7 6. 5 5 \pm 6. 1 8
$$

$$
8 1. 7 7 \pm 4. 0 7
$$

$$
7 8. 7 1 \pm 6. 3 4
$$

$$
7 1. 5 0 \pm 6. 4 4
$$

$$
7 7. 6 9 \pm 5. 5 2
$$

$$
5 9. 9 8 \pm 6. 7 5
$$

$$
8 0. 1 9 \pm 3. 9 5
$$

$$
6 5. 6 6 \pm 4. 3 6
$$

$$
7 5. 5 4 \pm 6. 3 3
$$

$$
8 1. 6 9 \pm 4. 0 4
$$

$$
7 8. 3 8 \pm 5. 8 0
$$

$$
8 0. 3 0 \pm 3. 6 7
$$

$$
8 2. 2 9 \pm 3. 9 5
$$

$$
8 0. 3 5 \pm 4. 2 1
$$

$$
7 5. 9 2 \pm 6. 1 8
$$

$$
6 4. 2 9 \pm 4. 2 7
$$

$$
8 2. 2 6 \pm 4. 8 0
$$

$$
7 7. 5 3 \pm 4. 8 2
$$

$$
8 2. 5 4 \pm 3. 6 6
$$

$$
6 5. 6 6 \pm 4. 4 3
$$

$$
7 9. 1 8 \pm 3. 9 5
$$

$$
7 4. 8 6 \pm 3. 9 8
$$

$$
8 1. 7 7 \pm 3. 6 9
$$

$$
7 8. 8 4 \pm 3. 0 6
$$

$$
7 3. 7 3 \pm 4. 3 9
$$

$$
7 2. 1 1 \pm 3. 4 4
$$

$$
7 9. 1 3 \pm 3. 1 2
$$

$$
7 5. 4 2 \pm 3. 5 0
$$

$$
5 8. 7 7 \pm 4. 6 1
$$

$$
7 6. 1 0 \pm 3. 3 6
$$

$$
5 8. 7 3 \pm 4. 3 9
$$

$$
8 2. 1 7 \pm 3. 2 1
$$

$$
7 3. 1 5 \pm 3. 5 0
$$

$$
6 8. 2 4 \pm 5. 0 1
$$

$$
8 0. 4 9 \pm 3. 2 6
$$

$$
6 7. 7 1 \pm 4. 5 1
$$

$$
5 8. 9 3 \pm 4. 1 6
$$

$$
8 2. 5 9 \pm 3. 0 3
$$

$$
6 2. 4 4 \pm 5. 3 5
$$

$$
\mathrm{Bagging}
$$

$$
6 8. 2 3 \pm 4. 5 2
$$

$$
5 9. 0 6 \pm 4. 9 7
$$

$$
8 0. 6 9 \pm 3. 8 4
$$

$$
6 6. 0 0 \pm 4. 6 9
$$

$$
7 8. 9 5 \pm 2. 9 1
$$

$$
7 6. 4 0 \pm 3. 3 6
$$

$$
\mathrm{Boosting}
$$

$$
7 2. 8 8 \pm 3. 6 8
$$

$$
7 1. 0 2 \pm 3. 0 1
$$

$$
4 9. 1 3 \pm 5. 3 4
$$

$$
6 7. 2 4 \pm 5. 3 3
$$

$$
6 3. 5 5 \pm 4. 2 8
$$

$$
6 7. 3 1 \pm 4. 7 5
$$

$$
6 1. 9 4 \pm 5. 6 4
$$

$$
\mathbf {8 3 . 3 8} \pm 3. 0 9
$$

$$
6 7. 5 6 \pm 4. 7 6
$$

$$
4 9. 2 3 \pm 4. 6 6
$$

$$
6 7. 6 4 \pm 4. 8 2
$$

$$
6 1. 6 2 \pm 4. 3 3
$$

$$
6 1. 0 8 \pm 5. 0 6
$$

$$
6 3. 5 3 \pm 6. 3 0
$$

$$
4 9. 1 3 \pm 5. 3 4
$$

$$
6 7. 1 3 \pm 5. 0 0
$$

$$
5 5. 0 4 \pm 4. 6 2
$$

$$
\mathbf {6 9 . 8 3 \pm 4 . 5 1}
$$

$$
\mathbf {8 0 . 2 9} \pm 9. 0 2
$$

$$
7 0. 4 6 \pm 9. 1 8
$$

$$
6 9. 3 2 \pm 9. 0 1
$$

$$
7 8. 4 2 \pm 9. 8 1
$$

$$
6 6. 1 2 \pm 9. 5 9
$$

$$
5 0. 5 1 \pm 2. 4 6
$$

$$
7 1. 3 0 \pm 1 1. 3 5
$$

$$
7 6. 2 0 \pm 1 1. 2 2
$$

$$
5 0. 2 2 \pm 2. 3 1
$$

$$
7 8. 2 1 \pm 1 1. 0 0
$$

$$
7 8. 6 8 \pm 7. 5 3
$$

$$
7 4. 4 3 \pm 1 1. 7 7
$$

$$
7 0. 4 6 \pm 9. 1 8
$$

$$
7 7. 2 3 \pm 8. 4 9
$$

$$
7 2. 5 3 \pm 1 0. 8 4
$$

$$
5 0. 5 1 \pm 2. 4 6
$$

$$
6 4. 9 1 \pm 1 0. 0 7
$$

$$
7 9. 6 4 \pm 6. 7 3
$$

$$
7 6. 2 0 \pm 1 1. 2 2
$$

$$
5 1. 0 0 \pm 9. 8 5
$$

$$
7 4. 2 7 \pm 8. 1 2
$$

$$
\text { Boosting }
$$

$$
7 7. 0 9 \pm 7. 8 6
$$

$$
7 8. 1 3 \pm 9. 0 5
$$

$$
7 3. 8 2 \pm 9. 2 8
$$

$$
6 7. 7 7 \pm 8. 7 2
$$

$$
7 1. 7 0 \pm 1 0. 1 6
$$

$$
7 5. 2 7 \pm 1 0. 1 4
$$

$$
5 0. 6 2 \pm 2. 7 9
$$

$$
7 4. 7 1 \pm 1 1. 0 8
$$

$$
7 7. 2 3 \pm 8. 4 9
$$

$$
5 1. 9 1 \pm 9. 9 5
$$

$$
7 8. 1 8 \pm 8. 0 2
$$

$$
7 7. 4 5 \pm 8. 1 7
$$

$$
6 3. 4 5 \pm 9. 8 6
$$

$$
8 0. 2 3 \pm 7. 5 7
$$

$$
6 7. 3 2 \pm 9. 9 4
$$

$$
5 1. 0 0 \pm 9. 8 5
$$

$$
6 3. 5 0 \pm 1 1. 4 4
$$

$$
6 2. 7 7 \pm 1 2. 1 2
$$

$$
7 8. 2 7 \pm 7. 8 0
$$

$$
8 1. 0 9 \pm 2. 6 2
$$

$$
6 1. 5 4 \pm 3. 7 6
$$

$$
8 0. 8 0 \pm 2. 6 5
$$

$$
6 5. 8 0 \pm 3. 3 5
$$

$$
7 5. 1 3 \pm 3. 2 1
$$

$$
7 5. 7 8 \pm 2. 6 1
$$

$$
5 0. 6 6 \pm 1. 4 8
$$

$$
7 8. 7 7 \pm 2. 6 9
$$

$$
5 1. 4 1 \pm 2. 1 0
$$

$$
6 8. 8 3 \pm 6. 6 6
$$

$$
8 1. 5 4 \pm 2. 5 9
$$

$$
8 1. 3 5 \pm 2. 6 0
$$

$$
6 1. 5 4 \pm 3. 7 6
$$

$$
6 7. 7 7 \pm 6. 7 5
$$

$$
7 3. 9 0 \pm 3. 0 2
$$

$$
5 7. 8 3 \pm 6. 6 2
$$

$$
6 9. 1 5 \pm 6. 7 2
$$

$$
5 0. 6 5 \pm 5. 4 7
$$

$$
6 9. 3 1 \pm 5. 5 8
$$

$$
5 0. 6 6 \pm 1. 4 8
$$

$$
7 1. 7 4 \pm 5. 6 5
$$

$$
7 8. 7 7 \pm 2. 6 9
$$

$$
8 0. 9 7 \pm 2. 7 3
$$

$$
6 3. 9 2 \pm 5. 2 9
$$

$$
8 0. 0 8 \pm 2. 6 1
$$

$$
5 1. 3 8 \pm 5. 6 4
$$

$$
7 4. 9 8 \pm 2. 7 5
$$

$$
6 9. 6 9 \pm 5. 4 9
$$

$$
6 9. 3 2 \pm 6. 0 0
$$

$$
\mathbf {8 1 . 6 0} \pm 2. 2 2
$$

$$
5 1. 9 9 \pm 2. 0 1
$$

$$
6 7. 7 7 \pm 6. 7 5
$$

$$
6 8. 7 7 \pm 6. 9 9
$$

$$
6 0. 6 2 \pm 6. 6 6
$$

$$
6 4. 8 4 \pm 5. 9 6
$$

$$
5 0. 6 5 \pm 5. 4 7
$$

$$
6 2. 9 6 \pm 5. 9 7
$$

$$
6 6. 6 6 \pm 5. 6 7
$$

$$
5 3. 5 0 \pm 6. 0 7
$$

$$
7 2. 1 3 \pm 5. 5 2
$$

<table><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>63.94 ± 4.65</td><td>64.22 ± 3.89</td><td>58.30 ± 4.95</td><td>56.87 ± 4.15</td><td>68.03 ± 4.33</td><td>BL</td><td>70.77 ± 6.94</td><td>72.09 ± 6.10</td><td>61.91 ± 6.69</td><td>54.87 ± 4.61</td><td>73.47 ± 6.55</td></tr><tr><td>Bagging</td><td>64.52 ± 4.55</td><td>62.84 ± 3.39</td><td>61.75 ± 4.49</td><td>56.45 ± 4.35</td><td>67.13 ± 3.80</td><td>Bagging</td><td>70.70 ± 6.16</td><td>67.02 ± 6.32</td><td>65.30 ± 7.51</td><td>53.64 ± 4.00</td><td>72.68 ± 6.12</td></tr><tr><td>Boosting</td><td>65.93 ± 5.20</td><td>63.96 ± 3.66</td><td>59.95 ± 5.15</td><td>56.87 ± 4.15</td><td>65.50 ± 4.30</td><td>Boosting</td><td>71.02 ± 6.20</td><td>72.09 ± 6.10</td><td>63.96 ± 7.27</td><td>54.87 ± 4.61</td><td>73.47 ± 6.55</td></tr><tr><td>RS</td><td>64.02 ± 4.90</td><td>66.87 ± 4.09</td><td>59.75 ± 5.61</td><td>62.53 ± 4.61</td><td>66.87 ± 3.90</td><td>RS</td><td>70.23 ± 6.34</td><td>72.60 ± 6.64</td><td>61.51 ± 6.63</td><td>61.85 ± 5.35</td><td>71.72 ± 6.16</td></tr></table>

suf<sup>fi</sup>cient information for choosing a single best learner. For example, there may be many base learners performing equally well on the training set. Thus, combining these learners may be a better choice. Secondly, the search processes of the learning algorithms might be imperfect. For example, even if there is a unique best hypothesis, it might be dif<sup>fi</sup>cult to attain this goal, since running the algorithms results in sub-optimal hypotheses. Thus, ensembles can compensate for such imperfect search processes. Thirdly, the hypothesis space being searched might not contain the true target function, while ensembles can give some good approximation. For example, the classi<sup>fi</sup>cation boundaries of DTs are linear segments parallel to coordinate axes. If the target classi<sup>fi</sup>cation boundary is a smooth diagonal line, using a single DT cannot lead to a good result. But a good approximation can be achieved by combining a set of DTs. Although these intuitive explanations are reasonable, they lack rigorous theoretical analyses.

In practice, to achieve a good ensemble, two necessary conditions should be satis<sup>fi</sup>ed: accuracy and diversity [46]. The base learner should be more accurate than random guessing, and each base learner should have its own knowledge about the problem, with a different pattern of errors than other base learners. In general, ensemble learning methods can be divided into two categories: instance partitioning methods and feature partitioning methods [30,51]. Bagging and Boosting are instance partitioning methods; Random Subspace is a feature partitioning method.

simplest to implement, with a surprisingly good performance. Diversity in Bagging is obtained by using bootstrapped replicas of the training data: different training data subsets are randomly drawn—with replacement—from the entire training dataset [40,51]. Each training data subset is used to train a different base learner of the same type.

The base learners' combination strategy for Bagging is majority vote. This simple strategy can reduce variance when combined with the base learner generation strategies. The Bagging algorithm process and pseudo-code are shown in Figs. 1 and 2.

Bagging (short for bootstrap aggregating) is one of the earliest ensemble learning algorithms [5]. It is also one of the most intuitive and

Bagging is particularly appealing when the available data are of limited size. To ensure that there are suf<sup>fi</sup>cient training samples in each subset, relatively large portions of the samples (75% to 100%) are drawn into each subset. This causes individual training subsets to overlap signi<sup>fi</sup>- cantly, with many of the same instances appearing in most subsets and some instances appearing multiple times in a given subset. To ensure diversity under this scenario, a relatively unstable base learner is used so that suf<sup>fi</sup>ciently different decision boundaries can be obtained for small perturbations in different training datasets.

## 3.1. Bagging

## 3.2. Boosting

Boosting [33] encompasses a family of methods. Unlike Bagging, Boosting creates different base learners by sequentially reweighting the instances in the training dataset. Each instance misclassi<sup>fi</sup>ed by the previous base learner will get a larger weight in the next round of training.

The basic idea of Boosting is to repeatedly apply a base learner to modi<sup>fi</sup>ed versions of the training dataset, thereby producing a sequence of base learners for a prede<sup>fi</sup>ned number of iterations. To begin with, all the instances are initialized with uniform weights. After this initialization, each boosting iteration <sup>fi</sup>ts a base learner to the weighted training data. Error is computed and the weight of the correctly classi<sup>fi</sup>ed instances is lowered while the incorrectly classi<sup>fi</sup>ed instances will get higher weights. The <sup>fi</sup>nal model obtained by the Boosting algorithm is a linear combination of several base learners weighted by their own performance.

Experiment results (Bigram-TP).

<table><tr><td colspan="6">Camera</td><td colspan="6">Camp</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>77.07 ± 5.82</td><td>80.75±6.73</td><td>60.12 ± 7.51</td><td>45.95 ± 7.46</td><td>74.03 ± 5.81</td><td>BL</td><td>77.24 ± 5.24</td><td>74.41 ± 6.81</td><td>69.67 ± 4.26</td><td>51.59 ± 4.63</td><td>77.76 ± 3.89</td></tr><tr><td>Bagging</td><td>76.83 ± 6.73</td><td>77.50 ± 5.92</td><td>67.40 ± 6.93</td><td>47.97 ± 7.15</td><td>75.03 ± 6.34</td><td>Bagging</td><td>77.41 ± 5.52</td><td>78.06 ± 4.31</td><td>72.11 ± 4.63</td><td>51.87 ± 4.81</td><td>78.80 ± 3.92</td></tr><tr><td>Boosting</td><td>74.84 ± 6.34</td><td>77.42 ± 7.13</td><td>64.48 ± 7.55</td><td>45.09 ± 7.12</td><td>72.46 ± 6.43</td><td>Boosting</td><td>77.81 ± 4.50</td><td>74.33 ± 5.67</td><td>70.72 ± 4.15</td><td>51.59 ± 4.63</td><td>73.98 ± 4.14</td></tr><tr><td>RS</td><td>76.47 ± 7.12</td><td>80.43 ± 6.30</td><td>64.81 ± 7.25</td><td>55.09 ± 8.02</td><td>76.28 ± 7.25</td><td>RS</td><td>77.01 ± 5.42</td><td>74.55 ± 4.82</td><td>73.13 ± 4.49</td><td>67.62 ± 4.80</td><td>81.42 ± 4.63</td></tr><tr><td colspan="6">Doctor</td><td colspan="6">Drug</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>72.27 ± 4.06</td><td>66.26 ± 4.58</td><td>66.66 ± 3.45</td><td>62.73 ± 3.98</td><td>77.61 ± 3.11</td><td>BL</td><td>68.28 ± 4.24</td><td>66.93 ± 4.71</td><td>56.61 ± 4.60</td><td>51.04 ± 4.76</td><td>65.56 ± 4.81</td></tr><tr><td>Bagging</td><td>72.80 ± 3.82</td><td>70.95 ± 3.54</td><td>70.78 ± 3.31</td><td>62.52 ± 3.46</td><td>79.35 ± 2.83</td><td>Bagging</td><td>68.78 ± 5.36</td><td>68.42 ± 5.72</td><td>61.87 ± 5.02</td><td>50.94 ± 4.93</td><td>66.63 ± 5.10</td></tr><tr><td>Boosting</td><td>77.12 ± 3.66</td><td>66.65 ± 4.01</td><td>69.16 ± 3.38</td><td>62.28 ± 3.90</td><td>78.21 ± 3.31</td><td>Boosting</td><td>66.46 ± 5.14</td><td>66.46 ± 4.82</td><td>59.06 ± 5.27</td><td>51.04 ± 4.76</td><td>66.03 ± 4.69</td></tr><tr><td>RS</td><td>72.40 ± 4.17</td><td>67.72 ± 4.12</td><td>72.18 ± 3.32</td><td>70.47 ± 3.74</td><td>81.41 ± 2.97</td><td>RS</td><td>67.80 ± 4.51</td><td>62.50 ± 5.38</td><td>61.57 ± 4.25</td><td>56.16 ± 5.31</td><td>68.88 ± 4.96</td></tr><tr><td colspan="6">Laptop</td><td colspan="6">Lawyer</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>77.26 ± 9.63</td><td>92.09 ± 5.65</td><td>58.85 ± 11.42</td><td>49.93 ± 4.73</td><td>73.44 ± 10.52</td><td>BL</td><td>76.50 ± 7.56</td><td>82.59 ± 8.10</td><td>59.68 ± 8.87</td><td>51.91 ± 3.94</td><td>78.45 ± 8.09</td></tr><tr><td>Bagging</td><td>78.14 ± 10.14</td><td>84.02 ± 6.75</td><td>63.17 ± 11.40</td><td>50.14 ± 3.65</td><td>71.56 ± 9.92</td><td>Bagging</td><td>77.59 ± 7.62</td><td>77.91 ± 7.62</td><td>64.05 ± 8.55</td><td>51.27 ± 4.39</td><td>78.27 ± 8.54</td></tr><tr><td>Boosting</td><td>75.57 ± 9.88</td><td>92.09 ± 5.65</td><td>61.55 ± 11.40</td><td>49.93 ± 4.73</td><td>73.44 ± 10.52</td><td>Boosting</td><td>76.82 ± 9.66</td><td>82.59 ± 8.10</td><td>61.45 ± 7.95</td><td>51.91 ± 3.94</td><td>78.45 ± 8.09</td></tr><tr><td>RS</td><td>75.62 ± 9.98</td><td>92.20 ± 5.83</td><td>62.32 ± 9.98</td><td>50.71 ± 5.81</td><td>75.85 ± 10.36</td><td>RS</td><td>75.68 ± 8.26</td><td>79.68 ± 8.11</td><td>63.05 ± 7.82</td><td>52.00 ± 4.10</td><td>77.27 ± 9.36</td></tr><tr><td colspan="6">Movie</td><td colspan="6">Music</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>76.55 ± 2.81</td><td>57.98 ± 3.45</td><td>60.73 ± 2.87</td><td>51.57 ± 2.47</td><td>71.76 ± 2.91</td><td>BL</td><td>64.29 ± 6.32</td><td>61.11 ± 8.01</td><td>53.92 ± 6.22</td><td>50.35 ± 5.96</td><td>69.28 ± 5.61</td></tr><tr><td>Bagging</td><td>75.96 ± 2.68</td><td>61.17 ± 3.07</td><td>68.09 ± 2.91</td><td>51.94 ± 2.89</td><td>74.76 ± 2.84</td><td>Bagging</td><td>65.29 ± 6.90</td><td>67.58 ± 6.70</td><td>58.56 ± 6.44</td><td>50.66 ± 5.39</td><td>68.96 ± 5.50</td></tr><tr><td>Boosting</td><td>75.93 ± 2.96</td><td>57.98 ± 3.45</td><td>66.49 ± 3.31</td><td>51.57 ± 2.47</td><td>71.76 ± 2.91</td><td>Boosting</td><td>67.25 ± 6.10</td><td>61.11 ± 8.01</td><td>57.46 ± 5.84</td><td>50.35 ± 5.96</td><td>62.68 ± 7.68</td></tr><tr><td>RS</td><td>75.85 ± 2.99</td><td>74.33 ± 2.90</td><td>67.36 ± 2.95</td><td>54.15 ± 3.49</td><td>75.40 ± 2.34</td><td>RS</td><td>65.05 ± 6.56</td><td>66.91 ± 6.05</td><td>57.15 ± 6.71</td><td>55.61 ± 7.34</td><td>72.02 ± 4.26</td></tr><tr><td colspan="6">Radio</td><td colspan="6">TV</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>70.41 ± 3.88</td><td>82.71 ± 3.36</td><td>56.25 ± 4.16</td><td>58.20 ± 4.34</td><td>70.94 ± 4.62</td><td>BL</td><td>66.98 ± 6.35</td><td>71.28 ± 6.19</td><td>56.17 ± 6.14</td><td>50.77 ± 2.14</td><td>70.55 ± 6.85</td></tr><tr><td>Bagging</td><td>69.80 ± 4.29</td><td>76.52 ± 3.58</td><td>59.88 ± 4.53</td><td>58.29 ± 4.48</td><td>71.09 ± 4.28</td><td>Bagging</td><td>66.43 ± 6.11</td><td>65.13 ± 5.31</td><td>55.79 ± 5.92</td><td>50.55 ± 2.16</td><td>69.96 ± 6.47</td></tr><tr><td>Boosting</td><td>70.97 ± 4.07</td><td>79.54 ± 3.80</td><td>56.93 ± 3.97</td><td>57.42 ± 4.50</td><td>68.50 ± 4.52</td><td>Boosting</td><td>66.98 ± 6.20</td><td>71.28 ± 6.19</td><td>56.89 ± 5.92</td><td>50.77 ± 2.14</td><td>70.55 ± 6.85</td></tr><tr><td>RS</td><td>70.19 ± 4.26</td><td>75.31 ± 4.53</td><td>59.37 ± 4.65</td><td>62.10 ± 3.88</td><td>73.78 ± 4.20</td><td>RS</td><td>67.19 ± 6.54</td><td>64.38 ± 5.47</td><td>56.00 ± 6.23</td><td>51.57 ± 4.25</td><td>70.00 ± 7.76</td></tr></table>

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

## 4. Experimental design

Even though there are several versions of Boosting algorithms, the most widely used is the one proposed by Freund and Schapire [30,33], which is known as AdaBoost. Therefore, we use the AdaBoost algorithm in this study. The algorithm's process and pseudo-code are shown in Figs. 3 and 4.

## 3.3. Random Subspace

## 4.1. Experimental datasets

The Random Subspace method is an ensemble construction technique proposed by Ho [19]. In Random Subspace, the training dataset is modi<sup>fi</sup>ed as in Bagging. However, this modi<sup>fi</sup>cation is performed in the feature space rather than in the instance space. The process and pseudo-code for the Random Subspace algorithm are shown in Figs. 5 and 6.

To verify the effectiveness of ensemble learning for sentiment analysis, we investigated ten public sentiment analysis datasets from a wide variety of domains. The Movie dataset was collected from the commonly-used Cornell movie-review dataset [27]. It consisted of four collections of movie-review documents labeled with sentiment polarities (positive or negative) or ratings on a scale from 1 to 5, and movie-review sentences labeled with subjectivity statuses (subjective or objective) or polarities. In our experiments, the documents labeled with polarities were chosen as the dataset, which contained 1000 positive and 1000 negative reviews. The other nine sentiment analysis datasets were provided by Whitehead and Yaeger [42]. These datasets included reviews and corresponding ratings, in which the rating of “1” was a positive sentiment and the rating o $\Gamma ^ { \bullet } - 1 ^ { \prime }$ was a negative senti ment. Except for the Camera dataset that contained 250 positive instances and 248 negative instances, the other eight datasets had the same number of positive and negative instances. The summary descriptions of the datasets are shown in Table 2.

The Random Subspace method may bene<sup>fi</sup>t from using random subspaces for both constructing and aggregating the base classi<sup>fi</sup>ers. When the dataset has many redundant or irrelevant features, one may obtain better base classi<sup>fi</sup>ers in random subspaces than in the original feature space [19]. The combined decision of such base classi<sup>fi</sup>ers may be superior to a single classi<sup>fi</sup>er constructed on the original training dataset in the complete feature sets.

The established standard measure in sentiment analysis, average accuracy, was adopted to evaluate the performance of the proposed method. The de<sup>fi</sup>nition of average accuracy can be explained with a confusion matrix as shown in Table 3.

## 4.2. Performance evaluation

Experiment results (Bigram-TF).

<table><tr><td colspan="6">Camera</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $78.15 \pm 5.50$ </td><td> $\mathbf{80.83} \pm 5.50$ </td><td> $62.22 \pm 6.29$ </td><td> $46.67 \pm 5.64$ </td><td> $74.52 \pm 5.77$ </td></tr><tr><td>Bagging</td><td> $78.03 \pm 5.35$ </td><td> $77.77 \pm 5.63$ </td><td> $66.99 \pm 7.39$ </td><td> $47.91 \pm 6.26$ </td><td> $75.44 \pm 5.48$ </td></tr><tr><td>Boosting</td><td> $74.72 \pm 6.08$ </td><td> $75.90 \pm 5.91$ </td><td> $65.33 \pm 6.84$ </td><td> $45.72 \pm 5.80$ </td><td> $72.56 \pm 6.32$ </td></tr><tr><td>RS</td><td> $76.99 \pm 4.71$ </td><td> $79.56 \pm 4.13$ </td><td> $66.13 \pm 6.09$ </td><td> $55.48 \pm 5.80$ </td><td> $76.13 \pm 5.52$ </td></tr><tr><td colspan="6">Doctor</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $72.41 \pm 4.42$ </td><td> $66.10 \pm 3.86$ </td><td> $67.09 \pm 3.95$ </td><td> $62.31 \pm 3.84$ </td><td> $77.27 \pm 3.56$ </td></tr><tr><td>Bagging</td><td> $72.59 \pm 4.55$ </td><td> $70.49 \pm 3.74$ </td><td> $71.48 \pm 3.91$ </td><td> $61.94 \pm 3.78$ </td><td> $78.31 \pm 3.28$ </td></tr><tr><td>Boosting</td><td> $77.58 \pm 4.36$ </td><td> $66.36 \pm 4.22$ </td><td> $68.64 \pm 3.92$ </td><td> $62.04 \pm 3.35$ </td><td> $77.83 \pm 3.45$ </td></tr><tr><td>RS</td><td> $72.40 \pm 4.39$ </td><td> $66.33 \pm 2.98$ </td><td> $72.20 \pm 3.96$ </td><td> $70.11 \pm 4.24$ </td><td> $\mathbf{80.75} \pm 3.19$ </td></tr><tr><td colspan="6">Laptop</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $77.04 \pm 8.62$ </td><td> $92.45 \pm 5.97$ </td><td> $57.78 \pm 11.36$ </td><td> $49.54 \pm 3.42$ </td><td> $74.29 \pm 11.44$ </td></tr><tr><td>Bagging</td><td> $77.70 \pm 7.68$ </td><td> $86.71 \pm 6.84$ </td><td> $61.65 \pm 8.81$ </td><td> $50.05 \pm 2.97$ </td><td> $74.47 \pm 10.58$ </td></tr><tr><td>Boosting</td><td> $74.08 \pm 10.27$ </td><td> $92.45 \pm 5.97$ </td><td> $63.84 \pm 8.96$ </td><td> $49.54 \pm 3.42$ </td><td> $74.29 \pm 11.44$ </td></tr><tr><td>RS</td><td> $76.41 \pm 9.84$ </td><td> $\mathbf{92.62} \pm 5.75$ </td><td> $61.24 \pm 8.93$ </td><td> $50.34 \pm 3.61$ </td><td> $76.02 \pm 12.25$ </td></tr><tr><td colspan="6">Movie</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $\mathbf{76.70} \pm 2.24$ </td><td> $58.73 \pm 3.60$ </td><td> $60.82 \pm 3.18$ </td><td> $51.50 \pm 2.09$ </td><td> $72.62 \pm 3.23$ </td></tr><tr><td>Bagging</td><td> $76.43 \pm 2.43$ </td><td> $60.63 \pm 2.79$ </td><td> $67.92 \pm 3.71$ </td><td> $51.87 \pm 2.39$ </td><td> $74.81 \pm 2.93$ </td></tr><tr><td>Boosting</td><td> $75.75 \pm 3.04$ </td><td> $58.73 \pm 3.60$ </td><td> $66.56 \pm 3.08$ </td><td> $51.50 \pm 2.09$ </td><td> $72.62 \pm 3.23$ </td></tr><tr><td>RS</td><td> $76.08 \pm 2.39$ </td><td> $74.57 \pm 2.87$ </td><td> $67.91 \pm 3.25$ </td><td> $54.59 \pm 2.93$ </td><td> $75.61 \pm 3.26$ </td></tr><tr><td colspan="6">Radio</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td> $70.42 \pm 4.18$ </td><td> $\mathbf{82.45} \pm 3.71$ </td><td> $56.29 \pm 4.33$ </td><td> $58.07 \pm 4.00$ </td><td> $71.68 \pm 4.26$ </td></tr><tr><td>Bagging</td><td> $70.04 \pm 4.59$ </td><td> $76.24 \pm 4.23$ </td><td> $58.87 \pm 3.95$ </td><td> $58.09 \pm 3.66$ </td><td> $71.01 \pm 4.16$ </td></tr><tr><td>Boosting</td><td> $70.80 \pm 4.25$ </td><td> $79.46 \pm 4.11$ </td><td> $56.59 \pm 3.90$ </td><td> $57.07 \pm 4.23$ </td><td> $69.05 \pm 4.56$ </td></tr><tr><td>RS</td><td> $70.42 \pm 4.26$ </td><td> $75.96 \pm 4.93$ </td><td> $59.86 \pm 4.25$ </td><td> $62.37 \pm 4.72$ </td><td> $74.48 \pm 4.23$ </td></tr></table>

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

<table><tr><td colspan="6">Camp</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>77.23 ± 4.72</td><td>74.05 ± 6.97</td><td>69.69 ± 4.32</td><td>51.33 ± 5.04</td><td>78.58 ± 4.01</td></tr><tr><td>Bagging</td><td>77.35 ± 4.80</td><td>77.97 ± 4.14</td><td>71.91 ± 4.20</td><td>51.74 ± 4.84</td><td>79.33 ± 3.69</td></tr><tr><td>Boosting</td><td>77.35 ± 5.03</td><td>74.43 ± 5.22</td><td>71.38 ± 5.37</td><td>51.33 ± 5.04</td><td>74.66 ± 3.39</td></tr><tr><td>RS</td><td>77.84 ± 5.63</td><td>73.39 ± 4.13</td><td>71.91 ± 5.31</td><td>67.25 ± 4.86</td><td>81.24 ± 4.55</td></tr><tr><td colspan="6">Drug</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>68.37 ± 5.48</td><td>66.77 ± 5.01</td><td>57.47 ± 5.43</td><td>51.16 ± 4.50</td><td>65.10 ± 4.80</td></tr><tr><td>Bagging</td><td>68.62 ± 4.97</td><td>67.20 ± 5.05</td><td>60.84 ± 5.04</td><td>50.81 ± 4.31</td><td>66.28 ± 5.11</td></tr><tr><td>Boosting</td><td>66.83 ± 4.69</td><td>66.10 ± 5.01</td><td>59.26 ± 5.27</td><td>51.25 ± 4.57</td><td>66.00 ± 4.91</td></tr><tr><td>RS</td><td>67.79 ± 5.45</td><td>63.29 ± 6.06</td><td>61.48 ± 5.39</td><td>56.21 ± 5.31</td><td>69.12 ± 4.43</td></tr><tr><td colspan="6">Lawyer</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>76.91 ± 7.96</td><td>81.00 ± 7.23</td><td>59.00 ± 10.11</td><td>52.00 ± 3.44</td><td>80.27 ± 7.40</td></tr><tr><td>Bagging</td><td>76.82 ± 7.71</td><td>77.36 ± 7.06</td><td>63.45 ± 10.29</td><td>52.09 ± 4.40</td><td>78.73 ± 7.56</td></tr><tr><td>Boosting</td><td>75.64 ± 7.47</td><td>81.00 ± 7.23</td><td>61.91 ± 9.96</td><td>52.00 ± 3.44</td><td>80.27 ± 7.40</td></tr><tr><td>RS</td><td>75.91 ± 7.66</td><td>80.91 ± 9.18</td><td>62.45 ± 9.62</td><td>53.91 ± 6.26</td><td>76.00 ± 7.48</td></tr><tr><td colspan="6">Music</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>64.90 ± 5.20</td><td>60.30 ± 7.86</td><td>53.47 ± 5.98</td><td>50.10 ± 6.13</td><td>69.68 ± 5.39</td></tr><tr><td>Bagging</td><td>65.70 ± 5.24</td><td>64.45 ± 6.08</td><td>58.49 ± 5.52</td><td>50.10 ± 5.90</td><td>69.16 ± 6.26</td></tr><tr><td>Boosting</td><td>66.90 ± 6.15</td><td>60.30 ± 7.86</td><td>57.28 ± 5.57</td><td>50.10 ± 6.13</td><td>62.30 ± 5.15</td></tr><tr><td>RS</td><td>65.42 ± 4.80</td><td>68.39 ± 5.37</td><td>57.34 ± 6.34</td><td>56.53 ± 5.33</td><td>72.10 ± 6.12</td></tr><tr><td colspan="6">TV</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>66.72 ± 6.72</td><td>70.34 ± 6.93</td><td>55.02 ± 5.19</td><td>51.11 ± 2.85</td><td>69.91 ± 7.17</td></tr><tr><td>Bagging</td><td>66.55 ± 6.58</td><td>64.11 ± 6.85</td><td>57.83 ± 6.84</td><td>50.60 ± 2.27</td><td>68.94 ± 7.17</td></tr><tr><td>Boosting</td><td>65.11 ± 6.67</td><td>70.34 ± 6.93</td><td>57.06 ± 6.42</td><td>51.11 ± 2.85</td><td>69.91 ± 7.17</td></tr></table>

$$
6 6. 4 3 \pm 7. 5 1
$$

$$
6 6. 1 3 \pm 6. 5 0
$$

$$
5 5. 5 7 \pm 5. 6 4
$$

$$
5 1. 0 2 \pm 3. 6 7
$$

$$
6 8. 4 7 \pm 6. 4 5
$$

Formally, average accuracy is de<sup>fi</sup>ned as follows:

$$
\text { Average   accuracy } = \frac {\mathrm{TP} + \mathrm{TN}}{\mathrm{TP} + \mathrm{FP} + \mathrm{FN} + \mathrm{TN}}\tag{1}
$$

## 4.3. Experimental procedure

To minimize the in<sup>fl</sup>uence of variability in the training set, 10-fold cross validation was performed ten times on the ten sentiment analysis datasets. In detail, each sentiment analysis dataset was partitioned into ten subsets with similar sizes and distributions. Then, the union of nine subsets was used as the training set while the remaining subset is used as the test set. The process was repeated ten times, such that every subset had been used as the test set once. The average test result was regarded as the result of the 10-fold cross validation. The process was repeated for 10 times with random partitions of the ten subsets, and the average results of these different partitions were recorded.

Ensemble methods are composed of several base learners. Based on the literature review [29,34,48], we chose <sup>fi</sup>ve widely used base learners for our experiment: NB, ME, DT, KNN, and SVM.

NB is a simple probabilistic classi<sup>fi</sup>cation method based on applying Bayes' theorem with strong independence assumptions [7]. It is very easy to construct, not requiring any complicated iterative parameter estimation. Also, it is readily applied to huge datasets. The main disadvantage is that the conditional independence assumption is violated by real-world data.

ME is one of the best methods for natural language processing [29]. Unlike NB, ME makes no assumptions about the relations between features, and therefore it may perform better when conditional independence assumptions are not met.

DT has been widely used in building classi<sup>fi</sup>cation models because it closely resembles human reasoning and is easy to understand [31]. DT is a sequential model, which logically combines a sequence of simple tests. Each test compares a numeric attribute against a threshold value or a nominal attribute against a set of possible values. In this study, we chose the widely used C4.5 for our experiments.

KNN is one of the simplest and rather trivial classi<sup>fi</sup>cation methods [8]. An object of KNN is classi<sup>fi</sup>ed by a majority vote of its neighbors. If $\mathrm { K } = 1$ , then the object is simply assigned to the class label of its nearest neighbor. One of the major drawbacks of KNN is that the classi<sup>fi</sup>er needs available data. This may lead to considerable overhead if the training dataset is large. In this study, we choose K = 1.

SVM is a state-of-the-art data mining technique that has proven its performance in many applications [39]. It has a sound theoretical foundation and requires a dozen instances for training. The strength of this technique lies with its ability to model non-linearity, resulting in complex mathematical models. SVM can capture the inherent characteristics of the data better than ANN can.

Three ensemble methods, i.e., Bagging, Boosting, and Random Subspace, were implemented respectively with the <sup>fi</sup>ve base learners. As discussed in the literature review and following [29], Unigram and Bigram weighted by term present, term frequency, and TF–IDF were selected to express the text information. A total of 1200 comparative group experiments (6 feature sets × 20 classi<sup>fi</sup>ers × 10 datasets) were

## Table 9

Experiment results (Bigram-TF–IDF).

<table><tr><td colspan="6">Camera</td><td colspan="6">Camp</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>77.44 ± 6.20</td><td>80.86±5.40</td><td>61.33 ± 5.42</td><td>46.48 ± 6.49</td><td>74.51 ± 5.75</td><td>BL</td><td>77.26 ± 4.62</td><td>73.86 ± 5.03</td><td>68.71 ± 4.22</td><td>51.10 ± 5.51</td><td>78.65 ± 4.40</td></tr><tr><td>Bagging</td><td>76.99 ± 6.36</td><td>76.82 ± 4.88</td><td>66.99 ± 6.93</td><td>47.97 ± 6.32</td><td>75.92 ± 5.86</td><td>Bagging</td><td>77.45 ± 4.60</td><td>77.65 ± 4.68</td><td>72.04 ± 4.55</td><td>51.46 ± 5.34</td><td>79.12 ± 4.28</td></tr><tr><td>Boosting</td><td>73.67 ± 6.78</td><td>77.24 ± 5.86</td><td>65.02 ± 7.64</td><td>45.95 ± 6.25</td><td>73.42 ± 5.20</td><td>Boosting</td><td>77.56 ± 4.76</td><td>73.94 ± 4.66</td><td>70.87 ± 4.66</td><td>51.10 ± 5.51</td><td>74.33 ± 4.83</td></tr><tr><td>RS</td><td>76.35 ± 6.13</td><td>80.85 ± 4.39</td><td>66.64 ± 6.16</td><td>55.50 ± 7.38</td><td>77.12 ± 5.16</td><td>RS</td><td>76.59 ± 4.04</td><td>74.66 ± 4.32</td><td>72.21 ± 3.66</td><td>67.24 ± 4.36</td><td>81.59 ± 4.13</td></tr><tr><td colspan="6">Doctor</td><td colspan="6">Drug</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>72.27 ± 3.54</td><td>65.93 ± 6.19</td><td>67.52 ± 3.38</td><td>62.69 ± 4.09</td><td>77.22 ± 3.07</td><td>BL</td><td>67.92 ± 4.77</td><td>67.66 ± 5.69</td><td>56.67 ± 5.96</td><td>50.73 ± 5.28</td><td>65.09 ± 4.69</td></tr><tr><td>Bagging</td><td>72.79 ± 3.80</td><td>70.97 ± 3.96</td><td>70.99 ± 3.51</td><td>62.27 ± 3.87</td><td>78.89 ± 3.40</td><td>Bagging</td><td>68.17 ± 4.71</td><td>67.87 ± 5.20</td><td>60.56 ± 4.51</td><td>50.99 ± 5.44</td><td>66.47 ± 4.78</td></tr><tr><td>Boosting</td><td>76.80 ± 3.52</td><td>65.32 ± 5.45</td><td>69.21 ± 3.62</td><td>62.36 ± 4.02</td><td>78.10 ± 2.97</td><td>Boosting</td><td>66.53 ± 4.51</td><td>66.86 ± 6.02</td><td>58.63 ± 5.43</td><td>51.05 ± 5.22</td><td>65.79 ± 4.73</td></tr><tr><td>RS</td><td>72.30 ± 3.47</td><td>66.35 ± 3.45</td><td>71.72 ± 3.00</td><td>70.31 ± 3.69</td><td>81.17 ± 3.31</td><td>RS</td><td>67.45 ± 4.73</td><td>63.63 ± 5.48</td><td>60.84 ± 4.60</td><td>56.51 ± 4.35</td><td>68.88 ± 4.17</td></tr><tr><td colspan="6">Laptop</td><td colspan="6">Lawyer</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>76.46 ± 10.12</td><td>92.05 ± 6.05</td><td>58.95 ± 11.31</td><td>49.32 ± 4.54</td><td>72.42 ± 9.29</td><td>BL</td><td>76.18 ± 8.40</td><td>81.64 ± 8.62</td><td>60.18 ± 8.50</td><td>51.55 ± 2.98</td><td>79.00 ± 7.42</td></tr><tr><td>Bagging</td><td>75.90 ± 9.99</td><td>85.80 ± 6.90</td><td>60.31 ± 10.17</td><td>50.44 ± 3.47</td><td>72.44 ± 10.03</td><td>Bagging</td><td>77.36 ± 8.30</td><td>76.36 ± 8.03</td><td>62.64 ± 7.77</td><td>51.82 ± 3.17</td><td>77.45 ± 7.13</td></tr><tr><td>Boosting</td><td>75.33 ± 9.39</td><td>92.05 ± 6.05</td><td>61.24 ± 10.59</td><td>49.32 ± 4.54</td><td>72.42 ± 9.29</td><td>Boosting</td><td>75.55 ± 8.85</td><td>81.64 ± 8.62</td><td>62.82 ± 9.78</td><td>51.55 ± 2.98</td><td>79.00 ± 7.42</td></tr><tr><td>RS</td><td>76.33 ± 11.21</td><td>90.92 ± 6.26</td><td>60.27 ± 11.05</td><td>50.55 ± 4.13</td><td>75.59 ± 9.81</td><td>RS</td><td>75.18 ± 8.28</td><td>79.18 ± 8.43</td><td>62.45 ± 7.96</td><td>53.18 ± 5.27</td><td>76.27 ± 7.15</td></tr><tr><td colspan="6">Movie</td><td colspan="6">Music</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>76.59 ± 2.79</td><td>58.36 ± 3.22</td><td>60.41 ± 3.79</td><td>51.70 ± 2.32</td><td>72.08 ± 2.88</td><td>BL</td><td>64.32 ± 6.73</td><td>60.22 ± 7.93</td><td>53.81 ± 6.97</td><td>50.38 ± 4.43</td><td>68.48 ± 6.42</td></tr><tr><td>Bagging</td><td>76.51 ± 2.82</td><td>55.48 ± 3.30</td><td>68.31 ± 3.01</td><td>52.26 ± 2.59</td><td>74.05 ± 3.34</td><td>Bagging</td><td>64.93 ± 6.83</td><td>63.80 ± 6.16</td><td>58.86 ± 5.44</td><td>50.24 ± 4.56</td><td>70.10 ± 6.03</td></tr><tr><td>Boosting</td><td>75.93 ± 3.01</td><td>58.36 ± 3.22</td><td>66.69 ± 2.70</td><td>51.70 ± 2.32</td><td>72.08 ± 2.88</td><td>Boosting</td><td>66.29 ± 6.16</td><td>60.22 ± 7.93</td><td>55.63 ± 6.81</td><td>50.38 ± 4.43</td><td>63.02 ± 5.69</td></tr><tr><td>RS</td><td>76.06 ± 2.83</td><td>74.77 ± 2.81</td><td>67.60 ± 2.88</td><td>54.43 ± 2.66</td><td>75.71 ± 2.74</td><td>RS</td><td>64.15 ± 7.35</td><td>67.69 ± 5.82</td><td>57.17 ± 6.15</td><td>56.49 ± 5.93</td><td>72.02 ± 6.46</td></tr><tr><td colspan="6">Radio</td><td colspan="6">TV</td></tr><tr><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td><td></td><td>NB</td><td>ME</td><td>DT</td><td>KNN</td><td>SVM</td></tr><tr><td>BL</td><td>70.35 ± 4.50</td><td>82.76 ± 3.57</td><td>55.72 ± 3.79</td><td>57.68 ± 4.62</td><td>71.02 ± 4.50</td><td>BL</td><td>67.66 ± 7.08</td><td>71.32 ± 5.77</td><td>56.26 ± 7.09</td><td>50.72 ± 2.61</td><td>70.34 ± 5.87</td></tr><tr><td>Bagging</td><td>69.87 ± 4.10</td><td>77.13 ± 3.94</td><td>59.05 ± 4.67</td><td>57.88 ± 4.60</td><td>71.05 ± 4.94</td><td>Bagging</td><td>67.40 ± 6.88</td><td>64.83 ± 5.97</td><td>58.85 ± 7.04</td><td>50.43 ± 2.54</td><td>70.55 ± 6.74</td></tr><tr><td>Boosting</td><td>71.33 ± 4.44</td><td>80.02 ± 3.87</td><td>57.51 ± 4.36</td><td>57.08 ± 4.04</td><td>68.72 ± 3.39</td><td>Boosting</td><td>67.74 ± 5.85</td><td>71.32 ± 5.77</td><td>58.60 ± 6.59</td><td>50.72 ± 2.61</td><td>70.34 ± 5.87</td></tr><tr><td>RS</td><td>69.97 ± 4.41</td><td>75.52 ± 4.94</td><td>59.14 ± 4.55</td><td>61.99 ± 4.20</td><td>74.70 ± 4.27</td><td>RS</td><td>67.40 ± 6.29</td><td>65.74 ± 6.42</td><td>57.40 ± 4.92</td><td>51.36 ± 3.78</td><td>69.91 ± 7.40</td></tr></table>

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

conducted to verify the effectiveness of ensemble learning for sentiment classi<sup>fi</sup>cation. The experimental procedure is shown in Fig. 7.

## 5. Experimental results and analysis

The experiments were performed on a PC with a 3.10 GHz AMD FX(tm)-8120 Eight-Core CPU and 8 GB RAM, using Windows 7 operating system. We used the data mining toolkit WEKA (Waikato Environment for Knowledge Analysis) version 3.7.0. This open-source toolkit includes a collection of machine learning algorithms for solving data mining problems [47].

In this study, we compared the performances of 20 methods, including NB, ME, DT, KNN and SVM, and their corresponding ensemble methods of Bagging, Boosting, and Random Subspace. Among these methods, the NB algorithm, ME algorithm, KNN algorithm, and SVM algorithm were implement by the Naive Bayes module, logistic module (WEKA's own version of multinomial logistic regression), IBk module, and SMO module of WEKA, respectively. The DT algorithm was implemented by the J48 module (WEKA's own version of C4.5). The Bagging module, AdaBoost M1 module, and Random SubSpace module of WEKA were used to implement respective algorithms. As the original datasets were text forms, WEKA's StringToWordVector <sup>fi</sup>lter was used to convert original texts into an N-gram representation. Except when stated otherwise, all the default parameters in WEKA were used.

The highest average accuracy of the Camera dataset is 80.86% using ME. The highest average accuracy of the Camp dataset is 85.48% using RS-SVM. The highest average accuracy of the Doctor dataset is 85.97% using RS-SVM. The highest average accuracy of the Drug dataset is 70.26% using RS-SVM. The highest average accuracy of the Laptop dataset is 92.62% using RS-ME. The highest average accuracy of the Lawyer dataset is 84.09% using SVM. The highest average accuracy of the Movie dataset is 82.54% using RS-SVM. The highest average accuracy of the Music dataset is 72.13% using RS-SVM. The highest average accuracy of the Radio dataset is 82.76% using ME. The highest average accuracy of the TV dataset is 77.94% using SVM.

## 5.1. Basic experimental results

Tables 4 to 9 summarize the experimental results of base learners and ensemble methods in sentiment classi<sup>fi</sup>cation, where the values following ± are standard deviations. The highest average accuracies of different datasets are boldfaced.

Among the ten datasets, SVM and ensemble methods using SVM as the base learner have eight of the highest average accuracies. These <sup>fi</sup>ndings indicate SVM has more powerful competitiveness in sentiment classi<sup>fi</sup>cation. This is consistent with previous research [2,29,43]. In addition, RS-SVM has the six highest average accuracies and similar average accuracies with other four datasets. It is interesting that the ensemble methods with the highest average accuracies are all based on Random Subspace. A potential explanation is that since the sentiment classi<sup>fi</sup>cation problem has tens of thousands of features, a feature partitioning method is better able to address this problem.

Table 10  
Outcomes of Wilcoxon matched-pairs signed-ranks test (Unigram-TP).  
Table 11

<table><tr><td rowspan="2"></td><td colspan="2">Bagging NB</td><td colspan="2">Boosting NB</td><td colspan="2">RS NB</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>NB</td><td>2/3/5</td><td>1.812</td><td>6/3/1</td><td>7.434**</td><td>0/3/7</td><td>5.338**</td></tr><tr><td>Bagging NB</td><td></td><td></td><td>6/2/2</td><td>8.031**</td><td>0/3/7</td><td>2.384*</td></tr><tr><td>Boosting NB</td><td></td><td></td><td></td><td></td><td>2/2/6</td><td>8.996**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging ME</td><td colspan="2">Boosting ME</td><td colspan="2">RS ME</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>ME</td><td>3/2/5</td><td>2.828**</td><td>0/8/2</td><td>8.514**</td><td>5/2/3</td><td>6.996**</td></tr><tr><td>Bagging ME</td><td></td><td></td><td>5/1/4</td><td>6.141**</td><td>7/0/3</td><td>7.709**</td></tr><tr><td>Boosting ME</td><td></td><td></td><td></td><td></td><td>6/2/2</td><td>9.654**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging DT</td><td colspan="2">Boosting DT</td><td colspan="2">RS DT</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>DT</td><td>10/0/0</td><td>19.700**</td><td>10/0/0</td><td>19.688**</td><td>10/0/0</td><td>19.884**</td></tr><tr><td>Bagging DT</td><td></td><td></td><td>3/0/7</td><td>3.332**</td><td>5/0/5</td><td>0.138</td></tr><tr><td>Boosting DT</td><td></td><td></td><td></td><td></td><td>7/2/1</td><td>3.080**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging KNN</td><td colspan="2">Boosting KNN</td><td colspan="2">RS KNN</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>KNN</td><td>3/0/7</td><td>2.689**</td><td>0/8/2</td><td>2.725**</td><td>9/0/1</td><td>14.280**</td></tr><tr><td>Bagging KNN</td><td></td><td></td><td>6/0/4</td><td>2.092*</td><td>9/1/0</td><td>15.433**</td></tr><tr><td>Boosting KNN</td><td></td><td></td><td></td><td></td><td>9/1/0</td><td>14.547**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging SVM</td><td colspan="2">Boosting SVM</td><td colspan="2">RS SVM</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>SVM</td><td>7/2/1</td><td>7.305**</td><td>1/6/3</td><td>0.880</td><td>7/1/2</td><td>9.942**</td></tr><tr><td>Bagging SVM</td><td></td><td></td><td>1/1/8</td><td>7.612**</td><td>7/1/2</td><td>5.749**</td></tr><tr><td>Boosting SVM</td><td></td><td></td><td></td><td></td><td>7/1/2</td><td>10.030**</td></tr></table>

Outcomes of Wilcoxon matched-pairs signed-ranks test (Unigram-TF).  
Note: Iman–Davenport test: 0.000. ⁎P-values signi<sup>fi</sup>cant at alpha = 0.05. ⁎⁎P-values signi<sup>fi</sup>cant at alpha = 0.01.

To ensure that the assessment does not happen by chance, we tested the signi<sup>fi</sup>cance of these results. Following [13,16], we <sup>fi</sup>rstly conducted an Iman–Davenport test [21], to ascertain whether there are signi<sup>fi</sup>cant differences among all methods. Then, pairwise differences were measured using a Wilcoxon test [13]. The formulation of the test

## 5.2. Analysis and discussion from the ensemble methods perspective

<table><tr><td rowspan="2"></td><td colspan="2">Bagging NB</td><td colspan="2">Boosting NB</td><td colspan="2">RS NB</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>NB</td><td>6/2/2</td><td>2.679**</td><td>7/1/2</td><td>9.306**</td><td>2/4/4</td><td>0.912</td></tr><tr><td>Bagging NB</td><td></td><td></td><td>6/2/2</td><td>7.959**</td><td>1/3/6</td><td>2.785**</td></tr><tr><td>Boosting NB</td><td></td><td></td><td></td><td></td><td>2/2/6</td><td>9.635**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging ME</td><td colspan="2">Boosting ME</td><td colspan="2">RS ME</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>ME</td><td>3/2/5</td><td>1.134</td><td>2/8/0</td><td>11.035**</td><td>4/0/6</td><td>0.027</td></tr><tr><td>Bagging ME</td><td></td><td></td><td>6/3/1</td><td>4.086**</td><td>5/0/5</td><td>0.094</td></tr><tr><td>Boosting ME</td><td></td><td></td><td></td><td></td><td>4/0/6</td><td>3.467**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging DT</td><td colspan="2">Boosting DT</td><td colspan="2">RS DT</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>DT</td><td>10/0/0</td><td>20.779**</td><td>10/0/0</td><td>20.928**</td><td>10/0/0</td><td>19.162**</td></tr><tr><td>Bagging DT</td><td></td><td></td><td>2/1/7</td><td>3.331**</td><td>2/3/5</td><td>1.890</td></tr><tr><td>Boosting DT</td><td></td><td></td><td></td><td></td><td>6/0/4</td><td>1.580</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging KNN</td><td colspan="2">Boosting KNN</td><td colspan="2">RS KNN</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>KNN</td><td>3/2/5</td><td>3.224**</td><td>0/8/2</td><td>3.520**</td><td>9/1/0</td><td>12.992**</td></tr><tr><td>Bagging KNN</td><td></td><td></td><td>4/2/4</td><td>2.314*</td><td>10/0/0</td><td>14.153**</td></tr><tr><td>Boosting KNN</td><td></td><td></td><td></td><td></td><td>10/0/0</td><td>13.514**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging SVM</td><td colspan="2">Boosting SVM</td><td colspan="2">RS SVM</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>SVM</td><td>6/0/4</td><td>5.073**</td><td>1/8/1</td><td>0.625</td><td>7/0/3</td><td>8.455**</td></tr><tr><td>Bagging SVM</td><td></td><td></td><td>3/0/7</td><td>5.386**</td><td>6/3/1</td><td>5.213**</td></tr><tr><td>Boosting SVM</td><td></td><td></td><td></td><td></td><td>7/0/3</td><td>8.478**</td></tr></table>

Note: Iman–Davenport test: 0.000. \*P-values signi<sup>fi</sup>cant at alpha = 0.05. \*\*P-values signi<sup>fi</sup>cant at alpha = 0.01.  
Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

[44] is as follows. Let d<sub>i</sub> be the difference between the error values of the methods in ith data set. These differences are ranked according to their absolute values; in case of ties, an average rank is assigned. Let $R ^ { + }$ be the sum of ranks for the data sets on which the second algorithm outperformed the <sup>fi</sup>rst, and let R<sup>−</sup> be the sum of ranks where the <sup>fi</sup>rst algorithm outperformed the second. Ranks are split evenly among the sums

$$
R ^ {+} = \sum_ {d _ {i} > 0} \operatorname{rank} (d _ {i}) + \frac {1}{2} \sum_ {d _ {i} = 0} \operatorname{rank} (d _ {i})\tag{2}
$$

and

$$
R ^ {-} = \sum_ {d _ {i} <   0} \operatorname{rank} (d _ {i}) + \frac {1}{2} \sum_ {d _ {i} = 0} \operatorname{rank} (d _ {i})\tag{3}
$$

Let T be the smaller of the two sums and N be the number of data sets. For a small N, there are tables with the exact critical values for T. For a larger $N ,$ the statistics

$$
z = \frac {T - \frac {1}{4} N (N + 1)}{\sqrt {\frac {1}{2 4} N (N + 1) (2 N + 1)}}\tag{4}
$$

is distributed approximately according to N(0,1). We combined these two tests to assess the performance difference of the different algorithms. When the comparison was between two algorithms only the Wilcoxon test was used.

Table 12  
Outcomes of Wilcoxon matched-pairs signed-ranks test (Unigram-TF–IDF).  
Table 13

<table><tr><td rowspan="2"></td><td colspan="2">Bagging NB</td><td colspan="2">Boosting NB</td><td colspan="2">RS NB</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>NB</td><td>5/3/2</td><td>0.707</td><td>4/2/4</td><td>3.434**</td><td>1/4/5</td><td>5.328**</td></tr><tr><td>Bagging NB</td><td></td><td></td><td>4/3/3</td><td>3.816**</td><td>1/1/8</td><td>4.935**</td></tr><tr><td>Boosting NB</td><td></td><td></td><td></td><td></td><td>3/1/6</td><td>0.728</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging ME</td><td colspan="2">Boosting ME</td><td colspan="2">RS ME</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>ME</td><td>4/1/5</td><td>1.647</td><td>0/7/3</td><td>9.038**</td><td>7/0/3</td><td>8.686**</td></tr><tr><td>Bagging ME</td><td></td><td></td><td>5/1/4</td><td>4.353**</td><td>7/0/3</td><td>8.571**</td></tr><tr><td>Boosting ME</td><td></td><td></td><td></td><td></td><td>8/1/1</td><td>11.238**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging DT</td><td colspan="2">Boosting DT</td><td colspan="2">RS DT</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>DT</td><td>10/0/0</td><td>18.146**</td><td>8/0/2</td><td>11.090**</td><td>9/0/1</td><td>15.448**</td></tr><tr><td>Bagging DT</td><td></td><td></td><td>1/0/9</td><td>9.835**</td><td>2/2/6</td><td>4.124**</td></tr><tr><td>Boosting DT</td><td></td><td></td><td></td><td></td><td>7/1/2</td><td>5.395**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging KNN</td><td colspan="2">Boosting KNN</td><td colspan="2">RS KNN</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>KNN</td><td>4/2/4</td><td>1.120</td><td>1/9/0</td><td>2.027*</td><td>9/1/0</td><td>19.895**</td></tr><tr><td>Bagging KNN</td><td></td><td></td><td>5/1/4</td><td>1.308</td><td>10/0/0</td><td>19.634**</td></tr><tr><td>Boosting KNN</td><td></td><td></td><td></td><td></td><td>9/1/0</td><td>19.903**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging SVM</td><td colspan="2">Boosting SVM</td><td colspan="2">RS SVM</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>SVM</td><td>6/1/3</td><td>3.007**</td><td>0/5/5</td><td>13.400**</td><td>6/0/4</td><td>6.080**</td></tr><tr><td>Bagging SVM</td><td></td><td></td><td>2/0/8</td><td>12.403**</td><td>6/1/3</td><td>3.781**</td></tr><tr><td>Boosting SVM</td><td></td><td></td><td></td><td>13.400**</td><td>8/0/2</td><td>13.386**</td></tr></table>

Note: Iman–Davenport test: 0.000. \*P-values signi<sup>fi</sup>cant at alpha = 0.05. \*\*P-values signi<sup>fi</sup>cant at alpha = 0.01.

We also employed the statistics used in [41] to compare two learning algorithms across all data sets, namely, the win/draw/loss record. The win/draw/loss record presents three values, the number of data sets for which algorithm A obtained better, equal, or worse performance than algorithm B with respect to classi<sup>fi</sup>cation accuracy. We also reported the statistically signi<sup>fi</sup>cant win/draw/loss record, where a win or loss was only counted if the difference in values was determined to be signi<sup>fi</sup>cant at the 0.05 level by a paired t-test.

Tables 10 to 15 show the comparison among the methods. Columns labeled s present the win/draw/loss record, where the <sup>fi</sup>rst value is the number of data sets for which row b col, the second is the number for which row = col, and the last is the number for which row N col. Columns labeled $P _ { w }$ present the results of Wilcoxon tests. For all methods, the Iman–Davenport test had a P-value of 0.000, showing signi<sup>fi</sup>cant differences among them.

As seen in the tables, for all groups except ME and related ensemble methods using Bigram-TF–IDF as a feature, at least one ensemble method has better comparative results than the base learner. Thus, we can conclude that ensemble methods are appropriate for sentiment classi<sup>fi</sup>cation.

Furthermore, some interesting phenomena were observed in the experiments. Among the three ensemble methods, Boosting had poor accuracy except when it used DT as the base learner. A potential explanation is because the BOW framework directly converts text information into space vectors, the space vectors contain many redundant and relevant features and some noise. Empirical and theoretical results have shown that Boosting is easily in<sup>fl</sup>uenced by noisy data [3,13,51]. The second interesting thing is that ensemble methods using DT as the base learner all have better comparative results. This result is consistent with prior research [5,13,30,51] and

Outcomes of Wilcoxon matched-pairs signed-ranks test (Bigram-TP).

<table><tr><td rowspan="2"></td><td colspan="2">Bagging NB</td><td colspan="2">Boosting NB</td><td colspan="2">RS NB</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>NB</td><td>5/1/4</td><td>1.826</td><td>4/2/4</td><td>1.806</td><td>1/3/6</td><td>3.037**</td></tr><tr><td>Bagging NB</td><td></td><td></td><td>5/1/4</td><td>0.351</td><td>2/2/6</td><td>3.246**</td></tr><tr><td>Boosting NB</td><td></td><td></td><td></td><td></td><td>2/3/5</td><td>3.125**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging ME</td><td colspan="2">Boosting ME</td><td colspan="2">RS ME</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>ME</td><td>5/0/5</td><td>4.430**</td><td>1/6/3</td><td>7.994**</td><td>3/2/5</td><td>0.643</td></tr><tr><td>Bagging ME</td><td></td><td></td><td>4/1/5</td><td>1.025</td><td>4/0/6</td><td>3.518**</td></tr><tr><td>Boosting ME</td><td></td><td></td><td></td><td></td><td>4/2/4</td><td>1.785</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging DT</td><td colspan="2">Boosting DT</td><td colspan="2">RS DT</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>DT</td><td>9/0/1</td><td>16.971**</td><td>10/0/0</td><td>11.558**</td><td>9/1/0</td><td>15.654**</td></tr><tr><td>Bagging DT</td><td></td><td></td><td>1/0/9</td><td>8.325**</td><td>2/1/7</td><td>1.833</td></tr><tr><td>Boosting DT</td><td></td><td></td><td></td><td></td><td>8/0/2</td><td>6.787**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging KNN</td><td colspan="2">Boosting KNN</td><td colspan="2">RS KNN</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>KNN</td><td>4/3/3</td><td>2.799**</td><td>0/7/3</td><td>4.348**</td><td>9/1/0</td><td>20.014**</td></tr><tr><td>Bagging KNN</td><td></td><td></td><td>2/2/6</td><td>4.571**</td><td>10/0/0</td><td>19.539**</td></tr><tr><td>Boosting KNN</td><td></td><td></td><td></td><td></td><td>9/1/0</td><td>20.234**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging SVM</td><td colspan="2">Boosting SVM</td><td colspan="2">RS SVM</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>SVM</td><td>5/2/3</td><td>5.110**</td><td>2/4/4</td><td>9.468**</td><td>8/0/2</td><td>14.399**</td></tr><tr><td>Bagging SVM</td><td></td><td></td><td>2/1/7</td><td>10.636**</td><td>8/1/1</td><td>11.257**</td></tr><tr><td>Boosting SVM</td><td></td><td></td><td></td><td></td><td>8/0/2</td><td>16.747**</td></tr></table>

Note: Iman–Davenport test: 0.000. \*P-values signi<sup>fi</sup>cant at alpha = 0.05. \*\*P-values signi<sup>fi</sup>cant at alpha = 0.01.

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

Table 14  
Table 15  
Outcomes of Wilcoxon matched-pairs signed-ranks test (Bigram-TF).

<table><tr><td rowspan="2"></td><td colspan="2">Bagging NB</td><td colspan="2">Boosting NB</td><td colspan="2">RS NB</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>NB</td><td>4/4/2</td><td>0.492</td><td>3/1/6</td><td>1.617</td><td>2/3/5</td><td>2.760**</td></tr><tr><td>Bagging NB</td><td></td><td></td><td>3/1/6</td><td>1.970*</td><td>2/1/7</td><td>2.417*</td></tr><tr><td>Boosting NB</td><td></td><td></td><td></td><td></td><td>6/1/3</td><td>0.172</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging ME</td><td colspan="2">Boosting ME</td><td colspan="2">RS ME</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>ME</td><td>5/0/5</td><td>5.528**</td><td>1/6/3</td><td>8.257**</td><td>3/2/5</td><td>1.316</td></tr><tr><td>Bagging ME</td><td></td><td></td><td>4/0/6</td><td>1.299</td><td>6/1/3</td><td>6.442**</td></tr><tr><td>Boosting ME</td><td></td><td></td><td></td><td></td><td>3/3/4</td><td>4.891**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging DT</td><td colspan="2">Boosting DT</td><td colspan="2">RS DT</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>DT</td><td>10/0/0</td><td>16.999**</td><td>10/0/0</td><td>13.505**</td><td>10/0/0</td><td>15.997**</td></tr><tr><td>Bagging DT</td><td></td><td></td><td>1/0/9</td><td>5.690**</td><td>3/3/4</td><td>0.916</td></tr><tr><td>Boosting DT</td><td></td><td></td><td></td><td></td><td>6/2/2</td><td>4.701**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging KNN</td><td colspan="2">Boosting KNN</td><td colspan="2">RS KNN</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>KNN</td><td>4/3/3</td><td>1.593</td><td>1/6/3</td><td>3.872**</td><td>9/1/0</td><td>21.072**</td></tr><tr><td>Bagging KNN</td><td></td><td></td><td>2/3/5</td><td>3.410**</td><td>10/0/0</td><td>20.579**</td></tr><tr><td>Boosting KNN</td><td></td><td></td><td></td><td></td><td>9/1/0</td><td>21.489**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging SVM</td><td colspan="2">Boosting SVM</td><td colspan="2">RS SVM</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>SVM</td><td>5/1/4</td><td>2.644**</td><td>2/4/4</td><td>10.145**</td><td>8/0/2</td><td>10.074**</td></tr><tr><td>Bagging SVM</td><td></td><td></td><td>2/1/7</td><td>9.825**</td><td>8/0/2</td><td>8.979**</td></tr><tr><td>Boosting SVM</td><td></td><td></td><td></td><td></td><td>8/0/2</td><td>14.093**</td></tr></table>

Note: Iman–Davenport test: 0.000. \*P-values signi<sup>fi</sup>cant at alpha = 0.05. \*\*P-values signi<sup>fi</sup>cant at alpha = 0.01.

can explain why previous researchers were more likely to choose DT as the base learner to test and verify their ensemble methods. The third interesting thing is that Random Subspace has better comparative results when using DT, KNN, and SVM as the base learner, but it has the worst comparative result when using NB as the base learner. A possible explanation is that NB is sensitive to the feature set because the default random subspace rate is set to 0.5 in the experiments.

## 5.3. Analysis and discussion from the base learner perspective

The average accuracy of different methods across the ten datasets from the base learner perspective is shown in Figs. 8 and 9.

Firstly, as shown in Figs. 8 and 9, RS-SVM has the best average accuracy, i.e., 78.50%, 77.83%, and 75.64% when using Unigram feature sets and gets the best average accuracy, i.e., 75.23%, 74.99%, and 75.30% when using Bigram feature sets. These results further testify that among 20 classi<sup>fi</sup>ers, RS-SVM has a distinct comparative advantage for sentiment classi<sup>fi</sup>cation.

Secondly, when using Unigram feature sets, SVM and NB have better results in the base learner group, Bagging group, Boosting group, and Random Subspace group. When using Bigram feature sets, SVM, NB, and ME obtain better results. These results are consistent with previous research [1,29,43]. Moreover, they further verify why SVM, NB, and ME are the most commonly used machine learning methods for sentiment classi<sup>fi</sup>cation [1,28].

Thirdly, KNN and ensemble classi<sup>fi</sup>ers using KNN as the base learner all have the worst results in the different groups. Following KNN, DT and ensemble classi<sup>fi</sup>ers using DT as the base learner have the second worst results. This is also consistent with prior studies [1,15,28]. KNN and DT can be used as classi<sup>fi</sup>ers when there are relatively few features to consider; however they become dif<sup>fi</sup>cult to manage for large numbers of features [15].

Outcomes of Wilcoxon matched-pairs signed-ranks test (Bigram-TF–IDF).

<table><tr><td rowspan="2"></td><td colspan="2">Bagging NB</td><td colspan="2">Boosting NB</td><td colspan="2">RS NB</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>NB</td><td>5/2/3</td><td>0.902</td><td>4/1/5</td><td>0.739</td><td>0/4/6</td><td>5.265**</td></tr><tr><td>Bagging NB</td><td></td><td></td><td>4/1/5</td><td>0.387</td><td>0/3/7</td><td>4.662**</td></tr><tr><td>Boosting NB</td><td></td><td></td><td></td><td></td><td>3/1/6</td><td>3.606**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging ME</td><td colspan="2">Boosting ME</td><td colspan="2">RS ME</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>ME</td><td>3/1/6</td><td>9.318**</td><td>0/6/4</td><td>8.021**</td><td>3/2/5</td><td>0.122</td></tr><tr><td>Bagging ME</td><td></td><td></td><td>6/0/4</td><td>5.448**</td><td>6/0/4</td><td>6.209**</td></tr><tr><td>Boosting ME</td><td></td><td></td><td></td><td></td><td>5/0/5</td><td>3.318**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging DT</td><td colspan="2">Boosting DT</td><td colspan="2">RS DT</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>DT</td><td>10/0/0</td><td>16.425**</td><td>10/0/0</td><td>12.603**</td><td>10/0/0</td><td>15.465**</td></tr><tr><td>Bagging DT</td><td></td><td></td><td>1/2/7</td><td>6.083**</td><td>2/5/3</td><td>2.050*</td></tr><tr><td>Boosting DT</td><td></td><td></td><td></td><td></td><td>7/1/2</td><td>4.906**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging KNN</td><td colspan="2">Boosting KNN</td><td colspan="2">RS KNN</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>KNN</td><td>6/2/2</td><td>3.473**</td><td>1/6/3</td><td>1.980*</td><td>10/0/0</td><td>21.312**</td></tr><tr><td>Bagging KNN</td><td></td><td></td><td>1/4/5</td><td>4.786**</td><td>9/1/0</td><td>20.104**</td></tr><tr><td>Boosting KNN</td><td></td><td></td><td></td><td></td><td>10/0/0</td><td>21.469**</td></tr><tr><td rowspan="2"></td><td colspan="2">Bagging SVM</td><td colspan="2">Boosting SVM</td><td colspan="2">RS SVM</td></tr><tr><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td><td>s</td><td> $P_w$ </td></tr><tr><td>SVM</td><td>6/3/1</td><td>7.611**</td><td>2/4/4</td><td>9.391**</td><td>8/1/1</td><td>14.287**</td></tr><tr><td>Bagging SVM</td><td></td><td></td><td>1/2/7</td><td>12.154**</td><td>8/0/2</td><td>10.191**</td></tr><tr><td>Boosting SVM</td><td></td><td></td><td></td><td></td><td>8/1/1</td><td>16.576**</td></tr></table>

Note: Iman–Davenport test: 0.000. \*P-values signi<sup>fi</sup>cant at alpha = 0.05. \*\*P-values signi<sup>fi</sup>cant at alpha = 0.01.

## 5.4. Analysis and discussion from the feature set perspective

To compare different weight calculation methods, the performance of Unigram-TP was set to the baseline. The average accuracy improvement of the other <sup>fi</sup>ve methods was calculated as:

Accuracy improvement

$$
= \frac {\text { Average   accuracy } _ {\text { Unigram - TP }} - \text { Average   accuracy } _ {\text { Compared }}}{\text { Average   accuracy } _ {\text { Compared }}}\tag{5}
$$

The results are shown in Figs. 10 to 14.

As shown in Figs. 10 to 14, the Unigram-TP is the best choice for NB, DT, KNN, SVM, and ensemble methods using them as the base learner. It is interesting that for ME and ensemble methods using ME as the base learner, the Unigram-TP is the worst choice. For them, the Bigram-TP is the better choice. These results are consistent with previous research [29,43]. Firstly, for the term present vs. frequency problem [28], the sentiment classi<sup>fi</sup>cation may not be highlighted through repeated use of the same terms. Our experimental results further support these analyses. Secondly, for the problem of whether higher-order N-gram are useful features, our experimental results show that Bigram yield better results only for the ME and ensemble methods using ME as the base learner. In addition, for the Camera, Laptop, and Radio datasets, the best sentiment classi<sup>fi</sup>cation results are from the Bigram feature set. As explanation in [28], this problem appears to be a matter of debate, and the choice depends on different classi<sup>fi</sup>ers and datasets.

(a) Term Present  
![](/api/attachments/ABQKEKXN/fulltext/images/b9a78518cf2b4727dd6ebd744677a298b547517e865c21654df07d830a5eaacf.jpg)

(b) Term Frequency  
![](/api/attachments/ABQKEKXN/fulltext/images/b6ffdb6479d827d05711e1a184a936edc2d09b1ba7ed03969dcf23edea36e794.jpg)

(c) TF-IDF  
![](/api/attachments/ABQKEKXN/fulltext/images/5017980774aa0a61de3d791b464d4e186ae5a8ee64467681fd235613d674a252.jpg)  
Fig. 8. Average accuracy of different methods (Unigram)

## 6. Conclusions and future directions

The rise of social media has fueled interest in sentiment classi<sup>fi</sup>- cation. Promptly and correctly classifying sentiment from the text has become an important task for individuals and companies. In this study, we empirically evaluated ensemble methods (Bagging, Boosting, and Random Subspace) for use in sentiment analysis. Ten public sentiment analysis datasets were investigated to verify the effectiveness of ensemble learning for sentiment analysis. Empirical results showed that ensemble methods can get better results than base learners. Among twenty methods, Random Subspace SVM had the best accuracy. All these results illustrate that ensemble learning methods can be used as a viable method for sentiment classi<sup>fi</sup>cation.

There are several future research directions for this study. Firstly, as the sentiment datasets are often imbalanced, large datasets should be collected to further validate the conclusions of the study. Secondly, feature set is one important factor for classi<sup>fi</sup>cation, but we only used bag-of-word feature sets in this research. In the next step, feature construction based on linguistics should be considered. Thirdly, as ensemble learning methods need a lot of computing time, parallel computing techniques should be explored to tackle this problem. Fourthly, a major limitation of ensemble learning methods is the lack of interpretability of the results: the knowledge learned by ensembles is dif<sup>fi</sup>cult for humans to understand. Therefore improving the interpretability of ensembles is another important research direction.

## Acknowledgments

The authors would like to thank the Editor-in-Chief and reviewers for their recommendation and comments. This work is partially supported by the National Natural Science Foundation of China (Nos. 71071045, 71131002, 71101042), Specialized Research Fund for the Doctoral Program of Higher Education (20110111120014), the China Postdoctoral Science Foundation (2011M501041, 2013T60611), Special Fund of AnHui Province Key Research Institute of Humanities and Social Sciences at Universities (SK2013B400), and Special Fund of Political Theory Research Center of HeFei University of Technology (2012HGXJ0392).

(a) Term Persent  
![](/api/attachments/ABQKEKXN/fulltext/images/614ca6e5c1f1a83c1b813fdcb1b3a4fcca3168b1c360a8a0136550b2fdaeb1d0.jpg)

(b) Term Frequency  
![](/api/attachments/ABQKEKXN/fulltext/images/3c20844e80a0154e58bd4c4ab115e5b69b50191135bcbeae225206a3471527f4.jpg)

(c) TF-IDF  
![](/api/attachments/ABQKEKXN/fulltext/images/6fc341637d35a4883a74a7f62cdea518394835f133850fefd7f2fda2ffa41e98.jpg)

Fig. 9. Average accuracy of different methods (Bigram)  
![](/api/attachments/ABQKEKXN/fulltext/images/e20dca78a3c7fb387b691a2c377d549dae5d749c6e809c90361da2a12f8e9313.jpg)

![](/api/attachments/ABQKEKXN/fulltext/images/14aa53992803591895abcffbf77d1aef4a7d3ef0e0e1d2ac063306e0b63a1437.jpg)

Fig. 10. Average accuracy improvement (Unigram-TP vs. Unigram-TF).  
![](/api/attachments/ABQKEKXN/fulltext/images/c82066373913c39ffeba3f6ab6f5943b3e5eccda1958bc471f6f49f81bd7590e.jpg)  
Fig. 11. Average accuracy improvement (Unigram-TP vs. Unigram-TF–IDF).

Fig. 12. Average accuracy improvement (Unigram-TP vs. Bigram-TP)  
![](/api/attachments/ABQKEKXN/fulltext/images/e3d10e11b4c3af5a5a78f0ab6347367358adc315282734d6e2ccbd0b9248e0b1.jpg)  
Fig. 13. Average accuracy improvement (Unigram-TP vs. Bigram-TF)

Please cite this article as: G. Wang, et al., Sentiment classi<sup>fi</sup>cation: The contribution of ensemble learning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.002

![](/api/attachments/ABQKEKXN/fulltext/images/0536a2886a0eba3264aa30d7b36fc6d3fc8faf13e217ba618a491fb7c3d833ab.jpg)  
Fig. 14. Average accuracy improvement (Unigram-TP vs. Bigram-TF–IDF).

## References

[1] A. Abbasi, H. Chen, A. Salem, Sentiment analysis in multiple languages: feature selection for opinion classi<sup>fi</sup>cation in web forums, ACM Transactions on Information Systems (TOIS) 26 (3) (2008) 12.

[2] A. Abbasi, H. Chen, S. Thoms, T. Fu, Affect analysis of web forums and blogs using correlation ensembles, IEEE Transactions on Knowledge and Data Engineering 20 (9) (2008) 1168–1180.

[3] E. Bauer, R. Kohavi, An empirical comparison of voting classi<sup>fi</sup>cation algorithms: bagging, boosting, and variants, Machine Learning 36 (1–2) (1999) 105–139.

[4] E. Boiy, M.-F. Moens, A machine learning approach to sentiment analysis in multilin gual web texts, Information Retrieval 12 (5) (2009) 526–558.

[5] L. Breiman, Bagging predictors, Machine Learning 24 (2) (1996) 123–140.

[6] H. Chen, C. Yang, Special issue on social media analytics: understanding the pulse of the society, Systems, Man and Cybernetics, Part A: Systems and Humans, IEEE Transactions on 41 (5) (2011) 826–827.

[7] J. Chen, H. Huang, S. Tian, Y. Qu, Feature selection for text classi<sup>fi</sup>cation with Naïve Bayes, Expert Systems with Applications 36 (3) (2009) 5432–5435.

[8] T. Cover, P. Hart, Nearest neighbor pattern classi<sup>fi</sup>cation, Information Theory, IEEE Transactions on 13 (1) (1967) 21–27.

[9] Y. Dang, Y. Zhang, H. Chen, A lexicon-enhanced method for sentiment classi<sup>fi</sup>cation: an experiment on online product reviews, Intelligent Systems, IEEE 25 (4) (2010) 46–53.

[10] B.V. Dasarathy, B.V. Sheela, A composite classi<sup>fi</sup>er system design: concepts and methodology, Proceedings of the IEEE 67 (5) (1979) 708–713.

[11] K. Dave, S. Lawrence, D.M. Pennock, Mining the peanut gallery: opinion extraction and semantic classi<sup>fi</sup>cation of product reviews, Proceedings of the 12th International Conference on World Wide Web, (ACM, 2003), 2003, pp. 519–528.

[12] L. Delacroix, Longman Advanced American Dictionary, Pearson Education, Edinburgh UK, 2007.

[13] J. Demšar, Statistical comparisons of classi<sup>fi</sup>ers over multiple data sets, Journal of Machine Learning Research 7 (2006) 1-30

[14] T. Dietterich, Machine learning research: four current directions, AI Magazine 18 (4) (1997) 97–136.

[15] G. Forman, An extensive empirical study of feature selection metrics for text classification Journal of Machine Learning Research 3 (2003) 1289–1305

[16] N. García-Pedrajas, Constructing ensembles of classi<sup>fi</sup>ers by means of weighted in stance selection, Neural Networks, IEEE Transactions on 20 (2) (2009) 258–277.

[17] L.K. Hansen, P. Salamon, Neural network ensembles, Pattern Analysis and Machine Intelligence, IEEE Transactions on 12 (10) (1990) 993–1001.

[18] V. Hatzivassiloglou, K.R. McKeown, Predicting the semantic orientation of adjectives, Proceedings of the eighth conference on European chapter of the Association for Computational Linguistics. (Association for Computational Linguistics) 1997. pp. 174–181.

[19] T.K. Ho. The random subspace method for constructing decision forests. Pattern Analysis and Machine Intelligence, JEEE Transactions on 20 (8) (1998) 832–844.

[20] Y. Hu, W. Li, Document sentiment classi<sup>fi</sup>cation by exploring description model of topical terms, Computer Speech & Language 25 (2) (2011) 386–403.

[21] R.L. Iman, J.M. Davenport, Approximations of the critical region of the fbietkan statistic, Communications in Statistics—Theory and Methods 9 (6) (1980) 571–595.

[22] S.-M. Kim, E. Hovy, Determining the sentiment of opinions, Proceedings of the 20th international conference on Computational Linguistics, (Association for Computational Linguistics), 2004, p. 1367.

[23] P.C.R. Lane, D. Clarke, P. Hender, On developing robust models for favourability analysis: model choice, feature sets and imbalanced data, Decision Support Systems 53 (4) (2012) 712–718.

[24] W. Li, W. WANG, Y. CHEN,, Heterogeneous ensemble learning for Chinese sentiment classi<sup>fi</sup>cation, Journal of Information & Computational Science 9 (15) (2012) 4551-4558

[25] L. Liu, M.T. Zsu, Encyclopedia of Database Systems, Springer Publishing Company, Incorporated, 2009.

[26] B. Lu, B.K. Tsou, Combining a large sentiment lexicon and machine learning for sub jectivity classi<sup>fi</sup>cation, Machine Learning and Cybernetics (ICMLC), 2010 Interna tional Conference on, (IEEE), 2010, pp. 3311–3316.

[27] B. Pang, L. Lee, A sentimental education: Sentiment analysis using subjectivity summarization based on minimum cuts, Proceedings of the 42nd annual meeting on Association for Computational Linguistics, (Association for Computational Linguistics), 2004, p. 271.

[28] B. Pang, L. Lee, Opinion mining and sentiment analysis, Foundations and Trends in Information Retrieval 2 (1–2) (2008) 1–135.

[29] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up?: sentiment classi<sup>fi</sup>cation using machine learning techniques, Proceedings of the ACL-02 conference on Empirical methods in natural language processing-Volume 10, (Association for Computational Linguistics, 2002, pp. 79–86.

[30] R. Polikar, Ensemble based systems in decision making, Circuits and Systems Magazine, IEEE 6 (3)(2006) 21–45

[31] Morgan kaufmann, J.R. Quinlan, C4. 5: Programs for Machine Learning, , 1993.

[32] K. Sarvabhotla, P. Pingali, V. Varma, Sentiment classi<sup>fi</sup>cation: a lexical similarity based approach for extracting subjectivity in documents, Information Retrieval 14 (3) (2011) 337–353.

[33] R.E. Schapire, The strength of weak learnability, Machine Learning 5 (2) (1990) 197–227.

[34] Y. Su, Y. Zhang, D. Ji, Y. Wang, H. Wu, Ensemble learning for sentiment classi<sup>fi</sup>cation, Chinese Lexical Semantics, Springer, 2013, pp. 84–93.

[35] V.S. Subrahmanian, D. Reforgiato, AVA: adjective–verb–adverb combinations for sentiment analysis, Intelligent Systems, IEEE 23 (4) (2008) 43–50.

[36] T.T. Thet, J.-C. Na, C.S. Khoo, Aspect-based sentiment analysis of movie reviews on discussion boards, Journal of Information Science 36 (6) (2010) 823–848.

[37] K. Tsutsumi, K. Shimada, T. Endo, Movie review classi<sup>fi</sup>cation based on a multiple classi<sup>fi</sup>er, the 21th Paci<sup>fi</sup>c Asia Conference on Language, Information and Computation (PACLIC), 2007.

[38] P.D. Turney, Thumbs up or thumbs down?: semantic orientation applied to unsupervised classi<sup>fi</sup>cation of reviews, Proceedings of the 40th annual meeting on association for computational linguistics, (Association for Computational Linguistics, 2002, pp. 417–424.

[39] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer, 2000

[40] G. Wang, J. Ma, S. Yang, Igf-bagging: information gain based feature selection for bagging, International Journal of Innovative Computing, Information and Control 7 (11) (2011) 6247–6259.

[41] G.I. Webb, Multiboosting: a technique for combining boosting and wagging, Machine Learning 40 (2) (2000) 159–196.

[42] M. Whitehead, L. Yaeger, Building a general purpose cross-domain sentiment mining model, World Congress on Computer Science and Information Engineering, 2009 WRI, IEEE, 2009, pp. 472–476.

[43] M. Whitehead, L. Yaeger, Sentiment mining using ensemble classi<sup>fi</sup>cation models, Innovations and Advances in Computer Sciences and Engineering, Springer, 2010, pp. 509–514.

[44] F. Wilcoxon, Individual comparisons by ranking methods, Biometrics Bulletin 1 (6) (1945) 80–83.

[45] T. Wilson, J. Wiebe, R. Hwa, Recognizing strong and weak opinion clauses, Computational Intelligence 22 (2) (2006) 73–99.

[46] T. Windeatt, G. Ardeshir, Decision tree simpli<sup>fi</sup>cation for classi<sup>fi</sup>er ensembles, International Journal of Pattern Recognition and Arti<sup>fi</sup>cial Intelligence 18 (5) (2004) 749–776.

[47] Morgan Kaufmann, I.H. Witten, E. Frank, M.A. Hall, Data Mining: Practical Machine Learning Tools and Techniques 2011.

[48] R. Xia, C. Zong, S. Li, Ensemble of feature sets and classi<sup>fi</sup>cation algorithms for sentiment classification, Information Sciences 181 (6) (2011) 1138–1152.

[49] J. Yi, T. Nasukawa, R. Bunescu, W. Niblack, Sentiment analyzer: extracting sentiments about a given topic using natural language processing techniques, Data Mining, 2003. ICDM 2003. Third IEEE International Conference on, (IEEE, 2003), 2003, pp. 427–434.

[50] C. Zhang, D. Zeng, J. Li, F.Y. Wang, W. Zuo, Sentiment analysis of Chinese documents: from sentence to document level, Journal of the American Society for Information Science and Technology 60 (12) (2009) 2474–2487.

[51] Z.-H. Zhou, Ensemble Methods: Foundations and Algorithms, Chapman & Hall, 2012.

Gang Wang is an Associate Professor in the School of Management, HeFei University of Technology. He received his Ph. D. in the School of Management, Fudan University. His current research focuses on Data Mining And Business Intelligence, ensemble learning, and social network analysis.

Jianshan Sun is a Ph. D. candidate of joint training of City University of Hong Kong and University of Science and Technology of China. His current research interests include ensemble learning, and business intelligence

Jian Ma is a Professor in the Department of Information Systems, City University of Hong Kong. He received his Doctor of Engineering degree in Computer Science from Asia Institute of Technology. Dr. Ma's research areas include decision and decision support systems, business intelligence, research information systems, research and innovation social networks. His past research has been published in IEEE Transactions on Engineering Management, IEEE Transactions on Education, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems, Information and Management, and European Journal of Operational Research.

Kaiquan Xu is a Assistant Professor in the School of Business, Nanjing University. He has received his Ph.D. in Business Information Systems from the City University of Hong Kong. His research interests include business intelligence and analytics, and knowledge management.

Jibao Gu is a Professor in the School of Management, University of Science and Technology of China. His research interests include marketing and international <sup>fi</sup>nancial.
