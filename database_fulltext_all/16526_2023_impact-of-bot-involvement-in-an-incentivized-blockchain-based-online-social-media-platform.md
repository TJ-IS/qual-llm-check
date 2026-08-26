---
otero_id: 16526
otero_key: "9DFFN5WJ"
title: "Impact of Bot Involvement in an Incentivized Blockchain-Based Online Social Media Platform"
authors: "Fatemeh Delkhosh; Ram D. Gopal; Raymond A. Patterson; Niam Yaraghi"
year: "2023"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2023.2229124"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of Bot Involvement in an Incentivized Blockchain-Based Online Social Media Platform

Fatemeh Delkhosh, Ram D. Gopal, Raymond A. Patterson & Niam Yaraghi

To cite this article: Fatemeh Delkhosh, Ram D. Gopal, Raymond A. Patterson & Niam Yaraghi (2023) Impact of Bot Involvement in an Incentivized Blockchain-Based Online Social Media Platform, Journal of Management Information Systems, 40:3, 778-806, DOI: 10.1080/07421222.2023.2229124

To link to this article: https://doi.org/10.1080/07421222.2023.2229124

![](/api/attachments/9DFFN5WJ/fulltext/images/74c703cf5f739584c51675edd86a81ae3ca766e61b3242ce45b06f5a70f38a99.jpg)

View supplementary material

![](/api/attachments/9DFFN5WJ/fulltext/images/a942311963e0cd009718db0e3b5658834280eddc5606f55d43364c62a24901df.jpg)

Published online: 23 Aug 2023.

![](/api/attachments/9DFFN5WJ/fulltext/images/15b5a15eb671be28dc8d1157aee7a07f0a6743f48475c37ebf0bc056974945a5.jpg)

Submit your article to this journal

![](/api/attachments/9DFFN5WJ/fulltext/images/291d98e670a537220c55981550bc6d59b91fe092c13cb38e8581faf88c9fddc8.jpg)

Article views: 1445

![](/api/attachments/9DFFN5WJ/fulltext/images/27c2e9d4d4dd785d37fc014e993ca20e46c2e7530803ecc3b0ac4204b703c1aa.jpg)

View related articles

![](/api/attachments/9DFFN5WJ/fulltext/images/c6a5105e99fffdf8663a2dd696df203318add3d3089b3aa5f91499d0a234523b.jpg)

View Crossmark data

![](/api/attachments/9DFFN5WJ/fulltext/images/e34dfabe41bcdea67be8adf0b230301d44b1007dcd118d671c0d18d80371c09f.jpg)

Citing articles: 7 View citing articles

Check for updates

# Impact of Bot Involvement in an Incentivized Blockchain-Based Online Social Media Platform

Fatemeh Delkhosh<sup>a</sup>, Ram D. Gopal<sup>b</sup>, Raymond A. Patterson<sup>a</sup>, and Niam Yaraghi<sup>c</sup>

<sup>a</sup>Business Technology Management Department, Haskayne School of Business, University of Calgary, Calgary, AB, Canada; <sup>b</sup>Information Systems and Management Department, Warwick Business School, The University of Warwick, Coventry, UK; <sup>c</sup>Business Technology, Miami Hebert Business School, University of Miami, Coral Gables, FL, USA

## ABSTRACT

Incentivized blockchain-based online social media (BOSM), where creators and curators of popular content are paid in cryptocurrency, have recently emerged. Traditional social media ecosystems have experienced significant bot involvement in their platforms, which has often had a negative impact on both users and platforms. BOSM can provide additional direct financial incentives as motivation for both bots’ and human users’ engagement. Using the panel vector autoregression and regression discontinuity in time framework, we analyze two distinct data sets from Steemit, the largest and most popular BOSM, to study the impact of bot engagement on human users and the impact of changes in financial reward on user engagement. Interestingly, our findings demonstrate that while increased engagement by bots is positively associated with engagement by human users, the association between bot engagement and human user engagement decreases as the number of votes for a post increases. We also find that shifts in economic incentives significantly influence the behavior of both human users and bots. This research provides significant insights on how social media platforms can leverage economic incentives to influence user behavior and, more importantly, leverage bots’ activity to increase the engagement of their human users.

## KEYWORDS

Blockchain; social media networks; bots; user engagement; online social media; online incentives; Steemit; PVAR model; RDiT model

## Introduction

Online social networks (OSNs) play an important role in content delivery, information exchange, and connecting people. Well-known OSNs such as Facebook and Twitter are currently dominating the market. Despite their many benefits, they are, however, hindered by a series of important challenges. While these platforms provide an opportunity for users to communicate freely, they do not provide any direct economic incentives for users to contribute to the platform and participate in faithful exchanges [18, 63]. This would, in part, lead to the prevalence of inaccurate information on traditional social media platforms as users do not have significant incentives to help the platform curb the malicious content [34]. Privacy leakage is another major challenge of traditional social media platforms, caused primarily by their central data management mechanisms [54].

Blockchain technology, with explicit features such as decentralization, immutability, transparency, and security, has the potential to solve the current problems of OSNs and introduce a new generation of platforms known as blockchain online social media (BOSM) platforms. For example, the peer-to-peer exchange capability of blockchain networks coupled with smart contracts can allow users to take full control of their data and their potential sale to third parties, effectively solving many of the problems with privacy leakage [14, 40]. Most importantly, many BOSMs such as Steemit and Sapien, provide economic incentives through cryptocurrency tokens to encourage users to contribute to the platform [35]. Given the capability of incentivized BOSMs to address the major challenges of their traditional counterparts, they are very likely to emerge as a significant form of social media in the near future [44].

A unique advantage of incentivized BOSMs is their ability to influence the behavior of both human users and bots by shifting the incentive structure for creation and curation of content. While traditional OSNs must rely on their users’ intrinsic incentives to create content and popularize content on their platforms, the incentivized BOSMs can directly influence the behavior of their users by providing financial incentives that are targeted toward shifting the creation or curation of content.

A more interesting aspect of such incentives is their impact on the behavior of algorithmic agents, hereafter “bots.” Bots in traditional OSNs play an important role in spreading inaccurate information and low-quality content by voting for a large number of posts [10]. However, the introduction of cryptocurrency rewards in conjunction with the special design of the incentivized BOSM platforms changes the incentive structure of the bots, leading them to operate differently in BOSMs. Instead of being utilized for spreading inaccurate information and low-quality content, bots in incentivized BOSMs are employed to earn rewards by engaging in voting activities [47]. Given that the bots in incentivized BOSMs operate under a completely different structure of economic incentives, their behavior and their subsequent impact on human users are not yet known. Also, despite these important features, the impact of such economic incentives on the behavior of human users and bots and their interlinked effects on one another have not been studied before.

This study aims to fill the two gaps previously described by conducting two empirical studies. First, we examine the dynamic relationships between bots and human users and study if and how bots and human users influence each other’s behavior in a social media environment with an economic incentive structure in place. Second, we explore how changes in the economic incentives for the creation and curation of content influence the behavior of bots and human users.

To address these research questions, we collect two different data sets from Steemit, the largest and most popular BOSM. We conduct two major empirical investigations. First, we use a panel vector autoregression (PVAR) model with exogenous variables and unobserved fixed individual effects to examine the dynamic effects of bots and human users on each other. Second, we take advantage of a policy shift by Steemit in their reward structure and implement a regression discontinuity in time (RDiT) analysis to examine how shifts in economic rewards influence the behavior of bots and humans. Furthermore, we provide empirical evidence to shed light on the mechanism of influence between humans and bots.

Our empirical analysis shows that bots’ presence in Steemit is positively associated with human users’ engagement. In particular, although traditional social media ecosystems have mostly experienced negative effects of bots on both human users and the platform, bot intervention in a post increased human user engagement in Steemit. In addition, we find that an increase in the number of votes for a post moderates the impact of bots’ engagement on human users’ engagement. That is, when it comes to voting for popular posts that have already attracted the attention of other users, Steemit’s current voting system does not allow subsequent voters to generate considerable curation rewards.

Our examination of the effects of shifting the economic incentives policy (which consists of decreasing rewards for the creation of content but increasing rewards for the curation of content) yields interesting insights. We show that the voting activity of bots decreases. We hypothesize that such effects are due to the economic incentives of bots and the reduction in the number of published posts by authors. They receive payments from human users to vote for specific posts created by humans. With fewer incentives to create content, human users are less likely to pay for bots’ votes, and the market for their services is disrupted. By analyzing the suspicious payments from human users to bots, we also show that such payments follow the same trend, essentially corroborating our proposed mechanism of impact. We also find that this change in the incentives does not have an impact on human users’ voting activity; however, as expected, it reduces the volume of content published by human users.

Our research contributes to the current knowledge of algorithmic agents in blockchainbased social media platforms that incentivize users for valuable contributions. While bots have the potential to spread false information or phishing scams, we demonstrate that a well-designed economic incentive system can result in net positive impacts by increasing user participation. We argue that bots are not inherently problematic, and it is the way in which they are incentivized that determines their impact.

The majority of research on bots in incentivized blockchain-based social media platforms focuses on their detection [45, 47]. However, in this study, we look at the consequences of bots on these platforms by studying the dynamic interactions between humans and bots. Our research also adds to the body of knowledge on user engagement in social media platforms. There are many internal and external factors that influence user engagement in online communities, such as content characteristics and activity level of other users, but in this work, we focus on one of the main characteristics of the incentivized BOSMs, their reward system, to determine its impact on the engagement of different types of users, including human and bot users.

## Context

We introduce Steemit, an incentivized BOSM platform. We discuss the main elements of Steemit’s design, including its token economy and reward mechanism. We also study its design challenges and the presence of bots in its ecosystem.

## Steemit

