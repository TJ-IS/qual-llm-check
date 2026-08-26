---
otero_id: 28409
otero_key: "67CKJE7T"
title: "Content Length Limit: How Does It Matter for a Consumer-to-Consumer Media Platform?"
authors: "Zheyin (Jane) Gu; Xuying Zhao"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0595"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Content Length Limit: How Does It Matter for a Consumer-to-Consumer Media Platform?

Zheyin (Jane) Gu,<sup>a,</sup>\* Xuying Zhao<sup>b</sup>

<sup>a</sup> Marketing Department, University of Connecticut, Storrs, Connecticut 06269; <sup>b</sup> Department of Information and Operations Management, Texas A&M University, College Station, Texas 77843

Contact: jane.gu@uconn.edu, https://orcid.org/0000-0002-8166-0144 (Z(J)G); xzhao@mays.tamu.edu, https://orcid.org/0000-0002-7695-5829 (XZ)

Received: October 29, 2022 Revised: June 22, 2023; September 23, 2023; November 4, 2023 Accepted: November 23, 2023 Published Online in Articles in Advance: January 3, 2024

https://doi.org/10.1287/isre.2022.0595

Copyright: © 2024 INFORMS

Abstract. Our study is inspired by the rapid growth of consumer-to-consumer (C2C) media platforms such as TikTok. We adopt a classical economical approach to modeling how utility-maximizing consumers select content pieces to view on a C2C media platform through a sequential inspection process and investigate how a platform in pursuit of market performance can devise an optimal policy on content length limit to induce desired viewer behaviors. First, we show that when content on the platform are longer, viewers set a higher standard of match value in selecting content to view, leading to a lower click-through rate of contributed content on the platform. This finding suggests that a tight limit on content length increases click-through rate. Second, we show that extended content length on the platform first enhances platform performance but then hurts its performance, following an inverted U-shape curve. This pattern holds true for short-term performance measured by viewer traffic and total viewing time, as well as for long-term performance measured by total consumer surplus. This finding suggests the existence of an optimal content length. Third, we find that the optimal content length that maximizes viewer traffic is smaller than that maximizes total viewing time, which is further smaller than that maximizes consumer surplus. As such, a platform that switches the strategic focus from short-term advertising revenue to long-term growth will benefit from extending content length limit.

History: Karthik Kannan, Senior Editor; Zhengrui Jiang, Associate Editor.

Keywords: consumer-to-consumer (C2C) media platform • digital content • content length limit • game theory

## 1. Introduction

TikTok, the mobile app that allows users to create and share 15-second videos on any topic, has experienced skyrocketing success since its launch in 2016. Its monthly active users reached 1.2 billion in Q4 2021 and are expected to reach 1.8 billion by the end of 2022. The company makes \$4.6 billion in revenue in 2021, a 142% increase year-on-year (Iqbal 2023). TikTok represents a type of media platform where content is self-posted by individual contributors who are willing to, that is, consumer-to-consumer (C2C) media platforms (Jain and Qian 2021, Bhargava 2022), as opposed to businessto-consumer (B2C) media platforms (Athey et al. 2018, Lin 2020, Amaldoss et al. 2021) such as Netflix, where content are acquired from professional producers. As a result of this self-posting mechanism, content on C2C media platforms typically cover a wide range of topics, reflecting the contributor’s diverse backgrounds. For example, the most popular content categories on TikTok include not only entertainment and dance, but pranks, fitness, do it yourself (DIY), skincare, and cooking (Izea 2023). Viewers with heterogeneous tastes are attracted by the large variety of content on C2C media platforms but may find difficulties choosing from the voluminous offerings the right pieces that match their tastes. Our study develops an analytical model to characterize viewer decisions about visiting a C2C media platform and choosing suitable content to view and investigates how a C2C platform in pursuit of desirable market outcomes can strategically design content length limit to influence consumer decisions.

