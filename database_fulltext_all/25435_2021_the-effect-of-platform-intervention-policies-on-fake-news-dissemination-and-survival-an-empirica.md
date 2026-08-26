---
otero_id: 25435
otero_key: "GRBMW4GS"
title: "The Effect of Platform Intervention Policies on Fake News Dissemination and Survival: An Empirical Examination"
authors: "Ka Chung Ng; Jie Tang; Dongwon Lee"
year: "2021"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2021.1990612"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Effect of Platform Intervention Policies on Fake News Dissemination and Survival: An Empirical Examination

## Ka Chung Ng, Jie Tang & Dongwon Lee

To cite this article: Ka Chung Ng, Jie Tang & Dongwon Lee (2021) The Effect of Platform Intervention Policies on Fake News Dissemination and Survival: An Empirical Examination, Journa of Management Information Systems, 38:4, 898-930, DOI: 10.1080/07421222.2021.1990612

To link to this article: https://doi.org/10.1080/07421222.2021.1990612

![](/api/attachments/GRBMW4GS/fulltext/images/a589b9c0e24184c10728389aa8e122f4b6c4d694b31c659683f741aa0a7095aa.jpg)

© 2021 The Author(s). Published with license by Taylor & Francis Group, LLC.

![](/api/attachments/GRBMW4GS/fulltext/images/b482d8e50a3590aa9fa0acc1cb30b0db737dd62d67f2bca30eb279caad617702.jpg)

Published online: 02 Jan 2022.

Article views: 4597

![](/api/attachments/GRBMW4GS/fulltext/images/14c03a4cad2af360a59e190730a7b8147a7659c2538cb7af765244a8c9627277.jpg)

View supplementary material

![](/api/attachments/GRBMW4GS/fulltext/images/fa86ae105f39924cad04b1791c0d8a99e7ca54f3648536c293c6797706096f02.jpg)

![](/api/attachments/GRBMW4GS/fulltext/images/2cf0632ade6fcc7437f5716fea23a3f583b549287e2b36f369c04831c7924e3d.jpg)

Submit your article to this journal

![](/api/attachments/GRBMW4GS/fulltext/images/ab0a5681c68c3bbeb0a19cd0c6b3f4a534d8d791979fb0fb63aca5532032c49a.jpg)

View related articles

![](/api/attachments/GRBMW4GS/fulltext/images/479d81db4632f2c804b0cf526018ecd9bfd5a261a750040468a3b2bccb286d1d.jpg)

View Crossmark data

![](/api/attachments/GRBMW4GS/fulltext/images/6c4701cd10d6c0c2a7fc33df3c6e527d799013d0f6214017c73715809d39d778.jpg)

Citing articles: 3 View citing articles

@ OPEN ACCESS

Check for updates

# The Efect of Platform Intervention Policies on Fake News Dissemination and Survival: An Empirical Examination

Ka Chung Ng <sup>a,b</sup>, Jie Tang <sup>c</sup>, and Dongwon Lee <sup>a</sup>

<sup>a</sup>Department of Information Systems, Business Statistics and Operations Management, School of Business and Management, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, HONG KONG; <sup>b</sup>Department of Management and Marketing, Faculty of Business, Hong Kong Polytechnic University, Hung Hom, Kowloon, HONG KONG; <sup>c</sup>HKU Business School, The University of Hong Kong, Pok Fu Lam, Hong Kong, HONG KONG

## ABSTRACT

Fake news on social media has become a serious problem, and social media platforms have started to actively implement various interventions to mitigate its impact. This paper focuses on the efectiveness of two platform interventions, namely a content-level intervention (i.e., a fake news flag that applies to a single post) and an account-level intervention (i.e., a forwarding restriction policy that applies to the entire account). Collecting data from China’s largest social media platform, we study the impact of a fake news flag on three fake news dissemination patterns using a propensity score matching method with a diference-in-diferences approach. We find that implementing a policy of using fake news flag influences the dissemination of fake news in a more centralized manner via direct forwards and in a less dispersed manner via indirect forwards, and that fake news posts are forwarded more often by influential users. In addition, compared with truthful news, fake news is disseminated in a less centralized and more dispersed manner and survives for a shorter period after a forwarding restriction policy is implemented. This study provides causal empirical evidence of the efect of a fake news flag on fake news dissemination. We also expand the literature on platform interventions to combat fake news by investigating a less studied account-level intervention. We discuss the practical implications of our results for social media platform owners and policymakers.

## KEYWORDS

Fake News; Fake News Online; Fake News Flag; Forwarding Restriction Policy; Fake News Dissemination; Quasi-Experiment; Online Disinformation; Platform Policies

## Introduction

Online channels such as social media play an important role in information acquisition and dissemination [62]. However, these channels are increasingly afected by the spread of fake news, which should be addressed through substantial eforts, especially during serious social, political, and epidemiological crises like the COVID-19 pandemic of 2020. Unlike content disseminated through traditional channels such as newspapers and broadcasts, social media content can be created, modified, and spread in a much less rigorous way. It can be published by a layperson without suficient knowledge of a topic, modified, and even distorted during dissemination, ultimately leading to serious and undesirable consequences.

For instance, as reported by CNN,<sup>1</sup> a man in Phoenix, U.S., died of chloroquine phosphate poisoning after taking a product intended for cleaning fish tanks in the hope of recovering from COVID-19, after reading a post on social media advocating this as a treatment. Antonio Guterres, Secretary-General of the United Nations, alerted people to the “dangerous epidemic of fake news” on COVID-19 in the current situation and stressed that social media companies should take responsibility for tackling the spread of fake news.<sup>2</sup>

In line with this alert, social media platforms have implemented various interventions in recent years, including WhatsApp’s forwarding restriction to slow the spread of fake news, Sina Weibo’s launch of its Community Management Center to detect fake news by social reporting,<sup>4</sup> and Facebook’s fact-checking teams that verify the factuality of news stories.<sup>5</sup> Although these eforts to protect the credibility of information are recognized, the efectiveness of platform interventions remains unclear [2,41,57]. We believe that it is urgent and important to examine the efectiveness of platform interventions with empirical evidence. This study thus performs a series of analyses to evaluate the efectiveness of platform interventions to limit the spread of fake news. Specifically, we study the efectiveness of platform interventions in terms of fake news dissemination and survival. We further divide fake news dissemination into three patterns to better understand the more nuanced impacts of platform interventions.

Previous studies focused primarily on the content-level platform intervention, which applies to a single piece of information. A fake news flag is a good example of the contentlevel intervention; it attaches a label to a post to indicate that the post is fake news [44,45,49]. The results of previous studies on its efectiveness mainly focus on the cognitive level. Several studies have shown that flagging fake news can reduce its believability and sharing intentions [17,44]. However, other studies have found that a fake news flag can be inefective due to confirmation bias [45] and people’s habit of disregarding warnings [55]. These seemingly inconsistent findings based on psychological outcomes motivate us to investigate the influence of a fake news flag on people’s actual behavior in a more generalizable setting. Many social media platforms, such as Twitter, do not prevent the spread of flagged fake news to ensure the practice of free speech, unless the harm caused by such fake news is extremely serious (i.e., a threat to national security).<sup>6</sup> Besides, fake news may be continuously forwarded even after being flagged as it is most often more novel than real news [69]. Therefore, it is of great interest to understand how a fake news flag works in the real world. Instead of focusing on the psychological outcomes induced by a fake news flag, we take a diferent approach by using large-scale archival data collected from the field and exploiting a quasi-experiment to establish a causal relationship between a fake news flag and people’s sharing behaviors.

In addition to studying a fake news flag, we identify an important research gap in the relevant literature. As the impact of fake news has become increasingly serious,<sup>7</sup> platforms have started to implement stricter regulations by imposing activity restrictions on accounts that publish fake news. We refer to this type of restriction as an account-level platform intervention. Unlike a fake news flag, which mitigates fake news by focusing on people’s cognitive processes [25], the restriction intervention directly controls the spread of fake news by limiting people’s engagement with fake news and inducing deterrence among accounts that intend to create and distribute fake news. However, there are concerns about the negative impacts of this intervention, as it may unintentionally restrict freedom of speech and block legitimate contents.<sup>8</sup> It also takes time for the platform to discern the legitimacy of a post [12]. Therefore, our work fills this research gap by empirically examining the efectiveness of the account-level intervention on fake news dissemination. As little is known about the impact of the account-level intervention, we also examine its efectiveness in shortening the survival time of fake news. Contrary to popular belief, fake news may not be overwhelmed by a huge amount of information online and disappear quickly (within days) [58,66]. If fake news can survive for an extended period, it is more likely to be spread through likes, sharing, comments, and, more importantly, reading. Exposure to fake news is dangerous, as people may take action without seeking the truth. Therefore, stopping the early spread of fake news is important to minimize its damage and negative social impact. In this regard, in addition to scholarly implications, we believe that understanding the impact of the account-level platform intervention on the survival time of fake news is of great importance for practice.

This study leverages two interventions implemented by Sina Weibo, the largest social media platform in China: a fake news flag as a content-level intervention and a forwarding restriction policy as an account-level intervention. To this end, we empirically examine how these two platform interventions afect fake news and answer the following two research questions:

1. How does a content-level platform policy, i.e., fake news flags, afect fake news dissemination?

2. How does an account-level platform policy, i.e., forwarding restrictions, afect fake news dissemination and fake news survival?

Using natural language processing and propensity score matching (PSM), we obtain a matched sample of fake news and truthful news to alleviate potential endogeneity issues for empirical analysis. We first study the impact of a fake news flag by using a diference-indiferences (DiD) approach. This specification helps us to identify a causal relationship between a fake news flag and fake news dissemination. We find that a post is distributed through more direct forwards than indirect forwards after being marked as “fake news.” Furthermore, a fake news flag encourages influential users to spread fake news posts to confirm its falsehood. Next, we estimate the impact of implementing a forwarding restriction policy by using the matched sample and controlling for the observable characteristics of the post and the user. Our results show that a forwarding restriction policy afects fake news and truthful news diferently. Compared with truthful news, fake news is disseminated in a less centralized but more dispersed manner and has a significantly shorter survival time after the implementation of a forwarding restriction policy.

Overall, we find that a fake news flag and a forwarding restriction policy have diferent efects on fake news, with the former leading to more centralized and less dispersed dissemination of fake news and the latter yielding the opposite pattern. These results are not contradictory, as fake news flag and forwarding restriction policy are theorized as two diferent types of platform intervention. Therefore, their diferent influences on fake news dissemination are expected and can be explained by two mechanisms. The impact of a fake news flag on fake news is explained by the reduction of content ambiguity [35], which afects the weak ties of the fake news publishing account, whereas the impact of a forwarding restriction policy on fake news is explained by relational concerns arising from the strong ties [71]. In practice, these findings can inform social media platforms about designing interventions to combat the spread of fake news. Although the accountlevel intervention seems to represent a “one-size-fits-all” policy, our results suggest that it does not afect the normal and desirable dissemination of truthful news.

This study contributes to the literature on platform interventions to combat fake news on social media. We provide empirical evidence based on field data of the causal impact of the content-level intervention (i.e., fake news flag) on fake news dissemination, which extends previous findings based on cognitive outcomes to actual behaviors by examining the practical importance of and capacity for flagging fake news to reduce its harm and social impact. We further investigate a less studied account-level intervention (i.e., forwarding restriction policy) and shed light on its efectiveness in mitigating the spread of fake news.

The rest of this paper is organized as follows. In the next section, we summarize the related literature and identify research gaps. In Section 3, we theorize the impacts of the two platform intervention policies on fake news. In Section 4, we introduce the research context and describe the data collected for the study. In Section 5, we propose our identification strategies. In Section 6, we present and discuss the research results. We discuss the contributions and limitations of this study in Section 7 and conclude our study in Section 8.

## Related Literature

## Fake News on Social Media

Fake news refers to news posts with deceptive intentions and false content [1,34]. Fake news also strongly overlaps with other deceptive information such as misinformation (false or misleading information) and disinformation (false information that is purposely spread to deceive people) [41]. As social media has changed the way news is created and consumed, such that people typically only read headlines or watch short videos,<sup>9</sup> we define fake news in a broader sense as any information that is intentionally and verifiably false and could mislead readers.

The issue of fake news on social media has received much attention in previous studies [1,33,45,69], given its huge impact on politics, social crises, and other aspects of social life. One strand of the literature focuses on the empirical analysis of fake news dissemination, using descriptive analyses to examine dissemination patterns in terms of post and user characteristics [42,46,65,69]. For instance, Vosoughi et al. [69] found that fake news spreads farther, faster, deeper, and more broadly than truthful news across various topics, including politics, terrorism, and natural disasters. In addition to these static characteristics, previous studies have adopted a dynamic perspective to study fake news dissemination with informative results [32,65]. For example, Sutton et al. [64] explored how users’ follower-followee networks can influence the transmission of crisis information from a social network perspective. Tang and Ng [66] examined the forwarding behavior of users and found that more forwards are associated with a longer survival time of fake news on social media. The characteristics of fake news recipients have also been examined. For example, in the context of the 2016 U.S. presidential election, studies have shown that people who were older [21,23], politically conservative [21,23], and heavily involved in political news [21] were more likely to engage with fake news.

