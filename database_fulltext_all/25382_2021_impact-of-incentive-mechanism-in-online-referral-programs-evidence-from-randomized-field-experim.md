---
otero_id: 25382
otero_key: "NVS77X3F"
title: "Impact of Incentive Mechanism in Online Referral Programs: Evidence from Randomized Field Experiments"
authors: "Jaehwuen Jung; Ravi Bapna; Alok Gupta; Soumya Sen"
year: "2021"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2021.1870384"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of Incentive Mechanism in Online Referral Programs: Evidence from Randomized Field Experiments

Jaehwuen Jung, Ravi Bapna, Alok Gupta & Soumya Sen

To cite this article: Jaehwuen Jung, Ravi Bapna, Alok Gupta & Soumya Sen (2021) Impact of Incentive Mechanism in Online Referral Programs: Evidence from Randomized Field Experiments, Journal of Management Information Systems, 38:1, 59-81, DOI: 10.1080/07421222.2021.1870384

To link to this article: https://doi.org/10.1080/07421222.2021.1870384

![](/api/attachments/NVS77X3F/fulltext/images/a3aef21c3e310c203eae9b672d32c0aebe1b579a1356f813c729bc8365c0a212.jpg)

\+ View supplementary material

![](/api/attachments/NVS77X3F/fulltext/images/79e9cacb0c5c3a2fc6631dd46c3739723f117cbac8b66aa7a8ed896823ed8266.jpg)

Published online: 02 Apr 2021.

![](/api/attachments/NVS77X3F/fulltext/images/d92a2d83ab263a684cd177364bacee9509190c6efa10d730f6a6e911fad806f7.jpg)

Submit your article to this journal

![](/api/attachments/NVS77X3F/fulltext/images/3d0835ed034944974f72c84dc341426fab7600e421d543dd90181fc9dbafe6c8.jpg)

Article views: 80

![](/api/attachments/NVS77X3F/fulltext/images/e09db59362858c16c1e17c8aeedac07c0006abb6bc926ab93b976b8c6e00a429.jpg)

View related articles

![](/api/attachments/NVS77X3F/fulltext/images/37d9b5fcb8286f1e8f289c43a3668304a9ff1b84ac032d575e07ad9ef3f7c6f5.jpg)

View Crossmark data

Check for updates

# Impact of Incentive Mechanism in Online Referral Programs: Evidence from Randomized Field Experiments

Jaehwuen Jung<sup>a</sup>, Ravi Bapna<sup>b</sup>, Alok Gupta<sup>b</sup>, and Soumya Sen<sup>b</sup>

<sup>a</sup>Department of Management Information Systems, Fox School of Business, Temple University Philadelphia, PA, USA; <sup>b</sup>Information & Decision Sciences Department, Carlson School of Management, University of Minnesota, Minneapolis, MN, USA

## ABSTRACT

Despite the growing popularity of online referral programs, a minimal amount is known regarding the theoretical foundations that drive the key actions associated with successful referrals. In this paper, we study which type of referral reward structure is most efective in maximizing word-of-mouth by conducting two randomized experiments in mobile gaming context. Specifically, we examine the efect of three incentive schemes: selfish reward (inviter gets all the reward), equal-split reward (50-50 split), and generous reward (invitee gets all the reward). Consistent across the two experiments, we find that pro-social referral incentive schemes, namely the equal-split and generous schemes, tend to dominate purely selfish schemes in creating WOM. Our mechanism-level analysis shows that both equal-split and generous schemes result in higher number of conversions by significantly increasing the invitee’s likelihood to accept referrals, which we further show that is partially due to selective and better targeted referrals. Our results contribute to the understanding of the optimal design of online referral programs and provide important implications for designing efective referral reward schemes in the digital world.

## KEYWORDS

Social contagion; viral marketing; referral incentives; eWOM; online referrals; online incentives; mechanism design

## Introduction

The massive growth in online social networking has revitalized academic interest in the power of social contagion as a force for individual and collective action. Many researchers have moved toward large-scale, in-vivo randomized field experiments to causally identify peer efects [3, 6] in online social networks, a significant scientific challenge with purely observational data. This new wave of literature gives us confidence that peer-efects are “atwork” in the general population of users in online social networks.

Having established the causal existence of peer efects, it becomes natural to evolve towards asking how we can create, perhaps even maximize, social contagion using specific mechanisms that may be at work in creating social contagion. This question is the focus of this paper. In particular, we study which type of incentive design is most efective in maximizing word-of-mouth (WOM, hereafter) based awareness and adoption of a digital product. Note that while peer influence works through a variety of mechanisms such as imitation, status seeking, creating awareness, explicit or tacit persuasion, observational or social learning, we focus on friends inviting friends either through ofline or online WOM. This focus reflects our belief that it is an important, possibly dominant<sup>1</sup> social contagion mechanism, [4] and that ofline WOM has the additional challenge that it has traditionally been hard to measure, as it does not lend itself to digitization. We detail how we overcome this challenge when we present the institutional context of our paper.

The broad category of economic incentives we examine fall under the label of what are known as referral rewards. In this incentive structure, a firm typically invites an existing customer to “refer” (bring in) another customer and ofers a reward to the referring customer. Such rewards can be monetary or cosmetic (e.g., status, badges) incentives to existing users for engaging in WOM, thereby increasing adoption of the product among their friends. For instance, Dropbox provides an extra 500MB of space to users for every instance in which a user refers new customers.<sup>2</sup> Groupon also ofers a user \$10 Groupon Bucks<sup>3</sup> (which can be used toward any purchase on the website) when a user refers a new customer and that new user makes their first purchase within certain number of hours. Other companies, such as Lyft, have tried referral schemes in which both a new customer and her inviter each receive compensation, for example, for Lyft, both parties received \$5.<sup>4</sup> In contrast, Blue Apron, an online meal subscription service, has a diferent referral reward strategy that allows existing users to send a free box of gourmet food to a friend who is not yet a user of the service.

Although these diferent schemes are being widely used in practice, their eficacy remains an open question. Scott Cook, CEO of Intuit, while speaking on their ad-hoc approach to designing referral reward schemes said:

. . . We’ve tried various artificial stimulants to word-of-mouth, like financial incentives to recommenders. None have worked. Some produced isolated, but surprising, negative reaction: “I don’t sell my friends for a bit of cash”<sup>6</sup> .

This begs the design of a systematic study of efectiveness of these diferent incentive schemes on generating WOM.

Our research design involves manipulations of how the monetary reward is shared between the inviter and the invitee of the referral. In particular, we are interested in the tradeofs between incentivizing the inviter of the referral and the invitee of the referral. Successful referrals are contingent on positive actions from both the inviter and the invitee (i.e., sending and accepting referrals, respectively). Both conventional wisdom and the observed norm in practice suggest incentivizing inviters to stimulate their act of referring. However, this can be counter-productive because when inviters are driven by extrinsic financial incentives, they may refer diferently than they would organically (e.g., care about friends’ payof) [17], which can lower the conversion rate of referrals. In addition, it may also decrease inviter’s likelihood to initiate a referral as inviter may feel guilt from getting a reward for referring their friends [29], especially when the reward is given solely to the inviter.

In contrast, there is also reason to believe that sharing a reward to the invitee may increase the efectiveness of WOM-based adoption. On the inviter side, once she realizes the invitee gets a reward for a referral, it may reduce her psychological cost of gaining referral rewards (if any) and motivate her to put more efort in finding invitee with a better match [33]. However, in exerting more efort, the inviter can become selective in sending referrals only to those friends with aligned interests [24], leading to fewer referrals as it becomes harder for the inviter to identify the right invitees. This potential downside of such selective referrals, however, can be counterbalanced together with rewards for the invitee to result in higher conversion rate [23]. Given these tradeofs, it is not clear which referral incentive design would lead to more referrals and better outcomes.