No previous research has examined the strategic implications of content length limit for a C2C platform, although people tend to agree that the “short” video format is pivotal to TikTok’s success. A short video is defined as one that is less than three minutes (Hubspot 2023). After the initial success, TikToK extended the content length limit from 15 seconds to one minute in 2020 and continued its rapid expansion. In 2021, TikToK again extended the content length limit to three minutes (Kastrenakes 2021). In 2022, TikTok tried to break into the long-video market dominated by YouTube by extending the content length limit to 10 minutes (Spangler 2022), yet its focus is still on the short video market. With the hope to replicate the TikTok magic, a number of new short video platforms have been founded, including startups such as Clash (https://clashapp.co/) and Thriller (https://triller.co/), as well as new features launched by big players such as Instagram Reels and YouTube Shorts. To help practitioners take better advantage of the business opportunity, researchers need to bring about the business logic of short videos in a C2C media platform. In particular, new theoretical insights are called for to understand how the limit for short video length contributes to TikTok’s phenomenal success and what motivates TikTok to extend the length limit for short videos.

As the first effort to investigate the strategic impact of content length limit, our study follows a classical, economical modeling approach led by Wolinsky (1986) and Anderson and Renault (1999). We examine how content length limit affects the sequential inspection process through which utility-maximizing consumers select suitable content to view and consequently affects platform performance measured by viewer traffic, total viewing time, and total consumer surplus. We then investigate how the migration in objective function over time may lead to changes in a platform’s optimal policy for content length limit. This modeling approach allows us to reveal the most fundamental driving force in the impact of video length limit, which paves the foundation for incorporating other factors.

Previous research has demonstrated the impact of content length on the effectiveness of content delivery. These studies typically take experimental approaches, asking subjects to view content and then comparing subject perceptions during viewing (e.g., engagement, irritation) and after viewing (e.g., recall, attitude) across different lengths of content. For example, in the context of commercials, researchers find that longer commercials (e.g., 30-second versus 15-second versus 7-second) are generally more effective (Singh and Cole 1993, Varan et al. 2020), but cause more irritation to viewers (Jeon et al. 2019). In the context of online education, Slemmons et al. (2018) find that the same content delivered in 10-minute or 20-minute videos made no significant difference in learning, although students self-reported to favor short videos. Manasrah et al. (2021) find that most students prefer online lectures of 6–10 minutes and consider videos under 3 minutes as including incomplete information. Whereas these studies focus on examining the impact of content length on consumers’ viewing experience ex post, our research focuses on investigating the impact of content length on how consumers select content to view ex ante before they actually view them. This ex ante decision is important because, on C2C media platforms, consumers face a large volume of content with similar lengths (owing to the content limit) but differentiated match values.

We investigate the following research questions: First, how does content length limit of a C2C media platform affect consumers’ decisions about which content pieces and how many content pieces to view? Second, how does content length limit of a C2C media platform affect its performance? Last, how can a C2C media platform use content length limit as a strategic tool?

We consider a platform that decides content length limit to maximize its market performance, measured by viewer traffic, total viewing time, and consumer surplus. Upon arriving at the platform, a utility-maximizing consumer sequentially inspects content pieces by incurring inspection costs and evaluates their match values, until the consumer finds one piece that matches the consumer’s taste. After the consumer incurs a time cost to view the content piece, the consumer decides whether to exit the platform, or to stay on the platform and find another content piece to view. Consumers decide whether to visit the platform based on the rational expectation about whether they will find suitable content to view before exiting. Our modeling approach follows the literature on sequential product search (Stahl 1989) in specifying consumer decision to select a content piece to view. Additionally, our study augments this literature by specifying a consumer’s decision about how many content pieces to view. This scenario of multi-item consumption is unique to and common in our research context of C2C media platforms.

In deciding which content pieces to view and how many content pieces to view, rational consumers balance the gains and costs associated with the time spent on viewing a content piece. On the one hand, a consumer derives enjoyment from viewing a content piece that matches the consumer’s taste. Extended content length generates enhanced enjoyment, constituting an economic gain. Yet the marginal benefit from viewing an additional content piece declines, according to the law of diminishing returns (Sundararajan 2004), and declines more rapidly on a platform that hosts longer content pieces. On the other hand, time is a scarce resource and is often equated to “money” that consumers do not want to waste (Leclerc et al. 1995). The longer time spent on viewing a content piece represents a higher opportunity cost, which is the loss of a potential gain from viewing a different content piece (Becker 1965). The limit on content length sets a consumer’s expectation on the time to spend on viewing a content piece and so moderates how the consumer makes tradeoffs between the gains and costs of time.

Our analysis generates several interesting findings. First, when content on the platform are longer, viewers set a higher standard of match value in searching for content to view, leading to a lower click-through rate of the contributed content. This finding suggests that a tight limit on content length can help increase click-through rate and may help explain the popularity of TikTok. Second, viewer traffic to a platform first increases with content length but then decreases, following an inverted U-shaped curve. Moreover, the total viewing time of consumers on the platform and the total consumer surplus also vary with content length following an inverted

U-shaped curve. Whereas higher viewer traffic and higher total viewing time of consumers imply greater advertising revenue for the platform, higher consumer surplus leads to greater consumer satisfaction and so implies future market growth (Srivastava et al. 1998) and better stock market performance (Luo et al. 2010). Our finding thus suggests the existence of optimal content length for a platform seeking to maximize short-term advertising revenue or long-term growth. Third, the optimal content length that maximizes viewer traffic is smaller than that maximizes total viewing time, which is further smaller than that maximizes consumer surplus. This finding implies that a platform that switches the strategic focus from short-term advertising revenue to long-term growth will benefit from extending the content length limit and enhancing consumer surplus. This insight provides a possible explanation for TikTok’s extensions of content length limit after its initial success.

Collectively, our study develops an analytical model to examine how consumers select suitable content to view from the large volume of content available on a C2C platform. We demonstrate how the platform policy on content length limit through affecting consumers content selection process brings nonlinear impact to various measures of platform performance. Our theoretical insights deepen the understanding of business practices and provide guidance about how a platform should craft and adjust policies in the changing business environment.

The remaining sections of the paper proceed as follows. We review related literature in Section 2. In Section 3, we build the model. Then we solve the model in Section 4. Section 5 demonstrates the robustness of our key insights in model extensions. Section 6 concludes the paper.

## 2. Literature

Our study is related to two streams of literature: video length and media platforms. Here we review each stream and position our study against existing works.

## 2.1. Video Length

Advertising researchers have explored the impact of commercial lengths. It is generally believed that longer commercials improve advertising effectiveness, measured by audiences’ learning, attention, recall, attitude toward ads, and advertisement likability (Wheatley 1968, Singh and Rothschild 1983, Mord and Gilson 1985, Fabian 1986, Rethans et al. 1986, Singh et al. 1988, Rogers 1995). This is because a longer commercial, in comparison with a shorter one, gives the viewer more time to process the message and thus enhances viewer learning and message effectiveness for persuasion (Rethans et al. 1986, Pechmann and Stewart 1988, MacInnis and Jaworski

1989). More recent advertising research reveals the benefits of short commercials. For example, Singh and Cole (1993) find that informational 15-second commercials are as effective as informational 30-second commercials in several situations, whereas emotional 30-second commercials are superior to emotional 15-second commercials in influencing a viewer’s learning of brand name and attitude. Varan et al. (2020) find that 7-second advertisements were almost as effective (measured by unaided recall) as 15-second advertisements and 60% as effective as 30-second advertisements, indicating diminishing returns of advertising length. Jeon et al. (2019) examine consumers’ perceptions and behaviors regarding commercials during online streaming and find that the presence of a timer decreases viewers’ perceived irritation for short commercials but increases irritation for long commercials. Also, subjects were more likely to skip an in-stream commercial when they perceived greater irritation.

Some researchers examine the impact of video length in online learning. Cognition load theory (Chase and Simon 1973, Chandler and Sweller 1991, DiMaggio 1997) predicts that shorter videos will help reduce extraneous cognitive load related to the design of the instructional materials and therefore allows students to focus on germane cognitive load of constructing schema. Slemmons et al. (2018) compare 10-minute and 20-minute videos and finds that video length does not influence a student’s immediate ability to recall content. However, shorter videos may influence a student’s capacity to recall information and demonstrate understanding over a longer scale. From students’ perspective, there seems to be an optimal video length. Hsin and Cigas (2013) show that students prefer six- to nine-minute videos based on their engagement time. Manasrah et al. (2021) find that the majority of students preferred the length of video lectures to be between 6 and 10 minutes, whereas some preferred 10- to 20-minute videos; short videos less than 3 minutes were perceived as having incomplete information and not useful.

Whereas the previously discussed works on video content take an empirical approach, our study takes a game-theoretical approach. More importantly, the existing research focuses on examining how video length affects consumers’ ex post perception of video content during watching (e.g., engagement, irritation) or after watching the video (e.g., recall, attitude). These findings have implications for content contributors such as advertisers and educators. In contrast, our study examines how video length affects consumers’ ex ante deci sion about which videos to watch and whether to visit a media platform. Our findings deepen the understanding of how the platform can use content length as a strategic tool to attract viewer traffic, boost content viewing, and enhance viewer experience.

## 2.2. Media Platforms

Early research on media platforms focuses on the business-to-consumer (B2C) context where content on the platform are acquired from professional producers. This body of literature focuses on modeling the consumer side of the market and investigates how a platform decides pricing and advertising policies under the crossexternalities between consumers and advertisers. Dukes and Gal-Or (2003) show that broadcasters can benefit from offering exclusive advertising contracts. Anderson and Coate (2005) show that, depending on the extent to which consumers regard advertising as a nuisance, competing platforms may overprovide or underprovide advertisements (compared with the socially optimal level of advertising). Godes et al. (2009) find that competition for advertisers makes a competing platform less willing to undercut the price for consumers. Athey et al. (2018) examine how consumer multihoming across competing platforms affects advertisers’ platform decisions and platforms’ investment in quality content. Lin (2020) shows that price discrimination on the consumer side of a platform can enforce price discrimination on the advertiser side. Amaldoss et al. (2021) examine the proportion of bandwidth (or space) that a media platform should allocate to content versus ads.

Recently, growing research attention has been paid to C2C context where content on the platform are selfposted by individual contributors. Existing studies in this literature have focused on the supplier side of the market, examining contributors’ decisions to join a platform and platform strategies to attract contributors. Toubia and Stephen (2013) show that contributors motivation to post content on social media is related to their intrinsic utility and image-related utility. Zhang and Sarvary (2015) show that competition between two platforms will make them endogenously acquire differentiated contributors. In these two studies, contributors do not receive payments for posting content. Bhargava (2022) examines how the distribution of contributor capabilities affects market concentration among contributors and how the distribution can be influenced by platform design. Jain and Qian (2021) examine how a platform can use revenue-sharing policies to encourage high-quality content creation. Our study complements the literature on C2C media platforms by focusing on the consumer side of the market. We examine consumers decisions to join and view content on a platform and investigate how the content length limit as a platform strategy can affect consumer decisions. We embed a micromodel of consumer content searching and viewing and therefore bring rich theoretical insights into how content length limit affects important metrics of consumer market performance, including viewer traffic, clickthrough rate, total viewing time, and consumer surplus.

Broadly, our work belongs to the literature on twosided platforms (Caillaud and Jullien 2003; Rochet and

Tirole 2003, 2006; Armstrong 2006; Armstrong and Wright 2007). A large body of this research examines platform mechanisms that facilitate the cross-side externalities between buyers and sellers. Hagiu and Wright (2020) examine a retail platform’s decision to facilitate the entry of untested new products/sellers alongside established products/sellers. Hagiu et al. (2020) examine a retail platform’s decision to invite rivals to sell products or services on top of its core product. In the context of resourcesharing platforms (e.g., Uber, Airbnb), Benjaafar et al. (2019) compare collaborative versus noncollaborative con sumption in terms of ownership and use levels, consumer surplus, and social welfare. Cachon et al. (2017) examine pricing schemes on self-scheduling platforms including surge pricing. Dou and Wu (2021) examine the interplay between the nonpricing policy of “piggybacking” (i.e., recruiting exclusive users from external networks) and pricing controls in accelerating user adoption in launching a two-sided platform. Our study also shows the existence of network effects between the two sides of a C2C media platform. In particular, more contributors post content when anticipating more viewer traffic.

## 3. Model

We consider a C2C media platform where consumers with heterogeneous tastes join to view contributed content with differentiated horizontal features. The platform operates in multiple strategic phases. In a strategic phase, the platform sets the policy for content length limit T to maximize its objective function. We focus on a content length limit that is reasonable in a given market. For example, in a short video market, the content length is under three minutes (Hubspot 2023). Meanwhile, the content length cannot be too short for consumers to derive any value from viewing it. For example, TikTok has specified that videos cannot be less than three seconds (Flixier 2022). Given the platform’s content length limit, contributors post content, and consumers make decisions to visit and view content on the platform.

Across strategic phases, the platform can set different strategic objectives and adjust content length limit accordingly. For example, the platform may switch goals from maximizing consumer traffic to maximizing total consumer viewing time or total consumer surplus. Discussing multiple strategic phases allows us to investigate a platform’s adjustment in content length limit. For example, TikTok initially set a 15-second limit, but since 2020 has extended the limit multiple times. Our analysis only applies when the platform adjusts content length limit within the reasonable range of a given market. In particular, TikTok’s latest extension of video length limit to 10 minutes can be viewed as an effort to enter the long video market and therefore is beyond our analysis of short videos (i.e., under 3 minutes). Here we detail our specifications for the platform, content contributors, and consumers. A summary of key model notation is given in Table 1.

Table 1. Key Model Notation

<table><tr><td>Notation</td><td>Meaning</td></tr><tr><td> $T > 0$ </td><td>Content length limit</td></tr><tr><td> $V \in [v_0 - \sigma, v_0 + \sigma]$ </td><td>Unit match value of a content piece from content feeds</td></tr><tr><td> $v$ </td><td>Realization of  $V$  after inspection</td></tr><tr><td> $v_0 > 0$ </td><td>Mean of unit match value across content feeds</td></tr><tr><td> $\sigma \in [0, v_0]$ </td><td>Content feed variety</td></tr><tr><td> $c > 0$ </td><td>Cost of inspecting a content piece</td></tr><tr><td> $\delta \in [\underline{\delta}, \overline{\delta}], 0 \leq \underline{\delta} \leq \overline{\delta}$ </td><td>Consumer-specific time cost coefficient</td></tr><tr><td> $CTR$ </td><td>Click-through rate of a content piece after being inspected</td></tr></table>

## 3.1. Platform

The platform tries to match viewers with content they enjoy and provides each viewer a customized set of content pieces, or content “feeds,” that are likely to match the consumer’s taste. Although the platform cannot determine the exact match value between a particular consumer and a specific content piece, we assume that its algorithm ensures that the match values of content feeds follow a uniform distribution on interval $\left[ v _ { 0 } - \sigma , v _ { 0 } + \sigma \right]$ The mean of this distribution, $v _ { 0 } ( v _ { 0 } > 0 )$ , is exogenously given and represents the platform’s knowledge about consumers. For example, TikTok’s content feeding algorithm considers a consumer’s video likes and shares, accounts followed, comments posted, content created, videos completed, and favorited videos (Zote 2022).

Parameter $\sigma ( 0 < \sigma < v _ { 0 } )$ defines the range of the match value distribution and captures the diversity in content feeds set by the platform. For example, a media platform can include in the feeds content pieces that are similar to what a consumer has previously viewed. The homogeneity in content feeds suggests a small σ. Alternatively, the platform may include in the feeds a variety of content pieces that are different from what the consumer has previously viewed. The consumer may find some pieces irrelevant and perceive a very low match value but may also find some pieces eye-opening and perceive a very high match value. This content-feeding strategy suggests a large σ. In practice, different platforms may set different levels of content feed variety. For example, many platforms set recommender systems in a way that provides a consumer with content feeds similar to what the consumer has previously viewed (Lu et al. 2015), whereas TikTok believes that a platform should provide diversified content feeds to keep consumers interested even if they may find some content irrelevant (TikTok 2020).

## 3.2. Contributors

A large number of contributors post a wide variety of content on the platform. The horizontal features (e.g., topic, style) of contributed content are observable to the platform. In the main model, we assume that a contributor always posts a content piece with a maximum length T to simplify analysis. Later in model extensions, we will demonstrate the robustness of our results when a contributor can provide a content piece with a length shorter than T.

## 3.3. Consumers

We consider a large number of consumers with heterogeneous tastes. A consumer first decides whether to visit the platform. Upon visiting the platform, the consumer is provided with a set of customized content feeds. This constitutes a decision environment similar to in Wolinsky (1986) and Anderson and Renault (1999). Following this literature, we assume that the consumer must incur an inspection cost to learn the match value with a content piece. A consumer inspects content feeds randomly and sequentially with costless recalls to find a suitable content piece to view.

To be consistent with practice, we allow a consumer to view multiple content pieces on the media platform and assume that a consumer’s marginal benefit from viewing an additional content piece diminishes over time. Each time after a consumer has viewed a content piece, the consumer evaluates the expected surplus from going through the inspection process again and viewing another content piece. If the surplus is positive, the consumer will stay on the platform, but otherwise the consumer will exit the platform.

Figure 1 illustrates a consumer’s decision flow upon arriving at the platform. In the figure, $N ^ { * } = 0 , 1 , 2 . .$ represents the total number of content pieces that a consumer has viewed on the platform. At the entry point of the decision flow, $N ^ { * } = 0 .$ . At the exit point of the decision flow, N<sup>∗</sup> gives the total number of content pieces that the consumer has viewed during the stay on the platform. Here we detail this decision flow for a representative consumer.

Figure 1. Consumer Decision-Making Process  
![](/api/attachments/67CKJE7T/fulltext/images/46f471cda45b5197ca29c394c6def8b41b3f2c6398ed488c27d8144054ddab9f.jpg)  
Note. N<sup>∗</sup> is the total number of content pieces viewed.

First, upon arriving at the platform, the consumer enters the inspection step. The consumer randomly inspects a content piece from the set of feeds to learn its match value.<sup>1</sup> We assume that the match value of a content piece is consistent throughout as common knowledge. This assumption is reasonable in our research context of short videos, whose content topic and shooting style are typically consistent throughout. We thus model that the content piece has a total match value of $v \cdot T ,$ with unit match value v being a realization of the random variable V that follows a uniform distribution on $\left[ v _ { 0 } - \sigma , v _ { 0 } + \sigma \right]$ and T being the content length. This formulation of total match value abstracts out consumer satiation. In model extension, we show the robustness of our main results under a general function of total match value and when a consumer may terminate watching before the entire video is over.

The consumer incurs inspection cost $c \left( c > 0 \right)$ to learn the unit match value v. We assume c mainly consists of cognition cost and the time involved in inspection is trivial. In practice, the consumer can look at the cover information and take a quick sample of the video. Under the assumption of consistent match value throughout, a consumer only needs to sample a moment of a video to inspect its unit match value v. We assume c is independent of content length T in the main model and demonstrate the robustness of our main results when this assumption is relaxed later in model extension.<sup>2</sup> For the sake of parsimony, we assume that after inspection the consumer learns the true match value with a content piece. In model extension, we show that relaxing this assumption does not affect our key results.

Next, the consumer enters decision point 1. We provide details here.

3.3.1. Decision Point 1. At this decision point, the consumer decides whether to view the content piece that has just been inspected with known unit match value $v ,$ to skip it, or to exit the platform. If being viewed, the content piece becomes the nth $\left( n = N ^ { * } + 1 \right)$ ) the consumer views on the platform. We use $U _ { e } ( n , v )$ to denote the consumer’s utility from viewing this content piece as the nth piece viewed on the platform. We let $U _ { s } ( n , v )$ denote the consumer’s expected utility from skipping this content piece and keep looking for the nth content to view. The consumer obtains zero utility from exiting the platform. We first derive $U _ { e } ( n , v )$ and $U _ { s } ( n , v )$ , respectively, and then specify the consumer’s decision rules.

