---
otero_id: 9254
otero_key: "7D3R32VU"
title: "Strategic effort allocation in online innovation tournaments"
authors: "Indika Dissanayake; Jie Zhang; Mahmut Yasar; Sridhar P. Nerur"
year: "2018"
journal: "Information & Management"
doi: "10.1016/j.im.2017.09.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Strategic e<sup>f</sup>ort allocation in online innovation tournaments

Indika Dissanayake<sup>a,⁎</sup>, Jie Zhang<sup>b</sup>, Mahmut Yasar<sup>c</sup>, Sridhar P. Nerur<sup>b</sup>

<sup>a</sup> University of North Carolina Greensboro, PO Box 26170, Greensboro, NC 27402, United States

<sup>b</sup> The University of Texas at Arlington, 701 S West St, PO Box 19437 Arlington, TX 76019, United States

<sup>c</sup> The University of Texas at Arlington, 701 S West St, PO Box 19479 Arlington, TX 76019, United States

## A R T I C L E I N F O

Keywords: Innovation tournaments Crowdsourcing Social comparison Solver strategies Sniping

## A B S T R A C T

Online innovation tournaments, such as those hosted by crowdsourcing platforms (e.g., Kaggle), have been widely adopted by <sup>fi</sup>rms to evolve creative solutions to various problems. Solvers compete in these tournaments to earn rewards. In such competitive environments, it is imperative that solvers provide creative solutions with minimum e<sup>f</sup>ort. This article explores the factors that in<sup>fl</sup>uence the solvers’ e<sup>f</sup>ort allocation decisions in a dynamic tournament setting. Speci<sup>fi</sup>cally, comprehensive time variant data of teams that participated in crowdsourcing competitions on Kaggle were analyzed to gain insight into how solvers continually formulate strategies in light of performance feedback obtained through interim ranking. The results suggest that solvers strategically allocate their e<sup>f</sup>orts throughout the contest to dynamically optimize their payo<sup>f</sup>s through balancing the probability of winning and the cost of expending e<sup>f</sup>ort. In particular, solvers tend to increase their e<sup>f</sup>orts toward the end of tournaments or when they get closer to winning positions. Furthermore, our <sup>fi</sup>ndings indicate that a last-minute surge in e<sup>f</sup>ort is more prevalent among high-skill solvers than in those with lower skill levels. In addition to providing insights that may help solvers develop strategies to improve their performance, the study has implications for the design of online crowdsourcing platforms, particularly in terms of incentivizing solvers to put forth their best e<sup>f</sup>ort.

## 1. Introduction

An innovation tournament refers to “a process that uncovers exceptionally good opportunities by considering many raw opportunities at the outset and selecting the best to survive” ([1] p.80). With rapid advances in Information Technologies, companies have increasingly adopted online innovation tournaments and contests to complement their in-house innovation projects, primarily to reduce costs without compromising on quality [2]. Online platforms facilitate tournamentbased tasks in di<sup>f</sup>erent areas, including software development, predictive analytics, scienti<sup>fi</sup>c problem solving, and graphics and arts de sign [3]. For instance, the celebrated Net<sup>fl</sup>ix \$1 M challenge attracted about 51,000 participants from 86 countries working, all vying to build a prediction model that would improve the accuracy of Net<sup>fl</sup>ix’s movie recommendation algorithm by 10% [4]. In yet another competition, more than 57,000 online gamers, most of whom had no prior experi ence in molecular biology, contributed to the identi<sup>fi</sup>cation of the structure of a particular protein within three weeks, thus solving a problem that had de<sup>fi</sup>ed researchers at the University of Washington for years [5,6]. It is apparent that such platforms provide a cost-e<sup>f</sup>ective means to exploiting the “wisdom of the crowds,” thereby a<sup>f</sup>ording companies novel insights and solutions that may not be forthcoming with in-house projects alone.

The emerging literature on innovation tournaments has primarily focused on the optimal design of contests [7–10] or on the e<sup>f</sup>ects of individual characteristics and behaviors on contest outcomes [11–15], with the goal of maximizing payo<sup>f</sup>s. These studies provide evidence of the bene<sup>fi</sup>ts of innovation contests, such as lower costs [13], lower risks [7], and higher quality of solutions [16], as well as a<sup>f</sup>ording multiple alternative solutions to challenging problems [9]. Prior studies (e.g., [17]) have carefully explored the impact of the characteristics and behaviors of solvers on the outcome of innovation tournaments under di<sup>f</sup>erent competition conditions. Our paper extends these studies by examining how solvers strategically exploit the dynamics of these tournaments to wisely allocate e<sup>f</sup>orts in an un-blind competition setting.

In innovation tournaments, solvers need to improve their skills and/ or enhance their e<sup>f</sup>orts to increase the likelihood of winning [9]. Although all the contestants expend e<sup>f</sup>ort to come up with a superior solution, it is only the best solution that is ultimately rewarded. Therefore, increasing e<sup>f</sup>ort in this setting can be costly, as a consequence of which contestants strategically decide how much e<sup>f</sup>ort to exert over the duration of the contest in order to enhance their chances of winning. That is, participants may not necessarily put forth their best e<sup>f</sup>orts to achieve their highest potential but rather strive just enough to accomplish their goal of providing a solution that is good enough to outperform their opponents and win the reward. Understanding these strategies would not only be helpful to contestants but also provide insights to platform providers. Seekers, or platform providers, do not have direct control over the extent to which contestants exert e<sup>f</sup>ort to solve the problem at hand. However, an understanding of the factors that in<sup>fl</sup>uence how much e<sup>f</sup>ort solvers expend would help platform providers design competitions in such a way that solvers are persuaded to put forth their best e<sup>f</sup>orts, thus increasing the likelihood of an op timal winning solution.

Our study used data from Kaggle.com, a large online predictive analytics tournament platform, to investigate how contestants formulate strategies for allocating e<sup>f</sup>orts throughout a contest with a view toward improving their rankings and eventually securing a winning position. We identi<sup>fi</sup>ed two di<sup>f</sup>erent strategies: timing of eforts (i.e., timing of submitting solutions) and interim rank impact. A key insight of our study is that solvers strategically delay their e<sup>f</sup>orts until the end of the contest. Speci<sup>fi</sup>cally, consistent with the <sup>fi</sup>ndings in a complete information, sequential all-pay auction setting, our results showed that strong players strategically delay their e<sup>f</sup>orts [18,19]. Furthermore, our <sup>fi</sup>nding that solvers strategize based on their interim rankings and subsequently exert more e<sup>f</sup>ort as they get closer to the winning position is consistent with the tenets of social comparison theory [20,21]. Thus, our study provides novel insight into the behavior of contestants as they respond to “game mechanics” such as interim rankings – a manifestation of leaderboards – and evolve strategies to strike the right balance between e<sup>f</sup>ort and performance.

In summary, this paper makes signi<sup>fi</sup>cant contributions to the sparse but emerging literature on innovation tournaments. First, this study is among a select few that have examined the e<sup>f</sup>ects of interim performance feedback in dynamic innovation tournaments. It extends the application of social comparison theory to online tournament platforms by showing that feedback can intensify the competition among top rankers. Interestingly, this is also an a<sup>fi</sup>rmation of the claim by ad vocates of gami<sup>fi</sup>cation that “gaming elements” such as leaderboard (i.e., interim rankings) can engage and motivate participants (e.g., [22]). Second, it extends the timing strategies that were widely ex amined in the online auction literature to investigate the timing of efforts in a dynamic innovation tournament setting. Third, it shows that these timing strategies are contingent on the expertise of solvers by examining the moderating impact of their skills. Finally, to the best of our knowledge, ours is the <sup>fi</sup>rst study to utilize temporally varying data, such as interim rankings and e<sup>f</sup>orts, to elucidate how participants with di<sup>f</sup>ering skills continually strategize to balance their e<sup>f</sup>ort with the level of performance they desire.

The remainder of this paper is organized as follows. The next section reviews the literature related to innovation tournaments, interim ranking feedback, and timing strategies. It is followed by an articulation of our research model and the hypotheses that follow from it. Subsequently, we describe our data collection procedures and measures and then present our <sup>fi</sup>ndings. Finally, we conclude with a discussion of the study’s theoretical and managerial implications as well as its limitations, followed by directions for future research.

## 2. Literature review

This study is grounded in two distinct streams of research, namely Tournament- and Auction-related. In a general tournament setting (e.g., Sport tournaments such as weightlifting tournaments [23]), social comparison theory can be used to explain the impact of interim ranking on participants’ e<sup>f</sup>orts allocation patterns, while in auctions, timing strategies are more apparent. However, innovation tournaments in an un-blind setting, such as this study, have features of both tournaments and all-pay auctions. Since these features simultaneously impact sol vers’ e<sup>f</sup>ort allocation decisions in innovation tournaments, it may not be appropriate to explore them separately. Thus, we relied on theories from both the auction and tournament literature to study this e<sup>f</sup>ect. In this section, we <sup>fi</sup>rst compare and contrast our study with prior work on innovation tournaments. Subsequently, we review pertinent literature and theories on interim ranking feedback (e.g., social comparison theory) and timing strategies (auction literature).

## 2.1. Innovation tournaments

A tournament is a “competition in which the outcome is determined by relative performance and the winner takes disproportionally larger award than the loser” ([24] p.578). It is also referred to as rank-ordered tournament since the performance is based on rank. Tournament theory has been applied in various contexts including academics, sports, sales, scienti<sup>fi</sup>c work, and executive promotions [3].

In the online innovation tournament context, geographically distributed contestants compete with one another for monetary rewards. There is a growing body of literature on online innovation tournaments that primarily investigates the in<sup>fl</sup>uence of contest characteristics (reward structure, problem characteristics, scope) and contestant characteristics (demographics, familiarity, skill) on the likelihood of <sup>fi</sup>nding a high-quality solution [11,25]. For example, Boudreau et al. [26] showed that, in general, increasing competition negatively impacts the performance of competitors, but induces a small group of competitors at the very top to exert more e<sup>f</sup>ort [3]. While adding more competitors reduces the incentive to solvers to exert more e<sup>f</sup>ort, it also increases the likelihood of <sup>fi</sup>nding an optimal solution [7]. Terwiesch and Xu [9] investigated how e<sup>fi</sup>ciencies in these competitions improved with changing award structure. Liu et al. [19] used a randomized <sup>fi</sup>eld experiment in a crowdsourcing context to examine the e<sup>f</sup>ects of reward size and early high-quality submission on the number and quality of subsequent submissions. They found that the level of participation as well as the quality of submissions was positively associated with the size of the incentive. Furthermore, they demonstrated that experienced users were less likely to pursue tasks that already had high-quality solutions. While their study focused on decisions related to contest participation, our study draws attention to the underlying dynamics of the e<sup>f</sup>ort allocation process. Archak [11] showed that reputation systems in<sup>fl</sup>uence strategic behaviors of solvers. Speci<sup>fi</sup>cally, the study demonstrated that top-rated solvers used di<sup>f</sup>erent strategies to successfully deter entry of their rivals in the same contest.

