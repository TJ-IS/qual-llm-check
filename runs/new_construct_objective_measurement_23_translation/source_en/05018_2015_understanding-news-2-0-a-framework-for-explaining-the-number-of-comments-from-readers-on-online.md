---
otero_id: 5018
otero_key: "N48FMMX2"
title: "Understanding News 2.0: A framework for explaining the number of comments from readers on online news"
authors: "Qian Liu; Mi Zhou; Xin Zhao"
year: "2015"
journal: "Information & Management"
doi: "10.1016/j.im.2015.01.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Understanding News 2.0: a Framework for Explaining the Number of Comments from Readers on Online News

Author: Qian Liu Mi Zhou Xin Zhao

![](/api/attachments/N48FMMX2/fulltext/images/d030b12aefafaf3499fcc5c959d1bb024454928007a637588ea2905f78be295a.jpg)

PII: S0378-7206(15)00003-8

DOI: http://dx.doi.org/doi:10.1016/j.im.2015.01.002

Reference: INFMAN 2784

To appear in: INFMAN

Received date: 31-8-2014

Revised date: 9-12-2014

Accepted date: 6-1-2015

Please cite this article as: Q. Liu, M. Zhou, X. Zhao, Understanding News 2.0: a Framework for Explaining the Number of Comments from Readers on Online News, Information and Management (2015), http://dx.doi.org/10.1016/j.im.2015.01.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

## Highlights

·The framework integrates news structure, content, and social media recommendation to explain the number of comments.

·Social media recommendation plays a relatively more important role than structural and content features.

·We explore a mediation model of recommendation in social media to explain the number of comments

·We also conceptualized new content features of online news articles.

# Understanding News 2.0: a Framework for Explaining the Number of Comments from Readers on Online News

Abstract: In the era of News 2.0, the number of comments can indicate the influence of online news, which brings potential social value and economic benefits. The present study proposes a framework that involves integrating the features of news structure, news content, and reader usage (social media recommendation) to explain the number of comments. The results of logistic regression suggest that the proposed framework is a powerful tool for explaining the number of comments $( \mathrm { R } ^ { 2 } { = } 4 7 . 1 \% )$ . The relative and mediating role of recommendation in social media from readers is also explored. The theoretical and managerial implications of these results are provided.

Keywords: News 2.0, reader comments, social media recommendation, content features, structural features.

## Acknowledgements

This paper was supported by two fund projects.

1. National Natural Science Foundation of China (Grant No. 71072129) Title: The Integrated Model and Empirical Study on EKRs continuance use

2. National Natural Science Foundation of China (Grant No. 71402136)

Title: Research on Knowledge Transfer between Professional Virtual Communities and Electronic Knowledge Repositories: Based on Big Data and User Behaviors Perspective

## Understanding News 2.0: a Framework for Explaining the Number of Comments from Readers on Online News

## 1. Introduction

News 2.0, which refers to news websites making use of Web 2.0-related technologies to encourage user participation, is embodied in user-generated content and user-to-user interaction [1]. To obtain great social value and economic benefits, News 2.0 websites enhance the popularity of online news and encourage users to comment on online news [67]. Different from traditional news platforms, which only contain input from journalists, comment pages of News 2.0 websites facilitate the aggregation of considerable user contributed information and opinion [26] in online news. Tsagkias et al. [66,68] suggest that the number of user supplied comments in a news article may be indicative of the importance, gathering on the comment webpage indicate the potential advertising value for news organizations and companies [40]. Furthermore, un traditional news readers, News 2.0 readers are not only news receivers and consumers, but also active participants of news writing, comments [26,67], and recommendations [46]. Reader recommendation have been rapidly growing in the online news sites and will help news organizations attract the attention of social media users [32,73]. A survey found that 37% of Internet users disseminate news content via postings on social media sites, such as Facebook and Twitter [58]. In the era of News 2.0, few studies have discussed the relationship among online news features, reader recommendation, and the number of online news comments, despite the tremendous changes that the goals of news organizations and the role of the readers have undergone.

Previous research on online news comments focused on predicting the development trend of comments, but did not explain the reasons for the different numbers of comments that news receives. Previous research assumed that past popularity is an effective predictor of future popularity [28]. Tsagkias et al. [68] examined the feasibility of predicting the total number of comments based on that observed shortly after publication. This technique requires historical data, which are difficult for third parties to obtain in practice. Previous research also

#

attempted to explore the factors that affected the number of online news comments. Abdul-Mageed [1] explored the relationship between four features of an online news article and commenting frequency. Tsagkias et al. [67] suggested that five feature sets influence the number of comments that a news article receives. This research is not only helpful in understanding how and why comments arise, but may also be useful in deriving practical guidelines to encourage readers in expressing opinions. However, features of online news, which prior research have considered, are limited and incomplete. New research should introduce more features from the perspective of online news content and the recommendation of readers, which previous research has ignored. Moreover, new research should further examine the relationship between the types of features to explain online news comments at a higher level.

The present study aims to explain the number of comments in online news articles. We seek to answer the question: What factors influence the number of online news comments? Specifically, we first introduced the structure, content, and usage features to form the framework that will answer the said question. We extracted the content features from an online news article through content analysis. Then, we tested the proposed framework using logistic regression method. In addition, we explored the superiority of recommendations in social media (usage features) over structure and content features in explaining the number of comments. We further explored the mediation effect of recommendations on social media for structure and content features to explain the number of comments.

We proposed a framework for explaining the extent of comments from readers, which has efficiently integrated the three feature groups (structure features, content features, and usage features) of online news attributes and reader recommendations. Overall, the contributions of this research are as follows: First, we developed recommendation in social media as a usage feature and investigated the relative role of this feature with other features to explain online news comments. Second, we explored a mediation model of recommendation in social media to explain the number of comments based on the research framework and analysis results. Third, we also conceptualized six content features of online news articles, which generalize the content attributes of online news.

In the next section, we introduce the background of News 2.0 and the related literature of online news comments. We then develop our research framework. Afterward, the research methodology is introduced and data analysis results are discussed. Finally, limitations and future research possibilities are suggested.

## 2. Background and Related Work

## 2.1 Background

The era of News 2.0 has arrived, with online news shifting from the traditional one-to-many communication model to a two-way, interactive pattern [56]. On one hand, news websites integrate with e-mails, BBS/forums, microblogs and other Web 2.0-related technologies to encourage user participation [11]. On the other hand, online readers rank, comment, and discuss the news, and react actively to online news. These changes have elicited considerable research interest [13,17,30,55,65]. Furthermore, scholars have argued that user-generated content and interactions are the core elements for this shifting [1]. Abdul-Mageed [1] defines News 2.0 refer as news websites that use Web 2.0-related technologies to encourage user participation, which is embodied in user-generated content and user-to-user interactions, a method that is fundamentally different from the previous journalism dogma, ―we write, you read‖ [16].

A news comment of a user is a typical form of user participation and interaction, producing unique content that is different from the news itself. Generally, a comment provides a response of a user/reader to a news item, expressing sentiment/opinion, a question, a rumor, or a call to action [41]. In terms of form, comments are usually short, unstructured, and with many irregular and informal sentences. Last, online news comments are sometimes implicit [48].

As the complement of traditional news, comments can attract additional readers, and create more business value and social influence. In the view of participatory journalism, News 2.0 gives ordinary people an opportunity to participate in professional online news editing and create more news-related content [29]. In China, NetEase news, which is known as ―news with attitude‖, highlights reader comments. News comments, as an extension of online news, give insight to popular opinions or feelings toward a given piece of news [68]. These comments, which accompany the news itself, may foster more browsing [23] and discussions [7,48]. News websites with large numbers of comments will certainly attract more concerns from merchants, companies, and advertisements [62,64]. Online news comments provide a space for expressing public opinion [26,50]. Furthermore, online news comments also play an important role in opinion analysis [48,59]. Moreover, the information embedded in news comments can be extracted as references for policy-making [33] and public management [48,69].

## 2.2 Related works

Previous research has explored the features from respective news structures to explain the number of comments as the antecedent. Abdul-Mageed [1] explored the relationship between three structure features of online news (position of story, days of the week, and regional coverage) and the frequency of commenting on news sites through the example of AL Jazeera. Tsagkias et al. [67] predicted the number of news article comments prior to publication using cumulative features (i.e., published articles in same hour for source), textual features (features of the top-100 terms that are ranked by the log-likelihood score of each source), and semantic features (i.e., number of location-type entities). Moreover, prior research has revealed that structure features play a key role in the popularity of user-generate content (UGC) (more research examples are shown in Appendix A). All these structure features can provide references for the study of online news comments, i.e., release time, source, regional information, UGC length, and so on.

Previous research ignored the influence of news content features on the number of online news comments. Abdul-Mageed [1] introduced the thematic category contrast based on news topics (including politics, military and political violence, foreign relations, religion, culture, economics, and disaster) to predict the frequency of comments on news sites through the example of AL Jazeera. News research should extract deep attributes of online news content because thematic category is the most superficial distinction of a news article. Moreover, several works have addressed the problem of predicting UGC popularity through deriving features of textual content features (Appendix B). Finch [25] conducted an exploratory study on the detailed description of customer messages on Internet discussions, which were read and categorized according to three subjective criteria (purpose, tone, and kano). Gupta et al.

