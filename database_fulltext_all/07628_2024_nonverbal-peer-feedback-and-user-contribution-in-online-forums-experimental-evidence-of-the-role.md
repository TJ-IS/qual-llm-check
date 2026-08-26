---
otero_id: 7628
otero_key: "EG88MYBZ"
title: "Nonverbal Peer Feedback and User Contribution in Online Forums: Experimental Evidence of the Role of Attribution and Emotions"
authors: "Ramesh Shankar; Lei Wang; Kunter Gunasti; Hongfei Li"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00840"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# Nonverbal Peer Feedback and User Contribution in Online Forums: Experimental Evidence of the Role of Attribution and Emotions

Ramesh Shankar , ramesh.shankar@uconn.edu

Lei Wang , Lei.Wang@psu.edu

Kunter Gunasti , kunter.gunasti@wsu.edu

Hongfei Li , hongfei.li@cuhk.edu.hk

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Nonverbal Peer Feedback and User Contribution in Online Forums: Experimental Evidence of the Role of Attribution and Emotions

Ramesh Shankar,<sup>1</sup> Lei Wang,<sup>2</sup> Kunter Gunasti,<sup>3</sup> Hongfei Li<sup>4</sup>

<sup>1</sup>School of Business, University of Connecticut, USA, ramesh.shankar@uconn.edu <sup>2</sup>Smeal College of Business, Penn State University, USA, lei.wang@psu.edu <sup>3</sup>Carson College of Business, Washington State University, USA, kunter.gunasti@wsu.edu <sup>4</sup>CUHK Business School, The Chinese University of Hong Kong, Hong Kong, hongfei.li@cuhk.edu.hk

## Abstract

Peer feedback is often associated with an increase in the contributions of members in online communities. Verbal feedback (such as a review) can give details about how the recipient can improve their contribution, but it requires the recipient to read and process the feedback. Conversely, nonverbal feedback (such as an upvote) is easy to comprehend but does not convey much helpful information. Prior studies have mainly focused on the impact of verbal feedback. However, little has been done to explore the underlying mechanism of the effect of nonverbal peer feedback on people’s tendency to contribute more. We present two experimental studies conducted on Amazon Mechanic Turk. Study 1 demonstrates how verbal and nonverbal feedback impact user contributions differently. Next, building on attribution-emotion-action theory, we use Study 2 to establish a causal mechanism between nonverbal feedback and users’ knowledge contribution. Specifically, users who receive nonverbal peer feedback make internal and external attributions, which in turn impact their emotions and contribution decisions. We find that users receiving more positive feedback attribute this in equal measure internally to perceived self-efficacy and externally to perceived fairness, whereas users who receive negative feedback attribute it more to the lack of perceived fairness of peer feedback. These findings have important implications for both content-sharing platforms and researchers trying to better understand the drivers of online content-sharing behavior.

Keywords: Nonverbal Peer Feedback, Attribution-Emotion-Action Theory, User-Generated Content, Experiment

Giri Kumar Tayi was the accepting senior editor. This research article was submitted on December 24, 2020 and underwent two revisions.

## 1 Introduction

Content contribution in online communities (such as YouTube, Stack Overflow, Reddit, and others) is a central area of interest for researchers and practitioners. Increasing members’ contributions represents a significant challenge for online platforms (Huang et al., 2018; Ma & Agarwal, 2007; Zhu et al., 2013). Because content contribution often depends on users’ goodwill and is typically supplied voluntarily, it suffers from an underprovisioning issue (Burtch et al., 2017; Huang et al., 2019), which has been recognized by both scholars and business practitioners.

Accordingly, finding ways to motivate users to contribute content is becoming an issue of prime importance for many online platforms. While monetary incentives (Li et al., 2022; Wang et al., 2021) are known to be significant motivators, nonmonetary incentives and multiple gamification tools (Wang et al., 2020) have been adopted to boost contributions on various online platforms—for example, badges on Stack Overflow, awards/trophies on Reddit, and periodic updates about the readership of users’ contributed content on TripAdvisor and Academia.edu. Feedback is recognized as an important element of nonmonetary incentives in a variety of contexts, including auctions (Adomavicius et al., 2012), decision quality (Surinder Singh & Randolph, 2003), and user-generated content (Burtch et al., 2021; Chen et al., 2018; Zhao et al., 2022).

In this paper, we focus on the role of nonverbal feedback in motivating subsequent contributions. When a user contributes to an online community (e.g., Stack Overflow or Reddit), other community members can give feedback in verbal (such as comments, follow-up questions, etc.) or nonverbal forms (such as upvotes, downvotes, emojis, etc.). While verbal feedback can contain specific information that can help the recipient better understand how to improve their subsequent contributions, verbal feedback also requires the recipient to read and process detailed information, which can be cognitively demanding and time-consuming. In contrast, nonverbal feedback such as an upvote or downvote is brief and can be quickly processed by the recipient, with one caveat: it lacks details. An upvote indicates approval only, while a downvote indicates disapproval without telling the recipient what was right or wrong about their contribution and how they could improve their contributions in the future. Therefore, we hypothesize that nonverbal feedback may have different impacts on future contributions compared to verbal feedback.

While many studies have focused on verbal feedback (in the form of messages) (Huang et al., 2019; Jabr et al., 2014), the importance of nonverbal feedback (such as upvotes and downvotes on Stack Overflow and YouTube, peer awards on Reddit, emojis and other visual cues, etc.) provided by other users has yet to be fully examined in the information systems literature. In a recent study, Burtch et al. (2021) showed that nonverbal positive peer feedback (i.e., peer awards) increases users’ content contribution quantity on Reddit and that this effect is more pronounced among new community members. In contrast, Wang et al. (2022) demonstrated that nontextual positive feedback is negatively associated with the knowledge contribution on Stack Overflow.

Thus, our research is motivated by the inconclusive evidence in prior literature regarding the effect of nonverbal feedback. Specifically, we explore the impact of nonverbal peer feedback, such as upvotes and downvotes from other peers in the community, on users’ subsequent content contribution propensity.

Furthermore, we examine the underlying mechanisms behind such an impact from a psychological perspective. We draw upon the attribution-emotionaction model of motivated behavior from the psychology literature, first introduced by Weiner (1980), which suggests that attributions provide affect—i.e. generate emotions, and these emotional reactions in turn provide the “motor and direction for behavior” (Weiner 1980). Therefore, following the attribution-emotions-action sequence, which is wellestablished in the psychology literature (Weiner, 1980), we address the following research questions:

1. How do content contributors make attributions regarding the nonverbal peer feedback they receive, internally or externally?

2. Are there any differences between contributors’ attribution of positive versus negative nonverbal peer feedback?

3. How do emotions such as excitement and hope mediate the relationship between contributors attribution and their willingness to contribute content?

Prior work has examined the impacts of positive and negative verbal feedback on recipients’ motivation to engage and contribute to online forums. For example, through a field experiment, Zhu et al. (2013) established that positive and negative verbal feedback impacts members’ contribution levels and that members’ prior experience moderates such impacts. Due to the correlational nature of studies employed in the past literature, the causal mechanisms behind why nonverbal peer feedback leads to the recipients increased or decreased contribution have yet to be explored. We address this gap and establish a causal mechanism linking nonverbal peer feedback and user contribution using experiments administered on Amazon Mechanical Turk (mTurk). Based on attribution-emotions-action theory (Weiner, 1980), our experiments helped us examine how users attribute nonverbal peer feedback and how emotions (excitement and hope) mediate the relationship between users’ attributions related to the feedback and their willingness to contribute.

Our research generated three major findings. First, we identified the mediating role of attributions on the relationship between peer feedback and user contribution. Specifically, we found that positive peer feedback causes the focal user to attribute it both internally (to perceived self-efficacy) and externally (to perceived fairness) in equal measure, which significantly increases users’ willingness to contribute. Regarding negative feedback, we found that users attribute it more externally (to perceived unfairness on the part of the feedback giver) and less internally (to perceived self-efficacy). Our findings indicate that feedback valence does not directly affect users’ willingness to contribute, but users receiving negative nonverbal feedback (relative to positive nonverbal feedback) attribute it to perceived unfairness to a greater degree. This suggests that compared to negative feedback, receiving positive nonverbal feedback may increase users’ willingness to contribute.

Second, regarding the role of emotions, we found that excitement and hope mediate the relationship between attributions and the willingness to contribute. Based on attribution-emotion-action theory from psychology (Weiner, 1980), we posit that after the user makes an attribution (internal or external) for the feedback they receive, they transition to an emotional state— excitement or hope in our case. We chose the emotions of excitement and hope for the following reasons: (1) prior literature has shown that excitement is an indicator of intrinsic motivation (Reeve & Cole, 1987); (2) based on hope theory (Rand & Cheavens, 2009; Snyder, 2002), hope is used to get rewards and has been employed as an indicator of extrinsic motivation. Thus, including both of these emotions allowed us to address multiple user motivation types (both intrinsic and extrinsic) in order to make further knowledge contributions. Specifically, we found that both internal and external attributions—perceived fairness (external) and perceived accuracy (internal)—have positive impacts on focal users’ excitement (Watson et al., 1988) and hope (Lopes, 1987). Furthermore, our findings indicate that these emotions have significant further impacts on users’ willingness to contribute.

Third, we used three outcomes of interest to capture users’ willingness to contribute: (1) willingness to contribute was used to capture the overall possibilities of future content contribution, which we then decomposed into (2) effort—the number of questions users/contributors are willing to answer, and (3) risk preference—choice of risk level, i.e., whether users/contributors are willing to answer questions with potentially higher gains or losses versus questions with lower potential gains and losses. We determined that in most cases, users who receive more positive feedback continue making contributions to the contentsharing platform by answering more questions (effort).

In the context of the above findings, our contribution is threefold. First, to the best of our knowledge, our research is the first to specifically study the mechanisms of the impact of nonverbal peer feedback (i.e., upvotes and downvotes) on user contribution in online content-sharing platforms. Second, we employ attribution theory (Kelley, 1967; Kelley & Michela, 1980) as part of attribution-emotion-action theory (Weiner, 1980) to better understand the mechanisms through which nonverbal peer feedback affects platform users’ contribution levels. Attribution theory has been used in the context of online communities in IS research to understand users’ behaviors regarding identity verification and extrinsic versus intrinsic motivation (Zhao et al., 2016). We posit and show that people inevitably make attributions to process the feedback because nonverbal feedback does not contain explanatory text that can help the recipient understand where they were right or wrong. We therefore motivate the connection between receiving peer feedback and making internal versus external attributions. Attribution-emotion-action theory then helps us to relate the attributions to the focal user’s emotions, in the form of excitement and hope, which then connect to the user’s contribution. This is supported by studies in other contexts, such as educational motivation and attainments as well as performance evaluations in human resource settings (Ho et al., 2017; Owen et al., 2012; Palmeri & Peter, 2019). Our work is novel in the context of online community-based content sharing and thus offers fresh insights into the drivers of user contribution in online content-sharing communities.

Finally, we decompose the user’s general willingness to contribute into two components: effort and risk preference. A user with a greater desire to contribute could do so by either answering more questions of a comparable level of difficulty or choosing more challenging questions to answer, suggesting a higher prospect of gain and a higher risk of loss. We attempt to tease out this nuance in our work. Doing so gives us a richer understanding of the mechanisms by which online community feedback can drive user contribution from two different perspectives.

## 2 Literature Review

Our study builds on the vast literature on the impact of feedback on content contribution in online communities (Table 1). In general, prior studies can be broadly classified based on three dimensions: the source of feedback, the type of feedback, and the valence of feedback. The first dimension relates to the source of feedback. Feedback can be provided either by the platform or by the peers on the platform. In the context of online communities, feedback provided by the platform helps to increase both the content contribution quantity and quality (Huang et al., 2019; Jabr et al., 2014; Zhu et al., 2013). Feedback provided by peers on the same platform also plays a vital role in boosting content contribution in online communities (Mousavi & Zhao, 2022). Using a randomized field experiment, Burtch et al. (2021) showed that peer feedback increases users’ content contribution quantity on Reddit and that such an effect is more pronounced among new community members. Our study focuses on peer feedback rather than platform feedback and tries to examine how platform users perceive feedback from their peers.

Table 1. Selected Research: The Impact of Feedback on Content Contribution

<table><tr><td rowspan="2">Reference</td><td rowspan="2">Source</td><td colspan="3">Feedback/Incentives</td><td colspan="2">Research design</td><td rowspan="2">Main research question</td></tr><tr><td>Type</td><td>Valence</td><td>Theory</td><td>Context</td><td>Methodology</td></tr><tr><td>This study</td><td>Peer</td><td>Nonverbal</td><td>Positive/negative</td><td>Feedback intervention &amp; attribution</td><td>Online communities: Stack Overflow</td><td>Lab experiment</td><td>Causal mechanisms underlying impact of peer feedback on contribution—attribution, emotions</td></tr><tr><td>Burtch et al. (2021)</td><td>Peer</td><td>Nonverbal</td><td>Positive</td><td>Intrinsic motivation</td><td>Online communities: Reddit</td><td>Randomized field experiment</td><td>Impact of peer awards on the contribution</td></tr><tr><td>Wang et al. (2020)</td><td>Platform</td><td>Nonverbal (monetary)</td><td></td><td>Reciprocity &amp; agency theory</td><td>Online communities: Zhihu</td><td>Natural experiment</td><td>The spillover effect of monetary rewards on nonrewarded content creation</td></tr><tr><td>Yu et al. (2020)</td><td>Platform</td><td>Nonverbal (monetary)</td><td></td><td>Cognitive evaluation theory</td><td>Online communities: Restaurant review</td><td>Quasi-experiment</td><td>The impact of monetary performance-contingent rewards on contribution quality, quantity, and valence</td></tr><tr><td>Huang et al. (2019)</td><td>Platform</td><td>Verbal</td><td>Positive</td><td>Social exchange theory</td><td>Online communities: Recipe-sharing</td><td>Randomized field experiment</td><td>The impact of framing (cooperative vs. competitive vs. individual) of feedback on contribution</td></tr><tr><td>Mousavi &amp; Zhao (2022)</td><td>Peer</td><td>Verbal</td><td>Positive/negative</td><td>Social isolation, reciprocity</td><td>Online marketplaces: Short-term rentals</td><td>Archival analysis</td><td>The impact of reciprocal peer feedback revelation timing on contribution quality</td></tr><tr><td>Zhu et al. (2013)</td><td>Platform</td><td>Verbal</td><td>Positive/negative</td><td>Feedback intervention</td><td>Online communities: Wikipedia</td><td>Randomized field experiment</td><td>The impact of verbal feedback on focal task vs. general motivation, on newcomers vs. experienced users</td></tr><tr><td>Moon &amp; Sproull (2008)</td><td>Both</td><td>Verbal</td><td>Positive/negative</td><td>Social identity theory</td><td>Online communities: IT support</td><td>Archival analysis</td><td>The impact of systematic feedback on user contribution</td></tr></table>