Most of these studies are based on blind, one-shot competition settings, with a few notable exceptions [25,27]. That is, solvers cannot see how good the solutions submitted by their rivals are, and they also get only one chance to submit a solution. Thus, the contestants primarily rely on the problem speci<sup>fi</sup>cation provided by the contest organizer at the beginning of the contest period.

Online “un-blind” innovation tournaments are becoming popular for <sup>fi</sup>nding creative solutions to diverse problems (e.g., Kaggle.com, logomyway.com, and taskcn.com). Moreover, some innovation tournaments allow solvers to make multiple solution submissions within the contest duration. Thus, over time solvers learn strategies to be successful in this “un-blind” and dynamic competition setting. However, to the best of our knowledge, the strategic behaviors of solvers have not attracted much attention in the innovation tournament literature. Among the few exceptions to this are [15,25,28,29]. Both Yang et al. [15] and Chen and Liu [29] showed that solvers who made their initial submission early or late within the contest duration have a higher chance of winning the competition, while Bockstedt et al. [28] showed that contestants who have a lower position in initial submission, or a higher level of separation between initial and last submission, are more likely to be successful. Yang et al. [15] argued that some solvers prefer to submit good solutions early in the contest to scare away other competitors as well as to receive early feedback from the seekers. In contrast, other contestants may prefer to strategically wait until the end to submit their solutions, so that they can have access to more information. Al-Hasan et al. [30] also emphasized the importance of the timing of the entry. They showed that feedback in open innovation contests helps early entrants by providing an opportunity to signi<sup>fi</sup>cantly revise their submission, while it results in a signi<sup>fi</sup>cant amount of information spillover favoring later entrants. However, our study is distinctive in many ways: First, Yang et al. [15] and Chen and Liu [29] considered only the timing of the initial submission. Thus, their data were cross-sectional in nature, similar to one-shot/one-bid auctions. Bockstedt et al. [25] showed that participants’ strategies, such as timing of the <sup>fi</sup>rst entry, number of entries, range of entries, and skewness of entries, in<sup>fl</sup>uence the probability of winning a contest. Though Bockstedt et al. [25] and Bockstedt et al. [28] refer to repeated submissions, they considered only the di<sup>f</sup>erence between the <sup>fi</sup>rst and last submissions. That is, they did not have any time variant component in their model. In our setting, solvers can make multiple submissions throughout the duration of the contest, which is akin to repeated/ multiple-bid auctions. We observed how the allocation of e<sup>f</sup>orts changes during the entire period of the contest and not just at the beginning or the end of the contest. Our study is unique in that it accounts for the dynamics of e<sup>f</sup>ort allocation throughout the competition by considering the timing of every submission by every team. Second, our study further distinguishes itself from prior works (e.g., [15,25,28,29]) by considering the impact of ranking feedback as well as the moder ating e<sup>f</sup>ect of the skill levels of contestants. Table 1, which compares and contrasts our work with previous studies on innovation tournaments, clearly shows the broader scope of our study.

Some crowdsourcing platforms provide interim feedback that can be viewed by all participants. For example, leaderboards, an element inspired by games and one that is strongly advocated by proponents of gami<sup>fi</sup>cation (e.g., [22]), display a rank-ordered listing of contestants. Feedback, in general, has a signaling e<sup>f</sup>ect on other solvers, potentially either motivating them to work harder to compete or persuading them to quit. Therefore, open feedback that can be viewed by all may in <sup>fl</sup>uence solvers’ e<sup>f</sup>ort levels. Wooten [31] showed that in un-blind, repeated entry settings, substantial solution improvement by a contestant enhances the e<sup>f</sup>orts of rivals and results in a higher submission rate. This, in turn, results in an improved contest outcome. The study also showed that contest-speci<sup>fi</sup>c characteristics, such as higher prices, and participant-speci<sup>fi</sup>c characteristics, such as prior performance and platform experience, lead to a greater number of incremental improvements.

The next section discusses how social comparison theory may be used to explain the e<sup>f</sup>ect of open feedback about interim rank on participants’ behaviors

Innovation Tournament Literature.

<table><tr><td rowspan="2"></td><td rowspan="2">Time Series Data</td><td colspan="3">Explanatory Variables</td></tr><tr><td>Timing Strategies</td><td>Skill Moderation</td><td>Interim Rank</td></tr><tr><td>Yang et al. [15]</td><td>□</td><td>☑</td><td>□</td><td>□</td></tr><tr><td>Chen &amp; Liu [29]</td><td>□</td><td>☑</td><td>□</td><td>□</td></tr><tr><td>Bockstedt et al. [28]</td><td>□</td><td>☑</td><td>□</td><td>□</td></tr><tr><td>Bockstedt et al. [25]</td><td>□</td><td>☑</td><td>□</td><td>□</td></tr><tr><td>Al-Hasan et al. [30]</td><td>□</td><td>☑</td><td>□</td><td>□</td></tr><tr><td>Liu et al. [19]</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>Terwiesch &amp; Xu [9]</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>Boudreau et. al. [25]</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>Boudreu et al. [26]</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>Wooten [31]</td><td>□</td><td>□</td><td>□</td><td>☑</td></tr><tr><td>Archak [11]</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>Boudreau et al. [3]</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>Our study</td><td>☑</td><td>☑</td><td>☑</td><td>☑</td></tr></table>

Note: represents “applied” or “considered.” ☐ represents “not applied” or “not considered .

## 2.2. Interim ranking feedback

According to social comparison theory, individuals are driven by a basic desire to improve their performance (“unidirectional drive upward ) and to minimize the di<sup>f</sup>erence between themselves and other persons (“targets”) [32]. Social comparison means “the tendency to self-evaluate by comparing ourselves to others” ([32] p. 634) and is the key to competitive behavior. Furthermore, scholars have shown that situational factors, such as incentive structure (e.g., winner takes all or multiple rewards), proximity to a standard $( \mathrm { i . e . , }$ closer to the winning position or far away), and the number of competitors in<sup>fl</sup>uence levels of social comparison [32]. All these situational factors are pertinent to the innovation tournaments discussed in this study. Furthermore, Garcia et al. [21] generalized their <sup>fi</sup>ndings and stated that there is “a tendency for competition among commensurate rivals on a relevant dimension to intensify in the proximity of a meaningful standard” ([21] p. 970).

In innovation tournaments, interim rank disclosure facilitates social comparisons among contestants $( \boldsymbol { \mathrm { i . e . } } ,$ they evaluate their own performance by comparing themselves with others). These social comparisons could result in competitive arousal [33] and impact contestants’ behaviors. This is a widely investigated area in the management and psychological literature [34]. However, <sup>fi</sup>ndings on the impact of ranking feedback on contestants’ e<sup>f</sup>orts are inconclusive.