Another strand of the literature focuses on the psychological mechanisms or consequences of users exposed to fake news on social media. Several studies have posited the existence of confirmation bias, arguing that users tend to believe news that confirms their prior beliefs, regardless of the authenticity of its content [33,34]. When encountering information that does not align with their prior beliefs, individuals experience cognitive dissonance [24] and tend to resolve such dissonance by rejecting new information, as this often requires less efort than changing one’s beliefs. Other mechanisms, such as fluency via prior exposure [50], laziness or lack of reasoning [51], and cognitive and afective engagement [42], have also been proposed to explain why people are susceptible to fake news. In terms of outcomes, previous studies have focused on perceived believability [33,34,45], engagement with the news (e.g., read, like, comment, and share) [33,34,43,45,47,49], and fact-checking behavior [68].

In summary, studies have investigated several aspects of fake news, including the characteristics of fake news content, publishers, and receivers; the mechanisms behind people’s susceptibility to fake news; and individuals’ attitudes and behavioral outcomes when exposed to fake news on social media. However, to the best of our knowledge, relatively few studies have used field data to investigate platform interventions aimed at changing people’s behavior toward fake news.

## Platform Interventions to Combat Fake News

Aside from understanding the phenomenon of fake news per se, previous studies have focused on platform interventions as mitigation strategies to detect [23,34] and stop [1,2,14,18,33] the spread of fake news. Most empirical studies of platform interventions, as summarized in Table 1, have focused on the content-level intervention, which only regulates one piece of information on social media. A fake news flag is a commonly studied content-level intervention, but the results of previous studies on its efectiveness are mixed.

For instance, Moravec et al. [44] showed that flagging fake news along with training on the meaning of the flag could significantly reduce the believability of fake news. They also showed that conducting flagging interventions to trigger subconscious processing (i.e., by displaying a visual “stop” sign when flagging fake news), deliberative reasoning (i.e., by displaying a text argument when flagging fake news), or a combination of these two approaches can efectively reduce the believability of fake news on social media. Garrett and Poulsen [17] reported that publishers’ self-identified flags could reduce people’s beliefs and sharing intentions regarding inaccurate messages. However, Moravec et al. [45] found that although a fake news flag can trigger increased cognitive activity in people, it cannot afect their judgments about the truth due to confirmation bias. In the same vein, Ross et al. [55] studied a fake news flag with additional manipulation (either a normal warning message indicating that the focal information was disputed by the third party or a negatively framed risk-handling advice) and found no significant efect of the flag on fake news. Considering the interaction between a fake news flag and the reputation of the information source, Figl et al. [14] found that although the flag may reduce the believability of fake news, this efect is weakened if the source of that fake news has a good reputation. Recently, Pennycook et al. [49] suggested that a fake news flag induces an implied truth efect so that unflagged fake news headlines are considered valid and more accurate by default.

<table><tr><td colspan="5">Table 1. Existing Empirical Studies on Platform Intervention against Fake News</td></tr><tr><td>Reference</td><td>Platform Intervention</td><td>Dependent Variable</td><td>Data</td><td>Fake vs. Truthful News Comparison</td></tr><tr><td>This study</td><td>Content-level: fake news flagAccount-level: forwarding restriction policy</td><td>Dissemination pattern and survival time</td><td>Field</td><td>Yes</td></tr><tr><td>Pennycook et al. [49]</td><td>Content-level: fake news flag</td><td>Accuracy judgment and social media sharing</td><td>Behavioral experiment</td><td>Yes</td></tr><tr><td>Figl et al. [14]</td><td>Content-level: fake news flag</td><td>News believability</td><td>Behavioral experiment</td><td>No</td></tr><tr><td>Kim and Dennis [33]</td><td>Content-level: highlighting source</td><td>Engagement with news (read, like, comment, and share)</td><td>Behavioral experiment</td><td>No</td></tr><tr><td>Kim et al. [34]</td><td>Content-level: source rating</td><td>Engagement with news (read, like, comment, and share)</td><td>Behavioral experiment</td><td>No</td></tr><tr><td>Moravec et al. [45]</td><td>Content-level: fake news flag</td><td>News believability</td><td>Behavioral experiment</td><td>Yes</td></tr><tr><td>Tang and Ng [66]</td><td>Community-level: launch of the social reporting system</td><td>Survival time</td><td>Field</td><td>No</td></tr><tr><td>Moravec et al. [44]</td><td>Content-level: fake news flag</td><td>News believability</td><td>Behavioral experiment</td><td>No</td></tr><tr><td>Ross et al. [55]</td><td>Content-level: fake news flag (warning message with/without risk-framed advice)</td><td>Number of hits and false alarms identified by a user</td><td>Behavioral experiment</td><td>No</td></tr></table>

The literature mainly addresses the efectiveness of a fake news flag based on cognitive and psychological outcomes, such as content believability and sharing intentions. To the best of our knowledge, little research has focused on changes in people’s actual behavior in response to a fake news flag. Understanding this efect is crucial for fake news research, as the ultimate goal of any platform intervention is to stop the spread of fake news. In this regard, this study considers a more generalizable setting that exploits field data to investigate the efectiveness of flagging deceptive content by examining changes in people’s sharing behavior. In particular, we aim to understand how a post is disseminated after being flagged as fake news.

In light of the huge impact of fake news on society, social media platforms have started to take a proactive approach by restricting the activities of accounts that publish deceptive information. This imposition of restrictions is considered an account-level intervention. Algorithms have been developed to detect and remove malicious and bot accounts created solely to spread fake news [59]. In addition, network-based methods have been proposed to stop the spread of fake news by identifying a set of accounts to monitor [59] or by controlling the flow of information through suspicious accounts [3]. Nevertheless, the efectiveness of this type of platform intervention has been less studied, as shown in Table 1. The account-level intervention is expected to be a better fake news mitigation strategy, as it not only regulates isolated fake news but also prevents the account publishing this fake news from performing activities such as forwarding posts or being followed by other accounts. This intervention should trigger inhibitory emotions such as fear and dread among accounts with the intent to deceive, efectively deterring them from creating and spreading fake news [52]. However, this account-level intervention may be detrimental to the freedom of speech and might inevitably hinder the normal circulation of credible information, i.e., truthful news. Therefore, it is theoretically and practically important to study the account-level intervention and its impact on the dissemination of fake and truthful news.

## Hypothesis Development

## Conceptualization of Dissemination Characteristics

The main objective of this study is to examine how content-level and account-level platform interventions afect fake news dissemination. We define “the dissemination of a post” as a directed network, with each node representing an account and each link representing a forwarding of the post by the account. We then divide the dissemination of posts into three patterns, namely centrality, dispersibility, and influenceability.

Centrality captures the centralized distribution of a post by counting its direct forwards. This pattern is commonly considered when studying information difusion [18,21,25]. In our context, high centrality indicates that a post receives more direct forwards than indirect forwards. Dispersibility captures how far and deep a post is distributed in its dissemination network. Vosoughi et al. [69] captured this dissemination characteristic through structural virality [19] and documented that fake news spreads significantly farther, deeper, and more broadly than truthful news. In this study, we propose a similar but more accurate measure than structural virality to represent the dispersibility of fake news, in which a post with high dispersibility indicates that it spreads farther and deeper than a post with low dispersibility.

Finally, influenceability captures whether a post is widely disseminated to other accounts through a few direct forwards. The literature suggests that influential users help to facilitate the cascade and spread of information [11,72]. Therefore, a few direct forwards of a fake news post can also reach many other accounts if it is forwarded by influential users. We represent influenceability as the reach of a post that is distributed through influential users.

Our three proposed dissemination patterns correspond to basic and commonly used measures in social networks, namely degree centrality, closeness centrality, and eigenvector centrality [19,56,73]. These three measures use various concepts of social networks, such as degree [56], shortest path, interconnectedness [40], social influence [73], and power [15], to capture the main aspects of a post dissemination network.

## Efect of the Content-Level Intervention: Fake News Flag

To identify the efect of a fake news flag on post dissemination patterns in terms of centrality and dispersibility, we first draw on social tie theory and define two types of social ties for an account: strong ties and weak ties [20]. Strong ties refer to proximate followers who can forward posts directly from the focal account, and weak ties refer to other users with more than one degree of separation from the focal account [71]. Due to the homophily of strong ties, followers are more likely to have the same views and beliefs as the focal account [22,38,48]. Therefore, the forwarding behavior of strong ties is not afected by a fake news flag due to confirmation bias [33,34,45].

In contrast, weak ties are distant followers who are less likely to have the same views and beliefs as the focal account. The forwarding behavior of weak ties is thus afected by a fake news flag that reduces the ambiguity of the post and eliminates the followers’ need for information verification. Rumor theory suggests that ambiguity is an important factor that leads to fake news dissemination [35]. For example, Rosnow [54] proposed that uncertainty is a major predictor of rumor generation and transmission. Oh et al. [46] found that the ambiguity of the information source is a significant predictor of rumor dissemination in the context of a social crisis. Therefore, before a post is identified as fake news, its authenticity is ambiguous to its audience. As individuals experience a lack of reliable information in an ambiguous situation, they tend to engage in information seeking, sharing, and elaboration to resolve information uncertainty, incompleteness, or incongruence [32,46]. With a fake news flag, the ambiguity is lifted because the post is verified as fake news. In line with this reasoning, we predict that flagging fake news will reduce its ambiguity, preventing it from spreading farther and more broadly through weak ties. Therefore, we expect that a fake news flag leads to more centralized and less dispersed dissemination of fake news and propose the following hypotheses:

H1a: A fake news flag increases the centrality of the fake news dissemination network.

H1b: A fake news flag decreases the dispersibility of the fake news dissemination network.

Regarding the influenceability of the fake news dissemination network, influential users with many followers are expected to behave more cautiously to protect their authenticity, good reputation, and good public relations [4,13]. They tend to avoid disseminating an ambiguous post until it has been verified but will forward verified fake news to help dispel it so that their followers are not fooled or confused by fake news posts. As a result, we expect influential users to be more likely to spread a post after it is flagged as fake news, as the ambiguity regarding its authenticity is removed. Accordingly, we propose the following hypothesis:

H1c: A fake news flag increases the influenceability of the fake news dissemination network.

## Efect of the Account-Level Intervention: Forwarding Restriction Policy

Unlike the content-level intervention that targets post of questionable reliability, the account-level intervention targets malicious accounts and imposes severe punishment to combat the spread of fake news. It can be a very eficient strategy to fight the wave of fake news, as accounts are completely blocked from posting deceptive information. However, as mentioned above, this intervention can also cause fear and concern among legitimate accounts about publishing trustworthy content and may restrict freedom of speech and the spread of truthful news. Research has also suggested that blocking malicious accounts is problematic if the decision is not transparent and publicly assessable [41]. We thus aim to empirically investigate this less studied platform intervention for better policy design.

To explain the relationship between a forwarding restriction policy and fake news dissemination, we argue that the strong ties and weak ties of an account difer with respect to their relational aspect [71]. Specifically, compared with weak ties, strong ties have a high level of emotional closeness and a strong proximate interpersonal relationship with the focal account [63,71]. When an account publishes a post whose authenticity is uncertain, strong ties tend to avoid forwarding that post by considering that the account may be punished with an activity restriction. For weak ties with less relational consideration, their forwarding behavior is less likely to be afected by a forwarding restriction policy. Taken together, there will be fewer direct forwards made by the strong ties but relatively more indirect forwards made by the weak ties, leading to less centralized and more dispersed dissemination of fake news. Therefore, we propose the following hypotheses:

H2a: Fake news is disseminated in a less centralized manner after the implementation of a forwarding restriction policy

H2b: Fake news is disseminated in a more dispersed manner after the implementation of a forwarding restriction policy.

In terms of influenceability, as discussed earlier, influential users’ forwarding behavior tends to be largely afected by reputational concerns because they feel more accountable for their behavior in the presence of a large audience. In other words, influential users decide to forward a post by considering whether this forwarding will harm their reputation or not. Unlike a fake news flag, which clearly alleviates the problem of sharing fake news by reducing its ambiguity, a forwarding restriction policy does not afect the forwarding behavior of influential users in a predictable direction. On the one hand, influential users may become more active in forwarding posts to protect the practice of free speech [5]. On the other hand, they may choose to share fewer posts to avoid forwarding fake news that would damage their reputation [4,13]. In line with this reasoning, we consider the efect of a forwarding restriction policy on the influenceability of fake news dissemination as an empirical question, and we do not formally propose a hypothesis here.

