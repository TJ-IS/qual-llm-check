---
otero_id: 27961
otero_key: "NHS3EZQM"
title: "From Anonymity to Accountability: How Virtual Identity Disclosure Changes the Quantity and Quality of “Likes”"
authors: "Bingjie Qian; Tat Koon Koh; Xiaoquan (Michael) Zhang"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0335"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# From Anonymity to Accountability: How Virtual Identity Disclosure Changes the Quantity and Quality of “Likes”

Bingjie Qian,<sup>a</sup> Tat Koon Koh,<sup>b</sup> Xiaoquan (Michael) Zhang<sup>c,</sup>\*

<sup>a</sup> Advanced Institute of Business, Tongji University, Shanghai 200070, China; <sup>b</sup>Hong Kong University of Science and Technology, Hong Kong; <sup>c</sup> Department of Decisions, Operations and Technology, CUHK Business School, Chinese University of Hong Kong, Shatin, N.T., Hong Kong \*Corresponding author

Contact: bingjieqian1211@gmail.com, https://orcid.org/0000-0001-7275-9911 (BQ); koh@ust.hk, https://orcid.org/0000-0002-5598-310X (TKK); zhang@cuhk.edu.hk, https://orcid.org/0000-0003-0690-2331 (X(M)Z)

Received: June 23, 2020 Revised: August 12, 2021; October 29, 2022; August 22, 2023; April 23, 202 Accepted: June 3, 2024 Published Online in Articles in Advance: December 26, 2024

https://doi.org/10.1287/isre.2020.0335

Copyright: © 2024 INFORMS

Abstract. An integral component of user participation in community-based platforms is giving “likes” to content posted by others. At the same time, online social participation differs from offline social participation in that online users are often allowed to create a virtual identity unrelated to their real-world identity. The objective of this study is to identify the motivations behind users’ giving “likes” when their virtual identity (i.e., username) is hid den or shown. Specifically, we leverage a natural experiment to examine the effect of vir tual identity disclosure on users’ “liking” behavior. Our identification strategy relies on an exogenous policy change in an online community-based platform, where likers’ username was not visible before but publicly shown after the change. Our results show that users “liked” fewer but higher-quality articles after the policy change, consistent with their protective self-presentation motivation. This study emphasizes the significance of virtual iden tity, arguing that a virtual identity devoid of real-world information should not be equated with anonymity. It also underscores the importance of protective self-presentation over acquisitive self-presentation, suggesting that research should focus not only on the actions users take but also on those they intentionally avoid taking. Furthermore, our study identi fies “liking” as a key channel of self-presentation, complementing the focus on posting behaviors in the extant literature. Practically, platforms can refine their policies on virtual identity disclosure to enhance content engagement, whereas content creators should tailor their offerings to meet the self-presentation needs of their audience.

History: Sam Ransbotham, Senior Editor; Jason Chan, Associate Editor History: Sam Ransbotham, Senior Editor; Jason Chan, Associate Editor

Funding: This research was supported by the National Natural Science Foundation of China (NSFC) [Grants 72121001, 72293562, 7247030852] and the Hong Kong Research Grant Council (RGC) [Grants GRF 14504524, 14500521, 165052947, 14501320].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2020.0335.

Keywords: community-based platform • “liking” behavior • natural experiment • identity disclosure • protective self-presentation

## Introduction

Community-based platforms such as social networking services (SNS; e.g., Facebook, Instagram) and knowledge exchange websites (e.g., Stack Overflow, Quora) are prominent in today’s highly digitized environment. A critical success factor for these platforms is user participation, and prior research has examined how it can be influenced by platform features such as user ranking systems (Shen et al. 2015, Goes et al. 2016), symbolic awards (Gallus 2017), interactivity (Jiang et al. 2010), social network integration (Huang et al. 2017), and anonymity (Cho and Kwon 2015, Bapna et al. 2016). At the same time, online social participation is distinctively different from offline social participation in that online users are often allowed to create a virtual identity and participate anonymously. This present study seeks to understand how a form of user participation (specifically, “liking” the content posted by others) is affected by a specific platform feature (specifically, whether likers’ virtual identity is disclosed). Various platforms provide a “Like” button for users to express their attitudes about the content that they consume. For example, Facebook explains that “[clicking] Like below a post on Facebook is a way to let people know that you enjoy it … ,” and Twitter describes that “Likes … are used to show appreciation for a post.”<sup>1</sup> Although “liking” takes only one click of the button, its impacts can be nontrivial. For platforms, the “like” feature can serve as an effective emotional sensor and thus contribute to their success (Kessler 2012). Many platforms use the “like” feature in their content ranking and recommendation algorithms. For example, on Facebook, the number of “likes” that a post receives is a major factor that affects its ranking in News Feed.<sup>2</sup> Also, the “like” feature can motivate user contribution and influence community growth. Research shows that the “likes” (and their equivalents, e.g., “favorites”) that users receive affect the quantity and quality of their contributions (Qiu and Kumar 2017, Moqri et al. 2018) and the subsequent growth of the community (Bapna et al. 2019).

Despite numerous studies examining the impacts or consequences of “likes,” research on the antecedents of “likes” is scant. Exceptions are studies that investigate the association between content characteristics and user engagement (e.g., “liking”) on social media (Lee et al. 2018, Bapna et al. 2019, Shin et al. 2019). In this study, we aim to add to the understanding of “likes” by examining the impact of platform design/policy on users’ “liking” behavior and the underlying mechanism. Specifically, we investigate how virtual identity disclosure—that is, disclosing likers’ username—affects users’ “liking” behavior. Whether users’ identity (virtual or real) is shown to third parties is a critical design consideration for content-related platforms. Some platforms disclose users’ identity to others. For example, Instagram publicly shows users’ username (i.e., virtual identity) when they “like” a post.<sup>3</sup> Other platforms allow users to keep their identity invisible or private. For example, LinkedIn users can choose to reveal their name (i.e., real identity), disclose profile characteristics (i.e., job title and industry), or be shown as “LinkedIn Member” when viewing other users’ profiles.<sup>4</sup> Although previous studies mainly focus on the impact of real identity disclosure (Forman et al. 2008, Pu et al. 2020), we show in this study that virtual identity disclosure can also influence users’ behavior.

To explain the effect of virtual identity disclosure in community-based platforms, we consider three different user motivations that are relevant: (i) intrinsic utility (to express satisfaction and enjoyment), (ii) relational motivation (to build, maintain, and/or strengthen relationships with others), and (iii) self-presentation (to present oneself and achieve desired impressions). Although these motivations are likely to coexist, some may dominate and dwarf the others in influencing users’ “liking” behavior. We thus aim to identify the dominating motivation and the impacts of virtual identity disclosure policies on content that users “like.” This knowledge can be critical for platforms that use “likes” to determine popular content and/or recommend content to users (e.g., collaborative filtering). Moreover, the dominating motive behind “likes” has implications for content creators. Many content creators (e.g., influencers) strive to produce highly engaging content, in which the number of “likes” received is a key performance indicator. Uncovering the dominating factor that drives users’ giving “likes” can thus help creators strategize the form and substance of their content.

We investigate the research questions using a natural experiment on a user-generated content platform. Our empirical strategy relies on an exogenous policy change of virtual identity disclosure on the platform. Before the policy change, likers’ usernames were not shown; after the policy change, likers’ usernames were publicly displayed. This policy change offers a unique opportunity to compare the three motivations for giving “likes” because, as shown below, these motivations give rise to different predictions regarding users’ reactions to the policy change. We find that after virtual identity disclosure, the number of “likes” on the platform decreased, but the overall quality of the “liked” content increased, which suggests the dominant role of protective self-presentation in users’ “liking” behavior.

