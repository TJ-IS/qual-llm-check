---
otero_id: 834
otero_key: "6NVF63D5"
title: "Research note: Examining gender emotional differences in Web forum communication"
authors: "Yulei Zhang; Yan Dang; Hsinchun Chen"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.04.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Research note: Examining gender emotional differences in Web forum communication

Yulei Zhang <sup>a,</sup>⁎, Yan Dang <sup>a</sup>, Hsinchun Chen <sup>b</sup>

<sup>a</sup> Computer Information Systems, The W. A. Franke College of Business, Northern Arizona University, Flagstaff, AZ, 86011, United States <sup>b</sup> Department of Management Information Systems, Eller College of Management, University of Arizona, Tucson, AZ, 85721, United States

## a r t i c l e i n f o

Article history: Received 23 May 2012 Received in revised form 13 April 2013 Accepted 16 April 2013 Available online 23 April 2013

Keywords: Gender emotional differences Sentiment analysis Web forums

## a b s t r a c t

Web 2.0 has enabled and fostered Internet users to share and discuss their opinions and ideas online. Thus, a large amount of opinion-rich content has been generated. With more and more women starting to participate in online communications, questions regarding gender emotional differences in Web 2.0 communication platform have been raised. However, few studies have systematically examined such differences. Motivated to address this gap, we have developed an advanced and generic framework to automatically analyze gender emotional differences in social media. Algorithms are developed and embedded in the framework to conduct analyses in different granularity levels, including sentence level, phrase level, and word level. To demonstrate the proposed research framework, an empirical experiment is conducted on a large Web forum. The analysis results indicate that women are more likely to express their opinions subjectively than men (based on sentence-level analysis), and they are more likely to express both positive and negative emotions (based on phrase-level and word-level analyses).

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The two-way communication enabled by Web 2.0 has revolutionized the way that people utilize the Internet [42]. Internet users no longer just passively acquire information from the Web but can also actively participate and contribute their own content to the Web. For example, they can post their opinions towards certain products, political or social issues on Web forums and blogs, and share information with others on social networking sites. Thus, a considerable amount of opinion- and emotion-rich content has been generated over the Internet with an exponentially increasing rate. Analyzing and better understanding such content could have practical importance for online service and product providers to develop Web 2.0 infrastructures and users to make their online purchase decisions [29,35], as well as taking actions towards social and political events and issues [6].

The Internet was generally known as male-dominated in terms of technology [56] and Internet usage [25] over years. For a long time, men had been associated with technology and women were treated as somewhat passive users [56]. In addition, there were more men than women to use the Internet regularly [25]. However, nowadays it has become a popular platform for women to share opinions about their personal, social and political issues as well [25]. With such a trend, researchers start to gain interests in investigating gender differences in online communication media, referring to the difference between the two genders in their usage of the Internet [17,19,26]. For example, previous research has found that women tend to treat the Internet as a communication tool and men tend to use it as a way of information seeking [30].

In terms of emotional difference between the two genders, previous literature has found that women tend to express more intensely positive emotions such as happiness, love, and life satisfaction than men [18,23,39,65]. Women also have reported higher levels of negative emotions in most cases [22,23,40]. However, many existing studies on gender emotional differences focus on face-to-face settings. Few have speci<sup>fi</sup>cally examined such differences in online communication media. Early research assumed that text-based online communications could not transmit socio-emotional content that is typically expressed in face-to-face communications [52]. However, later literature conducted in-depth analyses on the social information process and has argued that text-based online communications could support socio-emotional and relational communications when users feel they are af<sup>fi</sup>liated to the online communities [58]. Face-to-face communicative cues can be adapted to communications occurring via online media [24,31].

Sentiment analysis techniques can be leveraged to examine online opinions and emotions, and have been drawing great attention among researchers [33]. The goal of sentiment analysis is to identify and examine whether a text is objective or subjective, or whether a subjective text contains positive or negative sentiments [1]. There are two major approaches to conduct sentiment analysis, the machine learning approach and the semantic orientation approach [1]. In terms of granularity levels of sentiment analysis, most previous studies focused on document level and some were based on <sup>fi</sup>ner granularities such as sentence level [66,67].

To speci<sup>fi</sup>cally and empirically examine gender emotional differences in online communications, we develop a systematic and generic framework that aims to investigate and compare the intensity of emotions expressed by the two genders. Three algorithms are developed by leveraging both machine learning and semantic orientation approaches and are embedded in the framework. These algorithms focus on examining gender emotional differences on three levels of expression: sentence-level, phrase-level and word-level. Based on the proposed framework and emotion detection algorithms, an experiment is conducted on a Web forum that is popular in discussing political issues and is suggested by an expert researcher in gender studies.

The remainder of this paper is organized as follows. Section 2 reviews online gender differences, gender emotional studies, and sentiment analysis techniques that can be used to analyze emotional differences. We then summarize our literature review and highlight our motivation for this study in Section 3. In Section 4, we detail our research design in terms of data acquisition and emotion detection. We then describe our experimental study and results in Section 5, followed by a discussion of the study's contributions and some future research suggestions in Section 6.

## 2. Gender differences and sentiment analysis techniques

## 2.1. Online gender differences

Understanding gender and its role has been an important task in information systems literature. A vast amount of studies have investigated gender impact in areas such as feedback utilization [12], IT adoption [57], online trust [38], and blogger switching behavior [68].

Online gender differences refer to the differences between women and men in their Internet use [3]. At the relatively early stage of Internet use, the main online gender difference was that there were more men than women to use the Internet. For example, as in 1999, 53% of U.S. and Canadian Internet users were men and 47% were women [7]. However, with the recent advance and development in Internet technologies, such online gender difference is believed to be less signi<sup>fi</sup>- cant [45]. Instead, how the two genders utilize the Internet in different ways have become the new focus of online gender differences [26].

Understanding online gender differences and why they occur could be important for Internet service providers, system developers, information analysts, and end users. Many domains, such as security and marketing, could bene<sup>fi</sup>t from such an understanding. The ability of security researchers and analysts to track individual contributors, analyze gender-speci<sup>fi</sup>c trends and views, monitor certain opinion groups, and identify potential threats could be very useful. For the marketing domain, a better understanding of the different interests in various products between the two genders can help the sellers adopt and develop services and systems tailored for the two groups of people, and thereby attract more customers. For example, Van Slyke et al. [56] have examined online gender differences in terms of online shopping and found that women view online shopping less favorable than men. They propose several suggestions to improve women's perceptions of online shopping, such as increasing a sense of social community, providing accurate descriptions and quality images, and reducing the risk involved in purchasing online.

Depending on their own interests and material and emotional needs, women and men could have different Internet use patterns and ways to express opinions and ideas online [19,26,30,41]. For example, previous research has found that women are more likely to use the Internet as a communication tool while men tend to use it as a way of information seeking [30]. In terms of online communication style, women tend be less authoritative compared with men [41]. Women and men also tend to have different popular topics in online communications — women are observed to be more likely to talk about their private lives such as family and close friends, while men are more likely to talk about public lives such as government and commercial establishments [19].