Using a forwarding restriction policy is an efective way to stop the spread of fake news, as it restricts the activities of the fake news publishing account instead of just warning others about fake news. Although our above hypotheses posit that fake news will be disseminated in a more dispersed manner with a forwarding restriction policy, the impact of fake news should be limited because the strong ties of the fake news publishing account are unlikely to forward fake news due to relational concerns. As a result, the number of fake news forwards will be significantly reduced, ultimately leading to the faster and earlier disappearance of the post. Therefore, we propose the following hypothesis:

H2c: Fake news has a shorter survival time after the implementation of a forwarding restriction policy.

The next section describes the empirical context and data to test the proposed hypotheses.

## Empirical Context and Data

## Sina Weibo and Sina Community Management Center

Sina Weibo is one of China’s largest and most popular microblogging websites. Launched by Sina Corporation on August 14, 2009, Sina Weibo has grown dramatically and had over 497 million monthly active users in the third quarter of 2019.<sup>10</sup> Faced with the growing threat of fake news, Sina Weibo launched a Community Management Center<sup>11</sup> in May 2012 to take advantage of the collective intelligence of community users to control the spread of fake news. The center relies on a social reporting system, through which users can report a post if they believe it to be harmful information (e.g., a threat to national security, misleading advertising, or obscene information), a message related to personal attacks, or fake news (“misinformation”).<sup>12</sup> This report is posted publicly, with details including the reporting user’s ID, reasons for reporting, reported post, and processing stage (e.g., stage of proof, judgment, and publicity).

According to Sina Weibo Community Management Regulations,<sup>13</sup> a reported post will be accepted for validation only if 1) the post has been forwarded more than 100 times or 2) the post has been reported by more than 10 users. We believe that this rule validates our study, as we can avoid issues such as malicious and indiscriminate reporting. We focus on posts that are reported and verified as fake news and exclude those being reported as harmful information, as the latter will be directly assessed and removed by the platform and will not be allowed to be freely distributed. We also exclude all posts related to personal attacks, as they do not necessarily contain fake content.

## Content-level and Account-level Platform Interventions on Sina Weibo

Using the launch of this Community Management Center, we focus on two interventions implemented by Sina Weibo: a content-level intervention, i.e., fake news flag, and an account-level intervention, i.e., forwarding restriction policy.

Sina Weibo introduced the fake news flag on May 28, 2012, alongside the launch of its Community Management Center. Fake news is flagged with a message stating that “this post is identified as fake” after being reported and verified. Along with this warning message, users can follow the hyperlink, which directs them to the web page of the Community Management Center. This page provides users with various information about the fake news post, including the reporting time, the reporter, the reported proof, and the assessment process. Figure 1 shows a screenshot of this assessment page.

On August 30, 2013, Sina Weibo implemented a forwarding restriction policy based on a credit scoring system. The credit scoring system punishes users with score deductions for misbehavior, such as publishing fake news, and the number of deductions increases with the number of fake news forwards. As the number of forwards increases, an account’s credit score will be continuously reduced until it reaches a certain low value and the account’s activities are restricted, e.g., posts can no longer be forwarded by others. Before August 30, 2013, no form of punishment prevented users from engaging with accounts with low credit scores. However, after the implementation of the forwarding restriction policy (August 30, 2013), accounts with a credit score of fewer than 60 points are restricted automatically by preventing their posts from being forwarded by others, regardless of the content. Accounts with a credit score of fewer than 40 points are further restricted by hiding all their posts from their followers. To emphasize again, the forwarding restriction policy intervention takes efect at the account level and naturally influences all posts from restricted accounts, even if the content is truthful. As this platform intervention is unexpected or unpredictable, we consider it an exogenous shock to platform users and examine its impact on the dissemination of both fake and truthful news. Figure 2 shows how the intervention works to prevent platform users from forwarding fake news.

![](/api/attachments/GRBMW4GS/fulltext/images/873ded67596457a125dfce79e2c685c684ce216700578a4ce21aea4ad03a495b.jpg)  
Figure 1. Fake News Assessment Page from Sina Weibo

![](/api/attachments/GRBMW4GS/fulltext/images/2b878d1d344434c6c341f51029546c7e025d3054c4810d5151e43212c6f31e3e.jpg)  
Figure 2. Forwarding Restriction Policy Intervention from Sina Weibo

## Sina Weibo Datasets

To analyze the efects of the two platform interventions on fake news, we obtain our datasets from Sina Weibo through its open API.<sup>14</sup> The Sina Weibo API provides a comprehensive interface to capture all relevant information of a post and its forwards. We restrict our sample to all posts published after June 2012, as the Community Management Center was oficially launched on May 28, 2012. We then focus on a 2-year period, from June 2012 to May 2014. We identify a set of known fake news posts from the Community Management Center and only focus on posts reported as fake news by users. Notably, in addition to user reporting, Sina Weibo proactively identifies fake news either manually or by using machine learning algorithms. These fake news posts are likely to be identified quickly after publication due to sensitive keywords and images and then be deleted immediately. Therefore, they are unlikely to be disseminated and are not appropriate for our analysis of fake news dissemination pattern and survival. This proactive detection of fake news can also be seen as a form of censorship and is out of our scope. Therefore, we limit our scope to only fake news identified by the social reporting system rather than the platform. Based on our screening process, our dataset contains 1,514 fake news posts and all their forward/comment messages from 409,020 Weibo users. This sample of fake news posts covers various topics such as local news, international politics, and life-related news. In addition, we collect over 50,000 truthful news posts published during the same sample period.

For each post, we have information on the number of forwards, comments, likes received, and pictures included. We also know from which source the post is published (e.g., iPhone, website, or desktop app). In addition to post-specific information, we obtain user-specific information, including gender, self-description, number of posts, number of followers, number of friends, verification status, location, and account age. For all fake news posts, we collect their reported date.

## Operationalization of Variables

We study two platform interventions that are represented by two variables. For the fake news flag, we define Marked as a binary variable indicating the time before and after the flag, with a value of 1 when a post was flagged as fake news and 0 otherwise. For the forwarding restriction policy, we define Restriction as equal to 1 if a post was published after the implementation date of the restriction (August 30, 2013) and 0 otherwise. Of the 1,514 fake news posts, 137 were published after the implementation of the forwarding restriction policy.

For variables that capture the post dissemination patterns, two are directly adopted from the literature and one is adapted with minor modifications [40]. Centrality is measured by the standardized out-degree centrality score of a post in its dissemination network. Influenceability is measured by the eigenvector centrality score of a post in its dissemination network. Dispersibility is measured by taking the reciprocal of the standardized closeness centrality score of a post. As mentioned earlier, previous studies have used structural virality to capture the dispersibility of the spread of fake news [69]. This measure considers the average distance between all pairs of nodes in the dissemination network and is less accurate and reliable than our proposed measure that only considers the average distance between the focal node and all other nodes. When measuring the dispersibility of a post, we treat its dissemination network as an undirected network because forwarding is unidirectional, which causes a problem when calculating the shortest paths between nodes. Note that Centrality and Dispersibility are defined in a relative sense, as the two variables are based on standardized scores, although their rates of change are diferent. For example, centrality can decrease dramatically without a significant increase in dispersibility if indirect forwards occur within a few degrees of the focal account.

Following Tang and Ng [66], we operationalize fake news survival by two variables: Discovery time and Stopping time. Discovery time is measured (in minutes) by the time between the published time and the reported time. It captures how fast a post is identified and reported to the platform as fake news. Stopping time is measured (in minutes) by the time between the reported time and the time of the last reply (either a forward or comment), which serves as a proxy for fake news survival rather than an exact measure. As fake news has an efect when people read, comment, and forward it, an exact survival time should be measured by the time between the reported time and the time when no more users interact with that fake news post. However, it is impossible to identify whether any individual has read that fake news post or not. Thus, we consider the last observable user engagement as the length of time that fake news can survive after being verified and labeled.

Fake is a binary variable indicating whether a post is a fake news or not. Finally, to account for the heterogeneity of the post and user characteristics, we use a comprehensive set of control variables. The definitions of all variables used in this study are summarized in Appendix A. The summary statistics of the fake news variables are reported in Table 2.

Table 2. Summary Statistics of Variables for Fake News

<table><tr><td></td><td colspan="4">Overall (n = 1,514)</td><td colspan="4">Before Restriction (n = 1,377)</td><td colspan="4">After Restriction (n = 137)</td></tr><tr><td>Variable Name</td><td>Mean</td><td>Std. Dev.</td><td>Max.</td><td>Min.</td><td>Mean</td><td>Std. Dev.</td><td>Max.</td><td>Min.</td><td>Mean</td><td>Std. Dev.</td><td>Max.</td><td>Min.</td></tr><tr><td>Stopping Time (in min.)</td><td>115,731</td><td>216,957</td><td>1,714,810</td><td>0</td><td>124,395</td><td>223,064</td><td>1,714,810</td><td>0</td><td>28,653</td><td>108,750</td><td>1,006,050</td><td>0</td></tr><tr><td>Discovery Time (in min.)</td><td>38,152</td><td>253,520</td><td>2,513,535</td><td>1</td><td>39,461</td><td>259,680</td><td>2,513,535</td><td>1</td><td>24,992</td><td>180,461</td><td>1,501,583</td><td>4</td></tr><tr><td>Centrality</td><td>0.540</td><td>0.196</td><td>0.981</td><td>0.075</td><td>0.543</td><td>0.189</td><td>0.981</td><td>0.100</td><td>0.517</td><td>0.254</td><td>0.965</td><td>0.075</td></tr><tr><td>Dispersibility</td><td>2.000</td><td>0.866</td><td>9.576</td><td>1.019</td><td>1.972</td><td>0.791</td><td>9.126</td><td>1.019</td><td>2.279</td><td>1.388</td><td>9.576</td><td>1.038</td></tr><tr><td>Influenceability</td><td>0.004</td><td>0.002</td><td>0.014</td><td>0.001</td><td>0.004</td><td>0.002</td><td>0.014</td><td>0.001</td><td>0.004</td><td>0.003</td><td>0.012</td><td>0.001</td></tr><tr><td>Forward</td><td>336</td><td>230</td><td>999</td><td>0</td><td>335</td><td>229</td><td>999</td><td>0</td><td>347</td><td>238</td><td>974</td><td>78</td></tr><tr><td>Comment</td><td>92</td><td>127</td><td>2629</td><td>0</td><td>90</td><td>128</td><td>2629</td><td>0</td><td>115</td><td>116</td><td>577</td><td>0</td></tr><tr><td>Like</td><td>11</td><td>41</td><td>605</td><td>0</td><td>5</td><td>16</td><td>605</td><td>0</td><td>68</td><td>111</td><td>605</td><td>0</td></tr><tr><td>Picture</td><td>0.935</td><td>0.726</td><td>9</td><td>0</td><td>0.907</td><td>0.676</td><td>9</td><td>0</td><td>1.212</td><td>1.074</td><td>7</td><td>0</td></tr><tr><td>Description</td><td>0.933</td><td>0.251</td><td>1</td><td>0</td><td>0.934</td><td>0.249</td><td>1</td><td>0</td><td>0.920</td><td>0.273</td><td>1</td><td>0</td></tr><tr><td>Gender</td><td>0.631</td><td>0.483</td><td>1</td><td>0</td><td>0.630</td><td>0.483</td><td>1</td><td>0</td><td>0.635</td><td>0.483</td><td>1</td><td>0</td></tr><tr><td>Message</td><td>17,664</td><td>30,933</td><td>358,663</td><td>0</td><td>17,837</td><td>31,792</td><td>358,663</td><td>0</td><td>15,925</td><td>20,389</td><td>107,017</td><td>0</td></tr><tr><td>Follower</td><td>345,527</td><td>1,184,097</td><td>26,630,301</td><td>17</td><td>335,779</td><td>1,190,912</td><td>26,630,301</td><td>17</td><td>443,505</td><td>1,112,658</td><td>7,591,558</td><td>19</td></tr><tr><td>Friend</td><td>1,044</td><td>893</td><td>4,981</td><td>0</td><td>1,043</td><td>886</td><td>4,981</td><td>0</td><td>1,055</td><td>965</td><td>4,745</td><td>17</td></tr><tr><td>Account Age (in hr.)</td><td>15,945</td><td>7,808</td><td>40,329</td><td>1</td><td>15,344</td><td>7,383</td><td>34,854</td><td>1</td><td>21,984</td><td>9,291</td><td>40,329</td><td>912</td></tr><tr><td>Length</td><td>110</td><td>44</td><td>193</td><td>3</td><td>111</td><td>44</td><td>193</td><td>3</td><td>94</td><td>48</td><td>172</td><td>9</td></tr><tr><td>Number</td><td>0.606</td><td>0.489</td><td>1</td><td>0</td><td>0.614</td><td>0.487</td><td>1</td><td>0</td><td>0.518</td><td>0.502</td><td>1</td><td>0</td></tr></table>

## Empirical Methodology

We first use two matching strategies to alleviate potential selection bias and heterogeneity concerns to examine how the two platform interventions afect fake news dissemination.

## Matching Strategies

## Content-Based Matching: Latent Semantic Analysis

