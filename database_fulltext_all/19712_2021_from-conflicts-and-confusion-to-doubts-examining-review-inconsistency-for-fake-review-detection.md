---
otero_id: 19712
otero_key: "VB8FMHMP"
title: "From conflicts and confusion to doubts: Examining review inconsistency for fake review detection"
authors: "Guohou Shan; Lina Zhou; Dongsong Zhang"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113513"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# From conflicts and confusion to doubts: Examining review inconsistency for fake review detection

![](/api/attachments/VB8FMHMP/fulltext/images/abe7b55af23461223edb5e30b841175a55e2013de704ff5b2436f7a0afe10772.jpg)

Guohou Shan <sup>a,\*</sup>, Lina Zhou <sup>b</sup>, Dongsong Zhang b

<sup>a</sup> Fox School of Business, Temple University, 1801 Liacouras Walk, Philadelphia, PA 19122, USA <sup>b</sup> Department of Business Information Systems and Operations Management, The University of North Carolina at Charlotte, 9201 University City Blvd, Charlotte, NC 28223, USA

## A R T I C L E I N F O

Keywords: Online consumer reviews (OCRs) Review inconsistency Fake review detection Sentiment analysis

## A B S T R A C T

Inconsistency in online consumer reviews (OCRs) may cause uncertainty and confusion to consumers when they make purchase decisions. However, there is a lack of a systematic and empirical investigation of review inconsistency in the literature. This research characterizes review inconsistency from multiple aspects, including rating-sentiment, content, and language, and proposes hypotheses about their effects on fake OCR detection by drawing upon deception and attitude-behavior consistency theories. We characterize review inconsistency with 22 features, and test the hypotheses with machine learning models developed for fake OCR detection. Our empirical evaluation results using real OCRs not only confirm the presence of review inconsistency, but also demonstrate significant positive effects of review inconsistency on the performance of fake OCR detection. The research findings have important implications for improving the effectiveness of consumer decision making and the trustworthiness of OCRs

## 1. Introduction

An online consumer review (OCR) typically consists of a star rating and a textual comment on a product (referred to as content hereafter). A star rating, normally ranging from one to five stars, reflects a consumer’s overall experience with a target product or service, and review content provides an elaborated narrative. As a source of third-party product information, OCRs can help prospective customers reduce product un certainty or increase confidence in making purchase decisions [12]. However, this may not always be the case. Take the following three OCRs on Yelp.com as examples. They all share the same star rating of one, but differ in their opinions by providing mixed, extremely negative, and negative content, respectively:

A: “Positives- Great decor and ambiance. Not crowded, servers try hard. Negs- wine list insultingly expensive, portions small, prices really big. Organic steak consisted of about 4 oz piece and 1/3 fat and gristle. Chef should not have sent out for \$45.”

B: “Horrible service, bad food, mediocre drinks.”

C: “My friends and I drove up to Cardiff to find a quiet restaurant for dinner without any groupons, coupons or high expectations. When we entered, there were 6 people in a restaurant that appeared to seat well over 100. We thought we would try it in spite of the initial impression. With all due respect it may have been the worst meal we have had in 10 years. I would hope the owner reads these reviews because there is a common thread with all the yelps. "You are dying on the vine." Servers try real hard and do a very nice job. However, the big screens, the jazz, the groupons and coupons are all signs of desperation. Do the right thing, either quit or get food in there that is at the very least digestable [digestible]. Again this is not meant to be an insult as much as a wake up call from the obvious state of denial.”

A prospective consumer who reads the above three OCRs can easily get confused. The confusion could come from different sources: 1) the discordance between the rating and review content sentiment (i.e., positive or negative) of the same OCR (e.g., A); 2) the difference in content features (e.g., noun, verb, and adverb counts) of different OCRs on the same restaurant at the same geolocation with the same rating (e. g., review A contains 14 nouns and 5 verbs, and B contains 3 nouns and 0 verbs); and 3) the difference in the language style (e.g., review length and lexical diversity) among different OCRs from the same reviewers (e. g., review length and lexical diversity of A are 41 and 0.95, respectively, while those of B are 157 and 0.71, respectively). Consequently, they may hamper, rather than facilitate, a prospective consumer in making a product assessment or choice.

We refer to review inconsistency as the state of being inconsistent or conflict in an OCR, where different parts of an OCR or different OCRs are in disagreement with one another with respect to certain dimension(s) of OCRs. While browsing an OCR, consumers tend to check both its rating and content [2]. Specifically, an OCR with a high star rating and positive content are likely to induce positive perceptions of a target product. In contrast, an OCR with a low star rating and negative content may reduce consumers’ desire to purchase [68]. Therefore, understanding review inconsistency and its potential impacts on OCR credibility is instru mental to helping potential consumers perceive the quality of the target product.

In this research, we propose and categorize 22 review inconsistency features into three types (rating-sentiment inconsistency, content inconsis tency, and language inconsistency) from the star rating, review content, and language style aspects. Rating-sentiment inconsistency reflects the deviation between star ratings and content sentiments of the same OCRs; content inconsistency (e.g., inconsistencies in noun and verb counts) assesses the differences in review content features among different OCRs of the same star rating on the same products; and language inconsistency (e.g., inconsistencies in lexical validity and linguistic diversity) is manifested by the differences in language styles among different OCR of the same star rating from the same reviewer.

Fake OCRs, which contain intentionally manipulated or fabricated information to mislead consumers, pose significant challenges to the credibility of OCRs. They are often written by reviewers who may not actually have product purchasing or usage experiences [68]. It is esti mated that approximately 20–25% of OCRs on almost every OCR plat form are fake [68]. Unfortunately, the accuracy of manual detection of fake OCRs by consumers is considerably low [68]. In the past decade, there have been increasing efforts toward developing methods for automatic detection of fake OCRs based on the characteristics of re viewers, review content, star ratings, and target products [45,49,50]; however, none of the previous studies has focused on the impact of re view inconsistency on fake OCR detection. In particular, there is a lack of theoretical understanding and empirical evidence for the role of review inconsistency in fake OCR detection.

This study fills the above-mentioned literature gaps by examining review inconsistency and its role in the context of fake OCR detection. Specifically, we aim to answer two main research questions: 1) how prevalent is review inconsistency? and 2) does review inconsistency contribute to fake OCR detection? To answer these questions, this research conceptualizes review inconsistency in three dimensions, including rating-sentiment, content, and language style, proposes new measures of review inconsistency, provides empirical evidence for the existence of review inconsistency, and evaluates the impact of review inconsistency on fake OCR detection. Our findings show that all three types of review inconsistency exist in OCRs. By comparing review inconsistency between fake and authentic OCRs, we find that ratingsentiment inconsistency and most of the content inconsistency and language inconsistency features are more salient in fake OCRs than in authentic OCRs. These findings demonstrate that review inconsistency in fake OCRs is generally greater than that in authentic OCRs. Besides, incorporating the proposed review inconsistency features into fake OCR detection models significantly improves model performance.

This study makes several novel research contributions. First, we propose three types of review inconsistency, and empirically validate their presence in OCRs. Second, this study is the first effort to adapt the leakage theory of deception [15], Truth-Default Theory [39], and Attitude-behavior consistency theory [18] to explain the effect of review inconsistency on fake OCR detection. Third, this study proposes and validates the incorporation of review inconsistency features to improve automatic fake OCR detection. This research study offers new research and practical insights for improving fake OCR detection through probing review inconsistency.

The rest of this paper will be organized as follows. We first review related work and develop research hypotheses. Then, we introduce the overall design of a proposed fake OCR detection system that in corporates review inconsistency features. Next, we describe the evaluation of the performance of the fake OCR detection models, and examine the importance of each type of review inconsistency features. Finally, we discuss research findings, contributions, practical implica tions, and limitations of this research.

Table 1  
A summary of four types of sentiment analysis methods.

<table><tr><td>Types</td><td>Strengths</td><td>Weaknesses</td></tr><tr><td>Lexicon based</td><td>It is simple and easy to use; Labeled data and training are not needed</td><td>Pre-defined lexicons are not always available</td></tr><tr><td>Machine learning based</td><td>It doesn’t require dictionaries</td><td>Is domain specific; sometimes labeled data are difficult to acquire.</td></tr><tr><td>Statistics based</td><td>It is easy to implement</td><td>Provides little linguistic insight</td></tr><tr><td>Rule-based</td><td>It has high performance at review and sentence levels</td><td>Efficiency and accuracy depend on the defined rules</td></tr></table>

## 2. Related work

Existing studies have explored a variety of factors in the ecosystem of OCRs. Among them, star ratings and review content have been studied the most.

## 2.1. Star rating

Research on star ratings of OCRs mainly focuses on their associations with product sales, review quality, and rating-giving behavior. Online star ratings have been found to affect hotel booking behavior, review helpfulness, product value, and subsequent ratings, etc. [23,29,47]. For example, Hu and Chen [29] suggested considering OCR visibility and the interaction between star ratings and hotel ratings as new predictive features of review helpfulness. They built fake OCR detection models using decision tree, linear regression, and support vector regression al gorithms and hotel reviews collected from TripAdvisor.com. The eval uation results confirmed the effectiveness of the new features in predicting review helpfulness. Studies on rating-giving behaviors try to understand how ratings are generated and motivating factors of ratinggiving behaviors from different aspects [17,38,60]. For example, a study found that online book ratings were socially nudged [60] — similarity of ratings among reviewers became significantly higher after they formed friend relationships.

## 2.2. Content sentiment

