---
otero_id: 15620
otero_key: "MKHKB84J"
title: "Detecting Anomalous Online Reviewers: An Unsupervised Approach Using Mixture Models"
authors: "Naveen Kumar; Deepak Venugopal; Liangfei Qiu; Subodha Kumar"
year: "2019"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1661089"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Detecting Anomalous Online Reviewers: An Unsupervised Approach Using Mixture Models

Naveen KumarNAVEEN KUMAR, Deepak VenugopalDEEPAK VENUGOPAL, Liangfei QiuLIANGFEI QIU & Subodha KumarSUBODHA KUMAR

To cite this article: Naveen KumarNAVEEN KUMAR, Deepak VenugopalDEEPAK VENUGOPAL, Liangfei QiuLIANGFEI QIU & Subodha KumarSUBODHA KUMAR (2019) Detecting Anomalous Online Reviewers: An Unsupervised Approach Using Mixture Models, Journal of Management Information Systems, 36:4, 1313-1346, DOI: 10.1080/07421222.2019.1661089

To link to this article: https://doi.org/10.1080/07421222.2019.1661089

![](/api/attachments/MKHKB84J/fulltext/images/e219a43168ede10b0b7eca8594362bc76919246d7229b2dc36c36d35447eedc3.jpg)

View supplementary material

![](/api/attachments/MKHKB84J/fulltext/images/bb6b214a635bd867cc1cd6420876af866f7b10362c7b15e02566fbd6c77e9209.jpg)

Published online: 09 Oct 2019.

![](/api/attachments/MKHKB84J/fulltext/images/2d6bfc39a2025fe5ec8cda45d35796cbc7d87be3bf9155ebfaafbb58bc700631.jpg)

Submit your article to this journal

![](/api/attachments/MKHKB84J/fulltext/images/3950f236c995fbc209afd24f5aaef732cea5ca2e9174fc5bbdb9a56f6cb593ec.jpg)

Article views: 20

![](/api/attachments/MKHKB84J/fulltext/images/87f968db67c7bf07e078cab408ac4026c6a1e6afeec37f72e55cf9b88313a352.jpg)

View related articles

![](/api/attachments/MKHKB84J/fulltext/images/8d4a25d48efa429287bd8dde73629c0c259b11f13351920b3d9ac1627ccd5d0a.jpg)

View Crossmark data

# Detecting Anomalous Online Reviewers: An Unsupervised Approach Using Mixture Models

NAVEEN KUMAR, DEEPAK VENUGOPAL, LIANGFEI QIU, AND SUBODHA KUMAR

NAVEEN KUMAR (nkchawla@uw.edu) is an assistant professor of Management Information Systems in the School of Business, University of Washington, Bothell. He received his Ph.D. from the University of Washington, Seattle. His research focuses on applying deep learning and other artificial intelligence techniques in social media and information systems. Before joining academia, he worked as a researcher in the high-tech industry, solving complex business problems in IT, Finance, and Manufacturing using advanced machine-learning techniques.

DEEPAK VENUGOPAL (dvngopal@memphis.edu) is an assistant professor in the Department of Computer Science at the University of Memphis. He received his Ph.D. in computer science from the University of Texas at Dallas. His research interests focus on probabilistic and statistical relational models. Dr. Venugopal’s work has been published in the proceedings of conferences, including those of the Association for the Advancement of Artificial Intelligence, Conference on Neural Information Processing, and others.

LIANGFEI QIU (liangfei.qiu@warrington.ufl.edu; corresponding author) is an associate professor in the Department of Information Systems and Operations Management at the Warrington College of Business, University of Florida. He received his Ph.D. in economics from the University of Texas at Austin. Dr. Qiu’s research focuses on economics of information systems, prediction markets, social media, and telecommunications policy. His work has been published in Decision Support Systems, Information Systems Research, Journal of Management Information Systems, MIS Quarterly, and other journals.

Subodha KUMAR (subodha@temple.edu) is the Paul Anderson Distinguished Professor of Supply Chain Management, Marketing, Information Systems, and Statistical Science, and the director of the Center for Data Analytics at the Fox School of Business, Temple University. He earned his Ph.D. from the University of Texas at Dallas. Dr. Kumar has published numerous papers in a variety of journals. He is the deputy editor and a department editor of Production and Operations

Management and has served as a senior editor of Decision Sciences and an associate editor of Information Systems Research.

ABSTRACT: Online reviews play a significant role in influencing decisions made by users in day-to-day life. The presence of reviewers who deliberately post fake reviews for financial or other gains, however, negatively impacts both users and businesses. Unfortunately, automatically detecting such reviewers is a challenging problem since fake reviews do not seem out-of-place next to genuine reviews. In this paper, we present a fully unsupervised approach to detect anomalous behavior in online reviewers. We propose a novel hierarchical approach for this task in which we (1) derive distributions for key features that define reviewer behavior, and (2) combine these distributions into a finite mixture model. Our approach is highly generalizable and it allows us to seamlessly combine both univariate and multivariate distributions into a unified anomaly detection system. Most importantly, it requires no explicit labeling (spam/not spam) of the data. Our newly developed approach outperforms prior state-of-the-art unsupervised anomaly detection approaches.

KEY WORDS AND PHRASES: online reviews, fake reviews, opinion spam, unsupervised learning, anomaly detection, mixture models, deception detection.

Falsehood diffused significantly farther, faster, deeper, and more broadly than the truth in all categories of information. — Vosoughi et al. [86]

## Introduction

The past few years have witnessed an unprecedented spread of misinformation in various forms. While traditional spam e-mails have long been a threat, the rise of fake online reviews and fake news on social media platforms highlights the vulnerabilities of individuals, institutions, and society to manipulation in the age of social media. Misinformation on social media platforms has drawn recent attention in political contexts. Social media sites such as Facebook and Twitter are reported to be major platforms used to spread fake news in the 2016 U.S. presidential election cycle [38]. Recent research has mainly focused on the dissemination of misinformation through social media [86]. However, in the first place, we must identify and detect misinformation and understand how common misinformation is on social media platforms.

By now, machine-learning techniques can detect spam e-mails quite accurately [14, 94]. However, can we say the same about inauthentic online reviews on social media platforms? Are we equally equipped to rule them out as fake, or are they harder to pinpoint? This problem is particularly important to address since a large percentage of modern consumers routinely use online reviews as an important factor in their decision-making process [56]. It has been reported that up to 90 percent of consumers read online reviews before making a purchase, and most of these consumers trust the authenticity of the comments [56, 73]. Additionally, businesses pay close attention to what consumers are writing about them online to maintain their brand reputation [6]. Thus, maintaining a fair, unbiased review system is extremely important for both users and businesses. Since online reviews have such a high degree of influence, however, fake reviewers seek financial gain or other incentives in exchange for online review manipulation. For instance, reviewers may be hired by businesses to write biased reviews either favoring a product or unfairly denouncing a competitor’s products [82]. In fact, there have been several known instances of review manipulation misleading consumers and resulting in lawsuits [71]. More specifically, to boost demand, restaurants sometimes invest in hiring freelance writers or some social media optimization companies to post fake reviews on Yelp. The cost of doing this may be as low as \$2 per five-star review on platforms like Yelp and TripAdvisor.<sup>2</sup> Therefore, to ensure the integrity and trustworthiness of online reviews, it is essential to develop techniques that can automatically identify and flag such fake reviewers who exhibit anomalous behavior in online social media.

Automatic detection of fake reviewers, also referred to as opinion spammers [35], is a challenging problem. In some previous studies, even the accuracy of humans distinguishing fake reviews from real reviews was shown to be just slightly better than random chance [63]. In comparison, detecting anomalous behavior in e-mail messages is often not as challenging. For example, an unsolicited e-mail message received from an unknown user with the word “Viagra” or its variants is almost always spam [13] and may not be relevant to the vast majority of users who receive the e-mail. Conversely, fake reviews about a product are more likely to be trusted in an online forum even if they are from anonymous users [53].

However, since the ulterior motive of a fake reviewer is typically different from a regular user (e.g., financial gains, denouncing competitors, etc.), behaviors of fake reviewers are likely to show up as statistical anomalies when compared to the observed behaviors of regular users [21]. For example, reviewers who are being paid may write reviews very often while regular users may write reviews more sporadically. Some other types of anomalous behavior are more complex and require analysis of more than one variable simultaneously. For instance, a fake reviewer might specifically target restaurants that are popular among several other users. Therefore, in general, we can capture different aspects of reviewer behavior by modeling variables in an independent (univariate) or joint (multivariate) manner. The key goal of our work is to combine such univariate and multivariate models of reviewer behavior and use unsupervised learning to obtain a more robust anomaly detection system.

Over the past few years, different approaches have been proposed to detect fake reviews and reviewers starting with the pioneering work by Jindal and Liu [35]. Notable approaches include both supervised classification based methods [62, 63] and unsupervised techniques [1, 5, 57, 70]. However, even though probability distributions related to reviewing behavior have been studied in the past [15, 32, 35, 57], prior approaches do not fully exploit univariate and multivariate distributions associated with reviewers (and reviews) when detecting anomalies. For instance, Feng et al. [21] use only the J-shaped or bimodal characteristic typically associated with review ratings to flag reviewers who distort this shape, but they do not consider distributions over other possible features. Mukherjee et al. [57] develop a Bayesian learning approach to detect opinion spammers in Amazon.com reviews. However, since distinct features of online reviews have their own subtle distinctive distributional characteristics [15], the prior distributions used in Mukherjee et al. may not always be indicative of the true underlying distributions, thus biasing the model.

More recently, Kumar et al. [37] proposed an approach where they learn empirical distributions corresponding to several features from the data, and then use these distributions within a classifier, thus making the classifier more robust to noise and one that has better generalization. However, a major shortcoming of their proposed approach is that it requires the data to be labeled (with spam/no-spam labels). In general, it is quite difficult to obtain labeled data, especially for review spam detection [63]. In this work, we extend Kumar et al.’s [37] approach to develop a fully unsupervised model to identify review spam. Specifically, as in Kumar et al. [37], we learn independent probability distributions corresponding to univariate and multivariate features related to reviewing behavior. Once we obtain the empirical probability distributions, however, we develop a fully unsupervised method to combine the distributions into a unified anomaly detection model. Specifically, we develop a finite mixture model, where we combine the individual distributions that we learn corresponding to different features. We then learn the full mixture model by maximizing the overall log-likelihood of the data using an Expectation Maximization (EM) approach. Although we specifically consider the problem of detecting anomalous reviewers in the context of reviews, our general technique can be applied to other anomaly detection tasks quite easily. Note that the goal of this study is to detect fake reviewers rather than fake reviews.

To summarize, our main contributions are as follows:

1. We develop a novel probabilistic approach to detect anomalous reviewers in a fully unsupervised manner by learning a finite mixture model over derived feature distributions. Our approach is general in the sense that it can be regarded as a method to combine several heterogeneous distributions (both univariate and multivariate) into a unified model that represents overall behavior of a reviewer.

2. We perform a comprehensive experimental evaluation of our approach on real-world restaurant reviews taken from Yelp.com. Specifically, for our evaluation, we develop four baseline unsupervised methods for detecting anomalous reviews, namely Gaussian Mixture Models (GMM), Nonparametric Gaussian Mixtures, One-Class Support Vector Machines (SVMs), and Stacking (STK) with uniform weights. We compare our approach with each of these baselines on real-world data as well as synthetic data where we injected distributional anomalies. Furthermore, we compare our approach with two state-of-the-art unsupervised systems that have been evaluated for Yelp reviews, namely FraudEagle by Akoglu et al. [1] and SpEagle by Rayana and Akoglu [70]. We clearly show in our evaluation that our system outperforms all the baseline methods as well as FraudEagle and SpEagle in terms of accuracy.

