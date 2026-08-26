---
otero_id: 20395
otero_key: "9A97K99D"
title: "Influence of content and creator characteristics on sharing disaster-related information on social media"
authors: "Lifang Li; Jun Tian; Qingpeng Zhang; Jiaqi Zhou"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103489"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Influence of content and creator characteristics on sharing disaster-related information on social media

Lifang Li , Jun Tian , Qingpeng Zhang , Jiaqi Zhou

PII: S0378-7206(21)00063-X DOI: https://doi.org/10.1016/j.im.2021.103489 Reference: INFMAN 103489

![](/api/attachments/9A97K99D/fulltext/images/ffb3bdf6b21a7d50f36bf3c8faaea69d319a2533df95bbc6f420c759fe23a98c.jpg)

To appear in: Information & Management

Received date: 26 July 2018 Revised date: 23 April 2021 Accepted date: 2 May 2021

Please cite this article as: Lifang Li , Jun Tian , Qingpeng Zhang , Jiaqi Zhou , Influence of content and creator characteristics on sharing disaster-related information on social media, Information & Management (2021), doi: https://doi.org/10.1016/j.im.2021.103489

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all lega disclaimers that apply to the journal pertain.

© 2021 Published by Elsevier B.V.

# Influence of content and creator characteristics on sharing disaster-related information on social media

Lifang Li (lilifang2-c@my.cityu.edu.hk), Department of Systems Engineering and Engineering Management at City University of Hong Kong, Hong Kong SAR, China.

Jun Tian (tianjun@xjtu.edu.cn), School of Management at Xi’an Jiao Tong University, Xi’an, Shaanxi, 710049, China.

Qingpeng Zhang (corresponding author, qingpeng.zhang@cityu.edu.hk), School of Data Science and the Department of Systems Engineering and Engineering Management at City University of Hong Kong, Hong Kong SAR, China.

Jiaqi Zhou (jiaqi.zhou@cityu.edu.hk), Department of Systems Engineering and Engineering Management at City University of Hong Kong, Hong Kong SAR, China.

## Abstract

Identifying the key factors of the disaster-related information propagation process can provide decision support for disaster management. This study characterizes the effects of content types, location, and social capital of social media users on the virality of disaster-related information. We found through the Weibo dataset of the Yiliang earthquake that the virality of different types of information can vary on the basis of the social capital of users who post the information. This study fills the current research gaps by examining the individual and joint effects of the content and creator characteristics on the virality of disaster-related information.

Keywords: emergency management, information sharing, content analysis, social capital

## 1. Introduction

In response to the sudden onset of disasters, people seek and share updated information to learn about a situation or to take protective measures through reliable social media [1, 2, 3]. The information-sharing behavior of users after disasters is different from that during normal circumstances [4]. For example, the propagation scale and speed of earthquake-related posts were larger and faster than those under normal situations after the 2011 Great Eastern Japan earthquake [5, 6]. Authorities must obtain useful information from social media in a timely manner and identify the needs of users from this rich data source by characterizing the information sharing behavior of the public [7, 9, 11, 12].

Content and creator characteristics are relevant to the virality of social media content [8]. A good understanding of factors that affect social media users’ information-sharing behaviors during disasters can help authorities (such as the Federal Emergency Management Agency and nongovernmental organizations) develop timely disaster responses. Moreover, such understanding can help them optimize crisis communication and information release strategies to aid victims, inform people about the situation, and help victims cope with the disaster effectively [1, 7,13-17].

During disasters, various types of information are widely available on social media [7, 9-11]. Previous research suggests that different types of disaster-related information exhibit distinct propagation patterns on Weibo [18, 19]. For example, casualty-related information is generally popular at the early stage of post-disasters, whereas donation-related information is common during the latter recovery stage [11, 19]. Such varying virality is the result of the dynamic information need of the public at different stages of disasters. Multiple post-disaster stages (i.e., response, recovery, and mitigation) exist, during which social media users have different motivations to share information [20]. The well-established situation awareness theory [21] and recent empirical studies [19, 20] indicated that certain types of situational information, such as casualties and speculations, are more viral than information that does not promote situational awareness during the early response stage. This difference is due to the urgent need to fill the information gap about a situation after the onset of disasters. People directly affected by disasters post the latest updates about a situation, and those who are not directly affected share such information [15, 23, 24]. The most recent updates often become less viral at the latter recovery and mitigation stages when the gap of such early situational information has been largely filled [11, 19]. Information about donation/volunteering, help-seeking, and caution and advice could become viral because social media users would like to provide the needed social support to help the recovery and reconstruction during the recovery and mitigation stages [20, 21]. These findings in the literature indicate that content type is an important factor that influences users’ disaster-related information-sharing behavior. Regardless of recent empirical studies on the type of disaster-related information, a theory-driven typology is needed to facilitate the analytics and modeling of such information in research and practice.

A number of factors, such as the emotional tone of the post, location of users, and social capital of users, may affect the virality of disaster-related information on social media in addition to the type of information. Disasters cause additional emotional reactions among the public [25-28]. Understanding the emotional responses of the public to a crisis would help authorities or crisis-corresponding organizations to establish their reputation or propose proper crisis-coping strategies [27]. After natural disasters, the primary emotions of the public are anxiety, sadness, and anger as the result of the sudden damage caused by a disaster [25]. The reasons are as follows: (a)

disasters often cause chaos, which makes the public anxious; (b) the public may become angry at authorities’ improper disaster response strategies; and (c) people express sadness or sorrow to show empathy [2, 23, 27-29]. Negativity bias theory suggests that a post with many negative words is likely to become viral [30, 31].

The location of social media users has been recognized to influence their information-sharing behavior [2, 32, 33]. People share and search for disaster-related information actively if they are located near a disaster [2, 34]. Posts by users who are geographically close to the epicenter of a disaster become viral because they can provide first-hand and credible information as eyewitnesses [32]. We hypothesize that disaster-related posts from users located near a disaster are likely to become viral. Moreover, evidence shows that posts of social media users who are located in urban areas are more likely to go viral than those of people who are situated in rural areas due to digital inequality and geographical homophily [102, 103].

The social capital of social media users affects the virality of their disaster-related posts [30]. In particular, structural capital, a type of social capital, positively affects the number of reposts of disaster-related information [35]. From the network perspective, the number of followers and followees of social media users can represent their structural capital [37, 38]. Recent studies indicate that authorities often take advantage of high social capital users to publish actionable information after disasters [15]; social bots also purposely target at these users (via hashtags, mentions, responses, and retweets) to spread rumors because of their considerable influence on the virality of information [38-40]. Information published by high social capital users is frequently reposted because high social capital generally indicates high credibility; thus, their information is considered credible [41, 42].

## JournalPre-proof

The virality of information on social media platforms can be quantified in several ways [28, 42,43, 44]: the number of reposts [43, 45], dissemination depth (the number of hops in a dissemination/diffusion chain) [44], dissemination speed (the time difference between the original post and the first reposts) [44-46], and the duration of posts (the time difference between the original post and the latest repost, representing the persistence of users’ interest in the post over time) [45]. Dissemination scale and depth are two natural and common measurements of the influence of a post [47]. Compared with the information under normal circumstances, disaster-related information should be disseminated in a timely manner to help people fill the information gap; thus, the speed of reposts is another important way to quantify virality [1, 28, 48, 49]. The duration between the posting time of the last repost and that of the original post is also widely applied to characterize the severity of disasters [45]. In the information diffusion perspective, researchers often try to maximize and to minimize diffusion time considers these four measures of virality during natural disasters to help authorities develop proper information release strategies.

In summary, content-related factors, such as content type, negative emotions in content, and creator-related factors (e.g., location of users and social capital of users) affect the dissemination of disaster-related information on social media [2, 26, 32, 33, 35]. However, none of the current studies integrated content and creator characteristics in a comprehensive manner on the basis of mutual theories. Hence, the extension of existing information release strategies in different disasters is limited. The importance of social media in information acquisition and propagation is growing. Therefore, authorities need to learn the effects of these factors on information sharing on social media to prepare effective responses and interventions during natural disasters to minimize the negative effects of crises [7, 50, 51, 52]. This urgent need calls for data-driven research to fill the three research gaps in the literature. (a) First, the typology of disaster-related information is not uniform. In the literature, different studies proposed their own typologies, which have commonalities and differences. A theory-driven typology that unifies existing typologies and can be applied in various natural disaster contexts is critically needed. (b) Second, to the best of our knowledge, no study has accounted all the aforementioned main factors of the virality of disaster-related information, X including content type, emotion, and location, and the moderating effect of social capital. (c) Third, virality can be measured from multiple perspectives, including number of reposts, depth of reposts, repost speed, and duration, each of which has direct practical implications. A comprehensive understanding of virality from all perspectives is crucial to the proper decision-making of authorities. To date, studies in the literature only examined some perspectives of virality [13, 45, 48, 49, 52].

To fill these research gaps, the overarching objective of this study is to examine the main and joint effects of the type and emotional tone of a piece of content and the content creator’s attributes on the virality of disaster-related information on social media. Specifically, we aim to answer the following research questions:

(1) Does the virality of the different types of disaster-related information vary?

(2) Does the emotional tone of a disaster-related post positively affect its virality?

(3) Does the geographic location of a social media user significantly affect the virality of his/her post?

(4) Does social capital positively affect the virality of a disaster-related post?

(5) Does the effect of content type of the post and the location of social media users on its virality depend on the social capital (number of followers/followees) of these users?

By answering these questions and filling the current research gaps, this study contributes to IS (Information Systems) research in the following ways. First, this study integrates content- and creator-related factors to help authorities develop efficient disaster-related information releasing strategies. Second, we create a theoretical typology of disaster-related information on the basis of situational awareness and social support theories [10, 21, 53]. In particular, we group casualties and damages, doubt-casting, pleas for help, caution and advice, and donation-related information into situational information according to situational awareness theory. We further categorize donation-related, help-seeking, and caution and advice information into social support-related information [20, 54, 55]. Such theory-based categorization of natural disaster-related information provides knowledge bases for emergency information system developers and researchers. The researchers verify the importance of different types of disaster-related information. Third, this study extends social capital theory by testing the moderating effect of the social capital of social media users on the effects of content type, content emotional tone, and physical location of users to the virality of disaster-related information. Fourth, this study describes the virality of disaster-related information from four perspectives (number of reposts, depth of reposts, repost speed, and duration) to help other researchers understand the information-reposting behavior of users in a comprehensive perspective.

This study also contributes to practice. Proper information-publishing strategies need to be formulated to ensure the efficient dissemination of disaster-related information [56]. Emergency responders can employ precise information-publishing strategies on the basis of the information needs of the public by examining the effects of content type, negative emotions of a post, physical location of users, and social capital of social media users on virality (four varying perspectives of virality) of disaster-related information. This study helps emergency responders develop contingency information release plans by categorizing disaster-related information into several types according to theories.

This study is organized as follows. We review the existing literature about the effects of information sharing in this section. We establish the theoretical foundation and propose related hypotheses in Section 2. Earthquake-related Weibo posts that were published within three months during the Yiliang earthquake were gathered. Subsequently, we construct a 3-month propagation network for each type of disaster-related information and examine the reposted number, depth, and speed of shared information in Section 3. We conduct negative binomial regression analysis to test the hypotheses and draw conclusions Section 4. Finally, we discuss the implications and limitations of this study in Section

## 2. Theoretical Foundation and Hypothesis Development

## 2.1 Typology of disaster-related information

During disasters, various types of information are available on social media. Many typologies can be found in the literature. Table 1 summarizes the content types in detail.

Table 1. Summarization of the disaster-related content types in previous studies

<table><tr><td>Refs</td><td>Information types</td><td>Datasets</td></tr><tr><td>[20]</td><td>32 situational awareness types, e.g., advice, caution, evacuation, offer of help, request for help, request for information, damage, weather, environmental impact, etc.</td><td>Haiti Earthquake (2010); Oklahoma Fires (2009); Red River Flood (2009, 2010)</td></tr><tr><td>[9]</td><td>Personal only, informative (caution and advice, casualties and damage, donations of money, goods or service, people missing, found, or seen, information source)</td><td>Joplin tornado (2011)</td></tr><tr><td>[19]</td><td>Caution and advice, casualties and damage, donations of money, goods or service, help-seeking, personal only</td><td>Yiliang earthquake (2013)</td></tr><tr><td rowspan="2">[7]</td><td>Informational (actionable or non-actionable information) and non-informational information</td><td rowspan="2">Hurricane Sandy (2012)</td></tr><tr><td>Actionable information contains aid distribution, sheltering, donating, and volunteering</td></tr><tr><td>[57]</td><td>Initial information about disaster, situation updates, criticism about insufficient attention, moral support, preparations, criticism and control rumors, help request, offering help, self-organizing support, active volunteerism</td><td>Chennai flooding (2015)</td></tr><tr><td>[58]</td><td>Situational tweets (status updates, helping relief) and Non-situational tweets (sentiment or opinion, event analysis, charities)</td><td>Bomb blasts, Shoot, Flood, Typhoon</td></tr><tr><td>[59]</td><td>Opinion-related, situation update, emotion-related (providing social and emotional support), action-related (requesting help, looking for missing people, proposing relief actions), general earthquake-related, microblogging system-related, off-topic, and others</td><td>Yushu Earthquake (2011)</td></tr><tr><td>[10]</td><td>Affected individuals, infrastructures &amp; utilities, donations &amp; volunteer, caution &amp; advice, sympathy &amp; emotion &amp; support, other useful information</td><td>26 crises, e.g., earthquakes, floods, typhoon, bombings, etc. (2012–2013)</td></tr><tr><td>[60]</td><td>Reporting on the situation (from a personal perspective or second hand reporting), requesting help, coordinating relief efforts, providing mental counseling, criticizing the government, expressing well wishes and memorializing, discussing causes, connect community members</td><td>Typhoon Haiyan (2013)</td></tr><tr><td>[61]</td><td>Information sharing, information negotiation, information seeking, talking cure (expression of feelings and emotions), sharing individual actions, understanding the why (why the crisis happened), contemplating awareness, questioning the outcomes of the crisis, solidarity, opinion sharing</td><td>Brussels bombings (2016)</td></tr></table>

Table 1 shows that the typologies of natural disaster-related information in different studies have certain commonalities and differences [10, 23]. References [7, 9, 20, 58, 59] suggested that non-situational information (or noninformative information, personal only information, off-topics, and others) and situational information (informative information) are available in case of disasters. The situational information contains the following subtypes: (a) Casualties and damages, which are also named as affected individuals or infrastructures, situation updates, damage, and environment impact [9, 10, 19, 20, 60]; (b) doubt-casting or criticizing, which is also named as questioning, criticism about insufficient attention, and criticizing the government [57, 60, 61]; (c) caution and advice [9, 19, 20]; (d) donations of money, goods, or services, which was similar to the definitions of offer of help, offering help, providing social and emotional support, proposing relief actions, sympathy and emotion support, or donations and volunteer in other related papers [7, 9, 10, 19, 20, 59]; and (e) help-seeking, which is also named as request for help, request for information, and looking for missing people [19, 20, 59, 61]. Certain types of disaster-related information are context specific (e.g., the preparation-related [60], general-earthquake-related [59], and understanding the why [61]). In man-made disasters, such as Brussels bombings (2016), social media users attribute the reasons for the occurrence of such crisis [61]. In predictable disasters, such as flooding, the preparation-related information is contained [59].

Current studies reveal some commonalities of the disaster-related information types. Nevertheless, the underpinning theories are needed to consolidate the commonalities into a unified typology, which is general for various natural disaster contexts. In this study, we aim to provide such a typology, which applies the well-established situational awareness and social support theories. We categorize the disaster-related information into situational and non-situational information on the basis of the situational awareness theory. Furthermore, we categorize the situational information into social and nonsocial support-related information on the basis of the social support theory. Figure 1 and the following parts present the details.

![](/api/attachments/9A97K99D/fulltext/images/a33dc5aa822a78f098d11e8b869d18d403acacea1a6419d777f93ce5761c25a4.jpg)  
Figure 1. Types of disaster-related information.

Situational awareness refers to the perception of environmental elements and events [23]. By contrast, the non-situational information (or uninformative information) refers to the information that is “only of interest to its author and her immediate circle of family/friends” [9]. Non-situational information does not convey useful information to others in the same way as the situational doubt-casting or criticizing, caution and advice, donation of money/goods or services, and help-seeking. Information of casualties and damages is typically reported after disasters, thereby indicating the high situational awareness of the victims and the public [3, 17, 27, 62, 63]. Information of doubt-casting or criticizing is directly related to the responses and rescue actions of the authorities [2, 33, 34, 64]. Sharing such information helps others verify the truth or broaden their views to understand the crisis [57]. Caution and advice information notifies the public about how to protect themselves from disasters [9, 20]. Donations of money, goods, or services information helps the public and authorities (especially those who need help) to learn what types of help are available [20]. Help-seeking information spreads immediate help or assistance in crisis; sharing this type of information notifies the authorities and individuals who want to provide help to others [7].

