---
otero_id: 16770
otero_key: "V9J9K6X8"
title: "Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering"
authors: "Ajay Kumar; Ram D. Gopal; Ravi Shankar; Kim Hua Tan"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113728"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering

![](/api/attachments/V9J9K6X8/fulltext/images/d6960bb297b7170c0f2d5890ef5d0d3e74329bce0fd1f7104d7692b967e00443.jpg)

Ajay Kumar <sup>a,\*</sup>, Ram D. Gopal <sup>b</sup>, Ravi Shankar <sup>c</sup>, Kim Hua Tan <sup>d</sup>

<sup>a</sup> EMLYON Business School, Ecully, France

<sup>b</sup> Warwick Business School, University of Warwick, Coventry, United Kingdom

<sup>c</sup> Department of Management Studies, IIT Delhi, New Delhi, India

<sup>d</sup> University of Nottingham Business School, Nottingham, United Kingdom

## A R T I C L E I N F O

Keywords: Online reviews Digital platforms Review manipulation Machine learning Opinion spamming Feature engineering

## A B S T R A C T

Reading customer reviews before purchasing items online has become a common practice; however, some companies use machine learning (ML) algorithms to generate false reviews in order to create positive brand images of their own products and negative images of competitors' offerings. Existing techniques use review content to identify fraudulent reviewers; however, spammers become more intelligent, started to learn from their mistakes, and changed their tactics in order to avoid detection techniques. Thus, investigating fraudulent accounts' behaviour of generating fake negative or positive reviews for competitors or themselves and the necessity of ML classifiers to identify fraudulent reviews, is more important than ever. In this research, we present a novel feature engineering approach in which we (1) extract several “review-centric” and “reviewer-centric” features from a dataset; (2) combine the cumulative effects of features distributions into a unified model that represents overall behavior of the fraudulent reviewers; (3) investigate the role of effective data pre-processing to improve detection accuracy; and (4) develop a probabilistic approach to detect fraudulent reviewers by learning a novel M-SMOTE model over a derived balanced dataset and feature distributions, which outperforms other ML models. Our study contributes to the literature on digital platforms and fraudulent review detection with significant managerial and theoretical implications through these novel findings.

## 1. Introduction

Product reviews can make or break a business in the world of ecommerce. According to a study by BrightLocal [46], 91% of consumers report that positive reviews make them more likely to use a business, 82% will reject a business based on negative reviews, and 76% trust online reviews as much as personal recommendations. Consumers depend on online reviews to decide which movies they should watch, where to go for dinner, what to read, where to go on vacation, and which company's products they should purchase. Products with higher per centages of good reviews top the search results on websites like Amazon and Yelp, which essentially earns them an abundance of free exposure, as they are “highlighted” or “recommended” and even promoted in emails. Many companies feel unable to respond to negative reviews, which can destroy their reputations and diminish their profits.

In 2016, Alibaba highlighted the increasing proliferation of false reviews when it sued a third-party service provider for linking its merchants with people who were willing to falsify purchases and post positive comments to boost their rankings [9]. In what is commonly called a “brushing operation”, real customers paid for their transactions on Alibaba, submitted their positive reviews and ratings, and then recouped their money through electronic credits or other e-currency forms. Similarly, Amazon filed a lawsuit in 2015 against over a thousand Fiverr users for offering to post fraudulent reviews [10]. In 2019, the US Federal Trade Commission successfully brought the first-ever case of using fraudulent Amazon reviews to advertise an online product, whereby a company paid a third-party website to write five-star Amazon reviews for a weight-loss supplement that was widely advertised as enhancing weight loss, but actually causes acute liver failure [15]. The impact of such operations is twofold: they swell transaction figures on the vendor platform and artificially lift sellers' rankings. In the former case, the platform's reputation can be damaged, as news of such activ ities makes customers question its legitimacy. Whereas existing tech nologies can often detect individual incentivized reviewers, on a larger scale, opinion spammers tamper with existing systems to produce negative reviews, and the amount of fraudulent reviews produced by machines is substantially increasing.

In order to combat online review manipulation, many companies are seeking more effective strategies for identifying fraudulent reviews and reviewers [28]. Information systems (IS) domain is an emerging area of research in this area. Opinion mining and sentiment analysis have increased, and a wide range of algorithms is used to detect spammer's activity. However, spammers have become increasingly diligent in adapting their tactics to avoid detection techniques [20].

One of the most important elements of fraudulent review detection models is feature engineering, which entails a procedure of transforming raw data into novel features and selecting the best variables that improve the ML classifier's accuracy. A number of existing studies of fraudulent review detection have applied supervised ML algorithms as their baseline either with or without performing feature-engineering techniques [3,41,49,52], and there have also been some contributions on unsupervised ML algorithms [2,14,29,51,58]. A few studies have examined non-ML techniques with derived features [30,48]. However, comprehensive studies of feature engineering, particularly the distri butional characteristics of reviewers' features with data pre-processing challenges and class imbalanced problems, remain limited in the liter ature. Fraudulent reviews tend to deform a feature's underlying natural distribution [30], and a few studies have analyzed underlying distri butions in online product reviews such as power law and J-shaped dis tributions [11,23]. Feng et al. [16] elucidated the characteristics of natural opinion distribution with respect to TripAdvisor hotel reviews and Amazon product reviews, and Dalvi et al. [11] devised an average rating distribution in domains such as restaurants and movies. These studies concluded that rating distributions are heavily skewed by highly imbalanced datasets; however, they did not specifically devote attention to understanding how underlying distributions are related to the detection of fraudulent reviewers.

Overall, we found that no comprehensive distributions that consider specific aspects of feature engineering and imbalanced classification have been conducted to identify fraudulent reviews and opinion spam mers. To address this gap, we aimed to devise an approach for detecting potentially fraudulent reviews using an innovative feature engineering approach. A M-SMOTE (modified- synthetic minority over-sampling technique) model inclusive of a combination of several univariate user-reviewing distribution-based transformation of features is devel oped to detect fraudulent reviews based on patterns in online review data produced by the skewing of features. Our primary objective is to investigate the potential for using the review- and reviewer-centric features of users to develop fraudulent review detection models, and our second objective was to investigate the impact of data preprocessing and feature engineering tasks on ML classifiers to identify fraudulent reviews with high accuracy and develop an M-SMOTE model to solve the class imbalance problem. We empirically tested the model's ability to glean underlying distributional aspects of reviewer behavior and then applied it on a Yelp dataset and several other benchmarking datasets to analyze the impact of data pre-processing challenges in classification performance.

## 2. Related literature

A number of existing studies have examined ML techniques to detect fraudulent reviews and reviewers. Supervised ML methods include support vector machines (SVM) [20,32,35,41], logistic regression [6,20,26,41] ordinal multilevel regression [43], k-nearest neighbor [49,50], random forest [22,60], decision trees and J48 [5,26] naïve Bayes [50,61], boosting & bagging algorithms [18,19], and artificial neural networks (ANN) [36,52]. The considerable body of literature on unsupervised ML algorithms includes the FRAUDEAGLE clustering method [3], SPEAGLE clustering [51], the unified unsupervised review deviation model [40], dynamic k-value aggregation [21], the lexicon based unsupervised model [24], a statistics-based unsupervised clus tering algorithm [13], the unsupervised topic-sentiment joint probabi listic model [14], mixture models [29], and the unsupervised matrix iteration algorithm [58].

The majority of previous research has applied traditional supervised and unsupervised ML techniques to solve the problem of fraudulent reviewer detection using linguistic features (word unigrams and bigrams, LIWC features and POS features), user-behavior features (average review length, standard deviation in ratings etc.) and others reviewer-centric features. Jindal and Liu [23] experimented with su pervised ML techniques to identify opinion spam by manually labelling an Amazon dataset based on a linguistic and behavioral analysis of fraudulent reviewers. Ott et al. [47] used basic features such as unig rams, bigrams, trigrams and part-of-speech (POS) to develop a SVM based classifier to detect fraudulent reviews on a TripAdvisor dataset, and Li et al. [34] developed a supervised ML-based framework with a co training method to identify fraudulent reviewers and reviews based on pre-identified features. Lin et al. [39] proposed six features (personal content similarity, product review similarity, similarity with reviews on other products, reviewer's review frequency, product review frequency, and repeatability) and experimented with traditional supervised ML algorithms to detect fraudulent reviews. Abbasi et al. [2] extracted several unique features and used statistical learning theory to develop a fraudulent website detector system. Zhang et al. [60] used supervised ML techniques (SVM, decision tree and random forest) with verbal (n grams and POS) and non-verbal features to detect fraudulent reviews on a balanced (equal number of fraudulent and real reviews) Yelp dataset. Kumar et al. [28] similarly used a Yelp dataset to apply several tradi tional ML techniques (logistic regression, k-NN, boosting algorithms, SVM etc.) with univariate features (including review gap, review count, rating entropy, rating deviation, time of review, and user tenure) to detect fraudulent reviews. Siering et al. [53] used several linguistic features (complexity, expressivity and diversity) in textual information with ML methods to examine the manipulation in crowdfunding pro jects, and Ren and Ji [52] developed a LIWC framework based on POS, n-grams, and psychological features. Finally, Li et al. [36] used unigram, POS. and LIWC to create a deep learning model to detect fraudulent reviews on hotel and restaurant datasets.

We have observed several limitations in the information systems (IS) literature for detecting fraudulent reviews using feature engineering with review-centric features, reviewer-centric features, and behavioral characteristics. Although a few studies have demonstrated the use of advanced ML and deep learning techniques to detect fraudulent reviews [7,36,56,59,62], research with novel feature sets and feature engineer ing remains uncommon. In addition, to the best of our knowledge, although a few studies in the IS domain have used traditional ML techniques with pre-existing feature sets to detect fraudulent reviews or reviewers, accounting for data imbalance problem and other data pre processing challenges remains insufficiently explored.

Our study diverges from previous research in that rather than using pre-determined features, we incorporate several review- and reviewercentric features as well as fraudulent reviewer behavioral characteris tics into a ML model. The main advantages of our proposed model over other ML algorithms are its capacity to learn high-level features from balanced datasets and execute part of the feature engineering on its own. The proposed model scans the data to search for important features that have some correlations and combine them to improve the accuracy of the ML classifiers without being specifically instructed to do so. Similar studies by Kumar et al. [28,29] cannot be considered conclusive because they did not focus on solving any data pre-processing challenges and they only highlighted the skewed distribution of some features to improve the accuracy of machine learning classifiers.

Our proposed research also differs from the existing literature by focusing on fraudulent review detection in a hierarchical manner using a novel feature engineering method that is very helpful for improving the accuracy of classifiers. Zhang et al.'s [60] research can be considered a first step towards a more profound understanding of review-centric and reviewer-centric features; however, a number of questions regarding data pre-processing and improving the accuracy of ML classifiers remain to be addressed. Similarly, Kumar et al.'s [28,29] contribution to the engineering literature mainly focused on only one dimension (positive and negative skewed distribution of features), and although they used some transformed reviewer-centric features to understand the univari ate and joint behavior of features, they devoted less attention toward improving the accuracy of ML classifiers with other feature engineering tasks. To the best of our knowledge, no previous research has investi gated the importance of feature engineering and class imbalance for detecting fraudulent reviewer's behavior. Thus, the use of data preprocessing methods to exploit features in fraudulent review prediction is a promising area of research.

## 3. Conceptual background and research hypotheses

Features drawn from skewed distributions with imbalanced classi fications that are directly used in ML algorithms tend to decrease pre diction accuracy, which is illustrated in our baseline model with an undisturbed natural distribution of features. Initially, we built ML models with natural transformations and imbalanced datasets. and then we added new, transformed features and a balanced dataset to perform machine learning. Fig. 1 illustrates the proposed research framework, showing both scenarios, i.e., a) class imbalanced and b) transformation using distributional characteristics of relevant univariate features. The results will show that our proposed model with specific review and reviewer-centric features outperforms the traditional ML models that do not use normalized, transformed features and balanced datasets. Data pre-processing and feature engineering are the most crucial parts of any data science project, and the data on which it operates is the heart and soul of any machine-learning problem. The data used to construct the ML model plays the most critical part in determining its predictive power. The better the features we generate, the more accurate the results we obtain. However, some questions continue to be debated [1,31]: To what extent can data be operated on; How far can we generate the features; and how many features are sufficient? Data pre-processing is highly impacted by the hypothesis generation, which is a desire to utilize existing data to learn a trend that would best map the inputs to outputs. The more we invest in hypothesis-development, the better features we generate, and the greater accuracy we achieve for our predictive model.

