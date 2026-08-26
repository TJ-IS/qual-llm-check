---
otero_id: 6972
otero_key: "K3ZTFHXP"
title: "Stock market sentiment lexicon acquisition using microblogging data and statistical measures"
authors: "Nuno Oliveira; Paulo Cortez; Nelson Areal"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.02.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Stock market sentiment lexicon acquisition using microblogging data and statistical measures

Nuno Oliveira<sup>a,</sup>\*, Paulo Cortez<sup>a</sup>, Nelson Areal<sup>b</sup>

<sup>a</sup>ALGORITMI Centre, Department of Information Systems, University of Minho, 4804-533 Guimarães, Portuga <sup>b</sup>School of Economics and Management, Department of Management, University of Minho, 4710-057 Braga, Portugal

A R T I C L E I N F O

Article history: Received 1 June 2015 Received in revised form 1 February 2016 Accepted 27 February 2016 Available online xxxx

Keywords: Sentiment analysis Stock market Microblogging data

## A B S T R A C T

Lexicon acquisition is a key issue for sentiment analysis. This paper presents a novel and fast approach for creating stock market lexicons. The approach is based on statistical measures applied over a vast set of labeled messages from StockTwits, which is a specialized stock market microblog. We compare three adaptations of statistical measures, such as Pointwise Mutual Information (PMI), two new complementary statistics and the use of sentiment scores for affirmative and negated contexts. Using StockTwits, we show that the new lexicons are competitive for measuring investor sentiment when compared with six popular lexicons. We also applied a lexicon to easily produce Twitter investor sentiment indicators and analyzed their correlation with survey sentiment indexes. The new microblogging indicators have a moderate correlation with popular Investors Intelligence (II) and American Association of Individual Investors (AAII) indicators. Thus, the new microblogging approach can be used alternatively to traditional survey indicators with advantages (e.g., cheaper creation, higher frequencies).

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Recently, social media (e.g., Twitter, Facebook, message boards) has enabled a burst of unstructured opinion content that is potentially valuable for diverse decision-making processes [1]. Due to the volume and velocity properties of social media data, human analysis is impracticable and thus sentiment analysis (SA) is used to automatically mine large amounts of opinionated contents in order to summarize the opinions [2]. Several SA approaches apply common supervised classifiers such as Support Vector Machines [3], Naive Bayes [4] or ensembles [5,6]. Yet, the utilization of sentiment lexicons allows unsupervised classification of text, relieving the need for arduous manual labeling of text. Moreover, sentiment lexicons permit the creation of important features for supervised SA [7]. The sentiment lexicon is a list of words with a sentiment value (e.g., positive, negative) and it is considered a key element for SA [8]. For example, the sentence “this car is great” can be easily detected as positive if the lexicon has a term “great” with a positive value.

SA is being increasingly used to predict stock market variables [9–12]. In particular, microblogging data are a useful source for supporting stock market decisions [13,14]. Users post very frequently and data are readily available at low cost, allowing real-time assessment that can be exploited during the trading day. However, there has been little effort in producing lexicons adapted to the financial domain and microblogs. A financial lexicon was manually built by Loughran and McDonald [15] using text documents extracted from the U.S. Securities and Exchange Commission portal from 1994 to 2008. Mao et al. [16] proposed a procedure to automatically construct a Chinese financial lexicon by exploring a large news corpus classified as positive or negative according to the contemporaneous stock returns. Yet, these lexicons did not consider microblog messages, which is often informal and has character constraints. Furthermore, adopting a manual approach (e.g., [15]) is not feasible in practical terms given the huge effort required to label the large volumes of microblog texts. Moreover, the existing domain independent lexicons (e.g., [17–19]) may be ineffective for stock market contents. For instance, the word “explosive” is negative in most contexts but it may be positive in financial messages (e.g., “explosive rise”).

In this work, we present a novel automated approach for the acquisition of microblog stock market lexicons. Our main contributions are:

i) The adaptation of three statistical measures (e.g., pointwise mutual information) and creation of two new complementary statistics. These measures are applied in labeled messages of the StockTwits microblogging service to calculate a stock market sentiment score. To address negation more eficiently, sentiment scores are also created for afirmative and negated contexts.

ii) The comparison of the resulting stock market lexicons with six large popular lexical resources: Harvard General Inquirer (GI) [17], opinion lexicon (OL) [2], Macquarie Semantic Orientation Lexicon (MSOL) [20], MPQA subjectivity lexicon (MPQA) [18], SentiWordNet (SWN) 3.0 [19] and financial sentiment dictionaries (FIN) [15].

iii) The assessment of the information content of sentiment indicators produced with a created and a baseline lexicons using a different microblog data source (Twitter). The new Twitter sentiment indicators are correlated with two traditional survey sentiment indicators: Investors Intelligence (II) and American Association of Individual Investors (AAII).

This paper is structured as follows. Section 2 shows related work. Section 3 presents the microblogging data, lexicon methods and sentiment indicators. Section 4 describes the experiments conducted and analyzes the obtained results. Finally, conclusions are drawn in Section 5.

## 2. Related work

The sentiment lexicon is considered a key element for SA [8]. The utilization of lexicons permits the execution of effective unsupervised approaches [21,22] and provides high quality features for supervised SA [7,23]. Moreover, lexicons can be applied to diverse tasks such as SA, opinion retrieval [24] or opinion question answering and summarization [25], and they can be applied to diverse domains such as stock markets [15], electronic products [2] or the movie industry [26].

The creation of opinion lexicons is an important topic that has been studied for some time under two main approaches: manual and automatic creations. Manual creation is the most labor intensive and expensive approach because it requires experts to manually classify the sentiment value of each term. MPQA subjectivity lexicons [18] and General Inquirer [17] are two important examples of this methodology. Automatic creation requires much less human effort and allows for the faster inclusion of a larger set of lexical items. However, this is often achieved at the expense of accuracy.

There is substantial literature about the automatic construction of lexicons. Many of these studies apply text corpora for this procedure. Hatzivassiloglou and McKeown [27] extracted conjoined adjectives from a large Wall Street Journal corpus and produced a list of adjectives labeled as positive or negative. Using an initial set of adjectives with predetermined orientation labels, they developed a supervised learning algorithm to assign the sentiment polarity. First, they applied a log-linear regression model to determine if each pair of conjoined adjectives had the same or different orientations. Then, a clustering algorithm was used to divide the adjectives into two different positive and negative sets. Wiebe [28] extracted subjective adjectives from corpora by applying a method for clustering words based on distributional similarity [29] and another method to compute polarity and gradability [27]. Turney and Littman [21] tested two co-occurrence measures, Pointwise Mutual Information (PMI) and Latent Semantic Analysis (LSA), on the AltaVista Advanced Search engine in order to assign a semantic orientation to each word. The most accurate approach calculated the PMI of each term with pre-classified positive and negative words. A term was considered positive if the sum of its PMI scores with positive words was greater than the total PMI score with negative words, and vice-versa. Qiu et al. [30] explored diverse syntactic relations between opinion words and targets to iteratively extract further opinion words and targets. An initial seed set of opinion words was expanded and opinion targets were collected by continuously identifying terms having those syntactic associations with already extracted terms. Kiritchenko et al. [3] generated lexicons from tweets containing specific hashtag words and emoticons. These symbols were used as signals of the message sentiment (positive or negative). The sentiment score of each term was calculated using the PMI measures with positive and negative messages. These authors also produced distinct scores for negated and non-negated segments to properly obtain the sentiment in these contexts.

