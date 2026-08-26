---
otero_id: 14578
otero_key: "CZJ97CQA"
title: "The Impact of Subscription Reciprocity on Charitable Content Creation and Sharing: Evidence from Twitter on Giving Tuesday"
authors: "Xue (Jane) Tan; Yingda Lu; Yong Tan"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/14676"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# THE IMPACT OF SUBSCRIPTION RECIPROCITY ON CHARITABLE CONTENT CREATION AND SHARING: EVIDENCE FROM TWITTER ON GIVING TUESDAY $^{1}$

Xue (Jane) Tan
Department of Operations and Decision Technologies, Kelley School of Business,
Indiana University, Bloomington, IN, U.S.A. {janetan@iu.edu}

Yingda Lu
College of Business Administration, University of Illinois,
Chicago, IL, U.S.A. {yingdalu@uic.edu}

Yong Tan
Michael G. Foster School of Business, University of Washington,
Seattle, WA, U.S.A. {ytan@uw.edu}

Social broadcasting sites have grown from an information diffusion channel to a public medium that facilitates public conversations of charitable social movements. Two mechanisms foster user participation in charitable social movements: content creation and content sharing. Users can create original content to express their attitude of giving and promote their most valued nonprofit organizations, enriching the depth of the conversation. They can also share others' content to expedite the diffusion of high-quality content, expanding the breadth of the discussion. This paper investigates the impact of reciprocal and nonreciprocal followees (i.e., a followee is an account to which other users subscribe) on followers' decisions to create and share content. Analyzing the charitable movement of Giving Tuesday on Twitter, we find that original charitable content creation is prompted by reciprocal followees' participation but not nonreciprocal followees' participation in this movement. We also find that charitable content sharing is evoked by both reciprocal and nonreciprocal followees, with nonreciprocal followees having a greater impact. We discuss the theoretical and practical implications of these findings.

Keywords: Twitter, reciprocity, charitable movements, content creation, content sharing

## Introduction

Through a subscription relationship, Twitter captures people's dual needs of listening to others and expressing themselves. Users can subscribe to others' broadcasts without authorization as followers and can broadcast to their own subscribers as followees. A network derived from subscription relationships, like Twitter, is different from other social networks derived from friendship, kinship, and professional relationships. You may not be an actual friend of Ellen DeGeneres, but you can follow her on Twitter to see what she is up to. You may have never met Matthew, a movie fan, but you can read his commentary about new movies by following his Twitter account. Unlike Ellen, who does not follow you back, Matthew is more likely to reciprocate your gesture and become your follower, given your mutual interest in movies. As such, Twitter manages a hybrid of reciprocal and nonreciprocal relationships, resulting in a short diameter, a high frequency of updates, and, subsequently, a fast mode of information diffusion (i.e., diffusion refers to the spread of information among nodes in a social network) (Java et al. 2007). Rogers (2010) noted that “interactive communication technologies may be changing the diffusion process in certain fundamental ways” (p. 21). When information spreads beyond spatial distance, sparks of ideas may aggregate into collective actions (Oh et al. 2013). To better reflect the unique features of subscription-based networks, we follow Shi et al. (2014) to term such networks “social broadcasting networks.”

Social broadcasting networks rely on two mechanisms to facilitate decentralized information diffusion. The first mechanism is creating original content that includes a hashtag, which directs views based on a search term or prefixed keyword. $^{2}$ These hashtags become clickable links so that users' opinions can be diffused to people interested in a certain topic. For example, #OccupyWallStreet is a topical mark of a protest movement against economic inequality (Gleason 2013). The second mechanism is sharing content, which allows content to be diffused beyond the original author's audience. On Twitter, content sharing is referred to as "retweeting" because a social post is considered a tweet. This action facilitates a cascade of information and brings new people into existing threads, sometimes making news spread more rapidly on Twitter than in mainstream news media. The first mechanism of content creation promotes the self-expression of opinions concerning a topic to heighten its depth, and the second mechanism of content sharing focuses on the spread of information to broaden its breadth. With both depth and breadth, a popular hashtag can develop into a trending topic listed on the sidebar of Twitter, making it reach even more people.

Many trending topics concern societal issues such as the presidential election, environmental protection, and charitable movements (Gaffney 2010). This paper studies a charitable movement on Twitter. Charitable digital movements concern public consequences (Wejnert 2002) and play unique roles in encouraging the citizen behavior of charitable giving (Castillo et al. 2014). Such movements have become an increasingly important channel for individuals to express their social consciousness and for nonprofit organizations to generate awareness and recruit donors, supporting democratic vitality and encouraging charitable giving as a social norm (Miranda et al. 2016). These digital social movements require theoretically grounded investigation, in part because they are fundamentally different from business-oriented campaigns that are based on monetary incentives (e.g., Ellen DeGeneres endorses skincare products from Olay as a spokesperson).

We examine the effect of social influence on driving content creation and sharing with regard to charitable social movements on social media platforms. Users' participation in these movements is affected by the participation of their followees, and social influence is the key driver for individual behavior to aggregate into collective actions. The distinctive feature of the social broadcasting network is reciprocity—i.e., your reciprocal tie (Matthew) and nonreciprocal tie (Ellen) may impact your participation differently. Comparatively, the reciprocal relationship with Matthew is a strong tie that can either develop from online or offline interactions. The nonreciprocal relationship with Ellen is a weak tie that widely exists between users and content providers who are not necessarily celebrities. To understand charitable movements in social broadcasting networks and across the relationship maintained there, we sought to answer the research question: How does the reciprocity of ties attenuate social influence regarding people's content creation (as reflected in a tweet) and content sharing (as reflected in a retweet)?

The answer to this question concerns an underlying factor shaping the formation of social broadcasting networks—social capital. Social capital refers to resources embedded in a social structure for people’s furtherance of their self-interests (Coleman 1988). For example, when you advocate the same charitable movement as your reciprocal followee Matthew, he likely observes your behavior. This facilitates trust and mutual obligation, which are essentially social capital that can translate to mental support, social approval, or even information controls in the future (Putnam 1995). The story is different when the relationship is nonreciprocal. For instance, because of the lack of observability, you cannot accumulate social capital from Ellen even if you advocate the same movement as her. There is no obligation for her to support you in the future because social capital hinges on “general reciprocity” (Cropanzano and Mitchell 2005). However, retweeting a celebrity’s post may still be an attractive option for you because her content is likely of interest to a significant number of people and can help your reputation among your own followers (Granovetter 1973; Shi et al. 2014). A reputation for providing high-quality information is a strong motivator for participation in electronic networks (Bandura 2009; Smith and Kollock 1999). Although there are many network-level Twitter analyses uncovering the topological features of the networks and temporal trends of diffusion (Bakshy et al.; Cunha et al.; Romero et al. 2011), very little is known about how reciprocity can affect an individual's diffusion decisions. Linking individual diffusion decisions to social capital sets our study apart from the existing body of works.

In this paper, we conduct a node-level analysis of a 2017 event of an annual charitable movement on social media. We analyze 2,033 random individuals' content creation and sharing decisions in this particular movement as related to the participation of their followee network. We delineate reciprocal and nonreciprocal followees' participation to disentangle the role of reciprocity. Further, since users and their followees may have similar preferences, the users' successive participation in regard to their followees may not necessarily indicate causation. We control for the potential endogeneity issue arising from latent homophily using a latent instrumental variable (LIV) approach.

By comparing the diffusion processes of content creation and sharing, we find strong evidence for the theory of contagion complexity, $^{3}$ which posits that strong ties have an advantage over weak ties in the diffusion of complex behavior (Centola and Macy 2007). In our context, users' content creation is considered to be more complex than content sharing. We find that content creation is affected by reciprocal followees but not by nonreciprocal followees, underscoring the strength of strong ties in a complex diffusion process. Nonreciprocal ties, on the other hand, show a relatively higher propensity to drive content sharing, a simple diffusion process motivated by the novelty of information. This finding is consistent with the strength of weak tie theory, which posits that weak ties are advantageous in novel information transmission. By highlighting the complexity of behavior to be diffused, our study shows conditions that allow both the strong tie and the weak tie theories to take effect, reconciling the debate over the relative strength of strong and weak ties. Given the limited studies that examine how tie properties impact the capacity of social capital to facilitate different actions (Sandefur and Laumann 1998), our findings contribute to the literature on information systems and sociology in prosocial behavior.

## Theoretical Development

## Tie Strength

In his foundational account, Granovetter (1973) defined the strength of a tie (relationship) to be, among other features, a function of mutual confiding and reciprocal services. Three types of ties are emphasized in sociology literature: mutual positive, mutual nonpositive, and asymmetric. In sociometric tests in which subjects are asked to list people whom they like or trust, these three relationships correspond to mutual choices, mutual nonchoices, and unreciprocated (Davis 1970). Using 742 matrices of real-world data, Davis (1970) found that mutual positive corresponds to the strongest interpersonal relationship, mutual nonpositive holds the weakest relationship, and asymmetric pairs are intermediate.

A decade after he introduced the concept of weak ties, Granovetter (1983) revisited a body of work on weak ties that had developed since. In Granovetter's 1983 reassessment of the theory, Friedkin (1980) made the most comprehensive attempt to examine the validity of his arguments regarding weak ties. Friedkin (1980) defined a weak tie between two faculty members as one reporting having discussed his work with another, while the other did not report the same. Friedkin concluded that treating an asymmetrical relationship as a weak tie and a reciprocal relationship as a strong tie is consistent with Granovetter's definition of tie strength. Shi et al. (2014) considered tie strength to be contingent on reciprocity when they studied content sharing in the form of retweeting on Twitter. They argued that subscription networks facilitate electronic interactions, which occur more frequently between users with reciprocal ties. They also assessed overlapping neighbors between node pairs and found that reciprocal ties correspond to a higher overlap than nonreciprocal ties, a key distinction emphasized by Granovetter (1973) in terms of strong ties versus weak ties. Based on the above discussions, we consider a reciprocal tie to be stronger than a nonreciprocal tie. This allows us to draw on the rich literature of tie strength in diffusion.

## Diffusion and Contagion

A diffusion process is defined as the dynamic by which “contagions” (i.e., ideas, actions, products, and tastes) spread through a network (Baumgarten 1975). Varying scenarios—e.g., a farmer adopting newly invented hybrid seed corn (Ryan and Gross 1943), a doctor using a new prescription drug (Coleman et al. 1966), and individuals participating in social movements (Marwell and Oliver 1993)—show that affirmation needs to be received to trigger diffusion. Contagions have different levels of risk, cost, and controversy, leading to varying thresholds for adoption (Centola and Macy 2007). What determines the complexity of contagion is the number of sources needed to trigger adoption. Past research shows that the diffusion of behaviors generally has a higher adoption threshold than the diffusion of information. $^{4}$

Our study looks separately at two diffusion actions, content creation and content sharing, to disseminate charitable information proactively and voluntarily. Content creation has a higher complexity level for a number of reasons. First, content creation is riskier because content creators are held accountable for the content (e.g., the credibility of the endorsed charity or movement). Second, creating content exerts a higher cost because time and effort are needed to compose content. Third, charitable content creation is likely to be more controversial because others may suspect the motive behind such behavior to be reputation-driven instead of altruistic. As a result, one may need more adopted neighbors (i.e., participating followees) for content creation than for content sharing.

Past research on Twitter has vaguely defined diffusion, with some studies equating diffusion with sharing behaviors (Bhattacharya and Ram 2012; Taxidou and Fischer 2014) and others with original content creation (Romero et al. 2011). As Rogers (2010) notes, differentiating these two behaviors is important because they lead to different diffusion trajectories. Moreover, understanding the difference between content creation and content sharing is key to uncovering the process of seeking and processing information in order to reduce uncertainty about the advantages and disadvantages of an action to be diffused (Rogers 2010).

## Hypothesis

