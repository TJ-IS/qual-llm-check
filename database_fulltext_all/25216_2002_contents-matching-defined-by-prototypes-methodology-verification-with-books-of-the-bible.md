---
otero_id: 25216
otero_key: "CTSJWCH3"
title: "Contents Matching Defined by Prototypes: Methodology Verification with Books of the Bible"
authors: "Ari Visa; Jarmo Toivonen; Hannu Vanharanta; Barbro Back"
year: "2002"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2002.11045702"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/CTSJWCH3/fulltext/images/ce37a56cd6a772b2e77fb0fc57cf920c17a79857fb2357769fe6183c3748470c.jpg)

# Contents Matching Defined by Prototypes: Methodology Verification with Books of the Bible

Ari Visa, Jarmo Toivonen, Hannu Vanharanta, Barbro Back

To cite this article: Ari Visa, Jarmo Toivonen, Hannu Vanharanta, Barbro Back (2002) Contents Matching Defined by Prototypes: Methodology Verification with Books of the Bible, Journal of Management Information Systems, 18:4, 87-100

To link to this article: http://dx.doi.org/10.1080/07421222.2002.11045702

![](/api/attachments/CTSJWCH3/fulltext/images/6723bd96509aa480357d5113ee3a3f5ac87b11e0aca85fb55cc777d15d58d178.jpg)

Published online: 23 Dec 2014.

![](/api/attachments/CTSJWCH3/fulltext/images/9cbd8c05116aac2fc32e6199ecfe04b61d14e97fda982a924323147eb8d2a7e4.jpg)

Submit your article to this journal

Article views: 7

![](/api/attachments/CTSJWCH3/fulltext/images/c7c271edce0ded1293294c5cb266ca5dc0d5ea16c829fd2fc6fb060f4b33676c.jpg)

View related articles

# Contents Matching Defined by Prototypes: Methodology Verification with Books of the Bible

ARI VISA, JARMO TOIVONEN, HANNU VANHARANTA, AND BARBRO BACK

ARI VISA received his M.S. in computer science and technology from the Linköping University of Technology, Sweden, in 1981. The Licentiate and the Doctor of Technology degrees in information science he received from the Helsinki University of Technology, Finland, in 1988 and 1990, respectively. Since 1996 he has been a professor, first at the Lappeenranta University of Technology and from the beginning of 2000 at the Tampere University of Technology in Finland. His current research interests are in multimedia, data mining, knowledge discovery, and image processing. Professor Visa is the former president and vice president of the Pattern Recognition Society of Finland.

JARMO TOIVONEN received an M.S. (Eng.) in Information Technology from Lappeenranta University of Technology, Finland in 1999. He is currently working as a researcher and pursuing a D.Tech. in the Institute of Signal Processing at Tampere University of Technology, Finland. His research interests include natural language processing, information retrieval, knowledge discovery, and data mining.

HANNU VANHARANTA began his professional career in 1973 as technical assistant at the Turku office of the Finnish Ministry of Trade and Industry. From 1975 to 1992 he worked for Finnish International engineering companies—Jaakko Pöyry, Rintekno, and Ekono—as process engineer, section manager, and leading consultant, respectively. His doctoral thesis was approved in 1995. In 1995–1996 he was professor in Business Economics in the University of Joensuu. In 1996–1998 he served as Pur chasing and Supply Management Professor in the Lappeenranta University of Technology. Since 1998 he has been a professor in Industrial Management and Engineering in Pori School of Technology and Economics, Tampere University of Technology. He is a member of IPSERA and Research Fellow in the Institute for Advanced Management System Research, Åbo Akademi University.

BARBRO BACK is Professor in Accounting Information Systems at Åbo Akadem University in Turku, Finland. Her research interests include accounting information systems, intelligent systems in business, neural networks, and data mining. She has presented her research in the Journal of Management Information Systems, Accounting Management and Information Technology, European Journal of Operations Re search, International Journal of Intelligent Systems in Accounting, Management and Tax, Advances in Accounting, and other journals. She currently serves on the editoria board of The New Review of Applied Expert Systems and Emerging Technologies.