Our experimental design is motivated by multiple theories from economics and sociology. Our initial motivation comes from seminal research in economics that places individuals into three categories based on their self and other regarding preferences [2]. These categories reflect a person’s disposition to 1) be purely self-regarding, 2) care about others but not more than they care about themselves, and 3) have preferences that are substitutable between themselves and others. In line with this finding of Andreoni and Miller [2] and our aforementioned theoretical predictions, we test three diferent incentive schemes: a) the “selfish” reward scheme, where the inviter gets the reward, b) the “equal-split” reward scheme, where the inviter and the invitee split the reward equally, and c) the “generous” reward scheme, where the entire reward is given to the invitee. We explore this research question using two randomized field experiments that examine the efect of ofline and online WOM.

To conduct the experiments, we partnered with two companies that specialize in developing social gaming applications. These companies are of particular interest because their products are digital versions of popular board games, which highlight two important directions in which the digital goods have been evolving—mobile and social. The widespread adoption of mobile devices like smartphones and tablets has led to a burgeoning market for mobile applications, particularly gaming applications. The social interaction component embedded in the design of these games is a main reason for their growing popularity [15].<sup>7</sup> As the mobile gaming market continues to grow, the particular context of this study itself becomes more important market to investigate the question of how to structure the referral rewards to generate the adoption of games through WOM.

In Experiment 1, we deploy a field experiment to measure ofline WOM as a driver for the difusion of digital goods. This is available because the app’s design does not provide an online invitation feature; instead, it relies on players carrying out ofline (i.e., verbal) invitations to friends who gather at the same physical location to play the game. Next, Experiment 2 is designed to test the efect in the similar context of social mobile gaming, but with online WOM. It also helps us to better understand the underlying mechanisms, as we are unable to digitally track the users fully through the referral process in Experiment 1.

Our main finding in this paper, consistent across two experiments, is that pro-social referral incentive schemes, namely the equal-split and generous schemes described above, tend to dominate purely selfish schemes in creating WOM in the context of social games. Specifically, both equal-split and generous schemes lead to significantly larger number of conversions compared to the control group and selfish group, with the generous scheme having a higher (but not statistically distinguishable) efect than the equal-split scheme. The fact that the generous scheme maximizes the number of conversions adds to the body of evidence [2, 14, 25] against the purely rational theories of self-maximizing economic agents. When examining the efect of treatments on the senders’ decision to initiate referrals, we find that subjects in the selfish reward scheme sent the lowest number of referrals. This finding suggests that only incentivizing inviters may increase inviters’ psychological cost due to feelings of guilt in sending out referrals to friends and benefitting from it [29]. Regarding the equal-split and generous schemes, we find that while they do not significantly increase the number of referrals compared to the control group, conditional on sending a referral, invitees who received referral from those groups were significantly more likely to accept the invitations.

To further understand whether the high conversion rate is solely due to incentives given to the invitees or together with inviters efort to find a better match, we conduct additional analysis using inviter’s experience with the app and find supportive evidence that pro-social scheme also motivates inviters to exert more eforts to find a better potential invitee than other incentive schemes. Overall, the eficacy of the generous referral scheme shows the existence of pro-social behavior in social referral networks and lends credence to the theory that user happiness from pro-social spending and actions can dominate egocentrism in the online world [25]. These results have significant implications for the design of viral incentive systems for efective marketing of digital products.

Our research is among the first to directly test the efectiveness of diferent incentive schemes in stimulating social contagion through WOM-based adoption using two randomized field experiments. This work complements two streams of prior research on viral marketing [8]: estimating causal peer influence in networks, and constructing referral incentive schemes to promote WOM-based adoption. While there have been recent studies estimating causal peer influence in networks [3, 6], as well as analytical and experimental studies in optimal referral literature and WOM [24, 28, 29, 33, 35], there has been less work on how to use viral incentives to create contagion. We contribute to these research streams by empirically examining the impact of diferent incentive designs through two randomized field experiments and exploring the mechanisms behind those efects.

## Literature Review

## Social Contagion

Causal identification of how peer efects drive social contagion in the general population of users in online social networks has been of much interest to both academics and practitioners [7, 22]. However, identifying social contagion efects are methodologically dificult because user characteristics and behavior tend to cluster in online social network [3]. Randomization is an efective method for identifying social efects from homophily mechanisms and other confounders and can help to clearly estimate causal peer influence in networks. Recent research eforts have therefore focused on overcoming the challenges of analyzing purely observational data by using large-scale in-vivo randomized field experiments to causally identify the presence of peer efects [3, 6]in online social networks. Aral and Walker [3]focus on studying the efectiveness of diferent viral product design features in creating peer influence and social contagion in new product difusion by conducting a randomized block design field experiment on users of Facebook. Bapna and Umyarov [6] conduct a randomized field experiment in the context of a freemium social network to find the causal relationship of peer efect on premium subscriptions. Specifically, they distribute a premium subscription gift to randomly selected users, which work as an exogenous random assignment of a treatment to a subset of the population, and observe whether being connected to the users that received the premium service increases the likelihood of acquiring this service.

Although these previous studies have established the causal existence of peer efects, empirical evidence of what mechanisms drive behavioral contagions in social networks and how can we promote such contagion is still lacking [31]. Social contagion may be driven by a combination of diferent kinds of possible mechanisms such as awareness raising, explicit or tacit persuasion, observational or social learning [5, 16, 28], or imitation, among others [11].

Another important, possibly dominant mode of social contagion mechanism is WOM [18]. Individuals can exercise peer efect by sharing their overall experience and satisfaction level of the product. This WOM can change peers’ understanding of the product as well as peers’ expectations of utility function in two ways. Peers might change their behavior because they become aware of the existence of the product or be persuaded of the benefits of the product they already know [3, 10]. Therefore, firms are finding ways to interact with customers to manage WOM [20, 27]. Traditionally it has been hard to measure ofline WOM as it does not lend itself well to digitization. Our study adds to the literature on social contagion by focusing on ofline WOM as a mechanism for spreading awareness about a new product, and exploring how it can be stimulated by the design of economic incentives.

## Referral Program and Incentive Design

Several studies have recognized the importance of carefully managing referral programs to stimulate WOM.<sup>8</sup> Biyalogorsky et al. [9] develop an analytical model in which a customer’s delight level with the product causes referrals and identified conditions under which a referral reward is more efective than price reduction in enhancing a firm’s profitability. Van den Bulte et al. [33] examine the role of better matching and social enrichment as a mechanism in a customer referral program. Schmitt et al. [30] document that referred customers have 16–25 percent higher customer lifetime value compared to customers acquired from other channels. Based on the idea of social motives, Kornish and Li [24] establish a compensatory model in which inviters explicitly care about their friends satisfaction with their recommendations rather than their own delight with the product. Wirtz and Chew [35] and Ryu and Feick [29] investigate the efectiveness of referral bonuses in experimental settings. Wirtz and Chew [35] examine the role of incentive, deal proneness, satisfaction, and tie strength on WOM. Ryu and Feick [29] study the relationship between referral rewards and tie strength. They find that rewards are particularly efective in increasing referral, especially for weak ties and weaker brands.

Although these studies examine the efect of referral incentive design on WOM, a key limitation has been that these were conducted purely in a lab environment. Hong et al. [21] overcomes some limitations of the lab environment by designing a field experiment with an online retailer. They show how tie-strengths can afect the efectiveness of equally split incentives on the success of online referrals. In a similar context, Jung et al. [23] studies how the design of a call-to-action afects the success of online referrals in an equal-split incentive scheme.

Our approach difers from these previous works in that our experiment design allows us to capture ofline WOM—a key mechanism for referrals—as well as diferent incentive schemes that are absent in earlier experimental settings. Additionally, the referral schemes used in the previous works are based on diferent proportions of the incentive split, but they consider neither the purely selfish reward (inviter gets all of the incentive) nor the purely generous reward (invitee gets all of the incentive) schemes that are used in practice today. To the best of our knowledge, this is the first study that reports on the impact of incentive design on the WOM-based adoption among real users of a digital good using two randomized field experiments.

## User Behaviors and Incentive Design

