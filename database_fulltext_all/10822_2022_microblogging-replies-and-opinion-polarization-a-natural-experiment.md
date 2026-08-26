---
otero_id: 10822
otero_key: "9XPDZSMS"
title: "Microblogging Replies and Opinion Polarization: A Natural Experiment"
authors: "Yingda Lu; Junjie Wu; Yong Tan; Jian Chen"
year: "2022"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/15455"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# MICROBLOGGING REPLIES AND OPINION POLARIZATION: A NATURAL EXPERIMENT<sup>1</sup>

Yingda Lu College of Business Administration, University of Illinois Chicago, Chicago, IL, U.S.A {yingdalu@uic.edu}

Junjie Wu School of Economics and Management, Beihang University, Beijing, CHINA {wujj@buaa.edu.cn}

Yong Tan Michael G. Foster School of Business, University of Washington, Seattle, WA, U.S.A {ytan@u.washington.edu}

Jian Chen School of Economics and Management, Tsinghua University, Beijing, CHINA {chenj@sem.tsinghua.edu.cn}

In recent years, there has been a heated discussion on opinion polarization on social media platforms. Extant research attributes the emergence of echo chambers to higher exposure to information from users’ existing social networks, which consists of like-minded others and argues that the provision of information from outside users’ networks could alleviate opinion polarization. In this paper, we formulate a hierarchical Bayesian learning model to investigate the impact of replies, one of the main channels for information outside of users’ networks, on opinion polarization. We leverage a unique natural experiment contained in the data from a leading microblogging website in China in which the reply function was shut down for three days. This setting allows us to identify the impact of replies from that of peer microblogs. We found that shutting down reply function reduced sentiment polarization on the microblogging site. In addition, this effect was more significant for individuals with higher social media participation. The results of this study shed light on marketing campaign strategies as well as the ways in which platform design can reduce polarization.

Keywords: Opinion polarization, social media, Bayesian learning

## Introduction

In recent years, given the steady increase in polarization in the U.S. (Boxell et al., 2017), the heated discussion on “echo chambers” has inspired academic researchers to examine the mechanism of opinion polarization regarding political issues on social media platforms. There is also a concern that echo chambers could facilitate the spread of misinformation on social media platforms (Vicario et al., 2019). Similarly, in the business context, previous research has demonstrated that customer opinions can be very heterogeneous and shown that opinion polarization has a significant impact on product sales because of the disutility of product uncertainty and information values (Ye et al., 2009, Sun, 2012, Wu et al., 2013). Many studies have attributed opinion polarization to higher exposure to information from existing online social networks (e.g., “followers” on Twitter and Facebook “friends”), which generally consist of like-minded others (McPherson et al., 2001, Sunstein, 2018). However, the impact of replies, another important mechanism for information diffusion on social broadcasting platforms like Twitter, remains understudied.

As evidence of its importance, the reply mechanism on social broadcasting platforms is designed to receive attention from industry. Twitter has recently attracted attention over two controversial features related to replies. In November 2019, Twitter started allowing users to hide replies to their tweets by moving them to a different page. In May 2020, Twitter began testing a new setting in which users could limit who can reply to their tweets. While Twitter’s hope for these new features was to reduce “toxic content” on the platform, these features also triggered significant concerns among Twitter users because they may further enhance the echo chamber on social media platforms (Forbes, 2020).

Compared with tweets and retweets broadcasted along social networks constructed from the following relationship (i.e. if A follows B, B’s content will automatically be posted on A’s timeline), replies offer opportunities to individuals without any connection to the poster to join conversations that interest them (Twitter, 2017). For example, two users with no relationship with each other can still engage in a conversation about the recent Star Wars movie by replying to the same tweet. In other words, replies allow information from outside the user’s network (denoted as out-of-network information in this paper) to enter the conversation,<sup>2</sup> thus potentially increasing the variety of the information users are exposed to. In contrast, if the interaction is limited to social network ties (such as retweeting through the following relationship) information is likely to be exchanged with primarily like-minded users.

While Twitter imposed policies that restricted the use of replies, other platforms made changes to facilitate such provision of out-of-network information. For instance, Facebook has been working with The Wall Street Journal to create an online tool, “Blue Feed Red Feed,” to show liberal and conservative Facebook posts side by side. Mobile apps such as Burst for Reddit have been developed to allow users to see a variety of replies on social media platforms on topics ranging from political issues to new iPhones. Some researchers argue that through the provision of such out-of-network information, individuals are no longer disproportionally exposed to information from likeminded others on social media platforms and will thus be less prone to the “echo chamber” effect.

However, despite the importance of online opinion polarization for “democratic societies as well as decentralized organizations” (van Alstyne & Brynjolfsson, 2005), there is a scarcity of research on the impact of reply-type channels on opinion polarization in academia, and the results from a handful of relevant studies have provided mixed results. Most of the relevant research argues that out-of-network information is more heterogeneous than information diffused through social networks and that different viewpoints can help reduce segregation among contributors and lead to consensus—for example, in the context of Wikipedia (Greenstein et al., 2021) and online forums (Wagner & Ylä- Anttila, 2020). On the other hand, an experimental study by Bail et al. (2018) showed that requesting users to follow a bot with opposing political ideologies could backfire and further enhance the opinion polarization of online communities.

To the best of our knowledge, our study is the first to examine the role of replies on opinion polarization in the context of a microblogging platform like Twitter. We ask: When out-ofnetwork information from replies is presented on social media platforms, will users be more likely to reach consensus through conversations on social media platforms, or will “echo chambers” be further enhanced, leading to more segregated communities with polarized opinions? To bridge this research gap, the main research question we address in this paper is: Do replies on social media platforms influence opinion polarization on social media platforms?

We examine opinion polarization in the context of Weibo.com, the Chinese version of Twitter. Weibo was founded by the Sina Corporation in 2009 and is the largest microblogging website in China. It is also the leading broadcasting channel in several fields such as financial news (85%) and sports news (38%) (Sina Tech, 2015). As of 2020, it had around 516 million monthly active users (Sina Tech, 2020). Like Twitter, Weibo allows users to follow each other, with followees’ posts appearing on users’ timelines. In addition, Weibo also provides the same reply function as Twitter, allowing anyone to post their opinion on a microblog, with all replies being publicly displayed.<sup>3</sup>

One of the main econometric challenges of identifying the impact of replies on opinion polarization is that reply generation is endogenous; thus, the estimated impact can be biased by unobserved confounding factors. For example, controversial topics naturally inspire a larger number of and more heterogeneous replies; thus, the impact of replies may be confounded with topic controversy. In addition, individuals who post microblogs can also choose to disable the reply function, which introduces yet another source of endogeneity. We address this issue by employing a unique dataset from Weibo.com between March 17, 2012, and April 16, 2012. During this one-month period in our observation time frame, the website shut down the reply function for all microblogs for three days between March 31 and April 2. No one could reply to any microblog but the retweeting feature was still functional. This policy shift regarding the reply function provides a unique natural experimental setting with reversal design and offers the exclusion restrictions needed to identify the impact of replies on opinion polarization. Because this reply function shutdown only happened on Weibo.com, we employed data from Sohu Weibo (another large microblogging website in China) as well as Twitter as control groups to construct a difference-in-differences (DID) framework to further control for time-specific confounding factors.

Furthermore, compared with previous opinion formation studies in traditional media settings where only aggregated behaviors are observed, an advantage of our social media platform context is that it enables the measurement of the sentiment of user-generated content and tracks the process of how opinions are affected by others. With few exceptions (Watts & Dodd, 2007, Dai et al., 2018), most previous studies, have utilized observed individual decisions, such as past purchase experience (Erdem & Keane, 1996, Zhang, 2010), online reviews (Chevalier & Mayzlin, 2006), and new product adoption decisions (Iyengar et al., 2011), to infer the underlying opinion formation process. The unique context of our study allows us to explicitly examine the dynamics of opinion polarization with directly observed, rather than inferred, individual opinions. In addition, Weibo also facilitates the retweeting <sup>4</sup> of other users’ microblogs and allows users to embed their own opinion as part of the retweet. As a result, microblogging chains center on a specific topic, and opinions expressed in microblogs within the same chain explicitly demonstrate the individual opinion formation process. This specific social media platform feature results in a network where opinion formation takes place through the retweets and replies in a microblogging chain. This allows us to investigate the underlying mechanisms of opinion polarization at a much finer level than previous studies.

We estimate two regression models in this study. The first regression model is presented in the Natural Experiment and Aggregate-Level Model section addresses the research question at the aggregate level. We then present our second model, which allows us to model individual-level opinion formation using a Bayesian learning framework. We further demonstrate that this Bayesian learning model helps significantly improve the predictive performance. Contrary to the intuition that replies can reduce polarization by presenting out-of-network information, our results show that replies increase the polarization of communities on the social media platform. This surprising result suggests that attempts to provide out-of-network information may backfire and lead to further segregation among individuals. In addition, our Bayesian learning model also provides empirical evidence that confirmation bias—i.e., the tendency for individuals to seek and consume information consistent with their existing opinions—is one potential mechanism explaining why the reply function increases opinion polarization.

Our research makes the following contributions to the literature. First, this is the first study that examines the effect of the reply-type channel on opinion polarization on a social media platform. Second, leveraging a unique natural experiment featuring a reply shutdown, we demonstrate that replies increase opinion polarization. We further incorporate social network data and find that individuals with higher social media participation levels experienced more significant impacts from the reply shutdown. Third, given the recent heated discussion on echo chambers on social media platforms, our results provide timely managerial implications on how social media platforms could improve their designs to reduce opinion polarization and echo chambers.

The rest of the paper is organized as follows. In the next section, we review the related work to build the theoretical foundation of this research. Then, we discuss the use of a natural experimental setting to address endogeneity problems in this study and present an aggregate-level model to address our research question. Next, we present the Bayesian learning model setup and estimation approach. This is followed by the discussion of estimation results and our conclusion.

## Theoretical Foundations and Literature Review

## Opinion Formation

The notion of opinion formation has drawn attention from researchers in economics, management, political science, and physics. Several theoretical frameworks have been proposed to investigate this particular process using the Bayesian framework. Zaller (1992) designed a model in which individuals form their political preferences based on their prior beliefs and the information they receive. DeMarzo et al.

(2003) proposed a bounded rationality model that incorporates persuasion bias and found that the individual influence on others depends not only on the accuracy of information but also on the individual’s network capital. There is also a line of work in economics that studies the conditions under which a group of individuals could reach consensus through network interactions (DeGroot, 1974, Golub & Jackson, 2010, Bindel et al., 2011). Mullainathan and Shileifer (2005) built an analytical model and demonstrated that newspaper competition can enhance opinion polarization among readers.

One stream of research empirically explores various aspects of the opinion formation process (DellaVigna & Gentzkow, 2010). A large number of field experiments have been conducted to measure the effectiveness of different communication channels on the opinion formation of customers (Lodish et al., 1995, Hu et al., 2007), voters (Klapper, 1960, Gerber et al., 2011), and investors (Ball & Brown, 1968, Womack, 1996, Kothari, 2001). The main mechanism in which communication channels influence opinion is by changing receivers’ beliefs. Individuals commonly have certain prior beliefs about an issue and they update their beliefs based on the additional information they receive from various communication channels. The prior beliefs of individuals have also been shown to affect how they update their beliefs. When individuals are less certain about the truth of a matter, their beliefs are more likely to be influenced by new information (Ackerberg, 2003, DellaVigna & Gentzkow, 2010, Enikolopov et al., 2010). Characteristics of channels that convey additional information also may have impacts on the opinion formation process (Chiang & Knight, 2011). Gentzkow and Shapiro (2010) found that newspaper readers have a strong preference for like-minded news and that newspapers also tend to produce content consistent with reader preferences.

There are also studies investigating the impact of networks on opinion formation. Katz and Lazarfeld (1995) found that customer opinions are more susceptible to influences from their peers than to those from public media. In addition, researchers have made significant contributions in uncovering the dynamics of opinion formation by illustrating the importance of a critical mass of easily influenced individuals (Watts & Dodds, 2007) and the role of opinion leaders in opinion formation (van den Bulte & Joshi, 2007). Similarly, our research is also related to studies investigating the social dynamics of the generation of online review ratings (see, for example, Moe & Trusov, 2011, Godes & Silva, 2011).

Closely related to our study is the emerging literature on whether and how online communications lead to integrated or segregated communities. Van Alstyne and Brynjolfsson (2005) have examined how factors such as access, search, and screen can lead to consensus or polarization among internet users.

Lawrence et al. (2010) demonstrated that blog readers are indeed polarized regarding ideology; they further examined the participation level of blog readers with different political viewpoints. Gentzkow and Shapiro (2011) found that the ideological segregation of online news consumption is higher than that of offline news but lower than that of offline personal communications. Shore et al. (2016) suggested that individuals within a network’s core tend to be polarized, while other users are less polarized. Greenstein et al. (2021) examined usergenerated content on Wikipedia and found that conversations on Wikipedia lead to less extreme opinions among contributors. However, Wikipedia is different from a social broadcasting platform such as Twitter, as it is not designed as a platform for public information diffusion and conversation. On the other hand, Nyhan and Reifler (2010) identified a backfire effect and found that providing facts may further enhance individual ignorance. Wagner and Ylä-Anttila (2020) showed that providing individuals with the opportunity to participate in a forum with people of different viewpoints does not really help individuals learn from those with opposing views. Perhaps most relevant to our study, Bail et al. (2018) conducted a field experiment that incentivized Twitter users to follow a bot with opposing views and found that this enhances opinion polarization among users. However, their experimental study was restricted to the scenario of exogenously providing opposite viewpoints in a partisan political context, while our study examines the impact of endogenously generated replies and accounts for out-of-network information. In addition, Bail et al. (2018) only provided exogenous information to subjects whereas replies enable individuals to present their own opinions and interact with others.

As such, there is a scarcity of empirical research that examines how opinion polarization is affected by the replytype channel, which brings together strangers who are interested in the same topic. This is the research gap we intend to fill in this paper.

## Microblogs and Replies

In this section, we discuss the differences between microblogs and replies to elaborate how replies could influence opinion polarization differently from microblogs. This helped us generate the hypotheses of this study.

There are two main differences between microblogs and replies from a theoretical perspective. First, microblogs are diffused within the follower-followee network, and individuals who share ties often share similar opinions (McPherson et al., 2001). As a result, they are likely to be disproportionally exposed to opinions that are similar to their own. In contrast, users who reply to the same microblogs are attracted to the same topic but may have very few connections to each other. This is also consistent with De Stefano and Santelli’s (2019) study, which argues that the diffusion of microblogs is centered around embedded networks while replies are generally centered around topics. As a result, the reply function enhances users’ propensity of being exposed to individuals with different opinions. Indeed, the reply function is explicitly designed as a way of getting users interested in the same topic involved in a conversation. <sup>5</sup> In addition, Kim and Yoo (2012) distinguished the motivation behind posting retweets and replies and found that when individuals want to endorse a microblog, they are more likely to retweet it, whereas replies contain both negative and positive sentiment. Such conversation among individuals with different opinions could potentially help conversation participants reach consensus rather than becoming further embedded in polarized opinions (Greenstein et al., 2021).

Second, retweets mainly follow a one-directional broadcasting channel, whereas the conversations within replies tend to be two-way. Shi et al. (2014) proposed that microblogging websites are social broadcasting environments where retweets spread information through content sharing from followees to followers; thus, retweeting can be regarded as one-way information propagation. However, users post replies as a way of joining conversations in which back-andforth communications among multiple individuals can take place. We illustrate a typical example of back-and-forth conversation in Figure A2 in Appendix A.

These two differences allow replies to introduce more diverse information compared with microblogs. However, after individuals are exposed to such diverse information embedded in replies, there are two contradicting forces that could influence how individuals consume such information. On the one hand, there is a stream of literature suggesting that exposure to diverse information can increase consensus because the exposure to diverse information helps individuals better understand those with opposing opinions, which may motivate them to rethink their prior opinions (Fishkin, 2009). This could also enhance their respect for others with opposing viewpoints (Mutz, 2008) and consequently help them incorporate opposing information to update their own opinions (Pettigrew & Tropp, 2006). Greenstein et al. (2021) argued that dialogue among multiple individuals with different opinions can help facilitate the formation of consensus. We denote this process as the consensus effect. We thus hypothesize:

H1a: Replies reduce opinion polarization on social media platforms; therefore, shutting down the reply function will increase opinion polarization.

However, replies may also enhance opinion polarization. One potential reason for this is confirmation bias, in which individuals tend to self-select content that is consistent with their existing opinions (Mullainathan & Shileifer, 2005, Allahverdyan & Galstyan, 2014). Durante and Knight (2012) showed that viewers tend to consume TV programs that are in line with their political ideologies. Likewise, research has shown that individuals tend to doubt the accuracy of information sources if they contradict their prior beliefs on a topic (Getzkow & Shapiro, 2006, Getzkow & Shapiro, 2010). Confirmation bias has also been observed in online settings. Park et al. (2013) found that investors prefer online forum messages that support their beliefs. Yin et al. (2016) showed that online reviews that are consistent with readers’ beliefs are perceived to be more helpful. Although the potential influence of replies on opinion polarization through confirmation bias has not been previously studied, it is certainly possible that replies increase polarization because individuals are disproportionally influenced by replies that are consistent with their already formed beliefs and thus discount replies that oppose their beliefs. This, in turn, may lead to higher levels of polarization on microblogging platforms. Therefore, we propose the competing hypothesis:

