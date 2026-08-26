---
otero_id: 544
otero_key: "UB3UH6KY"
title: "The Importance of Interactions Between Content Characteristics and Creator Characteristics for Studying Virality in Social Media"
authors: "Yue Han; Theodoros Lappas; Gaurav Sabnis"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0903"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.238.7.40] On: 12 May 2020, At: 11:00 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/UB3UH6KY/fulltext/images/2cadb1b12fbef3750d18a07735757d59e81b5c853a216f29716e428c94533b67.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# The Importance of Interactions Between Content Characteristics and Creator Characteristics for Studying Virality in Social Media

Yue Han, Theodoros Lappas, Gaurav Sabnis

To cite this article: Yue Han, Theodoros Lappas, Gaurav Sabnis (2020) The Importance of Interactions Between Content Characteristics and Creator Characteristics for Studying Virality in Social Media. Information Systems Research

Published online in Articles in Advance 12 May 2020

https://doi.org/10.1287/isre.2019.0903

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Importance of Interactions Between Content Characteristics and Creator Characteristics for Studying Virality in Social Media

Yue Han,<sup>a</sup> Theodoros Lappas,<sup>b</sup> Gaurav Sabnis<sup>b</sup>

<sup>a</sup> Madden School of Business, Le Moyne College, Syracuse, New York 13214; <sup>b</sup> School of Business, Stevens Institute of Technology, Hoboken, New Jersey 07030

Contact: hany@lemoyne.edu, https://orcid.org/0000-0001-6713-4597 (YH); tlappas@stevens.edu, https://orcid.org/0000-0002-4669-4170 (TL); gsabnis@stevens.edu, https://orcid.org/0000-0001-6532-4717 (GS)

Received: October 3, 2017 Revised: October 31, 2018; June 10, 2019 Accepted: September 19, 2019 Published Online in Articles in Advance: May 12, 2020

https://doi.org/10.1287/isre.2019.0903

Copyright: © 2020 INFORMS

Abstract. With the ubiquity of social media usage and influence, the phenomenon of virality—that is, large-scale diffusion and sharing of an online post—has received considerable scrutiny. Research on virality is of primarily two types. Content-based research focuses on how content characteristics influence virality, whereas creator-based research uses characteristics of the creator of the content to study virality. Through this research note, we aim to draw attention toward a relatively ignored set of constructs—the interactions between content characteristics and creator characteristics. We propose a typology of content features and content message on one hand and creator features and creator history on the other. We argue that adding nuanced content–creator interactions to the nomological network for virality will add conceptual richness and improve predictive validity of future studies. We demonstrate this by running models, with and without the interactions, on a data set of nearly 800,000 posts from Twitter. We find that many of these interactions are significant, improve goodness of fit by 20%, provide clues about contextual factors in virality, and boost predictive power by 12%. Our results and subsequent discussions of the findings hope to spur more research on content–creator interactions in understanding virality.

History: Paul A. Pavlou, Senior Editor; Animesh Animesh, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0903.

Keywords: social media • virality • content characteristics • information diffusion

## 1. Introduction

A widely known but little understood phenomenon in social media is something “going viral.” Although there is no universal definition of the phenomenon, it is generally understood to happen when a social media post unexpectedly reaches an unusually large audience, enabled by a large number of users sharing it within their social networks. Once we know something that has gone viral, we can usually intuit what it was about the content or the creator of that content that contributed to the virality. A selfie posted by Ellen DeGeneres featuring a dozen Hollywood stars at the 2014 Academy Awards<sup>1</sup> was the highest shared tweet in history for three years, no doubt helped by the star power of everyone in the picture as well as DeGeneres’ massive following. It was overtaken in retweets in May 2017 by unknown teenager Carter Wilkerson,<sup>2</sup> who posted a screenshot of fast-food chain Wendy’s promising him free chicken nuggets for a year if he got 18 million retweets. The heartwarming and humorous aspect of helping someone get free food was clearly a bigger factor in the tweet’s virality than Wilkerson’s social capital.

The two most viral tweets of all time (as of 2018) differing so starkly in content as well as creator characteristics underline the complexities involved in studying virality in social media. Over the last decade or so, there have been numerous highly cited studies dedicated to studying online diffusion and virality (e.g., Berger and Milkman 2012, Susarla et al. 2012, Goel et al. 2015). These studies have provided profound insights about the antecedents and features of virality, usually focusing on content characteristics or creator characteristics, but rarely both The volume of research that studies the interactions between the two types of characteristics associated with virality is relatively minor.

The primary focus of this research note is to make a case for more research into the many interactions possible between the various types of content characteristics and creator characteristics in the nomological framework for explaining and predicting virality. This is a piece of descriptive research, intended to argue for the importance of content–creator interactions and provide empirical support for how including the interactions leads to greater predictive validity for the underlying constructs.

We are by no means the first to examine content and creator characteristics together while studying diffusion. Son et al. (2013) found evidence for variations in message characteristics in terms of heterogeneity by creator types (firm, news media, or individual). Wu and Wang (2011) found that positive online content about brands with higher source credibility leads to better brand attitudes. The SPIN framework proposed by Mills (2012) to explain virality takes into account both content characteristics and creator characteristics, but without interactions. Hoang and Lim (2012) modeled tweet virality and user virality together and found that their model outperformed previous ones in terms of predicting retweet likelihood. The content characteristics there were defined primarily by use of popular hashtags, whereas creator characteristics were primarily in terms of their ability to get retweets.

Our research note builds on these studies, along with others that focused only on content or creator characteristics, by describing an overall nomological framework for the interactions with a broader scope. We identify 18 content characteristics and classify them into two types: content features (such as the length or use of hashtags, numbering 7) and content message (such as topics or sentiments, numbering 11). We also identify 18 creator characteristics and classify them into two types: creator features (such as age or number of followers, numbering 5) and creator history (such as the propensity to post humor or history of getting retweets, numbering 13). We make a conceptual case for why interactions between these two sets of characteristics may be related to the virality of the posts, and we provide empirical evidence for the same. The motivation of our model is not to claim causality but instead to provide descriptive and predictive support for greater inclusion of content–creator interactions in the study of virality.

Twitter was the data source for our empirical analysis. We collected 2,627 tweets that went “viral” (defined later in Section 3.1) and also collected from the same users almost 800,000 tweets that did not go viral. We measured several content characteristics and creator characteristics of these tweets using a variety of techniques including machine learning. We then ran logistic regression models on these tweets, with and without interactions. We found 50 interactions to be significant, and the model with interactions had a significantly better fit $( R ^ { 2 } = 0 . 3 3 )$ than the model without interactions $( R ^ { 2 } = 0 . 2 7 )$ . The model with interactions also had a noticeably higher predictive power, achieving an accuracy improvement of 12% on out-of-sample data.