In terms of practical implementation of our method, we need to consider the dynamic nature of online platforms. On Yelp and Amazon, an enormous amount of online reviews is posted every hour or even every minute. Our approach can be viewed as a generic method to unify complex distributional characteristics into a unified probabilistic model. In practice, the distribution of the features can be updated regularly depending on the computational burden of the platform. In addition, although the high-level methodology can be the same, the features used in the systems should depend on the practical contexts. (For example, restaurant review platforms, such as Yelp, could be different from product review platforms, such as Amazon.)

In our current research, we primarily focus on detecting online spammers in online platforms such as Yelp. However, our modeling and evaluation framework can be extended to the cases of detecting social media bots in large online social networks. “A social bot is a computer algorithm that automatically produces content and interacts with humans on social media.” [22]. In Computer Science literature, a number of studies have focused on the design of advanced methods to automatically detect social bots. In general, there are three approaches in the literature: (i) Graph-based social bot detection, (ii) crowdsourcing social bot detection, and (iii) feature-based social bot detection. The first approach relies on studying the network structure of a social graph. The second approach makes use of human detection and crowdsources detection work to human workers. The last approach adopts machine-learning techniques to learn behavioral patterns. Our method of detecting online spammers belongs to the third approach and can be generalized to the context of detecting social bots.

The rest of this paper is organized as follows. We first review related work and our dataset. Next, we present analysis of univariate and multivariate features associated with reviewer behavior. We then describe our mixture model that combines feature distributions. Finally, we present our baseline methods for anomaly detection and conclude with our experimental evaluation and discussion.

## Related Work

Review Manipulation on digital platforms is a widely studied topic [23, 28, 30, 39, 40, 43, 67]. Luca and Zervas [47] analyze the correlation between reviews and competition. Mayzlin [51] apply game theory to analyze review manipulation by firms. Mayzlin et al. [52] explore relationships between reviews and hotel characteristics. However, online deception detection is still an open research area [60, 69], motivating us to study and develop more sophisticated methods.

Machine-learning is the pre-dominant approach to automatically detect manipulation in reviews and/or other forms of social media communication [77, 95]. The vast majority of existing approaches are supervised machine-learning methods that require the training data to be labeled as spam or not spam. Jindal and Liu [35] detect fake online product reviews using a supervised learning approach to recognize several key features unique to the behavior of review spammers. Following this, over the last few years, other approaches have been proposed to detect fake reviews as well as fake reviewers [1, 44, 45, 57].

Ludwig et al. [48] develop a multilevel regression model to detect deception in e-mails. Benjamin et al. [4] investigate cybercriminal communities to identify potential long-term and key participants. Lim et al. [45] use abnormalities in ratings to detect spammers in product reviews using a supervised model and evaluate their approach on reviews taken from amazon.com. Mukherjee et al. [57] develop a Bayesian inference framework using similar features to Jindal et al. [36], but unlike Jindal et al. they use unsupervised learning. Wang et al. [87] propose an approach to detect review spammers based on graphs constructed from reviews. Xie et al. [89] propose an approach where they discover temporal pattern distortions to detect spammers. Fei et al. [19] develop an approach to detect spammers who operate in bursts. Specifically, they model the interdependencies between reviewers as a graph and use supervised graph propagation methods to label spammers. Li et al. [44] create a dataset that includes reviews for different products/services such as hotels, restaurants, and healthcare, and they build a classification framework using a Sparse Additive Generative Model. Abnormal network footprints are used by Ye and Akoglu [91] to uncover coordinated groups of online review spammers. Similarly, Mukherjee et al. [58] and Xu and Zhang [90] develop methods to detect spammer groups, namely spammers who collude with each other. More recently, Ye et al. [92] use temporal analysis to signal opinion spam. Specifically, they model reviews as time series data and detect deviations in this model as potential signals of opinion spammers.

The problem of opinion spam and related topics has also been studied by the Natural Language Processing community. Several methods have been proposed that use linguistics to detect fake/manipulative reviews. Ott et al. [62, 63] develop a supervised learning model using linguistic features that detected deception in reviews. Banerjee and Chua [3] conduct a linguistic analysis to identify key features and use Logistic Regression to build a supervised classifier. Similarly, Newman et al. [61] look into possible linguistic cues to identify deception in language. Hu et al. [31] develop a statistical method to examine the review text and style to determine if online products are subject to review manipulation. Zhou et al. [97] build a model to detect deception in online communication using statistical language models that take advantage of dependencies between words. Feng et al. [20] analyze deep syntactic structure in sentences to infer deception in reviews. They evaluate their approach on several benchmarks including tripadvisor.com and yelp. com reviews.

Our work builds upon previous studies that have tried to analyze reviewing behavior with standard probability distributions. For instance, Hu et al. [32] analyze review ratings from Amazon and showed that typically all product ratings had a J-shaped or bimodal distribution. Similar results have been observed in earlier work [10, 16] that shows asymmetry and skewness as typical characteristics of reviews in general. Dalvi et al. [15] analyze ratings in three distinct domains, namely products, movies, and restaurants, and they conclude that selection bias contributes to heavily skewed rating distributions in these domains. Unlike previous studies that focus mainly on analyzing distributional characteristics for rating scores, our work more generally analyzes distributions for varied and complex features of reviewer behavior.

Also, when we consider the general area of anomaly detection, several probabilistic models have been proposed (e.g., Chandola et al. [9]). In the context of anomaly detection specific to online reviews, there have been prior approaches that use probabilistic methods or models to detect spammers. Notably, Jindal et al. [36] define the problem as computing a measure of unexpectedness of rules regarding reviewer behavior. Mukherjee et al. [57] take a Bayesian approach and develop an unsupervised model for anomaly detection. Akouglu et al. [1] model the network structure between products and reviewers as a probabilistic graphical model, and used belief propagation [93] to label spammers. Rayana and Akoglu [70] extend this approach with SpEagle, where they examine behavioral features using meta-data and language as priors in the graphical model.

We have further reviewed the prior Information Systems (IS) literature to identify studies that use unsupervised learning approaches in general and for anomalous users’ detection in particular. There are numerous studies that have used unsupervised learning techniques in general. A few notable ones include Zheng et al. [96], Bockstedt and Goh [7], Visa et al. [85], Churilov et al. [12], Guo et al. [26], and Ivanova and Scholz [34]. Zheng et al. [96] use a semi-supervised ensemble learning embedded with independent component analysis to identify highly influential reviewers. Bockstedt and Goh [7] use unsupervised learning techniques to identify common seller strategies for the use of discretionary auction attributes. Churilov et al. [12] use undirected knowledge discovery (unsupervised learning methods) to group the patients. Guo et al. [26] explore unsupervised deep learning for personalized point-of-interest recommendation. Visa et al. [85] use unsupervised learning method in content-based informational retrieval.

Based on further investigation, we have observed that IS literature for detecting anomalous users using unsupervised learning techniques is limited in nature. To the best of our knowledge, there are only a few studies in the IS domain that have used unsupervised learning techniques to detect anomalous reviewers or reviews in particular. For example, Ivanova and Scholz [34] develop an unsupervised learning approach to dynamically aggregate online ratings. We believe that our approach is the first one to consider the heterogeneity of distributions that characterize reviewer behavior in an unsupervised manner. In particular, we propose a generic method to unify these heterogeneous distributions (both univariate as well as multivariate) and use unsupervised learning methods in a principled manner, to yield a unified anomaly detection model.

## Dataset

We use the dataset of restaurant reviews taken from Yelp.com shared by Rayana and Akoglu that was previously used in their study on opinion spam [70]. This dataset contains a subset of the information in Yelp reviews. Specifically, it contains the rating scores, the review text, the date when the review was posted, the user (anonymized) who posted the review, and the restaurant for which the review was posted.

A high-level description of the attributes of this dataset is shown in Table 1. The number of spammers indicated in Table 1 is based on the label provided by Yelp. com’s proprietary filtering algorithm. Plotting the histogram for the rating scores in this dataset yields the unimodal skewed (left) distribution as shown in Figure 1. Based on the distribution analysis of filtered reviews per year (please refer to Online Supplemental Appendix A for details), we observe that the filtered reviews are on the rise every year, which confirms that the presence of anomalous reviews and reviewers on the social media platform is a serious issue.

## Detecting Anomalous Reviewers

In this section, we describe our main contribution, that is, a fully unsupervised method for detecting fake reviewers using a hierarchical approach. Specifically, we first consider several features that are commonly used indicators of reviewer behavior [35, 45] and empirically derive univariate distributions that can best generalize these features. Prior literature has mainly focused on using features to detect online spammers. These approaches do not fully exploit univariate and multivariate distributions associated with reviewers (and reviews) when detecting anomalies. Our model contributes to the literature by deriving distributions for key features and combing these distributions into a finite mixture model. Next, we model the joint distribution between users and restaurants as a Dirichlet-multinomial distribution. A Dirichlet-multinomial distribution is a compound distribution where the compounding is a Polya urn scheme, which in our case models the process where positive (negative) reviews about a restaurant generate more positive (negative) reviews from users. Finally, we combine the heterogeneous distributions by stacking them together to obtain an overall model representing reviewer behavior, and we use this model to detect anomalous reviewers. Our underlying assumption is that even though fake reviewers may look genuine when we analyze them with respect to a single distribution, since a fake reviewer’s end goal is to bias opinions falsely, such users will show up as anomalies when we view their behavior across multiple distributions. For instance, a user who assigns a 1-star rating to a restaurant that most other users have also rated as poor seems like a genuine user if we model that restaurant’s review pattern. However, if the same user repeatedly underrates every restaurant he/she reviews, then it might signal that the user is an anomaly using a model of a user’s review pattern.

Table 1. Data Description

<table><tr><td>Variables</td><td>Values</td></tr><tr><td>Number of Users</td><td>260277</td></tr><tr><td>Number of Restaurants</td><td>5044</td></tr><tr><td>Range of Summary Ratings</td><td>1-5</td></tr><tr><td>Range of Dates</td><td>7/17/10 - 11/16/14</td></tr><tr><td>Number of Spammers</td><td>62228</td></tr></table>

![](/api/attachments/MKHKB84J/fulltext/images/bf3b7d87620f58f5e70dcdc34d5b720366b05405c84ece8e38d4f31134cecb79.jpg)  
Figure 1. Histogram of Review Ratings in our Dataset

In the remainder of this section, we first derive distributions for univariate reviewer features. Then, we model joint dependencies between reviewers and restaurants using a Dirichlet-multinomial distribution, and finally stack all the distributions using a mixture model.

## Modeling Univariate Features

Several features have been proposed in previous approaches for identifying opinion spammers [19, 35, 43, 45, 57, 59, 70]. Here, we do not develop new features, but instead, for statistics related to existing features, we empirically derive the best fitting distribution family for that statistic.

Specifically, given data corresponding to a feature $f ,$ the task is to find a distribution family that best fits . For this, we fit a set of standard distribution families, ${ \mathcal P } ,$ by maximizing the likelihood of each distribution in $\mathcal { P }$ over $\mathcal { D } .$ However, in practice, it has been observed that several statistics related to reviews have highly skewed distributions [35]. To handle such cases, we use a data transformation technique that is often used to obtain a better fitting model for distributions with extreme-skewness. Specifically, we employ two well-known transformations, the log-log and the log-linear transform. In the log-log transform, we transform the values of the features in each instance of  to their log values, and in the log-linear transform, we only transform the feature’s value to its log value. Following Kumar et al. [37], we apply log transformation because in many cases (as we see in our experiments), the data is highly skewed and regular distributions do not fit it very well. In such cases, transforming the frequency helps us ensure a better fit, since in general a linear fit would be more preferable to a nonlinear fit (since it has a simpler form) when it comes to generalization performance [37].

