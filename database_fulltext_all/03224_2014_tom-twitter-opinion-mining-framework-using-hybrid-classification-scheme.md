---
otero_id: 3224
otero_key: "FG55HSBR"
title: "TOM: Twitter opinion mining framework using hybrid classification scheme"
authors: "Farhan Hassan Khan; Saba Bashir; Usman Qamar"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# TOM: Twitter opinion mining framework using hybrid classi<sup>fi</sup>cation scheme

Farhan Hassan Khan, Saba Bashir ⁎, Usman Qamar

Computer Engineering Department, College of Electrical and Mechanical Engineering, National University of Sciences and Technology (NUST), Islamabad, Pakistan

## a r t i c l e i n f o

Article history: Received 20 February 2013 Received in revised form 30 July 2013 Accepted 11 September 2013 Available online 21 September 2013

Keywords: Twitter Sentiment analysis Classification SentiWordNet Social network analysis Data sparsity

## a b s t r a c t

Twitter has become one of the most popular micro-blogging platform recently. Millions of users can share their thoughts and opinions about different aspects and events on the micro-blogging platform. Therefore, Twitter is considered as a rich source of information for decision making and sentiment analysis. Sentiment analysis refers to a classi<sup>fi</sup>cation problem where the main focus is to predict the polarity of words and then classify them into positive and negative feelings with the aim of identifying attitude and opinions that are expressed in any form or language. Sentiment analysis over Twitter offers organisations a fast and effective way to monitor the publics' feelings towards their brand, business, directors, etc. A wide range of features and methods for training sentiment classi<sup>fi</sup>ers for Twitter datasets have been researched in recent years with varying results. The primary issues in previous techniques are classi<sup>fi</sup>cation accuracy, data sparsity and sarcasm, as they incorrectly classify most of the tweets with a very high percentage of tweets incorrectly classi<sup>fi</sup>ed as neutral. This research paper focuses on these problems and presents an algorithm for twitter feeds classi<sup>fi</sup>cation based on a hybrid approach. The proposed method includes various pre-processing steps before feeding the text to the classi<sup>fi</sup>er. Experimental results show that the proposed technique overcomes the previous limitations and achieves higher accuracy when compared to similar techniques.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The emergence of social media has given web users a venue for expressing and sharing their thoughts and opinions on different topics and events. Twitter, with nearly 600 million users and over 250 million messages per day, has quickly become a gold mine for organisations to monitor their reputation and brands by extracting and analysing the sentiment of the Tweets posted by the public about them, their markets, and competitors.

Sentiment analysis over Twitter data and other similar micro-blogs faces several new challenges due to the typical short length and irregular structure of such content. The following are some challenges faced in sentiment analysis of Twitter feeds.

• Named Entity Recognition (NER) — NER is the method of extracting entities such as people, organisation and locations from twitter corpus.

• Anaphora Resolution — The process of resolving the problem of what a pronoun or noun phrase refers to. “We had a lavish dinner and went for a walk, it was awful”. What does “It” refer to?

• Parsing — The process of identifying the subject and object of the sentence. The verb and adjective are referring to what?

• Sarcasm — What does a verb actually stand for? Does ‘bad’ mean bad or good?

• Sparsity — Insuf<sup>fi</sup>cient data or very few useful labels in the training set.

• Twitter abbreviations, poor spellings, poor punctuation, poor grammar, incomplete sentences.

• The accuracy of tweets classi<sup>fi</sup>cation as compared to human judgments.

Fig. 1 presents a generic framework of sentiment analysis where a sentiment engine receives feedback (data) from different channels and then a unique algorithm categorizes (positive/negative) them by assigning scores. The results can be used to draw various types of graphs which are presented in the dashboard. These results can be used to <sup>fi</sup>nd out the overall feelings towards a particular person, product or service.

This research paper presents a technique for text mining of Twitter feeds in real time and sentiment analysis using three-way classi<sup>fi</sup>cation by investigating the sentiment intensity. The main focus is on improving the accuracy and solving the data sparsity issue in tweet classi<sup>fi</sup>cation, effectively reducing the number of tweets classi<sup>fi</sup>ed as neutral.

## 1.1. Motivation

Micro-blogging website Twitter has evolved to become a source of rich and varied information. This is due to nature of micro-blogs on which people post real time messages about their opinions on a variety of topics, discuss current issues, complain, and express positive sentiment for products they use in daily life. In fact, companies manufacturing such products have started to poll these tweets to get a sense of general sentiment for their product. Many times these companies study user reactions and reply to users on twitter. However, the sheer vastness of data makes it very dif<sup>fi</sup>cult to analyse and grasp this data. Therefore, it is necessary to automate the process of analysing the twitter's data. In order to complete this task, there is an immense need to automatically classify the twitter's tweets as positive, negative or neutral in real time.

![](/api/attachments/FG55HSBR/fulltext/images/4262ad5464878bfb02fc4b144b4e15aa24eb1abda1b60808cf1425d70f00fea3.jpg)  
Fig. 1. Generic sentiment analysis framework.

The main contributions of this paper can be summarised as follows:

• Introduces and implements a hybrid approach for determining the sentiment of each tweet

• Demonstrates the value of pre-possessing data using detection and analysis of slangs/abbreviations, lemmatization, correction and stop words removal

• Tests the accuracy of sentiment identi<sup>fi</sup>cation on 6 Twitter datasets, and produces an average harmonic mean of 83.3% and accuracy of 85.7%, with 85.3% precision and 82.2% recall

• Resolves the data sparsity issue using domain independent techniques.

• Comparison with other techniques to prove the effectiveness of the proposed hybrid approach.

The structure of the paper is described as follows. Section 2 outlines the recent related work. Section 3 introduces the proposed technique while Section 4 gives an overview of the results. Finally Section 5 summarises the work which has been done.

## 2. Literature review

There are multiple text mining techniques used to mine the twitter feeds.

Cui, A. et al. [1] showed that sentiment analysis of tweets is a challenging task due to multilingual and informal messages. The paper tackles this problem by analysis of emotion tokens. Emotion is the mood of a person depicted from the words in the tweet. Emotion can be sad, happy, angry, etc. The proposed approach has two steps. First, emotion tokens are extracted from the message. Second, graph propagation algorithm plots the tokens at different polarities. Finally, sentiment analysis algorithm analyses and classi<sup>fi</sup>es these emotion tokens. The results show that emotion tokens are a great approach towards semantic analysis of any natural language where lexicons are built independent of different time domains. The technical issues in the proposed approach are: less accuracy of sentiment analysis, dif<sup>fi</sup>culty in tackling sentiment analysis of Twitter stream for longer time and weak emotion representation.

Bifet, A. and Frank, E. [2] proposed a data mining technique used for sentiment knowledge in twitter data streams. The proposed algorithm focuses on classi<sup>fi</sup>cation of data streams and performs sentiment analysis in real time. The evaluation of results is veri<sup>fi</sup>ed using a sliding window kappa statistics that works for constantly changing data streams. Only a small number of tweets (177 negative and 182 positive) were used to test the accuracy. This is a very small number of tweets to make any judgment about the proposed technique. Only tweets containing an emoticon were considered; which is also a very small portion of overall tweets. The paper uses a balanced dataset which is not a sample of real-time Twitter stream which is normally unbalanced.

