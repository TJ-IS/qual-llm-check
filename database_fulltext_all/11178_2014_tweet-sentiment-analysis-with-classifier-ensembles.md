---
otero_id: 11178
otero_key: "NFUJCUW3"
title: "Tweet sentiment analysis with classifier ensembles"
authors: "Nádia F.F. da Silva; Eduardo R. Hruschka; Estevam R. Hruschka"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.07.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Tweet sentiment analysis with classi<sup>fi</sup>er ensembles

Nádia F.F. da Silva <sup>a,</sup>⁎, Eduardo R. Hruschka <sup>a</sup>, Estevam R. Hruschka Jr. <sup>b</sup>

<sup>a</sup> Institute of Mathematics and Computer Sciences, University of São Paulo (USP), São Carlos, SP, Brazil

<sup>b</sup> Department of Computer Science, Federal University of Sao Carlos (UFSCAR), São Carlos, SP, Brazil

## a r t i c l e i n f o

Article history: Received 2 January 2014 Received in revised form 2 May 2014 Accepted 6 July 2014 Available online xxxx

Keywords: Twitter Sentiment analysis Classi<sup>fi</sup>er ensembles

## a b s t r a c t

Twitter is a microblogging site in which users can post updates (tweets) to friends (followers). It has become an immense dataset of the so-called sentiments. In this paper, we introduce an approach that automatically classi<sup>fi</sup>es the sentiment of tweets by using classi<sup>fi</sup>er ensembles and lexicons. Tweets are classi<sup>fi</sup>ed as either positive or negative concerning a query term. This approach is useful for consumers who can use sentiment analysis to search for products, for companies that aim at monitoring the public sentiment of their brands, and for many other applications. Indeed, sentiment classi<sup>fi</sup>cation in microblogging services (e.g., Twitter) through classi<sup>fi</sup>er ensembles and lexicons has not been well explored in the literature. Our experiments on a variety of public tweet sentiment datasets show that classi<sup>fi</sup>er ensembles formed by Multinomial Naive Bayes, SVM, Random Forest, and Logistic Regression can improve classi<sup>fi</sup>cation accuracy.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Twitter is a popular microblogging service in which users post status messages, called “tweets”, with no more than 140 characters. In most cases, its users enter their messages with much fewer characters than the limit established. Twitter represents one of the largest and most dynamic datasets of user generated content — approximately 200 million users post 400 million tweets per day [1]. Tweets can express opinions on different topics, which can help to direct marketing campaigns so as to share consumers' opinions concerning brands and products [2], outbreaks of bullying [3], events that generate insecurity [4], polarity prediction in political and sports discussions [6], and acceptance or rejection of politicians [5], all in an electronic word-of-mouth way. Automatic tools can help decision makers to ensure ef<sup>fi</sup>cient solutions to the problems raised. Under this perspective, the focus of our work is on the sentiment analysis of tweets.

Sentiment analysis aims at determining opinions, emotions, and attitudes reported in source materials like documents, short texts, sentences from reviews [7–9], blogs [10,11], and news [12], among other sources. In such application domains, one deals with large text corpora and most often “formal language”. At least two speci<sup>fi</sup>c issues should be addressed in any type of computer-based tweet analysis: <sup>fi</sup>rst, the frequency of misspellings and slang in tweets is much higher than that in other domains, as users usually post messages from many different electronic devices, such as cell phones and tablets, and develop their own culture of a speci<sup>fi</sup>c vocabulary in this type of environment.

Second, Twitter users post messages on a variety of topics, unlike blogs, news, and other sites, which are tailored to speci<sup>fi</sup>c topics.

We consider sentiment analysis a classi<sup>fi</sup>cation problem. Just like in large documents, sentiments of tweets can be expressed in different ways and classi<sup>fi</sup>ed according to the existence of sentiment, i.e., if there is sentiment in the message, then it is considered polar (categorized as positive or negative), otherwise it is considered neutral. Some authors, on the other hand, consider the six “universal” emotions [13]: anger, disgust, fear, happiness, sadness, and surprise as sentiments. In this paper, we adopt the view that sentiments can be either positive or negative, as in [14–18].

Big challenges can be faced in tweet sentiment analysis (Hassan et al. [19]): (i) neutral tweets are way more common than positive and negative ones. This is different from other sentiment analysis domains (e.g. product reviews), which tend to be predominantly positive or negative; (ii) there are linguistic representational challenges, like those that arise from feature engineering issues; and (iii) tweets are very short and often show limited sentiment cues.

Many researchers have focused on the use of traditional classi<sup>fi</sup>ers, like Naive Bayes, Maximum Entropy, and Support Vector Machines to solve such problems. In this paper, we show that the use of ensembles of multiple base classi<sup>fi</sup>ers, combined with scores obtained from lexicons, can improve the accuracy of tweet sentiment classi<sup>fi</sup>cation. Moreover, we investigate different representations of tweets that take bagof-words and feature hashing into account [20].

The combination of multiple classi<sup>fi</sup>ers to generate a single classi<sup>fi</sup>er has been an active area of research over the last two decades [21–23]. For example, an analytical framework that quanti<sup>fi</sup>es the improvements in classi<sup>fi</sup>cation results due to the combination of multiple models is addressed in [24]. More recently, a survey on traditional ensemble techniques — together with their applications to many dif<sup>fi</sup>cult real-world problems, such as remote sensing, person recognition, and medicine — is presented in [24]. Studies on ensemble learning for sentiment analysis of large text corpora — like those found in movies and product reviews, web forum datasets, and question answering — are reported in [25–31]. In summary, the literature on the subject has shown that from independent, diversi<sup>fi</sup>ed classi<sup>fi</sup>ers, the ensemble created is usually more accurate than its individual components. Related work on tweet sentiment analysis is rather limited [32–34,19], but the initial results are promising.

Studies in tweet sentiment analysis.

<table><tr><td colspan="6">Classification with lexicons and standalone learning algorithms</td></tr><tr><td>Study</td><td>Year</td><td>Feature set</td><td>Lexicon</td><td>Classifier</td><td>Dataset</td></tr><tr><td>Read [39]</td><td>2005</td><td>N-gram</td><td>Emoticons</td><td>Naive Bayes and SVM</td><td>Read [39]</td></tr><tr><td>Go et al. [35]</td><td>2009</td><td>N-gram and POS</td><td>-</td><td>Naive Bayes, Maximum Entropy, and SVM</td><td>Go et al. [35]</td></tr><tr><td>Davidov et al. [36]</td><td>2010</td><td>Punctuation, n-grams, patterns, and tweet-based features</td><td>-</td><td>KNN</td><td>O&#x27;Connor et al. [45]</td></tr><tr><td>Zhang et al. [40]</td><td>2011</td><td>N-gram, emoticons and hashtags</td><td>Ding et al. [46]</td><td>SVM</td><td>Zhang et al. [40]</td></tr><tr><td>Agarwal et al. [38]</td><td>2011</td><td>POS, Lexicon, percentage of capitalized text, exclamation, capitalized text</td><td>Emoticons listed from  $Wikipedia^a$ , an acronym  $dictionary^b$ </td><td>SVM</td><td>Agarwal et al. [38]</td></tr><tr><td>Speriosu et al. [47]</td><td>2011</td><td>N-gram, hashtags, emoticons, lexicon and Twitter follower graph</td><td>Wilson et al. [48]</td><td>Maximum Entropy</td><td>Go et al. [35] and Speriosu et al. [47]</td></tr><tr><td>Saif et al. [42]</td><td>2012</td><td>N-gram, POS and semantic features</td><td>-</td><td>Naive Bayes</td><td>Go et al. [35], Speriosu et al. [47] and Shamma et al. [49]</td></tr><tr><td>Hu et al. [37]</td><td>2013</td><td>N-gram, POS, data representation of social relations</td><td>-</td><td>-</td><td>Go et al. [35] and Shamma et al. [49]</td></tr><tr><td>Saif et al. [41]</td><td>2013</td><td>N-gram, capitalized text, POS, lexicons</td><td>Mohammad and Yang [50], Wilson et al. [48], Hu and Liu [9], and other lexicons constructed from hashtags</td><td>SVM</td><td>Nakov et al. [51]</td></tr><tr><td colspan="6">Ensemble learning</td></tr><tr><td>Study</td><td>Year</td><td>Feature set</td><td>Base learner</td><td>Ensemble methods</td><td>Dataset</td></tr><tr><td>Lin and Kolcz [32]</td><td>2012</td><td>Feature hashing</td><td>Logistic Regression classifier</td><td>Majority vote</td><td>Private dataset ([32])</td></tr><tr><td>Rodriguez et al. [34]</td><td>2013</td><td>N-gram, lexicon, POS, tweet-based features and SentiWordnet</td><td>CRF, SVM and heuristic method</td><td>Majority vote, upper bound, ensemble vote</td><td>Nakov et al. [51]</td></tr><tr><td>Clark et al. [33]</td><td>2013</td><td>N-gram, lexicon and polarity strength</td><td>Naive Bayes</td><td>Weighted voting scheme</td><td>Nakov et al. [51]</td></tr><tr><td>Hassan et al. [19]</td><td>2013</td><td>A combination of unigrams and bigrams of simple words, part-of-speech and semantic features derived from WordNet [43] and SentiWordNet 3.0 [44]</td><td>RBF Neural Network, RandomTree, REP Tree, Naive Bayes, Bayes Net, Logistic Regression and SVM.</td><td>A bootstrap model by combining dataset, feature and classifier parameters</td><td>Sanders - Twitter Sentiment  $Corpus^c$ </td></tr></table>

