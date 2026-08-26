---
otero_id: 5560
otero_key: "EXGDEFSV"
title: "Semantic similarity of short texts in languages with a deficient natural language processing support"
authors: "Bojan Furlan; Vuk Batanović; Boško Nikolić"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.02.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Semantic similarity of short texts in languages with a de<sup>fi</sup>cient natural language processing support

Bojan Furlan ⁎, Vuk Batanović, Boško Nikolić

School of Electrical Engineering, Department of Computer Engineering and Information Theory, University of Belgrade, 11120 Belgrade, Serbia

## a r t i c l e i n f o

Article history: Received 22 June 2012 Received in revised form 17 December 2012 Accepted 8 February 2013 Available online 17 February 2013

Keywords: Linguistic tools for IS modeling Text DBs Semantic similarity of words Similarity of short texts Corpus-based measures Paraphrase corpora construction

## a b s t r a c t

Measuring the semantic similarity of short texts is a noteworthy problem since short texts are widely used on the Internet, in the form of product descriptions or captions, image and webpage tags, news headlines, etc. This paper describes a methodology which can be used to create a software system capable of determining the semantic similarity of two given short texts. The proposed LInSTSS approach is particularly suitable for application in situations when no large, publicly available, electronic linguistic resources can be found for the desired language. We describe the basic working principles of the system architecture we propose, as well as the stages of its construction and use. Also, we explain the procedure used to generate a paraphrase corpus which is then utilized in the evaluation process. Finally, we analyze the evaluation results obtained from a system created for the Serbian language, and we discuss possible improvements which would increase system accuracy.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Semantic similarity is a concept by which a metric is given to groups of terms or documents based on the similitude of their meanings. This is a key concept in the understanding of natural languages, for it allows us to make meaningful comparisons and conclusions. That is why it plays such an important role in many <sup>fi</sup>elds of arti<sup>fi</sup>cial intelligence, like automatic categorization and summarization, machine translation, information retrieval etc. The short text semantic similarity (STSS) is a noteworthy problem since short texts are widely used on the Internet, in the form of product descriptions or captions, image and webpage tags, news headlines, etc. STSS also plays an important role in issues related to education and learning, such as the automated testing and grading tasks [10].

There are two main manners of determining STSS — using topological or statistical word-to-word similarity [9]. Topological similarity uses data models which contain information about sets of concepts, and their interrelatedness. Statistical similarity, on the other hand, employs vector state spaces in order to express word correlations extracted from a given text corpus. A great advantage of the statistical tack is that it does not require the existence of any word data models.

For the English language a variety of Natural Language Processing (NLP) resources and tools can be found. Unfortunately, the creation of such resources necessitates signi<sup>fi</sup>cant time and effort, which is why they still do not exist for many languages, rendering many existing English language STSS solutions inapplicable. That lack is especially evident in minor languages and in languages with complex grammar rules.

This is a problem that had to be tackled in our efforts to create an STSS method suitable for Serbian, a highly in<sup>fl</sup>ectional language with very limited electronic linguistic resources. Therefore, we decided to base our approach on the statistical similarity method, devising a system-building methodology which would be applicable not only to Serbian, but to other languages with similar issues as well. We named it LInSTSS (Language Independent Short Text Semantic Similarity).

The basic procedure applied when calculating statistical similarity is the construction of a semantic space using the word distribution in the text corpus. In such a space each word has its own context vector, and the semantic similarity of words is represented by the relation of their vectors. This conclusion is a consequence of the distributional hypothesis which claims that words with similar meanings tend to appear in similar contexts. The hypothesis does not imply that words must appear next to one another, but that they should appear alongside the same set of other words.

This paper is organized as follows: in Section 2 we review some related work and analyze existing NLP tools and the prospects of their use in the development of the LInSTSS system. In Section 3 we describe system construction and in Section 4 we give an account and an example of system operation. Section 5 contains an explanation of the evaluation process. We discuss evaluation results of the Serbian language system in Section 6. Finally, in Section 7, we summarize our work and consider future system applications and improvements.

## 2. Analysis of available technologies and tools

Many quality STSS solutions, both topological and statistical, have already been developed. Yet, few of them are designed in a way that would make them adaptable to languages with a poor NLP support, since they often rely on advanced language-speci<sup>fi</sup>c processing techniques.

Mihalcea et al. [9] proposed a method for measuring the semantic similarity of two short texts (sentences or paragraphs) by using corpus-based and knowledge-based measures of word similarity. For each word in the text this method identi<sup>fi</sup>es the best match from the opposite text and then includes it in the overall measure of semantic similarity. This approach yields a high F-measure score, but it is computationally demanding and requires the use of a word data model. Islam and Inkpen [4] improved the similarity measure by combining a modi<sup>fi</sup>ed string matching algorithm with a corpus-based measure of semantic similarity. Semantic similarity also plays an important role in the task of recognizing textual entailment (RTE) and shares many features with it (e.g. Wang and Neumann [14]), but, as explained in [11], RTE is an asymmetric task, while determining semantic similarity is not, so a different tack is required.

Li et al. [7] proposed a method to determine sentence similarity that employs shallow parsing. Noun phrases, verb phrases and preposition phrases are extracted from the given sentences and the <sup>fi</sup>nal similarity is calculated as a combination of the similarities of these three kinds of phrases. Oliva et al. [11] combined semantic and syntactic information in their work as well. Syntax is analyzed through a deep parsing process to <sup>fi</sup>nd the phrases in each sentence. Similarity between concepts that play the same syntactic role is then calculated by using a lexical database. They also experimented with the utilization of psychological plausibility by differently weighing various syntactic roles. Regrettably, parsing tools for Serbian and for many other languages are nonexistent, making the proposed syntactic analysis techniques unfeasible.

Having considered the methods discussed above, we concluded that no existing solutions can be directly applied to the problem of determining STSS in Serbian. Hence, we decided to create our own approach, basing it on a modi<sup>fi</sup>cation of [4] due to the following reasons:

1. It does not use any external knowledge bases (e.g. WordNet), hand-crafted inference rules, or parsing tools, which would be an obstacle when dealing with languages that lack these resources.

2. Accuracy is the percentage of correct identi<sup>fi</sup>cations made by the system. Since it takes into account both false positive and false negative situations, it is one of the predominant parameters when comparing the qualities of different measures of semantic similarity. There are also others, like precision, recall, and F-measure. For each compared method these parameters were evaluated on the Microsoft Research Paraphrase Corpus (MSRPC), the largest English language paraphrase corpus consisting of 5801 pairs of sentences [2]. Methods that employ text parsing techniques [7,11] have shown high performance in F-measure and recall, but haven't reached a level of accuracy greater than [4], when evaluated on this corpus.

3. This method does not use the semantic similarity measure alone, but incorporates the string similarity measure as well, so it performs better with different forms of infrequent proper nouns, which is one of the main weaknesses of the knowledge-based measures [3]. While this advantage may not be so prominent in English, it is quite striking in highly in<sup>fl</sup>ectional languages that have many word forms. Consequently, evaluation results on English corpora may differ from the results derived for other languages.