As a major type of Web 2.0 social media, Web forums enable the two-way communications between Internet users and the online community. In general, Web forums have several characteristics that are not included in other social media. For example, compared with Web blogs, Web forums tend to have balanced numbers of participants and their discussion messages. In general, Web forum participants are free to initiate their own discussions on topics of their own choosing. However, topics on Web blogs are generally set by blog owners who lead the discussions and control the blogs.

Previous research on gender differences in Web forums has conducted keyword analysis to identify different topics that women and men are interested in [49]. For example, Seale et al. [49] analyzed Web forums focusing on discussions of cancers and have found that women tend to join the discussions related to emotional support and the impact of illness to others while men tend to discuss more about treatment information, medical personnel and procedures. Guiller and Durndell [24] studied an online course discussion board and have found that women tend to explicitly agree with and support others with more personal expressions while men tend to use authoritative language in response to others.

## 2.2. Gender emotional studies

Focusing on examining face-to-face communications, existing literature on gender emotional studies generally have concluded that women are more emotional than men and that they are more likely to express positive emotions than men [4,39,65]. Although some inconsistencies exist for negative emotions, women are generally reported with higher level of negative emotions such as sadness and fear [16,23].

Research has found that women tend to express emotions more than men [4,53,65]; they experience joy and sadness more intensely than men [18]; and they express more warmth and concern for others [23,39,51]. In addition, women are also reported to have higher levels of negative emotions such as depression, fear and sadness [22,23,40]. A cross-cultural analysis conducted by Lucas and Gohm [36] shows that women express both negative emotions (especially fear and sadness) and positive emotions more frequently than men in their daily lives.

Early studies on online communication media suggested that the capacity to transmit social and interpersonal information (such as emotions) and self-awareness in text-based online communication media would be greatly reduced [24,50,52] compared with face-to-face communications. Later research has examined the social information process [58] and has suggested that text-based online communications could support socio-emotional and relational communications when users feel they are af<sup>fi</sup>liated to the online communities [24]. It is believed that although there are limitations in the textual display of online communication media, users can adjust the communicative cues in order to communicate in those media [24]. Therefore, we could expect the existence of gender emotional differences in Web 2.0 social media such as Web forums. However, little effort has been seen in previous literature to speci<sup>fi</sup>cally examine it.

Most existing gender emotional studies have focused on the face-to-face communication medium; few are based on Web 2.0 social media such as Web forums. It would be of interest and importance to examine whether gender emotional differences exist in Web 2.0 social media and whether they are consistent with or different from the general conclusions drawn on the face-to-face communication medium.

## 2.3. Enabling techniques for sentiment analysis

Sentiment analysis is the automatic detection of opinions from free text. The computer-based detection and analysis of emotion from textual documents has been a growing interest among researchers in recent years [33,43]. Previous sentiment analysis studies include determining whether a text is objective or subjective [60,61], or whether a subjective text contains positive or negative sentiments[44,54]. Most sentiment analysis research focuses on classifying an opinioned piece of text into one of the two opposite sentiment polarities [43].

In terms of granularity levels of sentiment analysis, most studies focus on document level and some are based on sentence level [66,67]. Document-level sentiment analysis examines the overall polarity of a whole document. The limitation is that it may contain sentences in different sentiment polarities. Thus, to gain an in-depth understanding of sentiments expressed in a long document, analysis on a <sup>fi</sup>ner granularity level is needed. To do that, one popular way is to conduct sentence-level sentiment analysis that aims to evaluate the sentiment of each sentence in a document individually. In addition, some other studies try to investigate sentiments in an even <sup>fi</sup>ner granularity level by utilizing phrase patterns based on POS and n-gram analyses [15]. For example, Fei et al. [15] have noted that phrase patterns such as “n + aj” (noun followed by positive adjective) typically represent positive sentiment while $\mathrm { \ " n } + \mathrm { d } \mathrm { \ " n }$ (noun followed by negative adjective) often expresses negative sentiment. In those cases, sentiments are examined in phrase or even word levels.

Two approaches in sentiment analysis have been widely used: the machine learning approach and the semantic orientation approach (see [34,43,69] for more comprehensive reviews). The machine learning approach treats sentiment analysis as a topic-based text classi<sup>fi</sup>cation problem. Typically, a classi<sup>fi</sup>er is built on the training data, and is then evaluated on the testing data to <sup>fi</sup>ne tune its performance. Any text classi<sup>fi</sup>cation algorithm can be employed, e.g., Naïve Bayes [21,44], Support Vector Machines (SVM) [9,44], Maximum Entropy [5,44] etc. For example, Pang et al. [44] compared the performances of Naïve Bayes, SVM, and Maximum Entropy using movie reviews and found that Naïve Bayes and SVM performed well in determining if a piece of a review was negative or positive.

Features are important when using the machine learning approach [1]. A piece of text is usually converted into a feature vector that can represent the most salient and important information expressed in the original text. Different types of features have been used in sentiment classi<sup>fi</sup>cation studies, such as bag-of-words, n-grams [1,20,44], Part-of-Speech (POS) tags [1,20,44], and word position [32,44]. POS is commonly used in sentiment analysis because it can help with word sense disambiguation [62]. Adjectives have been widely accepted as good POS features [8,43]. Other words, such as nouns, verbs, and adverbs have also been used [2,8,61]. The position of a word in a text may in<sup>fl</sup>uence the overall sentiment or subjectivity of that text [43]. Thus, position information is sometimes considered as a type of features for sentiment analysis as well.

In contrast to the machine learning approach, the semantic orientation approach is domain independent with better generalizability [34,55,69]. This approach performs classi<sup>fi</sup>cation based on positive and negative sentiment words and phrases contained in each evaluation text, and no prior training is required [34]. This approach often relies on external knowledge resources beyond raw data and thus is knowledge-rich [69]. There are usually three steps involved: (1) extracting words or phrases with semantic orientations; (2) deciding the polarities of the extracted words or phrases; and (3) calculating the polarity of the text by aggregating the polarities of words or phrases in the text [69].

Most semantic orientation-based sentiment analysis research has followed the procedure of <sup>fi</sup>rst creating a sentiment lexicon and then calculating the positivity (or subjectivity) scores of a given textual document by mapping the positive and negative (or subjective)

words and phrases with the corresponding entries in the lexicon [43]. For example, Hu & Liu [28] used a bootstrapping technique to generate a set of opinion words with semantic orientations from a group of manually created seed adjectives by searching for their synonyms and antonyms in WordNet. The orientation of a sentence was determined by the dominant orientation of the opinion words in the sentence. That is, if positive (negative) opinion prevailed, the sentence was regarded as a positive (negative) one. Building upon WordNet, SentiWordNet [13] is a lexical resource for sentiment analysis which has more sentiment related features than WordNet. It assigns to each synset of WordNet three sentiment scores regarding positivity, negativity, and objectivity respectively. SentiWordNet has been used as the lexicon in recent sentiment classi<sup>fi</sup>cation studies [8,10,11,14,35].

