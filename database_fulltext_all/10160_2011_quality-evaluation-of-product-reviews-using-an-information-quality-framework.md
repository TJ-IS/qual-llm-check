---
otero_id: 10160
otero_key: "M9692CHG"
title: "Quality evaluation of product reviews using an information quality framework"
authors: "Chien Chin Chen; You-De Tseng"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.023"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Quality evaluation of product reviews using an information quality framework

Chien Chin Chen ⁎, You-De Tseng

Department of Information Management, National Taiwan University, No. 1, Sec. 4, Roosevelt Road, Taipei, 10617 Taiwan, ROC

a r t i c l e i n f o

Available online 27 August 2010

Keywords: Text mining Classi<sup>fi</sup>cation Opinion mining Opinion retrieval

## a b s t r a c t

The ubiquity of Web2.0 makes the Web an invaluable source of business information. For instance, product reviews composed collaboratively by many independent Internet reviewers can help consumers make purchase decisions and enable enterprises to improve their business strategies. As the number of reviews is increasing exponentially, opinion mining and retrieval techniques are needed to identify important reviews and opinions to answer users' queries. Most opinion mining and retrieval approaches try to extract sentimental or bipolar expressions from a large volume of reviews. However, the process often ignores the quality of each review and may retrieve useless or even noisy documents. In this paper, we propose a method for evaluating the quality of information in product reviews. We treat the evaluation of review quality as a classi<sup>fi</sup>cation problem and employ an effective information quality framework to extract representative review features. Experiments based on an expert-composed data corpus demonstrate that the proposed method outperforms state-of-the-art approaches signi<sup>fi</sup>cantly.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

When making customer-related decisions, business managers frequently ask questions like “How do people feel?” “What opinions do people have?” To answer such questions, enterprises usually need to conduct laborious surveys in order to gather enough opinions for analysis. However, with the advent of Web2.0, many online collaborative tools, e.g., weblogs and discussion forums, are being developed to allow Internet users to express opinions and share valuable knowledge. One consequence is that the Web has become an invaluable source of information for business enterprises. Roed [25] observes that Internet users are often willing to divulge personal information and are forthcoming in presenting their personal viewpoints honestly. This kind of behavior has an indirect word-of-mouth<sup>1</sup> effect on marketing because users' opinions posted on the Web have a huge impact on consumer decisions [3]. Many e-commerce companies and websites, such as Amazon,<sup>2</sup> are aware of the word-of-mouth effect and offer users a platform to post their product reviews. However, as the number of reviews is growing exponentially, companies and customers are <sup>fi</sup>nding it increasingly dif<sup>fi</sup>cult to <sup>fi</sup>nd desired information. To alleviate this information overload problem, opinion mining and retrieval techniques [5,11,15,20,24] have been devised to extract and retrieve meaningful opinions from reviews.

A major task of opinion mining and retrieval involves identifying sentimental (or bipolar) text units in review documents. A text unit can be a word, a sentence, a paragraph, or even the whole document, depending on the granularity of opinion mining and retrieval. While many opinion mining and retrieval approaches try to identify and analyze opinions extracted from reviews, comparatively few works consider the quality of reviews. As Web2.0 encourages knowledge sharing, there are no constraints on review writing; hence, the quality of reviews varies enormously. For example, many reviews posted on Amazon simply contain emotional expressions, such as “I just don't like this camera.” Since such reviews lack constructive expressions, they should not be included in the opinion mining and retrieval process. Some websites do consider the quality of reviews, and provide a review quality evaluation mechanism that ranks reviews based on votes submitted by readers. Fig. 1 shows a review quality evaluation on Amazon, where 121 out of 128 users thought the review was helpful. However, even under a voting mechanism, the quality evaluations are still affected by imbalanced vote bias, winner circle bias, and early bird bias, which make the system impracticable [21]. Thus, there is an urgent need for effective quality evaluation mechanisms to help opinion mining and retrieval algorithms identify informative reviews.

In this paper, we propose a method for evaluating the quality of information in product reviews. We treat the quality evaluation of product reviews as a classi<sup>fi</sup>cation problem and employ a multiclass support vector machine (multiclass SVM) [31] model to categorize reviews. In addition, we adopt a mature information quality (IQ) framework, which has been widely used in many domains over the last twenty years, to de<sup>fi</sup>ne review features for classi<sup>fi</sup>cation. Rowley and Hartley [26] de<sup>fi</sup>ne raw data as unprocessed observations,

121 of 128 people found the following review helpful:

Beautiful camera with one major shortcoming,March 29, 2008

By JOHN F. HuDsON "gardener" (Rockville, Maryland) - See all my reviews REAL NAME

![](/api/attachments/M9692CHG/fulltext/images/a74fb8ad2d6d93756661de89a014d69bff9ca8736793c4c61ef30db31bc7eed1.jpg)

I was attracted to this camera as a new version of the A460, which was highly rated by PC World It is indeed very simple to use with a large LCD display, much greater resolution than the A70 I bought five vears ago, and uses a 2 GB memory chip. The drawback is that the camera has no view finder. You take a picture by looking at it in the LCD display. That works fine indoors, but outdoors the daylight washes out the display so that framing a picture is almost quesswork.Canon PowerShot A470 7MP Digital Camera with 3.4x Optical Zoom (Red)

Fig. 1. A review quality evaluation on Amazon.

whereas information is structured and organized data. Thus, information is valuable for a speci<sup>fi</sup>c purpose or application. In addition to raw textual units (i.e., unigrams), the proposed IQ features can comprehend opinions and polarity information embedded in review content; hence, the feature set is information-oriented. A review retrieval system based on the proposed method is also implemented. The system ranks a review according to the quality of the information it contains as well as the content's relevance to a user query. We hypothesize that the proposed IQ-based features are effective in classifying review quality, and review retrieval systems that incorporate the proposed classi<sup>fi</sup>cation model could retrieve informative and query-relevant reviews. We conduct various experiments based an expert-composed data corpus to validate the hypotheses. The results demonstrate that the proposed method outperforms state-of-the-art review quality evaluation approaches signi<sup>fi</sup>cantly and the reviews retrieved by the proposed retrieval system are query-relevant and informative. In addition, the learned model helps identify the factors that are critical for compiling high-quality reviews.

The remainder of this paper is organized as follows. Section 2 contains a review of related works. In Section 3, we introduce the information quality framework and apply it to the problem of review quality classi<sup>fi</sup>cation. We present the review retrieval system in Section 4 and evaluate the system performance in Section 5. Then, in Section 6, we summarize our conclusions.

## 2. Related work

In this section, we consider a number of review quality evaluation, information quality, opinion retrieval, and opinion mining approaches.

## 2.1. Review quality evaluation

Most review quality evaluation approaches adopt sets of review features to evaluate the quality of reviews. However, many adopted feature sets are lexical or syntactically oriented, so they hardly re<sup>fl</sup>ect the diverse characteristics of reviews. Zhang and Varadarajan [34] and Kim et al. [16] measure the quality of a review in terms of the helpfulness votes submitted by readers. The quality of a review is high if it receives many helpfulness votes. Zhang and Varadarajan collected a set of product reviews posted on Amazon along with the corresponding helpfulness votes given by readers. Based on the votes, the authors quanti<sup>fi</sup>ed the quality of a review as the ratio of helpfulness votes submitted by readers and employed SVM regression to approximate the quality of the reviews. The resulting regression function was then used to estimate the quality of new reviews. The reported experiment results show that the shallow syntactic features, e.g., the counts of proper nouns, modal verbs, and comparative adjectives in a review, are highly correlated with review quality estimation. Kim et al. also employed SVM regression to predict the helpfulness vote ratio of a review, and used <sup>fi</sup>ve categories of review features, namely, structural, lexical, syntactical, semantic, and metadata features, to construct a regression function. They found that the lexical features, i.e., the unigrams of a review, together with review's length and product rating have a signi<sup>fi</sup>cant impact on users assessments of the review's quality.

Liu et al. [21] conducted a detailed survey of reviews posted on Amazon and found that users' votes were in<sup>fl</sup>uenced by three types of bias: imbalanced vote bias, winner circle bias, and early bird bias. The imbalanced vote bias means that Internet users tend to rate others' opinions positively rather than negatively. The winner circle bias indicates that reviews awarded a lot of helpfulness votes will continue to attract many votes. This is because the reviews are top ranked, so they are easily accessed by Internet users. The early bird bias suggests that the earlier a review is posted, the more votes it will receive. Because of these biases, the methods [16,34] that employ users' votes as training examples are unreliable. Rather than making quality evaluations based on biased votes, Liu et al. treat review quality evaluation as a classi<sup>fi</sup>cation problem. They also use an expertcomposed data set to train an unbiased SVM classi<sup>fi</sup>er, which then categorizes reviews as either high-quality or low-quality.

In this paper, we adopt an effective framework for assessing the quality of information. It considers various aspects of reviews to derive information-oriented features for evaluating the quality of the reviews. Using information-oriented features improves the evaluation performance, and resolves important issues related to the composition of informative reviews.

## 2.2. Information quality

