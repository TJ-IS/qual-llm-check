---
otero_id: 7596
otero_key: "QAVYFSSE"
title: "What Online Reviewer Behaviors Really Matter? Effects of Verbal and Nonverbal Behaviors on Detection of Fake Online Reviews"
authors: "Dongsong Zhang; Lina Zhou; Juan Luo Kehoe; Isil Yakut Kilic"
year: "2016"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2016.1205907"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# What Online Reviewer Behaviors Really Matter? Effects of Verbal and Nonverbal Behaviors on Detection of Fake Online Reviews

Dongsong Zhang, Lina Zhou, Juan Luo Kehoe & Isil Yakut Kilic

To cite this article: Dongsong Zhang, Lina Zhou, Juan Luo Kehoe & Isil Yakut Kilic (2016) What Online Reviewer Behaviors Really Matter? Effects of Verbal and Nonverbal Behaviors on Detection of Fake Online Reviews, Journal of Management Information Systems, 33:2, 456-481, DOI: 10.1080/07421222.2016.1205907

To link to this article: http://dx.doi.org/10.1080/07421222.2016.1205907

![](/api/attachments/QAVYFSSE/fulltext/images/b4cac0143ea9de14e21545f2f37294b243fa099e723f1dae3c0f1bda2961e11e.jpg)

Published online: 05 Oct 2016.

![](/api/attachments/QAVYFSSE/fulltext/images/07f2ac839ab93e71351aea6388fcebe77593d4a570918203f51d2aa2281ffbf0.jpg)

Submit your article to this journal

![](/api/attachments/QAVYFSSE/fulltext/images/a6da520dd9d29aba2a0f2bdd66864323d81c29fe349d3ba1944c3b8bf0b1c794.jpg)

Article views: 5

![](/api/attachments/QAVYFSSE/fulltext/images/029fbff51e6c05aadc590b626a978dd7fcc2a1cf5eccd09b50458144a0fc8677.jpg)

View related articles

![](/api/attachments/QAVYFSSE/fulltext/images/44a483ed387799a23233ed383a3867ab4c716bd383ac0c004db9051f87d563d3.jpg)

View Crossmark data

# What Online Reviewer Behaviors Really Matter? Effects of Verbal and Nonverbal Behaviors on Detection of Fake Online Reviews

DONGSONG ZHANG, LINA ZHOU, JUAN LUO KEHOE, AND ISILYAKUT KILIC

DONGSONG ZHANG (zhangd@umbc.edu; corresponding author) received his Ph.D. in management information systems from the University of Arizona. He is a chair professor at the International Business School, Jinan University, China, and a full professor in the Department of Information Systems at the University of Maryland, Baltimore County. His research interests include social computing, mobile human– computer interaction, business analytics, health information technologies, and online communities. He has published approximately 140 papers in journals and conference proceedings, including Journal of Management Information Systems, MIS Quarterly, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Software Engineering, and others. His research has been funded by the U.S. National Science Foundation, the U.S. National Institutes of Health, the U.S. Department of Education, the National Natural Science Foundation of China, Chinese Academy of Sciences, and Google, Inc.

LINA ZHOU (zhoul@umbc.edu) is an associate professor in the Department of Information Systems at the University of Maryland, Baltimore County. She received her Ph.D. in computer science from Peking University. Her research interests include online deception detection, computer-mediated communication, text mining, social network analysis, and intelligent user interfaces. She has published over sixty journal papers in Journal of Management Information Systems, MIS Quarterly, IEEE Transactions on Data and Knowledge Engineering, and others. Her research has been funded by the U.S. National Science Foundation.

JUAN LUO KEHOE (jluo1@umbc.edu) is a master’s student in the Department of Information Systems at the University of Maryland, Baltimore County. She received her Ph.D. in biochemistry and molecular biology from China Agricultural University. Her research focuses on data science and big data analysis in various domains.

ISIL YAKUT KILIC (yakut1@umbc.edu) is a Ph.D. student in the Department of Information Systems at the University of Maryland, Baltimore County. She received her Master’s degree in computer engineering from Bilkent University, Turkey. Her research focuses on mining user-generated content and generalizing across domains.

ABSTRACT: The value and credibility of online consumer reviews are compromised by significantly increasing yet difficult-to-identify fake reviews. Extant models for automated online fake review detection rely heavily on verbal behaviors of reviewers while largely ignoring their nonverbal behaviors. This research identifies a variety of nonverbal behavioral features of online reviewers and examines their relative importance for the detection of fake reviews in comparison to that of verbal behavioral features. The results of an empirical evaluation using real-world online reviews reveal that incorporating nonverbal features of reviewers can significantly improve the performance of online fake review detection models. Moreover, compared with verbal features, nonverbal features of reviewers are shown to be more important for fake review detection. Furthermore, model pruning based on a sensitivity analysis improves the parsimony of the developed fake review detection model without sacrificing its performance.

KEY WORDS AND PHRASES: deception detection, eWoM, electronic word of mouth, feature pruning, fake online reviews, online reviewer behavior, user-generated content.

Research has shown that online consumer reviews have a significant impact on consumers’ purchase decisions and sales [9, 27, 69]. In particular, positive reviews can promote the sales of products and services and result in significant financial gains and/or fame for businesses, organizations, or individuals, whereas negative reviews may severely damage the reputation of products and hurt their sales. A recent Cone Research study [8] reports that 80 percent of consumers reverse their purchase decisions after reading negative consumer reviews, while 87 percent affirm their purchase decisions after reading positive consumer reviews. Meanwhile, online retailers and manufacturers can also take advantage of online reviews by identifying desirable features or flaws of products commented by consumers in their reviews.

Unfortunately, the value and prevalent use of online consumer reviews also bring forth strong incentives for opinion spamming, which refers to illegal marketing practices that involve creating commercially advantageous fake reviews [6, 47]. We define fake reviews as deceptive reviews provided with an intention to mislead consumers in their purchase decision making, often by reviewers with little or no actual experience with the products or services being reviewed. Fake reviews can be either unwarranted positive reviews aiming to promote a product, or unjustified false negative comments on competing products in order to damage their reputations [59].

The prevalence of online fake reviews is escalating and representing a growing problem for market regulation [26, 37]. There are sufficient incentives for businesses to influence consumers through fake reviews. For example, Samsung was alleged to have hired students to post negative comments about mobile phones made by HTC;<sup>1</sup> New York’s attorney general announced on September 23, 2013 that nineteen New York-based companies had agreed to pay hefty penalties and stop writing fake online reviews—many of which had flooded consumer review sites such as Yelp.com and CitySearch.com. Similar reports of fake online reviews include those on iTunes reported by the New York Times,<sup>2</sup> the confession of a fake reviewer on Amazon. com,<sup>3</sup> fake reviews on TripAdvisor.com reported by USA Today on July 16, 2009, and so on. Some companies advertise online, such as on Craigslist, for freelance writers to write forged reviews,<sup>4</sup> or even provide professional fake review writing services, such as SponsoredReviews.com. Online review platforms provide an easy setting for creating fake reviews because most of them do not have specific restrictions on posting reviews and require little information about poster themselves [63]. Ott et al. [48] investigated the occurrence of fake reviews in six popular online review communities, including Expedia.com, Hotels.com, Orbitz.com, Priceline. com, TripAdvisor.com, and Yelp.com, and reported that fake reviews had become a growing problem across all of them. Most online review platforms do not publicly filter fake reviews. Even if some do, such as Yelp.com, their filtering algorithms remain a trade secret. Review readers are increasingly concerned about untrustworthy or fraudulent information in online reviews [63]. Those fake reviews can not only mislead consumers to make incorrect decisions, but also fundamentally undermine the credibility and value of reviews as a whole [26, 37]. Further, in view of the influence of earlier reviews on subsequent reviews [38], fake reviews can exert undesirable influence on later reviews. As a result, developing effective methods to detect fake reviews becomes essential and urgent.

Detecting online fake reviews, however, is a challenging task [21, 52]. Fabricating a fake review is essentially a deception process. Extensive deception studies have shown that the accuracy of human deception detection is only slightly higher than 50 percent, primarily due to people’s truth bias and misuse of telltale signs of deception [36, 68]. Detecting fake online reviews is even more difficult because: (1) many cues to deception in face-to-face communication, such as facial expression, body gesture, and tone of voice [61], are not available; and (2) fake reviews are often crafted like authentic reviews to avoid being detected [31]. As a result, manual detection of online fake reviews by consumers is difficult and inaccurate.