a. http://en,wikipedia.org/wiki/List of emoticons.  
<sup>b</sup> http://www.noslang.com/.  
<sup>c</sup> http://www.sananalytics.com/lab/twitter-sentiment/.

Our main contributions can be summarized as follows: (i) we show that classi<sup>fi</sup>er ensembles formed by diversi<sup>fi</sup>ed components are promising for tweet sentiment analysis; (ii) we compare bag-of-words and feature hashing-based strategies for the representation of tweets and show their advantages and drawbacks; and (iii) classi<sup>fi</sup>er ensembles obtained from the combination of lexicons, bag-of-words, emoticons, and feature hashing are studied and discussed.

The remainder of the paper is organized as follows: Section 2 addresses the related work. Section 3 describes our approach, for which experimental results are provided in Section 4. Section 5 concludes the paper and discusses directions for future work.

## 2. Related work

Several studies on the use of stand-alone classi<sup>fi</sup>ers for tweet sentiment analysis are available in the literature, as shown in the summary in Table 1. Some of them propose the use of emoticons and hashtags for building the training set, as Go et al. [35] and Davidov et al. [36], who identi<sup>fi</sup>ed tweet polarity by using emoticons as class labels. Others use the characteristics of the social network as networked data, like in Hu et al. [37]. According to the authors, emotional contagion theories are materialized based on a mathematical optimization formulation for the supervised learning process. Approaches that integrate opinion mining lexicon-based techniques and learning-based techniques have been studied. For example, Agarwal et al. [38], Read [39], Zhang et al. [40], and Saif et al. [41] used lexicons, part-of-speech, and writing style as linguistic resources. In a similar context, Saif et al. [42] introduced an approach to add semantics to the training set as an additional feature. For each extracted entity (e.g., iPhone), they added its respective semantic concept (like “Apple's product”) as an additional feature and measured the correlation of the representative concept as negative/positive sentiments.

Classi<sup>fi</sup>er ensembles for tweet sentiment analysis have been underexplored in the literature — few exceptions are [32–34,19]. Lin and Kolcz [32] used Logistic Regression classi<sup>fi</sup>ers learned from 4- gram hashed byte as features.<sup>1</sup> They made no attempt to perform any linguistic processing, not even word tokenization. For each of the (proprietary) datasets, they experimented with ensembles of different sizes, composed of different models, and obtained from different training sets, however with the same learning algorithm (Logistic Regression). Their results show that the ensembles lead to more accurate classi<sup>fi</sup>ers. The authors also proposed an approach to obtain diversi<sup>fi</sup>ed classi<sup>fi</sup>ers by using different training datasets (over the random shuf<sup>fl</sup>e of the training examples) [32].Rodriguez et al. [34] and Clark et al. [33] proposed the use of classi<sup>fi</sup>er ensembles at expression-level, which is related to Contextual Polarity Disambiguation. In this perspective, the sentiment label (positive, negative, or neutral) is applied to a speci<sup>fi</sup>c phrase or word within the tweet and does not necessarily match the sentiment of the entire tweet. Finally, a promising ensemble framework was recently proposed by Hassan et al. [19], who deal with class imbalance, sparsity, and representational issues. The authors propose enriching the corpus by using multiple additional datasets also related to sentiment classi<sup>fi</sup>cation. The authors use a combination of unigrams and bigrams of simple words, part-of-speech, and semantic features derived from WordNet [43] and SentiWordNet 3.0 [44]. Also, they employed summarizing techniques, like Legomena and Named Entity Recognition.

In our approach, we make use of feature hashing, which is a relatively new topic for text classi<sup>fi</sup>cation (broadly de<sup>fi</sup>ned) — e.g., see [20, 52–54]. Note that in traditional document classi<sup>fi</sup>cation tasks, the input to the machine learning algorithm is a free text, from which a bag-of-words representation is constructed — the individual tokens are extracted, counted, and stored as vectors. Typically, in tweets, these vectors are extremely sparse. One can deal with this sparsity by using feature hashing. It is a fast way of building a vector space model of features, which turns features into either a vector or a matrix. Such an approach produces features represented as hash integers rather than strings. Asiaee et al. [55] showed that the performance of the classi<sup>fi</sup>cation can be improved in a low dimensional space via feature hashing [20]. Similarly, Lin and Kolcz [32] used feature hashing to deal with the high dimensional input space of tweets and showed that it can improve the performance of the machine learning algorithms.

We shall remark that our work differs from the existing work due to several aspects: (i) we compare bag-of-words and feature hashing based strategies for the representation of tweets and show their advantages and drawbacks; (ii) we study classi<sup>fi</sup>er ensembles obtained from the combination of lexicons, bag-of-words, emoticons, and feature hashing. Although Lin and Kolcz [32] used feature hashing in an ensemble of classi<sup>fi</sup>ers, they trained the classi<sup>fi</sup>ers in partitions of a private dataset and did not use lexicons and emoticons. They used only Logistic Regression as a classi<sup>fi</sup>er. Rodriguez et al. [34] and Clark et al. [33] proposed the use of classi<sup>fi</sup>er ensembles at expression-level, while we are interested in the use of classi<sup>fi</sup>er ensembles at tweet-level. Hassan et al. [19] used a speci<sup>fi</sup>c combination of datasets as training data, different features, different classi<sup>fi</sup>ers, and different combination rules of classi<sup>fi</sup>ers. We are interested in exposing the pros and cons of classi<sup>fi</sup>er ensembles in combination with two possibilities for the representation of a tweet — feature hashing and bag-of-words. We also explore the gains of the enrichment of the representations with lexicons.

## 3. Classi<sup>fi</sup>er ensembles for tweet sentiment analysis

Ensemble methods train multiple learners to solve the same problem [22]. In contrast to classic learning approaches, which construct one learner from the training data, ensemble methods construct a set of learners and combine them. Dietterich [56] lists three reasons for using an ensemble based system:

Statistical Assume that we have a number of different classi-<sup>fi</sup>ers, and that all of them provide good accuracy in the training set. If a single classi<sup>fi</sup>er is chosen from the available ones, it may not yield the best generalization performance in unseen data. By combining the outputs of a set of classi<sup>fi</sup>ers, the risk of selecting an inadequate one is lower [21];

Computational Many learning algorithms work by carrying out a local search that may get stuck in local optima which may be far from global optima. For example, decision tree algorithms employ a greedy splitting rule and neural network algorithms employ gradient descent to minimize an error function over the training set. An ensemble constructed by running the local search from many different starting points may provide a better approximation than any of the individual classi<sup>fi</sup>ers;

Representational If the chosen model cannot properly represent the sought decision boundary, classi<sup>fi</sup>er ensembles with diversi<sup>fi</sup>ed models can represent the decision boundary. Certain problems are too dif<sup>fi</sup>cult for a given classi<sup>fi</sup>er to solve. Sometimes, the decision boundary that separates data from different classes may be too complex and an appropriate combination of classi<sup>fi</sup>ers can make it possible to cope with this issue.

From a practical point of view, one may ask: What is the most appropriate classi<sup>fi</sup>er for a given classi<sup>fi</sup>cation problem? This question can be interpreted in two different ways [22]: (i) What type of classi<sup>fi</sup>er should be chosen among many competing models, such as Support Vector Machines (SVM), Decision Trees, Naive Bayes Classi<sup>fi</sup>er?; (ii) Given a particular classi<sup>fi</sup>cation algorithm, which realization of this algorithm should be chosen? For example, different types of kernels used in SVM

![](/api/attachments/NFUJCUW3/fulltext/images/65557f40495e998697c82456d681f9bd38bb2c98d1ffdb78beb69b55c0a76775.jpg)  
Fig. 1. Classi<sup>fi</sup>er ensemble for tweet sentiment analysis: Σ refers to the combination rule (e.g., majority vote and average of class probabilities) for the base classi<sup>fi</sup>ers

Please cite this article as: N.F.F. da Silva, et al., Tweet sentiment analysis with classi<sup>fi</sup>er ensembles, Decision Support Systems (2014), http:// dx.doi.org/10.1016/j.dss.2014.07.003

N.F.F. da Silva et al. / Decision Support Systems xxx (2014) xxx–xxx

![](/api/attachments/NFUJCUW3/fulltext/images/c8ebe7804be80b035e79e98b2132136b472c6fff09d094317202991462ea12d9.jpg)  
Fig. 2. An example of majority voting as the combination rule. In this case, the majority of the classi<sup>fi</sup>ers agree that the class is positive.

can lead to different decision boundaries, even if all the other parameters are kept constant. Using an ensemble of such models and combining their outputs — e.g. by averaging them — the risk of an unfortunate selection of a particularly poorly performing classi<sup>fi</sup>er can be reduced.

It is important to emphasize that there is no guarantee that the combination of multiple classi<sup>fi</sup>ers will always perform better than the best individual classi<sup>fi</sup>er in the ensemble. Except for certain special cases [57], the ensemble average performance can not be guaranteed. Combining classi<sup>fi</sup>ers may not necessarily beat the performance of the best classi<sup>fi</sup>er in the ensemble, however it certainly reduces the overall risk of making a poor selection of the classi<sup>fi</sup>er to be used with new (target) data.

Effective ensembles require that the individual components exhibit some level of diversity [58,59,21,60]. Within the classi<sup>fi</sup>cation context, classi<sup>fi</sup>ers should generate different decision boundaries. If proper diversity is achieved, independent errors are produced by each classi<sup>fi</sup>er, and combining them usually reduces the total error. Fig. 1, adapted from [61], illustrates this concept for a common setting in our particular application domain: each classi<sup>fi</sup>er, trained in a different subset of the available training data, produces different errors. However, the combination of classi<sup>fi</sup>ers can provide the best decision boundary. Indeed, the Bayes error may be estimated from classi<sup>fi</sup>er ensembles [62]. Figs. 2 and 3 provide examples of combination rules.

Brown et al. [63] suggested three methods for creating diversity in classi<sup>fi</sup>er ensembles: (i) varying the starting points within the hypothesis space (for example, by different initializations of the learning algorithm); (ii) varying the training set for the base classi<sup>fi</sup>ers; and (iii) varying the base classi<sup>fi</sup>ers or ensemble strategies. Our focus is on (iii), different from Lin and Kolcz [32] and Clark et al. [33] that addressed diversity according to (ii), and Rodriguez et al. [34] that focus on an expression-level analysis, applying diversity according to the training set for the base classi<sup>fi</sup>ers.

## 3.1. Our approach

Our hypothesis is that, by holding the philosophy underlying the use of classi<sup>fi</sup>er ensembles, endowed with appropriate feature engineering, accurate tweet sentiment classi<sup>fi</sup>cation can be obtained.

Fig. 4 shows an overview of the approach adopted. Our base classi-<sup>fi</sup>ers are Random Forest, Support Vector Machines (SVM), Multinomial Naive Bayes, and Logistic Regression. Although we could have chosen other classi<sup>fi</sup>ers, the ones adopted here have been widely used in practice, therefore they are suitable as a proof of concept.

In practice, classi<sup>fi</sup>ers are built to classify unseen data, usually referred to as a target dataset. In a controlled experimental setting, as in the one addressed in Section 4, a validation set represents the target set. Actually, in controlled experimental settings the target set is frequently referred to as either a test or a validation set. These two terms have been used interchangeably, sometimes causing confusion. In our study, we assume that the target/validation set has not been used at all in the process of building the classi<sup>fi</sup>er ensembles. Once the base classi<sup>fi</sup>ers have been trained, a classi<sup>fi</sup>er ensemble is formed by (i) the average of the class probabilities obtained by each classi<sup>fi</sup>er or (ii) the majority voting.

The techniques used for feature representation (bag-of-words and feature hashing) and preprocessing tweet data are addressed in details in the next subsections.

## 3.1.1. Feature representation

Two techniques for feature representation are particularly suitable for tweet sentiment classi<sup>fi</sup>cation:

• Bag-of-words. Tweets are represented by a table in which the columns represent the terms (or existing words) in the tweets and the values represent their frequencies. Therefore, a collection of tweets — after the preprocessing step addressed later — can be represented as illustrated in Table 2, in which there are n tweets and m terms.<sup>2</sup> Each tweet is represented as $t w e e t _ { i } = ( a _ { i 1 } , a _ { i 2 } , . . . , a _ { i m } )$ , where $a _ { i j }$ is the fre quency of term t in the tweet . This value can be calculated in various ways.

• Feature hashing. It is used for text classi<sup>fi</sup>cation in [52,20,54,64,65]. For tweet classi<sup>fi</sup>cation, feature hashing offers an approach that reduces the number of features provided as input to a learning algorithm. The original high-dimensional space is “reduced” by hashing the features into a lower-dimensional space, i.e., mapping features to hash keys. Multiple features can be mapped to the same hash key, therefore their counts are “aggregated”. Fig. 5 shows the application of feature hashing to the tweet “@John: “I stand in solidarity with #ows.”!”. In the fourth step we use the hashing function in Eq. (1), which takes an l-length string s as a parameter and returns the sum of ASCII values of their characters (c ).

$$
h (s) = \Sigma_ {i} ^ {l} A S C I I (c _ {i}) / 1 0.\tag{1}
$$

## 3.1.2. Preprocessing

Retweets, stop words, links, URLs, mentions, punctuation, and accentuation were removed so that data set could be standardized. Stemming was performed so as to minimize sparsity. The bag-of-words was constructed with binary frequency, and a term is considered “frequent” if it occurs in more than one tweet.

We also used the opinion lexicon<sup>3</sup> proposed by Hu and Liu [9], who created a list of 4783 negative words and 2006 positive words. This list was compiled over many years and each of its words indicates an opinion. Positive opinion words are used to express desired states while negative opinion words are used to express undesired states. Examples of positive opinion words are beautiful, wonderful, good, and amazing and examples of negative opinion words are bad, poor, and terrible.

N.F.F. da Silva et al. / Decision Support Systems xxx (2014) xxx–xxx  
![](/api/attachments/NFUJCUW3/fulltext/images/f9595c00223bf36cc55ee392cc05d7f61eb626e1968d061e7bf6692fa0bd0abe.jpg)  
Fig. 3. An example of averaging probabilities as the combination rule. In this case, probability P(class = positive tweet) N P(class = negative tweet), then the output of the ensemble is positive.

![](/api/attachments/NFUJCUW3/fulltext/images/a324b3189d2c259bbacaf8c54ddf950452386b534e88c6e2b79644cbf0cf6b8c.jpg)  
Fig. 4. Overview of our approach.

Emoticons available in the tweets have been used to enrich our feature set. The number of positive and negative emotions was used to complement the information provided by the bag-of-words and the feature hashing. Moreover, we computed the number of positive and negative lexicons in each message.

## 4. Experimental evaluation

## 4.1. Datasets

Our experiments were performed in representative datasets obtained from tweets on different subjects [66]:

## 4.1.1. Sanders — Twitter Sentiment Corpus

It consists of hand-classi<sup>fi</sup>ed tweets collected from four Twitter search terms: @apple, #google, #microsoft, and #twitter. Each tweet has a sentiment label: positive, neutral, negative, and irrelevant. As in [67], we reported only the classi<sup>fi</sup>cation results for positive and negative classes, which resulted in 570 positive and 654 negative tweets.

## 4.1.2. Stanford — Twitter Sentiment Corpus

This dataset [35] has 1,600,000 training tweets collected by a scraper that queries the Twitter API. The scraper, periodically, sends a query to the positive emotion – :) – and a separate query to the negative emotion – :( – at the same time. After removing retweets, any tweet containing both positive and negative emoticons, repeated tweets, and bias caused by the emotions, one gets 800,000 tweets with positive emoticons and 800,000 tweets with negative emoticons. In contrast to the training set, which was collected based on speci<sup>fi</sup>c emoticons, the test set was collected by searching Twitter API with speci<sup>fi</sup>c queries and including product names, companies, and people. The tweets were manually annotated with a class label and 177 negative and 182 positive tweets were obtained. Although the Stanford test set is relatively small, it has been widely used in the literature in different evaluation tasks. For example, Go et al. [35], Saif et al. [42], Speriosu et al. [47], and

Bakliwal et al. [68] use it to evaluate their models for polarity classi<sup>fi</sup>cation (positive vs. negative). In addition to polarity classi<sup>fi</sup>cation, Marquez et al. [69] use this dataset for evaluating subjectivity classi<sup>fi</sup>cation (neutral vs. polar).

## 4.1.3. Obama-McCain Debate (OMD)

This dataset was constructed from 3238 tweets crawled during the <sup>fi</sup>rst U.S. presidential TV debate that took place in September 2008 [49]. The sentiment ratings of the tweets were acquired by using the Amazon Mechanical Turkte<sup>4</sup>. Each tweet was rated as positive, negative, mixed, and others. “Other” tweets are those that could not be rated. We kept only the tweets rated by at least three voters, which comprised a set of 1906 tweets, from which 710 were positive and 1196 were negative ones. In another con<sup>fi</sup>guration of the dataset, we considered only tweets with unanimity of opinion. We named it Strict Obama-McCain Debate (OMD) dataset, which has 916 tweets — 347 positive and 569 negative.

## 4.1.4. Health care reform (HCR)

This dataset was built by crawling tweets containing the hashtag “#hcr” (health care reform) in March 2010 [47]. A subset of this corpus was manually annotated as positive, negative, and neutral. The neutral tweets were not considered in the experiments, thus the training dataset contained 621 tweets (215 positive and 406 negative) whereas the test set contained 665 (154 positive and 511 negative).

## 4.2. Experimental setup

We conducted experiments in the WEKA platform<sup>5</sup> to run Multinomial Naive Bayes, Logistic Regression, and Random Forests. We used the Library for Support Vector Machines [70] LibSVM<sup>6</sup> for training SVM classi<sup>fi</sup>ers. For Obama-McCain Debate and Sanders Twitter Sentiment datasets we used the standard 10-fold cross validation. For Health Care Reform dataset, we used the same training and test folds available in the public resource [42]. Finally, for the Stanford Twitter Sentiment Corpus we did samplings from the original training set and validated in the test set available in [35].

Table 2  
Representation of tweets.

<table><tr><td></td><td> $t_1$ </td><td> $t_2$ </td><td>...</td><td> $t_m$ </td></tr><tr><td> $tweet_1$ </td><td> $a_{11}$ </td><td> $a_{12}$ </td><td>...</td><td> $a_{1m}$ </td></tr><tr><td> $tweet_2$ </td><td> $a_{21}$ </td><td> $a_{22}$ </td><td>...</td><td> $a_{2m}$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $tweet_n$ </td><td> $a_{n1}$ </td><td> $a_{n2}$ </td><td>...</td><td> $a_{nm}$ </td></tr></table>

## 4.3. Results

We compared the results of stand-alone classi<sup>fi</sup>ers with those of our ensemble approach described in Section 3.1. By considering different combinations of bag-of-words (BoW), feature hashing (FH), and lexicons, we can evaluate the potential of ensembles to boost classi<sup>fi</sup>cation accuracy. The best results described in the literature are also reported for comparison purposes.

Table 3 shows the results of the BoW-based approaches, whereas Table 4 focuses on the results of feature hashing. According to the tables, our ensembles provided accuracy gains in all assessed settings. As expected, the use of classi<sup>fi</sup>er ensembles may lead to additional computational costs, however accuracy gains are usually worthwhile. In pairwise comparisons of classi<sup>fi</sup>ers with and without lexicons, the former ones provided better results in all the experiments. As mentioned in Section 3.1, the lexicon dictionary was constructed for reviews of products sold on-line [9]. It consists of informal words, as well as types of messages, found in tweets. In the Stanford dataset the improvement was more relevant since the data has been collected from emoticons. In this type of dataset, there is no speci<sup>fi</sup>c domain, while the other datasets address more speci<sup>fi</sup>c topics, like technology (Sanders), politics (Strict OMD and OMD) and health (HCR dataset).

According to the feature hashing results (Table 4), our ensembles showed better accuracy rates than single base classi<sup>fi</sup>ers for all the datasets. By taking the average of the positive and negative F-Measure into account, we obtained the best results in 80% of the BoW cases. Note that feature hashing provides worse results than BoW in most of the datasets, except for the HCR dataset, where the results have shown to be the best in literature — including here our own results for the BoW-based ensemble. However, as expected, feature hashing enables a signi<sup>fi</sup>cant reduction in dimensionality, as shown in Table 5, and there is a trade-off between classi<sup>fi</sup>cation accuracy and computational savings. It is important to reinforce that none of the results reported in the literature make use of any dimensionality reduction technique and thereby can not be compared to our results obtained with feature hashing. To the best of our knowledge, feature hashing has not been assessed in public data sets for the sentiment analysis of tweets.

Some additional experiments for the Stanford dataset were also conducted. Due to computational limitations, we did not run experiments with the complete training data, but from balanced random sampling, whose sample sizes varied from 500 to 3000 tweets. We chose standalone classi<sup>fi</sup>ers as baselines to be compared to our ensemble approach. By considering different combinations of bag-of-words (BoW) and lexicons, we can evaluate the potential of ensembles to boost classi<sup>fi</sup>cation accuracy. Fig. 6 shows the overall picture of all machine learning

![](/api/attachments/NFUJCUW3/fulltext/images/ade5c7289dde678391eab922f5a9c8d9a28311a155561c70d151410fefea7603.jpg)  
Fig. 5. Feature hashing in a tweet example.

## Table 3

Cross comparison results for bag-of-words (best results in bold). LR, RF, and MNB refer to Logistic Regression, Random Forest, and Multinomial Naive Bayes, respectively. ENS indicates the use of ensembles, BoW refers to bag-of-words, lex refers to lexicon, and the SVM-BoW + lex abbreviation indicates that we used SVM with bag-of-words and lexicon as features. Other abbreviations are Acc. for the accuracy, F1 for the F-measure, and Avg for the average of positive and negative F-measures.

<table><tr><td rowspan="2">Method</td><td rowspan="2">Acc. (%)</td><td colspan="3">Positive class</td><td colspan="3">Negative class</td><td>Avg.</td></tr><tr><td>Precision (%)</td><td>Recall (%)</td><td>F1 (%)</td><td>Precision (%)</td><td>Recall (%)</td><td>F1 (%)</td><td>F1 (%)</td></tr><tr><td colspan="9">OMD dataset</td></tr><tr><td>SVM-BoW</td><td>72.25</td><td>64.90</td><td>55.50</td><td>59.80</td><td>75.70</td><td>82.20</td><td>78.80</td><td>69.30</td></tr><tr><td>SVM-BoW + lex</td><td>75.55</td><td>68.40</td><td>63.90</td><td>66.10</td><td>79.40</td><td>82.40</td><td>80.90</td><td>73.50</td></tr><tr><td>RF-BoW</td><td>71.04</td><td>62.90</td><td>54.20</td><td>58.20</td><td>74.90</td><td>81.00</td><td>77.80</td><td>68.00</td></tr><tr><td>RF-BoW + lex</td><td>73.82</td><td>66.70</td><td>59.30</td><td>62.80</td><td>77.30</td><td>82.40</td><td>79.80</td><td>71.30</td></tr><tr><td>LR-BoW</td><td>70.57</td><td>66.90</td><td>41.50</td><td>51.30</td><td>71.70</td><td>87.80</td><td>78.90</td><td>65.10</td></tr><tr><td>LR-BoW + lex</td><td>73.85</td><td>66.10</td><td>56.90</td><td>61.20</td><td>76.40</td><td>82.70</td><td>79.40</td><td>70.30</td></tr><tr><td>MNB-BoW</td><td>72.19</td><td>64.00</td><td>57.90</td><td>60.80</td><td>76.30</td><td>80.70</td><td>78.50</td><td>69.65</td></tr><tr><td>MNB-BoW + lex</td><td>75.97</td><td>68.80</td><td>65.10</td><td>66.90</td><td>79.90</td><td>82.40</td><td>81.20</td><td>74.05</td></tr><tr><td>ENS(LR + RF + MNB + SVM)-BoW</td><td>73.14</td><td>66.30</td><td>56.60</td><td>61.10</td><td>76.30</td><td>82.90</td><td>79.50</td><td>70.30</td></tr><tr><td>ENS(LR + RF + MNB)-BoW + lex</td><td>76.81</td><td>71.10</td><td>63.70</td><td>67.20</td><td>79.70</td><td>84.60</td><td>82.10</td><td>74.65</td></tr><tr><td>Best result from the literature [37,42]</td><td>76.30</td><td>75.00</td><td>66.60</td><td>70.30</td><td>82.90</td><td>88.10</td><td>85.40</td><td>77.85</td></tr><tr><td colspan="9">Strict OMD dataset</td></tr><tr><td>SVM-BoW</td><td>74.02</td><td>67.60</td><td>60.20</td><td>63.70</td><td>77.30</td><td>82.40</td><td>79.80</td><td>71.75</td></tr><tr><td>SVM-BoW + lex</td><td>78.93</td><td>73.80</td><td>68.90</td><td>71.20</td><td>81.80</td><td>85.10</td><td>83.40</td><td>77.30</td></tr><tr><td>RF-BoW</td><td>73.91</td><td>65.30</td><td>66.60</td><td>65.90</td><td>79.40</td><td>78.40</td><td>78.90</td><td>72.40</td></tr><tr><td>RF-BoW + lex</td><td>79.36</td><td>70.90</td><td>77.20</td><td>73.90</td><td>85.30</td><td>80.70</td><td>82.90</td><td>78.40</td></tr><tr><td>LR-BoW</td><td>72.38</td><td>70.60</td><td>46.40</td><td>56.00</td><td>73.00</td><td>85.20</td><td>79.90</td><td>67.95</td></tr><tr><td>LR-BoW + lex</td><td>78.06</td><td>74.50</td><td>64.00</td><td>68.80</td><td>79.80</td><td>86.60</td><td>83.10</td><td>75.95</td></tr><tr><td>MNB-BoW</td><td>75.43</td><td>68.70</td><td>64.60</td><td>66.60</td><td>79.20</td><td>82.10</td><td>80.60</td><td>73.60</td></tr><tr><td>MNB-BoW + lex</td><td>80.13</td><td>74.50</td><td>72.30</td><td>73.40</td><td>83.40</td><td>84.90</td><td>84.10</td><td>78.75</td></tr><tr><td>ENS(LR + RF + MNB)-BoW</td><td>75.55</td><td>70.20</td><td>59.70</td><td>64.50</td><td>77.50</td><td>84.50</td><td>80.80</td><td>72.65</td></tr><tr><td>ENS(LR + RF + MNB)-BoW + lex</td><td>80.35</td><td>73.50</td><td>75.20</td><td>74.40</td><td>84.70</td><td>83.50</td><td>84.10</td><td>79.25</td></tr><tr><td>Best result from the literature [37,42]</td><td>76.30</td><td>75.00</td><td>66.60</td><td>70.30</td><td>82.90</td><td>88.10</td><td>85.40</td><td>77.85</td></tr><tr><td colspan="9">Sanders - Twitter Sentiment Corpus</td></tr><tr><td>SVM-BoW</td><td>82.43</td><td>80.00</td><td>83.00</td><td>81.50</td><td>84.70</td><td>82.00</td><td>83.30</td><td>82.40</td></tr><tr><td>SVM-BoW + lex</td><td>83.98</td><td>81.20</td><td>85.40</td><td>83.20</td><td>86.70</td><td>82.70</td><td>84.70</td><td>83.95</td></tr><tr><td>RF-BoW</td><td>79.24</td><td>75.60</td><td>81.90</td><td>78.60</td><td>83.00</td><td>76.90</td><td>79.80</td><td>79.20</td></tr><tr><td>RF-BoW + lex</td><td>82.35</td><td>78.80</td><td>84.90</td><td>81.80</td><td>85.90</td><td>80.10</td><td>82.90</td><td>82.35</td></tr><tr><td>LR-BoW</td><td>77.45</td><td>76.40</td><td>74.60</td><td>75.50</td><td>78.30</td><td>80.00</td><td>79.10</td><td>77.30</td></tr><tr><td>LR-BoW + lex</td><td>79.49</td><td>77.20</td><td>79.50</td><td>78.30</td><td>81.60</td><td>79.50</td><td>80.60</td><td>79.45</td></tr><tr><td>MNB-BoW</td><td>79.82</td><td>80.10</td><td>75.40</td><td>77.70</td><td>79.60</td><td>83.60</td><td>81.60</td><td>79.65</td></tr><tr><td>MNB-BoW + lex</td><td>83.41</td><td>82.90</td><td>81.10</td><td>82.00</td><td>83.80</td><td>85.50</td><td>84.60</td><td>83.30</td></tr><tr><td>ENS(LR + RF + MNB + SVM)-BoW</td><td>82.76</td><td>80.70</td><td>82.80</td><td>81.70</td><td>84.70</td><td>82.70</td><td>83.70</td><td>82.70</td></tr><tr><td>ENS(SVM + RF + MNB)-BoW + lex</td><td>84.89</td><td>82.10</td><td>86.30</td><td>84.20</td><td>87.50</td><td>83.60</td><td>85.50</td><td>84.85</td></tr><tr><td>Best result from the literature [67]</td><td>84.40</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="9">Best sampling with Stanford dataset - sampling with 3000 tweets</td></tr><tr><td>SVM-BoW</td><td>67.41</td><td>67.2</td><td>69.80</td><td>68.50</td><td>67.60</td><td>65.00</td><td>66.30</td><td>67.40</td></tr><tr><td>SVM-BoW + lex</td><td>73.82</td><td>72.90</td><td>76.90</td><td>74.90</td><td>74.90</td><td>70.60</td><td>72.70</td><td>73.80</td></tr><tr><td>RF-BoW</td><td>66.57</td><td>65.00</td><td>73.60</td><td>69.10</td><td>68.60</td><td>59.30</td><td>63.60</td><td>66.35</td></tr><tr><td>RF-BoW + lex</td><td>74.37</td><td>73.00</td><td>78.60</td><td>75.70</td><td>76.10</td><td>70.10</td><td>72.90</td><td>74.30</td></tr><tr><td>LR-BoW</td><td>64.90</td><td>60.00</td><td>92.30</td><td>72.70</td><td>82.30</td><td>36.70</td><td>50.80</td><td>61.75</td></tr><tr><td>LR-BoW + lex</td><td>76.32</td><td>73.20</td><td>84.10</td><td>78.30</td><td>80.70</td><td>68.40</td><td>74.00</td><td>76.15</td></tr><tr><td>MNB-BoW</td><td>71.31</td><td>72.10</td><td>70.90</td><td>71.50</td><td>70.60</td><td>71.80</td><td>71.10</td><td>71.30</td></tr><tr><td>MNB-BoW + lex</td><td>79.39</td><td>80.70</td><td>78.00</td><td>79.30</td><td>78.10</td><td>80.80</td><td>79.40</td><td>79.35</td></tr><tr><td>ENS(LR + RF + MNB)-BoW</td><td>72.14</td><td>70.50</td><td>77.50</td><td>73.80</td><td>74.20</td><td>66.70</td><td>70.20</td><td>72.00</td></tr><tr><td>ENS(LR + RF + MNB)-BoW + lex</td><td>81.06</td><td>79.70</td><td>84.10</td><td>81.80</td><td>82.60</td><td>78.00</td><td>80.20</td><td>81.00</td></tr><tr><td>Best result from the literature [68,42]</td><td>87.20</td><td>85.80</td><td>79.40</td><td>82.50</td><td>82.70</td><td>88.20</td><td>85.30</td><td>83.90</td></tr><tr><td colspan="9">HCR dataset</td></tr><tr><td>SVM-BoW</td><td>73.99</td><td>42.00</td><td>32.50</td><td>36.60</td><td>81.00</td><td>86.50</td><td>83.60</td><td>60.10</td></tr><tr><td>SVM-BoW + lex</td><td>75.94</td><td>47.50</td><td>37.00</td><td>41.60</td><td>82.20</td><td>87.70</td><td>84.80</td><td>63.20</td></tr><tr><td>RF-BoW</td><td>70.83</td><td>34.60</td><td>29.20</td><td>31.70</td><td>79.60</td><td>83.40</td><td>81.50</td><td>56.60</td></tr><tr><td>RF-BoW + lex</td><td>72.93</td><td>38.40</td><td>27.90</td><td>32.30</td><td>79.90</td><td>86.50</td><td>83.10</td><td>57.70</td></tr><tr><td>LR-BoW</td><td>73.83</td><td>40.00</td><td>26.00</td><td>31.50</td><td>79.80</td><td>88.30</td><td>83.80</td><td>57.65</td></tr><tr><td>LR-BoW + lex</td><td>74.73</td><td>43.00</td><td>27.90</td><td>33.90</td><td>80.40</td><td>88.80</td><td>84.40</td><td>59.15</td></tr><tr><td>MNB-BoW</td><td>72.48</td><td>42.80</td><td>55.80</td><td>48.50</td><td>85.30</td><td>77.50</td><td>81.20</td><td>64.85</td></tr><tr><td>MNB-BoW + lex</td><td>75.33</td><td>47.40</td><td>60.40</td><td>53.10</td><td>87.00</td><td>79.80</td><td>83.30</td><td>68.20</td></tr><tr><td>ENS(LR + RF + MNB)-BoW</td><td>75.19</td><td>44.70</td><td>29.90</td><td>35.80</td><td>80.80</td><td>88.80</td><td>84.60</td><td>60.20</td></tr><tr><td>ENS(LR + RF + SVM + MNB)-BoW + lex</td><td>76.99</td><td>50.50</td><td>35.70</td><td>41.80</td><td>82.20</td><td>89.40</td><td>85.70</td><td>63.75</td></tr><tr><td>Best result from the literature [42]</td><td>71.10</td><td>53.80</td><td>47.20</td><td>50.30</td><td>84.50</td><td>87.60</td><td>86.00</td><td>68.15</td></tr></table>

algorithms used. Note that the ensemble obtained from BoW and lexicons has provided the best results. More importantly and in contrast to the other approaches, very good classi<sup>fi</sup>cation accuracy rates were obtained even for small sample sizes. The best accuracy rate reported in the literature for the complete dataset (formed by 1,600,000 tweets)

is 87.20%, whereas our ensemble trained with only 0.03% of the data obtained an accuracy of 81.06% in the test set available in [35].

Finally, it is worth comparing our results to those obtained in [19]. However, the datasets used in that study are not publicly available, except for Sanders. For this data, we carried out experiments considering the neutral class<sup>7</sup> and 10-fold cross validation. We assume that a neutral lexicon exists when neither positive nor negative lexicon exist in the opinion lexicon (Hu and Liu [9]). We obtained an accuracy rate of 76.25%, while Hassan et al. [19] obtained 76.30%. Our results are very good in comparison to theirs, since they used more linguistic resources and classi<sup>fi</sup>er models, and also expanded the number of patterns by including instances from different sub-domains.

Table 4  
Cross comparison results using feature hashing (FH) — best results in bold.

<table><tr><td rowspan="2">Method</td><td rowspan="2">Acc. (%)</td><td colspan="3">Positive class</td><td colspan="3">Negative class</td><td>Avg.</td></tr><tr><td>Precision (%)</td><td>Recall (%)</td><td>F1 (%)</td><td>Precision (%)</td><td>Recall (%)</td><td>F1 (%)</td><td>F1 (%)</td></tr><tr><td colspan="9">OMD dataset</td></tr><tr><td>SVM-FH</td><td>51.10</td><td>37.90</td><td>49.20</td><td>42.80</td><td>63.40</td><td>52.30</td><td>57.30</td><td>50.05</td></tr><tr><td>SVM-FH + lex</td><td>62.85</td><td>50.10</td><td>57.60</td><td>53.60</td><td>72.40</td><td>66.00</td><td>69.00</td><td>61.30</td></tr><tr><td>RF-FH</td><td>61.39</td><td>47.10</td><td>29.60</td><td>36.30</td><td>65.80</td><td>80.30</td><td>72.30</td><td>54.30</td></tr><tr><td>RF-FH + lex</td><td>67.37</td><td>58.50</td><td>42.50</td><td>49.30</td><td>70.60</td><td>82.10</td><td>75.90</td><td>62.60</td></tr><tr><td>LR-FH</td><td>63.28</td><td>61.90</td><td>3.70</td><td>6.90</td><td>63.30</td><td>98.70</td><td>77.10</td><td>42.00</td></tr><tr><td>LR-FH + lex</td><td>70.57</td><td>67.00</td><td>41.30</td><td>51.10</td><td>71.60</td><td>88.00</td><td>78.90</td><td>65.00</td></tr><tr><td>MNB-FH</td><td>62.54</td><td>47.20</td><td>4.80</td><td>8.70</td><td>63.10</td><td>96.80</td><td>76.40</td><td>42.55</td></tr><tr><td>MNB-FH + lex</td><td>70.41</td><td>64.40</td><td>45.90</td><td>53.60</td><td>72.60</td><td>84.90</td><td>78.30</td><td>65.95</td></tr><tr><td>ENS(LR + RF + MNB)-FH</td><td>64.59</td><td>39.80</td><td>32.00</td><td>35.50</td><td>63.80</td><td>71.30</td><td>67.40</td><td>51.45</td></tr><tr><td>ENS(LR + RF + MNB)-FH + lex</td><td>70.62</td><td>57.70</td><td>53.70</td><td>55.60</td><td>73.60</td><td>76.70</td><td>75.10</td><td>65.35</td></tr><tr><td colspan="9">Strict OMD dataset</td></tr><tr><td>SVM-FH</td><td>51.31</td><td>39.80</td><td>55.30</td><td>46.30</td><td>64.20</td><td>48.90</td><td>55.50</td><td>50.90</td></tr><tr><td>SVM-FH + lex</td><td>62.99</td><td>51.30</td><td>47.00</td><td>49.00</td><td>69.20</td><td>72.80</td><td>71.00</td><td>60.00</td></tr><tr><td>RF-FH</td><td>61.36</td><td>48.50</td><td>31.70</td><td>38.30</td><td>65.60</td><td>79.40</td><td>71.90</td><td>55.10</td></tr><tr><td>RF-FH + lex</td><td>72.60</td><td>69.00</td><td>50.10</td><td>58.10</td><td>73.90</td><td>86.30</td><td>79.60</td><td>68.85</td></tr><tr><td>LR-FH</td><td>65.29</td><td>65.30</td><td>17.90</td><td>28.10</td><td>65.30</td><td>94.20</td><td>77.10</td><td>52.60</td></tr><tr><td>LR-FH + lex</td><td>73.03</td><td>68.10</td><td>54.20</td><td>60.40</td><td>75.20</td><td>84.50</td><td>79.60</td><td>70.00</td></tr><tr><td>MNB-FH</td><td>60.70</td><td>36.20</td><td>4.90</td><td>8.60</td><td>62.00</td><td>94.70</td><td>75.00</td><td>41.80</td></tr><tr><td>MNB-FH + lex</td><td>71.39</td><td>66.20</td><td>50.10</td><td>57.00</td><td>73.50</td><td>84.40</td><td>78.60</td><td>67.80</td></tr><tr><td>ENS(LR + RF + MNB)-FH</td><td>65.17</td><td>59.60</td><td>23.30</td><td>33.50</td><td>65.90</td><td>90.30</td><td>76.20</td><td>54.85</td></tr><tr><td>ENS(LR + RF + MNB)-FH + lex</td><td>74.56</td><td>70.20</td><td>57.10</td><td>63.00</td><td>76.50</td><td>85.20</td><td>80.60</td><td>71.80</td></tr><tr><td colspan="9">Sanders - Twitter Sentiment Corpus</td></tr><tr><td>SVM-FH</td><td>49.75</td><td>46.30</td><td>49.80</td><td>48.00</td><td>53.20</td><td>49.70</td><td>51.40</td><td>49.70</td></tr><tr><td>SVM-FH + lex</td><td>75.00</td><td>74.10</td><td>71.20</td><td>72.60</td><td>75.70</td><td>78.30</td><td>77.00</td><td>74.80</td></tr><tr><td>RF-FH</td><td>55.64</td><td>52.10</td><td>59.80</td><td>55.70</td><td>59.80</td><td>52.00</td><td>55.60</td><td>55.65</td></tr><tr><td>RF-FH + lex</td><td>71.63</td><td>68.00</td><td>73.90</td><td>70.80</td><td>75.40</td><td>69.70</td><td>72.40</td><td>71.60</td></tr><tr><td>LR-FH</td><td>56.94</td><td>54.70</td><td>43.50</td><td>48.50</td><td>58.20</td><td>68.70</td><td>63.00</td><td>55.75</td></tr><tr><td>LR-FH + lex</td><td>75.98</td><td>74.40</td><td>73.90</td><td>74.10</td><td>77.40</td><td>77.80</td><td>77.60</td><td>75.85</td></tr><tr><td>MNB-FH</td><td>54.25</td><td>51.00</td><td>45.30</td><td>48.00</td><td>56.50</td><td>62.10</td><td>59.20</td><td>53.60</td></tr><tr><td>MNB-FH + lex</td><td>75.08</td><td>73.30</td><td>73.20</td><td>73.20</td><td>76.60</td><td>76.80</td><td>76.70</td><td>74.95</td></tr><tr><td>ENS(LR + RF + MNB)-FH</td><td>57.84</td><td>53.70</td><td>49.30</td><td>51.40</td><td>58.80</td><td>63.00</td><td>60.80</td><td>56.10</td></tr><tr><td>ENS(LR + RF + MNB)-FH + lex</td><td>76.63</td><td>75.40</td><td>73.20</td><td>74.30</td><td>77.20</td><td>79.20</td><td>78.20</td><td>76.25</td></tr><tr><td colspan="9">Best sampling with Stanford dataset - sampling with 3000 tweets</td></tr><tr><td>SVM-FH</td><td>47.63</td><td>47.50</td><td>31.90</td><td>38.20</td><td>47.70</td><td>63.80</td><td>54.60</td><td>46.40</td></tr><tr><td>SVM-FH + lex</td><td>54.32</td><td>54.00</td><td>66.50</td><td>59.60</td><td>54.80</td><td>41.80</td><td>47.40</td><td>53.50</td></tr><tr><td>RF-FH</td><td>47.63</td><td>52.50</td><td>58.80</td><td>55.40</td><td>51.60</td><td>45.20</td><td>48.20</td><td>51.80</td></tr><tr><td>RF-FH + lex</td><td>70.47</td><td>70.40</td><td>72.00</td><td>71.20</td><td>70.50</td><td>68.90</td><td>69.70</td><td>70.45</td></tr><tr><td>LR-FH</td><td>55.71</td><td>56.20</td><td>57.10</td><td>56.70</td><td>55.20</td><td>54.20</td><td>54.70</td><td>55.70</td></tr><tr><td>LR-FH + lex</td><td>78.55</td><td>76.60</td><td>83.00</td><td>79.70</td><td>80.90</td><td>74.00</td><td>77.30</td><td>78.50</td></tr><tr><td>MNB-FH</td><td>54.32</td><td>54.50</td><td>59.30</td><td>56.80</td><td>54.00</td><td>49.20</td><td>51.50</td><td>54.15</td></tr><tr><td>MNB-FH + lex</td><td>78.27</td><td>77.40</td><td>80.80</td><td>79.00</td><td>79.30</td><td>75.70</td><td>77.50</td><td>78.25</td></tr><tr><td>ENS(LR + RF + MNB)-FH</td><td>57.38</td><td>55.30</td><td>54.40</td><td>54.80</td><td>53.90</td><td>54.80</td><td>54.30</td><td>54.55</td></tr><tr><td>ENS(LR + RF + MNB)-FH + lex</td><td>79.11</td><td>76.90</td><td>78.60</td><td>77.70</td><td>77.50</td><td>75.70</td><td>76.60</td><td>77.15</td></tr><tr><td colspan="9">HCR dataset</td></tr><tr><td>SVM-FH</td><td>67.22</td><td>28.40</td><td>27.30</td><td>27.80</td><td>78.30</td><td>79.30</td><td>78.80</td><td>53.30</td></tr><tr><td>SVM-FH + lex</td><td>69.92</td><td>20.50</td><td>10.40</td><td>13.80</td><td>76.50</td><td>87.90</td><td>81.80</td><td>47.80</td></tr><tr><td>RF-FH</td><td>63.16</td><td>25.10</td><td>29.90</td><td>27.30</td><td>77.60</td><td>73.20</td><td>75.30</td><td>51.30</td></tr><tr><td>RF-FH + lex</td><td>72.48</td><td>38.70</td><td>45.50</td><td>41.80</td><td>82.60</td><td>78.30</td><td>80.40</td><td>61.10</td></tr><tr><td>LR-FH</td><td>67.52</td><td>26.90</td><td>23.40</td><td>25.00</td><td>77.80</td><td>80.80</td><td>79.30</td><td>52.15</td></tr><tr><td>LR-FH + lex</td><td>77.6</td><td>50</td><td>17.50</td><td>26.00</td><td>79.20</td><td>94.70</td><td>86.30</td><td>56.15</td></tr><tr><td>MNB-FH</td><td>73.83</td><td>34.80</td><td>10.40</td><td>16.00</td><td>77.70</td><td>94.10</td><td>85.10</td><td>50.55</td></tr><tr><td>MNB-FH + lex</td><td>75.34</td><td>46.50</td><td>26.00</td><td>33.30</td><td>80.30</td><td>91.00</td><td>85.30</td><td>59.30</td></tr><tr><td>ENB(LR + RF + MNB)-FH</td><td>76.09</td><td>27.50</td><td>7.10</td><td>11.30</td><td>77.10</td><td>94.30</td><td>84.90</td><td>48.10</td></tr><tr><td>ENB(LR + RF + MNB)-FH + lex</td><td>78.35</td><td>52.90</td><td>29.90</td><td>38.20</td><td>81.30</td><td>92.00</td><td>86.30</td><td>62.20</td></tr></table>

Table 5  
Number of features from bag-of-words and from feature hashing.

<table><tr><td>Dataset</td><td># of features from BoW</td><td># of features from FH</td></tr><tr><td>OMD dataset</td><td>1352</td><td>13</td></tr><tr><td>Strict OMD dataset</td><td>759</td><td>10</td></tr><tr><td>Sanders – Twitter Sentiment Corpus</td><td>1203</td><td>23</td></tr><tr><td>Stanford dataset</td><td>2137</td><td>21</td></tr><tr><td>HCR dataset</td><td>1432</td><td>10</td></tr></table>

<sup>7</sup> Hassan et al. [19] use other datasets, however they are not available.

N.F.F. da Silva et al. / Decision Support Systems xxx (2014) xxx–xxx

![](/api/attachments/NFUJCUW3/fulltext/images/eaed0de35e888511f8eef53c085094d3dd675f78c43eeac8c0f24b6570dfc1b8.jpg)  
Fig. 6. Accuracies from samplings of different sizes — Stanford dataset.

## 5. Concluding remarks

The use of classi<sup>fi</sup>er ensembles for tweet sentiment analysis has been underexplored in the literature. We have demonstrated that classi<sup>fi</sup>er ensembles formed by diversi<sup>fi</sup>ed components — specially if these come from different information sources, such as textual data, emoticons, and lexicons — can provide state-of-the-art results for this particular domain. We also compared promising strategies for the representation of tweets (i.e., bag-of-words and feature hashing) and showed their advantages and drawbacks. Feature hashing has shown to be a good choice in the scenario of tweet sentiment analysis where computational effort is of paramount importance. However, when the focus is on accuracy, the best choice is bag-of-words. Although our results have been obtained for data from Twitter, one of the most popular social media platforms, we believe that our study is also relevant for other social media analyses.

As future work we are going to study neutral tweets [19], where datasets are enriched with analogue domain datasets, and with different features. As it is widely known, diversity is a key point for the successful application of ensembles. Therefore, more effort will be devoted towards this direction.

## Acknowledgments

The authors would like to acknowledge Research Agencies CAPES (DS-7253238/D), FAPESP (2013/07787-6 and 2013/07375-0), and CNPq (303348/2013-5) for their <sup>fi</sup>nancial support. They are also grateful to Marko Grobelnik for pointing out some related work on tweet analysis.

## References

[1] A. Ritter, S. Clark, Mausam, O. Etzioni, Named entity recognition in tweets: an experimental study, Proceedings of the Conference on Empirical Methods in Natural Language Processing, EMNLP'11, Association for Computational Linguistics, Stroudsburg, PA, USA, 2011, pp. 1524–1534.

[2] B.J. Jansen, M. Zhang, K. Sobel, A. Chowdury, Twitter power: Tweets as electronic word of mouth, Journal of the American Society for Information Science and Technologv 60 (11) (2009) 2169–2188

[3] J.-M. Xu, K.-S. Jun, X. Zhu, A. Bellmore, Learning from bullying traces in social media, HLT-NAACL. The Association for Computational Linguistics 2012, 656–666

[4] M. Cheong, V.C. Lee, A microblogging-based approach to terrorism informatics: exploration and chronicling civilian sentiment and response to terrorism events via twitter, Information Systems Frontiers 13 (1) (2011) 45–59.

[5] P.H.C. Guerra, A. Veloso, W. Meira, V. Almeida Jr, From bias to opinion: a transferlearning approach to real-time sentiment analysis, Proceedings of the 17th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, San Diego, CA, 2011.

[6] N.A. Diakopoulos, D.A. Shamma, Characterizing debate performance via aggregated twitter sentiment. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, CHI'10, ACM, New York, NY, USA, 2010, pp. 1195–1198.

[7]. P.D. Turney, Thumbs up or thumbs down?: semantic orientation applied to unsupervised classification of reviews Proceedings of the 40th Annual Meeting on

Association for Computational Linguistics, ACL 02, Association for Computational Linguistics, Stroudsburg, PA, USA, 2002, pp. 417–424.

[8] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up? Sentiment classi<sup>fi</sup>cation using machine learning techniques, Proceedings of EMNLP, 2002, pp. 79–86.

[9] M. Hu, B. Liu, Mining and summarizing customer reviews, Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD'04, ACM, New York, NY, USA, 2004, pp. 168–177.

[10] B. He, C. Macdonald, J. He, I. Ounis, An effective statistical approach to blog post opinion retrieval, Proceedings of the 17th ACM Conference on Information and Knowledge Management, CIKM'08, ACM, New York, NY, USA, 2008, pp. 1063–1072.

[11] P. Melville, W. Gryc, R.D. Lawrence, Sentiment analysis of blogs by combining lexical knowledge with text classi<sup>fi</sup>cation, Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD'09, , ACM, New York, NY, USA, 2009, 1275–1284

[12] A. Balahur, R. Steinberger, M. Kabadjov, V. Zavarella, E. van der Goot, M. Halkia, B. Pouliquen, J. Belyaeva, Sentiment analysis in the news, in: N. C. C. Chair), K. Choukri, B. Maegaard, J. Mariani, J. Odijk, S. Piperidis, M. Rosner, D. Tapias (Eds.), Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC'10), European Language Resources Association (ELRA), Valletta, Malta, 2010.

