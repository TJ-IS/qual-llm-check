---
otero_id: 11160
otero_key: "VAAFHWTQ"
title: "An abusive text detection system based on enhanced abusive and non-abusive word lists"
authors: "Ho-Suk Lee; Hong-Rae Lee; Jun-U Park; Yo-Sub Han"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.06.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

An Abusive Text Detection System based on Enhanced Abusive and Non-Abusive Word Lists

![](/api/attachments/VAAFHWTQ/fulltext/images/08b5a3a92b2270bcedefd1d3e5a1986446689b093775f3d1571aabfd21f7462b.jpg)

Ho-Suk Lee, Hong-Rae Lee, Jun-U Park, Yo-Sub Han

<table><tr><td>PII:</td><td>S0167-9236(18)30106-4</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.06.009</td></tr><tr><td>Reference:</td><td>DECSUP 12967</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>15 December 2017</td></tr><tr><td>Revised date:</td><td>25 June 2018</td></tr><tr><td>Accepted date:</td><td>26 June 2018</td></tr></table>

Please cite this article as: Ho-Suk Lee, Hong-Rae Lee, Jun-U Park, Yo-Sub Han , An Abusive Text Detection System based on Enhanced Abusive and Non-Abusive Word Lists. Decsup (2018), doi:10.1016/j.dss.2018.06.009

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# An Abusive Text Detection System based on Enhanced Abusive and Non-Abusive Word Lists

Ho-Suk Lee, Hong-Rae Lee, Jun-U Park, Yo-Sub Han<sup>∗</sup>

## Abstract

Abusive text (indiscriminate slang, abusive language, and profanity) on the Internet is not just a message but rather a tool for very serious and brutal cyber violence. It has become an important problem to devise a method for detecting and preventing abusive text online. However, the intentional obfuscation of words and phrases makes this task very dificult and challenging. We design a decision system that successfully detects (obfuscated) abusive text using an unsupervised learning of abusive words based on word2vec’s skip-gram and the cosine similarity. The system also deploys several eficient gadgets for filtering abusive text such as blacklists, n-grams, edit-distance metrics, mixed languages, abbreviations, punctuation, and words with special characters to detect the intentional obfuscation of abusive words. We integrate both an unsupervised learning method and eficient gadgets into a single system that enhances abusive and non-abusive word lists. The integrated decision system based on the enhanced word lists shows a precision of 94.08%, a recall of 80.79%, and an f-score of 86.93% in malicious word detection for news article comments, a precision of 89.97%, a recall of 80.55%,

ACCEPTED MANUSCRIPT

and an f-score 85.00% for online community comments, and a precision of 90.65%, a recall of 93.57%, and an f-score 92.09% for Twitter tweets. We expect that our approach can help to improve the current abusive word detection system, which is crucial for several web-based services including social networking services and online games.

Keywords: Abusive Words, Slang Words, Profanity, Cyber Bullying, Detection Systems

## 1. Introduction

Indiscriminate slang, abusive language, and profanity are generated, used, and propagated more quickly on the Internet than in any other area, including schools, companies, and society in general [16]. The increase in the number of smart devices and mobile users means social networking services (SNSs) are now more pervasive then ever. One of the most common actions on a social network is to write a comment. For instance, users of an SNS (e.g., Facebook or Twitter), web community site (e.g., blog or user group), or a news service read articles written by others and write comments in order to express their ideas or opinions. We call a comment a text. There are three types of text: 1) benevolent comments, 2) neutral comments, and 3) malicious comments. The use of abusive text such as indiscriminate slang, abusive language, and profanity on the Internet has become a type of cyber violence. In the past, cyber violence tended to be limited to young people familiar with the Internet, but it now afects all age groups and has become a major problem in society [7]. The Cyberbullying Research Center surveyed a nationally representative sample of 5,700 middle and high school students between the ages of 12 and 17 in the United States. The survey results revealed that approximately 34% of the students have experienced cyberbullying<sup>1</sup>. Furthermore, the cyberbullying statistics published by the Korea Communications Commission and the Korea Internet & Security Agency in 2014 [23] reveal that 30.5% of adults have experienced cyber violence. Cyber violence can result in tragedy. In the Unite States, a 12-year-old girl committed suicide after being targeted by cyberbullies in 2013<sup>2</sup>. In Australia, Charlotte Dawson, who hosted the “Next Top Model” TV program committed suicide in 2012 after being received malicious online comments<sup>3</sup>. These are just a few examples of what is becoming an increasingly serious problem in modern society.

From a social science viewpoint and a computer science viewpoint, there is an urgent need to devise an eficient and efective system that can detect such abusive text online. A simple solution is to maintain a list of abusive words. However, the intentional obfuscation of words and phrases by users makes this task very dificult. Humans can easily understand sentences with intentional obfuscations of abusive words and, thus, detect abusive text. However, a computer system would find this far more dificult. This motivates us to design a system that successfully detects (obfuscated) abusive text. Note that several researchers have previously considered the obfuscated word problem in diferent domains and proposed efective solutions [10, 13].

Complicating the issue further is the invention of words that do not resemble known abusive words. Thus, there are two types of abusive words: 1) newly invented words, and 2) obfuscated words based on existing abusive words. Most existing approaches do not handle both cases efectively. For example, some are good at detecting the second type of abusive words, but cannot handle the first type efectively. We tackle these problems in two ways. First we use the word embedding of word2vec’s skip-gram and, second we use cosine similarity to detect newly invented abusive words. We employ several eficient gadgets to classify abusive and non-abusive word lists such as blacklists, n-grams and edit-distance metrics to detect intentionally obfuscated words. We combine these gadgets with unsupervised learning, and verify the performance of our system using real-world online messages and comments. The experimental results show that the proposed system efectively detects abusive text.

## 2. Related Work

Cyberbullying is causing numerous social problems caused. One common type of cyberbullying is the use of abusive text. Most existing research on detecting abusive language focused on areas such as NLP, AI, and databases. For example, researchers have found that abusive text is often closely related to sentiment [2, 29]. Two of the most popular platforms used for online sentiment analyses are Twitter and Facebook. Khan et al. [15] proposed a technique for mining the text in Twitter feeds in real time and presented a sentiment analysis using a three-way classification of sentiment intensity. da Silva et al. [26] proposed an algorithm that analyzes tweet sentiment based on classifier ensembles using a bag-of-words model and feature hashing. Their experiments on tweet sentiment data sets showed that classifier ensembles formed by multinomial naive Bayes, SVM, random forest, and logistic regressions improve the classification accuracy. Meire et al. [18] evaluated the added value of leading and lagging information in a sentiment analysis of Facebook status updates. They used two classification algorithms, namely, five two-fold cross-validation tests and the Friedman test, and demonstrated that including leading and lagging data in the sentiment analysis is a viable strategy.

People invent new words to circumvent a system that detects abusive text. This has been an issue since e-mail spam filtering became necessary, and various algorithms have been suggested as possible solutions [10, 13].

Recently, several studies have attempted to design eficient and efective decision systems for abusive text based on modifications of existing filtering or search algorithms. For instance, Schmidt and Weigand [25] presented a survey on the automatic detection of hate speech using natural language processing. Zhang et al. [30] proposed an algorithm for detecting hate speech are no public benchmark test sets, researchers tend to evaluate these systems using their own data sets. This makes direct comparisons dificult. Therefore, we compare the performance of previous approaches based on their precision, recall, and f-score, which are indirect comparison metrics.

