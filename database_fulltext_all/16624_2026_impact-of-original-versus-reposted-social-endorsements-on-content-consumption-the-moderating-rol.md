---
otero_id: 16624
otero_key: "U9HSA6JF"
title: "Impact of original versus reposted social endorsements on content consumption: The moderating role of Endorsers’ network characteristics"
authors: "Anqi Zhao; Qian Tang"
year: "2026"
journal: "Information & Management"
doi: "10.1016/j.im.2025.104266"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of original versus reposted social endorsements on content consumption: The moderating role of Endorsers’ network characteristics Anqi Zhao, Qian Tang

## To cite this version:

Anqi Zhao, Qian Tang. Impact of original versus reposted social endorsements on content consumption: The moderating role of Endorsers’ network characteristics. Information and Management, 2026, 63 (1), pp.104266. ⟨10.1016/j.im.2025.104266⟩. ⟨hal-05447151v2⟩

HAL Id: hal-05447151 https://hal.science/hal-05447151v2

Submitted on 25 Feb 2026

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L’archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la difusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d’enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Impact of Original versus Reposted Social Endorsements on Content Consumption: The Moderating Role of Endorsers’ Network Characteristics

Anqi Zhao (Corresponding Author) Shenzhen Audencia Financial Technology Institute, Shenzhen University anqizhao@szu.edu.cn

Qian Tang School of Computing and Information Systems, Singapore Management University qiantang@smu.edu.sg

Abstract: Social endorsements broadcast endorsers’ positive attitudes toward content or products, especially to their social ties. Original endorsements created by endorsers can be propagated further as reposted endorsements. Both are important marketing tools to increase content consumption, yet their differences are unclear. This study compares the impacts of original and reposted endorsements on content consumption and their contingencies on the endorsers’ network characteristics. Using data on social endorsements of YouTube videos on Twitter, we find that original endorsements (i.e., original tweets) significantly boost content consumption, and the effect is positively moderated by the endorsers’ network size but not their tie strength. In contrast, reposted endorsements (i.e., retweets) drive content consumption only when the endorsers have a sufficiently large number of social ties or a high percentage of weak ties. Furthermore, their endorsement effects differ regarding their contingencies on the endorsement message and the endorsed content. Specifically, original endorsements are more effective when the endorsement messages demonstrate higher cognitive effort, whereas the impact of reposted endorsements does not depend on the endorsement messages created by original endorsers. Additionally, the impact of original endorsements is more pronounced for content with higher user engagement, while reposted endorsements are more effective for content with lower user engagement. Our findings provide theoretical contributions and practical implications for consumer behavior and platform operations.

Keywords: original endorsements, reposted endorsements, content consumption, tie strength, user engagement

## 1 Introduction

Social media platforms have become instrumental in shaping consumer behavior, disrupting marketing operations, influencing purchasing decisions, and driving brand engagement (Heimbach and Hinz, 2018; Salehan et al., 2017). On these social platforms, users actively showcase their experiences, testimonials, and recommendations to peers. Such online user behavior gives rise to social endorsements, the public sharing of users’ positive attitudes to content or products, especially with their social ties. As low-cost advertising, social endorsements enable businesses and content providers to connect with potential customers (Aral et al., 2013; Gong et al., 2017; Yang et al., 2019), increasing brand awareness (Aral and Walker, 2011), driving consumption (Chen et al., 2015; Kim and Kim, 2018; Li and Wu, 2018; Rui et al., 2013), and enhancing word of mouth (WOM; Lee et al. 2015). According to American Express, social endorsements may be worth \$197 billion for small businesses, as 89 of consumers are more likely to shop at a small business that friends or peers have recommended.<sup>1</sup> Marketing Charts also reported that 93% of respondents place greater trust in friend and family endorsements than any other type of advertising.<sup>2</sup> While some businesses invest heavily in sponsored endorsements by influencers to expand reach, many primarily leverage organic endorsements to capitalize on the trend while minimizing costs (Chen and Guo, 2022).

To encourage social endorsements and user interactions, numerous e-commerce and online content platforms (e.g., Amazon and YouTube) offer social plugins, program codes that can be integrated into other social platforms (e.g., Twitter, which has been known as X since 2023, and Facebook) to generate original endorsements for products or content with a single click (Heimbach and Hinz, 2018). For example, YouTube users can easily post a video link to Twitter by simply clicking a “Share” button. These original endorsements are composed by the posting endorsers and reflect their personal views on the endorsed products or content (Alatas et al., 2020). With social plugins, original endorsements often arise from cross-platform interactions, where users consume content on one platform and share it on another.

After original endorsements are created on a social platform, they can be reposted or reshared by other users, often within the platform. Reposted endorsements disseminate original endorsers’ messages further. Although users may add their own thoughts when resharing, they still attribute their opinions to the original endorsers (Firdaus et al., 2018; Gong et al., 2017; Shi et al., 2014). For example, retweets, reposted endorsements on Twitter, always start with “RT @username” to acknowledge the original endorser. Different social platforms hold mixed views on user engagement via reposting. Many social platform algorithms, including Twitter’s, consider reposts as important engagement metrics when measuring the visibility of original posts. They view reposts as active interactions and conversation starters between the original and reposting endorsers, which add depth to the engagement and help foster a sense of community on the platform. In contrast, platforms such as Instagram disallow reposting due to concerns that reposts, which primarily attract information seekers, would decrease the authenticity of social interactions and the depth of user engagement.<sup>3</sup> This controversy partly stems from a limited understanding of reposting, particularly how its mechanisms and effects differ from those of original posts.

Original and reposted endorsements can engage users differently when they consume the endorsed content. While both spread content information, original endorsements, fully owned by the endorsers, generally represent higher cognitive effort and endorser involvement (Tan et al. 2021; Yang et al. 2019). They thus often engage recipients with a closer psychological distance than reposted endorsements (Lee and Sundar, 2013). As a result, original endorsements may have a stronger persuasive effect, while reposted endorsements primarily raise content awareness. These distinct information trajectories may lead to different effects on recipients’ consumption decisions. Additionally, social endorsements exert influence via the endorsers’ social networks, including factors such as network size and tie strength. Given the differences between original and reposted endorsements, the moderating effects of these network characteristics may also differ.

The different mechanisms of original and reposted endorsements in driving content consumption have important implications for online user engagement. By exploring how endorsement effects depend on the endorsers’ network characteristics, businesses can effectively identify desirable endorsers according to users’ network size and tie strength, thereby enhancing the effectiveness of their marketing strategies. These insights can also guide social platforms in optimizing reposting features and assist message recipients in refining their endorsement strategies.

Motivated by the practical importance of endorsements, we ask the following research questions:

Q1: How do original and reposted endorsements affect content consumption differently?

Q2: How do the impacts of original and reposted endorsements on content consumption depend on the size and strength of the endorsers’ social ties?

To answer these questions, we conduct an empirical study in the cross-platform context of YouTube and Twitter, whereby YouTube videos are socially endorsed on Twitter via original tweets (i.e., original endorsements) and retweets (i.e., reposted endorsements).<sup>4</sup> We collected panel data on video characteristics and consumption from YouTube and social endorsements from Twitter between December 2017 and December 2018. To alleviate the potential endogeneity concern, we use propensity score matching (PSM) and estimate a two-stage control function model at the video-week level. The results reveal a significantly positive association between original endorsements and content consumption, which is positively moderated by the endorsers’ network size but not their tie strength. In contrast, reposted endorsements only boost content consumption significantly when the endorsers have a sufficiently large number of social ties or a high percentage of weak ties. We also perform various robustness checks to ensure the consistency of our findings.

The different moderating roles of tie strength suggest different mechanisms at play for the effects of original and reposted endorsements. To further investigate this, we examine whether their effects vary differently according to endorsement message and content characteristics. The findings show that original endorsements with messages demonstrating higher cognitive effort (i.e., longer content and more insight words) are more influential in increasing content consumption. In contrast, the effect of reposted endorsements does not depend on the characteristics of the endorsement message composed by the original endorsers. Regarding content characteristics, original endorsements have a larger effect for content with higher levels of prior user engagement, while reposted endorsements are more effective for content with lower levels of prior user engagement. Our findings contribute to the theory of social influence on consumer behavior and the practice of social media marketing operations.

## 2 Literature Review

## 2.1 Effects of Social Endorsements

Prior literature on social endorsements has focused primarily on products, as summarized in Table 1. These studies generally find that both user-generated and sponsored social endorsements can boost customer brand relationships (John et al., 2017; Park et al., 2021; Thai and Wang, 2020; Wang et al., 2021), product engagement (Xu and Liu, 2019), product adoption (Aral and Walker, 2011, 2014), and product traffic and sales (Kim and Kim, 2018; Li and Wu, 2018; Rui et al., 2013; Sun et al., 2020). Several studies have compared the effects of different endorsement types. For example, Aral and Walker (2011) compared active-personalized invitations with passive-broadcast notifications, finding that active-personalized invitations are more effective in encouraging product adoption per message, while passive-broadcast is used more frequently, generating higher total peer adoption. Both Li and Wu (2018) and Kim and Kim (2018) found that Facebook likes have a positive effect on product sales, while Twitter tweets do not. Additionally, the effect of social endorsements on product outcomes depends on the endorsers’ network characteristics, such as network size (Park et al., 2021; Rui et al., 2013; Xu and Liu, 2019) and tie strength (Aral and Walker, 2014), and product characteristics, such as product type (Li and Wu, 2018; Park et al., 2021) and product sources (Sun et al., 2020).

In contrast, studies on the effect of social endorsements for content, especially online videos, remain relatively scarce. Messing and Westwood (2014) revealed that consumers are more likely to choose online news that was recommended by others, with the presence of social endorsements mitigating the effect of content source cues. Gong et al. (2017) compared the effects of company tweets and paid influential retweets and found that company tweets directly boosted TV show viewing, whereas influentials’ retweets increased viewing only when the company tweet was informative.

Our study extends this line of research in several ways. First, the differences between original and reposted endorsements remain largely unknown, except for Gong et al. (2017), which focuses on marketer-generated tweets and retweets. However, the effect of marketergenerated or sponsored endorsements can be different from that of organic user-generated endorsements (Goh et al., 2013; Tsiakali, 2018). Compared with marketer-generated or sponsored endorsements, where the marketers either create or pay for endorsement messages (Hwang and Jeong, 2016), organic endorsements with endorsers’ genuine opinions on content or products are earned publicity and typically are perceived as more unbiased and trustworthy (Kim and Song, 2018). Second, although prior studies consider the moderating role of follower size, they overlook the potential trade-off that tie strength may decrease as network size grows (Burke, 2011; Katona et al., 2011; Roberts et al., 2009). We address this gap by examining the moderating roles of both network size and tie strength to understand the value of social endorsements in content consumption accurately. Third, besides the network characteristics of the endorsers, we further investigate how content characteristics and endorsement message features shape the effectiveness of original versus reposted endorsements, establishing a comprehensive understanding of contingencies for different endorsement strategies.

Table 1. Literature on the impact of social endorsements

<table><tr><td rowspan="3">Literature</td><td rowspan="2" colspan="2">Endorsement</td><td rowspan="3">Outcomes</td><td colspan="4">Moderators</td></tr><tr><td colspan="2">Endorser</td><td rowspan="2">Content /Product</td><td rowspan="2">Endorsement Message</td></tr><tr><td>Format</td><td>Type</td><td>Network size</td><td>Tie strength</td></tr><tr><td colspan="8">Product</td></tr><tr><td>(Thai and Wang, 2020)</td><td>Likes</td><td>Organic</td><td>Brand relationships</td><td></td><td></td><td></td><td></td></tr><tr><td>(Wang et al., 2021)</td><td>Likes</td><td>Organic</td><td>Brand passion</td><td></td><td></td><td></td><td></td></tr><tr><td>(John et al., 2017)</td><td>Likes</td><td>Organic</td><td>Brand favorability</td><td></td><td></td><td></td><td></td></tr><tr><td>(Park et al. 2021)</td><td>Influencer endorsement</td><td>Sponsored</td><td>Brand authenticity</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>(Xu and Liu, 2019)</td><td>Likes</td><td>Organic</td><td>Product engagement</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>(Aral and Walker, 2014)</td><td>Endorsement notifications</td><td>Organic</td><td>Product adoption</td><td></td><td>√</td><td></td><td></td></tr><tr><td>(Aral and Walker, 2011)</td><td>Social invitations vs. endorsement notifications</td><td>Organic</td><td>Product adoption</td><td></td><td></td><td></td><td></td></tr><tr><td>(Sun et al. 2020)</td><td>Paid endorsement</td><td>Sponsored</td><td>Product sales</td><td></td><td></td><td>√</td><td></td></tr><tr><td>(Rui et al., 2013)</td><td>Tweets</td><td>Organic</td><td>Product sales</td><td>√</td><td></td><td></td><td></td></tr><tr><td>(Li and Wu, 2018)</td><td>Likes vs. tweets</td><td>Organic</td><td>Product sales</td><td></td><td></td><td>√</td><td></td></tr><tr><td>(Kim and Kim, 2018)</td><td>Likes vs. tweets</td><td>Organic</td><td>Product sales</td><td></td><td></td><td>√</td><td></td></tr><tr><td colspan="8">Content</td></tr><tr><td>(Messing and Westwood, 2014)</td><td>Recommendations</td><td>Organic</td><td>News consumption</td><td></td><td></td><td>√</td><td></td></tr><tr><td>(Gong et al., 2017)</td><td>Company tweets vs. influencer retweets</td><td>Sponsored</td><td>TV shows consumption</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Our Study</td><td>User-generated tweets vs. retweets</td><td>Organic</td><td>Content consumption</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

## 2.2 Moderating Effects of Social Network Characteristics

First and foremost, literature related to the endorsers’ network characteristics has recognized well that the effect of social media messages on consumption depends on the messenger’s network size. For example, Gong et al. (2017) demonstrated that the effect of company tweets on TV show viewing is positively moderated by the number of newly subscribed company followers. Rui et al. (2013) studied the effect of tweet endorsements on movie sales and found that the proportion of social endorsements from users with large audiences is positively associated with movie box office revenue.