Viewing. A consumer incurs time cost for viewing a content piece. We specify that a consumer who views n pieces of content on the platform incurs a total time cost of $\delta ( n T ) ^ { 2 }$ , where nT is the total length of n content pieces and parameter δ is the time cost coefficient specific to the consumer. That is, we assume the time cost increases convexly with nT, indicating an increasing marginal cost associated with viewing an additional content piece on the platform and consequently a diminishing surplus from doing so. This specification is consistent with the classical assumption that most consumption goods have diminishing marginal returns (Sundararajan 2004, Abhishek et al. 2016, Chellappa and Mehra 2018). We assume δ follows a uniform distribution on [δ, δ] $( 0 <$ $\underline { { \delta } } < \overline { { \delta } } )$ across all consumers. Taking the difference between the consumer’s total time cost of viewing n content pieces $( \mathrm { i . e . , } \delta ( n T ) ^ { 2 } )$ and viewing $n - 1$ pieces $( \mathrm { i . e . , }$ $\delta ( ( n - 1 ) T ) ^ { 2 } )$ , we obtain the consumer’s time cost for viewing the nth piece, $\cdot \delta ( 2 n - 1 ) T ^ { 2 }$

We give the consumer’s utility $U _ { e }$ from viewing a content piece with match value v as the nth content piece to view as

$$
\begin{array}{c} {U _ {e} (n, v) = v T - (\delta (n T) ^ {2} - \delta ((n - 1) T) ^ {2})} \\ {= v T - \delta (2 n - 1) T ^ {2}.} \end{array}\tag{1}
$$

Note that $U _ { e } ( n , v )$ decreases with $n ,$ indicating diminishing benefits from viewing an additional content piece, and also concave in T, indicating diminishing returns from viewing a longer content piece. This notion of diminishing returns of repeated experiences or satiation is documented in laboratory studies (Redden 2008). Intuitively, as a consumer views more and more content pieces, the marginal benefits decrease because of either a burnout effect or some new constraint that prevents the consumer from enjoying more content (e.g., the consumer may need to rest). This property ensures that consumers will not watch an infinite amount of content. In particular, the quadratic function format is commonly used to capture diminishing returns (Guo et al. 2019, Wang et al. 2023) because of its nice property in taking derivatives. In model extension, we show that our main results continue to hold under a general functional format of the viewing cost that ensures diminishing returns of viewing an additional content piece.

After viewing, the consumer exits decision point 1, following the arrow marked by “view” in Figure 1.

Skipping. If the consumer skips the content piece just inspected with known match value $v ,$ the consumer will keep looking for the nth content piece to view. In particular, the consumer will follow the arrow marked by “skip” in Figure 1 to go back to the inspection step and then re-enter decision point 1. Before skipping, the consumer evaluates the maximum ex ante expected utility $U _ { s } ( n , v )$ from doing so, which is given by

$$
\begin{array}{c} U _ {s} (n, v) = E _ {V} [ \max \{0, U _ {e} (n, \max \{v, V \}), \\ U _ {s} (n, \max \{v, V \}) ] - c. \end{array}\tag{2}
$$

In Equation (2), the second term c gives the consumer’s expected cost from going through the inspection step again. The consumer expects to inspect another randomly selected content piece from the set of feeds provided by the platform and learn its unit match value as another realization of the random variable V. For example, in TikTok, a consumer can easily skip the current video by swiping up the screen and TikTok automatically pushes the next video feed to the screen.

The first term in Equation (2) gives the consumers expected surplus from entering decision point 1 again. Note that at the time of forming $U _ { s \prime }$ the consumer is uncertain about the realization of the random variable V and so takes expectation of this surplus across all realizations of V. With any specific realization of $V ,$ the consumer anticipates three possible actions and chooses the one that generates the maximum surplus. The utilities of the three actions constitute the three components in the max function respectively. First, the consumer may exit the platform and obtain zero surplus. Second, the consumer may view a content piece, either the previously skipped one through free recall or the newly inspected one, whichever has a higher match $\mathrm { v a l u e } . ^ { 3 }$ If the consumer goes back to view the skipped content piece, the surplus is $U _ { e } ( n , v )$ . If the consumer views the newly-inspected piece, the consumer gets surplus $U _ { e } ( n , V )$ . Therefore, the consumer’s surplus from viewing is $U _ { e } ( n , m a x \{ v , V \} )$ ). Third, the consumer may skip the newly-inspected content piece again. The corresponding surplus is $U _ { s } ( n , \operatorname* { m a x } \{ v , V \} )$ ). Note that the total number of content pieces that the consumer has viewed remains the same as before skipping and so the index for the next content piece to view remains n. This is why n appears on the first term (but not n + 1).

As can be seen, $U _ { s } ( n , v )$ has a recursive structure, where the index n remains the same when the consumer keeps skipping content pieces to re-enter decision point 1. The future inspection cost associated with skipping a future content piece is incorporated through future $U _ { s \prime }$ which enters into the right-hand side of Equation (2).

Viewing, Skipping, or Exiting. We assume that the consumer views a content piece just inspected with known match value v if $U _ { e } ( n , v ) > \operatorname* { m a x } \{ U _ { s } ( n , v ) , 0 \}$ . The consumer skips the content piece if $U _ { s } ( n , v ) >$ max $\{ U _ { e } ( n , v ) , 0 \}$ . The consumer exits the platform if max $\{ U _ { e } ( n , v ) , U _ { s } ( n , v ) \} < 0$ . After viewing a content piece, the consumer enters decision point 2, which we discuss later.

3.3.2. Decision Point 2. After viewing N<sup>∗</sup> content pieces, the consumer decides whether to exit the platform or to stay on the platform and view an nth $( n = \bar { N } ^ { * } + 1 )$ piece. If choosing to stay, the consumer will go back to the inspection step and then enter decision point 1 again, as shown in Figure 1. Before making the decision, the consumer evaluates the expected utility from staying,

which is given by

$$
U ^ {s t a y} (n) = E _ {V} [ m a x \{0, U _ {e} (n, V), U _ {s} (n, V) \} ] - c.\tag{3}
$$

In Equation (3), the second term c gives the consumer’s expected cost from going through the inspection step again. The consumer expects to inspect another randomly selected content piece from the feeds and obtain its unit match value as another realization of the random variable V.

The first term of Equation (3) gives the consumer’s expected surplus from going through decision point 1 again. Note that at the time of forming $\boldsymbol { U } ^ { s t a y } ,$ the consumer is uncertain about the realization of $V$ and so takes expectation of this surplus across all realizations of V. With any specific realization of $V ,$ the consumer anticipates three possible actions and chooses the one that generates the maximum surplus. The utility of the three actions constitutes the three components in the max function: zero surplus if exiting the platform, $U _ { e } ( n , V )$ if viewing the inspected piece with unit match value $V ,$ and $U _ { s } ( n , V )$ if skipping the inspected piece.

The consumer stays on the platform if and only if $U ^ { s t a y } ( n ) > 0$ . When this happens, the consumer goes back to the inspection step and then goes through the process discussed in Sections 3.3.1 and 3.3.2 again. Whether a consumer will visit the platform is also a decision based on Equation (3). In particular, a consumer visits the platform if and only if ${ { U } ^ { s t a y } } ( n = 1 ) > 0$

## 3.4. Game Sequence

In any strategic phase, the game proceeds in two stages. First, the platform decides content length limit T. Then, consumers decide whether to visit the platform and if visiting, which content pieces to view.

## 4. Analysis and Results

We solve the model through backward induction by first examining consumer decisions and then solving for optimal platform policies. All proofs are in the appendix.

## 4.1. Consumer Decisions

Here we first examine a consumer’s optimal action at decision points 1 and 2, respectively, upon visiting the platform. We then solve for the consumer’s optimal action regarding whether to visit the platform.

4.1.1. Decision Point 1: Viewing or Skipping a Content Piece. At this decision point, a consumer decides whether to view the content piece just inspected with known match value v, to skip it and inspect another content piece, or to exit the platform. We obtain the following lemma.

Lemma 1. When a consumer enters decision point 1, (i) the expected utility from exiting the platform is dominated by the utilities from skipping or from viewing a content piece; and (ii) the consumer’s expected maximum utility $U _ { s } ( n , v )$ from skipping can be reduced to

$$
U _ {s} (n, v) = E _ {V} \big [ U _ {e} (n, \max \{v, V \}) \big ] - c.
$$

Lemma 1(i) indicates that the option of exiting the platform is always dominated. This is because a consumer who enters this decision point has already rationally anticipated a nonnegative surplus from viewing an additional content piece. In particular, if the consumer has just arrived at the platform and entered decision point 1 for the first time, the consumer has anticipated $\hat { U } ^ { s t a y } ( 1 ) > 0$ . If the consumer has already viewed $N ^ { \ast } \in$ $\{ 1 , 2 , \ldots \}$ content pieces on the platform, the consumer has been through decision point 2 and evaluated ${ \cal U } ^ { s t a y } ( n ) > 0 .$ , with $n = N ^ { * } + 1$ . From Equations (1) and (3), it is easy to prove $U _ { s } ( n , v ) \geq U ^ { s t a y } ( n \bar { ) } > 0$

Lemma 1(ii) indicates that a consumer’s maximum ex ante expected utility from skipping is the expected utility from skipping only once. Intuitively, skipping more times adds more inspection cost, but will not increase the expected value from viewing because the unit match value of any new content piece is another random draw of V from the same distribution. We then rewrite the consumer’s expected maximum utility from skipping a content piece defined in Equation (2) as

$$
\begin{array}{l} U _ {s} (n, v) = E _ {V} [ U _ {e} (n, m a x \{v, V \}) ] - c \\ \qquad = \int_ {v _ {0} - \sigma} ^ {v _ {0} + \sigma} (\max \{v, V \} \cdot T) d F (V) - \delta T ^ {2} (2 n - 1) - c. \end{array}\tag{4}
$$

By skipping, a consumer anticipates going back to the inspection step, incurring an inspection cost $c ,$ and then viewing a content piece. The first term of Equation (4) gives the consumer’s expected enjoyment from viewing. If the newly inspected content piece has a unit match value than the previously inspected one $( \mathrm { i . e . , } V < v )$ , the consumer will go back to view the old content piece through free recall, and otherwise $( \mathrm { i . e . , } V > v )$ , the consumer will view the newly inspected content piece. The second term gives the consumer’s time cost of viewing.

Lemma 1 suggests that the consumer will exit decision point 1 if and only if the consumer finds the nth content piece to view in the sequential process of content inspection. We proceed to solve for the consumer’s decision rule about which content piece to view. Given match value v of the inspected content piece, a consumer’s expected maximum benefit from skipping the content, compared with viewing the content, can be derived as $\begin{array} { r } { U _ { s } - U _ { e } = T \frac { ( v _ { 0 } + \sigma - v ) ^ { 2 } } { 4 \sigma } - c , } \end{array}$ which strictly decreases with v. That is, if there exists $v ^ { * } \in \left[ v _ { 0 } - \sigma , v _ { 0 } + \sigma \right]$ that satisfies $U _ { s } - U _ { e } = 0 .$ , then $U _ { s } - U _ { e } > 0$ for any $v < v ^ { * }$ and $U _ { s } -$ $U _ { e } < 0$ for any $v > v ^ { * }$ . A consumer’s optimal rule for content search can thus be stated as: Skipping the inspected content if the match value is lower than the reservation match value, that is, $v < v ^ { * }$ , terminating search and viewing the inspected content if $v > v ^ { * }$ , and taking either action if $v = v ^ { * }$ . In a symmetric Nash equilibrium, a consumer draws from the same distribution of match value each time a content piece is inspected. In this circumstance, the consumer’s stopping rule is independent of how many content pieces had been skipped or how many content pieces are left to search. This is in the same spirit of classical search models (Kohn and Shavell 1974, Stahl 1989), where the stopping rule does not depend on how many stores a consumer has searched or how many are left to search. We obtain the following lemma.

Lemma 2 (Consumer Content Viewing Decision). A consumer views a content piece with known match value v if this value meets the reservation match value $v ^ { * }$ , that is, if

$$
v \geq v ^ {*} = v _ {0} + \sigma - 2 \sqrt {\frac {c \sigma}{T}}.\tag{5}
$$