ABSTRACT: It is common that text documents are characterized and classified by key words, index terms, or headings. We have developed a new methodology based on prototype matching. The prototype is an interesting document or a part of an extracted, interesting text. This prototype is matched with the existing document database or with the monitored document flow. The claim is that the new methodology is capable of extracting the contents of the document. To verify this hypothesis, a test with the Bible was designed. Different translations in English, Latin, Greek, and Finnish were selected to test materials. Verification tests that included the search of the ten nearest books to every book of the Bible were performed with a designed prototype version of the software application. The test results are reported in this paper.

KEY WORDS AND PHRASES: Bible, document classification, knowledge discovery, methodology, prototype matching, text mining, verification.

NOWADAYS, A LARGE AMOUNT OF INFORMATION is stored on the Internet, intranets, or databases. Customer comments and communications, trade publications, competitor Web sites, and research reports are just a few examples of available electronic data. The need to find information is one of the basic needs. Besides that, everyone needs a solution for handling the large volume of unstructured information. Needs for document retrieval, document filtering, or text mining are obvious. These methods are usually based on natural language processing. However, the subject is vague. The meaning of terms knowledge, information, data, communication, content, meaning, and document varies depending on the research field. It is possible to study the prob lem from various points of view. At least communications, mathematics, computer science, psychology, linguistics, sociology, and epistemology are possible approaches. The vagueness in the definition of terms is also evident when checking the terms in various dictionaries [16, 17, 18]. However, a framework is needed for a successful research. In linguistics, meaning is studied above all in semantics but meaning is also an important concept for text linguistics. According to Brown and Yule [2], “The discourse analyst treats his data as the record (text) of a dynamic process in which language was used as an instrument of communication in a context by a speaker writer to express meanings and achieve intentions (discourse).” According to Lyons [10], the term communication can be defined in a restricted way, as an intentiona transmission of factual information. Communicative means meaningful for the sender and informative means meaningful for the receiver; receiver’s store of factual knowl edge is augmented in the communication process. Dretske emphasizes that a genuine theory of information would be a theory about the content of our messages, about the information we communicate [6]. Lyons draws a terminological distinction between signal information and semantic information, even though they interact in a complex manner. We are not doing that because there are many interesting discoveries concerning how evolutionary computation techniques can be used to the emergence of syntax and symbols from simple communication signals. These kind of discoveries are presented for example in articles by Cangelosi [3] and Kirby [8]. Their experiments are based on the Savage-Rumbaugh’s and Rumbaugh’s experimental stimulus in ape language research [15]. It seems that far more information is situated in rela tions between symbols than traditionally has been considered.

A common approach to topic detection and tracking is the usage of key words, especially in context of the Dewey decimal classification [4, 5], which is used in United States to classify books. The approach is based on the assumption that key words given by authors or indexers characterize the text well. This may be true, but then one neglects the accuracy. There are also automatic indexing approaches [9]. A more accurate method is to use all the words of a document and the frequency distribution of words, but the comparison of frequency distributions is a complicated task. Some theories say that the rare words in the word frequency histograms distinguish documents [11]. Traditionally, information retrieval has roughly been based on a fixed list of index terms [9, 11], or vector space models [13, 14]. The latter ones miss the information of co-occurrences of words. There are techniques that are capable of considering the co-occurrences of words, as latent semantic analysis [12], but they are computationally heavy.

In this paper, we represent our methodology briefly and concentrate on tests of content-based topic classification, which is highly attractive in text mining. The evolution of the methodology has been previously discussed in several publications [19, 20, 21]. In the next section the applied methodology is described. In the third section the designed experiments are described and the validation results are reported. Finally, the methodology and the results are discussed.

## Methodology

## Theoretical Basis

WE CONSIDER FIRST THE CONTENT-BASED INFORMATION retrieval at the word level. Assume a set of words W and a subset of words, a dictionary WN, so that WN Ì W. This means that a word w usually belongs to the dictionary, but that is not necessary, that is, $\{ w | w \subset W \land w \subset W N \}$ . The new words are projected to the known words in WN. This formulation makes it difficult to use grammars or rules, but allows us to introduce new words. To adapt vocabularies to different application fields the dictionary WN is created by unsupervised learning. Unsupervised learning is usually a kind of a clustering process. The only demand to this approach is that there be a large amount of representative text documents available. The idea with the clustering is to establish an association between a character string (word) and the meaning.