The concept of contagion complexity was brought up by Centola and Macy (2007) to resolve the continuing debate between two competing theories that assess the comparative strength of weak and strong ties for diffusion processes. Returning to Granovetter (1973), his strength of weak tie theory suggests that a weak tie is likely a bridge joining two sparsely connected network segments. Thus, weak ties likely possess novel information and promote diffusion that depends critically on the value of such information. Rodan and Galunic (2004) found that accessing heterogeneous knowledge from weak ties has a positive influence on managerial and innovation performance. More relevant to our study, Shi et al. (2014) developed a consumption-share model to reveal that users are more likely to share content posted by weak ties in pursuit of reputation.

Whereas weak ties can facilitate the acquisition of novel information, strong ties are considered more effective for conveying trust, applying peer pressure, and fostering cooperation (Coleman 1988). This is especially true when strong ties are defined as reciprocal ties since social capital is more likely to be accumulated when one's acts are observable. Regarding strong ties, Bond et al. (2012) found that people's voting behaviors are influenced to a greater degree by Facebook friends who are also friends offline. Aral and Van Alstyne (2011) used social networks and email content from an executive recruiting firm to show that strong ties are more effective than weak ties for information diffusion in a turbulent and high-dimensional information environment. Centola (2010) conducted an experiment to show that the diffusion of health behaviors with a high adoption threshold better benefits from strong ties than weak ones. Related to our study, strong ties on Flickr were found to encourage content creation (Zeng and Wei 2013).

To reconcile the competing theories and findings, Centola and Macy (2007) used theoretical network analysis to show that weak ties diminish in strength when the diffusion is complex and requires social reinforcement from multiple sources. Hansen's (1999) network study of an electric company's new product development found that weak ties helped with information searches across groups while simultaneously hampering the transfer of complex knowledge. A recent survey found that Facebook promotes costly and time-consuming political actions like participation in street demonstrations, while Twitter encourages the injection of political news and mobilization of information (Valenzuela et al. 2018). We follow the theory of contagion complexity to propose the following hypothesis:

Hypothesis: Strong ties have a greater impact on content creation than on content sharing, while weak ties have a greater impact on content sharing than on content creation, all else being equal.

The essence of this hypothesis is the diminishing effect of weak ties and the increasing importance of strong ties when contagions become more complex. The risk associated with a complex contagion is more likely mitigated by affirmation from strong ties. Empirical validation of this hypothesis is very limited because it requires comparison across contagions with different complexity, a protocol we follow in our empirical investigation.

## Research Context

In this section, we briefly describe the social broadcasting network of Twitter to contextualize our study. We introduce the charitable movement of Giving Tuesday and discuss our reasons for focusing on this movement.

## Tweet and Retweet

Twitter is a microblogging site that allows users to create and share content. When users log on to Twitter, their landing page is a feed of tweets posted by those they follow in reverse chronological order. Users can “like” others’ tweets as recognition of the tweet and reply to others’ tweets to express their opinions. Users may follow other users (without authorization) to receive content updates and repost their tweets for their own followers’ consumption, with the original author being highlighted as the owner of the content. $^{5}$ Previously, a tweet was limited to 140 characters; on November 7, 2017, the limit was expanded to 280 characters. In addition, it is a convention of Twitter users to amplify their content with hashtags to mark the tweets topically. Specifically, a keyword is prefixed by a # symbol and included in the tweet.

## Giving Tuesday

The hashtag #GivingTuesday was launched in 2012 by 92 $^{nd}$ Street Y $^{6}$ and the United Nations Foundation. It is a movement where users are encouraged to advocate for nonprofit organizations they value and give back to the community on the Tuesday after Black Friday and Cyber Monday following the U.S. holiday of Thanksgiving. The movement harnesses social media technology and circulates mainly on Twitter, Facebook, and Instagram. $^{7}$ Our study examines Giving Tuesday 2017, which took place on November 28, 2017. In Figure 1, we show the volume of tweets and donations reported by Blackbaud, the biggest payment processor for Giving Tuesday. We can see that a higher volume of tweets containing the hashtag #GivingTuesday is correlated with more total donations. Although actual donations are not itemized, it is generally believed that a higher volume of tweets related to #GivingTuesday leads to better fundraising performance. Our study prioritizes two behaviors that fuel this charitable movement: content creation and content sharing of other's tweets in relation to Giving Tuesday. The behaviors of content creation and sharing show significantly different levels of engagement—content creation can involve a first-person account and content sharing is based on a third-person account. Original tweets are usually emotionally charged with users' own experiences about the nonprofits that they endorse. For example, one original tweet in our study is: “I supported Fuller Center for Housing of Greater Kansas City on #GivingTuesday because they gave Calvin a fighting chance at the good life through their Greater Blessing program, which made over \$20k of needed repairs.”

![](/api/attachments/CZJ97CQA/fulltext/images/5e34629cd9fa1c2445fb1b1106fe4f80f62c6eb17fab1427812ab6271bb27938.jpg)  
Note: The social mentions reported here are different from some statistics reported online because we do not consider social posts generated prior to or after the launch of Giving Tuesday. Those tweets are usually not generated by individual users.

Figure 1. Social Mention and Donated Amount on Giving Tuesday

Shared content, on the other hand, indicates an affirmation of the charity and is aimed to broaden its exposure. For example, one user of our study retweeted a message originating from the reproductive rights organization NARAL: “RT @NARAL We’re in the fight of our lives. This #GivingTuesday, we need you to help us protect reproductive rights.” In terms of diffusion, retweeting only expands the reach of an existing post, but an original tweet reflects users’ self-presentation as an activist.

Giving Tuesday provides us with a unique opportunity to answer our research question for several reasons. First, since Giving Tuesday is an annual event that takes place on a specific date—always the Tuesday following Thanksgiving—our preselected random users were not likely to participate in the movement beforehand or afterward. This reduces the risk of truncation. Second, given the nature of charitable fundraising, posts relating to this topic have a homogenous sentiment, eliminating the potential confoundedness deriving from diverse content (Shore et al. 2016). Third, the reputation motivation inherent in prosocial behavior augments the reputational gain from content creation, making it easier for us to observe how content sharing and creation are impacted differently by reciprocity. Lastly, the pervasive engagement in Giving Tuesday provides us with ample variation in the degree to which individual users are exposed to it, allowing us to identify the effect of social influence within a single theme.

## Data

## Data Collection

At the user level, we selected random individual users to evaluate their diffusion behaviors. We randomly sampled 5,000 Twitter statuses published in the first ten days of November 2017 using Twitter API statues/sample, with five hundred random tweets collected daily. We chose this data collection period to avoid inactive or silent users, as it was close to Giving Tuesday. These tweets were created by 4,862 unique vocal Twitter users located in different local network structures of the Twittersphere. We excluded protected users—those whose tweets were “locked” and thus only available to approved followers but not for general consumption—and evaluated each remaining user to keep only individual parties. We did not include Twitter accounts administered by organizations as they likely had scheduled content to post and were less prone to social influence. Each user was kept in our sample if consensus among three Amazon Mechanical Turk workers was reached that the user was unambiguously individual and not an organization, news media, or other types of account.

![](/api/attachments/CZJ97CQA/fulltext/images/3b02834bc58c8deb5ae945ff2a6222a4d778040b6496c755f798e64058cbe4ce.jpg)  
diameter and is advantageous for information dissemination. Finally, we collected an additional 4,572,816 tweets not associated with Giving Tuesday, generated by the followee network on November 28, 2017 to control for focal users' newsfeed intensity.

All Turk workers were given instructions to examine the username, profile picture, bio, and associated tweets when drawing conclusions. $^{8}$ Following this process, we had 2,186 individual users for the analysis. Prior to Giving Tuesday, we collected these users' basic information, including their statuses, number of followers, and the date they joined Twitter. We also collected a list of their followees to construct their followee network. These users had 545,604 total followees. Right before Giving Tuesday, we conducted a user status check and found that 153 users were either deleted or suspended, leaving us with 2033 focal users (See Figure 2).

At the content level, we obtained all tweets that include the keyword “GivingTuesday” or “Giving Tuesday” on November 28, 2017. $^{9}$ There were 865,607 tweets that fit these criteria, consisting of 319,145 original tweets, 530,685 retweets, and 15,777 replies; our study focuses only on original tweets and retweets. We matched this tweet set with our focal users and their followee networks to identify user participation. We found that 39,665 tweets associated with Giving Tuesday were generated by 4,632 reciprocal followees and 12,414 nonreciprocal followees, which means that our relatively small group of focal users received 4.7% of all Giving Tuesday tweets. This demonstrates that the Twittersphere has a small effective

## Variables

We define two binary dependent variables to represent users' participation in Giving Tuesday. $Tweet_i$ takes the value of 1 if user $i$ creates at least one original post containing the keyword “Giving Tuesday” or “GivingTuesday.” $Retweet_i$ takes the value of 1 if user $i$ retweeted at least one tweet about Giving Tuesday. Otherwise, both variables take the value of 0. Among the 2,033 focal users, 56 generated original content and 157 retweeted others’ content. $^{10}$ Our independent variables are the number of reciprocal followees ( $RFollowees_i$ ) and nonreciprocal followees ( $NRFollowees_i$ ) who participated in Giving Tuesday 2017. If a focal user participated in Giving Tuesday, only followees who participated before the user’s first tweet or retweet were counted in these two measures.

![](/api/attachments/CZJ97CQA/fulltext/images/f8281397911f9789ed063901b946ccac95cfed236241be9dc50cd2f3f0de2323.jpg)

![](/api/attachments/CZJ97CQA/fulltext/images/bb9f5958dac5025dde234796b2ec38416c25323050c602e193620501cc3148c8.jpg)

![](/api/attachments/CZJ97CQA/fulltext/images/d78edac8345d4b8822797bd76795126c5ec767884b8cf6cb91f64738e2b58135.jpg)

![](/api/attachments/CZJ97CQA/fulltext/images/8363af6b102d100adc45c10788a2e1d66bcc6fb1bc57f65a5f44b8f2ddeb7c3c.jpg)  
Note: Rectangular kernel is employed when constructing the density plots. The variables are plotted with log-transformed values, and the median is reported at the original scale.

Figure 3. Density Plot of NRFollowee and RFollowee by Diffusion Choices  
![](/api/attachments/CZJ97CQA/fulltext/images/4b11d95a2f9410731f765d7c198b565986b4e47646f8de11c7daaed1fabe44c9.jpg)  
Figure 4. Histogram of Participating Followees by Reciprocity

![](/api/attachments/CZJ97CQA/fulltext/images/ccd6f604a5a7bded1868aa7537da3b03eb341aac0f23e4969e8cbcaeb8ef5443.jpg)

To provide some model-free intuition, we divided the 2,033 focal users into participants (207 users) and nonparticipants (1,826 users) of this movement. Nonparticipants are represented in black dashed lines in the top panel of Figure 3. This segment of users had a median of eight nonreciprocal followees and zero reciprocal followees that participated in the movement. It is notable that a considerable number of nonparticipants did not have any reciprocal followees involved in this movement; this pattern is not seen for participants. Participants that either created original tweets or retweeted other's content are represented by solid red lines in the top panel of Figure 3. These participants had a median of twenty-two nonreciprocal followees and two reciprocal followees that participated in this movement. From the distribution at the top panel of Figure 3, the solid red curves that represent participants significantly shift to the right of the dashed black curves that represent nonparticipants, suggesting that followees' participation plays an important role in driving focal users' participation.

We further divide the 207 participants into original content creators (or “tweeters”) and content sharing users (or “retweeters”) in the bottom panel of Figure 3. Tweeters are represented with solid green lines and retweeters are represented with dashed blue lines. Retweeters have a median value of 21 for $NRFollowees_{i}$ and 1 for $RFollowees_{i}$ , and tweeters have a median of 31 for $NRFollowees_{i}$ and 4 for $RFollowees_{i}$ . From the comparison of distributions, we see that nonreciprocal followees better differentiate tweeters from retweeters than reciprocal followees do. We plot the histogram of the log-transformed number of nonreciprocal followees ( $NRFollowees_{i}$ ) and reciprocal followees ( $RFollowees_{i}$ ) in Figure 4. The distributions are significantly different from a normal distribution, assuring the validity of the LIV method, which we detail later. Other variables are defined in Table 1 and the statistics are reported in Table 2.

