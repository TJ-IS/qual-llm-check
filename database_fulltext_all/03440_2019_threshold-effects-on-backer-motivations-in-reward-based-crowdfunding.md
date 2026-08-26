---
otero_id: 3440
otero_key: "QEVYWFUC"
title: "Threshold Effects on Backer Motivations in Reward-Based Crowdfunding"
authors: "Gen Li; Jing Wang"
year: "2019"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1599499"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Threshold Effects on Backer Motivations in Reward-Based Crowdfunding

Gen Li & Jing Wang

To cite this article: Gen Li & Jing Wang (2019) Threshold Effects on Backer Motivations in Reward-Based Crowdfunding, Journal of Management Information Systems, 36:2, 546-573, DOI: 10.1080/07421222.2019.1599499

To link to this article: https://doi.org/10.1080/07421222.2019.1599499

![](/api/attachments/QEVYWFUC/fulltext/images/16e1f52d3cf5cfa707569a73544fd75e3a56ea169de362665bcceb772a28302b.jpg)

View supplementary material

![](/api/attachments/QEVYWFUC/fulltext/images/ded5527b30ca6a580d74c20c7da6099d7a96156a2d5c539e5fa4ee7196a08364.jpg)

Published online: 14 Jun 2019.

![](/api/attachments/QEVYWFUC/fulltext/images/4a5f38ee3c7820e251049328312fe6c0607cc72989d0322477f0b8c7b1ec3a2d.jpg)

Submit your article to this journal

![](/api/attachments/QEVYWFUC/fulltext/images/ed165585c1ba3f6dc1a58c2f0400de06aaf1346b3d2d96dd340f34e464df288c.jpg)

Article views: 168

![](/api/attachments/QEVYWFUC/fulltext/images/c88b5dae943cc505f5424e64fd37d246e82162ba93264ea444547a18108dbdfa.jpg)

View Crossmark data

# Threshold Effects on Backer Motivations in Reward-Based Crowdfunding

GEN LI AND JING WANG

Gen Li (gliam@connect.ust.hk) is a Ph.D. candidate in Information Systems at the School of Business and Management, Hong Kong University of Science and Technology. He is interested in the area of crowdfunding, knowledge communities, and social networks.

Jing Wang (jwang@ust.hk; corresponding author) is an Assistant Professor of Information Systems at the School of Business and Management, Hong Kong University of Science and Technology. She received her Ph.D. in Information Systems from the Stern School of Business, New York University. Her research interests include crowdsourcing, online labor markets, crowdfunding, user-generated content, and data mining. Dr. Wang’s work has appeared in Proceedings of the National Academy of Science, Management Science, Information Systems Research, Data Mining and Knowledge Discovery, and several top Computer Science conferences.

ABSTRACT: Reward-based crowdfunding has been increasingly used by entrepreneurs and small businesses to raise capital for their creative projects. To keep the money raised, most platforms require that the total amount of pledged money must exceed a pre-specified funding goal. In this study, we aim to gain a better understanding of backer motivations by empirically investigating their pledging and sharing patterns at different stages of achieving the funding threshold. By analyzing a unique dataset that records the bi-hourly backer support for 1,058 successful Kickstarter projects, we find two threshold-induced effects. First, there is a sharp increase in the number of backers and Facebook shares during the few hours when the project approaches its funding threshold. Second, the numbers of backers and Facebook shares are substantially higher in the few days before the threshold is reached than in the few days afterward. We show that both effects are more pronounced in public-good than in private-good project categories. Our findings provide clear evidence for a strong effect of prosocial motivation in driving backer behaviors. In addition, the results support that both goal proximity and project prosociality have a positive impact on the prosocial motivation of backers.

KEY WORDS AND PHRASES: reward-based crowdfunding, prosocial motivation, economic motivation, goal proximity, uncertainty, public goods, private goods, fundraising.

## Introduction

The recent rise of crowdfunding—raising funds from a large number of individuals, each contributing a small amount of money—has attracted increasing attention from industry practitioners and academic researchers alike. There are four common types of crowdfunding models.<sup>1</sup> The donation-based model (e.g., GoFundMe) gives no return to donors and is often used to fundraise for causes such as disaster relief, medical care, and poverty alleviation. The lending-based model (e.g., LendingClub) offers lenders attractive interest rates and facilitates crowdfunded loans to individuals for purposes like debt consolidation, home improvement, car financing, etc. The reward-based model (e.g., Kickstarter) enables entrepreneurs to collect money from backers and compensate them with some tangible non-financial rewards such as a copy of the new product. The equity-based model (e.g., AngelList) is similar to the reward-based model in that it is also used to fund start-ups ventures, but differs in that investors are compensated with equity shares of firms rather than non-financial rewards.

In this study, we are interested in reward-based crowdfunding, which has now become a viable alternative for entrepreneurs and small businesses to raise capital. Many creative projects, spanning various fields such as art, film, games, music, and technology, are successfully funded through this type of crowdfunding. As of October 2018, one of the largest reward-based crowdfunding platforms, Kickstarter, had raised \$3.9 billion for more than 150,000 successful projects from over 15.0 million backers all over the world.<sup>2</sup> Another leading platform, Indiegogo, had raised \$1.3 billion for more than 800,000 innovative ideas, as of January 2018.<sup>3</sup>

Despite the popularity of reward-based crowdfunding platforms, the motivations behind backers’ pledging and sharing behaviors are not fully understood. Previous studies [10, 11, 16, 23] based on survey data have uncovered both the prosocial motivation<sup>4</sup> of pure altruism and impure altruism (e.g., warm glow, image concerns) and the economic motivation to collect rewards. However, the findings on the relative importance of different motivations in driving backers’ behaviors are mixed, with some indicating a strong effect of prosocial motivation [10, 11] and others reporting a dominant role of economic incentive [16]. In addition, survey studies based on selfreports may suffer from potential response biases such as social desirability bias<sup>5</sup> [22]. In this study, we aim to gain a deeper understanding of backer motivations by empirically investigating their dynamic behavioral patterns at various funding stages.

To achieve this objective, we leverage the all-or-nothing mechanism employed by most of the reward-based crowdfunding platforms (e.g., Kickstarter). That is, a project creator sets a fundraising goal (threshold) and a time period, then backers come to pledge their money to the project and/or share project information on social media sites; the creator keeps the pledged money only if the amount raised reaches the threshold by the funding deadline. Existing literature (e.g., Agrawal et al. [2], Mollick [43], and Thies et al. [51]) on backers’ decision-making in reward-based crowdfunding addresses the funding period as a whole and overlooks the role of funding status (i.e., progress in reaching the goal). However, backers who pledge at different stages of achieving the funding threshold may possess different motivations.

Before the project threshold is reached, prosocial motivation plays an important role in backers’ decision making. Backers may pledge their money or share project information to their friends because they want to help project creators and support causes [10, 23, 47]. The factors that drive their prosocial behavior may include feeling good about helping others, making a meaningful impact, developing a favorable image, and others [11, 23]. The desire to collect rewards may be another driver of backers’ support behavior. However, the uncertainty about the quality and future success of the project at this time may weaken this economic motivation and discourage backers from making contributions [11, 25].

As the project approaches its funding threshold, the risk of project failure is greatly reduced. Backers who pledge their money at this time can tip the project from failure to success [26]. The heightened level of perceived impact is likely to give backers a great sense of achievement and satisfaction, which in turn strengthens their prosocial motivation and results in a substantial increase in their likelihood of pledging. The word-of-mouth referrals may also be accelerated during this critical period as sharing project information on social networks can bolster the fundraising [33, 51].

After the threshold is reached, backers become certain about the success of the project and would perceive reaching the funding goal as a sign of high project quality [11]. As a result, the economic motivation to receive rewards is enhanced [47]. Their funding behavior at this stage is more like the pre-ordering in advance selling and their sharing behavior is highly similar to making product recommendations in online buying. However, the prosocial motivation is likely to be weakened because the project will be implemented regardless of the actions of future backers.

The possible varying numbers of backers and social media shares at different stages of reaching the funding threshold can help reveal the relative importance of different motivations in backers’ decision-making processes. In this study, we investigate backers’ pledging and sharing patterns before, close to, and after the project threshold is reached by analyzing a unique panel dataset from Kickstarter. To capture the dynamics of backer behaviors at a fine-grained level, we scraped project information from Kickstarter on a bi-hourly basis. To minimize the influence of various non-motivational factors that could possibly cause fluctuations in backer support, we narrow our scope to a focal time period that is not more than 48 hours from the threshold-reaching time interval both before and after.<sup>6</sup> We employ a fixed-effects negative binomial model to examine the changes in backer behaviors, and find two types of threshold-induced effects.

First, there is a dramatic increase in the number of backers and Facebook shares when the project approaches its funding threshold. The numbers of backers and Facebook shares in the two-hour interval during which the threshold is reached are 204.96% and 58.25% larger, respectively, than those in time intervals during the two days before. The result gives support to the heightened level of prosocial motivation among backers when the project is close to reaching its goal. Second, the numbers of backers and Facebook shares are higher in the two days before the threshold is reached than in the two days afterward. On average, the numbers of backers and Facebook shares per interval are