[27] provided a variety of event features or an event category, which can be used to estimate the popularity trend of events in micro-blog platforms. Bandari et al. [8] constructed a multi-dimensional feature (category score and subjectivity) space derived from properties of an article, which evaluated the efficacy of these features and served as predictors of online news popularity on Twitter. To predict the popularity of UGC, Carmel et al. [12] studied three predict UGC popularity and demonstrated how the novelty of newly published content plays an important role in affecting popularity by predicting the number of comments. Zhang et al. [74] considered that the topic of tweets and affective degree of tweets influence the popularity of tweets. Based on the above review, prior research on online news comments, which does include the thematic category construct, did not consider the effect of other online news content features at a higher level. This effect has been identified as validation in the UGC context. New research should explore the relationship between news content and the number of comments in online news sites.

The relationship between news and social media has become an area of significant research interest [66], however, no normative research on the effect of social media on online news comments has been conducted. For example, Mccreadie and Macdonald [52] investigated that the blogosphere, as a prime evidence source, could automatically have the same rank as the news article. Tsagkias et al [66] concluded that the internal document structure of a news article can help retrieve implicitly linked social media utterances. Hong [32] suggested that the social media adoption of newspapers is positively associated with an increase in online readership, and this association increases with the size of the newspapers’ social media networks (e.g., number of Twitter followers). New research should investigate whether the extent of reader recommendation within social media can make a difference on online news comments. To the best of our knowledge, this aspect has not been researched sufficiently and should be further investigated.

## 3. A Framework for Explaining the Number of Comments of Online News

## 3.1 Theoretical Foundations

News is a kind of information or knowledge for readers and news browsing is a procedure of information/knowledge processing. Educational psychologists Jonassen, Beissner, and Yacci (1993) maintained that information or knowledge can be simply divided into two categories: content and structure [36]. Previous research on information/knowledge adopted the content and structure division method to investigate various information/knowledge, for example, information from the Electronic Data Gathering, Analysis, and Retrieval System (EDGAR) [14], XML documents [31], web documents [21], hypertext [71], public affairs knowledge [19], top managers’ strategic knowledge [37], etc. This division method is the basic foundation of the present research framework. To construct the framework for explaining the number of comments of online news, two features should be taken into consideration, that is, content and structure of news.

With the arrival of News 2.0 era, news websites have effectively linked with social media, which provides a barrier-free way for readers to transfer between the two platforms [58]. For the strong information transmission effect of social media [32], readers’ recommendation of news on social media, which is the leading usage feature, can affect the degree of concerns on the news. The present research framework concerning about the recommendation effect of social media not only corresponds to the development tendency of practice, but also expand the theoretical basis of previous research.

Beyond the previous research, the present study proposes a new framework (see Fig. 1), that adopts online news features and reader recommendation in social media to interpret the variance of number of comments. This framework includes three groups of variables, which are reader comments, usage features and online news features. The third group of variables can be further divided into structure features and content features.

## 3.2 Reader’s comments: the number of online news comments

The comment number refers to how many users have commented on a news item. Number of user comments is an important indicator for popular concerns and participations of a particular piece of online news [67]. A large number of comments mean a wide range of social influence. These news pages may attract more commercial advertisements, and bring tangible benefits to news websites [62,64]. Thus, number of comments is significant for online news websites.

The present study aims to enhance the understanding of comment number changes among different news. Specifically, the present study aims to identify the reasons for some online news receiving more reader comments than others. Both news stories and readers are indispensable factors for online news comments. News can be considered raw materials and readers can act as information processors [18]. Readers access the news, process the news information, then generate new thoughts and individual comments about this piece of news [43]. Therefore, this framework focuses more on online news features that may affect the information processing of readers to explain the variance of comments number among different news. Besides, as a kind of information, the features of online news can be divided into two aspects, i.e. structure and content, which have a direct effect on the number of comments.

![](/api/attachments/N48FMMX2/fulltext/images/e3c4793c44944c2622844939ccb0d6071d284e92b736ec403725c95234427be7.jpg)  
Figure 1. The framework explaining the number of online news comments

## 3.3 Usage features: Recommendations on social media

Recommendations on social media refer to the extent to which readers recommend news on the third-party social media, which promotes the dissemination and discussion of online news. Recently, social media has become more influential, accompanied with an ever-increasing business value [20]. Companies of the information industry hope to establish connections

#

with social media for the promotion their own development, and online news websites are no exception [32]. In fact, many websites have built a green channel connecting their own online news websites to their own social media platforms，which allows users to easily share online news in social media. In addition, news websites provide the social media links of other network operators. The effective connection between news websites and social media provides a convenient and easy way for readers to transfer between the two platforms. Effective information transmission [32,75] and aggregation effect on people with common interests of social media [47,70] improve the possibility of concerns about the news [32,52,66]. In addition, in the era of News 2.0, readers are not only consumers, but also active spreaders and commentators of news [26,67]. The role shift of readers makes them play a key role in news transmission. Thus, social media recommendations cannot be ignored in the present research.

In this framework, reader recommendation has multiple roles. Both text and content attributes of online news can make readers share news or news links on social media profiles. Recommendations on social media increase the number of online news transmission channels, allowing the news to become more accessible to potential readers [45]. Access is the premise and foundation of the information process; more access may lead to more reader comments. readers and commentators compared with traditional online news websites. Recommenders and their friends or followers have certain similarities [51]. In other words, friends of recommenders are more interested in browsing and commenting on recommended online news compared with average readers. Furthermore, a few words attached to news recommendation provide clues about the news, which can inspire other readers to generate new thoughts or comments. Consequently, active recommendation from readers on social media will increase the number of comments of the news to a great degree.

## 3.4 Online news features

## 3.4.1 Structural features

Structural features, such as news release time, pictures, the number of words, videos, summaries, headlines with locational information, and locations of news events, describe the objective features of online news text. Overall, we assume that the group of structural variables influences readers to share news or news links on social media profiles and post comments on online news websites. Structure of the text is a carrier that conveys news and information to readers, inevitably influencing reader’s recommendations and comments. As discussed in 2.2, structural variables were tested in many empirical studies on online news popularity. For example, Zhang et al. [74] examined the length of tweets and tweeting time that contribute to the popularity of tweets, number of re-tweeting and number of comments. Relatively, researchers can easily observe such variables and assign values to them.

## 3.4.2 Content features

Content features concentrate on the attributes of online news content. Content, as the object of user comments accounts for the comment number of online news. In this group, the features of subjective opinion [1,6], positiveness/negativeness [6,8], which were proposed in previous research, are refined. Furthermore, we propose utilizing the other six variables, namely controversial news, serial news, news referring to the future, life-related news, private matters, and peculiarities, to obtain a comprehensive view of news content attributes (Table 3). Former empirical studies, which relied on superficial classifications [1,67], rarely focused on generalizing the content attributes of online news. In contrast with the thematic categories of news，this present study extracts deep attributes of online news content to understand user comments.

On the whole, we assume that the group of content variables influences the social media recommendation and the number of news comments. In systematic mode of information processing, individuals’ decisions toward messages are affected by contents implied in the message [60]. The content of news articles catches attentions from readers and makes them read and think about the news, which further induces readers’ comments or recommendation of the news on social media. Bandari et al. [8] examined that an article written in a more emotional, more personal, and more subjective voice can resonate stronger with the readers, which could further improve the popularity of tweets.

## 4. Research Methodology

## 4.1 Backgrounds of the online news