Sentiment Analysis is the process of extracting and analyzing senti ments from text [43]. It has been widely used to explore consumers attitude or emotions toward products via OCRs [20]. The methods of sentiment analysis can be broadly categorized into four types: lexicon, machine learning, statistics, and rule-based approaches [10,55].

A lexicon-based approach to sentiment analysis utilizes sentiment lexicons to identify sentiment polarity of text. A machine learning based method utilizes supervised machine learning models trained on labeled datasets to predict sentiment labels for target text [70]. A statistics based method for sentiment analysis treats each OCR as a combination of a star rating and the latent aspects extracted from review content [10]. Both star ratings and extracted latent aspects are assumed to follow multi nomial distributions [10]. Latent aspects of review content can be automatically learned by methods such as Latent Dirichlet Allocation Then, statistical models, such as Hidden Markov Model, will be trained on labeled data for classifying the polarity of text [13]. A rule-based approach first looks for words in OCRs that express opinions based on predefined rules, then determines the sentiment polarity by aggregating sentiment words associated with opinions [31]. Table 1 summarizes the strengths and weaknesses of those four approaches.

## 2.3. Content and language style features

Content and language style features (e.g., linguistic features) of OCR content have been widely used to predict review helpfulness [30,48,56,63]. For instance, Singh et al. [56] used linguistic features of review content, such as review polarity and readability, to build a gradient boosting machine learning (ML) model for predicting review helpfulness. Huang et al. [30] suggested that review length, not reviewer experience, would be associated with review helpfulness. Yin and Zhou [35] showed that review breadth and depth had positive effects, while review content redundancy had a curvilinear effect, on review helpful ness. Content and language style features have also been employed for fake OCR detection, which will be reviewed in the next subsection.

It is worth noting that a few studies have explored the relationships between star ratings and review content [9,28]. For example, Yu et al. [67] utilized review content to predict star ratings. Hu et al. [27] found that star ratings had an indirect, instead of a direct, effect on sales through content sentiments. Other studies used a combination of review content and star ratings to explain or predict review helpfulness and product sales [8,21]. However, none of them has empirically investi gated content and language style inconsistencies.

## 2.4. Fake review detection

Fake OCRs consist of fabricated content written by reviewers who intend to mislead consumers. Therefore, the credibility of OCRs is fundamentally threatened by fake OCRs [45]. Based on the techniques used, current approaches to automatic fake OCR detection can be clas sified into two main categories: machine learning and non-machine learning based. Up to date, fake OCR detection has been dominated by the former method. Supervised ML methods treat it as a binary classi fication problem to determine whether an OCR is fake or authentic. Traditional supervised ML techniques, such as Naïve Bayes (NB) and Support Vector Machine (SVM), typically represent OCRs with engi neered features (e.g., linguistic features of textual content of OCRs). For example, Ott et al. [53] built NB and SVM models for fake OCR detection using Linguistic Inquiry and Word Count (LIWC) categories, Parts-of-Speech (PoS), unigrams, bigrams, and trigrams as predictive features, and tested them on a dataset collected from Amazon Mechanical Turk ers. Mukherjee et al. [50] constructed SVM models for fake OCR detection by using unigrams and bigrams as input features. Their dataset was collected from Yelp.com.

In recent years, researchers started exploring deep learning model (e.g., Fusion Convolutional Attention Network (FCAN), Pre-training of Deep Bidirectional Transformers (BERT), and Convolutional Neural Network (CNN)) for fake OCR detection that represent OCRs using word embeddings. For example. Li et al. [41] proposed FCAN by incorporating user-level information (e.g., users’ registration time, the number of re views, and review length) into the OCR word embedding to detect opinion spams. The rationale of their method was that spammers and non-spammers differ in their preferences in review content and their behavior because they generate OCRs for different purposes. Their experimental results with Yelp and mobile01 data showed that FCAN worked better than the state-of-the-art methods. Kennedy et al. [36] examined the performance of Bidirectional Encoder Representations from Transformers (BERT), traditional ML models (e.g., SVM), and classic deep learning models (e.g., CNN) in detecting fake OCRs. They found that a fine-tuning BERT model was competitive with the state-ofthe-art methods using Yelp and OpSpam datasets. Hajek et al. [25] built two deep neural networks (CNN and deep feed-forward neural network (DFFNN)) for fake OCR detection using OCR representations that considered the semantic meanings and emotions of textual content, such as n-grams, word embedding, and various lexicon-based emotion in dicators. Their experimental results confirmed that both CNN and DFFNN outperformed the state-of-the-art methods on four OCR datasets.

An unsupervised machine learning method (e.g., clustering) does not require labeled training data [68]. It learns an automatic model based on the characteristics of training dataset inputs. Specifically, unsupervised machine learning finds patterns from input data, then uses the learned patterns to automatically predict the class of a sample. For example, Lim et al. [42] detected fake OCRs or OCR spammers based on their behavioral characteristics (e.g., deviating from other reviewers in product ratings on the same products). Mukherjee et al. [49] proposed an unsupervised author spamicity model to detect fake OCRs based on reviewers’ behavioral footprints.

Non-machine learning techniques have also been explored for the detection of fake OCRs, such as graph modeling and pattern matching [68]. Graph modeling builds a heterogeneous graph that represents the interaction relations among reviewers, reviews, and stores to detect fake OCRs [61]. The underlying rationales for this modeling approach are as follows: a reviewer is more likely to be honest if he or she has written a larger number of authentic OCRs; a store is more likely to be trustworthy if there are more authentic OCRs about it from honest reviewers; and an OCR tends to have higher probability of being authentic if it receives more support from honest reviewers. However, the graph modeling method does not consider any review content features or review inconsistency. Pattern matching leverages review content similarity in detecting fake OCRs [32], given the assumption that reviewers tend to fabricate OCRs with similar content or follow certain rules when fabri cating fake OCRs [40]. However, the usefulness and effectiveness of the pattern matching method is limited to some specific OCR scenarios (e.g., detecting OCR spams) [68].

Building machine learning based fake OCR detection models require the selection of input features. The sources of input features may include review content, star rating, reviewer, and product features, among others [68]. Although it is not easy to distinguish fake OCRs from authentic ones, studies have shown that subtle linguistic features extracted from review content (e.g., diversity, writing style, and read ability) may be helpful [3,51,68]. Input features have also been derived from star ratings, such as rating deviation and variance scores [51,65]. Reviewer features characterize the authors of OCRs, such as review frequency (e.g., the average number of reviews posted per day) [49,51], vote count, and whether a personal picture is provided in a user profile [34]. Finally, product features describe the attributes and/or compo nents of target products such as product type and selling price [32,49]. Among different sources of input features for building fake OCR detec tion models, review content and star rating are most frequently used. However, none of previous studies has examined the role of review inconsistency in detecting fake OCRs, especially from rating-sentiment, content, and language style aspects.

## 3. Research hypotheses

Based on our conceptualization of review inconsistency in the Introduction Section, we propose the following three types of review inconsistency:

• Rating-sentiment inconsistency refers to the inconsistency between star ratings and content sentiments of the same OCRs [19].

• Content inconsistency refers to the inconsistency among the content of different OCRs with the same star rating on the same product.

• Language inconsistency refers to the inconsistency in language style among different OCRs with the same star rating from the same reviewer.

Star ratings can be influenced by many factors, such as customers pre-purchase expectations, product performance [17], herding behavior [38], and friendship network [60]. Thus, despite the same star rating, different or even the same reviewers may express different rationales and sentiments about a product in review content. Therefore, we make the following proposition:

![](/api/attachments/VB8FMHMP/fulltext/images/9af02df59477947a93891ac9a41e34c238becf71367de4bffdd5a081bddbe361.jpg)  
(a) Authentic OCRs

![](/api/attachments/VB8FMHMP/fulltext/images/2a920cf68f7f2d3c931e68683410f94fdaf083919a1f7866dba6f222aafe9c15.jpg)  
(b) Fake OCRs  
Fig. 1. Distributions of OCR counts by reviewers.

Proposition. There exists review inconsistency, including rating sentiment inconsistency, content inconsistency, and language inconsis tency, in OCRs.

Despite preliminary evidence of rating-sentiment inconsistency [19], other types of review inconsistency remain unexplored, especially in the context of fake OCR detection. Fake OCRs can be considered as a type of deception [68]. Truth-Default Theory [39], a theory of deception, posits two types of consistency for distinguishing truthful messages from deceptive ones: correspondence and coherence [39]. Correspondence refers to the criterion that description (e.g., review content) should correspond to facts, and coherence refers to the criterion that description should not contain claims that are logically inconsistent with each other. The theory emphasizes contextualized communication content. Depending on the context of communication content in OCRs, such as within an OCR, across different OCRs with the same star rating on the same product, and across different OCRs with the same star rating from the same reviewers, review inconsistency is manifested as ratingsentiment inconsistency, content inconsistency, and language inconsis tency in this study. All those different types of inconsistency violate the coherence principle of truth.

The correspondence principle suggests that the two parts of the same OCRs, namely content and rating, are expected to be logically consistent, instead of contradicting, with each other. Fake reviewers may use different strategies when fabricating OCRs. For example, they may uti lize extreme ratings (e.g., one or five stars) to attract the attention of potential consumers yet express neutral or opposite sentiments in the review content. Therefore, we expect that both rating-sentiment and content inconsistencies are higher in fake OCRs than in authentic OCRs.