Accordingly, we propose several research hypotheses and contribu tions. First, we developed a comprehensive set of features, including some novel review-centric features as well as reviewer-centric features that previous studies have used to identify the characteristics of fraud ulent reviewer accounts. Second, we tried to address the question of whether reviewer-centric features are more useful than review-centric features for detecting fraudulent reviews, as stated in the following hypotheses:

Hypothesis 1. Compared with review-centric features, reviewer-centric features of users are more important for detecting fraudulent reviewers behavior.

Hypothesis 2. Combining reviewer-centric with review-centric features will improve the accuracy of ML detection models in comparison with using review-centric features alone.

Third, we developed a rule-based ML framework that highlights the role of data pre-processing tasks for enabling marketing managers to easily detect fraudulent reviews, as stated in the following hypotheses:

Hypothesis 3. Compared with symmetric distribution, features from skewed distributions that are directly used in machine learning will reduce the accuracy of predictive models.

Hypothesis 4. Compared with imbalanced and raw (not pre-processed) data, balanced and processed data (after solving all pre-processing challenges) will lead to better prediction and improved accuracy.

To summarize, our main contributions are as follows:

1. We developed a novel probabilistic approach to detect fraudulent reviewers by learning a proposed M-SMOTE ML algorithm over a derived balanced dataset and feature distributions. We tested four hypotheses and extracted some unique review- and reviewer-centric features and behavioral characteristics of opinion spammers that are very helpful for detecting the fraudulent reviewers in the proposed framework.

2. We performed a comprehensive experimental evaluation of our approach on real-world restaurant reviews taken from Yelp.com and combined the cumulative effects of several feature distributions into a unified model that represents the overall behavior of the fraudulent reviewer. Specifically, we extracted 12 unique features and devel oped several ML models on a balanced dataset. Furthermore, we compare our approach with those of six previous studies that have evaluated Yelp and Amazon reviews, namely Feng et al. [16], Akoglu et al. [3], Rayana and Akoglu [51], Zhang et al. [60], Kumar et al. [28,29], demonstrating that our model outperforms all of them in terms of accuracy and other statistical metrics.

Our findings provide several managerial and practical implications to help practitioners and marketing managers more effectively combat fraudulent reviews on e-commerce websites. Overall, our proposed model will improve revenue-generating opportunities and customer experience for both digital platforms and businesses.

## 4. Data description and model development

One of the important challenges of building ML models for identi fying fraudulent reviews is obtaining reviews that have been clearly identified as being fraudulent. Several existing models have used pseudo-fraudulent reviews that were either manually annotated or generated by Amazon Mechanical Truckers rather than officially filtered fraudulent reviews [44,45].

However, using a manually annotated dataset in our research would have been fundamentally problematic. Previous studies [44,60] sug gested that when Amazon Truckers write fraudulent reviews in com parison to actual fraudulent writers, the accuracy of predictive models is generally much higher than the accuracy of models developed on realworld fraudulent review because Amazon MT have different psycho logical states of mind when they write the fake reviews in comparison to actual fraudulent review writers. We decided to use the real-world dataset that Rayana and Akoglu [51] collected from Yelp.com, which provides several behavioral characteristics of fraudulent accounts. Our data encompasses 5044 restaurants in four U.S. states, namely Con necticut, New Jersey, Pennsylvania, and Virginia, and entries from 260,277 reviewers who posted from 2010 to 2014. The original dataset had only six variables: user ID, product ID, rating, label, date, and text review; however, we extracted 12 new features (six review-centric and six reviewer-centric features) for our fraudulent review detector models. We observed that 35,600 reviews (\~6%) have single star ratings, 42,985 s (\~7%) have two-star ratings, 83.139 (\~14%) have three-star ratings, 217,465 (\~35%) have four-star ratings, and 229,409 reviews (\~38%) have five-star ratings. Fig. 1 illustrates the four stages of model development: (i) text data pre-processing; (ii) feature extraction or new variable creation; (iii) feature engineering for improving the ML accu racy; and (iv) fraudulent review detection model development. This framework receives restaurant reviews and the relevant information of each reviewer as input. For the first task, we created six reviewer-centric features (rating entropy, review gap, review count, rating deviation, time of review, and user tenure) and six review-centric features (word density, review length (number of words), parts-of-speech ratio, ratio of positive and negative words, sentiment score, and SpamHitScore).

Scenario (hypothesis)-1: Does features from skewed distributions and directly used in ML reduce the accuracy of predictive models?

Scenario (hypothesis)-2: Does having balanced data lead to better prediction?

Scenario (hypothesis)-3: Does having more features lead to a better prediction?

Scenario (hypothesis)-4: Does data pre-processing improve accuracy of ML classifiers?

![](/api/attachments/V9J9K6X8/fulltext/images/50dad151a18fe80c64f38f704691297725f6a70e7c44ea0e496e4d611895eb6b.jpg)  
Fi<sub>g.</sub> 1 <sub>.</sub> P<sub>ropose</sub>d f<sub>rau</sub>d<sub>u</sub>l<sub>en</sub>t <sub>rev</sub>i<sub>ew</sub> d<sub>e</sub>t<sub>ec</sub>ti<sub>on</sub> <sub>mo</sub>d<sub>e</sub>l b<sub>ase</sub>d <sub>on</sub> M-SMOTE <sub>a</sub>l<sub>gor</sub>ith<sub>m</sub>.

Several steps are needed to extract the review-centric features from raw text, namely tokenization, stop-word removal, stemming and lemmati zation. Tokenization is the process of splitting a sentence, paragraph, or an entire text document into individual words or terms, which are called tokens. Stop-word removal is the process of removing “noise” words (e. g., is, are, am, this, that, a, an, the), and stemming is the process of removing the word suffixes to retain base words. Lemmatization is similar to stemming in that it groups together the different forms of a word; however, it brings context to the words and links words that have similar meaning [4].

In the next stage of the proposed framework, we present a dashboard of several data pre-processing solutions that will help remove noise, inconsistency, outliers, missing values, skewed distribution, class imbalance, correlated variables, and multicollinearity and then create several hypotheses based on data pre-processing and machine learning classifier performance. In the final stage, we develop a number of ma chine learning models for identifying fraudulent reviewers from the dataset and use the case of majority voting to assess the performance of the best three machine learning classifiers. We apply a simple rule of hard voting for predicting the class label Y via majority voting of three best classifiers [Y = mode{M1(X),M2(X),M3(X)}]. For example, if our three best ML classifiers give the prediction results if Classifier\_1 = Fraudulent (1), Classifier\_2 = True (0) and Classifier\_3 = True (1), then we would use the majority vote concept and the final prediction result would be Y = mode {1, 0, 1} =1. This would be the fourth prediction result, and we would consider it the final output of our ensemble vote classifier. Along with developing the fraudulent review predictive model, we will test all four hypotheses in the final stage of the proposed framework.

## 4.1. Review- and reviewer-centric feature generation

We initially extract various univariate and multivariate features to predict suspicious activity based on different characteristics of review ing behavior. We include six features, namely rating entropy, user tenure, review gap, time of review, review count and rating deviation, to which we added word density, parts-of-speech ratio, extremity of rating, ratio of positive and negative words, sentiment score and SpamHitScore. We empirically identify the best fitting distribution family for statistics related to both older and new features. Our study not only focuses on developing a ML detector model that introduces several new review centric features, but also contributes to the distribution-based trans formation of existing features. In this section, we explain the univariate and bivariate review- and reviewer-centric features used in our analysis.

## 4.1.1. Reviewer-centric features