Yin et al. [29] hypothesized that many expressions of harassment occur around the pronoun “you.” Using this hypothesis, they identified harassing IDF) and n-grams based on supervised learning for pronouns. Although their evaluation performance is not very good, they nevertheless provided the first method for detecting abusive language.

Sood et al. [28] proposed an abusive language detection system using words from noswearing.com<sup>4</sup> as an unethical lexicon. They also applied an edit-distance metric and support vector machines (SVMs). As experimental sets, Sood et al. [28] used a set of comments from a social news site labeled by Amazon Mechanical Turk to determine the presence of profanity.

Brody and Diakopoulos [2] assumed that emotions are embedded into a sentence when people use consecutive punctuation marks or alphabetic character lengthening. They suggested an algorithm that detects unethical text by measuring the length of a sentence; average word length; number of punctuation marks; use of a period, question mark, or exclamation mark; number of repeated punctuation marks; and number of single alphabet tokens. However, this approach does not guarantee efective performance in terms of detecting malicious words.

Chen et al. [5] applied an algorithm that uses a morphological analyzer a method for protecting adolescents from unethical Youtube comments using n-grams, blacklists, and SVM classifiers based on supervised learning. They attempted to correct spelling and grammar mistakes in raw sentences. For instance, they delete meaningless symbols or repeated letters in words, split long words, transpose substituted letters, and replace incorrect or missing letters before the feature extraction. Then, they use 1,700 corrected words for the detection. However, we believe that this approach is not suitable for words that have been obfuscated intentionally such as F\*\*K, \$TUPID, and jack@\$\$, which are common forms of words found online.

Sintsova and Pu [27] used the Twitter hashtag as index data for an emotion analysis to avoid the problem of requiring a large amount of index data for supervised learning. However, while it is an interesting idea to use hashtag words as correct answer data for an emotion analysis, this data set is dificult to build because Twitter removes tweets with malicious hashtags as well as the accounts that created them.

mining the presence of cyberbullying. Their approach relies on word2vec and an expanded list of predefined insults. They assign diferent weights to obtain bullying features, which are then concatenated with a bag-of-words and latent semantic features to form the final representation. However, since the evaluation set is relatively small, the bag-of-words technique might not be efective in detecting obfuscated abusive text.

Nobata et al. [22] developed a supervised classification methodology with NLP features that outperforms a deep learning approach. Then they extended this feature set with additional features derived from distributional semantics techniques. The conventional features are blacklist lexicon-based a sentence. Then, the method checks whether or not the sequences include both user identifiers and ofensive words. Their algorithm identifies abusive documents based on the length of the sentence or the number of tokens. They also relied on word2vec and comment2vec, and conducted various experiments using Yahoo! finance and news data. Their experimental results showed improved performance over any previous approaches.

Table 1 summarizes the aforementioned.  
Table 1: Summary of Related Works

<table><tr><td>objective</td><td>ref.</td><td>methodology</td><td>data source</td><td>acc.</td><td>prec.</td><td>recall</td><td>f-score</td></tr><tr><td>spam word filtering</td><td>[10]</td><td>null-char removal, key disambiguation, phonetic transcription</td><td>authors e-mail</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td rowspan="4">sentiment analysis</td><td>[15]</td><td>three-way classification</td><td>tweets</td><td>85.7</td><td>85.3</td><td>82.2</td><td>78.7</td></tr><tr><td>[26]</td><td>multinomial NB, SVM, random forest classification</td><td>tweets</td><td>76.3</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>[2]</td><td>word length analysis</td><td>tweets</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>[18]</td><td>SVM, random forest classification</td><td>Facebook data</td><td>74</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td rowspan="5">abuse detection in social network messages</td><td>[30]</td><td>combination of CNN and GRU</td><td>tweets</td><td>n/a</td><td>n/a</td><td>n/a</td><td>89.6</td></tr><tr><td>[5]</td><td>n-grams, blacklists, SVM</td><td>Youtube comments</td><td>n/a</td><td>98.2</td><td>94.3</td><td>96.3</td></tr><tr><td>[27]</td><td>n-gram, point-wise mutual information</td><td>tweets</td><td>62</td><td>33</td><td>36.1</td><td>33.1</td></tr><tr><td>[29]</td><td>TF-IDF, n-grams, sentimental features, contextual features</td><td>Slashdot, Myspace</td><td>n/a</td><td>39.4</td><td>61.9</td><td>48.1</td></tr><tr><td>[31]</td><td>bag-of-words, word2vec, insulting word list</td><td>tweets</td><td>n/a</td><td>76.8</td><td>79.4</td><td>78</td></tr><tr><td rowspan="2">abuse detection in news comments</td><td>[22]</td><td>n-grams, blacklist, word2vec, comment2vec</td><td>Yahoo! news</td><td>n/a</td><td>82.7</td><td>82.5</td><td>82.6</td></tr><tr><td>[28]</td><td>edit-distance, SVM</td><td>news comments</td><td>93</td><td>62</td><td>64</td><td>63</td></tr></table>

While existing techniques guarantee a certain level of performance in detecting abusive words, improvements are still possible. For example, we can reduce positive errors by enhancing both the abusive and non-abusive word lists. We suggest a more eficient abuse-detection system based on an abusive word list and a non-abusive word list. It is well known in the literature that abusive and non-abusive word lists are the most crucial components of identifying abusive text. We construct these two lists using the word embedding of word2vec’s skip-gram and the cosine similarity between two word vectors. This helps to identify newly invented abusive words efectively. Then, we improve our system by detecting variants and intentional obfuscations of abusive words. To do so, we use eficient gadgets to classify abusive and non-abusive word lists based on blacklists, n-grams, editdistance metrics, mixed languages, abbreviations, punctuation, and words with special characters. We combine these gadgets with an unsupervised learning method and demonstrate its efectiveness by enhancing the abusive and non-abusive word lists. We then evaluate the performance of our system using real-world online messages and comments. Lastly, we show that our

## 3. Data

We build a spoken expression corpus of 10 million data by crawling comments on political and economics articles. We create an initial abusive word list of 7,450 words by combining Google’s bad-word list, a swear- and four-letter-word list, an ofensive/profane word list, profanity in the Korean language, banned words in online game and community site, and other abusive words in the related literature. We then construct a non-abusive word list containing 1.5 million words to reduce positive errors when classifying abusive text.

## 3.1. Corpus

There are many corpora in the world. Wikipedia contained about 1.46 million pages as of April 2017, according to Publishers Weekly, and there were about 674 million books sold in 2016<sup>5</sup>. Every day, 10 million news and blog articles are posted online. In addition, there are a great many spoken corpora online. We use both corpora—the spoken language corpus and the written language corpus—for our system. The spoken language corpus appears in conversation between people, and the written language corpus appears in documents such as newspaper articles or novels [1]. Because the spoken language corpus is a good source of new abusive words, we use this to enhance the abusive word list. We use the written language corpus, which seldom contains abusive words, to build the non-abusive word list. We use Wikipedia headwords and Namu-wiki documents to build the written language corpus.