Social comparison theory o<sup>f</sup>ers some insights that can potentially provide an explanation for these inconclusive <sup>fi</sup>ndings. For instance, Hannan’s [35] experimental study showed that relative performance feedback under tournament compensation plan reduced the average performance, while it increased the average performance under in dividual performance compensation plan. According to social comparison theory, people generally exhibit an upward drive as they endeavor to improve their performance and outperform those they consider to be marginally better than themselves [36]. This, however, is contingent on the standard used for comparison. In the tournament compensation plan used by Hannan [35], only the top 10% were compensated. Thus, the standard was at the top. Analysis showed that even though the overall average performance went down, the mean performance of the top two deciles increased. This suggests that solvers closer to the standard act more competitively; thus, ranking feedback increases the e<sup>f</sup>ort of higher performing participants. In a classroom setting, Azmat and Iriberri [34] found that providing information about the class average to students has a positive e<sup>f</sup>ect on their <sup>fi</sup>nal performance. In contrast, Barankay’s [37] experiment showed that, in the absence of a standard, interim rank feedback negatively impacts employees’ e<sup>f</sup>orts. That is, participants in Barankay’s [37] study got paid irrespective of their performance or ranking. Thus, there was no standard. In yet an other study Casas-Arce and Martinez-Jerez [38] found that winners reduce their e<sup>f</sup>ort as the lead increases, while the trailing contestants reduce their e<sup>f</sup>orts only when the gap between their current rank and the winning position is very large. The context of Casas-Arce and Martinez-Jerez [38]’s study was, however, di<sup>f</sup>erent, for the top 50 participants were rewarded regardless of their true rankings. Thus, the goal of the solvers was to be among the <sup>fi</sup>rst 50 without incurring a huge cost in terms of e<sup>f</sup>ort. As a consequence, there is a heightened intensity of competition among commensurate rivals whose ranking are closer to the standard (e.g., #50 vs. #51), whereas those whose rankings are far away from the standard (e.g.. #1 ys. #2 or #1000 ys. #1001) tend to expend less e<sup>f</sup>ort. Ederer [39] has argued that interim performance feedback impacts workers’ incentives to exert e<sup>f</sup>ort. It helps workers e<sup>f</sup>ectively tailor their e<sup>f</sup>ort choices based on their abilities. That is, contestants with high abilities exert more e<sup>f</sup>ort, whereas contestants with lower abilities put forth less e<sup>f</sup>ort [39]. Ericksson [40] showed empirical evidence for positive peer e<sup>f</sup>ects of ranking feedback in a tournament. That is, frontrunners do not reduce their e<sup>f</sup>orts and underdogs do not leave the tournament.

In a weightlifting tournament setting, Genakos and Paliero [23] have shown that revealing information on the ranking of contestants increases risk-taking behavior of contestants who are just behind the interim leaders. Although risk-taking behavior is somewhat similar to e<sup>f</sup>ort allocation in innovation tournaments, e<sup>f</sup>ort allocation or the risk taking in a weightlifting tournament occurs at <sup>fi</sup>xed intervals and participants cannot decide on when to allocate the e<sup>f</sup>orts. In our context, solvers can simultaneously decide not only how much e<sup>f</sup>ort to put forth but also when to allocate the e<sup>f</sup>ort. Thus, our study enriches this lit erature by introducing timing strategies.

The next section explains how we draw on the conceptual under pinnings of the auction literature to explain timing strategies (i.e., timing of allocation of e<sup>f</sup>orts) that emerge in open innovation tour naments characterized by a repeated entry setting.

## 2.3. Timing strategies (auction literature)

Innovation tournaments explored in this study have features of all pay auction. In all-pay auctions, all the bidders must pay their bid amount regardless of whether they win the auction or not. Only the highest bid will receive the good or service. In an innovation tournament, when contestants are allowed to submit solutions anytime during the contest, the submissions (e<sup>f</sup>ort exertions) are similar to bidding in auctions [19,41]. Bid amount in all-pay auctions is analogous to e<sup>f</sup>orts of solvers in innovation competitions. In innovation competitions, all solvers expend e<sup>f</sup>orts, but only the winner will be entitled to a reward [19]. Thus, spending the right amount of e<sup>f</sup>ort at the right time is critical in this setting to increase the chance of winning without wasting signi<sup>fi</sup>cant amounts of e<sup>f</sup>ort.

In an online auction context, researchers have investigated dynamic bidding strategies and their bene<sup>fi</sup>ts. In general, the auction literature has found mixed results regarding the e<sup>f</sup>ect of early and late bidding strategies. Some scholars have argued that bidders prefer to strategically wait until the last minute to avoid an early bidding war that increases the transaction price. Moreover, bidding late helps informed bidders protect their information, thus preventing their competitors from learning. This last-minute bidding practice is called “sniping” in an auction context [42]. Revealing their true value early in the auction will give their rivals a competitive edge. While bidding near the end of the auction will not give competitors su<sup>fi</sup>cient time to respond, early movers may reveal strategies that bidders can learn. On the other hand, a bidder may decide to make an early high bid to make others les interested in the auction [15,30].

Roth and Ockenfels [42] showed that late bidding (sniping) is more prevalent in eBay auctions −where end times are <sup>fi</sup>xed − than in Amazon auctions where close times could be automatically extended based on when the last bid is received. They also observed that bidding patterns varied by the experience level of bidders. In an innovation tournament setting, the end times of the contest are <sup>fi</sup>xed. Thus, sniping is expected to be a dominant strategy. Solvers in an innovation tournament context are quite unlike some of these online auctions, where the reservation price can be simply <sup>fi</sup>xed and the system (sniping agent [33]) can then automatically raise bids by minimum increments above the previous high bid. Solvers must decide how much e<sup>f</sup>ort to put forth. Also, while bid prices in auctions can be made quickly, solutions to problems in an innovation tournament setting cannot be evolved ra pidly. Solution improvements not only take time but are also contingent on the skill levels of participants. Solvers with high skills, as opposed to low-skilled ones, could quickly improve their solution. Jian et al. [27] conducted an experiment to compare and contrast e<sup>f</sup>ort levels in si multaneous all-pay auctions and sequential all-pay auctions. They found that the expected maximum e<sup>f</sup>ort is higher in simultaneou auctions than in sequential auctions. Furthermore, they found that in a simultaneous auction setting, users with high ability tend to exert less e<sup>f</sup>ort when faced with multiple opponents. Our context, like the one in

Jian et al. [27], is similar to sequential auction. However, Jian et al. [27] considered a one-shot interaction, while our setup involved repeated entries. Moreover, they did not explore participants’ strategic behaviors with respect to timing and interim ranks. Also, many studies that have adopted the all-pay auction framework have not considered heterogeneity of contestant skills. The notable exceptions are Liu et al. [8] and Konrad and Leininger [18]. Liu et al. [8] argued that players exert their best e<sup>f</sup>ort when their rivals have similar skill levels. Konrad and Leininger [18] is the closest analytical model to this study. In an allpay auction setting with complete information, they have shown that contestants’ choice of timing can be endogenized and the strongest player strategically decides to enter late.

The ensuing section articulates a research model and formulates hypotheses resulting therefrom.

## 3. Research mode

In an online innovation tournament with an un-blind setting, solvers strategically alter their e<sup>f</sup>orts to enhance their chances of winning, while reducing the cost of e<sup>f</sup>ort. This study investigated solvers’ stra tegies using weekly performance data from an online innovation tournament platform for data analysts, Kaggle.com. Based on a review of prior literature as well as <sup>fi</sup>ndings from competitions, we identi<sup>fi</sup>ed two such strategies: timing strategies and strategies related to interim ranks. Drawing from the theoretical foundations of all-pay auctions with complete information and social comparison theory, we hypothesize that the contest time elapsed and the solvers’ rankings in<sup>fl</sup>uence their e<sup>f</sup>ort allocation decision.

Unlike o<sup>fl</sup>ine contests, most of these online contests allow participants to compete dynamically. Online innovation tournaments considered in this study show some characteristics of all-pay auctions with complete information. In our context, solvers can submit multiple solutions throughout the competition. Every time a contestant submits a solution, his/her ranking and solution quality are revealed in a dynamic leaderboard open to all the contestants. At the end of the competition, only the best solution will be entitled to the reward. Similarly, in auctions, all participants submit bids and only the winning bid will be entitled to the good/service. Thus, solution submission behaviors in these competitions are somewhat similar to bidding behaviors in auctions. The online auction literature has demonstrated that carefully choosing bid timing could signi<sup>fi</sup>cantly in<sup>fl</sup>uence the probability of winning the auction [43]. More speci<sup>fi</sup>cally, the auction literature has identi<sup>fi</sup>ed bene<sup>fi</sup>ts from the late-bidding or “sniping” strategy. Bidders tend to submit their bids at the end of the auction to avoid competition with other bidders [43]. Furthermore, in addition to avoiding bidding wars that lead to a high transaction price, it protects information spillovers [42].

We expect a similar behavior in the online tournament setting. Late submissions reduce information spillover, do not provide su<sup>fi</sup>cient time for rivals to respond, avoid submission wars that lead to very high efforts, and provide an opportunity for contestants to learn about their rivals’ performances. Thus, we argue that solvers strategically exert more e<sup>f</sup>ort toward the end of the competition. In the context of our study, the number of solution submissions is a re<sup>fl</sup>ection of the level of e<sup>f</sup>ort exerted. Hence, we have the following hypothesis:

Hypothesis 1 (Timing Strategy Hypothesis). Time elapsed is positively related to the level e<sup>f</sup>ort. That is, teams tend to make more submissions toward the end of the competition.

According to the conceptual underpinnings of all-pay auction with complete information, the best strategy for the strongest player is to enter late [18]. Liu et al. [19] empirically demonstrated that experienced users submit their initial solutions later than inexperienced ones. Thus, based on the theory and prior literature, we argue that high-skill players will bene<sup>fi</sup>t through strategically delaying their submissions. High-skill teams possess the necessary expertise to adapt, learn, and work fast; hence, they − unlike low-skill teams − can a<sup>f</sup>ord to wait. Moreover, information spillover is more critical to high-skill solvers, for the competitive edge they have − because of their task-related skills − may be lost if they revealed information about the quality of their solutions to their rivals. In the same setting, Wooten [31] showed that a substantially improved submission by a solver increases the subsequent e<sup>f</sup>orts of other participants. High-skill contestants are reluctant to submit a good solution early because that would set a higher standard for everyone, inducing contestants to expend more e<sup>f</sup>ort, which, in turn, would require the early contributors of high-quality solutions to increase their e<sup>f</sup>orts to win the competition. The goal of high-skill solvers, therefore, is not to submit their best solution, but to submit a solution that is good enough to outperform their rivals’ solutions. Hence, we argue that high-skill solvers strategically expend more e<sup>f</sup>ort (as evidenced by the number of submissions) toward the end of a competition when compared with low-skill solvers.

Hypothesis 2 (Skill Moderation Hypothesis). Solvers’ skill positively moderates the relationship between time elapsed and e<sup>f</sup>ort, such that high-skill solvers expend more e<sup>f</sup>ort toward the end of competition.

Ranking disclosures in tournaments facilitate social comparisons. That is, it allows contestants to compare their abilities with those of their opponents. Social comparison helps participants make informed decisions about how much e<sup>f</sup>ort they need to put forth to enhance their chances of winning while reducing the cost of e<sup>f</sup>ort. Thus, solvers can e<sup>f</sup>ectively tailor their e<sup>f</sup>orts based on interim feedback [39].

According to social comparison theory [20], contestants in competitive innovation tournaments, such as the one in our study, are likely to have a “drive upward” to perform well as they continually evaluate themselves vis-à-vis those who are placed higher on the leaderboard. The theory suggests that there are several predictors that account for participants’ strategic behaviors, namely mutually relevant dimension, meaningful standard, and commensurate rivals. In our context, the monetary reward would constitute the mutually relevant dimension. Only the winner, or the top ranker, would be eligible for the reward. Thus, the meaningful standard is the number one position (i.e., top ranking). Solvers with adjacent ranks are referred to as commensurate rivals. The game is dynamic because rankings on the leaderboard are updated regularly. Although the mutually relevant dimension stays the same throughout the competition, the proximity to a meaningful stan dard and to commensurate rivals could change every time a solver makes a new submission. Drawing on social comparison theory, Garcia et al. [21] showed that “rankings that coincide with a standard intensify the social comparison process to a greater extent than rankings that do not.” Interim ranking disclosure through open leaderboard would make the intensity of competition more unequally distributed among com peting solvers. Since only the top ranker is entitled to the reward, competitive behavior intensi<sup>fi</sup>es among commensurate rivals who have high rankings (e.g., #2 vs. #3), whereas the competition among those who have low rankings (e.g., #50 vs. # 51) is not likely to be intense [21]. In addition, from the perspective of economic theory, participants are motivated to increase their e<sup>f</sup>orts as the likelihood of winning increases [35]. Thus, we argue that when solvers get closer to the winning position, they tend to exert more e<sup>f</sup>ort.

Hypothesis 3 (Ranking Hypothesis). Solvers’ rankings of the previous week positively in<sup>fl</sup>uence their e<sup>f</sup>orts in the current week (i.e., top ranked players in the previous week’s leaderboard make more e<sup>f</sup>orts, while bottom-ranked players make less e<sup>f</sup>ort).

As indicated above, prior literature showed that the e<sup>f</sup>ort put forth by participants is in<sup>fl</sup>uenced by factors such as the gap between the current and the winning position [21,38], timing of the contest [15,29], contest-speci<sup>fi</sup>c characteristics, and participant-speci<sup>fi</sup>c characteristic [31]. In our model, the dependent variable is the e<sup>f</sup>ort of team i in contest j at time t. Our main explanatory variables were as follows: contest time elapsed in contest j as of time t, interim rank of team i in contest j at time (t-1), and the interaction of the skill of team i and the time elapsed. In addition, we added a term (square of the time elapsed) to account for non-linearity. Furthermore, we controlled for contestspeci<sup>fi</sup>c e<sup>f</sup>ects using <sup>fi</sup>xed e<sup>f</sup>ects. Also, we added lagged dependent variable to control for persistency. We also accounted for team-speci<sup>fi</sup>c e<sup>f</sup>ects by controlling for size and skill of team i in contest j. We summarize our econometric model as follows:

$$
\begin{array}{r l} E f f o r t _ {i j t} = & \alpha_ {0} + \alpha_ {1} E f f o r t _ {i j (t - 1)} + \alpha_ {2} T i m e E l a p s e d _ {j t} + \alpha_ {3} T i m e E l a p s e d _ {j t} ^ {2} \\ & + \alpha_ {4} R a n k _ {i j (t - 1)} + \alpha_ {5} T i m e E l a p s e d _ {j t} * T e a m S k i l l _ {i j} + \alpha_ {6} T e a m S i z e _ {i j} \\ & + \alpha_ {7} T e a m S k i l l _ {i j} + \delta_ {j} + \epsilon_ {i j} \end{array} \tag {1}
$$

where $\mathrm { i } , \mathrm { j } ,$ and t denote teams, contests, and time periods, respectively; $\alpha _ { k } ( k = 0 . . . 7 )$ represents the coe<sup>fi</sup>cients of the variables; and $\delta _ { j }$ denotes the contest dummies, which are included to control for the contest heterogeneity.

The dependent and explanatory variables included in this model are explained in the next section.

## 4. Data collection and variable de<sup>fi</sup>nitions

## 4.1. Data collection

As mentioned earlier, data for our study were obtained from Kaggle.com, a specialized innovation tournament platform that focuses on predictive analytics projects (Fig. 1). Kaggle has a pool of more than 100,000 data scientists coming from over 100 countries and 200 uni versities. These data scientists are experts in various quantitative <sup>fi</sup>elds, such as computer science, statistics, economics, mathematics, and physics. Over the last few years, Kaggle has served many companies, including GE, Allstate, Merck, Ford, and Facebook, and has helped them to improve sales forecasting, increase customer retention, reduce operating costs, accelerate product development, and gather information from social media (Kaggle.com).

Companies, government organizations, and researchers provide problem descriptions and relevant datasets to Kaggle and often specify the monetary reward they are willing to pay the winners. Based on these inputs, Kaggle sets up innovation tournaments or contests. Kaggle typically provides training and test datasets to the contestants. Each participant or participating team can submit multiple solutions before the contest deadline. Kaggle evaluates all submissions in real time and provides instant feedback to the participants. This feedback is displayed on a leaderboard that is open to the public. Contestants not only learn how good their models are but also get to know how smart their rivals are. Thus, these tournaments show some characteristics of all-pay auctions with complete information. Every time a solver submits a solution, the leaderboard is dynamically updated to show the current rank of solvers and the prediction accuracy score of their solution. The accuracy score and ranking are unique and serve as objective measures of solution quality, which is unavailable in most other innovation tournament initiatives. Moreover, Kaggle’s website provides each solver with an online pro<sup>fi</sup>le, which shows a solver’s personal information and overall performance score based on their <sup>fi</sup>nal rankings in previous contests (see Fig. 1).

For this study, we collected weekly leaderboard data for 25 tournaments from September 2013 to November 2014. The dataset consists of more than 10,000 teams and 73,670 observations. Tables 2 and 3 summarize the descriptive statistics and correlation matrix, respectively.

## 4.2. Dependent and independent variables

## 4.2.1. Efort

We used the number of solution submissions as a measure of team e<sup>f</sup>ort, the main dependent variable in our study. The number of submissions made within a week was used as a proxy for team e<sup>f</sup>ort in that week. Consistent with prior literature [14], e<sup>f</sup>ort was measured by taking the di<sup>f</sup>erence between the number of submissions for two consecutive weeks on the leaderboard shown in Fig. 1. In addition, we used predicted accuracy of the solution based on e<sup>f</sup>orts as an alternative measure of dependent variable in the section on robustness tests.

Table 2 Descriptive Statistics.  
Table 3 Correlation Matrix.  
![](/api/attachments/7D3R32VU/fulltext/images/5488898cd2a95da35037c975801ae7c3eee8fd4ca7e022cba8c376223fa3698f.jpg)  
Fig. 1. Screenshots of the Data Source: Kaggle.com.

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev</td><td>Min</td><td>Max</td></tr><tr><td>Team Size</td><td>1.16</td><td>0.68</td><td>1.00</td><td>24.00</td></tr><tr><td>Team Skill</td><td>33475.64</td><td>66731.47</td><td>0.00</td><td>876551.40</td></tr><tr><td>Submissions</td><td>2.14</td><td>6.49</td><td>0.00</td><td>334.00</td></tr><tr><td>Team Rank</td><td>375.73</td><td>356.29</td><td>1.00</td><td>1792.00</td></tr><tr><td>Time Elapsed</td><td>0.73</td><td>0.23</td><td>0.07</td><td>1.00</td></tr><tr><td>Std. Score</td><td>78.86</td><td>27.03</td><td>0.00</td><td>100.00</td></tr></table>

Our primary independent variables are team rank and time elapsed. Team skill was used as a moderator variable.

## 4.2.2. Time Elapsed

This is the percentage of contest time elapsed as of the current week (t).

## 4.2.3. Team Rank

This is the relative position of a team in a contest at the end of the previous week (t-1). This <sup>fi</sup>gure ranged from 1 to 1792, with a mean of 375.73.

## 4.2.4. Team skill

This is the average pro<sup>fi</sup>le score of the members in a team. Kaggle uses a formula to calculate each individual’s pro<sup>fi</sup>le score based on their performance in prior competitions. The maximum achievable score in a competition is derived from the total number of participants and the level of di<sup>fi</sup>culty of the contest. According to Kaggle, “the current formula for each competition splits the points among the team members, decays the points for lower <sup>fi</sup>nishes, adjusts for the number of teams that entered the competition, and linearly decays the points to 0 over a two-year period from the end of the competition.” Kaggle updates each individual’s skill scores after each competition. The team skill score in our dataset ranged from 0 to 877 K, with a mean of 33 K. We used a log transformation to address scaling issues.

## 4.3. Control variables

Team-speci<sup>fi</sup>c variables, such as team size and team skill, were used as controls. We used a <sup>fi</sup>xed-e<sup>f</sup>ects model to control for tournamentspeci<sup>fi</sup>c e<sup>f</sup>ects and lagged the dependent variable to control for persistency. Moreover, we re-ran the model with additional controls to control for the distance from the best score. These results are presented in the robustness tests section.

## 4.3.1. Team size

This is the number of members in a team. Previous studies [44,45] indicated that team size has an impact on team performance. The team size in our dataset ranged from 1 to 24, with a mean of 1.2.

## 4.3.2. Efort<sub>(t-1)</sub>

We also include the previous week’s e<sup>f</sup>ort (lagged dependent variable) in the model to address the persistency of e<sup>f</sup>ort variable. It is likely that, for most teams, e<sup>f</sup>orts are correlated over time due to some historical factors, such as work ethic, abilities, and other unobservable behaviors. Thus, the lagged dependent variable allows control for some team-speci<sup>fi</sup>c omitted factors.

<table><tr><td></td><td></td><td>1</td><td>2</td><td>3</td><td>5</td><td>7</td><td>8</td></tr><tr><td>1</td><td>Team Size</td><td>1.0000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Team Skill</td><td>-0.0160</td><td>1.0000</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Submissions</td><td>0.1566</td><td>0.2284</td><td>1.0000</td><td></td><td></td><td></td></tr><tr><td>4</td><td>Team Rank</td><td>-0.0758</td><td>-0.2669</td><td>-0.2663</td><td>1.0000</td><td></td><td></td></tr><tr><td>5</td><td>Time Elapsed</td><td>0.0021</td><td>-0.0330</td><td>0.1038</td><td>0.2720</td><td>1.0000</td><td></td></tr><tr><td>6</td><td>Std. Score</td><td>0.0113</td><td>0.1155</td><td>0.1663</td><td>-0.3432</td><td>0.0662</td><td>1.0000</td></tr></table>

## 4.3.3. ΔBestscore

This is the distance between the best score and the team’s score in the previous week (t-1) in a given contest. The auction literature has shown that jump bid $( \mathrm { i . e . }$ , a bid with signi<sup>fi</sup>cant increment) impacts the subsequent bidding behavior of the bidders by seriously deterring competitors through high entry cost [46,47]. Moreover, in the same setting, Wooten [31] has shown that a signi<sup>fi</sup>cantly improved solution results in an increase in subsequent e<sup>f</sup>orts of other contestants. To control for this, the deviation of the solver’s solution score from the best solution score was added to the model. We divided all values by the range to standardize scales. The distance from best score for team $i ,$ in contest j, and time (t-1) is given by

$$
\Delta B e s t S c o r e _ {i, (t - 1), j} = \frac {B e s t S c o r e _ {(t - 1) , j} - S c o r e _ {i , (t - 1) , j}}{S c o r e _ {m a x , j} - S c o r e _ {m i n , j}}\tag{2}
$$

## 5. Results

## 5.1. Negative binomial model

We used the negative binomial model for our analysis because it <sup>fi</sup>ts well with our data characteristics. Our main dependent variable is count data, and OLS regression is not appropriate because of the skewness of the data. Poisson and negative binomial models are com monly used for count data. However, our data present over-dispersion relative to the Poisson distribution. The log likelihood ratio test of alpha suggested that negative binomial distribution is superior to Poisson in this case [48,49].

Results are summarized in Table 4. Models 1 and 2 show the results without considering the lagged e<sup>f</sup>ect of the dependent variable, while Model 3 shows the results after controlling for the lagged e<sup>f</sup>ect. In both Models 1 and $^ { 2 , }$ the coe<sup>fi</sup>cients of time elapsed $( \mathbf { a } _ { 2 } = 0 . 8 9 5 , p \ < \ 0 . 0 1 ;$ $a _ { 2 } = 0 . 8 6 3 , p \ < \ 0 . 0 1 )$ and square of time elapsed $( \alpha _ { 3 } = 2 . 4 2 7$ $p ~ < ~ 0 . 0 1 ; ~ \alpha _ { 3 } = 2 . 4 4 3 , { p } ~ < ~ 0 . 0 1 )$ are positive and signi<sup>fi</sup>cant. Thus, “Timing Strategy Hypothesis $( \mathrm { H } 1 ) ^ { \dprime }$ is supported. The results suggest that solvers strategically delay their e<sup>f</sup>orts to enhance the chances of winning while reducing the cost of e<sup>f</sup>orts. The coe<sup>fi</sup>cient of the interaction e<sup>f</sup>ect of team skill and the time elapsed is positive and sig ni<sup>fi</sup>cant in both Models 2 and $3 ( \alpha _ { 5 } = 0 . 1 1 , \ p \ < \ 0 . 0 1 ; \ \alpha _ { 5 } = 0 . 1 2$ $p \ < \ 0 . 0 1 )$ . Thus, “Skill Moderation Hypothesis (H2)” is supported. Results show that strong teams strategically delay their e<sup>f</sup>orts compared to weak teams. The coe<sup>fi</sup>cient of rank is negative and signi<sup>fi</sup>cant in both models $( \alpha _ { 4 } = \mathrm { ~ - 0 . 0 0 1 } , ~ p ~ < ~ 0 . 0 1 ; ~ \alpha _ { 4 } = \mathrm { ~ - 0 . 0 0 1 }$ $p \ < \ 0 . 0 1 )$ . Thus, “Ranking Hypothesis $\mathbf { ( H 3 ) } ^ { \mathfrak { n } }$ is supported. This implies that when teams get closer to the winning position, they strategically exert more e<sup>f</sup>ort. This could be due to an increased con<sup>fi</sup>dence in winning. Our results show that the lagged dependent variable has a positive and signi<sup>fi</sup>cant impact on the dependent variable. Moreover, results suggest that all three hypotheses are supported even after con trolling for persistency.

Negative Binomial Regression Results.

<table><tr><td></td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td> $Team\ Rank_{(t-1)}$ </td><td>-0.0013 ***(0.0000)</td><td>-0.0013 ***(0.0000)</td><td>-0.0008 ***(0.0000)</td></tr><tr><td>Time Elapsed</td><td>0.8951 ***(0.0566)</td><td>0.8630 ***(0.0572)</td><td>0.7796 ***(0.0626)</td></tr><tr><td>Time Elapsed Sq</td><td>2.4267 ***(0.1919)</td><td>2.4430 ***(0.1919)</td><td>1.0177 ***(0.2446)</td></tr><tr><td>Time Elapsed*TeamSkill</td><td></td><td>0.1090 ***(0.0298)</td><td>0.1245 ***(0.0355)</td></tr><tr><td> $Effort_{(t-1)}$ </td><td></td><td></td><td>0.1621 ***(0.0027)</td></tr><tr><td>Team Skill</td><td>0.3547 ***(0.0078)</td><td>0.3565 ***(0.0078)</td><td>0.3202 ***(0.0085)</td></tr><tr><td>Team Size</td><td>0.5071 ***(0.0200)</td><td>0.5119 ***(0.0201)</td><td>0.4808 ***(0.0214)</td></tr><tr><td>Log likelihood</td><td>-107343.6</td><td>-107336.93</td><td>-75532.94</td></tr><tr><td>Observations</td><td>73670</td><td>73670</td><td>61084</td></tr></table>

\*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.1.

Table 5  
Team Skill Moderation Results

<table><tr><td>Team Skill</td><td>Time Elapsed Impact (Without Time Elapsed Sq)</td><td>Time Elapsed Impact (With Time Elapsed Sq)</td></tr><tr><td>Minimum</td><td>-0.3740 (0.2689)</td><td>-7.0695 *** (0.4297)</td></tr><tr><td>25th Percentile</td><td>0.3654 *** (0.0581)</td><td>-0.2470 *** (0.0172)</td></tr><tr><td>50th Percentile</td><td>0.4670 *** (0.0456)</td><td>0.8413 *** (0.488)</td></tr><tr><td>75th Percentile</td><td>0.5917 *** (0.0402)</td><td>0.9866 *** (0.0448)</td></tr><tr><td>95th Percentile</td><td>0.7441 *** (0.0681)</td><td>1.1641 *** (0.0821)</td></tr><tr><td>Maximum</td><td>0.9057 *** (0.1112)</td><td>1.3525 *** (0.1120)</td></tr><tr><td>Observations</td><td>73670</td><td>73670</td></tr></table>

\*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.1.

In addition, we used a bootstrap method to further evaluate the impact of the time elapsed at di<sup>f</sup>erent levels of team skill (Skill Moderation Hypothesis (H2)). Table 5 summarizes the results of bootstrap analysis. Given Eq. (1), the e<sup>f</sup>ort impact of the time elapsed can be written as

$$
\frac {\partial E f f o r t}{\partial T i m e E l a p s e d} = \hat {\alpha} _ {2} + \hat {\alpha} _ {5} T e a m S k i l l\tag{3}
$$

where αˆ signi<sup>fi</sup>es the direct impact of time elapsed on e<sup>f</sup>ort. We also expect the e<sup>f</sup>ort impact of time elapsed to be more pronounced for higher skill levels, which requires αˆ to be positive and signi<sup>fi</sup>cant. To evaluate this conditional e<sup>f</sup>ect further, we estimated the time elapsed impact on e<sup>f</sup>ort at various percentiles of TeamSkill variable. For instance, at the 25th percentile of the TeamSkill variable (without the Time Elapsed Square), we obtain the point estimate of 0.3654 for the e<sup>f</sup>ort impact of time elapsed. However, in order to know whether the estimates obtained at di<sup>f</sup>erent percentiles of TeamSkill variable are statistically signi<sup>fi</sup>cant, we also need to compute the corresponding standard errors. One can predict these standard errors by using the delta method [50], jackknife [51], or bootstrapping [52]. In this paper, we used the nonparametric bootstrap method introduced by Efron [52] that randomly resamples from our original sample of size n with replacement, obtains the bootstrapped sample of $( R _ { 1 } , R _ { 2 } , . . . . . . , R _ { n } )$ ,and computes the corresponding estimate $\hat { \delta } _ { b } \mathbf { 1 }$ from each of the B-bootstrapped samples. We then obtain the corresponding standard error as $s \hat { e } _ { \mathrm { B } } = \left\{ \sum _ { b = 1 } ^ { B } \ { [ \hat { \delta } _ { b } - \overline { { \hat { \delta } } } ] } ^ { 2 } / ( B - 1 ) \right\} ^ { 1 / }$ 2 , where $\hat { \delta } _ { b }$ is the estimate from the $b ^ { \mathrm { t h } } .$ resample $( \mathbf { b } { = } 1 , { \ldots } { \ldots } { \mathbf { , B } } )$ and $\overline { { \hat { \delta } } } = \sum _ { b = 1 } ^ { B } \hat { \lambda } _ { b } / B ,$ is the mean of the resampled values (see [53] for details).

As the results indicate, as the level of skills increases, teams tend to make more e<sup>f</sup>orts toward the end of the competition. These results are consistent with the behavior of strong players in complete information all-pay auctions. That is, strong players have an incentive to exert more e<sup>f</sup>orts toward the end of the competition. Results also indicate that teams with low skills make more e<sup>f</sup>orts at the beginning of the contest. Low-skill teams need more time to come up with a quality solution compared with high-skill teams; thus, they cannot a<sup>f</sup>ord to wait.

Furthermore, we re-ran the model including Bestscore to control for the e<sup>f</sup>ect of quality of the best solution in a given time on e<sup>f</sup>orts. As shown in Table $^ { 6 , }$ we observed that high-quality solutions (jump bids) negatively in<sup>fl</sup>uence solver e<sup>f</sup>orts. Consistent with the <sup>fi</sup>ndings in the auction literature, this observation indicates that a solution with a very high quality could be a serious deterrent to rivals, as a consequence of which they face very high entry cost (i.e., they have to put forth high e<sup>f</sup>orts).

Negative Binomial Regression Results (with ΔBestscore).

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td> $Team\ Rank_{(t-1)}$ </td><td>-0.0003 *** (0.0000)</td><td>-0.0002 *** (0.0000)</td></tr><tr><td>Time Elapsed</td><td>0.3738 *** (0.0553)</td><td>2.2630 *** (0.0561)</td></tr><tr><td>Time Elapsed Sq</td><td>2.1973 *** (0.1854)</td><td>2.2086 *** (0.1843)</td></tr><tr><td>Time Elapsed*Team Skill</td><td></td><td>0.2970 *** (0.0284)</td></tr><tr><td> $\Delta Bestscore_{(t-1)}$ </td><td>-3.9871 *** (0.0732)</td><td>-4.0888 *** (0.0742)</td></tr><tr><td>Team Skill</td><td>0.2932 *** (0.0076)</td><td>0.2979 *** (0.0076)</td></tr><tr><td>Team Size</td><td>0.4299 *** (0.0192)</td><td>0.4416 *** (0.0193)</td></tr><tr><td>Log likelihood</td><td>-105815.7</td><td>-105761.2</td></tr><tr><td>Observations</td><td>73670</td><td>73670</td></tr></table>

\*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.1.

## 5.2. Robustness tests

## 5.2.1. Seemingly unrelated regression model

Studies show that the performance of solvers is a function of their skill set as well as the e<sup>f</sup>ort they put forth [9]. Thus, enhancing either the skills or the e<sup>f</sup>orts of participants increases the chances of winning through improved quality of the solution. However, increasing the ef fort level is costly because only the winner will be entitled to a reward. Hence, solvers need to develop some strategies to increase the likelihood of winning without incurring signi<sup>fi</sup>cant cost of expending e<sup>f</sup>ort. They may achieve this by strategically allocating their e<sup>f</sup>orts.

To clarify the relationship, we identify the following statistical models, given data availability and the existing theories that explain the structural determinants of team e<sup>f</sup>ort and rank:

$$
\begin{array}{r l} E f f o r t _ {i j t} = & \alpha_ {0} + \alpha_ {1} E f f o r t _ {i j (t - 1)} + \alpha_ {2} T i m e E l a p s e d _ {j t} + \alpha_ {3} T i m e E l a p s e d _ {j t} ^ {2} \\ & + \alpha_ {4} R a n k _ {i j (t - 1)} + \alpha_ {5} T i m e E l a p s e d _ {j t} * T e a m S k i l l _ {i j} + \alpha_ {6} T e a m S i z e _ {i j} \\ & + \alpha_ {7} T e a m S k i l l _ {i j} + \delta_ {1 j} + \varepsilon_ {1 i j} \end{array} \tag {4}
$$

$$
\begin{array}{r l} \text {Rank} _ {i j t} & = \beta_ {0} + \beta_ {1} \text {Effort} _ {i j t} + \beta_ {2} \text {Rank} _ {i j (t - 1)} + \beta_ {3} \text {TeamSize} _ {i j} + \beta_ {4} \text {TeamSkill} _ {i j} \\ & + \delta_ {2 j} + \varepsilon_ {2 i j} \end{array} \tag {5}
$$

Since team e<sup>f</sup>ort and rank are expected to be driven by some common observable and unobservable variables, we model them as a set of relations. The unobservable factors or the omitted variables that may drive both e<sup>f</sup>ort and rank are part of the error terms ε and $\varepsilon _ { 2 } .$ Speci<sup>fi</sup>cally, it is likely that the information included in these omitted variables will be included in both error terms. Thus, the two equations in the system are linked, since the error term in the e<sup>f</sup>ort equation is likely to be signi<sup>fi</sup>cantly correlated with the error term in the rank equation. To identify this setup, we follow Zellner [54] and estimate a “seemingly unrelated regression” (SUR) model that allows correlated error terms. It involves a two-stage estimation procedure that is both consistent and e<sup>fi</sup>cient.

Our results from a generalized least-squares estimation indicate that residuals of the equations in the system are in fact significantly corre: lated, validating the use of SUR model to account for this correlation. Speci<sup>fi</sup>cally, given our Brusch–Pagan test statistic, we reject the null hypothesis of no correlation between error terms $\varepsilon _ { 1 }$ and $\varepsilon _ { 2 }$ at the sig ni<sup>fi</sup>cance level of 0.1.

As the results in Table 7 show, at higher levels of skill and e<sup>f</sup>ort, the ranking (relative performance) improves as well. Most importantly, the results from the equation system that considers the cross-equation correlations harmoniously support all three of our hypotheses. Thus, we conclude that solvers strategically allocate e<sup>f</sup>ort to enhance their chances of winning with a minimum cost.

Table 7  
Seemingly Unrelated Regression Results.

<table><tr><td></td><td> $Effort_t$ </td><td> $Rank_t$ </td></tr><tr><td> $Effort_t$ </td><td></td><td>-3.3380 *** (0.0464)</td></tr><tr><td> $Team\ Rank_{(t-1)}$ </td><td>-0.0027 *** (0.0000)</td><td>0.9857 *** (0.0011)</td></tr><tr><td>Time Elapsed</td><td>2.7681 *** (0.1258)</td><td></td></tr><tr><td>Time Elapsed Sq</td><td>5.1923 *** (0.4202)</td><td></td></tr><tr><td>Time Elapsed*Team Skill</td><td>0.5545 *** (0.0629)</td><td></td></tr><tr><td>Team Skill</td><td>0.9022 *** (0.0165)</td><td>-6.2682 *** (0.2113)</td></tr><tr><td>Team Size</td><td>1.5373 *** (0.0335)</td><td>-1.5501 *** (0.4289)</td></tr><tr><td>Observations</td><td>73670</td><td>73670</td></tr></table>

\*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.1.

## Table 8

Zero-In<sup>fl</sup>ated Negative Binomial Regression Results

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td> $Team\ Rank_{(t-1)}$ </td><td>-0.0010 *** (0.0000)</td><td>-0.0010 *** (0.0000)</td></tr><tr><td>Time Elapsed</td><td>0.8673 *** (0.0591)</td><td>0.7727 *** (0.0617)</td></tr><tr><td>Time Elapsed Sq</td><td>0.9170 *** (0.2442)</td><td>0.9901 *** (0.2445)</td></tr><tr><td>Time Elapsed*Team Skill</td><td></td><td>0.2032 *** (0.0366)</td></tr><tr><td> $Effort_{(t-1)}$ </td><td>0.1544 *** (0.0036)</td><td>0.1561 *** (0.0036)</td></tr><tr><td>Team Skill</td><td>0.0000 *** (0.0000)</td><td>0.0000 *** (0.0000)</td></tr><tr><td>Team Size</td><td>0.2718 *** (0.0219)</td><td>0.2842 *** (0.0223)</td></tr><tr><td>Log likelihood</td><td>-76269</td><td>-76254</td></tr><tr><td>Observations</td><td>61084</td><td>61084</td></tr></table>

\*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.1.

## 5.2.2. Zero-inflated negative binomial mode

As with many empirical count data, our dataset su<sup>f</sup>ers from the excess zero problem. The over-dispersion in the data could be a result of that. Therefore, we also ran our model using zero-in<sup>fl</sup>ated negative binomial model. Some teams may not submit their solutions frequently. This model is capable of separating out “always zero” group from “not always zero” group [49]. Table 8 summarizes the results. Model 1 shows the results without considering the interaction e<sup>f</sup>ect of team skill and time elapsed, while Model 2 shows the results including the mod eration e<sup>f</sup>ect. As shown in Table 8, all three hypotheses are supported, thus demonstrating the robustness of our results.

## 5.2.3. Efort versus team percentile

Kaggle evaluates team percentiles based on team rankings on the <sup>fi</sup>nal leaderboard (i.e., the ratio of team ranking to the maximum ranking on the <sup>fi</sup>nal leaderboard). To avoid confusion and to be consistent with de<sup>fi</sup>nitions, we rede<sup>fi</sup>ned team percentile as one minus the current value. Thus, high percentile indicates best teams and vice versa. We categorized teams into two groups based on their skill compared to median-skill, high-skill, and low-skill teams. Then, for each group, we estimate the impact of time elapsed on e<sup>f</sup>ort at di<sup>f</sup>erent levels of team percentiles using the bootstrap method. Results show that for each percentile, the e<sup>f</sup>ect of time elapsed on e<sup>f</sup>ort is high for high-skill group compared with low-skill group. Moreover, within each skill group, teams that performed well made more e<sup>f</sup>orts toward the end of the tournament (Table 9).

We categorized teams into four groups based on their performance. Then, we plotted a graph of cumulative number of submissions over time (Fig. 2). We saw di<sup>f</sup>erent submission patterns for these groups. The graphs show that winning teams (best teams) exert a considerably higher amount of e<sup>f</sup>ort toward the end of a tournament deadline by submitting more solutions. A sample graph for a contest is shown below.

Team Skill Moderation Results (Percentiles)

<table><tr><td></td><td>Low-Skill Teams</td><td>High-Skill Teams</td></tr><tr><td>25th Percentile</td><td>-0.0867 (0.1285)</td><td>0.7891 *** (0.0633)</td></tr><tr><td>50th Percentile</td><td>0.1860 (0.1312)</td><td>0.9060 *** (0.0900)</td></tr><tr><td>75th Percentile</td><td>0.4588 * (0.2531)</td><td>1.0230 *** (0.1228)</td></tr><tr><td>Observations</td><td>36835</td><td>36835</td></tr></table>

\*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.1.

![](/api/attachments/7D3R32VU/fulltext/images/63efd5649cad7749814da824b5ca50a4b97e73f2015006f145d694b32d512e14.jpg)  
Fig. 2. Cumulative E<sup>f</sup>ort over Time

## 5.2.4. Alternative measure of dependent variable

The model was re-estimated with the predicted accuracy of the solution as a function of e<sup>f</sup>ort serving as our dependent variable. Results were consistent with previous <sup>fi</sup>ndings. Table 10 summarizes the results with prediction accuracy as the dependent variable.

## 6. Discussion

## 6.1. Key findings

This study provides valuable insight into solvers’ strategic behaviors in dynamic innovation tournaments. It demonstrates that participants strategically vary their e<sup>f</sup>orts to enhance their chances of winning, while minimizing the cost of their e<sup>f</sup>orts. Our study makes several noteworthy contributions to the existing body of knowledge. First, our research found that in open innovation tournaments, solvers tend to put more e<sup>f</sup>ort toward the end of the contest. This could be to reduce the information spillovers, avoid submission wars, and/or to ensure that rivals do not have su<sup>fi</sup>cient time to respond. Furthermore, our results clearly show that strong teams exert relatively more e<sup>f</sup>orts toward the end of the competition than weak teams. Strategically delaying e<sup>f</sup>orts helps strong teams to win the competition with minimum e<sup>f</sup>ort.

## Table 10

OLS Regression Results with Estimated DV.

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td> $Team\ Rank_{(t-1)}$ </td><td>-0.0012 *** (0.0000)</td><td>-0.0012 *** (0.0000)</td></tr><tr><td>Time Elapsed</td><td>1.2807 *** (0.0563)</td><td>1.2361 *** (0.0565)</td></tr><tr><td>Time Elapsed Sq</td><td>2.1910 *** (0.1884)</td><td>2.3174 *** (0.1888)</td></tr><tr><td>Time Elapsed*Team Skill</td><td></td><td>0.2484 *** (0.0283)</td></tr><tr><td>Team Skill</td><td>0.3992 *** (0.0074)</td><td>0.4054 *** (0.0074)</td></tr><tr><td>Team Size</td><td>0.6847 *** (0.0150)</td><td>0.6907 *** (0.0150)</td></tr><tr><td> $R^2$ </td><td>12.7%</td><td>12.8%</td></tr><tr><td>Observations</td><td>73670</td><td>73670</td></tr></table>

\*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.1.

Second, our results show that interim rank disclosure in<sup>fl</sup>uences the e<sup>f</sup>ort allocation decisions of contestants. Solvers who are closer to the winners tend to exert more e<sup>f</sup>orts. One plausible explanation is that when they get closer to winning, the risk of losing is reduced and they are therefore motivated to exert more e<sup>f</sup>ort. Moreover, teams with higher rankings get more competitive.

In order to ensure that our <sup>fi</sup>ndings were robust, we ran our data using a zero-in<sup>fl</sup>ated negative binomial model to account for the excess zero issue in our dataset. We also used estimated solution accuracy as a measure of dependent variables. In addition, we ran our data using a seemingly unrelated regression model that included the relationship between e<sup>f</sup>ort and performance. The results were consistent with the main model, thus a<sup>fi</sup>rming the robustness of our results. Furthermore, we explored whether timing strategies are di<sup>f</sup>erent for di<sup>f</sup>erent teams. First, we calculated the impact of time elapsed for team with di<sup>f</sup>erent skill percentiles. Our study demonstrates that as the level of skill increases, the positive impact of time elapsed on e<sup>f</sup>ort is enhanced. Second, we categorized teams into four groups based on their perfor mance and plotted a graph of the cumulative number of submissions over time. We saw di<sup>f</sup>erent submission patterns for these groups. Though all groups, on average, tend to make more submissions toward the end of the tournament, graphs clearly showed that winning teams exert a considerably higher amount of e<sup>f</sup>ort toward the end of a tournament deadline. Third, we categorized teams by skill and their performance percentile. Results clearly show that within each skill level, winning teams exert more e<sup>f</sup>ort toward the end of the contest. The <sup>fi</sup>nding that the best teams strategically delay their e<sup>f</sup>orts to enhance their chances of winning strengthens the argument for sniping. Furthermore, our results showed evidence for persistency of e<sup>f</sup>orts. Finally, the impact of explanatory variables was signi<sup>fi</sup>cant even afte controlling for persistency in team e<sup>f</sup>orts.

Our <sup>fi</sup>ndings have several implications for theory and practice.

## 6.2. Theoretical implications

Our study is not only anchored in established conceptual foundations but also methodologically robust. Speci<sup>fi</sup>cally, our research brings together two distinct streams of research to investigate solvers’ e<sup>f</sup>ort allocation strategies in open innovation tournaments. From a theoretical perspective, it is important to investigate the combined e<sup>f</sup>ect as open innovation tournaments exhibit characteristics of both all-pay auctions (e.g., timing strategies in bidding) and tournaments (e.g., in terim rank feedbacks in sport competitions). Our study makes several contributions to the emerging literature on innovation tournaments.

First, our research extends the application of bidding strategies beyond an auction setting to an innovation tournament context. It shows evidence for the existence of sniping in dynamic innovation tournaments. Speci<sup>fi</sup>cally, consistent with <sup>fi</sup>ndings of all-pay auction in complete information settings, our study shows that strong teams exert more e<sup>f</sup>orts toward the end of innovation tournaments. Second, it ex tends the application of social comparison theory to an innovation tournament context and elucidates how interim rank disclosure a<sup>f</sup>ects the solvers’ decision with regard to the amount of e<sup>f</sup>ort to allocate. Solvers compare their performance with others and strategically alter their e<sup>f</sup>orts to increase their utility. Thus, it enriches the evolving theoretical foundation of innovation tournaments by con<sup>fi</sup>rming the transferability of timing and interim rank feedback e<sup>f</sup>ects in this con text. Furthermore, it adds to the existing body of knowledge on social comparison theory by demonstrating how its tenets can be used in an innovation tournament setting.

Third, while prior research primarily focused on blind contests where submission behaviors and interim solution quality were unobservable, our study leveraged unique data from a leading predictive analytics platform (Kaggle) that continually provided objective measures of e<sup>f</sup>orts and ranking of every team throughout the contest. This rich dataset allowed us to control for teams’ persistency, contest heterogeneity, and to use within-contest e<sup>f</sup>ort variations to assess teams strategies for exerting e<sup>f</sup>ort.

Finally, unlike prior studies that mainly focused on static one-shot interactions in innovation tournaments, our study utilizes time variant data to investigate how solvers change their e<sup>f</sup>ort allocation patterns throughout the competition based on the dynamics of the competition. Thus, our study extends the boundaries of knowledge by providing deep insight into the dynamics of innovation tournaments.

## 6.3. Managerial implications

The <sup>fi</sup>ndings of this study have several implications for tournament platform providers and solvers. Platform providers can use the results of our study to design their platforms in such a manner that they increase the likelihood of getting higher quality solutions to the problems posted by companies, researchers, and others. For instance, the insights related to the timing and level of information disclosure and feedback and how they impact e<sup>f</sup>ort allocation decisions can be particularly useful in designing a platform that engages and motivates participants throughout the contest. Speci<sup>fi</sup>cally, they could draw inspiration from games (e.g., video games) that commonly feature leaderboards, points, levels, and badges to involve participants and to encourage them to achieve higher levels [22]. Furthermore, our study demonstrates that competition intensi<sup>fi</sup>es among top rankers as only the best solution is rewarded. In order to motivate the lower performers, Kaggle and other platform designers can have a minimum standard to award badges or points that give competitors some sense of accomplishment. For example, if the competition said that the top 500 would receive some points that would establish or enhance their status on such platforms, it might motivate not just the leaders but those closer to the lower standard as well. In addition, platform providers can explore how a com bination of blind (private) and un-blind (public) disclosures may improve the solution quality. For example, if they made early feedback private and late feedback public, would that encourage strong players to submit their solutions early? Clearly, encouraging top-ranked players to submit early and often would result in superior solutions. In addition to providing feedback, platform providers may also induce participants, particularly the high-ranked ones, to submit early by providing incentives.

Our <sup>fi</sup>nding that solvers tend to put more e<sup>f</sup>orts toward the end of a tournament suggests that platform providers should perhaps explore the possibility of increasing overall e<sup>f</sup>orts by conducting contests in stages or multiple phases. The consequence of inducing contestants to expend more e<sup>f</sup>ort would be a winning solution of superior quality. However, additional research and in-depth empirical validations are needed to fully understand how these design choices impact the ultimate quality of the winning solution.

As far as solvers are concerned, the <sup>fi</sup>ndings of our study would be useful in understanding how a strategic adjustment in the level of e<sup>f</sup>ort can maximize their utility. Finally, the results of this study could help managers in organizational settings to provide a work environment that encourages employees to expend the right amount of e<sup>f</sup>ort to deliver their best performance.

## 6.4. Conclusion and future research

In a turbulent business environment characterized by hyper-competition and uncertainty, it is imperative that organizations continually and expeditiously derive actionable insights from data. Predictive modeling is at the heart of this endeavor. However, the limited resources that organizations have, coupled with a dearth of analytics talent, severely hamper an organization’s e<sup>f</sup>orts to derive value from data analytics. In order to augment their innovative capabilities, organizations crowdsource analytics solutions (e.g., machine learning and predictive modeling solutions) using popular contest platforms such as Kaggle. Given the increasing importance of such platforms, it is imperative that we study their dynamics to gain insight into what drives the participants and what factors in<sup>fl</sup>uence the quality of the winning solution.

As with many other empirical studies, our study has some limita tions. However, we believe that these shortcomings are minor and do not detract from our <sup>fi</sup>ndings or contributions in any way. Furthermore, being aware of these limitations gives us an opportunity to pursue further research to gain a deeper understanding of the innovation tournament context. First, our data only include information that is publicly available on the website. For instance, we do not observe participants’ real e<sup>f</sup>orts, and the number of submissions was used as a proxy for e<sup>f</sup>ort. Future research should de<sup>fi</sup>nitely consider a more expanded measure of e<sup>f</sup>ort. Additional methods, such as follow-up surveys, may also a<sup>f</sup>ord richer data, which, in turn, can lead to keener insights.

Second, our results are based on data from a speci<sup>fi</sup>c type of tour nament platform. Given the rapid development in innovation tournaments applications, richer data and cases will become available to enable further research on participants’ strategic behaviors and their implications for di<sup>f</sup>erent tournament settings. Finally, future studies may investigate the e<sup>f</sup>ects of gami<sup>fi</sup>cation (e.g., [22]) in the context of innovation tournaments. For example, would mechanisms commonly employed in games, such as leaderboards, points, badges, and levels, to name but a few, have the desired e<sup>f</sup>ect of persuading participants to expend more e<sup>f</sup>ort and produce superior solutions?

Our study is a small but important step toward providing insights that will enable providers such as Kaggle to design platforms that will engage and motivate participants to perform at their best level to deliver superior solutions. In addition, it is a useful benchmark for future studies that attempt to shed more light on the dynamics of innovation tournament platforms that organizations are increasingly turning to fo creative solutions to their challenging business analytics problems.

## References

[1] J.O. Wooten, K.T. Ulrich, Idea generation and the role of feedback: evidence from <sup>fi</sup>eld experiments with innovation tournaments, Prod. Oper. Manag. 26 (2017) 80 99.

[2] M.K. Poetz, M. Schreier, The value of crowdsourcing: can users really compete with professionals in generating new product ideas? J. Prod. Innov. Manag. 29 (2012) 245-256.

[3] K. Boudreau. C.E. Helfat. K.R. Lakhani, M.E. Menietti, Field evidence on individua

behavior & performance in rank-order tournaments, Harv. Bus. Sch. Work. Pap. (2012), https://dash.harvard.edu/handle/1/9502862.

[4] A. Vance, Fight club for geeks, Bus. Week (2012) 37–38.

[5] I. Dissanayake, J. Zhang, B. Gu, Task division for team success in crowdsourcing contests: resource allocation and alignment e<sup>f</sup>ects, J. Manag. Inf. Syst. 32 (2015) 8–39.

[7] K.J. Boudreau, N. Lacetera, K.R. Lakhani, Incentives and problem uncertainty in innovation contests: an empirical analysis, Manag. Sci. 57 (2011) 843 863.

[8] D. Liu, X. Geng, A.B. Whinston, Optimal design of consumer contests, J. Mark. 71 (2007) 140 155.

[9] C. Terwiesch, Y. Xu, Innovation contests open innovation, and multiagent problem solving, Manag. Sci. 54 (2008) 1529 1543.

[10] Y. Yang, P.Y. Chen, P. Pavlou, Open innovation: strategic design of online contests, Proc. 20th Workshop Inf. Syst. Econ, Association for Information Systems, Atlanta, GA, 2009, pp. 14–15.

[11] N. Archak, Money, glory and cheap talk: analyzing strategic behavior of contestants in simultaneous crowdsourcing contests on TopCoder.com, Proc. 19th Int. Conf. World Wide Web, Association for Computer Machinery, New York, 2010, pp. 21 30.

[12] B.L. Bayus, Crowdsourcing new product ideas over time: an analysis of the Dell IdeaStorm community, Manag. Sci. 59 (2013) 226 244.

[13] Y. Huang, P. Singh, K. Srinivasan, Crowdsourcing Blockbuster ideas: a dynamic structural model of ideation, Proc. 32nd Int. Conf. Inf. Syst. Atlanta, GA, 2011, pp. 19–22.

[14] J. Mo, Z. Zheng, X. Geng, Winning Crowdsourcing Contests: A Micro-Structura Analysis of Multi-Relational Networks., In: Harbin, China, (2011).

[15] Y. Yang, P.Y. Chen, R. Banker, Impact of past performance and strategic bidding on winner determination of open innovation contest, Proc. 21 St Workshop Inf. Syst. Econ. Association for Information Systems, Atlanta, GA, 2010, pp. 11–12.

[16] K. Girotra, C. Terwiesch, K.T. Ulrich, Idea generation and the quality of the best idea, Manag. Sci. 56 (2010) 591–605.

[17] D. Liu, X. Li, R. Santhanam, Digital games and beyond: what happens when players compete, MIS Q. 37 (2013) 111–124.

[18] K.A. Konrad, W. Leininger, The generalized stackelberg equilibrium of the all-pay auction with complete information. Rey. Econ. Des. 11 (2007) 165–174.

[19] T.X. Liu, J. Yang, L.A. Adamic, Y. Chen, Crowdsourcing with all-pay auctions: a <sup>fi</sup>eld experiment on Taskcn, Manag. Sci. 60 (2014) 2020–2037.

[20] L. Festinger, A theory of social comparison, Hum. Relat. 7 (1954) 117–140.

[21] S.M. Garcia, A. Tor, R. Gonzalez, Ranks and rivals. A theory of competition, Pers. Soc. Psychol. Bull. 32 (2006) 970–982.

[22] J. Simões, R.D. Redondo, A.F. Vilas, A social gami<sup>fi</sup>cation framework for a K-6 learning platform, Comput. Hum. Behav. 29 (2013) 345–353.

[23] C. Genakos, M. Pagliero, Interim rank risk taking, and performance in dynami tournaments, J. Polit. Econ. 120 (2012) 782 813.

[24] H. Yin, H. Zhang, Tournaments of <sup>fi</sup>nancial analysts, Rev. Account. Stud. 19 (2014) 573-605.

[25] J. Bockstedt, A. Mishra, C. Druehl, Do Participation Strategy and Experience Impact the Likelihood of Winning in Unblind Innovation Contests, (2011) http://papers. ssrn com/abstract= 1961244

[26] K.J. Boudreau, N. Lacetera, M. Menietti, Performance responses to competition across skill levels in rank-order tournaments: field evidence and implications for tournament design. Rand J. Econ, 47 (2016) 140–165

[27] L. Jian, Z. Li, T.X. Liu, Simultaneous versus sequential all-pay auctions: an experi mental study, Exp. Econ. (2016) 1–22, http://dx.doi.org/10.1007/s10683-016- 9504-1.

[28] J. Bockstedt, C. Druehl, A. Mishra, Heterogeneous submission behavior and its Implications for success in innovation contests with public submissions, Prod. Oper. Manag. 0 (2016) 1 20.

[29] L. Chen, D. Liu, Comparing Strategies for Winning Expert-Rated and Crowd-Rated Crowdsourcing Contest, (2012) http://aisel.aisnet.org/amcis2012/proceedings/ VirtualCommunities/16

[30] A. Al-Hasan. LH. Hann. S. Viswanathan, Information Spillovers and Strategic Behaviors in Open Innovation Crowdsourcing Contests: An Empirical Investigatior (n.d.), (2017) Retrieved from https://pdfs.semanticscholar.org/fcea/ 623f6c9ec21f975c710cf6e75d9d74af3eb3.pdf.

[31] J.O. Wooten, Leaps in Innovation: The E<sup>f</sup>ect of Discontinuous Progress in Algorithmic Tournaments, (2013) http://ssrn.com/abstract=2376350.

[32] S.M. Garcia, A. Tor, T.M. Schi<sup>f</sup>, The psychology of competition: a social comparison perspective, Perspect, Psychol, Sci., 8 (2013) 634–650.

[33] T. Teubner, M. Adam, R. Riordan, The impact of computerized agents on immediate emotions, overall arousal and bidding behavior in electronic auctions, J. Assoc. Inf. Svst. 16 (2015) 838–879.

[34] G. Azmat, N. Iriberri, The importance of relative performance feedback information: evidence from a natural experiment using high school students, J. Public Econ 94 (2010) 435 452.

[35] R.L. Hannan, R. Krishnan, A.H. Newman, The e<sup>f</sup>ects of disseminating relative performance feedback in tournament and individual performance compensation plans, Account. Rev. 83 (2008) 893 913.

[36] S.E. Taylor, M. Lobel, Social comparison activity under threat: downward evaluation and upward contacts, Psychol. Rey, 96 (1989) 569–575.

[37] I. Barankay, Rankings and Social Tournaments: Evidence from a Field Experiment, (2010) http://www8.gsb.columbia.edu/rt<sup>fi</sup>les/CDA%20Strategy/Barankay%20- %20Rankings%20and%20Social%20Tournaments%20MS.pdf.

[38] P. Casas-Arce, F.A. Martínez-Jerez, Relative performance compensation contests, and dynamic incentives, Manag. Sci. 55 (2009) 1306–1320.

[39] F. Ederer, Feedback and motivation in dynamic tournaments, J. Econ. Manag. Strategy 19 (2010) 733–769.

[40] T. Eriksson, A. Poulsen, M.C. Villeval, Feedback and incentives. Experimental evidence, Labour Econ. 16 (2009) 679–688.

[41] D. DiPalantino, M. Vojnovic, Crowdsourcing and all-pay auctions, Proc. 10th ACM Conf. Electron. Commer. ACM, New York, 2009, pp. 119–128.

[42] A.E. Roth, A. Ockenfels, Last minute bidding and the rules for ending second price auctions: evidence from eBay and amazon auctions on the internet, Am. Econ. Rev. 92 (2002) 1093 1103.

[43] W. Guo, Exploring and Modeling of Bidding Behavior and Strategies of Onlin Auctions, ProQuest Dissertations Publishing, University of Maryland, 2013http:// drum.lib.umd.edu/bitstream/handle/1903/14125/Guo\_umd\_0117E\_14236.pdf? sequence=1&isAllowed=y.

[44] R. Guimera, B. Uzzi, J. Spiro, L.A.N. Amaral, Team assembly mechanisms determine collaboration network structure and team performance, Science 308 (2005) 697–702.

[45] S.G. Cohen, D.E. Bailey, What makes teams work: group e<sup>f</sup>ectiveness research from the shop <sup>fl</sup>oor to the executive suite, J. Manag. 23 (1997) 239 290.

[46] E.T. Bradlow, Y.H. Park, Bayesian estimation of bid sequences in internet auctions using a generalized record-breaking model, Mark. Sci. 26 (2007) 218–229.

[47] X. Cui, V.S. Lai, Bidding strategies in online single-unit auctions: their impact and satisfaction, Inf. Manag. 50 (2013) 314–321.

[48] A.C. Cameron, P.K. Trivedi, Regression Analysis of Count Data, Econometric Society Monograph No.30, Cambridge University Press, 1998.

[49] R. Martinez-Espineira, Adopt a hypothetical pup: a count data approach to the valuation of wildlife, Environ. Resour. Econ. 37 (2007) 335–360.

[50] A.R. Gallant, A. Holly, Statistical inference in an implicit nonlinear, simultaneous equation model in the context of maximum likelihood estimation, Econometrica 48 (1980) 697–720.

[51] M.H. Quenouille, Notes on bias in estimation, Biometrika 4 (1956) 353–360.

[52] B. Efron, Bootstrap another look at the jackknife. Annu. Stat. 7 (1979) 1–26.

[53] M. Yaşar, C.J.M. Paul, Capital-skill complementarity, productivity and wages: evidence from plant-level data for a developing country. Labour Econ. 15 (2oo8) 1–17.

[54] A. Zellner, D.S. Huang, Further properties of e<sup>fi</sup>cient estimators for seemingly unrelated regression equations. Int. Econ. Rev. 3 (1962) 300–313.

Indika Dissanayake is an Assistant Professor of Information Systems and Supply Chain Management at the Bryan School of Business and Economics, the University of North Carolina Greensboro. She received her Ph.D. in Information Systems from the College of Business Administration. the University of Texas at Arlington. Her research interests include crowdsourcing, social media, and virtual communities. Her research has appeared in journals and conference proceedings such as Journal of Management Information Systems, International Conference on Information Systems, Americas Conference on Information Systems, Decision Science Institute, and Hawaii International Conference on System Sciences.

Jie (Jennifer) Zhang is an Associate Professor of Information Systems at the College of Business Administration, the University of Texas at Arlington. She received her Ph.D. in Computer Information Systems from the William E. Simon Graduate School of Business at the University of Rochester. She employs analytical and empirical techniques to examine a number of issues in ecommerce, software licensing, online reputation systems, web analytics, and social media. Her research appears in MIS Quarterly, Information Systems Research, Journal of Economics and Management Strategies, Journal of Management Information Systems, Communications of the ACM, and others.

Mahmut Yasar is an Associate Professor of Economics at the College of Business Administration, the University of Texas at Arlington (UTA). He is also an Adjunct Professor of Economics at the Emory University, and the Zhongnan University of Economics and Law in China. Before coming to UTA. he taught at the Goizueta Business School Department of Finance and the Department of Economics at the Emory University from 2003 to 2007. Dr. Yasar's primary research interests center around the microeconomics of trade and investment, productivity, knowledge and technology transfer, innovation, and applied micro-econometrics. He has also worked on issues in environmental economics and corporate <sup>fi</sup>nance. His research has appeared in journals such as Journal of Business and Economic Statistics, Journal of International Economics, and Weltwirtschaftliches Archiv. He has served as an Associate Editor of the International Economic Journal.

Sridhar Nerur is a Professor of Information Systems at the University of Texas at Arlington. He holds an engineering degree in electronics from the Bangalore University, a PGDM (MBA) from the Indian Institute of Management, Bangalore, India, and a Ph.D. in business administration from the University of Texas at Arlington. His research has been published in MIS Quarterly, Strategic Management Journal, Communications of the ACM, Communications of the AIS, The DATA BASE for Advances in Information Systems, European Journal of Information Systems, Information Systems Management, and Journal of International Business Studies. He has served as an Associate Editor of the European Journal of Information Systems and was on the editorial board of the Journal of AIS until December 2016. His research and teaching interests include social networks, machine learning, text analytics, cognitive aspects of design, dynamic IT capabilities, and agile software development.