The objective of information quality (IQ) research (also known as data quality research) is to determine the characteristics of information items that are important to, or suitable for information consumers [30]. Over the past decade, many IQ studies were developed to assess the information quality of various information technologies [1]. Most IQ studies consider information quality as a multi-dimensional framework in which each dimension represents a single aspect or construct of information items and is described by a set of features [17]. Zhu and Gauch [35] assessed the information quality of a Web page in terms of an IQ framework comprised of six quality dimensions, namely, currency, availability, information-tonoise ratio, authority, popularity, and cohesiveness. The authors measure the dimensions through the properties of Web pages and combine the measures linearly to calculate the quality score of a Web page. The reported experiment results show that the precision of Web searches is increased signi<sup>fi</sup>cantly by incorporating the framework into an information system. Hence, quality evaluation of Web pages is important for Web search engines. Chae and Kim [2] proposed an IQ framework for assessing the information quality of a mobile Internet service. The framework consists of four dimensions, namely, connection quality, content quality, interaction quality, and contextual quality. The authors conducted a large-scale survey to examine the effectiveness of the dimensions and found that all the dimensions help increase customer satisfaction and loyalty. However, the relative weights of the dimensions depend to a large extent on the customer's goals. Therefore, to provide better mobile services, service providers need to distinguish the goals of their consumers. Knight and Burn [17] proposed a methodology for developing a quality-based information system. The method <sup>fi</sup>rst identi<sup>fi</sup>es domain users, environments, and tasks in order to select appropriate IQ dimensions from the established IQ research literature. Next, the selected dimensions are prioritized in terms of cost, urgency, and importance to exclude less effective dimensions. Finally, the prioritized dimensions are incorporated in an information retrieval (IR) model to provide users with quality-based information retrieval. Moreover, to improve the performance of the system continuously, feedback from users and the system is analyzed periodically to adjust the prioritized IQ dimensions. Burgess et al. [1] also investigated the effectiveness of IQ frameworks on information searching. The authors suggest that IQ frameworks should be personalized because users have different perceptions of information quality. They therefore proposed a <sup>fl</sup>exible model that enables users to create and weight their own IQ dimensions and features. However, as the de<sup>fi</sup>nition of information quality (i.e., <sup>fi</sup>tness for use) is conceptual and vague, quantifying IQ dimensions and features is dif<sup>fi</sup>cult and errorprone for ordinary users.

Although a large number of studies have examined the effectiveness of IQ frameworks on various information technologies, to the best of our knowledge, no IQ framework has been developed for Internet product reviews. In this study, we employ a generic IQ framework, which has achieved superior performances in various application domains, to derive appropriate IQ features for review quality. We believe that by using the framework and the features the information overload problem of Internet product reviews can be alleviated effectively.

## 2.3. Opinion retrieval

Opinion retrieval was introduced as a special track at TREC 2006<sup>3</sup> and has since become an important research topic. The goal of the research is to develop effective retrieval systems that select blog entries containing opinions relevant to topical queries. Generally, opinion retrieval methods integrate opinion mining techniques into IR models to rank blog entries containing opinions. Zhang et al. [33] proposed a three-phase opinion retrieval method. Given a user query, the <sup>fi</sup>rst phase computes the content similarity between the query and every blog entry in terms of the Okapi BM-25 IR model [14]. Next, an SVM-based opinion classi<sup>fi</sup>er is employed to derive a score that indicates the opinion degree of an entry. Then, in the third phase, the similarity and the opinion score are combined linearly to rank the entry. Zhang and Ye [32] derived an opinion retrieval model by incorporating a sentiment constraint into a probabilistic IR framework. The model ranks an entry by quadratically combining the entry's opinion score with its content similarity to a user query. Topranked entries are then returned in response to the query. He et al. [9] proposed a dictionary-based opinion retrieval model that constructs an opinion dictionary from a set of blog entries, where each term has an opinion weight. To compute an opinion score for a blog entry, the top weighted terms are regarded as a query, and the score indicates the content similarity between the query and the entry. Similar to other opinion retrieval models, the opinion score is combined with a query-relevance score computed by an IR model to rank the entry. However, the authors demonstrated through experiments that logarithmic combinations generally outperform linear combinations.

## 2.4. Opinion mining

Opinion extraction and polarity identi<sup>fi</sup>cation are the major tasks in opinion mining. Depending on the granularity of the opinion mining approach, an opinion can be a word, a sentence, a paragraph, or even a complete review document. Most approaches rely on a humancomposed opinion lexicon. Turney [29] used seven positive and seven negative words as an opinion dictionary and proposed using pointwise mutual information (PMI) to calculate the degree of co-occurrence of a word with the words in the lexicon. A word has a positive orientation if it tends to co-occur with the positive words; otherwise, it has a negative orientation. Dave et al.'s approach [5] uses IR techniques to extract sentiment n-gram features from a set of positive and negative product reviews. Then, based on the features, classi<sup>fi</sup>cation algorithms are employed to extract and classify sentiments or opinions in new reviews. Ku et al. [18] dealt with Chinese opinion mining problems in a bottomup manner. To identify the polarity of a Chinese article, the authors translated the General Inquirer<sup>4</sup> opinion lexicon and combined the translations with the Chinese Network Sentimental Dictionary.<sup>5</sup> As the meaning of a Chinese word is generally made up of individual Chinese characters, the aggregated opinion lexicon determines the polarity of the characters and, by extension, the polarity of Chinese words, sentences, and documents. Hu and Liu [11] observed that opinion sentences usually contain sentiment adjectives; thus, their opinion lexicon contained a set of such adjectives. The authors used WordNet [8,23] to identify new sentiment adjectives found in reviews. The discovered adjectives were then added to the lexicon to expand it recursively. They also extracted sentences containing sentiment adjectives to compose opinion summaries of reviews. Kim and Hovy [15] also used WordNet to expand a human-composed opinion lexicon. To determine a word's polarity, the word is represented by a set of synonyms de<sup>fi</sup>ned by WordNet. Then, a Naive Bayes classi<sup>fi</sup>er is used to assign the polarity of the word. This method also identi<sup>fi</sup>es opinion holders by selecting name entities close to topic phrases in opinion sentences. In practice, opinion words are often context dependent and can belong to any part-of-speech [6]. For example, the word ‘simple’ has a positive orientation in the sentence “The user interface of this PDA is simple.” However, it conveys a negative sentiment in “The story of this movie is too simple.” Ding et al. expanded Hu and Liu's opinion lexicon by adding opinion verbs and nouns, and also considered the context information in sentences for opinion mining. Their experiments demonstrated that the accuracy of opinion mining can be improved by using a holistic opinion lexicon.

## 3. Methods

## 3.1. Definition of review quality

We regard review quality evaluation as a classi<sup>fi</sup>cation problem and employ an information quality framework to derive informative review features for classi<sup>fi</sup>cation. Five classes of review quality, namely ‘high-quality,’ ‘medium-quality,’ ‘low-quality,’ ‘duplicate,’ and ‘spam,’ are de<sup>fi</sup>ned according to the speci<sup>fi</sup>cation of review quality proposed by Liu et al. [21] and the de<sup>fi</sup>nition of spam reviews suggested by Jindal and Liu [12]. A high-quality review must provide complete and timely information about a product; and it must contain a large number of opinions to help readers make purchasing decisions. The content of a medium-quality review is relevant to a product, but it is not informative enough. Although such reviews are interesting, they hardly persuade readers to make decisions. A low-quality review contains little information about a product, or the information is too objective to judge the value of the product. A review is considered a duplicate if its content is very similar to a review posted previously. It may be plagiarism or a repeat review posted by mistake. Finally, a spam review only provides comments about product-irrelevant matters, such as other brands and services; otherwise, it may be an advertisement or a question-answer type of review.

## 3.2. Information quality-based review features

To comprehend various aspects of reviews from the perspective of readers (i.e., information customer) for review quality evaluation, we treat a review as an information item and adopt an IQ framework for model building. Eppler and Wittig [7] surveyed twenty IQ research models and concluded that Wang and Strong's IQ framework [30] (see Table 1) is the only one that attempts to strike a balance between theoretical consistency and practicability. Subsequently, Eppler and Wittig posited that Wang and Strong's IQ framework is generic and widely applicable to various domains. Therefore, we adopt the framework in this study to derive informative review features. The structure of the framework is hierarchical, and it organizes IQ features along <sup>fi</sup>fteen dimensions to comprehend the following four major constructs of information quality: intrinsic quality, contextual quality, representational quality, and accessibility quality. In this research, some dimensions are not considered because they are not applicable to product reviews. We use following nine dimensions and <sup>fi</sup>fty-one features for multiclass SVM training and testing.

## ➢ Believability (D1)

This dimension is the extent to which an information item (i.e., a review) is credible, or regarded as true. Jindal and Liu [12] observed that reviews whose product ratings are extremely high or extremely low probably contain radical opinions. We therefore measure the deviation of a review's product rating from the average to assess its believability.

• The product rating deviation of a review $\left( f _ { 1 } \right)$

## ➢ Objectivity (D2)

This dimension is the extent to which an information item is biased. Apparently, subjective opinions in reviews help readers make decisions. We therefore apply Hu and Liu's algorithm [11] to extract sentiment sentences and measure this dimension in terms of review opinions.

• The number of opinion sentences (f ), positive sentences $( f _ { 3 } ) ,$ negative sentences $( f _ { 4 } )$ , and neutral sentences $( f _ { 5 } )$ in a review.

• The percentage of opinion sentences $( f _ { 6 } ) ,$ , positive sentences $( f _ { 7 } )$ negative sentences (f ), and neutral sentences (f ) in all sentences of a review.

• The percentage of positive sentences $\left( f _ { 1 0 } \right)$ and negative sentences $\left( f _ { 1 1 } \right)$ in all opinion sentences of a review.

• The cosine similarity between the tf-idf vectors [22] of a review and the product description $( f _ { 1 2 } ) .$ . The larger the similarity, the more objective the review will be.

## ➢ Reputation (D3)

This dimension is the extent to which the author of a review is trusted or highly regarded. Reviews written by authoritative reviewers are certainly in<sup>fl</sup>uential. We measure this dimension based on the reviewer's publications and the ranking given by e-commerce websites.

• The number of reviews written by the reviewer $\left( f _ { 1 3 } \right)$