The authorities apply social media to provide social support and communicate with the general public during disasters [7]. Therefore, the social support theory was chosen as the theoretical foundation to explain and theorize the differences of several types of situational information with other types of situational information because certain types of situational information have social support purposes [7, 19, 20]. Social support satisfies “individual’s physical, psychological, and cognitive needs” [65] through supportive social networks. The literature summarized four types of social support: emotional support, informational support, instrumental support, and appraisal support [7, 53, 65]. In a disaster context, situational information, such as caution and advice, donation of money/goods or services, and help-seeking, is summarized as actionable information that belongs to informational support [7], a type of social support. These types of disaster-related information provide not only informational support but also other types of social support (appraisal support or emotional support) to the social media users (Figure 1).

Specifically, (a) caution and advice information mainly notifies the public (including where to obtain shelter or to help) and provides informational and appraisal support because it helps the public evaluate their circumstances to protect themselves [7, 9, 19, 58]. (b) Donation of money, goods, or services is a form of instrumental support because donations are tangible aid and financial assistance; sharing this type of information provides informational support to the authorities and the public, especially to those who need help [7]. Moreover, sharing donation-related information is primarily motivated by empathy toward others, which also provides emotional support to others [11]. (c) Help-seeking information can enlighten responders or authorities regarding the type of help needed [9, 19, 66]. This information provides informational support to others by helping the victims get the needed social support (either tangible aid or emotional support) and notifying the volunteers where to provide collective support [7, 11]. Sharing help-seeking information is a type of collective coping behavior that provides emotional support to the victims [60]. However, the other two types of situational information, such as casualties and damages and doubt-casting or criticizing, which only provide informational support to others, are categorized as nonsocial support information to distinguish it from those situational information, which provides multiple types of social support (Figure 1).

## 2.2. Influence of content type on the virality of disaster-related information

Social media users reveal different information needs, motivations, or interactions for various types of information; the virality of information is highly correlated with the topic and the people’s interest in it [43, 52, 67]. The different types of information would induce different reposting behaviors of social media users. The virality of different types of information would vary. Among all different types of disaster-related information, non-situational information is irrelevant to situation updates of disasters. Thus, this information fails to motivate other users to share such information compared with situational information.

Situational awareness can influence people’s behaviors [23]. Situational information, such as casualties and damage of the disaster, would become viral because it helps people learn about the situation and properly respond to the crisis [20, 27, 68]. Information on casualties and damages is widely reposted by social media users, particularly within the first 24 h after an earthquake [19]. Situational information doubts and criticisms are likely to be reposted on social media during disasters [69-71]. People share such information because of the negativity bias during emergencies [2, 27, 33, 34]. In particular, the dissemination speed of information about the casualties and damages of disasters may be faster than that of other types of information because the former can ease the anxiety of the public who is eager to learn about the situation and know how to take proper action [27]. Thus, we propose the following hypothesis:

H1a: Situational information is more viral (especially in terms of reposted speed) than non-situational information after disasters.

Social support and situational information include caution and advice, donations of money/goods or services, and help-seeking information after disasters [61, 62]. Recent empirical research revealed that the dissemination scale of donation-related information is the second-largest among all types during earthquakes [19]. Sharing help-seeking information helps victims recover because the support of others can help them overcome hardship [60]. Spreading such information can help victims obtain the necessary details and provide a sense of care and companionship. Information on caution and advice, donations, and help-seeking may exhibit a slow repost speed because this type of information may not be needed immediately after disasters [19]. Nevertheless, social support-related information may reveal a substantial number of reposts, depth, and duration because people extensively discuss information to provide emotional, informational, intangible, or tangible support to others during disasters [7, 27]. Thus, we formulate the following hypothesis.

H1b: Social support-related information is more viral (especially in terms of the number of reposts, depth, and duration) than the nonsocial-support-related information after disasters.

## 2.3 Influence of negative emotions on disaster-related information sharing

Feelings-as-information theory suggests that emotions likely influence the decision-making of users when they experience uncertainty or feel intense emotions [6]. People show intense emotional reactions during crises, especially negative emotional reactions [26, 36, 72]. This concept might be explained by negativity bias theory, which indicates that people strongly react to negative information compared with positive or neutral information [36, 73, 74]. In social media, when people were reading microblog content, they were likely to be attracted to negative information and repost it [75]. In particular, negative emotions, such as anger, anxiety, and sadness, are commonly observed after natural disasters [25, 26, 76]. Sadness is the common emotion that the public expresses after suffering an unchangeable loss [77]. People express anxiety when they face immediate, concrete, and overwhelming danger, and they seek solutions to ease their anxiety [77]. Anger is expressed when the organizations that are accountable for harmful actions, including slow response of authorities [77]. Emotions could elicit cognitive processes, particularly attention, thereby increasing the likelihood of information sharing [30, 31]. The negativity bias theory suggests that posts with negative emotions are likely to become viral [78]. Therefore, we propose the following hypothesis:

H2: The high number of negative emotional words (i.e., sadness, anxiety, and anger) contained in disaster-related information indicates high likelihood for such information to become viral.

## 2.4 Influence of spatial distance on information sharing

Spatial distance affects the information-sharing behavior of social media users [13, 33]. Construal-level theory suggests that the spatial/physical distance of users from a certain event can positively affect their informational needs and information-searching behavior [33, 79, 80]. During a crisis, people located near an event are active in sharing information, and their posts are likely to go viral [32, 45, 81-84]. Individuals located near the crisis are likely to be the eyewitnesses who can provide real-time information to others [32]. Real-time information is in great need in case of disasters [38]. Thus, we hypothesize the following:

H3a: Posts from users near a disaster are more viral than those from users far from the disaster.

Social media users are located in urban and rural areas [84-86]. Posts from urban and rural users show significantly different viralities [18, 81, 83, 84]. Such a location bias is found on Twitter and Weibo [18, 87]. Rural users are lagging behind those who live in urban areas in terms of obtaining information due to digital inequality [85]. Accordingly, social media users who live in rural areas cannot share timely and updated news to others compared with those who live in urban areas [85]. However, the urgency and timeliness are important factors that increase the virality of information, particularly after disasters [38, 45]. Therefore, we hypothesize the following:

H3b: Posts from users who live in urban areas are more viral than posts from those who live in rural areas.

## 2.5 Effect of social capital on disaster-related information sharing

Social capital refers to resources or assets embedded in the networks of individuals or communities [88]. Social capital has three main dimensions: (a) relational dimension, which refers to the nature of forming personal relationships, such as trust, norms, and obligations; (b) cognitive dimension, which refers to the resources that provide shared representations, interpretations, and systems of meaning among parties; and (c) structural dimension, which refers to the social connections among individuals in the social network [88].

Social capital enhances the ability of individuals to obtain information [81]. The number of social interactions has been recognized as a valid measure of social capital, particularly the structural capital [88-90]. From the network perspectives, the number of followers and followees (friends) of social media users can represent their structural capital [37, 38, 91]. Users with many followees generally have high intensity and broad breadth in obtaining information [88, 90, 92]. Users with a considerable number of followers can broadcast their opinions to a wide audience [92].

Social media users’ number of followers/followees positively affects the retweet probability of their posts [92]. Post from users with a high number of followers (e.g., local news outlets and opinion leaders) are reposted for the high credibility or reliability [24, 90]. In emergency management, users’ structural capital affects the intensity of information dissemination [39, 93]. Thus, we propose the following hypothesis.

H4a: The social capital of users (number of followers/followees) positively affects the virality of disaster-related information.

Users who are efficient in spreading disaster-related information provide insights into effective communication strategies [91]. The influence of social capital on the virality of different types of information varies [94]. Users with high social capital (especially those with a high number of followers) are reliable for helping emergency response agencies publicize situational (informative) information [7, 95]. During recovery, these users serve as opinion leaders to motivate donations [24, 95]. Thus, we propose the following hypothesis.

H4b: The virality of situational information is positively moderated by the social capital of users after disasters.

In the context of crises, people tend to express more negative emotions [29, 128]. Such emotional posts are more likely to be reposted because of the collective empathy and support of social media users [97] and the negativity bias of users [30, 31]. For example, it was found that posts with negative sentiments were more likely to be reposted [36, 46], especially posts that feature words related to anger and anxiety in crises [36]. In addition, people who experienced intense crisis emotions are more likely to search for information that supports their emotional experiences according to the selectivity bias of crisis emotions [124]. It suggests that the more negative emotions (such as sadness, anxiety, or anger) experienced by individuals in crisis, the more likely they would repost posts with similar emotions. Considering the crisis emotion selectivity bias of individuals [124], the greater influence of high social capital users on other individuals’ emotions [129] and the higher chance of high social capital users’ posts being seen by other individuals [92], we hypothesize the enhanced positive influence of the high social capital users on the virality of posts with more negative emotions.

H4c: The positive influence of users’ social capital on the virality of the posts will be stronger if the post contained more negative emotional words (especially the posts with anxiety and sadness words).

People tend to seek accurate, relevant, and reliable information after disasters [116]. [24, 41, 36, 117]. For example, during the 2008 Mumbai crisis, eyewitness provided instant information on Twitter and Flickr [125]. Wiegand and Middleton (2016) highlighted the value of eyewitness information in social media for its novelty [126]. The eyewitnesses’ posts were used by the journalists to add credibility to their posts and to enlarge their influence [96] because credibility is one of the most important factors that are positively related to the virality of a post [8, 118]. During a crisis, people are more likely to repost information from trustworthy sources and high social capital users were found to be more trustworthy [119, 120]. Additionally, high social capital users in social media play a critical role in crisis communication for that they can produce high pass-on value information [127] and located in the important positions of their followership network [123]. Therefore, high social capital users who are located near the disasters can provide timely, novelty, and high credibility crisis information which leads to the stronger positive effects of high social capital users on the virality of posts for users who are located near disasters. The following hypothesis was formulated:

H4d: The positive influence of users’ social capital on the virality of disaster-related information will be stronger if the information publisher located near the disaster area.

Timely information is viral, especially in crises [119]. Compared with rural users, urban users have more opportunities to obtain updated and timely information due to digital inequality [85]. Thus, information from urban users is more likely to go viral, especially in a time-critical crisis [121]. To spread information quickly (especially in a crisis), high social capital users are important because of the high pass-on value of their information [127] and their critical role in their followership networks [123]. It was found that the content generated by high social capital users was more widely reposted [35, 36]. Therefore, we argue that the positive effects of high social capital users on the virality of disaster-related posts will be stronger for users located in the urban area than for users located in the rural area because of their higher ability to get updated crisis information. The following hypothesis was formulated:

H4e: The positive influence of users’ social capital on the virality of disaster-related information will be stronger if the information publisher located in the urban areas.

We use the types and emotions contained in the posts and the location and social capital-related factors (e.g., number of followers/followees) of social media users as independent variables. These factors are assumed to affect the virality of posts (represented by the number of reposts, reposted depth, reposted speed, and duration). Figure 2 illustrates the theoretical model.

![](/api/attachments/9A97K99D/fulltext/images/9b503e15c166f119581d3efae806b3f16e754c9fd954b22bf09762a5bbf34e23.jpg)  
Figure 2. Theoretical model

## 3. Data and Methodology

## 3.1 Data collection

A series of earthquakes occurred on September 7, 2012 in Yiliang (彝良), Yunnan Province. The first epicenter was located slightly far from the county (15 kilometers away), whereas the second epicenter was only five kilometers away. The second epicenter was closer to a densely populated area and was more destructive than the first epicenter. Until September 8, 2012, the earthquake affected 183,000 people, including 80 deaths. A total of 7,138 houses collapsed, and 30,600 rooms were damaged.

After the Yiliang earthquake, Weibo provided users (victims and non-victims) a channel to obtain information and share feelings with others. The authorities also made several notifications to guide the public. We used the public application program interfaces provided by Weibo for data collection. We collected 9,396 original posts and their reposts containing the term “彝良” (Yiliang) and one of the following two terms, “震” (earthquake) and “灾” (disaster) from September 7, 2012 to December 7, 2012. Overall, we collected 244,424 posts. Each post contained information on the user ID, post ID, post content, posting time, user location, and number of followers and followees of the user. We also assigned each post with several other attributes, which will be discussed in the following sections.

## 3.2 Types of post

To identify how the type of content influences the number of reposts, the repost depth, and the repost speed of disaster-related information, we manually labeled 9,389 credible (seven of the original posts were deleted during the manual labeling process because they contained speculative information) posts, classified them into six types, and set the reposts as the same type as the original posts. The first four types, namely, personal-related and others; caution and advice; casualties and damages; and donation of money, goods, or services were borrowed from Imran et al. [9]. Help-seeking was defined in the literature [19]. Doubt casting was defined after discussing with a domain expert and referring to related literature [57]. The definitions of the content types are as follows:

 Type 1: Personal-related and others. This type conveys users’ emotions, such as sorrow.

 Type 2: Caution and advice. This type conveys a warning or advice about potential hazardous outcomes of an incident.

 Type 3: Casualties and damages. This type reports information about the casualties or damages resulting from an incident.

 Type 4: Donation of money, goods, or services. This type conveys information about how much money has been raised for the victims, the goods/services offered to them, or their pleas for help.

 Type 5: Help-seeking. This type reports information about people who went missing or were displaced during the disaster.

 Type 6: Doubt casting. This type conveys information about the doubts casted on the efficiency of disaster relief procedures conducted by the authorities.

The methodologies of Krippendorff and Landis and Koch were applied for the content labeling of all the original posts [97, 104]. Three graduate students were recruited to manually perform two rounds of labeling work. In the first round, we did a pilot labeling work of 1,000 posts and obtained an average Cohen kappa of 0.64, which was within the substantial interval [0.61, 0.80]. In the second round, we labeled the remaining 8,389 posts and obtained a kappa value of 0.76 after further discussions. The labeling results are summarized in Table 2.

On the basis of situational awareness and social support theories, we summarized Type 1 information as non-situational information. Types 2 and 3 information were labeled as situational information. Types 4, 5, and 6 information were summarized as social support-related information.

Table 2. Labeling results of Yiliang earthquake-related original posts

<table><tr><td></td><td>Type of Content</td><td>Manual Labeling</td></tr><tr><td>Non-situational</td><td>1—Personal-related and others</td><td>638</td></tr><tr><td rowspan="2">Situational</td><td>2—Casualties and damages</td><td>4,127</td></tr><tr><td>3—Doubt casting</td><td>899</td></tr><tr><td rowspan="3">Situational and social support-related</td><td>4—Caution and advice</td><td>156</td></tr><tr><td>5—Donation of money, goods or services</td><td>3,108</td></tr><tr><td>6—Help-seeking</td><td>461</td></tr><tr><td>Total</td><td></td><td>9,389</td></tr></table>

## 3.3 Physical location of user

The physical location of social media users has a significant influence on their information-sharing behavior, especially under the circumstances of disasters. We developed a binary variable named Neighbor to measure a such effect. We used the relative distance from Yiliang to Chongqing as our radius and placed Yiliang at the center of the circle. If a user is located in the area mainly affected by the earthquake, then the value of Neighbor is 1, and 0 otherwise. We also developed a binary variable named Urban to differentiate urban users from rural users. If a user is

## 3.4 Emotions of post

To identify the emotions of posts published within the three months of the earthquake, we processed them using the Linguistic Inquiry and Word Count (LIWC) software [105]. Subsequently, we grouped them into a single text sample to be evaluated using the LIWC Chinese dictionary. Specifically, we used three negative emotions: anxiety, anger, and sadness.

## 3.5 Social capital-related factors

According to social capital theory, the relationship network of an actor and the resources embedded in such a network strongly affect his/her knowledge-sharing behavior [106]. Under the circumstances of disasters, posts of users with a large number of social ties and a high structural capital are highly likely reposted [43]. In this study, the numbers of followers and followees were directly obtained from the dataset and were labeled as Follower and Followee, respectively.

## 3.6 Control variables

The authority and authenticity of a user have significant effects on the virality of information [33, 39]. If a social media user has high credibility, then the information he or she posts is likely reposted by others [3, 39, 107]. Weibo has a unique user verification feature to verify the true identity of users. A Weibo study shows that such verifications can enhance the credibility of Weibo users and establish their authenticity [108]. Naturally, the information posted by verified authorities is highly viral and can affect our research, which is focused on the public. Therefore, we controlled this variable by defining verified users with more than 10,000 followers as authorities. In addition, we used a dummy variable Authority to represent whether a user is an authority or not.