We then fit a Normal error regression model on the transformed data. Specifically, given the transformed data $\mathcal { D } ^ { \prime } = \{ ( X _ { i } , Y _ { i } ) \} _ { i = 1 } ^ { M }$ , we assume that $Y _ { i } = \beta _ { 0 } + \beta _ { 1 } X _ { i } + \epsilon _ { i }$ , where $\in _ { i } \sim N \big ( 0 , \sigma ^ { 2 } \big )$ and each error term is uncorrelated with all the other error terms. The distribution associated with the feature variable is given by $Y _ { i } \sim N \big ( \beta _ { 0 } + \beta _ { 1 } X _ { i } , \sigma ^ { 2 } \big )$ . We compute the parameters for the model, $\beta _ { 0 }$ and $\beta _ { 1 }$ , using Max-likelihood estimation. To obtain the distribution family for <sup>f</sup> , we compare the likelihood scores for each of the standard distribution families in and the Normal error regression models (with parameters $\beta _ { 0 } , \beta _ { 1 } )$ using the log-log and the log-linear transformed data. We choose the model that has the highest likelihood score as the distribution family that best generalizes <sup>f</sup> .

Next, we describe the feature statistics that we used and the type of distribution family that we choose for each feature. For the set, , we use a large set of standard distributions such as lognormal, beta, exponential, weibull, gamma, and so forth. Several of these distribution families can fit skewed distributions and J-shaped distributions, both of which are commonly encountered when analyzing review data [15, 32]. For readability in the subsequent figures, we only show the distribution for which we obtained the best likelihood score and also scale the feature values to a common range. Please note that we are approximating discrete frequency measures (that are observed in the data) with a continuous distribution. Therefore, the y-axis in the figures is a probability measure that fits the observed data based on the approximation with the continuous distribution. Of course, one could argue that we can simply use the discrete frequency measures (observed in the training data) and apply “nearest-neighbor” type of methods to approximate the frequencies in the test data. However, to reduce over-fitting, following Kumar et al. [37], we are generalizing the discrete measures with a continuous approximation based on standard distributions or transforms.

## Review Count

The number of reviews posted by a user is a useful feature to distinguish between a genuine and fake user. Specifically, paid reviewers may write many more or very few reviews compared to a regular user to avoid detection. Therefore, we derive the distribution of the number of reviews written by a user. The best fit for this distribution was the regression model with log-log transformed data. This is shown in Figure 2.

## Review Gap

The gap between messages is a useful statistic to distinguish between users who post messages in bursts as opposed to users who have a more uniform interval between messages. Fake reviewers in some cases may show the former tendency since genuine users typically write reviews when they visit restaurants, an activity that does not usually occur in bursts and is more uniform. The gap between the two successive reviews written by the same user is represented as follows:

$$
R G _ {i} = R _ {i, j} - R _ {i, j - 1},
$$

where $R G _ { i }$ corresponds to the review gap for the i-th user, $R _ { i , j }$ corresponds to the timestamp of the j-th review for user $i ,$ and $R _ { i , j - 1 }$ corresponds to the timestamp of the (<sup>j</sup> 1)-th review for user i.

We consider the average and standard deviation statistics of review gaps for a user. For the average statistic, the log-log transformed fit is the best fitting distribution as shown in Figure 3a. For the standard deviation, the best fitting distribution is again the regression model with a log-log transformation as shown in Figure 3b.

![](/api/attachments/MKHKB84J/fulltext/images/d6d2e180d7f7c4964e69b1b0c482b018e1abe3ec2fc8d6e5e2219cef53d345d1.jpg)  
Figure 2. Distribution for Review Count

![](/api/attachments/MKHKB84J/fulltext/images/bae502d1be2bea8ce2ff1a6e7053f6b37febe3d0ca43644766bf2db3393e246e.jpg)  
(a) Average

![](/api/attachments/MKHKB84J/fulltext/images/a9d365d9d26234c8dedaf73a03dfcd8d194cbe8cda65888b7a713bec8c277566.jpg)  
(b) Standard Deviation  
Figure 3. Distributions for Gaps between Reviews

## Rating Entropy

The genuine reviewer tends to write more balanced reviews, that is, equally critical or noncritical in nature. Therefore, the reviews may be distributed evenly across different ratings. By contrast, fake reviewers typically post uniform (extreme) reviews since their goal is either to artificially improve a restaurant’s quality rating or wrongly damage competitors. Therefore, their reviews tend to have smaller entropy. To assess randomness of the reviews, the entropy of the rating scores is computed as follows:

$$
E N _ {i} = \sum_ {j = 1} ^ {N} p _ {i, j} \log (p _ {i, j}),
$$

where $E N _ { i }$ is the entropy of a given user’s ratings, $p _ { i , j }$ is the probability of user i assigning a rating score $j ,$ and N is the number of rating scores that can be given by a user. For the entropy distribution, the best fit is obtained using the lognormal distribution as shown in Figure 4.

## Rating Deviation

Consider a reviewer whose pattern is to simply assign a low rating to each restaurant he/she reviews irrespective of the ratings given by others. To detect such reviewers, how their ratings deviate from the average restaurant ratings must be calculated. If the number of genuine reviewers is greater than the number of fake reviewers, it is possible to identify instances where a rating is significantly different from other reviews. We compute this measure as the absolute difference between the rating score assigned by a user to a restaurant and the average score received by the restaurant.

$$
R D _ {i} = \left| R _ {i, j} - \mu_ {H (j)} \right|,
$$

![](/api/attachments/MKHKB84J/fulltext/images/1245ee6ee08e2ca95c49805c2bfc35f4710676db72c4b672620da0b9946faaf0.jpg)  
Figure 4. Distribution for Rating Entropy

where $R D _ { i }$ corresponds to the rating deviation of the i-th user, $R _ { i , j }$ is the rating score given by the i-th reviewer for the j-th review which corresponds to restaurant $H ( j )$ 2 and $\mu _ { H ( j ) }$ is the mean rating for this restaurant. The distributions associated with the rating deviation of users is shown in Figure 5. For the average and standard deviation of this feature, the best fit is obtained using the lognormal distribution and the beta distribution respectively as shown in Figures 5a and 5b.

## Time of Review

Fake reviewers sometimes act very early (first reviews for a restaurant) in order to extend their influence over other reviews. Thus, if we notice a user who always reviews restaurants before any other user, then that might signal suspicious behavior. We model this using the difference (in days) between the time a reviewer reviews a restaurant and the first review posted for that restaurant. Time of Review $T R _ { i }$ for the i-th user is represented as follows:

![](/api/attachments/MKHKB84J/fulltext/images/7f4c1d27addd19ddd0e19a85d0d0e53f608ba40798f638590e47dfa1a05527a4.jpg)  
(a) Average  
Figure 5. Distributions for Rating Deviation

![](/api/attachments/MKHKB84J/fulltext/images/5463af0da837639d1bc6e91ad0c8b0116ece41f9d5b6192422c31603c58d7db3.jpg)  
(b) Standard Deviation

$$
T R _ {i} = \big (T _ {i, j} - D _ {H (j)} \big),
$$

where $T _ { i , j }$ is the timestamp for the j-th review written by the i-th user, $H ( j )$ is the restaurant corresponding to the j-th review, and $D _ { H ( j ) }$ is the timestamp for the initial review for this restaurant. Figure 6 shows the distribution of the average and standard deviation of the time deviations across users. The lognormal and the beta distribution yield the best fit for the average and standard deviation, respectively.

## Rating Scores

Figure 7 shows the distribution of the mean ratings and the standard deviation over ratings. Fake reviewers may tend to give out more extreme rating scores (e.g. rating 5 or rating 1) to influence other users, which can be captured by this feature. In this case, the beta distribution is the best fit for both the average and standard deviation of rating scores across all users.

## Text Length

We consider the number of words used in the review since fake reviewers may write reviews without too much information as opposed to genuine reviewers who write more detailed reviews. Specifically, we consider unigrams in the review text and pre-process the text by removing the stop words, performing word stemming (using Porter-stemmer) and lemmatization. We then count the total number of unique words after the pre-processing step. Figure 8 shows the distribution of users with respect to the average and standard deviations over word-counts. The lognormal and the beta distributions are the best fit distributions for the average and standard deviation statistics for this feature, respectively.

![](/api/attachments/MKHKB84J/fulltext/images/ab8998cb971da3512db2e9e149048618b955b8868a39839dd23b0d05acda0eda.jpg)  
(a) Average  
Figure 6. Distributions for Time Deviation

![](/api/attachments/MKHKB84J/fulltext/images/a335b25b3241925b444ac5a9ec7fb2927277941ddbe1c8b9e50ab5eb12ed1704.jpg)  
(b) Standard Deviation

![](/api/attachments/MKHKB84J/fulltext/images/3bbe43dfaacf8b4f2b0b9b3ec8ed138547befd10d754dfcc8671df65a6e9c62b.jpg)  
(a) Average

![](/api/attachments/MKHKB84J/fulltext/images/3e745451bfab3ae0bce9490a1e00118b00530da814c9e0402e0064477e37a668.jpg)  
(b) Standard Deviation

Figure 7. Distributions for Rating Scores  
![](/api/attachments/MKHKB84J/fulltext/images/6944ae82af6213f50fd9327a272027a5e95217bcc8a81608a0a4de79c7725c6f.jpg)  
(a) Average

![](/api/attachments/MKHKB84J/fulltext/images/d859d7c46129ba4d3b26bd49fef7dbc2398a993b12e16a68d88447cc44ca5e33.jpg)  
(b) Standard Deviation  
Figure 8. Distributions for Text Length

Table 2 represents the log-likelihood values obtained for each feature of the data using different distributions. We empirically chose the best fitting distribution for each feature based on the values obtained. Specifically, we choose the distributions with the maximum likelihood scores highlighted in bold. Our full list of features along with their summary statistics is shown in Table 3.

## Modeling Multivariate Features

Using univariate distributions to model individual review features has limitations for identifying bogus or deceptive reviews. Another factor to be considered is the mutual dependency between reviewers and restaurants. For example, consider a scenario where user ratings of a specific restaurant can be biased by the types of reviews the restaurant has received from other users. Specifically, some positive reviews could help generate more positive reviews, and some negative reviews could help generate more negative reviews. To model such interdependencies, we develop a joint model between reviewers and restaurants using a Dirichlet-multinomial distribution, which is also known as the multivariate Polya distribution.

Table 2. Performance Evaluation of Spammers Features Distributions