We gather news article comments from political and economics articles. Such comments often include a relatively large number of malicious expressions owing to opposing opinions and the resultant intense debates [8]. We first crawl 100,000 NAVER<sup>6</sup> political and economics news articles from January 2013 to January 2017, collecting 10 million comments.

A recent study showed that there are about 100,000 malicious tweets posted every week on Twitter [31]. This makes Twitter a good source for testing the efectiveness of our abuse-detection system. As test data, we create three sets of 1,000 messages from news comments, Twitter, and a Korean web community site<sup>7</sup>, which allegedly includes a large amount of profanity. We later use this test data to show that our proposed system can detect abuse in not only news article comments, but in other domain data as well. In summary, we use 10 million news comments data for training, and evaluate our system using three sets (news comments, tweets, and online community comments) of data, each containing 1,000 items.

## 3.2. Word List

We construct an abusive word list by collecting available data from various sites, and create a database of 7,450 words after removing duplicates. The collection consists of Google’s bad-word list (550 words)<sup>8</sup>, a swear-word and four-letter-word list<sup>9</sup> (384 words), an ofensive/profane word list (1,383 words), profanity from the Korean language (1,857 words) [14], and banned words from online gaming sites<sup>10</sup> (3,211 words) and communities<sup>11</sup> (2,137 words). We then combine these lists, removing duplicate words, and obtain a list of 7,450 0 abusive words. Note that these lists are often ad-hoc and the origin of these lists.

Next, we construct a 1.5 million non-abusive word list to reduce the misclassification of abusive words. We regard all words in this list as nonabusive. However, because some words in this list might be abusive, we use a malicious word judgment (list filtering), which we explain later. For the nonabusive word list construction, we rely on Wikipedia headwords (692,798 Korean words, 1,791,795 English words), neologism (435 words) [21], and the titles of Namu-wiki documents (170,327 words)<sup>12</sup>.

## 4. Methodology

We now describe the overall system and each module used to determine abusive words as shown in Figure 1.

Our system is based on the unsupervised learning of abusive text with word embedding using word2vec’s skip-gram and the cosine similarity between two word vectors. In this step, we use the corpus data described in Section 3.1. The system also employs several eficient gadgets to filter abusive text based on blacklists [5, 22], n-grams [3, 4], edit-distance [17], mixed languages, abbreviations, punctuation, and words with special characters [2, 22] to detect intentionally obfuscated words. The system uses each gadget and the unsupervised learning module to identify abusive words in a document. Since a word can appear in a diferent obfuscated form, whenever a gadget identifies a word as abusive, we consider the word to be abusive. This is why we use several gadgets together. Later in the experiment section, we show the efectiveness of these combined gadgets. We check each word individually. If the input text contains one or more abusive words, then we conclude that the text is abusive. We use the word list data described in Section 3.2. These two modules run independently of each other as illustrated in Figure 1. When both modules decide that a word is abusive, we check whether or not the word is in the non-abusive word list; if it is, we treat the word as non-abusive. We run this procedure to minimize the occurrence of false positives. When the results from the unsupervised learning module and the detection gadgets are the same, we add the word to the abusive or non-abusive word lists, according to the unanimous results, a process called auto-tagging. When there is a discrepancy between the unsupervised learning and the detection gadgets, we ask human experts to judge the word based on the abusive word decision guidelines in Table 3, and then place the word in the corresponding list. This is called manual tagging.

![](/api/attachments/VAAFHWTQ/fulltext/images/7337af295457fdc2a20bfc395611432d9d72ef87856ae68eceea4b51df656ea8.jpg)  
Figure 1: Framework of Our System

## 4.1. Unsupervised Learning Process Module

In the training data preprocessing stage, we remove comments of more than 100 characters in length, because they are likely to be an article or an advertisement. Because word2vec’s bag-of-words distinguishes between uppercase and lowercase words, all capital letters are changed to lowercase letters. We remove articles and prepositions that are unnecessary in detecting abusive words, and remove all punctuation to avoid cases in which word2vec recognizes words containing punctuation as a bag-of-words. Partof-speech (POS) tagging is the process of tagging a word in a corpus to its corresponding part of speech and its relationship with adjacent and related words in a sentence. We observe that when people write a comment, the spacing is usually not maintained well. While people can read and understand a mis-spaced sentence, a system may not be able to detect abuse in such a sentence. For example, “youareabitch” is well understood by humans but the system may have dificulty detecting the abuse. POS tagging can resolve this type of problem and, thus, improve the performance of the unsupervised learning step. We use CMU ARK Twitter Part-of-Speech Tagger<sup>13</sup> for POS tagging.

We apply the word2vec [19, 20] module using the preprocessed data. Google introduced word2vec, which is an efective word-embedding tool. Based on a three-layer (input layer, hidden layer, output layer) neural network language model, word2vec learns vector representations for each word.

The word2vec skip-gram model predicts a window of words with respect to a given single word, and produces a word embedding by taking a large corpus as its input and producing a vector space with each unique word in the corpus being assigned a vector. For example, our word2vec module output is “my [0.003, -0.191, 0.083, . . . , 0.019, -0.075]” “love [-0.096, -0.103, 0.034, . . . , 0.030, 0.004]” or “damn [-0.108, -0.123, 0.060, . . . , 0.123, -0.107]”, where each word has a vector of 100 dimensions—we set this as the dimension size for the word2vec module because it guarantees good performance within a reasonable training time [11, 24]. We then compare two word vectors by their cosine similarity to discover new abusive words as follows: In our unsupervised learning process, we extract n (10 – 15) words that have a close cosine similarity to a target word in the documents. For instance, for the word is “A”, the word vector is [0.005, -0.121, 0.005, . . . , 0.251, 0.068] and n similar words—the top n words that have the largest cosine similarity values with respect to the word vector of A—such as [“you”, “love”, “fuck”, “your”, . . ., “damn”, “okay”]. Because there is an abusive word in the n word list, the module decides that A is abusive. Some non-abusive words may be misclassified as abusive words if they are frequently used with abusive words. These mis-classified words are later checked against the non-abusive word list, and if they are in the list, we reclassify them as non-abusive. If the target word is not in the blacklist nor in the non-abusive word list, but the word is very similar to an abusive word, then it is tagged as abusive. This is because the target word might be a never-before-seen malicious word, namely, a new abusive word, which occurs often online.

## 4.2. Abusive Word Detection Gadgets

## 4.2.1. Blacklist

The blacklist [5, 22] module compares words in the target document and the abusive word list constructed in Section 3.2. We implement this comparison process by storing all abusive words in a hashset, which is a set data structure based on a hash table. Note that a hashset does not allow the duplication of data and guarantees a constant time performance using a hash for basic operations such as add, remove, and contains. We store both the abusive word list and the non-abusive word list using the hashset. This helps to detect abusive words very fast in practice without considering the order of abusive words in the text. Without the hashset data structure, the pattern-matching step becomes extremely slow. We use a list of about 7,450 abusive words and the maximum length of the comments is 100. This implies that, without a hashset, we need a total of 225,000 searches, assuming a document has about 30 words. Using the hashset, we reduce the number of searches to about 30 (instead of 225,000).

## 4.2.2. N-Gram