The URLs, videos, pictures, and hashtags included in a post can significantly influence the information-sharing behavior of users [92, 109-112]. On the one hand, given that URLs contain plenty of information about certain topics, posts with URLs have a high tendency of being reposted [92, 111]. On the other hand, hashtags summarize the main idea and clarify the content of posts; thus, posts that include hashtags have high chances of being shared [110, 111]. After a disaster occurs, times the posts are reposted [107, 113]. The publication time of a post can also significantly affect the number of reposts, that is, a post that is published early has high chances of being reposted [110]. In addition, the authenticity of users (measured by whether users have verified their true identity on Weibo) is expected to positively affect the virality of information [33]. Lastly, posts that mention other users (using the @ symbol) positively affect the virality of information [88].

In this study, the publication time of posts was also considered in the analysis. The number of hours between the posting time and the occurrence of the disaster was used to represent this variable, which was labeled as Time. The social media engagement of users was labeled as Involvement and was represented by the number of disaster-related posts published by users within three months of the earthquake. The numbers of hashtags and URLs were calculated and named as Hashtag and URL, respectively. Videos or pictures were calculated and labeled as Video and Picture, respectively. Posts with videos or pictures were given 1, whereas those without them were given a value of 0.

## 3.7 Extraction of the propagation scale, depth, speed, and duration

We obtained our dependent variable propagation scale (number of reposts) directly from the dataset. Specifically, we measured the speed by calculating the inverse of the time difference between the first repost and the original post. To measure reposted depth, we constructed propagation networks for each type of post and then calculated the depth of each node. Given that a period of three months is critical for earthquake recovery, we constructed 3-month propagation networks of the type of posts. In these networks, each node represented a unique user ID, whereas a directed edge represented the sink node, which reposted one or more original posts from the source node. For example, if user A reposts the original post of user B, then an edge is drawn from nodes B to A, indicating that the information propagates from B to A.

Afterward, we calculated the maximum path length of each node when it was the source of the network. Figure 3 shows the number of reposts and reposted depth in great detail. The blue dashed line represents the information flow of the post published by user A. Assume that this user posts “Gosh, another earthquake! Please inform us of the donation channels!” and users B1–B6 share this post. Subsequently, the post that is reshared by user B4 is reshared again by users C2 and C3. In this case, the post of user A is already reposted eight times, thus having an equivalent reposted depth of two. For the reposted speed (time lags), if B3 is the first user who reposts A’s post, then the reposted speed is the deviation of the publishing time of B3 and A. For the duration of A’s post, if C1 is the last user who reposts A’s post, then the duration of the post is the deviation of the publishing time of

## C1 and A.

![](/api/attachments/9A97K99D/fulltext/images/bb166761b63d830686cc5fa11d0b1168cb4ae03d04836553a4d70763b80277dd.jpg)  
Figure 3. Indication of the reposted amount, depth, speed, and duration of a post.

## 4. Empirical Analysis

## 4.1 Descriptive statistics of variables

The definitions and statistics of the variables included in our model are summarized in Table 3. To note that, for the numerical variables the mean, maximum value, minimum value, and the deviation are summarized; for the categorical variables, the coded number of the variable and its amount are summarized. Moreover, to generally compare the varying viralities of each type of posts, we summarized the average reposted count, depth, speed, and duration for each type of disaster-related posts in Table 3.

Table 3. Summary statistics of the variables for regression analyses.

<table><tr><td>Variables</td><td>Descriptions</td><td>Mean</td><td>Max</td><td>Min</td><td>Std. dev.</td></tr><tr><td colspan="6">Dependent variables (viralities)</td></tr><tr><td>Reposted amount</td><td>Number of reposts.</td><td>68.64</td><td>102,500</td><td>0</td><td>1755.77</td></tr><tr><td>Reposted depth</td><td>Maximum number of propagations between the original post and reposts.</td><td>1.113</td><td>86</td><td>0</td><td>2.59</td></tr><tr><td>Reposted speed</td><td>Inverse number of hours between the publishing time of the first repost and the original post.</td><td>11.91</td><td>5,397</td><td>0</td><td>55.73</td></tr><tr><td>Duration</td><td>Number of hours between the publishing time of the last repost and the original post.</td><td>79.79</td><td>5,524</td><td>0</td><td>461.2</td></tr><tr><td colspan="6">Independent variables</td></tr><tr><td>Type</td><td>The manually labelled results of all the original posts.</td><td></td><td></td><td></td><td></td></tr><tr><td>Neighbor</td><td colspan="5">Indicator of whether the sharer of a post is located in an urban area: 0:7727; 1: 1662</td></tr><tr><td>Urban</td><td colspan="5">Indicator of whether the sharer of a post is located near an earthquake-affected area: 0:7128; 1:2261</td></tr><tr><td>Anxious</td><td>Anxious-related word count ratio of LIWC results</td><td>0.41</td><td>22.2</td><td>0</td><td>1.20</td></tr><tr><td>Anger</td><td>Anger-related word count ratio of LIWC results</td><td>0.74</td><td>33.3</td><td>0</td><td>1.83</td></tr><tr><td>Sad</td><td>Sad-related word count ratio of LIWC results</td><td>0.87</td><td>33.3</td><td>0</td><td>1.77</td></tr><tr><td>Followers</td><td>Log-transformed number of followers of the users</td><td>819</td><td>121,600</td><td>0</td><td>816,003</td></tr><tr><td>Followees</td><td>Log-transformed number of followees of the users. Control variables</td><td>594.5</td><td>3,000</td><td>0</td><td>627.5</td></tr><tr><td>Involvement</td><td>Number of disaster-related posts posted by users</td><td>1.27</td><td>6</td><td>1</td><td>0.85</td></tr><tr><td>Hashtag</td><td>Indicator of whether a post contains hashtags or not</td><td colspan="4">0: 5,906; 1:3,483</td></tr><tr><td>URL</td><td>Indicator of whether a post contains URLs or not</td><td colspan="4">0:5,721; 1: 3,668</td></tr><tr><td>Time</td><td>Number of hours between the occurrence of the earthquake and the publication of the original post</td><td>852.0</td><td>5,614</td><td>0.2</td><td>1,224</td></tr><tr><td>Video</td><td>Indicator of whether a post contains videos or not</td><td colspan="4">0:9,289; 1:100</td></tr><tr><td>Picture</td><td>Indicator of whether a post contains pictures or not</td><td colspan="4">0:9,083; 1:306</td></tr><tr><td>Authority</td><td>Indicator of whether a user is influential or an authority (verified users with a least 10,000 followers)</td><td colspan="4">0:7,746; 1:1643</td></tr></table>

Table 4. Average viral degree of different types of information.

<table><tr><td>Content Type</td><td>Total posts #</td><td>Reposted amount</td><td>Reposted depth</td><td>Reposted speed</td><td>Duration</td></tr><tr><td>1—Personal-related and others</td><td>638</td><td>62.02</td><td>0.78</td><td>7.89</td><td>54.31</td></tr><tr><td>2—Casualties and damages</td><td>4,127</td><td>54.22</td><td>1.14</td><td>10.83</td><td>83.95</td></tr><tr><td>3—Doubt casting</td><td>899</td><td>18.10</td><td>0.75</td><td>4.51</td><td>63.15</td></tr><tr><td>4—Caution and advice</td><td>156</td><td>10.57</td><td>1.42</td><td>7.67</td><td>88.11</td></tr><tr><td>5—Donation of money, goods, or services</td><td>3,108</td><td>101.49</td><td>1.01</td><td>8.05</td><td>72.41</td></tr><tr><td>6—Help-seeking</td><td>461</td><td>103.56</td><td>2.51</td><td>15.14</td><td>157.20</td></tr></table>

Table 4 presents the average reposted counts of different types of information. In general, personal-related information and others tend to be less viral in terms of reposted depth, speed, and duration, whereas the reposted amount is higher for situational awareness and social support-related information. Donation and help-seeking-related posts are the most reposted. Help-seeking-related quite different reposting behaviors with regard to this type of information. Posts related to casualties and damages—and doubt casting also exhibit long duration, but their reposted amount is not as high as compared with other types.

Table 5. Correlation matrix of independent variables.

<table><tr><td></td><td>Type</td><td>Followers</td><td>Followees</td><td>Involvement</td><td>Anxious</td><td>Anger</td><td>Sad</td><td>Neighbor</td><td>Urban</td><td>Hashtag</td><td>URL</td><td>Time</td><td>Video</td><td>Picture</td><td>Authority</td></tr><tr><td>Type</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Followers</td><td>-0.02</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Followees</td><td>-0.02</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Involvement</td><td>-0.05</td><td>0.07</td><td>0.15</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Anxious</td><td>-0.003</td><td>0.01</td><td>-0.004</td><td>-0.005</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Anger</td><td>-0.01</td><td>0.01</td><td>0.03</td><td>-0.06</td><td>0.05</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sad</td><td>0.07</td><td>-0.03</td><td>-0.09</td><td>-0.08</td><td>0.24</td><td>0.03</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Neighbor</td><td>-0.10</td><td>-0.04</td><td>0.02</td><td>0.30</td><td>0.004</td><td>-0.06</td><td>-0.10</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Urban</td><td>0.004</td><td>0.14</td><td>0.04</td><td>-0.05</td><td>0.03</td><td>0.02</td><td>-0.02</td><td>-0.26</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Hashtag</td><td>0.03</td><td>0.11</td><td>0.06</td><td>-0.03</td><td>0.08</td><td>0.13</td><td>0.04</td><td>-0.13</td><td>0.02</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>URL</td><td>0.09</td><td>0.02</td><td>-0.06</td><td>-0.08</td><td>0.007</td><td>-0.04</td><td>0.26</td><td>-0.10</td><td>0.06</td><td>0.14</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>Time</td><td>0.09</td><td>0.01</td><td>0.07</td><td>3.5e-4</td><td>-0.001</td><td>-0.007</td><td>-0.08</td><td>0.11</td><td>-0.02</td><td>-0.02</td><td>-0.15</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>Video</td><td>-0.006</td><td>0.02</td><td>-0.004</td><td>-0.02</td><td>-0.004</td><td>-0.002</td><td>-0.03</td><td>-0.02</td><td>-0.003</td><td>0.008</td><td>0.08</td><td>-0.02</td><td>1.00</td><td></td><td></td></tr><tr><td>Picture</td><td>-0.07</td><td>0.04</td><td>0.02</td><td>0.02</td><td>-0.02</td><td>-0.05</td><td>-0.06</td><td>0.003</td><td>0.002</td><td>-0.001</td><td>0.04</td><td>-0.04</td><td>-0.007</td><td>1.00</td><td></td></tr><tr><td>Authority</td><td>-0.05</td><td>0.28</td><td>0.16</td><td>0.29</td><td>-0.006</td><td>-0.01</td><td>-0.11</td><td>0.11</td><td>0.12</td><td>0.17</td><td>-0.08</td><td>0.07</td><td>0.004</td><td>0.02</td><td>1.00</td></tr><tr><td> $VIF^1$ </td><td>1.37</td><td>3.07</td><td>1.43</td><td>1.24</td><td>1.08</td><td>1.11</td><td>1.23</td><td>1.24</td><td>1.13</td><td>1.16</td><td>1.19</td><td>1.09</td><td>1.02</td><td>1.02</td><td>2.28</td></tr></table>

Table 5 indicates that each pair of independent variables did not show high correlation, whereas their VIFs were all lower than 5. Therefore, these independent variables were suitable for the regression analysis. The dependent variables’ skewed distribution and over-dispersion were checked by calculating their mean and standard deviation.

In all the four measures of virality, such as reposted amount, depth, speed, and duration of the posts, we also calculated the correlations for the original data and the logarithmic transformation with the offset value of one for reposted amount, speed, and duration (in the brackets) in Table 6. The results indicated that the significant (at the level of p=0.001) positive linear correlations among the transformation. This result is reasonable because in the information propagation process, if one post can reach a large amount of people, then it may also have huge and deep reposted network. The post would be reposted in a large speed and attract great attention of people.

Table 6. Correlations among all the dependent variables.

<table><tr><td>Variables</td><td>Reposted amount</td><td>Reposted Depth</td><td>Reposted Speed</td><td>Duration</td></tr><tr><td>Reposted amount</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>Reposted depth</td><td>0.17 (0.82) ***</td><td>1.00</td><td></td><td></td></tr><tr><td>Reposted speed</td><td>0.06 (0.73) ***</td><td>0.25 (0.63) ***</td><td>1.00</td><td></td></tr><tr><td>Duration</td><td>0.28 (0.82) ***</td><td>0.45 (0.72) ***</td><td>0.14 (0.53) ***</td><td>1.00</td></tr></table>

The following multiple equations models were developed to simultaneously estimate the virality of the disaster-related information after transforming the dependent variables reposted count, reposted speed, and duration of the post into logarithms with the offset value of one to ensure that the model is convergent.

$$
V i r a l i t y = \beta_ {0} + \sum \beta_ {k} x _ {k} + \sum \beta_ {j} x _ {j} + \sum \beta_ {k q} x _ {k} \cdot x _ {q} + \sum \beta_ {m q} x _ {m} \cdot x _ {q} + u _ {i},\tag{1}
$$

in which,

?? = 1, 2, 3, 4, 5, 6; ?? = ??, ??, ??, ??1, ??2, ??3, ??, ??, ??, ℎ1, ℎ2, ??, ??, ??; ?? = ??, ??; ?? = ??1, ??2, ??3, ℎ1, ℎ2 where

 Virality of a post is indicated by the number of reposts, reposted depth, reposted speed, and duration of the post;

$x _ { k } = 1$ if a post belongs to type ??, and $x _ { k } = 0$ otherwise;

$x _ { a } = 1$ if a post contains a hashtag, and $x _ { a } = 0$ otherwise;

${ x } _ { b } = 1$ if a post contains a URL, and $x _ { b } = 0$ otherwise;

$x _ { c }$ denotes the publication time of the post;

$x _ { d 1 } , x _ { d 2 } , x _ { d 3 }$ denotes the frequency of anxious, sadness, and anger words contained in the post separately;

$x _ { e } , x _ { f }$ denotes the Log(followers) of user and the Log(followees) of user separately;

$x _ { h 1 } , x _ { h 2 } = 1$ if a post is published by a user located near the earthquake-affected area (in the urban area), and 0 otherwise;

$x _ { g }$ denotes the involvement of the user;

 $x _ { i } , x _ { j } = 1$ , if a post contains at least a video (or a picture), and 0 otherwise;

$x _ { w } = 1 , \mathrm { i f ~ a ~ p o s t }$ is published by the verified user whose follower is more than 10000, and 0 otherwise;

$u _ { i }$ is the random error.

All statistical analyses were undertaken using software “R” with the add-on package “systemfit”. We applied the ordinary least squares (OLS) approach to estimate the coefficients rather than the seemingly unrelated regression (SUR); we also applied the same regressors in each equation, and the OLS and SUR estimations result in identical estimation of the coefficients and their standard errors [114, 115]. The regression results of the multiple equations models were summarized in Section 4.2.

## 4.2 Regression results

We used multiple equations models for all the four dependent variables to test our hypotheses. For the reposted amount, reposted speed, and the duration of the post, we used the logarithmic form after adding one to all posts as the dependent variable to ensure that the model is convergent and performs well [for example, Log (?????????????????? ???????????? + $\begin{array} { r } { \mathbf { \rho } _ { 1 } ) = \beta _ { 0 } + \sum \beta _ { k } x _ { k } + \sum \beta _ { j } x _ { j } + \sum \beta _ { k q } x _ { k } . } \end{array}$ $x _ { q } + \sum \beta _ { m q } x _ { m } \cdot x _ { q } ]$ . For the reposted depth, we used the reposted depth itself as the dependent variable ( R???????????????? ?????? $\begin{array} { r } { \mathbf { \dot { \mu } } _ { h } = \mathbf { \mu } _ { \beta _ { 0 } } + \sum \beta _ { k } x _ { k } + \sum \beta _ { j } x _ { j } + \sum \beta _ { k q } x _ { k } \cdot x _ { q } + \sum \beta _ { m q } x _ { m } \cdot x _ { q } \mathbf { \mu } ) } \end{array}$ . Table 6 presents the multiple linear regression results for all the dependent variables. For the results with control variables, it shows similar results and robust standard error with the results in Table 6, please refer to Appendix (Table 12) for details.

Additionally, to test the effect of situational posts, we used similar regression models defined above by naming the not-situational posts as “Type 0” and the situational posts as “Type 1” (see Table 8). Similarly, to test the effect of social support-related information, we named the not social support information types as “Type 0” and named the social support information types as “Type 1” then carried out the regression analysis (see Table 9).