In order to construct the STSS system, we had to review existing stemming tools and algorithms of measuring string and semantic similarities. We then ascertained their adaptability to the problem in question, and chose the best available solutions.

Stemming is a transformation by which a word suf<sup>fi</sup>x is stripped off without the loss of the word's main semantic content. This procedure can also be viewed as a normalization process in which several morphological variants are mapped to the same form. Stemming, therefore, reduces the number of different words since all the words with the same stem are mapped into a single form. It should be noted that stemmers are the only language-dependent tools used in our approach.

There are numerous stemmers developed for English, among which the Porter stemmer is the most famous one. However, for many languages, including Serbian, such tools are not free, or can be hard to <sup>fi</sup>nd in the public domain. Kešelj and Šipka [6] proposed a general suf<sup>fi</sup>x subsumption-based technique of building stemmers for highly in<sup>fl</sup>ectional languages with only sparse resources, which can be applied to Serbian. Their stemmer for Serbian has an experimentally evaluated accuracy of 81.83%.

String similarity is based upon the analysis of lexical matching of words or parts of words. It has been shown [4] that the best system accuracy can be gained by combining the results of string and semantical similarities. Hence, we apply the same practice to calculate string similarity by using three modi<sup>fi</sup>cations of the LCS (Longest Common Subsequence) algorithm and <sup>fi</sup>nding the average of their grades. We employ the following LCS modi<sup>fi</sup>cations:

NLCS Normalized Longest Common Subsequence

MCLCS<sub>1</sub> Maximal Consecutive Longest Common Subsequence starting at character 1

MCLCS Maximal Consecutive Longest Common Subsequence starting at character N

All three modi<sup>fi</sup>cations employ a normalization procedure in which their similarity scores are divided by the lengths of the two strings that are compared. This is a strength in comparison to other string similarity methods that do not take into account the length of the shorter string, which, in some situations, can have a noticeable impact on the <sup>fi</sup>nal grade. Furthermore, the combination of both consecutive and non-consecutive subsequence measures serves to balance out the score.

For measuring the word-to-word semantic similarity we use readymade corpus processing algorithms from the S-Space package [5], which also incorporates many tools for corpus pre- and post-processing. The corpus processing algorithms utilize a co-occurrence matrix in which every row represents a unique word, and every column stands for a unique context. A matrix cell contains the number of occurrences of the row-word in the given column-context. A context can be a document or a region around a word, depending on the algorithm. In case it is a document, context vector dimension will correspond to the total number of documents, whereas in the case of a region-sized context that dimension can, in the worst case, correspond to the total number of different words found in the corpus. In this paper we applied the following algorithms:

COALS Correlated Occurrence Analogue to Lexical Semantic [12] RI Random Indexing [13]

We chose COALS because it achieves a more consistent accuracy in predicting human similarity judgments than the older algorithms like HAL (Hyperspace Analogue to Language) [12]. Furthermore, unlike LSA (Latent Semantic Analysis), which expects sets of documents as the input material [1], COALS makes use of an undifferentiated text corpus, and employs a moving window to de<sup>fi</sup>ne word collocations. This makes the size of a COALS co-occurrence matrix almost <sup>fi</sup>xed, unlike an LSA matrix whose dimension is proportional to the number of documents. Therefore, COALS proves to be far more scalable and easy to implement in situations requiring the use of large text corpora.

However, this scalability is achieved by using a computationally demanding technique of word space dimension reduction called SVD (Singular Value Decomposition), an algebraic operation which employs matrix factorization and decomposition. This approach is costly in terms of memory consumption, and can be unfeasible for especially large corpora, where initial word space sizes can be huge. For that reason we also considered the RI algorithm, an incremental word space model which does not require a separate dimension reduction phase, making it particularly suitable for big corpora processing.

Finally, to measure the similarity of a word pair, we determine its string and semantic similarity and combine them into a similarity score. These scores are then used to calculate the overall similarity of two text segments. The similarity score for each word pair is weighed by taking into account the speci<sup>fi</sup>city of its words. In order to improve the results of our method, we expressed the word speci<sup>fi</sup>city by utilizing a normalized term frequency weighing scheme, which gives a higher weight to pairs with more speci<sup>fi</sup>c words.

## 3. System construction

The work<sup>fl</sup>ow of our system construction process is shown in Fig. 1. It depicts the stages of semantic space creation.

Corpus acquisition deals with <sup>fi</sup>nding a suf<sup>fi</sup>ciently large set of texts that could be used to generate a semantic space. Numerous such corpora can be found in English, free of charge, but procuring one in a language like Serbian can prove to be a task with limited options. A good, publicly available one was found in the corpus of article abstracts from the Wikipedia in Serbian, which, at the time, comprised 479,990 pages totaling over 186 megabytes.

Corpus parsing is necessary so as to remove any super<sup>fl</sup>uous information from further consideration. In our article abstract corpus, the abstracts themselves are enclosed by speci<sup>fi</sup>c XML tags, but the corpus <sup>fi</sup>le also contains other, irrelevant data.

Corpus preprocessing serves to reduce the amount of different words in the corpus, effectively reducing the context vector dimension, and, in effect, the load on computer resources. In the LInSTSS approach preprocessing is done in three steps:

1. Text cleaning — this includes the deletion of all text characters not belonging to the native script of the language in question, the removal of numbers and words that contain numbers, the elimination of punctuation marks and the shifting of all capital letters into lower case.

![](/api/attachments/EXGDEFSV/fulltext/images/08b0ff983cd2f3de78eadb0faaa9f7ab752557e6781b7d44ca829b163d01fdec.jpg)  
Fig. 1. System construction work<sup>fl</sup>ow. It depicts the stages of semantic space creation.

2. Stop-words removal — stop-words are auxiliary words like prepositions, pronouns, interjections and conjunctions, which carry negligible semantic information, but which are often encountered due to their language function. By removing those words, we decrease the total number of different words in the corpus. The result is that the semantic space is reduced and the accuracy of the semantic algorithms is increased, since the links between semantically important words become more emphasized. The stop-word list utilized in our Serbian language system was formed by gathering the most fre quent words from the text corpus [8]. Given that the corpus that we used contains general knowledge taken from an encyclopedia, we expected that the individual word frequencies within it would relatively accurately re<sup>fl</sup>ect the general word frequencies in the language itself. The information about word frequencies in the corpus which is gathered in this step is saved for later use in calculating various term frequencies (TFs) for each word.

3. Stemming — the employed corpus of article abstracts is coded in the UTF-8 format and is written partially in Cyrillic and partially in Latin alphabet, since Serbian is a digraphic language that can be written in either script. This posed a problem, since the utilized stemmer demands that input strings be formatted in a special dual1 version of the ASCII coding system in which every character with a diacritic ought to be represented by a combination of two plain ASCII characters. Hence, in order to preserve compatibility with the stemmer module, we had to construct a converter that would process the corpus text into this special coding system, before sending it to the stemmer.

Corpus processing consists of choosing an algorithm for the creation of the semantic space and supplying it with the preprocessed corpus text.

Corpus post-processing deals with the reduction of context vector dimension, i.e. with the reduction of the co-occurrence matrix, which scales down the computational complexity of determining sentence similarity. Each algorithm has its own post-processing routine which is encapsulated within the algorithm, as de<sup>fi</sup>ned in the S-Space package.