Bifet, A., Holmes, ${ \sf G } _ { \cdot , \cdot }$ and Pfahringer, B. [3] discussed the handling of tweets in real-time. The research paper introduced a system, MOA-TweetReader, which processes the tweets in real-time despite their

![](/api/attachments/FG55HSBR/fulltext/images/3e70ec40fdbecad40e3cb6680c966c4d847563fe3735dd4cc7c833d9fc6782e3.jpg)  
Fig. 2. Detailed architecture of the proposed TOM framework.

dynamic nature. The system performs two functions: First, it detects the changes in term frequencies and second, it performs sentiment analysis in real-time. Some applications of the proposed framework have also been discussed in frequent item mining and sentiment analysis. The paper shows a correlation between the twitter sentiments and the Toyota crisis and successfully claims that the MOA-TweetReader tool could have identi<sup>fi</sup>ed the crisis coming. The authors only use positive/ negative classes for sentiment classi<sup>fi</sup>cation. There is a possibility that a tweet may be neutral, which is not considered in this paper. A small set of emoticons (5 positive and 3 negative) are used, which may not be enough to discover all the emoticons in the tweets.

Ye, S. and Wu, S. F. [4] discovered a message propagation pattern using Twitter. The evaluation is based on examining different social in<sup>fl</sup>uences and their effects such as stabilities, correlations and assessments. An important feature of this research is the identi<sup>fi</sup>cation of popular tweets. However, the authors do not explain the criteria for a

![](/api/attachments/FG55HSBR/fulltext/images/aa1c5130eeb7bd30e19929d0698a81b13536e7807e62ce92c6568d0a7df4df95.jpg)  
Fig. 3. Flow chart of proposed TOM framework.

tweet being popular. The paper also does not explain how it identi<sup>fi</sup>es the virus/worms posting tweets for marketing purposes. Social in<sup>fl</sup>uence is categorized into reply in<sup>fl</sup>uence and re-tweet in<sup>fl</sup>uence. There is no discussion about polarity of the in<sup>fl</sup>uence. The analysis of results is a great achievement towards systematic measurement and investigations on OSNs.

Argamon, S. et al. [5] used a supervised learning algorithm for determining complex sentiment-related attributes. These attributes

Negative emoticons sample set.

<table><tr><td>Emoticon</td><td>Meaning</td></tr><tr><td>:-):o):] :3:c) :&gt;= ] 8) =):}:^): )</td><td>Smiley or happy face</td></tr><tr><td>:-D :D 8-D 8D x-D xD X-D XD =-D =D =-3 =3 B^D :-))</td><td>Laughing, big grinVery happy or double chin</td></tr></table>

Begin Input QueryString Until the data is retrieved from Twitter Streaming API Do Filter English Language Tweets Remove Duplicates FOR each tweet, Do Procedure Pre-process (tweet) Remove URL Remove Hashtags Remove Username Spell Check & Correction Replace Slangs Replace Abbreviations Remove Stop Words Lemmatization Remove Special Characters End Procedure Procedure Classification (Refined tweet) Classifyrefined twveet using Enhanced Emoticon Classifier IF tweet is classified NEUTRAL Classify refined tweet using Enhanced Polarity Classifier ENDIF IF tweet is classified NEUTRAL Classifyrefined tweet using SentiWordNet Classifier ENDIF Write the classification result to file END Procedure End Until End

Fig. 4. Proposed PCA for sentiment analysis.

are classi<sup>fi</sup>ed as attitude type and force. The WordNet glosses are used for the implementation of supervised learning algorithm which classi<sup>fi</sup>es them into four force levels and eleven of attitude levels. The effectiveness of the algorithm is shown through experimental results. The results when averaged show that the Naïve Bayes algorithm is the best among the lot. SVM also dominates the results. The proposed algorithm is well suited where lexicons need to be generated from the scratch.

Fu, X. et al. [6] presented a method for semantic extraction using information theoretic co-clustering. The proposed algorithm is based on implicit associations within evaluated features, within evaluated semantic words and between evaluated features and semantic words. A feature semantic word matrix represents the co-occurrence relationships of feature words and semantic words. Then, co-clustering algorithm is applied on this matrix for clustering of these evaluated features. The dataset used for testing is in Chinese language. There are no details about how the manual analysis of the online review was conducted to ensure that the analysis was not biased. The effectiveness of the proposed technique is demonstrated in experimental results which show 78% accuracy.

Nagy, A. and Stamberger, J. [7] proposed a technique to ef<sup>fi</sup>ciently identify the sentiment from disaster micro-blogs. The paper presents a technique for crowd sentiment detection from informative messages that are crafted for the crowd. This technique is useful to detect the sentiment during disaster and crises. Comparing against the Bayesian network, the proposed technique achieved 27% better performance. Two main approaches used are list based and classi<sup>fi</sup>cation based. The ensemble based technique is used for tweet categorization. SentiWordNet 3.0, list of emoticons, sentiment based dictionary and list of out of vocabulary words is used for sentiment detection from tweet. The emoticon is a pictorial representation of a facial expression depicting the mood of a person as angry, sad, normal or happy. The basic advantage of the proposed technique is that it is generic enough to detect the emotional pulse of people during disasters and crises. It can also detect and analyse the sentiment of a given tweet automatically. The technique can be applied to disaster data and with minimal tweaking and customization, the sentiments of new events and disasters can be identi<sup>fi</sup>ed. Limitations of the technique include limited ability to expand the initial seeds and continuous maintenance of lists.

Montejo-Raez, A. et al. [8] proposed an unsupervised approach for sentiment polarity detection from twitter tweets. The polarity scores are calculated from SentiWordNet and random walk algorithm is used to calculate the weights from the tweet. The proposed algorithm has comparable performance with SVM algorithm. The bene<sup>fi</sup>t of the proposed technique is that there is no need of training corpus as required in supervised learning techniques and there is no dependency on the model domain. The limitations include handling of negation, manual labelling process for certain tweets and facing <sup>fl</sup>aws in calculation of <sup>fi</sup>nal polarity score.

Ortega, R. et al. [9] proposed a technique with three phases; pre-processing, polarity identi<sup>fi</sup>cation and classi<sup>fi</sup>cation. WordNet and SentiWordNet based approach is used for the purpose of polarity detection and rule-based classi<sup>fi</sup>cation is performed. Good classi<sup>fi</sup>cation results are achieved for twitter data. However, there are no details about the dataset being used and the implementation of referenced algorithms. There is no comparison of results with the existing techniques to prove the effectiveness of the proposed research.

Table 1 Positive emoticons sample set.

<table><tr><td>Emoticon</td><td>Meaning</td></tr><tr><td>:-)::o):]:3:c):=&gt;=]8)=):}:^):)</td><td>Smiley or happy face</td></tr><tr><td>::D:D 8-D 8D x-D xD X-D XD =-D =-D =-3 =3 B^D :-))</td><td>Laughing, big grinVery happy or double chin</td></tr></table>

Table 3  
Positive words sample.

<table><tr><td>Accurate</td><td>Beautiful</td><td>Capable</td><td>Decent</td><td>Ease</td><td>Faith</td></tr><tr><td>Gain</td><td>Happy</td><td>Immaculate</td><td>Joy</td><td>Keen</td><td>Lavish</td></tr><tr><td>Majestic</td><td>Neat</td><td>Optimal</td><td>Patriot</td><td>Quick</td><td>Rapid</td></tr><tr><td>Savvy</td><td>Thank</td><td>Unity</td><td>Valuable</td><td>Welcome</td><td>Youthful</td></tr></table>