The incentive structure of customer referral programs determines how the reward is divided between the inviter who makes a referral and an invitee (new customer) who accepts it. Recent studies from behavioral economists suggest that this division of incentive can greatly influence the outcome of the referral program because inviters exhibit three types of behavior: generosity, equity seeking, or selfishness. In an experiment setting, Andreoni and Miller [2] show that while only quarter of subjects reveal selfish behavior, the rest of subjects exhibit a significant degree of rationally altruistic behavior. Moreover, they demonstrate that almost half of the participants’ behavior was consistent with one of the three CES utility functions: perfectly selfish, perfect substitutes, or Leontief. Those with Leontief preferences always divided the surplus equally while those with perfect substitute preferences either act generously or selfishly depending on the price of giving. This observation provides the theoretical foundation for our experiment design in which we have explored these three reward-referral mechanisms: selfish reward (inviter gets the whole reward), equal reward (the reward is split equally between the inviter and invitee), and generous reward (invitee gets the whole reward).

On the one hand, there is no clear consensus emerging from the prior literature regarding which of these incentives schemes would maximize adoption of the product through referrals. Dunn and Norton’s research on pro-social happiness efect dictates that people are happier when they spend money on others [14], which implies that referral reward programs may benefit from tapping into the pro-social, “generous,” guilt-free incentive condition by giving the entire reward to the invitee. Equity theory says that individuals seek equity and fairness in what they give and receive from others [34], which suggests that a split condition that gives “equal” reward to the inviter and invitee may be an efective referral mechanism. Lastly, rational choice theory denotes that the reward should be given to an inviter in order to kick-start this referral process. That is, by tapping into the “selfish,” reward-seeking behavior of users, marketers can mobilize them to refer and recruit more friends to adopt the product. Ahrens et al. [1] conduct a field experiment in an online shopping mall with e-referrals and find that inequity between the inviter and invitee’s reward amount favors the inviter to enhance WOM.

On the other hand, some theories predict that providing incentive only to the inviters can prevent referrals. For example, metaperception theory denotes that giving incentive can prevent referrals when the incentive for referral is rewarded only to the inviter. Metaperception refers to the process by which people make decisions based on what the person perceives that others think of them or their behaviors [26]. According to metaperception theory, in a non-incentivized WOM setting, inviters will perceive themselves as performing a good action and believe that the invitees too would judge it that way. However, in an incentivized referral situation in which a referral is rewarded only to the inviter, an inviter may think that the invitee will perceive this referral as being driven by a desire to get the reward rather than an intrinsic motivation of inviting a friend (e.g., Wirtz et al. [36]), which would increase the inviter’s psychological cost of feeling guilty about gaining referral rewards [29]. In the latter case, the probability of referral would likely decrease.

It is dificult to reconcile these difering viewpoints regarding the eficacy of the diferent incentive schemes in the absence of a robust, randomized experimental design. In this paper, we conduct two randomized field experiments to address this issue, namely how to structure such incentives (i.e., divide it between the inviter and the invitee) to increase adoption of digital goods, in our case a mobile social game app, through referrals. Our work enriches the literature on viral incentive design by providing an empirical analysis of these diferent referral reward schemes and presents a first step in the efort toward deriving greater consensus on this topic.

## Experiment 1

## Institutional Details: Mobile Social Games with Ofline WOM

For Experiment 1, we collaborate with a U.S. mobile game developing company that has created a social party game that is played in a communal environment.<sup>9</sup> The application is a multi-player quiz game in which each player takes turn to ask funny questions from a pack of content cards and other players get to choose answers from a set of preloaded options, and earn points for best answers. Sample screenshots from the game are shown in Figure 1. In addition to content cards, the game also has a number of cosmetic features to enhance interaction among players (e.g., screen avatars, like and dislike options). The game was released on both Android and iOS app stores for free.

All players must be co-located when they play the game. Thus, users who discover and directly download the game from the app store have to personally invite their friends to play the game. Additionally, the company does not provide a feature for initiating online referrals in this app, making ofline WOM, such as face-to-face invitations to join the game, the key mechanism driving product adoption. The app uses a geo-sensing feature to add co-located players<sup>10</sup> to the game and to help new players explicitly identify their inviters. Specifically, the screen to attribute an invitation appears at the beginning of the first game played by a user if said user’s account was created within the last hour and has never played the game before. The invitation attribution screen is dynamically populated with a list of co-located users with whom this new user can play the first game and from which he/she can select the inviter. Conversely, if a user discovers and downloads the app on her own, and hence, do not play their first game within an hour of downloading the app, she will not see the invite attribution screen.<sup>11</sup> The reason—based on our conversations with the CEO of the gaming company—is that it is unlikely that the user will manage to find or convince at least two other users to download, install, sign up, and play the first game all within an hour.

![](/api/attachments/NVS77X3F/fulltext/images/e9a8fe90691566856ef9298d8797e552025da8ded0e53c42029a7876e6420105.jpg)  
Figure 1. Screenshots of the mobile game app (Experiment 1).

## Experimental Design

As previously mentioned, we designed the randomized field experiment to study which of the three key referral reward structures, namely selfish (inviter gets the entire incentive), equal-split (incentive is equally divided), and generous (invitee gets the entire incentive), maximizes WOM-based adoption. Specifically, when a user downloads or updates the app during the experiment period, she is randomly assigned to one of the five groups of the experiment according to the probabilities displayed in Table 1. Three of these groups were test groups defined by their referral reward structure: selfish (inviter gets the entire incentive), equal-split (incentive is equally divided), and generous (invitee gets the entire incentive).<sup>12</sup> Users in all these groups got reminder notifications to invite their friends to play with and to get rewarded according to the incentive structure on ofer for that user’s group.

The other two were control groups: one group with no reminders to invite new players and no reward (C1), and a second group with reminders but no rewards (C2). First control group (C1) provides the benchmark for the difusion rate of natural invites. Because social games require co-location of players, a user may already have some incentive to recruit other people to play the game with. This intrinsic motivation, if present in the population, will show up in this control group and anything we observe in the data from the treatment groups will be driven by what is over and above unobserved factors and caused by the randomized treatment. As the treatment efects estimated in the experiment are the combination of the efects of both incentive structure and notification, we use C2 as a baseline in our analysis. Comparing the previous treatment groups with C2 allows us to see that although customer pull-back mechanisms, such as reminder notifications, are popular mechanism for promoting adoptions, the right incentive schemes can have a significant impact in accelerating adoption.

Our experiment was conducted over a period of roughly one and a half months. The treatment assignment is constant for a given user for the duration of the experiment.

Table 1. Summary of experiment groups and incentive schemes (Experiment 1).

<table><tr><td>Testgroup</td><td>Assignment Probability</td><td>Referral Reward Mechanism</td><td>Inviter Incentive (Percent)</td><td>Invitee Incentive (Percent)</td><td>Number of Subjects</td></tr><tr><td>Control Group 1 (C1)</td><td>0.12</td><td>No rewards, no reminders</td><td>0</td><td>0</td><td>179</td></tr><tr><td>Control Group 2 (C2) – Baseline group</td><td>0.22</td><td>No rewards, reminder notifications</td><td>0</td><td>0</td><td>363</td></tr><tr><td>Treatment Group (T1) – Selfish reward</td><td>0.22</td><td>Inviter gets 1000 virtual coins</td><td>100</td><td>0</td><td>348</td></tr><tr><td>Treatment Group (T2) – Equal-split reward</td><td>0.22</td><td>Inviter and Invitee both get 500 virtual coins each</td><td>50</td><td>50</td><td>367</td></tr><tr><td>Treatment Group (T3) – Generous reward</td><td>0.22</td><td>Invitee gets 1000 virtual coins</td><td>0</td><td>100</td><td>376</td></tr></table>