<table><tr><td>Feature</td><td>loglog</td><td>loglin</td><td>norm</td><td>log-norm</td><td>beta</td><td>Rayleigh</td><td>weibull-min</td></tr><tr><td>Review Count</td><td>-7.47</td><td>-9.54</td><td>-94.89</td><td>-11.62</td><td>-28.82</td><td>-78.92</td><td>-13.18</td></tr><tr><td>Review Gap (avg)</td><td>-7.51</td><td>-14.62</td><td>-97.18</td><td>-9.71</td><td>-59.65</td><td>-76.92</td><td>-10.22</td></tr><tr><td>Review Gap (sd)</td><td>-6.53</td><td>-13.22</td><td>-24.67</td><td>-7.85</td><td>-11.17</td><td>-20.29</td><td>-7.16</td></tr><tr><td>Rating Entropy</td><td>-15.59</td><td>-13.62</td><td>-9.56</td><td>-7.15</td><td>-7.78</td><td>-7.28</td><td>-7.26</td></tr><tr><td>Rating Dev (avg)</td><td>-16.32</td><td>-13.28</td><td>-22.38</td><td>-10.36</td><td>-11.93</td><td>-12.17</td><td>-18.29</td></tr><tr><td>Rating Dev (sd)</td><td>-15.71</td><td>-13.26</td><td>-11.4</td><td>-8.21</td><td>-8.05</td><td>-9.96</td><td>-9.22</td></tr><tr><td>Time of Review (avg)</td><td>-15.37</td><td>-14.17</td><td>-8.12</td><td>-7.24</td><td>-7.28</td><td>-8.03</td><td>-8.47</td></tr><tr><td>Time of Review (sd)</td><td>-15.38</td><td>-13.71</td><td>-7.29</td><td>-7.21</td><td>-5.74</td><td>-7.86</td><td>-7.1</td></tr><tr><td>Rating Scores (avg)</td><td>-15.76</td><td>-18.44</td><td>-5.78</td><td>-5.77</td><td>-3.83</td><td>-4.86</td><td>-7.02</td></tr><tr><td>Rating Scores (sd)</td><td>-15.39</td><td>-15.15</td><td>-6.73</td><td>-6.82</td><td>-6.43</td><td>-7.82</td><td>-6.94</td></tr><tr><td>Text Length (avg)</td><td>-16.74</td><td>-13.27</td><td>-35.74</td><td>-8.17</td><td>-12.67</td><td>-25.6</td><td>-10.52</td></tr><tr><td>Text Length (sd)</td><td>-16.4</td><td>-12.95</td><td>-23.03</td><td>-8.58</td><td>-7.91</td><td>-17.92</td><td>-8.39</td></tr><tr><td>Multivariate Feature</td><td colspan="7">-0.015 (dirichlet distribution)</td></tr></table>

Table 3. Feature Statistics for Yelp Dataset

<table><tr><td>Feature</td><td>Mean</td><td>Std</td><td>Min</td><td>Max</td></tr><tr><td>Review Count</td><td>4.86</td><td>20.59</td><td>2</td><td>205</td></tr><tr><td>Review Gap (Avg)</td><td>163.4</td><td>260.4</td><td>0</td><td>3046</td></tr><tr><td>Review Gap (Std)</td><td>69.6</td><td>126.5</td><td>0</td><td>1488</td></tr><tr><td>Rating Entropy</td><td>1.20</td><td>0.69</td><td>0.45</td><td>5.25</td></tr><tr><td>Rating Deviation (Avg)</td><td>0.82</td><td>0.44</td><td>0</td><td>3.34</td></tr><tr><td>Rating Deviation (Std)</td><td>0.41</td><td>0.28</td><td>0</td><td>1.77</td></tr><tr><td>Time from Initial Review (Avg)</td><td>1477</td><td>661.6</td><td>0</td><td>3602</td></tr><tr><td>Time from Initial Review (Std)</td><td>590.50</td><td>362.42</td><td>0</td><td>1798.50</td></tr><tr><td>Rating Scores (Avg)</td><td>3.60</td><td>0.74</td><td>1</td><td>5</td></tr><tr><td>Rating Scores (Std)</td><td>0.66</td><td>0.50</td><td>0</td><td>2</td></tr><tr><td>Text Length (Avg)</td><td>53.59</td><td>38.48</td><td>0</td><td>480</td></tr><tr><td>Text Length (Std)</td><td>20.85</td><td>20.59</td><td>0</td><td>205</td></tr></table>

The Dirichlet-multinomial distribution, well known as a conjugate prior for multinomial distributions, is widely used for modeling multivariate count data and has several applications such as document clustering [17], genomics [29], topic modeling [54], and so forth. The Dirichlet-multinomial distribution is a compound distribution where we assume that the observed data is generated from a distribution p, which is itself drawn from a Dirichlet distribution. The compounding follows a Polya Urn scheme which is particularly useful to model processes that typically have the “richget-richer” effect [49]. Therefore, this is well suited in our case to model the interdependency between reviewer ratings and restaurant ratings where initial reviews typically have an influence on subsequent reviews [65]. Note that the Dirichlet distribution is one of the components in the mixture model. Thus, our mixture model can seamlessly integrate different types of distributions (univariate and multivariate) into a unified model. We next describe how we learn the Dirichletmultinomial distribution from our data.

Consider a user $u _ { i }$ (where i is the index for the users) who has rated <sup>m</sup> restaurants. We consider the joint distribution between the ratings given by $u _ { i }$ with the types of restaurants he/she has reviewed. Specifically, this is represented as a sequence of 2<sup>m</sup> variables, $x _ { 1 } , \hdots , x _ { m } , y _ { 1 } , \hdots , y _ { m } .$ , where $x _ { 1 } , \ldots , x _ { m }$ are the rating scores given by $u _ { i } ,$ and $y _ { 1 } , \ldots , y _ { m }$ are the average rating scores for each restaurant that the user has reviewed respectively. We now define the Polya distribution over 2<sup>C</sup> count variables for $u _ { i } ,$ where <sup>C</sup> is the total number of rating-bins. In our case, we have 5 bins, corresponding to rating scores $\leq ~ 1$ , rating scores $> 1 \ a n d \leq 2$ , rating scores $> 2 \ a n d \leq 3$ ; rating scores $> 3 \ a n d \leq 4$ , and rating scores ${ > } 4$ : Thus, user $u _ { i }$ is represented by a count vector $\langle n _ { i 1 } , n _ { i 2 } , \ldots , n _ { i 2 C } \rangle$ , where for the first <sup>C</sup> dimensions in the vector, $n _ { i k }$ corresponds to the number of reviews $u _ { i }$ has written corresponding to rating-bin <sup>k</sup>, and for the last <sup>C</sup> dimensions of the vector, $n _ { i k }$ corresponds to the number of restaurants reviewed by $u _ { i }$ with an average rating in rating-bin <sup>k</sup>. For example, if a user has rated three restaurants with scores, 2, 3, and 5, respectively, and the average ratings for those restaurants are 3.5, 3.25, and 4.4, respectively, the count vector for this user is given by 0; 1; 1; 0; 1; 0; 0; 0; 2; 1 . Note that $\textrm { y } ( y _ { 1 } , \dots , y _ { m } )$ , for example, represents the average rating scores of restaurants reviewed by a specific user. More specifically, we have used the scores at the time the user submits his/her rating, not at the time of data collection. Also, we have not considered the time of review in this formulation. Given a count vector for any user, represented generally by -<sup>u</sup>, the Polya distribution is given by

$$
\mathrm{P} (\bar {u} | \alpha) = \frac {\Gamma \sum_ {k} \alpha_ {k}}{\Gamma \left(\sum_ {k} n _ {k} + \alpha_ {k}\right)} \prod_ {k} \frac {\Gamma (n _ {k} + \alpha_ {k})}{\Gamma (\alpha_ {k})}\tag{1}
$$

where $a = a _ { 1 } , \ldots , a _ { k }$ are called concentration parameters of the Dirichlet distribution from which the distribution that generated the count vector for user -<sup>u</sup> was drawn.

We now estimate α using $\mathcal { D } = \left\{ \bar { d } _ { i } \right\} _ { i = 1 } ^ { M }$ , where $\bar { d } _ { i }$ is the count vector for user ${ \bar { u } } _ { i } .$ Let $n _ { i k }$ be the k-th dimension of $\bar { d } _ { i }$ <sup>¼</sup>. The log-likelihood of  is given by

$$
\begin{array}{l} \log P (\mathcal {D} | \alpha) = \sum_ {i} \log P (\bar {u} _ {i} | \alpha) \\ \qquad = \sum_ {i} \log \Gamma \Big (\sum_ {k} \alpha_ {k} \Big) - \log \Gamma \Big (n _ {i} + \sum_ {k} \alpha_ {k} \Big) \\ \qquad + \sum_ {k} \Gamma (n _ {i k} + \alpha_ {k}) - \log \Gamma (\alpha_ {k}) \end{array}\tag{2}
$$

where $n _ { i } = \textstyle \sum _ { k } n _ { i k }$

We can now compute the concentration parameters α that maximize the likelihood function in Equation (2). Since the likelihood function in this case is convex, we can reach the global optima through gradient ascent. Specifically, we randomly initialize parameters α and update them in each iteration using the following update equation until we converge to a fixed point (See Minka [55] for the derivation).

$$
\alpha_ {k} ^ {t + 1} = \alpha_ {k} ^ {t} \frac {\sum_ {i} \Psi (n _ {i k} + \alpha_ {k} ^ {t})}{\sum_ {i} \Psi (n _ {i} + \sum_ {k} \alpha_ {k} ^ {t}) - \Psi (\sum_ {k} \alpha_ {k} ^ {t})}, (3)\tag{3}
$$

where $\Psi$ is the digamma function and $a _ { k } ^ { t }$ is the value of parameter $\alpha _ { k }$ in iteration t. In our experiments, we initialized $a _ { k } ^ { 0 }$ using the moment matching estimate method [55].

## Mixture Model

Each of the distributions specified in the previous two subsections model a specific univariate/multivariate feature. We now combine these distributions into a unified model that intuitively provides a more “global” view of reviewer behavior. Combining models into a more powerful ensemble model is a wellknown supervised machine-learning method used in algorithms such as Bagging [8] and Boosting [24]. In both these approaches, the idea is to train a classification algorithm on sampled portions of the training data to yield multiple models and finally average all the models to reduce variance and/or bias in the overall classifier. Along similar lines, Wolpert proposes a method called stacking [88] that can be used to combine heterogeneous classifiers into a unified classifier. Furthermore, Smyth and Wolpert [78, 79] extend the stacking approach to probability density estimation by combining heterogeneous probability distributions together. Here, based on this approach, we learn a finite mixture model, where the individual components of the mixture model are the probability distributions corresponding to the univariate/multivariate features, which we refer to as base distributions. The main idea in learning the mixture model is to first compute the cross-validated likelihood scores for each training instance w.r.t each base distribution, and then estimate the coefficients of the mixture model to maximize the combined likelihood.

Formally, let $P _ { 1 } \ldots P _ { K }$ be the base distributions for our model. Our stacked model is a <sup>K</sup> component mixture model $\left\{ \phi _ { 1 } , \dots \phi _ { K } , P _ { 1 } , \dots , P _ { K } \right\}$ , where $\phi _ { 1 } , \dots \phi _ { K }$ are the mixture coefficients. The mixture coefficient $\phi _ { j }$ represents the probability that a randomly chosen reviewer from the data was generated from the j-th component of the mixture model. Thus, the mixture coefficients specify a distribution, i.e., $\textstyle \sum _ { k } \phi _ { k } = 1$ . For computing the test likelihood for each instance, we divide the set of users  into <sup>N</sup> roughly-equal folds. We learn the parameters for each base distribution from <sup>N</sup>  1 folds and compute the probability density values for all the instances in the remaining fold from the learned base distributions. Note that for each base distribution, we assume that the distribution family is always fixed as given in the previous section. We only re-compute the parameters of each distribution from the <sup>N</sup> 1 folds. Thus, we have a $M \times K$ matrix where the $( i , j ) \ – \mathrm { t h }$ entry is equal to $P _ { j } ( \bar { u } _ { i } )$ , which is the out-of-sample likelihood for $\bar { u } _ { i }$ w.r.t the j-th base distribution. That is, the likelihood is computed from a distribution whose parameters are learned from training data that does not include ${ { \bar { u } } _ { i } }$

We now search for optimal values of the mixture coefficients in the model such that overall out-of-sample log-likelihood score is maximized. Specifically, the optimization problem is given by

$$
\max _ {\phi_ {1} \dots \phi_ {k}} \sum_ {i = 1} ^ {M} \log \sum_ {j = 1} ^ {K} \phi_ {j} P _ {j} (\bar {u} _ {i}).\tag{4}
$$