<table><tr><td rowspan="3"></td><td colspan="8">Dependent Variable: Virality of Posts</td></tr><tr><td colspan="2">Reposted Amount</td><td colspan="2">Reposted Depth</td><td colspan="2">Reposted Speed</td><td colspan="2">Duration</td></tr><tr><td>B</td><td>SE</td><td>B</td><td>SE</td><td>B</td><td>SE</td><td>B</td><td>SE</td></tr><tr><td>T 2—Casualties and Y damages</td><td>0.017</td><td>0.04</td><td>0.18</td><td>0.10</td><td>0.04</td><td>0.05</td><td>-0.02</td><td>0.07</td></tr><tr><td>P 3—Doubt casting</td><td>0.12*</td><td>0.05</td><td>0.27*</td><td>0.12</td><td>0.06</td><td>0.06</td><td>0.10</td><td>0.09</td></tr><tr><td>E 4—Caution and advice</td><td>0.21*</td><td>0.09</td><td>0.53**</td><td>0.20</td><td>0.24*</td><td>0.10</td><td>0.46**</td><td>0.15</td></tr><tr><td>5—Donation-related</td><td>0.16***</td><td>0.05</td><td>0.38***</td><td>0.10</td><td>0.10*</td><td>0.05</td><td>0.24***</td><td>0.07</td></tr><tr><td>6—Help-seeking</td><td>0.39***</td><td>0.06</td><td>1.03***</td><td>0.14</td><td>0.26***</td><td>0.07</td><td>0.53***</td><td>0.10</td></tr><tr><td>Anxious</td><td>0.01</td><td>9.2e-3</td><td>4.6e-3</td><td>0.02</td><td>-9.5e-3</td><td>9.8 e-3</td><td>5.0e-3</td><td>0.01</td></tr><tr><td>Sad</td><td>0.02*</td><td>7.3e-3</td><td>0.03</td><td>0.02</td><td>0.01</td><td>7.7e-3</td><td>0.01</td><td>0.01</td></tr><tr><td>Anger</td><td>-0.02**</td><td>6.1e-3</td><td>-0.05***</td><td>0.01</td><td>-0.02***</td><td>6.4e-3</td><td>-0.03**</td><td>9.7e-3</td></tr><tr><td>Neighbor</td><td>0.18***</td><td>0.03</td><td>0.49***</td><td>0.07</td><td>0.26***</td><td>0.03</td><td>0.26***</td><td>0.05</td></tr><tr><td>Urban</td><td>0.07**</td><td>0.03</td><td>0.17**</td><td>0.06</td><td>0.05</td><td>0.03</td><td>0.11**</td><td>0.04</td></tr><tr><td>Log(Followers)</td><td>0.24***</td><td>0.02</td><td>0.27***</td><td>0.04</td><td>0.28***</td><td>0.02</td><td>0.21***</td><td>0.03</td></tr><tr><td>Log(Followees)</td><td>-0.17***</td><td>0.04</td><td>-0.17*</td><td>0.08</td><td>-0.17***</td><td>0.04</td><td>-0.25***</td><td>0.06</td></tr><tr><td>Type2* Log(Followers)</td><td>0.02</td><td>0.02</td><td>0.09.</td><td>0.04</td><td>-0.007</td><td>0.02</td><td>0.06</td><td>0.03</td></tr><tr><td>Type3* Log(Followers)</td><td>0.02</td><td>0.03</td><td>0.08</td><td>0.06</td><td>-0.02</td><td>0.03</td><td>0.04</td><td>0.04</td></tr><tr><td>Type4* Log(Followers)</td><td>0.02</td><td>0.04</td><td>0.20*</td><td>0.09</td><td>0.05</td><td>0.04</td><td>0.14*</td><td>0.07</td></tr><tr><td>Type5* Log(Followers)</td><td>0.02</td><td>0.02</td><td>0.08.</td><td>0.05</td><td>-0.03</td><td>0.02</td><td>0.07*</td><td>0.03</td></tr><tr><td>Type6* Log(Followers)</td><td>0.22***</td><td>0.03</td><td>0.39***</td><td>0.06</td><td>0.09**</td><td>0.03</td><td>0.23***</td><td>0.04</td></tr><tr><td>Type2* Log(Followees)</td><td>0.02</td><td>0.04</td><td>-0.02</td><td>0.08</td><td>0.03</td><td>0.04</td><td>0.05</td><td>0.06</td></tr><tr><td>Type3* Log(Followees)</td><td>0.05</td><td>0.05</td><td>0.06</td><td>0.10</td><td>0.09</td><td>0.05</td><td>0.09</td><td>0.07</td></tr><tr><td>Type4* Log(Followees)</td><td>-0.003</td><td>0.08</td><td>-0.02</td><td>0.17</td><td>0.09</td><td>0.08</td><td>-0.04</td><td>0.12</td></tr><tr><td>Type5* Log(Followees)</td><td>-0.03</td><td>0.04</td><td>-0.05</td><td>0.09</td><td>0.05</td><td>0.04</td><td>-0.003</td><td>0.06</td></tr><tr><td>Type6* Log(Followees)</td><td>-0.14**</td><td>0.05</td><td>-0.02</td><td>0.12</td><td>-0.02</td><td>0.06</td><td>0.02</td><td>0.08</td></tr><tr><td>Anxious* Log(Followers)</td><td>0.006</td><td>3.6e-3</td><td>-9.0e-3</td><td>7.9e-3</td><td>-9.4e-3*</td><td>3.8e-3</td><td>2.0e-3</td><td>5.7e-3</td></tr><tr><td>Anxious* Log(Followees)</td><td>0.02**</td><td>7.2e-3</td><td>0.03</td><td>0.02</td><td>0.02*</td><td>7.7e-3</td><td>0.02</td><td>0.01</td></tr><tr><td>Sad* Log(Followers)</td><td>3.6e-3</td><td>3.0e-3</td><td>0.02**</td><td>6.7e-3</td><td>6.4e-3*</td><td>3.2e-3</td><td>5.8e-3</td><td>4.7e-3</td></tr><tr><td>Sad* Log(Followees)</td><td>-0.01*</td><td>5.4e-3</td><td>-0.03*</td><td>0.01</td><td>-0.02**</td><td>5.8e-3</td><td>-0.01</td><td>8.5e-3</td></tr><tr><td>Anger* Log(Followers)</td><td>-5.7e-3*</td><td>2.4e-3</td><td>-0.02**</td><td>5.3e-3</td><td>-0.01***</td><td>2.5e-3</td><td>-0.02***</td><td>3.7e-3</td></tr><tr><td>Anger* Log(Followees)</td><td>4.7e-3</td><td>4.2e-3</td><td>0.01</td><td>9.4e-3</td><td>0.01**</td><td>4.5e-3</td><td>0.02*</td><td>6.6e-3</td></tr><tr><td>Neighbor* Log(Followers)</td><td>-0.07***</td><td>0.01</td><td>-0.06*</td><td>0.03</td><td>-0.05***</td><td>0.01</td><td>-0.09***</td><td>0.02</td></tr><tr><td>Neighbor * Log(Followees)</td><td>0.20***</td><td>0.02</td><td>0.34***</td><td>0.05</td><td>0.22***</td><td>0.02</td><td>0.20***</td><td>0.04</td></tr><tr><td>Urban* Log(Followers)</td><td>0.12***</td><td>0.01</td><td>0.21***</td><td>0.02</td><td>0.07***</td><td>0.01</td><td>0.14***</td><td>0.02</td></tr><tr><td>Urban* Log(Followees)</td><td>-0.03</td><td>0.02</td><td>-0.09.</td><td>0.05</td><td>0.04</td><td>0.02</td><td>-0.04</td><td>0.03</td></tr><tr><td>Intercept</td><td>0.49***</td><td>0.04</td><td>0.66</td><td>0.09</td><td>0.55***</td><td>0.04</td><td>0.68***</td><td>0.07</td></tr><tr><td>Adjusted R2</td><td>0.385</td><td></td><td>0.234</td><td></td><td>0.352</td><td></td><td>0.221</td><td></td></tr></table>

Sig. level ꞏSignificant at 0.1 level; \*Significant at 0.05 level; \*\* Significant at 0.01 level; \*\*\*Significant at 0.001 level.

Table 7. Results of multiple linear regression for all dependent variables.  
Table 8. Effect of situational awareness on the virality of disaster-related information.

<table><tr><td>Coefficients (SE)</td><td>Reposted amount</td><td>Reposted depth</td><td>Reposted speed</td><td>Duration</td></tr><tr><td>Situational information or not (1/0)</td><td>0.15**(0.05)</td><td>0.35**(0.11)</td><td>0.12*(0.05)</td><td>0.16*(0.08)</td></tr><tr><td>Intercept</td><td>0.52***(0.05)</td><td>0.79***(0.10)</td><td>0.58***(0.05)</td><td>0.76***(0.07)</td></tr><tr><td>Residual standard error</td><td>1.307</td><td>2.591</td><td>1.351</td><td>1.830</td></tr><tr><td colspan="5">Sig. level: ·Significant at 0.1 level; *Significant at 0.05 level; ** Significant at 0.01 level; ***Significant at 0.001 level.</td></tr></table>

Table 9. Effect of social support on the virality of disaster-related information.

<table><tr><td>Coefficients (SE)</td><td>Reposted amount</td><td>Reposted depth</td><td>Reposted speed</td><td>Duration</td></tr><tr><td>Social support-related or not (1/0)</td><td>0.07**(0.03)</td><td>0.18**(0.05)</td><td>-0.009(0.03)</td><td>0.20***(0.04)</td></tr><tr><td>Intercept</td><td>0.63***(0.02)</td><td>1.04***(0.03)</td><td>0.70***(0.05)</td><td>0.83***(0.02)</td></tr><tr><td>Residual standard error</td><td>1.307</td><td>2.591</td><td>1.351</td><td>1.828</td></tr><tr><td colspan="5">Sig. level · Significant at 0.1 level; *Significant at 0.05 level; ** Significant at 0.01 level; ***Significant at 0.001 level.</td></tr></table>

## 4.2.1 Effect of content type

Table 8 presents that the virality of situational information (containing the reposted amount, depth, speed, and duration) is significantly larger than the non-situational information after the Yiliang earthquake. Thus, results fully support H1a. Table 9 presents that reposted amount, depth, and duration of the social support-related information are significantly larger than the information that is non-social-support-related. However, the reposted speed of the social support information is smaller (not significant) than the non-social-support information. Thus, results partially support H1b.

To determine the specific effect of content types on the virality of disaster-related information, Tables 7 presents the specific effect of each type of disaster-related information on the reposted amount, reposted depth, reposted speed, and duration of the post. Table 7 shows that the reposted amount of Type 3 (doubt-casting), Type 4 (caution and advice), Type 5 (donation of goods, money, and services), and Type 6 information (help-seeking) increase by 12.7%, 23.4%, 17.4%, and 47.7%, respectively, compared with Type 1 (non-situational information, which we defined as personal-related and others) information. The reposted depth of Type 3 (doubt-casting), Type 4 (caution and advice), Type 5 (donation of goods, money, and services), and Type 6 (help-seeking) information will increase 0.27, 0.53, 0.38, and 1.03 compare with Type 1 (Personal-related and others) information, respectively. The reposted speed of Type 4, Type 5, and Type 6 information increases by 27.1%, 10.9%, and 29.7% than the reposted speed of Type 1 information. The increase in duration of all the three types of situational awareness and social support-related information (Type 4, caution and advice; Type 5, donation of money, goods, or services; Type 6, help-seeking) by 58.4%, 27.1%, and 69.9%, respectively, compared with Type 1 information.

## 4.2.2 Effect of negative emotions contained in the content

The effect of words regarding sadness positively related to its reposted amount. For each post, one unit increase of the variable sadness represents 1% increase of the ratio between the number of sadness-related words in the post and the total number of sadness-related words in the LIWC corpus. The results indicate that, the increase of sadness-related words is associated with the elevated reposted amount. However, the effect of anxiety is not significant on the virality of the posts. This may occur for the positive correlations (0.29, significant at 0.01 level) between sadness and anxiety, which exhibit greater effect on the virality of the disaster-related information than other variables. The effect of words of anger that are contained in the original posts is significantly negative on the reposted amount, depth, speed, and duration. In particular, a 1% increase in the anger words of the original post, the reposted amount decreases by 2%, reposted amount decreases by 5%, reposted speed decreases by 3%, and the duration decreases by 3%. Thus, our datasets partially support H2.

## 4.2.3 Effect of users’ location

The spatial location of social media users exhibits a significant positive effect on reposted amount, reposted depth, speed, and duration. Posts published by people near an event indicate an additional 19.7%, 29.7%, and 29.7 % effect on reposted amount, reposted speed, and duration, respectively, compared with posts published by people far from the same event. Moreover, the reposted depth of posts published by people located near an event is 63.2% deeper than the posts from those located far from the event. Therefore, our datasets partially support H3a.

Social media users who are situated in urban areas increase the viral degree of a post in all perspectives. In particular, posts published by people who are located in urban areas exhibit an additional 7.3%, 5.1% (insignificant), and 11.6% reposted amount, reposted speed, and duration, respectively, compared with the posts from rural users. Furthermore, the reposted depth of the posts of urban users is 18.5% deeper than the posts of rural users. Thus, our datasets partially support H3b.

4.2.4 Effect of users’ social capital

Each social capital factor indicates a similar effect on the number of reposts, reposted depth, and reposted speed. (a) The number of followers exhibits a significant positive effect on reposted amount, reposted depth, reposted speed, and the duration of the post. When the number of users’ followers increases by 1%, the number of reposts increases by 0.24%, repost speed increases by 0.28%, and the duration of the original posts increases by 0.21%. When the number of users’ followers increase 1%, the reposted depth increases 0.27. (b) The number of followees indicates a significant negative effect on reposted amount, reposted depth, reposted speed, and post duration. When the number of users’ followees increases by 1%, the number of reposts falls by 0.17%, repost speed declines by 0.17%, and the duration of the original posts falls by 0.25%. When the number of users’ followers increases by 1%, the reposted depth decreases 0.17. Therefore, our findings partially support H4a.

## JournalPre-proof

Table 6 reveals that the number of followers moderates the influence of information type on the viral degree of a post. First, the main effects of users’ number of followers and followees on the virality of information are as follows: (a) When the number of user’s followers increase by 1% and he/she publishes Type 6 (Help-seeking) information, more reposted amount, quicker reposted speed, and longer duration are generated than Type 1 information by 0.22%, 0.09%, and 0.23%, respectively. When the number of users’ followers increases 1%, the reposted depth of Type 6 information increases 47.7% compare with the reposted depth of Type 1 information. Furthermore, when the number of services), Type 4 (Caution and advice) information, the duration increases by 0.07% and 0.14%, and their number of followees increase by 1%, the post obtains a lower reposted amount than Type 1 information by 0.14%. Therefore, H4b is partially supported.

Second, the moderate effect of the number of followers and followees on the effect of negative and express sadness increased reposted depth and speed by 2% and 0.64% of the standard deviation, respectively. If users’ number of followers increased by 1%, then the 1% increases of the anxiety words in the posts could be slowly reposted at around 0.94% of its standard deviation. If users’ number of followees increased by 1%, then the reposted amount, speed, and duration of posts with increased anger emotion could be smaller reposted (0.57% of its standard deviation), slowly reposted (0.74% of its standard deviation), and shorter duration (2% of its standard deviation). (b) With the 1% increase of users’ number of followees, if the posts contain anxious feeling, then the reposted amount and reposted speed could increase by 2% of the standard deviation. Posts with sadness from users with a large number of followees could be reposted 1% (of the standard deviation) less deep and 2% (of the standard deviation) slower. Posts depicting anger from users with a high number of followees (1% increase) increased reposted speed by 1% and increased duration by 2% of its standard deviation. Thus, H4c was partially supported.

Third, the moderating effects of the numbers of followers and followees on the effect of users physical location are significant. (a) When users located near the event and their number of followers increase by 1%, their posts will obtain a lower reposted amount than by 0.07%, the reposted speed will number of users’ followers increases 1%, the reposted depth of the posts from those near the event decreases by 6% than the users’ number of followees, when the number of followees of users near the event increase by 1%, their posts will attract more reposted amount than the posts from users located far from the event by 0.20%, accelerate reposted speed by 0.22%, and increase the duration by 0.20%. When the number of users’ followees increases by 1%, the reposted depth of the posts from those near the event increases by 34% of the reposted depth of the posts from users located far from the event. Therefore, H4d was partially supported. (b) When users in the urban area whose number of followers increase by 1%, their posts will garner a higher repost number than posts from rural users by 0.12%, speed up the reposted speed by 0.07%, and enlarge the duration by 0.14%. When the number of users’ followers increases by 1%, the reposted depth of the post in the urban area increases by 21% than the reposted depth of posts from rural users. By contrast, the moderating effect of users’ number of followees on the physical location (urban or rural) is not significant. Therefore, H4d was partially supported.

In summary, our dataset fully supported H1a and H2a, and partially supported the left hypotheses.