[13] P. Ekman, Emotion in the Human Face, vol. 2Cambridge University Press, 1982.

[14] B. Liu, Sentiment analysis and opinion mining, Synthesis Lectures on Human Language Technologies. . Morgan & Claypool Publishers, 2012

[15] B. Liu, Web data mining: exploring hyperlinks, contents, and usage data, Data-Centric Systems and Applications, , Springer-Verlag New York, Inc., Secaucus, NJ, USA, 2006.

[16] B. Liu, Sentiment Analysis and Subjectivity, Taylor and Francis Group, Boca, 2010.

[17] A. Agarwal, P. Bhattacharyya, Sentiment analysis: a new approach for effective use of linguistic knowledge and exploiting similarities in a set of documents to be classi<sup>fi</sup>ed, Proceedings of the International Conference on Natural Language Processing (ICON), 2005.

[18] S.S. Standi<sup>fi</sup>rd, Reputation and e-commerce: ebay auctions and the asymmetrical impact of positive and negative ratings, Journal of Management 27 (3) (2001) 279–295.

[19] A. Hassan, A. Abbasi, D. Zeng, Twitter Sentiment Analysis: A Bootstrap Ensemble Framework SocialCom JEEE 2013. 357-364

[20] K.Q. Weinberger, A. Dasgupta, J. Langford, A.J. Smola, J. Attenberg, Feature hashing for large scale multitask learning, in: A.P. Danyluk, L. Bottou, M.L. Littman (Eds.), ICML, Vol. 382 of ACM International Conference Proceeding Series, ACM, 2009, p. 140.