In Equation (5), $v ^ { * }$ defines the lowest match value of a content piece that the consumer is willing to view. In making decisions about whether to skip the current piece with known match value v, the consumer evaluates the benefit of skipping (i.e., the expected value $\begin{array} { r } { \int _ { v } ^ { v _ { 0 } + \sigma } ( V T ) f ( V ) d V } \end{array}$ from viewing the next content piece with $V > v )$ and the cost of skipping (i.e., inspection cost c). A shorter content length reduces the benefit of skipping and so motivates the consumer to view content with lower match values, that $\mathrm { i s } , \frac { \partial v ^ { * } } { \partial T } > 0$ . Note that $v ^ { * }$ is independent of n or $\delta ,$ , parameters that affect a consumer’s viewing cost. This is because $v ^ { * }$ characterizes decision point 1 at which the consumer decides which content piece to view (but not whether to view). The consumer will always incur the same viewing cost no matter which piece the consumer finally views.

When $v ^ { * }$ is larger, a consumer is less likely to view a content piece that has been inspected. In other words, $v ^ { * }$ negatively indicates the click-through rate of a content piece after it has been inspected. We derive the clickthrough rate CTR as the probability of $v > v ^ { * }$ and obtain

$$
C T R = \min \left(1, \frac {v _ {0} + \sigma - v ^ {*}}{2 \sigma}\right) = \min \left(1, \sqrt {\frac {c}{\sigma T}}\right).\tag{6}
$$

We illustrate in Figure 2 how the reservation match value $v ^ { * }$ and the content click-through rate CTR vary with T in opposite directions and obtain the following proposition.<sup>4</sup>

Proposition 1 (Content Length Affects Content Click-Through Rate). Consumers are more likely to view a content piece that they have inspected when the media platform sets a shorter content length limit. That is, $\begin{array} { r } { \frac { \partial C T R } { \partial T } < \dot { 0 } . } \end{array}$

Proposition 1 is interesting because it shows how the attractiveness of contributed content in inducing “views” or “clicks” depends on the design of the platform, in particular, the content length limit. Our result suggests that platforms with a strict limit on video length such as TikTok are likely to generate a higher click-through rate for contributed content compared with platforms such as YouTube that implement a loose video length limit. In practice, people have noticed that short videos usually tend to have higher click-through rates (Delfino 2019, Yeshanew 2021).

Figure 2. (Color online) Impact of Content Length Limit T on Reservation Unit Match Value $v ^ { * }$ and Click-Through Rate CTR $( v _ { 0 } = 2 , \sigma = 1 , c = 0 . 2 , \underline { { \delta } } = 1 , \overline { { \delta } } = 1 0 0 )$  
![](/api/attachments/67CKJE7T/fulltext/images/5635a18a2217a16e4c798003da0250827a1df8f042845521e3dbac703dc6a9df.jpg)

To understand the intuition behind Proposition 1, viewing the current content piece brings the consumer a total match value of vT but deprives the consumer of the chance of viewing a different content piece, which may have a higher total match value. The option of viewing thus involves an opportunity cost, which increases with the content length T. On the other hand, skipping the current content piece involves a cost c for inspecting unit match value that is independent of content length. A consumer decides whether to view the content piece by evaluating the opportunity cost of viewing versus the inspection cost of skipping. Shorter content (i.e., a small T) motivate consumers to take the small opportunity cost of viewing and so increases the click-through rate, whereas longer content (i.e., a larger T) motivates consumers to take the inspection cost of skipping and so reduces the click-through rate.

4.1.2. Decision Point 2: Exiting or Staying on the Platform. At decision point 2, a consumer evaluates the expected utility from staying on the platform $U ^ { s t a y } ( n )$ where $n = N ^ { * } + 1$ and $N ^ { * }$ is the number of content pieces that the consumer has already viewed. The consumer stays on the platform if and only if $U ^ { s t a y } ( n ) > 0$

A consumer anticipates to go back to the inspection step and then enter decision point 1 again if staying on the platform. Recall that Lemma 1 indicates a consumer will not exit decision point 1 until after viewing a content piece. We then rewrite the consumer’s expected utility of staying on the platform $U ^ { s t a y } ( n )$ specified in Equation (3) in a recursive format as

$$
\begin{array}{l} U ^ {S t a y} (n) = \int_ {v ^ {*}} ^ {v _ {0} + \sigma} U _ {e} (n, V) f (V) d V \\ \qquad + \int_ {v _ {0} - \sigma} ^ {v ^ {*}} U ^ {S t a y} (n) f (V) d V - c. \end{array}\tag{7}
$$

The last term of Equation (7) represents the inspection cost the consumer anticipates to incur by going through the inspection step again. The first two terms represent the consumer’s expected surplus from two possible actions at decision point 1. If the inspection reveals a unit match value that exceeds reservation unit match value $v ^ { * }$ the consumer will view the content piece and obtain a utility of $U _ { e } ( n , V )$ . Otherwise, the consumer will skip the content piece and keep staying on the platform, which renders $\bar { U } ^ { s t a y } ( n )$ . We rearrange this equation and obtain

$$
\begin{array}{c} U ^ {s t a y} (n) = T \bigg (\sigma + v _ {0} - 2 \sqrt {\frac {c \sigma}{T}} \bigg) - T ^ {2} \delta (2 n - 1) \\ = v ^ {*} T - \delta T ^ {2} (2 n - 1). \end{array}\tag{8}
$$

Note that $U ^ { s t a y } ( n )$ is positively associated with reservation unit match value $v ^ { * }$ . This is because with a higher $v ^ { * }$ the consumer anticipates viewing a higher-valued content piece. Also, $U ^ { s t \hat { a y } } ( n ) > 0$ can be satisfied as long as n is not too large. Intuitively, every time the consumer enters decision point 2 again, the expected marginal benefit from staying on the platform and viewing an additional content piece shrinks; that is, $U ^ { s t a y } ( n )$ decreases with n. Moreover, $U ^ { s t a y } ( n )$ decreases with $\delta ,$ indicating that a consumer with higher content viewing cost $\delta$ is less likely to stay.

Understanding decision point 2 allows us to examine a consumer’s decision to visit the platform and the number of content pieces the consumer expects to view on the platform. In particular, a consumer enters decision point 2 every time after viewing a content piece. The total number of content pieces that a consumer expects to view on the platform thus depends on how many times the consumer expects to evaluate ${ \cal U } ^ { s t a y } > 0$ at decision point 2. We denote this number as $N ^ { * }$ , which satisfies $\hat { U } ^ { s t a y } ( N ^ { * } ) > 0$ and $U ^ { s t a y } ( N ^ { * } + 1 ) < 0 . \mathrm { A }$ rational consumer will visit the platform only if $N ^ { * } \geq 1$ , or equivalently $U ^ { s t a y } ( 1 ) > 0 ,$ , which condition is satisfied when the consu mer’s time cost is sufficiently small. We obtain the following lemma.

Lemma 3. A consumer visits the platform if and only if the time cost is not too $h i g h ,$

$$
\delta <   \delta^ {*} = \frac {v _ {0} + \sigma - 2 \sqrt {\frac {c \sigma}{T}}}{T} = \frac {v ^ {*}}{T}.\tag{9}
$$

Upon visiting the platform, the number of content pieces that the consumer views is

$$
N ^ {*} (\delta) = \left\lfloor \frac {\delta T + \left(\sigma + v _ {0} - 2 \sqrt {\frac {c \sigma}{T}}\right)}{2 \delta T} \right\rfloor = \left\lfloor \frac {1}{2} + \frac {\delta^ {*}}{2 \delta} \right\rfloor .\tag{10}
$$

In Equation (9), $\delta ^ { * }$ defines the highest time cost that allows a consumer to visit the platform, which can be written as a function of the reservation match value $v ^ { * }$ and the content length T. Also, Equation (10) suggests that $N ^ { * }$ is a linear transformation of $\delta ^ { * }$ . It is easy to see that as long as δ is sufficiently small, there always exists a portion of customers with time cost between $[ \underline { { \delta } } , \delta ^ { * } ]$ who will visit the platform. Directly from the lemma, we obtain how the content length limit affects consumers’ content viewing behaviors on a C2C media platform.

Proposition 2 (Content Length Limit Affects Consumer Viewing). When content length limit T increases, a consumer’s incentive to visit the platform first increases and then decreases. Moreover, upon visiting the platform, the total number of content pieces a consumer views first increases and then decreases. That $\begin{array} { r } { i s , \frac { \partial \delta ^ { * } } { \partial T } > 0 \ \& \frac { \partial N ^ { * } } { \partial T } > 0 f o r \ T < T _ { N } = \frac { 9 c \sigma } { \left( \sigma + v _ { 0 } \right) ^ { 2 } } , } \end{array}$ and $\begin{array} { r } { \frac { \partial \delta ^ { * } } { \partial T } < 0 \& \frac { \partial N ^ { * } } { \partial T } < 0 f o r T > T ^ { N } . } \end{array}$

Proposition 2 shows an interesting nonlinear impact of content length limit T on consumers’ viewing behaviors on a C2C platform. When content are longer (i.e., a larger $T ) .$ , a consumer sets a higher reservation match value $v ^ { * }$ and therefore expects a higher enjoyment from staying on the platform. This positive impact motivates the consumer to visit the platform and view more content pieces. On the other hand, longer content adds to the time cost of viewing, which increases with content length at an accelerating rate. This negative impact discourages the consumer from visiting the platform and viewing more content. The first, positive impact on the enjoyment of viewing dominates when content are relatively short, whereas the second, negative impact on the time cost of viewing dominates when content become sufficiently long.

Interestingly, this result suggests the existence of an optimal content length that motivates consumers’ content viewing on a C2C media platform. Previous research has demonstrated that when consumers are required to view, an optimal content length exists that maximizes the effectiveness of content understanding and recall (Slemmons et al. 2018, Manasrah et al. 2021). Our finding complements this research by showing that when consumers can decide whether to view, an optimal content length exists that maximizes the chance that consumers will view content.

## 4.2. Platform Decision

In a strategic phase, the platform sets content length limit to maximize its market performance. Here we first introduce three key measures of platform performance and then investigate the platform’s optimal strategy.

4.2.1. Measuring Platform Performance. We introduce three measures of the platform’s consumer market performance. First, we measure “viewer traffic,” or the total number of consumers who visit the platform. This measure is analogous to the size of viewer “demand” for the platform, and can be derived as

$$
D = \int_ {\underline {{\delta}}} ^ {\delta^ {*}} d F (\delta) = \frac {\delta^ {*} - \underline {{\delta}}}{\overline {{\delta}} - \underline {{\delta}}}.\tag{11}
$$

Viewer traffic indicates the platform’s visibility and can be positively associated with the platform’s advertising revenue. As shown previously, this measure is a linear transformation of $\delta ^ { * }$ , the highest time cost coefficient for a consumer to visit the platform, and therefore varies with content length limit T in the same pattern. We illustrate this insight in Figure 3.

Second, we measure “total viewing time” that all consumers spend on the platform. This measure is analogous to the total volume of content “sales” on the platform and can be obtained by adding up $T \cdot N ^ { \ast } ( \delta )$ for all consumers with $N ^ { * } ( \delta ) > 0$ , or all with $\delta < \delta ^ { * }$

$$
M = T \int_ {\underline {{\delta}}} ^ {\delta^ {*}} N ^ {*} (\delta) d F (\delta) = T \int_ {\underline {{\delta}}} ^ {\delta^ {*}} \left(\frac {1}{2} + \frac {\delta^ {*}}{2 \delta}\right) d F (\delta).\tag{12}
$$

Higher total viewing time indicates greater potential for the platform to generate revenue from contributed content. The total number of content views on the platform, $\begin{array} { r } { T N = \int _ { \delta } ^ { \delta ^ { * } } N ^ { * } ( \delta ) d F ( \delta ) } \end{array}$ , is positively associated with $\delta ^ { * } ,$ , and so positively associated with viewer traffic. Intuitively, more content views are generated when more viewers join the platform.

Third, we measure “total consumer surplus” that all consumers obtain from viewing content on the platform. For an individual consumer with time cost $\delta ,$ the surplus from viewing $n = 1 , 2 , \ldots , N ^ { * } ( \delta )$ th piece is $U ^ { s t a y } ( n )$ . We derive total consumer surplus as

Figure 3. (Color online) Impact of T on $\delta ^ { * }$ and D (v � 2, σ � 1, c � 0:2, δ � 1, δ � 100)  
![](/api/attachments/67CKJE7T/fulltext/images/0c2f4ea180b26866e1d3fba36f6e134a65a89b68042c5f922d4a13a6230b9516.jpg)  
Note. D is rescaled by multiplying 100.