Table 10 presents all the supportiveness of the proposed hypotheses for each measure of the virality.

Table 10. Summary of the hypothesis testing results.

<table><tr><td>Hypothesis</td><td>Amount</td><td>Depth</td><td>Speed</td><td>Duration</td><td>Virality</td></tr><tr><td>H1a</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>H1b</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>P</td></tr><tr><td>H2a</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>H2b</td><td>Y</td><td>Y</td><td>P</td><td>Y</td><td>P</td></tr><tr><td>H3</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td></tr><tr><td>H4a</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td></tr><tr><td>H4b</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td></tr><tr><td>H4c</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td></tr><tr><td>H4d</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td></tr><tr><td>H4e</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td></tr><tr><td colspan="6">Notes: Y (yes; the hypothesis was fully supported), N (no; the hypothesis was rejected), P (partially; the hypothesis was partially supported)</td></tr></table>

## 4.3 Robustness Check

To check the robustness of the proposed factors, we conducted negative binomial regression and Poisson regression for all the virility measures. Tables 11 and 12 summarize the detailed regression results. Note that Poisson regression is not well positioned to model our data because over-dispersion problem with a very bad goodness-of-fit (except when the dependent variable is reposted depth). Thus, we mainly compare the results of the main model and the negative binomial model. The results are largely consistent with the multiple linear regression results, indicating that our findings are meaningfully unchanged in terms of magnitude and significance. One exception is that the moderating effect of social capital on the types of information is inconsistent with the negative binomial regression. However, the goodness-of-fit of the negative binomial model is less than that of the multiple linear regression. In addition, negative binomial model usually requires more data samples to obtain significance. In fact, the moderating effect of social capital on the duration of Type

6 (help-seeking) information is insignificant at p-value<0.01 level, but significant at p-value<0.05 level, which indicates a reasonable significance given that there are only 461 data samples. H4b is then partially supported.

Table 11. Results of Negative Binomial regression for all dependent variables Dependent Variable: Virality of the posts

<table><tr><td rowspan="3" colspan="2"></td><td colspan="8">Dependent Variable: Virality of the posts</td></tr><tr><td colspan="2">Reposted amount</td><td colspan="2">Reposted depth</td><td colspan="2">Reposted speed</td><td colspan="2">Duration</td></tr><tr><td>b</td><td>SE</td><td>B</td><td>SE</td><td>B</td><td>SE</td><td>b</td><td>SE</td></tr><tr><td>T</td><td rowspan="2">2-Casualties &amp; damages</td><td rowspan="2">-0.04</td><td rowspan="2">0.08</td><td rowspan="2">0.16</td><td rowspan="2">0.14</td><td rowspan="2">0.09</td><td rowspan="2">0.11</td><td rowspan="2">-0.14</td><td rowspan="2">0.11</td></tr><tr><td>Y</td></tr><tr><td>P</td><td>3-Doubt casting</td><td>0.13</td><td>0.12</td><td>0.19</td><td>0.17</td><td>-0.08</td><td>0.14</td><td>0.08</td><td>0.13</td></tr><tr><td>E</td><td>4-Caution &amp; advice</td><td>0.45**</td><td>0.18</td><td>0.43</td><td>0.27</td><td>0.24</td><td>0.23</td><td>0.48***</td><td>0.20</td></tr><tr><td></td><td>5-Donation-related</td><td>0.29**</td><td>0.10</td><td>0.41**</td><td>0.14</td><td>0.27*</td><td>0.11</td><td>0.24***</td><td>0.11</td></tr><tr><td></td><td>6-Help-seeking</td><td>0.46***</td><td>0.13</td><td>0.74***</td><td>0.19</td><td>0.40*</td><td>0.15</td><td>0.40***</td><td>0.15</td></tr><tr><td colspan="2">Anxious</td><td>6.7e-3</td><td>0.02</td><td>0.02</td><td>0.03</td><td>0.01</td><td>0.02</td><td>4.4e-3</td><td>0.02</td></tr><tr><td colspan="2">Sad</td><td>-0.02</td><td>0.02</td><td>-0.05*</td><td>0.02</td><td>-0.09***</td><td>0.02</td><td>4.2e-3</td><td>0.02</td></tr><tr><td colspan="2">Anger</td><td>-0.05**</td><td>0.02</td><td>-0.09***</td><td>0.02</td><td>-0.05*</td><td>0.02</td><td>-0.03*</td><td>0.03</td></tr><tr><td colspan="2">Neighbor</td><td>0.61***</td><td>0.06</td><td>0.66***</td><td>0.08</td><td>0.69***</td><td>0.07</td><td>0.51***</td><td>0.07</td></tr><tr><td colspan="2">Urban</td><td>0.20***</td><td>0.06</td><td>0.21*</td><td>0.08</td><td>0.26***</td><td>0.08</td><td>0.14*</td><td>0.07</td></tr><tr><td colspan="2">Log(Followers)</td><td>0.37***</td><td>0.02</td><td>0.36***</td><td>0.02</td><td>0.43***</td><td>0.04</td><td>0.27***</td><td>0.02</td></tr><tr><td colspan="2">Log(Followees)</td><td>-0.19**</td><td>0.07</td><td>-0.09</td><td>0.10</td><td>0.02</td><td>0.09</td><td>-0.34***</td><td>0.08</td></tr><tr><td colspan="2">Type2* Log(Followers)</td><td>0.01</td><td>0.03</td><td>-0.03</td><td>0.05</td><td>-0.04</td><td>0.04</td><td>0.03</td><td>0.04</td></tr><tr><td colspan="2">Type3* Log(Followers)</td><td>0.04</td><td>0.04</td><td>0.01</td><td>0.07</td><td>7.5e-3</td><td>0.05</td><td>0.02</td><td>0.06</td></tr><tr><td colspan="2">Type4* Log(Followers)</td><td>-0.05</td><td>0.06</td><td>-2.9e-3</td><td>0.10</td><td>-2.8e-3</td><td>0.08</td><td>-0.03</td><td>0.08</td></tr><tr><td colspan="2">Type5* Log(Followers)</td><td>-0.01</td><td>0.03</td><td>-0.02</td><td>0.05</td><td>-0.04</td><td>0.04</td><td>4.2e-3</td><td>0.04</td></tr><tr><td colspan="2">Type6* Log(Followers)</td><td>0.02</td><td>0.04</td><td>-0.02</td><td>0.06</td><td>-0.03</td><td>0.05</td><td>0.01</td><td>0.05</td></tr><tr><td colspan="2">Type2* Log(Followees)</td><td>0.07</td><td>0.07</td><td>0.05</td><td>0.01</td><td>-0.02</td><td>0.09</td><td>0.14.</td><td>0.08</td></tr><tr><td colspan="2">Type3* Log(Followees)</td><td>0.13</td><td>0.09</td><td>0.15</td><td>0.14</td><td>0.22</td><td>0.12</td><td>0.15</td><td>0.10</td></tr><tr><td colspan="2">Type4* Log(Followees)</td><td>0.09</td><td>0.13</td><td>0.12</td><td>0.20</td><td>0.21</td><td>0.16</td><td>0.18</td><td>0.15</td></tr><tr><td colspan="2">Type5* Log(Followees)</td><td>-0.01</td><td>0.07</td><td>0.004</td><td>0.11</td><td>0.01</td><td>0.09</td><td>0.08</td><td>0.08</td></tr><tr><td colspan="2">Type6* Log(Followees)</td><td>0.06</td><td>0.10</td><td>0.13</td><td>0.15</td><td>-0.04</td><td>0.12</td><td>0.26*</td><td>0.12</td></tr><tr><td colspan="2">Anxious* Log(Followers)</td><td>-0.01</td><td>0.006</td><td>-0.02.</td><td>0.01</td><td>-0.02**</td><td>7.0e-3</td><td>1.7e-3</td><td>7.5e-3</td></tr><tr><td colspan="2">Anxious* Log(Followees)</td><td>0.05**</td><td>0.02</td><td>0.04.</td><td>0.02</td><td>0.04*</td><td>0.02</td><td>0.02</td><td>0.02</td></tr><tr><td colspan="2">Sad* Log(Followers)</td><td>0.02**</td><td>0.005</td><td>0.03***</td><td>0.01</td><td>0.04***</td><td>6.6e-3</td><td>3.5e-3</td><td>6.4e-3</td></tr><tr><td colspan="2">Sad* Log(Followees)</td><td>-0.04***</td><td>0.01</td><td>-0.03</td><td>0.02</td><td>-0.03.</td><td>0.01</td><td>-0.03*</td><td>0.01</td></tr><tr><td colspan="2">Anger* Log(Followers)</td><td>2.0e-3</td><td>4.6e-3</td><td>8.6e-3</td><td>7.2e-3</td><td>1.6e-3</td><td>5.2e-3</td><td>-6.0e-3</td><td>5.5e-3</td></tr><tr><td colspan="2">Anger* Log(Followees)</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.01</td><td>0.01</td><td>0.01</td></tr><tr><td colspan="2">Neighbor* Log(Followers)</td><td>-0.15***</td><td>0.01</td><td>-0.13***</td><td>0.03</td><td>-0.15***</td><td>0.02</td><td>-0.12***</td><td>0.03</td></tr><tr><td colspan="2">Neighbor * Log(Followees)</td><td>0.19***</td><td>0.04</td><td>0.17**</td><td>0.06</td><td>0.15**</td><td>0.05</td><td>0.18***</td><td>0.05</td></tr><tr><td colspan="2">Urban* Log(Followers)</td><td>-0.04*</td><td>0.02</td><td>-0.03</td><td>0.02</td><td>-0.08***</td><td>0.02</td><td>-0.01</td><td>0.02</td></tr><tr><td colspan="2">Urban* Log(Followees)</td><td>0.07.</td><td>0.03</td><td>0.02</td><td>0.06</td><td>0.02</td><td>0.05</td><td>0.09.</td><td>0.05</td></tr><tr><td colspan="2">Intercept</td><td>-1.22***</td><td>0.09</td><td>-0.81***</td><td>0.13</td><td>-1.28</td><td>0.11</td><td>-0.59***</td><td>0.10</td></tr><tr><td colspan="2">Pseudo R2</td><td>0.18</td><td></td><td>0.17</td><td></td><td>0.20</td><td></td><td>0.11</td><td></td></tr></table>

Table 12. Results of Poisson regression for all dependent variables.

<table><tr><td rowspan="3" colspan="2"></td><td colspan="8">Dependent Variable: Virality of the posts</td></tr><tr><td colspan="2">Reposted amount</td><td colspan="2">Reposted depth</td><td colspan="2">Reposted speed</td><td colspan="2">Duration</td></tr><tr><td>b</td><td>SE</td><td>b</td><td>SE</td><td>b</td><td>SE</td><td>b</td><td>SE</td></tr><tr><td>T Y</td><td>2—Casualties &amp; damages</td><td>-0.03</td><td>0.08</td><td>0.17**</td><td>0.06</td><td>0.10</td><td>0.07</td><td>-0.15**</td><td>0.05</td></tr><tr><td rowspan="4">P E</td><td>3—Doubt casting</td><td>0.13</td><td>0.09</td><td>0.18*</td><td>0.07</td><td>-0.07</td><td>0.09</td><td>0.05</td><td>0.07</td></tr><tr><td>4—Caution &amp; advice</td><td>0.44**</td><td>0.14</td><td>0.43***</td><td>0.11</td><td>0.22</td><td>0.16</td><td>0.44***</td><td>0.10</td></tr><tr><td>5—Donation-related</td><td>0.31***</td><td>0.08</td><td>0.45***</td><td>0.06</td><td>0.26***</td><td>0.08</td><td>0.23***</td><td>0.05</td></tr><tr><td>6—Help-seeking</td><td>0.52**</td><td>0.10</td><td>0.83***</td><td>0.07</td><td>0.48***</td><td>0.10</td><td>0.42***</td><td>0.07</td></tr><tr><td colspan="2">Anxious</td><td>3.4e-3</td><td>0.02</td><td>0.02*</td><td>0.01</td><td>2.2e-3</td><td>0.02</td><td>2.2e-3</td><td>0.01</td></tr><tr><td colspan="2">Sad</td><td>-0.02</td><td>0.01</td><td>-0.06***</td><td>0.01</td><td>-0.09***</td><td>0.01</td><td>5.9e-3</td><td>0.008</td></tr><tr><td colspan="2">Anger</td><td>-0.05***</td><td>0.01</td><td>-0.09***</td><td>0.01</td><td>-0.04***</td><td>0.01</td><td>-0.04***</td><td>0.01</td></tr><tr><td colspan="2">Neighbor</td><td>0.60***</td><td>0.04</td><td>0.65***</td><td>0.03</td><td>0.67***</td><td>0.04</td><td>0.49***</td><td>0.03</td></tr><tr><td colspan="2">Urban</td><td>0.22***</td><td>0.04</td><td>0.25***</td><td>0.03</td><td>0.28***</td><td>0.05</td><td>0.14***</td><td>0.03</td></tr><tr><td colspan="2">Log(Followers)</td><td>0.37***</td><td>0.02</td><td>0.33***</td><td>0.02</td><td>0.39***</td><td>0.02</td><td>0.25***</td><td>0.02</td></tr><tr><td colspan="2">Log(Followees)</td><td>-0.12**</td><td>0.05</td><td>-0.003</td><td>0.04</td><td>0.03</td><td>0.05</td><td>-0.24***</td><td>0.03</td></tr><tr><td colspan="2">Type2* Log(Followers)</td><td>0.005</td><td>0.02</td><td>-0.002</td><td>0.02</td><td>-0.03</td><td>0.02</td><td>0.05**</td><td>0.02</td></tr><tr><td colspan="2">Type3* Log(Followers)</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.01</td><td>0.02</td><td>0.04*</td><td>0.02</td></tr><tr><td colspan="2">Type4* Log(Followers)</td><td>-0.04</td><td>0.04</td><td>0.02</td><td>0.03</td><td>4.9e-3</td><td>0.04</td><td>0.009</td><td>0.03</td></tr><tr><td colspan="2">Type5* Log(Followers)</td><td>-0.02</td><td>0.02</td><td>-0.03.</td><td>0.02</td><td>-0.05**</td><td>0.02</td><td>0.009</td><td>0.02</td></tr><tr><td colspan="2">Type6* Log(Followers)</td><td>-0.01</td><td>0.02</td><td>-0.03.</td><td>0.07</td><td>-0.06**</td><td>0.02</td><td>0.01</td><td>0.02</td></tr><tr><td colspan="2">Type2* Log(Followees)</td><td>0.05</td><td>0.05</td><td>0.01</td><td>0.04</td><td>0.01</td><td>0.05</td><td>0.09</td><td>0.03</td></tr><tr><td colspan="2">Type3* Log(Followees)</td><td>0.13*</td><td>0.06</td><td>0.14</td><td>0.05</td><td>0.24***</td><td>0.07</td><td>0.10*</td><td>0.05</td></tr><tr><td colspan="2">Type4* Log(Followees)</td><td>0.07</td><td>0.09</td><td>0.11</td><td>0.07</td><td>0.23</td><td>0.09</td><td>0.10</td><td>0.06</td></tr><tr><td colspan="2">Type5* Log(Followees)</td><td>-0.02</td><td>0.04</td><td>-0.03</td><td>0.04</td><td>0.04</td><td>0.05</td><td>0.05</td><td>0.04</td></tr><tr><td colspan="2">Type6* Log(Followees)</td><td>0.04</td><td>0.06</td><td>0.07</td><td>0.05</td><td>-2.8e-4</td><td>0.06</td><td>0.19***</td><td>0.05</td></tr><tr><td colspan="2">Anxious* Log(Followers)</td><td>-4.3e-3</td><td>3.3e-3</td><td>-0.01***</td><td>2.6e-3</td><td>-0.01***</td><td>3.6e-3</td><td>-2.3e-3</td><td>2.9e-3</td></tr><tr><td colspan="2">Anxious* Log(Followees)</td><td>0.05***</td><td>0.01</td><td>0.03**</td><td>7.9e-3</td><td>0.03*</td><td>0.01</td><td>0.03***</td><td>0.008</td></tr><tr><td colspan="2">Sad* Log(Followers)</td><td>0.01***</td><td>0.003</td><td>0.03***</td><td>2.4e-3</td><td>0.03***</td><td>3.2e-3</td><td>5.5e-3*</td><td>2.5e-3</td></tr><tr><td colspan="2">Sad* Log(Followees)</td><td>-0.03***</td><td>0.008</td><td>-0.02*</td><td>7.5e-2</td><td>-0.01</td><td>0.01</td><td>-0.03***</td><td>0.006</td></tr><tr><td colspan="2">Anger* Log(Followers)</td><td>3.8e-3</td><td>2.7e-3</td><td>6.9e-3**</td><td>2.2e-3</td><td>-2.4e-5</td><td>2.6e-3</td><td>-3.3e-3</td><td>2.3e-3</td></tr><tr><td colspan="2">Anger* Log(Followees)</td><td>0.01*</td><td>0.01</td><td>0.02**</td><td>6.2e-3</td><td>0.02**</td><td>0.007</td><td>0.02***</td><td>0.006</td></tr><tr><td colspan="2">Neighbor* Log(Followers)</td><td>-0.14***</td><td>0.01</td><td>-0.12***</td><td>0.01</td><td>-0.13***</td><td>0.01</td><td>-0.12***</td><td>0.01</td></tr><tr><td colspan="2">Neighbor * Log(Followees)</td><td>0.16***</td><td>0.03</td><td>0.15***</td><td>0.06</td><td>0.11***</td><td>0.03</td><td>0.16***</td><td>0.02</td></tr><tr><td colspan="2">Urban* Log(Followers)</td><td>-0.04***</td><td>0.008</td><td>-0.02***</td><td>0.007</td><td>-0.06***</td><td>0.01</td><td>-0.01</td><td>0.008</td></tr><tr><td colspan="2">Urban* Log(Followees)</td><td>0.04</td><td>0.03</td><td>-0.04.</td><td>0.02</td><td>8.0e-3</td><td>0.03</td><td>0.07***</td><td>0.02</td></tr><tr><td colspan="2">Intercept</td><td>-1.23***</td><td>0.07</td><td>-0.84***</td><td>0.06</td><td>-1.26***</td><td>0.07</td><td>-0.58***</td><td>0.05</td></tr><tr><td colspan="2">Pseudo R2</td><td colspan="2">/</td><td colspan="2">0.27</td><td colspan="2">/</td><td colspan="2">/</td></tr></table>

