---
otero_id: 14708
otero_key: "AP45XVN3"
title: "Understanding Voluntary Knowledge Provision and Content Contribution Through a Social-Media-Based Prediction Market: A Field Experiment"
authors: "Liangfei Qiu; Subodha Kumar"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0679"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/AP45XVN3/fulltext/images/1181882a926f38c8f3ad4c2d0b4b25f5e6b08c93a2989fbad33037b903e454d5.jpg)

# Information Systems Research

![](/api/attachments/AP45XVN3/fulltext/images/442e5cedc1c1402a6a65d38206f6f917634bfc85a253cfe839de0724d095bb79.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Understanding Voluntary Knowledge Provision and Content Contribution Through a Social-Media-Based Prediction Market: A Field Experiment

http://orcid.org/0000-0002-8771-9389Liangfei Qiu, Subodha Kumar

To cite this article:

http://orcid.org/0000-0002-8771-9389Liangfei Qiu, Subodha Kumar (2017) Understanding Voluntary Knowledge Provision and Content Contribution Through a Social-Media-Based Prediction Market: A Field Experiment. Information Systems Research

Published online in Articles in Advance 18 Apr 2017

https://doi.org/10.1287/isre.2016.0679

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/AP45XVN3/fulltext/images/ce6c6b60ef1649db246457c7695a1c993023d8c6f68a36539d7bcfcf4ec25b0c.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Understanding Voluntary Knowledge Provision and Content Contribution Through a Social-Media-Based Prediction Market: A Field Experiment

Liangfei Qiu,<sup>a</sup> Subodha Kumar<sup>b</sup>

<sup>a</sup> Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>b</sup> Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122 Contact: liangfei.qiu@warrington.ufl.edu, http://orcid.org/0000-0002-8771-9389 (LQ); subodha@tamu.edu (SK)

Received: October 2, 2015 Accepted: September 2, 2016 Published Online in Articles in Advance: April 18, 2017

https://doi.org/10.1287/isre.2016.0679

Copyright: © 2017 INFORMS

Abstract. The performance of prediction markets depends crucially on the quality of user contribution. A social-media-based prediction market can utilize aspects of social efects to improve users’ contribution quality. In this study, we examine the causal efect of social audience size and online endorsement on prediction market participants’ prediction accuracy through a randomized field experiment. By conducting a comprehensive treatment efect analysis, we estimate both the average treatment efect (ATE) and the quantile treatment efect using the diference-in-diferences method. Our empirical results on ATE show that an increase in audience size leads to an improvement in prediction accuracy, and that a higher level of online endorsement also leads to prediction improvements. Interestingly, we find that the quantile treatment efects are heterogeneous: users of intermediate prediction ability respond most positively to an increase in social audience size and online endorsement. These findings suggest that prediction markets can target people of intermediate abilities to obtain the most significant prediction improvement.

History: Yong Tan, Senior Editor; Param Singh, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2016.0679.

Keywords: prediction market • social media • field experiment • treatment efects

## 1. Introduction

There is nothing more important than telling the company what we know. The Best Buy TagTrade prediction market provides an early warning indicator to help flag potential problems early.

—Jef Severts, EVP, Best Buy<sup>1</sup>

The GE Imagination Market helps us answer tough business questions such as “What new technology should we be investing in?” and “Which new products should we be developing?”

—Christina LaComb, Computer Scientist, Computational Intelligence Lab, GE Global Research<sup>2</sup>

## 1.1. Motivation and Research Context

In the past decade, we have witnessed the growing popularity of prediction markets, in which people place bets on events that they think are most likely to happen, thus revealing their cross-functional and frontline knowledge. Prediction markets are intriguing potential tools to revolutionize business forecasting and change the landscape of decision making. On one hand, a number of public prediction markets<sup>3</sup> have been proven to be an efective way to harness the wisdom of crowds in diverse areas, such as predicting political elections, movie box ofice revenue, sports outcomes, and finance and technology events (Spann and Skiera 2003, Wolfers and Zitzewitz 2004, Berg et al. 2008, Healy et al. 2010). On the other hand, big companies like Hewlett-Packard, Intel, Best Buy, Microsoft, and Google have all employed internal prediction markets to foretell how products might fare, assess likely product shipment dates, predict sales volume, and identify best-selling products (Schlack 2015). Corporate practitioners have already recognized the power of harnessing the collective wisdom in managing demand risk in supply chains, monitoring leading business indicators, and gathering new ideas and business innovations (Guo et al. 2006, Hopman 2007).<sup>4</sup> In general, the use of prediction markets will serve a critical role in bringing a new transparency to forecasting and allowing unheralded experts to challenge conventional wisdom during the innovation process.

Despite the popularity of public prediction markets and considerable interest in running internal corporate prediction markets, the use of prediction markets to help address real-world business challenges is still in its infancy, and the prediction market revolution in business is taking longer than expected (Hopman 2007, Broughton 2013). Essentially, a prediction market is a user-generated content (UGC) platform. One of the main challenges in implementing prediction markets is in finding an efective way to improve the quality of UGC and increase individual prediction accuracy. To resolve the problem of low-quality contribution, monetary incentives can be carefully designed using incentive-compatible mechanisms (Chen et al. 2010). However, because of the legal constraint, most public prediction markets operate without using “real money.”<sup>5</sup> In corporate prediction markets, small monetary prizes are not enough to elicit knowledge from employees (Coles et al. 2007). Therefore, a prediction market mainly relies on voluntary participation rather than monetary transfers, and the classical mechanism design theory in economics cannot be directly applied to the prediction market context.

In this study, we highlight that nonpecuniary incentive design is a core function of a prediction market designer. More specifically, we examine how to make use of social image (nonmonetary incentives) to improve individual prediction accuracy in a unique social-media-based prediction market where the predictions made by individual participants are pushed to their followers’ Twitter timelines, and these followers are able to benefit from those potentially valuable predictions. It is worth noting that public prediction market designers usually have less authority and control over participants than what the managers of corporate prediction markets have. Unlike managers in formal work organizations, public prediction market designers generally cannot rely on corporate hierarchies to get organizational members to show up and work (Ren et al. 2007), so using social image to incentivize individuals to provide high-quality predictions is particularly important in public prediction markets.

More generally, knowledge provision or UGC in online platforms is an important research area for both researchers and practitioners. We intend to identify factors that afect users’ contribution quality, since a lot of platforms’ success depends on users’ contribution quality. There has been a growing number of studies that explore users’ motivation to contribute content (e.g., Shriver et al. 2013, Toubia and Stephen 2013), but the underlying mechanism driving users’ contribution behavior has not been completely understood. What is more intriguing is perhaps the fact that several successful platforms featuring UGC do not provide users with monetary benefits, but users are still willing to contribute high-quality contents. Our research question in this paper is to extend this line of research and study a specific type of UGC (i.e., provision of users’ event predictions in a social-media-based prediction market), and explore important social factors that afect users’ contribution quality. We also ask the question whether users of difering levels of predictive accuracy might respond diferently to these social factors (the heterogeneity of social efects).

Empirically, we conduct a randomized field experiment by collaborating with a social-media-based prediction market. Users can log into the prediction market platform via Twitter and make predictions by simply clicking on either the “YEA” or “NAY” button on the prediction page, as shown in Figure 1. This social-media-enabled prediction market automatically tweets users’ predictions, and these tweets are pushed to their followers’ timelines. If a user thinks the stated event is likely to occur, she would click on “YEA”; otherwise, she would click on “NAY.” This user’s prediction (“NAY” in this case) is then automatically posted as a tweet and is pushed to her followers’ timelines. Once the event being predicted is realized, the prediction platform automatically posts a second tweet on behalf of the user, and the tweet gets subsequently pushed to her followers’ timelines. This tweet is either “You were right!” or “Your prediction was wrong!,” depending on whether the user predicted the event correctly. Note that no monetary incentive is involved in this social-media-based prediction market. The detailed institutional context of the social-media-based prediction market can be found in Online Appendix A.

Prior studies on UGC suggest that users’ contribution quantity might be influenced by social efects. For example, Zhang and Zhu (2011) find that Wikipedia contributors’ contribution quantity is afected by the size of the audience; Toubia and Stephen (2013) also find that social-media users’ posting level increases as their number of followers increases. To examine whether or not these efects are also present in a social-media-based prediction market, we design

Figure 1. (Color online) A Screenshot of a Social-Media-Based Prediction Market

Anti-EU fringe parties will capture more than 25% of the vote in European parliamentary elections.

## I voted #nay on @gideonrachman's prediction. goo.gl/dQK1Ay

Anti-EU fringe parties will capture more than 25% of the vote in.. By Gideon Rachman @gideonrachman

treatment conditions that reflect social efects and endorsement efects and study how these factors might afect users’ prediction accuracy. Since followers can observe whether or not the user has predicted events correctly, we suspect that some types of social efects and reputational concerns will play an important role in the prediction accuracy. In particular, having the predictions automatically broadcast to followers might induce social efects that would incentivize users to make predictions more carefully to maintain their reputation. In addition, since followers can interact with users by retweeting or marking any user tweet as a favorite, we suspect that this type of behavior might induce an endorsement efect that may also encourage users to make careful predictions.

## 1.2. Theoretical and Practical Contributions

Researchers often face the challenge of identifying the causal efect of social interaction on content contribution because of the endogenous nature of social tie formation. This is because voluntary knowledge contribution could be driven by social connection, while social connection could be facilitated by knowledge contribution, and both knowledge contribution and social connection could be driven by some unobserved individual characteristics (Ma and Agarwal 2007, Zhang and Zhu 2011). Some identification strategies include the use of instrumental variables (e.g., Shriver et al. 2013), natural experiments (e.g., Zhang and Zhu 2011, Zhang and Wang 2012), controlled laboratory experiments (e.g., Qiu et al. 2014a, b), and field experiments (e.g., Toubia and Stephen 2013). Experiments are efective ways to obtain causal efects, because researchers can impose exogenous shocks on experiment subjects, ceteris paribus. Our field experiment design is similar to that in Toubia and Stephen (2013), and has the advantage of studying individuals’ organic social ties, as opposed to controlled laboratory experiments in which social networks are often artificially assigned. Therefore, our experiment design can establish a higher level of external validity than controlled laboratory experiments.

We use a diference-in-diferences (DID) approach to estimate the efect of audience size and online endorsement on users’ prediction accuracy. The result shows that, consistent with our expectation, an increase in audience size leads to an improvement in average prediction accuracy. Furthermore, we find that an increase in the online endorsement level also leads to an increase in average prediction accuracy. While prior studies focus mostly on the average treatment efects (ATEs) of audience size (e.g., Zhang and Zhu 2011, Toubia and Stephen 2013), we also conduct a series of quantile treatment regressions to examine how users of diferent prediction abilities react to social efects and online endorsements. The estimation of quantile treatment efects (QTEs) allows us to discover the social efects on the entire distribution of prediction accuracy. By conducting a more complete treatment efect analysis, we find that QTEs are heterogeneous—users of intermediate prediction abilities react most positively to both audience size and online endorsement, whereas users of very high or very low prediction abilities exhibit less pronounced increases in their prediction accuracy.

Our contribution is threefold. First, to our knowledge, this is the first attempt in the information systems (IS) literature to causally quantify the impact of social efects on the quality of UGC. Although prior research on UGC has focused on how audience size influences posting frequency in social media (Toubia and Stephen 2013), how audience size afects the type of content people share (Barasch and Berger 2014), how content contribution levels in Wikipedia respond to audience size (Zhang and Zhu 2011), and how social comparison can increase individual contributions to an online community (Chen et al. 2010), very few studies have investigated how audience size and social endorsements shape content quality, especially in a prediction market context. The unique setup in our social-mediabased prediction markets highlights the role of social image or self-presentation on content quality. Note that the study context of most prior literature is blogging (Zhang and Zhu 2011, Toubia and Stephen 2013). As for blogging, the criterion for evaluating the quality of a user’s content contribution is relatively subjective. One blog article could fit some audience’s taste perfectly while misfit the others’ (horizontal diferentiation). However, in a prediction market, such criterion of quality evaluation becomes relatively objective (vertical quality). Therefore, the blogging literature has mainly focused on a context of horizontal competition. A social-media-based prediction market ofers us a unique context to examine the impact on contribution quality in the presence of vertical competition.<sup>6</sup> In our study, a prediction market is a context where such vertical quality measure of UGC exists,<sup>7</sup> and is a vehicle to carry out an experiment studying how audience size and social endorsement afect vertical quality.

Recently, there has been a stream of emerging market design literature on eliciting high-quality contributions in UGC platforms (Ghosh and McAfee 2011, Ghosh 2012, Anderson et al. 2013, Easley and Ghosh 2013, Ghosh and Hummel 2014). This stream of studies has mainly taken a game-theoretic approach to the problem of incentivizing high-content quality in UGC platforms. For instance, Ghosh and Hummel (2014) analyze equilibrium behavior in a rank-order mechanism, which is widely used by UGC platforms to incentivize high-quality content. Many websites rank UGC using viewer votes, displaying higher-quality contributions more prominently and suppressing lower-quality ones. Anderson et al. (2013) and Easley and Ghosh (2013) investigate how gamification via badge design can be most efectively used for incentivizing efort on UGC platforms. Unlike the prior game-theoretical models, we focus on empirically identifying the causal mechanism of social image on high-quality content contribution. Essentially, a practical question is what incentive strategy a website manager should employ to create high-quality content. The prior literature has addressed that the use of rank-order mechanism and gamification can incentivize higher-quality contributions in equilibrium. In an empirical setting, we use a field experiment to show that besides rank-order mechanism and gamification, social image (broadcast correct predictions to followers) can be another efective incentive strategy to elicit high-quality content contribution. Given the understanding of social image from the social psychology and economics literature on what constitutes a reward for these contributors, we are able to design a social-media-based system to incentivize desirable outcomes.

Second, our study contributes to the knowledge contribution and public goods provision literature by estimating a causal impact on knowledge contribution quality. The prior literature posited that a variety of drivers motivate the knowledge contribution behavior and private provision of public goods.<sup>8</sup> Wasko and Faraj (2005) find that reputation and altruism can be important motivations underlying knowledge contribution. Ma and Agarwal (2007) show that an online community member’s perceived identity verification is positively related to her knowledge contribution. Xia et al. (2012) demonstrate that reciprocity may drive sharing behaviors. However, most of these studies used survey-based data or observational data. Therefore, they focused more on verifying the association between underlying drivers and the level of knowledge contribution instead of establishing causality. Our research seeks to address this gap by conducting a field experiment that allows us to quantify the causal impact on knowledge contribution quality. Establishing a credible casual relation is extremely important in the design of improving UGC quality and in the implementation of theoretical insights. In the surveybased data or observational data used by the prior literature, observations were generated by a process such as “users who contribute high-quality content also interact with other online users frequently and have a large audience size,” but we want to examine what would happen if we change to a data generating process such as “increasing the frequency of social interaction level and the audience size,” and precisely measure the magnitude of the beneficial efects. Our approach of exogenously adding more followers for prediction market participants is similar to that of Toubia and Stephen (2013), who are able to make a causal statement regarding the efect of audience size on prediction accuracy. However, unlike their focus on ATEs, we further examine the heterogeneity of treatment efects and estimate QTEs of social factors.

Third, although the prior studies provide theoretical insights into knowledge contribution in general (Wasko and Faraj 2005), the implementation of these theoretical insights is still in its infancy. Practitioners cannot work only with the conceptual models. Instead, the practice calls for an engineering approach: how to design concrete incentive strategies to increase knowledge contribution quality from the perspective of designers and managers of an online community. The answer to this question does not merely depend on how well we understand the general principles that govern knowledge contribution, but also on how well we can bring this knowledge to bear on practical market design and implementation. To bridge the gap between theory and design (practical implementation), we take a step further and investigate how to use social-media technology to promote knowledge contribution quality in the context of prediction markets. Our incentive strategy is concrete and practical: incorporating social media into prediction market systems and making individual predictions observable to their social connections. Actually, practitioners have begun to realize the role of incorporating social media into prediction market systems. Montgomery et al. (2013) document that Ford has built an internal social platform for its prediction markets. Our randomized field experiment suggests that the individual prediction accuracy in prediction markets can be dramatically improved through an integration with social media and other well-designed social technologies. Our quantile treatment analysis further shows that prediction markets can selectively target users of intermediate ability level to obtain the largest improvement in prediction accuracy. In sum, our study highlights an efective approach of integrating social aspects to the design of a prediction market system to supplement existing forecasting methods.

## 1.3. Theoretical Development

Although audience size or social endorsement does not provide any new information, it changes the underlying incentives of users to contribute more time and efort in acquiring private information and in improving individual prediction performance. Our underlying logic chain is as follows: (1) Social image (social approval) incentivizes participants to contribute more eforts. Increasing audience size and social endorsements enhances the image value of broadcasting correct predictions to followers, and, as a consequence, leads to more contribution eforts. (2) More contribution eforts lead to a higher level of individual prediction accuracy (quality of contribution). The theoretical framework is depicted in Figure 2.

Figure 2. Theoretical Framework of Audience Size and Social Endorsement Efects  
![](/api/attachments/AP45XVN3/fulltext/images/080e167d2dc6547b544122907f9cb0aaf510b44fb223a0daf9a7a650de6942f6.jpg)

First, we use image motivation theory to justify why social image and emotionally prompted social approval is capable of incentivizing contribution eforts, and why increasing audience size and social endorsements can enhance image motivation.

What motivates users to contribute eforts? Harsanyi (1969, p. 127) ofer two explanations: “People’s behavior can largely be explained in terms of two dominant interests: economic gain and social acceptance.” Following these two explanations, on one hand, prior economics literature has mainly focused on how people change their behavior in response to changes in economic gain (Fehr and Falk 2002). On the other hand, the behavioral role of social rewards (social acceptance) is stressed in social exchange theory (Blau 1964). Social exchange theory posits that people engage in contributing behavior based on social rewards such as approval, status, and respect. Social image is one of the most important motivations for social rewards (Ariely et al. 2009), and it refers to an individual’s tendency to be motivated by others’ perceptions. Image motivation or self-presentation therefore captures the idea that people desire to be perceived as “good” (to be liked and respected by others), and present themselves in a positive light. The tendency to self-enhance, or bolster the self-concept, is one of the most central human motivations (Barasch and Berger 2014). The admiration that is expressed by others is a typical example of a social reward based on social image. For instance, social image may explain why people seldom give anonymously to charities and why many organizations make an individual’s contributions explicitly visible to others (Glazer and Konrad 1996). In general, social rewards are not based on explicit contractual arrangements, but are triggered by spontaneous positive emotions that can be interpreted as social approval (Gächter and Fehr 1999).

A potential way an individual can benefit from contributing is the perception that contributing enhances her social image. If individuals are looking to gain social approval of their behavior, they should provide more contribution eforts to yield a positive social image. Fehr and Falk (2002, p. 705) point out that “Social approval means that we are the objects of others’ admiration while disapproval means that we are the objects of others’ disgust and contempt. Approval, therefore, makes us proud and happy while disapproval causes embarrassment and shame and makes us unhappy. These social rewards and punishments are a basic “currency” that induces children and adults alike to perform certain activities and avoid others.” A stream of literature on public goods provision shows that the opportunity to express social approval generates a strong increase in contribution quantity using controlled laboratory experiments (Gächter and Fehr 1999, Rege and Telle 2004). In the context of ofline fundraising campaigns, social approval can significantly increase individual contributions (Frey and Meier 2004, Shang and Croson 2009). In the online contexts, social image also plays an important role in increasing individual contributions to online communities (Chen et al. 2010).

As argued above, social image (social approval) is influenced by what other people think of the individual. A crucial property of social image is its dependency on visibility (audience size); after all, image is a consequence of what others think. If the social image utility obtained from a prosocial activity (such as providing high-quality content in online communities) is positive, larger audience size will increase the image utility of conducting prosocial behavior and, as a consequence, will lead to more contribution eforts (Ariely et al. 2009). Additionally, Blau (1964) demonstrates that the social image motivation can be moderated by social distance: social approval becomes increasingly important with the decrease of social distance among people because the social distance among people is likely to be smaller the more often they interact with each other, and the interaction intensity is positively correlated with the importance of approval incentives. In a laboratory experiment, Gächter and Fehr (1999) confirm that social image incentives are more important the greater the density of social interaction among people. Therefore, like audience size, social endorsements should also enhance the image utility of conducting prosocial behavior and lead to more contribution eforts.

In our specific context of a social-media-based prediction market, no monetary incentive is involved.<sup>9</sup> Therefore, we focus on the role of social image (social approval) in incentivizing high-quality predictions. The role of social image in this social-media-based prediction market is highlighted by the platform design: The Twitter-based prediction market automatically tweets users’ predictions, and shows followers whether the predictions are correct. In this social context, a user may want to be perceived as a “prediction master” and be respected by her followers. The image motivation incentivizes participants to contribute more eforts.

It is worth noting that, in our experiment, we did not force participants to participate and predict. The fact that participants choose to participate in the prediction tasks suggests that they are confident about their predictions. More specifically, social image causes a selection efect: if participants worry that their predictions could be wrong, they will not make predictions in the first place. A participant is more likely to participate in the prediction tasks when she is more confident about her information. More importantly, when a participant is more confident, the role of her positive image utility will outweigh the role of her negative image utility (because she thinks that her prediction is very likely to be correct), and as a result, her expected image utility will be positive. Therefore, positive expected image utility can incentivize participants to contribute more eforts and improve prediction quality. In the case of donating to a charity, there is no uncertainty, and social image utility is always positive. In our context, if a prediction is correct/wrong, positive/negative social image utility will be generated. However, our key argument is that the expected image utility is positive because participants will choose to participate only when they are confident about their predictions.

Additionally, the potential negative image utility caused by a wrong prediction may also incentivize participants to contribute more eforts and improve prediction quality. If the positive image utility caused by a correct prediction is a “carrot” approach, then the negative image utility caused by a wrong prediction is a “stick” approach. To avoid the negative image utility caused by a wrong prediction, a participant may spend more time and efort to collect information and make a more careful prediction. Therefore, in our context, negative image utility may incentivize participants to contribute more eforts, and hence improve prediction accuracy.

The second part of our logic chain is that more contribution eforts lead to a higher quality of contribution (prediction accuracy). The relationship between eforts and contribution quality has been extensively studied in the literature. Prior studies on costly information acquisition adopted the paradigm that if individuals contribute more time and efort, they will acquire more precise private information and improve their decision making (Burguet and Vives 2000, Gabaix et al. 2006). The finance literature also confirmed the widely used modeling assumption that in financial markets, if a trader contributes more efort (a fixed cost), she will receive a more precise private signal about the underlying asset value (Grossman 1976, Grossman and Stiglitz 1980). In UGC platforms, Ghosh and McAfee (2011) and Ghosh and Hummel (2014) demonstrate that the cost of making a contribution (contribution efort) is increasing in its quality. In a prediction market context, the prior literature documented the positive impact of information acquisition eforts on individual prediction accuracy (Fang et al. 2010, Qiu et al. 2014a). Similarly, in our context, the key mechanism is that a participant will receive more precise private information if she contributes more time and efort on information acquisition, and as a consequence, she will make a more precise prediction.

The rest of the paper proceeds as follows. In Section 2, we detail the experiment design and the data. Sections 3 and 4 describe the empirical framework and present results. In Section 5, we discuss the managerial implications. Finally, Section 6 concludes the paper.

## 2. Experimental Design and Data Description

Our randomized field experiment consists of treatments that involve manipulating the audience size and/or the level of online endorsement. More specifically, we randomly select 240 participants from the subject pool of experienced users participating in a social-media-based prediction market. Since all of the participants are experienced users, they are familiar with the prediction market website, and the learning efect over time is minimized. Among these participants, 120 people were assigned to the control group, 60 people were assigned to the treatment group with Audience Size efect (referred to as the Treatment group AS hereafter), and 60 people were assigned to the treatment group with Audience Size and Online Endorsement efect (referred to as the Treatment group AS <sup>+</sup> OE hereafter).

To generate an audience size efect, we created and managed 100 fake/synthetic Twitter accounts and gradually made each of these fake Twitter accounts follow every public account in both treatment groups over a 60-day period.<sup>10</sup> Following Toubia and Stephen (2013), we made our fake Twitter accounts as realistic as possible.<sup>11</sup> In addition, for every public account in Treatment group AS <sup>+</sup> OE, we used the fake Twitter accounts created earlier to randomly favorite the treated account’s tweets a total of five times over the 60-day period, and to randomly retweet the treated account’s tweets with an average frequency of twice per day. These actions of our fake Twitter accounts generate a synthetic online endorsement efect. In summary, subjects in Treatment group AS received the audience size treatment, and subjects in Treatment group AS <sup>+</sup> OE received both the audience size treatment and the online endorsement treatment. The treated participants were not aware of the field experiment.

Figure 3. Timeline of the Experiment  
![](/api/attachments/AP45XVN3/fulltext/images/f17feb99db14c1770c15d9a4a117d08328d2ebc90463135555a885c0a5ec3b15.jpg)

The timeline of our experimental design is shown in Figure 3. Before we applied the treatments, all 240 participants were randomly assigned to complete 25 prediction tasks on various topics in the three-month pretreatment period (please refer to Table A.1 in Online Appendix A for a list of the prediction content). We implemented treatments AS and AS <sup>+</sup> OE in the subsequent two months. After the treatment period,<sup>12</sup> we invited all 240 participants to complete another 25 prediction tasks. This setup allows us to compare each participant’s prediction accuracy before and after the treatments. To ensure the validity of our experimental protocol, we conducted several pilot tests to check the diferences in the outcome variable as a result of the treatments. Our goal was to make sure that there were major efects that difered between the control group and the treatment group, so that we could be assured of the validity of our experimental protocol and proceed to the larger scale field experiment.

We report the summary statistics of participants’ connectedness and prediction accuracy in Table 1. A participant’s indegree is defined as the number of followers the participant has on Twitter, the outdegree is the number of users the participant follows, and prediction accuracy is defined as the percentage of correct predictions made by each participant. We can see that the control and treatment groups have comparable levels of average indegree, outdegree, and prediction accuracy prior to the treatment. Next, we conduct a series of tests to further verify that the randomization between treatment and control groups was done appropriately, and the results are shown in Table 2. We first use a two-sample t-test to compare the pretreatment levels of (1) average indegree, (2) average outdegree, and (3) average prediction accuracy, across the control and treatment groups. None of the results are significant, which suggests that these groups are similar prior to the treatment.

Since the t-test relies heavily on the asymptotic distributional assumption and may not perform well under small sample size, we also perform a Monte Carlo Fisher–Pitman permutation test with 200,000 permutations and a Wilcoxon rank-sum test on these averages. Both the Monte Carlo Fisher–Pitman permutation test and the Wilcoxon rank-sum test use a nonparametric approach to compute the sampling distribution where no assumption on the sampling distribution is required, and they tend to have greater eficiency than the t-test on nonnormal distributions. As shown in Table 2, none of these test results were statistically significant. To determine if there are any pretreatment diferences in the distribution of participants’ degree and prediction accuracy for the control and treatment groups, the Kolmogorov–Smirnov test is performed. The results suggest that we cannot reject the null hypothesis that the control and treatment samples are drawn from the same distribution.

Prior to the treatment, on average, the treated account’s tweets were favorited 4.2 times over two months; and in the treatment period, on average, the treated account’s tweets were favorited 8.9 times (average organic favorites <sup>+</sup> average fake favorites <sup></sup> 3.9 <sup>+</sup> 5) over two months. Prior to the treatment, on average, the treated account’s tweets were retweeted 1.1 times per day; and, in the treatment period, on average, each treated account’s tweets were retweeted 2.8 times per day (average organic retweets<sup>+</sup>average fake retweets <sup></sup> $0 . 8 + 2 )$ . From the data, we can see that the organic rate of social endorsements is consistent over time, and the main treatment efects come from our exogenous manipulations.

Table 1. Summary Statistics of Participants’ Connectedness and Prediction Accuracy

<table><tr><td rowspan="2">Variable</td><td colspan="2">Control group</td><td colspan="2">Treatment AS group</td><td colspan="2">Treatment AS + OE group</td></tr><tr><td>Mean</td><td>Std. dev.</td><td>Mean</td><td>Std. dev.</td><td>Mean</td><td>Std. dev.</td></tr><tr><td>Pretreatment Outdegree</td><td>92.983</td><td>73.248</td><td>86.5</td><td>56.829</td><td>84.167</td><td>69.497</td></tr><tr><td>Pretreatment Indegree</td><td>109.850</td><td>78.384</td><td>107.433</td><td>84.402</td><td>101.933</td><td>80.633</td></tr><tr><td>Pretreatment Prediction accuracy</td><td>0.565</td><td>0.167</td><td>0.548</td><td>0.161</td><td>0.521</td><td>0.175</td></tr><tr><td>Posttreatment Prediction accuracy</td><td>0.493</td><td>0.179</td><td>0.631</td><td>0.205</td><td>0.645</td><td>0.218</td></tr></table>

Table 2. Statistical Tests Between Control and Treatment Groups

<table><tr><td>Tests</td><td>Control group vs. treatment AS group</td><td>Control group vs. treatment AS + OE group</td></tr><tr><td colspan="3">(a) Comparing outdegree before treatment using different tests</td></tr><tr><td>Two-sample t test</td><td>p = 0.672</td><td>p = 0.586</td></tr><tr><td>Fisher-Pitman permutation test</td><td>p = 0.684</td><td>p = 0.594</td></tr><tr><td>Wilcoxon rank-sum test</td><td>p = 0.939</td><td>p = 0.593</td></tr><tr><td>Kolmogorov-Smirnov test</td><td>p = 0.759</td><td>p = 0.681</td></tr><tr><td colspan="3">(b) Comparing indegree before treatment using different tests</td></tr><tr><td>Two-sample t test</td><td>p = 0.706</td><td>p = 0.652</td></tr><tr><td>Fisher-Pitman permutation test</td><td>p = 0.702</td><td>p = 0.656</td></tr><tr><td>Wilcoxon rank-sum test</td><td>p = 0.767</td><td>p = 0.611</td></tr><tr><td>Kolmogorov-Smirnov test</td><td>p = 0.673</td><td>p = 0.545</td></tr><tr><td colspan="3">(c) Comparing prediction accuracy before treatment using different tests</td></tr><tr><td>Two-sample t test</td><td>p = 0.640</td><td>p = 0.250</td></tr><tr><td>Fisher-Pitman permutation test</td><td>p = 0.650</td><td>p = 0.258</td></tr><tr><td>Wilcoxon rank-sum test</td><td>p = 0.577</td><td>p = 0.384</td></tr><tr><td>Kolmogorov-Smirnov test</td><td>p = 0.635</td><td>p = 0.519</td></tr></table>

Table 3 shows the correlation among participants’ connectedness and prediction accuracy before treatment. The positive correlation between prediction accuracy and indegree before treatment is well established. What is unclear is whether this correlation is indeed driven by the actual social efect, or by the endogenously determined social network. In the first case, a larger number of followers actually leads to a higher level of prediction accuracy, which is the major underlying causal mechanism we hope to identify. However, the growing literature on the identification of social efects has recognized an important confounding factor: the network structure is endogenously determined (Manski 1993, Aral and Walker 2011, Bapna and Umyarov 2015). In our context, this means that the number of followers in a social-media-based prediction market may be the result of past prediction performance (i.e., the individuals may self-select their friends and tend to associate with participants with high predictive ability). Both the social efects and the endogenous network structure explanations are theoretically plausible, and they need to be empirically distinguished. Failure to account for the endogenous network structure might lead to an overestimate of the social efect. Our field experiment design helps us sidestep this potential identification issue, because we are able to exogenously increase the number of participants’ Twitter followers in the treatment group. Therefore, our randomized field experiment approach can better identify the causal social efect on the resulting prediction accuracy.

Table 3. Correlations Among Variables Before Treatment

<table><tr><td></td><td>Outdegree</td><td>Indegree</td><td>Prediction accuracy</td></tr><tr><td>Outdegree</td><td>1</td><td></td><td></td></tr><tr><td>Indegree</td><td>0.526 (p = 0.00)</td><td>1</td><td></td></tr><tr><td>Prediction accuracy</td><td>0.300 (p = 0.00)</td><td>0.442 (p = 0.00)</td><td>1</td></tr></table>

## 3. Empirical Framework

We use a DID method to estimate the impact of audience size and online endorsement on prediction accuracy. The DID method helps us use data with a time dimension to control for unobserved but fixed omitted variables. Recall that in our experimental design, each participant’s prediction accuracy is observed in both the pretreatment and posttreatment periods— both treatment groups are exposed to their respective treatment in the posttreatment period, but not in the pretreatment period. The control group is not exposed to any treatment during either period.

Before presenting the DID estimator, we start with two intuitive nonparametric comparisons of average prediction accuracy to establish the baseline efects. Let $Y _ { 0 } ^ { \mathrm { A S } }$ and $Y _ { 1 } ^ { \mathrm { A S } }$ be the sample averages of the prediction accuracy for Treatment group AS before and after treatment, respectively; let $\breve { Y _ { 0 } ^ { \mathrm { A S O E } } }$ and $Y _ { 1 } ^ { \mathrm { A S O E } }$ be the sample averages of the prediction accuracy for Treatment group AS<sup>+</sup>OE before and after treatment, respectively; and let $Y _ { 0 } ^ { \mathrm { C } }$ and $Y _ { 1 } ^ { \mathrm { C } }$ be the corresponding sample averages of the prediction accuracy for the control group. The two nonparametric comparisons include the following:

(i) A simple treatment vs. control estimator. This estimator allows us to compare the posttreatment average prediction accuracy of both treatment groups with the control group. Note that this estimator does not consider pretreatment outcomes. Specifically, the estimator comparing Treatment group AS and the control group is given by

$$
\theta_ {\mathrm{AS}} = Y _ {1} ^ {\mathrm{AS}} - Y _ {1} ^ {\mathrm{C}} = 0. 6 3 1 - 0. 4 9 3 = 0. 1 3 8,
$$

and the estimator comparing Treatment group $\mathrm { A S + O E }$ and the control group is given by

$$
\theta_ {\mathrm{ASOE}} = Y _ {1} ^ {\mathrm{ASOE}} - Y _ {1} ^ {\mathrm{C}} = 0. 6 4 5 - 0. 4 9 3 = 0. 1 5 2.
$$

(ii) A simple pre vs. post estimator. This estimator allows us to compare the average prediction accuracy before and after treatments for both treatment groups. Specifically, the estimator comparing Treatment group AS before and after the treatment is given by

$$
\delta_ {\mathrm{AS}} = Y _ {1} ^ {\mathrm{AS}} - Y _ {0} ^ {\mathrm{AS}} = 0. 6 3 1 - 0. 5 4 8 = 0. 0 8 3,
$$

and the estimator comparing treatment group AS <sup>+</sup> OE before and after the treatment is given by

$$
\delta_ {\mathrm{ASOE}} = Y _ {1} ^ {\mathrm{ASOE}} - Y _ {0} ^ {\mathrm{ASOE}} = 0. 6 4 5 - 0. 5 2 1 = 0. 1 2 4.
$$

These two simple estimators show the baseline efect of treatments AS and $\mathrm { A S + O E }$

We then construct a DID estimator to remove some potential biases that the aforementioned two simple estimators could not address: (i) the bias resulting from the permanent diference between the control and treatment groups; and (ii) the bias resulting from comparisons over time in the treatment groups that could be the result of trends<sup>13</sup> (Wooldridge 2002). In our DID regression, the outcome of interest, the participant i’s prediction accuracy, $Y _ { i t } ,$ is modeled by the following equation:

$$
\begin{array}{r} Y _ {i t} = \beta_ {0} + \beta_ {1} A S _ {i} + \beta_ {2} A S O E _ {i} + \beta_ {3} t + \beta_ {4} (t \cdot A S _ {i}) \\ + \beta_ {5} (t \cdot A S O E _ {i}) + \varepsilon_ {i t}, \end{array}\tag{1}
$$

where $A S _ { i }$ and $A S O E _ { i }$ are dummy variables corresponding to whether participant i belongs to Treatment group AS and Treatment group ${ \mathrm { A } } { \mathrm { S } } { \mathrm { + O E } } ,$ respectively, and t is a dummy variable with $t = 1$ corresponding to the posttreatment period. The dummy variables $A S _ { i }$ and $A S O E _ { i }$ capture any potential baseline diferences between the treatment and control groups prior to any treatment. In other words, the coeficients $\beta _ { 1 }$ and $\beta _ { 2 }$ measure the specific efects of being assigned to Treatment groups $\mathsf { A } \bar { \mathsf { S } }$ and $\mathrm { A S + O E }$ , which account for average permanent diferences between the control group and the treatment group. The coeficient associated with the time period dummy, $\beta _ { 3 } ,$ captures the time trend common to both treatment and control groups. The coeficients of interest are the interaction terms, $\beta _ { 4 }$ and $\beta _ { 5 } ,$ which measure the actual efects of treatments AS and $\mathsf { A S + O E }$

The key argument of the DID method is the “parallel paths” assumption, which posits that the average change in the control group represents the counterfactual change in the treatment group had there been no treatments (Abadie 2005). In other words, aside from those changes resulting from the treatment, any diferences between the treatment and control groups should be random. In our randomized field experiment, two specific experimental designs ensure that these interventions/treatments themselves are exogenous. First, participants in the control and treatment groups were randomly selected from the subject pool. Second, the increases in audience size and online endorsement (treatments) in our experiment were exogenous variations in the sense that fake followers were added to the treated users.

## 4. Empirical Results

## 4.1. Average Treatment Efects of Audience Size and Online Endorsement

The DID empirical results are shown in Table 4. The coeficients of interests are the interaction terms Treatment AS <sup>·</sup> t and (Treatment AS <sup>+</sup> OE) <sup>·</sup> t, each capturing the treatment efects of audience size and that of both the audience size and online social endorsement, respectively. Column 1 shows the ordinary least squares (OLS) results of the DID model. We find that the coeficients of the interaction terms are significantly positive, suggesting that the larger audience size increases the focal participant’s prediction accuracy by almost 15.5%; the extra online social endorsement can contribute to an additional 4.1% <sup>(</sup>19.6 <sup>−</sup> 15.5 <sup></sup> 4.1) increase in prediction accuracy.

To alleviate concerns about the failure to meet standard regression assumptions such as clustering and heteroskedasticity, we also compute the robust t statistics using the Huber–White sandwich estimators in column 2, and the results are robust. Another potential issue is the small sample size in our setup, which is a common problem for experimental methods. Since the validity of t-statistics depends on the asymptotic distribution of large samples, bootstrapping is useful for estimating the distribution of a statistic without resorting to asymptotic properties, and is particularly useful when the sample size is insuficient for straightforward statistical inference. Therefore, we use bootstrapping to compute the clustered standard errors. Specifically, we draw a sample of clusters with replacement, and repeat this process 10,000 times to compute the bootstrapped standard errors. As can be seen in column 3, our results are robust. In column 4, we estimate the fixed efects model to control for unobserved individual heterogeneity, and the results are similar.

Table 4. Estimation Results of the DID Model

<table><tr><td>Variables</td><td>(1)OLS</td><td>(2)Robust variance</td><td>(3)Cluster bootstrapping</td><td>(4)Fixed effects robust variance</td></tr><tr><td>T</td><td>-0.0727**(-2.183)</td><td>-0.0727**(-2.290)</td><td>-0.0727**(-2.286)</td><td>-0.0727**(-2.369)</td></tr><tr><td>Treatment AS</td><td>-0.0173(-0.425)</td><td>-0.0173(-0.476)</td><td>-0.0173(-0.453)</td><td></td></tr><tr><td>Treatment AS + OE</td><td>-0.0440(-1.079)</td><td>-0.0440(-1.143)</td><td>-0.0440(-1.171)</td><td></td></tr><tr><td>Treatment AS · t</td><td>0.155***(2.694)</td><td>0.155***(2.722)</td><td>0.155***(2.645)</td><td>0.155***(2.891)</td></tr><tr><td>(Treatment AS + OE) · t</td><td>0.196***(3.399)</td><td>0.196***(3.269)</td><td>0.196***(3.393)</td><td>0.196***(3.073)</td></tr><tr><td>Constant</td><td>0.565***(24.02)</td><td>0.565***(26.05)</td><td>0.565***(26.25)</td><td>0.550***(46.81)</td></tr><tr><td>Observations</td><td>480</td><td>480</td><td>480</td><td>480</td></tr><tr><td>R-squared</td><td>0.181</td><td>0.181</td><td>0.181</td><td>0.152</td></tr></table>

Note. t-statistics are in parentheses.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

The detailed description of the fixed efects model can be found in Online Appendix B.

Figures 4(a) and 4(b) show our treatment efects graphically. If the “parallel paths” assumption holds in the DID estimation, the average change in the control group (diamond marker in Figure 4) will represent the counterfactual change in the treatment group had there been no treatments (circle marker in Figure 4). In other words, the treatment efects can be measured by the diference in prediction accuracy between the treatment group and the counterfactual group.

## 4.2. Robustness Checks

To check whether our results are robust across diferent levels of indegrees and outdegrees, we split our sample into subsamples according to diferent levels of initial indegrees and outdegrees. In robustness check I, we split our sample into two subsamples according to initial indegrees: whether or not a participant has a top 50 percentile in terms of indegree. In robustness check II, we split our sample into two subsamples according to initial outdegrees: whether or not a participant has a top 50 percentile in terms of outdegree. The estimation results are presented in Table 5. We find that our results are robust across the subsamples: the treatment efects are significantly positive. It is worth noting that the treatment efect is significantly stronger for the top 50 percentile outdegree group than for the bottom 50 percentile outdegree group. A plausible explanation for this finding is that as the audience size and social endorsements (treatment) increase, participants are incentivized to use their information-sourcing channels (outdegree) to improve the prediction accuracy. Since the top 50 percentile group has a larger number of information-sourcing channels (outdegree), participants who belong to that group can more efectively improve their prediction accuracy.

Figure 4. (Color online) The Treatment Efects in the DID Model  
(a) The effect of treatment AS in the DID model  
![](/api/attachments/AP45XVN3/fulltext/images/0bb4826bbdefbeb0c9439105c06e7dacdc8a2b7ee899b8a622ae827b9ee3c133.jpg)

(b) The effect of treatment AS + OE in the DID model  
![](/api/attachments/AP45XVN3/fulltext/images/5ef9c6d77c81d0490545ddeebe6c3e96a5844ed9efbf91a2c6d6a5c250ff28f0.jpg)

Table 5. Subsample Estimation Results: Diferent Levels of Initial Indegrees and Outdegress

<table><tr><td rowspan="2">Variables</td><td>(1) Indegrees</td><td>(2) Indegress</td><td>(3) Outdegrees</td><td>(4) Outdegress</td></tr><tr><td>Bottom 50 percentile</td><td>Top 50 percentile</td><td>Bottom 50 percentile</td><td>Top 50 percentile</td></tr><tr><td>t</td><td>-0.0902**(-2.101)</td><td>-0.0627**(-2.218)</td><td>-0.0833**(-2.205)</td><td>-0.0692**(-2.176)</td></tr><tr><td>Treatment AS</td><td>-0.0264(-0.815)</td><td>-0.0156(-0.725)</td><td>-0.0297(-0.886)</td><td>-0.0148(-0.528)</td></tr><tr><td>Treatment AS + OE</td><td>-0.0352(-1.482)</td><td>-0.0705(-1.627)</td><td>-0.0308(-1.102)</td><td>-0.0682(-1.533)</td></tr><tr><td>Treatment AS · t</td><td>0.147**(2.176)</td><td>0.158***(3.204)</td><td>0.0812***(3.145)</td><td>0.171***(4.533)</td></tr><tr><td>(Treatment AS + OE) · t</td><td>0.172***(2.892)</td><td>0.232***(3.625)</td><td>0.106***(4.827)</td><td>0.318***(5.624)</td></tr><tr><td>R-squared</td><td>0.132</td><td>0.167</td><td>0.154</td><td>0.171</td></tr></table>

Note. Robust t-statistics are in parentheses.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

Additionally, we conduct F-tests to examine whether the coeficient on AS <sup>·</sup> t is statistically diferent from that on (AS <sup>+</sup> OE) <sup>·</sup> t. In the whole sample, they are not statistically significant $( p > 0 . 0 5 )$ . However, when we look at the top 50 percentile subsample in terms of outdegree, the coeficient on $( \mathrm { A S + O E } ) \cdot$ t is significantly greater than the coeficient on ${ \sf A S } \cdot t ~ \left( p = 0 . 0 3 < 0 . 0 5 \right)$ which suggests the impact of online endorsement is more significant when the participants have larger outdegrees.

We also conduct a robustness check on quantifying the magnitude of the impact of percentage changes in audience size and social endowments. We run a regression using the posttreatment subsamples as follows:

$$
Y _ {i 1} = \beta_ {0} + \beta_ {1} \text { Percent\_AS } _ {i} + \beta_ {2} \text { Percent\_OE } _ {i} + \varepsilon_ {i 1},
$$

where $Y _ { i 1 }$ is the posttreatment prediction accuracy, $P e r c e n t \_ A S _ { i }$ is the percentage increase in the number of followers, and Percent\_OE is the percentage increase in social endorsements. We find that the estimation results are robust: a percentage increase in audience size and social endorsements can significantly improve individual prediction accuracy. The estimation results are shown in Table 6: On average, a 10% increase in followers can increase prediction accuracy by 3.82%; and a 10% increase in online endorsements can improve prediction accuracy by 2.01%.

## 4.3. Quantile Treatment Efects of Audience Size and Online Endorsement

Previous studies on voluntary knowledge provision and content contribution (Zhang and Zhu 2011, Toubia and Stephen 2013) have mainly focused on estimating how social interactions or audience size afect users average content contribution (conditional mean). In our study, we use a quantile-regression approach to further estimate the casual efects of audience size and online endorsement on the entire distribution of the user’s prediction accuracy. It is possible that the magnitude of the efects of audience size and online endorsements might vary significantly at diferent quantiles of the distribution of prediction accuracy. For instance, the prediction accuracy of participants who have high prediction ability (at the high end of the distribution of prediction accuracy) may tend to be less afected by audience size or online endorsement, because these participants would have already put eforts and made predictions carefully even in the absence of treatments, and therefore there would be limited room for further improving their prediction accuracy. Cowgill and Zitzewitz (2015) empirically find that prediction market participants difer significantly in their prediction skill levels.

Figures 5(a) and 5(b) show our DID estimates of the ATE in equation (1) in horizontal dashed lines and the estimates of quantile treatments connected by the solid line, with the shaded area being their 95% confidence intervals. Note that there are seven estimated quantile regressions with the 0.2th, . . ., and 0.8th quantiles, respectively. In Figure 5(a), we find that the quantile estimates exhibit some heterogeneity across quantiles, ranging from 0.10 at the 0.2th quantile to 0.29 at the 0.6th quantile. In other words, the quantile estimates are significantly larger at the intermediate quantiles than those at the low and high ends (the quantile estimate at the 60th percentile is the largest). To examine whether the observed diferences among the estimates are statistically significant across quantiles, we further conduct interquantile tests of the equality of pairwise treatment efects (Koenker and Hallock 2001). More specifically, we test whether the QTE in the 0.6th quantile is the same as the QTE in the lower quantile (the 0.2th quantile), or the upper quantile (0.8th quantile). The tests show that the treatment efect at the 0.6th quantile is significantly diferent from that at the 0.2th quantile or the 0.8th quantile at the 5% significance level. In summary, we can conclude that it is important to take into account the distribution heterogeneity to study social efects on prediction accuracy. In Figure 5(b), the estimated QTEs of treatment AS <sup>+</sup> OE have similar patterns, which indicate that our results are quite robust.

Table 6. The Role of Percentage Increase in Followers and Endorsements

<table><tr><td>Variables</td><td>(1) OLS</td></tr><tr><td>Percent_AS</td><td>0.00382***(3.192)</td></tr><tr><td>Percent_OE</td><td>0.00201***(2.724)</td></tr><tr><td>R-squared</td><td>0.129</td></tr></table>

Note. Robust t-statistics are in parentheses.  
<sup>∗</sup>p < 0.1; <sup>∗∗</sup>p < 0.05; <sup>∗∗∗</sup>p < 0.01.

Figure 5. (Color online) Quantile Estimation Results in the DID Model  
![](/api/attachments/AP45XVN3/fulltext/images/990147d777acae311c937b0e2a8c4d26ae3ff3f2f909a379bb5f0a6a5761f94f.jpg)

![](/api/attachments/AP45XVN3/fulltext/images/356a49913ff305807590cd9a30f6ba28cad5c1053d69b9a5fb930dfc8b6d826f.jpg)  
Confidence intervals Quantile estimates DID estimate in Equation (1)

These findings suggest that (i) the magnitude of the impacts of audience size and online endorsement is smaller for participants who have extremely high or low prediction ability (at the two ends of the distribution of prediction accuracy); and (ii) the efects of audience size and online endorsements are strongest for participants who have an intermediate level of prediction ability. A possible explanation for the diference between the two ends and the intermediate quantiles of the distribution is as follows: At the low quantiles of prediction accuracy, even if participants try to put more eforts on prediction tasks, their prediction accuracy may not improve much because of their low prediction ability; for participants at high quantiles, there would be little room for improvement since their predictions might already be precise. By contrast, at intermediate quantiles, the impacts of audience size and online endorsement are found to be larger because participants who have an intermediate level of prediction ability might be able to improve their prediction performance dramatically when they put more eforts on prediction tasks and try to show high prediction performance to their followers. Here we interpret “participants with intermediate prediction accuracy” as “participants with intermediate prediction ability” because in the prediction market practice, a designer cannot directly observe a participant’s prediction ability, but can observe her prediction accuracy (performance). Usually, a designer will interpret a participant’s prediction performance/accuracy as a measure of her prediction ability.<sup>14</sup>

The prior studies have investigated diferences in incentive efects between high- and low-ability groups. For instance, Leuven et al. (2010) find that the incentives have no efects or even negative efects on achievement of low-ability students, whereas they have large and positive impacts on achievement of high-ability students. Therefore, it is consistent with our finding that the impact of incentive efects is small at the bottom of the performance distribution. However, our result suggests that the impact of incentive efects is also small (instead of large) at the top of the performance distribution. It is worth noting the task diference between our study and Leuven et al. (2010): Leuven et al. (2010) mainly focus on the incentive efects on students’ test scores, while in our study, we look at individuals’ prediction accuracy, which is more conceptual in nature. Psychological research (Lepper and Greene 1978) has shown that motivators were more efective as tasks were less conceptual. In the context of test scores, students can memorize a series of facts that may adequately prepare them. By putting in more efort, a student with high test scores can still get a significant improvement in her performance. By contrast, it is much more dificult for prediction market participants to prepare for a specific prediction task. For a participant who has already achieved high prediction performance, it is really dificult to improve her accuracy by putting in more efort. After all, the final prediction accuracy will be afected by uncertainty considerably.

In sum, Figure 5 indicates that average treatment efects estimated from the DID method tend to underestimate the impact of audience size and online endorsement at the intermediate quantiles of the distribution of prediction accuracy, and tend to overestimate the impact at the two ends. This has important managerial implications on the design of prediction markets. The quantile regression results from our field experiment suggest that facilitating social interactions for prediction market participants who have intermediate levels of prediction ability might be an efective strategy to induce high-quality predictions from participants.

## 4.4. Extensions

4.4.1. The Impact of Social Efects on User Participation. Since a thin market is a problem of prediction markets, we further examine the impact of the social efects on user participation. Note that, theoretically, the impact of audience size and social endorsements on user participation can be positive or negative. On one hand, audience size and social endorsements are likely to have adverse efects on user participation because people do not want to broadcast that they were wrong to their followers. On the other hand, people may be more willing to participate especially when they are confident about their predictions because they want to let their followers know that their predictions were correct. Therefore, both signs are theoretically plausible, and it is an empirical question to examine the impact of audience size and social endorsements on contribution quantity. In our social-media-based platform, besides the focal prediction markets<sup>15</sup> (we invite participants to join 25 prediction markets before the treatment and another 25 prediction markets after the treatment), the participants in the control and treatment groups also chose some other prediction markets to participate in before and after the treatment period. Therefore, we use the number of prediction markets each participant participated in to measure user participation. If a user participated in a larger number of prediction markets in a given time period (three months in our context), we would say that this user has a higher level of user participation.

We conduct a t-test and find that, before the treatment, the average number of prediction markets a participant joined in the treatment group is not significantly diferent from that in the control group $( p > 0 . 1 )$ .

Table 7. The Impact of Social Efects on User Participation

<table><tr><td>Variables</td><td>(1)User participation as dependent variable</td></tr><tr><td>T</td><td>-2.024(-0.783)</td></tr><tr><td>Treatment AS</td><td>-2.326(-1.102)</td></tr><tr><td>Treatment AS + OE</td><td>-1.145(-0.673)</td></tr><tr><td>Treatment AS · t</td><td>4.556***(3.024)</td></tr><tr><td>(Treatment AS + OE) · t</td><td>9.213***(4.535)</td></tr><tr><td>R-squared</td><td>0.115</td></tr></table>

Note. Robust t-statistics are in parentheses.  
<sup>∗</sup>p < 0.1; <sup>∗∗</sup>p < 0.05; <sup>∗∗∗</sup>p < 0.01.

However, after the treatment, treated participants are more likely to make predictions and participate in more prediction markets than controlled participants $( p < 0 . 0 5 )$ . This result provides some suggestive evidence that the positive impact of audience size and social endorsements on contribution quantity outweighs the negative one: the total efect of audience size and social endorsements on user participation is positive. An additional regression analysis is presented in Table 7. The dependent variable is the number of prediction markets a participant participated in. We find that the impact of audience size and social endorsements on user participation is significantly positive.

A plausible explanation for this finding (the positive impact of the social efects outweighs the negative one) is the overconfidence of participants in prediction markets: participants view themselves as more able to make correct predictions, and thus are more likely to participate in prediction markets. Actually, a large stream of literature on economics and finance has documented investor overconfidence in financial markets (Daniel et al. 1998, Scheinkman and Xiong 2003).

4.4.2. The Impact of Social Efects on Aggregated Prediction Market Performance. We also investigate if the aggregated prediction market performance is afected by the social efects while individuals are more accurate. Theoretically speaking, broadcasting predictions to followers is a double-edged sword in terms of prediction market performance: On one hand, it can incentivize users to provide high-quality predictions; on the other hand, it might make individual information correlated. It is an empirical question to examine the net efect. It is worth noting that our experimental treatments are not specifically designed for examining the aggregated prediction market performance (e.g., the number of prediction markets is relatively small in our experiment: only 25 posttreatment prediction markets), so our findings below are mostly suggestive correlations.

Table 8. The Role of Social Efects on Prediction Market Accuracy

<table><tr><td>Variables</td><td>(1) OLS</td><td>(2) Bootstrapping</td></tr><tr><td>Prop_Treated</td><td>-0.645***(3.445)</td><td>-0.645***(3.012)</td></tr><tr><td>Number_Participant</td><td>-0.000648***(3.256)</td><td>-0.000648***(2.828)</td></tr><tr><td>R-squared</td><td>0.112</td><td>0.112</td></tr></table>

Note. Robust/bootstrapped t-statistics are in parentheses. $^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1 .$

We run the following regression equation using the posttreatment subsamples:

$$
\begin{array}{c} M k t \_ e r r o r _ {j} = \beta_ {0} + \beta_ {1} P r o p \_ T r e a t e d _ {j} \\ + \beta_ {2} N u m b e r \_ P a r t i c i p a n t _ {j} + \varepsilon_ {j}, \end{array}
$$

where the dependent variable, prediction market error, is measured by Mkt\_error: the distance between the prediction market probability $M _ { j }$ and the actual binary outcome $R _ { j } , ^ { 1 6 } \ : | \boldsymbol { M } _ { j } { \dot { - } } \boldsymbol { R } _ { j } | .$ , Prop\_Treated (between 0 and 1) is the proportion of treated participants over the number of total participants in prediction market $j ,$ and Number\_Participan $\dot { \mathbf { \zeta } } _ { j }$ is the number of participants in prediction market $j$ . The estimation results are presented in Table 8. We are interested in the coeficient on Prop\_Treated, and it is significantly negative in column 1. The implication is that a percent increase in the proportion of treated participants may reduce prediction error by 0.645%, so a prediction market with a high proportion of treated participants outperforms a prediction market with a low proportion of treated participants. This empirical result tentatively suggests that broadcasting predictions to followers may have a positive impact on prediction market accuracy. To address the concern of small sample size, we look at the bootstrapped t statistics, and the results are similar.

## 5. Managerial Implications

Our study contributes to an increasingly extensive empirical literature on prediction markets and voluntary content contribution by conducting a randomized field experiment to establish the causal efect of audience size and online endorsement on prediction market participants’ prediction accuracy. Our experimental results show that the integration of social media into prediction market systems can efectively incentivize participants to achieve better forecasting performance without providing any monetary reward. Plott and Chen (2002) find that the monetary incentives encourage participants to search for the best information. Our research complements their study and suggests that the nonmonetary rewards, such as social efects and online endorsement from social media, can also create efective incentives for participants to provide highquality predictions.

Our study has important managerial implications on how to introduce social technologies and integrate social media into prediction markets for practitioners looking to implement their own prediction markets. Several companies, such as Inkling Markets and Consensus Point, provide prediction market platforms to help organizations aggregate decentralized information and make more informed decisions in public or corporate prediction markets. In the design of prediction markets, a challenge is how to incentivize and engage participants to share their insights in a quick, eficient way. Our experimental evidence supports that social efects and reputational concerns may play a key role in improving participants’ prediction accuracy, and provides a powerful motivation for prediction market participants to supply thoughtful responses. The results from our ATE analysis suggest that practitioners should consider integration of social-media/corporate internal social networks when designing their own public/corporate prediction markets. Our QTE results further demonstrate that the social-media-embedded prediction markets should target people of intermediate abilities to obtain the most significant prediction improvement. It is worth noting that our results are more applicable to public prediction markets than corporate internal prediction markets because (i) for the confidentiality concern, companies would be reluctant to push the prediction activities to public social networking sites (such as Twitter), and (ii) if companies limit pushing prediction activities to internal social networking, the audience and endorsement size would be too small to incentivize employees.

In prediction market practice, a designer is able to use observational data to estimate the correlation between prediction accuracy and audience size. However, the pure correlation does not provide enough guidance for a prediction market designer about whether or not to incorporate social media or internal social platform into their original prediction markets. When the prediction market designer makes such a decision, it will involve a cost-benefit analysis. The cost of incorporating social media or internal social platform into prediction markets is mainly a technical cost and should be straightforward to estimate. However, the benefit is directly related to the causal efect of social audience size and online endorsement on prediction market participants’ prediction accuracy, and is dificult to estimate from the correlations in observational data. Failure to account for the endogenous network structure (i.e., the individuals may self-select their friends and tend to associate with participants with high predictive ability) might lead to an overestimate of the social efect using observational data. The manipulation of the audience size and social endorsements in our experiment provides an exogenous variation to identify the casual impact, and can help the prediction market designer quantify the benefit of incorporating social media or internal social platform into prediction markets.

A designer of Google’s prediction markets (GPM) pointed out that Google “should make the trading more social . . . should build in more social features and personalization into GPM. It is pretty clear that Googlers trade to build their reputations. We should make these reputations more visible on an opt-in basis . . . Market operators should focus more on social rewards and the infrastructure and processes to deliver them . . . Confidential trading prevents traders from proudly sharing their accomplishments. How often inside corporations do you hear some variant of ’I told you so’? There is demand among employees to be able to take credit for accurate predictions on particular projects. Market operators need to give employees the tools they need to share their predictions.” (Coles et al. 2007, pp. 2, 13, 14, 20, 21). In our study, just like that designer suggested, we focus on how to build “the infrastructure and processes” to deliver social rewards and examine the causal impact of giving participants “the tools they need to share their predictions” on individual prediction performance.

Our research has broader implications on the design of online community-based question answering sites (involving vertical quality of UGC), such as Quora, Stack Exchange, and Stack Overflow. Nowadays, millions of users actively contribute to various types of online communities on a daily basis. Motivations for contributing to online communities have been of great interest to practitioners and scholars. A typical example of public goods are open source projects (Singh et al. 2011). A natural question is asked by (Lerner and Tirole 2002, p. 198), “Why would thousands of top-notch software developers contribute for free to the creation of a public good?” Generally, the diferent motivations to contribute have been classified as either intrinsic or extrinsic (Roberts et al. 2006). In our context of prediction markets, intrinsic motivations can be interpreted as the enjoyment or accomplishment in the performance of the prediction tasks, which are linked to the satisfaction of basic human needs for competence, control, and autonomy (Deci and Ryan 2000). By contrast, extrinsic motivations refer to nonmonetary rewards, such as social image or reputation, and monetary rewards as a result of the outcome of the prediction tasks. In our study, social audience size and online endorsements belong to nonmonetary extrinsic motivations (social image). Osterloh and Frey (2000) find the “crowding out efect”: under certain conditions, extrinsic motivations may displace intrinsic motivations. However, our findings suggest that the crowding out efect motivated by social image should be limited, because we can observe significant positive efects of social audience size and online endorsement on the quality of predictions.<sup>17</sup> One plausible explanation is that social audience size and online endorsements are symbolic extrinsic incentives (social image), and prior studies documented that the crowding out efect is much less for symbolic than monetary incentives (Roberts et al. 2006).

The efect of online users’ social interactions on their contribution to electronic communities has been widely examined using archival data in diferent contexts (Kankanhalli et al. 2005, Goes et al. 2014). In the context of social-media-based prediction markets, our study establishes a causal identification of social efects on individual prediction accuracy using a field experiment. More broadly, our results suggest that incorporating social features, such as the ability to follow and observe others’ activities, could be an efective approach to boost individuals’ contribution using nonmonetary incentives.

## 6. Conclusions and Future Research Directions

We conduct a randomized field experiment on a socialmedia-based prediction market to study users’ contribution behaviors. Through a DID method, we are able to estimate both the average treatment efect and the quantile treatment efect of audience size and endorsement on users’ prediction performance. We empirically find that an increase in audience size leads to an improvement in a focal user’s prediction accuracy, and that a higher level of online endorsement also leads to prediction improvements. More interestingly, our experimental results show that the quantile treatment efects are heterogeneous: users of intermediate prediction ability respond most positively to an increase in social audience size and online endorsement. These findings highlight how designers can make use of social media to improve prediction market design.

While our paper establishes a causal relationship between social efects and contribution behaviors, we recognize several limitations. First, in field experiments, it is usually dificult to isolate the behavioral mechanisms underlying the findings. In our specific context, the underlying mechanism behind the causal efect of social treatments is less clear. Our theoretical argument is that the social image incentivizes participants to contribute more eforts, and hence the prediction accuracy is improved. In Online Appendix C, we provide suggestive evidence showing that the participants put out more efort because of social image.

However, we do realize that there are alternative explanations for the suggestive evidence because we do not have a precise measure of user efort in our experimental settings. Investigating the underlying mechanism behind the causal efect of social treatments is an interesting possible future research direction.

Second, our field experiment was conducted in an online social-media-embedded prediction market. The prediction tasks were not real business-related forecasting problems (e.g., demand forecasting). Therefore, future studies are needed to establish the efects of audience size and online endorsement in a prediction market integrated with real business workflow. Third, a potential problem in integrating social media into prediction markets is the issue of free riding that could be caused by the automatic information sharing in our experiment context: users’ predictions will be automatically pushed to their followers’ timelines, and followers can free ride on focal users’ predictions (Qiu et al. 2014a). In our field experiment, this free-riding efect was minimized, because those randomly selected participants in our sample rarely followed each other during our experiment period. However, in real prediction markets, participants are likely to be connected on social media or internal social networks. As a consequence, integrating social media into prediction markets becomes a more complicated incentive problem involving the trade-of between social efects and freeriding efects. Finally, in this study, we primarily focus on individual prediction accuracy. As a future research direction, it would be interesting to carefully examine the efects of audience size and online endorsements on the overall prediction market performance in an experiment with a larger number of prediction markets.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three anonymous reviewers for their detailed and constructive comments. The authors also thank Shun-Yang Lee, De Liu, and the participants at the 2015 Workshop on Information Technologies and Systems (WITS) for their helpful feedback.

## Endnotes

<sup>1</sup> See http://www.consensuspoint.com/wp-content/themes/radius/ whitepapers/BestBuy\_Casestudy.pdf (accessed September 22, 2015).

<sup>2</sup> Seehttp://www.consensuspoint.com/wp-content/themes/radius/ whitepapers/GE\_Casestudy.pdf (accessed September 22, 2015).

<sup>3</sup> Notable examples are the Iowa Electronic Markets, PredictIt, Hollywood Stock Exchange, Foresight Exchange, and Smarkets.

<sup>4</sup> Plott and Chen (2002) show that the internal prediction market in Hewlett-Packard can reduce the uncertainty of forecasting making sales. Guo et al. (2006) propose a macro prediction market to efectively elicit useful information and reduce systematic demand risk in supply chains. Hopman (2007) document how Intel used prediction markets to manage demand risk.

<sup>5</sup> Because online gambling is outlawed in the United States through federal laws and many state laws as well, most prediction markets that target U.S. users operate with “play money” rather than “real money.” Notable exceptions are the Iowa Electronic Markets, which is operated by the University of Iowa under the cover of a no-action letter from the Commodity Futures Trading Commission, and PredictIt, which is operated by Victoria University of Wellington under the cover of a similar no-action letter.

<sup>6</sup> The vertical competition in our context should be more intense than the horizontal competition in the context of blogging. Prior literature shows that competition afects incentives to contribute. For instance, in a controlled laboratory experiment, Dufy and Kornienko (2010) find that the natural human competitiveness might be exploited to stimulate charitable giving. In other words, giving behavior may be afected by intrinsic competitive motives, e.g., with regard to one’s standing relative to others. The intrinsic competitive motive in a prediction market is greater than that in a blog context. The underlying reason is that the objective criterion of quality evaluation in a prediction market makes social comparison more direct and efective. In a broad sense, social comparison (relating one’s own features to those of others, and vice versa) is an important characteristic of human social life (Buunk and Mussweiler 2001). The previous studies on social comparison demonstrate that the use of social comparison can increase contributions in fundraising campaigns (Frey and Meier 2004, Shang and Croson 2009) and contributions to an online community (Chen et al. 2010). Our prediction market context difers from a blog context that is widely studied in the literature because more intense vertical competition in a prediction market can lead to a more direct and efective social comparison that provides a greater nonpecuniary incentive to motivate high-quality contributions.

<sup>7</sup> A vertical quality context can be found in the online communitybased question answering sites, such as Quora, Stack Exchange, and Stack Overflow.

<sup>8</sup> The incentive of private provision of public goods is a fundamental question in the public goods literature (Bergstrom et al. 1986, Chen et al. 2010, Zhang and Zhu 2011). A major focus of the literature is the free-rider hypothesis: as group size grows, individual contribution levels decline (Bergstrom et al. 1986). The free-rider problem is also related to the literature on collective action: disincentives of free riding discourage joint action by individuals in the pursuit of a common goal (Van Zomeren et al. 2008). To resolve the problem of free riding, researchers have focused on designing incentive-compatible mechanisms for private provision of public goods.

<sup>9</sup> Servan-Schreiber et al. (2004) argue that the use of real money is just one among many ways of motivating knowledgeable traders to provide high-quality contribution. In the case of play money, knowledgeable traders can be motivated by social incentives.

<sup>10</sup> The average increase in the number of organic followers of the treated participants in the treatment period is not statistically different from that of the control group. In other words, the organic growth rates of the treatment and control groups are similar.

<sup>11</sup> Each fake Twitter account has a profile picture. The names of the fake users were generated using a random name generator (http:// www.behindthename.com/random/). These accounts posted tweets regularly and followed an average of six other fake accounts as well as some celebrities and organizations.

<sup>12</sup> There are no treatments for the control group.

<sup>13</sup> In our context, the trends mean that the dificulty level of the 25 prediction tasks before the treatment might be diferent from that after the treatment.

<sup>14</sup> In other contexts, for instance, Leuven et al. (2010) use students’ test performance to measure their ability.

<sup>15</sup> In our experiment, each participant was invited to join 25 prediction markets before and after the treatment period by receiving emails from the experimenter. Besides that, they were free to join other prediction markets in the social-media-based platform. The reason we chose 25 focal prediction markets before and after the treatment is that we want the treated and controlled participants to make predictions on the same set of events so that we can give a fair comparison of prediction accuracy.

<sup>16</sup> In our context, the final forecast of a prediction market is a probability $M _ { j } ,$ which is between 0 and 1. The actual outcome in reality, $R _ { j }$ , is either 0 or 1 (whether the event happens).

<sup>17</sup> Even if there is a slight crowding out efect, the total efects of social audience size and online endorsement are significantly positive.

## References

Abadie A (2005) Semiparametric diference-in-diferences estimators. Rev. Econom. Stud. 72(1):1–19.

Anderson A, Huttenlocher D, Kleinberg J, Leskovec J (2013) Steering user behavior with badges. Schwabe D, Almeida V, Glaser H, eds. Proc. 22nd Internat. Conf. World Wide Web (ACM, New York), 95–106.

Aral S, Walker D (2011) Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Sci. 57(9):1623–1639.

Ariely D, Bracha A, Meier S (2009) Doing good or doing well? Image motivation and monetary incentives in behaving prosocially. Amer. Econom. Rev. 99(1):544–555.

Bapna R, Umyarov A (2015) Do your online friends make you pay? A randomized field experiment in an online music social network. Management Sci. 61(8):1902–1920.

Barasch A, Berger J (2014) Broadcasting and narrowcasting: How audience size afects what people share. J. Marketing Res. 51(3):286–299.

Berg JE, Forsythe R, Nelson F, Rietz T (2008) Results from a dozen years of election futures markets research. Plott CR, Smitt VL, eds. Handbook of Experimental Economics Results, Vol. 1 (North Holland, Amsterdam), 742–751.

Bergstrom T, Blume L, Varian H (1986) On the private provision of public goods. J. Public Econom. 29(1):25–49.

Blau P (1964) Exchange and Power in Social Life (Transaction Publishers, New Brunswick, NJ).

Broughton P (2013) Prediction markets: Value among the crowd. Financial Times (April 24), https://www.ft.com/content/f03f c956-9586-11e2-a151-00144feabdc0.

Burguet R, Vives X (2000) Social learning and costly information acquisition. Econom. Theory 15(1):185–205.

Buunk BP, Mussweiler T (2001) New directions in social comparison research. Eur. J. Soc. Psych. 31(5):467–475.

Chen Y, Harper FM, Konstan J, Li SX (2010) Social comparisons and contributions to online communities: A field experiment on MovieLens. Amer. Econom. Rev. 100(4):1358–1398.

Coles PA, Lakhani KR, McAfee A (2007) Prediction markets at Google. Harvard Business School Case 9-607-088.

Cowgill B, Zitzewitz E (2015) Corporate prediction markets: Evidence from Google, Ford, and firm X\*. Rev. Econom. Stud. 82(4):1309–1341.

Daniel K, Hirshleifer D, Subrahmanyam A (1998) Investor psychology and security market under—and overreactions. J. Finance 53(6):1839–1885.

Deci EL, Ryan RM (2000) The “what” and “why” of goal pursuits: Human needs and the self-determination of behavior. Psych. Inquiry 11(4):227–268.

Dufy J, Kornienko T (2010) Does competition afect giving? J. Econom. Behav. Organ. 74(1):82–103.

Easley D, Ghosh A (2013) Incentives, gamification, and game theory: An economic approach to badge design. Conitzer V, McAfee P, eds. Proc. Fourteenth ACM Conf. Electronic Commerce (ACM, New York), 359–376.

Fang F, Stinchcombe MB, Whinston AB (2010) Proper scoring rules with arbitrary value functions. J. Math. Econom. 46(6):1200–1210.

Fehr E, Falk A (2002) Psychological foundations of incentives. Eur. Econom. Rev. 46(4):687–724.

Frey BS, Meier S (2004) Social comparisons and pro-social behavior: Testing “conditional cooperation” in a field experiment. Amer. Econom. Rev. 94(5):1717–1722.

Gabaix X, Laibson D, Moloche G, Weinberg S (2006) Costly information acquisition: Experimental analysis of a boundedly rational model. Amer. Econom. Rev. 96(4):1043–1068.

Gächter S, Fehr E (1999) Collective action as a social exchange. J. Econom. Behav. Organ. 39(4):341–369.

Ghosh A (2012) Social computing and user-generated content: A game-theoretic approach. ACM SIGecom Exchanges 11(2):16–21.

Ghosh A, Hummel P (2014) A game-theoretic analysis of rankorder mechanisms for user-generated content. J. Econom. Theory 154:349–374.

Ghosh A, McAfee P (2011) Incentivizing high-quality user-generated content. Bertino E, Kumar R, eds. Proc. 20th Internat. Conf. World Wide Web (ACM, New York), 137–146.

Glazer A, Konrad KA (1996) A signaling explanation for charity. Amer. Econom. Rev. 86(4):1019–1028.

Goes PB, Lin M, Au Yeung CM (2014) “Popularity efect” in usergenerated content: Evidence from online product reviews. Inform. Systems Res. 25(2):222–238.

Grossman S (1976) On the eficiency of competitive stock markets where trades have diverse information. J. Finance 31(2): 573–585.

Grossman SJ, Stiglitz JE (1980) On the impossibility of informationally eficient markets. Amer. Econom. Rev. 70(3):393–408.

Guo Z, Fang F, Whinston AB (2006) Supply chain information sharing in a macro prediction market. Decision Support Systems 42(3):1944–1958.

Harsanyi JC (1969) Rational-choice models of political behavior vs. functionalist and conformist theories. World Politics 21(4): 513–538.

Healy PJ, Linardi S, Lowery JR, Ledyard JO (2010) Prediction markets: Alternative mechanisms for complex environments with few traders. Management Sci. 56(11):1977–1996.

Hopman JW (2007) Using forecasting markets to manage demand risk. Intel Technol. J. 11(2):127–136.

Kankanhalli A, Tan BC, Wei KK (2005) Contributing knowledge to electronic knowledge repositories: An empirical investigation. MIS Quart. 29(1):113–143.

Koenker R, Hallock K (2001) Quantile regression: An introduction. J. Econom. Perspect. 15(4):43–56.

Lepper MR, Greene DE (1978) The Hidden Costs of Reward: New Perspectives on the Psychology of Human Motivation (Lawrence Erlbaum, Hillsdale, NJ).

Lerner J, Tirole J (2002) Some simple economics of open source. J. Indust. Econom. 50(2):197–234.

Leuven E, Oosterbeek H, Klaauw B (2010) The efect of financial rewards on students’ achievement: Evidence from a randomized experiment. J. Eur. Econom. Assoc. 8(6):1243–1265.

Ma M, Agarwal R (2007) Through a glass darkly: Information technology design, identity verification, and knowledge contribution in online communities. Inform. Systems Res. 18(1):42–67.

Manski CF (1993) Identification of endogenous social efects: The reflection problem. Rev. Econom. Stud. 60(3):531–542.

Montgomery TA, Stieg PM, Cavaretta MJ, Moraal PE (2013) Experience from hosting a corporate prediction market: Benefits beyond the forecasts. Dhillon IS, Koren Y, Ghani R, Senator TE, Bradley P, Parekh R, He J, Grossman RL, Uthurusamy R, eds. Proc. 19th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 1384–1392.

Osterloh M, Frey BS (2000) Motivation, knowledge transfer, and organizational forms. Organ. Sci. 11(5):538–550.

Plott CR, Chen KY (2002) Information aggregation mechanisms: Concept, design and implementation for a sales forecasting problem. Working Paper 1131, California Institute of Technology Social Science, Pasadena.

Qiu L, Rui H, Whinston AB (2014a) Efects of social networks on prediction markets: Examination in a controlled experiment. J. Management Inform. Systems 30(4):235–268.

Qiu L, Rui H, Whinston AB (2014b) The impact of social network structures on prediction market accuracy in the presence of insider information. J. Management Inform. Systems 31(1): 145–172.

Rege M, Telle K (2004) The impact of social approval and framing on cooperation in public good situations. J. Public Econom. 88(7):1625–1644.

Ren Y, Kraut R, Kiesler S (2007) Applying common identity and bond theory to design of online communities. Organ. Stud. 28(3): 377–408.

Roberts JA, Hann IH, Slaughter SA (2006) Understanding the motivations, participation, and performance of open source software developers: A longitudinal study of the Apache projects. Management Sci. 52(7):984–999.

Scheinkman JA, Xiong W (2003) Overconfidence and speculative bubbles. J. Political Econom. 111(6):1183–1220.

Schlack JW (2015) Ask your customers for predictions, not preferences. Harvard Bus. Rev. (January 5), https://hbr.org/2015/01/ ask-your-customers-for-predictions-not-preferences.

Servan-Schreiber E, Wolfers J, Pennock DM, Galebach B (2004) Prediction markets: Does money matter? Electronic Markets 14(3):243–251.

Shang J, Croson R (2009) A field experiment in charitable contribution: The impact of social information on the voluntary provision of public goods. Econom. J. 119(540):1422–1439.

Shriver SK, Nair HS, Hofstetter R (2013) Social ties and usergenerated content: Evidence from an online social network. Management Sci. 59(6):1425–1443.

Singh PV, Tan Y, Mookerjee V (2011) Network efects: The influence of structural social capital on open source project success. MIS Quart. 35(4):813–829.

Spann M, Skiera B (2003) Internet-based virtual stock markets for business forecasting. Management Sci. 49(10):1310–1326.

Toubia O, Stephen AT (2013) Intrinsic vs. image-related utility in social media: Why do people contribute content to Twitter? Marketing Sci. 32(3):368–392.

Van Zomeren M, Postmes T, Spears R (2008) Toward an integrative social identity model of collective action: A quantitative research synthesis of three socio-psychological perspectives. Psych. Bull. 134(4):504–535.

Wasko MM, Faraj S (2005) Why should I share? Examining social capital and knowledge contribution in electronic networks of practice. MIS Quart. 29(1):35–57.

Wolfers J, Zitzewitz E (2004) Prediction markets. J. Econom. Perspect. 18(2):107–126.

Wooldridge JM (2002) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge, MA).

Xia M, Huang Y, Duan W, Whinston AB (2012) To continue sharing or not to continue sharing? An empirical analysis of user decision in peer-to-peer sharing networks. Inform. Systems Res. 23(1): 247–259.

Zhang X, Wang C (2012) Network positions and contributions to online public goods: The case of Chinese Wikipedia. J. Management Inform. Systems 29(2):11–40.

Zhang X, Zhu F (2011) Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev. 101(4):1601–1615.