$$
S = \int_ {\underline {{\delta}}} ^ {\delta^ {*}} \left(\sum_ {n = 1} ^ {N ^ {*} (\delta)} U ^ {s t a y} (n)\right) d F (\delta) = T ^ {2} \int_ {\underline {{\delta}}} ^ {\delta^ {*}} N ^ {*} (\delta) (\delta^ {*} - \delta) d F (\delta),\tag{13}
$$

which is also positively associated with $\delta ^ { * }$ . Higher consumer surplus is likely to produce greater viewer satisfaction from visiting the platform, which can have benefits of enhancing customer retention (Bearden and Teel 1983, Bolton and Drew 1991), word of mouth (Fornell 1992), and future revenue (Anderson et al. 2004, Aksoy et al. 2008). Positive changes in satisfaction have also been shown to promote faster market penetration such as faster trials, referrals, and adoptions (Srivastava et al. 1998) and enhance stock market performance (Luo et al. 2010).

The following proposition summarizes how content length limit affects the three key measures.

Proposition 3 (Content Length Limit Affects Platform Performance). In a given strategic phase, viewer traffic, total viewing time, and total consumer surplus on the platform all vary with expanded content length limit following an inverted U-shaped curve, and reach their maximum at $T ^ { D * } , T ^ { M * }$ , and $T ^ { S * }$ , respectively. Furthermore, $T ^ { D * } = T ^ { N } =$ $\begin{array} { r } { \frac { 9 c \sigma } { ( \sigma + v _ { 0 } ) ^ { 2 } } , } \end{array}$ , and $T ^ { D * } < T ^ { M * } < T ^ { S * }$

Figure 4 illustrates the different varying patterns of the three platform performance measures with respect to content length limit. Proposition 3 has several findings that are worth noting. First, content length limit has nonlinear impacts on all three key measures of consumer market performance. This result is driven by the nonlinear impact of T on $\delta ^ { * }$ as shown in Proposition 2. A moderate content length limit is required for a platform to maximize viewer traffic, total viewing time, or total consumer surplus. Content too short or too long are not desirable for the platform. Second, total viewing time on the platform reaches the maximum at a larger content length limit than viewer traffic, that is, $T ^ { M * } > \overline { { T } } ^ { D * }$ <sup>∗</sup>. This is because whereas the total number of content pieces being viewed is perfectly correlated with the viewer traffic, longer content extends the duration for viewing each content piece. As such, total viewing time continues to increase even when the total viewer traffic starts to decline from the maximum. Third, total consumer surplus keeps increasing with content length limit and reaches the maximum at $T ^ { S * } > T ^ { M * }$ . This is because longer content enhances $v ^ { * }$ and so the enjoyment level of each content piece the consumer views, in addition to extending consumers’ duration of enjoyment from viewing each content piece. With this additional benefit, total consumer surplus keeps increasing with content length, even when consumer traffic or total viewing time are lower than optimal.

Figure 4. (Color online) Impact of T on Viewer Traffic (D), Total Viewing Time (M), and Total Consumer Surplus (S) $\left( v _ { 0 } = 1 , \sigma = 0 . 8 , c = 0 . 1 , \underline { { \delta } } = 1 , \overline { { \delta } } = 1 0 0 , T ^ { D * } = 0 . 1 6 , T ^ { M * } = 0 . 4 1 , T ^ { S * } = 0 . 4 4 \right)$  
![](/api/attachments/67CKJE7T/fulltext/images/fe3f3ce22d9c11acd753fd3e7e591de9cf37bfd8542bdf836f34a22ce1c4159e.jpg)  
Note. D, M, and S are rescaled by multiplying 100.

Last, it is interesting to contrast the nonlinear impact of content length limit on the three key measures of platform performance with its negative influence on the click-through rate as illustrated in Figure 2. This contrast suggests that a platform’s effort to attract viewer traffic, increase content viewing time, or enhance consumer experience through extending content length limit may cause a decline in content click-through rate. Although the reduced click-through rate may worry contributors and advertisers, our study suggests that the loss will be compensated by increased viewer traffic to the platform, viewers’ extended length of stay, and enhanced viewer experience.

4.2.2. Platform Optimal Policy. In a single strategic phase, a platform’s objective function can be a weighted combination of viewer traffic T, total viewing time M, or total consumer surplus S. We consider the simplified case where the platform put all the weights on one performance measure. In this case, the platform’s optimal policy for content length limit can be derived as $T ^ { M * } , T ^ { D * } , \mathbf { o r } T ^ { S * }$ respectively.

Across strategic phases, the platform’s performance goal may change, causing a switch in its strategy. For example, a startup platform may focus more on securing a successful entry and set the policy to maximize viewer traffic and platform visibility. After the platform has established a customer base, it may switch the focus to generating revenue from content and adjust the policy to maximize total viewing time. Later, when survival is not a concern, the platform may switch the focus to building brand reputation for long-term growth and strengthening stock market performance. In this case, the platform may adjust its policy to maximize consumer surplus. We consider these two cases of platform goal switching and obtain the following proposition.

Proposition 4 (Optimal Policy for Content Length Limit). (i) When the platform switches its goal from maximizing viewer traffic to maximizing total viewing time, it extends the limit for content length from $T ^ { D * }$ to $\breve { T } ^ { M * }$ . (ii) When the platform switches its goal from maximizing total viewing time to maximizing total consumer surplus, it extends the limit for content length from $T ^ { M * }$ to $T ^ { S * }$

The intuition behind Proposition 4 can be traced back to the multifaceted impacts of content length limit $T$ on consumers’ content selecting and viewing behaviors. Consider a platform that sets optimal content length limit $T ^ { D * }$ that maximizes its viewer traffic. Note that $\stackrel { \cup } { T } ^ { D * }$ also maximizes the total number of content pieces that a consumer views on the platform. When the platform loosens the limit and allows contributors to post longer content, viewing an additional content piece becomes more costly. As such, consumers are more likely to find it too costly to view an additional content piece, compared with the outside option. Nonetheless, with increased content viewing cost, consumers become more careful in selecting the right piece to view (i.e., $v ^ { * }$ increases with T) and end up viewing content pieces with higher unit match values. This second, positive impact mitigates the first, negative impact, leading to increased total consumer viewing time until the content length limit reaches $T ^ { M * }$ . Interestingly, consumers experience a double boost in their surplus of viewing a longer content piece, from both the increased unit match value v and the extended content length T. This impact mitigates the first, negative impact even further, enabling total consumer surplus to keep increasing until the content limit reaches $T ^ { S * }$

Although our result is derived from the simplified case when the platform maximizes a single market performance measure, our insights continue to hold in the general case where the platform maximizes a weighted sum of the three market performance measures. For example, if in the second strategic phase the platform puts more weight on consumer surplus, it will extend the limit of content length. In a given strategic phase, higher viewer traffic and more total viewing time bring immediate revenue benefits. Higher total consumer surplus, on the other hand, benefits the platform in the long run by enhancing customer satisfaction and platform reputation. Our result thus suggests a platform that switches strategic focus from enhancing current revenue to fostering future growth can benefit from extending its content length limit. Our theoretical insight may provide a possible explanation for TikTok’s early success with its 15-second cap on content length and for its later extension of this limit.

## 5. Extension

## 5.1. Strategic Contributors

In the main model, we abstract out contributors’ decisions to post content. In this model extension, we consider contributor decisions and demonstrate the robustness of our key results. We assume a number $H ( H > 0 )$ of contributors, who decide whether to post a content piece on the platform in each strategic phase. We consider the case when H is very large so that in equilibrium a large number of contributors post. This assumption reflects the business reality in a C2C media platform such as TikToK where anybody with a smartphone can post content. We assume that all content pieces have the same distribution of unit match values among the consumer population. Following the main model, we assume all contributors post a content piece with length T. A contributor collects payoff $\rho ( \rho > 0 )$ from each view of its content piece. For example, a TikTok contributor earns roughly 4 cents for every 1,000 views a video received (Matsakis 2020). A contributor incurs a substantial fixed cost $g ( g > 0 )$ ) to create a content piece, which entails all time and effort the contributor incurs, including selecting the topic, conducting research, planning shooting, and so on. The fixed production cost varies across contributors with different expertise and creativity. We assume that g follows a uniform distribution on interval $( 0 , { \overline { { g } } } ] \ ( { \overline { { g } } } > 0 )$ ) across contributors. The marginal production cost on content length is trivial compared with this fixed cost and is normalized to zero.

A contributor posts a content piece if the expected revenue from content viewing is sufficient to cover the production cost. We assume tha $\overline { { g } }$ is sufficiently high so that a contributor of marginal type $g ^ { * } \in ( 0 , \overline { { g } } ]$ exists who is indifferent between posting and not posting. The contributor traffic can thus be derived as $\begin{array} { r } { R \equiv \frac { g ^ { * } } { \overline { { g } } } H } \end{array}$ . We derive contributors’ content posting behaviors as an equilibrium where each contributor decides whether to post based on the belief about other contributors’ behaviors and each contributor’s utility-maximizing behavior is consistent with others’ beliefs. The following lemma characterizes the equilibrium posting behaviors of contributors.

Lemma 4 (Contributor Traffic). In a given strategic phase, the total number of contributors who post on the platform i $\begin{array} { r } { R = \frac { g ^ { * } } { \overline { { g } } } H } \end{array}$ , where $g ^ { * } \in ( 0 , \overline { { g } } ]$ can be solved from

$$
(g ^ {*}) ^ {2} = \frac {\rho \overline {{g}}}{H} \int_ {\underline {{\delta}}} ^ {\delta^ {*}} N ^ {*} (\delta) d F (\delta).\tag{14}
$$

In the right-hand side of Equation (14), $\delta ^ { * }$ and $N ^ { * } ( \delta )$ are both functions of content length limit T. We obtain the following proposition, which summarizes how content length limit T affects contributor traffic R.

Proposition 5 (Content Length Limit Affects Contributor Traffic). When content length limit T increases, contributo traffic first increases and then decreases.

The nonmonotonic impact of content length limit on contributor traffic shows a familiar pattern as we have seen in Proposition 2 on viewer traffic D. This is because when contributors anticipate greater viewer traffic $( \mathrm { i . e . , }$ a larger $\delta ^ { * } ,$ , which is equivalent to a larger D), such anticipation also suggests more content views $\mathrm { ( i . e . , ~ } N ^ { \ast } ( \delta )$ increase with $\delta ^ { * } )$ , both leading to contributors’ stronger incentive to post content. When $\delta ^ { * }$ reaches the maximum at $T ^ { D * }$ , both consumer traffic D and contributor traffic R are maximized. We illustrate this insight in Figure 5. In particular, we solve for $g ^ { * }$ that satisfies Equation (14) at various values of $T$ and illustrate corresponding contributor traffic $R ( g ^ { * } )$ and consumer traffic $\bar { D } ( g ^ { * } )$ . As can be seen, the two traffic measures reach the maximum simultaneously at intermediate T. This discussion also suggests a network effect between the two sides of the C2C media platform, which we summarize in the following corollary.

Corollary 1 (Network Effect). In equilibrium, contributor traffic R is positively associated with viewer traffic D.

Corollary 1 suggests that more contributors will join the platform when anticipating more consumer traffic. This network effect echos the findings of Hagiu (2009), Anderson et al. (2014), and Dou and Wu (2021) in different platform contexts. On the other hand, given that a large number of contributors post content and the platform customizes content feeds for each individual consumer, consumers’ decisions as specified in the main model regarding which content piece to view (i.e., decision point 1) and whether to exit the platform (i.e., decision point 2) do not depend on contributor traffic R. Therefore, all our main model results continue to hold.

## 5.2. Robustness of Main Model Results

Here we demonstrate the robustness of our main model results in various model extensions.

