---
otero_id: 10150
otero_key: "DGRSYMH9"
title: "Using User- and Marketer-Generated Content for Box Office Revenue Prediction: Differences Between Microblogging and Third-Party Platforms"
authors: "Tingting Song; Jinghua Huang; Yong Tan; Yifan Yu"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0797"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [139.184.14.150] On: 06 March 2019, At: 03:38 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/DGRSYMH9/fulltext/images/fdf869979df6436e09992bc587c01e0f1deaf6b94fca08db1ac98bdbfaefff88.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Using User- and Marketer-Generated Content for Box Office Revenue Prediction: Differences Between Microblogging and Third-Party Platforms

Tingting Song, Jinghua Huang, \*, Yong Tan, Yifan Yu

To cite this article:

Tingting Song, Jinghua Huang,<sup>,</sup>\*, Yong Tan, Yifan Yu (2019) Using User- and Marketer-Generated Content for Box Office Revenue Prediction: Differences Between Microblogging and Third-Party Platforms. Information Systems Research

Published online in Articles in Advance 05 Mar 2019

https://doi.org/10.1287/isre.2018.0797

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Using User- and Marketer-Generated Content for Box Of<sup>fi</sup>ce Revenue Prediction: Differences Between Microblogging and Third-Party Platforms

Tingting Song,<sup>a</sup> Jinghua Huang,<sup>b,</sup>\* Yong Tan,<sup>c</sup> Yifan Yu<sup>b</sup>

<sup>a</sup> Antai College of Economics and Management, Shanghai Jiao Tong University, Shanghai 200030, China; <sup>b</sup> Research Center fo Contemporary Management, School of Economics and Management, Tsinghua University, Beijing 100084, China; <sup>c</sup> Michael G. Foster Schoo of Business, University of Washington, Seattle, Washington 98195

<sup>\*</sup> Corresponding author

Contact: songtt@sjtu.edu.cn, http://orcid.org/0000-0002-5079-5652 (TS); huangjh@sem.tsinghua.edu.cn, http://orcid.org/0000-0003-4344-7884 (JH); ytan@uw.edu, http://orcid.org/0000-0001-8087-3423 (YT); yuyf12@sem.tsinghua.edu.cn, http://orcid.org/0000-0002-8959-3169 (YY)

Received: January 7, 2016 Revised: November 21, 2016; November 6, 2017; March 16, 2018 Accepted: April 22, 2018 Published Online in Articles in Advance: March 5, 2019

https://doi.org/10.1287/isre.2018.0797

Copyright: © 2019 INFORMS

Abstract. In this research, we build a prediction model of movie box office revenue by empirically exploring its intricate relationships with user-generated content (UGC) as well as marketer-generated content (MGC) on a microblogging platform and UGC on a thirdparty platform. Our analyses are based on a panel vector autoregression (PVAR) model that is calibrated with a combination of data from Weibo (microblogging platform) and Douban! Movies (third party). Our empirical results show that microblogging UGC (MUGC) is a significant predictor of box office revenue and has stronger predictive power than UGC on Douban! Movies (DUGC). In addition, we find that the volume of enterprise microblogs (i.e., MGC) predicts box office revenue directly and also indirectly via MUGC, and MUGC thus exerts a partial mediating effect on the predictive relationship between the volume of enterprise microblogs and box office revenue. Finally, a prediction model of box office revenue using lagged box office revenue, MGC, MUGC, and DUGC is proposed, and its forecasting accuracy is found to outperform that of existing models. Managerial implications on utilizing social media for enterprises are provided.

History: Anindya Ghose, Senior Editor; Xiaoquan (Michael) Zhang, Associate Editor. Funding: Financial support from the MOE Project of the Key Research Institute of Humanity and Social Sciences at Universities [Grant 13JJD630008] is acknowledged. J. Huang acknowledges financial support from the National Natural Science Foundation of China [Grants 71272028 and 71490721].

Supplemental Material: The e-companion is available at https://doi.org/10.1287/isre.2018.0797.

Keywords: box of<sup>fi</sup>ce revenue • (enterprise) microblogging • social media • third-party platform • user-generated content • marketer-generated content • PVAR

## 1. Introduction

The proliferation of user-generated content (UGC) or online word-of-mouth (WOM) in the past decade has been shaping consumer attitudes and behaviors. Consumers seek UGC from various sources to learn product attributes and quality before making purchase decisions, particularly for experiential products such as movies (Liu 2006, Duan et al. 2008, Gu et al. 2012, Gopinath et al. 2013, Hennig-Thurau et al. 2015).

Established in 2005, Douban is one of the largest interest-oriented communities for book, music, and movie reviews. Douban is open to registered and unregistered users; unregistered users are those who only read content created by registered users. At the end of 2013, Douban had over 200 million unique visitors monthly, and the average daily page views were beyond 210 million.<sup>1</sup> In 2015, over 30% of Chinese Internet users accessed

Douban, making this platform a major magnet for Chinese film fans. On the basis of the page rankings of Alexa, Sogou, and Baidu, Chinese consumers traditionally obtain opinions or recommendations on movies from Douban! Movies of Douban.com. Douban! Movies is similar to Yahoo! Movies and IMDB and comprises a large collection of movie information such as the introduction, trailers screening schedules in all theaters, user comments, and ranking of movies. Users can write and read online reviews, create and view lists of their favorite movies, and purchase movie tickets at Douban! Movies. UGC on Douban! Movies (DUGC) may affect the adoption behaviors of consumers toward movies.

With the recent expansion of social broadcasting networks (Rui and Whinston 2011), Sina Weibo founded in 2009, is regarded as the most powerful microblogging platform and “Twitter in China.” As of December 2015,

Weibo had 222 million active users monthly.<sup>2</sup> Entertainment stars and movies are ranked as the first and second interesting topics on Sina Weibo, respectively. By learning of the hot topics about movies on Weibo, consumers may turn to Douban! Movies to read UGC. Consumers can also dig valuable or insightful DUGC and then share them on Weibo. These interactions not only change consumer behaviors but also influence movie sales. Weibo messages have become a new type of UGC, which can be called microblogging UGC (MUGC), and are rapidly changing the landscape of UGC. The adoption behaviors of consumers toward movies may also be affected by MUGC.

Weibo and Douban! Movies are significantly distinct in two aspects. First, the technical infrastructure of Weibo is relatively different from Douban! Movies. Weibo integrates social networks and broadcasting functions into its service. Microblogs are open to all users and broadcasted or pushed through direct subscription. The subscription relationship constitutes social networks, implying that the followers of a user subscribe and receive his or her Weibo messages and the followees of the user are the other users whose microblogs the user subscribes to (Shi et al. 2014). Through the social networks and broadcasting functions, Weibo triggers quick and extensive content sharing among users (Shi et al. 2014, Chen et al. 2015, Hennig-Thurau et al. 2015). By contrast, Douban! Movies is topic-centric. Consumers are likely to obtain DUGC by searching the title of a certain movie. Second, the role of the information sender varies; that is, the information may come from a user or an enterprise. The popularity of microblogging provides firms with new marketing opportunities and companies are gradually investing in creating their enterprise microblogging for branding, marketing, and customer services (Culnan et al. 2010, Hoffman and Fodor 2010, Goh et al. 2013). Specifically, many movie distributors in China provide their enterprise microblogging services on Weibo for marketing. Weibo integrates UGC and marketer-generated content (MGC), whereas Douban! Movies only comprises UGC. Considering the differences between Weibo and Douban! Movies, examining whether and how content from these two platforms affects the adoption behavior of consumers toward movies and consequently predicts movie box office revenue differently is interesting and important.

Academics have recognized the importance of online WOM or UGC, and many studies have examined how the volume and valence of online WOM affect the sales of books, music, movies, and digital products (Chevalier and Mayzlin 2006, Liu 2006, Dellarocas et al. 2007, Forman et al. 2008, Dhar and Chang 2009, Decker and Trusov 2010, Hu et al. 2010, Lee et al. 2011, Li 2011, Dewan and Ramaprasad 2012, Rui et al. 2013, Yu et al. 2013). Although these studies have compellingly established the significance of online WOM as predictor of product sales, they have only covered a single platform. In particular, if