• The ranking of the reviewer $\left( f _ { 1 4 } \right)$

## Table 1

Wang and Strong's hierarchical IQ framework [30].

<table><tr><td>IQ category</td><td>IQ dimensions</td></tr><tr><td>Intrinsic IQ</td><td>Believability, accuracy, objectivity, reputation</td></tr><tr><td>Contextual IQ</td><td>Value-added, relevancy, timeliness, completeness, appropriate amount of information</td></tr><tr><td>Representational IQ</td><td>Interpretability, ease of understanding, representational consistency, concise representation</td></tr><tr><td>Accessibility IQ</td><td>Accessibility, access security</td></tr></table>

## ➢ Relevancy (D4)

This dimension is the extent to which a review's content facilitates decision-making. Helpful product reviews should provide a large amount of product information. We consider the following statistics to assess the relevance of a review.

• The number of times the product name $( f _ { 1 5 } )$ , brand names $\left( f _ { 1 6 } \right)$ website names $\left( f _ { 1 7 } \right)$ , and other product names $\left( f _ { 1 8 } \right)$ are mentioned in a review.

• The percentage of the product name $\left( f _ { 1 9 } \right)$ , brand names $\left( f _ { 2 0 } \right)$ website names $\left( f _ { 2 1 } \right)$ , and other product names $( f _ { 2 2 } )$ among all these name entities in a review.

• The number of opinion sentences containing the product name $\left( f _ { 2 3 } \right)$ , brand names $( f _ { 2 4 } ) _ { }$ , website names $( f _ { 2 5 } )$ , and other product names $( f _ { 2 6 } )$ in a review.

• The percentage of opinion sentences containing the product name $( f _ { 2 7 } )$ , brand names $\left( f _ { 2 8 } \right)$ , website names $\left( f _ { 2 9 } \right)$ , and other product names $( f _ { 3 0 } )$ in all opinion sentences.

## ➢ Timeliness (D5)

This dimension is the extent to which the information in a review is timely and up-to-date. Old or duplicate reviews cannot re<sup>fl</sup>ect the value of a product over time; thus, the quality of information is low.

• The degree of duplication of a review $\left( f _ { 3 1 } \right)$ , de<sup>fi</sup>ned as the maximum cosine similarity between the tf-idf vectors of the review to those of reviews published previously.

• The interval (in terms of the number of days) between the current review and the <sup>fi</sup>rst review of the product $( f _ { 3 2 } )$

## ➢ Completeness (D6)

This dimension is the extent to which the information in a review is complete and covers various aspects of a product. Informative reviews should be wide ranging and cover many different product features and speci<sup>fi</sup>cations.

• The number of different product features $\left( f _ { 3 3 } \right)$ , brand names $( f _ { 3 4 } )$ , websites $( f _ { 3 5 } )$ , and product names $( f _ { 3 6 } )$ mentioned in a review.

## ➢ Appropriate Amount of Information (D7)

This dimension is the extent to which the volume of information in a review is suf<sup>fi</sup>cient for decision-making. A high-quality review should include a great deal of product information to help readers judge the value of a product.

• The number of product features $( f _ { 3 7 } )$ , opinion-bearing words $\left( f _ { 3 8 } \right)$ , words $\left( f _ { 3 9 } \right)$ , sentences $( f _ { 4 0 } ) _ { \mathrm { \Omega } }$ , and paragraphs $( f _ { 4 1 } )$ in a review.

• The average frequency of product features in a review $( f _ { 4 2 } )$

• The number of sentences that mention product features in a review (f ).

## ➢ Ease of Understanding (D8)

A comprehensible review should state opinions about a product directly and clearly; and it should not contain rarely used or misspelled words.

• The number of misspelled words in a review $( f _ { 4 4 } )$

• The average document frequency [22] of review words $( f _ { 4 5 } )$ . The average will be low if the review contains several rarely used words or misspellings.

• The position of the <sup>fi</sup>rst opinion sentence in a review $( f _ { 4 6 } )$

• The moving-average type/token ratios (MATTR) [4] in a review $( f _ { 4 7 } )$ . The measure calculates the average ratio of types (i.e., unique words) over tokens (i.e., words) in a moving context window. The average is high if the vocabulary of the review is diverse. As a result, readers would have to expend a great deal of effort on reading such reviews. In this research, we use a window size of 100, as suggested by Covington and McFall [4].

➢ Concise Representation (D9)

This dimension represents the conciseness of a review, and complements the dimension of the appropriate amount of information. Including a lot of information may result in a review that is too long.

• The average length of sentences $( f _ { 4 8 } )$ and paragraphs $( f _ { 4 9 } )$ in a review.

• The average number of sentences $( f _ { 5 0 } )$ and opinion sentences $( f _ { 5 1 } )$ in each paragraph of a review.

## 3.3. Classification models

By using the IQ framework, we can represent each review as a high-dimensional feature vector. To classify reviews in terms of quality, we employ the support vector machine (SVM), a state-of-theart machine learning algorithm for high-dimensional data classi<sup>fi</sup>cation [27]. More speci<sup>fi</sup>cally, we use two multiclass SVM-based approaches: One-Versus-All SVM and Single-Machine Multiclass SVM.

## ➢ One-Versus-All SVM (OVA SVM)

This approach decomposes a multiclass classi<sup>fi</sup>cation problem into N independent binary classi<sup>fi</sup>ers and assigns a class to a test review by using the following equation.

$$
f \left(\underline {{x}} _ {\text { test }}\right) = \arg \max _ {n} \left[ \left(\underline {{w}} _ {n} \cdot \underline {{x}} _ {\text { test }}\right) + b _ {n} \right], n = 1,..., N,\tag{1}
$$

where $\underline { { x } } _ { t e s t }$ is the high-dimensional feature vector of the test review; ${ \underline { { w _ { n } } } }$ and $b _ { n }$ are, respectively, the weight vector and intercept of a binary classi<sup>fi</sup>er n, and are learned from training reviews. When training a binary classi<sup>fi</sup>er for a quality class, the training reviews in the class are regarded as positive examples, and the remaining reviews are deemed negative examples. To classify a new review, each classi<sup>fi</sup>er computes a margin score that indicates the degree of association between the review and the corresponding class. The review is then assigned to the class with the largest score. We implement the One-Versus-All approach with the $\overline { { S } } V M ^ { l i g h t }$ binary SVM tool [13]. The RBF kernel is selected because of its superior classi<sup>fi</sup>cation performance.

## ➢ Single-Machine Multiclass SVM (SMM SVM)

Similar to OVA SVM, this approach classi<sup>fi</sup>es a test review by assigning it to the quality class with the maximal margin. However, rather than learn N independent binary classi<sup>fi</sup>ers, the single-machine approach learns ${ \underline { { w _ { n } } } }$ and $b _ { n }$ by considering N classes simultaneously [31] , as shown in Eqs. (2) and (3).

$$
\min \frac {1}{2} \sum_ {n = 1} ^ {N} \left(w _ {- n} \cdot w _ {- n}\right) + C \sum_ {i = 1} ^ {l} \sum_ {n \neq y _ {i}} \xi_ {i} ^ {n}\tag{2}
$$

s.t.

$$
\begin{array}{l} \left(w _ {- y _ {i}} \cdot x _ {- i}\right) + b _ {y _ {i}} \geq \left(w _ {- n} \cdot x _ {- i}\right) + b _ {n} + 2 - \xi_ {i} ^ {n}, \\ \xi_ {i} ^ {n} \geq 0, i = 1,..., l, n \in \{1,..., N \}, \end{array}\tag{3}
$$

where $\{ ( \underline { { x } } _ { 1 } , y _ { 1 } ) , . . . , ( \underline { { x } } _ { l } , y _ { l } ) \}$ is a set of l training examples. Each training review is represented as a high-dimensional feature vector $\underline { { x } } _ { i } ,$ and y is its class label; ζs are the slack variables for the training reviews; and C is a regularization term to control over<sup>fi</sup>tting. Minimizing the value of Eq. (2) allows us to search for the parameters that maximize the geometric margins between the N classes formed by the training reviews [22]. Eq. (3) requires that the searched parameters classify all the training reviews correctly. We employ the SVM<sup>multiclass</sup> tool [28] in our experiments; and we use linear kernels because non-linear kernels are time-consuming for multiclass problems. Moreover, experiments conducted by Hsu and Lin [10] demonstrated that linear kernels are comparable to non-linear kernels in many complex and large problems.

## 4. Quality-based review retrieval system

Based on the proposed method, we have developed a review retrieval system comprised of four major components, as shown in Fig. 2. In the following sub-sections, we describe each component in detail.

## 4.1. Data preprocessing

The data preprocessing component periodically searches various e-commerce websites and downloads new product reviews to our review database. Each review is parsed by using traditional information retrieval techniques, including tokenization, stopword <sup>fi</sup>ltering, and stemming, to extract terms for indexing [22]. To identify opinion sentences and sentence polarities in the reviews, we apply Hu and Liu's opinion mining algorithm [11]. The reviews are then transformed into IQ-based feature vectors for information quality classi<sup>fi</sup>cation.

## 4.2. Classification model construction

In this component, human experts are asked to compile a training dataset by elaborately labeling the quality classes of a suf<sup>fi</sup>cient number of reviews. The training dataset is then applied to the proposed classi<sup>fi</sup>cation method to construct an accurate quality classi<sup>fi</sup>er.

## 4.3. Review quality evaluation

This component classi<sup>fi</sup>es the information quality of reviews to facilitate quality-based review retrieval. For each review r in the database, the component uses the constructed classi<sup>fi</sup>er to compute a quality score scor ${ } _ { \stackrel { } { - } q u a l } ^ { 2 } ( r )$ , which indicates the degree of association (or the margin) between r and the ‘high-quality’ class. The higher the score, the better will be the information quality of r. Meanwhile, the score is normalized within the range (0,1] by the following equation.