When a player enters the experiment by downloading or updating the app, she immediately enters a one-week period, called the incentivized period, during which the player can earn the referral reward for inviting new users. As discussed previously in the previous section, a new user can identify their inviter. Additionally, the reward received (if any) by the inviter and invitee is based on the group that the inviter belongs to, provided that the inviter is still in the incentivized period. When an invitee attributes the invitation to an inviter, the incentivized period for that inviter resets. However, if an invitee attributes an invitation to an inviter when the inviter is no longer in her incentivized period, then no reward is given for that invitation but the incentivized period of the inviter resets. Additional invite attributions by new invitees will allow the inviter to continue to remain in an active incentivized period. Even though empirically it does not appear to be the case, it is possible that resetting the incentivized period for those who successfully invited someone within a week could result in endogenous treatment durations. Therefore, we examine the sensitivity of our main results to this issue by restricting our sample to the first seven days in the experiment phase for all the users when they are equal in terms of being in incentivized treatment period and randomly assigned. In our analysis, there is no resetting and all users are equal in terms of being in incentivized treatment period.

In summary, based on our experiment design, when a user updates or downloads the app during the experiment period, regardless of whether she used the app before or not, she will be randomly assigned to one of the groups and be a subject of the experiment. For each group, there are a similar number of existing users (who update the app) and new users (who download the app for the first time) who were the part of the experiment for a similar period of time. The referral incentives we ofered during the trial were 1,000 virtual coins that can be redeemed at any time in the app to purchase additional content and cosmetic game items.<sup>13</sup> That is, an inviter in a selfish reward group will receive all 1,000 coins and the invitee will receive nothing; the inviter and invitee in an equal-split reward group each receive 500 coins; and an inviter in the generous reward group gets nothing but the invitee receive 1,000 coins. Here, 1,000 virtual coins are equivalent to \$1 in worth, a value that compares well with the average price of similar online apps. It bears mention that we do not consider the case where both inviter and invitee get 1,000 coins each because it is akin to “growing the size of the pie” instead of dividing it. A profit-seeking game developer is only interested in awarding a certain amount of virtual coins per referral (e.g., 1,000 coins in this case) and the question is how to split it in a way that improves referral-based adoption of the game.

As previously mentioned, the mobile application also delivers reminder notifications<sup>14</sup> to the players in the four treatment groups during their incentivized period about the rewards they can receive upon inviting new people to adopt the game. Figure 2a shows screenshots of the reminders sent to the diferent groups of the trial to encourage ofline WOM-based invitations to their friends.

Upon successful referrals, the inviters and invitees also receive messages informing them about their received rewards. These sample messages are shown in Figure 2b. It is worth noting here that for the selfish reward group the app only informs the inviter about the reward and does not reveal to the invitee that the inviter was rewarded for the referral. This was done to reduce the potential negative impact that guilt may otherwise have in a social setting in the case of users assigned to the selfish reward group.

<table><tr><td>No reward group</td><td>Selfish reward group</td><td>Equal reward group</td><td>Generous reward group</td></tr><tr><td>Thank you for joiningHearsay! This game is bestplayed with new friends.Invite someone today!</td><td>Thank you for joiningHearsay! Invite a new friendto play before the nextweekend is over and we willreward you with 1,000 coins!</td><td>Thank you for joining Hearsay!Invite a new friend to playbefore the next weekend isover and we will reward bothof you with 500 coins each!</td><td>Thank you for joiningHearsay! Invite a new friendbefore the next weekend isover and we will reward them1,000 coins on your behalf!</td></tr><tr><td>Okay</td><td>Okay</td><td>Okay</td><td>Okay</td></tr></table>

![](/api/attachments/NVS77X3F/fulltext/images/66cb346d8a789ba46e54220e8099e3ba7ba606bf26b120eca42d01a264e34cf2.jpg)  
Figure 2. a) Sample reminder notifications received by inviters (Experiment 1). b) Sample messages received by inviters and invitees upon successful referrals (Experiment 1).

## Analyses and Results

## Data and Descriptive Statistics

A summary of the various groups and the referral reward design for each group is listed in Table 1. In the trial period, there were 1,633 players in total who adopted or updated the app. For each user, we know the time they joined the site, whether they joined the site before the experiment phase (existinguser = 1 for existing users, 0 for new users), and whether they joined the site on their own (invited = 1 when the user was invited, 0 when the user joined on her own). We define an outcome variable, invitation\_converted, measured as the number of converted referrals during the incentivized period; a variable, join\_time\_duration, measured as the number of days between the date when the user joined the trial and the end date of the trial; and a variable, app\_update\_date, measured as the number of days elapsed between the start date of the treatment phase of the trial and the day when the user actually joined the treatment by updating (for existing users) or downloading their app (for new users).

In addition, we collect login and gaming activities for the users in our sample for the pretreatment and treatment periods regarding which players play together in a group, the frequency and duration of games played by each group, and the location at which the games are usually played, among other data. For robustness purposes, such as establishing the equivalence of the treatment groups and control group, we constructed the following social engagement metrics based on activities one month prior to the experiment: login\_days (number of days that a user logged in), login\_hours (number of hours that a user logged in), game\_count (number of games that a user played), game\_total\_player (number of total players with whom a user played), game\_ave\_player (average number of players a user played with), game\_total\_time (number of total seconds during which a user played a game), game\_ave\_time (average seconds of games a user played), and location\_count (number of unique locations at which a user played).

## Efects of Incentive Structure on the Number of Converted Invitations

Before reporting the results of the analysis, we analyzed the data gathered in the pretreatment period about the behavior of the players assigned to the control and treatment groups to check if there are any statistically significant characteristic diferences between these groups. The summary statistics and comparisons of the pretreatment behavior across users in the diferent treatment and control groups are given in Table A2 in Online Supplemental Appendix A. We find the treatment and control groups have statistically indistinguishable properties, evidenced by a lack of a directional pattern in the magnitude as well as a lack of significance, prior to manipulation.

We begin our main analysis by exploring changes in the number of successful invitations (e.g., converted referrals) that were induced by our treatment over the incentivized period. Our main estimation equation for inviter j is

$$
\text { invitation\_converted } _ {j} = \alpha + \sum \beta_ {g} T _ {g} + \varepsilon_ {j}\tag{1}
$$

where invitation converted<sub>j</sub> is the number of converted invitations by an inviter j and the variable $T _ { g }$ indicates the treatment group that an inviter j is assigned to. Control group is the baseline. Table 2, Column (1) presents the results for the efect of the incentive schemes on the number of successful referrals by inviters.<sup>15</sup> We find that both equal-split and generous reward significantly increase the total number of conversions compared to the control group as well as the selfish reward. There was no significant diference between equal-split reward and generous reward.

Given that our outcome variable invitation\_converted is a count variable, we also verify the previous results using a Poisson regression [Table 2, Column (2)] using treatment as an independent variable uncorrelated with the residual. Consistent with the results in Column (1), we find that only the equal-split reward and generous reward are significant compared to the baseline group (C2).<sup>16</sup>

These results indicate that compared to the baseline group, the group with no reward but only notification, the selfish referral reward (i.e., inviter gets the whole reward) do not perform much better. However, the players in the equal-split reward and generous group promote a significantly higher number of successful referrals than the players in the control group. This provides initial evidence that, in the context of mobile social games, reward schemes with a pro-social component tend to dominate the egocentric referral schemes. Because our outcome measure is self-reported, it could be the case that the generous scheme may be linked with a greater propensity among recipients to report, and conversely a lower propensity to report if there is nothing in it for the recipients. However, we note that such a behavior is not without a significant social cost of denying someone you are going to socially interact with a fairly obtained monetary reward, which is substantial in a physical co-located setting.

Table 2. Main efect (Experiment 1).

<table><tr><td>DV</td><td colspan="2"> $invitation_{converted}$ </td></tr><tr><td>Column</td><td>(1)</td><td>(2)</td></tr><tr><td>Intercept</td><td>0.0220*(0.0108)</td><td>-3.8150***(0.3536)</td></tr><tr><td>C1: No reward, no reminders</td><td>-0.0053(0.0241)</td><td>-0.2738(0.6770)</td></tr><tr><td>T1: Selfish reward</td><td>-0.0048(0.0198)</td><td>-0.2455(0.5401)</td></tr><tr><td>T2: Equal-split reward</td><td>0.0325*(0.0195)</td><td>0.9053**(0.4183)</td></tr><tr><td>T3: Generous reward</td><td>0.0445**(0.0194)</td><td>1.1042***(0.4062)</td></tr><tr><td>Model</td><td>OLS</td><td>Poisson</td></tr><tr><td> $R^2$ </td><td>0.1064</td><td>-</td></tr><tr><td>AIC</td><td>-</td><td>554.77</td></tr><tr><td># of observations</td><td>1633</td><td>1633</td></tr></table>