Bravo-Marquez, F., Mendoza, M. and Poblete, B. [10] combine the existing techniques for opinion strength, emotion and polarity prediction. The results show a great improvement in the classi<sup>fi</sup>cation process. The proposed method is not clearly presented. The authors do not discuss the differences and advantages of the proposed method when comparing with other existing methods.

Kim, J., et al. [11] proposed a collaborative <sup>fi</sup>ltering based model for predicting sentiment in Twitter. Two Twitter datasets were used for evaluation of the proposed model. The results show the effectiveness of the proposed approach for sentiment prediction and provide a solution for data sparsity problem. Few existing approaches have been used but there is no clear presentation of proposed framework which makes it very dif<sup>fi</sup>cult to follow the method.

Machedon, R., Rand, W. and Joshi, Y. [12] de<sup>fi</sup>ned that social media messages are classi<sup>fi</sup>ed into three categories; informative, persuasive and transformative. The tweet data is collected for 65 music bands where each tweet was labelled by human. The authors do not explain if there was any checking process performed to reach a good set of judgments. The results show that the proposed method is effective for the ‘informative’ category only.

Balahur, A. [13] presents a sentiment analysis technique for Twitter data. Training models are generated using the proposed method and the results show good classi<sup>fi</sup>cation performance. Minimal linguistic processing is applied in order to support multilingual datasets. Tweets contain a lot of slangs and abbreviations which would not be interpreted in this case. There is no comparison of results with other techniques in order to judge the effectiveness of the proposed technique.

All the techniques discussed in this section have some advantages and limitations. Hence a comprehensive technique is still needed to overcome their limitations.

## 3. The proposed framework (TOM)

The TOM framework applies a variant of techniques for Twitter feed analysis and classi<sup>fi</sup>cation. This involves pre-processing steps and a hybrid scheme of classi<sup>fi</sup>cation algorithms. Pre-processing steps include: removal of URLs, hash-tags, username & special characters; spelling correction using a dictionary; substitution of abbreviations & slangs with expansions, lemmatization and stop words removal. The proposed classi<sup>fi</sup>cation algorithm incorporates a hybrid scheme using an enhanced form of emoticon analysis [14], SentiWordNet analysis [15] and an improved polarity classi<sup>fi</sup>er using list of positive/negative words [16,21,22].

Table 4  
Negative Words Sample.

<table><tr><td>Abnormal</td><td>Bad</td><td>Cancer</td><td>Danger</td><td>Enemy</td><td>Fake</td></tr><tr><td>Garbage</td><td>Hatred</td><td>Idiot</td><td>Jealous</td><td>Kill</td><td>Lazy</td></tr><tr><td>Malicious</td><td>Nervous</td><td>Obscure</td><td>Pain</td><td>Quarrel</td><td>Rage</td></tr><tr><td>Sad</td><td>Taunt</td><td>Upset</td><td>Vague</td><td>Weird</td><td>Zombie</td></tr></table>

Table 5  
Example Tweets.

<table><tr><td>Sentiment</td><td>Query</td><td>Tweet</td></tr><tr><td>Positive</td><td>Imran Khan</td><td>RT@PTIMalaysia: people of Pakistan love imran khan</td></tr><tr><td>Negative</td><td>Tom Cruise</td><td>#Celebrity #Headline: Tom Cruise&#x27;s “Jack Reacher” fails to reach audiences</td></tr><tr><td>Neutral</td><td>America</td><td>I want to travel around America. #travel #america</td></tr></table>

Previous research [17–19] on Twitter sentiment analysis present different techniques for text classi<sup>fi</sup>cation where the classi<sup>fi</sup>er performs a classi<sup>fi</sup>cation task on the basis of trained data set and machine learning (supervised) algorithms. Classi<sup>fi</sup>ers are trained on labelled corpora where the tweets are classi<sup>fi</sup>ed as positive and negative using emoticon analysis and other features like unigrams, part of speech tags and bigrams etc. Although these are good methods for tweet classi<sup>fi</sup>cation, they pose several challenges. The main challenges are: classi<sup>fi</sup>cation accuracy, sarcasm and data sparsity problem, as they incorrectly classify most of the tweets. The reason behind these problems is use of slangs and other shorthand grammars due to the limit of tweet message (140 characters). Major issues in supervised learning techniques are the availability of trained dataset and determining the structure of learned function. In contrast, unsupervised learning algorithms are a good option as they do not require any training data. Moreover, their goal depends only on situations and they are not mathematically well-de<sup>fi</sup>ned.

The main goal of this research is to improve the accuracy of text classi<sup>fi</sup>cation and resolve the data sparsity issues. The core idea is to preprocess the raw data and perform different transformations to remove the slangs, grammatical mistakes, abbreviations and other noise and then feed it to the classi<sup>fi</sup>er. The TOM system is able to test the data streams from twitter streaming API in real-time continuously. The tweets obtained from these data streams are used as input items. The proposed system is basically composed of three main modules. The <sup>fi</sup>rst module is data acquisition, a process of obtaining twitter feeds from OSN; the second module performs pre-processing and transforms the tweets containing real valued features or arbitrary components and re<sup>fi</sup>nes them into a stream pattern that can be easily used for subsequent analysis. The last component applies different classi<sup>fi</sup>cation techniques in a pipelined way which classi<sup>fi</sup>es the tweets into positive, negative or neutral. The proposed framework is shown in Fig. 2 and the <sup>fl</sup>owchart of the proposed framework is given in Fig. 3.

## 3.1. Proposed data acquisition technique

The fundamental purpose of data acquisition module is to obtain the Twitter feeds with sparse features in continuous fashion. The Twitter streaming API allows real time access to publicly available data on OSN. Twitter4J [20] library has been used for this purpose. The library was con<sup>fi</sup>gured to extract only English language tweets. The tweets serve as input to pre-processing module and then they are further classi<sup>fi</sup>ed as positive, negative or neutral.

Table 6  
Sample datasets.

<table><tr><td></td><td>Query string</td><td>No of tweets analysed</td></tr><tr><td>Dataset 1</td><td>Imran Khan</td><td>99</td></tr><tr><td>Dataset 2</td><td>Nawaz Sharif</td><td>105</td></tr><tr><td>Dataset 3</td><td>Dhoni</td><td>100</td></tr><tr><td>Dataset 4</td><td>Tom Cruise</td><td>300</td></tr><tr><td>Dataset 5</td><td>Pakistan</td><td>512</td></tr><tr><td>Dataset 6</td><td>America</td><td>1000</td></tr></table>

Table 7 Confusion matrix.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Predicted class</td></tr><tr><td>A</td><td>B</td><td>C</td></tr><tr><td rowspan="3">Known class</td><td>A</td><td>tpA</td><td>eAB</td><td>eAC</td></tr><tr><td>B</td><td>eBA</td><td>tpB</td><td>eBC</td></tr><tr><td>C</td><td>eCA</td><td>eCB</td><td>tpC</td></tr></table>

## 3.2. Proposed pre-processing steps

The pre-processing module involves performing intensive processing steps at each tweet individually and then passes each re<sup>fi</sup>ned tweet to the classi<sup>fi</sup>er. This consists of following steps:

• Look up for meaning of each word in three English dictionaries (WordNet/SpellCheck/JSpell). The words that are not found illustrate that they are either slangs or abbreviations. For example, the tweet “@xyz u and Jane are gud friends”. “u” and “gud” will not return any meaning.

• Abbreviations and/or shorthand notations will be replaced by expansions. Netlingo and sms dictionary are used for this purpose. Our example tweet will now be represented as, “@xyz you and Jane are good friends”.

• The next step is to apply lemmatization. Lemmatization is used to stem the words and apply corrections. For example, when ‘happiness is stemmed to ‘happi’.

• Apply spell checking of the tweet in order to correct the effects of the lemmatizer. This step feeds the remaining words in the spell checker and substitute with the best match. We have used Jazzy Spell Checker, JSpell and Snow ball for spell checking. For instance, ‘happi’ is corrected to ‘happy’.

• Identify and remove the stop words. Stanford, Wiki and Texti<sup>fi</sup>er are used to identify the stop words which are then simply stripped from the tweet under process.

• Identify presence of URL using a regular expression and remove all the URLs from the tweet.

• Remove all the private usernames identi<sup>fi</sup>ed by @user and the hashtags identi<sup>fi</sup>ed by the # symbol.

• Lastly, remove all the special characters excluding the emoticons.

• The re<sup>fi</sup>ned tweets are then classi<sup>fi</sup>ed using hybrid classi<sup>fi</sup>cation scheme.

## 3.3. Proposed Polarity Classification Algorithm and evaluation procedure

The proposed Polarity Classi<sup>fi</sup>cation Algorithm (PCA) in TOM framework classi<sup>fi</sup>es twitter feeds on the basis of

• Enhanced Emoticon Classi<sup>fi</sup>er (EEC)

• Improved Polarity Classi<sup>fi</sup>er (IPC)

• SentiWordNet Classi<sup>fi</sup>er (SWNC)

In EEC, classi<sup>fi</sup>cation is done on the basis of emoticons. It uses regular expressions to detect presence of emoticons which are then classi<sup>fi</sup>ed into positive or negative using a rich set of emoticons which are manually tagged as positive or negative. IPC uses a list of positive and negative words which are actually two text <sup>fi</sup>les that include positive and negative words respectively. SWNC is based on classi<sup>fi</sup>cation of tweets using SentiWordNet dictionary to check the sentiments for each word in the tweet.

Fig. 4 gives the detailed algorithm used for twitter feeds classi<sup>fi</sup>cation. Firstly, each tweet is pre-processed using pre-process procedure and then classi<sup>fi</sup>cation is performed at each re<sup>fi</sup>ned tweet as de<sup>fi</sup>ned in classi<sup>fi</sup>cation procedure. Finally, the output is generated in the form of positive, negative or neutral labelled tweets.

Let T be a set of tweets t de<sup>fi</sup>ned as:

$$
T = \{t _ {1}, t _ {2}, \ldots , t _ {n} \}.
$$

Table 8  
Dataset 1 experiment and results.

<table><tr><td rowspan="2" colspan="2">Dataset 1</td><td colspan="3">Confusion matrices</td><td colspan="4">Results</td></tr><tr><td>Positive</td><td>Negative</td><td>Neutral</td><td>Precision</td><td>Recall</td><td>F-measure</td><td>Accuracy</td></tr><tr><td rowspan="3">Proposed</td><td>Positive</td><td>39</td><td>5</td><td>2</td><td>95.12%</td><td>84.78%</td><td>89.66%</td><td rowspan="3">88.89%</td></tr><tr><td>Negative</td><td>2</td><td>38</td><td>0</td><td>84.44%</td><td>95.00%</td><td>89.41%</td></tr><tr><td>Neutral</td><td>0</td><td>2</td><td>11</td><td>84.62%</td><td>84.62%</td><td>84.62%</td></tr><tr><td rowspan="3">EEC</td><td>Positive</td><td>8</td><td>0</td><td>38</td><td>100.00%</td><td>17.39%</td><td>29.63%</td><td rowspan="3">21.21%</td></tr><tr><td>Negative</td><td>0</td><td>0</td><td>40</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>Neutral</td><td>0</td><td>0</td><td>13</td><td>14.29%</td><td>100.00%</td><td>25.00%</td></tr><tr><td rowspan="3">IPC</td><td>Positive</td><td>19</td><td>9</td><td>18</td><td>100.00%</td><td>41.30%</td><td>58.46%</td><td rowspan="3">65.66%</td></tr><tr><td>Negative</td><td>0</td><td>33</td><td>7</td><td>78.57%</td><td>82.50%</td><td>80.49%</td></tr><tr><td>Neutral</td><td>0</td><td>0</td><td>13</td><td>34.21%</td><td>100.00%</td><td>50.98%</td></tr><tr><td rowspan="3">SWNC</td><td>Positive</td><td>27</td><td>17</td><td>2</td><td>62.79%</td><td>58.70%</td><td>60.67%</td><td rowspan="3">61.62%</td></tr><tr><td>Negative</td><td>16</td><td>23</td><td>1</td><td>54.76%</td><td>57.50%</td><td>56.10%</td></tr><tr><td>Neutral</td><td>0</td><td>2</td><td>11</td><td>78.57%</td><td>84.62%</td><td>81.48%</td></tr></table>

Table 9 Dataset 2 experiment and results.

<table><tr><td rowspan="2" colspan="2">Dataset 2</td><td colspan="3">Confusion matrices</td><td colspan="4">Results</td></tr><tr><td>Positive</td><td>Negative</td><td>Neutral</td><td>Precision</td><td>Recall</td><td>F-measure</td><td>Accuracy</td></tr><tr><td rowspan="3">Proposed</td><td>Positive</td><td>38</td><td>3</td><td>0</td><td>82.61%</td><td>92.68%</td><td>87.36%</td><td rowspan="3">82.86%</td></tr><tr><td>Negative</td><td>8</td><td>32</td><td>2</td><td>80.00%</td><td>76.19%</td><td>78.05%</td></tr><tr><td>Neutral</td><td>0</td><td>5</td><td>17</td><td>89.47%</td><td>77.27%</td><td>82.93%</td></tr><tr><td rowspan="3">EEC</td><td>Positive</td><td>4</td><td>0</td><td>37</td><td>100.00%</td><td>9.76%</td><td>17.78%</td><td rowspan="3">23.81%</td></tr><tr><td>Negative</td><td>0</td><td>0</td><td>42</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>Neutral</td><td>0</td><td>1</td><td>21</td><td>21.00%</td><td>95.45%</td><td>34.43%</td></tr><tr><td rowspan="3">IPC</td><td>Positive</td><td>16</td><td>3</td><td>22</td><td>76.19%</td><td>39.02%</td><td>51.61%</td><td rowspan="3">55.24%</td></tr><tr><td>Negative</td><td>5</td><td>22</td><td>15</td><td>81.48%</td><td>52.38%</td><td>63.77%</td></tr><tr><td>Neutral</td><td>0</td><td>2</td><td>20</td><td>35.09%</td><td>90.91%</td><td>50.63%</td></tr><tr><td rowspan="3">SWNC</td><td>Positive</td><td>30</td><td>10</td><td>1</td><td>65.22%</td><td>73.17%</td><td>68.97%</td><td rowspan="3">68.57%</td></tr><tr><td>Negative</td><td>14</td><td>25</td><td>3</td><td>65.79%</td><td>59.52%</td><td>62.50%</td></tr><tr><td>Neutral</td><td>2</td><td>3</td><td>17</td><td>80.95%</td><td>77.27%</td><td>79.07%</td></tr></table>