50.23% and 41.62% larger, respectively, before the threshold than afterward. The higher level of backer support in the before period indicates that the positive effect of prosocial motivation outweighs the economic disutility from project uncertainty and quality concerns in reward-based crowdfunding.

Previous studies have suggested that the prosociality of campaigns can affect people’s participation decisions in that public goods are more likely to induce one’s prosocial motivation than private goods (e.g., Filiz-Ozbay and Ozbay [21], Hong et al. [33], and Smith et al. [50]). We divide all the projects into public-good projects and private-good projects based on the nature of the rewards and examine how the threshold effects vary with project types. The results show that both the sharp peaks in the number of backers and Facebook shares around the threshold-reaching time and the higher level of backer support before the threshold than afterward are more pronounced for public-good projects, which provides additional evidence that the observed threshold effects are likely to be explained by backers’ strong prosocial motivation.

Finally, we conduct a set of analyses to address other explanations that may arise from creators’ marketing efforts or own contributions. We also show that our findings are robust to the use of subgroup analysis, shorter or longer time windows, wider time interval, fixed-effects Poisson model, and pledge amount as dependent variable.

Our paper first contributes to the large body of work on goal-gradient behavior in both individual and collective settings (e.g., Cheema and Bagchi [15], Cryder et al. [17], Kivetz et al. [35], and Wu et al. [52]), which demonstrates that people become more motivated as they approach a goal because of the sense of achievement and heightened satisfaction at the tipping point. Our work enriches this stream of research by identifying and quantifying the positive effect of goal proximity on backers’ prosocial motivation for pledging and sharing in the context of rewardbased crowdfunding. Furthermore, we show that this behavior is more pronounced in public-good projects than in private-good projects, indicating that the prosociality of crowdfunding projects strengthens backers’ urge to achieve the goal.

Second, our work adds to the literature on backers’ pledging and sharing motivation in reward-based crowdfunding (e.g., Bretschneider and Leimeister [11], Cholakova and Clarysse [16], and Gerber and Hui [23]). Backers in such platforms exhibit both prosocial and economic motivations. By focusing on the few days before and after the thresholdreaching time, we are able to minimize the influence of various time-dependent factors and assess the significance of prosocial motivation and economic concerns in a more robust way. The higher level of backer support in the two days before the interval during which the threshold is reached than in the two days afterward suggests that the positive effect of the prosocial motivation outweighs the negative effect of project uncertainty and quality concerns. Our sub-group analyses show that this effect is more salient for publicgood projects than for private-good projects, which is consistent with our expectation that public goods are more likely to induce one’s prosocial motivation than private goods [4, 21, 37, 50] and lends validity to the argument that the strong prosocial motivation before reaching the goal is the likely explanation for the observed difference in backer support between the before and after threshold period.

## Literature Review

This study is first related to the growing literature on factors that affect individuals’ funding decisions on crowdfunding platforms. Previous studies have shown that geographic distance [2, 13, 39], social capital [2, 33, 38, 40], cultural differences [13], and founder race [46, 55] can have a significant impact on funders’ decisions. Another subset of papers examines the role of prior funders’ behaviors on the funding decisions of later ones. In a donation-based crowdfunding context, Burtch et al. [12] find that more initial contributions reduce later contributors’ incentive to provide additional funds. On the contrary, funders are found to engage in herding behavior on lending-based and rewardbased crowdfunding platforms [32, 34, 51, 56]. In this study, we investigate the effect of different threshold-reaching stages on backers’ decisions to pledge projects and share the project information within their social networks.

Second, our work is closely related to previous studies on funder motivations in various types of crowdfunding. In donation-based crowdfunding, donors contribute their money to help others mainly because of prosocial motivation, such as pure altruism, warm glow, and image enhancement (e.g., Bekkers and Wiepking [8], Gleasure and Feller [27], and Liu et al. [41]). In lending-based crowdfunding, lenders are primarily motivated by the potential financial returns and act as rational economic agents [20, 32]. In reward-based crowdfunding, backers can be driven by both prosocial and economic motivations. Previous studies have uncovered several key motives of backers to pledge their money, such as collect rewards, help others, be part of a community, and gain recognition [10, 11, 16, 23]. However, the evidence on the relative significance of different motivations is based on selfreported survey data and shows inconsistent findings. For example, several studies report that prosocial motivation plays an important role in driving backer behaviors [10, 11]. In contrast, Cholakova and Clarysse [16] find that nonfinancial motives have no significant effect. Fortunately, under the all-or-nothing mechanism employed by most reward-based crowdfunding platforms, the timing of backers’ contributions may signal their motivations. For example, Ryu et al. [47] find that reward motivation is associated with late funding, whereas prosocial motivation is associated with early funding. We aim to provide empirical evidence on the importance of prosocial and economic motivations by investigating backers’ pledging and sharing behaviors at different project fundraising stages.

Finally, our research relates to the stream of literature on threshold/goal effects on user behaviors in online platforms. Previous studies have shown that the presence of a threshold on crowdfunding platforms can bring benefits such as reducing the free-riding problem [1] and alleviating herd behavior [14]. Different from their focus on the informational role of the threshold, we investigate backers’ dynamic behaviors at different stages of achieving the funding threshold to gain a better understanding of backer motivations. In the group-buying context, Wu et al. [52] find that there is a dramatic increase in the number of new sign-ups around the time when the deal threshold is reached. The goal-gradient behavior has also been reported in blood and charitable donations [5, 17]. The setting of reward-based crowdfunding is unique in two aspects: first, prosocial and economic motivations can both drive backer decisions; second, the composition of prosocial and economic motivations is likely to vary with the prosociality of the projects. An objective of our study is to examine and quantify the role of goal proximity on backers’ prosocial motivation for public-good and private-good projects in reward-based crowdfunding.

## Hypotheses Development

In this section, we develop hypotheses on backers’ dynamic pledging and sharing behaviors across different stages of achieving the funding threshold.

## Pledging and Sharing Around the Threshold

Backers who pledge their money when the project approaches its threshold act as tipping points [26] whose contribution will tip the project outcome into success. This goal proximity is likely to induce a high level of effort among individuals, which has been observed in a variety of settings. For example, Anik and Norton [5] show that being the tipping points increases the likelihood of participants getting a blood test. Cryder et al. [17] reveal that people are more likely to contribute as charitable campaigns approach their funding goals. In the online group-buying context, Wu et al. [52] find that there is a surge of new sign-ups when approaching deal thresholds.

The close proximity to the goal can greatly strengthen backers’ prosocial motivation because the perceived impact of their contributions is remarkably high. Both the project creator and the existing backers who have already made their pledges can benefit if the project becomes successful. The threshold-induced social responsibility and psychological value (e.g., a sense of achievement, a high level of satisfaction) are likely to attract more backers to pledge their money, leading to a sudden increase in the number of backers. The word-of-mouth referrals may be also accelerated during this critical period because of similar underlying causes. Therefore, we hypothesize the following:

Hypothesis 1: There is a dramatic increase in the number of backers and shares when the project approaches its funding threshold.

## Pledging and Sharing Before Versus After the Threshold

Before the threshold is reached, the desire to help others and support causes plays an important role in backers’ decision making. Backers contribute their money because they want to see the creative ideas being implemented in real life. By doing so, they not only help creators realize their objectives but also help similarlyminded backers receive their rewards [10, 23]. Backers can reap a number of psychological (e.g., feeling good about themselves) and social benefits (e.g., gaining recognition among community members) from supporting projects in need of funding [11]. Besides pledging their money, they may help projects by spreading word of mouth through social networks (e.g., sharing the project information on Facebook or Twitter) to encourage their friends to contribute.

Besides the prosocial motivation, the economic motivation to collect rewards may also drive backers’ funding behavior [11, 16, 23]. However, at this stage, backers face uncertainty about project outcome. If the amount of money raised cannot meet the fundraising goal, the project will fail and backers will not be able to receive any rewards. Although the pledged money will be returned later, backers incur search and opportunity cost, and suffer psychological loss from not receiving the rewards [25]. Furthermore, previous studies have shown that backers may exhibit herd behavior in the crowdfunding market [11, 51]. The fact that the project has not yet met the goal may reduce its perceived quality and discourage backers from providing support.

After the threshold is reached, backers are certain about the success of the project. At this stage, backers’ funding behavior is more like the pre-ordering in advance selling. Backers who pledge their money will not incur any opportunity cost or suffer a psychological loss from not being able to receive the rewards. The reduction in project uncertainty and risk is likely to strengthen their economic motivation to collect rewards [47]. Furthermore, to reduce search and evaluation cost, backers may take being able to reach the funding goal as a sign of high project quality and be more willing to pledge their money once the project passes its threshold [11]. Backers might also be more motivated to share the project information with their friends because they believe the rewards are worth the pledge and want their friends to enjoy the benefits as well. Since the uncertainty is eliminated, the word-of-mouth referrals are highly similar to the recommendation behaviors in typical online retailing settings. When sharing the project information, backers do not need to worry about the opportunity cost and disappointment that their friends might experience due to the project failure caused by insufficient funds.