The n-gram [3, 4] is a contiguous sequence of n items and is a popular technique for natural language processing. We employ a character n-gram, which gives all substrings of size n (uni-gram if n = 1, bi-gram if $n = 2$ , or tri-gram if n = 3, and so on) with spacing. Because our goal is to detect obfuscated abusive words, we do not preprocess or normalize the training and test data in an n-gram in order to find words that are not on the abusive word list. We also use a token bi-gram to detect abusive words of two or more words in length.

• you are a bitchild

• hey jack a\$\$... fu ck you once again it has been proven beyond a shadow of a doubt that your messiah is a lying fraud

For example, the 5-gram finds “bitch” from the first example and the token bi-gram finds “fu ck” from the second example.

## 4.2.3. Edit-Distance

The edit-distance measures the similarity between two words [12, 17]. The algorithm calculates the number of operations (e.g., character deletion, insertion, or substitution) to change one string into another. We employ the Levenshtein distance [17], which is the most common edit-distance algorithm. We obtain the edit-distance between a word in the text and an

The following is an example of the edit-distance output: dist(asshole, @ssh0le) = 2, dist(Fuck you, Fuck y0u) = 1, dist(Crap, Cr@p) = 1, dist(piss, pi55) = 2. If we set the distance threshold to one, then we tag only ‘Fuck y0u’ and ‘Cr@p’ as abusive because they have an edit-distance of 1 with respect to a known abusive word. If the threshold is set too large, then we have many false positives. Thus, we need to pick a proper value and our empirical study shows that a threshold of one is suficient. We use the editdistance method to detect obfuscated abusive words that are intentionally or unintentionally misspelled.

4.2.4. Mixed Languages, Abbreviations, Punctuation, and Special Characters

Brody and Diakopoulos [2] measured a text sentiment based on the length of the sentence, average word length, number of repetitive letters, the emotional lexicon. Nobata et al. [22] looked for inflammatory words and elements of non-abusive language, such as the use of polite words or modal verbs. They considered several features such as the length of a comment in tokens; average length of a word; number of punctuation marks; numbers of periods, question marks, quotation marks, and repeated punctuation; number of single letter tokens; number of capitalized letters; number of URLs; number of tokens with non-alphabet characters in the middle; number of discourse connectives; number of polite words; number of modal words (to measure hedging and confidence by the writer); number of unknown words as compared to a non-abusive word list of English words (meant to measure uniqueness and any misspellings); number of insults and hateful blacklisted words. We focus on abusive words that are deliberately expressed in terms of words from other languages, abbreviated words, and punctuation marks instead of abusive sentence judgments based on an emotion and linguistic analysis. It is rare to use malicious words mixed with other languages in English, but in Korean, Chinese, or Japanese, English is often mixed with a native language to express abuse.

The following are examples:

• mixed languages: 王八蛋 wang ba dan (Chinese swear word), <sup>야</sup> <sup>이</sup> sibal (Korean swear word), HENTAI 馬鹿 (Japanese swear word)

• abbreviated words: WTF (what the fuck), S.O.B. (son of a bitch)

• punctuation and special characters: K.I.L.L. you, d!a!mn

For the mixed language case, we begin with frequently used English abusive words in our abusive word list, to which we add new words that are not English and that were discovered by our word2vec module in the training step. The abbreviated words case is similar; we begin with known abbreviated abusive words in the list, to which we add new words discovered by the word2vec module. We remove all punctuation and special characters and check the resulting words (in our examples, “KILL you”, “damn”) with respect to our abusive and non-abusive word lists to determine abuse.

## 4.2.5. Filtering, Tagging, Enhancing List

We use the list filtering module to reduce the occurrence of false positive errors when non-abusive words are misidentified as being malicious. This is also why we keep a list of non-abusive words. If a word is misclassified as abusive and is in the non-abusive word list, then we immediately conclude that the word is non-abusive and terminate the tagging procedure.

If the unsupervised learning module and the detection gadgets provide is used to tag words based on the output of the system without human intervention.

If there is a discrepancy between the unsupervised learning module and the judgment of the detection gadgets, the corresponding text is stored separately. Then, later, a human expert determines whether text is abusive based on the guidelines in Table 3. If a discrepant word is determined to be abusive (or non-abusive) by a human expert, then it is added to the abusive (or non-abusive) word list. This is the manual tagging step. In our experiment, we ask three human experts to decide whether a word is abusive, and put a tagged word into the abusive word list only if at least two experts agree that it should be there. We enhance the abusive and nonabusive word lists by repeating the manual tagging step several times using the training data.

## 5. Experiments

We use precision and recall, which are standard measurements of system performance in the literature, to evaluate the experimental results. We rely on these metrics to compare our system with the previous approaches because there are no benchmark data available for such comparisons. We also use an f-score, which is the weighted harmonic mean of precision and recall, to evaluate our system.

Table 2: True Positive, False Positive, False Negative, and True Negative

<table><tr><td rowspan="2" colspan="2">division</td><td colspan="2">correct answer</td></tr><tr><td>abusive</td><td>non-abusive</td></tr><tr><td rowspan="2">predicted answer</td><td>abusive</td><td>true positive (TP)</td><td>false positive (FP)</td></tr><tr><td>non-abusive</td><td>false negative (FN)</td><td>true negative (TN)</td></tr></table>

• precision $\scriptstyle \left( { \frac { \mathrm { T P } } { \mathrm { T P + F P } } } \right.$ ): the ratio of identified words that are actually abusive

• recall $\scriptstyle ( { \frac { \mathrm { T P } } { \mathrm { T P } + \mathrm { F N } } } ) :$ the ratio of abusive words that are correctly identified

• f-score $( 2 \times { \frac { { \mathrm { p r e c i s i o n } } \times { \mathrm { r e c a l l } } } { { \mathrm { p r e c i s i o n } } + { \mathrm { r e c a l l } } } } )$ : the weighted harmonic mean of precision and recall

## 5.1. Evaluation Data Set

## 5.1.1. Abusive Word Guidelines

Before creating an evaluation data set, we first set up guidelines for abusive words in Table 3 based on the “Study on Guideline for Restoring Game Language” [6] by the Korea Game Industry Promotion Agency and the word annotation instructions of Nobata et al. [22] that classify sentences into several categories such as hate speech, derogatory statements, and profanity.

Table 3: Abusive Word Guidelines

