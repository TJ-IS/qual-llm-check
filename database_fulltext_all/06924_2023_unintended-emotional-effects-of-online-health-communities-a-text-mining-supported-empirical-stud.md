---
otero_id: 6924
otero_key: "KXNUZDH3"
title: "Unintended Emotional Effects of Online Health Communities: A Text Mining-Supported Empirical Study"
authors: "Jiaqi Zhou; Qingpeng Zhang; Sijia Zhou; Xin Li; Xiaoquan (Michael) Zhang"
year: "2023"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/17018"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# UNINTENDED EMOTIONAL EFFECTS OF ONLINE HEALTH COMMUNITIES: A TEXT MINING-SUPPORTED EMPIRICAL STUDY <sup>1</sup>

Jiaqi Zhou and Qingpeng Zhang School of Data Science, City University of Hong Kong, Kowloon, Hong Kong, CHINA. {jiaqi.zhou@my.cityu.edu.hk}{qingpeng.zhang@cityu.edu.hk}

Sijia Zhou Department of Electronic Commerce, School of Economics and Management, Southeast University, Nanjing, CHINA {sijiazhou@seu.edu.cn}

Xin Li Department of Information Systems, College of Business, City University of Hong Kong, Kowloon, Hong Kong, CHINA {Xin.Li.PhD@gmail.com}

## Xiaoquan (Michael) Zhang

Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, Shenzhen, and Department of Decision Sciences and Managerial Economics, Business School, Chinese University of Hong Kong, Kowloon, Hong Kong, CHINA {zhangxiaoquan@sem.tsinghua.edu.cn}

Online health communities (OHCs) play an important role in enabling patients to exchange information and obtain social support from each other. However, do OHC interactions always benefit patients? In this research, we investigate different mechanisms by which OHC content may affect patients’ emotions. Specifically, we notice users can read not only emotional support intended to help them but also emotional support targeting other persons or posts that are not intended to generate any emotional support (auxiliary content). Drawing from emotional contagion theories, we argue that even though emotional support may benefit targeted support seekers, it could have a negative impact on the emotions of other support seekers. Our empirical study on an OHC for depression patients supports these arguments. Our findings are new to the literature and have critical practical implications since they suggest that we should carefully manage OHC-based interventions for depression patients to avoid unintended consequences. We design a novel deep learning model to differentiate emotional support from auxiliary content. Such differentiation is critical for identifying the negative effect of emotional support on unintended recipients. We also discuss options to alter the intervention volume, length, and frequency to tackle the challenge of the negative effect.

Keywords: Emotional contagion, emotional support, text classification, deep learning, online health community

## Introduction

Online health communities (OHCs) are platforms on which users can exchange information about diseases. OHCs play an important role in patients’ health management. Studies have demonstrated that OHCs can facilitate cross-region healthcare knowledge transfer (Mein Goh et al., 2016) and enable patients to help each other (Luo et al., 2018). Involvement in OHCs improves patients’ health (Yan & Tan, 2014, 2017).

In this study, we are interested in the impact of patients’ involvement in OHCs on their emotional status, which is an important part of their health. In particular, for mental diseases such as depression, studied in this paper, patients’ emotional status has critical implications (Smith, 2014). The inappropriate management of emotions may lead to severe outcomes such as suicide (Chau et al., 2020). However, it is sometimes difficult for patients to find people around to help. In such cases, OHCs become an important channel for patients to express themselves and seek support. Understanding OHCs’ emotional impact on patients is critical for improving OHC management and support for mental disease patients.

Although OHCs open up a new channel for patients to seek help, the emotional impact of this channel is not fully clear. Previous studies often attribute OHCs’ emotional impact to emotional support (Yan & Tan, 2014), which suggests that support providers’ posts help meet individuals’ social needs, such as affection and esteem, and improve their health (Kaplan et al., 1977). Beaudoin and Tao (2007) found that social support in an online cancer community led to positive outcomes in dealing with stress and depression. Yoo et al. (2014) found that both giving and receiving emotional support affected users’ emotions and showed that this effect is moderated by communication competence. The literature has also studied the antecedents of effective emotional support to direct practice (Chen et al., 2019; Huang et al., 2019).

Nevertheless, these studies often focus on the targeted audiences of provided support and ignore how social support can affect other audiences in OHCs. In reality, OHCs tend to take an open audience format (such as web forums) to facilitate anonymous posts. This is different from most health consultation channels, which tend to be private, and from many social networking websites, which are semiprivate and open only to selected friends. The open format of OHCs weakens support providers’ ability to control the recipients of their posts. Both targeted and other audiences could view such content. OHCs’ impact on audiences that are not the target of conversation has not been well studied in the literature.

Meanwhile, OHCs contain content that is not emotional support. As illustrated in Figure 1, textual online social support may also be informational support (Yan & Tan, 2014). OHCs also contain content such as general discussions (casual chats), advertisements, and other noise. We name the content that is not for emotional support purposes “auxiliary content.” While auxiliary content does not aim to improve patients’ emotions, it may also contain sentimental expressions, which could affect support seekers’ emotions. Such an impact has also not been sufficiently examined in the literature.

To further understand the emotional impact of OHCs, we seek insight from appraisal theory (Lazarus, 1991) and emotional contagion theory (Elfenbein, 2014). According to appraisal theory, emotional registration depends on the personal interpretation of the received stimulus. Thus, the same post may derive different emotional consequences in targeted and unintended recipients and generate outcomes that are not expected by support providers, such as social comparison (Barsade, 2002). This difference could be intensified in OHC users, who are patients suffering from diseases. According to emotional contagion theory, users’ emotional states can be influenced by stimuli in posts, which can take the form of an emotional expression of both emotional support and auxiliary content. However, these two types of content may trigger different levels of social comparison and emotional effects due to their different purposes. In light of these theories, as illustrated in Figure 1, we differentiate emotional support from auxiliary content and study how the sentimental expressions they contain may affect the targeted audience as well as the unintended audience. This study is different from previous studies on emotional support (Chen et al., 2019; Huang et al., 2019), which are mainly represented by the dashed arrow in Figure 1. This study is also different from traditional emotional contagion studies on social networking platforms (Ferrara & Yang, 2015; Kramer et al., 2014), which have different content and audiences from OHCs and thus cannot support the identification of the mechanisms examined in this study.

As illustrated in Figure 1, the core of this work is an empirical study to unveil the unintended emotional impacts of OHCs. For this purpose, we collected a dataset from a large web forum for patients with depression (i.e., major depressive disorder) in China. Before conducting the empirical study, we designed a deep learning model to differentiate emotional support from auxiliary content, since such data classification is difficult and is seldom provided by OHCs. The model outperformed stateof-the-art text mining methods in this task. Using the empirical framework, we established the necessity of conducting emotional support differentiation and examined how to respond to the negative effect of auxiliary content. Specifically, our empirical study shows that support seekers’ emotions (reflected by their expression sentiments) are negatively influenced by the sentiment of emotional support if support seekers are not the targeted audience. To strengthen the identification, we further conducted a post-level analysis and examined posts between support seekers’ replies in a thread, which have a higher chance of being viewed by them. The results remained stable. We provide supporting evidence that this negative effect is related to social comparison and the extent of patients’ depression. We also found the scales of the positive and negative effects of emotional support to be comparable. In other words, if support providers use a unified positive tone to support depression patients, their efforts will cancel out. Such ineffective online emotional support may lead to severe unintended negative impacts on depression patients, such as suicide and self-harm. This finding puts support providers in a contradictory position. In our follow-up analyses, we show that more support providers, a larger volume of responses, and longer responses would better combat our identified negative effects of OHCs in helping patients.

![](/api/attachments/KXNUZDH3/fulltext/images/d6cef3b3dddb424b91012b6c08a71d19b6dc4e4017d9b69096393f7c997b5d4a.jpg)  
Figure 1. Illustration of the Contents and the Players in OHCs

This paper makes three main contributions. First, we find that emotional support in OHCs could have a negative impact on unintended recipients. The appearance of this effect is due to support seekers’ comparison with others who have received support, which does not exist in the regular consultation process but is common in OHCs. This finding enriches our theoretical understanding of emotional influences in OHCs and calls for the development of strategies to mitigate such side effects.

Second, our analyses show that differentiating emotional support from auxiliary content is critical for identifying the negative impact of off-target emotional support. This may be due to the fact that auxiliary content’s noise covers the true effect of off-target support. While the reason for this requires more investigation, from a methodological perspective, the study shows the value of text classification in empirical studies.

Third, we leverage the two-directional structure (temporal sequence and reply interactions) of posts to build a deep learning model to differentiate emotional support from auxiliary content. Our evaluation shows that it outperforms state-of-the-art algorithms in classifying unbalanced posts. This algorithm itself is a technical contribution and can be used in studying web forums.

## Literature Review

## Studies on the Emotional Impact of OHCs

In Table 1, we review the studies on the emotional impact of OHCs. As can be seen, most previous studies tend to attribute OHCs’ emotional impact to emotional support. For example, Beaudoin and Tao (2007) studied an online cancer community and found that online social support led to positive outcomes in dealing with stress and depression. Aarts et al. (2015) found that an online expert forum positively influenced patient outcomes since patients require emotional support from their care providers. Previous studies have also found that emotional support has a bidirectional impact. Yoo et al. (2014) found that both giving and receiving emotional support affect users’ emotions and showed that this effect is moderated by communication competence. Chen et al. (2019) found that providing and receiving emotional support both affect users’ emotions.

Given the clear relationship between emotional support and emotions, some studies have focused on the antecedents of (perceived) emotional support, where stronger perceived support would indicate a better support effect. For example, Chung (2014) showed that the usage of discussion boards and online social networking features, such as friending and sharing on blogs, are both helpful in satisfying the need for emotional support. Reifegerste et al. (2017) found that asking and answering questions in forums strongly affects perceived emotional support.

<table><tr><td colspan="5">Table 1. Major Studies on the Emotional Impact of OHCs</td></tr><tr><td>Study</td><td>Mechanism</td><td>Subject</td><td>Support measure</td><td>Finding</td></tr><tr><td>(Beaudoin &amp; Tao, 2007)</td><td>Emotional support → Emotion</td><td>Target</td><td>Survey</td><td>Social support affects emotions, such as depression, stress, etc.</td></tr><tr><td>(Nambisan, 2011)</td><td>Emotional support → Emotion</td><td>Target</td><td>Survey</td><td>Social support does not affect perceived empathy</td></tr><tr><td>(Yoo et al., 2014)</td><td>Emotional support → Emotion</td><td>Provider; target</td><td>Emotional support post</td><td>Giving/receiving emotional support affects emotional well-being, which is moderated by communication competence</td></tr><tr><td>(Aarts et al., 2015)</td><td>Emotional support → Emotion</td><td>Target</td><td>Emotional support post</td><td>Expert forum helps to address patients&#x27; concerns</td></tr><tr><td>(Chen et al., 2019)</td><td>Emotional support → Emotion</td><td>Provider; target</td><td>Emotional support post</td><td>Provisioning and receiving emotional support both affect user emotion</td></tr><tr><td>(Chung, 2014)</td><td>Activity → Emotional support</td><td>Target</td><td>Survey</td><td>Discussion board use and friending activities improve perceived emotional support</td></tr><tr><td>(Reifegerste et al., 2017)</td><td>Activity → Emotional support</td><td>Provider; target</td><td>Survey</td><td>Asking and answering questions affects perceived emotional support</td></tr><tr><td>(Park &amp; Conway, 2017)</td><td>Activity → Emotion</td><td>Provider</td><td>-</td><td>Participation in forum improves users&#x27; emotions</td></tr><tr><td>(Chee, 2010)</td><td>Activity → Emotion similarity</td><td>Provider; target</td><td>-</td><td>Frequently interacting users have similar emotions</td></tr><tr><td>(Lin et al., 2019)</td><td>Emotion contagion</td><td>Target</td><td>Reply post</td><td>Sentiments of replies positively affect patients&#x27; emotions</td></tr><tr><td>This study</td><td>Unintended emotional impact</td><td>Non-target</td><td>Post</td><td>The impact of off-target emotional support and the impact of auxiliary content</td></tr></table>

A few studies have touched on factors other than emotional support that affect users’ emotions in OHCs. For example, Lin et al. (2019) found that the sentiment of replies positively affects patients’ emotions and showed that this effect can be explained by emotional contagion. Other than emotional content, individuals’ actions play an important role in OHCs’ emotional impact. Park and Conway (2017) found that participation in an online community itself has a positive impact on users’ emotions. Chee (2010) also found that frequently interacting users have similar emotions.

To illustrate the gap in the literature, we differentiate previous research according to how subjects are influenced and the measure of emotional support (see Table 1). In general, most studies have focused on the influence on the target subject of an action. A few studies have explored the emotional effect on subjects who initiate the action. There is rich evidence showing that both parties are influenced by the emotional exchange on OHCs. However, OHCs have many users besides the two parties in a conversation. How the emotional content affects such third-party players is unclear.

From a measurement perspective, some studies have relied on self-disclosure in questionnaires to measure emotional support (Nambisan, 2011). Another common practice is to employ post content as an indicator of emotional support. For example, Lin et al. (2019) used repliers’ posts to examine the emotional impact of OHCs. Some research has focused on emotional support posts (Chen et al., 2019). Nevertheless, OHCs contain more than just emotional support content. While examining other types of content is common in previous healthcare research (Yan & Tan, 2014), the differentiation of post content has thus far been insufficient in these studies.

To extend the existing literature, we focus on users who are either the provider or the target of emotional support to examine the emotional impact of OHCs. In addition, this study considers both emotional support and auxiliary content for reasons other than emotional support (such as informational support, general discussions, advertisements, and other noise).

## Emotional Contagion in OHCs

Extending previous OHC studies from the perspective of emotional support, we consider it necessary to employ emotional contagion theory to explain the emotional impact of OHCs.

Emotional contagion traditionally refers to emotion transfer between people through social interactions (Hatfield et al., 1993) due to mimicry, comparison, empathy, etc., and has been well studied in the offline context (Fowler and Christakis 2008). Recently, emotional contagion has also been found in computer-mediated communication, such as instant messaging (Hancock et al., 2008). More studies on emotional contagion have considered online social networks (Zhang & Zhu, 2011; Zhang & Wang, 2012; Sun et al., 2019). In a seminal paper, Kramer et al. (2014) conducted a field experiment on Facebook and identified emotional contagion where individuals’ posts affected the sentiments of their friends’ posts. Lin and Utz (2015) further found that the contagious effect on Facebook is stronger when the posts come from a strong tie than a weak tie. Ferrara and Yang (2015) studied emotional contagion on Twitter and found that positive emotions transfer more easily than negative emotions.