Second, another stream of related literature focuses on the role of strong ties and weak ties in information dissemination. While strong ties between close-knit members increase users’ frequency of access to information and the reliability of the accessed information because of trust and commitment (Aral and Walker, 2014), weak ties increase users’ exposure to new information (Rishika and Ramaprasad, 2019). Therefore, strong ties, often defined as reciprocated ties, are more effective in changing user behavior, such as voting (Bond et al., 2012), developing new products (Sosa, 2014), adopting applications (Aral and Walker, 2014), and creating content (Tan et al., 2021). For example, Rishika and Ramaprasad (2019) found that reciprocated ties have the greatest influence on users’ online contribution behavior, followed by nonreciprocated followee and follower ties. Similarly, Tan et al. (2021) found that reciprocal followees have a greater impact on content creation than nonreciprocal followees. In contrast, weak ties, or nonreciprocal ties, are more effective in diffusing information (Granovetter, 1973), especially for new information and innovations. For example, Tan et al. (2021) showed that weak ties are more effective in driving content sharing. Shi et al. (2014) also found that after a median-quality tweet is consumed, a weak tie is more likely to retweet

than a strong tie.

While prior research has explored how the impact of social media messages depends on network size or tie strength between the messenger and the recipient, we further differentiate the moderating role of these endorsers’ network characteristics for different endorsement formats (i.e., original versus reposted endorsement). Moreover, unlike prior studies that consider either network size or tie strength, we examine the moderating roles of both to understand the value of social networks in content consumption comprehensively.

## 3 Hypothesis Development

## 3.1 Impacts of Original and Reposted Endorsements

Social endorsements affect content consumption through two important mechanisms: the awareness effect and the persuasive effect (Rui et al., 2013). The awareness effect informs recipients of the content’s existence and affects their behavior only by putting the content in their choice set (Duan et al., 2008). In addition to raising awareness, social endorsements also represent persuasion attempts designed to influence recipients’ attitudes or decisions (Sun et al. 2020). Therefore, the persuasive effect functions by altering preferences toward the content.

Both original and reposted endorsements can disseminate content information among social media users, especially those with social ties connecting to the endorsers. By reading endorsement messages, which often include a URL link to the content, recipients can learn about the endorsed content and have the opportunity for consumption. As Tucker (2016) suggests, the awareness effect is the main effect underlying the effectiveness of social advertising, which targets networked consumers with similar responses. From this perspective, both original and reposted endorsements can promote content consumption via the awareness effect (Kim and Kim, 2018; Rui et al., 2013; Tang et al., 2019).

However, original endorsements may have a stronger persuasive effect than reposted endorsements. First, the information and opinion revealed in the original endorsement are fully owned by the endorser, demonstrating the endorser’s knowledge, skills, and creativity (Oeldorf-Hirsch and Sundar, 2015). In contrast, the reposting endorser only serves as an information intermediary and at most demonstrates agreement with the opinions of the original endorser (Shi et al., 2014). The original endorsement in the endorser’s own voice can be more convincing than the reposted endorsement simply passing on messages of others (Alatas et al., 2020). Second, the original endorsement is more costly for the endorser (Tan et al., 2021). Original endorsers have to invest more effort than reposting endorsers. They must discover the content, create the endorsement message, and post it on the social platform. When composing their messages, original endorsers often need to deliberate carefully why they endorse the content and how to articulate their opinions in clear and understandable language (Zhang et al. 2024). In contrast, reposted endorsements are often perceived as a “one-click action” on the platform, which is less cognitively demanding and represents a lower level of involvement (Shi et al., 2014). Therefore, recipients tend to trust original endorsements more than reposted endorsements. Third, the psychological distance to the original source is perceived to be shorter for original endorsements than for reposted endorsements. For the original endorsement, the original endorser is the proximal source; For the reposted endorsement, that role shifts to the reposted endorser, rendering the original endorser a distal source (Lee and Sundar, 2013). A shorter psychological distance will result in the original endorsement being perceived with higher source credibility (Hernández-Ortega, 2018). User engagement, trust, and source credibility all affect content consumption positively (Soni and Verghese, 2018).

Generally, although both original and reposted endorsements can increase content consumption, original endorsements drive content consumption via both awareness and persuasive effects, whereas reposted endorsements boost content consumption via the awareness effect primarily and if any, a weaker persuasive effect. Based on the above discussion, we expect a larger impact of original endorsements than reposted endorsements and propose the following hypothesis:

H1: Original endorsements increase content consumption more than reposted endorsements.

## 3.2 Moderating Effects of Endorsers’ Network Size

The effect of social endorsements (both original and reposted endorsements) depends on the network size of the endorsers (Gong et al., 2017; Rui et al., 2013). The central feature of social platforms is user-generated content, disseminated from the posting users to their social ties. More followers imply a larger audience that can potentially be engaged (Rui et al., 2013). When the endorser has more incoming social ties (e.g., followers and subscribers), more users will be informed of the content upon receiving the endorsement message (Zhang and Zhu, 2011). Therefore, network size will moderate the awareness effect of social endorsements positively.

Moreover, a large number of followers also indicates the high status of the endorser, which enhances the persuasive effect of the social endorsement (Huang et al., 2020). First, users with more followers have a higher degree of influence over their followers (Aral and Walker, 2012, 2014). Second, users with more followers may derive more self-image-related utility and thus be more selective about which content to share and how to share, making their endorsements more relevant and interesting (Toubia and Stephen, 2013). Therefore, network size will moderate the persuasive effect of social endorsements positively.

Based on the above discussion, we propose the following hypotheses:

H2a. When the endorsers have more followers, original endorsements increase content consumption more.

H2b. When the endorsers have more followers, reposted endorsements increase content consumption more.

## 3.3 Moderating Effects of Endorsers’ Tie Strength

Besides network size, tie strength between the endorsers and their network connections is another important factor affecting the effectiveness of social endorsements (Hershkovitz and Hayat, 2020). The elaboration likelihood model (ELM), a dual-process theory of persuasion that explains how individuals process information and how this processing affects attitude change, provides a useful framework to understand this moderating effect (Munaro et al., 2021; Park et al., 2024). According to the ELM, users form attitudes through two distinct routes: the central route, which involves high cognitive elaboration and thoughtful evaluation of information; and the peripheral route, which involves low elaboration and relies on heuristic cues or contextual signals (Petty and Cacioppo, 1986). The route activated depends on the recipient’s motivation and ability to process information (Petty and Cacioppo, 1986).

Strong ties are more likely to trigger central-route processing—scrutiny of argument quality. First, strong ties often share similar cultures, demographics, values, and beliefs because of homophily (Granovetter, 1973). Their messages are thus perceived as more relevant. Second, strong ties characterized by close interpersonal connections and frequent communication also involve a higher level of source credibility and trust (Rishika and Ramaprasad, 2019; Tan et al., 2021; Tsai and Bagozzi, 2014), which further motivates deeper cognitive elaboration.

In contrast, weak ties, such as acquaintances or distant contacts, often lack the relational closeness and trust necessary for deep engagement. While they provide novel or diverse information (Aral, 2016; Granovetter, 1983; Levin and Cross, 2004; Rodan and Galunic, 2004; Shi et al., 2014), recipients typically perceive their messages as less personally relevant or credible, reducing the motivation for elaboration. Consequently, peripheral-route processing is more likely in weak-tie contexts, where recipients rely on superficial cues such as the likability of the source or the number of reposts, rather than message substance.

Original endorsements, which typically involve cognitive investment and personalized reasoning, tend to provide rich information that supports deep elaboration, particularly when they originate from strong ties. This deeper processing enables strong ties to learn about the endorsed content and develop a nuanced understanding of its value, increasing the likelihood of consumption. We thus hypothesize as follows:

H3a. When the endorsers have greater tie strength, original endorsements increase content consumption more.

However, reposted endorsements typically lack personalized opinions and cognitive investment from the endorser. They function primarily as peripheral cues, particularly for recipients exposed to weak-tie sources. In these cases, reposting itself acts as a signal of social proof or perceived novelty, which can be persuasive despite minimal cognitive processing. Because weak-tie recipients are less motivated to scrutinize content deeply, they are more likely to infer value from the act of reposting, relying on peripheral cues rather than deliberative evaluation. Therefore, we hypothesize as follows:

H3b. When the endorsers have weaker tie strength, reposted endorsements increase content consumption more.

## 4 Empirical Setting

## 4.1 Research Context and Data Collection

Our cross-platform empirical setting is YouTube and Twitter, the leading platforms for online videos and short messages, respectively. On Twitter, original endorsements of a YouTube video are created in the form of original tweets containing the video link. These original tweets may be retweeted by others, generating reposted endorsements, in which the original endorser will still be highlighted as the initial author of the tweet message. Figure 1 illustrates an example where Joe creates an original tweet sharing a YouTube video and Ann later retweets it. Typically, users’ tweets and retweets are publicly shown and automatically appear on the newsfeeds of their followers. Most follower–followee relationships are one-way ties. When two users follow each other, they have a mutual tie. According to prior literature, we consider the mutual tie to be a strong tie and the one-way tie to be a weak tie (Shi et al., 2014; Tan et al., 2021).

![](/api/attachments/U9HSA6JF/fulltext/images/6da81b2a151050c093a38db2870c4179dc5cd0fcd16735932a7eaf0be14a8923.jpg)  
Figure 1. The process of endorsing a YouTube video on Twitter.

On 26 December 2017, we searched for new videos uploaded on YouTube for each hour of the day and retained the first 1,200 videos returned via YouTube API for each hour, resulting in a total of 28,800 sample videos. <sup>5</sup> For each sample video, video characteristics and corresponding tweets were collected daily from 26 December 2017 to 25 December 2018. Specifically, on YouTube, we collected data on videos (e.g., the number of views, likes, dislikes, comments, and the video category) and video providers (e.g., the number of subscribers, videos, channel views, and registration date). On Twitter, for each sample video, we queried Twitter API for the tweets that included the video link. Some videos were removed or made private by providers or YouTube during our observation period. After these videos were removed, our final dataset comprised 25,853 videos. Out of these videos, only 3,403 (13.16%) were tweeted on Twitter. A total of 43,054 tweets were collected, consisting of 18,483 original tweets and 24,571 retweets. For all endorsers, we also collected the lists of their followees and followers to construct their social networks on Twitter.

## 4.2 Key Variables and Summary Statistics

We aggregate data by week, considering the scarcity of daily tweets. Therefore, our main empirical analysis is at the video (i)–week (t) level. The dependent variable, content consumption, is measured using $ D v i e w s _ { i , t } ,$ the number of increased views of video i in week t. $O t w e e t s _ { i , t }$ and $R e t w e e t s _ { i , t } ,$ the number of original tweets and retweets containing video i’s YouTube link in week $t ,$ are used to measure original and reposted endorsements, respectively.

In terms of the endorsers’ network characteristics, we construct two variables for network size and two variables for tie strength. Otweets $\mathrm { \Delta } t i e s _ { i , t }$ and Retweets $\mathrm { \Delta } t i e s _ { i , t }$ are the average numbers of unique followers of original endorsers and reposting endorsers for video i in week $t ,$ respectively. At the social tie level, a reciprocal follower of an endorser is considered a strong tie to the endorser, while a nonreciprocal follower is regarded as a weak tie (Shi et al., 2014; Tan et al., 2021). As our analysis is at the video level, we use the percentage of strong-tie followers among all followers averaged across the endorsers to measure their tie strength. Specifically, Otweets\_tie\_strength<sub>i,t</sub> and Retweets\_tie\_strength<sub>i,t</sub> are the average percentages of reciprocal followers among all followers of original endorsers and reposting endorsers for video i in week t, respectively.<sup>6</sup>

Besides social endorsements, content consumption can be influenced by content characteristics, including popularity (Chen et al., 2011; Tucker and Zhang, 2011) and quality (Köcher and Köcher, 2018). We control for such influences using four time-varying video characteristics, $\mathit { V i e w s } _ { i , t } , L i k e s _ { i , t } , D i s l i k e s _ { i , t } ,$ and $C o m m e n t s _ { i , t } ,$ representing the numbers of views, likes, dislikes, and comments video i has received until week t, respectively. Moreover, we control for the following characteristics of the content provider (Khan and Vong, 2014):

CHcomments<sub>i,t</sub>, $C H \nu i e w s _ { i , t } ,$ and $C H s u b s c r i b e r s _ { i , t }$ measure the total numbers of comments, views, and subscribers received by the provider’s YouTube channel until week t, respectively. CHvideos<sub>i,t</sub> represents the total number of videos posted by the provider until week t. The channel age, $C H a g e _ { i , t } ,$ is the number of weeks since the provider registered on YouTube until week t.

Table 2 presents the summary statistics of the key variables. Given the skewness in the data, we log-transform the variables of $ D \nu i e w s _ { i , t } ,$ $\begin{array} { r } { O t w e e t s _ { i , t } , } \end{array}$ $R e t w e e t s _ { i , t } ,$ Otweets\_ $\mathrm { \it { t i e s i , t } } ,$ Retweets\_ $\mathbf { \Xi } _ { t i e s _ { i , t } . }$ $\mathit { V i e w s } _ { i , t } ,$ $L i k e s _ { i , t }$ $D i s l i k e s s _ { i , t } ,$ $C o m m e n t s _ { i , t } ,$ CHcomments<sub>i,t</sub>, $C H \nu i e w s _ { i , t } ,$ CHsubscribers<sub>i,t</sub>, and $C H \nu i d e o s _ { i , t }$ (Feng et al., 2014). The variable definition and correlation matrix are presented in Tables B1 and B2, respectively. Because several variables have correlations above 0.7 (Dormann et al., 2013), we test the extent of multicollinearity and address this concern in a robustness check.

Table 2. Summary statistics