<table><tr><td>(A) Violent expression1. Abusive2. Threat3. Other (including expressions that provoke or stimulate another person in the context of false expression</td></tr><tr><td>(B) Sexual expression1. Sexuality and related body language2. Sexual relatedness3. Other sexuality expressions that stimulate imagination or cause shame</td></tr><tr><td>(C) Discrimination1. Sex discrimination2. Age discrimination3. Others (racial and regional discrimination)</td></tr></table>

Table 4: Evaluation Data Sets

<table><tr><td rowspan="2"></td><td colspan="3">news article comments</td><td colspan="3">community comments</td><td colspan="3">Twitter</td></tr><tr><td>total</td><td>all agreed</td><td>2/3 agreed</td><td>total</td><td>all agreed</td><td>2/3 agreed</td><td>total</td><td>all agreed</td><td>2/3 agreed</td></tr><tr><td>total</td><td>1,000</td><td>883</td><td>117</td><td>1,000</td><td>874</td><td>126</td><td>1,000</td><td>960</td><td>40</td></tr><tr><td>non-abusive</td><td>599</td><td>614</td><td>19</td><td>599</td><td>551</td><td>48</td><td>661</td><td>633</td><td>25</td></tr><tr><td>abusive</td><td>401</td><td>269</td><td>98</td><td>401</td><td>323</td><td>78</td><td>339</td><td>327</td><td>15</td></tr><tr><td>Fleiss&#x27; kappa</td><td colspan="3">82.3 (almost perfect agreement)</td><td colspan="3">82.2 (almost perfect agreement)</td><td colspan="3">90.8 (almost perfect agreement)</td></tr></table>

## 5.1.2. Evaluation Data

We verify the efectiveness of our system after creating the following evaluation data: We first select 1,000 documents from crawled news article comments in the economics and political sections. As mentioned before, these comments often include opposing opinions, which users express using strong words, including ofensive and abusive expressions. We then ask three human raters who are trained to evaluate data sets according to the guidelines in Table 3 to evaluate all 1,000 documents.

In a similar manner, we select 1,000 comments from online community and 1,000 tweets from Twitter. We then ask three raters who are diferent from the raters of the news article comments. The reason for the crossdomain test is to run an experiment with diferent test data and to show the independence of the data set. These new raters evaluate the data set according to the same guidelines in Table 3.

Table 4 shows the distributions of the evaluation data. All data set’s Fleiss’ kappa values [9] (a statistical measure for assessing the reliability of agreement between a fixed number of raters) are over 80%—that is, all results are almost in perfect agreement. Thus, we confirm that the rater reliability is satisfactory.

## 5.2. Evaluation of News Article Comment Evaluation Data Set

We first evaluate the system using news article comment data. Table 5 shows the experimental results using the initial abusive word list and the initial non-abusive word list, which have not yet been enhanced by our system.

We evaluate the system using the data that all three raters agreed upon (all agreed), those agreed upon by two-thirds of the raters (2/3 agreed), and the sum of the two cases (total). In all cases, the experiment results do not show good performance with the initial lists. The “all agreed” and “2/3 agreed” cases show a similar performance in precision, but quite diferent recall scores. This is because there are a few cases that do not contain an explicit abusive word or that imply sarcasm in the “2/3 agreed” case, which can make it dificult for the system to detect abuse. We find a similar result for the f-score. Overall, this suggests that the initial lists are inefective in terms of identifying abuse and we need to enhance the lists for better performance.

Table 5: Initial Results for 1,000 News Article Comments Without Enhancing the Abusive and Non-Abusive Word Lists (%)

<table><tr><td rowspan="2">No.</td><td rowspan="2">module name</td><td colspan="3">total (1,000)</td><td colspan="3">all agreed (883)</td><td colspan="3">2/3 agreed (117)</td></tr><tr><td>precision</td><td>recall</td><td>f-score</td><td>precision</td><td>recall</td><td>f-score</td><td>precision</td><td>recall</td><td>f-score</td></tr><tr><td>M1</td><td>initial blacklist</td><td>77.52</td><td>56.50</td><td>65.36</td><td>77.31</td><td>62.08</td><td>68.87</td><td>78.57</td><td>38.82</td><td>51.97</td></tr><tr><td>M2</td><td>character 2-gram</td><td>44.68</td><td>83.05</td><td>58.10</td><td>40.80</td><td>86.61</td><td>55.47</td><td>70.11</td><td>71.76</td><td>70.93</td></tr><tr><td>M3</td><td>character 3-gram</td><td>45.56</td><td>78.24</td><td>57.59</td><td>41.71</td><td>81.41</td><td>55.16</td><td>69.88</td><td>68.23</td><td>69.04</td></tr><tr><td>M4</td><td>character 4-gram</td><td>51.05</td><td>68.07</td><td>58.35</td><td>48.02</td><td>72.12</td><td>57.65</td><td>69.12</td><td>55.29</td><td>61.43</td></tr><tr><td>M5</td><td>token 2-gram</td><td>69.34</td><td>56.21</td><td>62.09</td><td>68.33</td><td>60.97</td><td>64.44</td><td>74.46</td><td>41.17</td><td>53.03</td></tr><tr><td>M6</td><td>edit-distance</td><td>46.87</td><td>59.32</td><td>52.36</td><td>42.59</td><td>60.96</td><td>50.15</td><td>73.01</td><td>54.11</td><td>62.16</td></tr><tr><td>M7</td><td>mixed langs, abbreviation, punctuation, and special chars</td><td>77.52</td><td>56.50</td><td>65.36</td><td>77.31</td><td>62.08</td><td>68.87</td><td>78.57</td><td>38.82</td><td>51.97</td></tr><tr><td>M8</td><td>unsupervised learning module</td><td>87.16</td><td>36.44</td><td>51.39</td><td>87.70</td><td>39.78</td><td>54.73</td><td>84.62</td><td>25.88</td><td>39.64</td></tr></table>

Table 6: Experimental Results with the Enhanced Lists for News Article Comments (%)

<table><tr><td></td><td>total (1,000)</td><td>all agreed (883)</td><td>2/3 agreed (117)</td></tr><tr><td>precision</td><td>86.99 (39.72)</td><td>89.51 (34.69)</td><td>78.48 (73.08)</td></tr><tr><td>recall</td><td>85.02 (88.98)</td><td>88.84 (88.85)</td><td>72.94 (89.41)</td></tr><tr><td>f-score</td><td>86.00 (54.93)</td><td>89.17 (49.90)</td><td>75.60 (80.42)</td></tr><tr><td colspan="4">the score in parentheses is the initial result of M1 without the enhancement shown in Table 5</td></tr></table>

We enhance both the abusive and the non-abusive word lists using the manual tagging method described in Section 4.2.5. We then have an abusive word list of 5,456 words constructed by removing 2,835 words that are nonabusive from the original set of 7,450 and adding 927 newly detected abusive words. For the non-abusive word list, we have a list of 1,534,826 words. We remove eight words that are abusive from the initial non-abusive word list lists improve the system performance significantly as presented in Table 6. Table 6 shows an experimental result with the enhanced lists. We observe that the overall performance (f-score) is substantially improved in all cases compared with the initial experimental result.

Note that the experimental results for the “all agreed” case are better than those of the “2/3 agreed” case. This is because some of the evaluation owing to ambiguous meanings of the input text. For example, “You look like a pig” may or may not be abusive, depending on the context of the sentence. However, without explicit contextual information, human experts provide varying classifications. The context and semantic meaning of the text should be considered in future research. We believe that a list-based detection system is insuficient to tackle this problem.

Before concluding this section, note that in our training step, we use only 6.5% (64,300) of the training data to enhance the lists. Although more data may give rise to higher quality lists, this will require a significantly longer training time with no guarantee of better performance. We believe that it is crucial to enhance the lists using a small amount of data while guaranteeing a certain level of performance.

## 5.3. Evaluation of Tweets and Community Comments

We evaluate the performance of the proposed system using the evaluation data set of community comments (Fleiss’ kappa is 82.2%, almost perfect agreement) and tweets (Fleiss’ kappa is 90.8%, almost perfect agreement). Note that we use the same lists to evaluate the system as those used to evaluate the news article comments in Section 5.2. Table 7 shows the experimental results using the initial abusive word list and the initial non-abusive word list for the community data and Twitter data.

Table 7: Initial Results for Community Comments and Twitter Tweets (%)

<table><tr><td rowspan="2">Com.</td><td colspan="3">total (1,000)</td><td colspan="3">all agreed (874)</td><td colspan="3">2/3 agreed (126)</td></tr><tr><td>precision</td><td>recall</td><td>f-score</td><td>precision</td><td>recall</td><td>f-score</td><td>precision</td><td>recall</td><td>f-score</td></tr><tr><td>M1</td><td>83.74</td><td>77.06</td><td>80.26</td><td>83.86</td><td>82.04</td><td>82.94</td><td>83.02</td><td>56.41</td><td>67.18</td></tr><tr><td>M2</td><td>53.45</td><td>85.03</td><td>65.64</td><td>51.47</td><td>86.69</td><td>64.59</td><td>64.89</td><td>78.20</td><td>70.93</td></tr><tr><td>M3</td><td>54.17</td><td>76.05</td><td>63.28</td><td>51.88</td><td>76.78</td><td>61.92</td><td>67.06</td><td>73.08</td><td>69.94</td></tr><tr><td>M4</td><td>59.96</td><td>66.83</td><td>63.20</td><td>58.54</td><td>66.87</td><td>62.43</td><td>66.67</td><td>66.67</td><td>66.67</td></tr><tr><td>M5</td><td>78.64</td><td>72.56</td><td>75.49</td><td>78.23</td><td>76.78</td><td>77.50</td><td>81.13</td><td>55.12</td><td>65.65</td></tr><tr><td>M6</td><td>65.97</td><td>63.84</td><td>64.89</td><td>65.48</td><td>68.11</td><td>66.77</td><td>69.23</td><td>46.15</td><td>55.38</td></tr><tr><td>M7</td><td>83.74</td><td>77.06</td><td>80.26</td><td>83.86</td><td>82.04</td><td>82.94</td><td>83.02</td><td>56.41</td><td>67.18</td></tr><tr><td>M8</td><td>84.87</td><td>43.39</td><td>57.42</td><td>84.97</td><td>45.51</td><td>59.27</td><td>84.38</td><td>34.61</td><td>49.09</td></tr><tr><td rowspan="2">Twi.</td><td colspan="3">total (1,000)</td><td colspan="3">all agreed (960)</td><td colspan="3">2/3 agreed (40)</td></tr><tr><td>precision</td><td>recall</td><td>f-score</td><td>precision</td><td>recall</td><td>f-score</td><td>precision</td><td>recall</td><td>f-score</td></tr><tr><td>M1</td><td>65.06</td><td>83.33</td><td>73.07</td><td>65.59</td><td>84.40</td><td>73.80</td><td>52.94</td><td>60.00</td><td>56.25</td></tr><tr><td>M2</td><td>36.97</td><td>95.90</td><td>53.37</td><td>36.81</td><td>96.02</td><td>53.22</td><td>41.17</td><td>93.33</td><td>57.14</td></tr><tr><td>M3</td><td>36.84</td><td>92.10</td><td>52.63</td><td>36.73</td><td>92.35</td><td>52.56</td><td>39.39</td><td>86.67</td><td>54.16</td></tr><tr><td>M4</td><td>40.80</td><td>86.25</td><td>55.39</td><td>40.78</td><td>86.54</td><td>55.44</td><td>41.38</td><td>80.00</td><td>54.54</td></tr><tr><td>M5</td><td>61.15</td><td>84.21</td><td>70.85</td><td>61.73</td><td>85.32</td><td>71.63</td><td>47.37</td><td>60.00</td><td>52.94</td></tr><tr><td>M6</td><td>61.15</td><td>84.21</td><td>70.85</td><td>61.72</td><td>85.32</td><td>71.63</td><td>47.37</td><td>60.00</td><td>52.94</td></tr><tr><td>M7</td><td>65.82</td><td>83.33</td><td>73.55</td><td>66.19</td><td>84.40</td><td>74.19</td><td>56.25</td><td>60.00</td><td>58.06</td></tr><tr><td>M8</td><td>83.40</td><td>55.85</td><td>66.90</td><td>83.48</td><td>57.19</td><td>67.88</td><td>80.00</td><td>26.67</td><td>40.00</td></tr></table>

Table 8 shows the experimental results with the enhanced lists.

Table 8: Experimental Results with Enhanced Lists for Community Comments and Tweets (%)

<table><tr><td rowspan="2"></td><td colspan="3">community comments</td><td colspan="3">Twitter</td></tr><tr><td>total(1,000)</td><td>all agreed(874)</td><td>2/3 agreed(126)</td><td>total(1,000)</td><td>all agreed(960)</td><td>2/3 agreed(40)</td></tr><tr><td>precision</td><td>89.97</td><td>90.81</td><td>85.18</td><td>90.85</td><td>92.49</td><td>58.82</td></tr><tr><td>recall</td><td>80.54</td><td>85.75</td><td>58.97</td><td>92.98</td><td>94.18</td><td>66.66</td></tr><tr><td>f-score</td><td>85.00</td><td>88.21</td><td>69.69</td><td>91.90</td><td>93.33</td><td>62.50</td></tr></table>

We show that the enhanced lists are still very efective for these two sets. In particular, the online community comments are not used in training, indicating that the lists are domain independent. For the initial experiments without the list enhancement shown in Table 7, the online community results outperform the news article comments in Table 5 and the Twitter results show similar or lower performance. For the experiments after the list enhancement shown in Table 8, the online community results show similar performance to those of the news article comments in Table 6. The Twitter results improve because most abusive tweets contain explicit abusive words, which both the human experts and our system classify successfully. Overall, the experimental results in Table 8 confirm that our enhanced abusive and non-abusive word lists are very efective in terms of detecting abusive text across diferent domains.

## 5.4. Diferent Combinations of Gadgets

We further consider diferent combinations of our detection gadgets in Section 4.2 and their performance. Table 9 shows the experimental results for diferent combinations of gadgets: M1 (blacklist), M5 (n-gram), M6 (editdistance), M7 (mixed languages, abbreviations, punctuation, and special characters). In all cases, the combination of all four modules shows the best performance. This is the overall performance of our system.

Table 9: Experimental Results for Diferent Combinations of Modules (%)

<table><tr><td>data source</td><td>combined modules</td><td>precision</td><td>recall</td><td>f-score</td></tr><tr><td rowspan="4">news article comments</td><td>M1+M5+M6</td><td>93.77</td><td>80.79</td><td>86.80</td></tr><tr><td>M1+M6+M7</td><td>90.03</td><td>81.64</td><td>85.63</td></tr><tr><td>M1+M5+M7</td><td>94.08</td><td>80.79</td><td>86.93</td></tr><tr><td>M1+M5+M6+M7</td><td>94.08</td><td>80.79</td><td>86.93</td></tr><tr><td rowspan="4">community comments</td><td>M1+M5+M6</td><td>82.00</td><td>84.04</td><td>83.00</td></tr><tr><td>M1+M6+M7</td><td>86.74</td><td>81.55</td><td>84.06</td></tr><tr><td>M1+M5+M7</td><td>89.47</td><td>80.55</td><td>84.78</td></tr><tr><td>M1+M5+M6+M7</td><td>89.97</td><td>80.55</td><td>85.00</td></tr><tr><td rowspan="4">Twitter</td><td>M1+M5+M6</td><td>90.08</td><td>92.98</td><td>91.51</td></tr><tr><td>M1+M6+M7</td><td>82.99</td><td>94.15</td><td>88.22</td></tr><tr><td>M1+M5+M7</td><td>90.65</td><td>93.57</td><td>92.09</td></tr><tr><td>M1+M5+M6+M7</td><td>90.65</td><td>93.57</td><td>92.09</td></tr></table>

The results in Table 9 suggest that it is better to utilize all possible detection gadgets, because each identifies an abusive word in a diferent way. There are always new types of abusive words appearing online, and, thus, future work can add further useful gadgets and improve the system performance.

We also compare our approach to a current state-of-the art approach [22]. Since it is not possible to compare them directly, we reproduce the approach of Nobata et al. [22], which uses an abusive word list, n-gram, and unsupervised module, to evaluate its performance using our data. Table 10 shows the comparison results, verifying that our approach is better in all cases.

Table 10: Performance Comparison between Nobata et al. [22] and the Proposed Method (%)

<table><tr><td rowspan="2">data source</td><td colspan="3">Nobata et al.</td><td colspan="3">our approach</td></tr><tr><td>precision</td><td>recall</td><td>f-score</td><td>precision</td><td>recall</td><td>f-score</td></tr><tr><td>news article comments</td><td>77.52</td><td>56.50</td><td>65.36</td><td>94.08</td><td>80.79</td><td>86.93</td></tr><tr><td>community comments</td><td>83.74</td><td>77.06</td><td>80.26</td><td>89.97</td><td>80.55</td><td>85.00</td></tr><tr><td>Twitter</td><td>65.07</td><td>83.33</td><td>73.08</td><td>90.65</td><td>93.57</td><td>92.09</td></tr></table>

Overall, our system outperforms all of the previous approaches lists in Table 1 in terms of precision, recall, and f-score.

## 6. Conclusions

We have proposed an abusive text detection system based on an enhancement of abusive and non-abusive word lists. There have been several attempts in the literature to detect abusive text online. Two noteworthy studies are those of Zhao et al. [31] and Nobata et al. [22]. We have observed that these previous approaches cannot handle newly-invented abusive words and obfuscated abusive words at the same time. This led us to design an abuse-detection system that can tackle both types of abusive words efectively. We noticed that it is necessary to have a good abusive word list in order to identify abusive text efectively. In addition, we also need a good non-abusive word list to reduce the incidence of false positives. Therefore, we have begun with known abusive and non-abusive word lists, which the system then enhanced.

## 6.1. Theoretical and Methodological Implications

We built a corpus of 10 million spoken expressions to detect slang and abusive words in web community sites, online news comments, and tweets. Our initial abusive word list was taken from existing lists, consisting of about 7,450 words. The initial non-abusive word list was constructed from Wikipedia headwords and dictionary words, and consisted of about 1.5 million words.

Our system has two types of modules that it uses to determine abusive text. The first type is an unsupervised module based on word2vec. This module works in a similar to that of Zhao et al. [31], but we consider 10 million inputs whereas they only considered 1,762 inputs. We use this module to discover newly invented abusive words that do not resemble any known abusive words. The second type is based on several gadgets used to filter malicious comments, such as blacklists, n-grams, the edit-distance, mixed languages, abbreviations, punctuation, and special characters. This module helps to identify obfuscated words from existing abusive words. We rely on these modules to identify abusive text.

It is essential that an abusive text detection system has good abusive and non-abusive word lists. Several existing approaches rely on these lists for abuse detection. We have designed an algorithm to enhance the lists based on the word2vec module and a few decision modules, and shown the efectiveness of the proposed algorithm. We believe that our algorithm is useful for detecting new abusive words that are either a newly invented words or obfuscated versions of previously known abusive words, both of which appear frequently on the Internet.

## 6.2. Practical Implications

Using an unsupervised learning module and several gadgets, our system enhanced the abusive and non-abusive word lists. Then, using the enhanced lists, the system showed a precision of 94.08%, a recall of 80.79%, and an f-score of 86.93% for the news comment data. We have also evaluated the performance of the proposed system using other domain data, namely, community comments and Twitter. For the community comments, the system showed similar performance, with a precision of 89.97%, a recall of 80.55%, and an f-score of 85.00%. For Twitter, the system showed better performance, with a precision of 90.65%, a recall of 93.57%, and an f-score of 92.09%. This is because most abusive tweets contain explicit abusive words

We think it is crucial to minimize human intervention when maintaining the word lists since there are always new words appearing on the Internet. On the other hand, we also think that we cannot let the system enhance the lists by itself, because there are several ways of fooling the system. Therefore, it is important to have some human intervention when enhancing the lists, but this should be minimized while keeping the system performance. Our approach achieves this goal by deploying several detection gadgets and a learning module in order to decide the abusiveness of text eficiently. In addition, we use manual tagging for words that the system cannot classify in order to improve the overall performance of the system.

## 6.3. Limitations and Future Directions

The proposed system efectively detects abusive text when the input text contains an abusive word (even in an obfuscated form) based on the abusive and non-abusive word lists. On the other hand, the system cannot detect an abusive nuance or a sarcastic expression in text since our approach is based on word lists. For the same reason, our system does not efectively identify new abusive words that are not similar to known abusive words. However, if people use a new abusive word together with a known abusive word in comments or conversations, the system will identify the new word using the improve the system by having it discover new abusive words more quickly.

Another open problem is to devise a system that can detect contextbased abuse in sentences, paragraphs, or documents. The proposed system does not detect such abusive expressions well. Nevertheless, we believe that abusive word detection is the first step toward context-based abuse. We expect that the essential ideas are similar in the sense that we need to

An immediate future work is to improve the system performance by further enhancing the abusive and non-abusive word lists. We will also use additional gadgets to identify abusive text since there are always new types appearing online. In addition, we plan to evaluate the system using data sets from other domains to further confirm the domain-independence of the proposed system. We also need to evaluate the performance of the system for longer text such as documents or articles on social networks by considering the abusive word frequency or the weight of abuse. Another interesting line of future work is to consider the trade-of between the number of initial training data items and the system performance. We will also explore how the proposed system can be used to detect abusive nuance or sarcastic expressions that cannot be detected by the current approach. Furthermore, it will be interesting to categorize abusive words and to use weights to calculate the abusiveness of input text.

## Acknowledgements

We thank the referees for their careful reading of an earlier version of the paper and their many useful suggestions.

This work was supported by the Institute for Information & Communications Technology Promotion (IITP) grant funded by the Korea government (MSIP) (R0124-16-0002, Emotional Intelligence Technology to Infer Human Emotion and Carry on Dialogue Accordingly).

[1] D. Biber, S. Conrad, R. Reppen, Corpus Linguistics: Investigating Language Structure and Use, Cambridge University Press, 1998.

[2] S. Brody, N. Diakopoulos, Cooooooooooooooollllllllllllll!!!!!!!!!!!!!! using word lengthening to detect sentiment in microblogs, in: Proceedings of the 2011 Conference on Empirical Methods in Natural Language Processing, pp. 562–570.

[3] P.F. Brown, P.V. deSouza, R.L. Mercer, V.J.D. Pietra, J.C. Lai, Classbased n-gram models of natural language, Computational Linguistics 18 (1992) 467–479.

[4] W.B. Cavnar, J.M. Trenkle, N-gram-based text categorization, in: In Proceedings of SDAIR-94, 3rd Annual Symposium on Document Analysis and Information Retrieval, pp. 161–175.

[5] Y. Chen, Y. Zhou, S. Zhu, H. Xu, Detecting ofensive language in social media to protect adolescent online safety, in: Proceedings of the 2012 International Conference on Privacy, Security, Risk and Trust, pp. 71– 80.

[6] K.N. Choi, Study on Guideline for Restoring Game Language, Korea Game Industry Promotion Agency, 2009.

[7] W. Chung, H. Chen, W. Chang, S. Chou, Fighting cybercrime: a review and the Taiwan experience, Decision Support Systems 41 (2006) 669– 682.

[8] N. Diakopoulos, M. Naaman, Towards quality discourse in online news comments, in: Proceedings of the 2011 ACM Conference on Computer Supported Cooperative Work, pp. 133–142.

[9] J.L. Fleiss, J. Cohen, The equivalence of weighted kappa and the intraclass correlation coeficient as measures of reliability, Educational and Psychological Measurement 33 (1973) 613–619.

[10] V. Freschi, A. Seraghiti, A. Bogliolo, Filtering obfuscated email spam by means of phonetic string matching, in: Advances in Information Retrieval, pp. 505–509.

[11] Y. Goldberg, A primer on neural network models for natural language processing, Journal of Artificial Intelligence Research 57 (2016) 345– 420.

[12] R. Hamming, Error detecting and error correcting codes, Bell System Techincal Journal 29 (1950) 147–160.

[13] P. Hayati, V. Potdar, Evaluation of spam detection and prevention frameworks for email and image spam: A state of art, in: Proceedings of the 10th International Conference on Information Integration and Web-based Applications & Services, pp. 520–527.

[14] K.H. Jang, 2014 Neologism, The National Institute of The Korean Language, 2011.

[15] F.H. Khan, S. Bashir, U. Qamar, TOM: Twitter opinion mining frame-(2014) 245–257.

[16] S. Lee, H. Kim, Why people post benevolent and malicious comments online, Communications of the ACM 58 (2015) 74–79.

[17] V. Levenshtein, Binary codes capable of correcting deletions, insertions and reversals, Soviet Physics Doklady 10 (1966) 707–710.

[18] M. Meire, M. Ballings, D.V. den Poel, The added value of auxiliary data in sentiment analysis of Facebook posts, Decision Support Systems 89 (2016) 98–112.

[19] T. Mikolov, K. Chen, G. Corrado, J. Dean, Eficient estimation of word representations in vector space, CoRR abs/1301.3781 (2013).

[20] T. Mikolov, I. Sutskever, K. Chen, G.S. Corrado, J. Dean, Distributed representations of words and phrases and their compositionality, in: Proceedings of the 27th Annual Conference on Neural Information Processing Systems, pp. 3111–3119.

[21] G.I. Nam, Youth Language Status Language Consciousness National Survey, The National Institute of The Korean Language, 2014.

[22] C. Nobata, J.R. Tetreault, A. Thomas, Y. Mehdad, Y. Chang, Abusive language detection in online user content, in: Proceedings of the 25th International Conference on World Wide Web, pp. 145–153.

[23] S.G. Paik, 2014 Cyber Violence Survey, Korea Broadcasting Commission, Korea Internet and Security Agency, 2014.

[24] J. Pennington, R. Socher, C.D. Manning, GloVe: Global vectors for word representation, in: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 1532– 1543.

[25] A. Schmidt, M. Wiegand, A survey on hate speech detection using natural language processing, in: Proceedings of the Fifth International Workshop on Natural Language Processing for Social Media, pp. 1–10.

[26] N.F.F. da Silva, E.R. Hruschka, E.R. Hruschka, Jr., Tweet sentiment analysis with classifier ensembles, Decision Support Systems 66 (2014) 170–179.

[27] V. Sintsova, P. Pu, Dystemo: Distant supervision method for multicategory emotion recognition in tweets, ACM ACM Transactions on Intelligent Systems and Technology 8 (2016) 13:1–13:22.

[28] S.O. Sood, J. Antin, E.F. Churchill, Using crowdsourcing to improve profanity detection, in: Proceedings of Proceedings of AAAI Spring Symposium: Wisdom of the Crowd.

[29] D. Yin, Z. Xue, L. Hong, B.D. Davison, L. Edwards, Detection of hathe WEB 2.0, pp. 69–74.

[30] Z. Zhang, D. Robinson, J. Tepper, Detecting hate speech on Twitter using a convolution-GRU based deep neural network, in: Proceedings of the 15th Extended Semantic Web Conference (ESWC 2018). Accepted.

[31] R. Zhao, A. Zhou, K. Mao, Automatic detection of cyberbullying on social networks based on bullying features, in: Proceedings of the 17th International Conference on Distributed Computing and Networking, pp. 43:1–43:6.

## Biography

![](/api/attachments/VAAFHWTQ/fulltext/images/ec8e3d020724b027b5872bdbb30020747d62cb334b9eb14bef6d14d8bd1cee8e.jpg)

Ho-Suk Lee is a Master student in the Department of Computer Science at Yonsei University. His research interests include information retrieval and abusive detection systems.

![](/api/attachments/VAAFHWTQ/fulltext/images/97cad455b003c955c010c502cc1520279000f4b354609d919b4dccb15bb5fd69.jpg)

Hong-Rae Lee is a Ph.D. student in the Department of Computer Science at Yonsei University. His research interests include data analysis, information retrieval and efficient algorithm designs.

![](/api/attachments/VAAFHWTQ/fulltext/images/be268caad2f9d2a26be08260da1ecbce01bb4fef8803e8979727e20b8f7abab2.jpg)

Jun-U Park is a Master student in the Department of Computer Science at Yonsei University. His research interests include information retrieval using AI and abusive detection systems.

![](/api/attachments/VAAFHWTQ/fulltext/images/96b60e2ae59607578e5c30ffd2c66fbd8feb7563f91ca93393998a662ea4cc4c.jpg)

Yo-Sub Han obtained his Ph.D. in computer science from the Hong Kong University of Science and Technology in 2006. He worked as a researcher in Korea Institute of Science and Technology until 2009. He joined Yonsei University in 2009 and is now an associate professor in the Department of Computer Science. His research interests include formal language theory,

algorithm design and information retrieval.

## Highlights

 We enhance abusive and non-abusive word lists based on learning algorithms and gadgets.

 We design an effective abusive text detection system using both word lists.

 We evaluate the system using real-world data and show its effectiveness.

##

![](/api/attachments/VAAFHWTQ/fulltext/images/15de72d607edca9c7c35fdcaeb3345a2e5cbcdc367ab255dfc255cf96e6b399e.jpg)

##

##

##

##

##

##