Overall, the machine learning approach tends to be more accurate than the semantic orientation approach since a machine learning model is always tuned to the training data set; however, this also becomes a disadvantage of the machine learning approach as it is domain dependent with less generalizability [34,55,69].

One well-known and tested sentiment analysis tool is OpinionFinder hat aims to identify subjective sentences and classify embedded phrases into positive or negative sentiment [63]. OpinionFinder was developed by Wiebe's group based on a series of publications [46,59,63], and has been reported with good performance when testing against standard datasets. The sentiment classi<sup>fi</sup>ers in OpinionFinder are based on Naïve Bayes algorithm with the use of a variety of lexical and contextual features [46,59]. A set of rule-based features are also incorporated to increase the generalizability of classi<sup>fi</sup>ers [63]. OpinionFinder has been successfully used in many recent sentiment analysis studies such as analyzing sentiments in online news articles for better stock market prediction [48] and opinion mining for online word of mouth analysis in Yahoo Movies message board [35].

## 3. Research motivation and research hypotheses

Web 2.0 has provided a two-way communication channel between the Internet user and the online community. Users can not only acquire information from the Internet but also post and discuss their own opinions and ideas towards various topics. Thus, a considerable amount of opinion-rich, user-generated content has been available on the Internet. Although it is male-dominated in history, the Internet has been increasingly attracting female users to participate in online discussions to express their opinions and feelings [25]. Thus, investigating and understanding the opinion and sentiment differences between women and men (i.e., gender emotional difference) in social media (such as Web forums) has become of great interest and importance for researchers, online service or product providers, and Internet users.

As discussed in Section 2.2, in traditional face-to-face communications, it is generally concluded that women tend to be more emotional than men [4,53,65]. In addition, many studies have indicated that women are more likely to express both positive and negative emotions than men [22,23,39,40,51]. Different from the face-to-face communication medium that is rich in visual and verbal cues, most social media such as Web forums are text-based. Although online text-based communications are less rich than face-to-face communications, previous research on social information process has suggested that users could adjust the socio-emotional communicative cues and adapt them to the online media [24,31,58]. Because of that, it could be expected that gender emotional differences do exist in social media communications and such differences could be similar to what have been found in the traditional face-to-face medium. Thus, we hypothesize:

H1. Women are more likely to express their opinions subjectively than men in social media communications.

H2. Women are more likely to express positive opinions in social media communications.

H3. Women are more likely to express negative opinions in social media communications.

To examine gender emotional differences in social media and test the research hypotheses, we develop an advanced and generic framework using sentiment analysis techniques. Few studies have explicitly examined such differences. To the best of our knowledge, the only related study we have found was done by Thelwall et al. [53] which compared the emotional differences between women and men in MySpace (i.e., a social network site). However, they used a random sampling approach to get a relatively small subset of postings and adopted a manual analysis method.

Our proposed analysis framework contains three algorithms for different levels of analyses, including sentence level, phrase level, and word level. Since no study has been done to systematically examine the gender emotional difference in Web forums (a major Web 2.0 communication medium), an empirical experiment is conducted using the proposed framework on a large Web forum that is popular in discussing political issues and is suggested by an expert researcher in gender studies. In the next section, we describe our research design in detail.

## 4. Research design

A systematic and generic research framework is developed to examine gender emotional differences in Web 2.0 social media. As shown in Fig. 1, the framework includes three components: data acquisition, emotion detection, and gender emotion comparison. In the following subsections, we provide detailed description about the <sup>fi</sup>rst two components. For the last component, we use pairwise t-tests to examine the statistical signi<sup>fi</sup>cance of the gender emotional differences. We present our empirical testing results in Section 5.

## 4.1. Data acquisition

The data acquisition component consists of two steps: user-generated content collecting and user-generated content parsing. First, spidering programs are developed to collect all postings from a Web 2.0 site as HTML pages. After that, parsers are built to parse out the text body from the raw HTML pages and store the parsed data in a relational database.

## 4.2. Emotion detection

In the emotion detection component, we use automatic sentiment analysis techniques to calculate the sentiment scores for the two genders using the data collection obtained from the <sup>fi</sup>rst component.

Since the content in a Web 2.0 social media site is often posted in a longitudinal manner (as a sequence of events or conversations), to systematically examine and compare the gender emotional differences over time, we aggregate and organize the sequential postings based on a certain time unit. According to the characteristics of a given Web 2.0 site, the width of the time unit can be days, weeks, months, quarters, years, etc.

To make the analysis more systematic, we adopt both machine learning and semantic orientation approaches by leveraging OpinionFinder and SentiWordNet. OpinionFinder is a well-known

![](/api/attachments/6NVF63D5/fulltext/images/198bc65096469ba175bdedad647f92fa038189fb5c02eedba8e8f18d08ca561e.jpg)  
Fig. 1. Research framework of analyzing gender emotional differences in Web 2.0 media.

For each $t _ { i } \in \mathrm { ~ T ~ }$ (T is a set of text produced within a certain time unit)

For each $s _ { j } \in t _ { i }$ (sj is a given sentence)

If produced(ti) = Women

$$
N _ {w o m e n} + +
$$

Else

$$
N _ {m e n} + +
$$

If C1(sj)  C2(sj) = Subjective AND produced(ti) = Women Nwomen-subjective ++

Else If C1(sj) ∩ C2(sj) = Objective AND produced(ti) = Women Nwomen-objective ++

Else If C1(si) ∩ C2(si) = Subjective AND produced(ti) = Men

Else If C1(sj) O C2(sj) = Objective AND produced(ti) = Men Nmen-objective ++

Scorewomen-subjective ← Nwomen-subjective / Nwomen

Scorewomen-objective ← Nwomen-objective / Nwomen

Scoremen-subjective ← Nmen-subjective / Nmen

Scoremen-objective ← Nmen-objective / Nmen

Fig. 2. The procedure of subjectivity score calculation (Sentence-Level Emotion Detection algorithm).

sentiment classi<sup>fi</sup>cation tool developed by Wiebe's group [46,59,63]. In this study, we use its two major components: (1) the subjective sentence classi<sup>fi</sup>cation component, and (2) the sentiment expression classi<sup>fi</sup>cation component [63] to conduct sentence-level and phrase-level analyses respectively. As a well-known sentiment lexicon, SentiWordNet has been widely used in recent semantic orientation based sentiment classi<sup>fi</sup>cation studies [8,10,11,14,35]. In this study, we use it to conduct the word-level analysis.

## 4.2.1. Sentence-Level Emotion Detection (SED) algorithm