Note: \* significant at 10 percent; \*\* significant at 5 percent; \*\*\* significant at  
1 percent. Robust standard errors are in parentheses. C2 is the baseline group.

## Experiment 2

## Institutional Details: Mobile Social Games that Encourages Online WOM

While the context of Experiment 1 provides a unique setting to capture ofline word-of -mouth, the fact that users must be co-located to play the game, may, arguably, raise an issue of generalizability. In addition, as we do not observe how many and when the invitations were sent, it makes it challenging to appreciate the underlying mechanisms driving the results. Therefore, to explore the generalizability of our findings and uncover the underlying mechanisms, we replicate the treatments (i.e., selfish, equalsplit, generous) of the previous field experiment in a more classical online referral setting in Experiment 2. Specifically, we coordinate with a diferent mobile social game company in India whose game only allows users to send referral invitation through their application. The application is a quiz game in which several games are played live at a specific time every day and any user can access the app to play a game. Each game consists of 10 questions, and the winner of each game receives prize money. Sample screenshots from the game are shown in Figure 3. The game was released for free and ofered in both English and Hindi.

The context of this study overcomes the challenges of Experiment 1 and help us better understand the underlying mechanisms in two ways:

(1) The context is a pure online social mobile game, which does not sufer from potential treatment interference and bias from user co-location and help us check the generalizability of our results.

![](/api/attachments/NVS77X3F/fulltext/images/4c75bccb2708571ffd52ca6c6fab07d680b02078018507bcb504b2c53ae55e77.jpg)  
Figure 3. Screenshots of the mobile game app (Experiment 2).

(2) The referral process of the game uses an online invitation embedded in the app, which enable us to track when and how many referrals were sent and accepted, thus allowing us to investigate the underlying mechanisms.

## Experimental Design

Because the app already had a referral program with an equal-split reward scheme before conducting the experiment, our experiment only focuses on users who download the app for the first time. When a new user downloads the app during the experiment period, the user is randomly assigned to one of the treatment groups following the assignment probability given in Table 3.<sup>17</sup>

Once a user is assigned to one of the treatment groups, she will see a diferent call-toaction from the referral program in the app based on the group to which she is assigned. The user can invite friends in their contact list through the app. Once a user decides to send a referral, the app will send the invitation message according to the user’s assigned group.<sup>18</sup> The various calls-to-action to inviters and referral messages to invitees are shown in Table 4. Overall, the experiment was conducted for about 4 months, during which 2,817 new users downloaded the app.

Table 3. Summary of experiment groups and incentive schemes (Experiment 2).

<table><tr><td>Testgroup</td><td>Assignment Probability</td><td>Referral Reward</td><td>Number of Subjects</td></tr><tr><td>C1 (No reward)</td><td>0.1</td><td>No rewards</td><td>273</td></tr><tr><td>T1 (Selfish reward)</td><td>0.3</td><td>Inviter gets Rs 200</td><td>870</td></tr><tr><td>T2 (Equal-split reward)</td><td>0.3</td><td>Inviter and Invitee both get Rs 100 each</td><td>852</td></tr><tr><td>T3 (Generous reward)</td><td>0.3</td><td>Invitee gets Rs 200</td><td>822</td></tr></table>

Table 4. Messages shown to inviters and invitees (Experiment 2).

<table><tr><td>Testgroup</td><td>Call-to-Action to the Inviter</td><td>Message to the Invitee When the Inviter Sends an Invitation</td></tr><tr><td>C1 (No reward)</td><td>Invite your friend today!</td><td>Experience Muquaabla, a quiz app that lets you win cash prizes! Use my referral code blow:</td></tr><tr><td>T1 (Selfish reward)</td><td>Invite your friend and earn Rs 200!</td><td>Experience Muquaabla, a quiz app that lets you win cash prizes! Use my referral code blow:</td></tr><tr><td>T2 (Equal-split reward)</td><td>Invite your friend and both get Rs 100!</td><td>Experience Muquaabla, a quiz app that lets you win cash prizes! Use my referral code blow and we will both get Rs 100:</td></tr><tr><td>T3 (Generous reward)</td><td>Invite your friend and give Rs 200!</td><td>Experience Muquaabla, a quiz app that lets you win cash prizes! Use my referral code blow and you will get Rs 200:</td></tr></table>

## Analyses and Results

## Efects of Incentive Structure on the Number of Converted Invitations

To identify the efect of diferent incentive schemes on both inviter’s likelihood to send and the invitee’s likelihood to accept referrals, we run the regression both at the inviter level and invitee level [12, 13].

First, we relate the number of invitations sent by an inviter (e.g., invitation\_ sent) to dummy indicators of each of our treatment conditions and run an ordinary least square regression at the inviter level to analyze the relationship between incentive schemes and the inviter’s referral behavior (Equation 2). 19

$$
i n v i t a t i o n \_ s e n t _ {j} = \alpha + \sum \beta_ {g} T _ {g} + \varepsilon_ {j}\tag{2}
$$

$$
\text { invitation\_converted } _ {j} = \alpha + \sum \beta_ {g} T _ {g} + \varepsilon_ {j}\tag{3}
$$

Table 5 Column (1) shows the results for the efect of the incentive schemes on the number of referrals sent by users (i.e., inviters) to their friends. While we find no significant diferences across the treatments in the inviter’s referral behavior, the results shed light on inviter’s motive of sending referrals. First, the fact that the users in the selfish group make fewer absolute numbers of invitations than users in the control group suggests that the selfish scheme increases psychological cost of inviters about only gaining referral rewards [29]. This is also supported by the fact that users in the selfish group sent fewer referrals compared to even those in the equalsplit group who receive less rewards for referrals. In addition, we find that users in the generous group send out similar number of invitations compared to the control group. The result implies that the users in the generous group are driven by intrinsic motivation similar to the control group (e.g., organic WOM).

Subsequently, we run the regression (Equation 3) to analyze the relationship between various incentive schemes and the successful referral outcomes (e.g., invitation\_converted). The results are reported in Table 5, Column (2). Consistent with Experiment 1, we find that both equal-split and generous schemes lead to a significantly larger number of conversions compared to the control group and selfish group, with the generous scheme having a higher 20 (but not statistically distinguishable) efect than the equal-split scheme.

To further understand the efect of diferent incentive schemes on invitee’s likelihood to accept referrals, following the idea of Bapna and Umyarov [6], we collect 405 inviter-invitee dyads of all referral data and employ a random efects model at the recipient level using the specification in Equation 4.<sup>21</sup> accept invitation<sub>ij</sub> indicates invitee i’s decision to adopt the invitation after receiving inviter j’s referral.

Table 5. Main efect using OLS (Experiment 2).

<table><tr><td rowspan="2">DV</td><td> $invitation_{sent}$ </td><td> $invitation_{converted}$ </td></tr><tr><td>(1)</td><td>(2)</td></tr><tr><td>Intercept</td><td>0.1429***(0.0310)</td><td>0.0147(0.0129)</td></tr><tr><td>T1 (Selfish reward)</td><td>-0.0176(0.0355)</td><td>-0.0055(0.0147)</td></tr><tr><td>T2 (Equal-split reward)</td><td>0.0250(0.0356)</td><td>0.0253*(0.0148)</td></tr><tr><td>T3 (Generous reward)</td><td>-0.0042(0.0358)</td><td>0.0291**(0.0148)</td></tr><tr><td> $R^2$ </td><td>0.0011</td><td>0.0053</td></tr><tr><td># of observations</td><td>2817</td><td>2817</td></tr></table>