However, after the project reaches its funding threshold, the perceived impact of one’s contribution is substantially lower because the project will be implemented regardless of whether the backer pledges his/her money. As a result, the prosocial motivation arising from empathy and a sense of achievement is significantly reduced. The image motivation to behave prosocially is also much weaker as others will interpret one’s pledging behavior as pre-ordering instead of helping.

The aforementioned opposing arguments precluded us from making conclusive determinations on the relative magnitude of the number of backers and Facebook shares before and after the threshold was reached. Therefore, we propose the following two competing hypotheses:

Hypothesis 2a: Backers are more likely to pledge and share before the threshold is reached than afterward.

Hypothesis 2b: Backers are less likely to pledge and share before the threshold is reached than afterward.

## Moderating Role of Project Prosociality

Public goods differ from private goods in that they are non-excludable in supply (i.e., everyone can enjoy the benefit from consuming them once they are made available) and non-rival in demand (i.e., one person’s consumption does not reduce the utility of other users) [48]. Examples of public goods include public parks, scientific knowledge, and user-generated content. In the crowdfunding context, projects that aim to produce something that can benefit society as a whole, such as arts, publishing, and music, are likely to be perceived as public goods. The production of such public goods is likely to induce a high level of intrinsic and image motivation of individuals [4, 6, 19, 21, 50]. Under such circumstances, backers care less about the project uncertainty and are likely to pledge at an earlier time. Furthermore, backers are motivated to share the project information with their online friends in order to help the creator raise more funds and enhance their own social image [9, 30]. The positive effect of goal proximity is likely to be particularly strong for public-good projects because backers feel a greater social responsibility to turn these projects from failure to success and can derive a higher level of perceived impact from their contributions [5, 17].

By contrast, private goods are provided or manufactured by entrepreneurs who aim to earn profits. One main motive of backers is to receive and use the products promised by project creators. Examples of private-good projects in crowdfunding include camera equipment, gadgets, and video games. The pledging behavior of backers is similar to the pre-ordering behavior of consumers in advance selling except for the uncertainty about the project success. The intrinsic and image motivations of backers for private-good projects are not as strong as those for public-good projects [21, 37]. The strengthened economic motivation and weakened prosocial motivation may induce backers to postpone their decisions until receiving a credible signal of high product quality. When it comes to Facebook shares, although backers may want to help private-good projects succeed by sharing information with their friends, the concern about project quality and uncertainty may hinder their sharing behavior. Furthermore, despite the fact that backers still attain a high level of excitement from beating the threshold of private-good projects, the social responsibility and perceived impact of helping these projects succeed are not as significant as those of helping public-good projects. The different nature of private-good and public-good projects leads us to the following hypotheses:

Hypothesis 3: Compared to private-good projects, public-good projects are more likely to experience a dramatic increase in backer support in pledging and sharing around the threshold-reaching time.

Hypothesis 4: Compared to private-good projects, public-good projects are more likely to attract a higher level of backer support in pledging and sharing before the threshold is reached than afterward.

## Context and Data

## Context

Our empirical setting is a leading reward-based crowdfunding platform, Kickstarter. On Kickstarter, creators can post various types of projects with a clear description of project details, expected rewards, funding goal, and funding period. Backers who are interested can pledge their money to help creators implement their ideas and to receive the promised rewards in the future. Kickstarter adopts the all-or-nothing fundraising scheme, in which creators cannot receive any money unless the pledged amount surpasses the predetermined goal. If the project is successfully funded, a 5% Kickstarter fee and 3-5% payment processing fees will be charged. Kickstarter also enables social media features that allow users to share the project information on social media sites like Facebook or Twitter. Figure 1 shows a snapshot of the homepage of a project on Kickstarter.

![](/api/attachments/QEVYWFUC/fulltext/images/29ddab0d82425206a54f8d8bc53b49c5c5b4e1f5bd88f68e044312f4ccb1980b.jpg)  
Figure 1. Homepage of a Project on Kickstarter

## Data

We built a data crawler written in Java to extract project information on Kickstarter every two hours from October 7, 2015 to December 15, 2015, for a total of 70 days.<sup>7</sup> In each crawl, we collected a comprehensive list of characteristics for each project, including number of backers, pledge amount, number of Facebook shares, goal amount, whether it is a featured project, number of updates, number of comments, number of projects the creator has backed or created before, and whether the creator discloses his/her personal Facebook account. We also recorded the positions of each project under the popularity and magic ranking mechanisms of Kickstarter.

As our objective is to study the threshold-induced effects, we focus on projects that successfully reached their funding goals before the deadline. To allow for sufficient observations in both before-threshold and after-threshold period, we exclude those projects that reached their goals in either the first three days or the last three days of their fundraising periods. We also remove projects whose goal amount was less than \$1,000 or whose final number of backers was fewer than 10 to reduce the influence of small projects. Our final data consists of 1,058 projects. Tables 1 and 2 present the descriptions and summary statistics for the time-invariant and time-varying variables in our study. Table A1 in the Appendix reports the correlation matrix.

## Empirical Analyses

One challenge encountered in this study is that the diffusion rate of projects varies with time. Previous studies [36, 45] have shown that the typical pattern of project support on Kickstarter is U-shaped; that is, backers are more likely to contribute to a project at the beginning and at the end of the fundraising period, whereas the pledge in the middle period is relatively stable. This is mainly due to the high visibility and exposure given to projects when they are newly launched or close to deadline. To abstract from this U-shaped diffusion pattern and minimize the influence of other possible confounding factors, we narrow our scope to a short time window which is not far away from the time when the project threshold is reached. In particular, we use the subset of data that consists of project observations in the focal period of the 48 hours before, the two hours during, and the 48 hours after the threshold-reaching time interval. The approximately four-day time window is long enough for us to detect the differences in pledging and sharing levels before and after the project threshold is reached and yet short enough relative to the average 30-day funding cycle that it is unlikely that the differences can be attributed to simple project diffusion or changes in other relevant variables.

Table 1. Variable Descriptions

<table><tr><td>Variable</td><td>Description</td></tr><tr><td colspan="2">Time-Invariant Variables:</td></tr><tr><td>Goal</td><td>The minimum amount of money required to make the project successful</td></tr><tr><td>Has_video</td><td>Whether the description of the project contains a video</td></tr><tr><td>Create_num</td><td>The number of projects that the creator has created before the launch of the project</td></tr><tr><td>Back_num</td><td>The number of projects that the creator has backed before the launch of the project</td></tr><tr><td>Fb_connected</td><td>Whether the project creator is connected to his/her Facebook account</td></tr><tr><td colspan="2">Time-Varying Variables:</td></tr><tr><td>Backers_incre</td><td>The incremental number of backers pledging to the project at a time interval</td></tr><tr><td>Fb_shares_incre</td><td>The incremental number of Facebook shares for the project at a time interval</td></tr><tr><td>Pledge_incre</td><td>The incremental amount of money pledged to the project at a time interval</td></tr><tr><td>Updates_incre</td><td>The incremental number of updates posted by the project creator at a time interval</td></tr><tr><td>Comments_incre</td><td>The incremental number of comments left by backers of the project at a time interval</td></tr><tr><td>Featured</td><td>Whether the project is featured at a time interval</td></tr><tr><td>Popular_rank</td><td>The position of the project under the Kickstarter&#x27;s Popularity ranking mechanism</td></tr><tr><td>Magic_rank</td><td>The position of the project under the Kickstarter&#x27;s Magic ranking mechanism</td></tr></table>

## Model-Free Evidence

Given that the main purpose is to examine the effects of different thresholdreaching stages on backers’ pledging and sharing behaviors, as a first step, we plot the average log incremental number of backers and Facebook shares for all projects in the 48 hours before, the two hours during, and the 48 hours after the threshold is reached in Figure 2. The figure shows two interesting facts. First, the incremental number of backers and Facebook shares reach a peak during the twohour interval when the threshold is reached. Second, both numbers are higher in the two days before the interval during which the threshold is reached than in the two days afterward. In addition, the support level in the two days before (after) the threshold-reaching time interval is relatively stable, indicating that time-varying project diffusion rate is not a concern in our chosen focal period.

These results give us some preliminary evidence that being close to reaching the threshold can strongly boost backers’ prosocial motivation to pledge and share, supporting Hypothesis 1. Furthermore, the positive effect of the prosocial motivation outweighs the negative effect of project uncertainty and quality concerns,

Table 2. Summary Statistics