H1b: Replies increase opinion polarization on social media platforms; therefore, shutting down the reply function will decrease opinion polarization.

We further examine the moderating effect of individual social media participation on the impact of replies on the extremity of opinions.<sup>6</sup> We argue that users’ social media participation level could enhance the impact of replies on their opinion extremity. Previous studies have demonstrated that individuals with higher levels of social media participation interact with people with more diverse opinions, as they spend more time browsing and consuming content on social media platforms (Brundidge, 2010). Such individuals would thus also inevitably have higher chances of joining conversations with individuals with opposing viewpoints, which could occur either voluntarily or inadvertently. Lee et al. (2014) provide empirical evidence that the usage of social media is associated with individual exposure to opposing viewpoints. In addition, previous communication research suggests that individuals consider new information more seriously when they anticipate a response from others on their expressed opinions (Hardy & Scheufele, 2005). In the context of social media platforms, we also expect users with higher participation levels to examine information in replies more carefully. As a result, if individuals can assimilate opposing viewpoints into the formation of their own opinions, replies can further reduce the opinion extremity of individuals with higher social media participation levels. If the consensus bias effect dominates the way that individuals consume replies, individuals with higher social media participation are also the ones who will become more extreme under the influence of replies. Thus, we propose:

H2: The individual social media participation level enhances the impact of replies on opinion extremity.

## Background and Data

Founded in 2009, Weibo has become the largest microblogging website in China. To construct our estimation dataset, we first collected all users who had ever posted any microblog on the website between March 17 and April 16, 2012. Next, from over 50 million users on this microblogging platform, we randomly selected genuinely active users with more than 200 but fewer than 3000 followers that had also published fewer than 3000 microblogs.<sup>7</sup> We set the lower limit for the number of followers to rule out spam or inactive accounts on Weibo.com. We set the upper limit for number of followers to exclude “celebrities.” These two types of accounts could both introduce tweeting/replying relationships that are distinctively different from the ordinary microblogging users in whom we are interested. A random sampling among these genuinely active users generated 2801 users.<sup>8</sup> We then traced back all activity history of these users on Weibo.com up to September 2011. We also collected related information for each microblog, including the author, time stamp, sequence of each microblog retweeting chain, and the full text. We further collected information about all replies associated with these microblogs, including authorship, time stamp, and full text.

Before moving on to the details of our model setup, we briefly introduce the mechanism by which users receive information on Weibo. We use a tree graph (Figure 1) to depict a specific microblog tree in our data. The square node represents the microblog that initiates the entire microblog tree. The white dots right below represent retweeted microblogs in the chain. Lines represent the retweeting relationship between microblogs, thus dots on different levels represent the microblogs in different levels of the microblog tree.

When a user logs onto Weibo, the platform sends notifications and displays microblogs of the user’s followees (i.e., users who the user follows) on the user’s homepage. As a result, the user is exposed to followees’ microblogs as well as the ones that precede these microblogs in the same chain. The user can also simply click a button to easily browse the replies accompanying these microblogs. These microblogs and replies naturally influence the user’s opinion about this topic (Dai et al., 2018), which then is reflected in the user’s own microblog if desired.

We use Figure 2 to show the scheme of a microblog chain, including original microblogs, retweets, and replies. Notice that in contrast to the way retweeting works on Twitter.com, the design of Weibo displays all tweets (including the original tweet and retweets) in a microblog chain. In other words, any user who follows User 3 in Figure 2 will be exposed to tweets 1, 2, and 3 irrespective of whether the focal user follows User 1 or User 2. Notice that during the reply-shutdown period, existing replies were still available to the public. An illustration of the microblog and reply mechanism on Weibo.com can be found in Appendix A.

Because individual opinions are expressed explicitly through microblogs on the platform, we measure individual opinion by applying machine learning techniques to microblog texts. As microblogs tend to be quite short, the accuracy of sentiment analysis using text mining has been very challenging. In this study, we adapt the multiclass sentiment analysis in Zhao et al. (2012) and further incorporate emoticons into the construction of the naive Bayes classifier. The predictive performance is very high, considering the short length of the tweets: precision is 0.7439, recall is 0.7483 and the F-score is 0.7394. The details about our opinion mining technique can be found in Appendix D. Employing this innovative algorithm, we are able to classify the microblogs into three different categories: positive, neutral, and negative.<sup>9</sup>

We list the statistics of key variables in Table 1. In our dataset, the average in-degree for each user is 12.81 (only including users in the estimation dataset). 17,945 microblogs were posted every day. Each user posted 198.6 microblogs, on average, over our observation period. The average number of replies per day was around 1.6 million. The average sentiment of each microblog was 0.179, indicating a positive opinion environment in general.

![](/api/attachments/9XPDZSMS/fulltext/images/1804ec0a22ef3c72680ccc62b90a70d2e56d1eb4b7d81b7df89be4a339b10eea.jpg)  
Figure 1. Example of Microblog Tree

![](/api/attachments/9XPDZSMS/fulltext/images/3cc8adbf8293bfdb5a34ae184ab9f25c48f4f8c038f9391ddccffd5ca7917bb4.jpg)  
Figure 2. Conceptual Graph of Microblog Chain Structure

<table><tr><td colspan="3">Table 1. Variable Statistics</td></tr><tr><td>Variables</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Number of users</td><td>2801</td><td></td></tr><tr><td>Time period (days)</td><td>31</td><td></td></tr><tr><td>Number of microblogs (including retweets)</td><td>556,281</td><td></td></tr><tr><td>In-Degree within estimation dataset</td><td>12.81</td><td>7.39</td></tr><tr><td>Number of microblogs per day</td><td>17,945</td><td>7,913</td></tr><tr><td>Number of microblogs per user</td><td>198.6</td><td>709.75</td></tr><tr><td>Number of replies per day</td><td> $1.627 \times 10^{6}$ </td><td> $8.254 \times 10^{5}$ </td></tr><tr><td>Number of replies per microblog</td><td>76.95</td><td>269.49</td></tr></table>

## Natural Experiment and Aggregate-Level Model

In this section, we first elaborate our identification strategy leveraging an exogenous shock for model estimation and then provide an aggregate-level model to address the research question by aggregating our data at the microblog chain level.

## The Econometric Challenge and Identification Strategy Using a Natural Experiment

The main econometric challenge for our study examining the impact of replies is that replies are endogenously generated. There are two sources of endogeneity. First, individuals who post microblogs can endogenously choose to disable the reply function. Second, the impact of replies can be confounded by unobserved topic characteristics. In particular, it is difficult to distinguish the impact of replies on individual opinion formation from the possibility that the sentiment of replies is driven by the topic itself.<sup>10</sup> For example, controversial topics may generate polarized opinions and are also likely to attract a lot of replies. In addition, retweet characteristics and reply characteristics are generally correlated. The correlation between the number of microblogs and the number of replies within a microblogging chain is 0.359 for the period before our treatment time period.

To address the econometric challenge of endogenous replies, we exploit a unique natural experiment setting in this study (Zhang & Zhu, 2011). Specifically, between March 31 and April 2, 2012, Weibo.com shut down the reply function of the website<sup>11</sup> and no notification was sent about this shutdown until around 12 hours before the reply function was disabled. Replies posted before the reply shutdown were still available during this three-day period. This treatment is exogenous because users would not have been able to strategically respond to this design change. This exogenous shock creates a natural experiment that provides an ideal exclusion restriction for our identification of the impact of replies. With the help of this natural experiment, we can compare the opinion polarization before, during, and after the treatment, and attribute the differences in the opinion polarization to the impact of replies.

One of the concerns about this natural experimental setting is that there could have been a time effect that confounded the impact of shutting down the reply function. To control for this, we incorporated data from Sohu Weibo (a different website founded by the Sina Corporation), one of the four largest microblogging websites during the time period of our study. Because Sohu Weibo did not shut down the reply function on its platform, it becomes an ideal candidate for a control group in our estimation models.<sup>12</sup> We further conducted propensity score matching based on microblog chain characteristics to generate datasets that are comparable across these two different platforms. <sup>13</sup> We consequently conducted a DID model to alleviate the concerns about a potential confounding time effect in our study.

Another unique characteristic of our dataset is that the natural experiment happened during our observation period and the reply function resumed after the treatment period. This type of A-B-A design, in contrast to the traditional A-B design in quasi-experiment studies, allowed us to further exclude the time trend as a potential confounding factor. The addition of the reversal stage significantly increases the internal validity of the study (Price et al., 2016). We discuss this in more detail in the Robustness Checks section.

## Aggregate-Level Model

In this section, we propose an aggregate-level regression in which we evaluate how the treatment measures the influence of replies on average sentiment $( S e n t i M _ { m t p } )$ and the sentiment polarization $( P o l a r M _ { m t p } )$ of microblogs within the microblog chain ?? at period ?? (we define one period as one day) for platform ?? on an aggregated level using Equations (1) and (2) respectively:<sup>14</sup>

$$
\begin{array}{l} \text {PolarM} _ {m t p} = \alpha_ {0} + \alpha_ {1} \text {PolarM} _ {m t - 1 p} + \alpha_ {2} \text {NumM} _ {m t - 1 p} + \\ \alpha_ {3} \text {NumUser} _ {m t - 1 p} + \alpha_ {4} D I D _ {t p} + \alpha_ {5} \text {Topic} _ {m} + \alpha_ {6} T _ {t} + \\ \alpha_ {7} P _ {p} + \alpha_ {8} \text {Weekend} _ {t} + \varepsilon_ {1 m t p} \end{array} \tag {1}
$$

$$
\begin{array}{l} S e n t i M _ {m t p} = \alpha_ {0} + \alpha_ {1} S e n t i M _ {m t - 1 p} + \alpha_ {2} N u m M _ {m t - 1 p} + \\ \alpha_ {3} N u m U s e r _ {m t - 1 p} + \alpha_ {4} D I D _ {t p} + \alpha_ {5} T o p i c _ {m} + \alpha_ {6} T _ {t} + \\ \alpha_ {7} P _ {p} + \alpha_ {8} W e e k e n d _ {t} + \varepsilon_ {2 m t p}, \end{array} \tag {2}
$$

Equations (1) and (2) are estimated simultaneously, allowing their error terms to be correlated. Notice that we mainly discuss the results for Equation (1), as the focus of our research is on opinion polarization. We measure polarization by calculating the standard deviation of the sentiment of corresponding microblogs. When there is a higher percentage of both positive and negative sentiment microblogs, the standard deviation will be higher, and this also indicates that individuals will tend to have more opposing opinions. Here $D I D _ { t p }$ is the dummy variable of our interest in this DID model. It captures the treatment group (e.g., Weibo) during the time period of the reply function shutdown. For example, if the coefficient of $D I D _ { t p }$ is positive for the regression on $P o l a r M _ { m t p } ,$ replies decrease the polarity of sentiments in microblogs. In other words, replies help the community reach consensus, and such results would support our H1a. $P _ { p } = 0$ if microblog chain ?? is on Sohu Weibo platform and $P _ { p } = 1$ if it is on Weibo platform (i.e., in treatment group). We also included a dummy variable for the reply-shutdown period $T _ { t }$ in our model.

We included the average and standard deviation of microblogs from the previous period in the same microblog chain $( S e n t i M _ { m t - 1 p }$ and $P o l a r M _ { m t - 1 p } )$ , as well as the number of related microblogs $( N u m M _ { m t - 1 p } )$ in the equations above to control for microblog-related characteristics. We also used $N u m U s e r _ { m t - 1 }$ to account for the number of users who participated in this microblog chain in period ?? − 1. We did not include reply characteristics in the equations above because

Sohu Weibo reply texts from 2012 were no longer available when we conducted this study. However, omitting reply characteristics is unlikely to bias our results, as our identification strategy relies on reply shutdown as the exogenous treatment. Nonetheless, to test the robustness of our results against reply characteristics, we conducted a robustness check with reply characteristics but removed Sohu Weibo as a control variable. Please refer to the Robustness Checks section for more details. Table 2 summarizes the variable definition for the aggregatelevel model, the Bayesian learning model, and other robustness check models in the remaining sections.

We also included control variables for microblogging topics in this model. We used a dummy vector $T o p i c _ { m }$ to denote the corresponding topic of the microblog chain. In this paper, we use the topic modeling technique to determine the topic of the microblog chain and included microblogs from eight major categories in our dataset: finance, IT, entertainment, sport, education, equipment, women/home, and automobiles. <sup>15</sup> Please refer to Appendix D for details on the topic modeling algorithm we employ in this study.<sup>16</sup>

We present the results of aggregate-level regressions in Table 3. The results for sentiment polarization regression are in the first column and those for average sentiment regression are in the second column. We omit the coefficients for control variables for simplicity. The full results can be found in Appendix B.

Our main research question is on the impact of the reply function on opinion polarization; thus, we focus on the results in the first column. The coefficient of $D I D _ { t p }$ is negative and significant, meaning that shutting down the reply function reduced the polarity of sentiments. In other words, replies for microblogs increase opinion polarization among users, thus supporting H1b. This is in stark contrast to many practitioners arguments that exposing individuals to more heterogeneous information can reduce polarization and alleviate echo chambers. Based on our discussion for H1b, this result provides empirical evidence that the confirmation bias effect dominates the diversity of information sources brought by replies. In other words, individuals on Weibo tend to focus more on reading replies that are consistent with their existing beliefs, while discounting replies that oppose their viewpoints. As we discuss in the following sections, the results of the aggregate-level model are consistent with the estimation results for our main Bayesian learning model.

<table><tr><td colspan="2">Table 2. Variable Definition</td></tr><tr><td>Variable</td><td>Definition</td></tr><tr><td> $PolarM_{mtp}$ </td><td>Polarity of sentiment of microblog chain m in period t on platform p, measured as the standard deviation of all microblogs within microblog chain m posted in period t</td></tr><tr><td> $SentiM_{mtp}$ </td><td>Average sentiment of microblog chain m in period t on platform p, measured by calculating the average sentiment across all microblogs within microblog chain m posted in period t</td></tr><tr><td> $NumM_{mtp}$ </td><td>Number of microblogs of microblog chain m posted in period t on platform p</td></tr><tr><td> $PolarC_{mtp}$ </td><td>Polarity of sentiment of replies for microblog chain m in period t on platform p, measured as the standard deviation of replies of all microblogs within microblog chain m posted in period t</td></tr><tr><td> $SentiC_{mtp}$ </td><td>Average sentiment of replies for microblog chain m in period t on platform p, measured by calculating the average sentiment across replies of all microblogs within microblog chain m posted in period t</td></tr><tr><td> $NumC_{mtp}$ </td><td>Number of replies of microblogs in microblog chain m posted in period t on platform p</td></tr><tr><td> $NumUser_{mtp}$ </td><td>Number of users that contribute to microblog chain m in period t on platform p</td></tr><tr><td> $DID_{tp}$ </td><td>Dummy variable, variable value is 1 for observations on Weibo platform during the treatment period and zero otherwise</td></tr><tr><td> $Topic_m$ </td><td>Dummy variables to control for topic categories for microblog chain m</td></tr></table>

<table><tr><td colspan="3">Table 3. Estimation Results for Aggregate-Level Model</td></tr><tr><td>Variable</td><td>Sentiment polarization</td><td>Average sentiment</td></tr><tr><td> $PolarM_{mt-1p}$ </td><td>0.045***(0.004)</td><td>--</td></tr><tr><td> $SentiM_{mt-1p}$ </td><td>--</td><td>0.064***(0.002)</td></tr><tr><td> $NumM_{mt-1p}$ </td><td>-0.008***(0.000)</td><td>-0.002***(0.000)</td></tr><tr><td> $NumUser_{mt-1p}$ </td><td>0.019***(0.007)</td><td>0.005***(0.001)</td></tr><tr><td> $DID_{tp}$ </td><td>-0.013***(0.004)</td><td>0.007***(0.001)</td></tr><tr><td>Is Weibo ( $P_p$ )</td><td>0.025***(0.000)</td><td>0.020***(0.006)</td></tr><tr><td>Reply-shutdown period ( $T_t$ )</td><td>0.003*(0.001)</td><td>0.002*(0.001)</td></tr><tr><td> $Weekend_t$ </td><td>-0.007*(0.003)</td><td>0.004**(0.002)</td></tr><tr><td>Topic-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>0.262***(0.003)</td><td>0.215***(0.081)</td></tr><tr><td> $R^2$ </td><td>0.323</td><td>0.237</td></tr></table>

Note: Standard error in parentheses. Significance: \*\*\*1%; \*\*5%; \*10%.

## Bayesian Learning Model Setup

In this section, we formulate a Bayesian learning model to capture the individual opinion formation process and examine the impact of replies on opinion extremity at the individual level. Compared with the aggregate-level model in the previous section, the Bayesian learning model has the following advantages. First, the aggregate-level model considers opinion polarization as a linear function of covariates, while opinion formation is best described using a nonlinear Bayesian updating process (Demarzo et al., 2003). Thus, the Bayesian learning model is expected to significantly improve predictive power. It can also avoid potential biases due to the lack of control of the nonlinear relationship between our focal covariates and individual opinions. Second, the Bayesian learning model allows us to examine how replies influence opinion extremity at the individual level, allowing us to incorporate individual social media participation levels into the model and thereby test H2. Third, the Bayesian learning model can simultaneously model the impact on the mean and variance of opinions. Lastly, we can incorporate the impact of individual prior beliefs into the Bayesian framework.