The second dimension concerns the type of feedback: verbal or nonverbal. Verbal feedback refers to feedback typically provided in the format of a message. In contrast, nonverbal feedback refers to feedback comprising nontextual information, such as the upvotes/downvotes a user may receive from peers. Prior literature has repeatedly confirmed the positive impact of verbal feedback such as messages (Huang et al., 2019; Moon & Sproull, 2008; Zhu et al., 2013). For example, Huang et al. (2019) examined how the types of peer feedback messages affected users’ contributions to a recipe-sharing platform. They found that feedback emphasizing cooperation is more attractive to women, whereas feedback emphasizing competition is more attractive to men. In contrast, there is little research on the impact of nonverbal feedback. However, Jabr et al. (2014), focusing mainly on positive nonverbal feedback such as voting others’ contributions as helpful and correct, found that such feedback has a positive relationship to the content contribution on IT support online communities. We aim to contribute to this underdeveloped research stream by focusing on both positive and negative nonverbal feedback and exploring the underlying mechanisms through which upvotes and downvotes motivate users to contribute more. The verbal or nonverbal nature of feedback is of crucial importance to our focus on attribution because nonverbal feedback is more susceptible to interpretation and attribution by the recipient due to the lack of explanatory information in the feedback.

Third, the valence of feedback refers to whether the recipient interprets it as being positive or negative. Previous studies have examined how the valence of feedback affects user contribution. Zhu et al. (2013) tested the impacts of negative and positive feedback on members’ contributions and found that positive feedback increases users’ general motivation to contribute content. In contrast, negative feedback increases users’ efforts on focal tasks (i.e., editing the target article on Wikipedia). Our work differs from Zhu et al. (2013) in terms of the nature of the feedback we focus on: we study nonverbal feedback such as upvotes and downvotes, which is different from detailed text-based feedback (Zhu et al., 2013).

Furthermore, although both positive and negative nonverbal feedback is widely used in the form of upvotes and downvotes, we know less about the impact of negative nonverbal feedback. The valence of the feedback—positive versus negative—is crucial to our focus on attribution, as the recipient could attribute positive feedback differently than negative feedback. This motivated us to compare positive and negative nonverbal feedback and understand how they have different effects on user contribution in online communities.

To summarize, our research differs from previous studies in that we focus on (1) feedback that is offered by other users on the same platform, (2) nonverbal feedback that contains less detailed information regarding the contributed content (e.g., about the clarity or helpfulness) than explanatory feedback, and (3) positive (upvotes) as well as negative (downvotes) feedback, with a focus on users’ heterogeneous reactions to these two types of nonverbal feedback. In this context, our focus on nonverbal peer feedback is interesting because, by its very nature, nonverbal feedback requires the recipient to perform an interpretation—which involves making attributions, which can then impact their emotional state and cause them to subsequently on that. Based on the above discussion, it is evident that the underlying mechanism through which nonverbal peer feedback impacts content contributors’ behaviors has not been thoroughly examined. This study addresses this critical research gap by implementing a randomized experiment on the Amazon Mechanical Turk platform to test our hypotheses.

## 3 Theoretical Foundation

To better understand the causal mechanisms, we first posit that verbal and nonverbal feedback are fundamentally different from each other. Verbal feedback, such as feedback messages, tend to give detailed information about things to improve. Nonverbal feedback, such as upvotes and downvotes, merely indicates approval or disapproval of performance with less information provided. To examine the impact of nonverbal peer feedback, we adopt attribution-emotion-action theory, which is wellestablished in the psychology literature (Weiner, 1980).

The present research focuses on nonverbal peer feedback (upvotes, downvotes). It is up to the individual to interpret—through attributions—the nonverbal peer feedback and subsequently act on that. Internal attribution is “one in which the cause of a behavior is internal to an actor,” and external attribution is “one in which the cause is perceived to be situational or environmental” (Calder, 1977). When an anonymous Reddit user or Stack Overflow user upvotes or downvotes an answer, the recipient of the upvote or downvote may attribute the vote (1) internally to their competence, which will likely enhance their selfefficacy and self-confidence (as shown in prior literature), or (2) externally to the peer(s) giving the feedback. Attribution theory has not been used to study nonverbal feedback in previous literature; thus, our paper makes a novel contribution in this regard.

When the user makes an attribution about the feedback they receive, they then transition to an emotional state. Since our focus is on the user’s motivation to make further contributions, we focus on emotions that are relevant to this, i.e., (1) emotions that connect to the task itself—the joy of performing the task—and (2) emotions that pertain to the rewards gleaned from the successful performance of the task. In other words, we focus on emotions associated with intrinsic as well as extrinsic motivation (Davis et al., 1992; Hennessey et al., 2015).

Regarding intrinsic motivation, it is well-established that excitement is a strong indicator of intrinsic motivation (Reeve & Cole, 1987; Reeve et al., 1986). Excitement has been shown to transmit and kindle intrinsic motivation (Patrick et al., 2000). Intrinsic motivation is linked to positive outcomes in a variety of settings and is linked to greater effort and higher intention to expend future effort (Oman & McAuley, 1993). This fits well with the attribution-emotionaction temporal sequence (Weiner, 1980), where emotion leads to action (in our case, future effort on knowledge contribution).

Hope is defined by Rand and Cheavens (2009) as “the perceived capability to derive pathways to desired goals, and motivate oneself via agency thinking to use those pathways” and is strongly associated with goaldirected action. Goals serve as the foundation upon which hope theory is built (Rand & Cheavens, 2009). Feedback can ignite hope (Fong et al., 2016), and hope can serve as a mediator and motivator of action (Wlodarczyk et al., 2017). Higher levels of hope have been consistently related to improved outcomes in academics, athletics, physical health, psychological adjustment, and psychotherapy (Snyder, 2002). Research has also shown that hope leads to greater effort and better-quality solutions; higher levels of hope among management executives are associated with producing more and better quality solutions to work-related problems, indicating that hopefulness may assist employees in overcoming obstacles and problems in the workplace (Peterson & Byron, 2008). In our context, we measure users’ hope in the context of achieving their goal of winning more points in future attempts. In contrast to the excitement associated with intrinsic motivation, since hope is leveraged to obtain rewards, it serves as an indicator of extrinsic motivation.<sup>1</sup>

these emotions to intrinsic and extrinsic motivation. Therefore, we did not include these other emotions in our

## 4 Hypothesis Development

In this paper, we focus on positive and negative nonverbal feedback in the context of online communities. Positive feedback acknowledges the excellent work of a focal user, whereas negative feedback often serves as an admonishment or warning to improve the quality of the contribution. We first consider the impact of feedback valence on knowledge contribution and seek to measure users’ broad willingness to answer questions after receiving positive/negative feedback, including both effort and risk. Users who receive positive feedback are more motivated to work (Zhu et al., 2013) and therefore might expend more effort in terms of the number of questions they are willing to answer, whereas users who receive negative feedback feel less motivated (Halfaker et al., 2011; Zhu et al., 2012).

The importance of effort and risk, arising from the fear of sharing incorrect information (Pillai & Min, 2010) and the fear of being punished due to such mistakes (Davenport & Prusak, 1998), has been recognized in domains such as knowledge sharing and online reviews and in the context of online communities such as Reddit. As Liu et al. (2019) discussed in the context of online reviews, when a user contemplates contributing, the effort involved is costly and carries a risk of failure, which can therefore potentially prevent one from contributing. The contribution is also risky due to the potential for downvotes. Bessi et al. (2016) explore the impact of the risk of receiving “downvotes” on Facebook contributors, highlighting the potential harm to the contributor’s reputation if they make polarizing contributions. Davis and Graham (2021) have noted that “the cumulative ‘karma’ points Reddit users can earn increase with popular (upvoted) content and decrease with unpopular (downvoted) content.” Thus, the potential loss of reputation may discourage users from contributing answers to more challenging questions.

Prior literature has suggested that positive feedback improves perceived self-efficacy (Peifer et al., 2020), which, in turn, promotes risk-taking behaviors (Krueger Jr. & Dickson, 1994). Therefore, we conjecture that after receiving positive (negative) feedback, a user might be willing to expend more (less) effort in contributing and might take on more (less) risk to answer more (less) challenging/rewarding questions. Prior literature has mostly focused on detailed verbal feedback and less attention has been paid to the impact of nonverbal feedback on users’ contribution. Thus, in this research, we focus on nonverbal peer feedback and present the following hypothesis:

H1: Overall, positive nonverbal feedback from peers directly increases users’ willingness to (a) contribute more, (b) expend more effort in contributing, and (c) take higher risks in contributing.

Upon receiving peer feedback, users may form attributions that are perceived as causes of outcomes (Pintrich & Schunk, 2002). In this study, the absence of verbal feedback suggests that recipients are not given clear reasons why they performed well or poorly. Thus, we posit that nonverbal feedback such as upvotes and downvotes, delivered by anonymous community members, leads the recipient to attribute the feedback to internal and/or external reasons. The attribution made by users serves as a critical mediating factor in stimulating their contribution in response to peer feedback (Hsieh & Kang, 2010; Weiner, 2010). Users could attribute peer feedback to internal and/or external factors. A major internal factor is perceived self-efficacy (Bandura, 1990; Krueger Jr. & Dickson, 1994; Salanova et al., 2012; Schunk, 1984). Perceived self-efficacy refers to “an individual’s belief in his or her capacity to execute behaviors necessary to produce specific performance attainments” (Bandura, 1997, p. 604), and it is “perceived” because it is based on the individual’s belief in their capacity (Chen & Zahedi, 2016; Marakas et al., 2007). Thus, we characterize perceived self-efficacy as the result of internal attribution of causality (Salanova et al., 2012) and the perceived fairness of the feedback provider as the result of external attribution.

Positive feedback could be attributed to internal factors— such as perceived self-efficacy (Bandura, 1990). For instance, in education, students gain information about their level of self-efficacy from teachers’ feedback (Schunk, 1984). Thus, we expect positive peer feedback to increase contributors’ self-efficacy by increasing their perceived accuracy of the contribution. Regarding negative feedback, prior studies have identified its significant bearing on perceived fairness in the context of personnel selection (van Vianen et al., 2004). An objective interpersonal treatment has been found to reduce negative dispositional attribution to negative feedback (Leung et al., 2001). However, in online communities, there is often insufficient scope to establish fair interactions between participants. Therefore, negative feedback may be perceived as unfair; conversely, positive feedback may be perceived as fair. Based on the above discussion, we posit the following hypotheses:

H2a: Receiving positive nonverbal peer feedback increases users’ perceived fairness of the feedback.

H2b: Receiving positive nonverbal peer feedback increases users’ perceived self-efficacy.

Emotions are essential drivers of engagement in online contexts (Claffey & Brady, 2019; Schreiner et al., 2021). Emotions, particularly excitement and hope, have been identified as common reactions to positive feedback (Carver & White, 1994; Lovett & Eckert, 2009). Excitement has been associated with greater intrinsic motivation to undertake challenging tasks: prior literature has shown that excitement is an indicator of intrinsic motivation (Reeve et al., 1986). Hope has been linked to increased extrinsic motivation to continue with a task: since hope is a mechanism relied upon by people who wish to stay motivated in working toward an extrinsic reward, it can be used as an indicator of extrinsic motivation (Rand & Cheavens, 2009; Snyder, 2002). Given the focus of our task, we anticipate that users will exhibit greater excitement and hope upon receiving positive nonverbal feedback.

Another relevant stream of research concerns the performance and intensity of emotional reactions and emotional arousal (Fisher, 2008; Malhotra et al., 2008). Positive feedback, which is analogous to winning, can increase the overall emotional intensity and arousal (Verbruggen et al., 2017). Given the risky nature of making contributions, we also draw upon the literature on the psychology of risk (Lopes, 1987) and posit that in addition to excitement, hope will increase as part of emotional arousal. This helps to account for the risky nature of answering questions, which could be either upvoted or downvoted.

Additionally, prior literature has shown that excitement is an indicator of intrinsic motivation (Reeve & Cole, 1987), while hope is used as a motivation to obtain rewards and can be used as an indicator of extrinsic motivation. Thus, including both of these emotions covers users’ motivation types (both intrinsic and extrinsic) and thereby makes further knowledge contributions. Consequently, we anticipate that positive feedback will result in a heightened intensity of emotional reactions among users, specifically in terms of excitement and hope. The following hypotheses capture this notion.

H3: Positive nonverbal peer feedback increases the intensity of users’ emotional reactions, including (a) excitement and (b) hope.