At the sentence and paragraph level the retrieval problem is similar. The successive words $w _ { i } , w _ { i + 1 } , w _ { i + 2 } , \dots , w _ { i + n }$ define a set of sentences S. This set may be very large. In the same manner the successive sentences $s _ { i } , s _ { i + 1 } , s _ { i + 2 } , \ldots , s _ { i + n }$ define a set of paragraphs P. This set P is also very large. We should estimate these sets S and P by subsets SN and PN. Set WN and the relational sets SN and PN are used to characterize the text document at word, sentence, and paragraph levels.

## Methods

The original text is first preprocessed, extra spaces and carriage returns are omitted, and so on. The filtered text is next translated into a suitable form for encoding purposes. The encoding of words is a wide subject and there are several approaches for doing it. The word can be recognized and replaced with a code. This approach is sensitive to new words. The succeeding words can be replaced with a code. This method is language sensitive. Or, each word can be analyzed character-by-characte and based on the characters a key entry to a code table is calculated. This approach is sensitive to capital letters and conjugation if the code table is not arranged in a special way.

The last alternative is selected because it is accurate and suitable for statistical analysis. A word w is transformed into a number in the following manner:

$$
y = \sum_ {i = 0} ^ {L - 1} k ^ {i} * c _ {L - i},
$$

where $L$ is the length of the character string (the word), $c _ { i }$ is the ASCII value of a character within a word w, and k is a constant. Example: if the word is “c a $\mathbf { t } , \vec { \mathbf { \Lambda } }$ then

$$
\mathrm{y} = \mathrm{k} ^ {2} * \text { ASCII } (\mathrm{c}) + \mathrm{k} * \text { ASCII } (\mathrm{a}) + \text { ASCII } (\mathrm{t}).
$$

The encoding algorithm produces a different number for each different word, only the same word can have an equal number. After each word has been converted to a code number, one considers the distribution of the code numbers of the words. One tries to estimate the distribution of these numbers. Many distributions, such as, gamma distribution, are possible. However, it would be advantageous if the selected distribution had only a few parameters and it matched the observed distribution as well as possible. Based on tests with different types of text databases, the Weibull distribution is selected to represent the distribution. The distribution of the code numbers is similar to the Weibull distribution with most test databases. In the training phase the range between the minimum and the maximum values of code numbers is divided to $N _ { \scriptscriptstyle w }$ logarithmically equal bins. The frequency count of words belonging to each bin is calculated. The bins’ counts are normalized with the number of all words. Then the best Weibull distribution corresponding to the data is determined. Weibull distribution is compared with empirical distribution by examining both distributions’ cumulative distributions. Weibull’s Cumulative Distribution Function (CDF) is calculated by:

$$
\mathrm{CDF} = 1 - e ^ {\left(\left(\left(- 2. 6 * \log (y / y _ {\max})\right) ^ {b}\right) * a\right)}.
$$

There are two parameters that can be varied in Weibull’s CDF formula: a and b. A set of Weibull distributions are calculated with all the possible combinations of $\boldsymbol { a } ^ { \prime } \boldsymbol { s }$ and $b \mathbf { \bar { s } }$ using a selected precision. The possible values for the coefficients are restricted between realistic minimum and maximum values. The empirical cumulative distribution and Weibull’s cumulative distribution are compared in the least square sum sense.

In the next phase the best found Weibull distribution is divided into $N _ { \scriptscriptstyle w }$ equal probable bins. Every word belongs now to a bin that can be found using the word number and the best-fitting Weibull distribution. Using this type of quantization the word can now be presented as the bin number, that is, the number of the bin that it belongs to. Due to the selected coding method the resolution will be the best where the words are most typical to text (usually two to five length words). Rare words (usually long words) are not so accurately separated from each other.

Similarly, at the sentence level, every sentence has to be converted to a number. Every word in a sentence is replaced with a bin number in the same way we did with words earlier. Example:

$$
\begin{array}{c c c c c} \textbf {I} & \textbf {h a v e} & \textbf {a} & \textbf {c a t} & . \\ b n _ {0} & b n _ {1} & b n _ {2} & b n _ {3} & b n _ {4} \end{array}
$$

where $b n _ { i } = \mathsf { b i n }$ number of the word i.