This study contributes insights to theory and practice. First, although most previous studies focus on the disclosure of users’ real-world identity (see Table 1), this study suggests that even if users are allowed to use a pseudonym unrelated to their real-world identity, disclosing the pseudonym can still alter their behavior. Therefore, research must broaden the concept of user identity to include both virtual and real identities.

Second, this study adds to our understanding of user participation behaviors and motives in communitybased platforms by accounting for different motivations of user participation (i.e., intrinsic utility, relational, and self-presentation motivation) and examines their comparative strength. Our differentiation of acquisitive and protective self-presentation modes and the evidence for the dominant influence help explain the inhibition effect of (real and virtual) identity disclosure that this and previous studies find (Huang et al. 2017, Pu et al. 2020). An implication is that research on self-presentation should consider not only the actions individuals choose to take but also activities they can engage in but intentionally refrain from.

Third, our focus on the antecedents and motivations of “liking” also complements the research on its consequences, thus providing a more holistic picture of the causes and effects of this form of user participation. In addition, our emphasis on “liking” extends the focus on posting behaviors in extant studies (see Table 1). This is meaningful as it helps the literature cover a fuller spectrum of user participation in community-based platforms. This study also has practical implications for the strategies of platforms and content creators. For platforms, understanding users’ motivations to give “likes” and the effects of virtual identity disclosure can help refine community policies to encourage quality content engagement. For content creators, our findings suggest they can enhance content engagement by aligning their offerings with the self-presentation goals of their audience.

Table 1. Studies on Identity Disclosure

<table><tr><td>Study</td><td>Real vs. virtual identity disclosure</td><td>Posting vs. “liking” content</td></tr><tr><td>Forman et al. (2008)</td><td>Real</td><td>Posting</td></tr><tr><td>Cho and Kwon (2015)</td><td>Real</td><td>Posting</td></tr><tr><td>Fredheim et al. (2015)</td><td>Real</td><td>Posting</td></tr><tr><td>Huang et al. (2017)</td><td>Real</td><td>Posting</td></tr><tr><td>Pu et al. (2020)</td><td>Real</td><td>Posting</td></tr><tr><td>Kilner and Hoadley (2005)</td><td>Virtual</td><td>Posting</td></tr><tr><td>This study</td><td>Virtual</td><td>“Liking”</td></tr></table>

## Literature Review and Research Framework

## Virtual Identity Disclosure

Virtual identity disclosure refers to the disclosure of users’ pseudonyms or usernames to third parties. It differs from identity disclosure in prior literature, which relates to the situations in which users’ real-world identity is disclosed (Forman et al. 2008, Pu et al. 2020). In practice, some platforms do not require users to provide their real identity but disclose their virtual identity (e.g., username) to third parties during some activities. A prototypical example is Instagram, which does not require users to submit their real name but discloses their username in all their posts and “likes.”

The extant literature suggests that anonymity/ nonanonymity in offline environments can affect individual behaviors. According to the deindividuation theory (Zimbardo 1969), anonymity reduces self-awareness, self-observation, and concern for social evaluation, leading to less inner constraint and self-regulation. Therefore, under the cloak of anonymity, individuals are more likely to behave in a socially undesirable manner and conduct otherwise inhibited behaviors. For example, anonymity could increase group polarization, bystander apathy, and social loafing (Christopherson 2007). In contrast, when individuals’ identity is visible (i.e., nonanonymous), they tend to be more restrained in their behaviors. For instance, Halloween trick-or-treaters who are asked their name and address are less likely to steal candy when left unattended than children who remain anonymous (Diener et al. 1976).

Previous studies have demonstrated the inhibition effect of real identity disclosure in community-based platforms. For example, real name disclosure can lead to less content generation in corporate online communities (Pu et al. 2020), and the integration of SNS accounts can cause a decrease in inflammatory comments (Cho and Kwon 2015), politicized topics (Fredheim et al. 2015), negations (Huang et al. 2017), and total comment quantity (Fredheim et al. 2015). Research also finds that a visible browsing record can make users browse fewer profiles on dating websites (Bapna et al. 2016). Interestingly, if the platform requires users to provide their real identifying information (e.g., real name, identification number, etc.) but does not show the identifying information publicly, it will not produce an inhibition effect on users’ behavior (Kilner and Hoadley 2005, Cho and Kwon 2015); this clearly highlights the influence of identity disclosure on users.

Although there are numerous studies on anonymity/ nonanonymity in offline environments and real identity disclosure in online platforms, research on virtual identity disclosure is scant, and its impact remains unclear. On the one hand, users can register a new virtual identity at a low cost or have multiple virtual identities at the same time. They can also easily manipulate their online profiles or forge fictional identities completely different from their real-world identities; such behaviors can be observed in accounts of users maintaining alternate personas in online communities (Froomkin 1999) and being involved in identity deception (Tsikerdekis and Zeadally 2015). As such, users who find their virtual identity associated with a negative reputation or blocked by a platform can simply switch to another account (Tsikerdekis and Zeadally 2014). The relatively low effort in creating and maintaining virtual identities suggests that users may not care significantly about such identities, especially compared with their realworld identities.

On the other hand, as users can be identified and traced by the unique and persistent user identifier (ID) of their virtual identity, they may perceive accountability for their online behaviors even if their virtual and real-world identities are not linked (Ma and Agarwal 2007). Users can strive to establish an image associated with their virtual identity and maintain a consistent persona through their platform activities. For instance, Twitter users can shape their online persona by maintaining the topic distribution of their self-tweets and retweets (Geva et al. 2019). At times, individuals identify more with their online selves than with their real-world identities; users with high self-identity verification in platforms feel that other members appreciate their skills and contributions, and they believe that their online personas cannot be easily substituted (Kuem et al. 2020). Given the contrasting theoretical possibilities, it is unclear how much users value their online identities and whether their reactions to virtual identity disclosure mirror their responses to real identity disclosure.

## Users’ “Liking” of Content

This study focuses on users’ “liking” behaviors, the nature of which differs from that of content generation. First, “liking” is a response to others’ content (Hayes et al. 2016) and takes only a click of a button. By contrast, generating content is a form of direct expression that can require extensive effort (e.g., writing answers in online knowledge exchanges (Wasko and Faraj 2005) and making predictions in online prediction platforms (Qiu and Kumar 2017)). Second, although users’ content can be elaborative and contain high clarity (e.g., readable and objective product reviews (Goes et al. 2014)), their “likes” lack nuances and can lead to high levels of communicative ambiguity (Sumner et al. 2018). For example, a “like” given to a detailed restaurant review that discusses both food and service is not informative about whether the liker agrees with the food description or service evaluation. Third, content posting can be used for monetization, especially for virtual identities with many followers, whereas “liking” has little, if any, monetizing effect. That “liking” and content generation are fundamentally different (in terms of purpose, effort, etc.) implies that users will likely have different considerations for the respective activities. As such, we need to cautiously apply knowledge about users’ content generation behaviors when studying users’ “liking” behaviors. For example, although research shows identity disclosure affects content generation (Huang et al. 2017, Pu et al. 2020), we should carefully examine its influence on “liking” using perspectives that closely align with users’ corresponding motivations and considerations for this activity. Doing so can offer distinct theoretical and practical implications, which is important as the “like” feature is integral on many platforms.