(i) Rating entropy: Luca and Zervas [42] empirically proved that honest reviewers are highly likely to balance their activity be tween critical or noncritical reviews, whereas fraudulent re viewers generally post uniformly extreme reviews aiming to artificially either enhance or damage a company's ratings. The entropy rate for fraudulent reviews tends to be small due to the lack of balance.

(ii) Review gap: Mukherjee et al. [45] showed that fraudulent re viewers are usually not registered on an e-commerce website for a long period of time; thus, suspicious behavior is indicated in cases when a reviewer has posted all of their reviews within a short time span. Real reviewers generally only use their accounts from time to time to post reviews, so if reviews are posted over a relatively long timeframe, we can consider that normal activity.

(iii) Review count: Mukherjee et al. [44,45] demonstrated that paid and fraudulent users generally write more reviews than real re viewers. Thus, number of reviews associated with a particular account could be an important factor to distinguish fraudulent and real reviews.

(iv) Rating deviation: Let us take an example of a reviewer whose general trend is to give a low rating to every restaurant he/she reviews without accounting for the ratings given by others. These reviewers should be detected because their ratings deviate from the restaurant's average ratings. If there is a case with a greater number of real than fraudulent reviewers, chances are high that we will detect instances in which a rating significantly deviates from all the other ratings. According to Lim et al. [38], we count this metric as an absolute difference between the review score given by a user to a restaurant and an overall average score credited to the restaurant.

(v) Time of review: Lim et al. [38] and Mukherjee et al. [44] demonstrated that spammers tend to write reviews early after a product or service is introduced to maximize their impact on a consumer's perception of a product. Thus, we should be alert if we notice a user who always posts restaurant reviews before any other user. We capture this in our model with the use of difference between the time a reviewer reviews a restaurant and the very first review posted for that restaurant in the form of days.

(vi) User tenure: This feature denotes the amount of time a user is active on an online forum [17,25]. Fraudulent reviewers generally use short-lived accounts with a comparatively high volume of reviews and handles on a particular e-commerce website to avoid detection via ML algorithms. Hence, to identify fraudulent re viewers, we take the time period in the form of number of days the user is active as a feature.

## 4.1.2. Review-centric features

(i) Review length (number of words): One observation that we considered is the amount of words put in the reviews. According to Jindal and Liu [23], fraudulent reviewers are likely to write less detailed reviews, whereas a genuine reviewer will write a more detailed review. Unigrams and bigrams are specifically considered in the review text data for counting the total number of unique words.

(ii) Word density: This important text feature denotes the average length of the words used in each review [23]. Word density is calculated by number of characters divided by number of words in each review. We set the calculation formula for “word density” as (char count)/(word count +1) to avoid division by zero, as some reviews might not have punctuations.

(iii) Part-of-speech ratio: The main objective of part-of-speech ratio is to extract the linguistic characteristics of fraudulent reviews and identify the grammatical groups of given words. According to Zhang et al. [60], we can count the number of all of these char acteristics individually and divide the sum by the word count to assign a corresponding score to the instances.

(iv) Ratio of positive and negative words: We use the sentiment dictio nary to calculate the “ratio of positive words” and “ratio of negative words” and then divide them by the number of words in each review [55].

(v) SpamHitScore: Jindal and Liu [23] showed that some companies hire professionals to regularly write fraudulent reviews. In such cases of repeated practice, fraudulent reviewers tend to use particular word or phrase patterns. To model this suspicious behavior, we use bigram sets with corresponding words & ex pressions. We use a dictionary to break each review into corre sponding N-gram and calculate the score after checking for the presence or absence of a particular word or expression in the fraudulent or real review. The resulting score indicates how much a particular review is different or similar to the spam or fraudu lent review.

(vi) Sentiment probability: Zhang et al. [60] showed the importance of this variable to predict the fraudulent reviewer’ behavior in their research. To calculate the probability of a review (A) being positive or negative based on B (the length of the review), we can use the conditional probability P(A|B) = P(A and B)/P(B). We use the sentiment dictionary to teach the model how a positive/ negative review looks based on the words it contains. When we run the classifier on each review, it returns the sentiment (posi tive/negative) along with a probability of how confident the classifier is while making this decision, the latter of which com prises the sentiment score. Tables 1 and 2 present the detailed summary statistics of reviewer- and review-centric pre-processed features, respectively.

## 5. Feature engineering, M-SMOTE algorithm development, hypotheses testing, experimentation, and results

Machine learning often entails working with imbalanced, nonnormal, and skewed datasets; however, sending raw or real-world data to the model without processing might result in errors and false results. Feature engineering transforms real-world data into a machine under standable format. Because our dataset is highly imbalanced and we have highly skewed features, we need to solve all data pre-processing chal lenges before developing the ML models. This work is presented step-bystep in the below subsections.

## 5.1. Step 1: creation of new variables (extracting new features)

One of the main contributions of this study is to build novel and univariate review- and reviewer-centric features and distributional as pects to detect fraudulent reviewers and their behavior. To illustrate the efficiency and robustness of our proposed approach, reviewers' features and their distributional characteristics are used to address the following questions: (1) Do features from skewed distributions that are directly used in machine learning reduce the accuracy of predictive models? (2) When characterizing overall spammer behavior, what is the specific contribution of each feature? We develop a framework in which uni variate features are transformed according to their underlying proba bility distribution by generalizing the features in accordance with distribution transformations and the whole process is discussed in next sections.

## 5.2. Step 2: treatment of missing values, outliers and Feature ranking and dimensionality reduction

Rather than immediately scaling the data, we first dealt with the outliers. Outliers significantly contribute to skewness; however, some outliers might actually contribute to the model's learning. Considering both the scenarios, we first visualized the outliers for each feature/col umn with the help of boxplots to glean distortions in the data and then applied log transformation on the complete dataset to help retain novel outliers and enhance the Gaussian distribution. Next, we obtained the interquartile ranges for outlier removal and then used the “Remov eWithValue” filter to removed 36,382 outliers and 10,353 extreme values from the dataset. In order to gain insights into the relative importance of individual features, we used the model-agnostic feature importance score to determine the univariate importance of each feature with respect to the target variable. As seen in Table 3, our ranking system resulted in reducing the initial 19 features to the top 12 (six review-centric and six reviewer-centric) features that produce the best performance results on predictive models. Next, we used the heat map to analyze correlations and multicollinearity among features, and observed that there are no strong positive or negative correlations among the features.

Table 1  
Summary statistics of reviewer-centric features.

<table><tr><td>Features</td><td>Max</td><td>Min</td><td>Mean</td><td>SD</td></tr><tr><td>Review count</td><td>2</td><td>4.64</td><td>6.43</td><td>165</td></tr><tr><td>User tenure</td><td>0</td><td>328.37</td><td>1613</td><td>1613</td></tr><tr><td>Rating deviation</td><td>0</td><td>0.82</td><td>0.44</td><td>3.3</td></tr><tr><td>Review gap</td><td>0</td><td>140.07</td><td>211.08</td><td>1594</td></tr><tr><td>Time of review</td><td>0</td><td>745.7</td><td>372.14</td><td>1611</td></tr><tr><td>Rating entropy</td><td>0.45</td><td>1.17</td><td>0.69</td><td>5.08</td></tr></table>

Table 2  
Summary statistics of review-centric features.

<table><tr><td>Features</td><td>Max</td><td>Min</td><td>Mean</td><td>SD</td></tr><tr><td>Review length</td><td>1</td><td>117</td><td>108</td><td>5333</td></tr><tr><td>Word density</td><td>0.50</td><td>5.40</td><td>2.91</td><td>810</td></tr><tr><td>Part-of-speech ratio</td><td>0</td><td>0.08</td><td>0.04</td><td>0.50</td></tr><tr><td>Ratio of positive words</td><td>0</td><td>0.02</td><td>0.04</td><td>0.36</td></tr><tr><td>Ratio of negative words</td><td>0</td><td>0.01</td><td>0.03</td><td>0.30</td></tr><tr><td>Spam hit score</td><td>0</td><td>72.99</td><td>66.85</td><td>3224</td></tr><tr><td>Sentiment score</td><td>0.50</td><td>0.83</td><td>0.14</td><td>1</td></tr><tr><td>Ratio of nouns</td><td>0</td><td>0.25</td><td>0.07</td><td>0.92</td></tr><tr><td>Ratio of verbs</td><td>0</td><td>0.17</td><td>0.05</td><td>0.75</td></tr><tr><td>Ratio of adverb</td><td>0</td><td>0.08</td><td>0.04</td><td>0.67</td></tr><tr><td>Ratio of adjectives</td><td>0</td><td>0.11</td><td>0.05</td><td>0.99</td></tr></table>

Table 3  
Ranking of most important review-centric and reviewer-centric features.

<table><tr><td>Rank</td><td>Features</td><td>Important Scores</td></tr><tr><td>1</td><td>Review count</td><td>85.23</td></tr><tr><td>2</td><td>Review gap</td><td>57.66</td></tr><tr><td>3</td><td>Review count</td><td>46.55</td></tr><tr><td>4</td><td>SpamHitScore</td><td>42.45</td></tr><tr><td>5</td><td>Rating deviation</td><td>37.12</td></tr><tr><td>6</td><td>Review length</td><td>28.56</td></tr><tr><td>7</td><td>Rating entropy</td><td>24.46</td></tr><tr><td>8</td><td>User tenure</td><td>22.12</td></tr><tr><td>9</td><td>Time of review</td><td>14.66</td></tr><tr><td>10</td><td>Word density</td><td>14.23</td></tr><tr><td>11</td><td>Sentiment score</td><td>13.49</td></tr><tr><td>12</td><td>Ratio of positive words</td><td>13.01</td></tr></table>

## 5.3. Step 3: operating features individually