The whole encoded sentence is then considered as a sampled signal. Since the sentences of the text contain different numbers of words, the sentence vectors’ lengths differ. To get past this fact, we use the Discrete Fourier Transform (DFT) to transform the sentence vectors. We do not consider all the coefficients. The input for the DFT is $( b n _ { 0 } , b n _ { 1 } , b n _ { 2 } , \dots , b n _ { n } )$ . DFT’s outputs are coefficients $B _ { 0 }$ to $B _ { n }$ . The second coefficien $B _ { 1 }$ is selected to be the number that describes the sentence. The reason why the $B _ { 1 }$ component is selected is that it characterizes roughly the envelope of the signal and it is not affected too much by the lengths of the sentences.

After every sentence has been converted to numbers, a cumulative distribution is created from the sentence data set in the same way as on the word level. Now the range between the minimum and the maximum value of the sentence numbers are divided to $N _ { s }$ equal size bins. The frequency count of sentences belonging to each bin is calculated and the bins’ counts are normalized with the number of all sentences. The best Weibull distribution corresponding to the sentence data is found using the cumulative distribution of both distributions. Now the best distribution can be used in the quantization of sentences. An example of a sentence distribution and a corresponding best Weibull distribution are illustrated in Figure 1, subplots 1 and 3.

On the paragraph level the method is similar. The paragraphs of the document are first converted to vectors using the code numbers of the sentences. The vectors are Fourier-transformed and the coefficient $B _ { 1 }$ is chosen to represent the paragraph. After the best Weibull distribution corresponding to the paragraph data is found the quantized distribution can be used in encoding of paragraphs.

When examining the single-text documents one creates histograms of the documents word, sentence, and paragraph code numbers. On the word level the filtered text from a single document is encoded word-by-word. Each word number is quantized using word quantization created with all the words of the database. The quantization value is determined, an accumulator corresponding to the value is increased, and thus a word histogram $A _ { \scriptscriptstyle w }$ is created. The histogram $A _ { \scriptscriptstyle w }$ consisting of $N _ { \scriptscriptstyle w }$ bins is finally normalized by the total word count of the document. On the sentence and the paragraph levels the histogram creation process is similar. The single document is encoded to sentence and paragraph code numbers and the hits according to the corresponding place in the histograms $A _ { s }$ and $A _ { p } .$ . An example of a sentence histogram is illustrated in Figure 1, subplot 2. With the histograms derived from all the documents in the database we can compare and analyze the single documents’ text on the word, sentence, and paragraph levels against the other texts in the database. The histogram creation and comparison processes are illustrated in Figure 2.

![](/api/attachments/CTSJWCH3/fulltext/images/dea67a42f49ebedd9a80394cae69c2e18cf730715afeffdc077774ded07f6233.jpg)

![](/api/attachments/CTSJWCH3/fulltext/images/617a61b6156f24daf6840e4cdacf653eb4b1a2367ed530cdc924a38c3e323bf6.jpg)

3. Corresponding Weibull Distribution $( \mathsf { a } = 2 . 3 9 , \mathsf { b } = 1 . 7 5 )$  
![](/api/attachments/CTSJWCH3/fulltext/images/f676a49f3238df9959201dcd7b58d1002820fbdee8765e9a77104a1a88293ed0.jpg)  
Figure 1. Example of a Sentence Quantization Process

Note that it is not necessary to know anything from the actual text document to do this. It is sufficient to use one document as a prototype. The methodology gives the user all the similar documents and distance values as goodness measures.

## Experiments

OUR ASSUMPTION IS THAT THE CONTENTS OF TEXT depends on given factors:

$$
\text { text   contents } = \text { message } + \text { style } + \text { language } + \text { methodology }.
$$

![](/api/attachments/CTSJWCH3/fulltext/images/39193491ba4d0094add649ed875d00ef090c54664ebcb6965572c5a15b71fada.jpg)  
Figure 2. The Process of Comparing and Analyzing Documents Based on the Extracted Histograms on Different Levels