Note: \* significant at 10 percent; \*\* significant at 5 percent; \*\*\* significant at  
1 percent. Robust standard errors are in parentheses.

$$
a c c e p t \_ i n v i t a t i o n _ {i j} = \alpha + \sum \beta_ {j} T _ {j} + \mu_ {i} + \varepsilon_ {i j}\tag{4}
$$

The results are reported in Table 6, which show that only the equal-split and generous treatments are significant in driving referral conversions. We also find similar results by looking at the conversion rate of referrals sent from each group (Figure 4), that is, conditional on receiving a referral, pro-social schemes (i.e., equal-split and generous scheme) have better conversion rates compared to the control group.

Overall, our analysis ofers interesting mechanism level insights into the inherent tradeof between incentivizing the inviter and the invitee. First, for the selfish scheme, in contrast to ex ante expectations of rational utility maximizing agents, we find that the incentive design decreases the rate of sending out referrals. This is possibly because the sender feels guilt from engaging in referral program that only incentivizes herself [29]. In addition, the lower conversion rate of the invitees compared to the control group provides suggestive evidence that those who sent out referrals in the selfish group may be driven by extrinsic motivations and do not consider recipient’s interest in accepting the referral [23]. In relation to the equal-split scheme, the results show that incentivizing both inviter and invitee results in higher conversions compared to the control group by not only increasing the number of referrals but also increasing the conversion rate of invitees. Especially, the fact that inviters shared higher number of referrals compared to selfish scheme while receiving less incentive suggests that incentivizing the invitee reduces the feeling of guilt and further motivates inviters to initiate referrals. Lastly, regarding the generous scheme, we find that the generous incentive design does not increase the number of referrals compared to the control group. However, conditional on sharing a referral, it results in higher conversion rate which leads to the highest number of conversions. The higher conversion rate for both equal-split and generous schemes suggests that firms can apportion some of the inviter’s reward to the invitee without demotivating the inviters from initiating referrals.

Table 6. Efect on invitee’s likelihood to accept referrals (Experiment 2).

<table><tr><td>DV</td><td> $accept_{invitation}$ </td></tr><tr><td>Intercept</td><td>0.1056*(0.0617)</td></tr><tr><td>T1 (Selfish reward)</td><td>-0.0318(0.0749)</td></tr><tr><td>T2 (Equal-split reward)</td><td>0.1254*(0.0731)</td></tr><tr><td>T3 (Generous reward)</td><td>0.1984***(0.0746)</td></tr><tr><td># of observations</td><td>405</td></tr></table>

Note: \* significant at 10 percent; \*\* significant at 5 percent; \*\*\* significant at 1 percent. Robust standard errors are in parentheses.

![](/api/attachments/NVS77X3F/fulltext/images/6f287292ec902dbb24378e5c9264457e25574efa0c56b880cd3809af4db52c3e.jpg)  
Figure 4. Referral conversion rate of each group.

Together, consistent findings from our two experiments suggest that a budget-constrained marketer should lean towards using referral incentive schemes that have a significant prosocial component in them in order to promote viral adoption in the digital world.

## Exploring Mechanisms on Why Pro-social Schemes Result in Higher Conversion

Our results show that both equal-split and generous schemes result in a significantly larger number of conversions. A high conversion rate in those schemes could have one of two explanations: 1) invitees in these groups receive rewards for accepting a referral, and 2) prosocial component in the incentive scheme encourages inviters to send selective and bettertargeted referrals.

To further investigate whether the inviter’s efort played an important role in increasing conversion rate, we conducted additional analyses. Specifically, we examine whether different incentive schemes motivated users with diferent levels of experience with using the app to share referrals and whether that experience has a positive efect on increasing the invitee’s likelihood to accept referrals. Van den Bulte and Iyengar [32] find that experienced users make better referrals and suggest this happens because they have better knowledge about the product and exert greater efort in finding good matches (e.g., potential recipients).<sup>22</sup> Aligned with this finding, if experienced users (i.e., those who used the app more frequently) made referrals in a specific incentive scheme and those referrals had a positive impact on invitees’ to accept the referrals, the results will provide suggestive evidence that the incentive scheme motivated inviters to exert greater efort to find a good potential recipient.

We first examine the number of games that inviters in each group played when sending referrals and report the results in Figure 5. As per Figure 5, we find that users in the equal-split and generous scheme sent referrals when they had more (but not significant) experience with the app than those in the control group. To check whether inviter’s usage experience with the app has a positive efect on the likelihood to accept referrals, we compare the inviter’s experience variable to dummy indicators of each in our treatment conditions in Equation 4 and estimate the model using the following specification

$$
a c c e p t \_ i n v i t a t i o n _ {i j} = \alpha + \sum \beta_ {j} T _ {j} + \sum \sigma_ {j} T _ {j} * a p p \_ e x p e r i e n c e _ {j} + \mu_ {i} + \varepsilon_ {i j}\tag{5}
$$

where $a p p _ { e x p e r i e n c e _ { j } }$ denotes the number of games inviter j played before sending a referral.<sup>23</sup> A positive and significant coeficient $\sigma _ { j }$ indicates that referrals in that group were more likely to be accepted when they were sent from experienced users, who may exert greater efort in sending a referral. It also implies that the incentive scheme in these groups motivated more experienced users, who can make better-targeted referrals, to send out referrals.

The results are reported in Table 7. The results show that the inviter’s experience with the app played a significant positive role for users in equal-split and generous groups. Overall, our results provide evidence that pro-social schemes motivate users to become more selective and make better-targeted referrals. We conduct an additional analysis using tenure (e.g., the number of days since a user downloaded the app) as an alternative app experience measure and confirm that the results are consistent (see Table A7 in Online Supplemental Appendix A).

![](/api/attachments/NVS77X3F/fulltext/images/1f07157066c9b6bf1cb2984c98defe077398a226f52b4a4e47160584fe2dd0f3.jpg)  
Panel A  
Figure 5. Inviter’s app experience when sending referrals.

![](/api/attachments/NVS77X3F/fulltext/images/bcc06fedb01d5d7092cb956dee512bb62fb40b933ef0984879184bc03c79a77d.jpg)  
Panel B

![](/api/attachments/NVS77X3F/fulltext/images/9e9d2948fab5dabef453fb896d92727c6d07e4c6e6d563ffa176bb58b4b9ef1c.jpg)  
Panel C

Table 7. Efect of inviter app experience on accepting referrals (Experiment 2).

<table><tr><td>DV</td><td> $accept_{invitation}$ </td></tr><tr><td>Intercept</td><td>0.0743(0.0747)</td></tr><tr><td>T1 (Selfish reward)</td><td>0.0038(0.0845)</td></tr><tr><td>T2 (Equal-split reward)</td><td>0.1248(0.0836)</td></tr><tr><td>T3 (Generous reward)</td><td>0.1837**(0.0854)</td></tr><tr><td>Control * app_experience</td><td>0.0186(0.0228)</td></tr><tr><td>T1 * app_experience</td><td>-0.0047(0.0127)</td></tr><tr><td>T2 * app_experience</td><td>0.0180*(0.0093)</td></tr><tr><td>T3 * app_experience</td><td>0.0211**(0.0087)</td></tr><tr><td># of observations</td><td>405</td></tr></table>

Note: \* significant at 10 percent; \*\* significant at 5 percent; \*\*\* significant at 1 percent. Robust standard errors are in parentheses. The interaction term presents whether the coeficient is significantly diferent from 0.

## Discussion

## Theoretical Contributions

This work complements two streams of research on viral marketing. First, the study contributes to the stream of literature estimating causal peer influence in social networks. Although previous studies using randomization trials have demonstrated peer influence at work, there have not been many empirical investigations to discover how diferent referral incentive schemes drive the peer influence through WOM in the social contagion process.