Table 2. Motivations of User Participation in Platforms

<table><tr><td rowspan="2">Study</td><td rowspan="2">User behavior</td><td colspan="3">Motivations of user behavior</td><td rowspan="2">Comparative strength of multiple motivations</td></tr><tr><td>Intrinsic utility</td><td>Relational</td><td>Self-presentation</td></tr><tr><td>Schau and Gilly (2003)</td><td>Posting content</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Hennig-Thurau et al. (2004)</td><td>Visiting platform, posting content</td><td></td><td>√</td><td>√</td><td></td></tr><tr><td>Wasko and Faraj (2005)</td><td>Posting content</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Ma and Agarwal (2007)</td><td>Posting content</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Sheldon et al. (2011)</td><td>Visiting platform</td><td></td><td>√</td><td></td><td></td></tr><tr><td>Xia et al. (2012)</td><td>Providing files</td><td>√</td><td></td><td></td><td></td></tr><tr><td>Shriver et al. (2013)</td><td>Posting content</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Toubia and Stephen (2013)</td><td>Posting content</td><td>√</td><td></td><td>√</td><td>√</td></tr><tr><td>Zeng and Wei (2013)</td><td>Posting content</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Goes et al. (2014)</td><td>Posting content</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Jabr et al. (2014)</td><td>Posting content</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Qiu and Kumar (2017)</td><td>Posting content</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Moqri et al. (2018)</td><td>Contributing to open-source software (OSS) projects</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Geva et al. (2019)</td><td>Sharing content</td><td></td><td></td><td>√</td><td></td></tr><tr><td>This study</td><td>“Liking” content</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

## Motivations of User Participation in Platforms

We posit that the effect of virtual identity disclosure on users’ “liking” behavior depends on their motivations to give “likes.” Based on the extant literature, we identify three motivations of user participation that are relevant in our context: intrinsic utility, relational, and self-presentation. Table 2 provides a summary. We consider the implications of virtual identity disclosure for the respective motivations to pinpoint the dominating motivation in users’ “liking” behavior. As shown in Table 3, different motivations give different predictions about the impact of virtual identity disclosure on the quantity of “likes” and the quality of “liked” content. We submit that virtual identity disclosure’s overall or net effect on users’ “liking” behavior depends on the dominating motivation.

Intrinsic Utility Motivation. Users can give “likes” to express their approval for the content that they enjoy, agree with, and/or find useful; this is what platforms (e.g., Facebook and Twitter) typically assume users do with this feature (see endnote 1). Such “liking” is based primarily on the intrinsic value of the content to the focal users and independent of whether the likers identity is visible to others. Ceteris paribus, if intrinsic utility motivation dominates, the policy change of disclosing likers’ virtual identity should not substantially affect the amount and the quality of the content that users “like.”

Relational Motivation. Individuals have a fundamental need for social relationships, leading them to reach out and interact with others (Baumeister and Leary 1995,

Table 3. Theoretical Development

<table><tr><td rowspan="2">Effect of virtual identity disclosure on:</td><td rowspan="2">Intrinsic utility</td><td rowspan="2">Relational</td><td colspan="2">Self-presentation</td></tr><tr><td>Acquisitive</td><td>Protective</td></tr><tr><td>Quantity of “likes”</td><td>No change</td><td>Increase</td><td>Increase</td><td>Decrease</td></tr><tr><td>Quality of “liked” content</td><td>No change</td><td>No change</td><td>Increase</td><td>Increase</td></tr></table>

Berger 2014). Prior research shows that this need motivates people to participate in online communities. People use social media to cope with their feelings of disconnection (Sheldon et al. 2011), share news and information to enhance social bonds (Milkman and Berger 2014), and blog to facilitate interaction or socializing with others (Shriver et al. 2013).

In online communities, “liking” allows users to indicate that they have read certain content and find it useful or interesting. In this sense, “liking” serves as a signal of attention and support, which facilitates the building, maintaining, and strengthening of social relationships with others, particularly with content creators (Ellison et al. 2014). Hayes et al. (2016) conceptualize the “like” feature on social media as a “paralinguistic digital affordance” that facilitates user interactions, similar to phatic communication like waving and nodding. Giving “likes” can also help users gain reciprocal “likes” from others, which improves their popularity and relational standing in the community; as reciprocity is based on a sense of mutual indebtedness, which can give rise to ongoing social exchanges between two individuals, we classify it as relational motivation, following Wasko and Faraj (2005). However, a necessary condition for “likes” to affect social relationships is that likers’ identities are visible to others. Therefore, if relational motivation dominates in users’ “liking” behavior, virtual identity disclosure should increase the number of “likes” they give. However, as this kind of “likes” is largely driven by users’ desire to initiate and maintain relationships with content creators (Sumner et al. 2018), virtual identity disclosure may not affect the quality of content users “like.” To enhance their relationship with the content creators, users who are driven strongly by relational motivation can “like” the content regardless of its quality to signal that they have attended to it.

Self-Presentation Motivation. Self-presentation is how individuals present themselves and project a desired impression (Goffman 1959). Self-presentation or image motivation captures the idea that individuals are influenced by others’ perceptions and the desire to be well regarded by others (Ariely et al. 2009). Following extant literature, we view self-presentation and privacy maintenance as two sides of the same coin (Bartsch and Subrahmanyam 2015), as both are achieved by controlling the information available to others about oneself. Previous studies find that users control their selfpresentation on social networking sites using privacy settings (e.g., restricting others’ access to their profile and posts) (Chen and Marcus 2012) and engage in selective information disclosure to preserve privacy when using instant messaging (e.g., self-censoring what they say) (Kobsa et al. 2012). Leary (1996) suggests that individuals shape their images not only by describing themselves in specific ways but also by omitting certain information from their self-descriptions. Goffman (1959, p. 141) also indicates that self-presentation involves “the overcommunication of some facts and the undercommunication of others.” Based on these perspectives, maintaining privacy is akin to individuals minimizing self-presentation.

Studies on self-presentation in online communities mostly focus on users’ content generation behavior, showing that users present themselves and achieve their desired image by posting content on social network sites (Shriver et al. 2013), product review platforms (Hennig-Thurau et al. 2004, Goes et al. 2014), and photo-sharing communities (Zeng and Wei 2013). Extending prior research, we propose that self-presentation may also be achieved through “liking” activities. Specifically, the content that users “like” signals their tastes and preferences. Research finds that users show a “you are what you ‘Like’” mentality and give “likes” based on what they want others to see they “like” (Sumner et al. 2018).

As in the case of relational motivation, selfpresentation motivation requires users’ identity to be visible to others, as others’ impressions about a user are based on what they see about that user. When users are anonymous, they tend to feel more comfortable and secure and be less aware and concerned about social evaluation (Christopherson 2007). Consequently, they may engage in socially unfavorable behaviors, such as being selfish in dictator games (Andreoni and Bernheim 2009) or posting low-quality content (Pu et al. 2020). However, when users’ identity is visible, their concern about their image increases. As a result, they are likely to participate less in socially undesirable activities and more in activities that bene fit their image (Ariely et al. 2009).