MUGC offers useful predictive information that supplements UGC from third-party platforms, the combination of both data sources may yield more accurate sales predictions. This thus raises an important question that lies at the core of this research: Do and how do MUGC and DUGC predict box office revenue differently? Our second research question is whether enterprise microblogs (i.e., MGC) can predict product sales effectively. We acquire national daily movie box office revenue for each movie and obtain UGC data from Douban! Movies. Two types of messages on Weibo that are generated by different information senders (i.e., MUGC and MGC) are identified A panel vector autoregression (PVAR) model using the generalized method of moments (GMM) is employed for sales prediction.

The rest of this article is organized into several sections. The findings and limitations of previous literature are reviewed in Section 2. Section 3 describes the data that we use for the empirical analysis. In Section 4, we elaborate the research methodology, and the empirical results are presented in Section 5. Finally, we conclude by discussing the theoretical and practical implications of this study in Section 6.

## 2. Literature Review

## 2.1. The Predictive Power of Online User-Generated Content

Many studies in information systems and marketing have demonstrated that the valence and volume of online WOM from different online platforms, such as retailer hosted third party (e.g., Yahoo! Movies and IMDB), and blogging platforms, are shown to carry importance for predictions (e.g., Chevalier and Mayzlin 2006, Chintagunta et al. 2010, Onishi and Manchanda 2012). About the possible lag effect of online WOM, recent studies have shown that the valence or volume of prior period WOM can predict the future sales of products (Dellarocas et al. 2007, Dhar and Chang 2009, Archak et al. 2011). Other studies have further reported that product sales can also predict online WOM (Moon et al. 2010, Li 2011). The valence and volume of WOM are also interrelated. Duan et al. (2008) and Park et al. (2012) demonstrated a positive interaction between WOM valence and its own volume at retailer and thirdparty review websites.

With the increasing popularity of social media in recent years, tweets have become a new type of UGC and have demonstrated the effective predictor for sales (Rui et al. 2013, Hennig-Thurau et al. 2015). Hennig-Thurau et al. (2015) empirically reported user-generated tweets as an important factor in explaining box office revenue by immediately disseminating consumers postpurchase quality evaluations. Rui et al. (2013) used machine-learning algorithms, classified tweets into intention and nonintention tweets, and constructed measures for capturing the valence and volume of tweets. They indicated that positive (negative) valence of tweets is associated with high (low) box office revenue, and the volume of tweets as well as tweets expressing the intention of users to watch a certain movie exhibit their usefulness for predicting box office revenue. Although the literature is rapidly growing, few studies have taken the potential dynamic effect between Weibo messages (or tweets on Twitter) and sales into consideration, which may lead to the biased predictive results. In terms of the research on retweets (i.e., content diffusion), most studies have focused on the antecedents of content diffusion and found that retweets are motivated by user characteristics (e.g., Bakshy et al. 2011, Wu et al. 2011, Zhang et al. 2017, Lambrecht et al. 2018), content features (URLs and hashtags), contextual features (number of followers and followees and the age of the account) (e.g., Suh et al. 2010, Zhang et al. 2017), and social relationships (Shi et al. 2014). To the best of our knowledge, few studies have investigated the usefulness of rebroadcasts on Weibo (or retweets on Twitter) for predicting sales. These highlighted needs and the gap in the literature motivate our study.

## 2.2. Online User-Generated Content from Multiple Platforms

Given that consumers typically encounter WOM from multiple sources simultaneously, their decisions may be jointly affected by different types of WOM. Therefore, the predictive accuracy of product sales may be significantly improved when we take WOM from multiple sources into consideration. Marketing and information systems researchers have devoted substantial attention to the relative effectiveness of WOM from different platforms on product sales (e.g., Gu et al. 2012, Dewan and Ramaprasad 2014). Among these studies, some have compared the different effects of WOM from retailer-hosted platforms (e.g., Amazon) with that from third-party platforms (e.g., Yahoo! Movies, IMDB, and Epinions). Park et al. (2009) examined how WOM from Amazon and CNET.com affected the sales of digital cameras, and they revealed that the valence of third-party WOM (i.e., CNET.com) influences sales more than that of retailer-hosted WOM (i.e., Amazon). Gu et al. (2012) also compared WOM from Amazon with that from three external WOM websites (CNET, DpReview, and Epinions), and reported that third-party WOM significantly affects the sales of digital cameras, whereas retailer-hosted WOM does not exhibit the same effect. An explanation of why third-party WOM is useful in explaining (or predicting) future sales is offered by Gu et al. (2012), who suggest that prepurchase information searches of consumers differ markedly with product involvement and third-party WOM enjoys better reputation and recognition as well as offers greater depth and more insights than retailer-hosted WOM.

Other studies compared the different effects of WOM from social media with that from conventional media (e.g., newspapers, Google searches, and business magazines) and found that the former is more useful in explaining sales than the latter. Considering that UGC from social media platforms is often regarded credible and trustworthy, Yu et al. (2013) studied the effects of UGC from social media (blogs, forums, and Twitter) and conventional media (major newspapers, television broadcasting companies, and business magazines) on short-term firm stock market performances. They found that UGC from social media had a stronger relationship with firm stock performance than that from conventiona media. Dewan and Ramaprasad (2014) argued that new media are starting to displace conventional media in terms of the way consumers learn about products and services and how to consume them. They found that the negative effect of new media (Blog buzz) on song sales is greater than the positive effect of conventional media (radio play) because free online sampling dominates. Stephen and Galak (2012) also argued that the media landscape has dramatically changed with the rising of social media, and thus they compared the marketing effects of conventional and social media. They demonstrated that the effect of blogging (on a microlending platform) on transactions is significantly greater than that of conventional media, such as newspapers and magazines. Luo et al. (2013) suggested that managers should understand the relative effects of buzz and traffic on firm performance to balance their resources for digital marketing strategies. They examined social media-based metrics (web blogs and review valence on CNET) and conventional online behavioral metrics (Google searches and web traffic) and found that the latter exhibits a significant yet substantially weaker predictive relationship with firm equity value than the former.

To the best of our knowledge, the contrasts between social media data and third-party WOM have not been previously studied in the context of sales prediction. Gu et al. (2012) and Yu et al. (2013) suggested that content from third-party and social media platforms is credible and trustworthy, and moreover, unlike the largely different content consumption behaviors of consumers toward social media and conventional media platforms (Stephen and Galak 2012, Dewan and Ramaprasad 2014), how consumers learn about services and consume content from social media and third-party platforms is rather similar. Our study makes contributions by better understanding the predictive potential of third-party and social media data as the mechanisms or explanations of UGC from these two types of platforms for sales prediction are possibly different from those proposed in previous research.

## 2.3. The Predictive Power of Online Marketer-Generated Content

Firm-initiated social media remains a new phenomenon, which may also serve as an important factor in explaining or predicting sales. Researchers began to investigate the outcomes of firms adopting social media to generate content related to their brands or products and communicate with their customers. Tucker (2012) asserted that “social advertising” in Facebook based on social relationships of users effectively increases advertising clicks. Aral and Walker (2011) showed that firms can create social contagion on Facebook using viral features in marketing campaigns. Firm-hosted fan pages on Facebook open a new channel of communication through which customers can connect and communicate directly with the firm and other customers, increasing the frequency of customer visits to offline stores; this effect is enhanced with a high level of message postings (Rishika et al. 2013). Gong et al. (2017) conducted a field experiment on Weibo with a major global media company that produced documentary television (TV) shows and created its official microblogging account to post information about its shows. The experiment demonstrated that official Weibo messages of the company effectively increase its TV show viewing. Lee et al. (2018) further examined the effectiveness of different types of firm-generated content to provide valuable guidance on deploying content design strategies in social media. They found that informative content, such as the mention of deals and promotions, directly induces consumers’ click-throughs.