While OHCs may have one-to-one social networking features, they often take a web forum format, where patients can join anonymous open discussions to protect their privacy and gain information from multiple sources. As a result, communication in OHCs is often less directed than on social networking sites. There was limited research on this type of social media when studying emotional contagion. Related studies on other anonymous channels have found that YouTube videos (Rosenbusch et al., 2019) and Online News (Bösch et al., 2018) influence the sentiment of user comments, and earlier comments affect the sentiment of later comments (Kwon & Gruzd, 2017). These findings indicate the existence of emotional contagion In anonymous open discussions but they are not sufficient to provide a clear picture of emotional contagion in generic web forums.

Moreover, the topics and audiences of OHCs are different from regular social networking sites. Pressured by disease, OHC users are more sensitive than other people, which may affect their emotional contagion behavior. Previously, Lin et al. (2019) found that the sentiments of replies in OHCs influence patients’ emotions, which might be due to emotional contagion. But the study failed to provide adequate evidence and identification.

In viewing the uniqueness of OHCs and the limits of previous studies, this study further investigates emotional contagion in OHCs.

## Research Context

The data used in this study were collected from Douban (Wang et al., 2011), a popular social media platform for liberal arts topics in China, with approximately 62 million users. One major feature of the platform is its interest groups, which are communities devoted to various topics. These interest groups are presented as web forums with threads and replies generated by the users.

The interest group we studied is the largest Douban interest group for major depressive disorders (MDD). This group is specifically designed for people who have been diagnosed with depression rather than simply having depressive feelings. This group encourages its members to discuss their depression-related problems and possible therapies to cope with negative emotions and difficult experiences. The group was founded on August 26, 2008, and had more than 5,000 members at the time of data collection in 2015. Soon after we retrieved the data, the group changed from public to private, disabling nonmembers’ access to the content.

In the MDD group, any member can seek support by starting a discussion thread. Other group members can reply to the support seeker’s original post or other replies in a thread. In both cases, new replies are added to the end of the thread. Thus, as illustrated in Figure A4 in the Appendix, all replies in a thread are listed in chronological order without formatting differences, which means that users will see earlier posts before reading later posts. These replies may contain support providers’ support to support seekers, general discussions that veer off track from the original posts, advertisements, and other posts. After reading such discussions, a support seeker may reply to certain posts. For example, in Figure A4, User 2’s Reply 3 replies to User 3’s Reply 2. The forum also contains threads that are started by other support seekers or non-support seekers, which a support seeker may visit. Support seekers will be notified if someone replies in a thread they started or participated in if they do not view it within a certain time frame.

## Theoretical Basis and Hypotheses

Given the MDD group context, a particular support seeker (Seeker S) may observe different information. First, Seeker S may read the information in their help-seeking thread, of which Seeker S is the support target of most posts, except for off-track conversations. Second, Seeker S may visit other support seekers’ support-seeking threads and observe social support provided to other persons. In such a case, Seeker S is an unintended audience of those posts. From Seeker S’s perspective, we call the content targeting Seeker S “on-target content” and the content targeting other persons (where Seeker S is not the intended audience) “off-target content.”

Moreover, we classify the content that Seeker S observes into emotional support and auxiliary content. As mentioned before, the two types of content have different purposes in helping their intended audience. Since MDD’s purpose is to help patients suffering from depression, emotional support posts are in a unique position to affect patients’ emotions. Their purpose is to reduce patients’ negative feelings and avoid the potentially severe outcomes of depression. Auxiliary content, including informational support, off-track discussions, advertisements, and other noise, does not aim to change patients’ emotions or to help the patients at all. Both types of content may exist in any thread, whether Seeker S is the intended audience or not.

Thus, we could differentiate the posts in the MDD group into four groups for each support seeker based on whether they are the target of the posts and the purpose of the posts as follows: (1) emotional support targets the focal support seeker, (2) off-target emotional support targets a different audience, (3) auxiliary content targets the focal support seeker, and (4) off-target auxiliary content targets a different audience. From each support seeker’s perspective, only the first type of content is emotional support, which is the major focus of previous studies (Keating, 2013; Yoo et al., 2014). Our study is more focused on the other three types of posts that are either not intended for the focal support seeker or not intended to be emotional support at all, leading to the hypotheses in Figure 2. In these hypotheses, we study, from an emotional contagion perspective, whether the sentiment of posts could affect users’ emotions (as reflected by their post sentiments).

## Effect of Off-Target Emotional Support

The purpose of emotional support is to offer empathy, concern, affection, love, trust, acceptance, intimacy, encouragement, or care to a subject. In emotional support content, support providers may provide comforting words or use others’ experiences to encourage the targeted support seeker (Smailhodzic et al., 2016). In offline contexts and some computer-mediated communication channels, emotional support can be privately provided to depression patients. However, in OHCs, support seekers can often see emotional support content targeted at other users. Such offtarget emotional support could create a unique impact on the support seeker.

According to the appraisal theory (Lazarus, 1991), the emotional registration of a stimulus depends on personal interpretation. Thus, the same stimulus may derive different emotional sequences in on-target and off-target recipients. Specifically, when observing one person providing a positive expression to help another person, a support seeker may develop a sense of the targeted user’s feelings through imagining (Elfenbein, 2014), which may cause opposite appraisal due to two competing mechanisms—empathy and social comparison.

On the one hand, imagining another support seeker’s feelings may trigger an empathy process (Hatfield et al., 1993), where the recipient shares a similar emotional state with the target support seeker (Hawk et al., 2011). In this process, the recipient would put themselves in the same position as the target. If more positive emotional support is provided, the recipient may project that the targeted support seeker’s emotion has improved, and thus their emotional status and expression sentiment will be more positive.

On the other hand, the recipient may assume a competitive or comparative position with the target support seeker, which causes social comparison (Barsade, 2002). The effect of social comparison depends on whether comparers position themselves as superior or inferior to others (Suls et al., 2002). If the recipient’s assessment is that the target support seeker’s emotion has improved, the recipient may feel worse off and not cared for. Thus, a positive stimulus to target users may negatively influence the emotions of unintended users (Feinstein et al., 2013). In studies on social media, the envy effect of social comparison has been widely observed (Appel et al., 2016; de Vries et al., 2018; Pera, 2018). Accordingly, the more positive emotional support provided to targeted support seekers, the worse the emotions of unintended recipients will be.

While both mechanisms may exist, their relative scale may be different on different web forums. In this study, our interest is an OHC for depression patients. As shown in previous research (O’Connor et al., 2002), depression patients tend to rank themselves lower in terms of social comparison, making it easier for them to feel worse off when observing others receiving help and causing them to sense a negative effect. Meanwhile, depression patients have stronger empathy for distress (O’Connor et al., 2002), leading to a lower ability to feel empathy for others’ improvement (due to emotional support). Thus, the positive effect on such individuals would likely be weaker. Therefore, we hypothesize:

H1: The sentiment of the emotional support content targeting other support seekers will negatively influence the emotion of the support seeker (reflected by expression sentiment).

Figure 2. Illustration of the Framework for the Study

![](/api/attachments/KXNUZDH3/fulltext/images/4ee16605d331977c1604955c2cfb56af0eda8c079fff6c28fc40dbf5ef2db227.jpg)

## Effect of Auxiliary Content

While emotional support is the main form of support that OHCs provide to depression patients, other content in OHCs, including informational support, off-track discussions, and noise, may also impact support seekers in that they also contain emotional expressions.

According to emotional contagion theory (Elfenbein, 2014), emotion spreads from source to recipient through the stimulus-registration-experience-expression process. The emotional expressions in auxiliary content could act as stimuli. When viewing such stimuli, support seekers may register and experience the emotion and form shared emotional stimulus contagion (Elfenbein, 2014). In such a mechanism, more positive stimuli will lead to a more positive impact on the user’s emotions. This effect has been identified by many previous studies (Bollen et al., 2011; Fowler & Christakis, 2008; Kramer et al., 2014).

Moreover, informational support in OHCs may direct readers to positive speculations for certain treatments. In Elfenbein’s framework, it could trigger a behavioral consequence, where patients imagine the outcomes of activities rather than the emotions of users. Such information may also positively affect patients’ health conditions by impacting their self-care activities (Wang et al., 2017). In both cases, the potential or concrete positive outcome may lead to recipients experiencing positive expectations and emotions, which would likely be reflected by the sentiments of their posts and expressions. Thus, we hypothesize:

H2: The sentiment of the auxiliary content will positively influence the emotion of the targeted support seeker (reflected by expression sentiment).

When unintended persons read auxiliary content, it may also lead to two competing mechanisms, as in off-target emotional support. On the one hand, patients may develop empathy for how the targeted user may feel. On the other hand, they may develop social comparison and envy about the positive outcome/emotion of the targeted users.

Note that the purpose of auxiliary content is different from emotional support and is often to provide information rather than care. Auxiliary content thus tends to be more objective and contains less sense of a target. According to appraisal theory (Lazarus, 1991), people’s appraisals appear in multiple steps, where the primary appraisal assesses relevance and congruence and the secondary appraisal involves coping. In particular, in the secondary appraisal, one needs to assess the people accountable for the situation. With fewer accountable targets in auxiliary content, the secondary appraisal may not be able to generate blame (Lazarus, 1991). In the context of potential social comparison caused by off-target content, recipients would be less likely to form a social comparison if the accountable target is not clear (as in auxiliary content). Previously, Argo et al. (2006) found that more objective information could lead to less social comparison. In the healthcare context, it is also found that objective comparison content (such as on procedures and coping) leads to a higher life quality, as compared with emotional comparison content (Buunk et al., 2012).

With a lower-level social comparison effect, the negative effect of off-target auxiliary content may not be stronger than the positive effect caused by empathy. In fact, with the two effects canceling each other out, it may not be possible to observe the emotional impact of off-target auxiliary content at all. Nevertheless, to conduct statistical tests on this aspect, we construct an alternative hypothesis on the existence of the relationship as follows:

H3-0: The sentiment of the auxiliary content targeting other support seekers will NOT influence the emotion of a support seeker (reflected by expression sentiment).

H3-1: The sentiment of the auxiliary content targeting other support seekers will negatively influence the emotion of a support seeker (reflected by expression sentiment).

## Preprocessing: Emotional Support Differentiation

To support our study, we need to differentiate between posts’ target and content type (emotional support or auxiliary content). In this study, we use the reply relationship in support replies to identify the conversation target. If a reply does not specify the reply target, we assume that it targets the original support seeker who started the thread since helping the support seeker is the main purpose of the forum. Compared to the conversation target, content type is tricky to differentiate. Due to the large volume of posts, it is impossible for human coders to manually screen all posts. Thus, we built a novel compound hierarchical attention networks model (C-HAN) to differentiate whether an OHC post constitutes emotional support for the conversation target.

## A Deep Learning Model

In the model, we aim to classify whether a focal post (such as post p in the middle of the thread in Figure 3) constitutes emotional support to the conversation target, i.e., the user it replies to. As illustrated in Figure 3, the post is actually a combination of two structures of web forum threads. On the one hand, there is a sequence presentation structure from the initial post to the last post, indicating the time each post is generated. On the other hand, there is a reply relationship between posts indicating the conversation logic. Our model leverages these two types of structures together with the thread’s initial post (which set the scene of the thread) in making sense of the textual features of posts. We briefly introduce the method below; further details are presented in the Appendix.

First, we used a bidirectional long short-term memory (BiLSTM) layer to process the initial post of the thread (as annotated by ① in Figure 3). BiLSTM is a classic text classification model that extends the LSTM model and models the bidirectional dependencies of words in a document (Zhou et al., 2016). We used it to capture the semantics of the support seekers’ help-seeking posts. Here, we enforced the length of each post to be 200 by truncating long posts and extending short posts with additional zeros for processing.

Second, we modeled the reply relationship of a post (as annotated by ② in Figure 3) using the hierarchical attention networks (HAN) model (Yang et al., 2016). Specifically, we combined the focal post, the post replied to by the focal post, and the first post reply to the focal post into a tuple and used HAN to model the combination of the three posts. In the process, the HAN model considers not only the interdependencies of words but also the interdependencies of posts. It also gives words different weights when modeling into a post and gives posts different weights when modeling the tuple, which helped us focus on important words and posts in the classification. If a post did not reply to any post or had no replies, the corresponding part was considered empty (while the conversation target was considered to be the original poster). Here we adopted the bidirectional gated recurrent unit (GRU) layer with 100 neurons in the HAN model.

Third, we modeled the sequential relationship of a post (as annotated by ③ in Figure 3) using the HAN model. Similar to modeling the reply relationship, we combined the focal post with the post before and after it into one tuple and applied the HAN model for processing. If the current post was the last post in the thread, the next post was considered empty.

After capturing the three parts of the information as three vectors, we used a concatenate layer to combine them and fed that to a dense layer to conduct the classification task.

## Classification Effectiveness

To train the machine learning model, we coded 901 randomly selected posts in threads initiated by support seekers as the gold standard. These posts either explicitly or implicitly replied to the support seeker in the conversation, which made them valid candidates for emotional support.

![](/api/attachments/KXNUZDH3/fulltext/images/16b7f88c3047009cb5aca583776634e5b16b57b907e98ae323153e6afbb25413.jpg)  
Figure 3. The Structure of the C-HAN Model for Emotional Support Identification

We hired 3 coders with master’s degrees in management to code the gold standard.<sup>2</sup> Then, the three coders coded the 901 posts independently. The Fleiss’s kappa of the three Ras’ coding was 0.750, which indicates substantial agreement. Posts with inconsistent coding were discussed by the coders to reach a consensus label. Eventually, 207 out of the 901 posts were labeled as emotional support. We used this dataset to evaluate the performance of the model.

To illustrate the effectiveness of our C-HAN model, we compared its performance with state-of-the-art baseline methods, including SVM (with linear kernel and radial kernel), decision tree, the BiLSTM model, and the graph convolutional network (GCN) model (Kipf & Welling, 2017). As explained in the Appendix, the baseline BiLSTM model was applied to the content of the focal post p. The GCN model further considered the reply relationship between posts to model p. For the input of these models, we conducted Chinese word segmentation on all the posts using an open-source toolkit, ICTCLAS 2016 (Zhang et al., 2003). For BiLSTM, GCN, and C-HAN, we conducted word embedding using a pretrained model as input, which captured the semantics and sequences of the (Chinese) words.

We conducted 10-fold cross-validation to evaluate the performance of the different models and conducted pair-wise ttests. We used the area under the curve (AUC), accuracy, precision, recall, and the F-measure as the evaluation metrics. Since our dataset is unbalanced, we reported the performance on both emotional support and auxiliary content labels, with emotional support as our focal label.