A separate part of post-processing involves the calculation of min–max TFs for all words found within the corpus. We obtain the min–max normalization of TF for each word by using the following formula:

$$
T F _ {\min - \max} = \frac {T F _ {\log}}{\max \left(T F _ {\log}\right)}\tag{1}
$$

where $T F _ { \mathrm { l o g } }$ is the log-number of times the given word appears in the corpus, and max $( T F _ { \mathrm { l o g } } )$ is the log-number of times the most frequently occurring word in the corpus appears in it. The TF log-number is calculated as follows:

$$
T F _ {\log} = - \log \left(\frac {T F _ {\text { count }}}{n}\right)\tag{2}
$$

where $T F _ { \mathrm { c o u n t } }$ is the occurrence count of the given word in the corpus, and n is the total number of words in the corpus.

Storing the semantic space on a hard drive is necessary in order to avoid recreating the whole semantic space at every program startup. Saving it as a single <sup>fi</sup>le is not practical due to poor performance achieved when trying to access a random part of a huge <sup>fi</sup>le. Hence, we decided to store the semantic space within a database, which utilizes an index structure, therefore providing an acceptable level of speed when searching and accessing data. The database holds two tables — one for the semantic space built by COALS, and another for the space created by RI. Both tables share the same structure, consisting of key, word, and context vector columns. Context vectors are recorded as long string variables. An additional database table is dedicated to storing the min–max TF values for all corpus words.

## 4. System operation

Determining the similarity of texts is done by using a bag-of-words approach based on a modi<sup>fi</sup>cation of [4], in which for each word in the shorter text P we <sup>fi</sup>nd the most similar matching word in the longer text R. Our modi<sup>fi</sup>cation is inspired by the method proposed in [9], which relies on a similar bag-of-words approach, but uses word speci<sup>fi</sup>city to weigh the word similarity. In the text to follow we will <sup>fi</sup>rst analyze issues related to methods [9] and [4], and then we will introduce our algorithm.

The problem of method [9] is that it has a tendency to overestimate text similarity because it allows multiple words from one text to be paired up with a single word in the other text. For example, let us consider the following text segments:

## 1. botanical gardens

## 2. plantation house

According to [9], both words in the <sup>fi</sup>rst segment would be linked up to the <sup>fi</sup>rst word (plantation) of the second segment. This would happen because method [9] pairs up each word in the <sup>fi</sup>rst segment with its most similar word in the second segment, and vice versa, regardless of whether a word has already been paired up. Due to this practice, many dissimilar sentence pairs will be, in fact, deemed similar. To some extent this problem is alleviated in [9] by measuring similarity only between words within the same part-of-speech class. However, as we have already noted, advanced NLP tools like part-of-speech taggers are not available in our case.

On the other hand, method [4] circumvents this issue by eliminating all paired up words from further consideration in the pairing process. In the previous example, the pair (gardens, plantation) would probably have the highest similarity, and would therefore be included in the overall score and then discarded. The similarity score would then be calculated for the remaining pair (botanical, house) after which it would be added to the similarity sum. This approach thus gives a more realistic result of the overall text similarity measure.

Still, method [9] improves its results by taking into account word speci<sup>fi</sup>city in the word similarity weighing. Therefore, we have decided to combine these two approaches by utilizing a normalized term frequency weighing scheme. To measure the similarity of a word pair, we <sup>fi</sup>rst determine its string similarity, and then the semantic one. This technique is then enhanced by using a term frequency ponderation. Particularly, for the ponderation of a word pair similarity score, we employ the following normalization formula:

$$
T F _ {\text { norm }} = 2 ^ {(T F 1 _ {\min - \max} \times T F 2 _ {\min - \max}) - 1}\tag{3}
$$

where $T F 1 _ { \mathrm { m i n - m a x } }$ is the min–max TF of the <sup>fi</sup>rst word, and TF2 is the min–max TF of the second word, as de<sup>fi</sup>ned in (1). By using this TF normalization technique, we are able to obtain normalized values for each word pair in the range [0.5, 1]. Very common words will have a low $T F _ { \mathrm { l o g } }$ value which means that their min–max TFs will be close to 0. This will, in turn, mean that all $T F _ { \mathrm { n o r m } }$ values for those words will be close to 0.5. On the other hand, rare words will have a high $T F _ { \mathrm { l o g } }$ value, allowing them to have a min–max TF value close or equal to 1. Word pairs which consist of rare words will, thus, have a $T F _ { \mathrm { n o r m } }$ value close or equal to 1. In effect, when using normalized TFs in a similarity score ponderation, word pairs made up of rare words will retain their full similarity score, while the scores of word pairs containing common words will be reduced by as much as 50%.

The system operation work<sup>fl</sup>ow is shown in Fig. 2. It depicts the stages of determining the numerical similarity score of two given short texts. We will describe the working of the system phase-by-phase, and demonstrate it by utilizing the COALS algorithm on a pair of sentences taken from our Serbian language paraphrase corpus. These sentences and their English translations are shown in Fig. 3.

![](/api/attachments/EXGDEFSV/fulltext/images/319b2daf6a711dae104281104d6c50e8f1256f22dbfde8217638cb4509b24d84.jpg)  
Fig. 2. System operation work<sup>fl</sup>ow. It depicts the stages of determining the numerical similarity score of two given short texts

Text preprocessing begins with the text cleaning procedure described in the Corpus preprocessing part of Section 3. It continues with the removal of stop words from the given texts, which are then converted into the aforementioned dual1 coding system. The remaining words from both texts are then stemmed. After this stage, our example sentence pair has the form shown in Fig. 4. We can see that the number of tokens in the <sup>fi</sup>rst text P, which we refer to as its length m, is 12, while the length n of the second text R is 17

Processing of words appearing in both texts starts with the identi<sup>fi</sup>- cation of those words. In our example, those words are the following: podizn, spusxtajucy, platfor, osob, ju, pescacxk, prolaz, and terazij. We consider their similarity scores to be equal to their normalized term frequencies, which are calculated using Eq. (3) as follows:

$$
T F _ {\text { norm }} = 2 ^ {T F _ {\min - \max} ^ {2} - 1}.\tag{4}
$$

We thus treat words appearing in both texts as a word pair which consists of two identical words. We automatically assign a min–max TF value of 1 to words like “podizn” which have not appeared in the corpus material. Table 1 displays the min–max term frequencies and similarity scores of these words. After calculating their similarity scores, we add them up into a similarity sum $S _ { s a m e } ,$ and then discard these words from further consideration. In our example, the value of the $S _ { s a m e }$ sum would be 6.319.

String similarity matrix construction creates a matrix in which every cell is occupied by a numerical value between 0 and 1 representing the string similarity between the column-word and the row-word. The rows of the matrix are used for the remaining words from the <sup>fi</sup>rst text, while the columns represent the remaining words from the second text. A zero value denotes entirely different string contents, while a value of one indicates a perfect string match. In Section 2 we have presented the approach which we have used to calculate string similarity. Table 2 shows the string similarity matrix which corresponds to the example sentence pair.