Furthermore, we performed another robust check by defining reposted speed as the time difference between the first repost and the original post (time lags). Under such definition, we performed Heckman’s two-step model to avoid sample selection bias [122]. The first step is to use the Probit model to model the probability of users to repost the original posts and to obtain the inverse Mill’s ratio (IMR). The second step is to apply the OLS model to obtain the time lags (reposted speed) of the original posts. Table 13 presents the effect of 0/1 variables situational information or not and social support-related information or not on the time lags of the posts. Table 14 presents the results of the selection model when all the defined variables and IMR are considered.

Table 13. Effect of situational awareness and social support on the time lags of disaster-related information

<table><tr><td rowspan="2">Coefficients (SE)</td><td colspan="2">Situational information or not</td><td colspan="2">Social support-related or not</td></tr><tr><td>Step 1</td><td>Step 2</td><td>Step 1</td><td>Step 2</td></tr><tr><td>(1/0)</td><td>-0.08(0.04)</td><td>-49.8*(23.1)</td><td>0.07* (0.03)</td><td>-0.25 (14.1)</td></tr><tr><td>Intercept</td><td>-0.39***(0.04)</td><td>105.5***(21.9)</td><td>-0.49***(0.02)</td><td>60.8***(9.0)</td></tr><tr><td>Residual standard error</td><td>/</td><td>0.001</td><td>/</td><td>-0.0003</td></tr><tr><td colspan="5">Sig. level · Significant at 0.1 level; *Significant at 0.05 level; ** Significant at 0.01 level; ***Significant at 0.001 level.</td></tr></table>

The results in Tables 13 and 14 show that most of the coefficients of the time lags are opposite to the coefficients in Tables 7, 8, and 9. For example, in Table 8, the coefficient of situational information or not (1/0) is 0.12 (significant at 0.05); in Table 13, the coefficient of the Probit model (step 1) and the coefficient of the OLS model (step 2) are −0.08 and −49.8, respectively. The coefficient of social support-related information or not (1/0) is −0.009 (insignificant). In Table 13, the coefficient of the Probit model (step 1) and the coefficient of the OLS model (step 2) are −0.07 (significant at 0.05) and −0.25 (insignificant), respectively. This result is reasonable, because time lags are the inverse value of the previously defined reposted speed. This result also suggests the

robustness of the defined independent variables.

Table 14. Results of selection model for reposted speed (time lags)

<table><tr><td rowspan="3"></td><td colspan="4">Dependent Variable: Time lags of the posts</td></tr><tr><td colspan="2">Step 1: Selection model</td><td colspan="2">Step 2. Regression model</td></tr><tr><td>B</td><td>SE</td><td>B</td><td>SE</td></tr><tr><td colspan="5">Type</td></tr><tr><td>2—Casualties &amp; damages</td><td>-0.19***</td><td>0.05</td><td>-121.4***</td><td>28.9</td></tr><tr><td>3—Doubt casting</td><td>-0.09</td><td>0.07</td><td>-57.0</td><td>36.0</td></tr><tr><td>4—Caution &amp; advice</td><td>0.28*</td><td>0.12</td><td>8.4</td><td>56.2</td></tr><tr><td>5—Donation-related</td><td>0.02</td><td>0.06</td><td>-60.8*</td><td>26.9</td></tr><tr><td>6—Help-seeking</td><td>0.17</td><td>0.09</td><td>-82.4</td><td>43.3</td></tr><tr><td>Anxious</td><td>-0.01</td><td>0.01</td><td>-1.76</td><td>18.8</td></tr><tr><td>Sad</td><td>-0.03**</td><td>0.01</td><td>28.39***</td><td>19.1</td></tr><tr><td>Anger</td><td>0.40***</td><td>0.04</td><td>12.30*</td><td>7.7</td></tr><tr><td>Neighbor</td><td>0.09*</td><td>0.04</td><td>-1.37</td><td>15.4</td></tr><tr><td>Urban</td><td>0.29***</td><td>0.02</td><td>-41.47*</td><td>-45.2</td></tr><tr><td>Log(Followers)</td><td>-0.13**</td><td>0.04</td><td>23.35</td><td>47.7</td></tr><tr><td>Log(Followees)</td><td>-0.01</td><td>0.02</td><td>-36.84</td><td>-213.6</td></tr><tr><td>Type2* Log(Followers)</td><td>-0.01</td><td>0.02</td><td>-1.7</td><td>8.1</td></tr><tr><td>Type3* Log(Followers)</td><td>-0.03</td><td>0.04</td><td>-3.0</td><td>12.5</td></tr><tr><td>Type4* Log(Followers)</td><td>-0.03</td><td>0.06</td><td>-22.3</td><td>17.5</td></tr><tr><td>Type5* Log(Followers)</td><td>0.01</td><td>0.03</td><td>-5.3</td><td>8.4</td></tr><tr><td>Type6* Log(Followers)</td><td>0.12**</td><td>0.04</td><td>5.6</td><td>11.1</td></tr><tr><td>Type2* Log(Followees)</td><td>0.03</td><td>0.04</td><td>122.9***</td><td>18.4</td></tr><tr><td>Type3* Log(Followees)</td><td>0.14*</td><td>0.06</td><td>84.6**</td><td>28.9</td></tr><tr><td>Type4* Log(Followees)</td><td>0.11</td><td>0.10</td><td>134.1***</td><td>35.3</td></tr><tr><td>Type5* Log(Followees)</td><td>-0.01</td><td>0.05</td><td>99.8***</td><td>19.2</td></tr><tr><td>Type6* Log(Followees)</td><td>-0.01</td><td>0.08</td><td>153.3***</td><td>27.0</td></tr><tr><td>Anxious* Log(Followers)</td><td>-0.01*</td><td>0.01</td><td>-2.4</td><td>2.3</td></tr><tr><td>Anxious* Log(Followees)</td><td>0.02*</td><td>0.01</td><td>-8.4</td><td>5.7</td></tr><tr><td>Sad* Log(Followers)</td><td>0.01</td><td>0.01</td><td>-0.8</td><td>1.9</td></tr><tr><td>Sad* Log(Followees)</td><td>-0.02*</td><td>0.01</td><td>-34.0***</td><td>4.7</td></tr><tr><td>Anger* Log(Followers)</td><td>-0.004</td><td>0.004</td><td>-3.3*</td><td>1.5</td></tr><tr><td>Anger* Log(Followees)</td><td>0.01*</td><td>0.01</td><td>-4.9</td><td>3.9</td></tr><tr><td>Neighbor* Log(Followers)</td><td>-0.07***</td><td>0.02</td><td>-0.7</td><td>7.6</td></tr><tr><td>Neighbor * Log(Followees)</td><td>0.14***</td><td>0.03</td><td>86.6***</td><td>14.8</td></tr><tr><td>Urban* Log(Followers)</td><td>-0.01</td><td>0.02</td><td>1.8</td><td>5.6</td></tr><tr><td>Urban* Log(Followees)</td><td>0.06*</td><td>0.03</td><td>73.9***</td><td>14.4</td></tr><tr><td>IMF</td><td></td><td></td><td>369.8***</td><td>88.3</td></tr><tr><td>Intercept</td><td>-0.56***</td><td>0.05</td><td>-240.0*</td><td>110.7</td></tr><tr><td>R^2</td><td colspan="2">0.155</td><td colspan="2">/</td></tr></table>

## 5. Implications and Limitations

## 5.1 Findings

Several insights emerged from the results of this study. First, the type of post type exhibits a significant effect on the number of reposts, reposted depth, and reposted speed of disaster-related information. After the Yiliang earthquake, information related to situational awareness and social support, such as caution and advice, donations, and help-seeking, became viral from almost all perspectives (reposted amount, depth, speed, and duration) compared with other types of information. In addition, information on doubt-casting is significantly larger than personal-related and others information in terms of reposted amount and depth. Doubt-casting information became viral because of its potential to induce conflicts or negative feelings. However, the reposted amount of casualties and damages information is slightly smaller than that of personal-related and others information. This finding is reasonable because when people initially hear casualties during a disaster, they tend to repost prayers to offer condolences [27]. In our dataset, prayer posts of a few celebrities quickly went viral, thereby contributing to the relatively large number of average reposted counts.

Second, posts containing a high number of sad words are more viral in terms of reposted amount and duration compared with posts containing low number of sad words. This phenomenon may be reasonable because empathizing to users who were affected by the earthquake would be appreciated, and this factor is a type of social support (emotional support) [53]. However, the high number of angry words in the original posts reduces its tendency to become viral. This result may be reasonable because the earthquake is unpredictable, and the authorities exerted their best efforts to respond to such a disaster; thus, they exhibit low tendency to express anger and repost those posts with angry words.

Third, people near the earthquake gain more reposted amount, depth, and speed than those who were far from the earthquake. The information from the former contained more situational awareness than that from the latter. Moreover, the viral degree of disaster-related information from people with a high number of followers who are located near the event is considerably less than that of those who are located farther from the earthquake center. This phenomenon occurred because Yiliang is a small regions, such as Beijing, Shanghai, Guangzhou, and Shenzhen, which are far from Yiliang. The viral degree of disaster-related information from people with a high number of followees and are located near the event was higher than the disaster-related information from those located farther from the earthquake center. In summary, the results support construal-level theory and suggest that individuals construe related information differently depending on varying distances from the occurrence of an event.

Fourth, posts by people with high number of followers and who publish Help-seeking information were larger, deeper, quicker, and longer reposted by the public compared with the posts regarding the same content of those with low number of followers. Broadcasting this type of information is beneficial through the help of users with many followers from Weibo. By contrast, the help of users with high followee numbers decreases the dissemination amount of Help-seeking information. The type of post, the emotion manifested by the post, and the spatial location of the user in relation to his/her social capital as social media users should be considered for the significant effect on the viral degree of disaster-related information.

## 5.2 Implications for Research

This study further examines the effect of content type, content emotion, social media users’ physical location, and their social capital on the viral degree of disaster-related information. The study contributes to the theories in three ways.

First, this study fills the gap in recent emergency management research by providing a theory-driven typology of disaster-related information on social media. The proposed typology is based on previous empirical studies and well-established situational awareness and social support theories. The actual Weibo data after the Yiliang earthquake aided this study in providing theoretical and empirical pieces of evidence to interpret the varying viral degrees of different types of information. The study results provide theoretical support to formulate IS research on information dissemination on social media after disasters. These findings also lay the foundation for interdisciplinary emergency management research using information system (IS) techniques. In particular, the IS techniques, theory-driven typology, and empirical evidence can be extended to other emergency situations, including other natural disasters, riots, social movements, and mass incidents.

Second, to the best of our knowledge, this study incorporates a comprehensive set of factors related to disaster-related information sharing on social media. These factors are derived from two groups of factors: content-related factors (type and emotions in the content) and creator-related factors (geolocation and social capital of the creators). The results can describe the information-sharing patterns with a high resolution by analyzing the effect of these factors with well-established theories. These factors can also be used in enhancing the performance of future machine learning models that predict the propagation of disaster-related information on social media.

Third, the social capital of users exhibits a moderating effect on the main factors of the virality of disaster-related information. To the best of our knowledge, this study is the first to examine the moderating effect of the social capital users on emergencies. The significant moderating effect of social capital has been observed in content type and user location, thereby indicating that information should be differentiated on the basis of the social status of users who post it. This result applies to other problems that involve information dissemination on social media and on social networks in general.

## 5.3 Implications for practice

During and after disasters, people need information to be aware of the situation and take proper actions for coping with disasters [16, 30]. Social media has already become one of the important channels for the public to acquire timely and situational awareness information [16, 30, 33]. Authorities can develop a prioritized information release strategy for specific types of disaster-related information by developing the theory-driven typology of disaster-related information and investigating the viral degree, thereby possibly increasing the disaster mitigation efficiency.

This study also finds that the effects of content type, content emotion, and user location are moderated by the social capital of social media users. Such finding helps researchers or emergency management experts establish effective information-publishing strategies. The social capital of social media users should be employed to improve the efficiency of information release. For example, help-seeking information is crucial for disaster recovery; thus, this type of information must be deeply and quickly disseminated after the Yiliang earthquake. Emergency management departments can use the power of users with a high number of followers to develop a scientific and effective information promotion strategy for expanding this type of information dissemination. Users with a high number of followees and who are situated near the earthquake or those who have a high number of followers who live in urban areas can be highly prioritized to expand the dissemination scale of disaster-related information. With regard to redundant information that likely causes information overload or information that is harmful to disaster relief, dissemination should be mitigated through adjusting the emotion of a post, its publishing frequency, and its release time.

Third, we obtain evidence suggesting that the negative emotions of users with high social capital are likely propagated on social media. This finding indicates that social capital may contribute number of followees are viral. The sad emotions contained in the posts of social media users with a high number of followers are viral. Thus, the information posted by high social capital users is important to estimate and predict the spread of negative emotions (such as anger, anxiety, and sadness) among the public.

## 5.4 Limitations and future work

The study exhibits two limitations. First, all reposts are regarded as similar to the original ones for the convenience of calculating the reposted depth. However, users may add further information when reposting original posts, thereby increasing the chance that the information type can change into another type. Future research can pay increased attention to such added contents and investigate how content type changes at different periods of disasters. Second, our research background is in the domain of emergency management, which has a unique character. Thus, whether this background is suitable for other domains must be verified.

## 6. Conclusions

Social media has become a major platform for people to share disaster-related information during crises [22]. This study fills the current research gaps by examining the individual and joint effects of content and creator characteristics on the virality of disaster-related information. On the basis of situational awareness and social support theories, we develop a comprehensive typological of disaster-related information. In addition, we characterize the relationship between the virality of disaster-related information and content and content creator’s characteristics on a major Chinese social media platform. In practice, this study provides useful insights for authorities in emergency management into timely responses to disasters, effective information releasing strategies, and better use of users’ social capital to facilitate information propagation. As a result, authorities may provide the public with much-needed valid information during crises in a timely manner.

## Appendix

In this section, we have summarized the estimation results of the four basic models by considering all the variables including the control variables in Table 15. It shows that the coefficient for each factor is similar as the results in Table 7, and the standard error is robust.