Our study explains the number of online news comments on NetEase News (http://news.163.com/), which is one of the largest online news sites in China. NetEase News aims to create a ―news portal with attitude‖ and encourages users to comment on the news. NetEase can bring users the timeliest updated news and the most fluent news display. On July 9, 2013, users of NetEase News exceeded 120 million and active users reached 40 million in a day [53].

In the News 2.0 era, besides browsing news and commenting on news, users can also recommend news. The news that a number of users recommend are shown on the home page of JianXinWen, which is a website that NetEase established by to collect recommended news. In addition, NetEase News cooperates with third party party media sites, which permit users to create a newsfeed on social media. Four third-party media sites are used, including: NetEase Microblog and JianXinWen, which are owned by NetEase; and Sina Microblog and Q-zone , which are the social media of other organizations.

## 4.2 Data collection

Data collection involved two rounds. The purpose of round one was to gather online news articles. We used four different online news data sets to obtain generalizable insights on the popularity of online news: (1) social news, (2) entertainment news, (3) SciTech news, (4) and financial news, which have received widespread concern from the public. Two of the authors and two graduate students who were familiar with the data collection approach from personal experience, collected 2008 pieces of online news articles. Each was responsible for one news data set. From June 9 to June 15, 2014, news articles were collected from the ranking list of NetEase news every day. The variables of structure features, news release time, pictures, the number of words, videos, summaries, headlines with locational information, and locations of news events, which are the objective data of an online news article, was also recorded.

In round two, the number of comments and the recommendations on social media were collected. Tatar et al. [63] observed that the majority of news articles receive all comments within the first day after publication. For insurance purposes, we collected the number of comments from June 23 to June 30, 2014, which was approximately one week (seven days) after data collection of round one. Concurrently, we began data collection by keywords including ―the title of online news‖ and ―NetEase‖ on Sina microblog, NetEase microblog, and Q-space. Two authors and two graduate students read through all the microblogs to collect the number of forwards and remove irrelevant microblogs. Then, the number of recommendations from JianXinWen was collected.

## 4.3 Variables and operationalization

Three groups of features were considered: structural features, content features, and usage features, for the dependent variable, which is, the number of comments. Table 3 summarizes all features.

Dependent variable. ―The number of comments‖ refers to how many users have commented on a news item. This is a continuous variable as well, which is operationalized by ―the number of the follow-up comments‖ shown on the page of NetEase News.

Usage features. ―Social media recommendation‖ refers to the extent to which a reader recommends news on third-party social media. This continuous variable is operationalized through four social media: NetEase Microblog, Sina Microblog, Q-zone, and Recommended News. The present study adds the number of times the news item is forwarded in the four media platforms to present the total promotional effect of a news item.

Structural features. ―News release time‖, a nominal variable, refers the time when a news item is released. According to ―the release time‖ on the NetEase News page, the present study divides online news into four categories: from 7 am to 12 pm o’clock is marked as 1, 12 pm to 5 pm as 2, 5 pm to 10 pm as 3, and 10 pm to 7 am as 4. ―Picture‖ refers to the number of pictures involved in a news item. ―The number of words‖ refers to the number of Chinese characters involved in a news text. The present study adopts a text statistical software to count the number of words. ―Video‖ refers to the number of videos involved in a news item. ―Picture‖, ―the number of words‖, and ―video‖ are continuous variables. ―Summary‖ refers to information that presents or summarizes the main idea of a news item at the beginning of the news text. ―Headline with locational information‖ refers to the explicit location information in the headline of a news item. ―Location of news event‖ refers to where a news event happened. The present study divides the location into three categories: regional, inland, and overseas, which includes Hong Kong, Macao, and Taiwan. ―Summary‖, ―headline with locational information‖ and ―location of news event‖ are classified variables.

Content features. Variables related to the content are coded in the news text, which will be explained in detail (4.4).

Table 3. All variables and operationalization

<table><tr><td>Variable</td><td>Definition</td><td>Operationalization</td><td>Data type</td></tr><tr><td>The number of comments (DV)</td><td>How many users have commented on a news item.</td><td>the number of the follow-up comments” showed on the page of NetEase News</td><td>Con</td></tr><tr><td colspan="4">Usage features</td></tr><tr><td>Social media Recommendation (MV)</td><td>The extent to which reader recommend news on the third-party social media.</td><td>Adds up times of the forwarded news item on the four media platform (NetEase weibo; Sina weibo; Tencent space; Recommended news).</td><td>Con</td></tr><tr><td colspan="4">Structural features</td></tr><tr><td>News release time (IV)</td><td>The time that a news item is released</td><td>1 (7:00-12:00); 2 (12:00-17:00); 3 (17:00-22:00); 4 (22:00-7:00)</td><td>Cat</td></tr><tr><td>Pictures (IV)</td><td>The number of pictures involved in a news item</td><td>The number of pictures</td><td>Con</td></tr><tr><td>The number of words (IV)</td><td>the number of Chinese characters involved in a news text</td><td>The number of words</td><td>Con</td></tr><tr><td>Video (IV)</td><td>The number of videos involved in a news item</td><td>The number of video</td><td>Con</td></tr><tr><td>Summary (IV)</td><td>Information that presents or summarizes the main idea of a news item at the beginning of the news text</td><td>1 (yes); 0 (no)</td><td>Dic</td></tr><tr><td>Headline with locational information (IV)</td><td>The explicit location information in the headline of a news item</td><td>1 (yes); 0 (no)</td><td>Dic</td></tr><tr><td>Location of news event (IV)</td><td>Where a news event happened</td><td>1 (regional); 2 (inland);3 (oversea (including Hongkong, Macao, and Taiwan area))</td><td>Cat</td></tr><tr><td colspan="4">Content features</td></tr><tr><td>Subjective opinion (IV)</td><td>The presence of subjective opinion in a news text</td><td>1 (subjective); 0 (objective)</td><td>Dic</td></tr><tr><td>Positiveness/negativeness (IV)</td><td>From three dimensions of positiveness/negativeness: relation, performance, evaluation</td><td>1 (positiveness); 0 (negativeness)</td><td>Dic</td></tr><tr><td>Controversial news (IV)</td><td>At least two different opinions, comments or advice in a news text</td><td>1 (yes); 0 (no)</td><td>Dic</td></tr><tr><td>Serial news (IV)</td><td>A follow-up report about the previous related news event</td><td>1 (yes); 0 (no)</td><td>Dic</td></tr><tr><td>News referring to the future(IV)</td><td>The future pertains to a news item that includes the prediction of theperformance or development tendency of the event besides the report of the news event itself</td><td>1 (yes); 0 (no)</td><td>Dic</td></tr><tr><td>Life-related news (IV)</td><td>News that is related to daily life</td><td>1 (yes); 0 (no)</td><td>Dic</td></tr><tr><td>Private matters (IV)</td><td>News events involve private instances, which the people who are involved would prefer not to disclose to others</td><td>1 (yes); 0 (no)</td><td>Dic</td></tr><tr><td>Peculiarity (IV)</td><td>news event or the people involved in the news are novel and odd</td><td>1 (yes); 0 (no)</td><td>Dic</td></tr><tr><td colspan="4">Note. The data type is either continuous variable (Con), dichotomous (Dic) or categorical variable (Cat).</td></tr></table>

## 4.4 Extraction of Content Features by Content analysis

## 4.4.1 Coding scheme for content features

Content analysis was used to extract the quantification of the content features [2] variables because these variables were embedded in each online news article. Content analysis is a popular technique that transforms the meaning of text into objective data by systematic procedures to ensure the objectivity, reproducibility, and reliability of the data analysis [3,4,22,57]. Each online news article was coded to measure the content features variables (Table 3). In addition, content feature variables were dichotomously coded through checking the presence of variable traits in a news article (Table 4).

―Subjective opinion‖ refers to the presence of subjective opinion in a news text, as in the following three circumstances: (1) news about the views of experts or scholars, i.e., Example 1 in Table 4a; (2) the news text describes the event while having opinions from people on all sides, i.e., Example 2 in Table 4a; (3) hearsay or unverified news, i.e., Example 3 in Table 4a. The news that did not contain subjective opinions under the following three conditions was coded: (1) a news text that merely describes the event objectively, i.e., Example 4 in Table 4a; (2) the objective information related to the news event that was received from somebody in the news text, i.e., Example 5 in Table 4a; (3) policies, views, and speeches from state leaders or the government (news related to Chinese state leaders or the government are often objective reports of given facts), i.e., Example 6 in Table 4a.

Table 4a. Examples of subjective opinions

<table><tr><td>Coded as 1</td><td>Coded as 0</td></tr><tr><td>1. Experts: house price in China will not slump, people without house should not be too optimistic. (experts&#x27; opinion)</td><td>4. Tutors of the Voice of China Section 3 were determined: Na Ying, Wang Feng, Luo Dayou and Yang Kun. (report of an objective incident)</td></tr><tr><td>2. Bankers: alipay is a pity for banks. (a party&#x27;s opinion)</td><td>5. A navy plane crash: the dead 25 years old pilot scheduled to get married this year. (objective incident with added subjective information)</td></tr><tr><td>3. Rumor: passengers shouting out “bomb” when playing “fight the landlord” causes flight delay. (hearsay)</td><td>6. Xi Jinping: master key technology. (speech of a state leader)</td></tr></table>

The present study sets the variable ―positiveness/negativeness‖ based on the definition from van Atteveldt et al. (2008), who provided three dimensions of positiveness/negativeness: (1) Relation: Given two concepts located in the online news article, the relation may be positive (cooperative, supportive), i.e., Example 1 in Table 4b, or negative (conflictive, critical), i.e., Example 4 in Table 4b; (2) Performance: Given a concept located in the online news article, the concept may be successful (increasing, winning) , i.e., Example 2 in Table 4b, or failing (decreasing, losing), i.e., Example 5 in Table 4b; (3) Evaluation: Given a concept located in the online news article, the evaluation may be positive (good, sincere, or beautiful) , i.e., Example 3 in Table 4b, or negative (evil, wicked, or ugly), i.e., Example 6 in Table 4b. Two components, i.e., positive and negative are in a news text. Previous research coded these news (positive and negative news) as neutral [5,26]. This approach is not precise. We regard the news events as a process of development when coding these complicated news items. We code the news as positiveness when a news event develops from the bad aspect to the good aspect. By contrast, we code the news as negativeness when the opposite occurs.

Controversial news indicates at least two different opinions, comments or advice in a news text. Specific examples are shown in Table 4c.

Serial news is a follow-up report about the previous related news event. A news text can be coded as ―serial news‖ in the following two circumstances: (1) symbolic words are found in the headline, such as ―follow-up,‖ ―deny,‖ ―respond,‖ ―another news,‖ or ―another report,‖ e.g., example 1 in Table 4d; and (2) an obvious review about the previous situation of the event in the news text exists, e.g., example 2 in Table 4d.

News referring to the future pertains to a news item that includes the prediction of the performance or development tendency of the event aside from the report of the news event itself. Specific examples are shown in Table 4e.

Table 4b. Examples of positiveness/negativeness

<table><tr><td>Coded as1</td><td>Coded as 0</td></tr><tr><td>After Yixin, Qihoo 360 cooperates with Microsoft Xiaobing. (cooperative relationship)</td><td>4. Wong Li Kat accuses JDB again of tort: claiming for 20 million yuan. (controversy relationship)</td></tr><tr><td>Shanghai index increases by 1.08%, over the average level in 60 days----safely lead information up. (increase of the performance)</td><td>5. Hard landing of Shanxi&#x27;s economy: the profits of coal industry in the first quarter are just 0.8 billion yuan, decreasing by 86%. (decrease of the performance)</td></tr><tr><td>Tsinghua University offers help to the boy seizing knife to save people: having contacted with his school. (positive comment)</td><td>6. Supervision of taxi software: do not just for saving previous profits. (negative comment)</td></tr></table>

Table 4c Examples of controversial news

<table><tr><td>Coded as 1</td><td>Coded as 0</td></tr><tr><td>1. Policemen in three provinces shoot dead three persons in one day, when did they shoot raising controversy. (controversial views of a news event)</td><td>2. Decline of “Coal Golden Triangle” in China: it has created over 10000 billionaires. (a view without controversy)</td></tr></table>

Table 4d Examples of serial news

<table><tr><td>Coded as 1</td><td>Coded as 0</td></tr><tr><td>1. Pan Shiyi deny hitting the female staff of Shenzhen Airlines.(respond as symbolic words)</td><td>3. Collision of two electric vehicles: one person is injured and a passerby giving advices to see a doctor suffers claim of indemnity.(the latest news)</td></tr><tr><td>2. Kidnap in Qianjiang, Hubei province: the deputy secretary asks for being the hostage.(add detailed information of a news event)</td><td>4. Four ways to check personal credit report from June 9. (the latest news)</td></tr></table>

Table 4e. Examples of news referring to the future

<table><tr><td>Coded as 1</td><td>Coded as 0</td></tr><tr><td>1. The Central Bank directs to decrease quasi-A shares: three shares are expected to gain benefits. (performance prediction)</td><td>4. 113 key staffs of the heresy “Omnipotent God” are arrested in Liaoning. (the news event has happened, no prediction)</td></tr></table>

Life-related news. This variable refers to news that are related to daily life, including the following aspects: (1) food, such as food safety, e.g., example 1 in Table 4f; (2) consumer price, such as price index, e.g., example 2 in Table 4f; (3) housing, such as the increase in housing prices; (4) investment, such as stock information; (5) children, such as campus news, e.g., example 3 in Table 4f; (6) safety, such as violent and terrorist events or air pollution, e.g. example 4 in Table 4f; (7) education, such as problems of entering a higher school; and (8) medical problems, such as medical disputes and medical negligence.

Private matters refer to news events involve private instances, which the people who are involved would prefer not to disclose to others, such as sexual relations, family affairs, or private lives of famous persons. Specific examples are shown in Table 4g.

Table 4f Examples of life-related news

<table><tr><td>Coded as 1</td><td>Coded as 0</td></tr><tr><td>1. “Smelly foot rice noodles” in Dongguan: workers step on rice noodles or sleep in barefoot.(related to food safety)</td><td>5. Naval fleet first takes part in RIMPAC at Pearl Harbor.(military news, not related to daily life)</td></tr><tr><td>2. Guangdong Mobile: 4G traffic will realize “no clearing” indirectly.(related to mobile phone tariff)</td><td>6. Chinese government presents a note to UNSG about Vietnam’s illegal disturbance of the “Zhong Jian Nan Program”.(political news, not related to daily life)</td></tr><tr><td>3. Hebei: a baby boy born after 72 days is stolen, the police offers a reward of 100000 yuan for clues.(related to children)</td><td>7. Technology creates the future: Baidu issues a billion bond.(news of a company, not related to daily life)</td></tr><tr><td>4. Chinese Academy of Social Science: canalizing between Beijing and Tianjin will improve the problem of haze. (related to air pollution control)</td><td></td></tr></table>

Table 4g Examples of private matters

<table><tr><td>Coded as 1</td><td>Coded as 0</td></tr><tr><td>1. A typical notification from the Commission for Discipline Inspection in Shenzhen: a policeman goes out to get a hotel room during office hours. (related to improper sexual relations)</td><td>2. Xi Jinping: master key technology. (state leader&#x27;s opinion, not related to privacy)</td></tr></table>

Peculiarity means that news event or the people involved in the news are novel or odd. The events or people that are involved in an odd news are illogical or are rarely seen in daily life.

Specific examples are shown in Table 4h.

Table 4h Examples of peculiarities

<table><tr><td>Coded as 1</td><td>Coded as 0</td></tr><tr><td>1. A dolphin commits suicide after being separated with the beautiful language teacher it loves.(animal commits suicide for human beings, rarely seen)</td><td>2. Four ways to check personal credit report from June 9.(establishing the credit system has been discussed for a long time, not rare)</td></tr></table>

## 4.4.2 Content analysis procedure

We followed the steps of content coding and analysis that were suggested by Krippendorff [42] and Landis and Koch [44]. In our research, the unit of analysis was an online news article. For the content coding, four graduate students were hired to code the online news data separately. We ensured that each news set was coded by two persons separately. The authors were not involved in content coding. The graduate student coders were not allowed to communicate with one another while coding and were asked not to spend more than two hours each day in data coding to minimize fatigue-related coding errors.

Pilot data coding was performed for the online news data sets. Our goal for pilot coding was to repeat the coding and refine the coding book. If the pilot coding result did not reach the Kappa threshold value of $0 . 7 0 ,$ then the two authors and all student coders discussed the disputed coding results. The coding disagreements were adjudicated by discussion, and consensus was reached after a joint examination of the feature. Inter-coder reliability, which was computed using the agreement percentage for all variables, ranged from 0.70 to 0.97, which showed high reliability levels for all variables [42,44].

## 4.5 Analysis method

Given the dichotomous nature of certain independent variables (such as the summary, title with location information, and positiveness/negativeness), we employed the logistic regression method. Logistic regression was appropriate for the outcome and predictor variables to come out dichotomous, continuous, or categorical [24]. Tsagkias et al. [67] showed that the linear log method was also reliable for predicting the popularity of news articles.

The Spearman rank correlation test results (Appendix C) indicated that, all the correlations were less than 0.3, except for one item. The correlation between social media recommendations and the number of comments was 0.607, which mean that this relationship warrants further research. Moreover, the multicollinearity problems test (Appendix D) indicated that all tolerances were close to 1 and the VIFs were less than 1.4 for both the number of browses and comments [54]. All these results indicated that no significant multicollinearity problems were found.

We conducted t-tests to determine whether the overall data (social, entertainment, SciTech, and financial news) could be pooled and treated as a single sample [39]. The results revealed no significant differences among the four news categories for all the independent and dependent variables. However, the samples can be combined.

## 5. Evaluation Results

## 5.1 Three group features to explain the number of readers’ comments

Using logistic regression analysis, we explained the number of comments in online news sites using 16 independent variables. To determine the extent, structural features, content features, and usage features to help explain the variance in the number of comments, we conducted three hierarchical regressions. In step 1, we entered the structural features, which we named ―model 1‖. In step 2, we entered the content features, which we named ―model 2‖. In step 3, we entered the usage feature, which we named ―model 3‖. Such hierarchical regressions allowed us to determine the unique variance that was measured as the increment in the R-square change and in the F-value, which showed how each set of IVs contributed to the dependent variables [15,38] in our study, i.e., the number of comments.

Table 5 shows that the R-square changes of the three regression steps are all significant at the p< 0.01 level, including the regressions of the structural features (model 1), content features (model 2), and usage features (model 3). Although each of the specific structural, content, and usage features did not have the same influence on the number of comments, the overall significance of the R-square changed for models 1, 2, and 3, which verified that the three sets of IVs contributed to the number of comments in principle. The results suggested positive increasing effects of the three categories of features: structural features (F change =

$9 9 . 1 0 2 \ \mathrm { P } < 0 . 0 0 1 )$ , content features $( \mathrm { F \ c h a n g e } = 1 9 . 4 3 4 \ \mathrm { P } < 0 . 0 0 1 )$ ), and usage features (F change = 597.992 P < 0.001). As indicated in Table 5, the R-square change of model 3 was significant $( \mathrm { F } = 5 9 7 . 9 9 2 , \mathrm { P } < 0 . 0 0 1 )$ . The inclusion of the usage features indicated an equally strong beta of 0.465, which increased the $\mathsf { R } ^ { 2 }$ to 0.471. In model 3, the usage features (social media recommendations), which was suggested to affect the number of comments, possessed a significantly higher explanatory power than model 2.

Table 5 Logistic regression results

<table><tr><td rowspan="2">Independent variables</td><td colspan="2">Social media recommendation</td><td colspan="3">The number of comments</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td colspan="6">Structural features</td></tr><tr><td>News release time</td><td>-0.042*</td><td>-0.037N.S.</td><td>0.026N.S.</td><td>0.016***</td><td>0.034*.</td></tr><tr><td>Pictures</td><td>0.178***</td><td>0.188***</td><td>0.194***</td><td>0.183***</td><td>0.096***</td></tr><tr><td>The number of words</td><td>0.166***</td><td>0.146***</td><td>0.059**</td><td>0.038 N.S.</td><td>-0.030N.S.</td></tr><tr><td>Video</td><td>0.054**</td><td>0.059**</td><td>0.081***</td><td>0.049*</td><td>0.022N.S.</td></tr><tr><td>Summary</td><td>0.008N.S.</td><td>0.028N.S.</td><td>-0.012N.S.</td><td>-0.005N.S.</td><td>-0.018N.S.</td></tr><tr><td>Headline with locational information</td><td>0.376***</td><td>0.321***</td><td>0.441***</td><td>0.417***</td><td>0.268***</td></tr><tr><td>Location of news events</td><td>-0.188***</td><td>-0.128***</td><td>-0.198***</td><td>-0.145***</td><td>-0.086***</td></tr><tr><td colspan="6">Content features</td></tr><tr><td>Subjective opinion</td><td rowspan="8"></td><td>-0.022 N.S.</td><td rowspan="8"></td><td>0.001 N.S.</td><td>0.011N.S.</td></tr><tr><td>Positiveness/negativeness</td><td>-0.157***</td><td>-0.137***</td><td>-0.063***</td></tr><tr><td>Controversial news</td><td>0.036 N.S.</td><td>0.072***</td><td>0.055***</td></tr><tr><td>Serial news</td><td>-0.022 N.S.</td><td>0.024N.S.</td><td>0.034*</td></tr><tr><td>News referring to the future</td><td>-0.003 N.S.</td><td>0.056**</td><td>0.057***</td></tr><tr><td>Life-related news</td><td>0.135***</td><td>0.130***</td><td>0.067***</td></tr><tr><td>Private matters</td><td>-0.049*</td><td>0.073***</td><td>0.096***</td></tr><tr><td>Peculiarity</td><td>0.036 N.S.</td><td>-0.036N.S.</td><td>-0.053***</td></tr><tr><td colspan="6">Usage features</td></tr><tr><td>Social media recommendation</td><td></td><td></td><td></td><td></td><td>0.465***</td></tr><tr><td> $R^2$ </td><td>21.7%</td><td>26.5%</td><td>25.8%</td><td>31.2%</td><td>47.1%</td></tr><tr><td>Change in  $R^2$ </td><td>21.7%</td><td>4.9%</td><td>25.8%</td><td>5.4%</td><td>15.9%</td></tr><tr><td>Adjusted  $R^2$ </td><td>21.4%</td><td>26%</td><td>25.5%</td><td>30.6%</td><td>46.6%</td></tr><tr><td>F</td><td>78.893***</td><td>47.879***</td><td>99.102***</td><td>60.062***</td><td>110.531***</td></tr><tr><td>F Change</td><td>78.893***</td><td>16.466***</td><td>99.102***</td><td>19.434***</td><td>597.992***</td></tr></table>

With regard to the structural features, we found the following in model 3, (1) the news

#

release time was found to positively affect the number of comments $( \beta = 0 . 0 3 4 , \rho < 0 . 0 5 )$ . (2) Pictures were found to positively affect the number of comments $( \beta = 0 . 0 9 6 , \rho < 0 . 0 0 1 )$ . (3) A headlines with location information was found to positively affect the number of comments (β $= 0 . 2 6 8 , \mathrm { ~ p ~ } < 0 . 0 0 1 )$ . (4) The location of the news event was found to negatively affect the number of comments $( \beta = - 0 . 0 8 6 , \ p < 0 . 0 0 1 )$ ). Moreover, certain structural features did not affect the online news comments: (1) the relationship between the number of words and the number of comments; (2) the relationship between the video and the number of comments; and (3) the relationship between the summary and the number of comments.

For content features, the results are as follows: (1) the positiveness/negativeness of the content was found to negatively affect the number of comments $( \beta = - 0 . 0 6 3 , \rho < 0 . 0 0 1 )$ . (2) Controversial news was found to positively affect the number of comments $( \beta = 0 . 0 5 5 , \rho <$ 0.001). (3) Serial news was found to positively affect the number of comments $( \beta = 0 . 0 3 4 , \rho <$ 0.05). (4) News referring to the future was found to positively affect the number of comments $( \beta = 0 . 0 5 7 , \ p < 0 . 0 0 1 )$ . (5) Life-related news was found to positively affect the number of comments $( \beta = 0 . 0 6 7 , \rho < 0 . 0 0 1 )$ ). (6) News on private matters was found to positively affect the number of comments $( \beta = 0 . 0 9 6 , \rho < 0 . 0 0 1 )$ the number of comments $( \beta = - 0 . 0 5 3 , \mathrm { p } < 0 . 0 0 1 )$ ). However, we did not find an effect of a subjective opinion on the number of comments.