5.2.1. Varied Length of Contributed Content. In the main model, we assume that all contributors post content of maximum length T. Now we demonstrate the robustness of our results in an extended model where contributors can post content pieces shorter than T. We assume that across contributors the length t of content pieces follows a distribution on (0, T], with mean<sub>fififififififiq</sub> $t _ { e } \equiv$ E[t] and gyradius $\begin{array} { r } { r \equiv \sqrt { \frac { E [ t ^ { 2 } ] } { E [ t ] } } } \end{array}$ . The main model can thus be viewed as a special case where $t _ { e } = r ^ { 2 } = T$ . This distribution of t is common knowledge. We assume that on average contributors generate longer content when content length limit is extended, that is, $t _ { e }$ increases with T. We also assume that the variance in the length of contributed content is not too large such that r also increases with T. These assumptions receive support from business practice. For example, a recent study shows that after TikTok has extended the length limit from 15 to 60seconds, the average length of the top 100 clips is 16seconds, and 80% of them have lengths between 10 and 20seconds (Slee 2020). Other specifications of the main model apply.

Figure 5. (Color online) Impact of T on Contributor Traffic R and Consumer Traffic D $( v _ { 0 } = 1 , \sigma = 1 , c = 0 . 0 5 , \overline { { g } } = 1 0 ,$ H � 100)  
![](/api/attachments/67CKJE7T/fulltext/images/5d15a1155d9a2eb8512464515e8913fc27d37dc2ccfd498fbcdcb0cf686891eb.jpg)  
Note. R and D are normalized using the min-max approach to show their evolution trend

We let $t _ { 1 } , \dots t _ { n }$ denote independent and identically distributed random variables that represent the lengths of the $\mathrm { f i r s t } , \ldots ,$ , nth content pieces that a consumer views. At decision point 1, a consumer’s expected utility from viewing an inspected content piece with unit match value v as the nth piece viewed on the platform is

$$
\begin{array}{r} U _ {e} (n, v) = v E [ t _ {n} ] - \delta (E [ (t _ {1} + \dots + t _ {n}) ^ {2} ] \\ - E [ (t _ {1} + \dots + t _ {n - 1}) ^ {2} ]) = v t _ {e} - \delta (2 n - 1) t _ {e} r ^ {2}. \end{array}\tag{15}
$$

The consumer’s expected utility from skipping this content piece can be derived as

$$
U _ {s} (n, v) = t _ {e} \int_ {v _ {0} - \sigma} ^ {v _ {0} + \sigma} \max \{v, V \} d F (V) - \delta (2 n - 1) t _ {e} r ^ {2} - c.\tag{16}
$$

Comparing Equations (15) and (16), we obtain that the consumer will view the content piece if $v \geq v ^ { * } =$ v<sub>0</sub> + $\begin{array} { r } { \sigma - 2 \sqrt { \frac { c \sigma } { t _ { e } } } . } \end{array}$ . Given that $t _ { e }$ is monotonically increasing with $T ,$ the positive impact of T on $v ^ { * }$ that we discuss in the main model continues to hold and so Proposition 1 continues to hold. At decision point 2, the consumer’s expected utility from staying on the platform to view the nth content piece is $\begin{array} { r } { U ^ { s t a y } ( n ) = t _ { e } \bigg ( \sigma + v _ { 0 } - 2 \sqrt { \frac { c \sigma } { t _ { e } } } \bigg ) - } \end{array}$ $\delta ( 2 n - 1 ) t _ { e } r ^ { 2 } = t _ { e } v ^ { * } - \delta ( 2 n - 1 ) t _ { e } r ^ { 2 }$ . The total number of content pieces a consumer with time cost coefficient δ views on the platform can be derived as $N ^ { * } ( \delta ) =$ $\lfloor \frac { 1 } { 2 } + \frac { v ^ { * } } { 2 \delta r ^ { 2 } } \rfloor$ . A consumer will visit the platform if the consumer’s time cost coefficient $\delta$ is sufficiently small, $\begin{array} { r } { \delta < \delta ^ { * } = \frac { v ^ { * } } { r ^ { 2 } } , } \end{array}$ so that $N ^ { * } ( \delta ) \geq 1$ . Given $T ,$ the viewer traffic is $\begin{array} { r } { D = \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } d F ( \delta ) = \frac { \delta ^ { * } - \underline { { \delta } } } { \delta - \delta } , } \end{array}$ consumers’ total viewing time is $\begin{array} { r } { M = t _ { e } \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } N ^ { * } ( \delta ) d F ( \delta ) = t _ { e } \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } \big ( \frac { 1 } { 2 } + \frac { \delta ^ { * } } { 2 \delta } \big ) d F ( \delta ) } \end{array}$ , and the total consumer surplus is $\begin{array} { r } { S = \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } s ( \delta ) d F ( \delta ) = t _ { e } r ^ { 2 } \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } N ^ { * } ( \delta ) } \end{array}$ $( \delta ^ { * } - \delta ) d F ( \delta )$ . Given that $t _ { e }$ and r both increase with $T ,$ the impacts of $T$ on D, M, and S as specified in Proposition 3 continue to hold. It is straightforward that other results in the main model retain qualitatively.

5.2.2. General Function of Content Viewing Cost. In the main model, we assume a specific functional format for the viewing cost. Essentially, our assumption ensures diminishing returns of viewing an additional content piece so that consumers will stop watching at a point. This notion of diminishing returns from repeated experiences or satiation is documented in various laboratory studies (Redden 2008). Our key results will continue to hold with a general function $\delta \cdot K ( T , n )$ for a consumer of type δ viewing the nth content piece, as long as $\begin{array} { r } { \frac { \partial K ( T , n ) } { \partial n } > 0 , \frac { \partial K ( T , n ) } { \partial T } > 0 , } \end{array}$ and $\frac { \partial ^ { 2 } K ( T , n ) } { \partial T ^ { 2 } } > 0$ are satisfied. In particular, the first condition indicates that the consumer viewing cost increases in n and the other two conditions ensure that consumer viewing cost increases in T with an increasing speed. An example of such a general function is $K ( T , n ) { \stackrel { - } { = } } { \bar { n } } \cdot T ^ { a } , a > 1$ , which suggests the content viewing cost increases with content length at a faster speed than total match value vT. We show that under this specification, the results regarding consumer decision point 1 $( \mathrm { i } . \mathrm { e } . , v ^ { * } )$ remain unchanged and the results regarding consumer decision point 2 show the same properties as in the main model. All key results in the main model continue to hold qualitatively. For instance, given $v _ { 0 } = 2 , \sigma =$ $1 , \ c = 0 . 2 , \overline { { \delta } } = 1 0 0 , \underline { { \delta } } = 1 , a = 1 . 4$ , we solve for $T ^ { D * } = 0 . 4 5 ,$ $T ^ { M * } = 3 . 4 _ { \AA }$ , and $T ^ { S * } = 3 . 6$ , which demonstrates $T ^ { D * } <$ $T ^ { M * } < T ^ { S * }$ and therefore is consistent with Proposition 3.

5.2.3. General Function of Inspection Cost. In the main model, we assume that the inspection cost c to reveal the unit match value of a content piece is independent of content length. Our key results will continue to hold qualitatively under a general inspection cost function C(T) as long as $0 \leq C ^ { \prime } ( \bar { T } ) < C ( T ) / \bar { T }$ is satisfied so that $v ^ { * }$ as shown in Equation (5) increases with T. An example of such a general function is $C ( T ) = c \cdot T ^ { b } ,$ $0 < b < 1$ , which suggests the inspection cost to learn the unit match value of a content piece increases with the content length at a lower speed compared with total match value $v \breve { T } .$ . In this specification, $b = 1$ means that a consumer inspects every moment of the content piece to learn its unit match value v, making cT the highest possible inspection cost. In our research context of short videos, $0 < b < 1$ is a reasonable restriction because standard information of a content piece (e.g., who posted the content, its genre, the number of views and likes) is independent of its length and the video quality is relatively consistent throughout. Given $v _ { 0 } = 2 , \sigma = 1 .$ $c = 0 . 2 , \overline { { \delta } } \overset { \cdot } { = } 1 0 0 , \underline { { \delta } } = 1 , b = 0 . 2 ,$ , we solve for $T ^ { D * } = 0 . 1 2 ,$

$T ^ { M * } = 0 . 3 5 ,$ , and $T ^ { S * } = 0 . 3 8$ , which demonstrates $T ^ { D * } <$ $T ^ { M * } < T ^ { S * }$ and consistence with Proposition 3.

5.2.4. Imperfect Inspection. In the main model, we assume that consumers learn the true match value of a content piece after inspection. Our key insights continue to hold when the inspection is not fully accurate. To see this, assume that a consumer’s inspection renders the true unit match value v with probability w $( 0 < w < 1 )$ and renders a random draw from the distribution of unit match value $\left[ v _ { 0 } - \sigma , v _ { 0 } + \sigma \right]$ with probability $1 - w .$ The consumer’s ex-ante valuation of the content piece is thus $v ^ { \prime } = w v + ( 1 - w ) v _ { 0 }$ . We can then replicate the entire analysis in the main model by replacing v with $v ^ { \prime } .$ . All results in the main model continue to hold qualitatively.

5.2.5. General Function of Total Match Value. In the main model, we assume that the consumer’s enjoyment from viewing a content piece with match value v and content length T is vT. Our key insights continue to hold under a general function $\overset { \cdot } { Y } ( v , \ \bar { T } )$ of consumer’s enjoyment as long as $Y ( v , T )$ increases with v and T. To see this, we rewrite a consumer’s utility from viewing the content piece and skipping the content piece as $U _ { e } ( n , v ) = Y ( v , T ) - \delta ( 2 n - 1 ) T ^ { 2 }$ and $\begin{array} { r } { U _ { s } ( n , v ) = \int _ { v _ { 0 } - \sigma } ^ { v _ { 0 } + \sigma } \mathrm { m a x } } \end{array}$ $\{ Y ( v , T ) , Y ( V , T ) \} f ( V ) d V - \delta T ^ { 2 } ( 2 n - 1 ) - c ,$ , respectively. The reservation unit match value $v ^ { * }$ satisfies $\int _ { v ^ { * } } ^ { v _ { 0 } + \sigma } Y ( V ,$ $T ) f ( V ) d V - c = 0$ and can be proved as increasing with T. The rest of the analysis in the main model follows, and it is easy to see that all results continue to hold qualitatively.

5.2.6. Early Termination of Content Viewing. In the main model, we assume that a consumer watches the entire content piece once deciding to view it. In practice, a consumer may terminate watching before the entire content piece is over. If the consumer watches only a small proportion of the content piece before quitting, it can be viewed as part of the inspection process and so already captured by the inspection cost c. If the consumer has watched a good portion of the content piece before quitting, it can be viewed as the consumer has obtained partial value vt, where $t < T .$ Based on our analysis in Section 5.2.1, our main model results will continue to hold qualitatively when t follows a distribution on (0, T] with mean and gyradius increasing in T.

## 6. Conclusion

Our study is inspired by the rapid growth of C2C media platforms such as TikTok. Content on a C2C media platform is self-posted by any contributors who are willing to and so covers a large range of topics that can suit viewers with heterogeneous tastes. A challenge for viewers thus is to select suitable content to view from a large number of available offerings. Our study adopts a classical, economical approach to model how utilitymaximizing consumers select content to view through a sequential inspection process. We demonstrate how the platform policy on content length limit affects this process and how the platform can set optimal content limit to maximize its performance. Our theoretical insights provide a microfoundation to understand business practices of C2C media platforms and offer guidance for platforms in different stages of business development.

First, we show that when content on the platform are longer, viewers set a higher standard of match value in selecting content to view, leading to a lower clickthrough rate of content. This finding suggests that a tight limit on content length can increase click-through rate, which may provide an explanation for the popularity of TikTok, the video-sharing platform known for its 15-second limit on video length. Second, we show that extended content length on the platform first enhances its performance but then hurts its performance, following an inverted U-shape curve. This is true for shortterm performance measured by viewer traffic and total viewing time, as well as for long-term performance measured by total consumer surplus. This finding suggests the existence of an optimal content length. Third, we find that a platform that switches the focus from short-term advertising revenue to long-term growth will benefit from extending the content length limit and enhancing consumer surplus. This finding suggests that TikTok’s extensions of content length limit from 15 seconds to 3 minutes may be driven by its enhanced focus on future growth after the company has secured the customer base and revenue sources.

We acknowledge that other factors that we do not model may also affect a platform’s content length limit. For example, short videos may have additional benefits of being easier to create, feeling more “real,” and fitting users’ short attention spans or busy schedules. Moreover, TikTok’s recent extension of content length limit to 10 minutes may attract new consumers who desire longform videos and lead to competition with YouTube.