$$
\widetilde {s c o r e _ {q u a l} (r)} = \frac {\text { score } _ {q u a l} (r) - \min _ {r ^ {\prime} \in R} \left(\text { score } _ {q u a l} (r ^ {\prime})\right) + 0 . 5}{\max _ {r ^ {\prime} \in R} \left(\text { score } _ {q u a l} (r ^ {\prime})\right) - \min _ {r ^ {\prime} \in R} \left(\text { score } _ {q u a l} (r ^ {\prime})\right) + 0 . 5},\tag{4}
$$

where R is the set of reviews in the system database. To avoid reclassifying a review's quality every time the system resolves a query and to improve the ef<sup>fi</sup>ciency of review retrieval, the normalized score is saved in the database.

## 4.4. Review ranking and retrieval

Given a query Q described by a set of query terms $\left\{ q _ { 1 } , q _ { 2 } , . . . , q _ { M } \right\}$ this component <sup>fi</sup>rst computes the degree of content relevance between Q and each review r in the system database. In this study, we employ the Okapi BM-25 weighting scheme to derive a queryrelevance score, denoted by $s c o r e _ { r e l } ( r , Q )$ , between r and Q. Okapi BM-25, de<sup>fi</sup>ned in Eq. (5), has been widely used in a range of information retrieval tasks and is considered a state-of-the-art information retrieval model [22].

$$
\operatorname{score} _ {r e l} (r, Q) = \sum_ {t = 1} ^ {M} \left(\log \frac {N}{d f _ {t}} \times \frac {\left(k _ {1} + 1\right) t f _ {t r}}{k _ {1} \left((1 - b) + b \left(L _ {d} / L _ {a v e}\right)\right) + t f _ {t r}}\right),\tag{5}
$$

where N is the number of reviews in the database; df is the document frequency of term q ; $t f _ { t r }$ is the term frequency of term q in review r;

![](/api/attachments/M9692CHG/fulltext/images/2873bf95f5b1fd7626ecb55745fd009a0bed29f3dd346abb3d2cf4d6ff0fc3ad.jpg)  
Fig. 2. The system architecture.

$L _ { r }$ is the length of review r; $L _ { a v e }$ is the average document length of all the reviews in the database; and parameters $k _ { 1 }$ and b are set at 1.2 and 0.75 respectively, as suggested in [22]. A large score $_ { r e l } ( r , Q )$ indicates that the content of review r is highly relevant to the query. We also normalize the score within the range [0,1] by the following equation.

$$
\widetilde {s c o r e _ {r e l}} (r, Q) = \frac {\text { score } _ {r e l} (r , Q)}{\max _ {r ^ {\prime} \in R} (\text { score } _ {r e l} (r ^ {\prime} , Q))}.\tag{6}
$$

After computing the query-relevance score, we derive a ranking score of r against Q, denoted as score $_ { r a n k } ( r , Q )$ , by combining score ${ } _ { r e l } ( r ,$ Q) with score $\check { \mathbf { \phi } } _ { q u a l } ( r )$ . In this research, we employ the logarithmic combination scheme [9], which has demonstrated superior performances in TREC opinion retrieval tracks. It is de<sup>fi</sup>ned as follows:

$$
\operatorname{score} _ {\text { rank }} (r, Q) = \alpha \times \operatorname{score} _ {\text { rel }} ^ {\sim} (r, Q) + (1 - \alpha) \frac {1}{1 - \log \left(\operatorname{score} _ {\text { qual }} ^ {\sim} (r)\right)},\tag{7}
$$

where parameter α is in the range [0, 1]. The parameter controls the weight of the query-relevance score and the logarithmic review quality score. The range of score $_ { r a n k } ( r , Q )$ is [0,1]; and a large score indicates that the review is both informative and query-relevant. Finally, the component ranks the reviews in the database in terms of their ranking scores, and the top-ranked reviews are returned to provide informative and query-relevant reviews for users.

Fig. 3 shows a screenshot of the system, in which the query is “Canon SD1100IS Digital Camera.” The system also provides a slide bar to control the weight of α so that users can choose reviews with highquality information or reviews that are highly query-relevant.

## 5. Performance evaluations

In this section, we analyze the performance of the IQ dimensions; compare the proposed approach with several review quality evaluation methods to demonstrate the advantages of the IQ framework; evaluate the quality-based review retrieval system; and examine the effectiveness of the IQ features for compiling informative product reviews. The evaluations are based on a review corpus where the quality of each review is annotated by human experts. The annotation process assumes that the criteria of quality judgments are constant (over the time period of the evaluations), and that the quality of reviews, once determined, will not <sup>fl</sup>uctuate according to other external factors.

## 5.1. Data preprocessing and annotation

In the <sup>fi</sup>eld of text mining, performance evaluations are normally based on of<sup>fi</sup>cial benchmarks. However, to the best of our knowledge, there are no of<sup>fi</sup>cial benchmarks for the review quality evaluation task because the research <sup>fi</sup>eld is relatively new. We therefore compiled our own review corpus for performance evaluations. Speci<sup>fi</sup>cally, our corpus comprises reviews on two types of products, namely digital cameras and mp3 players. We selected ten popular digital cameras and ten mp3 players advertised on Amazon. Then, for each product, we collected the <sup>fi</sup>rst 150 reviews (in order of publication date) to compile an evaluation corpus. Two human experts annotated the reviews independently based on the quality classes de<sup>fi</sup>ned in Section 3. Inconsistent annotations were resolved through discussions between the annotators and a third person to establish a groundtruth, as shown in Table 2. The kappa statistics between the annotators for digital cameras and mp3 players are 0.7253 and 0.7928, respectively. The scores are good enough to conduct reliable evaluations.

![](/api/attachments/M9692CHG/fulltext/images/cabde77d9accb0f10b1fb30f4bf0e1c5e3320c471c79e3cfbd309837dd9d3c16.jpg)  
Fig. 3. A screenshot of the quality-based review retrieval system.

Evaluations of review quality are conducted as follows. First, we examine the performance of our IQ dimensions. Then, the most effective combination of dimensions is compared with the following three feature sets: 1) the shallow syntactic feature set [34]; 2) the lexical features, i.e., unigrams, along with the length and the product rating of a review [16]; and 3) the informativeness feature set [21]. We use these feature sets for comparison because they have proven effective in review quality evaluations. In addition, we assess the performance of the bag-of-words model in which each unique term is represented as a feature [22]. This straightforward method is regarded as a baseline system. To convert the selected reviews into IQ-based feature vectors, we <sup>fi</sup>rst remove stopwords [22] from the reviews and check the remaining terms for misspellings by using WordNet, Wiktionary,<sup>6</sup> and Google's spell check function.<sup>7</sup> Next, we apply Hu and Liu's mining algorithm [11] to extract opinion sentences and sentence polarities from the reviews. According to Hu and Liu's experiments, the precision, recall, and, accuracy of the mining algorithm are 64.2%, 69.3%, and 84.2%, respectively. To reduce the effect of false extraction by the algorithm on our experiments, the extracted entities are examined manually.

Tables 3 and 4 detail the statistics of the opinion mining process. For digital camera reviews, 11,247 out of 27,499 sentences were extracted as opinion sentences. Among them, 6951 contained strong opinions. In addition, the algorithm wrongly identi<sup>fi</sup>ed the polarity of 465 opinion sentences and missed a further 3108 opinion sentences. For mp3 player reviews, 7919 out of 17,323 sentences were extracted as opinion sentences. Among them 4807 contained strong opinions. The algorithm wrongly identi<sup>fi</sup>ed the polarity of 658 opinion sentences and missed a further 1510 opinion sentences. In total, we manually correct 7869 sentences for the digital camera reviews and 5280 sentences for the mp3 player reviews.

The statistics of the review corpus.

<table><tr><td>Ground-truth</td><td>High</td><td>Medium</td><td>Low</td><td>Duplicate</td><td>Spam</td><td>Total</td></tr><tr><td>Digital cameras</td><td>113</td><td>297</td><td>1053</td><td>13</td><td>24</td><td>1500</td></tr><tr><td>mp3 players</td><td>134</td><td>297</td><td>1007</td><td>37</td><td>25</td><td>1500</td></tr><tr><td>Total</td><td>247</td><td>594</td><td>2060</td><td>50</td><td>49</td><td>3000</td></tr></table>

Table 3  
The contingency table for opinion extraction from digital camera reviews.

<table><tr><td></td><td>Opinioned</td><td>Non-opinioned</td><td>Total</td></tr><tr><td>Extracted</td><td>6951</td><td>4296</td><td>11,247</td></tr><tr><td>Not extracted</td><td>3108</td><td>13,144</td><td>16,252</td></tr><tr><td>Total</td><td>10,059</td><td>17,440</td><td>27,499</td></tr></table>

To ensure that the comparisons are fair, the SVM parameters C and ζ are set at 512 and 1.91e−006, respectively, for all the following evaluations. For each compared method, we use 10-fold crossvalidation [22] to derive credible results; that is, the review corpus is randomly divided into 10 equal sets. In each cross-validation run, one set is selected for testing, and the remaining sets are used for training to obtain SVM classi<sup>fi</sup>ers. Then, the results of the 10 crossvalidation runs are averaged for comparison. The evaluation metrics include the macro/micro-average precision, recall, and, F1 scores [22]. Precision is the proportion of reviews classi<sup>fi</sup>ed in a quality class that are actually in that class. Recall is the proportion of reviews in a quality class that are actually classi<sup>fi</sup>ed in that class. The F1 score is the weighted harmonic mean of precision and recall, and is commonly used to evaluate the overall effectiveness of a system [22]. In our corpus, as each review can only belong to one quality class, the microaverage precision, recall, and F1 scores are equivalent; thus, we only list the micro-average F1 scores. In addition, as shown in Table 2, the ‘spam’ and ‘duplicate’ quality classes are very small; hence, a simple misclassi<sup>fi</sup>cation in these classes would cause a huge variation in the macro-averaging performance. However, the micro-average F1 score is insensitive to class size, so it is appropriate for evaluating the overall performance of the compared methods.