Next, we explore whether internal or external attribution impacts the focal user’s emotion— specifically, whether perceived fairness and perceived self-efficacy impact the focal user’s positive feelings of excitement and hope. Attribution has been found to impact the motivation of participants in educational settings via the mediating mechanisms of emotion (Weiner, 2010). Self-efficacy, emotions, and engagement (Salanova et al., 2011) have been found to be related in the context of education: selfefficacy impacts the emotion (emotional state) of the user, which in turn influences user engagement metrics such as the vigor and dedication of teachers. These prior findings are used to motivate our hypothesis that the user’s attribution, in turn, impacts their emotion. Based on prior literature, beliefs of self-efficacy “reciprocally influence activity engagement indirectly through their impact on positive emotion (enthusiasm, satisfaction, comfort)” (Salanova et al., 2011). In addition, perceived fairness elicits emotional reactions, as seen in the social justice literature (van den Bos et al., 2003) and human resource management literature (Harrington & Lee, 2015). Therefore, we posit the following linkages between internal and external attributions (perceived accuracy and perceived fairness) and the user’s emotion:

H4a: Perceived fairness increases the intensity of users emotional reactions (excitement/hopefulness).

H4b: Perceived self-efficacy increases the intensity of users’ emotional reactions (excitement/ hopefulness).

Finally, we focus on the user’s propensity to contribute, which can be expressed in various ways on platforms like YouTube, Reddit, or Stack Overflow. For example, after receiving nonverbal feedback, users may decide to exert even more effort and answer more questions, or they may get discouraged and reduce the frequency of their contributions. From a strategic perspective, answering more difficult questions may lead to the user gaining more reputation points (on Stack Overflow), karma points (on Reddit), or subscribers (on YouTube) or cause them to risk losing these things. Accordingly, we decompose the propensity to contribute into (1) the willingness to keep contributing, (2) the willingness to expend effort (number of questions a user is willing to answer), and (3) the willingness to take risks (to what extent the user is willing to answer a question with a higher potential gain but also a higher potential loss).

Self-efficacy literature suggests that when people have an increase in their perceived self-efficacy, e.g., when they feel they are more accurate in a task, they should be willing to expend more effort and feel more confident about taking more risks related to the task (Bandura, 1990). In parallel, when people feel that an interaction or procedure is fair, they will feel more committed to an organization and willing to increase their engagement in it (Brockner et al., 1992; Lind & Tyler, 1988). Thus, we propose that both perceived fairness and perceived selfefficacy can directly impact the user’s propensity to contribute. This is captured through the following hypotheses:

H5a: Perceived fairness increases users’ willingness to (i) contribute more, (ii) expend more effort in contributing, and (iii) take higher risks in contributing.

H5b: Perceived self-efficacy increases users’ willingness to (i) contribute more, (ii) expend more effort in contributing, and (iii) take higher risks in contributing.

In addition to the attribution-linked variables, the users’ emotions can also impact their propensity to contribute. The literature on the psychology of risk (Lopes, 1987) suggests that when people feel more hopeful, they tend to take higher risks. As users receive more positive feedback, they are likely to get more excited about the task and feel more hopeful about making impactful contributions. Emotions have also been linked to social contribution (Sun et al., 2017). Positive voting by the community and comments from peers motivate participants to contribute more to the online community (Chen et al., 2019). This is captured through the following hypothesis:

H6: Users’ emotions (excitement/hope) increase their willingness to (a) contribute more, (b) expend more effort in contributing, and (c) take higher risks in contributing.

To summarize, in this study, we focused on how nonverbal feedback from community members affects the focal subject’s engagement behavior outcomes through (1) the focal subject’s attributions of feedback to external factors such as the fairness of evaluations from other subjects (perceived fairness) and to internal factors such as their ability to accurately perform a task requiring knowledge (perceived accuracy), and (2) the focal subject’s emotional states: excited and hopeful, and their effect on (3) outcome variables that capture the subjects’ knowledge contribution. Willingness to contribute measures the intention to continue contributing after receiving nonverbal peer feedback. This overall willingness to contribute may be decomposed into effort and risk. Number of questions measures effort: how many more questions a subject is willing to answer given their performance. Choice of risk level captures a subject’s choice on the risk level they are willing to take in terms of winning or losing points given their performance. Figure 1 presents our research model, with H1 through H6 as indicated.

## 5 The Differences between Verbal and Nonverbal Feedback

Prior studies have mainly focused on the impact of verbal feedback (i.e., reviews, comments) on various business outcomes, such as consumers’ purchase intentions (Jiménez & Mendoza, 2013; Vana & Lambrecht, 2021), user engagement (Huang et al., 2019; Zhu et al., 2013), product sales and revenue (Chevalier & Mayzlin, 2006; Li & Hitt, 2008; Zhu & Zhang, 2010), etc. Besides verbal feedback, nonverbal feedback (i.e., upvotes, downvotes, helpful votes, etc.) has been adopted by multiple platforms, with relatively few studies examining its impact (Chen et al., 2018). Before we dive into details and analyze the effects of nonverbal feedback, we must first address a fundamental question: whether and how nonverbal feedback differs from verbal feedback in terms of its impact on knowledge contribution. We propose an experimental study to answer this question.

To abstract away from the specifics of any particular context, we chose a simple task in the context of a game called “Spot the Ball,” which was broadly familiar to our participants. Participants were shown a series of photographs of ongoing soccer matches, with various players nearby trying to engage with the ball, but with the ball removed. They were asked to guess where the ball might be. Since soccer is a widely known and played game, we could expect that our participants would be able to make an appropriate guess as to where the missing ball might be. This task does not perfectly mimic content sharing or knowledge sharing in any particular forum but is intended to be a simple representative task that can capture the essential aspects of the issue being studied—the differences between verbal and nonverbal feedback. Similar tasks have been studied in the context of goal literature (Gunasti & Ozcan, 2019). Soccer has been used as a representative context in prior experimental work on decision-making and judgment under uncertainty (e.g., Sonneman et al., 2013; Tannenbaum et al., 2017).

![](/api/attachments/EG88MYBZ/fulltext/images/db7ab1d1f3cec388c6b5ddda631af8fab43c205bb6784c8191bd4dc11afadae1.jpg)  
Figure 1. Research Model

Table 2. Descriptive Statistics for Study 1

<table><tr><td rowspan="2"></td><td></td><td>Overall mean</td><td>Verbal-positive</td><td>Verbal-negative</td><td>Nonverbal-positive</td><td>Nonverbal-negative</td><td colspan="2">ANOVA</td></tr><tr><td>Range</td><td>(n = 248)</td><td>(n = 62)</td><td>(n = 62)</td><td>(n = 60)</td><td>(n = 64)</td><td>F</td><td>P</td></tr><tr><td>Gender</td><td>1 - 3</td><td>1.407</td><td>1.387</td><td>1.403</td><td>1.433</td><td>1.406</td><td>0.086</td><td>0.968</td></tr><tr><td>Age</td><td>1 - 9</td><td>3.399</td><td>3.306</td><td>3.290</td><td>3.517</td><td>3.484</td><td>0.943</td><td>0.421</td></tr><tr><td>Education</td><td>1 - 7</td><td>5.185</td><td>5.194</td><td>5.242</td><td>5.150</td><td>5.156</td><td>0.219</td><td>0.883</td></tr><tr><td>Avg. risk attitude</td><td>1 - 5</td><td>3.355</td><td>3.269</td><td>3.309</td><td>3.456</td><td>3.388</td><td>0.745</td><td>0.526</td></tr></table>

## 6 Study 1

## 6.1 Method

For our study, we recruited 275 mTurk workers (mTurkers) residing in the US. Our final data sample consisted of 248 participants (39.1% female, 62.9% between 25 and 34 years old, with 94.4% having a 4- year college degree or more) who passed our attention checks, completed the study, and received a nominal payment for their participation. As shown in Table 2, there was no significant difference across our treatments in terms of gender, age, education level, and risk attitude, which suggests that all participants were randomly assigned to our treatment groups. Participants were randomly assigned to four conditions in a 2×2 between-subjects design, with two levels of feedback: verbal vs. nonverbal (our treatment of interest) and two levels of feedback momentum: more positive vs. more negative. To mimic the dynamics of online communities where feedback is given, such as online Q&A platforms<sup>2</sup> where users answer each other’s questions, we led participants to believe that some of them (“contributors”) would be providing advice to others (“players”) by trying to guess the position of the ball. The participants were told that the players would then play according to their advice, assess the accuracy of the advice, and evaluate the contributors’ answers in terms of how accurate they were. In reality, all participants were in the “contributor” group and were trying to guess the position of the ball. While we led them to believe that the feedback they were getting was from other community members supposedly playing the game, in actuality, we provided all the feedback, both verbal and nonverbal, and controlled who got positive or negative feedback for each contribution.

Study 1 had three stages: (1) initial assessment and practice, (2) main task involving contributions of answers (guesses) of where the ball might be in the various images being shown, and (3) measures of willingness, effort, and risk-taking regarding future contributions. The first stage had two sample questions to help familiarize participants with the game and to create an initial assessment of their abilities. The second stage contained four questions to manipulate the feedback momentum (more positive vs. more negative). Participants answered four questions in a sequence and were given feedback at the end of each answer, in the form of verbal (“Your answer is correct/wrong.”) or nonverbal (upvote or downvote) feedback. The third stage is when participants revealed (1) their willingness to contribute to the game—“Do you feel like continuing to answer questions?,” (2) the number of questions (effort) they were willing to answer—“How many more questions do you feel like answering? Scale of 1-10,” and (3) their choice of risk level—players were allowed to choose among four questions with varying risk levels and potential points for wins or losses. Appendix A provides the details of our experiment design for Study 1.

## 6.2 Results

We commenced with a model-free plot illustrating the mean values of our three dependent variables: willingness to contribute, number of questions, and choice of risk level, under the 2×2 condition (verbal vs. nonverbal and positive vs. negative feedback), as depicted in Figure 2. Our observations suggest that verbal feedback may engender a heightened willingness to contribute and an increased number of questions. However, this distinction appears to be evident primarily with negative feedback. More specifically, the type of feedback (verbal or nonverbal) seems to have had little difference in terms of the willingness to contribute or number of questions when the feedback was positive. In contrast, when the feedback was negative, nonverbal cues may have contributed to the more significant reduction in terms of both willingness to contribute and number of questions. This could have been due to the more explicit nature of verbal feedback, which provides additional context and explanation, thereby making negative criticism easier to digest for recipients. Regarding the third dependent variable, choice of risk level, nonverbal feedback appears to have stimulated a higher level of risk-taking. This pattern remained consistent regardless of whether the feedback was positive or negative.

![](/api/attachments/EG88MYBZ/fulltext/images/43e61e18e0e8d30f4e69e9c214c69301df61c107b703f881322db1ea162a702d.jpg)  
Feedback Type  
Figure 2. The Average Dependent Variables

Table 3. t-test Results of Verbal vs. Nonverbal

<table><tr><td>Feedback</td><td>Willingness to contribute</td><td>Number of questions</td><td>Choice of risk level</td><td>Obs.</td></tr><tr><td>Verbal</td><td>4.315</td><td>7.040</td><td>2.710</td><td>124</td></tr><tr><td>Nonverbal</td><td>4.097</td><td>6.444</td><td>3.016</td><td>124</td></tr><tr><td>Ver - non</td><td>0.218**</td><td>0.597**</td><td>-0.387**</td><td></td></tr></table>

The model-free plot delineates the overarching pattern of the results of this experiment. To supplement these findings with statistical inference, we followed a two-step process: (1) we first presented the results of t-tests to understand how verbal and nonverbal feedback affected the three outcome variables, willingness to contribute, number of questions, and choice of risk level, (2) then we examined the role of the momentum of feedback (more positive vs. more negative).

The three t-test results presented in Table 3 elucidate significant discrepancies between the impacts of verbal and nonverbal feedback on all three dependent variables: willingness to contribute, number of questions, and choice of risk level. Verbal feedback, in contrast to nonverbal feedback, seems to engender a greater willingness to contribute and a higher motivation to answer questions. Conversely, nonverbal feedback appears to catalyze more risk-taking behavior—users seemed to be more inclined to embrace challenges when answering questions. These findings align with our inferences derived from the model-free plot.

Our findings in Study 1 support that by providing specific and detailed evaluations of users’ contributions, verbal feedback enhances their willingness to contribute and incentivizes them to answer more questions. We believe that this occurs because verbal feedback offers users a more profound understanding of their performance, which subsequently informs future contributions. As visualized in the model-free plot, nonverbal feedback— particularly when expressing negative sentiments solely through downvotes—provides only a general disapproval devoid of justification. This type of feedback tended to diminish users’ willingness to contribute and their motivation to answer questions, compared to negative verbal feedback. Our subsequent experiment will probe deeper into the dynamics underlying such negative nonverbal feedback.

Interestingly, the absence of specific feedback in nonverbal cues might also stimulate users’ willingness to experiment and take risks, as they navigate various strategies to discern what succeeds and what fails, ultimately leading to more risk-taking behaviors. In contrast, verbal feedback provides more specific evaluations that foster a clearer understanding of the appropriate approach, guiding users toward behaviors that entail less risk.

We ran two subgroup analyses on verbal and nonverbal feedback, respectively, and examined the role of the momentum of feedback (more positive vs. more negative). For the verbal feedback, the t-test results (shown in Table 4) prove that there is only one significant difference in the choice of risk level between positive and negative feedback. Positive feedback led to a significantly higher choice of risk level when the feedback was verbal.

Regarding nonverbal feedback, our t-test results (presented in Table 5) demonstrate significant differences in all three dependent variables— willingness to contribute, number of questions, and choice of risk level—between positive and negative feedback. Users who received positive nonverbal feedback were more willing to contribute and were more likely to answer more questions and to answer more challenging questions with higher risk.

Table 4. t-test Results of Positive vs. Negative for Verbal Feedback

<table><tr><td>Feedback</td><td>Willingness to contribute</td><td>Number of questions</td><td>Choice of risk level</td><td>Obs.</td></tr><tr><td>Pos</td><td>4.355</td><td>7.226</td><td>2.952</td><td>62</td></tr><tr><td>Neg</td><td>4.274</td><td>6.855</td><td>2.468</td><td>62</td></tr><tr><td>Pos - Neg</td><td>0.081</td><td>0.371</td><td>0.484**</td><td></td></tr><tr><td colspan="5">Note: *** p &lt; 0.01, ** p &lt; 0.05, * p &lt; 0.1</td></tr></table>