Our current model framework can be potentially extended to investigate other issues related to content length limit and other strategic decisions of a C2C media platform. For example, content length, by affecting the total number of content pieces consumer views, may affect a platform’s learning about consumer tastes and its capability to feed consumers with suitable content. The content length limit may also have implications for consumer variety seeking and consequently affect the platform’s decision regarding content feed diversity. Our study focuses on examining consumers’ decisions in selecting suitable content pieces to view in a C2C media platform and abstracts out the existence of “fake content,” a unique business reality on a C2C media platform such as TikTok where content are freely posted by any individuals who wish to.<sup>5</sup> Whereas the existence of fake content does not affect the key insights regarding how consumers make tradeoffs between the inspection cost and the potential gain in match value in the content selection process, it would be interesting to investigate the platform’s incentive and strategic activities to manage fake content. We leave these interesting issues for future investigations.

## Acknowledgments

The authors thank the senior editor, area editor, and three anonymous reviewers for valuable comments and advice throughout the review process and Mingliu Chen and D. J. Wu for feedback on an early version of the work.

## Appendix A

## A.1. Proof of Results

Proof of Lemma 1. A consumer entering decision point 1 warrants $U ^ { s t a y } ( n ) = E _ { V } [ m a x \{ 0 , U _ { e } ( n , V ) , U _ { s } ( \stackrel { . } { n } , V ) \} ] - c > 0 \quad ( n =$ $1 , 2 , \ldots )$ . At decision point 1, the consumer’s utility from skipping an inspected content piece with known match value v is $U _ { s } ( n , v ) = E _ { V } [ \operatorname* { m a x } \{ 0 , U _ { e } ( n , \operatorname* { m a x } \{ v , V \} ) , U _ { s } ( n , \operatorname* { m a x } \{ v , V \} ) ,$ $V \} ) \}$ . Because $E _ { V } U _ { e } ( n , m a x \{ v , V \} ) \ge E _ { V } U _ { e } ( n , V )$ and $E _ { V }$ $U _ { s } ( n , m a x \{ v , V \} ) \geq E _ { V } U _ { s } ( n , V )$ , we obtain $U _ { s } ( n , v ) \geq U ^ { s t a y } ( n ) >$ 0. That is, the consumer always prefers skipping rather than exiting the platform at decision point 1. We thus prove the first part of this lemma.

Given $U _ { s } ( n , v ) > 0 ,$ we rewrite $U _ { s } ( n , v ) = E _ { V } [ \operatorname* { m a x } \{ U _ { e }$ $( n , \operatorname* { m a x } \{ v , V \} ) , U _ { s } ( n , \operatorname* { m a x } \{ v , V \} ) \} ] - c .$ . We can further write $U _ { s } ( n , \operatorname* { m a x } \{ v , V \} ) \} = E _ { V } [ \operatorname* { m a x } \{ U _ { e } ( n , \operatorname* { m a x } \{ v , V \} ) , U _ { s } ( n , \operatorname* { m a x } \{ v , V \} ] -$ $c = U _ { s } ( n , v ) - c .$ . That is, $U _ { e } ( n , \operatorname* { m a x } \{ v , V \} ) > U _ { s } ( n , \operatorname* { m a x } \{ v , V \} )$ has to be satisfied. We thus write $U _ { s } ( n , v ) = U _ { e } ( n , \operatorname* { m a x } \{ v ,$ V}) � c and prove the second part of this lemma.

Proof of Lemma 2. A consumer views a content piece with perceived match value v if $\begin{array} { r } { U _ { e } - U _ { s } = c - T \frac { \left( v _ { 0 } + \sigma - v \right) ^ { 2 } } { 4 \sigma } \geq 0 . } \end{array}$ The reservation match value v<sup>∗</sup> is the lowest value of v that satisfies this condition. We thus obtain<sub>fi fifi</sub> $v ^ { * } = v _ { 0 } + \sigma -$ $2 \sqrt { \frac { c \sigma } { T } } .$ . Moreover, we have $\begin{array} { r } { \frac { \partial v ^ { * } } { \partial T } = \frac { \sqrt { c } \sqrt { \sigma } } { T ^ { 3 / 2 } } > 0 } \end{array}$

Proof of Proposition 2. A consumer views content on the platform only if $U ^ { s t a y } ( 1 ) = T v ^ { * } - \delta T ^ { 2 } > 0 .$ , that is, if $\delta < \delta ^ { * } =$ ${ \frac { v ^ { * } } { T } } .$ Moreover, we have $\begin{array} { r } { \frac { \partial \delta ^ { * } } { \partial T } = \frac { 3 \sqrt { c } \sqrt { \sigma } } { T ^ { 5 / 2 } } - \frac { \sigma + v _ { 0 } } { T ^ { 2 } } . } \end{array}$ . It can be proved that $\begin{array} { r } { \frac { \partial \delta ^ { * } } { \partial T } > 0 \mathrm { ~ i f ~ } T < T ^ { N } = \frac { 9 c \sigma } { \left( \sigma + v _ { 0 } \right) ^ { 2 } } } \end{array}$ and $\begin{array} { r } { \frac { \partial \delta ^ { * } } { \partial T } < 0 \mathrm { ~ i f ~ } T > T ^ { N } . \mathrm { ~ A t ~ } T ^ { N } , } \end{array}$ $\begin{array} { r } { \frac { \partial \delta ^ { * } } { \partial T } = 0 } \end{array}$ and $\delta ^ { * }$ reaches maximum.

Proof of Proposition 3. First, D, M, and S are all positively associated with δ<sup>∗</sup>. In particular, $\begin{array} { r } { \frac { \partial D } { \partial \delta ^ { * } } = \frac { 1 } { \bar { \delta } - \underline { { \delta } } } > 0 , \frac { \partial M } { \partial \delta ^ { * } } = } \end{array}$ $\begin{array} { r } { T + T \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } \frac { 1 } { 2 \delta } d F ( \delta ) > 0 } \end{array}$ (note that $N ^ { * } ( \delta ^ { * } ) = 1 )$ , and $\frac { \partial S } { \partial \delta ^ { * } } = T ^ { 2 }$ $\begin{array} { r } { \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } \left( \frac { \delta ^ { * } - \delta } { 2 \delta } + N ^ { * } ( \delta ) \right) d F ( \delta ) > 0 } \end{array}$ . Recall that Proposition 2 shows $\delta ^ { * }$ is conçave on $T .$ As such, D. M, and S are all concave on T.

First, from $\begin{array} { r } { \frac { \partial D } { \partial T } = \frac { \partial D } { \partial \delta ^ { * } } \frac { \partial \delta ^ { * } } { \partial T } = \frac { 1 } { \delta } \frac { \partial \delta ^ { * } } { \partial T } , } \end{array}$ we obtain that D varie with T in the exactly the same trend that $\delta ^ { * }$ moves with T and reaches the maximum at $T ^ { N }$ . That is, $T ^ { D * } = T ^ { N }$

Then, $\begin{array} { r } { \frac { \partial M } { \partial T } = \frac { M } { T } + \frac { \partial M } { \partial \delta ^ { * } } \frac { \partial \delta ^ { * } } { \partial T } = \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } N ^ { * } ( \delta ) d F ( \delta ) + } & { T \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } \frac { \partial N ^ { * } ( \delta ) } { \partial \delta } d F ( \delta ) \frac { \partial \delta ^ { * } } { \partial T } . } \end{array}$ Therefore, when $\begin{array} { r } { \frac { \partial \delta ^ { * } } { \partial T } = 0 } \end{array}$ at $T ^ { N }$ so that $\begin{array} { r } { \frac { \partial D } { \partial T } = 0 , } \end{array}$ , we must have $\begin{array} { r } { \frac { \partial M } { \partial T } > 0 . } \end{array}$ . This implies $T ^ { M * } > T ^ { D * } = T ^ { N }$

Last, $\begin{array} { r } { \frac { \partial S } { \partial T } = \frac { 2 S } { T } + \frac { \partial S } { \partial \delta ^ { * } } \frac { \partial \delta ^ { * } } { \partial T } = 2 T \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } N ^ { * } ( \delta ) ( \delta ^ { * } - \delta ) d F ( \delta ) + T ^ { 2 } \int _ { \underline { { \delta } } } ^ { \delta ^ { * } } \frac { \partial N ^ { * } ( \delta ) ( \delta ^ { * } - \delta ) } { \partial \delta } } \end{array}$ <sup>∂δ∗</sup>. Easy to see that $T ^ { S * } > T ^ { D * } = T ^ { N }$ Moreover, $\begin{array} { r l } & { \frac { \partial \int _ { \delta } ^ { \delta ^ { * } } N ^ { * } ( \delta ) ( \delta ^ { * } - \delta ) d F ( \delta ) } { \partial \delta } = \int _ { \frac { \delta } { - } } ^ { \delta ^ { * } } \left( \frac { \partial N ^ { * } ( \delta ) } { \partial \delta } ( \delta ^ { * } - \delta ) + N ^ { * } ( \delta ) \right) d F ( \delta ) > \frac { \partial \int _ { \delta } ^ { \delta ^ { * } } N ^ { * } ( \delta ) d F ( \delta ) } { \partial \delta } = 1 + \frac { \delta } { \partial \delta } \int _ { \delta } ^ { \delta ^ { * } } N ^ { * } ( \delta ^ { * } - \delta ) \delta ( \delta ^ { * } - \delta ) d F ( \delta ) > 0 } \end{array}$ $\int _ { \underline { { \delta } } } ^ { \delta ^ { * } } \frac { \partial N ^ { * } ( \delta ) } { \partial \delta } d F ( \delta )$ . Given that $T ^ { 2 }$ increases with T at a higher rate than $T ,$ we conclude that $\begin{array} { r } { S = T ^ { 2 } \int _ { \delta } ^ { \delta ^ { * } } N ^ { * } ( \delta ) ( \delta ^ { * } - \delta ) d F ( \delta ) } \end{array}$ increases with T in a larger range than $\begin{array} { r } { M = T \int _ { \delta } ^ { \delta ^ { * } } N ^ { * } ( \delta ) d F ( \delta ) } \end{array}$ and so arrives at the maximum at a higher level of T, that is, $T ^ { S * } > T ^ { M * }$

Proof of Lemma 4. Assume that a contributor believes that the cost coefficient of the marginal contributor is $g ^ { \ast b } \in ( 0 , \overline { { g } } ]$ . Because contributors offer horizontally differentiated content, each content has the same matching value distribution among the consumer population and has an equal chance to be inspected by consumers. Thus, each content piece has an equal chance of being viewed by consumers. It is thus anticipated that each of the $\textstyle { \frac { g ^ { * b } } { \overline { { g } } } } H$ contributors that post content obtains an equal share of total viewing time M. A contributor’s expected profit is thus $\begin{array} { r } { \pi ( g ) = \rho _ { \frac { g ^ { * b } } { \overline { { g } } } H } - g , T N = \int _ { \frac { \delta } { - } } ^ { \delta ^ { * } } N ^ { * } ( \delta ) d F ( \delta ) } \end{array}$ ). In equilibrium, the mar ginal contributor satisfies $\pi ( g \leq g ^ { * } ) \geq 0$ and $\pi ( g > g ^ { * } ) < 0 .$ consistent with the common belief. That is, $g ^ { * } = g ^ { * b }$ . Rearranging $\rho _ { \frac { g ^ { * } } { \overline { { g } } } H } ^ { \frac { T N } { } } - g ^ { * } = 0 ,$ , we obtain Equation (14).

Proof of Proposition 5. Trivial. Omitted.

Proof of Corollary 1. Trivial. Omitted.

## Endnotes

<sup>1</sup> On different platforms, consumers’ random inspection may realize in different formats. For example, TikTok shows a single video on the interface and a consumer swipes the screen to inspect the next. In this context, random inspection suggests the videos are presented to consumers in random order. On platforms such as YouTube where multiple videos are shown on the interface, random inspection indi cates that a consumer inspects videos in random order.