<table><tr><td>Variable</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td><td>N</td></tr><tr><td colspan="6">Time-Invariant Variables:</td></tr><tr><td>Goal</td><td>14,341.470</td><td>25,468.980</td><td>1,000</td><td>349,750</td><td>1,058</td></tr><tr><td>Has_video</td><td>0.882</td><td>0.323</td><td>0</td><td>1</td><td>1,058</td></tr><tr><td>Create_num</td><td>1.622</td><td>2.205</td><td>1</td><td>36</td><td>1,058</td></tr><tr><td>Back_num</td><td>7.409</td><td>34.867</td><td>0</td><td>867</td><td>1,058</td></tr><tr><td>Fb_connected</td><td>0.513</td><td>0.500</td><td>0</td><td>1</td><td>1,058</td></tr><tr><td colspan="6">Time-Varying Variables:</td></tr><tr><td>Backers_incre</td><td>0.712</td><td>2.453</td><td> $0^a$ </td><td>161</td><td>360,073</td></tr><tr><td>Fb_shares_incre</td><td>2.609</td><td>17.339</td><td> $0^a$ </td><td>1,400</td><td>360,073</td></tr><tr><td>Pledge_incre</td><td>67.306</td><td>364.766</td><td> $0^a$ </td><td>37,539.090</td><td>360,073</td></tr><tr><td>Updates_incre</td><td>0.014</td><td>0.121</td><td>0</td><td>5</td><td>360,073</td></tr><tr><td>Comments_incre</td><td>0.072</td><td>0.627</td><td>0</td><td>118</td><td>360,073</td></tr><tr><td>Featured</td><td>0.005</td><td>0.073</td><td>0</td><td>1</td><td>360,073</td></tr><tr><td>Popular_rank</td><td>132.551</td><td>109.393</td><td>1</td><td>806</td><td>360,073</td></tr><tr><td>Magic_rank</td><td>216.903</td><td>170.700</td><td>1</td><td>887</td><td>360,073</td></tr></table>

Notes: <sup>a</sup>Since backers can cancel their pledges and Facebook shares, or change their pledge amount at any time, backer\_incre, Fb\_share\_incre values, and pledge\_incre are negative at a very small number of time intervals (<1%). Given that negative binomial model can only handle nonnegative values, we replace all negative values by zero in our analyses.

lending support to Hypothesis 2a. However, this preliminary analysis does not take into consideration the various factors that might affect backers’ decisions, such as project heterogeneity and time effects. Next, we employ more rigorous empirical models to test the effects.

## Main Model

Given that our dependent variables (i.e., the incremental number of backers and Facebook shares) are non-negative count variables with a skewed distribution, we apply a fixed-effects negative binomial model<sup>8</sup> [3] with robust standard errors on project observations in the focal period using the following specification:

$$
\begin{array}{l} \log \left(\mu_ {i t}\right) = \beta_ {0} + \beta_ {1} I _ {i t} ^ {\text { thre }} + \beta_ {2} I _ {i t} ^ {a f t} + \beta_ {3} \log \left(\text { updates\_increase } _ {i t}\right) + \beta_ {4} \log \left(\text { comments\_increase } _ {i t}\right) \\ + \beta_ {5} \text { featured } _ {i t} + \beta_ {6} \log \left(\text { popular\_rank } _ {i t}\right) + \beta_ {7} \log \left(\text { magic\_rank } _ {i t}\right) + \psi_ {t} + \tau_ {t} + \mu_ {i} + \varepsilon_ {i t}, \end{array} \tag {1}
$$

$$
\operatorname * {P r} (y _ {i t} = \mathrm{k}) = \frac {\Gamma (k + \alpha^ {- 1})}{\Gamma (k + 1) \Gamma (\alpha^ {- 1})} \left(\frac {1}{1 + \alpha \mu_ {i t}}\right) ^ {\alpha^ {- 1}} \left(\frac {\alpha \mu_ {i t}}{1 + \alpha \mu_ {i t}}\right) ^ {k},
$$

where $y _ { i t }$ is the incremental number of backers or Facebook shares of project during the interval at time $t , \Gamma ( \cdot )$ represents gamma function, $\mu _ { i t }$ is the mean of $y _ { i t } .$

![](/api/attachments/QEVYWFUC/fulltext/images/f88600491636d59971091421d71aa7409d17d57772a02947e99df97a695e94b7.jpg)

![](/api/attachments/QEVYWFUC/fulltext/images/376906ab10dcbaf3fc4c396c51b26cf2703469a0f94f3165cd803835410f63d0.jpg)  
Figure 2. Average Bi-hourly Log Incremental Number of Backers and Facebook Shares Notes: The x-axis refers to time intervals in the 48 hours before, the two hours during, and the 48 hours after the interval when the threshold is reached. 0 refers to the time interval during which the threshold is reached, -1 refers to the last interval before the threshold is reached, and 1 refers to the first interval after the threshold is reached.

and α is the overdispersion parameter. The $I _ { i t } ^ { t h r e }$ is an indicator for the time interval during which the threshold is reached,<sup>9</sup> and $I _ { i t } ^ { a f t }$ is an indicator for the 24 time intervals after the interval during which the threshold is reached. The remaining 24 time intervals before the threshold-reaching interval are used as the baseline for comparison. The coefficients of these two indicator variables capture the two types of threshold-induced effects in which we are interested. In addition, we add other time-varying project variables, including the log of the incremental number of updates and comments, whether it is a featured project, and the log of the project ranks under the popularity and magic ranking mechanism. To control for the unobserved project heterogeneity and time effects, we include both a projectspecific fixed effect and a time-specific fixed effects: $\psi _ { t }$ measures the time-of-theday fixed effect, $\tau _ { t }$ measures the day-of-the-week fixed effect, and $\mu _ { i }$ measures the time-invariant project fixed effect.

The results from the main model are shown in Table 3. Columns 1 and 2 report the results for the incremental number of backers and the incremental number of Facebook shares, respectively. First, the coefficients of Around\_threshold are positive and statistically significant for both dependent variables. On average, there are 204.96% <sup>10</sup> more backers and 58.25% more Facebook shares during the two-hour interval when the threshold is reached, compared to other intervals in the two days before. This surge around the threshold lends support to Hypothesis 1, confirming the positive effect of goal proximity on backers’ prosocial motivation on Kickstarter. Second, the coefficients of After\_threshold are negative and significant. The fact that the threshold has not been met is associated with 50.23% more backers and 41.62% more Facebook shares per two-hour interval, which is consistent with our Hypothesis 2a and indicates that the positive effect of prosocial motivation triumphs over the negative effect of project uncertainty and quality concerns.

In addition, we find that the numbers of updates and comments are positively correlated with backer support, which is consistent with previous studies (e.g., Molllick [43] and Xu et al. [54]). Our results also indicate that being ranked in a better position under the popularity sorting mechanism is more likely to generate a higher number of backers and Facebook shares, coinciding with our belief that highly ranked items based on quality indicators (e.g., popularity, relevance) are more attractive to potential users [24]. On the contrary, project position under the magic ranking mechanism seems to have little effect on backers’ decisions to pledge and share, which may be due to backers’ lack of information on how the magic mechanism works. We do not find any significant influence of being featured by Kickstarter on backers’ contribution and referral behaviors. One possible reason for this is that backers might have low trust in the endorsement of the platform.

Furthermore, our results show that backers are more likely to pledge from Monday to Friday and between 8am and 6pm PDT (see Figures 3 and 4), indicating that potential backers tend to look for projects to pledge during their work time.<sup>11</sup> We suspect that this is because people like to visit Kickstarter when browsing the Internet (e.g., checking personal emails, reading news reports) during short breaks at work. This is in striking contrast to the bidding and purchase patterns of consumers in online auction and shopping [42, 49]. The day-of-the-week and time-of-the-day effects on the incremental number of Facebook shares are qualitatively similar and reported in Figures A1 and A2 in the Appendix. The distinct patterns observed on this crowdfunding platform have direct implications for project creators who are seeking ways to increase their funding amount and word-of-mouth referrals.

## Moderating Effect of Project Prosociality

The projects we collect fall into seven categories: Arts, Design, Film, Games, Music, Publishing, and Technology. The distribution of projects across categories is shown in Table 4. As discussed in the hypotheses development section, the threshold effects may vary across different project categories. Public-good project categories are more likely to induce stronger prosocial motivation (e.g., warm glow, image enhancement) whereas private-good project categories may induce a higher level of economic motivation (i.e., collecting rewards). Following Hong et al. [33], we categorize projects in Games and Technology into private goods, and Arts, Design, Film, Music, and Publishing into public goods. This classification is based on the idea that people tend to pre-order video games and technology products and perceive original work such as arts and film as something that can benefit society as a whole.

Table 3. Regression Results under Main Model