For the usage features, we found that social media recommendation had a positive effect on the number of comments $( \beta = 0 . 4 6 5 , \rho < 0 . 0 0 1 )$ .

We further explained social media recommendation on online news sites for the structural and content features. Table 4 shows our observations on the effect of structural and content features on social media recommendation. For the structural features: (1) pictures were found to positively affect the social media recommendation $( \beta = 0 . 1 8 8 , \rho < 0 . 0 0 1 )$ . (2) The number of words was found to positively affect social media recommendation $( \beta = 0 . 1 4 6 , \ p < 0 . 0 0 1 )$ ). (3) Video was found to positively affect social media recommendation $( \beta = 0 . 0 5 9 , \rho < 0 . 0 1 )$ ). (4) A headline with location information was found to positively affect social media recommendation $( \beta = 0 . 3 2 1 , \mathrm { ~ p ~ < ~ } 0 . 0 0 1 )$ . (5) The location of a news event was found to negatively affect social media recommendation $( \beta = - 0 . 1 2 8 , \mathrm { ~ p ~ < ~ } 0 . 0 0 1 )$ . For the content features: (1) the positiveness/negativeness of the content was found to negatively affect socia media recommendation $( \beta \ = \ - 0 . 1 5 7 , \ \mathrm { p } \ < \ 0 . 0 0 1 )$ . (2) A life-related news was found to positively affect social media recommendation $( \beta = 0 . 1 3 5 , \rho < 0 . 0 0 1 )$ ). (3) Private matters were found to negatively affect social media recommendation $( \beta = - 0 . 0 4 9 , \rho < 0 . 0 5 )$ \_