<table><tr><td>Variables</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td colspan="5">Consumption for video i in week t</td></tr><tr><td> $Dviews_{i,t}$ </td><td>1,034</td><td>18,140</td><td>0</td><td>4,433,685</td></tr><tr><td colspan="5">Social endorsements for video i in week t</td></tr><tr><td> $Otweets_{i,t}$ </td><td>0.021</td><td>1.967</td><td>0</td><td>1,457</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.028</td><td>2.868</td><td>0</td><td>1,302</td></tr><tr><td> $Otweets\_ties_{i,t}$ </td><td>10,099</td><td>140,018</td><td>0</td><td>5,376,958</td></tr><tr><td> $Retweets\_ties_{i,t}$ </td><td>4,316</td><td>44,264</td><td>0</td><td>1,601,111</td></tr><tr><td> $Otweets\_tie\_strength_{i,t}$ </td><td>0.356</td><td>0.252</td><td>0</td><td>1</td></tr><tr><td> $Retweets\_tie\_strength_{i,t}$ </td><td>0.392</td><td>0.218</td><td>0</td><td>1</td></tr><tr><td colspan="5">Characteristics of video i until week t</td></tr><tr><td> $Views_{i,t}$ </td><td>44,979</td><td>402,700</td><td>0</td><td>40,087,480</td></tr><tr><td> $Likes_{i,t}$ </td><td>798</td><td>5,507</td><td>0</td><td>306,569</td></tr><tr><td> $Dislikes_{i,t}$ </td><td>40</td><td>343</td><td>0</td><td>28,430</td></tr><tr><td> $Comments_{i,t}$ </td><td>103</td><td>870</td><td>0</td><td>73,869</td></tr><tr><td colspan="5">Characteristics of video i&#x27;s provider until week t</td></tr><tr><td> $CHcomments_{i,t}$ </td><td>165</td><td>18,682</td><td>0</td><td>3,953,563</td></tr><tr><td> $CHviews_{i,t}$ </td><td>137,441</td><td>737,080</td><td>0</td><td>28,532,095</td></tr><tr><td> $CHsubscribers_{i,t}$ </td><td>245,638</td><td>1,079,316</td><td>0</td><td>42,031,464</td></tr><tr><td> $CHvideos_{i,t}$ </td><td>7,991</td><td>26,246</td><td>0</td><td>436,393</td></tr><tr><td> $CHage_{i,t}$ </td><td>234</td><td>153</td><td>1</td><td>702</td></tr></table>

Notes: The number of sample videos is 25,853. The number of observations is 880,856. S.D. stands for standard deviation.

## 5 Empirical Strategies and Results

## 5.1 Propensity Score Matching (PSM)

The videos in our research context can be classified into three categories: treated videos that are endorsed either via original tweets (tweet-endorsed videos), or through both original tweets and retweets (retweet-endorsed videos), and control videos that are not endorsed (notendorsed videos). In an ideal research design, videos would be randomly endorsed by users on Twitter so that the difference in consumption of not-endorsed videos, tweet-endorsed videos, and retweet-endorsed videos could be causally attributed to tweet and retweet endorsements. However, in reality, tweet-endorsed and retweet-endorsed videos may be systematically different from the not-endorsed videos. That is, users’ endorsement decisions may be driven by video or video provider characteristics, confounding their effect on content consumption. Following the common approach in the literature (Aral et al., 2009; Susarla et al., 2016), we adopt propensity score matching (PSM) to alleviate this endogeneity concern.

Because all sample videos were newly posted during our observation period, we first use the video characteristics (Category, Language, and Duration) and all channel characteristics (CHcomments, CHviews, CHsubscribers, CHvideos, and CHage) on 26 December 2017 as the matching variables (Susarla et al., 2016). Then we use multinomial logistic regression to calculate the likelihood of a video being tweet-endorsed and the likelihood of its being retweetendorsed (Aral et al., 2009). Next, we conduct one-to-three matching with replacement and a caliper of 0.15 standard deviations of the propensity score for tweet-endorsed videos and notendorsed videos based on the propensity score for being tweet-endorsed (i.e., receiving original tweets only) (Stuart, 2010). <sup>7</sup> This results in 2,339 tweet-endorsed videos and 5,061 notendorsed videos. We repeat this procedure to match retweet-endorsed videos with not-endorsed videos based on the propensity score for being retweet-endorsed (i.e., receiving both original tweets and retweets), which results in 1,019 retweet-endorsed videos and 2,463 not-endorsed videos. Table 3 reports the comparisons of summary statistics between the treatment and control videos before and after matching. As shown, all the significant differences in observable characteristics between the treatment (tweet-endorsed or retweet-endorsed) and control (notendorsed) videos become statistically nonsignificant after matching, with all standardized differences smaller than 0.10 (Austin, 2009).

Table 3. Balance test on the treatment and control groups

<table><tr><td rowspan="2">Variable</td><td>Unmatched</td><td colspan="2">Mean</td><td rowspan="2">Bias (%)</td><td rowspan="2">Bias reduction (%)</td><td rowspan="2">t-test</td></tr><tr><td>Matched</td><td>Treated</td><td>Control</td></tr><tr><td colspan="7">Tweet-endorsed videos vs. not-endorsed videos</td></tr><tr><td rowspan="2">Language</td><td>U</td><td>0.238</td><td>0.131</td><td>28</td><td rowspan="2">84.5</td><td>14.36***</td></tr><tr><td>M</td><td>0.235</td><td>0.252</td><td>-4.3</td><td>-1.33</td></tr><tr><td rowspan="2">Duration</td><td>U</td><td>27.304</td><td>30.427</td><td>-5.9</td><td rowspan="2">34.9</td><td>-2.71***</td></tr><tr><td>M</td><td>27.279</td><td>29.312</td><td>-3.8</td><td>-1.09</td></tr><tr><td rowspan="2">CHcomments</td><td>U</td><td>1.088</td><td>0.487</td><td>32.5</td><td rowspan="2">98.8</td><td>18.96***</td></tr><tr><td>M</td><td>1.072</td><td>1.065</td><td>0.4</td><td>0.11</td></tr><tr><td rowspan="2">CHviews</td><td>U</td><td>15.612</td><td>12.959</td><td>70.4</td><td rowspan="2">97.7</td><td>30.09***</td></tr><tr><td>M</td><td>15.591</td><td>15.531</td><td>1.6</td><td>0.63</td></tr><tr><td rowspan="2">CHsubscribers</td><td>U</td><td>9.517</td><td>6.826</td><td>66.6</td><td rowspan="2">96.3</td><td>29.72***</td></tr><tr><td>M</td><td>9.496</td><td>9.397</td><td>2.5</td><td>0.91</td></tr><tr><td rowspan="2">CHvideos</td><td>U</td><td>6.347</td><td>5.864</td><td>22.4</td><td rowspan="2">99.6</td><td>9.92***</td></tr><tr><td>M</td><td>6.345</td><td>6.344</td><td>0.1</td><td>0.03</td></tr><tr><td rowspan="2">CHage</td><td>U</td><td>223.120</td><td>166.200</td><td>36.6</td><td rowspan="2">92.7</td><td>17.16***</td></tr><tr><td>M</td><td>222.350</td><td>226.480</td><td>-2.7</td><td>-0.89</td></tr><tr><td colspan="7">Retweet-endorsed videos vs. not-endorsed videos</td></tr><tr><td rowspan="2">Language</td><td>U</td><td>0.189</td><td>0.131</td><td>15.9</td><td rowspan="2">85</td><td>5.39***</td></tr><tr><td>M</td><td>0.189</td><td>0.180</td><td>2.4</td><td>0.51</td></tr><tr><td rowspan="2">Duration</td><td>U</td><td>23.149</td><td>30.427</td><td>-14.3</td><td rowspan="2">83.2</td><td>-4.3***</td></tr><tr><td>M</td><td>23.149</td><td>24.374</td><td>-2.4</td><td>-0.54</td></tr><tr><td rowspan="2">CHcomments</td><td>U</td><td>1.146</td><td>0.487</td><td>36</td><td rowspan="2">92.9</td><td>14.69***</td></tr><tr><td>M</td><td>1.146</td><td>1.099</td><td>2.6</td><td>0.5</td></tr><tr><td rowspan="2">CHviews</td><td>U</td><td>15.781</td><td>12.959</td><td>76.8</td><td rowspan="2">94</td><td>21.56***</td></tr><tr><td>M</td><td>15.781</td><td>15.611</td><td>4.6</td><td>1.25</td></tr><tr><td rowspan="2">CHsubscribers</td><td>U</td><td>9.958</td><td>6.826</td><td>82.2</td><td rowspan="2">96.2</td><td>23.47***</td></tr><tr><td>M</td><td>9.958</td><td>9.839</td><td>3.1</td><td>0.83</td></tr><tr><td rowspan="2">CHvideos</td><td>U</td><td>6.203</td><td>5.864</td><td>15.8</td><td rowspan="2">64.4</td><td>4.7***</td></tr><tr><td>M</td><td>6.203</td><td>6.082</td><td>5.6</td><td>1.38</td></tr><tr><td rowspan="2">CHage</td><td>U</td><td>230.810</td><td>166.200</td><td>41.7</td><td rowspan="2">99.7</td><td>13.24***</td></tr><tr><td>M</td><td>230.810</td><td>230.620</td><td>0.1</td><td>0.03</td></tr></table>

Note: Category of videos is included as matching variables. CHcomments, CHviews, CHsubscribers<sub>,</sub> and CHvideos are transformed logarithmically.

$$
^ {* * *} p <   0. 0 1, ^ {* *} p <   0. 0 5, ^ {*} p <   0. 1.
$$

## 5.2 Control Function

Although PSM can alleviate the selection endogeneity concern based on observables, it does not account for the selection on unobservable confounding factors. For instance, endorsements received by a video may be affected by YouTube recommendation algorithms or social endorsements on other platforms. Following prior studies (Mallipeddi et al., 2021; Mulwa and Visser, 2020), we adopt the control function approach, also referred to as the twostage residual inclusion (2SRI) method, to alleviate such endogeneity concerns. In the first stage, we regress the endogenous variables $( O t w e e t s _ { i , t }$ and $R e t w e e t s _ { i , t } )$ on the instrumental variables (IVs) and covariates, revealing how original tweets and retweets are generated. In the second stage, the outcome variable $( D \nu i e w s _ { i , t + I } )$ is regressed on the endogenous variables, covariates, and the residuals of the first-stage regressions, which are included to account for the unobserved confounders (Wooldridge, 2015).

For the first-stage estimation, valid IVs should satisfy two conditions. First, IVs should be relevant to explaining the variation in the endogenous variables (relevance). Second, IVs should not affect the outcome other than through the endogenous variables (exclusion restriction). In our estimation, we use the number of original (OppOtweets<sub>i,t</sub>) or reposted endorsements $( O p p R e t w e e t s _ { i , t } )$ of competing videos released in the same week as the IV for the original and reposted endorsements of the focal video, respectively. This approach is consistent with prior literature (Germann et al., 2015; Mallipeddi et al., 2021), which suggests that actions of competing units can partially explain the variation in the endogenous actions of a focal unit. In our research context, videos released in the same week target a shared audience and thus compete for user attention on social media. As a result, higher levels of original or reposted endorsements for competing videos in a given week may crowd out attention and reduce the volume of similar endorsement activity for the focal video. Consequently, the number of original or reposted endorsements of competing videos in the same week serve as plausible and relevant instruments for the original and reposted endorsements of the focal video, respectively. This relevance condition is also validated empirically by the first-stage regression results reported in Table D3 of Appendix D.

Regarding the exclusion restriction condition, we argue that the endorsements of competing videos in the same week are unlikely to affect the consumption of the focal video in the subsequent week directly. That is, the IVs, OppOtweets<sub>i,t</sub> and OppRetweets<sub>i,t</sub>, affect Dviews<sub>i,t+1</sub> only via affecting endorsements of the focal video $( O t w e e t s _ { i , t }$ and Retweets<sub>i,t</sub>). One potential concern is that increased endorsements of competing videos could raise their own consumption, thereby reducing consumption of the focal video. However, we believe that this indirect channel is unlikely to pose a significant threat to identification for several reasons. First, compared with social endorsements such as tweeting or retweeting, which reflect effortful and deliberate user behavior, video consumption requires substantially less effort and cognitive discretion. Second, users frequently consume multiple videos in a single session, particularly in digital environments characterized by algorithmic content delivery and infinitescroll interfaces designed to promote continuous engagement. This binge-like viewing behavior reduces the likelihood of direct competition between videos for user attention within short timeframes. Thus, even if competing videos attract more viewers due to higher endorsement activities, this is unlikely to suppress the consumption of the focal video substantially. Thus, the exclusion restriction condition is plausibly satisfied.

Although the exclusion restriction condition cannot be tested formally due to unobserved true error, we conduct an informal test following Mallipeddi et al. (2021) and Bichescu and Hilafu (2023). Specifically, we check the statistical relationship between the $\mathrm { I V s } \ : ( O p p O t w e e t s _ { i , i }$ and $O p p R e t w e e t s _ { i , t } )$ and the outcome $( D \nu i e w s _ { i , t + I } )$ after controlling for the endogenous variables. Table D1 reports insignificant coefficients of the IVs, suggesting no direct relationship between the IVs and the outcome. Additionally, we conduct a falsification test based on a subsample to assess the validity of the exclusion restriction. If an IV does not affect the endogenous regressor in a specific subsample, then any estimated association between the IV and the outcome in that subsample would indicate a violation of the exclusion restriction (Kang et al., 2013; Labrecque and Swanson, 2018). To test this, we estimate the effects of $O p p O t w e e t s _ { i , t }$ and $O p p R e t w e e t s _ { i , t }$ on $\_ D v i e w s _ { i , t + I }$ using a subsample of videos from low Twitterpenetration countries and without social endorsements. The procedure is detailed in Appendix D. Table D2 reports insignificant coefficients of $O p p O t w e e t s _ { i , t }$ and $O p p R e t w e e t s _ { i , t } ,$ supporting the exclusion restriction.

The first-stage estimations using original and reposted endorsements as dependent variables are shown in the equations

$$
O t w e e t s _ {i, t} = \beta_ {1 0} + \beta_ {1 1} O p p O t w e e t s _ {i, t} + \gamma_ {1 2} X _ {i, t - 1} + \alpha_ {1 i} + \tau_ {1 t} + \epsilon_ {1, i, t},\tag{1}
$$

$$
R e t w e e t s _ {i, t} = \beta_ {2 0} + \beta_ {2 1} O p p R e t w e e t s _ {i, t} + \beta_ {2 2} O t w e e t s _ {i, t} + \beta_ {2 3} O t w e e t s _ {i, t} *
$$

$$
O t w e e t s \_ t i e \_ s t r e n g t h _ {i, t} + \beta_ {2 4} O t w e e t s _ {i, t} * O t w e e t s \_ t i e s _ {i, t} + \gamma_ {2 5} X _ {i, t - 1} +
$$

$$
\alpha_ {2 i} + \tau_ {2 t} + \epsilon_ {2, i, t},\tag{2}
$$