To find out which of the mentioned factors are the most powerful, an experiment was designed. In the tests we kept the methodology the same all the time and varied the style, language, and message. It was important to find a text that is carefully translated into another language. In translation, it is important to keep the message the same even though the form depends on the language. The Bible was selected to meet the demands. The translations used were King James Bible in English, Jerome’s translation (Vulgate) from the years 382 to 405 in Latin, and the Westcott-Hort translation in Greek. Two different era translations of the Bible in Finnish were also used. The older Finnish Bible version was from the years 1933 (the Old Testament) and 1938 (the New Testament), and the more recent from 1992.

Precision and recall were used as measures of effectiveness [11]. The recall window of closest matches was selected to 10. The size of the histograms for the word level was 2,080, for the sentence level 25, and for the paragraph level 10. The histogram sizes were found by experiments. The word, sentence, and paragraph level histograms were created based on the whole text of the Bibles. No stemming or reduction into the base form has been used. Euclidean distance was used in the comparisons of the histograms.

The first experiment considers the differences between the languages and the style in more detail. Each pair of two different translations is selected from the group of three translations. It is known that the Old and the New Testament books differ. Every book was taken one-by-one as a prototype, and ten closest matches were examined. The order within the window is not considered, only the co-occurrences. First, the influence of style was considered. The Finnish translations were selected as test texts. They both were based on the same source. The results are about the same between the Greek–Finnish 1933/1938 translations and the Greek–Finnish 1992 translations in Figures 3 and 4. The results between the Finnish translations are better than between the Greek–Finnish translations, as expected, but the results are not perfect, see Figure 5. As a control test, the same experiment was repeated between the English (King James) and the Finnish (1933/1938) translation and between the Latin (Vulgate) and the Finnish (1933/1938), see Figures 6 and 7. It seems that the style plays in, but its role is less than that of the language.

![](/api/attachments/CTSJWCH3/fulltext/images/d7d60c03a98b3fc3d4e493cf34e491fafa43f459e968ddab457d70b0d9ffdb1d.jpg)

<table><tr><td></td><td>Old Testament Average</td><td>New Testament Average</td><td>Total Average</td></tr><tr><td>Word level</td><td>5.49</td><td>5.87</td><td>5.61</td></tr><tr><td>Sentence level</td><td>4.00</td><td>3.85</td><td>3.94</td></tr><tr><td>Paragraph level</td><td>2.79</td><td>2.26</td><td>2.58</td></tr></table>

Figure 3. Number of the Same Books Among Ten Closest Matches in the Greek and th Finnish 1933/1938 Translations  
![](/api/attachments/CTSJWCH3/fulltext/images/b5190ec3db5e7d56b62b51a67f75553a3cef6430514a2b3adaa1c0424d9dc570.jpg)

<table><tr><td></td><td>Old Testament Average</td><td>New Testament Average</td><td>Total Average</td></tr><tr><td>Word level</td><td>4.87</td><td>5.33</td><td>5.06</td></tr><tr><td>Sentence level</td><td>4.33</td><td>3.81</td><td>4.12</td></tr><tr><td>Paragraph level</td><td>2.82</td><td>1.81</td><td>2.41</td></tr></table>

Figure 4. Number of the Same Books Among Ten Closest Matches in the Greek and th Finnish 1992 Translations

In the second experiment, the effect of the message is studied. We know that in the Bible, the books can be divided into groups based on similarity of their contents. Two of this kind of distinct groups are the books 18 through 22 (Job, Psalms, Proverbs, Ecclesiastes, Song of Solomon) and the books 40 through 44 (the gospels by Matthew, Mark, Luke, and John, and The Acts). By examining these groups, one tries to find out how well our methodology is capable of clustering these texts, keeping in mind the style and language effects. In this experiment the recall window size is five. The reason why the recall window is now five is that there are no more than five books in both test sets. The number of expected books is counted within the recall window. The results are presented in Tables 1 through 4. Note that since the prototype book is not compared with itself, the possible maximum value for the number of books of the same group in the recall window is four. Tables 2 and 3 show that the style plays a certain role in these experiments. Tables 1, 2, and 4 also show that the language has an effect on the results. The experiments indicate clearly that the content of the documents is the most important separative factor. This claim is easily motivated by probability calculations and comparison with the observed counts.

![](/api/attachments/CTSJWCH3/fulltext/images/54a078e0231992f481da19d5b05847e947d134ab2fd21934220f42d1a70a9263.jpg)