[21] L.I. Kuncheva, Combining Pattern Classi<sup>fi</sup>ers: Methods and Algorithms, Wiley-Interscience. 2004

[22] Z. Zhou, Ensemble methods: foundations and algorithms, Chapman & Hall/CRC Data Mining and Knowledge Discovery Series, , Taylor & Francis, 2012.

[23] J.A. Benediktsson, J. Kittler, F. Roli, Multiple classi<sup>fi</sup>er systems, Vol. 5519 of Lecture Notes in Computer Science, , Springer, Reykjavik, Iceland, 2009.

[24] K. Tumer, J. Ghosh, Analysis of decision boundaries in linearly combined neural classifiers Pattern Recognition 29 (1996) 341–348

[25] G. Wang, J. Sun, J. Ma, K. Xu, J. Gu, Sentiment classi<sup>fi</sup>cation: the contribution of en semble learning, Decision Support Systems (0) (2013).

[26] A. Abbasi, H. Chen, S. Thoms, T. Fu, Affect analysis of web forums and blogs using correlation ensembles IEEE Transactions on Knowledge and Data Engineering 20 (9) (2008) 1168–1180.

[27] Heterogeneous ensemble learning for Chinese sentiment classi<sup>fi</sup>cation, Journal of Information and Computational Science 9 (15) (2012) 4551–4558.