Table 5. t-test Results of Positive vs. Negative for Nonverbal Feedback

<table><tr><td>Feedback</td><td>Willingness to contribute</td><td>Number of questions</td><td>Choice of risk level</td><td>Obs.</td></tr><tr><td>Pos</td><td>4.433</td><td>6.933</td><td>3.217</td><td>60</td></tr><tr><td>Neg</td><td>3.781</td><td>5.984</td><td>2.828</td><td>64</td></tr><tr><td>Pos - Neg</td><td>0.652***</td><td>0.949**</td><td>0.389*</td><td></td></tr><tr><td colspan="5">Notes: *** p &lt; 0.01, ** p &lt; 0.05, * p &lt; 0.1</td></tr></table>

Thus, Study 1 helped us to demonstrate how nonverbal feedback differs from verbal feedback. Specifically, the impacts of verbal and nonverbal feedback on user knowledge contribution are different in terms of willingness to contribute, number of questions, and choice of risk level. Verbal feedback enhanced users’ willingness to contribute and prompted them to respond to a greater number of questions. On the other hand, nonverbal feedback encouraged users to engage more frequently in risk-taking behavior when answering questions. Furthermore, regarding the role of feedback momentum (more positive vs. more negative), the positive momentum had a significant impact when users received nonverbal feedback. Based on the above discussion, we will dive deeply into nonverbal feedback in our subsequent Study 2 and explore the underlying mechanisms for how nonverbal feedback motivates users to contribute more knowledge.

## 7 Study 2: Nonverbal Peer Feedback and Knowledge Contribution and Mechanisms

In our second study, we first focused on the causal relationship between the nonverbal peer feedback (upvotes and downvotes) and individuals’ engagement in knowledge contribution, such as the willingness to contribute, the number of questions the user is willing to answer (effort), and the choice of risk level (i.e., choice of questions with higher/lower levels of point gains and point losses). Then, we further explored the underlying mechanisms behind this, in terms of the mediating role of perceived fairness and perceived accuracy and the emotional states such as being excited and hopeful about the challenge ahead.

## 7.1 Method

For Study 2, 223 mTurkers residing in the US participated. Our ultimate sample consisted of 197 participants (39.6% female, 40.1% between 25 and 34 years old, 82.3% with a 4-year college degree or more)

who passed our attention checks and received a nominal payment for their participation. As shown in Table 6, no significant difference was detected across treatments in terms of gender, age, education level, and risk attitude, suggesting a successful random assignment of participants.

mediating role of perceived fairness and perceived accuracy and the emotional states of being excited and hopeful. Appendix B provides the details of our experiment design for Study 2.

Our Study 2 had three stages: (1) initial assessment and practice, (2) main task involving contributions of answers (guesses) of where the ball might be in the various images being shown, and (3) measures of willingness, effort, and risk-taking with regard to future contributions. The first stage had two sample questions to help familiarize participants with the game and to create an initial assessment of their abilities. All participants were told that based on their answers they would receive some points and they received 800 points to start with. It was clarified that these points would be assigned by the system based on an evaluation of the accuracy of their answers (i.e., evaluation by the system rather than by peers). Everyone got the same number of points (800 points), but (1) each participant only knew how many points they had, and (2) we manipulated the framing of these points to be high or low by informing participants that their scores were at the top 20% or bottom 20% of the whole group. This allowed us to frame the participants’ perceptions of their self-efficacy while keeping the points numerically identical in order to control for any number-specific framing effects. The goal here was to establish a baseline of points for the users, as awarded by the impersonal platform rather than by other participants. We wanted to control for this baseline perception among users, and its possible effect on their subsequent reactions to peer feedback. To some extent, this mirrors the reputation points that a user has at any given time on knowledge-sharing platforms, such as Stack Overflow and Reddit.

Table 6. Descriptive Statistics for the Experiment

<table><tr><td rowspan="2"></td><td></td><td>Overall mean</td><td>Upvotes high score</td><td>Upvotes low score</td><td>Downvotes high score</td><td>Downvotes low score</td><td colspan="2">ANOVA</td></tr><tr><td>Range</td><td>(n = 197)</td><td>(n = 54)</td><td>(n = 48)</td><td>(n = 49)</td><td>(n = 46)</td><td>F</td><td>P</td></tr><tr><td>Gender</td><td>1 - 3</td><td>1.416</td><td>1.444</td><td>1.417</td><td>1.347</td><td>1.457</td><td>0.153</td><td>0.696</td></tr><tr><td>Age</td><td>1 - 9</td><td>3.977</td><td>4.037</td><td>3.750</td><td>4.122</td><td>4.000</td><td>1.221</td><td>0.271</td></tr><tr><td>Education</td><td>1 - 7</td><td>4.847</td><td>4.889</td><td>4.833</td><td>4.776</td><td>4.891</td><td>0.041</td><td>0.840</td></tr><tr><td>Avg. risk attitude</td><td>1 - 5</td><td>3.019</td><td>2.988</td><td>2.962</td><td>3.099</td><td>3.029</td><td>0.422</td><td>0.517</td></tr></table>

Participants were randomly assigned to four conditions in a 2×2 between-subjects design, with two levels of nonverbal peer feedback: more upvotes vs. more downvotes, and two levels of initial score: high vs. low—assigned by the “system” as a baseline—in contrast to subsequent scores that were assigned by peers. To ensure consistency, we adopted the majority of the design of Study 1 and continuously used the online guessing game where participants were shown pictures of a soccer game with the ball removed and had to guess the actual location of the ball. To further understand the underlying mechanism behind nonverbal peer feedback and user engagement, more questions were added in Study 2 to investigate the

The second stage contains six questions<sup>3</sup> to manipulate the nonverbal peer feedback momentum (more upvotes vs. more downvotes), where participants helped others by evaluating the submitted answers and assigning upvotes or downvotes based on the accuracy of their answers. The goal here was to give participants the impression that other peer members (rather than the impersonal platform as in the earlier case) were evaluating them and upvoting/downvoting them. This was done to mimic nonverbal peer feedback mechanics used on typical online community forums, such as Stack Overflow.

The third stage is when participants revealed (1) their willingness to contribute to the game—“Do you feel like continuing to answer questions?,” (2) the number of questions (effort) they were willing to answer— “How many more questions do you feel like answering? Scale of 1-10,” and (3) their choice of risk—players were allowed to choose among four questions with varying risk levels and potential points for wins or losses (see Appendix B for details).

Finally, we measured (1) participants’ perceived fairness regarding the process (“Do you feel that you have been fairly evaluated by other participants?”), (2) their perceived accuracy (“Do you think you can accurately find the soccer ball position?”), and (3) their emotional states in terms of being excited (“How excited are you about the challenge level of this game?”), and hopeful (“How hopeful are you about winning more points if we continue the game?”) on 5- point scales (1- not at all, 5- very).

## 7.2 Results

We present our findings in the following sequence: First, we first show the result of univariate analysis of variance to understand which factor(s) affect the outcomes of interest. Then, we then dive deeper to understand how people attribute nonverbal peer feedback (internally or externally). Finally, we test a serial mediation model to examine the mediating roles of perceived accuracy and fairness along with the emotional responses for the effects of nonverbal peer feedback on behavior outcomes.

The univariate analysis results (presented in Table 7) show that only positive nonverbal peer feedback affects participants’ willingness to contribute and the number of questions they are willing to answer. The participants’ baseline score level did not affect the outcomes of interest.

Internal vs. external attribution: A mixed ANOVA was conducted; the two types of nonverbal peer feedback (upvotes, downvotes) served as the betweensubjects factor, whereas internal attribution: (perceived accuracy) and external attribution (perceived fairness) served as the repeated measures factor. When participants were downvoted, their perceived accuracy (internal attribution) decreased relative to when they were upvoted (which is as expected), but their perceived fairness (external attribution) decreased by about twice as much, which is interesting. Table 8 presents the detailed estimation results. There is a significant interaction between attribution and feedback (F (1,219) = 7.86, p = 0.005).

Table 7. Univariate Analysis of Variance

<table><tr><td></td><td>Willingness to contribute</td><td>Number of questions</td><td>Choice of risk</td></tr><tr><td>Baseline points</td><td>1.020</td><td>0.020</td><td>3.165</td></tr><tr><td>Nonverbal peer feedback</td><td>24.189***</td><td>5.828*</td><td>0.061</td></tr><tr><td>Interaction</td><td>0.168</td><td>0.275</td><td>0.885</td></tr><tr><td colspan="4">Note: F-statistics are reported in this table, * p&lt;0.05; ** p&lt;0.01; *** p&lt;0.001.</td></tr></table>

Table 8. ANOVA - Attribution

<table><tr><td></td><td>Mediators</td><td>Mean</td><td>SE</td></tr><tr><td rowspan="2">UPVOTED</td><td>Perceived accuracy (internal attribution)</td><td>3.99</td><td>.090</td></tr><tr><td>Perceived fairness (external attribution)</td><td>4.14</td><td>.097</td></tr><tr><td rowspan="2">DOWNVOTED</td><td>Perceived accuracy (internal attribution)</td><td>3.48</td><td>.093</td></tr><tr><td>Perceived fairness (external attribution)</td><td>3.18</td><td>.100</td></tr></table>

When there were more downvotes, users felt that they were less accurate in absolute terms but more accurate relative to perceived fairness, which was perceived to be less fair, i.e., they had more negative external attribution $( M _ { \mathrm { { A c c } } } = 3 . 4 8$ vs. $M _ { \mathrm { F a i r } } = 3 . 1 8 ,$ , F (1,219) = 6.82, $p ~ = ~ . 0 1 )$ . However, when there were more upvotes, users’ ratings of the fairness of the peer feedback were not significantly different from their perceptions of accuracy $( M _ { \mathrm { A c c } } = 3 . 9 9 ~ \mathrm { v s . } ~ M _ { \mathrm { F a i r } } = 4 . 1 4 $ $F \left( 1 , 2 1 9 \right) = 1 . 7 8 , p > 0 . 1 )$ . Thus, Table 8 suggests that users attribute upvotes internally to their accuracy as well as externally to others’ fairness, whereas they attribute downvotes primarily externally to the lack of fairness in the peer evaluations they receive, though their internal attribution to accuracy decreases somewhat as well.

Next, we tested a serial mediation model to examine the mediating roles of perceived accuracy and fairness along with the emotional responses for the effects of nonverbal peer feedback on behavior outcomes (see Figure 1 for all paths tested). We used the Process Macro in SPSS by (Hayes 2018) to estimate our models. Furthermore, we reviewed the models for each of the two emotional states (excited and hopeful) and for each of the three outcome variables (willingness to contribute, number of questions, and choice of risk).

Excited as the emotional state mediator: The model that used Excited as the emotional state (emotional affect) mediator is summarized in Table 9a. The positive significant coefficients of nonverbal Peer feedback indicate that upvotes helped to increase perceived fairness and perceived accuracy. When participants received positive nonverbal peer feedback such as upvotes, they felt that they were being fairly evaluated by other users and that they could accurately guess the ball position. Our findings show that perceived fairness and perceived accuracy had both direct and indirect impacts on the outcome variables, such as willingness to contribute and number of questions to answer: Participants who felt they were being fairly treated and believed they could accurately pinpoint the ball position, were more willing to contribute knowledge by answering more questions. Furthermore, the impacts of perceived fairness and perceived accuracy on the outcomes were also mediated by excited: Participants with high perceptions of fairness and accuracy tended to be more excited about the game, which in turn led to a higher likelihood of contributing, a greater willingness to answer more questions (effort), and a lower likelihood of answering questions with more points to lose (lower risk-taking). In addition, we found that positive nonverbal peer feedback (upvotes) had a significant negative direct impact on the emotional state of excited, suggesting that participants’ level of excitement decreased when they received upvotes, after controlling for the impact of perceived fairness and accuracy (by itself, i.e., without controlling for perceived fairness and perceived accuracy, excited is positively linked to the number of upvotes).

We tested the direct relationship between nonverbal peer feedback and engagement behavior outcomes but found no evidence for it. Then, we tested the indirect effect; the results are summarized in Table 9b. The results show a significant indirect effect of nonverbal peer feedback on the willingness to contribute through (1) perceived fairness only (b = 0.401, 95% confidence interval (CI): 0.207 \~ 0.601); (2) excited only (b = ̵ 0.101, 95% CI: ̵ 0.211 \~ ̵ 0.021); (3) both perceived fairness and excited (b = 0.151, 95% CI: 0.063 \~ 0.270). The indirect effects of (1) and (3) are positive whereas the indirect effect of (2) is negative. However, as shown in Table 9b, the total indirect effect of nonverbal peer feedback on willingness to contribute is significant and positive (b = 0.561, 95% CI: 0.292 \~ 0.870).

Table 9a. Estimation Results for “Excited” as Mediator

<table><tr><td></td><td>Perceived fairness</td><td>Perceived accuracy</td><td>Excited</td><td>Willingness To contribute</td><td>Number of questions</td><td>Choice of risk</td></tr><tr><td>Constant</td><td>3.185***(0.099)</td><td>3.482***(0.093)</td><td>-0.164(0.325)</td><td>0.758***(0.240)</td><td>-0.987(0.654)</td><td>3.303***(0.345)</td></tr><tr><td>Nonverbal peer feedback</td><td>0.954***(0.139)</td><td>0.510***(0.129)</td><td>-0.421*(0.163)</td><td>0.016(0.122)</td><td>-0.129(0.333)</td><td>0.131(0.176)</td></tr><tr><td>Perceived fairness</td><td></td><td></td><td>0.661***(0.075)</td><td>0.420***(0.064)</td><td>0.525**(0.176)</td><td>-0.191*(0.093)</td></tr><tr><td>Perceived accuracy</td><td></td><td></td><td>0.318*(0.081)</td><td>0.141*(0.061)</td><td>0.383*(0.167)</td><td>0.160(0.088)</td></tr><tr><td>Excited</td><td></td><td></td><td></td><td>0.239***(0.050)</td><td>1.043***(0.136)</td><td>-0.192**(0.072)</td></tr><tr><td colspan="7">Note: Standard errors are in parentheses. * p&lt;0.05; ** p&lt;0.01; *** p&lt;0.001</td></tr></table>