## 5.2. IQ dimension evaluations

Fig. 4 shows the performance of the IQ dimensions using the SMM SVM and OVA SVM approaches. As shown in the <sup>fi</sup>gure, dimensions ‘Objectivity (D2)’ and ‘Appropriate Amount of Information (D7)’ achieve superior evaluation performances, but ‘Completeness (D6)’ is not effective under SMM SVM. The results re<sup>fl</sup>ect an interesting phenomenon about product review writing. From the corpus, we observed that the kinds of product features, product names, brands, and websites are quite diverse, so a review may only be able to cover a few of them, no matter what quality class they belong to. Consequently, ‘Completeness’ is not effective in discriminating review quality. Even though reviews do not usually present broad investigations, high-quality reviews still present in-depth opinions and comments on the covered product features in order to make them constructive. As a result, ‘Objectivity’ and ‘Appropriate Amount of Information’ are effective. In sum, all the IQ dimensions, except ‘Completeness’ under linear SMM SVM, are effective in evaluating the quality of reviews.

Tables 5 and 6 show the effects of the IQ dimensions iteration by iteration. In the <sup>fi</sup>rst iteration, we examine the performance of each IQ dimension and list the performance of the dimension that produces the best micro-average F1 score in the <sup>fi</sup>rst row of each table. In the ith iteration (2≤i≤9), the set of dimensions selected in the (i−1)th iteration serves as the basis. Next, we examine each remaining dimension combined with the basis and show the performance of the combination that produces the best micro-average F1 score in the ith row. For instance, the third row in Table 3 shows the performance of the top-3 effective dimensions, {Objectivity, Reputation, Appropriate Amount of Information}, that produce the best micro-average F1 score under SMM SVM. For each row, a one-tail paired t-test is applied to determine whether combining each dimension with the basis improves the system performance signi<sup>fi</sup>cantly. The symbol (\*) indicates that combining a dimension improves the performance signi<sup>fi</sup>cantly, while the symbol ‘#’ indicates the opposite. We consider a dimension effective if combining it with the basis does not reduce any micro-average F1 score for the digital camera reviews and mp3 player reviews. In addition, the selected dimension must yield a signi<sup>fi</sup>cant improvement in the micro-average F1 score of at least one type of product review. Consequently, the most effective dimension combinations for the linear kernel and the RBF kernel are {D2, D3, D7, D8} and {D2, D7, D9} respectively. We use them in the following comparisons.

Table 4  
The contingency table for opinion extraction from mp3 player reviews.

<table><tr><td></td><td>Opinioned</td><td>Non-opinioned</td><td>Total</td></tr><tr><td>Extracted</td><td>4807</td><td>3112</td><td>7919</td></tr><tr><td>Not extracted</td><td>1510</td><td>7894</td><td>9404</td></tr><tr><td>Total</td><td>6317</td><td>11,006</td><td>17,323</td></tr></table>

(a) Digital cameras  
![](/api/attachments/M9692CHG/fulltext/images/837a17693766c2ddfc97c7e4831f6c9e560978e049083dfd24d399412c912581.jpg)

(b) Mp3 players  
![](/api/attachments/M9692CHG/fulltext/images/abaa3865d06c96b6fdeefe66b61b2456dd7df9a914ee21dae4fd248e9d655543.jpg)  
Fig. 4. The performance of the IQ dimensions.

It is noteworthy that one IQ dimension (i.e., D7 — Appropriate Amount of Information) is suf<sup>fi</sup>cient for the RBF kernel to achieve superior performances; however, combining this dimension with the other IQ dimensions does not improve the system performance overall. This is because non-linear kernels have a powerful modeling ability, so a few discriminative features and dimensions are suf<sup>fi</sup>cient to construct accurate classi<sup>fi</sup>ers. Note that ‘Objectivity (D2)’ and ‘Appropriate Amount of Information (D7)’ are in the top-3 effective dimensions of both SVM approaches. This indicates, once again, that the degree of sentiment and the amount of product information are critical criteria for judging the quality of a review. We observe that the less effective dimensions often contain diverse features. For instance, the features of the ‘Completeness’ dimension are too sparse to discriminate quality classes. Consequently, there is little difference between using all IQ dimensions to evaluate the quality of reviews and only using the most effective combinations.

Table 6  
Table 7  
Table 5  
The effect of IQ dimensions using SMM SVM with the linear kernel operator.

<table><tr><td rowspan="2"></td><td colspan="4">Digital cameras</td><td colspan="4">mp3 players</td></tr><tr><td>Mac-precision</td><td>Mac-recall</td><td>Mac-F1</td><td>Mic-F1</td><td>Mac-precision</td><td>Mac-recall</td><td>Mac-F1</td><td>Mic-F1</td></tr><tr><td>Objectivity (D2)</td><td>0.697</td><td>0.440</td><td>0.535</td><td>0.768</td><td>0.715</td><td>0.358</td><td>0.471</td><td>0.742</td></tr><tr><td>+ Reputation (D3)</td><td>*0.745</td><td>****0.486</td><td>***0.585</td><td>****0.832</td><td>*0.742</td><td>****0.404</td><td>****0.514</td><td>****0.782</td></tr><tr><td>+ Information (D7)</td><td>****0.868</td><td>****0.575</td><td>****0.691</td><td>****0.900</td><td>*0.800</td><td>****0.465</td><td>****0.584</td><td>****0.849</td></tr><tr><td>+ Understanding (D8)</td><td>0.870</td><td>****0.588</td><td>**0.702</td><td>*0.909</td><td>*0.834</td><td>*0.483</td><td>*0.612</td><td>****0.863</td></tr><tr><td>+ Timeliness (D5)</td><td>0.866</td><td>*0.597</td><td>0.706</td><td>0.909</td><td>0.845</td><td>0.483</td><td>0.614</td><td>0.864</td></tr><tr><td>+ Believability (D1)</td><td>0.868</td><td>0.601</td><td>0.708</td><td>0.910</td><td>0.842</td><td>0.482</td><td>0.613</td><td>0.863</td></tr><tr><td>+ Relevancy (D4)</td><td>0.868</td><td>#0.594</td><td>0.705</td><td>0.906</td><td>#0.789</td><td>0.478</td><td>#0.596</td><td>0.858</td></tr><tr><td>+ Completeness (D6)</td><td>##0.847</td><td>0.589</td><td>#0.695</td><td>0.906</td><td>0.791</td><td>0.485</td><td>0.601</td><td>0.861</td></tr><tr><td>+ Concise (D9)</td><td>0.835</td><td>##0.574</td><td>#0.681</td><td>#0.901</td><td>0.789</td><td>0.489</td><td>0.603</td><td>0.861</td></tr></table>

\*, \*\*, \*\*\*, and \*\*\*\* represent right-tail paired t-tests with α = 0.1, 0.05, 0.025, and 0.01, respectively.  
#, ##, ###, and #### represent left-tail paired t-tests with α=0.1, 0.05, 0.025, and 0.01, respectively

The effect of IQ dimensions using OVA SVM with the RBF kernel operator.

<table><tr><td rowspan="2"></td><td colspan="4">Digital cameras</td><td colspan="4">mp3 players</td></tr><tr><td>Mac-precision</td><td>Mac-recall</td><td>Mac-F1</td><td>Mic-F1</td><td>Mac-precision</td><td>Mac-recall</td><td>Mac-F1</td><td>Mic-F1</td></tr><tr><td>Information (D7)</td><td>0.838</td><td>0.586</td><td>0.686</td><td>0.908</td><td>0.821</td><td>0.508</td><td>0.622</td><td>0.870</td></tr><tr><td>+ Concise (D9)</td><td>0.861</td><td>*0.592</td><td>0.700</td><td>0.910</td><td>*0.832</td><td>0.506</td><td>0.623</td><td>*0.875</td></tr><tr><td>+ Objectivity (D2)</td><td>0.866</td><td>0.597</td><td>0.706</td><td>*0.914</td><td>0.836</td><td>0.505</td><td>0.623</td><td>0.876</td></tr><tr><td>+ Believability (D1)</td><td>0.866</td><td>0.597</td><td>0.706</td><td>0.914</td><td>0.836</td><td>0.505</td><td>0.623</td><td>0.876</td></tr><tr><td>+ Completeness (D6)</td><td>0.865</td><td>0.597</td><td>0.705</td><td>0.914</td><td>0.831</td><td>0.508</td><td>0.624</td><td>0.876</td></tr><tr><td>+ Understanding (D8)</td><td>0.864</td><td>0.595</td><td>0.703</td><td>0.912</td><td>0.831</td><td>0.507</td><td>0.623</td><td>0.875</td></tr><tr><td>+ Timeliness (D5)</td><td>0.820</td><td>0.584</td><td>0.682</td><td>0.907</td><td>0.843</td><td>0.502</td><td>0.624</td><td>0.873</td></tr><tr><td>+ Relevancy (D4)</td><td>0.818</td><td>0.580</td><td>0.678</td><td>0.906</td><td>0.844</td><td>0.499</td><td>0.623</td><td>0.871</td></tr><tr><td>+ Reputation (D3)</td><td>#0.783</td><td>#0.571</td><td>#0.657</td><td>#0.901</td><td>#0.836</td><td>#0.495</td><td>##0.617</td><td>#0.867</td></tr></table>