Let W be a set of words w in each tweet t de<sup>fi</sup>ned as:

$$
W = \{w _ {1}, w _ {2}, \dots , w _ {m} \}.
$$

Score S is calculated as follows:

$$
\text { Score } = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} S _ {t _ {i} w _ {j}}.
$$

where S is the sentiment score calculated for each word in the tweet.

We will use following three score calculations for the <sup>fi</sup>nal classi<sup>fi</sup>cation of the tweet.

## 3.3.1. EEC score calculation

Emoticons are domain and language independent. They are used very sparingly and they constitute a very small portion of the text. As observed by Read [14], only 2.435% of downloaded Usenet articles contained a wink emoticon. EEC is very effective when the emoticons are present in the data. Read [14] achieved 70% accuracy for article extracts from emoticon dataset. EEC is not effective when classifying datasets that do not contain any emoticon. From these points we come to a conclusion that EEC should be used when an emoticon is present in the tweet. Otherwise, some other classi<sup>fi</sup>er may be used for classi<sup>fi</sup>cation.

Table 10  
Dataset 3 experiment and results.

<table><tr><td rowspan="2" colspan="2">Dataset 3</td><td colspan="3">Confusion matrices</td><td colspan="4">Results</td></tr><tr><td>Positive</td><td>Negative</td><td>Neutral</td><td>Precision</td><td>Recall</td><td>F-measure</td><td>Accuracy</td></tr><tr><td rowspan="3">Proposed</td><td>Positive</td><td>35</td><td>3</td><td>0</td><td>79.55%</td><td>92.11%</td><td>85.37%</td><td rowspan="3">86.00%</td></tr><tr><td>Negative</td><td>7</td><td>46</td><td>1</td><td>92.00%</td><td>85.19%</td><td>88.46%</td></tr><tr><td>Neutral</td><td>2</td><td>1</td><td>5</td><td>83.33%</td><td>62.50%</td><td>71.43%</td></tr><tr><td rowspan="3">EEC</td><td>Positive</td><td>13</td><td>0</td><td>25</td><td>100.00%</td><td>34.21%</td><td>50.98%</td><td rowspan="3">23.00%</td></tr><tr><td>Negative</td><td>0</td><td>2</td><td>52</td><td>100.00%</td><td>3.70%</td><td>7.14%</td></tr><tr><td>Neutral</td><td>0</td><td>0</td><td>8</td><td>9.41%</td><td>100.00%</td><td>17.20%</td></tr><tr><td rowspan="3">IPC</td><td>Positive</td><td>14</td><td>3</td><td>21</td><td>87.50%</td><td>36.84%</td><td>51.85%</td><td rowspan="3">48.00%</td></tr><tr><td>Negative</td><td>2</td><td>27</td><td>25</td><td>87.10%</td><td>50.00%</td><td>63.53%</td></tr><tr><td>Neutral</td><td>0</td><td>1</td><td>7</td><td>13.21%</td><td>87.50%</td><td>22.95%</td></tr><tr><td rowspan="3">SWNC</td><td>Positive</td><td>24</td><td>10</td><td>4</td><td>58.54%</td><td>63.16%</td><td>60.76%</td><td rowspan="3">67.00%</td></tr><tr><td>Negative</td><td>15</td><td>38</td><td>1</td><td>77.55%</td><td>70.37%</td><td>73.79%</td></tr><tr><td>Neutral</td><td>2</td><td>1</td><td>5</td><td>50.00%</td><td>62.50%</td><td>55.56%</td></tr></table>

Table 11 Dataset 4 experiment and results.

<table><tr><td rowspan="2" colspan="2">Dataset 4</td><td colspan="3">Confusion matrices</td><td colspan="4">Results</td></tr><tr><td>Positive</td><td>Negative</td><td>Neutral</td><td>Precision</td><td>Recall</td><td>F-measure</td><td>Accuracy</td></tr><tr><td rowspan="3">Proposed</td><td>Positive</td><td>188</td><td>10</td><td>0</td><td>87.44%</td><td>94.95%</td><td>91.04%</td><td rowspan="3">85.00%</td></tr><tr><td>Negative</td><td>27</td><td>67</td><td>0</td><td>78.82%</td><td>71.28%</td><td>74.86%</td></tr><tr><td>Neutral</td><td>0</td><td>8</td><td>0</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td rowspan="3">EEC</td><td>Positive</td><td>16</td><td>0</td><td>182</td><td>100.00%</td><td>8.08%</td><td>14.95%</td><td rowspan="3">8.00%</td></tr><tr><td>Negative</td><td>0</td><td>1</td><td>93</td><td>50.00%</td><td>1.06%</td><td>2.08%</td></tr><tr><td>Neutral</td><td>0</td><td>1</td><td>7</td><td>2.48%</td><td>87.50%</td><td>4.83%</td></tr><tr><td rowspan="3">IPC</td><td>Positive</td><td>78</td><td>7</td><td>113</td><td>96.30%</td><td>39.39%</td><td>55.91%</td><td rowspan="3">44.33%</td></tr><tr><td>Negative</td><td>3</td><td>48</td><td>43</td><td>85.71%</td><td>51.06%</td><td>64.00%</td></tr><tr><td>Neutral</td><td>0</td><td>1</td><td>7</td><td>4.29%</td><td>87.50%</td><td>8.19%</td></tr><tr><td rowspan="3">SWNC</td><td>Positive</td><td>180</td><td>18</td><td>0</td><td>77.92%</td><td>90.91%</td><td>83.92%</td><td rowspan="3">75.00%</td></tr><tr><td>Negative</td><td>49</td><td>45</td><td>0</td><td>65.22%</td><td>47.87%</td><td>55.21%</td></tr><tr><td>Neutral</td><td>2</td><td>6</td><td>0</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr></table>

An emoticon is identi<sup>fi</sup>ed using a regular expression. The emoticon classi<sup>fi</sup>cation is based on sets of positive & negative emoticons. EEC is an enhancement of the technique proposed by Read [14]. Read used 11 trained emoticons whereas we have used a total of 145 emoticons; 70 of which are tagged positive and 75 are tagged as negative. The sample sets of positive and negative emoticons are given in Tables 1 and 2 respectively. Furthermore, we feed pre-processed text for classi<sup>fi</sup>- cation. If the emoticon is found in the positive set then it is declared as positive. The emoticon is declared negative if it is found in negative set. If the emoticon is not found in both the sets, we declare it as neutral. Total positive and negative emoticons are counted and the sum is calculated. The re<sup>fi</sup>ned tweet is assigned a score of 1 if the sum is greater than zero. A score of −1 is assigned if the sum is less than zero. A score of zero indicates that the calculated sum is zero.

Table 12  
Dataset 5 experiment and results.