Automatic detection of online fake reviews by leveraging machine learning techniques can help address the above-mentioned limitations of manual detection in that machine-learning models can easily scale up in terms of the number of reviews and the number of predictive features (i.e., cues to fake reviews). Those models have been proven to be able to significantly surpass humans’ deception detection performance [17, 18, 65]. Despite increasing research on automatic detection of online fake reviews in recent years, existing studies have several limitations. First, verbal features (i.e., features extracted from review text) have been dominating the predictive feature set of existing fake review detection models. In contrast, nonverbal behaviors of reviewers, such as their review posting behavior and social interactions with other reviewers on an online review platform, have been understudied. According to deception theories and findings of previous deception detection studies [4, 71], nonverbal behaviors of individuals can serve as effective leakage cues to deception. Therefore, we expect that nonverbal behaviors of reviewers significantly contribute to the detection of fake reviews. Second, some studies used fake reviews manually created by Amazon Mechanical Turkers or other types of human participants as the training and testing data [29, 46, 49]. Comparative studies have suggested that Turkers seem to have different psychological states of mind when writing fake reviews in comparison to actual fake review writers, causing the accuracy of detection models constructed based on those pseudo-fake reviews much higher than the accuracy of models constructed based on real-world fake reviews [46, 47]. Third, previous studies have typically assessed the overall effectiveness of a fake review detection model as a whole without looking into the effects of individual predictive features. As a result, their findings provide few theoretical insights and little practical guidance on how to improve the effectiveness and generality of fake review detection models.

The goal of fake reviewers, or deceivers in general, is to deceive others while striving to avoid being detected. Motivated by financial gains or other benefits, fake reviewers may continuously learn from their previous experiences to improve their chances of success. They have plenty of time to edit and polish fake reviews to make the review content look more believable. Consequently, fake reviews may exhibit linguistic characteristics similar to those of authentic reviews [6, 47]. This phenomenon is also observed in other real-life online deception such as evolving spam e-mails [55, 58]. Therefore, fake review detection systems that mainly rely on verbal features extracted from review text will likely become less effective over time.

Motivated by improving the credibility of reviewers and connecting reviewers socially, some online consumer review platforms are becoming social platforms that transcend just presenting and archiving reviews. They allow a variety of social interactive activities among reviewers and provide additional information about reviewers, including reviewers’ personal information (e.g., name and location), reviewer ranking, posting history, and social interactions with other reviewers (e.g., number of friends and useful votes received from or given to other reviewers) on a review platform. Such nonverbal information about reviewers may provide rich, diverse, and reliable cues for distinguishing fake reviews from authentic ones for two reasons. One is that most fake reviewers are paid to write fake reviews [44]. They normally do not spend much time engaging with other reviewers or reviews as authentic reviewers may do. The other is that it is much more difficult and costly for a reviewer to manipulate his/her review posting history and social interactive activities in an online review platform than to manipulate the content of specific reviews that he/she posts. Although several recent studies considered some reviewer related features [30, 62], they only used a very small number of such features, leaving many other promising features unexplored. Furthermore, no studies have ever examined the relative impact of individual features on the performance of a fake review detection model.

The primary objective of this research is to systematically investigate potential impacts of verbal and nonverbal behavioral features of reviewers on fake review detection to fill the gap in the literature. This study makes several major research contributions. First, we categorize potential cues to online fake review detection into verbal and nonverbal categories by extending the interpersonal deception theory to online fake review detection, and create a relatively comprehensive set of features for each of the categories. Second, we build fake review detection models that incorporate the identified nonverbal behaviors of reviewers, along with common verbal features (i.e., review features) commonly used in previous studies. The results of an empirical evaluation with real-world online reviews demonstrate that incorporating nonverbal features significantly improves the performance of fake review detection. Third, we discover that nonverbal features have stronger influence on fake review detection than verbal features through a sensitivity analysis. Fourth, we improve the parsimony of the developed fake review detection model through feature pruning. The performance of the pruned model with only the top-twelve most influential features is comparable to that of the original model built with all features. Moreover, most of the top-ranked features are extracted from the nonverbal behaviors of reviewers, confirming the high efficacy and importance of nonverbal features for fake review detection. These findings provide novel research and practical implications for how to combat online fake reviews effectively.

## Related Work

A variety of techniques have been explored for automated fake review detection. Those approaches can be classified into two broad categories: machine learning and nonmachine learning methods, with the former being the dominant and more widely used approach.

## Machine Learning Approaches

The goal of machine learning is to apply statistical learning and artificial intelligence techniques to automatically learn hidden knowledge or patterns from training data or previous experience. Among different types of machine learning tasks, a crucial distinction is drawn between supervised and unsupervised learning. Supervised machine learning, such as classification and regression, refers to training a computer model with a set of data samples that are described with both inputs and corresponding target output values, which is then able to make predictions on new data. Supervised machine learning has been the dominant approach to detecting fake reviews [10, 12, 14, 32, 46, 49] where fake review detection is viewed as a binary classification problem—a target review will be labeled as either an authentic review or a fake review.

Unsupervised machine learning, such as clustering, refers to learning a model based on a set of training data consisting of inputs but no corresponding target output values. Thus, it must find patterns and relationships therein through an algorithm itself. Only a few studies have explored unsupervised machine learning methods for fake review detection to date [36, 42, 60]. For example, Mukherjee et al. [42] formulated fake review detection as a clustering problem by modeling spamicity of reviewers through creating a margin that separates population distributions of spammer and nonspammer clusters.

Both supervised and unsupervised machine learning methods require the selection of a set of input features for developing fake review models. These features may be related to review content, product ratings, reviewer characteristics, and/or brands.

● Review content features are linguistic or content features extracted from the text of an online review. Studies have emphasized the importance of review content features to consumers’ evaluation of reviews [24]. Although authentic and fake reviews may not be easily distinguishable from each other, many researchers believe that subtle linguistic cues may set them apart. These kinds of features include review length, n-grams, subjectivity of review content, the number of nouns, verbs, and adjectives [23], sentiment, readability (the effort and expertise of readers required to comprehend reviews), genre (e.g., the use of self-references and distribution of parts of speech [POS] tags), writing style (e.g., use of specific types of words such as affective cues, perceptual words, and future tense), diversity (i.e., the ratio of unique words), nonimmediacy (e.g., the number of self-references), rate of typos, psycholinguistic cues (e.g., the number of emotion terms), and so on [2, 47, 49, 63, 65, 66]. For example, Ott et al. [49] adopted eighty psycholinguistic features from linguistic inquiry and word count (LIWC) in their detection model, which were grouped into several main categories, including linguistic process features that represent functional aspects of text (e.g., the average number of words per sentence in a review), psychological process features that include social, emotional, cognitive, perceptual, and biological processes, anything related to time and space, any references to work, leisure, religion, and so on, and spoken categories that refer to primary filler and agreement words.

● Rating features focus on reviewers’ numeric ratings of products and the patterns of their ratings. Examples of rating features are general rating deviation (i.e., the average difference between a reviewer’s rating of a product and the product’s average rating) and rating deviation scores (i.e., the variance of a reviewer’s ratings across different brands) [47, 62].

● Reviewer characteristics are nonverbal features associated with reviewers themselves, their review posting behavior, and their interactions with other reviewers in an online review platform. These features are not attached to a particular review. Examples of such features include the average number of reviews that a reviewer posted per day, reviewer activity window (the days between the first and last posts) [42, 47], ratio of the number of the first reviews of products posted by a reviewer to the total number of reviews that he/she has posted, review votes cast, and avatar picture provided [30]. Only a handful of studies have incorporated a few reviewer features into fake review detection models to date.

● Brand features are characteristics specifically related to target products or services that are reviewed, such as price, sales rank, and business/product type [28, 42].

Among the above types of features, review content features have been the most commonly used ones in building online fake review detection models.

## Nonmachine Learning Approaches

A couple of nonmachine learning approaches to fake review detection have been explored, such as pattern matching and graph-based methods. A pattern matching method for fake review detection relies on comparing review content similarity [28], which is based on the assumption that fake reviewers post similar fake reviews, or relies on temporal patterns of reviews [67] or follows certain rules [33]. This method is rarely used because it is only effective for certain types of review spamming activities such as duplicated review spams.