The goal of standardization or normalization is to bring variables to similar scale when comparing measurements across units. There is high chance of bias when variables are with different scales and hence do not contribute equally and fairly to model performance. When features have different ranges, the algorithm's learning rate is determined by the feature with the largest range; thus, scaling the data speeds up the al gorithm's training time and improves the overall accuracy of the model. After performing previous steps, the data are normally distributed for half of the features; however, other techniques are needed to achieve bell curves for the remaining features. To achieve normalization, we used min-max scaling and later applied a “yeo-johnson” power trans formation for negatively skewed data and a “box-cox” power for posi tively skewed data. In cases of rigidly skewed data, we applied a multi step power transformation to bring it within normal distributed range (i. e., − 0.5–0.5). Figs. 2 and 3 illustrate the transformed reviewer- and review-centric features, respectively. We can see that all features now have a normal distribution, and they can now be used to develop our fraudulent review prediction models.

## 5.4. Step 4: solving the class imbalance problem

Class imbalance occurs in supervised machine learning when sam ples or observations in one class are much higher than the other class. ML algorithms are biased towards majority class samples, which they accurately predict, and tend to ignore minority class samples, resulting in significant misclassifications. Three well-known methods to handle class imbalances are SMOTE, undersampling, and oversampling [27].

![](/api/attachments/V9J9K6X8/fulltext/images/70bd0e2ddece718fe6b872fb234a81805b6a0b96ddddd967b97a8035a2212cda.jpg)  
(a)

![](/api/attachments/V9J9K6X8/fulltext/images/59e704b5141ece10c8cae55131039731eff4617c5c71954f67894382943edb0d.jpg)  
(b)

![](/api/attachments/V9J9K6X8/fulltext/images/f2aa26e91e31be6561d009c775d0df939808a9552bc0b0bd34df1a63dc7eb33d.jpg)  
(c)

![](/api/attachments/V9J9K6X8/fulltext/images/6ed50869f7798ce7776f6ad587e5e53245b5fb95969ee7b1360cd9a5720982db.jpg)  
(d)

![](/api/attachments/V9J9K6X8/fulltext/images/3d760c257fc9a7fd87699ecf10b0258b1d956d2adc3932a13aaac758f8f64e91.jpg)  
(e)

![](/api/attachments/V9J9K6X8/fulltext/images/6c4470d6f3415f28b147e3be9c82453d1f55623c2a2fc3c28633ff8c464e77db.jpg)  
(f)

Fig. 2. Transformed reviewer-centric features.  
![](/api/attachments/V9J9K6X8/fulltext/images/69db4b93baf998b8e49382faebb637dd2f2cdec6edf884aad844e7886fb9be94.jpg)  
(a)

![](/api/attachments/V9J9K6X8/fulltext/images/0371afde78857be76949db8fb140e6f61d5a80dc032e92acd6a829da401fe426.jpg)  
(b)

![](/api/attachments/V9J9K6X8/fulltext/images/fccaccb445e73c92bfad6d92191f6ffb79cedac916fb79eabb4bdf85422a7211.jpg)  
(c)

![](/api/attachments/V9J9K6X8/fulltext/images/0f3b57dc513dc710eac934228d89a7df68c4cb52bc822880376e7fcc1c017133.jpg)  
(d)

![](/api/attachments/V9J9K6X8/fulltext/images/ee21b194ce0aa1d675c5d16e26b737342f67c6f107fc9beba3e68ebb6c21bab1.jpg)  
(e)  
Fig. 3. Transformed review-centric features.

![](/api/attachments/V9J9K6X8/fulltext/images/9967a2b3f45c6e0a3d969ae19128a1cd7446850f7cb2f935b1a7203ae0b180b2.jpg)  
(f)

SMOTE creates “synthetic” samples in minority class rather than by over-sampling with replacement [8]. Undersampling balances class distribution by randomly removing majority class examples, whereas oversampling entails randomly adding minority class samples. With a ratio of 91:9 between majority and minority instances, our Yelp dataset was highly imbalanced. We developed a modified form of SMOTE called M-SMOTE, which gives better results compared with the above described methods. After applying the M-SMOTE algorithm in the steps elucidated below, the imbalance ratio is reduced to 71:29 instances.