The purchase decisions of consumers are often influenced by UGC and MGC because of the simultaneous engagement of consumers and marketers on social media. Accordingly, product sales are expected to correspond to both UGC and MGC. Some studies have compared the effect of UGC with that of MGC (Albuquerque et al. 2012) and showed that UGC may be more relevant to consumers than MGC and is thus more useful in helping consumers to purchase their preferred products (Chen and Xie 2008). Goh et al. (2013) measured the effect of UGC and MGC on the apparel purchase expenditures of consumers. They found that firms engaging in Facebook brand communities increase consumers’ purchase expenditures and UGC exhibited a stronger effect on consumer purchase behavior than MGC. Gong et al. (2017) concluded that UGC (i.e., Weibo messages from influential users) is more effective than MGC (i.e., company’s own Weibo messages) in acquiring new followers of enterprise microblogging and increasing the company’s TV show viewing.

To our knowledge, previous studies have devoted substantial attention to the relative effectiveness of MGC and UGC on social media (Albuquerque et al. 2012, Goh et al. 2013, Gong et al. 2017). However, none of these studies have explored the interplay relationship between MGC and UGC and the usefulness of such relationship in predicting product sales.

## 3. Data Collection

## 3.1. Data Collection and Processing

The data collection procedure involves several steps. First, we select the movies to be included in the sample. We search for movies released in 2012 with complete national daily box office revenue information and obtain 156 movies. We delete 17 movies that lack DUGC information during their screening periods. Using the titles of 139 movies as keywords, we search the movies with certified enterprise microblogging accounts on Weibo. We subsequently obtain 60 movies as the sample. Second, we collect information on the 60 movies from www.cbooo.cn using a JAVA program, including their screening periods, national daily box office revenue, and screen ratio. Third, we crawl DUGC data of the 60 movies using a JAVA program and use the number and average ratings of daily reviews on Douban! Movies as the volume and valence of DUGC Overall, we obtain 358,980 DUGC of the 60 movies during the screening periods. Fourth, by obtaining the application programming interface access from Weibo, we capture the data of enterprise microblogs, including content and timestamp posted by the 60 movie distributors on their enterprise microblogging web page. We obtain 15,705 MGC of the 60 movies during the screening periods. Fifth, we use the movie titles and their screening periods as the search keywords to retrieve user microblogging information in the search engine of Weibo and use a crawler to download the information, including original microblogs created by users, rebroadcasting number of each original microblog, and users’ credentials of each original microblog. We delete users as well as their microblogs who are not verified by Weibo.com to avoid potential issues that some movie companies may employ Internet “water army” to post fake Weibo messages to boost box office revenue. We then obtain 258,665 user-generated microblogs of the 60 movies during the screening periods.

Then, we conduct a two-stage data processing suggested by Hennig-Thurau et al. (2015) to calculate the valence of each Weibo message of users. First, we conduct content classification to identify Weibo review messages by sorting 258,665 user-generated microblogs into one of the three following groups: (1) Weibo intention messages that express users’ intention to watch a certain movie in the future; (2) Weibo review messages which express users’ opinions after watching a certain movie; (3) spam and irrelevant Weibo messages, such as advertising (Hennig-Thurau et al. 2015). Second, we divide Weibo review messages into positive and negative reviews using the method of sentiment analysis.

Specifically, we conduct the following steps for content classification. First, the training set is labeled. Four coders, who were extensively trained for the task, manually coded 20,000 randomly selected Weibo messages and divided them into the three different groups mentioned above. Second, the features are extracted and selected. Using the Chinese word segmentation repository by Python, we use feature hashing method, also known as the hashing trick, to extract 15,000 Chinese word or word group features from 20,000 Weibo messages. Third, from 15,000 features, we select categorization features with the highest discriminatory power by measuring their chisquared statistics. Next, each Weibo message is assigned to a vector, which is mapped into the number of categorization features in dimensional space. Fourth, training classification model is employed. We train the algorithm of a support vector machine (SVM) model using the above training data set. We use cross-validation method to compare the results of SVM model with the manually coded results and derive the precision of SVM model, which is 87.59%. Finally, we use the derived SVM model to classify 258,665 Weibo messages and obtain 79,305 Weibo review messages.

We follow similar steps to conduct sentiment analysis on these 79,305 Weibo review messages. First, we manually coded 7,194 randomly selected Weibo review messages into positive or negative ones as our training set. Second, from the above mentioned 15,000 features, we select valence features that can separate positive and negative Weibo messages by measuring their chisquared statistics. Then, each Weibo review message is assigned to a vector, which is mapped into the number of valence features in dimensional space. Third, we train the SVM model with the training set data and follow the method proposed by Yang et al. (2016) to calculate its precision, recall and F1-score by 10-fold cross validation. The average precision, recall and F1-score of our SVM model are 94.83%, 95.19%, and 94.94%, respectively. This indicates that our model provides satisfactory performance on this sentiment analysis. Finally, we use the derived SVM model to analyze 79,305 Weibo review messages and identify whether they are positive or negative.

The overall performance of our SVM model for the sentiment analysis is much enhanced, possibly because of the following three reasons. First, we have filtered out spam and irrelevant Weibo messages as mentioned previously. This process helps to reduce noises in our training set. Second, according to Hennig-Thurau et al. (2015), our improved precision level may be a result of the brevity of Weibo messages. The average Weibo messages in our training set has 74.5 characters, with a 140-character limit of Sina Weibo. The brevity of Weibo messages could help to reduce the difficulty in accurate analysis of the message sentiment. Third, we adopt the strategy of adjusting penalty weights (also known as penalty parameter C of the error term in SVM model) for different sentiment classes to mitigate the unbalanced sample distribution problem of the training set (Luo et al. 2006), which also enhances the overall performance. We notice that our training set is unbalanced; that is, only 5.76% Weibo messages are labeled as negative ones. Because negative training samples are much less than positive ones, negative messages are more likely to be misclassified (Luo et al. 2006). To address this issue, we use different penalty weights for each class, namely, $C = 1 0 . 0$ for positive class and C = 50.0 for negative class, after parameter selection. In other words, we give more importance to negative messages so that we could better identify them. This strategy is suggested by Vapnik (1998), which is also implemented by the well-known machine learning tool Scikit-learn.<sup>3</sup>

## 3.2. Descriptive Statistics

We sort the preceding data set and obtain 1,441 records on the 60 movies. Table 1 summarizes descriptions and descriptive statistics of key variables for the 60 movies. Each movie has an average box office revenue of 18.9 million Renminbi (RMB), with 0.29 million RMB and 147 million RMB as the minimum and maximum revenues, respectively. The ratio of the opening-week box office revenue to the total box office revenue is above 60%. Each movie has been screened for an average of 26.68 days, with 12 days as the shortest screening time and 52 days as the longest. Using daily box office revenue as the dependent variable is more appropriate than using weekly box office revenue because the life span of movies is typically short. The daily average volume of MUGC is 51.29, with a minimum of 0 Weibo messages and a maximum of 444 Weibo messages. These movies have an average of 206.53 daily reviews in Douban! Movies, with a minimum of 0 reviews and a maximum of $^ { 3 , 7 1 0 }$ reviews, indicating that DUGC volume is larger than MUGC volume. Compared with MUGC volume, MGC volume is relatively limited with approximately 10 Weibo messages a day. The average rebroadcasting volume of MUGC is 101.46 per day, with some MUGC rebroadcasted 9,007 times, and other MUGC not rebroadcasted by any users. The sentiment of Douban reviews and that of Weibo messages on Weibo tend to be positive. The daily average valence of DUGC and MUGC is 5.59 and 0.74, respectively.

Table 1. Variables, Descriptions, and Summary Statistics of the Movie Sample