where $O p p O t w e e t s _ { i , t }$ and $O p p R e t w e e t s _ { i , t }$ denote the number of original tweets and retweets of other videos released on the same day in week $t ,$ respectively. For both equations, we control for $X _ { i , t - l , }$ a set of time-varying video and channel characteristics as listed in Table 2. We also include video fixed effects (?) to account for video heterogeneity and week dummies (?) for time fixed effects. $\epsilon _ { 1 , i , t }$ and $\epsilon _ { 2 , i , t }$ are the error terms. For equation (2), $O t w e e t s _ { i , t } ,$ and its interactions with Otweets\_ $\_ t i e s _ { i , t }$ and Otweets\_tie\_strength<sub>i,t</sub> are included to control for the number of original endorsements and the original endorsers’ network characteristics.

Then, the residuals from equations (1) and $( 2 ) , \hat { \epsilon } _ { 1 , i , t }$ and $\hat { \epsilon } _ { 2 , i , t }$ , are included in the secondstage estimation,

$$
\begin{array}{r} D v i e w s _ {i, t + 1} = \beta_ {0} + \beta_ {1} O t w e e t s _ {i, t} + \beta_ {2} R e t w e e t s _ {i, t} + \gamma X _ {i, t} + \alpha_ {i} + \tau_ {t + 1} + \\ \rho_ {1} \hat {\epsilon} _ {1, i, t} + \rho_ {2} \hat {\epsilon} _ {2, i, t} + \epsilon_ {i, t + 1}, \end{array}\tag{3}
$$

where $\_ D v i e w s _ { i , t + I }$ is the number of increased views for video i in week t+1. Lagged independent and control variables are used to alleviate reverse causality (Mallipeddi et al. 2021; Park et al. 2018; Rui et al. 2013). To test the moderating effect of the endorsers’ network size, we add two interaction terms of Otweets<sub>i,t</sub> \* Otweets $\mathrm { \Delta } t i e s _ { i , t }$ and Retweets<sub>i,t</sub> \* Retweets $\mathbf { \xi } _ { t i e s _ { i , t } }$ to equation (3). For the moderating effect of the endorsers’ tie strength, interaction terms of $O t w e e t s _ { i , t }$ \* Otweets\_tie\_strength<sub>i,t</sub> and Retweets<sub>i,t</sub> \* Retweets\_tie\_strength<sub>i,t</sub> are added to equation (3).<sup>8</sup>

## 5.3 Main Results

Table D3 presents the results of the first-stage regressions based on the matched sample.

The negative coefficients of OppOtweets<sub>i,t</sub> and OppRetweets<sub>i,t</sub> suggest that social endorsements for competing videos reduce the number of social endorsements for the focal video. In column (2), the coefficient of Otweets<sub>i,t</sub> \* Otweets\_ $\mathrm { \Delta } t i e s _ { i , t }$ is positive and statistically significant, suggesting that the effect of original endorsements on reposted endorsements is positively moderated by the network size. The coefficient of Otweets<sub>i,t</sub> \*Otweets\_tie\_strength<sub>i,t</sub> is significantly negative, suggesting that original endorsements lead to more reposted endorsements when the original endorsers have weaker tie strength.

Table 4. Effects of original and reposted endorsements on content consumption