Graph-based methods have also been applied to fake review detection. Wang et al. [60] represented the relationships among reviewers, reviews, and stores (i.e., three types of nodes) with a heterogeneous graph. They explored how interactions among nodes could reveal the causes of fake reviews and proposed an iterative computation model to identify suspicious reviewers. Intuitively, a reviewer would be more trustworthy if he/she has written more honest reviews; a store would be more reliable if it has received more positive reviews from trustworthy reviewers; and a review would more likely be authentic if more honest reviewers support it. Nevertheless, their graph model did not use any review content features.

We make several observations through an extensive literature review. First, extant studies rely mainly on verbal features extracted from review text for building fake review detection models [46, 47, 54], while reviewers’ nonverbal features are significantly underused or under-studied. Research on deception detection suggests that characteristics of deceivers (e.g., fake reviewers) influence the outcome of deception detection (e.g., fake review detection) [4]. As online review platforms become more socially interactive, they offer increasing information about reviewers, particularly their nonverbal behaviors. Second, there is a lack of understanding of the relative impacts of reviewers’ verbal and nonverbal behaviors on fake review detection. Third, although various features have been employed in building models for fake review detection, feature selection has yet to be fully investigated for improving the performance and generality of detection models. This study aims to fill the above research gaps.

## Theoretical Foundation and Research Hypotheses

Many theories and models have been proposed to explain general deception behavior. Among them, interpersonal deception theory (IDT) [4] posits that deceivers display both strategic behaviors (e.g., information manipulation) and nonstrategic behaviors (e.g., leakage of nonverbal cues) during deception. Both types of behavior can serve as cues to deception. The concept of strategic behavior is grounded in the functionality of communication: a communicator’s plan and intentions are translated into behavioral routines (i.e., strategies) composed of specific actions (tactics). Information manipulation theory reflects the strategic element of deception in how interaction dictates messages crafted by deceivers [39]. Within this, deceivers are considered as uncooperative speaking partners who use verbal strategies that violate conversational assumptions. Nonstrategic behaviors include more commonly identified features of deceptive displays—nonverbal behavior leakage [4]. Such behaviors are difficult to control and thus can be particularly effective for deception detection [67]. In traditional face-to-face environments, nonverbal behaviors can be manifested by hand gestures, facial expressions, body movements, and so on [22]. However, they are often filtered by an online communication medium. On the other hand, some unique capabilities of online communication environments, such as reprocessability and rehearsability [11], enable alternative nonverbal behaviors. For example, review posting frequency and patterns can be viewed as nonverbal behaviors of online reviewers. In addition, a reviewer may interact with other reviewers through complimenting, responding to, or following others’ reviews, and/or adding other reviewers as friends.

To better understand and categorize behaviors of online reviewers for fake review detection, we draw on the key proposition of IDT—that both strategic and nonstrategic behaviors of deceivers can serve as cues to deception [4, 67]. Accordingly, we categorize predictive features for fake review detection into two general categories: verbal and nonverbal features. In the context of online reviews, verbal features include linguistic and content (e.g., lexical, syntactic, and semantic) features extracted from review text, and nonverbal features refer to reviewers’ behaviors that are indirectly engendered via posting reviews, such as social and review posting behaviors of reviewers on an online review platform. Social interaction with other reviewers may occur in both directions (from/to other reviewers). The majority of extant studies using machine learning approaches rely mainly on verbal features, whereas the impact of nonverbal features of reviewers on fake review detection is significantly under-studied. Therefore, the fundamental research question that this study endeavors to address is: Can nonverbal behaviors of reviewers serve as effective cues/features for fake review detection, and if so, to what extent?

Although many verbal features have been used in online fake review detection models and proven to be correlated with fake review behavior [46, 48], some researchers also found that suspicious reviewers on Yelp.com used language in their fake reviews very similar to that used in authentic reviews [47]. This finding implies that using only verbal features extracted from review content may not always be effective for fake review detection. Based on IDT, reviewers’ nonverbal features, as nonstrategic behaviors, should help reveal the deceptive intention of fake reviewers. Preliminary evidence shows that nonverbal features can help differentiate deception from truth in online text-based communication [64]. Therefore, we predict that nonverbal behavioral features of reviewers can help detect online fake reviews, as stated in the following hypothesis:

Hypothesis 1: Combining nonverbal features of reviewers with verbal features will improve the performance of online fake review detection in comparison to using verbal features alone.

Research on deception detection in online communication has shown that deceivers make an effort to disguise their deceptive intention by carefully editing and rehearsing their text messages [68]. An online review platform is an asynchronous communication environment, in which fake reviewers have plenty of time to edit and polish their fake reviews before submission in order to avoid being detected. In addition, these reviewers are also motivated to refer to other authentic reviews and guidelines on how to make their reviews look “real” while preparing fake reviews. Therefore, verbal behaviors exhibited in review text can be easily manipulated by reviewers who post fake reviews [64]. In contrast, it would be more difficult and costly for fake reviewers to manipulate their nonverbal behaviors that are not directly related to the current review. Therefore, we propose that effective nonverbal behaviors of reviewers would be more important for fake review detection than their verbal feature counterparts, which is stated in the second hypothesis:

Hypothesis 2: Compared with verbal features, nonverbal behavioral features of reviewers will be more important for the detection of online fake reviews.

## Method

Machine learning is the dominant approach to online fake review detection and has shown some success, whereas nonmachine learning approaches are still rare, immature, and limited in use. Thus, we adopted the machine learning approach in this study. In this section, we introduce the data sets, input features, and classification algorithms that we used to train and test fake review detection models.

## Data Set

One of the major challenges and difficulties in building a fake review detection model through machine learning lies in acquiring labeled reviews. Many existing approaches based on supervised machine learning techniques use pseudo-fake reviews rather than fake reviews filtered by a commercial website [47, 63]. Pseudo-fake reviews are either manually annotated [36, 61], or generated by Amazon Mechanical Turkers (AMT) [29, 46, 49]. Manual annotation of deception is fundamentally problematic. The same challenges for manual annotation in other domains also apply to the annotation of fake reviews [20]. Fake reviews are difficult to identify in the first place, and turkers are unlikely to have the same psychological state of mind as actual fake reviewers [47]. Therefore, detection models constructed by using pseudo-fake reviews, although they may result in higher accuracy than those constructed by using real-life fake reviews [46], may not be effective in detecting real-life fake reviews [47].

Given the above concerns (similar to [14, 30, 46, 47]), we chose to use real-life authentic and fake reviews collected from Yelp.com, which provides rich posting history and social behavior data of reviewers. Yelp.com had an average of 142 million monthly unique visitors in 2015 from 31 countries all over the world. Up to 2015, over 77 million reviews had been posted on Yelp.com. Yelp strives to provide users with trustworthy reviews through its review filtering process, which automatically filters out fake reviews and puts them in a separate category that is available to the public [47]. However, Yelp does not reveal the clues used by its filtering algorithm. Despite some false positives, Yelp’s review filter is considered highly accurate and reliable [46, 47]. For example, Mukherjee et al. [46] confirmed that the filtered Yelp reviews were strongly correlated with abnormal spamming behaviors. They conclude that Yelp fake review filtering is sufficiently reliable and provides possibly the closest to the ground-truth labels in the real-life setting. Therefore, it is reasonable to use online reviews categorized by Yelp for training and testing a fake review deception model [37, 46, 47].

Previous research [47, 49] has indicated that 400 authentic reviews and 400 fake reviews would be sufficient for training a fake review detection model. In this study, we randomly selected 1,033 authentic reviews and 1,100 fake reviews on restaurants from the Yelp review data set used by Mukherjee et al. [46, 47]. We used similar numbers of authentic and fake reviews to avoid the common data imbalance problem, which occurs when training a classification model with data samples that do not represent classes equally. The ratio of authentic reviews to fake reviews in Yelp is approximately 6:1. With such an unbalanced data set, a model will tend to classify the instances of the minority class (i.e., fake reviews) into the majority class (i.e., authentic reviews). The undersampling technique that randomly selects a subset of instances from the majority class to form a balanced class distribution data set is a well-known technique to deal with the data imbalance problem [47].