![](/api/attachments/EXGDEFSV/fulltext/images/c816a2c16b719c3de033b4619189f4c1bb4ab2063bba94f51d872fa833021788.jpg)  
Fig. 3. An example sentence pair taken from the Serbian language paraphrase corpus. Original sentences in Serbian are presented alongside their translations into English.

<table><tr><td>Text segment 1: podizn spusxtajucy platfor osob posebn potre ju pusx rad pesxacxk prolaz terazij</td></tr><tr><td>Text segment 2: osob invaliditet svi ima potesxkocy kretany ju mo kor podizn spusxtajucy platfor podzemn pesxacxk prolaz terazij beograd</td></tr></table>

Fig. 4. The example sentence pair after the text preprocessing stage.

Semantic similarity matrix construction creates a matrix in which every cell is occupied by a numerical value between 0 and 1 representing the semantic similarity between the column-word and the row-word. The rows of the matrix are used for the words from the <sup>fi</sup>rst text, while the columns represent the words from the second text. Similar to the string similarity measurement, a zero value denotes entirely different semantic contents, while a value of one indicates a perfect semantic match. We gain the semantic similarity of words in a pair by calculating the cosine similarity of their context vectors, read from the database. Table 3 shows the semantic similarity matrix obtained by utilizing the COALS algorithm on our example sentence pair.

Similarity matrix unification combines the string and the semantic similarity matrices into one by multiplying their values by a certain ponderation factor and adding them up. Experiments done on our Serbian language system have demonstrated that, in this case, optimal accuracy is attained by using ponderation values of 0.45 and 0.55 for the string and semantic similarity scores, respectively. Table 4 shows the uni<sup>fi</sup>ed similarity matrix which corresponds to our example sentence pair.

The TF matrix construction and ponderation phase begins with the creation of a normalized term frequency matrix in which every cell is occupied by a normalized TF value calculated using Eq. (3). Table 5 shows the normalized term frequency matrix which corresponds to our example sentence pair. The <sup>fi</sup>nal similarity matrix, shown in Table 6, is gained by multiplying each cell of the uni<sup>fi</sup>ed similarity matrix with the corresponding cell of the normalized TF matrix.

Min–max term frequencies and similarity scores of words appearing in both texts.

<table><tr><td>Word</td><td>Podizn</td><td>Spusxtajucy</td><td>Platfor</td><td>Osob</td><td>Ju</td><td>Pescacxk</td><td>Prolaz</td><td>Terazij</td></tr><tr><td> $TF_{\text{min-max}}$ </td><td>1.000</td><td>1.000</td><td>0.733</td><td>0.548</td><td>0.561</td><td>0.849</td><td>0.643</td><td>0.889</td></tr><tr><td>Similarity score</td><td>1.000</td><td>1.000</td><td>0.726</td><td>0.616</td><td>0.622</td><td>0.824</td><td>0.666</td><td>0.865</td></tr></table>

Best word pair selections start with the <sup>fi</sup>nal similarity matrix. The goal is to match words across the two texts according to their mutual similarity score. Hence, we search for the highest value within the <sup>fi</sup>nal similarity matrix, and add it to a similarity sum $S _ { d i f f e r e n t \cdot }$ We then remove the row and the column of the matrix to which the selected cell belonged, thereby discarding all other word pairs in which words from the chosen pair appeared. We repeat this procedure until there are no more rows and/or columns left in the matrix. This procedure is demonstrated step-by-step in Tables 6–11 where the highest value cell is marked in bold script.

Table 6 — The highest similarity score in our <sup>fi</sup>nal similarity matrix is the one for the (rad, beograd) word pair. After this <sup>fi</sup>rst step the S similarity sum has a value of 0.138.

Table 7 — The highest similarity score in the step 2 matrix is the one for the (posebn, podzemn) word pair. After the second step, the $S _ { d i f f e r e n t }$ similarity sum has a value of 0.224.

Table 8 — The highest similarity score in the step 3 matrix is the one for the (potre, potesxkocy) word pair. After the third step, the $S _ { d i f f e r e n t }$ similarity sum has a value of 0.3.

Table 9 — The highest similarity score in the step 4 matrix is the one for the (pusx, svi) word pair. After the fourth step, the $S _ { d i f f e r e n t }$ similarity sum reaches a <sup>fi</sup>nal value of 0.328.

The final similarity score calculation is performed by utilizing the following formula:

$$
S (P, R) = \frac {\left(S _ {s a m e} + S _ {d i f f e r e n t}\right) \times (m + n)}{2 m n .}\tag{5}
$$

In other words, the <sup>fi</sup>nal similarity score S(P,R) is gained by summing up the similarity scores of words that appear in both texts $\left( S _ { s a m e } \right)$ and the scores of word pairs formed from words unique to one of the texts $( S _ { d i f f e r e n t } )$ . Lastly, this sum is multiplied by a reciprocal harmonic mean function of the lengths of both texts, so as to achieve a <sup>fi</sup>nal text similarity score between 0 and 1. For our example sentence pair, the <sup>fi</sup>nal text similarity score will have the following value:

$$
S (P, R) = \frac {(6 . 3 1 9 + 0 . 3 2 8) \times (1 2 + 1 7)}{2 \times 1 2 \times 1 7 .} = 0. 4 7 2.
$$

Table 2 String similarity matrix.

<table><tr><td>Word</td><td>Invaliditet</td><td>Svi</td><td>Ima</td><td>Potesxkocy</td><td>Kretany</td><td>Mo</td><td>Kor</td><td>Podzemn</td><td>Beograd</td></tr><tr><td>Posebn</td><td>0.010</td><td>0.037</td><td>0.000</td><td>0.094</td><td>0.039</td><td>0.055</td><td>0.037</td><td>0.189</td><td>0.016</td></tr><tr><td>Potre</td><td>0.030</td><td>0.000</td><td>0.000</td><td>0.224</td><td>0.075</td><td>0.066</td><td>0.110</td><td>0.160</td><td>0.047</td></tr><tr><td>Pusx</td><td>0.000</td><td>0.055</td><td>0.000</td><td>0.116</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.035</td><td>0.000</td></tr><tr><td>Rad</td><td>0.050</td><td>0.000</td><td>0.073</td><td>0.000</td><td>0.079</td><td>0.000</td><td>0.073</td><td>0.031</td><td>0.283</td></tr></table>

Table 3  
Semantic similarity matrix.

<table><tr><td>Word</td><td>Invaliditet</td><td>Svi</td><td>Ima</td><td>Potesxkocy</td><td>Kretany</td><td>Mo</td><td>Kor</td><td>Podzemn</td><td>Beograd</td></tr><tr><td>Posebn</td><td>0.000</td><td>0.127</td><td>0.211</td><td>0.000</td><td>0.132</td><td>0.181</td><td>0.195</td><td>0.083</td><td>0.093</td></tr><tr><td>Potre</td><td>0.000</td><td>0.105</td><td>0.152</td><td>0.000</td><td>0.097</td><td>0.139</td><td>0.106</td><td>0.062</td><td>0.047</td></tr><tr><td>Pusx</td><td>0.000</td><td>0.029</td><td>0.054</td><td>0.000</td><td>0.027</td><td>0.034</td><td>0.048</td><td>0.020</td><td>0.043</td></tr><tr><td>Rad</td><td>0.000</td><td>0.131</td><td>0.191</td><td>0.000</td><td>0.150</td><td>0.200</td><td>0.204</td><td>0.085</td><td>0.198</td></tr></table>