Table 9b. Indirect Effect of Nonverbal Peer Feedback (“Excited” as Mediator)

<table><tr><td></td><td colspan="3">Willingness to contribute</td><td colspan="3">Number of questions</td><td colspan="3">Choice risk</td></tr><tr><td></td><td>b</td><td>LLCI</td><td>ULCI</td><td>b</td><td>LLCI</td><td>ULCI</td><td>b</td><td>LLCI</td><td>ULCI</td></tr><tr><td>Total</td><td>0.561</td><td>0.327</td><td>0.806</td><td>1.083</td><td>0.442</td><td>1.715</td><td>-0.172</td><td>-0.376</td><td>0.006</td></tr><tr><td>Ind1</td><td>0.401</td><td>0.207</td><td>0.601</td><td>0.500</td><td>0.127</td><td>0.888</td><td>-0.182</td><td>-0.387</td><td>-0.007</td></tr><tr><td>Ind2</td><td>0.072</td><td>-0.001</td><td>0.169</td><td>0.195</td><td>0.011</td><td>0.430</td><td>0.082</td><td>0.004</td><td>0.187</td></tr><tr><td>Ind3</td><td>-0.101</td><td>-0.211</td><td>-0.021</td><td>-0.439</td><td>-0.840</td><td>-0.099</td><td>0.081</td><td>0.013</td><td>0.164</td></tr><tr><td>Ind4</td><td>0.151</td><td>0.063</td><td>0.270</td><td>0.658</td><td>0.361</td><td>1.024</td><td>-0.121</td><td>-0.236</td><td>-0.028</td></tr><tr><td>Ind5</td><td>0.039</td><td>-0.011</td><td>0.088</td><td>0.169</td><td>0.054</td><td>0.344</td><td>-0.031</td><td>-0.070</td><td>-0.006</td></tr><tr><td>Ind1</td><td colspan="9">Nonverbal peer feedback → Fairness → Outcomes</td></tr><tr><td>Ind2</td><td colspan="9">Nonverbal peer feedback → Accuracy → Outcomes</td></tr><tr><td>Ind3</td><td colspan="9">Nonverbal peer feedback → Excited → Outcomes</td></tr><tr><td>Ind4</td><td colspan="9">Nonverbal peer feedback → Fairness →Excited → Outcomes</td></tr><tr><td>Ind5</td><td colspan="9">Nonverbal peer feedback → Accuracy → Excited → Outcomes</td></tr><tr><td colspan="10">Note: Ind stands for the indirect path effect. LLCI/ULCI: Lower/upper levels of 95% confidence interval. Bolded numbers refer to significant indirect paths.</td></tr></table>

Similarly, nonverbal peer feedback has a significant positive indirect effect on the number of questions through perceived fairness, perceived accuracy, and excited. Thus, we conclude that subjects with positive nonverbal peer feedback are more likely to continue the game and answer more questions, mainly because they think they have been fairly judged by their peers (perceived fairness), they have higher perceived selfefficacy (perceived accuracy), and they feel very excited about the game.

Hopeful as the emotional state mediator: The other emotional state mediator is hopeful, and we present its estimation results in Table 10a. The results are consistent with the case where excited is used as the mediator. We observe that nonverbal peer feedback had positive and significant impacts on perceived fairness and perceived accuracy, which then had positive direct impacts on the outcome variables or indirect impacts through hopeful.

We conclude that compared to subjects who are downvoted, subjects who receive upvotes perceive that they are being evaluated more fairly and can position the ball more accurately, which then makes them have greater hope in terms of winning the game. Furthermore, when subjects have higher perceived fairness and perceived accuracy, they are more likely to continue the game and answer more questions.

Using hopeful as a mediator, a direct relationship between nonverbal peer feedback and the engagement behavior outcomes is still lacking. However, we did observe significant indirect effects, which are summarized in Table 10b. Our findings indicate that nonverbal peer feedback has positive indirect effects on willingness to contribute through (1) perceived fairness (b = 0.404, 95% CI: 0.228 \~ 0.614); (2) hopeful (b = ̵ 0.125, 95% CI: ̵ 0.231 \~ ̵ 0.038); (3) both perceived fairness and hopeful (b = 0.148, 95% CI: 0.062 \~ 0.253); and (4) both perceived accuracy and hopeful (b = 0.045, 95% CI: 0.013 \~ 0.099). Similarly, nonverbal peer feedback has a significant positive indirect effect on the number of questions through perceived fairness, perceived accuracy, and hopeful. All the findings are presented in Figure 3 for better visualization.

Table 10a. Estimation Results for “Hopeful” as Mediator

<table><tr><td></td><td>Perceived fairness</td><td>Perceived accuracy</td><td>Hopeful</td><td>Willingness To contribute</td><td>Number of questions</td><td>Choice of risk</td></tr><tr><td>Constant</td><td>3.185 ***(0.099)</td><td>3.482***(0.093)</td><td>0.711*(0.283)</td><td>0.507*(0.241)</td><td>-1.695*(0.715)</td><td>3.369***(0.355)</td></tr><tr><td>Nonverbal peer feedback</td><td>0.954***(0.139)</td><td>0.510***(0.129)</td><td>-0.420**(0.142)</td><td>0.183(0.122)</td><td>-0.252 (0.361)</td><td>0.192(0.179)</td></tr><tr><td>Perceived fairness</td><td></td><td></td><td>0.522***(0.065)</td><td>0.423***(0.062)</td><td>0.820***(0.185)</td><td>-0.292**(0.092)</td></tr><tr><td>Perceived accuracy</td><td></td><td></td><td>0.293***(0.070)</td><td>0.129*(0.061)</td><td>0.492**(0.181)</td><td>0.114(0.090)</td></tr><tr><td>Hopeful</td><td></td><td></td><td></td><td>0.297***(0.057)</td><td>0.755***(0.168)</td><td>-0.049(0.084)</td></tr><tr><td colspan="7">Note: Standard errors are in parentheses. * p&lt;0.05; ** p&lt;0.01; *** p&lt;0.001.</td></tr></table>

Table 10b. Indirect Effect of Nonverbal Peer Feedback (“Hopeful” as Mediator)

<table><tr><td rowspan="2"></td><td colspan="3">Willingness to contribute</td><td colspan="3">Number of questions</td><td colspan="3">Choice risk</td></tr><tr><td>b</td><td>LLCI</td><td>ULCI</td><td>b</td><td>LLCI</td><td>ULCI</td><td>b</td><td>LLCI</td><td>ULCI</td></tr><tr><td>Total</td><td>0.537</td><td>0.301</td><td>0.785</td><td>1.205</td><td>0.650</td><td>1.784</td><td>-0.232</td><td>-0.432</td><td>-0.050</td></tr><tr><td>Ind1</td><td>0.404</td><td>0.228</td><td>0.614</td><td>0.782</td><td>0.405</td><td>1.204</td><td>-0.279</td><td>-0.482</td><td>-0.102</td></tr><tr><td>Ind2</td><td>0.066</td><td>-0.004</td><td>0.160</td><td>0.251</td><td>0.055</td><td>0.509</td><td>0.058</td><td>-0.027</td><td>0.163</td></tr><tr><td>Ind3</td><td>-0.125</td><td>-0.231</td><td>-0.038</td><td>-0.317</td><td>-0.610</td><td>-0.095</td><td>0.021</td><td>-0.050</td><td>0.090</td></tr><tr><td>Ind4</td><td>0.148</td><td>0.062</td><td>0.253</td><td>0.376</td><td>0.167</td><td>0.653</td><td>-0.024</td><td>-0.111</td><td>0.052</td></tr><tr><td>Ind5</td><td>0.045</td><td>0.013</td><td>0.099</td><td>0.113</td><td>0.033</td><td>0.243</td><td>-0.007</td><td>-0.034</td><td>0.019</td></tr><tr><td>Ind1</td><td colspan="9">Nonverbal peer feedback → Fairness → Outcomes</td></tr><tr><td>Ind2</td><td colspan="9">Nonverbal peer feedback → Accuracy → Outcomes</td></tr><tr><td>Ind3</td><td colspan="9">Nonverbal peer feedback → Hopeful → Outcomes</td></tr><tr><td>Ind4</td><td colspan="9">Nonverbal peer feedback → Fairness → Hopeful → Outcomes</td></tr><tr><td>Ind5</td><td colspan="9">Nonverbal peer feedback → Accuracy → Hopeful → Outcomes</td></tr><tr><td colspan="10">Note: Ind stands for the Indirect path effect. LLCI/ULCI: Lower/Upper levels of 95% confidence interval. Bolded numbers refer to significant indirect paths.</td></tr></table>

![](/api/attachments/EG88MYBZ/fulltext/images/f2d0af1e871bc643077803aa6b0be182b872245ef7104d8d359f2bfb31329eac.jpg)  
Figure 3. Experiment Results Summary

Table 11. Hypotheses Testing Summary

<table><tr><td>Hypothesis</td><td>Findings</td></tr><tr><td>H1: Overall, positive nonverbal feedback from peers directly increases users&#x27; willingness to (a) contribute more, (b) expend more effort in contributing, and (c) take higher risks in contributing.</td><td>Not supported</td></tr><tr><td>H2a: Positive nonverbal peer feedback increases users&#x27; perceived fairness of the feedback.H2b: Positive nonverbal peer feedback increases users&#x27; perceived self-efficacy in the form of their perceived accuracy.</td><td>Supported</td></tr><tr><td>H3: Positive nonverbal peer feedback increases the intensity of users&#x27; emotional reactions (excitement/hopefulness).</td><td>Not supported</td></tr><tr><td>H4a: The perceived fairness increases the intensity of users&#x27; emotional reactions (excitement/hopefulness).H4b: The perceived accuracy increases the intensity of users&#x27; emotional reactions (excitement/hopefulness).</td><td>Supported</td></tr><tr><td>H5a: The perceived fairness increases users&#x27; willingness to (i) contribute more, (ii) expend more effort in contributing, and (iii) take higher risks in contributing.H5b: The perceived accuracy increases users&#x27; willingness to (i) contribute more, (ii) expend more effort in contributing, and (iii) take higher risks in contributing.</td><td>Supported for outcomes (i) and (ii)</td></tr><tr><td>H6: The intensity of users&#x27; emotional reactions (excitement/hopefulness) positively influences their willingness to (a) contribute more, (b) expend more effort in contributing, and (c) take higher risk in contributing</td><td>Supported for excited and hopeful for outcomes (a) and (b)</td></tr></table>

Study 2 helped us test our hypotheses regarding nonverbal peer feedback and knowledge contribution activities. A brief summary is presented in Table 11. We provide a detailed discussion below on whether our hypotheses are supported or not based on our experiment results. First, we did not find any significant direct impact of nonverbal peer feedback on contribution outcomes—willingness to contribute, effort (number of questions willing to contribute), or choice of risk. Thus, H1 is not supported. Second, there appears to be support for H2a and H2b: as shown in Table 8, upvotes (compared to downvotes) lead to significantly greater perceived fairness and perceived accuracy. The difference in the perceived fairness is higher than (about twice) the difference in the perceived accuracy. Upvoted participants made external and internal attributions that were about the same (i.e., the similar extent of perceived fairness and accuracy).

However, though both perceived fairness and perceived accuracy decreased, downvoted participants appear to have attributed their downvotes significantly more to a lack of perceived fairness than a lack of perceived accuracy. In the estimation results reported in Tables 9a and 10a, nonverbal peer feedback is shown to have a positive impact on perceived fairness as well as perceived accuracy. The effect is greater on the perceived fairness, which is consistent with the results from Table 8 discussed above.

Third, H3—the direct effect of positive nonverbal feedback on users’ emotional reaction—is not supported because after controlling for perceived fairness and accuracy, nonverbal peer feedback appears to have statistically significant and negative impacts on both excitement and hope. Fourth, our findings indicate that perceived fairness and perceived accuracy have positive and highly significant impacts on excitement and hopefulness. Therefore, H4 is supported. This finding suggests that in general, if participants (1) perceived others to be fair, and/or (2) perceived themselves to be accurate, that created a strong positive affect (excitement and hopefulness).

Fifth, perceived fairness and perceived accuracy significantly increased participants’ willingness to contribute, as well as their willingness to put in more effort contributing. In terms of the willingness to take greater risks, we found that perceived fairness had a significant impact whereas perceived accuracy did not. Thus, H5 is largely supported. Last, we found that when users feel excited and hopeful, they are more willing to contribute knowledge and answer more questions. Therefore, H6 is supported.

In summary, our experimental results suggest that when knowledge contributors in online forums receive positive nonverbal peer feedback, it causes them to perceive themselves as accurate and perceive their peers as fair; this, in turn, causes them to feel emotions of excitement and hopefulness, which in turn causes them to become more willing to contribute and expend more effort in contribution. The causal mechanism appears to pass through the mediating effects of internal and external attribution and emotional affect; beyond these, there does not appear to be a direct causal relationship between receiving positive nonverbal peer feedback and the propensity to contribute.

## 8 Conclusion and Discussion

## 8.1 Summary of Main Findings

To summarize, we experimentally studied the linkages between users receiving nonverbal peer feedback and their content contribution activities in the context of online forums. We deployed two experimental studies on Amazon Mechanical Turk. Study 1 demonstrated that the impact of nonverbal peer feedback on knowledge contribution is different from verbal peer feedback. Specifically, both verbal and nonverbal peer feedback helped to increase users’ willingness to contribute, but verbal feedback increased the contribution by motivating users to answer more questions, whereas nonverbal feedback increased the contribution by motivating users to answer more challenging questions.