The first matching strategy is based on the idea of textual similarity, in which we match fake news and truthful news so that they are semantically similar. The basic logic is to quantify the news content in a numerical representation using natural language processing techniques and then apply similarity measures (e.g., cosine similarity and Euclidean distance) to infer semantic similarity between news posts. This approach has been implemented in various applications, such as collaborative filtering [29], incident risk factor identification [60], business proximity analysis [61], copycat detection [70], and customer agility measurement [74].

We start with truthful news posts. Due to the highly noisy dataset, a preliminary step is implemented to manually remove all posts that are (1) meaningless (with only emojis, numbers, or fewer than five words), (2) advertisements, and (3) forwarded posts. We remove all meaningless posts because they are not suitable for our content-based matching strategy. We ignore advertisements to avoid comparison with fake news posts, which are expected to be diferent from truthful news posts. Finally, we exclude forwarded posts because they are used to construct the post dissemination network. As a result, we obtain 23,535 truthful news posts, which are matched to our 1,514 fake news posts for further processing. We then tokenize all posts into a bag-of-words dictionary and remove all stop words and punctuation. Thus, each post is represented by a word vector, and each vector value indicates the frequency of a word occurring in the corresponding post. The term frequency-inverse document frequency (TF-IDF) technique is applied to all posts to normalize their corresponding word vectors. The result is a word-by-post matrix, with each row representing a post, each column representing a unique word, and each cell representing the TF-IDF value of the word in the post.

Next, we apply latent semantic analysis (LSA)<sup>15</sup> to the word-by-post matrix to reduce the dimensionality and independency between words [39]. A dimensionality of 300 is chosen for LSA so that each word vector of a post is decomposed into a 300-dimensional feature vector. Finally, we match each fake news post to one or two truthful news posts based on the smallest angle calculated from the cosine similarity between their feature vectors. As a result, we obtain a matched sample of 1,586 truthful news posts and 1,514 fake news posts. The performance of the content-based matching method is reported in Appendix B1. Table 3 reports the summary statistics for truthful news posts after content-based matching.

## Post-Based Matching: Propensity Score Matching

Based on the content-based matched sample, we implement a second matching strategy to control for post and user characteristics using the propensity score matching (PSM) approach [53]. This strategy helps us remove non-comparable fake and truthful news posts to minimize estimation bias arising from the post and user characteristics. One-toone matching is implemented with a caliper size of 0.01. The matching procedures and performance assessment are reported in Appendix B2. With both matching strategies, we obtained a matched sample of 703 fake news posts and 703 truthful news posts for regression analysis.

Table 3. Summary Statistics of Variables for Truthful News After Content-Based Matching

<table><tr><td></td><td colspan="4">Overall (n = 1,586)</td><td colspan="4">Before Restriction (n = 1,246)</td><td colspan="4">After Restriction (n = 340)</td></tr><tr><td>Variable Name</td><td>Mean</td><td>Std. Dev.</td><td>Max.</td><td>Min.</td><td>Mean</td><td>Std. Dev.</td><td>Max.</td><td>Min.</td><td>Mean</td><td>Std. Dev.</td><td>Max.</td><td>Min.</td></tr><tr><td>Centrality</td><td>0.667</td><td>0.233</td><td>1.000</td><td>0.028</td><td>0.674</td><td>0.229</td><td>1.000</td><td>0.028</td><td>0.644</td><td>0.246</td><td>1.000</td><td>0.030</td></tr><tr><td>Dispersibility</td><td>1.583</td><td>0.818</td><td>16.746</td><td>1.000</td><td>1.561</td><td>0.651</td><td>8.727</td><td>1.000</td><td>1.665</td><td>1.250</td><td>16.746</td><td>1.000</td></tr><tr><td>Influenceability</td><td>0.006</td><td>0.050</td><td>1.000</td><td>0.001</td><td>0.006</td><td>0.041</td><td>1.000</td><td>0.001</td><td>0.009</td><td>0.076</td><td>1.000</td><td>0.001</td></tr><tr><td>Forward</td><td>463</td><td>250</td><td>999</td><td>13</td><td>449</td><td>251</td><td>999</td><td>13</td><td>514</td><td>242</td><td>982</td><td>13</td></tr><tr><td>Comment</td><td>198</td><td>329</td><td>5,285</td><td>0</td><td>183</td><td>307</td><td>5,285</td><td>0</td><td>253</td><td>393</td><td>4,816</td><td>0</td></tr><tr><td>Like</td><td>74</td><td>240</td><td>4,348</td><td>0</td><td>24</td><td>91</td><td>1,551</td><td>0</td><td>257</td><td>443</td><td>4,348</td><td>0</td></tr><tr><td>Picture</td><td>1.067</td><td>1.187</td><td>9</td><td>0</td><td>0.885</td><td>0.551</td><td>9</td><td>0</td><td>1.732</td><td>2.216</td><td>9</td><td>0</td></tr><tr><td>Description</td><td>0.970</td><td>0.170</td><td>1</td><td>0</td><td>0.967</td><td>0.178</td><td>1</td><td>0</td><td>0.982</td><td>0.132</td><td>1</td><td>0</td></tr><tr><td>Gender</td><td>0.602</td><td>0.490</td><td>1</td><td>0</td><td>0.601</td><td>0.490</td><td>1</td><td>0</td><td>0.603</td><td>0.490</td><td>1</td><td>0</td></tr><tr><td>Message</td><td>40,429</td><td>42,461</td><td>295,309</td><td>40</td><td>40,797</td><td>43,447</td><td>295,309</td><td>40</td><td>39,081</td><td>38,664</td><td>228,462</td><td>95</td></tr><tr><td>Follower</td><td>5,814,669</td><td>10,140,082</td><td>50,910,636</td><td>0</td><td>5,544,103</td><td>10,021,889</td><td>50,910,636</td><td>132</td><td>6,806,215</td><td>10,517,658</td><td>48,251,168</td><td>0</td></tr><tr><td>Friend</td><td>805</td><td>849</td><td>5,000</td><td>0</td><td>805</td><td>838</td><td>5,000</td><td>0</td><td>807</td><td>891</td><td>5,000</td><td>0</td></tr><tr><td>Account Age (in hr.)</td><td>20,138</td><td>8,886</td><td>39,985</td><td>1</td><td>18,364</td><td>7,841</td><td>34,933</td><td>1</td><td>26,641</td><td>9,457</td><td>39,985</td><td>1,386</td></tr><tr><td>Length</td><td>113</td><td>41</td><td>226</td><td>10</td><td>112</td><td>41</td><td>226</td><td>10</td><td>116</td><td>41</td><td>194</td><td>14</td></tr><tr><td>Number</td><td>0.512</td><td>0.500</td><td>1</td><td>0</td><td>0.509</td><td>0.500</td><td>1</td><td>0</td><td>0.524</td><td>0.500</td><td>1</td><td>0</td></tr></table>

## Regression Analysis

We first use the fake news flag intervention implemented by Sina Weibo to establish the causal impact of the platform intervention on fake news dissemination. As the fake news flag is only applied to fake news but not truthful news, we can consider a quasi-experimental design based on a matched DiD sample to tease out unobservable characteristics of posts that may bias our estimation [10,37]. The matched sample of truthful news posts is then used as the quasi-control group to reveal the impact of flagging on fake news dissemination. The following model specification is estimated:

$$
\text { Dissemination } _ {i t} = \beta_ {0} + \beta_ {1} \text { Fake } _ {i} + \beta_ {2} \text { Marked } _ {t} + \beta_ {3} \text { Fake } _ {i} \times \text { Marked } _ {t} + \varepsilon_ {i t},\tag{1}
$$

where Disseminatio $n _ { \mathrm { i t } }$ is one of the three dissemination variables of post i measured up to time t, Fake<sub>i</sub> indicates whether post i is fake news, Marked<sub>t</sub> is coded as 0 if t is before the flagged time and 1 otherwise, and t represents the daily time range from three days before to three days after the flagged time. A major challenge is that fake news posts have diferent discovery and end times. For instance, one fake news post may be identified three days after its publication and stop spreading five days after, and another fake news post may be identified two months after its publication and stop spreading one month later. To overcome this challenge, we focus on the dissemination patterns three days before and three days after the flagged date of a fake news post, which corresponds to one week. To do so, we perform time matching between the matched fake news and truthful news pairs to align the unflagged period before the fake news post is identified. Figure 3 illustrates our identification strategy. Consider a pair of matched posts. The fake news post was published on April 12, 2013, and discovered on May 12, 2013, and the truthful news post was published on February 28, 2013. We compare the dissemination patterns of the fake news post three days before and after May 12, 2013. As it took 30 days for the fake news post to be discovered, we also use 30 days to identify a matched period of the matched truthful news post for comparison. From Figure 3, we subsample fake news posts between May 9, 2013, and May 15, 2013, and truthful news posts between March 27, 2013, and April 2, 2013, and specify a DiD strategy during this matched period. As some fake news posts only last for a very short time (e.g., less than a day), we exclude these and their matched truthful news posts, which leads to a matched sample of 1,014 pairs for our DiD analysis.

![](/api/attachments/GRBMW4GS/fulltext/images/c16083c89e4dcdb6720a717140708f30de7983f67efe912aa8890a8dea6ca0a6.jpg)  
Figure 3. Illustration of the Identification Strategy for the Fake News Flag

![](/api/attachments/GRBMW4GS/fulltext/images/bafdb66120efd257b8eccfa9af26b066f5610bc2fd4f5e32a6ccd2e21140d032.jpg)  
We compare matched fake and truthful news before and after the implementation of the forwarding restrictionpolicy  
Figure 4. Illustration of the Identification Strategy for the Forwarding Restriction Policy

Our next model uses the forwarding restriction policy intervention implemented on August 30, 2013. As this intervention afects both fake and truthful news, we are interested in examining its diferent impacts on the dissemination of fake and truthful news. Our regression framework is specified below:

$$
\begin{array}{l} \text { Dissemination } _ {i t} = \beta_ {0} + \beta_ {1} \text { Fake } _ {i} + \beta_ {2} \text { Restriction } _ {t} + \beta_ {3} \text { Fake } _ {i} \times \text { Restriction } _ {t} + \text { ControlVars } _ {i} \\ \quad + \gamma_ {t} + \varepsilon_ {i t}, \end{array}\tag{2}
$$

where Disseminatio $\iota _ { i t }$ is one of the three dissemination variables of post i published at time t, measured up to the post’s end time; Restriction is coded as 0 if t is before the implementation date of the forwarding restriction policy and 1 otherwise; ControlVars<sub>i</sub> represents time-invariant post control variables; $\gamma _ { t }$ represents week fixed efects; and t represents the daily time range throughout our analysis period. The coeficient of the interaction term revealed by $\beta _ { 3 }$ helps us to determine how fake news is disseminated after the forwarding restriction policy is implemented. We use our matched sample of 1,406 pairs obtained from the content-based and post-based matching approaches for this model specification. An illustration of this analysis framework is presented in Figure 4.

Finally, to examine the impact of the forwarding restriction policy on fake news survival, we specify two regression frameworks for a more comprehensive analysis. The first regression is an ordinary least squares (OLS) regression specified below:

$$
\text { Time } _ {i t} = \beta_ {0} + \beta_ {1} \text { Restriction } _ {t} + \text { ControlVars } _ {i} + \gamma_ {t} + \varepsilon_ {i t},\tag{3}
$$

where $T i m e _ { i t }$ represents either the logarithm of Discovery time or Stopping time of fake news i measured at time t, and t represents the daily time range throughout our analysis period. The advantage of this framework is that we can incorporate time fixed efects $\gamma _ { t }$ to account for potential time-induced and trend efects. The second regression is a Cox proportionalhazards framework commonly used to investigate how multiple covariates are simultaneously related to survival time:

$$
h \left(\text { Time } _ {i t}\right) = h _ {0} \left(\text { Time } _ {i t}\right) \times \exp \left(\beta_ {1} \text { Restriction } _ {t} + \text { ControlVars } _ {i}\right),\tag{4}
$$

where $h ( \cdot )$ is the hazard function and $h _ { 0 } ( . )$ the baseline hazard function with all variables set to 0. This framework is a natural choice because our variable of interest is the survival time of fake news. However, the two limitations of this framework are the lack of data censoring, as all fake news posts are eventually identified, and the proportional hazards assumption, which precludes the incorporation of time fixed efects. Therefore, we implement both frameworks to complement each other’s limitations for a robust analysis of the impact of this platform intervention.

![](/api/attachments/GRBMW4GS/fulltext/images/b767ffa66eab875ec5cfcb44a6bb500dda5885b5baa9da250a12317126137f54.jpg)

![](/api/attachments/GRBMW4GS/fulltext/images/09f49bc364572390bb67d72a718662ac6db6019c883f1d0c3b0e13a3985b7e5f.jpg)

![](/api/attachments/GRBMW4GS/fulltext/images/6596e02ba3ec1a446fe0c0a03f4f42c13b93db968eadf5239c804c79a008e96f.jpg)  
Figure 5. Model-Free Evidence of the Efect of the Fake News Flag on Fake News Dissemination