Steemit was launched in May 2016 and is built upon the Steem blockchain. Among the current incentivized BOSMs, Steemit is the most popular, with a market capitalization of around 399 million USD on April 10, 2021 (https://steemd.com/). On Steemit, users can perform more than thirty different types of operations and engage in various social and financial activities, such as publishing and voting on posts and transferring cryptocurrency [47]. The Steem blockchain, the publicly accessible distributed ledger, was used to store all the operations performed by users as a chain of blocks. Unlike Bitcoin and other blockchains, which only store the currency they generate, the Steem blockchain stores content too. Figure 1 shows an example of recorded data in one of Steem’s blocks.

![](/api/attachments/9DFFN5WJ/fulltext/images/71ff80fa8a8bab947f4bb54599de65810625cc08c2d23d4206f7f4a9daa40970.jpg)  
Figure 1. Example of recorded data in one of Steem’s blocks.  
Source: From STEEM Block Explorer, available at the following URL: https://steemblockexplorer.com/.

Steemit aims to reward users who generate and curate high-quality content with its native cryptocurrency, STEEM, in order to create fair outcomes for all platform participants and increase user participation [62]. Users can vote on the quality of posts, and Steemit aggregates these votes, weighting them based on the voters’ token holdings and then rewards the posts according to the weighted average. Steemit hopes that economic incentives will aid in creating high-quality content by human users in a decentralized manner.

Every blockchain-based project is governed by a consensus mechanism. There are several protocols for achieving blockchain consensus, including Proof of Work (PoW), Proof of Stake (PoS), and Delegated Proof of Stake (DPoS). The PoW protocol requires block validators to solve a complex mathematical problem, in which the first to solve the problem adds a block to the chain and receives a cryptocurrency reward. In the PoS protocol, block validators are selected randomly, and the probability of agents being drawn is equal to their stake cryptocurrency.

Finally, in the DPoS, block validators or witnesses will be chosen by the community members. Witnesses in DPoS blockchains gather user-generated data, bundle it into some blocks, and append new blocks to the existing ones. Steemit is governed by a DPoS consensus mechanism and operated by 21 witnesses. Steemit allows witnesses to be scheduled to produce blocks every 3 seconds [62].

## Steemit Token Economy

Steemit is a multi-token economy that consists of three financial instruments: STEEM, Steem Power, and STEEM Blockchain Dollars (SBD) [41]. STEEM is Steemit’s native cryptocurrency. It is a liquid and tradeable cryptocurrency, similar to bitcoin, and its value changes based on supply and demand. Steem Power is yet another cryptocurrency in Steemit that provides users with a stake in the platform and serves as a long-term investment. Steem Power, in other words, is a measure of a user’s influence in the Steem network. The more Steem Power users owned, the more their influence was on their votes for Steemit [13]. Overall, users who hold Steem Power are the primary investors in the platform, and they wield significant influence by voting on posts and participating in witness elections. As such, they play a critical role in the platform’s sustainability, and the quality of their decisions directly affects the platform’s success.

Each Steem Power is assigned about 2000 vested shares (VESTS) of Steemit. SBDs are stable-value tokens planned to be equal to \$1 USD. “SBDs were designed to bring stability to the world of cryptocurrency and to the individuals who use the Steem network [13, p. 7].”

STEEM, Steem Power, and SBD can be purchased and/or earned by posting and voting in Steemit. Users can also trade various tokens in both the internal and external markets. Users can acquire STEEM, Steem Power, and SBD using other cryptocurrencies via external markets. Users can also earn STEEM, Steem Power, and SBD by posting and voting on Steemit. Steem Power and SBD can also be converted to STEEM in the internal market. Steem Power can be converted to STEEM through a process known as “powering down” that lasts 13 weeks, and SBD can also be converted to STEEM over 3.5 days. STEEM also could be immediately converted to Steem Power through the “powering up” process. Figure 2 shows Steemit’s currency system.

Steemit has an uncapped structure, meaning there are no token supply constraints [26]. Every day, new STEEM tokens are created. “Since December 2016, Steemit began creating new tokens at an annual inflation rate of 9.5%. The inflation rate decreases at a rate of 0.01% every 250,000 blocks, or about 0.5% per year” [62, p. 26]. Seventy-five percent of the newly generated tokens fund the reward pool, which is split between authors and users who vote on posts. Users who vote on posts (voters) are referred to as curators on Steemit. Steem

![](/api/attachments/9DFFN5WJ/fulltext/images/196370459d041fe3cd9fbe8f4d1a6c74b4c6a5e67de63923d1c134d034efc896.jpg)  
Figure 2. Steemit currency system (adapted from Casadesus-Masanell et al. [13]).

Power holders will receive 15 percent of the new tokens. The remaining 10 percent pays for the witnesses who help to power the blockchain [62].

## Steemit Reward Mechanism

To encourage post authors and curators to create and vote for high-quality content, a large portion (75 percent) of newly generated tokens is added to the reward pool. When an author publishes a post on Steemit, others can upvote or downvote it, just like on other OSNs such as Reddit. Unlike other OSNs, the vote of each voter, hereafter called “curator” has a weight that depends on the curator’s characteristics including her voting power, voting weight, and vesting shares (VESTS). As we explained earlier, the VESTS of each curator depend on the number of Steem Power that she holds. Each Seem Power is assigned about 2000 VESTS. In the following, we define the concepts of voting power and voting weight.

## Voting Power

Unlike other OSNs where voters do not have limitations on the number of posts for which they vote, Steemit has a restriction that is imposed on an account’s ability to vote, and it is called voting power. The logic behind having this voting power element is to limit the number of votes that users can cast per day, which is one of Steemit’s strategies to highlight high-quality posts and prevent everyone from bestowing unlimited rewards. Thus, the user is allocating a fixed set of resources on Steemit. The higher is a curator’s voting power, the stronger is its vote. Voting power is analogous to a large tank of water. Every time a curator casts a vote, a valve at the tank’s bottom opens and squirts out some power. The fuller is the tank, the more power squirts out of the valve. The amount of power that squirts out of the valve is one factor that determines how powerful the curator’s vote is.

## Voting Weight

The voting weight indicates the strength of a curator’s vote. If a curator holds at least one million VESTS, when voting, she can vote at any percentage between 1 and 100, with 100 being the most powerful. The curator can adjust the strength of her vote based on how much she likes each post and how many times she wants to vote per day.

When a curator votes on a post, its voting power, voting weight, and VESTS are multiplied to produce a number known as the curator’s reward shares (rshares), which are credited towards the post the curator voted for. Each curator’s rshares represent the curator’s contribution to the post reward. According to Li and Palanisamy [47], each curator (c)’s rshares (rs) to the post i is:

$$
r s _ {c i} = V E S T S _ {c} \times \frac {\left(v p _ {c} \times v w _ {c} - 0 . 0 0 4 9\right)}{5 0},\tag{1}
$$

where ${ \nu } p _ { c }$ and $\nu w _ { c }$ stand for a curator’s voting power and voting weight, respectively. All notations are summarized in Table 1.

Holding all other factors constant, including voting weight and voting power, a curator who owns more VESTS contributes more rshares by her vote. Next, we provide an example to make the above statement more clear. Depending on the number of VESTS Alice owns, the value of her rs on a post will be maximum when her vp = 100 percent. If Alice’s vp is less than 100 percent, her rs will be less. Suppose her rs on a post at $\nu p = 1 0 0$ percent, is \$10. Then, at 50 percent and 25 percent vp, her rs will be \$4.90 and \$2.40, respectively. When Alice upvotes a post, she may not want to vote at her current vp and use only a percentage of it. In (1), vw represents this percentage. Thus, if Alice’s rs is worth \$10 at $\nu p = 1 0 0$ percent and vw = 100 percent, then at $\nu p = 5 0$ percent and $\nu w = 5 0$ percent, her rs is roughly \$2.40.

Table 1. Notations.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td colspan="2">Notations in Equations 1 and 2</td></tr><tr><td> $rs_{ci}$ </td><td>Curator c&#x27;s rshares to post i.</td></tr><tr><td> $VESTS_c$ </td><td>The amount of the vesting shares that curator c owns.</td></tr><tr><td> $vp_c$ </td><td>Curator c&#x27;s voting power.</td></tr><tr><td> $vw_c$ </td><td>Curator c&#x27;s voting weight.</td></tr><tr><td> $p_i$ </td><td>Reward of post i.</td></tr><tr><td>RS</td><td>Monetary reward in the reward pool.</td></tr><tr><td colspan="2">Notations in Equation 3</td></tr><tr><td> $Comment_{ijt}$ </td><td>Total number of comments on post i published by author j at time t.</td></tr><tr><td> $TotalVote_{ijt}$ </td><td>Total number of votes on post i published by author j at time t.</td></tr><tr><td> $BotContribution_{ijt}$ </td><td>Bot contribution on post i published by author j at time t.</td></tr><tr><td> $HumanUserContribution_{ijt}$ </td><td>Human contribution on post i published by author j at time t.</td></tr><tr><td> $\xi_i$ </td><td>Vector of unobserved post effects.</td></tr><tr><td> $Y_j$ </td><td>Vector of unobserved author effects.</td></tr><tr><td> $f_t$ </td><td>Vector of time dummies.</td></tr><tr><td> $\varepsilon_{ijt}$ </td><td>Vector of errors.</td></tr><tr><td colspan="2">Notations in Equation 5</td></tr><tr><td> $BTC_t$ </td><td>Bitcoin&#x27;s daily closing price.</td></tr><tr><td>PolicyChange</td><td>Binary variable indicating the shift in policy.</td></tr><tr><td>t</td><td>Linear time trend.</td></tr><tr><td> $x_t$ </td><td>Dummy variable for day of the week.</td></tr><tr><td> $\varepsilon_t$ </td><td>Vector of errors.</td></tr></table>

A post can accumulate rshares from received votes for seven days after post creation. There is a pool of rewards called reward pool that is distributed between posts that have reached the end of their seven-day time window. Every day, the Steem blockchain issues a number of STEEM tokens to the reward pool, and at the end of the seven-day time window, posts compete against each other to split up the monetary reward (number of STEEM tokens × STEEM price on that day) in the reward pool based on the total number of rshares from the received votes [47]. The more rshares a post has in total, the higher its reward. Then the reward of a single post i is calculated as follows:

$$
P _ {i} = \frac {\sum_ {c} r s _ {c i}}{\sum_ {k \neq i} \sum_ {c} r s _ {c k}} \times R S,\tag{2}
$$

where RS is the monetary reward in the reward pool which we defined it before, the numerator of the fraction in (2) is total number of rshares from the received votes for post i, and the denominator is total number of rshares from the received votes for all post that have reached the end of their seven-day time window except i. If a post does not earn any upvotes from Steemit users, it is not rewarded. A post is rewarded if at least one curator votes for it. In contrast to OSNs like YouTube, where content providers were continuously rewarded for new views of their existing videos, Steemit had a limited payout period.

After the post’s reward is determined on Steemit, the author receives 75 percent of the post reward as authorship reward. The remaining 25 percent is considered a curation reward distributed between the author and curators to varying degrees based on how much time had passed from post creation. When a curator upvotes a post within the first 30 minutes of a post’s publication, a portion of the curator’s curation reward is returned to the author.

For example, if Alice votes on a post immediately after it is published, the author receives 100 percent of her curation reward, whereas if Alice votes on the post 6 minutes later, she receives 20 percent of her curation reward and the author receives 80 percent. After 27 minutes, 10 percent of Alice’s curation reward goes to the author of the post and 90 percent goes to Alice, and after 30 minutes or more, 100 percent of Alice’s curation reward goes to Alice [13]. Generally speaking, when Alice votes earlier, her curation reward will be higher. If curators upvote a post before it becomes popular and it subsequently becomes popular, curators would earn more curation rewards than if that post had not done well. In other words, curators who want to earn more curation rewards should vote on posts (after 30 minutes of the post’s creation) that are likely to be voted on by more curators in the future sooner [47]. Finally, the author of an eligible post would receive a combination of STEEM, SBD, and VESTS as rewards, and curators would receive VESTS as their curation rewards [62]. Figure 3 represents a summary of the Steemit reward system.

## Bots in Steemit

Despite Steemit’s claims that asking for money, views, upvotes, and follows is considered plagiarism, spam, and abuse, the literature indicates that there is a lot of bot activity on Steemit. Voting is the primary activity of bots in Steemit. Bots primarily vote to earn rewards, but they can also collect side payments from authors for their vote. Bots can participate in the witness election activity. Bots can also author posts, but this is rather limited.

![](/api/attachments/9DFFN5WJ/fulltext/images/2bd947ca752ceb7da898bd31f7cbfd33605ef2afb6a60bcfc6f4181b8af3cd31.jpg)  
Figure 3. Summary of Steemit reward system.

The issue of bots in traditional social media has been a long-standing problem. Bots in OSNs upvote a large number of posts and spread noncurated content by voting on trending topics and hashtags to reach a larger audience, which in many cases helps in the spread of fake news [10]. However, due to the special design of Steemit, where users have a limitation on the number of posts that they can vote in total, the whole curation process makes it harder for bots to spread misinformation.

However, Steemit’s financial incentives and reward system still encourage a bot to participate in the platform in two ways [47]. The first is getting paid by authors (through the “transfer” operation in Steemit) in exchange for bots’ upvotes. Bots also systematically vote for posts, even when they are not directly paid to receive curation rewards. To ensure that their posts are rewarded, authors must receive upvotes. Some authors may send STEEM to one or more bots for their upvotes. Under such circumstances, because of holding a large number of VESTS, when bots upvote a post, the post’s reward, and visibility increase. This, in turn, encourages human users to contribute more to the post and increase the post’s reward. It is worth noting that these transactions provide bots with even more vesting shares via the curation reward earned by voting for the post. The second reason for bots’ contribution to a post is similar to human users. In particular, bots are incentivized to vote for a post that is likely to garner greater rewards [36].

## Summary

Steemit is an incentivized BOSM built upon the Steem blockchain that aims to support social media by rewarding users who create and curate high-quality content with cryptocurrency in a decentralized way. Steemit is designed to address the major issues in the traditional OSNs, including lack of quality content and user participation, and through this process, it plans to create a currency that is able to reach a broad market. Steemit is governed by the DPoS consensus mechanism, and the community elects 21 witnesses to bundle all user-generated operations in blocks.

Steemit has three different tokens: STEEM, Steem Power, and SBD. STEEM is Steemit’s native cryptocurrency. Steem Power is a long-term investment, and users who own more Steem Power have more influence in the platform. SBDs are highly stable tokens that are planned to be equal to \$1 USD. Users can buy different tokens from external markets using other cryptocurrencies such as Bitcoin or earn them by posting and voting in the Steemit network. Users can also trade different tokens in both the Steemit network and external markets.

Steemit rewards both the author and curators of quality content. Every time an author publishes a post, other users can vote (upvote or downvote) the post. Unlike other social media platforms like Reddit, curators’ vote has a weight in Steemit. In other words, when a curator votes for a post, the vote contributes a certain number of rshares to the post, which is a function of the curator’s vesting shares, voting power, and voting weight. A post accumulates rshares from received votes for seven days after post creation, and after a seven-day time window, based on their total number of rshares from received votes, posts compete with each other to split up the reward pool. Unlike traditional OSNs, users have limitations for the number of votes they can cast per day, and they cannot vote for an unlimited number of posts, and after a seven-day time window, posts no longer earn rewards from upvotes.

Due to the financial incentives that Steemit provides for its users, bots exist in its ecosystem. There are many bot accounts with a large amount of Steem Power in Steemit. Other users could pay these bots for their upvotes, resulting in large rewards for the users due to the bots’ high power. Bots will vote for posts even if other users do not directly pay them to do so.

## Background and Related Literature

Our work relates to three themes of literature. First is the blockchain technology and mechanism design of blockchains. Second is the role and impact of bots in usergenerated content platforms. Third is users’ engagement in social media platforms.

The first theme consists of research that explores the growing literature on blockchain technology. A number of authors investigate a variety of organizational impacts that result from the unique technological features of a blockchain that are not typically found in enterprise systems.

Cho et al. [17] examine the impact that the inherent transparency of a blockchain can have on inter-organizational activities and tax fraud. Sarker et al. [56] examine the potential impact of blockchains to reduce corruption in global shipping. Zhang et al. [72] present methods to retain privacy in blockchain-enabled insurance contracts. Liang et al. [48] examine the factors that influence a manager’s decision to utilize blockchain technology.

Other studies in this stream investigate the mechanism design of blockchain-based platforms and their fairness. Benhaim et al. [9] believe core ideas of committee-based consensus should not be undermined because popular blockchains such as Cosmos are relying on them. However, the majority of prior research criticizes the fairness of committee-based blockchain mechanisms (e.g., PoS and DPoS) in terms of their technical design and business model [67]. For example, Fanti et al. [23] and Tsoukalas and Falk [65] show that such mechanisms induce wealth concentration and create potential misalignment between the extent to which agents possess relevant information and hold stakes. Moreover, Kudva et al. [46] show that the mining in blockchain-based networks is more randomized under PoS and PoW mechanisms which threaten networks’ fairness. To show how difficult it is to ensure the fairness of a committee-based blockchain mechanism, Amoussou-Guenou et al. [2] derive its necessary condition that is the detectability of faulty processes (processes that behave arbitrarily). In fact, most committee-based blockchain mechanisms jeopardize fairness by allowing the wealthiest stakeholders to exert control over the majority of blocks, which results in discouraging poorer users from participating [70]. Our exploratory analysis provides additional support for the negative relationship between utilizing the DPoS mechanism and wealth distribution.

The second theme in the literature relates to studies that investigate the role and impact of bots in user-generated content platforms. Empirical evidence indicates bots can affect human users’ behavior when making political, social, and financial decisions [22, 30]. Prior research in this stream can be classified based on their focus on the positive and negative impacts of bots in social media. Social networks and voting sites are the home of millions of social bots, which often adversely affect the performance of such OSNs. By analyzing millions of articles on Twitter, Shao et al. [59] show social bots play a disproportionate role in the spreading of online misinformation and low-quality content. In terms of abusing bots for political purposes, Bessi and Ferrara [10] provide evidence on abusing social bots in the 2016 U.S. presidential election and the harmful impacts of bots on democratic political discussions in online communities.

Due to their automated nature, bots behave differently than humans. Gilani et al. [28] find that bots are much more active than human users; bots retweet messages more often than human users. Gilbert [29] scrutinizes the role of bots in the most famous OSN voting site, Reddit, and show that the presence of bots causes widespread underprovision of votes, which contrasts with the core purpose of Reddit. Conversely, social bots can permeate a social media sphere [4] and facilitate human users’ participation by disseminating news, especially for a social media with limited resources [21]. Due to implemented reward systems in incentivized BOSMs, including Steemit, bots have financial incentives to participate and misuse their reward systems [47]. For example, to generate more revenues, findings in Li and Palanisamy [47] and [36] show a fraction of human users pay bots for their upvotes which is in contrast to Steemit’s envisioned goal that is rewarding high-quality content.

Although prior studies [36, 37, 47] explore the behavior of bots in Steemit, according to our best knowledge, the dynamic relationship between bots and human users has not yet been examined. We contribute to this literature by investigating the impact of bots’ activities on human users and vice versa in the incentivized BOSM, Steemit.

The third theme in the literature consists of the research that investigates users’ engagement in social media platforms. Previous studies identify various internal and external factors affecting user engagement in social media such as content characteristics [1], symbolic awards [25], and the level of other users’ engagement [8]. In comparison to traditional social media, in addition to the aforementioned factors, human users’ engagement in incentivized BOSMs is also affected by implemented rewarding [50] which can entice more users to engage in more activities [18]. Furthermore, the presence of bots in incentivized BOSMs can affect human users’ rewards and, as a result, their engagement.

There are different measurements for user engagement in social networks, such as the number of likes, comments, shares, and clicks on posts. Yang et al. [68] use the number of likes and comments received by posts as measurements for user engagement and investigate how posts’ valence and content characteristics affect customer engagement in Meta’s Facebook. Complementing this stream of work, we investigate how bots’ voting behavior affects human users’ engagement and we measure users’ engagement by the number of rshares they contribute to a post by voting. We also examine how changes in the financial incentives affect the engagement of both humans and bots.

## Hypotheses Development

In this section, we provide two sets of hypotheses. First, we focus on the interlinked effects between bots and human users and theorize how bots can increase engagement by human users. Second, we theorize about the impact of shifts in economic incentives on both bots’ and human users’ content creation and curation activities.

## Dynamic Efects of Bots on Human Users

As stated before, previous studies have explored the impact of bots on OSNs and found both positive and negative outcomes. Bots can improve communication, aid in governance, and efficiently evaluate a large number of works, leading to positive impacts on online communities [58, 64]. The information generated by algorithmic agents can help users process information more efficiently and encourage user participation [39]. Conversely, some studies find that bots demotivate users’ engagement and result in unintended consequences [5, 32, 42].

Traditional social media platforms fail to incentivize users to generate high-quality content and contribute to constructive exchanges, while also lacking mechanisms to penalize or discourage users from creating and sharing low-quality content. This deficiency results in situations where malicious users can spam the platform and disseminate fake news or hate speech without economic consequences. The absence of incentives to create good content and disincentives to create bad content creates opportunities for users with malicious intentions, including those sponsored by adversary states, to exploit bots to amplify their negative impact [6, 11, 38].

BOSMs address both problems by implementing a rewarding and pricing mechanism enabled by cryptocurrency tokens. The existence of such mechanisms in BOSMs can change how bots and human users interact with each other. In this research, we examine how this reward mechanism governs the relationship between bots and humans.

As explained earlier, the reward mechanism in blockchain-based social media platforms encourages users to create and contribute to posts that are likely to be appreciated by others. To limit voting on posts, these platforms impose restrictions on the number of posts that users can vote on, making voting a non-free activity. These mechanisms turn social media activities into a form of investment by providing economic incentives to create and promote good content while discouraging the creation and promotion of bad content. Users aim to maximize their cryptocurrency token returns by investing in high-quality content and avoiding poor-quality content.

Within this framework of economic incentives, bots and human users would both have the same goal of maximizing their returns, yet these two types of users have different capabilities and decision-making processes. Bots can spend all of their time on the platform and therefore contribute to a post at any point during the time, while human users can only allocate a portion of their time on the platform and therefore can contribute to a post only at certain times during the day. Moreover, bots are programmed to contribute to a post based on an algorithm that is designed to identify posts that are most likely to go viral, hence earning the bot a higher return on investment. That is, their decision-making process by design is completely void of emotional cues.

Conversely, while humans also try to maximize their returns, their decision to contribute to a post is based on a heuristic process influenced by psychological cues in their environment. The differences in capabilities and decision-making processes between bots and human users determine how these users interact with and influence each other.

Bots quickly identify potentially viral posts by constantly monitoring the platform. These bots are driven by purely economic incentives to contribute to these posts very early on. In contrast, humans have limited time and cognitive resources, relying on emotional cues and heuristics to monitor content [60].

An important instance of biases that arise in humans’ decision-making process is herding. That is when investors follow the crowd rather than making decisions based on their own independent analysis [7, 19]. The herding behavior in investors has been very well established in finance literature [57]. Following others leads to momentum investment, which Grundy and Martin [33] define as “buying recent winners and shorting recent losers [p. 29].”

To make a decision about contributing to a post, a human is prone to follow the herd and invest in momentum by contributing to the posts that have already garnered a lot of rhsares contributions (which means a lot of post rewards) from a few users. According to Li and Palanisamy [47] because bots tend to hold high Steem Power and vote early, they increase the post’s reward by their upvotes, and the increased reward of the post enhances its visibility and attractiveness of a post to human users. A post that would otherwise have gone unnoticed will be pushed to the top by early bot contributors, increasing its chance of garnering human users’ attention. Therefore, we propose the following hypothesis:

Hypothesis 1 (Engagement Hypothesis) (H1): Increased engagement by bots is positively associated with engagement by human users.

Unlike humans, bots’ decision-making process is less prone to biases from herding and momentum investing due to the fact that all bot actions are programmed. Therefore, an increase in the contributions received by a post would have to be programmed into the bot in order for the bot to contribute to it. On the contrary, as explained earlier, the incentives are structured in such a way that returns on investments decrease as the number of votes cast for a post increases. Moreover, once the number of votes cast for a post increases, its chances to be discovered by other human users increase substantially, alleviating its dependence on bots’ contributions. In summary, we expect the influence of bot contributions on raising the profile of a post to decrease, as more humans already discover it. We therefore propose the following hypotheses:

Hypothesis 2 (Vote Interaction Hypothesis) (H2): The association between bot engagement and human user engagement will reduce as the number of votes for a post increases.

## Efects of Economic Incentives on Users

Motivation theory posits that there are two types of motivations for individuals to participate in online communities: intrinsic and extrinsic [55]. Intrinsic motivation refers to an individual’s internal drive or desire to engage in an activity or task. It is driven by personal interest, enjoyment, and a sense of fulfillment or satisfaction that comes from the activity itself rather than external rewards or pressures.

On the other hand, extrinsic motivation refers to the type of motivation that comes from external factors such as rewards, recognition, or punishment. It is a type of motivation that originates from outside the individual rather than from within. When users participate in an activity for the sake of the external value rather than the enjoyment of the activity itself, their perceived self-determination is undermined. Extrinsic incentives will thus crowd out intrinsic motivations if the former is deemed dominant.

In our case, one of the reasons that users migrate from traditional OSNs to incentivized BOSMs is that they are rewarded for their contributions to the community; thus, extrinsic motivation outweighs intrinsic motivation, and we expect that changes in the reward system significantly change user behavior. If the authorship reward is reduced, authors may feel that the effort required to create and share content is no longer worth the reward, leading to a decrease in their motivation to publish posts.

In other words, we expect reduced authorship reward to reduce the incentive for authors to participate, and hence the number of author posts should decline. Note that since bots are primarily involved in voting activity and do not create much content on the platform, we therefore only hypothesize about the effect of shifting authorship rewards for human users. Formally, we propose the following hypothesis:

Hypothesis 3 (Author Reward-Activity Hypothesis) (H3): Reducing authorship rewards reduces the number of posts generated by human users.

As discussed, earlier curators play a critical role in incentivized BOSM platforms because they are the platform’s primary investors, and the platform’s sustainability is heavily dependent on their investment and the quality of their decisions. Therefore, increasing curator participation is crucial for the platform’s success, and one way to do so is by offering additional financial incentives for desired actions.

According to economic theory, rational individuals are utility-driven, which means that financial incentives should affect people’s behavior. Therefore, if the platform increases the curation reward, we expect more curators to vote and more investors to enter the scene. As the potential reward for an action is increased, individuals may perceive that the benefits outweigh the costs, and thus they are more likely to engage in that behavior.

For example, if the platform increases the financial reward for curating content, curators may believe that the benefits of performing curation outweigh the costs (e.g., the time and effort required to curate content). This may encourage curators to increase their activity on the platform, resulting in increased engagement.

Consistent with our expectation, multiple studies have shown that even small changes in financial incentives are effective at stimulating behavior online [12, 24, 43]. As a result, we anticipate that the voting activity of both types of curators, bots, and human users would increase because of the increase in curation reward. Therefore, we assert the following hypotheses:

Hypothesis 4a (Curation Reward-Human Voting Hypothesis) (H4a): Increasing curation rewards increases the number of votes by human users.

Hypothesis 4b (Curation Reward-Bot Voting Hypothesis) (H4b): Increasing curation rewards increases the number of votes by bots.

Conversely, the reduction in authorship reward is expected to decrease the total number of posts which can influence users’ voting activity. According to network effect theory, the utility of users from voting activities increases with the total number of posts. In fact, because the number of posts has a significant impact on the overall experience for curators, as the total number of posts decreases, users have fewer options to vote on, and hence the overall utility of voting activities decreases. In other words, if the total number of posts were to decrease, then the total number of votes by human users and bots may also decrease. Therefore, one can expect that the reduction in authorship reward leads to a decrease in the number of votes by human users and bots.

The reduction in the authorship reward also has another impact on bots’ voting activity on the platform. As discussed earlier, the bots on incentivized BOSMs primarily operate with the objective of maximizing their financial rewards. One stream of revenue for these bots is generated from the pool of human users who want to maximize their authorship rewards and thus pay bots to upvote their posts. Because of the decrease in authorship reward, we expect that the authors who have been paying bots for their upvotes will have less incentive to continue buying votes from bots, effectively disrupting the market for bot votes.

Therefore, we can hypothesize that a reduction in authorship rewards decreases the number of votes by bots. It is important to note that we propose the payments from human users to bots as the underlying mechanism of impact. We, therefore, propose that the reduction in authorship rewards reduces the suspicious payments from human users to bots. Based on the above explanations, we assert the following hypotheses:

Hypothesis 5a (Author Reward-Human Voting Hypothesis) (H5a): Reducing authorship rewards decreases the total number of votes by human users.

Hypothesis 5b (Author Reward-Bot Voting Hypothesis) (H5b): Reducing authorship rewards decreases the total number of votes by bots.

Hypothesis 5c (Reward-Suspicious Payments Hypothesis) (H5c): Reducing authorship rewards decreases the suspicious payments from human users to bots.

We also explain the process mechanics of the relationships in Online Supplemental Appendix A.

## Data

We collected two sets of data to study the impact of bots and change in the reward mechanism on user engagement. Next, we explain the details of each data set.

## Data for Bots

The data collection procedure for the first data set involves several steps. First, in order to detect bots, we collected 5,127,498 operations, including filtered transfer, comments, and vote operations performed by Steemit users from the Steem-blockchain’ Application Programming Interface (API) (https://developers.steem.io/). Because some bots offer their services in their bios, we also retrieved personal information for 30,376 users to further discern between bots and human users.

Following Li and Palanisamy [47], we identified 483 bots by investigating the temporal correlation between transfer and vote operations. We specifically detected all transfer operations and filtered out those that only contain a link to a post published by the sender of a transfer operation in their “memo” areas (where the sender can send a brief message to the recipient of the transfer operation). If the recipient of the transfer operation votes for the post that its information is provided in the memo area, this can be interpreted as a suspicious trade between the post author and a voting bot. In other words, the recipient of the transfer operation is suspected of being a bot. Furthermore, we found 42 additional bots by examining the frequency of comments with the same and suspicious content from authors who advertise their voting services to many people at the same time.

Finally, examination of users’ biographical information results in the identification of 26 more bots. In total, we found 551 users as bots. Note that we collected all of the operations performed by users on the platform in the sample period and therefore we were not concerned with selection bias.

Next, we gathered a data set consisting of information about posts and users from Steemit’s API over a period of eight months (September 2020 to April 2021). Our data set included 930,363 posts published by 40,588 authors, of which 23,690 posts are authored by bots, and 906,637 are authored by human users. Of the 930,363 posts, 349,109 are affected by bot voting, 475,965 are affected only by human voting. 105,289 had neither bot nor human voting and are excluded from our data set because they are irrelevant to our research. Thus, bots engage in more voting activities relative to authoring activities. For each of the 825,074 posts affected by bots’ and/or human users’ voting, we collected the total number of comments, the total number of votes, post’s reward, curators’ rshares contribution, and the amount of curation rewards that they have earned from voting to the post. Using our dataset, we also compared bot and human activity (see the Online Supplemental Appendix B).

To examine the dynamic relationship between bots and human users, we randomly selected the total number of 33,214 posts published by 10,028 authors from our data set, including the total number of 825,074 posts. Our sample consists of full information of each post during the seven-day time window that a post can accumulate rshares from curators, including each curator’s rshares contribution to a post and the total number of comments and votes at the exact time (with dates, hours, minutes and seconds) a curator voted for the post. Table 2 presents summary statistics of our sample. Table 2 shows the mean values (Mean) standard deviation (SD), minimum value (Min), and maximum value (Max) of the variables.

## Comment<sub>ijt</sub>

This variable shows the cumulative number of comments on post i that is published by author j at time t, when a curator votes for a post. Both human users and bots can put comments on posts. More comments can be an indicator of a post’s popularity.

## TotalVote<sub>ijt</sub>

This variable is the total number of votes for post i published by author j at time t, when a curator votes for a post. Bots and human users can upvote a post if they find it valuable and downvote it if they think it is spam or low-quality.

Table 2. Summary statistics for first data set.

<table><tr><td>Variable</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>Comment</td><td>2.918</td><td>7.492</td><td>0</td><td>412</td></tr><tr><td>TotalVote</td><td>30.108</td><td>70.001</td><td>1</td><td>977</td></tr><tr><td>BotContribution</td><td>1.72</td><td>8.67</td><td>-4.63</td><td>810</td></tr><tr><td>HumanUserContribution</td><td>0.21</td><td>0.69</td><td>-21.2</td><td>233</td></tr></table>

Table 3. Summary statistics for second data set.

<table><tr><td rowspan="2">Variable</td><td colspan="4">Before change</td><td colspan="4">After change</td><td rowspan="2">P-value</td></tr><tr><td>Mean</td><td>SD</td><td>Min</td><td>Max</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>log (Total number of posts)</td><td>4.02</td><td>0.02</td><td>3.97</td><td>4.05</td><td>3.95</td><td>0.03</td><td>3.89</td><td>4.03</td><td>&lt; 0.001</td></tr><tr><td>log (Total number of human votes)</td><td>5.70</td><td>0.02</td><td>5.66</td><td>5.74</td><td>5.66</td><td>0.02</td><td>5.62</td><td>5.70</td><td>&lt; 0.001</td></tr><tr><td>log (Total number of bot votes)</td><td>3.87</td><td>0.03</td><td>3.81</td><td>3.92</td><td>3.79</td><td>0.05</td><td>3.68</td><td>3.85</td><td>&lt; 0.001</td></tr><tr><td>log (Total number of suspicious transfers)</td><td>3.46</td><td>0.06</td><td>3.31</td><td>3.55</td><td>3.17</td><td>0.06</td><td>3.09</td><td>3.30</td><td>&lt; 0.001</td></tr><tr><td>log (Total dollar value of suspicious transfers)</td><td>7.79</td><td>0.10</td><td>7.61</td><td>7.99</td><td>7.52</td><td>0.15</td><td>7.11</td><td>7.82</td><td>&lt; 0.001</td></tr><tr><td>log (BTC)</td><td>4.03</td><td>0.03</td><td>3.98</td><td>4.08</td><td>4.00</td><td>0.03</td><td>3.91</td><td>4.03</td><td>&lt; 0.001</td></tr></table>

Note: All variables are calculated per day at the platform level.  
P-values test the comparison of whether the means before and after the change are statistically diferent.

## BotContribution<sub>ijt</sub>

This variable is a bot’s rshares contribution to post i published by author j at time t. As mentioned previously, each time a bot votes for a post, it contributes a certain number of rshares to that post. If a bot upvotes (downvotes) a post, the amount of its rshares contribution to that particular post would be positive (negative). Bot’s rshares contribution to a post can also be zero. Once bots’ voting power drops to 0 percent, they do not contribute to posts by their voting.

## HumanUserContribution<sub>ijt</sub>

This variable is a human user’s rshares contribution to a post. Following the same logic utilized to explain BotContribution, this variable can take positive, negative, and zero values.

## Data for Change in Incentive Mechanism

We additionally seek to analyze the impact of a change in the reward incentive mechanism on user engagement, and for this, we collected a second set of data. We gathered posts, votes, and transfer operations between July 22, 2019 and October 3, 2019. Because we could not collect data on September 2, 2019 due to API maintenance, we removed that day from our data set. In total, our dataset contains 692,488 posts, 34,136, 918 votes, and 2,442,886 transfer operations. On August 27, 2019, the platform introduced a new policy. With this new policy, the Steem reward pool distributed daily to content creators and curators was reduced by 10 percent (it was 75 percent before the policy change and 65 percent after the policy change). The rewards for content creators were reduced by 25 percent to 50 percent of the total post reward, while the rewards for content curators increased by 25 percent to 50 percent of the total post reward. The platform’s rationale for making these changes was to increase the incentives for curators, who are the platform’s primary investors, to invest and participate more in the platform.

We treat this policy change as a natural experiment that provides an exogenous shock to the platform. Table 3 includes summary statistics of the data. The variables include the total number of posts, total number of human votes, total number of bot votes, total number of suspicious transfers, and the total dollar value of suspicious transfers. We also include the closing Bitcoin (BTC) price as a control variable. All variables are in log form, and we observe that the difference in the average of all variables is statically significant and lower after the policy change. Table 3 shows the Mean, SD, Min and Max values for the variables, as well as the P-value for the test of significance for the difference in the Mean values.

## Empirical Study

## Model Specification for Bots Involvement

We applied a PVAR model with exogenous variables and unobserved fixed effects to examine the dynamic relationship between human users’ and bots’ engagement in a sample of 33,214 Steemit posts.

On the one hand, the PVAR models benefit from both the vector autoregression (VAR) model and the panel data set’s structure, so they are useful for investigating dynamic relationship and have been used in previous information systems (IS) research [49, 53, 61, 66]. The PVAR models allow us to endogenize the main variables without requiring additional explanatory variables to capture the short-term and long-term relationships and interdependencies among these variables.

Additionally, PVAR models enable the inference of reciprocal relationships between endogenous variables and ensure the robustness of the model to issues of nonstationarity, spurious causality, endogeneity, serial correlation, and reverse causality [31]. The availability of panel data also allows us to control for unobserved individual and post heterogeneity and utilizes instruments within the model such as lagged dependent variables in the generalized method of moments (GMM) estimation to obtain consistent estimates [15, 51].

On the other hand, the PVAR models also have some limitations. First of all, as the number of endogenous variables or lags increases, so does the number of parameters, resulting in inefficiencies in the estimation approach. Second, the GMM estimator can be a disadvantage compared to the instrumental variable approach that utilizes exogenous instruments [15].

We adopt the reduced form of VAR models in which each dependent variable is a linear function of its own past values, the past values of all other dependent variables, the set of exogenous variables, and the error term. Thus, our PVAR model specification is the following:

$$
\begin{array}{c} y _ {i j t} = \binom {\text {Human User Contribution} _ {i j t}} {\text {Bot Contribution} _ {i j t}} = \sum_ {s = 1} ^ {p} \psi_ {s} \binom {\text {Human User Contribution} _ {i j t - s}} {\text {Bot Contribution} _ {i j t - s}} + \\ \beta_ {1} \text {Comment} _ {i j t - 1} + \beta_ {2} \text {TotalVote} _ {i j t - 1} + \xi_ {i} + \gamma_ {j} + f _ {t} + \varepsilon_ {i j t}, \end{array}\tag{3}
$$

where i indexes post, j indexes author, and t indexes time that a curator (bot or human) has voted for the post i; $\gamma _ { i j t }$ is a two-element column vector, containing the dependent variables; $\psi _ { s }$ are $2 \times 2$ matrices of coefficients for s-period lagged endogenous variables; and $\boldsymbol { p }$ shows the number of lags. We also include a set of exogenous variables such as $C o m m e n t _ { i j t - l } ,$ , and $T o t a l V o t e _ { i j t - 1 }$ . The $\xi _ { i }$ value is a column vector of unobserved post effects, characterizing posts’ time-invariant attributes. The $\gamma _ { j }$ is a column vector of unobserved author effects, characterizing authors’ time-invariant attributes, and the $f _ { t }$ value is a column vector of time dummies that control for any time effects such as seasonality. We do not account for any remaining unobserved time-varying variables related to a specific post other than the total number of votes and number of comments. However, given that activity on each post lasts only a single week, we believe that it is highly unlikely that there exist other unobserved time-varying factors that can significantly impede our findings. Finally, $\varepsilon _ { i j t } = \big ( \varepsilon _ { 1 , i j t } , \varepsilon _ { 2 , i j t } \big )$ is a two-element vector of errors satisfying the assumption presented in EQ. (4) that means error terms are serially uncorrelated when the appropriate lag (p) is used.

$$
E \left(\varepsilon_ {m, i j t}\right) = E \left(\varepsilon_ {m, i j t} \varepsilon_ {m, i j s}\right) = 0, \quad \forall t \neq s a n d m = 1, 2.\tag{4}
$$

Details regarding the PVAR model estimation procedure are provided in the Online Supplemental Appendix C.

## Model Specification for Change in Reward Mechanism

To study the impact of changes in the financial rewards on human and bot activity, we utilize the RDiT analysis as our empirical strategy. Several studies use RDiT to investigate the causal impact of a policy change [3, 20]. According to Yoo et al. [69] two commonly used econometric models for natural experiments, namely matching with difference-indifference and synthetic control, are not suitable for this study due to two reasons. First, the policy change implemented across the platform occurred at the same time, on the same day, for all. Second, the platform is unique and there is no close competitor in the same market to obtain a suitable control group.

With these limitations, we utilize the RDiT framework as the primary research methodology for this study. By using time as the running variable, RDiT applies the concept of regression discontinuity design (RDD). The date of policy change serves as the discontinuity threshold in RDiT. Although many studies use the global polynomial RDiT framework to analyze the impact of a policy change [16, 20], following Gelman and Imbens [27] we use the local linear specification and triangular kernel function as our primary specification because the estimators for causal effects based on global polynomial suffer from overfitting and can be misleading. The local linear specification is as follows:

$$
Y _ {t} = \beta_ {0} + \beta_ {1} \text { PolicyChange } _ {t} + \beta_ {2} t + \beta_ {3} B T C _ {t} + \beta_ {4} x _ {t} + \varepsilon_ {t}\tag{5}
$$

where the outcome variable, $Y _ { t } ,$ is regressed on PolicyChange<sub>t</sub> which is our primary explanatory variable. PolicyChange is a binary variable that indicates the shift in policy. This variable is equal to 1 if the period is post-implementation of the policy change (August 27, 2019) and 0 (zero) otherwise. The coefficient of the binary variable indicates whether there is a change in the outcome variable after the policy change, where t is a linear time trend. To control for the impact of cryptocurrency market prices, we also control for the daily closing BTC price. Finally, the variable $x _ { t }$ is a dummy variable for the day of the week.

## Results

## Short-term Dynamics of Human Users’ and Bots’ Contribution

Table 4 provides the dynamics among bots’ and human users’ engagement in the short term. To explore how bots’ involvement and other exogenous variables influence human users’ engagement in a post, we first look at the results of our regression model with human user contribution as the dependent variable. We observe some intriguing patterns. Our findings indicate that the previous total rshares contribution by all users (bots and human users) has a significant and positive impact on a human user’s rshares contribution at time t. However, the magnitude of bots’ rshares contribution is greater than that of human users. This result can be explained by bots’ early voting strategy as well as their large amount of Steem Power. When bots cast their votes for a post, the visibility and credibility of the post will increase. We speculate that human users perceive this prominence as a signal about the quality of the post and are more likely to contribute more to that particular post. The results show that we do not have enough evidence to reject the Engagement Hypothesis (H1).

Table 4. PVAR estimation results.

<table><tr><td>Independent variable</td><td>HumanUserContributionijt</td><td>BotContributionijt</td></tr><tr><td> $HumanUserContribution_{ijt-1}$ </td><td>0.571*** (0.057)</td><td>0.025 (0.029)</td></tr><tr><td> $HumanUserContribution_{ijt-2}$ </td><td>0.004 (0.004)</td><td>-0.002 (0.002)</td></tr><tr><td> $BotContribution_{ijt-1}$ </td><td>1.750*** (0.224)</td><td>0.973*** (0.114)</td></tr><tr><td> $BotContribution_{ijt-2}$ </td><td>-0.009* (0.005)</td><td>-0.008*** (0.003)</td></tr><tr><td> $Comment_{ijt-1}$ </td><td>-0.009*** (0.003)</td><td>0.001 (0.001)</td></tr><tr><td> $TotalVote_{ijt-1}$ </td><td>-0.001*** (0.0001)</td><td>0.0001 (0.0001)</td></tr><tr><td>Time Dummies</td><td>Yes</td><td>Yes</td></tr></table>

Note: Standard errors are in parentheses.  
\*p < 0.1. \*\*p < 0.05. \*\*\*p < 0.01.  
Abbreviations: PVAR, panel vector autoregression.

Table 4 allows us to also examine the potential reverse causality and see if human users’ behavior also impacts bots’ behavior. We do not observe any statistically significant impact from bots on human user engagement, confirming our initial contention that bots are mostly programmed to vote independently from humans. Interestingly, we also observe that prior engagement by bots is correlated with their engagement in the next time periods. While we have not hypothesized about the consecutive impact of bots on each other, such correlation may be the result of a similarity of programming and behavioral rules among bots. Moreover, results suggest that the total number of votes at time t-1 (and the number of comments at time t-1) negatively affect a human user’s contribution at time t because according to Steemit’s reward system, as the number of votes and comments of a post increases, the post’s curation rewards should be divided among more curators, in favor of those who participated earlier. Therefore, curators who cast their votes later earn fewer rewards than those who voted earlier. Not surprisingly, the total number of votes and comments do not impact bot involvement in a post, which can be justified following the same logic utilized to explain the lack of impact of human users’ past rshares contribution on a bot’s rshares contribution.

We test our second hypothesis by analyzing the interaction between users’ engagement and the number of votes a post receives. The results of this analysis are presented in Table 5. We introduce the interaction term between a counter of time (number of total votes) and contribution level by bots in our model. The estimate of this interaction term indicates whether the impact of bot contributions on human users changes over time.

The estimated value of the interaction coefficient is (−0.013, which is the sum of past bot contribution at time t−1 (−0.014) and time t−2 (0.001)) and statistically significant, supporting the Vote Interaction Hypothesis (H2) that as a post garners more total votes, the influence of bots’ contribution on human users decline. As previously discussed, when a post has not yet been noticed by many other human users, the contribution of bots can have a significant impact by raising the profile of a post and attracting human attention to it, causing humans to contribute to it. As more votes are collected from other curators, the impact of bot contributions on human contributions will be reduced because the post has received many votes, and the post reward should be shared among more curators, and the curators who vote late earn less curation rewards. Therefore, human users prefer to invest in other posts rather than this already popular post.

Table 5. PVAR estimation results for interaction efects.

<table><tr><td>Independent variable</td><td>HumanUserContributionijt</td><td>BotContributionijt</td></tr><tr><td> $HumanUserContribution_{ijt-1}$ </td><td>0.552*** (0.041)</td><td>0.087*** (0.020)</td></tr><tr><td> $HumanUserContribution_{ijt-2}$ </td><td>-0.045*** (0.005)</td><td>-0.009*** (0.002)</td></tr><tr><td> $BotContribution_{ijt-1}$ </td><td>1.891*** (0.218)</td><td>0.732*** (0.112)</td></tr><tr><td> $BotContribution_{ijt-2}$ </td><td>-0.070*** (0.006)</td><td>-0.011*** (0.003)</td></tr><tr><td> $Comment_{ijt-1}$ </td><td>-0.019*** (0.003)</td><td>-0.001** (0.001)</td></tr><tr><td> $TotalVote_{ijt-1}$ </td><td>0.008*** (0.001)</td><td>0.003*** (0.001)</td></tr><tr><td> $HumanUserContribution_{ijt-1} \times TotalVote_{ijt-1}$ </td><td>-0.002*** (0.0002)</td><td>-0.0004*** (0.00001)</td></tr><tr><td> $HumanUserContribution_{ijt-2} \times TotalVote_{ijt-2}$ </td><td>0.001*** (0.00004)</td><td>0.0001*** (0.00001)</td></tr><tr><td> $BotContribution_{ijt-1} \times TotalVote_{ijt-1}$ </td><td>-0.014*** (0.002)</td><td>-0.006** (0.001)</td></tr><tr><td> $BotContribution_{ijt-2} \times TotalVote_{ijt-2}$ </td><td>0.001*** (0.0001)</td><td>0.0002*** (0.00003)</td></tr><tr><td>Time Dummies</td><td>Yes</td><td>Yes</td></tr></table>

Note: Standard errors are in parentheses.  
\*p < 0.1. \*\*p < 0.05. \*\*\*p < 0.01.  
Abbreviations: PVAR, panel vector autoregression.

Interestingly, when interaction effects are taken into consideration there is a minuscule but statistically significant impact of previous human users on bot engagement. This tiny effect diminishes towards insignificance as the total number of votes increases. This may indicate the algorithmic logic embedded in some of the bots in the early stages of voting.

In addition, we conduct the impulse response functions (IRFs) analysis (see the Online Supplemental Appendix D), the forecast error variance decomposition (FEVD) analysis (see the Online Supplemental Appendix E), and check the stability of the estimated PVAR (see the Online Supplemental Appendix F).

## Impact of Reward Change on Users’ Engagement

Table 6 reports the RDiT estimates. We discover that the coefficient of the policy change is negative and significant for the total number of posts. As the authorship reward is reduced, authors lose their incentive to publish posts, resulting in a decrease in the number of published posts. This finding supports the Author Reward-Activity Hypothesis (H3).

In terms of the impact of the reward change on human user voting activity, we observe no significant changes. Thus, we cannot support either Curation Reward-Human Voting Hypothesis (H4a) or Author Reward-Human Voting Hypothesis (H5a). Note that H4a advocates for an increase in the total number of human votes, and a decrease for H5a. These results imply that the financial rewards are not significant enough for human curators in light of intrinsic value they derive from high quality content.

Our findings show that the bots’ voting activity was significantly reduced after the policy change. This is consistent with lower authorship rewards resulting in a lower number of published posts and a reduction in author demand to buy votes from bots. Therefore, we cannot support the Curation Reward-Bot Voting Hypothesis (H4b), but our findings support the Author Reward-Bot Voting Hypothesis (H5b). The results also reveal that after the policy change, the total number and dollar value of suspicious transfers between bots and humans decreases. Based on what we hypothesized before, this occurs because the authorship reward has been reduced, making it less profitable for authors to pay bots for upvotes.

Table 6. RDiT estimates.

<table><tr><td></td><td>Total number of posts</td><td>Total number of human votes</td><td>Total number of bot votes</td><td>Total number of suspicious transactions</td><td>Total dollar value of suspicious transactions</td></tr><tr><td>Policy</td><td>-0.056**</td><td>-0.021</td><td>-0.035*</td><td>-0.285***</td><td>-0.222***</td></tr><tr><td>Change</td><td>(0.018)</td><td>(0.013)</td><td>(0.019)</td><td>(0.039)</td><td>(0.059)</td></tr><tr><td rowspan="2">log (BTC)</td><td>-0.428</td><td>0.858***</td><td>2.363***</td><td>0.008</td><td>-0.464</td></tr><tr><td>(0.237)</td><td>(0.205)</td><td>(0.422)</td><td>(0.699)</td><td>(1.411)</td></tr><tr><td>Adjusted R2</td><td>0.901</td><td>0.842</td><td>0.898</td><td>0.957</td><td>0.716</td></tr></table>

Note: Standard errors are in parentheses.  
\*p < 0.1. \*\*p < 0.05. \*\*\*p < 0.01.  
Abbreviations: RDiT, regression discontinuity in time; BTC, Bitcoin.

Thus, demand from authors for these side payments is reduced, and this result supports the Reward-Suspicious Payments Hypothesis (H5c).

It is also interesting to investigate the effect of BTC price on different dependent variables as shown in Table 6. The BTC price, which is a control variable, serves as a proxy for the external cryptocurrency market. It has a significant and positive impact on the total voting activity of both human and bot users. We also observe that the BTC price has no statistically significant effect on the number of posts published by human users, the number of suspicious transfers, and the dollar value of suspicious transactions.

## Discussion

Our study investigates both the impact of bot involvement on human users and the change in the reward mechanism in an incentivized BOSM. Although it is against the policy of Steemit (https://steemit.com/faq.html), some bots are collecting side payments from authors to upvote a post. Such illegitimate contributions are very difficult for human users to detect without significant investments of time and cognitive effort. Thus, suspicious side payments have the potential to distort the information value from the number of votes.

In this research, we investigate how bots’ engagement affects human users’ engagement and discover the following results. Our analysis indicates that bots are incentivized to engage early. More importantly, we find bot involvement in a post encourages human users’ engagement, and that the effect of bot involvement on human user engagement decreases as the popularity of the post increases.

Using an RDiT analysis, we also investigate the effects of shifting the economic incentives policy on human and bot engagement. Our findings show that with the decrease in authorship reward and increase in curation reward, human users’ voting activity does not change. However, bots’ voting engagement decreases, in part due to a decrease in suspicious side payments from authors to bots for a bot’s upvote. We also observe that the total number of posts published by authors decreases significantly, which is in line with reduced economic incentives for authorship.

Note that to motivate the hypotheses in this research, we rely on the economic incentives for bots and human users that are created as a direct consequence of the rewarding and pricing mechanisms of BOSMs. That is, rather than developing hypotheses as functions of the technology itself, we build our hypotheses to predict associations contingent on the existence of these economic incentives (which are a typical feature of BOSMs). This allows our insights to be more generalizable and even apply to traditional social media platforms as long as they also implement similar rewarding mechanisms.

Most BOSMs, including DTube (https://d.tube/), Sapien (https://www.sapien.net work/) and Minds (https://www.minds.com/) employ a similar mechanism to encourage users to participate, publish, and identify high-quality content. Our findings are therefore immediately applicable and generalizable to the current incentivized BOSMs, which are growing in popularity. While the specifics of the economic incentive structures that we analyze are used by Steemit, the basic economic mechanism of reward is common and widely used across a spectrum of incentivized BOSMs. Thus, our examination of the incentive mechanisms used by Steemit is therefore generalizable. We also demonstrate that our findings regarding the impact of bot involvement apply to DTube (see the Online Supplemental Appendix G).

Finally, this research presents a forward-looking and early attempt at theory development for blockchain-based social media technologies. The incentive design mechanisms in these platforms have the potential to emerge as a dominant force in the market.

## Theoretical Implications

While the relationship between bots and human users has been extensively studied in the context of OSNs, we are not aware of any studies on this relationship in the context of incentivized BOSMs. As we discussed in the Introduction section, incentivized BOSMs can implement an economic rewarding mechanism to incentivize users for their faithful contributions. The existence of such a mechanism can be an effective governance strategy for platforms to promote the creation and dissemination of premium content. Given how these incentives change the behavior of bots and humans, it is necessary to examine the interplay between these two types of users in BOSMs where the rewarding mechanism is in place. To the best of our knowledge, this is one of the first studies that examine if and how bots can positively contribute to a social media platform by increasing the engagement from human users.

While previous research has mostly shown that bots have a negative impact on human users on traditional social media platforms, in our study, we present a case where bots have a positive impact on human user engagement due to the presence of a reward system. This study also offers an important insight into how the number of votes that have been cast for a post negatively moderates the relationship between the contributions of bots and human users. As such, the association between contributions from bots and human users declines as the number of votes for a post increases.

Our study also explores how changes in financial incentives affect user engagement, which is a significant question in the world of incentivized BOSMs. While some studies [43, 71] examine how monetary incentives impact the quantity and quality of reviews, the concept of rewarding users with cryptocurrency within the context of social media is unique to incentivized BOSMs. These platforms introduce financial rewards for both content creators and curators, a significant departure from traditional social media. As far as we know, our study is the first to investigate whether and how changes in the reward mechanism affect bot and human user engagement in various types of activities. This research is essential in understanding how to optimize reward mechanisms to boost user participation in incentivized BOSMs.

## Practical Implications

Our results help BOSM practitioners by shedding light on how human users behave in incentivized blockchain-based social media. Algorithmic users such as social bots were initially utilized to support and facilitate human users’ engagement in online communities. Despite extensive discussion on the role of bots in online communities, the question of how bots’ involvement affects human users’ engagement in incentivized BOSMs was previously unanswered.

In contrast to the current perception among social media experts, our analysis indicates a positive relationship between bots and human users’ engagement in voting activities. Therefore, before adopting more stringent bot detection algorithms, BOSM developers are advised to consider the favorable impacts of bots. Bots can assist BOSMs in overcoming the inevitable and enduring challenge of expanding the user base. In fact, bots can increase the value of incentivized BOSMs if their positive impact on human users’ engagement surpasses adverse effects on publishing high-quality posts (if at all negative). It is worth noting that empirical evidence show the positive relationship between bots and human users that is also true in enterprise social media [52]. Thus, although we acknowledge that managers should be aware of mechanisms to alleviate potential negative impacts of bot agents, they should also be aware of the positive impact of properly incentivized bots.

Our study’s findings provide valuable insights for managers of BOSM platforms to optimize the reward system for enhancing user experience and engagement, leading to long-term sustainability. The results suggest that increasing the curators’ share of revenue at the expense of authors does not boost voting activity due to the network effect. This strategy (reducing authorship reward and increasing curation reward) negatively impacts posting activity and fails to affect human users’ voting activity. However, reducing authorship reward disincentivizes authors from pursuing side payments. Thus, BOSM platform managers, like managers everywhere, are faced with a balancing act when setting incentives for authorship and voting behavior.

## Limitations and Future Work

This paper has some limitations, which can be used as potential directions for future research on the role of bots and the reward mechanism in incentivized BOSMs. As previously discussed, providing high-quality content is a primary goal for Steemit. However, side payments from authors to bots for upvotes can harm the platform’s credibility and reduce human participation. Future research can also look into the impact of changes in financial incentives on the quality of posts published by users. It is interesting to see how the reward mechanism change has affected post quality and user activities.

Second, we assert that the use of the PVAR model estimation procedure is not robust to unobserved time-varying variables and therefore its estimates should not be considered as evidence for causality in case such time-varying effects are present. Future studies can potentially use a randomized controlled experiment to further examine whether or not bots involvement results in higher human user engagement.

Third, Bots are not unique to BOSMs like Steemit, and it is unknown if the findings from these systems apply to non-blockchain-based OSNs like Reddit, that offer symbolic rewards to its users to deal with bots’ activities. Addressing these limitations can open up new and productive avenues for future research.

## Disclosure Statement

No potential conflict of interest was reported by the authors.

## Funding

Ram D. Gopal acknowledges funding support from the Gillmore Centre for Financial Technology at the Warwick Business School. Raymond A. Patterson acknowledges funding support from the Haskayne School of Business.

## Notes on contributors

Fatemeh Delkhosh (Fatemeh.Delkhosh@ucalgary.ca) is a Ph.D. student in Business Technology Management at Haskayne School of Business, University of Calgary, Canada. She holds an M.Sc. in Industrial Engineering from Iran University of Science and Technology. Her research interest is in the economics of blockchain, with a particular interest in how to manage and design blockchainbased platforms. Her research generally focuses on the economics of information systems using analytical modeling and econometric methods.

Ram D. Gopal (Ram.Gopal@wbs.ac.uk) is the Information Systems Society’s Distinguished Fellow and a Professor of Information Systems and Management at the Warwick Business School, United Kingdom. His research portfolio spans big data analytics, health informatics, financial technologies, information security, privacy and valuation, intellectual property rights, online market design, and business impacts of technology. His research work has appeared in Management Science, Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Operations Research, INFORMS Journal on Computing, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, and many other journals and conference proceedings.

Raymond A. Patterson (Raymond.Patterson@ucalgary.ca; corresponding author) holds the Haskayne Research Professorship in BTM and serves as the BTM Area Chair at the Haskayne School of Business, University of Calgary, in Canada. His primary research interests include information systems, analytics, and quantitative decision and artificial intelligence technologies. Dr. Patterson has published extensively in premier journals such as Information Systems Research, Journal of Management Information Systems, MIS Quarterly, INFORMS Journal on Computing, Operations Research, Production and Operations Management, and many others.

Niam Yaraghi (Niamyaraghi@miami.edu) is an Assistant Professor of Business Technology at Miami Herbert Business School at the University of Miami and a Non-resident Senior Fellow at the Brookings Institution. Dr. Yaraghi studies the business models and policy structures that incentivize interoperability and sharing of health information among patients, providers, payers and regulators. His research has appeared in leading business journals including Management Science, MIS Quarterly, Information Systems Research, and Production and Operations Management, as well as in the top-tier health policy and informatics journals including Journal of American Medical Informatics Association and Milbank Quarterly.

## References

1. Aaltonen, A.; and Seiler, S. Cumulative growth in user-generated content production: Evidence from Wikipedia. Management Science, 62, 7 (July 2016), 2054–2069.

2. Amoussou-Guenou, Y.; del Pozzo, A.; Potop-Butucaru, M.; and Tucci-Piergiovanni, S. On fairness in committee-based blockchains. arXiv preprint arXiv:1910.09786, 2019.

3. Anderson, M.L. Subways, strikes, and slowdowns: The impacts of public transit on traffic congestion. American Economic Review, 104, 9 (September 2014), 2763–2796.

4. Appel, G.; Grewal, L.; Hadi, R.; and Stephen, A.T. The future of social media in marketing. Journal of the Academy of Marketing Science, 48, 1 (January 2020), 79–95.

5. Ashktorab, Z.; Dugan, C.; Johnson, J.; Pan, Q.; Zhang, W.; Kumaravel, S.; Campbell, M. Effects of communication directionality and AI agent differences in human-AI interaction. Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems, Yokohama, 2021, pp. 1–15.

6. Badawy, A.; Ferrara, E.; and Lerman, K. Analyzing the digital traces of political manipulation: The 2016 Russian Interference Twitter Campaign. 2018 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM). (2018), pp. 258–265.

7. Baddeley, M. Herding, social influence and economic decision-making: Socio-psychological and neuroscientific analyses. Philosophical Transactions of the Royal Society B: Biological Sciences, 365, 1538 (2010), 281–290.

8. Bao, Z.; and Han, Z. What drives users’ participation in online social Q&A communities? An empirical study based on social cognitive theory. Aslib Journal of Information Management, 71, 5 (January 2019), 637–656.

9. Benhaim, A.; Hemenway Falk, B.; and Tsoukalas, G. Scaling Blockchains: Can Committee-Based Consensus Help? arXiv preprint arXiv: 2110.08673, 2021.

10. Bessi, A.; and Ferrara, E. Social Bots Distort the 2016 US Presidential Election Online Discussion. First Monday, 21, 11, 3, 2016, https://firstmonday.org/ojs/index.php/fm/article/ view/7090 .

11. Broniatowski, D.A.; Jamison, A.M.; Qi, S., et al. Weaponized health communication: Twitter bots and Russian trolls amplify the vaccine debate. American Journal of Public Health, 108, 10 (2018), 1378–1384.

12. Cabral, L.; and Li, L. (Ivy). A dollar for your thoughts: Feedback-conditional rebates on eBay. Management Science, 61, 9 (September 2015), 2052–2063.

13. Casadesus-Masanell, R.; White, A.; and Elterman, K. Steemit: A new social media. Harvard Business School Case 720-428, (2019), 34 pp.

14. Chakravorty, A.; and Rong, C. Ushare: User controlled social media based on blockchain. Proceedings of the 11th International Conference on Ubiquitous Information Management and Communication, Beppu, 2017, pp. 1–6.

15. Chen, H.; De, P.; and Hu, Y.J. IT-enabled broadcasting in social media: An empirical study of artists’ activities and music sales. Information Systems Research, 26, 3 (September 2015), 513–531.

16. Chen, Y.; and Whalley, A. Green infrastructure: The effects of urban rail transit on air quality. American Economic Journal: Economic Policy, 4, 1 (2012), 58–97.

17. Cho, S.; Lee, K.; Cheong, A.; No, W.G.; and Vasarhelyi, M.A. Chain of values: Examining the economic impacts of blockchain on the value-added tax system. Journal of Management Information Systems, 38, 2 (2021), 288–313.

18. Choi, T.-M., Guo, S., and Luo, S. When blockchain meets social-media: Will the result benefit social media analytics for supply chain operations management? Transportation Research Part E: Logistics and Transportation Review, 135, (March 2020), 101860.

19. Cote, J.; and Sanders, D. Herding behavior: Explanations and implications. Information Systems Research, 29, 2 (2018), 381–400.

20. Davis, L.W. The effect of driving restrictions on air quality in Mexico City. Journal of Political Economy, 116, 1 (February 2008), 38–81.

21. Edwards, C.; Edwards, A.; Spence, P.R.; and Shelton, A.K. Is that a bot running the social media feed? Testing the differences in perceptions of communication quality for a human agent and a bot agent on Twitter. Computers in Human Behavior, 33, (April 2014), 372–376.

22. Fan, R.; Talavera, O.; and Tran, V. Social media bots and stock markets. European Financial Management, 26, 3 (2020), 753–777.

23. Fanti, G.; Kogan, L.; Oh, S.; Ruan, K.; Viswanath, P.; and Wang, G. Compounding of wealth in proof-of-stake cryptocurrencies. International Conference on Financial Cryptography and Data Security, St. Kitts: Springer, 2019, pp. 42–61.

24. Fradkin, A.; Grewal, E.; Holtz, D.; and Pearson, M. Bias and reciprocity in online reviews: Evidence from field experiments on Airbnb. Proceedings of the Sixteenth ACM Conference on Economics and Computation. Association for Computing Machinery, New York, NY, USA, 2015, p. 641.

25. Gallus, J. Fostering public good contributions with symbolic awards: A large-scale natural field experiment at Wikipedia. Management Science, 63, 12 (December 2017), 3999–4015.

26. Gan, R.; Tsoukalas, G.; and Netessine, S. To infinity and beyond: Financing platforms with uncapped crypto tokens. Research Paper, SMU Cox School of Business, 2021.

27. Gelman, A.; and Imbens, G. Why high-order polynomials should not be used in regression discontinuity designs. Journal of Business & Economic Statistics, 37, 3 (July 2019), 447–456.

28. Gilani, Z.; Farahbakhsh, R.; Tyson, G.; and Crowcroft, J. A Large-scale behavioural analysis of bots and humans on Twitter. ACM Transactions on the Web, 13, 1 (February 2019), 1–23.

29. Gilbert, E. Widespread underprovision on Reddit. Proceedings of the 2013 Conference on Computer Supported Cooperative Work, San Antonio Texas USA: ACM Press, 2013, pp. 803–808.

30. Gorodnichenko, Y.; Pham, T.; and Talavera, O. Social media, sentiment and public opinions: Evidence from #Brexit and #USElection. European Economic Review, 136, (July 2021), 103772.

31. Granger, C.W.J.; and Newbold, P. Forecasting Economic Time Series. Academic Press, Boston, 2014.

32. Grimes, G.M.; Schuetzler, R.M.; and Giboney, J.S. Mental models and expectation violations in conversational AI interactions. Decision Support Systems, 144, (May 2021), 113515.

33. Grundy, B.D.; and Martin, J.S.M. Understanding the Nature of the Risks and the Source of the Rewards to Momentum Investing. The Review of Financial Studies, 14, 1 (January 2001), 29–78.

34. Guidi, B. When Blockchain meets Online Social Networks. Pervasive and Mobile Computing, 62, (February 2020), 101131.

35. Guidi, B.; Clemente, V.; García, T.; and Ricci, L. A Rewarding Model for the next generation Social Media. Proceedings of the 6th EAI International Conference on Smart Objects and Technologies for Social Good, New York, NY, USA, 2020, pp. 169–174.

36. Guidi, B.; and Michienzi, A. Users and Bots behaviour analysis in Blockchain Social Media. 2020 Seventh International Conference on Social Networks Analysis, Management and Security (SNAMS), 2020, pp. 1–8.

37. Guidi, B.; Michienzi, A.; and Ricci, L. A Graph-based socioeconomic analysis of Steemit. IEEE Transactions on Computational Social Systems, 8, 2 (April 2021), 365–376.

38. Hegelich, S.; and Janetzko, D. Are social bots on Twitter political actors? Empirical evidence from a Ukrainian social botnet. Proceedings of the International AAAI Conference on Web and Social Media, Atlanta, 2016, pp. 579–582.

39. Jhaver, S.; Bruckman, A.; and Gilbert, E. Does transparency in moderation really matter? User behavior after content removal explanations on Reddit. Proceedings of the ACM on Human-Computer Interaction, 3, (November 2019), 150:1–150:27.

40. Jiang, L.; and Zhang, X. BCOSN: A blockchain-based decentralized online social network. IEEE Transactions on Computational Social Systems, 6, 6 (December 2019), 1454–1466.

41. Kang, S.; Cho, K.; and Park, K. On the effectiveness of multi-token economies. 2019 IEEE International Conference on Blockchain and Cryptocurrency (ICBC), Seoul, 2019, pp. 180–184.

42. Kang, S.; Liu, X. (Jim); Kim, Y.; and Yoon, V. Can bots help create knowledge? The effects of bot intervention in open collaboration. Decision Support Systems, 148, (September 2021), 113601.

43. Khern-am-nuai, W.; Kannan, K.; and Ghasemkhani, H. Extrinsic versus intrinsic rewards for contributing reviews in an online platform. Information Systems Research, 29, 4 (December 2018), 871–892.

44. Kim, G.H. How will blockchain technology affect the future of the internet? Advances in Computer Science and Ubiquitous Computing: CSA-CUTE 2019. Springer, Singapore, 2021, pp. 289–294.

45. Kim, T.; Shin, H.; Hwang, H.J.; and Jeong, S. Posting bot detection on blockchain-based social media platform using machine learning techniques. Proceedings of the International AAAI Conference on Web and Social Media, California, (May 2021), 303–314.

46. Kudva, S.; Badsha, S.; Sengupta, S.; Khalil, I.; and Zomaya, A. Towards secure and practical consensus for blockchain based VANET. Information Sciences, 545, (February 2021), 170–187.

47. Li, C.; and Palanisamy, B. Incentivized blockchain-based social media platforms: A case study of Steemit. Proceedings of the 10th ACM Conference on Web Science, New York, NY, USA, 2019, pp. 145–154.

48. Liang, T.P.; Kohli, R.; Huang, H.C.; and Li, Z.L. What drives the adoption of the blockchain technology? A fit-viability perspective. Journal of Management Information Systems, 38, 2 (April 2021), 314–337.

49. Lin, Y.K.; Rai, A.; and Yang, Y. Information Control for Creator Brand Management in Subscription-Based Crowdfunding. Information Systems Research, 33, 3 (September 2022), 846–866.

50. Liu, Y.; and Feng, J. Does Money Talk? The impact of monetary incentives on user-generated content contributions. Information Systems Research, 32, 2 (June 2021), 394–409.

51. Love, I.; and Zicchino, L. Financial development and dynamic investment behavior: Evidence from panel VAR. The Quarterly Review of Economics and Finance, 46, 2 (May 2006), 190–210.

52. Meske, C.; Amojo, I. Social bots as initiators of human interaction in enterprise social networks. Australasian Conference on Information Systems, Sydney, 2018.

53. Moqri, M.; Mei, X.; Qiu, L.; and Bandyopadhyay, S. Effect of “following” on contributions to open source communities. Journal of Management Information Systems, 35, 4 (October 2018), 1188–1217.

54. Poongodi, T.; Sujatha, R.; Sumathi, D.; Suresh, P.; and Balamurugan, B. Blockchain in social networking. Cryptocurrencies and Blockchain Technology Applications, 2020, pp. 55–76.

55. Ryan, R.M.; and Deci, E.L. Intrinsic and extrinsic motivations: Classic definitions and new directions. Contemporary Educational Psychology, 25, 1 (January 2000), 54–67.

56. Sarker, S.; Henningsson, S.; Jensen, T.; and Hedman, J. The use of blockchain as a resource for combating corruption in global shipping: An interpretive case study. Journal of Management Information Systems, 38, 2 (April 2021), 338–373.

57. Scharfstein, D.S.; and Stein, J.C. Herd behavior and investment. The American Economic Review, 80, 3 (1990), 465–479.

58. Seering, J.; Flores, J.P.; Savage, S.; and Hammer, J. The social roles of bots: Evaluating impact of bots on discussions in online communities. Proceedings of the ACM on Human-Computer Interaction, 2, New York: ACM Press, (November 2018), 157:1-157:29.

59. Shao, C.; Ciampaglia, G.L.; Varol, O.; Yang, K.C.; Flammini, A.; and Menczer, F. The spread of low-credibility content by social bots. Nature Communications, 9, 1 (November 2018), 4787.

60. Slovic, P. Psychological study of human judgment: Implications for investment decision making. The Journal of Finance, 27, 4 (1972), 779–799.

61. Song, T.; Huang, J.; Tan, Y.; and Yu, Y. Using user- and marketer-generated content for box office revenue prediction: Differences between microblogging and third-party platforms. Information Systems Research, 30, 1 (March 2019), 191–203.

62. Steem, J. Steem: An incentivized, blockchain-based, public content platform. (2017).

63. Stieglitz, S.; Mirbabaie, M.; Ross, B.; and Neuberger, C. Social media analytics – Challenges in topic discovery, data collection, and data preparation. International Journal of Information Management, 39, (April 2018), 156–168.

64. Tsai, W.H.S.; Liu, Y.; and Chuan, C.H. How chatbots’ social presence communication enhances consumer engagement: The mediating role of parasocial interaction and dialogue. Journal of Research in Interactive Marketing, 15, 3 (January 2021), 460–482.

65. Tsoukalas, G.; and Falk, B.H. Token-weighted crowdsourcing. Management Science, 66, 9 (September 2020), 3843–3859.

66. Wang, Y.Y.; Susarla, A.; and Sambamurthy, V. The untold story of social media on offline sales: The impact of Facebook in the U.S. automobile industry. In ICIS 2015 Proceedings, (December 2015). Fort Worth, Texas, United States: Association for Information Systems (AIS), pp. 1–10.

67. Xu, B.; Luthra, D.; Cole, Z., and Blakely, N. EOS: An architectural, performance, and economic analysis. Retrieved June, 11, (2018), 2019. https://blog.bitmex.com/wp-content/uploads/2018/ 11/eos-test-report.pdf

68. Yang, M.; Ren, Y.; and Adomavicius, G. Understanding user-generated content and customer engagement on Facebook business pages. Information Systems Research, 30, 3 (September 2019), 839–855.

69. Yoo, C. (Chang); Khern-am-nuai, W.; Tanlamai, J.; and Adulyasak, Y. Haters gonna hate? How removing downvote option impacts discussions on online forum. Proc. 2020 International Conference on Information Systems (ICIS), Association for Information Systems: Atlanta 2020.

70. Yu, B.; Liu, J.; Nepal, S.; Yu, J.; and Rimba, P. Proof-of-QoS: QoS based blockchain consensus protocol. Computers & Security, 87, (November 2019), 101580.

71. Yu, Y.; Khern-am-nuai, W.; and Pinsonneault, A. When paying for reviews pays off: The case of performance-contingent monetary rewards. Management Information Systems Quarterly, 46, 1 (March 2022), 609–626.

72. Zhang, W.; Wei, C.P.; Jiang, Q.; Peng, C.H.; and Zhao, J.L. Beyond the block: A novel blockchain-based technical model for long-term care insurance. Journal of Management Information Systems, 38, 2 (April 2021), 374–400.