<table><tr><td></td><td>(1)DV: Incre_Backers</td><td>(2)DV: Incre_Fb_Shares</td><td>(3)DV: Incre_Backers</td><td>(4)DV: Incre_Fb_Shares</td></tr><tr><td>Around_threshold</td><td>1.115***(0.035)</td><td>0.459***(0.051)</td><td>0.888***(0.071)</td><td>0.402***(0.110)</td></tr><tr><td>After_threshold</td><td>-0.407***(0.014)</td><td>-0.348***(0.017)</td><td>-0.275***(0.025)</td><td>-0.179***(0.035)</td></tr><tr><td>Around_threshold × public</td><td></td><td></td><td>0.289***(0.080)</td><td>0.067(0.122)</td></tr><tr><td>After_threshold × public</td><td></td><td></td><td>-0.201***(0.030)</td><td>-0.224***(0.040)</td></tr><tr><td>Log(Updates_incre)</td><td>0.413***(0.058)</td><td>0.762***(0.072)</td><td>0.416***(0.058)</td><td>0.768***(0.072)</td></tr><tr><td>Log(Comments_incre)</td><td>0.216***(0.026)</td><td>0.281***(0.038)</td><td>0.221***(0.026)</td><td>0.281***(0.037)</td></tr><tr><td>Featured</td><td>-0.129(0.082)</td><td>-0.093(0.101)</td><td>-0.121(0.083)</td><td>-0.079(0.101)</td></tr><tr><td>Log(Popular_rank)</td><td>-0.901***(0.029)</td><td>-0.698***(0.031)</td><td>-0.918***(0.029)</td><td>-0.712***(0.031)</td></tr><tr><td>Log(Magic_rank)</td><td>0.012(0.012)</td><td>0.042***(0.014)</td><td>0.010(0.012)</td><td>0.040***(0.014)</td></tr><tr><td>Time-of-day FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Day-of-week FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Project FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of Observations</td><td>51,842</td><td>51,842</td><td>51,842</td><td>51,842</td></tr><tr><td>No. of Projects</td><td>1,058</td><td>1,058</td><td>1,058</td><td>1,058</td></tr><tr><td>Log Likelihood</td><td>-45,020.459</td><td>-68,607.159</td><td>-44,986.164</td><td>-68,590.121</td></tr><tr><td colspan="5">Notes: Robust standard errors in parentheses; * significant at 10% level; ** significant at 5% level; *** significant at 1% level.</td></tr></table>

![](/api/attachments/QEVYWFUC/fulltext/images/eb702b020ba6b3ee5ff48bf25755e046d55b89e763d9a88b98a6acafcea326d3.jpg)  
Figure 3. Day-of-the-Week Effects on Incremental Number of Backers Notes: Sunday serves as the reference group and is not shown here.

![](/api/attachments/QEVYWFUC/fulltext/images/c4a648d507cc8df6df5866926beca13afb2d3bcba2f17fba43460aae89b294e3.jpg)  
Figure 4. Time-of-the-Day Effects on Incremental Number of Backers Notes: 0–2 serves as the reference group and is not shown here.

To capture the moderating effect of project prosociality, we construct a variable Public indicating whether the project is a public-good project or not, and interact the Public variable with $I _ { i t } ^ { t h r e }$ and $I _ { i t } ^ { a f t }$ respectively. The new negative binomial model specification is:

Table 4. Distribution of Projects Across Categories

<table><tr><td>Category</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Arts</td><td>91</td><td>8.60</td></tr><tr><td>Design</td><td>195</td><td>18.43</td></tr><tr><td>Film</td><td>147</td><td>13.89</td></tr><tr><td>Games</td><td>121</td><td>11.44</td></tr><tr><td>Music</td><td>219</td><td>20.70</td></tr><tr><td>Publishing</td><td>153</td><td>14.46</td></tr><tr><td>Technology</td><td>132</td><td>12.48</td></tr></table>

$$
\begin{array}{l} \log (\mu_ {i t}) = \beta_ {0} + \beta_ {1} I _ {i t} ^ {\text { thre }} + \beta_ {2} I _ {i t} ^ {\text { aft }} + \beta_ {3} I _ {i t} ^ {\text { thre }} \times \text { public } _ {i} + \beta_ {4} I _ {i t} ^ {\text { aft }} \times \text { public } _ {i} \\ + \beta_ {5} \log (\text { updates\_increase } _ {i t}) + \beta_ {6} \log (\text { comments\_increase } _ {i t}) + \beta_ {7} \text { featured } _ {i t} \\ + \beta_ {8} \log (\text { popular\_rank } _ {i t}) + \beta_ {9} \log (\text { magic\_rank } _ {i t}) + \psi_ {t} + \tau_ {t} + \mu_ {i} + \varepsilon_ {i t}, \\ \operatorname * {P r} (y _ {i t} = k) = \frac {\Gamma (k + \alpha^ {- 1})}{\Gamma (k + 1) \Gamma (\alpha^ {- 1})} \left(\frac {1}{1 + \alpha \mu_ {i t}}\right) ^ {\alpha^ {- 1}} \left(\frac {\alpha \mu_ {i t}}{1 + \alpha \mu_ {i t}}\right) ^ {k} \end{array}\tag{2}
$$

With this specification, the coefficients of the two interaction terms are our coefficients of interest. $\beta _ { 3 }$ captures the relative difference in the dramatic increase in backer support around the threshold-reaching time between publicgood projects and private-good projects, and $\beta _ { 4 }$ measures the relative difference in the before- and after-threshold changes in backer support between publicgood projects and private-good projects.

The results for the incremental number of backers and the incremental number of Facebook shares are shown in Columns 3 and 4 of Table 3, respectively. The coefficients of $I _ { i t } ^ { t h r e } \times p u b l i c _ { i }$ is positive and statistically <sup>it</sup>significant for the incremental number of backers. Specifically, compared to private-good projects, public-good projects receive 33.51% more backers during the two-hour interval when the threshold is reached relative to the two days before. The same coefficient for the incremental number of Facebook shares is positive although not significant. The coefficients of $I _ { i t } ^ { a f t } \times p u b l i c _ { i }$ are significantly negative for both dependent variables. Compared to private-good projects, public-good projects attract 22.26% more backers and 25.11% more Facebook shares in the two days before the thresholds is reached than in the two days afterward. These results show that both types of threshold effects are more pronounced for public-good projects, supporting our Hypothesis 3 and Hypothesis 4. Clearly, both the direct effect of prosocial motivation and the moderating effect of goal proximity are stronger for public-good projects than for private-good projects.

## Alternative Explanations

Our analysis shows that there are two types of threshold-induced effects: a sudden increase in backer support around the threshold-reaching time and a higher level of backer support before the threshold is reached than afterward. Both effects are more salient in public-good project categories than in private-good project categories. We attribute our findings to backers’ strong prosocial motivation in reward-based crowdfunding, which is particularly heightened when the project approaches its funding threshold. We now consider two alternative explanations that could give rise to our findings.

## Creators’ Marketing Efforts

One possible explanation of our results is that project creators may undertake more marketing efforts (e.g., publish more posts/messages on Facebook/Twitter) before and especially around the time when the thresholds are reached. If this is true, the behavioral changes in pledges and Facebook shares may simply be a response to creators’ marketing activities rather than reflecting a change in backers’ motivation. To test this explanation, we hired a few student helpers to find the Facebook page and Twitter account of each project (if they exist). For all identified Facebook pages and Twitter accounts, we crawled the timestamps and content of posts/messages sent within the project lifetime. Then, we construct two variables:   , which represents whether there is any post published on the Facebook page of project  at time ; and   , which represents whether there is any message posted on the Twitter account of project at time . We add these two control variables to Equation (2) and re-estimate the model.

The results obtained are shown in Table 5, which are qualitatively and quantitatively similar to the previously reported findings. The coefficients of and are both positive, indicating that creators’ marketing efforts on Facebook and Twitter indeed have a positive effect on backers’ pledging and sharing behavior. Despite this, our main coefficients of interest are still positive and of similar magnitudes as before, suggesting that the marketing efforts cannot explain the two types of thresholdinduced effects observed in our study. We include these two variables in all the subsequent analyses to control for the effects of creators’ marketing efforts.

## Creators’ Own Contributions

Another concern of the results is that a considerable proportion of backer support before or around the threshold-reaching time may come from creators themselves. However, this is apparently a costly action because, even if the project is successfully funded, the creator needs to pay 8-10% in fees. Therefore, project creators are not likely to pledge especially when the project is far enough from the deadline. Following this rationale, we exclude those projects that reached their thresholds in the last week of their funding periods and redo our analysis. When there is sufficient time before the deadline, creators are not likely to contribute because making pledges would impose a nontrivial cost on them. Second, this kind of self-contribution is less likely to happen in projects with larger goal amounts due to the higher cost. Therefore, we also exclude projects whose goal amounts are less than \$5,000.

Table 5. Regression Results After Controlling for Creators’ Marketing Efforts