Attitude-behavior consistency theory posits that people’s attitudes determine their behavior [18,57]. A star rating manifests a consumer’s general attitude toward a product, and review content is the outlet for the consumer to display his/her verbal behavior [68]. Accordingly, when a consumer gives the same star rating to different products, he/she is expected to display consistent verbal behavior (e.g., linguistic fea tures) across different review content. However, fake OCR reviewers have different motivations and may use different strategies to make up for their lack of actual experience and knowledge with target products [6]. For instance, they may copy other consumers’ OCRs on the same products or use similar yet irrelevant content such as OCRs of other products. In the meantime, they may manipulate star ratings to draw initial attention. Those behaviors will lead to language inconsistency. Thus, we predict that all of the three types of review inconsistency are more likely to appear in fake OCRs than in authentic OCRs. Thus, we propose our first hypothesis as follows:

Hypothesis H1. Fake OCRs show greater a) rating-sentiment incon sistency; b) content inconsistency; and c) language inconsistency than

authentic OCRs.

Discrepancy is consistently and positively correlated with deception [71]. Deceptive communication generally appears to be more discrepant and inconsistent than truthful communication. Studies suggest that deception would result in cross-modal discrepancies in impressions of agreeableness, which are related to the judgement of deception [26]. Researchers have considered both verbal (e.g., lexical diversity of re view content) and non-verbal features (e.g., # of voted “likes” and reviewer characteristics such as posting frequency and interaction behavior features) when building models for fake OCR detection [68]. Research has shown that people can hide their emotions in verbal behavior [14]. Leakage of concealed signs of emotions in nonverbal behavior can reveal deception intention due to its contradiction to verbally claimed emotions [14]

The design and production of deception follows a variety of information manipulation strategies [46]. Information quality is also one of the key dimensions of information manipulation [46]. Information quality of OCRs is determined by the aspects of information contained in OCRs that are important to consumers [35]. In addition to intrinsic quality such as believability, reputation, and objectivity, representa tional quality is another dimension of information quality [62]. Incon sistent representations of OCRs across different modalities or reviews could indicate information manipulation. Therefore, review inconsis tency is expected to contribute to the detection of fake OCRs. We pro pose the following second hypothesis:

Hypothesis H2. Incorporating a) rating-sentiment inconsistency; b) content inconsistency; and c) language inconsistency will improve the performance of fake OCR detection models.

## 4. Method

## 4.1. Dataset

When building fake OCR detection models, acquiring labeled re views is often a major challenge. Many prior studies used pseudo-fake OCRs [51,66], which were either manually annotated [64] or gener ated by AMT [53]. Human labeling is known for not having high accu racy because fake OCRs are produced by mimicking the content and style of authentic OCRs and consequently are very difficult to identify. Also, Amazon Mechanical Turkers usually do not have the same moti vations, psychological minds, and behaviors as real fake reviewers of OCRs [51]. As a result, using pseudo-fake reviews to construct models for fake OCR detection may be inaccurate or not perform well in detecting fake OCRs in real-life settings [51].

To address the above-mentioned concerns, we collected real-world fake and authentic OCRs from Yelp.com, which had more than 178 million unique visitors from 32 countries per month on average in 2020. The platform deploys its own OCR filtering process that puts fake and authentic OCRs into different categories [51,68]. The class labels pro vided by the platform are considered accurate, reliable, and highly close to real-life OCR labels [50,51]. In our research, 24,539 labeled restau rant OCRs were collected from Yelp.com, including information about both reviewers and OCRs, such as reviewer id, star ratings, review content, and review labels. Among them, 11,641 were authentic and 12,898 were fake. In the dataset, there were 1,577 reviewers who posted more than one OCR. The distributions of reviewer count for the top 30 most frequent OCR counts are plotted in Fig. 1. The figure demonstrates that among all reviewers who posted fake OCRs, all but 300 posted two or more OCRs. Among all reviewers who posted authentic OCRs, all but 135 posted two or more OCRs, laying the ground for examining lan guage inconsistency in this study.

![](/api/attachments/VB8FMHMP/fulltext/images/0761f8db5b02e844b95f02a2d5380a16a738965f8c992e3ef20463ef834c4e3c.jpg)  
Fig. 2. The overall design of the fake OCR detection system.

## 4.2. System design: Fake OCR detection

The overall design of our proposed fake OCR detection system, as depicted in Fig. 2, consists of four main components: feature extraction, review inconsistency analyses, model development, and sensitivity analysis. For each OCR, the key outputs of feature extraction include sentiments, content, and language style features. First, we performed review-level sentiment analysis and review content feature extraction. Then, we extracted the three types of review inconsistency features, as introduced in Section 3. Those extracted features along with the star rating and nonverbal features served as the inputs for developing fake OCR detection models. Finally, we conducted sensitivity analyses using the developed models to discover the importance of individual features. We will introduce the system design in detail in the remainder of this section.

## 4.2.1. Sentiment analysis

In this study, we adopted a lexicon-based method to extract senti ments from the content of OCRs. There are a large number of sentiment lexicons available, such as LIWC [59] and SentiWordNet 3.0 [1]. We selected SentiWordNet 3.0 due to its high accuracy [54].

The procedure for content sentiment analysis consisted of four main steps: preprocessing, sentiment term extraction, sentiment score calcu lation, and sentiment score aggregation. The pre-processing in turn consisted of the following processes: tokenization $( \mathrm { i . e . } ,$ , transforming review text into tokens (words)), lemmatization (i.e., converting words into their meaningful base forms), PoS tagging (i.e., assigning syntactic tags to individual words), and term filtering (e.g., selecting adjectives, adverbs, verbs, and nouns from the words). The sentiment scores of the identified terms were calculated based on the SentiWordNet 3.0 lexicon.

Table 2  
The selected content features and their descriptions.

<table><tr><td>Feature Types</td><td>Feature</td><td>Description</td></tr><tr><td rowspan="6">Content</td><td>Noun count</td><td>Total number of nouns</td></tr><tr><td>Verb count</td><td>Total number of verbs</td></tr><tr><td>Personal pronoun count</td><td>Total number of personal pronouns</td></tr><tr><td>Pronoun count</td><td>Total number of pronouns</td></tr><tr><td>Adverb count</td><td>Total number of adverbs</td></tr><tr><td>Adjective count</td><td>Total number of adjectives</td></tr><tr><td rowspan="15">Language style</td><td>Review length</td><td>Total number words</td></tr><tr><td>Average sentence length</td><td>Average word count per sentence</td></tr><tr><td>Noun ratio</td><td>Ratio of noun count to review length</td></tr><tr><td>Subjectivity</td><td>Percentage of subjective word count to objective word count</td></tr><tr><td>Lexical validity</td><td>Percentage of misspellings</td></tr><tr><td>Sentiment</td><td>Sentiment score of an OCR</td></tr><tr><td>Sentiment orientation</td><td>Percentage of sentiment indicators in an OCR</td></tr><tr><td>Lexical diversity</td><td>Unique word count/Review length</td></tr><tr><td>Linguistic diversity</td><td>Unique noun and verb counts/total noun and verb counts</td></tr><tr><td>PoS (part of speech) bigram diversity</td><td>Unique PoS bigrams/total PoS bigrams</td></tr><tr><td>Capitalized diversity</td><td>Percentage of word tokens with initial capital letter(s) to all token count</td></tr><tr><td>Emotiveness diversity</td><td>Adjective and adverb counts/total noun and verb counts</td></tr><tr><td>Self-reference diversity</td><td>Number of first-person pronoun word count/ number of all pronoun word count</td></tr><tr><td>Average content similarity</td><td>Average content similarity of OCRs written by the same reviewer</td></tr><tr><td>Redundancy</td><td>Repeated token count/total token count</td></tr></table>

Subsequently, the overall sentiment score of an OCR was derived as an aggregation of the sentiment values of individual terms in the sentiment score aggregation component.

## 4.2.2. Content feature extraction

We selected features from the content of OCRs based on findings of the related study [68]. We further grouped those features into content and language style categories, as shown in Table 2.

## 4.2.3. Review inconsistency analysis

This step focused on analyzing three types of review inconsistencies, namely rating-sentiment inconsistency, content inconsistency, and lan guage inconsistency. The rating-sentiment inconsistency was defined as the absolute difference between content sentiment and star rating of the same OCR (see Eq. 1).