Table 2 reports the experimental performances and t-test results for the C-HAN model and the baselines. As shown, the C-HAN model achieved the highest AUC (82.9%) with a much more balanced performance than all baselines. It had about 60\~70% precision/recall/F-measure on classifying emotional support and about 80\~90% precision/recall/F-measure on classifying auxiliary content. Overall, it had 84.7% accuracy. Other models, in general, had an AUC 10-30% worse than our model and an accuracy of 5\~10% worse than our model. Moreover, they tended to have much worse precision/recall/F-measure on classifying emotional support, which is our focal task. It should be noted that the GCN model actually had higher accuracy than our model. However, this advantage was achieved at the cost of very low performance on emotional support (and very high performance on auxiliary content). The 20\~30% precision/recall/F-measure on emotional support indicates the failure of the algorithm in our specific context. Even though GCN is an effective model, its original form was unable to meet our needs in this research. We leave the further extension of GCN to address the emotional support classification task to future research.

Overall, our proposed C-HAN model achieved a more balanced and better performance on both emotional support and auxiliary content, as compared with the baseline methods. We believe that this is because it captures both the textual content and the relationships between posts. According to previous research (Deng et al., 2018), our text classification performance is sufficient to support a follow-up empirical study. We thus applied this model to all other posts in the dataset to prepare for the content-type dimension of our empirical study.

## Emotional Impact Assessment

## Econometric Models

To test our hypotheses, we built econometric models to model each support seeker’s emotional change. To ensure that the studied subjects were patients seeking help, instead of random visitors or support providers, we manually screened the initial posts of each thread to filter subjects for our study. Each support seeker i was able to post a series of posts (in different threads) over time. Aligning with previous research (Golder & Macy, 2011), we considered the sentiment of these posts to reflect support seekers’ emotions, which could be measured at the post level or aggregated to a daily level. In this study, we used this measure as the dependent variable.

Our dependent variable is the emotion of support seekers as measured by their posting sentiment (SENTIMENT). Following the common practice in previous studies (Chen et al., 2019), we built a daily-level panel data model on support seekers and examined how the support seeker’s posting sentiment on day t would be affected by the posts in their involved threads that were posted on day t-1. Since each support seeker made multiple posts per day, we averaged the sentiment of all the support seeker’s posts each day as the dependent variable. We specify a fixed-effect model on support seeker i’s posting sentiment on day $t , S E N T I M E N T _ { i , t } ,$ as:

$$
\begin{array}{r l} & S E N T I M E N T _ {i, t} = \alpha + \beta_ {1} S E N T I M E N T _ {i, t - 1} + X _ {i, t - 1} \Gamma + \\ & Z _ {i, t - 1} \phi + \varphi_ {t} + \eta_ {i} + \varepsilon_ {i, t}, \end{array}\tag{1}
$$

where $S E N T I M E N T _ { i , t - l }$ is the support seeker’s posting sentiment on day t-1, which accounts for the serial correlation of the variable. $X _ { i , t - I }$ represents the vector of independent variables (i.e., the four types of content in OHCs) on t-1 and $Z _ { i , t - I }$ denotes the vector of control variables, which will be elaborated later. <sub>t</sub> accounts for the time-variant effect, such as economic, social, and environmental factors, and the activity level of the forum (in terms of the number of supporters and support seekers on the market). <sub>i</sub> accounts for the heterogeneity of support seekers. $\varepsilon _ { i , t }$ denotes the random noise that cannot be explained by this model.

The variance of the independent variables of this model comes from whether a support seeker participates in (and potentially observes) a thread and whether the support seeker is the target of a conversation. Thus, the same web forum leads to different independent variables for different support seekers. Similar to previous studies on social media (Kramer et al., 2014) and online communities (Yan & Tan, 2014), the model relies on (some) support seekers observing the posts and being influenced. Since a user may leave a thread while others keep posting in the thread, we consider the last reply as the end of a user’s participation in a thread. The OHC we study notifies users when their participated threads are updated, increasing the user exposure in their participated threads.

Table 2. Emotional Support Classification Performance

<table><tr><td rowspan="2"></td><td rowspan="2">AUC</td><td rowspan="2">Accuracy</td><td colspan="3">Emotional support</td><td colspan="3">Auxiliary content</td></tr><tr><td>Precision</td><td>Recall</td><td>F1</td><td>Precision</td><td>Recall</td><td>F1</td></tr><tr><td>Decision tree</td><td>0.581***</td><td>0.776***</td><td>0.478***</td><td>0.467***</td><td>0.466***</td><td>0.848***</td><td>0.859***</td><td>0.853***</td></tr><tr><td>SVM (linear kernel)</td><td>0.690***</td><td>0.761***</td><td>0.477***</td><td>0.487***</td><td>0.463***</td><td>0.843***</td><td>0.842***</td><td>0.84***</td></tr><tr><td>SVM (radial kernel)</td><td>0.741**</td><td>0.811**</td><td>0.626</td><td>0.52***</td><td>0.533*</td><td>0.828**</td><td>0.848*</td><td>0.835*</td></tr><tr><td>BiLSTM</td><td>0.746***</td><td>0.800***</td><td>0.57**</td><td>0.568</td><td>0.588*</td><td>0.871</td><td>0.868**</td><td>0.869**</td></tr><tr><td>GCN</td><td>0.643***</td><td>0.929***</td><td>0.225***</td><td>0.345***</td><td>0.272***</td><td>0.972***</td><td>0.952**</td><td>0.965***</td></tr><tr><td>C-HAN (our model)</td><td>0.829</td><td>0.847</td><td>0.680</td><td>0.617</td><td>0.639</td><td>0.885</td><td>0.927</td><td>0.901</td></tr></table>

Note: Largest value in bold. p-value for comparison with the C-HAN model: \*\*\*<0.01; \*\*<0.05; \*<0.1

In the model, our independent variables are calculated on day t-1, and we inspected their impact on users’ behavior on day t. Since a support seeker on day t-1 cannot observe content posted on day t, the setup teases out the reverse causality issue. We also conducted mean centering on the variables to reduce the effect of nonessential multicollinearity.

## Independent Variables

Our independent variables are the sentiments of off-target emotional support (OT-EmoSupport), auxiliary content (AuxContent), and off-target auxiliary content (OT-AuxContent). We also controlled for the sentiment of emotional support (EmoSupport) since it is a main effect in OHCs. As mentioned, we identified target users based on reply relationships (if a post did not reply to any post, we considered it as a reply to the initial post of the thread) and employed a machine learning model to differentiate emotional support and auxiliary content. With these differentiations, we put each post into one of the four categories for each support seeker. We averaged the sentiment of the posts from each type of content to obtain four independent variables.

To calculate independent and dependent variables, we needed to calculate sentiment for each post. After conducting Chinese word segmentation using ICTCLAS 2016, we coded the segmented words using Chinese Linguistic Inquiry Word Count (LIWC http://cliwc.weebly.com), a widely used toolkit for psychometric analysis (Pennebaker et al., 2001). LIWC contains 7,444 Chinese words, which were classified into seven categories and 64 subcategories when we conducted the research. We used the positive and negative sentiment words in LIWC to assess emotion for each post. After labeling all sentiment words, we used the ratio of positive and negative terms, as in Kokkodis & Lappas (2020), as the emotional magnitude of each post— $\begin{array} { r } { e m o t i o n = l o g \frac { \% \ o f \ p o s i t i v e \_ e m o t i o n \ t e r m s + \varepsilon } { \% \ o f \ n e g a t i v e \_ e m o t i o n \ t e r m s + \varepsilon } } \end{array}$ , where ε = 0.001—to avoid zeros in the numerators and denominators; log transformation converted the ratio to a real number (positive or negative sentiment).

## Control Variables

In the study, we mainly focused on emotional contagion. We also controlled for a number of variables to rule out the confounding factors in the study.

Number of replies (NumReply): The user’s emotion may depend on the volume of support received. Thus, we controlled for the total number of posts within the threads in which the support seeker participated. This variable reflects the total amount of information consumed. As this is a count variable, logarithm transformation (LN(X+1)) was applied to the variable.

Informational Support (InfoSupport): The replies often contain health-related information, which is a form of informational support. To control for this effect, we used LIWC to calculate the proportion of health-related terms to measure the amount of informational support in each post. This measure is an average on all four kinds of posts the support seeker received.

Support-Seeking Content (SupportSeek): In addition to emotional support and auxiliary content, posts also contain support-seeking content. To address the influence of this content, we controlled for the sentiment of support-seeking posts for the threads that the focal user participated in.

Activeness (Active): Support seekers’ emotions may depend on their own activities. Thus, we controlled for the number of discussion threads that the support seeker participated in over the past 90 days. As a count variable, logarithm transformation (LN(X+1)) was applied to the variable.

Duration of Support Seeking (Duration): Patients’ emotions can evolve over time even if they do not receive any social support. To control for this effect, we calculated the number of days since a support seeker sought support in the OHC. If a support seeker’s posts were separated by more than three months, the posts were considered to belong to two separate support-seeking requests.

We controlled for the time effect in the model. Since we had a very long panel with sparse data and more than 50% of days only had 1 or 2 observations, we included week-fixed effects and fixed effects for the days of the week. We also controlled for major holidays (such as Chinese New Year, Valentine’s Day, Mid-Autumn Festival, Christmas, etc.) that may have affected users’ emotions.

## Addressing Endogeneity Concerns

Our identification relies on the possibility that a user can observe the posts forming independent variables. Even though our model followed a common practice to capture both exposure and influence (i.e., if users did not read the posts, we did not identify a significant relationship), there could still be a measurement error concern, i.e., whether the user read the posts, especially the posts not targeting them. We tackled this challenge using two approaches.

First, we developed instrumental variables (Bollen, 2012) on the measurement error caused by support seekers not reading off-target posts. Since our independent variables are support providers’ post sentiments, we chose their historical post sentiments (90 days before t-1) as the instrument. For example, the instrument variable for OT-EmoSupport is:

$$
I V \_ O T - E m o S u p p o r t _ {i, t} = \frac {1}{n} \sum_ {k = 1} ^ {n} 9 0 d a y \_ S e n t i m e n t _ {u s e r (k)},
$$

where k represents each of the n posts that form $O T _ { - }$ EmoSupport<sub>i,t,</sub> and user(k) represents the poster of k. Based on the individual support provider’s habit, the support provider’s post sentiment in forming OT-EmoSupport should have a correlation with their historical post sentiment. Thus, considering the existence of multiple, dynamic support providers’ posts every day, there should be a correlation between IV\_OT-EmoSupport and OT-EmoSupport. However, support providers’ historical posts should be independent of the support seeker’s emotion since it is unlikely that one would check multiple support seekers’ 90-day historical posts on a regular basis to form a daily-level emotion. The instrument could also alleviate the omitted variable bias (e.g., some posts influencing a support seeker were not included in $X _ { i , t - l } )$ ).

Second, we tried to strengthen the capture of support seekers viewing of posts. Specifically, we looked at the “replying” activities of support seekers. In the OHC we studied, all posts were presented sequentially in chronological order on the same page. If a user replied to a post, the user first had to observe a certain number of posts before viewing the repliedto post. Thus, as illustrated in Figure 4, we built a post-level model and studied how the posts before a reply j of support seeker i affected the sentiment of the reply, as follows:

$$
\begin{array}{l} S E N T I M E N T _ {i, j} = \alpha + \beta_ {1} S E N T I M E N T _ {i, j - 1} + X _ {i, j, j - 1} \Gamma + \\ Z _ {i, j - 1} \phi + \varphi_ {t} + \eta_ {i} + \varepsilon_ {i, t}, \end{array} \tag {2}
$$

where $S E N T I M E N T _ { i , j - l }$ and $S E N T I M E N T _ { i , j }$ are the sentiment of two subsequent posts to user i’s post in the thread and $S E N T I M E N T _ { i , j - l }$ captures serial correlation of the users posting sentiments. $X _ { i , j , j - I }$ are the independent variables calculated between the two posts that are replied to by j and j-1. (Note that these posts could appear before j and j-1.) Other variables are the same as in (1).

To strengthen identification, as illustrated in Figure 4, among the sequence of posts of user i, we only considered the subsequent reply pairs (i.e., j and j-1) appearing in the same thread, between which the support seeker did not make posts in any other threads. We also restricted the time between j and $j { - } 1$ , to make sure that the support seeker was consistently focusing on this thread. By doing so, we reduced the chance of the support seeker being influenced by posts in other threads, making the measurement of the support seeker’s posting sentiment, SENTIMENT<sub>i,j</sub>, more accurate. Moreover, to improve the possibility of the support seeker’s observation, we restricted the independent variable calculation to a certain number of posts close to the post replied to by j in our robustness check.

Since the posting times of support seekers are stochastic, Equation (2) is not a classic panel data model (to be more specific, the data is an irregularly spaced panel, see Millimet & McDonough, 2017). Due to the difficulty in estimation, we set up Equation (2) on pairs on replies (j and j-1) and controlled for time- and user-fixed effects in the model.

## Results

## Summary Statistics

We collected the data of the MDD group from its founding date to January 6, 2015, comprising 3,565 threads and 47,247 posts generated by 5,013 users. Since the platform experienced a major update (adding the reply-to function) on December 30, 2011, we only used the data after this date as our dataset, which contains 3,323 threads (44,478 posts) by 4,692 users. As shown in Table 3, the characteristics of the MDD group activities remained consistent for the entire time scope, including after the website update.

![](/api/attachments/KXNUZDH3/fulltext/images/854ebba28424d5fc100ed813dba9dca89001f7d7e5e85e670819a981065954e2.jpg)  
Figure 4. Illustration of the Empirical Setup on View before Reply

<table><tr><td colspan="7">Table 3. Summary of the MDD Group Activities</td></tr><tr><td></td><td colspan="3">All MDD data</td><td colspan="3">Data after 2011</td></tr><tr><td></td><td>N</td><td>Mean</td><td>Std. dev.</td><td>N</td><td>Mean</td><td>Std. dev.</td></tr><tr><td># User per thread</td><td>3,565</td><td>5.945</td><td>9.982</td><td>3,323</td><td>5.932</td><td>9.756</td></tr><tr><td># Post per thread</td><td>3,565</td><td>13.304</td><td>29.491</td><td>3,323</td><td>13.385</td><td>29.480</td></tr><tr><td># Word per post</td><td>47,247</td><td>44.170</td><td>255.066</td><td>44,478</td><td>44.028</td><td>260.052</td></tr><tr><td>Post sentiment</td><td>47,247</td><td>0.144</td><td>4.322</td><td>44,478</td><td>0.160</td><td>4.328</td></tr></table>