<table><tr><td></td><td>(1)DV: Incre_Backers</td><td>(2)DV: Incre_Fb_Shares</td><td>(3)DV: Incre_Backers</td><td>(4)DV: Incre_Fb_Shares</td></tr><tr><td>Around_threshold</td><td>1.101***(0.035)</td><td>0.445***(0.051)</td><td>0.864***(0.070)</td><td>0.371***(0.108)</td></tr><tr><td>After_threshold</td><td>-0.404***(0.014)</td><td>-0.345***(0.017)</td><td>-0.271***(0.025)</td><td>-0.174***(0.035)</td></tr><tr><td>Around_threshold × public</td><td></td><td></td><td>0.303***(0.080)</td><td>0.087(0.121)</td></tr><tr><td>After_threshold × public</td><td></td><td></td><td>-0.203***(0.030)</td><td>-0.228***(0.040)</td></tr><tr><td>Log(Updates_incre)</td><td>0.370***(0.059)</td><td>0.721***(0.073)</td><td>0.373***(0.058)</td><td>0.727***(0.073)</td></tr><tr><td>Log(Comments_incre)</td><td>0.210***(0.026)</td><td>0.268***(0.037)</td><td>0.215***(0.026)</td><td>0.269***(0.037)</td></tr><tr><td>Featured</td><td>-0.125(0.082)</td><td>-0.086(0.101)</td><td>-0.116(0.083)</td><td>-0.072(0.102)</td></tr><tr><td>Log(Popular_rank)</td><td>-0.905***(0.029)</td><td>-0.703***(0.030)</td><td>-0.922***(0.029)</td><td>-0.717***(0.031)</td></tr><tr><td>Log(Magic_rank)</td><td>0.013(0.012)</td><td>0.043***(0.014)</td><td>0.011(0.012)</td><td>0.041***(0.014)</td></tr><tr><td>Has_fb_post</td><td>0.155***(0.035)</td><td>0.212***(0.043)</td><td>0.156***(0.034)</td><td>0.214***(0.043)</td></tr><tr><td>Has_twi_msg</td><td>0.229***(0.031)</td><td>0.243***(0.039)</td><td>0.233***(0.031)</td><td>0.245***(0.039)</td></tr><tr><td>Time-of-day FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Day-of-week FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Project FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of Observations</td><td>51,842</td><td>51,842</td><td>51,842</td><td>51,842</td></tr><tr><td>No. of Projects</td><td>1,058</td><td>1,058</td><td>1,058</td><td>1,058</td></tr><tr><td>Log Likelihood</td><td>-44,968.06</td><td>-68,563.528</td><td>-44,932.198</td><td>-68,545.728</td></tr><tr><td colspan="5">Notes: Robust standard errors in parentheses; * significant at 10% level; ** significant at 5% level; *** significant at 1% level.</td></tr></table>

We rerun our model using the subsample obtained and present the results in Table 6. It is clear that our findings are robust to the exclusion of projects with late threshold-reaching time and projects with small goal amounts, suggesting that the two types of thresholdinduced effects are unlikely to be driven by creators’ own contributions to their projects.

## Robustness Checks

To further validate our findings, we conduct a set of additional tests. First, in the previous analysis, interaction terms are used to examine the moderating role of project prosociality. To see whether our results are sensitive to the use of alternative method, we perform a subgroup analysis for public-good projects and private-good projects separately. The results in Table A2 of the Appendix show that the magnitudes of the two coefficients of interest are substantially larger for public-good projects than for private-good projects, which further confirms our Hypothesis 3 and Hypothesis 4.

Second, the time window in the main model is 48 hours before and 48 hours after the threshold-reaching time interval. To assess whether our results are robust to alternative length of time window, we change the time window from 48 hours before/after the threshold-reaching interval to 24 hours and 72 hours, respectively. The results shown in Tables A3 and A4 of the Appendix are qualitatively similar to our main results.

Third, we adopt the default bi-hourly time interval in the main analyses. To test the reliability of the results to the use of a wider interval, we aggregate two bihourly intervals into one and redo the analyses. Under the four-hour time interval, the threshold-reaching interval consists of the bi-hourly interval during which the threshold is reached and the bi-hourly interval right before that. The 12 four-hour time intervals before (after) are used as the before (after) period. The results shown in Table A5 of the Appendix are consistent with our findings obtained using bihourly time interval.

Fourth, the Poisson model is another commonly used model for count variables. Although the negative binomial model provides a better fit to our data, we explore the robustness of our findings to the use of a fixed-effects Poisson model. The results, as reported in Table A6 of the Appendix, show that our findings are quite robust.

Lastly, we examine whether our results still hold when we use the incremental pledge amount as the dependent variable. The results are shown in Table A7 of the Appendix. All the effects are still present, and the magnitudes of the coefficients are even larger. The results indicate that the two types of threshold effects are not only reflected in the likelihood to pledge and share, but also in the amount of money pledged.

## Discussion

## Key Findings

Our study examines the effects of threshold-reaching stages on backers’ pledging and sharing behaviors in reward-based crowdfunding. We find that there is a surge in backer support in the few hours when the project reaches its threshold. This is likely to be due to backers’ heightened prosocial motivation arising from close proximity to the goal. In addition, backer support is higher before the threshold is reached than afterward, providing empirical evidence that the prosocial motivation outweighs the uncertainty reduction and herding motivation in driving backers’ pledging and sharing decisions. We further show that both types of threshold effects are more pronounced in public-good project categories, which is consistent with the theory that public-good projects are more likely to induce backers’ prosocial motivation.

## Theoretical Implications

This study first advances our understanding of goal-gradient behavior, which has been well documented in the literature. The majority of studies have examined how and why individuals increase their efforts as they approach their personal goals such as receiving a reward in loyalty program programs [35, 57] and achieving a badge/ rank in knowledge contributions [28, 44]. Recently, there are a few studies in contexts where goals are pursued collectively, such as blood donation [5], charitable giving [17], and group-buying [52]. Our finding in reward-based crowdfunding provides an additional piece of evidence on the heightened motivation of individuals as they approach a collective goal in a context where both prosocial and economic motivations coexist. We also show that the surge in backer support is only evident when projects are very close to reaching their funding goals,<sup>12</sup> whereas the support level before that is relatively stable.

Second, our work extends previous economics and information systems research on what motivates people to participate in crowdfunding. While donation-based crowdfunding is likely to induce one’s prosocial motivation [8, 27, 41] and lendingbased crowdfunding is more likely to stimulate one’s financial incentive [20, 32], backers’ motivation in reward-based crowdfunding is more complicated and deserves further attention. Previous survey research on the motivation of backers has reported mixed findings on the importance of prosocial motivation and economic motivation in driving backers’ pledging behavior [10, 11, 16]. Furthermore, the results based on self-reports may be distorted by respondents’ tendency to provide socially desirable answers. The implementation of all-or-nothing scheme offers a unique opportunity for us to empirically test the significance of backers’ motivations by examining the timing of their contributions. Our results support the existence of a strong prosocial motivation among backers, which triumphs over backers’ aversion to project uncertainty in quality and outcome.

Table 6. Regression Results after Excluding Projects that Reach Thresholds Late and Projects with Small Goal Amounts

<table><tr><td></td><td>(1)DV: Incre_Backers</td><td>(2)DV: Incre_Fb_Shares</td><td>(3)DV: Incre_Backers</td><td>(4)DV: Incre_Fb_Shares</td></tr><tr><td>Around_threshold</td><td>0.855***(0.048)</td><td>0.504***(0.077)</td><td>0.711***(0.084)</td><td>0.266***(0.118)</td></tr><tr><td>After_threshold</td><td>-0.305***(0.018)</td><td>-0.171***(0.024)</td><td>-0.246***(0.028)</td><td>-0.071*(0.043)</td></tr><tr><td>Around_threshold × Public</td><td></td><td></td><td>0.217**(0.101)</td><td>0.331**(0.150)</td></tr><tr><td>After_threshold × Public</td><td></td><td></td><td>-0.101***(0.038)</td><td>-0.152***(0.052)</td></tr><tr><td>Log(Updates_incre)</td><td>0.335***(0.077)</td><td>0.625***(0.098)</td><td>0.340***(0.077)</td><td>0.637***(0.098)</td></tr><tr><td>Log(Comments_incre)</td><td>0.222***(0.027)</td><td>0.217***(0.040)</td><td>0.224***(0.027)</td><td>0.222***(0.039)</td></tr><tr><td>Featured</td><td>-0.155(0.095)</td><td>-0.394***(0.114)</td><td>-0.151(0.096)</td><td>-0.381***(0.114)</td></tr><tr><td>Log(Popular_rank)</td><td>-0.834***(0.039)</td><td>-0.780***(0.042)</td><td>-0.845***(0.039)</td><td>-0.793***(0.042)</td></tr><tr><td>Log(Magic_rank)</td><td>0.004(0.015)</td><td>0.042**(0.019)</td><td>0.003(0.015)</td><td>0.040**(0.019)</td></tr><tr><td>Has_fb_post</td><td>0.115**(0.043)</td><td>0.204***(0.055)</td><td>0.116***(0.042)</td><td>0.205***(0.055)</td></tr><tr><td>Has_twi_msg</td><td>0.194***(0.041)</td><td>0.180***(0.052)</td><td>0.198***(0.041)</td><td>0.185***(0.052)</td></tr><tr><td>Time-of-day FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Day-of-week FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Project FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of Observations</td><td>20,874</td><td>20,874</td><td>20,874</td><td>20,874</td></tr><tr><td>No. of Projects</td><td>426</td><td>426</td><td>426</td><td>426</td></tr><tr><td>Log Likelihood</td><td>-24,921.140</td><td>-35,217.825</td><td>-24,913.914</td><td>-35,209.589</td></tr></table>