## 5.2 Mediating effect of social media recommendation on number of comments

Social media recommendation affects the number of comments, and is influenced by both structural and content features (Table 5). We further investigated the mediating role of social media recommendations, which mediates the relationship between structural and content features, and the number of online news comments, and we determined whether recommendation had a partial or full mediation. To test this mediating effect, we used three regression analysis and followed Sobel’s procedure [10,34], which allowed us to examine whether the relationship between features and the number of comments was considerably reduced (partial mediation) or completely diminished (full mediation) when we incorporated social media recommendation into the model.

Table 6. Mediation effect of social media recommendation between the independent variables and the number of comments

<table><tr><td>Social media recommendation(M)</td><td colspan="7">The number of comments (Y)</td></tr><tr><td>(X)</td><td>c</td><td>a</td><td>b</td><td>c'</td><td>Sobel test</td><td>Mediation effect</td><td>Mediation effect/Total effect</td></tr><tr><td colspan="8">Structural features</td></tr><tr><td>News release time</td><td>0.052*</td><td>-0.019N.S.</td><td>0.608***</td><td>0.064***</td><td>-0.818N.S.</td><td>N.S.(c'&gt;c)</td><td></td></tr><tr><td>Pictures</td><td>0.124***</td><td>0.102***</td><td>0.601***</td><td>0.062***</td><td>4.601***</td><td>PM(c')49.4%</td><td>49.4%</td></tr><tr><td>The number of words</td><td>0.041N.S.</td><td>0.151***</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Video</td><td>0.088***</td><td>0.062**</td><td>0.604***</td><td>0.050**</td><td>2.805**</td><td>PM(c')4.43%</td><td>4.43%</td></tr><tr><td>Summary</td><td>0.051*</td><td>0.056*</td><td>0.606***</td><td>0.017N.S.</td><td>2.528**</td><td>FM(c’N.S.)</td><td>66.5%</td></tr><tr><td>Headline with locational information</td><td>0.413***</td><td>0.345***</td><td>0.527***</td><td>0.231***</td><td>14.312***</td><td>PM(c')44%</td><td>44%</td></tr><tr><td>Location of news events</td><td>-0.207***</td><td>-0.207***</td><td>0.589***</td><td>-0.085***</td><td>-8.977***</td><td>PM(c')58.9%</td><td>58.9%</td></tr><tr><td colspan="8">Content features</td></tr><tr><td>Subjective opinion</td><td>-0.089</td><td>-0.057</td><td>0.604</td><td>-0.055</td><td>-2.560</td><td>PM</td><td>38.7%</td></tr><tr><td></td><td>***</td><td>**</td><td>***</td><td>**</td><td>**</td><td> $(c'$ </td><td></td></tr><tr><td>Positiveness/negativeness</td><td>-0.281***</td><td>-0.278***</td><td>0.573***</td><td>-0.122***</td><td>-12.147***</td><td>PM\( (c')</td><td>56.7%</td></tr><tr><td>Controversial news</td><td>0.147***</td><td>0.114***</td><td>0.598***</td><td>0.078***</td><td>5.096***</td><td>PM $(c')$ </td><td>46.3%</td></tr><tr><td>Serial news</td><td>0.071***</td><td>0.018N.S.</td><td>0.606***</td><td>0.060***</td><td>0.815N.S.</td><td>N.S.</td><td></td></tr><tr><td>News referring to the future</td><td>-0.008N.S</td><td>-.045*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Life-related news</td><td>0.19***</td><td>0.2***</td><td>0.593***</td><td>0.071***</td><td>8.906***</td><td>PM $(c')$ </td><td>62.4%</td></tr><tr><td>Private matters</td><td>0.028N.S.</td><td>-0.086***</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Peculiarity</td><td>-0.069***</td><td>0.008N.S.</td><td>0.608***</td><td>-0.074***</td><td>0.344N.S.</td><td>N.S.</td><td></td></tr><tr><td colspan="8">Note. *: p&lt;0.05, **: P&lt;0.01, ***: P&lt;0.001 N.S.: not significant S.: significantX: Independent variables; M: Mediation variable; Y: Dependent variablePM: partial mediation FM: Full mediationa: Beta of X→Mb: Beta of M→Y c: Beta of X→Y c': Beta of X and M→Y</td></tr></table>