Table 4  
Uni<sup>fi</sup>ed similarity matrix.

<table><tr><td>Word</td><td>Invaliditet</td><td>Svi</td><td>Ima</td><td>Potesxkocy</td><td>Kretany</td><td>Mo</td><td>Kor</td><td>Podzemn</td><td>Beograd</td></tr><tr><td>Posebn</td><td>0.005</td><td>0.086</td><td>0.116</td><td>0.042</td><td>0.090</td><td>0.124</td><td>0.124</td><td>0.131</td><td>0.058</td></tr><tr><td>Potre</td><td>0.014</td><td>0.058</td><td>0.084</td><td>0.101</td><td>0.087</td><td>0.106</td><td>0.108</td><td>0.106</td><td>0.047</td></tr><tr><td>Pusx</td><td>0.000</td><td>0.040</td><td>0.030</td><td>0.052</td><td>0.015</td><td>0.019</td><td>0.026</td><td>0.027</td><td>0.024</td></tr><tr><td>Rad</td><td>0.023</td><td>0.072</td><td>0.138</td><td>0.000</td><td>0.118</td><td>0.110</td><td>0.145</td><td>0.061</td><td>0.236</td></tr></table>

Table 5  
Normalized term frequency matrix.

<table><tr><td>Word</td><td>Invaliditet</td><td>Svi</td><td>Ima</td><td>Potesxkocy</td><td>Kretany</td><td>Mo</td><td>Kor</td><td>Podzemn</td><td>Beograd</td></tr><tr><td>Posebn</td><td>0.711</td><td>0.640</td><td>0.593</td><td>0.707</td><td>0.646</td><td>0.580</td><td>0.620</td><td>0.659</td><td>0.598</td></tr><tr><td>Potre</td><td>0.756</td><td>0.669</td><td>0.611</td><td>0.751</td><td>0.676</td><td>0.595</td><td>0.644</td><td>0.691</td><td>0.617</td></tr><tr><td>Pusx</td><td>0.810</td><td>0.702</td><td>0.632</td><td>0.804</td><td>0.711</td><td>0.613</td><td>0.672</td><td>0.730</td><td>0.640</td></tr><tr><td>Rad</td><td>0.679</td><td>0.620</td><td>0.580</td><td>0.676</td><td>0.625</td><td>0.569</td><td>0.603</td><td>0.636</td><td>0.585</td></tr></table>

As will be shown in Section 6, the optimal threshold value for our system is 0.407 when using the COALS algorithm. Therefore, the system would correctly identify the sentence pair from the example as one in which sentences are highly semantically related.

## 5. Evaluation resources

The main issue encountered in system evaluation is <sup>fi</sup>nding the work parameter values for which the system achieves maximal accuracy, which is the greatest level of matching between the system-designated similarity scores and the similarity grades that a human would give. In this regard, it is important to determine an optimal system similarity threshold which would serve as a boundary, such that all score values above it could be treated as an assessment of semantic similarity, and all values below it as an appraisal of semantic dissimilitude. The optimal threshold value is one for which the system reaches its maximal possible accuracy. In order to <sup>fi</sup>nd this threshold, a substantially large set of sentence pairs is needed. Sentences in a pair ought to overlap in their semantic content — some of them should represent actual paraphrases, while others should only be semantically related to an extent.

Nevertheless, a collection of such sentence pairs is usually called a paraphrase corpus. After manually assigning a binary grade to every pair in this corpus, it is possible to compare human-given grades and system similarity scores for each pair and, by using statistical analysis, to determine the optimal threshold value.

As a starting point, we reviewed the insights gained during the construction of the MSRPC [2]. The basic approach to building such a sentence pair corpus lies in the exploitation of a journalistic convention by which the <sup>fi</sup>rst few sentences of a news article usually contain a short summarization of the article content. Therefore, gathering multiple articles dealing with the same subject matter from different news sources and extracting their starting sentences are a good way of <sup>fi</sup>nding sentence pairs that are probably semantically comparable. The work<sup>fl</sup>ow of the evaluation resources creation is shown in Fig. 5. It depicts how a paraphrase corpus is created and processed before being put to use.

News corpus acquisition deals with <sup>fi</sup>nding a free and publicly available web news archive that allows for easy access to news articles for a desired date. A prime solution for our Serbian language system was the website www.vesti.rs. This site is a news aggregator which collects articles from all major media outlets in Serbia, including not only TV stations and newspapers, but Internet magazines and portals as well. In total, it makes use of over 210 different news sources. We decided to process only the top news stories for each date, because they have the highest probability of being covered by multiple outlets. Moreover, this ensured the procurement of various sentence pairs dealing with all kinds of topics, which prevented the paraphrase corpus from becoming too focused on a single point. We compiled the top news stories from 2010 and from the <sup>fi</sup>rst seven months of 2011 so as to provide us with enough material for corpus construction.

Parsing and evaluating news article texts is a necessary step after the collection of all news reports. The cleaning and parsing of obtained sentences are a particularly problematic task due to their completely unstructured format, the usage of periods not being limited to sentence endings, and the various forms of unnecessary information which ought to be removed (e.g. information about the news agency, and the location of the event). We assigned several descriptive attributes to every sentence pair that met certain minimal criteria concerning sentence length and the number of semantically signi<sup>fi</sup>cant words they contain. These attributes were used later on to determine the best sentence pair for every article. The attributes we used are: the number of long words in the shorter sentence, the number of long words in the longer sentence, and the number of long words which appear in both sentences, without counting word repetitions. “Long words” is a term we use for those words whose length makes them almost certainly semantically relevant. The minimal length required to deem a word semantically relevant depends, of course, on the language in question. For example, in Serbian there are many <sup>fi</sup>ve-letter prepositions and personal pronouns. Hence, we concluded that, in this case, we should set a long word minimal length of six letters.

Selecting the best sentence pairs out of all the pairs coupled to articles is performed by choosing the pair with the highest chances of being the best one for each article. This selection process required the calculation of a numerical quality score for each pair on the basis of its given attributes. An excellent quality sentence pair is one whose sentences provide the same semantic information, but conveyed in wholly different manners. Sentences regarded as being of poor quality are (a) those that are likely semantically diverse, or (b) those that are indeed semantically equivalent, but only due to a great level of string similarity between them. An example of a good quality sentence pair is already shown in Fig. 3. Examples of two poor quality pairs for cases (a) and (b) are given consecutively in Fig. 6. In conclusion, the main goal of the paraphrase corpus creation process is to achieve a suitably high percentage of semantically similar sentence pairs. While doing this, it is important to avoid as much as possible the common examples of semantic equivalence originating in a high level of string matching.

Table 6 Final similarity matrix