## Model

## Baseline Model

Our baseline model is a probit model with a binary outcome $Tweet_{i}$ (or $Reweet_{i}$ ). We present the model with the dependent variable being $Tweet_{i}$ , and estimate both models when the outcome is $Tweet_{i}$ or $Reweet_{i}$ .

$$
T w e e t _ {i} = \left\{ \begin{array}{l l} 1, & \text { if   } T w e e t _ {i} ^ {*} \geq 0; \\ 0, & \text { otherwise. } \end{array} \right.\tag{1}
$$

A latent continuous variable $Tweet_{i}^{*}$ determines whether individuals make the decision to participate:

$$
\text { Tweet } _ {i} ^ {*} = \gamma_ {1} R F o l l o w e e s _ {i} + \gamma_ {2} N R F o l l o w e e s _ {i} + \boldsymbol {\beta} \mathbf {x} _ {i} + u _ {i},
$$

$$
\begin{array}{l} \text { where } \beta \mathbf {x} _ {i} = \beta_ {0} + \beta_ {1} \text { Tenure } _ {i} + \beta_ {2} \text { OtherPosts } _ {i} \\ \quad + \beta_ {3} \text { Statuses } _ {i} + \beta_ {4} \text { Followers } _ {i} + \beta_ {5} \text { Followees } _ {i}. \end{array} \tag {2}
$$

In this baseline model, $u_{i}$ is assumed to be independent and identically distributed. However, the independence assumption of $u_{i}$ is likely to be violated due to its potential correlation with the independent variable $RFollowees_{i}$ , or even $NRFollowees_{i}$ . If users who actively advocate for charities are more likely to hold a tie with others who share the same concerns, the correlation between users' number of participating followees and their own participation may be more an expression of latent homophily rather than social contagion (McPherson et al. 2001). Since marketers can only control the choice of influencers but not the formation of the network structure, researchers are most interested in the effect of social contagion. To test and account for the endogeneity bias resulting from homophily, a common solution is to use observed instrumental variables (IVs) that meet the “exclusion restriction”—i.e., variables need to be correlated with the endogenous variables and uncorrelated with the error term.

Despite the popularity of this method, questions have been raised regarding its untestable nature and weak instrument problem. The IVs are not testable because the exogeneity test (e.g., Hausman test) is based on the availability of valid IVs. This is a circular problem that leads to the overuse of IVs (Hueter 2016). The other common issue is the weak instrument problem that occurs when the IVs do not sufficiently explain the variation of the endogenous variable. Under such cases, using IVs will lead to more bias than not using the IVs at all (Bound et al. 1995). A further complication is related to the context of the social broadcasting network. When estimating social influence, a commonly used IV is the characteristics of focal users' friends' friends. These characteristics will affect users' friends but not the focal users directly. However, this approach is prohibited by the size of the followee network. Given the small diameter of a social broadcasting network, collecting focal users' second-degree followees would require obtaining a huge partial network. Given the above reasons, we adopt an "instrument-free" approach to test and account for the endogeneity issues.

<table><tr><td colspan="2">Table 1. Variable Definitions</td></tr><tr><td>Variables</td><td>Description</td></tr><tr><td colspan="2">Dependent Variables</td></tr><tr><td>Tweeti</td><td>Indicator variable for individual i who generated original post(s) about Giving Tuesday</td></tr><tr><td>Retweeti</td><td>Indicator variable for individual i who generated retweet post(s) about Giving Tuesday</td></tr><tr><td colspan="2">Independent Variables</td></tr><tr><td>RFolloweesi</td><td>The number of reciprocal followees who participated in Giving Tuesday (before i&#x27;s first tweet or retweet of the same topic, if any)</td></tr><tr><td>NRFolloweesi</td><td>The number of nonreciprocal followees who participated in Giving Tuesday (before i&#x27;s first tweet or retweet of the same topic, if any)</td></tr><tr><td colspan="2">Control Variables</td></tr><tr><td>Statusesi</td><td>The number of all Twitter statuses generated by i before Giving Tuesday 2017</td></tr><tr><td>Followersi</td><td>The number of Twitter users following i before Giving Tuesday 2017</td></tr><tr><td>Followeesi</td><td>The number of Twitter users followed by i before Giving Tuesday 2017</td></tr><tr><td>OtherPostsi</td><td>The number of posts not associated with Giving Tuesday on Giving Tuesday 2017 (before i&#x27;s first tweet or retweet of the same topic, if any)</td></tr><tr><td>Tenurei</td><td>The number of days since i joined the Twitter platform</td></tr></table>

Note: Log-transformations are conducted for all variables except for $Tenure_{i}$ due to the high skewness. $Tenure_{i}$ was normalized between 0 and 1 for estimation convenience.

<table><tr><td colspan="9">Table 2. Summary Statistics (N = 2,033)</td></tr><tr><td></td><td colspan="4">Transformed Scales</td><td colspan="4">Original Scales</td></tr><tr><td></td><td>Mean</td><td>Sd</td><td>Min</td><td>Max</td><td>Mean</td><td>Sd</td><td>Min</td><td>Max</td></tr><tr><td>Tweeti</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.03</td><td>0.16</td><td>0</td><td>1</td></tr><tr><td>Retweeti</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.07</td><td>0.26</td><td>0</td><td>1</td></tr><tr><td>RFolloweesi</td><td>0.55</td><td>1.06</td><td>0.00</td><td>5.99</td><td>5.30</td><td>27.46</td><td>0</td><td>398</td></tr><tr><td>NRFolloweesi</td><td>2.24</td><td>1.53</td><td>0.00</td><td>6.67</td><td>27.24</td><td>55.59</td><td>0</td><td>789</td></tr><tr><td>Followeesi</td><td>5.87</td><td>1.32</td><td>0.00</td><td>10.58</td><td>730.36</td><td>1359.23</td><td>0</td><td>39161</td></tr><tr><td>Followersi</td><td>5.70</td><td>1.60</td><td>0.00</td><td>10.49</td><td>815.39</td><td>1749.82</td><td>0</td><td>36114</td></tr><tr><td>Statusesi</td><td>8.89</td><td>1.97</td><td>0.69</td><td>13.64</td><td>26118.26</td><td>49716.31</td><td>1</td><td>839573</td></tr><tr><td>OtherPostsi</td><td>6.39</td><td>2.05</td><td>0.00</td><td>9.94</td><td>678.16</td><td>826.46</td><td>0</td><td>9421</td></tr><tr><td>Tenurei</td><td>0.45</td><td>0.25</td><td>0.00</td><td>1.00</td><td>1561.24</td><td>968.45</td><td>0</td><td>3705</td></tr></table>

## Latent Instrumental Variable Method

A family of frugal IV estimations was developed to account for endogeneity issues without the use of observed instruments (Ebbes et al. 2009; Park and Gupta 2012). We use a parametric approach in the main analysis and a semi-parametric approach in the robustness check. $^{[11]}$ The LIV approach with linear regression was introduced by Ebbes et al. (2005), and the nonlinear adaptation is discussed in Ebbes (2004). LIV assumes the existence of a latent categorical instrument variable that satisfies the exclusion restriction required for an observable instrumental variable and estimates the distribution of the latent IV together with other coefficients of interest. It not only solves the circular problem of testing exogeneity but also alleviates the weak instrument issue because the latent instrument is, by construction, the “best” IV. It has been applied in marketing studies on the effect of visual attention to advertisements (Zhang et al. 2009) and the position of text ads in search campaigns (Rutz et al. 2012), and has been extended to time series data to understand the role of online communications in sales (Sonnier et al. 2011). Most relevant to our setting, LIV has been used to account for latent homophily in the estimation of social influence (Ma et al. 2014). In our study, we follow Ebbes (2004) to devise a probit-LIV estimator to fit the binary outcome.

In the following model specification, we assume the number of participating reciprocal followees ( $RFollowwees_{i}$ ) to be endogenous and the number of participating nonreciprocal followees ( $NRFollowees_{i}$ ) to be exogenous. Theoretically, the stronger a tie connecting two people, the more similar the two people are (Laumann 1968). Therefore, homophily occurs within strong ties that manifest in a reciprocal following relationship. Also, because of the success of Giving Tuesday, many organizations and news media accounts that are one-way connected by individual accounts have participated in the event regardless of whether they have a charitable nature. Further, a separate model in which we assumed $NRFollowees_{i}$ to be endogenous was estimated and did not reveal significant dependency between the error term and the endogenous variable. Lastly, we account for the endogeneity of both $RFollowees_{i}$ and $NRFollowees_{i}$ in a robustness check, where our results hold.

To account for the dependency between $RFollowees_{i}$ and $u_{i}$ , the LIV approach decomposes the endogenous variable $RFollowees_{i}$ into an exogenous part $a_{i}'\pi$ and an endogenous part $v_{i}$ ,

$$
R F o l l o w e e s _ {i} = \boldsymbol {\alpha} _ {\mathrm{i}} ^ {\prime} \boldsymbol {\pi} + v _ {i}.\tag{3}
$$

The exogenous part $\alpha_{i}'\pi$ is a function of the latent categorical instrument $\alpha_{i}$ and the categorical means $\pi$ . The latent instrument $\alpha_{i}$ is assumed to follow an M-dimensional multinomial distribution with probability $\lambda_{j}$ for each dimension j, where $j=1,\cdots,M$ . The other component $\pi$ is a vector of categorical means $\pi_{j}$ , where $j=1,\ldots,M$ . When the value of the latent instrument for a specific dimension j is $1 (\alpha_{ij}=1)$ , individual i belongs to category j and the exogenous part takes the value of $\pi_{j}$ . For example, suppose we have M = 2 and $\pi=(\pi_{1}\quad\pi_{2})'=(0.5\quad1.5)'$ . We draw $\alpha_{i}$ for individual i from the binomial distribution to find that $\alpha_{i}=(1\quad0)'$ . We can then calculate the exogenous part for i to be $\alpha_{i}'\pi=(1\quad0)\cdot(0.5\quad1.5)'=0.5$ . If $\lambda_{1}=0.2$ and $\lambda_{2}=0.8$ , we know that $\alpha_{i}=(1\quad0)'$ with a probability of 20% and $\alpha_{i}=(0\quad1)'$ with a probability of 80%. According to this setting, $\alpha_{i}'\pi$ is uncorrelated with $u_{i}$ , and is essentially a latent discrete variable with M categorical levels.

Based on the above equations, the endogeneity issue arises if the error term $u_{i}$ of Equation (2) is correlated with the error term $v_{i}$ of Equation (3). This leads to the correlation between $RFollowees_{i}$ and $u_{i}$ . By modeling the dependency explicitly, we control for this endogeneity problem. We assume that the error terms $(u_{i},\nu_{i})$ follow a bivariate normal distribution with mean zero and variance matrix $\begin{pmatrix}\sigma_{u}^{2}&\rho\sigma_{u}\sigma_{v}\\ \rho\sigma_{u}\sigma_{v}&\sigma_{v}^{2}\end{pmatrix}$ . In Appendix A, we derive the log-likelihood function as below:

$$
\begin{array}{l} L L = \sum_ {i} \ln \left(\sum_ {j = 1} ^ {M} \lambda_ {j} \cdot \binom {\left(1 - T w e e t _ {i}\right) + \left(2 \cdot T w e e t _ {i} - 1\right)} {\times \Phi \left(\frac {\gamma R F o l l o w e e _ {i} + \boldsymbol {\beta x} _ {i} + \rho \left(\sigma_ {u} / \sigma_ {v}\right) \left(R F o l l o w e e _ {i} - \pi_ {j}\right)}{\sqrt {1 - \rho^ {2}} \sigma_ {u}}\right)}\right) \\ \cdot \phi \left(\frac {R F o l l o w e e _ {i} - \pi_ {j}}{\sigma_ {v}}\right) - \sum_ {i} \ln \sigma_ {v}, \end{array} \tag {4}
$$

where $\Phi(\cdot)$ is the cumulative density function of a standard normal distribution, and $\phi(\cdot)$ is the probability density function of a standard normal distribution. In our estimation, we cannot identify both $\sigma_{u}$ and $\sigma_{\nu}$ . Therefore, we estimate the ratio of them as $\sigma = \sigma_{u} / \sigma_{\nu}$ . Given the likelihood function, a maximum likelihood estimator was employed for estimation.

The identifying assumption of the LIV model is that the distribution of the endogenous variable is significantly different from a normal distribution. This stems from the normality assumption of $v_{i}$ . If the latent variable does not differ significantly from a normal distribution, the algorithm will fail to distinguish it from the error term. To validate the identification of our estimation, we first show in Figure 4 that RFollowees and NRFollowees are very skewed. We then conduct a comprehensive simulation study in the second section of Appendix A, where we simulate an endogenous variable that appears similar to the one we have. The simulation shows the good performance of our estimation method in alleviating endogeneity.

## Results

## Model Selection

For the LIV model, we determined the number of levels (M) for the latent discrete variable following Ebbes et al. (2005). We calculated the integrated classification likelihood (ICL), Akaike information criterion (AIC), and Bayesian information criterion (BIC) when M equals 2, 3, and 4, respectively. The ICL is a modified version of BIC which adds a penalty for the entropy of the categorization and is more suitable for selecting the component number in mixture models. The fitness statistics are reported in Table 3, where a three-class model outperforms both when the outcome is tweeting original content and when the outcome is retweeting others' content.

## Main Results

The estimated coefficients for the naive probit model and the LIV model are reported in Table 4. We see that content creation is positively affected by reciprocal followees but not nonreciprocal followees. Conversely, retweeting behavior is positively affected by both reciprocal and nonreciprocal followees, with the latter having a greater impact, as shown in the LIV model. The coefficient for the effect of the reciprocal followees on retweeting is reduced from $\gamma_{1}^{Baseline-Retweet} = 0.172$ ( $p$ -value $< 0.01$ ) in the baseline model to $\gamma_{1}^{LIV-Retweet} = 0.112$ ( $p$ -value $< 0.05$ ) in the LIV model, showing that $34.9\%$ of the estimated effect in the baseline model is likely spurious. To test our hypothesis, we vertically compare the effects of reciprocal and nonreciprocal followees on both processes. Such a comparison is meaningful because we use the same sample in both processes with standard binary outcomes. The reciprocal followees have a larger impact on content creation ( $\gamma_{1}^{LIV-Tweet} = 0.293$ , $p$ -value $< 0.01$ ) than on retweeting ( $\gamma_{1}^{LIV-Reweet} = 0.112$ , $p$ -value $< 0.05$ ). The difference between coefficients is significant according to the Z-test with a $p$ -value less than 0.01 (Clogg et al. 1995; Paternoster et al. 1998). As noted earlier, nonreciprocal followees have a null effect on content creation and a positive effect on content sharing ( $\gamma_{2}^{LIV-Reweet} = 0.19$ , $p$ -value $< 0.01$ ). Such a difference in the statistical significance confirms that weak ties play a more salient role in content sharing than content creation. Thus, our hypothesis is fully supported.

Other findings involving the control variables reveal interesting patterns. Neither the number of users' followers (Followers $_{i}$ ) nor followees (Followees $_{i}$ ) have a significant correlation with users' content creation during this event. However, on retweeting, the number of users' followers (Followers $_{i}$ ) has a negative impact, while the number of users' followees (Followees $_{i}$ ) has a positive impact. This shows that retweeting has a higher dependency on the network in which users are embedded and with richer sources of information, users are more likely to share. However, users' concerns regarding sharing charitable content seem to grow with audience size. The number of followees' other tweets (OtherPosts $_{i}$ ) is generally negatively related to users' participation in the charitable movement, possibly because other posts dilute the message of Giving Tuesday. In addition, with more past statuses (Statuses $_{i}$ ), users are more likely to share content but less likely to create original content. Finally, from the estimated coefficient of Tenure $_{i}$ , early Twitter adopters are more likely to create original content, whereas new users are more inclined to share others' content.

<table><tr><td></td><td colspan="2">ICL</td><td colspan="2">AIC</td><td colspan="2">BIC</td></tr><tr><td></td><td>Original Tweet</td><td>Retweet</td><td>Original Tweet</td><td>Retweet</td><td>Original Tweet</td><td>Retweet</td></tr><tr><td>M = 2</td><td>5684.363</td><td>6185.222</td><td>5606.812</td><td>6107.659</td><td>5679.837</td><td>6180.683</td></tr><tr><td>M = 3</td><td>4817.755</td><td>5318.947</td><td>4737.607</td><td>5238.787</td><td>4806.866</td><td>5308.046</td></tr><tr><td>M = 4</td><td>4829.707</td><td>5330.862</td><td>4760.607</td><td>5261.787</td><td>4822.101</td><td>5323.281</td></tr></table>

Table 4. Estimation Results

<table><tr><td></td><td colspan="2">Original Tweet</td><td colspan="2">Retweet</td></tr><tr><td></td><td>Probit</td><td>LIV</td><td>Probit</td><td>LIV</td></tr><tr><td> $RFollowees_i$ </td><td>0.337***(0.0590)</td><td>0.293***(0.056)</td><td>0.172***(0.0460)</td><td>0.112**(0.044)</td></tr><tr><td> $NRFollowees_i$ </td><td>0.0213(0.0619)</td><td>0.075(0.059)</td><td>0.163***(0.0470)</td><td>0.190***(0.044)</td></tr><tr><td> $Followers_i$ </td><td>-0.0185(0.0797)</td><td>-0.006(0.080)</td><td>-0.152**(0.0633)</td><td>-0.139**(0.063)</td></tr><tr><td> $Statuses_i$ </td><td>-0.124***(0.0463)</td><td>-0.121***(0.046)</td><td>0.245***(0.0396)</td><td>0.243***(0.040)</td></tr><tr><td> $Followees_i$ </td><td>0.0621(0.0787)</td><td>0.039(0.079)</td><td>0.155***(0.0550)</td><td>0.142**(0.055)</td></tr><tr><td> $Tenure_i$ </td><td>0.611**(0.253)</td><td>0.592**(0.253)</td><td>-0.506***(0.186)</td><td>-0.515***(0.187)</td></tr><tr><td> $OtherPosts_i$ </td><td>-0.0750*(0.0422)</td><td>-0.104**(0.043)</td><td>-0.0970***(0.0278)</td><td>-0.114***(0.028)</td></tr><tr><td>ρ</td><td></td><td>0.03(0.0716)</td><td></td><td>0.102*(0.0523)</td></tr><tr><td>σ</td><td></td><td>0.407***(0.00705)</td><td></td><td>0.408***(0.00719)</td></tr><tr><td>Likelihood</td><td>-217.339</td><td>-2346.304</td><td>-469.787</td><td>-2596.894</td></tr></table>

Note: $^{*}p < 0.1$ ; $^{**}p < 0.05$ ; $^{***}p < 0.01$ .

<table><tr><td colspan="5">Table 5. LIV Parameters of the Latent Variable</td></tr><tr><td></td><td colspan="2">Original tweet</td><td colspan="2">Retweet</td></tr><tr><td> $\pi_1$ </td><td>0.126***</td><td>(0.011)</td><td>0.127***</td><td>(0.011)</td></tr><tr><td> $\pi_2$ </td><td>2.261***</td><td>(0.037)</td><td>2.265***</td><td>(0.037)</td></tr><tr><td> $\pi_3$ </td><td>4.815***</td><td>(0.071)</td><td>4.818***</td><td>(0.069)</td></tr><tr><td> $\lambda_1$ </td><td>0.822***</td><td>(0.0108)</td><td>0.823***</td><td>(0.0107)</td></tr><tr><td> $\lambda_2$ </td><td>0.141***</td><td>(0.00784)</td><td>0.140***</td><td>(0.00781)</td></tr><tr><td> $\lambda_3$ </td><td>0.0377***</td><td>(0.00551)</td><td>0.0376***</td><td>(0.00541)</td></tr></table>

Note: $^{*}p < 0.1$ ; $^{**}p < 0.05$ ; $^{***}p < 0.01$

The estimated coefficient for $\rho$ is an indicator for the existence of endogeneity. Our results show an insignificant $\rho$ for the process of content creation and a significant $\rho$ for the process of retweeting (p-value < 0.1). Since endogeneity occurs when omitted variables impact both the error terms and the endogenous variables, $^{12}$ we interpret the result of $\rho$ as follows: Unobservable factors (e.g., mutual interest in advocating for charities) drive both users' retweeting behaviors and their reciprocal followees' participation in Giving Tuesday; such factors do not drive people's original content creation concerning the charitable movement. We also note that when we assume $NRFollowees_{i}$ to be the endogenous variable, the estimated $\rho$ is insignificant for both processes. The advantage of LIV to test exogeneity helps us to accurately specify our model, for which we only assume $RFollowees_{i}$ to be endogenous.

## Other Coefficients

We report the other parameters for the LIV model in Table 5. The point estimates for the categorical means ( $\pi$ ) show good separation and the separation of the category probabilities ( $\lambda$ ) also seems to be sufficient. Ebbes (2004) considers the parameters ( $\pi$ and $\lambda$ ) that govern the exogenous part of the endogenous variable to be “nuisance” parameters—that is, of no theoretical interest. In rare cases, the predicted LIV instrument can be profiled using observed data (Ebbes 2004). However, most applications of LIV do not correspond to interpretable predicted LIV, and our study falls in this category.

## Robustness

We conducted a series of checks to examine the robustness of our findings. The first robustness check used a different and smaller charitable movement. The second and third robustness checks estimate the content creation and content sharing processes simultaneously. We incorporate users' past participation in previous Giving Tuesdays in the fourth robustness check. We use a different “instrument-free” approach to handle the scenario with two endogenous variables as another check. Further, in Appendix B, we construct a panel data structure to control for the effect of time and incorporate the length of content as an additional control variable in two robustness checks.

## Alternative Social Movement: Red Nose Day

In this robustness check, we examined users' participation in Red Nose Day, a small-scale charitable movement carried out on May 24, 2018. We obtained all tweets associated with this event through an official partner of Twitter. In total, 12,924 original tweets, 26,445 retweets, and 1,446 reply messages were procured. We matched these tweets' authors with the 2,033 Twitter users in the main analysis and found that 13 users retweeted posts containing the keyword "RedNoseDay" or "red nose day." Due to the relatively low participation rate, we did not find anyone creating original tweets related to Red Nose Day. We also obtained focal users' followees participating in Red Nose Day and their other tweets on the same day. We re-ran the analysis and reported the results in Table 6, for which the dependent variable is the retweeting decision. Based on this small-scale campaign, positive effects were found from nonreciprocal followees but not from reciprocal followees, which is consistent with our main finding.

## Alternative Model: Biprobit Model

Our analyses to this point have estimated the process of content creation and content sharing separately. However, these two processes may be interrelated, and estimating them simultaneously may lead to an efficiency improvement. $^{13}$ In this section, we propose a biprobit model to estimate the process of tweeting and retweeting simultaneously (Roodman 2009). This model assumes that the error terms of the tweeting equation and the retweeting equation follow a bivariate normal distribution. The correlation between these two error terms is assumed to be $\rho$ . The means of both error terms are assumed to be 0 and the variance of both is assumed to be 1. We report the results in Table 7. For the content creation process, only the effects of reciprocal followees are significantly positive. For the content sharing process, effects from both types of followees are significantly positive. Our hypothesis still holds that reciprocal followees have strength in promoting original content creation and nonreciprocal followees play a more significant role in content sharing. We note that the estimation of $\rho$ is significant, indicating a positive association between the error terms of these two processes.

<table><tr><td colspan="3">Table 6. Robustness: Red Nose Day (N = 2,033)</td></tr><tr><td></td><td colspan="2">Retweet</td></tr><tr><td> $RFollowees_i$ </td><td>0.0337</td><td>(0.183)</td></tr><tr><td> $NRFollowees_i$ </td><td>0.265*</td><td>(0.16)</td></tr></table>

Note: Standard errors in parentheses, $^{*}p < 0.10$ , $^{**}p < 0.05$ , $^{***}p < 0.01$ , controls not reported.

<table><tr><td colspan="3">Table 7. Robustness: Biprobit Model (N = 2033)</td></tr><tr><td colspan="3">Original Tweet</td></tr><tr><td> $RFollowees_i$ </td><td>0.33***</td><td>(0.054)</td></tr><tr><td> $NRFollowees_i$ </td><td>0.0435</td><td>(0.061)</td></tr><tr><td colspan="3">Retweet</td></tr><tr><td> $RFollowees_i$ </td><td>0.202***</td><td>(0.04)</td></tr><tr><td> $NRFollowees_i$ </td><td>0.159***</td><td>(0.0425)</td></tr><tr><td>ρ</td><td>0.442***</td><td>(0.077)</td></tr></table>

Note: Standard errors in parentheses, $^{*}p < 0.10$ , $^{**}p < 0.05$ , $^{***}p < 0.01$ , controls not reported

<table><tr><td colspan="3">Table 8. Robustness: Multinomial Probit (N = 2,033)</td></tr><tr><td colspan="3">Base</td></tr><tr><td colspan="3">Original Tweet</td></tr><tr><td> $RFollowees_i$ </td><td>0.472***</td><td>(0.078)</td></tr><tr><td> $NRFollowees_i$ </td><td>0.0815</td><td>(0.0844)</td></tr><tr><td colspan="3">Retweet</td></tr><tr><td> $RFollowees_i$ </td><td>0.255***</td><td>(0.0614)</td></tr><tr><td> $NRFollowees_i$ </td><td>0.234***</td><td>(0.0652)</td></tr></table>

Note: Standard errors in parentheses, $^{*}p < 0.10$ , $^{**}p < 0.05$ , $^{***}p < 0.01$ , controls not reported.

<table><tr><td colspan="5">Table 9. Robustness Check: Past Events (N = 2,033)</td></tr><tr><td></td><td colspan="2">Original Tweet</td><td colspan="2">Retweet</td></tr><tr><td> $RFollowees_i$ </td><td>0.306***</td><td>(0.0620)</td><td>0.166***</td><td>(0.0461)</td></tr><tr><td> $NRFollowees_i$ </td><td>0.0311</td><td>(0.0645)</td><td>0.163***</td><td>(0.0470)</td></tr><tr><td> $PastEvents_i$ </td><td>1.336***</td><td>(0.267)</td><td>0.315</td><td>(0.201)</td></tr></table>

Note: Standard errors in parentheses, $^{*}p < 0.10$ , $^{**}p < 0.05$ , $^{***}p < 0.01$ , controls not reported.

<table><tr><td colspan="5">Table 10. Robustness Check: Copula Approach (N = 2,033)</td></tr><tr><td></td><td colspan="2">Original Tweet</td><td colspan="2">Retweet</td></tr><tr><td> $RFollowees_i$ </td><td>0.538**</td><td>(0.268)</td><td>0.142</td><td>(0.215)</td></tr><tr><td> $NRFollowees_i$ </td><td>0.491</td><td>(0.32)</td><td>0.849***</td><td>(0.257)</td></tr><tr><td> $\sigma_u \cdot (\rho_{u2} - \rho_{12}\rho_{u2})/(1 - \rho_{12}^2)$ </td><td>-0.807</td><td>(0.531)</td><td>-1.16***</td><td>(0.428)</td></tr><tr><td> $\sigma_u \cdot (\rho_{u1} - \rho_{12}\rho_{u1})/(1 - \rho_{12}^2)$ </td><td>-0.419</td><td>(0.659)</td><td>0.196</td><td>(0.526)</td></tr></table>

Note: Standard errors in parentheses, $^{*}p < 0.10$ , $^{**}p < 0.05$ , $^{***}p < 0.01$ , controls not reported.

## Alternative Model: Multinomial Probit Model

In this robustness check, we classified users who both tweeted and retweeted as original content creators. Thus users' options are mutually exclusive. We then estimated both diffusion processes at the same time by allowing users to choose from three options: tweet, retweet, and not participating. A multinomial probit model is employed with both tweeting and retweeting decisions compared to the base choice of not participating (Butler and Moffitt 1982). The results are presented in Table 8, and our hypothesis still holds.

## Additional Control: Past Participation

In our main analysis, we did not account for users' past participation in Giving Tuesday because our users are a random sample from the Twittersphere. In this section, we collected all focal users' 62,208 tweets generated on Giving Tuesdays for the previous five years (11/27/2012, 12/3/2013, 12/2/2014, 12/1/2015, 11/29/2016). We found that among our focal users, four participated in the 2013 event, six participated in the 2014 event, eight participated in the 2015 event, and twelve participated in the 2016 event. We constructed a count variable $PastEvents_i$ to denote the number of past participation among users and included it in our analysis to examine the robustness of our result. As shown in Table 9, our hypothesis is still supported. From the estimated coefficient for $PastEvents_i$ , we see that past participation in Giving Tuesday promotes users' content creation related to this charitable movement but not content sharing.

## Alternative Model: Two Endogenous Variables

In this robustness check, we assume both $RFollowees_{i}$ and $NRFollowees_{i}$ to be endogenous. We use another statistical method, the copula approach, to account for the endogeneity issue. The copula approach nonparametrically estimates the marginal distribution of the endogenous regressors and uses a copula function to build the joint distribution of the endogenous regressors and the structural error term. Suppose that $H_{1}(\cdot)$ and $H_{2}(\cdot)$ are marginal distribution functions of $RFollowees_{i}$ and $NRFollowees_{i}$ that we obtained nonparametrically, and $G(u_{i})$ is the marginal distribution of $u_{i}$ where $u_{i}$ is assumed to be normally distributed.

Let $F(RFollowees_{i}, NRFollowees_{i}, u_{i})$ be the joint distribution function, and Sklar's Theorem states the existence of a copula function C such that

$$
\begin{array}{r l} F (R F o l l o w e e s _ {i}, N R F o l l o w e e s _ {i}, u _ {i}) & = C \left(H _ {1} \left(R F o l l o w e e s _ {i}\right), H _ {2} \left(N R F o l l o w e e s _ {i}\right), G \left(u _ {i}\right)\right) \\ & = C \left(R F o l l o w e e s _ {i} ^ {*}, N R F o l l o w e e s _ {i} ^ {*}, u _ {i} ^ {*}\right), \end{array} \tag {5}
$$

where $H_{1}(RFollowees_{i})$ , $H_{2}(NRFollowees_{i})$ , and $G(u_{i})$ are probability integral transformations represented by $RFollowees_{i}^{*}$ , $NRFollowees_{i}^{*}$ , and $u_{i}^{*}$ . We operationalize C as a Gaussian copula such that

$$
\begin{array}{c} C \left(R F o l l o w e e s _ {i} ^ {*}, N R F o l l o w e e s _ {i} ^ {*}, u _ {i} ^ {*}\right) = \Psi \left(\Phi^ {- 1} \left(R F o l l o w e e s _ {i} ^ {*}\right), \right. \\ \Phi^ {- 1} \left(N R F o l l o w e e s _ {i} ^ {*}\right), \Phi^ {- 1} \left(u _ {i} ^ {*}\right)), \end{array} \tag {6}
$$

where $\Psi$ denotes a three-dimensional multivariate normal distribution. We then have

$$
\binom{R F o l l o w e e s _ {i} ^ {*}}{N R F o l l o w e e s _ {i} ^ {*}} \sim N \left(\left[ \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right], \left[ \begin{array}{c c c} 1 & \rho_ {1 2} & \rho_ {u 1} \\ \rho_ {1 2} & 1 & \rho_ {u 2} \\ \rho_ {u 1} & \rho_ {u 2} & 1 \end{array} \right]\right),\tag{7}
$$

where the variance for $RFollowees_{i}^{*}$ and $NRFollowees_{i}^{*}$ are assumed to be one, and that for the structural error term is assumed to be $\sigma_{u}$ . Using the marginal distribution of multivariate normal distribution, we have:

$$
\begin{array}{l} \text {Tweet} _ {i t} ^ {*} = \gamma_ {1} R F o l l o w e e s _ {i} + \gamma_ {2} N R F o l l o w e e s _ {i} \\ \quad + \sigma_ {u} \cdot \frac {\rho_ {u 1} - \rho_ {1 2} \rho_ {u 2}}{1 - \rho_ {1 2} ^ {2}} \cdot R F o l l o w e e _ {i} ^ {*} \\ \quad + \sigma_ {u} \cdot \frac {\rho_ {u 2} - \rho_ {1 2} \rho_ {u 2}}{1 - \rho_ {1 2} ^ {2}} \cdot N R F o l l o w e e _ {i} ^ {*} \\ \quad + \boldsymbol {\beta} \mathbf {x} _ {i} + \sigma_ {u} \cdot \sqrt {1 - \rho_ {u 1} ^ {2} - \frac {\left(\rho_ {u 2} - \rho_ {1 2} \rho_ {u 1}\right) ^ {2}}{1 - \rho_ {1 2} ^ {2}}} \cdot \omega , \\ \text { where } \boldsymbol {\beta} \mathbf {x} _ {i} = \beta_ {0} + \beta_ {1} T e n u r e _ {i} + \beta_ {2} O t h e r P o s t s _ {i t} \\ \quad + \beta_ {3} S t a t u s _ {i} + \beta_ {4} F o l l o w e e s _ {i} + \beta_ {5} F o l l o w e e s _ {i}. \end{array} \tag {8}
$$

$\omega$ is a random variable not related to any other variable in Equation (8), and we can unbiasedly estimate the coefficients of $\gamma_{1}$ and $\gamma_{2}$ with variables $RFollowee_{i}^{*}$ and $NRFollowee_{i}^{*}$ included in the estimation. From the estimation results in Table 10, we find that tweeting is only affected by reciprocal followees and retweeting behavior is only affected by nonreciprocal followees, which is consistent with our hypothesis. The diminished significance from reciprocal followees on retweeting decisions may be due to specifying an exogenous variable NRFollowees as endogenous.

## Discussion

## Key Findings

In this study, we found that charitable content creation is prompted by reciprocal followees but not nonreciprocal followees. However, charitable content sharing is invoked by both reciprocal and nonreciprocal followees, with nonreciprocal followees having a greater impact. Below, we leverage the rich tweet content to exemplify theoretical arguments in support of the hypothesis and further interpret the results.

## Qualitative Observations & Future Research

Our hypothesis posits that weak ties promote content sharing because they bring high-quality content. Indeed, we observe that tweets from nonreciprocal ties that prompt content sharing are often novel, such as this one: "Google adds a donate button to search results to encourage giving during the holidays." In contrast, reciprocal followees' tweets that were not retweeted typically did not contain novel information, such as "When communities need us the most, we're there. Please, remember the #RedCross today."

To explain why weak ties have no significant impact on content creation, we argue that content creation is usually associated with high-cost actions such as charitable giving. As evidence, all tweets in our sample that report giving are originally created content because self-announcement is based on the first-person account. For example, one wrote, “I gave to @kcpetproject on #GivingTuesday because I had to show some love to the creatures, too!” Besides, content creation is of high risk as content creators may be held accountable when they endorse a charitable organization, especially a less reputable or less popular one. For example, one focal user followed multiple reciprocal followees to support @A4A\_org, a nonprofit organization with only four thousand followers. This is less likely to happen if this user does not observe sufficient affirmation from strong ties.

Lastly, we argue that a nonreciprocal relationship prohibits the accumulation of social capital (Rogers and Kincaid 1981). A significant form of social capital is an effective norm, or more intuitively, social pressure. For example, if your participation is driven by social pressure from your reciprocal followee Matthew, you may want to leverage visible channels to ensure that your participation is observed. When retweeting an existing post, Matthew may not notice your effort because the original tweeter is highlighted as creating the content. As evidence of people's desire to be observed, one focal user tweeted “On #GivingTuesday; I warmly giveBackToALLofU!” with a few mentions of this users’ reciprocal followees who had participated in Giving Tuesday. The story is different when users mention a nonreciprocal Twitter tie such as Ellen DeGeneres because she is unlikely to notice such mentions.

Other than the above observations specific to our results, we have some other observations that may pave the way for future study. The tweet that was the most often seen includes simply the hashtag #GivingTuesday and no other content. Such content was exposed to ten unique users in our data, yet none of these users participated in Giving Tuesday. Apparently, this tweet was neither informative nor emotionally charged. The tweet “#GivingTuesday is powered by #netneutrality. Tell Congress to stop the FCC’s plan to end the open internet now.” was exposed to three unique users in our sample and was unsuccessful in inducing further participation. This tweet is more politically oriented, possibly leading to reluctance in response from the audience. One tweet that successfully induced action reads “Today #GivingTuesday, I wrote about why I give to the Internet Archive: this year we scanned a long-lost reel of film from the Japanese American incarceration camp at Jerome, AK. It hasn’t been seen in 72 years!” This tweet conveys a detailed personal story. Another successful tweet in invoking participation reads “Thanks, Jessica! We hope more of our followers will be moved to support the reporting too.” This tweet acknowledged a previous giver before calling for similar behaviors and could be a good social media marketing strategy. Such observations make us believe that it is promising to examine the lexical features of content in persuasiveness—the ability to induce desirable economic or social behaviors. Given the increasing call for socially responsible digital platforms, such studies are urgently needed to understand digital social movements.

## Theoretical Implications

Our study makes a distinct theoretical contribution to the literature. Information technology has been considered a new vehicle for building social networks (Bandura 2009). It has been well documented that electronic social networks transcend the barriers of time and space, unlike traditional social networks (Garton et al. 1997). Wellman (1997) proposed the importance of studying online interaction using a social network approach and specifically listed strength of tie as a topic of investigation. Our study followed this research agenda and discovered that reciprocal and nonreciprocal followees facilitate distinct yet complimentary paths for information diffusion. This new perspective allows us to tap into the rich literature of sociology and social network to understand social broadcasting networks. More importantly, we provide empirical evidence for Centola and Macy's (2007) contagion complexity theory in the social media context and expand the explanatory power of the theory in the digital world.

We expanded past works by differentiating between content creation and content sharing. In contrast to the previous finding that shows a similar topical pattern between original and shared content (Geva et al. 2019), we discover the different network factors that drive those two diffusion processes. The delineation between content creation and sharing also enhances the understanding of social media as a way to process citizen-driven information collectively (Oh et al. 2013). Specifically, content creation drives content diversity (i.e., emancipatory) and content sharing promotes content concentration (i.e., hegemonic). To this end, we answer the call of Miranda et al. (2016) to “compare different digitalized processes” to develop a more comprehensive understanding of the differentiating effects of these processes.

## Practical Implications

Our findings have direct implications for social media marketing. To promote content sharing and raise more awareness, charitable campaign managers should encourage celebrity or media accounts (i.e., weak ties) to broadcast novel information like corporate matching programs and new ways of fundraising. To deepen the conversation, managers should encourage users to share their own stories and invite their friends to do the same. Further, when the contagion is complex, like dumping a bucket of icy water over one's head, campaigns making use of social pressure, like friend tagging, may work better (Townsend 2014).

The diffusion patterns we found can potentially be generalized into social movements concerning public welfare or even social media marketing in general. Individual behaviors can only be integrated into collective actions when the behaviors meet the expectations and values of the community. Therefore, it is critical to form social norms in order to launch social movements or marketing campaigns successfully. For example, to encourage Twitter users to announce their voting behavior in a presidential election, marketing managers need to prioritize users who are deeply embedded in the network. Users with many reciprocal relationships are good choices for marketing investments, as they may effectively drive the chain of adoption actions.

## Limitations and Conclusions

There are a few limitations of our study. First, our focus on charitable movements means that the diffusion complexity of tweeting and retweeting is significantly different than other contexts. For example, corporations sometimes launch social responsibility programs to pledge a fixed monetary amount to charities for every social media mention that includes a specific keyword. Our findings may not hold in this case, as the original content creation merely necessitates copying and pasting the keyword. Second, we focus on the tweets posted on the exact date of Giving Tuesday. Different findings may be generated by looking at the dynamics before and after the event. Third, our work is conducted at a node level but not a dyad level because we do not know which tweet triggered users to post on a particular topic. Therefore, we lack insights into how different tweet content persuades readers. Moreover, social broadcasting sites are rich in ties that feature the need for content consumption. In other networking environments with different types of ties, like Facebook, where online friends often maintain offline relationships, we may see different dynamics of diffusion. In addition, our data sample represents users who actively generate or share content but not those who only use Twitter to acquire information. Finally, due to data limitations, we did not examine social influence measures in conjunction with fundraising outcomes. Future research can fill this void by linking social media topic richness (results of content creation) and topic mention volume (results of content sharing) to fundraising outcomes.

By comparing content creation and content sharing, our findings contribute to the debate on the comparative strength of strong and weak ties. This unique angle distinguishes our study from existing research on information systems and online communities. Given the need to engage individuals in collective actions of various contexts (e.g., political movements, product adoption, professional collaboration, and cultural interactions), close scrutiny of diffusion complexity is compelling. Along with contributing to the theoretical understanding of the diffusion process in social broadcasting networks, we hope that our study helps practitioners better strategize for their social media campaigns.

## Acknowledgments

The authors thank the senior editor, associated editor, and three anonymous reviewers for their insightful comments and constructive suggestions. This work was supported in part by the National Natural Science Foundation of China [Grants 71729001 and 71490723].

## References

Aral, S., and Van Alstyne, M. 2011. “The Diversity-Bandwidth Trade-Off,” American Journal of Sociology (117:1), pp. 90-171.

Bakshy, E., Hofman, J. M., Mason, W. A., and Watts, D. J. 2011. "Everyone's an Influencer: Quantifying Influence on Twitter," in Proceedings of the Fourth ACM International Conference On Web Search And Data Mining, pp. 65-74.

Bandura, A. 2009. “Social Cognitive Theory of Mass Communication,” in Media Effects, M. B. Oliver, A. A. Raney, and J. Bryant (eds.), New York: Routledge, pp. 110-140.

Baumgarten, S. A. 1975. “The Innovative Communicator in the Diffusion Process,” Journal of Marketing Research (12:1), pp. 12-18.

Bhattacharya, D., and Ram, S. 2012. “Sharing News Articles Using 140 Characters: A Diffusion Analysis on Twitter,” in Proceedings of the IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM), pp. 966-971.

Bond, R. M., Fariss, C. J., Jones, J. J., Kramer, A. D., Marlow, C., Settle, J. E., and Fowler, J. H. 2012. “A 61-Million-Person Experiment in Social Influence and Political Mobilization,” Nature (489:7415), p. 295.

Bound, J., Jaeger, D. A., and Baker, R. M. 1995. “Problems with Instrumental Variables Estimation When the Correlation Between the Instruments and the Endogenous Explanatory Variable Is Weak,” Journal of the American Statistical Association (90:430), pp. 443-450.

Butler, J. S., and Moffitt, R. 1982. “A Computationally Efficient Quadrature Procedure for the One-Factor Multinomial Probit Model,” Econometrica: Journal of the Econometric Society (50:3), pp. 761-764.

Castillo, C., El-Haddad, M., Pfeffer, J., and Stempeck, M. 2014. "Characterizing the Life Cycle of Online News Stories Using Social Media Reactions," in Proceedings of the 17th ACM Conference on Computer Supported Cooperative Work & Social Computing, pp. 211-223.

Centola, D. 2010. “The Spread of Behavior in an Online Social Network Experiment,” Science (329:5996), pp. 1194-1197.

Centola, D., and Macy, M. 2007. “Complex Contagions and the Weakness of Long Ties,” American Journal of Sociology (113:3), pp. 702-734.

Clogg, C. C., Petkova, E., and Haritou, A. 1995. “Statistical Methods for Comparing Regression Coefficients between Models,” American Journal of Sociology (100:5), pp. 1261-1293.

Coleman, J. S. 1988. “Free Riders and Zealots: The Role of Social Networks,” Sociological Theory (6:1), pp. 52-57.

Coleman, J. S., Katz, E., and Menzel, H. 1966. Medical Innovation: A Diffusion Study. Indianapolis, IN: Bobbs-Merrill Co.

Cropanzano, R., and Mitchell, M. S. 2005. “Social Exchange Theory: An Interdisciplinary Review,” Journal of Management (31:6), pp. 874-900.

Cunha, E., Magno, G., Comarela, G., Almeida, V., Gonçalves, M. A., and Benevenuto, F. C. 2011. “Analyzing the Dynamic Evolution of Hashtags on Twitter: A Language-Based Approach,” Proceedings of the Workshop on Languages in Social Media, pp. 58-65.

Davis, J. A. 1970. “Clustering and Hierarchy in Interpersonal Relations: Testing Two Graph Theoretical Models on 742 Sociomatrices,” American Sociological Review, (35:5), pp. 843-851.

Ebbes, P. 2004. “Latent Instrumental Variables,” Unpublished Ph.D. Thesis, University of Groningen, Groningen, Netherlands.

Ebbes, P., Wedel, M., and Böckenholt, U. 2009. “Frugal IV Alternatives to Identify the Parameter for an Endogenous Regressor,” Journal of Applied Econometrics (24:3), pp. 446-468.

Ebbes, P., Wedel, M., Böckenholt, U., and Steerneman, T. 2005. "Solving and Testing for Regressor-Error (in) Dependence When No Instrumental Variables Are Available: With New Evidence for the Effect of Education on Income," Quantitative Marketing and Economics (3:4), pp. 365-392.

Friedkin, N. 1980. “A Test of Structural Features of Granovetter’s Strength of Weak Ties Theory,” Social Networks (2:4), pp. 411-422.

Gaffney, D. 2010. “Iranelection: Quantifying Online Activism,” in Proceedings of the Web Science Conference, Raleigh, NC.

Garton, L., Haythornthwaite, C., and Wellman, B. 1997. "Studying Online Social Networks," Journal of Computer-Mediated Communication (3:1), JCMC313.

Geva, H., Oestreicher-Singer, G., and Saar-Tsechansky, M. 2019. “Using Retweets When Shaping Our Online Persona:

Topic Modeling Approach," MIS Quarterly (43:2), pp. 501-524.

Gleason, B. 2013. “#Occupy Wall Street: Exploring Informal Learning About a Social Movement on Twitter,” American Behavioral Scientist (57:7), pp. 966-982.

Granovetter, M. 1983. “The Strength of Weak Ties: A Network Theory Revisited,” Sociological Theory (1), pp. 201-233.

Granovetter, M. S. 1973. “The Strength of Weak Ties,” American Journal of Sociology (78:6), pp. 1360-1380.

Hansen, M. T. 1999. “The Search-Transfer Problem: The Role of Weak Ties in Sharing Knowledge Across Organization Subunits,” Administrative Science Quarterly (44:1), pp. 82-111.

Hueter, I. 2016. “Latent Instrumental Variables: A Critical Review,” Institute for New Economic Thinking, Working Paper 46 (https://www.ineteconomics.org/uploads/papers/WP\_46\_Hueter.pdf).

Java, A., Song, X., Finin, T., and Tseng, B. 2007. “Why We Twitter: Understanding Microblogging Usage and Communities,” in Proceedings of the 9th WebKDD and 1st SNA-KDD 2007 Workshop On Web Mining And Social Network Analysis, pp. 56-65.

Laumann, E. 1968. “Interlocking and Radial Friendship Networks: A Cross-sectional Analysis,” Working Paper, Center for Research on Social Organization, Department of Sociology, University of Michigan (https://deepblue.lib.umich.edu/bitstream/handle/2027.42/50846/65.pdf;sequence=1).

Ma, L., Krishnan, R., and Montgomery, A. L. 2014. “Latent Homophily or Social Influence? An Empirical Analysis of Purchase within a Social Network,” Management Science (61:2), pp. 454-473.

Marwell, G., and Oliver, P. 1993. The Critical Mass in Collective Action, Cambridge: Cambridge University Press.

McPherson, M., Smith-Lovin, L., and Cook, J. M. 2001. “Birds of a Feather: Homophily in Social Networks,” Annual Review of Sociology (27:1), pp. 415-444.

Miranda, S. M., Young, A., and Yetgin, E. 2016. “Are Social Media Emancipatory or Hegemonic? Societal Effects of Mass Media Digitization,” MIS Quarterly (40:2), pp. 303-329.

Oh, O., Agrawal, M., and Rao, H. R. 2013. “Community Intelligence and Social Media Services: A Rumor Theoretic Analysis of Tweets During Social Crises,” MIS Quarterly (37:2), pp. 407-426.

Park, S., and Gupta, S. 2012. “Handling Endogenous Regressors by Joint Estimation Using Copulas,” Marketing Science (31:4), pp. 567-586.

Paternoster, R., Brame, R., Mazerolle, P., and Piquero, A. 1998. "Using the Correct Statistical Test for the Equality of Regression Coefficients," Criminology (36:4), pp. 859-866.

Petrovic, S., Osborne, M., and Lavrenko, V. 2011. “RT to Win! Predicting Message Propagation in Twitter,” ICWSM (11), pp. 586-589.

Putnam, R. D. 1995. “Tuning in, Tuning Out: The Strange Disappearance of Social Capital in America,” PS: Political Science & Politics (28:4), pp. 664-683.

Rodan, S., and Galunic, C. 2004. “More Than Network Structure: How Knowledge Heterogeneity Influences

Managerial Performance and Innovativeness,” Strategic Management Journal (25:6), pp. 541-562.

Rogers, E. M. 2010. Diffusion of Innovations, New York: Simon & Schuster.

Rogers, E. M., and Kincaid, D. L. 1981. Communication Networks: Toward a New Paradigm for Research, New York: Free Press.

Romero, D. M., Meeder, B., and Kleinberg, J. 2011. "Differences in the Mechanics of Information Diffusion across Topics: Idioms, Political Hashtags, and Complex Contagion on Twitter," Proceedings of the 20th International Conference on the World Wide Web, pp. 695-704.

Roodman, D. 2009. “Estimating Fully Observed Recursive Mixed-Process Models with Cmp,” Center for Global Development, Working Paper 168 (available at https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=1392466).

Rutz, O. J., Bucklin, R. E., and Sonnier, G. P. 2012. “A Latent Instrumental Variables Approach to Modeling Keyword Conversion in Paid Search Advertising,” Journal of Marketing Research (49:3), pp. 306-319.

Ryan, B., and Gross, N. C. 1943. “The Diffusion of Hybrid Seed Corn in Two Iowa Communities,” Rural Sociology (8:1), pp. 15-24.

Sandefur, R. L., and Laumann, E. O. 1998. “A Paradigm for Social Capital,” Rationality and Society (10:4), pp. 481-501.

Shi, Z., Rui, H., and Whinston, A. B. 2014. “Content Sharing in a Social Broadcasting Environment: Evidence from Twitter,” MIS Quarterly (38:1), pp. 123-142.

Shore, J., Baek, J., and Dellarocas, C. 2016. “Network Structure and Patterns of Information Diversity on Twitter,” Boston University Questrom School of Business, Research Paper 2813342 (available at https://papers.ssrn.com/ sol3/papers.cfm?abstract\_id=2813342#)

Smith, M. A., and Kollock, P. 1999. Communities in Cyberspace, New York: Routledge.

Sonnier, G. P., McAlister, L., and Rutz, O. J. 2011. “A Dynamic Model of the Effect of Online Communications on Firm Sales,” Marketing Science (30:4), pp. 702-716.

Taxidou, I., and Fischer, P. M. 2014. “Online Analysis of Information Diffusion in Twitter,” in Proceedings of the 23rd International Conference on World Wide Web, pp. 1313-1318.

Townsend, L. 2014. “How Much Has the Ice Bucket Challenge Achieved?” BBC (https://www.bbc.com/news/magazine-29013707)

Valenzuela, S., Correa, T., and Gil de Zúñiga, H. 2018. “Ties, Likes, and Tweets: Using Strong and Weak Ties to Explain Differences in Protest Participation across Facebook and Twitter Use,” Political Communication (35:1), pp. 117-134.

Wejnert, B. 2002. “Integrating Models of Diffusion of Innovations: A Conceptual Framework,” Annual Review of Sociology (28:1), pp. 297-326.

Wellman, B. 1997. “An Electronic Group Is Virtually a Social Network,” Culture of the Internet (4), pp. 179-205.

Zeng, X., and Wei, L. 2013. “Social Ties and User Content Generation: Evidence from Flickr,” Information Systems Research (24:1), pp. 71-87.

Zhang, J., Wedel, M., and Pieters, R. 2009. “Sales Effects of Attention to Feature Advertisements: A Bayesian Mediation Analysis,” Journal of Marketing Research (46:5), pp. 669-681.

## About the Authors

Xue (Jane) Tan is an assistant professor in the Department of Operations and Decision Technologies, Kelley School of Business, Indiana University. She received her Ph.D. in business administration from the Foster School of Business, University of Washington. Her research interests include social network analysis, social media fundraising, online volunteerism, and electronic commerce. She has published in Information Systems Research.

Yingda Lu is an assistant professor in the College of Business Administration, University of Illinois, Chicago. He obtained his Ph.D. in information systems at the Tepper School of Business, Carnegie Mellon University. His research leverages economic theory with state-of-the-art empirical methods to provide actionable policies to improve the design of various social media platforms. His research has appeared in top academic journals such as Management Science and MIS Quarterly, as well as top conferences such as the International Conference on Information Systems.

Yong Tan is the Michael G. Foster Endowed Professor of Information Systems at the Michael G. Foster School of Business, University of Washington, and a Distinguished Fellow of the INFORMS Information Systems Society. His research interests include social media and networks, mobile and electronic commerce, and big data analytics. He has published in MIS Quarterly, Information Systems Research, Management Science, among other outlets. He is a senior editor at Information Systems Research.

## Appendix A

## LIV Maximum Likelihood Estimator

## Maximum Likelihood Estimator

The error terms in Equations (2) and (3), $(u_{i}, v_{i})$ , are assumed to follow a bivariate normal with mean 0 and variance matrix:

$$
\left( \begin{array}{c c} \sigma_ {u} ^ {2} & \rho \sigma_ {u} \sigma_ {v} \\ \rho \sigma_ {u} \sigma_ {v} & \sigma_ {v} ^ {2} \end{array} \right).
$$

Therefore, the joint probability of $\left(Tweet_{i}^{*}, RFollowees_{i}\right)$ conditional on $x_{i}$ and category j $prob\left(Tweet_{i}^{*}, RFollowees_{i} \mid x_{i}, j\right)$ , is a bivariate normal with the mean:

$$
\binom{\gamma \pi_ {j} + \boldsymbol {\beta} \mathbf {x} _ {i}}{\pi_ {j}},
$$

and variance matrix:

$$
\left( \begin{array}{c c} \gamma^ {2} \sigma_ {\nu} ^ {2} + 2 \gamma \rho \sigma_ {u} \sigma_ {\nu} + \sigma_ {u} ^ {2} & \gamma \sigma_ {\nu} ^ {2} + \rho \sigma_ {u} \sigma_ {\nu} \\ \gamma \sigma_ {\nu} ^ {2} + \rho \sigma_ {u} \sigma_ {\nu} & \sigma_ {\nu} ^ {2} \end{array} \right).
$$

Note that $\gamma$ refers to $\gamma_{1}$ in Equation (2) because we now only treat $RFollowee_{i}$ as endogenous. We then have:

$$
\operatorname{prob} \left(T w e e t _ {i} ^ {*}, R F o l l o w e e _ {i} \mid \mathbf {x} _ {i}, j\right) = \operatorname{prob} \left(T w e e t _ {i} ^ {*} \mid R F o l l o w e e _ {i}, \mathbf {x} _ {i}, j\right) \times \operatorname{prob} \left(R F o l l o w e e _ {i} \mid j\right),
$$

where:

$$
\operatorname{prob} \left(R F o l l o w e e _ {i} \mid j\right) = \frac {1}{\sigma_ {\nu}} \phi \left(\frac {R F o l l o w e e _ {i} - \pi_ {j}}{\sigma_ {\nu}}\right),
$$

and $\phi$ is the PDF of standard Normal. $prob\left(Tweet_{i}^{*} \mid RFollowee_{i}, \mathbf{x}_{i}, j\right)$ follows a normal distribution with the mean:

$$
E \left(T w e e t _ {i} ^ {*} \mid R F o l l o w e e _ {i}, \mathbf {x} _ {i}, j\right) = \gamma \pi_ {j} + \boldsymbol {\beta} \mathbf {x} _ {i} + \left(\gamma + \rho \frac {\sigma_ {u}}{\sigma_ {v}}\right) \left(R F o l l o w e e _ {i} - \pi_ {j}\right),
$$

and the variance:

$$
\operatorname{Var} \left(\text { Tweet } _ {i} ^ {*} \mid R \text { Followee } _ {i}, \mathbf {x} _ {i}, j\right) = \left(1 - \rho^ {2}\right) \sigma_ {u} ^ {2}.
$$

Now we evaluate:

$$
\begin{array}{l} \text {prob} \big (T w e e t _ {i} = 1 \mid R F o l l o w e e _ {i}, \mathbf {x} _ {i}, j \big) = \text {prob} \big (T w e e t _ {i} ^ {*} \geq 0 \mid R F o l l o w e e _ {i}, \mathbf {x} _ {i}, j \big) \\ = \Phi \left(\frac {\gamma \pi_ {j} + \boldsymbol {\beta} \mathbf {x} _ {i} + \big (\gamma + \rho \big (\sigma_ {u} / \sigma_ {v} \big) \big) \big (R F o l l o w e e _ {i} - \pi_ {j} \big)}{\sqrt {1 - \rho^ {2}}   \sigma_ {u}}\right), \end{array}
$$

where $\Phi$ is the CDF of standard Normal. The log likelihood function as expressed in Equation (4) follows.

## Simulation Analysis

We use simulated data to show the validity of the LIV approach we adopt. The outcome variable y is a binary variable governed by a latent continuous variable $y^{*}$ . The endogenous variable z is a continuous variable composed of an exogenous categorical variable $\alpha^{\prime}\pi$ with two levels and an endogenous error term V. Below is the model specification.

$$
y = \left\{ \begin{array}{l l} 1, & \text { if } y ^ {*} \geq 0; \\ 0, & \text { otherwise }, \end{array} \right.
$$

$$
z = \alpha^ {\prime} \pi + v,
$$

$$
y ^ {*} = c z + b x + u,
$$

where $\pi = (\pi_1 - \pi_2)'$ , and $\alpha$ follows a binomial distribution with probability $\lambda_j$ for each dimension $j$ , where $j = 1,2$ . $(u,v)$ follows a bivariate normal distribution with the variance-covariance matrix $\Sigma = \begin{pmatrix} \sigma_u^2 & \rho \sigma_u \sigma_v \\ \rho \sigma_u \sigma_v & \sigma_v^2 \end{pmatrix}$ . Since we cannot identify both $\sigma_v$ and $\sigma_u$ , we set $\Sigma = \begin{pmatrix} 1 & \rho \frac{\sigma_v}{\sigma_u} \\ \rho \frac{\sigma_v}{\sigma_u} & \frac{\sigma_v^2}{\sigma_u^2} \end{pmatrix}$ , and consider $\frac{\sigma_v}{\sigma_u}$ as one parameter.

## Simulation Process

\- Generate exogenous variable $x \sim N(\mu = 1, sd = 2)$ .

\- Set $\lambda = (\lambda_1 - \lambda_2)' = (0.7 - 0.3)'$ . Parameter $\lambda$ is critical for the distribution of the latent instrumental variable.

\- Set $\pi = (\pi_1 - \pi_2)' = (-1 - 3)'$ . The vector of $\pi$ will determine how separate different categorical levels are.

\- Set $\Sigma = \left( \begin{array}{cc}1 & \rho \frac{\sigma_v}{\sigma_u}\\ \rho \frac{\sigma_v}{\sigma_u} & \frac{\sigma_v^2}{\sigma_u^2} \end{array} \right)$ .

• Use $\Sigma$ , we simulate a set of error terms v and u.

\- To calculate the endogenous variable $z$ , we sum up the categorical value $\pmb{a}'\pmb{\pi}$ and the error term $v$ . $\pmb{a} = (\alpha_1 - \alpha_2)'$ is a draw of the binomial distribution governed by $\lambda$ . We truncate the data at the mass of zero, and round $z$ to the nearest integer. We assume that $c = 1$ .

![](/api/attachments/CZJ97CQA/fulltext/images/191b8a39aa599d1ad19f7a825149b9263b31eeb715382ff79c8e003a817cd214.jpg)  
(a)

![](/api/attachments/CZJ97CQA/fulltext/images/7353f5c06dd07484a211f812b9cf01c405acce95d2138814be663b179171cdbd.jpg)  
(b)

![](/api/attachments/CZJ97CQA/fulltext/images/ba47353a8a1cee38ab3914c7ece52b60d566a17ddb089a2a26da2ac13ce51503.jpg)

![](/api/attachments/CZJ97CQA/fulltext/images/9cfde37fb0fa1256d4d69dbfea3ddd9717656cf587c37a780cb6d59d1a9d551a.jpg)  
(d)  
Figure A1. Generate the Endogenous Variable  
Next, we explain why we choose the specific parameters in our simulation. The goal of this simulation is to generate an endogenous variable that looks like what we have in the main analysis and to examine the performance of the LIV estimator along with that of the naïve Probit model. We went through several steps as shown in Figure A1 to achieve the first goal. In step (a), we constructed an endogenous variable z with some arbitrary parameters. We let $\lambda = (\lambda_{1} - \lambda_{2})' = (0.7 - 0.3)'$ so that we can create a mass at the low categorical level. We further let $\pi = (\pi_{1} - \pi_{2})' = (-1 - 3)'$ so that the low categorical level is below zero. This will help us create a mass at zero. From panel (a) of Figure A1, we can see the clear separation of different categorical levels. This is not what we observe in the real data. Therefore, we decreased the ratio between $\sigma_{u}$ and $\sigma_{v}$ from 1 to 0.3 so that the categorical levels are blended as in panel (b) of Figure A1. The next step is critical as we truncate our data to change the negative values to zero. One's followees may obtain different levels of utility from sharing charitable content, and we observe zero if the utility is zero or negative. This leads to the histogram of z as in panel (c) of Figure A1. We further round the endogenous variable to the closest integer in panel (d) of Figure A1, making z similar to the distribution of our endogenous variable RFollowees.

## Performance

From Table A1, we can see that when the noise is strong and the two categorical levels blend, LIV provides an unbiased estimator and is strictly better than the naïve Probit model. When the noise is medium, the LIV no longer provides an unbiased estimator but is still strictly better than the naïve Probit estimator. Lastly, in the boundary condition, when the noise is weak and the separation between categorical levels is significant, these two estimators provide similar performance. Our application does not fall into the third category because we do not observe separate categorical levels and the estimates generated by the two models were very different. Our simulation shows that the LIV estimator outperforms the naïve Probit estimator, especially when they generate different estimates.

<table><tr><td>Histogram of z</td><td> $\sigma_u / \sigma_v$ </td><td>ρ</td><td>Probit</td><td>LIV</td><td>Coupla</td></tr><tr><td rowspan="5">Histogram of z</td><td rowspan="5"> $\frac{\sigma_u}{\sigma_v} = 0.3$ </td><td>ρ=0</td><td>1.0046***(0.0334)</td><td>1.017***(0.0459)</td><td>0.978(0.055)</td></tr><tr><td>ρ=0.25</td><td>1.123***(0.0377)</td><td>0.983***(0.0439)</td><td>1.28***(0.0587)</td></tr><tr><td>ρ=0.5</td><td>1.316***(0.0448)</td><td>1.015***(0.0476)</td><td>1.719***(0.066)</td></tr><tr><td>ρ=0.75</td><td>1.587***(0.055)</td><td>1.039***(0.0533)</td><td>2.365***(0.0809)</td></tr><tr><td>ρ=1</td><td>1.991***(0.0705)</td><td>1.023***(0.0533)</td><td>3.635***(0.121)</td></tr><tr><td rowspan="5">Histogram of z</td><td rowspan="5"> $\frac{\sigma_u}{\sigma_v} = 0.5$ </td><td>ρ=0</td><td>1.00579***(0.0324)</td><td>0.995***(0.0371)</td><td>1.028***(0.0476)</td></tr><tr><td>ρ=0.25</td><td>1.104***(0.0354)</td><td>1.0145***(0.0382)</td><td>1.206***(0.0499)</td></tr><tr><td>ρ=0.5</td><td>1.247***(0.0403)</td><td>1.106***(0.0427)</td><td>1.432***(0.0545)</td></tr><tr><td>ρ=0.75</td><td>1.46***(0.0483)</td><td>1.242***(0.0511)</td><td>1.777***(0.0626)</td></tr><tr><td>ρ=1</td><td>1.646***(0.0546)</td><td>1.28***(0.0541)</td><td>2.255***(0.0737)</td></tr><tr><td rowspan="5">Histogram of z</td><td rowspan="5"> $\frac{\sigma_u}{\sigma_v} = 0.75$ </td><td>ρ=0</td><td>1.061***(0.0339)</td><td>1.061***(0.0339)</td><td>1.087***(0.0445)</td></tr><tr><td>ρ=0.25</td><td>1.075***(0.0344)</td><td>1.074***(0.0343)</td><td>1.12***(0.045)</td></tr><tr><td>ρ=0.5</td><td>1.166***(0.0375)</td><td>1.162***(0.0375)</td><td>1.232***(0.0475)</td></tr><tr><td>ρ=0.75</td><td>1.248***(0.0404)</td><td>1.24***(0.041)</td><td>1.35***(0.05)</td></tr><tr><td>ρ=1</td><td>1.231***(0.039)</td><td>1.230***(0.0104)</td><td>1.43***(0.05)</td></tr></table>

## Appendix B

## Robustness Checks

## Alternative Sample of Panel Data

To examine whether our analyses are sensitive to the sample we selected, we changed our sampling method to choose original content generators and retweeting users directly from the tweet set that contains all tweets associated with Giving Tuesday 2017. We randomly chose 500 original tweets and 500 retweets concerning Giving Tuesday. These tweets correspond to 949 unique Twitter users. We used Amazon Mechanical Turk workers to identify 257 individual users. We classify a user to be a content generator if she generated one at least original tweet; otherwise, the user is a retweeter. We ended up with 148 original content generators and 109 retweeters. Since all these users participated in the movement, we exploit their decision-making process from a panel data structure in which tweeting/retweeting is only conducted at one specific point in time. We sliced time into three-hour intervals and aggregated cumulative reciprocal and nonreciprocal followees at different times ( $CumRFollowees_{it}$ and $CumNRFollowees_{it}$ ). The same data aggregation procedure is applied to $OtherPosts_{it}$ , and all these three variables now have subscripts of individual i and time t. Such a data structure and model specification has been used in Tucker (2008) to identify network externalities in technology adoption.

<table><tr><td colspan="5">Table B1. Robustness: Panel Data</td></tr><tr><td></td><td colspan="2">Original tweet</td><td colspan="2">Retweet</td></tr><tr><td> $CumRFollowees_{it}$ </td><td>0.186*</td><td>(0.0851)</td><td>-0.0395</td><td>(0.0948)</td></tr><tr><td> $CumNRFollowees_{it}$ </td><td>0.0522</td><td>(0.0751)</td><td>0.237**</td><td>(0.0865)</td></tr><tr><td> $Followers_i$ </td><td>0.175*</td><td>(0.0719)</td><td>0.0175</td><td>(0.0777)</td></tr><tr><td> $Statuses_i$ </td><td>-0.0994*</td><td>(0.0467)</td><td>0.133**</td><td>(0.0484)</td></tr><tr><td> $OtherPosts_{it}$ </td><td>-0.456***</td><td>(0.0490)</td><td>-0.409***</td><td>(0.0510)</td></tr><tr><td> $Tenure_i$ </td><td>0.596*</td><td>(0.280)</td><td>-0.335</td><td>(0.299)</td></tr><tr><td>Hour 3-6</td><td>0.126</td><td>(0.339)</td><td>0.133</td><td>(0.377)</td></tr><tr><td>Hour 6-9</td><td>0.495</td><td>(0.329)</td><td>-0.0227</td><td>(0.376)</td></tr><tr><td>Hour 9-12</td><td>0.636</td><td>(0.349)</td><td>0.418</td><td>(0.392)</td></tr><tr><td>Hour 12-15</td><td>1.057**</td><td>(0.351)</td><td>0.598</td><td>(0.395)</td></tr><tr><td>Hour 15-18</td><td>1.199**</td><td>(0.365)</td><td>0.725</td><td>(0.411)</td></tr><tr><td>Hour 18-21</td><td>0.487</td><td>(0.422)</td><td>1.382***</td><td>(0.418)</td></tr><tr><td>Hour 21-24</td><td>0.254</td><td>(0.561)</td><td>2.080***</td><td>(0.567)</td></tr></table>

Note: Standard errors in parentheses, $^{*}p < 0.05$ , $^{**}p < 0.01$ , $^{***}p < 0.001$

From the results presented in Table B1, we can see that only reciprocal followees positively impact original content generation, and only nonreciprocal followees affect people's retweeting decisions. By looking into the time effects, we further find that retweeting is more popular after 18:00, and peaks in the last three hours of the day. On the other hand, original content generation is the most popular in the afternoon (12:00 – 18:00). Capturing time effects is essential for the panel data structure because information diffusion patterns (generating content before diffusing it) may confound with the number of participating followees.

## Length of Content

In this section, we look at the length of content users tweeted or retweeted. Length of content reflects the volume of information to be diffused. We included only participating users to explore the factors that affect content length. We find that, for original content generation, nonreciprocal followees' participation reduces the content length. However, the length is not affected by the number of participated reciprocal followees. This indicates that users perceive content shared by nonreciprocal followees as an information source. In order to produce original content that is novel to the densely knit group, users will reduce their own content length to avoid repetition. However, the content generated by their reciprocal followees is considered a kind of social reinforcement and should not affect the amount of information to be created.

<table><tr><td colspan="5">Table B2. Robustness: Content Length</td></tr><tr><td></td><td colspan="2">Original Tweet</td><td colspan="2">Retweet</td></tr><tr><td> $RFollowee_i$ </td><td>-5.055</td><td>(8.604)</td><td>-11.87**</td><td>(5.173)</td></tr><tr><td> $NRFollowee_i$ </td><td>-12.47*</td><td>(7.177)</td><td>6.960</td><td>(6.188)</td></tr></table>

Note: Standard errors in parentheses, $^{*}p < 0.10$ , $^{**}p < 0.05$ , $^{***}p < 0.01$ , controls not reported.

In terms of content sharing, the length of the retweeted post will reduce if more reciprocal followees participate in the broadcasting of this topic. However, the number of nonreciprocal followees does not significantly affect the length of content to be shared. Given that we are conducting a node-level analysis but not a dyad-level analysis, the explanation we provide below is very limited. Rather than generating original content, retweeting users base their content on their followees' content. In general, lengthy content is generated by organizations to announce their participation, such as introducing a donation matching program. Abbreviated content, on the other hand, is likely to come from individuals to announce their favorite causes. With more reciprocal followee posting, focal users are more likely to share their content that is short in length.