Table 4. Efect of the Fake News Flag on Fake News Dissemination

<table><tr><td></td><td>Centrality</td><td>Dispersibility</td><td>Influenceability</td></tr><tr><td>Fake</td><td>-0.007(0.005)</td><td>0.017(0.030)</td><td>-0.093***(0.030)</td></tr><tr><td>Marked</td><td>0.000(0.007)</td><td>0.000(0.032)</td><td>0.000(0.033)</td></tr><tr><td> $Fake \times Marked$ </td><td>0.055***(0.012)</td><td>-0.250***(0.045)</td><td>0.903***(0.012)</td></tr><tr><td>Log Likelihood</td><td>68</td><td>-9,639</td><td>-9,788</td></tr><tr><td>Observations</td><td>1,014</td><td>1,014</td><td>1,014</td></tr></table>

Notes. \*, \*\* and \*\*\* indicate statistical significance at the 10%, 5% and 1% levels, respectively. Standard errors are displayed in parentheses under the coeficient estimates.

## Results

## Efect of the Fake News Flag on Fake News Dissemination

We present the results of our main analyses in this section. We first assess the parallel trend assumption in Figure 5. Figure 5 shows a sharp change in centrality, dispersibility, and influenceability after the intervention, which provides us with model-free evidence of the efect of the fake news flag. We also analyze pre-treatment trends to verify the parallel trend assumption and report the results in Appendix C. Table 4 reports the DiD regression results. We find that the intervention has a positive and significant impact on the centrality $( \beta = 0 . 0 5 5 , p < 0 . 0 1 )$ of fake news, which means that after a fake news post is flagged as such, it is more likely to be disseminated through direct forwards (H1a is supported). We also find that the flag has a significant and negative efect on the dispersibility $( \beta = - 0 . 2 5 0 , p \mathrm { < } 0 . 0 1 )$ of fake news, which means that fake news is less likely to be forwarded to distant others after the intervention (H1b is supported). Moreover, the intervention has a significant and positive impact on the influenceability $( \beta = 0 . 9 0 3 , p < 0 . 0 1 )$ of fake news. In other words, the flag encourages influential users to forward fake news posts (H1c is supported).

To identify the underlying mechanism, we test whether the ambiguity of fake news decreases after being flagged as such. We perform a content analysis on all fake news forwarding comments. We use a popular psycholinguistic dictionary, the Linguistic Inquiry and Word Count (LIWC) constructed by Tausczik and Pennebaker [67], to infer the extent of ambiguity for each fake news forwarding comment [27, 28]. We consider the two most

Table 5. Ambiguity Analysis

<table><tr><td>Condition</td><td>Tentative Word Usage</td><td>Affective Word Usage</td></tr><tr><td>Before fake news flag</td><td>0.137 (0.401)</td><td>7.282 (5.595)</td></tr><tr><td>After fake news flag</td><td>0.100 (0.339)</td><td>5.036 (5.456)</td></tr><tr><td>Within-subject t-test</td><td>2.671***</td><td>13.048***</td></tr><tr><td>Observations</td><td>1,250</td><td>1,250</td></tr></table>

Notes. \*\*\* indicates statistical significance at the 1% level. Mean values are displayed with standard errors in parentheses.

<sub>8</sub>.W<sup>e</sup>l<sup>comeon-s</sup>i<sup>teconsu</sup> <sub>money</sub>. <sub>Ch</sub>i<sub>na’s</sub> <sub>Bone</sub> <sub>Mar</sub><sup>row</sup> <sup>Bank</sup> <sup>w</sup>ill <sup>ho</sup>l<sup>d</sup> <sup>an</sup> <sup>open</sup>i<sup>ng</sup> <sup>day</sup> ill <sub>be</sub> <sub>refunded</sub> <sub>and</sub> <sub>any</sub> <sub>defic</sub>i<sub>t</sub> <sub>w</sub>ill <sub>be</sub> <sub>repa</sub>i<sub>d</sub>. <sup>The</sup> <sup>Bone</sup> <sup>Ma</sup> <sub>used</sub> <sub>for</sub> <sub>transportat</sub>i<sub>on,</sub> <sub>co</sub>ll<sub>ect</sub>i<sub>on,</sub> <sub>an</sub>d <sup>other</sup> <sup>donor</sup> <sup>expe</sup> i<sub>nc</sub>i<sub>p</sub>l<sub>e</sub> <sub>that</sub> <sub>donors</sub> <sub>shou</sub>l<sub>d</sub> <sub>not</sub> <sub>meet</sub> <sub>pa</sub>ti<sup>ents,</sup> <sup>we</sup> <sup>co</sup>ll<sup>ect</sup> <sup>20,</sup> <sub>as</sub> <sub>never</sub> <sub>charged</sub> i<sub>t</sub>. <sub>The</sub> <sub>number</sub> <sub>“50,000</sub> y<sup>uan”</sup> i<sup>s</sup> <sup>a</sup>l<sup>so</sup> <sup>wro</sup> <sub>bank,</sub> <sub>wh</sub>i<sub>ch</sub> i<sub>s</sub> <sub>current</sub>l<sub>y</sub> <sub>funded</sub> <sup>by</sup> <sup>the</sup> <sup>financ</sup>i<sup>a</sup>l <sup>department</sup> <sub>arro</sub>w <sup>Bank</sup> <sup>search</sup> i<sup>s</sup> <sup>free</sup>: <sup>500</sup> <sup>yuan</sup> i<sup>s</sup> <sup>the</sup> <sup>HLA</sup> <sup>typ</sup>i<sup>ng</sup> <sup>test</sup> <sup>fee</sup>

i<sub>nnosuke</sub> <sub>Nohara</sub> i<sub>s</sub> <sub>to</sub> <sub>be</sub> <sub>b</sub>l<sub>a</sub>m<sup>ed</sup> <sup>for</sup> <sup>post</sup>i<sup>ng</sup> <sup>th</sup>i <sub>as</sub> <sub>prov</sub>i<sub>ded</sub> <sub>b</sub>y <sup>th</sup>i<sup>s</sup> <sup>s</sup>i<sup>ng</sup>l<sup>e</sup> <sup>user,</sup> <sup>and</sup> i<sup>ts</sup> <sup>factua</sup>li<sup>ty</sup> <sup>cou</sup>l<sup>d</sup> <sup>n</sup> <sub>ce</sub> <sub>forwarded</sub> <sub>th</sub>i<sub>s</sub> <sub>post</sub>. <sub>At</sub> <sub>around</sub> <sub>12</sub> <sub>p</sub>.m.<sup>,</sup> <sup>the</sup> <sup>ch</sup>il<sup>d</sup> <sup>w</sup> l<sub>aza</sub> <sub>South</sub> <sub>Road,</sub> <sub>Nanchang</sub> <sub>C</sub>i<sub>ty,</sub> <sub>J</sub>i<sub>angx</sub>i <sub>Prov</sub>i<sub>nce</sub>. <sub>So</sub>m<sup>e</sup> <sup>ce</sup> <sub>edaughterofh</sub>i<sub>s/herfr</sub>i<sub>end’scowor</sub>k<sup>erwasabducted</sup> <sub>ce,</sub> <sub>the</sub> i<sub>nformat</sub>i<sub>on</sub> <sub>source</sub> i<sub>s</sub> i<sub>dent</sub>i<sub>fied</sub>: <sub>user</sub> @<sup>storm0109</sup> <sup>repo</sup>

<sub>s</sub> <sub>ca</sub>ll<sub>ed</sub> <sub>“Sunsh</sub>i<sub>ne</sub> <sub>Mar</sub><sup>row</sup> <sub>marro</sub>w <sup>bank</sup>. <sup>From</sup> i<sup>nqu</sup>i<sup>ry</sup> <sup>to</sup> <sup>transp</sup>l<sup>antat</sup>i<sup>on,</sup> <sup>the</sup> <sup>process</sup> i <sub>marro</sub>w! <sup>Therefore,</sup> <sup>Pek</sup>i<sup>ng</sup> <sup>Un</sup>i<sup>vers</sup>i<sup>ty</sup> <sup>students</sup> <sup>were</sup> <sup>outrag</sup> <sub>at</sub>i<sub>ent</sub> will <sup>be</sup> <sup>charged</sup> <sup>500</sup> <sup>yuan</sup> <sup>for</sup> <sup>each</sup> i<sup>nqu</sup>i<sup>ry</sup> <sup>and</sup> <sup>at</sup> l<sup>east</sup> <sup>5</sup> <sub>nts,</sub> <sub>they</sub> <sub>w</sub>ill <sub>contact</sub> <sub>vo</sub>l<sub>unteers</sub> <sub>to</sub> <sub>donate</sub> <sub>bone</sub> m<sup>arrow</sup>. <sup>H</sup> i<sub>ons</sub>i<sub>nthenameofchar</sub>i<sub>tyandc</sub>r<sup>eatesabankofsamp</sup>l<sup>e</sup> <sub>arro</sub>w <sup>Bank,</sup> <sup>sponsored</sup> <sup>by</sup> <sup>the</sup> <sup>Red</sup> <sup>Cross</sup> <sup>Soc</sup>i<sup>ety</sup> <sup>of</sup> <sup>Ch</sup>i<sup>na,</sup>

<sub>rket</sub> i<sub>n</sub> <sub>X</sub>i<sub>ao</sub>l<sub>an</sub>. I <sub>hope</sub> <sub>more</sub> <sub>peop</sub>l<sub>e</sub> <sub>can</sub> <sub>fo</sub>ll<sub>o</sub>w <sup>and</sup> <sup>forw</sup> <sub>o</sub> m<sup>y</sup> <sup>best</sup> <sup>to</sup> <sup>get</sup> <sup>your</sup> <sup>attent</sup>i<sup>on</sup>. <sup>Th</sup>i<sup>s</sup> <sup>ch</sup>il<sup>d</sup> <sup>has</sup> <sup>just</sup> <sup>been</sup> <sup>abd</sup> <sub>ot</sub> <sub>a</sub> <sub>ce</sub>l<sub>ebr</sub>i<sub>ty,</sub> I <sub>not</sub>i<sub>ce</sub> <sub>that</sub> <sub>there</sub> <sub>are</sub> <sub>more</sub> <sup>and</sup> <sup>more</sup> <sup>bad</sup> <sup>peop</sup>l

relevant word categories: Tentative and Afect. We expect the reduced ambiguity of fake news after being flagged to be reflected by the reduced use of tentative words, such as “maybe,” “perhaps,” and “guess,” in forwarding comments. We also expect a reduced use of afective words in forwarding comments, as ambiguity is strongly associated with various emotions such as anxiety and worry [9,16]. We only focus on fake news with forwarding comments containing at least one tentative or afective word, resulting in a sample of 1,250 fake news posts for analysis. We then perform a within-subjects t-test to statistically compare the proportions of tentative or afective words used in fake news forwarding comments before and after the implementation of the fake news flag. Table 5 shows a significant decrease in the use of tentative and afective words in forwarding comments after a post is flagged as fake news, which supports our conjecture that the fake news flag can reduce the ambiguity of fake news.

Table 7. Efect of the Forwarding Restriction Policy on Fake News Dissemination