\* represents right-tail paired t-tests with α=0.1.  
# and ## represent left-tail paired t-tests with α=0.1 and 0.05, respectively.

The comparison results using SMM SVM with the linear kernel operator.

<table><tr><td rowspan="2"></td><td colspan="4">Digital cameras</td><td colspan="4">mp3 players</td></tr><tr><td>Mac-precision</td><td>Mac-recall</td><td>Mac-F1</td><td>Mic-F1</td><td>Mac-precision</td><td>Mac-recall</td><td>Mac-F1</td><td>Mic-F1</td></tr><tr><td>Baseline</td><td>****0.424</td><td>****0.323</td><td>****0.365</td><td>****0.670</td><td>****0.361</td><td>****0.257</td><td>****0.297</td><td>****0.580</td></tr><tr><td>Shallow syntactic</td><td>****0.279</td><td>****0.283</td><td>****0.275</td><td>****0.608</td><td>****0.213</td><td>****0.239</td><td>****0.220</td><td>****0.298</td></tr><tr><td>Lexical</td><td>****0.595</td><td>****0.362</td><td>****0.448</td><td>****0.744</td><td>****0.472</td><td>****0.306</td><td>****0.369</td><td>****0.683</td></tr><tr><td>Informativeness</td><td>0.853</td><td>***0.562</td><td>*0.676</td><td>****0.886</td><td>***0.794</td><td>0.463</td><td>*0.581</td><td>**0.844</td></tr><tr><td>D2 + D3 + D7 + D8</td><td>0.870</td><td>0.588</td><td>0.702</td><td>0.909</td><td>0.834</td><td>0.483</td><td>0.612</td><td>0.863</td></tr></table>

\*, \*\*, \*\*\*, and \*\*\*\* represent right-tail paired t-tests with α=0.1, 0.05, 0.025, and 0.01, respectively.

## 5.3. Comparison with other methods

Tables 7 and 8 show the performances of the compared methods. Generally, all the methods outperform the baseline method in terms of the micro-average F1 scores. The proposed method achieves the best performance and the improvement over each of the compared methods is statistically signi<sup>fi</sup>cant in terms of a one-tailed paired ttest. Liu's approach is a state-of-the-art method for classifying the quality of reviews. The set of informativeness features is also information-oriented; hence, its performance is good and comparable to that of the proposed method. The sets of shallow syntactic features and lexical features are effective in determining a review's helpfulness, which is the ratio of helpfulness votes given by readers; however, as mentioned previously, the helpfulness-based review quality is affected by biases. Therefore, the performances of those features are inferior, and they are even worse than the performance of the baseline method when the linear kernel is used.

of reviews in detail. The superior evaluation performances indicate that the derived features and dimensions based on the theoretical IQ framework are highly representative of the reviews' characteristics.

The bag-of-words model has proven effective in traditional text classi<sup>fi</sup>cation tasks [22], but its inferior performances in evaluating the quality of reviews highlight the dif<sup>fi</sup>culty of the evaluation task. Since reviews are sentimental and information-oriented, evaluation systems must consider both the textual and semantic characteristics of reviews to measure review quality effectively. Our method examines various factors

## 5.4. Quality-based review retrieval evaluation

In this section, ten queries<sup>8</sup> related to 5 popular digital cameras and 5 mp3 players are selected for quality-based review retrieval evaluation. For each query, the proposed review retrieval system ranks reviews according to the score calculated by Eq. (7). Here, we adopt OVA SVM with the RBF kernel to calculate the quality score because of the approach's superior classi<sup>fi</sup>cation performance, as shown in Section 5.3. Two independent experts then examine the ranking and measure a precision at k score [22] of the ranking. Precision at k is an effective evaluation metric that measures the performance of an information retrieval system [22]. It calculates the proportion of good results in the top-k returned documents for a query. A review retrieval system is effective if its top-ranked reviews help users evaluate a product. As a result, the precision at k score will be high. In the following experiments, we <sup>fi</sup>rst examine the effect of parameter α in Eq. (7), which controls the weights of the query-relevance score and the quality score for ranking calculations. Then, we compare the retrieval performance of the quality evaluation methods examined in Section 5.3 to demonstrate the advantage of the proposed system.

Table 8  
The comparison results using OVA SVM with the RBF kernel operator.

<table><tr><td rowspan="2"></td><td colspan="4">Digital cameras</td><td colspan="4">mp3 players</td></tr><tr><td>Mac-precision</td><td>Mac-recall</td><td>Mac-F1</td><td>Mic-F1</td><td>Mac-precision</td><td>Mac-recall</td><td>Mac-F1</td><td>Mic-F1</td></tr><tr><td>Baseline</td><td>****0.696</td><td>****0.412</td><td>****0.516</td><td>****0.782</td><td>****0.711</td><td>****0.389</td><td>****0.502</td><td>****0.757</td></tr><tr><td>Shallow syntactic</td><td>****0.796</td><td>****0.577</td><td>****0.666</td><td>****0.888</td><td>0.817</td><td>0.491</td><td>0.610</td><td>****0.852</td></tr><tr><td>Lexical</td><td>**0.821</td><td>****0.576</td><td>***0.674</td><td>****0.895</td><td>****0.801</td><td>0.515</td><td>0.626</td><td>***0.856</td></tr><tr><td>Informativeness</td><td>0.836</td><td>0.590</td><td>0.688</td><td>****0.904</td><td>****0.800</td><td>**0.488</td><td>***0.601</td><td>****0.856</td></tr><tr><td>D2 + D7 + D9</td><td>0.866</td><td>0.597</td><td>0.706</td><td>0.914</td><td>0.836</td><td>0.505</td><td>0.623</td><td>0.876</td></tr></table>

Table 9 shows the averaged precision at k scores derived by the proposed system for the queries. When α=1, the retrieval system ignores information quality and simply ranks reviews in terms of query relevance. Top-ranked reviews thus provide few opinions because opinion information is not the focus of the search process. Consequently, the returned reviews hardly help users review a product and the corresponding precision at k score is low. Conversely, by setting α at 0, the system ranks reviews regardless of query relevance. Most of the topranked reviews are thus irrelevant to the queried product, so the precision at k score is also inferior. For α=0.25, 0.5, and 0.75, the precision at k score decreases as α increases. This indicates that query relevance is relatively less important than information quality when searching for review. This is because the examined queries are distinct product names, so the retrieval system can identify query-relevant reviews unambiguously. Consequently, information quality is a critical factor in providing good reviews for users. Another interesting phenomenon shown in Table 9 is that the precision at k score decreases as k increases. This is because lowranked reviews are relatively inferior to top-ranked reviews in terms of information quality and query relevance. Hence, the precision decreases as the number of retrieved reviews increases. It is also noteworthy that the precision scores in the table are relatively lower than those in Tables 5 and 6. This is because we do not manually examine reviews retrieved by the system to exclude false opinion entities extracted by the opinion mining algorithm. As the retrieval database is very large and grows every time our review crawler downloads new reviews from e-commerce websites, manual examinations would be too time-consuming and therefore infeasible given our limited human resources. Consequently, the performance of the retrieval system is affected by false opinion entity extractions. However, as opinion mining and extraction are active research <sup>fi</sup>elds, we expect that the false opinion extraction problem will be alleviated when new opinion mining technologies are invented. As shown in Table 9, setting α at 0.25 produces the most accurate retrieval precision score for each setting of k. In addition, more than half of the returned reviews are helpful for users. We thus employ this setting in the next experiment. In sum, the improvements derived by setting α=0.25 over α=0, 0.75, and 1 are statistically signi<sup>fi</sup>cant at the 99% con<sup>fi</sup>dence level based on a one-tailed paired t-test. For α=0.5, the con<sup>fi</sup>dence level of the improvement is 90%.

Table 9  
The precision at k scores of the proposed system

<table><tr><td>α</td><td>P@1</td><td>P@3</td><td>P@5</td><td>P@10</td><td>P@15</td><td>P@20</td></tr><tr><td>0</td><td>0.05</td><td>0.05</td><td>0.04</td><td>0.035</td><td>0.067</td><td>0.06</td></tr><tr><td>0.25</td><td>0.85</td><td>0.733</td><td>0.67</td><td>0.635</td><td>0.577</td><td>0.515</td></tr><tr><td>0.5</td><td>0.65</td><td>0.583</td><td>0.56</td><td>0.525</td><td>0.517</td><td>0.45</td></tr><tr><td>0.75</td><td>0.35</td><td>0.317</td><td>0.29</td><td>0.315</td><td>0.31</td><td>0.275</td></tr><tr><td>1</td><td>0.3</td><td>0.25</td><td>0.21</td><td>0.215</td><td>0.197</td><td>0.188</td></tr></table>

P@k: precision at k.

Table 10  
The review retrieval performance of the evaluated methods.

<table><tr><td>α=0.25</td><td>P@1</td><td>P@3</td><td>P@5</td><td>P@10</td><td>P@15</td><td>P@20</td></tr><tr><td>Baseline</td><td>***0.45</td><td>***0.417</td><td>***0.42</td><td>****0.43</td><td>****0.407</td><td>****0.368</td></tr><tr><td>Shallow syntactic</td><td>*0.75</td><td>***0.6</td><td>**0.58</td><td>****0.505</td><td>****0.473</td><td>****0.425</td></tr><tr><td>Lexical</td><td>0.8</td><td>0.683</td><td>0.65</td><td>***0.56</td><td>****0.48</td><td>****0.428</td></tr><tr><td>Informativeness</td><td>0.8</td><td>0.7</td><td>0.63</td><td>***0.565</td><td>*0.537</td><td>**0.473</td></tr><tr><td>Our method</td><td>0.85</td><td>0.733</td><td>0.67</td><td>0.635</td><td>0.577</td><td>0.515</td></tr></table>