The mean post number for each thread is 13.3. The average number of users for each thread is 5.9. The average number of words per post is 44. The mean emotion of posts slightly improves from 0.144 to 0.16 after 2011, which we think may be due to the development of group goodwill to provide help. We believe that using the data after 2011 did not affect the validity of our findings and also ruled out the impact of the website update.

For the econometric analysis, we first ensured that the studied subjects are patients who are seeking help. We recruited 3 coders and manually screened the initial posts to filter out the noise, advertisements, announcements, and informational posts. The Fleiss’s kappa of the three coders’ coding is 0.714, indicating a substantial agreement level. Moreover, we only used fully agreed-upon threads to further improve data validity. Eventually, the coders identified 1,489 discussion threads that were initiated by 1,098 MDD users seeking social support.

Figure 5 reports the users’ distribution on activity days and the number of posts per day. As can be seen, most support seekers remained on the OHC for less than 10 days and posted less than 20 posts. There were about 10 times more other users than support seekers in the population, with the majority having a similar number of posts. No user stayed on the platform for more than 200 days or posted more than 1,000 posts. Long-term OHC users do not represent regular support seekers. They may be dedicated to providing help or may be helpers converted from support seekers. Thus, we only examined the first 30 days of support seekers’ activities in our research.

We built the deep learning model using a gold standard coded from a random sample of the threads initiated by support seekers. After applying the deep learning model to the entire dataset, we identified 7,300 emotional support posts. The other posts are considered to be auxiliary content. As shown in Figure 6, while both types of content contain positive and negative sentiments, the sentiment distribution of auxiliary content is more balanced, while the emotional support posts contain more positive words. Figure 6 shows the monthly average sentiment of the two types of content. As we can see, even though the auxiliary content is not intended to make an emotional impact, there exist fluctuations of expression sentiments, which could have affected users’ emotions.

![](/api/attachments/KXNUZDH3/fulltext/images/183fb6f927bb7b07b005c207cbc425a7f60998d5691bdbe743f85540ad0fb6ee.jpg)  
Figure 5. Activity Level of Support Seekers vs. Other Users

![](/api/attachments/KXNUZDH3/fulltext/images/e570223e65d1dd174b686973dee55d576150b520eaff5c8ec7d34ebd5d14ad97.jpg)

![](/api/attachments/KXNUZDH3/fulltext/images/fb66f70822e363e85a2fdde74d7d57f120b2aee2b1218a5e5773f702ccdeaef3.jpg)

![](/api/attachments/KXNUZDH3/fulltext/images/6c46bbedbd6b7f504b72090a196b6cad7fc4a3ad7f788c3edfc1708830fce42e.jpg)  
Figure 6. Sentiment Level of Emotional Support vs. Auxiliary Content

After data cleaning, our dataset contained 1,022 support seekers. Our classifier identified 6,883 replies as emotional support for these users, and the remaining 37,595 replies were considered to be auxiliary content. These data are scattered over 2,379 calendar days. Table 4 provides the summary statistics. On average, the sentiment of support seekers expressions (SENTIMENT) is close to neutral (-0.024). The sentiments of emotional support content (EmoSupport, OT-EmoSupport) are positive (0.6 and 0.4). The sentiments of auxiliary content (AuxContent, OT-AuxContent) are more objective (0.06 and -0.001, respectively).

## Testing Hypotheses on Emotional Effects

Table 5 reports the findings of our model. Columns 1 and 2 present the results of the main model with fixed and random effects. The Hausman test (Hausman, 1978) shows that the fixed-effect model is more consistent than the random-effect model (Prob > chi<sup>2</sup> = 0.0000). So, we chose the fixed-effect model as the basis for subsequent analysis. Column 3 shows the results with instrumental variables on off-target emotional support and off-target auxiliary content. Our instrumental variables are exogenous (with a Durbin chi-squared value of 2.4752 with p-value = 0.2901 and a Wu-Hausman F-value of 1.1340 with p-value=0.3200) and strong (with a minimum eigenvalue statistic of 8.40191, while 10% maximal IV size = 7.03), and thus can be used to deal with the endogeneity issue (with a chi-squared value of 427.59 and p-value = 0.000). Column 4 shows the results based on the “replying” activities of support seekers. Since it is on two subsequent replies after initial support, the control variable SupportSeek is omitted.

As shown in Table 5, the findings of the four models are generally consistent. The results do show that depression patients’ emotions are positively associated with the sentiment of the emotional support they received.

<table><tr><td colspan="6">Table 4. Summary Statistics of the Data</td></tr><tr><td></td><td>N</td><td>Mean</td><td>Std. dev.</td><td>Max</td><td>Min</td></tr><tr><td>SENTIMENT</td><td>1,994</td><td>-0.0249</td><td>3.1398</td><td>9.2104</td><td>-8.5174</td></tr><tr><td>EmoSupport</td><td>1,994</td><td>0.5983</td><td>2.2671</td><td>9.2104</td><td>-8.5174</td></tr><tr><td>AuxContent</td><td>1,994</td><td>0.0668</td><td>2.7364</td><td>8.5174</td><td>-9.2104</td></tr><tr><td>OT-EmoSupport</td><td>1,994</td><td>0.4401</td><td>1.7255</td><td>9.2104</td><td>-7.8244</td></tr><tr><td>OT-AuxContent</td><td>1,994</td><td>-0.0012</td><td>1.8311</td><td>8.6997</td><td>-8.4059</td></tr><tr><td>NumReply</td><td>1,994</td><td>6.5527</td><td>11.9205</td><td>220</td><td>0</td></tr><tr><td>InfoSupport</td><td>1,994</td><td>0.4023</td><td>1.2405</td><td>16.6667</td><td>0</td></tr><tr><td>SupportSeek</td><td>1,994</td><td>-0.0705</td><td>0.7992</td><td>8.5174</td><td>-7.7446</td></tr><tr><td>Active</td><td>1,994</td><td>13.6680</td><td>21.3619</td><td>160</td><td>0</td></tr><tr><td>Duration</td><td>1,994</td><td>3.6339</td><td>6.4500</td><td>29</td><td>0</td></tr></table>

Table 5. Regression Results for Testing Hypotheses

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td></td><td>Fixed effect</td><td>Random effect</td><td>Instrumental variable</td><td>Between-reply</td></tr><tr><td> $SENTIMENT_{i,t-1}$ </td><td>-0.143***(-4.251)</td><td>-0.007(-0.228)</td><td>0.087*(2.206)</td><td>-0.128***(-4.599)</td></tr><tr><td> $EmoSupport_{i,t-1}$ </td><td>0.067#(1.775)</td><td>0.088*(2.515)</td><td>0.113*(2.573)</td><td>0.226***(4.532)</td></tr><tr><td> $AuxContent_{i,t-1}$ </td><td>0.072**(2.614)</td><td>0.066*(2.516)</td><td>0.059#(1.657)</td><td>0.082**(2.666)</td></tr><tr><td> $OT-EmoSupport_{i,t-1}$ </td><td>-0.094*(-2.176)</td><td>-0.066#(-1.771)</td><td>-1.672#(-1.710)</td><td>-0.216#(-1.750)</td></tr><tr><td> $OT-AuxContent_{i,t-1}$ </td><td>0.010(0.200)</td><td>-0.018(-0.399)</td><td>-0.221(-0.601)</td><td>0.003(0.040)</td></tr><tr><td> $NumReply_{i,t-1}$ </td><td>0.151(1.463)</td><td>0.209**(2.398)</td><td>0.919*(1.993)</td><td>0.268(0.796)</td></tr><tr><td> $InfoSupport_{i,t-1}$ </td><td>-0.020(-0.228)</td><td>-0.022(-0.328)</td><td>-0.055(-0.630)</td><td>-0.020***(-2.803)</td></tr><tr><td> $SupportSeek_{i,t-1}$ </td><td>-0.073(-0.718)</td><td>-0.071(-0.765)</td><td>-0.081(-0.660)</td><td></td></tr><tr><td> $Active_{i,t-1}$ </td><td>0.224(1.003)</td><td>-0.027(-0.240)</td><td>0.025(0.199)</td><td>0.062*(1.996)</td></tr><tr><td> $Duration_{i,t-1}$ </td><td>0.007(0.344)</td><td>0.004(0.241)</td><td>0.016(0.917)</td><td>-0.060(-1.244)</td></tr><tr><td>Week</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Day of the week</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Holiday</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td># observations</td><td>1994</td><td>1994</td><td>1994</td><td>2937</td></tr><tr><td># subjects</td><td>469</td><td>469</td><td>469</td><td>433</td></tr><tr><td>R-squared</td><td>0.151</td><td>0.136</td><td>-0.010</td><td>0.287</td></tr></table>

Note: t-statistic in parentheses; <sup>#</sup>p < 0.10; \*p < 0.05; \*\*p < 0.01, \*\*\*p < 0.005

While the effect of emotional support is consistent with our intuition, the effect of off-target emotional support is more interesting. We find a negative impact of off-target emotional support on the emotional state of focal users, which has a pvalue of 0.030 in the fixed-effect model and 0.087 and 0.081 in the models with instrumental variables and the reply setup. H1 is generally supported in the different models. Our results show that after seeing other people receiving help, depression patients actually feel worse. The coefficient is about -0.094 in the fixed-effect model, which is at the same scale as the main effect of emotional support. In other words, if one helps a support seeker on the platform by providing positive emotional support, one may, at the same time, generate a similar level of hurt to other support seekers. This creates a paradox for designing intervention strategies in online communities, which we will discuss in later sections.

Second, we find that the impact of auxiliary content is also positive and significant. H2 is supported. In other words, even if the intention is not to provide emotional support, support providers’ positive expressions still help. The coefficient is about 0.072 in the fixed-effect model, which is slightly smaller than the effect of emotional support content.

The results also show that off-target auxiliary content does not have a significant effect; thus, we are unable to reject the null hypothesis H3-0. It shows that the social comparison effect of off-target auxiliary content is less obvious compared with offtarget emotional support.

## Robustness Checks

We conducted multiple robustness checks of the results. First, in Column 1 of Table 6, we include the second day of public holidays as additional control variables. This operation addresses the potential lag effect of holidays that last more than one day. The coefficients of this model are consistent with our main model.

In our main model, we built the panel according to calendar days. However, as shown in Figure A5 in the Appendix, users are still very active after midnight, with the lowest activity level at about 6 am. Thus, setting the time period based on calendar days could have led to observing content posted before 12 am influencing emotion after 12 am. To control for users who stayed past midnight, we set the analysis period to 6 am each day. As shown in Column 2 of Table 6, the results remain consistent and significant.

Moreover, most support seekers stayed on the platform only for a few days. Those who remained on the platform for a long time may have had different roles and behaviors from support seekers new to the platform. We created a robustness check by only retaining the first five days’ activities of each support seeker in the model. As shown in Column 3 of Table 6, the results are generally consistent with the main model.

We also conducted robustness checks at the post level (Equation 2). First, we limited the posts in the between-reply window and considered posts closer to when the focal user’s reply was viewed. In Columns 1 and 2 of Table 7, we limit that window to 10 and 20 posts, respectively. As shown in the table, the results are consistent under this manipulation.

Second, we obtained user access logs of the webpages after July 2013.<sup>3</sup> In Columns 3 and 4 of Table 7, we enforce the post-level model (Equation 2) to further confirm that support seekers were reading posts between their replies. Specifically, we assumed that support seekers who opened the thread (according to the access log) between the two replies paid more attention to it than others. Each time support seekers open a thread, they might read some posts at the end of the thread (until they find something they want to reply to). For such support seekers, the likelihood that they will read the last 10 to 20 posts (as specified in the post-level model) is higher. As shown in Table 7, the results are consistent with the main model.

Overall, we summarize our hypotheses testing results in Table 8. We find that emotional support negatively impacts the expression sentiment of support seekers who are not the target. We also find that auxiliary content has a positive impact on target support seekers and a nonsignificant impact on non-target users.

## Mechanisms

## Independence between On-Target and Off-Target Content

In the study, we found that on-target content and off-target content had opposite effects on users, which we argue is due to different mechanisms. A natural question is whether the two types of content have interaction effects with each other. Columns 1 and 2 in Table 9 report the results, adding interaction variables between on-target and off-target support. As shown, on-target and off-target content do not have significant interaction effects, demonstrating that the two types of content do not intervene in each other’s impact on users. We determined that the scale of the negative effect of off-target emotional support does not vary according to the emotional support received by the support seeker. These two analyses provide clear evidence that social comparison exists independently from the emotional support effect in OHCs.

<table><tr><td colspan="4">Table 6. Robustness Checks on Observation Time Variants</td></tr><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>After holiday effect</td><td>Midnight effect</td><td>Early period effect</td></tr><tr><td> $SENTIMENT_{i,t-1}$ </td><td>-0.145***(-4.210)</td><td>-0.143***(-4.252)</td><td>-0.056(-1.459)</td></tr><tr><td> $EmoSupport_{i,t-1}$ </td><td>0.067# (1.750)</td><td>0.067# (1.779)</td><td>0.104***(2.838)</td></tr><tr><td> $AuxContent_{i,t-1}$ </td><td>0.067*(2.414)</td><td>0.072**(2.616)</td><td>0.086***(2.734)</td></tr><tr><td> $OT-EmoSupport_{i,t-1}$ </td><td>-0.104*(-2.395)</td><td>-0.094*(-2.165)</td><td>-0.108*(-2.091)</td></tr><tr><td> $OT-AuxContent_{i,t-1}$ </td><td>-0.000(-0.007)</td><td>0.005(0.096)</td><td>-0.054(-1.011)</td></tr><tr><td> $NumReply_{i,t-1}$ </td><td>0.153(1.442)</td><td>0.151(1.457)</td><td>0.253*(2.374)</td></tr><tr><td> $InfoSupport_{i,t-1}$ </td><td>-0.031(-0.343)</td><td>-0.022(-0.251)</td><td>-0.046(-0.640)</td></tr><tr><td> $SupportSeek_{i,t-1}$ </td><td>-0.058(-0.557)</td><td>-0.072(-0.691)</td><td>-0.023(-0.231)</td></tr><tr><td> $Active_{i,t-1}$ </td><td>0.240(1.054)</td><td>0.226(1.101)</td><td>-0.041(-0.301)</td></tr><tr><td> $Duration_{i,t-1}$ </td><td>0.008(0.384)</td><td>0.007(0.343)</td><td>-0.176*(-2.162)</td></tr><tr><td>Fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td># observations</td><td>1994</td><td>1994</td><td>1526</td></tr><tr><td># subjects</td><td>469</td><td>469</td><td>442</td></tr><tr><td>R-squared</td><td>0.158</td><td>0.151</td><td>0.253</td></tr></table>