<table><tr><td>Word</td><td>Invaliditet</td><td>Svi</td><td>Ima</td><td>Potesxkocy</td><td>Kretany</td><td>Mo</td><td>Kor</td><td>Podzemn</td><td>Beograd</td></tr><tr><td>Posebn</td><td>0.003</td><td>0.055</td><td>0.069</td><td>0.030</td><td>0.058</td><td>0.072</td><td>0.077</td><td>0.086</td><td>0.035</td></tr><tr><td>Potre</td><td>0.010</td><td>0.038</td><td>0.051</td><td>0.076</td><td>0.059</td><td>0.063</td><td>0.069</td><td>0.073</td><td>0.029</td></tr><tr><td>Pusx</td><td>0.000</td><td>0.028</td><td>0.019</td><td>0.042</td><td>0.010</td><td>0.011</td><td>0.018</td><td>0.020</td><td>0.015</td></tr><tr><td>Rad</td><td>0.015</td><td>0.045</td><td>0.080</td><td>0.000</td><td>0.074</td><td>0.063</td><td>0.088</td><td>0.039</td><td>0.138</td></tr></table>

Table 7  
Best word pair selection — step 2.

<table><tr><td>Word</td><td>Invaliditet</td><td>Svi</td><td>Ima</td><td>Potesxkocy</td><td>Kretany</td><td>Mo</td><td>Kor</td><td>Podzemn</td></tr><tr><td>Posebn</td><td>0.003</td><td>0.055</td><td>0.069</td><td>0.030</td><td>0.058</td><td>0.072</td><td>0.077</td><td>0.086</td></tr><tr><td>Potre</td><td>0.010</td><td>0.038</td><td>0.051</td><td>0.076</td><td>0.059</td><td>0.063</td><td>0.069</td><td>0.073</td></tr><tr><td>Pusx</td><td>0.000</td><td>0.028</td><td>0.019</td><td>0.042</td><td>0.010</td><td>0.011</td><td>0.018</td><td>0.020</td></tr></table>

Table 8  
Best word pair selection — step 3.

<table><tr><td>Word</td><td>Invaliditet</td><td>Svi</td><td>Ima</td><td>Potesxkocy</td><td>Kretany</td><td>Mo</td><td>Kor</td></tr><tr><td>Potre</td><td>0.010</td><td>0.038</td><td>0.051</td><td>0.076</td><td>0.059</td><td>0.063</td><td>0.069</td></tr><tr><td>Pusx</td><td>0.000</td><td>0.028</td><td>0.019</td><td>0.042</td><td>0.010</td><td>0.011</td><td>0.018</td></tr></table>

We observed that giving preference to sentences of similar lengths that have around 50% of the same words yields the best results. When sentences in a pair have widely different lengths, the likelihood of them being real paraphrases is reduced. We also noticed that a high percentage of the same words appearing in both sentences greatly increases the chance that one sentence is a mere repetition of the other, with only some slight, semantically irrelevant new information added. On the other hand, a low percentage most often means that the pair is built out of two semantically diverse parts of news articles. Additionally, we assigned a greater weight to shorter sentence pairs, since for them each word plays a proportionately bigger part in the creation of the <sup>fi</sup>nal score.

Sentence pair grading is done manually. During the grading process, for some sentence pairs it was immediately clear what grade they should be given, but there were also pairs whose semantic information are somewhat similar, but not entirely. Since there were many such occurrences, it was obligatory to establish certain grading guidelines which would ensure the greatest possible uniformity of grading criteria. These guidelines are presented in Fig. 7, in a pseudocode form. Furthermore, in this stage we also corrected all typographical and other errors that originated in source text imperfections. Grading was performed by a single human judge, after which a second judge rated a random selection of corpus sentence pairs. This selection's size equaled 30% of the total corpus. The double-checking was done in order to estimate the inter-rater agreement, which is an important parameter since it dictates the upper bound for system accuracy. The inter-rater agreement observed on our control selection of sentence pairs was 78.27%.

Finally, using this procedure to create and prepare evaluation resources, we were able to acquire a Serbian language corpus consisting of 1194 sentence pairs. It includes 553 semantically equivalent pairs, and 641 pairs marked as semantically divergent. Percentage-wise, the semantically equivalent pairs comprise 46.31%, and the semantically divergent 53.69%.

Table 9  
Best word pair selection — step 4.

<table><tr><td>Word</td><td>Invaliditet</td><td>Svi</td><td>Ima</td><td>Kretany</td><td>Mo</td><td>Kor</td></tr><tr><td>Pusx</td><td>0.000</td><td>0.028</td><td>0.019</td><td>0.010</td><td>0.011</td><td>0.018</td></tr></table>

## 6. Evaluation results

The process of <sup>fi</sup>nding an optimal threshold value is initially performed on a larger sentence pair set called a Training data set. The obtained threshold value is afterwards veri<sup>fi</sup>ed on an independent Test data set, and, if it produces a satisfactory accuracy on it as well, then that value is adopted as the optimal one. The Training set for our Serbian language system is made up of 835 randomly selected sentence pairs (70% of the subtotal), while the Test set comprises 359 pairs (30% of the subtotal).

Various accuracies achieved during the scoring of the Serbian paraphrase corpus using a range of threshold values and the COALS algorithm are shown in Table 10. Accuracy represents the ratio of the number of correctly graded sentence pairs and the total number of pairs in the corpus. The threshold value was increased in steps of 0.001, so as to attain the maximal possible accuracy. The highest percentage of correctly identi<sup>fi</sup>ed pairs is gained by using a threshold value of 0.407, which leads to a system accuracy of 76.6%.

The expression True Positives (TP) stands for those sentence pairs which are paraphrases and are correctly identi<sup>fi</sup>ed as such by the algorithm. True Negatives (TN) encompasses dissimilar sentence pairs which are correctly recognized by the algorithm. False Positives (FP) consists of semantically dissimilar sentence pairs erroneously marked as paraphrases. False Negatives (FN) represents sentence pairs which are paraphrases but are incorrectly assessed as semantically different.

On the other hand, accuracies achieved during the scoring of the paraphrase corpus using a range of threshold values and the RI algorithm are shown in Table 11. The optimal threshold value is 0.417, which leads to a system accuracy of 76.6%.

Both COALS and RI reach a similar level of accuracy. However, timing tests performed during the evaluation process showed COALS to be consistently faster. This is probably due to the relatively small size of the text corpus utilized for semantic space creation, which prevented RI, an algorithm primarily devised for large corpora, from showing its strong suit in this regard.

In the information retrieval theory, precision (P), recall (R) and F-measure (F) are measures that are used extensively. They are calculated according to the following expressions:

![](/api/attachments/EXGDEFSV/fulltext/images/7b368045a325c50b63d2e614a25128872dd98f8a1be496294e78c5766e498b38.jpg)  
Fig. 5. Evaluation resources creation work<sup>fl</sup>ow. It depicts the stages of paraphrase corpus creation.

![](/api/attachments/EXGDEFSV/fulltext/images/76508e90bcd44280c7cc10f53775e630e2988266bbe00932f5205d90459830a8.jpg)  
Fig. 6. Examples of good and poor quality sentence pairs. Original sentences in Serbian are presented alongside their translations into English.