<table><tr><td></td><td>Old Testament Average</td><td>New Testament Average</td><td>Total Average</td></tr><tr><td>Word level</td><td>7.38</td><td>7.07</td><td>7.26</td></tr><tr><td>Sentence level</td><td>4.90</td><td>3.93</td><td>4.50</td></tr><tr><td>Paragraph level</td><td>2.67</td><td>2.37</td><td>2.55</td></tr></table>

Figure 5. Number of the Same Books Among Ten Closest Matches in the Finnish 1933/1938 and the Finnish 1992 Translations

![](/api/attachments/CTSJWCH3/fulltext/images/247e6910bfe56e216c48a4f24aa2e43d16f8010bebc4cfe0c00ac42e84312a4c.jpg)

<table><tr><td></td><td>Old Testament Average</td><td>New Testament Average</td><td>Total Average</td></tr><tr><td>Word level</td><td>6.56</td><td>6.89</td><td>6.70</td></tr><tr><td>Sentence level</td><td>5.05</td><td>3.89</td><td>4.58</td></tr><tr><td>Paragraph level</td><td>3.33</td><td>1.96</td><td>2.77</td></tr></table>

Figure 6. Number of the Same Books Among Ten Closest Matches in the English and the Finnish 1933/1938 Translations

## Discussion

THE CONTENT-BASED INFORMATION RETRIEVAL is a complicated area. Commonly, the problems have been addressed by information description languages. Harter [7] ar ranged some major classes of information description languages along a continuum, by the increased deviation from natural language, see Figure 8. The left half of the continuum presents the natural language approaches and the right half of the continuum presents the controlled vocabulary approaches. The natural language approaches include full texts of documents, abstracts, titles, and identifiers extracted from the original text by indexers. The controlled vocabulary approaches include descriptors, subject headings, and hierarchical classification. The difference between identifiers and descriptors is that, whereas identifiers are derived from the original text, descriptors are listed in thesauri, which helps to deal with synonyms, homographs, and such. The difference between descriptors and subject headings is that, whereas thesauri are usually derived from existing document collections, subject heading lists are often a prior attempt to represent the whole structure of the universe instead of representing the vocabulary of specific document collection.

![](/api/attachments/CTSJWCH3/fulltext/images/881884a9580cc26e1b1a6cb639379b9a0ad94ee59c18ee7e3c36278aa21fec80.jpg)  
Figure 7. Number of the Same Books Among Ten Closest Matches in the Finnish 1933/1938 and the Latin Translations

Our approach is clearly in the left half of the continuum. We try to keep as much information as possible from the original text document. We consider the text at word, sentence, and paragraph levels. New words, sentence, or paragraph structures do not disturb our approach. The main idea is to define the target information with prototypes, text documents that are considered interesting by the user. After this decision, the problem is transformed into the subproblem to find similar documents. One of our basic assumptions is that within a specific field, for instance in law or business, the ambiguities of words will not disturb significantly.

From linguistics we know that a text document can be described with a model. Our experiments are based on the model that the contents of a document is described by the message, the language, and the style. It was important to find a document that was carefully translated into several languages. That was the reason why the Bible wa selected. We know that the translations have been done very carefully, at least at the information level. Besides the language and style aspects, there should also be an agreement concerning the grouping of documents. Because of the selected model, it is now possible to consider the problem in detail. Based on Figures 3 through 7, it seems that the effect of style is less than the effect of language. Based on Tables 1 and 2, it also seems that the effect of language is less than the effect of the contents.

<table><tr><td colspan="8">Table 1. Number of the Books of the Same Class Among Five Closest Matches in the Greek Translation</td></tr><tr><td>Book</td><td>Word</td><td>Sentence</td><td>Paragraph</td><td>Book</td><td>Word</td><td>Sentence</td><td>Paragraph</td></tr><tr><td>18</td><td>1/5</td><td>2/5</td><td>2/5</td><td>40</td><td>3/5</td><td>3/5</td><td>0/5</td></tr><tr><td>19</td><td>0/5</td><td>2/5</td><td>2/5</td><td>41</td><td>2/5</td><td>3/5</td><td>0/5</td></tr><tr><td>20</td><td>1/5</td><td>1/5</td><td>0/5</td><td>42</td><td>3/5</td><td>3/5</td><td>1/5</td></tr><tr><td>21</td><td>0/5</td><td>1/5</td><td>1/5</td><td>43</td><td>3/5</td><td>3/5</td><td>2/5</td></tr><tr><td>22</td><td>1/5</td><td>1/5</td><td>0/5</td><td>44</td><td>2/5</td><td>0/5</td><td>0/5</td></tr><tr><td>Sum (max 20/25)</td><td>3/25</td><td>7/25</td><td>5/25</td><td></td><td>13/25</td><td>12/25</td><td>3/25</td></tr></table>