Given that we had 50 significant content–creator interactions, it is difficult to describe and explain each of them in detail. But we address a few interesting findings in the discussion section. For example, the interaction between content humor and a creator’s historical propensity to post original content is positive, which suggests that humorous content posted by a creator known to post original content is more likely to go viral—a finding that has face validity.

In addition to drawing attention to the importance of content–creator characteristics in understanding and predicting virality, our research note makes two more contributions. First, the patterns of interactions between content features/message and creator features/history suggest paths for further research delving into the antecedents of virality. Second, firms will get clues for crafting the right kind of message to propagate online depending on their own brand personalities or the characteristics of the social influencers they might want to engage.

The rest of this note is organized as follows. First, we summarize the existing literature on virality as it pertains to content and creator characteristics, and we make the case for the importance of their interactions. Then we describe our data, variables, and model. Next, we present our results with some details on select interactions. We end with a discussion of the implications of the results and directions for further research.

## 2. Conceptual Development

In today’s densely connected world, online information diffusion is growing in leaps and bounds thanks to social media platforms such as blogs, Facebook, Instagram, Reddit, YouTube, and, of course, Twitter. The rapid growth of social media platforms has also resulted in an explosion in the volume of online content an individual is exposed to. Thus, to succeed in using social media as a platform, the key is getting your message to break through the ambient chatter and stand out. Be it Justin Bieber going from an unknown YouTube amateur to a multiplatinum success, or Dollar Shave Club going from an unknown razor delivery start-up to a billion dollar buyout by Unilever, such successes have been built on going viral.

Going viral has not only become a buzzword in popular culture but is also a subject of intense scrutiny among researchers (Gruhl et al. 2004, Hansen et al. 2011, Naveed et al. 2011, Berger and Milkman 2012). Indeed, virality has become a key construct in domains as varied as information systems, marketing, communication studies, sociology, and computer science. In the practitioner world, there is widespread awareness of social media return on investment being tied to virality, be it through corporate social media accounts or by engaging with social influencers (Trusov et al. 2009, Kumar and Mirchandani 2012) The research in this domain is plentiful and varied, and so we summarize only some of its slices relevant to content and creator characteristics.

## 2.1. Content Characteristics

Prior research on online diffusion or virality of social media posts has used content characteristics that can be classified into two types. First are the readily discernible characteristics that a user can gauge almost instantly, such as the length of the post; whether it mentions someone; whether it uses hashtags; whether it has hyperlinks, images, videos, and so on (e.g., Suh et al. 2010, Berger and Milkman 2012, and Malhotra et al. 2013). We classify these objective characteristics as content features. Second are the characteristics of the message that a user has to read or watch to comprehend, such as sentiments, opinions, facts, humor, affective cues, topics, and so on (e.g., Hansen et al. 2011, Molyneux 2015, and Taecharungroj and Nueangjamnong 2015). We classify these partly subjective characteristics as content message. A content message requires more cognitive effort from the reader to comprehend and interpret.

## 2.2. Creator Characteristics

Characteristics of the creator (i.e., the person who posts the message on social media) also have a clear effect on the message’s diffusion and the likelihood of it going viral. Similar to content features, there are some objective creator features that are easily evident to a reader. These include numerical measures of popularity or reach such as followers or friends (e.g., Suh et al. 2010, Li and Du 2011, and Goes et al. 2014) or the number of posts or their frequency (Claussen et al. 2013). Studies have also shown evidence of homophily (Susarla et al. 2012, Weng et al. 2013) in the widespread diffusion of online content. Most users can see display pictures or online bios and readily make a determination about relevant demographic characteristics that have been found to play a role in social contagion, such as race (Sharma 2013, Florini 2014) or age (Correa et al. 2010, Schwartz et al. 2013). We classify these tangible characteristics as creator features.

There are other characteristics of users that are not readily visible at a glance but can be known to their followers or online contacts, leading to reputation, credibility, and certain expectations. Abbasi and Liu (2013) propose using past behavior to measure user credibility. Ho and Dempsey (2010) found that individualism and altruism are significant predictors for virality. Liu et al. (2012) found that the creator’s trustworthiness, expertise, and attractiveness have a significant impact on diffusion. Westerman et al. (2014) found that source credibility online was positively related to cognitive elaboration by users, and it follows that the longer a user has been exposed to a creator’s posts, the better that user will be able to gauge credibility. Even going beyond credibility or trustworthiness, creators consciously put efforts into a presentation of their selves (Hogan 2010) in terms of the kind of content they post. These characteristics can only be gauged by users over a longer period of time and thus we classify them as creator history.

## 2.3. The Case for Content–Creator Interactions

We are hardly the first to think of how online diffusion in general and virality in particular will be affected by not only the content and the creator but also which creator is posting which content. All of us have at least one gullible friend or relative who has a history of posting rumors or conspiracy theories online and whose rantings we will ignore. But if an unusual piece of information comes from someone we deem credible, we are likely to share it with others. There have been multiple studies about the role source credibility plays in information diffusion during crises (e.g., Acar and Muraki 2011 and Utz et al. 2013). Wu and Wang (2011) found that in the context of brands, positive word-of-mouth has a higher online diffusion when the sources are deemed to have higher credibility. Son et al. (2013) tested the effects of six different content characteristics on diffusion and found that the effects were moderated by whether the creator is an individual, a firm, or a media entity. Hoang and Lim (2012) defined content virality and creator virality in terms of the diffusion observed, and they tested their interaction in the context of a network of users during elections in Singapore and popular hashtags. They, however, did not collect detailed creator character istics and, for content, only studied the virality of hashtags.

We find the aforementioned studies useful and valid, and we propose the need for expanding the scope of the phenomenon beyond just credibility, crisis settings, or brand setting. We also argue for a more nuanced and detailed typology of characteristics underlying both content and creator, as well as the variety of interactions possible. The highest retweeted tweet in history that we mentioned at the beginning of the paper is a case in point. Somehow, the idea of helping an unknown teenager get free chicken from a large corporation appealed to millions of people. The creator feature of age may have played a role in how the content message of getting free chicken and the content feature of including a message led to this tweet going viral. We humbly submit that a similar request from an unknown middleaged corporate executive might not have yielded the same viral response. Similarly, a tweet posted without the screenshot of Wendy’s promising free chicken might not have gone viral. It is important for us to understand how individual-level characteristics of content creators play a role in what kind of content posted by them gains traction.