<table><tr><td></td><td colspan="2">Centrality</td><td colspan="2">Dispersibility</td><td colspan="2">Influenceability</td></tr><tr><td>Fake</td><td>0.042(0.029)</td><td>0.108(0.103)</td><td>-0.182(0.119)</td><td>-0.450(0.424)</td><td>-0.230***(0.068)</td><td>0.051(0.240)</td></tr><tr><td>Restriction</td><td>-0.058(0.090)</td><td>-0.069(0.101)</td><td>0.356(0.366)</td><td>0.248(0.413)</td><td>-0.298(0.211)</td><td>-0.259(0.233)</td></tr><tr><td> $Fake \times Restriction$ </td><td></td><td>-0.338*(0.179)</td><td></td><td>1.471**(0.736)</td><td></td><td>-0.102(0.416)</td></tr><tr><td> $ln(Forward)$ </td><td>-0.102***(0.008)</td><td>-0.098***(0.008)</td><td>0.274***(0.034)</td><td>0.259***(0.035)</td><td>-0.879***(0.020)</td><td>-0.894***(0.020)</td></tr><tr><td> $ln(Comment)$ </td><td>0.068***(0.006)</td><td>0.067***(0.006)</td><td>-0.104***(0.026)</td><td>-0.108***(0.026)</td><td>-0.095***(0.015)</td><td>-0.095***(0.015)</td></tr><tr><td> $ln(Like)$ </td><td>0.005(0.006)</td><td>0.009(0.006)</td><td>-0.084***(0.022)</td><td>-0.075***(0.023)</td><td>-0.041***(0.013)</td><td>-0.021(0.013)</td></tr><tr><td> $ln(Picture)$ </td><td>-0.010(0.023)</td><td>-0.012(0.023)</td><td>-0.201**(0.094)</td><td>-0.143(0.093)</td><td>0.220***(0.054)</td><td>0.252***(0.053)</td></tr><tr><td>Description</td><td>0.018(0.025)</td><td>0.002(0.025)</td><td>-0.206**(0.102)</td><td>-0.160(0.101)</td><td>-0.055(0.059)</td><td>-0.050(0.057)</td></tr><tr><td>Gender</td><td>0.034***(0.011)</td><td>0.033***(0.010)</td><td>-0.079*(0.043)</td><td>-0.089**(0.042)</td><td>0.009(0.025)</td><td>0.015(0.024)</td></tr><tr><td> $ln(Message)$ </td><td>-0.018***(0.004)</td><td>-0.012***(0.004)</td><td>0.115***(0.017)</td><td>0.122***(0.018)</td><td>-0.043***(0.010)</td><td>-0.037***(0.010)</td></tr><tr><td> $ln(Follower)$ </td><td>0.039***(0.003)</td><td>0.041***(0.003)</td><td>-0.152***(0.012)</td><td>-0.155***(0.012)</td><td>0.042***(0.007)</td><td>0.034***(0.007)</td></tr><tr><td> $ln(Friend)$ </td><td>-0.020***(0.004)</td><td>-0.017***(0.004)</td><td>0.036**(0.018)</td><td>0.030*(0.018)</td><td>-0.009(0.010)</td><td>0.000(0.010)</td></tr><tr><td> $ln(Account Age)$ </td><td>0.001(0.007)</td><td>-0.006(0.007)</td><td>-0.041(0.029)</td><td>-0.027(0.030)</td><td>-0.011(0.017)</td><td>-0.024(0.017)</td></tr><tr><td> $ln(Length)$ </td><td>0.002(0.009)</td><td>0.009(0.008)</td><td>-0.004(0.035)</td><td>-0.026(0.035)</td><td>0.015(0.020)</td><td>0.008(0.020)</td></tr><tr><td>Number</td><td>0.003(0.011)</td><td>0.005(0.011)</td><td>-0.068(0.044)</td><td>-0.061(0.044)</td><td>0.035(0.026)</td><td>0.055**(0.025)</td></tr><tr><td>Verified Type</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Location</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Source</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Week Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Log Likelihood</td><td>662</td><td>761</td><td>-1,305</td><td>-1,223</td><td>-529</td><td>-420</td></tr><tr><td>Observations</td><td>1,406</td><td>1,406</td><td>1,406</td><td>1,406</td><td>1,406</td><td>1,406</td></tr></table>

Notes. 1. \*, \*\* and \*\*\* indicate statistical significance at the 10%, 5% and 1% levels, respectively. Standard errors are displayed in parentheses under the coeficient estimates  
2. For fake news, the sample sizes before and after restriction are 623 and 80, respectively. For truthful news, the sample sizes before and after restriction are 586 and 117, respectively.

In summary, we find that the fake news flag leads the fake news dissemination network to be more centralized through direct forwards than dispersed through indirect forwards. These results confirm our theorization based on the basic law of rumor [35] that flagging fake news can reduce its ambiguity and prevent it from being disseminated farther and deeper. In terms of the efect of the fake news flag on fake news influenceability, influential users with a large number of followers are expected to behave more cautiously. Therefore, they tend to avoid disseminating an ambiguous post until it has been verified. The increased influenceability of fake news after the implementation of the fake news flag highlights the efort of influential users to help dispel fake news. Table 6 qualitatively supports this claim, as we find that influential users forward fake news posts with an intention to confirm their falsehood. In short, the fake news flag significantly alters the spread of fake news by generating more direct than indirect forwards, causing fake news posts to be disseminated more by influential users.

## Efect of the Forwarding Restriction Policy on Fake News Dissemination

We now examine the impact of the forwarding restriction policy on post dissemination patterns. We first provide a descriptive analysis to understand how the forwarding restriction policy shapes the post dissemination network. We randomly select 24 fake news and 24 truthful news dissemination networks before and after the intervention for visual comparison, as shown in Appendix D. Before the intervention, the fake news dissemination networks were more centralized, and only a relatively small portion spread to distant accounts. A similar pattern can be observed for truthful news, with their dissemination network showing high centrality but low dispersibility. In general, both fake news and truthful news dissemination networks involved some degree of influenceability. However, after the implementation of the forwarding restriction policy, a clear distinction can be observed: the fake news dissemination networks become more dispersed with longer tails (i.e., more indirect forwards) and less centralized (i.e., fewer direct forwards). We observe no significant change in the truthful news dissemination networks from before to after the intervention. In short, the visualization of these networks is consistent with our expectation that the forwarding restriction policy influences fake news and truthful news diferently.

We present the regression results in Table 7. The significant and negative coeficient of $F a k e \times R e s t r i c t i o n$ on the centrality $( \beta = - 0 . 3 3 8 , \ p < 0 . 1 )$ of fake news indicates that compared with truthful news, fake news is disseminated via less direct forwards after the implementation of the forwarding restriction policy (H2a is supported). However, the significant and positive coeficient of Fake × Restriction on the dispersibility $( \beta = 1 . 4 7 1$ $\textstyle P ^ { < } 0 . 0 5 )$ of fake news suggests that compared with truthful news, fake news is disseminated in a more dispersed manner after the intervention (H2b is supported). We find no significant efect $( \beta = - 0 . 1 0 2 , p > 0 . 1 )$ of the forwarding restriction policy on the influenceability of fake news. Taken together, the forwarding restriction policy leads to significantly less centralized and more dispersed dissemination of fake news as compared with truthful news.

The above results are consistent with our theorization based on the social tie theory. After the implementation of the forwarding restriction policy, the strong ties of fake news publishing accounts are prevented from forwarding fake news posts by relational concerns, whereas their weak ties are not afected by relational concerns and continue to forward fake news posts. Thus, the dissemination of fake news becomes less centralized and more dispersed than truthful news.

## Robustness Checks

We run two additional tests to check whether the impact of the forwarding restriction policy on fake news dissemination changes based on the topic and sentiment. The results are reported in Appendix E. We find that the forwarding restriction policy only afects liferelated fake news posts but does not afect international and local fake news posts (Table E2). Relational concerns are not likely to occur among the strong ties of fake news publishing accounts that publish international and local fake news, as these types of posts have more efect on society than life-related fake news posts. This finding indirectly supports our proposed mechanism of relational concerns arising from strong ties. In addition, we find that fake news sentiment does not afect the dissemination patterns of fake news, which confirms that the identified efect is not driven by the emotions expressed in the content of fake news (Table E4).

Another major concern regarding the dissemination of fake news is whether social bot accounts spread fake news on social media on a large scale [59]. Previous research has shown that social bots play a significant role in promoting fake news that distorts various social events [6], such as the 2016 U.S. election. However, this is not a concern in our study due to the real-name policy implemented by Sina Weibo since 2011.<sup>16</sup> The policy states that Weibo users must verify their accounts by using their real names for account registration. This policy was formally launched on March 3, 2012, before our analysis period. According to this real-name policy, accounts registered without real-name verification can only read posts on Weibo but cannot publish, comment, or forward posts. We believe that the realname policy alleviates the concern that our findings might be contaminated by social bots.

In summary, this study reveals that the fake news flag and the forwarding restriction policy have diferent efects on fake news dissemination. In a broader sense, the fake news flag (content-level intervention) afects the spread of fake news by reducing its ambiguity, leading to more centralized and less dispersed dissemination of fake news and more forwards by influential users. The forwarding restriction policy (account-level intervention) creates relational concerns among the strong ties of fake news publishing accounts, leading to less centralized and more dispersed dissemination of fake news. These findings provide insights into the efectiveness of diferent types of platform interventions in fake news mitigation.

## Efect of the Forwarding Restriction Policy on Fake News Survival

As little research focuses on the impact of account-level interventions (e.g., forwarding restriction policy), we conducted an additional analysis to examine how the forwarding restriction policy influences fake news survival, which is a more direct way to examine the efectiveness of this type of intervention. We report the results in Table 8. As the lifespans of some fake news posts may overlap with the intervention implementation date, we remove these posts for a more robust analysis, which reduces our sample to 1,368 fake news posts. We obtain consistent results across the two regression models. For the linear regression model, the significant and negative coeficient of Restriction on Stopping time $( \beta = - 8 . 7 7 9 .$

Table 8. Efect of the Forwarding Restriction Policy on Fake News Surviva

<table><tr><td rowspan="2"></td><td colspan="2">OLS</td><td colspan="2">Cox Proportional-Hazards Model</td></tr><tr><td>log(Stopping Time)</td><td>log(Discovery Time)</td><td>Stopping Hazard</td><td>Discovery Hazard</td></tr><tr><td>Restriction</td><td>-8.779***(2.848)</td><td>-0.673(2.341)</td><td>0.899***(0.154)</td><td>0.013(0.122)</td></tr><tr><td>log(Forward)</td><td>0.817***(0.142)</td><td>-0.010(0.116)</td><td>-0.427***(0.052)</td><td>-0.098*(0.052)</td></tr><tr><td>log(Comment)</td><td>-0.175*(0.099)</td><td>-0.106(0.081)</td><td>0.037(0.039)</td><td>0.051(0.039)</td></tr><tr><td>log(Like)</td><td>0.148(0.094)</td><td>0.013(0.077)</td><td>0.082**(0.037)</td><td>0.081**(0.032)</td></tr><tr><td>log(Picture)</td><td>0.042(0.436)</td><td>0.267(0.359)</td><td>0.651***(0.170)</td><td>-0.216(0.146)</td></tr><tr><td>Description</td><td>-0.359(0.339)</td><td>0.355(0.278)</td><td>-0.108(0.142)</td><td>-0.085(0.120)</td></tr><tr><td>Gender</td><td>-0.311*(0.167)</td><td>-0.011(0.138)</td><td>0.130*(0.072)</td><td>-0.002(0.063)</td></tr><tr><td>log(Message)</td><td>-0.147***(0.056)</td><td>-0.001(0.046)</td><td>0.100***(0.024)</td><td>-0.009(0.020)</td></tr><tr><td>log(Follower)</td><td>-0.058(0.050)</td><td>0.033(0.041)</td><td>-0.061***(0.021)</td><td>0.001(0.017)</td></tr><tr><td>log(Friend)</td><td>0.068(0.070)</td><td>-0.083(0.057)</td><td>-0.019(0.031)</td><td>0.023(0.025)</td></tr><tr><td>log(Account Age)</td><td>0.157(0.112)</td><td>-0.166*(0.092)</td><td>0.089*(0.048)</td><td>0.050(0.039)</td></tr><tr><td>log(Length)</td><td>-0.073(0.128)</td><td>0.279***(0.106)</td><td>-0.077(0.052)</td><td>-0.106**(0.045)</td></tr><tr><td>Number</td><td>0.005(0.179)</td><td>-0.275*(0.147)</td><td>0.137*(0.077)</td><td>0.053(0.066)</td></tr><tr><td>Verified Type</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Location</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Source</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Week Fixed Effect</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Log Likelihood</td><td>-3,111</td><td>-2,843</td><td>-8,244</td><td>-8,535</td></tr><tr><td>Observations</td><td>1,368</td><td>1,368</td><td>1,368</td><td>1,368</td></tr></table>

Notes. \*, \*\* and \*\*\* indicate statistical significance at the 10%, 5% and 1% levels, respectively. Standard errors are displayed in parentheses under the coeficient estimates.

$p { < } 0 . 0 1 )$ indicates that fake news has a shorter average survival time after the intervention. In the Cox proportional-hazards model analysis, the positive and significant coeficient of Restriction on Stopping time $( \beta = 0 . 8 9 9 , p < 0 . 0 1 )$ suggests a higher hazard rate of fake news after the intervention. Specifically, the expected hazard of fake news increases by 146% after the intervention, compared with that before the intervention. We find no evidence of the impact of the forwarding restriction policy on the discovery time of fake news. In all cases, we examine the Kaplan-Meier curves of the Cox proportional-hazards models and find no violation of the proportional hazard assumption [26].

We find that the forwarding restriction policy efectively combats the spread of fake news by shortening its lifespan because relational concerns of strong ties prevent the further spread of fake news. However, the forwarding restriction policy has no efect on the discovery time of fake news, likely because there are no relational concerns before the verification of fake news. We also conduct a placebo test by repeating the same regression analyses on truthful news as a robustness check and find that the forwarding restriction policy has no efect on the lifespan of truthful news. The placebo test is presented in Appendix F.

Overall, after the implementation of the forwarding restriction policy, 1) fake news is disseminated in a less centralized and more dispersed manner, compared with truthful news, and 2) fake news survives for a much shorter time but is not discovered sooner. These findings have several implications for social media platforms, as they show how the account-level intervention afects user engagement with fake news and suggest that this type of platform intervention can efectively mitigate fake news by shortening its survival time.

## Discussion

## Contributions