Fig. 4 depicts a flowchart of the M-SMOTE algorithm. First, the initial imbalanced dataset is classified by the GaussianProcessClassifier algo rithm, and the minority misclassified samples are grouped into a single sample set. The K nearest neighbor samples are generated for each of the misclassified samples. Second, following noise removal, we use the kmeans algorithm to find the center (c) of the misclassified samples. We then calculate the cosine similarity distance d (distance from data point $\because a ^ { \prime \prime }$ to center $\ " \mathrm { c } \ : \mathrm { ) }$ from the center sample to each of the minority sam ples, and calculate the average d\_mean of all distances. Next, we calculate the ratio between average d\_mean (Average of all “d”) and Euclidean distance. Fourth new instances are generated in the following process: (a) We count the values of the neighbor samples of the minority sample (u\_s) and save it by number $" \mathbf { n } ^ { \prime \prime }$ of minority class in the neighbor sample. We can get an idea of the number of minority samples after calculating the value of $\ " \mathbf { n . } \ "$ If the value of “n” is large, then we provide the smaller weight to generate the minority instances; if the value of $" \mathbf { n } ^ { \prime \prime }$ is small, then the function should generate more samples. (b) The most similar neighbors are again used in generating new instances in the formula shown in Eq. (6).

$$
\begin{array}{r l} & \mathrm {t = u + random(0,M[i]* 0.2)*(u_ {-s} - u)x_ {-new}} \\ & = \mathrm {u + random(0,M[i]* 0.8)*(t - c)} \end{array}\tag{6}
$$

where, u = the minority data point, u\_s = the most similar neighbor of u, c = the minority cluster center, M[i] = the d/d\_mean for a specific data point at index $\mathbf { \hat { i } } , \mathbf { \vec { d } } =$ the distance from data point $\mathbf { \ddot { u } } ^ { , 3 }$ to center $" \mathbf { c } _ { 3 } "$ d\_mean = the average of all $\mathrm { \ddot { c } d } , \mathrm  \ddot { }$ and x\_new = the newly generated instance.

Next, steps 3 and 4 are repeated until we reach the difference of instances between minority and majority instances. We have to remove the newly generated boundary instances until the minority and majority class instances are balanced. Finally, we integrate the newly generated data with the previous dataset to create a final dataset. LR-SMOTE uses very similar principles to generate a new minority class instance; how ever, it solves noise generation by first removing the noise from the original dataset and then performing weighted multiplication to over sample the minority class [37]; however, this method does not take care of the noise that it has generated itself while performing weighted multiplication. Our M-SMOTE works in a similar pattern as LR-SMOTE; however, it takes care to minimize the noise generated due to newly generated minority instances, thereby avoiding the production of redundant data. To improve the denoising technique used in LR-SMOTE, we changed the classification algorithm from SVM to GaussianProces sClassifier. SVM's less competent classification could bottleneck the denoising algorithm and data generation, and GaussianProcessClassifier performs better even in complex and rich features datasets. In addition, we use the Cosine similarity rather than Euclidean distance to find the most similar neighbors to use for generating new instances. Unlike LR-SMOTE and SMOTE, in which the newly generated data points will al ways be on the same line connecting the data points used $( \mathrm { u } \mathrm { ~ i } )$ and the center, in our case, the data points will not be on a same line; the most similar neighbor will contribute in the direction, which empowers the data distribution and guarantees a better overall data density that en ables easy classification. The LR-SMOTE formula adds a small scaler value to the original point to generate a new point; however, this will only generate points in same direction of a line connecting the center and the original point. To overcome that problem, we consider both a vector value (which gives direction towards a similar looking point) and a scaler value. For further verification that our M-SMOTE algorithm can be universally applicable on several imbalanced datasets, we tested six datasets from the UCI machine learning repository [54]. As shown in Table 4, our proposed M-SMOTE algorithm performs better than SMOTE according to the precision, recall, F-1, and AUC values. Whether we use the XGBoost or random forest predictive model, the AUC score obtained is higher in the modified dataset.

![](/api/attachments/V9J9K6X8/fulltext/images/cc1a8dc28da8cfc46414598db6d5ac37c9bbf13342fb957fc6cb6ca85cbd5b72.jpg)  
Fig. 4. Flow chart of the main steps of M-SMOTE algorithm.

## 5.5. Step 5: model development

To evaluate the performance of several ML classifiers with and without data pre-processing and feature engineering solutions, we apply the 5-fold (k = 5) cross validation procedure, whereby the algorithm randomly chooses four partitions for training purposes whereas the fifth is used for testing. The algorithm repeats this procedure five times in order to use each partition. We then take the average performance of the particular ML model on each partition and use it to measure the average F-1 score and AUC with the best threshold or hyper parameter for all runs. Below, we analyze the empirical results of applying several data pre-processing techniques and feature engineering tasks in three experimental scenarios.

## 5.5.1. First scenario- no pre-processing

Table 5 shows the results of performing classification with and without using any feature engineering on the dataset. Compared with the first baseline algorithm (P: 73.2%, R: 70.7%, F-1: 72.1%, and AUC: 79.6%), which used XGBoost with all 12 features extracted from the review text and without any data pre-processing and feature engineer ing, the performance of the same XGBoost model is significantly better across all four measures after solving all data pre-processing challenges and feature engineering tasks. This result supports our first two hy potheses that feature engineering improves the accuracy of ML classi fiers and that features from skewed distributions that are directly used in ML reduce the accuracy of predictive models. The results also support our third hypothesis that data pre-processing and feature-engineering steps improve the accuracy of all ML classifiers.

5.5.2. Second Scenario: outliers & extreme value treatment + standardization/scaling + normalization + class imbalance treatment ➔ model development using M-SMOTE algorithm

The first part of Table 6 shows that the performance of the same XGBoost model (is significantly increased across all four measures after solving the class imbalance problem using the M-SMOTE technique. The results support the fourth hypothesis that if we solve the class imbalance problem, we can improve the classifier accuracy and model interpret ability and decrease the misclassification rate of all ML models.

We next present the result of classifying fraudulent reviewers using our proposed model that applies feature engineering and majority voting (Table 7). In this stage, we develop a number of machine learning models for identifying the fraudulent reviewers from the dataset after solving all data pre-processing challenges & feature engineering tasks and then use the case of majority voting on the best three machine learning classifiers' performance. Table 5 shows that score of XGBoost, LSTM and Light GBM models provide the best results on the Yelp dataset, so we select these, apply the majority voting rule on them, and calculate the accuracy of the final predictive model. We apply a simple rule of hard voting for predicting the class label Y via majority voting of three best classifiers [Y = mode{M1(X),M2(X),M3(X)}]. For example, if our three best machine learning classifiers give the prediction results as follows: if Classifier1 = Fraudulent (1), Classifier2 = True (0) and Classifier3 = True (1) then we would use the majority vote concept and the final prediction result would be Y = mode {1, 0, 1} =1. This would be the fourth prediction result, and we would consider it final output of our ensemble vote classifier in our proposed framework for detecting the fraudulent reviews. The left side of Table 7 shows that the XGBoost has the best chance of being able to distinguish between fraudulent review and real review class on the Yelp dataset, followed by the LSTM and Light GBM models, respectively. The right side of Table 7 shows the results of the last majority vote step of our proposed fraudulent review detection model. The overall results show an improvement of 2–6% with our proposed model compared to the baseline approaches.

To further validate our hypotheses (H1 and H2) concerning the relative importance of reviewer-centric features vs review-centric fea tures and the benefits of combining the features. we test the combined effect of all features for improving the accuracy of all machine learning classifiers, we repeated the same set of data pre-processing and feature engineering tasks on both datasets. Table 8 shows that the results of reviewer-centric features are significantly better than those of the review-centric features across all four measures after separately applying the same machine learning algorithms on both datasets. Thus,

Value of each evaluation index on UCI, Amazon and Yelp datasets.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">Methods</td><td colspan="4">XGBoost</td><td colspan="4">Random forest</td></tr><tr><td> $P^a$ </td><td> $R^a$ </td><td>F-1</td><td>AUC</td><td>P</td><td>R</td><td>F-1</td><td>AUC</td></tr><tr><td rowspan="4">Haberman</td><td>None</td><td>0.624</td><td>0.638</td><td>0.695</td><td>0.928</td><td>0.792</td><td>0.807</td><td>0.763</td><td>0.796</td></tr><tr><td>SMOTE</td><td>0.667</td><td>0.967</td><td>0.944</td><td>0.941</td><td>0.822</td><td>0.826</td><td>0.793</td><td>0.802</td></tr><tr><td>M-SMOTE</td><td>0.811</td><td>0.992</td><td>0.965</td><td>0.961</td><td>0.878</td><td>0.877</td><td>0.881</td><td>0.831</td></tr><tr><td>None</td><td>0.701</td><td>0.803</td><td>0.752</td><td>0.785</td><td>0.613</td><td>0.643</td><td>0.705</td><td>0.818</td></tr><tr><td rowspan="3">Breast cancer</td><td>SMOTE</td><td>0.867</td><td>0.804</td><td>0.791</td><td>0.822</td><td>0.674</td><td>0.688</td><td>0.725</td><td>0.868</td></tr><tr><td>M-SMOTE</td><td>0.899</td><td>0.889</td><td>0.876</td><td>0.872</td><td>0.723</td><td>0.739</td><td>0.792</td><td>0.932</td></tr><tr><td>None</td><td>0.554</td><td>0.588</td><td>0.605</td><td>0.689</td><td>0.501</td><td>0.511</td><td>0.603</td><td>0.637</td></tr><tr><td rowspan="3">Telecom Churn</td><td>SMOTE</td><td>0.662</td><td>0.677</td><td>0.694</td><td>0.722</td><td>0.563</td><td>0.578</td><td>0.624</td><td>0.642</td></tr><tr><td>M-SMOTE</td><td>0.794</td><td>0.810</td><td>0.812</td><td>0.822</td><td>0.713</td><td>0.722</td><td>0.733</td><td>0.748</td></tr><tr><td>None</td><td>0.954</td><td>0.338</td><td>0.315</td><td>0.958</td><td>0.902</td><td>0.432</td><td>0.395</td><td>0.931</td></tr><tr><td rowspan="3">Abalone</td><td>SMOTE</td><td>0.917</td><td>0.927</td><td>0.864</td><td>0.911</td><td>0.922</td><td>0.928</td><td>0.873</td><td>0.901</td></tr><tr><td>M-SMOTE</td><td>0.991</td><td>0.982</td><td>0.995</td><td>0.992</td><td>0.962</td><td>0.971</td><td>0.963</td><td>0.944</td></tr><tr><td>None</td><td>0.604</td><td>0.648</td><td>0.615</td><td>0.668</td><td>0.534</td><td>0.565</td><td>0.645</td><td>0.602</td></tr><tr><td rowspan="3">Amazon</td><td>SMOTE</td><td>0.657</td><td>0.687</td><td>0.664</td><td>0.701</td><td>0.598</td><td>0.613</td><td>0.684</td><td>0.665</td></tr><tr><td>M-SMOTE</td><td>0.803</td><td>0.842</td><td>0.885</td><td>0.891</td><td>0.671</td><td>0.744</td><td>0.754</td><td>0.769</td></tr><tr><td>None</td><td>0.732</td><td>0.707</td><td>0.721</td><td>0.796</td><td>0.611</td><td>0.572</td><td>0.599</td><td>0.644</td></tr><tr><td rowspan="2">Yelp</td><td>SMOTE</td><td>0.742</td><td>0.716</td><td>0.733</td><td>0.802</td><td>0.623</td><td>0.593</td><td>0.622</td><td>0.664</td></tr><tr><td>M-SMOTE</td><td>0.772</td><td>0.747</td><td>0.781</td><td>0.838</td><td>0.655</td><td>0.670</td><td>0.690</td><td>0.712</td></tr></table>

a. P = precision; R = recall

## Table 7

## Table 5

Table 9  
Performance comparison of ML classifiers with and without data pre-processing challenges.

<table><tr><td></td><td colspan="4">Without pre-processing</td><td colspan="4">After solving all pre-processing challenges including data imbalance by M-SMOTE algorithm</td></tr><tr><td>Algorithms</td><td>P</td><td>R</td><td>F-1</td><td>AUC</td><td>P</td><td>R</td><td>F-1</td><td>AUC</td></tr><tr><td>XGBoost</td><td>0.732</td><td>0.707</td><td>0.721</td><td>0.796</td><td>0.772</td><td>0.747</td><td>0.781</td><td>0.838</td></tr><tr><td>Long short-term memory (LSTM)</td><td>0.710</td><td>0.698</td><td>0.702</td><td>0.765</td><td>0.740</td><td>0.748</td><td>0.743</td><td>0.809</td></tr><tr><td>Light Gradient Boosting Method (GBM)</td><td>0.698</td><td>0.687</td><td>0.666</td><td>0.743</td><td>0.723</td><td>0.710</td><td>0.766</td><td>0.797</td></tr><tr><td>Artificial Neural Network (ANN)</td><td>0.677</td><td>0.645</td><td>0.688</td><td>0.736</td><td>0.695</td><td>0.703</td><td>0.754</td><td>0.788</td></tr><tr><td>Recurrent Neural Network (RNN)</td><td>0.644</td><td>0.637</td><td>0.654</td><td>0.731</td><td>0.667</td><td>0.707</td><td>0.733</td><td>0.780</td></tr><tr><td>SVM (Radial basis function)</td><td>0.601</td><td>0.572</td><td>0.590</td><td>0.633</td><td>0.678</td><td>0.699</td><td>0.727</td><td>0.793</td></tr><tr><td>Logistic Regression</td><td>0.554</td><td>0.713</td><td>0.642</td><td>0.727</td><td>0.722</td><td>0.701</td><td>0.723</td><td>0.775</td></tr><tr><td>k-NN (k = 20)</td><td>0.546</td><td>0.704</td><td>0.624</td><td>0.704</td><td>0.642</td><td>0.714</td><td>0.721</td><td>0.754</td></tr><tr><td>Naïve Bayes</td><td>0.633</td><td>0.587</td><td>0.609</td><td>0.664</td><td>0.682</td><td>0.607</td><td>0.719</td><td>0.732</td></tr><tr><td>Random Forest</td><td>0.611</td><td>0.572</td><td>0.599</td><td>0.644</td><td>0.655</td><td>0.670</td><td>0.690</td><td>0.712</td></tr></table>

Table 6  
Performance comparison of top three ML classifiers with and without solving class imbalance problem.

<table><tr><td></td><td colspan="4">Without solving class imbalance problem</td><td colspan="4">After solving all pre-processing challenges including data imbalance by M-SMOTE algorithm</td></tr><tr><td>Algorithms</td><td>P</td><td>R</td><td>F-1</td><td>AUC</td><td>P</td><td>R</td><td>F-1</td><td>AUC</td></tr><tr><td>XGBoost</td><td>0.741</td><td>0.725</td><td>0.741</td><td>0.810</td><td>0.772</td><td>0.747</td><td>0.781</td><td>0.838</td></tr><tr><td>LSTM</td><td>0.723</td><td>0.698</td><td>0.702</td><td>0.765</td><td>0.740</td><td>0.748</td><td>0.743</td><td>0.809</td></tr><tr><td>Light GBM</td><td>0.708</td><td>0.707</td><td>0.683</td><td>0.761</td><td>0.723</td><td>0.710</td><td>0.766</td><td>0.797</td></tr></table>

Final model results.

<table><tr><td></td><td colspan="4">After solving all pre-processing challenges (including data imbalance)</td><td colspan="4">After applying majority vote rule Y = mode {0, 1, 1} = 1</td></tr><tr><td>Algorithms</td><td>P</td><td>R</td><td>F-1</td><td>AUC</td><td>P</td><td>R</td><td>F-1</td><td>AUC</td></tr><tr><td>XGBoost</td><td>0.772</td><td>0.747</td><td>0.781</td><td>0.838</td><td></td><td></td><td></td><td></td></tr><tr><td>LSTM</td><td>0.720</td><td>0.738</td><td>0.733</td><td>0.809</td><td>0.794</td><td>0.835</td><td>0.853</td><td>0.874</td></tr><tr><td>Light GBM</td><td>0.723</td><td>0.710</td><td>0.786</td><td>0.797</td><td></td><td></td><td></td><td></td></tr></table>

Table 8  
Performance of ML models with review-centric vs. reviewer-centric features.

<table><tr><td rowspan="2">Algorithms</td><td colspan="4">Reviewer-centric Features</td><td colspan="4">Review-centric Features</td></tr><tr><td>Precision</td><td>Recall</td><td>F-1</td><td>AUC</td><td>Precision</td><td>Recall</td><td>F-1</td><td>AUC</td></tr><tr><td>XGBoost</td><td>0.704</td><td>0.721</td><td>0.741</td><td>0.806</td><td>0.675</td><td>0.647</td><td>0.702</td><td>0.733</td></tr><tr><td>LSTM</td><td>0.730</td><td>0.702</td><td>0.762</td><td>0.782</td><td>0.623</td><td>0.658</td><td>0.673</td><td>0.708</td></tr><tr><td>Light GBM</td><td>0.705</td><td>0.694</td><td>0.766</td><td>0.765</td><td>0.626</td><td>0.660</td><td>0.657</td><td>0.681</td></tr><tr><td>Random Forest</td><td>0.682</td><td>0.667</td><td>0.698</td><td>0.743</td><td>0.593</td><td>0.623</td><td>0.650</td><td>0.664</td></tr><tr><td>Logistic Regression</td><td>0.652</td><td>0.643</td><td>0.692</td><td>0.720</td><td>0.564</td><td>0.677</td><td>0.637</td><td>0.643</td></tr></table>

H1 is supported across all statistical measures. (See Table 9.)

To further validate our next hypothesis (H2), Table 8 results show the performance of top five ML models developed using all features (review- and reviewer-centric) and review-centric features, and Table 10 shows the t-test results comparing the accuracy of the top five ML classifiers when combining review- and reviewer-centric features over reviewer-centric features alone. Both tables demonstrate that incorpo rating both review- and reviewer's behavior features improved all ML classifiers performance in terms of precision, recall, AUC score and F-1 scores compared with using review-centric features alone in the same

Table 10

Performance improvement after incorporating reviewer-centric features (mean difference).

<table><tr><td>Algorithms</td><td>Precision (%)</td><td>Recall (%)</td><td>F-1 (%)</td><td>AUC (%)</td></tr><tr><td>XGBoost</td><td>+6.8***</td><td>+2,6***</td><td>+4%***</td><td>+3.0***</td></tr><tr><td>LSTM</td><td>+0.4</td><td>+3.6</td><td>-2.9</td><td>+2.2</td></tr><tr><td>Light GBM</td><td>1.8</td><td>+1.6</td><td>+2.0</td><td>+2.9</td></tr><tr><td>Logistic Regression</td><td>+7.0</td><td>+5.8</td><td>+3.1</td><td>+5.5</td></tr></table>

Denote the significance at 0.001 level.

Performance of ML models with all features vs. reviewer-centric features.

<table><tr><td rowspan="2">Algorithms</td><td colspan="4">Reviewer-centric + Review-centric Features (%)</td><td colspan="4">Reviewer-centric Features (%)</td></tr><tr><td>Precision</td><td>Recall</td><td>F-1</td><td>AUC</td><td>Precision</td><td>Recall</td><td>F-1</td><td>AUC</td></tr><tr><td>XGBoost</td><td>0.772</td><td>0.747</td><td>0.781</td><td>0.836</td><td>0.704</td><td>0.721</td><td>0.741</td><td>0.806</td></tr><tr><td>LSTM</td><td>0.730</td><td>0.738</td><td>0.733</td><td>0.804</td><td>0.726</td><td>0.702</td><td>0.762</td><td>0.782</td></tr><tr><td>Light GBM</td><td>0.723</td><td>0.710</td><td>0.786</td><td>0.794</td><td>0.705</td><td>0.694</td><td>0.766</td><td>0.765</td></tr><tr><td>Random Forest</td><td>0.655</td><td>0.670</td><td>0.690</td><td>0.712</td><td>0.682</td><td>0.667</td><td>0.698</td><td>0.743</td></tr><tr><td>Logistic Regression</td><td>0.722</td><td>0.701</td><td>0.723</td><td>0.775</td><td>0.652</td><td>0.643</td><td>0.692</td><td>0.720</td></tr></table>

logistic regression model. We can clearly see that the performance of the same logistic regression model is significantly increased across all four measures after incorporating review-centric features with reviewercentric features in developing the fraudulent review detection models. Therefore, H2 is supported across all statistical measures.

In summary, the analysis leads to the following conclusions: We can verify that positive reviews (5-star ratings) tend to be lengthier and more detailed, and exhibit a high rate of misspelled words and incorrectly used apostrophes. Negative reviews (1-star ratings) are typically shorter and often do not include any punctuation. Furthermore, fraudulent re viewers use more content and more verbs, adjectives, and filler words than real reviewers do, whereas real reviews contain more nouns and pronouns (Fig. 5). We have also identified positive reviews generally contain longer and more error-filled prose than negative reviews (Fig. 6).

Fig. 7 shows that “food” and “service” are among the top words across both positive and negative reviews, which indicates that these are the two most important dimensions that reviewers consider when they visit and evaluate a restaurant.

We can also see that reviewers tend to most frequently express positive views, as the average of positive words triple that of negative words across all reviews. Initially, we assumed that one- and five-sta ratings would have the longest reviews because when a reviewer is very disappointed or very satisfied with a particular restaurant, they might write a relatively long review to express their strong emotions. However, 5-star reviews are in fact lengthier than 1-star reviews, although the latter do tend to be longer that 2- and 3-star reviews. Otherwise, as the star rating decreases, so do the average number of words in the review. Our assumption that directly using skewed features in ML models would reduce their predictive accuracy was verified by our analysis, as was our hypotheses that reviewer-centric features of users are more important that review-centric features for detecting fraudulent reviewer's behavior and that combining reviewer-centric with review centric features improves the accuracy of all ML detection models in comparison with using review-centric features alone. Finally, our anal ysis verifies that if we want to introduce new features that are not correlated with each other, then the adjusted R-squared will increase only if the introduced feature improves the model.

## 6. Methodology validation and performance comparison with prior studies

We can now validate our methodology on other three datasets from Yelp and Amazon website. We performed and repeated the same set of feature engineering and data pre-processing steps on two different Amazon datasets [12,23] as well as the Yelp Open Dataset [57]. Table 11 shows the performance of the top four ML models with and without feature engineering on the Amazon dataset, all of which are largely consistent with those based on our original Yelp review dataset. After solving all data pre-processing and feature engineering tasks and applying our proposed M-SMOTE model, all of the classifiers perform better than the raw data on all four datasets. We can clearly see that the performance of the same random forest model is significantly better and increased across all four measures after solving all data pre-processing challenges and feature engineering tasks before feeding it into our proposed model. Therefore, these predictive results confirm the findings from the original Yelp restaurant review results.

![](/api/attachments/V9J9K6X8/fulltext/images/b663ef252bad61880b4d51180183d6f3f04b185f80e11df58c2afae527a372dc.jpg)  
Fig. 5. Part-of-Speech Ratios.

We also compare the results of our proposed model with several other notable previous studies conducted on the Amazon and Yelp datasets. Jindal and Liu [23] used the Amazon dataset to train their predictive models and showed an AUC score of 78%. They did not used any feature engineering process on the dataset and used the raw data directly to develop the machine learning models. Feng et al. [16] derived probabilistic context- free grammars from Yelp and TripAdvisor datasets to develop the fraudulent review detection models; however, both datasets were quite small (around 800–900 reviews). ML classifier's performance are strongly affected by data-set size and the noise con tained in the training set, which is likely why they achieved only 64.3% accuracy on Yelp dataset. Zhang et al. [60] used verbal and non-verbal features on an Amazon dataset but did not improve ML classifier accu racy in any way or perform any data pre-processing and feature engi neering tasks on the dataset before feeding it into machine learning. The only feature-engineering task that Kumar et al. [28] worked on was the “skewed distribution” of features before developing the supervised ML models on the Yelp dataset, and they obtained an 81.7% AUC score in the logistic regression model. Ravana and Akoglu [51] and Kumar et al. [29] used the Yelp dataset and combined metadata and text features to develop the unsupervised ML models. As previously described, Rayana and Akoglu [51] performed traditional text pre-processing solutions before developing their unsupervised ML models and obtained a 68.28% AUC score. Kumar et al. [29] incorporated two feature engineering tasks, namely “skewed distributions of features” and “outlier detection and removal" and used a mixture model for detecting the fraudulent reviews, ultimately obtaining a 70% AUC score. In comparison with the above, our proposed model achieves a greater than 80% AUC score on all four datasets, and on the main Yelp dataset we achieve particularly high scores across all four measures (P: 79.4%, R: 83.5%, F-1: 85.3%. and AUC: 87.4%). Clearly, our proposed fraudulent review prediction model outperforms the above-mentioned methods.

## 7. Discussions, conclusion, limitations and future work

In this paper, we have proposed an M-SMOTE-based ML framework to develop a fraudulent review detection model that can assist marketing managers and consumers to detect the opinion spammers and their suspicious behavior in the decision-making process. Although several other models to detect fraudulent reviewers have been developed, none of these fully exploits feature engineering, data pre-processing, or the underlying distributional characteristics of reviewers' behavior. Our model combines various heterogeneous distributions, pre-processing tasks, and feature engineering on a balanced dataset in order to holis tically explain different characteristics of fraudulent reviewers' behavior. Our analysis of the correlation between ratings and the results of fraudulent reviewers' sentiments revealed that the most positive re views tend to be longer and more detailed and have a higher rate of misspelled words and incorrectly used apostrophes, whereas the most negative reviews are typically shorter in length and often do not include any punctuation. We have also identified that positive reviews contain longer and more error-filled prose than negative reviews. Moreover, whereas fraudulent reviews contain more content, verbs, adjectives, and filler words than real reviews, the latter contain more nouns and ad jectives. During several experiments, we have: (1) derived univariate distributions of features that are commonly used to characterize re: viewer's behavior; (2) performed feature engineering to transform the features and delete unnecessary entries from the dataset; (3) developed an M-SMOTE algorithm to solve the class imbalance problem; and (4) incorporated univariate distributions into a machine-learning model to detect fraudulent reviewers and their behavior. We have used both synthetic and real-world Yelp restaurant review data to compare our methodology with the traditional ML algorithms and other state-of-theart supervised methods for detecting fraudulent reviewers and demon strated that our method outperforms other approaches.

![](/api/attachments/V9J9K6X8/fulltext/images/b3d911ffe727e0febd7195f16f7216fe04c9fec4dbca9edfa7f0caaa720df733.jpg)  
Fig. 6. Star rating vs character length.

![](/api/attachments/V9J9K6X8/fulltext/images/a8606b643aabf541879eb82750168ea9e76037bc5a49619cf4f9eba1e6dde3d2.jpg)  
(a)

![](/api/attachments/V9J9K6X8/fulltext/images/07f6bec0818ab243fd855e07e6f397ab29920efdd6e7d2fd3e2b3f1104c4a1e9.jpg)  
(b)

Fig. 7. Predominant categories in positive and negative reviews.  
Table 11  
Comparison of ML classifiers' performance on the validation dataset.

<table><tr><td></td><td colspan="4">After solving all pre-processing challenges (including data imbalance)</td><td colspan="4">After applying majority vote rule Y = mode {0, 1, 1} = 1</td></tr><tr><td>Model</td><td>Precision</td><td>Recall</td><td>F-1</td><td>AUC</td><td>Precision</td><td>Recall</td><td>F-1</td><td>AUC</td></tr><tr><td>XGBoost</td><td>0.803(+3.3%)</td><td>0.842(+4.6%)</td><td>0.885(+5.2%)</td><td>0.891(+7.8%)</td><td></td><td></td><td></td><td></td></tr><tr><td>LSTM</td><td>0.692(+9.3%)</td><td>0.775(+6.8%)</td><td>0.794(+6.2%)</td><td>0.821(+11.3%)</td><td>0.812</td><td>0.869</td><td>0.902</td><td>0.937</td></tr><tr><td>ANN</td><td>0.683 + (+4.7%)</td><td>0.751(+5.3%)</td><td>0.782(+6.2%)</td><td>0.776(+6.6%)</td><td></td><td></td><td></td><td></td></tr><tr><td>Random Forest</td><td>0.671 + (+11.3%)</td><td>0.744(+9.1%)</td><td>0.754(+7.2%)</td><td>0.769(+11.8%)</td><td></td><td></td><td></td><td></td></tr></table>

The present findings confirm that combining reviewer-centric fea tures with review-centric features can significantly improve the perfor mance of fraudulent review detection models. Importantly, our results provide evidence that reviewer-centric features can be more effective than review-centric features for detecting the opinion spammers, as reviewer-centric features are complementary to reviewers' behaviors, which deserve more attention when developing predictive models. We believe that the strong effect of reviewer-centric features is due to the likelihood that it is more difficult and costly to manipulate reviewers behavior, which makes it a more robust and reliable cue to detect opinion spamming. Our research model has several additional implica tions for online e-commerce. As social media platforms have become major conduits of fraudulent information, automated social media ac counts are increasingly likely to increase the spread of fraudulent news and reviews [33]. Our proposed solution handles biases that make social media websites vulnerable to misinformation by offering an M-SMOTE fraudulent detector tool. Our proposed novel supervised ML method can be extended to categorize the fraudulent accounts of social bots, and ecommerce companies can use it to redesign their existing predictive model and combat the automated spread of fraudulent news content. Our findings suggest that online e-commerce platforms should encourage social interactions between customers and reviewers in order to supply rich evidence of reviewers' behavior to enhance the detection of opinion spamming.

This research has some limitations that might restrict the general ization of the findings and provide potential opportunities for further research. First, the proposed model has only been tested on three different datasets from two platforms. Although Yelp and Amazon are very popular online review platforms and contain rich collections of the social activities of individual reviewers, different results might have been obtained if the model had been tested on other platforms such as Walmart, Alibaba, eBay, or TripAdvisor. The findings might not be directly applicable on other datasets because some novel features included in our predictive models may not be available. To overcome these limitations, further research should certainly examine the role of additional features of fraudulent reviewers' behavior, and the frame work should be tested on multiple datasets collected from additional online platforms. ML models can produce false signals when fraudulent reviewers dynamically change their behavior; thus, if we apply the same features on new datasets, there is a high risk of the model losing credi bility. However, we suggest that the features developed in this study could be generalized to other online e-commerce platforms, which is worthy of further investigation and future research. Moreover, we plan to more deeply analyze review-centric information in order to extract additional novel features that could contribute to improve the accuracy and interpretability of machine learning models.

## References

[1] A. Abbasi, F.M. Zahedi, D. Zeng, Y. Chen, H. Chen, J.F. Nunamaker, Enhancing predictive analytics for anti-phishing by exploiting website genre information, J. Manag. Inf. Syst. 31 (4) (2015) 109–157.

[2] A. Abbasi, Z. Zhang, D. Zimbra, H. Chen, J.F. Nunamaker, Detecting fraudulent websites: the contribution of statistical learning theory, MIS Q. 34 (3) (2010)

[3] L. Akoglu, R. Chandy, C. Faloutsos, Opinion fraud detection in online reviews by network effects, Proceedings of the Int. AAAI Conf, on Weblogs and Social Media 7 (2013) 2–11.

[4] O. Arazy, C. Woo, Enhancing information retrieval through statistical natural language processing: a study of collocation indexing, MIS Q. 31 (3) (2007) 525–546.

[5] L. Ball, J. Elworthy, Fraudulent or real? The computational detection of online deceptive text, J. Marketing Anal. 2 (2014) 187–201.

[6] S. Banerjee, A.Y. Chua, A theoretical framework to identify authentic online reviews, Online Inf, Rev, 38 (5) (2014) 634–649.

[7] S. Bhutada, V.V.S.S.S. Balaram, C.A. Sree, Deep learning framework to detect the false analysis of a product given by robots and malicious users. International Journal of Innovative Technology and Exploring Engineering 8 (6) (2019) 689-692.

[8] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: Synthetic minority over-sampling technique, J. Artif. Intell. Res. 16 (2002) 321–357.

[9] L.Y. Chen, Alibaba lawsuit throws the spotlight on fraudulent reviews, Bloomberg News (December 19 2016). Available from, https://www.bloomberg.com/news/a rticles/2016-12-19/alibaba-lawsuit-throws-spotlight-on-brushers-gaming-ranking s.

[10] C. Conner, Amazon sues 1,114 fraudulent reviewers on Fiverr, Forbes (October 8, 2015). Available from, https://www.forbes.com/sites/cherylsnappconner/2015/ 10/18/amazon-sues-1114-fake-reviewers-on-fiverr-com/.

[11] N.N. Dalvi, R. Kumar, B. Pang, Para 'normal' activity: on the distribution of average ratings, in: Proceeding of the Seventh International AAAI Conference on Weblogs

[12] Deception-Detection-on-Amazon-reviews-dataset, Available from, https://github. com/aayush210789/Deception-Detection-on-Amazon-reviews-dataset.

[13] S. Deng, Deceptive reviews detection of industrial product, Int. J. Serv. Operations and Inform, 8 (2) (2016) 122.

[14] L. Dong, S. Ji, C. Zhang, Q. Zhang, D.W. Chiu, L. Qiu, D. Li, An unsupervised topicsentiment joint probabilistic model for detecting deceptive reviews, Expert Syst. Appl. 114 (2018) 210–223.

[15] Federal Trade Commission, FTC brings first case challenging fraudulent paid reviews on an independent retail website, February 26, 2019. Available at, https ://www.ftc.gov/news-events/press-releases/2019/02/ftc-brings-first-case-ch allenging-fraudulent-paid-reviews-independent.

[16] S. Feng, R. Banerjee, Y. Choi, Syntactic stylometry for deception detection, in: Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics, Association for Computational Linguistics, Stroudsburg, 2012, pp. 171–175.

[17] P.B. Goes, M. Lin, C.M. Au Yeung, Popularity effect in user-generated content: Evidence from online product reviews, Inf. Syst. Res. 25 (2) (2014) 222–238.

[18] M. Hazim, N.B. Anuar, M.F. Ab Razak, N.A. Abdullah, Detecting opinion spams through supervised boosting approach, PLoS One 13 (6) (2018), e0198884.

[19] B. Heredia, T.M. Khoshgoftaar. J.D. Prusa, M. Crawford. Improving detection of untrustworthy online reviews using ensemble learners combined with feature selection, Soc, Netw, Anal, Min, 7 (37) (2017) 1–18.

[20] S.M. Ho. J.T. Hancock, C. Booth. X. Liu, Computer-mediated deception: Strategies revealed by language-action cues in spontaneous communication, J. Manag, Inf. Syst. 33 (2) (2016) 393–420.

[21] O. Ivanova, M. Scholz, How can online marketplaces reduce rating manipulation? A new approach on dynamic aggregation of online ratings, Decis. Support. Syst. 104 (4) (2017) 64–78.

[22] D. Jalther, G. Priya, Reputation reporting system using text based classification, Int. J. Innov. Technol. and Expl. Eng. 8 (8) (2019) 1555–1558.

[23] N. Jindal, B. Liu, Opinion spam and analysis, in: Proceedings of the Internationa Conference on Web Search and Data Mining, ACM, New York, NY, 2008, pp. 219–230.

[24] M.D. Kamalesh, H.K. Diwedi, Extracting product features from consumer reviews and its applications. Int. J. Appl, Eng. Res. 10 (2) (2015) 2345–2350

[25] L. Khansa, X. Ma, D. Liginlal, and. Kim, S.S., Understanding members’ active participation in online question-and-answer communities: a theory and empirical analysis, J. Manag. Inf. Syst. 32 (2) (2015) 162–203.

[26] F. Khurshid, Y. Zhu, Z. Xu, M. Ahmad, M. Ahmad, Enactment of ensemble learning for review spam detection on selected features, Int. J. Comp. Intell. Systems 12 (1) (2019) 387–394.

[27] A. Kumar, R. Shankar, A.K. Choudhary, L.S. Thakur, A big data MapReduce framework for fault diagnosis in cloud-based manufacturing, Int. J. Prod. Res. 54 (2016) 7060–7073.

[28] N. Kumar, D. Venugopal, L. Qiu, S. Kumar, Detecting review manipulation on online platforms with hierarchical supervised learning, J. Manag. Inf. Syst. 35 (1) (2018) 350–380.

[29] N. Kumar, D. Venugopal, L. Qiu, S. Kumar, Detecting anomalous online reviewers: an unsupervised approach using mixture models, J. Manag. Inf. Syst. 36 (4) (2019) 1313–1346.

[30] T. Lappas, G. Sabnis, G. Valkanas, The impact of fake reviews on online visibility: A vulnerability assessment of the hotel industry, Inf. Syst. Res. 27 (4) (2016) 940–961.

[31] M.T. Lash, K. Zhao, Early predictions of movie success: The who, what, and when of profitability, J. Manag. Inf. Syst. 33 (3) (2016) 874–903.

[32] R.Y.K. Lau, S.Y. Liao, R.C.W. Kwok, K. Xu, Y. Xia, Y. Li, Text mining and probabilistic language modeling for online review spam detection, Transac. on Manag. Inform. Systems 2 (4) (2011) 1–30.

[33] D.M. Lazer, M.A. Baum, Y. Benkler, A.J. Berinsky, K.M. Greenhill, F. Menczer, M. Schudson, The science of fraudulent news, Science 359 (6380) (2018 1094–1096.

[34] F. Li, M. Huang, Y. Yang, X. Zhu, Learning to identify review spam, Proceedings Int. Joint Conf. on Artificial Intell. 22 (3) (2011) 2488–2493.

[35] H. Li, B. Liu, A. Mukherjee, J. Shao, Spotting fraudulent reviews using positive unlabeled learning, Computations y Sistemas 18 (3) (2014) 467–475.

[36] L. Li, B. Qin, W. Ren, T. Liu, Document representation and feature combination for deceptive spam review detection. Neurocomputing 254 (2017) 33–41.

[37] X. Liang, A. Jiang, T. Li, Y. Xue, G. Wang, LR-SMOTE—An improved unbalanced dataset oversampling based on K-means and SVM. Knowl.-Based Syst. 196 (2020) 105845.

[38] E. Lim, V.A. Nguven, N. Jindal, B. Liu, H. Lauw. Detecting product review spammers using rating behavior, in: Proceedings of the 19th ACM internationa conference on Information and knowledge management, ACM, Lyon, 2010, pp. 939–948.

[39] Y. Lin, T. Zhu, H. Wu, J. Zhang, X. Wang, A. Zhou, Towards online anti-opinion spam: spotting fraudulent reviews from the review sequence, in: Proceedings of the 2019 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining, Association for Computing Machinery, New York, 2014, pp. 261–264.

[40] Y. Liu, B. Pang, A unified framework for detecting author spamicity by modeling review deviation, Expert Syst. Appl. 112 (2018) 148–155.

[41] Y. Liu, B. Pang, X. Wang, Opinion spam detection by incorporating multimodal embedded representation into a probabilistic review graph, Neurocomputing 366 (2019) 276–283.

[42] M. Luca, G. Zervas, Fake it till you make it: reputation, competition, and yelp review fraud, Manag. Sci. 62 (12) (2016) 3412–3427.

[43] S. Ludwig, T. Van Laer, K. De Ruyter, M. Friedman, Untangling a web of lies: Exploring automated detection of deception in computer-mediated communication, J. Manag, Inf, Syst, 33 (2) (2016) 511–541

[44] A. Mukherjee, A. Kumar, B. Liu, J. Wang, M. Hsu, M. Castellanos, R. Ghosh, Spotting opinion spammers using behavioral footprints, in: Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining,

[45] A. Mukherjee, B. Liu, N. Glance, Spotting fake reviewer groups in consumer reviews, in: Proceedings of the 21<sup>st</sup> International World Wide Web Conference (IW3C), ACM, Lyon, 2012, pp. 191–200.

[46] R. Murphy, Local consumer review survey, Available from: https://www.brigh tlocal.com/research/local-consumer-review-survey/. December 2019.

[47] M. Ott, Y. Choi, C. Cardie, J.T. Hancock, Finding deceptive opinion spam by any stretch of the imagination, in: Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies, Association for Computational Linguistics, Stroudsburg, 2011, pp. 309–319.

[48] J.G. Proudfoot, J.L. Jenkins, J.K. Burgoon, J.F. Nunamaker Jr., More than meets the eve: how oculometric behaviors evolve over the course of automated deceptior detection interactions, J. Manag, Inf. Syst. 33 (2) (2016) 332–360.

[49] S. Rajamohana, K. Umamaheswari, Hybrid approach of improved binary particle swarm optimization and shuffled frog leaping for feature selection, Comput. Electr Eng. 67 (2018) 497–508.

[50] S. Rajamohana, K. Umamaheswari, B. Abirami, Performance analysis of iBPSO and BFPA based feature selection techniques for improving classification accuracy in review spam detection, Appl. Math.& Inform. Sci. 11 (4) (2017) 1149–1153.

[51] S. Rayana, L. Akoglu, Collective opinion spam detection: bridging review networks and metadata, Proceedings of the ACM SIGKDD Int. Conf. on Know. Discov. Data Mining 21 (2015) 985–994.

[52] Y. Ren, D. Ji, Neural networks for deceptive opinion spam detection: an empirical study, Inf. Sci. 385 (2017) 213–224.

[53] M. Siering, J.A. Koch, A.V. Deokar, Detecting fraudulent behavior on crowd platforms: The role of linguistic and content-based cues in static and dynamic contexts, J. Manag. Inf. Syst. 33 (2) (2016) 421–455.

[54] UCI machine learning repository, Available from, https://archive.ics.uci. edu/ml/datasets.php

[55] T. Vanta, M. Aono, Fraudulent review detection focusing on emotional expressions and extreme rating, in: Proceedings of the 25th Annual Conference of the Language Processing Society (NLP2019), The Association for Natural Language Processing, Nagoya, Japan, 2019, pp. 1–30.

[56] Y. Xu, Y. Yang, J. Han, E. Wang, J. Ming, H. Xiong, Slanderous user detection with modified recurrent neural networks in recommender system, Inf. Sci. 505 (2019) 265-281.

[58] C. Yu, Y. Zuo, B. Feng, B. Chen, An individual-group-merchant relation model for identifying fraudulent online reviews: an empirical study on a Chinese e-commerce platform, Inf. Technol. Manag. 20 (2019) 123–138.

[57] Yelp open dataset, Available from, https://www.yelp.com/dataset/.

[59] S. Yuan, X. Wu, Y. Xiang, Task-specific word identification from short texts using a convolutional neural network, Intell. Data Anal. 22 (3) (2018) 533–550.

[60] D.S. Zhang, L.N. Zhou, J.L. Kehoe, I.Y. Kilic, What online reviewer behaviors really matter? Effects of verbal and nonverbal behaviors on detection of fraudulent online reviews, J. Manag. Inf. Syst. 33 (2) (2016) 456–481.

[61] L. Zhang, Z. Wu, J. Cao, Detecting spammer groups from product reviews: a partially supervised learning model, IEEE Access 6 (2018) 2559–2568.

[62] W. Zhang, Y. Du, T. Yoshida, Q. Wang, DRI-RCNN: an approach to deceptive review identification using recurrent convolutional neural network, Inf. Process. Manag. 54 (4) (2018) 576–592.

Ajay Kumar is an Assistant Professor at the AIM Research Center on Artificial Intellegence in Value Creation, EMLYON Business School in France. His research and teaching interests are in data and text mining, decision support systems, business intelligence and enterprise modeling. He has been Postdoctoral Fellow at Massachusetts Institute of Technology and Harvard Business School. He has published several research papers in reputed journals, including Decision Support Systems, Journal of Business Research, International Journal of

Operations & Production Management, IEEE Transactions on Engineering Management, Inter national Journal of Production Economics, Industrial Marketing Management, Telematics & Informatics, Technological Forecasting & Social Change, Annals of Operation Research, etc

Ram D. Gopal is the Information Systems Society's Distinguished Fellow and a Professor of Information Systems and Management at the Warwick Business School, UK. He previously served as the Head of the Department of Operations and Information Management in the School of Business, University of Connecticut. USA from 2008–2018. His research has appeared in Management Science, Management Information Systems Quarterly, Operations Research, INFORMS Journal on Computing, Information Systems Research, Journal of Man agement Information Systems, and other journals and conference proceedings. He is currently a Senior Editor of ‘Information Systems Research’ journal and has held editorial positions at Decision Sciences, Journal of Database Management, Information Systems Frontiers, and Journal of Management Sciences. He served as the President of the Workshop on Information Technologies and Systems organization from 2016 to 2018.

Ravi Shankar is the “Amar S. Gupta Chair Professor of Decision Science” and Group Chair of Operations and Supply Chain Management in the Department of Management Studies, Indian Institute of Technology Delhi, India. His areas of interest are supply chain analytics, business analytics, operations research, big data analytics, fuzzy modelling, sustainable logistics, etc. He has published over 300 research papers in reputed journals, including Journal of Operations Management, European Journal of Operations Research, Decision Support Systems, Omega, Expert System with Applications, Applied Soft Computing, International Journal of Production Research, International Journal of Production Economics, IEEE Systems Man and Cybernetics Part C, Computers and Operations Research, etc.

Kim Hua Tan is a Professor in Operations and Innovation Management domain at Not tingham University Business School, UK. Prior to this, he was a researcher and teaching assistant at Centre for Strategy and Performance. University of Cambridge. Professor Tan spent many vears in industry. before joining academia in 1999. His current research in terests are lean management, operations strategy, decision making, and supply chain risk management. Professor Tan has published a book called 'Winning Decisions: Translating Business Strategy into Action Plans,' and numerous articles in academic journals such as Decision Sciences, International Journal of Operations and Production Management, Interna tional Journal of Production Economics, International Journal of Innovation Management, and others.