It is difficult to obtain a closed-form optimal solution for this optimization problem. Therefore, we use the EM (Expectation-Maximization) approach to optimize Equation (4). Specifically, let <sup>W</sup> be a $M \times K$ matrix of weights that determine the relative importance of each mixture component. The (<sup>i</sup>; <sup>j</sup>)-th entry in <sup>W</sup> represents the weight for the <sup>i</sup>-th user being generated by the <sup>j</sup>-th mixture component, and is given by

$$
w _ {i j} = \frac {\phi_ {j} P _ {j} (\bar {u} _ {i})}{\sum_ {k = 1} ^ {K} \phi_ {k} P _ {k} (\bar {u} _ {k})}.\tag{5}
$$

We start by initializing the mixture coefficients to random initial values, $\phi _ { 1 } ^ { ( 0 ) } \ldots \phi _ { K } ^ { ( 0 ) }$ . In each subsequent step, we re-compute each mixture coefficient as

$$
\phi_ {k} ^ {(t + 1)} = \frac {\sum_ {i = 1} ^ {M} w _ {i K}}{M}\tag{6}
$$

Note that in the typical use of EM algorithms for learning mixture models, such as in the Gaussian Mixture Model, in each step, the parameters of the mixture components, namely the Gaussian distributions, are re-estimated based on the updated mixture coefficients. However, in the stacking approach, we fix the parameters of the mixture components and only re-estimate the mixture coefficients in each step. We terminate the algorithm once the coefficients converge to a fixed point. In our experiments, we use the stopping criteria, max $\left| \phi _ { i } ^ { ( t ) } - \phi _ { i } ^ { ( t - 1 ) } \right| \leq 0 . 0 0 0 1$ . To avoid local minima, we run the learning algorithm from several initial random points and average the converged coefficient values across these runs.

Finally, we use all of the training data to re-estimate the parameters for each base distribution. Our final mixture distribution weighs each base distribution (with the re-learned parameters) with the learned mixture coefficients and is given by

$$
P (\bar {u}) = \sum_ {j = 1} ^ {K} \phi_ {j} P _ {j} (\bar {u}).\tag{7}
$$

Algorithm 1 summarizes our two-stage method for learning the mixture model. As shown here, in the first stage, we learn the parameters for the distributions corresponding to each feature. We then compute the weight matrix using the out-ofsample likelihood values for each user with respect to each of the learned distributions. Next, we compute the mixture coefficients that maximize the likelihood of the mixture model that combines the distributions. An anomalous user is likely to have a smaller probability with respect to the mixture distribution in Equation (7) as compared to a nonanomalous user.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Mixture Model Learning
Input: A set of distribution types $D_{1} \ldots D_{k}$, where each $D_{i}$ corresponds to the distribution-type of a univariate/multivariate feature for the dataset $\mathcal{D}$
Output: Mixture distribution $P(\bar{u})$
//Learn the mixture distributions
1 Divide $\mathcal{D}$ into 5 folds
2 for each fold $\mathcal{D}_{i}$ do
3 Estimate the parameters of $D_{1} \ldots D_{k}$ using the remaining 4 folds
4 $P_{1} \ldots P_{K}$= Estimated distributions for the features
5 for each user $\bar{u}_{i}$ in $\mathcal{D}_{j}$ do
6 Compute $P_{1}(\bar{u}_{i}) \ldots P_{K}(\bar{u}_{i})$
7 Compute $w_{ij}$, for $1 \leq j \leq K$ using Eq. (5)
//Learn the mixture coefficients
8 initialize the coefficients $\phi_{1} \ldots \phi_{K}$ randomly
9 while $\phi_{1} \ldots \phi_{K}$ have not converged do
10 Update $\phi_{1} \ldots \phi_{K}$ using Eq. (6)
11 Return $\sum_{j=1}^{K} \phi_{j} P_{j}(\bar{u})$
</div>

## Baseline Systems

To evaluate the performance of our stacked model in anomaly detection, we develop the following four unsupervised anomaly detection systems and use them as baselines in our experiments.

1. Gaussian Mixture Models based anomaly detection: Here, we model the joint distribution over users by a finite mixture of multivariate Gaussian distributions. This approach is similar to the general anomaly detection approach proposed in Song et al. [80]. This baseline model constitutes the case where we do not consider the natural distribution shapes of individual features when modeling the overall joint distribution. In other words, we assume that the joint distribution over reviewers can be modeled as a mixture of Gaussians. To learn this model, we use the EM algorithm for Gaussian mixtures.

2. Nonparametric Gaussian Mixture Models based anomaly detection: This model is similar to GMM except that we do not fix the number of mixture components a priori. We learn the optimal number of mixture components using a Bayesian approach. That is, we assume that the components are generated from a Dirichlet process-distributed distribution. Thus, this baseline is a fully nonparametric approach for anomaly detection. We use the EM algorithm for finite Gaussian mixtures to learn the parameters of this model.

3. One-Class SVM based anomaly detection: One-Class SVMs are a stateof-the-art approach for outlier detection [75, 76]. Unlike traditional SVMs which are used for classification, in One-Class SVMs all the examples in the training data are considered as belonging to a single (positive) class. Thus, the SVM model is only learned over one class and examples that are classified as out-of-class are considered outliers. During training, a tunable parameter bounds the number of data points in data that are to be regarded as outliers (or out-of-class examples). Similar to standard SVMs, several different kernels, such as the linear kernel, Radial Basis Function (RBF) kernel, or the sigmoid kernel, can be used within One-Class SVMs. One-Class SVMs have been used for anomaly detection in various studies [2, 27, 81]. We construct features for our One-Class SVM based anomaly detector as follows. We use all the univariate features that we use in the stacking-based model, but we use their raw values instead of converting them to their probability values. For the multivariate feature, we use the raw counts to learn the Dirichlet-multinomial. We standardize all the feature values by subtracting them by the mean and then dividing by the standard deviation of the feature. This baseline models the case where we do not explicitly consider the probability distributions that generate the feature values for anomaly detection.

4. Uniform Stacking based anomaly detection: In this model, similar to our stacking model, we combine the learned base distributions into a mixture model. However, we do not learn the mixture component weights, as in the stacked model. Instead, we weigh each component equally. That is, given individual distributions, $P _ { 1 } \ldots P _ { k }$ , we combine them into a single mixture distribution as,

$$
P (\bar {u}) = \sum_ {j = 1} ^ {K} \frac {1}{K} P _ {j} (\bar {u}).
$$

Using this baseline, we wish to evaluate the case where we consider the underlying distributional characteristics of each feature, but we simply give each base distribution equal importance in the overall mixture model.

## Experimental Setup and Results

## Datasets

We use two datasets in our experiments. The first one is a synthetic dataset where we inject anomalies and the next one is the real-world Yelp.com dataset described in the earlier section. We generate the synthetic dataset as follows. We generate the set of nonanomalous instances in the data by sampling each feature from its corresponding distribution (derived in the earlier section). For generating anomalous instances, we use the following sampling strategy. Following the work by Eskin [18], for each feature, we assume that with probability $\alpha ,$ the feature value is sampled from its corresponding distribution, and with probability $1 - \alpha ,$ it is sampled from a uniform distribution since we do not know a priori the distribution for the anomalous features. Thus, for an anomalous instance, certain features may look anomalous with respect to the feature’s natural distribution, and certain other features may look non-anomalous with respect to its distribution. Similar to that in past studies, we set $\alpha$ as 0.25 in our experiments. We generate 10,000 instances of nonanomalous users and vary the percentage of anomalous users in the dataset in our experiments.

## Evaluation Setup

Evaluating the performance of our system is a challenging problem by itself. The main issue is the lack of annotated or gold standard data since labeling the data is quite challenging. To get around this problem, some earlier studies have used crowdsourcing to write known deceptive reviews. For instance, in Ott et al. [62, 63], the authors used Amazon Mechanical Turk to have paid reviewers write false reviews for TripAdvisor, thus creating a labeled dataset with known anomalies. For the Yelp dataset that we used, it turns out that yelp.com generates its own classification of spam, also called “filtered reviews,” which are available to us as labels of anomalies. Unfortunately, the method used by yelp.com for their classification is proprietary. Therefore, it is quite hard to verify what these labels signify and to determine what anomalous behaviors of spammers are considered in Yelp’s classification. However, Mukherjee et al. [59] empirically studied the Yelp filtering algorithm in detail and were quite positive in their analysis regarding the performance of the filtering system in identifying opinion spammers. Therefore, even though it is not an ideal gold standard, for the purpose of our evaluation, we choose to use Yelp’s labels to signal anomalies in our dataset. Specifically, we label a reviewer as anomalous if he/she has even one review that has been filtered out by Yelp’s filtering algorithm. This assumption is similar to the assumptions made in previous work [70] and is consistent with our observations in the dataset. Specifically, in our Yelp dataset, 62,228 reviewers have written at least one filtered review, and out of these reviewers, 60,107 of them have all their reviews marked as filtered reviews.

In our evaluation, we use standard metrics for comparing performance. For comparing accuracy, we use the ROC-AUC (area under the ROC curve) scores. For measuring relevance, we use precision@K, a measure commonly used to measure effectiveness of information retrieval systems [50], where relevant results at the top are far more important than the relevant results returned at the bottom. In our case, precision@K is the ratio of spammers in the first k users ranked by the anomaly detector. Thus, a more effective anomaly detection method will place several anomalous reviewers at the top of its rankings.

Finally, to evaluate how well a model fits the data, we use its test log-likelihood score. Specifically, we run k-fold cross validation and we learn the parameters of the model on the training folds and compute log-likelihood of the data in the test fold using the learned parameters. We repeat this process for all k folds and report the average log-likelihood over the folds.

While describing our results in the following section, we abbreviate our approaches as: Stacking (STK), Gaussian Mixture Model (GMM), non-parametric Dirichlet Process Gaussian Mixture Model (DPGMM), One-Class SVMs (OSVM) and Uniform Stacking (UM).

## Results on Synthetic Data

Figure 9 illustrates the ROC curves obtained using different competing methods for varying amount of anomalies in the data (controlled by parameter p). Table 4 shows the corresponding ROC-AUC scores obtained for the ROC curves. We report the average ROC-AUC scores over the scores obtained using five-fold cross-validation. Here, OSVM-L, OSVM-R and OSVM-S denote the linear, RBF, and sigmoid kernels used within OSVM, respectively. Note that we have included only the best performing OSVM in Figure 9 for readability purpose.

As seen from our results, STK obtained the best score for all values of p as compared to the other baseline methods. In general, as the number of anomalous reviewers increases in the dataset, the accuracy of the anomaly detector goes down slightly, since anomalies distort the distributions learned for the features to a greater extent.

Figure 10 compares the log-likelihood scores for the different probabilistic methods for varying amounts of anomalies in the data. As seen here, for all values of ${ \dot { p } } ,$ , the log-likelihood score for STK is higher than all the other baseline methods. UM has the next highest score, which is significantly higher than the scores obtained using GMM and DPGMM. This illustrates that our stacking-based mixture models fit the data better when features are derived from multiple heterogeneous distributions as compared to methods that make assumptions about the underlying distribution (e.g., GMM and DPGMM assume that the data is generated from a mixture of multivariate Gaussian distributions).

![](/api/attachments/MKHKB84J/fulltext/images/d275b6ef5d5ce04e08627a8f60aea0d9ebb2248ef1cd895aa2b8855f16fbee58.jpg)  
(a) $p = \pmb { \theta } . \pmb { \theta } I$