The study makes two main contributions to the literature. First, we extend the fake news literature by establishing a causal relationship between the fake news flag and fake news dissemination using empirical field data. To the best of our knowledge, previous studies have mainly focused on the cognitive and psychological impacts of the fake news flag by using experimental laboratory data, and few have addressed the actual behavior change caused by this flag. Thus, we complement the literature by using field data and providing causal empirical evidence to better understand the efectiveness of the fake news flag.

Second, we extend the literature on platform interventions that target fake news by examining the impact of the forwarding restriction policy on fake news dissemination and survival time. Previous studies have mainly focused on the content-level intervention (i.e., fake news flag) from a cognitive perspective to reduce people’s willingness to engage with fake news [25]. We find that the forwarding restriction policy, a type of stricter platform intervention applied at the account level, can shorten the survival time of fake news, with no detrimental efect on the dissemination of truthful news. Furthermore, we highlight the diferent impacts of the two interventions on fake news dissemination, thereby solving a conundrum that has never been adequately addressed. This missing piece of the puzzle advances our understanding of the efectiveness of platform interventions by providing a holistic view of how content-level and account-level interventions work diferently to combat the spread of fake news.

From a practical perspective, our findings provide important insights for online platform owners and policymakers. Today, the Internet and social media have become the primary sources of information consumption for most people. Online platforms are important mediators that ensure the quality of information to prevent consumers from exposure to misleading and manipulative news. However, the efectiveness and eficacy of platform interventions are questionable [41], and more efort should be devoted to better understanding how diferent policies work. Our study responds to this call by empirically examining the efects of two platform interventions in a rigorous framework. Our analysis of the fake news flag provides a result consistent with that of Moravec et al. [45], indicating that people continue to forward fake news posts even after they are identified as fake news. Our proposed mechanism is supported, showing that the fake news flag reduces the ambiguity of fake news posts and, therefore, helps control the spread of fake news within a smaller network, i.e., direct forwards within one degree of separation. However, our findings also suggest a possible consequence of the increased echo chamber, as the flagged fake news posts are likely to be forwarded more by like-minded people [38], adversely reinforcing polarization and fueling extreme emotions within the online user community. In brief, the fake news flag may have both positive and potential negative efects on controlling the spread of fake news. Contrary to the concern that the account-level intervention may interfere with the spread of truthful news due to its strict “one-size-fits-all” approach, our results reveal diferent efects for fake and truthful news. Although we find that fake news spreads much farther and more broadly after the implementation of the forwarding restriction policy, it stops the spread of fake news much more quickly. Altogether, these findings have important implications for online platforms in designing interventions to mitigate the spread of fake news.

For policymakers, this study suggests that platform interventions on social media are an efective way to combat the spread of fake news. Specifically, the two platform interventions have diferent objectives. The fake news flag is efective because it can prevent fake news from spreading farther and deeper within the dissemination network. In addition, as the fake news flag encourages influential users to spread fake news posts, we recommend that the platform develop an efective policy to motivate influential users to dispel fake news. This study reveals that the account-level intervention can efectively mitigate fake news by shortening its survival time. As this intervention only afects the dissemination of fake news but not truthful news, platform owners may consider implementing this account-level intervention to stop the spread of fake news quickly.

## Limitations and Future Research

We acknowledge that this paper has several limitations. Measuring the fake news survival time may be of concern, as users may remember a post after several years and forward or comment on it, which may potentially compromise our survival time measure. We address this concern with two points. First, we ensure that all forwards and comments collected from the posts cover the period up to 2018, so any forward or comment after a suficiently long period is unlikely to happen. Second, the mean and standard deviation of the number of forwards are very similar before and after the implementation of the forwarding restriction policy (Before: M = 335, SD = 229; After: M = 347, SD = 238).<sup>17</sup> Thus, we believe that the efect of the forwarding restriction policy on the survival time of fake news is unlikely to be afected by forwards or comments omitted during data collection.

Another limitation is that this study only investigates one social media platform in China. Although Sina Weibo ofers the opportunity to investigate the efectiveness of both platform interventions, the findings of this study may not be widely generalizable to other cultures, e.g., the United States. Referring to the influential theory of cultural dimensions [30, 31], we suggest that two dimensions should be taken into consideration when applying our findings to other cultures. One dimension is power distance, which is defined as “the extent to which the members of a society accept that power in institutions and organizations is distributed unequally” [30]. Brockner et al. [8] showed that people tend to react unfavorably when they have little voice in a decision-making process, but this tendency is weaker for people in high power distance cultures (e.g., China) than in low power distance cultures (e.g., the United States). Therefore, Chinese people might be more willing to accept a fake news flag verified by a reliable or mainstream information source. In contrast, people in low power distance cultures may not react favorably to the fake news flag, as they have little say in investigating and claiming the authenticity of a post.

The second cultural dimension is individualism/collectivism, which is defined as the extent to which members of a society emphasize their own needs over those of the group and tend to act as individuals rather than as members of a group [30]. It has been argued that members of a collectivist culture like China value harmony and group consensus more than freedom of expression, compared with members of an individualistic culture like the United States [36]. Hence, social media users in individualistic cultures may be more tolerant of extreme, irrational, and harmful posts and may be less likely to spontaneously report such posts.

Our results show that the fake news flag leads to more centralized and less dispersed dissemination of fake news. We argue that this observation can be explained by the reduced ambiguity of fake news content and provide empirical evidence to support this proposed mechanism. However, we note that the more centralized fake news dissemination network can also be explained by alternative theories such as the echo chamber [38] or social bot sharing [7]. Social bot sharing is less likely to be a concern due to the above-mentioned realname policy implemented by Sina Weibo. Regarding the echo chamber, like-minded individuals may be more likely to forward fake news posts after flagging. Multiple mechanisms may occur simultaneously to explain why individuals continue to engage with fake news after it is flagged as such, and our study proposes and empirically tests one mechanism, reduced ambiguity. Therefore, future research could conduct a more in-depth investigation to determine how diferent mechanisms interact to strengthen our study results.

Our study ofers several research opportunities for future studies. First, our sample of fake news posts relies on a social reporting system operated through the collective intelligence of the crowd, but social media platforms are increasingly using machine learningbased fake news detection systems. Future research could compare the efectiveness of these two types of systems in terms of fake news mitigation. Second, our study only focuses on a simple type of fake news flag. More empirical studies should be conducted to examine a fake news flag with various manipulations, such as a strong warning or a high level of severity, which is expected to have a more salient deterrent efect on fake news dissemination. Third, as the forwarding restriction policy depends on a credit scoring system, future research could explore the impact of the credit score on users’ fake news posting and forwarding behavior and study its interaction with the platform intervention. Fourth, future research could investigate the dynamic change in the survival time of fake news. An interesting research question would be to study how two fake news posts with the same survival time difer if one is disseminated with an initial surge followed by a decline and the other is disseminated with a slow start followed by a huge surge.

## Conclusions

This study exploits fake news data and two types of platform interventions in Sina Weibo to study the impact of platform interventions on fake news dissemination and survival. First, we exploit a natural experiment using a DiD approach to identify the causal relationship between the fake news flag (content-level intervention) and three fake news dissemination patterns. We show that after a post is flagged as fake news, its dissemination network instantly becomes more centralized and less dispersed. Furthermore, fake news is more likely to be spread by influential users. We attribute these findings to the reduced ambiguity of fake news [35]. Second, we investigate how the forwarding restriction policy (accountlevel intervention) influences the spread of fake and truthful news. We show that the implementation of the forwarding restriction policy leads to less direct and more indirect forwards of fake news, compared with truthful news. This phenomenon can be explained by social tie theory [20], as relational concerns prevent the strong ties of fake news publishing accounts from spreading fake news but have no efect on the weak ties. We also show that the forwarding restriction policy shortens the survival time of fake news. This study is among the first to provide empirical evidence of the efectiveness of platform interventions in combating the spread of fake news. Thus, our study constitutes an early efort, and we hope that our work will shed light on subsequent understandings of platform interventions and fake news dissemination.

## Notes

1. https://edition.cnn.com/2020/03/23/health/arizona-coronavirus-chloroquine-death/index. html

2. https://news.un.org/en/story/2020/04/1061682

3. https://www.theguardian.com/technology/2020/apr/07/whatsapp-to-impose-new-limit-onforwarding-to-fight-fake-news

4. https://chinacopyrightandmedia.wordpress.com/2012/05/08/sina-weibo-communitymanagement-regulations-trial/

5. https://www.facebook.com/journalismproject/programs/third-party-fact-checking

6. https://blog.twitter.com/en\_us/topics/product/2020/updating-our-approach-to-misleadinginformation.html; https://economictimes.indiatimes.com/magazines/panache/twitter-tightens -rules-will-label-tweets-that-spread-fake-news-to-ensure-a-fair-us-election/articleshow/ 78617901.cms

7. https://www.bbc.com/news/blogs-trending-37846860

8. https://theconversation.com/governments-are-making-fake-news-a-crime-but-it-could-stiflefree-speech-117654

9. https://www.forbes.com/sites/nicolemartin1/2018/11/30/how-social-media-has-changed-how -we-consume-news/?sh=18400d243c3c

10. https://www.chinainternetwatch.com/statistics/weibo-mau

11. http://service.account.weibo.com/?type=0&status=4

12. Full details of the diference between harmful information and fake news can be found in this policy document: https://chinacopyrightandmedia.wordpress.com/2012/05/08/sina-weibocommunity-management-regulations-trial

13. https://chinacopyrightandmedia.wordpress.com/2012/05/08/sina-weibo-community management-regulations-trial/

14. http://www.open.weibo.com/

15. https://radimrehurek.com/gensim/models/lsimodel.html

16. https://baike.baidu.com/item/%E5%BE%AE%E5%8D%9A%E5%AE%9E%E5%90%8D%E5% 88%B6; https://www.globaltimes.cn/content/700489.shtm

17. The mean diference is not statistically significant based on independent two-samples t-tests (t-statistic = -0.564).

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Notes on contributors

Ka Chung Ng (borisnkc@gmail.com) is an assistant professor in the Department of Management and Marketing, Faculty of Business, Hong Kong Polytechnic University. He received his Ph.D. in Information Systems from the Hong Kong University of Science and Technology. His research interests lie in fake news, business analytics, and fintech. His work has appeared in the Journal of Management Information Systems and ACM Transactions on Management Information Systems.

Jie Tang (tangjie@connect.hku.hk) is a Ph.D. student in Information Systems in HKU Business School at the University of Hong Kong. Her research interests include social media, information privacy, and human-computer interaction. Her research has appeared in the proceedings of several international conferences including International Conference on Information Systems and Pacific Asia Conference on Information Systems.

Dongwon Lee (dongwon@ust.hk; corresponding author) is an assistant professor in the Information Systems, Business Statistics, and Operations Management Department at the Hong Kong University of Science and Technology (HKUST). He received his Ph.D. in Information Systems from University of Maryland. His research interests focus on customer analytics, mobile commerce, digital nudging, digital transformation, and economics of information systems. Dr. Lee’s work has been appeared in a number of premier journals as well as major conferences and workshops in Information Systems.

## ORCID

Ka Chung Ng http://orcid.org/0000-0001-7875-8194 Jie Tang http://orcid.org/0000-0002-9588-8756 Dongwon Lee http://orcid.org/0000-0001-7450-4437

## References

1. Allcott, H. and Gentzkow, M. Social media and fake news in the 2016 election. Journal of Economic Perspectives, 31, 2 (2017), 211–236.

2. Allcott, H., Gentzkow, M., and Yu, C. Trends in the difusion of misinformation on social media. Research and Politics, 6, 2 (2019), 1–8.

3. Amoruso, M., Anello, D., Auletta, V., Cerulli, R., Ferraioli, D., and Raiconi, A. Contrasting the spread of misinformation in online social networks. In K. Larson, M. Winikof, S. Das and E. Durfee (eds.), Journal of Artificial Intelligence Research. International Foundation for Autonomous Agents and Multiagent Systems, São Paulo, Brazil, 2020, pp. 847–879.

4. Audrezet, A., de Kerviler, G., and Guidry Moulard, J. Authenticity under threat: When social media influencers need to go beyond self-presentation. Journal of Business Research, 117, (2020), 557–569.

5. Balkin, J.M. Free speech in the algorithmic society: Big data, private governance, and new school speech regulation. SSRN Electronic Journal, 51, (2017), 1149–1210.

6. Bessi, A. and Ferrara, E. Social bots distort the 2016 U.S. Presidential election online discussion. First Monday, 21, 11 (2016).

7. Boichak, O., Jackson, S., Hemsley, J., and Tanupabrungsun, S. Automated difusion? Bots and their influence during the 2016 U.S. Presidential election. In G. Chowdhury, J. McLeod, V. Gillet and P. Willett (eds.), Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics). Springer, Cham, 2018, pp. 17–26.

8. Brockner, J., Ackerman, G., Greenberg, J., et al. Culture and procedural justice: The influence of power distance on reactions to voice. Journal of Experimental Social Psychology, 37, 4 (2001), 300–315.