Table 6 shows that (1) social media recommendation appears to partially mediate the influence of pictures on the number of comments $( \mathbf { c } ^ { \prime } = 0 . 0 6 2 < \mathbf { c } = 0 . 1 2 4$ , Sobel test [4.6901 p<0.001], and mediation effect/total $\mathrm { e f f e c t } \ = \ 4 9 . 4 \% )$ . (2) Social media recommendation appears to partially mediate the influence of videos on the number of comments $( \mathrm { c } ^ { 3 } = 0 . 0 5 0 <$ ${ \mathrm { c } } = 0 . 0 8 8$ , Sobel test [2.805 p<0.01], mediation effect/total effect = 4.43%). (3) Social media recommendation appears to fully mediate the influence of the summary on the number of comments $( \mathrm { c } \ ^ { \prime } = 0 . 0 1 7 \ : \mathrm { N } . S . ,$ Sobel test [2.528 p<0.01], mediation effect/total effect = 66.5%). (4) Social media recommendation appears to partially mediate the influence of a headline with location information on the number of comments $( \mathrm { c } ^ { \prime } = 0 . 2 3 1 < \mathrm { c } = 0 . 4 1 3$ , Sobel test [14.312 p<0.001], mediation effect/total effect = 44%). (5) Social media recommendation appears to partially mediate the influence of the location of a news event on the number of comments $( \mathbf { c } ^ { \prime } = - 0 . 0 8 5 < \mathbf { c } = - 0 . 2 0 7$ , Sobel test [-8.977 p<0.001], mediation effect/total effect = 58.9%). (6) Social media recommendation appears to partially mediate the influence of a subjective opinion on the number of comments $( \mathrm { c } ^ { \ \prime } = - 0 . 0 5 5 < \mathrm { c } = - 0 . 0 8 9$ , Sobel test [-2.560 $\mathrm { p { < } 0 . 0 1 ] }$ , mediation effect/total effect = 38.7%). (7) Social media recommendation appears to partially mediate the influence of positiveness/negativeness on the number of comments $\therefore \overrightarrow { \mathbf { \nabla } } ( \mathbf { c _ { \alpha } } ) = \mathbf { \nabla }$ $- 0 . 2 8 1 < \mathbf { c } = - 0 . 1 2 2$ , Sobel test [-12.147 p<0.001], mediation effect/total effect = 56.7%). (8) Social media recommendation appears to partially mediate the influence of controversial news on the number of comments $( \mathrm { c } ^ { \mathrm { \prime } } = 0 . 0 7 8 < \mathrm { c } = 0 . 1 4 7$ , Sobel test $[ 5 . 0 9 6 \ \mathrm { p } { < } 0 . 0 0 1 ]$ mediation effect/total effect = 46.3%). (9) Social media recommendation appears to partially mediate the influence of a life-related news on the number of comments $( \mathrm { c } ^ { \mathrm { 3 } } = 0 . 0 7 1 < \mathrm { c } = 0 . 1 9$ Sobel test $[ 8 . 9 0 6 \mathrm { p } { < } 0 . 0 0 1 ]$ , mediation effect/total effect = 62.4%).

![](/api/attachments/N48FMMX2/fulltext/images/4da667e404f5f0369c126dadb0b1e7197ca00176b807651b4a23e5e3227e9591.jpg)  
Figure 2. Mediation model for explaining the number of comments

Based on these results, we constructed a mediation model, that indicated the significance of social media recommendation in explaining the number of comments. The mediating effect of social media indicated that both structural (pictures, video, headline with locational information, and locations of news events) and content (subjective opinion, positiveness/negativeness, controversial news, and life-related news) features affected the number of comments both directly and indirectly, whereas the summary affected the number of comments indirectly only.

## 6. Discussion

## 6.1 Key findings

The objective of this research is to explain the reason behind the difference in the number of online news comments. We developed a framework that integrated three types of features (structural, content, and usage features), to explain the number of comments. This study is the first to thoroughly examine the role of the structural, content, and usage features in the online news context. The regression model reveals 47.1% of the variance in the number of comments. In general, this result shows that the framework is powerful in explaining the number of comments. Based on the data analysis results, we obtained three main findings. First, in addition to the attributes of online news, our study also conceptualized, operationalized, and validated the nature of the social media recommendations. We explored the relative role of social media recommendation as the usage feature, rather than the structural and content features, to explain the number of comments. Second, we found a mediation model of social media recommendation for the explanation of the number of comments. This mediation model indicates that social media recommendation may be an important path and mechanism for structural and content features that affect the reader’s comments. Finally, we have developed six content features, namely, controversial news, serial news, news referring to the future, life-related news, private matters, and peculiarities, from the online news article content. Content features are important attributes of online news, which could be extracted through content analysis method. The logistic regression results show that content features have significant effects on the number of online news comments.

## 6.1.1 Usage features

#

Social media recommendation is positively significant and is the most effective feature for explaining the number of comments. Readers’ recommendation promotes online news on social media to attract online readers, who have more or less similar interests with the recommender. The efficient promotional effect of social media generates more attention and comments for the online news. Our analyses show that the explaining power of the model is improved as usage features (social media recommendation) are added into the framework. The results also further confirm the superiority of social media recommendation over structural and content features in explaining the number of comments.

Furthermore, our findings reveal the key role of social media recommendation in explaining the number of comments, by mediating the influences of recommendation on structural features (pictures, video, summary, headline with location information, and location of news event) and content features (subjective opinion, positiveness/negativeness, controversial news, and life-related news). From these results, we constructed a mediation model to explain the number of comments，which meant that social media recommendation may be the valuable mechanism for structural and content features that affect readers comments.

## 6.1.2 Structural features

The logistic regression results for the number of comments indicate that although the number of words, videos, and summary do not contribute to the number of comments, news release time, pictures, headline with location information, and location of the news event have significant contributions. If we remove the content and usage features from the model, the results show that the number of words and videos both significantly affect the number of

This result implies that users would be more active to longer online news with pictures and videos. The number of words, pictures, and video, as carriers of online news, could convey rich information, which could arouse the readers’ attention extensively. Moreover, readers who pay more attention to online news will more likely tend to post comments. Online news that are released from 10 pm to 7 am are found to generate a larger number of comments, whereas online news that are released from 7 am to 12 am generate fewer comments. This observation may be because many people prefer to read the news in the morning, which are published the previous night (10 pm to 7 am). The large number of readings in the morning will result in more comments on the news that are released from 10 pm to 7am. The location information mentioned in the online news headline could arouse some readers’ interest, especially for those who live in the area mentioned or those who are concerned about the area. Regional online news receives more comments, because regional online news can strongly resonate with the readers. Unexpectedly, the summary has no contributions to the number of comments, which may be because 64% of the news articles in our sample has the summary at the beginning and the summary shows the basic writing skills of the news author.

## 6.1.3 Content features

In addition to the subjective opinion, other content features have significant effects on the number of comments on online news sites. The logistic regression results indicate that negative news articles received much more comments than positive news articles. Negative information can encourage the readers’ thinking and criticism to the online news event, which result in active discussions. Online news articles with controversial opinions are more likely to receive comments because a double controversy could be discuss material for readers. Controversy attracts, readers’ critical thinking which could, then urge the readers to express their views. If the news event has already been released (i.e., has accumulated a large amount of attention) recently, the series of online news articles on this event will receive more views from commenters. This higher number of comments may be caused by the promotional effect of preliminary reports on the news event, and subsequent reports can more easily catch readers’ attention. Future-related online news articles receive much more comments, because the uncertainty of a forecast could attract readers’ expectations, which could urge the readers to think about the developmental trend of the news event and express their views on this news. Given that readers’ concerns and demands are closely related to their daily life, life-related news receive an even higher number of comments. In addition, reader focus more on private matters, such as matters that actors prefer to hide. Given reader curiosity, they are more likely to comment on online news that are related to private matters. Interestingly, the results indicate that readers do not like to comment on the odd news, which may be because most odd news are deviated from facts, deliberately exaggerated, and may even be false news, which arouses readers’ antipathy.

By contrast from previous literature [8], online news articles that are written in a more emotional, personal, and subjective tone do not receive more comments. We further test the effect of subjective opinion in different types of online news. The results indicate that subjective opinions have a negatively significant effect on the number of comments for social and entertainment news. Understanding the social and entertainment news events is easier for most online news readers. Thus, readers tend to explore the truth behind the news events, and readers tend to independently express their own views without others’ opinions. However, for SciTech and financial news, subjective opinion has a positively significant effect on the number of comments. Understanding the relevant professional knowledge in SciTech and financial news is difficult for most readers. To help readers understand the news events, and to urge the readers to express their points of view in these types of news, expert analysis is needed.

## 6.2 Theoretical contributions

This study deepens and extends prior research by proposing a new framework, which is the first study to thoroughly examine the role of structural, content, and usage features in the online news context, to explain the number of readers’ comments on the online news sites. Prior research on social media have mainly focused on the exploration of how structural features, such as days of the week [1], regional coverage [1] and articles that are published at the same hour for a source [68], and on the prediction of the comment number of comments in the news articles. Given that readers’ comments on online news sites are becoming more complex and multifaceted, introducing more features from a holistic perspective is necessary. The present research provides a powerful framework for gaining a better understanding of the number of readers’ comments. Future research should further develop this framework, which can be applied in shaping comments in other media contexts.

Our research framework offer several important theoretical contributions and implications for future online news comment research. First, to the best of our knowledge, this is the first study that examines the nature and role of social media recommendation. With regard to the 16 features variables, we highly consider social media recommendation as relatively more important than structural and content features for explaining the number of comments. Prior research has ignored the critical role of social media recommendation in online news comments. This study extends our understanding of the promotional effect of social media in explaining the number of readers’ comments. The superiority of social media recommendation suggests future research should conceptualize the effects of recommendation in understanding the number of readers’ comments.