<table><tr><td>Variable</td><td>Description</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td> $AggBoxoffice_{it}$ </td><td>Aggregated box office revenue of movie i (RMB million)</td><td>18.9</td><td>29.5</td><td>0.29</td><td>147</td></tr><tr><td> $BoxOfficeRev_{it}$ </td><td>Box office revenue of movie i on day t (RMB million)</td><td>2.89</td><td>6.29</td><td>0.005</td><td>82.5</td></tr><tr><td> $WeiboVol_{it}$ </td><td>MUGC volume of movie i on day t</td><td>51.29</td><td>58.56</td><td>0</td><td>444</td></tr><tr><td> $WeiboVal_{it}$ </td><td>MUGC valence of movie i on day t</td><td>0.74</td><td>0.27</td><td>-1</td><td>1</td></tr><tr><td> $RWeiboVol_{it}$ </td><td>Rebroadcasting volume of MUGC for movie i on day t</td><td>101.46</td><td>460.60</td><td>0</td><td>9,007</td></tr><tr><td> $DoubanVol_{it}$ </td><td>DUGC volume of movie i on day t</td><td>206.53</td><td>408.36</td><td>0</td><td>3,710</td></tr><tr><td> $DoubanVal_{it}$ </td><td>DUGC valence of movie i on day t</td><td>5.59</td><td>1.52</td><td>1.33</td><td>9.74</td></tr><tr><td> $OfficialVol_{it}$ </td><td>MGC volume of movie i on day t</td><td>9.90</td><td>16.32</td><td>0</td><td>170</td></tr><tr><td> $Days_{i}$ </td><td>Screening days of movie i</td><td>26.68</td><td>8.50</td><td>12</td><td>52</td></tr></table>

## 4. Empirical Methodology

We present our model specification in Figure 1. The box office revenue, MUGC (DUGC) volume and valence, MGC volume, and rebroadcasting volume of MUGC tend to be correlated with one another. Each variable is endogenous and is a linear function of its own past values and the past values of all other variables.

We employ and estimate a PVAR model with exogenous variables and unobserved fixed individual effects to predict box office revenue. On the one hand, VAR models are especially well suited to measure dynamic interactions among variables, assuming that each dependent variable is a function of its own past values and the past values of all other dependent variables. On the other hand, the panel nature of the data can handle unobserved individual heterogeneity and utilize instruments within the model, such as lagged dependent variables in the estimation, to obtain consistent estimates (Love and Zicchino 2006, Dewan and Ramaprasad 2014, Chen et al. 2015). We specify the model as follows:<sup>4</sup>

$$
\begin{array}{c} \left( \begin{array}{c} L B o x O f f i c e R e v _ {i t} \\ L W e i b o V o l _ {i t} \\ W e i b o V a l _ {i t} \\ L R W e i b o V o l _ {i t} \\ L D o u b a n V o l _ {i t} \\ D o u b a n V a l _ {i t} \\ L O f f i c i a l V o l _ {i t} \end{array} \right) = \sum_ {j = 1} ^ {p} \Gamma_ {j} \cdot \left( \begin{array}{c} L B o x O f f i c e R e v _ {i t - j} \\ L W e i b o V o l _ {i t - j} \\ W e i b o V a l _ {i t - j} \\ L R W e i b o V o l _ {i t - j} \\ L D o u b a n V o l _ {i t - j} \\ D o u b a n V a l _ {i t - j} \\ L O f f i c i a l V o l _ {i t - j} \end{array} \right) \\ + \beta \cdot S c r e e n R a t i o _ {i t} + \eta \cdot A g e _ {i t} \\ + \gamma \cdot W e e k e n d _ {t} + \delta_ {t} + \mu_ {i} + \varepsilon_ {i t}, \end{array}\tag{1}
$$

where Γ are $7 \times 7$ matrices of slope coefficients for endogenous variables. The p value indicates the number of lags, which may be determined using Akaike’s information criterion (AIC) and Schwartz’s Bayesian information criterion (BIC). We make the log transformation of box office revenue, MUGC volume, rebroadcasting volume of MUGC, DUGC volume, and MGC volume. For example, $L B o x O f f i c e R e v _ { i t }$ is the log transformation of the daily box office revenue for movie i on day t. We consider three exogenous variables as follows. $A g e _ { i t }$ is the number of days movie i has been released on day $t ,$ and Weekend indicates if t falls in weekend (1 for Saturday, Sunday or holiday, and 0 otherwise) to control for the possible weekend and holiday effects. Moviegoers perceptions of a movie are affected by the other competing movies during the same releasing period (Ainslie et al. 2005, Chintagunta et al. 2010). Perceived quality of a movie over time may affect demand expectations held by the market, which directly determines the daily number of movie screening by profit-maximizing agents (theater owners) because the financial incentive motivates them to correctly predict consumer demand for a movie (Moretti 2011). Thus, we use screen ratio for movie i on day $: ( S c r e e n R a t i o _ { i t } )$ to measure the timevariant quality perceptions of movie i. The u value is a column vector of unobserved movie-specific effect characterizing the time-invariant attributes of movies, such as time-invariant advertising and genre of movies. The $\delta _ { t }$ value is a column vector of time dummies that control for any time effects, such as seasonality, and $\varepsilon _ { i t }$ is the mean zero error term.

Figure 1. Research Framework  
![](/api/attachments/DGRSYMH9/fulltext/images/07d0840edda0168e2c8590b2ffe3eb9a08beb46aca8ec071f4329140dceb2845.jpg)

## 5. Empirical Results

## 5.1. Model Identi<sup>fi</sup>cation

We estimate the PVAR model using the GMM estimator. To examine the stationarity of panel data set, we conduct the stationarity test (Wooldridge 2010) that includes unit-root and cointegrated tests. Stationarity implies that although an unexpected change in the endogenous variables in PVAR can induce fluctuations over time, the effects of such change ultimately dissipate. Then, the endogenous variables revert back to a deterministic pattern without a permanent regime shift. Given that our data are unbalanced, we use the Fisher-type tests for each variable. The stationary test results indicate that all of the variables are stationary. Subsequently, we carry out the lag selection procedure using the aforementioned criteria (AIC and BIC). The optimal lag length is 4 according to the trade-off among the two (Lütkepohl 1985).

Given that the fixed effects are correlated with the regressors because of the lagged values, we follow Love and Zicchino (2006) and employ the forward meandifferencing approach (the Helmert procedure), which removes the fixed effects by transforming all of the variables in the model into deviations from forward means, i.e., subtracting the mean of all future observations available for each movie day. This transformation preserves homoscedasticity and orthogonality between transformed variables and lagged regressors (Arellano and Bover 1995), enabling us to use the lagged regressors as instruments for the forward-differenced variables (Dewan and Ramaprasad 2014). The time fixed effects are removed by subtracting the mean value of each variable computed for each day (Chang and Zhang 2015).

## 5.2. Model Estimation

Table 2 presents the estimation results for the PVAR model, which shows the coefficients, standard errors, and significance levels of the seven endogenous and three exogenous control variables.

We examine the regression results using box office revenue as dependent variable. The MUGC volume on the third lag has a significant positive predictive relationship with box office revenue, whereas the DUGC volume does not predict box office revenue significantly. This result indicates that the MUGC volume explains more variance in the box office revenue than the DUGC volume. Although both the MUGC valence on the third lag and DUGC valence on the second lag significantly predict box office revenue, MUGC valence does not explain more variance in box office revenue than DUGC valence as demonstrated by the results of the t-test $( t = 1 . 1 0 ,  p > 0 . 1 )$ . MGC volume also has positive association with box office revenue. When the MUGC volume is the dependent variable (column 2 in Table 2), the enterprise microblogging volume on the first lag significantly predicts MUGC volume. Hence an unexpected increase in the volume of enterprise microblogging could predict a surge in MUGC volume.

Our results suggest that MUGC, DUGC, and MGC metrics add meaningful explanatory power for box office revenue prediction. MUGC metrics are comparatively stronger predictors for box office revenue than DUGC metrics. We also observe that although the rebroadcasting volume of MUGC does not predict box office revenue directly, its first and second lags exert significantly positive predictions on MGC volume, thereby predicting box office revenue indirectly. The screen ratio is also associated positively with box office revenue, and this outcome is in line with prior studies (Luo et al. 2013, Chen et al. 2015), thereby indicating that time-variant quality perceptions of a movie can positively predict consumer intentions to watch a movie.

## 5.3. Forecasting Accuracy