9. Buhr, K. and Dugas, M.J. The intolerance of uncertainty scale: Psychometric properties of the English version. Behaviour Research and Therapy, 40, 8 (2002), 931–945.

10. Chan, J. and Wang, J. Hiring preferences in online labor markets: Evidence of a female hiring bias. Management Science, 64, 7 (2018), 2973–2994.

11. Chen, D., Lü, L., Shang, M.S., Zhang, Y.C., and Zhou, T. Identifying influential nodes in complex networks. Physica A: Statistical Mechanics and its Applications, 391, 4 (2012), 1777– 1787.

12. Craig, S. This analysis shows how viral fake election news stories outperformed real news on Facebook. BuzzFeed News, 2016, 1–7. https://www.buzzfeednews.com/article/craigsilverman/ viral-fake-election-news-outperformed-real-news-on-facebook .

13. Enke, N. and Borchers, N.S. Social media influencers in strategic communication: A conceptual framework for strategic social media influencer communication. International Journal of Strategic Communication, 13, 4 (2019), 261–277.

14. Figl, K., Rank, C., Kießling, S., and Vakulenko, S. Fake news flags, cognitive dissonance, and the believability of social media posts. In H. Krcmar, J. Fedorowicz, W.F. Boh, J.M. Leimeister, and S. Wattal (eds.), International Conference on Information Systems, Munich, Germany, 2019.

15. Friedkin, N.E. Theoretical Foundations for Centrality Measures. American Journal of Sociology, 96, 6 (1991), 1478–1504.

16. Gao, G. and Gudykunst, W.B. Uncertainty, anxiety, and adaptation. International Journal of Intercultural Relations, 14, (1990), 301–317.

17. Garrett, R.K. and Poulsen, S. Flagging Facebook falsehoods: Self-identified humor warnings outperform fact checker and peer warnings. Journal of Computer-Mediated Communication, 24, 5 (2019), 240–258.

18. Gimpel, H., Heger, S., Olenberger, C., and Utz, L. The efectiveness of social norms in fighting fake news on social media. Journal of Management Information Systems, 38, 1 (2021), 196–221.

19. Goel, S., Anderson, A., Hofman, J., and Watts, D.J. The structural virality of online difusion. Management Science, 62, 1 (2016), 180–196.

20. Granovetter, M. The strength of weak ties: A network theory revisited. Sociological Theory, 1, (1983), 201.

21. Grinberg, N., Joseph, K., Friedland, L., Swire-Thompson, B., and Lazer, D. Political science: Fake news on Twitter during the 2016 U.S. presidential election. Science, 363, 6425, (2019) 374–378.

22. Gu, B., Konana, P., Raghunathan, R., and Chen, H.M. The allure of homophily in social media: Evidence from investor responses on virtual communities. Information Systems Research, 25, 3 (2014), 604–617.

23. Guess, A., Nyhan, B., and Reifler, J. Selective exposure to misinformation: Evidence from the consumption of fake news during the 2016 US presidential campaign. European Research Council 9.3 (2018): 4.

24. Harmon-Jones, E. and Mills, J. An introduction to cognitive dissonance theory and an overview of current perspectives on the theory. Stanford University Press, 2004.

25. Hartley, K. and Vu, M.K. Fighting fake news in the COVID-19 era: policy insights from an equilibrium model. Policy Sciences, 53, 4 (2020), 735–758.

26. Hess, K.R. Graphical methods for assessing violations of the proportional hazards assumption in cox regression. Statistics in Medicine, 14, 15, (1995), 1707–1723.

27. Hinz, O. and Spann, M. The impact of information difusion on bidding behavior in secret reserve price auctions. Information Systems Research, 19, 3 (2008), 351–368.

28. Ho, S.M., Hancock, J.T., Booth, C., and Liu, X. Computer-mediated deception: Strategies revealed by language-action cues in spontaneous communication. Journal of Management Information Systems, 33, 2 (2016), 393–420.

29. Hofmann, T. Latent semantic models for collaborative filtering. ACM Transactions on Information Systems, 22, 1 (2004), 89–115.

30. Hofstede, G. The interaction between national and organizational value systems[1]. Journal of Management Studies, 22, 4 (1985), 347–357.

31. Jalili, M. and Perc, M. Information cascades in complex networks. Journal of Complex Networks, 5, 5 (2017), 665–693.

32. Katz, E. and Shibutani, T. Improvised News: A Sociological Study of Rumor. The Bobbs-Merrill Company Inc., 1969.

33. Kim, A. and Dennis, A.R. Says who? The efects of presentation format and source rating on fake news in social media. MIS Quarterly, 43, 3 (2019), 1025–1039.

34. Kim, A., Moravec, P.L., and Dennis, A.R. Combating fake news on social media with source ratings: The efects of user and expert reputation ratings. Journal of Management Information Systems, 36, 3 (2019), 931–968.

35. Knapp, R.H. A psychology of rumor. Public Opinion Quarterly, 8, 1 (1944), 22–37.

36. Koh, N.S., Hu, N., and Clemons, E.K. Do online reviews reflect a product’s true perceived quality? An investigation of online movie reviews across cultures. Electronic Commerce Research and Applications, 9, 5 (2010), 374–385.

37. Kuang, L., Huang, N., Hong, Y., and Yan, Z. Spillover efects of financial incentives on non-incentivized user engagement: Evidence from an online knowledge exchange platform. Journal of Management Information Systems, 36, 1 (2019), 289–320.

38. Kwon, H.E., Oh, W., and Kim, T. Platform structures, homing preferences, and homophilous propensities in online social networks. Journal of Management Information Systems, 34, 3 (2017), 768–802.

39. Landauer, T.K., Foltz, P.W., and Laham, D. An introduction to latent semantic analysis. Discourse Processes, 25, 2–3 (1998), 259–284.

40. Landherr, A., Friedl, B., and Heidemann, J. A critical review of centrality measures in social networks. Business & Information Systems Engineering, 2, 6 (2010), 371–385.

41. Lazer, D.M.J., Baum, M.A., Benkler, Y., et al. The science of fake news. Science, 359, 6380 (2018), 1094–1096.

42. Maasberg, M., Ayaburi, E., Liu, C., and Au, Y. Exploring the propagation of fake cyber news: An experimental approach. In Proceedings of the 51st Hawaii International Conference on System Sciences. Curran Associates Inc., Hawaii, USA, 2018.

43. Marett, K. and Joshi, K.D. The decision to share information and rumors: Examining the role of motivation in an online discussion forum. Communications of the Association for Information Systems, 24, 1 (2009), 47–68.

44. Moravec, P.L., Kim, A., and Dennis, A.R. Flagging fake news: System 1 vs. System 2. In J.P. Heje, S. Ram, and M. Rosemann (eds.), International Conference on Information Systems, San Francisco, USA, 2018.

45. Moravec, P.L., Minas, R.K., and Dennis, A.R. Fake news on social media: People believe what they want to believe when it makes no sense at All. MIS Quarterly, 43, 4 (2019), 1343–1360.

46. Oh, O., Agrawal, M., and Rao, H.R. Community intelligence and social media services: A rumor theoretic analysis of tweets during social crises. MIS Quarterly, 37, 2 (2013), 407–426.

47. Papanastasiou, Y. Fake news propagation and detection: A sequential model. Management Science, 66, 5, (2020), 1826–1846.

48. Park, J.H., Konana, P., Gu, B., Kumar, A., and Raghunathan, R. Information valuation and confirmation bias in virtual communities: Evidence from stock message boards. Information Systems Research, 24, 4 (2013), 1050–1067.

49. Pennycook, G., Bear, A., Collins, E.T., and Rand, D.G. The implied truth efect: Attaching warnings to a subset of fake news headlines increases perceived accuracy of headlines without warnings. Management Science, 66, 11 (2020), 4944–4957.

50. Pennycook, G., Cannon, T.D., and Rand, D.G. Prior exposure increases perceived accuracy of fake news. Journal of Experimental Psychology: General, 147, 12, (2018), 1865–1880.

51. Pennycook, G. and Rand, D.G. Lazy, not biased: Susceptibility to partisan fake news is better explained by lack of reasoning than by motivated reasoning. Cognition, 188, (2019), 39–50.

52. Pickett, J.T., Roche, S.P., and Pogarsky, G. Toward a Bifurcated Theory of Emotional Deterrence. Criminology, 56, 1 (2018), 27–58.

53. Rosenbaum, P.R. and Rubin, D.B. The central role of the propensity score in observational studies for causal efects. Biometrika, 70, 1 (1983), 41–55.

54. Rosnow, R.L. Inside rumor: A personal journey. American Psychologist, 46, 5 (1991), 484–496.

55. Ross, B., Heisel, J., Jung, A.K., and Stieglitz, S. Fake news on social media: The (in)efectiveness of warning messages. In J.P. Heje, S. Ram, and M. Rosemann (eds.), International Conference on Information Systems, San Francisco, USA, 2018.

56. Sarker, S., Ahuja, M., Sarker, S., and Kirkeby, S. The role of communication and trust in global virtual teams: A social network perspective. Journal of Management Information Systems, 28, 1 (2011), 273–310.

57. Schulze, E. EU tells Facebook, Google and Twitter to take more action on fake news. In CNBC. 2019.

58. Shao, C., Hui, P.M., Cui, P., Jiang, X., and Peng, Y. Tracking and characterizing the competition of fact checking and misinformation: Case Studies. IEEE Access, 6, (2018), 75327–75341.

59. Sharma, K., Qian, F., Jiang, H., Ruchansky, N., Zhang, M., and Liu, Y. Combating fake news: A survey on identification and mitigation techniques. ACM Transactions on Intelligent Systems and Technology, 10, 3 (2019), 1–41.

60. Shi, D., Guan, J., Zurada, J., and Manikas, A. A data-mining approach to identification of risk factors in safety management systems. Journal of Management Information Systems, 34, 4 (2017), 1054–1081.

61. Shi, Z.M., Lee, G.M., and Whinston, A.B. Toward a better measure of business proximity: Topic modeling for industry intelligence. MIS Quarterly, 40, 4 (2020), 1035–1056.

62. Stieglitz, S. and Dang-Xuan, L. Emotions and information difusion in social media - Sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29, 4 (2013), 217–248.

63. Suh, A., Shin, K.S., Ahuja, M., and Kim, M. The influence of virtuality on social networks within and across work groups: A multilevel approach. Journal of Management Information Systems, 28, 1 (2011), 351–386.

64. Sutton, J., Spiro, E.S., Fitzhugh, S., Johnson, B., Gibson, B., and Butts, C.T. Terse message amplification in the Boston bombing response. In S.R. Hiltz, M.S. Pfaf, L. Plotnick and P.C. Shih (eds.), ISCRAM 2014 Conference Proceedings - 11th International Conference on Information Systems for Crisis Response and Management. University Park, USA, 2014, pp. 612–621.

65. Sutton, J., Spiro, E.S., Johnson, B., Fitzhugh, S., Gibson, B., and Butts, C.T. Warning tweets: serial transmission of messages during the warning phase of a disaster event. Information Communication and Society, 17, 6 (2014), 765–787.

66. Tang, J., and Ng, K.C. Reposts influencing the efectiveness of social reporting system: An empirical study from sina weibo. In H. Krcmar, J. Fedorowicz, W.F. Boh, J.M. Leimeister, and S. Wattal (eds.), International Conference on Information Systems, Munich, Germany, 2019.

67. Tausczik, Y.R. and Pennebaker, J.W. The psychological meaning of words: LIWC and computerized text analysis methods. Journal of Language and Social Psychology, 29, 1 (2010), 24–54.

68. Torres, R., Gerhart, N., and Negahban, A. Combating fake news: An investigation of information verification behaviors on social networking sites. In Proceedings of the 51st Hawaii International Conference on System Sciences. Curran Associates Inc., Hawaii, USA, 2018.

69. Vosoughi, S., Roy, D., and Aral, S. The spread of true and false news online. Science, 359, 6380 (2018), 1146–1151.

70. Wang, Q., Li, B., and Singh, P.V. Copycats vs. original mobile apps: A machine learning copycat-detection method and empirical analysis. Information Systems Research, 29, 2 (2018), 273–291.

71. Zhang, X. and Venkatesh, V. Explaining employee job performance: The role of online and ofline workplace communication networks. MIS Quarterly, 37, 3 (2013), 695–722.

72. Zhang, X., Zhu, J., Wang, Q., and Zhao, H. Identifying influential nodes in complex networks with community structure. Knowledge-Based Systems, 42, (2013), 74–84.

73. Zhang, X.M. and Wang, C. Network positions and contributions to online public goods: The case of Chinese wikipedia. Journal of Management Information Systems, 29, 2 (2012), 11–40.

74. Zhou, S., Qiao, Z., Du, Q., Wang, G.A., Fan, W., and Yan, X. Measuring customer agility from online reviews using big data text analytics. Journal of Management Information Systems, 35, 2 (2018), 510–539.