<sup>2</sup> To further understand this assumption, c is the inspection cost for the unit match value v, but not for the total match value vT. In our research context, the platform usually provides some standard information about video features, including who has posed the video, its genre, how many views and likes a video has received. The cost of inspecting such standard information does not depend on video length. Moreover, for short videos, video features such as content topic and shooting style are typically consistent throughout. As such, a consumer only needs to sample a moment of a short video to inspect its unit match value v, regardless of the video length. We recognize this assumption might not hold for the differ ent research context of long videos.

<sup>3</sup> With free recall, a consumer can always go back, without extra costs, to the last content piece that the consumer has inspected but skipped. Technically, the assumption of free recall ensures model traceability by making the recursive structure of $U _ { s }$ stationary, which is also the reason why free recall is a standard assumption in the consumer search literature (Stahl 1989). If a recall is costly, the optimal search behavior becomes nonstationary, as demonstrated by Janssen and Parakhonyak (2007). In our research context of online videos, going back to the last skipped piece involves only a click or a swipe, and the cost associated with such actions is minimal.

<sup>4</sup> In a given market, the reasonable content length can have a common sense minimum, and our analysis only applies to content that exceeds this minimum. Further reducing content length below this common sense minimum may not further increase the click-through rate.

<sup>5</sup> TikTok’s defines the following: “Scams are fraudulent and deceitful acts that can take place online. These scams typically include the exploitation of others for some form of monetary gain but may also involve a scammer trying to obtain an individual’s personal data (https://www.tiktok.com/safety/en/scams/).”

## References

Abhishek V, Jerath K, Zhang ZJ (2016) Agency selling or reselling? Channel structures in electronic retailing. Management Sci. 62(8):2259–2280.

Aksoy L, Cooil B, Groening C, Keiningham TL, Yalc¸in A (2008) The long-term stock market valuation of customer satisfaction. J. Marketing 72(4):105–122.

Amaldoss W, Du J, Shin W (2021) Media platforms’ content provision strategies and sources of profits. Marketing Sci. 40(3):395–591.

Anderson S, Renault R (1999) Pricing, product diversity, and search costs: A Bertrand-Chamberlin-Diamond model. RAND J. Econom 30(4):719–735.

Anderson SP, Coate S (2005) Market provision of broadcasting: A welfare analysis. Rev. Econom. Stud. 72(4):947–972.

Anderson EW, Fornell C, Mazvancheryl SK (2004) Customer satis faction and shareholder value. J. Marketing 68(4):172–185.

Anderson E, Parker GG, Tan B (2014) Platform performance investment in the presence of network externalities. Inform. Systems Res. 25:152–172.

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Armstrong M, Wright J (2007) Two-sided markets, competitive bottlenecks and exclusive contracts. Econom. Theory 32(2):353–380.

Athey S, Calvano E, Gans J (2018) The impact of consumer multihoming on advertising markets and media competition. Man agement Sci. 64(4):1574–1590.

Bearden WO, Teel JE (1983) Selected determinants of consumer satisfaction and complaint reports. J. Marketing Res. 20(1):21–28.

Becker GS (1965) A theory of the allocation of time. Econom. J. (Lon don) 75(299):493–517.

Benjaafar S, Kong G, Li X, Courcoubetis C (2019) Peer-to-peer prod uct sharing: Implications for ownership, usage, and social wel fare in the sharing economy. Management Sci. 65(2):477–493.

Bhargava HK (2022) The creator economy: Managing ecosystem supply, revenue sharing, and platform design. Management Sci. 68(7):5233–5251.

Bolton RN, Drew JH (1991) A longitudinal analysis of the impact of service changes on customer attitudes. J. Marketing 55(1):1–9.

Cachon GP, Daniels KM, Lobel R (2017) The role of surge pricing on a service platform with self-scheduling capacity. Manufacturing Service Oper. Management 19(3):368–384.

Caillaud B, Jullien B (2003) Chicken & egg: Competition among intermediation service providers. RAND J. Econom. 34(2):309–328.

Chandler P, Sweller J (1991) Cognitive load theory and the format of instruction. Cognition Instruments 8(4):293–332.

Chase WG, Simon H (1973) Perception in chess. Cognitive Psych. 4(1):55–81.

Chellappa RK, Mehra A (2018) Cost drivers of versioning: Pricing and product line strategies for information goods. Management Sci, 64(5):2164–2180

Delfino D (2019) How long a YouTube video on your channel can be depending on if your account is verified. Accessed December 15, 2023, https://www.busin essinsider.com/guides/streaming how-long-can-a-youtube-video-be.

DiMaggio P (1997) Culture and cognition. Annu. Rev. Sociol. 23:263–287.

Dou Y, Wu D (2021) Platform competition under network effects: Piggybacking and optimal subsidization. Inform. Systems Res. 32(3):820–835.

Dukes A, Gal-Or E (2003) Negotiations and exclusivity contracts for advertising. Marketing Sci. 22(2):222–245.

Fabian GS (1986) 15-second commercials-the inevitable evolution. J. Advertising Res. 26(4):RC3–RC5.

Flixier (2022) Ideal TikTok video length and size in 2023: The ultimate guide. Accessed December 15, 2023, https://flixier.com/ blog/ideal-tiktok-video-length-and-size-in-2022.

Fornell C (1992) A national customer satisfaction barometer: The Swedish experience. J. Marketing 56(1):6–21.

Godes D, Ofek E, Sarvary M (2009) Content vs. advertising: The impact of competition on media firm strategy. Marketing Sci. 28(1):20–35.

Guo H, Zhao X, Hao L, Liu D (2019) Economic analysis of reward advertising. Production Oper. Management 28:2413–2430.

Hagiu A (2009) Two-sided platforms: Product variety and pricing structures. J. Econom. Management Strategy 18(4):1011–1043.

Hagiu A, Wright J (2020) Platforms and the exploration of new pro ducts. Management Sci. 66(4):1509–1782.

Hagiu A, Jullien B, Wright J (2020) Creating platforms by hosting rivals. Management Sci. 66(7):2801–3294.

Hsin WJ, Cigas J (2013) Short videos improve student learning in online education. J. Comput. Sci. College 28(5):253–259.

Hubspot (2023) The video marketing playbook trends & tips to create a video strategy in 2023. Accessed December 15, 2023, https:// blog.hubspot.com/marketing/video-marketing-report.

Iqbal M (2023) TikTok revenue and usage statistics. Accessed December 15, 2023, https://www.businessofapps.com/data/tik tok-statistics/.

Izea (2023) TikTok categories grabbing the most views. Accessed December 15, 2023, https://izea.com/resources/tiktok-categoriesgrabbing-the-most-views/.

Jain S, Qian K (2021) Compensating online content producers: A theoretical analysis. Management Sci. 67(11):7075–7090.

Janssen MC, Parakhonyak A (2007) Optimal search with costly recall. Technical report, Tinbergen Institute, Amsterdam.

Jeon YA, Son H, Chung AD, Drumwright ME (2019) Temporal certainty and skippable in-stream commercials: Effects of ad length, timer, and skip-ad button on irritation and skipping behavior. J. Interactive Marketing 47(1):144–158.

Kastrenakes J (2021) TikTok is rolling out longer videos to everyone. Accessed December 15, 2023, https://www.theverge.com/2021/ 7/1/22558856/tiktok-videos-three-minutes-length.

Kohn MG, Shavell S (1974) The theory of search. J. Econom. Theory 9(2):93–123.

Leclerc F, Schmitt BH, Dube L (1995) Waiting time and decision making: Is time like money? J. Consumer Res. 22(1):110–119.

Lin S (2020) Two-sided price discrimination by media platforms. Marketing Sci. 39(2):285–457.

Lu J, Wu D, Mao M, Wang W, Zhang G (2015) Recommender system application developments: A survey. Decision Support Sys tems 74(c):12–32

Luo X, Homburg C, Wieseke J (2010) Customer satisfaction, analyst stock recommendations, and firm value. J. Marketing Res. 47(6):1041–1058.

MacInnis DJ, Jaworski BJ (1989) Information processing from advertisements: Toward an integrative framework. J. Marketing 53(4):1–23.

Manasrah A, Masoud M, Jaradat Y (2021) Short videos, or long videos? A study on the ideal video length in online learning. Jaber KM, ed. Proc. Internat. Conf. on Inform. Tech. (IEEE, Piscat away, NJ), 366–370.

Matsakis L (2020) TikTok is paying creators. not all of them are happy. Accessed December 15, 2023, https://www.wired.com/story/ tiktok-creators-fund-revenue-sharing-complaints/.

Mord MS, Gilson E (1985) Shorter units-risk responsibility reward. J. Advertising Res. 25(4):9–19.

Pechmann C, Stewart DW (1988) Advertising repetition: A critical review of wearin and wearout. Current Issues Res. Advertising 11(1–2):285–329.

Redden JP (2008) Reducing satiation: The role of categorization level. J. Consumer Res. 34(5):624–634.

Rethans AJ, Swasy JL, Marks LJ (1986) Effects of television commercial repetition, receiver knowledge, and commercial length: A test of the two-factor model. J. Marketing Res. 23(1):50–61.

Rochet JC, Tirole J (2003) Platform competition in two-sided markets. J. Eur. Econom. Assoc. 1(4):990–1029.

Rochet JC, Tirole J (2006) Two-sided markets: A progress report. RAND J. Econom. 37(3):645–667.

Rogers SC (1995) How to create advertising that works. J. Bus Industry Marketing 10(2):20–33.

Singh SN, Cole CA (1993) The effects of length, content, and repetition on television commercial effectiveness. J. Marketing Res. 30(1):91–104.

Singh SN, Rothschild ML (1983) Recognition as a measure of learning from television commercials. J. Marketing Res. 20(3):235–248.

Singh SN, Rothschild ML, Churchill GA Jr (1988) Recognition vs. recall as measures of television commercial forgetting. J. Market ing Res. 25(1):72–80.

Slee D (2020) Clipped: I watched the 100 best TikTok videos to find the optimum length of a clip. Accessed December 15, 2023, https://danslee.co.uk/2020/01/21/clipped-i-watched-the-100- best-tiktok-videos-to-find-the-optimum-length-of-a-clip/.

Slemmons K, Anyanwu K, Hames J, Grabski D, Mlsna J, Simkins E, Cook P (2018) The impact of video length on learning in a middle-level flipped science setting: Implications for diversity inclusion. J. Sci. Ed. Tech. 27(5):469–479.

Spangler T (2022) TikTok bumps up max video length to 10 minutes. Accessed December 15, 2023, https://variety.com/2022/digital news/tiktok-maximum-video-length-10-minutes-1235191773/.

Srivastava RK, Shervani TA, Fahey L (1998) Market-based asset and shareholder value: A framework for analysis. J. Marketin 62(1):2–18.

Stahl DO (1989) Oligopolistic pricing with sequential consumer search. Amer. Econom. Rev. 79(4):700–712.

Sundararajan A (2004) Nonlinear pricing of information goods. Management Sci. 50(12):1660–1673.

TikTok (2020) How TikTok recommends videos for you. Accessed December 15, 2023, https://newsroom.tiktok.com/en-us/howtiktok-recommends-videos-for-you.

Toubia O, Stephen AT (2013) Intrinsic vs. image-related utility in social media: Why do people contribute content to twitter? Marketing Sci. 32(3):368–392.

Varan D, Nenycz-Thiel M, Kennedy R, Bellman S (2020) The effects of commercial length on advertising impact: What short advertisements can and cannot deliver. J. Advertising Res. 60(1):54–70.

Wang C, Zhou B, Joshi YV (2023) Endogenous consumption and metered paywalls. Marketing Sci., ePub ahead of print May 9, https://doi.org/10.1287/mksc.2023.1444.

Wheatley JJ (1968) Influence of commercial’s length and position. J. Marketing Res. 5(2):199–202.

Wolinsky A (1986) True monopolistic competition as a result of imperfect information. Quart. J. Econom. 101(3):493–511.

Yeshanew H (2021) Shorter videos are in demand. Here's how different social media platforms are reacting. Accessed December 15, 2023 https://www.entrepreneur.com/science-technology/shortervideos-are-in-demand-heres-how-different-social/393036.

Zhang K, Sarvary M (2015) Differentiation with user-generated con tent. Management Sci. 61(4):898–914.

Zote J (2022) The TikTok algorithm explained. Accessed December 15, 2023, https://sproutsocial.com/insights/tiktok-algorithm/.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