<table><tr><td rowspan="2" colspan="2">Dataset 5</td><td colspan="3">Confusion matrices</td><td colspan="4">Results</td></tr><tr><td>Positive</td><td>Negative</td><td>Neutral</td><td>Precision</td><td>Recall</td><td>F-measure</td><td>Accuracy</td></tr><tr><td rowspan="3">Proposed</td><td>Positive</td><td>177</td><td>16</td><td>2</td><td>80.45%</td><td>90.77%</td><td>85.30%</td><td rowspan="3">85.55%</td></tr><tr><td>Negative</td><td>37</td><td>220</td><td>4</td><td>89.80%</td><td>84.29%</td><td>86.96%</td></tr><tr><td>Neutral</td><td>6</td><td>9</td><td>41</td><td>87.23%</td><td>73.21%</td><td>79.61%</td></tr><tr><td rowspan="3">EEC</td><td>Positive</td><td>21</td><td>1</td><td>173</td><td>72.41%</td><td>10.77%</td><td>18.75%</td><td rowspan="3">16.02%</td></tr><tr><td>Negative</td><td>8</td><td>6</td><td>247</td><td>75.00%</td><td>2.30%</td><td>4.46%</td></tr><tr><td>Neutral</td><td>0</td><td>1</td><td>55</td><td>11.58%</td><td>98.21%</td><td>20.72%</td></tr><tr><td rowspan="3">IPC</td><td>Positive</td><td>80</td><td>5</td><td>110</td><td>90.91%</td><td>41.03%</td><td>56.54%</td><td rowspan="3">59.77%</td></tr><tr><td>Negative</td><td>8</td><td>171</td><td>82</td><td>96.61%</td><td>65.52%</td><td>78.08%</td></tr><tr><td>Neutral</td><td>0</td><td>1</td><td>55</td><td>22.27%</td><td>98.21%</td><td>36.30%</td></tr><tr><td rowspan="3">SWNC</td><td>Positive</td><td>149</td><td>38</td><td>8</td><td>64.22%</td><td>76.41%</td><td>69.79%</td><td rowspan="3">71.68%</td></tr><tr><td>Negative</td><td>76</td><td>176</td><td>9</td><td>79.64%</td><td>67.43%</td><td>73.03%</td></tr><tr><td>Neutral</td><td>7</td><td>7</td><td>42</td><td>71.19%</td><td>75.00%</td><td>73.04%</td></tr></table>

Table 13  
Dataset 6 experiment and results.

<table><tr><td rowspan="2" colspan="2">Dataset 6</td><td colspan="3">Confusion matrices</td><td colspan="4">Results</td></tr><tr><td>Positive</td><td>Negative</td><td>Neutral</td><td>Precision</td><td>Recall</td><td>F-measure</td><td>Accuracy</td></tr><tr><td rowspan="3">Proposed</td><td>Positive</td><td>443</td><td>45</td><td>4</td><td>88.60%</td><td>90.04%</td><td>89.31%</td><td rowspan="3">85.90%</td></tr><tr><td>Negative</td><td>45</td><td>366</td><td>6</td><td>83.18%</td><td>87.77%</td><td>85.41%</td></tr><tr><td>Neutral</td><td>12</td><td>29</td><td>50</td><td>83.33%</td><td>54.95%</td><td>66.23%</td></tr><tr><td rowspan="3">EEC</td><td>Positive</td><td>38</td><td>4</td><td>450</td><td>63.33%</td><td>7.72%</td><td>13.77%</td><td rowspan="3">13.40%</td></tr><tr><td>Negative</td><td>20</td><td>11</td><td>386</td><td>57.89%</td><td>2.64%</td><td>5.05%</td></tr><tr><td>Neutral</td><td>2</td><td>4</td><td>85</td><td>9.23%</td><td>93.41%</td><td>16.80%</td></tr><tr><td rowspan="3">IPC</td><td>Positive</td><td>209</td><td>54</td><td>29</td><td>74.64%</td><td>42.48%</td><td>54.15%</td><td rowspan="3">52.90%</td></tr><tr><td>Negative</td><td>62</td><td>243</td><td>112</td><td>80.46%</td><td>58.27%</td><td>67.59%</td></tr><tr><td>Neutral</td><td>9</td><td>5</td><td>77</td><td>18.42%</td><td>84.62%</td><td>30.26%</td></tr><tr><td rowspan="3">SWNC</td><td>Positive</td><td>315</td><td>172</td><td>5</td><td>84.45%</td><td>64.02%</td><td>72.83%</td><td rowspan="3">74.20%</td></tr><tr><td>Negative</td><td>35</td><td>376</td><td>6</td><td>66.55%</td><td>90.17%</td><td>76.58%</td></tr><tr><td>Neutral</td><td>23</td><td>17</td><td>51</td><td>82.26%</td><td>56.04%</td><td>66.67%</td></tr></table>

Let PE denote a set of positive emoticons

PE   Set of Positive Emoticons :

Let NE denote a set of negative emoticons

NE Set of Negative Emoticons :

The emoticon score $S _ { e }$ is calculated as:

$$
\operatorname{Score} (e) = \left\{ \begin{array}{l} 1, (w _ {x} \in W) \land (t \in T) \land (w _ {x} \in \mathrm{PE}) \\ - 1, \Big (w _ {y} \in W \Big) \land (t \in T) \land \Big (w _ {y} \in \mathrm{NE} \Big) \\ 0, (w _ {z} \in W) \land (t \in T) \land (w _ {z} \notin \mathrm{PE}) \land (w _ {z} \notin \mathrm{NE}) \end{array} \right.
$$

where $w _ { x } , w _ { y }$ and w are words belonging to set of words W and t is a tweet from the set of tweets T.

## 3.3.2. IPC score calculation

IPC uses ‘bag of words’ approach. Words are domain independent. Each word in the list has been classi<sup>fi</sup>ed as positive/negative. We have to provide words in correct spelling to be classi<sup>fi</sup>ed by IPC. Every word has the same weight. There may be a combination of positive/negative words in a tweet which may result in incorrect classi<sup>fi</sup>cation of tweet as neutral. There may be unrecognized words in the tweet resulting in incorrectly classifying the tweet as neutral. These problems can be solved by using SWNC.

A word is identi<sup>fi</sup>ed by splitting the re<sup>fi</sup>ned tweet using the word separators like space, comma, semi-colon and full stop. The IPC is an improvement over the technique proposed in [16] by using a richer trained data set and pre-processed text. The set of positive and negative words are created from the Bing Liu list [21] and the Bill McDonald list [22]. The word count in the Bing Liu list is: 2006 positive words and 4784 negative words which makes 6790 in total whereas the word count in the Bill McDonald list is: 354 positive words and 2349 negative words which makes 2703 words in total. The total trained word count for the IPC is 9493. The sample sets of positive and negative words are given in Table 3 and Table 4. If the word is found in the positive set then it is declared as positive. It is declared negative if found in the negative set.

If the word is not found in both the sets, we declare it as neutral. Total positive and negative words are counted and the sum is calculated. A score of 1 is assigned to the re<sup>fi</sup>ned tweet, if the sum is greater than zero. A score of −1 is assigned if the sum is less than zero. A score of zero indicates that the calculated sum is zero.

Let PW be a set of positive words

PW    Set of Positive Words :

Let NW be a set of negative words

NW Set of Negative Words :

The list of words score $S _ { w }$ is calculated as:

$$
\operatorname{Score} (w) = \left\{ \begin{array}{l} 1, (w _ {x} \in W) \land (t \in T) \land (w _ {x} \in \mathrm{PW}) \\ - 1, \left(w _ {y} \in W\right) \land (t \in T) \land \left(w _ {y} \in \mathrm{NW}\right) \\ 0, (w _ {z} \in W) \land (t \in T) \land (w _ {z} \notin \mathrm{PW}) \land (w _ {z} \notin \mathrm{NW}) \end{array} \right.
$$

where $w _ { x } , w _ { y }$ and $w _ { z }$ are words belonging to set of words W and t is a tweet from the set of tweets T.

## 3.3.3. SWNC score calculation

SWNC assigns different sentiment weights to different words. It also depends on the how the word is being used in the sentence i.e. identi<sup>fi</sup>- cation of ‘part of speech’ for the word is necessary to be classi<sup>fi</sup>ed by SWNC.

Similar to the previous step, a word is identi<sup>fi</sup>ed by splitting the re-<sup>fi</sup>ned tweet using the word separators like space, comma, semi-colon and full stop. The sentiment value of each word is calculated by calling the SentiWordNet. Sentiment weight for each word is found and the sum is calculated by adding each of the sentiment weights. A score of 1 is assigned to the re<sup>fi</sup>ned tweet, if the calculated sum is greater than zero. A score of 1 is assigned if the sum is less than zero. A score of zero indicates that the calculated sum is zero.

![](/api/attachments/FG55HSBR/fulltext/images/3d8eca13ec64c773e29036c2b521b4d1c12da09ce4bbfeeee68e0059cfcf9445.jpg)  
Fig. 5. Distribution of overall dataset tweets.

The SWNC score $S _ { s }$ is calculated as:

$$
\operatorname{Score} (s) = \left\{ \begin{array}{l} 1, (w _ {x} \in W) \wedge (t \in T) \wedge (\text { weight } (w _ {x}) > 0) \\ - 1, \left(w _ {y} \in W\right) \wedge (t \in T) \wedge \left(\text { weight } (w _ {y}) <   0\right) \\ 0, (w _ {z} \in W) \wedge (t \in T) \wedge (\text { weight } (w _ {z}) <   0) \end{array} \right.
$$

where $w _ { x } , w _ { y }$ and $w _ { z }$ are words belonging to set of words W and t is a tweet from the set of tweets T and weights are calculated using SentiWordNet dictionary.

## 3.4. Classifying the tweet

First we perform the EEC based classi<sup>fi</sup>cation, next IPC classi<sup>fi</sup>cation is done and lastly SWNC based classi<sup>fi</sup>cation is performed. If the result of EEC is a neutral tweet, we perform IPC and if it is still classi<sup>fi</sup>ed as neutral, we move to SWNC. If all the three techniques classify the tweet as neutral, we declare it as neutral. Otherwise, we classify it into positive or negative as declared by the classi<sup>fi</sup>ers. This helps to reduce the number of neutral tweets which was a major issue in previous techniques. The results also indicate that this classi<sup>fi</sup>cation procedure is more accurate than its predecessors.

The <sup>fi</sup>nal classi<sup>fi</sup>cation is done using the three scores as below:

$$
\text { Class } = \left\{ \begin{array}{l} \text { Positive, } (S _ {e} > 0) \lor (S _ {e} = 0 \land S _ {w} > 0) \lor (S _ {e} = 0 \land S _ {w} = 0 \land S _ {s} > 0) \\ \text { Negative, } (S _ {e} <   0) \lor (S _ {e} = 0 \land S _ {w} <   0) \lor (S _ {e} = 0 \land S _ {w} = 0 \land S _ {s} <   0) \\ \text { Neutral, } (S _ {e} = 0) \land (S _ {w} = 0) \land (S _ {w} = 0) \end{array} \right.
$$

where $S _ { e } , S _ { w }$ and $S _ { s }$ are scores from EEC, IPC and SWNC respectively.

## 4. Results and discussion

The datasets were generated using the data acquisition module. The experiments have been conducted using 6 different datasets. The experiments are performed using 2116 random tweets. These tweets were collected from Twitter using twitter streaming API. Random tweets with different search strings at different times were considered for analysis. Crowdsourcing method was used to gather human judgments as mentioned in [12]. Different sets of tweets were distributed among students, teachers, and industry people in such a way that we had at least 5 judgments for each tweet. Then majority voting was applied to classify the tweet. This process ensures that a good set of judgments are available for testing the classi<sup>fi</sup>er performance.

The upper limit of number of tweets provided by the API is around 100 in one attempt, so we have to query again to get more tweets as they come along as the time passes. In this way we collected 6 sets of tweets. Each set of the tweet is about a certain object, personality or event. Table 5 shows some examples of positive, negative and neutral tweets. The count of each data set is given in Table 6.

Confusion matrices, precision, recall, F-measure and accuracy are used for evaluation of the proposed framework and comparison with other techniques. The confusion matrix is de<sup>fi</sup>ned in Table 7.

The diagonal elements (tpA, tpB, tpC) in the confusion matrix present the correctly classi<sup>fi</sup>ed data for each class whereas all other elements show incorrectly classi<sup>fi</sup>ed data.

Precision is de<sup>fi</sup>ned by the fraction of true positives against both true positives and false positives (all positive results). Mathematically:

$$
\text { PrecisionA } = \frac {\mathrm{tpA}}{\mathrm{tpA} + \mathrm{eBA} + \mathrm{eCA}}
$$

where tpA is the number of true positive predictions for the class A and eBA, eCA are false positives.

Recall is the proportion between correctly classi<sup>fi</sup>ed positives by the classi<sup>fi</sup>er and manual classi<sup>fi</sup>ed positives (true positives + false negatives). Mathematically:

$$
\text { RecallA } = \frac {\mathrm{tpA}}{\mathrm{tpA} + \mathrm{eAB} + \mathrm{eAC}}
$$

where tpA is the number of true positive predictions for the class A and eAB, eAC are false negatives.

F-measure is the harmonic mean of both precision and recall. Mathematically:

$$
F \text {-measure} = 2 * \frac {\text { Precision } * \text { Recall }}{\text { Precision } + \text { Recall }}.
$$

Accuracy is de<sup>fi</sup>ned as the proportion of true positive, true negatives and true neutrals (true results) from all the given data.

```python
Accuracy = # True Positives + True Negatives + True Neutrals
# True Positives + False Positives + True Negatives + False Negatives + True Neutrals + False Neutrals
```

The classi<sup>fi</sup>cation algorithm runs on test datasets and processes each tweet. It classi<sup>fi</sup>es the tweets into positive, negative and neutral classes.

![](/api/attachments/FG55HSBR/fulltext/images/2b608832eace18c8f4e6547da092fe0755db83985ff5d4abdbde49b3424977a9.jpg)  
Fig. 6. Precision, recall and F-measure of proposed algorithm.

![](/api/attachments/FG55HSBR/fulltext/images/0868140467088f61e34b79f7ce6f06c61f39927deadc0388f0b46685932a4e35.jpg)  
Fig. 7. Classi<sup>fi</sup>ers accuracy comparison using different datasets

Confusion matrices, precision, recall, F-measure and accuracy are calculated for the proposed TOM framework and also for the EEC, IPC & SWNC. The results are used to verify the superiority of the proposed classi<sup>fi</sup>er. Tables 8–13 show these results for all the datasets.

The overall dataset is shown in Fig. 5. We have used a total of 2116 tweets which are classi<sup>fi</sup>ed as 1058 positive, 872 negative and 186 neutral by crowd sourcing method.

The evaluation results of precision, recall and F-measure of complete datasets are shown in Fig. 6.

We have compared the accuracy of the proposed technique with other related techniques of sentiment analysis. It is clear from the comparison that the proposed algorithm shows better accuracy for classi<sup>fi</sup> cation. The graphical representation of comparison is done in Fig. 7.

Pre-processing, EEC, IPC and SWNC play a major role in the resolution of sparsity issue. The pre-processing step is involved indirectly as it prepares the data that is worked upon by the EEC, IPC and SWNC. As a result, the proposed framework is successfully able to label the tweets without any training dataset using domain independent features like words and emoticons.

## 5. Conclusion and future work

The research paper has proposed a new algorithm for twitter sentiment analysis and it is based on three way classi<sup>fi</sup>cation algorithm. We have also discussed challenges that are faced during sentiment analysis and proposed the algorithm that resolves these issues and increases the classi<sup>fi</sup>cation accuracy effectively reducing the number of classi<sup>fi</sup>ed neutrals. The results of the proposed framework show great improvement when comparing with similar work. We have achieved an average accuracy of 85.7% with 85.3% precision and 82.2% recall. Future research directions include the development of a web application in order to compare the performance of our algorithm with other applications like TweetFeel & Sentiment140 and the use of supervised learning algorithms to further increase the accuracy.

## References

[1] A. Cui, M. Zhang, Y. Liu, S. Ma, Emotion Tokens: Bridging the Gap among Multilingual Twitter Sentiment Analysis, Springer-Verlag, Berlin, Heidelberg, 2011, pp. 238–249.

[2] A. Bifet, E. Frank, Sentiment Knowledge Discovery in Twitter Streaming Data, Springer-Verlag, Berlin, Heidelberg, 2010, pp. 1–15.

[3] A. Bifet, G. Holmes, B. Pfahringer, MOA-TweetReader: real-time analysis in twitter streaming data in: T. Elomaa I. Hollm'en H. Mannila (Eds.). DS 2011 LNCS 6926 Springer-Verlag, Berlin Heidelberg, 2011, pp. 46–60.

[4] S. Ye, S.F. Wu, Measuring message propagation and social in<sup>fl</sup>uence on Twitter.com, in: L. Bolc, M. Makowski, A. Wierzbicki (Eds.), SocInfo 2010, LNCS 6430 Springer-Verlag, Berlin Heidelberg, 2010, pp. 216–231.

[5] S. Argamon, K. Bloom, A. Esuli, F. Sebastiani, Automatically determining attitude type and force for sentiment analysis, in: Z. Vetulani, H. Uszkoreit (Eds.), LTC 2007, LNAI 5603, Springer-Verlag, Berlin Heidelberg, 2009, pp. 218–231.

[6] X. Fu, Y. Guo, W. Guo, Z. Wang, et al., Aspect and sentiment extraction based on information-theoretic co-clustering, in: J. Wang, G.G. Yen, M.M. Polycarpou (Eds.), ISNN 2012, Part II, LNCS 7368, Springer-Verlag, Berlin, Heidelberg, 2012, pp. 326–335.

[7] A. Nagy, J. Stamberger, Crowd sentiment detection during disasters and crises Proceedings of the 9th International ISCRAM Conference — Vancouver, Canada, 2012.

[8] A. Monteio-Raez. E. Martınez-Camara. M.T. Martın-Valdivia. L.A. Urena-Lopez. RandomWalk weighting over SentiWordNet for sentiment polarity detection on Twitter, Proceedings of the 3rd Workshop on Computational Approaches to Subjectivity and Sentiment Analysis, 2012, pp. 3–10.

[9] R. Ortega, A. Fonseca, M. Mendoza, Y. Guti'errez, SSA-UO: unsupervised Twitter sentiment analysis, in: A. Montoyo (Ed.), Second Joint Conference on Lexical and Computational Semantics (\*SEM), Volume 2: Seventh International Workshop on Semantic Evaluation (SemEval 2013), 2013, pp. 501–507. (Atlanta. Georgia)

[10] F. Bravo-Marquez, M. Mendoza, B. Poblete, Combining Strengths, Emotions and Polarities for Boosting Twitter Sentiment Analysis, WISDOM'13, Chicago, IL, USA, 2013.

[11] J. Kim, J. Yoo, H. Lim, H. Qiu, Z. Kozareva, A. Galstyan, Sentiment Prediction using Collaborative Filtering, Association for the Advancement of Arti<sup>fi</sup>cial Intelligence, 2013.

[12] R. Machedon, W. Rand, Y. Joshi, Automatic Classi<sup>fi</sup>cation of Social Media Messaging using Multi-Dimensional Sentiment Analysis and Crowdsourcing, 2013, 2013. http://dx.doi.org/10.2139/ssrn.2244353 (Available at SSRN: http://ssrn.com/ abstract=2244353).

[13] A. Balahur, Sentiment Analysis in Social Media Texts, 2013, pp. 120–128, Atlanta, Georgia.

[14] J. Read, Using emoticons to reduce dependency in machine learning techniques for sentiment classification Proceedings of the ACI Student Research Workshop 2005 pp. 43–48.

[15] S. Baccianella, A. Esuli, F. Sebastiani, SENTIWORDNET 3.0: an enhanced lexical resource for sentiment analysis and opinion mining, http://nmis.isti.cnr.it/sebastiani/ Publications/LREC10.pdf(Accessed 4 Feb 2013).

[16] B. Liu, S. Li, W.S. Lee, P.S. Yu, Text classi<sup>fi</sup>cation by labeling words, Proceedings of the National Conference on Artificial Intelligence, AAAL Press: MIT Press Menlo Park CA: Cambridge MA: London 2004 pp. 425–430

[17] L. Barbosa, J. Feng, Robust sentiment detection on twitter from biased and noisy data, Proceedings of COLING, 2010, pp. 36–44.

[18] A. Go, R. Bhayani, L. Huang, Twitter sentiment classi<sup>fi</sup>cation using distant supervision, CS224N Project Report, Stanford, 2009.

[19] A. Pak, P. Paroubek, Twitter as a corpus for sentiment analysis and opinion mining, Proceedings of LREC, 2010.

[20] Twitter4J, http://twitter4j.org/en/index.html, Accessed 4 Feb 2013.

[21] Bing Liu list of words, http://www.cs.uic.edu/ liub/FBS/opinion-lexicon-English.rar, Accessed 16 Feb 2013

[22] Bill McDonald list of words, http://www3.nd.edu/mcdonald/Word\_Lists.html, Accessed 16 Feb 2013

Saba Bashir is an Assistant Professor in Computer Science Department at Federal Urdu University of Arts, Science & Technology, Pakistan. She is also a PhD research scholar at NUST, Pakistan. Her research interest lies in predictive systems, web services and object oriented computing, She has published more than 8 research papers in international conferences & journals.

Farhan Hassan Khan has been working as a Project Manager in a software development organisation in Pakistan since 2005. He is also a PhD research scholar at NUST, Pakistan His research interest lies in text mining, web service computing and VoIP billing products He has published many research papers in international conferences & journals.

Dr. Usman Qamar is an Assistant Professor in Computer Engineering Department at CE&ME, National University of Science & Technology, Pakistan. He completed his PhD (Information Systems) from the University of Manchester, UK. His research interest lies in Data Mining, Outlier Detection, and Feature Selection.