There are two modes of self-presentation: acquisitive and protective (Arkin 1981). Acquisitive self-presentation is to relate oneself to desired images, whereas protective self-presentation is to distance oneself from undesired images (Barasch and Berger 2014). Acquisitive selfpresentation reflects a more proactive mindset, seeking positive impressions and social approval by actively participating in certain activities. For example, people talk about positive personal experiences with products and services (e.g., “the restaurant I picked was great”) to signal their expertise and maintain their reputation (DeAngelis et al. 2012, Wojnicki and Godes 2017). They also share news that reflects positively on them to generate desired impressions (Milkman and Berger 2014) and publicize their connection with successful others to enhance their image (Cialdini et al. 1976). By contrast, protective self-presentation reflects a more conservative orientation, avoiding negative impressions and social disapproval by reducing certain activities. For example, individuals tend not to post negative information about themselves on social media (Gonzales and Han cock 2011) or share personal experiences that cast themselves in a negative light as the size of the audience grows (Barasch and Berger 2014).

In our research setting, the two self-presentation modes can have different implications about the number of “likes” users give. Acquisitive self-presentation implies that users will embrace the chance to present positive images through the content that they are associated with and thus give more “likes.” By contrast, protective self-presentation indicates that users will refrain from giving “likes” because of the concern that others will make negative inferences about them based on the content they “like.” Although both modes of self-presentation can be present, protective self-presentation occurs more often (Tice 1991, Barasch and Berger 2014, Berger 2014), suggesting it can be more influential. People generally are more motivated to avoid bad impressions than to pursue good ones (Baumeister et al. 2001), and the aversion to shame is more powerful than the anticipation of prestige as a motivator (Samek and Sheremeta 2014). Arkin (1981) indicates that when the audience consists of strangers whose evaluation standards are unpredictable, acquisitive self-presentation will be risky and protective self-presentation will be more salient. An implication is that users not highly familiar with others in online communities may strive to avoid potential social disapproval when their identity is visible to others. This can be why real identity disclosure leads users to generate less content in online communities (Fredheim et al. 2015, Pu et al. 2020) and browse fewer profiles on dating platforms (Bapna et al. 2016). Hence, in our context, the stronger influence of protective self-presentation suggests that users will become more selective in giving “likes” when their virtual identity is disclosed, resulting in fewer “likes.”

Whereas the impact of the two self-presentation modes on the quantity of “likes” that users give may differ, that on the quality of content that users “like” can be similar. As the content that users associate with can greatly impact their image (Schau and Gilly 2003, Milkman and Berger 2014), they will care more about content quality after virtual identity disclosure. As a result, they will engage in strategic and selective “liking” activities to enhance their image. Users driven by acquisitive selfpresentation will seek high-quality content that aligns with their desired image and give more “likes” to such content. In contrast, users motivated by protective selfpresentation will avoid low-quality content that reflects poorly on their image and give fewer “likes” to such content. Regardless of the self-presentation mode, the quality of the content that users “like” should be higher after virtual identity disclosure.

## Research Context and Data

Our research context is Douban (www.douban.com), an online community where users can create content and interact with others. Established in March 2005, it had over 200 million registered users by the end of 2019.<sup>5</sup> It has several sections for different functions (e.g., movie reviews, group discussions). This study focuses on the group discussion section, one of the earliest and most popular sections. In this section, users can create new and join existing discussion groups for specific topics (e.g., sports and music). Although users can post and comment on articles only in the groups they have joined, they can “like” and share articles in all groups.

An exogenous policy change happened on July 16, 2018. Before the change, Douban showed the number of users who “liked” an article but not their identities. After the change, the virtual identities (i.e., the usernames) of those who “liked” an article were shown below the article. Clicking a username leads to the respective personal page that provides details about the user. Other features, such as those related to posting and commenting, were not altered during the policy change. Online Appendix A shows the interface of the group discussion section after the policy change. This exogenous policy change sets up a natural experiment to study the influence of virtual identity disclosure on users’ giving “likes,” in which the counterfactual is the observations before the change (Zhang and Zhu 2011, Pu et al. 2020).

Using public application programming interfaces (APIs), we collected data of all group discussion articles from March 1, 2018, to December 30, 2018. Our data included details of users who posted articles and who “liked” and commented on articles. We generated a panel data set of each user’s “likes” each week. We could collect data on users’ “liking” behavior before the policy change because after the policy change, the platform disclosed likers’ usernames for all articles, regardless of when they were posted. The data consisted of 43 weeks, from March 5, 2018, to December 30, 2018 (i.e., 19 weeks before and 24 weeks after the policy change), and 911,791 users who “liked” at least one article. The policy change was implemented on the first day of week 20. Although March 5 is the first day in our data on users’ “liking” behavior, we also collected articles posted between March 1 and March 4 because users may “like” articles posted earlier. To minimize the problem of missing observations, we excluded users who registered and discussion groups created on or after March 5, 2018. Figure 1 shows the timeline of our study.

## Empirical Analysis Main Analysis

Effect of Policy Change on Quantity of “Likes.” Figure 2 illustrates the total number of “likes” given on each day from March 5 to December 30, 2018. There was a sharp decrease after July 16, which stabilized after a month, suggesting that users took some time to react to the policy change.

Figure 1. (Color online) Timeline of Study

<table><tr><td>Mar 5, 2018</td><td>Jul 16, 2018</td><td>Dec 30, 2018</td></tr><tr><td>Virtual identity not disclosed</td><td colspan="2">Virtual identity disclosed</td></tr><tr><td> $1 \leq t \leq 19$ After $_{t}$ =0</td><td colspan="2"> $20 \leq t \leq 43$ After $_{t}$ =1</td></tr></table>

We examined the effect of virtual identity disclosure on the number of “likes” each user gave each week. We utilized the fixed-effects Poisson regression model because the dependent variable is a count variable. The Poisson model specifies that the dependent variable $L i k e N b r _ { i t }$ (the number of articles that user $i \ ^ { \prime \prime } ] \mathrm { i k e s } ^ { \prime \prime }$ in week t) follows a Poisson distribution with parameter $\lambda _ { i t } ,$ , which is explained by the independent variables as follows:

$$
\ln (\lambda_ {i t}) = \beta_ {0} + \beta_ {1} A f t e r _ {t} + C o n t r o l V a r s _ {i t} + \mu_ {i} + \epsilon_ {i t},\tag{1}
$$

where i indexes the users and t indexes the weeks. $A f t e r _ { t }$ is a dummy that equals zero if week $t \leq 1 9$ and one if week $t \geq 2 0$ (see Figure 2). We included week variable and its squared term to control for time effect; using the number of weeks since the users joined the platform as an alternative control variable yields qualitatively similar results. $\mu _ { i }$ is a user fixed effect that controls individual differences. We did not include week fixed effect in the regression as it is collinear with the independent variable of interest $A f t e r _ { t } .$ . Table 4 shows the descriptions and summary statistics.

Table 5 reports the results. After virtual identity disclosure, users gave significantly fewer $\mathit { 1 i k e s . } ^ { \prime \prime }$ Specifically, the number of “likes” per week per user decreased by $1 - \exp { ( - 0 . 2 5 2 ) } = 2 2 . 3 \%$ after the policy change. The result indicates that protective self-presentation motivation dominates in users’ motivations to give “likes” when the likers’ identity is visible (see Table 3).

Figure 2. (Color online) The Number of “Likes” on Each Day  
![](/api/attachments/NHS3EZQM/fulltext/images/b1aafbe1dcd5eb1da062ee48c490a67b4e36066fcf5a36e12c14599ba1130f90.jpg)