To test the forecasting accuracy of our model, we follow a k-fold cross-validation procedure, which is the common practice in predictive research (Efron and Tibshirani 1993). Specifically, we randomly divide our data set into five subsets<sup>5</sup> and then repeat the holdout method five times for our model. Each time, one of the five movie subsets is used as the test set, and the other four subsets are put together to form a training set. Alternatively, we can measure performance using a moving window approach (Geva et al. 2017). That is, for month t (t > 6), the preceding six months (months t – 6 to t – 1) are used as a training set and month t is used as the test set.

We use the mean absolute percentage error (MAPE) between the observed and predicted box office revenues on any given day as our performance criterion. LBoxOff iceRev , (i.e., the log transformation of the daily box office revenue for movie i on day t) is the observed box office revenue. As for the predicted box office revenue, we initially use the estimates (including endogenous and exogeneous values) in Table 2 to calculate the estimated revenue; and afterward, we derive the predicted revenue with a reversal of forward mean-differencing and time-demeaning value. Both the average MAPE of the fivefold cross-validation procedure and that of the moving window approach are 3.2%. The results of each test set for our model are reported in Table 3. Our forecasting accuracy results compare favorably with those reported by Liu (2006) and Dellarocas et al. (2007), who use similar crossvalidation procedures for WOM data from third-party platforms. The MAPE for the aggregate box office revenue of Liu (2006) is 47% and that for blockbuster movies’ box office revenue of Dellarocas et al. (2007) is 7%

Table 2. Model Estimation Results

<table><tr><td rowspan="2"></td><td colspan="7">Dependent variable</td></tr><tr><td> $LBoxOfficeRev_{it}$ </td><td> $LWeiboVol_{it}$ </td><td> $WeiboVal_{it}$ </td><td> $LRWeiboVol_{it}$ </td><td> $LDoubanVol_{it}$ </td><td> $DoubanVal_{it}$ </td><td> $LOfficialVol_{it}$ </td></tr><tr><td> $LBoxOfficeRev_{it-1}$ </td><td>0.778***(0.086)</td><td>0.142***(0.043)</td><td>-0.020(0.014)</td><td>0.108(0.090)</td><td>0.013(0.046)</td><td>0.130***(0.049)</td><td>-0.021(0.049)</td></tr><tr><td> $LBoxOfficeRev_{it-2}$ </td><td>0.109(0.068)</td><td>-0.083***(0.030)</td><td>0.004(0.012)</td><td>-0.066(0.072)</td><td>-0.046(0.035)</td><td>-0.015(0.038)</td><td>-0.024(0.037)</td></tr><tr><td> $LBoxOfficeRev_{it-3}$ </td><td>0.010(0.055)</td><td>0.019(0.031)</td><td>0.003(0.011)</td><td>-0.028(0.060)</td><td>0.039(0.037)</td><td>0.001(0.033)</td><td>0.002(0.034)</td></tr><tr><td> $LBoxOfficeRev_{it-4}$ </td><td>-0.002(0.055)</td><td>-0.025(0.025)</td><td>-0.005(0.008)</td><td>-0.046(0.044)</td><td>-0.012(0.035)</td><td>-0.014(0.024)</td><td>-0.018(0.031)</td></tr><tr><td> $LWeiboVol_{it-1}$ </td><td>-0.116(0.084)</td><td>0.276***(0.058)</td><td>0.036(0.025)</td><td>0.058(0.127)</td><td>-0.009(0.067)</td><td>0.117(0.072)</td><td>0.056(0.070)</td></tr><tr><td> $LWeiboVol_{it-2}$ </td><td>-0.020(0.066)</td><td>0.188***(0.045)</td><td>-0.009(0.019)</td><td>0.139(0.103)</td><td>-0.054(0.054)</td><td>0.018(0.062)</td><td>0.040(0.056)</td></tr><tr><td> $LWeiboVol_{it-3}$ </td><td>0.111**(0.051)</td><td>0.146***(0.037)</td><td>-0.000(0.017)</td><td>0.169*(0.090)</td><td>0.079*(0.046)</td><td>-0.002(0.053)</td><td>-0.009(0.047)</td></tr><tr><td> $LWeiboVol_{it-4}$ </td><td>-0.087(0.054)</td><td>-0.040(0.033)</td><td>0.031**(0.014)</td><td>-0.035(0.085)</td><td>-0.098**(0.044)</td><td>0.047(0.046)</td><td>-0.051(0.045)</td></tr><tr><td> $WeiboVal_{it-1}$ </td><td>0.183(0.169)</td><td>0.113(0.153)</td><td>0.014(0.078)</td><td>0.368(0.319)</td><td>0.020(0.149)</td><td>-0.077(0.201)</td><td>-0.274*(0.154)</td></tr><tr><td> $WeiboVal_{it-2}$ </td><td>0.225(0.153)</td><td>-0.024(0.133)</td><td>0.027(0.074)</td><td>0.125(0.281)</td><td>-0.165(0.138)</td><td>-0.022(0.186)</td><td>0.079(0.157)</td></tr><tr><td> $WeiboVal_{it-3}$ </td><td>0.305**(0.145)</td><td>0.222*(0.115)</td><td>0.110*(0.060)</td><td>-0.017(0.274)</td><td>0.352***(0.130)</td><td>0.071(0.163)</td><td>0.110(0.142)</td></tr><tr><td> $WeiboVal_{it-4}$ </td><td>0.087(0.152)</td><td>0.127(0.097)</td><td>0.037(0.060)</td><td>0.346(0.263)</td><td>-0.046(0.123)</td><td>-0.269*(0.140)</td><td>-0.004(0.133)</td></tr><tr><td> $LRWeiboVol_{it-1}$ </td><td>-0.021(0.021)</td><td>-0.000(0.018)</td><td>-0.005(0.009)</td><td>0.119***(0.044)</td><td>-0.019(0.020)</td><td>-0.018(0.023)</td><td>0.055***(0.020)</td></tr><tr><td> $LRWeiboVol_{it-2}$ </td><td>0.008(0.020)</td><td>0.018(0.014)</td><td>-0.012*(0.006)</td><td>0.096**(0.039)</td><td>0.025(0.019)</td><td>-0.015(0.019)</td><td>0.046**(0.020)</td></tr><tr><td> $LRWeiboVol_{it-3}$ </td><td>-0.019(0.020)</td><td>-0.008(0.016)</td><td>-0.011(0.007)</td><td>0.021(0.041)</td><td>0.006(0.018)</td><td>0.013(0.020)</td><td>-0.002(0.020)</td></tr><tr><td> $LRWeiboVol_{it-4}$ </td><td>-0.019(0.024)</td><td>0.015(0.015)</td><td>-0.009(0.006)</td><td>0.054(0.040)</td><td>0.013(0.020)</td><td>-0.024(0.020)</td><td>0.002(0.020)</td></tr><tr><td> $LDoubanVol_{it-1}$ </td><td>0.003(0.069)</td><td>0.077*(0.042)</td><td>0.018(0.015)</td><td>0.213**(0.101)</td><td>0.766***(0.050)</td><td>-0.089(0.057)</td><td>0.008(0.052)</td></tr><tr><td> $LDoubanVol_{it-2}$ </td><td>-0.058(0.060)</td><td>-0.029(0.037)</td><td>-0.011(0.016)</td><td>-0.114(0.094)</td><td>0.028(0.046)</td><td>-0.039(0.050)</td><td>-0.104**(0.048)</td></tr><tr><td> $LDoubanVol_{it-3}$ </td><td>0.043(0.054)</td><td>0.014(0.034)</td><td>0.023*(0.013)</td><td>0.032(0.081)</td><td>0.033(0.044)</td><td>0.041(0.044)</td><td>0.054(0.049)</td></tr><tr><td> $LDoubanVol_{it-4}$ </td><td>0.013(0.040)</td><td>-0.010(0.030)</td><td>-0.017(0.012)</td><td>-0.025(0.065)</td><td>0.014(0.035)</td><td>0.000(0.035)</td><td>0.039(0.036)</td></tr><tr><td> $DoubanVal_{it-1}$ </td><td>0.094(0.071)</td><td>0.072(0.051)</td><td>0.014(0.022)</td><td>0.093(0.127)</td><td>-0.001(0.060)</td><td>0.303***(0.073)</td><td>0.002(0.065)</td></tr><tr><td> $DoubanVal_{it-2}$ </td><td>0.091*(0.053)</td><td>0.085**(0.035)</td><td>0.024(0.015)</td><td>0.156*(0.087)</td><td>0.074(0.045)</td><td>0.145***(0.052)</td><td>0.012(0.045)</td></tr><tr><td> $DoubanVal_{it-3}$ </td><td>-0.020(0.040)</td><td>0.020(0.030)</td><td>-0.002(0.012)</td><td>-0.043(0.068)</td><td>0.037(0.034)</td><td>0.145***(0.042)</td><td>-0.014(0.041)</td></tr><tr><td> $DoubanVal_{it-4}$ </td><td>0.013(0.040)</td><td>0.028(0.029)</td><td>-0.004(0.013)</td><td>-0.016(0.074)</td><td>0.064*(0.033)</td><td>-0.033(0.051)</td><td>-0.003(0.038)</td></tr><tr><td> $LOfficialVol_{it-1}$ </td><td>0.093**(0.036)</td><td>0.063**(0.028)</td><td>0.004(0.012)</td><td>0.166**(0.072)</td><td>0.028(0.033)</td><td>-0.012(0.035)</td><td>0.458***(0.037)</td></tr><tr><td> $LOfficialVol_{it-2}$ </td><td>0.005(0.033)</td><td>-0.004(0.025)</td><td>-0.006(0.011)</td><td>-0.093(0.062)</td><td>0.039(0.033)</td><td>0.019(0.029)</td><td>0.167***(0.036)</td></tr><tr><td> $LOfficialVol_{it-3}$ </td><td>0.004(0.036)</td><td>0.022(0.024)</td><td>0.005(0.010)</td><td>0.082(0.057)</td><td>0.001(0.030)</td><td>-0.032(0.032)</td><td>0.073**(0.036)</td></tr><tr><td> $LOfficialVol_{it-4}$ </td><td>0.041(0.029)</td><td>-0.016(0.022)</td><td>-0.005(0.011)</td><td>0.065(0.057)</td><td>0.024(0.027)</td><td>-0.056*(0.030)</td><td>0.129***(0.031)</td></tr><tr><td> $ScreenRatio_{it}$ </td><td>12.093***(0.387)</td><td>5.475***(0.289)</td><td>-0.054(0.067)</td><td>6.450***(0.382)</td><td>7.624***(0.383)</td><td>3.377***(0.370)</td><td>1.709***(0.254)</td></tr><tr><td> $Age_{it}$ </td><td>-0.027***(0.005)</td><td>-0.014***(0.003)</td><td>0.000(0.001)</td><td>-0.046***(0.005)</td><td>-0.036***(0.005)</td><td>0.025***(0.004)</td><td>-0.083***(0.003)</td></tr><tr><td> $Weekend_t$ </td><td>0.489***(0.091)</td><td>0.262***(0.068)</td><td>-0.013(0.016)</td><td>0.063(0.089)</td><td>0.228**(0.090)</td><td>0.022(0.086)</td><td>-0.186***(0.059)</td></tr></table>