(a) Digital cameras  
![](/api/attachments/M9692CHG/fulltext/images/6b6d2987789282166b2ca4f0c8fd5142859aa4e71d991bff680e2fdb9de1b2c0.jpg)

(b) Mp3 players  
![](/api/attachments/M9692CHG/fulltext/images/c1ebe1641da9e2726ffa78a6bb1c117faea2d4d9dfbb7b684dfef9c1658d69c1.jpg)  
Fig. 5. The lift curves of the top-5 IQ features for high-quality reviews.

Table 11  
The representative feature averages for quality classes.

<table><tr><td rowspan="2">Feature</td><td colspan="5">Digital cameras</td><td colspan="5">mp3 players</td></tr><tr><td>High</td><td>Medium</td><td>Low</td><td>Duplicate</td><td>Spam</td><td>High</td><td>Medium</td><td>Low</td><td>Duplicate</td><td>Spam</td></tr><tr><td> $f_2$ </td><td>21.78</td><td>10.53*</td><td>3.94*</td><td>20.85</td><td>1.88*</td><td>11.97</td><td>6.51*</td><td>2.52*</td><td>6.41*</td><td>0.28*</td></tr><tr><td> $f_{37}$ </td><td>68.31</td><td>28.69*</td><td>8.76*</td><td>53.00</td><td>3.46*</td><td>46.22</td><td>19.66*</td><td>6.46*</td><td>20.89*</td><td>3.44*</td></tr><tr><td> $f_{38}$ </td><td>42.72</td><td>19.53*</td><td>6.51*</td><td>36.92</td><td>3.38*</td><td>38.06</td><td>16.67*</td><td>6.09*</td><td>14.24*</td><td>3.48*</td></tr><tr><td> $f_{39}$ </td><td>662.43</td><td>289.22*</td><td>87.41*</td><td>542.92</td><td>73.71*</td><td>662.22</td><td>284.13*</td><td>100.15*</td><td>238.27*</td><td>97.96*</td></tr><tr><td> $f_{43}$ </td><td>28.40</td><td>12.94*</td><td>4.49*</td><td>23.46</td><td>2.54*</td><td>23.73</td><td>10.58*</td><td>3.65*</td><td>10.43*</td><td>1.96*</td></tr></table>

⁎ The con<sup>fi</sup>dence level reaches 99% based on a one-tailed t-test to test the mean difference between the high-quality and other quality.

Table 10 shows the retrieval performance of the quality evaluation approaches discussed in Section 5.3. Once again, the proposed method outperforms the other methods and achieves the best precision at k score for all conditions. Moreover, the improvements over the other approaches are statistically signi<sup>fi</sup>cant when $k \geq 1 0 .$ . The experiment results demonstrate that our method can classify the quality class of reviews accurately and also provide effective review retrieval for users.

## 5.5. High-quality review analysis

After examining the performance of the IQ framework, we determine the important factors involved in compiling high-quality reviews. We employ lift analysis [19] to visualize the effectiveness of an IQ feature in representing high-quality reviews. Lift analysis, a popular method for measuring the effectiveness of data mining components [12], examines the effectiveness of an IQ feature by <sup>fi</sup>rst dividing the review corpus into training and test sets. Next, the training reviews are used to build a highquality classi<sup>fi</sup>er based on the IQ feature. The classi<sup>fi</sup>er computes a margin score for each test review, after which the test reviews are sorted in descending order based on the margin score and divided into 10 equal deciles. Finally, a lift curve of the feature is constructed by computing the cumulative gain (CG) for each decile as follows:

$$
C G _ {j} = \frac {\text { the   cumulated   number   of   high   quality   reviews   at   decile } j}{\text { the   total   number   of   high   quality   reviews }} \times 100 \%\tag{8}
$$

where j is the index of deciles and $0 { \leq } j { \leq } 1 .$ . In short, $C G _ { j }$ represents the cumulative percentage of high-quality reviews from the <sup>fi</sup>rst decile to decile j. Graphically, a lift curve always runs from the bottom lefthand corner to the top right-hand corner of a lift curve chart. A feature is representative of high-quality reviews if its classi<sup>fi</sup>er tends to compute large margins for high-quality reviews. In such cases, the lift curve will climb steeply on the left-hand side and the area under the curve will be large. By contrast, a non-representative feature will distribute the high-quality reviews randomly over the deciles, so its lift curve will be diagonal. We examine the lift curves of all IQ features and show the top-5 IQ features in terms of the area under the lift curve in Fig. 5. Again, we employ 10-fold cross-validation and adopt OVA SVM with the RBF kernel because of its superior performance.

As shown in the <sup>fi</sup>gure, the <sup>fi</sup>rst two deciles of the top-5 features account for 80% to 100% of high-quality reviews. Therefore, they are representative of high-quality reviews. To further investigate the characteristics of the features in high-quality reviews, we average the feature values for each of the <sup>fi</sup>ve quality classes. The statistics are detailed in Table 11.

As shown in the table, the averages of the ‘high-quality’ class are higher than those of the other quality classes. Moreover, except for the ‘duplicate’ class, the average differences over the other classes are statistically signi<sup>fi</sup>cant at the 99% con<sup>fi</sup>dence level in a one-tail paired t-test. Based on the results, we present the following guidelines for compiling high-quality reviews:

• High-quality reviews should contain a large number of opinions, as suggested by the statistics of f (the number of opinion sentences) and $f _ { 3 8 }$ (the number of opinion-bearing words). We also compile lift curves for $f _ { 1 0 }$ (the percentage of positive sentences in all opinion sentences extracted from a review) and $f _ { 1 1 }$ (the percentage of negative sentences in all opinion sentences extracted from a review) to determine whether the opinions need to be positive or negative. It is interesting that opinion polarity is not a representative factor, as shown by the nearly diagonal curves in Fig. 6. The results indicate that, in addition to learning about the advantages of a product through positive opinions, users also appreciate negative opinions because they can learn about the product's defects.

(a) Digital cameras  
![](/api/attachments/M9692CHG/fulltext/images/f6f93d77253ac8a24cb406a05e46836aeaad79ac1d883a7749e4338ecd5c2969.jpg)

![](/api/attachments/M9692CHG/fulltext/images/b3accb3ccf5d13b944bd260e4c7e9c85f8aff1b5908b10653d115ea1e118ec10.jpg)  
Fig. 6. The lift curves of $f _ { 1 0 }$ and $f _ { 1 1 }$ for high-quality reviews.

• High-quality reviews should contain abundant product information as suggested by the high statistics of $f _ { 3 7 }$ (the number of product features), $f _ { 3 9 }$ (the number of words), and $f _ { 4 3 }$ (the number of sentences that mention product features). In other words, to be constructive, reviews should present in-depth opinions and comments on a product's features.

As shown in Table 11, the averages of the ‘duplicate’ class are relatively close to the averages of the ‘high-quality’ and ‘mediumquality’ classes. This is because many duplicated reviews are actually plagiarized, and plagiarists naturally select good reviews to modify in order to make their reviews attractive. Thus, the statistics are similar. To discriminate duplicated reviews from high-quality and mediumquality reviews, the IQ framework considers a review's timeliness (i.e., dimension D5). As shown in Fig. 7, the lift curve of feature $f _ { 3 1 }$ (the degree of duplication of a review, a factor of dimension D5), is very steep for duplicated reviews; hence, our IQ-based classi<sup>fi</sup>ers can accurately identify duplicated reviews.

(a) Digital cameras  
![](/api/attachments/M9692CHG/fulltext/images/ab31c659ea9e8c399e74cbdc54f8f0317e04169919174fbea2cda23b54446826.jpg)

(b) Mp3 players  
![](/api/attachments/M9692CHG/fulltext/images/dd44cb5e7e65545bfa2dfc46a2162c369a028f1843d12b9e5eb02c9a76af88ff.jpg)  
Fig. 7. The lift curves of $f _ { 3 1 }$ for high-quality and duplicated reviews.

We also examine the lift curves of $f _ { 1 3 }$ (the number of reviews written by the reviewer) and $f _ { 1 4 }$ (the ranking of the reviewer) to determine whether the reputation of reviewers is a critical component in compiling high-quality reviews. As shown in Fig. 8, the lift curves of the features are not as steep as the curves in Fig. 5. This means that, although authoritative reviewers generally produce highquality reviews, good reviews can be written by non-experts, provided that the content is informative. As the spirit of Web2.0 encourages Internet users to share their knowledge, the majority of Internet reviews are written by ordinary, possibly anonymous, contributors. Quality evaluation methods that pay too much attention to the reputation of reviewers may ignore potential reviewers and miss many informative reviews. In contrast, our IQ framework considers the reputation of reviewers as well as many critical review characteristics. Thus, its evaluations of review quality are superior to those of existing methods.

Finally, we consider the lift curves of the IQ dimensions. As shown in Fig. 9, dimension ‘Appropriate Amount of Information (D7)’ is the most effective dimension in representing high-quality reviews. The result is highly consistent with the results presented in Fig. 5 and

(a) Digital cameras  
![](/api/attachments/M9692CHG/fulltext/images/43b9b56f8d1c328ef536e4497e7cfacc498d46dc18732fa36fe856dc3417b27d.jpg)

![](/api/attachments/M9692CHG/fulltext/images/f0d065fd2989f0d50167a133cdce84beb5d3ef50ae3e499dc8bbf980188584ea.jpg)  
Fig. 8. The lift curves o $\dot { f } _ { 1 3 }$ and $f _ { 1 4 }$ for high-quality reviews.