Third, this paper enriches the literature by examining the heterogeneous threshold-induced effects across the public-good and private-good project categories. Most of existing studies on user motivation focus on one single platform and do not differentiate between different types of activities. The heterogeneity in the nature of activities, however, may provide novel insights into a deeper understanding of individual motivation. Our subgroup analysis sheds light on the moderating role of project prosociality on backers’ goal-gradient behavior. Specifically, we show that the desire to beat the goal is stronger in public-good projects than in private-good projects and attribute this difference to the social responsibility and high perceived impact that one can derive from making contributions to public goods. The fact that the two types of threshold effects are more salient in publicgood projects than in private-good projects offers further support for the claim that the strong prosocial motivation before and near goal attainment is likely to be the reason behind our findings.

## Practical Implications

This research has important implications for both platform designers and project creators in reward-based crowdfunding (e.g., [1, 53]). Backers who contribute at different stages of funding status may be driven by different motives. A better understanding of the importance of different motivations would allow platform designers to design their search and ranking mechanisms to better accommodate the interests of backers and attract more potential backers to pledge and share project information on their social networks. For example, Cheema and Bagchi [15] show that easy-to-visualize goals can enhance goal pursuit. Given the heightened level of backer motivation near the threshold-reaching time, platform designers can introduce a new ranking mechanism such as “Near Threshold”<sup>13</sup> to increase the visibility of projects that are close to reaching their thresholds. Furthermore, motivated by the evidence on backers’ strong prosocial motivation, platform designers can have a new feature such as “Projects in Need” to label those projects, especially public-good projects, that have accumulated a considerable number of backers already but still need a few days to reach their thresholds.

For project creators, our findings can provide guidance on the development of more effective and targeted marketing strategies. For instance, they can post more updates on the platform and other social media channels before the projects reach their thresholds to exploit the strong prosocial motivation of backers. They can also design their marketing messages in a way that emphasizes the prosocial nature of the project (e.g., how the success of the project can benefit society as a whole) and the potential impact that backers can have on others by pledging their money. Given that there are more backers during the daytime (8:00 am to 6:00 pm PDT) on weekdays, creators should increase their marketing activities within this time range. The findings on threshold effects can also guide project creators to choose funding goals more strategically. Creators who launch projects on crowdfunding platforms often face the question of how to choose an appropriate goal amount. Many of them are hesitant to choose a larger goal due to a concern that a small funding percentage may give backers the impression that the projects are of low quality. However, setting the goal too small may create the problem of insufficient funds even if the threshold is met. Our results suggest that project creators, especially those who initiate public-good projects, can slightly increase the goal amount to better monetize backers’ prosocial motivation. However, we caution that if the goals are set too high, projects may not be fully funded and creators will end up receiving nothing under the all-or-nothing fundraising scheme.

## Limitations and Future Research

Our study is subject to several limitations. First, omitted variable bias may be present. For example, creators may use channels other than Facebook and Twitter to advertise their projects. However, other marketing activities, if any, should be highly correlated with those on Facebook and Twitter, as creators often spread marketing messages across different platforms at the same time. Given that we have controlled for both project fixed effects and time-varying project characteristics, we believe that omitted variable bias should not be a serious concern for our study. Second, in our analyses, we exclude projects that reached their goals in the first three days of their fundraising periods. It is possible that backers’ motivations may be different for highly popular projects that reach their funding goals within a very short time period (e.g., one day). However, the empirical investigation of these projects is not feasible because backer support decays very fast in the first few days, regardless of the threshold-reaching status [36, 45].

Despite the limitations, we believe that our work makes a unique contribution to the crowdfunding literature by empirically investigating backers’ pledging and sharing behaviors at different stages of achieving the funding threshold. Future work can proceed in several ways. First, our paper focuses on the all-or-nothing funding type. Another common funding scheme is the keep-it-all model, in which creators keep all the money raised regardless of the funding status [18]. It would be interesting to examine the threshold-induced effects under this alternative funding scheme. Second, our study empirically examines two types of threshold-induced effects and infers backer motivations based on the results. To control for U-shaped diffusion pattern and other time-varying confounding factors, we take a time window of a few days before and after the threshold-reaching time. The findings may not generalize to time intervals that are far away from reaching the thresholds. Future researchers may wish to conduct experiments to validate our findings and examine the significance of backer motivations throughout the entire fundraising period. Third, the results are obtained using aggregate-level data, which prevents us from drawing conclusions at the individual level. It would also be interesting to study how the threshold effects vary with the characteristics of individuals.

2. https://www.kickstarter.com/help/stats (accessed October 2018).

## Conclusions

Reward-based crowdfunding has become a mainstream approach for entrepreneurs to secure funding for their creative projects. Despite the popularity, our understanding of backer motivations in reward-based crowdfunding platforms is rather limited and somewhat mixed. Leveraging the all-or-nothing mechanism employed by Kickstarter, we are able to provide empirical evidence on backer motivations by investigating the timing of backers’ pledging and sharing behaviors. Our findings suggest that backers exhibit a strong prosocial motivation, which prevails over their aversion to potential economic loss due to uncertainty in project quality and outcome. Furthermore, we show that both goal proximity and project prosociality positively affect the prosocial motivation of backers. Our results advance the current understanding of backer motivations in reward-based crowdfunding platforms and provide actionable guidance for both platform owners and entrepreneurs who are interested in this new form of fundraising.

Acknowledgments: The authors are listed in alphabetical order. We would like to thank three anonymous reviewers for their constructive comments. We are also grateful for the helpful feedback received from participants at Statistical Challenges in Electronic Commerce Research (SCECR 2017) and China Summer Workshop on Information Management (CSWIM 2017).

## Funding

We acknowledge financial support from the Hong Kong Research Grants Council [Project No: 16501317].

## NOTES

1. https://www.kauffman.org/microsites/state-of-the-field/topics/finance/crowdfunding (accessed October 2018).

3. https://venturebeat.com/2018/01/15/indiegogo-moves-beyond-crowdfunding-to-helpstartups-with-manufacturing/(accessed October 2018).

4. The prosocial motivation in this study is defined as “the desire to expend effort to benefit other people” [7, 29], which encompasses both the intrinsic and image motivations presented in Ariely et al. [6].

5. Social desirability bias refers to the tendency of survey respondents to answer questions in a socially desirable way rather than stating their true thoughts.

6. As shown in robustness checks, our results are robust to the use of alternative lengths of focal period, such as not more than 24 (72) hours from the threshold-reaching time interval.

7. We scraped projects in the seven most popular categories: Arts, Design, Film, Games, Music, Publishing, and Technology.

9. As shown in robustness checks, our results are robust to the inclusion of both this interval and the interval right before as the indicator.

10. For negative binomial model, we apply the following transformation on the coefficient to get the interpretation using percentage: exp (1.115) −1=204.96%.