Lexical databases and thesaurus are also extensively applied in the creation of opinion lexicons. Kamps et al. [31] calculated the synonymy shortest path on the WordNet database (http://wordnet. princeton.edu) of adjectives to the words “good“ and “bad” and determined their sentiment orientation based on these values. Kim and Hovy [32] created a system that automatically extracts holders and sentiment of each opinion about a given topic. This system includes a module for computing word sentiment. Synonymy and antonymy relations from WordNet are applied in this module in order to expand a small set of seed words and to calculate the strength of sentiment polarity. Esuli and Sebastiani [33] applied text classification techniques to the glosses of subjective words in order to determine their sentiment polarity. Mohammad et al. [20] produced a large lexicon using a set of afix patterns and the Macquarie thesaurus. The sentiment of every thesaurus paragraph was classified using a set of positive and negative words collected utilizing afix patterns. Then, each lexical item assumed the most common sentiment label of paragraphs containing the respective term. Baccianella et al. [19] produced the SentiWordNet lexicon by automatically calculating sentiment values to all WordNet synsets. First, these synsets were classified by a group of classifiers trained with preclassified synsets. The different classification results were combined to generate a sentiment score to each synset. In a second phase, two iterative random-walk procedures were executed for the positivity and negativity values. These processes applied a graph with directed links from synsets included in glosses of other synsets. The random walk phase began with the values created in the previous step and finished when the processes had converged. Neviarouskaya et al. [34] created a lexicon by expanding an initial set of lexicon entries through synonymy, antonymy and hyponymy relations, derivation and compounding.

Other works explore both text corpora and lexical databases. Hu and Liu [2] utilized consumer reviews and Wordnet to select and classify opinion words associated to frequent product attributes. First, they extracted all adjectives included in the sentences of consumer reviews mentioning those product features. The sentiment orientation was assigned according to their semantic association in Wordnet with a seed list of words with known sentiment orientation. Each adjective assumed the same sentiment of synonyms or the inverse polarity of antonyms. The seed list was iteratively expanded with these newly classified words until no further words had antonyms or synonyms in the list. Takamura et al. [35] proposed the utilization of a spin model, where each word had a sentiment polarity (positive or negative), to produce an opinion lexicon. They created a lexical network based on the occurrence of terms in glosses of other terms, the synonymy, antonymy and hypernymy relations in thesaurus and some conjunctive expressions in corpus. Then, the mean-field method was applied on the network to determine the semantic orientations. Lu et al. [36] automatically generated a context-dependent sentiment lexicon by combining the utilization of domain independent lexicons, sentiment ratings of reviews, synonym and antonym relations in Wordnet and linguistic rules.

The utilization of generic lexicons or lexicons associated to other domains may be ineffective to SA on stock market text because sentiment is sensitive to the domain [21]. For example, the verb “underestimate” has often a negative sentiment but an underestimated stock can constitute an opportunity to buy, thus denoting a positive value within the stock market domain. However, the creation of opinion lexicons for the financial domain has been scant. One of the most popular works in this context is by Loughran and McDonald [15], who manually created six word lists (i.e., positive, negative, litigious, uncertainty, modal strong and modal weak) from words occurring in at least 5% of a large collection of 10,000 documents between 1994 and 2008. Also in 2014, Mao et al. [16] presented a procedure to automatically produce a Chinese financial lexicon. A large Chinese news corpus was labeled according to the stock returns. Then, a set of seed words was selected based on the Document Frequency value with news associated with very high or very low returns. The lexicon was expanded by considering the statistical association with seed words and the economic significance of candidate terms. The final lexicon was obtained by an iterative optimization process.

In summary, the majority of the studies applies text corpora (e.g., [2,3,16,27,28,30,35]) and/or existing lexical databases and thesaurus (e.g., [2,19,20,26,31–35,37]). The extraction of opinion words or targets is mainly based on syntactic relations (e.g., [27,30]), part of speech (e.g., adjectives [2,27,28]), co-occurrence with terms (e.g., [2]) and semantic relations in WordNet (e.g., [32,34]). The calculation of the sentiment polarity or score is mostly performed by statistical measures (e.g., PMI [3,21]), text classification of glosses (e.g., [19,20,33]), semantic associations (e.g., synonymy, antonymy relations in WordNet [2,31,32,34] ), syntactic relations (e.g., [30]) and clustering methods (e.g., [27,28]). Only one study produced different sentiment scores for afirmative and negated contexts [3], although applied for generic Twitter messages and thus not specifically adjusted to the stock market domain, as performed in this paper. Some of these studies extract and classify opinions words simultaneously by iteratively expanding a pre-labeled seed list by semantic or syntactic relations (e.g., [2,30]). The newly collected words assume the same or the opposite polarity of the associated term.

Some of these approaches are ineffective for the creation of specialized domain lexicons. Methods based on WordNet or thesaurus produce domain independent lexicons, possibly unadjusted for stock market contents [38]. Therefore, the utilization of methods such as semantic relations in WordNet and text classification of glosses is unsatisfactory for our purpose. The usage of a small group of syntactic relations (e.g., conjunctions [27,35] ) does not allow for the selection of a large set of words. Moreover, extracting only adjectives (e.g., [2,27,31]) ignores terms with a strong sentiment, such as “love“ and “hate” verbs. In addition, the expansion of a seed list of classified words (e.g., [30]) is less effective than the application of classified text corpora. Since we have classified data exclusively about stock markets, we do not need to restrict the collection to words co-occurring with specific terms (e.g., [2]) and clustering methods (e.g., [27,28]) become less relevant to assign sentiment polarity.

In this work, we propose a novel automated approach for the creation of microblog stock market lexicons. Three adaptations (e.g., PMI) and two new proposed statistics were applied in a large data set of classified data provided by a microblogging platform exclusively dedicated to stock markets (http://stocktwits.com). We believe this is the largest labeled data set used in the creation of stock market lexicons. Additionally, sentiment scores were created for afirmative and negated contexts in order to address negation properly. Within our knowledge, this work presents the first stock market lexicons with two different context scores for each entry.

## 3. Material and methods

## 3.1. Microblogging data

Microblogging data are useful for the creation of investor sentiment indicators. The community of investors using these services is growing and becoming more representative. The character limit demands greater objectivity. Microblogging users usually react promptly to events, allowing a near real-time sentiment assessment. Data is quite vast and freely available allowing a more frequent production of indicators than traditional sources, such as extensive surveys. The selection of messages containing cashtags reduces the amount of irrelevant data and permits the creation of sentiment indicators related to particular stocks. A cashtag is composed by a ”\$” character and a stock ticker (e.g., \$AAPL) and it is usually applied in messages about that stock. In this work, we use StockTwits data to create stock market lexicons and Twitter data in the production of sentiment indicators that are used to correlate with traditional sentiment indicators.

StockTwits is a microblogging service exclusively dedicated to stock market conversations (http://stocktwits.com) that has currently more than 300,000 users. StockTwits users can label their own text messages as “bullish” (optimistic opinion) or “bearish” (pessimistic view). Author supplied sentiment labels are already explored in SA on other social media (e.g., blogs [38]) and topics. In this paper, we explore these labeled messages, as kindly provided by StockTwits from June 2, 2010 to March 31, 2013, in a total of 350,000 posts<sup>1</sup> . We note that such dimension is significantly higher when compared with the majority of works on this topic.

Twitter (http://twitter.com) is the most popular microblogging service. Unlike StockTwits, it is a generic platform. Yet, Twitter users also apply cashtags in stock market conversations. In the creation of microblogging sentiment indicators, we used Twitter for reasons of data availability. Using Twitter REST API (https://dev.twitter. com/docs/api) and the R language (or statistical environment), we collected all tweets containing cashtags of all stocks traded in US stock markets from 22nd of December 2012 to 27th of March 2015<sup>2</sup> .

## 3.2. Baseline lexicons

For comparison purposes, we adopt six large and popular lexicons:

• GI [17] — comprises around 11,000 words (http://www.wjh. harvard.edu/\~inquirer/spreadsheet\_guide.htm). In particular, we used all words of the “Positiv” and “Negativ” attributes.

• OL [2] — contains nearly 6000 positive and negative terms. The lexicon also contains common social media misspelled words (http://www.cs.uic.edu/\~liub/FBS/opinionlexicon-English.rar).

• MSOL [20] — classifies more than 75,000 n-grams as positive or negative (http://saifmohammad.com/Lexicons/MSOL-June15- 09.txt.zip).

• MPQA [18] — with around 8000 entries (http://mpqa.cs.pitt. edu/lexicons/subj\_lexicon/). It contains a list of strong and weak subjective terms. We assigned half of the sentiment score (i.e., 0.5 or −0.5) to weaker terms.

• SWN [19] — with continuous sentiment values to the nearly 117,000 synsets (i.e., group of words that are semantically equivalent in some context) of the WordNet lexical database (http://sentiwordnet.isti.cnr.it/downloadFile.php). A word may have multiple scores, since it can belong to diverse synsets. To solve this issue, we averaged the positive and negative values for all (word, POS tag) pairs.

• FIN [15] — contains word lists commonly applied in financial text documents (http://www3.nd.edu/\~mcdonald/Word\_Lists. html). We adopted the terms classified as negative (2349) and positive (354).

## 3.3. Lexicon creation

This work applies two different validation approaches. To build a single large lexicon and evaluate its performance, we adopt a holdout split method, where the first 75% StockTwits classified messages are used to create lexicons (training set) and the remaining (most recent) 25% posts are used for evaluation purposes (test set). To perform a robust comparison of the distinct lexicon creation methods, we adopt a realistic rolling window method [39], where the labeled data are split into 20 equally sized parts ordered by time. The first 2/3 messages (training set) of each data window is utilized to create lexicons and the last 1/3 (test set) are applied in the evaluation. After performing the data pre-processing tasks, we selected all items having a minimum number of occurrences in the training set $( O _ { m i n } ) .$ The removal of non-frequent items is a usual preprocessing task in the creation of lexicons (e.g., [3,15,16,30]). This operation permits the elimination of many orthographic errors. Also, some statistical measures (e.g., PMI) are unsatisfactory estimators of association for infrequent terms [3]. Since the dimension of training data sets for each evaluation procedure is very different, we defined a different minimum number of occurrences $( O _ { m i n } )$ for each evaluation scheme.

The usage of different combinations of statistical measures on training data generates several lexicons. First, we produce three lexicons by applying adaptations of three known statistical measures (Term frequency–inverse document frequency (TF–IDF), Information Gain (IG) and Pointwise Mutual Information (PMI)) to calculate the sentiment score of each selected item. Then, we create three more versions of previous lexicons (i.e., a total of 12 lexicon versions) by utilizing two new complementary statistics $( P _ { \mathrm { d a y s } } ( l )$ and $M _ { \mathrm { a s s o c } } ( l ) )$ . In order to refine the sentiment score, the value obtained by the latter measures is multiplied by the score produced by each adapted measure. Additionally, we tested the calculation of sentiment scores for afirmative and negated contexts. The previously described procedure is used for separate afirmative and negated training data.

## 3.3.1. Data pre-processing

In order to prepare the microblogging data for the lexicon creation, we performed various pre-processing tasks using the R tool [40]:

• substitute all cashtags by a unique term, thus avoiding cashtags to gain a sentiment value related with a particular time period;

• replace numbers by a single tag, since the whole set of distinct numbers is too vast;

• for privacy reasons, all mentions and URL addresses were normalized to “@user” and “URL”, respectively;

• exclude messages composed only by cashtags, url links, mentions or punctuation (7176 messages were removed).

Next, we adopted the Stanford CoreNLP tool [41] to execute common natural language processing operations, such as tokenization, part of speech (POS) tagging and lemmatization.

The holdout split method uses a large training set with 250,000 posts and thousands of distinct terms. Thus, for this evaluation scheme we included only terms with more than $O _ { m i n } = 1 0$ occurrences in the training data set and excluded all punctuation, resulting in approximately 7000 unigrams and 27,000 bigrams analyzed. The rolling window method creates lexicons in each one of the 20 data partitions. In this validation scheme, the training set of the partitions is much smaller (about 11,100 messages) and thus we adopted a lower minimum number of occurences, with $O _ { m i n } = 4$ in each training set. Also, we eliminated all punctuation

## 3.3.2. Statistical measures

In this work, we adapt three popular statistical measures and propose two new complementary ones. The former measures were applied to determine the information value of lexical items and thus allow us to discriminate them between “bullish“ or “bearish”:

1. TF–IDF — often used for textual data representation (e.g., [21]) and that is calculated as:

$$
t f (l, d) = \frac {n _ {d , l}}{n _ {D}}\tag{1}
$$

$$
i d f (l) = \log {\frac {N _ {d}}{N _ {l} + 1}}\tag{2}
$$

$$
t f - i d f (l, d) = t f (l, d) \times i d f (l)\tag{3}
$$

where l is a lexical entry, d is a particular document, $n _ { d , l }$ is the number of occurrences of l in document d, n is the number of lexical items in document d, $N _ { d }$ is the number of documents and N is the number of documents containing l. We first created two documents composed by all messages of each class $( d _ { 1 } -$ bullish and $d _ { 2 } - \mathsf { b e a r i s h } )$ . Then, we executed the tfidf function of the textir R package to compute $t f - i d f ( l , d )$ . To provide a single value that reflects the tendency to a sentiment class, we calculated the sentiment value $S _ { \mathrm { T F } } .$ <sub>–IDF</sub> as:

$$
S _ {\mathrm{TFIDF}} (l) = \frac {t f - i d f (l , d _ {1}) - t f - i d f (l , d _ {2})}{t f - i d f (l , d _ {1}) + t f - i d f (l , d _ {2})}.\tag{4}
$$

The final sentiment class depends on the $S _ { \mathrm { T F - I D F } } ( l )$ value: “bullish” if positive, “bearish” if negative or “neutral” if zero.

2. IG — commonly used to access the information value of an attribute (e.g., [42,43]) and that is computed as:

$$
I G (l, c) = \sum_ {d \in \{c, \bar {c} \}} \sum_ {w \in \{l, \bar {l} \}} p (w, d) \log \frac {p (w , d)}{p (w) \times p (d)}\tag{5}
$$

where c refers to a category (bullish or bearish), c¯ means the non-membership in category c and <sup>¯</sup>l refers to the absence of l. Since there are only 2 categories, c¯ of each class corresponds to c of the other class and IG values are equal for both categories. Hence, we propose the slight adaptation:

$$
\begin{array}{l} I G _ {a} (l) = p (l, b l) \log \frac {p (l , b l)}{p (l) \times p (b l)} + p (\bar {l}, b r) \log \frac {p (\bar {l} , b r)}{p (\bar {l}) \times p (b r)} \\ - p (\bar {l}, b l) \log \frac {p (\bar {l} , b l)}{p (\bar {l}) \times p (b l)} - p (l, b r) \log \frac {p (l , b r)}{p (l) \times p (b r)} \end{array}\tag{6}
$$

where bl refers to bullish class and br corresponds to bearish category. In this calculation, instead of summing the values of mutual information of all tuples, we add those referring to tuples correlated to bullish class, (l, bl) and $\left( { \bar { l } } , \ b r \right)$ , and subtract values corresponding to tuples associated to bearish class, (l, br) and <sup>¯</sup>l, bl<sup></sup>. Thus, a positive value indicates a bullish orientation and a negative value means a bearish item. Since very frequent words tend to present very high IG values, we prevent this effect by computing the final sentiment score as:

$$
S _ {\mathrm{IG}} (l) = \frac {I G _ {a} (l)}{n _ {l}}\tag{7}
$$

where $n _ { l }$ is the number of times that term l appears in all texts. 3. PMI — a popular statistic in the development of lexicons (e.g., [3,21]):

$$
P M I (x, y) = \log_ {2} \frac {p (x , y)}{p (x) p (y)}\tag{8}
$$

where x and y are words or sets of words, p(x, y) is the probability that they co-occur, and $p ( x )$ and $p ( y )$ are the probabilities of occurring x and y in the corpus, respectively. PMI will be largely positive if x and y are strongly associated, highly negative if they are complementary and near zero if there is no significant relationship between them. We adapt the sentiment score to include both positive and negative PMI values:

$$
S _ {\mathrm{PMI}} (l) = P M I (l, b u l l i s h) - P M I (l, b e a r i s h)\tag{9}
$$

where l is a lexical item, bullish refers to all bullish messages and bearish corresponds to all bearish messages. The sentiment score signal reflects the sentiment orientation.

The three statistical measures were computed to both unigrams (individual words) and bigrams (two sequential terms). We produced one lexicon for each measure, which includes unigrams and bigrams that present a better sentiment score than their constituent terms.

Two novel complementary metrics, $P _ { \mathrm { d a y s } } ( l )$ and $M _ { \mathrm { a s s o c } } ( l ) ,$ , are proposed to refine the sentiment score produced by each previously described metric $( S _ { \mathrm { T F I D F } } ( l ) , S _ { \mathrm { I G } } ( l ) \mathrm { o r } S _ { \mathrm { P M I } } ( l ) )$ . They may increase or decrease the sentiment value calculated by each of the three adapted metrics. We apply the complementary metrics by multiplying them with other metrics $( \mathbf { e } . \mathbf { g } . , S _ { \mathrm { T F I D F } } ( l ) , S _ { \mathrm { I G } } ( l )$ and $S _ { \mathrm { P M I } } ( l ) )$ . For example, the score of item l produced by the combination of $P _ { \mathrm { d a y s } } ( l ) , M _ { \mathrm { a s s o c } } ( l )$ and S<sub>PMI</sub>(l) is: $P _ { \mathrm { d a y s } } ( l ) \times M _ { \mathrm { a s s o c } } ( l ) \times S _ { \mathrm { P M I } } ( l )$

The $P _ { \mathrm { d a y s } } ( l )$ statistic calculates, for each lexical item, the percentage of days where the majority of messages mentioning it have the same sentiment polarity of the item. To have a less biased measure favoring the dominant class (i.e., bullish), we multiply the daily number of bearish messages containing the lexical item by the following adjustment value:

$$
V _ {\mathrm{adj}} = \frac {N _ {\mathrm{bull}}}{N _ {\mathrm{bear}}}\tag{10}
$$

where $N _ { \mathrm { b u l l } }$ is the total number of bullish messages in training set and $N _ { \mathrm { b e a r } }$ is the total number of bearish messages. We tested the $P _ { \mathrm { d a y s } } ( l )$ metric to prevent terms appearing in an abnormally high number in few days to have a polluted sentiment score by the predominant opinion in those days. While a low value may indicate the existence of the described situation, a high $P _ { \mathrm { d a y s } } ( l )$ value means that the lexical item has consistently the same sentiment orientation. Therefore, we expect that this measure may improve sentiment score computation.

Previous measures also do not account for the association of two sets of words: intensifiers (e.g., more, increase, up) and diminishers (e.g., less, decrease, down). Yet, the analysis of these relationships may improve the calculation of sentiment. The presence of diminishers may reverse the sentiment of the following word (e.g., less debt) while intensifiers may reinforce it (e.g., more debt). Thus, previous measures will not be effective in those situations. For instance, the likely presence of “less profit“ in a negative message would incorrectly decrease the sentiment score of the positive word “profit” when calculated by former statistical measures. Therefore, we propose the $M _ { \mathrm { a s s o c } } ( l )$ metric to address this issue:

$$
N _ {\mathrm{Int}} (l) = N _ {\mathrm{IntBull}} (l) + N _ {\mathrm{DimBear}} (l)\tag{11}
$$

$$
N _ {\mathrm{Dim}} (l) = N _ {\mathrm{IntBear}} (l) + N _ {\mathrm{DimBull}} (l)\tag{12}
$$

$$
M _ {\text {assoc}} (l) = \left\{ \begin{array}{l l} \frac {N _ {\text {Int}} (l)}{N _ {\text {Int}} (l) + N _ {\text {Dim}} (l) \times \frac {T _ {\text {Int}}}{T _ {\text {Dim}}}} + 0. 5 & \text {if l is Bullish} \\ \frac {N _ {\text {Dim}} (l)}{N _ {\text {Int}} (l) + N _ {\text {Dim}} (l) \times \frac {T _ {\text {Int}}}{T _ {\text {Dim}}}} + 0. 5 & \text {if l is Bearish} \end{array} \right.\tag{13}
$$

where N denotes the number of occurrences of the lexical item adjoined to: IntBull – intensifier words (e.g., more profit) in bullish messages; IntBear – intensifier words in bearish messages; DimBull – diminisher words (e.g., less profit) in bullish messages; and DimBear – diminisher words in bearish messages. For all analyzed elements, $T _ { \mathrm { I n t } }$ is the sum of $N _ { \mathrm { I n t } } ( l )$ and $T _ { \mathrm { D i m } }$ is the sum of $N _ { \mathrm { D i m } } ( l )$

The $M _ { \mathrm { a s s o c } } ( l )$ measure is only used in elements with more than four occurrences adjoined to intensifiers and diminishers. We selected this threshold value because we consider that a lower number would produce many cases of less solid values of association. For instance, it is more likely to happen an excessively high $M _ { \mathrm { a s s o c } } ( l )$ value for elements with two occurrences (e.g., $N _ { \mathrm { I n t } } ( l ) ~ = ~ 2$ and $N _ { \mathrm { D i m } } ( l ) = 0$ for a bullish term) than with four or more occurrences.

We distinguished the formula for bullish and bearish items because bullish terms shall have higher $N _ { \mathrm { I n t } } ( l )$ values and bearish terms shall produce higher $N _ { \mathrm { D i m } } ( l )$ values. Since $M _ { \mathrm { a s s o c } } ( l ) \in [ 0 . 5 , 1 . 5 ]$ a $M _ { \mathrm { a s s o c } } ( l )$ value close to 1.5 means that these associations are highly concordant to the assigned sentiment polarity and the absolute sentiment score will increase. A low $M _ { \mathrm { a s s o c } } ( l )$ value indicates the opposite, decreasing the absolute score. The intensifiers and diminishers (Table 1) were manually selected. First, we choose a small set of words (e.g., less, more, very) and then added synonyms found in a thesaurus.

## 3.3.3. Scores for afirmative and negative contexts

The sentiment value of a term may change in different contexts. For instance, negation is a frequent context that can modify the sentiment polarity or intensity of a particular word. While many studies process negation by reverting sentiment polarity (from positive to negative and vice-versa), others argue that sentiment reversion may not be adequate [3]. For example, “frightening“ is very negative but “not frightening” often suggests a less intense negative emotion.

To address negation more eficiently, we calculated sentiment scores for negated and afirmative (non-negated) contexts separately [3]. We divided the training data set into an afirmative and a negated corpus. The negated set contains all negated context segments and the afirmative set is composed by the remaining segments. The negated contexts are the sentence segments starting with a negation word present in the Christopher Potts sentiment tutorial (http://sentiment.christopherpotts.net/lingstruc. html) and ending with one of the punctuation marks: ‘,’, ‘.’, ‘:’, ‘;’, ‘!’, ‘?’. Then, we create the stock market lexicon by applying the same procedure utilized for the “general” score (i.e., described in the previous subsection) on each corpus (afirmative and negated), producing two sentiment scores for each item that should be used in the respective context. However, some items do not have suficient occurrences in each corpus in order to have both sentiment scores calculated. In such situations, we assign its “general” sentiment to the unavailable sentiment context score

Table 1 Intensifiers and Diminishers.

<table><tr><td>Intensifiers</td><td>Diminishers</td></tr><tr><td>accretion, accrual, addendum, addition, augmentation, boost, expansion, gain, increment, more, plus, proliferation, raise, rise, accelerate, add, aggrandize, amplify, augment, enlarge, escalate, expand, extend, hype, multiply, swell, stoke, supersize, up, accumulate, climb, proliferate, soar, uprise, desire, fancy, prefer, enjoy, relish, admire, adore, esteem, hallow, idolize, revere, venerate, worship, appreciate, love, elevated, escalated, heightened, increased, raised, admiring, applauding, appreciative, approbatory, approving, commendatory, complimentary, friendly, good, positive</td><td>abatement, decline, decrease, decrement, depletion, diminishment, diminution, fall, lessening, loss, lowering, reduction, shrinkage, diminish, dwindle, lessen, recede, wane, abate, downsize, lower, minify, reduce, subtract, drop, descend, dip, plunge, dive, sink, slide, abhor, abominate, despise, detest, execrate, loathe, deplore, deprecate, disapprove, disdain, disfavor, dislike, hate, decreased, depressed, dropped, receded, under, down, low, adverse, depreciative, depreciatory, derogatory, disapproving, inappreciative, negative, unappreciative, uncomplimentary, unfavorable, unflattering, unfriendly</td></tr></table>

## 3.4. Lexicon evaluation

As explained in Section 3.3, we adopt two complementary evaluation procedures that use a time ordered training/test split: a single holdout (75%/25%) and a rolling window (with 20 windows, each with 2/3 for training and 1/3 for testing). The former procedure creates a large lexicon that is publicly made available, while the latter procedure uses much less data to generate each lexicon but it allows us to get several test sets and thus execute statistical significance tests. For both evaluation methods, we performed SA in each test set by applying each lexicon. The message overall sentiment value is computed as the sum of all its lexical scores. When lexicon bigrams are present in the text, we only sum the score of the bigrams and do not account for the score of their individual constituents. The message is classified as “bullish”, “bearish“ or “neutral” according to the sign of the sum (positive, negative or zero). In SA applying lexicons with afirmative and negated scores, we also identified the afirmative and negated context segments in order to utilize the adequate sentiment score.

The classification measures used were:

• the percentage of correct classifications (CC1);

• the percentage of unclassified messages, i.e., texts with no lexicon items (Unc);

• the percentage of correct classifications excluding unclassified messages (CC2);

• precision for “bullish” $( \mathrm { P _ { B u l l } } )$ and “bearish” $( { \mathrm { P } } _ { \mathrm { B e a r } } ) ,$ given by $\frac { T P } { T P + F P }$ , where TP denotes the number of true positives and FP the number of false positives;

• recall for “bullish” (R ) and “bearish” $( \mathrm { R } _ { \mathrm { B e a r } } ) ,$ given by $\frac { T P } { T P + F N } .$ where FN denotes the number of false negatives;

• F-score for “bullish” (F1 ) and “bearish” $( \mathrm { F } 1 _ { \mathrm { B e a r } } )$ , where $F _ { 1 } =$ $\pm \frac { P r e c 1 s t o n * R e c a l l } { P r e c i s i o n + R e c a l l }$

• macro-averaged F-score $( \mathrm { F } _ { \mathrm { A v g } } )$ that averages both F-scores $( { \mathrm { F } } 1 _ { \mathrm { B u l l } } , { \mathrm { F } } 1 _ { \mathrm { B e a r } } )$

We assume that the classification is correct when it matches the same sentiment (“bullish” or “bearish”) as provided by user who made the post. Under the rolling window scheme, we verified the statistical significance of CC1 and $\mathsf { F } _ { \mathsf { A v g } }$ improvements obtained by a specific approach relatively to another one. The parametric paired Student’s t-test and the non-parametric Wilcoxon signed rank test were applied to pairs of lexicon creation methods.

## 3.5. Sentiment indicators

Some works in the literature argue that sentiment may affect prices. In these studies, sentiment indicators based on indirect measures (e.g., end fund discount, NYSE share turnover) or surveys have informative value in the forecasting of aggregate stock market returns (e.g., [44,45]) or in the prediction of returns of portfolios formed on diverse attributes (e.g., market value [46,47],

Classification results for the created lexicons with unique context score (in %, best values in bold)

<table><tr><td>Lexicon</td><td>CC1</td><td>Unc</td><td>CC2</td><td> $P_{Bull}$ </td><td> $R_{Bull}$ </td><td> $F1_{Bull}$ </td><td> $P_{Bear}$ </td><td> $R_{Bear}$ </td><td> $F1_{Bear}$ </td><td> $F_{Avg}$ </td></tr><tr><td colspan="11">Panel A: evaluation results of holdout split method</td></tr><tr><td> $PMI_{Scr}$ </td><td>75.2</td><td>0.5</td><td>75.5</td><td>88.6</td><td>76.5</td><td>82.1</td><td>51.9</td><td>71.5</td><td>60.1</td><td>71.1</td></tr><tr><td> $PMI_{Assoc}$ </td><td>75.6</td><td>0.5</td><td>76.0</td><td>88.5</td><td>77.4</td><td>82.6</td><td>52.6</td><td>70.6</td><td>60.3</td><td>71.4</td></tr><tr><td> $PMI_{Days}$ </td><td>78.8</td><td>0.5</td><td>79.1</td><td>86.0</td><td>85.4</td><td>85.7</td><td>59.5</td><td>59.6</td><td>59.6</td><td>72.6</td></tr><tr><td> $PMI_{All}$ </td><td>78.8</td><td>0.5</td><td>79.2</td><td>86.0</td><td>85.5</td><td>85.8</td><td>59.7</td><td>59.5</td><td>59.6</td><td>72.7</td></tr><tr><td> $TFIDF_{Scr}$ </td><td>74.3</td><td>0.5</td><td>74.7</td><td>88.6</td><td>75.1</td><td>81.3</td><td>50.6</td><td>71.9</td><td>59.4</td><td>70.4</td></tr><tr><td> $TFIDF_{Assoc}$ </td><td>74.8</td><td>0.5</td><td>75.1</td><td>88.4</td><td>76.2</td><td>81.8</td><td>51.3</td><td>70.8</td><td>59.5</td><td>70.7</td></tr><tr><td> $TFIDF_{Days}$ </td><td>78.4</td><td>0.5</td><td>78.7</td><td>85.6</td><td>85.4</td><td>85.5</td><td>58.8</td><td>58.3</td><td>58.6</td><td>72</td></tr><tr><td> $TFIDF_{All}$ </td><td>78.5</td><td>0.5</td><td>78.8</td><td>85.5</td><td>85.5</td><td>85.5</td><td>59.1</td><td>58.1</td><td>58.6</td><td>72.1</td></tr><tr><td> $IG_{Scr}$ </td><td>70.5</td><td>0.5</td><td>70.8</td><td>89.4</td><td>68.5</td><td>77.5</td><td>46.1</td><td>76.3</td><td>57.4</td><td>67.5</td></tr><tr><td> $IG_{Assoc}$ </td><td>71.6</td><td>0.5</td><td>71.9</td><td>89.5</td><td>70.1</td><td>78.6</td><td>47.3</td><td>75.9</td><td>58.3</td><td>68.4</td></tr><tr><td> $IG_{Days}$ </td><td>76.0</td><td>0.5</td><td>76.4</td><td>87.2</td><td>79.5</td><td>83.2</td><td>53.4</td><td>65.9</td><td>59.0</td><td>71.1</td></tr><tr><td> $IG_{All}$ </td><td>76.4</td><td>0.5</td><td>76.7</td><td>86.9</td><td>80.4</td><td>83.5</td><td>54.1</td><td>64.9</td><td>59.0</td><td>71.3</td></tr><tr><td colspan="11">Panel B: average evaluation results of rolling window method</td></tr><tr><td> $PMI_{Scr}$ </td><td>71.1</td><td>0.5</td><td>71.4</td><td>90.0</td><td>69.0</td><td>78.0</td><td>45.7</td><td>77.0</td><td>56.9</td><td>67.4</td></tr><tr><td> $PMI_{Assoc}$ </td><td>71.5</td><td>0.5</td><td>71.9</td><td>89.9</td><td>69.8</td><td>78.4</td><td>46.2</td><td>76.7</td><td>57.3</td><td>67.9</td></tr><tr><td> $PMI_{Days}$ </td><td>77.3</td><td>0.5</td><td>77.7</td><td>87.4</td><td>81.5</td><td>84.3</td><td>54.1</td><td>64.4</td><td>58.5</td><td>71.4</td></tr><tr><td> $PMI_{All}$ </td><td>77.5</td><td>0.5</td><td>77.8</td><td>87.3</td><td>81.7</td><td>84.4</td><td>54.6</td><td>64.2</td><td>58.7</td><td>71.5</td></tr><tr><td> $TFIDF_{Scr}$ </td><td>71.6</td><td>0.5</td><td>71.9</td><td>89.1</td><td>70.8</td><td>78.8</td><td>45.6</td><td>73.4</td><td>55.8</td><td>67.3</td></tr><tr><td> $TFIDF_{Assoc}$ </td><td>72.1</td><td>0.5</td><td>72.5</td><td>89.0</td><td>71.7</td><td>79.3</td><td>46.3</td><td>73.1</td><td>56.3</td><td>67.8</td></tr><tr><td> $TFIDF_{Days}$ </td><td>77.1</td><td>0.5</td><td>77.5</td><td>86.4</td><td>82.4</td><td>84.3</td><td>54.0</td><td>60.5</td><td>56.6</td><td>70.5</td></tr><tr><td> $TFIDF_{All}$ </td><td>77.3</td><td>0.5</td><td>77.7</td><td>86.5</td><td>82.7</td><td>84.5</td><td>54.5</td><td>60.4</td><td>56.9</td><td>70.7</td></tr><tr><td> $IG_{Scr}$ </td><td>67.4</td><td>0.5</td><td>67.7</td><td>90.5</td><td>63.8</td><td>74.2</td><td>42.7</td><td>78.7</td><td>54.3</td><td>64.2</td></tr><tr><td> $IG_{Assoc}$ </td><td>68.0</td><td>0.5</td><td>68.3</td><td>90.5</td><td>64.7</td><td>74.9</td><td>43.2</td><td>78.5</td><td>54.6</td><td>64.8</td></tr><tr><td> $IG_{Days}$ </td><td>75.2</td><td>0.5</td><td>75.5</td><td>88.4</td><td>77.4</td><td>82.3</td><td>50.6</td><td>68.6</td><td>57.3</td><td>69.8</td></tr><tr><td> $IG_{All}$ </td><td>75.5</td><td>0.5</td><td>75.8</td><td>88.4</td><td>77.8</td><td>82.6</td><td>51.0</td><td>68.5</td><td>57.6</td><td>70.1</td></tr></table>

Please cite this article as: N. Oliveira, et al., Stock market sentiment lexicon acquisition using microblogging data and statistical measures, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.013

Table 4  
Table 3  
Paired Student’s t-test and the Wilcoxon signed rank test for pairwise comparison of lexicons using unique context scores. The following symbols denote significance at the 5% level: a — paired Student’s t-test fo $\mathrm { F } _ { \tt A v g } ; \mathrm { b } - \mathrm { W }$ ilcoxon signed rank test for $\mathrm { F } _ { \mathrm { A v g } } ; \mathrm { c - }$ — paired Student’s t-test for CC1; d — Wilcoxon signed rank test for CC1. Alternative hypothesis: lexicon in the row has higher values than the lexicon in the column.

<table><tr><td></td><td> $PMI_{Scr}$ </td><td> $PMI_{Assoc}$ </td><td> $PMI_{Days}$ </td><td> $PMI_{All}$ </td><td> $TFIDF_{Scr}$ </td><td> $TFIDF_{Assoc}$ </td><td> $TFIDF_{Days}$ </td><td> $TFIDF_{All}$ </td><td> $IG_{Scr}$ </td><td> $IG_{Assoc}$ </td><td> $IG_{Days}$ </td><td> $IG_{All}$ </td></tr><tr><td> $PMI_{Scr}$ </td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>abcd</td><td>abcd</td><td></td><td></td></tr><tr><td> $PMI_{Assoc}$ </td><td>abcd</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td>abcd</td><td>abcd</td><td></td><td></td></tr><tr><td> $PMI_{Days}$ </td><td>abcd</td><td>abcd</td><td>-</td><td></td><td>abcd</td><td>abcd</td><td>ab</td><td>ab</td><td>abcd</td><td>abcd</td><td>abcd</td><td>abcd</td></tr><tr><td> $PMI_{All}$ </td><td>abcd</td><td>abcd</td><td>abcd</td><td>-</td><td>abcd</td><td>abcd</td><td>ab</td><td>ab</td><td>abcd</td><td>abcd</td><td>abcd</td><td>abcd</td></tr><tr><td> $TFIDF_{Scr}$ </td><td></td><td></td><td></td><td></td><td>-</td><td></td><td></td><td></td><td>abcd</td><td>abcd</td><td></td><td></td></tr><tr><td> $TFIDF_{Assoc}$ </td><td>cd</td><td></td><td></td><td></td><td>abcd</td><td>-</td><td></td><td></td><td>abcd</td><td>abcd</td><td></td><td></td></tr><tr><td> $TFIDF_{Days}$ </td><td>abcd</td><td>abcd</td><td></td><td></td><td>abcd</td><td>abcd</td><td>-</td><td></td><td>abcd</td><td>abcd</td><td>acd</td><td>cd</td></tr><tr><td> $TFIDF_{All}$ </td><td>abcd</td><td>abcd</td><td></td><td></td><td>abcd</td><td>abcd</td><td>abcd</td><td>-</td><td>abcd</td><td>abcd</td><td>abcd</td><td>acd</td></tr><tr><td> $IG_{Scr}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td><td></td><td></td><td></td></tr><tr><td> $IG_{Assoc}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>abcd</td><td>-</td><td></td><td></td></tr><tr><td> $IG_{Days}$ </td><td>abcd</td><td>abcd</td><td></td><td></td><td>abcd</td><td>abcd</td><td></td><td></td><td>abcd</td><td>abcd</td><td>-</td><td></td></tr><tr><td> $IG_{All}$ </td><td>abcd</td><td>abcd</td><td></td><td></td><td>abcd</td><td>abcd</td><td></td><td></td><td>abcd</td><td>abcd</td><td>abcd</td><td>-</td></tr></table>

financial distress [46,47], volatility [44,46,47]). Recently, several studies applied computational linguistic methods to textual contents (e.g., microblogs, message boards or newspapers) to extract investor sentiment indicators (e.g., [9–14,48–50]). Some of these papers found that sentiment indicators have predictive value for future market directions (e.g., [10–13,48]) and returns (e.g., [49]) and allow profitable trading strategies (e.g., [11,50]).

In this work, we measured the correlation of microblogging sentiment indicators with two widely applied survey sentiment indicators: the American Association of Individual Investors (AAII) (e.g., [45,51]) and Investors Intelligence (II) (e.g., [45,51,52]). AAII measures the percentage of individual investors who are bullish, bearish, and neutral based on the votes of their members to a poll questioning their sentiment on the stock market for the next six months. AAII values are published online each Thursday morning containing data from previous Thursday until last Wednesday. II analyzes each week over a hundred market newsletters and categorizes each author’s current opinion about the market as bullish, bearish or correction. The percentage of newsletters classified as bullish, bearish or correction is published every Wednesday and they include the newsletters analyzed until Tuesday. II measures may be more correlated to institutional sentiment than AAII, because many authors are market professionals [51]. AAII and II indicators were collected from Thompson Reuters Datastream (http://online. thomsonreuters.com/datastream/).

Twitter sentiment indicators were created by applying SA on the collected Twitter data using two distinct lexicons:

• TWTSML uses the selected stock market lexicon (SML), i.e., the $\mathrm { P M I _ { B i S c r } }$ lexicon created using 75% of StockTwits data (Section 3). Afirmative or negated context scores are applied in the respective segments.

• TWTSWN applies the SWN lexicon (the selected baseline lexicon, Section 3).

Six different values are computed for each time period:

$$
\mathrm{TWTSML} _ {\text { bull }, \mathrm{t}} = \mathrm{SML} _ {\text { bull }, \mathrm{t}} / (\mathrm{SML} _ {\text { bull }, \mathrm{t}} + \mathrm{SML} _ {\text { bear }, \mathrm{t}})\tag{14}
$$

$$
\mathrm{TWTSML} _ {\text { bear }, \mathrm{t}} = \mathrm{SML} _ {\text { bear }, \mathrm{t}} / (\mathrm{SML} _ {\text { bull }, \mathrm{t}} + \mathrm{SML} _ {\text { bear }, \mathrm{t}})\tag{15}
$$

$$
\mathrm{TWTSML} _ {\text { spread }, \mathrm{t}} = \mathrm{TWTSML} _ {\text { bull }, \mathrm{t}} - \mathrm{TWTSML} _ {\text { bear }, \mathrm{t}}\tag{16}
$$

$$
\mathrm{TWTSWN} _ {\text { bull,   t }} = \mathrm{SWN} _ {\text { bull,   t }} / (\mathrm{SWN} _ {\text { bull,   t }} + \mathrm{SWN} _ {\text { bear,   t }})\tag{17}
$$

$$
\mathrm{TWTSWN} _ {\text { bear }, \mathrm{t}} = \mathrm{SWN} _ {\text { bear }, \mathrm{t}} / (\mathrm{SWN} _ {\text { bull }, \mathrm{t}} + \mathrm{SWN} _ {\text { bear }, \mathrm{t}})\tag{18}
$$

$$
\mathrm{TWTSWN} _ {\text { spread }, \mathrm{t}} = \mathrm{TWTSWN} _ {\text { bull }, \mathrm{t}} - \mathrm{TWTSWN} _ {\text { bear }, \mathrm{t}}\tag{19}
$$

Classification results for the selected lexicon creation method and baseline lexicons (in %, best values in bold).

<table><tr><td>Lexicon</td><td>CC1</td><td>Unc</td><td>CC2</td><td> $P_{Bull}$ </td><td> $R_{Bull}$ </td><td> $F1_{Bull}$ </td><td> $P_{Bear}$ </td><td> $R_{Bear}$ </td><td> $F1_{Bear}$ </td><td> $F_{Avg}$ </td></tr><tr><td colspan="11">Panel A: evaluation results of holdout split method</td></tr><tr><td> $PMI_{All}$ </td><td>78.8</td><td>0.5</td><td>79.2</td><td>86.0</td><td>85.5</td><td>85.8</td><td>59.7</td><td>59.5</td><td>59.6</td><td>72.7</td></tr><tr><td>FIN</td><td>16.8</td><td>66.0</td><td>49.3</td><td>83.5</td><td>13.9</td><td>23.8</td><td>34.3</td><td>25.1</td><td>29.0</td><td>26.4</td></tr><tr><td>GI</td><td>37.7</td><td>25.8</td><td>50.8</td><td>82.5</td><td>36.2</td><td>50.3</td><td>37.5</td><td>42.1</td><td>39.7</td><td>45.0</td></tr><tr><td>MSOL</td><td>53.4</td><td>1.8</td><td>54.3</td><td>79.1</td><td>58.6</td><td>67.3</td><td>33.9</td><td>38.2</td><td>35.9</td><td>51.6</td></tr><tr><td>MPQA</td><td>36.9</td><td>37.5</td><td>59.0</td><td>80.6</td><td>40.6</td><td>54.0</td><td>34.3</td><td>26.3</td><td>29.8</td><td>41.9</td></tr><tr><td>OL</td><td>31.8</td><td>43.0</td><td>55.9</td><td>82.6</td><td>32.7</td><td>46.8</td><td>37.7</td><td>29.4</td><td>33.1</td><td>39.9</td></tr><tr><td>SWN</td><td>57.4</td><td>5.1</td><td>60.5</td><td>79.9</td><td>59.7</td><td>68.3</td><td>34.1</td><td>50.7</td><td>40.7</td><td>54.5</td></tr><tr><td colspan="11">Panel B: average evaluation results of rolling window method</td></tr><tr><td> $PMI_{All}$ </td><td>77.5</td><td>0.5</td><td>77.8</td><td>87.3</td><td>81.7</td><td>84.4</td><td>54.6</td><td>64.2</td><td>58.7</td><td>71.5</td></tr><tr><td>FIN</td><td>17.3</td><td>63.7</td><td>47.8</td><td>84.2</td><td>13.9</td><td>23.8</td><td>32.8</td><td>27.4</td><td>29.3</td><td>26.5</td></tr><tr><td>GI</td><td>37.4</td><td>25.8</td><td>50.4</td><td>82.6</td><td>36.1</td><td>50.2</td><td>35.8</td><td>41.1</td><td>37.8</td><td>44.0</td></tr><tr><td>MSOL</td><td>52.3</td><td>1.2</td><td>53.0</td><td>80.2</td><td>55.8</td><td>65.6</td><td>32.5</td><td>41.9</td><td>36.1</td><td>50.8</td></tr><tr><td>MPQA</td><td>39.1</td><td>34.7</td><td>59.8</td><td>81.3</td><td>42.6</td><td>55.8</td><td>35.2</td><td>28.4</td><td>31.1</td><td>43.5</td></tr><tr><td>OL</td><td>34.1</td><td>39.5</td><td>56.3</td><td>83.5</td><td>34.6</td><td>48.9</td><td>38.2</td><td>32.3</td><td>34.7</td><td>41.8</td></tr><tr><td>SWN</td><td>58.9</td><td>4.4</td><td>61.6</td><td>80.6</td><td>61.4</td><td>69.7</td><td>33.8</td><td>51.1</td><td>40.4</td><td>55.0</td></tr></table>

Please cite this article as: N. Oliveira, et al., Stock market sentiment lexicon acquisition using microblogging data and statistical measures, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.013

Paired Student’s t-test and the Wilcoxon signed rank test for pairwise comparison of PMI method with baseline lexicons. The following symbols denote significance at the 5% level: a — paired Student’s t-test for $\mathrm { F } _ { \mathrm { A v g } } ; \mathrm { b - }$ Wilcoxon signed rank test for $\mathrm { F _ { A v g } ; }$ c — paired Student’s t-test for CC1; d — Wilcoxon signed rank test for CC1. Alternative hypothesis: lexicon in the row has higher values than the lexicon in the column.

<table><tr><td></td><td>FIN</td><td>GI</td><td>MSOL</td><td>MPQA</td><td>OL</td><td>SWN</td></tr><tr><td> $PMI_{All}$ </td><td>abcd</td><td>abcd</td><td>abcd</td><td>abcd</td><td>abcd</td><td>abcd</td></tr></table>

where:

${ \mathsf { S M L } } _ { \mathrm { b u l l } } ,$ corresponds to the sum of all positive SA scores (i.e., greater than zero) using SML (i.e., PMI lexicon) on all tweets from a given t time period.

$\mathsf { S M L } _ { \mathrm { b e a r , t } }$ corresponds to absolute value of the sum of all negative SA scores (i.e., less than zero) using SML on all tweets for time t.

$\mathsf { S W N } _ { \mathsf { b u l l } } ,$ corresponds to the sum of all positive SA scores using the selected baseline lexicon (i.e., SWN lexicon) on all tweet for time t.

$\mathrm { S W N } _ { \mathrm { b e a r , t } }$ corresponds to absolute value of the sum of all negative SA scores using the SWN lexicon on all tweets for time t.

We used survey and Twitter indicators from February 1, 2013 to March 27, 2015. This time period is subsequent to the applied in the creation of the selected stock market lexicon. Since both AAII and II use ratios, we also created bullish and bearish ratios. We decided to use SA scores instead of the number of bullish or bearish messages because we consider that they better indicate the sentiment strength. Additionally, we calculated the bull–bear spread $( \mathrm { T W T S M L } _ { \mathrm { s p r e a d } } , \mathrm { T W T S W N } _ { \mathrm { s p r e a d } } ) ,$ , a common measure of sentiment (e.g., $[ 5 1 , { \dot { 5 } } 2 ] )$ . Different Twitter sentiment indicators $\mathrm { ( i . e . , T W T S M L _ { b u l l } , T W T S M L _ { b e a r } , T W T S M L _ { s p r e a d } , T W T S W N _ { b u l l } , }$ $\mathrm { T W I S W N _ { b e a r } , T W T S W N _ { s p r e a d } , }$ were computed for each survey sentiment indicator corresponding to their time periods. Each Twitter sentiment indicator is correlated to their AAII and II counterparts $( \mathrm { e . g . , T W T S M L _ { b u l l } \ w i t h { A A I I _ { b u l l } } , T W T S W N _ { s p r e a d } \ w i t h { I I _ { s p r e a d } } } ) .$

## 4. Results

## 4.1. Lexicon evaluation

In this section we present the SA results for the tested lexicons. We start by analyzing the use of the proposed statistical measures in the computation of a unique sentiment score for each item. We experimented four different scores for the three main statistical measures (PMI, TFIDF, IG):

• Scr corresponds to the value calculated by the main statistical measure $( S _ { \mathrm { P M I } } , S _ { \mathrm { T F I D F } } , S _ { \mathrm { I G } } ) ;$

• Assoc is the product of Scr and $M _ { \mathrm { a s s o c } } ;$

• Days is the product of Scr and $P _ { \mathrm { d a y s } } ;$

• All is the product of Scr, $M _ { \mathrm { a s s o c } }$ and $P _ { \mathrm { d a y s } } .$

Table 2 shows all classification metrics for the created lexicons using a unique context score and Table 3 indicates which lexicons

Examples of lexical terms with different sentiment value in $\mathrm { P M I } _ { \mathrm { A l l } }$ and SWN.

obtain statistically significant higher CC1 and $\mathrm { F _ { A v g } }$ values compared with other lexicons according to the paired Student’s t-test and the Wilcoxon signed rank test. The alternative hypothesis of these tests is that the lexicon in the row has higher results than the lexicon in the column.

The best overall results (e.g., highest CC1, CC2 and $\mathsf { F } _ { \mathsf { A v g } }$ values) are obtained by the $\mathrm { P M I } _ { \mathrm { A l l } }$ method, which delivers statistically significant higher CC1 and $\mathrm { F _ { A v g } }$ values than all other lexicons. The complementary metrics proved to be useful because they improved the evaluation results for all main statistical measures. Every lexicon applying $M _ { \mathrm { a s s o c } }$ or $P _ { \mathrm { d a y s } }$ metrics obtains statistically significant higher CC1 and $\mathrm { F _ { A v g } }$ values than their Scr counterparts (e.g., PMI , $\mathrm { T F I D F _ { A l l } }$ and $\mathrm { I G } _ { \mathrm { D a y s } }$ are higher than $\scriptstyle \mathrm { P M I } _ { \mathrm { S c r } } , \mathrm { T F I D F } _ { \mathrm { S c r } }$ and $\mathrm { I G } _ { \mathrm { S c r } }$ , respectively). The $M _ { \mathrm { a s s o c } }$ measure permits slight gains in both $F 1 _ { \mathrm { B u l l } }$ and $F 1 _ { \mathrm { B e a r } }$ scores. The $P _ { \mathrm { d a y s } }$ metric is able to substantially improve F1 values while maintaining the $F 1 _ { \mathrm { B e a r } }$ very similar.

Next, we compare the selected $\mathrm { P M I } _ { \mathrm { A l l } }$ with diverse reference lexicons. The SA results obtained by these lexical resources are presented in Tables 4 and 5. $\mathrm { P M I } _ { \mathrm { A l l } }$ based lexicons achieve the best results for all evaluation metrics by a significant margin. For example, sentiment classification using this lexicon obtains a $1 8 . 2 ~ ( \mathrm { F _ { A v g } ) , }$ , 18.7 (CC2) and 21.4 (CC1) percentage point difference in the holdout split scheme when compared with the baseline resource that has the highest overall results (i.e., SWN). All these improvements are statistically significant. In addition, the approximately 20,000 lexical entries that belong to the lexicons created in this work are included in more messages (only 0.5% of the posts are not classified). In contrast, the generic SWN lexicon, which contains a larger number of lexical items (117,000), presents a higher unclassification rate (5.1%). The financial lexicon (FIN) achieves the lowest $\mathrm { F _ { A v g } , }$ , CC1 and CC2 values, despite having the second highest $\mathrm { \sf P _ { B u l l } . }$ . The poorer FIN unclassified message performance (66%) confirms that there is a considerable difference between the lexical terms extracted from financial text documents and StockTwit messages. In effect, there are several popular StockTwits terms, such as “bearish”, “bullish”, “breakout”, “put” and “short”, that are not present in FIN. Since “bullish” and “bearish” are distinctive terms of stock market terminology, we verified their presence and classification in baseline lexicons. FIN and GI lexicons do not contain these terms and MSOL lexicon incorrectly classifies “bullish” as negative. The remaining lexicons assign the correct classification to these words.

Next, we analyze the differences between the selected large lexicon $( \mathrm { P M I } _ { \mathrm { A l l } } , 2 0 5 5 0 \mathrm { i t e m s } )$ and baseline lexicons (SWN, 117,000 entries). The lexicons are quite distinct, since only 2695 lexical terms (13% of $\mathsf { P M I } _ { \mathsf { A l l } } )$ belong to both lexicons. Indeed, the presence of diverse stock market terms in generic opinion lexicons is unlikely [38]. Also, 42% of these common terms (1121) have different sentiment polarities, as shown in Table 6. In particular, Table 6 presents examples of terms associated with: stock price changes (e.g., dip, downside, explosive, outperform, rip, sink); stock expectations (e.g., overvalue, underestimate); and stock operations (e.g., long). Under non-financial contexts, these terms can suggest different sentiment values. For example, “underestimate” is in general a negative verb but when related with stocks it can suggest an opportunity to buy. These differences highlight the importance of producing specialized stock market lexicons. For demonstration purposes, Fig. 1 plots a word cloud of the most interesting $\mathrm { P M I } _ { \mathrm { A l l } }$ bullish

Table 6

<table><tr><td>Item</td><td>POS tag</td><td> $PMI_{All}$ </td><td>SWN</td><td>Item</td><td>POS tag</td><td> $PMI_{All}$ </td><td>SWN</td></tr><tr><td>Careful</td><td>Adjective</td><td>Negative</td><td>Positive</td><td>Overvalue</td><td>Verb</td><td>Negative</td><td>Positive</td></tr><tr><td>Dip</td><td>Noun</td><td>Positive</td><td>Negative</td><td>Outperform</td><td>Verb</td><td>Positive</td><td>Negative</td></tr><tr><td>Rip</td><td>Verb</td><td>Positive</td><td>Negative</td><td>Downside</td><td>Noun</td><td>Negative</td><td>Positive</td></tr><tr><td>Sink</td><td>Verb</td><td>Negative</td><td>Positive</td><td>Explosive</td><td>Adjective</td><td>Positive</td><td>Negative</td></tr><tr><td>Long</td><td>Adjective</td><td>Positive</td><td>Negative</td><td>Underestimate</td><td>Verb</td><td>Positive</td><td>Negative</td></tr></table>

Please cite this article as: N. Oliveira, et al., Stock market sentiment lexicon acquisition using microblogging data and statistical measures, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.013

N. Oliveira, et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/K3ZTFHXP/fulltext/images/c2504348315bebace758312d992954e6aef19aa68a5c4838f2691dc56d1af6f1.jpg)  
Fig. 1. Bullish and bearish word cloud for a stock market lexicon $( { \mathrm { P M I } } _ { \mathrm { A l l } } ) .$

and bearish terms. Diverse terms with different sentiment polarity or absent from SWN stand out in this figure.

The utility of afirmative and negated context scores is assessed by comparing $\mathrm { P M I } _ { \mathrm { A l l } }$ $\mathrm { T F I D F _ { A l l } }$ and $\mathsf { I G } _ { \mathsf { A l l } }$ with the equivalent lexicons containing afirmative and negated context scores $( { \mathrm { P M I } } _ { \mathrm { B i S c r } } ,$ $\mathrm { T F I D F } _ { \mathrm { B i S c r } } , \mathrm { I G } _ { \mathrm { B i S c r } } ) .$ . Thus, all sentiment scores apply the complementary metrics $( M _ { \mathrm { a s s o c } }$ and $P _ { \mathrm { d a y s } } )$ . Tables 7 and 8 show the evaluation results.

The application of afirmative and negated context scores appears to be beneficial. Despite the reduced difference, lexicons having two context scores improve or maintain almost all evaluation results compared to the unique score counterparts. $\mathsf { I G } _ { \mathrm { B i S c r } }$ obtains statistically significant higher CC1 and $\mathrm { F _ { A v g } }$ values than $\mathsf { I G } _ { \mathsf { A l l } }$ and $\mathrm { P M I _ { B i S c r } }$ produces statistically significant higher CC1 values than $\mathrm { P M I } _ { \mathrm { A l l } } .$ Moreover, $\mathrm { P M I _ { B i S c r } }$ lexicon has statistically significant higher CC1 and $\mathrm { F _ { A v g } }$ values than all IG and TFIDF lexicons. Fig. 2 shows the sentiment

Classification results for unique and dual context scores (in %, best values in bold).

<table><tr><td>Lexicon</td><td>CC1</td><td>Unc</td><td>CC2</td><td> $P_{Bull}$ </td><td> $R_{Bull}$ </td><td> $F1_{Bull}$ </td><td> $P_{Bear}$ </td><td> $R_{Bear}$ </td><td> $F1_{Bear}$ </td><td> $F_{Avg}$ </td></tr><tr><td colspan="11">Panel A: evaluation results of holdout split method</td></tr><tr><td> $PMI_{All}$ </td><td>78.8</td><td>0.5</td><td>79.2</td><td>86.0</td><td>85.5</td><td>85.8</td><td>59.7</td><td>59.5</td><td>59.6</td><td>72.7</td></tr><tr><td> $TFIDF_{All}$ </td><td>78.5</td><td>0.5</td><td>78.8</td><td>85.5</td><td>85.5</td><td>85.5</td><td>59.1</td><td>58.1</td><td>58.6</td><td>72.1</td></tr><tr><td> $IG_{All}$ </td><td>76.4</td><td>0.5</td><td>76.7</td><td>86.9</td><td>80.4</td><td>83.5</td><td>54.1</td><td>64.9</td><td>59.0</td><td>71.3</td></tr><tr><td> $PMI_{BiScr}$ </td><td>79.0</td><td>0.5</td><td>79.3</td><td>86.2</td><td>85.4</td><td>85.8</td><td>59.8</td><td>60.3</td><td>60.1</td><td>73.0</td></tr><tr><td> $TFIDF_{BiScr}$ </td><td>78.5</td><td>0.5</td><td>78.9</td><td>86.0</td><td>85.1</td><td>85.5</td><td>59.0</td><td>59.6</td><td>59.3</td><td>72.4</td></tr><tr><td> $IG_{BiScr}$ </td><td>76.7</td><td>0.5</td><td>77.0</td><td>87.0</td><td>80.8</td><td>83.8</td><td>54.7</td><td>64.8</td><td>59.3</td><td>71.5</td></tr><tr><td colspan="11">Panel B: average evaluation results of rolling window method</td></tr><tr><td> $PMI_{All}$ </td><td>77.5</td><td>0.5</td><td>77.8</td><td>87.3</td><td>81.7</td><td>84.4</td><td>54.6</td><td>64.2</td><td>58.7</td><td>71.5</td></tr><tr><td> $TFIDF_{All}$ </td><td>77.3</td><td>0.5</td><td>77.7</td><td>86.5</td><td>82.7</td><td>84.5</td><td>54.5</td><td>60.4</td><td>56.9</td><td>70.7</td></tr><tr><td> $IG_{All}$ </td><td>75.5</td><td>0.5</td><td>75.8</td><td>88.4</td><td>77.8</td><td>82.6</td><td>51.0</td><td>68.5</td><td>57.6</td><td>70.1</td></tr><tr><td> $PMI_{BiScr}$ </td><td>78.3</td><td>0.5</td><td>78.7</td><td>86.4</td><td>84.2</td><td>85.2</td><td>56.8</td><td>60.0</td><td>58.1</td><td>71.7</td></tr><tr><td> $TFIDF_{BiScr}$ </td><td>77.3</td><td>0.5</td><td>77.7</td><td>86.5</td><td>82.6</td><td>84.4</td><td>54.4</td><td>60.7</td><td>57.0</td><td>70.7</td></tr><tr><td> $IG_{BiScr}$ </td><td>75.6</td><td>0.5</td><td>76.0</td><td>88.6</td><td>77.8</td><td>82.7</td><td>51.2</td><td>69.2</td><td>58.0</td><td>70.3</td></tr></table>

Please cite this article as: N. Oliveira, et al., Stock market sentiment lexicon acquisition using microblogging data and statistical measures, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.013

Table 8  
Paired Student’s t-test and the Wilcoxon signed rank test for pairwise comparison of lexicons using unique and two context scores. The following symbols denote significance at the 5% level: a — paired Student’s t-test for F ; b — Wilcoxon signed rank test for $\mathrm { F _ { A v g } ; c - }$ paired Student’s t-test for CC1; d — Wilcoxon signed rank test for CC1. Alternative hypothesis: lexicon in the row has higher values than the lexicon in the column.

<table><tr><td></td><td> $PMI_{All}$ </td><td> $TFIDF_{All}$ </td><td> $IG_{All}$ </td><td> $PMI_{BiScr}$ </td><td> $TFIDF_{BiScr}$ </td><td> $IG_{BiScr}$ </td></tr><tr><td> $PMI_{All}$ </td><td>-</td><td>ab</td><td>abcd</td><td></td><td>ab</td><td>abcd</td></tr><tr><td> $TFIDF_{All}$ </td><td></td><td>-</td><td>acd</td><td></td><td></td><td>cd</td></tr><tr><td> $IG_{All}$ </td><td></td><td></td><td>-</td><td></td><td></td><td></td></tr><tr><td> $PMI_{BiScr}$ </td><td>cd</td><td>abcd</td><td>abcd</td><td>-</td><td>abcd</td><td>abcd</td></tr><tr><td> $TFIDF_{BiScr}$ </td><td></td><td></td><td>acd</td><td></td><td>-</td><td>cd</td></tr><tr><td> $IG_{BiScr}$ </td><td></td><td></td><td>abcd</td><td></td><td></td><td>-</td></tr></table>

scores of all $\mathrm { P M I _ { B i S c r } }$ items for both contexts. We can observe that the sentiment reversion in negation is not always appropriate. Indeed, only 41% have their sentiment orientation modified in negated contexts. Moreover, many items have much stronger sentiment value in negated contexts than in afirmative contexts and vice-versa. For example, the term bearish has $\texttt { a } - 6 . 6 3 4$ score in afirmative contexts and just −0.794 in negated contexts. For instance, saying “not bearish” does not signify the same as being bullish. Usually it just means that the opinion is not pessimistic. In the opposite situation, bailout has −5.392 points for negated contexts and only −0.657 for afirmative segments. The refusal of a bailout may imply the business downfall while its application may not necessarily mean a successful future. Negation handling is not a straightforward procedure, it may vary according to each term. Thus, the use of two context scores may be very useful in this matter. The $\mathsf { P M I } _ { \mathrm { B i S c r } }$ lexicon created using the first 75% labeled messages is available at https://github. com/nunomroliveira/stock\_market\_lexicon.

## 4.2. Correlation with survey sentiment indicators

To evaluate the relevance of microblogging sentiment indicators created using the stock market lexicon, we assess the association between Twitter sentiment indicators and two popular survey sentiment indicators: AAII and II. A strong correlation may indicate that the microblogging sentiment indicator can be an acceptable alternative or proxy. The correlation calculation uses 112 observations for AAII and 110 observations for II. Table 9 presents the respective Pearson’s correlation values.

![](/api/attachments/K3ZTFHXP/fulltext/images/2ef9956fcde5545031720f16bc1c61639270e166e1d33b305a8166942fd198d1.jpg)  
Fig. 2. Distribution of sentiment scores for afirmative and negated contexts.

Table 9  
Pearson’s correlation values of Twitter sentiment indicators with survey sentiment indicators (best correlation values for each survey sentiment value in bold).

<table><tr><td>Pair</td><td>Correlation</td><td>Pair</td><td>Correlation</td></tr><tr><td> $(TWTSML_{bear}, AAI_{bear})$ </td><td>0.489*</td><td> $(TWTSWN_{bear}, AAI_{bear})$ </td><td>0.436*</td></tr><tr><td> $(TWTSML_{bull}, AAI_{bull})$ </td><td>0.233**</td><td> $(TWTSWN_{bull}, AAI_{bull})$ </td><td>0.220**</td></tr><tr><td> $(TWTSML_{spread}, AAI_{spread})$ </td><td>0.376*</td><td> $(TWTSWN_{spread}, AAI_{spread})$ </td><td>0.342*</td></tr><tr><td> $(TWTSML_{bear}, II_{bear})$ </td><td>0.540*</td><td> $(TWTSWN_{bear}, II_{bear})$ </td><td>0.628*</td></tr><tr><td> $(TWTSML_{bull}, II_{bull})$ </td><td>0.533*</td><td> $(TWTSWN_{bull}, II_{bull})$ </td><td>0.445*</td></tr><tr><td> $(TWTSML_{spread}, II_{spread})$ </td><td>0.585*</td><td> $(TWTSWN_{spread}, II_{spread})$ </td><td>0.551*</td></tr></table>

<sup>∗</sup> p-value < 0.01.  
<sup>∗∗</sup> p-value < 0.05.

The obtained results show that Twitter sentiment indicators have a statistical significant moderate correlation with diverse survey sentiment values. Indeed, only the bullish value of AAII is poorly correlated with both Twitter sentiment indicators. II indicators present higher correlation values than AAII, so it may indicate that Twitter users posting about stock market are informed traders because II is more associated to professional investors than AAII [51]. Moreover, sentiment indicators produced with the selected stock market lexicon (SML, i.e., $\mathrm { P M I _ { B i S c r } ) }$ are more correlated to almost all survey sentiment values than indicators created with the selected baseline lexicon (i.e., SWN). Only $\mathrm { I I } _ { \mathrm { b e a r } }$ is less correlated with TWTSML values than with TWTSWN values.

Sentiment indicators created using automated computational methods have various advantages regarding the traditional sentiment indicators produced from surveys. For instance, the creation of these sentiment indicators is faster and cheaper, permits higher frequencies (e.g., daily) and may be targeted to a more restricted set of stocks (e.g., stock market indices or individual stocks). Therefore, the application of SA in microblogging data may constitute a valuable alternative to the creation of investor sentiment indicators. Additionally, the utilization of stock market lexicons allows an easy and fast unsupervised production of these indicators.

## 5. Conclusions

With the expansion of social media (e.g., Twitter, message boards), the interest in sentiment analysis (SA) is increased, allowing the summary of opinions from large amounts of opinionated messages and thus supports decision-making in several domains, including stock markets. A sentiment lexicon is a crucial resource for SA, enabling an easy and fast unsupervised SA and avoiding the expensive and arduous task of manually labeling data. Moreover, opinion lexicons permit the creation of very informative features for supervised SA. However, there are very few financial lexicons (e.g., [15,16]) and the existing domain independent lexicons $( \mathbf { e . g . , [ 1 7 - 1 9 ] } )$ may not be adjusted to the stock market domain.

In this paper, we propose an automated and fast approach to create stock market lexicons for microblogging messages. We employed a large labeled data set of StockTwits messages and tested three adaptations and two novel statistical measures to calculate the sentiment score. Also, we suggest the use of sentiment scores for afirmative and negated contexts in order to improve the dificult task of negation processing. The results on the test data confirmed that these newly created lexicons substantially increase the SA when compared with six reference lexicons. The improvements in evaluation metrics obtained by the created lexicons are statistically significant. Furthermore, the use of the proposed complementary metrics proved to be useful. Lexicons applying any of these measures obtain statistically higher evaluation results in SA than their counterparts that do not use the complementary metrics. Moreover, the utilization of afirmative and negated context scores appears to be beneficial. Lexicons applying these measures improve or maintain almost all evaluation results compared to their counterparts. Some of these improvements are statistically significant. A substantial contribution of this work is to make publicly available a large stock market lexicon with context scores. This is accessable at: https://github.com nunomroliveira/stock\_market\_lexicon.

Also in this work, we selected a stock market lexicon (SML, i.e., $\mathrm { P M I _ { B i S c r } ) }$ and a baseline lexicon (SWN) to easily generate investor sentiment indicators from Twitter messages holding cashtags of stocks traded in US markets. Twitter based sentiment indicators showed a significant moderate Pearson’s correlation with the widely applied AAII and II survey sentiment indicators. Therefore, the Twitter based sentiment indicator can be used as an acceptable proxy for survey sentiment indicators. Moreover, the sentiment indicators created with the proposed lexicon showed higher correlation values than indicators produced with the baseline lexicon in five of the six analyzed survey indicators. A microblogging sentiment indicator presents several advantages when compared with survey sentiment indicators: it is faster and cheaper to produce, it allows higher frequencies (e.g., daily) and it can be adjusted to both stock market indices and individual stocks.

The proposed procedure allows the fast and effortless creation of a lexicon properly adapted to stock market contents. This lexicon may permit an easy and effective unsupervised SA related to the stock market domain, such as the creation of investor sentiment indicators. However, this process requires labeled stock market documents and such data sets are in short supply.

Our results suggest that the proposed microblogging sentiment lexicon approach might be a useful source of information for stock market participants, and this merits future research. For instance, a collective intelligence approach can be used to more easily assign sentiments to unlabeled text and identify stock market terms, thus widening the applicability of the proposed procedure to other stock market message sources (e.g., Twitter) and producing more accurate and comprehensive lexicons. Active learning algorithms may complement this approach by automatically selecting a reduced but more relevant set of text messages for human classification, thus reducing the manual labeling effort. Moreover, it is important to analyze the informative content of microblogging sentiment indicators to forecast stock market behavior. Sentiment indicators created by SA using stock market lexicons can be included in models to predict diverse stock market variables (e.g., returns, trading volume, volatility) in order to assess their predictive ability. In future work, we will also explore other text processing possibilities, such as the inclusion of exclamation points or question marks, which could be relevant in microblogs.

## Acknowledgments

This work was supported by FCT — Fundação para a Ciência e Tecnologia within the Project Scope UID/CEC/00319/2013. We would like to thank the anonymous reviewers for their helpful suggestions. We also thank StockTwits for the provision of their data.

## References

[1] Andrés Montoyo, Patricio Martínez-Barco, Alexandra Balahur, Subjectivity and sentiment analysis: an overview of the current state of the area and envisaged developments, Decision Support Systems 53 (4) (2012) 675–679.

[2] Hu Minqing, Bing Liu, Mining and summarizing customer reviews, Proceedings of the 2004 ACM SIGKDD international conference on Knowledge discovery and data mining KDD 04 04.2 (2004) 168

[3] Svetlana Kiritchenko, Xiaodan Zhu, Saif Mohammad, Sentiment analysis of short informal texts, Journal of Artificial Intelligence Research 50 (2014) 723–762.

[4] Hassan Saif, Yulan He, Harith Alani, Semantic sentiment analysis of Twitter, The Semantic Web-ISWC 2012, Springer 2012, pp. 508–524.

[5] Nádia FF da Silva, Eduardo R. Hruschka, Estevam R. Hruschka, Tweet sentiment analysis with classifier ensembles, Decision Support Systems 66 (2014) 170–179.

[6] E. Fersini, E. Messina, F.A. Pozzi, Sentiment analysis: Bayesian ensemble learning, Decision Support Systems 68 (2014) 26–38.

[7] Sara Rosenthal, Preslav Nakov, Svetlana Kiritchenko, Saif M Mohammad, Alan Ritter, Veselin Stoyanov, Semeval-2015 task 10: sentiment analysis in Twitter, Proceedings of the 9th International Workshop on Semantic Evaluation, SemEval, 2015.

[8] Ronen Feldman, Techniques and applications for sentiment analysis, Communications of the ACM 56 (4) (2013) 82–89.

[9] Werner Antweiler, Murray Z. Frank, Is all that talk just noise? The information content of internet stock message boards, The Journal of Finance 59 (3) (2004) 1259–1294.

[10] Robert P. Schumaker, Yulei Zhang, Chun-Neng Huang, Hsinchun Chen, Evaluating sentiment in financial news articles, Decision Support Systems 53 (3) (2012) 458–464.

[11] Robert P. Schumaker, Hsinchun Chen, Textual analysis of stock market prediction using breaking financial news: the AZFin text system, ACM Transactions on Information Systems (TOIS) 27 (2) (2009) 12

[12] Yu Yang, Wenjing Duan, Qing Cao, The impact of social and conventional media on firm equity value: a sentiment analysis approach, Decision Support Systems 55 (4) (2013) 919–926.

[13] Johan Bollen, Huina Mao, Xiaojun Zeng, Twitter mood predicts the stock market, Journal of Computational Science 2 (1) (2011) 1–8.

[14] Nuno Oliveira, Paulo Cortez, Nelson Areal, On the predictability of stock market behavior using StockTwits sentiment and posting volume, Progress in Artificial Intelligence, Vol. 8154 of Lecture Notes in Computer Science, Springer Berlin Heidelberg 2013, pp. 355–365.

[15] Tim Loughran, Bill McDonald, When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks., Journal of Finance 66 (1) (2011) 35–65.

[16] Huina Mao, Pengjie Gao, Yongxiang Wang, Johan Bollen, Automatic construction of financial semantic orientation lexicon from large-scale Chinese news corpus, 7th Financial Risks International Forum, Institut Louis Bachelier 2014,

[17] P.J. Stone, D.C. Dunphy, M.S. Smith, D.M. Ogilvie, The General Inquirer: A Computer Approach to Content Analysis, vol. 08. MIT Press 1966.

[18] Theresa Wilson, Paul Hoffmann, Swapna Somasundaran, Jason Kessler, Janyce Wiebe, Yejin Choi, Claire Cardie, Ellen Riloff, Siddharth Patwardhan, Opinion-Finder : A System For Subjectivity Analysis October, October 2005, 34–35.

[19] Stefano Baccianella, Andrea Esuli, Fabrizio Sebastiani, SentiWordNet 3.0: An enhanced lexical resource for sentiment analysis and opinion mining, Proceedings of the Seventh Conference on International Language Resources and Evaluation LREC10, vol. 0, European Language Resources Association (ELRA) 2010, pp. 2200–2204.

[20] Saif Mohammad, Cody Dunne, Bonnie Dorr, Generating high-coverage semantic orientation lexicons from overtly marked words and a thesaurus, Pro ceedings of the 2009 Conference on Empirical Methods in Natural Language Processing, Vol. 2 of EMNLP ’09, Association for Computational Linguistic 2009 pp. 599-608

[21] Peter D. Turney, Michael L. Littman, Measuring praise and criticism: inference of semantic orientation from association ACM Transactions on Information Systems 21 (4) (2003) 315–346.

[22] Vasileios Hatzivassiloglou, Janyce M. Wiebe, Effects of adjective orientation and gradability on sentence subjectivity, Proceedings of the 18th Conference on Computational Linguistics—Volume 1, Association for Computational Linguistics 2000, pp. 299–305

[23] Yejin Choi, Claire Cardie, Adapting a polarity lexicon using integer linear programming for domain-specific sentiment classification, Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing: Volume 2-Volume 2, Association for Computational Linguistics 2009, pp. 590–598.

[24] Iadh Ounis, Craig Macdonald, Ian Soboroff, On the TREC Blog Track., ICWSM, 2008.

[25] Hoa Trang Dang, Karolina Owczarzak, Overview of the tac 2008 opinion question answering and summarization tasks, Proc. of the First Text Analysis Conference, 2008.

[26] Alistair Kennedy, Diana Inkpen, Sentiment classification of movie reviews using contextual valence shifters, Computational intelligence 22 (2) (2006) 110–125.

[27] V. Hatzivassiloglou, K.R. McKeown, Predicting the semantic orientation of adjectives, Proceedings of the 35th Annual Meeting of the Association for Computational Linguistics and Eighth Conference of the European Chapter of the Association for Computational Linguistics, 1997. pp. 181

[28] Janyce Wiebe, Learning subjective adjectives from corpora, AAAI/IAAI, 2000. pp. 735–740.

[29] Dekang Lin, Automatic retrieval and clustering of similar words, Proceedings of the 36th Annual Meeting of the Association for Computational Linguistics and 17th International Conference on Computational Linguistics—Volume 2, Association for Computational Linguistics 1998, pp. 768-774

[30] Guang Qiu, Bing Liu, Bu Jiajun, Chun Chen, Opinion word expansion and target extraction through double propagation, Computational Linguistics 37 (1) (2011) 9–27.

[31] J. Kamps, R.J. Mokken, M. Marx, M. De Rijke, Using WordNet to measure semantic orientation of adjectives, Proceedings of the 4th International Conference on Language Resources and Evaluation LREC 2004, vol. 4, Citeseer 2004, pp. 1115–1118.

[32] Soo-Min Kim, Eduard Hovy, Determining the sentiment of opinions, Proceedings of the 20th International Conference on Computational Linguistics, Association for Computational Linguistics 2004, pp. 1367

[33] Andrea Esuli, Fabrizio Sebastiani, Determining the semantic orientation of terms through gloss classification, Proceedings of the 14th ACM International Conference on Information and Knowledge Management, ACM 2005, pp. 617–624.

[34] Alena Neviarouskaya, Helmut Prendinger, Mitsuru Ishizuka, SentiFul: A lexicon for sentiment analysis, Affective Computing, IEEE Transactions on 2 (1) (2011) 22–36.

[35] Hiroya Takamura, Takashi Inui, Manabu Okumura, Extracting semantic orientations of words using spin model, Proceedings of the 43rd Annual Meeting on Association for Computational Linguistics, Association for Computational Linguistics 2005, pp. 133–140.

[36] Lu Yue, Malu Castellanos, Umeshwar Dayal, ChengXiang Zhai, Automatic construction of a context-aware sentiment lexicon: an optimization approach, Proceedings of the 20th International Conference on World Wide Web, ACM 2011, pp. 347–356.

[37] Dan Tufi ¸s, Dan ¸Stefanescu, Experiments with a differential semantics anno-˘ tation for WordNet 3.0, Decision Support Systems 53 (4) (2012) 695–703.

[38] Daniel E. O’Leary, Blog mining-review and extensions: “From each according to his opinion”, Decision Support Systems 51 (4) (2011) 821–830

[39] Sérgio Moro, Paulo Cortez, Paulo Rita, A data-driven approach to predict the success of bank telemarketing, Decision Support Systems 62 (2014) 22–31

[40] R. Core Team, R: A Language and Environment for Statistical Computing, R Foundation for Statistical Computing, Vienna, Austria, 2013, http://www.Rproject.org/.

[41] Kristina Toutanova, Dan Klein, Christopher D. Manning, Yoram Singer, Feature-rich part-of-speech tagging with a cyclic dependency network, Proceedings of the 2003 Conference of the North American Chapter of the Association for Computational Linguistics on Human Language Technology NAACL 03, 1, June 2003. pp. 173–180.

[42] David D. Lewis, An evaluation of phrasal and clustered representations on a text categorization task, Proceedings of the 15th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR ’92, ACM, New York, NY, USA, 1992, pp. 37–50.

[43] Zhaohui Zheng, Wu Xiaoyun, Rohini Srihari, Feature Selection for Text Categorization on Imbalanced Data. 2004

[44] Malcolm Baker, Jeffrey Wurgler, Investor sentiment in the stock market, Journal of Economic Perspectives 21 (2) (2007) 129–151.

[45] Kenneth L. Fisher, Meir Statman, Investor sentiment and stock returns, Financial Analysts Journal 56 (2) (2000) 16–23.

[46] Malcolm Baker, Jeffrey Wurgler, Investor sentiment and the cross-section of stock returns, The Journal of Finance 61 (4) (2006) 1645–1680.

[47] Malcolm Baker, Jeffrey Wurgler, Yu Yuan, Global, local, and contagious investor sentiment, Journal of Financial Economics 104 (2) (2012) 272–287.

[48] Oh Chong, Olivia R. Liu Sheng, Investigating predictive power of stock micro blog sentiment in forecasting future stock price directional movement, ICIS 2011 Proceedings, AIS, Shanghai, China, 2011,

[49] Timm O. Sprenger, Andranik Tumasjan, Philipp G. Sandner, Isabell M. Welpe, Tweets and trades: the information content of stock microblogs, European Financial Management 20 (5) (2014) 926–957.

[50] Michael Hagenau, Michael Liebmann, Dirk Neumann, Automated news reading: stock price prediction based on financial news using context-capturing features, Decision Support Systems 55 (3) (2013) 685–697.

[51] Gregory W. Brown, Michael T. Cliff, Investor sentiment and the near-term stock market, Journal of Empirical Finance 11 (1) (2004) 1–27.

[52] Rahul Verma, Gökçe Soydemir, The impact of individual and institutional investor sentiment on the market price of risk, The Quarterly Review of Economics and Finance 49 (3) (2009) 1129–1145.

![](/api/attachments/K3ZTFHXP/fulltext/images/af034c79a3d2a4bae9833db02b7fdca403b7dde6e8831e9a1c9184abd6ca2d12.jpg)

Nuno Oliveira is a PhD student in the Doctoral Program on Information Systems and Technologies at Universit of Minho. He holds a Master of Science in Information Systems Engineering and Management and a Bachelor’s degree in Business Informatics from the same university. His research interests include: sentiment analysis, natural language processing, social media and data mining.

![](/api/attachments/K3ZTFHXP/fulltext/images/5cb132f688c5d362778e539a4eba1d34acebb2127ce8e6be80a58fbbab264509.jpg)

Paulo Cortez is an Associate Professor at the Department of Information Systems at University of Minho and Coordinator of the Information Systems and Technologies R&D group of ALGORITMI Research Centre. He completed his PhD (2002) in Computer Science and Habilitation (2013) in Information Systems and Technologies at the same university. His research interests include: business intelligence, data mining, neural networks, evolutionary computation and forecasting. Currently, he is an associate editor of the journals Expert Systems and Neural Processing Letters. He has published more than 92 indexed (ISI or Scopus) papers. His research has appeared in Journal of Heuristics, Decision Support Systems, Information Sciences and others (see http://www3.dsi.uminho.pt/ pcortez).

![](/api/attachments/K3ZTFHXP/fulltext/images/78ae9713c69b0e0ea9674d3178efb7b622d1bc900248e319a2a61eee86c077c0.jpg)

Nelson Areal is an Assistant Professor at the School of Economics and Management, University of Minho. His research interests are in risk measures and forecasting, option valuation using numerical methods, performance measurement and social responsible investments. His work has appeared in various international journals, such as: European Journal of Finance, International Journal of Finance & Economics, Journal of Futures Markets, Journal of Business Ethics, Review of Derivatives Research, Quantitative Finance. He obtained his PhD in Accounting and Finance from Lancaster University (UK). He has regularly presented his research at international academic conferences and seminars.