[28] B. Lu, B. Tsou, Combining a large sentiment lexicon and machine learning for subjectivity classification, 2010 International Conference on Machine Learning and Cybernetics (ICMLC), vol. 6, 2010, pp. 3311–3316.

[29] Y. Su, Y. Zhang, D. Ji, Y. Wang, H. Wu, Ensemble learning for sentiment classi<sup>fi</sup>cation, in: D. Ji, G. Xiao (Eds.), Chinese Lexical Semantics, Vol. 7717 of Lecture Notes in Computer ScienceSpringer, Berlin Heidelberg, 2013, pp. 84–93.

[30] M. Whitehead, L. Yaeger, Sentiment mining using ensemble classi<sup>fi</sup>cation models, in: T. Sobh (Ed.), Innovations and Advances in Computer Sciences and Engineering, Springer, Netherlands, 2010, pp. 509–514.

[31] A. Abbasi, H. Chen, S. Thoms, T. Fu, Affect analysis of web forums and blogs using correlation ensembles, IEEE Transactions on Knowledge and Data Engineering 20 (9) (2008) 1168–1180.

[32] J. Lin, A. Kolcz, Large-scale machine learning at twitter, Proceedings of the 2012 ACM SIGMOD International Conference on Management of Data, SIGMOD'12, ACM, New York, NY, USA, 2012, pp. 793–804.