Although race and gender disparities have been around for decades, recent activist movements launched online such as #BlackLivesMatter, #MeToo, and #TimesUp may have reached a wider audience because they gave millions of those in affected groups the narrative agency to shape and disseminate the message (Yang 2016). In other words, creator features, such as race or gender, and creator history, such as the creator’s past online activism, interacted with the content message about racism or misogyny and possibly with content features such as whether he or she showed images or videos that pertained to relevant news articles about police brutality or sexual harassment.

A tragic example of the content–creator interplay was seen in the immediate aftermath of the Boston Marathon bombing in 2012, when the Tripathi family was harassed because misinformation about their son being a bomber went viral (Madrigal 2013). After surveillance footage of the bombers was posted online by the Federal Bureau of Investigation (FBI), individuals on Reddit started efforts to identify them, with several names and theories being discussed. A “Redditor” (registered Reddit user) misidentified one of the bombers as Sunil Tripathi, a Brown University student who had been reported missing for a month (and was later found to have committed suicide for unrelated reasons). BuzzFeed’s Andrew Kaczynski saw this on Reddit and decided to tweet it out to his large number of followers, and suddenly this rumor went viral and was even reported in the mainstream media. The Tripathi family received death threats for days, although the record was set straight by the FBI and other authorities very soon after, making it clear that Sunil Tripathi was not a suspect. If Kaczynski, who had a reputation of a reliable “new media” journalist plugged into online sources, had not tweeted out the rumor, it likely would have stayed confined to a few hundred people on Reddit. In this case, it was not just Kaczynski’s high follower count but also his history of providing scoops gleaned from online sources that interacted with the notable content message that a terrorist had supposedly been identified.

These well-known news stories are just three of many that demonstrate how it is not just content alone and creator alone but a specific combination of their characteristics that seems to be related to virality. Although research papers explicitly addressing the interaction effects are few, there are results on the sidelines from highly cited papers on the contentvirality and creator-virality main effects that provide support for our contention about the need to expand the nomological framework in this domain.

Our proposed nomological framework is depicted in Figure 1.

Goel et al. (2015) found that structural virality differed considerably across videos, images, news articles, and so on (content features), and that these cascades were strongly related to the popularity of those who posted them (creator features). Susarla et al. (2012), studying virality on YouTube, found support for interactions between video age (content feature) and the centrality and nonlocal friend counts (creator features) for those who posted the videos. Zeng and Wei (2013) found that on Flickr, the relationship between content message and the ties of those who post the content is influenced by creator features as well as creator history. Bakshy et al. (2011) found that, in quantifying influencers on Twitter, the efficacy of using someone with a large number of followers or a moderate number of followers (creator features) is dependent on the context of the message being disseminated.

In sum, it is our contention that, in understanding and predicting which content goes viral, content features, which are easily discernible, and the content message, which is subjective and requires cognitive effort, are known to have a relationship with virality. Moreover, we contend that the relationship between virality and content features varies significantly with creator features, which are easily discernible, and creator history, which is built and observed over time. And it is our assertion that including these content–creator interactions in the study of virality will yield better predictive power as well as a better understanding of the phenomenon.

## 3. Data and Model Development

In this section, we describe how our research question motivated our selection of the data context and the model.

## 3.1. Data Motivation

We chose Twitter as the context for our study, because it is universally regarded as an influential medium for social issues, businesses, entertainment, politics, and almost every context imaginable. We treat the number of retweets (RTs) as the measure of virality. Virality is easy to identify, but there is no universal agreement on how it should be quantified. The two commonly agreed-upon features of virality are that (1) it is characterized by a volume of widespread diffusion and (2) it should be an unusual spike in diffusion.

So the key questions for us were, how many RTs qualify for virality, and what counts as an unusual spike? Almost every tweet by Lady Gaga or Cristiano Ronaldo or Elon Musk gets thousands of RTs, so every tweet of theirs qualifies on the volume front, but it is not unusual. On the other hand, a thousand RTs from an account that never before had even—say, 10— could be argued to have gone viral.

Figure 1. Nomological Framework for Content and Creator Interactions  
![](/api/attachments/UB3UH6KY/fulltext/images/ab96b46c0baa511e8d3e1ae1d482b0fed239a2357b463ec50fd989e08ee00ea8.jpg)

As a pretest to come up with quantifiable metrics for virality, we collected all tweets retweeted by the account @kalesalad, a former Buzzfeed employee whose bio says, “I retweet the greatest tweets on twitter” (Chen 2017). The account has more than 180,000 followers on Twitter and over 2.5 million on Instagram. @kalesalad has been repeatedly cited as a source of viral tweets in mainstream media (Sommerlad 2018). The account has been mentioned in hundreds of news stories on platforms that cover social media, such as Buzzfeed, Mashable, and Vogue (Chen 2017, Read 2018, Sung 2018).

In that data set, to quantify what counts as an “unusual” spike in RTs for a user, we compared RTs for a tweet with the average number of RTs for all other tweets by that user that the Twitter search engine allowed us to collect. We found the viral tweets to be approximately at least two standard deviations above the mean for a user. Next, we assessed the lower cutoff for RTs in the data set and found it to be about 5,000. Thus, we decided to consider a tweet as viral if (1) it has a number of RTs that is at least two standard deviations above the mean for its creator, and (2) the tweet has at least 5,000 RTs. We also carried out robustness checks in where we relaxed these criteria, with ranges of 1.75–2.25 standard deviations and 4,000–6,000 RTs, and our results did not change much.

Given these two criteria, we discarded the Kale Salad data set, to avoid bias likely to be introduced by what that one person considers as viral. For our actual regression analysis, we collected tweets using Twitter’s “min\_retweets:number” search feature, specifying 5,000 as the minimum retweet number. We then filtered out tweets that did not satisfy the unusualness criterion in terms of two standard deviations from the user’s average retweets. So even if a celebrity has 7,000 RTs on a tweet, it was not included in our data set if it did not fall above two standard deviations from the mean for the celebrity For each user that had a viral tweet, we also recovered the user’s full tweet history, as far back as permitted, via the Twitter API. This yielded 2,627 viral tweets and a further 797,316 nonviral tweets from the same users’ histories, leading to a total 799,943 tweets. A sample of our viral tweets, as well as corresponding nonviral tweets from the same user, is in Figure 2.