Second, based on the framework and data analysis results, we have found a mediation model of social media recommendation to explain the number of comments. Previous researches have ignored the path analysis between the various features and the number of reader comments. To the best of our knowledge, this study is the first to develop recommendation on the social media construct. Furthermore, the construct of social media recommendation as mediator for the five structural features (pictures, video, summary, headline with location information, and location of news event) and four content features (subjective opinion, positiveness/negativeness, controversial news and life-related news) to explain the number of comments, has been tested by data analysis. The mediation effect of social media recommendation in explaining the number of readers’ comments suggests that future research on online news comments should consider this promotional effect construct and should conceptualize not only the independent effects, but also the potential mediation effect in understanding the number of readers’ comments on online news.

Third, our study primarily conceptualizes, operationalizes, and validates the six content features, namely, controversial news, serial news, news referring to the future, life-related news, private matters, and peculiarity, from online news articles. Prior research on online news mainly focus on the objective structural features [1,25,67] and propose subjective/negative and positive/negative [6,8,72] features for the online news content. Our study provides a deep understanding of online news content attributes and work on generalizes these content features. Future online news research might consider these content features as a possible factor for the study of online news comments.

## 6.3 Practical Contributions

Our findings have important practical implications for both online news websites and marketing managers of other industries.

This explanation model for the number of online news will help news websites and their managers to better understand the determinants of the number of comments in a news item, which allows the managers to develop effective methods to improve the number of comments in a news item. According to the logistic regression results in this paper, online news websites can add pictures and videos; use more words; highlight the location information in the titles,; emphasize the objective, positive, controversial, serial, future-oriented, life-related, and impersonal contents, to foster more user comments.

Most importantly, the results of data mining show that reader recommendation on social media is the most powerful factor for increasing online news comments. News sites should attach importance to social media and to recommenders. News websites should practice measures to attract the attentions of potential recommenders, and to provide facilities that would allow endorsing the news on the personal profiles of the recommenders. These possible facilities include technical feasibility and a variety of incentives.

The findings of this study also benefit business companies. Based on these results, marketing managers can identify news web pages that aid in gaining more and deeper concers from readers, and helps in a more effective investment of the business advertisement of marketing managers. Particularly, advertising online news with pictures; videos; more words; and objective, positive, controversial, serial, future-oriented, life-related, and impersonal contents, it cost effective for business companies.

## 6.4 Limitations and suggestion for future research

Similar to other studies, this study also has limitations. First, various kinds of news in online news sites exist, with different characteristics. This study only considers four news types news, namely, social, entertainment, SciTech, and financial news. Although these four news types are on top of news rankings, other news types are also popular, such as sports news. Future research should extend the scope of online news. Moreover, our current treatment of online news does not distinguish the four news types. To extend our understanding of the specific online news types, future research should identify the different online news types, and compare the relative roles of different antecedents, as identified in our proposed framework.

Second, we have only considered eight content features (subjective opinion, positiveness/negativeness, controversial news, serial news, news that refer to the future, life-related news, private matters, and peculiarities) and one usage features (social media recommendation) in our study. However, the attributes of online news, and the interaction between online news sites and social media are complex, which may affect readers’ comments. Future research could exceed these content and usage features that we used and explore more complex features as antecedents for readers’ comments. For example, ―the celebrity effect‖ [26] and ―actors identity‖ are both possible influential factors.

Third, news articles are extremely time sensitive by nature [8]. We have tested the number of comments only with seven days after the news is being released. Testing the number of comments at different times is worthwhile, such as in the first 30 minutes of the online news or on the first day of the online news. Panel data is meaningful for future research, which could be used to observe the developmental trend of news comments and compare the relatively important features to explain readers’ comments at different times.

## 7. Conclusion

Drawing from the attributes of online news and readers’ social media recommendation, we introduced three sets of features (structural, content, and usage features) as the framework to explain the number of readers’ comments on online news sites. We first developed six content features and obtained data extracted from online news articles through the content analysis method. In addition to the structural and content features, we also first developed the construct of ―social media recommendation‖ as the usage features. We then used logistic regression to testify the proposed framework. The results indicated that it is a powerful framework to explain the number of readers’ comments. Furthermore, we demonstrated the superiority of social media recommendation than structural and content features in explaining the number of the number of readers’ comments. Subsequently, we found the mediation model of ―social media recommendation‖ for five structural features and four content features to explain the number of comments. The results should be valuable for online news providers to devise effective interventions to encourage more reader comments.

## Reference

[1] M. Abdul-Mageed, Online news sites and journalism 2.0: reader comments on Al jazeera arabic, tripleC Commun. Capital. Crit. Open Access J. a Glob. Sustain. Inf. Soc. 6(2), 2008, pp. 59–76.

[2] A.S. Abrahams, W. Fan, G. Alan Wang, Z.J. Zhang, J. Jiao, An integrated text 2014.

[3] A.S. Abrahams, J. Jiao, W. Fan, G.A. Wang, Z. Zhang, What’s buzzing in the blizzard of buzz? Automotive component isolation in social media postings, Decis. Support Syst. 55(4), 2013, pp. 871–882.

[4] A.S. Abrahams, J. Jiao, G.A. Wang, W. Fan, Vehicle defect discovery from social media, Decis. Support Syst. 54(1), 2012, pp.87–97.

[5] W. van Atteveldt, J. Kleinnijenhuis, N. Ruigrok, S. Schlobach, Good news or bad news? Conducting sentiment analysis on dutch text to distinguish between positive and negative relations, J. Inf. Technol. Polit. 5(1), 2008, pp. 73–94.

[6] A. Balahur, R. Steinberger, Rethinking sentiment analysis in the news: From theory to practice and back, in: Proceeding of WOMSA, 2009.

[7] A. Balali, H. Faili, M. Asadpour, M. Dehghani, A supervised approach for reconstructing thread structure in comments on blogs and online news agencies, Comput. Y Sist. 17(2), 2013, pp. 207–217.

[8] R. Bandari, S. Asur, B. Huberman, The pulse of news in social media: forecasting popularity, in: ICWSM, 2012.

[9] P. Bao, H. Shen, J. Huang, X. Cheng, Popularity prediction in microblogging network : A case study on sina weibo, in: Proc. 22nd Int. Conf. World Wide Web Companion, 2013, pp. 177–178.

[10] R.M. Baron, D.A. Kenny, The moderator-mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations, J. Pers. Soc. Psychol. 51(6), 1986, pp. 1173–1182.

[11] M. Briggs, Journalism 2.0: how to survive and thrive, USF Tampa Bay Open Access Textb. Collect. B. 2. 2007.

[12] D. Carmel, H. Roitman, E. Yom-Tov, On the relationship between novelty and popularity of user-generated content, ACM Trans. Intell. Syst. Technol. 3(4), 2012, 69.

[13] D.S. Chung, Profits and perils: online news producers’ perceptions of interactivity and uses of interactive features, Converg. Int. J. Res. into New Media Technol. 13(1), 2007, pp. 43–61.

[14] Y. Cong, A. Kogan, M.A. Vasarhelyi, Extraction of structure and content from the edgar database : A template-based approach, J. Emerg. Technol. Account. 4(1), 2007, pp. 69–86.

[15] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: A comparison of two theoretical models, Manage. Sci. 35(8), 1989, pp. 982–1003.

[16] M. Deuze, The web and its journalisms : Considering the consequences of different types of newsmedia online, News Media Soc. 5(2), 2003, pp. 203–230.

[17] D. Domingo, Interactivity in the daily routines of online newsrooms: Dealing with an uncomfortable myth, J. Comput. Commun. 13(3), 2008, pp. 680–704.

[18] D. Van Essen, C. Anderson, D. Felleman, Information processing in the primate visual system: An integrated systems perspective, Science. 255(5043), 1992, pp. 419–423.

[19] W.P. Eveland, K. Marton, M. Seo, Moving beyond ―just the facts‖: The influence of online news on the content and structure of public affairs knowledge, Communic. Res. 31(1), 2004, pp. 82–108.

[20] W. Fan, M.D. Gordon, The power of social media analytics, Commun. ACM. 57(6), 2014, pp. 74–81.

[21] W. Fan, M.D. Gordon, P. Pathak, Genetic Programming-based discovery of ranking functions for effective web search, J. Manag. Inf. Syst. 21(4), 2005, pp. 37–56.

[22] W. Fan, L. Wallace, S. Rich, Z. Zhang, Tapping the power of text mining, Communications. 49(9), 2006, pp. 77–82.

[23] S. Faridani, E. Bitton, K. Ryokai, K. Goldberg, B. Ca, Opinion space : a scalable tool for browsing online comments, in: Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2010, pp. 1175–1184.

[24] A. Field, Discovering statistics using SPSS, Sage Publications, 2009.

[25] B. Finch, Internet discussions as a source for consumer product customer involvement and quality information: An exploratory study, J. Oper. Manag. 17(5), 1999, pp. 535–556.

[26] G. Giannopoulos, I. Weber, A. Jaimes, T. Sellis, Diversifying user comments on news articles, in: Web Inf. Syst. Eng. 2012, Springer Berlin Heidelberg, 2012, pp. 100–113.

[27] M. Gupta, J. Gao, C. Zhai, J. Han, Predicting future popularity trend of events in microblogging platforms, Proc. Am. Soc. Inf. Sci. Technol. 49(1), 2012, pp. 1–10.

[28] X. He, M. Gao, M.-Y. Kan, Y. Liu, K. Sugiyama, Predicting the popularity of web 2.0 items based on user comments, in: Proc. 37th Int. ACM SIGIR Conf. Res. Dev. Inf. Retr. - SIGIR ’14, ACM Press, New York, New York, USA, 2014, pp. 233–242.

[29] A. Hermida, N. Thurman, Comments please : how the british news media are struggling with user-generated content comments please : How the british news media is struggling with user-generated content, in: Artic. Present. En El 8th Int. Symp. Online Journal., 2007, pp. 1–28.