[33] S. Clark, R. Wicentwoski, Swatcs: combining simple classi<sup>fi</sup>ers with estimated accuracy, Second Joint Conference on Lexical and Computational Semantics (\*SEM), Proceedings of the Seventh International Workshop on Semantic Evaluation (SemEval 2013), vol. 2, Association for Computational Linguistics, Atlanta, Georgia, USA, 2013, pp. 425–429.

[34] C. Rodriguez Penagos, J. Atserias, J. Codina-Filba, D. Garcıa-Narbona, J. Grivolla, P. Lambert, R. Saur, Fbm: combining lexicon-based ml and heuristics for social media polarities, Proceedings of SemEval-2013 — International Workshop on Semantic Evaluation Co-located with \*Sem and NAACL, Atlanta, Georgia, 2013, (url date at 2013-10-10).

[35] A. Go, R. Bhayani, L. Huang, Twitter sentiment classi<sup>fi</sup>cation using distant supervision, Unpublished Manuscript, Stanford University 1–6

[36] D. Davidov, O. Tsur, A. Rappoport, Enhanced sentiment learning using twitter hashtags and smileys, Proceedings of the 23rd International Conference on Computational Linguistics: Posters, COLING'10, Association for Computational Linguistics, Stroudsburg, PA, USA, 2010, pp. 241–249.