Note: t-statistic in parentheses; <sup>#</sup>p < 0.10; \*p < 0.05; \*\*p < 0.01, \*\*\*p < 0.005

<table><tr><td colspan="5">Table 7. Robustness Check on Post-Level Models</td></tr><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>All users10 posts</td><td>All users20 posts</td><td>Users in log10 posts</td><td>Users in log20 posts</td></tr><tr><td> $SENTIMENT_{i,t-1}$ </td><td>-0.128***(-4.593)</td><td>-0.128***(-4.600)</td><td>-0.046#(-1.811)</td><td>-0.046#(-1.811)</td></tr><tr><td> $EmoSupport_{i,t-1}$ </td><td>0.133***(4.444)</td><td>0.133***(4.430)</td><td>0.453**(2.800)</td><td>0.453**(2.800)</td></tr><tr><td> $AuxContent_{i,t-1}$ </td><td>0.047*(2.566)</td><td>0.048**(2.596)</td><td>0.163#(1.671)</td><td>0.163#(1.671)</td></tr><tr><td> $OT-EmoSupport_{i,t-1}$ </td><td>-0.155*(-1.993)</td><td>-0.138#(-1.843)</td><td>-0.275*(-2.119)</td><td>-0.275*(-2.119)</td></tr><tr><td> $OT-AuxContent_{i,t-1}$ </td><td>-0.004(-0.080)</td><td>0.006(0.130)</td><td>-0.592*(-2.170)</td><td>-0.592*(-2.170)</td></tr><tr><td> $NumReply_{i,t-1}$ </td><td>0.221(0.587)</td><td>0.212(0.598)</td><td>-0.033(-0.053)</td><td>-0.033(-0.053)</td></tr><tr><td> $InfoSupport_{i,t-1}$ </td><td>-0.018(-1.016)</td><td>-0.021(-1.180)</td><td>0.029(0.518)</td><td>0.029(0.518)</td></tr><tr><td> $Active_{i,t-1}$ </td><td>0.057#(1.810)</td><td>0.057#(1.829)</td><td>0.016(0.492)</td><td>0.016(0.492)</td></tr><tr><td> $Duration_{i,t-1}$ </td><td>-0.061(-1.258)</td><td>-0.062(-1.272)</td><td>0.034(0.782)</td><td>0.034(0.782)</td></tr><tr><td>Fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td># observations</td><td>2937</td><td>2937</td><td>2232</td><td>2232</td></tr><tr><td># subjects</td><td>433</td><td>433</td><td>290</td><td>290</td></tr><tr><td>R-squared</td><td>0.285</td><td>0.285</td><td>0.062</td><td>0.062</td></tr></table>

Note: t-statistic in parentheses; <sup>#</sup>p < 0.10; \*p < 0.05; \*\*p < 0.01, \*\*\*p < 0.005

<table><tr><td colspan="5">Table 8. Summary of Hypotheses Testing Results</td></tr><tr><td>ID</td><td>Content type</td><td>Recipient</td><td>Hypothesized emotional impact</td><td>Finding</td></tr><tr><td>H1</td><td>Emotional support</td><td>Non-target support seeker</td><td>Negative impact on the expression sentiment</td><td>Supported</td></tr><tr><td>H2</td><td>Auxiliary content</td><td>Targeted support seeker</td><td>Positive impact on the expression sentiment</td><td>Supported</td></tr><tr><td>H3-0</td><td rowspan="2">Auxiliary content</td><td rowspan="2">Non-target support seeker</td><td>No impact on the expression sentiment</td><td>Supported</td></tr><tr><td>H3-1</td><td>Negative impact on the expression sentiment</td><td>Not supported</td></tr></table>

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td></td><td>Interaction</td><td>Interaction</td><td>Before/after support</td><td>Initial emotion &lt; 0</td><td>Initial emotion ≥ 0</td></tr><tr><td> $SENTIMENT_{i,t-1}$ </td><td>-0.143***(-4.225)</td><td>-0.143***(-4.251)</td><td>-0.143***(-4.216)</td><td>-0.224***(-4.131)</td><td>-0.148***(-3.031)</td></tr><tr><td> $EmoSupport_{i,t-1}$ </td><td>0.066# (1.759)</td><td>0.069# (1.821)</td><td>0.070# (1.844)</td><td>0.148** (2.585)</td><td>-0.038 (-0.778)</td></tr><tr><td> $AuxContent_{i,t-1}$ </td><td>0.072**(2.616)</td><td>0.071*(2.581)</td><td>0.071*(2.580)</td><td>-0.007 (-0.146)</td><td>0.102***(2.859)</td></tr><tr><td> $OT-EmoSupport_{i,t-1}$ </td><td>-0.096*(-2.082)</td><td>-0.094*(-2.165)</td><td></td><td>-0.249**(-2.615)</td><td>-0.040(-0.860)</td></tr><tr><td> $OT-AuxContent_{i,t-1}$ </td><td>0.010 (0.203)</td><td>0.006 (0.138)</td><td>0.009 (0.193)</td><td>-0.009 (-0.093)</td><td>0.018 (0.288)</td></tr><tr><td> $EmoSupport_{i,t-1}$ *OT-EmoSupport i,t-1</td><td>0.007 (0.359)</td><td></td><td></td><td></td><td></td></tr><tr><td> $AuxContent_{i,t-1}$ *OT-AuxContent i,t-1</td><td></td><td>0.006 (0.331)</td><td></td><td></td><td></td></tr><tr><td> $OT-EmoSupport Before_{i,t-1}$ </td><td></td><td></td><td>-0.093# (-1.772)</td><td></td><td></td></tr><tr><td> $OT-EmoSupport After_{i,t-1}$ </td><td></td><td></td><td>-0.006 (-0.077)</td><td></td><td></td></tr><tr><td> $NumReply_{i,t-1}$ </td><td>0.157 (1.464)</td><td>0.152 (1.475)</td><td>0.131 (1.288)</td><td>0.165 (1.050)</td><td>0.184 (1.251)</td></tr><tr><td> $InfoSupport_{i,t-1}$ </td><td>-0.021 (-0.237)</td><td>-0.021 (-0.237)</td><td>-0.013 (0.146)</td><td>0.017 (0.118)</td><td>-0.108 (-0.798)</td></tr><tr><td> $SupportSeek_{i,t-1}$ </td><td>-0.073 (-0.709)</td><td>-0.074 (-0.722)</td><td>-0.072 (-0.705)</td><td>0.011 (0.065)</td><td>-0.116 (-0.976)</td></tr><tr><td> $Active_{i,t-1}$ </td><td>0.229 (1.007)</td><td>0.214 (0.946)</td><td>0.223 (0.991)</td><td>0.477 (0.859)</td><td>0.418 (1.576)</td></tr><tr><td> $Duration_{i,t-1}$ </td><td>0.007 (0.334)</td><td>0.007 (0.343)</td><td>0.007 (0.352)</td><td>-0.020 (-0.503)</td><td>-0.010 (-0.405)</td></tr><tr><td>Fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td># observations</td><td>1994</td><td>1994</td><td>1994</td><td>829</td><td>1165</td></tr><tr><td># subjects</td><td>469</td><td>469</td><td>469</td><td>235</td><td>234</td></tr><tr><td>R-squared</td><td>0.151</td><td>0.151</td><td>0.150</td><td>0.319</td><td>0.214</td></tr></table>

Note: t-statistic in parentheses; <sup>#</sup> p < 0.10; \* p < 0.05; \*\* p < 0.01, \*\*\* p < 0.005

## Social Comparison: Support Before/After Comparison

We argue social comparison may be the cause of the negative effect of off-target emotional support. To further validate this argument, we separated off-target emotional support each day into two types: that happening before emotional support is received (OT-EmoSupport Before<sub>i,t-1</sub>) and that happening after emotional support is received (OT-EmoSupport After<sub>i,t-1</sub>), depending on whether the focal users received some emotional support before or after making the first reply on day t-1. If on day t-1 the focal user did not receive any emotional support, all off-target emotional support is categorized as OT-EmoSupport Before<sub>i,t-1</sub>.

Column 3 of Table 9 reports the results of this analysis. As shown, if the focal user did not receive any emotional support on a particular day, off-target emotional support shows a strong negative effect. But if the focal user did receive emotional support, off-target emotional support is not significant. We argue this is because emotional support would make the focal user feel higher in position in comparison with others, while not receiving emotional support would make the focal user feel bad when seeing others being supported. This evidence indicates that social comparison is one potential reason for the negative effect of off-target emotional support.

## Social Comparison: Extent of Depression.

We argue the nature of the OHC (i.e., major depressive disorder) intensifies the negative effects of off-target emotional support by causing patients to place themselves lower in social comparisons. To explore this mechanism, we differentiated users according to their emotion reflected in their original support-seeking posts, which reflects the extent of patients’ depression. As shown in Columns 4 and 5 of Table 9, for users who were initially severely depressed (whose initial posts expressed negative sentiments) off-target emotional support had a strong negative impact. However, for support seekers who were initially in a better condition (whose initial posts expressed neutral or positive sentiments), offtarget emotional support did not have a significant negative effect. While our dataset cannot support further analysis, this result shows that depressed patients in poor condition, who tend to make stronger social comparisons, would experience a stronger negative impact from off-target emotional support.

## Discussion

## The Need for Content Differentiation

One major part of our approach is the differentiation of emotional support and auxiliary content. To answer the question of whether such a manipulation is necessary, we conducted a counterfactual analysis. As shown in Table 10, if we do not differentiate emotional support from emotional contagion, we can only observe a positive impact for the ontarget content; we would not be able to observe the negative impact of off-target content. This could be the reason that previous research only identifies the positive effect of emotional support and largely ignores the negative effect of off-target emotional support.

To further understand the classified emotional and auxiliary content, we inspected their topics using the LDA model (Blei et al., 2003). After determining the number of clusters using the UMass coherence measure (Mimno et al., 2011), we report three major topics for each type of content in Figure A6 in the Appendix. As shown in the emotional support content, the discussions contain direct comfort, references to parents and friends, therapy suggestions, and so forth, which are more subjective. The auxiliary content text is more objective and includes discussions related to symptoms, external factors related to depressive emotions, and academic discussion. Overall, these analyses show that differentiating online support content is meaningful and critical to understanding OHC content’s impact on support seekers.

## Toward a Proper Intervention

While the above analysis deepens the understanding of OHCs impact on depression users, it also generates a paradox: providing stronger emotional support to help a user may hurt other users on the platform. One approach to tackle this problem would be to take the emotional support to a private channel so that it cannot be observed by other support seekers. However, this practice is not always plausible due to the sensitivity of support seekers. It also goes against the original intention of open online communities. To develop proper intervention through OHCs, we explore the impact of aspects other than expression sentiment on support seekers.

## Support Volume and Length

In light of Chen et al. (2019), we inspect the effects of support style in terms of volume and length after controlling for support sentiment. Column 1 of Table 11 shows that the support volume of emotional support does have a significant positive impact on the targeted support seeker’s emotions. Since the effect of off-target emotional support volume is not significant, it is possible to provide more (instead of more positive) emotional support for targeted users.

Column 2 of Table 11 shows the effect of emotional support length (i.e., average characters of each post). As we can see, while the length of emotional support does not help support seekers, the length of off-target emotional support has a positive effect on support seekers’ emotions. In other words, providing longer (i.e., wordier) emotional support does not help our target but will benefit the other unintended audiences.

Combining the above two arguments, if we increase the volume of emotional support or the length of emotional support, we can improve either the emotions of targeted support seekers or those of the unintended audience, which is better than improving emotional support sentiment.

<table><tr><td colspan="4">Table 10. The Need to Differentiate Emotional Support and Auxiliary Content</td></tr><tr><td rowspan="2"></td><td colspan="2">(1)</td><td>(2)</td></tr><tr><td colspan="2">Differentiate</td><td>Do not differentiate</td></tr><tr><td> $SENTIMENT_{i,t-1}$ </td><td colspan="2">-0.143***(-4.251)</td><td>-0.145***(-4.280)</td></tr><tr><td> $EmoSupport_{i,t-1}$ </td><td>0.067#(1.775)</td><td rowspan="2">\}</td><td rowspan="2">0.090***(3.306)</td></tr><tr><td> $AuxContent_{i,t-1}$ </td><td>0.072**(2.614)</td></tr><tr><td> $OT-EmoSupport_{i,t-1}$ </td><td>-0.094*(-2.176)</td><td rowspan="2">\}</td><td rowspan="2">-0.029(-0.646)</td></tr><tr><td> $OT-AuxContent_{i,t-1}$ </td><td>0.010(0.200)</td></tr><tr><td> $NumReply_{i,t-1}$ </td><td colspan="2">0.151(1.463)</td><td>0.126(1.228)</td></tr><tr><td> $InfoSupport_{i,t-1}$ </td><td colspan="2">-0.020(-0.228)</td><td>0.020(0.687)</td></tr><tr><td> $SupportSeek_{i,t-1}$ </td><td colspan="2">-0.073(-0.718)</td><td></td></tr><tr><td> $Active_{i,t-1}$ </td><td colspan="2">0.224(1.003)</td><td>0.213(0.964)</td></tr><tr><td> $Duration_{i,t-1}$ </td><td colspan="2">0.007(0.344)</td><td>0.009(0.437)</td></tr><tr><td>Fixed effect</td><td colspan="2">Yes</td><td>Yes</td></tr><tr><td># Observations</td><td colspan="2">1994</td><td>1994</td></tr><tr><td># Subjects</td><td colspan="2">469</td><td>469</td></tr><tr><td>R-squared</td><td colspan="2">0.151</td><td>0.149</td></tr></table>

Note: t-statistic in parentheses; <sup>#</sup>p < 0.10; \*p < 0.05; \*\*p < 0.01, \*\*\*p < 0.005