![](/api/attachments/MKHKB84J/fulltext/images/555b6a49e9e7fb1ecb20ca7586c05452de3ca5586fd31b3a560dfd261f705294.jpg)  
(b) $\mathbf { \varepsilon } _ { p } = \mathbf { \varepsilon } _ { 0 . } \mathbf { \varepsilon } _ { 0 5 }$

![](/api/attachments/MKHKB84J/fulltext/images/2cfd7edbacb500b304f13d399552b5e6439e922542966e2e8e497344740fc2c7.jpg)  
(c) $p = \pmb { \theta } . \pmb { I } \pmb { \theta }$

![](/api/attachments/MKHKB84J/fulltext/images/2757a1670febb6c99f300cf03974c8921c1247842461e5f8e6979bdd8ff0414c.jpg)  
(d) $p = \pmb { \theta } . \pmb { I } \pmb { \bar { s } }$

![](/api/attachments/MKHKB84J/fulltext/images/cda9fbe62f21bda486fa25578dc68fc1e6773f3be891c9d0e44981ee20bcf106.jpg)  
(e) $\mathbf { \varepsilon } _ { p } = \mathbf { \varepsilon } _ { 0 . 2 0 }$

![](/api/attachments/MKHKB84J/fulltext/images/e430149c71a5a1669c6ceeddd89a0c373c26115204c635db667c2dc91d640e53.jpg)  
(f) $\mathbf { \varepsilon } _ { p } = \mathbf { \varepsilon } _ { 0 . 2 5 }$  
Figure 9. ROC Curves (Synthetic data) for Varying Percentage of Anomalies (denoted by <sup>p</sup>)

Table 4. ROC-AUC Scores (Synthetic Data) for Varying Percentage of Anomalies (<sup>p</sup>)

<table><tr><td>p</td><td>GMM</td><td>DPGMM</td><td>OSVM-L</td><td>OSVM-R</td><td>OSVM-S</td><td>UM</td><td>STK</td></tr><tr><td>0.01</td><td>0.45</td><td>0.46</td><td>0.84</td><td>0.81</td><td>0.82</td><td>0.69</td><td>0.93</td></tr><tr><td>0.05</td><td>0.45</td><td>0.45</td><td>0.83</td><td>0.79</td><td>0.80</td><td>0.68</td><td>0.89</td></tr><tr><td>0.10</td><td>0.45</td><td>0.44</td><td>0.83</td><td>0.78</td><td>0.81</td><td>0.68</td><td>0.89</td></tr><tr><td>0.15</td><td>0.45</td><td>0.45</td><td>0.82</td><td>0.81</td><td>0.82</td><td>0.68</td><td>0.89</td></tr><tr><td>0.20</td><td>0.45</td><td>0.44</td><td>0.81</td><td>0.81</td><td>0.82</td><td>0.67</td><td>0.87</td></tr><tr><td>0.25</td><td>0.45</td><td>0.44</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.68</td><td>0.85</td></tr></table>

![](/api/attachments/MKHKB84J/fulltext/images/f5de413f0a4e76011ff52b4daeb0629a2b453422fff70320bee74171115265cc.jpg)  
Figure 10. Comparison of Log-Likelihood Scores (Synthetic Data)

## Results on Real-World Data

Figure 11 shows the ROC curves for STK and the other baseline algorithms. As seen from our results, our approach performs much better than the OSVM based approaches as well as the Gaussian Mixture Models based methods. UM is the best performing algorithm among the baseline anomaly detectors.

We next compare the accuracy of our approaches with two state-of-the-art unsupervised approaches, FraudEagle [1] and SpEagle [70]. Both these approaches model the joint distribution using a Markov Random Field (MRF). Computing exact probabilities from the MRF is a computationally hard problem. Therefore,

![](/api/attachments/MKHKB84J/fulltext/images/0802e97249b1f7bd6cb7319779b24d5f6d62343db287ea4e1557db33906bf224.jpg)  
Figure 11. Comparison of ROC Curves (Yelp Data)

FraudEagle and SpEagle use a well-known approximate inference method known as Loopy Belief Propagation [66, 93]. The results for both these methods are available for the same Yelp dataset [70]. Table 5 compares the ROC-AUC scores for our method with the corresponding scores obtained for the baselines as well as FraudEagle and SpEagle. As seen here, our approach performs better than all the other approaches. It improves over the ROC-AUC score obtained in SpEagle by around 3 points. It performs significantly better than GMM, DPGMM, and OSVM. UM is the best performing baseline algorithm, which also performs slightly better than FraudEagle but worse than SpEagle.

Table 6 shows the results for precision@K, that is, the percentage of spammers at the top K positions when we rank users in the dataset. As we see here, STK outperforms all the baseline anomaly detectors by a significant margin for each value of K. It also performs better than SpEagle for several smaller values of K. For slightly larger values of K, STK and SpEagle achieve comparable scores. This means that STK is quite precise in its top rankings of anomalies. The best performing baseline method is UM that outperforms the OSVM based methods as well as GMM and DPGMM. Note that the results for FraudEagle precision@K were unavailable to us, and therefore, we do not report them here.

Table 5. Comparison of ROC-AUC Scores (Yelp Data)

<table><tr><td>Algorithm</td><td>AUC-Score</td></tr><tr><td>GMM</td><td>0.52</td></tr><tr><td>DPGMM</td><td>0.53</td></tr><tr><td>OSVM-L</td><td>0.49</td></tr><tr><td>OSVM-R</td><td>0.49</td></tr><tr><td>OSVM-S</td><td>0.49</td></tr><tr><td>UM</td><td>0.62</td></tr><tr><td>FraudEagle</td><td>0.61</td></tr><tr><td>SpEagle</td><td>0.67</td></tr><tr><td>STK</td><td>0.70</td></tr></table>

Table 6. Comparison of precision@K (Yelp Data)

<table><tr><td>K</td><td>GMM</td><td>DPGMM</td><td>OSVM-L</td><td>OSVM-R</td><td>OSVM-S</td><td>UM</td><td>SpEagle</td><td>STK</td></tr><tr><td>100</td><td>0.13</td><td>0.13</td><td>0.38</td><td>0.1</td><td>0.38</td><td>0.32</td><td>0.44</td><td>0.57</td></tr><tr><td>200</td><td>0.13</td><td>0.14</td><td>0.20</td><td>0.28</td><td>0.20</td><td>0.30</td><td>0.53</td><td>0.54</td></tr><tr><td>300</td><td>0.14</td><td>0.13</td><td>0.14</td><td>0.19</td><td>0.14</td><td>0.26</td><td>0.5</td><td>0.54</td></tr><tr><td>400</td><td>0.12</td><td>0.13</td><td>0.12</td><td>0.14</td><td>0.12</td><td>0.26</td><td>0.54</td><td>0.54</td></tr><tr><td>500</td><td>0.12</td><td>0.12</td><td>0.12</td><td>0.13</td><td>0.12</td><td>0.25</td><td>0.52</td><td>0.5</td></tr><tr><td>600</td><td>0.13</td><td>0.13</td><td>0.11</td><td>0.13</td><td>0.11</td><td>0.24</td><td>0.51</td><td>0.5</td></tr><tr><td>700</td><td>0.13</td><td>0.12</td><td>0.10</td><td>0.12</td><td>0.10</td><td>0.25</td><td>0.50</td><td>0.48</td></tr><tr><td>800</td><td>0.13</td><td>0.12</td><td>0.11</td><td>0.11</td><td>0.11</td><td>0.25</td><td>0.50</td><td>0.48</td></tr><tr><td>900</td><td>0.13</td><td>0.13</td><td>0.11</td><td>0.11</td><td>0.11</td><td>0.25</td><td>0.49</td><td>0.48</td></tr><tr><td>1000</td><td>0.13</td><td>0.13</td><td>0.10</td><td>0.11</td><td>0.10</td><td>0.25</td><td>0.50</td><td>0.48</td></tr></table>

In our final experiment, we compare the log-likelihood scores for the four probabilistic methods namely, GMM, DPGMM, UM, and STK, for the Yelp dataset. Table 7 shows our results, from which it can be seen that STK fits the data much better than the competing approaches. GMM and DPGMM have significantly smaller log-likelihood scores, which indicate that leveraging the distributional shapes of the behavioral features is important to design a robust probabilistic model of a user’s online behavior. UM performs much better than GMM and DPGMM but worse than STK. This indicates that it is important to consider the importance of specific features in the mixture model in order to obtain a better fit for the data.

Note that in our study, we adopt a measure (log-likelihood score) that is widely used in the Computer Science (CS) literature [72, 46, 11, 25, 74]. The idea of including the log-likelihood scores (apart from the ROC-AUC) is to compare how well our probabilistic model fits the data. The number of parameters across the models is comparable to each other. That is, GMM, DPGMM, UM, and STK are all different mixture models. That is, each of them mixes several mixture component distributions. UM and STK use the same number of components (corresponding to our features) in the mixture. GMM uses the same number of components as UM and STK (but still do not fit the data very well) since it assumes that the mixture component distributions are Gaussian distributions. DPGMM uses even more components (and still does not fit very well due to the Gaussian distribution assumption) since we do not pre-specify the number of components in the mixture. That is, we use a Bayesian approach to learn the optimal number of components. Thus, all our models are comparable in terms of parameters. Thus, the fit of the distribution is based on how well we can model the underlying distribution in our mixture. The experiments related to log-likelihood scores illustrate this in general, and therefore seeks to complement our ROC-AUC scores. In addition, we have used AIC and BIC as performance metrics. The results are presented in Table 8. We observe that STK model outperforms the competing approaches. Our model for predicting or classifying a new user is very fast. Specifically, for around 18K users, it takes only 0.09 seconds to classify whether each of them is a real or fake reviewer. We measured these times on an Intel Core i7 3.1 GHz processor system with 16 GB memory. The implementation of our entire system was done using python available from the Anaconda distribution.

Table 7. Comparison of Log-Likelihood Scores (Yelp Data)

<table><tr><td>GMM</td><td>DPGMM</td><td>UM</td><td>STK</td></tr><tr><td>-64.50</td><td>-65.52</td><td>-10.40</td><td>-2.12</td></tr></table>

Table 8. Performance Comparison using AIC and BIC Scores

<table><tr><td></td><td>GMM</td><td>DPGMM</td><td>UM</td><td>STK</td></tr><tr><td>AIC</td><td>2316980</td><td>2991243</td><td>111498</td><td>110952</td></tr><tr><td>BIC</td><td>2324163</td><td>2998427</td><td>112074</td><td>111528</td></tr></table>

As part of the robustness test, we have used several methods to show generalizability of our approach. First, we have used a new test dataset and the results are presented in Online Supplemental Appendix B. Second, we have rerun our experiments using a stricter definition of filtered reviewers, i.e., reviewers who have all their reviews marked as filtered reviews. The results are presented and discussed in Online Supplemental Appendix C. Third, we have used two additional outlier detection methods: Local Outlier Factors (LOF) and Elliptic Envelopes (E-Env). The results are robust and are presented in Online Supplemental Appendix D.

## Discussion and Conclusions

Detecting fake reviewers in online forums is known to be a challenging task. Even though several approaches have been proposed to detect such reviewers, they do not fully exploit the underlying distributional characteristics of reviewing behavior. In this work, we propose a novel method for unsupervised identification of anomalous reviewers. The key idea in our approach is to combine several heterogeneous distributions that describe different facets of reviewing behavior into a unified model for anomaly detection. Specifically, we derive (1) univariate distributions of features commonly used to characterize reviewing habits, and (2) a Dirichlet-multinomial distribution that models the interdependent features. Furthermore, we stack these distributions into a single mixture model and learn the parameters of the model in an unsupervised manner using the EM algorithm. We perform a comprehensive experimental study in which we develop four baseline algorithms for anomaly detection based on Gaussian mixture models and One-Class SVMs. Using both synthetic data as well as real-world restaurant reviews from yelp.com, we compare our approach with the baseline algorithms and state-of-the-art unsupervised methods for spammer detection, and show that our approach outperforms all these methods.