<sub>ftheBooksoftheSameClassAmongFiveClosest</sub>M<sup>atchesintheFinnish</sup>

<table><tr><td>Book</td><td>Word</td><td>Sentence</td><td>Paragraph</td><td>Book</td><td>Word</td><td>Sentence</td><td>Paragraph</td></tr><tr><td>18</td><td>1/5</td><td>3/5</td><td>1/5</td><td>40</td><td>4/5</td><td>1/5</td><td>1/5</td></tr><tr><td>19</td><td>1/5</td><td>3/5</td><td>1/5</td><td>41</td><td>2/5</td><td>2/5</td><td>2/5</td></tr><tr><td>20</td><td>2/5</td><td>3/5</td><td>0/5</td><td>42</td><td>4/5</td><td>1/5</td><td>1/5</td></tr><tr><td>21</td><td>1/5</td><td>2/5</td><td>2/5</td><td>43</td><td>3/5</td><td>2/5</td><td>1/5</td></tr><tr><td>22</td><td>1/5</td><td>1/5</td><td>0/5</td><td>44</td><td>1/5</td><td>2/5</td><td>1/5</td></tr><tr><td>Sum (max 20/25)</td><td>6/25</td><td>4/25</td><td>4/25</td><td></td><td>14/25</td><td>8/25</td><td>6/25</td></tr></table>

<sub>ftheBooksoftheSameClassAmongFiveClosest</sub>M<sup>atchesintheEn</sup>

<table><tr><td>Book</td><td>Word</td><td>Sentence</td><td>Paragraph</td><td>Book</td><td>Word</td><td>Sentence</td><td>Paragraph</td></tr><tr><td>18</td><td>2/5</td><td>3/5</td><td>1/5</td><td>40</td><td>4/5</td><td>3/5</td><td>2/5</td></tr><tr><td>19</td><td>1/5</td><td>2/5</td><td>2/5</td><td>41</td><td>3/5</td><td>3/5</td><td>0/5</td></tr><tr><td>20</td><td>3/5</td><td>3/5</td><td>3/5</td><td>42</td><td>4/5</td><td>3/5</td><td>2/5</td></tr><tr><td>21</td><td>2/5</td><td>1/5</td><td>2/5</td><td>43</td><td>4/5</td><td>3/5</td><td>0/5</td></tr><tr><td>22</td><td>2/5</td><td>0/5</td><td>0/5</td><td>44</td><td>3/5</td><td>1/5</td><td>2/5</td></tr><tr><td>Sum (max 20/25)</td><td>10/25</td><td>9/25</td><td>8/25</td><td></td><td>18/25</td><td>13/25</td><td>6/25</td></tr></table>

![](/api/attachments/CTSJWCH3/fulltext/images/946a38fb082a953310055014ee6b1e49a60e134a72bc0ded5b0747f5ff92ab9e.jpg)  
Figure 8. Information Description Languages, Arranged by Degree of Departure from Natural Language, According to Harter [7]

However, one should be careful with generalizations. There are evidences that the situation is different with short text documents [21]. It seems that the content-based matching is possible, at least at word and sentence levels. At the paragraph level the structure of the text plays a role. There is also evidence that the methodology used at word and sentence levels is in some cases capable of author identification [21]. Moreover, we have tried out an earlier version of the methodology for qualitative analyses of text information from organizations [1]. Our work continues to find out the scope of validity of the represented methodology.

It seems that the developed methodology is very promising. The methodology is capable of content-based information retrieval and filtering. The methodology makes it possible to search text documents defined by a prototype. It is simple, fast, and highly suitable to existing computers. It is also easy to adapt the presented methodol ogy to new application fields by training.