To further examine and understand the causal mechanisms behind the impact of nonverbal feedback, we ran another experimental analysis (Study 2) on mTurk to identify the causal linkage between nonverbal peer feedback and recipients’ propensity to contribute to these online forums. Specifically, we found that positive nonverbal feedback caused recipients to attribute this in equal measure internally to greater perceived accuracy (perceived self-efficacy) and externally to a greater perceived fairness of peers giving feedback. On the other hand, negative nonverbal feedback caused recipients to attribute this to a greater extent externally to perceived unfairness by peers and to a lesser extent internally to perceived self-efficacy. In other words, when contributors are upvoted, people attribute it equally to their accuracy and to their peers’ fairness. When they are downvoted, they attribute it somewhat to their lack of accuracy but much more to the unfairness of their peers.

We also found that these internal and external attributions led to changes in the emotions of the participant, who felt excitement and hope. These emotions further increased the overall willingness to contribute and expend greater effort into contributing (i.e., answering more questions). The impact on contributors’ willingness to take greater risks (i.e., choosing harder questions with the potential for greater payoffs—or losses through negative feedback) was either negative or not significant.

## 8.2 Discussion of Contributions

Providing feedback is very important in all contexts, including educational settings and professional work (Buckingham & Goodall, 2019). Yet, providing constructive, positive feedback is not an easy task (Chappelow & McCauley, 2019). Prior literature has mainly focused on verbal feedback, and the impact of nonverbal peer feedback has been largely neglected. Our work contributes to the literature by (1)

demonstrating how verbal and nonverbal feedback affect knowledge contribution through different channels (answering more questions vs choosing harder questions) and (2) providing an enhanced understanding of users’ reactions to nonverbal peer feedback, such as upvotes and downvotes. In addition, following attribution-emotion-action theory from psychology, our work highlights the importance of internal and external attributions made by feedback recipients and their subsequent impact on recipients emotions in understanding how contributors and participants in online communities respond to nonverbal peer feedback. We conclude that when users receive nonverbal evaluative feedback, the lack of actionable information in the feedback causes feedback recipients to make varying degrees of internal attributions of perceived self-efficacy and external attributions of perceived fairness. These attributions lead to different levels of impact on emotional states such as excitement and hope, which then influence the users’ willingness to contribute.

Our research strengthens prior findings that feedback leads to greater contributions (Burtch et al., 2021). To the best of our knowledge, our study is among the first to exclusively examine nonverbal evaluative feedback instead of educative feedback, which typically consists of written or verbal feedback (Palmeri & Peter, 2019). We build upon prior work to delve deeper into the mechanisms behind how and why positive or negative nonverbal peer feedback impacts recipients’ subsequent willingness to contribute.

## 8.3 Managerial Implications

Our findings also provide important implications for firms and online platform designers. Nonverbal feedback mechanisms such as upvotes and downvotes have proliferated on online platforms (i.e., Stack Overflow and Reddit) because it is convenient for users to give upvotes and downvotes. It is also convenient for platforms to aggregate the votes and display a summary measure of popularity or usefulness for contributed content. However, our work suggests that excessive or exclusive reliance on such feedback mechanisms may backfire. Recipients are free to make unintended (and perhaps mistaken) internal or external attributions based on such feedback mechanisms, which can have unexpected consequences for subsequent user contributions, user morale, and the vibrancy of the online community. Thus, to address this potential issue, our work suggests that nonverbal peer feedback should be designed to have a particular focus in order to facilitate attribution that goes beyond simple upvotes and downvotes. Furthermore, our work potentially highlights the importance of excitement and hope, which should be incorporated when platforms design their feedback mechanisms.

Our findings suggest that when users receive downvotes, they tend to attribute their poor performance more to the perceived unfairness of their peers rather than their lack of accuracy. To mitigate this negative perception and encourage continued participation, the platform should facilitate mechanisms for users to provide specific feedback to contributors, particularly when a user downvotes someone’s contributions, and offer them the opportunity to appeal any downvotes they feel are unfair. For instance, on Stack Overflow, when a user downvotes a contribution, our research findings might support the creation of a small text box for the user to enter short verbal feedback in order for their downvote to be accepted by the platform. By creating a more transparent and fair evaluation system, the platform can help mitigate users’ negative perceptions of downvotes, increase their understanding of the evaluation process, and foster their willingness to continue contributing.

There is value in knowing that the impact of feedback on contribution behavior is mediated by emotions such as excitement and hope. For managers of websites such as Stack Overflow or Reddit who are trying to devise better nonverbal feedback mechanisms (e.g., emojis, symbols, or points), it is difficult to observe whether a new feedback mechanism will result in more contributions, because contributions can take days and weeks to materialize. However, if the managers know that the impact of nonverbal feedback on contribution is mediated by emotions such as hope and excitement, they can immediately measure the extent of hope and excitement in their subjects who are exposed to the new feedback mechanism, and that will give them a proxy for how much contribution they can expect. The managers can also manipulate or redesign the nonverbal feedback mechanism for increased excitement or hope in the respondents.

While emotions cannot be manipulated directly, they can be triggered through various cues and methods. For example, previous studies have shown that colors can influence emotions and trigger feelings of excitement and hope (Jonauskaite et al., 2020). In our study of nonverbal feedback, we found that when users receive positive feedback, they are more likely to attribute it to a higher level of perceived fairness and accuracy, thus leading to a higher level of feelings of excitement and hope. This, in turn, leads to increased motivation to contribute.

## 8.4 Limitations and Future Work

Our paper has several limitations, which suggest potential future extensions. First, more research is needed to establish the role of reputation in encouraging online content contributions. In online communities, peer feedback in the form of upvotes or downvotes leads to reputation gains and losses. Therefore, there is the upvote or downvote itself, and there is the consequence to the recipient in the form of gain or loss in reputation points. In our experimental setting, we only focus on upvotes and downvotes instead of point gains and losses. More research is needed to disentangle the impacts of points versus votes. It would be interesting to explore whether the votes received are more salient than the points gained or lost.

While our work focuses on the emotions of excitement and hope, we note that other emotions such as contentment, anger, or sorrow could also be relevant in the context of receiving feedback in online forums and can influence a user’s motivation and engagement. When a user receives positive feedback and attributes it to a fair and supportive community, they may experience contentment. This emotion could lead to sustained participation, as the user feels satisfied and valued within the community. If a user perceives negative feedback as unfair or interprets it as a personal attack, they might experience anger. This emotion could lead to a decrease in participation or aggressive responses, or it could motivate the user to prove themselves by contributing more or improving the quality of their contributions. Receiving negative feedback, especially if attributed to personal shortcomings, could lead to feelings of sadness or sorrow. This could demotivate users, causing them to withdraw from the community or reduce their contributions. In some cases, users may become anxious about how their contributions will be received, especially if they have experienced negative feedback in the past. This anxiety could lead to hesitation in making further contributions. When receiving positive feedback, a user might feel pride, especially if they attribute the feedback to their own skills and knowledge. This could serve as a motivating factor, encouraging continued and even increased participation. If a user expected positive feedback but received negative feedback, they might feel disappointed. This could affect their motivation, and they might either strive to improve or disengage from the platform. It is important for academic as well as practitioner audiences to conduct further research to fully understand these emotions and how they interact with the attribution process.

Moreover, we note that emotions such as hope and excitement can be ephemeral. Nevertheless, they may still have an impact on behavior, including future contribution behavior in online forums, through a variety of mechanisms that require further research. Transient experiences can potentially influence longterm behavior through memory, habits, identity, community, and long-term goal setting in the following ways:

The immediate emotional reaction to feedback may be strong enough to create a memory or association. The excitement from receiving upvotes could be remembered positively, and even after the emotion has faded, this memory could still influence the decision to contribute again.

If a user consistently receives positive feedback and experiences emotions like hope and excitement, these emotions could be reinforced over time. This pattern could lead to the formation of habits or expectations that could motivate continued contributions even when the immediate emotional response is not the primary driver.

Emotions may play a role in shaping an individual’s identity and self-perception. For example, repeated excitement from positive feedback might lead someone to see themselves as a valued member of the community. This identity could motivate future contributions.

Emotional experiences may also impact how connected an individual feels to a community. Positive emotions might foster a sense of belonging to the community, which could serve as a motivating factor in contributing even when the immediate emotions have subsided.

Hope can lead to setting longer-term goals or expectations. Even after the initial emotion has faded, the goals or expectations set during that emotional state might continue to influence behavior.

In summary, while emotions themselves are fleeting, they can have lasting effects through the formation of memories, habits, identity, social bonds, and goals. However, relying solely on the transient nature of emotions might not be sufficient for sustained engagement and online platforms should look at other motivators and factors that can encourage continued contributions. Further research is needed to explore these mechanisms.

## Acknowledgements

The authors thank the senior editor, the associate editor, and three anonymous reviewers for their constructive comments throughout the review process.

## References

Adomavicius, G., Gupta, A., & Sanyal, P. (2012). Effect of information feedback on the outcomes and dynamics of multisourcing multiattribute procurement auctions. Journal of Management Information Systems, 28(4), 199-230.

Bandura, A. (1990). Perceived self-efficacy in the exercise of personal agency. Revista Española de Pedagogía, 48(187), 397-427.

Bandura A. (1997). Self-efficacy: the exercise of control. W. H. Freeman. p. 604.

Brockner, J., Tyler, T. R., & Cooper-Schneider, R. (1992). The influence of prior commitment to an institution on reactions to perceived unfairness: The higher they are, the harder they fall. Administrative Science Quarterly, 37(2), 241-261.

Buckingham, M., & Goodall, A. (2019). The feedback fallacy. Harvard Business Review, 97(2), 92– 101.

Burtch, G., He, Q., Hong, Y., & Lee, D. (2022). "How do peer awards motivate creative content? Experimental evidence from Reddit." Management Science 68(5), 3488-3506.

Burtch, G., Hong, Y., Bapna, R., & Griskevicius, V. (2017). Stimulating online reviews by combining financial incentives and social norms. Management Science, 64(5), 2065- 2082.

Calder, B. J. (1977). Endogenous-exogenous versus internal-external attributions: Implications for the development of attribution theory. Personality and Social Psychology Bulletin, 3(3), 400-406.

Carver, C. S., & White, T. L. (1994). Behavioral inhibition, behavioral activation, and affective responses to impending reward and punishment: The BIS/BAS Scales. Journal of Personality and Social Psychology, 67(2), 319- 333.

Chappelow, C., & McCauley, C. (2019). What good feedback really looks like. Harvard Business Review. https://hbr.org/2019/05/what-goodfeedback-really-looks-like

Chen, L., Baird, A., & Straub, D. (2019). Why do participants continue to contribute? Evaluation of usefulness voting and commenting motivational affordances within an online knowledge community. Decision Support Systems, 118, 21-32.

Chen, W., Wei, X., & Xiaoguo Zhu, K. (2018). Engaging voluntary contributions in online

communities: A hidden Markov model. MIS Quarterly, 42(1), 83-100.

Chen, Y., & Zahedi, F. M. (2016). Individuals’ internet security perceptions and behaviors: polycontextual contrasts between the United States and China. MIS Quarterly, 40(1), 205- 222.

Chevalier, J. A., & Mayzlin, D. (2006). The effect of word of mouth on sales: Online book reviews. Journal of Marketing Research, 43(3), 345- 354.

Claffey, E., & Brady, M. (2019). An empirical study of the impact of consumer emotional engagement and affective commitment in firmhosted virtual communities. Journal of Marketing Management, 35(11-12), 1047- 1079.

Davenport, T. H., & Prusak, L. (1998). Working knowledge: How organizations manage what they know. Harvard Business School Press.

Davis, F. D., Bagozzi, R. P., & Warshaw, P. R. (1992). Extrinsic and intrinsic motivation to use computers in the workplace. Journal of Applied Social Psychology, 22(14), 1111-1132.

Davis, J. L., & Graham, T. (2021). Emotional consequences and attention rewards: The social effects of ratings on Reddit. Information, Communication & Society, 24(5), 649-666.

Fisher, C. D. (2008). Emotions in and around performance: The thrill of victory, the agony of defeat. In N. M. Ashkanasy & C. L. Cooper (Eds.), New horizons in management. Research companion to emotion in organizations (pp. 120–135). Northampton, MA: Edward Elgar Publishing.

Gunasti, K, Ozcan, T. (2019). The Role of Scale-Induced Round Numbers and Goal Specificity on Goal Accomplishment Perceptions. Marketing Letters, 30, 207–217.

Halfaker, A., Kittur, A., & Riedl, J. (2011). Don’t bite the newbies: how reverts affect the quantity and quality of Wikipedia work. Proceedings of the 7th International Symposium on Wikis and Open Collaboration.

Harrington, J. R., & Lee, J. H. (2015). What drives perceived fairness of performance appraisal? Exploring the effects of psychological contract fulfillment on employees’ perceived fairness of performance appraisal in U.S. federal agencies. Public Personnel Management, 44(2), 214-238.

Hennessey, B., Moran, S., Altringer, B., & Amabile, T. M. (2015). Extrinsic and intrinsic motivation. Wiley Encyclopedia of Management.

https://doi.org/https://doi.org/10.1002/9781118 785317.weom110098

Ho, M., MacGlashan, J., Littman, M., & Cushman, F. (2017). Social is special: A normative framework for teaching with and learning from evaluative feedback. Cognition, 167, 91-106.

Hsieh, P. P.-H., & Kang, H.-S. (2010). Attribution and Self-Efficacy and Their Interrelationship in the Korean EFL Context. Language Learning, 60(3), 606-627.

Huang, N., Burtch, G., Gu, B., Hong, Y., Liang, C., Wang, K., Fu, D., & Yang, B. (2019). Motivating user-generated content with performance feedback: Evidence from randomized field experiments. Management Science, 65(1), 327-345.