[30] A. Hermida, N. Thurman, A clash of cultures: the integration of user-generated content within professional journalistic frame-works at british newspaper websites, Journal. Pract. 2(3), 2008, pp. 343–356.

[31] L. Hlaoua, K. Pinel-Sauvagnat, M. Boughanem, Relevance feedback revisited: dealing with content and structure in XML documents, Int. J. Digit. Libr. 11(1), 2010, pp. 1–24.

[32] S. Hong, Online news on Twitter: newspapers’ social media adoption and their online readership, Inf. Econ. Policy. 24(1), 2012, pp. 69–74.

[33] J.B. Houston, G.J. Hansen, G.S. Nisbett, Influence of user comments on perceptions of media bias and third-person effect in online news, Electron. News. 5(2), 2011, pp. 79–92.

[34] L.R. James, J.M. Brett, Mediators, moderators, and tests for mediation, J. Appl. Psychol. 69(2), 1984, pp. 307–321.

[35] W. Jiang, W. Li, W. Weili, Predicting information popularity degree in microblogging diffusion networks, Int. J. Multimed. Ubiquitous Eng. 9(3), 2014, pp. 21–30.

[36] D.H. Jonassen, K. Beissner, M. Yacci, Structural knowledge:Techniques for representing, conveying, and acquiring structural knowledge, L.Erlbaum Associates, Hillsdale, 1993.

[37] B. Kabanoff, S. Brown, Knowledge structures of prospectors,analyzers, and defenders: Content,structure,stability,and performance, Strateg. Manag. J. 29(2), 2008, pp. 149–171.

[38] R.T. Keller, Technology-information processing fit and the performance of R&D project groups: A test of contingency theory, Acad. Manag. J. 37(1), 1994, pp. 167–179.

[39] H.J. Keselman, A.R. Othman, R. R.Wileox, K. Fradette, The new and improved two-sample t test, Psychol. Sci. 15(1), 2004, pp. 47–51.

[40] P. Korgaonkar, L.D. Wolin, Web usage, advertising, and shopping: Relationship patterns, Internet Res. 12(2), 2002, pp. 191–204.

[41] A. Kothari, W. Magdy, K. Darwish, A. Mourad, A. Taei, Detecting comments on news articles in microblogs, in: Proc. Seventh Int. AAAI Conf. Weblogs Soc. Media, 2013, pp. 293–302.

[42] K. Krippendorff, Content analysis. In E. Barnouw, G. Gerbner, W. Schramm, T.L. Worth, & L. Gross (Eds.), International encyclopedia of communication (1, pp. 403-407). New York, NY: Oxford University Press. 1989.

[43] D. LaBerge, S.J. Samuels, Toward a theory of automatic information processing in reading, Cogn. Psychol. 6(2), 1974, pp. 293–323.

[44] J.R. Landis, G.G. Koch, The measurement of observer agreement for categorical data, Biometrics. 1997, pp. 159–174.

[45] K. Lerman, R. Ghosh, T. Surachawala, Social contagion : An empirical study of information spread on digg and Twitter follower graphs, in: Proc. Fourth Int. AAAI Conf. Weblogs Soc. Media, 2010, pp. 90–97.

[46] Q. Li, J. Wang, Y.P. Chen, Z. Lin, User comments for news recommendation in forum-based social media, Inf. Sci. (Ny). 180(24), 2010, pp. 4929–4939.

[47] H. Lin, W. Fan, P.Y.K. Chau, Determinants of users’ continuance of social networking sites: A self-regulation perspective, Inf. Manag. 51(5), 2014, pp. 595-603.

[48] T. Ma, X. Wan, Opinion target extraction in Chinese news comments, in: Proc. 23rd Int. Conf. Comput. Linguist. Posters, 2010, pp. 1–30.

[49] Z. Ma, A. Sun, G. Cong, Will this #hashtag be popular tomorrow?, in: Proc. 35th Int. ACM SIGIR Conf. Res. Dev. Inf. Retr. - SIGIR ’12, ACM Press, New York, New York, USA, 2012, pp. 1173-1174.

[50] E. Manosevitch, D. Walker, Reader comments to online opinion journalism: A space of public deliberation, Int. Symp. Online Journal. 10, 2009, pp. 1–30.

[51] V. Martha, W. Zhao, X. Xu, A study on Twitter user-follower network a network based analysis, in: 2013 IEEE/ACM Int. Conf. Adv. Soc. Networks Anal. Min., 2013, pp. 1405–1409.

[52] R.M.C. Mccreadie, C. Macdonald, News article ranking : leveraging the wisdom of bloggers, in: Adapt. Pers. Fusion Heterog. Inf., 2010, pp. 40–48.

[53] NetEaseTechnology, User number of NetEase News Client has reached 0.12 billion, Last Accessed http//tech.163.com/13/0709/21/93CEN7TG000915BF.html. 2013.

[54] J. Neter, M.H. Kutner, C.J. Machtsheim, W. Wasseman, Applied linear statistical models, Irwin. Hom, Chicago, 1990.

[55] H. Örnebring, The consumer as producer—of what?, Journal. Stud. 9(5), 2008, pp. 771–785.

[56] J.V. Pavlik, Journalism and new media, New York: Columbia University Press, New York, 2013.

[57] P. a. Pavlou, A. Dimoka, The nature and role of feedback text comments in online marketplaces: implications for trust building, price premiums, and deller differentiation, Inf. Syst. Res. 17(4), 2006, pp. 392–414.

[58] Pew Research Center for the People and the Press, Americans spending more time following the news, http://people–press.org/files/legacy–pdf/652.pdf.2010.

[59] K. Song, D. Wang, S. Feng, G. Yu, Detecting opinion leader dynamically in Chinese news comments, in: Web-Age Inf. Manag. Lect. Notes Comput. Sci., Springer Berlin Heidelberg, 2012, pp. 197–209.

[60] V. a. Stone, J.L. Hoyt, The emergence of source-message orientation as a communication variable, Communic. Res. 1(1), 1974, pp. 89–109.

[61] B. Suh, L. Hong, P. Pirolli, E.H. Chi, Want to be retweeted? Large scale analytics on factors impacting retweet in twitter network, in: 2010 IEEE Second Int. Conf. Soc. Comput., Ieee, 2010, pp. 177–184.

[62] A. Tatar, P. Antoniadis, M.D. De Amorim, S. Fdida, Ranking news articles based on popularity prediction, in: Proc. 2012 Int. Conf. Adv. Soc. Networks Anal. Min. (ASONAM 2012, 2011, pp. 106–110.

[63] A. Tatar, P. Antoniadis, M. Dias, D.A. Serge, From popularity prediction to ranking online news, Soc. Netw. Anal. Min. 4(1), 2014, pp.1–12.

[64] A. Tatar, J. Leguay, P. Antoniadis, A. Limbourg, M.D. de Amorim, S. Fdida, Predicting the popularity of online articles based on user comments, in: Proc. Int.

Conf. Web Intell. Min. Semant. - WIMS ’11, ACM Press, New York, New York, USA, 2011: p.67.

[65] N. Thurman, Forums for citizen journalists ? Adoption of user generated content initiatives by online news media, News Media Soc. 10(1), 2008, pp. 139–157.

[66] M. Tsagkias, M. De Rijke, W. Weerkamp, Linking online news and social media, in: Proc. Fourth ACM Int. Conf. Web Search Data Mining, ACM, 2011, pp. 565-574.

[67] M. Tsagkias, W. Weerkamp, M. de Rijke, Predicting the volume of comments on online news stories, in: Proceeding 18th ACM Conf. Inf. Knowl. Manag. - CIKM ’09, ACM Press, New York, New York, USA, 2009, pp. 1765-1768.

[68] M. Tsagkias, W. Weerkamp, M. De Rijke, News comments : exploring, modeling, and online prediction, in: Adv. Inf. Retr., 2010, pp. 191–203.

[69] J.B. Walther, D. DeAndrea, J. Kim, J.C. Anthony, The influence of online comments on perceptions of antimarijuana public service announcements on YouTube, Hum. Commun. Res. 36(4), 2010, pp. 469–492.

[70] G.A. Wang, J. Jiao, A.S. Abrahams, W. Fan, Z. Zhang, Expert rank: A topic-aware expert finding algorithm for online knowledge communities, Decis. Support Syst. 54(3), 2013, pp. 1442–1451.

[71] J. Waniek, How information organisation affects users’representation of hypertext structure and content, Behav. Inf. Technol. 31(2), 2012, pp. 143–154.

[72] J. Wiebe, E. Riloff, Creating subjective and objective sentence classifiers from unannotated texts, in: Comput. Linguist. Intell. Text Process., 2005, pp. 486–497.

[73] D. Zeng, H. Chen, R. Lusch, S. Li, Social media analytics and intelligence, Intell. Syst. IEEE. 25(6), 2010, pp. 13–16.

[74] L. Zhang, T. Peng, Y. Zhang, X. Wang, Content or context : which carries more weight in predicting popularity of tweets in China, in: Annu. Conf. World Assoc. Public Opin. Res., Hong Kong, 2012, pp. 14–16.

[75] M. Zhou, L. Lei, J. Wang, W. Fan, A.G. Wang, Social media adoption and corporate disclosure, Journal of Information Systems. forthcoming, 2014.

First author： Qian Liu School of Management Xi’an Jiaotong University Email: liuqian00\_china@163.com

Second author：（corresponding author） Mi Zhou School of Management Xi’an Jiaotong University Email : zhoumi@mail.xjtu.edu.cn

Third author：

Xin Zhao

School of Economics and Management

Xi’an University of Technology

Email: zhaoxin\_zzz@163.com