Our findings also complement other recent research with respect to constructing referral incentive schemes to promote WOM based adoption. Existing studies of designing referral incentives on WOM mainly focused on inviters’ behavior and rarely considered incentive sharing schemes in which both parties receive rewards. We contribute to the literature by studying how an important mechanism of social contagion, WOM, is causally influenced by the design of a given referral incentive scheme—namely selfish reward, equal-split reward, and generous reward schemes. Thus, the findings of our study are relevant to creating referral programs to promote WOM based adoption of digital goods.

## Managerial Implications

In addition to the theoretical insights, our study also provides clear managerial implications for firms. First, the results show that the generous pro-social referral reward schemes dominate purely selfish schemes in creating word-of-mouth. This is consistent with the observations of Dunn and Norton [14] that happiness resulting from altruistic behavior can be a strong motivator for WOM based viral adoption.

Another factor may be the lack of guilt when one is being generous in inviting other friends to adopt the product. A combination of factors like the lack of guilt, inherent altruism, and pro-social happiness efect may contribute towards this outcome. Second, our findings of heterogeneity in treatment efects across diferent customer segments suggest that firms should target customers with diferent incentive scheme in their referral campaign. Overall, our findings suggest that a firm should lean towards using referral incentive schemes with a significant pro-social component in order to promote viral adoption in the digital world.

## Limitations and Directions for Further Research

Although the context (i.e., mobile social games) and the international scale (i.e., United States and India) of our two experiments allow us to capture the general efect of the diferent referral incentive schemes to promote the adoption of digital products, future works should test the generalizability of these insights to other contexts with lower network efects. Second, when designing diferent incentive schemes, the financial reward for participation was relatively small, consistent with what mobile gaming applications are ofering these days. However, it is not clear whether the findings would also generalize for larger financial rewards. We expect future work to use a similar experimental setup to study the efect using larger financial rewards. Lastly, we did not have access to users’ demographic information; therefore, we could not examine the heterogeneous treatment efects across diferent demographics (e.g., age, gender, etc.). One of the constraints of the mobile app ecosystem, especially in the gaming context, is that users are loath to provide demographic information, and they are not required to create authentic and detailed profiles for app downloads for most online games. Hence, we could not have the same data that is available to companies like Facebook, LastFM or OkCupid, where users have specific reasons to set up their profiles. Future research can examine whether the diferent incentive schemes would diferently impact across diferent demographics.

## Conclusions

Understanding how an incentive structure causally impacts the difusion of products through WOM is a crucial to developing efective referral reward strategies for viral adoption of digital goods. Referral marketing of digital goods frequently involves providing monetary or cosmetic (e.g., status, badges) incentives to existing users to stimulate WOM to increase product adoption among their friends. However, relatively few studies have examined which type of referral reward structure (i.e., incentive sharing between the inviter and the invitee) is most efective in maximizing WOM.

We explore this issue by designing two randomized field experiments in which we test the efectiveness of selfish, equal, and generous referral rewarding schemes. We partnered with two mobile social game application companies to conduct randomized experiments of these referral schemes for their products. Experiment 1 allowed us to design a clean study examining the efect of online referral reward structure on the ofline difusion of the product. Then, Experiment 2 was designed to test the efect in the similar context in a classical online referral setting as well as dig deeper into the underlying mechanisms. Consistent across both sets of results, we find that pro-social referral incentive schemes, namely equal-split and generous schemes, lead to significantly larger number of conversions compared to the control group and selfish group, with the generous scheme having a higher efect than the equal-split scheme. Additionally, our mechanism level analysis shows that both equal-split and generous schemes result in higher number of conversions by significantly increasing the invitee’s likelihood to accept referrals, which we further show is partially due to selective and better targeted referrals. Our results contribute to the understanding of the optimal design of online referral programs and provide important implications for designing efective referral reward schemes in the digital world.

## Notes

1. For instance, industry reports suggest that face to face invites have 5x the acceptance rate of Facebook invites as per http://www.nielsen.com/us/en/newswire/2009/global-advertisingconsumers-trust-real-friends-and-virtual-strangers-the-most.html

2. https://www.dropbox.com/referrals

3. http://www.groupon.com/referral

4. https://www.lyft.com/help/article/1455280

5. https://awesomesauceeats.wordpress.com/tag/blue-apron/

6. Rosen 2009, The Anatomy of Buzz Revisited: Real-life lessons in Word-of-Mouth Marketing, Crown Business.