<table><tr><td colspan="4">Table 11. Volume and Length vs. Sentiment</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>Reply characteristic →</td><td>Volume</td><td>Length</td><td># Replier</td></tr><tr><td> $SENTIMENT_{i,t-1}$ </td><td>-0.148***(-4.296)</td><td>-0.146***(-4.272)</td><td>-0.149***(-4.344)</td></tr><tr><td>Characteristic of  $EmoSupport_{i,t-1}$ </td><td>0.436# (1.891)</td><td>0.001 (0.636)</td><td>0.332**(2.425)</td></tr><tr><td>Characteristic of  $AuxContent_{i,t-1}$ </td><td>0.072 (0.373)</td><td>0.005*(2.215)</td><td>-0.008(-0.112)</td></tr><tr><td>Characteristic of OT-EmoSupport $_{i,t-1}$ </td><td>-0.155(-0.594)</td><td>0.003# (1.833)</td><td>-0.108(-0.842)</td></tr><tr><td>Characteristic of OT-AuxContent $_{i,t-1}$ </td><td>0.047 (0.207)</td><td>-0.001(-0.565)</td><td>0.016(0.272)</td></tr><tr><td>Vol Per Replier of  $EmoSupport_{i,t-1}$ </td><td></td><td></td><td>-0.108(-0.592)</td></tr><tr><td>Vol Per Replier of  $AuxContent_{i,t-1}$ </td><td></td><td></td><td>0.002(0.037)</td></tr><tr><td>Vol Per Replier of OT-EmoSupport $_{i,t-1}$ </td><td></td><td></td><td>0.056(0.424)</td></tr><tr><td>Vol Per Replier of OT-AuxContent $_{i,t-1}$ </td><td></td><td></td><td>-0.091(-1.530)</td></tr><tr><td> $EmoSupport_{i,t-1}$ </td><td>0.046 (1.174)</td><td>0.063# (1.661)</td><td>0.047(1.194)</td></tr><tr><td> $AuxContent_{i,t-1}$ </td><td>0.067*(2.397)</td><td>0.067*(2.423)</td><td>0.069*(2.414)</td></tr><tr><td>OT-EmoSupport $_{i,t-1}$ </td><td>-0.087# (-1.675)</td><td>-0.103*(-2.370)</td><td>-0.089#(-1.760)</td></tr><tr><td> $OT-AuxContent_{i,t-1}$ </td><td>0.000(0.003)</td><td>-0.003(-0.060)</td><td>0.002(0.036)</td></tr><tr><td> $NumReply_{i,t-1}$ </td><td>0.057(0.190)</td><td>0.084(0.776)</td><td>0.183(0.786)</td></tr><tr><td> $InfoSupport_{i,t-1}$ </td><td>-0.106(-1.053)</td><td>-0.044(-0.485)</td><td>-0.096(-0.988)</td></tr><tr><td> $SupportSeek_{i,t-1}$ </td><td>-0.071(-0.663)</td><td>-0.057(-0.544)</td><td>-0.071(-0.648)</td></tr><tr><td> $Active_{i,t-1}$ </td><td>0.244(1.069)</td><td>0.234(1.014)</td><td>0.228(1.00)</td></tr><tr><td> $Duration_{i,t-1}$ </td><td>0.010(0.467)</td><td>0.010(0.474)</td><td>0.010(0.448)</td></tr><tr><td>Fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td># Observations</td><td>1994</td><td>1994</td><td>1994</td></tr><tr><td># Subjects</td><td>469</td><td>469</td><td>469</td></tr><tr><td>R-squared</td><td>0.160</td><td>0.162</td><td>0.162</td></tr></table>

Note: t-statistic in parentheses; <sup>#</sup>p < 0.10; \*p < 0.05; \*\*p < 0.01, \*\*\*p < 0.005

## Repeated Support and Number of Support Providers

Another aspect we are interested in is whether it is better to provide multiple support replies or to involve multiple people in the support process. In Table 11, we differentiate the number of repliers and the volume of replies per replier for the four types of content. As we can see, while more repliers providing emotional support benefits targeted users, having more replies per replier does not change support seekers emotions. Thus, it would be better to form a team to help depression patients online.

## Implications

The econometric analysis shows that the effect of off-target emotional support has a negative impact on support seekers. This study offers several important implications.

From a theoretical perspective, the findings echo and enrich emotional contagion theories in the context of OHCs. Confirming existing theories, our study shows that the emotions of depression patients can be improved through the online support provided through forum-like OHCs and through emotional contagion from auxiliary content. Moreover, under the joint effect of emotional contagion and depression patients’ self-evaluation in social comparison, emotional support in OHCs can cause a negative emotional impact on the unintended audience.

From a methodological perspective, the analysis shows that if we do not differentiate emotional support and auxiliary content, we will not be able to observe the negative effect of off-target content. OHCs are unique with respect to being anonymous and self-organized. The effect of off-target content is important and should not be ignored. Our study not only shows the potential of leveraging this wealth of data but also exemplifies the need for a proper methodology to deal with it. More detailed text mining is necessary to understand this phenomenon in OHCs, and our deep learning model can be applied in similar settings.

Practically, this study demonstrates the potential of leveraging OHCs to help patients suffering from depression. Due to the specifics of the disease, depression patients have a high probability of committing self-harm and even suicide. Our findings show that the scale of the positive and negative effects of emotional support are at a similar level. In other words, support providers’ positive impact on one patient can be canceled out by negative impacts on other (unintended) patients. Such ineffective online emotional support may lead to individual harm and the loss of life. According to our follow-up analyses, we should not overuse positive expressions to encourage patients. Instead, we suggest providing emotional support via more postings and longer postings from a larger group of support providers. By doing so, OHCs can help support seekers while reducing the negative impact on other users.

## Conclusion and Future Work

In this study, we examine the influence of different content in a depression OHC on patients’ emotions. We first built a deep learning model to classify post content into emotional support and auxiliary content. Then, we differentiated the content target as on-target and off-target and built a panel data model to study their respective effects. Our results confirm the positive effect of emotional support and auxiliary content. Moreover, we found that depressed patients’ emotions are negatively affected by emotional support content targeting other users. We provide evidence that this negative effect is robust and may be caused by social comparison. We also provide suggestions for tackling this negative effect.

The findings of the study have significant theoretical and practical implications. They enrich the understanding of OHCs in terms of the within-community emotional influence. Moreover, if emotional support and auxiliary content are not differentiated, it will only be possible to observe the effect of on-target content (as shown in previous research), with the negative effect of off-target content remaining unobserved. Missing such information can lead to a misunderstanding of the mechanisms of OHCs and could even have fatal consequences for users. The findings shed light on how to best use OHCs to enhance the mental health conditions of patients and suggest potential OHC-based intervention strategies. Combining advanced machine learning models with a deeper understanding of OHCs offers invaluable insights that could significantly improve patient welfare.

Our research is not without limitations. First, we studied a Chinese OHC. As in many other studies, the culture of the subjects may have affected the generalizability of the findings. For example, the “Mianzi/Face” problem may have an impact on mental health (Taylor et al., 2004; J. Zhang et al., 2004) in China. It would thus be worthwhile to study OHCs in other cultural settings to further validate our findings. Second, we used user expression sentiment as a measurement of users’ emotions. Although this is an established method in the literature, it would be better if we could validate the findings with additional measures, such as through the use of psychological questionnaires. Third, our study mainly focuses on emotional support following its differentiation from auxiliary content. Nevertheless, there are multiple types of auxiliary content in OHCs. It would be worthwhile to inspect the heterogeneous effect of different types of auxiliary content. For instance, do ads and other offtopic discussions have different effects than informational support? Would other auxiliary content also lead to social comparison? Such questions are worthy of further examination in future research. Fourth, this research studied a depression OHC. It is necessary to study whether the findings can be generalized to OHCs for other disorders.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the reviewers for their invaluable comments and suggestions throughout the review process. The authors also thank Douban for allowing us to access part of the data after anonymization for the study. This research is partially supported by the National Natural Science Foundation of China [Grant 71572169, 71672163, 71972164]; the Research Grants Council of the Hong Kong Special Administrative Region, China [GRF 11500519, 14500521, 14501320, 14503818, 165052947; Theme Based Research: T31- 604/18-N]; and the City University of Hong Kong [SRG 7005195, 7005474, 7005767].

## References

Aarts, J. W. M., Van Oers, A. M., Faber, M. J., Cohlen, B. J., Nelen, W. L. D. M., Kremer, J. A. M., & Van Dulmen, A. M. (2015). Communication at an online infertility expert forum: Provider responses to patients’ emotional and informational cues. Journal of Psychosomatic Obstetrics and Gynecology, 36(2), 66-74. https://doi.org/10.3109/0167482X.2015.1009033

Appel, H., Gerlach, A. L., & Crusius, J. (2016). The interplay between Facebook use, social comparison, envy, and depression. Current Opinion in Psychology, 9, 44-49. https://doi.org/10.1016/j.copsyc.2015.10.006

Argo, J. J., White, K., & Dahl, D. W. (2006). Social comparison theory and deception in the interpersonal exchange of consumption information. Journal of Consumer Research, 33(1), 99-108. https://doi.org/10.1086/504140

Bahdanau, D., Cho, K. H., & Bengio, Y. (2015). Neural machine translation by jointly learning to align and translate. In Proceedings of the 3rd International Conference on Learning Representations. https://doi.org/10.48550/arXiv.1409.0473

Barsade, S. G. (2002). The ripple effect: Emotional contagion and its influence on group behavior. Administrative Science Quarterly, 47(4), 644-675. https://doi.org/10.2307/3094912

Beaudoin, C. E., & Tao, C. C. (2007). Benefiting from social capital in online support groups: An empirical study of cancer patients. CyberPsychology & Behavior, 10(4), 587-590. https://doi.org/10.1089/cpb.2007.9986

Berkman, L. F., Glass, T., Brissette, I., & Seeman, T. E. (2000). From social integration to health: Durkheim in the new millennium. Social Science & Medicine, 51(6), 843-857. https://doi.org/10.1016/S0277-9536(00)00065-4

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of Machine Learning Research, 3, 993- 1022. https://doi.org/10.1162/jmlr.2003.3.4-5.993

Bollen, J., Gonçalves, B., Ruan, G., & Mao, H. (2011). Happiness is assortative in online social networks. Artificial Life, 17(3), 237-251. https://doi.org/10.1162/artl\_a\_00034

Bollen, K. A. (2012). Instrumental variables in sociology and the social sciences. Annual Review of Sociology, 38, 37-72. https://doi.org/10.1146/annurev-soc-081309-150141

Bösch, K., Müller, O., & Schneider, J. (2018). Emotional contagion through online newspapers. In Proceedings of the 26th European Conference on Information Systems.

Buunk, A. P., Bennenbroek, F. T. C., Stiegelis, H. E., van den Bergh, A. C. M., Sanderman, R., & Hagedoorn, M. (2012). Follow-up effects of social comparison information on the quality of life of cancer patients: The moderating role of social comparison orientation. Psychology and Health, 27(6), 641- 654. https://doi.org/10.1080/08870446.2011.613994

Chau, M., Li, T. M. H., Wong, P. W. C., Xu, J. J., & Chen, H. (2020). Finding people with emotional distress in online social media: A design combining machine learning and rule based classification. MIS Quarterly, 44(2), 933-955. https://doi.org/ 10.25300/MISQ/2020/14110

Chee, B. (2010). Sickness and health: Homophily in online health forums. Available at http://hdl.handle.net/2142/14926

Chen, L., Baird, A., & Straub, D. (2019). Fostering participant health knowledge and attitudes: An econometric study of a chronic disease-focused online health community. Journal of

Management Information Systems. https://doi.org/10.1080/ 07421222.2018.1550547

Chollet, F. (2015). Keras: Deep learning library for Theano and TensorFlow. Available at https://faroit.com/keras-docs/1.1.1/

Chung, J. E. (2014). Social networking in online support groups for health: How online social networking benefits patients. Journal of Health Communication, 19(6), 639-659. https://doi.org/ 10.1080/10810730.2012.757396

de Vries, D. A., Möller, A. M., Wieringa, M. S., Eigenraam, A. W., & Hamelink, K. (2018). Social comparison as the thief of joy: Emotional consequences of viewing strangers’ Instagram posts. Media Psychology, 21(2), 222-245. https://doi.org/10.1080/ 15213269.2016.1267647

Deng, S., Huang, Z., Sinha, A. P., & Zhao, H. (2018). The interaction between microblog sentiment and stock returns: An empirical examination. MIS Quarterly, 42(3), 895-918. https://doi.org/10.25300/MISQ/2018/14268

Elfenbein, H. A. (2014). The many faces of emotional contagion: An affective process theory of affective linkage. Organizational Psychology Review, 4(4), 326-362. https://doi.org/10.1177/2041386614542889

Feinstein, B. A., Hershenberg, R., Bhatia, V., Latack, J. A., Meuwly, N., & Davila, J. (2013). Negative social comparison on Facebook and depressive symptoms: Rumination as a mechanism. Psychology of Popular Media Culture, 2(3), 161. https://doi.org/10.1037/a0033111

Ferrara, E., & Yang, Z. (2015). Measuring emotional contagion in social media. PLoS ONE, 10(11), Article e0142390. https://doi.org/10.1371/journal.pone.0142390

Fowler, J. H., & Christakis, N. A. (2008). Dynamic spread of happiness in a large social network: longitudinal analysis over 20 years in the Framingham Heart Study. British Medical Journal, 337, a2338-a2338. https://doi.org/10.1136/bmj.a2338

Golder, S. A., & Macy, M. W. (2011). Diurnal and seasonal mood vary with work, sleep, and day length across diverse cultures. Science, 333(6051), 1878-1881. https://doi.org/10.1126/ science.1202775

Hancock, J. T., Gee, K., Ciaccio, K., & Lin, J. M. (2008). I’m sad you’re sad: Emotional contagion in CMC. In Proceedings of the ACM Conference on Computer Supported Cooperative Work (pp. 295-298). https://doi.org/10.1145/1460563.1460611

Hatfield, E., Cacioppo, J., & Rapson, R. (1993). Emotional contagion. Current Directions in Psychological Science, 2(3), 96-100. https://doi.org/10.1086/322897

Hausman, A. J. A. (1978). Specification tests in econometrics. Econometrica: Journal of the Econometric Society, 46(6), 1251-1271. https://doi.org/10.2307/1913827

Hawk, S. T., Fischer, A. H., & Van Kleef, G. A. (2011). Taking your place or matching your face: Two paths to empathic embarrassment. Emotion, 11(3), 502. https://doi.org/10.1037/ a0022762

Huang, K. Y., Chengalur-Smith, I. S., & Pinsonneault, A. (2019). Sharing is caring: Social support provision and companionship activities in healthcare virtual support communities1. MIS Quarterly, 43(2), 395-423. https://doi.org/10.25300/MISQ/ 2019/13225

Kaplan, B. H., Cassel, J. C., & Gore, S. (1977). Social support and health. Medical Care 15(5), 47-58. https://doi.org/10.1097/ 00005650-197705001-00006