Consider a microblog chain ?? on this platform, which starts from the original microblog by an individual and continues when one of the individual’s followers retweets the original microblog.<sup>17</sup> This chain will keep growing as the retweeted microblog is retweeted by others. All of the microblogs within the same chain cover the same topic. Meanwhile, any user from this microblogging website can leave replies on each one of these microblogs. We use $N _ { m }$ to denote the total number of levels for microblog chain ??, and ?? to denote the microblog on the $n ^ { t h }$ level of the microblog chain.

Individual $i \in \{ 1 , 2 , \ldots , K \}$ writes a microblog on the $n ^ { t h }$ level of the microblog chain ?? . ?? represents the number of individuals. Before reading the microblogs on this microblogging platform, individual i has certain prior knowledge about the topic from other resources such as $\mathrm { T V } .$ news websites, etc. These exposures to external sources will help individual i form certain opinions about the topic that this microblog chain covers. Here we use $s _ { i m 0 }$ to represent the prior opinion that individuals have before they read microblogs from their peers on a specific topic. To capture opinion extremity in which users have opposing opinions, we assume that $s _ { i m 0 }$ follows a Gaussian mixture distribution with two mixture components. For identification purposes, we assume that $s _ { i m 0 } { \sim } N ( \bar { s } _ { i m 1 } , \sigma _ { m } ^ { 2 } )$ with probability $p _ { s }$ , and $s _ { i m 0 } { \sim } N ( \bar { s } _ { i m 2 } , \sigma _ { m } ^ { 2 } )$ with probability $1 - p _ { s } . \ \bar { s } _ { i m 1 }$ and $\bar { s } _ { i m 2 }$ are the mean of two potential prior opinions for individual ?? on topic ?? and $\sigma _ { m } ^ { 2 }$ is the variance of prior opinion for topic ??. Please refer to Appendix C for more details about prior opinion in our model. In the next subsection, we first discuss modeling the impact of microblogs from individual i’s peers on individual i’s opinion formation process, and then move on to further incorporate the impact of replies.

## Bayesian Updating Process

Individual opinion can be influenced by microblogs from individual i’s peers for two reasons. First, individuals receive signals about others’ opinions on this topic. By learning the information contained in their microblogs, individual i might experience an opinion change because of the newly obtained knowledge. Second, an individual may want to post microblogs reflecting relatively similar opinions vis-à-vis peers because individuals generally seek consistency with the social norm of the social group they belong to (Dai et al., 2018). In other words, individuals may derive disutility if their expressed opinions deviate from the mainstream opinion of their friends.

We use $s _ { i m n }$ to denote the actual posterior opinion of individual ?? when they post the $n ^ { t h }$ level microblog on microblog chain ??. By adapting the model proposed by Dai et al. (2018), we can write individual i’s opinion as a weighted sum of their prior opinion and the influence received from peers: <sup>18</sup>

$$
\begin{array}{r l} & s _ {i m n} = (1 - \varphi_ {0}) s _ {i m 0} + \\ & \varphi_ {0} E \big (F _ {i m n} \big | s _ {m 1} ^ {(i)}, s _ {m 2} ^ {(i)}, \dots , s _ {m n - 1} ^ {(i)}, s _ {i m 0} \big) + \varphi_ {1} D I D _ {t p} \\ & + \varphi_ {2} \big (s _ {i m n - 1} ^ {p} - A v g S _ {i m n} \big) D I D _ {t p} + \varphi_ {3} P a r _ {i} \big (s _ {i m n - 1} ^ {p} - A v g S _ {i m n} \big) D I D _ {t p} + \varphi_ {4} T _ {t} + \varphi_ {5} P _ {p} \end{array}\tag{3}
$$

$\varphi _ { 0 }$ is the weight of peer influence in opinion formation. The first component captures the impact of individual $i ^ { \mathbf { \gamma } } \mathbf { s }$ prior beliefs. $F _ { i m n }$ measures the peer impact individual ?? receives on the $n ^ { t h }$ level of microblog of microblog chain ?? . $E ( F _ { i m n } | s _ { m 1 } ^ { ( i ) } , s _ { m 2 } ^ { ( i ) } , \ldots , s _ { m n - 1 } ^ { ( i ) } , s _ { i m 0 } )$ is the posterior peer impact of previous microblogs on the same microblog chain conditional on individual $i \ ' _ { \mathbf { S } }$ prior opinion and all the expressed opinions of preceding microblogs.<sup>19</sup> We use $s _ { m l } ^ { ( i ) }$ to denote the opinion of the microblog that precedes $s _ { i m n }$ and is on level ??. Thus, the second component of Equation (3) captures how much individual posterior opinion $( E ( F _ { i m n } ) )$ is influenced by previous microblogs in the same chain $( s _ { m 1 } ^ { ( i ) } , s _ { m 2 } ^ { ( i ) } , . . . , s _ { m n - 1 } ^ { ( i ) } )$ . We describe the calculation of this term, $E ( F _ { i m n } | s _ { m 1 } ^ { ( i ) } , s _ { m 2 } ^ { ( i ) } , \ldots , s _ { m n - 1 } ^ { ( i ) } , s _ { i m 0 } )$ , in Equation (5) below. Notice that we do not impose any restrictions on the value of $\varphi _ { 0 }$ , and we empirically estimate this value with our framework. A positive $\varphi _ { 0 }$ indicates the impact of peer influence, where a user’s opinion becomes closer to the opinion of their peers. A negative $\varphi _ { 0 }$ suggests that individuals prefer to show that their opinions are different from the rest of the group. However, we assume that the value of $\varphi _ { 0 }$ is no larger than 1 so that the impact of prior opinion will not increase with new information.

To examine the impact of the reply function, we include a dummy variable for the treatment platform during the natural experiment period, denoted as $D I D _ { t p } \ . \ D I D _ { t p } = 1$ for observations on Weibo during the three days when the reply function was shut down, and zero otherwise. We use $\varphi _ { 1 }$ to measure the impact of the reply shutdown on the individual posterior opinion mean. To provide additional empirical evidence to test the impact of the reply shutdown on opinion polarization (H1a and H1b), we further include an interaction term between $D I D _ { t p }$ and $( s _ { i m n - 1 } ^ { p } - A v g S _ { i m n } )$ Here, $s _ { i m n - 1 } ^ { p }$ represents individual $i \ \mathrm { ^ { \circ } s }$ expressed opinion in microblog chain ?? before reading the microblog on $n -$ $1 ^ { t h }$ level. $A v g S _ { i m n }$ is the average sentiment of microblogs of microblog chain ?? preceding the level ?? microblog written by individual ??. If $\varphi _ { 2 } > 0$ , when previous opinion $( s _ { i m n - 1 } ^ { p } )$ is higher than average sentiment $( A v g S _ { i m n } )$ , the resulting posterior mean opinion $\left( \begin{array} { l } { s _ { i m n } } \end{array} \right)$ is even more positive, and vice versa. In other words, the reply shutdown increases opinion polarity in this scenario. Similarly, if $\varphi _ { 2 } <$ 0, the reply shutdown decreases opinion polarity. Note that our Bayesian model is conducted at the individual level and it thus provides empirical evidence to test H1a/b at the individual level rather than directly testing H1a/b at the aggregate level. While the impact of $D I D _ { t p }$ term on the opinion formation process is nonlinear in this Bayesian learning model, the intuition remains the same as that of our aggregate model.

To examine H2, we include the last term in Equation (3), to capture how users’ social media participation moderates the impact of replies on opinion extremity. $P a r _ { i }$ captures individual social media participation level for individual ?? for the focal topic, calculated as the total number of microblogs individual ?? posted between February 17 and March 16, 2012, related to the topic of the focal microblog chain. To better interpret the coefficient of this term, remember that term $\big ( s _ { i m n - 1 } ^ { p } - A v g S _ { i m n } \big ) D I D _ { t p }$ captures the impact of reply shutdown on opinion extremity. When the sign of $\varphi _ { 3 }$ is the same as $\varphi _ { 2 }$ , the social media participation level enhances the impact of reply (as well as the reply shutdown) on opinion extremity, supporting H2.

Next, we discuss how the second term in Equation (3) is calculated. Individuals realize that their peers’ information is not complete and could thus be inaccurate (Demarzo et al., 2003). As such, if we use $s _ { m n } ^ { ( i ) }$ to denote how individual ?? perceives the opinion of the $n ^ { t h }$ microblog on topic ?? posted by individual ??, we can use the formula below to model the perceived inaccuracy of the peer’s microblog:

$$
s _ {m n} ^ {(i)} = s _ {j m n} + \delta_ {A},\tag{4}
$$

where $\delta _ { A } { \sim } N ( 0 , \sigma _ { A } ^ { 2 } )$ captures the variance sourcing from the peer’s inaccurate information. Intuitively, if an individual believes their peer’s information to be more inaccurate (with large $\delta _ { A } )$ , the individual is less likely to be influenced by the peer’s opinion.

We can write the peer influence component in Equation (3) following the Bayesian updating rule (DeGroot, 1970, Erdem & Keane, 1996):

$$
\begin{array}{r l} & E \big (F _ {i m n} \big | s _ {m 1} ^ {(i)}, s _ {m 2} ^ {(i)}, \ldots , s _ {m n - 1} ^ {(i)}, s _ {i m 0} \big) \\ & = E \big (F _ {i m n} \big | s _ {m 1} ^ {(i)}, \ldots , s _ {m n - 2} ^ {(i)}, s _ {i m 0} \big) + \beta_ {i m n - 1} \left(s _ {m n - 1} ^ {(i)} - s _ {m n - 2} ^ {(i)}, s _ {i m 0} ^ {(i)}\right) \\ & E \big (s _ {m n - 1} ^ {(i)} \big | s _ {m 1} ^ {(i)}, \ldots , s _ {m n - 2} ^ {(i)}, s _ {i m 0} \big) \Big). \end{array}\tag{5}
$$

$E \big ( F _ { i m n } \big | s _ { m 1 } ^ { ( i ) } , s _ { m 2 } ^ { ( i ) } , \ldots , s _ { m n - 1 } ^ { ( i ) } , s _ { i m 0 } \big )$ is the influence from peers microblog on individual i’s opinion after reading through the previous $n - 1$ microblogs in Equation (3). The way this opinion is formed can be decomposed into two steps: first, individuals are influenced by peers’ microblogs after reading through the previous $n - 2$ microblogs. This is captured by the first term $E \big ( F _ { i m n } \big | s _ { m 1 } ^ { ( i ) } , s _ { m 2 } ^ { ( i ) } , \ldots , s _ { m n - 2 } ^ { ( i ) } , s _ { i m 0 } \big )$ . Second, individuals are influenced by the $( \ n - 1 \ ) ^ { t h }$ microblog, captured by second term, $\beta _ { i m n - 1 } ( s _ { m n - 1 } ^ { ( i ) } - $ $E \bigl ( s _ { m n - 1 } ^ { ( i ) } \bigl | s _ { m 1 } ^ { ( i ) } , \ldots , s _ { m n - 2 } ^ { ( i ) } , s _ { i m 0 } \bigr ) \bigr )$ . This second term suggests that individuals update their opinion by comparing the perceived opinion of the $( n - 1 ) ^ { t h }$ microblog and the influence from the preceding $n - 2$ microblogs. By doing this recursively, we can eventually calculate the influence of all preceding microblogs. $\beta _ { i m n }$ is the Kalman gain coefficient, which can be calculated as (DeGroot, 1970):

$$
\beta_ {i m n} = \frac {\sigma_ {i m n} ^ {2}}{\sigma_ {i m n} ^ {2} + \sigma_ {A} ^ {2}},\tag{6}
$$

If $\sigma _ { A } ^ { 2 }$ is large, $\beta _ { i m n }$ will be small; thus, the impact of this microblog on the user’s posterior opinion will be small. $\sigma _ { i m n } ^ { 2 }$ is the variance of an individual’s opinion given information obtained before level ?? of microblog chain ??. Intuitively, the Kalman gain coefficient $\beta _ { i m n }$ measures the weight of microblogs when individuals update their opinions about the topic. $\sigma _ { i m n } ^ { 2 }$ can be calculated using the formula below:

$$
\frac {1}{\sigma_ {i m n} ^ {2}} = \frac {1}{\sigma_ {m} ^ {2}} + \frac {n - 1}{\sigma_ {A} ^ {2} + \rho_ {1} D I D _ {t p} + \rho_ {2} T _ {t} + \rho_ {3} P _ {p}}.\tag{7}
$$

DeGroot (1974) argued that individuals receive imperfect information from others and update their opinions accordingly. In this process, additional information helps them form opinions and they thus become more certain about their beliefs. Following a similar logic, Equation (7) suggests that when individuals read more microblogs on a specific topic, the posterior variance of individual opinion decreases. As a result, individuals become more and more certain about their opinion on this topic. This is consistent with extensive prior literature (such as Hawkins & Hoch, 1992) where individuals are more certain about their opinions when they are repeatedly exposed to information from peers.

We also included a dummy variable $D I D _ { t p }$ in Equation (7) to capture the effect of the interaction between microblogs and the treatment on opinion formation. When this coefficient of $\mathrm { D I D } _ { \mathrm { t p } } \left( \rho _ { 1 } \right)$ is positive, shutting down the reply function will increase the posterior variance $\sigma _ { i m n } ^ { 2 } .$ , and consequently reduce individual certainty about a topic. Furthermore, based on Equation (6), a larger posterior variance $\sigma _ { i m n } ^ { 2 }$ will reduce the value of the Kalman gain coefficient and, consequently, the impact of microblogs on opinion.

As a final note on the identification of parameters in this Bayesian learning framework, $\sigma _ { A } ^ { 2 }$ is identified as we observe the change of sentiment of an individual’s microblog within a microblog chain. When the change is large, $\sigma _ { A } ^ { 2 }$ will be large, assuming everything else is the same. In addition, the impacts of covariates other than the ones associated with the dummy variable are evaluated based on the variation in exogenous characteristics for identification.

## The Likelihood Function of Writing Microblogs

Note that if we only include the observed microblogs in the estimation dataset, the dataset will be truncated and the estimation results could be potentially biased. Previous literature has suggested that reported online reviews may suffer from self-selection bias because users are more likely to post positive reviews than negative reviews (Dellarocas & Wood, 2008). Similarly, we would expect individuals with different opinions to have a different propensity for posting microblogs. As a result, we need to explicitly model the decision to post microblogs as a function of individual opinions. Specifically, we include individual opinion as well as previous microblog generating frequency in the decision to post microblogs in order to account for endogeneity. In addition, we incorporate the number of followers of individual ?? in the model for posting microblogs. One reason for doing so is that individuals with a large number of followers may have a greater incentive to write more microblogs to maintain their social status on the platform. The second possible reason is that they may know that their microblogs will attract a larger viewership and therefore have more incentive to write microblogs (Huang et al., 2014). We write the conditional probability of individual ?? writing a microblog at level ?? for microblog chain ?? given individual opinion and characteristics as a Probit function:

$$
P r (b _ {i m n} | s _ {i m n}, \pmb {X _ {i}}) = \frac {e x p (\gamma_ {0} + \gamma_ {1} \pmb {X _ {i}} + \gamma_ {2} s _ {i m n})}{1 + e x p (\gamma_ {0} + \gamma_ {1} \pmb {X _ {i}} + \gamma_ {2} s _ {i m n})},\tag{8}
$$

where $b _ { i m n } = 1$ if individual ?? writes a microblog at level ?? for microblog chain ??, and zero otherwise. $X _ { i }$ captures the impact of observed individual characteristics on the propensity to write microblogs. Here, we include the number of followers and the frequency of writing microblogs (measured by the number of microblogs per day in the previous month) in $X _ { i } .$

Given the conditional probability in Equation (3), we can calculate the probability that individual ?? writes a microblog with opinion $s _ { i m n }$ at level ?? of microblog chain ??:

$$
P r (s _ {i m n}, b _ {i m n} | \pmb {X} _ {i}) = P r (b _ {i m n} | s _ {i m n}, \pmb {X} _ {i}) * P r (s _ {i m n} | \pmb {X} _ {i}),\tag{9}
$$

Notice that $P r ( s _ { i m n } | X _ { i } )$ in Equation (9) is the individual posterior opinion calculated based on Equation (3). While this individual posterior opinion in Equation (9) follows a normal distribution, our calculated sentiment, denoted as $\bar { s } _ { i m n }$ , can only take discrete values (negative, neutral, and positive). Thus we update Equation (9) above to Equation (9<sup>′</sup>) by using an ordered probit model:

$$
P r (\bar {s} _ {i m n}, b _ {i m n} | \pmb {X} _ {i}) = P r (b _ {i m n} | s _ {i m n}, \pmb {X} _ {i}) * P r o b i t (\bar {s} _ {i m n} | \pmb {X} _ {i}),\tag{\( (9') \}
$$

Next, we derive the likelihood function based on the probability function in Equation (9). On microblogging platforms such as Twitter, individuals can choose to follow other users on the platform. Whenever a followee posts a microblog on the platform, the platform will send notifications and display these microblogs on their screen. In other words, individuals update their opinion only when a microblog is posted by their followee; otherwise, their opinion is likely to remain the same. As a result, it is intuitive to assume that individuals make the decision to retweet microblogs only when one of their followees posts a microblog. Hence, the likelihood function can be expressed as:

$$
L = \sum_ {i, m, n} P r (\bar {s} _ {i m n}, b _ {i m n} | \pmb {X} _ {i}) I (b _ {m n - 1} \in G _ {i}),\tag{10}
$$

where we use $G _ { i }$ to represent the network structure of individual ?? . $I ( b _ { m n - 1 } \in G _ { i } ) = 1$ if a user who individual ?? follows posts a microblog at level (?? − 1) of microblog chain ?? and zero otherwise. By maximizing the likelihood function above, we can infer the mechanism of opinion formation through the observed sentiment of microblogs that users post on the platform.

Note that we also control for individual unobserved heterogeneity in our model. Please refer to Appendix C for more details on unobserved heterogeneity and the data generation process of our model.

## Bayesian Learning Model Results

We present our estimation results in Table 4. We first discuss the estimation results associated with opinion extremity on this social media platform and then move to other estimation results that are of significant interest for the opinion formation mechanism.

<table><tr><td colspan="2">Table 4. Estimation Results</td></tr><tr><td>Variables</td><td>Posterior mean opinion</td></tr><tr><td colspan="2">Microblog opinion formation</td></tr><tr><td colspan="2">Formation of posterior opinion</td></tr><tr><td>Peer influence weight ( $\varphi_0$ )</td><td>0.220***</td></tr><tr><td>Impact of treatment on posterior mean opinion ( $\varphi_1$ )</td><td>0.025**</td></tr><tr><td>Impact of treatment on opinion extremity ( $\varphi_2$ )</td><td>-0.029***</td></tr><tr><td>Interaction between treatment and social media participation ( $\varphi_3$ )</td><td>-0.005**</td></tr><tr><td>Impact of treatment on posterior variance ( $\rho_1$ )</td><td>0.055**</td></tr><tr><td>Prior accuracy variance ( $\sigma_A^2$ )</td><td>3.789***</td></tr><tr><td>Time-fixed effect</td><td>Yes</td></tr><tr><td>Platform-fixed effect</td><td>Yes</td></tr><tr><td colspan="2">Prior opinion</td></tr><tr><td>Average of individual prior opinion across population—first component ( $\alpha_{10}$ )</td><td>0.266***</td></tr><tr><td>Average of individual prior opinion across population—second component ( $\alpha_{20}$ )</td><td>-0.067***</td></tr><tr><td>Probability of belong to first component ( $p_s$ )</td><td>0.641***</td></tr><tr><td>Sentiment of same chain microblogs from followees in previous month</td><td>0.308***</td></tr><tr><td>Number of Microblogs in previous month</td><td>0.018</td></tr><tr><td>Number of followers</td><td>0.147**</td></tr><tr><td>Individual average opinions from past microblogs</td><td>0.194**</td></tr><tr><td>Prior opinion variance shape parameter ( $\alpha_\sigma$ )</td><td>2.767***</td></tr><tr><td>Prior opinion variance scale parameter ( $\beta_{\sigma0}$ )</td><td>0.262***</td></tr><tr><td>Previous variance of microblog ( $\beta_{\sigma1}$ )</td><td>0.051**</td></tr><tr><td>Finance</td><td>-0.062</td></tr><tr><td>IT</td><td>-0.016</td></tr><tr><td>Entertainment</td><td>0.155*</td></tr><tr><td>Sports</td><td>0.098*</td></tr><tr><td>Education</td><td>-0.023</td></tr><tr><td>Equipment</td><td>-0.034</td></tr><tr><td>Women/home</td><td>0.118**</td></tr><tr><td>Writing microblog</td><td></td></tr><tr><td>Posterior opinion mean</td><td>-0.559***</td></tr><tr><td>Frequency of posting microblogs in previous month</td><td>0.036***</td></tr><tr><td>Number of followers</td><td>0.139***</td></tr><tr><td>Constant</td><td>-3.078***</td></tr></table>

Note: Significance: \*\*\*1%; \*\*5%; \*10%. We use automobiles as the baseline category.

## Opinion Extremity in the Bayesian Model

The main focus of this research is to investigate the mechanism of opinion polarization on social media platforms. Note that during the treatment period, the reply function was shut down and no new replies could be posted during this period. Therefore, the coefficients for the treatment dummy $( \varphi _ { 2 } )$ should be interpreted in the reverse direction of the impact of replies.

The coefficient of the treatment for opinion extremity $( \varphi _ { 2 } )$ is negative and significant. This suggests that shutting down replies decreases opinion extremity and that replies thus increase opinion extremity. This result is consistent with the results discussed in the Aggregate-Level Model section, and again supports H1b.

Next, the coefficient of the interaction between the treatment and social media participation level $( \varphi _ { 3 } )$ is the same as $\varphi _ { 2 } ,$ and is also negative and significant. This result supports H2. Together with the result that shutting down replies reduces extremity, this suggests that the negative impact of reply shutdown on opinion extremity is larger for users with higher levels of social media participation. Following our discussion in the Theoretical Foundations section, individuals with higher levels of social media participation are more likely to be exposed to diverse information (e.g., Brundidge, 2010). More importantly, this result suggests that in the context of Weibo.com, users with high levels of social media participation employ such diverse information to further support their existing beliefs, making their views even more polarized (Lee et al., 2014). As discussed in the Theoretical Foundations section, one of the mechanisms behind H2 is confirmation bias. This coefficient for the interaction term thus provides additional empirical support for confirmation bias being an important mechanism behind the formation of user opinion on microblogging platforms. We discuss the managerial implications of these findings in more detail in a later section.

## Other Parameters

The coefficient of peer influence weight $( \varphi _ { 0 } )$ is positive and significant. This shows that individuals on the platform were indeed influenced by their peers, resulting in their opinions becoming more similar to those of their networked peers on the platform. The impact of the treatment (shutting down the reply function, $\varphi _ { 1 } )$ on the posterior mean opinion is positive and significant, showing that replies lead to a more negative sentiment among users.

The posterior variance of individual opinions measures individual uncertainty about a specific topic. The impact of treatment on posterior variance ${ \bf \Xi } ( { \bf \Lambda } \rho _ { 1 } { \bf \Lambda } )$ is positive and significant. Thus, individual uncertainty about a specific topic increased when Weibo shuts down the reply function, indicating that replies decrease individual uncertainty about a specific topic.

Prior opinion represents individual opinion without the influence of information from a social media platform. The coefficient of sentiment of the same chain of microblogs from followees is positive and significant; thus, individual prior opinion is also positively influenced by followees’ previous posts. Second, the coefficient of the number of microblogs is insignificant, meaning that user participation level on the platform has no impact on prior opinion. Third, the coefficient of the number of followers is significant and positive. This indicates that the individuals who are more connected in the online network tend to have a more positive prior opinion compared to those with fewer followers. Fourth, the coefficient of the average opinion from past microblogs is positive and significant. This suggests that individuals who demonstrate positive sentiment in the past are more likely to post positive microblogs in the future, and vice versa.

Lastly, we examine the coefficients related to the individual decision to write microblogs. First, the coefficient of the individual posterior mean opinion is negative and significant, meaning individuals are more likely to retweet microblogs if they have more negative opinions. This contrasts with previous theories suggesting that individuals are more likely to express positive opinions than negative opinions (Dellarocas & Woods, 2008). Second, the frequency of posting microblogs in the past has a positive and significant impact on the propensity to post microblogs. This factor controls for the observed individual heterogeneity in the propensity to post microblogs. The more frequently a user posted microblogs previously, the more likely it is that the user will post in the current period. Third, the coefficient of the number of followers is also positive and significant after controlling for the individual frequency of writing microblogs. One potential reason is that users with large numbers of followers are more incentivized to write more microblogs (than those with only a few followers) because they know their microblogs will have a large readership.

## Empirical Evidence on Confirmation Bias

Our estimation results for both the aggregate-level model and the Bayesian learning model suggest that replies increase opinion polarization on microblogging platforms. In the Theoretical Foundations section, we argue that one potential mechanism explaining how replies increase polarization is confirmation bias. In this section, we revise our Bayesian learning model by explicitly incorporating confirmation bias to provide empirical evidence supporting this claim.

On the Weibo platform, to access replies associated with a microblog, users need to click the “reply” button right below the microblog text. Because of this design, platform users will always first be exposed to microblogs before they are exposed to corresponding replies. As a result, we explicitly model one type of confirmation bias in our Bayesian learning model: when individuals are first exposed to the microblog, replies that have different sentiment from this microblog may be discounted.

Such a model setup follows previous literature in which user-generated content can bias subsequent opinions, thus providing evidence for the existence of confirmation bias on social media platforms. For example, Yin et al. (2016) examined confirmation bias, showing that if individuals are exposed to positive (negative) information first, they will perceive subsequent positive (negative) reviews to be more helpful and vice versa. Jin et al. (2018) also demonstrated that the timing of information has an important impact on subsequent individual opinions.

Note that reply sentiment data is needed to evaluate the heterogeneous impact of replies that confirm related microblogs versus that of replies that oppose related microblogs. Thus, we only use Weibo data without Sohu Weibo data, as the Sohu Weibo reply text was not available when we collected the data. We first revise Equation (5) to explicitly incorporate confirmation bias:

$$
\begin{array}{r l} & {\left(F _ {i m n} \big | s _ {m 1} ^ {(i)}, s _ {m 2} ^ {(i)}, \ldots , s _ {m n - 1} ^ {(i)}\right) =} \\ & {E \big (F _ {i m n} \big | s _ {m 1} ^ {(i)}, s _ {m 2} ^ {(i)}, \ldots , s _ {m n - 2} ^ {(i)} \big) + \beta_ {i m n - 1} \left(s _ {m n - 1} ^ {(i)} - \right.} \\ & {\left. E \big (s _ {m n - 1} ^ {(i)} \big | s _ {m 1} ^ {(i)}, s _ {m 2} ^ {(i)}, \ldots , s _ {m n - 2} ^ {(i)} \big)\right)} \\ & {+ \delta_ {1} c s a m e _ {i m n - 1} + \delta_ {2} c d i f f _ {i m n - 1}} \end{array}\tag{11}
$$

Instead of using the exogenous shock (e.g., the shutdown of replies) in Equation (5), we now include $c s a m e _ { i m n - 1 }$ and $c d i f f _ { i m n - 1 }$ in Equation (11) to capture the confirmation bias we mentioned earlier. Here, ???????? $\scriptstyle { \dot { \cdot } } _ { i m n - 1 }$ and $c d i f f _ { i m n - 1 }$ are the number of replies for the $n ^ { t h }$ microblog within microblog chain ?? , which are of the same/different sentiment as this microblog. As a simple example, if the $n ^ { t h }$ microblog within topic ?? has negative sentiment about a topic, and among all replies on this specific microblog, there are three replies with negative sentiment and four replies with nonnegative sentiment, then the value of ??????????<sub>????</sub> <sub>−</sub> and $c d i f f _ { i m n - 1 }$ will be 3 and 4, respectively. In this case, if the absolute value of $\delta _ { 1 }$ is larger than that of $\delta _ { 3 }$ , the existence of confirmation bias is indicated in our context.

Following the same logic, we also revise Equation (7), the calculation of $\sigma _ { i m n } ^ { 2 }$ in the Kalman gain coefficient:

$$
\frac {1}{\sigma_ {i m n} ^ {2}} = \frac {1}{\sigma_ {m} ^ {2}} + \delta_ {3} \sum_ {j = 1} ^ {n} c s a m e _ {i m j - 1} + \delta_ {4} \sum_ {j = 1} ^ {n} c d i f f _ {i m j - 1}\tag{12}
$$

We included the number of replies and the standard deviation of reply sentiment in Equation (12) to capture the impact of replies on the posterior variance of individual opinions. If $\bar { \delta _ { 3 } } > 0$ , a larger number of replies with the same sentiment will lead to a larger value of $\frac { 1 } { \sigma _ { i m n } ^ { 2 } } ;$ thus, individual ?? will be more certain about the topic. Following similar logic, if $\delta _ { 4 } < 0$ , when individual ?? is exposed to a larger number of replies with different sentiment, individuals will be less certain about the topic. We did not include the treatment variable, as our focal treatment does not contribute to distinguishing the impact of replies with similar sentiment from that of replies with different sentiment. As such, we only included the observations within two weeks before treatment. For simplicity, we present the key estimation results in Table 5 only.

The impact of previous replies with the same sentiment on the posterior mean opinion $( \delta _ { 1 } )$ is positive and significant, while that of previous replies with different sentiment $( \delta _ { 2 } )$ is insignificant. This demonstrates that compared with replies with consistent sentiment, individuals heavily discount replies that are inconsistent with related microblogs. This provides additional evidence on replies increasing opinion polarization through confirmation bias.

## Performance Test

One of the advantages of the Bayesian learning model is that by controlling for individual prior opinion and explicitly modeling the opinion updating process, the predictive power of the model can be significantly improved. To demonstrate the predictive power of the Bayesian learning model compared with the aggregate-level model, we compare the performance of these two models. Because the dependent variables in these two models are different, we used polarization (i.e., standard deviation of microblog sentiment) of microblog chain ?? on platform ?? in period ?? as the prediction objective to compare model performance. We randomly selected 80% of the data as the training sample, and the remaining 20% of data as the calibration dataset. The RMSE (root-mean-squared error) for the aggregate-level model is 0.17, while that for the Bayesian learning model is 0.12. The MAE (mean absolute error) for the aggregate-level model is 0.13 and for the Bayesian learning model it is 0.09. The significant improvements over both RMSE and MAE demonstrate that using the Bayesian learning model significantly improves the model’s predictive power.

## Robustness Checks

In this section, we present a series of robustness checks to demonstrate that our results are unlikely to be biased by potential confounding factors. Because the focus of our paper is on opinion polarization, we only report results for Equation (1), where the dependent variable is microblog polarization $( P o l a r M _ { m t p } )$ . Note that we still estimate Equations (1) and (2) simultaneously in robustness checks below. Because of space limitations, we only include robustness checks for aggregatelevel model; robustness checks for Bayesian learning model can be found in Appendix E.

<table><tr><td colspan="2">Table 5. Modeling Confirmation Bias in Bayesian Learning Model</td></tr><tr><td>Variables</td><td>Posterior mean opinion</td></tr><tr><td colspan="2">Microblog opinion formation, formation of posterior opinion</td></tr><tr><td>Peer influence weight ( $\varphi_0$ )</td><td>0.285***(0.049)</td></tr><tr><td>Impact of previous replies number with the same sentiment on posterior mean opinion ( $\delta_1$ )</td><td>0.006**(0.003)</td></tr><tr><td>Impact of previous replies number with different sentiment on posterior mean opinion ( $\delta_2$ )</td><td>-0.001 (0.002)</td></tr><tr><td>Impact of previous replies number with the same sentiment on posterior variance ( $\delta_3$ )</td><td>0.002**(0.001)</td></tr><tr><td>Impact of previous replies number with different sentiment on posterior variance ( $\delta_4$ )</td><td>0.000*(0.000)</td></tr></table>

Note: Standard error in parentheses. Significance: \*\*\*1%; \*\*5%; \*10%.

## Reply Characteristics and the A-B-A Setting

It may be argued that it is important to control for reply characteristics in our model setup. Unfortunately, given the significant time that has elapsed since the treatment in this study occurred, reply texts are no longer available for Sohu Weibo. As a result, we cannot present a DID model with reply characteristics. However, we do want to emphasize that our main identification strategy relies on the unique natural experiment in this study; thus, omitting reply characteristics in the estimation model is unlikely to bias our estimation results.

Nonetheless, we conducted a robustness check in which we included reply characteristics, but we do not include Sohu Weibo as the control group in Table 6. Instead, we include $P o l a r C _ { m t - 1 }$ and $N u m C _ { m t - 1 }$ to denote the standard deviation of sentiment and number of replies of the corresponding microblogs in period ?? − 1 in Table 6.

One of the advantages of our experimental setting is that we collected data both before and after the three-day treatment period. Thus, in this robustness check, we further constructed two separate estimation datasets; the first dataset consists of a period before and during treatment (March 17 to April 2, 2012) and the second one consists of a period during and after the treatment (March 31 to April 16, 2012). This allowed us to alleviate the potential concern that the opinion polarization level on this social media platform changed over time. For example, it is possible that when users are on the platform longer, their opinions may be more likely to be shaped by their conversations with others with similar mindsets, making them more polarized over time.

As shown in Table 6, our results are robust whether we use the data for the A-B period or the data for the B-A period. In particular, the coefficients before the focal variable ????????????ℎ?????????????????????????? are negative and significant for both of these two models. This is consistent with our aggregatelevel model results, which demonstrates that our results are robust after we controlled for reply characteristics; the time trend is thus unlikely to be a confounding factor in our model. Note that the covariates for reply characteristics are endogenous in this regression model and corresponding coefficients could thus be biased. This highlights the importance of employing the natural experiment setting for this model.

## Alternative Sampling Technique and Control Group

In our main analysis, we randomly selected active users and collected corresponding microblogs among genuinely active microblogging users. However, given that the sample size is relatively small compared with the entire Weibo-sphere, it is possible that we only captured a relatively small portion of each of the topics that emerged on Weibo during this period. The resulting dataset is thus not representative of the microblogging sphere as a whole. Ideally, we would collect all Weibo microblogs during our study period. However, even collecting 5% of all microblogs is a very difficult task given the huge volume of data available on Weibo. As an alternative, in this robustness check, we collected all microblogs with top hashtags during our estimation period so that we could construct a complete dataset associated with these top hashtags. Specifically, we first identified the top 500 hashtags during our estimation period based on microblog numbers. We then manually removed all hashtags that are related to social news/politics, as well as the ones with no microblogs during the treatment period. For the remaining 145 hashtags, we then collected all microblogs containing these hashtags, as well as retweets and replies of these microblogs during the estimation period. This allowed us to collect all activities on Weibo related to these 145 hashtags. The resulting dataset contains 305,078 microblogs, and 222,264 replies. This new treatment dataset helped us address the concern that our estimation dataset may not be large enough to represent activities for each of the topics captured in the dataset.

Following our aggregate-level model, we first conducted propensity score matching to match the new treatment dataset based on top hashtags with the Sohu Weibo dataset to construct treatment and control groups. We then estimated the aggregate-level model based on this new treatment and the control datasets. We present the results in Table 7. Our results remain qualitatively the same.

<table><tr><td colspan="3">Table 6. Results with Replies Characteristics</td></tr><tr><td>Variable</td><td>Sentiment polarization before and during treatment (A-B period)</td><td>Sentiment polarization during and after treatment (B-A period)</td></tr><tr><td> $PolarM_{mt-1}$ </td><td>0.039***(0.003)</td><td>0.053***(0.004)</td></tr><tr><td> $NumM_{mt-1}$ </td><td>-0.008***(0.000)</td><td>-0.012***(0.000)</td></tr><tr><td> $PolarC_{mt-1}$ </td><td>0.205***(0.067)</td><td>0.190***(0.062)</td></tr><tr><td> $NumC_{mt-1}$ </td><td>0.001***(0.000)</td><td>0.001***(0.000)</td></tr><tr><td> $NumUser_{mt-1}$ </td><td>0.024***(0.008)</td><td>0.023***(0.008)</td></tr><tr><td>Reply-shutdown period ( $T_t$ )</td><td>-0.018***(0.006)</td><td>-0.014***(0.005)</td></tr><tr><td> $Weekend_t$ </td><td>-0.003*(0.002)</td><td>-0.008*(0.004)</td></tr><tr><td>Topic-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>0.289***(0.003)</td><td>0.316***(0.004)</td></tr><tr><td> $R^2$ </td><td>0.367</td><td>0.347</td></tr></table>

Note: Standard error in parentheses. Significance: \*\*\*: 1%; \*\*: 5%; \*: 10%

<table><tr><td colspan="2">Table 7. Robustness Checks with Alternative Sampling Strategy</td></tr><tr><td>Variable</td><td>Sentiment polarization</td></tr><tr><td> $PolarM_{mt-1}$ </td><td>0.036***(0.004)</td></tr><tr><td> $NumM_{mt-1}$ </td><td>-0.005***(0.000)</td></tr><tr><td> $NumUser_{mt-1}$ </td><td>0.028***(0.006)</td></tr><tr><td> $DID_{tp}$ </td><td>-0.017***(0.002)</td></tr><tr><td>Is Weibo ( $P_p$ )</td><td>0.022***(0.000)</td></tr><tr><td>Reply-shutdown period ( $T_t$ )</td><td>0.002*(0.001)</td></tr><tr><td> $Weekend_t$ </td><td>-0.007*(0.004)</td></tr><tr><td>Topic-fixed effect</td><td>Yes</td></tr><tr><td>Constant</td><td>0.215***(0.005)</td></tr><tr><td> $R^2$ </td><td>0.364</td></tr></table>

Note: Standard error in parentheses. Significance: \*\*\*1%; \*\*5%; \*10%.

## An Alternative Control Group Using Twitter

In our main analysis, we used Sohu Weibo, another major microblogging platform in China as the control group. However, it is possible that microblogs and replies on Sohu Weibo are also influenced by the political event that triggered our treatment. Because we focused on nonpolitical microblogs, we believe the impact of the reply shutdown on such microblogs is unlikely to be confounded with potential political factors. Nonetheless, to further demonstrate that our results are robust regarding potential political factors, we employed an alternative control group in this robustness check. Specifically, based on the 145 topics we chose in the previous robustness checks, we collected tweets with the same hashtag on Twitter.com.<sup>20</sup> Because tweets on Twitter were very unlikely to be censored on the basis of the political event that triggered the reply shutdown on Weibo, we believe that this dataset from Twitter is a good candidate for the control group in our study. The results, shown in Table 8, are qualitatively similar.

## Falsification Test

To further alleviate the concern regarding a potential time trend as a confounding factor, we conducted a falsification test in this subsection. Specifically, we conducted two falsification tests in which we used false time as the treatment. In the pre-treatment period, we changed the treatment time to the start of the second week of our estimation period (March 24-March 26) and used the first two weeks of data as the estimation dataset.

<table><tr><td colspan="2">Table 8. Robustness Check with Twitter as the Control Group</td></tr><tr><td>Variable</td><td>Sentiment polarization</td></tr><tr><td> $PolarM_{mt-1}$ </td><td>0.022***(0.005)</td></tr><tr><td> $NumM_{mt-1}$ </td><td>-0.015***(0.002)</td></tr><tr><td> $NumUser_{mt-1}$ </td><td>0.041***(0.013)</td></tr><tr><td> $DID_{tp}$ </td><td>-0.021**(0.010)</td></tr><tr><td>Is Weibo ( $P_p$ )</td><td>0.012***(0.001)</td></tr><tr><td>Reply-shutdown period ( $T_t$ )</td><td>0.008**(0.004)</td></tr><tr><td> $Weekend_t$ </td><td>-0.000 (0.001)</td></tr><tr><td>Topic-fixed effect</td><td>Yes</td></tr><tr><td>Constant</td><td>0.142***(0.007)</td></tr><tr><td> $R^2$ </td><td>0.305</td></tr></table>

Note: Standard error in parentheses. Significance: \*\*\*1%; \*\*5%; \*10%.

<table><tr><td colspan="3">Table 9. Robustness Check with Falsification Test</td></tr><tr><td>Variable</td><td>Polarization before treatment</td><td>Polarization after treatment</td></tr><tr><td> $PolarM_{mt-1}$ </td><td>0.069***(0.005)</td><td>0.056***(0.004)</td></tr><tr><td> $NumM_{mt-1}$ </td><td>-0.009***(0.000)</td><td>-0.006***(0.000)</td></tr><tr><td> $NumUser_{mt-1}$ </td><td>0.013***(0.006)</td><td>0.022***(0.007)</td></tr><tr><td> $DID_{tp}$ </td><td>0.003 (0.005)</td><td>-0.001 (0.003)</td></tr><tr><td>Is Weibo ( $P_p$ )</td><td>0.034***(0.000)</td><td>0.015***(0.000)</td></tr><tr><td>Reply-shutdown period ( $T_t$ )</td><td>0.001 (0.002)</td><td>0.002 (0.002)</td></tr><tr><td> $Weekend_t$ </td><td>-0.006*(0.003)</td><td>-0.004*(0.002)</td></tr><tr><td>Topic-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>0.254***(0.003)</td><td>0.266***(0.003)</td></tr><tr><td> $R^2$ </td><td>0.337</td><td>0.329</td></tr></table>

Note: Standard error in parentheses. Significance: \*\*\*1%; \*\*5%; \*10%.

For the post-treatment period, we changed the treatment time to the start of the second week after the actual treatment ended (April 9-April; 11) and used the two weeks after the treatment period ended as the estimation dataset. We present the results of these two estimations below. Because the focus of this research is on opinion polarization, we present the results for the model using sentiment polarization as a dependent variable. As seen in Table 9, the coefficients before $D I D _ { t p }$ are now insignificant. This alleviates the concerns about a potential time trend being a confounding factor.

## Conclusions and Managerial Implications

With the development of social media technologies, opinion polarization on social media platforms has stimulated intense discussions among academic researchers and practitioners.

While managing consumer product uncertainty is challenging for marketing initiatives (Castaño et al., 2008), opinion polarization on social media platforms imposes additional difficulties, as potential adopters are exposed to different opinions generated from previous peer consumers. In addition, the notion of the “echo chamber” has also attracted significant attention in recent years, given public fears that polarized opinions may lead to a fragmented society.

In this study, we focus on the impact of replies on opinion polarization on microblogging platforms. As an important feature that invites out-of-network users to join conversations on microblogging platforms, the reply function is under increasing scrutiny, particularly given the recent policy changes in the reply function on Twitter. This has been further exacerbated due to the recent legal battle between President Trump and the U.S. Appeals Court regarding whether the president can block certain users based on their replies. However, there is a scarcity of research regarding the impact of replies on opinion formation, not to mention opinion polarization.

In this paper, we employ a unique natural experimental setting and identify the impact of replies on individual opinion polarization. This study is one of the first to empirically investigate individual opinion polarization on a social media platform using microlevel data. Many practitioners and commentators argue that out-of-network information such as Twitter replies can bring together individuals with opposing views and can thus help break the echo chamber and alleviate polarization on social media platforms. However, our results demonstrate that replies from the general public, in fact, significantly increase opinion polarization on social media platforms. We further provide empirical evidence demonstrating that confirmation bias is an important channel for the positive impact of replies on opinion polarization. In other words, individuals self-select into consuming replies that share similar opinions, even when they are provided with information from outside of their existing network. Our study further demonstrates that the positive impact of replies on opinion polarization is even stronger for individuals with a higher level of social media participation.

Our results have several significant managerial implications for social media strategies for firms.<sup>21</sup> From a platform design perspective, our findings suggest that platforms should be cautious when they implement features intended to expose users to more heterogeneous information. In particular, while academics and practitioners are now advocating for the design of recommender systems that can introduce diverse information (Jiang et al., 2019), our research shows that this may not necessarily reduce opinion polarization. One potential design to reduce opinion polarization could be to provide aggregate summary statistics of user-generated content. For instance, Yelp provides numerical scores averaged across all reviews. Likewise, Amazon also highlights a most-helpful positive review and a most-helpful negative review for their products. However, we also wish to remind practitioners to interpret our results with caution, as our results should not be interpreted as predicting that Twitter’s new feature of allowing users to select who can reply to posts will inevitably lead to lower opinion polarization. Indeed, preventing certain users from replying may itself trigger more polarized opinions on the platform. In addition, this new feature is also different from our research setting in the sense that replies are completely shut down in our context whereas Twitter’s new initiative will screen replies.

From a marketing practitioner’s perspective, our results provide two insights into social media strategies. First, previous studies on social media strategies have largely focused on how to leverage customer social networks to better engage customers when conducting social media campaigns. However, our study demonstrates a significant challenge in managing replies because posting positive content is unlikely to change the opinion of users with opposing views. In addition, our study provides managerial implications on targeting social media users in marketing campaigns. While marketing practitioners primarily target individuals with large numbers of followers, our study shows that companies should also take into account subsequently generated replies because followers with heterogeneous opinions are more likely to generate polarized opinions in replies, which can negatively influence marketing campaign performance. Thus, it may be more beneficial for companies to target individuals with fewer followers but more homogenous opinions, rather than targeting individuals with large numbers of followers who have different opinions. Second, our results demonstrate that individuals with high participation levels are more likely to have polarized opinions due, in part, to replies. Thus, companies may consider leveraging more resources toward users with high participation levels who tend to express negative opinions about the company or its products rather than devoting attention to users with more favorable opinions.

Our research also has several limitations. First, we focused on the impact of replies on opinion polarization among ordinary users on a social media platform. Thus, we selected individuals with 200-3000 followers in this study. Because “online celebrities” with large numbers of followers have different incentive structures on social media platforms than ordinary users, whether our results can be generalized to such users is worthy of further exploration. Previous research has suggested that elite individuals tend to be more polarized than the general public (Abramowitz & Saunders, 2008). Therefore, the impact of replies may be even higher for elite users, as replies provide an additional incentive for them to express their opinion. Second, due to data limitations, we only explored confirmation bias as a mechanism driving our main results. Thus the conditions under which the provision of exogenous information such as replies can have a positive versus negative influence on opinion polarization remains unclear. We leave other potential mechanisms for future research to explore. Third, another data limitation is that we did not have data on user viewing history. Accessing viewing history would help us better capture how information other than previous microblogs in the same chain could influence opinion polarization and help model individual decisions to post replies. Fourth, one of the focuses of this study is the moderating role of social media participation on the impact of replies on opinion polarization. It would be interesting to investigate how other network characteristics might influence the opinion formation process and opinion polarization—in particular, whether individuals embedded in networks with different community characteristics (e.g., community density, clustering coefficients) are influenced by replies differently.

## Acknowledgments

Dr. Junjie Wu’s work was partially supported by the National Natural Science Foundation of China (71725002, 72031001, 72021001), and Key Projects of Science and Technology Program of Beijing Municipal Education Commission (KZ202110017025). Dr. Jian Chen’s work was partially supported by the National Natural Science Foundation of China (71490723).

## References

Abramowitz, A. I., & Saunders, K. L. (2008). Is polarization a myth? The Journal of Politics, 70(2), 542-555.

Ackerberg, D. A. (2003). Advertising, learning, and consumer choice in experience good markets: An empirical examination. International Economic Review, 44(3), 1007-1040.

Allahverdyan, A.E., & Galstyan, A. (2014). Opinion dynamics with confirmation bias. PloS One, 9(7), Article e99557.

Aral, S., & Walker, D. (2011). Creating social contagion through viral product design: a randomized trial of peer influence in networks. Management Science, 57(9), 1623-1639.

Bail, C. A., Argyle, L. P., Brown, T. W., Bumpus, J. P., Chen, H., Hunzaker, M. F., & Volfovsky, A. (2018). Exposure to opposing views on social media can increase political polarization. In Proceedings of the National Academy of Sciences, 115(37), 9216-9221.

Ball, R., & Brown, P. (1968). An empirical evaluation of accounting income numbers. Journal of Accounting Research, 6(2), 159-178

Bakshy, E., Messing, S., & Adamic, L. A. (2015). Exposure to ideologically diverse news and opinion on Facebook. Science, 348(6239), 1130-1132.

Barberá, P., Jost, J. T., Nagler, J., Tucker, J. A., & Bonneau, R. (2015). Tweeting from left to right: Is online political communication more than an echo chamber? Psychological Science, 26(10), 1531-1542.

Bapna, R., & Umyarov, A. (2015). Do your online friends make you pay? A randomized field experiment on peer influence in online social networks. Management Science, 61(8), 1902- 1920.

Beese, J. (2011). Social networks influence 74% of consumers’ buying decisions. Sproutsocial. http://sproutsocial.com/ insights/social-networks-influence-buying-decisions/

Bindel, D., Kleinberg, J., & Oren, S. (2011). How bad is forming your own opinion. In Proceedings IEEE 52nd Annual Symposium on Foundations of Computer Science.

Boxell, L., Gentzkow, M., & Shapiro, J. M. (2017). Greater internet use is not associated with faster growth in political polarization

among US demographic groups. In Proceedings of the National Academy of Sciences, 114(40), 10612-10617.

Brundidge, J. (2010). Encountering “difference” in the contemporary public sphere: The contribution of the internet to the heterogeneity of political discussion networks. Journal of Communication, 60(4), 680-700.

Campaign. (2016). Twitter makes @replies public and drops multimedia from 140-character count. https://www. campaignlive.co.uk/article/twitter-makes-replies-publicdrops-multimedia-140-character-count/1396186

Castaño, R., Sujan, M., Kacker, M., & Sujan, H. (2008). Managing consumer uncertainty in the adoption of new products: Temporal distance and mental simulation. Journal of Marketing Research, 45(3), pp.320-336.

Chevalier, J., & Mayzlin, D. (2006). The effect of word of mouth on sales: Online book reviews. Journal of Marketing Research, 43(3), 345-354.

Chiang, C. F., & Knight, B. G. (2011). Media bias and influence: Evidence from newspaper endorsements. The Review of Economic Studies, 78(3), 795-820.

Cho, H., Boster, F. J. (2005). Development and validation of value-, outcome-, and impression-relevant involvement scales. Communication Research, 32(2), 235-264.

Conover, M., Ratkiewicz, J., Francisco, M. R., Gonçalves, B., Menczer, F., & Flammini, A. (2011). Political polarization on Twitter. Proceedings of the Fifth International AAAI Conference on Weblogs and Social Media, 5(1), 89-96.

Cover, T. M., & J. A. Thomas. (2012). Elements of information theory. Wiley.

Dai, W., Jin, G., Lee, J., & Luca, M. (2018). Aggregation of consumer ratings: An application to Yelp.com. Quantitative Marketing and Economics, 16(3), 289-339.

Degroot, M. (1970). Optimal statistical decisions. McGraw-Hill

DeGroot, M. (1974). Reaching a consensus. Journal of the American Statistical Association, 69(345), 118-121.

Dellarocas, C., & Wood, C. (2008). The sound of silence in online feedback: Estimating trading risks in the presence of reporting bias. Management Science, 54(3), 460-476.

DellaVigna, S., & Gentzkow, M. (2010). Persuasion: Empirical evidence. Annual Review of Economics, 2(1), 643-669.

DeMarzo, P., Vayanos, D., & Zwiebel, J. (2003). Persuasion bias, social influence, and unidimensional opinions. The Quarterly Journal of Economics, 18(3), 909-968.

Durante, R., & Knight, B. (2012). Partisan control, media bias, and viewer responses: Evidence from Berlusconi’s Italy. Journal of the European Economic Association, 10(3), 451-481.

Enikolopov, R., Petrova, M., Zhuravskaya, E. (2010). Media and political persuasion: Evidence from Russia. American Economic Review, 101(7), 3253-3285.

Erdem, T., & Keane, M. (1996). Decision-making under uncertainty: Capturing dynamic brand choice processes in turbulent consumer goods markets. Marketing Science, 15(1), 1-20.

Ewing, M. (2012). 71% more likely to purchase based on social media referrals. Hubspot. http://blog.hubspot.com/blog/tabid/ 6307/bid/30239/71-More-Likely-to-Purchase-Based-on-Social-Media-Referrals-Infographic.aspx

Fan, R.-E., K.-W. Chang, C.-J. Hsieh, X.-R. Wang, and C.-J. Lin. (2008). Liblinear: A library for large linear classification. Journal of Machine Learning Research, 9, 1871-1874.

Festinger, L. (1957). A theory of cognitive dissonance. Stanford University Press

Fishkin, J. S. (2009). When the people speak: Deliberative democracy and public consultation. Oxford University Press.

Flanagin, A. J., & Metzger, M. J. (2013). Trusting expert-versus user-generated ratings online: The role of information volume, valence, and consumer characteristics. Computers in Human Behavior, 29(4), 1626-1634.

Forbes. (2020). Twitter’s new feature to limit replies could exacerbate echo chambers. Forbes. https://www.forbes.com/ sites/rebeccabellan/2020/05/21/twitters-new-feature-to-limitreplies-could-exacerbate-echo-chambers/#10fde8905432

Gentzkow, M., & Shapiro, J. M. (2006). Media bias and reputation. Journal of Political Economy, 114(2), 280-316.

Gentzkow, M., & Shapiro, J.M. (2010). What drives media slant? Evidence from U.S. daily newspapers.” Econometrica, 78(1), 35-71.

Gentzkow, M., & Shapiro, J. M. (2011). Ideological segregation online and offline. The Quarterly Journal of Economics, 126(4), 1799-1839.

Gerber, A., Gimpel, J., Green D., & Shaw D. (2011). How large and long-lasting are the persuasive effects of televised campaign ads? Results from a randomized experiment. American Political Science Review, 105(1), 135-150.

Greenstein, S., Gu, G., & Zhu, F. (2021). Ideology and composition among an online crowd: Evidence from Wikipedians. Management Science, 67(5), 3067-3086.

Godbole, S., & S. Sarawagi. (2004). Discriminative methods for multi-labeled classification. Springer.

Godes, D., & Silva, J. C. (2012). Sequential and temporal dynamics of online opinion. Marketing Science, 31(3), 448-473.

Golub, B., & Jackson, M. O. (2010). Naïve learning in social networks: Convergence, influence and the wisdom of crowds. American Economics Journal: Microeconomics, 2(1), 112-149.

Golub, B., & Jackson, M. O. (2012). How homophily affects the speed of learning and best-response dynamics. Quarterly Journal of Economics, 127(3), 1287-1338.

Hardy, B. W., & Scheufele, D. A. (2005). Examining differential gains from internet use: Comparing the moderating role of talk and online interactions. Journal of Communication, 55(1), 71- 84.

Hawkins, S., & Hoch, S. (1992). Low-involvement learning: Memory without evaluation. Journal of Consumer Research, 19(2), 212-225.

Hu, Y., Lodish, L. M., & Krieger, A. M. (2007). An analysis of real world TV advertising tests: A 15-year update. Journal of Advertising Research, 47(3), 341-353

Iyengar, R., van den Bulte, C., Valente, T. W. (2011). Opinion leadership and social contagion in new product diffusion. Marketing Science, 30(2), 195-212

Jeong, M., Zo, H., Lee, C. H., & Ceran, Y. (2019). Feeling displeasure from online social media postings: A study using cognitive dissonance theory. Computers in Human Behavior, 97, 231-240.

Jiang, R., Chiappa, S., Lattimore, T., György, A., & Kohli, P. (2019). Degenerate feedback loops in recommender systems. In Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society (pp. 383-390).

Johnson, B. K., Neo, R. L., Heijnen, M. E., Smits, L., van Veen, C. (2020). Issues, involvement, and influence: Effects of selective

exposure and sharing on polarization and participation. Computers in Human Behavior, 104, Article 106155.

Karypis, G., E.-H. S. Han, and V. Kumar. (1999). Chameleon: Hierarchical clustering using dynamic modeling. Computer, 32(8), 68-75.

Klapper, J. T. (1960). The effects of mass communication. Free Press.

Katz, E., Lazarsfeld, P. (1955). Personal influence: The part played by people in the flow of mass communications. Free Press.

Knowledge Networks. (2011). Social media now influences brand perceptions, purchase decisions of 38 million in U.S. http://www.knowledgenetworks.com/news/releases/2011/061 411\_social-media.html

Kothari, S. P. (2001). Capital markets research in accounting. Journal of Accounting and Economics, 31(1-3), 105-231.

Lawrence, E., Sides, J., & Farrell, H. (2010). Self-segregation or deliberation? Blog readership, participation, and polarization in American politics. Perspectives on Politics, 8(1), 141-157.

Lee, J. K., Choi, J., Kim, C., & Kim, Y. (2014). Social media, network heterogeneity, and opinion polarization. Journal of Communication, 64(4), 702-722.

Liu, Y. (2006). Word of mouth for movies: Its dynamics and impact on box office revenue. Journal of Marketing, 70(3), 74-89.

Lodish, L. M., Abraham, M., Kalmenson, S., Livelsberger, J., Lubetkin, B., Richardson, B., & Stevens, M. E. (1995). How T.V. Advertising works: A meta-analysis of 389 real world split cable T.V. advertising experiments. Journal of Marketing Research, 32(2), 125-139.

Mayzlin, D., & Yoganarasimhan, H. (2012). Link to success: How blogs build an audience by promoting rivals. Management Science, 58(9), 1651-1668.

McClurg, S. D. (2006). The electoral relevance of political talk: Examining disagreement and expertise effects in social networks on political participation. American Journal of Political Science, 50, 737-754.

McPherson, M., Smith-Lovin, L., & Cook, J. (2001). Birds of a feather: Homophily in social networks. Annual Review of Sociology, 27, 415-444.

Meyer, B. D. (1995). Natural and quasi-experiments in economics. Journal of Business & Economic Statistics, 13(2), 151-161.

Moe, W. W., Trusov, M. (2011). The value of social dynamics in online product ratings forums. Journal of Marketing Research, 48(3), 444-456.

Mullainathan, S., & Shleifer, A. (2005). The market for news. The American Economic Review, 95(4), 1031-1053.

Mutz, D. (2002). Cross-cutting social networks: Testing democratic theory in practice. American Political Science Review, 96(1), 111-126.

Mutz, D. (2008). Is deliberative democracy a falsifiable theory? Annual Review of Political Science, 11(1), 521-538.

Nyhan, B., & Reifler, J. (2010). When corrections fail: The persistence of political misperceptions. Political Behavior, 32(2), 303-330.

Olenski, S. (2012). Are brands wielding more influence in social media than we thought? Forbes. http://www.forbes.com/sites/ marketshare/2012/05/07/are-brands-wielding-more-influencein-social-media-than-we-thought/

Park, JaeHong, Prabhudev Konana, Bin Gu, Alok Kumar, and Rajagopal Raghunathan. (2013). Information valuation and

confirmation bias in virtual communities: Evidence from stock message boards. Information Systems Research, 24(4), 1050- 1067.

Perloff, R. M. (1989). Ego-involvement and the third person effect of televised news coverage. Communication Research, 16(2), 236-262.

Mitchell, A., Gottfried, J., Barthel, M., & Shearer, E. (2016). The modern news consumer. Pew Research Center https://www.pewresearch.org/journalism/2016/07/07/themodern-news-consumer/ Pew Research Center

Pettigrew, T. F., & Tropp, L. R. (2006). A meta-analytic test of intergroup contact theory. Journal of Personality and Social Psychology, 90(5), 751-783.

Price, P., R. Jhangiani and I-C. Chiang. (2016). Research methods in psychology. University of Minnesota Libraries Publishing.

Price, V., Cappella, J. N., & Nir, L. (2002). Does disagreement contribute to more deliberative opinion? Political Communication, 19(1), 95-112.

Shi, Z., Rui, H., Whinston, A. B. (2014). Content sharing in a social broadcasting environment: Evidence from Twitter, 38(1), 123- 142.

Sina Tech. (2015). Tianhao Capital: Sina dominates the Weibo app market. http://tech.sina.com.cn/i/2015-02-20/doc-iavxeafs123 6800.shtml

Sina Tech. (2020). Weibo has 516 million monthly active users, and the barriers to competition remain solid. https://tech.sina.com.cn/i/2020-02-26/doc-iimxxstf4598954. shtml

Shore, J., Baek, J., & Dellarocas, C. (2016). Network structure and patterns of information diversity on Twitter. Working paper. Available at https://www.semanticscholar.org/paper/Networkstructure-and-patterns-of-information-on-Shore-Baek/42bd23331a0bbe494529d273 d6ec82c7e87361bf.

Sun, M. (2012). How does the variance of product ratings matter? Management Science, 58(4), 696-707.

Susarla, A., Oh, J.-H., & Tan, Y. (2012). Social networks and the diffusion of user-generated content: Evidence from YouTube. Information Systems Research, 23(1), 23-41.

Sunstein, C. R. (2018). # Republic: Divided democracy in the age of social media. Princeton University Press.

Taber, C. S., & Lodge, M. (2006). Motivated skepticism in the evaluation of political beliefs. American Journal of Political Science, 50(3), 755-769.

Twitter. (2017). About conversations on Twitter. https://support.twitter.com/articles/20174577

van Alstyne, M., Brynjolfsson, E. (2005). Global village or cyber-Balkans? Modeling and measuring the integration of electronic communities. Management Science, 51(6), 851-868.

van den Bulte, C., & Joshi, Y. V. (2007). New product diffusion with influentials and imitators. Marketing Science, 26(3), 400- 421.

Vicario, M., Bessi, A., Zollo, F., Petroni, F., Scala, A., Caldarelli, G., Quattrociocchi, W. (2016). The spreading of misinformation online. In Proceedings of the National Academy of Sciences, 113(3), 554-559.

Wagner, P. M., & Ylä-Anttila, T. (2020). Can policy forums overcome echo chamber effects by enabling policy learning? Evidence from the Irish climate change policy network. Journal of Public Policy, 40(2), pp.194-211.

Karp, H. (2013). Beyonce releases latest album-quietly. Wall Street Journal. https://www.wsj.com/articles/SB1000142405270230 4202204579256591030008758

Watts, D. J., & Dodds, P. S. (2007). Influentials, networks, and public opinion formation. Journal of Consumer Research, 34(4), 441-458.

Womack, K. L. (1996). Do brokerage analysts’ recommendations have investment value? Journal of Finance, 51(1), 137-67.

Wood, T., & Porter, E. (2019). The elusive backfire effect: mass attitudes’ steadfast factual adherence. Political Behavior, 41(1), 135-163.

Wu, J., Wu, Y., Sun, J., & Yang, Z. (2013). User reviews and uncertainty assessment: A two stage model of consumers’ willingness-to-pay in online markets. Decision Support Systems, 55(1), 175-185.

Ye, Q., Law, R., & Gu, B. (2009). The impact of online user reviews on hotel room sales. International Journal of Hospitality Management, 28(1), 180-182.

Yin, D., Mitra, S., Zhang, H. (2016). Research note: When do consumers value positive vs. negative reviews? An empirical investigation of confirmation bias in online word of mouth. Information Systems Research, 27(1), 131-144.

Zaller, J. (1992). The nature and origins of mass opinions. Cambridge University Press.

Zhang, J. (2010). The sound of silence: Observational learning in the US kidney market. Marketing Science, 29(2), 315-335.

Zhang, Xiaoquan (Michael), and Feng Zhu. (2011). Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. American Economic Review, 101(4), 1601-1615.

Zhao, J., Dong, L., Wu, J., & Xu, K. (2012). MoodLens: An emoticon-based sentiment analysis system for Chinese tweets. Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 1528-1531).

## About the Authors

Yingda Lu is an assistant professor at the College of Business Administration, University of Illinois, Chicago. He obtained his Ph.D. in information systems from the Tepper School of Business, Carnegie Mellon University. His research leverages economic theory with state-of-the art machine learning algorithms to provide actionable policies to improve the policy design of social media platforms as well as algorithmic-driven decision systems. His research appears in top academic journals such as Management Science and MIS Quarterly, as well as the proceedings of top conferences such as the International Conference on Information Systems.

Junjie Wu is a professor in the Information Systems Department at Beihang University. He received his Ph.D. degree in management science and engineering and his B.Sc. degree in hydraulic engineering from Tsinghua University. He is currently the director of the Research Center for Data Intelligence (DIG), the chairman of the Institute of Artificial Intelligence for Management (AIM), and a member of the 8th MOE Discipline Council of Management Science and Engineering. His general area of research is information systems and machine learning, with special interests in solving real-life data-intensive problems arising from areas of computational sociology, smart cities, healthcare, and finance. He is the recipient of the NSFC Distinguished Young Scholars award and the MOE Changjiang Young Scholars award in China.

Yong Tan is the Michael G. Foster Endowed Professor of Information Systems at the Michael G. Foster School of Business, University of Washington, and a Distinguished Fellow of the INFORMS Information Systems Society. His research interests include social media and networks, mobile and electronic commerce, AI and big data analytics, sharing economy, and fintech. He has published in MIS Quarterly, Information Systems Research, and Management Science, among other journals.

Jian Chen is the Lenovo Chair Professor and chairman of the Management Science Department, and director of the Research Center for Contemporary Management, Tsinghua University. He received a B.Sc. degree in electrical engineering from Tsinghua University, Beijing, China, in 1983, and M.Sc. and Ph.D. degrees in Systems Engineering from the same university in 1986 and 1989, respectively. His main research interests include supply chain management, e-commerce, decision support systems, and systems engineering. Dr. Chen has published over 200 papers in refereed journals and has been a principal investigator for more than 50 grants or research contracts with the National Science Foundation of China, governmental organizations, and companies. He has been invited to present several plenary lectures at international conferences. He has been elected as an IEEE Fellow (2008). He has served as editor-in-chief/senior editor/editorial board member for many international journals.

## Appendix A

## Detailed Explanation of Microblog and Comments Mechanism on Weibo.com

Shi et al. (2014) proposed that Twitter is a social broadcasting environment where retweets spread information through content sharing between followers and followees. In other words, retweets can be regarded as one-way information propagation. The main objective of an individual retweeting a microblog is also to spread this microblog among their Twitter followers. Figure A1 illustrates this one-way information propagation:

![](/api/attachments/9XPDZSMS/fulltext/images/3aa192623d48f7efdc6791e03cde5160fca8b9f2e970210270b0f9e533a8b915.jpg)

Figure A1. Illustration of a Retweeting Example

For this figure, nodes represent users and the ties represent the following relationship between users. Arrows of ties represent the direction of the following relationship. For instance, the arrow from A to D represents D and follows A. We also use dashed lines to represent nonreciprocal ties (D follows A but A does not follow D) and use solid lines to represent reciprocal ties (A follows B and B follows A). When A posts a tweet, all A’s followers (B, C, D, and E) will be exposed to this tweet. After B and E decide to retweet A’s tweet, K and F are exposed to this microblog. And after F decides to retweet, L is exposed to this tweet. We use solid black dots to represent users who are exposed to the tweet from A. As we indicate using two blue arrows, this tweet spreads along two one-way links in this small network (A→E→K and A→B→F→L). It is worth mentioning that retweets from B, F, and L will not appear on E’s timeline. However, if B wrote a comment for A’s microblog, E can see this comment simply by clicking the “Comments” button on the screen.

Users post comments as a way of joining a conversation. Twitter also offers a comment function (this function is called reply in Twitter) a a way of getting involved in a conversation (https://support.twitter.com/articles/20174577). We use the scheme in Figure A2 to demonstrate an example of conversation through microblog comments. Figure A2 is an example scheme showing a few of the comments on a microblog posted by a Chinese cellphone producer on Weibo. We translated the microblogs and corresponding comments into English. After this microblog was posted, Users A and D commented on this microblog, as well as many others. Users B and C further reply based on A’s comments. Notice that these comments are publicly available for all platform users. For instance, before posting comments, User D will be exposed to all previously posted comments, rather than only being posted on followees’ timelines as a microblog.

A Mobile Phone Producer Weibo Account

XXX/20/2017, 17:29

Brand new model AA will start sale today on 18:08. Join the family and let witness the future!

## Comments

```txt
User A XXX/20/2017, 18:22
```

```txt
I will wait and see the feedback from the first hundreds of people who bought this. I really want to try Android phones, but the price of this one is a bit high…not sure…heard the company pays a lot of money for
```

Reply to User A comments:

## User B XXX/23/2017, 13:06

I bought the previous model, and it worked fine. I used it for two years, just a few times it automatically shut down by itself, and I also dropped it on floor many times…still works

## User C XXX/25/2017,08:13

I have been using brand ZZ, very cheap, good camera.

User A replying C XXX/25/2017,08:45

Frankly speaking, with an extra few hundreds, I can buy an inhone I still think this model AA is pricev

User C replying A XXX/26/2017, 08:12

Go to the offline stores and try these phones out yourself. You will realize price of model AA is very

User D XXX/20/2017, 18:46

Bought it already! I like the pro version even more!

Figure A2. Example of Comment Mechanism on Weibo

## Appendix B

Full Results for Aggregate-Level Model

<table><tr><td colspan="7">Table B1. Full Results for Aggregate-Level Model</td></tr><tr><td>Variable</td><td colspan="3">Sentiment polarization</td><td colspan="3">Average sentiment</td></tr><tr><td> $PolarM_{mt-1p}$ </td><td>0.045</td><td>***</td><td>(0.004)</td><td></td><td></td><td></td></tr><tr><td> $SentiM_{mt-1p}$ </td><td></td><td></td><td></td><td>0.064</td><td>***</td><td>(0.002)</td></tr><tr><td> $NumM_{mt-1p}$ </td><td>-0.008</td><td>***</td><td>(0.000)</td><td>-0.002</td><td>***</td><td>(0.000)</td></tr><tr><td> $NumUser_{mt-1p}$ </td><td>0.019</td><td>***</td><td>(0.007)</td><td>0.005</td><td>***</td><td>(0.001)</td></tr><tr><td> $DID_{tp}$ </td><td>-0.013</td><td>***</td><td>(0.004)</td><td>0.007</td><td>***</td><td>(0.001)</td></tr><tr><td>Is Weibo ( $P_p$ )</td><td>0.025</td><td>***</td><td>(0.000)</td><td>0.020</td><td>***</td><td>(0.006)</td></tr><tr><td>Reply-shutdown period ( $T_t$ )</td><td>0.003</td><td>*</td><td>(0.001)</td><td>0.002</td><td>*</td><td>(0.001)</td></tr><tr><td> $Weekend_t$ </td><td>-0.007</td><td>*</td><td>(0.003)</td><td>0.004</td><td>**</td><td>(0.002)</td></tr><tr><td> $Finance_m$ </td><td>-0.067</td><td></td><td>(0.052)</td><td>0.030</td><td></td><td>(0.029)</td></tr><tr><td> $IT_m$ </td><td>-0.044</td><td></td><td>(0.028)</td><td>0.021</td><td></td><td>(0.012)</td></tr><tr><td> $Entertainment_m$ </td><td>0.155</td><td>*</td><td>(0.082)</td><td>0.257</td><td>**</td><td>(0.103)</td></tr><tr><td> $Sport_m$ </td><td>0.049</td><td></td><td>(0.030)</td><td>-0.074</td><td></td><td>(0.048)</td></tr><tr><td> $Education_m$ </td><td>0.032</td><td></td><td>(0.023)</td><td>0.050</td><td></td><td>(0.039)</td></tr><tr><td> $Equipment_m$ </td><td>-0.090</td><td>*</td><td>(0.051)</td><td>-0.032</td><td>*</td><td>(0.017)</td></tr><tr><td> $Female/Home_m$ </td><td>0.067</td><td>*</td><td>(0.038)</td><td>0.025</td><td></td><td>(0.016)</td></tr><tr><td>Constant</td><td>0.262</td><td>***</td><td>(0.003)</td><td>0.215</td><td>***</td><td>(0.081)</td></tr><tr><td> $R^2$ </td><td colspan="3">0.323</td><td colspan="3">0.237</td></tr></table>

Note: \*\*\*significant at 1%; \*\*significant at 5%; \*Significant at 10%. We use transportation as the baseline category

## Appendix C

## Controlling for Heterogeneity and Data Generation Process

## Controlling for Heterogeneity

On the microblogging website, individuals are heterogeneous in their prior opinions depending on their individual characteristics. For example, optimistic users are more likely to write microblogs with positive opinions, whereas pessimistic users are more likely to write negative posts. Thus, we need to incorporate individual characteristics to account for individual heterogeneity in our model. In this paper, we assume that $s _ { i m 0 } ,$ , the prior mean of initial distribution of opinion, follows a Gaussian mixture distribution. Specifically, $s _ { i m 0 } { \sim } N ( \bar { s } _ { i m 1 } , \sigma _ { m } ^ { 2 } )$ with probability $p _ { s } ,$ and $s _ { i m 0 } { \sim } N ( \bar { s } _ { i m 2 } , \sigma _ { m } ^ { 2 } )$ with probability $1 - p _ { s } . \bar { s } _ { i m 1 }$ and $\bar { s } _ { i m 2 }$ are the mean of two potential prior opinions for individual ?? on topic ?? and $\sigma _ { m } ^ { 2 }$ is the variance of the prior opinion for topic ??. To incorporate individual characteristics, we assume $\hat { s } _ { i m j }$ follows the equation below, where ?? ∈ {1,2}:

$$
\bar {s} _ {i m j} = \alpha_ {m j 0} + \pmb {\alpha_ {1}} \pmb {Z} _ {i m},\tag{A1}
$$

$\alpha _ { m j 0 } { \sim } N ( \alpha _ { \mathrm { j 0 } } , 1 )$ measures the intrinsic population opinion for the topic itself. Here we normalize the variance to 1 for identification purposes. In addition, we omit the automobiles dummy variable in the regression so that $\alpha _ { 0 }$ can be identified. Some topics are intrinsically perceived as negative while others are intrinsically perceived as positive. Thus, we use this topic-specific random effect to capture the unobserved heterogeneity among topic population opinions. $\mathbf { Z } _ { i m }$ contains the sentiment of previous microblogs from focal user’s followees in previous months on topic ?? to capture existing impact of followees’ microblogs on focal individual prior opinions before the start of estimation period. In addition, $\mathbf { Z } _ { i m }$ also includes three individual characteristics for individual ??. We use number of microblogs in previous month to capture individual contribution level on the platform, and number of followers to measure individual network capital. We also calculate individual average opinion for the user’s microblog in previous month to control for individual opinion tendency, where some users tend to hold more positive views towards topics and others are more likely to express negative views on platform.

Furthermore, we assume that the variance of prior opinion follows $\sigma _ { m } ^ { 2 } { \sim } G a m m a ( \alpha _ { \sigma } , \beta _ { \sigma } )$ so that $\sigma _ { m } ^ { 2 }$ is always positive. This heterogeneity allows us to accommodate the possibility that some topics are controversial (thus a smaller $\sigma _ { m } ^ { 2 }$ value) while opinions on other topics are more homogeneous (thus a larger $\sigma _ { m } ^ { 2 }$ value). To better capture how controversial a topic is, we further calculate $\beta _ { \sigma } = \beta _ { \sigma 0 } + \beta _ { \sigma 1 } P r e S v a r _ { m } .$ $P r e S v a r _ { m }$ is calculated as the variance of microblogs in microblog chain ??, which was posted within one week prior to our estimation dataset. It is worth mentioning that because our model compares the opinion formation process with and without natural experiment, this further alleviates the concern on unobserved topic characteristics. In addition, we can identify $\alpha _ { \sigma } , \beta _ { \sigma 0 }$ as sentiment of the first microblog of each microblog chain is different.

## Data Generation Process

Summarizing the model specifications above, we can write the data generation process as follows:

1. A microblog thread on topic ?? appears on the platform. Individual ?? starts with an initial opinion on the topic, $s _ { i m 0 }$

2. Whenever individual ?? receives a notification on a retweeted microblog from friends (this microblog is on the $( n - 1 ) ^ { t h }$ level of this thread), individual ??′?? opinion on the topic will be changed based on their prior opinion, the opinion of preceding microblogs from the same thread, as well as the comments on these microblogs. The resulting opinion takes the form in Equation (1):

$$
s _ {i m n} = (1 - \varphi) s _ {i m 0} + \varphi E (F _ {i m n} | s _ {m 1} ^ {(i)}, s _ {m 2} ^ {(i)}, \dots , s _ {m n - 1} ^ {(i)}, s _ {i m 0}),
$$

where $E ( F _ { i m n } | s _ { m 1 } ^ { ( i ) } , s _ { m 2 } ^ { ( i ) } , \ldots , s _ { m n - 1 } ^ { ( i ) } , s _ { i m 0 } )$ characterizes the posterior peer impact from different information sources. The individual posterior opinion is assumed to follow a Bayesian updating process.

3. Individual ?? makes decisions on writing microblogs and comments conditional on their individual characteristics and posterior opinion.

4. All followers of individual ?? update their opinions based on the Bayesian updating rule described in Step 2. Go to Step 2.

5. Stop if no one writes new microblogs.

## Appendix D

## Text Mining Details

## Sentiment Classification

As a typical machine learning problem, conventional sentiment classification methods either involve building large sentiment lexicons or a lot of manual sentiment labeling, which is usually infeasible in real-world applications. Moreover, user generated-content like tweets on Weibo is extremely short, which makes sentiment classification a very challenging task. Recent years have witnessed the growing use of graphical emoticons in online social media, which enables a new paradigm for sentiment analysis. In light of this, we employ an emoticon-based approach for sentiment classification, whose effectiveness was empirically demonstrated in Moodlens (Zhao et al., 2012), the well-known first demo system for multiclass sentiment analysis of massive tweets on Chinese Weibo. Specifically, we first selected the tweets containing emoticons as the training set, and then label them automatically with the sentiments conveyed by the emoticons. The key here is to map each emoticon to an emotional state. To this end, we manually selected 95 out of a total of over 1000 emoticons that have clear polarities and mapped them onto three types of sentiments: positive, neutral, and negative. For classification modeling, we adopted the naive Bayes (NB) classifier, which is known for its high efficiency, good interpretability, and decent classification accuracy (Zhao et al., 2012). For more details on this classifier, please refer to Appendix C.

For the empirical study, we randomly sampled 6600 tweets with emoticons from Weibo on September 1, 2013, and labeled them into the three predefined sentiment categories. We obtained 2190 negative, 1340 neutral and 3060 positive tweets. We used a fivefold cross-validation and employed three metrics to evaluate the classification performance (Godbole & Sarawagi, 2004) including the macro-average precision, recall, and F-score. In each run, we trained a model on one fold and evaluated its performance on the remaining fourfolds. The final result is the average performance of the five runs as follows: macro-average precision is 0.7439, macro-average recall is 0.7483 and macro-average F-score is 0.7394. The final classifier was built on all 6590 labeled tweets. Using this classifier, we can predict the sentiment labels of unseen tweets with or without emoticons. To obtain a continuous sentiment measure, we used the predicted probability with a positive or negative label as the real-value measure of each tweet’s sentiment intensity.

## Topic Mining

To probe topics on Weibo tweets, we adopted two types of approaches. The first one is an unsupervised clustering method that employs a repeated bisecting algorithm to group tweets into different clusters, and the well-partitioned clusters are treated as topics. This unsupervised method is of great help for exploring undefined topics hidden inside tweets. The second approach is a supervised classification method that employs a support vector machines (SVM) classifier to assign each tweet with one of the nine predefined topic labels, i.e., politics, finance, car, education, women/home, IT, equipment, entertainment, and sports. This supervised method can provide more accurate prediction than unsupervised ones with the guidance of predefined topic labels. Specifically, to tackle the issues of high dimensionality and sparsity of short texts, we adopted the RB algorithm provided in the well-known too CLUTO2 (Karypis et al., 1999) for clustering, and the SVM with linear kernel provided in LIBLINEAR3 (Fan et al., 2008) for classification.

To evaluate clustering performance, we first randomly sampled 100000 tweets on September 1, 2013. We then extracted the top 10 hot hashtags in our study and kept only the tweets containing these 10 hashtags, which resulted in 10000 tweets each containing only one hashtag as its true topic category. The normalized mutual information (NMI) (Cover & Thomas, 2012) was used as an external evaluation metric. As default settings, RB adopted cosine as a similarity function, and the cluster number was set to 10. We ran this 10 times and each run was carried out with 10 trials to select the solution with the best criterion function value, which returned an average NMI value of 0.3185.

We evaluated classification performance on one public dataset: Sohu News Corpus4. This dataset contains all news pages crawled from 18 channels of Sohu (http://news.sohu.com/) between June and July 2012. Each news page contains the ID, URL, title, and content. As we worked with shorttext topic mining, we kept only the title of each news page, which could be regarded as a kind of short-text document. From the same site, we also collected the categorical labels of the news as predefined ground-truth topics. Finally, we obtained 104639 news titles within eight topic categories. We performed a fivefold cross-validation and reported the average performance in terms of multiclass classification as follows: macro-averag precision is 0.866, macro-average recall is 0.798 and macro-average F-score is 0.824.

## Naive Bayes Classifier

Assume that we have E emoticons in a labeled tweet set T. For each tweet t in $^ \mathrm { T , }$ we first represent t in a sequence of words $\{ w _ { i } \}$ , where $w _ { i }$ is the $i ^ { t h }$ word in t. From the labeled tweets, we could obtain the word $w _ { i }$ ’s prior probability of belonging to the sentiment category $c _ { j }$ as $\operatorname { P } ( w _ { i } | c _ { j } ) = \frac { n ^ { c _ { j } } ( w _ { i } ) + 1 } { \sum _ { q } ( n ^ { c _ { j } } \big ( w _ { q } \big ) + 1 ) } ,$ where the category index $j = - 1 , 0 ,$ , 1 corresponds to negative, neutral and positive respectively, $n ^ { c _ { j } } ( w _ { i } )$ represents the times that ?? appears in all the tweets in the category $c _ { j }$ and Laplace smoothing is used to avoid the problem of zero probability. Then, we can establish the naive Bayes classifier as follows. For an unlabeled tweet t with word sequence $\{ w _ { i } \}$ , its category could be obtained as $\begin{array} { r } { c ^ { * } ( t ) = a r g \operatorname* { m a x } _ { j } P ( c _ { j } ) \prod _ { i } P ( w _ { i } | c _ { j } ) } \end{array}$ , where $P ( c _ { j } )$ is the prior probability of $c _ { j }$ .

## Appendix E

## Robustness Check Based on Topic Level Instead of Microblog Chain Level

In the main estimation model, our unit of analysis is for each microblog chain. For example, in Equation (1) of manuscript, we examine how sentiment polarization of microblog chain ?? on platform ?? at period ?? $( P o l a r M _ { m t p } )$ changes as a result of our treatment. In this robustness check, we used a different unit of analysis in which we first employed the topic modeling algorithm described in Appendix D to categorize microblogs into 2,000 topics. We then examined how the polarization of topic ?? on platform ?? at period $t ( P o l a r M _ { j t p } )$ changes as a result of the treatment. Specifically, we estimate the equations below:

$$
P o l a r M _ {j t p} = \alpha_ {0} + \alpha_ {1} P o l a r M _ {j t - 1 p} + \alpha_ {2} N u m M _ {j t - 1 p} + \alpha_ {3} N u m U s e r _ {j t - 1 p} + \alpha_ {4} D I D _ {t p} + \alpha_ {5} T _ {t} + \alpha_ {6} P _ {p} + \alpha_ {7} W e e k e n d _ {t} + \varepsilon_ {1 j t p},
$$

$$
S e n t i M _ {j t p} = \alpha_ {0} + \alpha_ {1} S e n t i M _ {j t - 1 p} + \alpha_ {2} N u m M _ {j t - 1 p} + \alpha_ {3} N u m U s e r _ {j t - 1 p} + \alpha_ {4} D I D _ {t p} + \alpha_ {5} T _ {t} + \alpha_ {6} P _ {p} + \alpha_ {7} W e e k e n d _ {t} + \varepsilon_ {2 j t p}.
$$

We report the estimation results in table E1. Following the same logic, we also estimated the corresponding Bayesian Learning model. We report the results in Table E2. As we can see from these two tables, our results are generally robust when we use topics as the unit of analysis.

<table><tr><td colspan="7">Table E1. Aggregate-Level Model for Each Topic</td></tr><tr><td>Variable</td><td colspan="3">Sentiment polarization</td><td colspan="3">Average sentiment</td></tr><tr><td> $PolarM_{mt-1p}$ </td><td>0.024</td><td>***</td><td>(0.007)</td><td></td><td>--</td><td></td></tr><tr><td> $SentiM_{mt-1p}$ </td><td></td><td>--</td><td></td><td>0.042</td><td>***</td><td>(0.008)</td></tr><tr><td> $NumM_{mt-1p}$ </td><td>-0.004</td><td>***</td><td>(0.000)</td><td>-0.004</td><td>***</td><td>(0.001)</td></tr><tr><td> $NumUser_{mt-1p}$ </td><td>0.079</td><td>***</td><td>(0.023)</td><td>0.011</td><td>***</td><td>(0.001)</td></tr><tr><td> $DID_{tp}$ </td><td>-0.025</td><td>***</td><td>(0.006)</td><td>0.005</td><td>***</td><td>(0.001)</td></tr><tr><td>Is Weibo ( $P_p$ )</td><td>0.021</td><td>***</td><td>(0.000)</td><td>0.015</td><td>*</td><td>(0.008)</td></tr><tr><td>Reply-shutdown period ( $T_t$ )</td><td>0.004</td><td>**</td><td>(0.002)</td><td>0.001</td><td>*</td><td>(0.000)</td></tr><tr><td> $Weekend_t$ </td><td>-0.009</td><td>*</td><td>(0.004)</td><td>0.001</td><td>**</td><td>(0.000)</td></tr><tr><td>Topic-fixed effect</td><td colspan="3">Yes</td><td colspan="3">Yes</td></tr><tr><td>Constant</td><td>0.312</td><td>***</td><td>(0.005)</td><td>0.187</td><td>***</td><td>(0.090)</td></tr><tr><td> $R^2$ </td><td colspan="3">0.355</td><td colspan="3">0.281</td></tr></table>

Note: \*\*\*significant at 1%; \*\*significant at 5%; \*significant at 10%

<table><tr><td colspan="2">Table E2. Bayesian Learning Model using Topic as Observation Level</td></tr><tr><td>Variables</td><td>Posterior mean opinion</td></tr><tr><td colspan="2">Microblog opinion formation</td></tr><tr><td colspan="2">Formation of posterior opinion</td></tr><tr><td>Peer influence weight ( $\varphi_0$ )</td><td>0.392***</td></tr><tr><td>Impact of treatment on posterior mean opinion ( $\varphi_1$ )</td><td>0.038***</td></tr><tr><td>Impact of treatment on opinion polarization ( $\varphi_2$ )</td><td>-0.021**</td></tr><tr><td>Interaction between treatment and social media participation on opinion polarization ( $\varphi_3$ )</td><td>-0.008*</td></tr><tr><td>Impact of treatment on posterior variance ( $\rho_1$ )</td><td>0.071**</td></tr><tr><td>Prior accuracy variance ( $\sigma_A^2$ )</td><td>3.144***</td></tr><tr><td>Time-fixed effect</td><td>Yes</td></tr><tr><td>Platform-fixed effect</td><td>Yes</td></tr><tr><td colspan="2">Prior opinion</td></tr><tr><td>Average of individual prior opinion across population—first component ( $\alpha_{10}$ )</td><td>0.483***</td></tr><tr><td>Average of individual prior opinion across population—second component ( $\alpha_{20}$ )</td><td>-0.077***</td></tr><tr><td>Probability of belong to first component ( $p_s$ )</td><td>0.686***</td></tr><tr><td>Sentiment of same chain microblogs from followees in previous month</td><td>0.298***</td></tr><tr><td>Number of Microblogs in previous month</td><td>0.030</td></tr><tr><td>Number of followers</td><td>0.070**</td></tr><tr><td>Individual average opinions from past microblogs</td><td>0.130**</td></tr><tr><td>Prior opinion variance shape parameter ( $\alpha_{\sigma}$ )</td><td>2.475***</td></tr><tr><td>Prior opinion variance scale parameter ( $\beta_{\sigma 0}$ )</td><td>0.330***</td></tr><tr><td>Previous variance of microblog ( $\beta_{\sigma 1}$ )</td><td>0.022*</td></tr><tr><td>Finance</td><td>-0.062</td></tr><tr><td>IT</td><td>-0.045</td></tr><tr><td>Entertainment</td><td>0.132*</td></tr><tr><td>Sport</td><td>0.070*</td></tr><tr><td>Education</td><td>-0.021</td></tr><tr><td>Equipment</td><td>-0.070</td></tr><tr><td>Women/home</td><td>0.101**</td></tr><tr><td>Writing microblog</td><td></td></tr><tr><td>Posterior opinion mean</td><td>-0.368***</td></tr><tr><td>Frequency of posting microblogs in previous month</td><td>0.072**</td></tr><tr><td>Number of followers</td><td>0.133***</td></tr><tr><td>Constant</td><td>-3.739***</td></tr></table>

Note: \*\*\*significant at 1%; \*\*significant at 5%; \*significant at 10%

## APPENDIX F

## Robustness Checks for Bayesian Learning Model

In our manuscript, we only demonstrate robustness checks for aggregate-level model due to space limits. In this Appendix, we further conducted similar robustness checks for the Bayesian learning model. The results are generally consistent with our main model.

## Robustness Check with Reply Characteristics and A-B-A Setting

Similar to the corresponding robustness check in the manuscript, we incorporated reply characteristics in the Bayesian learning model. We removed Sohu Weibo as a control group, as Sohu Weibo reply data was unavailable. We also leveraged the A-B-A setting in our natural experiment and estimated the two datasets: the first one consists of a period before and during treatment and the second one consists of a period during and after treatment. We present the estimation results of these two datasets below.

<table><tr><td colspan="3">Table F1. Bayesian Learning Model with Before and During Treatment Data</td></tr><tr><td>Variables</td><td>Before and during treatment</td><td>During and after treatment</td></tr><tr><td colspan="3">Microblog opinion formation</td></tr><tr><td colspan="3">Formation of posterior opinion</td></tr><tr><td>Peer influence weight ( $\varphi_0$ )</td><td>0.246***</td><td>0.205***</td></tr><tr><td>Impact of treatment on posterior mean opinion ( $\varphi_1$ )</td><td>0.028***</td><td>0.022**</td></tr><tr><td>Impact of treatment on opinion polarization ( $\varphi_2$ )</td><td>-0.021***</td><td>-0.030***</td></tr><tr><td>Interaction between treatment and social media participation ( $\varphi_3$ )</td><td>-0.005**</td><td>-0.006***</td></tr><tr><td>Impact of treatment on posterior variance ( $\rho_1$ )</td><td>0.043**</td><td>0.059**</td></tr><tr><td>Prior accuracy variance ( $\sigma_A^2$ )</td><td>3.545***</td><td>3.809***</td></tr><tr><td>Time-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Platform-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="3">Prior opinion</td></tr><tr><td>Average of individual prior opinion across population—first component ( $\alpha_{10}$ )</td><td>0.308***</td><td>0.296***</td></tr><tr><td>Average of individual prior opinion across population—second component ( $\alpha_{20}$ )</td><td>-0.066***</td><td>-0.044***</td></tr><tr><td>Probability of belong to first component ( $p_s$ )</td><td>0.626***</td><td>0.600***</td></tr><tr><td>Sentiment of same chain microblogs from followees in previous month</td><td>0.274***</td><td>0.304***</td></tr><tr><td>Number of Microblogs in previous month</td><td>0.009</td><td>0.021*</td></tr><tr><td>Number of followers</td><td>0.106**</td><td>0.185***</td></tr><tr><td>Individual average opinions from past microblogs</td><td>0.285***</td><td>0.156**</td></tr><tr><td>Prior opinion variance shape parameter ( $\alpha_\sigma$ )</td><td>2.980***</td><td>2.368***</td></tr><tr><td>Prior opinion variance scale parameter ( $\beta_{\sigma 0}$ )</td><td>0.272***</td><td>0.249***</td></tr><tr><td>Previous variance of microblog ( $\beta_{\sigma 1}$ )</td><td>0.041***</td><td>0.075***</td></tr><tr><td>Finance</td><td>-0.080</td><td>-0.093</td></tr><tr><td>IT</td><td>-0.031</td><td>-0.040</td></tr><tr><td>Entertainment</td><td>0.180*</td><td>0.133*</td></tr><tr><td>Sports</td><td>0.086*</td><td>0.105*</td></tr><tr><td>Education</td><td>-0.026</td><td>-0.016</td></tr><tr><td>Equipment</td><td>-0.042</td><td>-0.017</td></tr><tr><td>Women/home</td><td>0.140**</td><td>0.103**</td></tr><tr><td>Writing microblog</td><td></td><td></td></tr><tr><td>Posterior opinion mean</td><td>-0.580***</td><td>-0.604***</td></tr><tr><td>Frequency of posting microblogs in previous month</td><td>0.041***</td><td>0.023***</td></tr><tr><td>Number of followers</td><td>0.142***</td><td>0.119***</td></tr><tr><td>Constant</td><td>-3.460***</td><td>-2.901***</td></tr></table>

Note: \*\*\*significant at 1%; \*\*significant at 5%; \*significant at 10%. We use automobiles as the baseline category.

## Robustness Check with Alternative Sampling Technique and Control Group

Similar to the corresponding robustness checks in the manuscript, we collected microblogs from Weibo, Sohu Weibo and Twitter with the 145 top hashtags. We then estimated the Bayesian learning models using the Weibo and Sohu Weibo data and present the results in the table below. Then we estimated the Bayesian learning model using Weibo, and Twitter data and present the results in the table below. The results are consistent with our main results.

<table><tr><td colspan="2">Table F2. Alternative Sampling Strategy Using Sohu Weibo as Control</td></tr><tr><td>Variables</td><td>Posterior mean opinion</td></tr><tr><td colspan="2">Microblog opinion formation</td></tr><tr><td colspan="2">Formation of posterior opinion</td></tr><tr><td>Peer influence weight ( $\varphi_0$ )</td><td>0.313***</td></tr><tr><td>Impact of treatment on posterior mean opinion ( $\varphi_1$ )</td><td>0.006**</td></tr><tr><td>Impact of treatment on opinion polarization ( $\varphi_2$ )</td><td>-0.031***</td></tr><tr><td>Interaction between treatment and social media participation ( $\varphi_3$ )</td><td>-0.006**</td></tr><tr><td>Impact of treatment on posterior variance ( $\rho_1$ )</td><td>0.017**</td></tr><tr><td>Prior accuracy variance ( $\sigma_A^2$ )</td><td>3.087***</td></tr><tr><td>Time-fixed effect</td><td>Yes</td></tr><tr><td>Platform-fixed effect</td><td>Yes</td></tr><tr><td colspan="2">Prior opinion</td></tr><tr><td>Average of individual prior opinion across population—first component ( $\alpha_{10}$ )</td><td>0.303***</td></tr><tr><td>Average of individual prior opinion across population—second component ( $\alpha_{20}$ )</td><td>-0.087***</td></tr><tr><td>Probability of belong to first component ( $p_s$ )</td><td>0.595***</td></tr><tr><td>Sentiment of same chain microblogs from followees in previous month</td><td>0.301***</td></tr><tr><td>Number of Microblogs in previous month</td><td>0.024*</td></tr><tr><td>Number of followers</td><td>0.118***</td></tr><tr><td>Individual average opinions from past microblogs</td><td>0.240***</td></tr><tr><td>Prior opinion variance shape parameter ( $\alpha_\sigma$ )</td><td>2.162***</td></tr><tr><td>Prior opinion variance scale parameter ( $\beta_{\sigma 0}$ )</td><td>0.310***</td></tr><tr><td>Previous variance of microblog ( $\beta_{\sigma1}$ )</td><td>0.017**</td></tr><tr><td>Finance</td><td>-0.091*</td></tr><tr><td>IT</td><td>-0.062</td></tr><tr><td>Entertainment</td><td>0.130*</td></tr><tr><td>Sports</td><td>0.009</td></tr><tr><td>Education</td><td>-0.063</td></tr><tr><td>Equipment</td><td>-0.014</td></tr><tr><td>Women/home</td><td>0.201*</td></tr><tr><td>Writing microblog</td><td></td></tr><tr><td>Posterior opinion mean</td><td>-0.552***</td></tr><tr><td>Frequency of posting microblogs in previous month</td><td>0.030***</td></tr><tr><td>Number of followers</td><td>0.143***</td></tr><tr><td>Constant</td><td>-3.289***</td></tr></table>

Note: \*\*\*significant at 1%; \*\*significant at 5%; \*significant at 10%. We use automobiles as the baseline category.

<table><tr><td colspan="2">Table F3. Alternative Sampling Strategy Using Twitter as Control</td></tr><tr><td>Variables</td><td>Posterior mean opinion</td></tr><tr><td colspan="2">Microblog opinion formation</td></tr><tr><td colspan="2">Formation of posterior opinion</td></tr><tr><td>Peer influence weight ( $\varphi_0$ )</td><td>0.184***</td></tr><tr><td>Impact of treatment on posterior mean opinion ( $\varphi_1$ )</td><td>0.025**</td></tr><tr><td>Impact of treatment on opinion polarization ( $\varphi_2$ )</td><td>-0.023*</td></tr><tr><td>Interaction between treatment and social media participation ( $\varphi_3$ )</td><td>-0.009***</td></tr><tr><td>Impact of treatment on posterior variance ( $\rho_1$ )</td><td>0.038**</td></tr><tr><td>Prior accuracy variance ( $\sigma_A^2$ )</td><td>3.640***</td></tr><tr><td>Time-fixed effect</td><td>Yes</td></tr><tr><td>Platform-fixed effect</td><td>Yes</td></tr><tr><td colspan="2">Prior opinion</td></tr><tr><td>Average of individual prior opinion across population—first component ( $\alpha_{10}$ )</td><td>0.291***</td></tr><tr><td>Average of individual prior opinion across population—second component ( $\alpha_{20}$ )</td><td>-0.058***</td></tr><tr><td>Probability of belong to first component ( $p_s$ )</td><td>0.556***</td></tr><tr><td>Sentiment of same chain microblogs from followees in previous month</td><td>0.328***</td></tr><tr><td>Number of Microblogs in previous month</td><td>0.010</td></tr><tr><td>Number of followers</td><td>0.134**</td></tr><tr><td>Individual average opinions from past microblogs</td><td>0.177***</td></tr><tr><td>Prior opinion variance shape parameter ( $\alpha_\sigma$ )</td><td>2.611***</td></tr><tr><td>Prior opinion variance scale parameter ( $\beta_{\sigma_0}$ )</td><td>0.203***</td></tr><tr><td>Previous variance of microblog ( $\beta_{\sigma_1}$ )</td><td>0.051**</td></tr><tr><td>Finance</td><td>-0.101*</td></tr><tr><td>IT</td><td>-0.011</td></tr><tr><td>Entertainment</td><td>0.109*</td></tr><tr><td>Sports</td><td>0.067*</td></tr><tr><td>Education</td><td>-0.013</td></tr><tr><td>Equipment</td><td>-0.068*</td></tr><tr><td>Women/home</td><td>0.082**</td></tr><tr><td>Writing microblog</td><td></td></tr><tr><td>Posterior opinion mean</td><td>-0.569***</td></tr><tr><td>Frequency of posting microblogs in previous month</td><td>0.031***</td></tr><tr><td>Number of followers</td><td>0.124***</td></tr><tr><td>Constant</td><td>-3.109***</td></tr></table>

Note: \*\*\*significant at 1%; \*\*significant at 5%; \*significant at 10%. We use automobiles as the baseline category.

## Falsification Test

Following similar logic as our manuscript, we changed the treatment time to the start of second week after the beginning of our estimation period (March 24-March 26), and used the first two weeks of data as the estimation dataset. Whereas in the post-treatment period, we changed the treatment time to the start of second week after the actual treatment ended (April 9-April 11) and used the two weeks after the treatment period ended as the estimation dataset. We then estimated these two datasets using the Bayesian learning model. We report the results in the table below. As we can see the coefficients associated with treatment $( \varphi _ { 1 } , \varphi _ { 2 } , \varphi _ { 3 } , \rho _ { 1 } )$ are now insignificant. This helped us alleviate the concern about a potential time trend as a confounding factor.

<table><tr><td colspan="3">Table F4. Falsification Test Using Bayesian Learning Model</td></tr><tr><td>Variables</td><td>Falsification test with first two weeks</td><td>Falsification test with last two weeks</td></tr><tr><td colspan="3">Microblog opinion formation</td></tr><tr><td colspan="3">Formation of posterior opinion</td></tr><tr><td>Peer influence weight ( $\varphi_0$ )</td><td>0.271***</td><td>0.195***</td></tr><tr><td>Impact of treatment on posterior mean opinion ( $\varphi_1$ )</td><td>0.009</td><td>-0.007</td></tr><tr><td>Impact of treatment on opinion polarization ( $\varphi_2$ )</td><td>0.007</td><td>0.002</td></tr><tr><td>Interaction between treatment and social media participation ( $\varphi_3$ )</td><td>-0.000</td><td>0.000</td></tr><tr><td>Impact of treatment on posterior variance ( $\rho_1$ )</td><td>0.020</td><td>0.008</td></tr><tr><td>Prior accuracy variance ( $\sigma_A^2$ )</td><td>3.933***</td><td>3.532***</td></tr><tr><td>Time-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Platform-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="3">Prior opinion</td></tr><tr><td>Average of individual prior opinion across population—first component ( $\alpha_{10}$ )</td><td>0.238***</td><td>0.215***</td></tr><tr><td>Average of individual prior opinion across population—second component ( $\alpha_{20}$ )</td><td>-0.071***</td><td>-0.058***</td></tr><tr><td>Probability of belong to first component ( $p_s$ )</td><td>0.624***</td><td>0.696***</td></tr><tr><td>Sentiment of same chain microblogs from followees in previous month</td><td>0.294***</td><td>0.301***</td></tr><tr><td>Number of Microblogs in previous month</td><td>0.007</td><td>0.021</td></tr><tr><td>Number of followers</td><td>0.106*</td><td>0.154**</td></tr><tr><td>Individual average opinions from past microblogs</td><td>0.208**</td><td>0.226**</td></tr><tr><td>Prior opinion variance shape parameter ( $\alpha_{\sigma}$ )</td><td>2.460***</td><td>2.954***</td></tr><tr><td>Prior opinion variance scale parameter ( $\beta_{\sigma 0}$ )</td><td>0.297***</td><td>0.260***</td></tr><tr><td>Previous variance of microblog ( $\beta_{\sigma 1}$ )</td><td>0.047***</td><td>0.48***</td></tr><tr><td>Finance</td><td>-0.088</td><td>-0.061</td></tr><tr><td>IT</td><td>-0.077</td><td>-0.065</td></tr><tr><td>Entertainment</td><td>0.165*</td><td>0.128*</td></tr><tr><td>Sport</td><td>0.103*</td><td>0.081*</td></tr><tr><td>Education</td><td>-0.028</td><td>-0.035</td></tr><tr><td>Equipment</td><td>-0.059</td><td>-0.034</td></tr><tr><td>Women/home</td><td>0.078*</td><td>0.125*</td></tr><tr><td>Writing microblog</td><td></td><td></td></tr><tr><td>Posterior opinion mean</td><td>-0.618***</td><td>-0.573***</td></tr><tr><td>Frequency of posting microblogs in previous month</td><td>0.034***</td><td>0.039***</td></tr><tr><td>Number of followers</td><td>0.125***</td><td>0.137***</td></tr><tr><td>Constant</td><td>-2.940***</td><td>-3.465***</td></tr></table>

Note: \*\*\*significant at 1%; \*\*significant at 5%; \*significant at 10%. We use automobiles as the baseline category.