<table><tr><td rowspan="2"></td><td colspan="4"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Ottweets_{i,t}$ </td><td>0.361***(0.074)</td><td>0.323***(0.067)</td><td>0.341***(0.115)</td><td>0.383***(0.089)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.233**(0.091)</td><td>-0.096(0.086)</td><td>0.337***(0.124)</td><td>-0.069(0.112)</td></tr><tr><td> $Ottweets_{i,t} * Ottweets\_ties_{i,t}$ </td><td></td><td>0.024***(0.007)</td><td></td><td>0.025***(0.007)</td></tr><tr><td> $Retweets_{i,t} * Retweets\_ties_{i,t}$ </td><td></td><td>0.046***(0.009)</td><td></td><td>0.047***(0.009)</td></tr><tr><td> $Ottweets_{i,t} * Ottweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>0.032(0.111)</td><td>-0.088(0.101)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-0.228*(0.121)</td><td>-0.197*(0.119)</td></tr><tr><td> $Residual(Otweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $Residual(Retweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td><td>345,021</td><td>345,021</td></tr><tr><td> $R^2$ </td><td>0.5356</td><td>0.5357</td><td>0.5356</td><td>0.5358</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time fixed effects. \*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

Table 4 shows the second-stage results based on the matched sample. Column (1) reports the baseline without interaction effects. Models in columns (2) and (3) with interaction terms examine how the effects of social endorsements are contingent on the endorsers’ network size and tie strength, respectively. Both moderating effects are included in the estimation of column (4). The estimated coefficients of Otweets<sub>i,t</sub> are consistently positive and statistically significant, suggesting that original tweets increase video consumption significantly. However, the coefficients of Retweets<sub>i,t</sub> become nonsignificant after the interaction terms of network size are added, indicating that retweets on the average do not significantly increase content consumption. Instead, their effects are contingent on network size. As such, original endorsements increase content consumption more than reposted endorsements, supporting H1.

We find a significant and positive moderating effect of the endorsers’ network size on the effect of original tweets, as shown by the consistently positive and significant coefficients of Otweets<sub>i,t</sub> \* Otweets\_ties<sub>i,t</sub>. Therefore, original endorsements increase content consumption more when the original endorsers have more followers, supporting H2a. Similarly, the coefficients of Retweets<sub>i,t</sub> \* Retweets\_ $t i e s _ { i , t }$ are also positive and statistically significant, suggesting a positive moderating effect of the endorsers’ network size on the endorsement effect of retweets, supporting H2b. The coefficients of Retweets<sub>i,t</sub> \*Retweets\_ties<sub>i,t</sub> are significantly larger than those of Otweets<sub>i,t</sub> \* Otweets\_ $t i e s _ { i , t }$ , indicating that the effect of reposted endorsements on content consumption depends more on the endorsers’ network size. Given the nonsignificant effect of retweets in column (4), we plot its marginal effect to better illustrate how the impact of retweets changes with the number of followers. As shown in Figure 2a, reposted endorsements significantly increase content consumption only when the average number of unique followers of the reposting endorsers exceeds 402 (6 after log transformation).

![](/api/attachments/U9HSA6JF/fulltext/images/efa983a78bb925cd65fb720c599cd43d4ccf8c6d25731f21f6ae4ef9749d7984.jpg)

![](/api/attachments/U9HSA6JF/fulltext/images/5011fe9916be7d5b691fe56889269de78909c56bf2947c192bfd27214fbf3ac8.jpg)  
Figure 2. Marginal effects of reposted endorsements on content consumption.

Regarding the moderating effect of tie strength, the nonsignificant coefficients of Otweets<sub>i,t</sub> \* Otweets\_tie\_strength<sub>i,t</sub> suggest that the effect of original endorsements on content consumption does not depend on the original endorsers’ tie strength. Therefore, H3a is not supported. A plausible explanation for this lies in the substantial heterogeneity in the quality of original endorsement messages. While original endorsements are generally expected to contain personalized reasoning and richer information content, this is not always the case in practice. Some original endorsements may be poorly crafted—with limited cognitive efforts, weak reasoning, or unconvincing logic. When strong ties engage in the central-route processing, as suggested by the ELM, these low-quality messages may be scrutinized more carefully and followers may become less persuaded, or even skeptical, about the endorsed content. Unlike peripheral-route processing, where surface-level cues may suffice, central-route processing amplifies the impact of message quality, making weak or flawed original messages more salient and potentially counterproductive. As a result, the anticipated positive moderating effect of the endorsers’ tie strength is likely neutralized by the presence of weak or inconsistent message quality across original endorsements. In contrast, the coefficients of Retweets<sub>i,t</sub> \*

Retweets $t i e \_ s t r e n g t h _ { i , t }$ are significantly negative, indicating that the effect of reposted endorsements on content consumption decreases as the reposting endorsers’ tie strength increases, supporting H3b. As illustrated in Figure 2b, reposted endorsements have a significant positive effect on content consumption only when the repositing endorsers have below 30 percentage of strong ties among all followers.

## 5.4 Robustness Checks

Alternative IVs. In the main analysis, we use the number of original tweets of the competing videos $( O p p O t w e e t s _ { i , t } )$ as the IV for the number of original tweets of the focal video $( O t w e e t s _ { i , t } )$ . Similarly, $O p p R e t w e e t s _ { i , t }$ is used as the IV for $R e t w e e t s _ { i , t }$ . To ensure that our results are robust, we extend our analysis using three alternative sets of IV. First, we use both $O p p O t w e e t s _ { i , t }$ and $O p p R e t w e e t s _ { i , t }$ as the IVs for $O t w e e t s _ { i , t } ,$ as the competing videos endorsements including both original tweets and retweets could deviate the audience’s attention for the focal video. Similarly, these two variables are also used as IVs for $R e t w e e t s _ { i , t } .$ Second, instead of using the total number of social endorsements of competing videos, we use their average number of original tweets $( A \nu e O p p O t w e e t s _ { i , t } )$ as the IV for $O t w e e t s _ { i , t } ,$ , and average number of retweets $( A \nu e O p p R e t w e e t s _ { i , t } )$ as the IV for $R e t w e e t s _ { i , t }$ . Third, $A \nu e O p p O t w e e t s _ { i , t }$ and $A \nu e O p p R e t w e e t s _ { i , t }$ are both used as IVs for $O t w e e t s _ { i , t }$ and $R e t w e e t s _ { i , t } .$ All results are presented in Table E1 of Appendix E and demonstrate the robustness of our findings.

Self-Endorsements. Social endorsements by video providers can be generated differently from those by viewers and have different impacts on video consumption. Therefore, we identify and remove self-endorsements by video providers in our estimations. Specifically, for our sample video providers, we first collect Twitter links and corresponding Twitter accounts they posted on their YouTube channel homepages. Then we compare these Twitter accounts with those of the video endorsers to identify the providers’ self-endorsements. Out of all 16,718 video providers in our dataset, 3,063 (18.32%) providers posted their Twitter accounts on their YouTube homepages. Following this approach, among the 43,054 endorsements, only 47 (0.11%) endorsements, comprising 36 original endorsements and 11 reposted endorsements, were identified to be posted by video providers. Finally, we re-estimate our models by removing these self-endorsements. The results in Table E2 provide consistent findings.

Confounding Factors in Retweets. The total number of previous retweets may influence current retweet behavior and potentially confound the effect of retweets on video consumption. Additionally, the original endorsers’ past activities—such as favoriting, tweeting, and groupjoining—reflecting their general engagement level and network prominence could also bias the estimated effect of retweets. To address these concerns, we construct four variables—the number of tweets favorited by the original endorsers (Oendorser\_favorites<sub>i,t</sub>), the number of tweets and retweets posted by the original endorsers (Oendorser $p o s t s _ { i , t } )$ , the number of social groups (lists) endorsers belong as members (Oendorser\_ $\mathbf { \xi } _ { l i s t s _ { i , t } ) }$ , and total number of previous retweets for the video $( P r i o r R e t w e e t s _ { i , t } )$ —and incorporate them as additional controls in the analyses. As shown in Table E3, the results are consistent with our main findings.

Potential Measurement Error of Tie Strength. Reciprocal following reflects only a basic form of social connection and may underestimate actual tie strength by omitting other types of user interactions. If our measure systematically underestimates tie strength for some endorsers (e.g., endorsers with more weak ties) but not others, that may cause the nonsignificant moderating effect of Otweets\_tie\_strength<sub>i,t</sub> and the significant negative moderating effect of Retweets\_tie\_strength<sub>i,t</sub>. To evaluate this concern, we conduct a sensitivity analysis following prior studies (Kannan et al., 2025). Specifically, we artificially inflate Otweets\_tie\_strength<sub>i,t</sub> and Retweets\_tie\_strength<sub>i,t</sub> for endorsers with more weak ties (i.e., below the sample median) in 2-percentage-point increments. As shown in Figure E1(a), for original endorsements, the moderating effect of Otweets\_tie\_strength<sub>i,t</sub> remains consistently nonsignificant even when tie strength is increased by up to 12%. In contrast, Figure E1(b) shows that, for reposted endorsements, the moderating effect of Retweets\_tie\_strength<sub>i,t</sub> becomes statistically nonsignificant only when tie strength is systematically underestimated by 12% or more. Notably, the sample mean of Retweets\_tie\_strength<sub>i,t</sub> at a 12% inflation reaches 0.424, which is substantially higher than empirical estimates of reciprocal ties on Twitter in prior studies (Kwak et al., 2010; Shi et al., 2014). A measurement error of such magnitude is unlikely, and our results thus appear robust to potential mismeasurement of tie strength.

Multicollinearity. Several independent variables are highly correlated (see Table B2 of Appendix B), suggesting that multicollinearity can be a concern. To check the extent of multicollinearity, we first calculate variance inflation factors (VIFs) for all variables, as shown in Table E4, and only the VIF for $R e t w e e t s _ { i , t }$ is above the commonly used threshold of 10 for multicollinearity (Figueiredo and Silverman, 2012). Second, we calculate the condition number, the square root of the ratio of the largest and smallest eigenvalues, of the data matrix X’X, where X consists of main variables with high correlation in our estimation. The condition number for this data matrix is 9.06, well below the recommended cutoff of 30 (Kennedy, 2003), suggesting that multicollinearity is not a serious concern. Nonetheless, we normalize all the key variables before creating the interaction variables, to mitigate the potential multicollinearity concern (Lim and McCann, 2014). The results in Table E5 are qualitatively the same as those in Table 4.

Outliers. We employ two methods to deal with outliers (e.g., viral videos) that deviate significantly from other observations in our dataset. First, we apply winsorizing, a common method of minimizing the influence of outliers by setting outliers to a specific percentile of the data (Kwak and Kim, 2017). Specifically, we winsorize all key variables at the 99th percentiles of our data points and re-estimate our models using the winsorized data. Besides the 99th percentiles, we also use three times the standard deviation above the mean as the threshold to identify outliers. All results reported in Table E6 and E7 remain consistent with the main results. Second, we remove the outliers above 95 percentiles of data points. The consistent results are shown in Table E8.

Alternative Models. First, instead of a fixed effects model, we estimate a random effects model to control for unobserved video heterogeneity across different categories. The results reported in Table E9 are consistent with those of fixed effects estimation. Second, instead of using log transformation to deal with overdispersion, we employ a negative binomial model, a generalization of a Poisson regression model that allows for overdispersion by incorporating an individual unobserved effect into the conditional mean (Hausman et al., 1984). The negative binomial estimations provide generally consistent results, as shown in Table E10.

## 6 Additional Results

## 6.1 Moderating Effects of Endorsement Message Characteristics

On social platforms, original endorsements elucidate the opinions of original endorsers about the content, showcasing the endorsers’ knowledge and skills (Oeldorf-Hirsch and Sundar, 2015). From this perspective, original endorsements with messages demonstrating higher cognitive effort may have a stronger effect on content consumption. In contrast, as suggested by the negative moderating effect of reposting endorsers’ tie strength (H3b), reposting endorsers primarily serve as information intermediaries and attribute the opinions to the original endorsers (Shi et al., 2014). Especially in our context, 97.27% of reposted endorsements are retweets that simply repost original tweets without any modification or addition. Therefore, we expect the endorsement message characteristics to be more important for original endorsements than for reposted endorsements.

To test this difference, we first measure original endorsers’ efforts demonstrated by the endorsement message length, Otweets\_ $\mathbf { \xi } _ { l e n _ { i , t } }$ and Retweets\_ $\mathbf { \xi } _ { l e n _ { i , t } , \ }$ the average lengths of original and reposted endorsements for video i in week $t ,$ respectively. Second, leveraging the 2022 version of Linguistic Inquiry and Word Count (LIWC; Pennebaker et al., 2015), we derive Otweets\_ $i n s i g h t _ { i , t }$ and Retweets\_ $i n s i g h t _ { i , t } ,$ , the average percentage of insight words (e.g., realize, know, how, think, feel) in original and reposted endorsements for video i in week $t ,$ to reflect original endorsers’ active cognitive processes (Abe, 2009).

Table 5 presents the results with the two endorsement message characteristics added as moderators for the endorsement effects. As shown, the length and insight words of original endorsements moderate the effect of original endorsements on content consumption positively, suggesting that original endorsements demonstrating higher effort are more effective. For reposted endorsements, the moderating effects of message length and insight words are both nonsignificant, confirming that the effect of reposted endorsements does not depend on the endorsement message composed by the original endorsers.

Table 5. Moderating effects of endorsement message characteristics

<table><tr><td rowspan="2"></td><td colspan="2"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td></tr><tr><td> $Otwerts_{i,t}$ </td><td>0.229***(0.089)</td><td>0.335***(0.072)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.248*(0.128)</td><td>0.221**(0.089)</td></tr><tr><td> $Otwerts_{i,t}*Otweets\_len_{i,t}$ </td><td>0.002**(0.001)</td><td></td></tr><tr><td> $Retweets_{i,t}*Retweets\_len_{i,t}$ </td><td>-0.0004(0.001)</td><td></td></tr><tr><td> $Otwerts_{i,t}*Otweets\_insight_{i,t}$ </td><td></td><td>0.040***(0.012)</td></tr><tr><td> $Retweets_{i,t}*Retweets\_insight_{i,t}$ </td><td></td><td>0.003(0.013)</td></tr><tr><td>Residual( $Otwerts_{i,t}$ )</td><td>Yes</td><td>Yes</td></tr><tr><td>Residual( $Retweets_{i,t}$ )</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td></tr><tr><td> $R^2$ </td><td>0.5356</td><td>0.5356</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time-fixed effects.  
\*\*\* $p < 0 . 0 1 , ^ { * * } p < 0 . 0 5 , ^ { * } p < 0 . 1 .$

## 6.2 Moderating Effects of Content Characteristics

Examining the moderating effects of content characteristics can also reveal how the two types of social endorsements affect content consumption differently. The results can demonstrate how the information cues provided by the content platform interact with the social cues of the endorsement on the social platform. We measure content characteristics in terms of prior viewership $( V i e w s _ { i , t } )$ , comments $( C o m m e n t s _ { i , t } )$ , and likes and dislikes $( R a t e s _ { i , t } )$ . All of these information cues, derived from the content platform, indicate the level of prior user engagement for the content. Table 6 consistently suggests significantly positive moderating effects of prior consumption, comments, and rates on the impact of original endorsements. In contrast, all the coefficients of interaction terms for reposted endorsements are negative and significant. Therefore, we conclude that original endorsements have a larger effect on content with higher user engagement, while reposted endorsements are more effective for content with lower user engagement.

Table 6. Moderating effects of content characteristics

<table><tr><td rowspan="2"></td><td colspan="3"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td> $Otwerts_{i,t} * Views_{i,t}$ </td><td>0.086***(0.012)</td><td></td><td></td></tr><tr><td> $Retweets_{i,t} * Views_{i,t}$ </td><td>-0.026**(0.011)</td><td></td><td></td></tr><tr><td> $Otwerts_{i,t} * Comments_{i,t}$ </td><td></td><td>0.028**(0.012)</td><td></td></tr><tr><td> $Retweets_{i,t} * Comments_{i,t}$ </td><td></td><td>-0.023**(0.010)</td><td></td></tr><tr><td> $Otwerts_{i,t} * Rates_{i,t}$ </td><td></td><td></td><td>0.044***(0.011)</td></tr><tr><td> $Retweets_{i,t} * Rates_{i,t}$ </td><td></td><td></td><td>-0.027***(0.010)</td></tr><tr><td> $Otwerts_{i,t}$ </td><td>-0.741***(0.162)</td><td>0.208**(0.093)</td><td>0.212**(0.096)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.604***(0.159)</td><td>0.335***(0.106)</td><td>0.353***(0.115)</td></tr><tr><td>Residual( $Otwerts_{i,t}$ )</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Residual( $Retweets_{i,t}$ )</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td><td>345,021</td></tr><tr><td> $R^2$ </td><td>0.5361</td><td>0.5356</td><td>0.5344</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time-fixed effects.  
\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

## 7 Conclusions and Implications

To summarize, we studied the differences between original and reposted endorsements by investigating their effects on content consumption and the moderating effects of the endorsers’ network characteristics. We find a significantly positive effect of original endorsements on content consumption, which is positively moderated by the endorsers’ network size but not by the tie strength between endorsers and their followers. In contrast, reposted endorsements increase content consumption only when the endorsers have a large number of followers or a high percentage of weak ties among their followers. Furthermore, the endorsement message characteristics significantly moderate the effect of original endorsements but not that of reposted endorsements. Specifically, original endorsements with messages demonstrating higher cognitive effort increase content consumption more. Additionally, the effect of original endorsements is stronger for content with higher prior user engagement, whereas reposted endorsements have a greater impact on content with lower prior user engagement.

## 7.1 Theoretical Contribution

Our study makes several important theoretical contributions. First, our work contributes to the extensive literature on online WOM by studying a different form of online WOM, social endorsements. Existing studies focus on online reviews/rating, exploring topics such as the production of online reviews (Wang et al. 2019), the improvement of the online review ecosystem (Kokkodis et al., 2022), network factors influencing rating convergence (Lin and Wang, 2018), and the effects of online reviews on product/service strategies (Sun and Xu 2018; Zhao et al. 2022) and consumer decisions (Ba et al., 2020; Lei et al., 2022). Unlike online reviews and ratings, social endorsements leverage social ties for information diffusion and social influence. Importantly, our study reveals that tie strength moderates the effectiveness of original and reposted endorsements differently.

Second, we add to the literature on marketer-generated or sponsored endorsements (Gong et al., 2017; Park et al., 2021; Sun et al., 2020) by studying organic social endorsements. More importantly, we differentiate original and reposted endorsements and examine their differences in affecting content consumption. Specifically, our results generalize the positive effect of marketer-generated tweets on content consumption studied by Gong et al. (2017) to usergenerated original tweets. Adding to Gong et al. (2017), who show that the effect of influential retweets are effective only when the original tweets are informative, we find that the effectiveness of retweets depends on the endorsers’ network size and tie strength.

Third, prior research on the value of social networks in product promotion (Gao et al. 2020), open innovation (Billington and Davidson, 2013), new product development (Sosa, 2014), information evaluation (Yan et al., 2019), knowledge generation (Jin et al., 2022; Wei et al., 2021), and product/content consumption (Gong et al., 2017; Rui et al., 2013) typically studies either network size or tie strength, but rarely both. While some studies suggest the positive moderating role of network size (Gong et al., 2017; Rui et al., 2013), others find that endorsements from micro-influencers are more effective than those from mega-influencers (Park et al. 2021). These mixed findings may stem from the confounding role of tie strength. We add to this stream of literature by jointly considering network size and tie strength to examine the moderating role of follower networks in endorsement effects, offering a more accurate understanding of the endorsers’ influence. Moreover, we enrich the understanding of how weak and strong ties shape information processing by examining their complementary roles in different types of endorsements. Our results demonstrate that weak ties tend to induce peripheral-route processing, making reposted endorsements—which serve as heuristic cues— more influential. In contrast, strong ties are more likely to elicit central-route processing, making original endorsements—which contain richer content and personalized reasoning— more persuasive.

Fourth, our research extends the growing literature that examines how various functions of online social platforms address managerial problems, such as information-revealing (Qiu and Whinston, 2017), live-chat (Sun et al. 2021), message propagation (Gopal et al., 2016), information disclosure (Guan et al., 2020; Rong et al., 2022), and responding to customer reviews (Gu and Ye, 2014). Examining the function of social sharing, we demonstrate how original and reposted sharing perform differently according to content and endorsement message characteristics. Extending prior studies that revealed that the endorsement effect varies according to seller reputation (Sun et al. 2020), product type (Li and Wu, 2018; Park et al., 2021), or content source (Messing and Westwood, 2014), our results suggest that the endorsement effect depends on prior user engagement with the endorsed content. While original endorsements are more effective for content with higher user engagement, reposted endorsements are more effective for content with lower user engagement. In line with prior research showing that more informative endorsement messages have stronger effects (Gong et al., 2017; John et al., 2017), we also find that original endorsements are more effective when the endorsement messages demonstrate more cognitive efforts invested by endorsers. However, these message characteristics become less important once endorsements are reposted.

## 7.2 Practical Implications

Our findings provide two sets of implications for social platforms. First, our findings show that collaboration with content platforms (e.g., YouTube) can be beneficial, because endorsing cross-platform content can encourage user engagement through reposting the endorsements and consuming the endorsed content. Second, differently than original endorsements, reposted endorsements engage users mainly through weak ties for content consumption, supporting social platforms’ concern that reposting may jeopardize the authenticity of social interactions and the depth of user engagement. Therefore, enabling reposting is beneficial for social platforms aiming to facilitate information diffusion and discovery but may not serve those aiming to foster strong social connections.

For businesses leveraging social media marketing, our results suggest that they should prioritize facilitating and encouraging original endorsements by actively engaging audience in meaningful conversations on social platforms. While reposting original endorsements can be encouraged, its effectiveness should not be overstated. To harness the benefits of reposted endorsements, businesses should engage active influentials with a large number of followers. Collaborating with OSNs to leverage granular data on users’ tie strength with their followers can help target certain audiences on platforms like Twitter. For example, businesses may invite influentials with a high percentage of weak ties to retweet endorsement message by directly addressing original tweets to them (e.g., using the “@” function on Twitter). In addition, different strategies can be taken according to content characteristics. For highly engaging content, encouraging original endorsements is more effective, whereas for less engaging content, activating reposted endorsements may be more rewarding.

Finally, endorsement message recipients can signal high cognitive involvement with the content by crafting original endorsements that use longer messages and more insightful words. For users with a large number of followers or mostly weak ties, reposting the received endorsements can spread the content information effectively.

## 7.3 Limitations and Future Research

There are several limitations of our study, which also provide opportunities for future research. First, as Twitter exemplifies a social platform characterized by network-centric algorithms, information diffusion norms, and text-based interactions, our findings may be generalized to other platforms with similar characteristics, such as Weibo and Reddit. However, caution should be exercised when applying these findings to platforms driven by contentcentric algorithms or community-building norms. Future research could extend our work by examining how the effect of original and reposted endorsements varies across platforms with different structural and interactional affordances. Second, while reciprocal following is a widely used proxy for tie strength in prior studies (e.g., Shi et al., 2014; Tan et al., 2021), it provides only a coarse-grained measure. Future research can examine alternative measures using prior message exchanges or engagement history. Third, we account for YouTube providers’ self-endorsements only if they posted their Twitter accounts on their YouTube homepage, which may not fully address the self-endorsement issue in our dataset.

## References

Abe, J. A. A. (2009). Words that predict outstanding performance. Journal of Research in Personality, 43(3), 528–531.

Alatas, V., Chandrasekhar, A. G., Mobius, M., Olken, B. A., and Paladines, C. (2020). Celebrities and public health campaigns: A nationwide Twitter experiment promoting vaccination in Indonesia. https://economics.mit.edu/files/16501

Aral, S. (2016). The future of weak ties. American Journal of Sociology, 121(6), 1931–1939.

Aral, S., Dellarocas, C., and Godes, D. (2013). Social media and business transformation: A framework for research. Information Systems Research, 24(1), 3–13.

Aral, S., Muchnik, L., and Sundararajan, A. (2009). Distinguishing influence-based contagion from homophily-driven diffusion in dynamic networks. Proceedings of the National Academy of Sciences, 106(51), 21544–21549.

Aral, S., and Walker, D. (2011). Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Science, 57(9), 1623–1639.

Aral, S., and Walker, D. (2012). Identifying influential and susceptible members of social networks. Science, 337(6092), 337–341.

Aral, S., and Walker, D. (2014). Tie strength, embeddedness, and social influence: A largescale networked experiment. Management Science, 60(6), 1352–1370.

Austin, P. C. (2009). Balance diagnostics for comparing the distribution of baseline covariates between treatment groups in propensity-score matched samples. Statistics in Medicine, 28(25), 3083–3107.

Ba, S., Jin, Y., Li, X., and Lu, X. (2020). One size fits all? The differential impact of online reviews and coupons. Production and Operations Management, 29(10), 2403–2424.

Bichescu, B., and Hilafu, H. (2023). Effects of hospital-acquired conditions on readmission risk: The mediating role of length of stay. Manufacturing and Service Operations Management, 25(4), 1603–1621.

Billington, C., and Davidson, R. (2013). Leveraging open innovation using intermediary networks. Production and Operations Management, 22(6), 1464–1477.

Bond, R. M., Fariss, C. J., Jones, J. J., Kramer, A. D. I., Marlow, C., Settle, J. E., and Fowler, J. H. (2012). A 61-million-person experiment in social influence and political mobilization. Nature, 489(7415), 295–298.

Burke, M. (2011). Reading, writing, relationships: The impact of social network sites on relationships and well-being. Carnegie Mellon University.

Chen, H., De, P., and Hu, Y. J. (2015). It-enabled broadcasting in social media: An empirical study of artists’ activities and music sales. Information Systems Research, 26(3), 513–531.

Chen, J., and Guo, Z. (2022). New-media advertising and retail platform openness. MIS Quarterly, 46(1), 431–456.

Chen, Y., Wang, Q., and Xie, J. (2011). Online social interactions: A natural experiment on word of mouth versus observational learning. Journal of Marketing Research, 48(2), 238– 254.

Dormann, C. F., Elith, J., Bacher, S., Buchmann, C., Carl, G., Carré, G., Marquéz, J. R. G., Gruber, B., Lafourcade, B., Leitão, P. J., Münkemüller, T., McClean, C., Osborne, P. E., Reineking, B., Schröder, B., Skidmore, A. K., Zurell, D., and Lautenbach, S. (2013). Collinearity: A review of methods to deal with it and a simulation study evaluating their performance. Ecography, 36(1), 27–46.

Duan, W., Gu, B., and Whinston, A. B. (2008). Do online reviews matter? — An empirical investigation of panel data. Decision Support Systems, 45(4), 1007–1016.

Feng, C., Wang, H., Lu, N., Chen, T., He, H., Lu, Y., and Tu, X. M. (2014). Log-transformation and its implications for data analysis. Shanghai Archives of Psychiatry, 26(2), 105–109.

Figueiredo, J. M. de, and Silverman, B. S. (2012). Firm survival and industry evolution in vertically related populations. Management Science, 58(9), 1632–1650.

Firdaus, S. N., Ding, C., and Sadeghian, A. (2018). Retweet: A information diffusion mechanism – A survey paper. Online Social Networks and Media, 6, 26–40.

Gao, H., Zhao, H., Tan, Y. (Ricky), Lin, Y. (Lisa), and Wei, L. (2020). Social promotion: A creative promotional framework on consumers’ social network value. Production and Operations Management, 29(12), 2661–2678.

Germann, F., Ebbes, P., and Grewal, R. (2015). The chief marketing officer matters! Journal of Marketing, 79(3), 1–22.

Goh, K.-Y., Heng, C.-S., and Lin, Z. (2013). Social media brand community and consumer behavior: Quantifying the relative impact of user- and marketer-generated content. Information Systems Research, 24(1), 88–107.

Gong, S., Zhang, J., Zhao, P., and Jiang, X. (2017). Tweeting as a marketing tool: A field experiment in the TV industry. Journal of Marketing Research, 54(6), 833–850.

Gopal, R., Hidaji, H., Patterson, R. A., Rolland, E., and Zhdanov, D. (2016). Design improvements for message propagation in malleable social networks. Production and Operations Management, 25(6), 993–1005.

Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360–1380.

Granovetter, M. S. (1983). The strength of weak ties: A network theory revisited. Sociological Theory, 1, 201–233.

Gu, B., and Ye, Q. (2014). First step in social media: Measuring the influence of online management responses on customer satisfaction. Production and Operations Management, 23(4), 570–582.

Guan, X., Wang, Y., Yi, Z., and Chen, Y. (2020). Inducing consumer online reviews via disclosure. Production and Operations Management, 29(8), 1956–1971.

Hausman, J., Hall, B. H., and Griliches, Z. (1984). Econometric models for count data with an application to the patents-R and D relationship. Econometrica, 52(4), 909–938.

Heimbach, I., and Hinz, O. (2018). The impact of sharing mechanism design on content sharing in online social networks. Information Systems Research, 29(3), 592–611.

Hernández-Ortega, B. (2018). Don’t believe strangers: Online consumer reviews and the role of social psychological distance. Information and Management, 55(1), 31–50.

Hershkovitz, A., and Hayat, Z. (2020). The role of tie strength in assessing credibility of scientific content on facebook. Technology in Society, 61, 101261.

Huang, S., Aral, S., Hu, Y. J., and Brynjolfsson, E. (2020). Social advertising effectiveness across products: A large-scale field experiment. Marketing Science, 39(6), 1142–1165.

Hwang, Y., and Jeong, S.-H. (2016). “This is a sponsored blog post, but all opinions are my own’’: The effects of sponsorship disclosure on responses to sponsored blog posts. Computers in Human Behavior, 62, 528–535.

Jin, Y., Tan, Y., and Huang, J. (2022). Managing contributor performance in knowledgesharing communities: A dynamic perspective. Production and Operations Management, 31(11), 3945–3962.

John, L. K., Emrich, O., Gupta, S., and Norton, M. I. (2017). Does “liking” lead to loving? The impact of joining a brand’s social network on marketing outcomes. Journal of Marketing Research, 54(1), 144–155.

Kang, H., Kreuels, B., Adjei, O., Krumkamp, R., May, J., and Small, D. S. (2013). The causal effect of malaria on stunting: A Mendelian randomization and matching approach. International Journal of Epidemiology, 42(5), 1390–1398.

Kannan, K. B., Overby, E., and Narasimhan, S. (2025). Can improvements to mobile internet

service help reduce digital inequality? An empirical analysis of education and overall data consumption. Management Science, 71(7), 5419–6318.

Katona, Z., Zubcsek, P. P., and Sarvary, M. (2011). Network effects and personal influences: The diffusion of an online social network. Journal of Marketing Research, 48(3), 425– 443.

Kennedy, P. (2003). A guide to econometrics. MIT Press.

Khan, G. F., and Vong, S. (2014). Virality over YouTube: An empirical analysis. Internet Research, 24(5), 629–647.

Kim, M., and Song, D. (2018). When brand-related UGC induces effectiveness on social media: The role of content sponsorship and content type. International Journal of Advertising, 37(1), 105–124.

Kim, N., and Kim, W. (2018). Do your social media lead you to make social deal purchases? Consumer-generated social referrals for sales via social commerce. International Journal of Information Management, 39, 38–48.

Köcher, S., and Köcher, S. (2018). Should we reach for the stars? Examining the convergence between online product ratings and objective product quality and their impacts on sales performance. Journal of Marketing BehaviorJournal of Marketing Behavior, 3(2), 167– 183.

Kokkodis, M., Lappas, T., and Kane, G. C. (2022). Optional purchase verification in ecommerce platforms: More representative product ratings and higher quality reviews. Production and Operations Management, 31(7), 2943–2961.

Kwak, H., Lee, C., Park, H., and Moon, S. (2010). What is Twitter, a social network or a news media? Proceedings of the 19th International Conference on World Wide Web, 591–600.

Kwak, S. K., and Kim, J. H. (2017). Statistical data preparation: Management of missing values and outliers. Korean Journal of Anesthesiology, 70(4), 407–411.

Labrecque, J., and Swanson, S. A. (2018). Understanding the assumptions underlying instrumental variable analyses: A brief review of falsification strategies and related tools. Current Epidemiology Reports, 5(3), 214–220.

Lee, J. Y., and Sundar, S. S. (2013). To tweet or to retweet? That is the question for health professionals on Twitter. Health Communication, 28(5), 509–524.

Lee, Y.-J., Hosanagar, K., and Tan, Y. (2015). Do I follow my friends or the crowd? Information cascades in online movie ratings. Management Science, 61(9), 2241–2258.

Lei, Z., Yin, D., Mitra, S., and Zhang, H. (2022). Swayed by the reviews: Disentangling the effects of average ratings and individual reviews in online word‐of‐mouth. Production and Operations Management, 31(6), 2393–2411.

Levin, D. Z., and Cross, R. (2004). The strength of weak ties you can trust: The mediating role of trust in effective knowledge transfer. Management Science, 50(11), 1477–1490.

Li, X., and Wu, L. (2018). Herding and social media word-of-mouth: Evidence from Groupon. MIS Quarterly, 42(4), 1331–1351.

Lim, E. N. K., and McCann, B. T. (2014). Performance feedback and firm risk taking: The moderating effects of CEO and outside director stock options. Organization Science, 25(1), 262–282.

Lin, Z., and Wang, Q. (2018). E-commerce product networks, word-of-mouth convergence, and product sales. Journal of the Association for Information Systems, 19(1), 23–39.

Mallipeddi, R. R., Janakiraman, R., Kumar, S., and Gupta, S. (2021). The effects of social media content created by human brands on engagement: Evidence from Indian general election 2014. Information Systems Research, 32(1), 212–237.

Messing, S., and Westwood, S. J. (2014). Selective exposure in the age of social media: Endorsements trump partisan source affiliation when selecting news online. Communication Research, 41(8), 1042–1063.

Mulwa, C. K., and Visser, M. (2020). Farm diversification as an adaptation strategy to climatic shocks and implications for food security in northern Namibia. World Development, 129, 104906.

Munaro, A. C., Hübner Barcelos, R., Francisco Maffezzolli, E. C., Santos Rodrigues, J. P., and Cabrera Paraiso, E. (2021). To engage or not engage? The features of video content on YOUTUBE affecting digital consumer engagement. Journal of Consumer Behaviour, 20(5), 1336–1352.

Oeldorf-Hirsch, A., and Sundar, S. S. (2015). Posting, commenting, and tagging: Effects of sharing news stories on facebook. Computers in Human Behavior, 44, 240–249.

Park, E., Rishika, R., Janakiraman, R., Houston, M. B., and Yoo, B. (2018). Social dollars in online communities: The Effect of product, user, and network characteristics. Journal of Marketing, 82(1), 93–114.

Park, J., Lee, J. M., Xiong, V. Y., Septianto, F., and Seo, Y. (2021). David and Goliath: When and why micro-influencers are more persuasive than mega-influencers. Journal of Advertising, 50(5), 584–602.

Park, S. (Steven), Wei, X., and Lee, H. (2024). Revisiting the elaboration likelihood model in the context of a virtual influencer: A comparison between high‐ and low‐involvement products. Journal of Consumer Behaviour, 23(4), 1638–1652.

Pennebaker, J. W., Boyd, R. L., Jordan, K., and Blackburn, K. (2015). The Development and Psychometric Properties of LIWC2015. University of Texas at Austin.

Petty, R. E., and Cacioppo, J. T. (1986). The elaboration likelihood model of persuasion. Advances in Experimental Social Psychology, 19, 123–205.

Qiu, L., and Whinston, A. B. (2017). Pricing strategies under behavioral observational learning in social networks. Production and Operations Management, 26(7), 1249–1267.

Rishika, R., and Ramaprasad, J. (2019). The effects of asymmetric social ties, structural embeddedness, and tie strength on online content contribution behavior. Management Science, 65(7), 3398–3422.

Roberts, S. G. B., Dunbar, R. I. M., Pollet, T. V., and Kuppens, T. (2009). Exploring variation in active network size: Constraints and ego characteristics. Social Networks, 31(2), 138– 146.

Rodan, S., and Galunic, C. (2004). More than network structure: How knowledge heterogeneity influences managerial performance and innovativeness. Strategic Management Journal, 25(6), 541–562.

Rong, K., Zhou, D., Shi, X., and Huang, W. (2022). Social information disclosure of friends in

common in an e-commerce platform ecosystem: An online experiment. Production and Operations Management, 31(3), 984–1005.

Rui, H., Liu, Y., and Whinston, A. (2013). Whose and what chatter matters? The effect of tweets on movie sales. Decision Support Systems, 55(4), 863–870.

Salehan, M., Kim, D., and Kim, C. (2017). Use of online social networking services from a theoretical perspective of the motivation-participation-performance framework. Journal of the Association for Information Systems, 18(2), 141–172.

Shi, Z., Rui, H., and Whinston, A. B. (2014). Content sharing in a social broadcasting environment: Evidence from Twitter. MIS Quarterly, 38(1), 123–142.

Soni, N., and Verghese, M. (2018). Analyzing the impact of online brand trust on sales promotion and online buying decision. Journal of Marketing Management, 17(3), 7–25.

Sosa, M. E. (2014). Realizing the need for rework: From task interdependence to social networks. Production and Operations Management, 23(8), 1312–1331.

Stuart, E. A. (2010). Matching methods for causal inference: A review and a look forward. Statistical Science, 25(1), 1–21.

Sun, H., Chen, J., and Fan, M. (2021). Effect of live chat on traffic‐to‐sales conversion: Evidence from an online marketplace. Production and Operations Management, 30(5), 1201–1219.

Sun, H., Fan, M., and Tan, Y. (2020). An empirical analysis of seller advertising strategies in an online marketplace. Information Systems Research, 31(1), 37–56.

Sun, H., and Xu, L. (2018). Online reviews and collaborative service provision: A signaljamming model. Production and Operations Management, 27(11), 1960–1977.

Susarla, A., Oh, J.-H., and Tan, Y. (2016). Influentials, imitables, or susceptibles? Virality and word-of-mouth conversations in online social networks. Journal of Management Information Systems, 33(1), 139–170.

Tan, X. (Jane), Lu, Y., and Tan, Y. (2021). The impact of subscription reciprocity on charitable content creation and sharing: Evidence from Twitter on giving Tuesday. MIS Quarterly, 45(2), 535–562.

Tang, Q., Song, T., Qiu, L., and Agarwal, A. (2019). Online content consumption: Social endorsements, observational learning and word-of-mouth. Fortieth International Conference on Information Systems, 1–17.

Thai, T. D.-H., and Wang, T. (2020). Investigating the effect of social endorsement on customer brand relationships by using statistical analysis and fuzzy set qualitative comparative analysis (fsQCA). Computers in Human Behavior, 113, 106499.

Toubia, O., and Stephen, A. T. (2013). Intrinsic vs. image-related utility in social media: Why do people contribute content to Twitter? Marketing Science, 32(3), 368–392.

Tsai, H.-T., and Bagozzi, R. P. (2014). Contribution behavior in virtual communities: Cognitive, emotional, and social influences. MIS Quarterly, 38(1), 143–164.

Tsiakali, K. (2018). User-generated-content versus marketing-generated-content: Personality and content influence on traveler’s behavior. Journal of Hospitality Marketing and Management, 27(8), 946–972.

Tucker, C. E. (2016). Social advertising: How advertising that explicitly promotes social

influence can backfire. https://ssrn.com/abstract\_id=1975897

Tucker, C. E., and Zhang, J. (2011). How does popularity information affect choices? A field experiment. Management Science, 57(5), 828–842.

Wang, T., Thai, T. D.-H., Ly, P. T. M., and Chi, T. P. (2021). Turning social endorsement into brand passion. Journal of Business Research, 126, 429–439.

Wang, Y., Goes, P., Wei, Z., and Zeng, D. (2019). Production of online word‐of‐mouth: Peer effects and the moderation of user characteristics. Production and Operations Management, 28(7), 1621–1640.

Wei, Z., Xiao, M., and Rong, R. (2021). Network size and content generation on social media platforms. Production and Operations Management, 30(5), 1406–1426.

Wooldridge, J. M. (2015). Control function methods in applied econometrics. Journal of Human Resources, 50(2), 420–445.

Xu, P., and Liu, D. (2019). Product engagement and identity signaling: The role of likes in social commerce for fashion products. Information and Management, 56(2), 143–154.

Yan, L., Yan, X., Tan, Y., and Sun, S. X. (2019). Shared minds: How patients use collaborative information sharing via social media platforms. Production and Operations Management, 28(1), 9–26.

Yang, M., Ren, Y., and Adomavicius, G. (2019). Understanding user-generated content and customer engagement on Facebook business pages. Information Systems Research, 30(3), 839–855.

Zhang, Q., Liang, H., Peng, T.-Q., and Zhu, J. J. H. (2024). The effect of affordance on deliberation when retweeting: From the perspective of expression effect. Computers in Human Behavior, 151, 108010.

Zhang, X. (Michael), and Zhu, F. (2011). Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. American Economic Review, 101(4), 1601–1615.

Zhao, C., Wang, X., Xiao, Y., and Sheng, J. (2022). Effects of online reviews and competition on quality and pricing strategies. Production and Operations Management, 31(10), 3840– 3858.

## Appendix A. Video Category Distribution

In our dataset, the most popular video categories, “Gaming”, “People & Blogs”, and “Entertainment” account for 28.04%, 19.75%, and 13,94% of all sample videos, respectively. This observed distribution aligns closely with the established trends for general YouTube videos in Figure A1, which visualizes the distribution of YouTube videos by category from 2005 to 2021. According to Figure A1, “Gaming” became the most popular video category around 2018, followed by “People & Blogs” and “Entertainment”. While this consistency may not serve as rigorous proof that our sample is perfectly representative, it does support that our sample videos do not deviate from the general YouTube videos in terms of category distribution.

![](/api/attachments/U9HSA6JF/fulltext/images/18d52bce68792dfee385393dbab56f9a7421232377edfc52df9c68d3a4c6ac18.jpg)  
Figure A1. Percent of YouTube video content by category. <sup>9</sup>

## Appendix B. Variable Definition and Correlation

Table B1. Variable definition

<table><tr><td>Variables</td><td>Definition</td></tr><tr><td> $Dviews_{i,t}$ </td><td>Increased video views</td></tr><tr><td> $Otweets_{i,t}$ </td><td>Number of original tweets</td></tr><tr><td> $Retweets_{i,t}$ </td><td>Number of retweets</td></tr><tr><td> $Otweets\_ties_{i,t}$ </td><td>Average number of unique followers of original endorsers</td></tr><tr><td> $Retweets\_ties_{i,t}$ </td><td>Average number of unique followers of reposting endorsers</td></tr><tr><td> $Otweets\_tie\_strength_{i,t}$ </td><td>Average percentage of reciprocal followers of original endorsers</td></tr><tr><td> $Retweets\_tie\_strength_{i,t}$ </td><td>Average percentage of reciprocal followers of reposting endorsers</td></tr><tr><td> $Views_{i,t}$ </td><td>Total video views</td></tr><tr><td> $Likes_{i,t}$ </td><td>Total video likes</td></tr><tr><td> $Dislikes_{i,t}$ </td><td>Total video dislikes</td></tr><tr><td> $Comments_{i,t}$ </td><td>Total video comments</td></tr><tr><td> $CHcomments_{i,t}$ </td><td>Total channel comments</td></tr><tr><td> $CHviews_{i,t}$ </td><td>Total channel views (in thousands)</td></tr><tr><td> $CHsubscribers_{i,t}$ </td><td>Total channel subscribers</td></tr><tr><td> $CHvideos_{i,t}$ </td><td>Total videos posted</td></tr><tr><td> $CHage_{i,t}$ </td><td>Number of weeks since the provider registered on YouTube</td></tr></table>

Table B2. Correlation

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td><td>(13)</td><td>(14)</td><td>(15)</td></tr><tr><td>(1)Otwets $_{i,t}$ </td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2)Retweets $_{i,t}$ </td><td>0.540</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3)Otwets tie strength $_{i,t}$ </td><td>0.710</td><td>0.260</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4)Retweets tie strength $_{i,t}$ </td><td>0.446</td><td>0.703</td><td>0.305</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5)Otwets ties $_{i,t}$ </td><td>0.824</td><td>0.479</td><td>0.767</td><td>0.441</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(6)Retweets ties $_{i,t}$ </td><td>0.508</td><td>0.805</td><td>0.307</td><td>0.843</td><td>0.504</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(7)Views $_{i,t}$ </td><td>0.068</td><td>0.030</td><td>0.061</td><td>0.030</td><td>0.064</td><td>0.033</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(8)Likes $_{i,t}$ </td><td>0.077</td><td>0.037</td><td>0.065</td><td>0.034</td><td>0.072</td><td>0.039</td><td>0.871</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(9)Dislikes $_{i,t}$ </td><td>0.075</td><td>0.030</td><td>0.063</td><td>0.028</td><td>0.067</td><td>0.033</td><td>0.816</td><td>0.853</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(10)Comments $_{i,t}$ </td><td>0.077</td><td>0.036</td><td>0.063</td><td>0.033</td><td>0.070</td><td>0.039</td><td>0.773</td><td>0.878</td><td>0.807</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(11)CHcomments $_{i,t}$ </td><td>0.056</td><td>0.031</td><td>0.039</td><td>0.025</td><td>0.055</td><td>0.033</td><td>0.085</td><td>0.093</td><td>0.074</td><td>0.081</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>(12)CHviews $_{i,t}$ </td><td>0.032</td><td>0.014</td><td>0.025</td><td>0.010</td><td>0.031</td><td>0.014</td><td>0.622</td><td>0.455</td><td>0.451</td><td>0.376</td><td>0.207</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>(13)CHsubscribers $_{i,t}$ </td><td>0.034</td><td>0.018</td><td>0.025</td><td>0.014</td><td>0.033</td><td>0.017</td><td>0.560</td><td>0.509</td><td>0.460</td><td>0.445</td><td>0.191</td><td>0.770</td><td>1.000</td><td></td><td></td></tr><tr><td>(14)CHvideos $_{i,t}$ </td><td>-0.015</td><td>-0.010</td><td>-0.016</td><td>-0.013</td><td>-0.013</td><td>-0.012</td><td>0.079</td><td>-0.071</td><td>-0.013</td><td>-0.096</td><td>0.194</td><td>0.730</td><td>0.506</td><td>1.000</td><td></td></tr><tr><td>(15)CHage $_{i,t}$ </td><td>0.006</td><td>0.004</td><td>0.003</td><td>0.003</td><td>0.005</td><td>0.005</td><td>0.010</td><td>0.000</td><td>-0.017</td><td>-0.010</td><td>0.330</td><td>0.246</td><td>0.215</td><td>0.309</td><td>1.000</td></tr></table>