To perform sentence-level emotion detection, we've developed the Sentence-Level Emotion Detection (SED) algorithm. First, we use the two classi<sup>fi</sup>ers in the subjective sentence classi<sup>fi</sup>cation component of OpinionFinder to classify each sentence in the whole data collection to be subjective, objective, or unknown [46,59,63]. The <sup>fi</sup>rst classi<sup>fi</sup>er (C1) tags each sentence as either subjective or objective. It tries to maximize the overall accuracy of classi<sup>fi</sup>cation. The second classi<sup>fi</sup>er (C2) tries to optimize classi<sup>fi</sup>cation precision. Evaluated on 9732 sentences from the MPQA opinion corpus (4352 objective and 5380 subjective sentences), the <sup>fi</sup>rst classi<sup>fi</sup>er achieved an accuracy of 74%, subjective precision of 78.4%, subjective recall of 73.2% and subjective F-measure of 75.7%, and the second classi<sup>fi</sup>er got 91.7% in subjective precision, 30.9% in subjective recall, 83.0% in objective precision, and 32.8% in recall.

Second, we calculate the subjectivity scores using the procedure shown in Fig. 2. Within each time unit, only sentences classi<sup>fi</sup>ed as subjective (objective) by both classi<sup>fi</sup>ers are kept. All the others are treated as “unknown.” Since the total numbers of sentences produced by women and men within a given time unit could be signi<sup>fi</sup>cantly different, we normalize the score by taking into account such total numbers. Speci<sup>fi</sup>cally, for each time unit, the sentence-level subjective (objective) score for women (men) is calculated as the number of sentences classi<sup>fi</sup>ed as subjective (objective) by both C1 and C2 divided by the total number of sentences produced by women (men) within that time unit.

A limitation of the sentence classi<sup>fi</sup>cation component of OpinionFinder is that it cannot provide detailed analyses on the two polarities of positivity and negativity. Thus, the proposed SED algorithm is developed to conduct objectivity and subjectivity analyses instead of positivity and negativity analyses on the sentence level. Although there is a technical limitation about it, we believe it is reasonable to conduct objectivity and subjectivity analyses on the sentence level since sentences can vary a lot in terms of length. For a long sentence, there could be a part of it containing positive emotions and the other part expressing negative sentiments. To overcome this limitation and to provide a more comprehensive analysis result, we conduct positivity and negativity analyses in the phrase and word levels respectively, since phrases and words are more consistent in terms of expressing certain polarity. The two related algorithms are described as follows.

## 4.2.2. Phrase-Level Emotion Detection (PED) algorithm

To perform phrase-level emotion detection, we've developed the Phrase-Level Emotion Detection (PED) algorithm. First, for the whole data collection, we use the sentiment expression classi<sup>fi</sup>cation component of OpinionFinder to identify phrases that express positive or negative sentiments following a two-step analysis [63]. The <sup>fi</sup>rst step classi<sup>fi</sup>es each phrase as neutral or polar using BoosTexter machine learning algorithm [47]. The second step further determines the contextual polarity of all phrases that are identi<sup>fi</sup>ed as polar in the <sup>fi</sup>rst step [64]. Features used in the neutral-polar classi<sup>fi</sup>er include word features, modi<sup>fi</sup>cation features, sentence features, structure features, and document features [64]. Features used in the polarity classi<sup>fi</sup>er include word features and polarity features. Evaluated on the MPQA opinion corpus, this component achieved an overall accuracy of 73.9% which is signi<sup>fi</sup>cantly better than the baseline majority rating method [64].

After that, we calculate the polarity scores using the procedure shown in Fig. 3. Similar to the sentence-level subjectivity score calculation, for each time unit, a phrase-level polarity score is calculated as the number of phrases that are classi<sup>fi</sup>ed as positive (negative) divided by the total number of sentences<sup>1</sup> produced by women (men) in that time unit.

For each $t _ { i } \in \mathrm { ~ T ~ }$ (T is a set of text produced within a certain time unit)