$$
\left\{ \begin{array}{c} r a t i n g \_ s e n t i \_ i n c o n ^ {j} = | z \_ r a t i n g ^ {j} - z \_ s e n t i ^ {j} | \\ z \_ r a t i n g ^ {j} = \frac {r a t i n g ^ {j} - \overline {{r a t i n g}}}{\sigma_ {r a t i n g}} \\ z \_ s e n t i ^ {j} = \frac {s e n t i ^ {j} - \overline {{s e n t i}}}{\sigma_ {s e n t i}} \end{array} \right.\tag{1}
$$

where rating\_senti\_incon<sup>j</sup> indicates rating-sentiment inconsistency of the jth OCR; z\_rating<sup>j</sup> and z\_senti<sup>j</sup> represent the z-scores of the rating and sentiment of the jth OCR, respectively; rating and senti denote the mean values of ratings and sentiments of OCRs of the same products, respec tively; rating<sup>j</sup>and senti<sup>j</sup> indicate the rating and sentiment of the jth OCR, respectively; and $\sigma _ { r a t i n g }$ and $\sigma _ { s e n i }$ denote the standard deviations of rat ings and sentiment scores for a group of OCRs, respectively. In other words, the sentiment and rating were both normalized as z-scores.

Content inconsistency was operationalized as the content deviation of a target OCR from the average content of all OCRs on the same product with the same star rating (see Eq. 2). In view of the strong effect of geographic locations on restaurant ranking [33], we selected OCRs from the same geographic location in deriving the means. We measured

Table 3  
A list of non-verbal features and their descriptions.

<table><tr><td>Features</td><td>Description</td></tr><tr><td>Duplicated reviews (0/1)</td><td>Review content that is more than 95% similar to the content of any other reviews on the same product (Y/N)?</td></tr><tr><td>Membership length</td><td>Yelp membership length in terms of months</td></tr><tr><td>Elite reviewer term</td><td>Number of years of being an ‘elite’ reviewer</td></tr><tr><td>Tip count</td><td>Tip count</td></tr><tr><td>Photo count</td><td>Number of photos in an OCR</td></tr><tr><td>List count</td><td>The number of hyperlinks in an OCR</td></tr><tr><td>Blog link (Y/N)</td><td>A binary variable, indicating whether a blog link is embedded in an OCR</td></tr><tr><td>Review count</td><td>Review count</td></tr><tr><td>Maximum posting rate</td><td>Maximum review count posted per day</td></tr><tr><td>Average posting rate</td><td>Average review count posted per day</td></tr><tr><td>Review updates</td><td>Review update count</td></tr><tr><td>First review</td><td>First review count posted for any product</td></tr><tr><td>Positive ratio</td><td>Positive review count/total review count</td></tr><tr><td>Positive-to-negative ratio</td><td>Review count with ratings 4 or 5 /review count with ratings 1 or 2</td></tr><tr><td>Review duration</td><td>Days between the posting dates of the first and the last OCRs</td></tr><tr><td>Review burstiness</td><td>Logarithm of the probability distribution of post frequency over time</td></tr><tr><td>Check-ins</td><td>Check-in count of a reviewer at the same place</td></tr><tr><td>Maximum check-ins</td><td>Maximum check-in count at a certain place</td></tr><tr><td>Total check-ins</td><td>Check-in count in total</td></tr><tr><td>Vote count</td><td>Total number of votes cast on an OCR</td></tr><tr><td>Useful, funny, cool votes</td><td>The numbers of useful, funny, cool votes on an OCR, respectively</td></tr><tr><td>Friend count</td><td>The number of friends of a reviewer</td></tr><tr><td>Follower count</td><td>The number of followers of a reviewer</td></tr><tr><td>Compliment count</td><td>The number of compliments that a reviewer has received</td></tr></table>

$$
c o n t e n t \_ i n c o n _ {i} ^ {j} = \frac {\left| f _ {i} ^ {j} - \overline {{f}} _ {i} \right|}{\sigma_ {i}}
$$

content inconsistency via six content features such as noun count and pronoun count (see Table 2).

(2)

where content\_incon<sup>j</sup> represents a cross-content inconsistency feature (e. g., Noun count) of the jth OCR with rating i; f<sup>j</sup>denotes a content feature f calculated by the feature occurrence (e.g., noun) count in the jth OCR with star rating i; f and σ denote the mean and standard deviation of f across all reviews with star rating i, respectively.

Language inconsistency was operationalized as the absolute devia tion of the language style of a target OCR from the mean of language style of all OCRs with the same star rating from the same reviewer, as shown in Eq. 3. The language inconsistency was measured by 15 features such as review length and noun ratio (see Table 2).

$$
l a n g u a g e \_ i n c o n _ {i} ^ {j} = \frac {\left| f _ {i} ^ {j} - \overline {{f}} _ {i} ^ {\prime} \right|}{\sigma_ {i} ^ {\prime}}\tag{3}
$$

where language\_incon<sup>j</sup> represents a reviewer language style inconsistency feature (e.g., noun ratio) of the jth OCR with rating i, and ${ \overline { { f _ { i } } } ^ { \prime } }$ and σ <sup>′</sup>denote the mean and standard deviation of f across all OCRs with star rating i from the same reviewer, respectively. If there is no presence of incon sistency in an OCR, the inconsistency measures will be 0. As the degree of inconsistency increases, the values of these measures would get larger.

## 4.2.4. Fake OCR detection

Using the outputs of feature extraction, star rating, as well as nonverbal features (see Table 3) used in a previous study [68] as the inputs, we developed fake OCR detection models using several classifi cation techniques, including SVM, NB, Classification and Regression Trees (CART), Random Forest (RF), and Multi-Layer Perceptron Neural Network (MLPNN), because those techniques have been frequently used in previous fake OCR detection studies $[ 7 , 6 8 ] \colon$

• SVM, a kernel method, classifies OCRs using different separating hyper-planes [3].

• NB uses the Bayes’ theorem to distinguish different classes [69].

• The CART algorithm adopts a tree structure that splits a node into two child nodes repeatedly based on information gains until reaching a pre-defined termination condition [68]. In the tree structure, each fork represents a split in the values of a predictive variable, and each terminal node denotes a prediction of the target variable.

• RF is an ensemble classifier that consists of a group of decision trees trained on labeled datasets and an ensemble of the decision trees is in turn used to make predictions [5].

• MLPNN is the most commonly used feedforward neural network classifier [52].

We did not consider deep neural network models with word em beddings in this study primarily because the primary objective of this research was to examine the impacts of review inconsistency features on fake OCR detection. The latent word embedding representation of OCR and the black-box nature of deep learning models do not serve that goal well.

## 4.2.5. Sensitivity analysis

Sensitivity analysis (SA) can be used to identify the relative impor tance of individual features to fake OCR detection models [68]. Different methods for sensitivity analysis have been proposed. For example, postmodeling sensitivity analysis calculates the relative feature importance through a backward feature elimination process where the reduced estimation error of a specific feature is considered as its relative importance [68]; One-dimensional SA (1D-SA) examines model perfor mance change by varying one input feature at a time while holding the remaining ones at their average values [37]. Two-dimensional sensi tivity analysis, an extension of 1D-SA, investigates model performance change by varying any two features at a time while holding the remaining features at their average values [16]. Cortez and Embrechts [11] proposed three different methods: Data-based SA (DSA). Monte Carlo SA (MSA), and Cluster-based SA (CSA). DSA is similar to 1D-SA, but takes multiple random samples from the original dataset to calcu late the sensitivity of one input feature. MSA is similar to DSA except that the randomly selected samples are built by Monte-Carlo simulation, following the uniform distribution. CSA first generates different sample clusters based on the value segments of an input feature, then calculates the sensitivity (relative importance) of that feature within a specific cluster.

Because post-modeling sensitivity analysis has been commonly used to analyze the feature sensitivity and importance to adapted machine learning models in Management Information Systems literature [4,24,58,68], we used it to conduct a sensitivity analysis in this study. Specifically, we used the VarImp function provided in the caret package of R to implement the sensitivity analysis in this research.

## 5. Evaluation

The performance metrics for assessing fake OCR detection models included accuracy (A), precision (P), recall (R), and F-score (F) [7]. Accuracy was defined as the ratio of the number of correctly classified fake and authentic OCRs to the total number of OCRs (see Eq. (4)). Precision was defined as the percentage of identified fake OCRs that were truly fake (see Eq. (5)), and recall (see Eq. (6)) was the percentage of correctly identified fake OCRs among all of the fake OCRs in a dataset. F-measure was a metric balancing precision and recall by using their harmonic mean (see Eq. (7)).

$$
A = \frac {t p + t n}{t p + t n + f p + f n}\tag{4}
$$

<sup>\*\*</sup> P < .01.

Descriptive statistics of review inconsistency features and results of one-sample t-test.

<table><tr><td>Inconsistency Features</td><td>Mean</td><td>Std.</td><td>T statistic</td></tr><tr><td>Rating_sentiment_incon</td><td>0.881</td><td>0.675</td><td>453.798***</td></tr><tr><td>Adjective count_incon</td><td>0.641</td><td>0.767</td><td>130.964***</td></tr><tr><td>Personal pronoun count_incon</td><td>0.760</td><td>0.649</td><td>183.414***</td></tr><tr><td>Verb count_incon</td><td>0.697</td><td>0.717</td><td>152.346***</td></tr><tr><td>Pronoun count_incon</td><td>0.768</td><td>0.641</td><td>187.725***</td></tr><tr><td>Adverb count_incon</td><td>0.713</td><td>0.701</td><td>159.267***</td></tr><tr><td>Noun count_incon</td><td>0.691</td><td>0.723</td><td>149.641***</td></tr><tr><td>Sentiment_incon</td><td>0.754</td><td>0.579</td><td>107.857***</td></tr><tr><td>Sentiment orientation_incon</td><td>0.756</td><td>0.576</td><td>108.707***</td></tr><tr><td>Emotiveness diversity_incon</td><td>0.748</td><td>0.586</td><td>105.800***</td></tr><tr><td>Subjectivity_incon</td><td>0.763</td><td>0.566</td><td>111.712***</td></tr><tr><td>Lexical validity_incon</td><td>0.755</td><td>0.577</td><td>108.380***</td></tr><tr><td>Average sentence length_incon</td><td>0.753</td><td>0.580</td><td>107.749***</td></tr><tr><td>PoS n-gram diversity_incon</td><td>0.780</td><td>0.543</td><td>118.976***</td></tr><tr><td>Redundancy_incon</td><td>0.766</td><td>0.563</td><td>112.781***</td></tr><tr><td>Self-reference diversity_incon</td><td>0.781</td><td>0.542</td><td>119.468***</td></tr><tr><td>Noun ratio_incon</td><td>0.703</td><td>0.639</td><td>91.184***</td></tr><tr><td>Capitalized diversity_incon</td><td>0.751</td><td>0.583</td><td>106.861***</td></tr><tr><td>Lexical diversity_incon</td><td>0.784</td><td>0.537</td><td>121.090***</td></tr><tr><td>Review length_incon</td><td>0.787</td><td>0.533</td><td>122.467***</td></tr><tr><td>Linguistic diversity_incon</td><td>0.773</td><td>0.554</td><td>115.528***</td></tr><tr><td>Average content similarity_incon</td><td>0.943</td><td>0.116</td><td>673.361***</td></tr></table>

Note: Std denotes standard deviation.  
Significant at a 0.001 level

$$
P = \frac {t p}{t p + f p}\tag{5}
$$

$$
R = \frac {t p}{t p + f n}\tag{6}
$$

$$
F = \frac {2 P R}{P + R}\tag{7}
$$

where tp (true positive) denotes the number of correctly classified fake OCRs; fp (false positive) denotes the number of authentic OCRs wrongly classified as fake; fn (false negative) represents the number of fake OCRs wrongly identified as authentic; and tn (true negative) indicates the number of correctly identified authentic OCRs.

We adopted the features from a previous study [68] as the baseline features because that study: (1) considered a comprehensive list of verbal and nonverbal input features; (2) represented the start-of-the-art performance in automated fake OCR detection; and (3) used OCRs from Yelp.com as well. Those baseline features are presented in Tables 2 and 3. To evaluate the effects of the proposed review inconsistency features, both individually and as a whole, on the performance of fake OCR detection, we also considered four other feature combinations as model inputs. As a result, we considered the following five input feature settings:

• Baseline features (B0): baseline features only without any review inconsistency features.

• RSI: baseline + rating-sentiment inconsistency feature

• CI: baseline + content inconsistency features

• LI: baseline+ language inconsistency features

• AI: baseline + all of the three types of inconsistency feature combined

The evaluation of model performance was based on 10-fold crossvalidations. Specifically, we ran each fake OCR detection model 10 times, and reported the average performance of the 10 models.

## 6. Analyses and results

In this section, we first verified the presence of review inconsistency.

Table 5  
Descriptive statistics (mean [std]) of content and language inconsistency fea tures for fake and authentic OCRs and results of the MANOVA.

<table><tr><td>Inconsistency Features</td><td>Fake OCRs</td><td>Authentic OCRs</td><td>F statistic</td></tr><tr><td>Adjective count_incon</td><td>0.669 [0.845]</td><td>0.610 [0.669]</td><td>69.836***</td></tr><tr><td>Personal pronoun count_incon</td><td>0.786 [0.677]</td><td>0.732 [0.616]</td><td>3.733</td></tr><tr><td>Verb count_incon</td><td>0.720 [0.728]</td><td>0.672 [0.704]</td><td>18.071***</td></tr><tr><td>Pronoun count_incon</td><td>0.785 [0.660]</td><td>0.749 [0.618]</td><td>24.856***</td></tr><tr><td>Adverb count_incon</td><td>0.744 [0.735]</td><td>0.679 [0.660]</td><td>5.941*</td></tr><tr><td>Noun count_incon</td><td>0.726 [0.779]</td><td>0.652 [0.654]</td><td>10.850**</td></tr><tr><td>Sentiment_incon</td><td>0.749 [0.523]</td><td>0.749 [0.504]</td><td>6.605*</td></tr><tr><td>Sentiment orientation_incon</td><td>0.750 [0.518]</td><td>0.751 [0.506]</td><td>0.247</td></tr><tr><td>Emotiveness diversity_incon</td><td>0.752 [0.528]</td><td>0.741 [0.506]</td><td>6.186*</td></tr><tr><td>Subjectivity_incon</td><td>0.755 [0.510]</td><td>0.755 [0.500]</td><td>3.717</td></tr><tr><td>Lexical validity_incon</td><td>0.760 [0.530]</td><td>0.736 [0.500]</td><td>13.244***</td></tr><tr><td>Average sentence length_incon</td><td>0.752 [0.514]</td><td>0.747 [0.515]</td><td>0.407</td></tr><tr><td>PoS n-gram diversity_incon</td><td>0.771 [0.498]</td><td>0.759 [0.480]</td><td>7.932**</td></tr><tr><td>Redundancy_incon</td><td>0.763 [0.509]</td><td>0.747 [0.499]</td><td>4.733*</td></tr><tr><td>Self-reference diversity_incon</td><td>0.767 [0.490]</td><td>0.769 [0.483]</td><td>0.055</td></tr><tr><td>Noun ratio_incon</td><td>0.721 [0.578]</td><td>0.716 [0.530]</td><td>20.774***</td></tr><tr><td>Capitalized diversity_incon</td><td>0.749 [0.525]</td><td>0.747 [0.505]</td><td>3.874*</td></tr><tr><td>Lexical diversity_incon</td><td>0.768 [0.497]</td><td>0.763 [0.481]</td><td>5.114*</td></tr><tr><td>Review length_incon</td><td>0.770 [0.486]</td><td>0.775 [0.469]</td><td>1.698</td></tr><tr><td>Linguistic diversity_incon</td><td>0.762 [0.502]</td><td>0.766 [0.484]</td><td>0.162</td></tr><tr><td>Average content similarity_incon</td><td>0.945 [0.116]</td><td>0.941 [0.116]</td><td>1.363</td></tr></table>

<sup>\*\*\*</sup> P < .001.  
<sup>\*</sup> P < .05.

Then, we tested hypothesis H1 by performing ANCOVA and MANOVA that treated review inconsistency features as the dependent variable(s) and review veracity (i.e., fake vs. authentic) as the indepdent (or fixed) variable seperately, and tested hypothesis H2 by performing paired sample t-tests on the performances of different fake OCR detection models. Finally, we conducted a sensitivity analysis to rank features in terms of their importance to model performance.

## 6.1. Review inconsistency

To confirm the presence of review inconsistency, we performed a one-sample t-test on each of the review inconsistency features using zero (i.e., no inconsistency) as the hypothesized population mean. The test results are reported in Table 4, which show that all the three types of review inconsistency features had significant presence in OCRs (p < .001).

## 6.2. Comparison of review inconsistency between fake and authentic OCRs

To examine the difference in rating-sentiment inconsistency (RSI) between fake and authentic OCRs, we performed ANCOVA by treating RSI as the dependent variable and review veracity as a covariate. The analysis yielded a significant effect of review veracity on RSI. Specif ically, fake OCRs showed a higher level $( p < . 0 0 1 )$ of RSI (mean = 0.887, std = 0.682) than the authentic counterparts (mean = 0.793, std = 0. 667).

To examine the difference in content inconsistency (CI) and language style inconsistency (LI) between fake and authentic OCRs, we performed MANOVA by treating CI and LI features as dependent variables, and review veracity as independent variable. The descriptive statistic of the CI and LI features of fake and authentic OCRs is reported in Table 5. The analysis vielded signifciant effects of review veracity on all CI features except personal pronoun count $\left( p > . 0 5 \right)$ . Additionally, the analysis yiel ded a significant effect of review veracity on eight LI features such as sentiment\_incon $( p < . 0 5 )$ and emotiveness diversity\_incon $( p < . 0 5 )$ , but did not yield any effect on other LI features such as subjectivity\_incon $( p >$ .05) and review length\_incon $\left( p > . 0 5 \right)$ . For all the CI and LI features that showed significant differences between authentic and fake OCRs, their values were consitently higher for fake OCRs than for authentic OCRs. Therefore, hypothesis H1(a) was supported and H1(b) and H1(c) were partialy supported.

Table 6  
Fake OCR detection performance.

<table><tr><td></td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F-score</td></tr><tr><td colspan="5">(a) Baseline models</td></tr><tr><td>RF</td><td>0.878</td><td>0.871</td><td>0.896</td><td>0.883</td></tr><tr><td>CART</td><td>0.862</td><td>0.853</td><td>0.886</td><td>0.868</td></tr><tr><td>SVM</td><td>0.838</td><td>0.826</td><td>0.868</td><td>0.846</td></tr><tr><td>NB</td><td>0.704</td><td>0.585</td><td>0.853</td><td>0.671</td></tr><tr><td>MLPNN</td><td>0.755</td><td>0.769</td><td>0.764</td><td>0.766</td></tr><tr><td colspan="5">(b) Rating-sentiment inconsistency models</td></tr><tr><td>RF</td><td>0.922***</td><td>0.925***</td><td>0.921**</td><td>0.923***</td></tr><tr><td>CART</td><td>0.895**</td><td>0.905**</td><td>0.893*</td><td>0.897**</td></tr><tr><td>SVM</td><td>0.863**</td><td>0.891***</td><td>0.884*</td><td>0.887**</td></tr><tr><td>NB</td><td>0.777**</td><td>0.826***</td><td>0.857</td><td>0.841***</td></tr><tr><td>MLPNN</td><td>0.833***</td><td>0.884***</td><td>0.824***</td><td>0.853***</td></tr><tr><td colspan="5">(c) Content inconsistency models</td></tr><tr><td>RF</td><td>0.910***</td><td>0.925***</td><td>0.898</td><td>0.911**</td></tr><tr><td>CART</td><td>0.893**</td><td>0.907**</td><td>0.893*</td><td>0.900**</td></tr><tr><td>SVM</td><td>0.847</td><td>0.891***</td><td>0.895**</td><td>0.893**</td></tr><tr><td>NB</td><td>0.732*</td><td>0.847***</td><td>0.855</td><td>0.851***</td></tr><tr><td>MLPNN</td><td>0.814***</td><td>0.830**</td><td>0.832***</td><td>0.831***</td></tr><tr><td colspan="5">(d) Language inconsistency models</td></tr><tr><td>RF</td><td>0.921***</td><td>0.931***</td><td>0.909**</td><td>0.920***</td></tr><tr><td>CART</td><td>0.880**</td><td>0.888**</td><td>0.886</td><td>0.887**</td></tr><tr><td>SVM</td><td>0.853*</td><td>0.901***</td><td>0.877*</td><td>0.889***</td></tr><tr><td>NB</td><td>0.768**</td><td>0.85**</td><td>0.858</td><td>0.854***</td></tr><tr><td>MLPNN</td><td>0.813***</td><td>0.857***</td><td>0.773*</td><td>0.813***</td></tr><tr><td colspan="5">(e) All review inconsistency models</td></tr><tr><td>RF</td><td>0.929***</td><td>0.936***</td><td>0.928***</td><td>0.932***</td></tr><tr><td>CART</td><td>0.907***</td><td>0.926***</td><td>0.891*</td><td>0.908***</td></tr><tr><td>SVM</td><td>0.849*</td><td>0.9***</td><td>0.871*</td><td>0.885***</td></tr><tr><td>NB</td><td>0.735*</td><td>0.856*</td><td>0.884**</td><td>0.869***</td></tr><tr><td>MLPNN</td><td>0.836***</td><td>0.886***</td><td>0.869***</td><td>0.877***</td></tr></table>

Denoting performance improvement over the baseline models.  
<sup>\*\*\*</sup> p < .001.  
p < .01.  
p < .05.

![](/api/attachments/VB8FMHMP/fulltext/images/9f89ac60d8f3081fe9a6018347e1596ae0a80750956de0eb50c6a733af7e4789.jpg)  
Fig. 3. The F-score comparison of different methods across different feature combinations.  
Notes: ‘B0’, ‘RSI’, ‘CI’, ‘LI’, and ‘AI’ represent baseline models, models with the baseline and rating-sentiment inconsistency features, models with the baseline and content inconsistency features, models with the baseline and language inconsistency features, and models with the baseline and all inconsistency features combined, respectively.

Table 7  
Sensitivity analysis results.

<table><tr><td>Features</td><td>Scores</td><td>Features</td><td>Scores</td></tr><tr><td colspan="4">(a) The importance of inconsistency features</td></tr><tr><td>Rating_sentiment_incon</td><td>44.15</td><td>Emotiveness diversity_incon</td><td>5.27</td></tr><tr><td>Noun ratio_incon</td><td>33.24</td><td>Capitalized diversity_incon</td><td>5.23</td></tr><tr><td>Verb count_incon</td><td>21.46</td><td>Sentiment_incon</td><td>5.01</td></tr><tr><td>Adjective count_incon</td><td>10.65</td><td>Subjectivity_incon</td><td>2.29</td></tr><tr><td>Lexical validity_incon</td><td>10.07</td><td>Review length_incon</td><td>1.97</td></tr><tr><td>Pronoun count_incon</td><td>10.03</td><td>Average sentence length_incon</td><td>1.82</td></tr><tr><td>Noun count_incon</td><td>9.50</td><td>Average content similarity_incon</td><td>1.77</td></tr><tr><td>PoS n-gram diversity_incon</td><td>9.03</td><td>Linguistic diversity_incon</td><td>1.29</td></tr><tr><td>Lexical diversity_incon</td><td>5.94</td><td>Self-reference diversity_incon</td><td>1.06</td></tr><tr><td>Redundancy_incon</td><td>5.72</td><td>personal pronoun count_incon</td><td>0.9</td></tr><tr><td>Adverb count_incon</td><td>5.53</td><td>Sentiment orientation_incon</td><td>0.2</td></tr><tr><td colspan="4">(b) The overall top-30 most important features (with inconsistency features highlighted)</td></tr><tr><td>Vote count</td><td>134.41</td><td>Review duration</td><td>10.85</td></tr><tr><td>Review count</td><td>82.49</td><td>Adjective count_incon</td><td>10.65</td></tr><tr><td>Membership length</td><td>79.18</td><td>Cool votes</td><td>10.08</td></tr><tr><td>First review</td><td>77.11</td><td>Lexical validity_incon</td><td>10.07</td></tr><tr><td>Useful votes</td><td>52.26</td><td>Pronoun count_incon</td><td>10.03</td></tr><tr><td>Review burstiness</td><td>49.32</td><td>Noun count_incon</td><td>9.50</td></tr><tr><td>Average content similarity</td><td>47.58</td><td>Positive ratio</td><td>9.47</td></tr><tr><td>Average posting rate</td><td>47.35</td><td>PoS n-gram diversity_incon</td><td>9.03</td></tr><tr><td>Rating_sentiment_incon</td><td>44.15</td><td>Maximum check-ins</td><td>8.57</td></tr><tr><td>Noun ratio_incon</td><td>33.24</td><td>Capitalized diversity</td><td>8.50</td></tr><tr><td>Maximum posting rate</td><td>32.09</td><td>Friend count</td><td>8.32</td></tr><tr><td>Photo count</td><td>21.85</td><td>Review updates</td><td>7.71</td></tr><tr><td>Verb count_incon</td><td>21.46</td><td>Check-ins</td><td>7.54</td></tr><tr><td>Funny votes</td><td>21.41</td><td>Tip count</td><td>7.11</td></tr><tr><td>Positive-to-negative ratio</td><td>18.40</td><td>Average sentence length</td><td>6.86</td></tr></table>

## 6.3. Fake OCR detection

The model performance of fake OCR detection models is reported in Table 6 and Fig. 3. The results of paired-sample t-tests between the models with and without (i.e., baseline models) incorporating the cor responding inconsistency features are presented in Tables 6(b) \~ (e).We examined the correlations between the inconsistency features and among all of the features. The results of Pearson Correlation analysis show that the coefficients were insignificant (p>.05) except for a few (e. g., lexical diversity and PoS n-gram diversity, and pronoun count\_incon and personal pronoun count\_incon). To understand the impacts of those highly correlated features on model performance, we compared the performances of the best RF model before and after removing one (less important one based on the information gain) from all the correlated feature pairs. The results of paired sample t-tests did not yield a signif icant change in model performance (p>.05).

It is shown from Table 6 that the proposed models that incorporated RSI features alone (b), CI features alone (c), LI features alone (d), and all the three types of inconsistency features combined (AI) (e) significantly outperformed the baseline models (p < .05) across all of the evaluation metrics with only a few exceptions: the improvements in the recall of the NB models after incorporating individual types of inconsistency fea tures, the recall of the RF model after incorporating the CI features, and the recall of the CART model after incorporating LI features were not statistically significant (p > .05). Among the five classification methods, the RF model that incorporated all of the three types of review incon sistency features (AI) achieved the best performance in terms of accu racy, precision, recall, and F-score. These results provide strong evidence that incorporating rating-sentiment, content, and language inconsistency features, either individually or as a whole, improves the performance of fake OCR detection. In addition, the models that com bined all three types of inconsistency features achieved the best per formance in fake OCR detection. Therefore, hypotheses H2(a), H2(b), and H2(c) were supported.

![](/api/attachments/VB8FMHMP/fulltext/images/8ed8a6cb0cf0d53ab99f0ebcdb272eeba42623242e860092e3155a203052ee0e.jpg)  
(a) Review-sentiment inconsistency

![](/api/attachments/VB8FMHMP/fulltext/images/861b12188e70959b36e5543e855dc50b562c5cde67f50be5bad2bfea47193839.jpg)  
(b) Noun count icnon

![](/api/attachments/VB8FMHMP/fulltext/images/911b29fa9f460866ad151d3afd131b8031bd214fe007101972e3091dc77d539c.jpg)  
(c) Noun ratio icnon  
Fig. 4. Boxplots of sample review inconsistency features.

## 6.4. Feature importance ranking

To examine the relative importance of individual review inconsis tency features for fake OCR detection, we performed a post-modeling sensitivity analysis on the RF model with the baseline combined with all the inconsistency features $( \mathrm { i . e . , }$ the best-performed model) using the Caret package of R. Sensitivity analysis is aimed to analyze how an in dependent variable may affect the dependent variable (i.e., outcome), assuming all other independent variables remain the same. If the value of the dependent variable does not vary significantly as the value of an independent variable changes (while keeping the values of other inde pendent variables fixed), then that independent variable is not impor tant to the dependent variable. Tables 7(a) reports the importance scores of inconsistency features, and Table 7(b) reports those of the top-30 features overall, respectively.

It is shown from Table 7(a) that different inconsistency features have different levels of contributions to the discrimination of fake OCRs. The most important inconsistency feature is rating-sentiment inconsistency. It is noted from Table 7(b) that the top-30 most important features include features from each of the three types of review inconsistency, which further confirm the importance of all the proposed review inconsistency to fake OCR detection.

## 6.5. Robustness check for review inconsistency

To further illustrate review inconsistency, we produced boxplots for each of the three types of review inconsistency features across the different levels of star rating in Fig. 4. Given the large number of the CI and LI features, we randomly selected one feature from each type $( \mathrm { i . e . , }$ noun\_count\_incon and noun ratio\_incon) for illustration. In the figures, symbols ${ \bf \cdot _ { 0 } } ,$ and ‘\*’ indicate a mild outlier and an extreme outlier, respectively, which clearly demonstrate the presence of all three types of review inconsistency across different ratings.

## 6.6. Robustness check for feature correlation

We conducted a Pearson Correlation [72] analysis in order to un derstand the correlations among inconsistency features and among all of the features. The values of Pearson Correlation Coefficients (PCC) range between − 1 (i.e., perfect negative correlation) and 1 (i.e., perfect posi tive correlation). The results are reported in Figs. 5 and 6 below. The color in the figures indicates the correlation strength. Specifically, darkest red, gray, and darkest blue colors indicate perfect positive cor relation, no correlation, and perfect negative corrleation, respectively.

The following results show the correlations among inconsistency features and correlations among all of the features. Because the corre lation matrices are huge, we use Figures A and B to show the correlation matrices:

Based on Figs. 5 and $^ { 6 , }$ most of the feature pairs don’t show strong correlations except a few, which are listed in the Table 8.

Based on [73], generally, the correlation of predictors doesn’t inhibit the model fitting and prediction on new observations, provided the prediction is made within the observation region. In order to empirically investigate the impact of those highly correlated features on model performance, we compared the performance of the best RF model with all of the features vs. its performance after removing one of two highly correlated features, which was less important based on information gain. For example, the relative importance scores of Lexical diversity and PoS n-gram diversity were 0.0124 and 0.0141, respectively, and they are highly correlated. We removed Lexical diversity because it is less important. Using the same process, we removed Cool votes, Review up dates, personal pronoun count\_incon, PoS n gram diversity, and personal pronoun count. Then, we ran the RF model with the remaining features. The model comparison results are shown in the Table 9.

The performance results shown in the above table reveal that removing those highly correlated features did not affect model perfor mance significantly. Thus, the correlation among some features did not affect our research findings.

## 7. Discussion

Review inconsistency introduces conflicts either within or among OCRs. Such conflicts may confuse consumers and cast doubts on the credibility of OCRs, which may further lead to adverse effects on con sumers’ purchase decisions. This research conceptualizes and introduces three types of review inconsistency: rating-sentiment inconsistency, content inconsistency, and reviewer language inconsistency. It also proposes the operationalizations of review inconsistency with 22 fea tures. The empirical results confirm the presence of the three types of review inconsistency in OCRs, and more importantly, reveal the signif icant differences in review inconsistency between fake and authentic OCRs. Furthermore, the evaluation results show that incorporating the review inconsistency features help boost fake OCR detection performance.

This study makes several novel research contributions. First, although a few prior studies mentioned inconsistency between review content and star rating in general (e.g., [19,22]), they did not provide empirical evidence about its prevalence in OCRs or theoretical concep tualization of review inconsistency. This research introduces the three types of review inconsistency, and empirically validates their presence in OCRs.

Second, this research extends Truth-Default Theory [39] to explain the effect of review inconsistency on fake OCR detection for the first time. Specifically, it draws upon a coherence view for the role of ratingsentiment inconsistency and a correspondence view for those of content inconsistency and language inconsistency to distinguish fake OCRs from authentic ones. It provides strong empirical evidence that fake OCRs tend to have more review inconsistencies than authentic OCRs, implying that review inconsistency can serve as an effective source of cues for the detection of fake OCRs. Additionally, the positive effect of rating sentiment inconsistency on fake OCRs detection provides new evi dence for the leakage theory of deception [15]. Furthermore, the importance of language inconsistency to fake OCR detection provides an extension to and support of attitude-behavior consistency theory [18].

Third, this study introduces a new and reliable means to improve the state-of-the-art methods for automatic fake OCR detection. Our empir ical comparisons of five classification models with and without incor porating the three types of review inconsistency features demonstrate that those inconsistency features can contribute to the performance of fake OCR detection regardless of the choice of specific classification algorithms. The findings offer new research insights for improving fake OCR detection through probing review inconsistency.

This study has some limitations that invite potential opportunities for future research. First, the OCR data used in this study were collected from Yelp.com. Yelp reviews are mainly related to local businesses and online reservation services [44], which may bring concerns about generalizability of the research findings. Therefore, it would be valuable to examine if the findings of this study can be generalizable to OCRs of other types of products and/or review platforms. In addition, it is worth exploring inconsistency in other dimensions of OCRs such as business features. Moreover, the conceptualization and measurement of the re view inconsistency can also potentially be helpful in improving fake

OCR detection models using the deep learning technique. Deep learning models use word embedding to represent an OCR. It will be interesting to investigate whether review inconsistency is still helpful if it is enco ded as latent features in the OCR representation via word embedding, or combined with the word embedding representation. Further, the role of review inconsistency in other applications such as review helpfulness prediction can be an interesting issue for future research.

## Acknowledgement

This research is partially supported by U.S. National Science Foun dation (Award #s: CNS 1704800 and SES 1527684). Any opinions, findings, and conclusions expressed in this material are those of the authors and do not necessarily reflect the views of NSF.

## References

[1] S. Baccianella, A. Esuli, F. Sebastiani, Sentiwordnet 3.0: an enhanced lexica resource for sentiment analysis and opinion mining, Lrec, 2010, pp. 2200–2204

[2] H. Baek, J. Ahn, Y. Choi, Helpfulness of online consumer reviews: Readers objectives and review cues, Int. J. Electron. Commer. 17 (2) (2012) 99–126.

[3] S. Banerjee, A.Y. Chua, A study of manipulative and authentic negative reviews, in: Proceedings of the 8th International Conference on Ubiquitous Information Management and Communication, ACM, 2014, p. 76.

[4] B. Biswas, P. Sengupta, D. Chatterjee, Examining the determinants of the count of customer reviews in peer-to-peer home-sharing platforms using clustering and count regression techniques, Decision Supp. Syst. (2020) 113324.

[5] L. Breiman, Random forests, Mach. Learn. 45 (1) (2001) 5–32.

[6] G. Burtch, Y. Hong, R. Bapna, V. Griskevicius, Stimulating online reviews by combining financial incentives and social norms, Manag. Sci. 64 (5) (2018) 2065–2082.

[7] Y.-R. Chen, H.-H. Chen, Opinion spam detection in web forum: a real case study, in: Proceedings of the 24th International Conference on World Wide Web, International World Wide Web Conferences Steering Committee, 2015, pp. 173–183.

[8] A.Y. Chua, S. Banerjee, Understanding review helpfulness as a function of reviewer reputation, review rating, and review depth, J. Assoc. Inf. Sci. Technol. 66 (2) (2015) 354–362

[9] A.Y. Chua, S. Banerjee, Helpfulness of user-generated reviews as a function of review sentiment, product type and information quality, Comput. Hum. Behav. 54 (2016) 547–554.

[10] A. Collomb, C. Costea, D. Joyeux, O. Hasan, L. Brunie, A Study and Comparison of Sentiment Analysis Methods for Reputation Evaluation, Rapport de Recherche RR-LIRIS-2014-002, 2014

[11] P. Cortez, M.J. Embrechts, Using sensitivity analysis and visualization techniques to open black box data mining models, Inf. Sci. 225 (2013) 1–17.

[12] A. Dimoka, Y. Hong, P.A. Pavlou, On product uncertainty in online markets: Theory and evidence. MIS O. 36 (2012)

[14] P. Ekman, Facial expression and emotion, Am. Psychol. 48 (4) (1993) 384.

[13] A. Duric, F. Song, Feature selection for sentiment analysis based on content and syntax models, Decis Support. Syst, 53 (4) (2012) 704–711.

[15] P. Ekman, W.V. Friesen, Nonverbal leakage and clues to deception, Psychiatry 32 (1) (1969) 88–106.

[16] M.J. Embrechts, F.A. Arciniegas, M. Ozdemir, R.H. Kewley, Data mining for molecules with 2-D neural network sensitivity analysis, Intern. J. Smart Eng. Syst. Design 5 (4) (2003) 225–239.

[17] T.H. Engler, P. Winter, M. Schulz, Understanding online product ratings: a customer satisfaction model, J. Retail. Consum. Serv. 27 (2015) 113–120.

[18] R.H. Fazio, M.P. Zanna, Direct experience and attitude-behavior consistency, in: Advances in Experimental Social Psychology, Elsevier, 1981, pp. 161–202.

[19] B. Fu, J. Lin, L. Li, C. Faloutsos, J. Hong, N. Sadeh, Why people hate your app: Making sense of user feedback in a mobile app store, in: Proceedings of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM. 2013 pn.1276-1284

[20] H. Gangadharbatla, Facebook me: collective self-esteem, need to belong, and internet self-efficacy as predictors of the iGeneration’s attitudes toward socia networking sites, J. Interact. Advert. 8 (2) (2008) 5–15.

[21] D. Gavilan, M. Avello, G. Martinez-Navarro, The influence of online ratings and

[22] M. Geierhos, F.S. B¨aumer, S. Schulze, V. Stuß, I grade what I get but write what I think, in: Inconsistency Analysis in Patients’ Reviews, 2015.

[23] B. Guo, S. Zhou, Understanding the impact of prior reviews on subsequent reviews: the role of rating volume, variance and reviewer characteristics. Electron. Commer Res, Appl, 20 (2016) 147–158

[24] S. Guohou, Z. Lina. Z. Dongsong, What reveals about depression level? The role of multimodal features at the level of interview questions, Inf, Manag, 57 (7) (2020) 103349.

[25] P. Hajek, A. Barushka, M. Munk, Fake consumer review detection using deep neural networks integrating word embeddings and emotion mining, Neural Comput. & Applic. (2020) 1–16.

[26] C.U. Hrinrich, P. Borkenau, Deception and deception detection: the role of cross modal inconsistency, J. Pers. 66 (5) (1998) 687–712.

[27] N. Hu, N.S. Koh, S.K. Reddy, Ratings lead you to the product, reviews help you clinch it? The mediating role of online review sentiments on product sales, Decis. Support, Syst, 57 (2014) 42–53

[28] N. Hu, P.A. Pavlou, J.J. Zhang, On self-selection biases in online product reviews, MIS Q. 41 (2) (2017) 449–471.

[29] Y.-H. Hu, K. Chen, Predicting hotel review helpfulness: the impact of review visibility, and interaction between hotel stars and review ratings, Int. J. Inf. Manag. 36 (6) (2016) 929–944.

[30] A.H. Huang, K. Chen, D.C. Yen, T.P. Tran, A study of factors that contribute to online review helpfulness, Comput. Hum. Behav. 48 (2015) 17–27.

[31] C.J. Hutto, E. Gilbert, Vader: A parsimonious rule-based model for sentiment analysis of social media text, in: Eighth International AAAI Conference on Weblogs and Social Media, 2014.

[32] N. Jindal, B. Liu, Opinion spam and analysis, in: Proceedings of the 2008 international conference on web search and data mining, ACM, 2008, pp. 219–230.

[33] D. Jurafsky, V. Chahuneau, B.R. Routledge, N.A. Smith, Narrative framing of consumer sentiment in online restaurant reviews, First Monday 19 (4) (2014).

[34] D. Kamerer, Understanding the yelp review filter: an exploratory study, First Monday 19 (9) (2014).

[35] Y. Kang, L. Zhou, Helpfulness assessment of online reviews: the role of semantic hierarchy of product features, ACM Trans. Manage. Inform. Syst. (TMIS) 10 (3) (2019) 1–18.

[36] S. Kennedy, N. Walsh, K. Sloka, A. McCarren, J. Foster, Fact or factitious? Contextualized opinion spam detection, in: Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: Student Research Workshop, 2019, pp. 344–350.

[37] R.H. Kewley, M.J. Embrechts, C. Breneman, Data strip mining for the virtual design of pharmaceuticals with neural networks, IEEE Trans. Neural Netw. 11 (3) (2000) 668–679.

[38] Y.-J. Lee, K. Hosanagar, Y. Tan, Do I follow my friends or the crowd? Information cascades in online movie ratings, Manag. Sci. 61 (9) (2015) 2241–2258.

[39] T.R. Levine, Truth-default theory (TDT) a theory of human deception and deception detection, J. Lang. Soc. Psychol. 33 (4) (2014) 378–392.

[40] H. Li, Z. Chen, B. Liu, X. Wei, J. Shao, Spotting fake reviews via collective positiveunlabeled learning, in: 2014 IEEE International Conference on Data Mining, IEEE, 2014, pp. 899–904.

[41] J. Li, Q. Ma, C. Yuan, W. Zhou, J. Han, S. Hu, Fusion convolutional attention network for opinion spam detection, in: International Conference on Neural Information Processing, Springer, 2019, pp. 223–235

[42] E.-P. Lim, V.-A. Nguyen, N. Jindal, B. Liu, H.W. Lauw, Detecting product review spammers using rating behaviors, in: Proceedings of the 19th ACM International Conference on Information and Knowledge Management. 2010. pp. 939–948.

[43] B. Liu. Sentiment analysis and opinion mining. Synth. Lect. Human Lang. Technol 5 (1) (2012) 1–167

[44] M. Luca, Reviews, Reputation, and Revenue: The Case of Yelp.com, 2016.

[45] M. Luca, G. Zervas, Fake it till you make it: reputation, competition, and yelp review fraud, Manag, Sci, 62 (12) (2016) 3412–3427.

[46] S.A. McCornack, Information manipulation theory, Commun. Monogr. 59 (1) (1992) 1–16.

[47] W.W. Moe, M. Trusov, The value of social dynamics in online product ratings forums, J. Mark. Res. 48 (3) (2011) 444–456.

[48] S.M. Mudambi, D. Schuff, Research note: What makes a helpful online review? A study of customer reviews on Amazon.com, MIS O. (2010) 185–200

[49] A. Mukherjee, A. Kumar, B. Liu, J. Wang, M. Hsu, M. Castellanos, R. Ghosh, Spotting opinion spammers using behavioral footprints, in: Proceedings of the 19th ACM SIGKDD International Conference on KNOWLEDGE Discovery and Data Mining, ACM, 2013, pp. 632–640.

[50] A. Mukherjee, V. Venkataraman, B. Liu, N. Glance, Fake review detection: classification and analysis of real and pseudo reviews, technical report UIC-CS-2013–03, University of Illinois at Chicago, Tech. Rep. (2013).

[51] A. Mukherjee, V. Venkataraman, B. Liu, N. Glance, What yelp fake review filter might be doing?, in: Seventh International AAAI Conference on Weblogs and Social Media, 2013.

[52] U. Orhan, M. Hekim, M. Ozer, EEG signals classification using the K-means clustering and a multilayer perceptron neural network model, Expert Syst. Appl. 38 (10) (2011) 13475–13481,

[53] M. Ott, Y. Choi, C. Cardie, J.T. Hancock, Finding deceptive opinion spam by any stretch of the imagination, in: Proceedings of the 49th Annual Meeting of the

Association for Computational Linguistics: Human Language Technologies-Volume 1, Association for Computational Linguistics, 2011, pp. 309–319.

[54] F.N. Ribeiro, M. Araújo, P. Gonçalves, M.A. Gonçalves, F. Benevenuto, Sentibencha benchmark comparison of state-of-the-practice sentiment analysis methods, EPJ Data Sci. 5 (1) (2016) 23.

[55] G. Shan, D. Zhang, L. Zhou, L. Suo, J. Lim, C. Shi, Inconsistency Investigation between Online Review Content and Ratings, 2018.

[56] J.P. Singh, S. Irani, N.P. Rana, Y.K. Dwivedi, S. Saumya, P.K. Roy, Predicting the “helpfulness” of online consumer reviews, J. Bus. Res. 70 (2017) 346–355.

[57] R.E. Smith. W.R. Swinvard. Attitude-behavior consistency: the impact of produc trial versus advertising, J. Mark. Res. 20 (3) (1983) 257–267.

[58] D.M. Steiger, Enhancing user understanding in a decision support system: a theoretical basis and framework, J. Manag. Inf. Syst. 15 (2) (1998) 199–220.

[59] Y.R. Tausczik, J.W. Pennebaker, The psychological meaning of words: LIWC and computerized text analysis methods, J. Lang. Soc. Psychol. 29 (1) (2010) 24–54.

[60] C. Wang, X. Zhang, I.-H. Hann, Socially nudged: a quasi-experimental study of friends’ social influence in online product ratings, Inf. Syst. Res. 29 (3) (2018) 641-655.

[61] G. Wang, S. Xie, B. Liu, P.S. Yu, Identify online store review spammers via social review graph, ACM Trans. Intell. Syst. Technol. (TIST) 3 (4) (2012) 61.

[62] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, J. Manag. Inf. Syst. 12 (4) (1996) 5–33.

[63] D. Weathers, S.D. Swain, V. Grover, Can online product reviews be more helpful? Examining characteristics of information content by product type, Decis. Support. Syst. 79 (2015) 12–23.

[64] G. Wu, D. Greene, B. Smyth, P. Cunningham, Distortion as a validation criterion in the identification of suspicious reviews, in: Proceedings of the First Workshop on Social Media Analytics, ACM, 2010, pp. 10–13

[65] C. Xu, Detecting collusive spammers in online review communities, in: Proceedings of the Sixth Workshop on Ph. D. Students in Information and Knowledge Management, ACM, 2013, pp. 33–40

[66]. K.-H. Yoo. U. Gretzel. Comparison of deceptive and truthful travel reviews. Inform Commun, Technol, Tour, 2009 (2009) 37–47

[67] D. Yu, Y. Mu, Y. Jin, Rating prediction using review texts with underlying sentiments. Inf, Process. Lett, 117 (2017) 10–18.

[68] D. Zhang, L. Zhou, J.L. Kehoe, I.Y. Kilic, What online reviewer behaviors really matter? Effects of verbal and nonverbal behaviors on detection of fake online reviews, J. Manag. Inf. Syst. 33 (2) (2016) 456–481.

[69] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating role of product and consumer characteristics, J. Mark. 74 (2) (2010) 133–148.

[70] H. Zou, X. Tang, B. Xie, B. Liu, Sentiment classification using machine learning techniques with syntax features. in: Computational Science and Computational Intelligence (CSCD). 2015 International Conference on. JEEE. 2015. pp. 175–179.

[711 M. Zuckerman. R. Driver. R. Koestner. Discrepancy as a cue to actual and perceived deception, J. Nonverbal Behav, 7 (2) (1982) 95–100.

[72] J. Benesty, J. Chen, Y. Huang, I. Cohen, Pearson correlation coefficient, in: Noise reduction in speech processing, Springer, 2009, pp. 1–4.

[Z3] M.H. Kutner. CJ. Nachtsheim. J. Neter. W. Li. Applied linear statistical models McGraw-Hill Irwin, New York, 2005

Guohou Shan is a second year PhD student in the Management Information System Concentration at Fox School of Business in Temple University. His research interests include Healthcare IT, online community, and fake news detection.

Lina Zhou is a Professor of Management Information Systems at the Belk College of Business at UNC Charlotte. Her research interests span the areas of social media analytics deception detection, knowledge management, biomedical informatics, and intelligent mobile interface. She has (co-)-authored articles published in journals such as MIS Quar terly. Journal of Management Information Systems. Decision Support Systems. JEEE Trans actions. Information and Management. and so on.

Dongsong Zhang is a Belk Distinguished Professor in Business Analytics in the Depart ment of Business Information Systems and Operations Management, at UNC Charlotte. He received his Ph.D. in Management Information Systems from the University of Arizona. His research interests include business intelligence, social media analytics, mobile HCI, and health IT. He has published approximately 150 research articles and received a dozen research grants and awards from National Science Foundation, National Institute of Health, and U.S. Department of Education, among other funding agencies.