Keating, D. M. (2013). Spirituality and support: A descriptive analysis of online social support for depression. Journal of Religion and Health, 52(3), 1014-1028. https://doi.org/ 10.1007/s10943-012-9577-x

Kingma, D. P., & Ba, J. L. (2015). Adam: A method for stochastic optimization. In Proceedings of the 3rd International Conference on Learning Representations. Available at https://doi.org/ 10.48550/ arXiv.1412.6980

Kipf, T. N., & Welling, M. (2017). Semi-supervised classification with graph convolutional networks. In Proceedings of the 5th International Conference on Learning Representations. Available at https://doi.org/10.48550/arXiv.1609.02907

Kokkodis, M., & Lappas, T. (2020). Your hometown matters: Popularity-difference bias in online reputation platforms. Information Systems Research, 31(2), 412-430. https://doi.org/10.1287/ISRE.2019.0895

Kramer, A., Guillory, J. E., & Hancock, J. T. (2014). Experimental evidence of massive-scale emotional contagion through social networks. In Proceedings of the National Academy of Sciences, 111(24), 8788-8790. https://doi.org/10.1073/pnas.1412469111

Kwon, K. H., & Gruzd, A. (2017). Is offensive commenting contagious online? Examining public vs interpersonal swearing in response to Donald Trump’s YouTube campaign videos. Internet Research, 27(4), 1066-2243. https://doi.org/10.1108/ IntR-02-2017-0072

Lazarus, R. S. (1991). Progress on a cognitive-motivationalrelational theory of emotion. American Psychologist, 46(8), 819-834. https://doi.org/10.1037/0003-066X.46.8.819

Leung, L. (2011). Loneliness, social support, and preference for online social interaction: the mediating effects of identity experimentation online among children and adolescents. Chinese Journal of Communication, 4(4), 381-399. https://doi.org/10.1080/17544750.2011.616285

Li, S., Zhao, Z., Hu, R., Li, W., Liu, T., & Du, X. (2018). Analogical reasoning on Chinese morphological and semantic relations. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics. https://doi.org/ 10.18653/v1/p18-2023

Lin, R., & Utz, S. (2015). The emotional responses of browsing Facebook: Happiness, envy, and the role of tie strength. Computers in Human Behavior, 52, 29-38. https://doi.org/ 10.1016/j.chb.2015.04.064

Lin, Y. W., Ahsen, M. E., Shaw, M. J., & Seshadri, S. (2019). The impacts of patients’ sentiment trajectory features on their willingness to share in online support groups. In Proceedings of the International Conference on Information Systems.

Luo, K., Teo, H. H., Wang, Q. H., & Chen, X. (2018). Better inpatient health quality at lower cost: Should I participate in the online healthcare community first? In Proceedings of the International Conference on Information Systems.

Mein Goh, J., Gao, G., Agarwal, R., Goh, J. M., Gao, G., & Agarwal, R. (2016). The creation of social value: Can an online health community reduce rural-urban health disparities? MIS Quarterly, 40(1), 247-263. https://www.jstor.org/stable/ 26628392

Millimet, D. L., & McDonough, I. K. (2017). Dynamic panel data models with irregular spacing: With an application to early childhood development. Journal of Applied Econometrics, 32(4), 725-743. https://doi.org/10.1002/jae.2548

Mimno, D., Wallach, H. M., Talley, E., Leenders, M., & McCallum, A. (2011). Optimizing semantic coherence in topic models. In Proceedings of the Conference on Empirical Methods in Natural Language Processing.

Nambisan, P. (2011). Information seeking and social support in online health communities: Impact on patients’ perceived empathy. Journal of the American Medical Informatics Association, 18(3), 298-304. https://doi.org/10.1136/amiajnl-2010-000058

O’Connor, L. E., Berry, J. W., Weiss, J., & Gilbert, P. (2002). Guilt, fear, submission, and empathy in depression. Journal of Affective Disorders, 71(1-3), 19-27. https://doi.org/ 10.1016/S0165-0327(01)00408-6

Park, A., & Conway, M. (2017). Longitudinal changes in psychological states in online health community members: Understanding the long-term effects of participating in an online depression community. Journal of Medical Internet Research, 19(3), Article e71. https://doi.org/10.2196/jmir.6826

Pennebaker, J., Francis, M., & Booth, R. (2001). Linguistic inquiry and word count: LIWC 2001. Lawrence Erlbaum Associates.

Pera, A. (2018). Psychopathological processes involved in social comparison, depression, and envy on Facebook. Frontiers in Psychology, 9(22). https://doi.org/10.3389/fpsyg.2018.00022

Reifegerste, D., Wasgien, K., & Hagen, L. M. (2017). Online social support for obese adults: Exploring the role of forum activity. International Journal of Medical Informatics, 101, 1-8. https://doi.org/10.1016/j.ijmedinf.2017.02.003

Rosenbusch, H., Evans, A. M., & Zeelenberg, M. (2019). Multilevel emotion transfer on YouTube: Disentangling the effects of emotional contagion and homophily on video audiences. Social Psychological and Personality Science, 10(8), 1028-1035. https://doi.org/10.1177/1948550618820309

Smailhodzic, E., Hooijsma, W., Boonstra, A., & Langley, D. J. (2016). Social media use in healthcare: A systematic review of effects on patients and on their relationship with healthcare professionals. BMC Health Services Research, 16(1), 1-14. https://doi.org/10.1186/s12913-016-1691-0

Smith, K. (2014). Mental health: A world of depression. Nature, 515(181), 10-1038. https://doi.org/10.1038/515180a

Suls, J., Martin, R., & Wheeler, L. (2002). Social comparison: Why, with whom, and with what effect? Current Directions in Psychological Science, 11(5), 159-163. https://doi.org/ 10.1111/1467-8721.00191

Sun, M., Zhang, X., & Zhu, F. (2019). U-shaped conformity in online social networks. Marketing Science, 38(3), 461-480. https://doi.org/10.1287/mksc.2018.1133

Taylor, S. E., Sherman, D. K., Kim, H. S., Jarcho, J., Takagi, K., & Dunagan, M. S. (2004). Culture and social support: Who seeks it and why? Journal of Personality and Social Psychology, 87(3), 354-362. https://doi.org/10.1037/0022-3514.87.3.354

Wang, A., Zhang, X., & Hann, I. (2018) Socially nudged: A quasi-experimental study of friends' social influence in online product ratings. Information Systems Research, 29(3), 641- 655. https://doi.org/10.1287/isre.2017.0741

Wang, X., Bagul, D. M., Parameswaran, S., & Kishore, R. (2017). Does online social support work in stigmatized chronic diseases? A study of the impacts of different facets of informational and emotional support on self-care behavior in an HIV online forum. In Proceedings of the International

Conference on Information Systems. https://aisel.aisnet.org/ icis2017/General/Presentations/22

Yan, L., & Tan, Y. (2014). Feeling blue? Go online: An empirical study of social support among patients. Information Systems Research, 25(4), 690-709. https://doi.org/10.1287/ isre.2014.0538

Yan, L., & Tan, Y. (2017). The consensus effect in online healthcare communities. Journal of Management Information Systems, 34(1), 11-39. https://doi.org/10.1080/07421222.2017. 1296742

Yang, Z., Yang, D., Dyer, C., He, X., Smola, A., & Hovy, E. (2016). Hierarchical attention networks for document classification. In Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics (pp. 1480-1489). https://doi.org/10.18653/v1/N16- 1174

Yoo, W., Namkoong, K., Choi, M., Shah, D. V., Tsang, S., Hong, Y., Aguilar, M., & Gustafson, D. H. (2014). Giving and receiving emotional support online: Communication competence as a moderator of psychosocial benefits for women with breast cancer. Computers in Human Behavior, 30, 13-22. https://doi.org/10.1016/j.chb.2013.07.024

Zhang, H.-P., Yu, H.-K., Xiong, D.-Y., & Liu, Q. (2003). HHMMbased Chinese lexical analyzer ICTCLAS. In Proceedings of the Second SIGHAN Workshop on Chinese Language Processing. https://doi.org/10.3115/1119250.1119280

Zhang, J., Conwell, Y., Zhou, L., & Jiang, C. (2004). Culture, risk factors and suicide in rural China: A psychological autopsy case control study. Acta Psychiatrica Scandinavica, 110(6), 430-437. https://doi.org/10.1111/j.1600-0447.2004.00388.x

Zhang, X., & Wang, C. (2012). Network positions and contributions to online public goods: The case of Chinese Wikipedia. Journal of Management Information Systems, 29(2), 11-40. https://doi.org/10.2753/MIS0742-1222290202

Zhang, X., and Zhu, F. (2011). Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. American Economic Review, 101 (4), 1601-1615. https:// doi.og/10.1257/aer.101.4.1601

Zhou, P., Shi, W., Tian, J., Qi, Z., Li, B., Hao, H., & Xu, B. (2016). Attention-based bidirectional long short-term memory networks for relation classification. In Proceedings of the 54<sup>th</sup> Annual Meeting of the Association for Computational Linguistics. https://doi.org/10.18653/v1/P16-2034

## About the Authors

Jiaqi Zhou is an Algorithm Expert in the Alibaba Group. He received his Ph.D. degree in data science from the City University of Hong Kong in 2018. His research interests include healthcare data analytics, recommender systems, machine learning and deep learning.

Qingpeng Zhang is an associate professor with the School of Data Science at City University of Hong Kong. He received his Ph.D. degree in systems and industrial engineering with a minor in management information systems from The University of Arizona in 2012. Prior to joining City University of Hong Kong in 2014, he worked as a postdoctoral research associate with The Tetherless

World Constellation in the Department of Computer Science at Rensselaer Polytechnic Institute. His research interests include healthcare data analytics, medical informatics, network science, and artificial intelligence. His research has appeared in Nature Human Behaviour, Nature Communications, Journal of the American Medical Informatics Association, Briefings in Bioinformatics, Physical Review E, and so on. He received the City University of Hong Kong President’s Award (2022) and Outstanding Research Award for Junior Faculty (2021). His ORCiD is 0000-0002-6819-0686.

Sijia Zhou is an assistant professor in the Department of Electronic Commerce at Southeast University, China. She received her Ph.D. in information systems from the City University of Hong Kong. Her research interests are online healthcare and social influence. Her research has been published in Information Processing & Management and several conferences. Her ORCiD is 0000-0002- 3126-1305.

Xin Li is a professor in the Department of Information Systems at the City University of Hong Kong. He received his Ph.D. in management from the University of Arizona and his B.E. and M.E.

from Tsinghua University. His research interests include digital economy, data science, healthcare, network analysis, and applied econometrics. His research appears in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, and INFORMS Journal on Computing, among other outlets. He is an associate editor of INFORMS Journal on Computing and a senior editor of Information Technology and People. His ORCiD is 0000-0002-0041-3134.

Xiaoquan (Michael) Zhang is the Irwin and Joan Jacobs Chair Professor at the School of Economics and Management, Tsinghua University. He has a Ph.D. in management from MIT Sloan School of Management, and several degrees (MSc., BE, BA) from Tsinghua University. Professor Zhang’s works study pricing of information goods, online advertising, and the use of artificial intelligence in financial markets. His research has appeared in American Economic Review, Management Science, Marketing Science, Journal of Marketing, MIS Quarterly, Information Systems Research, and so on. He co-authored a book on digital transformation: Digital Quantum Leap-Strategies and Tactics for Organizational Transformation. His ORCiD is 0000-0003-0690-2331.

## Appendix

## The C-HAN Model

T denotes a support-seeking thread in the online health community. For each post ?? ∈T, we aim to identify if it provides emotional support to the conversation target. In our dataset, the conversation target is either a target user or the original post if no reply relationship exists.

![](/api/attachments/KXNUZDH3/fulltext/images/470eda211019f9bbe3a22841538ef51c2814d0e59434c7d1358a9259863dbe4a.jpg)  
Figure A1. Modeling the Context and Two Types of Relations in a Thread  
Figure A1 illustrates the three components in our proposed model. Component $\textcircled{1}$ deals with the original post $p _ { o }$ of the discussion thread. In this component, we leverage a Bidirectional Long Short-Term Memory (BiLSTM) (Zhou et al., 2016) module to capture the context of the thread set up by the support seeker. Component $\textcircled{2}$ captures the reply-to relationship $P _ { r } = { < p _ { \bar { r } } , p , p _ { r } > } ,$ , where p replied to $p _ { \bar { r } }$ and $p _ { r }$ replies to $p .$ If there is no reply to $p , p _ { r }$ is null. $\mathrm { I f } p$ does not reply to a specific post, the reply is considered to target the original post $p _ { o } ,$ i.e., $p _ { \bar { r } } = p _ { o } .$ In this component, we leverage a Hierarchical Attention Networks (HAN) (Yang et al., 2016) module to capture the explicit conversation process. Component $\textcircled{3}$ captures the sequential relationship $P _ { s } = < p _ { \bar { s } } , p , p _ { s } > _ { \mathrm { { \scriptscriptstyle S } } }$ , where $p _ { \bar { s } }$ is the immediate post before $p$ and $p _ { s }$ is the immediate post after p. $\mathrm { I f } p$ is the original post $p _ { o } ,$ $p _ { \bar { s } }$ is null. $\mathrm { I f } p$ is the last post in $T , p _ { s }$ is null. In this component, we leveraged a HAN module to model the implicit conversation process that ma exist along with the sequence of posts. Then, we combined the information from the three modules to build a classifier.

Our model is a composition model that combines three deep learning structures. Such a method to combine basic deep learning modules into a complicated model is common in literature (for example, BiLSTM is a combination of two LSTMs, and HAN is a combination of two layers of BiGRUs). In this study, we consider the original post context, the conversation relationship, and the sequence of posts because they all play a vita role in identifying whether the current post is emotional support. Thus, we composited them into a prediction model. For example, if $p _ { \bar { r } }$ expresses sadness or anxiety and ?? is offering encouragement or comfort, $\mathbf { \nabla } _ { p }$ is more likely to be emotional support. Besides, $\mathrm { i f } p$ provides emotional support, $p _ { r }$ could be a post of appreciation or relief. Our model is novel in the literature in considering the post structure of web forums to composite the three models. Below, we elaborate on the detailed setup of each module.

## BiLSTM Module to Process Original Post

![](/api/attachments/KXNUZDH3/fulltext/images/4279dd85d3b1488434ba89c287f482f2c83e04814e7f392bf585e2fe4077c83b.jpg)  
Figure A2. LSTM Memory Block with One Cell  
First, we used a bidirectional long short-term memory (BiLSTM) (Zhou et al., 2016) model (as annotated by ① in Figure 3 in the paper) to process the original post $p _ { o } .$ In the process, we conducted word segmentation of po and embedded its words to a d1-dimension word vector. (We chose ${ \bf d } _ { 1 } = 3 0 0$ for this study.) Here, we enforced the length of each post to be 200 words by truncating long posts and extending short posts with additional zeros.