(a) Digital cameras  
![](/api/attachments/M9692CHG/fulltext/images/7edbe49b6e067688ea32e4adb78f6c68bee6387936b23f1bbb0c4003c2229c86.jpg)

(b) Mp3 players  
![](/api/attachments/M9692CHG/fulltext/images/9220ea84101e8c6d87d864c5efe8dc81d0e1005e716b4d4e94b7ab8f23481967.jpg)  
Fig. 9. The lift curves of the IQ dimensions for high-quality reviews.

Table 11, in which most of the effective IQ features also belong to dimension D7. The steep curves of ‘Objectivity (D2),’ ‘Relevancy (D4), and ‘Completeness (D6)’ once again indicate that a high-quality review should contain a large number of opinions and include as much product information as possible.

## 6. Conclusion

The Web has become a valuable source of business information. For instance, product reviews posted on e-commerce websites and forums can help Internet users and enterprises make decisions. Positive opinions expressed in reviews may persuade users to purchase a product, while negative opinions may alert enterprises to defects in their products or motivate them to re<sup>fi</sup>ne their business strategies. Opinion mining of product reviews has thus become an important research area. Many opinion mining approaches focus on identifying bipolar opinions in reviews; however, few works consider the quality of information in reviews. Although reviews and opinions may be sentimental, they may not be informative. In this paper, we have proposed a method for evaluating the quality of information in product reviews. We regard a review as an information item and apply a theoretical information quality framework to derive representative review features and dimensions. Experiments show that our method can accurately classify reviews in terms of their quality, and that it signi<sup>fi</sup>cantly outperforms state-of-the-art methods. In addition, we analyze the factors that are important for compiling high-quality reviews and demonstrate that such reviews need to be subjective and provide in-depth comments on a number of product features. Finally, we present an effective review retrieval system that considers both the information quality and query relevance of reviews.

In the future, we will examine the correlation between features and <sup>fi</sup>lter out those that are redundant to improve the system's ef<sup>fi</sup>ciency. We will also apply the proposed method to various styles of documents that contain opinions, such as blog entries and forum threads, to assess the quality of the information they provide.

## Acknowledgements

The authors would like to thank the anonymous reviewers for their valuable comments and suggestions. This work was supported in part by the NSC 97-2221-E-002-225-MY2.

## References

[1] M.S.E. Burgess, W.A. Gray, N.J. Fiddian, Using quality criteria to assist in information searching, International Journal of Information Quality 1 (1) (2007) 83–99

[2] M. Chae, J. Kim, Information quality for mobile Internet services: a theoretical model with empirical validation, Electronic Markets 12 (1) (2002) 38–46.

[3] J.A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (3) (2006) 345–354.

[4] M.A. Covington, J.D. McFall, The Moving-Average Type-Token Ratio (MATTR), Linguistic Society of America, 2008.

[5] K. Dave, S. Lawrence, D.M. Pennock, Mining the Peanut Gallery: Opinion Extraction and Semantic Classi<sup>fi</sup>cation of Product Reviews, Proceedings of the 12th International Conference on World Wide Web, 2003, pp. 519–528.

[6] X. Ding, B. Liu, P.S. Yu, A Holistic Lexicon-Based Approach to Opinion Mining, Proceedings of the International Conference on Web Search and Web Data Mining, 2008, pp. 231–240.

[7] M.J. Eppler, D. Wittig, Conceptualizing Information Quality: A Review of Information Quality Frameworks from the Last Ten Years, Proceedings of the 2000 Conference on Information Quality, 2000, pp. 83–96.

[8] C. Fellbaum, WordNet: an Electronic Lexical Database, MIT Press, 1998.

[9] B. He, C. Macdonald, J. He, I. Ounis, An Effective Statistical Approach to Blog Post Opinion Retrieval, Proceeding of the 17th ACM Conference on Information and Knowledge Management, 2008, pp. 1063–1072.

[10] C.W. Hsu, C.J. Lin, A comparison of methods for multiclass support vector machines, IEEE Transactions on Neural Networks 13 (2) (2002) 415–425.

[11] M. Hu, B. Liu, Mining and Summarizing Customer Reviews, Proceedings of the tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2004, pp. 168–177.

[12] N. Jindal, B. Liu, Opinion Spam and Analysis, Proceedings of the international conference on Web Search and Web Data Mining, 2008, pp. 219–230.

[13] T. Joachims, Making large-scale SVM learning practical, Advances in Kernel Methods: Support Vector Learning (1999) 169–184.

[14] K.S. Jones, S. Walker, S.E. Robertson, A probabilistic model of information retrieval: development and comparative experiments: part 1, Information Processing and Management 36 (6) (2000) 779–808

[15] S.M. Kim, E. Hovy, Determining the Sentiment of Opinions, Proceedings of the 20th International Conference on Computational Linguistics, 2004, pp. 1367–1373.

[16] S.M. Kim, P. Pantel, T. Chklovski, M. Pennacchiotti, Automatically Assessing Review Helpfulness, Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing, 2006, pp. 423–430

[17] S. Knight, J. Burn, Developing a framework for assessing information quality on the world wide web, Information Science Journal 8 (2005) 159–172.

[18] L.W. Ku, Y.T. Liang, H.H. Chen, Opinion Extraction, Summarization and Tracking in News and Blog Corpora, Proceedings of the AAAI Spring Symposium on Computational Approaches to Analyzing Weblogs, 2006, pp. 100–107.

[19] C. Ling, C. Li, Data Mining for Direct Marketing: Problems and Solutions, Proceedings of the Fourth International Conference on Knowledge Discovery and Data Mining, 1998, pp. 73–79.

[20] B. Liu, M. Hu, J. Cheng, Opinion Observer: Analyzing and Comparing Opinions on the Web, Proceedings of the 14th International Conference on World Wide Web, 2005, pp. 342–351.

[21] J. Liu, Y. Cao, C.Y. Lin, Y. Huang, M. Zhou, Low-Quality Product Review Detection in Opinion Summarization, Proceedings of the 2007 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning, 2007, pp. 334-342

[22] C. Manning, P. Raghavan, H. Schütze, An Introduction to Information Retrieval, Cambridge University Press, 2008.

[23] G. Miller, R. Beckwith, C. Fellbaum, D. Gross, K. Miller, Introduction to WordNet: an online Lexical Database, International Journal of Lexicography 3 (4) (1990) 235–244.

[24] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up? Sentiment Classi<sup>fi</sup>cation Using Machine Learning Techniques, Proceedings of the ACL-02 Conference on Empirical Methods in Natural Language Processing, Vol. 10, 2002, pp. 79–86.

[25] J. Roed, Language learner behavior in a virtual environment, Computer Assisted Language Learning 16 (2–3) (2003) 155–172.

[26] J. Rowley, R. Hartley, Organizing Knowledge: An Introduction to Managing Access to Information, Fourth edition, Ashgate, 2008.

[27] I. Steinwart, A. Christmann, Support Vector Machines, Springer, 2008.

[28] I. Tsochantaridis, T. Joachims, T. Hofmann, Y. Altun, Large margin methods for structured and interdependent output variables, Journal of Machine Learning Research 6 (Sep 2005) 1453–1484.

[29] P.D. Turney, Thumbs Up or Thumbs Down? Semantic Orientation Applied to Unsupervised Classi<sup>fi</sup>cation of Reviews, Proceedings of the 40th Annual Meetin of the Association for Computational Linguistics, 2002, pp. 417–424.

[30] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4) (1996) 5–33.

[31] J. Weston, C. Watkins, Multi-class Support Vector Machines, Technical Report CSD-TR-98-04, University of London, Department of Computer Science, Royal Holloway, 1998.

[32] M. Zhang, X. Ye, A Generation Model to Unify Topic Relevance and Lexicon-based Sentiment for Opinion Retrieval, Proceedings of the 31st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 2008, pp. 411–418.

[33] W. Zhang, C. Yu, W. Meng, Opinion Retrieval from Blogs, Proceedings of the sixteenth ACM Conference on Conference on Information and Knowledge Management, 2007, pp. 831–840.

[34] Z. Zhang, B. Varadarajan, Utility Scoring of Product Reviews, Proceedings of the 15th ACM international Conference on Information and Knowledge Management, 2006, pp. 51–57.

[35] X. Zhu, S. Gauch, Incorporating Quality Metrics in Centralized/Distributed Information Retrieval on the World Wide Web, Proceedings of the 23rd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 2000, pp. 288–295

![](/api/attachments/M9692CHG/fulltext/images/23086080f9c936da3873cad8efc75a918b92bb1314e0ab09c19b723cc7d34e24.jpg)

Chien Chin Chen received his B.S. and M.S. degrees in Computer Science and Information Engineering from National Central University, Taiwan, in 1997 and 1999, respectively. Then he joined the Institute of Information Science at Academia Sinica Taiwan as a research assistant and participated several research projects in the area of text mining. In August 2003, he began his Ph.D. program and received his Ph.D. degree in Electrical Engineering from National Taiwan University, Taiwan, in 2007. He is currently an assistant professor of the department of Information Management at National Taiwan University. His papers have appeared in ACM Transactions on Information Systems (TOIS), ACM SIGIR, ACM SIGKDD,

etc. His current research interests include text mining, information retrieval, knowl edge discovery, and data mining.

![](/api/attachments/M9692CHG/fulltext/images/4463b7f0d5e5346313957b93ec17feb02ada113f69a8a3d77e4db4d941c60873.jpg)

You-De Tseng received his M.S. degree in Information Management from National Taiwan University, Taiwan, in 2009. His current research interests include opinion mining, information quality evaluation, and text mining.