11. Over 70% of backers on Kickstarter are from United States and Canada. Therefore, between 8am and 6pm PDT is their work time (https://www.statista.com/chart/1962/kickstar ter-pledges-by-country/, accessed on October 2018).

12. The mean progress of projects at two (four) hours before reaching the threshold is 94.38% (92.97%).

13. Kickstarter implemented a “Nearly Funded” feature on 11/02/2016. Our results are not affected by this new feature given that our data period is from 10/07/2015 to 12/15/2015. Instead, our results serve as empirical evidence for the effectiveness of this feature.

## REFERENCES

1. Agrawal, A.; Catalini, C.; and Goldfarb, A. Some simple economics of crowdfunding. Innovation Policy and the Economy, 14, 1 (2014), 63–97.

2. Agrawal, A.; Catalini, C.; and Goldfarb, A. Crowdfunding: Geography, social networks, and the timing of investment decisions. Journal of Economics & Management Strategy, 24, 2 (2015), 253–274.

3. Allison, P. D.; and Waterman, R. P. 7. Fixed-effects negative binomial regression models. Sociological Methodology, 32, 1 (2002), 247–265.

4. Andreoni, J. Impure altruism and donations to public goods: A theory of warm-glow giving. The Economic Journal, 100, 401 (1990), 464–477.

5. Anik, L.; and Norton, M. On being the “tipping point”: threshold incentives motivate behavior. NA – Advances in Consumer Research. Duluth, MN: Association for Consumer Research. 2015, pp. 85–89.

6. Ariely, D.; Bracha, A.; and Meier, S. Doing good or doing well? Image motivation and monetary incentives in behaving prosocially. American Economic Review, 99, 1 (2009), 544–555.

7. Batson, C. D. Prosocial motivation: Is it ever truly altruistic? Advances in Experimental Social Psychology, 20, (1987), 65–122.

8. Bekkers, R.; and Wiepking, P. A literature review of empirical studies of philanthropy: Eight mechanisms that drive charitable giving. Nonprofit and Voluntary Sector Quarterly, 40, 5 (2011), 924–973.

9. Bénabou, R.; and Tirole, J. Incentives and prosocial behavior. American Economic Review, 96, 5 (2006), 1652-1678.

10. Berglin, H.; and Strandberg, C. Leveraging customers as investors: The driving forces behind crowdfunding. Working Paper. Uppsala University, 2013.

11. Bretschneider, U.; and Leimeister, J. M. Not just an ego-trip: Exploring backers’ motivation for funding in incentive-based crowdfunding. The Journal of Strategic Information Systems, 26, 4 (2017), 246–260.

12. Burtch, G.; Ghose, A.; and Wattal, S. An empirical examination of the antecedents and consequences of contribution patterns in crowd-funded markets. Information Systems Research, 24, 3 (2013), 499–519.

13. Burtch, G.; Ghose, A.; and Wattal, S. Cultural differences and geography as determinants of online pro-social lending. MIS Quarterly, 38, 3 (2014), 773–794.

14. Burtch, G.; Hong, Y.; and Liu, D. The role of provision points in online crowdfunding. Journal of Management Information Systems, 35, 1 (2018), 117–144.

15. Cheema, A.; and Bagchi, R. The effect of goal visualization on goal pursuit: Implications for consumers and managers. Journal of Marketing, 75, 2 (2011), 109–123.

16. Cholakova, M.; and Clarysse, B. Does the possibility to make equity investments in crowdfunding projects crowd out reward-based investments? Entrepreneurship Theory and Practice, 39, 1 (2015), 145–172.

17. Cryder, C. E.; Loewenstein, G.; and Seltman, H. Goal gradient in helping behavior. Journal of Experimental Social Psychology, 49, 6 (2013), 1078–1083.

18. Cumming, D. J.; Leboeuf, G.; and Schwienbacher, A. Crowdfunding models: keep-itall vs. all-or-nothing. Working paper, https://ssrn.com/abstract=2447567, (2015).

19. Daughety, A. F.; and Reinganum, J. F. Public goods, social pressure, and the choice between privacy and publicity. American Economic Journal: Microeconomics, 2, 2 (2010), 191–221.

20. De Buysere, K.; Gajda, O.; Kleverlaan, R.; Marom, D; and Klaes, M. A framework for European crowdfunding. Brussels: European Crowdfunding Network, 2012.

21. Filiz-Ozbay, E.; and Ozbay, E. Y. Effect of an audience in public goods provision. Experimental Economics, 17, 2 (2014), 200–214.

22. Furnham, A. Response bias, social desirability and dissimulation. Personality and Individual differences, 7, 3 (1986), 385–400.

23. Gerber, E. M.; and Hui, J. Crowdfunding: motivations and deterrents for participation. In ACM Transactions on Computer-Human Interaction (TOCHI), 20, 6 (2013), Article 34.

24. Ghose, A.; Ipeirotis, P. G.; and Li, B. Examining the impact of ranking on consumer behavior and search engine revenue. Management Science, 60, 7 (2014), 1632-1654.

25. Gierczak, M.; Bretschneider, U.; and Leimeister, J. M. Is all that glitters gold? Exploring the effects of perceived risk on backing behavior in reward-based crowdfunding. International Conference on Information Systems Proceeding, Atlanta, GA: Association for Information Systems. 2014.

26. Gladwell, M. The tipping point: How little things can make a big difference. Boston: Little, Brown. 2006.

27. Gleasure, R.; and Feller, J. Does heart or head rule donor behaviors in charitable crowdfunding markets? International Journal of Electronic Commerce, 20, 4 (2016), 499–524.

28. Goes, P. B.; Guo, C.; and Lin, M. Do incentive hierarchies induce user effort? Evidence from an online knowledge exchange. Information Systems Research, 27, 3 (2016), 497–516.

29. Grant, A. M. Does intrinsic motivation fuel the prosocial fire? Motivational synergy in predicting persistence, performance, and productivity. Journal of Applied Psychology, 93, 1 (2008), 48–58.

30. Griskevicius, V.; Tybur, J. M.; and Van den Bergh, B. Going green to be seen: status, reputation, and conspicuous conservation. Journal of Personality and Social Psychology, 98, 3 (2010), 392–404.

31. Hausman, J. A. Specification tests in econometrics. Econometrica, 46, 6 (1978), 1251–1271.

32. Herzenstein, M.; Dholakia, U. M.; and Andrews, R. L. Strategic herding behavior in peer-to-peer loan auctions. Journal of Interactive Marketing, 25, 1 (2011), 27–36.

33. Hong, K.; Hu, Y.; and Burtch, G. Embeddedness, Pro-Sociality, and Social Influence: Evidence from Online Crowdfunding. MIS Quarterly, 42, 4 (2018), 1211–1224.

34. Kim K.; and Viswanathan S. The Experts in the Crowd: The Role of Experienced Investors in a Crowdfunding Market. MIS Quarterly, forthcoming (2018).

35. Kivetz, R.; Urminsky, O.; and Zheng, Y. The goal-gradient hypothesis resurrected: Purchase acceleration, illusionary goal progress, and customer retention. Journal of Marketing Research, 43, 1 (2006), 39–58.

36. Kuppuswamy, V.; and Bayus, B. L. Crowdfunding creative ideas: The dynamics of project backers. The Economics of Crowdfunding, 2018, Cham: Palgrave Macmillan, pp. 151–182.

37. Labaree, D. F. Public goods, private goods: The American struggle over educational goals. American Educational Research Journal 34, 1 (1997), 39–81.

38. Lin, M.; Prabhala, N. R.; and Viswanathan, S. Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. Management Science, 59, 1 (2013), 17–35.

39. Lin, M., and Viswanathan, S. Home bias in online investments: An empirical study of an online crowdfunding market. Management Science, 62, 5 (2015), 1393–1414.

40. Liu, D.; Brass, D. J.; Lu, Y.; and Chen, D. Friendships in Online Peer-to-Peer Lending: Pipes, Prisms, and Relational Herding. MIS Quarterly, 39, 3 (2015), 729–742.

41. Liu, L.; Suh A.; and Wagner C. Donation Behavior in Online Micro Charities: An Investigation of Charitable Crowdfunding Projects. In Proceedings of the 50th Hawaii International Conference on System Sciences, Atlanta: Association for Information Systems, 2017, pp. 843–852.

42. Lu, Y.; Gupta, A.; Ketter, W.; and Heck, E. V. Exploring bidder heterogeneity in multichannel sequential B2B auctions. MIS Quarterly, 40, 3 (2016), 645–662.

43. Mollick, E. The dynamics of crowdfunding: an exploratory study. Journal of Business Venturing, 29, 1 (2014), 1–16.

44. Mutter, T.; and Kundisch, D. Behavioral mechanisms prompted by badges: The goalgradient hypothesis. In International Conference on Information Systems Proceeding, Atlanta: Association for Information Systems, 2014.

45. Rakesh, V.; Choo, J.; and Reddy, C. K. Project Recommendation Using Heterogeneous Traits in Crowdfunding. In International Conference on Web and Social Media, Palo Alto: Association for the Advancement of Artificial Intelligence, 2015, pp. 337–346.

46. Rhue, L.; and Clark, J. The consequences of authenticity: quantifying racial signals and their effects on crowdfunding success. Working paper, https://ssrn.com/abstract=2837042, (2018).

47. Ryu, S.; Kim K.; and Kim, Y.G. Reward versus Philanthropy Motivation in Crowdfunding Behavior. In Pacific Asia Conference on Information Systems Proceeding, Atlanta: Association for Information Systems, 2016.

48. Samuelson, P. A. The pure theory of public expenditure. The Review of Economics and Statistics, 36, 4 (1954), 387-389.

49. Simonsohn, U. eBay’s crowded evenings: Competition neglect in market entry decisions. Management Science, 56, 7 (2010), 1060–1073.

50. Smith, V. H.; Kehoe, M. R.; and Cremer, M. E. The private provision of public goods: Altruism and voluntary giving. Journal of Public Economics, 58, 1 (1995), 107–126.

51. Thies, F.; Wessel, M.; and Benlian, A. Effects of social interaction dynamics on platforms. Journal of Management Information Systems, 33, 3 (2016), 843–873.

52. Wu, J.; Shi, M.; and Hu, M. Threshold effects in online group buying. Management Science, 61, 9 (2014), 2025–2040.

53. Wu, Z.; Lin, Z.; and Tan, Y. Crowdfunding platforms: The role of information providers. Working paper, https://ssrn.com/abstract=2832597, (2016).

54. Xu, A.; Yang, X.; Rao, H.; Fu, W. T.; Huang, S. W.; and Bailey, B. P. Show me the money!: An analysis of project updates during crowdfunding campaigns. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, New York City, NY: Association for Computing Machinery, 2014, pp. 591–600.

55. Younkin, P.; and Kuppuswamy, V. The colorblind crowd? Founder race and performance in crowdfunding. Management Science, 64, 7 (2017), 3269–3287.

56. Zhang, J.; and Liu, P. Rational herding in microloan markets. Management Science, 58, 5 (2012), 892–912.

57. Zhang, Y.; and Huang, S. C. How endowed versus earned progress affects consumer goal commitment and motivation. Journal of Consumer Research, 37, 4 (2010), 641–654.