Effect of Policy Change on Quality of “Liked” Articles. We used four measures to evaluate article quality: swearword usage, idiom usage, readability, and num ber of shares. Swearword usage suggests low content quality (Cho and Kwon 2015), whereas idiom usage, readability, and number of shares are generally associated with high content quality. Using idioms can make the content more concise, vivid, and elegant (Jiao 2016) and improve the content’s opulence, picturesqueness, and impressiveness (Roberts 1944). As many Chinese idioms originate from fables, myths, and famous quotations, the use and appreciation of idioms can also signal one’s intellectual status (Jiao 2016). Content readability, that is, how easy it is for readers to understand the content, is critical for effective expression and communication (Zinsser 2001, Johnson et al. 2015) and has been used to measure online content quality in prior research (Khern-am-nuai et al. 2018). Additionally, the sharing of content is closely related to content quality. For example, it is found that scientific discoveries that are more positive, emotional, interesting, and useful, and those that reflect more positively on the sender, are more likely to be shared (Milkman and Berger 2014). Therefore, we also used the number of times each article was shared at the time of data collection as an indicator of its quality.

To generate the percentage of swearwords in each article, we performed text segmentation by splitting each article, which consists of a sequence of Chinese characters, into a list of words. (Each word can consist of one or multiple characters.) We then used the text analytics software Linguistic Inquiry and Word Count (LIWC) (Pennebaker et al. 2001) to generate the percentage of words in each article that matched the “swear” category in the Simplified Chinese LIWC2015 Dictionary; LIWC is widely used in the information systems and marketing literature (Berger and Milkman 2012, Goes et al. 2014). For the percentage of idioms, we matched the words in each article with an authoritative dictionary of Chinese idioms (Xu 2015) and calculated the percentage of idioms therein. The widely used readability indices, such as the Flesch Reading Ease and the Gunning-Fog index (Ghose and Ipeirotis 2011), are primarily designed for the English language and are not applicable to the Chinese content in our context. We thus adopted the main idea behind these indices and used the percentage of easy words to measure content readability. To identify easy words in each article, we utilized the word list provided by HSK, a standardized Chinese proficiency test for nonnative speakers.<sup>6</sup> Specifically, we used the word list of HSK level $^ { 6 , }$ which contains 5,000 Chinese words, in our analyses; using HSK levels 1 to 5 yields similar results.

Table 4. Main Variables at User-Week Level

<table><tr><td>Variable</td><td>Description</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td><td>N</td></tr><tr><td> $After_t$ </td><td>Dummy that equals zero if week  $t \leq 19$  and one if week  $t \geq 20$ </td><td>0.56</td><td>0.50</td><td>0</td><td>1</td><td>39,207,013</td></tr><tr><td> $LikeNbr_{it}$ </td><td>Number of articles that user  $i$  “liked” in week  $t$ </td><td>0.55</td><td>4.75</td><td>0</td><td>4,848</td><td>39,207,013</td></tr><tr><td> $LikeSwear_{it}$ </td><td>Average percentage of swearwords in the articles that user  $i$  “liked” in week  $t$ </td><td>0.08</td><td>0.41</td><td>0</td><td>100</td><td>5,051,701</td></tr><tr><td> $LikeIdiom_{it}$ </td><td>Average percentage of idioms in the articles that user  $i$  “liked” in week  $t$ </td><td>0.28</td><td>0.90</td><td>0</td><td>100</td><td>5,051,701</td></tr><tr><td> $LikeReadability_{it}$ </td><td>Average percentage of HSK words in the articles that user  $i$  “liked” in week  $t$ </td><td>53.31</td><td>14.46</td><td>0</td><td>100</td><td>5,051,701</td></tr><tr><td> $LikeShare_{it}$ </td><td>Average number of shares of the articles that user  $i$  “liked” in week  $t$ </td><td>66.19</td><td>159.64</td><td>0</td><td>1,883</td><td>5,051,701</td></tr></table>

Notes. The variables LikeSwear , LikeIdiom , LikeReadability , and LikeShare have fewer observations than the other variables, because the user week panel contains all users who “liked” at least one article during the whole period. If user i did not “like” any articles in week t, LikeNbr equals zero but LikeSwear , LikeIdiom , LikeReadability , and LikeShare are missing

To examine the effect of the policy change on the quality of articles that users “liked,” we estimated the following ordinary least squares (OLS) models:

$$
L i k e S w e a r _ {i t} = \beta_ {0} + \beta_ {1} A f t e r _ {t} + C o n t r o l V a r s _ {i t} + \mu_ {i} + \epsilon_ {i t},\tag{2}
$$

$$
L i k e I d i o m _ {i t} = \beta_ {0} + \beta_ {1} A f t e r _ {t} + C o n t r o l V a r s _ {i t} + \mu_ {i} + \epsilon_ {i t},\tag{3}
$$

$$
L i k e R e a d a b i l i t y _ {i t} = \beta_ {0} + \beta_ {1} A f t e r _ {t} + C o n t r o l V a r s _ {i t} + \mu_ {i} + \epsilon_ {i t},\tag{4}
$$

$$
L i k e S h a r e _ {i t} = \beta_ {0} + \beta_ {1} A f t e r _ {t} + C o n t r o l V a r s _ {i t} + \mu_ {i} + \epsilon_ {i t},\tag{5}
$$

Table 5. Effect of Policy Change on the Number of “Likes”

<table><tr><td>Dependent variableModel</td><td>LikeNbrPoisson</td></tr><tr><td>After</td><td>-0.252**(0.006)</td></tr><tr><td>Week</td><td>-0.025**(0.007)</td></tr><tr><td> $Week^2$ </td><td>-0.001**(0.000)</td></tr><tr><td>User fixed</td><td>Yes</td></tr><tr><td>Observations</td><td>39,207,013</td></tr></table>

Note. Cluster-robust standard errors in parentheses (clustered on user). $^ { * } p < 0 . 0 5 ; ^ { * * } p < 0 . 0 1 .$

where LikeSwear , LikeIdiom , and LikeReadability are the average percentage of swearwords, idioms, and HSK words, respectively, in the articles that user i “liked” in week $t ,$ and $L i k e S h a r e _ { i t }$ is the average number of shares received by the articles that user i “liked” in week t. We added week variable and its squared term in the regressions. We also controlled for article length (the number of Chinese characters, LikeLength) when the dependent variable is LikeSwear , LikeIdiom , or LikeReadability , as it tends to correlate with these text features (Huang et al. 2017).

Table 6 shows the results. The articles that users “liked” after the policy change tended to have fewer swearwords and more idioms, were more readable, and were shared by more people, all indicating a higher quality than before the policy change. This result sug gests the dominating influence of self-presentation motivation when virtual identity is disclosed.

## Robustness Checks

Supply Side of Articles. A potential concern is whether the changes in users’ giving “likes” are due to changes in the supply side of articles. It might be that fewer and higher-quality articles were posted after the policy change, thus leading to the “liking” behaviors observed in the previous sections. We conducted three analyses to address this concern. We report the broad findings here and provide the details in Online Appendix B. First, we examined the supply side of articles at the discussion group level. The data set consists of all the 61,607 groups that posted at least one article during the study period. The results show that the number and characteristics of articles posted in each group each week after the policy change were not significantly different from those posted before the policy change. Second, we conducted an article-level analysis of the supply side. The data set consists of all the articles posted during the study period. The results indicate that the characteristics of the articles posted before and after the policy change were not significantly different. Third, we accounted for the influence of the supply side on users’ “liking” behavior by adding the number and characteristics of articles posted each week as control variables in Equations (1)–(5). The results are consistent with the results of the baseline regressions. These three analyses minimize the concern that the observed changes in users’ giving “likes” were caused by the changes in the supply side of articles.