[37] X. Hu, L. Tang, J. Tang, H. Liu, Exploiting social relations for sentiment analysis in microblogging, Proceedings of the Sixth ACM International Conference on Web Search and Data Mining, 2013.

[38] A. Agarwal, B. Xie, I. Vovsha, O. Rambow, R. Passonneau, Sentiment analysis of twitter data, Proceedings of the Workshop on Languages in Social Media, LSM'11, Association for Computational Linguistics, Stroudsburg, PA, USA, 2011, pp. 30–38.

[39] J. Read, Using emoticons to reduce dependency in machine learning techniques for sentiment classi<sup>fi</sup>cation, Proceedings of the ACL Student Research Workshop, ACLstudent'05, Association for Computational Linguistics, Stroudsburg, PA, USA, 2005, pp. 43–48.

[40] L. Zhang, R. Ghosh, M. Dekhil, M. Hsu, B. Liu, Combining lexicon-based and learningbased methods for twitter sentiment analysis, HP Laboratories, 2011. (technical Report).

[41l. S. Mohammad S. Kiritchenko. X. Zhu Nrc-Canada: building the state-of-the-art in sentiment analysis of tweets, Proceedings of the Seventh International Workshop on Semantic Evaluation Exercises (SemEval-2013), Atlanta, Georgia, USA, 2013.

[42] H. Saif, Y. He, H. Alani, Semantic sentiment analysis of twitter, Proceedings of the 11th International Conference on The Semantic Web — Volume Part I, ISWC'12, Springer-Verlag, Berlin, Heidelberg, 2012, pp. 508–524.

[43] G.A. Miller, Wordnet: a lexical database for english, Communications of the ACM 38 (11) (1995) 39–41.

[44] S. Baccianella, A. Esuli, F. Sebastiani, Sentiwordnet 3.0: An enhanced lexical resource for sentiment analysis and opinion mining, in: N. C. C. Chair), K. Choukri, B. Maegaard, J. Mariani, J. Odijk, S. Piperidis, M. Rosner, D. Tapias (Eds.), Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC 10), European Language Resources Association (ELRA), Valletta, Malta, 2010.