We performed review content analysis and feature extraction using the Natural Language ToolKit (NLTK 3.0),<sup>5</sup> which provides easy-to-use interfaces to over fifty corpora and lexical resources such as WordNet, a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, and wrappers for industrial-strength natural language processing libraries [40]. We validated the feature extraction results by manually checking a set of randomly selected twenty reviews. All the extracted feature values were confirmed.

## Predictive Features

Given the focus of this study, our selection of predictive features for fake review detection centered mainly on verbal and nonverbal behavioral features of reviewers. Verbal features were selected based on the findings of previous studies (e.g., [13, 19, 28, 30, 32, 42, 49]), which were extracted from review text. Nonverbal features were selected based on our prediction of their possible influence on fake review detection and their availability at Yelp. com. The two groups of selected features are presented in Table 1.

Among the selected nonverbal features, useful votes, average posting rate, tips count, elite reviewer term, positive-to-negative ratio, review updates, follower count, membership length, blog link, and counts of business photos, lists, compliments, and check-ins at a local business have rarely been studied before.

Table 1. Initial Set of Verbal and Nonverbal Features  
```txt
Categories Features
Verbal features (of a review) Review length: the total number of words
Average sentence length: average number of words per sentence
Noun ratio: the percentage of nouns
Noun, verb, personal pronoun, adjective, adverb, pronoun counts: the total number of nouns, verbs, personal pronouns, adjectives, adverbs, and pronouns
Subjectivity: the ratio of subjective to objective words
Lexical validity: the ratio of misspellings to the total number of words
sentiment orientation: the ratio of sentiment indicators to the total number of words
Lexical diversity: the ratio of unique words to the total number of words
Content diversity: the ratio of unique nouns and verbs to the total number of nouns and verbs
PoS (part of speech) n-gram diversity: the ratio of unique PoS bigrams to the total number of POS bigrams
Capitalized diversity: the ratio of the number of word tokens with initial capital letter(s) to the total number of tokens
Redundancy: the ratio of repeated tokens to the total number of tokens
Emotiveness diversity: the ratio of adjectives and adverbs to the total number of nouns and verbs
Self-reference diversity: the ratio of first-person pronouns to the total number of pronouns
Average content similarity: average similarity among the reviews posted by the same reviewer
Duplicated reviews (0/1): it takes the value of 1 if the content of a review is similar (more than 95 percent) to any other review on the same product (using cosine similarity), and 0 otherwise
```

<sub>rev</sub>i<sub>e</sub>w<sup>e</sup> <sub>ha</sub>vi<sup>ors</sup> <sub>o</sub>ci<sup>a</sup> <sub>ost</sub>i<sub>n</sub>g <sup>an</sup> <sub>e</sub>a<sup>ture</sup> <sub>onv</sub><sup>erb</sup>

## Classification Methods