Notes. Variables are logged and forward mean differences.  
\*\*\*, \*\*, and \* denote significance at 1%, 5%, and 10%, respectively.

Appendix A in the e-companion lists the detailed MAPE for each of the 60 movies in our data set.

Figure 2 provides two illustrative examples of movies observed box office revenues and the corresponding predicted ones generated by our model. It is remarkable to observe that our model can correctly predict the general shape of these revenues and shows its effectiveness in predicting a movie’s box office revenue.

We further construct a parsimonious prediction model by including only the variables that significantly affect box office revenue in Table 2. The MAPE results are shown in Table 4 where the average MAPE of the fivefold cross-validation procedure and that of the moving window approach are 3.4% and 3.1%, respectively. This suggests that the performance of the parsimonious model does not differ significantly from that of the full model. In other words, when forecasting movie box office revenue, we only need to consider the values of box office revenue on the first lag, MGC on the first lag, MUGC on the third lag as well as DUGC rating on the second lag.

## 6. Discussion and Conclusions 6.1. Discussion

Our proposed model based on a combination of Weibo and third-party data can obtain more accurate box office revenue predictions compared with the models based on third-party data alone (Liu 2006, Dellarocas et al. 2007). MUGC is a leading indicator of box office revenue and has stronger predictive value than the conventional DUGC from the third-party platform. These findings conform to our expectations that transmission speed and scope of Weibo messages are faster and larger than those of DUGC on Douban! Movies. Moreover, MUGC exerts a partial mediating role in the predictive relationship between MGC volume and box office revenue because MGC volume is an effective predictor for both box office revenue and MUGC volume. The rebroadcasting volume of MUGC also predicts box office revenue indirectly via MGC volume. By using a more parsimonious model, we show that five variables (i.e., box office revenue on the first lag, MGC on the first lag, MUGC volume and valence on the third lag as well as DUGC rating on the second lag) are sufficient in predicting box office revenue accurately.

Table 2 shows that DUGC volume has an insignificantly predictive relationship with box office revenue. However, if we do not add Weibo sentiment and Douban ratings in the predictive model, DUGC volume positively predicts box office revenue. The main predictor of box office performance being the valence on third-party platforms rather than the volume is consistent with the finding of Chintagunta et al. (2010).

## 6.2. Contributions

This research contributes to the literature on UGC and the business value of social media. First, this study proposes a novel forecasting model, PVAR, which shows its effectiveness in predicting box office revenue. Our model outperforms traditional autoregressive model that does not consider the panel nature of the data to handle unobserved individual heterogeneity (Yu et al. 2012) and linear models that do not measure dynamic interactions among variables (Liu 2006, Asur and Huberman 2010).

Table 3. Forecasting Accuracy of the Model

<table><tr><td rowspan="2"></td><td colspan="5">Fivefold cross-validation procedure</td><td colspan="6">Moving window approach</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>MAPE</td><td>0.034</td><td>0.035</td><td>0.030</td><td>0.033</td><td>0.029</td><td>0.044</td><td>0.038</td><td>0.032</td><td>0.027</td><td>0.027</td><td>0.025</td></tr><tr><td>SD</td><td>0.027</td><td>0.023</td><td>0.026</td><td>0.014</td><td>0.015</td><td>0.023</td><td>0.016</td><td>0.013</td><td>0.003</td><td>0.007</td><td>0.008</td></tr></table>

Figure 2. Actual Versus Predicted Box Office Revenues for Two Illustrative Movies  
![](/api/attachments/DGRSYMH9/fulltext/images/45ecdb08fd631f4dcedbcca5abdacadb95affa23e2d1b5c4f9b7e4f6936182cb.jpg)

![](/api/attachments/DGRSYMH9/fulltext/images/2b71e71e6b81e24052c8ffafb24082737bd1ed5843ac46d3e28060ebb5b59673.jpg)  
----- Predicted Actual

Second, previous studies emphasize on the credibility and trustworthiness of third-party platforms (versus retailer-hosted platforms) (Gu et al. 2012) as well as the largely different content consumption behaviors of consumers toward social media and conventional media platforms (Stephen and Galak 2012, Dewan and Ramaprasad 2014). However, in the context of this study, the contents from these two types of platforms are credible and trustworthy (Yu et al. 2013), and how consumers learn about services and consume content from both platforms is rather similar. Therefore, the mechanism of how UGC from third-party and microblogging platforms affects box office revenue differs from that in previous studies. We deduce that content sharing with respective networks of users amplifies the new audience of the content to a possibly massive scale and at a quicker speed (Shi et al. 2014). The brevity of MUGC makes it more readable, helpful, and diagnostic than DUGC (Godes and Mayzlin 2009). MUGC with a hashtag may increase the possibilities of drawing other users’ attention and expanding the exposure of MUGC as well as awareness of a movie with unprecedented speed and scale (Kwon et al. 2012, Oh et al. 2015). All these reasons could result in stronger predictive power of MUGC volume than DUGC volume. We show that the forecasting accuracy of the model that combines traditional third-party and microblogging data outperforms that of forecasting models that only consider third-party data (Liu 2006, Dellarocas et al. 2007).