Table 6. Effect of Policy Change on Quality of “Liked” Articles

<table><tr><td>Dependent variable Model</td><td>LikeSwear OLS (1)</td><td>LikeIdiom OLS (2)</td><td>LikeReadability OLS (3)</td><td>LikeShare OLS (4)</td></tr><tr><td rowspan="2">After</td><td>-0.009**</td><td>0.022**</td><td>0.686**</td><td>4.357**</td></tr><tr><td>(0.001)</td><td>(0.002)</td><td>(0.025)</td><td>(0.260)</td></tr><tr><td rowspan="2">Week</td><td>0.000*</td><td>-0.003**</td><td>0.027**</td><td>-0.442**</td></tr><tr><td>(0.000)</td><td>(0.000)</td><td>(0.002)</td><td>(0.022)</td></tr><tr><td rowspan="2"> $Week^2$ </td><td>0.000</td><td>0.000**</td><td>0.000</td><td>0.016**</td></tr><tr><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td>(0.001)</td></tr><tr><td rowspan="2">LikeLength</td><td>0.000**</td><td>0.000**</td><td>-0.000**</td><td></td></tr><tr><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td></td></tr><tr><td>User fixed</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>5,051,701</td><td>5,051,701</td><td>5,051,701</td><td>5,051,701</td></tr><tr><td> $R^2$ </td><td>0.234</td><td>0.223</td><td>0.309</td><td>0.290</td></tr></table>

Note. Cluster-robust standard errors in parentheses (clustered on user). \*p < 0.05; \*\*p < 0.01.

Monthly Aggregated Data. As the main results in Tables 5 and 6 are based on weekly data, we performed robustness analyses using monthly data. Every four weeks were aggregated as a month, and the data set consists of four months before and six months after the policy change. The results are consistent with our main results (see Online Appendix C).

## Heterogeneous Effects

To better ascertain the dominating role of selfpresentation motivation in users’ giving “likes,” we investigated the effect of the policy change for different types of users. If the behavior was driven by selfpresentation motivation, the policy change should have a stronger impact on those who cared more deeply about their image. We infer the extent to which users cared about their image by (i) the number of followers they had and (ii) the level of their content generation activities before the policy change. Users with more followers enjoy higher visibility on the platform, which should cause them to attach greater importance to their image (Ariely et al. 2009, Qiu and Kumar 2017). Research points out that individuals often use the content that they generate on social media (e.g., posting status updates, photos, comments, etc.) for self-presentation (Schau and Gilly 2003, Shriver et al. 2013, Zeng and Wei 2013); ceteris paribus, users who care more about their self-presentation are thus more likely to actively generate content to achieve and/or promote their desired identity for others to see. By extension, we expect these users to also use “liking” for self-presentation.

Given our research setting, we used the number of followers the respective users had and the total number of articles they posted before the policy change as indicators of how much they cared about their image. We extended the baseline specifications by adding the interaction of these indicators with $A f t e r _ { t }$ in Equations (1)–(5). We present the results in Online Appendix D. Consistent with the results in Tables 5 and 6, users generally “liked” fewer but higher-quality articles after the policy change. Furthermore, these effects are larger for users who, before the policy change, had more followers and were more active on the platform. The result indicates that the more users care about their image, the more they are affected by virtual identity disclosure, which is consistent with the prediction of self-presentation motivation. These results provide evidence for the dominating role of self-presentation motivation.

## Difference-in-Differences (DID) Analysis

In the above analyses, we examined the impact of the policy change by comparing users’ “liking” behavior before and after virtual identity disclosure. Because all the users in the group discussion section were exposed to the policy change, we lacked a control group of users who were not affected by the policy change. This raises a concern of confounding factors causing changes in users’ giving “likes.” We thus conducted a DID analy sis to ascertain the causal effect of the policy change. Specifically, we utilized users’ commenting behavior as the control group for their “liking” behavior, as the commenting function on the platform did not experience the policy change of virtual identity disclosure (i.e., commenters’ usernames were disclosed through out the study period). We focused on the 405,795 users in our data set who had both “liking” and commenting activities during the study period. The results show that users’ “liking” activities decreased relative to their commenting activities after the policy change.

A fundamental assumption underlying the DID approach is that the pretreatment trends are parallel between the treatment and control groups (Bertrand et al. 2004, Angrist and Pischke 2008). We tested the parallel trend assumption using a relative time model (Greenwood and Wattal 2017, Huang et al. 2017, Lu et al. 2019) and found no pretreatment differences in trends between the control and treatment groups. Details of this analysis are reported in Online Appendix E.

## Discussion and Conclusion

This research examines how virtual identity disclosure affects users’ giving “likes” to content on communitybased platforms. As shown in Table 2, this study differs from the existing literature by comparing three user motivations to identify the dominant motivation in users’ “liking” behavior. Our findings suggest that when likers’ virtual identity is visible, protective selfpresentation, that is, the motivation to avoid negative impressions and social disapproval, is dominant in users’ giving “likes.” Specifically, after virtual identity disclosure, the number of “likes” each user gives decreases significantly, but the quality of the “liked” articles increases. Also, the impact of virtual identity disclosure may be more substantial for users who care more about their image.

This study has important theoretical and practical implications. It highlights the role of virtual identity in affecting platform user behaviors. Although users pseudonym identity is unrelated to their real-world identity, virtual identity disclosure still significantly affects their behaviors. A theoretical implication is that users’ identity should not simply be considered anonymous even if they do not provide real-world identifying information. This is important, as many prominent platforms only reveal users’ virtual identity (e.g., Reddit, Stack Overflow, Quora). Future research should thus expand the scope of users’ identity to include virtual identity in addition to real identity.

Another theoretical insight is that platform policies and features can strongly influence the dominant motivations underlying certain user behaviors. In our case, intrinsic utility motivation, which was likely the primary motive for giving “likes” when likers were anonymous (and the reason we observed the “likes” before the policy change), took a back seat to self-presentation motivation when the platform disclosed likers’ virtual identity. This affected users’ “liking” behavior. Future studies should thus consider platform policies and features when examining users’ activities and motivations to better understand how platform-based contextual factors drive users’ behaviors.

Our findings also contribute to a more holistic picture of users’ strategic self-presentation behaviors in community-based platforms. First, we differentiate between two modes of self-presentation, that is, acquisitive and protective self-presentation, and provide empirical evidence for their comparative strength. Our findings suggest that platform users are more motivated to avoid negative impressions than to pursue good ones. The more substantial influence of protective self-presentation than of acquisitive self-presentation can help explain the inhibition effect of (real or virtual) identity disclosure in this and previous studies (Huang et al. 2017, Pu et al. 2020). Self-presentation is not only about what individuals choose to do but also what they opt not to do. Thus, self-presentation research should account for activities individuals can do but intentionally avoid doing. Second, our findings indicate that besides cultivating desired impressions through posting content on online platforms (Toubia and Stephen 2013, Goes et al. 2014), users can achieve the same goal by “liking” others’ content. Because giving “likes” demands little effort and is scalable to a large amount of content, users may consider this a cost-effective way to complement other self-presentation activities. Research examining self-presentation on platforms should thus consider its roles in both posting and “liking” behaviors to avoid missing out on a significant portion of users self-presentation activities. This is particularly critical because a large proportion of users do not create content in online communities (Chen et al. 2010).