In the context of STSS, precision can be understood as the ratio of the number of correctly identi<sup>fi</sup>ed paraphrase sentence pairs and the total number of pairs marked as paraphrases by the algorithm. Recall represents the ratio between the correctly identi<sup>fi</sup>ed paraphrase sentence pairs and the real number of paraphrase sentence pairs in the corpus. F-measure is computed as the harmonic mean of precision and recall.

Table 12 displays a comparison of the main characteristics of some previously described methods, as well as the approach we propose. The <sup>fi</sup>rst three rows (1–3) present results of Mihalcea et al. [9], Islam and Inkpen [4], and Li et al. [7], which are evaluated on the Microsoft Research Paraphrase Corpus (MSRPC). The last three rows (4–6) present the results evaluated on our Serbian language paraphrase corpus (SRB). In order to perform a comparison, we implemented the steps of the method proposed in [4], but we used COALS and RI for measuring the semantic similarity of a word pair.

```vhdl
if semantic contents of sentences are completely different then
    assign grade 0;
else begin
    remove from consideration differences arising from the use of pronominal and noun phrase anaphora;
    if it is unclear whether sentences refer to the same event then
    assign grade 0;
    else if the sentences have the same subject matter but employ different rhetorical structures then
    assign grade 0;
    else if the sentences have the same subject matter but emphasize different aspects of it then
    assign grade 0;
    else begin
    if one sentence represents a semantic subset of the other then
    begin
    extract the information present only in the semantically richer sentence;
    if that information is not particularly important then
    assign grade 1;
    else
    assign grade 0;
    end;
    else begin
    compare the subjects, predicates and other important semantic features of both sentences;
    if there is a semantic discrepancy then
    assign grade 0;
    else
    assign grade 1;
    end;
end;
```  
Fig. 7. Guidelines for sentence pair grading. These guidelines are necessary in order to ensure the general uniformity of grading criteria

Table 10  
An overview of sentence pair scores gained by using the COALS algorithm.

<table><tr><td rowspan="3">Threshold</td><td colspan="6">Sentences correctly identified by the COALS algorithm</td></tr><tr><td colspan="2">Semantically equivalent $\frac{\text{TP}}{\text{TP}+\text{FN}}$ </td><td colspan="2">Semantically diverse  $\frac{\text{TN}}{\text{TN}+\text{FP}}$ </td><td colspan="2">Overall  $\frac{\text{TP}+\text{TN}}{\text{TP}+\text{FP}+\text{TN}+\text{FN}}$ </td></tr><tr><td>Training set</td><td>Test set</td><td>Training set</td><td>Test set</td><td>Training set</td><td>Test set</td></tr><tr><td>0.1</td><td>100%</td><td>100%</td><td>0%</td><td>0%</td><td>46.23%</td><td>46.52%</td></tr><tr><td>0.2</td><td>99.48%</td><td>100%</td><td>2.67%</td><td>2.6%</td><td>47.43%</td><td>47.91%</td></tr><tr><td>0.3</td><td>96.11%</td><td>97.01%</td><td>33.63%</td><td>38.02%</td><td>62.51%</td><td>65.46%</td></tr><tr><td>0.4</td><td>72.02%</td><td>71.86%</td><td>75.28%</td><td>77.6%</td><td>73.77%</td><td>74.93%</td></tr><tr><td>0.407</td><td>70.73%</td><td>71.26%</td><td>77.28%</td><td>81.25%</td><td>74.25%</td><td>76.6%</td></tr><tr><td>0.5</td><td>36.79%</td><td>35.93%</td><td>96.66%</td><td>96.88%</td><td>68.38%</td><td>68.52%</td></tr><tr><td>0.6</td><td>8.03%</td><td>8.98%</td><td>99.78%</td><td>100%</td><td>57.37%</td><td>57.66%</td></tr><tr><td>0.7</td><td>0.52%</td><td>0%</td><td>100%</td><td>100%</td><td>54.01%</td><td>53.48%</td></tr><tr><td>0.8</td><td>0%</td><td>0%</td><td>100%</td><td>100%</td><td>53.77%</td><td>53.48%</td></tr><tr><td>0.9</td><td>0%</td><td>0%</td><td>100%</td><td>100%</td><td>53.77%</td><td>53.48%</td></tr></table>

We obtained the best results in our implementation of [4] by using COALS, and we therefore used those results as a baseline, shown here in row 4. The last two rows (5–6) contain the results of the LInSTSS approach that we propose, in both COALS and RI variants.

The optimal threshold values for COALS and RI gravitate toward 0.4, which is also the case with [7]. Also, our implementation of method [4] evaluated on the SRB corpus has the same optimal threshold value as the original one evaluated on MSRPC.

Our approach leads to the highest recorded accuracy that is slightly higher than the baseline and which is just a few percentages short of the maximal possible system accuracy, given the inter-rater agreement (78.27%). It also has a signi<sup>fi</sup>cantly higher recall, at the cost of lower precision. The difference between these two measures is reduced in respect to the baseline method, so it improves the overall F-measure value. Also, since we used word speci<sup>fi</sup>city to weigh differently the similarity of word pairs, our approach is to some extent strict in assigning the semantic similarity label, which can be noted by comparing values close to the optimal threshold in the Semantically equivalent and Semantically diverse columns of Tables 10 and 11.

## 7. Conclusion

In this paper we described the LInSTSS approach to building a software system for determining the semantic similarity of short texts.

Table 11  
An overview of sentence pair scores gained by using the RI algorithm.

<table><tr><td rowspan="3">Threshold</td><td colspan="6">Sentences correctly identified by the RI algorithm</td></tr><tr><td colspan="2">Semantically equivalent  $\frac{TP}{TP+FN}$ </td><td colspan="2">Semantically diverse  $\frac{TN}{TN+FP}$ </td><td colspan="2">Overall  $\frac{TP+TN}{TP+FP+TN+FN}$ </td></tr><tr><td>Training set</td><td>Test set</td><td>Training set</td><td>Test set</td><td>Training set</td><td>Test set</td></tr><tr><td>0.1</td><td>100%</td><td>100%</td><td>0%</td><td>0%</td><td>46.23%</td><td>46.52%</td></tr><tr><td>0.2</td><td>99.48%</td><td>100%</td><td>1.56%</td><td>1.56%</td><td>46.83%</td><td>47.35%</td></tr><tr><td>0.3</td><td>97.41%</td><td>97.6%</td><td>30.29%</td><td>33.85%</td><td>61.32%</td><td>63.51%</td></tr><tr><td>0.4</td><td>73.58%</td><td>73.65%</td><td>72.38%</td><td>75.52%</td><td>72.93%</td><td>74.65%</td></tr><tr><td>0.417</td><td>69.95%</td><td>69.46%</td><td>77.95%</td><td>82.81%</td><td>74.25%</td><td>76.6%</td></tr><tr><td>0.5</td><td>38.08%</td><td>37.72%</td><td>95.99%</td><td>96.35%</td><td>69.22%</td><td>69.08%</td></tr><tr><td>0.6</td><td>8.55%</td><td>9.58%</td><td>99.78%</td><td>100%</td><td>57.6%</td><td>57.94%</td></tr><tr><td>0.7</td><td>0.52%</td><td>0%</td><td>100%</td><td>100%</td><td>54.01%</td><td>53.48%</td></tr><tr><td>0.8</td><td>0%</td><td>0%</td><td>100%</td><td>100%</td><td>53.77%</td><td>53.48%</td></tr><tr><td>0.9</td><td>0%</td><td>0%</td><td>100%</td><td>100%</td><td>53.77%</td><td>53.48%</td></tr></table>