BiLSTM extends the classic long short-term memory (LSTM) model by modeling the bidirectional dependencies of words in a document. LSTM is a recurrent neural network that process the input word vector xt of d dimensions, where t indicates the sequence of words in $p _ { o }$ . It has an input gate $i _ { t , }$ an output gate $O t ,$ and a forget gate $f _ { t }$ around state cell ct. The module generates a hidden vector ht as output. During the processing, the input data are converted to ${ \bf d } _ { 2 }$ dimensions. (We chose $\mathbf { d } _ { 2 } = 2 0 0$ for this study.) At the end, ct generates output through the output gate. The model is formulated as follows:

$$
i _ {t} = \tanh (W _ {i} x _ {t} + U _ {i} h _ {t - 1} + b _ {i}),\tag{A1}
$$

$$
f _ {t} = \tanh (W _ {f} x _ {t} + U _ {f} h _ {t - 1} + b _ {f}),\tag{A2}
$$

$$
o _ {t} = \tanh (W _ {o} x _ {t} + U _ {o} h _ {t - 1} + b _ {o}),\tag{A3}
$$

$$
\widetilde {h _ {t - 1}} = \tanh (W _ {c} x _ {t} + U _ {c} h _ {t - 1} + b _ {c}),\tag{A4}
$$

$$
c _ {t} = f _ {t} \odot c _ {t - 1} + i _ {t} \odot \widetilde {h _ {t}},\tag{A5}
$$

$$
h _ {t} = o _ {t} \odot \tanh (c _ {t}),\tag{A6}
$$

where state $c _ { t }$ is updated based on the state in the previous word $c _ { t - l }$ manipulated by forget gate $f _ { t }$ and a transformed input activation $\widetilde { h _ { t } }$ manipulated by input gate $i _ { t . }$ The gates and $\widetilde { h _ { t } }$ depend on ${ \mathrm { d } } _ { 1 }$ -dimension input $x _ { t } ,$ which is converted to ${ \bf d } _ { 2 }$ dimensions with weights $W _ { i } , W _ { f } ,$ $W _ { o } , W _ { c } ( d _ { 2 } ^ { * } d _ { I }$ dimensions). Meanwhile, they also depend on the hidden vector ht-1 of the previous word with weights $U _ { i } , U _ { f } , U _ { o } , U _ { c } ( d _ { 2 } ^ { * } d _ { 2 }$ dimensions) and incept $b _ { i } , b _ { f } , b _ { o } ,$ and $b _ { c }$ (d2 dimensions). At last, hidden vector $h _ { t - I }$ is generated by state $c _ { t } ,$ manipulated by output gate $o _ { t } .$ In the process, we choose the hyperbolic tangent activation function tanh( ). ʘ is the tensor dot product. (We chose ${ \mathrm { d } } _ { 1 } = 3 0 0$ and ${ \bf d } _ { 2 } = 2 0 0$ for this study.)

Based on LSTM, BiLSTM combines one forward LSTM and one backward LSTM (which reverse the words appearing along with t) to capture two directions of sequential context into an output vector $\nu _ { o } .$ Since each vector is d2 dimensions, the combined ${ \bf V } _ { 0 }$ is 2d2 dimensions. The vector would allow us to identify the meaning of po if feeding to an appropriate classifier.

## HAN Module to Capture Reply-to Relationship (Reply HAN)

Second, we modeled the reply-to relationship of a post (as annotated by $\textcircled{2}$ in Figure 3 in the paper) using HAN. We set $P _ { r } { < } p _ { \bar { r } } { , } p , p _ { r } { > }$ as the input of HAN. HAN considers the interdependencies among words and posts and assigns weights to words in a post and assigns weights to the three posts in a $P _ { r }$ , which helps to determine p’s type.

When applying the HAN model on $P _ { r }$ , we conducted word segmentation and embedded words to d3-dimension word vectors for each post. (We chose ${ \bf d } _ { 3 } = 3 0 0$ for this study.) Thus, we have three word vectors for the three posts in tuple $P _ { r }$ . This creates a two-layer structure (wordpost-tuple) that allowed us to leverage the HAN model (i.e., post is as sentence and tuple is as document).

We adopted the bidirectional gated recurrent unit (BiGRU) layer with 100 neurons as the first layer of the encoder for the HAN model. GRU has two gates, the update gate $z _ { t }$ and the reset gate $r _ { t }$ (Bahdanau et al., 2015), and can be formalized as follows:

$$
z _ {t} = \tanh (W _ {z} x _ {t} + U _ {z} h _ {t - 1} + b _ {z}),\tag{A7}
$$

$$
r _ {t} = \tanh (W _ {r} x _ {t} + U _ {r} h _ {t - 1} + b _ {r}),\tag{A8}
$$

$$
\widetilde {h} _ {t} = \tanh (W _ {k} x _ {t} + r _ {t} \odot (U _ {k} h _ {t - 1}) + b _ {k}),\tag{A9}
$$

$$
h _ {t} = (1 - z _ {t}) \odot h _ {t - 1} + z _ {t} \odot \widetilde {h} _ {t},\tag{A10}
$$

where $\mathbf { X } _ { \mathrm { { f } } }$ is the d3-dimensional input of the embedded words and $h _ { t }$ is the d4-dimensional hidden vector as output. (We chose $\mathrm { d } _ { 4 } = 1 0 0$ for this study.) ht is updated based on the state in the previous word ht-1 and a transformed input activation $\widetilde { h _ { t } }$ manipulated by update gate zt. The gates and $\widetilde { h _ { t } }$ depend on d3-dimension input xt, which is converted to d4 dimensions with weights $W _ { z } , W _ { r } , W _ { k } ( \mathrm { d } _ { 4 } { * } \mathrm { d } _ { 3 }$ dimensions). Meanwhile, they also depend on the hidden vector ht-1 of the previous word with weights $U _ { z } , U _ { r } , U _ { k } ( \mathrm { d } _ { 4 } \ast$ d4 dimensions) and incept $b _ { z } , b _ { r } , b _ { k }$ (d4 dimensions). Besides, in $\widetilde { h _ { t } }$ the effect of hidden vector $h _ { t - I }$ is manipulated by gate $r _ { t } .$ In the process, we use the hyperbolic tangent activation function tanh( ). ʘ is the tensor dot product.

Similar to the BiLSTM structure, inputs to a BiGRU form two series of outputs, which account for the two directions of word correlations We combined them into one vector, which forms a 2d4 dimension vector for each word in a post. Note that the BiGRU can be applied on all posts in the forum. For processing the three posts in tuple Pr, we denote them as $\mathrm { I } \in ( p _ { \bar { r } } , p , p _ { r } )$ in the below formulae and denote the corresponding output of BiGRU as $h _ { i t }$

Then, the attention mechanism of HAN could extract the importance of words for assessing the meaning of each post using the following formulae:

$$
u _ {i t} = \tanh (W _ {w} h _ {i t} + b _ {w}),\tag{A11}
$$

$$
\alpha_ {i t} = s o f t m a x (u _ {i t} ^ {\prime} * u _ {w}),\tag{A12}
$$

$$
s _ {i} = \sum_ {t} \alpha_ {i t} h _ {i t},\tag{A13}
$$

where $u _ { i t }$ is a d5 dimensions latent representation of the 2d4 dimension input hit with weight $W _ { w } ( { \mathrm { d } } s ^ { * } 2 { \mathrm { d } } u$ dimensions). (We chose ${ \bf d } _ { 5 } = 1 0 0$ for this study.) $\alpha _ { i t }$ is the normalized importance weight representing the importance of each word. HAN calculates it as the similarity between latent representation $u _ { i t }$ and a word-level context vector $u _ { w }$ (followed by a softmax function). $u _ { w }$ is a parameter vector of d5 dimensions learned through training on all the data. In the end, $\alpha _ { i t }$ is used to weight each word in the 2d4 dimension input hit to generate the 2d4 dimension output $s _  i , $ representing the meaning of the post i.

Then, for the three posts in tuple $P _ { r } ,$ we have three 2d dimension vectors s as post-level input. We applied another bidirectional GRU encoding at post level, converting them to d6 dimension hidden post-level vectors $h _ { i } ^ { s }$ . (We chose $\mathrm { d } _ { 6 } = 1 0 0$ for this study.) We also used the attention mechanism to extract the importance of each of the three posts. Similar to the word-level attention module, we generated the postlevel context vectors and calculated the post-level importance weight $\alpha _ { i } ^ { s }$ , which allowed us to combine the information in the three posts into a 2d6 dimension vector vr representing the tuple $P r$

$$
v _ {r} = \sum_ {t} \alpha_ {i} ^ {s} h _ {i} ^ {s},\tag{A14}
$$

Figure A3 illustrates the above process. Assume we have an emotional support posting “抱抱,一起加油努力(Hug, let’s work hard together),” which can be segmented to four words, “抱抱(hug),” “一起(together),” “加油(work/fight),” and “努力(hard).” After word embedding, it becomes four 300-dimension vectors. After bidirectional GRU encoding, we get four 200-dimension vectors. Through the word-level attention mechanism, we have a 200-dimensional post-level vector. By repeating the process on all three posts in Pr, through bidirectional GRU and attention, we get an aggregate 200-dimensional tuple meaning vector vr.

![](/api/attachments/KXNUZDH3/fulltext/images/964d61314f54f8ac86576efa9547a528164aca0cfc3becfe2c48f59a0dd51b88.jpg)  
Figure A3. Reply HAN Illustration

## HAN Module to Capture Sequential Relationship (Sequence HAN)

Third, we modeled the sequential relationship of a post (as annotated by $\textcircled{3}$ in Figure 3 in the paper). Similar to the modeling of the reply relationship, we combined and modeled $P _ { s } < p _ { s i } , p , p _ { s j } >$ using HAN. This HAN model has the same structure as in the reply HAN. We also used the attention mechanism to capture important words in posts and important posts in the tuple

## Concatenate Layer

The output of the three components, vo for the BiLSTM module (①), vr for the Reply HAN (②), and $v _ { s }$ for the Sequence HAN $\textcircled{3}$ , are combined in a concatenation layer v=[vo;vr;vs]. Then, we use it as the feature through a softmax action function

$$
p = \text { softmax } (W _ {c} v + b _ {c}),\tag{A15}
$$

and minimize the log likelihood of the labels j of post d:

$$
L = - \sum_ {d} \log p _ {d j},\tag{A16}
$$

## Parameter Tuning

We conducted Chinese word segmentation on all the posts using a standard toolkit, ICTCLAS 2016 (H.-P. Zhang et al., 2003). We also used pretrained Word2Vec to preprocess the data for dimension reduction (Li et al., 2018), which converts each word into a vector, and a post becomes a sequence of vectors based on the word vector (with zero-word vector to fill up sentences that are not long enough). Eventually, all posts are represented by a sequence of vectors, which capture the semantics and sequences of the words.

To train the model, we adopted the Adam optimization solver (Kingma & Ba, 2015) in TensorFlow (with the Keras API) (Chollet, 2015) to implement the proposed model. For the hyperparameter tuning, the neural network is trained by back-propagation in mini-batches. For the input, we set the word embedding dimension for individual posts to be 300 for each word, and the input feature length is 200 for the BiLSTM and Bidirectional GRU models. The initial learning rate is 0.00001, and the batch size is 128. For the BiLSTM module to process origina posts, the dropout is 0.2, and the number of nodes in each layer is 200. For the HAN module to capture reply relationships and sequence relationships, the dropout is 0.2, and the number of nodes in each layer is 100

## Parameter Tuning for The Baseline Models

For the baseline BiLSTM model, which only considers the sequence of words in each post, we set up it the same as the BiLSTM module in C-HAN. For the hyperparameter tuning, the input feature length is 200. The initial learning rate is 0.007, and the batch size is 128. The dropout is 0.2, and the number of nodes in each layer is 200.

Another baseline is the graph convolutional network (GCN), which represents each post as a vertex and captures the reply relationship of posts. We used a two-layer GCN model to capture the potential interrelations between nodes. We adopted the Adam optimization solver (Kingma & Ba, 2015) in TensorFlow (with the Keras API) (Chollet, 2015) for implementation. The initial learning rate is 0.0001 and the batch size is 128.

Figures  
![](/api/attachments/KXNUZDH3/fulltext/images/7bbea84c3856abfcf7e10900887342e6532913962074d369464f0d592e6f2c02.jpg)

Figure A4. Mock (Translated) Screenshot of Discussion Thread on Douban

![](/api/attachments/KXNUZDH3/fulltext/images/b2558f587f663ce877c5f48345157b4c956598c1e21ad6222a8ee5b25add30ec.jpg)

Figure A5. The Hourly Activity of Users

<table><tr><td colspan="3">Major Topics of Emotional Support</td></tr><tr><td>打坐britpopsavedmylife周日好久改天倾向休学 哈哈哈情感 音乐 感慨没事儿真诚暂时</td><td>内心 运动 父母 努力痛苦 东西 生活心理 朋友 经历 世界 事情加油 自杀 人生</td><td>幸福 交流 药物意识 治疗 网上工作 有时候 影响 方法真的 纠结过程 放弃 快乐</td></tr><tr><td>MeditatebritpopsavedmylifeAnother daySunday Long time tendencySuspension HahahaFeelingMusic Sincere Never mind Lament Temporary</td><td>Inner Sports ParentsWork hardPainThing LivingMentalFriendExperience World ThingGo for it Suicide Life</td><td>Wellbeing Interaction MedicineIntention Internet Work Sometimes Influence Method Really Tangled Process Give up Happy</td></tr><tr><td colspan="3">Major Topics of Auxiliary Content</td></tr><tr><td>心理学 说话世界 音乐 环境爱情 加油结果自杀 也许事情 成长 绝望 同学没什么</td><td>女人 硕神病晒太阳 研究 爸爸白天 爸爸长期 晚上 适合强迫 睡眠 症状焦虑 北京</td><td>正确 不用 可怕 空白</td></tr><tr><td>Psychology TalkWorld Music Environment Love Go for itEnd Suicide PerhapsThing Grow up Give up Classmate</td><td>Woman Study Mental illness Sunbath Day FatherLong Term Night Heal SuitableForce Sleep Symptom Anxiety Beijing</td><td>Correct Terrible No need Spring Insurance Blank Trust Care Control word Those away appetite brain</td></tr></table>

Figure A6. Major Topics Words (and English Translation) in Emotional Support and Auxiliary Content