Our research has important managerial implications for social media platforms. New social media technologies have facilitated information sharing and shaped the information to which individuals were exposed [68, 83, 84]. Meanwhile, these technologies enable misinformation to spread rapidly through online media, which suggests that social media platforms are vulnerable to manipulation [42]. For instance, false information on Twitter is retweeted by many more users — and far more rapidly — than true information [86]. Specifically, a false tweet claimed that Barack Obama was injured in an explosion has caused a \$130 billion loss in stock value [86]. Our proposed method offers a useful platform-based detection and intervention tool to correct biases that make social media platforms vulnerable to misinformation. As social media platforms have become the primary conduits of fake news, social bots (automated social media accounts) can magnify the spread of fake news by liking and sharing information. According to a recent estimate, 9-15 percent of active Twitter accounts are social bots [41]. Our novel hierarchical approach using unsupervised-learning approach on detecting online spammers can be generalized to identify social bots. Social media platforms can use our method to redesign their systems and curb the automated spread of news content by social bots.

With a surge in fake reviewers on social media platforms, the issue of detecting fake reviewers is of increasing importance to firms and their customers. Our research study is very timely since there is a great interest in deploying fake reviewers’ detection models in production by social media platforms. Detecting fake reviewers in a realworld production setting is a very complex task. Even after the development of one of the best performing machine-learning algorithms, deployment and maintenance of fake reviewers’ detection models into production on social media platforms can pose a challenge. The ongoing monitoring and review of a model’s success in detecting real fake reviewers is a critical component. If supervised models trained on historical labeled data are allowed to continue running on a social media platform, there is substantial risk of losing credibility because fake reviewers continuously come up with new tricks to game the system. The supervised learning models can lose their effectiveness and produce false signals when fake reviewers dynamically change behaviors. Social media platforms may not have access to the most up-to-date labeled dataset. In other situations, the high effort and costs associated with periodically (manually) labeling large amounts of data becomes a prohibitive factor when using supervised learning techniques. Even if we disregard all these challenges for a moment, the overhead of continuously updating model parameters with a new labeled dataset significantly add to the model deployment costs. In these situations, using unsupervised learning techniques that do not rely on the labeled data is more cost effective, and easier to deploy and maintain in a production environment. Moreover, when using unsupervised models, the social media platforms do not have to deal with the cumbersome task of labeling data at a regular time interval. Given the merits of the proposed unsupervised learning-based mixture models, deploying these models in the production environment does not pose a serious challenge. In addition, a plethora of open source deployment tools and libraries are available these days that support the methodology proposed in this paper.

Our approach can also be viewed as a generic method to unify complex distributional characteristics into a unified probabilistic model and is thus applicable across several domains. Future work includes applying our general approach to detect spammer groups [57, 90] by modeling them as multivariate distributions. We would also like to develop adaptive versions of our method [33] and integrate advanced linguistics into our model such as models that detect deceptive writing [63] and models for sentiment analysis [64].

## NOTES

1. See http://www.huffingtonpost.com/2013/09/25/fake-yelp-reviews\_n\_3983564.html, retrieved on March 19, 2019.

2. See http://www.nytimes.com/2011/08/20/technology/finding-fake-reviews-online.html, retrieved on March 19, 2019.

## Supplemental Material

Supplemental data for this article can be accessed on the publisher’s website.

## ORCID

Liangfei Qiu http://orcid.org/0000-0002-8771-9389

## REFERENCES

1. Akoglu, L.; Chandy, R.; and Faloutsos, C. Opinion fraud detection in online reviews by network effects. Proceedings of the International AAAI Conference on Weblogs and Social Media, 7, (2013), 2–11.

2. Amer, M.; Goldstein, M.; and Abdennadher, S. Enhancing one-class support vector machines for unsupervised anomaly detection. In Proceedings of the ACM SIGKDD Workshop on Outlier Detection and Description. New York, NY: ACM, 2013, pp. 8–15.

3. Banerjee, S.; and Chua, A.Y.K. A study of manipulative and authentic negative reviews. Proceedings of the International Conference on Ubiquitous Information Management and Communication, 8, (2014), 76:1-76:6.

4. Benjamin, V.; Zhang, B.; Nunamaker Jr, J.F.; and Chen, H. Examining hacker participation length in cybercriminal Internet-relay-chat communities. Journal of Management Information Systems, 33, 2 (2016), 482–510.

5. Bhattarai, A.; Rus, V.; and Dasgupta, D. Characterizing comment spam in the blogosphere through content analysis. Proceedings of IEEE Symposium on Computational Intelligence in Cyber Security, 1, (2009), 37–44.

6. Blanding, M. The yelp factor: Are consumer reviews good for business? Harvard Business School, 2011. https://hbswk.hbs.edu/item/the-yelp-factor-are-consumer-reviewsgood-for-business (accessed on July 4, 2018).

7. Bockstedt, J.; and Goh, K. H. Seller strategies for differentiation in highly competitive online auction markets. Journal of Management Information Systems, 28, 3 (2011), 235–268.

8. Breiman, L. Bagging predictors. Machine Learning, 24, 2 (1996), 123–140.

9. Chandola, V.; Banerjee, A.; and Kumar, V. Anomaly detection: A survey. ACM Computing Surveys, 41, 3 (2009), 15:1-15:58.

10. Chevalier, J.A.; and Mayzlin, D. The effect of word of mouth on sales: Online book reviews. Journal of Marketing Research, 43, 3 (2006), 345–354.

11. Chou, L.; Sarkhel, S.; Ruozzi, N.; and Gogate, V. On parameter tying by quantization. In Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence, 2016, pp. 3241–3247.

12. Churilov, L.; Bagirov, A.; Schwartz, D.; Smith, K.; and Dally, M. Data mining with combined use of optimization techniques and self-organizing maps for improving risk grouping rules: application to prostate cancer patients. Journal of Management Information Systems, 21, 4 (2005), 85–100.

13. ClearMyMail. Viagra spam e-mails.http://www.clearmymail.com/guides/viagra\_spam\_ emails.aspx (accessedon July 4, 2018).

14. Cormack, G.V. Email spam filtering: A systematic review. Foundations and Trends in Information Retrieval, 1, 4 (2008), 335–455.

15. Dalvi, N.N.; Kumar, R.; and Pang, B. Para ’normal’ activity: On the distribution of average ratings. Proceedings of the International AAAI Conference on Weblogs and Social Media, 7, (2013), 110–119.

16. Eliashberg, J.; and Shugan, S.M. Film critics: Influencers or predictors? Journal of Marketing, 61, 2 (1997), 68–78.

17. Elkan, C. Clustering documents with an exponential-family approximation of the dirichlet compound multinomial distribution. In Proceedings of the 23rd International Conference on Machine Learning. New York, NY: ACM, 2006, pp. 289–296.

18. Eskin, E. Anomaly detection over noisy data using learned probability distributions. In Proceedings of the Seventeenth International Conference on Machine Learning. San Francisco, CA: Morgan Kaufmann, 2000, pp. 255–262.

19. Fei, G.; Mukherjee, A.; Liu, B.; Hsu, M.; Castellanos, M.; and Ghosh, R. Exploiting burstiness in reviews for review spammer detection. Proceedings of the International AAAI Conference on Weblogs and Social Media, 7, (2013), 175–184.

20. Feng, S.; Banerjee, R.; and Choi, Y. Syntactic stylometry for deception detection. Proceedings of the Annual Meeting of the Association for Computational Linguistics, 50, (2012), 171–175.

21. Feng, S.; Xing, L.; Gogar, A.; and Choi, Y. Distributional footprints of deceptive product reviews. Proceedings of the International AAAI Conference on Weblogs and Social Media, 6, (2012), 98–105.

22. Ferrara, E.; Varol, O.; Davis, C.; Menczer, F.; and Flammini, A. The rise of social bots. Communications of the ACM, 59, 7 (2016), 96–104.

23. Forman, C.; Ghose, A.; and Wiesenfeld, B. Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets. Information Systems Research, 19, 3 (2008), 291–313.

24. Freund, Y.; and Schapire, R.E. Experiments with a new boosting algorithm. In Proceedings of the Thirteenth International Conference on Machine Learning. San Francisco, CA: Morgan Kaufmann, 1996, pp. 148–156.

25. Gogate, V.; Webb, W.; and Domingos, P. Learning efficient markov networks. In Advances in Neural Information Processing Systems, 2010, pp. 748–756.

26. Guo, J.; Zhang, W.; Fan, W.; and Li, W. Combining geographical and social influences with deep learning for personalized point-of-interest recommendation. Journal of Management Information Systems, 35, 4 (2018), 1121–1153.

27. Heller, K.A.; Svore, K.M.; Keromytis, A.D.; and Stolfo, S.J. One class support vector machines for detecting anomalous windows registry accesses. In Proceedings of the work shop on Data Mining for Computer Security, 2003.

28. Ho, S.M.; Hancock, J.T.; Booth, C.; and Liu, X. Computer-mediated deception: strategies revealed by language-action cues in spontaneous communication. Journal of Management Information Systems, 33, 2 (2016), 393–420.

29. Holmes, I.; Harris, K.; and Quince, C. Dirichlet multinomial mixtures: Generative models for microbial metagenomics. PLoS ONE, 7, 2 (2012), 1–15.

30. Hu, N.; Bose, I.; Gao, Y.; and Liu, L. Manipulation in digital word-of-mouth: a reality check for book reviews. Decision Support Systems, 50, 3 (2011), 627–635.

31. Hu, N.; Bose, I.; Koh, N.S.; and Liu, L. Manipulation of online reviews: An analysis of ratings, readability, and sentiments. Decision Support Systems, 52, 3 (2012), 674–684.

32. Hu, N.; Zhang, J.; and Pavlou, P.A. Overcoming the j-shaped distribution of product reviews. Communications of the ACM, 52, 10 (2009), 144–147.

33. Hulten, G.; Spencer, L.; and Domingos, P. Mining time-changing data streams. In Proceedings of the Seventh ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. New York, NY: ACM, 2001, pp. 97–106.

34. Ivanova, O.; and Scholz, M. How can online marketplaces reduce rating manipulation? A new approach on dynamic aggregation of online ratings. Decision Support Systems, 104, 4 (2017), 64–78.

35. Jindal, N.; and Liu, B. Opinion spam and analysis. In Proceedings of the 2008 International Conference on Web Search and Data Mining, New York, NY: ACM, 2008, pp. 219–230.

36. Jindal, N.; Liu, B.; and Lim, E.-P. Finding unusual review patterns using unexpected rules. In Proceedings of the 19th ACM International Conference on Information and Knowledge Management. New York, NY: ACM, 2010, pp. 1549–1552.

37. Kumar, N.; Venugopal, D.; Qiu, L.; and Kumar, S. Detecting review manipulation on online platforms with hierarchical supervised learning. Journal of Management Information Systems, 35, 1 (2018), 350–380.

38. Kurtzleben, D. Did fake news on Facebook help elect Trump? Here’s what we know. NPR News. April 11, 2018. https://www.npr.org/2018/04/11/601323233/6-facts-we-knowabout-fake-news-in-the-2016-election (accessed on July 4, 2018).

39. Lappas, T.; Sabnis, G.; and Valkanas, G. The impact of fake reviews on online visibility: a vulnerability assessment of the hotel industry. Information Systems Research, 27, 4 (2016), 940–961.

