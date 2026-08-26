---
otero_id: 14348
otero_key: "CW5EZP2F"
title: "Towards building a high-quality microblog-specific Chinese sentiment lexicon"
authors: "Fangzhao Wu; Yongfeng Huang; Yangqiu Song; Shixia Liu"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.04.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards building a high-quality microblog-specific Chinese sentiment lexicon

Fangzhao Wu<sup>a,</sup>\*, Yongfeng Huang<sup>a</sup>, Yangqiu Song<sup>b</sup>, Shixia Liu<sup>c</sup>

<sup>a</sup>Department of Electronic Engineering, Tsinghua University, Beijing 100084, China

<sup>b</sup>Lane Department of Computer Science and Electrical Engineering, West Virginia University, USA

<sup>c</sup>School of Software, Tsinghua University, Beijing 100084, China

## A R T I C L E I N F O

Article history: Received 18 December 2015 Received in revised form 8 April 2016 Accepted 27 April 2016 Available online xxxx

Keywords: Sentiment lexicon Sentiment analysis Microblog

## A B S T R A C T

Due to the huge popularity of microblogging services, microblogs have become important sources of customer opinions. Sentiment analysis systems can provide useful knowledge to decision support systems and decision makers by aggregating and summarizing the opinions in massive microblogs automatically. The most important component of sentiment analysis systems is sentiment lexicon. However, the perfor mance of traditional sentiment lexicons on microblog sentiment analysis is far from satisfactory, especially for Chinese. In this paper, we propose a data-driven approach to build a high-quality microblog-specific sentiment lexicon for Chinese microblog sentiment analysis system. The core of our method is a unified framework that incorporates three kinds of sentiment knowledge for sentiment lexicon construction, i.e., the word-sentiment knowledge extracted from microblogs with emoticons, the sentiment similarity knowledge extracted from words’ associations among all the messages, and the prior sentiment knowledge extracted from existing sentiment lexicons. In addition, in order to improve the coverage of our sentiment lexicon, we propose an effective method to detect popular new words in microblogs, which considers not only words’ distributions over texts, but also their distributions over users.The detected new words with strong sentiment are incorporated in our sentiment lexicon.We built a microblog-specific Chinese sentiment lexicon on a large microblog dataset with more than 17 million messages. Experimental results on two microblog sentiment datasets show that our microblog-specific sentiment lexicon can significantly improve the performance of microblog sentiment analysis.

© 2016 Elsevier B.V. All rights reserved

## 1. Introduction

Microblogging services, such as Twitter<sup>1</sup> and Weibo<sup>2</sup> , have become increasingly popular in recent years.They provide great platforms to hundreds of millions of users to freely express their opinions on various topics, such products, brands and companies, in an unconstrained and unbiased environment [1]. Thus microblogging platforms have become ideal sources of customer opinions and market intelligence [2]. Analyzing and summarizing the sentiments in these large-scale opinion-rich microblogs can provide useful knowledge to both companies and customers for making better decisions [2,3,4,5]. For example, consumers can make more informed decisions when buying products or services by referring to masses of other customers’ opinions and perform comparison shopping [6]. Companies can sense how and in which aspects their customers like and dislike their products or services in real time. They can remain competitive by inferring customers’ need and taste from their microblogs, and manage good relationships with customers by analyzing and responding to their comments timely [2]. In addition, companies can improve their advertising campaigns and market strategies by analyzing their customers’ opinions towards their brands and products on a large scale [3]. Besides, companies managers can track the fluctuations of their companies’ reputation as well as those of their competitors’ to adjust their producing and sale strategies [7]. However, since microblogs are on an extremely large scale, it is costly and time-consuming to analyze the opinions in them by manual inspection. Thus, sentiment analysis systems which can aggregate, organize, analyze and summarize the opinions in microblogs automatically is very important for extracting useful knowledge from massive opinion-rich microblogs in real time and on a large scale, in order to help decision support systems and decision makers to make better decisions in business activities [2].

Sentiment lexicon, which consists of a list of sentiment words and phrases as well as their sentiment polarities and intensities, is the most important component in sentiment analysis systems [3,8–11]. The performance of sentiment analysis systems heavily depends on the accuracy and coverage of the sentiment lexicon they use. However, existing sentiment lexicons are not suitable for microblog sentiment analysis due to two reasons. First, when posting microblog messages, users frequently use informal new words, such as “tnx” and “coooool”, to express their emotions. Many of these informal new words convey rich sentiment information and are important for microblog sentiment analysis. But they are not covered by traditional sentiment lexicons [12]. Second, formal words may have different sentiments in microblogging scenario. For example, Chinese word “ ” represents a kind of pear in traditional texts. However, it is often used to express “pressure” in microblog messages. Manually detecting and annotating these informal new words and formal words with changed sentiments are costly and time-consuming, because they are on a large scale and continuously emerging. Thus an automatic method to build a microblog-specific sentiment lexicon is of great value [12].