<table><tr><td rowspan="3"></td><td colspan="8">Dependent Variable: Virality of Posts</td></tr><tr><td colspan="2">Reposted Amount</td><td colspan="2">Reposted Depth</td><td colspan="2">Reposted Speed</td><td colspan="2">Duration</td></tr><tr><td>B</td><td>SE</td><td>B</td><td>SE</td><td>B</td><td>SE</td><td>B</td><td>SE</td></tr><tr><td>T 2-Casualties and Y damages</td><td>-3.8e-3</td><td>0.04</td><td>0.18</td><td>0.09</td><td>0.02</td><td>0.05</td><td>-7.9e-3</td><td>0.07</td></tr><tr><td>P 3-Doubt casting</td><td>0.12*</td><td>0.05</td><td>0.29*</td><td>0.12</td><td>0.08</td><td>0.06</td><td>0.10</td><td>0.08</td></tr><tr><td>E 4-Caution and advice</td><td>0.16</td><td>0.09</td><td>0.39</td><td>0.20</td><td>0.15</td><td>0.10</td><td>0.39**</td><td>0.15</td></tr><tr><td>5-Donation-related</td><td>0.15***</td><td>0.05</td><td>0.40***</td><td>0.10</td><td>0.09</td><td>0.05</td><td>0.25***</td><td>0.07</td></tr><tr><td>6-Help-seeking</td><td>0.36***</td><td>0.06</td><td>0.96***</td><td>0.14</td><td>0.25***</td><td>0.07</td><td>0.48***</td><td>0.10</td></tr><tr><td>Anxious</td><td>0.01</td><td>9.1e-3</td><td>5.0e-3</td><td>0.02</td><td>-9.2e-3</td><td>9.6e-3</td><td>7.7e-3</td><td>0.01</td></tr><tr><td>Sad</td><td>0.02**</td><td>7.3e-3</td><td>0.05**</td><td>0.02</td><td>0.01</td><td>7.6e-3</td><td>0.02*</td><td>0.01</td></tr><tr><td>Anger</td><td>-0.01</td><td>6.1e-3</td><td>-0.04**</td><td>0.01</td><td>-0.01</td><td>6.4e-3</td><td>-0.02</td><td>9.7e-3</td></tr><tr><td>Neighbor</td><td>0.08*</td><td>0.03</td><td>0.22**</td><td>0.07</td><td>0.12***</td><td>0.03</td><td>0.09</td><td>0.05</td></tr><tr><td>Urban</td><td>0.07**</td><td>0.03</td><td>0.18**</td><td>0.06</td><td>0.06*</td><td>0.03</td><td>0.12**</td><td>0.04</td></tr><tr><td>Log(Followers)</td><td>0.21***</td><td>0.02</td><td>0.22***</td><td>0.04</td><td>0.23***</td><td>0.02</td><td>0.16***</td><td>0.03</td></tr><tr><td>Log(Followees)</td><td>-0.16***</td><td>0.03</td><td>-0.15</td><td>0.08</td><td>-0.15***</td><td>0.04</td><td>-0.23***</td><td>0.06</td></tr><tr><td>Type2* Log(Followers)</td><td>0.02</td><td>0.02</td><td>0.08</td><td>0.04</td><td>-0.02</td><td>0.02</td><td>0.07*</td><td>0.03</td></tr><tr><td>Type3* Log(Followers)</td><td>0.03</td><td>0.03</td><td>0.09</td><td>0.06</td><td>-0.01</td><td>0.03</td><td>0.06</td><td>0.04</td></tr><tr><td>Type4* Log(Followers)</td><td>-1.6e-3</td><td>0.04</td><td>0.14</td><td>0.09</td><td>4.6e-3</td><td>0.04</td><td>0.10</td><td>0.07</td></tr><tr><td>Type5* Log(Followers)</td><td>0.02</td><td>0.02</td><td>0.07</td><td>0.05</td><td>-0.04*</td><td>0.02</td><td>0.06</td><td>0.03</td></tr><tr><td>Type6* Log(Followers)</td><td>0.23***</td><td>0.03</td><td>0.41***</td><td>0.06</td><td>0.09**</td><td>0.03</td><td>0.24***</td><td>0.04</td></tr><tr><td>Type2* Log(Followees)</td><td>0.02</td><td>0.04</td><td>-0.01</td><td>0.08</td><td>0.04</td><td>0.04</td><td>0.06</td><td>0.06</td></tr><tr><td>Type3* Log(Followees)</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.09</td><td>0.09</td><td>0.05</td><td>0.09</td><td>0.07</td></tr><tr><td>Type4* Log(Followees)</td><td>0.02</td><td>0.07</td><td>0.03</td><td>0.16</td><td>0.14</td><td>0.08</td><td>1.3e-3</td><td>0.12</td></tr><tr><td>Type5* Log(Followees)</td><td>-0.04</td><td>0.04</td><td>-0.07</td><td>0.08</td><td>0.05</td><td>0.04</td><td>-0.01</td><td>0.06</td></tr><tr><td>Type6* Log(Followees)</td><td>-0.17**</td><td>0.05</td><td>-0.08</td><td>0.12</td><td>-0.04</td><td>0.06</td><td>-7.6e-3</td><td>0.08</td></tr><tr><td>Anxious* Log(Followers)</td><td>5.9e-3</td><td>3.6e-3</td><td>-9.0e-3</td><td>7.9e-3</td><td>-9.4e-3*</td><td>3.8e-3</td><td>1.9e-3</td><td>5.6e-3</td></tr><tr><td>Anxious* Log(Followees)</td><td>0.02**</td><td>7.2e-3</td><td>0.03*</td><td>0.02</td><td>0.02**</td><td>7.5e-3</td><td>0.02</td><td>0.01</td></tr><tr><td>Sad* Log(Followers)</td><td>4.9e-3</td><td>3.0e-3</td><td>0.02***</td><td>6.5e-3</td><td>8.5e-3**</td><td>3.1e-3</td><td>2.5e-3</td><td>4.7e-3</td></tr><tr><td>Sad* Log(Followees)</td><td>-0.01</td><td>5.4e-3</td><td>-0.03*</td><td>0.01</td><td>-0.02**</td><td>5.7e-3</td><td>-0.01</td><td>8.5e-3</td></tr><tr><td>Anger* Log(Followers)</td><td>-4.4e-3</td><td>2.4e-3</td><td>-0.01*</td><td>5.2e-3</td><td>-7.4e-3**</td><td>2.5e-3</td><td>-0.01***</td><td>3.7e-3</td></tr><tr><td>Anger* Log(Followees)</td><td>4.2e-3</td><td>4.2e-3</td><td>0.01</td><td>9.3e-3</td><td>0.01*</td><td>4.4e-3</td><td>0.02*</td><td>6.6e-3</td></tr><tr><td>Neighbor* Log(Followers)</td><td>-0.12***</td><td>0.01</td><td>-0.18***</td><td>0.03</td><td>-0.13***</td><td>0.01</td><td>-0.17***</td><td>0.02</td></tr><tr><td>Neighbor * Log(Followees)</td><td>0.22***</td><td>0.02</td><td>0.39***</td><td>0.05</td><td>0.26***</td><td>0.02</td><td>0.23***</td><td>0.04</td></tr><tr><td>Urban* Log(Followers)</td><td>0.12***</td><td>0.01</td><td>0.20***</td><td>0.02</td><td>0.06***</td><td>0.01</td><td>0.13***</td><td>0.02</td></tr><tr><td>Urban* Log(Followees)</td><td>-0.04</td><td>0.02</td><td>-0.09*</td><td>0.05</td><td>0.03</td><td>0.02</td><td>-0.04</td><td>0.03</td></tr><tr><td>Hashtag</td><td>9.0e-3</td><td>0.02</td><td>-0.06</td><td>0.05</td><td>0.01</td><td>0.02</td><td>-0.08*</td><td>0.04</td></tr><tr><td>URL</td><td>-0.01</td><td>0.02</td><td>-0.17***</td><td>0.05</td><td>-0.08***</td><td>0.02</td><td>-0.04</td><td>0.04</td></tr><tr><td>Time</td><td>2.8e-5**</td><td>9.0e-6</td><td>7.2e-5***</td><td>2.0e-5</td><td>1.3e-6</td><td>9.5e-6</td><td>7.4e-5**</td><td>1.4e-5</td></tr><tr><td>Picture</td><td>0.41***</td><td>0.06</td><td>0.65***51</td><td>0.13</td><td>0.27***</td><td>0.06</td><td>0.45***</td><td>0.09</td></tr><tr><td>Video</td><td>0.08</td><td>0.06</td><td>0.16</td><td>023</td><td>0.10</td><td>0.11</td><td>0.06</td><td>0.16</td></tr><tr><td>Involvement</td><td>0.19 ***</td><td>0.01</td><td>0.46***</td><td>0.03</td><td>0.25***</td><td>0.02</td><td>0.25***</td><td>0.02</td></tr><tr><td>Authority</td><td>0.15***</td><td>0.04</td><td>0.32***</td><td>0.09</td><td>0.46***</td><td>0.04</td><td>0.36***</td><td>0.07</td></tr><tr><td>Intercept</td><td>0.23***</td><td>0.05</td><td>0.08</td><td>0.10</td><td>0.21***</td><td>0.05</td><td>0.31***</td><td>0.07</td></tr><tr><td colspan="9">Sig. level · Significant at 0.1 level; *Significant at 0.05 level; ** Significant at 0.01 level; ***Significant at 0.001 level.</td></tr></table>

Table 15. Results of multiple linear regression for all variables.

## Author statement

Lifang Li: Conceptualization, Methodology, Investigation, Writing—Original Draft, Writing—Review & Editing, Visualization.

Jun Tian: Investigation, Writing—Review & Editing, Supervision, Funding acquisition.

Qingpeng Zhang: Conceptualization, Methodology, Investigation, Writing—Original Draft, Writing—Review & Editing, Supervision, Funding acquisition.

Jiaqi Zhou: Methodology, Investigation.

## References

[1] Kim T. Observation on copying and pasting behavior during the Tohoku earthquake: Retweet pattern changes[J]. International journal of information management, 2014, 34(4): 546-555.

[2] Chen R, Sakamoto Y. Perspective matters: Sharing of crisis information in social media[C]//2013 46th Hawaii International Conference on System Sciences. IEEE, 2013: 2033-2041.

[3] Guo J, Liu N, Wu Y, Zhang C, Why Do Citizens Participate on Government Social Media Accounts During Crises? A Civic Voluntarism Perspective, Information and Management (2020), doi: https://doi.org/10.1016/j.im.2020.103286

[4] Miles B, Morse S. The role of news media in natural disaster risk and recovery[J]. Ecological

Economics, 2007, 63(2-3): 365-373.

[5] Toriumi F, Sakaki T, Shinoda K, et al. Information sharing on Twitter during the 2011 catastrophic earthquake[C]//Proceedings of the 22nd International Conference on World Wide Web. 2013: 1025-1028.

[6] Chen R, Sakamoto Y. Feelings and perspective matter: Sharing of crisis information in social media[C]//2014 47th Hawaii International Conference on System Sciences. IEEE, 2014: 1958-1967.

[7] Yan L, Pedraza‐Martinez A J. Social media for disaster management: Operational value of the social conversation[J]. Production and Operations Management, 2019, 28(10): 2514-2532.

[8] Han Y, Lappas T, Sabnis G. The Importance of Interactions Between Content Characteristics and Creator Characteristics for Studying Virality in Social Media[J]. Information Systems Research, 2020. 0–13. https://doi.org/10.1287/isre.2019.0903.

[9] Imran M, Elbassuoni S, Castillo C, et al. Extracting information nuggets from disaster-related messages in social media[C]//Iscram. 2013, 791–800.

[10] Olteanu A, Vieweg S, Castillo C. What to expect when the unexpected happens: Social media communications across crises[C]//Proceedings of the 18th ACM conference on computer supported cooperative work & social computing. 2015: 994-1009.

[11] Chen Y, Liang C, Cai D. Understanding WeChat users’ behavior of sharing social crisis information[J]. International Journal of Human–Computer Interaction, 2018, 34(4): 356-366.

[12] White C, Plotnick L, Kushma J, et al. An online social network for emergency management[J]. International Journal of Emergency Management, 2009, 6(3-4): 369-382.

[13] Chen R. Sharing of Crisis Information in Social Media: The Roles of Distance, Perspective-taking, and Feelings[D]. Stevens Institute of Technology, 2014.

[14] Landwehr P M, Carley K M. Social media in disaster relief[M]//Data mining and knowledge discovery for big data. Springer, Berlin, Heidelberg, 2014: 225-257.

[15] Shao C, Ciampaglia G L, Varol O, et al. The spread of low-credibility content by social bots[J]. Nature communications, 2018, 9(1): 1-9.

[16] Skinner J. Natural disasters and Twitter: Thinking from both sides of the tweet[J]. First Monday, 2013, 18(9).

[17] Simon T, Goldberg A, Adini B. Socializing in emergencies—A review of the use of social media in emergency situations[J]. International Journal of Information Management, 2015, 35(5): 609-619.

[18] Li Y, Gao H, Yang M, et al. What are Chinese talking about in hot weibos?[J]. Physica A: Statistical Mechanics and its Applications, 2015, 419: 546-557.

[19] Li L, Zhang Q, Tian J, et al. Characterizing information propagation patterns in emergencies: A case study with Yiliang Earthquake[J]. International Journal of Information Management, 2018, 38(1): 34-41.

[20] S.E. Vieweg, Situational Awareness in Mass Emergency: A Behavioral and Linguistic Analysis of Microblogged Communications[D], (2012) 1–300.

[21] Webb J, Ahmad A, Maynard S B, et al. A situation awareness model for information security risk management[J]. Computers & security, 2014, 44: 1-15.

[22] Li L, Zhang Q, Wang X, et al. Characterizing the propagation of situational information in social media during covid-19 epidemic: A case study on weibo[J]. IEEE Transactions on

Computational Social Systems, 2020, 7(2): 556-562.

[23] N.A. Abdullah, U. Sains, D. Nishioka, I. Prefectural, Y. Tanaka, Y. Murayama, Why I Retweet? Exploring User’s Perspective on Decision -Making of Information Spreading during Disasters, Hawaii Int. Conf. Syst. Sci. 2017. (2017) 432–441.

[24] Turcotte J, York C, Irving J, et al. News recommendations from social media opinion leaders: Effects on media trust and information seeking[J]. Journal of Computer-Mediated Communication, 2015, 20(5): 520-535.

[25] Jin Y, Pang A. Future directions of crisis communication research: Emotions in crisis—The next frontier[J]. Handbook of crisis communication, 2010: 677-682.

[26] Jin Y, Pang A, Cameron G T. Toward a publics-driven, emotion-based conceptualization in crisis communication: Unearthing dominant emotions in multi-staged testing of the integrated crisis mapping (ICM) model[J]. Journal of Public Relations Research, 2012, 24(3): 266-298.

[27] Mukkamala A, Beck R. The Role of Social Media for Collective Behavior Development in Response to Natural Disasters[J]. Twenty-Sixth European Conference on Information Systems (ECIS2018), Portsmouth, UK, 2018.

[28] Son J, Lee H K, Jin S, et al. Content features of tweets for effective communication during disasters: A media synchronicity theory perspective[J]. International Journal of Information Management, 2019, 45: 56-68.

[29] Utz S, Schultz F, Glocka S. Crisis communication online: How medium, crisis type and emotions affected public reactions in the Fukushima Daiichi nuclear disaster[J]. Public relations review, 2013, 39(1): 40-46.

[30] Hornik J, Satchi R S, Cesareo L, et al. Information dissemination via electronic

word-of-mouth: Good news travels fast, bad news travels faster![J]. Computers in Human Behavior, 2015, 45: 273-280.

[31] Grabe M E, Kamhawi R. Hard wired for negative news? Gender differences in processing broadcast news[J]. Communication Research, 2006, 33(5): 346-369.

[32] Yardi S, Boyd D. Tweeting from the town square: Measuring geographic local networks[C]//Fourth international AAAI conference on weblogs and social media. 194–201.

[33] Yom-Tov E, Diaz F. The effect of social and physical detachment on information need[J]. ACM Transactions on Information Systems (TOIS), 2013, 31(1): 1-19.

[34] Backstrom L, Kleinberg J, Kumar R, et al. Spatial variation in search engine queries[C]//Proceedings of the 17th international conference on World Wide Web. 2008: 357-366.

[35] Lu Y, Yang D. Information exchange in virtual communities under extreme disaster conditions[J]. Decision Support Systems, 2011, 50(2): 529-538.

[36] Li L, Wang Z, Zhang Q, et al. Effect of anger, anxiety, and sadness on the propagation scale of social media posts after natural disasters. Information Processing & Management, 2020,

[37] Mendoza M, Poblete B, Castillo C. Twitter under crisis: Can we trust what we RT?[C]//Proceedings of the first workshop on social media analytics. 2010: 71-79.

[38] Vosoughi S, Roy D, Aral S. The spread of true and false news online[J]. Science, 2018, 359(6380): 1146-1151.

[39] Wang Z, Ye X, Tsou M H. Spatial, temporal, and content analysis of Twitter for wildfire hazards[J]. Natural Hazards, 2016, 83(1): 523-540.

[40] Starbird K, Palen L. Pass it on?: Retweeting in mass emergency[M]. Seattle, Washington, DC: International Community on Information Systems for Crisis Response and Management, 2010.

[41] Tapia A H, Bajpai K, Jansen B J, et al. Seeking the trustworthy tweet: Can microblogged data fit the information needs of disaster response and humanitarian relief organizations[C]//ISCRAM. 2011. 1–10.

[42] Hoang T A, Lim E P. Microblogging content propagation modeling using topic-specific behavioral factors[J]. IEEE Transactions on Knowledge and Data Engineering, 2016, 28(9): 2407-2422.