40. Lau, R.Y.K.; Liao, S.Y.; Kwok, R.C.W.; Xu, K.; Xia, Y.; and Li, Y. Text mining and probabilistic language modeling for online review spam detection. ACM Transactions on Management Information Systems, 2, 4 (2011), 1–30.

41. Lazer, D.M.; Baum, M.A.; Benkler, Y.; Berinsky, A.J.; Greenhill, K.M.; Menczer, F.; and Schudson, M. The science of fake news. Science, 359, 6380 (2018), 1094–1096.

42. Lee, S.Y.; Qiu, L.; and Whinston, A.B. Sentiment manipulation in online platforms: An analysis of movie tweets. Production and Operations Management, 27, 3 (2018), 393–416.

43. Li, F.; Huang, M.; Yang, Y.; and Zhu, X. Learning to identify review spam. Proceedings of the International Joint Conference on Artificial Intelligence, 22, 3 (2011), 2488–2493.

44. Li, J.; Ott, M.; Cardie, C.; and Hovy, E. Towards a general rule for identifying deceptive opinion spam. Proceedings of the Annual Meeting of the Association for Computational Linguistics, 52, (2014), 1566–1576.

45. Lim, E.-P.; Nguyen, V.-A.; Jindal, N.; Liu, B.; and Lauw, H.W. Detecting product review spammers using rating behaviors. Proceedings of the ACM International Conference on Information and Knowledge Management, 19, (2010), 939–948.

46. Lowd, D.; and Rooshenas, A. Learning markov networks with arithmetic circuits. In Artificial Intelligence and Statistics. 2013, pp. 406–414.

47. Luca, M.; and Zervas, G. Fake it till you make it: reputation, competition, and Yelp review fraud. Management Science, 62, 12 (2016), 3412–3427.

48. Ludwig, S.; Van Laer, T.; De Ruyter, K.; and Friedman, M. Untangling a web of lies: exploring automated detection of deception in computer-mediated communication. Journal of Management Information Systems, 33, 2 (2016), 511–541.

49. Mahmoud, H. Polya Urn Models (1st ed.). New York, NY: Chapman and Hall/CRC, 2008.

50. Manning, C.D.; Raghavan, P.; and Schütze, H. Introduction to Information Retrieval. New York, NY: Cambridge University Press, 2008.

51. Mayzlin, D. Promotional chat on the Internet. Marketing Science, 25, 2 (2006), 155–163.

52. Mayzlin, D.; Dover, Y.; and Chevalier, J. Promotional reviews: an empirical investigation of online review manipulation. American Economic Review, 104, 8 (2014), 2421–2455.

53. Michaels, J. Four digital marketing trends that will impact small business in 2015. Beyond Social Buzz, 2014. https://beyondsocialbuzz.co.uk/small-business-digital-marketingtrends/(accessed on July 4, 2018).

54. Mimno, D.M.; and McCallum, A. Topic models conditioned on arbitrary features with Dirichlet-multinomial regression. In Proceedings of the Twenty-Fourth Conference on Uncertainty in Artificial Intelligence. Arlington, VA: AUAI Press, 2008, pp. 411–418.

55. Minka, T. Estimating a Dirichlet distribution. Technical report, MIT, 2000.

56. Mintel. Seven in 10 Americans seek out opinions before making purchases. Mintel. June 3, 2015. http://www.mintel.com/press-centre/social-and-lifestyle/seven-in-10-americans -seek-out-opinions-before-making-purchases. (accessed on July 4, 2018).

57. Mukherjee, A.; Kumar, A.; Liu, B.; Wang, J.; Hsu. M., Castellanos; M., and Ghosh, R. Spotting opinion spammers using behavioral footprints. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 19, (2013), 632–640.

58. Mukherjee, A.; Liu, B.; and Glance, N. Spotting fake reviewer groups in consumer reviews. Proceedings of the International Conference on World Wide Web, 21, (2012), 191–200.

59. Mukherjee, A.; Venkataraman, V.; Liu, B.; and Glance, N.S. What yelp fake review filter might be doing? Proceedings of the International AAAI Conference on Weblogs and Social Media, 7, (2013), 409–418.

60. Narayan, R.; Rout, J. K.; and Jena, S. K. Review spam detection using opinion mining. In Progress in Intelligent Computing Techniques: Theory, Practice, and Applications. Springer, Singapore, 2018, pp. 273–279.

61. Newman, M.L.; Pennebaker, J.W.; Berry, D.S.; and Richards, J.M. Lying words: Predicting deception from linguistic styles. Personality and Social Psychology Bulletin, 29, 5 (2003), 665–675.

62. Ott, M.; Cardie, C.; and Hancock, J.T. Estimating the prevalence of deception in online review communities. Proceedings of the International Conference on World Wide Web, 21, (2012), 201–210.

63. Ott, M.; Choi, Y.; Cardie, C.; and Hancock, J.T. Finding deceptive opinion spam by any stretch of the imagination. Proceedings of the Annual Meeting of the Association for Computational Linguistics: Human Language Technologies, 49, 1 (2011), 309–319.

64. Pang, B.; and Lee, L. Opinion mining and sentiment analysis. Foundations and Trends in Information Retrieval, 2, 1–2 (2008), 1–135.

65. Park, S.; Shin, W.; and Xie, J. The first-review effect: Interdependence between volume and valence of online consumer reviews. Working paper, University of Florida, 2016. https://ssrn.com/abstract=2824846 (accessed on July 4, 2018).

66. Pearl, J. Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference. San Francisco, CA: Morgan Kaufmann, 1988.

67. Proudfoot, J.G.; Jenkins, J.L.; Burgoon, J.K.; and Nunamaker, J.F. Jr. More than meets the eye: how oculometric behaviors evolve over the course of automated deception detection interactions. Journal of Management Information Systems, 33, 2 (2016), 332–360.

68. Qiu, L.; Tang, Q.; and Whinston, A.B. Two formulas for success in social media: Learning and network effects. Journal of Management Information Systems, 32, 4 (2015), 78–108.

69. Olivieri, A.; Shabani, S.; Sokhn, M.; and Cudré-Mauroux, P. Creating task-generic features for fake news detection. In Proceedings of the 52nd Hawaii International Conference on System Sciences, 2019, pp. 5196–5205.

70. Rayana, S.; and Akoglu, L. Collective opinion spam detection: bridging review networks and metadata. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 21, (2015), 985–994.

71. Roberts, J. Amazon sues people who charge 5 for fake reviews. Fortune Magazine. October 19, 2015. http://fortune.com/2015/10/19/amazon-fake-reviews/(accessed on July 4, 2018).

72. Rooshenas, A.; and Lowd, D. Learning sum-product networks with direct and indirect variable interactions. In International Conference on Machine Learning, (2014), pp. 710–718.

73. Rudolph, S. The impact of online reviews on customers buying decisions. Business 2 Community. July 25, 2015. https://www.business2community.com/infographics/impactonline-reviews-customers-buying-decisions-infographic-01280945#iZwM69pSgVKLlH6A. 97 (accessed on July 4, 2018).

74. Sarkhel, S.; Venugopal, D.; Pham, T. A.; Singla, P.; and Gogate, V. Scalable training of markov logic networks using approximate counting. In Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence, 2016, pp. 1067–1073.

75. Schölkopf, B.; Platt, J.C.; Shawe-Taylor, J.C.; Smola, A.J.; and Williamson, R.C. Estimating the support of a high-dimensional distribution. Neural Computation, 13, 7 (2001), 1443–1471.

76. Schölkopf, B.; Williamson, R.C.; Smola, A.J.; Shawe-Taylor, J.; and Platt, J.C. Support vector method for novelty detection. Proceedings of Advances in Neural Information Processing Systems, 12, (1999), 582–588.

77. Siering, M.; Koch, J.A.; and Deokar, A.V. Detecting fraudulent behavior on crowdfunding platforms: the role of linguistic and content-based cues in static and dynamic contexts. Journal of Management Information Systems, 33, 2 (2016), 421–455.

78. Smyth, P.; and Wolpert, D. Linearly combining density estimators via stacking. Machine Learning, 36, 1 (1999), 59–83.

79. Smyth, P.; and Wolpert, D. Stacked density estimation. Proceedings of Advances in Neural Information Processing Systems, 10, (1997), 668–674.

80. Song, X.; Wu, M.; Jermaine, C.; and Ranka, S. Conditional anomaly detection. IEEE Transactions on Knowledge and Data Engineering, 19, 5 (2007), 631–645.

81. Stolfo, S.J.; Apap, F.; Eskin, E.; Heller, K.; Hershkop, S.; Honig, A.; and Svore, K. A comparative evaluation of two algorithms for windows registry anomaly detection. Journal of Computer Security, 13, 4 (2005), 659–693.

82. Stritfeld, D. The best book reviews money can buy. New York Times. August 26, 2012. http://www.nytimes.com/2012/08/26/business/book-reviewers-for-hire-meet-a-demand-foronline-raves.html (accessed on July 4, 2018).

83. Susarla, A.; Oh, J.H.; and Tan, Y. Influentials, imitables, or susceptibles? Virality and word-of-mouth conversations in online social networks. Journal of Management Information Systems, 33, 1 (2016), 139–170.

84. Susarla, A.; Oh, J.H.; and Tan, Y. Social networks and the diffusion of user-generated content: Evidence from YouTube. Information Systems Research, 23, 1 (2012), 23–41.

85. Visa, A.; Toivonen, J.; Vanharanta, H.; and Back, B. Contents matching defined by prototypes: Methodology verification with books of the Bible. Journal of Management Information Systems, 18, 4 (2002), 87–100.

86. Vosoughi, S.; Roy, D.; and Aral, S. The spread of true and false news online. Science, 359, 6380 (2018), 1146–1151.

87. Wang, G.; Xie, S.; Liu, B.; and Yu, P.S. Review graph based online store review spammer detection. Proceedings of the International Conference on Data Mining, 11, (2011), 1242–1247.

88. Wolpert, D. Stacked generalization. Neural Networks, 5, 2 (1992), 241–259.

89. Xie, S.; Wang, G.; Lin, S.; and Yu, P.S. Review spam detection via temporal pattern discovery. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 18, (2012), 823–831.

90. Xu, C.; and Zhang, J. Towards collusive fraud detection in online reviews. Proceedings of IEEE International Conference on Data Mining, 15, (2015), 1051–1056.

91. Ye, J.; and Akoglu, L. Discovering opinion spammer groups by network footprints. In Proceedings of the Joint European Conference on Machine Learning and Knowledge Discovery in Databases. Berlin, Heidelberg: Springer, (2015), pp. 267–282.

92. Ye, J.; Kumar, S.; and Akoglu, L. Temporal opinion spam detection by multivariate indicative signals. Proceedings of the International AAAI Conference on Web and Social Media, 10, (2016), 743–746.

93. Yedidia, J.S.; Freeman, W.T.; and Weiss, Y. Constructing free-energy approximations and generalized Belief propagation algorithms. IEEE Transactions on Information Theory, 51, 7 (2005), 2282–2312.

94. Yerazunis, W.S. The spam-filtering accuracy plateau at 99.9% accuracy and how to get past it. Proceedings of MIT Spam Conference, 2004.

95. Zhang, L.; Ma, B.; and Cartwright, D.K. The impact of online user reviews on cameras sales. European Journal of Marketing, 47, 7 (2013), 1115–1128.

96. Zheng, X.; Zhu, S.; and Lin, Z. Capturing the essence of word-of-mouth for social commerce: Assessing the quality of online e-commerce reviews by a semi-supervised approach. Decision Support Systems, 56, 4 (2013), 211–222.

97. Zhou, L.; Shi, Y.; and Zhang, D. A statistical language modeling approach to online deception detection. IEEE Transactions on Knowledge and Data Engineering, 20, 8 (2008), 1077–1081.