This research also provides practical contributions for various stakeholders. For platforms, this research sheds light on the impacts of their identity disclosure policy. Prior works have explored how identity disclosure shapes users in terms of the content they post (see Table 1). This research suggests that identity disclosure can also influence users’ giving of “likes,” which is a prominent feature on many platforms. Although identity disclosure can cause users to give fewer “likes” because of self-presentation considerations, it may lead them to “like” higher-quality content. Platforms can thus examine how their identity disclosure policy can complement other incentives to motivate users to identify quality content for them to use in their content ranking and recommendation algorithms.

Our results indicate that content creators should pay more attention to their target audience’s needs, especially when users’ identity is disclosed for content consumption behaviors. This is because the users may strategically give and withhold their “likes” for content for self-presentation. Thus, content creators who wish to improve content engagement (especially in terms of “likes” received) should craft their content in ways that help users present specific desired images. Although our analyses are based on swearword usage, idiom usage, and readability of articles, content creators should consider other ways to enhance their content for self-presentation purposes. The specific approaches to achieving this are likely to vary across and even within platforms; what is critical is that content creators understand the types of images their key audience wants to curate and plan the form and substance of their content accordingly.

We conclude by discussing the limitations of this study. First, our findings are based on a single interestbased community (Douban), which may limit the generalizability of the insights. Future studies can explore other types of communities, such as online brand communities or support group communities, to contribute to greater external validity. Second, our study focuses on the impact of one specific platform policy—virtual identity disclosure—on users’ “liking” behavior. Further research can examine other platform policies to provide additional practical implications for how platforms can motivate users to “like” high-quality content. For example, if likers’ identities were disclosed only to the content creator, the relative strength of the three motivations we identified might be different; relational motivation might play a more vital role, whereas self-presentation motivation might be weaker. Consequently, the impact of this policy on users “liking” behavior might differ. Third, our study highlights that users tend to “like” high-quality content to project a more positive image, but we did not investigate the different types of images that users may want to project. Subsequent works should address this limitation and build on our findings using other methodologies. For example, a survey-based study can explore whether users maintain an online persona similar to or distinct from their real-world identity.

## Endnotes

<sup>1</sup> See https://www.facebook.com/help/110920455663362 (accessed October 2024) and https://help.twitter.com/en/using-twitter/likingtweets-and-moments (accessed October 7, 2024).

<sup>2</sup> See https://www.facebook.com/help/1155510281178725/how-newsfeed-works/ (accessed October 7, 2024).

<sup>3</sup> See https://help.instagram.com/281388201973414 (accessed October 7, 2024).

<sup>4</sup> See https://www.linkedin.com/help/linkedin/answer/49410 (accessed October 7, 2024).

<sup>5</sup> See https://www.douban.com/partner/intro (accessed October 7, 2024).

<sup>6</sup> See https://en.wikipedia.org/wiki/Hanyu\_Shuiping\_Kaoshi (accessed October 7, 2024).

## References

Andreoni J, Bernheim BD (2009) Social image and the 50–50 norm: A theoretical and experimental analysis of audience effects. Econometrica 77(5):1607–1636.

Angrist JD, Pischke J-S (2008) Mostly Harmless Econometrics: An Empiri cist’s Companion (Princeton University Press, Princeton, NJ).

Ariely D, Bracha A, Meier S (2009) Doing good or doing well? Image motivation and monetary incentives in behaving proso cially. Amer. Econom. Rev. 99(1):544–555.

Arkin RM (1981) Self-presentation styles. Tedeschi JT, ed. Impression Management Theory and Social Psychological Research (Academic Press, New York), 311–333.

Bapna S, Benner MJ, Qiu L (2019) Nurturing online communities An empirical investigation. MIS Quart. 43(2):425–452.

Bapna R, Ramaprasad J, Shmueli G, Umyarov A (2016) One-way mirrors in online dating: A randomized field experiment. Man agement Sci. 62(11):3100–3122.

Barasch A, Berger J (2014) Broadcasting and narrowcasting: How audi ence size affects what people share. J. Marketing Res. 51(3):286–299.

Bartsch M, Subrahmanyam K (2015) Technology and self-presentation: Impression management online. Rosen LD, Cheever NA, Carrier LM, eds. The Wiley Handbook of Psychology, Technology, and Society (Wiley Blackwell, Chichester, UK), 339–357.

Baumeister RF, Leary MR (1995) The need to belong: Desire for interpersonal attachments as a fundamental human motivation. Psych. Bull. 117(3):497–529

Baumeister RF, Bratslavsky E, Finkenauer C, Vohs KD (2001) Bad is stronger than good. Rev. General Psych. 5(4):323–370.

Berger J (2014) Word of mouth and interpersonal communication: A review and directions for future research. J. Consumer Psych. 24(4):586–607.

Berger J, Milkman KL (2012) What makes online content viral? J. Marketing Res. 49(2):192–205.

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1):249–275.

Chen B, Marcus J (2012) Students’ self-presentation on Facebook: An examination of personality and self-construal factors. Com put. Human Behav. 28(6):2091–2099.

Chen Y, Harper FM, Konstan J, Li SX (2010) Social comparisons and contributions to online communities: A field experiment on Movielens. Amer. Econom. Rev. 100(4):1358–1398.

Cho D, Kwon KH (2015) The impacts of identity verification and disclosure of social cues on flaming in online user comments Comput. Human Behav. 51(Part A):363–372.

Christopherson KM (2007) The positive and negative implications of anonymity in internet social interactions: “On the internet, nobody knows you’re a dog.” Comput. Human Behav. 23(6):3038–3056.

Cialdini RB, Borden RJ, Thorne A, Walker MR, Freeman S, Sloan LR (1976) Basking in reflected glory: Three (football) field studies J. Personality Soc. Psych. 34(3):366–375.

DeAngelis M, Bonezzi A, Peluso AM, Rucker DD, Costabile M (2012) On braggarts and gossips: A self-enhancement account of word-of-mouth generation and transmission. J. Marketin Res. 49(4):551–563.

Diener E, Fraser SC, Beaman AL, Kelem RT (1976) Effects of deindividuation variables on stealing among Halloween trick-or-treaters. J. Personality Soc. Psych. 33(2):178–183.

Ellison NB, Vitak J, Gray R, Lampe C (2014) Cultivating social resources on social network sites: Facebook relationship maintenance behaviors and their role in social capital processes. J. Comput. Mediated Comm. 19(4):855–870.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclo sure in electronic markets. Inform. Systems Res. 19(3):291–313.

Fredheim R, Moore A, Naughton J (2015) Anonymity and online commenting: The broken windows effect and the end of drive-by com menting. Proc. ACM Web Sci. Conf. (ACM Press, New York), 1–8.

Froomkin AM (1999) Legal issues in anonymity and pseudonymity Inform. Soc. 15(2):113–127.

Gallus J (2017) Fostering public good contributions with symbolic awards: A large-scale natural field experiment at Wikipedia. Management Sci. 63(12):3999–4015.

Geva H, Oestreicher-Singer G, Saar-Tsechansky M (2019) Using retweets when shaping our online persona: Topic modeling approach. MIS Quart. 43(2):501–524.

Ghose A, Ipeirotis PG (2011) Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteris tics. IEEE Trans. Knowledge Data Engrg. 23(10):1498–1512.

Goes PB, Guo C, Lin M (2016) Do incentive hierarchies induce user effort? Evidence from an online knowledge exchange. Inform. Systems Res. 27(3):497–516.

Goes PB, Lin M, Au Yeung C-M (2014) “Popularity effect” in usergenerated content: Evidence from online product reviews. Inform. Systems Res. 25(2):222–238