Huang, P., Tafti, A., & Mithas, S. (2018). Platform sponsor investments and user contributions in knowledge communities: The role of knowledge seeding. MIS Quarterly, 42(1), 213- 240.

Jabr, W., Mookerjee, R., Tan, Y., & Mookerjee, V. S. (2014). Leveraging philanthropic behavior for customer support the case of user support forums. MIS Quarterly, 38(1), 187-208.

Jiménez, F. R., & Mendoza, N. A. (2013). Too popular to ignore: The influence of online reviews on purchase intentions of search and experience products. Journal of Interactive Marketing, 27(3), 226-235.

Jonauskaite, D., Parraga, C. A., Quiblier, M., & Mohr, C. (2020). Feeling blue or seeing red? Similar patterns of emotion associations with colour patches and colour terms. i-Perception, 11(1). https://doi.org/10.1177/2041669520902484

Kelley, H. (1967). Attribution theory in social psychology. Nebraska Symposium on Motivation, 15, 192-238.

Kelley, H. H., & Michela, J. L. (1980). Attribution theory and research. Annual Review of Psychology, 31, 457-501.

Krueger Jr., N., & Dickson, P. R. (1994). How believing in ourselves increases risk taking: perceived self-efficacy and opportunity recognition. Decision Sciences, 25(3), 385-400.

Leung, K., Su, S., & Morris, M. W. (2001). When is criticism not constructive? The roles of fairness perceptions and dispositional attributions in employee acceptance of critical supervisory feedback. Human Relations, 54(9), 1155-1187.

Li, X., & Hitt, L. M. (2008). Self-selection and information role of online product reviews. Information Systems Research, 19(4), 456-474.

Li, Y. J., Hoffman, E., & Zhu, D. (2022). Should firms pay for online brand communities: Using lead user theory in analyzing two contrasting cases. Decision Support Systems, 155, Article 113729.

Lind, E. A., & Tyler, T. R. (1988). The social psychology of procedural justice. Springer.

Liu, X., Zhang, Z., Law, R., & Zhang, Z. (2019). Posting reviews on OTAs: Motives, rewards and effort. Tourism Management, 70, 230-237.

Lopes, L. L. (1987). Between hope and fear: The psychology of risk. Advances in Experimental Social Psychology, 20, 255-295.

Lovett, B. J., & Eckert, T. L. (2009). Reinforcement sensitivity and responsiveness to performance feedback: A preliminary investigation. Journal of Applied School Psychology, 25, 204-219.

Ma, M., & Agarwal, R. (2007). Through a glass darkly: Information technology design, identity verification, and knowledge contribution in online communities. Information Systems Research, 18(1), 42-67.

Malhotra, D., Ku, G., & Murnighan, J. K. (2008). When winning is everything. Harvard Business Review, 86(5), 78-86.

Marakas, G., Johnson, R., & Clay, P. (2007). The evolving nature of the computer self-efficacy construct: An empirical investigation of measurement construction, validity, reliability and stability over time. Journal of the Association for Information Systems, 8(1), 16- 46.

Moon, J. Y., & Sproull, L. S. (2008). The role of feedback in managing the internet-based volunteer work force. Information Systems Research, 19(4), 494-515.

Oman, R., & McAuley, E. (1993). Intrinsic motivation and exercise behavior. Journal of Health Education, 24(4), 232-238.

Owen, D. J., Slep, A. M. S., & Heyman, R. E. (2012). The effect of praise, positive nonverbal response, reprimand, and negative nonverbal response on child compliance: a systematic review. Clinical Child and Family Psychology Review, 15(4), 364-385.

Palmeri, A., & Peter, J. (2019). Pivoting from evaluative to educative feedback during postobservation conferencing: Supporting the development of preservice teachers. In T. E. Hodges & A. C. Baum (Eds.). Handbook of

research on field-based teacher education (pp. 495-517). IGI Global.

Patrick, B. C., Hisley, J., & Kempler, T. (2000). “What’s everybody so excited about?”: The effects of teacher enthusiasm on student intrinsic motivation and vitality. The Journal of Experimental Education, 68(3), 217-236.

Peifer, C., Schönfeld, P., Wolters, G., Aust, F., & Margraf, J. (2020). Well done! Effects of positive feedback on perceived self-efficacy, flow and performance in a mental arithmetic task. Frontiers in Psychology, 11, Article 1008.

Pillai, K. G., & Min, S. (2010). A firm’s capability to calibrate supply chain knowledge— Antecedents and consequences. Industrial Marketing Management, 39(8), 1365-1375.

Pintrich, P. R., & Schunk, D. H. (2002). Motivation in education: Theory, research, and applications. Prentice Hall.

Rand, K. L., & Cheavens, J. S. (2009). 323 Hope Theory. In S. J. Lopez & C. R. Snyder (Eds.), The Oxford handbook of positive psychology (pp. 323-334). Oxford University Press.

Reeve, J., & Cole, S. G. (1987). Integration of affect and cognition in intrinsic motivation. The Journal of Psychology, 121(5), 441-449.

Reeve, J., Cole, S. G., & Olson, B. C. (1986). Adding excitement to intrinsic motivation research. Journal of Social Behavior & Personality, 1(3), 349-363.

Salanova, M., Llorens, S., & Schaufeli, W. B. (2011). “Yes, I can, I feel good, and I just do it!” On gain cycles and spirals of efficacy beliefs, affect, and engagement. Applied Psychology: An International Review, 60(2), 255-285.

Salanova, M., Martínez, I., & Llorens, S. (2012). Success breeds success, especially when selfefficacy is related with an internal attribution of causality. Estudios de Psicología, 33(2), 151- 165.

Schreiner, M., Fischer, T., & Riedl, R. (2021). Impact of content characteristics and emotion on behavioral engagement in social media: Literature review and research agenda. Electronic Commerce Research, 21(2), 329- 345.

Schunk, D. H. (1984). Self‐efficacy perspective on achievement behavior. Educational Psychologist, 19(1), 48-58.

Snyder, C. R. (2002). Hope theory: Rainbows in the mind. Psychological Inquiry, 13, 249-275.

Sun, J., Stevenson, K., Kabbani, R., Richardson, B., & Smillie, L. D. (2017). The pleasure of making a difference: Perceived social contribution explains the relation between extraverted behavior and positive affect. Emotion, 17(5), 794-810.

Surinder Singh, K., & Randolph, B. C. (2003). Exploring the core concepts of media richness theory: The impact of cue multiplicity and feedback immediacy on decision quality. Journal of Management Information Systems, 20(1), 263-299.

van den Bos, K., Maas, M., Waldring, I., & Semin, G. (2003). Toward understanding the psychology of reactions to perceived fairness: The role of affect intensity. Social Justice Research, 16, 151-168.

van Vianen, A. E. M., Taris, R., Scholten, E., & Schinkel, S. (2004). Perceived fairness in personnel selection: Determinants and outcomes in different stages of the assessment procedure. International Journal of Selection and Assessment, 12(1-2), 149-159.

Vana, P., & Lambrecht, A. (2021). The effect of individual online reviews on purchase likelihood. Marketing Science, 40(4), 708-730.

Verbruggen, F., Chambers, C. D., Lawrence, N. S., & McLaren, I. P. L. (2017). Winning and losing: Effects on impulsive action. Journal of Experimental Psychology: Human Perception and Performance, 43(1), 147-168.

Wang, J., Li, G., & Hui, K.-L. (2022). Monetary incentives and knowledge spillover: Evidence from a natural experiment. Management Science 68(5), 3549-3572.

Wang, L., Gunasti, K., Shankar, R., Pancras, J., & Gopal, R. (2020). Impact of gamification on perceptions of word-of-mouth contributors and actions of word-of-mouth consumers. MIS Quarterly, 44(4), 1987-2011.

Wang, N., Liu, Y., & Xiao, S. (2022). Which feedback matters? The role of expressions and valence in continuous high-quality knowledge contribution in the online Q&A community. Decision Support Systems, 156, Article 113750.

Watson, D., Clark, L. A., & Tellegen, A. (1988). Development and validation of brief measures of positive and negative affect: The PANAS scales. Journal of Personality and Social Psychology, 54(6), 1063-1070.

Weiner, B. (1980). A cognitive (attribution)-emotionaction model of motivated behavior: An analysis of judgments of help-giving. Journal

of Personality and Social Psychology, 39, 186- 200.

Weiner, B. (2010). The development of an attributionbased theory of motivation: A history of ideas. Educational Psychologist, 45(1), 28-36.

Zhao, K., Zhang, P., & Lee, H.-M. (2022). Understanding the impacts of user- and marketer-generated content on free digital content consumption. Decision Support Systems, 154, Article 113684.

Zhao, L., Detlor, B., & Connelly, C. E. (2016). Sharing knowledge in social Q&A sites: The unintended consequences of extrinsic motivation. Journal of Management Information Systems, 33(1), 70- 100.

Zhu, F., & Zhang, X. (2010). Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74(2), 133-148.

Zhu, H., Kraut, R., & Kittur, A. (2012). Effectiveness of shared leadership in online communities Proceedings of the ACM 2012 Conference on Computer Supported Cooperative Work. https://doi.org/10.1145/2145204.2145269

Zhu, H., Zhang, A., He, J., Kraut, R. E., & Kittur, A. (2013). Effects of peer feedback on contribution: A field experiment in Wikipedia. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. https://doi.org/10.1145/2470654.2481311

## Appendix A: Study 1 Qualtrics Design

## 1. Attention Check

Q1. How are you feeling right now? Although we are interested in how you really feel, for the purpose of this question, please choose slightly unhappy below.

• Extremely happy

• Moderately happy

• Slightly happy

• Neither happy nor unhappy

• Slightly unhappy

• Moderately unhappy

• Extremely unhappy

Your help is very important to us, please attend to the questions.

## 2. Introduction

Intro1. In this study, you will be asked to play a game called spot the ball. You will be shown screen captures from soccer matches where the ball has been removed and you will try to guess the location of the ball. You will be randomly assigned into two groups, “A” and “B”: ”A” group participants (mTurkers) will be helping “B” group participants. The “B” group participants will be evaluating the “A” group participants. Based on the accuracy of the provided answers, group A participants could be upvoted by earning points, or downvoted by losing points.

Please enter a valid mTurk ID (required for compensation) and click -> to continue…

Intro2. You have been chosen to be an “A” group participant. In the following pages, we will first ask you to complete a skill assessment task and based on your performance you will be awarded reputation points by the system. Then, you will start the game with the initial reputation points you earned, and you will be asked to answer some questions. Your answers will help group ”B” participants, who will then either upvote or downvote you, depending on the accuracy of your answers. Based on the upvotes or downvotes by “B” group participants, you will gain or lose points for each question until the end of the game. You may be able to earn bonus money depending on the points you earn.

## Q2. Which Group are you in?

Group A - you will give answers that will help Group B who will evaluate you.

Group B - you will evaluate the answers of Group A who will help you.

Q3. You picked the wrong group indicating that you are not paying attention. Please read carefully.

You have been chosen to be an “A” group participant. Participants in Group “B” who you will be helping will evaluate the quality of your help. Specifically, they will either upvote or downvote you, depending on the accuracy of your answers.

In the following pages, we will first ask you to complete a skill assessment task and based on your performance you will be awarded reputation points by the system. Then, you will start the game with the points you earned, and depending on the accuracy of your answers, you will earn or lose points for each question until the end of the game - based on upvotes or downvotes by “B” group participants.

Depending on the points you earn, you may be able to earn a monetary bonus on top of your regular compensation.

Q4. While we are assigning your role: How are you feeling right now? Although we are interested in how you really feel, for the purpose of this question, please choose slightly unhappy below.

• Extremely happy

• Moderately happy

• Slightly happy

• Neither happy nor unhappy

• Slightly unhappy

• Moderately unhappy

• Extremely unhappy

## 3. Initial Assessment Tasks

Q5. This is the initial assessment task consisting of 2 questions. This is a snapshot from a soccer game where the ball has been removed from the picture. You are asked to guess the most likely location of the ball. Think carefully, where is the ball in the below picture? (Click on one of the dots 1, 2, or 3 in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/2cc1f5d0495c3709745921f6f12ce4447448c3faca67d6cb8947527f17621ecd.jpg)

Q6. Where is the ball in the below picture? (Click on one of the dots 1, 2, or 3 in the photo)  
![](/api/attachments/EG88MYBZ/fulltext/images/50efd313f3781f506b03b88e4a0790ea8d0b1b5015bdddeebff76ef1b1ba1204.jpg)

4. Experiment Group: Nonverbal – More Positive<sup>4</sup>

Statement. You received 800 points for starting the game.

Also, remember now other mTurkers will be evaluating your performance. The more points you win, the more bonus you may earn.

On the next page, we will start the actual game.

## Picture\_A

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/e61cf390403a072c7360fe8f657f01339eeeab29fb49d7494f6324c6765e0155.jpg)

## Picture\_A \_Result

Other mTurkers have upvoted you based on their evaluation of how close you were to the correct location.

## Picture\_B

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/8dd8057c8070bf3d152b53a95e5cdf76d9dccec69633d73aa812c2da40db862e.jpg)

## Picture\_B\_Result

Other mTurkers have downvoted you based on their evaluation of how close you were to the correct location.

Picture\_C

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/975f52614f1e5e6091a0abf52f28095e403be641a4fd0137a857949a1db83b10.jpg)

## Picture\_C\_Result

Other mTurkers have upvoted you based on their evaluation of how close you were to the correct location.

## Picture\_D

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/621965c0c80d12af49e6a82aaae6aa09ee2b3f6d446b09e21c02e6c27e20dea7.jpg)

## Picture\_D\_Result

Other mTurkers have upvoted you based on their evaluation of how close you were to the correct location.

Q7. Based on your performance, do you feel like continuing to answer questions?

• Strongly Disagree

• Disagree

• Neutral

• Agree

• Strongly Agree

Q8. Based on your performance, how many more questions do you feel like answering?

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Number of Questions ()</td><td colspan="10"></td></tr></table>