## 3.2. Measures

The dependent variable is virality as measured in the previous section. Thus if a tweet is viral, satisfying the two criteria, it is designated as 1; if it does not, it is designated as 0. Having viral and nonviral tweets from the same users gives us a context that allows us to estimate the interactions between content and creator characteristics. The average number of RTs for a viral tweet was 63,385.3 and for nonviral tweets was 750.6.

Figure 2. (Color online) Examples of Viral Tweets and Nonviral Tweets  
![](/api/attachments/UB3UH6KY/fulltext/images/581cd114f061c2bee8ab07181bb5461946da7ddb92fbcad825dda99774a2388c.jpg)

As content features, we used objective characteristics used in virality research previously—namely, the length of the tweet in characters and binary variables for the use of hashtags, images, videos, quote RTs, mentions, and web links.

For content message, we used latent Dirichlet allocation (LDA; Blei et al. 2003) on the text of the tweets and their replies to get the topic models. Although a tweet by itself, often containing just a short line or an image or video, might not yield enough information to classify it, the many replies to it have enough words to give an indication about the topic. For instance, someone might tweet a humorous image, and that tweet by itself might not have enough content to objectively gauge what it is about. But if it is perceived as humorous by a large number of readers, the replies are likely to be dominated by text such as “Haha,” “LOL,” and “Funny!,” for example. Thus, analyzing the text of replies can give us a proxy for what the topic content of the tweet was.

The LDA model was trained on the full set of replies for each of the tweets in our data set. After experimenting with K of topic count in the range of 20–200, we used the established perplexity measure (Blei et al. 2003, Asuncion et al. 2009) to choose K = 100 topics. As is common in LDA analysis, we then manually studied the term distribution in each topic to assign a label to the topic (Wang et al. 2013). Of 100 topics, 11 were labeled as “politics,” 35 as “pop culture,” 6 as “sports,” 1 as “profanity,” 3 as “humor,” 4 as “emotional,” 2 as “animals,” 1 as “family,” 2 as “relationships,” 18 as “noise,” 2 as “books,” 2 as “non-English,” 1 as “health,” 1 as “clothing,” 2 as “science,” 3 as “food,” 1 as “gaming,” 2 as “wishes” (birthday, holidays, etc.), 1 as “religion,” 1 as “technology,” and 1 as “school”

We omitted non-English tweets from our data set. The topics of noise, books, health, clothing, science, food, gaming, wishes, religion, technology, and school were also omitted from our final model because they covered a trivial percentage (less than 0.5%) of tweet content and were never reported as the dominant topic for a tweet. Running the model with or without these topics yielded no significant change in the other coefficients. Thus, we have nine topics for content message, which, for every tweet, were measured as the proportion of words pertaining to that topic. In line with previous research on the importance of valence, we also included the count of positive and negative words using the NRC Emotion Lexicon (Mohammad and Turney 2013).

We measured creator features studied previously in the literature—namely, the number of followers the creator has as a measure of popularity, the number of users the creator is following as a measure of gregariousness, and the number of tweets the creator has as a measure of platform experience. We also identified Age and Race as categorical variables using agreement among three independent raters who looked at the bio and display pictures of each creator in our data set.<sup>3</sup>

For creator history, we measured the proportion of words corresponding to the topics in the content message as a proxy for the creator’s propensity to tweet about those topics. We also measured the average length of past tweets (as a proxy for propensity for verbosity), the average RTs received by the user in the past (as a proxy for history of virality), and what percentage of previous tweets were original content, versus retweets or replies. Descriptive statistics for all variables are given in Table 1.

To control for other factors that could have an impact of virality, we used the time lag between the viral tweet and the user’s previous tweet (as a proxy for recency), as well as weekday, date, month, and year variables to account for temporal effects.

## 3.3. Model Description and Robustness Checks

As described in Section 3.1 and 3.2, we came up with a binary measure for virality based on the minimum number of retweets (5,000 plus) and the retweets being at least two standard deviations from the creator’s average retweets. Of nearly 800,000 tweets, only 2,627 are viral, which is 0.33%, a number that was yielded by the data after combining viral and nonviral tweets for the users. Given how few posts on social media go viral, this small percentage certainly has face validity. Considering the binary nature of our dependent variable, we used a standard logit model (Greene 2017) with robust standard errors given the variety of categorical and continuous variables in our data set. The model corrects for intragroup correlation, which is a concern for our variables. We ran the model without and with interactions, yielding a noticeable improvement in goodness of fit as well as predictive validity. We validated our results using multiple nonlinear classification algorithms (random forest, support vector machine, multinomial na¨ıve Bayes, and k-nearest neighbors) and included the results in the online appendix. The findings and trends are consistent across algorithms: adding the interactions consistently results in predictive accuracy. Our content message and creator history variables are defined as proportions, so as not to pigeonhole the tweet and its user into just one topic. However, we also ran a model classifying them as categorical variables, assigning the respective topics with the highest proportion to both content and creator. Our results were consistent. We also addressed possible multicollinearity concerns by computing the variance inflation scores for our logistic model. The results are also included in the online appendix

Table 1. Variable Description and Summary Statistics