Notes: All variables are log-transformed, except for Otweets\_tie\_strength<sub>i,t</sub>, Otweets\_tie\_strength<sub>i,t</sub> , and CHage<sub>i,t</sub>.

## Appendix C. Different PSM Parameters

Table C1. Estimation results with different PSM parameters

<table><tr><td rowspan="4"></td><td colspan="5"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td colspan="3">Neighbor=1</td><td colspan="2">Neighbor=3</td></tr><tr><td>Caliper=0.15</td><td>Caliper=0.01</td><td>Caliper=0.001</td><td>Caliper=0.01</td><td>Caliper=0.001</td></tr><tr><td> $Otwerts_{i,t}$ </td><td>0.337***(0.093)</td><td>0.337***(0.093)</td><td>0.353***(0.093)</td><td>0.384***(0.089)</td><td>0.449***(0.089)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>-0.035(0.118)</td><td>-0.035(0.118)</td><td>-0.023(0.119)</td><td>-0.069(0.112)</td><td>-0.057(0.111)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_ties_{i,t}$ </td><td>0.022***(0.007)</td><td>0.022***(0.007)</td><td>0.021***(0.007)</td><td>0.025***(0.007)</td><td>0.023***(0.007)</td></tr><tr><td> $Retweets_{i,t} * Retweets\_ties_{i,t}$ </td><td>0.046***(0.010)</td><td>0.046***(0.010)</td><td>0.047***(0.010)</td><td>0.047***(0.009)</td><td>0.047***(0.009)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_tie\_strength_{i,t}$ </td><td>-0.064(0.109)</td><td>-0.064(0.109)</td><td>-0.075(0.108)</td><td>-0.089(0.101)</td><td>-0.118(0.100)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td>-0.209*(0.123)</td><td>-0.209*(0.123)</td><td>-0.251**(0.120)</td><td>-0.196*(0.119)</td><td>-0.235**(0.117)</td></tr><tr><td> $Residual(Otwerts_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $Residual(Retweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>203,531</td><td>203,531</td><td>202,905</td><td>344,899</td><td>343,654</td></tr><tr><td> $R^2$ </td><td>0.5513</td><td>0.5513</td><td>0.5515</td><td>0.5358</td><td>0.5356</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time fixed effects.  
\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

## Appendix D. Control Function

Table D1. Informal test of the exclusion restriction assumption of IVs

<table><tr><td></td><td> $Dviews_{i,t+1}$ </td></tr><tr><td> $Otwerts_{i,t}$ </td><td>0.426***(0.029)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.004(0.025)</td></tr><tr><td> $OppOtwerts_{i,t}$ </td><td>0.529(1.144)</td></tr><tr><td> $OppRetweets_{i,t}$ </td><td>-0.128(0.184)</td></tr><tr><td>Controls</td><td>Yes</td></tr><tr><td>Observations</td><td>365,615</td></tr><tr><td> $R^2$ </td><td>0.5263</td></tr></table>

Notes: The analysis is based on the matched sample. Standard errors in parentheses are clustered at the video level. The estimation includes video and time fixed effects.  
\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

In our research setting, Twitter has limited reach in certain countries such as China, Netherlands, Poland, Belgium, and Germany.<sup>10</sup> For videos originating from these countries, their low or negligible social endorsements (i.e., $O t w e e t s _ { i , t }$ and $R e t w e e t s _ { i , t } )$ —driven by low Twitter penetration—are unlikely to be affected by the proposed IVs (i.e., OppOtweets<sub>i,t</sub> and $O p p R e t w e e t s _ { i , t } )$ . If the exclusion restriction holds, these IVs (i.e., OppOtweets<sub>i,t</sub> and $O p p R e t w e e t s _ { i , t } )$ should exhibit no significant effect on the outcome $( \mathrm { i . e . , } D \nu i e w s _ { i , t + I } )$ in this subsample. To test this, we estimate the effects of $O p p O t w e e t s _ { i , t }$ and OppRetweets<sub>i,t</sub> on $\_ D v i e w s s _ { i , t + I }$ using a subsample of videos from low Twitter-penetration countries and without social endorsements. Table D2 reports insignificant coefficients of OppOtweets<sub>i,t</sub> and $O p p R e t w e e t s _ { i , t } ,$ supporting the exclusion restriction.

Table D2. Falsification test for the IVs

<table><tr><td></td><td> $Dviews_{i,t+1}$ </td></tr><tr><td> $OppOtwerts_{i,t}$ </td><td>-0.752(0.833)</td></tr><tr><td> $OppRetweets_{i,t}$ </td><td>0.141(0.225)</td></tr><tr><td>Controls</td><td>Yes</td></tr><tr><td>Observations</td><td>2,710</td></tr><tr><td> $R^2$ </td><td>0.6233</td></tr></table>

Notes: The analysis is based on the matched sample. Standard errors in parentheses are clustered at the video level. The estimation includes video and time fixed effects.  
\*\*\* $p < 0 . 0 1 , ^ { * * } p < 0 . 0 5 , ^ { * } p < 0 . 1 .$

Table D3. First stage results of control function

<table><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td></tr><tr><td> $Otweets_{i,t}$ </td><td> $Retweets_{i,t}$ </td></tr><tr><td> $OppOtwerts_{i,t}$ </td><td>-21.481***(1.871)</td><td></td></tr><tr><td> $OppRetweets_{i,t}$ </td><td></td><td>-2.254***(0.274)</td></tr><tr><td> $Otweets_{i,t}$ </td><td></td><td>0.516***(0.050)</td></tr><tr><td> $Otweets_{i,t} * Otweets\_ties_{i,t}$ </td><td></td><td>0.030***(0.006)</td></tr><tr><td> $Otweets_{i,t} * Otweets\_tie\_strength_{i,t}$ </td><td></td><td>-0.469***(0.069)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>375,471</td><td>375,471</td></tr><tr><td> $R^2$ </td><td>0.2575</td><td>0.3328</td></tr></table>

Notes: The analyses are based on the matched sample. Standard errors in parentheses are clustered at the video level. All estimations include video and time fixed effects.

$$
^ {* * *} p <   0. 0 1, ^ {* *} p <   0. 0 5, ^ {*} p <   0. 1.
$$

## Appendix E. Robustness Checks

Table E1. Estimation results with alternative IVs

<table><tr><td></td><td colspan="3"> $Dviews_{i,t+1}$ </td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td> $Otwets_{i,t}$ </td><td>0.369***(0.074)</td><td>0.309***(0.067)</td><td>0.320***(0.088)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.023(0.109)</td><td>-0.093(0.064)</td><td>-0.097(0.073)</td></tr><tr><td> $Otwets_{i,t} * Otwets\_ties_{i,t}$ </td><td>0.022***(0.007)</td><td>0.027***(0.006)</td><td>0.027***(0.007)</td></tr><tr><td> $Retweets_{i,t} * Retweets\_ties_{i,t}$ </td><td>0.047***(0.009)</td><td>0.046***(0.010)</td><td>0.046***(0.010)</td></tr><tr><td> $Otwets_{i,t} * Otwets\_tie\_strength_{i,t}$ </td><td>-0.047(0.099)</td><td>-0.096(0.090)</td><td>-0.097(0.091)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td>-0.212*(0.119)</td><td>-0.193*(0.116)</td><td>-0.192*(0.116)</td></tr><tr><td>Residual( $Otwets_{i,t}$ )</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Residual( $Retweets_{i,t}$ )</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td><td>345,021</td></tr><tr><td> $R^2$ </td><td>0.5358</td><td>0.5358</td><td>0.5358</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time fixed effects.  
\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

Table E2. Estimation results after removing endorsements by video providers

<table><tr><td rowspan="2"></td><td colspan="4"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Otwerts_{i,t}$ </td><td>0.320***(0.072)</td><td>0.292***(0.063)</td><td>0.279**(0.110)</td><td>0.335***(0.084)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.261***(0.092)</td><td>-0.095(0.086)</td><td>0.385***(0.125)</td><td>-0.046(0.113)</td></tr><tr><td> $Otwerts_{i,t}*Otwerts\_ties_{i,t}$ </td><td></td><td>0.026***(0.007)</td><td></td><td>0.027***(0.007)</td></tr><tr><td> $Retweets_{i,t}*Retweets\_ties_{i,t}$ </td><td></td><td>0.047***(0.009)</td><td></td><td>0.048***(0.009)</td></tr><tr><td> $Otwerts_{i,t}*Otwerts\_tie\_strength_{i,t}$ </td><td></td><td></td><td>0.066(0.109)</td><td>-0.062(0.100)</td></tr><tr><td> $Retweets_{i,t}*Retweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-0.245**(0.121)</td><td>-0.211*(0.119)</td></tr><tr><td> $Residual(Otwerts_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $Residual(Retweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td><td>345,021</td><td>345,021</td></tr><tr><td> $R^2$ </td><td>0.5356</td><td>0.5357</td><td>0.5356</td><td>0.5358</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time fixed effects.  
\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

![](/api/attachments/U9HSA6JF/fulltext/images/7221ed3fa066af226e24ba49248a7b7ec3d99ed32f359f8657cfa682fa289d1a.jpg)

![](/api/attachments/U9HSA6JF/fulltext/images/1b2a8ac306e67b2dbdb34b510e05c934cd2d255e5efb3f0191c231cfbf9c3d76.jpg)  
Figure E1. Sensitivity analysis for potential systematic mismeasurement of tie strength.

Table E3. Estimations results with additional controls

<table><tr><td rowspan="2"></td><td colspan="4"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Ottweets_{i,t}$ </td><td>0.293***(0.074)</td><td>0.280***(0.068)</td><td>0.295***(0.108)</td><td>0.331***(0.089)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.179**(0.088)</td><td>-0.118(0.093)</td><td>0.263**(0.118)</td><td>-0.079(0.116)</td></tr><tr><td> $Ottweets_{i,t} * Ottweets\_ties_{i,t}$ </td><td></td><td>0.016**(0.007)</td><td></td><td>0.017**(0.007)</td></tr><tr><td> $Retweets_{i,t} * Retweets\_ties_{i,t}$ </td><td></td><td>0.051***(0.010)</td><td></td><td>0.052***(0.010)</td></tr><tr><td> $Ottweets_{i,t} * Ottweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-0.002(0.111)</td><td>-0.079(0.103)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-0.217*(0.120)</td><td>-0.213*(0.119)</td></tr><tr><td> $PriorRetweets_{i,t}$ </td><td>-0.098**(0.050)</td><td>-0.104**(0.051)</td><td>-0.098*(0.051)</td><td>-0.101*(0.052)</td></tr><tr><td> $Oendorser\_favorites_{i,t}$ </td><td>-0.044(0.038)</td><td>-0.025(0.038)</td><td>-0.041(0.038)</td><td>-0.021(0.038)</td></tr><tr><td> $Oendorser\_posts_{i,t}$ </td><td>0.110***(0.030)</td><td>0.080***(0.031)</td><td>0.109***(0.030)</td><td>0.081***(0.030)</td></tr><tr><td> $Oendorser\_lists_{i,t}$ </td><td>-0.594(0.795)</td><td>0.029(0.789)</td><td>-0.485(0.792)</td><td>0.146(0.787)</td></tr><tr><td> $Residual(Otweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $Residual(Retweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td><td>345,021</td><td>345,021</td></tr><tr><td> $R^2$ </td><td>0.5357</td><td>0.5358</td><td>0.5357</td><td>0.5359</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time fixed effects.  
\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

Table E4. VIF

<table><tr><td></td><td> $Dviews_{i,t+1}$ </td></tr><tr><td> $Otweets_{i,t}$ </td><td>8.48</td></tr><tr><td> $Retweets_{i,t}$ </td><td>11.62</td></tr><tr><td> $Otweets_{i,t} *Otweets ties_{i,t}$ </td><td>4.63</td></tr><tr><td> $Retweets_{i,t} *Retweets ties_{i,t}$ </td><td>5.24</td></tr><tr><td> $Otweets_{i,t} *Otweets tie strength_{i,t}$ </td><td>4.59</td></tr><tr><td> $Retweets_{i,t} *Retweets tie strength_{i,t}$ </td><td>7.83</td></tr><tr><td> $Views_{i,t}$ </td><td>6.45</td></tr><tr><td> $Likes_{i,t}$ </td><td>7.87</td></tr><tr><td> $Dislikes_{i,t}$ </td><td>4.57</td></tr><tr><td> $Comments_{i,t}$ </td><td>4.64</td></tr><tr><td> $CHcomments_{i,t}$ </td><td>1.16</td></tr><tr><td> $CHviews_{i,t}$ </td><td>6.33</td></tr><tr><td> $CHsubscribers_{i,t}$ </td><td>2.61</td></tr><tr><td> $CHvideos_{i,t}$ </td><td>3.54</td></tr><tr><td> $CHage_{i,t+1}$ </td><td>1.22</td></tr><tr><td>Mean VIF</td><td>5.38</td></tr></table>

Table E5. Estimation results with normalized main variables

<table><tr><td rowspan="2"></td><td colspan="4"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Otwerts_{i,t}$ </td><td>2.630***(0.538)</td><td>2.350***(0.488)</td><td>2.485***(0.835)</td><td>2.793***(0.650)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>1.672**(0.653)</td><td>-0.689(0.614)</td><td>2.414***(0.893)</td><td>-0.494(0.805)</td></tr><tr><td> $Otwerts_{i,t} *Otwerts\_ties_{i,t}$ </td><td></td><td>0.386***(0.105)</td><td></td><td>0.400***(0.105)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_ties_{i,t}$ </td><td></td><td>0.769***(0.155)</td><td></td><td>0.784***(0.156)</td></tr><tr><td> $Otwerts_{i,t} *Otwerts\_tie\_strength_{i,t}$ </td><td></td><td></td><td>0.230(0.812)</td><td>-0.639(0.733)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-1.635*(0.869)</td><td>-1.410*(0.850)</td></tr><tr><td> $Residual(Otwerts_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $Residual(Retweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td><td>345,021</td><td>345,021</td></tr><tr><td> $R^2$ </td><td>0.5356</td><td>0.5357</td><td>0.5356</td><td>0.5358</td></tr></table>

Notes: The analyses are based on the matched sample. Otweets<sub>i,t</sub>, Retweets<sub>i,t</sub>, Otweets\_ties<sub>i,t</sub>, Retweets\_ties<sub>i,t</sub> Otweets\_tie\_strength<sub>i,t</sub>, and Retweets\_tie\_strength<sub>i,t</sub> are normalized. Clustered standard errors at the video level are in parentheses. All estimations include video and time fixed effects.

Table E6. Estimation results using winsorized data (99 percentiles)

<table><tr><td rowspan="2"></td><td colspan="4"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Otwerts_{i,t}$ </td><td>0.404***(0.067)</td><td>0.358***(0.067)</td><td>0.400***(0.100)</td><td>0.429***(0.086)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.212**(0.087)</td><td>-0.088(0.087)</td><td>0.308***(0.118)</td><td>-0.064(0.113)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_ties_{i,t}$ </td><td></td><td>0.021***(0.007)</td><td></td><td>0.022***(0.007)</td></tr><tr><td> $Retweets_{i,t} * Retweets\_ties_{i,t}$ </td><td></td><td>0.045***(0.009)</td><td></td><td>0.046***(0.010)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_tie\_strength_{i,t}$ </td><td></td><td></td><td>0.013(0.107)</td><td>-0.097(0.101)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-0.233*(0.119)</td><td>-0.210*(0.118)</td></tr><tr><td> $Residual(Otwerts_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $Residual(Retweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td><td>345,021</td><td>345,021</td></tr><tr><td> $R^2$ </td><td>0.5356</td><td>0.5358</td><td>0.5356</td><td>0.5358</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time fixed effects.

$$
p <   0. 0 1, * * p <   0. 0 5, * p <   0. 1.
$$

Table E7. Estimation results using winsorized data (three standard deviations above the mean)

<table><tr><td rowspan="2"></td><td colspan="4"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Otwerts_{i,t}$ </td><td>0.408***(0.064)</td><td>0.373***(0.065)</td><td>0.395***(0.094)</td><td>0.427***(0.083)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.209**(0.082)</td><td>-0.079(0.089)</td><td>0.312***(0.110)</td><td>-0.040(0.115)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_ties_{i,t}$ </td><td></td><td>0.017**(0.007)</td><td></td><td>0.019**(0.008)</td></tr><tr><td> $Retweets_{i,t} * Retweets\_ties_{i,t}$ </td><td></td><td>0.045***(0.010)</td><td></td><td>0.046***(0.010)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_tie\_strength_{i,t}$ </td><td></td><td></td><td>0.027(0.105)</td><td>-0.076(0.102)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-0.237**(0.119)</td><td>-0.219*(0.118)</td></tr><tr><td> $Residual(Otwerts_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $Residual(Retweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td><td>345,021</td><td>345,021</td></tr><tr><td> $R^2$ </td><td>0.5357</td><td>0.5358</td><td>0.5357</td><td>0.5358</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time fixed effects.  
\*\*\* $p < 0 . 0 1$ , \*\* p < 0.05, \* p < 0.1.

Table E8. Estimation results with outliers removed (95 percentiles)

<table><tr><td rowspan="2"></td><td colspan="4"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Otwerts_{i,t}$ </td><td>0.408***(0.052)</td><td>0.335***(0.065)</td><td>0.384***(0.073)</td><td>0.332***(0.079)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.156*(0.094)</td><td>-0.181*(0.103)</td><td>0.324***(0.115)</td><td>-0.048(0.124)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_ties_{i,t}$ </td><td></td><td>0.019**(0.009)</td><td></td><td>0.019**(0.009)</td></tr><tr><td> $Retweets_{i,t} * Retweets\_ties_{i,t}$ </td><td></td><td>0.046***(0.012)</td><td></td><td>0.045***(0.013)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_tie\_strength_{i,t}$ </td><td></td><td></td><td>0.037(0.117)</td><td>-0.003(0.116)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-0.388**(0.159)</td><td>-0.304*(0.159)</td></tr><tr><td> $Residual(Otwerts_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $Residual(Retweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>344,329</td><td>344,306</td><td>344,255</td><td>344,234</td></tr><tr><td> $R^2$ </td><td>0.5281</td><td>0.5279</td><td>0.5276</td><td>0.5274</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video and time fixed effects.  
\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

Table E9. Estimation results using video random effects

<table><tr><td rowspan="2"></td><td colspan="4"> $Dviews_{i,t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Otwerts_{i,t}$ </td><td>0.262***(0.080)</td><td>0.249***(0.063)</td><td>0.276***(0.100)</td><td>0.282***(0.080)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>0.269**(0.111)</td><td>-0.098(0.095)</td><td>0.374***(0.126)</td><td>-0.009(0.116)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_ties_{i,t}$ </td><td></td><td>0.025***(0.007)</td><td></td><td>0.024***(0.007)</td></tr><tr><td> $Retweets_{i,t} * Retweets\_ties_{i,t}$ </td><td></td><td>0.046***(0.009)</td><td></td><td>0.047***(0.009)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-0.042(0.093)</td><td>-0.076(0.090)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td></td><td></td><td>-0.253**(0.119)</td><td>-0.228*(0.117)</td></tr><tr><td> $Residual(Otwerts_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $Residual(Retweets_{i,t})$ </td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>345,021</td><td>345,021</td><td>345,021</td><td>345,021</td></tr></table>

Notes: The analyses are based on the matched sample. Clustered standard errors at the video level are in parentheses. All estimations include video random effects and time fixed effects.  
\*\*\* $p < 0 . 0 1$ \*\* $p < 0 . 0 5$ $\cdot _ { p } < 0 . 1$

Table E10. Estimation results using the negative binomial model

<table><tr><td></td><td> $Dviews_{i,t+1}$ </td></tr><tr><td> $Otwerts_{i,t}$ </td><td>0.089***(0.012)</td></tr><tr><td> $Retweets_{i,t}$ </td><td>-0.069***(0.014)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_ties_{i,t}$ </td><td>0.033***(0.001)</td></tr><tr><td> $Retweets_{i,t} * Retweets\_ties_{i,t}$ </td><td>0.030***(0.002)</td></tr><tr><td> $Otwerts_{i,t} * Otwerts\_tie\_strength_{i,t}$ </td><td>0.008(0.021)</td></tr><tr><td> $Retweets_{i,t} *Retweets\_tie\_strength_{i,t}$ </td><td>-0.169***(0.028)</td></tr><tr><td>Controls</td><td>Yes</td></tr><tr><td>Observations</td><td>365,615</td></tr></table>

Notes: The analysis is based on the matched sample. The estimation includes video random effects and time fixed effects.

$$
p <   0. 0 1, ^ {* *} p <   0. 0 5, ^ {*} p <   0. 1.
$$