[43] Hoang T A, Lim E P. Virality and susceptibility in information diffusions[C]//Sixth international AAAI conference on weblogs and social media. 2012. 146–153.

[44] Yang J, Counts S. Predicting the speed, scale, and range of information diffusion in twitter[C]//Fourth International AAAI Conference on Weblogs and Social Media. 2010. 355– 358. doi:10.1016/j.plantsci.2007.02.015.

[45] Burnap P, Williams M L, Sloan L, et al. Tweeting the terror: modelling the social media reaction to the Woolwich terrorist attack[J]. Social Network Analysis and Mining, 2014, 4(1): 206.

[46] Stieglitz S, Dang-Xuan L. Emotions and information diffusion in social media—sentiment of microblogs and sharing behavior[J]. Journal of management information systems, 2013, 29(4): 217-248.

[47] Francalanci C, Metra I. Content-based discovery of twitter influencers[J]. E-Review of, 2015. 1–5.

[48] Bordia P, DiFonzo N. Problem solving in social interactions on the Internet: Rumor as social

cognition[J]. Social Psychology Quarterly, 2004, 67(1): 33-49.

[49] Li X, Wang Z, Gao C, et al. Reasoning human emotional responses from large-scale social and public media[J]. Applied Mathematics and Computation, 2017, 310: 182-193.

[50] Vieweg S, Hughes A L, Starbird K, et al. Microblogging during two natural hazards events: what twitter may contribute to situational awareness[C]//Proceedings of the SIGCHI conference on human factors in computing systems. 2010: 1079-1088.

[51] Zhang W, Wang M, Zhu Y. Does government information release really matter in regulating contagion-evolution of negative emotion during public emergencies? From the perspective of cognitive big data analytics[J]. International Journal of Information Management, 2020, 50: 498-514.

[52] Marett K, Joshi K D. The decision to share information and rumors: Examining the role of motivation in an online discussion forum[J]. Communications of the Association for Information Systems, 2009, 24(1): 4.

[53] Lu W, Hampton K N. Beyond the power of networks: Differentiating network structure from social media affordances for perceived social support[J]. New Media & Society, 2017, 19(6): 861-879.

[54] Oh O, Kwon K H, Rao H R. An Exploration of Social Media in Extreme Events: Rumor Theory and Twitter during the Haiti Earthquake 2010[C]//Icis. 2010, 231: 7332-7336.

[55] Palen L, Vieweg S, Liu S B, et al. Crisis in a networked world: Features of computer-mediated communication in the April 16, 2007, Virginia Tech event. Social Science Computer Review, 2009, 27(4): 467-480.

[56] Wray R J, Becker S M, Henderson N, et al. Communicating with the public about emerging

health threats: lessons from the pre-event message development project[J]. American Journal of Public Health, 2008, 98(12): 2214-2222.

[57] Mukkamala, A., & Beck, R. (2018). The role of social media for collective behavior development in response to natural disasters. ECIS Proceedings, 109.

[58] Rudra K, Ghosh S, Ganguly N, et al. Extracting situational information from microblogs during disaster events: a classification-summarization approach[C]//Proceedings of the 24th ACM International on Conference on Information and Knowledge Management. 2015: 583-592.

[59] Qu Y, Huang C, Zhang P, et al. Microblogging after a major disaster in China: a case study of the 2010 Yushu earthquake[C]//Proceedings of the ACM 2011 conference on Computer supported cooperative work. 2011: 25-34.

[60] Tandoc Jr E C, Takahashi B. Log in if you survived: Collective coping on social media in the 1778-1793.

[61] Mirbabaie M, Zapatka E. Sensemaking in social media crisis communication–A case study on the Brussels Bombings in 2016[C]. In Proceedings of the 25th European Conference on Information Systems (ECIS), Guimarães, Portugal, June 5-10, 2017 (pp. 2169-2186).

[62] Shklovski I, Palen L, Sutton J. Finding community through information and communication technology in disaster response[C]//Proceedings of the 2008 ACM conference on Computer supported cooperative work. 2008: 127-136.

[63] Verma S, Vieweg S, Corvey W J, et al. Natural language processing to the rescue? extracting" situational awareness" tweets during mass emergency[C]//Fifth international AAAI conference

on weblogs and social media. 2011. 385–392.

[64] Qu Y, Huang C, Zhang P, et al. Harnessing social media in response to major disasters[C]//CSCW 2011 Workshop: Designing Social and Collaborative Systems for China. 2011. 2008–2011.

[65] Huang K Y, Chengalur-Smith I S, Pinsonneault A. Sharing is caring: Social support provision and companionship activities in healthcare virtual support communities. MIS Quarterly, 2019, 43(2): 395-424.

[66] Olsson E K, Nord L W. Paving the way for crisis exploitation: The role of journalistic styles

[67] Berger J, Milkman K L. What makes online content viral?. Journal of marketing research, 2012, 49(2): 192-205.

[68] Sreenivasan N D, Lee C S, Goh D H L. Tweet me home: Exploring information use on Twitter in crisis situations[C]//International Conference on Online Communities and Social Computing. Springer, Berlin, Heidelberg, 2011: 120-129.

[69] Chatfield A T, Scholl H J, Brajawidagda U. # Sandy tweets: citizens' co-production of time-critical information during an unfolding catastrophe[C]//2014 47th Hawaii International Conference on System Sciences. IEEE, 2014: 1947-1957.

[70] Gupta A, Lamba H, Kumaraguru P, et al. Faking sandy: characterizing and identifying fake images on twitter during hurricane sandy[C]//Proceedings of the 22nd international conference on World Wide Web. 2013: 729-736.

[71] Hughes A L, St. Denis L A A, Palen L, et al. Online public communications by police & fire services during the 2012 Hurricane Sandy[C]//Proceedings of the SIGCHI conference on

human factors in computing systems. 2014: 1505-1514.

[72] Kim H J, Cameron G T. Emotions matter in crisis: The role of anger and sadness in the publics’ response to crisis news framing and corporate crisis response[J]. Communication Research, 2011, 38(6): 826-855.

[73] George B, Baekgaard M, Decramer A, et al. Institutional isomorphism, negativity bias and performance information use by politicians: A survey experiment[J]. Public administration, 2020, 98(1): 14-28.

[74] Yin C, Zhang X, Liu L. Reposting negative information on microblogs: Do personality traits matter?[J]. Information Processing & Management, 2020, 57(1): 102106.

[75] Zhang H, Qu C. Emotional, especially negative microblogs are more popular on the web: evidence from an fMRI study[J]. Brain imaging and behavior, 2018: 1-11.

[76] Liu B F, Fraustino J D, Jin Y. How disaster information form, source, type, and prior disaster exposure affect public outcomes: Jumping on the social media bandwagon?[J]. Journal of Applied Communication Research, 2015, 43(1): 44-65.

[77] Jin Y, Pang A, Cameron G T. The role of emotions in crisis responses: Inaugural test of the integrated crisis mapping (ICM) model[J]. Corporate Communications: An International Journal, 2010, 15(4): 428-452.

[78] Bebbington, K., MacLeod, C., Ellison, T. M., & Fay, N. (2017). The sky is falling: evidence of a negativity bias in the social transmission of information. Evolution and Human Behavior, 38(1), 92–101.

[79] Trope Y, Liberman N. Construal-level theory of psychological distance[J]. Psychological review, 2010, 117(2): 440.

[80] Fujita K, Henderson M D, Eng J, et al. Spatial distance and mental construal of social events[J]. Psychological Science, 2006, 17(4): 278-282.

[81] Osatuyi B. Information sharing on social media sites[J]. Computers in Human Behavior, 2013, 29(6): 2622-2631.

[82] Bakshy E, Rosenn I, Marlow C, et al. The role of social networks in information diffusion[C]//Proceedings of the 21st international conference on World Wide Web. 2012: 519-528.

[83] Warren M. The digital vicious cycle: Links between social disadvantage and digital exclusion in rural areas[J]. Telecommunications Policy, 2007, 31(6-7): 374-388.

[84] Aral S, Muchnik L, Sundararajan A. Distinguishing influence-based contagion from homophily-driven diffusion in dynamic networks[J]. Proceedings of the National Academy of Sciences, 2009, 106(51): 21544-21549.

[85] Stern M J, Adams A E, Elsasser S. Digital inequality and place: The effects of technological diffusion on Internet proficiency and usage across rural, suburban, and urban counties[J]. Sociological Inquiry, 2009, 79(4): 391-417.

[86] Johnson I, McMahon C, Schöning J, et al. The Effect of Population and" Structural" Biases on Social Media-based Algorithms: A Case Study in Geolocation Inference Across the Urban-Rural Spectrum[C]//Proceedings of the 2017 CHI conference on Human Factors in Computing Systems. 2017: 1167-1178.

[87] Sakaki T, Okazaki M, Matsuo Y. Earthquake shakes Twitter users: real-time event detection by social sensors[C]//Proceedings of the 19th international conference on World wide web. 2010: 851-860.

[88] Chang H H, Chuang S S. Social capital and individual motivations on knowledge sharing: Participant involvement as a moderator[J]. Information & management, 2011, 48(1): 9-18.

[89] Hofer M, Aubert V. Perceived bridging and bonding social capital on Twitter: Differentiating between followers and followees[J]. Computers in Human Behavior, 2013, 29(6): 2134-2142.

[90] Chiu C M, Hsu M H, Wang E T G. Understanding knowledge sharing in virtual communities: An integration of social capital and social cognitive theories[J]. Decision support systems, 2006, 42(3): 1872-1888.

[91] Roy, K. C., Hasan, S., Sadri, A. M., & Cebrian, M. (2020). Understanding the efficiency of social media based crisis communication during hurricane Sandy. International Journal of Information Management, (August 2018), 102060. doi:10.1016/j.ijinfomgt.2019.102060.

[92] Suh B, Hong L, Pirolli P, et al. Want to be retweeted? large scale analytics on factors impacting retweet in twitter network[C]//2010 IEEE Second International Conference on Social Computing. IEEE, 2010: 177-184.

[93] Alaa A M, Ahuja K, van der Schaar M. A micro-foundation of social capital in evolving social networks[J]. IEEE Transactions on Network Science and Engineering, 2017, 5(1): 14-31.

[94] Zhao K, Kumar A. Who blogs what: understanding the publishing behavior of bloggers[J]. World Wide Web, 2013, 16(5-6): 621-644.

[95] Asgary, A., & Penfold, G. (2011). Willingness to Donate to Victims of a Hypothetical Future Earthquake Disaster in Vancouver. International Journal of Business and Social Science, 2(16), 64–71.

[96] Diakopoulos N, De Choudhury M, Naaman M. Finding and assessing social media information sources in the context of journalism[C]//Proceedings of the SIGCHI conference on human

factors in computing systems. 2012: 2451-2460.

[97] Takahashi K, Kitamura Y. Disaster anxiety and self-assistance behaviours among persons with cervical cord injury in Japan: a qualitative study[J]. BMJ open, 2016, 6(4): e009929.

[98] McNicol S, Aillerie K. Digital inequalities and social media: experiences of young people in Chile[J]. Information and Learning Science, 2017. 372–384.

[99] Blank G, Graham M, Calvino C. Local geographies of digital inequality[J]. Social Science Computer Review, 2018, 36(1): 82-102.

[100] Robinson L, Cotten S R, Ono H, et al. Digital inequalities and why they matter[J]. Information, communication & society, 2015, 18(5): 569-582.

[101] Kempe D, Kleinberg J, Tardos É. Maximizing the spread of influence through a social network[C]//Proceedings of the ninth ACM SIGKDD international conference on Knowledge discovery and data mining. 2003: 137-146.

[102] Jiang Q, Song G, Cong G, et al. Simulated annealing based influence maximization in social networks[C]//Proceedings of the twenty-fifth AAAI conference on artificial intelligence. 2011: 127-132.

[103] Lu Z, Wen Y, Cao G. Information diffusion in mobile social networks: The speed perspective[C]//IEEE INFOCOM 2014-IEEE Conference on Computer Communications. IEEE, 2014: 1932-1940.

[104] Krippendorff K. Content analysis: An introduction to its methodology[M]. Sage publications, 2018.

[105] Pennebaker J W, Francis M E, Booth R J. Linguistic inquiry and word count: LIWC 2001[J]. Mahway: Lawrence Erlbaum Associates, 2001, 71(2001): 2001.

[106] Nahapiet J, Ghoshal S. Social capital, intellectual capital, and the organizational advantage[J]. Academy of management review, 1998, 23(2): 242-266.

[107] Li R, Suh A. Factors influencing information credibility on social media platforms: Evidence from Facebook pages[J]. Procedia computer science, 2015, 72(1): 314-328.

[108] Lei K, Liu Y, Zhong S, et al. Understanding user behavior in Sina Weibo online social network: A community approach[J]. IEEE Access, 2018, 6: 13302-13316.

[109] Marwick A, Boyd D. To see and be seen: Celebrity practice on Twitter[J]. Convergence, 2011, 17(2): 139-158.

[110] Pervin N, Takeda H, Toriumi F. Factors affecting retweetability: an event-centric analysis on Twitter[J]. Icis-Rp. 2014. 1–10.

[111] Wang X, Liu H, Zhang P, et al. Identifying information spreaders in twitter follower networks[J]. School of Comput., Infor., and Decision Sys. Eng, 2012.

[112] Nagarajan M, Purohit H, Sheth A. A qualitative examination of topical tweet and retweet practices[C]//Fourth International AAAI Conference on Weblogs and Social Media. 2010. 295–298.

[113] Burger J, Gochfeld M, Jeitner C, et al. Trusted information sources used during and after Superstorm Sandy: TV and radio were used more often than social media[J]. Journal of Toxicology and Environmental Health, Part A, 2013, 76(20): 1138-1150.

[114] Cadavez V A P, Henningsen A. The use of seemingly unrelated regression to predict the carcass composition of lambs[J]. Meat science, 2012, 92(4): 548-553.

[115] Greene W H. Econometric analysis[M]. Pearson Education India, 2003.

[116] Liu S B, Palen L, Sutton J, et al. In search of the bigger picture: The emergent role of on-line

photo sharing in times of disaster[C]//Proceedings of the information systems for crisis response and management conference (ISCRAM). 2008: 4-7.[117] Hansson K, Ekenberg L. Understanding the demographics of the crowd: mapping the role of the participant in crisis informatics[C]//Proceedings of the Internationsl Conference on Electronic Governance and Open Society: Challenges in Eurasia. 2017: 160-165.

[118] Li H, Sakamoto Y. Social impacts in social media: An examination of perceived truthfulness and sharing of information[J]. Computers in Human Behavior, 2014, 41: 278-287.

[119] Veil S R, Buehner T, Palenchar M J. A work‐in‐process literature review: Incorporating social media in risk and crisis communication[J]. Journal of contingencies and crisis management, 2011, 19(2): 110-122.

[120] Mirbabaie M, Bunker D, Stieglitz S, et al. Social media in times of crisis: Learning from Hurricane Harvey for the coronavirus disease 2019 pandemic response[J]. Journal of Information Technology, 2020: 0268396220929258.

[121] Otioma C, Madureira A M, Martinez J. Spatial analysis of urban digital divide in Kigali, Rwanda[J]. GeoJournal, 2019, 84(3): 719-741.

[122] Heckman, J. J. (1979). Sample selection bias as a specification error. Econometrica: Journal of the Econometric Society, 1979: 153-161.

[123] Z. Jianqiang, G. Xiaolin, T. Feng, A new method of identifying influential users in the micro-blog networks, IEEE Access. 5 (2017) 3008–3015.

[124] Lu, Y., & Huang, Y. H. C. (2018). Getting emotional: An emotion-cognition dual-factor model of crisis communication. Public Relations Review, 44(1), 98-107.

[125] Veil, S. R., Buehner, T., & Palenchar, M. J. (2011). A work‐in‐process literature review:

Incorporating social media in risk and crisis communication. Journal of contingencies and crisis management, 19(2), 110-122.

[126] Wiegand S, Middleton S E. Veracity and velocity of social media content during breaking news: Analysis of November 2015 Paris shootings[C]//Proceedings of the 25th international conference companion on world wide web. 2016: 751-756.

[127] Zhao, X., Zhan, M., & Wong, C. W. (2018). Segmenting and understanding publics in a social media information sharing network: An interactional and dynamic approach. International Journal of Strategic Communication, 12(1), 25-45.

[128] Berger, J., & Milkman, K. (2010). Social transmission, emotion, and the virality of online content. Wharton Research Paper, 106, 1-52.

[129] Xiong, X., Li, Y., Qiao, S., Han, N., Wu, Y., Peng, J., & Li, B. (218). An emotional contagion model for heterogeneous social media with multiple behaviors. Physica A: Statistical Mechanics and its Applications, 490, 185-202.