Acknowledgments: This research is supported by TEKES, the National Technology Agency of Finland (grant number 40943/99). The support is gratefully acknowledged.

## REFERENCES

1. Back, B.; Toivonen, J.; Vanharanta, H.; and Visa, A. Comparing numerical data and tex information from annual reports using self-organizing maps. International Journal of Accounting Information Systems, 2, 4 (2001), 249–269.

2. Brown, G., and Yule, G. Discourse Analysis. Cambridge: Cambridge University Press, 1983.

3. Cangelosi, A. Evolution of communication and language using signals, symbols, and words. IEEE Transactions in Evolutionary Computation, 5, 2 (2001), 93–101.

4. Dewey, M. A Classification and Subject Index for Cataloguing and Arranging the Books and Pamphlets of a Library. Amherst, MA: Case, Lockwood & Brainard, 1876.

5. Dewey, M. Catalogs and cataloguing: A decimal classification and subject index. In U.S. Bureau of Education Special Report on Public Libraries Part I. Washington, DC: U.S. Government Printing Office, 1876, pp. 623–648.

6. Dretske, F.I. Knowledge and the Flow of Information. Oxford: Basil Blackwell, 1981.

7. Harter, S.P. Online Information Retrieval: Concepts, Principles, and Techniques. Or lando, FL: Academic Press, 1986.

8. Kirby, S. Spontaneous evolution of linguistic structure: An iterated learning model of the emergence of regularity and irregularity. IEEE Transactions on Evolutionary Computation, 5 2 (2001), 102–110.

9. Lahtinen, T. Automatic Indexing: An Approach Using an Index Term Corpus and Combining Linguistic and Statistical Methods. Ph.D. dissertation, Department of General Linguistics, University of Helsinki, Finland, 2000.

10. Lyons, J. Semantics I. Cambridge: Cambridge University Press, 1977.

11. Manning, C.D., and Schütze, H. Foundations of Statistical Natural Language Processing. Cambridge, MA: MIT Press, 1999.

12. Oard, D.W., and Marchionini, G. A conceptual framework for text filtering. Technical report CS-TR3643, University of Maryland, College Park, May 1996.

13. Salton, G. Automatic Text Processing. Boston: Addison Wesley, 1989

14. Salton, G.; Wong, A.; and Yang, C. A vector space model for automatic indexing. Com munications of the ACM, 18, 11 (1975), 613–620.

15. Savage-Rumbaugh, S., and Rumbaugh, D.M. Symbolization, language, and chimpanzees: A theoretical reevaluation on initial language acquisition processes in four young pan troglodytes. Brain and Language, 6, 3 (1978), 265–300.

16. Sinclair, J. (editor in chief). Collins Cobuild English Language Dictionary. London: William Collins, 1987.

17. Soukhanov, A.H., and Ellis, K. (eds.). Webster’s II New Riverside University Dictionary. Boston: Riverside Publishing, 1984.

18. Sykes, J.B. (ed.). The Concise Oxford Dictionary, 6th ed. Oxford: Clarendon Press, 1976.

19. Visa, A.; Toivonen, J.; Back, B.; and Vanharanta, H. Improvements on a knowledge discovery methodology for text documents. In Proceedings of SSGRR 2000—International Conference on Advances in Infrastructure for Electronic Business, Science, and Education on the Internet. L’Aquila, Italy: Scuola Superiore Guglielmo Reiss Romoli, 2000.

20. Visa, A.; Toivonen, J.; Vanharanta, H.; and Back, B. Prototype matching—Finding meaning in the books of the Bible. In R.H. Sprague Jr. (ed.), Proceedings of the Thirty-Fourth Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2001.

21. Visa, A.; Toivonen, J.; Autio, S.; Mäkinen, J.; Vanharanta, H.; and Back, B. Data mining of text as a tool in authorship attribution. In B.V. Dasarathy (ed.), Proceedings of AeroSense 2001, SPIE Fifteenth Annual International Symposium on Aerospace/Defense Sensing, Simulation and Controls. Data Mining and Knowledge Discovery: Theory, Tools, and Technolog III, vol. 4384. Bellingham, WA: SPIE, The International Society for Optical Engineering, 2001, pp. 149–156.