Table 12  
A comparison of the characteristics of various STSS methods

<table><tr><td>Method</td><td>Optimal threshold</td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F-measure</td></tr><tr><td>1. Mihalcea et al. (MSRPC)</td><td>0.5</td><td>70.3%</td><td>69.6%</td><td>97.7%</td><td>81.3%</td></tr><tr><td>2. Islam and Inkpen (MSRPC)</td><td>0.6</td><td>72.64%</td><td>74.65%</td><td>89.13%</td><td>81.25%</td></tr><tr><td>3. Li et al. (MSRPC)</td><td>0.4</td><td>70.8%</td><td>70.3%</td><td>97.4%</td><td>81.6%</td></tr><tr><td>4. Baseline (SRB)</td><td>0.599</td><td>76.04%</td><td>82.93%</td><td>61.08%</td><td>70.34%</td></tr><tr><td>5. LInSTSS – COALS (SRB)</td><td>0.407</td><td>76.6%</td><td>76.77%</td><td>71.26%</td><td>73.91%</td></tr><tr><td>6. LInSTSS – RI (SRB)</td><td>0.417</td><td>76.6%</td><td>77.85%</td><td>69.46%</td><td>73.42%</td></tr></table>

Bold font is used to emphasize the data with the highest values.

This approach is particularly useful for languages where other, alternative system-building methods are not applicable. We discussed the process of constructing such a system, and we showed its operation, as well as the procedure of gathering and preparing resources for its evaluation. Moreover, we presented the results gained from the evaluation of a system which works with texts written in Serbian.

One of the key traits of the proposed system-building methodology is its modularity, which should allow other researchers to easily adjust to the speci<sup>fi</sup>cities of their own language. We plan to test our approach on another language ourselves, in order to further verify its wide applicability.

Increases in the accuracy of our proposed system can be achieved by using a larger text corpus for semantic space creation. A bigger corpus means a greater number of words within it, which consequently leads to a higher accuracy of the co-occurrence matrix. Another approach to increasing the system's accuracy would be the improvement of preprocessing techniques, achieved chie<sup>fl</sup>y through re<sup>fi</sup>nements of the stemmer module. Evaluation quality could be enhanced by an enlargement of the paraphrase corpus which would strengthen the representability of the evaluation results.

## Acknowledgment

The work presented here was partially supported by the Serbian Ministry of Education and Science (projects III 44006, III 44009, and III 32047). The authors would also like to thank the anonymous reviewers for their helpful and constructive comments.

## References

[1] S. Deerwester, S. Dumais, G. Furnas, T. Landauer, R. Harshman, Indexing by latent semantic analysis, Journal of the American Society for Information Science 41 (6) (1990).

[2] B. Dolan, C. Quirk, C. Brockett, Unsupervised construction of large paraphrase corpora: exploiting massively parallel news sources, Proceedings of the 20th International Conference on Computational Linguistics, 2004.

[3] B. Furlan, V. Sivački, D. Jovanović, B. Nikolić, Comparable evaluation of contemporary corpus-based and knowledge-based semantic similarity measures of short texts Journal of Information Technology and Applications 1 (1) (2011) 65–71.

[4] A. Islam, D. Inkpen, Semantic text similarity using corpus-based word similarity and string similarity, ACM Transactions on Knowledge Discovery from Data 2 (2) (2008) 1–25.

[5] D. Jurgens, K. Stevens, The S-space package: an open source package for word space models, Proceedings of the ACL System Demonstrations, Uppsala, Sweden, 2010.

[6] V. Kešelj, D. Šipka, A suf<sup>fi</sup>x subsumption-based approach to building stemmers and lemmatizers for highly in<sup>fl</sup>ectional languages with sparse resources, INFOTHECA – Journal of Informatics and Librarianship 9 (1–2) (2008)

[7] L. Li, Y. Zhou, B. Yuan, J. Wang, X. Hu, Sentence similarity measurement based on shallow parsing, Fuzzy Systems and Knowledge Discovery 7 (2009) 487–491.

[8] R.T. Lo, B. He, I. Ounis, Automatically building a stopword list for an information retrieval system, 5th Dutch-Belgium Information Retrieval Workshop, Utrecht, Netherlands, 2005.

[9] R. Mihalcea, C. Corley, C. Strapparava, Corpus-based and knowledge-based measures of text semantic similarity, Proceedings of the National Conference on Arti<sup>fi</sup>cial Intelligence 21 (1) (2006) 775–780.

[10] M. Mohler, R. Mihalcea, Text-to-text semantic similarity for automatic short answer grading, European Chapter of the Association for Computational Linguistics, 2009.pp.567-575

[11] J. Oliva, J.I. Serrano, M.D. del Castillo, Á. Iglesias, SyMSS: a syntax-based measure for short-text semantic similarity Data & Knowledge Engineering 70 (4) (2011) 390–405

[12] D.L.T. Rohde, L.M. Gonnerman, D.C. Plaut, An improved method for deriving word meaning from lexical co-occurrence, Cognitive Psychology 7 (2004) 573–605.

[13] M. Sahlgren, An introduction to random indexing, Methods and Applications of Semantic Indexing Workshop at the 7th International Conference on Terminology and Knowledge Engineering, Copenhagen, Denmark, 2005.

[14] R. Wang, G. Neumann, Recognizing textual entailment using sentence similarity based on dependency tree skeletons, ACL-PASCAL Workshop on Textual Entailment and Paraphrasing, 2007, pp. 36–41.

Bojan Furlan received his diploma degree in electrical engineering and computer science from the University of Belgrade, Serbia. Currently, he is a PhD candidate in Software Engineering at the School of Electrical Engineering of the University of Belgrade. He is working as a teaching assistant at the Department of Computer Engineering and Information Theory of the same school. His research interests include semantic similarity of short texts intelligent question routing and knowledge management. His personal web page can be

found at http://home.etf.bg.ac.rs/\~bfurlan

Vuk Batanović received the B.Sc. and M.Sc. in electrical engineering and computer science from the University of Belgrade, Serbia. He is currently a PhD student at the School of Electrical Engineering, Department of Software Engineering, of the University of Belgrade. His research interests focus on arti<sup>fi</sup>cial intelligence, particularly on natural language processing and computational linguistics, and their application in human-computer interaction.

Boško Nikolić received his Dipl Ing, MSc, and PhD degrees in computer engineering and science from the University of Belgrade, Serbia, in 1996, 2001, and 2005, respectively. He is currently an associate professor of computer engineering at the Faculty of Electrical Engineering, University of Belgrade. His research interests include Internet programming, arti<sup>fi</sup>cial intelligence, digital systems simulation, and distance learning.