[45] B. O'Connor, R. Balasubramanyan, B.R. Routledge, N.A. Smith, From tweets to polls: linking text sentiment to public opinion time series. Proceedings of the International AAAI Conference on Weblogs and Social Media, 2010.

[46] X. Ding, B. Liu, P.S. Yu, A holistic lexicon-based approach to opinion mining, Proceedings of First ACM International Conference on Web Search and Data Mining (WSDM-2008), 2008.

[47] M. Speriosu, N. Sudan, S. Upadhyay, J. Baldridge, Twitter polarity classi<sup>fi</sup>cation with label propagation over lexical links and the follower graph, Proceedings of the First Workshop on Unsupervised Learning in NLP, EMNLP'11, Association for Computational Linguistics, Stroudsburg, PA, USA, 2011, pp. 53–63.

[48] T. Wilson, J. Wiebe, P. Hoffmann, Recognizing contextual polarity in phrase-level sentiment analysis, Proceedings of the Conference on Human Language Technology and Empirical Methods in Natural Language Processing, HLT'05, Association for Computational Linguistics, Stroudsburg, PA, USA, 2005, pp. 347–354.

[49] D.A. Shamma, L. Kennedy, E.F. Churchill, Tweet the debates: understanding community annotation of uncollected sources, In WSM?09: Proceedings of the International Workshop on Workshop on Social, 2009.

[50] S.M. Mohammad, P.D. Turney, Emotions evoked by common words and phrases: using mechanical turk to create an emotion lexicon, Proceedings of the NAACL HLT 2010 Workshop on Computational Approaches to Analysis and Generation of Emotion in Text, CAAGET'10, Association for Computational Linguistics, Stroudsburg, PA, USA, 2010, pp. 26–34

[51] P. Nakov, S. Rosenthal, Z. Kozareva, V. Stoyanov, A. Ritter, T. Wilson, Semeval-2013 task 2: sentiment analysis in twitter, Second Joint Conference on Lexical and Computational Semantics (\*SEM), Proceedings of the Seventh International Workshop on Semantic Evaluation (SemEval 2013), vol. 2, Association for Computational Linguistics, Atlanta, Georgia, USA, 2013, pp. 312–320.

[52] Q. Shi, J. Petterson, G. Dror, J. Langford, A. Smola, S. Vishwanathan, Hash kernels for structured data, Journal of Machine Learning Research 10 (2009) 2615–2637.

[53] K. Ganchev, M. Dredze, Small statistical models by random feature mixing, Proceedings of the ACL-2008 Workshop on Mobile Language Processing, Association for Computational Linguistics, 2008.

[54] G. Forman, E. Kirshenbaum, Extremely fast text feature extraction for classi<sup>fi</sup>cation and indexing, CIKM'08: Proceeding of the 17th ACM Conference on Information and Knowledge Management, , ACM, New York, NY, USA, 2008. 1221–1230.

[55] A. Asiaee, T.M. Tepper, A. Banerjee, G. Sapiro, If you are happy and you know it… tweet, Proceedings of the 21st ACM International Conference on Information and Knowledge Management, CIKM'12, ACM, New York, NY, USA, 2012, pp. 1602–1606.

[56] T.G. Dietterich, Ensemble methods in machine learning, Proceedings of the First International Workshop on Multiple Classi<sup>fi</sup>er Systems, MCS'00, Springer-Verlag, London, UK, 2000, pp. 1–15.

[57] G. Fumera, F. Roli, A theoretical and experimental analysis of linear combiners for multiple classi<sup>fi</sup>er systems, IEEE Transactions on Pattern Analysis and Machine In telligence 27 (6) (2005) 942–956.

[58] K. Tumer, J. Ghosh, Error correlation and error reduction in ensemble classi<sup>fi</sup>ers, Connection Science 8 (3–4) (1996) 385–403.

[59] A. Krogh, J. Vedelsby, Neural network ensembles, cross validation, and active learning, Advances in Neural Information Processing Systems, , MIT Press, 1995. 231–238.

[61] R. Polikar, Ensemble learning, Scholarpedia 4 (1) (2009) 2776.

[60] L.I. Kuncheva, C.J. Whitaker, Measures of diversity in classi<sup>fi</sup>er ensembles and their relationship with the ensemble accuracy, Machine Learning 51 (2) (2003) 181–207.

[62] K. Tumer, J. Ghosh, Bayes error rate estimation using classi<sup>fi</sup>er ensembles, International Journal of Smart Engineering System Design 5 (2) (2003) 95–110.

[63] G. Brown, J. Wyatt, R. Harris, X. Yao, Diversity creation methods: a survey and categorisation, Information Fusion 6 (2005) 5–20.

[64] J. Langford, A. Strehl, L. Li, Vowpal Wabbit online learning project, http://mloss.org software/view/53/ 2007.

[65] C. Caragea, A. Silvescu, P. Mitra, Protein Sequence Classi<sup>fi</sup>cation Using Feature Hashing, in: F.-X. Wu, M.J. Zaki, S. Morishita, Y. Pan, S. Wong, A. Christianson, X. Hu (Eds.), BIBM, IEEE, 2011, pp. 538–543.

[66] H. Saif, M. Fernandez, Y. He, H. Alani, Evaluation datasets for twitter sentiment analysis: a survey and a new dataset, the STS-Gold, in: C. Battaglino, C. Bosco, E. Cambria, R. Damiano, V. Patti, P. Rosso (Eds.), ESSEM@AI\*IA, Vol. 1096 of CEUR Workshop Proceedings, CEUR-WS.org, 2013, pp. 9–21.

[67] D. Ziegelmaver, R. Schrader Sentiment polarity classification using statistical data compression models, in: I. Vreeken, C. Ling, M.I. Zaki, A. Siebes. IX. Yu. B. Goethals. G.I. Webb, X. Wu (Eds.), ICDM Workshops, IEEE Computer Society, 2012, pp. 731-738.

[68] A. Bakliwal, P. Arora, S. Madhappan, N. Kapre, M. Singh, V. Varma, Mining sentiments from tweets, Proceedings of the 3rd Workshop in Computational Approaches to Subjectivity and Sentiment Analysis, Association for Computational Linguistics, Jeju, Korea, 2012, pp. 11–18, (URL http://www.aclweb.org/anthology-new/W/ W12/W12-3704.bib ).

[69] F. Bravo-Marquez, M. Mendoza, B. Poblete, Combining strengths, emotions and polarities for boosting twitter sentiment analysis, Proceedings of the Second International Workshop on Issues of Sentiment Discovery and Opinion Mining, WISDOM'13, ACM, New York, NY, USA, 2013, pp. 2:1–2:9.

[70] C.-C. Chang, C.-J. Lin, Libsvm: a library for support vector machines, ACM Transactions on Intelligent Systems and Technology 2 (3) (2011) 27:1–27:27.