Goffman E (1959) The Presentation of Self in Everyday Life (Anchor, New York).

Gonzales AL, Hancock JT (2011) Mirror, mirror on my Facebook wall: Effects of exposure to Facebook on self-esteem. Cyberpsych. Behav. Soc. Networking 14(1–2):79–83.

Greenwood BN, Wattal S (2017) Show me the way to go home: An empirical investigation of ride-sharing and alcohol related motor vehicle fatalities. MIS Quart. 41(1):163–187.

Hayes RA, Carr CT, Wohn DY (2016) One click, many meanings: Interpreting paralinguistic digital affordances in social media. J. Broadcasting Electronic Media 60(1):171–187.

Hennig-Thurau T, Gwinner KP, Walsh G, Gremler DD (2004) Electronic word-of-mouth via consumer-opinion platforms: What motivates consumers to articulate themselves on the internet? J. Interactive Marketing 18(1):38–52.

Huang N, Hong YK, Burtch G (2017) Social network integration and user content generation: Evidence from natural experiments. MIS Quart. 41(4):1035–1058.

Jabr W, Mookerjee R, Tan Y, Mookerjee VS (2014) Leveraging philanthropic behavior for customer support: The case of user support forums. MIS Quart. 38(1):187–208.

Jiang Z, Chan J, Tan BC, Chua WS (2010) Effects of interactivity on website involvement and purchase intention. J. Assoc. Inform. Systems 11(1):34–59.

Jiao L (2016) Chinese idioms. Chan S-W, Minett J, eds. The Routledge Encyclopedia of the Chinese Language (Routledge, London), 64–89.

Johnson SL, Safadi H, Faraj S (2015) The emergence of online community leadership. Inform. Systems Res. 26(1):165–187.

Kessler A (2012) The button that made Facebook billions. Wall Street Journal (February 2), https://www.wsj.com/articles/SB1000142 4052970204652904577196992203069570

Khern-am-nuai W, Kannan K, Ghasemkhani H (2018) Extrinsic versus intrinsic rewards for contributing reviews in an online plat form. Inform. Systems Res. 29(4):871–892.

Kilner PG, Hoadley C (2005) Anonymity options and professional participation in an online community of practice. Conf. Comput. Supported Collaborative Learn. 2005 (CSCL 2005) (International Society of the Learning Sciences, Taipei, Taiwan), 272–280.

Kobsa A, Patil S, Meyer B (2012) Privacy in instant messaging: An impression management model. Behav. Inform. Tech. 31(4): 355–370.

Kuem J, Khansa L, Kim SS (2020) Prominence and engagement: Different mechanisms regulating continuance and contribution in online communities. J. Management Inform. Systems 37(1):162–190.

Leary MR (1996) Self-Presentation: Impression Management and Inter personal Behavior (Routledge, Abingdon, UK).

Lee D, Hosanagar K, Nair HS (2018) Advertising content and consumer engagement on social media: Evidence from Facebook. Management Sci. 64(11):5105–5131.

Lu Y, Gupta A, Ketter W, van Heck E (2019) Information transparency in business-to-business auction markets: The role of win ner identity disclosure. Management Sci. 65(9):4261–4279.

Ma M, Agarwal R (2007) Through a glass darkly: Information technology design, identity verification, and knowledge contribu tion in online communities. Inform. Systems Res. 18(1):42–67.

Milkman KL, Berger J (2014) The science of sharing and the sharing of science. Proc. Natl. Acad. Sci. USA 111(Supplement 4): 13642–13649.

Moqri M, Mei X, Qiu L, Bandyopadhyay S (2018) Effect of “following” on contributions to open source communities. J. Management Inform. Systems 35(4):1188–1217.

Pennebaker JW, Francis ME, Booth RJ (2001) Linguistic Inquiry and Word Count (LIWC2001) (Lawrence Erlbaum Associates, Mahwah, NJ)

Pu J, Chen Y, Qiu L, Cheng HK (2020) Does identity disclosure help or hurt user content generation? Social presence, inhibition, and displacement effects. Inform. Systems Res. 31(2):297–322

Qiu L, Kumar S (2017) Understanding voluntary knowledge provision and content contribution through a social-media-based prediction market: A field experiment. Inform. Systems Res. 28(3):529–546

Roberts MH (1944) The science of idiom: A method of inquiry into the cognitive design of language. PMLA 59(1):291–306.

Samek AS, Sheremeta RM (2014) Recognizing contributors: An experiment on public goods. Experiment. Econom. 17(4):673–690.

Schau HJ, Gilly MC (2003) We are what we post? Self-presentation in personal web space. J. Consumer Res. 30(3):385–404.

Sheldon KM, Abad N, Hinsch C (2011) A two-process view of Facebook use and relatedness need-satisfaction: Disconnection drives use, and connection rewards it. J. Personality Soc. Psych. 100(4):766–775.

Shen W, Hu Y, Ulmer JR (2015) Competing for attention: An empirical study of online reviewers’ strategic behavior. MIS Quart. 39(3):683–696.

Shin D, He S, Lee GM, Whinston AB, Cetintas S, Lee K-C (2019) Enhancing social media analysis with visual data analytics: A deep learning approach. MIS Quart. 44(4):1459–1492.

Shriver SK, Nair HS, Hofstetter R (2013) Social ties and user generated content: Evidence from an online social network. Management Sci. 59(6):1425–1443.

Sumner EM, Ruge-Jones L, Alcorn D (2018) A functional approach to the Facebook Like button: An exploration of meaning, interpersonal functionality, and potential alternative response buttons. New Media Soc. 20(4):1451–1469.

Tice DM (1991) Esteem protection or enhancement? Self-handicapping motives and attributions differ by trait self-esteem. J. Personality Soc. Psych. 60(5):711–725.

Toubia O, Stephen AT (2013) Intrinsic vs. image-related utility in social media: Why do people contribute content to Twitter? Marketing Sci. 32(3):368–392.

Tsikerdekis M, Zeadally S (2014) Multiple account identity deception detection in social media using nonverbal behavior. IEEE Trans. Inform. Forensics Security 9(8):1311–1321.

Tsikerdekis M, Zeadally S (2015) Detecting and preventing online identity deception in social networking services. IEEE Internet Comput. 19(3):41–49.

Wasko MM, Faraj S (2005) Why should I share? Examining social capital and knowledge contribution in electronic networks of practice. MIS Quart. 29(1):35–57.

Wojnicki AC, Godes D (2017) Signaling success: Word of mouth as self-enhancement. Customer Needs Solutions 4(4):68–82.

Xia M, Huang Y, Duan W, Whinston AB (2012) Research note—To continue sharing or not to continue sharing? An empirical anal ysis of user decision in peer-to-peer sharing networks. Inform. Systems Res. 23(1):247–259.

Xu Z (2015) 新 华 成 语 词 典 (Xinhua Dictionary of Chinese Idioms) (TheCommercial Press, Beijing).

Zeng X, Wei L (2013) Social ties and user content generation: Evi dence from Flickr. Inform. Systems Res. 24(1):71–87.

Zhang XM, Zhu F (2011) Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev. 101(4):1601-1615.

Zimbardo PG (1969) The human choice: Individuation, reason, and order versus deindividuation, impulse, and chaos. Arnold WJ, Levine D, eds. Nebraska Symposium on Motivation, vol. 17 (Uni versity of Nebraska Press, Lincoln), 237–307.

Zinsser WK (2001) On Writing Well: The Classic Guide to Writing Nonfiction, 6th ed. (Collins, New York).

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