Several methods have been proposed for English microblogspecific sentiment lexicon construction. For example, Kiritchenko et al. proposed to calculate words’ sentiment scores by leveraging their associations with emoticons (such as “:)” ) or sentiment-word hashtags (such as #joy) [13]. Tang et al. regarded the sentiment lexicon construction as a word-level sentiment classification problem, and proposed a representation learning method to classify sentiments of English n-grams in tweets [12]. Compared to English lexicons, building microblog-specific Chinese sentiment lexicon is more challenging because there is no natural segmentation symbol such as blank space to separate continuous Chinese characters into words. Existing Chinese word segmentation tools often fail to detect the user-invented new words used in microblogs and simply split them into single characters [14]. Thus, the aforementioned methods designed for English sentiment lexicon construction cannot be directly applied in our task.

To build a microblog-specific Chinese sentiment lexicon, Feng et al. inferred words’ sentiment scores using their associations with positive and negative sentiment emoticons [15]. However, this method can neither detect new words used in Chinese microblogs nor specify sentiment polarities for them. Thus the coverage of sentiment lexicon built using this method is still limited. More recently, Huang et al. proposed a pattern-based method to detect adjective new words from POS-tagged microblog texts. They computed the sentiment polarities of these words using their associations with sentiment emoticons [14]. They found that incorporating these new sentiment words into traditional sentiment lexicons can benefit Chinese microblog sentiment classification. However, this method still has several limitations. First, it can only detect adjective new sentiment words while many new sentiment words belong to other syntactic classes, such as verb and noun, which limits the coverage of the sentiment lexicon built in this way. Second, since microblog texts are very casual and noisy, it is dificult to obtain high-quality POS-tagging results. And finally, traditional words may change their sentiments when used in microblogging scenario.

To overcome these limitations, in this paper we propose a datadriven approach to build a high-quality microblog-specific Chinese sentiment lexicon.

First, in order to improve the coverage of our sentiment lexicon, we develop an effective new word detection method to detect the popular user-invented new words used in microblogs. The major feature of this method is that it utilizes not only words’ distributions over messages but also their distributions over users. It iteratively detects candidate new words and adds them to the dictionary of Chinese word segmentation tools. The candidate new words detected in previous iterations are refined in subsequent iterations. Accordingly, the word segmentation performance can be improved and more new words can be detected simultaneously.

Second, we propose a unified framework to build a high-quality microblog-specific Chinese sentiment lexicon by incorporating three kinds of sentiment knowledge. The first one is the word-sentiment knowledge, which represents words’ sentiment scores extracted from the associations between words (both formal and new words) and emoticons. The second one is the sentiment similarity knowledge, which represents the sentiment similarities among words, and is extracted from all the available microblog messages. The third one is the prior knowledge extracted from existing sentiment lexicons.

We build a microblog-specific Chinese sentiment lexicon using a large Chinese microblog dataset with more than 17 million messages. Experimental results on two Chinese microblog sentiment datasets validate that our microblog-specific sentiment lexicon can outperform existing sentiment lexicons by a large margin in various sentiment analysis tasks, such as subjectivity detection and sentiment polarity classification, at both sentence and message levels.

The major contributions of our work are as follows:

We propose an effective and purely data-driven method to detect popular user-invented new words in Chinese microblogs, which utilizes both words’ distributions over text messages and their distributions over users. These new words can improve the coverage of our microblog-specific sentiment lexicon significantly.

We propose a unified framework which can incorporate three kinds of sentiment knowledge to build a high-quality microblog-specific sentiment lexicon.

We build a microblog-specific Chinese sentiment lexicon using a large microblog dataset, and conduct extensive experiments on two microblog sentiment datasets to evaluate its performance in various sentiment analysis tasks.

The rest of this paper is organized as follows. Related works are introduced in Section 2. In Section 3, we introduce our new word detection method. We present our approach to microblogspecific sentiment lexicon construction in Section 4. We report the experimental results in Section 5. Section 6 concludes this paper.

## 2. Related work

In this section we introduce several works related to sentiment lexicon construction and Chinese new word detection.

## 2.1. Sentiment lexicon construction

Sentiment lexicons, which consist of a list of sentiment words as well as their sentiment polarities and intensities, play an important role in many sentiment analysis systems [9,10]. Traditional sentiment lexicons were constructed manually [16] or automatically [12,13,17–21]. In automatic methods, usually a set of seed sentiment words and their sentiment labels are given in advance. Then the information in these seed sentiment words is propagated to other words. Many methods following this research direction are based on graph propagation [18,19]. In these methods, a sentiment similarity graph is first constructed, where words and phrases are modeled as nodes and sentiment connections between them are regarded as edges. These sentiment connections can be extracted from thesauruses [8,18], syntactic contexts [19], parsing results [22], and so on. For example, Hu and Liu exploited the synonym and antonym relations in WordNet to construct the sentiment similarity graph [18]. Esuli and Sebastiani used the glosses in WordNet to infer the words’ sentiment relations [8]. Wiebe utilized the dependency triples obtained using an parser to obtain sentiment graph [22]. Velikovich et al. computed the sentiment similarity between a pair of words using the cosine similarity of their local syntactic contexts [19]. The second step in these propagation based methods is iteratively propagating the sentiment information in the seed words along the sentiment similarity graph, and various propagation methods have been explored [8,19,23,24]. For example, Rao and Ravichandran utilized the label propagation algorithm [23], while Velikovich et al. found that graph propagation algorithm performs better than label propagation when sentiment similarity graph contains noise [19]. Random walk and PageRank algorithms also have been used for this task [8,24].

However, as to microblog-specific sentiment lexicon construction, since there are massive formal and informal sentiment words used in microblog texts, it is not practical to construct a microblogspecific sentiment lexicon manually. In addition, traditional thesaurus used in propagation based methods, such as WordNet, cannot cover the massive informal words and phrases widely used in microblogs [12]. Since microblog texts are very casual and noisy, the parsing results are not reliable. Besides, these propagation based methods do not take important sentiment clues in microblog texts, such as emoticons, into account [13].

There have been several explorations in building microblogspecific sentiment lexicons. In [13], Mohamad et al. built two tweet-specific sentiment lexicons based on words’ associations with emoticons and sentiment-word hashtags (such as #joy) respectively. Tang et al. proposed a representation learning approach for building tweet-specific sentiment lexicon [12]. They formulated sentiment construction as a word-level sentiment classification problem, and used emoticons to help learn the distributed representation of words. However, these methods are designed for English microblogs, and are unsuitable for microblog-specific Chinese sentiment lexicon construction, because Chinese microblog texts are noisier and Chinese new words are often mistakenly segmented into single characters by segmentation tools. For building microblog-specific Chinese sentiment lexicons, Feng et al. proposed to compute Chinese words’ sentiment scores using their associations with emoticons, and then refine these associations by means of microblogging search engines [15]. However, this method cannot find informal new words with clear sentiment polarities. Thus the coverage of the sentiment lexicon built using this method is limited. Huang et al. proposed a pattern-based method to detect adjective new sentiment words from the POS-tagged microblog texts [14]. The sentiment polarities of these new words were computed using their associations with emoticons. New words with strong sentiments were added to an existing sentiment lexicon for Chinese microblog sentiment analysis. However, the new sentiment words detected by this method are limited to a specific syntactic class, i.e., adjective, while many popular new words with strong sentiments belong to other syntactic classes, such as verb and noun. In addition, this method depends on the POS-tagging results, which are inaccurate for microblog messages because they are highly noisy and casual.

Different from above methods for microblog-specific Chinese sentiment lexicon construction, our method can detect new words belonging to all syntactic classes. Our microblog-specific sentiment lexicon contains both formal words and informal new words. Their sentiment polarities and intensities are specified not only according to their associations with emoticons, but also according to the sentiment similarities among them and prior sentiment knowledge inferred from existing sentiment lexicons.

In summary, our approach is different from existing sentiment lexicon construction methods in three major aspects. First, different from existing methods which mainly build sentiment lexicon for formal texts, our approach focuses on building sentiment lexicon for microblog sentiment analysis, which is a more challenging task because there are masses of user-invented informal sentiment words in microblogs and these words are quickly time-evolving. Second, different from existing microblog sentiment lexicon construction methods which mainly build English lexicons, the purpose of our approach is building a microblog-specific Chinese sentiment lexicon, which is more dificult because there is no natural segmentation symbol (such as blank space) to separate words in Chinese language and it is hard to figure out the massive user-invented new Chinese words for existing Chinese word segmentation tools. Thus we propose an effective and eficient method to detect the popular userinvented new Chinese words from 17 million messages. Third, different from existing methods to microblog-specific sentiment lexicon construction which mainly utilize one type of sentiment knowledge, our approach can incorporate three kinds of sentiment knowledge into a unified framework to build a high-quality microblog-specific sentiment lexicon. The experimental results show that each kind of sentiment knowledge used in our approach is useful for sentiment lexicon construction and by combining them together our approach can achieve significantly better performance than existing sentiment lexicons.

## 2.2. Chinese new word detection

New word detection is very important for many Chinese natural language processing tasks, such as word segmentation, name entity recognition, sentiment analysis, question answering, and so on [14]. New words are emerging all the time and traditional word dictionaries cannot cover these words completely and timely. Researchers have found that more than 60% word segmentation errors are caused by new words [25].

Various methods have been proposed for new word detection. The first kind of methods integrate new word detection into word segmentation [26]. In these methods, the most probable word segments which are not included in existing word dictionaries are extracted as candidate new words. Thus new word detection is regarded as a sub-task of word segmentation in these methods. The second kind of methods are based on complex linguistic rules and knowledge, such as regular expressions [27], morphological rules [28] and so on. Designing these rules needs the help of linguistic experts and these rules cannot cover all the cases. The third type of methods formulate new word detection as a classification problem [29]. Engineering informative linguistic features and labeling enough training data are important for these methods, both of which are costly and time-consuming. The fourth type of methods are statistical methods, which are unsupervised and treat new word detection as a multiword expression extraction problem [30–33], since new Chinese words are usually new combinations of multiple Chinese characters. Pointwise mutual information (PMI) is the first model proposed to measure the bi-gram association [30]. Afterwards, many varieties of PMI were proposed [31]. In order to measure association of n-grams, Enhanced Mutual Information (EMI) was proposed [32].

Our method to new word detection belongs to statistical method. The difference is that we not only consider the association of a candidate new word among the texts, but also consider its association among different users. In this way, many spurious candidate new words can be filtered. In addition, our method iteratively detects low-order n-gram candidate new words from the word segmentation results of existing Chinese word segmentation tools and adds these new words into the dictionary of these tools. In this way, our method can detect new words and improve word segmentation performance simultaneously, and has a much lower complexity than EMI.

## 3. New word detection

When posting microblog messages, users frequently use new words for different reasons, such as showing personality, expressing strong emotions, making their message lively, and so on. Many of these new words remain Out-Of-Vocabulary (OOV) words for many Chinese NLP tools, which brings big challenges to many Chinese NLP tasks, such as Chinese word segmentation, named entity recognition (NER), machine translation, and so on [14]. Researchers have found that more than 60% word segmentation errors are caused by new words [25]. For example, a Chinese microblog message may be “ ” (So annoying!). The correct segmentation result is “ (so, adverb) (annoying, adjective).” However, many mainstream Chinese word segmentation tools, such as NLPIR <sup>3</sup> and ANSJ <sup>4</sup> , segment it to be “ (good, adjective) (hole, noun) (dad, noun)”, which is wrong because they do not recognize that “ ” is a new word. Thus, new word detection is very important for segmenting microblog texts into words correctly.

New word detection is also important for microblog sentiment analysis, because many widely used new words convey strong emotions. They are important for understanding the sentiments contained in microblog messages. In addition, the sentiments of these new words usually cannot be inferred from the characters they contain. For example, $" \mathcal { H } \mathcal { K } "$ is a popular new word which means “happy”, because it shares similar pronunciation with “ ” (happy). However, neither “ ” (open) nor “ ” (forest) contains any sentiment polarity. Thus, if we cannot recognize that “ ” is a new word, then microblog messages like “ ” (Today I am very happy) will be misclassified into neutral, which is in fact positive. Another example is “ ”, whose meaning is “extremely handsome”. This new word conveys a strong positive sentiment. The first character “ ” means “handsome” and is positive. However, the second character “ ” means “dull” and is negative. Thus, it is hard to classify microblog messages like “ ” (You are very handsome today) if we cannot identify that $" \Vert \Vert \frac { _ { \mathrm { ~ H ~ } } } { \mathrm { ~ \uparrow ~ } } \ " $ is a new word and incorrectly segment it into “ ” and “ ”.

Existing Chinese word segmentation tools tend to segment new words into multiple characters and/or words. Thus, we formulate Chinese new word detection as a multi-word expression extraction problem. Many statistical methods such as pointwise mutual information (PMI) [30], enhanced mutual information (EMI) [32], and symmetrical conditional probability (SCP) [33], can be applied to solve this problem. In this paper, we select EMI to compute the associations of multi-word expressions, i.e., candidate new words. Assume a candidate new word w consists of T single characters and/or words $w _ { 1 } , w _ { 2 } , \dots , w _ { T } ,$ , i.e., $w = w _ { 1 } w _ { 2 } \dots w _ { T } ,$ then the EMI score of w is defined as:

$$
E M I (w) = \log \frac {n _ {w} / N}{\prod_ {i = 1} ^ {T} (n _ {w _ {i}} - n _ {w}) / N},\tag{1}
$$

where $n _ { w }$ is the frequency of w, $n _ { w _ { i } }$ is the frequency of $w _ { i } ,$ and N is the total number of documents [32]. If a multi-word expression has a higher EMI score, then the association of the characters and/or words it consists of is stronger, and it has a higher probability to be a new word.

In existing statistics-based new word detection methods, such as EMI and SCP, the association of a multi-word expression is computed only using its distribution over texts. Different from traditional texts, social media texts contain not only the textual content information, but also the information of authors who post them. These author records can provide useful additional information for our microblog new word detection task, because a popular new word should not only have high frequency, but also be widely used by a large number of microblogging users. If a multi-word expression is used by only a single user or a small group of users, then it has a high probability to be a substring of some template-generated texts or advertisements, and should be filtered, no matter how frequently it appears. Motivated by this observation, in this paper we propose a new measure for microblog new word detection, which we denote as UserEMI and is defined in Eq. (2):

$$
\text { UserEMI } (w) = \log \frac {n _ {w} ^ {u} / N _ {u}}{\prod_ {i = 1} ^ {T} \left(n _ {w _ {i}} ^ {u} - n _ {w} ^ {u}\right) / N _ {u}},\tag{2}
$$

where $w = w _ { 1 } w _ { 2 } \dots w _ { T } . n _ { w } ^ { u }$ and $n _ { w _ { i } } ^ { u }$ are the numbers of users who use w and w at least once respectively, and $N _ { u }$ is the total number of users. If a multi-word expression w is used by more users, then it tends to have a higher UserEMI score, indicating that it has a strong association over different users. The final association score of a multiword expression w is defined as:

$$
\operatorname{Score} (w) = \theta E M I (w) + (1 - \theta) \text { UserEMI } (w),\tag{3}
$$

where $\theta \in \left[ 0 , 1 \right]$ is the linear combination parameter. In this paper we empirically set $\theta = 0 . 5$ . That is to say we regard EMI and UserEMI as equally important.

Unlike PMI which only can measure the association of bi-grams, our EMI-based method can measure the association of n-grams. However, since microblog text is casual and noisy, the number of n-grams<sup>5</sup> grows very quickly as n increases, which brings a big challenge to computer memory. In order to overcome this dificulty, we propose an iterative method which has significantly lower memory requirement compared with the original EMI method. Our new word detection method is summarized in Algorithm 1. In each iteration, we find low-order multi-word expressions (in this paper we use bi-grams and 3-grams), and calculate their frequencies and association scores. Then, the multi-word expressions whose frequencies and association scores both exceed predefined thresholds are added to the candidate new word set, which are further added to the dictionary of Chinese word segmentation tools to improve the word segmentation performance. The frequencies of candidate new words found in previous iterations are also updated in current iteration, and those with a frequency lower than threshold will be filtered. Above processes are iteratively conducted until no candidate new word is added or filtered.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1. Our microblog new word detection algorithm.

1: Input: Microblog dataset D, Chinese segmentation tool SegTool, the threshold of word frequency  $t_{n}$  and the threshold of word association score  $t_{s}$ .

2: Output: The set of candidate new words W.

3: Initialize W as an empty set, iteration index iter = 0.

4: while the convergence condition is not satisfied do

5: iter = iter + 1.

6: Use W as additional dictionary of SegTool.

7: Segment all messages in D into words using SegTool.

8: Count words' frequencies w.r.t. messages and users and save them in F =  $\{(w_{i}, n_{i}, n_{i}^{u}) | i = 1, 2, \ldots\}$ .

9: Filter the words in W whose frequencies are lower than  $t_{n}$  according to F.

10: Find all the bi-grams and 3-grams, count their frequencies w.r.t. messages and users, save them in G =  $\{(w_{i}, n_{i}, n_{i}^{u}) | i = 1, 2, \ldots\}$ .

11: Compute the association scores of these n-grams in G using Eq. (3).

12: Add the n-grams whose frequencies are higher than  $t_{n}$  and association scores higher than  $t_{s}$  to W.

13: end while

14: Return W as the set of candidate new words.
</div>

## 4. Sentiment lexicon construction

Sentiment lexicon is the most important component in sentiment analysis systems [3,18]. Traditional sentiment lexicons have achieved huge success in classifying the sentiments of product reviews [18], movie reviews [17] and news articles [34]. However, they are not suitable for microblog sentiment analysis due to two reasons. First, there are masses of popular user-invented new words used in microblogs, which may convey strong sentiment polarities but are not contained in these traditional sentiment lexicons. For example, Chinese microblogging users frequently use new words such as $\ " \angle \bigtriangleup \mathbb { H } \sharp \ " $ (kiss), $\ J \overline { { \mathcal { H } } } \overline { { \mathcal { H } } } \overline { { \mathfrak { P } } }$ (happy), and “ ” (darling) to express emotions, which are user-invented informal words and contain clear sentiment information. Second, formal words may convey different sentiments when used in social media scenario. For example, $" { \underline { { \mathbf { \sigma } } } } \cdot \ '$ is a neutral word in traditional texts which means “two”. But in microblogs it is frequently used to express “stupid”. Another example is $" \mathbb { H } \underline { { \mathbb { H } } } \ Zmathring { \ast } ^ { \prime \downarrow } \ Y$ , which represents a kind of pear. However, microblogging users often use it to express “pressure”, because it has similar pronunciation with $" \mathbb { E } \mathcal { H } ^ { \prime \prime }$ (pressure).

Since the new words with strong sentiments and the formal words with changed sentiments are on a large scale and continuously emerging, it is impractical to manually identify and annotate them. In this paper we propose an automatic and purely data-driven method to build a microblog-specific sentiment lexicon for Chinese microblog sentiment analysis. Specifically, we propose a unified framework which can incorporate three kinds of sentiment knowledge for sentiment lexicon construction, i.e., microblog-specific word-sentiment knowledge extracted from microblog messages with emoticons, sentiment similarity knowledge extracted from all the messages, and prior sentiment knowledge extracted from existing sentiment lexicons. Next we describe how to extract these three kinds of sentiment knowledge and how to incorporate them into our framework.

## 4.1. Word-sentiment knowledge

When posting microblog messages, users frequently use emoticons to express their emotions. Chinese microblogging services, such as Sina Weibo, make it very convenient for users to insert emoticons into their messages, usually with only two to three mouse clicks. Researchers have found that more than 16% Chinese microblog messages contain at least one emoticon [15]. These emoticons contain useful sentiment information. For example, (laugh) and (lovely) are usually used to express positive emotions. (angry) and (sad) usually indicate negative emotions. We can regard these emoticons as noisy sentiment labels, and estimate a word’s sentiment score using its association with emoticons. In this paper, we use pointwise mutual information (PMI) [30] to measure the associations, which is defined as follows:

$$
P M I (a, b) = \log {\frac {p (a , b)}{p (a) p (b)}},\tag{4}
$$

where a and b are two random variables, $p ( a )$ and $p ( b )$ are their marginal probabilities, and $p ( a , b )$ is the probability they co-occur. If two random variables share a higher PMI score, then they have a stronger statistical dependency.

The sentiment score of a word w is defined as its PMI score with positive emoticons minus its PMI score with negative emoticons, shown in Eq. (5):

$$
\begin{array}{l} S e n t i S c o r e (w) = P M I (w, p o s E m o) - P M I (w, n e g E m o) \\ \qquad = \log \frac {n (w , p o s E m o) N}{n (w) n (p o s E m o)} - \log \frac {n (w , n e g E m o) N}{n (w) n (n e g E m o)} \\ \qquad = \log \frac {n (w , p o s E m o) n (n e g E m o)}{n (w , n e g E m o) n (p o s E m o)} \\ \qquad = \log \frac {p (w | p o s E m o)}{p (w | n e g E m o)}, \end{array}\tag{5}
$$

where posEmo and negEmo are positive and negative emoticon sets respectively. N represents the total number of messages. n(w, posEmo) and n(w, negEmo) are the frequencies of word w cooccurring with positive and negative emotions respectively. n(w), n(posEmo) and n(negEmo) are the frequencies of word w, positive emoticons and negative emoticons respectively. According to Eq. (5), the sentiment score of word w is in fact the logarithm of the ratio of its conditional probability given positive emoticons to its conditional probability given negative emoticons.

## 4.2. Sentiment similarity knowledge

Although microblog messages with emoticons are common in microblogging websites, most of the messages are without emoticons. Not containing emoticon does not mean that there is no sentiment in them. In fact, masses of them convey strong and clear sentiments. Although we can not infer the words’ sentiment polarities from these messages, we can still obtain some useful information. A common phenomenon is that sentiment words with the same similarity frequently co-occur with each other. For example, a Chinese microblog message may be “ ” (Failed the exam, very sad). There are many cases that $\arg \# \# \# \arg$ (fail) and “ ” (sad) co-occur. Thus they have a high probability to convey the similar sentiments.

In this paper, we propose to estimate words’ sentiment similarities using their PMI scores, as defined in $\operatorname { E q . }$ (6):

$$
S e n t i S i m i l a r i t y \left(w _ {i}, w _ {j}\right) = \log \frac {n \left(w _ {i} , w _ {j}\right) N}{n \left(w _ {i}\right) n \left(w _ {j}\right)},\tag{6}
$$

where n(w ) and $n ( w _ { j } )$ are the frequencies of words w and w respectively. $n ( w _ { i } , w _ { j } )$ is frequency of word w and w co-occurring, and N is the number of all sentences. From Eq. (6) we can see that if two words have a higher probability to co-occur, then they will have a larger SentiSimilarity score and tend to convey similar sentiments. Note that the sentiment similarity score between two words calculated according to Eq. (6) can be negative. In this case we set it to zero. In other words, we only keep positive sentiment similarity scores.

## 4.3. Prior sentiment knowledge

Although some formal words change their sentiments when used in microblogging scenario, most of the traditional sentiment words convey the same sentiment polarities in both traditional texts and social media texts. Thus, although traditional sentiment lexicons do not cover the new words with strong sentiments, they can still provide some useful prior sentiment knowledge of the traditional sentiment words. We define the prior sentiment score (priorScore) of a word w inferred from an existing sentiment lexicon SL using Eq. (7):

$$
p r i o r S c o r e (w) = \left\{ \begin{array}{l l} 1 & \text { if   w   is   labeled   as   positive   in   SL }, \\ - 1 & \text { if   w   is   labeled   as   negative   in   SL }, \\ 0 & \text { otherwise }. \end{array} \right.\tag{7}
$$

Please cite this article as: F. Wu, Y. Huang, Y. Song, S. Liu, Towards building a high-quality microblog-specific Chinese sentiment lexicon, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.007

## 4.4. Sentiment lexicon construction framework

In this section, we introduce the sentiment lexicon construction framework, which can integrate the three kinds of sentiment knowledge described in previous sections and output a highquality microblog-specific sentiment lexicon. First we introduce some notations that will be used. We denote $\textbf { \textsf { s } } \in \ \mathbb { R } ^ { D \times 1 }$ as the word-sentiment knowledge, inferred from microblog messages with emoticons using Eq. (5), where D is the size of dictionary, i.e., the number of all words. s is the SentiScore of the i-th word in the dictionary. Denote $\pmb { \Lambda } \in \dot { \mathbb { R } } ^ { D \times D }$ as the sentiment similarity knowledge extracted from all the microblog messages according to Eq. $( 6 ) . A _ { i , j }$ is the sentiment similarity score between word i and word j. We use $\pmb { \mathrm { p } } \in \mathbb { R } ^ { D \times 1 }$ to represent the prior sentiment knowledge extracted from an existing sentiment lexicon using $\operatorname { E q . } ( 7 )$ and $p _ { i }$ is the prior sentiment score of the i-th word. Denote $\mathbf { x } \in \mathbb { R } ^ { D \times 1 }$ as the sentiment score vector of the final sentiment lexicon, which is the output of our framework.

Based on above notations, the unified framework proposed in this paper for microblog-specific sentiment lexicon construction is formulated as follows:

$$
\begin{array}{l} \arg \min _ {\mathbf {x}} \mathcal {L} (\mathbf {x}) = \sum_ {i = 1} ^ {D} (x _ {i} - s _ {i}) ^ {2} + \frac {1}{2} \alpha \sum_ {i = 1} ^ {D} \sum_ {j \neq i} A _ {i j} (x _ {i} - x _ {j}) ^ {2} - \beta \sum_ {i = 1} ^ {D} p _ {i} x _ {i} \\ \qquad + \lambda \sum_ {i = 1} ^ {D} | x _ {i} | = \| \mathbf {x} - \mathbf {s} \| _ {2} ^ {2} + \alpha \mathbf {x} ^ {T} \mathbf {L x} - \beta \mathbf {p} ^ {T} \mathbf {x} + \lambda \| \mathbf {x} \| _ {1}, \end{array}\tag{8}
$$

where $\alpha , \beta ,$ and k are non-negative regularization parameters. L is the Laplacian matrix of $\mathbf { A } ,$ , which is defined as $\mathbf { L } = \mathbf { D } - \mathbf { A } ,$ , where D is a diagonal matrix and $\begin{array} { r } { D _ { i i } = \sum _ { i = 1 } ^ { D } A _ { i j } . } \end{array}$

In Eq. (8), minimizing $\textstyle \sum _ { i = 1 } ^ { D } ( x _ { i } - s _ { i } ) ^ { 2 }$ means that we hope the final sentiment scores are consistent with their original word-sentiment knowledge inferred from the large-scale messages with emoticons. In addition, by minimizing $\textstyle \sum _ { i = 1 } ^ { D } { \bar { \sum } } _ { j \not = i } A _ { i j } { ( x _ { i } - x _ { j } ) } ^ { 2 }$ , we constrain that if a pair of words share strong sentiment similarity, then their final sentiment scores should not differ from each other too much. Besides, minimizing $\Sigma _ { i = 1 } ^ { D }$ p x means that if a word i is contained in an existing sentiment lexicon, i.e., $p _ { i } \neq 0$ , then its final sentiment score should not violate its prior sentiment polarity too much. Moreover, introducing the $L _ { 1 } \ L _ { }$ -norm regularization of the final sentiment scores is motivated by Lasso [35], which can set some parameters to exact zeros. Since not all the words are sentiment words, introducing this term can be regarded as sentiment words selection. Our framework in Eq. (8) is a convex optimization problem [36] and we use FISTA algorithm [37] to solve it in this paper.

## 5. Experiments

We report the experimental results in this section. We first introduce the datasets used in our experiments. Then we report the results of our new word detection method. After that, we introduce our microblog-specific sentiment lexicon in detail and show its effectiveness in microblog subjectivity detection and sentiment polarity classification. In the end, we discuss the influence of parameter values on the performance of our sentiment lexicon.

## Table 1

The statistics of the datasets for sentiment lexicon evaluation.

<table><tr><td>Name</td><td>#Objective</td><td>#Positive</td><td>#Negative</td><td>#Total</td><td>Granularity</td></tr><tr><td>EvaData1</td><td>1171</td><td>370</td><td>1607</td><td>3148</td><td>Sentence level</td></tr><tr><td>EvaData2</td><td>637</td><td>550</td><td>877</td><td>2064</td><td>Message level</td></tr></table>

Table 2  
Several examples of the popular user-invented new words detected by our method.

<table><tr><td>No.</td><td>Word</td><td>Meaning</td><td>Frequency</td></tr><tr><td>1</td><td>傻逼</td><td>The stupid</td><td>29,089</td></tr><tr><td>2</td><td>男神</td><td>Male idol</td><td>17,163</td></tr><tr><td>3</td><td>闺蜜</td><td>Bestie</td><td>15,201</td></tr><tr><td>4</td><td>逗比</td><td>Funny</td><td>11,654</td></tr><tr><td>5</td><td>吐槽</td><td>Complain</td><td>9570</td></tr><tr><td>6</td><td>点赞</td><td>Admire</td><td>7232</td></tr><tr><td>7</td><td>靠谱</td><td>Reliable</td><td>6731</td></tr></table>

## 5.1. Dataset description

Three Chinese microblog datasets were used in our experiments. The first one is a large dataset for microblog-specific sentiment lexicon construction. It was crawled using Sina Weibo API during a time period from Feb. 1st, 2015 to April 1st, 2015.

Sina Weibo is the most popular Chinese microblogging website, with more than 5 hundred million users. We removed the repetitive messages according to their IDs. We also filtered noisy microblog messages such as advertisements. Finally, we obtained 17,095,031 unique microblog messages posted by 5,617,972 users. This dataset is denoted as LargeData, and is used for new word detection and microblog-specific Chinese sentiment lexicon construction.

The second dataset is a Chinese microblog sentiment dataset provided by NLP&CC $2 0 1 2 ^ { 6 }$ . This dataset was crawled from Tecent Weibo<sup>7</sup> , another major microblogging website in China. It contains 2023 labeled messages on 20 topics. Each message was split into sentences, and each sentence was manually annotated according to their subjectivity. Each subjective sentence was further annotated with their polarity. There are 3148 labeled sentences in total, among which 1171 are objective and 1977 are subjective. In these subjective sentences, 370 are positive and 1607 are negative. This dataset is used for evaluating the performance of our microblog-specific sentiment lexicon. We denote this dataset as EvaData1 and summarize it in Table 1.

The third dataset is also used for sentiment lexicon evaluation. Since EvaData1 is a sentence-level Chinese microblog sentiment dataset and we cannot find any public available message-level dataset for Chinese microblog sentiment analysis, we built one by ourselves. We randomly sampled 4000 messages from LargeData<sup>8</sup>, and invited three annotators to label these messages with four categories, i.e., neutral (objective), positive, negative and irrelevant (noisy or containing multiple sentiments). Majority voting was applied to specify the final sentiment label for each message. Finally we obtained 637 neutral messages, 550 positive messages, and 877 negative messages. Others are irrelevant. This dataset is denoted as EvaData2 and summarized in Table 1.

## 5.2. New word detection

In this section we present the experimental results of our new word detection method. These experiments were conducted on LargeData dataset. Table 2 shows several popular user-invented new words detected by our method.

We can see from Table 2 that the popular new words detected by our method are correct. In addition, they are widely used in microblog messages. Adding these new words to the dictionary of

![](/api/attachments/CW5EZP2F/fulltext/images/7aa2b8eb5958590ead59cf4fcf0d18536c70cbae13cd8a46777445268da8d0a5.jpg)  
Fig. 1. The precisions of different new word detection methods on top 100, 500, and 1000 words with the highest frequencies. The precisions were calculated by manual inspection.

Chinese word segmentation tools will be useful for improving the word segmentation accuracy. In addition, many of these new words, such as “ ” (complain), “ ” (support), and “ ” (reliable), convey strong sentiment polarity. Incorporating them into our sentiment lexicon can improve its coverage significantly and is beneficial for microblog sentiment analysis.

We also conducted experiments to compare the performance of our new word detection method with two baseline methods. The first method is the original EMI method Eq. (1). We limited the maximal value of n in Eq. (1) to be 5. This method was introduced to verify whether our iterative method can find new words more accurately than directly applying EMI. The second method is similar with our method which iteratively finds new words and adds them to dictionary of Chinese word segmentation tools. The difference is that in each iteration the association score of a candidate new word is computed only using its distribution over texts Eq. (1) in this method, while our method can take both the distribution over texts and distribution over users into consideration Eq. (3). This method is denoted as IterEMI and is used to verify whether incorporating user information can help improve new word detection accuracy. In all the three methods, the threshold of minimal frequency of a candidate new word is set to 200, the minimal association score is set to 1, and the maximal length of a candidate new word is set to 7. The performance of our new word detection method and these two baseline methods are shown in Fig. 1.

From Fig. 1, our new word detection method achieves the best performance. Our method can outperform the original EMI method because our method can improve the word segmentation performance by adding the detected new words into dictionary, which in turn helps find more candidate new words. The shortcoming of EMI is that it may find many n-grams which have high association scores but are substrings of some long words. For example, “ ” was found by EMI as a new word, but it has no specific meaning. In fact, it is a substring of the new word “ ” (cute). The better performance of our method compared with IterEMI indicates that incorporating user information is useful for filtering some frequent word sequences generated using templates by a small group of people.

Our method found 4346 new words in total. We added these new words to the dictionary of ANSJ<sup>9</sup> , a popular Chinese word segmentation tool, and used this tool to segment Chinese microblog messages in following experiments.

## Table 3

Statistics of different sentiment lexicons.

<table><tr><td>Lexicon</td><td>#Positive</td><td>#Negative</td><td>#Total</td></tr><tr><td>SWOL</td><td>11,229</td><td>10,783</td><td>22,012</td></tr><tr><td>HowNetSenti</td><td>4504</td><td>4370</td><td>8874</td></tr><tr><td>NTUSD</td><td>2810</td><td>8274</td><td>11,084</td></tr><tr><td>Ours</td><td>3420</td><td>3122</td><td>6542</td></tr></table>

## 5.3. Sentiment lexicon construction

In this section we introduce the microblog-specific sentiment lexicon we built and evaluate its performance in microblog sentiment analysis tasks.

The word-sentiment knowledge (Section 4.1) was extracted using the messages with emoticons in the LargeData dataset. We manually labeled 100 most frequently used emoticons according to their sentiment polarities.

Then we extracted all the microblog messages in LargeData which contains at least one of these emoticons. Messages that contain both positive emoticons and negative emoticons were filtered. We obtained 969,295 messages in total and denote them as Emoti-Data. The word-sentiment scores were computed using EmotiData according to Eq. (5).

The sentiment similarity knowledge (Section 4.2) was also extracted from LargeData. If two words $w _ { 1 }$ and w co-occur in the same sentence, then their co-occur frequency $n ( w _ { 1 } , w _ { 2 } )$ increases by one. In order to avoid the cases that opposite sentiments are expressed in the same sentence, if a sentence contains Chinese negations words, then this sentence will not be considered in sentiment similarity knowledge extraction. The sentiment similarity scores were calculated according to Eq. (6). We filtered the sentiment similarities whose scores are less than 1 in order to reduce noise.

The prior sentiment knowledge (Section 4.3) was extracted from an existing Chinese sentiment lexicon, which is called “Sentiment Word Ontology Library” (denoted as SWOL)<sup>10</sup> . It contains 11,229 positive words and 10,783 negative words, as shown in Table 3. This sentiment lexicon has a large coverage of traditional sentiment words.

Based on the three kinds of sentiment knowledge described above, we applied our framework (Eq. (8)) to construct our microblog-specific Chinese sentiment lexicon. The parameters q and $L _ { 0 }$ were manually set to 2 and 1 respectively. The values of $\alpha , \beta$ and k were set to 0.4, 0.3, and 0.75 respectively. Finally, we obtained 3420 positive words and 3122 negative words in our microblog-specific sentiment lexicon, as summarized in Table 3. Several representative words with the highest positive and negative sentiment scores are shown in Table 4.

From Table 4, the words with high sentiment scores in our sentiment lexicon convey strong sentiments. Their sentiment polarities are consistent with our intuition. In addition, many of these

Table 4  
Several examples of the sentiment words in our microblog-specific sentiment lexicon.

<table><tr><td rowspan="2">No.</td><td colspan="3">Positive</td><td colspan="3">Negative</td></tr><tr><td>Word</td><td>Meaning</td><td>Score</td><td>Word</td><td>Meaning</td><td>Score</td></tr><tr><td>1</td><td>美美哒</td><td>Beautiful</td><td>1.293</td><td>心塞</td><td>Sad</td><td>-1.776</td></tr><tr><td>2</td><td>超赞</td><td>Great</td><td>1.161</td><td>头晕</td><td>Dizzy</td><td>-1.619</td></tr><tr><td>3</td><td>么么哒</td><td>Kiss</td><td>1.118</td><td>胃痛</td><td>Stomachache</td><td>-1.535</td></tr><tr><td>4</td><td>美腻</td><td>Beauty</td><td>1.049</td><td>泪奔</td><td>Cry</td><td>-1.404</td></tr><tr><td>5</td><td>开森</td><td>Happy</td><td>1.038</td><td>忧桑</td><td>Depressed</td><td>-1.359</td></tr></table>

Table 5

words, such as “ ” (kiss), “ ” (beauty), “ ” (happy), “ ” (cry), and “ ” (sad), are popular user-invented new words. They are important for microblog sentiment analysis, but are not included in traditional sentiment lexicons.

We further evaluated our microblog-specific sentiment lexicon using its performance on two microblog sentiment analysis tasks. The first task is subjectivity detection, i.e., judging whether a text contains subjective information or not [9,10]. The second task is sentiment polarity classification, i.e., classifying an opinionated text into positive or negative according to the sentiment polarity [9]. We followed the lexicon based sentiment classification method proposed in [19]. First, if a sentence contains an odd number of negation words, then the sentiment polarities of the words within the scope of the negation words were inversed. Second, the sentiment scores of all the words in the sentence are summarized to represent the sentiment score of the sentence. Third, if a message contains multiple sentences, then its sentiment score is specified by the average of all the sentences’ sentiment scores. If a message’s sentiment score is zero, then it is classified to be objective; otherwise, subjective. If the sentiment score of a subjective message is greater than zero, then it is regarded as positive; otherwise, negative. Our experiments were conducted on the two manually labeled datasets, i.e., EvaData1 and EvaData2, which are shown in Table 1. EvaData1 is sentence-level and EvaData2 is message-level. Macro-averaged F-score was used to measure the performance.

We compared the performance of our microblog-specific sentiment lexicon with a series of existing sentiment lexicons. The first one is “Sentiment Word Ontology Library” (denoted as SWOL)<sup>11</sup>, which was constructed by first extracting candidate sentiment words from various thesauruses and then manually specifying the sentiment polarities of these words. The second one is “HowNet Sentiment Analysis Word Library”<sup>12</sup> (denoted as HowNetSenti), a widely used Chinese sentiment lexicon. The third one is called “NTU Sentiment Dictionary” (denoted as NTUSD)<sup>13</sup> , which is another popular Chinese sentiment lexicon. These three sentiment lexicons are all traditional sentiment lexicons for formal texts. Their detailed statistics are summarized in Table 3. We also compared our sentiment lexicon construction approach with two existing methods. The first one is proposed by Feng et al. in [15]. We denote it as Feng. The words’ sentiment scores in their method were specified using their associations with emoticons, and these associations were refined using microblogging search engines. However, new words were not considered in this method. The second one is proposed by Huang et al. in [14], where adjective new words were detected using manually designed patterns and their sentiment scores were also calculated based on their associations with emoticons. The new sentiment words were added to HowNetSenti sentiment lexicon to build the final sentiment lexicon. We denote this method as Huang. Besides, we also compared our method with two state-of-the-art sentiment lexicon construction methods. The first one is the label propagation method proposed by Rao and Ravichandran [23] (denoted as LP). The seed sentiment words used in their method are the sentiment words in SWOL. The sentiment similarity graph used in this method is the same with our method. The reason that we didn’t utilize Chinese thesaurus such as HowNet<sup>14</sup> to build sentiment similarity graph using synonym relations as [23] is that most of the new Chinese words are not covered by these thesauruses. The second one is graph propagation method proposed by Velikovich et al. [19] (denoted as GP). The seed sentiment words and the sentiment similarity graph used in this method are the same with previous method. The performances of different sentiment lexicons and sentiment lexicon construction methods are shown in Table 5.

Performance of different sentiment lexicons and sentiment lexicon construction methods.

<table><tr><td rowspan="2">Lexicon</td><td colspan="2">Subjectivity classification</td><td colspan="2">Polarity classification</td></tr><tr><td>EvaData1</td><td>EvaData2</td><td>EvaData1</td><td>EvaData2</td></tr><tr><td>SWOL</td><td>0.5139</td><td>0.4585</td><td>0.4442</td><td>0.3611</td></tr><tr><td>HowNetSenti</td><td>0.5545</td><td>0.5378</td><td>0.4796</td><td>0.4771</td></tr><tr><td>NUTSD</td><td>0.5160</td><td>0.5277</td><td>0.4482</td><td>0.5161</td></tr><tr><td>Feng</td><td>0.5438</td><td>0.5756</td><td>0.5636</td><td>0.6996</td></tr><tr><td>Huang</td><td>0.5602</td><td>0.5619</td><td>0.5111</td><td>0.5553</td></tr><tr><td>LP</td><td>0.5484</td><td>0.5667</td><td>0.5641</td><td>0.7143</td></tr><tr><td>GP</td><td>0.5612</td><td>0.5876</td><td>0.5682</td><td>0.7348</td></tr><tr><td>Ours</td><td>0.5732</td><td>0.6210</td><td>0.5804</td><td>0.8229</td></tr></table>

From Table 5, our sentiment lexicon achieves the best perfor mance in both microblog subjectivity detection and sentiment polarity classification on both datasets. It significantly outperforms traditional sentiment lexicons, such as SWOL, HowNetSenti, and NTUSD. This is because our microblog-specific sentiment lexicon contains a large number of popular user-invented sentiment words, such as “ ” (sad), “ ” (baby), and “ ” (cute). These new sentiment words are very common in microblog messages and convey strong sentiments, but they are not included in traditional sentiment lexicons. In addition, when used in microblog messages, the sentiments of many formal words are different from their original sentiments in traditional sentiment lexicons. For example, $" \equiv 4 �atop - 1 1 )$ (wool) is a neutral word in traditional sentiment lexicons. But it is usually used as a negative word in microblogs to express disagreement. Another example $\mathrm { i } s \ \stackrel { \scriptscriptstyle { w } } { \scriptscriptstyle { \mathrm { L } } } \ne \ddagger { \scriptscriptstyle { \frac { \scriptscriptstyle { w } } { \scriptscriptstyle { \mathrm { L } } } } } \ '$ (shy), which is recognized as a negative word in NTUSD. However, it is frequently used as a positive word to express happiness and enjoyment in social media. Our sentiment lexicon construction method can successfully recognize the correct sentiment polarities of these words and incorporate them into our microblog-specific sentiment lexicon. Thus our sentiment lexicon is more suitable for microblog sentiment analysis than traditiona sentiment lexicons. The superior performance of our sentiment lexicon compared with Feng’s method [15] shows that detecting the new words used in microblogs and identifying their sentiment polarities are beneficial for analyzing the sentiments of microblogs. Our sentiment lexicon also outperforms Huang’s method [14] because our method can find new words belonging to all syntactic classes while their method can only detect the adjective new words. Many new words with strong sentiments are not limited to be adjective. For example, “ ” (baby) and $" \overrightarrow { \mathcal { X } } _ { \mathrm { { \ell } } } \overrightarrow { \mathbb { H } } ^ { \prime \prime }$ (try to be cute) are both new sentiment words, but they are noun and verb respectively. In addi tion, in their method, the sentiments of formal words are extracted from HowNetSenti sentiment lexicon directly which are not suitable for microblog sentiment analysis. Our sentiment lexicon construction method also outperforms the two state-of-the-art methods compared here, i.e., LP and GP. This is because our approach can incorporate various types of sentiment knowledge into a unified framework for sentiment lexicon construction, such as the word sentiment knowledge extracted from the microblogs with emoticons However, in IP [23] and GP [19] this sentiment knowledge is not considered.

In order to explore the contributions of different kinds of sentiment knowledge to the performance improvement of our microblog-specific sentiment lexicon, we built different sentiment lexicons using different combinations of sentiment knowledge. The experimental results on EvaData1 are shown in Fig. 2 and the pattern on EvaData2 is similar. Fig. 2 shows that although the prior sentiment knowledge, i.e., the traditional sentiment lexicon SWOL, has a poor performance on microblog sentiment analysis, combining it with the word-sentiment knowledge extracted from messages with emoticons can consistently improve the performance of our sentiment lexicon. This is mainly because emoticons are noisy sentiment labels and the word-sentiment knowledge extracted from them is not 100% accurate. At the same time, many formal sentiment words do not change their sentiments when used in microblogs. Thus the prior sentiment knowledge extracted from traditional sentiment lexicons can provide useful supplementary information to refine the sentiment scores in word-sentiment knowledge. For example, $\because \angle B , C , \angle C ,$ (kind-hearted people) is a positive word in both traditional texts and microblog messages. However, in microblog messages it is frequently used in scenarios where the message authors come into dificulties and need someone’s help. For example, a microblog message may be “ $1 2 ^ { \circ } \# \Re \not \equiv 1 1 \hbar \gamma$ (Lost my purse. Hope some kind-hearted people can help find it. [Crying]). Thus, the word $\because \angle B E \cdot \angle C , \angle C \cdot \angle \cdot$ frequently co-occurs with negative emoticons and has a negative score in word-sentiment knowledge. However, since $\because \angle B E \cdot \angle C , \Lambda ^ { \prime \prime }$ is labeled as a positive word in SWOL, this prior knowledge can help refine the polarity of this word in the final sentiment lexicon. In addition, the experimental results in Fig. 2 show that combining the sentiment similarity knowledge can also help improve the performance of our microblog-specific sentiment lexicon. It indicates that the sentiment similarity knowledge can provide useful information for refining the word-sentiment knowledge extracted from emoticons. For example, $\because \angle B A C , \angle C , A C$ (kind-hearted people) frequently co-occurs with $\bullet _ { \mathcal { H } _ { \mathbb { H } } } \mathfrak { L } _ { \mathbb { H } } \mathfrak { n }$ (hope), $" \frac { 2 } { 1 0 } \frac { 1 3 } { 1 2 } " \frac { 2 } { 2 } "$ (help), and $\cdots \operatorname { \mathbb { H } } \mathrm { \# } \mathrm { \# } \mathrm { \# } \mathrm { \# } \mathrm { \# }$ (thanks), which are all highly positive words. Since a word’s sentiment polarity is usually similar to the sentiment polarities of the words it closely accompanies [17], we can infer from the sentiment similarity knowledge that $\cdot \cdot \angle 7 = 9 0 ^ { \circ }$ is also a positive word. Another important observation from Fig. 2 is that combining all the three kinds of sentiment knowledge can further improve the performance of our microblog-specific sentiment lexicon, indicating that different kinds of sentiment knowledge can collaborate with each other under our unified framework.

![](/api/attachments/CW5EZP2F/fulltext/images/e036a7d4de5456ee44e37e96533bce5180e3853de8f32e6e481d3e0355a3ee81.jpg)  
Fig. 2. The performance of our sentiment lexicon with different kinds of sentiment knowledge. “Score” represents the word-sentiment knowledge. “Sim” stands for sentiment similarity knowledge. “Prior” means the prior sentiment knowledge. “All” represents that all the three kinds of knowledge are incorporated into our sentiment lexicon.

## 5.4. Parameter analysis

In this section we conducted experiments to explore the influence of parameters on the performance of our microblog-specific sentiment lexicon. The most important parameters in our model of sentiment lexicon construction (Eq. (8)) are $\alpha , \beta ,$ and k. a and $\beta$ are used to control the relative importance of sentiment similarity knowledge and prior sentiment knowledge respectively. k is used to control the penalty introduced by the $L _ { 1 } { \mathrm { - } } \mathrm { n o r m }$ of the model parameters, which influences the number of sentiment words in the final sentiment lexicon.

![](/api/attachments/CW5EZP2F/fulltext/images/1125cfbaf62cc3afa8fa8c3e55bbf717ba3422f01110c05b531346adbdb6b668.jpg)  
Fig. 3. The performance of our microblog-specific sentiment lexicon with different values of a.

Fig. 3 shows the influence of a on the performance of our sentiment lexicon on EvaData1. The patterns on EvaData2 are similar. From Fig. 3, we can see that the value of a has a high influence on sentiment polarity classification performance of our sentiment lexicon. However, the influence of a on subjectivity detection performance is minor. This result indicates that sentiment similarity knowledge is more useful in refining sentiment polarity labels of sentiment words rather than changing their subjectivity labels. When the value of a increases from 0, the performance of our sentiment lexicon on sentiment polarity classification first increases, then reaches the peak, and decreases afterwards. This is because when the value of a is too small, the information in sentiment similarity knowledge is not fully used. But since the sentiment similarities contain noise, if the value of a is too big, the information in sentiment similarities is overemphasized and the performance will be hurt. Moderate values of $\alpha ,$ such as values ranging from 0.15 to 0.5, are most suitable for our model. pt

Fig. 4 shows the influence of $\beta$ on the performance of our sentiment lexicon on EvaData1. The results on EvaData2 show the similar patterns. From Fig 4, the value of $\dot { \boldsymbol { \beta } }$ has clear influence on both subjectivity detection and sentiment polarity classification. It implies that prior sentiment knowledge extracted from existing sentiment lexicons can change both the subjectivity labels and sentiment polarity labels of candidate sentiment words. Fig. 4 shows that when the value of $\beta \ \mathrm { i } s \ 0 ,$ the prior sentiment knowledge in traditional sentiment lexicon is not used, and the performance is not optimal. The performance improves as b increases from 0. However, when $\beta$ is too big, the sentiment polarities of formal sentiment words are mainly decided by traditional sentiment lexicon, which is unsuitable for microblog sentiment analysis since many formal sentiment words convey different sentiment polarities and intensities when used in microblogging scenario. Thus the performance decreases when b gets too big.

![](/api/attachments/CW5EZP2F/fulltext/images/c9048d6df771e664ee87462e1926d89c7278237ccbb4f25db2df5ecfc6205e43.jpg)  
Fig. 4. The performance of our microblog-specific sentiment lexicon with different values of b.

![](/api/attachments/CW5EZP2F/fulltext/images/41964a64c12d5edaf7373abdb084890187fda600444f8f86ba4fbd3faad039c4.jpg)  
(a) Influence of λ on subjectivity detection.

![](/api/attachments/CW5EZP2F/fulltext/images/c01b6d7d19ed1c0645b65640948f1406f3697271eb31944789fffef25bb2d735.jpg)  
(b) Influence of $\lambda$ on sentiment polarity classification.

![](/api/attachments/CW5EZP2F/fulltext/images/639903f869c64a8de7d519f17c6de698d36793ea70e21f0b4085c4a96b798eef.jpg)  
(c) Influence of λ on sentiment lexicon size.  
Fig. 5. Comparison of our sentiment lexicon with different k values. In (a), P\_Sub and R\_Sub are the precision and recall of subjective category respectively. P\_Obj and R\_Obj are the precision and recall of objective category respectively. Fscore is the macro-average Fscore. In (b), Precision, Recall, and Fscore represent the macro-averaged precision, recall and Fscore on sentiment polarity classification respectively.

Fig. 5 (a) and Fig. 5 (b) show the influence of k on the performance of our microblog-specific sentiment lexicon on subjectivity detection and sentiment polarity classification on EvaData2 respectively. The patterns on EvaData1 are similar. From Fig. 5 (a), as the value of k increases from 0, the Fscore of our sentiment lexicon on subjectivity detection first increases, then decreases. This is because the value of k can influence the number of sentiment words in our sentiment lexicon, as shown in Fig. 5 (c). Small k results in too many words in our sentiment lexicon, many of which are objective words. It leads to that many objective messages are misclassified to be subjective, and the recall of objective category in subjectivity detection is quite low. When k increases from a small value, the recall of objective category increases significantly. Thus the overall performance, i.e., Fscore, increases. However, when k gets too big, many sentiment words are misclassified to be objective and filtered from the sentiment lexicon. It leads to that many subjective messages are not correctly detected. Thus the recall of subjective category as well as the overall performance decreases. As to sentiment polarity classification, according to Fig. 5 (b), when k increases, the average precision increases slowly. The average recall first keeps steady then decreases quickly, because many messages with sentiment polarities are misclassified to be objective due to the coverage of the sentiment lexicon becomes very small when k gets very big. Thus the overall performance of sentiment polarity classification first increases slowly then decreases quickly.

## 6. Conclusion

Microblogging users frequently express their opinions towards companies, brands and products by posting microblogs. Sentiment analysis systems can automatically analyze and summarize the sentiment information in these massive opinion-rich messages and provide useful knowledge to companies and customers when making business-related decisions. An accurate and comprehensive microblog-specific sentiment lexicon can significantly improve the performance of sentiment analysis systems in analyzing the sentiments of microblogs. In this paper we propose a datadriven approach to build a high-quality microblog-specific Chinese sentiment lexicon. Specifically, we propose a unified framework that integrates three types of sentiment knowledge extracted from massive microblogs and existing sentiment lexicons for microblogspecific sentiment lexicon construction. Since many popular sentiment words used in microblogs are user-invented new words and not covered by existing dictionaries, in order to improve the coverage of our sentiment lexicon, we propose a data-driven method for microblog new word detection, which utilizes both words’ distributions over texts and their distributions over users.

We build our microblog-specific Chinese sentiment lexicon on a large microblog dataset with more than 17 million microblog messages. Our sentiment lexicon contains both formal sentiment words and popular user-invented sentiment words. We conduct extensive experiments to evaluate its performance on two Chinese microblog sentiment datasets. Experimental results show that our sentiment lexicon can significantly improve the performance of microblog sentiment analysis tasks, such as subjectivity detection and sentiment polarity classification.

In our future work, we plan to build an accurate microblog sentiment analysis system based on our microblog-specific sentiment lexicon, and use it to extract market intelligence from massive opinion-rich microblogs for companies to improve their products and services, conduct more effective social advertising, design better market strategies and so on. In addition, it can provide customers useful information to make more informed decisions on whether purchasing a product or service.

## Acknowledgments

This research is supported by the Key Program of National Natural Science Foundation of China (Grant nos. U1536201 and U1405254), National Natural Science Foundation of China (Grant no. 61472092) and the Initiative Scientific Research Program of Tsinghua University.

## References

[1] F. Wu, Y. Song, Y. Huang, Microblog sentiment classification with contextual knowledge regularization, Proceedings of the Twenty-Ninth AAAI Conference on Artificial Intelligence, 2015. pp. 2332–2338.

[2] Y.-M. Li, T.-Y. Li, Deriving market intelligence from microblogs, Decision Support Systems 55 (1) (2013) 206–217.

[3] A. Hogenboom, B. Heerschop, F. Frasincar, U. Kaymak, F. de Jong, Multi-lingual support for lexicon-based sentiment analysis guided by semantics, Decision Support Systems 62 (2014) 43–53.

[4] M. Salehan, D.J. Kim, Predicting the performance of online consumer reviews: a sentiment mining approach to big data analytics, Decision Support Systems 81 (2016) 30–40.

[5] F. Wu, Y. Huang, Y. Song, Structured microblog sentiment classification via social context regularization, Neurocomputing 175 (2016) 599–609.

[6] R.Y. Lau, C. Li, S.S. Liao, Social analytics: learning fuzzy product ontologies for aspect-oriented sentiment analysis, Decision Support Systems 65 (2014) 80–94.

[7] F.H. Khan, S. Bashir, U. Qamar, TOM: Twitter opinion mining framework using hybrid classification scheme, Decision Support Systems 57 (2014) 245–257.

[8] A. Esuli, F. Sebastiani, Sentiwordnet: a publicly available lexical resource for opinion mining, Proceedings of the Third International Conference on Language Resources and Evaluation, 2006. pp. 417–422.

[9] B. Pang, L. Lee, Opinion mining and sentiment analysis, Foundations and Trends in Information Retrieval 2 (1-2) (2008) 1–135.

[10] B. Liu, Sentiment analysis and opinion mining, Synthesis Lectures on Human Language Technologies 5 (1) (2012) 1–167.

[11] G. Wang, J. Sun, J. Ma, K. Xu, J. Gu, Sentiment classification: the contribution of ensemble learning, Decision Support Systems 57 (2014) 77–93.

[12] D. Tang, F. Wei, B. Qin, M. Zhou, T. Liu, Building large-scale Twitter-specific sentiment lexicon: a representation learning approach, Proceedings of the 25th International Conference on Computational Linguistics, 2014. pp. 172–182.

[13] S. Kiritchenko, X. Zhu, S.M. Mohammad, Sentiment analysis of short informal texts, Journal of Artificial Intelligence Research 50 (2014) 723–762

[14] M. Huang, B. Ye, Y. Wang, H. Chen, J. Cheng, X. Zhu, New word detection for sentiment analysis, Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics, 2014. pp. 531–541.

[15] S. Feng, L. Wang, W. Xu, D. Wang, G. Yu, Unsupervised learning Chinese sentiment lexicon from massive microblog data, Advanced Data Mining and Applications, Springer 2012, pp. 27–38.

[16] S.R. Das, M.Y. Chen, Yahoo! for Amazon: sentiment extraction from small talk on the web, Management Science 53 (9) (2007) 1375–1388.

[17] P.D. Turney, Thumbs up or thumbs down?: semantic orientation applied to unsupervised classification of reviews, Proceedings of the 40th Annual Meeting on Association for Computational Linguistics, 2002. pp. 417–424.

[18] M. Hu, B. Liu, Mining and summarizing customer reviews, Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM 2004, pp. 168–177.

[19] L. Velikovich, S. Blair-Goldensohn, K. Hannan, R. McDonald, The viability of web-derived polarity lexicons, HLT ’10 Human Language Technologies: The 2010 Annual Conference of the North American Chapter of the Association for Computational Linguistics, 2010. pp. 777–785.

[20] F. Li, S.J. Pan, O. Jin, Q. Yang, X. Zhu, Cross-domain co-extraction of sentiment and topic lexicons, Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics: Long Papers, vol. 1, 2012. pp. 410–419.

[21] J. Steinberger, M. Ebrahim, M. Ehrmann, A. Hurriyetoglu, M. Kabadjov, P. Lenkova, R. Steinberger, H. Tanev, S. VáZquez, V. Zavarella, Creating Sentiment Dictionaries via Triangulation, Decision Support Systems 53 (4) (2012) 689–694.

[22] J. Wiebe, Learning subjective adjectives from corpora, Proceedings of the Seventeenth National Conference on Artificial Intelligence and Twelfth Conference on Innovative Applications of Artificial Intelligence, AAAI Press 2000, pp. 735–740.

[23] D. Rao, D. Ravichandran, Semi-supervised polarity lexicon induction, Proceedings of the 12th Conference of the European Chapter of the Association for Computational Linguistics, 2009. pp. 675–682.

[24] S. Baccianella, A. Esuli, F. Sebastiani, SentiWordNet 3.0: an enhanced lexical resource for sentiment analysis and opinion mining., Proceedings of the Seventh International Conference on Language Resources and Evaluation, 10, 2010. pp. 2200–2204.

[25] R. Sproat, T. Emerson, The first international Chinese word segmentation bakeoff, Proceedings of the Second SIGHAN workshop on Chinese Language Processing, vol. 17, 2003. pp. 133–143.

[26] X. Sun, H. Wang, W. Li, Fast online training with frequency-adaptive learning rates for chinese word segmentation and new word detection, Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics: Long Papers — Volume 1, 2012. pp. 253–262

[27] J.S. Justeson, S.M. Katz, Technical terminology: some linguistic properties and an algorithm for identification in text, Natural Language Engineering 1 (01) (1995) 9–27.

[28] K.-J. Chen, W.-Y. Ma, Unknown word extraction for Chinese documents, Proceedings of the 19th International Conference on Computational Linguistics-Volume 1, 2002. pp. 1–7.

[29] H. Li, C.-N. Huang, J. Gao, X. Fan, The use of SVM for Chinese new word identification, Proceedings of the First International Joint Conference on Natural Language Processing, Springer-Verlag 2005, pp. 723–732.

[30] K.W. Church P. Hanks Word association norms mutual information and lexicography ComputationalLinguistics 16 (1) (1990) 22-29

[31] T. Dunning, Accurate methods for the statistics of surprise and coincidence, Computational Linguistics 19 (1) (1993) 61–74.

[32] W. Zhang, T. Yoshida, X. Tang, T.-B. Ho, Improving effectiveness of mutual information for substantival multiword expression extraction, Expert Systems with Applications 36 (8) (2009) 10919–10930.

[33] F. Bu, X. Zhu, M. Li, Measuring the non-compositionality of multiword expressions, Proceedings of the 23rd International Conference on Computationa Linguistics, 2010. pp. 116–124

[34] A. Devitt, K. Ahmad, Sentiment polarity identification in financial news: a cohesion-based approach, Proceedings of the 45th Annual Meeting of the Association of Computational Linguistics, 2007. pp. 984–991.

[35] R. Tibshirani, Regression shrinkage and selection via the lasso, Journal of the Royal Statistical Society. Series B (Methodological) (1996) 267–288.

[36] S. Boyd, L. Vandenberghe, Convex Optimization, Cambridge University Press 2009.

[37] A. Beck, M. Teboulle, A fast iterative shrinkage-thresholding algorithm for linear inverse problems, SIAM Journal on Imaging Sciences 2 (1) (2009) 183–202.

![](/api/attachments/CW5EZP2F/fulltext/images/0ae69dd77fdcd1c0702171f31dcc790870ea327f92a281c122fd88e605c72551.jpg)  
Fangzhao Wu received the B.E. degree in Electronic Engi neering from Tsinghua University in 2012. He is currently working towards the PhD degree in the Department of Electronic Engineering at Tsinghua University, Beijing, China. His research interests include machine learning text mining and social network analysis.

![](/api/attachments/CW5EZP2F/fulltext/images/52ef4941ebc8be2a3ed5475dc71de6c14b35a912f471653f58b66bf29a355ce5.jpg)

Yongfeng Huang is a Professor in the Department of Electronic Engineering, Tsinghua University, China. He received the PhD degree in computer science and engineering from Huazhong University of Science and Technology in 2000. His research interests include next generation Internet and Web data mining.

![](/api/attachments/CW5EZP2F/fulltext/images/92f57a103d95f92e2c4254a18f113c0dd59cbaa2482ff9d7528da227e54652ff.jpg)

Yangqiu Song is an assistant professor at West Virginia University, USA. He received his B.E. and PH.D. degree from Tsinghua University, China. His research interest i using machine learning and data mining techniques to extract and infer insightful knowledge from big data.

![](/api/attachments/CW5EZP2F/fulltext/images/8d5260f9b5292e198e7984802f9319553ea3cbf55be85e2ddf3fd8c98369536d.jpg)

Shixia Liu received the BS and MS degrees in computa tional mathematics from the Harbin Institute of Technol ogy, the PhD degree in computer science from Tsinghua University. She is an associate professor at Tsinghua Uni versity. Her research interests include visual text analyt ics, visual social analytics, and graph visualization.