$$
s _ {i} \in t _ {i} (s _ {j}
$$

$$
N _ {w o m e n} + +
$$

Else

$$
N _ {m e n} + +
$$

For each $p _ { i } \in t _ { i } ( p _ { j }$ is a given phrase)

Scorewomen-positive ← Nwomen-positive / Nwomen

Scorewomen-negative ← Nwomen-negative / Nwomen

Fig. 3. The procedure of polarity score calculation (Phrase-Level Emotion Detection algorithm).

## 4.2.3. Word-Level Emotion Detection (WED) algorithm

To perform word-level emotion detection, we've developed the Word-Level Emotion Detection (WED) algorithm. As a widely adopted sentiment-based lexicon, SentiWordNet has been used in recent sentiment classi<sup>fi</sup>cation studies [8,10,11,14]. It assigns to each synset in WordNet three sentiment scores regarding positivity, negativity, and objectivity respectively [13]. To use it, we <sup>fi</sup>rst conduct POS tagging on the whole data collection. Once the POS tag for each word is decided, we then calculate the sentiment score of a word by looking up SentiWordNet. According to previous literature [2,27,28], we include adjectives, adverbs, verbs, and nouns in our analysis. Since each word in SentiWordNet has multiple POS senses, each of which is also related to multiple synsets, we calculate the average positive and average negative scores for its adjective, adverb, verb, and noun senses separately using the prior-polarity formula adopted from previous literature [8,10,14].

$$
\begin{array}{l} \text { Score } (w o r d = p o s) _ {i} \\ = \frac {\sum_ {k \in S e n t i W o r d N e t (w o r d = p o s \& p o l a r i t y = i)} S e n t i W o r d N e t \_ S c o r e (k) _ {i}}{| s y n s e t s (w o r d = p o s) |} \end{array}
$$

Here, pos ∈ {adjective, adverb, verb, noun}, i ∈ {positive, negative}, and k denotes the synsets of a given word in a particular POS sense. To determine the polarity of each word in a given POS sense, we compare the average positive score and the average negative score of that word and treat it as positive if its average positive score is greater than its average negative score, and vice versa. This method of deciding the polarities have been used in previous literature [8,10]. For example, Dang et al. [8] utilized sentiment features (i.e., words with semantic orientations) as an additional dimension of features for the machine learning classi<sup>fi</sup>ers. To determine the semantic orientation (either positive or negative) of each word in different POS senses, sentiment scores were calculated by looking up SentiWordNet. If the positive score was greater than the negative score, the word in the given POS sense was treated as positive.

Denecke [10] developed classi<sup>fi</sup>ers to conduct sentiment analyses on multilingual documents. A proposed classi<sup>fi</sup>er utilized SentiWordNet to calculate the aggregated polarity scores of each document based on the words it contains. A document was classi<sup>fi</sup>ed as positive if its positivity score was greater than or equal to the negativity score. Otherwise, the document was considered as negative.

For each time unit, a word-level polarity score regarding each POS sense (including adjective, adverb, verb, and noun) is calculated as the number of words that are identi<sup>fi</sup>ed as positive (negative) divided by the total number of words produced by women (men) in that time unit. Fig. 4 summarizes the prior-polarity score calculation procedure.

## 5. Experimental study

## 5.1. Data set

To demonstrate our proposed framework to automatically examine gender emotional differences in Web 2.0 social media, we conducted an empirical study on a large Web forum that is popular in discussing political issues and is suggested by an expert researcher in gender studies. As a major type of social media, Web forums provide the general public a platform to express opinions and exchange information with each other no matter they are acquainted or not.

In total, 15,479 and 16,791 messages<sup>2</sup> written by women and men respectively (with self-reported gender information) over 34 months were collected from the study site. For the analysis, we chose the width of the time unit to be one month. On average, women produced 455 messages per month with a similar number, 494, for men. All messages posted in the same month were aggregated to calculate the sentiment scores using the SED, PED, and WED algorithms described in the previous section.

For each $t _ { i } \in \mathrm { T }$ (T is a set of text produced within a certain time unit)

For each wj ∈ ti (wj is a given word)

While pos ∈ {adjective, adverb, verb, noun}

If produced(ti) = Women

N(pos)women ++

Else

N(pos)men++

If Score(word=pos)positive > Score(word=pos)negative

AND produced(ti) = Women

N(pos) women-positive ++

Else If Score(word=pos)positive < Score(word=pos)negativ

AND produced(ti) = Women

N(pos)women-negative ++

Else If Score(word=pos)positive > Score(word=pos)negative

AND produced(ti) = Men

N(pos)men-positive ++

Else If Score(word=pos)positive < Score(word=pos)negativ

AND produced(ti) = Men

N(pos)men-negative ++

Score(pos)women-positive ← N(pos)women-positive / N(pos) women

Score(pos)women-negative ← N(pos)women-negative / N(pos) women

Score(pos)men-positive ← N(pos)men-positive / N(pos) men

Score(pos)men-negative ← N(pos)men-negative / N(pos)men

Fig. 4. The procedure of prior-polarity score calculation (Word-Level Emotion Detection algorithm).

## 5.2. Results and discussion

We used the SED and PED algorithms to calculate the sentenceand phrase-level sentiment scores respectively. For each month, the sentence-level subjectivity scores and phrase-level polarity scores were calculated using the procedures shown in Figs. 2 and 3.

We used the WED algorithm to calculate the word-level sentiment scores. First, we used the Stanford POS tagger (http://nlp.stanford. edu/software/tagger.shtml) to tag the entire data collection. Only words that were tagged as adjective, adverb, verb, or noun were kept for further analysis. We then calculated the prior-polarity scores for each word by looking up SentiWordNet and using the prior-polarity formula mentioned in Section 4.2. Finally, for each POS sense (i.e., adjective, adverb, verb, or noun), the word-level sentiment scores were calculated using the procedure shown in Fig. 4.

One-tailed, pairwise t-tests (with n = 34) were conducted to show the statistical signi<sup>fi</sup>cance of the emotional differences between the two genders. As summarized in Table 1, the sentence-level analysis results indicated that women were signi<sup>fi</sup>cantly more subjective than men (p-value = 0.0087), thus supporting H1. The phrase-level analysis results showed that women were both signi<sup>fi</sup>cantly more positive (p-value = 0.0271) and signi<sup>fi</sup>cantly more negative (p-value b 0.0001) than men. Therefore, H2 and H3 are supported in the phrase-level. In addition, the average objective score of men was greater than that of women, but not statistically signi<sup>fi</sup>cant (p-value = 0.1935).

Table 1  
Sentence-level and phrase-level analysis results.

<table><tr><td>Hypothesis</td><td>Comparison</td><td>Measure</td><td>WomenMean/SD</td><td>MenMean/SD</td><td>p-value</td></tr><tr><td colspan="6">Sentence-level analysis result</td></tr><tr><td>H1</td><td>Women &gt; Men</td><td>Subjectivity</td><td>0.221/0.023</td><td>0.209/0.020</td><td>0.0087**</td></tr><tr><td>H1&#x27;</td><td>Women &lt; Men</td><td>Objectivity</td><td>0.136/0.023</td><td>0.142/0.026</td><td>n.s.</td></tr><tr><td colspan="6">Phrase-level analysis result</td></tr><tr><td>H2</td><td>Women &gt; Men</td><td>Positivity</td><td>0.373/0.052</td><td>0.350/0.041</td><td>0.0271*</td></tr><tr><td>H3</td><td>Women &gt; Men</td><td>Negativity</td><td>0.209/0.028</td><td>0.184/0.025</td><td>&lt;0.0001**</td></tr></table>

Note. Signi<sup>fi</sup>cance levels \* α = 0.05 and \*\* α = 0.01; n.s. indicates not signi<sup>fi</sup>cant.  
' H1 is about subjectivity between women and men. The testing here is based on the objectivity scores.

Table 2 lists the results of the word-level analysis for different POS senses, including adjective, adverb, verb, and noun. The results of six out of all eight comparisons showed that women had signi<sup>fi</sup>cantly higher polarity scores than men. Speci<sup>fi</sup>cally, women were signi<sup>fi</sup>cantly more likely to use negative adjectives than men (p-value = 0.0004). They were also signi<sup>fi</sup>cantly more likely to use positive adverbs in comparison with men (p-value = 0.0009). In terms of verbs, women were signi<sup>fi</sup>cantly more likely to use both positive verbs (p-value = 0.0499) and negative verbs (p-value = 0.0208). When using nouns, women were signi<sup>fi</sup>cantly more likely to use both positive nouns (p-value = 0.0229) and negative nouns (p-value = 0.0014) than men as well. Therefore, H2 is supported in three out of the four POS dimensions, including adverb, verb, and noun. H3 is supported in three POS dimensions that are adjective, verb, and noun. However, out of all eight comparisons, the hypotheses are not supported in two of them — that is positive adjectives and negative adverbs. This could be attributed to the noise introduced by applying sentiment analysis tools, such as OpinionFinder and SentiWordNet, to the social media data. Compared with the traditional data sources, such as news reports and professional articles, social media data is free of styles and lacks a standard structure. This makes it more dif<sup>fi</sup>cult to analyze social media data. In addition, even though OpinionFinder and SentiWordNet are very popular and widely adopted, they could still introduce some noises in the data analysis. Because of that, in this study, we try to conduct relatively comprehensive analyses by performing analyses on three different levels (i.e., sentence, phrase, and word) and leveraging different tools and algorithms. The majority of the analysis results indicate that women are more likely to express their opinions subjectively than men, and they tend to be more likely to express both positive and negative emotions in Web forum communications.

Table 2  
Word-level analysis results.

<table><tr><td>POS</td><td>Hypothesis</td><td>Comparison</td><td>Measure</td><td>Women Mean/SD</td><td>Men Mean/SD</td><td>p-value</td></tr><tr><td rowspan="2">Adjective</td><td>H2</td><td>Women &gt; Men</td><td>Positivity</td><td>0.442/0.024</td><td>0.444/0.025</td><td>n.s.</td></tr><tr><td>H3</td><td>Women &gt; Men</td><td>Negativity</td><td>0.358/0.016</td><td>0.343/0.019</td><td>0.0004**</td></tr><tr><td rowspan="2">Adverb</td><td>H2</td><td>Women &gt; Men</td><td>Positivity</td><td>0.445/0.034</td><td>0.422/0.019</td><td>0.0009**</td></tr><tr><td>H3</td><td>Women &gt; Men</td><td>Negativity</td><td>0.337/0.024</td><td>0.357/0.019</td><td>n.s.</td></tr><tr><td rowspan="2">Verb</td><td>H2</td><td>Women &gt; Men</td><td>Positivity</td><td>0.347/0.020</td><td>0.339/0.013</td><td>0.0499*</td></tr><tr><td>H3</td><td>Women &gt; Men</td><td>Negativity</td><td>0.291/0.013</td><td>0.286/0.011</td><td>0.0208*</td></tr><tr><td rowspan="2">Noun</td><td>H2</td><td>Women &gt; Men</td><td>Positivity</td><td>0.224/0.019</td><td>0.218/0.011</td><td>0.0229*</td></tr><tr><td>H3</td><td>Women &gt; Men</td><td>Negativity</td><td>0.166/0.011</td><td>0.157/0.013</td><td>0.0014**</td></tr></table>

Note. Signi<sup>fi</sup>cance levels ${ } ^ { * } \alpha = 0 . 0 5$ and ${ } ^ { * * } \alpha = 0 . 0 1 ;$ n.s. indicates not signi<sup>fi</sup>cant.

Overall, our analysis results indicate that gender emotional differences do exist in Web forum communications and are consistent with what previous research has found in face-to-face communications. That is, women are more emotionally expressive than men and they are more likely to express both positive and negative emotions.

## 6. Conclusions and future directions

## 6.1. Research contributions

With the advent of Web 2.0, a large and increasing amount of opinion-rich user-generated content has been emerging on the Internet. In addition, more and more women have become active in participating in online communications on Web 2.0 social media. With such a trend, it is becoming important and interesting for researchers, Internet service and product providers, and users to understand gender emotional differences in the new media. However, few studies have systematically examined gender emotional differences in social media. Towards this end, this study has made several research contributions.

First, this study proposes an advanced and generic research framework to automatically analyze gender emotional differences in Web 2.0 social media. The framework leverages sentiment analysis techniques including both machine learning and semantic orientation approaches. Unlike previous research that used the random sampling technique to conduct analyses on a relative small portion of data, the proposed framework can conduct automatic analyses by taking into account all messages in an entire Web 2.0 site. This can provide more comprehensive and unbiased analysis results.

Second, different algorithms are developed and embedded in the framework to investigate gender emotional differences at different granularity levels of expression, including sentence, phrase, and word levels. Different from most existing sentiment analysis studies that focused on document-level analysis, the <sup>fi</sup>ner and detailed analyses provided in the proposed framework can help us better understand gender emotional differences in social media. To the best of our knowledge, this is the <sup>fi</sup>rst study to utilize advanced sentiment analysis techniques to conduct different levels of analyses on gender emotional differences in Web 2.0 media.

In addition, to demonstrate the performance of the proposed framework, an empirical study is conducted on a large Web forum. To the best of our knowledge, this is the <sup>fi</sup>rst empirical study to speci<sup>fi</sup>cally examine gender emotional differences in Web forum communications. The sentence-level analysis results indicate that women are signi<sup>fi</sup>cantly more subjective than men. The phrase- and word-level analysis results show that in general women are signi<sup>fi</sup>cantly more likely to express both positive and negative emotions as compared to men. These <sup>fi</sup>ndings suggest the existence of gender emotional differences in Web 2.0 social media, and are generally consistent with what have been found in face-to-face communications.

## 6.2. Limitations and future research directions

This study demonstrates the gender emotional differences in Webbased communications. Although the online communication channel is distinctive from and less rich than the face-to-face communication channel, users are able to use it to express and share their social– emotional content. This study aims to explore gender emotional differences in the online communication channel. Future research can examine how to leverage both channels together to further help users (especially women) to build and expand their social communities with their friends. Different channels could be more suitable for different types of friends and to express different types of social-emotional content.

Several limitations of this study can be addressed in future research. First, as mentioned in previous literature [37,53], there is no perfect way to measure emotion. Future studies can explore other methodologies to examine whether consistent results can be found about gender emotional differences in Web 2.0 social media. Second, the types of emotion measured in this study focus on positivity versus negativity. Future research can conduct detailed in-depth analyses to investigate more speci<sup>fi</sup>c types of emotion, such as different dimensions of positivity (e.g., happiness, love, and life satisfaction) and different types of negativity (e.g., fear, sadness, and anger). To do that, advanced analysis techniques need to be developed and applied. Third, in this study, an empirical experiment is conducted in Web forum communications. Future research can apply the proposed framework to examine gender emotional differences in other Web 2.0 social media. Moreover, although an English-language data set was used in the experimental study, the proposed framework could be applied to other languages as well, and a multilingual emotion analysis component could be developed to support such research. In addition, to determine the polarity of each word in a given POS sense in the word-level analysis (i.e., the WED algorithm), we compare the average positive score and the average negative score of that word and treat it as positive if its average positive score is greater than its average negative score, and vice versa. This method may not be advanced enough to capture the exact sentiments of each word in a POS sense, since words have various facets. Future research may consider developing more sophisticated and advanced methods, such as adding probability as an attribute, to determine the polarity of different words.

## Acknowledgement

This work was supported by the NSF Computer and Network Systems (CNS) Program, CNS-0709338. We would also like to thank Mr. Chun-Neng Huang for his help in data processing.

## References

[1] A. Abbasi, H. Chen, A. Salem, Sentiment analysis in multiple languages: feature selection for opinion classi<sup>fi</sup>cation in Web forums, ACM Transactions on Informa tion Systems 26 (3) (2008) 1–34.

[2] F. Benamara, C. Cesarano, A. Picariello, D. Reforgiato, V.S. Subrahmanian, Sentiment analysis: adjectives and adverbs are better than adjectives alone, the International Conference on Weblogs and Social Media (ICWSM-2007), AAAI Press, Boulder, CO, 2007, pp. 203–206.

[3] B. Bimber, Measuring the gender gap on the internet, Social Science Quarterly 81 (3) (2000) 868–876.

[4] L.R. Brody, J. Hall, Gender and emotion, in: M. Lewis, J. Haviland (Eds.), Handbook of emotions, Guilford Press, New York, 1993, pp. 447–461.

[5] P. Chaovalit, L. Zhou, Movie review mining: a comparison between supervised and unsupervised classi<sup>fi</sup>cation approaches, the 38th Annual Hawaii International Conference on System Sciences, IEEE Press, Hawaii, HI, 2005.

[6] H. Chen, AI, e-government, and politics 2.0, IEEE Intelligent Systems 24 (5) (2009) 64–67.

[7] CommerceNet, The CommerceNet/Nielsen internet demographic survey (1999) http://www.commerce.net.

[8] Y. Dang, Y. Zhang, H. Chen, A lexicon enhanced method for sentiment classi<sup>fi</sup>cation: An experiment on online product reviews, IEEE Intelligent Systems 25 (4) (2010) 46–53.

[9] K. Dave, S. Lawrence, D. Pennock, Mining the peanut gallery: opinion extraction and semantic classi<sup>fi</sup>cation of product reviews, the International World Wide Web Conference, ACM Press, Budapest, Hungary, 2003, pp. 519–528.

[10] K. Denecke, Using SentiWordNet for multilingual sentiment analysis, the IEEE 24th International Conference on Data Engineering Workshop (ICDEW 2008), IEEE Press, Cancun, 2008, pp. 507–512.

[11] A. Devitt, K. Ahmad, Sentiment polarity identi<sup>fi</sup>cation in <sup>fi</sup>nancial news: a cohesionbased approach, the 45th Annual Meeting of the Association of Computational Linguistics, ACL Press, Prague, 2007, pp. 984–991.

[12] S. Djamasbi, E.T. Loiacono, Do men and women use feedback provided by their Decision Support Systems (DSS) differently? Decision Support Systems 44 (4) (2008) 854–869.

[13] À. Esuli, F. Sebastiani, SentiWordNet: a publicly available lexical resource for opinion mining, LREC-06, the 5th Conference on Language Resources and Evaluation, European Language Resources Association, Genova, Italy, 2006, pp. 417–422

[14] A. Fahrni, M. Klenner, Old wine or warm beer: target-speci<sup>fi</sup>c sentiment analysis of adjectives, Proceedings of the AISB 2008 Symposium on Affective Language in Human and Machine, The Society for the Study of Arti<sup>fi</sup>cial Intelligence and Simulation of Behaviour Press, Aberdeen, Scotland, 2008, pp. 60–63.

[15] Z. Fei, J. Liu, G. Wu, Sentiment classi<sup>fi</sup>cation using phrase patterns, the 4th IEEE International Conference on Computer Information Technology, IEEE Press, 2004, pp. 1147–1152.

[16] A.H. Fischer, A.S.R. Manstead, Gender and culture differences in emotion, Emotion 4 (1) (2004) 87–94.

[17] J.E. Fountain, Constructing the information society: women, Information Technology, and Design, Technology and Society 22 (1) (2000) 45–62.

[18] F. Fujita, E. Diener, E. Sandvik, Gender differences in negative affect and well-being: the case for emotional intensity, Journal of Personality and Social Psychology 61 (1991) 427–434.

[19] J.E. Fuller, Equality in cyberdemocracy? Gauging gender gaps in on-line civic participation, Social Science Quarterly 85 (4) (2004) 938–957.

[20] M. Gamon, Sentiment classi<sup>fi</sup>cation on customer feedback data: noisy data, large feature vectors, and the role of linguistic analysis, the 20th International Conference on Computational Linguistics, ACL Press, Geneva, CH, 2004, pp. 841–847.

[21] M. Gamon, A. Aue, S. Corston-Oliver, E. Ringger, Pulse: mining customer opinions from free text, the 6th International Symposium on Intelligent Data Analysis, Springer, Madrid, Spain, 2005

[22] W.R. Gove, Sex differences in mental illness among adult men and women: an evaluation of four questions raised regarding the evidence on the higher rates of women. Social Science & Medicine 12 (1978) 187-198

[23] M. Grossman, W. Wood, Sex differences in the intensity of emotional experience: a social role interpretation, Journal of Personality and Social Psychology 65 (1993) 1010–1022.

[24] J. Guiller, A. Durndell, Students' linguistic behaviour in online discussion groups: does gender matter? Computers in Human Behavior 23 (5) (2007) 2240–2255.

[25] W. Harcourt, The personal and the political: women using the internet, Cyberpsychology & Behavior 3 (5) (2000) 693–697.

[26] D. Harp, M. Tremayne, The gendered blogosphere: examining inequality using network and feminist theory, Journalism and Mass Communication Quarterly 83 (2)(2006) 247-264

[27] V. Hatzivassiloglou, J. Wiebe, Effects of adjective orientation and gradability on sentence subjectivity, the 18th International Conference on Computational Linguistics, ACL Press, 2000, pp. 299–305.

[28] M. Hu, B. Liu, Mining and summarizing customer reviews, the ACM SIGKDD International Conference, ACM Press, 2004, pp. 168–177.

[29] N. Hu, I. Bose, Y. Gao, L. Liu, Manipulation in digital word-of-mouth: a reality check for book reviews, Decision Support Systems 50 (3) (2011) 627–635.

[30] L.A. Jackson, K.S. Ervin, P.D. Gardner, N. Schmitt, Gender and the internet: women communicating and men searching, Sex Roles: A Journal of Research 44 (5–6) (2001) 363–378.

[31] J.M. Jaffe, Y.E. Lee, L. Huang, H. Oshagan, Gender identi<sup>fi</sup>cation, interdependence and pseudonyms in CMC: language patterns in an electronic conference, The In formation Society 15 (1999) 221–234.

[32] S.-M. Kim, E. Hovy, Automatic identi<sup>fi</sup>cation of pro and con reasons in online reviews, the COLING/ACL Main Conference, ACL Press, Morristown, NJ, 2006, pp. 483–490.

[33] N. Li, D.D. Wu, Using text mining and sentiment analysis for online forums hotspot detection and forecast, Decision Support Systems 48 (2) (2010) 354–368.

[34] B. Liu, Web data mining, Springer, Berlin Heidelberg, 2007.

[35] Y. Liu, Y. Chen, R.F. Lusch, H. Chen, D. Zimbra, S. Zeng, User-generated content on social media: predicting market success with online word-of-mouth, IEEE Intelli gent Systems 25 (1) (2010) 75–78.

[36] R.E. Lucas, C.L. Gohm, Age and sex differences in subjective well-being across cultures, in: E. Diener, E.M. Suh (Eds.), Culture and subjective wellbeing, MIT Press, Cambridge, MA, 2000, pp. 291–318.

[37] I.B. Mauss, M.D. Robinson, Measures of emotion: a review, Cognition and Emotion 23 (2) (2009) 209–237.

[38] V. Midha, Impact of consumer empowerment on online trust: an examination across genders, Decision Support Systems 54 (1) (2012) 198–205

[39] M.L. Newman, C.J. Groom, L.D. Handelman, J.W. Pennebaker, Gender differences in language use: an analysis of 14,000 text samples, Discourse Processes 45 (2008) 211–236.

[40] S. Nolen-Hoeksema, Sex differences in unipolar depression: evidence and theory, Psychological Bulletin 101 (1987) 259–282.

[41] C. Ogan, F. Cicek, M. Ozakca, Letters to Sarah: analysis of email responses to an online editorial, New Media and Society 7 (4) (2005) 533–557.

[42] T. O'Reilly, What is Web 2.0? Design patterns and business models for the next generation of software, http://www.oreillynet.com/pub/a/oreilly/tim/news/2005/09/ 30/what-is-web-20.html2005.

[43] B. Pang, L. Lee, Opinion mining and sentiment analysis, Foundations and Trends in Information Retrieval 1 (1–2) (2008) 1–135.

[44] B. Pang, L. Lee, S. Vaithyanathain, Thumbs up? Sentiment classi<sup>fi</sup>cation using machine learning techniques, the ACL-02 Conference on Empirical Methods in Natural Language Processing (EMNLP), ACL Press, Philadelphia, 2002, pp. 79–86.

[45] Pew internet and American life project, http://www.pewinternet.org/trends/User\_ Demo\_7.22.08.htm 2008.

[46] E. Riloff, J. Wiebe, Learning extraction patterns for subjective expressions, the Conference on Empirical Methods in Natural Language Processing, ACL Press, Morristown, NJ, 2003, pp. 105–112.

[47] R.E. Schapire, Y. Singer, BoosTexter: a boosting-based system for text categorization, Machine Learning 39 (2–3) (2000) 135–168.

[48] R.P. Schumaker, Y. Zhang, C.-N. Huang, H. Chen, Evaluating sentiment in <sup>fi</sup>nancial news articles, Decision Support Systems 53 (3) (2012) 458–464.

[49] C. Seale, S. Ziebland, J. Charteris-Black, Gender, cancer experience and internet use: a comparative keyword analysis of interviews and online cancer support groups, Social Science & Medicine 62 (10) (2006) 2577–2590.

[50] J. Short, B. Christie, E. Williams, The social psychology of telecommunications, Wiley, London, 1976.

[51] J.T. Spence, R.L. Helmreich, Masculinity and femininity, University of Texas Press, Austin, 1978.

[52] L. Sproull, S. Kiesler, Reducing social context cues: Electronic mail in organisational communication, Management Science 32 (1986) 1492–1512.

[53] M. Thelwall, D. Wilkinson, S. Uppal, Data mining emotion in social network communication: gender differences in MySpace, Journal of the American Society for Information Science and Technology (JASIST) 61 (1) (2010) 190–199.

[54] P.D. Turney, Thumbs up or thumbs down? Semantic orientation applied to unsupervised classification of reviews, the 40th Annual Meetings of the Association for Computational Linguistics, ACL Press, Philadelphia, Pennsylvania, 2002, pp. 417–424.

[55] P.D. Turney, M.L. Littman, Measuring praise and criticism: inference of semantic orientation from association, ACM Transactions on Information Systems 21 (4) (2003) 315–346.

[56] C. Van Slyke, C.L. Comunale, F. Belanger, Gender differences in perceptions of web-based shopping, Communications of the ACM 45 (8) (2002) 82–86.

[57] V. Venkatesh, M.G. Morris, Why don't men ever stop to ask for directions? Gender, social in<sup>fl</sup>uence, and their role in technology acceptance and usage behavior, MIS Quarterly 24 (1) (2000) 115–139.

[58] J.B. Walther, Interpersonal effect in computer-mediated interaction: a relational perspective, Communication Research 19 (1992) 50–88.

[59] J. Wiebe, E. Riloff, Creating subjective and objective sentence classi<sup>fi</sup>ers from unannotated texts, the Sixth International Conference on Intelligent Text Processing and Computational Linguistics, Springer, Mexico City, Mexico, 2005.

[60] J. Wiebe, T. Wilson, M. Bell, Identifying collocations for recognizing opinions, the ACL/EACL Workshop on Collocation, ACL Press, Toulouse, France, 2001.

[61] J. Wiebe, T. Wilson, R. Bruce, M. Bell, M. Martin, Learning subjective language, Computational Linguistics 30 (3) (2004) 277–308.

[62] Y. Wilks, M. Stevenson, The grammar of sense: using part-of-speech tags as a <sup>fi</sup>rst step in semantic disambiguation, Journal of Natural Language Engineering 4 (1998) 135–144.

[63] T. Wilson, P. Hoffmann, S. Somasundaran, J. Kessler, J. Wiebe, Y. Choi, C. Cardie, E. Riloff, S. Patwardhan, OpinionFinder: a system for subjectivity analysis, the Human Language Technology Conference, Basis Technology, Vancouver, Canada, 2005.

[64] T. Wilson, J. Wiebe, P. Hoffmann, Recognizing contextual polarity in phrase-level sentiment analysis, the Conference on Human Language Technology and Empirical Methods in Natural Language Processing, Association for Computational Linguistics, Vancouver, Canada, 2005.

[65] W. Wood, N. Rhodes, M. Whelan, Sex differences in positive well-being: a consideration of emotional style and marital status, Psychological Bulletin 106 (1989) 249–264.

[66] H. Yu, H. Yu, Towards answering opinion questions: separating facts from opinions and identifying the polarity of opinion sentences, Proceedings of the 2003 conference on Empirical methods in natural language processing, Association for Computational Linguistics, 2003, pp. 129–136.

[67] C. Zhang, D. Zeng, J. Li, F.-Y. Wang, W. Zuo, Sentiment analysis of chinese documents: from sentence to document level, Journal of the American Society for Information Science and Technology 60 (12) (2009) 2474–2487.

[68] K.Z.K. Zhang, M.K.O. Lee, C.M.K. Cheung, H. Chen, Understanding the role of gender in bloggers' switching behavior, Decision Support Systems 47 (4) (2009) 540–546.

[69] L. Zhou, P. Chaovalit, Ontology-supported polarity mining, Journal of the American Society for Information Science and Technology (JASIST) 59 (1) (2008) 98–110.

Yulei Zhang is an assistant professor of computer information systems in the W.A. Franke College of Business at Northern Arizona University. He received his Ph.D. in management information systems from the University of Arizona. His research interests include social computing and social media analytics, text and Web mining, knowledge management, and information technology adoption. His research has been published in Decision Support Systems, Journal of Management Information Systems, Journal of the American Society for Information Science and Technology, IEEE Intelligent Systems, IEEE Transactions on Systems, Man, and Cybernetics. Part A, and other journals.

Yan Dang is an assistant professor of computer information systems in the W.A. Franke College of Business at Northern Arizona University. She received her Ph.D. in management information systems from the University of Arizona. Her research interests include implementation and adoption of information technology, knowledge-based systems and knowledge management, human cognition and decision making, and human computer interaction. Her research has been published in Decision Support Systems, Journal of Management Information Systems, Journal of the American Society for Information Science and Technology, IEEE Intelligent Systems, IEEE Transactions on Systems, Man, and Cybernetics, Part A, and other journals

Hsinchun Chen is McClelland Professor of Information Systems and the director of the Artificial Intelligence Lab at the University of Arizona. He received his Ph D. in informa: tion systems from New York University. He has authored or edited 18 books, 17 book chapters, and more than 180 Science Citation Index journal articles covering digital library, intelligence analysis, biomedical informatics, data/text/Web mining, knowledge management, and Web computing. He serves on 10 editorial boards and has been an adviser for the U.S. National Science Foundation, U.S. Department of Justice, U.S. National Library of Medicine, U.S. Department of Defense, U.S. Department of Homeland Security, and other international research programs. He received the IEEE Computer Society 2006 Technical Achievement award. He is a fellow of IEEE and the American Association for the Advancement of Science (AAAS).