7. These games are even becoming a fun-filled way of providing training, teaching social skills, encouraging collaboration, and devising strategy. In 2019, mobile games made up 60 percent of revenue for the global video game market, generating \$49 billion in revenue, based on a study by GoldenCasinoNews.com (https://goldencasinonews.com/blog/2019/12/30/mobile-gaminggenerated-60-of-the-global-video-games-revenue-in-2019/). The mobile gaming market is forecast to grow 2.9 percent annually to hit \$56.6 billion by 2024.

8. We provide the summary of prior research on referral program in Table A1 in Online Supplemental Appendix A.

9. This social app needs at least three co-located players to play a round of the game.

10. As far as the geo-sensing feature is concerned, co-located users can be within 1 degree of latitude and longitude of each other. But only users that are physically co-located can play this game together because it requires verbal interaction.

11. A potential misclassification of an invited user as an organic user may happen in the unlikely event where the invited user is instructed to download the app in advance in anticipation of playing the game later on. If the duration between the app download and the first game is more than an hour, then this user will not see the invitation attribution screen. However, because of randomization, there is little reason for this scenario to arise systematically in any treatment group, and as such is not a major threat to our inference.

12. While a continuous range of incentive splits of the form (x, 100 – x) between inviter and invitee are possible, we chose (100, 0), (50, 50), and (0, 100) as the treatment options because these can be unambiguously interpreted as purely selfish, equal-split, and purely generous.

13. These game items include content such as question cards, user avatars, virtual weapons, and so forth. As these items are tied to the purchasing user and provide them with features that others do not have, they largely have an individual value.

14. The app provided two types of reminders—one is a local notification that is sent out the first time 3 hours after the app’s download (to nudge them to invite friends) and then onwards on every Friday (to encourage them to play the party game in the upcoming weekend), the other is an in-app notification that is visible in the home screen once the app is launched. It is important to note that these reminder mechanisms were consistent across all treatments. The diference in results we find across the treatment groups is therefore driven by the incentive schemes.

15. We provide the summary statistics of the Experiment 1 results in Table A3 in Online Supplemental Appendix A.

16. The detailed specifications and the results of additional robustness check are presented in Online Supplemental Appendix B.

17. The total referral incentive we ofer in Experiment 2 is Rs 200 which is equivalent to \$2.5.

18. To examine the clear efect of diference referral schemes, we ensure that users cannot change the referral message sent to their friends.

19. We provide the summary statistics of the Experiment 2 results in Table A4 in Online Supplemental Appendix A.

20. We conduct the analysis using Poisson regression and confirm that the results are consistent (Table A5 in Online Supplemental Appendix A).

21. We choose a random efects model based on a Hausman test that could not reject the null hypothesis that the errors are not correlated with the explanatory variables (Prob $> \chi 2 = 0 . 2 7 7 )$ 1 (Green [19]).

22. The authors also suggest that it may happen as experienced users share similar unobservable characteristics. However, because of randomization, we believe this efect (if any) would be the same across treatment groups.

23. It is important to note that we did not include the main efect (e.g., app\_experience) in the model since we would like to examine whether the interaction term is significantly diferent from 0 not from the baseline group. The results including the in the model is reported in Table A6 in Online Supplemental Appendix A.

## Acknowledgements

The authors thank the review team for providing very constructive feedback. The authors also thank Avijit Sengupta for the collaboration and support.

## References

1. Ahrens, J.; Coyle, J. R.; and Strahilevitz, M. A. Electronic word of mouth: The efects of incentives on E-referrals by senders and receivers, European Journal of Marketing, 47, 7 (2013), 1034–1051.

2. Andreoni, J.; and Miller, J. Giving According to GARP: An experimental test of the consistency of preferences for altruism, Econometrica, 70, 2 (2002), 737–753.

3. Aral, S.; and Walker, D. Creating social contagion through viral product design: A randomized trial of peer influence in networks, Management Science, 57, 9 (2011), 1623-1639.

4. Baker, A. M.; Donthu, N.; and Kumar, V. Investigating how word-of-mouth conversations about brands influence purchase and retransmission intentions. Journal of Marketing Research, 53, 2, (2016), 225–239.

5. Banerjee, A. V. A simple model of herd behavior. The Quarterly Journal of Economics, 107, 3 (1992), 797–817.

6. Bapna, R.; and Umyarov, A. Do your online friends make you pay? A randomized field experiment in an online music social network. Management Science, 61, 8 (2015), 1902–1920.

7. Berger, J.; and Milkman, K.L. What makes online content viral? Journal of Marketing Research, 49, 2 (2012), 192–205.

8. Berger, J.; and Schwartz, E. What drives immediate and ongoing word of mouth. Journal of Marketing Research, 48, 5 (2011), 869–880.

9. Biyalogorsky, E.; Gerstner, E.; and Libai, B. Customer referral management: Optimal reward programs. Marketing Science, 20, 1 (2001), 82–95.

10. Ceran, Y.; Singh, H.; and Mookerjee, V. Knowing what your customer wants: Improving inventory allocation decisions in online movie rental systems. Production and Operations Management, 25, 10 (2016), 1673-1688.

11. Duan, W.; Gu, B.; and Whinston, A. B. Informational cascades and software adoption on the Internet: An empirical investigation. MIS Quarterly, 33, 1 (2009), 23–48.

12. Duflo, E.; Glennerster, R.; and Kremer, M. Using randomization in development economics research: A toolkit. Handbook of development economics, 4 (2007), 3895–3962.

13. Duflo, E.; Dupas, P.; and Kremer, M. Peer efects, teacher incentives, and the impact of tracking: Evidence from a randomized evaluation in Kenya. American Economic Review, 101, 5 (2011), 1739–1774.

14. Dunn, E.; and Norton, M. Happy Money: The Science of Happier Spending. New York, NY: Simon & Schuster Paperbacks, 2014.

15. Fang, B.; Zheng, Z.; Ye, Q.; and Goes, P. B. Social influence and monetization of freemium social games. Journal of Management Information Systems, 36, 3 (2019), 730–754.

16. Ferreira, P.; Telang, R.; and De Matos, M. G. Efect of friends’ churn on consumer behavior in mobile networks. Journal of Management Information Systems, 36, 2 (2019), 355–390.

17. Gneezy, U.; Stephan, M.; and Pedro, R.B. When and why incentives (don’t) work to modify behavior. Journal of Economic Perspectives, 25, 4 (2011), 191–210.

18. Godes, D.; and Mayzlin, D. Using online conversations to study word-of-mouth communication. Marketing Science. 23, 4 (2004), 545–560.

19. Green, W. Econometric Analysis, New York, NY: Prentice Hall, 2012.

20. Gu, B. and Ye, Q. First step in social media: Measuring the influence of online management responses on customer satisfaction. Production and Operations Management, 23, 4 (2014), 570–582.

21. Hong, Y.; Pavlou, P.; Shi, N.; and Wang, K. On the role of fairness and social distance in designing efective social referral systems. MIS Quarterly, 41, 3 (2017), 787–809.

22. Iyengar, R.; Van den Bulte, C.; and Valente, T. Opinion leadership and social contagion in new product difusion. Marketing Science, 30, 2 (2011), 195–212.

23. Jung, J.; Bapna, R.; Golden, J.; and Sun, T. Words matter! Towards pro-social call-to-action for online referral: Evidence from two field experiments. Information Systems Research, 31, 1 (2020), 16–36.

24. Kornish, L. J.; and Li, Q. Optimal referral bonuses with asymmetric information: Firm-ofered and interpersonal incentives, Marketing Science, 29, 1 (2010), 108–121.

25. Kuem, J.; Ray, S.; Siponen, M.; and Kim, S. S. What leads to prosocial behaviors on social networking services: A tripartite model. Journal of Management Information Systems, 34, 1 (2017), 40–70.

26. Laing, R. D.; Phillipson, H.; and Lee, A. R. Interpersonal Perception: A Theory and a Method of Research. New York, NY: Springer, 1966.

27. Lee, B.; Cheung, H.; and Li, X. Impact of online word of mouth on channel disintermediation for information goods. Journal of Management Information Systems, 35, 3 (2018), 964–993.

28. Qiu, L.; and Whinston, A. Pricing strategies under behavioral observational learning in social networks. Production and Operations Management, 26, 7 (2017), 1249–1267.

29. Ryu, G.; and Feick, L. A penny for your thought: Referral reward programs and referral likelihood, Journal of Marketing, 71, 1 (2007), 84–94.

30. Schmitt, P.; Skiera, B.; and Van den Bulte, C. Referral programs and customer value. Journal of Marketing, 75, 1 (2011), 46–59.

31. Sundararajan, A.; Provost, F.; Oestreicher-Singer, G.; and Aral, S. Research Commentary— Information in Digital, Economic, and Social Networks. Information Systems Research, 24, 4 (2013), 883–905

32. Van den Bulte, C.; and R. Iyengar. Tricked by truncation: Spurious duration dependence and social contagion in hazard models. Marketing Science. 30, 2 (2011), 233–248.

33. Van den Bulte, C.; Bayer, E.; Skiera, B.; and Schmitt, P. (2018) How customer referral programs turn social capital into economic capital. Journal of Marketing Research, 55, 1 (2018), 132–146.

34. Walster, E.; Berscheid, E.; and Walster, G. W. New directions in equity research, Journal of Personality & Social Psychology, vol. 25, 2 (1973), 151–176.

35. Wirtz, J.; and Chew, P. The efects of incentives, deal proneness, satisfaction and tie strength on word-of-mouth behavior. International Journal of Service Industry Management, 13, 2 (2002), 141– 162.

36. Wirtz, J.; Orsingher, C.; Chew, P.; and Tambyah, S. K. The role of metaperception on the efectiveness of referral reward programs. Journal of Service Research. 16, 1 (2013), 82–98.

## About the Authors

Jaehwuen Jung (jaejung@temple.edu; corresponding author) is an assistant professor of Management Information Systems at Fox School of Business, Temple University. The unifying theme of his research is to causally examine the impact of new technology channels, digital platforms, and technology-enabled features on user behavior and firms’ outcomes. His work has been published in such journals as Information Systems Research and MIS Quarterly.

Ravi Bapna (rbapna@umn.edu) is the Curtis L. Carlson Chair in Business Analytics and Information Systems at the Carlson School of Management where he also serves as the Associate Dean for Executive Education and Academic Director of the Carlson Analytics Lab. His research investigates social media, social engagement, analytics, economics of information systems, trust and peer influence online, e-market design, grid computing, and the design of the IT organization. His research has been published in a wide array of journals, such as Management Science, Information Systems Research, Journal of Management Information Systems, MIS Quarterly, INFORMS Journal on Computing, Naval Research Logistics, and many others.

Alok Gupta (agupta037@umn.edu) is the Associate Dean of Faculty and Research and Curtis L. Carlson School-wide Chair in Information Management at the Carlson School of Management, University of Minnesota. His research has been published in various information systems, economics, and computer science journals. His work has been published in various information systems, economics, and computer science journals, such as Management Science, Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Journal of Operations Management, Computational Economics, and many others. He is Editor-in-Chief of Information Systems Research.

Soumya Sen (ssen@umn.edu) is an Associate Professor of Information & Decision Sciences at the Carlson School of Management and a McKnight Presidential Fellow at the University of Minnesota, where he is also the academic director of Management Information Systems Research Center. Dr. Sen’s research takes an interdisciplinary approach involving computer science and economics to address topics in resource allocation, incentive design, and development of information technology artifacts. His work has been published in various leading journals such as Journal of Management Information Systems, MIS Quarterly, IEEE/ACM Transactions on Networking, IEEE Transactions on Knowledge and Data Engineering, Journal of the American Medical Association, and others.