Third, this study contributes to better understanding of how rebroadcasting volume can add predictive value to box office revenue. Prior research on content diffusion has examined the factors that trigger content diffusion and methods on how to predict content diffusion effectively (Suh et al. 2010, Bakshy et al. 2011, Wu et al. 2011, Shi et al. 2014, Zhang et al. 2017, Lambrecht et al. 2018). Few studies have examined the potential power of rebroadcasts (i.e., content diffusion) in predicting box office revenue. This study finds that although rebroadcasting volume does not predict box office revenue directly, it can indirectly predict it via MGC because content rebroadcasted by many users can often attract the attention of consumers and trigger movie distributors’ involvement in similar content contribution so as to attract more consumers’ attention. Accordingly, compared with third-party platforms, rebroadcasting as one of the key distinct functions of microblogging platforms shows its usefulness in box office revenue prediction and cannot be ignored.

Fourth, unlike previous studies that focus mainly on the comparison of the relative effectiveness of MGC and UGC on social media (Albuquerque et al. 2012, Goh et al. 2013, Gong et al. 2017), the present study represents one of the few efforts to unveil the interplay between UGC and MGC on microblogging platforms. We reveal that sole reliance on UGC to explain box office revenue overlooks and omits the persuasive and advertising effects of MGC. MGC can predict box office revenue directly because enterprise microblogging by providing movie-related Weibo messages may transfer relevant content (Ackerloff 1970) or provide rich multimedia information (Cai et al. 2009) to potential consumers, thereby resolving consumers’ asymmetry to adopt a movie. MGC can also predict box office revenue indirectly via MUGC because followers of the enterprise microblogging are expected to be favorably disposed toward enterprise microblogging or the movie (Anderson and Sullivan 1993, Anderson 1998, Bowman and Narayandas 2001, Godes and Mayzlin 2009), thereby contributing movie-related Weibo messages voluntarily despite the lack of monetary return to seek reputational or structural embeddedness (Wasko and Faraj 2005). Therefore, we underscore that marketers can engage in enterprise microblogging by accentuating the role of MGC, thereby reaping increased business value from social media.

Table 4. Forecasting Accuracy of the Model with Only Significant Variables

<table><tr><td rowspan="2"></td><td colspan="5">Fivefold cross-validation procedure</td><td colspan="6">Moving window approach</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>MAPE</td><td>0.034</td><td>0.035</td><td>0.034</td><td>0.035</td><td>0.030</td><td>0.030</td><td>0.038</td><td>0.034</td><td>0.027</td><td>0.026</td><td>0.029</td></tr><tr><td>SD</td><td>0.027</td><td>0.022</td><td>0.027</td><td>0.016</td><td>0.023</td><td>0.023</td><td>0.014</td><td>0.017</td><td>0.003</td><td>0.007</td><td>0.001</td></tr></table>

## 6.3. Managerial Implications

The findings of this study provide several useful managerial implications. First, cinema operators may take advantage of our findings to increase the box office revenue of their movies by scheduling film screenings. Traditionally, cinema operators merely arrange film screenings based on their experiences or relationships with movie distributors (Eliashberg et al. 2006). However, such experiences are mostly ineffective because of the delayed responses from markets. Some films are very popular that their screenings are often sold out, whereas other films offer many screenings yet attract limited attendance. Cinema operators can consider previous volume and valence of MUGC before scheduling the current film screenings because these messages can quickly predict the future box office revenue of a movie. In this manner, cinema operators can increase the attendance rate of movies.

Second, movie distributors should optimize their online media strategy to improve their box office revenue. On the one hand, movie distributors can better allocate resources across microblogging platforms and conventional third-party platforms. To boost box office revenue, movie distributors should shift more resources to improving the volume and valence of their MUGC because they have relatively stronger predictive values. On the other hand, movie distributors can fully utilize enterprise microblogging to generate movie-related Weibo messages as MGC volume is capable of not only predicting box office revenue directly but also predicting MUGC volume, subsequently forecasting movie box office revenue indirectly. For example, Dragon Inn and The Four were distributed by the same distributor “Enlight Media Group.” The former and the latter contributed 53 and 266 enterprise microblogs, respectively, during their screening periods. The box office revenue of the former is only 6 million RMB, whereas the latter is over 195 million RMB.

## 6.4. Limitations and Future Research

Despite several significant findings, we acknowledge some limitations of this work. First, we only use 60 movies released in China in 2012 to conduct empirical analyses. Future research may incorporate additional samples into the analyses to increase the reliability and robustness of the results. Second, although fixed effects models enable us to control for the time-invariant at tributes of movies, such as genre of movies, different types of movies may present distinct trends. Future studies may consider how UGC and MGC of movies from different genres affect box office revenue differ ently. Third, unobserved time-varying features may be a concern to prevent us from making causal arguments. Future studies may try to find some exogenous shocks to conduct quasi-experimental designs. Fourth, the phenomenon of UGC and MGC is not unique to Weibo. Many other social media platforms (e.g., MySpace and Facebook) offer similar functions for marketers and consumers to engage in social interactions and can be examined to generalize our findings.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for constructive suggestions.

## Endnotes

<sup>1</sup> See http://www.wearesocial.com/. Accessed August 2016.

<sup>2</sup> See http://www.emarketer.com/Article/Weibo-Reaches-100-Million -Daily-Users/1013449. Accessed August 2016.

<sup>3</sup> See http://scikit-learn.org/stable/modules/svm.html. Accessed March 2018

<sup>4</sup> The extended model also accounts for post-release time-varian advertising data.

<sup>5</sup> The authors also attempted to divide the data set into 10 subsets as a robustness check and derived similar results.

## References

Ackerloff GA (1970) The market for “Lemons”: Quality uncertainty and the market mechanism. Quart. J. Econom. 84(3):488–500.

Ainslie A, Dreze X, Zufryden F (2005) Modeling movie lifecycles and market share. Marketing Sci. 24(3):508–517.

Albuquerque P, Pavlidis P, Chatow U, Chen K, Jamal Z, Koh K (2012) Evaluating promotional activities in an online two-sided market of user-generated content. Marketing Sci. 31(3):406–432

Anderson EW (1998) Customer satisfaction and word of mouth J. Service Res. 1(1):5–17.

Anderson EW, Sullivan MW (1993) The antecedents and conse quences of customer satisfaction for firms. Marketing Sci. 12(2): 125–143.

Aral S, Walker D (2011) Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Sci. 57(9):1623–1639.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Arellano M, Bover O (1995) Another look at the instrumental variable estimation of error-components models. J. Econometrics 68(1):29–51.

Asur S, Huberman BA (2010) Predicting the future with social media. Proc. IEEE/WIC/ACM Internat. Conf. Web Intelligence Intelligent Agent Tech. (IEEE, New York), 492–499

Bakshy E, Hofman JM, Mason WA, Watts DJ (2011) Everyone’s an influencer: Quantifying influence on Twitter. Proc. Fourth ACM Internat. Conf. Web Search Data Mining (ACM, New York), 65–74.

Bowman D, Narayandas D (2001) Managing customer-initiated contacts with manufacturers: The impact on share of category requirements and word-of-mouth behavior. J. Marketing Res. 38(3):291–297.

Cai H, Chen Y, Fang H (2009) Observational learning: Evidence from a randomized natural field experiment. Amer. Econom. Rev. 99(3): 864–882.

Chang X, Zhang HF (2015) Managerial entrenchment and firm value: A dynamic perspective. J. Financial Quant. Anal. 50(5):1083–1103.