In this study, we selected four classification algorithms, including support vector machine (SVM), Naїve Bayes (NB), decision tree, and random forest (RF). We chose them because they are the frequently used classification algorithms. Among them, SVM is the most commonly used classification algorithm for fake review detection (e.g., [6, 7, 15, 32, 33, 44–46, 48, 49, 62]), with NB (e.g., [28, 34, 35, 43, 46, 53, 56]) and decision tree (e.g., [5, 50, 51] are also often used. Naїve RF is an ensemble learning method for classification. Although few studies have applied RF for fake review detection, we selected it because some studies have reported that RF often produces better classification results than alternative algorithms such as NB and decision trees (e.g., [21, 39, 51]).

● SVM is regarded as an important example of “kernel methods” in statistical learning, one of the key areas in machine learning [2]. It is a discriminative classifier for binary classification formally defined by a separating hyperplane. The operation of the SVM algorithm is based on finding the hyperplane that separates m-dimensional data into two classes and gives the largest distance to the nearest training samples of the two classes. In this study, we used SVM with the radial basis function (RBF) as the kernel method.

● NB classifiers are probabilistic classifiers that apply the Bayes theorem [69]. As one of the oldest 415 classification algorithms, NB is easy to construct and does not need any complicated iterative parameter estimation schemes. Thus, they are highly scalable and can be trained efficiently. The NB classification technique is particularly suited when the dimensionality of inputs is high.

● A decision tree uses a treelike graph to model the reasoning process of mapping an input feature set to one of the predefined class labels. Each internal node of a decision tree represents a test on a feature of an item (e.g., an online review); outgoing branches of an internal node correspond to all possible outcomes of the feature testing; and each leaf node represents a class label, to which the current target item belongs. We chose the CART (classification and regression trees) algorithm in this study. It constructs a binary decision tree by splitting a node into two child nodes repeatedly, beginning with the root node that contains the whole learning sample.

● RF [1, 41] is an ensemble classifier that operates by constructing a number of decision trees at training time and outputting the class that is the mode of the classes generated by individual trees [3]. As a type of recursive partitioning method, RF constructs an ensemble of classification trees based on random subsets of data using a subset of randomly restricted and selected features for each split in each classification tree.

## Evaluation Metrics

The performances of the constructed fake review detection models were evaluated using four metrics that have been commonly used for evaluating classification models, including precision (P), recall (R), F-measure (F), and accuracy (A) [6], as defined in Equations (1)–(4). Precision is the percentage of total reviews detected as fake reviews that are indeed fake ones; recall is the percentage of total fake reviews in the data set that are correctly identified; F-measure is a harmonic mean of precision and recall; and accuracy is the percentage of correctly detected fake and authentic reviews among the total number of reviews examined.

$$
P = \frac {t p}{t p + f p}\tag{1}
$$

$$
R = \frac {t p}{t p + f n}\tag{2}
$$

$$
F = \frac {2 P R}{P + R}\tag{3}
$$

$$
A = \frac {t p + t n}{t p + t n + f p + f n},\tag{4}
$$

where $t p$ (true positive) denotes the number of correctly detected fake reviews; $f \dot { p }$ (false positive) denotes the number of authentic reviews that are incorrectly detected as fake reviews; $f h$ (false negative) represents the number of fake reviews that are identified as authentic reviews; and tn (true negative) represents the number of correctly classified authentic reviews. Values of these four measures range from 0 to 100 percent.

We used tenfold cross-validation in evaluation. The average performance of the ten models was reported for each of the four classification methods. In order to assess the impacts of incorporating nonverbal features of reviewers on fake review detection, we selected several baseline methods. One was the method proposed by Mukherjee et al. [47], which was selected for two main reasons: (1) it used only verbal features as predictive features and a data set from the same Yelp review corpus. The verbal features included word unigrams, bigrams, POS unigrams, LIWC features derived from analyzing review text, deep syntax features, and so on; and (2) it used SVM and achieved good performance in fake review detection. The other set of baseline models were constructed using our selected verbal features only (i.e., excluding nonverbal features) (Table 1) and using the same four classification algorithms and data sets. By comparing the performances of our proposed models and these baseline models for fake review detection, we were able to examine whether or not incorporating nonverbal behavioral features of reviewers could improve the performance of fake review detection.

## Results and Analyses

In this study, the development of fake review detection models went through three phases: (1) training and testing detection models using the full set of the selected predictive features and each of the four classification algorithms, then selecting the model with the best overall performance; (2) accessing the impacts of individual features from the best model on fake review detection performance using a sensitivity analysis technique, followed by feature pruning that only keeps the most influential ones; and (3) retraining and retesting the best-performing classifier using the pruned feature set. Below we report the detailed results of each of the above phases.

## Training and Testing Classification Models with the Full Set of Features

The primary objectives of this study are to build an effective online fake review detection model and examine the impact of individual verbal and nonverbal features on detection performance. We initially included all the selected features in the detection models.

The performances of the fake review detection models using the full feature set (only independent features were used for NB) are presented in Table 2. NB assumes that features are independent given the class variable, which has been perceived as unrealistic and mostly not held [57, 62]. Despite relatively frequent use of NB for online fake review detection (e.g., [28, 34, 35, 43, 46, 53, 56]), none of them examined feature independence and performed feature pruning in advance. In this study, we ran a Pearson correlation analysis on the initial full-feature set and removed those features that were highly correlated with others (i.e., coefficients ≥ 0.5). The remaining features were then used to train and test the NB model.

We conducted one-way analysis of variance (ANOVA) with post hoc Tukey HSD (honest significant difference) test on the performances of all models. The Tukey test results (see Table 3) show that the performances of the RF, CART, and SVM models are significantly better than that of the NB model across all performance measures $( p < 0 . 0 0 1$ for all except $p < 0 . 0 1$ for SVM vs. NB on Fmeasure). In addition, the RF model outperformed the SVM model in precision, F-measure, and accuracy $( p < 0 . 0 5 )$ . Although the performance of the CART model was better than that of SVM across all measures, the difference was not statistically significant $( p = \mathsf { n . s . } )$ . Similarly, the performance improvements of RF over CART across all four measures were not statistically significant $( p = { \mathfrak { n } } . { \mathfrak { s } } . )$ The above results reveal that RF produced the best overall model, and thus it was selected for subsequent analysis.

Table 2. Performances of Models with All Features vs. Verbal Features Only

<table><tr><td rowspan="2">Classification algorithms</td><td colspan="4">Verbal + nonverbal features (%)</td><td colspan="4">Verbal features only (%)</td></tr><tr><td>P</td><td>R</td><td>F</td><td>A</td><td>P</td><td>R</td><td>F</td><td>A</td></tr><tr><td>RF</td><td>87.12</td><td>89.63</td><td>88.31</td><td>87.81</td><td>77.83</td><td>89.70</td><td>83.33</td><td>77.27</td></tr><tr><td>CART</td><td>85.28</td><td>88.57</td><td>86.81</td><td>86.17</td><td>77.23</td><td>87.66</td><td>82.07</td><td>75.75</td></tr><tr><td>SVM</td><td>82.63</td><td>86.77</td><td>84.60</td><td>83.78</td><td>77.00</td><td>87.12</td><td>81.73</td><td>75.34</td></tr><tr><td>NB</td><td>58.51</td><td>85.30</td><td>67.10</td><td>70.36</td><td>51.96</td><td>78.14</td><td>62.40</td><td>65.50</td></tr></table>

Table 3. Tukey’s HSD Test of Model Performances (Mean Difference)

<table><tr><td>Comparisons</td><td>P</td><td>R</td><td>F</td><td>A</td></tr><tr><td>SVM-NB</td><td>24.12***</td><td>1.47***</td><td>17.5**</td><td>13.42***</td></tr><tr><td>RF-NB</td><td>28.61***</td><td>4.33***</td><td>21.21***</td><td>17.45***</td></tr><tr><td>CART-NB</td><td>26.77***</td><td>3.27***</td><td>19.71***</td><td>15.81***</td></tr><tr><td>RF-SVM</td><td>4.49*</td><td>2.86</td><td>3.71*</td><td>4.03*</td></tr><tr><td>CART-SVM</td><td>2.65</td><td>1.8</td><td>2.21</td><td>2.39</td></tr><tr><td>RF-CART</td><td>1.84</td><td>1.06</td><td>1.5</td><td>1.64</td></tr></table>

$^ { * * * } , ~ ^ { * * } ,$ and \*, denote significance at the .001, .01, and .05 levels, respectively.

Compared with the first baseline method (P: 64.9 percent, R: 81.2 percent, F: 72.1 percent, and A: 68 percent) [47], which used SVM with verbal features extracted from review text, the performance of our SVM model (P: 82.63 percent, R: 86.77 percent, F: 84.60 percent, and A: 83.78 percent) is significantly better across all four measures. This result suggests that the predictive features of our model are more effective for fake review detection.

The performances of other baseline methods (i.e., with verbal features only) are also reported in Table 2. We performed a paired-sample t-test to compare the performances of these baseline models against our trained models (combine verbal and nonverbal features). The results reveal that all our models trained by the four classification algorithms consistently outperformed their baseline counterparts $( p < 0 . 0 0 1 )$ in precision, F-measure, and accuracy across the four classification algorithms, but did not yield a statistically significant improvement in recall except for the NB model. The results show that nonverbal features have significant positive impacts on the performance of fake review detection. Therefore, H1 is supported in terms of precision, F-measure, and accuracy.

## Feature Ranking and Pruning via Sensitivity Analysis

In order to gain insights into the relative importance of individual features for fake review detection, which has rarely been examined in the literature, we selected the best performed RF model for feature ranking and pruning.

We performed a postmodeling sensitivity analysis using the varImp function in the Caret package to identify important features in the RF model, where the importance of each input feature to the model output was assessed in a systematic way. Based on the results of the sensitivity analysis, we ranked the input features and presented the top-twelve most important features along with their importance scores in Table 4, which produced the best model performance. As we further incorporated additional, the model performance would either level off or even get worse.

Among the top-twelve most important features, all except the tenth one (i.e., average content similarity) belong to the nonverbal feature category. By treating the remaining features as not important, we created a 2 × 2 contingency table using feature category and feature importance as the two dimensions, as shown in Table 5. We performed a one-sided Fisher’s exact test [16] to examine whether the relative proportion of nonverbal features among important features for fake review detection is statistically higher than that of verbal features. The test yielded a p-value less than 0.01. Thus, H2 is supported.

## Model Retraining with Pruned Features

Machine learning strives to develop parsimonious models while achieving goodnessof-fit. Parsimonious models are desirable because removing unnecessary complexity from models helps discriminate the signal from noise, leading to better prediction and generalization performance.

Table 4. The Most Important Features (Restaurant Reviews)

<table><tr><td>Rank</td><td>Features</td><td>Importance scores</td></tr><tr><td>1</td><td>Useful votes</td><td>280.23</td></tr><tr><td>2</td><td>Review burstiness</td><td>232.57</td></tr><tr><td>3</td><td>Cool votes</td><td>66.77</td></tr><tr><td>4</td><td>Friend count</td><td>51.68</td></tr><tr><td>5</td><td>Review count</td><td>48.58</td></tr><tr><td>6</td><td>Funny votes</td><td>41.35</td></tr><tr><td>7</td><td>Review duration</td><td>32.27</td></tr><tr><td>8</td><td>Average posting rate</td><td>20.82</td></tr><tr><td>9</td><td>Membership length</td><td>18.44</td></tr><tr><td>10</td><td>Average content similarity</td><td>15.60</td></tr><tr><td>11</td><td>Positive ratio</td><td>15.03</td></tr><tr><td>12</td><td>Positive-to-negative ratio</td><td>13.72</td></tr></table>

Table 5. A 2 × 2 Contingency Table

<table><tr><td></td><td>Important</td><td>Not important</td><td>Row total</td></tr><tr><td>Verbal features</td><td>1</td><td>20</td><td>21</td></tr><tr><td>Nonverbal features</td><td>11</td><td>15</td><td>26</td></tr><tr><td>Total</td><td>12</td><td>35</td><td>47</td></tr></table>

After trimming the feature set from original forty-seven down to the top twelve features, we repeated the model training and testing procedure using the RF classification method on the same data set. A side-by-side comparison of performances of the original RF model against the pruned RF model is shown in Figure 1. The average false negative and false positive rates of the pruned model are 6.03 percent and 11.98 percent, respectively. A paired-sample t-test did not yield any significant difference in detection performance between the two models $( p = \mathrm { n . s . ) }$ .

## Validation

To further validate our findings about the importance of nonverbal features for online fake review detection, we crawled additional 1,299 reviews on hotels from Yelp.com, with 530 of them being fake reviews. Then, we repeated the same set of analyses performed on the restaurant reviews as described earlier on these new hotel reviews. The performances of models constructed using all features and verbal features only are presented in Table 6 (the NB model used only independent features). The t-test results of performance improvement by combining nonverbal and verbal features over using verbal features only are reported in Table 7.

The results are largely consistent with those of restaurant reviews, which show that RF produced the best overall model and NB produced the worst. The t-test results show that incorporating nonverbal features of reviewers improved the detection performance of RF, CART, and SVM models in terms of precision, F-measure, and accuracy, compared with using verbal features alone.

Based on the results of sensitivity analysis on the RF model, we selected the toptwelve most important features that led to the best performance $( P = 8 6 . 0 1 $ percent, R $= 8 9 . 8 9 $ percent, $F = 8 7 . 8 7$ percent, and $A = 8 3 . 9 9$ percent) (see Table 8).

![](/api/attachments/QAVYFSSE/fulltext/images/72fbf9b1f19a69b7ed97b9203b8898359d490972724f8bb756e2e1f899d68393.jpg)  
Figure 1. Performance Comparison Before and After Pruning

Table 6. Performances of Models using both Verbal and Nonverbal Features vs. Verbal Features Only

<table><tr><td rowspan="2">Algorithms</td><td colspan="4">Verbal + nonverbal features (%)</td><td colspan="4">Verbal features only (%)</td></tr><tr><td>P</td><td>R</td><td>F</td><td>A</td><td>P</td><td>R</td><td>F</td><td>A</td></tr><tr><td>RF</td><td>86.53</td><td>89.47</td><td>87.94</td><td>84.19</td><td>74.54</td><td>89.56</td><td>81.33</td><td>73.45</td></tr><tr><td>CART</td><td>85.79</td><td>88.37</td><td>86.95</td><td>82.85</td><td>75.18</td><td>88.25</td><td>81.11</td><td>73.52</td></tr><tr><td>SVM</td><td>81.86</td><td>88.14</td><td>84.84</td><td>79.65</td><td>72.12</td><td>90.19</td><td>80.12</td><td>71.12</td></tr><tr><td>NB</td><td>85.97</td><td>32.58</td><td>44.09</td><td>52.58</td><td>42.69</td><td>84.65</td><td>56.73</td><td>54.72</td></tr></table>

Table 7. Performance Improvements After Incorporating Nonverbal Features (Mean Difference)

<table><tr><td>Algorithms</td><td>P</td><td>R</td><td>F</td><td>A</td></tr><tr><td>RF</td><td>+11.99***</td><td>-0.09</td><td>+6.61***</td><td>+10.74***</td></tr><tr><td>CART</td><td>+10.61***</td><td>+0.12</td><td>+5.84***</td><td>+9.33***</td></tr><tr><td>SVM</td><td>+9.74***</td><td>-2.05</td><td>+4.72**</td><td>+8.53***</td></tr><tr><td>NB</td><td>+43.28***</td><td>-52.07***</td><td>-12.64**</td><td>-2.14</td></tr></table>

\*\*\*, \*\*, and \*, denote significance at the .001, .01, and .05 levels, respectively.

As shown in Table 8, ten out of the twelve most important features belong to the nonverbal feature category. A comparison of the list of the top features identified from hotel reviews against that identified from restaurant reviews (Table 4) reveals that the two lists share ten out of twelve most important features, including nine nonverbal features and one verbal feature. On the other hand, the comparison also reveals a few differences. In particular, two nonverbal features, namely positive ratio and positive-to-negative ratio, were important for restaurant reviews only, while capitalized diversity (verbal feature) and tips count (nonverbal feature) were important for hotel reviews only. A Fisher’s exact test of the selected most important features shows a significant difference in the relative proportions of nonverbal and verbal features $( p < 0 . 0 5 )$ . A t-test of performances of the RF model in fake review detection before and after feature pruning did not yield a statistical significant difference $( p = \mathsf { n . s . } )$ . Therefore, these results confirm the findings from the restaurant reviews.

Table 8. The Top-Twelve Most Important Features (Hotel Reviews)

<table><tr><td>Ranks</td><td>Features</td><td>Importance scores</td></tr><tr><td>1</td><td>Useful votes</td><td>153.94</td></tr><tr><td>2</td><td>Review count</td><td>46.13</td></tr><tr><td>3</td><td>Average posting rate</td><td>45.10</td></tr><tr><td>4</td><td>Review duration</td><td>43.03</td></tr><tr><td>5</td><td>Reviewing burstiness</td><td>37.60</td></tr><tr><td>6</td><td>Cool votes</td><td>23.78</td></tr><tr><td>7</td><td>Membership length</td><td>23.35</td></tr><tr><td>8</td><td>Funny votes</td><td>21.39</td></tr><tr><td>9</td><td>Friend count</td><td>18.63</td></tr><tr><td>10</td><td>Capitalized diversity</td><td>14.66</td></tr><tr><td>11</td><td>Average content similarity</td><td>13.12</td></tr><tr><td>12</td><td>Tips count</td><td>13.10</td></tr></table>

## Discussion

There has been increasing research on online fake review detection since the first study on this phenomenon published in 2007 [29]. This is mainly due to the increasing importance of online reviews to consumer purchase decisions, the growing threat of online fake reviews, as well as the difficulty in manually detecting fake reviews. These fake reviews can severely damage the credibility of online consumer reviews and compromise their potential value for businesses and individual consumers.

This study makes several research contributions, particularly from theoretical, methodological, and behavioral perspectives. First, this study extends IDT and the notion of nonverbal behavior to the context of online fake review detection. IDT suggests the potential of nonverbal behaviors of deceivers as leakage cues to deception in face-to-face communication. Recent studies of deception detection in online communication (e.g., instant messaging and online chat) [17, 18, 25, 68] have provided preliminary evidence for the feasibility and importance of discovering nonverbal behaviors from online communication and incorporating them into online deception detection. Drawing upon IDT, this study categorizes predictive features for online fake review detection into verbal and nonverbal categories. However, the vast majority of existing approaches to online fake review detection heavily or solely rely on verbal features [10, 32, 36, 49, 60]. Nonverbal features of reviewers have been either largely ignored or understudied. The findings on the impact of nonverbal behaviors of reviewers on the detection of online fake reviews provide strong evidence that IDT can be used to explain online fake reviews.

Second, the findings of this study demonstrate that incorporating nonverbal features can significantly improve the performance of fake review detection models. In other words, nonverbal behaviors of reviewers are complementary to their verbal behaviors for the detection of fake reviews, which deserve significant attention. On the other hand, verbal features remain useful because the models built solely using verbal behavioral features still achieved a decent level of performance which is comparable to those of the state-of-the-art models using verbal features only in the literature (e.g., [5, 35, 62]). In addition, there are verbal features make the list of most important features.

Third, the study reveals that nonverbal features can be more effective for detecting online fake reviews than verbal features. One possible explanation is that fake reviewers tend to write multiple fake reviews. As fake reviewers gain more experience and skills in manipulating review content to evade detection, the effectiveness of verbal features would decrease. In contrast, nonverbal behaviors of reviewers are more difficult and costly to manipulate or fabricate, and accordingly are more robust and reliable as cues for detecting fake reviews. Additionally, we explored a dozen nonverbal behavioral features of reviewers that have not been studied previously, such as positive-to-negative ratio, useful votes, and membership length, which have been proven to be important and effective cues for online fake review detection.

Fourth, this research offers insights into the impacts of individual features on the performance of fake review detection, which fills a gap in the literature. The findings from the sensitivity analyses show that individual features have varying levels of impact on detection performance. Specifically, top-ranked nonverbal features have a stronger influence than their verbal counterparts. The findings from online restaurant reviews were validated using hotel reviews, providing evidence for the generality of the proposed method.

Fifth, model parsimony has received little attention in the extant literature on fake review detection. In this study, we built parsimonious RF detection models using the top most influential features identified from sensitivity analyses, and more importantly, they achieved similar detection performances and model goodness-of-fit to those of the original models built with the full feature set.

The above findings provide multiple practical implications for how to improve the effectiveness of online fake review detection and how to create trustworthy online review platforms. First, developing automated models for online fake review detection can help consumers eliminate inherent truth bias in detecting fake reviews. Second, given that different features have varying levels of importance to fake review detection, designers of fake review filtering systems should focus on the most influential features as cues to online fake reviews, as identified through this study. Third, the importance of nonverbal features discovered in this study suggests that online review platforms should facilitate and encourage social interactions among reviewers and between reviewers and prospect consumers in order to supply rich nonverbal behaviors for the detection of fake reviews. Fourth, for researchers who are interested in building machine learning models for online fake review detection, the findings of this study suggest that incorporating more predictive features into a fake review detection model does not necessarily lead to the improved performance. What really matters to detection performance is the relevance and importance of predictive features. Simpler models are likely more efficient and generalizable, which helps improve the usability of fake review detection systems. Last but not least, the findings of this research indicate that it would be beneficial to combine verbal and nonverbal features in building fake review detection models. Verbal features are still helpful, especially when there are limited access to nonverbal features of reviewers.

This study has some limitations that offer potential opportunities for future research. We used reviews collected from Yelp.com only. Among existing online review platforms, the website provides one of the richest collections of posting behaviors and social activities of individual reviewers. Some reviewer features included in our models may not be available in another online review platform. As a result, the findings of this study may not be directly applicable to fake review detection on other platforms. Nevertheless, the main contribution of this study lies in a new theory-driven method for designing and building effective online fake review detection models. Thus, we expect that the importance of nonverbal behaviors of reviewers to fake review detection discovered in this study can be generalized to other online review platforms, which is worthy of future investigation. In addition, it looks promising to develop a taxonomy of nonverbal behaviors to guide future research in this area.

## Conclusion

This study performs an in-depth investigation of the impacts of verbal and nonverbal behavioral features of online reviewers on fake review detection by using labeled Yelp.com reviews as the ground truth. This is the first study that theorizes predictive features as verbal and nonverbal categories for building fake review detection models. Our results show that nonverbal features of reviewers are very effective in detecting online fake reviews. On the other hand, verbal features, which have been emphasized in online fake review detection literature, may become less effective as fake reviewers gain experience with manipulating the content of reviews. Our findings provide several research and practical implications for improving the trustworthiness of online review platforms and the performance of online fake review detection.

Acknowledgment: Any opinions, findings or recommendations expressed here are those of the authors and not necessarily those of the sponsor of this research.

## Funding

This study was supported by the National Science Foundation (Award #695SES 1527684).

## NOTES

1. www.bbc.com/news/technology-22166606/.

2. www.nytimes.com/2010/08/27/technology/27ftc.html?\_r=0/.

3. http://blogs.wsj.com/wallet/2009/07/09/delonghis-strange-brew-tracking-down-fakeamazon-raves/.

4. www.thestar.com/business/2013/09/23/fake\_online\_reviews\_exposed\_by\_new\_york\_ attorney\_general.html.

5. www.nltk.org.

6. Example: www.yelp.com/user\_local\_photos?userid=GlPKDZwvK\_QsLkjHm6xsRA

## REFERENCES

1. Alpaydin, E. Introduction to Machine Learning. Cambridge, MA: MIT Press, 2009.

2. Banerjee, S., and Chua, A.Y.K. A study of manipulative and authentic negative reviews. In Proceedings of the Eighth International Conference on Ubiquitous Information Management and Communication. Cambodia, January 9–11, 2014.Article No. 76.

3. Breiman, L. Random forests. Machine Learning, 45, 1 (2001), 5–32.

4. Buller, D.B., and Burgoon, J.K. Interpersonal deception theory. Communication Theory, 6, 3 (1996), 203–242.

5. Chen, L.S., and Lin, J.Y. A study on review manipulation classification using decision tree. Proceedings of the Tenth IEEE International Conference on Service Systems and Service Management (ICSSSM). Hong Kong, July 17–19, 2013, pp. 680–685.

6. Chen, Y., and Chen, H. Opinion spam detection in web forum: A real case study. Proceedings of WWW, May 18–22, 2015, Florence, Italy, pp. 173–183.

7. Chen, C.; Wu, K.; Srinivasan, V.; and Zhang, X. Battling the Internet water army: Detection of hidden paid posters. Proceedings of the 2013 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining. Niagara Falls, Canada, August 25–28, pp. 116–120.

8. Cone Research. Game changer: Corn survey finds 4-out-of-5 consumers reverse purchase decisions based on negative online reviews. 2011. www.conecomm.com/contentmgr/ showdetails.php/id/4008 (accessed on September 15, 2015).

9. Cui, G.; Lui, H.-K.; and Guo, X. The effect of online consumer product reviews on new product sales. International Journal of Electronic Commerce, 17, 1 (2012), 39–58.

10. Dave, K.; Lawrence, S.; and Pennock, D.M. Mining the peanut gallery: Opinion extraction and semantic classification of product reviews. Proceedings of the Twelfth International Conference on World Wide Web, Budapest, May 20–24, 2003, pp. 519–528.

11. Dennis, A.R.; Robert M. Fuller; and Valacich, J.S. Media, tasks, and communication processes: A theory of media synchronicity. MIS Quarterly, 32, 3 (2008), 575–600.

12. Duan, H., and Zirn, C. Can we identify manipulative behavior and the corresponding suspects on review websites using supervised learning? Lecture Notes in Computer Science, 7617 (2012), pp. 215–230.

13. Fei, G.; Mukherjee, A.; Liu, B.; Hsu, M.; Castellanos, M.; and Ghosh, R. Exploiting burstiness in reviews for review spammer detection. Proceedings of the International AAAI Conference on Weblogs and Social Media (ICWSM-2013), Boston, MA, July 8–10, 2013, pp. 175–184.

14. Feng, S., Banerjee, R., and Choi, Y. Syntactic stylometry for deception detection. Proceedings of the Fiftieth Annual Meeting of the Association for Computational Linguistics. Jeju, Republic of Korea, July 8–14, 2012, pp. 171–175.

15. Feng, S.; Xing, L.; Gogar, A.; and Choi, Y. Distributional footprints of deceptive product reviews. Proceedings of the Sixth International AAAI Conference on Weblogs and Social Media. June 4–8, 2012, Dublin. pp. 98–105.

16. Fisher, R.A. On the interpretation of χ<sup>2</sup> from contingency tables, and the calculation of P. Journal of the Royal Statistical Society, 85, 1 (1922), 87–94.

17. Fuller, C.M.; Biros, D.P.; Burgoon, J.; and Nunamaker, J. An examination and validation of linguistic constructs for studying high-stakes deception. Group Decision and Negotiation, 22, 1 (2013), 117–134.

18. Fuller, C.M.; Biros, D.P.; and Delen, D. An investigation of data and text mining methods for real world deception detection. Expert Systems with Applications, 38, 7 (2011), 8392–8398.

19. Ghose, A., and Ipeirotis, P. Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions on Knowledge and Data Engineering, 23, 10 (2011), 1498–1512.

20. Gokhman, S.; Hancock, J.; Prabhu, P.; Ott, M.; and Cardie, C. In search of a gold standard in studies of deception. Proceedings of the Workshop on Computational Approaches to Deception Detection, Stroudsburg, PA, April 23, 2012, pp. 23–30.

21. Gupta, D.L.; Malviya, A.; and Singh, S. Performance analysis of classification tree learning algorithms. International Journal of Computer Applications, 55, 6 (2012), 39–44.

22. Hocking, J.E., and Leathers, D.G. Nonverbal indicators of deception: A new theoretical perspective. Communication Monographs, 47, 2 (1980), 119–131.

23. Hu, M., and Liu, B. Mining and summarizing customer reviews. Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge discovery and Data Mining, Seattle, WA, August 22–25, 2004, pp. 168–177.

24. Huang, L.; Tan, C.H.; Ke, W.; and Wei, K.K. Comprehension and assessment of product reviews: A review-product congruity proposition. Journal of Management Information Systems, 30, 3 (2013), 311–343.

25. Humpherys, S.L.; Moffitt, K.C.; Burns, M.B.; Burgoon, J.K.; and Felix, W.F. Identification of fraudulent financial statements using linguistic credibility analysis. Decision Support Systems, 50, 3 (2011), 585–594.

26. Hunt, K.M. Gaming the system: Fake online reviews v. consumer law. Computer Law and Security Review, 31, 1 (2015), 3–25.

27. Jensen, M.L.; Averbeck, J.M.; Zhang, Z.; and Wright, K.B. Credibility of anonymous online product reviews: A language expectancy perspective. Journal of Management Information Systems, 30, 1 (2013), 293–324.

28. Jindal, N., and Liu, B. Opinion spam and analysis. First ACM International Conference on Web Search and Data Mining (WSDM-2008), Stanford, CA, February 11–12, 2008, pp. 219–230.

29. Jindal, N., and Liu, B. Review spam detection. Proceedings of WWW-2007, Banff, Canada, May 8–12, 2007, pp. 1189–1190.

30. Kamerer, D. Understanding the Yelp review filter: An exploratory study. First Monday, 19, 9 (2014). http://firstmonday.org/article/view/5436/4111.

31. Lappas, T. Fake reviews: the malicious perspective. Proceedings of the Seventeenth international Conference on Applications of Natural Language Processing and Information Systems. Groningen, June 26–28, 2012, pp. 23–34.

32. Lau, R.Y.K.; Liao, S.Y.; Kwok, R.C.-W.; Xu, K.; Xia, Y.; and Li, Y. Text mining and probabilistic language modeling for online review spam detection. ACM Transactions on Management Information Systems, 2, 4 (2011), 1–30.

33. Li, H.; Chen, Z.; Liu, B.; Wei, X.; and Shao, J. Spotting fake reviews via collective positive-unlabeled learning. IEEE International Conference on Data Mining (ICDM). Shenzhen, December 14–17, 2014, pp. 899–904.

34. Li, F.; Huang, M.; Yang, Y.; and Zhu, X. Learning to identify review spam. Proceedings of the Twenty-Second International Joint Conference on Artificial Intelligence. Barcelona, July 16–22, 2011, pp. 2488–2493.

35. Li, J.; Ott, M.; Cardie, C.; and Hovy, E. Towards a general rule for identifying deceptive opinion spam. Proceedings of the Fifty-Second Annual Meeting of the Association for Computational Linguistics. Baltimore, June 23–25, 2014, pp. 1566–1576.

36. Lim, E.-P.; Nguyen, V.-A.; Jindal, N.; Liu, B.; and Lauw, H. Detecting product review spammers using rating behaviors. Proceedings of the Nineteenth ACM International Conference on Information and Knowledge Management (CIKM-2010), Toronto, Canada, October 26–30, 2010, pp. 939–948.

37. Luca, M., and Zervas, G. Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Science, published online on January 28, 2016. http://dx.doi.org 10.1287/mnsc.2015.2304

38. Ma, X.; Khansa, L.; Deng, Y.; and Kim, S. Impact of prior reviews on the subsequent review process in reputation systems. Journal of Management Information Systems, 30, 3 (2013), 279–310.

39. McCornack, S. Information manipulation theory. Communication Monographs, 59, 1 (1992), 1–16.

40. Mihalcea, R., and Strapparava, C. The lie detector: Explorations in the automatic recognition of deceptive language. Proceedings of the ACLIJCNLP 2009 Conference, Singapore, August 2–7, 2009, pp. 309–312.

41. Mitchell, T.M. Machine Learning. Burr Ridge, IL: McGraw-Hill, 1997.

42. Mukherjee, A.; Kumar, B.; Liu, B.; Wang, J.; Hsu, M.; Castellanos, M.; and Ghosh, R. Spotting opinion spammers using behavioral footprints. Proceedings of the SIGKDD

International Conference on Knowledge Discovery and Data Mining (KDD-2013), Chicago, IL, August 11–14, 2013, pp. 632–640.

43. Mukherjee, A., & Liu, B. Modeling review comments. Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics. 1 (2011), pp. 320–329

44. Mukherjee, A.; Liu, B.; and Glance, N. Spotting fake reviewer groups in consumer reviews. Proceedings of the International World Wide Web Conference (WWW-2012), Lyon, France, April 16–20, 2012, pp. 191–200.

45. Mukherjee, A.; Liu, B.; Wang, J.; Glance, N.; and Jindal, N. Detecting group review spam. Proceedings of WWW 2011, Hyderabad, India, March 28–April 1, 2011, pp. 93–94.

46. Mukherjee, A.; Venkataraman, V.; Liu, B.; and Glance, N. Fake review detection: Classification and analysis of real and pseudo reviews Technical report. University of Illinois at Chicago, 2013.

47. Mukherjee, A.; Venkataraman, V.; Liu, B.; and Glance, N. What Yelp fake review filter might be doing. Proceedings of the International AAAI Conference on Weblogs and Social Media (ICWSM-2013), Boston, MA, July 8–10, 2013.

48. Ott, M.; Cardie, C.; and Hancock, J. Estimating the prevalence of deception in online review communities. Proceedings of WWW 2012, Lyon, France, April 16–20, 2012, pp. 201–210.

49. Ott, M.; Choi, Y.; Cardie, C.; and Hancock, J. Finding deceptive opinion spam by any stretch of the imagination. Proceedings of the Forty-Ninth Annual Meeting of the Association for Computational Linguistics: Human Language Technologies, Portland, OR, June 19–24, 2011, pp. 309–319.

50. Patil, M.S., and Bagade, A. Online review spam detection using language model and feature selection. International Journal of Computer Applications, 59, 7 (2012), 33–36.

51. Rahman, M.; Carbunar, B.; Ballesteros, J.; Burri, G.; and Chau, D.H.P. Turning the tide: Curbing deceptive Yelp behaviors. Proceedings of SIAM Data Mining Conference (SDM). Philadelphia, April 24–26, 2014, pp. 244–252.

52. Rish, I.; Hellerstein, J.; and Thathachar, J. An analysis of data characteristics that affect Naïve Bayes performance. Proceedings of the Eighteenth Conference on Machine Learning– ICML 2001, Williamstown, MA, June 28–July 1, 2001, pp. 30–37.

53. Sharma, K., and Lin, K. Review spam detector with rating consistency check. Proceedings of ACMSE’13, Savannah, GA, April 4–6, 2013, pp. 30–37, Article No. 34.

54. Shojaee, S.; Murad, M.A.A.; Azman, A.B.; Sharef, N.M.; and Nadali, S. Detecting deceptive reviews using lexical and syntactic features. Proceedings of the Thirteenth International Conference on Intelligent Systems Design and Applications (ISDA), Banji, December 8–10, 2013, pp. 53–58.

55. Spirin, N., and Han, J. Survey on web spam detection: principles and algorithms. ACM SIGKDD Explorations Newsletter, 13, 2 (2012), 50–64.

56. Sun, H.; Morales, A.; and Yan, X. Synthetic review spamming and defense. Proceedings of SIGKDD 2013. Chicago, August 11–14, 2013, pp. 1088–1096.

57. Tsuruoka, Y., and Tsujii, J. Training a naive Bayes classifier via the EM algorithm with a class distribution constraint. Proceedings of the Seventh Conference on Natural Language Learning at HLT-NAACL, Edmonton, Canada, May 31–June 1, 2003, pp. 127–134.

58. Wakade, S.; Liszka, K.J.; and Chan, C.C. Application of learning algorithms to image spam evolution. In Ramanna, S., Jain, L.C., and Howlett, R.J. (ed.) Emerging Paradigms in Machine Learning, Berlin: Springer, 2013, pp. 471–495.

59. Wang, G.; Xie, S.; Liu, B.; and Yu, P.S. Review graph based online store review spammer detection. Proceedings of ICDM-2011, Vancouver, Canada, December 11–14, 2011, pp. 1242–1247.

60. Wang, G.; Xie, S.; Liu, B.; and Yu, P.S. Identify online store review spammers via social review graph. ACM Transactions on Intelligent Systems and Technology, 3, 4 (2011), 1–21.

61. Wu, G.; Greene, D.; Smyth, B.; and Cunningham, P. Distortion as a validation criterion in the identification of suspicious reviews. Proceedings of the First Workshop on Social Media Analytics. Washington, DC, July 25, 2010, pp.10–13.

62. Xu, C. Detecting collusive spammers in online review communities. Proceedings of the Sixth Workshop on Ph.D. Students in Information and Knowledge Management, San Francisco, CA, October 27–November 1, 2013, pp. 33–40.

63. Yoon, K., and Gretzel, U. Comparison of deceptive and truthful travel reviews. International Conference on Information and Communication Technologies in Tourism, Amsterdam, 2009, pp. 37–47.

64. Zhou, L. An empirical investigation of deception behavior in Instant Messaging. IEEE Transactions on Professional Communication, 48, 2 (2005), 147–160.

65. Zhou, L.; Shi, Y.; and Zhang, D. Catch deceptive messages online. Proceedings of the Fourteenth Workshop on Information Technology and Systems (WITS 2004). Washington, DC, 2004, pp. 230–235.

66. Zhou, L.; Burgoon, J.K.; Nunamaker, J.F.; and Twitchell, D. Automated linguistics based cues for detecting deception in text-based asynchronous computer-mediated communication: An empirical investigation. Group Decision and Negotiation, 13, 1 (2004), 81–106.

67. Zhou, L.; Sung, Y.; and Zhang, D. Deception performance in online group negotiation and decision making: The effects of deception experience and deception skill. Group Decision and Negotiation, 22 (2013), 153–172.

68. Zhou, L., and Zhang, D. Following linguistic footprints: Automatic deception detection in online communication. Communications of the ACM (CACM), 51, 9 (2008), 119–122.

69. Zhu, F., and Zhang, X. Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74, 2 (2010), 133–148.