<table><tr><td>Category</td><td>Variable</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td rowspan="7">Content  $features^a$ </td><td>Length</td><td>99.555</td><td>55.154</td><td>0</td><td>280</td></tr><tr><td>Hashtag</td><td>0.087</td><td>0.282</td><td>0</td><td>1</td></tr><tr><td>Image</td><td>0.269</td><td>0.443</td><td>0</td><td>1</td></tr><tr><td>Video</td><td>0.05</td><td>0.218</td><td>0</td><td>1</td></tr><tr><td>QuoteRT</td><td>0.113</td><td>0.317</td><td>0</td><td>1</td></tr><tr><td>Mention</td><td>0.111</td><td>0.314</td><td>0</td><td>1</td></tr><tr><td>Link</td><td>0.226</td><td>0.418</td><td>0</td><td>1</td></tr><tr><td rowspan="11"> $Content\ \( message^b$ </td><td>M_Positive</td><td>0.942</td><td>1.102</td><td>0</td><td>7</td></tr><tr><td>M_Negative</td><td>0.502</td><td>0.834</td><td>0</td><td>7</td></tr><tr><td>M_Profane</td><td>0.016</td><td>0.067</td><td>0</td><td>0.815</td></tr><tr><td>M_Humor</td><td>0.025</td><td>0.08</td><td>0</td><td>0.977</td></tr><tr><td>M_Family</td><td>0.006</td><td>0.038</td><td>0</td><td>0.953</td></tr><tr><td>M_Pop</td><td>0.128</td><td>0.185</td><td>0</td><td>0.988</td></tr><tr><td>M_Politic</td><td>0.049</td><td>0.128</td><td>0</td><td>0.981</td></tr><tr><td>M_Sports</td><td>0.022</td><td>0.09</td><td>0</td><td>0.977</td></tr><tr><td>M_Relation</td><td>0.013</td><td>0.058</td><td>0</td><td>0.907</td></tr><tr><td>M_Animal</td><td>0.014</td><td>0.063</td><td>0</td><td>0.971</td></tr><tr><td>M Emotion</td><td>0.036</td><td>0.1</td><td>0</td><td>0.971</td></tr><tr><td rowspan="5"> $Creator\ \( features^c$ </td><td>Age</td><td colspan="4">Young: 65.34%Middle aged: 10.47%Old: 2.25%Other/unknown: 21.94%</td></tr><tr><td>TweetVolume</td><td>7.982</td><td>0.294</td><td>1.099</td><td>8.087</td></tr><tr><td>Followers</td><td>10.001</td><td>3.034</td><td>2.197</td><td>18.296</td></tr><tr><td>Following</td><td>6.433</td><td>1.366</td><td>0</td><td>12.866</td></tr><tr><td>Race</td><td colspan="4">Asian: 2.79%Black: 11.43%White: 74.84%Other: 10.95%</td></tr><tr><td rowspan="13"> $Creator\ \( history^d$ </td><td>H_Length</td><td>99.555</td><td>27.196</td><td>28.526</td><td>247.858</td></tr><tr><td>H_Viral</td><td>4.755</td><td>1.805</td><td>0.02</td><td>10.973</td></tr><tr><td>H_RT</td><td>0.229</td><td>0.149</td><td>0</td><td>0.892</td></tr><tr><td>H_Original</td><td>0.177</td><td>0.129</td><td>0</td><td>0.903</td></tr><tr><td>H_Profane</td><td>0.067</td><td>0.087</td><td>0</td><td>1</td></tr><tr><td>H_Humor</td><td>0.118</td><td>0.082</td><td>0</td><td>0.805</td></tr><tr><td>H_Family</td><td>0.031</td><td>0.027</td><td>0</td><td>0.5</td></tr><tr><td>H_Pop</td><td>0.564</td><td>0.299</td><td>0</td><td>1.973</td></tr><tr><td>H_Politic</td><td>0.225</td><td>0.24</td><td>0</td><td>2.217</td></tr><tr><td>H_Sports</td><td>0.09</td><td>0.131</td><td>0</td><td>1.304</td></tr><tr><td>H_Relation</td><td>0.062</td><td>0.042</td><td>0</td><td>1</td></tr><tr><td>H_Animal</td><td>0.062</td><td>0.07</td><td>0</td><td>1</td></tr><tr><td>H Emotion</td><td>0.165</td><td>0.151</td><td>0</td><td>1.098</td></tr></table>

<sup>a</sup>Length of a tweet is measured in characters; all other features are binary.  
<sup>b</sup>M\_Positive and M\_Negative are counts of word valence. All other variables are the proportion of words with those topics.  
<sup>c</sup>TweetVolume, Followers, and Following are logged as a result of overdispersion.  
<sup>d</sup>H\_Length is the mean of past tweets in characters. H\_Viral is the log of RTs received by the user previously. All other variables are proportions of words in previous tweet with those topics.

As this research note is focused on a descriptive and predictive contribution, not a methodological one, we have kept the model relatively simple. However, our results are largely consistent even when we use more sophisticated models such as negative binomial or zero-inflated Poisson on the actual RT counts. The added benefit of including content–creator interactions is robust across all models.

## 4. Results

We first ran the logit model without interactions and then with interactions. We have 18 content variables, 18 creator variables, and a large number of categorical control variables for temporal effects, so just the number of main effect coefficients is close to 100. Add the interaction effects, and we have over 400 rows in the full results table. Given the space constraints, we have put the full results table in the online appendix and will summarize the main findings here.

The McFadden’s R<sup>2</sup> goodness of fit improved from 0.27 to 0.33 when interactions were included. Furthermore, adding the interactions led to a 12% increase in the model’s predictive accuracy. This is the mean improved achieved over 100 bootstrapped samples. For each sample, we used 75% of the data for testing and 25% for training. We repeat the process for the model with and without interactions. The corresponding mean accuracies were 83% and 71%. The standard deviations were equal to 2% and 6%, respectively.

With 18 content variables and 18 creator variables, there are 324 possible interaction coefficients, of which 51 were statistically significant. However, bear in mind that whereas we use proportions for topics in the content message and creator history to avoid pigeonholing them, realistically, not every topic is likely to play a role in every tweet. Thus practically speaking, there are 2 content message variables (topic and valence) in addition to the 7 content features and 4 creator history variables (topic, average length of past tweets, retweet history, and propensity for original content), in addition to the 5 creator features— which makes the 50 interactions we found to be a respectable number.

For ease in interpretation of the interaction results, we present them as four matrices in Table 2—content features/message × creator features/history. The second row and column in each matrix denotes the main effects. The remaining cells indicate the interaction coefficients for the two variables. If a cell is blank, it was not significant. If a cell is coded $^ { \prime \prime } { + + ^ { \prime \prime } }$ (“<sup>− −</sup>”), the coefficient was significant (with p < 0.05) and positive (negative). Readers interested in the numerical coefficients can access the full table in the online appendix.

The presence of over four dozen interactions, when taken with the notable improvements in the goodness of fit and predictive accuracy, provide empirical evidence in support of our central argument. Space constraints prohibit discussing each of the interactions in detail. However, we provide a brief summary.

Among the content feature and creator feature interactions (Table 2, panel A), it was interactions with creator followers that were most notable. These coefficients were negative for the content length and presence of a video but positive for mentions. Having a mention indicates a reply, and it makes sense that the main effect for it would be negative, as other readers might not be interested in those conversations. However, the follower–mention interaction being positive is an interesting result. Someone with a high follower count including a mention in a tweet might be replying to a fan, and that seems to have a positive relationship with virality.

Interactions between content features and creator history (Table 2, panel B) show the most interactions for whether the tweet includes an image and whether a tweet includes a video. For both those content features, the creator’s length history has a negative interaction, whereas the creator’s history of posting original content has a positive interaction. This suggests that someone that readers perceive as having a history of posting original content is more likely to have his or her image or video tweet shared. This makes sense, as visual content perceived to be original is likely to intrigue readers enough to share it.

Panel A: Content Features × Creator Features  
Table 2. Interaction Matrices

<table><tr><td colspan="14">Panel A: Content Features × Creator Features</td><td></td></tr><tr><td></td><td>Creator</td><td colspan="2">Age: middle-aged</td><td>Age: old</td><td>Age: young</td><td>TweetVolume</td><td>Followers</td><td>Following</td><td>Race: Asian</td><td>Race: Black</td><td>Race: White</td><td></td><td></td><td></td></tr><tr><td>Content</td><td>Main effects</td><td colspan="2">++</td><td></td><td></td><td>--</td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td></tr><tr><td>Length</td><td>++</td><td></td><td></td><td></td><td></td><td></td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Hashtag</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Image</td><td>++</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Video</td><td>++</td><td></td><td></td><td></td><td></td><td></td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>QuoteRT</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mention</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td>++</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Link</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="14">Panel B: Content Features × Creator History</td><td></td></tr><tr><td></td><td>Creator</td><td>H_Length</td><td>H_Viral</td><td>H_RT</td><td>H_Original</td><td>H_Profane</td><td>H_Humor</td><td>H_Family</td><td>H_Pop</td><td>H_Politic</td><td>H_Sports</td><td>H_Relation</td><td>H_Animal</td><td>H_Emotion</td></tr><tr><td>Content</td><td>Main effects</td><td></td><td>++</td><td></td><td>++</td><td>--</td><td>--</td><td>--</td><td></td><td></td><td>--</td><td>--</td><td></td><td></td></tr><tr><td>Length</td><td>++</td><td>--</td><td></td><td></td><td></td><td></td><td>--</td><td></td><td>++</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Hashtag</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Image</td><td>++</td><td>--</td><td>--</td><td>++</td><td>++</td><td>++</td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td></tr><tr><td>Video</td><td>++</td><td>--</td><td></td><td></td><td>++</td><td>++</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>QuoteRT</td><td></td><td></td><td>++</td><td></td><td></td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mention</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Link</td><td>--</td><td></td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="14">Panel C: Content Message × Creator Features</td><td></td></tr><tr><td></td><td>Creator</td><td colspan="2">Age: middle-aged</td><td>Age: old</td><td>Age: young</td><td>TweetVolume</td><td>Followers</td><td>Following_log</td><td>Race: Asian</td><td>Race: Black</td><td>Race: White</td><td></td><td></td><td></td></tr><tr><td>Content</td><td>Main effects</td><td colspan="2">++</td><td></td><td></td><td>--</td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td></tr><tr><td>M_Positive</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Negative</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Profane</td><td></td><td></td><td></td><td></td><td></td><td>----</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Humor</td><td>++</td><td></td><td></td><td></td><td></td><td></td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Family</td><td>++</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Pop</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Politic</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Sports</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Relation</td><td>++</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Animal</td><td>++</td><td></td><td></td><td></td><td></td><td></td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Emotion</td><td>++</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="15">Panel D: Content Message × Creator History</td></tr><tr><td rowspan="2">Content</td><td>Creator</td><td>H_Length</td><td>H_Viral</td><td>H_RT</td><td>H_Original</td><td>H_Profane</td><td>H_Humor</td><td>H_Family</td><td>H_Pop</td><td>H_Politic</td><td>H_Sports</td><td>H_Relation</td><td>H_Animal</td><td>H_Emotion</td></tr><tr><td>Main effects</td><td></td><td>++</td><td></td><td>++</td><td>--</td><td>--</td><td>--</td><td></td><td></td><td></td><td>--</td><td>--</td><td></td></tr><tr><td>M_Positive</td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Negative</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Profane</td><td></td><td>--</td><td>--</td><td>--</td><td></td><td>++</td><td>--</td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td></tr><tr><td>M_Humor</td><td>++</td><td>--</td><td></td><td></td><td>++</td><td></td><td>--</td><td></td><td></td><td>--</td><td>++</td><td></td><td></td><td></td></tr><tr><td>M_Family</td><td>++</td><td></td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Pop</td><td></td><td></td><td></td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Politic</td><td></td><td>--</td><td></td><td>--</td><td></td><td></td><td></td><td></td><td>--</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Sports</td><td>--</td><td></td><td>----</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Relation</td><td>++</td><td>--</td><td></td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Animal</td><td>++</td><td></td><td></td><td>--</td><td>--</td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M_Emotion</td><td>++</td><td></td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td>++</td><td></td><td></td><td></td><td></td></tr></table>

Table 2.
(Continued)

Interactions between content message and creator features (Table 2, panel C) again show interactions with creator followers to be most of the significant ones. It shows negative interactions with profanity, humor, and animals in the content message but a positive interaction with sports. Interactions between the content message and the creator history (Table 2, panel D) deliver the most numerous and interesting results. Not every kind of content message will have a significant interaction with every kind of creator. Profanity and humor, two frequent features in tweets, have the highest number of interactions with creator history.

These results are varied in nature, but the consistencies in the patterns of the interactions further underline the need for more research into these phenomena.

## 5. Discussion and Conclusion

The primary objective of this research note is to provide arguments and evidence for the importance of interactions between content and creator in understanding virality. We would like to spur more research in understanding what type of content by what type of creator goes viral. We classified content characteristics as features, which are readily discernible, and message, which is somewhat subjective and contextual. We classified creator characteristics as features, also readily discernible, and history, which gives an indication of the users’ propensity to post topics and the manner in which they make posts. Defining virality as a binary variable, we found that including interactions significantly improves the goodness of fit (by 20%) as well as the predictive validity (by 12%). These results by themselves provide evidence in support of fulfilling our primary objective.

Furthermore, the variety of interactions we found between content and creator characteristics offers insights into how to build on this work. We used LDA topic modeling to come up with nuanced measures for the content message and the creator history. The idea behind this approach was the intuition that the virality of a content message could be related to the creator of the message. We now further discuss some interactions and what they imply. Even though the following are not claims of causality, there are enough such interactions in our results with face validity that can offer clues for deeper study of the contextual antecedents of virality.

For example, a tweet being emotional by itself seems to have no significant relationship with virality as a main effect. However, the interaction coefficient show that if the content is emotional and is also posted by an account with a history of posting about politics, there is a positive relationship with virality. Given the contentious and polarized nature of the political discourse in the last couple of years, with Brexit, Black Lives Matter, and immigration issues, among others, it is understandable why accounts that are politicsheavy posting emotional tweets seem to see virality.

Humor has long been understood to be related to the online diffusion of a post (e.g., Highfield 2015 and Ge et al. 2018), as borne out by the positive significant main effect. However, the interactions suggest that tweet length history of the creator has a negative interaction with tweet humor, in line with Shakespeare’s observation that brevity is the soul of wit. On the other hand, a creator’s historic propensity to post original content (as opposed to RTs or replies) has a positive interaction coefficient with content humor, which suggests that perhaps people are more likely to retweet content from users who they think came up with a joke themselves.

Profanity is generally off-putting to people, but it seems to have a positive interaction with a history of profanity, suggesting that the propensity to be profane might get baked into readers’ reactions to it. It also has a positive interaction with the history of posting about sports, which also has face validity, because sports is one of the few contexts where expressing disappointment or joy using profanity seems to have social acceptability. The history of tweet length also has negative interactions with the tweet message being about politics or relationships. This suggests that someone with a propensity to be prolix might not get the best responses to long tweets or even threads complaining about politics or their personal lives.

Whereas our results provide some clues to academic researchers for how to further the study of content–creator interactions, they also have practical implications. Most businesses today, large and small, are spending resources on using social media popularity for marketing and brand building. This includes shaping corporate social media accounts with voices distinct from their competitors to stand out. For example, Wendy’s carefully curated Twitter account is known for its irreverent and edgy voice, using humor and the occasional profanity to take digs at competitors as well as to “roast” complaining customers (Whitten 2018). On the other hand, Chick-Fil-A employs a friendly, wholesome, and family-oriented approach on their social media platforms (Salo 2016). Our findings on how creator history interacts with content characteristics can help social media managers crafting their strategies to pick their brand voice and their content accordingly.

Another widely used social media strategy by businesses involves compensating some active and popular creators, or “social influencers,” to endorse and recommend their products or services (Booth and Matic 2011, Li et al. 2011). Our topology of content and creator characteristics as well as our interactions can help social media managers in choosing which social influencers to engage with and what kind of content to seed in these networks.

There are a few limitations to our study that we acknowledge. Although we have been able to empirically demonstrate the descriptive validity and the predictive power of incorporating content–creator interactions in studying virality, our study neither aims to nor provides causal findings. Also, given the nature and the space constraints of a research note, it cannot provide detailed theoretical explanations for all the interactions we found to be significant. We hope that further research can build on these avenues.

Our results, although conducted in the context of Twitter, should have some generalizable implications for other social media platforms too. Almost all our content message and content history variables can be used and tested in the context of Facebook, Instagram, and so on. Especially for Instagram, where the content is exclusively visual, the interactions between content message and creator history should be interesting in predicting virality. Facebook, with the recent concerns over Russian bots planting fake news stories to influence elections, could particularly benefit by understanding the content–creator dynamics.

The path forward for social media strategy involves more detailed study of the various underlying features that lead to diffusion. Understanding the antecedents of virality is akin to solving a 1,000-piece jigsaw puzzle. The aim of this research note is to add to the crucial corner pieces by underlining the interactions between the content and creator. We hope our findings will encourage researchers to put more pieces in place as we all strive toward a complete picture of virality.

## Endnotes

<sup>1</sup> See https://twitter.com/TheEllenShow/status/440322224407314432/ photo/1.

<sup>2</sup> See https://twitter.com/carterjwm/status/849813577770778624 photo/1.

<sup>3</sup> We tried to identify gender as well, but it did not yield sufficient interrater reliability, so we did not include the variable in our model.

## References

Abbasi MA, Liu H (2013) Measuring user credibility in social media. Greenberg AM, Kennedy WG, Bos ND, eds. Internat. Conf. Soc. Comput. Behav.-Cultural Model. Prediction (Springer, Berlin), 441–448.

Acar A, Muraki Y (2011) Twitter for crisis communication: Lessons learned from Japan’s tsunami disaster. Internat. J. Web Based Comm. 7(3):392–402.

Asuncion A, Welling M, Smyth P, Teh YW (2009) On smoothing and inference for topic models. Bilmes J, Ng A, eds. Proc. 25th

Conf. Uncertainty Artificial Intelligence (AUAI Press, Arlington, VA), 27–34.

Bakshy E, Hofman JM, Mason WA, Watts DJ (2011) Everyone’s an influencer: Quantifying influence on Twitter. Proc. 4th ACM Internat. Conf. Web Search Data Mining (ACM, New York), 65–74.

Berger J, Milkman KL (2012) What makes online content viral? J. Marketing Res. 49(2):192–205.

Blei DM, Ng AY, Jordan MI (2003) Latent Dirichlet allocation. J. Machine Learn. Res. 3(January):993–1022.

Booth N, Matic JA (2011) Mapping and leveraging influencers in social media to shape corporate brand perceptions. Corporate Comm. 16(3):184–191.

Chen T (2017) This woman’s allegedly stolen tweet became a bizarre “Parrot-Ghazi” scandal and now she’s speaking out. BuzzFeed News (March 28), https://www.buzzfeednews.com/article/ tanyachen/parrotghazi.

Claussen J, Kretschmer T, Mayrhofer P (2013) The effects of rewarding user engagement: The case of Facebook apps. Inform. Systems Res. 24(1):186–200.

Correa T, Hinsley AW, de Zuñiga HG (2010) Who interacts on the Web?: The intersection of users’ personality and social media use. Comput. Human Behav. 26(2):247–253.

Florini S (2014) Tweets, tweeps, and signifyin’ communication and cultural performance on “black Twitter.” TV New Media 15(3): 223–237.

Ge J, Gretzel U, Zhu Y (2018) Humour in firm-initiated social media conversations: A conceptual model. Internat. J. Digital Cultural Electronic Tourism 2(4):273–293.

Goel S, Anderson A, Hofman J, Watts DJ (2015) The structural virality of online diffusion. Management Sci. 62(1):180–196.

Goes PB, Lin M, Au Yeung C (2014) “Popularity effect” in usergenerated content: Evidence from online product reviews. In form. Systems Res. 25(2):222–238.

Greene WH (2017) Econometric Analysis. 8th ed. (Pearson, Upper Saddle River, NJ).

Gruhl D, Guha R, Liben-Nowell D, Tomkins A (2004) Information diffusion through blogspace. Proc. 13th Internat. Conf. World Wide Web (ACM, New York), 491–501.

Hansen LK, Arvidsson A, Nielsen FA, Colleoni E, Etter M (2011)<sup>˚</sup> Good friends, bad news-affect and virality in Twitter. Park JJ, Yang LT, Lee C, eds. Future Information Technology (Springer, Berlin), 34–43.

Highfield T (2015) Tweeted joke lifespans and appropriated punch lines: Practices around topical humor on social media. Internat. J. Comm. 9(2015):2713–2734.

Ho JY, Dempsey M (2010) Viral marketing: Motivations to forward online content. J. Bus. Res. 63(9–10):1000–1006.

Hoang T-A, Lim EP (2012) Virality and susceptibility in information diffusions. Proc. 6th Internat. AAAI Conf. Weblogs Soc. Media (AAAI Press, Palo Alto, CA), 146–153.

Hogan B (2010) The presentation of self in the age of social media: Distinguishing performances and exhibitions online. Bull. Sci. Tech. Soc. 30(6):377–386.

Kumar V, Mirchandani R (2012) Increasing the ROI of social media marketing. MIT Sloan Management Rev. 54(1):55–61.

Li F, Du TC (2011) Who is talking? An ontology-based opinion leader identification framework for word-of-mouth marketing in online social blogs. Decision Support Systems 51(1): 190–197.

Li YM, Lai CY, Chen CW (2011) Discovering influencers for marketing in the blogosphere. Inform. Sci. 181(23):5143–5157.

Liu Z, Liu L, Li H (2012) Determinants of information retweeting in microblogging. Internet Res. 22(4):443–466.

Madrigal AC (2013) #BostonBombing: The anatomy of a misinformation disaster. The Atlantic (April 19), https://www.theatlantic .com/technology/archive/2013/04/-bostonbombing-the -anatomy-of-a-misinformation-disaster/275155/.

Malhotra A, Malhotra CK, See A (2013) How to create brand engagement on Facebook. MIT Sloan Management Rev. 54(2):18–20.

Mills AJ (2012) Virality in social media: The SPIN framework. J. Public Affairs 12(2):162–169.

Mohammad SM, Turney PD (2013) Crowdsourcing a word-emotion association lexicon. Comput. Intelligence 29(3):436–465.

Molyneux L (2015) What journalists retweet: Opinion, humor, and brand development on Twitter. Journalism 16(7):920–935.

Naveed N, Gottron T, Kunegis J, Alhadi AC (2011) Bad news travel fast: A content-based analysis of interestingness on Twitter. Proc. 3rd Internat. Web Sci. Conf. (ACM, New York), Article 8.

Read B (2018) Here’s why you keep seeing certain Instagram commenters over others. Vogue (May 4), https://www.vogue.com article/how-instagram-comments-work.

Salo J (2016) How Chick-Fil-A’s social media marketing translated into Twitter, Facebook and Instagram success. International Business Times (January 15), https://www.ibtimes.com/howchick --fil-social-media-marketing-translated-twitter-facebook -instagram-success-2265588.

Schwartz HA, Eichstaedt JC, Kern ML, Dziurzynski L, Ramones SM, Agrawal M, Shah A, Kosinski M, Stillwell D, Seligman ME (2013) Personality, gender, and age in the language of social media: The open-vocabulary approach. PLoS One 8(9):e73791.

Sharma S (2013) Black Twitter? Racial hashtags, networks and contagion. New Formations 78(1):46–64.

Sommerlad J (2018) Twitter suspends popular accounts for “tweetdecking” to inflate popularity. Independent (March 12), https:// www.independent.co.uk/life-style/gadgets-and-tech/news/ twitter-tweetdecking-accounts-suspended-spam-retweeting -crackdown-purge-a8252106.html

Son I, Lee D, Kim Y (2013) Understanding the effect of message content and user identity on information diffusion in online social networks. Lee J-N, Mao J-Y, Thong J, eds. Pacific Asia Conf. Inform. Systems Proc. (Association for Information Systems, Atlanta), Article 8.

Suh B, Hong L, Pirolli P, Chi EH (2010) Want to be retweeted? Large scale analytics on factors impacting retweet in Twitter network. 2010 IEEE Second Internat. Conf. Soc. Comput. (IEEE Computer Society, Los Alamitos, CA), 177–184.

Sung M (2018) Friends lost their camera at Coachella. It only took the internet 1 day to reunite them. Mashable (June 5), https:/ mashable.com/2018/06/05/coachella-lost-disposable-camera -found/#n.GDZldgQiqh.

Susarla A, Oh JH, Tan Y (2012) Social networks and the diffusion of user-generated content: Evidence from YouTube. Inform. Systems Res. 23(1):23–41.

Taecharungroj V, Nueangjamnong P (2015) Humour 2.0: Styles and types of humour and virality of memes on Facebook. J. Creative Comm. 10(3):288–302.

Trusov M, Bucklin RE, Pauwels K (2009) Effects of word-of-mouth vs. traditional marketing: findings from an internet social net working site. J. Marketing 73(5):90–102.

Utz S, Schultz F, Glocka S (2013) Crisis communication online: How medium, crisis type and emotions affected public reactions in the Fukushima Daiichi nuclear disaster. Public Relations Rev. 39(1): 40–46.

Wang S, Lo D, Jiang L (2013) An empirical study on developer interactions in StackOverflow. Proc. 28th Annual ACM Sympos. Appl. Comput. (ACM, New York), 1019–1024.

Weng L, Menczer F, Ahn Y-Y (2013) Virality prediction and community structure in social networks. Sci. Rep. 3(2013):Article 2522.

Westerman D, Spence PR, Van Der Heide B (2014) Social media as information source: Recency of updates and credibility of information. J. Comput.-Mediated Comm. 19(2):171–183.

Whitten S (2018) Snarky Twitter feeds: Wendy’s and White Castle’s most dangerous weapon. CNBC (June 15), https://www.cnbc .com/2018/06/15/wendys-white-castles-most-dangerous-weapon -a-snarky-twitter-feed.html.

Wu PC, Wang Y-C (2011) The influences of electronic word-of-mouth message appeal and message source credibility on brand attitude. Asia Pacific J. Marketing Logist. 23(4):448–472.

Yang G (2016) Narrative agency in hashtag activism: The case of #BlackLivesMatter. Media Comm. 4(4):13–17.

Zeng X, Wei L (2013) Social ties and user content generation: Evidence from Flickr. Inform. Systems Res. 24(1):71–87.