Q9. You started out with 800 reputation points and you now have 960 points based on upvotes and downvotes by other participants.

Please pick one final question to answer, from among the choices below. As before, your answers will be upvoted or downvoted by other participants.

Remember that the more points you win, the more bonus you may earn.

• Question A: Chance to win up to 200 points or lose up to 40 points

• Question B: Chance to win up to 400 points or lose up to 80 points

• Question C: Chance to win up to 600 points or lose up to 120 points

• Question D: Chance to win up to 800 points or lose up to 160 points

## 5. Demographics

Q10. What’s your gender?

Male

• Female

• Other

## Q11. What’s your age?

• Under 18

• 18 - 24

• 25 - 34

• 35 - 44

• 45 - 54

• 55 - 64

• 65 - 74

• 75 - 84

• 85 or older

## Q12. What’s your education level?

Less than high school

High school graduate

• Some college

• 2-year degree

• 4-year degree

• Professional degree

Doctorate

Q13. Risk Level - Provide a rating from Very unlikely to Very likely, using the following scale:

<table><tr><td></td><td>Very unlikely</td><td>Somewhat unlikely</td><td>Neither likely nor unlikely</td><td>Somewhat likely</td><td>Very likely</td></tr><tr><td>Betting a day&#x27;s income at the horse races.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Investing 10% of your annual income in a moderate growth diversified fund.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Betting a day&#x27;s income at a high-stake poker game.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Investing 5% of your annual income in a very speculative stock.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Betting a day&#x27;s income on the outcome of a sporting event.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Investing 10% of your annual income in a new business venture.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr></table>

The four feedback messages we used in Study 1:

## • Verbal Positive Feedback

“According to the feedback from other mTurkers, the players’ positions reflect that the ball can be at the position you selected. Your selection aligns well with others’ views.”

## • Verbal Negative Feedback

“According to the feedback from other mTurkers, the players’ positions do not reflect that the ball can be at the position you selected. Your selection differs from others’ views.”

• Nonverbal Positive Feedback

“Other mTurkers have upvoted you based on their evaluation of how close you were to the correct location.”

● Nonverbal Negative Feedback

“Other mTurkers have downvoted you based on their evaluation of how close you were to the correct location.”

## Appendix B: Study 2 Qualtrics Design

The experiment flow for our main study is summarized in Figure B1.

![](/api/attachments/EG88MYBZ/fulltext/images/acafcf6d89803a9b1908bcd23c6e423b2ccb832bd58c92212670b47a84c791c1.jpg)  
Figure B1. The Experiment Flow for Main Study

## 1. Attention Checks

Please read the following attention check questions carefully. If you give a wrong answer, you will not be able to continue the survey or receive compensation:

Q1. Before you start, please answer the following human check questions. If you answer them wrong, you will not be able to continue or receive any compensation. What is the fifth word in the following sentence:

Bobby is very happy because he is going to the movies.

Very Happy • Going • Because • movies • is the

Q2. How many stars are there? Please choose number two instead of the actual number of stars.

• 1 • 2 • 3 • 4 • 5

## 2. Introduction

Intro1. In this study, you will be asked to play a game called spot the ball. You will be shown screen captures from soccer matches where the ball has been removed and you will try to guess the location of the ball. You will be randomly assigned into two groups, “A” and “B”: ”A” group participants (mTurkers) will be helping “B” group participants.

The “B” group participants will be evaluating the “A” group participants. Based on the accuracy of the provided answers, group A participants could be upvoted by earning points, or downvoted by losing points.

Please enter a valid mTurk ID (required for compensation) and click -> to continue…

Intro2. You have been chosen to be an “A” group participant. In the following pages, we will first ask you to complete a skill assessment task and based on your performance you will be awarded reputation points by the system. Then, you will start the game with the initial reputation points you earned, and you will be asked to answer some questions. Your answers will help group “B” participants, who will then either upvote or downvote you, depending on the accuracy of your answers. Based on the upvotes or downvotes by “B” group participants, you will gain or lose points for each question until the end of the game. You may be able to earn bonus money depending on the points you earn.

Q3. Which Group are you in?

Group A - you will give answers that will help Group B who will evaluate you.

Group B - you will evaluate the answers of Group A who will help you.

## Q4. You picked the wrong group indicating that you are not paying attention. Please read carefully.

You have been chosen to be an “A” group participant. Participants in Group “B” who you will be helping will evaluate the quality of your help. Specifically, they will either upvote or downvote you, depending on the accuracy of your answers.

In the following pages, we will first ask you to complete a skill assessment task and based on your performance you will be awarded reputation points by the system. Then, you will start the game with the points you earned, and depending on the accuracy of your answers, you will earn or lose points for each question until the end of the game - based on upvotes or downvotes by “B” group participants.

Depending on the points you earn, you may be able to earn a monetary bonus on top of your regular compensation.

Q5. While we are assigning your role: How are you feeling right now? Although we are interested in how you really feel, for the purpose of this question, please choose slightly unhappy below.

• Extremely happy

• Moderately happy

• Slightly happy

• Neither happy nor unhappy

• Slightly unhappy

• Moderately unhappy

• Extremely unhappy

## 3. Initial Assessment Tasks

IniAssTask1. This is the initial assessment task consisting of 2 questions. The following picture is a snapshot from a soccer game where the ball has been removed from the picture. You are asked to guess the most likely location of the ball. Depending on your accuracy, you will be assigned initial reputation points by the system.

Think carefully, where is the ball in the below picture? (Click on one of the dots 1, 2, or 3 in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/8f1f5fa1b78e0f4d4c61772ad3777e9f739d656deab9d73be6c4dcabdcea6b1c.jpg)

IniAssTask2. Where is the ball in the below picture? (Click on one of the dots 1, 2, or 3 in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/db358a8ee923370571724eaa6ff5acb6e980af10a3793426ab20651911cc553a.jpg)

4. Experiment Group: High Initial Points – More Downvotes<sup>5</sup>

Statement. Great! You have done a good job. You received 800 points and you are in the top 20% group among all the participants.

On the next page, we will start the actual game.

Also, remember now other mTurkers will be evaluating your performance. The more points you win, the more bonus you may earn.

## Picture\_A

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/8393aa886a71d134190fd23821ccd80e35adfc021327dae5f265f83e33252b51.jpg)

## Picture\_A \_Result

You have been downvoted. Other mTurkers removed 80 points from your total, based on their evaluation of how close your answer was to the correct answer, and now you have 720 reputation points. Your performance record so far: Downvoted

## Picture\_B

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/e9e8dca307d524680de82ca80cf590e632e649e5785d28371c7e3428894bff72.jpg)

## Picture\_B\_Result

You have been upvoted. Other mTurkers awarded you 80 points based on their evaluation of how close your answer was to the correct answer, and now you have 800 reputation points. Your performance record so far: Downvoted, Upvoted

## Picture\_C

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/7290c526196729ecf082deac490b56b2b426795f055187fb6d7bb9ccbf0896c1.jpg)

## Picture\_C\_Result

You have been downvoted. Other mTurkers removed 80 points from your total, based on their evaluation of how close your answer was to the correct answer, and now you have 720 reputation points. Your performance record so far: Downvoted, Upvoted, Downvoted

## Picture\_D

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/2578ec58b52aaeae80799f7c4c26f3af06c6f039868783a7482c269ec4ba4cf1.jpg)

## Picture\_D\_Result

You have been downvoted. Other mTurkers removed 80 points from your total, based on their evaluation of how close your answer was to the correct answer, and now you have 640 reputation points. Your performance record so far: Downvoted, Upvoted, Downvoted, Downvoted

Picture\_E

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/227c8d17797bf333852ea325829f9a5f0631354274895d2d4a5ce19fe2ffb1e0.jpg)

Picture\_E\_Result You have been downvoted. Other mTurkers removed 80 points from your total, based on their evaluation of how close your answer was to the correct answer, and now you have 560 reputation points. Your performance record so far: Downvoted, Upvoted, Downvoted, Downvoted, Downvoted,

Picture\_F

Where is the ball in the below picture? (Click on one of the dots A, B, or C in the photo)

![](/api/attachments/EG88MYBZ/fulltext/images/cdc12077f3fa575f7408d6338795c68f8f8c224d39c1bf5dd15039cc8252bf27.jpg)

Picture\_F\_Result You have been downvoted. Other mTurkers removed 80 points from your total, based on their evaluation of how close your answer was to the correct answer, and now you have 480 reputation points.

Your performance record so far: Downvoted, Upvoted, Downvoted, Downvoted, Downvoted, Downvoted

Q6. Based on your performance, do you feel like continuing to answer questions?

• Strongly Disagree

• Disagree

Neutral

• Agree

• Strongly Agree

Q7. Based on your performance, how many more questions do you feel like answering?

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Number of Questions ()</td><td colspan="10"><img src="/api/attachments/EG88MYBZ/fulltext/images/91f375e0df36738d135c66a96171bef966631e68e8c18824bded37c96b957b7e.jpg"/></td></tr></table>

Q8. You started out with 800 reputation points and placed in the top 20% group among all the participants. You now have 480 points based on subsequent upvotes and downvotes by other participants.

Please pick one final question to answer, from among the choices below. As before, your answers will be upvoted or

downvoted by other participants.

Remember that the more points you win, the more bonus you may earn.

• Question A: Chance to win up to 200 points or lose up to 40 points

• Question B: Chance to win up to 400 points or lose up to 80 points

• Question C: Chance to win up to 600 points or lose up to 120 points

• Question D: Chance to win up to 800 points or lose up to 160 points

Q9. So far others have downvoted you five times and upvoted you once, do you feel that you have been fairly evaluated by other participants?

• Strongly Disagree

• Disagree

Neutral

• Agree

• Strongly Agree

## Q10. Based on your performance, do you think you can accurately find the soccer ball position?

• Not accurately at all

• Slightly accurately

• Moderately accurately

• Accurately

• Very accurately

## 5. Emotion and Demographics

Q11. How excited are you about the challenge level of this game?

• Not excited

• Just a little bit excited

• Somewhat excited

Excited

• Very excited

## Q12. How hopeful are you about winning more points if we continue the game?

• Very hopeless

• Somewhat hopeless

• Neither hopeful nor hopeless

• Somewhat hopeful

• Very hopeful

## Q13. What’s your gender?

Male

• Female

• Other

Q14. What’s your age?

Under 18

• 18 - 24

• 25 - 34

• 35 - 44

• 45 - 54

• 55 - 64

65 - 74

• 75 - 84

85 or older

Q15. What’s your education level?

• Less than high school

High school graduate

• Some college

• 2-year degree

• 4-year degree

• Professional degree

Doctorate

Q16. Risk Level - Provide a rating from Very unlikely to Very likely, using the following scale:

<table><tr><td></td><td>Very unlikely</td><td>Somewhat unlikely</td><td>Neither likely nor unlikely</td><td>Somewhat likely</td><td>Very likely</td></tr><tr><td>Betting a day&#x27;s income at the horse races.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Investing 10% of your annual income in a moderate growth diversified fund.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Betting a day&#x27;s income at a high-stake poker game.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Investing 5% of your annual income in a very speculative stock.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Betting a day&#x27;s income on the outcome of a sporting event.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Investing 10% of your annual income in a new business venture.</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr></table>

## About the Authors

Ramesh Shankar is an associate professor of information systems at the School of Business, University of Connecticut. His current research focuses on online user behavior and economic analysis of digital goods. Ramesh has a PhD from the Leonard N. Stern School of Business, NYU. His work has been published in leading journals including Information Systems Research, MIS Quarterly, Marketing Science, and Production & Operations Management. He has served as associate editor for MIS Quarterly and has reviewed extensively for several journals and conferences.

Lei Wang is an assistant professor of information systems at the Smeal College of Business, Pennsylvania State University. She received her PhD degree in operations and information management from the University of Connecticut, a master’s degree in economics, and a bachelor’s degree in electronic engineering. Her research interests include location-based services, gamification, user engagement on digital platforms, artificial intelligence (AI), and web3. Her work has appeared in leading journals, such as MIS Quarterly, Information Systems Research, Production and Operations Management, and Decision Support Systems. She was awarded the INFORMS ISS Nunamaker-Chen Dissertation Award in 2015. She currently serves as an associate editor for Decision Support Systems. In addition, Lei is an ad hoc reviewer for Management Science, Information Systems Research, MIS Quarterly, Production and Operations Management, Journal of Management Information Systems, Decision Support Systems, and Service Science. She has also served as an associate editor, session chair, discussant, or program committee member for conferences including ICIS, CIST, WITS, WISE, CSWIM, and PACIS.

Kunter Gunasti is an associate professor of marketing at the Carson College of Business, Washington State University. He holds a PhD in marketing from Penn State University along with a BSc in engineering and an MBA in finance. His research focuses on numerical cognition, branding, inference making and consumption experiences such as word of mouth and gift giving. Dr. Gunasti’s work has been published in premium outlets including the MIS Quarterly, Journal of Consumer Research, Journal of Marketing Research, Journal of Consumer Psychology, Journal of Retailing, Marketing Letters, Journal of Business Ethics, and Journal of Business Research. He was the recipient of the Thomas Kinnear Award for the Best Article published in the Journal of Public Policy and Marketing as well as the Emerald Literati Highly Commended Paper Award published in the European Journal of Marketing. He has also received two American Marketing Association Best Paper Awards and the Advena World’s Outstanding Speaker Award.

Hongfei Li is an assistant professor in the Department of Decisions, Operations and Technology at The Chinese University of Hong Kong (CUHK) Business School. Before joining CUHK, he received his PhD from the School of Business at the University of Connecticut and his BS and MS from Renmin University of China in Beijing. His current research focuses on three main streams: (1) business analytics in emerging online platforms, (2) applications of artificial intelligence and machine learning, and (3) statistical methodology. His work has been published in leading academic journals, such as Information Systems Research, Decision Support Systems, and ACM Transactions on Management Information Systems.

Copyright © 2024 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