Chen HL, Prabuddha D, Yu JH (2015) IT-enabled broadcasting in social media: An empirical study of artists’ activities and music sales. Inform. Systems Res. 26(3):513–531.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Sci. 54(3):477–491.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chintagunta PK, Gopinath S, Venkataraman S (2010) The effects of online user reviews on movie box office performance: Accounting for sequential rollout and aggregation across local markets. Marketing Sci. 29(5):944–957.

Culnan MJ, McHugh PJ, Zubillaga JI (2010) How large U.S. companies can use Twitter and other social media to gain business value. MIS Quart. Executive 9(4):243–259.

Decker R, Trusov M (2010) Estimating aggregate consumer preferences from online product reviews. Internat. J. Res. Marketing 27(4):293–307.

Dellarocas C, Zhang XM, Awad NF (2007) Exploring the value of online product reviews in forecasting sales: The case of motion pictures. J. Interactive Marketing 21(4):23–45.

Dewan S, Ramaprasad J (2012) Music blogging, online sampling, and the long tail. Inform. Systems Res. 23(3):1056–1067.

Dewan S, Ramaprasad J (2014) Social media, traditional media, and music sales. MIS Quart. 38(1):101–122.

Dhar V, Chang EA (2009) Does chatter matter? The impact of user generated content on music sales. J. Interactive Marketing 23(4): 300–307.

Duan W, Gu B, Whinston AB (2008) The dynamics of online word-ofmouth and product sales: An empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Efron B, Tibshirani RJ (1993) An Introduction to the Bootstrap (Chapman and Hall, Boca Raton, FL).

Eliashberg J, Elberse A, Leenders MA (2006) The motion picture industry: Critical issues in practice, current research, and new research directions. Marketing Sci. 25(6):638–661.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Geva T, Oestreichersinger G, Efron N, Shimshoni Y (2017) Using forum and search data for sales prediction of high-involvement projects. MIS Quart. 41(1):65–82.

Godes D, Mayzlin D (2009) Firm-created word of mouth communication: Evidence from a field test. Marketing Sci. 28(4): 721–739.

Goh KY, Heng CH, Lin Z (2013) Social media brand community and consumer behavior: Quantifying the relative impact of user- and marketer-generated content. Inform. Systems Res. 24(1):88–107.

Gong S, Zhang J, Zhao P, Jiang X (2017) Tweeting as a marketing tool: A field experiment in the TV industry. J. Marketing Res. 54(6):833–850.

Gopinath S, Chintagunta PK, Venkataraman S (2013) Blogs, advertising, and local-market movie box office performance. Man agement Sci. 59(12):2635–2654.

Gu B, Park J, Konana P (2012) The impact of external word-of-mouth sources on retailer sales of high-involvement products. Inform Systems Res. 23(1):182–196.

Hennig-Thurau T, Wiertz C, Feldhaus F (2015) Does Twitter matter? The impact of microblogging word of mouth on consumers adoption of new movies. J. Acad. Marketing Sci. 43(3):1–20.

Hoffman DL, Fodor M (2010) Can you measure the ROI of your social media marketing? MIT Sloan Management Rev. 52(1):43–50

Hu N, Liu L, Bose I (2010) Does sampling influence customers in online retailing of digital music? Inform. Systems E-Busines Management 8(4):357–377.

Kwon KH, Oh O, Agrawal M, Rao HR (2012) Audience gatekeeping in the Twitter service: An investigation of tweets about the 2009 Gaza conflict. Trans. Human-Computer Interaction 4(4):212–229.

Lambrecht A, Tucker C, Wiertz C (2018) Advertising to early trend propagators: Evidence from Twitter. Marketing Sci. 37(2): 177–199.

Lee D, Hosanagar K, Nair HS (2018) Advertising content and consumer engagement on social media: Evidence from Facebook. Management Sci. 64(11):5105–5131

Lee J, Lee JN, Shin H (2011) The long tail or the short tail: The category-specific impact of eWOM on sales distribution. Decision Support Systems 51(3):466–479.

Li Q (2011) Word-of-blog for movies: A predictor and an outcome of box office revenue? J. Electronic Commerce Res. 12(3):187–198.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box office revenue. J. Marketing 70(3):74–89.

Love I, Zicchino L (2006) Financial development and dynamic investment behavior: Evidence from panel VAR. Quart. Rev Econom. Finance. 46(2):190–210.

Luo LK, Peng H, Zhang QS, Lin CD (2006) A comparison of strategies for unbalance sample distribution in support vector machine. Proc. 2006 1st IEEE Conf. Indust. Electronics Appl. (IEEE, New York), 1–5.

Luo X, Zhang J, Duan W (2013) Social media and firm equity value Inform. Systems Res. 24(1):146–163.

Lütkepohl H (1985) Comparison of criteria for estimating the order of a vector autoregressive process. J. Time Series Anal. 6(1):35–52.

Moon S, Bergey PK, Iacobucci D (2010) Dynamic effects among movie ratings, movie revenues, and viewer satisfaction. J. Marketing 74(1):108–121.

Moretti E (2011) Social learning and peer effects in consumption: Evidence from movie sales. Rev. Econom. Stud. 78(1):356–393.

Oh O, Eom CY, Rao HR (2015) Role of social media in social change: An analysis of collective sense-making during the 2011 Egypt revolution. Inform. Systems Res. 26(1):210–223.

Onishi H, Manchanda P (2012) Marketing activity, blogging and sales. Internat. J. Res. Marketing 29(3):221–234

Park JH, Gu B, Konana P (2009) Impact of multiple word of mouth sources on retail sales. Proc. Internat. Conf. Inform. Systems, Phoenix.

Park JH, Gu B, Lee HY (2012) The relationship between retailer hosted and third-party hosted WOM sources and their influence on retailer sales. Electronic Commerce Res. Appl. 11(3):253–261.

Rishika R, Kumar A, Janakiraman R, Bezawada R (2013) The effect of customers’ social media participation on customer visit frequency and profitability: An empirical investigation. Inform. Systems Res 24(1):108–127.

Rui H, Whinston AB (2011) Designing a social-broadcasting-based business intelligence system. ACM Trans. Management Inform. Systems 2(4): 22:1–22:19.

Rui H, Liu Y, Whinston AB (2013) Whose and what chatter matters? The effect of tweets on movie sales. Decision Support System 55(4):863–870.

Shi Z, Rui H, Whinston AB (2014) Content sharing in a social broadcasting environment: Evidence from Twitter. MIS Quart. 38(1):123–142.

Stephen A, Galak J (2012) The effects of traditional and social earned media on sales: A study of a microlending marketplace. J. Marketing Res. 49(5):624–639.

Suh B, Hong L, Pirolli P, Chi EH (2010) Want to be retweeted? Large scale analytics on factors impacting retweet in Twitter network. Proc. 2010 IEEE Second Internat. Conf. Social Comput. (IEEE, New York), 177–184.

Tucker C (2012) Social advertising. Working paper, MIT University, Cambridge, MA.

Vapnik VN (1998) Statistical Learning Theory (John Wiley & Sons, New York).

Wasko M, Faraj S (2005) Why should I share? Examining social capital and knowledge contribution in electronic networks of practice. MIS Quart. 29(1):35–57.

Wooldridge JM (2010) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge, MA).

Wu S, Hofman JM, Mason WA, Watts DJ (2011) Who says what to whom on Twitter. Proc. 20th Internat. World Wide Web Conf. (ACM, New York), 705–714.

Yang X, Zhang Z, Zhang Z, Mo Y, Li L, Li Y (2016) Automatic construction and global optimization of a multi-sentiment lex icon. Comput. Intelligence Neurosci. 2016(5):1–8.

Yu X, Liu Y, Huang JX, An A (2012) Mining online reviews fo predicting sales performance: A case study in the movie domain. IEEE Trans. Knowledge Data Engrg. 24(4):720–734.

Yu Y, Duan W, Cao Q (2013) The impact of social and conventional media on firm equity value: A sentiment analysis approach. Decision Support Systems 55(4):919–926

Zhang Y, Moe WW, Schweidel DA (2017) Modeling the role of message content and influencers in social media rebroadcasting. Internat. J. Res. Marketing 34(1):100–119.
